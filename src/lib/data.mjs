import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

// Astro and the test runner execute from the repository root.
const readData = (file) => JSON.parse(readFileSync(resolve('data', file), 'utf8'));
export const projects = readData('projects.json');

const cache = new Map();

/** Load a versioned ranking and join editorial annotations without changing it. */
export function getProject(id) {
  if (cache.has(id)) return cache.get(id);
  const project = projects.find((item) => item.id === id);
  if (!project) throw new Error(`Unknown project: ${id}`);

  const snapshotPath = `snapshots/${project.snapshot}`;
  const source = readData(`${snapshotPath}/source.json`);
  const ranking = readData(`${snapshotPath}/${project.id}.json`);
  const annotations = readData(project.annotations);
  const entries = ranking.map((entry) => {
    const key = entry.year ? `${entry.title} (${entry.year})` : entry.title;
    const annotation = annotations[key];
    if (!annotation?.summary || !annotation?.category) {
      throw new Error(`Missing introduction: ${id}/${key}`);
    }
    return { ...entry, ...annotation };
  });
  const categories = [...new Set(entries.map((entry) => entry.category))]
    .map((name) => ({ name, count: entries.filter((entry) => entry.category === name).length }))
    .sort((a, b) => b.count - a.count || a.name.localeCompare(b.name, 'zh-CN'));

  const result = { ...project, source, entries, categories };
  cache.set(id, result);
  return result;
}

/** A BOM lets common spreadsheet applications recognize the Chinese text. */
export function toCsv(entries) {
  const columns = [
    ['排名', 'rank'], ['中文名', 'zh'], ['原名', 'title'], ['作者', 'author'],
    ['上映年份', 'year'], ['分类', 'category'], ['提及数', 'mentions'],
    ['帖子提及数', 'stories'], ['评论提及数', 'comments'], ['简介', 'summary'],
  ];
  const escape = (value) => {
    const text = String(value ?? '');
    return /[",\r\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
  };
  return '\ufeff' + [
    columns.map(([name]) => name).join(','),
    ...entries.map((entry) => columns.map(([, key]) => escape(entry[key])).join(',')),
  ].join('\r\n') + '\r\n';
}

export const formatNumber = (value) => new Intl.NumberFormat('en-US').format(value);
