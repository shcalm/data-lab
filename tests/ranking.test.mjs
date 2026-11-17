import test from 'node:test';
import assert from 'node:assert/strict';
import { getProject } from '../src/lib/data.mjs';

const movies = getProject('movies').entries;
const books = getProject('books').entries;
const load = async () => {
  let module;
  try { module = await import('../src/lib/ranking.mjs'); } catch {}
  assert.ok(module, 'The shared ranking search and sort behavior is missing');
  return module.selectEntries;
};

test('search finds Chinese, English, authors, and multiword queries without changing source ranks', async () => {
  const select = await load();
  assert.deepEqual(select(movies, { q: ' ＭＡＴＲＩＸ ' }).map(x => x.rank), [1]);
  assert.deepEqual(select(movies, { q: '黑客帝国' }).map(x => x.rank), [1]);
  assert.deepEqual(select(movies, { q: 'blade 2049' }).map(x => x.rank), [20]);
  assert.ok(select(books, { q: 'Orwell' }).some(x => x.title === '1984'));
  assert.equal(select(movies, { q: '完全不存在的作品xyz' }).length, 0);
  assert.equal(select(movies).length, 100);
});

test('category and sort compose, preserve ties, and distinguish film versions', async () => {
  const select = await load();
  const docs = select(movies, { category: '纪录片', sort: 'least' });
  assert.ok(docs.length > 0 && docs.every(x => x.category === '纪录片'));
  assert.equal(docs[0].title, 'An Inconvenient Truth');
  assert.deepEqual(select(movies, { q: 'Dune', sort: 'year' }).map(x => x.year), [2021, 1984]);
  const least = select(movies, { sort: 'least' });
  assert.equal(least[0].rank, 99);
  assert.equal(least[1].rank, 100);
  const alpha = select(movies, { sort: 'title' });
  assert.equal(alpha[0].title, '12 Monkeys');
  assert.equal(movies[0].rank, 1);
});
