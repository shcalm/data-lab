import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

const readJson = path => JSON.parse(readFileSync(resolve(path), 'utf8'));
const project = readJson('data/interesting-themes.json');
let cache;

/** The page and downloads use the same reviewed claims and source quotations. */
export function getInterestingThemes() {
  if (cache) return cache;
  const root = `public/${project.dataPath}`;
  const { metadata, themes } = readJson(`${root}/themes.json`);
  const starters = new Set(metadata.starter_theme_ids);
  const entries = themes.map(theme => ({
    ...theme,
    starter: starters.has(theme.id),
    searchText: [theme.title_zh, theme.category, theme.group_zh, theme.one_sentence_zh,
      theme.insight_zh, theme.mechanism_zh, theme.caveat_zh, theme.further_question_zh,
      ...theme.sources.map(source => source.title)].join(' '),
  }));
  const groups = project.groups.map(group => ({
    ...group, count: entries.filter(theme => theme.domain === group.id).length,
    entries: entries.filter(theme => theme.domain === group.id),
  }));
  cache = {
    ...project, entries, groups, metadata,
    sources: readJson(`${root}/sources.json`),
    verification: readJson(`${root}/verification.json`),
    downloadFiles: [
      { file: 'themes.csv', label: '主题表格', format: 'CSV' },
      { file: 'themes.json', label: '完整主题', format: 'JSON' },
      { file: 'README.md', label: '完整报告', format: 'Markdown' },
      { file: 'hn-interesting-themes.zip', label: '全部整理', format: 'ZIP' },
    ],
  };
  return cache;
}
