import test from 'node:test';
import assert from 'node:assert/strict';

async function loadData() {
  let module;
  try { module = await import('../src/lib/school-reading.mjs'); } catch {}
  assert.ok(module, 'The school reading book catalogue has not been implemented');
  return module.getSchoolReading();
}

async function loadFilter() {
  let module;
  try { module = await import('../src/lib/school-reading-filter.mjs'); } catch {}
  assert.ok(module, 'Age and category book filtering has not been implemented');
  return module.selectBooks;
}

test('school reading contains complete unique books with exclusive unknown ages', async () => {
  const { entries, ageGroups, categories } = await loadData();
  assert.equal(entries.length, 109);
  assert.equal(new Set(entries.map(book => book.title)).size, 109);
  assert.equal(new Set(entries.map(book => book.id)).size, 109);
  assert.deepEqual(ageGroups.map(group => group.count), [30, 16, 27, 23, 29]);
  assert.equal(categories.length, 9);
  assert.equal(categories.reduce((sum, group) => sum + group.count, 0), 109);
  const unknown = entries.filter(book => book.ageIds.includes('unspecified'));
  assert.equal(unknown.length, 29);
  assert.ok(unknown.every(book => book.ageIds.length === 1));
  assert.equal(entries.filter(book => !book.ageIds.includes('unspecified')).length, 80);
  for (const book of entries) {
    assert.ok(book.zh && book.title && book.author && book.summary.length >= 25);
    assert.ok(book.ageIds.length && book.ageBasis && book.evidence.length);
    assert.ok(!('rank' in book) && !('mentions' in book));
    assert.ok(categories.some(category => category.name === book.category));
  }
  const parentReading = entries.find(book => book.title.includes('Defying Hitler'));
  assert.ok(parentReading.note.includes('家长给6岁孩子朗读'));
});

test('age, category and Unicode search intersect while preserving the source', async () => {
  const { entries } = await loadData();
  const selectBooks = await loadFilter();
  const titles = entries.map(book => book.title);
  assert.equal(selectBooks(entries).length, 109);
  for (const [age, count] of [['6-8', 30], ['9-11', 16], ['12-14', 27], ['15-18', 23], ['unspecified', 29]]) {
    assert.equal(selectBooks(entries, { age }).length, count);
  }
  const science = selectBooks(entries, { age: '6-8', category: '科普与自然' });
  assert.equal(science.length, 3);
  assert.ok(science.every(book => book.ageIds.includes('6-8') && book.category === '科普与自然'));
  assert.deepEqual(selectBooks(entries, { age: '12-14', q: ' ＯＲＷＥＬＬ ' }).map(book => book.title), ['1984']);
  assert.equal(selectBooks(entries, { age: '6-8', category: '科普与自然', q: '万物 运转' }).length, 1);
  assert.equal(selectBooks(entries, { age: '6-8', q: '神经漫游者' }).length, 0);
  assert.equal(selectBooks(entries, { q: '完全不存在的书 998877' }).length, 0);
  assert.deepEqual(entries.map(book => book.title), titles);
});
