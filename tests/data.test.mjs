import test from 'node:test';
import assert from 'node:assert/strict';

test('source rankings retain their 100 unique ranked works and verified counts', async () => {
  let module;
  try { module = await import('../src/lib/data.mjs'); } catch {}
  assert.ok(module, 'The shared, validated project loader has not been implemented');
  const { projects, getProject } = module;
  assert.ok(projects.length >= 2);
  assert.equal(new Set(projects.map(x => x.id)).size, projects.length);
  assert.equal(new Set(projects.map(x => x.path)).size, projects.length);
  assert.equal(new Set(projects.map(x => x.exportSlug)).size, projects.length);
  for (const project of projects) {
    const data = getProject(project.id);
    assert.equal(data.entries.length, project.expectedCount);
    assert.deepEqual(data.entries.map(x => x.rank), Array.from({ length: project.expectedCount }, (_, i) => i + 1));
    assert.equal(new Set(data.entries.map(x => `${x.title}/${x.year ?? ''}`)).size, project.expectedCount);
    for (const [i, row] of data.entries.entries()) {
      assert.ok(Number.isInteger(row.mentions) && row.mentions > 0);
      assert.equal(row.mentions, row.stories + row.comments);
      assert.ok(row.summary.length >= 30, `${row.title} needs an introduction`);
      assert.ok(row.category);
      if (i) assert.ok(data.entries[i - 1].mentions >= row.mentions);
    }
  }
  assert.equal(getProject('books').entries[0].mentions, 8143);
  assert.equal(getProject('movies').entries[0].mentions, 4067);
  assert.equal(getProject('books').source.eligibleItems, 34721984);
});

test('CSV output quotes arbitrary content and preserves Unicode and counts', async () => {
  let module;
  try { module = await import('../src/lib/data.mjs'); } catch {}
  assert.ok(module, 'The data exporter has not been implemented');
  const text = module.toCsv([{ rank: 1, zh: '书,名', title: 'A "quote"', author: '作者', mentions: 3, stories: 1, comments: 2, summary: '第一行\n第二行', category: '文学' }]);
  assert.ok(text.startsWith('\ufeff排名,'));
  assert.ok(text.includes('"书,名"'));
  assert.ok(text.includes('"A ""quote"""'));
  assert.ok(text.includes('"第一行\n第二行"'));
});
