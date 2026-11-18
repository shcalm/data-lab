# HN 全时段与每月 Top 20

覆盖 2006-10-09T18:21:51Z 至 2026-08-23T08:44:12Z。共 239 个连续日历月，237 个月有有效帖子，逐月榜单共 4721 条，另列全时段20条。

## 排名与数据

按 score 降序、UTC发帖时间升序、ID升序取前20。评论数仅展示，不参与排序。同一条目只属于其发帖月份；零帖与不足20条的月份如实保留。首月和末月仅覆盖实际数据日期。

下载源：https://huggingface.co/datasets/open-index/hacker-news，revision `c54ced5973b95d80cd934b8921f44ec8d87c3cd1`，ODC-By-1.0；原始内容权利属于各作者。本地索引有 4,755,791 条有效主帖，排除 deleted、dead、无标题记录。索引SHA256：`7c81ec5ce8d6dbf8a01c3b2d472832b05706b2de6d586d15280675bffeb9a23a`。

原始存档部分时段的得分和评论数偏低，因此补查 HN Algolia 搜索索引的各月高分候选。空查询按points排序，每页100条，与本地ID和精确发帖时间匹配；候选末尾得分须低于入选第20名，若有同分或匹配不足则继续翻页。只收录本地有效主帖，未额外引入本地不存在的帖子。

另扫描全部本地档案中原始得分达到各月入选门槛、但未出现在搜索候选中的记录，用官方Firebase API补核ID、精确时间、类型和得分，再重新排序。此次核对 1 篇，入选 1 篇。是否有资格参与以原始档案状态为准；补查时的dead/deleted状态另存为current_dead/current_deleted并在页面说明。官方记录若无descendants，评论数保留原始archive_comments，comments_source=archive；不以kids长度冒充评论总数。标题和原文地址仍使用原始档案。

补查范围：2026-11-18T10:37:43Z 至 2026-11-18T11:06:37Z。score/comments分别注明score_source/comments_source，原始archive_score/archive_comments另存。搜索索引无候选时明确回退到本地快照，月份为：无。无有效帖子月份：2006-11, 2007-01。

这是一份可复核的查询时得分榜，不能还原HN首页的时间衰减排名，也不是月末或最终得分。索引覆盖范围和查询时间会影响结果；即使核对已知高分漏项，原始分数偏低也可能使其他漏项未被发现。

标题与自帖节选来自本地原始档案。此次有 4721 篇中文导读，字段guide_zh；导读由模型依据原题及已有自帖节选逐条撰写，是帮助选择阅读的说明，不是外链全文或评论区总结。标题中的观点、质疑、指控仍属于原作者表达。导读不参与排名。编辑源文件SHA256：`10e4de003107d089183196edd5659155d29c1ae8e6e78bc6c149144efbcde61b`。

## 文件与复核

- rankings.json：网页共用的规范数据，含全时段20、连续月份、每月统计和排名。
- rankings.csv：scope=all-time或monthly；全时段20与逐月条目分别保留，不应直接混合计数。
- rankings.md：按年月整理的完整可读榜单。
- months/YYYY-MM.json与.csv：逐月独立数据。
- verification.json：独立SQL验算、原始索引校验值及原始API响应摘要。
- hn-monthly-top20.zip：上述全部文件。

重跑：`.venv/bin/python reports/monthly-top20/build_results.py --index reports/interesting-themes/research/all-stories.parquet --output reports/monthly-top20/results --cache reports/monthly-top20/api-cache --guides reports/monthly-top20/guides/guides.json`。缓存保存在研究目录api-cache，刷新时应另用空缓存目录并保留旧版。使用本站仓库scripts中的副本时必须显式传入--index、--output、--cache及--guides；本站导读编辑源位于data/monthly-top-guides.json。提供--guides时会要求每条入选记录都有中文导读；刷新榜单产生新入选条目时应先补齐导读。
