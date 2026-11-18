import { readFileSync } from 'node:fs';

const read = path => JSON.parse(readFileSync(path, 'utf8'));
let cached;

function enhance(entry) {
  let articleUrl = '';
  let domain = 'HN 自帖';
  try {
    const url = new URL(entry.url);
    if (['http:', 'https:'].includes(url.protocol)) {
      articleUrl = url.href;
      domain = url.hostname.replace(/^www\./, '');
    }
  } catch {}
  return { ...entry, articleUrl, domain,
    searchText: [entry.title, entry.guide_zh, entry.current_title, entry.author, domain, entry.excerpt].filter(Boolean).join(' ') };
}

export function getMonthlyTop() {
  if (cached) return cached;
  const project = read('data/monthly-top.json');
  const data = read(`public/${project.dataPath}/rankings.json`);
  const months = data.months.map(month => ({ ...month, entries: month.entries.map(enhance) }));
  const years = [...new Set(months.map(month => month.month.slice(0, 4)))].reverse().map(year => ({
    year, months: months.filter(month => month.month.startsWith(year)),
  }));
  cached = { ...project, metadata: data.metadata, months, years, allTime: data.all_time.map(enhance),
    verification: read(`public/${project.dataPath}/verification.json`) };
  return cached;
}
