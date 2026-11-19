# Ask / Show 每月 Top10

覆盖原始档案 2006-10-09T18:21:51Z 至 2026-08-23T08:44:12Z，共 239 个连续UTC自然月；Ask和Show各取每月前10，共 4351 条。Ask 2348 条，Show 2003 条。

按score降序、UTC发帖时间升序、ID升序；评论数不参与排序。取自本地 4,755,791 篇有效主帖，排除原始deleted/dead/无标题记录。来源 https://huggingface.co/datasets/open-index/hacker-news，revision `c54ced5973b95d80cd934b8921f44ec8d87c3cd1`，ODC-By-1.0；内容权利归原作者。索引SHA256 `7c81ec5ce8d6dbf8a01c3b2d472832b05706b2de6d586d15280675bffeb9a23a`。

Ask按原始无外链自帖（不含Show）识别，因此含Tell HN、Launch HN等自帖；Show按原始Show HN或早期Show YC前缀识别，忽略大小写。按Algolia标签ask_hn/show_hn及不限频道的story空查询合并候选，每页100条，ID和精确UTC时间匹配原始档案，再按原始类别取Top10。不限定频道的检索继续到末尾得分低于各频道第10名，同分边界继续翻页；已匹配该月全部原始类别记录或检索穷尽时停止。此方式也覆盖标题修改、当前频道标签被移除的帖子。类别与当前标签不符时category_source=archive。触及每次查询1000条的分页上限时，按上一页末尾分数设置包含等分的points上限，重新分段查询；API错误不作为空结果接受。已穷尽的早期月份如实保留。

另扫描全部原始类别候选中分数达到各月门槛但未被索引召回的记录，用官方Firebase核对ID／时间／类型／得分，共核对 1 篇、补入 1 篇；类别仍按原始档案，category_source显式注明。标题／URL保留原始值，当前dead/deleted状态另列。官方缺少descendants时评论数沿用archive_comments，comments_source=archive，未用kids长度作总评论数。

不影响入选边界的ID／时间冲突保留在verification.json，若冲突可能改变榜单则导出失败，须先核对。

补查 2026-11-18T10:37:43Z 至 2026-11-19T02:55:33Z。score_source/comments_source分别记来源；archive_score/archive_comments保存原始快照。这是查询时得分榜，不能还原月末、最终分数或历史首页排名。搜索索引仍可能遗漏，原始低分可能掩盖更多漏项；原始与当前频道分类也可能不同。首末月仅含存档日期，空月与不足10篇的月份如实保留。

每篇配一句中文导读（guide_zh，共 4351 篇），由模型依据原始标题与已有自帖节选逐条撰写，帮助选择阅读；不概括外链全文或评论区。原题中的观点、疑问和指控保留归属。导读不参与排名。编辑源SHA256 `81a955aaca1424b074ff6bce2f1211622e36842e71f3611b189ee31ad5a089c0`。

文件：rankings.json／csv／md为完整双频道数据；ask/与show/各有独立rankings.json／csv及239个月的JSON／CSV。verification.json保存SQL独立重排、原始响应哈希与数据校验值。hn-ask-show-top10.zip收录全部文件。原始API缓存留在研究目录。

重跑：`python3 scripts/hn-ask-show-top10/build_results.py --index /path/to/all-stories.parquet --output /path/to/results --cache /path/to/cache --guides data/ask-show-guides.json`；需要Python3、DuckDB以及同级hn-monthly-top20辅助脚本。研究项目中的辅助目录名为monthly-top20。刷新使用新缓存，保留旧快照；新入选记录须补齐中文导读。
