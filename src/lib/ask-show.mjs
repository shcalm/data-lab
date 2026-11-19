import { readFileSync } from 'node:fs';
import { enhance } from './monthly-top.mjs';

const read = path => JSON.parse(readFileSync(path, 'utf8'));
let cached;

export function getAskShow() {
  if (cached) return cached;
  const project = read('data/ask-show.json');
  const data = read(`public/${project.dataPath}/rankings.json`);
  const channels = Object.fromEntries(Object.entries(data.channels).map(([id, channel]) => {
    const months = channel.months.map(month => ({ ...month, entries: month.entries.map(enhance) }));
    const years = [...new Set(months.map(month => month.month.slice(0,4)))].reverse().map(year => ({
      year, months: months.filter(month => month.month.startsWith(year)),
    }));
    return [id, { ...channel, months, years }];
  }));
  cached = { ...project, metadata: data.metadata, channels,
    verification: read(`public/${project.dataPath}/verification.json`) };
  return cached;
}
