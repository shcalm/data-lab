# Data Lab

shcalm 的个人数据实验室：用一个仓库持续整理有意思的榜单和数据观察。

站点地址：**https://shcalm.github.io/data-lab/**

目前包含 Hacker News 十年讨论中的[书籍 Top 100](https://shcalm.github.io/data-lab/hn/books/)、[电影 Top 100](https://shcalm.github.io/data-lab/hn/movies/)、[学生阅读书目](https://shcalm.github.io/data-lab/hn/school-reading/)、[历史书目与纪录片](https://shcalm.github.io/data-lab/hn/history-documentaries/)，以及从2006—2026全档案发现的[30个深挖主题](https://shcalm.github.io/data-lab/hn/interesting-themes/)。两份榜单提供搜索、主题筛选和排序；学生书目提供109部作品及年龄与类别交叉筛选；历史专题收录100项书目、97部纪录片／系列，其中64部为历史题材；深挖主题提供机制、边界、异议和原文，支持领域与精选阅读筛选。所有项目均有内容说明与数据下载。

## 本地运行

使用 Node.js 22.12+（当前验证版本为 22.22.1；CI 使用 Node.js 24）。在仓库根目录执行：

```sh
npm ci
npm run dev
```

打开终端显示的 `/data-lab/` 地址。

```sh
npm test             # 数据一致性、搜索与排序
npm run build        # 测试后生成静态站点到 dist/
npm run preview      # 预览生产构建
```

`tests/browser_smoke.py` 可在安装了 Python Playwright 和 Chromium 的环境运行，默认检查 `http://127.0.0.1:4321/data-lab/`。截图输出到不入库的 `test-results/`。

```sh
python3 tests/browser_smoke.py
```

## 内容放在哪里

```text
data/
  projects.json                   # 项目目录、标题、路径、简介和数据版本
  school-reading.json             # 学生书目元数据、时间窗口及公开数据位置
  snapshots/2026-08-23/
    books.json                    # 原始排名与次数
    movies.json
    source.json                   # 时间、数据来源、计数单位与限制
    books-verification.json       # 原分析流程的检查结果
    movies-verification.json
  annotations/
    books.json                    # 每本书的中文简介与主题分类
    movies.json                   # 电影按“原名 (年份)”区分同名版本
public/downloads/hn-school-reading/
  书目总表.json                    # 学生书目网页直接读取的同一份下载数据
  书目总表.csv
  按年龄/                         # 每个年龄组的 CSV / JSON / Markdown
  按类别/                         # 九个类别的 CSV / JSON / Markdown
  书目来源.json                    # 分龄依据与原文链接
  学生阅读书目.zip
src/
  pages/index.astro               # 项目首页
  pages/[...project].astro        # 共享的榜单页面
  pages/hn/school-reading.astro   # 按年龄与类别浏览具体书目
  pages/about.astro               # 数据来源与统计口径
  pages/downloads/               # 构建时生成 CSV / JSON
  layouts/                       # 所有页面共用的导航和页脚
```

统计快照与编辑内容分开维护。修改简介不会改变排名；更新统计数据时保留旧快照，新增日期目录，再修改项目的 `snapshot` 字段。一个新快照目录包含该版本所需的排名文件和 `source.json`。

## 后续增加项目

不需要新建仓库。简单延用当前 HN 榜单结构时：

1. 新增 `data/snapshots/<日期>/<项目 id>.json`，包含 `rank`、`title`、`zh`、`mentions`、`stories`、`comments`，书籍用 `author`，电影用 `year`。
2. 在 `data/annotations/` 新增相应简介与分类。书籍键为原名；带年份作品的键为 `原名 (年份)`。
3. 在 `data/projects.json` 增加一项。复制现有项目，修改 `id`、`path`、`exportSlug`、`expectedCount`、`snapshot`、`annotations`、文案和前三名的 `previewLabels`；`catalogueSizeField` 对应来源文件中的候选目录大小字段。
4. 同时核对来源、时间范围、候选目录、页面统计说明和关于页。运行测试与构建，再提交并推送。

共享页面目前面向 HN 作品提及榜单。如果是不同来源、不同结构的数据（例如地图、趋势图），在 `src/pages/` 新增对应页面，复用 `SiteLayout.astro`，并在首页增加入口即可。所有项目继续由这个仓库统一部署，路径可以使用 `/data-lab/<主题>/<项目>/`。

`expectedCount` 用于检查每份榜单是否缺行。搜索始终保留原榜名次，次数相同的条目保留快照顺序。下载文件由同一份数据生成，避免网页和导出版本不一致。

## 学生阅读书目维护

书目数据来自 HN 相关讨论中人工挑选并核对的作品，整理于 2026-11-18，沿用 2016-08-23 至 2026-08-23 UTC 的窗口。它是分类书目，不按提及次数排名，也未穷尽所选讨论中的全部书名。

主表共 109 部不同作品（含系列），80 部有分龄依据，29 部没有明确年龄。四个年龄视图分别有 30、16、27、23 部；跨组作品可重复，年龄未明确组仅保留完全没有已知年龄的作品。九个主类别各自独立，每部只归入一个类别。

`src/lib/school-reading.mjs` 从 `public/downloads/hn-school-reading/` 读取书目、数据说明和来源；网页与下载共用同一份 JSON。更新时从已核验的书目导出目录完整同步此目录（包括年龄、类别和 ZIP），并更新 `data/school-reading.json` 的版本、时间窗口和对应说明。不要单独修改网页内容或把旧 ZIP 与新主表混用。

页面支持 `?age=6-8&category=科普与自然&q=万物` 等可分享查询。关闭 JavaScript 时仍显示完整 109 部书目和所有下载链接。简介保持展开，分龄依据与来源使用原生 `details`。

## 历史书目与纪录片维护

页面 `/hn/history-documentaries/` 提供历史书目、全部纪录片、历史纪录片三个视图，支持题材与关键词交叉筛选，参数为 `view`（`books`／`documentaries`／`history-documentaries`）、`category`、`q`。默认显示100项历史书目。关闭 JavaScript 时完整显示197项作品与来源、下载链接。

已核验的结果完整保存在 `public/downloads/hn-history-documentaries/`，共18个文件（含ZIP）。`src/lib/history-documentaries.mjs` 直接读取其中的历史书目、纪录片单和讨论来源JSON；元数据在 `data/history-documentaries.json`，过滤函数在 `src/lib/history-documentaries-filter.mjs`，不引入文件系统依赖。

更新时从上游 `hacker_news/reports/history-books-documentaries/results/` 完整同步此目录，同时更新元数据、100／97／64数量与形式分布、404条证据、来源说明和验收。网页使用原始简介和逐条语气；不要把已核查证据条数展示成全站提及量。历史纪录片为策展子集，不能简单由题材类别推算。下载ZIP与独立JSON／CSV／Markdown必须保持一致。

## 深挖主题维护

`/hn/interesting-themes/` 从完整下载档案的4,755,791篇可检索主帖发现主题，范围为2006-10-09至2026-08-23 UTC。精选30个主题、四组7／9／7／7、62篇来源及106条引文；阅读记录覆盖72个讨论串中的1,391条评论或片段。主题内容和阅读顺序属于编辑选择，保留适用条件和异议。

`public/downloads/hn-interesting-themes/` 保存上游 `hacker_news/reports/interesting-themes/` 的8个已核验文件（含ZIP）。网页通过 `src/lib/interesting-themes.mjs` 直接读取同一份 `themes.json`；分类元数据在 `data/interesting-themes.json`，纯筛选逻辑在 `src/lib/interesting-themes-filter.mjs`。更新时完整同步导出文件，检查JSON、CSV、Markdown和ZIP的一致性，并更新页面数量、时间范围与验收。原始全库索引与讨论树留在研究项目中。

参数为 `group`（`cognition`／`institutions`／`science`／`computing`）、`q`和`view=starters`。主题永久链接为 `#theme-<id>`，分享入口使用清除筛选的完整路径；访问主题锚点时自动展开，若查询条件隐藏该主题则清空筛选再定位。关闭JavaScript时完整渲染30个主题、原生展开内容及下载入口。历史档案与API的两处作者显示名差异保留双边字段。

## GitHub Pages 发布

首次在仓库 **Settings → Pages → Build and deployment → Source** 中选择 **GitHub Actions**。随后向 `main` 推送提交，或在 Actions 页手动运行 **Publish Data Lab**。

工作流会安装依赖、检查数据、构建站点并发布 `dist/`。Pages 需要首次启用；普通工作流的 `GITHUB_TOKEN` 无法代替仓库所有者完成首次启用设置。

`astro.config.mjs` 固定 `site: https://shcalm.github.io` 和 `base: /data-lab`。静态页面、脚本和下载地址均带项目路径。

## 统计口径

- 窗口：2016-08-23 08:44:12 至 2026-08-23 08:44:12，UTC；截至数据集末日，而非网站发布时间。
- 有效帖子与评论共 34,721,984 条；按 HN item ID 合并去重，排除 deleted / dead。
- 同一作品在同一条记录中最多计一次，帖子和评论分别统计。
- 候选目录：书籍 509 项、电影 1,166 项。规则匹配可能误计或漏计，候选目录也并不穷尽所有作品。
- 提及次数不是推荐数或评分。简介与分类另行整理，不代表 HN 用户观点。

原始数据来自 [open-index/hacker-news](https://huggingface.co/datasets/open-index/hacker-news)，revision 为 `c54ced5973b95d80cd934b8921f44ec8d87c3cd1`。本仓库保存聚合排名与元数据，不上传原始全量数据。
