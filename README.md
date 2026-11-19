# Data Lab

shcalm 的个人数据实验室：用一个仓库持续整理有意思的榜单和数据观察。

站点地址：**https://shcalm.github.io/data-lab/**

目前包含 Hacker News 十年讨论中的[书籍 Top 100](https://shcalm.github.io/data-lab/hn/books/)、[电影 Top 100](https://shcalm.github.io/data-lab/hn/movies/)、[学生阅读书目](https://shcalm.github.io/data-lab/hn/school-reading/)、[历史书目与纪录片](https://shcalm.github.io/data-lab/hn/history-documentaries/)，以及从2006—2026全档案发现的[30个深挖主题](https://shcalm.github.io/data-lab/hn/interesting-themes/)、[HN 每月 Top 20](https://shcalm.github.io/data-lab/hn/monthly-top/)。两份榜单提供搜索、主题筛选和排序；学生书目提供109部作品及年龄与类别交叉筛选；历史专题收录100项书目、97部纪录片／系列，其中64部为历史题材；深挖主题提供机制、边界、异议和原文，支持领域与精选阅读筛选。每月Top20覆盖239个日历月，提供4,721条月榜记录和全时段Top20，可按月翻阅。另有[课程与学习资源](https://shcalm.github.io/data-lab/hn/learning-resources/)，从25个主题整理83项具体资源，保留推荐原话。所有项目均有内容说明与数据下载。

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

## HN 每月 Top 20 维护

`/hn/monthly-top/` 提供全时段得分 Top 20 和完整年月档案。`/hn/monthly-top/YYYY-MM/` 是可独立分享的月页。覆盖 2006-10 至 2026-08，共 239 个连续日历月，237 个月有有效主帖，月榜合计 4,721 条；2006-11、2007-01 无有效主帖，2006-12 只有1篇。按UTC发帖月份划分，score降序、发帖时间升序、ID升序取前20，评论数不参与排名。

原始存档部分月份得分偏低，已于2026-11-18补查HN Algolia搜索索引的高分候选，与本地有效主帖ID和精确发帖时间匹配。每月取100个候选，必要时翻页至末尾得分低于入选第20名；再扫描全部本地档案中得分达到各月入选门槛却不在候选池中的记录，用官方Firebase核对后重排。本次补入1篇（ID36860065），明确保存其补查时dead状态，官方缺少评论总数时单独注明沿用原始快照。保留本地原始数值和查询数值，分别记录score_source/comments_source。网页显示查询时得分，不代表月末得分、最终得分或历史HN首页排名。搜索索引本身仍可能遗漏帖子，原始低分也可能使其他漏项未被发现。

每篇保留原题，并配一句中文导读，供读者选择感兴趣的讨论。导读由模型依据标题与已有自帖节选逐条撰写，不概括未读的外链全文或评论区，原题中的主张与指控保留归属。编辑源在 `data/monthly-top-guides.json`，通过 `guide_zh` 字段合入规范数据，不参与排名；中文导读同样可以在当前榜单搜索。

规范数据为 `public/downloads/hn-monthly-top20/rankings.json`，页面通过 `src/lib/monthly-top.mjs` 读取。目录内保留完整JSON／CSV／Markdown、239个月的JSON／CSV、核验及ZIP，共484个文件。网页只加载当前20条的筛选字段；静态页在关闭JavaScript时仍可完整浏览和翻月。`?q=`仅搜索当前榜单，保留原始排名，`#story-ID`为帖子定位链接。

重跑脚本和合成边界测试在 `scripts/hn-monthly-top20/`，需要Python3和DuckDB。显式传入本地去重索引、结果目录和API缓存目录：

```sh
python3 scripts/hn-monthly-top20/build_results.py --index /path/to/all-stories.parquet --output /path/to/results --cache /path/to/api-cache --guides data/monthly-top-guides.json
python3 -m unittest discover -s scripts/hn-monthly-top20 -p 'test_*.py'
python3 tests/monthly_top_browser.py --base-url http://127.0.0.1:4321/data-lab/
```

完整同步导出后核对连续月份、排名、全部中文导读、JSON／CSV／ZIP的一致性、补查时间和哈希。刷新查询值时使用新的缓存目录，保留旧版研究记录，不与旧快照混用。出现新入选条目时先补齐导读，否则指定 `--guides` 的导出会报错。原始API响应仅保存在研究项目中，发布目录保留其哈希和复核记录。

## Ask / Show 每月 Top 10 维护

`/hn/ask-show/` 提供两个频道入口，`/hn/ask-show/ask/` 与 `/hn/ask-show/show/` 各自提供完整年月档案，月页为 `/hn/ask-show/<频道>/YYYY-MM/`。每个频道覆盖2006-10至2026-08的239个连续UTC自然月，独立按score降序、时间升序、ID升序取前10。频道切换保留月份；空月与不足10篇的月份如实保留。

Ask按原始无外链自帖识别，排除Show，因此包含Tell HN、Launch HN及其他自帖。Show按原始标题的Show HN／早期Show YC前缀识别，忽略大小写。Algolia频道标签与不限频道的story查询合并召回高分候选，与本地ID、精确时间、原始类别匹配；不限频道的检索继续到得分低于各频道入选门槛，以覆盖同分边界及标题／标签被修改的原始类别帖子。原始高分记录未被召回时用官方Firebase核对；保留当前状态与各字段来源。使用查询时分数，原始与当前分类可能不同，索引仍可能遗漏。

共4,351篇不同主帖（Ask 2,348篇、Show 2,003篇），各配一句中文导读。规范数据位于 `public/downloads/hn-ask-show-top10/rankings.json`，由 `src/lib/ask-show.mjs` 直接读取。元数据为 `data/ask-show.json`，逐条中文导读编辑源为 `data/ask-show-guides.json`，与每条 `guide_zh` 一致。导读依据原题与已有自帖节选撰写，不概括外链全文或评论区。导出共966个文件，ZIP内含其余965个文件；两个频道、各月及ZIP须完整同步，网页与导出使用同一份数据；更新入选记录先补齐导读。

```sh
python3 scripts/hn-ask-show-top10/build_results.py --index /path/to/all-stories.parquet --output /path/to/results --cache /path/to/cache --guides data/ask-show-guides.json
python3 -m unittest discover -s scripts/hn-ask-show-top10 -p 'test_*.py'
python3 tests/ask_show_browser.py --base-url http://127.0.0.1:4326/data-lab/
python3 tests/ask_show_browser.py --base-url https://shcalm.github.io/data-lab/ --skip-full-archive --download-timeout-ms 180000
```

复用同级 `hn-monthly-top20` 的来源、文本与导出辅助函数。刷新时使用新缓存并保留旧快照，核对所有月份、导读、数据来源、CSV／JSON／ZIP与哈希。验收同时覆盖原有月榜，避免共享日历和榜单组件改变已有行为。

## 课程与学习资源维护

`/hn/learning-resources/` 提供25个学习主题、83项资源、36个推荐来源讨论及183段引文。主题分为计算机、数学与AI、物理与工程、人文社会、艺术、学习方法六个领域。资源支持`topic`、`kind`和`q`交叉筛选，资源永久链接为`#resource-<id>`；链接目标被条件隐藏时恢复完整列表再展开。

完整同步上游 `hacker_news/reports/learning-resources/results/` 到 `public/downloads/hn-learning-resources/`，包括CSV、JSON、Markdown、各主题文件、核验记录和ZIP。`src/lib/learning-resources.mjs`直接读取同一份`resources.json`，在原内容外添加浏览字段；主题导航元数据在`data/learning-resources.json`，纯筛选在`src/lib/learning-resources-filter.mjs`。资源属于多个主题时总数仍按独立ID计，不展示为全站推荐排名。

181段引文与下载档案一致，另外2段评论有后续编辑，已保留当前树版本标记；页面保留不同意见、先修、历史版本、已失效入口与后续材料的区别。已复核的导出JSON是发布输入，原始索引和讨论树保留在研究项目中。更新时保持JSON、CSV、Markdown和ZIP一致，核对所有资源与主题数量、引文状态、入口说明和下载字节。

```sh
node --test tests/learning-resources.test.mjs
npm run build
python3 tests/learning_resources_browser.py --base-url http://127.0.0.1:4327/data-lab/
```

关闭JavaScript仍显示83项完整资源和183段可原生展开的引文。界面沿用站点颜色与排版，不引入额外前端框架。

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
