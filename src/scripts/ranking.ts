import { selectEntries } from '../lib/ranking.mjs';

const root = document.querySelector<HTMLElement>('[data-ranking]');
if (root) {
  const form = root.querySelector<HTMLFormElement>('[data-controls]')!;
  const search = form.querySelector<HTMLInputElement>('#search')!;
  const category = form.querySelector<HTMLSelectElement>('#category')!;
  const sort = form.querySelector<HTMLSelectElement>('#sort')!;
  const list = root.querySelector<HTMLOListElement>('[data-list]')!;
  const rows = new Map(Array.from(list.querySelectorAll<HTMLElement>('[data-rank]')).map((row) => [Number(row.dataset.rank), row]));
  const entries = JSON.parse(root.querySelector('#ranking-data')!.textContent!);
  const count = root.querySelector<HTMLElement>('[data-result-count]')!;
  const empty = root.querySelector<HTMLElement>('[data-empty]')!;
  const expand = root.querySelector<HTMLButtonElement>('[data-expand]')!;
  const resets = root.querySelectorAll<HTMLButtonElement>('[data-reset]');
  let visibleRows: HTMLElement[] = [];

  function updateExpandLabel() {
    expand.textContent = visibleRows.length && visibleRows.every((row) => row.querySelector('details')!.open)
      ? '收起全部简介' : '展开全部简介';
    expand.disabled = visibleRows.length === 0;
  }

  function apply(updateUrl = true) {
    const selected = selectEntries(entries, { q: search.value, category: category.value, sort: sort.value });
    const selectedRanks = new Set(selected.map((entry) => entry.rank));
    rows.forEach((row, rank) => { row.hidden = !selectedRanks.has(rank); });
    visibleRows = selected.map((entry) => rows.get(entry.rank)!);
    const fragment = document.createDocumentFragment();
    visibleRows.forEach((row) => fragment.append(row));
    list.append(fragment);
    count.textContent = String(selected.length);
    empty.hidden = selected.length > 0;
    const active = Boolean(search.value || category.value || sort.value !== 'most');
    resets.forEach((button) => { button.disabled = !active; });
    updateExpandLabel();

    if (updateUrl) {
      const url = new URL(window.location.href);
      const values = { q: search.value.trim(), category: category.value, sort: sort.value === 'most' ? '' : sort.value };
      Object.entries(values).forEach(([key, value]) => value ? url.searchParams.set(key, value) : url.searchParams.delete(key));
      window.history.replaceState(null, '', url);
    }
  }

  function restore() {
    const params = new URLSearchParams(window.location.search);
    search.value = params.get('q') ?? '';
    category.value = Array.from(category.options).some((option) => option.value === params.get('category')) ? params.get('category')! : '';
    sort.value = Array.from(sort.options).some((option) => option.value === params.get('sort')) ? params.get('sort')! : 'most';
    apply(false);
  }

  form.hidden = false;
  root.querySelector<HTMLElement>('[data-list-actions]')!.hidden = false;
  search.addEventListener('input', () => apply());
  category.addEventListener('change', () => apply());
  sort.addEventListener('change', () => apply());
  form.addEventListener('submit', (event) => { event.preventDefault(); apply(); });
  resets.forEach((button) => button.addEventListener('click', () => {
    form.reset();
    apply();
    search.focus();
  }));
  expand.addEventListener('click', () => {
    const open = visibleRows.some((row) => !row.querySelector('details')!.open);
    visibleRows.forEach((row) => { row.querySelector('details')!.open = open; });
    updateExpandLabel();
  });
  list.addEventListener('toggle', updateExpandLabel, true);
  window.addEventListener('popstate', restore);
  restore();
}
