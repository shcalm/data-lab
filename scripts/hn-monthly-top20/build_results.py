"""Build monthly HN score rankings, preserving archive values alongside checked values.

The public Algolia HN index supplies score-ordered candidates, restricted to
stories present in the supplied local archive. Raw responses remain cached for
audit. This does not reconstruct HN's time-dependent front-page ranking.
"""
import argparse
import concurrent.futures
import csv
import hashlib
import html
import io
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
DEFAULT_INDEX = ROOT.parent / 'interesting-themes/research/all-stories.parquet'
REVISION = 'c54ced5973b95d80cd934b8921f44ec8d87c3cd1'


def calendar_months(first, last):
    year, month = map(int, first.split('-'))
    result = []
    while f'{year:04}-{month:02}' <= last:
        result.append(f'{year:04}-{month:02}')
        year, month = (year + 1, 1) if month == 12 else (year, month + 1)
    return result


def rank_rows(rows):
    ordered = sorted(rows, key=lambda r: (-r['score'], r['time_utc'], r['id']))[:20]
    return [{**row, 'rank': rank} for rank, row in enumerate(ordered, 1)]


def plain_excerpt(text):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]*>', ' ', text or ''))).strip()[:480].rstrip()


def utc(value):
    return value.astimezone(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')


def fetch_month(month, cache, page=0):
    path = cache / f'{month}-{page}.json'
    if path.exists():
        return json.loads(path.read_text())
    year, number = map(int, month.split('-'))
    start = datetime(year, number, 1, tzinfo=timezone.utc)
    end = datetime(year + (number == 12), 1 if number == 12 else number + 1, 1, tzinfo=timezone.utc)
    params = {'tags': 'story', 'numericFilters': f'created_at_i>={int(start.timestamp())},created_at_i<{int(end.timestamp())}',
              'hitsPerPage': 100, 'page': page}
    url = 'https://hn.algolia.com/api/v1/search?' + urllib.parse.urlencode(params)
    for attempt in range(3):
        try:
            request = urllib.request.Request(url, headers={'User-Agent': 'Data-Lab-monthly-rankings/1.0'})
            with urllib.request.urlopen(request, timeout=22) as response:
                result = {'month': month, 'url': url, 'checked_at': utc(datetime.now(timezone.utc)), 'response': json.load(response)}
            hits = result['response']['hits']
            scores = [hit.get('points') or 0 for hit in hits]
            if scores != sorted(scores, reverse=True):
                raise ValueError(f'{month}: API candidates are not ordered by points')
            path.write_text(json.dumps(result, ensure_ascii=False) + '\n')
            return result
        except Exception:
            if attempt == 2:
                raise
            time.sleep(attempt + 1)


def fetch_firebase(item_id, cache):
    path = cache / f'firebase-{item_id}.json'
    if path.exists():
        return json.loads(path.read_text())
    url = f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json'
    for attempt in range(3):
        try:
            request = urllib.request.Request(url, headers={'User-Agent': 'Data-Lab-monthly-rankings/1.0'})
            with urllib.request.urlopen(request, timeout=22) as response:
                result = {'id': item_id, 'url': url, 'checked_at': utc(datetime.now(timezone.utc)), 'response': json.load(response)}
            path.write_text(json.dumps(result, ensure_ascii=False) + '\n')
            return result
        except Exception:
            if attempt == 2:
                raise
            time.sleep(attempt + 1)


def entry(row, hit=None, checked_at=None):
    return {'id': row['id'], 'title': row['title'], 'author': row['by'] or '', 'time_utc': utc(row['time']),
            'url': row['url'] or '', 'hn_url': f"https://news.ycombinator.com/item?id={row['id']}",
            'score': hit['points'] if hit else row['score'], 'comments': (hit.get('num_comments') or 0) if hit else row['descendants'],
            'archive_score': row['score'], 'archive_comments': row['descendants'],
            'score_source': 'algolia' if hit else 'archive', 'comments_source': 'algolia' if hit else 'archive',
            'checked_at': checked_at, 'current_dead': None, 'current_deleted': None,
            'current_title': hit.get('title') if hit else None, 'excerpt': plain_excerpt(row['text'])}


def firebase_entry(row, result):
    hit = result['response']
    if not isinstance(hit, dict) or hit.get('id') != row['id'] or hit.get('time') != int(row['time'].timestamp()) or hit.get('type') != 'story':
        raise ValueError(f"{row['id']}: Firebase identity/timestamp/type mismatch")
    if not isinstance(hit.get('score'), int) or hit['score'] < 0:
        raise ValueError(f"{row['id']}: missing checked official score")
    has_comments = isinstance(hit.get('descendants'), int) and hit['descendants'] >= 0
    return {**entry(row), 'score': hit['score'], 'score_source': 'firebase',
            'comments': hit['descendants'] if has_comments else row['descendants'],
            'comments_source': 'firebase' if has_comments else 'archive',
            'checked_at': result['checked_at'], 'current_title': hit.get('title'),
            'current_dead': bool(hit.get('dead')), 'current_deleted': bool(hit.get('deleted'))}


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


FIELDS = ['scope', 'month', 'rank', 'id', 'title', 'author', 'time_utc', 'score', 'comments',
          'archive_score', 'archive_comments', 'score_source', 'comments_source', 'checked_at',
          'current_dead', 'current_deleted', 'hn_url', 'url', 'excerpt', 'guide_zh']


def write_csv(path, rows):
    with path.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)


def markdown_table(rows):
    lines = ['| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |', '|---:|---|---|---:|---:|---|']
    for row in rows:
        title = row['title'].replace('|', '\\|').replace('\n', ' ')
        guide = row.get('guide_zh', '').replace('|', '\\|').replace('\n', ' ')
        notes = []
        if row.get('current_dead'):
            notes.append('补查时已标记dead')
        if row.get('current_deleted'):
            notes.append('补查时已标记删除')
        if row['score_source'] != row['comments_source']:
            notes.append('评论数沿用原始快照')
        if notes:
            guide += '（' + '；'.join(notes) + '）'
        lines.append(f"| {row['rank']} | [{title}]({row['hn_url']}) | {guide} | {row['score']} | {row['comments']} | {row['time_utc'][:10]} |")
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--index', type=Path, default=DEFAULT_INDEX)
    parser.add_argument('--output', type=Path, default=ROOT / 'results')
    parser.add_argument('--cache', type=Path, default=ROOT / 'api-cache')
    parser.add_argument('--guides', type=Path, help='Edited ID-to-Chinese-introduction JSON; require complete selected-story coverage when supplied.')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    args.cache.mkdir(parents=True, exist_ok=True)
    db = duckdb.connect(config={'threads': 2, 'memory_limit': '1536MB'})
    db.execute("SET TimeZone='UTC'")
    db.read_parquet(str(args.index)).create_view('stories')
    total, unique, first, last = db.execute('SELECT count(*),count(DISTINCT id),min(time),max(time) FROM stories').fetchone()
    assert total == unique
    stats = {}
    for month, count, high, p99 in db.execute("SELECT strftime(time,'%Y-%m'),count(*),count(*) FILTER(WHERE score>=100),quantile_cont(score,0.99) FROM stories GROUP BY 1").fetchall():
        stats[month] = {'eligible_story_count': count, 'archive_high_score_count': high, 'archive_score_p99': round(p99, 2)}
    months = calendar_months(first.strftime('%Y-%m'), last.strftime('%Y-%m'))
    requests = {}
    nonempty = [month for month in months if month in stats]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(fetch_month, month, args.cache): month for month in nonempty}
        for done, future in enumerate(concurrent.futures.as_completed(futures), 1):
            month = futures[future]
            requests[month] = [future.result()]
            if done % 20 == 0 or done == len(nonempty):
                print(f'Fetched {done}/{len(nonempty)} monthly candidate searches', flush=True)

    def archive_rows():
        ids = sorted({int(hit['objectID']) for pages in requests.values() for result in pages for hit in result['response']['hits']})
        db.execute('CREATE OR REPLACE TEMP TABLE candidate_ids(id BIGINT)')
        db.executemany('INSERT INTO candidate_ids VALUES (?)', [(item_id,) for item_id in ids])
        result = db.execute('SELECT s.* FROM stories s JOIN candidate_ids c ON s.id=c.id')
        columns = [d[0] for d in result.description]
        return {row[0]: dict(zip(columns, row)) for row in result.fetchall()}

    local = archive_rows()
    result = db.execute("SELECT * FROM stories QUALIFY row_number() OVER(PARTITION BY strftime(time,'%Y-%m') ORDER BY score DESC,time ASC,id ASC)<=20")
    columns = [d[0] for d in result.description]
    archived_tops = {}
    for values in result.fetchall():
        row = dict(zip(columns, values))
        archived_tops.setdefault(row['time'].strftime('%Y-%m'), []).append(row)

    output = []
    for month in months:
        info = {**stats.get(month, {'eligible_story_count': 0, 'archive_high_score_count': 0, 'archive_score_p99': None}),
                'month': month, 'entries': [], 'ranking_basis': 'empty', 'candidate_boundary_verified': True,
                'matched_candidate_count': 0, 'search_candidate_count': 0}
        if month not in stats:
            output.append(info)
            continue
        for page in range(10):
            pages = requests[month]
            hits = [(hit, response['checked_at']) for response in pages for hit in response['response']['hits']]
            valid = []
            for hit, checked_at in hits:
                item_id = int(hit['objectID'])
                if item_id not in local:
                    continue
                source = local[item_id]
                assert source['time'].strftime('%Y-%m') == month, (month, item_id, 'month mismatch')
                assert int(source['time'].timestamp()) == hit['created_at_i'], (month, item_id, 'timestamp mismatch')
                if hit.get('points') is None:
                    continue
                valid.append(entry(source, hit, checked_at))
            ranking = rank_rows(valid)
            last_response = pages[-1]['response']
            exhausted = not last_response['hits'] or len(last_response['hits']) < 100 or last_response['nbHits'] <= len(hits)
            boundary = bool(len(ranking) == min(20, stats[month]['eligible_story_count']) and
                            (exhausted or (last_response['hits'][-1].get('points') or 0) < ranking[-1]['score']))
            if not hits:
                info.update(ranking_basis='archive', entries=rank_rows([entry(row) for row in archived_tops[month]]), candidate_boundary_verified=False)
                print(f'{month}: no API candidates; archive-only ranking explicitly labelled', flush=True)
                break
            if boundary or exhausted:
                if len(ranking) < min(20, stats[month]['eligible_story_count']):
                    raise ValueError(f'{month}: insufficient matching candidates ({len(ranking)})')
                info.update(ranking_basis='algolia', entries=ranking, matched_candidate_count=len(valid),
                            search_candidate_count=len(hits), candidate_boundary_verified=True)
                break
            requests[month].append(fetch_month(month, args.cache, page + 1))
            local = archive_rows()
        else:
            raise ValueError(f'{month}: top20 cutoff tie not resolved within API pagination limit')
        output.append(info)

    # The search index can omit archived high-score stories. Scan the entire
    # local index against each resolved cutoff, then check missing candidates
    # against the official API rather than mixing in unchecked archive scores.
    db.execute('CREATE TEMP TABLE cutoffs(month VARCHAR,score BIGINT)')
    db.executemany('INSERT INTO cutoffs VALUES (?,?)', [(m['month'], m['entries'][-1]['score']) for m in output if m['ranking_basis'] == 'algolia'])
    result = db.execute("SELECT s.* FROM stories s JOIN cutoffs c ON strftime(s.time,'%Y-%m')=c.month WHERE s.score>=c.score AND NOT EXISTS (SELECT 1 FROM candidate_ids q WHERE q.id=s.id) ORDER BY s.time,s.id")
    columns = [d[0] for d in result.description]
    omissions = [dict(zip(columns, values)) for values in result.fetchall()]
    official = []
    for row in omissions:
        verified = firebase_entry(row, fetch_firebase(row['id'], args.cache))
        official.append(verified)
        month = next(m for m in output if m['month'] == verified['time_utc'][:7])
        month['entries'] = rank_rows(month['entries'] + [verified])
        month['ranking_basis'] = 'algolia+firebase'
        month['official_candidate_count'] = month.get('official_candidate_count', 0) + 1

    selected = [row for month in output for row in month['entries']]
    guides = json.loads(args.guides.read_text()) if args.guides else {}
    if args.guides:
        for row in selected:
            guide = guides.get(str(row['id']))
            if not isinstance(guide, str) or not guide.strip() or not re.search(r'[\u3400-\u9fff]', guide):
                raise ValueError(f"{row['id']}: missing Chinese introduction")
            row['guide_zh'] = guide.strip()
    all_time = rank_rows(selected)
    api_dates = [result['checked_at'] for pages in requests.values() for result in pages]
    checked_dates = api_dates + [r['checked_at'] for r in official]
    sha256 = hashlib.file_digest(args.index.open('rb'), 'sha256').hexdigest() if hasattr(hashlib, 'file_digest') else hashlib.sha256(args.index.read_bytes()).hexdigest()
    metadata = {'schema_version': 2, 'dataset': 'open-index/hacker-news', 'revision': REVISION,
                'dataset_url': 'https://huggingface.co/datasets/open-index/hacker-news',
                'license': 'ODC-By-1.0', 'index_sha256': sha256, 'eligible_story_count': total,
                'first_story_utc': utc(first), 'last_story_utc': utc(last), 'archive_end_utc': '2026-08-23T08:44:12Z',
                'calendar_month_count': len(months), 'nonempty_month_count': len(stats), 'monthly_entry_count': len(selected),
                'all_time_entry_count': len(all_time), 'api_checked_from_utc': min(checked_dates), 'api_checked_to_utc': max(checked_dates),
                'order': ['score DESC', 'time_utc ASC', 'id ASC'],
                'month_rule': 'UTC calendar month of original submission; values are query-time scores, not month-end scores.',
                'selection': 'Score-ordered Algolia story candidates per month, joined by item ID and exact submission timestamp to the eligible local archive; retrieve additional pages until the top20 score boundary is resolved. Scan all archived scores at or above each monthly cutoff for missing candidates and check those IDs/times/types/scores against official Firebase records before re-ranking.',
                'api_method': 'Empty-query /api/v1/search, tags=story, inclusive UTC month start/exclusive next-month start; 100 hits per page. Exact original response cache is retained in the research directory.',
                'limitations': ['Eligibility is determined from the local archive, excluding records marked deleted/dead/untitled there. Current official dead/deleted status of supplementary candidates is shown explicitly. The external index may omit other stories; low archive scores can hide further omissions.',
                               'Scores are query-time checked values, not final scores or historical front-page ranks; comment counts can retain archive totals where explicitly marked.',
                               'If the official record omits descendants, comments retain the original archive value and comments_source is archive; kids length is never used as a total comment count.',
                               'An archive-only month is explicitly labelled when the search index returns no candidates.',
                               'Title and body excerpts come from the original archive. Chinese introductions are editorial/model-written reading guides based on those titles and excerpts, not summaries of linked articles or comment threads.'],
                'archive_only_months': [m['month'] for m in output if m['ranking_basis'] == 'archive'],
                'empty_months': [m['month'] for m in output if not m['entries']],
                'api_search_count': len(api_dates), 'official_candidate_count': len(official),
                'official_selected_count': sum(r['score_source'] == 'firebase' for r in selected),
                'guide_count': sum(bool(r.get('guide_zh')) for r in selected),
                'guides_sha256': hashlib.sha256(args.guides.read_bytes()).hexdigest() if args.guides else None,
                'guide_basis': 'One Chinese reading guide per selected story, written from the original title and available self-post excerpt.'}
    canonical = {'metadata': metadata, 'all_time': all_time, 'months': output}
    write_json(args.output / 'rankings.json', canonical)

    # Independently re-sort all collected eligible candidates in SQL and compare
    # each selected month's IDs/ranks. Archive fallback is verified against SQL
    # over the complete original index, rather than a second Python sort.
    db.execute('CREATE TEMP TABLE checked(id BIGINT,month VARCHAR,score BIGINT,time_utc TIMESTAMPTZ)')
    check_values = []
    for month in output:
        if month['ranking_basis'].startswith('algolia'):
            for result in requests[month['month']]:
                for hit in result['response']['hits']:
                    item_id = int(hit['objectID'])
                    if item_id in local and hit.get('points') is not None:
                        check_values.append((item_id, month['month'], hit['points'], local[item_id]['time']))
        elif month['ranking_basis'] == 'archive':
            check_values.extend((r['id'], month['month'], r['score'], r['time']) for r in archived_tops[month['month']])
    check_values.extend((r['id'], r['time_utc'][:7], r['score'], datetime.fromisoformat(r['time_utc'].replace('Z', '+00:00'))) for r in official)
    db.executemany('INSERT INTO checked VALUES (?,?,?,?)', check_values)
    checked = db.execute('SELECT month,id,row_number() OVER(PARTITION BY month ORDER BY score DESC,time_utc ASC,id ASC) rank FROM checked QUALIFY rank<=20 ORDER BY month,rank').fetchall()
    expected = [(month['month'], row['id'], row['rank']) for month in output for row in month['entries']]
    assert checked == expected
    assert len(selected) == len({row['id'] for row in selected})
    assert sum(m['eligible_story_count'] for m in output) == total
    assert all(len(m['entries']) == min(20, m['eligible_story_count']) for m in output)
    assert [r[0] for r in db.execute('SELECT id FROM checked ORDER BY score DESC,time_utc ASC,id ASC LIMIT 20').fetchall()] == [r['id'] for r in all_time]
    verification = {'failure_count': 0, 'monthly_rank_rows_checked_independently_in_sql': len(checked),
                    'all_time_rows_checked': len(all_time), 'calendar_months_checked': len(months),
                    'canonical_json_sha256': hashlib.sha256((args.output / 'rankings.json').read_bytes()).hexdigest(),
                    'source_identity': 'Original local item ID and exact UTC timestamp matched for every API candidate used.',
                    'api_month_cutoff_verified': sum(m['ranking_basis'].startswith('algolia') and m['candidate_boundary_verified'] for m in output),
                    'archive_above_cutoff_omissions_checked_officially': [r['id'] for r in official],
                    'official_selected_count': metadata['official_selected_count'], 'guide_count': metadata['guide_count'],
                    'archive_only_months': metadata['archive_only_months'], 'empty_months': metadata['empty_months'],
                    'changed_score_count': sum(r['score'] != r['archive_score'] for r in selected),
                    'raw_api_response_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(args.cache.glob('*.json'))}}
    write_json(args.output / 'verification.json', verification)
    flat = [{**row, 'scope': 'all-time', 'month': row['time_utc'][:7]} for row in all_time]
    flat.extend({**row, 'scope': 'monthly', 'month': month['month']} for month in output for row in month['entries'])
    write_csv(args.output / 'rankings.csv', flat)
    month_dir = args.output / 'months'
    month_dir.mkdir(exist_ok=True)
    for month in output:
        write_json(month_dir / f"{month['month']}.json", month)
        write_csv(month_dir / f"{month['month']}.csv", [{**r, 'scope': 'monthly', 'month': month['month']} for r in month['entries']])
    description = f'''# HN 全时段与每月 Top 20

覆盖 {metadata['first_story_utc']} 至 {metadata['archive_end_utc']}。共 {len(months)} 个连续日历月，{len(stats)} 个月有有效帖子，逐月榜单共 {len(selected)} 条，另列全时段20条。

## 排名与数据

按 score 降序、UTC发帖时间升序、ID升序取前20。评论数仅展示，不参与排序。同一条目只属于其发帖月份；零帖与不足20条的月份如实保留。首月和末月仅覆盖实际数据日期。

下载源：{metadata['dataset_url']}，revision `{REVISION}`，ODC-By-1.0；原始内容权利属于各作者。本地索引有 {total:,} 条有效主帖，排除 deleted、dead、无标题记录。索引SHA256：`{sha256}`。

原始存档部分时段的得分和评论数偏低，因此补查 HN Algolia 搜索索引的各月高分候选。空查询按points排序，每页100条，与本地ID和精确发帖时间匹配；候选末尾得分须低于入选第20名，若有同分或匹配不足则继续翻页。只收录本地有效主帖，未额外引入本地不存在的帖子。

另扫描全部本地档案中原始得分达到各月入选门槛、但未出现在搜索候选中的记录，用官方Firebase API补核ID、精确时间、类型和得分，再重新排序。此次核对 {len(official)} 篇，入选 {metadata['official_selected_count']} 篇。是否有资格参与以原始档案状态为准；补查时的dead/deleted状态另存为current_dead/current_deleted并在页面说明。官方记录若无descendants，评论数保留原始archive_comments，comments_source=archive；不以kids长度冒充评论总数。标题和原文地址仍使用原始档案。

补查范围：{metadata['api_checked_from_utc']} 至 {metadata['api_checked_to_utc']}。score/comments分别注明score_source/comments_source，原始archive_score/archive_comments另存。搜索索引无候选时明确回退到本地快照，月份为：{', '.join(metadata['archive_only_months']) or '无'}。无有效帖子月份：{', '.join(metadata['empty_months'])}。

这是一份可复核的查询时得分榜，不能还原HN首页的时间衰减排名，也不是月末或最终得分。索引覆盖范围和查询时间会影响结果；即使核对已知高分漏项，原始分数偏低也可能使其他漏项未被发现。

标题与自帖节选来自本地原始档案。此次有 {metadata['guide_count']} 篇中文导读，字段guide_zh；导读由模型依据原题及已有自帖节选逐条撰写，是帮助选择阅读的说明，不是外链全文或评论区总结。标题中的观点、质疑、指控仍属于原作者表达。导读不参与排名。编辑源文件SHA256：`{metadata['guides_sha256'] or '未提供'}`。

## 文件与复核

- rankings.json：网页共用的规范数据，含全时段20、连续月份、每月统计和排名。
- rankings.csv：scope=all-time或monthly；全时段20与逐月条目分别保留，不应直接混合计数。
- rankings.md：按年月整理的完整可读榜单。
- months/YYYY-MM.json与.csv：逐月独立数据。
- verification.json：独立SQL验算、原始索引校验值及原始API响应摘要。
- hn-monthly-top20.zip：上述全部文件。

重跑：`.venv/bin/python reports/monthly-top20/build_results.py --index reports/interesting-themes/research/all-stories.parquet --output reports/monthly-top20/results --cache reports/monthly-top20/api-cache --guides reports/monthly-top20/guides/guides.json`。缓存保存在研究目录api-cache，刷新时应另用空缓存目录并保留旧版。使用本站仓库scripts中的副本时必须显式传入--index、--output、--cache及--guides；本站导读编辑源位于data/monthly-top-guides.json。提供--guides时会要求每条入选记录都有中文导读；刷新榜单产生新入选条目时应先补齐导读。
'''
    (args.output / 'README.md').write_text(description)
    md = [description, '\n## 全时段 Top 20\n', markdown_table(all_time)]
    for month in output:
        md += [f"\n## {month['month']}\n", f"有效主帖 {month['eligible_story_count']:,} 条；排名来源 {month['ranking_basis']}。\n",
               markdown_table(month['entries']) if month['entries'] else '本地档案中没有有效主帖。']
    (args.output / 'rankings.md').write_text('\n'.join(md) + '\n')
    archive_path = args.output / 'hn-monthly-top20.zip'
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(args.output.rglob('*')):
            if path.is_file() and path != archive_path:
                archive.write(path, 'hn-monthly-top20/' + path.relative_to(args.output).as_posix())
    print(json.dumps({'metadata': metadata, 'verification': {k: v for k, v in verification.items() if k != 'raw_api_response_sha256'}}, ensure_ascii=False, indent=2), flush=True)


if __name__ == '__main__':
    main()
