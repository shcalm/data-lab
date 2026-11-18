# 学生阅读书目 Implementation Plan

> **For agentic workers:** 在当前会话执行，用户已授权加入并发布到 Data Lab。逐项核验，使用既有页面风格。

**Goal:** 将 109 部学生阅读书目加入 Data Lab，支持分龄、分类、搜索和数据下载。

**Architecture:** 独立静态书目页复用站点布局，读取公开下载目录中的同一份 JSON，使用纯函数和浏览器脚本增强筛选。

**Tech Stack:** Astro 6、原生 TypeScript / CSS、Node 测试、Python Playwright。

## 步骤

- [x] 在 `tests/school-reading.test.mjs` 添加年龄集合、交叉查询、Unicode 搜索和特殊个案的验收测试，运行 `node --test tests/school-reading.test.mjs` 确认新增模块尚未实现。
- [x] 将 `/work/hua2/projects/hacker_news/reports/school-reading-booklists/` 复制到 `public/downloads/hn-school-reading/`。新增 `data/school-reading.json`、`src/lib/school-reading.mjs` 和 `src/lib/school-reading-filter.mjs`。运行 `npm test` 验证 109 / 80 / 29，以及分龄 30 / 16 / 27 / 23。
- [x] 新增 `src/pages/hn/school-reading.astro`、`src/scripts/school-reading.ts`、`src/styles/school-reading.css` 和 `src/components/SchoolReadingCard.astro`。书目按类别分组，搜索、类别、年龄相交，查询参数为 `q` / `category` / `age`；所有内容静态输出，增强控件默认隐藏。
- [x] 修改 `src/pages/index.astro`、`src/layouts/SiteLayout.astro`、`src/pages/about.astro`、`README.md`，增加入口、项目数量和书目口径。旧榜单继续使用已有模块和页面。
- [x] 扩展 `tests/browser_smoke.py`：109 本静态输出、四个年龄组和独立未知组、组合查询、刷新与历史恢复、空结果、下载文件、移动布局、无 JS。运行 `npm run build` 和 `python3 tests/browser_smoke.py`，视觉检查截图。
- [x] 核对 `git diff --check`、下载与原始导出哈希；提交并合并到 main，推送 `origin main`。检查公开 GitHub Actions 状态，线上首页、新页面、原榜单及下载响应。

## 发布核验（2026-11-18）

- 页面：https://shcalm.github.io/data-lab/hn/school-reading/
- 内容提交：`284f5e9752a4caa7d87ca869653f61987bfd13c8`。
- [GitHub Pages 构建与发布](https://github.com/shcalm/data-lab/actions/runs/44229640361)均成功。
- 六项 Node 测试、生产构建和五个页面的完整浏览器检查通过；另核验六个临界宽度。独立代码复核提出的逐条年龄注释已补齐，全部 96 条展示证据注释保留。
- 线上确认：首页入口、109 部书、全部年龄组、交叉筛选、网址恢复、移动布局、分龄注释、旧书籍和电影榜单、关于页均正常。线上主表 CSV / JSON 与 ZIP 的 SHA-256 和本地已核验导出一致；年龄、类别与交叉表下载数量一致。
