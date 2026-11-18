const normalize = value => String(value ?? '').normalize('NFKC').toLocaleLowerCase('en').replace(/[’‘]/g, "'").trim();

/** Match all search terms while retaining the reviewed order and content. */
export function selectThemes(entries, { group = '', q = '', view = 'all' } = {}) {
  const knownGroup = entries.some(theme => theme.domain === group);
  const terms = normalize(q).split(/\s+/).filter(Boolean);
  return entries.filter(theme =>
    (!knownGroup || theme.domain === group)
    && (view !== 'starters' || theme.starter)
    && terms.every(term => normalize(theme.searchText).includes(term)));
}
