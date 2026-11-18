import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

async function loadCollection() {
  let module;
  try { module = await import('../src/lib/history-documentaries.mjs'); } catch {}
  assert.ok(module, 'History and documentary catalogue is not implemented');
  return module.getHistoryDocumentaries();
}

async function loadFilter() {
  let module;
  try { module = await import('../src/lib/history-documentaries-filter.mjs'); } catch {}
  assert.ok(module, 'History and documentary filters are not implemented');
  return module.selectHistoryWorks;
}

test('history collection preserves all reviewed works, formats and source evidence', async () => {
  const { entries, discussions, views, dataPath } = await loadCollection();
  assert.equal(entries.length, 197);
  assert.equal(new Set(entries.map(work => work.id)).size, 197);
  assert.deepEqual(views.map(view => view.count), [100, 97, 64]);
  assert.equal(discussions.length, 18);
  assert.equal(entries.reduce((sum, work) => sum + work.evidence.length, 0), 404);
  const formats = entries.reduce((counts, work) => {
    counts[work.format] = (counts[work.format] ?? 0) + 1;
    return counts;
  }, {});
  assert.deepEqual(formats, { book: 100, 'documentary film': 68, 'documentary series': 28, 'documentary short': 1 });
  for (const work of entries) {
    assert.ok(work.title && work.zh && work.category && work.summary.length >= 25);
    assert.ok(work.evidence.length > 0);
    assert.ok(!('rank' in work) && !('mentions' in work));
    for (const evidence of work.evidence) {
      assert.ok(evidence.quote && evidence.stance);
      assert.ok(discussions.some(discussion => discussion.id === evidence.discussion_id));
      assert.equal(evidence.item_url, `https://news.ycombinator.com/item?id=${evidence.item_id}`);
    }
  }
  for (const [file, kind] of [['历史书目.json', 'books'], ['纪录片单.json', 'documentaries']]) {
    const original = JSON.parse(readFileSync(`public/${dataPath}/${file}`, 'utf8'));
    const displayed = entries.filter(work => work.kind === kind);
    assert.deepEqual(displayed.map(work => work.title), original.map(work => work.title));
    assert.deepEqual(displayed.map(work => work.summary), original.map(work => work.summary_zh));
  }
});

test('three views intersect with category and Unicode search without changing source order', async () => {
  const { entries } = await loadCollection();
  const select = await loadFilter();
  const order = entries.map(work => work.id);
  assert.equal(select(entries).length, 100);
  assert.equal(select(entries, { view: 'documentaries' }).length, 97);
  assert.equal(select(entries, { view: 'history-documentaries' }).length, 64);
  assert.equal(select(entries, { view: 'unknown' }).length, 100);
  assert.equal(select(entries, { view: 'books', category: '亚洲史' }).length, 6);
  const war = select(entries, { view: 'history-documentaries', category: '战争与大屠杀' });
  assert.equal(war.length, 12);
  assert.ok(war.every(work => work.historyRelated));
  assert.deepEqual(select(entries, { view: 'history-documentaries', q: ' ＦＯＧ　ＭＯＲＲＩＳ ' }).map(work => work.rawId), ['fog-of-war']);
  assert.deepEqual(select(entries, { view: 'books', q: '丝绸之路 欧亚' }).map(work => work.rawId), ['silk-roads']);
  assert.deepEqual(select(entries, { view: 'documentaries', q: 'Internet’s Own Boy' }).map(work => work.rawId), ['internets-own-boy']);
  assert.equal(select(entries, { view: 'history-documentaries', q: 'AlphaGo' }).length, 0);
  assert.equal(select(entries, { view: 'documentaries', q: 'AlphaGo' }).length, 1);
  assert.equal(select(entries, { view: 'books', category: '战争与外交史', q: '丝绸之路' }).length, 0);
  assert.equal(select(entries, { q: '不存在的作品 998877' }).length, 0);
  assert.deepEqual(entries.map(work => work.id), order);
});
