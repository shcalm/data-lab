# Interesting Themes Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to execute these steps; use superpowers:requesting-code-review for the final independent review. User authorization includes implementation and publication in the existing Data Lab.

**Goal:** Publish the 30 reviewed themes at `/data-lab/hn/interesting-themes/` with comfortable reading, filters, evidence and downloads.

**Architecture:** Follow the existing Astro collection pattern. Read the exact public research JSON on the server, pass compact searchable fields to the browser, and keep filtering independent of the filesystem. Render every theme on the server and enhance with native browser controls.

**Tech Stack:** Astro 6, plain CSS, TypeScript, Node test runner, Python Playwright, GitHub Pages.

## 1. Import the reviewed research and add meaningful data checks

- [x] Copy `README.md`, `themes.json`, `themes.csv`, `sources.json`, `evidence.json`, `verification.json`, `reading-audit.json`, and `hn-interesting-themes.zip` from `hacker_news/reports/interesting-themes/` into `public/downloads/hn-interesting-themes/` without changing bytes.
- [x] Add `data/interesting-themes.json`: page title, path, download root, group IDs/labels and group introduction.
- [x] Write `tests/interesting-themes.test.mjs` before the loader/filter. Assert30 themes,62 unique stories,106 evidence references, groups7/9/7/7,12 starters; preserve all source quotes and archived/API author labels. Test Chinese/English multiword Unicode queries, group+starters intersections, unknown values and unchanged input order.
- [x] Run `node --test tests/interesting-themes.test.mjs` and confirm it fails because the new collection/filter is missing.
- [x] Add `src/lib/interesting-themes.mjs`, exposing `getInterestingThemes()` with `entries`, `groups`, `metadata`, `sources`, `verification` and `downloadFiles`. Add `src/lib/interesting-themes-filter.mjs`, exposing `selectThemes(entries,{group='',q='',view='all'}={})` with group normalization and all-token matching.
- [x] Re-run the focused tests and confirm all pass.

## 2. Build the reading page and integrate the site

- [x] Add `src/pages/hn/interesting-themes.astro`, `src/styles/interesting-themes.css` and `src/scripts/interesting-themes.ts`: hero, group buttons, search, selected12 toggle, result status, grouped articles, native expandable explanations/evidence, source links, methodology and exact downloads.
- [x] Use `id="theme-<id>"` and canonical per-theme links without current filters. On hash navigation reveal/open the target; URL fields are `group`, `q`, `view`; restore via popstate.
- [x] Add `src/components/InterestingThemesCard.astro`; update `src/pages/index.astro`, `src/layouts/SiteLayout.astro` and `src/pages/about.astro` with the fifth collection and full-archive scope. Keep the original ranking pages' ten-year range explicit.
- [x] Update `README.md` with data ownership, update instructions, query parameters and download location.
- [x] Run `npm run build` and verify the built new page has30 articles and106 blockquotes, all links preserve `/data-lab/`.

## 3. Browser acceptance, review and publication

- [x] Add meaningful browser scenarios in `tests/browser_smoke.py`: new page discovery; filtering and URL restore; deep links across filters; expanded full evidence; archive/API author difference; no-JS;320–1440px and existing-page regression. Validate JSON, CSV and ZIP contents.
- [x] Run production preview and `tests/browser_smoke.py`, inspect desktop/mobile screenshots, and compare8 copied files with source SHA-256.
- [x] Request independent code review under requesting-code-review; resolve substantive findings and run affected checks.
- [x] Commit implementation, fast-forward into main, push main, wait for GitHub Pages workflow success, then check live page and downloads.
- [x] Record verification, remove merged feature worktree/branch, stop preview, and return the live URL.

## Local acceptance — 2026-11-18

- `npm run build`:10 tests passed;7 static pages generated.
- `python3 tests/browser_smoke.py --base-url http://127.0.0.1:4324/data-lab/`:7 pages,69 internal links/assets,9 viewport sizes, query/history/deep-link behavior, keyboard, no JavaScript, downloads and ZIP passed; no browser script errors.
- All8 public files match upstream SHA-256; built HTML contains30 themes and106 quotations.
- Desktop1440px and mobile375px hero and expanded reading screenshots inspected.
- Independent review found no substantive issues; separately checked all8 export files, full explanation/quote preservation, permalink/history behavior and additional navigation widths901–1100px.

## Publication acceptance — 2026-11-18

- Fast-forwarded implementation `ee1d11d9655da1de6f9503a9b03e56a7cb31845e` into `main`; merged-tree `npm run build` passed all 10 tests and generated 7 pages.
- Pushed `main`; [Publish Data Lab run 44266891886](https://github.com/shcalm/data-lab/actions/runs/44266891886) completed successfully for that exact implementation SHA.
- [Live collection](https://shcalm.github.io/data-lab/hn/interesting-themes/) returned HTTP 200. Verified homepage/navigation entry, all 30 themes and 106 quotations, group/search/selected-reading intersections, refresh and history restoration, conflicting hash reveal, both author-display differences, and 375px expanded reading without horizontal overflow.
- All 8 live downloads are byte-identical to the reviewed exports. ZIP integrity and its 7 members passed. No-JavaScript reading worked; no browser script errors occurred.
- Preserved reviewed screenshots and live screenshots under ignored `test-results/`. Stopped the feature preview and removed the merged feature worktree and branch.
