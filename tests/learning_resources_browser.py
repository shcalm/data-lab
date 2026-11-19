"""Check the learning reader against its reviewed data, with and without JavaScript."""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import quote, urljoin

from playwright.sync_api import sync_playwright, expect

parser = argparse.ArgumentParser()
parser.add_argument('--base-url',default='http://127.0.0.1:4327/data-lab/')
parser.add_argument('--core-downloads',action='store_true',help='Check the main exports only on a remote site.')
args = parser.parse_args()
base = args.base_url.rstrip('/')+'/'
root = Path(__file__).resolve().parents[1]
exports = root/'public/downloads/hn-learning-resources'
canonical = json.loads((exports/'resources.json').read_text())
output = root/'test-results'
output.mkdir(exist_ok=True)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(viewport={'width':1440,'height':1050})
    page = context.new_page()
    errors = []
    page.on('pageerror',lambda error:errors.append(str(error)))
    page.goto(base,wait_until='networkidle')
    expect(page.locator('.project-learning h3')).to_contain_text('课程与学习资源')
    expect(page.locator('.year-figure > span')).to_have_text('8')
    page.get_by_role('link',name='学习资源',exact=True).click()
    page.wait_for_url('**/hn/learning-resources/')
    rows = page.locator('[data-learning-resource]:visible')
    expect(rows).to_have_count(83)
    expect(page.locator('.learning-topic-group')).to_have_count(6)
    expect(page.locator('.learning-topic-group li')).to_have_count(25)

    page.locator('#learning-topic').select_option('cs-foundations')
    expect(rows).to_have_count(3)
    page.locator('#learning-kind').select_option('book')
    expect(rows).to_have_count(0)
    expect(page.locator('[data-learning-empty]')).to_be_visible()
    page.locator('[data-learning-empty] button').click()
    expect(rows).to_have_count(83)
    expect(page.locator('#learning-search')).to_be_focused()
    page.locator('#learning-search').fill('Model Thinking 模型')
    expect(rows).to_have_count(1)
    assert rows.first.get_attribute('data-learning-resource')=='hum-model-thinking'
    page.reload(wait_until='networkidle')
    expect(rows).to_have_count(1)
    expect(page.locator('#learning-search')).to_have_value('Model Thinking 模型')
    page.locator('[data-learning-reset]').first.click()
    page.locator('.learning-topic-group summary').first.click()
    page.locator('[data-learning-topic-link="cs-systems"]').first.click()
    expect(rows).to_have_count(6)
    expect(page.locator('#learning-topic')).to_have_value('cs-systems')
    expect(page.locator('[data-learning-heading]')).to_be_focused()
    assert 'topic=cs-systems' in page.url
    page.goto(urljoin(base,'hn/learning-resources/?topic=hum-music&q=missing#resource-cs-mit-distributed'),wait_until='networkidle')
    expect(rows).to_have_count(83)
    expect(page.locator('#resource-cs-mit-distributed [data-learning-reader]')).to_have_attribute('open','')
    assert '?' not in page.url
    page.goto(urljoin(base,'hn/learning-resources/?topic=invalid&kind=invalid'),wait_until='networkidle')
    expect(rows).to_have_count(83)
    reader = page.locator('[data-learning-reader]').first
    reader.locator('summary').focus()
    page.keyboard.press('Enter')
    expect(reader).to_have_attribute('open','')
    page.goto(urljoin(base,'hn/learning-resources/'),wait_until='networkidle')
    for width in [320,375,620,621,800,801,1000,1001,1151,1280,1440]:
        page.set_viewport_size({'width':width,'height':1000})
        assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'),width
    page.set_viewport_size({'width':1440,'height':1050})
    page.goto(urljoin(base,'hn/learning-resources/'),wait_until='networkidle')
    page.screenshot(path=str(output/'learning-desktop.png'))
    page.set_viewport_size({'width':375,'height':950})
    page.goto(urljoin(base,'hn/learning-resources/?topic=hum-economics-finance#learning-results'),wait_until='networkidle')
    expect(rows).to_have_count(4)
    page.locator('#learning-results').scroll_into_view_if_needed()
    page.screenshot(path=str(output/'learning-mobile.png'))
    rows.first.locator('summary').click()
    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
    assert not errors,errors

    nojs = browser.new_context(java_script_enabled=False,viewport={'width':375,'height':950})
    static = nojs.new_page()
    static.goto(urljoin(base,'hn/learning-resources/'),wait_until='networkidle')
    expect(static.locator('[data-learning-resource]:visible')).to_have_count(83)
    expect(static.locator('[data-learning-controls]')).to_be_hidden()
    assert static.locator('blockquote').count()==183
    for resource in canonical['resources']:
        row=static.locator(f"#resource-{resource['id']}")
        assert row.locator('h3').text_content().strip()==resource['title']
        assert row.locator('.learning-summary').text_content().strip()==resource['summary_zh']
        assert row.locator('.learning-reason').text_content().strip().endswith(resource['why_recommended_zh'])
        assert row.locator('.learning-open').get_attribute('href')==resource['resource_url']
        links = row.locator('a').evaluate_all('(links)=>links.map(a=>a.getAttribute("href"))')
        supplementary = [link['url'] for link in resource.get('related_urls',[])] + resource.get('related_resource_urls',[])
        assert all(url in links for url in supplementary),(resource['id'],'missing supplementary entrance')
        assert row.locator('.learning-reading-notes p').first.text_content().strip()==resource['prerequisites_zh']
        assert row.locator('blockquote').all_text_contents()==[e['quote'] for e in resource['evidence']]
        assert row.locator('.learning-evidence-meta a').evaluate_all('(links)=>links.map(a=>a.href)')==[e['item_url'] for e in resource['evidence']]
    static.locator('[data-learning-reader] summary').first.click()
    expect(static.locator('[data-learning-reader]').first).to_have_attribute('open','')
    print('PASS: all83 resource descriptions,183 quotations and83 entrances preserved; no-JS, filters, URL restoration, hash recovery, keyboard and11 viewport widths.',flush=True)

    names = ['resources.json','resources.csv','evidence.json','学习资源总表.md','hn-learning-resources.zip'] if args.core_downloads else [p.relative_to(exports).as_posix() for p in exports.rglob('*') if p.is_file()]
    for name in names:
        response=context.request.get(urljoin(base,'downloads/hn-learning-resources/'+quote(name)),timeout=180000)
        assert response.status==200,(name,response.status)
        assert hashlib.sha256(response.body()).digest()==hashlib.sha256((exports/name).read_bytes()).digest(),name
    print(f'PASS: {len(names)} downloads match reviewed export bytes; zero browser errors.',flush=True)
    browser.close()
