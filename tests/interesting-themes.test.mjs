import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

async function collection() {
  let module;
  try { module = await import('../src/lib/interesting-themes.mjs'); } catch {}
  assert.ok(module, 'The reviewed themes collection has not been implemented');
  return module.getInterestingThemes();
}

async function filter() {
  let module;
  try { module = await import('../src/lib/interesting-themes-filter.mjs'); } catch {}
  assert.ok(module, 'Theme search and group filters have not been implemented');
  return module.selectThemes;
}

test('theme collection preserves all reviewed claims, caveats, sources and exact evidence', async () => {
  const { entries, groups, metadata, dataPath, verification, sources } = await collection();
  const original = JSON.parse(readFileSync(`public/${dataPath}/themes.json`, 'utf8'));
  assert.equal(entries.length, 30);
  assert.equal(new Set(entries.map(theme => theme.id)).size, 30);
  assert.deepEqual(groups.map(group => group.count), [7, 9, 7, 7]);
  assert.equal(entries.filter(theme => theme.starter).length, 12);
  assert.equal(new Set(entries.flatMap(theme => theme.sources.map(source => source.story_id))).size, 62);
  assert.equal(entries.flatMap(theme => theme.sources.flatMap(source => source.evidence)).length, 106);
  assert.equal(sources.length, 62);
  assert.equal(metadata.archive.unique_indexed_stories, 4755791);
  assert.equal(verification.failure_count, 0);
  assert.equal(verification.api_and_archive_quote_match_count, 106);
  assert.equal(verification.cross_snapshot_author_difference_count, 2);
  entries.forEach((theme, index) => {
    const raw = original.themes[index];
    for (const key of ['title_zh', 'one_sentence_zh', 'insight_zh', 'mechanism_zh', 'caveat_zh', 'further_question_zh']) {
      assert.ok(theme[key]);
      assert.equal(theme[key], raw[key]);
    }
    assert.deepEqual(theme.sources, raw.sources);
    assert.equal(theme.starter, metadata.starter_theme_ids.includes(theme.id));
    assert.ok(!('rank' in theme) && !('mentions' in theme));
    for (const source of theme.sources) {
      assert.ok(sources.some(row => row.story_id === source.story_id));
      assert.equal(source.url, `https://news.ycombinator.com/item?id=${source.story_id}`);
      for (const evidence of source.evidence) {
        assert.ok(evidence.api_quote_verified && evidence.archive_quote_verified);
        assert.ok(evidence.author && evidence.api_author && evidence.archive_author);
        assert.equal(evidence.url, `https://news.ycombinator.com/item?id=${evidence.comment_id}`);
      }
    }
  });
});

test('theme search combines group, selected reading and normalized multikeyword queries', async () => {
  const { entries } = await collection();
  const select = await filter();
  const before = structuredClone(entries);
  assert.equal(select(entries).length, 30);
  assert.equal(select(entries, { view: 'starters' }).length, 12);
  assert.equal(select(entries, { group: 'science' }).length, 7);
  assert.equal(select(entries, { group: 'science', view: 'starters' }).length, 4);
  assert.equal(select(entries, { group: 'unknown', view: 'wrong' }).length, 30);
  assert.deepEqual(select(entries, { q: ' ＣＲＤＴＳ　语义 ' }).map(theme => theme.id), ['computing_convergence_not_agreement']);
  assert.deepEqual(select(entries, { q: '阳光 窗口' }).map(theme => theme.id), ['science-sky-as-heat-sink']);
  assert.equal(select(entries, { group: 'cognition', q: '阳光 窗口' }).length, 0);
  assert.deepEqual(select(entries, { q: 'Goodhart’s' }).map(theme => theme.id), ['metrics-change-behaviour']);
  assert.equal(select(entries, { q: '完全不存在-998877' }).length, 0);
  assert.deepEqual(entries, before);
});
