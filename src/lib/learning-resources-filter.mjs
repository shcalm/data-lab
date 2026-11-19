const normalize = value => String(value ?? '').normalize('NFKC').toLocaleLowerCase('en').replace(/[’‘]/g,"'").trim();

/** A resource can belong to several learning themes; filtering preserves the curated order. */
export function selectLearningResources(entries,{topic='',kind='',q=''}={}) {
  const knownTopic = entries.some(r => r.topics.includes(topic));
  const knownKind = entries.some(r => r.kind===kind);
  const terms = normalize(q).split(/\s+/).filter(Boolean);
  return entries.filter(r => (!knownTopic || r.topics.includes(topic))
    && (!knownKind || r.kind===kind)
    && terms.every(term => normalize(r.searchText).includes(term)));
}
