# Learning Resources Implementation Plan

> Execute inline in the isolated worktree. Publication and push are explicitly authorized by the user.

**Goal:** Publish the reviewed25-topic,83-resource catalogue on Data Lab with readable descriptions and traceable recommendations.

**Architecture:** Reuse SiteLayout, site tokens and progressive enhancement. Load canonical public JSON in a build-only module; keep browser filtering in a filesystem-free module. Preserve all upstream exports byte for byte.

**Tech Stack:** Astro6, existing CSS tokens, TypeScript browser script, node:test and Python Playwright.

- [x] Sync the complete verified `hacker_news/reports/learning-resources/results/` directory into `public/downloads/hn-learning-resources/`.
- [x] Add `tests/learning-resources.test.mjs` before the adapter and filter: verify83 unmodified resources,25 topic memberships,36 sources,183 quotations, negative evidence and combined normalized search. Run `node --test tests/learning-resources.test.mjs` and confirm missing-feature failure.
- [x] Implement `data/learning-resources.json`, `src/lib/learning-resources.mjs` and `src/lib/learning-resources-filter.mjs`. Run the focused tests.
- [x] Implement `src/pages/hn/learning-resources.astro`, `src/styles/learning-resources.css` and `src/scripts/learning-resources.ts`. Provide six topic groups, topic/type/search controls, readable resources, native evidence disclosures, downloads, methodology and resource permalinks.
- [x] Add `src/components/LearningResourcesCard.astro`; update the homepage count, SiteLayout navigation, about page and README.
- [x] Run `npm run build`. Use Playwright on the built preview to exercise filters, shared URLs, hash recovery, native disclosures, no-JavaScript content, mobile widths and download consistency. Review desktop and mobile screenshots.
- [x] Inspect the diff, commit the feature, fast-forward main and push to origin.
- [x] Track the Pages workflow for this commit, verify the live resource page and exports, then remove the temporary preview and worktree.

Local verification on2026-11-19:17unit tests passed;729static pages built. Browser checks passed at11viewport widths, with and without JavaScript; all83resources,183quotes and67download hashes match their canonical inputs. Desktop and mobile screenshots reviewed. Independent review identified5omitted supplementary course entrances; confirmed the failing regression, rendered both supplementary-link fields and reran browser verification successfully.

Generated Markdown exports retain the upstream final blank lines so their download hashes stay identical. Whitespace checks for implementation and documentation exclude the copied exports.

Published commit: `e90b9fdf29073962386bad8b59403432f8b7ff77`. [Publish Data Lab run44458600623](https://github.com/shcalm/data-lab/actions/runs/44458600623) completed successfully at2026-11-19T04:29:33Z. Live verification at`https://shcalm.github.io/data-lab/hn/learning-resources/` passed the same browser interactions, content preservation, no-JavaScript and viewport checks; all5core downloads returned200 and matched the reviewed export hashes. Temporary preview stopped, dependency symlink removed, and the merged feature worktree and branch cleaned up.
