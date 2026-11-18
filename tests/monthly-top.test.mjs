import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

async function collection() {
  let mod;
  try { mod = await import('../src/lib/monthly-top.mjs'); } catch {}
  assert.ok(mod, 'Monthly Top20 collection is not implemented');
  return mod.getMonthlyTop();
}

test('monthly archive preserves a continuous calendar, exact ranked values and checked source fields', async () => {
  const data = await collection();
  const raw = JSON.parse(readFileSync(`public/${data.dataPath}/rankings.json`, 'utf8'));
  assert.equal(data.months.length, 239);
  assert.equal(data.metadata.eligible_story_count, 4755791);
  assert.equal(data.months[0].month, '2006-10');
  assert.equal(data.months.at(-1).month, '2026-08');
  assert.deepEqual(data.months.filter(m => !m.entries.length).map(m => m.month), ['2006-11', '2007-01']);
  assert.equal(data.months.find(m => m.month === '2006-12').entries.length, 1);
  assert.equal(data.months.flatMap(m => m.entries).length, 4721);
  assert.equal(data.allTime.length, 20);
  assert.equal(data.verification.failure_count, 0);
  const seen = new Set();
  const compare = (a, b) => b.score - a.score || a.time_utc.localeCompare(b.time_utc) || a.id - b.id;
  data.months.forEach((month, i) => {
    assert.equal(month.month, new Date(Date.UTC(2006, 9 + i)).toISOString().slice(0, 7));
    assert.equal(month.entries.length, Math.min(20, month.eligible_story_count));
    assert.deepEqual(month.entries.map(e => e.id), [...month.entries].sort(compare).map(e => e.id));
    for (const [j, entry] of month.entries.entries()) {
      assert.equal(entry.rank, j + 1);
      assert.equal(entry.time_utc.slice(0, 7), month.month);
      assert.ok(!seen.has(entry.id));
      seen.add(entry.id);
      for (const [key, value] of Object.entries(raw.months[i].entries[j])) assert.deepEqual(entry[key], value);
      assert.equal(entry.hn_url, `https://news.ycombinator.com/item?id=${entry.id}`);
      assert.ok(Number.isInteger(entry.score) && Number.isInteger(entry.comments));
      assert.ok(entry.articleUrl === '' || /^https?:\/\//.test(entry.articleUrl));
    }
  });
  assert.deepEqual(data.allTime.map(e => e.id), data.months.flatMap(m => m.entries).sort(compare).slice(0,20).map(e => e.id));
  for (const entry of data.allTime) {
    const monthEntry = data.months.flatMap(m => m.entries).find(e => e.id === entry.id);
    for (const key of ['title','score','comments','archive_score','archive_comments','time_utc','guide_zh']) assert.deepEqual(entry[key], monthEntry[key]);
  }
});

test('every story has a Chinese reading guide and missing-index exception preserves provenance', async () => {
  const data = await collection();
  const entries = data.months.flatMap(m => m.entries);
  assert.equal(data.metadata.guide_count, entries.length);
  for (const entry of entries) {
    assert.match(entry.guide_zh, /[\u3400-\u9fff]/u);
    assert.ok(entry.searchText.includes(entry.guide_zh));
    assert.ok(!entry.guide_zh.includes('\n'));
  }
  const missing = entries.find(e => e.id === 36860065);
  assert.ok(missing, 'Known above-cutoff local story must be included');
  assert.equal(missing.score, 1205);
  assert.equal(missing.score_source, 'firebase');
  assert.equal(missing.current_dead, true);
  assert.equal(missing.archive_score, 1202);
  assert.equal(missing.comments, missing.archive_comments);
  assert.equal(missing.comments_source, 'archive');
});

test('current-list search normalizes Unicode, combines words and preserves original rank', async () => {
  let mod;
  try { mod = await import('../src/lib/monthly-top-filter.mjs'); } catch {}
  assert.ok(mod, 'Monthly search is not implemented');
  const entries = [
    { id: 1, rank: 1, searchText: 'Google’s API ＳＳＨ 中文' },
    { id: 2, rank: 2, searchText: 'Google API 设计' },
  ];
  const before = structuredClone(entries);
  assert.deepEqual(mod.selectMonthlyStories(entries, ' google’s　SSH '), [entries[0]]);
  assert.deepEqual(mod.selectMonthlyStories(entries, 'Google API'), entries);
  assert.deepEqual(mod.selectMonthlyStories(entries, '中文 API'), [entries[0]]);
  assert.deepEqual(mod.selectMonthlyStories(entries, 'unknown'), []);
  assert.deepEqual(entries, before);
});
