"""Production-site acceptance checks. Requires Python Playwright + Chromium."""
import argparse
import csv
import io
import json
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit

from playwright.sync_api import sync_playwright, expect

parser = argparse.ArgumentParser()
parser.add_argument('--base-url', default='http://127.0.0.1:4321/data-lab/')
args = parser.parse_args()
base = args.base_url.rstrip('/') + '/'
root = Path(__file__).resolve().parents[1]
output = root / 'test-results'
output.mkdir(exist_ok=True)
pages = {'home': '', 'books': 'hn/books/', 'movies': 'hn/movies/', 'reading': 'hn/school-reading/', 'history': 'hn/history-documentaries/', 'about': 'about/'}

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(viewport={'width': 1440, 'height': 1080})
    page = context.new_page()
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    internal = set()

    for name, path in pages.items():
        response = page.goto(urljoin(base, path), wait_until='networkidle')
        assert response.status == 200, (name, response.status)
        expect(page.locator('h1')).to_have_count(1)
        assert page.locator('main').inner_text().strip(), name
        for value in page.locator('a[href], link[href], script[src]').evaluate_all(
            '(els) => els.map(el => el.href || el.src)'
        ):
            parsed = urlsplit(value)
            if parsed.netloc == urlsplit(base).netloc:
                assert parsed.path.startswith(urlsplit(base).path), value
                internal.add(urlunsplit((parsed.scheme, parsed.netloc, parsed.path, '', '')))

    for address in sorted(internal):
        response = context.request.get(address)
        assert response.status == 200, (address, response.status)

    for kind, anchor in [('books', 8143), ('movies', 4067)]:
        page.goto(urljoin(base, f'hn/{kind}/'), wait_until='networkidle')
        rows = page.locator('[data-rank]:visible')
        expect(rows).to_have_count(100)
        expect(page.locator('[data-result-count]')).to_have_text('100')
        data = page.locator('#ranking-data').text_content()
        entries = json.loads(data)
        assert len(entries) == 100 and entries[0]['mentions'] == anchor

        page.locator('#search').fill('黑客帝国' if kind == 'movies' else 'Orwell')
        assert rows.count() > 0
        assert 'q=' in page.url
        if kind == 'movies':
            expect(rows).to_have_count(1)
            assert rows.first.get_attribute('data-rank') == '1'
        else:
            assert '1984' in rows.all_inner_texts()[0]

        filtered_ranks = rows.evaluate_all('(els) => els.map(el => el.dataset.rank)')
        page.reload(wait_until='networkidle')
        assert rows.evaluate_all('(els) => els.map(el => el.dataset.rank)') == filtered_ranks
        page.locator('[data-reset]').first.click()
        expect(rows).to_have_count(100)
        expect(page.locator('#search')).to_be_focused()
        assert '?' not in page.url

        page.locator('#search').fill('no-such-work-完全不存在-992233')
        expect(rows).to_have_count(0)
        expect(page.locator('[data-empty]')).to_be_visible()
        page.locator('[data-empty] [data-reset]').click()
        expect(rows).to_have_count(100)

        category = entries[0]['category']
        page.locator('#category').select_option(category)
        assert rows.count() == sum(entry['category'] == category for entry in entries)
        assert all(category in row for row in rows.all_inner_texts())
        page.locator('[data-reset]').first.click()
        page.locator('#sort').select_option('least')
        assert int(rows.first.get_attribute('data-rank')) == min(entries, key=lambda entry: (entry['mentions'], entry['rank']))['rank']
        page.locator('#sort').select_option('title')
        assert rows.first.locator('.original-title').inner_text() == min(entries, key=lambda entry: entry['title'].lower())['title']
        page.locator('[data-reset]').first.click()

        first_details = rows.first.locator('details')
        first_details.locator('summary').focus()
        page.keyboard.press('Enter')
        expect(first_details).to_have_attribute('open', '')
        assert first_details.locator('.details-body p').inner_text().strip()
        page.locator('[data-expand]').click()
        expect(page.locator('[data-rank] details[open]')).to_have_count(100)
        page.locator('[data-expand]').click()
        expect(page.locator('[data-rank] details[open]')).to_have_count(0)

        page.locator('#search').focus()
        page.keyboard.press('Tab')
        expect(page.locator('#category')).to_be_focused()
        page.keyboard.press('Tab')
        expect(page.locator('#sort')).to_be_focused()

        for ext in ['csv', 'json']:
            response = context.request.get(urljoin(base, f'downloads/hn-{kind}-top100.{ext}'))
            assert response.status == 200
            text = response.body().decode('utf-8')
            if ext == 'csv':
                assert text.startswith('\ufeff排名,')
                exported = list(csv.DictReader(io.StringIO(text.lstrip('\ufeff'))))
                assert len(exported) == 100 and int(exported[0]['提及数']) == anchor
                assert all(row['简介'] and row['分类'] for row in exported)
            else:
                exported = json.loads(text)
                assert exported['entries'] == entries
                assert exported['source']['eligibleItems'] == 34721984

    page.goto(urljoin(base, 'hn/school-reading/'), wait_until='networkidle')
    books = page.locator('[data-book]:visible')
    entries = json.loads(page.locator('#school-reading-data').text_content())
    expect(books).to_have_count(109)
    assert all(book['summary'] in page.locator('main').inner_text() for book in entries)
    for book_id, qualification in [
        ('harry-potter', '明确是第一册，作品按系列合并；孩子并未理解所有细节。'),
        ('asterix', '按初中阅读水平分组，不推定孩子的确切年龄。'),
        ('design-real-world', '英国GCSE通常处于14–16岁阶段，跨两个导航组；不是确切年龄。'),
    ]:
        details = page.locator(f'[data-book="{book_id}"] details')
        details.locator('summary').click()
        assert qualification in details.inner_text(), (book_id, qualification)
    for age, count in [('6-8', 30), ('9-11', 16), ('12-14', 27), ('15-18', 23), ('unspecified', 29)]:
        page.locator(f'[data-age="{age}"]').click()
        expect(books).to_have_count(count)
        expect(page.locator('[data-result-count]')).to_have_text(str(count))
        expect(page.locator(f'[data-age="{age}"]')).to_have_attribute('aria-pressed', 'true')
    page.locator('[data-age="6-8"]').click()
    page.locator('#reading-category').select_option('科普与自然')
    expect(books).to_have_count(3)
    page.locator('#reading-search').fill('万物 运转')
    expect(books).to_have_count(1)
    expect(books.first.locator('h3')).to_have_text('万物运转的秘密')
    assert 'age=6-8' in page.url and 'category=' in page.url and 'q=' in page.url
    filtered_url = page.url
    page.reload(wait_until='networkidle')
    expect(books).to_have_count(1)
    page.goto(urljoin(base, 'hn/school-reading/?age=15-18'), wait_until='networkidle')
    expect(books).to_have_count(23)
    page.go_back(wait_until='networkidle')
    assert page.url == filtered_url
    expect(books).to_have_count(1)
    page.locator('[data-reading-reset]').first.click()
    expect(books).to_have_count(109)
    expect(page.locator('#reading-search')).to_be_focused()
    assert '?' not in page.url
    page.locator('#reading-search').fill('没有这本书-998877')
    expect(books).to_have_count(0)
    expect(page.locator('[data-reading-empty]')).to_be_visible()
    page.locator('[data-reading-empty] [data-reading-reset]').click()
    expect(books).to_have_count(109)
    page.locator('#reading-search').fill('ＯＲＷＥＬＬ')
    expect(books).to_have_count(1)
    books.first.locator('summary').focus()
    page.keyboard.press('Enter')
    expect(books.first.locator('details')).to_have_attribute('open', '')
    assert books.first.locator('details a').count() > 0
    page.locator('#reading-search').focus()
    page.keyboard.press('Tab')
    expect(page.locator('#reading-category')).to_be_focused()
    page.goto(urljoin(base, 'hn/school-reading/?age=wrong&category=不存在'), wait_until='networkidle')
    expect(books).to_have_count(109)

    download_root = 'downloads/hn-school-reading/'
    for ext in ['csv', 'json']:
        response = context.request.get(urljoin(base, download_root + '书目总表.' + ext))
        assert response.status == 200
        text = response.body().decode('utf-8')
        exported = list(csv.DictReader(io.StringIO(text.lstrip('\ufeff')))) if ext == 'csv' else json.loads(text)
        assert len(exported) == 109
        assert [row['原书名'] for row in exported] == [book['title'] for book in entries]
        assert all(row['内容简介'] and row['作者'] and row['年龄分组'] for row in exported)
    age_export = context.request.get(urljoin(base, download_root + '按年龄/6-8岁.json')).json()
    assert len(age_export) == 30
    category_export = context.request.get(urljoin(base, download_root + '按类别/科普与自然.json')).json()
    assert len(category_export) == 7
    response = context.request.get(urljoin(base, download_root + '学生阅读书目.zip'))
    import zipfile
    with zipfile.ZipFile(io.BytesIO(response.body())) as archive:
        assert archive.testzip() is None
        assert len(json.loads(archive.read('书目总表.json'))) == 109

    page.goto(urljoin(base, 'hn/history-documentaries/'), wait_until='networkidle')
    works = page.locator('[data-work]:visible')
    catalogue = json.loads(page.locator('#history-documentaries-data').text_content())
    assert len(catalogue) == 197
    expect(page.locator('[data-work]')).to_have_count(197)
    expect(works).to_have_count(100)
    assert page.locator('[data-work] p.reading-summary').count() == 197
    for view, count in [('books', 100), ('documentaries', 97), ('history-documentaries', 64)]:
        page.locator(f'[data-view="{view}"]').click()
        expect(works).to_have_count(count)
        expect(page.locator('[data-result-count]')).to_have_text(str(count))
        expect(page.locator(f'[data-view="{view}"]')).to_have_attribute('aria-pressed', 'true')
    page.locator('#history-category').select_option('战争与大屠杀')
    expect(works).to_have_count(12)
    page.locator('#history-search').fill('ＦＯＧ　ＭＯＲＲＩＳ')
    expect(works).to_have_count(1)
    assert works.first.get_attribute('data-work') == 'documentaries-fog-of-war'
    assert 'view=history-documentaries' in page.url and 'category=' in page.url and 'q=' in page.url
    filtered_url = page.url
    page.reload(wait_until='networkidle')
    expect(works).to_have_count(1)
    page.goto(urljoin(base, 'hn/history-documentaries/?view=documentaries'), wait_until='networkidle')
    expect(works).to_have_count(97)
    page.go_back(wait_until='networkidle')
    assert page.url == filtered_url
    expect(works).to_have_count(1)
    details = works.first.locator('details')
    details.locator('summary').focus()
    page.keyboard.press('Enter')
    expect(details).to_have_attribute('open', '')
    assert details.locator('blockquote').count() > 0
    assert details.locator('a[href*="news.ycombinator.com/item?id="]').count() > 0
    page.locator('[data-history-reset]').first.click()
    expect(works).to_have_count(64)
    expect(page.locator('#history-search')).to_be_focused()
    page.locator('#history-search').fill('不存在的影片-998877')
    expect(works).to_have_count(0)
    expect(page.locator('[data-history-empty]')).to_be_visible()
    page.locator('[data-history-empty] [data-history-reset]').click()
    expect(works).to_have_count(64)
    page.locator('#history-search').fill('AlphaGo')
    expect(works).to_have_count(0)
    page.locator('[data-view="documentaries"]').click()
    expect(works).to_have_count(1)
    assert 'AlphaGo' in works.first.locator('h4').inner_text()
    page.locator('[data-history-reset]').first.click()
    page.locator('#history-category').select_option('文化与艺术')
    page.locator('[data-view="books"]').click()
    expect(page.locator('#history-category')).to_have_value('')
    expect(works).to_have_count(100)
    page.locator('#history-search').fill('丝绸之路 欧亚')
    expect(works).to_have_count(1)
    page.locator('#history-search').focus()
    page.keyboard.press('Tab')
    expect(page.locator('#history-category')).to_be_focused()
    page.goto(urljoin(base, 'hn/history-documentaries/?view=wrong&category=不存在'), wait_until='networkidle')
    expect(works).to_have_count(100)
    page.goto(urljoin(base, 'hn/history-documentaries/?view=history-documentaries#work-documentaries-fog-of-war'), wait_until='networkidle')
    expect(page.locator('#work-documentaries-fog-of-war')).to_be_visible()
    page.locator('.history-discussions summary').click()
    expect(page.locator('.history-discussions li')).to_have_count(18)

    history_download_root = 'downloads/hn-history-documentaries/'
    for name, count in [('历史书目', 100), ('纪录片单', 97), ('历史题材纪录片', 64)]:
        response = context.request.get(urljoin(base, history_download_root + name + '.json'))
        assert response.status == 200
        data = response.json()
        assert len(data) == count
        for work in data:
            assert work['summary_zh'] and work['mentions']
        csv_response = context.request.get(urljoin(base, history_download_root + name + '.csv'))
        exported = list(csv.DictReader(io.StringIO(csv_response.body().decode('utf-8-sig'))))
        assert len(exported) == count
        assert [row['英文名'] for row in exported] == [work['title'] for work in data]
    response = context.request.get(urljoin(base, history_download_root + '历史书目与纪录片.zip'))
    with zipfile.ZipFile(io.BytesIO(response.body())) as archive:
        assert archive.testzip() is None
        assert len(json.loads(archive.read('历史书目.json'))) == 100
        assert len(json.loads(archive.read('纪录片单.json'))) == 97
        assert len(json.loads(archive.read('历史题材纪录片.json'))) == 64

    page.goto(urljoin(base, 'hn/movies/?q=Dune&sort=year'), wait_until='networkidle')
    expect(page.locator('[data-rank]:visible')).to_have_count(2)
    assert page.locator('[data-rank]:visible').first.get_attribute('data-rank') == '86'
    page.goto(urljoin(base, 'hn/movies/?category=不存在&sort=wrong'), wait_until='networkidle')
    expect(page.locator('[data-rank]:visible')).to_have_count(100)

    for width, height in [(320, 740), (375, 900), (620, 900), (621, 900), (768, 1024), (800, 900), (801, 900), (1080, 900), (1440, 1080)]:
        page.set_viewport_size({'width': width, 'height': height})
        for name, path in pages.items():
            page.goto(urljoin(base, path), wait_until='networkidle')
            assert not page.evaluate('document.documentElement.scrollWidth > window.innerWidth'), (name, width)
            if width in (375, 1440):
                page.screenshot(path=str(output / f'{name}-{width}.png'))
            if name in ('books', 'movies'):
                page.locator('[data-expand]').click()
                assert not page.evaluate('document.documentElement.scrollWidth > window.innerWidth'), (name, width, 'expanded')
                if width == 375:
                    page.locator('[data-rank="1"]').evaluate("el => el.scrollIntoView({block:'start', behavior:'instant'})")
                    page.screenshot(path=str(output / f'{name}-reading-{width}.png'))
            if name == 'history':
                page.locator('[data-view="history-documentaries"]').click()
                page.locator('[data-work="documentaries-fog-of-war"] summary').click()
                assert not page.evaluate('document.documentElement.scrollWidth > window.innerWidth'), (name, width, 'evidence')
                if width in (375, 1440):
                    page.locator('[data-work="documentaries-fog-of-war"]').evaluate("el => el.scrollIntoView({block:'start', behavior:'instant'})")
                    page.screenshot(path=str(output / f'{name}-evidence-{width}.png'))

    page.emulate_media(reduced_motion='reduce')
    assert page.locator('html').evaluate('el => getComputedStyle(el).scrollBehavior') == 'auto'
    page.goto(base, wait_until='networkidle')
    page.keyboard.press('Tab')
    expect(page.locator('.skip-link')).to_be_focused()
    assert not errors, errors

    plain = browser.new_context(java_script_enabled=False, viewport={'width': 375, 'height': 900})
    static = plain.new_page()
    response = static.goto(urljoin(base, 'hn/history-documentaries/'), wait_until='networkidle')
    assert response.status == 200
    expect(static.locator('[data-work]:visible')).to_have_count(197)
    expect(static.locator('[data-history-controls]')).to_be_hidden()
    static.locator('[data-work] summary').first.click()
    expect(static.locator('[data-work] details').first).to_have_attribute('open', '')
    assert not static.evaluate('document.documentElement.scrollWidth > window.innerWidth')
    static.close()
    static = plain.new_page()
    static.goto(urljoin(base, 'hn/school-reading/'), wait_until='networkidle')
    expect(static.locator('[data-book]:visible')).to_have_count(109)
    expect(static.locator('[data-reading-controls]')).to_be_hidden()
    assert static.locator('[data-book] p.reading-summary').count() == 109
    static.locator('[data-book] summary').first.click()
    expect(static.locator('[data-book] details').first).to_have_attribute('open', '')
    static.close()
    for kind in ['books', 'movies']:
        static = plain.new_page()
        response = static.goto(urljoin(base, f'hn/{kind}/'), wait_until='networkidle')
        assert response.status == 200
        expect(static.locator('[data-rank]:visible')).to_have_count(100)
        expect(static.locator('[data-controls]')).to_be_hidden()
        static.locator('[data-rank="1"] summary').click()
        expect(static.locator('[data-rank="1"] details')).to_have_attribute('open', '')
        static.close()
    plain.close()
    browser.close()
    print(f'PASS: 6 pages, {len(internal)} internal assets/links, two rankings, 109 student books and 197 history/documentary works; view/age/category/search intersections, URL/history restore, downloads/ZIP, quotes, keyboard, no-JS, reduced motion, 9 viewport sizes; no script errors.')
