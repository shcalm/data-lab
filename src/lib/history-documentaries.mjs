import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

const readJson = path => JSON.parse(readFileSync(resolve(path), 'utf8'));
const project = readJson('data/history-documentaries.json');
const categoryOrder = [
  '世界与区域通史', '古代史料与回忆录', '欧洲史', '亚洲史', '美国史',
  '战争与外交史', '历史人物传记', '经济与社会史', '思想与文化史',
  '科学史', '技术与工业史', '计算机与信息史',
  '战争与大屠杀', '政治与社会', '经济与商业', '科技与思想', '计算机与互联网',
  '航天', '文化与艺术', '自然与科学', '职业、人物与日常生活', '体育与户外',
  '调查与公共议题', '影像散文与实验纪录',
];
const formatLabels = {
  book: '书籍', 'documentary film': '纪录长片',
  'documentary series': '纪录系列', 'documentary short': '纪录短片',
};
let cache;

/** Build from the exact reviewed public exports, also offered for download. */
export function getHistoryDocumentaries() {
  if (cache) return cache;
  const root = `public/${project.dataPath}`;
  const books = readJson(`${root}/历史书目.json`);
  const documentaries = readJson(`${root}/纪录片单.json`);
  const entries = [
    ...books.map(work => ({ work, kind: 'books' })),
    ...documentaries.map(work => ({ work, kind: 'documentaries' })),
  ].map(({ work, kind }) => ({
    id: `${kind}-${work.id}`, rawId: work.id, kind,
    title: work.title, zh: work.title_zh || work.title,
    creator: work.creators.join('、'), year: work.year,
    format: work.format, formatLabel: formatLabels[work.format],
    category: work.category, summary: work.summary_zh, note: work.note_zh,
    historyRelated: work.history_related === true,
    evidence: work.mentions,
  }));
  const views = [
    { id: 'books', label: '历史书目', subtitle: '书籍与系列', count: books.length, file: '历史书目' },
    { id: 'documentaries', label: '全部纪录片', subtitle: '各种题材', count: documentaries.length, file: '纪录片单' },
    { id: 'history-documentaries', label: '历史纪录片', subtitle: '只看历史题材', count: documentaries.filter(work => work.history_related).length, file: '历史题材纪录片' },
  ];
  const collections = ['books', 'documentaries'].map(kind => {
    const works = entries.filter(work => work.kind === kind);
    return {
      kind, label: kind === 'books' ? '历史书目' : '纪录片单',
      categories: categoryOrder.filter(name => works.some(work => work.category === name)).map(name => ({
        name, entries: works.filter(work => work.category === name),
      })),
    };
  });
  cache = { ...project, entries, views, collections, discussions: readJson(`${root}/讨论来源.json`) };
  return cache;
}
