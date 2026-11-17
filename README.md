# Data Lab

shcalm 的个人数据实验室：用一个仓库持续整理有意思的榜单和数据观察。

站点地址：**https://shcalm.github.io/data-lab/**

目前包含 Hacker News 十年讨论中的[书籍 Top 100](https://shcalm.github.io/data-lab/hn/books/) 和[电影 Top 100](https://shcalm.github.io/data-lab/hn/movies/)，共 200 条中文简介，支持中英文搜索、主题筛选、排序、展开简介，以及 CSV / JSON 下载。

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
  snapshots/2026-08-23/
    books.json                    # 原始排名与次数
    movies.json
    source.json                   # 时间、数据来源、计数单位与限制
    books-verification.json       # 原分析流程的检查结果
    movies-verification.json
  annotations/
    books.json                    # 每本书的中文简介与主题分类
    movies.json                   # 电影按“原名 (年份)”区分同名版本
src/
  pages/index.astro               # 项目首页
  pages/[...project].astro        # 共享的榜单页面
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
