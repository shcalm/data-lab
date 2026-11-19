import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

async function collection() {
  let mod;
  try { mod = await import('../src/lib/ask-show.mjs'); } catch {}
  assert.ok(mod, 'Ask/Show monthly collection is not implemented');
  return mod.getAskShow();
}

test('Ask and Show each preserve the complete calendar, exact checked values and score ordering', async () => {
  const data = await collection();
  const raw = JSON.parse(readFileSync(`public/${data.dataPath}/rankings.json`, 'utf8'));
  const guidesFile = readFileSync('data/ask-show-guides.json');
  const guides = JSON.parse(guidesFile);
  assert.equal(createHash('sha256').update(guidesFile).digest('hex'),data.metadata.guides_sha256);
  assert.equal(createHash('sha256').update(readFileSync(`public/${data.dataPath}/rankings.json`)).digest('hex'),data.verification.canonical_json_sha256);
  const compare = (a,b) => b.score-a.score || a.time_utc.localeCompare(b.time_utc) || a.id-b.id;
  const seen = new Set();
  assert.deepEqual(Object.keys(data.channels), ['ask', 'show']);
  for (const channel of Object.values(data.channels)) {
    assert.equal(channel.months.length, 239);
    assert.equal(channel.months[0].month, '2006-10');
    assert.equal(channel.months.at(-1).month, '2026-08');
    assert.equal(channel.path, `hn/ask-show/${channel.id}`);
    assert.equal(channel.years.length, 21);
    let total = 0;
    channel.months.forEach((month, i) => {
      assert.equal(month.month, new Date(Date.UTC(2006, 9+i)).toISOString().slice(0,7));
      assert.equal(month.entries.length, Math.min(10, month.eligible_story_count));
      assert.deepEqual(month.entries.map(e=>e.id), [...month.entries].sort(compare).map(e=>e.id));
      month.entries.forEach((entry,j) => {
        assert.equal(entry.rank,j+1);
        assert.equal(entry.channel,channel.id);
        assert.equal(entry.time_utc.slice(0,7),month.month);
        assert.ok(!seen.has(entry.id)); seen.add(entry.id);
        for(const [key,value] of Object.entries(raw.channels[channel.id].months[i].entries[j])) assert.deepEqual(entry[key],value);
        assert.ok(['algolia','firebase'].includes(entry.score_source));
        assert.ok(['algolia','firebase','archive'].includes(entry.comments_source));
        assert.equal(entry.hn_url,`https://news.ycombinator.com/item?id=${entry.id}`);
        assert.ok(entry.articleUrl === '' || /^https?:\/\//.test(entry.articleUrl));
        assert.match(entry.guide_zh,/[\u3400-\u9fff]/u);
        assert.equal(entry.guide_zh,guides[entry.id]);
        assert.ok(entry.searchText.includes(entry.guide_zh));
        assert.ok(!entry.guide_zh.includes('\n'));
      });
      total += month.entries.length;
    });
    assert.equal(total,channel.monthly_entry_count);
  }
  assert.equal(seen.size,data.metadata.monthly_entry_count);
  assert.equal(data.metadata.guide_count,seen.size);
  assert.equal(Object.keys(guides).length,seen.size);
  assert.equal(data.verification.failure_count,0);
});

test('early sparse months and Ask self-post scope remain visible', async () => {
  const {channels} = await collection();
  assert.equal(channels.ask.months[0].entries.length,0);
  assert.equal(channels.show.months.find(m=>m.month==='2009-03').entries.length,3);
  assert.ok(channels.ask.months.find(m=>m.month==='2023-07').entries.some(e=>e.id===36609641));
  for (const id of [37062422,37020610,37267597,34972791,38088538,48034587]) assert.ok(channels.show.months.flatMap(m=>m.entries).some(e=>e.id===id), `Removed Show tag must not hide ${id}`);
  for (const id of [47501426,35138319]) assert.ok(channels.ask.months.flatMap(m=>m.entries).some(e=>e.id===id), `Removed Ask tag must not hide ${id}`);
  assert.ok(channels.show.months.flatMap(m=>m.entries).every(e=>/^\s*show\s+(hn|yc)\b/i.test(e.title)));
});
