const normalize = (value) => String(value ?? '').normalize('NFKC').toLocaleLowerCase('en').replace(/[’‘]/g, "'").trim();

/** Age groups overlap; "unspecified" only contains books without any known age. */
export function selectBooks(entries, { q = '', age = '', category = '' } = {}) {
  const terms = normalize(q).split(/\s+/).filter(Boolean);
  return entries.filter(book => {
    if (age && !book.ageIds.includes(age)) return false;
    if (category && book.category !== category) return false;
    const text = normalize([book.zh, book.title, book.author, book.category, book.summary].join(' '));
    return terms.every(term => text.includes(term));
  });
}
