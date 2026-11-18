# Monthly Top 20 Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans for inline execution and superpowers:requesting-code-review for final independent review. User authorization covers the established Data Lab publication workflow.

**Goal:** Publish a complete archive of per-month Top20 stories plus an all-time Top20, ranked by query-time checked score across the available HN archive, each with its original title and one Chinese reading guide.

**Architecture:** Build deterministic rankings in Python/DuckDB using score-ordered Algolia candidates matched to the verified local index; preserve query-time and original snapshot values separately. Scan the complete archive for above-cutoff candidates missing from Algolia, check them with official Firebase, and retain explicit status/comment provenance. Merge independently authored Chinese reading guides by item ID. Export one canonical JSON and tabular/archive downloads. Load that JSON at Astro build time and render a landing page plus one page per UTC calendar month; browser code only enhances filtering and month navigation.

**Tech Stack:** Python3/DuckDB, Astro6, plain CSS/TypeScript, Node test runner, Python Playwright, GitHub Pages.

## 1. Rank and verify the archive

- [x] Add `reports/monthly-top20/test_build_results.py` before the exporter. Test date/ID tie breaking, fewer-than20, empty calendar months and preserving source fields. Run `.venv/bin/python -m unittest discover -s reports/monthly-top20 -p 'test_*.py'` and observe missing exporter failure.
- [x] Implement `reports/monthly-top20/build_results.py` with CLI `--index`, `--output`, `--cache`. Fetch score-ordered API candidates for each UTC month, match original ID and exact timestamp, and resolve the score cutoff; rank by score/time/ID and compute all-time20. Calendar includes every month between minimum and maximum archived dates. Export `rankings.json`, `rankings.csv`, `README.md`, `rankings.md`, `months/YYYY-MM.json`, `months/YYYY-MM.csv`, `verification.json` and `hn-monthly-top20.zip`.
- [x] Run exporter on `reports/interesting-themes/research/all-stories.parquet`. Independently verify monthly selections with SQL over the full matched candidate pool, source fields and all-time ordering; record data quality observations, source revision, counts, index SHA256 and reproducible command. Preserve both original and checked values.

## 2. Build the archive pages

- [x] Copy reviewed exports to `public/downloads/hn-monthly-top20/`; add `data/monthly-top.json` with path and descriptions.
- [x] Add `tests/monthly-top.test.mjs` first: complete calendar, no repeated ID within/across months, top20 rank/score/date order, all-time rows equal monthly originals, first/last/sparse/empty months, original fields, filtering normalization. Confirm missing loader/filter failure.
- [x] Implement `src/lib/monthly-top.mjs` and browser-safe `src/lib/monthly-top-filter.mjs`; expose collection and current20 search with NFKC all-token matching. Static route generation computes neighboring months. Do not send full archive to browser.
- [x] Add `src/components/MonthlyTopList.astro`, `MonthlyTopArchive.astro`, `MonthlyTopMethod.astro`, `MonthlyTopCard.astro`, `src/pages/hn/monthly-top/index.astro`, `src/pages/hn/monthly-top/[month].astro`, `src/styles/monthly-top.css`, `src/scripts/monthly-top.ts`. Render all story fields as escaped text and restrict external URLs to http(s).
- [x] Add homepage card, navigation and about/source/download information; document update procedure in README. Preserve reproducible exporter and tests in `scripts/hn-monthly-top20/`.
- [x] Run `npm run build` and check one landing page plus239 monthly pages and existing pages, no output path escapes.

## 3. Chinese reading guides — user response received

- [x] User selected original title + one Chinese introduction for every selected story. Keep introductions grounded in titles and available self-post excerpts; label the editorial basis.
- [x] Compose all guides in three independent eras, verify exact selected-ID coverage, review samples, and preserve the ID-to-guide editorial source in data/monthly-top-guides.json.
- [x] Add guide rendering and Chinese search, export fields, coverage checks and browser assertions before the final content build.
- [x] Regenerate every export with --guides, then rerun final data/build/browser checks.

## 4. Acceptance and publication

- [x] Add `tests/monthly_top_browser.py`: compare every built month with canonical data; production-browser first/last/empty/sparse/corrected-score months, search/URL/keyboard, UTC dates, month navigation, no-JavaScript, downloads/ZIP and responsive screenshots.
- [x] Run dedicated acceptance and existing `tests/browser_smoke.py`; inspect desktop/mobile screenshots and source/download hashes.
- [x] Request independent review, fix substantive findings, run affected checks.
- [ ] Commit, fast-forward into main, build merged tree, push and wait for exact implementationSHA Pages success.
- [ ] Verify live new routes/navigation/search/downloads, record results, stop preview, remove merged worktree/branch and leave main clean/synced.

## Local acceptance — 2026-11-18

- Exporter: 3 meaningful synthetic checks passed after observing the expected missing-exporter failure. All 237 nonempty months fetched, original IDs/timestamps matched, and score cutoffs resolved. Independent SQL agreed on all 4,721 monthly rows and 20 all-time rows; 446 selected rows have corrected scores.
- `npm run build`: 12 Node tests passed and 247 static pages generated (240 new archive pages plus 7 existing pages).
- `python3 tests/monthly_top_browser.py --base-url http://127.0.0.1:4325/data-lab/`: all 239 HTML month pages preserve exact IDs/titles/scores/comments/UTC times; monthly JSON/CSV and 483 ZIP members match. Every month returns HTTP 200. Source correction, query/history/hash restoration, month navigation, sparse/empty/partial months, downloads, keyboard, no-JavaScript and 16 viewport widths passed; no script errors.
- Existing `tests/browser_smoke.py`: 7 pages/73 internal links and assets, all previous collections and responsive/no-JavaScript/download behaviors passed.
- All 484 exported public files and both reproducibility scripts are byte-identical to the research results; canonical SHA256 matches verification.json. Excerpt truncation now trims terminal whitespace before exporting; complete diff whitespace validation passes with CRLF CSV recognized via cr-at-eol.
- Desktop1440px and mobile375px archive/month screenshots inspected; no horizontal overflow at320–1440px including navigation breakpoints.

## Independent review fixes

- Both P2 findings were reproduced before fixes. The browser accessibility assertion failed because the filtered rank20 was hidden; the new official fallback unit test failed before implementation.
- Exposed readable 第N名 in the accessible rank. Focused production-browser verification passes for the filtered rank20.
- Full-archive cutoff scan found exactly one missing Algolia candidate: 36860065 (July2023), original score1202. Official Firebase checked score1205 and dead=true; original title/URL retained, comments=archive3 because official descendants is missing. Do not infer total comments from kids. The merged SQL verifier passes all4,721 monthly selections; 4 Python tests pass.
- User replied with the preferred summary depth during final review, so publication also includes complete Chinese guides rather than the initially prepared title-only view.

## Final local verification — 2026-11-18

- All4,721selected stories have one Chinese reading guide, with exact ID coverage. The editorial source SHA matches metadata; the canonical JSON SHA is `45265ca8c8cf3e024c008b46b0bc53ba5a8372d8e4ceac2f22e5e951917e50b4`. All484exports and both scripts match research bytes.
- Exporter4Python tests and independent full-archive SQL passed. Final build passed13Node tests and generated247static pages.
- Full monthly acceptance passed all239HTTPmonths; all239built pages preserve exact ID/title/guide/score/comment/time fields; monthlyCSV/JSON and483ZIPmembers match. Chinese guide search, accessible filtered rank20, official missing-index record/status/comment fallback, URL/history/hash, sparse/empty/partial months, keyboard, noJS and16viewportwidths passed.
- Legacy smoke passed7pages/73links and all existing collections, downloads, filters, keyboard/noJS and9viewportwidths.
- Final1440px/375px reading/hero screenshots inspected; typography, spacing and mobile layout accepted.
- Independent reviewer rechecked4,721rankings/source fields, Chinese-guide coverage in all exports/built pages,484copies and238APIresponse hashes. Both P2 findings fixed; final verdict: ready to publish, no substantive outstanding findings. External-index coverage limitation remains documented.
