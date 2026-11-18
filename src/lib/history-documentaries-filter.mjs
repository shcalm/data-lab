const normalize = value => String(value ?? '').normalize('NFKC').toLocaleLowerCase('en').replace(/[’‘]/g, "'").trim();

/** Documentary history is an explicit curated subset, independent of topic. */
export function selectHistoryWorks(entries, { view = 'books', q = '', category = '' } = {}) {
  const terms = normalize(q).split(/\s+/).filter(Boolean);
  const documentaries = view === 'documentaries' || view === 'history-documentaries';
  return entries.filter(work => {
    if (work.kind !== (documentaries ? 'documentaries' : 'books')) return false;
    if (view === 'history-documentaries' && !work.historyRelated) return false;
    if (category && work.category !== category) return false;
    const text = normalize([work.zh, work.title, work.creator, work.category, work.summary].join(' '));
    return terms.every(term => text.includes(term));
  });
}
