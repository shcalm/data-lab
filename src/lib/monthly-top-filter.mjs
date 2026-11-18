const normalize = value => String(value ?? '').normalize('NFKC').replace(/[‘’]/g, "'").toLowerCase();

/** Search the displayed Top20; original rank and ordering always survive. */
export function selectMonthlyStories(entries, query = '') {
  const tokens = normalize(query).trim().split(/\s+/).filter(Boolean);
  return entries.filter(entry => tokens.every(token => normalize(entry.searchText).includes(token)));
}
