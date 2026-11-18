# Monthly Top 20 Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans for inline execution and superpowers:requesting-code-review for final independent review. User authorization covers the established Data Lab publication workflow.

**Goal:** Publish a complete archive of per-month Top20 stories plus an all-time Top20, ranked by snapshot score across the available HN archive.

**Architecture:** Build deterministic rankings in Python/DuckDB from the verified local index. Export one canonical JSON and tabular/archive downloads. Load that JSON at Astro build time and render a landing page plus one page per UTC calendar month; browser code only enhances filtering and month navigation.

**Tech Stack:** Python3/DuckDB, Astro6, plain CSS/TypeScript, Node test runner, Python Playwright, GitHub Pages.

## 1. Rank and verify the archive

- [ ] Add `reports/monthly-top20/test_build_results.py` before the exporter. Test UTC boundaries, date/ID tie breaking, fewer-than20, empty months and preserving source fields. Run `.venv/bin/python -m unittest discover -s reports/monthly-top20 -p 'test_*.py'` and observe missing exporter failure.
- [ ] Implement `reports/monthly-top20/build_results.py` with CLI `--index` and `--output`. Rank using `row_number() over(partition by strftime(time,'%Y-%m') order by score desc,time asc,id asc)` and compute all-time20. Calendar includes every month between minimum and maximum archived dates. Export `rankings.json`, `rankings.csv`, `README.md`, `rankings.md`, `months/YYYY-MM.json`, `months/YYYY-MM.csv`, `verification.json` and `hn-monthly-top20.zip`.
- [ ] Run exporter on `reports/interesting-themes/research/all-stories.parquet`. Independently verify monthly selections against correlated-count SQL, source fields and all-time ordering; record data quality observations, source revision, counts, index SHA256 and reproducible command.

## 2. Build the archive pages

- [ ] Copy reviewed exports to `public/downloads/hn-monthly-top20/`; add `data/monthly-top.json` with path and descriptions.
- [ ] Add `tests/monthly-top.test.mjs` first: complete calendar, no repeated ID within/across months, top20 rank/score/date order, all-time rows equal monthly originals, first/last/sparse/empty months, original fields, filtering normalization. Confirm missing loader/filter failure.
- [ ] Implement `src/lib/monthly-top.mjs` and browser-safe `src/lib/monthly-top-filter.mjs`; expose collection, month lookup, navigation, current20 search with NFKC all-token matching. Do not send full archive to browser.
- [ ] Add `src/components/MonthlyTopList.astro`, `src/components/MonthlyTopCard.astro`, `src/pages/hn/monthly-top/index.astro`, `src/pages/hn/monthly-top/[month].astro`, `src/styles/monthly-top.css`, `src/scripts/monthly-top.ts`. Render all story fields as escaped text and restrict external URLs to http(s).
- [ ] Add homepage card, navigation and about/source/download information; document update procedure in README.
- [ ] Run `npm run build` and check one landing page plus239 monthly pages and existing pages, no output path escapes.

## 3. Acceptance and publication

- [ ] Add `tests/monthly_top_browser.py`: compare every built month with canonical data; production-browser first/last/empty/sparse/low-score months, search/URL/keyboard, UTC dates, month navigation, no-JavaScript, downloads/ZIP and responsive screenshots.
- [ ] Run dedicated acceptance and existing `tests/browser_smoke.py`; inspect desktop/mobile screenshots and source/download hashes.
- [ ] Request independent review, fix substantive findings, run affected checks.
- [ ] Commit, fast-forward into main, build merged tree, push and wait for exact implementationSHA Pages success.
- [ ] Verify live new routes/navigation/search/downloads, record results, stop preview, remove merged worktree/branch and leave main clean/synced.
