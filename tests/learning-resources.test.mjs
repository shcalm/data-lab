import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

async function collection() {
  let module;
  try { module = await import('../src/lib/learning-resources.mjs'); } catch {}
  assert.ok(module, 'The learning resources collection has not been implemented');
  return module.getLearningResources();
}

async function selector() {
  let module;
  try { module = await import('../src/lib/learning-resources-filter.mjs'); } catch {}
  assert.ok(module, 'Learning resource filters have not been implemented');
  return module.selectLearningResources;
}

test('published learning resources preserve the reviewed descriptions, topic memberships and quotations', async () => {
  const project = await collection();
  const original = JSON.parse(readFileSync(`public/${project.dataPath}/resources.json`, 'utf8'));
  assert.equal(project.entries.length, 83);
  assert.equal(project.topics.length, 25);
  assert.equal(project.sources.length, 36);
  assert.equal(project.entries.flatMap(r => r.evidence).length, 183);
  assert.equal(new Set(project.groups.flatMap(g => g.topics.map(t => t.id))).size, 25);
  assert.equal(project.groups.reduce((sum,g) => sum + g.topics.length, 0), 25);
  assert.deepEqual(project.kinds.map(k => k.count), [43,18,13,8,1]);
  assert.deepEqual(project.metadata.exact_archive_quote_counts, { exact:181, different:2 });
  project.entries.forEach((entry,index) => {
    const raw = original.resources[index];
    for (const key of Object.keys(raw)) assert.deepEqual(entry[key],raw[key],`${entry.id}/${key}`);
    assert.ok(entry.kind && entry.searchText);
    assert.ok(entry.evidence.some(e => ['recommendation','qualified_recommendation'].includes(e.stance)));
    assert.ok(!('rank' in entry) && !('mentions' in entry));
  });
  assert.equal(project.entries.filter(r => r.evidence.some(e => e.stance==='criticism')).length > 0,true);
});

test('resource search combines shared topic membership, resource kind and normalized keywords', async () => {
  const { entries } = await collection();
  const select = await selector();
  const before = structuredClone(entries);
  assert.equal(select(entries).length,83);
  assert.deepEqual(select(entries,{topic:'cs-foundations'}).map(r => r.id),['cs-cs50','cs-sicp','cs-nand2tetris']);
  assert.equal(select(entries,{kind:'path'}).length,8);
  assert.equal(select(entries,{topic:'cs-foundations',kind:'book'}).length,0);
  assert.deepEqual(select(entries,{q:' ＭＡＰＲＥＤＵＣＥ　ＧＯ '} ).map(r => r.id),['cs-mit-distributed']);
  assert.deepEqual(select(entries,{q:'Model Thinking 模型'}).map(r => r.id),['hum-model-thinking']);
  assert.deepEqual(select(entries,{topic:'hum-economics-finance',q:'资产负债表'}).map(r => r.id),['hum-money-banking']);
  assert.equal(select(entries,{topic:'unknown',kind:'unknown'}).length,83);
  assert.equal(select(entries,{q:'完全不存在的资源-998877'}).length,0);
  assert.deepEqual(entries,before);
});
