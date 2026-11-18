import { selectHistoryWorks } from '../lib/history-documentaries-filter.mjs';

const root = document.querySelector<HTMLElement>('[data-history-collection]');
if (root) {
  const controls = root.querySelector<HTMLFormElement>('[data-history-controls]')!;
  const search = controls.querySelector<HTMLInputElement>('#history-search')!;
  const category = controls.querySelector<HTMLSelectElement>('#history-category')!;
  const buttons = [...controls.querySelectorAll<HTMLButtonElement>('[data-view]')];
  const rows = new Map([...root.querySelectorAll<HTMLElement>('[data-work]')].map(row => [row.dataset.work, row]));
  const groups = [...root.querySelectorAll<HTMLElement>('[data-work-group]')];
  const sections = [...root.querySelectorAll<HTMLElement>('[data-history-section]')];
  const entries = JSON.parse(root.querySelector('#history-documentaries-data')!.textContent!);
  const count = root.querySelector<HTMLElement>('[data-result-count]')!;
  const total = root.querySelector<HTMLElement>('[data-view-total]')!;
  const label = root.querySelector<HTMLElement>('[data-current-view]')!;
  const empty = root.querySelector<HTMLElement>('[data-history-empty]')!;
  const resets = root.querySelectorAll<HTMLButtonElement>('[data-history-reset]');
  let view = 'books';

  function updateCategories(value = '') {
    const works = selectHistoryWorks(entries, { view });
    const names = groups.filter(group => works.some(work => work.kind === group.dataset.kind && work.category === group.dataset.category)).map(group => group.dataset.category!);
    category.replaceChildren(new Option('全部题材', ''), ...names.map(name => new Option(`${name} · ${works.filter(work => work.category === name).length}`, name)));
    category.value = names.includes(value) ? value : '';
  }

  function apply(updateUrl = true) {
    const selected = selectHistoryWorks(entries, { view, q: search.value, category: category.value });
    const ids = new Set(selected.map(work => work.id));
    rows.forEach((row, id) => { row.hidden = !ids.has(id); });
    groups.forEach(group => {
      const matches = selected.filter(work => work.kind === group.dataset.kind && work.category === group.dataset.category).length;
      group.hidden = matches === 0;
      group.querySelector<HTMLElement>('[data-category-count]')!.textContent = String(matches);
    });
    sections.forEach(section => { section.hidden = !selected.some(work => work.kind === section.dataset.historySection); });
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.view === view)));
    label.textContent = buttons.find(button => button.dataset.view === view)!.querySelector('span')!.firstChild!.textContent;
    count.textContent = String(selected.length);
    total.textContent = String(selectHistoryWorks(entries, { view }).length);
    empty.hidden = selected.length > 0;
    resets.forEach(button => { button.disabled = !(search.value || category.value); });
    if (updateUrl) {
      const url = new URL(window.location.href);
      const values = { view: view === 'books' ? '' : view, q: search.value.trim(), category: category.value };
      Object.entries(values).forEach(([key, value]) => value ? url.searchParams.set(key, value) : url.searchParams.delete(key));
      window.history.replaceState(null, '', url);
    }
  }

  function restore() {
    const params = new URLSearchParams(window.location.search);
    view = buttons.some(button => button.dataset.view === params.get('view')) ? params.get('view')! : 'books';
    search.value = params.get('q') ?? '';
    updateCategories(params.get('category') ?? '');
    apply(false);
  }

  buttons.forEach(button => button.addEventListener('click', () => {
    view = button.dataset.view!;
    updateCategories();
    apply();
  }));
  search.addEventListener('input', () => apply());
  category.addEventListener('change', () => apply());
  controls.addEventListener('submit', event => { event.preventDefault(); apply(); });
  resets.forEach(button => button.addEventListener('click', () => {
    search.value = '';
    category.value = '';
    apply();
    search.focus();
  }));
  window.addEventListener('popstate', restore);
  restore();
  controls.hidden = false;
  root.querySelector<HTMLElement>('[data-history-actions]')!.hidden = false;
}
