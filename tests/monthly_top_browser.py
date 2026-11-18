"""Monthly archive acceptance against a production build and HTTP preview/live site."""
import argparse
import csv
import html
from html.parser import HTMLParser
import io
import json
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import zipfile

from playwright.sync_api import sync_playwright, expect

parser = argparse.ArgumentParser()
parser.add_argument('--base-url', default='http://127.0.0.1:4325/data-lab/')
parser.add_argument('--skip-full-archive', action='store_true', help='Skip 239 HTTP requests; still compare all built HTML pages.')
args = parser.parse_args()
base = args.base_url.rstrip('/') + '/'
root = Path(__file__).resolve().parents[1]
exports = root / 'public/downloads/hn-monthly-top20'
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
for month in canonical['months']:
    path = root / 'dist/hn/monthly-top' / month['month'] / 'index.html'
    document = Stories()
    document.feed(path.read_text())
    expected = [{key: entry[key] for key in ['id', 'title', 'guide_zh', 'score', 'comments', 'time_utc']} for entry in month['entries']]
    for entry in expected:
        entry['title'] = entry['title'].strip()
    assert document.rows == expected, month['month']
    link_targets.update(document.links)
    month_json = json.loads((exports / 'months' / f"{month['month']}.json").read_text())
    assert month_json == month
    rows = list(csv.DictReader((exports / 'months' / f"{month['month']}.csv").open(encoding='utf-8-sig', newline='')))
    assert [int(row['id']) for row in rows] == [row['id'] for row in month['entries']]
for href in link_targets:
    if href.startswith('/data-lab/'):
        target = unquote(urlsplit(href).path).removeprefix('/data-lab/')
        path = root / 'dist' / target
        assert path.is_file() or (path / 'index.html').is_file(), href
flat = list(csv.DictReader((exports / 'rankings.csv').open(encoding='utf-8-sig', newline='')))
assert len(flat) == 4741
assert sum(row['scope'] == 'all-time' for row in flat) == 20
with zipfile.ZipFile(exports / 'hn-monthly-top20.zip') as archive:
    assert archive.testzip() is None
    assert len(archive.namelist()) == 483
    for member in archive.namelist():
        relative = Path(member).relative_to('hn-monthly-top20')
        assert archive.read(member) == (exports / relative).read_bytes(), member
print('PASS: all 239 built month pages preserve 4,721 exact ranked rows; all links, monthly CSV/JSON and 483 ZIP members match.', flush=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(viewport={'width': 1440, 'height': 1080}, timezone_id='Asia/Shanghai')
    page = context.new_page()
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    if not args.skip_full_archive:
        for month in canonical['months']:
            response = context.request.get(urljoin(base, f"hn/monthly-top/{month['month']}/"))
            assert response.status == 200, month['month']
    for name in ['README.md', 'rankings.json', 'rankings.csv', 'rankings.md', 'verification.json', 'hn-monthly-top20.zip', 'months/2006-11.csv', 'months/2006-12.json', 'months/2026-08.csv']:
        response = context.request.get(urljoin(base, 'downloads/hn-monthly-top20/' + name))
        assert response.status == 200, name
        assert response.body() == (exports / name).read_bytes(), name

    page.goto(base, wait_until='networkidle')
    assert page.locator('a[href="/data-lab/hn/monthly-top/"]').count() >= 2
    page.goto(urljoin(base, 'hn/monthly-top/'), wait_until='networkidle')
    rows = page.locator('[data-monthly-story]:visible')
    expect(rows).to_have_count(20)
    assert [int(row) for row in rows.evaluate_all('(els)=>els.map(el=>el.dataset.monthlyStory)')] == [e['id'] for e in canonical['all_time']]
    page.locator('#monthly-search').fill(canonical['all_time'][-1]['title'])
    expect(rows).to_have_count(1)
    assert '第20名' in ''.join(rows.first.aria_snapshot().split())
    last = canonical['all_time'][-1]
    page.locator('#monthly-search').fill(last['guide_zh'])
    expect(rows).to_have_count(1)
    assert rows.first.get_attribute('data-monthly-story') == str(last['id'])
    expect(rows.first.locator('.monthly-story-guide')).to_have_text(last['guide_zh'])
    page.locator('#monthly-search').fill('Stephen Ｈａｗｋｉｎｇ')
    expect(rows).to_have_count(1)
    assert rows.first.get_attribute('data-monthly-story') == '16582136'
    assert 'q=' in page.url
    filtered = page.url
    page.reload(wait_until='networkidle')
    expect(rows).to_have_count(1)
    page.goto(urljoin(base, 'hn/monthly-top/2024-03/'), wait_until='networkidle')
    page.go_back(wait_until='networkidle')
    assert page.url == filtered
    expect(rows).to_have_count(1)
    page.locator('#monthly-search').fill('不存在的帖子-778899')
    expect(rows).to_have_count(0)
    expect(page.locator('[data-monthly-empty]')).to_be_visible()
    page.locator('[data-monthly-empty] button').click()
    expect(rows).to_have_count(20)
    expect(page.locator('#monthly-search')).to_be_focused()
    page.locator('#monthly-search').fill('Hawking')
    rows.first.locator('.monthly-story-links a').last.click()
    assert '?' not in page.url
    expect(rows).to_have_count(20)

    page.goto(urljoin(base, 'hn/monthly-top/2023-07/#story-36860065'), wait_until='networkidle')
    exception = page.locator('#story-36860065')
    expect(exception).to_be_visible()
    expect(exception.locator('[data-story-score]')).to_have_text('1,205')
    assert '补查时已标记 dead' in exception.locator('.monthly-story-meta').inner_text()
    assert '存档' in exception.locator('.monthly-story-numbers').inner_text()
    exception.locator('.monthly-values summary').click()
    assert '官方记录未提供评论总数' in exception.locator('.monthly-values').inner_text()

    page.goto(urljoin(base, 'hn/monthly-top/2023-02/?q=missing#story-34804874'), wait_until='networkidle')
    expect(rows).to_have_count(20)
    assert '?' not in page.url
    entry = next(m for m in canonical['months'] if m['month'] == '2023-02')['entries'][0]
    assert entry['score'] == 3363 and entry['score'] != entry['archive_score']
    first = rows.first
    expect(first.locator('time')).to_have_text(entry['time_utc'][:10])
    first.locator('.monthly-values summary').focus()
    page.keyboard.press('Enter')
    expect(first.locator('.monthly-values')).to_have_attribute('open', '')
    assert str(entry['archive_score']) in first.locator('.monthly-values').inner_text()
    page.locator('[data-monthly-jump] select').select_option('2006-12')
    page.locator('[data-monthly-jump] button').click()
    page.wait_for_url('**/2006-12/')
    expect(rows).to_have_count(1)
    page.locator('a[rel="prev"]').click()
    page.wait_for_url('**/2006-11/')
    expect(rows).to_have_count(0)
    expect(page.locator('.monthly-no-data')).to_be_visible()
    assert page.locator('a[rel="prev"]').get_attribute('href').endswith('/2006-10/')

    for month in ['2006-10', '2006-11', '2006-12', '2007-01', '2023-02', '2026-08']:
        page.goto(urljoin(base, f'hn/monthly-top/{month}/'), wait_until='networkidle')
        expected = next(m for m in canonical['months'] if m['month'] == month)
        expect(rows).to_have_count(len(expected['entries']))
        assert [int(row) for row in rows.evaluate_all('(els)=>els.map(el=>el.dataset.monthlyStory)')] == [e['id'] for e in expected['entries']]
        if month == '2006-10':
            expect(page.locator('a[rel="prev"]')).to_have_count(0)
        if month == '2026-08':
            expect(page.locator('a[rel="next"]')).to_have_count(0)
            assert '本月仅覆盖档案实际日期' in page.locator('.monthly-month-note').inner_text()

    page.goto(urljoin(base, 'hn/monthly-top/#year-2011'), wait_until='networkidle')
    expect(page.locator('#year-2011')).to_have_attribute('open', '')
    page.locator('#year-2011 a').first.click()
    page.wait_for_url('**/2011-01/')
    for width in [320,375,620,621,768,800,801,900,901,950,1080,1100,1150,1151,1280,1440]:
        page.set_viewport_size({'width': width, 'height': 900})
        for path in ['', 'hn/monthly-top/', 'hn/monthly-top/2023-02/']:
            page.goto(urljoin(base,path), wait_until='networkidle')
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), (width,path)
            if width in (375,1440) and path:
                name = 'month' if path.endswith('2023-02/') else 'archive'
                page.screenshot(path=str(output / f'monthly-{name}-{width}.png'), full_page=True)
    plain = browser.new_context(java_script_enabled=False, viewport={'width':375,'height':900})
    static = plain.new_page()
    static.goto(urljoin(base, 'hn/monthly-top/'), wait_until='networkidle')
    expect(static.locator('[data-monthly-story]:visible')).to_have_count(20)
    expect(static.locator('[data-monthly-search]')).to_be_hidden()
    expect(static.locator('[data-monthly-jump]')).to_be_hidden()
    static.locator('#year-2006 > summary').click()
    static.locator('#year-2006 a').last.click()
    static.wait_for_url('**/2006-12/')
    expect(static.locator('[data-monthly-story]:visible')).to_have_count(1)
    static.locator('a[rel="prev"]').click()
    static.wait_for_url('**/2006-11/')
    expect(static.locator('.monthly-no-data')).to_be_visible()
    assert not errors, errors
    browser.close()
print('PASS: all-time/monthly navigation, source correction, query/history/hash restoration, sparse/empty/partial months, downloads, keyboard, no-JS and 16 viewport widths; no script errors.', flush=True)
