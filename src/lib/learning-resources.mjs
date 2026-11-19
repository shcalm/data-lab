import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

const readJson = path => JSON.parse(readFileSync(resolve(path),'utf8'));
const project = readJson('data/learning-resources.json');
const kinds = [
  { id:'course', label:'大学课与MOOC', formats:['university_course','mooc'] },
  { id:'practice', label:'讲座与实作', formats:['online_course','lecture_series','video_series','tutorial','practice_tool','interactive_course'] },
  { id:'book', label:'教材与书籍', formats:['book','online_book'] },
  { id:'path', label:'路线与课程目录', formats:['study_path','course_directory'] },
  { id:'podcast', label:'播客', formats:['podcast'] },
];
const formatLabels = { university_course:'大学课程', mooc:'MOOC', online_course:'在线课程',
  lecture_series:'系列讲座', video_series:'系列视频', tutorial:'教程', practice_tool:'练习工具',
  interactive_course:'交互课程', book:'教材／书籍', online_book:'在线教材', study_path:'学习路线',
  course_directory:'课程目录', podcast:'播客' };
let cache;

/** The web reader adds navigation fields to the unmodified reviewed resources. */
export function getLearningResources() {
  if (cache) return cache;
  const original = readJson(`public/${project.dataPath}/resources.json`);
  const topics = original.topics;
  const topicMap = new Map(topics.map(t => [t.id,t]));
  const entries = original.resources.map(resource => {
    const kind = kinds.find(k => k.formats.includes(resource.format));
    if (!kind) throw new Error(`Unknown resource format: ${resource.format}`);
    return { ...resource, kind:kind.id, formatLabel:formatLabels[resource.format],
      topicLabels:resource.topics.map(id => topicMap.get(id).title_zh),
      searchText:[resource.title,resource.provider,resource.summary_zh,resource.prerequisites_zh,
        resource.why_recommended_zh,...resource.topics.map(id => topicMap.get(id).title_zh),
        ...resource.evidence.map(e => e.quote)].join(' ') };
  });
  cache = { ...project, entries, topics, metadata:original.metadata, sources:original.sources,
    groups:project.groups.map(group => ({...group,topics:group.topicIds.map(id => topicMap.get(id))})),
    kinds:kinds.map(kind => ({...kind,count:entries.filter(r => r.kind===kind.id).length})),
    downloadFiles:[
      {file:'resources.csv',label:'资源表格',format:'CSV'},
      {file:'resources.json',label:'完整资源与引文',format:'JSON'},
      {file:'学习资源总表.md',label:'中文完整介绍',format:'Markdown'},
      {file:'hn-learning-resources.zip',label:'全部整理',format:'ZIP'},
    ] };
  return cache;
}
