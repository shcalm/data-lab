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
pages = {'home': '', 'books': 'hn/books/', 'movies': 'hn/movies/', 'about': 'about/'}

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

    page.goto(urljoin(base, 'hn/movies/?q=Dune&sort=year'), wait_until='networkidle')
    expect(page.locator('[data-rank]:visible')).to_have_count(2)
    assert page.locator('[data-rank]:visible').first.get_attribute('data-rank') == '86'
    page.goto(urljoin(base, 'hn/movies/?category=不存在&sort=wrong'), wait_until='networkidle')
    expect(page.locator('[data-rank]:visible')).to_have_count(100)

    for width, height in [(320, 740), (375, 900), (768, 1024), (844, 390), (1440, 1080)]:
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

    page.emulate_media(reduced_motion='reduce')
    assert page.locator('html').evaluate('el => getComputedStyle(el).scrollBehavior') == 'auto'
    page.goto(base, wait_until='networkidle')
    page.keyboard.press('Tab')
    expect(page.locator('.skip-link')).to_be_focused()
    assert not errors, errors

    plain = browser.new_context(java_script_enabled=False, viewport={'width': 375, 'height': 900})
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
    print(f'PASS: 4 pages, {len(internal)} internal assets/links, both complete rankings and exports; search, category, sort, URL restore, keyboard, no-JS, reduced motion, 5 viewport sizes; no script errors.')
