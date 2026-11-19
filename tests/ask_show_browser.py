"""Verify monthly Ask/Show pages, exports and browser behavior against canonical data."""
import argparse
import csv
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import zipfile
from playwright.sync_api import sync_playwright, expect

parser = argparse.ArgumentParser()
parser.add_argument('--base-url', default='http://127.0.0.1:4326/data-lab/')
parser.add_argument('--skip-full-archive', action='store_true')
parser.add_argument('--download-timeout-ms', type=int, default=30000,
                    help='Total timeout for each download; use a longer limit on slow remote connections.')
args = parser.parse_args()
base = args.base_url.rstrip('/') + '/'
root = Path(__file__).resolve().parents[1]
exports = root / 'public/downloads/hn-ask-show-top10'
canonical = json.loads((exports / 'rankings.json').read_text())
output = root / 'test-results'
output.mkdir(exist_ok=True)

class Stories(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows = []
        self.row = None
        self.field = None
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])
        if 'data-monthly-story' in attrs:
            self.row = {'id': int(attrs['data-monthly-story'])}
        if self.row is not None:
            if tag == 'h3':
                self.field = ('title', 'h3')
            elif 'monthly-story-guide' in attrs.get('class', '').split():
                self.field = ('guide_zh', 'p')
            elif 'data-story-score' in attrs:
                self.field = ('score', 'b')
            elif 'data-story-comments' in attrs:
                self.field = ('comments', 'b')
            if tag == 'time':
                self.row['time_utc'] = attrs['datetime']

    def handle_data(self, text):
        if self.row is not None and self.field:
            field = self.field[0]
            self.row[field] = self.row.get(field, '') + text

    def handle_endtag(self, tag):
        if self.field and tag == self.field[1]:
            self.field = None
        if tag == 'li' and self.row is not None:
            self.row['title'] = self.row['title'].strip()
            for field in ['score', 'comments']:
                self.row[field] = int(self.row[field].replace(',', ''))
            self.rows.append(self.row)
            self.row = None

link_targets = set()
count = 0
all_csv_rows = []
for kind, channel in canonical['channels'].items():
    aggregate = json.loads((exports / kind / 'rankings.json').read_text())
    assert aggregate == {'metadata': canonical['metadata'], **channel}
    for month in channel['months']:
        path = root / 'dist' / channel['path'] / month['month'] / 'index.html'
        document = Stories()
        document.feed(path.read_text())
        expected = [{key: row[key] for key in ['id','title','guide_zh','score','comments','time_utc']} for row in month['entries']]
        for row in expected:
            row['title'] = row['title'].strip()
        assert document.rows == expected, (kind,month['month'])
        count += len(expected)
        link_targets.update(document.links)
        assert json.loads((exports / kind / f"{month['month']}.json").read_text()) == month
        rows = list(csv.DictReader((exports / kind / f"{month['month']}.csv").open(encoding='utf-8-sig', newline='')))
        assert len(rows) == len(month['entries'])
        all_csv_rows.extend(rows)
        for actual, entry in zip(rows, month['entries']):
            for key in ['rank','id','title','guide_zh','author','score','comments','archive_score','archive_comments','score_source','comments_source','category_source','checked_at','current_dead','current_deleted','time_utc','hn_url','url','excerpt']:
                assert actual[key] == (str(entry[key]) if entry[key] is not None else ''), (kind,month['month'],entry['id'],key)
            assert actual['channel'] == kind and actual['month'] == month['month']
for target in link_targets:
    if target.startswith('/data-lab/'):
        path = root / 'dist' / unquote(urlsplit(target).path).removeprefix('/data-lab/')
        assert path.is_file() or (path / 'index.html').is_file(), target
assert count == canonical['metadata']['monthly_entry_count']
flat = list(csv.DictReader((exports / 'rankings.csv').open(encoding='utf-8-sig',newline='')))
assert len(flat) == count
assert flat == all_csv_rows
for kind in canonical['channels']:
    aggregate_csv = list(csv.DictReader((exports / kind / 'rankings.csv').open(encoding='utf-8-sig',newline='')))
    assert aggregate_csv == [r for r in flat if r['channel'] == kind]
with zipfile.ZipFile(exports / 'hn-ask-show-top10.zip') as archive:
    assert archive.testzip() is None
    assert len(archive.namelist()) == len(list(exports.rglob('*.*'))) - 1
    for member in archive.namelist():
        relative = Path(member).relative_to('hn-ask-show-top10')
        assert archive.read(member) == (exports / relative).read_bytes(), member
print(f'PASS: 478 built month pages, {count} exact rows, monthly CSV/JSON, internal links and complete ZIP.',flush=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(viewport={'width':1440,'height':1080},timezone_id='Asia/Shanghai')
    page = context.new_page()
    errors = []
    page.on('pageerror',lambda error:errors.append(str(error)))
    if not args.skip_full_archive:
        for kind, channel in canonical['channels'].items():
            for month in channel['months']:
                r = context.request.get(urljoin(base,f"{channel['path']}/{month['month']}/"))
                assert r.status == 200,(kind,month['month'])
    for name in ['rankings.json','rankings.csv','rankings.md','README.md','verification.json','hn-ask-show-top10.zip','ask/rankings.csv','show/rankings.json','ask/2006-10.csv','show/2009-03.json']:
        r = context.request.get(urljoin(base,'downloads/hn-ask-show-top10/'+name), timeout=args.download_timeout_ms)
        assert r.status == 200 and r.body() == (exports / name).read_bytes(), name
    page.goto(base,wait_until='networkidle')
    assert page.locator('a[href="/data-lab/hn/ask-show/"]').count() >= 2
    page.goto(urljoin(base,'hn/ask-show/'),wait_until='networkidle')
    expect(page.locator('.ask-show-channel')).to_have_count(2)
    page.locator('.ask-show-channel h2 a').first.click()
    page.wait_for_url('**/ask/')
    expect(page.locator('.ask-show-tabs a[aria-current]')).to_contain_text('ASK')
    page.goto(urljoin(base,'hn/ask-show/ask/2023-07/'),wait_until='networkidle')
    month = next(m for m in canonical['channels']['ask']['months'] if m['month']=='2023-07')
    rows = page.locator('[data-monthly-story]:visible')
    expect(rows).to_have_count(10)
    assert rows.first.get_attribute('data-monthly-story') == str(month['entries'][0]['id'])
    last = month['entries'][-1]
    page.locator('#monthly-search').fill(last['guide_zh'])
    expect(rows).to_have_count(1)
    assert rows.first.get_attribute('data-monthly-story') == str(last['id'])
    assert '第10名' in ''.join(rows.first.aria_snapshot().split())
    filtered = page.url
    page.reload(wait_until='networkidle')
    expect(rows).to_have_count(1)
    page.locator('.ask-show-tabs a').last.click()
    page.wait_for_url('**/show/2023-07/')
    expect(rows).to_have_count(10)
    page.go_back(wait_until='networkidle')
    assert page.url == filtered
    expect(rows).to_have_count(1)
    page.locator('#monthly-search').fill('不存在的帖子-778899')
    expect(rows).to_have_count(0)
    page.locator('[data-monthly-empty] button').click()
    expect(rows).to_have_count(10)
    expect(page.locator('#monthly-search')).to_be_focused()
    page.goto(urljoin(base,f"hn/ask-show/ask/2023-07/?q=missing#story-{last['id']}"),wait_until='networkidle')
    expect(rows).to_have_count(10)
    expect(page.locator(f"#story-{last['id']}")).to_be_visible()
    assert '?' not in page.url
    page.locator('.monthly-values summary').first.focus()
    page.keyboard.press('Enter')
    expect(page.locator('.monthly-values').first).to_have_attribute('open','')
    page.locator('[data-monthly-jump] select').select_option('2006-10')
    page.locator('[data-monthly-jump] button').click()
    page.wait_for_url('**/ask/2006-10/')
    expect(rows).to_have_count(0)
    expect(page.locator('.monthly-no-data')).to_be_visible()
    expect(page.locator('.monthly-no-data')).to_contain_text('本频道')
    expect(page.locator('a[rel="prev"]')).to_have_count(0)
    page.locator('.ask-show-tabs a').last.click()
    page.wait_for_url('**/show/2006-10/')
    expect(rows).to_have_count(0)
    page.goto(urljoin(base,'hn/ask-show/show/2009-03/'),wait_until='networkidle')
    expect(rows).to_have_count(3)
    expect(page.locator('.ask-show-sparse')).to_contain_text('3 篇')
    page.goto(urljoin(base,'hn/ask-show/show/#year-2011'),wait_until='networkidle')
    expect(page.locator('#year-2011')).to_have_attribute('open','')
    page.locator('#year-2011 a').first.click()
    page.wait_for_url('**/show/2011-01/')
    page.goto(urljoin(base,'hn/ask-show/show/2026-08/'),wait_until='networkidle')
    expect(page.locator('a[rel="next"]')).to_have_count(0)
    expect(page.locator('.monthly-month-note')).to_contain_text('本月仅覆盖档案实际日期')
    for width in [320,375,620,621,768,800,801,1080,1151,1280,1281,1440]:
        page.set_viewport_size({'width':width,'height':900})
        for path in ['', 'hn/ask-show/', 'hn/ask-show/ask/', 'hn/ask-show/show/2023-07/']:
            page.goto(urljoin(base,path),wait_until='networkidle')
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),(width,path)
            if width in (375,1440) and path:
                name = 'month' if path.endswith('2023-07/') else 'channel' if path.endswith('ask/') else 'landing'
                page.screenshot(path=str(output/f'ask-show-{name}-{width}.png'),full_page=True)
    assert not errors,errors
    nojs = browser.new_context(java_script_enabled=False,viewport={'width':375,'height':900})
    static = nojs.new_page()
    static.goto(urljoin(base,'hn/ask-show/ask/2023-07/'),wait_until='networkidle')
    expect(static.locator('[data-monthly-story]')).to_have_count(10)
    expect(static.locator('[data-monthly-search]')).to_be_hidden()
    expect(static.locator('.monthly-story-guide')).to_have_count(10)
    static.locator('.ask-show-tabs a').last.click()
    static.wait_for_url('**/show/2023-07/')
    expect(static.locator('[data-monthly-story]')).to_have_count(10)
    static.locator('a[rel="prev"]').click()
    static.wait_for_url('**/show/2023-06/')
    browser.close()
print('PASS: HTTP/downloads, channel/month navigation, Chinese search, query/hash/history, sparse/empty months, keyboard, mobile and no-JavaScript.',flush=True)
