import { selectThemes } from '../lib/interesting-themes-filter.mjs';

const root = document.querySelector<HTMLElement>('[data-themes-collection]');
if (root) {
  const form = root.querySelector<HTMLFormElement>('[data-themes-controls]')!;
  const search = form.querySelector<HTMLInputElement>('#themes-search')!;
  const starters = form.querySelector<HTMLInputElement>('#themes-starters')!;
  const buttons = [...form.querySelectorAll<HTMLButtonElement>('[data-theme-group]')];
  const rows = new Map([...root.querySelectorAll<HTMLElement>('[data-theme]')].map(row => [row.dataset.theme!, row]));
  const sections = [...root.querySelectorAll<HTMLElement>('[data-theme-section]')];
  const count = root.querySelector<HTMLElement>('[data-result-count]')!;
  const empty = root.querySelector<HTMLElement>('[data-themes-empty]')!;
  const resets = [...root.querySelectorAll<HTMLButtonElement>('[data-themes-reset]')];
  const entries = JSON.parse(root.querySelector('#interesting-themes-data')!.textContent!);
  let group = '';

  function apply(updateUrl = true) {
    const selected = selectThemes(entries, { group, q: search.value, view: starters.checked ? 'starters' : 'all' });
    const ids = new Set(selected.map((theme: { id: string }) => theme.id));
    rows.forEach((row, id) => { row.hidden = !ids.has(id); });
    sections.forEach(section => {
      const matches = selected.filter((theme: { domain: string }) => theme.domain === section.dataset.themeSection).length;
      section.hidden = matches === 0;
      section.querySelector<HTMLElement>('[data-group-count]')!.textContent = String(matches);
    });
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.themeGroup === group)));
    count.textContent = String(selected.length);
    empty.hidden = selected.length > 0;
    resets.forEach(button => { button.disabled = !(group || search.value || starters.checked); });
    if (updateUrl) {
      const url = new URL(window.location.href);
      const values = { group, q: search.value.trim(), view: starters.checked ? 'starters' : '' };
      Object.entries(values).forEach(([key, value]) => value ? url.searchParams.set(key, value) : url.searchParams.delete(key));
      if (url.hash.startsWith('#theme-') && rows.get(url.hash.slice(7))?.hidden) url.hash = '';
      window.history.replaceState(null, '', url);
    }
  }

  function revealHash() {
    const row = rows.get(window.location.hash.replace(/^#theme-/, ''));
    if (!row) return;
    if (row.hidden) {
      group = '';
      search.value = '';
      starters.checked = false;
      apply();
    }
    row.querySelector<HTMLDetailsElement>('[data-theme-reader]')!.open = true;
    requestAnimationFrame(() => row.scrollIntoView({ block: 'start', behavior: 'instant' }));
  }

  function restore() {
    const params = new URLSearchParams(window.location.search);
    const requested = params.get('group') ?? '';
    group = buttons.some(button => button.dataset.themeGroup === requested) ? requested : '';
    search.value = params.get('q') ?? '';
    starters.checked = params.get('view') === 'starters';
    apply(false);
    revealHash();
  }

  buttons.forEach(button => button.addEventListener('click', () => { group = button.dataset.themeGroup!; apply(); }));
  search.addEventListener('input', () => apply());
  starters.addEventListener('change', () => apply());
  form.addEventListener('submit', event => { event.preventDefault(); apply(); });
  resets.forEach(button => button.addEventListener('click', () => {
    group = '';
    search.value = '';
    starters.checked = false;
    apply();
    search.focus();
  }));
  window.addEventListener('popstate', restore);
  window.addEventListener('hashchange', revealHash);
  restore();
  form.hidden = false;
  root.querySelector<HTMLElement>('[data-themes-actions]')!.hidden = false;
}
