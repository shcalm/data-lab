"""Build separate monthly Ask/Show Top10 rankings from the complete local archive.

Scores are checked with Algolia, with known high-score omissions checked against
official Firebase. Original values and Chinese guide provenance remain explicit.
Pass --guides for a publication build; omitted guides permit research extraction.
"""
import argparse
import concurrent.futures
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import time
from datetime import datetime, timezone
import urllib.parse
import urllib.request
import zipfile

import duckdb

ROOT = Path(__file__).resolve().parent
helper = next((ROOT.parent / name / 'build_results.py' for name in ('monthly-top20', 'hn-monthly-top20')
               if (ROOT.parent / name / 'build_results.py').exists()))
spec = importlib.util.spec_from_file_location('monthly_ranking_common', helper)
common = importlib.util.module_from_spec(spec)
spec.loader.exec_module(common)
CHANNELS = {'ask': 'Ask HN', 'show': 'Show HN'}
SHOW_PATTERN = r'(?i)^\s*show\s+(hn|yc)\b'


def archive_channel(title, url):
    if re.search(SHOW_PATTERN, title or ''):
        return 'show'
    return 'ask' if not (url or '').strip() else None


def rank_rows(rows):
    ordered = sorted(rows, key=lambda r: (-r['score'], r['time_utc'], r['id']))[:10]
    return [{**row, 'rank': i} for i, row in enumerate(ordered, 1)]


def reconcile_candidates(kind, month, hits, local):
    valid, mismatches = {}, {}
    for hit, checked_at in hits:
        item_id = int(hit['objectID'])
        source = local.get(item_id)
        if not source or source['channel'] != kind or hit.get('points') is None:
            continue
        if int(source['time'].timestamp()) != hit['created_at_i'] or source['time'].strftime('%Y-%m') != month:
            mismatches[item_id] = {'id': item_id, 'channel': kind, 'month': month,
                'archive_time_utc': common.utc(source['time']),
                'index_time_utc': common.utc(datetime.fromtimestamp(hit['created_at_i'], timezone.utc)),
                'index_score': hit['points']}
            continue
        value = {**common.entry(source, hit, checked_at), 'channel': kind,
                 'category_source': 'archive+algolia' if f'{kind}_hn' in hit.get('_tags', []) else 'archive'}
        if item_id not in valid or checked_at > valid[item_id]['checked_at']:
            valid[item_id] = value
    return list(valid.values()), mismatches


def candidate_boundary(ranking, eligible_count, matched_count, response, total_hits):
    if response.get('message'):
        raise ValueError(f"API error must not be treated as an empty month: {response['message']}")
    exhausted = response['nbHits'] <= total_hits
    if not response['hits'] and not exhausted:
        raise ValueError('API pagination ended before all reported candidates; cutoff remains unresolved')
    return (matched_count == eligible_count or exhausted or
            (len(ranking) == min(10, eligible_count) and
             (response['hits'][-1].get('points') or 0) < ranking[-1]['score']))


def next_generic_page(pages):
    last = pages[-1]
    ceiling = last.get('score_ceiling')
    if last['response']['page'] < 9:
        return last['response']['page'] + 1, ceiling
    next_ceiling = last['response']['hits'][-1]['points']
    if next_ceiling == ceiling:
        raise ValueError('A single equal-score bucket exceeds the API limit; cutoff unresolved')
    return 0, next_ceiling


def fetch_month(channel, month, cache, page=0, score_ceiling=None):
    window = f'-points-{score_ceiling}' if score_ceiling is not None else ''
    path = cache / f'{channel}-{month}{window}-{page}.json'
    if path.exists():
        result = json.loads(path.read_text())
        if result['response'].get('message'):
            raise ValueError(f"Cached API error: {result['response']['message']}")
        return result
    year, number = map(int, month.split('-'))
    start = datetime(year, number, 1, tzinfo=timezone.utc)
    end = datetime(year + (number == 12), 1 if number == 12 else number + 1, 1, tzinfo=timezone.utc)
    params = {'tags': 'story' if channel == 'all' else f'story,{channel}_hn',
              'numericFilters': f'created_at_i>={int(start.timestamp())},created_at_i<{int(end.timestamp())}',
              'hitsPerPage': 100, 'page': page}
    if score_ceiling is not None:
        params['numericFilters'] += f',points<={score_ceiling}'
    url = 'https://hn.algolia.com/api/v1/search?' + urllib.parse.urlencode(params)
    for attempt in range(3):
        try:
            request = urllib.request.Request(url, headers={'User-Agent': 'Data-Lab-Ask-Show/1.0'})
            with urllib.request.urlopen(request, timeout=22) as response:
                result = {'channel': channel, 'month': month, 'url': url,
                          'checked_at': common.utc(datetime.now(timezone.utc)), 'response': json.load(response)}
            if result['response'].get('message'):
                raise ValueError(f"API error: {result['response']['message']}")
            if score_ceiling is not None:
                result['score_ceiling'] = score_ceiling
            scores = [hit.get('points') or 0 for hit in result['response']['hits']]
            if scores != sorted(scores, reverse=True):
                raise ValueError(f'{channel}/{month}: candidates not score ordered')
            path.write_text(json.dumps(result, ensure_ascii=False) + '\n')
            return result
        except Exception:
            if attempt == 2:
                raise
            time.sleep(attempt + 1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--index', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=ROOT / 'results')
    parser.add_argument('--cache', type=Path, default=ROOT / 'api-cache')
    parser.add_argument('--guides', type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    args.cache.mkdir(parents=True, exist_ok=True)
    db = duckdb.connect(config={'threads': 2, 'memory_limit': '1536MB'})
    db.execute("SET TimeZone='UTC'")
    db.read_parquet(str(args.index)).create_view('stories')
    db.sql("SELECT *,CASE WHEN regexp_matches(title,$pattern) THEN 'show' WHEN trim(coalesce(url,''))='' THEN 'ask' END AS channel FROM stories", params={'pattern': SHOW_PATTERN}).create_view('categorized')
    total, unique, first, last = db.execute('SELECT count(*),count(DISTINCT id),min(time),max(time) FROM stories').fetchone()
    assert total == unique
    calendar = common.calendar_months(first.strftime('%Y-%m'), last.strftime('%Y-%m'))
    stats = {(kind, month): count for kind, month, count in db.execute("SELECT channel,strftime(time,'%Y-%m'),count(*) FROM categorized WHERE channel IS NOT NULL GROUP BY 1,2").fetchall()}
    requests = {}
    keys = list(stats) + [('all', month) for month in calendar if any(stats.get((kind, month), 0) for kind in CHANNELS)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        jobs = {pool.submit(fetch_month, kind, month, args.cache): (kind, month) for kind, month in keys}
        for done, future in enumerate(concurrent.futures.as_completed(jobs), 1):
            requests[jobs[future]] = [future.result()]
            if done % 40 == 0 or done == len(jobs):
                print(f'Fetched {done}/{len(jobs)} initial channel/general searches', flush=True)

    def archive_matches():
        ids = sorted({int(hit['objectID']) for pages in requests.values() for result in pages for hit in result['response']['hits']})
        db.execute('CREATE OR REPLACE TEMP TABLE candidate_ids AS SELECT unnest(?::BIGINT[]) id', [ids])
        cursor = db.execute('SELECT s.* FROM categorized s JOIN candidate_ids c ON s.id=c.id')
        columns = [d[0] for d in cursor.description]
        return {row[0]: dict(zip(columns, row)) for row in cursor.fetchall()}

    output = {kind: [{'month': month, 'eligible_story_count': stats.get((kind, month), 0), 'entries': [],
                     'ranking_basis': 'empty', 'candidate_boundary_verified': True,
                     'matched_candidate_count': 0, 'search_candidate_count': 0}
                    for month in calendar] for kind in CHANNELS}
    checked_pool, timestamp_mismatches = {}, {}
    # General story candidates cover original-category posts whose current title
    # or channel tag was edited. Batch each pagination round to scan the index once.
    for round_number in range(31):
        local = archive_matches()
        need_more = set()
        for kind in CHANNELS:
            for info in output[kind]:
                month, count = info['month'], info['eligible_story_count']
                if not count:
                    continue
                generic = requests['all', month]
                pages = generic + requests[kind, month]
                hits = [(h, r['checked_at']) for r in pages for h in r['response']['hits']]
                valid, mismatches = reconcile_candidates(kind, month, hits, local)
                timestamp_mismatches.update(mismatches)
                ranking = rank_rows(valid)
                total_generic = sum(len(r['response']['hits']) for r in generic if r.get('score_ceiling') == generic[-1].get('score_ceiling'))
                boundary = candidate_boundary(ranking, count, len(valid), generic[-1]['response'], total_generic)
                checked_pool[kind, month] = {r['id']: r for r in valid}
                info.update(entries=ranking, ranking_basis='algolia' if valid else 'official-pending',
                            matched_candidate_count=len(valid), search_candidate_count=len({int(h['objectID']) for h, _ in hits}),
                            candidate_boundary_verified=boundary)
                if not boundary:
                    need_more.add(month)
        if not need_more:
            break
        if round_number == 30:
            raise ValueError(f'Unresolved generic score cutoff within pagination limit: {sorted(need_more)}')
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            jobs = {}
            for month in need_more:
                page, ceiling = next_generic_page(requests['all', month])
                jobs[pool.submit(fetch_month, 'all', month, args.cache, page, ceiling)] = month
            for future in concurrent.futures.as_completed(jobs):
                requests['all', jobs[future]].append(future.result())
        print(f'Fetched general candidate page {round_number + 2} for {len(need_more)} months', flush=True)

    # Scan complete original category pools for high-score records omitted by
    # search. For underfilled searches check all records, preserving completeness
    # for the earliest sparse months instead of inventing absent entries.
    cutoffs = [(kind, m['month'], m['entries'][-1]['score'] if len(m['entries']) == min(10, m['eligible_story_count']) else 0)
               for kind in CHANNELS for m in output[kind] if m['eligible_story_count']]
    db.execute('CREATE TEMP TABLE cutoffs AS SELECT unnest(?::VARCHAR[]) channel,unnest(?::VARCHAR[]) month_key,unnest(?::BIGINT[]) score',
               [[r[i] for r in cutoffs] for i in range(3)])
    matched_ids = sorted({item_id for pool in checked_pool.values() for item_id in pool})
    db.execute('CREATE TEMP TABLE matched_ids AS SELECT unnest(?::BIGINT[]) id', [matched_ids])
    cursor = db.execute("SELECT s.* FROM categorized s JOIN cutoffs c ON s.channel=c.channel AND strftime(s.time,'%Y-%m')=c.month_key WHERE s.score>=c.score AND NOT EXISTS(SELECT 1 FROM matched_ids q WHERE q.id=s.id) ORDER BY s.time,s.id")
    columns = [d[0] for d in cursor.description]
    omissions = [dict(zip(columns, row)) for row in cursor.fetchall()]
    print(f'Checking {len(omissions)} original above-cutoff omissions with official API', flush=True)
    official = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        jobs = {pool.submit(common.fetch_firebase, row['id'], args.cache): row for row in omissions}
        for future in concurrent.futures.as_completed(jobs):
            row = jobs[future]
            value = {**common.firebase_entry(row, future.result()), 'channel': row['channel'], 'category_source': 'archive'}
            official.append(value)
            checked_pool.setdefault((row['channel'], row['time'].strftime('%Y-%m')), {})[row['id']] = value

    guides = json.loads(args.guides.read_text()) if args.guides else {}
    for kind in CHANNELS:
        for month in output[kind]:
            pool = checked_pool.get((kind, month['month']), {})
            month['entries'] = rank_rows(list(pool.values()))
            official_count = sum(r['score_source'] == 'firebase' for r in pool.values())
            if official_count:
                month['ranking_basis'] = 'algolia+firebase' if month['matched_candidate_count'] else 'firebase'
            month['official_candidate_count'] = official_count
            if len(month['entries']) != min(10, month['eligible_story_count']):
                raise ValueError(f"{kind}/{month['month']}: not enough verified entries")
            for row in month['entries']:
                if args.guides:
                    guide = guides.get(str(row['id']))
                    if not isinstance(guide, str) or not re.search(r'[\u3400-\u9fff]', guide) or '\n' in guide:
                        raise ValueError(f"{row['id']}: missing/invalid Chinese guide")
                    row['guide_zh'] = guide.strip()
            for mismatch in timestamp_mismatches.values():
                if (mismatch['channel'], mismatch['month']) == (kind, month['month']):
                    if not month['entries'] or len(month['entries']) < min(10, month['eligible_story_count']) or mismatch['index_score'] >= month['entries'][-1]['score']:
                        raise ValueError(f"{mismatch['id']}: timestamp mismatch could affect selected ranking")

    selected = [r for kind in CHANNELS for m in output[kind] for r in m['entries']]
    all_checked = [r for pool in checked_pool.values() for r in pool.values()]
    db.execute('CREATE TEMP TABLE checked AS SELECT unnest(?::BIGINT[]) id,unnest(?::VARCHAR[]) channel,unnest(?::VARCHAR[]) time_utc,unnest(?::BIGINT[]) score',
               [[r[k] for r in all_checked] for k in ['id', 'channel', 'time_utc', 'score']])
    verified = db.execute("SELECT channel,substr(time_utc,1,7) AS month_key,id,row_number() OVER(PARTITION BY channel,month_key ORDER BY score DESC,time_utc ASC,id ASC) AS rank FROM checked QUALIFY rank<=10 ORDER BY channel,month_key,rank").fetchall()
    expected = [(kind, m['month'], r['id'], r['rank']) for kind in CHANNELS for m in output[kind] for r in m['entries']]
    assert verified == expected
    assert len(selected) == len({r['id'] for r in selected})
    dates = [r['checked_at'] for pages in requests.values() for r in pages] + [r['checked_at'] for r in official]
    metadata = {'schema_version': 1, 'dataset': 'open-index/hacker-news', 'revision': common.REVISION,
                'dataset_url': 'https://huggingface.co/datasets/open-index/hacker-news', 'license': 'ODC-By-1.0',
                'index_sha256': hashlib.sha256(args.index.read_bytes()).hexdigest(), 'eligible_story_count': total,
                'first_story_utc': common.utc(first), 'last_story_utc': common.utc(last), 'archive_end_utc': '2026-08-23T08:44:12Z',
                'calendar_month_count': len(calendar), 'monthly_limit': 10, 'monthly_entry_count': len(selected),
                'order': ['score DESC', 'time_utc ASC', 'id ASC'], 'timezone': 'UTC',
                'api_checked_from_utc': min(dates), 'api_checked_to_utc': max(dates),
                'api_search_count': sum(len(pages) for pages in requests.values()),
                'score_window_search_count': sum(r.get('score_ceiling') is not None for pages in requests.values() for r in pages),
                'official_candidate_count': len(official), 'official_selected_count': sum(r['score_source'] == 'firebase' for r in selected),
                'guide_count': sum(bool(r.get('guide_zh')) for r in selected),
                'guides_sha256': hashlib.sha256(args.guides.read_bytes()).hexdigest() if args.guides else None,
                'category_rule': 'Ask: original self-posts with no external URL, excluding Show prefixes. Show: original title starts with Show HN or historical Show YC (case-insensitive). Algolia ask_hn/show_hn tags and unrestricted story searches retrieve checked candidates; unrestricted searches continue below each category cutoff, covering removed tags and edited titles. Candidates without a matching current category tag retain category_source=archive.',
                'guide_basis': 'Chinese reading introductions written from original titles and available self-post excerpts, not linked articles or comment threads.',
                'limitations': ['Only eligible stories from the supplied local archive; deleted/dead/untitled there are excluded.',
                               'Scores are query-time checked values, not month-end/final scores or historical HN front-page ranks.',
                               'Ask includes Tell HN, Launch HN and other self-posts, rather than only Ask HN-prefixed questions.',
                               'External index omissions can remain hidden by undercounted original scores; original and current channel categorization can differ.',
                               'Official missing descendants retains archive comments with explicit comments_source; kids length is not total comments.',
                               'Below-cutoff ID/time conflicts are excluded and listed in verification; ranking-affecting conflicts fail export.',
                               'First/last months are partial; early empty and sparse months remain explicit.']}
    channels = {kind: {'id': kind, 'title': CHANNELS[kind], 'path': f'hn/ask-show/{kind}',
                       'eligible_story_count': sum(stats.get((kind, m), 0) for m in calendar),
                       'monthly_entry_count': sum(len(m['entries']) for m in output[kind]),
                       'nonempty_month_count': sum(bool(m['entries']) for m in output[kind]),
                       'months': output[kind]} for kind in CHANNELS}
    canonical = {'metadata': metadata, 'channels': channels}
    common.write_json(args.output / 'rankings.json', canonical)
    verification = {'failure_count': 0, 'monthly_rank_rows_checked_independently_in_sql': len(verified),
                    'calendar_months_per_channel': len(calendar),
                    'canonical_json_sha256': hashlib.sha256((args.output / 'rankings.json').read_bytes()).hexdigest(),
                    'above_cutoff_omissions_checked_officially': sorted(r['id'] for r in official),
                    'changed_score_count': sum(r['score'] != r['archive_score'] for r in selected),
                    'below_cutoff_timestamp_mismatches_excluded': list(timestamp_mismatches.values()),
                    'guide_count': metadata['guide_count'],
                    'raw_api_response_sha256': {p.relative_to(args.cache).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(args.cache.rglob('*.json'))},
                    'rejected_api_responses_preserved': [p.relative_to(args.cache).as_posix() for p in sorted((args.cache / 'rejected').glob('*.json'))]}
    common.write_json(args.output / 'verification.json', verification)
    common.FIELDS = ['channel', 'month', 'rank', 'id', 'title', 'guide_zh', 'author', 'time_utc', 'score', 'comments',
                     'archive_score', 'archive_comments', 'score_source', 'comments_source', 'category_source',
                     'checked_at', 'current_dead', 'current_deleted', 'hn_url', 'url', 'excerpt']
    flat = [{**r, 'month': m['month']} for kind in CHANNELS for m in output[kind] for r in m['entries']]
    common.write_csv(args.output / 'rankings.csv', flat)
    for kind in CHANNELS:
        directory = args.output / kind
        directory.mkdir(exist_ok=True)
        common.write_json(directory / 'rankings.json', {'metadata': metadata, **channels[kind]})
        common.write_csv(directory / 'rankings.csv', [r for r in flat if r['channel'] == kind])
        for month in output[kind]:
            common.write_json(directory / f"{month['month']}.json", month)
            common.write_csv(directory / f"{month['month']}.csv", [{**r, 'month': month['month']} for r in month['entries']])
    description = f'''# Ask / Show 每月 Top10

覆盖原始档案 {metadata['first_story_utc']} 至 {metadata['archive_end_utc']}，共 {len(calendar)} 个连续UTC自然月；Ask和Show各取每月前10，共 {len(selected)} 条。Ask {channels['ask']['monthly_entry_count']} 条，Show {channels['show']['monthly_entry_count']} 条。

按score降序、UTC发帖时间升序、ID升序；评论数不参与排序。取自本地 {total:,} 篇有效主帖，排除原始deleted/dead/无标题记录。来源 {metadata['dataset_url']}，revision `{common.REVISION}`，ODC-By-1.0；内容权利归原作者。索引SHA256 `{metadata['index_sha256']}`。

Ask按原始无外链自帖（不含Show）识别，因此含Tell HN、Launch HN等自帖；Show按原始Show HN或早期Show YC前缀识别，忽略大小写。按Algolia标签ask_hn/show_hn及不限频道的story空查询合并候选，每页100条，ID和精确UTC时间匹配原始档案，再按原始类别取Top10。不限定频道的检索继续到末尾得分低于各频道第10名，同分边界继续翻页；已匹配该月全部原始类别记录或检索穷尽时停止。此方式也覆盖标题修改、当前频道标签被移除的帖子。类别与当前标签不符时category_source=archive。触及每次查询1000条的分页上限时，按上一页末尾分数设置包含等分的points上限，重新分段查询；API错误不作为空结果接受。已穷尽的早期月份如实保留。

另扫描全部原始类别候选中分数达到各月门槛但未被索引召回的记录，用官方Firebase核对ID／时间／类型／得分，共核对 {len(official)} 篇、补入 {metadata['official_selected_count']} 篇；类别仍按原始档案，category_source显式注明。标题／URL保留原始值，当前dead/deleted状态另列。官方缺少descendants时评论数沿用archive_comments，comments_source=archive，未用kids长度作总评论数。

不影响入选边界的ID／时间冲突保留在verification.json，若冲突可能改变榜单则导出失败，须先核对。

补查 {metadata['api_checked_from_utc']} 至 {metadata['api_checked_to_utc']}。score_source/comments_source分别记来源；archive_score/archive_comments保存原始快照。这是查询时得分榜，不能还原月末、最终分数或历史首页排名。搜索索引仍可能遗漏，原始低分可能掩盖更多漏项；原始与当前频道分类也可能不同。首末月仅含存档日期，空月与不足10篇的月份如实保留。

每篇配一句中文导读（guide_zh，共 {metadata['guide_count']} 篇），由模型依据原始标题与已有自帖节选逐条撰写，帮助选择阅读；不概括外链全文或评论区。原题中的观点、疑问和指控保留归属。导读不参与排名。编辑源SHA256 `{metadata['guides_sha256'] or 'not supplied'}`。

文件：rankings.json／csv／md为完整双频道数据；ask/与show/各有独立rankings.json／csv及239个月的JSON／CSV。verification.json保存SQL独立重排、原始响应哈希与数据校验值。hn-ask-show-top10.zip收录全部文件。原始API缓存留在研究目录。

重跑：`python3 scripts/hn-ask-show-top10/build_results.py --index /path/to/all-stories.parquet --output /path/to/results --cache /path/to/cache --guides data/ask-show-guides.json`；需要Python3、DuckDB以及同级hn-monthly-top20辅助脚本。研究项目中的辅助目录名为monthly-top20。刷新使用新缓存，保留旧快照；新入选记录须补齐中文导读。
'''
    (args.output / 'README.md').write_text(description)
    markdown = [description]
    for kind, label in CHANNELS.items():
        markdown.append(f'\n## {label}\n')
        for month in output[kind]:
            markdown.extend([f"\n### {month['month']}\n", common.markdown_table(month['entries']) if month['entries'] else '本月原始档案无该类有效主帖。'])
    (args.output / 'rankings.md').write_text('\n'.join(markdown) + '\n')
    archive_path = args.output / 'hn-ask-show-top10.zip'
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(args.output.rglob('*')):
            if path.is_file() and path != archive_path:
                archive.write(path, 'hn-ask-show-top10/' + path.relative_to(args.output).as_posix())
    print(json.dumps({'metadata': metadata, 'channels': {k: {key: v for key, v in val.items() if key != 'months'} for k, val in channels.items()},
                      'verification': {k: v for k, v in verification.items() if k != 'raw_api_response_sha256'}}, ensure_ascii=False, indent=2), flush=True)


if __name__ == '__main__':
    main()
