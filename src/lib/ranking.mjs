const normalize = (value) => String(value ?? '').normalize('NFKC').toLocaleLowerCase('en').replace(/[’‘]/g, "'").trim();

/** Search all editorial fields; always retain the source rank as a stable tie break. */
export function selectEntries(entries, { q = '', category = '', sort = 'most' } = {}) {
  const terms = normalize(q).split(/\s+/).filter(Boolean);
  const filtered = entries.filter((entry) => {
    if (category && entry.category !== category) return false;
    const text = normalize([entry.title, entry.zh, entry.author, entry.year, entry.category, entry.summary].join(' '));
    return terms.every((term) => text.includes(term));
  });
  return filtered.sort((a, b) => {
    if (sort === 'least') return a.mentions - b.mentions || a.rank - b.rank;
    if (sort === 'title') return a.title.localeCompare(b.title, 'en') || a.rank - b.rank;
    if (sort === 'year') return (b.year ?? 0) - (a.year ?? 0) || a.rank - b.rank;
    return a.rank - b.rank;
  });
}
