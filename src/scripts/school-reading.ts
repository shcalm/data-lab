import { selectBooks } from '../lib/school-reading-filter.mjs';

const root = document.querySelector<HTMLElement>('[data-school-reading]');
if (root) {
  const controls = root.querySelector<HTMLFormElement>('[data-reading-controls]')!;
  const search = controls.querySelector<HTMLInputElement>('#reading-search')!;
  const category = controls.querySelector<HTMLSelectElement>('#reading-category')!;
  const ageButtons = [...controls.querySelectorAll<HTMLButtonElement>('[data-age]')];
  const rows = new Map([...root.querySelectorAll<HTMLElement>('[data-book]')].map(row => [row.dataset.book, row]));
  const sections = [...root.querySelectorAll<HTMLElement>('[data-book-category]')];
  const entries = JSON.parse(root.querySelector('#school-reading-data')!.textContent!);
  const count = root.querySelector<HTMLElement>('[data-result-count]')!;
  const empty = root.querySelector<HTMLElement>('[data-reading-empty]')!;
  const resets = root.querySelectorAll<HTMLButtonElement>('[data-reading-reset]');
  let age = '';

  function apply(updateUrl = true) {
    const selected = selectBooks(entries, { q: search.value, age, category: category.value });
    const ids = new Set(selected.map(book => book.id));
    rows.forEach((row, id) => { row.hidden = !ids.has(id); });
    sections.forEach(section => {
      const total = selected.filter(book => book.category === section.dataset.bookCategory).length;
      section.hidden = total === 0;
      section.querySelector<HTMLElement>('[data-category-count]')!.textContent = String(total);
    });
    ageButtons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.age === age)));
    count.textContent = String(selected.length);
    empty.hidden = selected.length > 0;
    resets.forEach(button => { button.disabled = !(search.value || age || category.value); });
    if (updateUrl) {
      const url = new URL(window.location.href);
      const values = { q: search.value.trim(), age, category: category.value };
      Object.entries(values).forEach(([key, value]) => value ? url.searchParams.set(key, value) : url.searchParams.delete(key));
      window.history.replaceState(null, '', url);
    }
  }

  function restore() {
    const params = new URLSearchParams(window.location.search);
    search.value = params.get('q') ?? '';
    age = ageButtons.some(button => button.dataset.age === params.get('age')) ? params.get('age')! : '';
    category.value = [...category.options].some(option => option.value === params.get('category')) ? params.get('category')! : '';
    apply(false);
  }

  search.addEventListener('input', () => apply());
  category.addEventListener('change', () => apply());
  ageButtons.forEach(button => button.addEventListener('click', () => { age = button.dataset.age!; apply(); }));
  controls.addEventListener('submit', event => { event.preventDefault(); apply(); });
  resets.forEach(button => button.addEventListener('click', () => {
    controls.reset();
    age = '';
    apply();
    search.focus();
  }));
  window.addEventListener('popstate', restore);
  restore();
  controls.hidden = false;
  root.querySelector<HTMLElement>('[data-reading-actions]')!.hidden = false;
}
