# Ask / Show 每月 Top10

沿用现有 HN 月榜：覆盖完整下载档案的2006-10至2026-08，每月分别提供 Ask 与 Show 各10篇，得分降序，UTC发帖时间、ID升序作同分排序。保留原题、一句中文导读、原帖节选、得分与评论的各自来源、HN及原文链接。评论数不参与排序。

按 Algolia 的 ask_hn / show_hn 标签检索各月高分候选，匹配本地有效主帖的原始ID与精确时间。Ask频道包含普通自帖与Tell HN；本地档案类别候选以无外链自帖（排除Show前缀）识别，Show以Show HN／早期Show YC前缀识别。扫描原始分数达到入选门槛却未被索引召回的本地类别候选，核对官方Firebase；保留当前状态、原始标题与评论来源。未能核实的记录显式标注，不混用为当前得分。空月及不足10篇如实显示。

页面沿用纸色与绿色月榜，新增 /hn/ask-show/ 入口，Ask/Show两张频道卡；频道入口 /hn/ask-show/ask/ 与 /show/，独立月份页 /hn/ask-show/<channel>/YYYY-MM/。频道切换保留月份，原生链接无需JavaScript；当前10条搜索沿用现有组件。原有全帖Top20数据和路径保持稳定。

复用 MonthlyTopList 与可传入project的 MonthlyTopArchive。新的频道加载器读取规范JSON，复用URL清洗与搜索字段增强。独立导出脚本、JSON／CSV／Markdown／逐月文件／ZIP、核验记录和导读编辑源。独立合成边界测试、全量数据SQL复核、所有静态月页字段一致性、生产浏览器新功能及旧页面回归。

此任务延续用户已授权的Data Lab整理与发布工作；无需再进行设计、合并、发布确认。实现前自查范围、数据口径与字段，完成后独立审查并发布，核对exact implementation SHA的Pages成功及线上行为。
