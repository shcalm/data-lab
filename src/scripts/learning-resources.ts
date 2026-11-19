import { selectLearningResources } from '../lib/learning-resources-filter.mjs';

const root = document.querySelector<HTMLElement>('[data-learning-collection]');
if (root) {
  const form = root.querySelector<HTMLFormElement>('[data-learning-controls]')!;
  const search = form.querySelector<HTMLInputElement>('#learning-search')!;
  const topic = form.querySelector<HTMLSelectElement>('#learning-topic')!;
  const kind = form.querySelector<HTMLSelectElement>('#learning-kind')!;
  const count = root.querySelector<HTMLElement>('[data-learning-count]')!;
  const heading = root.querySelector<HTMLElement>('[data-learning-heading]')!;
  const description = root.querySelector<HTMLElement>('[data-learning-description]')!;
  const empty = root.querySelector<HTMLElement>('[data-learning-empty]')!;
  const resets = [...root.querySelectorAll<HTMLButtonElement>('[data-learning-reset]')];
  const rows = new Map([...root.querySelectorAll<HTMLElement>('[data-learning-resource]')].map(row => [row.dataset.learningResource!,row]));
  const {entries,topics} = JSON.parse(root.querySelector('#learning-resources-data')!.textContent!);

  function apply(updateUrl=true) {
    const selected = selectLearningResources(entries,{topic:topic.value,kind:kind.value,q:search.value});
    const ids = new Set(selected.map((r:{id:string}) => r.id));
    rows.forEach((row,id) => {row.hidden=!ids.has(id);});
    count.textContent=String(selected.length);
    empty.hidden=selected.length>0;
    const selectedTopic=topics.find((t:{id:string}) => t.id===topic.value);
    heading.textContent=selectedTopic?.question_zh ?? '给好奇心，一条学习的路。';
    description.textContent=selectedTopic?.description_zh ?? '课程、讲座与教材都在这里，按自己的起点慢慢选。';
    resets.forEach(button => {button.disabled=!(topic.value || kind.value || search.value);});
    if (updateUrl) {
      const url=new URL(window.location.href);
      Object.entries({topic:topic.value,kind:kind.value,q:search.value.trim()}).forEach(([key,value]) => value ? url.searchParams.set(key,value) : url.searchParams.delete(key));
      if (url.hash.startsWith('#resource-') && rows.get(url.hash.slice(10))?.hidden) url.hash='';
      window.history.replaceState(null,'',url);
    }
  }

  function reset() {topic.value='';kind.value='';search.value='';}
  function revealHash() {
    const row=rows.get(window.location.hash.replace(/^#resource-/,''));
    if (!row) return;
    if (row.hidden) {reset();apply();}
    row.querySelector<HTMLDetailsElement>('[data-learning-reader]')!.open=true;
    requestAnimationFrame(() => row.scrollIntoView({block:'start',behavior:'instant'}));
  }
  function restore() {
    const params=new URLSearchParams(window.location.search);
    const requestedTopic=params.get('topic') ?? '';
    const requestedKind=params.get('kind') ?? '';
    topic.value=[...topic.options].some(o => o.value===requestedTopic) ? requestedTopic : '';
    kind.value=[...kind.options].some(o => o.value===requestedKind) ? requestedKind : '';
    search.value=params.get('q') ?? '';
    apply(false);revealHash();
  }
  form.addEventListener('submit',event => {event.preventDefault();apply();});
  search.addEventListener('input',() => apply());
  topic.addEventListener('change',() => apply());
  kind.addEventListener('change',() => apply());
  resets.forEach(button => button.addEventListener('click',() => {reset();apply();search.focus();}));
  document.querySelectorAll<HTMLAnchorElement>('[data-learning-topic-link]').forEach(link => link.addEventListener('click',event => {
    if (event.button!==0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();reset();topic.value=link.dataset.learningTopicLink!;apply();
    const url=new URL(window.location.href);url.hash='learning-results';window.history.replaceState(null,'',url);
    root.scrollIntoView({block:'start'});
    heading.setAttribute('tabindex','-1');heading.focus({preventScroll:true});
  }));
  window.addEventListener('popstate',restore);
  window.addEventListener('hashchange',revealHash);
  restore();
  form.hidden=false;
  root.querySelector<HTMLElement>('[data-learning-actions]')!.hidden=false;
}
