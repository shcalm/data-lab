# 历史与纪录片 Implementation Plan

> **For agentic workers:** 在当前会话逐项执行。用户已授权加入并发布；使用现有视觉方案，不需再次确认发布权限。

**Goal:** 发布可分类搜索、有完整简介与来源的历史书目和纪录片专题。

**Architecture:** Astro 静态页面直接读取公开下载 JSON，浏览器通过独立纯函数增强筛选。沿用现有布局、书目卡片与设计变量，首页及关于页增加入口。

**Tech Stack:** Astro 6、原生 TypeScript／CSS、Node test、Python Playwright。

## 实施步骤

- [x] 运行 `npm test` 确认现有基线；在 `tests/history-documentaries.test.mjs` 添加来源、作品格式、100／97／64集合与组合筛选验收，运行该文件确认新模块尚未存在。
- [x] 从 `/work/hua2/projects/hacker_news/reports/history-books-documentaries/results/` 完整复制导出到 `public/downloads/hn-history-documentaries/`。新增 `data/history-documentaries.json`、`src/lib/history-documentaries.mjs`、`src/lib/history-documentaries-filter.mjs`，运行新测试。
- [x] 新增专题页 `src/pages/hn/history-documentaries.astro`、增强脚本 `src/scripts/history-documentaries.ts`、少量补充样式 `src/styles/history-documentaries.css` 及首页卡片 `src/components/HistoryDocumentariesCard.astro`。三视图参数为 books／documentaries／history-documentaries；保留无 JS 全量阅读。
- [x] 更新 `src/pages/index.astro`、`src/layouts/SiteLayout.astro`、`src/pages/about.astro`、`README.md` 的入口、数量、方法和维护说明。
- [x] 扩展 `tests/browser_smoke.py`：静态197项、视图数量100／97／64、类别和关键词交叉、刷新与历史恢复、空状态、引文展开、CSV／JSON／ZIP及无 JS；沿用完整旧页面回归和多尺寸检查。运行 `npm run build`，预览生产构建，再运行浏览器验收并检查截图。
- [ ] 核对导出哈希和 `git diff --check`；提交、合并到 main、推送。检查当前提交的 GitHub Actions 与线上页面、视图及下载，记录发布证据。

## 本地验证（2026-11-18）

- 8项Node验收、生产构建通过；完整浏览器检查覆盖6页、59个站内链接／资源与9个宽度。
- 100／97／64视图、Unicode与类别交叉、URL恢复、空状态、来源引文、下载ZIP、键盘、无JS及旧页面回归全部通过。
- 独立代码复核未发现发布阻塞；18个公开下载文件与上游字节一致，ZIP内部文件及CRC通过。
