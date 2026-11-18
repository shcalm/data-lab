import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

const readJson = (path) => JSON.parse(readFileSync(resolve(path), 'utf8'));
const project = readJson('data/school-reading.json');
let cache;

/** The public JSON is also the build input, so reading and downloads agree. */
export function getSchoolReading() {
  if (cache) return cache;
  const root = `public/${project.dataPath}`;
  const rows = readJson(`${root}/书目总表.json`);
  const metadata = readJson(`${root}/数据说明.json`);
  const provenance = new Map(readJson(`${root}/书目来源.json`).map(row => [row.原书名, row]));
  const ageIds = ['6-8', '9-11', '12-14', '15-18', 'unspecified'];
  const ageGroups = metadata.按年龄.map((group, i) => ({
    id: ageIds[i], label: group.分组, shortLabel: group.分组.split('／')[0],
    count: group.书目数量, file: group.文件,
  }));
  const entries = rows.map(row => {
    const source = provenance.get(row.原书名);
    if (!source?.分龄证据?.length) throw new Error(`Missing reading evidence: ${row.原书名}`);
    const labels = row.年龄分组.split('；');
    return {
      id: source.分龄证据[0].evidence_id.split(':')[0],
      title: row.原书名, zh: row.书名, author: row.作者,
      category: row.类别, summary: row.内容简介, form: row.作品形式,
      ageIds: ageGroups.filter(group => labels.includes(group.label)).map(group => group.id),
      ageBasis: row.分龄依据, note: row.备注,
      evidence: source.分龄证据.filter(e => labels.includes('年龄未明确') || e.kind !== 'unspecified'),
    };
  });
  const categories = metadata.按类别.map(group => ({
    name: group.类别, count: group.书目数量, file: `按类别/${group.类别}`,
  }));
  cache = {
    ...project, entries, ageGroups, categories,
    knownAgeCount: metadata.有分龄依据的不同书目数,
    unknownAgeCount: metadata.年龄未明确的不同书目数,
  };
  return cache;
}
