import { selectMonthlyStories } from '../lib/monthly-top-filter.mjs';

const list = document.querySelector<HTMLElement>('[data-monthly-list]');
const form = list?.querySelector<HTMLFormElement>('[data-monthly-search]');
if (list && form) {
  const search = form.querySelector<HTMLInputElement>('input')!;
  const entries = JSON.parse(list.querySelector('#monthly-search-data')!.textContent!);
  const rows = new Map([...list.querySelectorAll<HTMLElement>('[data-monthly-story]')].map(row => [row.dataset.monthlyStory!, row]));
  const resets = [...list.querySelectorAll<HTMLButtonElement>('[data-monthly-reset]')];
  function apply(updateUrl = true) {
    const selected = selectMonthlyStories(entries, search.value);
    const ids = new Set(selected.map((entry: {id: number}) => String(entry.id)));
    rows.forEach((row, id) => { row.hidden = !ids.has(id); });
    list!.querySelector('[data-monthly-count]')!.textContent = String(selected.length);
    list!.querySelector<HTMLElement>('[data-monthly-empty]')!.hidden = selected.length > 0;
    resets.forEach(button => { button.disabled = !search.value; });
    if (updateUrl) {
      const url = new URL(location.href);
      search.value.trim() ? url.searchParams.set('q', search.value.trim()) : url.searchParams.delete('q');
      if (url.hash.startsWith('#story-') && rows.get(url.hash.slice(7))?.hidden) url.hash = '';
      history.replaceState(null, '', url);
    }
  }
  function reveal() {
    const row = rows.get(location.hash.replace(/^#story-/, ''));
    if (!row) return;
    if (row.hidden) { search.value = ''; apply(); }
    requestAnimationFrame(() => row.scrollIntoView({block:'start', behavior:'instant'}));
  }
  function restore() { search.value = new URLSearchParams(location.search).get('q') ?? ''; apply(false); reveal(); }
  search.addEventListener('input', () => apply());
  form.addEventListener('submit', event => { event.preventDefault(); apply(); });
  resets.forEach(button => button.addEventListener('click', () => { search.value = ''; apply(); search.focus(); }));
  window.addEventListener('popstate', restore);
  window.addEventListener('hashchange', reveal);
  restore();
  form.hidden = false;
}
document.querySelectorAll<HTMLFormElement>('[data-monthly-jump]').forEach(form => {
  form.addEventListener('submit', event => {
    event.preventDefault();
    const month = form.querySelector<HTMLSelectElement>('select')!.value;
    location.assign(form.dataset.path + month + '/');
  });
  form.hidden = false;
});
function revealYear() {
  const year = document.getElementById(location.hash.slice(1));
  if (year instanceof HTMLDetailsElement && year.classList.contains('monthly-year')) year.open = true;
}
revealYear();
window.addEventListener('hashchange', revealYear);
