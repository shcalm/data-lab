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


## 全时段 Top 20

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Stephen Hawking has died](https://news.ycombinator.com/item?id=16582136) | 物理学家 Stephen Hawking 去世。 | 6015 | 436 | 2018-03-14 |
| 2 | [A Message to Our Customers](https://news.ycombinator.com/item?id=11116274) | Apple 向客户发布一封公开信。 | 5771 | 967 | 2016-02-17 |
| 3 | [OpenAI Announces Leadership Transition](https://news.ycombinator.com/item?id=38309611) | OpenAI 宣布领导层变动。 | 5710 | 2530 | 2023-11-17 |
| 4 | [Backdoor in upstream xz/liblzma leading to SSH server compromise](https://news.ycombinator.com/item?id=39865810) | xz 与 liblzma 上游被植入可能导致 SSH 服务器失陷的后门。 | 4549 | 1849 | 2024-03-29 |
| 5 | [CrowdStrike Update: Windows Bluescreen and Boot Loops](https://news.ycombinator.com/item?id=41002195) | 用户集中报告 Windows 蓝屏与循环启动，怀疑与 CrowdStrike 更新有关。 | 4489 | 3859 | 2024-07-19 |
| 6 | [Steve Jobs has passed away.](https://news.ycombinator.com/item?id=3078128) | Steve Jobs 去世的消息引发社区悼念。 | 4338 | 363 | 2011-10-05 |
| 7 | [Bram Moolenaar Passed Away](https://news.ycombinator.com/item?id=37011324) | Vim 创建者 Bram Moolenaar 去世。 | 4310 | 428 | 2023-08-05 |
| 8 | [Mechanical Watch](https://news.ycombinator.com/item?id=31261533) | 介绍机械手表的内部结构与运作。 | 4298 | 413 | 2022-05-04 |
| 9 | [YouTube-dl has received a DMCA takedown from RIAA](https://news.ycombinator.com/item?id=24872911) | RIAA 发出 DMCA 下架通知，要求移除 youtube-dl。 | 4240 | 1443 | 2020-10-23 |
| 10 | [Don't post generated/AI-edited comments. HN is for conversation between humans.](https://news.ycombinator.com/item?id=47340079) | HN 要求用户不要发布生成或经 AI 编辑的评论，以维护人与人的对话。 | 4229 | 1668 | 2026-03-11 |
| 11 | [Reflecting on one very, very strange year at Uber](https://news.ycombinator.com/item?id=13682022) | 作者回顾自己在 Uber 度过的极不寻常的一年。 | 4107 | 1013 | 2017-02-19 |
| 12 | [Google’s copying of the Java SE API was fair use [pdf]](https://news.ycombinator.com/item?id=26699106) | 法院认定谷歌复制 Java SE API 属于合理使用。 | 4103 | 932 | 2021-04-05 |
| 13 | [GPT-4](https://news.ycombinator.com/item?id=35154527) | OpenAI 发布 GPT-4。 | 4091 | 2507 | 2023-03-14 |
| 14 | [Replit used legal threats to kill my open-source project](https://news.ycombinator.com/item?id=27424195) | 开发者称 Replit 通过法律威胁终结其开源项目。 | 4022 | 1274 | 2021-06-07 |
| 15 | [How I cut GTA Online loading times by 70%](https://news.ycombinator.com/item?id=26296339) | 开发者分享将 GTA Online 加载时间缩短七成的过程。 | 3883 | 699 | 2021-02-28 |
| 16 | [Bye, Amazon](https://news.ycombinator.com/item?id=23065782) | 作者讲述与亚马逊告别的决定。 | 3816 | 1097 | 2020-05-04 |
| 17 | [Kevin Mitnick has died](https://news.ycombinator.com/item?id=36795173) | 知名黑客 Kevin Mitnick 去世。 | 3699 | 613 | 2023-07-19 |
| 18 | [Sora: Creating video from text](https://news.ycombinator.com/item?id=39386156) | OpenAI 展示由文字生成视频的 Sora。 | 3647 | 2231 | 2024-02-15 |
| 19 | [Google Search Is Dying](https://news.ycombinator.com/item?id=30347719) | 作者分析谷歌搜索质量衰退的迹象。 | 3636 | 1561 | 2022-02-15 |
| 20 | [Every Google result now looks like an ad](https://news.ycombinator.com/item?id=22107823) | 谷歌搜索结果的外观越来越像广告，链接辨识变得困难。 | 3592 | 972 | 2020-01-21 |

## 2006-10

有效主帖 44 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Y Combinator](https://news.ycombinator.com/item?id=1) | 创业孵化机构 Y Combinator 的官方网站入口。 | 57 | 3 | 2006-10-09 |
| 2 | [A Student's Guide to Startups](https://news.ycombinator.com/item?id=2) | 面向学生介绍如何理解创业并迈出第一步。 | 16 | 0 | 2006-10-09 |
| 3 | [Google Acquires YouTube For $1.6B](https://news.ycombinator.com/item?id=27) | Google 宣布以约 16 亿美元收购 YouTube。 | 12 | 0 | 2006-10-10 |
| 4 | [Black triangle: a useful shorthand and metaphor](https://news.ycombinator.com/item?id=57) | 用“黑色三角形”比喻开发中难以从外观察觉的进展。 | 12 | 1 | 2006-10-14 |
| 5 | [Feld: Question Regarding NDAs](https://news.ycombinator.com/item?id=16) | Brad Feld 提出有关保密协议的问题。 | 11 | 0 | 2006-10-09 |
| 6 | [LikeBetter featured by BBC](https://news.ycombinator.com/item?id=8) | LikeBetter 获得 BBC 报道，展示产品受到的关注。 | 10 | 0 | 2006-10-09 |
| 7 | [MySpace: Not a purely viral start](https://news.ycombinator.com/item?id=24) | 追溯 MySpace 早期增长，质疑纯粹依靠病毒传播的说法。 | 9 | 0 | 2006-10-10 |
| 8 | [Salaries at VC-backed companies](https://news.ycombinator.com/item?id=20) | 关注获得风险投资的公司如何确定员工薪酬。 | 8 | 1 | 2006-10-09 |
| 9 | [Woz Interview: the early days of Apple](https://news.ycombinator.com/item?id=3) | 沃兹尼亚克在访谈中回顾苹果公司的创立初期。 | 7 | 0 | 2006-10-09 |
| 10 | [Google, YouTube acquisition announcement could come tonight](https://news.ycombinator.com/item?id=5) | 报道 Google 与 YouTube 可能当晚公布收购消息。 | 7 | 0 | 2006-10-09 |
| 11 | [Top ten geek business myths](https://news.ycombinator.com/item?id=53) | 梳理技术创业中常见的十种商业迷思。 | 7 | 0 | 2006-10-12 |
| 12 | [NYT: How Friendster Blew It](https://news.ycombinator.com/item?id=58) | 《纽约时报》追问 Friendster 如何错失发展机会。 | 7 | 0 | 2006-10-15 |
| 13 | [Best IRR ever?  YouTube 1.65B...](https://news.ycombinator.com/item?id=21) | 从 YouTube 的高价收购案看投资回报率。 | 6 | 1 | 2006-10-10 |
| 14 | [NYC Developer Dilemma](https://news.ycombinator.com/item?id=4) | 聚焦纽约开发者面临的职业与创业选择困境。 | 5 | 0 | 2006-10-09 |
| 15 | [Sevin Rosen Unfunds - why?](https://news.ycombinator.com/item?id=7) | 追问 Sevin Rosen 停止募集基金背后的缘由。 | 5 | 0 | 2006-10-09 |
| 16 | [Participation Inequality: Encouraging More Users to Contribute](https://news.ycombinator.com/item?id=11) | 分析用户贡献不均的现象，以及如何鼓励更多人参与。 | 5 | 0 | 2006-10-09 |
| 17 | [Wired: The Desktop is Dead](https://news.ycombinator.com/item?id=12) | 《连线》提出桌面时代终结的判断。 | 5 | 0 | 2006-10-09 |
| 18 | [The Hardest Lessons for Startups to Learn](https://news.ycombinator.com/item?id=13) | 梳理初创公司最难真正学会的几条教训。 | 5 | 0 | 2006-10-09 |
| 19 | [A Story About Not Going IPO During The Bubble](https://news.ycombinator.com/item?id=25) | 回顾一家企业在互联网泡沫期间没有上市的经历。 | 5 | 0 | 2006-10-10 |
| 20 | [Scratchtop - notepad for the web](https://news.ycombinator.com/item?id=32) | 介绍面向网页使用的记事本工具 Scratchtop。 | 5 | 0 | 2006-10-10 |

## 2006-11

有效主帖 0 条；排名来源 empty。

本地档案中没有有效主帖。

## 2006-12

有效主帖 1 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Productivity Surges During Reddit Downtime](https://news.ycombinator.com/item?id=62) | 以 Reddit 宕机时生产力上升的说法调侃上网习惯。 | 3 | 0 | 2006-12-14 |

## 2007-01

有效主帖 0 条；排名来源 empty。

本地档案中没有有效主帖。

## 2007-02

有效主帖 510 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Please tell us what features you'd like in news.ycombinator](https://news.ycombinator.com/item?id=363) | 邀请用户为 news.ycombinator 提出功能需求。 | 262 | 1590 | 2007-02-21 |
| 2 | [Why we made this site](https://news.ycombinator.com/item?id=189) | 解释创建这个创业新闻社区的初衷。 | 166 | 58 | 2007-02-20 |
| 3 | [I Dropped Out of Grad School Today](https://news.ycombinator.com/item?id=227) | 作者记录自己当天退出研究生学习的决定。 | 92 | 49 | 2007-02-21 |
| 4 | [Seven steps to remarkable customer service](https://news.ycombinator.com/item?id=122) | 介绍提升客户服务体验的七个步骤。 | 83 | 8 | 2007-02-19 |
| 5 | [Getting Real: Free Book by 37signals](https://news.ycombinator.com/item?id=574) | 37signals 免费公开产品开发书籍《Getting Real》。 | 72 | 8 | 2007-02-23 |
| 6 | [On Having Balls, Part II: Staying Hungry](https://news.ycombinator.com/item?id=110) | 围绕保持进取心谈创业者应有的胆量。 | 67 | 1 | 2007-02-19 |
| 7 | [Forget VC Money, Fund Yourself](https://news.ycombinator.com/item?id=721) | 主张创业者通过自筹资金启动公司。 | 66 | 24 | 2007-02-23 |
| 8 | [Notes from Del.icio.us founder Joshua Schachter](https://news.ycombinator.com/item?id=495) | 整理 Del.icio.us 创始人 Joshua Schachter 的经验。 | 61 | 14 | 2007-02-22 |
| 9 | [Startup news link submission site.](https://news.ycombinator.com/item?id=124) | 介绍一个供用户提交创业新闻链接的网站。 | 58 | 19 | 2007-02-19 |
| 10 | [Dexter Walks (first dynamically balancing biped robot)](https://news.ycombinator.com/item?id=1315) | 展示可动态保持平衡的双足机器人 Dexter。 | 55 | 20 | 2007-02-27 |
| 11 | [Brutal reality of startup life](https://news.ycombinator.com/item?id=1545) | 讲述创业生活中残酷而现实的一面。 | 39 | 10 | 2007-02-28 |
| 12 | [Startup School 2007: 3/24 at Stanford](https://news.ycombinator.com/item?id=74) | 公布 2007 年创业学校在斯坦福举办的时间。 | 37 | 0 | 2007-02-19 |
| 13 | [Defiance of the &#34;Venture Capital&#34; Model [video] - Panel with Guy Kawasaki, Fark, Hi5, Suicide Girls, HotOrNot](https://news.ycombinator.com/item?id=667) | 创业者在视频圆桌中讨论对风险投资模式的挑战。 | 35 | 11 | 2007-02-23 |
| 14 | [Inside Myspace.com - (great info on how they scaled)](https://news.ycombinator.com/item?id=1015) | 介绍 MySpace 为扩大系统规模采用的技术做法。 | 35 | 9 | 2007-02-25 |
| 15 | [Ten rules for web startups](https://news.ycombinator.com/item?id=276) | 为互联网初创公司提出十条行动准则。 | 34 | 0 | 2007-02-21 |
| 16 | [Applications open for summer 2007 YC funding](https://news.ycombinator.com/item?id=445) | Y Combinator 开放 2007 年夏季项目申请。 | 32 | 55 | 2007-02-22 |
| 17 | [Startupping - a community for Internet entrepreneurs](https://news.ycombinator.com/item?id=317) | 介绍面向互联网创业者的社区 Startupping。 | 28 | 4 | 2007-02-21 |
| 18 | [NDA = Not doing anything](https://news.ycombinator.com/item?id=638) | 以“什么也没做”讽刺创业中过分依赖保密协议。 | 27 | 12 | 2007-02-23 |
| 19 | [Why you should study at Stanford](https://news.ycombinator.com/item?id=1328) | 阐述选择斯坦福学习的理由。 | 26 | 6 | 2007-02-27 |
| 20 | [From Oxford to Silicon Valley](https://news.ycombinator.com/item?id=63) | 讲述从牛津走向硅谷的经历。 | 25 | 2 | 2007-02-19 |

## 2007-03

有效主帖 1,732 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Why to Not Not Start a Startup](https://news.ycombinator.com/item?id=6668) | 逐一审视那些让人不敢创业的理由。 | 99 | 139 | 2007-03-27 |
| 2 | [Paul Graham convinced me to drop out of school / quit my job [Vote up if true]](https://news.ycombinator.com/item?id=6918) | 邀请因 Paul Graham 而退学或辞职的读者投票。 | 98 | 58 | 2007-03-28 |
| 3 | [y combinator news bookmarklet](https://news.ycombinator.com/item?id=2929) | 提供便于向 YC 新闻提交链接的浏览器书签工具。 | 85 | 12 | 2007-03-08 |
| 4 | [Kiko guys back as reality tv stars](https://news.ycombinator.com/item?id=4950) | Kiko 创业者以真人秀明星身份再次出现。 | 75 | 25 | 2007-03-19 |
| 5 | [Scaling Y Combinator: the Grahambot [PNG]](https://news.ycombinator.com/item?id=7554) | 用 Grahambot 图片戏谈如何扩大 Y Combinator 规模。 | 58 | 12 | 2007-03-30 |
| 6 | [Moonlighter's Dilemma: Guide to Starting a Startup PartTime](https://news.ycombinator.com/item?id=1758) | 为兼顾本职工作的创业者提供兼职创业指南。 | 45 | 8 | 2007-03-01 |
| 7 | [The 53,651 meme](https://news.ycombinator.com/item?id=4101) | 介绍围绕数字 53,651 流传的网络话题。 | 45 | 17 | 2007-03-14 |
| 8 | [The lessons I've learnt during Y Combinator](https://news.ycombinator.com/item?id=3542) | 作者总结参加 Y Combinator 期间学到的经验。 | 40 | 9 | 2007-03-11 |
| 9 | [Search News YC (unofficial)](https://news.ycombinator.com/item?id=4780) | 推出可搜索 YC 新闻内容的非官方工具。 | 39 | 6 | 2007-03-17 |
| 10 | [To win big, shrink a market.](https://news.ycombinator.com/item?id=3782) | 提出通过缩小市场来争取更大成功的观点。 | 37 | 7 | 2007-03-12 |
| 11 | [The Architecture of Mailinator - averaging 4.5million emails a day on a single 2Ghz machine](https://news.ycombinator.com/item?id=7859) | 介绍 Mailinator 单机日处理约 450 万封邮件的架构。 | 37 | 11 | 2007-03-31 |
| 12 | [Demo Day: Y Combinator's Spring Chicks](https://news.ycombinator.com/item?id=3098) | 报道 Y Combinator 春季团队的 Demo Day 展示。 | 36 | 19 | 2007-03-09 |
| 13 | [Aaronsw: We'd set out to make something people want -- but what if they didn't want to want it?](https://news.ycombinator.com/item?id=7543) | Aaron Swartz 反思用户想要却不愿承认想要的产品。 | 36 | 17 | 2007-03-30 |
| 14 | [The First Penny - getting your users to pay you anything at all](https://news.ycombinator.com/item?id=3670) | 探讨如何让用户迈出首次付费的一步。 | 34 | 16 | 2007-03-12 |
| 15 | [The Graphing Calculator Story](https://news.ycombinator.com/item?id=1741) | 讲述图形计算器软件背后的开发故事。 | 33 | 6 | 2007-03-01 |
| 16 | [New YC Startup: Buxfer](https://news.ycombinator.com/item?id=2055) | 介绍 Y Combinator 新团队 Buxfer。 | 32 | 22 | 2007-03-03 |
| 17 | [Guy Kawasaki on Founders at Work](https://news.ycombinator.com/item?id=2798) | Guy Kawasaki 分享对《Founders at Work》的看法。 | 32 | 22 | 2007-03-08 |
| 18 | [Paul Buchheit: Equity math for startups (sometimes 0.1% equals $138 million)](https://news.ycombinator.com/item?id=5050) | Paul Buchheit 用实例解释创业公司股权的价值。 | 30 | 7 | 2007-03-19 |
| 19 | [Failing Cheaper](https://news.ycombinator.com/item?id=3944) | 讨论如何降低创业失败所付出的代价。 | 29 | 0 | 2007-03-13 |
| 20 | [Paul Graham's Talk at Startup School 2007](https://news.ycombinator.com/item?id=6134) | 分享 Paul Graham 在 2007 年创业学校的演讲。 | 29 | 20 | 2007-03-25 |

## 2007-04

有效主帖 2,056 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [My YC app: Dropbox - Throw away your USB drive](https://news.ycombinator.com/item?id=8863) | Dropbox 以替代 U 盘的构想展示其 YC 申请项目。 | 104 | 71 | 2007-04-04 |
| 2 | [Microsoft is Dead](https://news.ycombinator.com/item?id=9770) | 以“微软已死”的尖锐判断审视其行业地位。 | 77 | 445 | 2007-04-06 |
| 3 | [Y2 Combinator launches: the startup starter starter.](https://news.ycombinator.com/item?id=16764) | Y2 Combinator 以“创业启动器的启动器”戏仿孵化模式。 | 74 | 31 | 2007-04-25 |
| 4 | [Why Y Combinator is a waste of time](https://news.ycombinator.com/item?id=9361) | 作者阐述认为参加 Y Combinator 浪费时间的理由。 | 61 | 68 | 2007-04-05 |
| 5 | [The Hacker's Guide to Investors](https://news.ycombinator.com/item?id=17947) | 为技术创业者提供理解和接触投资人的指南。 | 59 | 46 | 2007-04-29 |
| 6 | [Vote up if you would like news.Ycomb add a feature where users can save their favorite stories](https://news.ycombinator.com/item?id=14957) | 征集为 YC 新闻增加收藏文章功能的支持票。 | 54 | 24 | 2007-04-20 |
| 7 | [Vote up if you're refreshing your email once a minute today](https://news.ycombinator.com/item?id=11285) | 邀请正在频繁刷新邮箱等待消息的用户投票。 | 50 | 96 | 2007-04-10 |
| 8 | [Vote up if you're rejected but will still proceed](https://news.ycombinator.com/item?id=11551) | 邀请申请被拒后仍决定继续创业的人投票。 | 50 | 62 | 2007-04-10 |
| 9 | [From Google (Norvig): How to write a spelling check in 20 lines (very cool)](https://news.ycombinator.com/item?id=10967) | Peter Norvig 展示约二十行代码实现拼写检查的方法。 | 46 | 4 | 2007-04-09 |
| 10 | [Two Kinds of Judgement](https://news.ycombinator.com/item?id=13343) | 区分并分析两种不同的判断方式。 | 37 | 31 | 2007-04-16 |
| 11 | [Jessica Livingston's Founders at Work talk at Google](https://news.ycombinator.com/item?id=15293) | Jessica Livingston 在 Google 分享《Founders at Work》。 | 36 | 8 | 2007-04-21 |
| 12 | [What I Expected from YC and What I Got](https://news.ycombinator.com/item?id=13125) | 对照作者参加 YC 前的期待与实际收获。 | 35 | 10 | 2007-04-15 |
| 13 | [Paul Graham: Handling Investors (talk at Stanford 11 April 07)](https://news.ycombinator.com/item?id=12282) | Paul Graham 在斯坦福演讲中谈如何应对投资人。 | 34 | 29 | 2007-04-12 |
| 14 | [What are the best non-database solutions you've seen? What did Viaweb use?](https://news.ycombinator.com/item?id=14605) | 征集数据库之外的数据方案，并追问 Viaweb 的做法。 | 34 | 65 | 2007-04-19 |
| 15 | [Lessons learned after 3 months of Y Combinator](https://news.ycombinator.com/item?id=11594) | 作者总结参加 Y Combinator 三个月后的经验。 | 33 | 6 | 2007-04-10 |
| 16 | [The problem with conventional databases](https://news.ycombinator.com/item?id=16098) | 审视传统数据库方案存在的问题。 | 33 | 38 | 2007-04-23 |
| 17 | [Paul Buchheit: The secret to making things easy: avoid hard problems](https://news.ycombinator.com/item?id=16409) | Paul Buchheit 提出通过避开难题让事情变简单。 | 33 | 32 | 2007-04-24 |
| 18 | [Y Combinator interview tips](https://news.ycombinator.com/item?id=9935) | 分享准备 Y Combinator 面试的实用建议。 | 32 | 9 | 2007-04-07 |
| 19 | [Vote up if you want the submission title displayed as your browser title for bookmarking](https://news.ycombinator.com/item?id=16703) | 建议把投稿标题用作页面标题，方便浏览器收藏。 | 32 | 12 | 2007-04-25 |
| 20 | [What is the best credit card processing setup for startups?](https://news.ycombinator.com/item?id=12010) | 征求适合初创公司的信用卡收款方案。 | 30 | 23 | 2007-04-11 |

## 2007-05

有效主帖 1,940 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Vote up if you want YC to remember your cookie for longer than a few hours](https://news.ycombinator.com/item?id=18275) | 征集延长 YC 新闻登录 Cookie 有效期的支持。 | 78 | 15 | 2007-05-01 |
| 2 | [Inc Magazine: "Lucky things happen to entrepreneurs who start fundamentally innovative, morally compelling, and philosophically positive companies."](https://news.ycombinator.com/item?id=20032) | 《Inc》文章将创业好运与创新、道德及积极理念联系起来。 | 44 | 23 | 2007-05-06 |
| 3 | [Aaron Swartz explains why he left reddit](https://news.ycombinator.com/item?id=20219) | Aaron Swartz 解释自己离开 Reddit 的原因。 | 44 | 29 | 2007-05-07 |
| 4 | [A Boot Camp for the Next Tech Billionaires](https://news.ycombinator.com/item?id=21664) | 介绍培养下一批科技创业者的密集训练项目。 | 43 | 36 | 2007-05-12 |
| 5 | [The Bipolar Lisp Programmer](https://news.ycombinator.com/item?id=20012) | 讲述一位患有双相障碍的 Lisp 程序员的故事。 | 40 | 8 | 2007-05-06 |
| 6 | [The Only Way is the Wrong Way](https://news.ycombinator.com/item?id=22517) | 以“唯一的路是错路”的说法挑战常规做事思路。 | 36 | 12 | 2007-05-16 |
| 7 | [Subdomains + Development = Sucks: A quick tip from Kevin Hale of Wufoo](https://news.ycombinator.com/item?id=24089) | Wufoo 的 Kevin Hale 分享子域名开发中的小技巧。 | 36 | 22 | 2007-05-23 |
| 8 | [Y Combinator startup Scribd raises VC and creates secret jobs page just for news.ycombinator readers](https://news.ycombinator.com/item?id=20659) | Scribd 获得风投，并为 YC 新闻读者开设专属招聘页。 | 35 | 7 | 2007-05-09 |
| 9 | [The Real Story of JPG Magazine - a cautionary tale for founders](https://news.ycombinator.com/item?id=22231) | JPG Magazine 的经历为创始人提供警示。 | 33 | 12 | 2007-05-15 |
| 10 | [Virtualmin Founder Joe Cooper Explains Y Combinator to Slashdot Trolls](https://news.ycombinator.com/item?id=21907) | Virtualmin 创始人向 Slashdot 读者解释 Y Combinator。 | 32 | 29 | 2007-05-14 |
| 11 | [YC's Xobni: Lessons learned in the last 14 months](https://news.ycombinator.com/item?id=25459) | Xobni 团队总结过去十四个月的创业经验。 | 32 | 28 | 2007-05-30 |
| 12 | [Reddit's Advice On Cheap Marketing](https://news.ycombinator.com/item?id=20342) | 分享 Reddit 团队对低成本营销的建议。 | 30 | 14 | 2007-05-07 |
| 13 | [How To Stop Hostile Jerks From Killing Your Social Site by Cory Doctorow](https://news.ycombinator.com/item?id=22277) | Cory Doctorow 谈如何避免恶意用户毁掉社交网站。 | 29 | 39 | 2007-05-15 |
| 14 | [One Person Startup  5 to 10 million a year revenues.](https://news.ycombinator.com/item?id=23976) | 介绍一家据称年营收五百万至一千万美元的单人公司。 | 29 | 21 | 2007-05-23 |
| 15 | [Amazingly Bad APIs](https://news.ycombinator.com/item?id=23601) | 列举令人困扰的 API 设计案例。 | 28 | 31 | 2007-05-21 |
| 16 | [Why getting acquired sucks by Steve Gedikian of Nullsoft](https://news.ycombinator.com/item?id=24276) | Nullsoft 的 Steve Gedikian 分享对公司被收购的负面体验。 | 28 | 2 | 2007-05-24 |
| 17 | [How Ads Really Work: Superfans and Noobs -- Great post by creator of Metafilter](https://news.ycombinator.com/item?id=25710) | MetaFilter 创办者从忠实用户与新人角度解释广告效果。 | 28 | 5 | 2007-05-31 |
| 18 | [PG on Unions](https://news.ycombinator.com/item?id=20249) | 介绍 Paul Graham 对工会的看法。 | 27 | 73 | 2007-05-07 |
| 19 | [14 rules for fast web pages](https://news.ycombinator.com/item?id=21083) | 归纳提升网页加载速度的十四条规则。 | 27 | 4 | 2007-05-10 |
| 20 | [Paul Graham - The Record Label Executive](https://news.ycombinator.com/item?id=18953) | 以唱片公司高管的视角审视 Paul Graham。 | 26 | 17 | 2007-05-03 |

## 2007-06

有效主帖 1,433 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Finally, voting without refresh](https://news.ycombinator.com/item?id=27550) | YC 新闻推出无需刷新页面即可投票的功能。 | 176 | 42 | 2007-06-12 |
| 2 | [It's official: Google buys Zenter](https://news.ycombinator.com/item?id=29307) | Google 正式收购 Zenter。 | 77 | 47 | 2007-06-19 |
| 3 | [Why not to do a startup](https://news.ycombinator.com/item?id=29058) | 讨论哪些理由可能让人决定不去创业。 | 51 | 8 | 2007-06-19 |
| 4 | [Jessica Livingston, Founders at Work author and YC partner, launches her new blog powered by Weebly](https://news.ycombinator.com/item?id=29679) | Jessica Livingston 用 Weebly 搭建并推出个人博客。 | 50 | 13 | 2007-06-20 |
| 5 | [Just Say No To Google: Internal Microsoft Email](https://news.ycombinator.com/item?id=30922) | 披露微软内部一封主张拒绝 Google 的邮件。 | 47 | 13 | 2007-06-26 |
| 6 | [The Pmarca Guide to Startups, part 4: The only thing that matters](https://news.ycombinator.com/item?id=30693) | Marc Andreessen 的创业指南讨论什么才是最关键的事。 | 46 | 26 | 2007-06-26 |
| 7 | [Marc Andreessen:  Analyzing the Facebook Platform, three weeks in](https://news.ycombinator.com/item?id=27532) | Marc Andreessen 分析推出三周后的 Facebook 平台。 | 39 | 13 | 2007-06-12 |
| 8 | [How Guy Kawasaki Launched Truemors for $12,107.09](https://news.ycombinator.com/item?id=26237) | Guy Kawasaki 分享以 12,107.09 美元启动 Truemors 的过程。 | 37 | 26 | 2007-06-04 |
| 9 | [Safari on Windows](https://news.ycombinator.com/item?id=27297) | Safari 浏览器推出 Windows 版本。 | 37 | 22 | 2007-06-11 |
| 10 | [Paul Buchheit: Three types of ideas](https://news.ycombinator.com/item?id=30285) | Paul Buchheit 区分三种不同类型的创意。 | 37 | 18 | 2007-06-23 |
| 11 | [Zenter: How a six-month-old startup got bought by Google](https://news.ycombinator.com/item?id=29919) | 回顾成立仅六个月的 Zenter 被 Google 收购的过程。 | 35 | 35 | 2007-06-21 |
| 12 | [John Lam on Software: Steve Yegge ported Rails to JavaScript](https://news.ycombinator.com/item?id=30462) | John Lam 介绍 Steve Yegge 将 Rails 移植到 JavaScript 的工作。 | 33 | 16 | 2007-06-25 |
| 13 | [Web App Autopsy](https://news.ycombinator.com/item?id=30839) | 通过剖析一个 Web 应用审视其实现与问题。 | 33 | 4 | 2007-06-26 |
| 14 | [Why I don't want funding](https://news.ycombinator.com/item?id=25847) | 作者解释自己不想接受融资的原因。 | 32 | 9 | 2007-06-01 |
| 15 | [Stevey's Blog Rants: Rhino on Rails (straight from the horse's mouth)](https://news.ycombinator.com/item?id=31059) | Steve Yegge 亲自介绍 Rhino on Rails 项目。 | 32 | 14 | 2007-06-27 |
| 16 | [How Justin.TV's Live Video System Was Born](https://news.ycombinator.com/item?id=28261) | 回顾 Justin.TV 实时视频系统的诞生过程。 | 31 | 7 | 2007-06-15 |
| 17 | [Thrown out of Ebay Live for wearing Google shirt](https://news.ycombinator.com/item?id=28934) | 讲述因穿 Google 衬衫而被请出 eBay Live 的遭遇。 | 31 | 27 | 2007-06-18 |
| 18 | [Max Levchin: "The last time I got kids to drop out of college, they all bought houses for cash."](https://news.ycombinator.com/item?id=31190) | Max Levchin 以早年退学创业者的财富经历谈创业。 | 31 | 14 | 2007-06-27 |
| 19 | [Rejected Y Combinator company Bandsintown.com is now Live!](https://news.ycombinator.com/item?id=27490) | 被 YC 拒绝的 Bandsintown.com 正式上线。 | 30 | 34 | 2007-06-12 |
| 20 | [Stevey's Blog Rants: Rich Programmer Food](https://news.ycombinator.com/item?id=30136) | Steve Yegge 分享题为“程序员的丰盛食粮”的文章。 | 30 | 25 | 2007-06-22 |

## 2007-07

有效主帖 1,635 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Stuff - Paul Graham](https://news.ycombinator.com/item?id=38028) | Paul Graham 借个人经历反思不断积累物品的负担。 | 105 | 92 | 2007-07-31 |
| 2 | [The Equity Equation](https://news.ycombinator.com/item?id=35015) | 用股权公式思考创业公司中的权益分配。 | 72 | 156 | 2007-07-18 |
| 3 | [Applications Open for Winter 2008 YC Funding](https://news.ycombinator.com/item?id=32085) | Y Combinator 开放 2008 年冬季项目申请。 | 60 | 101 | 2007-07-02 |
| 4 | [Matt Maroon: Advice for Would-Be Y Combinator Founders](https://news.ycombinator.com/item?id=33410) | Matt Maroon 为计划申请 YC 的创始人提供建议。 | 54 | 21 | 2007-07-10 |
| 5 | [Note to Founders: Have Vesting](https://news.ycombinator.com/item?id=35938) | 提醒创业创始人在股权安排中设置归属期。 | 50 | 19 | 2007-07-22 |
| 6 | [If you are reading this you are not working on your startup.](https://news.ycombinator.com/item?id=34114) | 以阅读创业资讯的行为提醒创业者关注实际行动。 | 45 | 28 | 2007-07-13 |
| 7 | [Don't Break The Chain](https://news.ycombinator.com/item?id=36497) | 用“别打断链条”的方法鼓励长期坚持行动。 | 43 | 16 | 2007-07-25 |
| 8 | [The 80-hour Myth (Your best work is in bursts, surrounded by periods of dullness and inactivity)](https://news.ycombinator.com/item?id=34328) | 质疑每周工作八十小时的神话，强调高效工作的节奏。 | 37 | 12 | 2007-07-15 |
| 9 | [Y! releases YSlow for Firebug - Analyzes pages and tells you why they're slow](https://news.ycombinator.com/item?id=36543) | 雅虎发布 YSlow，帮助 Firebug 用户分析网页缓慢原因。 | 37 | 10 | 2007-07-25 |
| 10 | [New: Code in comments (plus a bit of Arc)](https://news.ycombinator.com/item?id=32768) | YC 新闻新增评论代码格式，并介绍少量 Arc 相关内容。 | 36 | 7 | 2007-07-06 |
| 11 | [Never Use a Warning When You Mean Undo](https://news.ycombinator.com/item?id=34746) | 主张在可以撤销操作时用撤销功能替代警告提示。 | 34 | 10 | 2007-07-17 |
| 12 | [The iPhone is a piece of shit, and so is your face.](https://news.ycombinator.com/item?id=34789) | 作者以激烈措辞批评 iPhone 及相关争论。 | 34 | 20 | 2007-07-17 |
| 13 | [Hungry entrepreneurs eat up Y Combinator's help](https://news.ycombinator.com/item?id=34973) | 报道创业者如何获得 Y Combinator 的帮助。 | 33 | 21 | 2007-07-18 |
| 14 | [Why you won't run out of money](https://news.ycombinator.com/item?id=33224) | 探讨为什么创业过程中未必会耗尽资金。 | 31 | 1 | 2007-07-09 |
| 15 | [Ads on paulgraham.com -- Check the bottom of any PG essay](https://news.ycombinator.com/item?id=36152) | 读者注意到 Paul Graham 文章底部出现相关广告。 | 31 | 58 | 2007-07-23 |
| 16 | [Richard Feynman and The Connection Machine](https://news.ycombinator.com/item?id=31834) | 回顾物理学家费曼与 Connection Machine 的交集。 | 30 | 5 | 2007-07-01 |
| 17 | [Facebook acquires Blake Ross and Joe Hewitt's Parakey](https://news.ycombinator.com/item?id=35409) | Facebook 收购 Blake Ross 和 Joe Hewitt 创办的 Parakey。 | 30 | 16 | 2007-07-19 |
| 18 | [The Secret...to talking to customers before you have a product -- or even a company](https://news.ycombinator.com/item?id=35550) | 介绍在产品甚至公司成立前与客户交流的方法。 | 30 | 5 | 2007-07-20 |
| 19 | [PG: If starting Viaweb today, would you use Lisp?](https://news.ycombinator.com/item?id=36905) | 追问今天重做 Viaweb 是否仍会选择 Lisp 及其思维优势。 | 30 | 33 | 2007-07-26 |
| 20 | [Real-Time 3D in Javascript using divs](https://news.ycombinator.com/item?id=33048) | 展示仅用 JavaScript、HTML 和 CSS div 实现实时三维效果。 | 28 | 6 | 2007-07-08 |

## 2007-08

有效主帖 2,503 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [How Not to Die](https://news.ycombinator.com/item?id=48294) | 以“如何不死”为题，思考避免失败与终结的办法。 | 169 | 143 | 2007-08-30 |
| 2 | [Hacker News](https://news.ycombinator.com/item?id=42317) | 介绍 Hacker News 这一新闻社区。 | 150 | 76 | 2007-08-14 |
| 3 | [Holding a program in one's head](https://news.ycombinator.com/item?id=45698) | 探讨程序员如何在头脑中把握整个程序。 | 142 | 131 | 2007-08-23 |
| 4 | [Teenage Girl's MySpace Layouts Worth Millions, Drops Out Of High School](https://news.ycombinator.com/item?id=47147) | 报道一名靠 MySpace 页面设计获利的少女选择高中退学。 | 88 | 34 | 2007-08-27 |
| 5 | [Programmers Need To Learn Statistics or I Will Kill Them All - Zed Shaw](https://news.ycombinator.com/item?id=48006) | Zed Shaw 以激烈措辞呼吁程序员学习统计学。 | 68 | 19 | 2007-08-29 |
| 6 | [Norvig: How to write a spelling corrector](https://news.ycombinator.com/item?id=42587) | Peter Norvig 逐步用 Python 构建简化的拼写纠错器。 | 63 | 7 | 2007-08-15 |
| 7 | [We are living in someone else's computer simulation](https://news.ycombinator.com/item?id=42398) | 提出人类可能生活在他人计算机模拟中的假说。 | 57 | 41 | 2007-08-14 |
| 8 | [A way to find other Y Combinator readers in your area](https://news.ycombinator.com/item?id=43942) | 提供寻找附近 Y Combinator 读者的方法。 | 55 | 38 | 2007-08-19 |
| 9 | [Norvig: Teach Yourself Programming in Ten Years](https://news.ycombinator.com/item?id=43243) | Peter Norvig 主张以十年尺度学习编程。 | 54 | 7 | 2007-08-16 |
| 10 | [Xobni's Facebook app replaces Facebook messaging with email](https://news.ycombinator.com/item?id=38908) | Xobni 的 Facebook 应用尝试用邮件替代站内消息。 | 53 | 12 | 2007-08-03 |
| 11 | [How to create a startup in 10.5 hours](https://news.ycombinator.com/item?id=43124) | FEEDJIT 作者分享从开始编码到上线十个半小时的经历。 | 53 | 19 | 2007-08-16 |
| 12 | [PG on Y Combinator](https://news.ycombinator.com/item?id=46974) | 通过访谈了解 Paul Graham 与 Y Combinator 的运作。 | 50 | 19 | 2007-08-27 |
| 13 | [Goodbye, Hacker News. I'm going back to Reddit.](https://news.ycombinator.com/item?id=43635) | 一位用户因社区内容方向与氛围变化宣布离开 HN。 | 48 | 67 | 2007-08-17 |
| 14 | [Aaron Swartz:  Perfectionism (and his new startup, Jottit)](https://news.ycombinator.com/item?id=48770) | Aaron Swartz 谈完美主义，并介绍新项目 Jottit。 | 48 | 102 | 2007-08-31 |
| 15 | [Indian mathematicians discovered infinite series in 1350](https://news.ycombinator.com/item?id=42320) | 文章称印度数学家在 1350 年已发现无穷级数。 | 45 | 13 | 2007-08-14 |
| 16 | [Scaling a startup from 0 to 40 hits per second in 3 days](https://news.ycombinator.com/item?id=45104) | 分享三天内将创业网站扩展至每秒四十次访问的经历。 | 45 | 24 | 2007-08-22 |
| 17 | [Philip Greenspun: Improving Undergraduate Computer Science Education](https://news.ycombinator.com/item?id=45773) | Philip Greenspun 提出改进本科计算机教育的建议。 | 45 | 14 | 2007-08-23 |
| 18 | [How to Massively Increase Your Productivity and Happiness in 2 Hours Per Day](https://news.ycombinator.com/item?id=39699) | 作者建议提前两小时睡觉，以改善效率与幸福感。 | 43 | 42 | 2007-08-06 |
| 19 | [Luck and the entrepreneur, part 1: The four kinds of luck](https://news.ycombinator.com/item?id=42222) | 从四种幸运的分类探讨运气与创业的关系。 | 43 | 13 | 2007-08-14 |
| 20 | [The "I Have 250,000 Users, Now What?" guy just sold his Facebook app for $3 million](https://news.ycombinator.com/item?id=43352) | 曾询问二十五万用户下一步怎么办的开发者售出 Facebook 应用。 | 43 | 21 | 2007-08-17 |

## 2007-09

有效主帖 2,423 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [CMU professor gives his last lesson on life](https://news.ycombinator.com/item?id=57195) | 一位卡内基梅隆教授在最后一课中分享人生感悟。 | 121 | 33 | 2007-09-20 |
| 2 | [Paul Graham: News from the Front](https://news.ycombinator.com/item?id=50456) | Paul Graham 以“前线消息”为题分享观察。 | 103 | 124 | 2007-09-05 |
| 3 | [Joel explains how a new monopoly will emerge around AJAX](https://news.ycombinator.com/item?id=56626) | Joel Spolsky 解释他认为 AJAX 周围将出现新垄断的原因。 | 101 | 82 | 2007-09-19 |
| 4 | [How to Do Philosophy](https://news.ycombinator.com/item?id=58025) | 探讨如何开展哲学思考。 | 96 | 229 | 2007-09-21 |
| 5 | [7 reasons I switched back to PHP after 2 years on Rails - O'Reilly Ruby](https://news.ycombinator.com/item?id=58429) | 作者列出使用 Rails 两年后重新选择 PHP 的七个理由。 | 83 | 27 | 2007-09-23 |
| 6 | [C++ is a horrible language, says Linus Torvalds](https://news.ycombinator.com/item?id=51451) | Linus Torvalds 以尖锐措辞批评 C++ 语言。 | 62 | 60 | 2007-09-07 |
| 7 | ["10 Lessons of an MIT Education" by Gian-Carlo Rota](https://news.ycombinator.com/item?id=53322) | Gian-Carlo Rota 总结麻省理工教育带来的十点启发。 | 61 | 14 | 2007-09-11 |
| 8 | [Observations from 10 Months Working at a Small Startup](https://news.ycombinator.com/item?id=49785) | 作者分享在一家小型风投创业公司工作十个月的观察。 | 58 | 6 | 2007-09-03 |
| 9 | [Are you going to change the world?  (Really?)](https://news.ycombinator.com/item?id=57298) | 由一位患癌教授的人生态度追问创业者如何改变世界。 | 57 | 94 | 2007-09-20 |
| 10 | [Guide to Low Cost, High-Impact Websites](https://news.ycombinator.com/item?id=58522) | 用十五条建议帮助以较低成本启动有效的网站项目。 | 57 | 7 | 2007-09-23 |
| 11 | [What I learned about women & business today](https://news.ycombinator.com/item?id=61006) | 作者从女性高管圆桌中思考女性与商业的问题。 | 56 | 22 | 2007-09-29 |
| 12 | [Startup idea list](https://news.ycombinator.com/item?id=55974) | 邀请读者在评论区提出创业点子并通过投票反馈。 | 54 | 167 | 2007-09-18 |
| 13 | [Love at First Byte](https://news.ycombinator.com/item?id=59512) | 以“一见字节钟情”的双关标题展开技术主题叙事。 | 54 | 6 | 2007-09-25 |
| 14 | [I Think You're Fat: The Radical Honesty Movement](https://news.ycombinator.com/item?id=50436) | 介绍主张直言不讳的“彻底诚实”运动。 | 53 | 42 | 2007-09-05 |
| 15 | [How I can charge so much](https://news.ycombinator.com/item?id=60109) | 作者解释自己为何能够收取较高价格。 | 53 | 19 | 2007-09-27 |
| 16 | [Paul Graham Facts](https://news.ycombinator.com/item?id=60433) | 以“Paul Graham 事实”为题呈现相关趣味内容。 | 53 | 27 | 2007-09-28 |
| 17 | [Steve Jobs - To All iPhone Customers](https://news.ycombinator.com/item?id=51226) | Steve Jobs 向所有 iPhone 用户发表公开信。 | 52 | 46 | 2007-09-06 |
| 18 | [Aaron Swartz's Jottit has been officially released](https://news.ycombinator.com/item?id=54977) | Aaron Swartz 与 Simon Carstensen 的 Jottit 正式发布。 | 51 | 88 | 2007-09-15 |
| 19 | [Ten Tips For A Slightly Less Awful Resume](https://news.ycombinator.com/item?id=59764) | 提供十条让简历不那么糟糕的改进建议。 | 50 | 28 | 2007-09-26 |
| 20 | [Amazon Web Services $100,000 Startup Challenge](https://news.ycombinator.com/item?id=53818) | AWS 推出奖金十万美元的创业挑战赛。 | 47 | 29 | 2007-09-12 |

## 2007-10

有效主帖 2,792 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Why to Apply to YCombinator](https://news.ycombinator.com/item?id=65327) | 作者以个人申请经历说明为何值得申请 Y Combinator。 | 113 | 36 | 2007-10-09 |
| 2 | [The Future of Web Startups](https://news.ycombinator.com/item?id=63009) | 展望 Web 初创公司的未来发展。 | 107 | 169 | 2007-10-04 |
| 3 | [Aaron Swartz: How to Get a Job Like Mine](https://news.ycombinator.com/item?id=63912) | Aaron Swartz 分享如何获得像自己这样的工作。 | 78 | 40 | 2007-10-06 |
| 4 | [Why to Move to a Startup Hub](https://news.ycombinator.com/item?id=65815) | 阐述创业者搬往创业聚集地的理由。 | 63 | 95 | 2007-10-10 |
| 5 | [What if Google had to design their user interface to rank high on Google?](https://news.ycombinator.com/item?id=68377) | 设想 Google 为迎合自身搜索排名而设计界面的结果。 | 61 | 6 | 2007-10-16 |
| 6 | [YC: What No Means](https://news.ycombinator.com/item?id=69273) | 解释 YC 语境下拒绝答复意味着什么。 | 61 | 14 | 2007-10-17 |
| 7 | [California](https://news.ycombinator.com/item?id=63702) | 把目光投向加利福尼亚这一创业者关注的地区。 | 59 | 49 | 2007-10-05 |
| 8 | [Zombo.com - YC applicant - feedback wanted](https://news.ycombinator.com/item?id=66701) | 一位 YC 申请者为 Zombo.com 原型征求反馈。 | 58 | 55 | 2007-10-12 |
| 9 | [Ask news YC: Your best sources to learn about design & usability](https://news.ycombinator.com/item?id=66863) | 征集学习设计与可用性的优质网站和博客。 | 58 | 31 | 2007-10-12 |
| 10 | [taoyue.com: Why I Never Hire Brilliant Men](https://news.ycombinator.com/item?id=73906) | 作者以“从不雇用聪明男人”为题说明其招聘观点。 | 58 | 19 | 2007-10-29 |
| 11 | [Physician with a Slick, Web 2.0-ish Method of Practice](https://news.ycombinator.com/item?id=62913) | 介绍一位采用 Web 2.0 风格方式执业的医生。 | 56 | 25 | 2007-10-04 |
| 12 | [3998-byte executable reduced to 45 bytes](https://news.ycombinator.com/item?id=68056) | 展示把 3,998 字节可执行文件缩减到 45 字节的成果。 | 55 | 10 | 2007-10-15 |
| 13 | [Zero to Riding the Rails in Four Months](https://news.ycombinator.com/item?id=68075) | 回顾四个月内从零开始学习 Rails 的过程。 | 55 | 27 | 2007-10-15 |
| 14 | [Reddit lesson #3: fuck facebook, make real friends](https://news.ycombinator.com/item?id=71189) | 从 Reddit 经历谈建立真实朋友关系的价值。 | 55 | 14 | 2007-10-22 |
| 15 | [Open Social: a new universe of social applications all over the web (Marc Andreessen)](https://news.ycombinator.com/item?id=74611) | Marc Andreessen 介绍跨网站社交应用平台 OpenSocial。 | 55 | 16 | 2007-10-31 |
| 16 | [Financial Models for Underachievers: Two Years of the Real Numbers of a Startup](https://news.ycombinator.com/item?id=61643) | 作者用创业两年的真实数据审视保守的财务预测模型。 | 54 | 6 | 2007-10-01 |
| 17 | ['Second Earth' found, 20 light years away](https://news.ycombinator.com/item?id=68563) | 报道距地球二十光年处发现所谓“第二地球”。 | 54 | 78 | 2007-10-16 |
| 18 | [What reddit taught me about startups: "because it's your damn job"](https://news.ycombinator.com/item?id=65239) | 以“这是你的职责”为线索总结 Reddit 创业经验。 | 53 | 23 | 2007-10-09 |
| 19 | [Wolfram: The Simplest Universal Turing Machine is proven by 20 year old student](https://news.ycombinator.com/item?id=72010) | 报道称一名二十岁学生证明了最简通用图灵机的通用性。 | 53 | 14 | 2007-10-24 |
| 20 | [Y Combinator co-founder Jessica Livingston shares advice on how to get accepted (audio interview)](https://news.ycombinator.com/item?id=62787) | Jessica Livingston 在音频访谈中分享申请 YC 的建议。 | 52 | 14 | 2007-10-03 |

## 2007-11

有效主帖 2,390 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Number of founders - statistics](https://news.ycombinator.com/item?id=77525) | 统计一百家上市科技公司的创始人人数，并说明局限。 | 232 | 38 | 2007-11-08 |
| 2 | [Absolutely, DO NOT, get a co-founder!](https://news.ycombinator.com/item?id=77246) | 一位有多年创业公司经验的作者主张不要寻找联合创始人。 | 112 | 94 | 2007-11-08 |
| 3 | [How to be a genius](https://news.ycombinator.com/item?id=75761) | 探讨成为天才这一目标及其实现方式。 | 77 | 37 | 2007-11-03 |
| 4 | [New Feature: get kicked off News.YC on demand](https://news.ycombinator.com/item?id=77173) | YC 新闻推出可按需限制自己访问的新功能。 | 64 | 46 | 2007-11-07 |
| 5 | [Warning: Software Startups are Not as Easy as Everyone Says](https://news.ycombinator.com/item?id=76630) | 提醒读者软件创业没有流行说法中那么容易。 | 63 | 39 | 2007-11-06 |
| 6 | [It's not exponential, it's sigmoidal](https://news.ycombinator.com/item?id=83580) | 提醒读者区分指数增长与 S 形增长。 | 63 | 8 | 2007-11-26 |
| 7 | [xkcd - Network](https://news.ycombinator.com/item?id=84141) | 分享以网络为主题的 xkcd 漫画。 | 63 | 13 | 2007-11-28 |
| 8 | [The PayPal mafia](https://news.ycombinator.com/item?id=79713) | 关注 PayPal 创业者及其后续形成的人脉网络。 | 61 | 18 | 2007-11-14 |
| 9 | [Larry and Sergey Won't Respect You In The Morning](https://news.ycombinator.com/item?id=75776) | 以 Larry 和 Sergey 为对象，讨论与 Google 的关系。 | 59 | 46 | 2007-11-03 |
| 10 | [Buffet: Saving Sex For Your Old Age](https://news.ycombinator.com/item?id=81453) | 巴菲特用“把性生活留到老年”的比喻表达看法。 | 57 | 8 | 2007-11-19 |
| 11 | [The Future of Reading (a play in 6 acts)](https://news.ycombinator.com/item?id=81834) | 以六幕剧形式思考阅读的未来。 | 53 | 11 | 2007-11-20 |
| 12 | [The Secret to Raising Smart Kids](https://news.ycombinator.com/item?id=84655) | 探讨培养聪明孩子的关键做法。 | 53 | 9 | 2007-11-29 |
| 13 | [Lessons Learned from our YC Interview (with Tips!)](https://news.ycombinator.com/item?id=77197) | 分享 YC 面试中的经验教训与准备建议。 | 52 | 20 | 2007-11-07 |
| 14 | [Fruit of 4 years of 14 hours per day, 7 days a week](https://news.ycombinator.com/item?id=79048) | 展示连续四年每天十四小时工作的成果。 | 51 | 17 | 2007-11-13 |
| 15 | [Google's Goal: Renewable Energy Cheaper than Coal](https://news.ycombinator.com/item?id=84090) | Google 提出让可再生能源比煤电更便宜的目标。 | 50 | 32 | 2007-11-28 |
| 16 | [Andrew Chen: Do you ever say, "MySpace is sooo ugly?" This blog's for you...](https://news.ycombinator.com/item?id=84807) | Andrew Chen 从 MySpace 的外观争议谈网站设计判断。 | 49 | 22 | 2007-11-29 |
| 17 | [Is Aaron Swartz the Paris Hilton of Web 2.0?](https://news.ycombinator.com/item?id=79982) | 发帖者质疑 Aaron Swartz 的知名度是否与实际贡献相称。 | 48 | 103 | 2007-11-15 |
| 18 | [Why I Program In Ruby (And Maybe Why You Shouldn't)](https://news.ycombinator.com/item?id=83161) | 作者解释自己使用 Ruby 的理由，并提醒它未必适合所有人。 | 48 | 20 | 2007-11-24 |
| 19 | [Doctorow: How Your Creepy Ex-Co-Workers Will Kill Facebook](https://news.ycombinator.com/item?id=83930) | Cory Doctorow 探讨令人不适的前同事如何影响 Facebook。 | 48 | 28 | 2007-11-27 |
| 20 | [Feynman's Letter to Wolfram](https://news.ycombinator.com/item?id=80909) | 分享费曼写给 Stephen Wolfram 的信。 | 46 | 7 | 2007-11-17 |

## 2007-12

有效主帖 2,249 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Code's Worst Enemy](https://news.ycombinator.com/item?id=91140) | 探讨什么会成为代码最棘手的敌人。 | 125 | 43 | 2007-12-19 |
| 2 | [We didn't start the Fire (2.0)](https://news.ycombinator.com/item?id=86003) | 以《We Didn't Start the Fire》为题呈现 2.0 版本内容。 | 103 | 57 | 2007-12-04 |
| 3 | [Rails is a Ghetto... [NSFW for Language]](https://news.ycombinator.com/item?id=93984) | 作者用激烈措辞批评 Rails 社区。 | 94 | 68 | 2007-12-31 |
| 4 | [Joel Spolsky's talk at Yale, part 1](https://news.ycombinator.com/item?id=85671) | 分享 Joel Spolsky 在耶鲁大学的演讲上半部分。 | 73 | 36 | 2007-12-03 |
| 5 | [Evan Williams: Will it fly? How to Evaluate a New Product Idea](https://news.ycombinator.com/item?id=90198) | Evan Williams 介绍评估新产品创意的方法。 | 70 | 23 | 2007-12-17 |
| 6 | [Success [pic]](https://news.ycombinator.com/item?id=89610) | 通过一张图片呈现对“成功”的理解。 | 64 | 13 | 2007-12-14 |
| 7 | [Ask 37signals: How do you process credit cards?](https://news.ycombinator.com/item?id=93320) | 向 37signals 询问信用卡支付处理方式。 | 61 | 10 | 2007-12-28 |
| 8 | [The Dictatorship of Talent](https://news.ycombinator.com/item?id=86506) | 探讨以人才为核心的权力与决策方式。 | 59 | 60 | 2007-12-06 |
| 9 | [Randall Munroe talks xkcd at Google (astounding cameo at 21:30)](https://news.ycombinator.com/item?id=88662) | Randall Munroe 在 Google 演讲介绍 xkcd。 | 59 | 12 | 2007-12-12 |
| 10 | [AppJet (YC co) Makes Simple Web Apps A Breeze](https://news.ycombinator.com/item?id=88711) | 介绍让简单 Web 应用更易开发的 YC 项目 AppJet。 | 58 | 36 | 2007-12-12 |
| 11 | [Man, weather.com really sucks. I bet I could make a better one in a day.](https://news.ycombinator.com/item?id=93683) | 作者抱怨 weather.com，并提出一天做出更好网站的挑战。 | 57 | 48 | 2007-12-30 |
| 12 | [Joel Spolsky's talk at Yale, part 2](https://news.ycombinator.com/item?id=85843) | 分享 Joel Spolsky 在耶鲁大学的演讲下半部分。 | 54 | 18 | 2007-12-04 |
| 13 | [Paul Buchheit: Is there more to life than money?](https://news.ycombinator.com/item?id=87558) | Paul Buchheit 追问人生是否还有金钱之外的追求。 | 54 | 54 | 2007-12-10 |
| 14 | [Start-Up sells solar panels that are cheaper than coal power](https://news.ycombinator.com/item?id=91106) | 报道称一家创业公司销售的太阳能板发电比煤电便宜。 | 53 | 22 | 2007-12-19 |
| 15 | [Please Don't Steal My Focus](https://news.ycombinator.com/item?id=86329) | 呼吁软件界面避免擅自抢夺用户的输入焦点。 | 51 | 13 | 2007-12-05 |
| 16 | [The world's most toxic value system](https://news.ycombinator.com/item?id=92792) | 作者批评一种被其视为极具毒性的价值体系。 | 51 | 76 | 2007-12-26 |
| 17 | [Embed charts in webpages with one of our simplest APIs yet](https://news.ycombinator.com/item?id=86680) | 介绍用简单 API 把图表嵌入网页的方法。 | 50 | 11 | 2007-12-06 |
| 18 | [Rails 2.0 Released](https://news.ycombinator.com/item?id=87016) | Ruby on Rails 2.0 正式发布。 | 50 | 14 | 2007-12-07 |
| 19 | ["The Most Complex Piece of Engineering Known to Man"](https://news.ycombinator.com/item?id=90065) | 聚焦被题名称为人类最复杂工程的对象。 | 48 | 21 | 2007-12-16 |
| 20 | [Something new for the New Year: SearchYC.com](https://news.ycombinator.com/item?id=93864) | SearchYC.com 作为新年项目上线。 | 48 | 22 | 2007-12-31 |

## 2008-01

有效主帖 3,294 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Arc's Out](https://news.ycombinator.com/item?id=106398) | Arc 编程语言正式发布。 | 240 | 124 | 2008-01-29 |
| 2 | [More advice for new Y Combinator founders](https://news.ycombinator.com/item?id=95857) | 为 YC 新创始人提供保持情绪稳定、专注产品及谨慎招聘的建议。 | 124 | 28 | 2008-01-08 |
| 3 | [PG: Arc Likely To Be Open-Sourced This Winter](https://news.ycombinator.com/item?id=98360) | Paul Graham 表示 Arc 很可能在当年冬天开源。 | 118 | 88 | 2008-01-14 |
| 4 | [Interview with Paul Graham at Imperial College London ](https://news.ycombinator.com/item?id=94580) | 分享 Paul Graham 在伦敦帝国理工学院的访谈。 | 89 | 31 | 2008-01-03 |
| 5 | [Absolutely Unbelievable: Richard Stallman Crankin' Dat Soulja Boy in front of the Green Building at MIT [video]](https://news.ycombinator.com/item?id=99632) | 视频展示 Richard Stallman 在麻省理工跳 Soulja Boy 舞。 | 82 | 41 | 2008-01-17 |
| 6 | [Two AI Pioneers. Two Bizarre Suicides. What Really Happened?](https://news.ycombinator.com/item?id=100838) | 追问两位人工智能先驱离奇自杀事件的真相。 | 82 | 53 | 2008-01-19 |
| 7 | [Every time you search for a domain on Network Solutions, they register it themselves.](https://news.ycombinator.com/item?id=96246) | 帖子指称 Network Solutions 会抢先注册用户查询的域名。 | 71 | 42 | 2008-01-09 |
| 8 | [Surprisingly useful new page: Web Developer's Field Guide](https://news.ycombinator.com/item?id=104246) | 介绍名为 Web Developer's Field Guide 的开发资源页面。 | 71 | 16 | 2008-01-25 |
| 9 | [Anywhere.FM acquired by imeem](https://news.ycombinator.com/item?id=105557) | 在线音乐服务 Anywhere.FM 宣布被 imeem 收购。 | 70 | 27 | 2008-01-28 |
| 10 | [Reddit Adds Ability to Create your own Reddits](https://news.ycombinator.com/item?id=102452) | Reddit 新增让用户自行创建社区的功能。 | 67 | 29 | 2008-01-22 |
| 11 | [UNIX tips: Learn 10 good UNIX usage habits](https://news.ycombinator.com/item?id=103725) | 分享十个值得培养的 UNIX 使用习惯。 | 64 | 17 | 2008-01-24 |
| 12 | [Five whys](https://news.ycombinator.com/item?id=102315) | 介绍通过连续追问“五个为什么”寻找深层原因的方法。 | 63 | 21 | 2008-01-22 |
| 13 | [A bot that allows you to say only original content](https://news.ycombinator.com/item?id=98158) | 介绍一个要求用户只能发布原创内容的机器人。 | 58 | 14 | 2008-01-14 |
| 14 | ['Excuse Me. May I Have Your Seat?'](https://news.ycombinator.com/item?id=94568) | 围绕向他人请求让座的情境展开观察。 | 57 | 8 | 2008-01-03 |
| 15 | [Aguri: Coolest Data Structure You've Never Heard Of](https://news.ycombinator.com/item?id=101969) | 介绍较少为人所知的数据结构 Aguri。 | 57 | 39 | 2008-01-22 |
| 16 | [Sun Buys MySQL](https://news.ycombinator.com/item?id=99206) | Sun 宣布收购 MySQL。 | 55 | 44 | 2008-01-16 |
| 17 | [Bram Cohen on great programmers](https://news.ycombinator.com/item?id=100531) | Bram Cohen 分享对优秀程序员的看法。 | 55 | 7 | 2008-01-18 |
| 18 | [Interview with a Hedge Fund Manager: "I'm sure today I would never get hired."](https://news.ycombinator.com/item?id=101106) | 一位对冲基金经理在访谈中感叹自己如今可能无法获聘。 | 55 | 21 | 2008-01-20 |
| 19 | [How to Write Stories (and lose weight, clean up the environment, and make a million dollars)](https://news.ycombinator.com/item?id=99831) | 以写故事为起点，串联减重、环保与赚钱的话题。 | 54 | 10 | 2008-01-17 |
| 20 | [xkcd endorses Obama](https://news.ycombinator.com/item?id=105739) | xkcd 作者公开支持奥巴马。 | 53 | 59 | 2008-01-28 |

## 2008-02

有效主帖 4,081 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Paul Graham: Six Principles for Making New Things](https://news.ycombinator.com/item?id=116768) | Paul Graham 提出创造新事物的六条原则。 | 173 | 118 | 2008-02-16 |
| 2 | [Genius hack by PhD candidate (with source code): Turn any monitor into a 3D display using a Wiimote](https://news.ycombinator.com/item?id=121053) | 一名博士生用 Wiimote 将普通显示器变成三维显示装置。 | 142 | 26 | 2008-02-22 |
| 3 | [PG on trolls](https://news.ycombinator.com/item?id=117118) | Paul Graham 谈网络中蓄意挑衅的用户。 | 137 | 183 | 2008-02-16 |
| 4 | [News.YC open-sourced](https://news.ycombinator.com/item?id=122829) | YC 新闻的源代码正式公开。 | 127 | 20 | 2008-02-25 |
| 5 | [Smjörið er brætt og hveitið smátt og smátt hrært út í það, þangað til það er gengið upp í smjörið.](https://news.ycombinator.com/item?id=111100) | 用冰岛语内容验证 Patrick Collison 修复后的 UTF-8 支持。 | 125 | 154 | 2008-02-07 |
| 6 | [Learning Math](https://news.ycombinator.com/item?id=108723) | 一位三十多岁读者征求从基础建立数学直觉的学习资源。 | 122 | 74 | 2008-02-03 |
| 7 | [Joel: How Hard Could It Be?: Lessons I Learned in the Army](https://news.ycombinator.com/item?id=125572) | Joel Spolsky 分享军旅经历带来的经验教训。 | 95 | 23 | 2008-02-28 |
| 8 | [The most important thing to understand about new products and startups](https://news.ycombinator.com/item?id=117533) | 讨论理解新产品与创业公司时最应把握的事情。 | 92 | 26 | 2008-02-17 |
| 9 | [The importance of launching early and staying alive](https://news.ycombinator.com/item?id=123754) | 强调尽早发布产品并让公司活下去的重要性。 | 92 | 29 | 2008-02-26 |
| 10 | [Don't Become a Scientist.](https://news.ycombinator.com/item?id=122106) | 作者提出不应成为科学家的劝告。 | 83 | 91 | 2008-02-23 |
| 11 | [Microsoft bids $44.6 billion for Yahoo](https://news.ycombinator.com/item?id=107771) | 微软向雅虎提出约 446 亿美元的收购报价。 | 82 | 80 | 2008-02-01 |
| 12 | [Git is the next Unix](https://news.ycombinator.com/item?id=108172) | 以“下一个 Unix”为比喻评价 Git 的潜力。 | 79 | 19 | 2008-02-02 |
| 13 | [How do you learn?](https://news.ycombinator.com/item?id=109802) | 邀请程序员交流各自最有效的自学方法。 | 79 | 54 | 2008-02-05 |
| 14 | [Ask News.YC: How to re-motivate yourself?](https://news.ycombinator.com/item?id=121175) | 创业近一年的发帖者寻求重新找回动力的方法。 | 75 | 42 | 2008-02-22 |
| 15 | [How I lost my faith (in Lisp)](https://news.ycombinator.com/item?id=107683) | 作者讲述自己如何失去对 Lisp 的信心。 | 72 | 97 | 2008-02-01 |
| 16 | [This Psychologist Might Outsmart the Math Brains Competing for the Netflix Prize](https://news.ycombinator.com/item?id=125401) | 介绍一位试图在 Netflix 算法竞赛中挑战数学高手的心理学家。 | 70 | 24 | 2008-02-28 |
| 17 | [So You Hacked Our Site!?](https://news.ycombinator.com/item?id=126162) | 围绕网站被入侵后的反应展开讨论。 | 70 | 22 | 2008-02-29 |
| 18 | [Arc Ported to JavaScript](https://news.ycombinator.com/item?id=110625) | Arc 被移植到 JavaScript。 | 69 | 23 | 2008-02-07 |
| 19 | [Do it Fucking Now.](https://news.ycombinator.com/item?id=121534) | 用直白强烈的语言催促读者立即采取行动。 | 68 | 30 | 2008-02-22 |
| 20 | [Why a School Banned Legos](https://news.ycombinator.com/item?id=119760) | 追问一所学校禁止乐高积木的原因。 | 64 | 90 | 2008-02-20 |

## 2008-03

有效主帖 4,969 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [You weren't meant to have a boss](https://news.ycombinator.com/item?id=141898) | 作者提出人不应受老板支配的观点。 | 239 | 298 | 2008-03-20 |
| 2 | [New Video of BigDog Quadruped Robot Is So Stunning It's Spooky](https://news.ycombinator.com/item?id=138966) | 展示四足机器人 BigDog 令人惊叹的新视频。 | 192 | 91 | 2008-03-17 |
| 3 | [How to Disagree](https://news.ycombinator.com/item?id=149052) | 分析如何提出有质量的不同意见。 | 183 | 224 | 2008-03-29 |
| 4 | [Hacker News Site Guidelines](https://news.ycombinator.com/item?id=133453) | 公布 Hacker News 社区的参与准则。 | 177 | 35 | 2008-03-10 |
| 5 | [Codepad.org, a pastebin that executes code](https://news.ycombinator.com/item?id=129207) | 介绍可直接执行粘贴代码的分享网站 Codepad.org。 | 143 | 57 | 2008-03-04 |
| 6 | [Why Not To Do A Startup](https://news.ycombinator.com/item?id=140602) | 列出不选择创业的理由，供潜在创业者思考。 | 136 | 83 | 2008-03-19 |
| 7 | [Dropbox launches (YC summer 07)](https://news.ycombinator.com/item?id=134405) | YC 2007 年夏季项目 Dropbox 正式推出。 | 133 | 65 | 2008-03-11 |
| 8 | [Workplace Experiments at 37signals](https://news.ycombinator.com/item?id=129463) | 介绍 37signals 在工作安排方面进行的实验。 | 128 | 46 | 2008-03-05 |
| 9 | [The mortgage crisis, in cartoon form (has cursing, maybe NSFW?)](https://news.ycombinator.com/item?id=140044) | 用漫画形式解释住房抵押贷款危机。 | 127 | 25 | 2008-03-18 |
| 10 | [Coding Horror: Paul Graham's Participatory Narcissism](https://news.ycombinator.com/item?id=143148) | Coding Horror 批评 Paul Graham 的“参与式自恋”。 | 121 | 130 | 2008-03-22 |
| 11 | [How to Lay Off Your Developers the Right Way ](https://news.ycombinator.com/item?id=148112) | 讨论裁减开发人员时应如何妥善处理。 | 118 | 21 | 2008-03-27 |
| 12 | [Paul Buchheit: Ideas vs Judgment and Execution: Climbing the Mountain](https://news.ycombinator.com/item?id=150694) | Paul Buchheit 用登山比喻思考创意、判断力与执行力。 | 114 | 42 | 2008-03-31 |
| 13 | [Sign Up Forms Must Die](https://news.ycombinator.com/item?id=145622) | 作者呼吁淘汰妨碍体验的注册表单。 | 113 | 34 | 2008-03-25 |
| 14 | [A New Venture Animal](https://news.ycombinator.com/item?id=133430) | 以“新的创投物种”为题，观察创业投资领域的变化。 | 106 | 58 | 2008-03-10 |
| 15 | [Would this community prefer to be under the radar?](https://news.ycombinator.com/item?id=146604) | 发帖者询问 TechCrunch 的曝光是否会伤害 HN 社区。 | 103 | 91 | 2008-03-26 |
| 16 | [Little Known Hacker News Is My First Read Every Morning](https://news.ycombinator.com/item?id=133440) | 作者分享每天早晨首先阅读 Hacker News 的习惯。 | 96 | 81 | 2008-03-10 |
| 17 | [Amazon EC2 gets static IPs.](https://news.ycombinator.com/item?id=147665) | Amazon EC2 增加静态 IP 地址功能。 | 96 | 33 | 2008-03-27 |
| 18 | [Disagreeing with Paul Graham](https://news.ycombinator.com/item?id=151109) | 作者针对 Paul Graham 的观点提出不同意见。 | 96 | 73 | 2008-03-31 |
| 19 | [Communicate Acquires Y Combinator Startup Auctomatic, Unveils New Business Strategy](https://news.ycombinator.com/item?id=146774) | Communicate 收购 YC 项目 Auctomatic 并公布新业务战略。 | 91 | 39 | 2008-03-26 |
| 20 | [Get that job at Google](https://news.ycombinator.com/item?id=135666) | 分享如何争取获得 Google 工作机会的建议。 | 90 | 74 | 2008-03-13 |

## 2008-04

有效主帖 5,150 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Be Good](https://news.ycombinator.com/item?id=168636) | 围绕“做好事”这一原则展开思考。 | 182 | 202 | 2008-04-20 |
| 2 | [Want to Remember Everything You'll Ever Learn? Surrender to This Algorithm](https://news.ycombinator.com/item?id=170542) | 介绍借助记忆算法长期保存所学知识的思路。 | 172 | 61 | 2008-04-22 |
| 3 | [Gin, Television, and Social Surplus](https://news.ycombinator.com/item?id=174410) | 从杜松子酒与电视谈社会可支配精力的变化。 | 153 | 55 | 2008-04-26 |
| 4 | [Why There Aren't More Googles](https://news.ycombinator.com/item?id=163552) | 追问为何没有更多像 Google 这样的公司出现。 | 152 | 154 | 2008-04-14 |
| 5 | [Google Jumps Head First Into Web Services With Google App Engine](https://news.ycombinator.com/item?id=157443) | Google 发布面向 Web 应用的云服务 App Engine。 | 139 | 113 | 2008-04-08 |
| 6 | [Pmarca: If Microsoft goes fully hostile on Yahoo](https://news.ycombinator.com/item?id=175477) | Marc Andreessen 分析微软若对雅虎发动全面敌意收购的局面。 | 134 | 27 | 2008-04-28 |
| 7 | [Solo founders: how do you stay emotionally efficient?](https://news.ycombinator.com/item?id=166905) | 独立创始人征求保持情绪与心理状态稳定的方法。 | 119 | 96 | 2008-04-18 |
| 8 | [Some Heroes](https://news.ycombinator.com/item?id=155400) | 以“一些英雄”为题关注值得敬佩的人物。 | 116 | 91 | 2008-04-05 |
| 9 | [DHH: Are you sure you want to be in San Francisco?](https://news.ycombinator.com/item?id=170719) | DHH 质疑创业者是否一定需要在旧金山发展。 | 108 | 108 | 2008-04-22 |
| 10 | [Fleaflicker (solo founder) Acquired by AOL](https://news.ycombinator.com/item?id=173588) | 独立创始人打造的 Fleaflicker 被 AOL 收购。 | 97 | 55 | 2008-04-25 |
| 11 | [Facebook Is Not Really That Special](https://news.ycombinator.com/item?id=160408) | 作者质疑 Facebook 是否真有那么特殊。 | 95 | 119 | 2008-04-10 |
| 12 | [Hire Family People](https://news.ycombinator.com/item?id=172915) | 作者主张在招聘时考虑有家庭的员工。 | 95 | 152 | 2008-04-24 |
| 13 | [The Great Ubuntu-Girlfriend Experiment](https://news.ycombinator.com/item?id=175604) | 记录让女友试用 Ubuntu 的实验。 | 95 | 82 | 2008-04-28 |
| 14 | [Would you have answered this job ad?](https://news.ycombinator.com/item?id=176674) | 邀请读者判断自己是否会回应一则招聘广告。 | 93 | 55 | 2008-04-29 |
| 15 | [The boring truth about why groups don't get invited to interviews](https://news.ycombinator.com/item?id=160021) | 解释某些创业团队没有获得面试邀请的原因。 | 89 | 48 | 2008-04-10 |
| 16 | [The Thing About Git](https://news.ycombinator.com/item?id=158008) | 分享对 Git 特点与使用的看法。 | 86 | 31 | 2008-04-08 |
| 17 | [SICP - summary of 10 months working through the entire book](https://news.ycombinator.com/item?id=167335) | 总结花十个月完整学习《SICP》的经历。 | 86 | 39 | 2008-04-18 |
| 18 | [Programmer Destroys Seven Billion Dollar Industry With A Single Software Application](https://news.ycombinator.com/item?id=155601) | 标题以夸张口吻描述一个软件对七十亿美元行业的冲击。 | 82 | 39 | 2008-04-05 |
| 19 | [Storage Space, The Final Frontier: Amazon EC2 adds persistent disks](https://news.ycombinator.com/item?id=162851) | Amazon EC2 新增持久化磁盘存储。 | 82 | 16 | 2008-04-14 |
| 20 | [Lessons of Y Combinator: Things I’d do differently after 2 startups](https://news.ycombinator.com/item?id=152936) | 经历两次创业后，作者总结哪些事情会采取不同做法。 | 81 | 32 | 2008-04-02 |

## 2008-05

有效主帖 5,409 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Startups Wiki: Ask YC Archive](https://news.ycombinator.com/item?id=184766) | Startups Wiki 整理 YC 问答帖的历史档案。 | 198 | 25 | 2008-05-08 |
| 2 | [Lies We Tell Kids](https://news.ycombinator.com/item?id=188489) | 反思成年人对孩子讲述的谎言。 | 188 | 418 | 2008-05-13 |
| 3 | [Cities and Ambition](https://news.ycombinator.com/item?id=201373) | 探讨城市环境如何塑造个人的抱负。 | 156 | 306 | 2008-05-27 |
| 4 | [PG: Disconnecting Distraction](https://news.ycombinator.com/item?id=192654) | Paul Graham 谈如何切断干扰、保持专注。 | 153 | 198 | 2008-05-17 |
| 5 | [Why Zappos Pays New Employees to Quit—And You Should Too](https://news.ycombinator.com/item?id=194708) | 解释 Zappos 为何付钱让新员工离职，并建议其他公司借鉴。 | 137 | 37 | 2008-05-20 |
| 6 | [Tell YC: Answers from John McCarthy](https://news.ycombinator.com/item?id=185348) | 一位学生整理 John McCarthy 在斯坦福课堂访谈中的回答。 | 136 | 72 | 2008-05-09 |
| 7 | [My experiment with smart drugs: Viagra for the brain?](https://news.ycombinator.com/item?id=190676) | 作者分享尝试所谓“聪明药”的个人经历。 | 134 | 114 | 2008-05-15 |
| 8 | [Sleep deprivation is not a badge of honor](https://news.ycombinator.com/item?id=178655) | 提醒读者不应把睡眠不足当作荣誉。 | 133 | 43 | 2008-05-01 |
| 9 | [Architecture astronauts take over](https://news.ycombinator.com/item?id=178010) | 批评脱离实际、沉迷宏大架构的设计思路。 | 131 | 75 | 2008-05-01 |
| 10 | [Ask YC: Startup crisis. Out of money and tech co-founder has bailed.](https://news.ycombinator.com/item?id=183535) | 一位非技术创始人在资金耗尽、技术合伙人退出后求助。 | 129 | 232 | 2008-05-07 |
| 11 | [When did we forget our dreams?](https://news.ycombinator.com/item?id=197024) | 追问人们何时开始忘记自己的梦想。 | 123 | 49 | 2008-05-22 |
| 12 | [Ask YC: Feedback on early version of my startup, a digital whiteboard that doesn't suck](https://news.ycombinator.com/item?id=202798) | 开发者为数字白板创业项目的早期版本征求反馈。 | 122 | 129 | 2008-05-29 |
| 13 | [Processing ported to JavaScript](https://news.ycombinator.com/item?id=185191) | Processing 被移植到 JavaScript。 | 112 | 28 | 2008-05-09 |
| 14 | [Google releases free, detailed, HTML/CSS/Javascript encyclopedia by Mark Pilgrim](https://news.ycombinator.com/item?id=189992) | Google 发布 Mark Pilgrim 编写的免费 Web 技术资料。 | 111 | 23 | 2008-05-14 |
| 15 | [The Coolest Business Plan Ever](https://news.ycombinator.com/item?id=182719) | 介绍一个被作者称为极酷的商业计划。 | 104 | 11 | 2008-05-06 |
| 16 | [Ask YC: Have you built a good website that nobody visits?](https://news.ycombinator.com/item?id=187977) | 邀请读者分享产品不错却无人访问的网站项目。 | 103 | 120 | 2008-05-12 |
| 17 | [Michael Arrington: “I’m a Click-Whoring Jackass”](https://news.ycombinator.com/item?id=203839) | Michael Arrington 以尖锐的自嘲回应争议。 | 103 | 36 | 2008-05-29 |
| 18 | [Scaling Facebook Chat to 70 Million Active Users Almost Overnight ](https://news.ycombinator.com/item?id=190215) | 介绍 Facebook Chat 如何迅速扩展到七千万活跃用户。 | 93 | 42 | 2008-05-15 |
| 19 | [You Can't Soak the Rich](https://news.ycombinator.com/item?id=195085) | 作者质疑通过向富人征税解决问题的思路。 | 91 | 109 | 2008-05-20 |
| 20 | [Essential Python Tips, Tricks, and Hacks](https://news.ycombinator.com/item?id=196597) | 整理 Python 开发中的实用技巧与窍门。 | 90 | 25 | 2008-05-21 |

## 2008-06

有效主帖 5,438 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Congrats to PG on getting hitched](https://news.ycombinator.com/item?id=205918) | 社区祝贺 Paul Graham 结婚。 | 228 | 95 | 2008-06-01 |
| 2 | [Diary of a Failed Startup](https://news.ycombinator.com/item?id=225209) | 通过日记回顾一家创业公司的失败经历。 | 224 | 34 | 2008-06-23 |
| 3 | [Reddit goes open source - the actual announcement from reddit. ](https://news.ycombinator.com/item?id=220733) | Reddit 正式宣布开放源代码。 | 168 | 66 | 2008-06-18 |
| 4 | [Done, and Gets Things Smart](https://news.ycombinator.com/item?id=219425) | 以“完成事情并让事情变聪明”为题思考做事能力。 | 137 | 65 | 2008-06-17 |
| 5 | [The Disadvantages of an Elite Education](https://news.ycombinator.com/item?id=224861) | 审视精英教育可能带来的局限。 | 131 | 69 | 2008-06-23 |
| 6 | [How to sell your software for $20,000](https://news.ycombinator.com/item?id=230347) | 讨论如何让软件以两万美元的价格成交。 | 125 | 55 | 2008-06-27 |
| 7 | [Full text: An epic Bill Gates e-mail rant](https://news.ycombinator.com/item?id=227045) | 公开 Bill Gates 一封措辞激烈的长邮件全文。 | 116 | 89 | 2008-06-25 |
| 8 | [Robokill:  Superb new Flash game from News.YC members](https://news.ycombinator.com/item?id=218322) | 介绍 HN 成员制作的 Flash 游戏 Robokill。 | 115 | 82 | 2008-06-16 |
| 9 | [This is what your customers think of asking for their email password](https://news.ycombinator.com/item?id=209870) | 从客户角度审视索取其邮箱密码的做法。 | 111 | 59 | 2008-06-05 |
| 10 | [17 Mistakes Start-Ups Make by John Osher (inventor of Crest Spinbrush)](https://news.ycombinator.com/item?id=221750) | Spinbrush 发明人 John Osher 总结创业的十七种错误。 | 108 | 21 | 2008-06-19 |
| 11 | [Scaling Fast](https://news.ycombinator.com/item?id=209474) | 探讨业务或系统快速扩大规模的过程。 | 107 | 16 | 2008-06-04 |
| 12 | [I'm not sure who this Oleg person is, but he sure has some cool links on his site.](https://news.ycombinator.com/item?id=227605) | 推荐一位名叫 Oleg 的人整理的技术链接。 | 106 | 6 | 2008-06-25 |
| 13 | [How Hard Could it Be? Joel Spolsky recalls what it was like to work for Bill Gates](https://news.ycombinator.com/item?id=228298) | Joel Spolsky 回忆为 Bill Gates 工作的经历。 | 104 | 52 | 2008-06-26 |
| 14 | [Google: we're having scaling issues, please stop distributing your FF extension](https://news.ycombinator.com/item?id=229243) | Google 因扩展规模问题要求暂停分发某款 Firefox 扩展。 | 99 | 19 | 2008-06-26 |
| 15 | [Reddit's Ranking Algorithm](https://news.ycombinator.com/item?id=231168) | 介绍 Reddit 对内容进行排序的算法。 | 97 | 34 | 2008-06-29 |
| 16 | [The richer a society or peer group, the less important visible spending becomes.](https://news.ycombinator.com/item?id=219804) | 提出社会或同伴群体越富裕，炫耀性消费越不重要的观点。 | 93 | 57 | 2008-06-17 |
| 17 | [Goosh - The Unofficial Google Shell](https://news.ycombinator.com/item?id=206683) | 介绍提供类 UNIX 命令行体验的 Google 服务入口 Goosh。 | 91 | 35 | 2008-06-02 |
| 18 | [Would you work with micromanaging boss, no salary, and all your work thrown away?](https://news.ycombinator.com/item?id=222157) | 以苛刻工作条件设问，反思人们为何愿意投入某类工作。 | 91 | 54 | 2008-06-19 |
| 19 | [Things I've learned from running a business (ie: Don't do what I did)](https://news.ycombinator.com/item?id=221171) | 作者分享经营企业时犯过的错误和得到的教训。 | 89 | 15 | 2008-06-18 |
| 20 | [Code_swarm. An experiment in organic software visualization.](https://news.ycombinator.com/item?id=216872) | Code_swarm 尝试用动态视觉呈现软件开发活动。 | 86 | 19 | 2008-06-13 |

## 2008-07

有效主帖 5,797 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Startup Ideas We'd Like to Fund](https://news.ycombinator.com/item?id=250704) | 列出作者希望投资的创业点子与方向。 | 532 | 381 | 2008-07-19 |
| 2 | [Randy Pausch, noted CMU prof, succumbs to cancer](https://news.ycombinator.com/item?id=256623) | 卡内基梅隆教授 Randy Pausch 因癌症去世。 | 187 | 57 | 2008-07-25 |
| 3 | [In the Basement of the Ivory Tower](https://news.ycombinator.com/item?id=246606) | 从象牙塔底层视角观察高等教育。 | 170 | 127 | 2008-07-15 |
| 4 | [Google Acquires Omnisio (YC Winter 08)](https://news.ycombinator.com/item?id=262240) | Google 收购 YC 2008 年冬季项目 Omnisio。 | 168 | 45 | 2008-07-30 |
| 5 | [Why S3 went down](https://news.ycombinator.com/item?id=257279) | 解释 Amazon S3 服务发生故障的原因。 | 144 | 36 | 2008-07-26 |
| 6 | [JL: Why I Do YC](https://news.ycombinator.com/item?id=237357) | Jessica Livingston 分享自己参与 YC 的理由。 | 130 | 42 | 2008-07-05 |
| 7 | [You don't have to sell your company to have financial security](https://news.ycombinator.com/item?id=255716) | 提出创业者无需出售公司也可获得财务安全。 | 129 | 89 | 2008-07-24 |
| 8 | [A Brief History of Dangerous Ideas](https://news.ycombinator.com/item?id=253301) | 梳理曾被视为危险的思想如何出现与发展。 | 123 | 32 | 2008-07-22 |
| 9 | [YC is a cult](https://news.ycombinator.com/item?id=260017) | 以“邪教”为比喻评价 Y Combinator 的组织氛围。 | 116 | 154 | 2008-07-29 |
| 10 | [Why are Black Nerds so Unpopular? ](https://news.ycombinator.com/item?id=237955) | 追问黑人技术爱好者为何面临不受欢迎的处境。 | 109 | 65 | 2008-07-06 |
| 11 | [The Pooled-Risk Company Management Company](https://news.ycombinator.com/item?id=254335) | 提出通过公司管理机构共同分担风险的构想。 | 107 | 83 | 2008-07-23 |
| 12 | [Profitable After 3 Weeks](https://news.ycombinator.com/item?id=247720) | 分享一个项目在启动三周后实现盈利的经历。 | 100 | 46 | 2008-07-16 |
| 13 | [Donate to help a MySQler](https://news.ycombinator.com/item?id=249120) | 发起捐助，帮助一位 MySQL 社群成员。 | 96 | 62 | 2008-07-17 |
| 14 | [Play this game for 20 minutes - learn about concurrency](https://news.ycombinator.com/item?id=244594) | 推荐通过二十分钟游戏理解并发概念。 | 94 | 31 | 2008-07-12 |
| 15 | [10 Incredibly Awesome Documents to Help You Start a Company](https://news.ycombinator.com/item?id=243087) | 整理有助于创办公司的十份实用文档。 | 93 | 8 | 2008-07-11 |
| 16 | [GitHub on applying Getting Real to their unfunded startup](https://news.ycombinator.com/item?id=259495) | GitHub 分享如何在未融资创业中实践《Getting Real》。 | 93 | 7 | 2008-07-28 |
| 17 | [Why you should never be a startup girlfriend](https://news.ycombinator.com/item?id=244906) | 作者提醒读者了解与创业程序员恋爱可能面对的现实。 | 92 | 70 | 2008-07-13 |
| 18 | [Pets.com CEO: The Five Big Mistakes That Changed My Life and How I Moved Past Them](https://news.ycombinator.com/item?id=263443) | Pets.com 前 CEO 回顾改变人生的五次重大错误。 | 90 | 34 | 2008-07-31 |
| 19 | [Xkcd - Linux, a cautionary tale](https://news.ycombinator.com/item?id=261598) | 分享 xkcd 围绕 Linux 创作的警示漫画。 | 89 | 62 | 2008-07-30 |
| 20 | [Inside Chernobyl, a strange new lifeform is blooming](https://news.ycombinator.com/item?id=257454) | 作者以“如何招到笨蛋”为题反思招聘。 | 87 | 23 | 2008-07-26 |

## 2008-08

有效主帖 5,227 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [How to hire an idiot (from the 'How to sell your software for $20,000' guy)](https://news.ycombinator.com/item?id=263599) | 作者以“如何招到笨蛋”为题反思招聘。 | 220 | 42 | 2008-08-01 |
| 2 | [Start a side project, says GitHub founder](https://news.ycombinator.com/item?id=282158) | GitHub 创始人建议启动一个业余项目。 | 210 | 40 | 2008-08-20 |
| 3 | [Y Combinator To Offer Standardized Angel Funding Legal Docs](https://news.ycombinator.com/item?id=275328) | Y Combinator 将提供标准化天使投资法律文件。 | 156 | 45 | 2008-08-13 |
| 4 | [Aaron Swartz: How To Launch Software](https://news.ycombinator.com/item?id=283908) | Aaron Swartz 分享发布软件的方法。 | 148 | 48 | 2008-08-22 |
| 5 | [A Fundraising Survival Guide](https://news.ycombinator.com/item?id=270809) | 为创业者提供融资过程中的生存建议。 | 145 | 94 | 2008-08-08 |
| 6 | [The Tech (MIT student newspaper) publishes the banned DEFCON slides](https://news.ycombinator.com/item?id=271920) | 麻省理工学生报刊登遭禁止公开的 DEFCON 演讲幻灯片。 | 144 | 60 | 2008-08-09 |
| 7 | [Calvin and Jobs (comic)](https://news.ycombinator.com/item?id=265138) | 分享将 Calvin 与 Steve Jobs 联系起来的漫画。 | 132 | 28 | 2008-08-02 |
| 8 | [Series AA Documents Back Online](https://news.ycombinator.com/item?id=283067) | Series AA 融资文件重新上线。 | 130 | 23 | 2008-08-21 |
| 9 | [Business Requirements are Bullshit](https://news.ycombinator.com/item?id=273887) | 作者以强烈措辞质疑“业务需求”的表达方式。 | 116 | 84 | 2008-08-12 |
| 10 | [The secret of the web (hint: it's a virtue)](https://news.ycombinator.com/item?id=272314) | 以一种美德为线索解释 Web 的成功秘诀。 | 114 | 37 | 2008-08-10 |
| 11 | [For Most People, College Is a Waste of Time](https://news.ycombinator.com/item?id=275258) | 作者提出大学教育对大多数人而言浪费时间的观点。 | 113 | 139 | 2008-08-13 |
| 12 | [What I Learned Buying a Rug in Turkey](https://news.ycombinator.com/item?id=270145) | 作者分享在土耳其购买地毯时得到的启示。 | 110 | 64 | 2008-08-08 |
| 13 | [Indie game designer spent three years and $180,000 making a masterpiece](https://news.ycombinator.com/item?id=284417) | 报道独立游戏作者投入三年和十八万美元完成作品。 | 110 | 18 | 2008-08-23 |
| 14 | [The Google black hole: What happens to startups when they're bought by Google?](https://news.ycombinator.com/item?id=276041) | 追问创业公司被 Google 收购后会经历什么。 | 103 | 55 | 2008-08-14 |
| 15 | [Why the lucky stiff: when you don't create things...](https://news.ycombinator.com/item?id=271044) | _why 谈不再创造事物时人的状态。 | 97 | 60 | 2008-08-08 |
| 16 | [Do you know any programmers who exhibit these personality traits?](https://news.ycombinator.com/item?id=286300) | 邀请读者判断身边程序员是否具有某些人格特征。 | 95 | 67 | 2008-08-25 |
| 17 | [One Inviolable Rule](https://news.ycombinator.com/item?id=287851) | 提出一条被作者视为不可违背的规则。 | 94 | 105 | 2008-08-27 |
| 18 | [Colorful programs for Mac OS X, Linux and Windows](https://news.ycombinator.com/item?id=276556) | 介绍可在 macOS、Linux 和 Windows 上运行的彩色程序。 | 91 | 22 | 2008-08-14 |
| 19 | [JParallax - Javascript parallax effect](https://news.ycombinator.com/item?id=288894) | 介绍实现 JavaScript 视差效果的 JParallax。 | 91 | 20 | 2008-08-28 |
| 20 | [Part-time apps developers getting rich](https://news.ycombinator.com/item?id=264191) | 关注通过兼职开发应用获得可观收入的开发者。 | 90 | 50 | 2008-08-01 |

## 2008-09

有效主帖 5,322 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Golden Rules for Making Money by P. T. Barnum (1880)](https://news.ycombinator.com/item?id=310056) | 分享 P. T. Barnum 于 1880 年提出的赚钱准则。 | 227 | 56 | 2008-09-20 |
| 2 | [Ask YC: What do you think of my new search engine?](https://news.ycombinator.com/item?id=315142) | 开发者邀请 YC 社区评价自己的新搜索引擎。 | 186 | 138 | 2008-09-25 |
| 3 | [Google Chrome, Google's Browser Project](https://news.ycombinator.com/item?id=291946) | Google 公布浏览器项目 Chrome。 | 173 | 108 | 2008-09-01 |
| 4 | [I'm out, baby](https://news.ycombinator.com/item?id=300960) | 一位社区成员存够一万五千美元后辞职，准备全职创业。 | 164 | 99 | 2008-09-11 |
| 5 | [The Google Chrome download link is live.](https://news.ycombinator.com/item?id=292980) | Google Chrome 的下载链接正式开放。 | 153 | 177 | 2008-09-02 |
| 6 | [Dropbox finally launches to the public (YC summer 07)](https://news.ycombinator.com/item?id=301605) | Dropbox 正式向公众开放使用。 | 144 | 80 | 2008-09-11 |
| 7 | [Shoestring Budget?  Starting to feel growth issues on your back-end?  Embrace unix and C](https://news.ycombinator.com/item?id=299451) | 一支预算有限的搜索创业团队分享借助 UNIX 和 C 应对增长。 | 140 | 120 | 2008-09-09 |
| 8 | [Bankruptcy, not bailout, is the right answer](https://news.ycombinator.com/item?id=319582) | 作者主张通过破产而非政府救助处理危机。 | 139 | 84 | 2008-09-30 |
| 9 | [Outsourcing Cooking with Craigslist for $60/week](https://news.ycombinator.com/item?id=311835) | 分享通过 Craigslist 以每周六十美元外包做饭的做法。 | 135 | 73 | 2008-09-23 |
| 10 | [Django 1.0 is finally here](https://news.ycombinator.com/item?id=294364) | Django 1.0 正式发布。 | 132 | 20 | 2008-09-03 |
| 11 | [$700bn Bailout is shot down by House of Rep Vote (205-228), US stock market plummets](https://news.ycombinator.com/item?id=318595) | 美国众议院否决七千亿美元救助计划，股市随之大跌。 | 130 | 189 | 2008-09-29 |
| 12 | [A guy tries to find the origins of a Windows desktop image](https://news.ycombinator.com/item?id=291912) | 记录寻找一张 Windows 桌面壁纸拍摄来源的过程。 | 129 | 15 | 2008-09-01 |
| 13 | [How My Start-Up Failed](https://news.ycombinator.com/item?id=303780) | 作者复盘自己的创业项目如何失败。 | 128 | 61 | 2008-09-14 |
| 14 | [The most thorough task execution I've ever seen (dude polishes car)](https://news.ycombinator.com/item?id=295560) | 通过一位细致抛光汽车的人展示彻底完成任务的态度。 | 127 | 37 | 2008-09-05 |
| 15 | [Obama is RESTful](https://news.ycombinator.com/item?id=298532) | 用 REST 架构的概念解读奥巴马。 | 127 | 48 | 2008-09-08 |
| 16 | [App Store: I'm out](https://news.ycombinator.com/item?id=303199) | 作者宣布退出 App Store。 | 123 | 78 | 2008-09-13 |
| 17 | [Making money twice](https://news.ycombinator.com/item?id=312429) | 围绕“赚两次钱”的想法探讨收入获取方式。 | 120 | 36 | 2008-09-23 |
| 18 | [How to get into the Hottest Restaurants in Town](https://news.ycombinator.com/item?id=318827) | 分享争取进入城中热门餐厅的方法。 | 117 | 41 | 2008-09-29 |
| 19 | [10,000 Mechanical Turkers work separately to draw a 100 dollar bill.](https://news.ycombinator.com/item?id=313451) | 让一万名 Mechanical Turk 参与者分别绘制百元钞票的一部分。 | 115 | 48 | 2008-09-24 |
| 20 | [The best description of the fed bailout](https://news.ycombinator.com/item?id=312807) | 推荐一份解释美联储救助行动的材料。 | 114 | 24 | 2008-09-23 |

## 2008-10

有效主帖 5,986 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Why to Start a Startup in a Bad Economy](https://news.ycombinator.com/item?id=334355) | 阐述经济低迷时期仍值得创业的理由。 | 254 | 195 | 2008-10-16 |
| 2 | [How I Turned Down $300,000 from Microsoft to go Full-Time on GitHub](https://news.ycombinator.com/item?id=338286) | 作者回顾拒绝微软三十万美元待遇、全职投入 GitHub 的决定。 | 224 | 68 | 2008-10-20 |
| 3 | [A programmer's view of the Universe, part 1: The fish](https://news.ycombinator.com/item?id=347162) | 从程序员视角观察宇宙，首篇以鱼为切入点。 | 177 | 66 | 2008-10-29 |
| 4 | [Don’t Mistake Ambition for Entitlement](https://news.ycombinator.com/item?id=342358) | 提醒读者区分雄心与理所当然的索取心态。 | 174 | 169 | 2008-10-24 |
| 5 | [Stefano’s Linotype: Why Programmers Suck at CSS Design (CSS Guide)](https://news.ycombinator.com/item?id=345782) | 为不擅长视觉设计的程序员提供 CSS 设计指南。 | 172 | 42 | 2008-10-27 |
| 6 | [Hedge Fund Manager: Goodbye and Good Luck](https://news.ycombinator.com/item?id=335815) | 一位对冲基金经理发表告别与祝福。 | 158 | 67 | 2008-10-17 |
| 7 | [Reflections of a YC Dropout](https://news.ycombinator.com/item?id=330470) | 作者回顾退出 Y Combinator 的经历。 | 155 | 161 | 2008-10-12 |
| 8 | [The genius of late bloomers - Gladwell](https://news.ycombinator.com/item?id=331446) | Gladwell 探讨大器晚成者的创造力。 | 150 | 40 | 2008-10-13 |
| 9 | [IPhone NDA officially dropped](https://news.ycombinator.com/item?id=320751) | 苹果正式取消 iPhone 相关保密协议。 | 145 | 52 | 2008-10-01 |
| 10 | [Looking Back on Selling Gravatar to Automattic](https://news.ycombinator.com/item?id=345531) | 作者回顾将 Gravatar 出售给 Automattic 的经历。 | 143 | 23 | 2008-10-27 |
| 11 | [Paul Krugman: How I work](https://news.ycombinator.com/item?id=331832) | Paul Krugman 分享自己的工作方式。 | 135 | 47 | 2008-10-14 |
| 12 | [Python 2.6 Released](https://news.ycombinator.com/item?id=321411) | Python 2.6 正式发布。 | 130 | 31 | 2008-10-02 |
| 13 | [The Universal Design Pattern](https://news.ycombinator.com/item?id=337746) | 探讨一种被称为“通用设计模式”的思路。 | 127 | 44 | 2008-10-20 |
| 14 | [A CEO's Sequoia Meeting Notes](https://news.ycombinator.com/item?id=327937) | 一位 CEO 分享参加红杉会议的笔记。 | 123 | 61 | 2008-10-09 |
| 15 | [Rackspace acquire Slicehost](https://news.ycombinator.com/item?id=340289) | Rackspace 收购 Slicehost。 | 121 | 54 | 2008-10-22 |
| 16 | [Follow Stanford’s iPhone Programming Class For Free](https://news.ycombinator.com/item?id=349391) | 斯坦福的 iPhone 编程课程提供免费学习资源。 | 120 | 23 | 2008-10-30 |
| 17 | [How to go down with style](https://news.ycombinator.com/item?id=330689) | 以一位 CEO 帮员工妥善离职的经历谈如何体面关闭公司。 | 117 | 32 | 2008-10-13 |
| 18 | [Sell Your Web App: Lessons I Learned From Selling DropSend](https://news.ycombinator.com/item?id=347381) | 作者总结出售 Web 应用 DropSend 的经验。 | 117 | 28 | 2008-10-29 |
| 19 | [Ask HN: What is the best way to promote your new fancy web application?](https://news.ycombinator.com/item?id=341138) | 准创业者征求推广新 Web 应用的有效方法。 | 113 | 25 | 2008-10-23 |
| 20 | [Whiner Jerkins All Hands Meeting Powerpoint Revealed](https://news.ycombinator.com/item?id=331077) | 公开以 Whiner Jerkins 为名的全员会议幻灯片。 | 111 | 49 | 2008-10-13 |

## 2008-11

有效主帖 5,387 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [“Single?” Lawn Signs Conquer the American Landscape](https://news.ycombinator.com/item?id=355819) | 观察写着“单身？”的草坪广告牌如何遍布美国。 | 228 | 26 | 2008-11-06 |
| 2 | [Tell HN: Vote.](https://news.ycombinator.com/item?id=352800) | 一位社区成员呼吁有资格的美国读者参加投票。 | 184 | 289 | 2008-11-04 |
| 3 | [The other half of "Artists Ship"](https://news.ycombinator.com/item?id=379460) | 重新审视“艺术家要交付作品”这句话的另一面。 | 182 | 125 | 2008-11-28 |
| 4 | [Let's End Adolescence](https://news.ycombinator.com/item?id=358256) | 作者提出结束青春期这一社会阶段的主张。 | 172 | 162 | 2008-11-09 |
| 5 | [Balsamiq hits $100,000 in revenue](https://news.ycombinator.com/item?id=364254) | Balsamiq 的收入达到十万美元。 | 168 | 72 | 2008-11-14 |
| 6 | [Solve the halting problem, $300-$1000](https://news.ycombinator.com/item?id=376238) | 一则悬赏三百至一千美元解决停机问题的帖子。 | 166 | 83 | 2008-11-25 |
| 7 | [Ask HN: Who's Hiring?](https://news.ycombinator.com/item?id=375410) | 经济衰退期间征集招聘信息，帮助失业人才找到工作。 | 163 | 208 | 2008-11-24 |
| 8 | [Let Detroit Go Bankrupt](https://news.ycombinator.com/item?id=369932) | 作者主张让底特律汽车企业走破产程序。 | 158 | 188 | 2008-11-19 |
| 9 | [How people really use the iPhone](https://news.ycombinator.com/item?id=358659) | 观察用户实际上如何使用 iPhone。 | 155 | 60 | 2008-11-10 |
| 10 | [My Public Apology](https://news.ycombinator.com/item?id=371638) | 一位用户为自己在 Justin.tv 讨论中的言论公开道歉。 | 151 | 108 | 2008-11-21 |
| 11 | [Tell Hacker News: Throwaway accounts](https://news.ycombinator.com/item?id=360128) | 用户举报疑似用多个临时账号互相刷票的行为。 | 149 | 58 | 2008-11-11 |
| 12 | [Amazon Moving To Frustration-Free Packaging](https://news.ycombinator.com/item?id=352201) | 亚马逊开始推广更易开启的商品包装。 | 147 | 46 | 2008-11-03 |
| 13 | [CNN/Fox Projection: Obama wins presidential election.](https://news.ycombinator.com/item?id=354165) | CNN 与 Fox 预测奥巴马赢得美国总统选举。 | 145 | 137 | 2008-11-05 |
| 14 | [The IT Contract from Hell](https://news.ycombinator.com/item?id=368138) | 讲述一份令人头疼的 IT 合同。 | 133 | 27 | 2008-11-18 |
| 15 | [How to be a Programmer: A Short, Comprehensive, and Personal Summary](https://news.ycombinator.com/item?id=370874) | 以简明而个人化的总结介绍如何成为程序员。 | 128 | 28 | 2008-11-20 |
| 16 | [The End of Wall Street's Boom](https://news.ycombinator.com/item?id=361817) | 审视华尔街繁荣时期的终结。 | 123 | 21 | 2008-11-12 |
| 17 | [Mr. Benioff, Tear Down That Wall ](https://news.ycombinator.com/item?id=353798) | 以拆墙的呼吁向 Salesforce 的 Benioff 提出意见。 | 119 | 17 | 2008-11-04 |
| 18 | [Is it going to rain?](https://news.ycombinator.com/item?id=378987) | 围绕“是否会下雨”这一直接的天气问题展开。 | 114 | 70 | 2008-11-27 |
| 19 | [The End of Wall Street (Liar's Poker author)](https://news.ycombinator.com/item?id=360412) | 《说谎者的扑克牌》作者审视华尔街时代的终结。 | 112 | 34 | 2008-11-11 |
| 20 | [The 'broken windows' theory of crime is tested and seems correct](https://news.ycombinator.com/item?id=373356) | 报道一项研究检验犯罪“破窗理论”并发现支持证据。 | 108 | 35 | 2008-11-23 |

## 2008-12

有效主帖 5,495 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Love, Internet Style](https://news.ycombinator.com/item?id=395330) | 关注互联网环境中的爱情与交往。 | 242 | 43 | 2008-12-12 |
| 2 | [Wow, check out this guy's comment](https://news.ycombinator.com/item?id=412785) | 作者分享一条让自己重新思考金钱与工作动力的博客评论。 | 233 | 101 | 2008-12-29 |
| 3 | [I don't want to work very hard](https://news.ycombinator.com/item?id=394609) | 一位热爱写代码的资深开发者坦言难以维持职场工作动力。 | 224 | 193 | 2008-12-11 |
| 4 | [So you want to be a consultant?](https://news.ycombinator.com/item?id=411994) | 讨论成为顾问之前需要考虑的现实问题。 | 193 | 26 | 2008-12-28 |
| 5 | [After Credentials](https://news.ycombinator.com/item?id=399863) | 探讨学历与资历证明之后的评价方式。 | 186 | 201 | 2008-12-16 |
| 6 | [The nicest math book I own](https://news.ycombinator.com/item?id=406885) | 作者推荐自己收藏的一本出色数学书。 | 175 | 56 | 2008-12-22 |
| 7 | [Profitable Until Deemed Illegal](https://news.ycombinator.com/item?id=395970) | 讲述一项原本盈利却被认定违法的业务。 | 174 | 130 | 2008-12-12 |
| 8 | [Freezing cold, no Internet, boring: it's a French web 2.0 conference](https://news.ycombinator.com/item?id=393629) | 批评一场寒冷、无网络且无趣的法国 Web 2.0 会议。 | 171 | 69 | 2008-12-10 |
| 9 | [The High-Res Society](https://news.ycombinator.com/item?id=384606) | 以“高分辨率社会”为题思考社会变化。 | 168 | 127 | 2008-12-03 |
| 10 | [Could VC be a Casualty of the Recession?](https://news.ycombinator.com/item?id=386493) | 追问风险投资是否会成为经济衰退的牺牲品。 | 160 | 139 | 2008-12-05 |
| 11 | [Ever wondered what the 'Free Public WiFi' networks you see everywhere are?](https://news.ycombinator.com/item?id=386183) | 解释随处可见的“Free Public WiFi”网络名称意味着什么。 | 155 | 34 | 2008-12-04 |
| 12 | [Rails and Merb Merge](https://news.ycombinator.com/item?id=408011) | Rails 与 Merb 宣布合并。 | 155 | 52 | 2008-12-23 |
| 13 | [Techniques To Improve Your User Interface Designs ](https://news.ycombinator.com/item?id=398913) | 分享改进用户界面设计的技巧。 | 153 | 44 | 2008-12-15 |
| 14 | [How do you generate passive income?](https://news.ycombinator.com/item?id=387789) | 征求通过网络、房地产或投资获得被动收入的经验。 | 151 | 146 | 2008-12-06 |
| 15 | [Python 3.0 Released](https://news.ycombinator.com/item?id=385182) | Python 3.0 正式发布。 | 147 | 60 | 2008-12-04 |
| 16 | [Dear Reddit, Hacker News...](https://news.ycombinator.com/item?id=409659) | 一封写给 Reddit 与 Hacker News 社区的公开文字。 | 133 | 82 | 2008-12-25 |
| 17 | [If programming languages were religions](https://news.ycombinator.com/item?id=399699) | 把不同编程语言比作宗教，呈现各自的文化特征。 | 131 | 108 | 2008-12-16 |
| 18 | [Genetic Algorithm building a little car](https://news.ycombinator.com/item?id=390067) | 展示用遗传算法逐步生成小汽车的实验。 | 126 | 54 | 2008-12-08 |
| 19 | [Scientists extract images directly from brain](https://news.ycombinator.com/item?id=394826) | 报道科学家尝试直接从脑部活动中重建图像。 | 126 | 56 | 2008-12-11 |
| 20 | [Ask YC: Let's start a Hacker News book club](https://news.ycombinator.com/item?id=407067) | 提议成立 HN 读书会，以定期共读推动阅读和交流。 | 126 | 79 | 2008-12-23 |

## 2009-01

有效主帖 6,635 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [New users: Welcome.  Please read the site guidelines.](https://news.ycombinator.com/item?id=459289) | 欢迎新用户，并提醒发言前阅读社区准则、保持礼貌。 | 532 | 137 | 2009-01-31 |
| 2 | [Some things need to change](https://news.ycombinator.com/item?id=453514) | 作者呼吁对一些现状作出改变。 | 287 | 204 | 2009-01-28 |
| 3 | [A “short squeeze” sounds innocuous enough...](https://news.ycombinator.com/item?id=424506) | 以金融系统中的一次巧妙操作解释“逼空”。 | 224 | 51 | 2009-01-08 |
| 4 | [Why Google Employees Quit](https://news.ycombinator.com/item?id=439298) | 探讨 Google 员工选择离职的原因。 | 202 | 98 | 2009-01-18 |
| 5 | [How Much I Money Made From Side Projects In 2008](https://news.ycombinator.com/item?id=423204) | 作者盘点 2008 年业余项目带来的收入。 | 190 | 60 | 2009-01-07 |
| 6 | [Joel Spolsky: Thanks or No Thanks](https://news.ycombinator.com/item?id=433866) | Joel Spolsky 围绕接受还是拒绝表达看法。 | 188 | 84 | 2009-01-14 |
| 7 | [Congratulations, Paul & Jessica; Welcome to the world, George](https://news.ycombinator.com/item?id=448821) | 社区祝贺 Paul 与 Jessica 迎来孩子 George。 | 188 | 77 | 2009-01-25 |
| 8 | [The real cause of the financial crisis -- An MIT Blackjack Team perspective](https://news.ycombinator.com/item?id=433456) | 一位 MIT 二十一点团队成员提出对金融危机成因的解释。 | 185 | 60 | 2009-01-14 |
| 9 | [How to Sell More Software by Adding 12 Characters to Your Homepage](https://news.ycombinator.com/item?id=456768) | 介绍通过给首页增加十二个字符促进软件销售的做法。 | 185 | 65 | 2009-01-29 |
| 10 | [Potion - a little fast OO language by _why](https://news.ycombinator.com/item?id=425258) | 介绍 _why 开发的小型快速面向对象语言 Potion。 | 183 | 55 | 2009-01-08 |
| 11 | [The 37signals Effect](https://news.ycombinator.com/item?id=440432) | 探讨被称为“37signals 效应”的影响。 | 171 | 75 | 2009-01-19 |
| 12 | [Taming Perfectionism](https://news.ycombinator.com/item?id=452341) | 分享应对和控制完美主义的方法。 | 170 | 39 | 2009-01-27 |
| 13 | [Add "pwn" before youtube in the url of any youtube video to download it](https://news.ycombinator.com/item?id=458409) | 介绍在 YouTube 链接中加入 pwn 即可下载视频的工具。 | 164 | 53 | 2009-01-30 |
| 14 | [Lazy Linux: essential tricks for admins](https://news.ycombinator.com/item?id=435879) | 为 Linux 管理员整理节省操作时间的实用技巧。 | 162 | 53 | 2009-01-15 |
| 15 | [Apple: Jobs to Take Medical Leave of Absence](https://news.ycombinator.com/item?id=434351) | 苹果宣布 Steve Jobs 将请病假。 | 159 | 107 | 2009-01-14 |
| 16 | [YHackers: Click that "New" link](https://news.ycombinator.com/item?id=445454) | 呼吁用户查看 HN 新帖列表，帮助优质投稿获得关注。 | 157 | 59 | 2009-01-22 |
| 17 | [Working from Home: Why It Sucks](https://news.ycombinator.com/item?id=450408) | 作者讲述居家办公令自己不满意的地方。 | 156 | 101 | 2009-01-26 |
| 18 | [Steve Jobs speaks out about his health](https://news.ycombinator.com/item?id=420450) | Steve Jobs 公开回应外界对其健康的关切。 | 153 | 91 | 2009-01-05 |
| 19 | [Ever wonder what the Wikipedia database schema looks like?](https://news.ycombinator.com/item?id=441892) | 介绍维基百科数据库的表结构。 | 151 | 46 | 2009-01-20 |
| 20 | [Starting this summer, YC will be in California year-round](https://news.ycombinator.com/item?id=444114) | YC 宣布从当年夏季起全年在加州运作。 | 150 | 101 | 2009-01-22 |

## 2009-02

有效主帖 6,279 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Last.fm: "Techcrunch are full of shit"](https://news.ycombinator.com/item?id=491750) | Last.fm 用强烈措辞反驳 TechCrunch 的说法。 | 413 | 101 | 2009-02-23 |
| 2 | [What I've Learned from Hacker News](https://news.ycombinator.com/item?id=495053) | 作者总结从 Hacker News 社区学到的事情。 | 381 | 119 | 2009-02-25 |
| 3 | [How FriendFeed uses MySQL to store schema-less data](https://news.ycombinator.com/item?id=496946) | 介绍 FriendFeed 如何用 MySQL 存储无固定模式的数据。 | 347 | 84 | 2009-02-27 |
| 4 | [The most surprising thing I've seen in 2009, courtesy of Etherpad](https://news.ycombinator.com/item?id=495336) | 作者分享 Etherpad 带来的一次意外体验。 | 338 | 126 | 2009-02-26 |
| 5 | [Startups in 13 Sentences](https://news.ycombinator.com/item?id=491196) | 用十三句话概括创业的关键认识。 | 322 | 101 | 2009-02-23 |
| 6 | [Building and Scaling a Startup on Rails: Things We Learned the Hard Way (by Posterous S08)](https://news.ycombinator.com/item?id=491004) | Posterous 团队总结基于 Rails 创业和扩容时的教训。 | 249 | 55 | 2009-02-22 |
| 7 | [Why CSS should not be used for layout](https://news.ycombinator.com/item?id=463234) | 作者提出不应用 CSS 进行布局的观点。 | 248 | 147 | 2009-02-03 |
| 8 | [Keep Your Identity Small  ](https://news.ycombinator.com/item?id=471660) | 主张减少身份认同的束缚，以保持思考开放。 | 234 | 253 | 2009-02-08 |
| 9 | [A Unix Utility You Should Know About: Pipe Viewer](https://news.ycombinator.com/item?id=462244) | 介绍可显示管道数据传输进度的 UNIX 工具 Pipe Viewer。 | 201 | 63 | 2009-02-02 |
| 10 | [How Not To Sort By Average Rating](https://news.ycombinator.com/item?id=478632) | 解释为什么不应简单按平均评分排序。 | 195 | 56 | 2009-02-12 |
| 11 | [New Product From 280North: Atlas](https://news.ycombinator.com/item?id=493712) | 280 North 推出新产品 Atlas。 | 192 | 73 | 2009-02-24 |
| 12 | [Papers Every Programmer Should Read](https://news.ycombinator.com/item?id=496830) | 整理值得程序员阅读的论文。 | 189 | 14 | 2009-02-27 |
| 13 | [I opened a charming neighborhood coffee shop. Then it destroyed my life.](https://news.ycombinator.com/item?id=461791) | 作者讲述开一家温馨社区咖啡馆如何严重影响生活。 | 186 | 96 | 2009-02-02 |
| 14 | [How Not to Pitch to a Startup](https://news.ycombinator.com/item?id=487311) | 讨论向创业公司推销时应避免的做法。 | 184 | 44 | 2009-02-19 |
| 15 | [Continuous Deployment at IMVU: Doing the impossible fifty times a day.](https://news.ycombinator.com/item?id=475017) | 介绍 IMVU 如何通过持续部署每天上线约五十次。 | 172 | 73 | 2009-02-10 |
| 16 | [Hacker News is 2](https://news.ycombinator.com/item?id=486940) | Hacker News 迎来创立两周年。 | 165 | 67 | 2009-02-19 |
| 17 | [The most effective debt collecting email I ever wrote](https://news.ycombinator.com/item?id=462259) | 作者分享自己写过的一封有效催款邮件。 | 164 | 30 | 2009-02-02 |
| 18 | [The Audacity of Doing Nothing](https://news.ycombinator.com/item?id=477955) | 以“无所作为的勇气”为题反思行动与克制。 | 159 | 111 | 2009-02-12 |
| 19 | [On Building A Stupidly Fast Graph Database](https://news.ycombinator.com/item?id=497039) | 探讨构建高速图数据库的技术思路。 | 159 | 43 | 2009-02-27 |
| 20 | [How I almost killed Facebook](https://news.ycombinator.com/item?id=495334) | 作者回顾一次差点让 Facebook 遭受严重影响的经历。 | 157 | 55 | 2009-02-26 |

## 2009-03

有效主帖 7,001 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Google is Evil, Worse than PayPal: Don't use Google Checkout for your business](https://news.ycombinator.com/item?id=533849) | 作者批评 Google Checkout，并劝企业不要使用该服务。 | 400 | 150 | 2009-03-26 |
| 2 | [The Innards of Erlang ](https://news.ycombinator.com/item?id=512178) | 深入介绍 Erlang 的内部机制。 | 327 | 34 | 2009-03-11 |
| 3 | [Jason Fried: Get Satisfaction is "awfully close to blackmail"](https://news.ycombinator.com/item?id=540540) | Jason Fried 批评 Get Satisfaction 的做法近似敲诈。 | 291 | 142 | 2009-03-31 |
| 4 | [Why HN is slow lately](https://news.ycombinator.com/item?id=512145) | HN 因日访问人数大涨而变慢，站方说明临时应对措施。 | 270 | 122 | 2009-03-11 |
| 5 | [My Manhattan Project: How I helped build the bomb that blew up Wall Street.](https://news.ycombinator.com/item?id=538849) | 作者回顾自己参与构建危及华尔街的金融工具的经历。 | 260 | 43 | 2009-03-30 |
| 6 | [Understanding Git](https://news.ycombinator.com/item?id=531517) | 帮助读者理解 Git 的工作原理。 | 258 | 12 | 2009-03-25 |
| 7 | [Starting up with a friend](https://news.ycombinator.com/item?id=511539) | 讨论与朋友共同创业的经验与问题。 | 252 | 59 | 2009-03-11 |
| 8 | [Be Relentlessly Resourceful](https://news.ycombinator.com/item?id=508033) | 鼓励创业者持续主动寻找解决问题的办法。 | 241 | 161 | 2009-03-09 |
| 9 | [Why I Sued Google (and Won)](https://news.ycombinator.com/item?id=505255) | 作者讲述起诉 Google 并获胜的经历。 | 222 | 110 | 2009-03-06 |
| 10 | [Y Combinator: Party Like it's 2009](https://news.ycombinator.com/item?id=518411) | 以 2009 年为背景关注 Y Combinator 的创业活动。 | 222 | 49 | 2009-03-16 |
| 11 | [Why MIT switched from Scheme to Python](https://news.ycombinator.com/item?id=530605) | 解释麻省理工为何将相关课程从 Scheme 改为 Python。 | 219 | 128 | 2009-03-24 |
| 12 | [College dropout makes  $100,000 a year, with a two-day workweek](https://news.ycombinator.com/item?id=523849) | 报道一位大学辍学生每周工作两天、年入十万美元的经历。 | 194 | 75 | 2009-03-19 |
| 13 | [How to get a merchant account - a series of hoops](https://news.ycombinator.com/item?id=530055) | 梳理申请商户收款账户需要跨过的层层门槛。 | 190 | 40 | 2009-03-24 |
| 14 | [Command-line Fu ](https://news.ycombinator.com/item?id=527486) | 介绍汇集命令行技巧的 Command-line Fu。 | 189 | 22 | 2009-03-22 |
| 15 | [Zed's "One Battery Review" of Django](https://news.ycombinator.com/item?id=524715) | Zed Shaw 分享针对 Django 的一次简短评测。 | 188 | 35 | 2009-03-20 |
| 16 | [Goodbye Google: "Visual Design Lead" leaves Google](https://news.ycombinator.com/item?id=524956) | Google 视觉设计负责人宣布离职并解释决定。 | 188 | 96 | 2009-03-20 |
| 17 | [Perfect German Board Game Redefines Genre](https://news.ycombinator.com/item?id=535212) | 介绍一款被认为重塑类型的德国桌面游戏。 | 181 | 82 | 2009-03-27 |
| 18 | [Not Lisp again....](https://news.ycombinator.com/item?id=504667) | 以“又是 Lisp”为题回应关于这门语言的讨论。 | 178 | 39 | 2009-03-05 |
| 19 | [Y Combinator in Erlang](https://news.ycombinator.com/item?id=512210) | 展示用 Erlang 表达 Y 组合子的实现。 | 174 | 2 | 2009-03-11 |
| 20 | [Interview with the man who built Google's V8 engine from scratch](https://news.ycombinator.com/item?id=536438) | 访谈从零构建 Google V8 引擎的开发者。 | 170 | 46 | 2009-03-28 |

## 2009-04

有效主帖 6,759 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Oracle to buy Sun](https://news.ycombinator.com/item?id=570502) | Oracle 宣布将收购 Sun。 | 249 | 121 | 2009-04-20 |
| 2 | [Google uncloaks once-secret server](https://news.ycombinator.com/item?id=542531) | Google 揭开此前保密的服务器设计。 | 238 | 53 | 2009-04-01 |
| 3 | [Pirate Bay officially loses case](https://news.ycombinator.com/item?id=566565) | 海盗湾在相关诉讼中正式败诉。 | 226 | 164 | 2009-04-17 |
| 4 | [Designer gets accused of stealing his own work and billed $18,000](https://news.ycombinator.com/item?id=548166) | 一位设计师被指盗用自己的作品，还收到一万八千美元账单。 | 206 | 45 | 2009-04-06 |
| 5 | [Hacker News Startups: Listing/Wiki of startups founded by HNers (not just YC)](https://news.ycombinator.com/item?id=572631) | 汇集由 HN 用户创办的创业公司，而不限于 YC 项目。 | 205 | 47 | 2009-04-21 |
| 6 | [Pirate Bay's judge biased: Member of copyright organisations.](https://news.ycombinator.com/item?id=575261) | 报道海盗湾案件法官加入版权组织，引发公正性质疑。 | 202 | 38 | 2009-04-23 |
| 7 | [The Founder Visa](https://news.ycombinator.com/item?id=556908) | 提出为创业创始人设立签证的构想。 | 200 | 151 | 2009-04-10 |
| 8 | [Paul Buchheit: Make your site faster and cheaper to operate in one easy step](https://news.ycombinator.com/item?id=566609) | Paul Buchheit 分享一种同时提高网站速度与降低成本的办法。 | 186 | 59 | 2009-04-17 |
| 9 | [Five Founders](https://news.ycombinator.com/item?id=542240) | 以五位创始人为线索关注创业者。 | 179 | 66 | 2009-04-01 |
| 10 | [Why I Never Let Employees Negotiate a Raise](https://news.ycombinator.com/item?id=542173) | 作者解释为何不允许员工通过谈判争取加薪。 | 175 | 91 | 2009-04-01 |
| 11 | [The dark side of Dubai](https://news.ycombinator.com/item?id=550719) | 揭示迪拜繁华表象背后的阴暗面。 | 174 | 66 | 2009-04-07 |
| 12 | [Why Being Smart Won't Get You Laid](https://news.ycombinator.com/item?id=567807) | 作者讨论聪明才智为何未必有助于获得亲密关系。 | 172 | 147 | 2009-04-17 |
| 13 | [YC Rejected: Please read.](https://news.ycombinator.com/item?id=550351) | 面向 YC 被拒申请者解释社区无法判定拒绝原因。 | 171 | 31 | 2009-04-07 |
| 14 | [Ask HN: Do you have any code or projects of your own you would like to talk about instead?](https://news.ycombinator.com/item?id=586140) | 邀请读者分享正在开发的项目与代码，让讨论回到技术实践。 | 165 | 102 | 2009-04-30 |
| 15 | [There Is No Such Thing as Nuclear Waste](https://news.ycombinator.com/item?id=587271) | 作者提出所谓核废料并非真正废物的观点。 | 162 | 117 | 2009-04-30 |
| 16 | [Fuck the foundries](https://news.ycombinator.com/item?id=572730) | 作者以激烈措辞表达对字体厂商的不满。 | 161 | 105 | 2009-04-21 |
| 17 | [FBI seizes entire data center, won't say why](https://news.ycombinator.com/item?id=546067) | 报道 FBI 扣押整个数据中心却未说明理由。 | 158 | 49 | 2009-04-04 |
| 18 | [Hacker Newspaper: reformatted Hacker News](https://news.ycombinator.com/item?id=561161) | 介绍重新排版 Hacker News 内容的 Hacker Newspaper。 | 154 | 63 | 2009-04-14 |
| 19 | [Ubuntu 9.04 released](https://news.ycombinator.com/item?id=575567) | Ubuntu 9.04 正式发布。 | 154 | 116 | 2009-04-23 |
| 20 | ["I never said she stole my money" has 7 different meanings depending on the stressed word](https://news.ycombinator.com/item?id=583555) | 用一句英语的七种重音展示强调位置如何改变含义。 | 154 | 62 | 2009-04-28 |

## 2009-05

有效主帖 6,405 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Deny This, Last.fm](https://news.ycombinator.com/item?id=623086) | 作者以“否认这个吧”为题再次质问 Last.fm。 | 312 | 68 | 2009-05-23 |
| 2 | [A brief, incomplete and mostly wrong history of programming languages](https://news.ycombinator.com/item?id=599164) | 用简短、不完整且刻意失真的方式讲述编程语言史。 | 303 | 14 | 2009-05-08 |
| 3 | [HN Frontpage ranked using only votes from accounts over a year old](https://news.ycombinator.com/item?id=607271) | 尝试只用注册超过一年的账号投票来排列 HN 首页。 | 300 | 107 | 2009-05-13 |
| 4 | [My $3.3M Mistake](https://news.ycombinator.com/item?id=628335) | 作者回顾一次价值三百三十万美元的错误。 | 251 | 44 | 2009-05-27 |
| 5 | [Is There Anything Good About Men?](https://news.ycombinator.com/item?id=589346) | 以“男性有什么优点”为问题审视性别话题。 | 232 | 88 | 2009-05-02 |
| 6 | [How to Teach a Child to Argue](https://news.ycombinator.com/item?id=632518) | 讨论如何教孩子进行有理据的争辩。 | 217 | 54 | 2009-05-29 |
| 7 | [Hacker News Disease](https://news.ycombinator.com/item?id=588752) | 以“Hacker News 病”为名反思使用社区的习惯。 | 215 | 104 | 2009-05-01 |
| 8 | [PDF presentations on Data Mining, Bayesian Networks, Game Theory, Search Algorithms](https://news.ycombinator.com/item?id=608788) | 分享数据挖掘、贝叶斯网络、博弈论及搜索算法的讲义。 | 197 | 7 | 2009-05-14 |
| 9 | [Milton Glaser: Ten Things I Have Learned](https://news.ycombinator.com/item?id=592580) | Milton Glaser 总结自己学到的十件事。 | 194 | 33 | 2009-05-04 |
| 10 | [Can you trust 37signals with your password? ](https://news.ycombinator.com/item?id=589852) | 质疑用户是否能放心把密码交给 37signals。 | 189 | 130 | 2009-05-02 |
| 11 | [Don’t! The secret of self-control](https://news.ycombinator.com/item?id=603364) | 探讨克制冲动和维持自我控制的秘诀。 | 186 | 69 | 2009-05-11 |
| 12 | [Spolsky: Why Circuit City Failed, and Why B&H Thrives](https://news.ycombinator.com/item?id=593984) | Joel Spolsky 对比 Circuit City 的失败与 B&H 的兴盛。 | 185 | 79 | 2009-05-05 |
| 13 | [My Personal Credit Crisis](https://news.ycombinator.com/item?id=610896) | 作者记录自己经历的个人信贷危机。 | 185 | 201 | 2009-05-15 |
| 14 | [Why it's expensive to be poor](https://news.ycombinator.com/item?id=619110) | 解释贫困为何反而可能增加日常生活成本。 | 183 | 194 | 2009-05-20 |
| 15 | [The speed, size and dependability of programming languages](https://news.ycombinator.com/item?id=634692) | 比较编程语言在速度、程序规模与可靠性方面的表现。 | 176 | 56 | 2009-05-31 |
| 16 | [Programmers Need To Learn Statistics Or I Will Kill Them All (2005)](https://news.ycombinator.com/item?id=626771) | 重读 Zed Shaw 于 2005 年呼吁程序员学习统计学的文章。 | 174 | 116 | 2009-05-26 |
| 17 | [Google Wave Drips With Ambition. A New Communication Platform For A New Web.](https://news.ycombinator.com/item?id=630427) | 介绍试图重塑网络沟通的 Google Wave 平台。 | 169 | 99 | 2009-05-28 |
| 18 | [The night I met Einstein](https://news.ycombinator.com/item?id=589608) | 作者回忆某个夜晚与爱因斯坦相遇的经历。 | 167 | 39 | 2009-05-02 |
| 19 | [How to Be Persuasive](https://news.ycombinator.com/item?id=613402) | 分享提高表达说服力的方法。 | 160 | 26 | 2009-05-17 |
| 20 | [Homebrewed CPU Is a Beautiful Mess of Wires](https://news.ycombinator.com/item?id=630154) | 展示由大量连线搭建而成的自制 CPU。 | 159 | 53 | 2009-05-28 |

## 2009-06

有效主帖 6,460 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [How I Hacked Hacker News (with arc security advisory)](https://news.ycombinator.com/item?id=639976) | 作者披露 HN 登录 Cookie 随机性漏洞及 Arc 3 修复建议。 | 928 | 78 | 2009-06-03 |
| 2 | [Typing The Letters A-E-S Into Your Code? You’re Doing It Wrong](https://news.ycombinator.com/item?id=639647) | 提醒开发者审慎对待在代码中直接使用 AES 的做法。 | 258 | 74 | 2009-06-03 |
| 3 | [Less, a leaner CSS](https://news.ycombinator.com/item?id=660674) | 介绍让 CSS 编写更精简的 Less。 | 253 | 85 | 2009-06-16 |
| 4 | [RIP Michael Jackson](https://news.ycombinator.com/item?id=674438) | 悼念逝世的歌手 Michael Jackson。 | 248 | 158 | 2009-06-25 |
| 5 | [US Patent 5255452 (or: Why Michael Jackson was a Hacker)](https://news.ycombinator.com/item?id=674647) | 通过一项美国专利展示 Michael Jackson 的发明者一面。 | 239 | 58 | 2009-06-25 |
| 6 | [The First Few Milliseconds of an HTTPS Connection](https://news.ycombinator.com/item?id=650914) | 拆解 HTTPS 连接建立最初几毫秒发生的过程。 | 236 | 33 | 2009-06-10 |
| 7 | [Firefox 3.5 is out](https://news.ycombinator.com/item?id=680853) | Firefox 3.5 正式发布。 | 234 | 71 | 2009-06-30 |
| 8 | [No Hire](https://news.ycombinator.com/item?id=675544) | 围绕招聘中“不录用”的决定展开思考。 | 230 | 115 | 2009-06-26 |
| 9 | [Apple’s WWDC-Closing ‘Fuck You’ to iPhone Developers](https://news.ycombinator.com/item?id=659271) | 作者认为苹果在 WWDC 结束时冒犯了 iPhone 开发者。 | 228 | 142 | 2009-06-15 |
| 10 | [Kindle's DRM Rears Its Ugly Head and It Is Ugly](https://news.ycombinator.com/item?id=669231) | 作者批评 Kindle 数字版权限制带来的问题。 | 208 | 41 | 2009-06-22 |
| 11 | [Time Wastes Too Fast](https://news.ycombinator.com/item?id=675308) | 感叹时间流逝过快，反思如何使用时间。 | 202 | 35 | 2009-06-26 |
| 12 | [Why Google Bothered to Appeal a $761 Small Claims Case (and Won)](https://news.ycombinator.com/item?id=649490) | 解释 Google 为何为一宗 761 美元小额案件上诉并获胜。 | 195 | 137 | 2009-06-09 |
| 13 | [The Zen of HN](https://news.ycombinator.com/item?id=668973) | 以禅意视角思考 Hacker News 的参与方式。 | 182 | 46 | 2009-06-22 |
| 14 | [Pirate Party Wins 7.1% of Swedish Vote, Enters European Parliament](https://news.ycombinator.com/item?id=646288) | 瑞典海盗党获得 7.1% 选票，进入欧洲议会。 | 177 | 54 | 2009-06-07 |
| 15 | [Pragmatic Theory, Commendo, Yahoo and AT&T hit the Netflix grand prize](https://news.ycombinator.com/item?id=676038) | 报道多个团队在 Netflix 算法竞赛中达到大奖门槛。 | 174 | 29 | 2009-06-26 |
| 16 | [Astalavista.com hacked, including details](https://news.ycombinator.com/item?id=642671) | 披露 Astalavista.com 遭入侵的消息及相关细节。 | 171 | 64 | 2009-06-05 |
| 17 | [Ask HN: Please review my new project: almost.at](https://news.ycombinator.com/item?id=636711) | 开发者邀请 HN 用户评价新项目 almost.at。 | 164 | 81 | 2009-06-01 |
| 18 | [Why you need your own company](https://news.ycombinator.com/item?id=651879) | 阐述拥有自己公司的理由。 | 161 | 38 | 2009-06-10 |
| 19 | [Opera Unite reinvents the Web: a Web server on the Web browser](https://news.ycombinator.com/item?id=659696) | Opera Unite 尝试在浏览器中加入 Web 服务器。 | 160 | 117 | 2009-06-16 |
| 20 | [Python to get Google-backed speedup](https://news.ycombinator.com/item?id=656369) | 介绍获得 Google 支持的 Python 加速计划。 | 158 | 69 | 2009-06-13 |

## 2009-07

有效主帖 7,909 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Introducing the Google Chrome OS](https://news.ycombinator.com/item?id=693293) | Google 正式介绍 Chrome OS 操作系统。 | 370 | 167 | 2009-07-08 |
| 2 | [My students forged the notes. I turned them into a lesson plan.](https://news.ycombinator.com/item?id=719526) | 教师把学生伪造请假条的行为转化为课堂教案。 | 327 | 64 | 2009-07-23 |
| 3 | [Amazon deletes purchased copies of 1984 from Kindle](https://news.ycombinator.com/item?id=710506) | 亚马逊从 Kindle 删除用户已购买的《1984》。 | 320 | 141 | 2009-07-17 |
| 4 | [Maker's Schedule, Manager's Schedule](https://news.ycombinator.com/item?id=718279) | 区分创造者与管理者对时间安排的不同需求。 | 312 | 89 | 2009-07-22 |
| 5 | [Did you mean recursion?](https://news.ycombinator.com/item?id=719408) | 以“你是指递归吗”的问句呈现递归概念。 | 290 | 50 | 2009-07-23 |
| 6 | [Zed Shaw: Why I (A/L)GPL](https://news.ycombinator.com/item?id=703086) | Zed Shaw 解释自己选择 AGPL 或 LGPL 许可证的理由。 | 279 | 174 | 2009-07-14 |
| 7 | [Why I won't be at my high school reunion](https://news.ycombinator.com/item?id=709733) | 作者解释为何不参加高中同学聚会。 | 271 | 262 | 2009-07-17 |
| 8 | [Ramen Profitable](https://news.ycombinator.com/item?id=726544) | 介绍创业公司收入足以维持创始人基本生活的状态。 | 264 | 136 | 2009-07-27 |
| 9 | [You should follow me on Twitter](https://news.ycombinator.com/item?id=704738) | 作者邀请读者在 Twitter 关注自己。 | 263 | 71 | 2009-07-14 |
| 10 | [Share HN: I wrote an app to help my paralyzed cousin type significantly faster.](https://news.ycombinator.com/item?id=715265) | 开发者分享帮助瘫痪表亲显著提高打字速度的应用。 | 240 | 29 | 2009-07-20 |
| 11 | [MacBook Pro, Thousands of Colors](https://news.ycombinator.com/item?id=706343) | 围绕 MacBook Pro 显示色彩数量的问题展开关注。 | 231 | 148 | 2009-07-15 |
| 12 | [Linus: "Microsoft Hatred Is a Disease"](https://news.ycombinator.com/item?id=720779) | Linus Torvalds 批评把仇视微软当作立场的心态。 | 227 | 55 | 2009-07-24 |
| 13 | [Pro Git - CC licensed book on Git by Scott Chacon](https://news.ycombinator.com/item?id=726023) | 介绍 Scott Chacon 采用 CC 许可发布的《Pro Git》。 | 224 | 25 | 2009-07-27 |
| 14 | [Tony Hsieh's Email to Employees RE: Zappos' Sale to Amazon](https://news.ycombinator.com/item?id=718483) | 分享 Tony Hsieh 就 Zappos 出售给亚马逊写给员工的邮件。 | 221 | 32 | 2009-07-22 |
| 15 | [The Trouble with the Segway](https://news.ycombinator.com/item?id=730755) | 讨论 Segway 面临的问题。 | 221 | 165 | 2009-07-29 |
| 16 | [FCC Takes On Apple And AT&T Over Google Voice Rejection](https://news.ycombinator.com/item?id=735677) | FCC 就 Google Voice 被拒事件向苹果和 AT&T 展开问询。 | 217 | 91 | 2009-07-31 |
| 17 | [Potion: A Short Pamphlet](https://news.ycombinator.com/item?id=682936) | 以简短手册形式介绍 Potion 语言。 | 214 | 46 | 2009-07-01 |
| 18 | [Source code from Apollo 11 open-sourced](https://news.ycombinator.com/item?id=715395) | 阿波罗 11 号的相关源代码被公开。 | 211 | 58 | 2009-07-20 |
| 19 | [Bobby McFerrin Demonstrates the Power of the Pentatonic Scale](https://news.ycombinator.com/item?id=734380) | Bobby McFerrin 用现场演示展示五声音阶的力量。 | 210 | 48 | 2009-07-31 |
| 20 | [Calling out Hacker News](https://news.ycombinator.com/item?id=682594) | 作者公开对 Hacker News 提出批评。 | 209 | 68 | 2009-07-01 |

## 2009-08

有效主帖 8,356 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [_why is no more](https://news.ycombinator.com/item?id=773106) | 关注 Ruby 创作者 _why 突然离开公众视野的消息。 | 558 | 399 | 2009-08-19 |
| 2 | [Why Van Halen's contract calls for the removal of all brown M&Ms](https://news.ycombinator.com/item?id=743860) | 解释 Van Halen 合同为何要求去掉所有棕色 M&M 巧克力豆。 | 364 | 79 | 2009-08-05 |
| 3 | [Make Frontpage of Slashdot, Reddit, Hacker News == Google Disables AdSense](https://news.ycombinator.com/item?id=790800) | 作者称登上多个技术社区首页后，自己的 AdSense 被停用。 | 359 | 159 | 2009-08-28 |
| 4 | [Dirty Coding tricks used in Production Video Games](https://news.ycombinator.com/item?id=776296) | 分享商业电子游戏开发中采用的巧妙编码捷径。 | 330 | 45 | 2009-08-20 |
| 5 | [Apple now censoring dictionaries in the App Store](https://news.ycombinator.com/item?id=742616) | 批评苹果开始审查 App Store 中的词典内容。 | 327 | 80 | 2009-08-05 |
| 6 | [Eulogy to _why](https://news.ycombinator.com/item?id=773920) | 以悼词形式回顾 _why 对技术社区的影响。 | 318 | 92 | 2009-08-19 |
| 7 | [  Facebook Acquires FriendFeed ](https://news.ycombinator.com/item?id=753750) | Facebook 收购 FriendFeed。 | 279 | 82 | 2009-08-10 |
| 8 | [Signs that you're a bad programmer](https://news.ycombinator.com/item?id=746873) | 列举可能暴露编程能力问题的行为迹象。 | 273 | 121 | 2009-08-07 |
| 9 | [What Kate saw in Silicon Valley](https://news.ycombinator.com/item?id=796573) | 讲述 Kate 在硅谷看到的景象。 | 264 | 107 | 2009-08-31 |
| 10 | [So long, and thanks for all the fish](https://news.ycombinator.com/item?id=776978) | 作者以“再见，感谢所有的鱼”表达告别。 | 245 | 93 | 2009-08-21 |
| 11 | [You're a little company, now act like one](https://news.ycombinator.com/item?id=795976) | 提醒小公司按照自身规模选择做事方式。 | 240 | 53 | 2009-08-31 |
| 12 | [Traffic Hacks: How One Driver Can Vastly Improve Traffic](https://news.ycombinator.com/item?id=785259) | 探讨一名司机如何通过驾驶方式改善整体交通。 | 237 | 146 | 2009-08-25 |
| 13 | [Ask HN: Who's Hiring? (take 2)](https://news.ycombinator.com/item?id=759452) | 再次征集招聘岗位，帮助 HN 企业与求职者建立联系。 | 202 | 227 | 2009-08-12 |
| 14 | [Dr. Eric Schmidt Resigns from Apple’s Board of Directors](https://news.ycombinator.com/item?id=739070) | Eric Schmidt 辞去苹果董事职务。 | 199 | 47 | 2009-08-03 |
| 15 | [How I explained REST to my wife](https://news.ycombinator.com/item?id=763570) | 作者分享向妻子解释 REST 的方法。 | 199 | 57 | 2009-08-14 |
| 16 | [Please don't use hnreputation](https://news.ycombinator.com/item?id=789469) | 站方要求停用会高频请求服务器的 hnreputation 脚本。 | 199 | 82 | 2009-08-27 |
| 17 | [R.I.P. Les Paul ](https://news.ycombinator.com/item?id=761205) | 悼念音乐人 Les Paul。 | 196 | 34 | 2009-08-13 |
| 18 | [YC startups unite to drive nail into the coffin of Internet Explorer 6](https://news.ycombinator.com/item?id=742029) | 多家 YC 公司联手推动停止支持 Internet Explorer 6。 | 187 | 110 | 2009-08-04 |
| 19 | [999999999999999 - 999999999999997](https://news.ycombinator.com/item?id=782985) | 以两个大整数相减的算式引出计算问题。 | 185 | 101 | 2009-08-24 |
| 20 | [Hacking a Google Interview - MIT's guide to Google interviews](https://news.ycombinator.com/item?id=784479) | 分享 MIT 整理的 Google 技术面试准备指南。 | 185 | 41 | 2009-08-25 |

## 2009-09

有效主帖 7,994 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Petabytes on a budget: How to build cheap cloud storage](https://news.ycombinator.com/item?id=797995) | 介绍以较低预算搭建 PB 级云存储的方法。 | 401 | 105 | 2009-09-01 |
| 2 | [Yeah Ok, So Facebook Punk’d Us](https://news.ycombinator.com/item?id=816715) | 作者承认自己被 Facebook 的做法戏弄。 | 347 | 83 | 2009-09-11 |
| 3 | [When a co-founder dies](https://news.ycombinator.com/item?id=843399) | 探讨联合创始人去世后公司与同伴面对的处境。 | 335 | 43 | 2009-09-25 |
| 4 | [The Duct Tape Programmer](https://news.ycombinator.com/item?id=840523) | 以“胶带程序员”为喻赞赏务实解决问题的开发方式。 | 333 | 118 | 2009-09-24 |
| 5 | [How to run a small consultancy / freelancing business](https://news.ycombinator.com/item?id=848370) | 分享经营小型咨询公司或自由职业业务的方法。 | 319 | 63 | 2009-09-28 |
| 6 | [Dropbox's Summer 07 YC Application](https://news.ycombinator.com/item?id=801503) | 公开 Dropbox 申请 YC 2007 年夏季项目的材料。 | 310 | 59 | 2009-09-03 |
| 7 | [Tornado: FriendFeed's non-blocking Python web server is now open source](https://news.ycombinator.com/item?id=815681) | FriendFeed 将非阻塞 Python Web 服务器 Tornado 开源。 | 291 | 73 | 2009-09-10 |
| 8 | [Experiment: No Comment Scores](https://news.ycombinator.com/item?id=844979) | HN 试验隐藏评论分数，希望改善随大众投票的氛围。 | 289 | 313 | 2009-09-26 |
| 9 | [The bar for success in our industry is too low](https://news.ycombinator.com/item?id=800450) | 作者批评科技行业对成功的衡量门槛过低。 | 282 | 81 | 2009-09-02 |
| 10 | [Want to Remember Everything You'll Ever Learn? Surrender to This Algorithm ](https://news.ycombinator.com/item?id=818157) | 介绍通过记忆算法帮助长期保留所学内容的思路。 | 258 | 87 | 2009-09-11 |
| 11 | [Learning Advanced JavaScript](https://news.ycombinator.com/item?id=823347) | 提供学习 JavaScript 进阶知识的资源。 | 257 | 44 | 2009-09-15 |
| 12 | [  Google Has A Solution For Internet Explorer: Turn It Into Chrome ](https://news.ycombinator.com/item?id=837597) | Google 推出让 Internet Explorer 使用 Chrome 能力的方案。 | 245 | 92 | 2009-09-22 |
| 13 | [Why I'm Moving From Desktop Apps to Web Apps](https://news.ycombinator.com/item?id=806683) | 作者解释从桌面应用转向 Web 应用的原因。 | 243 | 74 | 2009-09-05 |
| 14 | [10 Downing Street: Treatment of Alan Turing was "appalling"](https://news.ycombinator.com/item?id=816217) | 英国首相府称当年对待 Alan Turing 的方式令人震惊。 | 237 | 81 | 2009-09-10 |
| 15 | [The Next Generation Bends Over](https://news.ycombinator.com/item?id=829502) | 作者以尖锐标题表达对下一代处境的忧虑。 | 220 | 204 | 2009-09-18 |
| 16 | [Efficient Editing With vim](https://news.ycombinator.com/item?id=843732) | 分享使用 Vim 提高编辑效率的方法。 | 218 | 121 | 2009-09-25 |
| 17 | [And if only 1% of those people...](https://news.ycombinator.com/item?id=847334) | 质疑创业预测中“只要其中百分之一的人购买”的推算。 | 210 | 43 | 2009-09-27 |
| 18 | [Teaching Linear Algebra](https://news.ycombinator.com/item?id=850485) | 讨论线性代数的教学方式。 | 208 | 59 | 2009-09-29 |
| 19 | [How a software engineer invented a breakthrough medical device](https://news.ycombinator.com/item?id=804974) | 讲述一位软件工程师发明突破性医疗设备的经历。 | 207 | 81 | 2009-09-04 |
| 20 | [How Tim Schafer Broke Into the Game Industry: A Legendary Cover Letter](https://news.ycombinator.com/item?id=850948) | 通过一封求职信回顾 Tim Schafer 如何进入游戏行业。 | 207 | 14 | 2009-09-29 |

## 2009-10

有效主帖 8,568 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [A terrible tragedy: Dan Haubert of Ticketstumbler (fallentimes) has passed away](https://news.ycombinator.com/item?id=859117) | Ticketstumbler 的 Dan Haubert 去世，社区表达哀悼。 | 626 | 134 | 2009-10-03 |
| 2 | [What Startups Are Really Like](https://news.ycombinator.com/item?id=902151) | 揭示创业公司的真实生活与日常处境。 | 382 | 119 | 2009-10-25 |
| 3 | [So...what the hell's wrong with you, Shooter?](https://news.ycombinator.com/item?id=868325) | 用户讲述被误诊为 ALS 等疾病的漫长求医经历。 | 324 | 126 | 2009-10-08 |
| 4 | [This Is a Photoshop and It Blew My Mind - Photosketch](https://news.ycombinator.com/item?id=863294) | 展示名为 PhotoSketch 的图像合成技术。 | 321 | 67 | 2009-10-06 |
| 5 | [If you had 5 dollars and 2 hours, how would you make as much money as possible?](https://news.ycombinator.com/item?id=912105) | 提出仅有五美元和两小时应如何尽量赚钱的挑战。 | 321 | 185 | 2009-10-30 |
| 6 | [I Was Told I Was Very Smart](https://news.ycombinator.com/item?id=896113) | 作者反思从小被称赞聪明的经历。 | 309 | 113 | 2009-10-22 |
| 7 | [The Gervais Principle, or The Office According to "The Office"](https://news.ycombinator.com/item?id=881296) | 借电视剧《办公室》提出解释职场组织的 Gervais 原理。 | 307 | 63 | 2009-10-14 |
| 8 | [Google Groups is Dead ](https://news.ycombinator.com/item?id=905520) | 作者以“Google Groups 已死”批评这项服务的状态。 | 259 | 67 | 2009-10-27 |
| 9 | [Thank you for giving me the opportunity to explain this to you](https://news.ycombinator.com/item?id=891726) | 围绕“感谢你给我解释机会”这句话展开交流思考。 | 254 | 53 | 2009-10-20 |
| 10 | [Tell HN: My 'mystery project': I couldn't sleep, so I backed up GeoCities](https://news.ycombinator.com/item?id=903567) | 一位用户因失眠启动项目，备份即将消失的 GeoCities。 | 250 | 65 | 2009-10-26 |
| 11 | [How to Write Clearly, Think Clearly, and Learn Easily](https://news.ycombinator.com/item?id=874747) | 分享清晰写作、清晰思考与高效学习的方法。 | 241 | 110 | 2009-10-11 |
| 12 | [What I've Earned (And Learned) From Writing a Ruby Programming Book](https://news.ycombinator.com/item?id=869106) | 作者总结写作 Ruby 编程书带来的收入与经验。 | 233 | 70 | 2009-10-08 |
| 13 | [Paul Buchheit: Applied Philosophy, a.k.a. "Hacking"](https://news.ycombinator.com/item?id=880730) | Paul Buchheit 将实践哲学与黑客式探索联系起来。 | 233 | 34 | 2009-10-14 |
| 14 | [Aaron Swartz shows his FBI file](https://news.ycombinator.com/item?id=862529) | Aaron Swartz 展示 FBI 为他建立的档案。 | 224 | 85 | 2009-10-05 |
| 15 | [Example of a good YC application video: Directed Edge](https://news.ycombinator.com/item?id=855057) | 以 Directed Edge 为例展示一份优秀的 YC 申请视频。 | 218 | 29 | 2009-10-01 |
| 16 | [How We Made GitHub Fast: A detailed look at GitHub's new architecture](https://news.ycombinator.com/item?id=895072) | 深入介绍 GitHub 为提高速度采用的新架构。 | 214 | 23 | 2009-10-21 |
| 17 | [What problems does Google Wave solve?](https://news.ycombinator.com/item?id=883116) | 追问 Google Wave 究竟解决了哪些问题。 | 213 | 67 | 2009-10-15 |
| 18 | [Guido's Proposal: Moratorium on Python language changes](https://news.ycombinator.com/item?id=895101) | Guido 提议暂停 Python 语言层面的变更。 | 210 | 64 | 2009-10-21 |
| 19 | [Ubuntu 9.10 Karmic Koala released](https://news.ycombinator.com/item?id=909981) | Ubuntu 9.10 Karmic Koala 正式发布。 | 204 | 164 | 2009-10-29 |
| 20 | [Brewing a Better Rating System](https://news.ycombinator.com/item?id=910976) | 探讨如何设计更合理的评分系统。 | 200 | 35 | 2009-10-29 |

## 2009-11

有效主帖 8,027 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Apple's Mistake](https://news.ycombinator.com/item?id=950751) | 作者审视苹果犯下的一项错误。 | 723 | 269 | 2009-11-19 |
| 2 | [Secret copyright treaty leaks. It's bad. Very bad.](https://news.ycombinator.com/item?id=920704) | 报道秘密版权条约内容泄露，并对其表达担忧。 | 588 | 287 | 2009-11-04 |
| 3 | [The End Of The CrunchPad ](https://news.ycombinator.com/item?id=968018) | 关注 CrunchPad 项目的终结。 | 435 | 138 | 2009-11-30 |
| 4 | [Google Go: A New Programming Language That’s Python Meets C++](https://news.ycombinator.com/item?id=934142) | 介绍 Google 新语言 Go 及其与 Python、C++ 的联系。 | 377 | 218 | 2009-11-10 |
| 5 | [One of my favorite professors in college was a self-confessed liar](https://news.ycombinator.com/item?id=959550) | 作者回忆一位坦承自己说谎的大学教授。 | 376 | 58 | 2009-11-24 |
| 6 | [HN Help: I'm lost](https://news.ycombinator.com/item?id=937430) | 一位有知名作品的 HN 老用户匿名倾诉人生迷茫并求助。 | 366 | 261 | 2009-11-12 |
| 7 | [Performance comparison between EC2, Slicehost, Linode, Rackspace Cloud, Prgmr](https://news.ycombinator.com/item?id=966555) | 比较 EC2、Slicehost、Linode 等云服务的性能。 | 365 | 146 | 2009-11-29 |
| 8 | [The Incompetence of American Airlines and the Fate of Mr. X](https://news.ycombinator.com/item?id=922913) | 围绕美国航空的工作失误与一位员工的命运展开批评。 | 323 | 98 | 2009-11-04 |
| 9 | [Your looks and your inbox](https://news.ycombinator.com/item?id=949519) | 探讨个人外貌与收到的消息之间的关系。 | 315 | 102 | 2009-11-19 |
| 10 | [Thank you, Rails](https://news.ycombinator.com/item?id=925436) | 作者向 Rails 表达感谢。 | 297 | 77 | 2009-11-06 |
| 11 | [Wakemate (YC S09) helps you kiss groggy mornings goodbye](https://news.ycombinator.com/item?id=960163) | 介绍旨在改善起床状态的 YC 项目 Wakemate。 | 289 | 143 | 2009-11-24 |
| 12 | [Scamville: The Social Gaming Ecosystem of Hell](https://news.ycombinator.com/item?id=914685) | 揭露社交游戏生态中被称为“骗局之城”的乱象。 | 279 | 90 | 2009-11-01 |
| 13 | [Aaron Swartz: How I Hire Programmers](https://news.ycombinator.com/item?id=965982) | Aaron Swartz 分享招聘程序员的方法。 | 276 | 97 | 2009-11-29 |
| 14 | [The Nerd Handbook](https://news.ycombinator.com/item?id=938809) | 提供理解技术宅思维与行为方式的手册。 | 247 | 55 | 2009-11-12 |
| 15 | [Scroll Clock](https://news.ycombinator.com/item?id=949404) | 展示名为 Scroll Clock 的时钟作品。 | 216 | 12 | 2009-11-18 |
| 16 | [How to get automatically rejected by an angel investor](https://news.ycombinator.com/item?id=921779) | 列出会让天使投资人直接拒绝的行为。 | 214 | 21 | 2009-11-04 |
| 17 | [Creating Controversy for its own Sake (AA.com redesign fiasco)](https://news.ycombinator.com/item?id=924943) | 以美国航空网站改版争议反思刻意制造争议的做法。 | 210 | 113 | 2009-11-05 |
| 18 | [Deep Tracing of Internet Explorer](https://news.ycombinator.com/item?id=947470) | 介绍深入跟踪 Internet Explorer 执行行为的方法。 | 201 | 14 | 2009-11-17 |
| 19 | [Mandelbulb: The Unravelling of the Real 3D Mandelbrot Fractal](https://news.ycombinator.com/item?id=935241) | 介绍三维曼德布罗分形 Mandelbulb 的探索。 | 200 | 23 | 2009-11-11 |
| 20 | [Node.js is genuinely exciting](https://news.ycombinator.com/item?id=957266) | 作者分享对 Node.js 技术潜力的兴奋。 | 197 | 67 | 2009-11-23 |

## 2009-12

有效主帖 7,875 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Microsoft rips off Plurk](https://news.ycombinator.com/item?id=994417) | 指称微软抄袭社交网站 Plurk。 | 581 | 135 | 2009-12-14 |
| 2 | [There's no speed limit. (The lessons that changed my life.)](https://news.ycombinator.com/item?id=970945) | 作者分享改变自己人生、打破学习速度限制的经验。 | 386 | 60 | 2009-12-01 |
| 3 | [The story of my startup (and the Google/YouTube API trap)](https://news.ycombinator.com/item?id=1019360) | 作者回顾创业经历及依赖 Google、YouTube API 的陷阱。 | 352 | 119 | 2009-12-28 |
| 4 | [How to Slice a Bagel into Two Linked Halves](https://news.ycombinator.com/item?id=982249) | 展示把百吉饼切成相互套连两半的方法。 | 350 | 25 | 2009-12-07 |
| 5 | [How do I know China wrecked the Copenhagen deal? I was in the room.](https://news.ycombinator.com/item?id=1011258) | 一位亲历者指称中国破坏了哥本哈根气候协议谈判。 | 349 | 188 | 2009-12-23 |
| 6 | [Why I gave away my company to charity](https://news.ycombinator.com/item?id=976659) | 作者解释将自己的公司捐给慈善机构的原因。 | 328 | 83 | 2009-12-04 |
| 7 | [The Elves Leave Middle Earth – Sodas Are No Longer Free](https://news.ycombinator.com/item?id=1007750) | 用汽水不再免费这一变化描写公司氛围的转变。 | 327 | 226 | 2009-12-21 |
| 8 | [Forensic analysis of recent Victoria's Secret photo](https://news.ycombinator.com/item?id=1017726) | 对一张维多利亚的秘密照片进行图像取证分析。 | 308 | 54 | 2009-12-27 |
| 9 | [Welcome to HN.  Please, read 'Hacker News Guidelines.' We take them seriously.](https://news.ycombinator.com/item?id=978217) | 提醒新用户认真阅读并遵守 Hacker News 社区准则。 | 301 | 117 | 2009-12-05 |
| 10 | [Schneier's response to Eric Schmidt](https://news.ycombinator.com/item?id=986716) | Bruce Schneier 回应 Eric Schmidt 的隐私言论。 | 291 | 96 | 2009-12-09 |
| 11 | [A piece with a lot of screenshots about the close tab behaviour in Google Chrome](https://news.ycombinator.com/item?id=988411) | 用大量截图分析 Chrome 关闭标签页时的行为。 | 283 | 100 | 2009-12-10 |
| 12 | [Eric Schmidt: "If you have something [to hide], maybe you shouldn't be doing it"](https://news.ycombinator.com/item?id=983717) | Eric Schmidt 关于“有事要隐藏”的言论引发隐私讨论。 | 279 | 168 | 2009-12-08 |
| 13 | [Squareup](https://news.ycombinator.com/item?id=970250) | 介绍移动收款服务 Squareup。 | 278 | 155 | 2009-12-01 |
| 14 | [EtherPad Back Online Until Open Sourced](https://news.ycombinator.com/item?id=979055) | EtherPad 恢复在线服务，承诺保持运行直到开源。 | 276 | 68 | 2009-12-06 |
| 15 | [EtherPad Open Source Release](https://news.ycombinator.com/item?id=1002592) | EtherPad 正式公开源代码。 | 275 | 73 | 2009-12-18 |
| 16 | [How Duke Nukem Forever Failed: Unlimited time, budget and ambition](https://news.ycombinator.com/item?id=1008624) | 从无限时间、预算和野心审视《永远的毁灭公爵》的失败。 | 270 | 75 | 2009-12-21 |
| 17 | [Introducing Google Public DNS: A new DNS resolver from Google](https://news.ycombinator.com/item?id=974642) | Google 推出公共 DNS 解析服务 Google Public DNS。 | 264 | 155 | 2009-12-03 |
| 18 | [Google acquires AppJet/Etherpad](https://news.ycombinator.com/item?id=977015) | Google 收购 AppJet 及其 EtherPad 产品。 | 258 | 98 | 2009-12-04 |
| 19 | [The Apple Tablet](https://news.ycombinator.com/item?id=1024709) | 关注苹果平板电脑这一产品话题。 | 254 | 143 | 2009-12-31 |
| 20 | [They Killed My Lawyer](https://news.ycombinator.com/item?id=1016515) | 作者以“他们杀了我的律师”为题讲述遭遇。 | 252 | 65 | 2009-12-27 |

## 2010-01

有效主帖 9,459 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [A new approach to China](https://news.ycombinator.com/item?id=1048800) | Google 宣布对中国业务采取新的处理方式。 | 1145 | 368 | 2010-01-12 |
| 2 | [Dan](https://news.ycombinator.com/item?id=1085258) | 一篇以 Dan 为题、围绕这一人物展开的文字。 | 508 | 34 | 2010-01-28 |
| 3 | [Evolution of a Python programmer](https://news.ycombinator.com/item?id=1087068) | 描写 Python 程序员随经验积累发生的变化。 | 366 | 90 | 2010-01-29 |
| 4 | [The 4 Big Myths of Profile Pictures](https://news.ycombinator.com/item?id=1065087) | 总结个人头像照片常见的四种误解。 | 357 | 126 | 2010-01-20 |
| 5 | [Need to refresh your math skills? From basic algebra to calculus and beyond.](https://news.ycombinator.com/item?id=1058359) | 整理从基础代数到微积分及更高阶内容的数学复习资源。 | 344 | 70 | 2010-01-17 |
| 6 | [I Have No Talent](https://news.ycombinator.com/item?id=1048202) | 作者以“我没有天赋”为题反思能力与成长。 | 334 | 74 | 2010-01-12 |
| 7 | [Realism in UI Design](https://news.ycombinator.com/item?id=1067333) | 探讨用户界面设计中写实风格的运用。 | 324 | 57 | 2010-01-21 |
| 8 | [Black Hat SEO Case Study: How Mahalo Makes Black Look White](https://news.ycombinator.com/item?id=1073723) | 以 Mahalo 为例审视所谓黑帽搜索优化做法。 | 278 | 68 | 2010-01-24 |
| 9 | [How Do You Look When Merging Fails](https://news.ycombinator.com/item?id=1039984) | 用合并失败的情境呈现版本控制中的窘态。 | 269 | 30 | 2010-01-08 |
| 10 | [A successful Git branching model](https://news.ycombinator.com/item?id=1063198) | 介绍一套实践中有效的 Git 分支管理模型。 | 268 | 44 | 2010-01-19 |
| 11 | [Balsamiq Makes 1.6 Million with 70% Profit in 2009](https://news.ycombinator.com/item?id=1028418) | Balsamiq 公布 2009 年收入 160 万美元、利润率 70%。 | 262 | 122 | 2010-01-03 |
| 12 | [What boyfriends and girlfriends search for on Google](https://news.ycombinator.com/item?id=1043476) | 观察恋爱中的男女朋友在 Google 搜索什么。 | 262 | 97 | 2010-01-10 |
| 13 | [Pure CSS new 3D effect](https://news.ycombinator.com/item?id=1077484) | 展示纯 CSS 实现的新三维视觉效果。 | 252 | 28 | 2010-01-26 |
| 14 | [Gordon: An open source Flash runtime written in pure JavaScript](https://news.ycombinator.com/item?id=1050482) | 介绍用纯 JavaScript 编写的开源 Flash 运行时 Gordon。 | 246 | 97 | 2010-01-13 |
| 15 | [Personalized Porn [SFW]](https://news.ycombinator.com/item?id=1057573) | 围绕“个性化色情内容”的概念展开讨论。 | 238 | 62 | 2010-01-16 |
| 16 | [Do you need a co-founder? (Google Docs list)](https://news.ycombinator.com/item?id=1052950) | 通过共享表格帮助寻找联合创始人的人建立联系。 | 230 | 133 | 2010-01-14 |
| 17 | [A Tool to Deceive and Slaughter](https://news.ycombinator.com/item?id=1068575) | 介绍以“欺骗与杀戮的工具”为名的项目。 | 227 | 49 | 2010-01-21 |
| 18 | [Will single founders please stand up?](https://news.ycombinator.com/item?id=1045694) | 邀请独立创始人现身交流。 | 224 | 149 | 2010-01-11 |
| 19 | [JQuery 1.4 released](https://news.ycombinator.com/item?id=1053420) | jQuery 1.4 正式发布。 | 214 | 41 | 2010-01-14 |
| 20 | [How A Great Product Can Be Bad News: Apple, iPad, and the Closed Mac](https://news.ycombinator.com/item?id=1081519) | 反思 iPad 的优秀体验与封闭计算平台之间的关系。 | 213 | 193 | 2010-01-27 |

## 2010-02

有效主帖 10,127 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Automatically followed by abusive ex-husband (and his friends) on Google Buzz](https://news.ycombinator.com/item?id=1120145) | 一位用户称 Google Buzz 自动让施暴前夫及其朋友关注自己。 | 549 | 275 | 2010-02-12 |
| 2 | [A Big Case of Oops](https://news.ycombinator.com/item?id=1153093) | 讲述一次被作者形容为重大失误的事件。 | 395 | 99 | 2010-02-26 |
| 3 | [HTML5 Canvas based fast painting app](https://news.ycombinator.com/item?id=1106720) | 展示基于 HTML5 Canvas 的快速绘画应用。 | 378 | 89 | 2010-02-06 |
| 4 | [Microsoft’s Creative Destruction ](https://news.ycombinator.com/item?id=1100377) | 以“创造性破坏”为主题审视微软。 | 342 | 235 | 2010-02-04 |
| 5 | [I want privacy because I break the law](https://news.ycombinator.com/item?id=1091814) | 作者以自己会违法为由，解释为何需要隐私。 | 320 | 117 | 2010-02-01 |
| 6 | [Nginx, the little Russian web server taking on the giants](https://news.ycombinator.com/item?id=1147166) | 介绍与大型服务器竞争的俄罗斯 Web 服务器 Nginx。 | 318 | 109 | 2010-02-24 |
| 7 | [Facebook makes HipHop for PHP open source](https://news.ycombinator.com/item?id=1095440) | Facebook 将 PHP 加速项目 HipHop 开源。 | 315 | 190 | 2010-02-02 |
| 8 | [Hg Init: a Mercurial tutorial by Joel Spolsky](https://news.ycombinator.com/item?id=1148157) | Joel Spolsky 推出 Mercurial 入门教程 Hg Init。 | 296 | 71 | 2010-02-24 |
| 9 | [Newbie Fashion Tips for Grown-up Men](https://news.ycombinator.com/item?id=1136261) | 为不熟悉穿搭的成年男性提供服装建议。 | 294 | 171 | 2010-02-19 |
| 10 | [The hell that is a restaurant website](https://news.ycombinator.com/item?id=1130419) | 批评餐厅网站给访客查找信息带来的糟糕体验。 | 292 | 92 | 2010-02-17 |
| 11 | [GoDaddy store your passwords in clear and may access your VPS without permission](https://news.ycombinator.com/item?id=1148092) | 指称 GoDaddy 明文存储密码并可能未经许可访问 VPS。 | 288 | 119 | 2010-02-24 |
| 12 | [Simplicity is hard. Let’s go shopping](https://news.ycombinator.com/item?id=1145593) | 以购物为场景探讨实现简洁设计的困难。 | 282 | 99 | 2010-02-23 |
| 13 | [Serious threat to the web in Italy](https://news.ycombinator.com/item?id=1147670) | 关注意大利一项被认为威胁 Web 的动向。 | 282 | 141 | 2010-02-24 |
| 14 | [School used student laptop webcams to spy on them at school and home](https://news.ycombinator.com/item?id=1134022) | 报道称学校利用学生笔记本摄像头监视校内外活动。 | 275 | 157 | 2010-02-18 |
| 15 | [Please Rob Me](https://news.ycombinator.com/item?id=1131613) | 介绍以“来抢我吧”为名的 Please Rob Me 项目。 | 270 | 130 | 2010-02-17 |
| 16 | ["Mad Libs" Style Form Increases Conversion 25-40%](https://news.ycombinator.com/item?id=1151052) | 称填词游戏式表单可使转化率提高 25% 至 40%。 | 270 | 50 | 2010-02-25 |
| 17 | [Think big with a gig: Our experimental fiber network](https://news.ycombinator.com/item?id=1115169) | 介绍以千兆连接为目标的实验性光纤网络。 | 269 | 149 | 2010-02-10 |
| 18 | [If your product is Great, it doesn't need to be Good.](https://news.ycombinator.com/item?id=1111826) | 提出产品若有突出优势，未必需要面面俱到的观点。 | 265 | 78 | 2010-02-09 |
| 19 | [Things I've learned at Google so far](https://news.ycombinator.com/item?id=1092382) | 作者总结进入 Google 后迄今学到的事情。 | 264 | 194 | 2010-02-01 |
| 20 | [AmEx: "We discourage the use of special characters because..."](https://news.ycombinator.com/item?id=1108482) | 关注美国运通不鼓励使用特殊字符的解释。 | 259 | 102 | 2010-02-07 |

## 2010-03

有效主帖 10,811 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [A real person, a lot like you](https://news.ycombinator.com/item?id=1232489) | 以“像你一样的真实的人”为切入点思考人与人的理解。 | 624 | 139 | 2010-03-31 |
| 2 | [New IDE: code bubbles](https://news.ycombinator.com/item?id=1181742) | 介绍采用代码气泡界面的新 IDE。 | 414 | 219 | 2010-03-10 |
| 3 | [Wikileaks: Something is up](https://news.ycombinator.com/item?id=1215692) | 关注 WikiLeaks 出现的异常动向。 | 407 | 116 | 2010-03-24 |
| 4 | [Congratulations Patrick](https://news.ycombinator.com/item?id=1230156) | 社区祝贺 Patrick McKenzie 辞去日本工作、全职经营软件业务。 | 400 | 61 | 2010-03-30 |
| 5 | [Your high IQ will kill your startup](https://news.ycombinator.com/item?id=1166638) | 作者警告过度依赖高智商可能伤害创业。 | 384 | 182 | 2010-03-04 |
| 6 | [Running a Software Business on 5 Hours A Week](https://news.ycombinator.com/item?id=1206649) | 分享每周投入五小时经营软件业务的经验。 | 359 | 78 | 2010-03-20 |
| 7 | [Photoshop CS5's new "Content-aware Fill"](https://news.ycombinator.com/item?id=1215756) | 展示 Photoshop CS5 的新功能“内容识别填充”。 | 325 | 95 | 2010-03-24 |
| 8 | [Hacker News bans Google and all other search engines](https://news.ycombinator.com/item?id=1194421) | 用户发现 HN 阻止搜索引擎抓取，询问站方原因。 | 318 | 120 | 2010-03-15 |
| 9 | [Show HN: I finally released that sheet music app I keep yammering about](https://news.ycombinator.com/item?id=1196055) | 开发者发布此前多次提及的乐谱应用。 | 318 | 112 | 2010-03-16 |
| 10 | [Teal and Orange - Hollywood, Please Stop the Madness](https://news.ycombinator.com/item?id=1193657) | 批评好莱坞电影过度使用青橙配色。 | 314 | 64 | 2010-03-15 |
| 11 | [I was the one who came forward about the Macbook Air](https://news.ycombinator.com/item?id=1160643) | 作者说明自己是站出来谈 MacBook Air 事件的人。 | 310 | 144 | 2010-03-02 |
| 12 | [Ask HN: Fastest way to make $300-400 a month online?](https://news.ycombinator.com/item?id=1171520) | 一位程序员征求快速在网上月赚三四百美元维持生活的办法。 | 304 | 127 | 2010-03-06 |
| 13 | [U.S. must stop spying on WikiLeaks - Details on intimidation attempts](https://news.ycombinator.com/item?id=1220562) | 要求美国停止监视 WikiLeaks，并介绍相关施压尝试。 | 304 | 113 | 2010-03-26 |
| 14 | [A new approach to China: an update](https://news.ycombinator.com/item?id=1211090) | Google 更新其对中国业务采取新措施的进展。 | 286 | 122 | 2010-03-22 |
| 15 | [Garmin Connect team asked to relocate - this is how they declined](https://news.ycombinator.com/item?id=1196996) | Garmin Connect 团队以特别的方式拒绝搬迁要求。 | 281 | 176 | 2010-03-16 |
| 16 | [Vimcasts](https://news.ycombinator.com/item?id=1228779) | 介绍 Vim 教学资源 Vimcasts。 | 277 | 42 | 2010-03-30 |
| 17 | [Solving turnover (unusual dailywtf)](https://news.ycombinator.com/item?id=1201832) | 分享一个处理员工流失问题的另类案例。 | 276 | 96 | 2010-03-18 |
| 18 | [China's instructions on reporting on Google](https://news.ycombinator.com/item?id=1218679) | 关注中国有关报道 Google 的指示。 | 275 | 164 | 2010-03-25 |
| 19 | [I want to compile a C program so simple I can explain all of the assembly](https://news.ycombinator.com/item?id=1195802) | 希望编译一个简单到能解释全部汇编指令的 C 程序。 | 274 | 38 | 2010-03-16 |
| 20 | [Japan: It's Not Funny Anymore](https://news.ycombinator.com/item?id=1173679) | 作者以“再也不好笑了”为题审视日本的问题。 | 261 | 175 | 2010-03-07 |

## 2010-04

有效主帖 10,585 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Thoughts on Flash](https://news.ycombinator.com/item?id=1304310) | 分享对 Flash 技术与平台的看法。 | 962 | 505 | 2010-04-29 |
| 2 | [New iPhone Agreement Bans Flash-to-iPhone Compiler & Others](https://news.ycombinator.com/item?id=1250799) | 新版 iPhone 协议禁止使用 Flash 转 iPhone 编译器等工具。 | 525 | 480 | 2010-04-08 |
| 3 | [Android – Now Ported On The iPhone](https://news.ycombinator.com/item?id=1283780) | Planetbeing 成功将 Android 移植到 iPhone。 | 494 | 121 | 2010-04-22 |
| 4 | [The story BCG offered me $16,000 not to tell](https://news.ycombinator.com/item?id=1257644) | 作者讲述 BCG 曾愿付一万六千美元请其不公开的故事。 | 446 | 210 | 2010-04-11 |
| 5 | [Wikileaks gun camera video of civilians shot in Baghdad 07/12/07](https://news.ycombinator.com/item?id=1241879) | WikiLeaks 公布 2007 年巴格达平民遭射击的机载影像。 | 439 | 278 | 2010-04-05 |
| 6 | [The case of the 500-mile email](https://news.ycombinator.com/item?id=1293652) | 讲述一桩邮件只能发送至五百英里以内的技术故障。 | 434 | 24 | 2010-04-25 |
| 7 | [Steve Jobs Has Just Gone Mad](https://news.ycombinator.com/item?id=1252791) | 作者以“Steve Jobs 疯了”为题批评其决定。 | 410 | 228 | 2010-04-09 |
| 8 | [An apology...](https://news.ycombinator.com/item?id=1278409) | 作者发表一份公开致歉。 | 367 | 189 | 2010-04-20 |
| 9 | [Soldier in Wikileaks video of 2007 Apache attack reveals what happened that day](https://news.ycombinator.com/item?id=1280561) | 一名士兵讲述 WikiLeaks 所披露阿帕奇攻击当天的情况。 | 361 | 106 | 2010-04-20 |
| 10 | [Booted out of Bootup Labs](https://news.ycombinator.com/item?id=1266723) | 作者讲述被 Bootup Labs 请出的经历。 | 345 | 158 | 2010-04-15 |
| 11 | [How I got sued by Facebook](https://news.ycombinator.com/item?id=1243159) | 作者回顾自己如何遭到 Facebook 起诉。 | 336 | 80 | 2010-04-05 |
| 12 | [The Thrill of Flying the SR-71 Blackbird](https://news.ycombinator.com/item?id=1247709) | 分享驾驶 SR-71 黑鸟侦察机的震撼体验。 | 333 | 87 | 2010-04-07 |
| 13 | [Steve Jobs’ response on Section 3.3.1](https://news.ycombinator.com/item?id=1255858) | Steve Jobs 回应 iPhone 协议第 3.3.1 条引发的争议。 | 320 | 172 | 2010-04-10 |
| 14 | [Best Writing Advice for Engineers I've Ever Seen.](https://news.ycombinator.com/item?id=1244397) | 推荐一份面向工程师的写作建议。 | 318 | 73 | 2010-04-06 |
| 15 | [HTML5 presentation](https://news.ycombinator.com/item?id=1272481) | 分享介绍 HTML5 的演示文稿。 | 316 | 57 | 2010-04-17 |
| 16 | [HP Buying Palm For $1.2 Billion](https://news.ycombinator.com/item?id=1302538) | 惠普宣布以十二亿美元收购 Palm。 | 313 | 143 | 2010-04-28 |
| 17 | [How Not to copy your SSH private key to your servers](https://news.ycombinator.com/item?id=1276760) | 提醒用户不要以不恰当方式把 SSH 私钥复制到服务器。 | 309 | 72 | 2010-04-19 |
| 18 | [Jobs on Flash: Hypocrisy So Thick You Could Cut it with a Knife](https://news.ycombinator.com/item?id=1305346) | 作者批评 Jobs 关于 Flash 的说法自相矛盾。 | 309 | 112 | 2010-04-29 |
| 19 | [We are like prisoners... We do not have a life, only work.](https://news.ycombinator.com/item?id=1265327) | 以“只有工作、没有生活”的陈述关注劳动者处境。 | 293 | 195 | 2010-04-14 |
| 20 | [The real reason why Steve Jobs hates Flash](https://news.ycombinator.com/item?id=1307681) | 作者提出对 Steve Jobs 排斥 Flash 原因的解释。 | 286 | 77 | 2010-04-30 |

## 2010-05

有效主帖 11,295 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [A new type of phishing attack. Works on savvy users.](https://news.ycombinator.com/item?id=1376075) | 介绍一种连熟练用户也可能中招的新型钓鱼攻击。 | 491 | 114 | 2010-05-25 |
| 2 | [_why: A Tale Of A Post-Modern Genius](https://news.ycombinator.com/item?id=1350583) | 以“后现代天才”为视角讲述 _why 的故事。 | 382 | 179 | 2010-05-15 |
| 3 | [I just launched my bootstrapped startup. Pray for me.](https://news.ycombinator.com/item?id=1336406) | 一位自筹资金的创业者终于上线产品，并向社区寻求鼓励。 | 362 | 247 | 2010-05-11 |
| 4 | [Arrington : "You’re Welcome, You Bastards"](https://news.ycombinator.com/item?id=1345322) | Arrington 以强烈措辞发表一番“感谢”。 | 360 | 112 | 2010-05-13 |
| 5 | [Tynt, the Copy/Paste Jerks](https://news.ycombinator.com/item?id=1386772) | 作者批评 Tynt 对复制粘贴行为的干预。 | 357 | 113 | 2010-05-28 |
| 6 | [Google Prediction API](https://news.ycombinator.com/item?id=1362289) | 介绍 Google Prediction API。 | 355 | 81 | 2010-05-19 |
| 7 | [Facebook Tries to Make Violations of Terms of Use Into Criminal Violations](https://news.ycombinator.com/item?id=1319054) | 批评 Facebook 试图将违反使用条款变成刑事违法。 | 340 | 153 | 2010-05-04 |
| 8 | [Those Aren’t Fighting Words, Dear ](https://news.ycombinator.com/item?id=1355266) | 围绕哪些话语构成挑衅展开辨析。 | 325 | 115 | 2010-05-17 |
| 9 | [Facebook Privacy Scanner is launched](https://news.ycombinator.com/item?id=1354731) | Facebook 隐私扫描工具正式推出。 | 321 | 59 | 2010-05-17 |
| 10 | [How real-world corruption works](https://news.ycombinator.com/item?id=1379381) | 探讨现实世界中的腐败如何运作。 | 316 | 72 | 2010-05-26 |
| 11 | [Scribd in HTML](https://news.ycombinator.com/item?id=1327459) | 关注 Scribd 采用 HTML 展示内容的变化。 | 315 | 104 | 2010-05-07 |
| 12 | [Today the Dow dropped 1000 points in about ten minutes.](https://news.ycombinator.com/item?id=1325253) | 记录道琼斯指数约十分钟内下跌一千点的异动。 | 310 | 263 | 2010-05-06 |
| 13 | [Perfect email regex finally found](https://news.ycombinator.com/item?id=1387418) | 以“终于找到完美邮箱正则”为题探讨地址验证。 | 310 | 112 | 2010-05-28 |
| 14 | [Major Facebook security hole lets you view your friends’ live chats](https://news.ycombinator.com/item?id=1321065) | 披露 Facebook 漏洞可让用户查看好友的实时聊天。 | 301 | 61 | 2010-05-05 |
| 15 | [Scribd CTO: “We Are Scrapping Flash And Betting The Company On HTML5″ ](https://news.ycombinator.com/item?id=1322768) | Scribd CTO 宣布放弃 Flash，将公司押注于 HTML5。 | 299 | 120 | 2010-05-05 |
| 16 | [Play PacMan at google.com Now.](https://news.ycombinator.com/item?id=1367518) | Google 首页提供可直接游玩的吃豆人游戏。 | 298 | 91 | 2010-05-21 |
| 17 | [Diaspora's Curse - Jason Fried](https://news.ycombinator.com/item?id=1353587) | Jason Fried 思考 Diaspora 项目面临的难题。 | 296 | 138 | 2010-05-17 |
| 18 | [Drive: The surprising truth about what motivates us](https://news.ycombinator.com/item?id=1357390) | 介绍《Drive》对人类行为动机的探讨。 | 293 | 41 | 2010-05-18 |
| 19 | [What To Do With Your Millions](https://news.ycombinator.com/item?id=1385356) | 讨论拥有数百万财富后应如何安排。 | 291 | 89 | 2010-05-28 |
| 20 | [PhD Student gets quadrotor helicopter moving aggressively](https://news.ycombinator.com/item?id=1387043) | 一名博士生展示让四旋翼直升机快速灵活飞行的成果。 | 281 | 100 | 2010-05-28 |

## 2010-06

有效主帖 10,947 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Where can I fly for how much?](https://news.ycombinator.com/item?id=1421381) | 围绕目的地与票价探索“能花多少钱飞到哪里”。 | 668 | 106 | 2010-06-10 |
| 2 | [To Paul Graham](https://news.ycombinator.com/item?id=1398250) | 一位读者致信 Paul Graham，表达对 HN 简洁设计的看法。 | 647 | 152 | 2010-06-02 |
| 3 | [Hacker Monthly #1 is here](https://news.ycombinator.com/item?id=1394526) | 第一期《Hacker Monthly》正式推出。 | 641 | 177 | 2010-06-01 |
| 4 | [Why I Sold Zappos](https://news.ycombinator.com/item?id=1409858) | 作者解释自己出售 Zappos 的原因。 | 526 | 88 | 2010-06-07 |
| 5 | [Banana equivalent dose](https://news.ycombinator.com/item?id=1429524) | 介绍用香蕉作参照衡量辐射的“香蕉等效剂量”。 | 470 | 84 | 2010-06-14 |
| 6 | [Save My Life - help a fellow HN'er](https://news.ycombinator.com/item?id=1399450) | 呼吁帮助一位生命处境危急的 HN 成员。 | 455 | 316 | 2010-06-02 |
| 7 | [How to make McDonalds french fries](https://news.ycombinator.com/item?id=1408561) | 分享复刻麦当劳薯条的做法。 | 396 | 93 | 2010-06-06 |
| 8 | [Ask HN: What were your naivetés in your twenties?](https://news.ycombinator.com/item?id=1474094) | 邀请年长读者回顾二十多岁时的天真想法。 | 391 | 263 | 2010-06-30 |
| 9 | [Introducing Google Command line Tool](https://news.ycombinator.com/item?id=1443114) | 介绍 Google 命令行工具。 | 390 | 51 | 2010-06-18 |
| 10 | [No, really, pi is wrong: The Tau Manifesto (Tau Day, 2010)](https://news.ycombinator.com/item?id=1468341) | 《Tau 宣言》主张使用 τ 代替 π 作为基础圆常数。 | 367 | 147 | 2010-06-28 |
| 11 | [U.S. Discovers Est. $1 Trillion of Minerals in Afghanistan](https://news.ycombinator.com/item?id=1428589) | 美国宣布在阿富汗发现估值约一万亿美元的矿产资源。 | 354 | 218 | 2010-06-14 |
| 12 | [Unix toolbox](https://news.ycombinator.com/item?id=1411075) | 整理 UNIX 常用工具与操作方法。 | 333 | 23 | 2010-06-07 |
| 13 | [Google Checkout Nightmare and the $126,000 phone call](https://news.ycombinator.com/item?id=1432107) | 一位商户称 Google Checkout 扣留十二万六千美元款项。 | 330 | 118 | 2010-06-15 |
| 14 | [Antenna designer writes about the iPhone 4](https://news.ycombinator.com/item?id=1459728) | 一位天线设计师分析 iPhone 4。 | 327 | 69 | 2010-06-25 |
| 15 | [How To Become a Millionaire In Three Years](https://news.ycombinator.com/item?id=1449688) | 作者分享三年成为百万富翁的思路。 | 322 | 73 | 2010-06-21 |
| 16 | [Ask HN: How to become a millionaire in 3 years?](https://news.ycombinator.com/item?id=1447428) | 读者征求三年内积累一百万美元净资产的办法。 | 313 | 134 | 2010-06-20 |
| 17 | [YouTube wins case against Viacom](https://news.ycombinator.com/item?id=1456216) | YouTube 在与 Viacom 的诉讼中获胜。 | 313 | 43 | 2010-06-23 |
| 18 | [After 15 years of practice..](https://news.ycombinator.com/item?id=1434064) | 作者以十五年的练习经历为背景分享体会。 | 310 | 97 | 2010-06-15 |
| 19 | [There Are No Famous Programmers](https://news.ycombinator.com/item?id=1413497) | 作者提出“没有著名程序员”的观察。 | 303 | 196 | 2010-06-08 |
| 20 | [How I "hacked" Dustin Curtis's Posterous.](https://news.ycombinator.com/item?id=1441997) | 作者称通过伪造发件地址向 Dustin Curtis 的 Posterous 发帖。 | 298 | 115 | 2010-06-18 |

## 2010-07

有效主帖 11,038 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [The Top Idea in Your Mind ](https://news.ycombinator.com/item?id=1536356) | 探讨占据脑海首位的想法如何影响注意力。 | 650 | 191 | 2010-07-21 |
| 2 | [Drowning Doesn't Look Like Drowning](https://news.ycombinator.com/item?id=1492835) | 提醒读者真实的溺水表现可能与想象不同。 | 611 | 127 | 2010-07-06 |
| 3 | [Wikileaks To Leak 5000 Open Source Java Projects](https://news.ycombinator.com/item?id=1555688) | 以“泄露五千个开源 Java 项目”的说法呈现 WikiLeaks 话题。 | 487 | 126 | 2010-07-28 |
| 4 | [The Acceleration of Addictiveness](https://news.ycombinator.com/item?id=1549363) | 探讨产品与内容的成瘾性如何不断增强。 | 470 | 269 | 2010-07-26 |
| 5 | [How to Lose Time and Money](https://news.ycombinator.com/item?id=1492475) | 讨论让人损失时间与金钱的做法。 | 467 | 175 | 2010-07-06 |
| 6 | [Ask HN:  Does reading HN ever make you feel like shit?](https://news.ycombinator.com/item?id=1537461) | 一位用户询问阅读 HN 是否也会让他人产生自卑感。 | 441 | 202 | 2010-07-22 |
| 7 | [Told to remove blog posts describing patented algorithm](https://news.ycombinator.com/item?id=1496683) | 作者被要求删除介绍已获专利算法的博客文章。 | 429 | 147 | 2010-07-08 |
| 8 | [How to Destroy Someone's Life or They called me a child pornographer](https://news.ycombinator.com/item?id=1531004) | 作者讲述被指为儿童色情传播者后遭受的伤害。 | 428 | 210 | 2010-07-20 |
| 9 | [Growing Number of Prosecutions for Videotaping the Police](https://news.ycombinator.com/item?id=1531613) | 关注因拍摄警察执法视频而遭起诉的案例增加。 | 398 | 114 | 2010-07-20 |
| 10 | [One of the most amazing physics engines I’ve ever seen](https://news.ycombinator.com/item?id=1532071) | 展示一款令作者赞叹的物理引擎。 | 377 | 49 | 2010-07-20 |
| 11 | [Will it optimize?](https://news.ycombinator.com/item?id=1540567) | 以“编译器会优化吗”为问题审视优化行为。 | 357 | 59 | 2010-07-23 |
| 12 | [My loss](https://news.ycombinator.com/item?id=1484602) | 作者分享自己经历的一次失去。 | 348 | 105 | 2010-07-03 |
| 13 | [I assume I'm below average](https://news.ycombinator.com/item?id=1480002) | 作者谈将自己视作低于平均水平的思考方式。 | 340 | 106 | 2010-07-02 |
| 14 | [Now legal in the U.S.: Jailbreaking your iPhone, ripping a DVD for education](https://news.ycombinator.com/item?id=1548378) | 美国新规允许 iPhone 越狱及为教育用途提取 DVD 内容。 | 325 | 85 | 2010-07-26 |
| 15 | [Google agrees to buy ITA Software for $700 million](https://news.ycombinator.com/item?id=1479107) | Google 同意以七亿美元收购 ITA Software。 | 316 | 121 | 2010-07-01 |
| 16 | [Woot To The AP: Nice Story About Our Sale — You Now Owe Us $17.50](https://news.ycombinator.com/item?id=1490284) | Woot 要求美联社为引用其出售消息支付 17.50 美元。 | 314 | 46 | 2010-07-06 |
| 17 | [Everyone Who Tried to Convince Me to Use Vim Was Wrong](https://news.ycombinator.com/item?id=1556835) | 作者反思别人劝自己使用 Vim 时给出的理由。 | 309 | 208 | 2010-07-29 |
| 18 | [I am doing a startup (putting virtual machines on the web)](https://news.ycombinator.com/item?id=1534973) | 作者宣布创业，尝试把虚拟机放到 Web 上。 | 299 | 103 | 2010-07-21 |
| 19 | [Too many laws, too many prisoners](https://news.ycombinator.com/item?id=1541942) | 批评法律过多与囚犯过多的问题。 | 293 | 167 | 2010-07-23 |
| 20 | [What's wrong with 1975 programming](https://news.ycombinator.com/item?id=1554656) | 反思沿用 1975 年式编程方式存在的局限。 | 293 | 115 | 2010-07-28 |

## 2010-08

有效主帖 11,750 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Keep calm & carry on: What you didn't know about the reddit story](https://news.ycombinator.com/item?id=1571427) | 补充 Reddit 一则故事背后不为人知的情况。 | 776 | 83 | 2010-08-03 |
| 2 | [P ≠ NP](https://news.ycombinator.com/item?id=1585850) | 关注一项关于 P 是否等于 NP 的数学主张。 | 740 | 208 | 2010-08-08 |
| 3 | [Google Kills Wave](https://news.ycombinator.com/item?id=1575892) | Google 宣布停止发展 Wave。 | 712 | 237 | 2010-08-04 |
| 4 | [What Happened to Yahoo](https://news.ycombinator.com/item?id=1596607) | 回顾雅虎经历的变化与问题。 | 688 | 270 | 2010-08-11 |
| 5 | [My Thoughts on Oracle v Google](https://news.ycombinator.com/item?id=1607210) | 作者分享对 Oracle 起诉 Google 的看法。 | 606 | 82 | 2010-08-16 |
| 6 | [Why GNU grep is Fast](https://news.ycombinator.com/item?id=1626305) | 解释 GNU grep 为什么运行得快。 | 512 | 115 | 2010-08-23 |
| 7 | [Welcome to the new decade](https://news.ycombinator.com/item?id=1604504) | 以“欢迎来到新十年”为题观察时代变化。 | 486 | 158 | 2010-08-15 |
| 8 | [A letter to my students](https://news.ycombinator.com/item?id=1631682) | 分享作者写给学生的一封信。 | 462 | 169 | 2010-08-25 |
| 9 | [Oracle sues Google over use of Java in Android](https://news.ycombinator.com/item?id=1599584) | Oracle 因 Android 使用 Java 起诉 Google。 | 452 | 326 | 2010-08-13 |
| 10 | ["My husband is a programmer; I have no idea what that means."](https://news.ycombinator.com/item?id=1595950) | 以配偶不了解程序员工作为切入点观察职业沟通。 | 417 | 144 | 2010-08-11 |
| 11 | [Common Programmer Health Problems](https://news.ycombinator.com/item?id=1585085) | 整理程序员常见的健康问题。 | 394 | 184 | 2010-08-08 |
| 12 | [Wired's bullshit "The web is dead" graph](https://news.ycombinator.com/item?id=1611648) | 作者批评《连线》支持“Web 已死”判断的图表。 | 394 | 73 | 2010-08-17 |
| 13 | [Rails 3.0: It's ready](https://news.ycombinator.com/item?id=1644876) | Rails 3.0 正式发布。 | 385 | 65 | 2010-08-29 |
| 14 | [Hey, Guys, It's Totally Okay If You Don't Get Rich](https://news.ycombinator.com/item?id=1601281) | 提醒读者没有变得富有也完全可以接受。 | 383 | 219 | 2010-08-13 |
| 15 | [Regrets of the Dying](https://news.ycombinator.com/item?id=1643239) | 回顾临终者常表达的人生遗憾。 | 371 | 90 | 2010-08-29 |
| 16 | [What happens when you give homeless people a prepaid credit card. ](https://news.ycombinator.com/item?id=1643318) | 记录给无家可归者预付信用卡后发生的事情。 | 369 | 242 | 2010-08-29 |
| 17 | [Valedictorian Speaks Out Against Schooling in Graduation Speech](https://news.ycombinator.com/item?id=1573636) | 一位毕业生代表在毕业演讲中公开批评学校教育。 | 360 | 207 | 2010-08-04 |
| 18 | [This document is confidential ](https://news.ycombinator.com/item?id=1612676) | 围绕一份标注为机密的文件展开关注。 | 358 | 44 | 2010-08-17 |
| 19 | [Kind reminder: please (re)read the HN guidelines](https://news.ycombinator.com/item?id=1646871) | 再次提醒社区成员阅读 Hacker News 参与准则。 | 353 | 133 | 2010-08-30 |
| 20 | [Bill Gates Enrolls His Kids In Khan Academy](https://news.ycombinator.com/item?id=1646215) | 报道 Bill Gates 让孩子使用可汗学院学习。 | 344 | 93 | 2010-08-30 |

## 2010-09

有效主帖 12,404 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [So A Blogger Walks Into A Bar… ](https://news.ycombinator.com/item?id=1714377) | 以博主走进酒吧的情境展开一则故事。 | 1098 | 232 | 2010-09-21 |
| 2 | [Asteroids JavaScript Bookmarklet to blow up any web site](https://news.ycombinator.com/item?id=1737276) | JavaScript 书签工具让用户像玩《小行星》一样摧毁网页。 | 684 | 74 | 2010-09-28 |
| 3 | [Ron Conway Drops A Nuclear Bomb On The Super Angels](https://news.ycombinator.com/item?id=1722384) | Ron Conway 对“超级天使”投资人作出激烈回应。 | 558 | 206 | 2010-09-24 |
| 4 | [What Happens At Y Combinator](https://news.ycombinator.com/item?id=1733236) | 介绍参加 Y Combinator 期间会经历什么。 | 549 | 143 | 2010-09-27 |
| 5 | [Bribing maitre d' to skip the line](https://news.ycombinator.com/item?id=1653891) | 探讨通过给餐厅领位员小费来跳过排队的做法。 | 529 | 177 | 2010-09-01 |
| 6 | [Start ups, please don't force me to log in with Facebook](https://news.ycombinator.com/item?id=1732411) | 用户呼吁创业公司提供 Facebook 登录之外的认证选择。 | 508 | 266 | 2010-09-27 |
| 7 | [Apple Relaxes iOS Restrictions On Development Tools, Publishes Review Guidelines](https://news.ycombinator.com/item?id=1675131) | 苹果放宽 iOS 开发工具限制，并公开应用审核准则。 | 464 | 229 | 2010-09-09 |
| 8 | [What happens when you refuse to answer a passport control officer's questions](https://news.ycombinator.com/item?id=1681721) | 讲述拒绝回答护照检查人员问题后发生的事情。 | 463 | 281 | 2010-09-11 |
| 9 | [Design for Hackers: Why Monet Never Used Black, & Why You Shouldn't Either](https://news.ycombinator.com/item?id=1736055) | 借莫奈不用黑色的说法，为技术人员解释配色设计。 | 428 | 76 | 2010-09-28 |
| 10 | [Paypal is holding over 600,000 euros from the minecraft developer](https://news.ycombinator.com/item?id=1678582) | 报道称 PayPal 扣留 Minecraft 开发者逾六十万欧元资金。 | 418 | 169 | 2010-09-10 |
| 11 | [Evercookie: A cookie that undeletes itself from 8 different storages](https://news.ycombinator.com/item?id=1714446) | Evercookie 将数据写入多种存储位置，使 Cookie 删除后重现。 | 391 | 108 | 2010-09-21 |
| 12 | [Bill Gates: "Someone decided to trash the one part of Windows that was usable?"](https://news.ycombinator.com/item?id=1660096) | Bill Gates 对 Windows 可用部分遭改动的言论引发关注。 | 375 | 212 | 2010-09-03 |
| 13 | [How to keep someone with you forever](https://news.ycombinator.com/item?id=1677013) | 围绕如何让一个人永远留在自己身边展开思考。 | 372 | 95 | 2010-09-09 |
| 14 | [Google Instant Search Released](https://news.ycombinator.com/item?id=1672391) | Google 发布即时搜索功能。 | 371 | 216 | 2010-09-08 |
| 15 | [IPhone vs Android? No. We're fighting the wrong fight](https://news.ycombinator.com/item?id=1690789) | 作者质疑 iPhone 与 Android 之争是否抓住了真正问题。 | 366 | 157 | 2010-09-14 |
| 16 | [Leaving .net](https://news.ycombinator.com/item?id=1719277) | 作者讲述离开 .NET 技术体系的决定。 | 355 | 213 | 2010-09-23 |
| 17 | [Bill Gates, Hero](https://news.ycombinator.com/item?id=1694538) | 用户感叹 Bill Gates 从受批评对象转变为英雄的形象变化。 | 351 | 227 | 2010-09-15 |
| 18 | [I’m done building Facebook apps for clients](https://news.ycombinator.com/item?id=1731427) | 作者宣布不再替客户开发 Facebook 应用。 | 348 | 76 | 2010-09-27 |
| 19 | [There is a Horse in the Apple Store](https://news.ycombinator.com/item?id=1661831) | 记录一匹马出现在苹果商店的场景。 | 338 | 112 | 2010-09-04 |
| 20 | [Thanks For Paying Taxes. Here's A Receipt.](https://news.ycombinator.com/item?id=1745133) | 用收据形式展示纳税人的钱被如何使用。 | 331 | 181 | 2010-09-30 |

## 2010-10

有效主帖 13,745 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Firesheep: Easy HTTP session hijacking from within Firefox](https://news.ycombinator.com/item?id=1827928) | 介绍能在 Firefox 中方便劫持 HTTP 会话的 Firesheep。 | 714 | 341 | 2010-10-25 |
| 2 | [Thank HN: 7 months ago, I asked for help. Now I've got 5 employees.](https://news.ycombinator.com/item?id=1772205) | 曾求助生活费的用户感谢 HN，七个月后已雇用五名员工。 | 620 | 114 | 2010-10-08 |
| 3 | [WePay Drops 600lbs of ice in front of PayPal Conference](https://news.ycombinator.com/item?id=1834976) | WePay 在 PayPal 会议前放置六百磅冰块进行宣传。 | 605 | 161 | 2010-10-26 |
| 4 | [The reverse job applicant](https://news.ycombinator.com/item?id=1806911) | 分享一种颠倒传统求职方式的案例。 | 518 | 302 | 2010-10-19 |
| 5 | [Amazon AWS Free Usage Tier](https://news.ycombinator.com/item?id=1816773) | AWS 推出免费使用额度。 | 479 | 137 | 2010-10-21 |
| 6 | [Tell HN: Please continue offering your services (goods, rooms etc)](https://news.ycombinator.com/item?id=1840143) | 用户主张继续允许社区成员发布服务与物品援助信息。 | 461 | 31 | 2010-10-27 |
| 7 | [Show HN: I asked an HN member for feedback and she blew my mind](https://news.ycombinator.com/item?id=1836538) | 一位创业者分享 HN 成员为其网站文案提供的详尽反馈。 | 453 | 120 | 2010-10-26 |
| 8 | [Google Cars Drive Themselves, in Traffic](https://news.ycombinator.com/item?id=1775584) | Google 自动驾驶汽车开始在真实交通中行驶。 | 436 | 205 | 2010-10-09 |
| 9 | [Resignation letter from Microsoft Employee](https://news.ycombinator.com/item?id=1795141) | 分享一位微软员工的辞职信。 | 433 | 105 | 2010-10-15 |
| 10 | [Paul Buchheit: Serendipity finds you](https://news.ycombinator.com/item?id=1826666) | Paul Buchheit 探讨意外机遇如何出现。 | 421 | 54 | 2010-10-24 |
| 11 | [Tell HN: Please stop offering your services](https://news.ycombinator.com/item?id=1839723) | 用户认为大规模发布服务推介不可持续，呼吁停止此类帖子。 | 406 | 106 | 2010-10-27 |
| 12 | [Land of Lisp is finally out...and has a music video.](https://news.ycombinator.com/item?id=1836935) | 《Land of Lisp》正式发行，并配有音乐视频。 | 398 | 108 | 2010-10-27 |
| 13 | [Apple deprecates Java](https://news.ycombinator.com/item?id=1814613) | 苹果将 Java 标记为弃用。 | 386 | 268 | 2010-10-21 |
| 14 | [Engineer saves man by crashing into him on purpose](https://news.ycombinator.com/item?id=1823419) | 一位工程师故意撞向他人以挽救对方生命。 | 383 | 70 | 2010-10-23 |
| 15 | [After 4 years of self-funded coding marathons I feel "finished", care to talk?](https://news.ycombinator.com/item?id=1817883) | 一位自费创业四年的程序员陷入低谷，向社区寻求支持。 | 379 | 184 | 2010-10-21 |
| 16 | [PayPal robbed my bank account](https://news.ycombinator.com/item?id=1802801) | 作者指称 PayPal 擅自从其银行账户取款。 | 378 | 185 | 2010-10-18 |
| 17 | [How Fake Money Saved Brazil](https://news.ycombinator.com/item?id=1757716) | 讲述一种“假货币”如何帮助巴西应对经济问题。 | 377 | 131 | 2010-10-04 |
| 18 | [Why Wesabe Lost to Mint](https://news.ycombinator.com/item?id=1746832) | 分析个人财务服务 Wesabe 为何败给 Mint。 | 373 | 195 | 2010-10-01 |
| 19 | [What We Look for in Founders](https://news.ycombinator.com/item?id=1820561) | 介绍投资或筛选创始人时看重的特质。 | 362 | 174 | 2010-10-22 |
| 20 | [Rollover image on your website? That will be $80,000 (please)](https://news.ycombinator.com/item?id=1791718) | 关注网站鼠标悬停图像效果遭索赔八万美元的事件。 | 352 | 177 | 2010-10-14 |

## 2010-11

有效主帖 13,945 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Google Beatbox](https://news.ycombinator.com/item?id=1952356) | 分享名为 Google Beatbox 的声音玩法。 | 1028 | 96 | 2010-11-29 |
| 2 | [The day Steve Jobs dissed me hard](https://news.ycombinator.com/item?id=1896189) | 作者回忆被 Steve Jobs 当面严厉奚落的一天。 | 567 | 122 | 2010-11-12 |
| 3 | [How Israel handles airport security](https://news.ycombinator.com/item?id=1907890) | 介绍以色列处理机场安检的方式。 | 550 | 162 | 2010-11-15 |
| 4 | [Gmail: Trap my contacts now (warning when exporting contacts to Facebook)](https://news.ycombinator.com/item?id=1890164) | 关注 Gmail 在用户向 Facebook 导出联系人时显示的提醒。 | 470 | 169 | 2010-11-10 |
| 5 | [Re-entry to US without backscatter or pat-down](https://news.ycombinator.com/item?id=1931688) | 讲述未接受背散射扫描或拍身检查而重返美国的经历。 | 459 | 179 | 2010-11-22 |
| 6 | [Remind HN: Vote](https://news.ycombinator.com/item?id=1859796) | 在美国选举日提醒读者抽空行使投票权。 | 454 | 382 | 2010-11-02 |
| 7 | [Son, as soon as someone puts their hands on you...](https://news.ycombinator.com/item?id=1895057) | 以父亲对儿子谈身体接触界限的话语展开叙事。 | 443 | 354 | 2010-11-11 |
| 8 | [Google and Microsoft Cheat on Slow-Start. Should You?](https://news.ycombinator.com/item?id=1942442) | 讨论 Google、微软改变 TCP 慢启动行为的做法是否值得效仿。 | 437 | 67 | 2010-11-26 |
| 9 | [When we got to the scanner, I opted out. Then they opted out.](https://news.ycombinator.com/item?id=1910954) | 作者讲述拒绝机场扫描后对方也选择放弃的经历。 | 422 | 184 | 2010-11-16 |
| 10 | [SR-71 Blackbird Communication to Tower](https://news.ycombinator.com/item?id=1930497) | 分享 SR-71 黑鸟侦察机与塔台之间的通信。 | 422 | 68 | 2010-11-22 |
| 11 | [The ~200 Line Linux Kernel Patch That Does Wonders](https://news.ycombinator.com/item?id=1910085) | 介绍一份约两百行、据称明显改善体验的 Linux 内核补丁。 | 420 | 96 | 2010-11-16 |
| 12 | [An Awesome Book](https://news.ycombinator.com/item?id=1916576) | 介绍名为《An Awesome Book》的书。 | 409 | 100 | 2010-11-18 |
| 13 | [Do you read HackerNews all day and never actually do anything?](https://news.ycombinator.com/item?id=1917274) | 用户反思整天读 HN 却没有真正动手做项目的习惯。 | 389 | 142 | 2010-11-18 |
| 14 | [Life Hack - The 30/30 Minute Work Cycle Feels Like Magic](https://news.ycombinator.com/item?id=1888843) | 作者推荐采用三十分钟交替节奏的工作方法。 | 380 | 134 | 2010-11-10 |
| 15 | [Reddit’s Astonishing Altruism](https://news.ycombinator.com/item?id=1901916) | 关注 Reddit 社区展现的利他行为。 | 372 | 125 | 2010-11-13 |
| 16 | [The Myth of the Immortal Hamburger](https://news.ycombinator.com/item?id=1878188) | 检视“汉堡不会腐坏”这一流传的说法。 | 371 | 34 | 2010-11-07 |
| 17 | [Ubuntu To Ditch X Server For Wayland](https://news.ycombinator.com/item?id=1872536) | Ubuntu 计划以 Wayland 替代 X 服务器。 | 369 | 154 | 2010-11-05 |
| 18 | [Kinect reverse-engineered; open driver available](https://news.ycombinator.com/item?id=1891660) | Kinect 被逆向分析，开放驱动可供使用。 | 369 | 85 | 2010-11-10 |
| 19 | [Goodbye, Google App Engine](https://news.ycombinator.com/item?id=1927903) | 一位创业者认为采用 App Engine 是昂贵错误，决定离开。 | 362 | 95 | 2010-11-21 |
| 20 | [This is why sites choose to stay vulnerable to Firesheep](https://news.ycombinator.com/item?id=1880412) | 解释一些网站为何仍未解决 Firesheep 暴露的风险。 | 354 | 139 | 2010-11-07 |

## 2010-12

有效主帖 14,562 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Introducing Word Lens](https://news.ycombinator.com/item?id=2014555) | 介绍翻译应用 Word Lens。 | 1297 | 281 | 2010-12-17 |
| 2 | [Today you, tomorrow me ](https://news.ycombinator.com/item?id=2003515) | 以“今天帮你，明天帮我”的话语呈现互助精神。 | 1270 | 203 | 2010-12-14 |
| 3 | [Salesforce Buys Heroku (YC W08)  For $212 Million In Cash](https://news.ycombinator.com/item?id=1982489) | Salesforce 以 2.12 亿美元现金收购 Heroku。 | 717 | 198 | 2010-12-08 |
| 4 | [Why Do Google Maps’s City Labels Seem So Readable?](https://news.ycombinator.com/item?id=1963612) | 分析 Google 地图城市标签为何容易阅读。 | 687 | 104 | 2010-12-02 |
| 5 | [Sacked by a Google algorithm](https://news.ycombinator.com/item?id=2049105) | 讲述一位用户被 Google 算法影响生计的遭遇。 | 685 | 283 | 2010-12-29 |
| 6 | [Everest is littered with dead, exposed bodies](https://news.ycombinator.com/item?id=1978295) | 关注珠穆朗玛峰上遗留的遇难者遗体。 | 664 | 255 | 2010-12-07 |
| 7 | [Ben the Bodyguard: Gorgeous HTML5 Website](https://news.ycombinator.com/item?id=1961680) | 展示 Ben the Bodyguard 制作精美的 HTML5 网站。 | 586 | 97 | 2010-12-02 |
| 8 | [Google Engineer bails out student in jail](https://news.ycombinator.com/item?id=2036588) | 一位 Google 工程师为被关押学生提供保释帮助。 | 540 | 196 | 2010-12-24 |
| 9 | [What does it feel like to be stupid? An anonymous Quora user explains.](https://news.ycombinator.com/item?id=1990498) | 一位匿名 Quora 用户描述自觉不聪明是什么体验。 | 521 | 149 | 2010-12-10 |
| 10 | [If people tried to pay for other services like they try to pay for programming](https://news.ycombinator.com/item?id=2006458) | 用其他服务类比客户对编程工作的付费方式。 | 503 | 123 | 2010-12-15 |
| 11 | [Cambridge University refuses to censor student's thesis](https://news.ycombinator.com/item?id=2053228) | 剑桥大学拒绝审查一位学生的论文。 | 498 | 61 | 2010-12-30 |
| 12 | [Yahoo is Shutting Down Del.icio.us](https://news.ycombinator.com/item?id=2013248) | 关注雅虎据称将关闭 Delicious 的消息。 | 486 | 293 | 2010-12-16 |
| 13 | [How I Screwed Up My Google Acquisition](https://news.ycombinator.com/item?id=1984084) | 作者复盘自己如何搞砸与 Google 的收购交易。 | 472 | 103 | 2010-12-08 |
| 14 | [Facebook intern visualizes friendships, draws world map](https://news.ycombinator.com/item?id=2002742) | 一位 Facebook 实习生以好友关系数据绘出世界地图。 | 430 | 116 | 2010-12-14 |
| 15 | [Haskell Researchers Announce Discovery of Industry Programmer Who Gives a Shit](https://news.ycombinator.com/item?id=1959782) | 用找到关心 Haskell 的产业程序员这一说法调侃语言推广。 | 429 | 109 | 2010-12-01 |
| 16 | [Hey Yahoo, Can you please open source Delicious?](https://news.ycombinator.com/item?id=2014054) | 向雅虎呼吁开放 Delicious 的源代码。 | 413 | 84 | 2010-12-16 |
| 17 | [Allegations of FBI crypto backdoors in OpenBSD IPSEC](https://news.ycombinator.com/item?id=2006128) | 报道有关 FBI 在 OpenBSD IPsec 中植入后门的指控。 | 395 | 139 | 2010-12-14 |
| 18 | [Tablets](https://news.ycombinator.com/item?id=1959338) | 围绕平板电脑这一类计算设备展开思考。 | 387 | 250 | 2010-12-01 |
| 19 | [Cassandra vs MongoDB vs CouchDB vs Redis vs Riak comparison](https://news.ycombinator.com/item?id=2052852) | 比较 Cassandra、MongoDB、CouchDB、Redis 与 Riak。 | 380 | 89 | 2010-12-30 |
| 20 | [Ask HN: I built a site that just went ridiculously viral. What do I do now?](https://news.ycombinator.com/item?id=2051288) | threewords.me 突然爆红，开发者求助如何应对成本与后续发展。 | 370 | 188 | 2010-12-30 |

## 2011-01

有效主帖 15,898 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Google algorithm change launched](https://news.ycombinator.com/item?id=2152286) | Google 调整算法，旨在降低采集站排名并优先展示原创来源。 | 688 | 183 | 2011-01-28 |
| 2 | [My winter break project — Silk](https://news.ycombinator.com/item?id=2089615) | 开发者展示寒假创作的生成艺术绘画项目 Silk。 | 687 | 88 | 2011-01-10 |
| 3 | [Eric Schmidt: On April 4th I Will Step Down, Larry Page to be CEO](https://news.ycombinator.com/item?id=2125251) | Eric Schmidt 宣布卸任 CEO，由 Larry Page 接任。 | 679 | 150 | 2011-01-20 |
| 4 | [Carnegie Mellon CS Professor challenges Sony by mirroring Geohot's PS3 hacks](https://news.ycombinator.com/item?id=2098247) | 卡内基梅隆教授通过镜像 Geohot 的 PS3 破解内容回应索尼。 | 620 | 81 | 2011-01-12 |
| 5 | [Google tracks you. We don't. An illustrated guide](https://news.ycombinator.com/item?id=2063377) | 一份图文说明对比 Google 的用户追踪与无追踪搜索。 | 588 | 168 | 2011-01-03 |
| 6 | [Oops: No copied Java code or weapons of mass destruction found in Android](https://news.ycombinator.com/item?id=2128825) | 作者反驳 Android 中存在复制 Java 代码的指控。 | 584 | 57 | 2011-01-21 |
| 7 | [Google Removing H.264 Support in Chrome](https://news.ycombinator.com/item?id=2093219) | Google 宣布移除 Chrome 对 H.264 的支持。 | 579 | 349 | 2011-01-11 |
| 8 | [Trouble In the House of Google](https://news.ycombinator.com/item?id=2062855) | 关注 Google 内部面临的问题。 | 461 | 162 | 2011-01-03 |
| 9 | [Steve's story - Google employee #13](https://news.ycombinator.com/item?id=2086628) | 讲述 Google 第十三号员工 Steve 的故事。 | 440 | 89 | 2011-01-09 |
| 10 | [Dear Google: please let me ban sites from results](https://news.ycombinator.com/item?id=2075049) | 用户请求 Google 提供跨浏览器屏蔽指定搜索来源的功能。 | 438 | 208 | 2011-01-06 |
| 11 | [Introducing Amazon Simple Email Service](https://news.ycombinator.com/item?id=2138720) | 亚马逊推出简单邮件服务 SES。 | 438 | 168 | 2011-01-25 |
| 12 | [Yuri Milner, SV Angel Offer Every New Y Combinator Startup $150k](https://news.ycombinator.com/item?id=2154706) | Yuri Milner 与 SV Angel 向每家新 YC 公司提供十五万美元投资。 | 425 | 189 | 2011-01-29 |
| 13 | [Delegate or die: the self-employed trap](https://news.ycombinator.com/item?id=2132591) | 提醒自雇者通过授权分工避免陷入事事亲为的困境。 | 423 | 72 | 2011-01-23 |
| 14 | [For what are the Windows A:\ and B:\ drives used?](https://news.ycombinator.com/item?id=2095628) | 解释 Windows 的 A 盘和 B 盘字母通常用于什么设备。 | 415 | 271 | 2011-01-12 |
| 15 | [Why 3D doesn't work and never will.](https://news.ycombinator.com/item?id=2134906) | 作者提出三维显示行不通、未来也难成功的观点。 | 411 | 198 | 2011-01-24 |
| 16 | [ So Long and Thanks for all the Bits](https://news.ycombinator.com/item?id=2161427) | 作者以“再见，感谢所有比特”为题表达告别。 | 404 | 103 | 2011-01-31 |
| 17 | [JavaScript ( (__ = $ + $)[+$] + ({} + $)[_/_] +({} + $)[_/_] )](https://news.ycombinator.com/item?id=2129745) | 用特殊符号组成的表达式展示 JavaScript 的隐式转换。 | 403 | 46 | 2011-01-22 |
| 18 | [Dating Denial of Service attack](https://news.ycombinator.com/item?id=2065604) | 把约会情境与拒绝服务攻击联系起来展开讨论。 | 390 | 123 | 2011-01-04 |
| 19 | [How (not) to write Factorial in Java](https://news.ycombinator.com/item?id=2143310) | 通过 Java 阶乘实现示例反思代码写法。 | 387 | 199 | 2011-01-26 |
| 20 | [NYT Review of ‘The 4-Hour Body’](https://news.ycombinator.com/item?id=2077312) | 分享《纽约时报》对《The 4-Hour Body》的书评。 | 383 | 203 | 2011-01-06 |

## 2011-02

有效主帖 15,480 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Mea Culpa: GitHub works well, my mistake made them look bad](https://news.ycombinator.com/item?id=2164406) | 作者承认自己的错误让 GitHub 看起来出了问题。 | 704 | 45 | 2011-02-01 |
| 2 | [Google: Bing Is Cheating, Copying Our Search Results](https://news.ycombinator.com/item?id=2165469) | Google 指称 Bing 通过复制自己的搜索结果作弊。 | 684 | 272 | 2011-02-01 |
| 3 | [Money Won’t Buy You Health Insurance](https://news.ycombinator.com/item?id=2247560) | 讲述即使有钱也未必能够买到医疗保险的处境。 | 596 | 423 | 2011-02-21 |
| 4 | [How I Got Kicked Out of Y Combinator and Then Raised $1.5m for My Startup](https://news.ycombinator.com/item?id=2208155) | 作者回顾被 YC 除名后为创业公司融得一百五十万美元的经历。 | 589 | 112 | 2011-02-11 |
| 5 | [Pictures of kittens for use as placeholders in your designs or code](https://news.ycombinator.com/item?id=2271795) | 提供可在设计或代码中用作占位图的小猫照片。 | 569 | 116 | 2011-02-28 |
| 6 | [Man with ALS writes patch for Gnome using morse code (with touching story)](https://news.ycombinator.com/item?id=2266924) | 一位 ALS 患者通过摩尔斯码输入，为 GNOME 编写补丁。 | 543 | 32 | 2011-02-27 |
| 7 | ["You've angered the hive"](https://news.ycombinator.com/item?id=2189907) | 以“你激怒了蜂群”为题呈现群体反应。 | 521 | 214 | 2011-02-07 |
| 8 | [Nokia CEO: Nokia is "standing on a burning platform"](https://news.ycombinator.com/item?id=2195520) | 诺基亚 CEO 将公司比作站在燃烧的平台上。 | 513 | 196 | 2011-02-09 |
| 9 | [Microsoft’s Bing uses Google search results—and denies it](https://news.ycombinator.com/item?id=2167875) | 文章指称 Bing 使用 Google 搜索结果，而微软予以否认。 | 511 | 196 | 2011-02-01 |
| 10 | [New Chrome extension: block sites from Google’s web search results](https://news.ycombinator.com/item?id=2218382) | 介绍可从 Google 搜索结果中屏蔽网站的 Chrome 扩展。 | 508 | 214 | 2011-02-14 |
| 11 | [Cached OkCupid Article: Why You Should Never Pay For Online Dating](https://news.ycombinator.com/item?id=2170998) | 分享 OkCupid 主张不应为在线约会付费的文章缓存。 | 490 | 80 | 2011-02-02 |
| 12 | [I'm a designer who learned Django and launched her first webapp in 6 weeks](https://news.ycombinator.com/item?id=2227770) | 一位设计师分享学习 Django 并在六周内发布首个 Web 应用的经历。 | 490 | 120 | 2011-02-16 |
| 13 | [How we fed ourselves for a year & sold a startup...with only 300 lines of code](https://news.ycombinator.com/item?id=2222522) | 作者分享凭三百行代码维持一年生计并出售项目的经历。 | 488 | 109 | 2011-02-15 |
| 14 | [ I'm a pregnant hacker. Please review my side project.](https://news.ycombinator.com/item?id=2175757) | 一位怀孕的技术开发者邀请社区评价自己的业余项目。 | 485 | 179 | 2011-02-03 |
| 15 | [An Open Letter to Apple on the Readability App rejection](https://news.ycombinator.com/item?id=2245692) | 一封就 Readability 应用遭拒致苹果的公开信。 | 478 | 199 | 2011-02-21 |
| 16 | [Guy commits his genome to Github, smartass forks and issues a pull request](https://news.ycombinator.com/item?id=2211928) | 有人把基因组提交到 GitHub，引来分支与拉取请求玩笑。 | 476 | 72 | 2011-02-13 |
| 17 | [Show HN: Our new $149 hackable Bluetooth wristwatch ](https://news.ycombinator.com/item?id=2221579) | 展示售价 149 美元、可供改造的蓝牙腕表。 | 460 | 143 | 2011-02-15 |
| 18 | [Isotope - An exquisite jQuery plugin for magical layouts](https://news.ycombinator.com/item?id=2189251) | 介绍用于动态网页布局的 jQuery 插件 Isotope。 | 459 | 58 | 2011-02-07 |
| 19 | [Don't waste your time by cd-ing in the terminal](https://news.ycombinator.com/item?id=2237595) | 分享减少在终端中反复使用 cd 切换目录的办法。 | 449 | 118 | 2011-02-18 |
| 20 | [How one man tracked down Anonymous—and paid a heavy price ](https://news.ycombinator.com/item?id=2200720) | 讲述一名追查 Anonymous 的人如何付出沉重代价。 | 432 | 155 | 2011-02-10 |

## 2011-03

有效主帖 18,360 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Patio11 says Hello Ladies](https://news.ycombinator.com/item?id=2371965) | 以 Patio11 向女士问好的情境呈现个人故事。 | 699 | 114 | 2011-03-26 |
| 2 | [My fellow geeks, we need to have a talk.](https://news.ycombinator.com/item?id=2322696) | 作者向技术同好提出一场需要认真进行的对话。 | 697 | 238 | 2011-03-14 |
| 3 | [I took "abusing the HTML5 History" to the next level.](https://news.ycombinator.com/item?id=2301801) | 开发者展示受滥用 HTML5 历史记录启发的进一步实验。 | 681 | 62 | 2011-03-08 |
| 4 | [8.9 earthquake hits Japan](https://news.ycombinator.com/item?id=2312474) | 日本发生里氏 8.9 级地震。 | 678 | 254 | 2011-03-11 |
| 5 | [Patio11's perspective on the Japan Earthquake](https://news.ycombinator.com/item?id=2319629) | Patio11 分享对日本地震的亲身观察。 | 673 | 108 | 2011-03-13 |
| 6 | [Firefox 4 is here](https://news.ycombinator.com/item?id=2354354) | Firefox 4 正式发布。 | 670 | 345 | 2011-03-22 |
| 7 | [How to damage your brand in one smooth shot - Way to GoDaddy](https://news.ycombinator.com/item?id=2392542) | 作者用 GoDaddy 的行为举例说明如何损害品牌。 | 619 | 320 | 2011-03-31 |
| 8 | [Subject: Airbnb](https://news.ycombinator.com/item?id=2337093) | 分享以 Airbnb 为主题的通信内容。 | 614 | 134 | 2011-03-17 |
| 9 | [Entreporn, The Fallacy That Wastes Your Life](https://news.ycombinator.com/item?id=2337745) | 批评沉迷创业成功故事而耗费人生的现象。 | 607 | 227 | 2011-03-17 |
| 10 | [Everything You Know About Fitness is a Lie](https://news.ycombinator.com/item?id=2287213) | 作者挑战读者对健身的常见认识。 | 592 | 353 | 2011-03-04 |
| 11 | [At work? Try this Hacker News homepage inspired by Node [SFW]](https://news.ycombinator.com/item?id=2392051) | 展示一个受 Node 风格启发、适合工作时浏览的 HN 首页。 | 581 | 97 | 2011-03-31 |
| 12 | [Angry Nerds](https://news.ycombinator.com/item?id=2394082) | 关注技术爱好者表达愤怒的现象。 | 572 | 41 | 2011-03-31 |
| 13 | [GitHub now has view modes for image diffs.](https://news.ycombinator.com/item?id=2351851) | GitHub 新增查看图像差异的多种模式。 | 570 | 58 | 2011-03-21 |
| 14 | [A fifteen year old TCP bug?](https://news.ycombinator.com/item?id=2364065) | 追查一个疑似存在十五年的 TCP 漏洞。 | 546 | 59 | 2011-03-24 |
| 15 | [Man upgrades Windows 1.0 to Windows 7 (video)](https://news.ycombinator.com/item?id=2281045) | 视频记录从 Windows 1.0 一路升级到 Windows 7 的过程。 | 526 | 115 | 2011-03-02 |
| 16 | [AT&T has a fiberoptic splitter copying our data to NSA](https://news.ycombinator.com/item?id=2348156) | 指称 AT&T 使用光纤分路设备将数据复制给 NSA。 | 525 | 220 | 2011-03-21 |
| 17 | [MIT is a national treasure](https://news.ycombinator.com/item?id=2358559) | 作者赞赏麻省理工作为国家宝贵资源的价值。 | 525 | 150 | 2011-03-23 |
| 18 | [Accounting for Computer Scientists](https://news.ycombinator.com/item?id=2298471) | 为计算机背景读者介绍会计知识。 | 520 | 75 | 2011-03-07 |
| 19 | [Steve Jobs' reality distortion takes its toll on truth](https://news.ycombinator.com/item?id=2284547) | 作者批评 Steve Jobs 的现实扭曲力损害事实表达。 | 513 | 325 | 2011-03-03 |
| 20 | [How a simple comment on Hacker News made me quit my job and launch a startup](https://news.ycombinator.com/item?id=2340732) | 作者因 HN 的一条评论辞职，并启动自己的创业项目。 | 504 | 92 | 2011-03-18 |

## 2011-04

有效主帖 15,746 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [I don't learn anything on HN anymore, bring back the upvote count](https://news.ycombinator.com/item?id=2495137) | 用户认为隐藏赞数降低了学习价值，呼吁恢复显示。 | 1136 | 228 | 2011-04-28 |
| 2 | [Sony: All personal data stolen from PSN](https://news.ycombinator.com/item?id=2486924) | 索尼披露 PlayStation Network 用户个人资料遭窃。 | 1074 | 279 | 2011-04-26 |
| 3 | [Using prime numbers to make better backgrounds](https://news.ycombinator.com/item?id=2419347) | 介绍用质数改善背景图案的方法。 | 975 | 52 | 2011-04-07 |
| 4 | [Dropbox Attempts To Kill Open Source Project](https://news.ycombinator.com/item?id=2482712) | 指称 Dropbox 试图阻止一个开源项目的发展。 | 886 | 292 | 2011-04-25 |
| 5 | [FBI seized PokerStars.com, FullTiltPoker.com, UB.com,...  domain names](https://news.ycombinator.com/item?id=2451302) | FBI 扣押 PokerStars 等在线扑克网站的域名。 | 880 | 384 | 2011-04-15 |
| 6 | [Showoff](https://news.ycombinator.com/item?id=2467107) | 介绍名为 Showoff 的项目。 | 805 | 214 | 2011-04-20 |
| 7 | [Amazon’s $23,698,655.93 book about flies](https://news.ycombinator.com/item?id=2475854) | 一部关于苍蝇的书在亚马逊标价近二千四百万美元。 | 711 | 140 | 2011-04-23 |
| 8 | [Workers Leaving the Googleplex](https://news.ycombinator.com/item?id=2500082) | 关注员工离开 Google 园区与公司的现象。 | 690 | 391 | 2011-04-30 |
| 9 | [YouTube Founders Acquire Delicious From Yahoo](https://news.ycombinator.com/item?id=2490067) | YouTube 创始人从雅虎收购 Delicious。 | 573 | 118 | 2011-04-27 |
| 10 | [Amazon Web Services are down](https://news.ycombinator.com/item?id=2469838) | Amazon Web Services 出现服务故障。 | 560 | 332 | 2011-04-21 |
| 11 | [Hashify.me - store entire website content in the URL](https://news.ycombinator.com/item?id=2464213) | Hashify.me 尝试把整个网页内容存进 URL。 | 554 | 123 | 2011-04-19 |
| 12 | [Nginx 1.0.0 is out](https://news.ycombinator.com/item?id=2436536) | Nginx 1.0.0 正式发布。 | 549 | 75 | 2011-04-12 |
| 13 | [Facebook open sources its servers and data centers](https://news.ycombinator.com/item?id=2420325) | Facebook 公开服务器与数据中心的相关设计。 | 530 | 98 | 2011-04-07 |
| 14 | [Crash Course: Design for Startups](https://news.ycombinator.com/item?id=2424822) | 为初创公司提供快速入门的设计知识。 | 523 | 33 | 2011-04-08 |
| 15 | [Chinese Infinite Magical Hard-Drive](https://news.ycombinator.com/item?id=2418837) | 介绍被称为“中国无限魔法硬盘”的异常存储设备。 | 522 | 118 | 2011-04-07 |
| 16 | [Dear Dr. Stallman: An Open Letter](https://news.ycombinator.com/item?id=2477586) | 分享一封致 Richard Stallman 的公开信。 | 493 | 199 | 2011-04-23 |
| 17 | [Ask HN: How to stave off decline of HN?](https://news.ycombinator.com/item?id=2403696) | 站方征求遏制 HN 评论质量下降与恶意内容获赞的办法。 | 465 | 680 | 2011-04-03 |
| 18 | [Predator Object Tracking Algorithm](https://news.ycombinator.com/item?id=2403290) | 介绍名为 Predator 的目标跟踪算法。 | 460 | 76 | 2011-04-03 |
| 19 | [The US Government Keeps Harassing a UW Researcher Who Speaks for WikiLeaks](https://news.ycombinator.com/item?id=2430090) | 报道称一位为 WikiLeaks 发声的华盛顿大学研究者持续遭骚扰。 | 454 | 143 | 2011-04-10 |
| 20 | [Before I Die...](https://news.ycombinator.com/item?id=2417828) | 以“在我死之前”为题思考未完成的人生愿望。 | 449 | 70 | 2011-04-07 |

## 2011-05

有效主帖 15,447 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Boot a linux kernel right inside your browser. ](https://news.ycombinator.com/item?id=2555349) | 展示直接在浏览器中启动 Linux 内核的项目。 | 1820 | 239 | 2011-05-17 |
| 2 | [TermKit - a graphical terminal replacement](https://news.ycombinator.com/item?id=2559734) | 介绍尝试替代传统终端的图形化工具 TermKit。 | 1056 | 200 | 2011-05-18 |
| 3 | [Osama bin Laden Is Dead](https://news.ycombinator.com/item?id=2504770) | 美国宣布 Osama bin Laden 已死亡。 | 924 | 430 | 2011-05-02 |
| 4 | [Facebook Loses Much Face In Secret Smear On Google](https://news.ycombinator.com/item?id=2539929) | Facebook 秘密抹黑 Google 的行动被曝光并引发批评。 | 779 | 142 | 2011-05-12 |
| 5 | [This Guy Has My MacBook](https://news.ycombinator.com/item?id=2604013) | 作者讲述追踪拿着自己 MacBook 的人的经历。 | 741 | 411 | 2011-05-31 |
| 6 | [Creator of "Dirty Jobs" Mike Rowe testifies to Congress](https://news.ycombinator.com/item?id=2544500) | 《Dirty Jobs》创作者 Mike Rowe 在国会作证。 | 667 | 207 | 2011-05-13 |
| 7 | [How AirBnB Became a Billion Dollar Company](https://news.ycombinator.com/item?id=2603844) | 回顾 Airbnb 如何成长为十亿美元估值的公司。 | 654 | 186 | 2011-05-31 |
| 8 | [Guy unknowingly live tweets the Osama raid in Abbottabad](https://news.ycombinator.com/item?id=2505610) | 一名男子在不知情下实时发推记录阿伯塔巴德突袭行动。 | 638 | 101 | 2011-05-02 |
| 9 | [The Last Post](https://news.ycombinator.com/item?id=2514270) | 作者以“最后一帖”为题表达告别。 | 604 | 61 | 2011-05-04 |
| 10 | [John Resig joins the Khan Academy](https://news.ycombinator.com/item?id=2510585) | John Resig 加入可汗学院。 | 585 | 73 | 2011-05-03 |
| 11 | [LastPass Disclosure Shows Why We Can't Have Nice Things](https://news.ycombinator.com/item?id=2526868) | 从 LastPass 的披露事件反思安全沟通面临的困境。 | 559 | 82 | 2011-05-08 |
| 12 | [Cool, but obscure Unix tools](https://news.ycombinator.com/item?id=2567186) | 推荐一些实用却鲜为人知的 UNIX 工具。 | 534 | 120 | 2011-05-20 |
| 13 | [You can increase your intelligence](https://news.ycombinator.com/item?id=2562632) | 提出智力可以提升的观点。 | 519 | 132 | 2011-05-19 |
| 14 | [Game developer David Braben creates a USB stick PC for $25](https://news.ycombinator.com/item?id=2519248) | 游戏开发者 David Braben 打造售价二十五美元的微型电脑。 | 518 | 91 | 2011-05-05 |
| 15 | [Satellite Images of North Korea Prison Camps Find 200,000 Living as Slaves](https://news.ycombinator.com/item?id=2541189) | 卫星图像揭示朝鲜劳改营状况，报道称约二十万人被奴役。 | 486 | 205 | 2011-05-12 |
| 16 | [My daughter was first sued in the womb](https://news.ycombinator.com/item?id=2551436) | 作者讲述女儿尚在母腹时就遭起诉的经历。 | 477 | 67 | 2011-05-16 |
| 17 | [Intel Reinvents Transistors Using New 3-D Structure](https://news.ycombinator.com/item?id=2514363) | Intel 用新的三维结构改进晶体管。 | 470 | 101 | 2011-05-04 |
| 18 | ["The Best of edw519" is now free. Reverse Happy Birthday](https://news.ycombinator.com/item?id=2564099) | 《The Best of edw519》开始免费提供，作为反向生日礼物。 | 467 | 62 | 2011-05-19 |
| 19 | [Why should anyone ever use a Google API again?](https://news.ycombinator.com/item?id=2592399) | 质疑开发者今后为何还应依赖 Google API。 | 463 | 180 | 2011-05-27 |
| 20 | [Google Chrome Hacked?](https://news.ycombinator.com/item?id=2529663) | 追问 Google Chrome 是否已被成功入侵。 | 450 | 210 | 2011-05-09 |

## 2011-06

有效主帖 15,868 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ooops.](https://news.ycombinator.com/item?id=2661209) | 以“哎呀”为题呈现一次出错或失误的情境。 | 1123 | 238 | 2011-06-16 |
| 2 | [Enough Is Enough](https://news.ycombinator.com/item?id=2606727) | 作者以“够了”为题表达对某种现状的不满。 | 1032 | 185 | 2011-06-01 |
| 3 | [GitHub for Mac](https://news.ycombinator.com/item?id=2683996) | GitHub 推出 Mac 客户端。 | 680 | 206 | 2011-06-22 |
| 4 | [I'm the guy who bought 259684 Bitcoins for under $3000 yesterday](https://news.ycombinator.com/item?id=2676263) | 作者自称以不到三千美元买到 259,684 枚比特币。 | 664 | 312 | 2011-06-20 |
| 5 | [Advice From An Old Programmer](https://news.ycombinator.com/item?id=2662617) | 一位老程序员分享经验与建议。 | 649 | 220 | 2011-06-16 |
| 6 | [Kind of Screwed](https://news.ycombinator.com/item?id=2687950) | 作者以“有点糟糕”为题讲述所处困境。 | 611 | 237 | 2011-06-23 |
| 7 | [Robert Morris, Pioneer in Computer Security, Dies at 78](https://news.ycombinator.com/item?id=2712469) | 计算机安全先驱 Robert Morris 去世，享年七十八岁。 | 588 | 45 | 2011-06-30 |
| 8 | [My Email Canary](https://news.ycombinator.com/item?id=2636685) | 介绍作者的“邮件金丝雀”做法。 | 581 | 118 | 2011-06-09 |
| 9 | [The FBI stole an Instapaper server in an unrelated raid](https://news.ycombinator.com/item?id=2688614) | 指称 FBI 在无关搜查中扣走一台 Instapaper 服务器。 | 581 | 250 | 2011-06-23 |
| 10 | [Tell HN: Our experience with Groupon](https://news.ycombinator.com/item?id=2654788) | 一位跳伞场经营者分享开展 Groupon 团购促销的经历。 | 562 | 105 | 2011-06-14 |
| 11 | [DuckDuckGo: Escape your search engine filter bubble](https://news.ycombinator.com/item?id=2673898) | DuckDuckGo 提出帮助用户摆脱搜索结果的过滤气泡。 | 548 | 214 | 2011-06-20 |
| 12 | [Testing Benford's Law](https://news.ycombinator.com/item?id=2701342) | 通过实验检验本福特定律。 | 546 | 88 | 2011-06-27 |
| 13 | [Google Reveals Its Stealth Social Project, Google+](https://news.ycombinator.com/item?id=2706214) | Google 揭晓社交项目 Google+。 | 526 | 339 | 2011-06-28 |
| 14 | ["My current theory is that programming is quite literally writing."](https://news.ycombinator.com/item?id=2632816) | 作者提出编程在字面意义上就是写作的看法。 | 513 | 190 | 2011-06-08 |
| 15 | [Y Combinator Numbers](https://news.ycombinator.com/item?id=2608440) | 介绍与 Y Combinator 有关的数据。 | 506 | 115 | 2011-06-01 |
| 16 | [TrueCrypt User Held in Contempt of Court](https://news.ycombinator.com/item?id=2693599) | 一位 TrueCrypt 用户被判藐视法庭。 | 488 | 186 | 2011-06-24 |
| 17 | [My Life as an Undocumented Immigrant](https://news.ycombinator.com/item?id=2684406) | 作者讲述作为无证移民生活的经历。 | 476 | 323 | 2011-06-22 |
| 18 | [Why I've built an alternative to Github](https://news.ycombinator.com/item?id=2674417) | 作者解释为何开发 GitHub 的替代服务。 | 473 | 192 | 2011-06-20 |
| 19 | [How to Make Text Look Interesting: Minimalist Web Design](https://news.ycombinator.com/item?id=2692214) | 从极简网页设计角度介绍如何让文字更有吸引力。 | 455 | 72 | 2011-06-24 |
| 20 | [Skype protocol reverse engineered, source available](https://news.ycombinator.com/item?id=2611299) | Skype 协议被逆向分析，相关源代码已提供。 | 451 | 133 | 2011-06-02 |

## 2011-07

有效主帖 15,924 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Airbnb Nightmare: No End In Sight](https://news.ycombinator.com/item?id=2820615) | 一位用户称自己的 Airbnb 噩梦仍未结束。 | 1017 | 482 | 2011-07-29 |
| 2 | [Violated: A traveler’s lost faith, a difficult lesson learned ](https://news.ycombinator.com/item?id=2811080) | 一位旅行者讲述信任受损后得到的艰难教训。 | 952 | 380 | 2011-07-27 |
| 3 | [Chosen: A javascript plug-in that makes long select boxes user-friendly.](https://news.ycombinator.com/item?id=2793086) | Chosen 插件改善冗长下拉选择框的使用体验。 | 923 | 76 | 2011-07-22 |
| 4 | [Bored People Quit](https://news.ycombinator.com/item?id=2754986) | 探讨员工因感到无聊而选择离职的现象。 | 840 | 151 | 2011-07-12 |
| 5 | [33GB of public domain JSTOR articles, and a manifesto](https://news.ycombinator.com/item?id=2789709) | 公开 33GB 公共领域 JSTOR 文章，并附上一份宣言。 | 840 | 179 | 2011-07-21 |
| 6 | [A lesson on the importance of encouraging your children with their projects](https://news.ycombinator.com/item?id=2757980) | 通过故事说明鼓励孩子坚持个人项目的重要性。 | 821 | 103 | 2011-07-13 |
| 7 | [You are not running out of time](https://news.ycombinator.com/item?id=2778342) | 提醒读者不必总觉得自己已经来不及了。 | 696 | 125 | 2011-07-18 |
| 8 | [Why I will never pursue cheating again](https://news.ycombinator.com/item?id=2774254) | 作者解释为何不再寻求作弊的机会。 | 691 | 482 | 2011-07-17 |
| 9 | [Aaronsw indicted for hacking MIT network to download millions of JSTOR docs](https://news.ycombinator.com/item?id=2781615) | Aaron Swartz 因侵入 MIT 网络下载大量 JSTOR 文献被起诉。 | 603 | 313 | 2011-07-19 |
| 10 | [Google made my son cry](https://news.ycombinator.com/item?id=2725983) | 作者讲述 Google 的做法让儿子哭泣的经历。 | 583 | 265 | 2011-07-04 |
| 11 | [Matz (creator of Ruby) joins Heroku](https://news.ycombinator.com/item?id=2756314) | Ruby 创造者 Matz 加入 Heroku。 | 578 | 75 | 2011-07-12 |
| 12 | [Steve Yegge quits Google in the middle of his speech [OSCON Data 2011]](https://news.ycombinator.com/item?id=2811818) | Steve Yegge 在 OSCON Data 演讲中作出辞职 Google 的表示。 | 546 | 130 | 2011-07-27 |
| 13 | [Nobody Understands REST or HTTP](https://news.ycombinator.com/item?id=2724488) | 作者批评人们对 REST 与 HTTP 缺乏真正理解。 | 520 | 133 | 2011-07-03 |
| 14 | [User testing in the wild: he has never used a computer](https://news.ycombinator.com/item?id=2737645) | 通过一位从未使用过电脑的人开展真实用户测试。 | 513 | 199 | 2011-07-07 |
| 15 | [Greece defaults](https://news.ycombinator.com/item?id=2791778) | 报道希腊发生债务违约。 | 500 | 145 | 2011-07-21 |
| 16 | [How The Hell Is This My Fault?](https://news.ycombinator.com/item?id=2825177) | 作者追问为何自己要为某件事承担责任。 | 481 | 281 | 2011-07-30 |
| 17 | [How Running A Business Changes The Way You Think](https://news.ycombinator.com/item?id=2742985) | 探讨经营企业如何改变人的思考方式。 | 477 | 98 | 2011-07-08 |
| 18 | [A pound of flesh: how Cisco's "unmitigated gall" derailed one man's life](https://news.ycombinator.com/item?id=2789540) | 讲述 Cisco 的做法如何严重影响一名男子的生活。 | 467 | 101 | 2011-07-21 |
| 19 | [Webdesigners: please make text readable](https://news.ycombinator.com/item?id=2807047) | 呼吁网页设计师确保文字清晰可读。 | 467 | 106 | 2011-07-26 |
| 20 | [XKCD's Randall Munroe on Google+ requiring your gender to be public](https://news.ycombinator.com/item?id=2741425) | Randall Munroe 评论 Google+ 要求公开性别的规定。 | 463 | 283 | 2011-07-08 |

## 2011-08

有效主帖 17,333 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Steve Jobs Resigns as CEO of Apple](https://news.ycombinator.com/item?id=2922756) | Steve Jobs 辞去苹果 CEO 职务。 | 1667 | 305 | 2011-08-24 |
| 2 | [Google Buys Motorola For $12.5 Billion](https://news.ycombinator.com/item?id=2886342) | Google 以 125 亿美元收购摩托罗拉相关业务。 | 1214 | 369 | 2011-08-15 |
| 3 | [Twitter Bootstrap](https://news.ycombinator.com/item?id=2904355) | 介绍 Twitter 推出的网页前端框架 Bootstrap。 | 1047 | 108 | 2011-08-19 |
| 4 | [Show HN: Codecademy.com, the easiest way to learn to code](https://news.ycombinator.com/item?id=2901156) | Codecademy 展示以互动方式帮助新手学习编程的平台。 | 787 | 232 | 2011-08-18 |
| 5 | [Rob "CmdrTaco" Malda Resigns From Slashdot](https://news.ycombinator.com/item?id=2924731) | Slashdot 的 Rob “CmdrTaco” Malda 宣布离职。 | 784 | 143 | 2011-08-25 |
| 6 | [United States loses AAA credit rating from S&P ](https://news.ycombinator.com/item?id=2852380) | 标准普尔取消美国的 AAA 主权信用评级。 | 769 | 497 | 2011-08-06 |
| 7 | [Microsoft UI has officially entered the realm of self-parody](https://news.ycombinator.com/item?id=2938271) | 作者认为微软界面设计已到了自我戏仿的程度。 | 742 | 326 | 2011-08-29 |
| 8 | [Jonathan's Card](https://news.ycombinator.com/item?id=2857424) | 介绍名为 Jonathan's Card 的项目。 | 726 | 219 | 2011-08-07 |
| 9 | [An iOS Developer Takes on Android](https://news.ycombinator.com/item?id=2832390) | 一位 iOS 开发者分享尝试 Android 开发的体验。 | 720 | 116 | 2011-08-01 |
| 10 | [Solar-panel "trees" really are inferior](https://news.ycombinator.com/item?id=2906538) | 对“树状太阳能板更好”的说法提出反驳。 | 650 | 98 | 2011-08-20 |
| 11 | [13-Year-Old Makes Solar Power Breakthrough by Harnessing the Fibonacci Sequence](https://news.ycombinator.com/item?id=2902329) | 报道称一名十三岁少年利用斐波那契数列改进太阳能发电。 | 649 | 142 | 2011-08-19 |
| 12 | [Steve Jobs Resigns as Apple CEO (Official Letter)](https://news.ycombinator.com/item?id=2922770) | 分享 Steve Jobs 辞去苹果 CEO 的正式信件。 | 641 | 65 | 2011-08-24 |
| 13 | [How Browsers Work](https://news.ycombinator.com/item?id=2894708) | 介绍浏览器内部的工作机制。 | 633 | 36 | 2011-08-17 |
| 14 | [Icon Ambulance](https://news.ycombinator.com/item?id=2923885) | 介绍名为 Icon Ambulance 的图标项目。 | 622 | 87 | 2011-08-25 |
| 15 | [If Software Is Eating The World, Why Don't Coders Get Any Respect?](https://news.ycombinator.com/item?id=2919708) | 追问软件日益重要，为何程序员未获得相应的尊重。 | 618 | 265 | 2011-08-24 |
| 16 | [The Patent Pledge](https://news.ycombinator.com/item?id=2947203) | 介绍围绕专利使用作出的承诺。 | 618 | 194 | 2011-08-31 |
| 17 | [That truck driver you flipped off? Let me tell you his story.](https://news.ycombinator.com/item?id=2841992) | 讲述被人竖中指的卡车司机背后不为人知的故事。 | 616 | 286 | 2011-08-03 |
| 18 | [Warren Buffett: Stop coddling the super rich](https://news.ycombinator.com/item?id=2885367) | Warren Buffett 呼吁停止对超级富豪的优待。 | 605 | 336 | 2011-08-15 |
| 19 | [Learn Vim Progressively](https://news.ycombinator.com/item?id=2936670) | 提供循序渐进学习 Vim 的路线。 | 605 | 113 | 2011-08-29 |
| 20 | [SICP is Under Attack](https://news.ycombinator.com/item?id=2843715) | 关注《SICP》及其教学理念遭受的质疑。 | 570 | 196 | 2011-08-03 |

## 2011-09

有效主帖 16,748 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [I was once a Facebook fool](https://news.ycombinator.com/item?id=3029872) | 作者反思自己曾对 Facebook 抱有的天真信任。 | 1390 | 163 | 2011-09-23 |
| 2 | [Stripe: instant payment processing for developers](https://news.ycombinator.com/item?id=3053883) | 介绍为开发者提供便捷支付处理的 Stripe。 | 1249 | 348 | 2011-09-29 |
| 3 | [Speed-of-light experiments yield baffling result at LHC](https://news.ycombinator.com/item?id=3027056) | 报道一项出现疑似超光速结果的实验，引发科学疑问。 | 938 | 239 | 2011-09-22 |
| 4 | [Bring a stick man to life.](https://news.ycombinator.com/item?id=3024860) | 展示让手绘火柴人动起来的互动体验。 | 862 | 64 | 2011-09-22 |
| 5 | [Fucking Sue Me](https://news.ycombinator.com/item?id=2985195) | 作者以“有本事告我”为题表达强烈回应。 | 695 | 148 | 2011-09-11 |
| 6 | [If this then that](https://news.ycombinator.com/item?id=2970550) | 介绍用“如果这样就那样”连接操作的服务。 | 673 | 149 | 2011-09-07 |
| 7 | [This is what happens when one guy practices art every day for nine years](https://news.ycombinator.com/item?id=3031684) | 展示一名创作者连续九年每天练习艺术后的成果。 | 664 | 99 | 2011-09-23 |
| 8 | [Git Is Simpler Than You Think](https://news.ycombinator.com/item?id=2970149) | 解释 Git 为何可能比想象中更简单。 | 609 | 118 | 2011-09-07 |
| 9 | [Joel Spolsky Launches Trello - Organize Anything Together](https://news.ycombinator.com/item?id=2993732) | Joel Spolsky 推出协作组织工具 Trello。 | 595 | 269 | 2011-09-13 |
| 10 | [Linux is now hosted on GitHub](https://news.ycombinator.com/item?id=2960677) | Linux 源代码开始托管在 GitHub。 | 568 | 93 | 2011-09-05 |
| 11 | [Facebook is scaring me](https://news.ycombinator.com/item?id=3033385) | 作者表达 Facebook 的做法令自己不安。 | 553 | 270 | 2011-09-24 |
| 12 | [Academics should stop doing free peer-review for non-open-access journals.](https://news.ycombinator.com/item?id=3051546) | 主张学者停止为非开放获取期刊免费进行同行评审。 | 551 | 89 | 2011-09-29 |
| 13 | [Hey Google, I want my cache links back](https://news.ycombinator.com/item?id=3047335) | 用户要求 Google 恢复搜索结果中的缓存链接。 | 519 | 172 | 2011-09-28 |
| 14 | [Google Flight Search](https://news.ycombinator.com/item?id=2992660) | Google 推出航班搜索服务。 | 516 | 278 | 2011-09-13 |
| 15 | [A First Look at BankSimple](https://news.ycombinator.com/item?id=3022537) | 初步介绍 BankSimple。 | 477 | 189 | 2011-09-21 |
| 16 | [Google Correlate by Drawing ](https://news.ycombinator.com/item?id=2953900) | 介绍通过绘图使用 Google Correlate 的方式。 | 475 | 77 | 2011-09-02 |
| 17 | [Logging out of Facbook is not enough](https://news.ycombinator.com/item?id=3035418) | 提醒用户仅退出 Facebook 登录可能还不够。 | 475 | 120 | 2011-09-25 |
| 18 | [Technical Papers Every Programmer Should Read (At Least Twice)](https://news.ycombinator.com/item?id=2979458) | 整理值得程序员至少阅读两遍的技术论文。 | 467 | 57 | 2011-09-09 |
| 19 | [The Best Science Fiction Books (According to Reddit)](https://news.ycombinator.com/item?id=2978027) | 整理 Reddit 用户推荐的优秀科幻书籍。 | 466 | 287 | 2011-09-09 |
| 20 | [Twitter's Storm (complex event processing system) is now open source](https://news.ycombinator.com/item?id=3014039) | Twitter 将复杂事件处理系统 Storm 开源。 | 461 | 56 | 2011-09-19 |

## 2011-10

有效主帖 18,206 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Steve Jobs has passed away.](https://news.ycombinator.com/item?id=3078128) | Steve Jobs 去世的消息引发社区悼念。 | 4338 | 363 | 2011-10-05 |
| 2 | [Rob Pike: Dennis Ritchie has died](https://news.ycombinator.com/item?id=3105526) | Rob Pike 宣布 Dennis Ritchie 去世。 | 1958 | 196 | 2011-10-13 |
| 3 | [A Sister’s Eulogy for Steve Jobs](https://news.ycombinator.com/item?id=3174961) | 分享 Steve Jobs 姐妹为他写的悼词。 | 1736 | 121 | 2011-10-30 |
| 4 | [John McCarthy Has Died](https://news.ycombinator.com/item?id=3151233) | 人工智能先驱 John McCarthy 去世。 | 1619 | 218 | 2011-10-24 |
| 5 | [Steve's Google Platform rant](https://news.ycombinator.com/item?id=3101876) | Steve Yegge 就 Google 平台战略发表长篇批评。 | 1196 | 393 | 2011-10-12 |
| 6 | [My dad taught me cashflow with a soda machine](https://news.ycombinator.com/item?id=3167630) | 作者回忆父亲如何用一台汽水机教自己理解现金流。 | 1060 | 101 | 2011-10-28 |
| 7 | [Don't Call Yourself a Programmer](https://news.ycombinator.com/item?id=3170766) | 作者建议技术从业者不要只以“程序员”定义自己。 | 1021 | 267 | 2011-10-29 |
| 8 | [Steve Jobs has died](https://news.ycombinator.com/item?id=3078107) | 报道苹果联合创始人 Steve Jobs 去世。 | 901 | 69 | 2011-10-05 |
| 9 | [Amit Gupta needs you](https://news.ycombinator.com/item?id=3149337) | 呼吁读者为 Amit Gupta 提供帮助。 | 886 | 143 | 2011-10-24 |
| 10 | [Apple RIP Logo design](https://news.ycombinator.com/item?id=3079100) | 展示纪念 Steve Jobs 的苹果标志设计。 | 812 | 45 | 2011-10-06 |
| 11 | [Subtle Patterns: Free textures for your next web project](https://news.ycombinator.com/item?id=3091846) | Subtle Patterns 提供可用于网页项目的免费纹理。 | 801 | 64 | 2011-10-10 |
| 12 | [Daring Fireball: Universe Dented, Grass Underfoot](https://news.ycombinator.com/item?id=3080068) | Daring Fireball 以“宇宙留下凹痕”悼念 Steve Jobs。 | 749 | 135 | 2011-10-06 |
| 13 | [I quit my job last March and it was a bad idea.](https://news.ycombinator.com/item?id=3102143) | 一位用户分享辞职后的不顺经历，提醒读者考虑另一面。 | 745 | 325 | 2011-10-12 |
| 14 | [Up and Down the Ladder of Abstraction](https://news.ycombinator.com/item?id=3099595) | 探讨如何在不同抽象层次之间来回思考。 | 733 | 72 | 2011-10-11 |
| 15 | [Bitbucket now rocks Git](https://news.ycombinator.com/item?id=3066828) | Bitbucket 开始支持 Git。 | 726 | 173 | 2011-10-03 |
| 16 | [Ask HN: What programming blogs do you read daily?](https://news.ycombinator.com/item?id=3120380) | 征集读者每天阅读的编程博客。 | 716 | 116 | 2011-10-17 |
| 17 | [We now have an effective vaccine for Malaria](https://news.ycombinator.com/item?id=3128320) | 报道一种疟疾疫苗取得有效性进展。 | 622 | 138 | 2011-10-19 |
| 18 | [24 year old student lights match: Europe versus Facebook](https://news.ycombinator.com/item?id=3127185) | 一位二十四岁学生发起欧洲用户针对 Facebook 的行动。 | 579 | 214 | 2011-10-18 |
| 19 | [Video: Quantum Levitation](https://news.ycombinator.com/item?id=3123373) | 通过视频展示量子悬浮现象。 | 572 | 95 | 2011-10-18 |
| 20 | [The Steve Jobs I Knew](https://news.ycombinator.com/item?id=3078706) | 作者回忆自己认识的 Steve Jobs。 | 571 | 11 | 2011-10-06 |

## 2011-11

有效主帖 16,871 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Watch a VC use my name to sell a con](https://news.ycombinator.com/item?id=3288671) | 作者指称一位风投人士用自己的名字推销骗局。 | 2376 | 292 | 2011-11-29 |
| 2 | [Zynga to employees: Give back our stock or you'll be fired](https://news.ycombinator.com/item?id=3220819) | 报道称 Zynga 要求部分员工退还股票，否则将被解雇。 | 1120 | 370 | 2011-11-10 |
| 3 | [In defense of the Google chef](https://news.ycombinator.com/item?id=3223595) | 作者为一位 Google 厨师辩护。 | 994 | 188 | 2011-11-11 |
| 4 | [Stop SOPA, save the Internet](https://news.ycombinator.com/item?id=3235059) | 呼吁阻止 SOPA 法案以保护互联网。 | 883 | 131 | 2011-11-14 |
| 5 | [A Brief Rant on the Future of Interaction Design](https://news.ycombinator.com/item?id=3212949) | 对未来交互设计的方向提出简短而直接的批评。 | 830 | 150 | 2011-11-08 |
| 6 | [I was annoyed with sites asking for too many Facebook privileges and made this](https://news.ycombinator.com/item?id=3287272) | 开发者因反感过多 Facebook 权限请求而制作工具。 | 820 | 141 | 2011-11-28 |
| 7 | [Diaspora Co-Founder Ilya Zhitomirskiy Passes Away At 21](https://news.ycombinator.com/item?id=3231531) | Diaspora 联合创始人 Ilya Zhitomirskiy 去世，年仅二十一岁。 | 764 | 230 | 2011-11-13 |
| 8 | [Don't use MongoDB](https://news.ycombinator.com/item?id=3202081) | 作者提出不要使用 MongoDB 的建议。 | 706 | 293 | 2011-11-06 |
| 9 | [Secret app on millions of phones logs key taps ](https://news.ycombinator.com/item?id=3295341) | 报道称数百万手机中的秘密应用会记录按键操作。 | 700 | 189 | 2011-11-30 |
| 10 | [Mozilla urges its users to raise their voice against SOPA](https://news.ycombinator.com/item?id=3242700) | Mozilla 呼吁用户发声反对 SOPA。 | 699 | 41 | 2011-11-16 |
| 11 | [Internet giants place full-page anti-SOPA ad in NYT](https://news.ycombinator.com/item?id=3244994) | 互联网企业在《纽约时报》刊登整版反 SOPA 广告。 | 687 | 111 | 2011-11-16 |
| 12 | [Amit Gupta hasn't found a marrow transplant match; today's your last chance.](https://news.ycombinator.com/item?id=3297091) | Amit Gupta 尚未找到骨髓配型，帖子再次紧急呼吁帮助。 | 652 | 234 | 2011-11-30 |
| 13 | [The Sugru story](https://news.ycombinator.com/item?id=3260801) | 讲述 Sugru 产品的诞生与发展故事。 | 644 | 86 | 2011-11-21 |
| 14 | [I swapped my MacBook for an iPad+Linode](https://news.ycombinator.com/item?id=3186476) | 作者分享以 iPad 加 Linode 替代 MacBook 的经历。 | 634 | 338 | 2011-11-02 |
| 15 | [Doom 3 source released](https://news.ycombinator.com/item?id=3267701) | 《Doom 3》的源代码正式公开。 | 630 | 101 | 2011-11-22 |
| 16 | [Watch Me Make Mistakes](https://news.ycombinator.com/item?id=3216529) | 作者邀请读者观看自己犯错的过程。 | 603 | 116 | 2011-11-09 |
| 17 | [I regularly hire women for 65% to 75% of what males make](https://news.ycombinator.com/item?id=3289750) | 作者自称经常以男性薪酬的 65% 至 75% 雇用女性。 | 601 | 277 | 2011-11-29 |
| 18 | [Adobe ceases development on mobile browser Flash, refocuses efforts on HTML5](https://news.ycombinator.com/item?id=3214454) | Adobe 停止开发移动浏览器 Flash，并转向 HTML5。 | 597 | 154 | 2011-11-09 |
| 19 | [Tell congress to stop SOPA with a physical letter](https://news.ycombinator.com/item?id=3240981) | 鼓励读者通过纸质信件要求国会停止 SOPA。 | 594 | 93 | 2011-11-15 |
| 20 | [Learn Web Design, Web Development, and iOS Development - Treehouse](https://news.ycombinator.com/item?id=3206540) | 介绍教授网页设计、Web 开发和 iOS 开发的 Treehouse。 | 589 | 175 | 2011-11-07 |

## 2011-12

有效主帖 17,175 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Paul Graham: SOPA Supporting Companies No Longer Allowed At YC Demo Day](https://news.ycombinator.com/item?id=3383209) | Paul Graham 宣布支持 SOPA 的公司不得参加 YC Demo Day。 | 1742 | 272 | 2011-12-22 |
| 2 | [GoDaddy supports SOPA, redditor proposes "Move your Domain Day"](https://news.ycombinator.com/item?id=3381822) | GoDaddy 支持 SOPA，引发 Reddit 用户倡议迁出域名。 | 1121 | 244 | 2011-12-22 |
| 3 | [A Step By Step Guide to Transfer Domains Out Of GoDaddy](https://news.ycombinator.com/item?id=3383097) | 提供将域名从 GoDaddy 转出的分步指南。 | 1086 | 103 | 2011-12-22 |
| 4 | [Time to end the war on drugs](https://news.ycombinator.com/item?id=3392857) | 作者呼吁结束禁毒战争。 | 905 | 208 | 2011-12-26 |
| 5 | [Suicide](https://news.ycombinator.com/item?id=3348671) | 围绕自杀这一沉重话题展开讨论。 | 880 | 275 | 2011-12-13 |
| 6 | [More Paypal nonsense](https://news.ycombinator.com/item?id=3317856) | 作者再次批评 PayPal 带来的问题。 | 870 | 246 | 2011-12-06 |
| 7 | [Louis C.K. experiment results: over $500,000 in 4 days](https://news.ycombinator.com/item?id=3350474) | Louis C.K. 的销售实验四天获得逾五十万美元收入。 | 868 | 279 | 2011-12-14 |
| 8 | [What really happened aboard Air France 447](https://news.ycombinator.com/item?id=3327202) | 回顾法航 447 航班机上究竟发生了什么。 | 858 | 365 | 2011-12-08 |
| 9 | [GoDaddy has not withdrawn its official congressional support for SOPA ](https://news.ycombinator.com/item?id=3389594) | 指出 GoDaddy 尚未正式向国会撤回对 SOPA 的支持。 | 825 | 59 | 2011-12-24 |
| 10 | [Don't Be A Free User](https://news.ycombinator.com/item?id=3320931) | 作者劝读者不要只做产品的免费用户。 | 793 | 170 | 2011-12-06 |
| 11 | [HP to Contribute webOS to Open Source](https://news.ycombinator.com/item?id=3334877) | 惠普宣布将 webOS 贡献给开源社区。 | 751 | 194 | 2011-12-09 |
| 12 | [An Indian Inventor Disrupts The Period Industry](https://news.ycombinator.com/item?id=3370034) | 讲述一位印度发明者改变经期卫生用品行业的故事。 | 705 | 145 | 2011-12-19 |
| 13 | [GoDaddy: A glimpse of the Internet under SOPA](https://news.ycombinator.com/item?id=3393477) | 以 GoDaddy 的做法设想 SOPA 下的互联网。 | 705 | 38 | 2011-12-26 |
| 14 | [Dear Internet: It's no Longer OK Not to Know How Congress Works](https://news.ycombinator.com/item?id=3369541) | 呼吁互联网用户了解美国国会的运作方式。 | 681 | 157 | 2011-12-19 |
| 15 | [Mint.com turns 404 ad page into date ad for developer](https://news.ycombinator.com/item?id=3322561) | Mint.com 将 404 广告页面变成开发者的征友广告。 | 672 | 149 | 2011-12-07 |
| 16 | [In Memoriam: Christopher Hitchens, 1949–2011](https://news.ycombinator.com/item?id=3359498) | 悼念作家 Christopher Hitchens 的一生。 | 669 | 220 | 2011-12-16 |
| 17 | [How Doctors Die](https://news.ycombinator.com/item?id=3313570) | 探讨医生面对自己死亡时如何作出选择。 | 663 | 177 | 2011-12-05 |
| 18 | [Fuck passwords](https://news.ycombinator.com/item?id=3313790) | 作者以强烈措辞批评依赖密码的认证方式。 | 655 | 240 | 2011-12-05 |
| 19 | [Bullshit](https://news.ycombinator.com/item?id=3402859) | 围绕“胡说”这一概念展开批评与辨析。 | 651 | 225 | 2011-12-29 |
| 20 | [Go Daddy No Longer Supports SOPA](https://news.ycombinator.com/item?id=3386667) | GoDaddy 宣布不再支持 SOPA。 | 645 | 226 | 2011-12-23 |

## 2012-01

有效主帖 20,312 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Request for Startups: Kill Hollywood.](https://news.ycombinator.com/item?id=3491542) | 向创业者征集挑战好莱坞模式的项目。 | 2060 | 665 | 2012-01-20 |
| 2 | [Amit Gupta has found a 10/10 matched donor](https://news.ycombinator.com/item?id=3482119) | Amit Gupta 找到十项指标完全匹配的捐献者。 | 1179 | 100 | 2012-01-18 |
| 3 | [PayPal forces buyer to destroy $2500 pre-WWII antique violin in dispute](https://news.ycombinator.com/item?id=3421882) | 指称 PayPal 在争议处理中要求买家销毁二战前古董小提琴。 | 988 | 289 | 2012-01-03 |
| 4 | [Wikipedia to Shut Down on Wednesday to Protest SOPA](https://news.ycombinator.com/item?id=3471726) | 维基百科计划周三暂停服务，以抗议 SOPA。 | 951 | 192 | 2012-01-16 |
| 5 | [Reddit to go dark on Jan 18 to protest SOPA](https://news.ycombinator.com/item?id=3449510) | Reddit 宣布一月十八日关闭网站抗议 SOPA。 | 922 | 150 | 2012-01-10 |
| 6 | [Why I'm a Pirate](https://news.ycombinator.com/item?id=3478850) | 作者解释自己为何认同“海盗”身份。 | 857 | 514 | 2012-01-18 |
| 7 | [Understanding the bin, sbin, usr/bin , usr/sbin split](https://news.ycombinator.com/item?id=3519952) | 解释 UNIX 中 bin、sbin 与 usr 下相应目录的历史分工。 | 857 | 151 | 2012-01-27 |
| 8 | [Fun with math: Dividing one by 998001 yields a surprising result](https://news.ycombinator.com/item?id=3514721) | 展示 1 除以 998001 得到的有趣数字规律。 | 754 | 90 | 2012-01-26 |
| 9 | [Google, what were you thinking?](https://news.ycombinator.com/item?id=3460033) | 用户质疑一篇批评 Google 的 Mocality 文章为何无法正常出现。 | 751 | 143 | 2012-01-13 |
| 10 | [The Five Stages of Hosting](https://news.ycombinator.com/item?id=3526767) | 把网站托管的发展经历归纳为五个阶段。 | 747 | 179 | 2012-01-30 |
| 11 | [Richard Stallman Was Right All Along](https://news.ycombinator.com/item?id=3417033) | 作者提出 Richard Stallman 的担忧早已正确。 | 731 | 226 | 2012-01-02 |
| 12 | [No New Accounts Today](https://news.ycombinator.com/item?id=3481174) | 因 Reddit 抗议停站带来大量流量，HN 暂停注册以示尊重。 | 718 | 94 | 2012-01-18 |
| 13 | [Two things about SOPA/PIPA and then I'll shut up](https://news.ycombinator.com/item?id=3495062) | 作者补充关于 SOPA 和 PIPA 的两点看法。 | 709 | 172 | 2012-01-21 |
| 14 | [Megaupload down, FBI Charges Seven With Online Piracy](https://news.ycombinator.com/item?id=3486268) | Megaupload 被关闭，FBI 以网络盗版相关罪名起诉七人。 | 698 | 337 | 2012-01-19 |
| 15 | [A simple guide for getting started with git](https://news.ycombinator.com/item?id=3442431) | 提供一份简明的 Git 入门指南。 | 665 | 129 | 2012-01-09 |
| 16 | [What if Hollywood had to use tech like we have to watch movies?](https://news.ycombinator.com/item?id=3524008) | 设想好莱坞必须像用户看电影那样使用技术时的处境。 | 663 | 112 | 2012-01-29 |
| 17 | [How to nap](https://news.ycombinator.com/item?id=3448266) | 分享如何安排午睡与小憩。 | 647 | 133 | 2012-01-10 |
| 18 | [Why 37signals Doesn't Hire Programmers Based on Brainteasers](https://news.ycombinator.com/item?id=3428984) | 解释 37signals 为何不用脑筋急转弯招聘程序员。 | 605 | 423 | 2012-01-05 |
| 19 | [Schlep Blindness](https://news.ycombinator.com/item?id=3465521) | 探讨创业者对繁琐实际工作的视而不见。 | 604 | 181 | 2012-01-14 |
| 20 | [Stop SOAP](https://news.ycombinator.com/item?id=3479558) | 以“停止 SOAP”的口号表达对这一技术的批评。 | 598 | 67 | 2012-01-18 |

## 2012-02

有效主帖 18,320 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Hit men, click whores, and paid apologists: Welcome to the Silicon Cesspool](https://news.ycombinator.com/item?id=3587730) | 批评硅谷中的付费辩护、博眼球及攻击行为。 | 1319 | 195 | 2012-02-13 |
| 2 | [Farewell Stack Exchange](https://news.ycombinator.com/item?id=3559631) | 作者向 Stack Exchange 告别。 | 1233 | 213 | 2012-02-06 |
| 3 | [Every day at my job I helped people just barely survive](https://news.ycombinator.com/item?id=3607217) | 作者回顾每天在工作中帮助他人勉强维持生存的经历。 | 928 | 315 | 2012-02-18 |
| 4 | [Path uploads your entire iPhone address book to its servers](https://news.ycombinator.com/item?id=3563016) | 披露 Path 会把 iPhone 整本通讯录上传到服务器。 | 834 | 267 | 2012-02-07 |
| 5 | [14 years ago: the day Teller gave me the secret to my career in magic.](https://news.ycombinator.com/item?id=3596124) | 作者回忆十四年前 Teller 如何给予自己魔术生涯的启示。 | 797 | 63 | 2012-02-15 |
| 6 | [Bootstrap 2.0, From Twitter](https://news.ycombinator.com/item?id=3536291) | Twitter 发布 Bootstrap 2.0。 | 773 | 158 | 2012-02-01 |
| 7 | [Dear Boss: For a programmer, 10 minutes = 3 hours](https://news.ycombinator.com/item?id=3548445) | 向管理者解释为何打断程序员十分钟可能耗掉三小时。 | 699 | 157 | 2012-02-03 |
| 8 | [Ubuntu for Android](https://news.ycombinator.com/item?id=3617238) | 介绍 Ubuntu for Android 项目。 | 698 | 171 | 2012-02-21 |
| 9 | [ASCII interactive fluid animation](https://news.ycombinator.com/item?id=3567209) | 展示以 ASCII 字符呈现的交互式流体动画。 | 663 | 66 | 2012-02-08 |
| 10 | [Handwriting to LaTeX maths](https://news.ycombinator.com/item?id=3542534) | 介绍将手写数学表达式转换为 LaTeX 的工具。 | 652 | 88 | 2012-02-02 |
| 11 | [Producer vs. Consumer](https://news.ycombinator.com/item?id=3555237) | 对照创造者与消费者两种角色。 | 647 | 64 | 2012-02-05 |
| 12 | [Xcode, GCC, and Homebrew](https://news.ycombinator.com/item?id=3600758) | 探讨 Xcode、GCC 与 Homebrew 的关系。 | 646 | 103 | 2012-02-16 |
| 13 | [TV is broken](https://news.ycombinator.com/item?id=3629803) | 作者批评电视体验存在的问题。 | 635 | 258 | 2012-02-24 |
| 14 | [I have a bad feeling about this](https://news.ycombinator.com/item?id=3569443) | 作者表达自己对某一动向的不祥预感。 | 629 | 179 | 2012-02-09 |
| 15 | [The myth of the eight-hour sleep](https://news.ycombinator.com/item?id=3620742) | 检视连续睡八小时才正常这一常见观念。 | 607 | 161 | 2012-02-22 |
| 16 | [Jotform domain seized by US due to user generated content](https://news.ycombinator.com/item?id=3597025) | 美国因用户生成内容扣押 Jotform 的域名。 | 605 | 236 | 2012-02-16 |
| 17 | [Teller Reveals His Secrets](https://news.ycombinator.com/item?id=3632821) | 魔术师 Teller 分享表演秘密。 | 602 | 36 | 2012-02-25 |
| 18 | [Back on Linux (after one year of Apple and OS X)](https://news.ycombinator.com/item?id=3584609) | 作者使用苹果与 OS X 一年后重新回到 Linux。 | 593 | 321 | 2012-02-13 |
| 19 | [Game Developer Gives 7-Year-Old Best Birthday Present Ever](https://news.ycombinator.com/item?id=3590795) | 一位游戏开发者送给七岁孩子特别的生日礼物。 | 593 | 45 | 2012-02-14 |
| 20 | [Right versus pragmatic](https://news.ycombinator.com/item?id=3633985) | 探讨坚持原则正确与采取务实做法之间的关系。 | 568 | 162 | 2012-02-25 |

## 2012-03

有效主帖 20,749 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: This up votes itself](https://news.ycombinator.com/item?id=3742902) | 展示一个会给自己投赞成票的 HN 项目。 | 3531 | 82 | 2012-03-23 |
| 2 | [$1B of TSA Nude Body Scanners Made Worthless By Blog ](https://news.ycombinator.com/item?id=3673462) | 报道称一篇博客揭示了 TSA 昂贵人体扫描设备的缺陷。 | 1637 | 330 | 2012-03-06 |
| 3 | ["Lighten up"](https://news.ycombinator.com/item?id=3736037) | 围绕“放轻松”这句话展开反思。 | 1371 | 794 | 2012-03-21 |
| 4 | [DuckDuckGo is blowing up](https://news.ycombinator.com/item?id=3770958) | 关注 DuckDuckGo 的快速增长。 | 1221 | 203 | 2012-03-29 |
| 5 | [Six-Legged Giant Finds Secret Hideaway, Hides For 80 Years](https://news.ycombinator.com/item?id=3651551) | 讲述一种巨型六足生物藏身八十年后被重新发现的故事。 | 1154 | 172 | 2012-03-01 |
| 6 | [Frighteningly Ambitious Startup Ideas](https://news.ycombinator.com/item?id=3686840) | 提出一些雄心大到令人望而生畏的创业构想。 | 1032 | 430 | 2012-03-10 |
| 7 | [Why I Left Google](https://news.ycombinator.com/item?id=3700277) | 作者解释自己离开 Google 的原因。 | 947 | 306 | 2012-03-13 |
| 8 | [I am very real](https://news.ycombinator.com/item?id=3776040) | 作者以“我是真实的”为题回应关于自身的疑问。 | 943 | 150 | 2012-03-30 |
| 9 | [Wind Map](https://news.ycombinator.com/item?id=3767889) | 展示以地图形式呈现风向与风场的 Wind Map。 | 909 | 79 | 2012-03-28 |
| 10 | [Why I Am Leaving Goldman Sachs](https://news.ycombinator.com/item?id=3702253) | 作者解释自己离开高盛的原因。 | 896 | 249 | 2012-03-14 |
| 11 | [Codename: Obtvse](https://news.ycombinator.com/item?id=3744237) | 介绍代号为 Obtvse 的项目。 | 889 | 355 | 2012-03-23 |
| 12 | [TSA Pressures Mainstream Media Not To Cover Story](https://news.ycombinator.com/item?id=3681202) | 指称 TSA 向主流媒体施压，要求不报道相关事件。 | 745 | 149 | 2012-03-08 |
| 13 | [There is no point to distributing music in 24-bit/192kHz format.](https://news.ycombinator.com/item?id=3668310) | 作者质疑以 24 位、192kHz 格式发行音乐的必要性。 | 732 | 316 | 2012-03-05 |
| 14 | [A Woman’s Story](https://news.ycombinator.com/item?id=3772292) | 讲述一位女性的个人故事。 | 716 | 194 | 2012-03-29 |
| 15 | [Font Awesome, the pictographic font designed for use with Twitter Bootstrap](https://news.ycombinator.com/item?id=3672526) | 介绍为 Bootstrap 设计的图标字体 Font Awesome。 | 711 | 91 | 2012-03-06 |
| 16 | [There's no speed limit (2009)](https://news.ycombinator.com/item?id=3761013) | 重读一篇关于突破自我限制的 2009 年文章。 | 699 | 194 | 2012-03-27 |
| 17 | [Notch gives his $3,000,000 Minecraft dividend to his employees](https://news.ycombinator.com/item?id=3654648) | Notch 将三百万美元 Minecraft 分红分给员工。 | 694 | 209 | 2012-03-01 |
| 18 | [Sqrt(x*x+y*y)+3*cos(sqrt(x*x+y*y))+5 from -20 to 20 ](https://news.ycombinator.com/item?id=3777505) | 展示由平方根与余弦组成的函数在指定区间的图形。 | 692 | 135 | 2012-03-30 |
| 19 | [New: Apply to Y Combinator without an Idea](https://news.ycombinator.com/item?id=3700712) | YC 新增允许申请者在没有创业点子的情况下申请。 | 687 | 292 | 2012-03-13 |
| 20 | [Time.is](https://news.ycombinator.com/item?id=3690435) | 介绍用于查看准确时间的在线服务 Time.is。 | 661 | 107 | 2012-03-11 |

## 2012-04

有效主帖 20,190 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Light Table - a new IDE concept](https://news.ycombinator.com/item?id=3836978) | 展示新的集成开发环境概念 Light Table。 | 1592 | 291 | 2012-04-13 |
| 2 | [Show HN: Meteor, a realtime JavaScript framework](https://news.ycombinator.com/item?id=3824908) | 介绍实时 JavaScript 开发框架 Meteor。 | 1386 | 322 | 2012-04-10 |
| 3 | [I hereby resign](https://news.ycombinator.com/item?id=3790378) | 作者发表正式辞职声明。 | 1175 | 366 | 2012-04-02 |
| 4 | ["That's Why You Don't Have Any Friends."](https://news.ycombinator.com/item?id=3883682) | 以“这就是你没有朋友的原因”为题审视人际评价。 | 1041 | 195 | 2012-04-24 |
| 5 | [Mosh: SSH for 2012](https://news.ycombinator.com/item?id=3819382) | 介绍试图改进远程终端体验的 Mosh。 | 900 | 193 | 2012-04-09 |
| 6 | [Facebook acquires Instagram](https://news.ycombinator.com/item?id=3817840) | Facebook 宣布收购 Instagram。 | 837 | 374 | 2012-04-09 |
| 7 | [How I attacked myself using Google and I ramped up a $1000 bandwidth bill](https://news.ycombinator.com/item?id=3890328) | 作者用 Google 攻击自己，导致一千美元带宽账单。 | 775 | 142 | 2012-04-25 |
| 8 | [PHP: A fractal of bad design](https://news.ycombinator.com/item?id=3820431) | 以“糟糕设计的分形”为比喻批评 PHP。 | 765 | 495 | 2012-04-10 |
| 9 | [How Not To Sort By Average Rating](https://news.ycombinator.com/item?id=3792627) | 解释按平均分排列评分可能造成的问题。 | 750 | 153 | 2012-04-03 |
| 10 | [Don’t Be Evil: How Google Screwed a Startup](https://news.ycombinator.com/item?id=3803568) | 指称 Google 的做法损害了一家创业公司。 | 710 | 246 | 2012-04-05 |
| 11 | [Incredibox - Background music for programming. ](https://news.ycombinator.com/item?id=3900711) | 推荐 Incredibox 作为编程时的背景音乐来源。 | 688 | 167 | 2012-04-27 |
| 12 | [The Top Of My Todo List](https://news.ycombinator.com/item?id=3872613) | 作者分享待办清单最上方的事项。 | 683 | 185 | 2012-04-21 |
| 13 | [Introducing Google Drive... yes, really](https://news.ycombinator.com/item?id=3884720) | Google 正式推出云端存储服务 Drive。 | 663 | 492 | 2012-04-24 |
| 14 | [Light Table Is On Kickstarter](https://news.ycombinator.com/item?id=3855248) | Light Table 在 Kickstarter 发起众筹。 | 619 | 215 | 2012-04-17 |
| 15 | [Modern Web Development](https://news.ycombinator.com/item?id=3880213) | 介绍现代 Web 开发的相关思路。 | 605 | 85 | 2012-04-23 |
| 16 | [9 year old's DIY Cardboard Arcade gets Flash mobbed: Video](https://news.ycombinator.com/item?id=3829120) | 九岁男孩自制纸板游乐场获快闪人群支持及奖学金捐助。 | 603 | 131 | 2012-04-11 |
| 17 | [Valve Employee Handbook](https://news.ycombinator.com/item?id=3871463) | 分享 Valve 的员工手册。 | 569 | 160 | 2012-04-21 |
| 18 | [The Beer Game -or- Why Apple Can’t Build iPads in the US](https://news.ycombinator.com/item?id=3802515) | 借“啤酒游戏”解释苹果难以在美国生产 iPad 的原因。 | 562 | 246 | 2012-04-05 |
| 19 | [Instantly create beautiful GitHub project pages](https://news.ycombinator.com/item?id=3788962) | 介绍快速创建精美 GitHub 项目页面的方法。 | 553 | 46 | 2012-04-02 |
| 20 | [Show HN: Imagine a search engine that removed top million sites from its index](https://news.ycombinator.com/item?id=3910304) | 展示一个从索引中移除排名前百万网站的搜索引擎。 | 552 | 195 | 2012-04-30 |

## 2012-05

有效主帖 20,374 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Plagiarism](https://news.ycombinator.com/item?id=3972651) | 围绕抄袭现象展开讨论。 | 1230 | 311 | 2012-05-14 |
| 2 | [Hunting Down My Son's Killer](https://news.ycombinator.com/item?id=4038113) | 作者讲述追查杀害自己儿子的凶手的经历。 | 1139 | 318 | 2012-05-29 |
| 3 | [20 lines of code that beat A/B testing every time](https://news.ycombinator.com/item?id=4040022) | 介绍一种据称只需二十行代码即可优于 A/B 测试的方法。 | 989 | 147 | 2012-05-29 |
| 4 | [Please don't learn to code](https://news.ycombinator.com/item?id=3975744) | 作者提出不必人人都学习编程的观点。 | 746 | 266 | 2012-05-15 |
| 5 | [Oracle v. Google - Judge Alsup Rules APIs Not Protected By Copyright](https://news.ycombinator.com/item?id=4050490) | Oracle 诉 Google 案中，Alsup 法官裁定相关 API 不受版权保护。 | 735 | 141 | 2012-05-31 |
| 6 | [Apple rejecting applications which use Dropbox](https://news.ycombinator.com/item?id=3916826) | 报道称苹果拒绝使用 Dropbox 的应用。 | 723 | 348 | 2012-05-01 |
| 7 | [Verdict for Google in Oracle's patent infringement case](https://news.ycombinator.com/item?id=4014400) | Google 在 Oracle 的专利侵权诉讼中获有利裁决。 | 723 | 165 | 2012-05-23 |
| 8 | [Recursive Drawing](https://news.ycombinator.com/item?id=3951255) | 展示通过递归方式进行绘画的项目。 | 694 | 83 | 2012-05-10 |
| 9 | [The Cab Ride I'll Never Forget](https://news.ycombinator.com/item?id=3918783) | 作者回忆一段令自己难以忘怀的出租车旅程。 | 688 | 188 | 2012-05-02 |
| 10 | [Being deaf](https://news.ycombinator.com/item?id=4001727) | 分享作为听障人士的生活体验。 | 676 | 153 | 2012-05-21 |
| 11 | [Please Don't Become Anything, Especially Not A Programmer](https://news.ycombinator.com/item?id=3977918) | 作者反思被要求成为某种职业身份，尤其是程序员。 | 670 | 218 | 2012-05-15 |
| 12 | [Please Learn to Code](https://news.ycombinator.com/item?id=3975992) | 作者呼吁读者学习编程。 | 654 | 146 | 2012-05-15 |
| 13 | [Space Station grabs SpaceX Dragon ship](https://news.ycombinator.com/item?id=4023484) | 国际空间站捕获 SpaceX 的“龙”飞船。 | 585 | 166 | 2012-05-25 |
| 14 | [GitHub for Windows](https://news.ycombinator.com/item?id=4003523) | GitHub 推出 Windows 客户端。 | 549 | 236 | 2012-05-21 |
| 15 | [The frequent fliers who flew too much](https://news.ycombinator.com/item?id=3936310) | 讲述一些常旅客因飞得太多而引发的问题。 | 546 | 222 | 2012-05-06 |
| 16 | [Welcome To Life](https://news.ycombinator.com/item?id=3969653) | 以“欢迎来到生活”为题呈现对生活的思考。 | 545 | 183 | 2012-05-14 |
| 17 | [Backdoor found in a China-made US military chip ](https://news.ycombinator.com/item?id=4030746) | 报道称一款中国制造、供美军使用的芯片被发现存在后门。 | 536 | 149 | 2012-05-27 |
| 18 | [Linus Torvalds won't do github pull requests](https://news.ycombinator.com/item?id=3960876) | Linus Torvalds 表示不会采用 GitHub 的拉取请求方式。 | 535 | 267 | 2012-05-11 |
| 19 | [Google is making a huge and annoying mistake](https://news.ycombinator.com/item?id=3919078) | 作者批评 Google 正在犯一个重大且令人烦恼的错误。 | 534 | 261 | 2012-05-02 |
| 20 | [Carmack on why transatlantic ping is faster than pushing a pixel to the screen](https://news.ycombinator.com/item?id=3914638) | John Carmack 解释跨大西洋网络延迟为何能低于屏幕显示延迟。 | 531 | 64 | 2012-05-01 |

## 2012-06

有效主帖 18,402 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [It all began with a strange email](https://news.ycombinator.com/item?id=4114295) | 作者讲述一段从奇怪邮件开始的经历。 | 874 | 124 | 2012-06-15 |
| 2 | [R.I.P. Ray Bradbury, Author of Fahrenheit 451 and The Martian Chronicles ](https://news.ycombinator.com/item?id=4073942) | 悼念《华氏 451 度》与《火星编年史》作者 Ray Bradbury。 | 821 | 95 | 2012-06-06 |
| 3 | [Sublime Text 2.0 Released](https://news.ycombinator.com/item?id=4161610) | Sublime Text 2.0 正式发布。 | 813 | 352 | 2012-06-26 |
| 4 | [A VC-funded startup called WhosHere is trying to steal my social network](https://news.ycombinator.com/item?id=4055256) | 作者指称获风投支持的 WhosHere 试图夺走自己的社交网络。 | 787 | 219 | 2012-06-01 |
| 5 | [The Silencing of Maya](https://news.ycombinator.com/item?id=4103344) | 关注 Maya 遭到噤声的故事。 | 785 | 321 | 2012-06-12 |
| 6 | [The Recruiter Honeypot](https://news.ycombinator.com/item?id=4163820) | 介绍以招聘者为对象设置的“蜜罐”实验。 | 655 | 156 | 2012-06-26 |
| 7 | [US and Israel created Stuxnet, lost control of it](https://news.ycombinator.com/item?id=4052719) | 报道称美国与以色列开发 Stuxnet，随后失去控制。 | 650 | 310 | 2012-06-01 |
| 8 | [Paul Graham's Letter to YC Companies](https://news.ycombinator.com/item?id=4067297) | Paul Graham 致信 YC 公司，提醒关注 Facebook IPO 后的融资变化。 | 645 | 185 | 2012-06-05 |
| 9 | [A day in the life of a startup founder](https://news.ycombinator.com/item?id=4166183) | 以虚构日程戏仿创业圈对创始人生活习惯的过度追捧。 | 633 | 126 | 2012-06-27 |
| 10 | [Microsoft Introduces New "Surface" Tablet](https://news.ycombinator.com/item?id=4129125) | 微软发布新的 Surface 平板电脑。 | 611 | 660 | 2012-06-18 |
| 11 | [Famous judge spikes Apple-Google case, calls patent system “dysfunctional”](https://news.ycombinator.com/item?id=4085502) | 一位法官终止苹果与 Google 相关诉讼，批评专利制度失灵。 | 601 | 121 | 2012-06-08 |
| 12 | [Mihai Pătraşcu 1982–2012](https://news.ycombinator.com/item?id=4140524) | 悼念生于 1982 年、卒于 2012 年的 Mihai Pătraşcu。 | 599 | 29 | 2012-06-21 |
| 13 | [Bye Bye Craigslist](https://news.ycombinator.com/item?id=4148997) | 作者以“再见 Craigslist”为题表达离开的态度。 | 586 | 297 | 2012-06-22 |
| 14 | [Why three prongs?](https://news.ycombinator.com/item?id=4058834) | 追问为何采用三个插脚的设计。 | 581 | 146 | 2012-06-02 |
| 15 | [Moderators of HN: please stop changing post titles](https://news.ycombinator.com/item?id=4102013) | 用户要求 HN 管理员不要在帖子上首页后继续改动标题。 | 572 | 46 | 2012-06-12 |
| 16 | [Eulerian Video Magnification for Revealing Subtle Changes in the World](https://news.ycombinator.com/item?id=4062216) | 介绍通过欧拉视频放大呈现现实中细微变化的技术。 | 566 | 129 | 2012-06-04 |
| 17 | [Kid Automates Work, Is Fired, Hired Back, Automates Business](https://news.ycombinator.com/item?id=4167186) | 讲述青年自动化工作、被解雇后再获聘并继续自动化的经历。 | 566 | 198 | 2012-06-27 |
| 18 | [6.5 Million LinkedIn Password Hashes Leaked](https://news.ycombinator.com/item?id=4073309) | LinkedIn 约六百五十万个密码哈希泄露。 | 561 | 511 | 2012-06-06 |
| 19 | [Michael Lewis: Don't Eat Fortune's Cookie](https://news.ycombinator.com/item?id=4065233) | Michael Lewis 以“别吃命运饼干”为题分享人生看法。 | 552 | 180 | 2012-06-04 |
| 20 | [Show HN: movies.io — torrent search like it should be](https://news.ycombinator.com/item?id=4054568) | 展示以改进种子搜索体验为目标的 movies.io。 | 550 | 487 | 2012-06-01 |

## 2012-07

有效主帖 19,000 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Company withdrawing from Facebook as analytics show 80% of ad clicks from bots](https://news.ycombinator.com/item?id=4312731) | 一家公司因分析显示八成广告点击来自机器人而撤离 Facebook。 | 1347 | 356 | 2012-07-30 |
| 2 | [The Next Microsoft](https://news.ycombinator.com/item?id=4195208) | 围绕谁可能成为“下一个微软”展开思考。 | 1183 | 329 | 2012-07-03 |
| 3 | [Google Fiber Plans & Pricing](https://news.ycombinator.com/item?id=4296898) | 介绍 Google Fiber 的套餐与价格。 | 1139 | 466 | 2012-07-26 |
| 4 | [Physical assault by McDonald's for wearing Digital Eye Glass](https://news.ycombinator.com/item?id=4252955) | 作者称因佩戴数字眼镜在麦当劳遭受身体攻击。 | 1056 | 446 | 2012-07-16 |
| 5 | [Google’s Marissa Mayer Tapped as Yahoo’s Chief](https://news.ycombinator.com/item?id=4252274) | Google 高管 Marissa Mayer 被任命为雅虎掌门人。 | 1016 | 343 | 2012-07-16 |
| 6 | [The Challenge of Making Friends as an Adult](https://news.ycombinator.com/item?id=4247488) | 讨论成年人结交新朋友时面临的困难。 | 697 | 304 | 2012-07-15 |
| 7 | [Higgs Boson Explained by Cartoon](https://news.ycombinator.com/item?id=4193590) | 用漫画解释希格斯玻色子。 | 646 | 127 | 2012-07-03 |
| 8 | [The Marco.org Review of John Siracusa’s Review of OS X 10.8 Mountain Lion](https://news.ycombinator.com/item?id=4290605) | Marco.org 评论 John Siracusa 对 OS X Mountain Lion 的评测。 | 641 | 118 | 2012-07-25 |
| 9 | [A Dust Over India](https://news.ycombinator.com/item?id=4214480) | 以“印度上空的尘埃”为题呈现相关观察。 | 633 | 304 | 2012-07-08 |
| 10 | [Late bloomer, not a loser. (I hope) ](https://news.ycombinator.com/item?id=4213386) | 作者希望将自己的经历理解为大器晚成，而非失败。 | 604 | 191 | 2012-07-08 |
| 11 | [Github Raises $100 Million](https://news.ycombinator.com/item?id=4220353) | GitHub 融资一亿美元。 | 547 | 222 | 2012-07-09 |
| 12 | [A file that's both an acceptable HTML page and a JPEG (view source on it)](https://news.ycombinator.com/item?id=4209052) | 展示一个同时符合 HTML 页面与 JPEG 格式的文件。 | 536 | 128 | 2012-07-06 |
| 13 | [Got 15 minutes and want to learn Git?](https://news.ycombinator.com/item?id=4199772) | 提供可在浏览器中完成的十五分钟 Git 教程。 | 510 | 171 | 2012-07-04 |
| 14 | [How Amazon’s ambitious new push for same-day delivery will destroy local retail](https://news.ycombinator.com/item?id=4232104) | 作者认为亚马逊当日送达计划将重创本地零售。 | 509 | 309 | 2012-07-11 |
| 15 | [PostgreSQL Rising](https://news.ycombinator.com/item?id=4268525) | 关注 PostgreSQL 的发展与影响力上升。 | 506 | 194 | 2012-07-19 |
| 16 | [Sparrow acquired by Google](https://news.ycombinator.com/item?id=4271376) | Google 收购邮件应用 Sparrow。 | 502 | 380 | 2012-07-20 |
| 17 | [John Siracusa's OS X 10.8 Mountain Lion Review](https://news.ycombinator.com/item?id=4290579) | 分享 John Siracusa 对 OS X 10.8 Mountain Lion 的详细评测。 | 497 | 135 | 2012-07-25 |
| 18 | [ACTA killed in EU parliament: 478 votes to 39](https://news.ycombinator.com/item?id=4198825) | 欧洲议会以 478 票对 39 票否决 ACTA。 | 495 | 86 | 2012-07-04 |
| 19 | [Show HN: fontBomb - Stylishly destroy the web](https://news.ycombinator.com/item?id=4208102) | fontBomb 让用户以视觉爆破效果“摧毁”网页。 | 489 | 85 | 2012-07-06 |
| 20 | [MVC is dead, it's time to MOVE on](https://news.ycombinator.com/item?id=4189811) | 作者提出用 MOVE 模式替代 MVC 的构想。 | 487 | 222 | 2012-07-02 |

## 2012-08

有效主帖 19,457 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Neil Armstrong has died at 82 Today](https://news.ycombinator.com/item?id=4432894) | 登月宇航员 Neil Armstrong 去世，享年八十二岁。 | 980 | 92 | 2012-08-25 |
| 2 | [This is how Visa works](https://news.ycombinator.com/item?id=4396414) | 解释 Visa 支付网络如何运作。 | 931 | 97 | 2012-08-17 |
| 3 | [Amazon Glacier](https://news.ycombinator.com/item?id=4411536) | 介绍亚马逊面向长期归档的云存储服务 Glacier。 | 906 | 378 | 2012-08-21 |
| 4 | [Why I now, unfortunately, hate Hacker News..](https://news.ycombinator.com/item?id=4396747) | 一位老用户解释自己为何从喜爱 HN 变得反感社区氛围。 | 871 | 431 | 2012-08-17 |
| 5 | [This is a bit f'd, Quora](https://news.ycombinator.com/item?id=4377181) | 作者以直白措辞批评 Quora 的做法。 | 827 | 226 | 2012-08-13 |
| 6 | [Textmate2 Goes Open Source](https://news.ycombinator.com/item?id=4361390) | TextMate 2 宣布开放源代码。 | 780 | 300 | 2012-08-09 |
| 7 | [Design Tip: Never Use Black](https://news.ycombinator.com/item?id=4357002) | 提出设计时避免使用纯黑色的建议。 | 761 | 210 | 2012-08-08 |
| 8 | [An Unexpected Ass Kicking](https://news.ycombinator.com/item?id=4342790) | 讲述一次出乎意料的挫败经历。 | 746 | 196 | 2012-08-05 |
| 9 | [Dear Mark Zuckerberg](https://news.ycombinator.com/item?id=4325231) | 分享一封写给 Mark Zuckerberg 的公开文字。 | 743 | 261 | 2012-08-01 |
| 10 | [I Have 50 Dollars](https://news.ycombinator.com/item?id=4395665) | 作者以“我有五十美元”为起点讲述个人处境。 | 647 | 196 | 2012-08-17 |
| 11 | [ToS;DR — TL;DR for Terms of Service and Privacy Policy](https://news.ycombinator.com/item?id=4350907) | ToS;DR 为冗长的服务条款与隐私政策提供简要说明。 | 629 | 128 | 2012-08-07 |
| 12 | [Valve Source Engine Running Faster on Linux than Windows](https://news.ycombinator.com/item?id=4327908) | Valve 报告 Source 引擎在 Linux 上运行快于 Windows。 | 611 | 238 | 2012-08-02 |
| 13 | [Mars Curiosity's first images](https://news.ycombinator.com/item?id=4343891) | 展示“好奇号”火星车传回的首批照片。 | 592 | 168 | 2012-08-06 |
| 14 | [SpaceX wins $440M contract with NASA to develop Space Shuttle successor](https://news.ycombinator.com/item?id=4334852) | SpaceX 获 NASA 4.4 亿美元合同，开发航天飞机后继方案。 | 564 | 180 | 2012-08-03 |
| 15 | [Great work Visa, now I hate you](https://news.ycombinator.com/item?id=4347103) | 作者表达 Visa 的做法令自己产生强烈反感。 | 551 | 261 | 2012-08-06 |
| 16 | [Wikipedia Redefined](https://news.ycombinator.com/item?id=4352290) | 展示重新构想的维基百科设计。 | 550 | 288 | 2012-08-07 |
| 17 | [What Happens to Stolen Bicycles?](https://news.ycombinator.com/item?id=4444708) | 追问自行车被盗后通常会流向何处。 | 534 | 347 | 2012-08-28 |
| 18 | [A Generation Lost in the Bazaar ](https://news.ycombinator.com/item?id=4407188) | 以“迷失在集市的一代”为题审视一代人的处境。 | 519 | 344 | 2012-08-20 |
| 19 | [Ecuador grants Julian Assange asylum](https://news.ycombinator.com/item?id=4390885) | 厄瓜多尔给予 Julian Assange 政治庇护。 | 515 | 499 | 2012-08-16 |
| 20 | [Why it's so hard to find a photo of Neil Armstrong on the moon](https://news.ycombinator.com/item?id=4434509) | 解释为何很难找到 Neil Armstrong 站在月面的照片。 | 494 | 120 | 2012-08-26 |

## 2012-09

有效主帖 17,942 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Bret Victor: Learnable Programming](https://news.ycombinator.com/item?id=4577133) | Bret Victor 探索更容易理解和学习的编程环境。 | 1080 | 183 | 2012-09-26 |
| 2 | [Xkcd "Click and Drag" in a "map" interface](https://news.ycombinator.com/item?id=4543202) | 用地图式界面浏览 xkcd 的《Click and Drag》漫画。 | 844 | 86 | 2012-09-19 |
| 3 | [The Amazing iOS 6 Maps](https://news.ycombinator.com/item?id=4548829) | 以“惊人的 iOS 6 地图”为题审视苹果地图体验。 | 837 | 371 | 2012-09-20 |
| 4 | [Good riddance, PayPal](https://news.ycombinator.com/item?id=4483710) | 作者向 PayPal 告别并表达不满。 | 713 | 261 | 2012-09-06 |
| 5 | [Black Swan Farming](https://news.ycombinator.com/item?id=4497461) | 以“培育黑天鹅”为喻思考创业投资。 | 703 | 303 | 2012-09-09 |
| 6 | [Meeting A Troll](https://news.ycombinator.com/item?id=4567735) | 作者讲述与一位网络挑衅者见面的经历。 | 673 | 201 | 2012-09-24 |
| 7 | [Why was a scam company able to raise $76 Million Series B?](https://news.ycombinator.com/item?id=4592778) | 用户质疑商业模式有争议的 JustFab 为何能获得巨额融资。 | 660 | 174 | 2012-09-30 |
| 8 | [Everything's broken and nobody's upset](https://news.ycombinator.com/item?id=4531549) | 作者感叹许多东西出了问题，却少有人感到不满。 | 658 | 401 | 2012-09-17 |
| 9 | [AntiSec leaks 1,000,001 Apple UDIDs, Device Names/Types](https://news.ycombinator.com/item?id=4472897) | AntiSec 公布逾百万条苹果设备标识符及设备信息。 | 648 | 268 | 2012-09-04 |
| 10 | [A Letter from Tim Cook on Maps](https://news.ycombinator.com/item?id=4585223) | Tim Cook 就苹果地图发表公开信。 | 620 | 486 | 2012-09-28 |
| 11 | [PayPal CEO writes personal response](https://news.ycombinator.com/item?id=4493984) | PayPal CEO 亲自撰文回应。 | 619 | 159 | 2012-09-08 |
| 12 | [Startup = Growth](https://news.ycombinator.com/item?id=4556838) | 提出创业公司的核心特征在于增长。 | 586 | 206 | 2012-09-22 |
| 13 | [Realtime Web Messaging over Animated Gifs](https://news.ycombinator.com/item?id=4521334) | 展示通过动态 GIF 实现实时 Web 消息传输的方法。 | 576 | 106 | 2012-09-14 |
| 14 | [RIP Vile Rat, EVE Online Diplomat, IRL State Dept Rep Killed In Benghazi](https://news.ycombinator.com/item?id=4509291) | 悼念在班加西遇害的 EVE 玩家、美国国务院人员 Vile Rat。 | 539 | 261 | 2012-09-12 |
| 15 | [Show HN: We got tired of asking 'What browser are you using?' and created this](https://news.ycombinator.com/item?id=4499435) | 开发者制作工具，减少反复询问用户浏览器信息的麻烦。 | 521 | 175 | 2012-09-10 |
| 16 | [A 4G LTE base station running entirely in software on a standard PC](https://news.ycombinator.com/item?id=4469424) | 展示完全以软件在普通电脑上运行的 4G LTE 基站。 | 502 | 128 | 2012-09-03 |
| 17 | [Depression lies](https://news.ycombinator.com/item?id=4508873) | 用“抑郁会说谎”提醒读者审视抑郁状态中的判断。 | 496 | 229 | 2012-09-12 |
| 18 | [Sh.py](https://news.ycombinator.com/item?id=4530897) | 介绍将 Shell 命令带入 Python 调用方式的工具 Sh.py。 | 493 | 64 | 2012-09-17 |
| 19 | [Tomorrow Theme](https://news.ycombinator.com/item?id=4476359) | 介绍名为 Tomorrow Theme 的主题配色项目。 | 483 | 131 | 2012-09-04 |
| 20 | [The man who singlehandedly carved a road through a mountain](https://news.ycombinator.com/item?id=4557726) | 讲述一名男子独力在山中开凿道路的故事。 | 483 | 96 | 2012-09-22 |

## 2012-10

有效主帖 19,533 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Outlawed by Amazon DRM](https://news.ycombinator.com/item?id=4682392) | 作者讲述因亚马逊数字版权限制而被排除在外的经历。 | 1445 | 479 | 2012-10-22 |
| 2 | [The Future of Markdown](https://news.ycombinator.com/item?id=4700160) | 探讨 Markdown 的未来发展。 | 877 | 328 | 2012-10-25 |
| 3 | [Conway's Game of Life, using floating point values instead of integers](https://news.ycombinator.com/item?id=4642133) | 展示用浮点数替代整数的康威生命游戏变体。 | 688 | 96 | 2012-10-11 |
| 4 | [HN Spoof](https://news.ycombinator.com/item?id=4621731) | 介绍对 Hacker News 的戏仿作品。 | 681 | 82 | 2012-10-06 |
| 5 | [Tell HN: Let's Be Civil](https://news.ycombinator.com/item?id=4707475) | 用户呼吁讨论 iPad mini、Surface 等产品时保持礼貌。 | 671 | 138 | 2012-10-27 |
| 6 | [Linus Torvalds: Make 2560x1600 the new standard laptop resolution](https://news.ycombinator.com/item?id=4721751) | Linus Torvalds 呼吁将 2560×1600 设为笔记本新标准分辨率。 | 633 | 327 | 2012-10-31 |
| 7 | [Nexus: The best of Google, now in three sizes](https://news.ycombinator.com/item?id=4712924) | Google 介绍提供三种尺寸的 Nexus 产品系列。 | 603 | 456 | 2012-10-29 |
| 8 | [Amazon EC2 currently down. Affecting Heroku, Reddit, Others](https://news.ycombinator.com/item?id=4684384) | Amazon EC2 故障波及 Heroku、Reddit 等服务。 | 602 | 295 | 2012-10-22 |
| 9 | [Why is processing a sorted array faster than an unsorted array?](https://news.ycombinator.com/item?id=4637196) | 追问处理有序数组为何可能比处理无序数组更快。 | 590 | 119 | 2012-10-10 |
| 10 | [Apple's tribute to Steve Jobs, one year on.](https://news.ycombinator.com/item?id=4616292) | 苹果在 Steve Jobs 逝世一周年时发布纪念内容。 | 588 | 194 | 2012-10-05 |
| 11 | [Xkcd style graphs](https://news.ycombinator.com/item?id=4597977) | 介绍绘制 xkcd 风格图表的方法。 | 585 | 51 | 2012-10-01 |
| 12 | [The Most Revealing Job Interview Question](https://news.ycombinator.com/item?id=4613413) | 分享一个被认为能揭示求职者特质的面试问题。 | 578 | 235 | 2012-10-04 |
| 13 | [Introducing the Redesigned Bitbucket](https://news.ycombinator.com/item?id=4631926) | Bitbucket 推出重新设计的版本。 | 569 | 286 | 2012-10-09 |
| 14 | [Apple, Facebook, Google, Microsoft and others launch webplatform.org](https://news.ycombinator.com/item?id=4627106) | 苹果、Facebook、Google 与微软等共同推出 webplatform.org。 | 526 | 159 | 2012-10-08 |
| 15 | [Jessica Livingston: What Goes Wrong](https://news.ycombinator.com/item?id=4699862) | Jessica Livingston 分享创业过程中容易出什么问题。 | 518 | 88 | 2012-10-25 |
| 16 | [Show HN: I spent two years working on an HTML5 game. I finally released it](https://news.ycombinator.com/item?id=4684696) | 开发者发布自己花两年时间制作的 HTML5 游戏。 | 515 | 145 | 2012-10-22 |
| 17 | [Chrome DevTools could do that?](https://news.ycombinator.com/item?id=4614546) | 探索 Chrome 开发者工具中容易被忽略的功能。 | 514 | 74 | 2012-10-04 |
| 18 | [How cork is made](https://news.ycombinator.com/item?id=4668526) | 介绍软木的制作过程。 | 514 | 120 | 2012-10-18 |
| 19 | [The little ssh that (sometimes) couldn't](https://news.ycombinator.com/item?id=4709438) | 讲述 SSH 在某些情况下无法正常工作的排障故事。 | 508 | 63 | 2012-10-28 |
| 20 | [Never Give Your Information To 10 Minute Old Startups](https://news.ycombinator.com/item?id=4619541) | 提醒用户谨慎向刚成立的创业公司提供个人信息。 | 501 | 169 | 2012-10-06 |

## 2012-11

有效主帖 19,546 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Reddit user captures video of 2012 voting machines altering votes](https://news.ycombinator.com/item?id=4749574) | Reddit 用户拍到疑似在 2012 年选举中改动选票的投票机。 | 1072 | 637 | 2012-11-06 |
| 2 | [How I went from $100-an-hour programming to $X0,000-a-week consulting](https://news.ycombinator.com/item?id=4805091) | 作者分享从时薪一百美元编程转向高额周费咨询的经历。 | 1034 | 261 | 2012-11-19 |
| 3 | [Hacking my Vagina](https://news.ycombinator.com/item?id=4826561) | 作者以“改造我的阴道”为题分享个人探索。 | 952 | 253 | 2012-11-24 |
| 4 | [How to Get Startup Ideas](https://news.ycombinator.com/item?id=4806852) | 分享寻找创业点子的方法。 | 914 | 231 | 2012-11-19 |
| 5 | [Suite of 300 icons for web and user interface design](https://news.ycombinator.com/item?id=4821689) | 提供适用于网页与用户界面设计的三百枚图标。 | 821 | 98 | 2012-11-23 |
| 6 | [The Quiet Ones](https://news.ycombinator.com/item?id=4802118) | 以“安静的人们”为题关注少言者。 | 807 | 382 | 2012-11-18 |
| 7 | [The Worst](https://news.ycombinator.com/item?id=4838109) | 作者以“最糟糕”为题表达负面体验或判断。 | 770 | 207 | 2012-11-27 |
| 8 | [100,000 stars](https://news.ycombinator.com/item?id=4784821) | 展示以十万颗恒星为对象的星空探索项目。 | 746 | 109 | 2012-11-14 |
| 9 | [RethinkDB: An open-source distributed database built with love over three years](https://news.ycombinator.com/item?id=4763879) | 推出开发三年的开源分布式数据库 RethinkDB。 | 739 | 237 | 2012-11-09 |
| 10 | [The Fight](https://news.ycombinator.com/item?id=4740540) | 以“抗争”为题呈现一段冲突叙事。 | 734 | 133 | 2012-11-04 |
| 11 | [Leaping Brain's "Virtually Uncrackable" DRM is just an XOR with "RANDOM_STRING"](https://news.ycombinator.com/item?id=4834372) | 揭示 Leaping Brain 自称难以破解的 DRM 仅使用固定字符串异或。 | 720 | 254 | 2012-11-26 |
| 12 | [You are committing a crime right now](https://news.ycombinator.com/item?id=4812496) | 以“你此刻正在犯罪”为命题反思法律与日常行为的关系。 | 709 | 192 | 2012-11-21 |
| 13 | [Why Google Went Offline Today and a Bit about How the Internet Works](https://news.ycombinator.com/item?id=4747910) | 解释 Google 当天离线的原因，并介绍互联网运作方式。 | 676 | 154 | 2012-11-06 |
| 14 | [Nate Silver correctly called 50 out of 50 states](https://news.ycombinator.com/item?id=4752208) | Nate Silver 准确预测美国全部五十州的选举结果。 | 667 | 269 | 2012-11-07 |
| 15 | [Skrillex Quest](https://news.ycombinator.com/item?id=4851458) | 介绍名为 Skrillex Quest 的游戏。 | 592 | 197 | 2012-11-30 |
| 16 | [Ask HN: Help, HN'er in trouble, we need a laywer in Delhi immediately](https://news.ycombinator.com/item?id=4739649) | 一位 HN 用户在印度被警方拘留，社区紧急寻找德里律师。 | 591 | 108 | 2012-11-04 |
| 17 | [Microsoft turns spoken English into spoken Mandarin – in the same voice](https://news.ycombinator.com/item?id=4759620) | 微软展示保留说话者音色的英语语音转普通话技术。 | 583 | 121 | 2012-11-08 |
| 18 | [How I made $500k with machine learning and high frequency trading](https://news.ycombinator.com/item?id=4748624) | 作者分享用机器学习与高频交易赚取五十万美元的经历。 | 551 | 308 | 2012-11-06 |
| 19 | [Low-cost Solution to Clearing Afghan Landmines](https://news.ycombinator.com/item?id=4808061) | 介绍低成本清除阿富汗地雷的方案。 | 548 | 171 | 2012-11-20 |
| 20 | [You can do it alone](https://news.ycombinator.com/item?id=4799163) | 鼓励读者相信自己可以独立完成事情。 | 534 | 170 | 2012-11-17 |

## 2012-12

有效主帖 19,017 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [I love you, dad](https://news.ycombinator.com/item?id=4916629) | 作者以“爸爸，我爱你”表达对父亲的情感。 | 1104 | 209 | 2012-12-13 |
| 2 | [Thinking of Selling on eBay using Paypal? Think Again](https://news.ycombinator.com/item?id=4867484) | 提醒打算通过 PayPal 在 eBay 销售商品的人审慎考虑。 | 989 | 388 | 2012-12-03 |
| 3 | [Thinking the unthinkable](https://news.ycombinator.com/item?id=4927404) | 探讨如何思考原本被认为无法想象的事情。 | 963 | 442 | 2012-12-16 |
| 4 | [Google Maps for iOS](https://news.ycombinator.com/item?id=4914089) | Google 地图推出 iOS 版本。 | 827 | 447 | 2012-12-13 |
| 5 | [Page Weight Matters](https://news.ycombinator.com/item?id=4957992) | 强调网页体积对使用体验的重要性。 | 717 | 164 | 2012-12-23 |
| 6 | [Apple - Think Twice](https://news.ycombinator.com/item?id=4865826) | 以“再想一次”的说法回应苹果及其产品选择。 | 714 | 395 | 2012-12-03 |
| 7 | [You’re not anonymous. I know your name, email, and company.](https://news.ycombinator.com/item?id=4907609) | 作者指出网络用户可能暴露姓名、邮箱与公司身份。 | 710 | 231 | 2012-12-11 |
| 8 | [Everything You Know About Fitness is a Lie (2011)](https://news.ycombinator.com/item?id=4971196) | 重读一篇于 2011 年挑战常见健身观念的文章。 | 708 | 331 | 2012-12-26 |
| 9 | [The Gift](https://news.ycombinator.com/item?id=4934739) | 以“礼物”为题展开一段叙事。 | 669 | 173 | 2012-12-17 |
| 10 | [Notch trying jsFiddle](https://news.ycombinator.com/item?id=4862830) | Notch 尝试使用 jsFiddle。 | 659 | 134 | 2012-12-02 |
| 11 | [Why I Quit Being So Accommodating (1922)](https://news.ycombinator.com/item?id=4969041) | 分享一篇 1922 年谈不再过分迁就他人的文章。 | 650 | 162 | 2012-12-26 |
| 12 | [Great HN parody](https://news.ycombinator.com/item?id=4881042) | 推荐一则对 Hacker News 的戏仿作品。 | 642 | 163 | 2012-12-06 |
| 13 | [The Web We Lost](https://news.ycombinator.com/item?id=4917828) | 回顾与反思人们失去的早期 Web 体验。 | 636 | 153 | 2012-12-13 |
| 14 | [Google Apps stops accepting free sign-ups](https://news.ycombinator.com/item?id=4884665) | Google Apps 停止接受新的免费注册。 | 626 | 455 | 2012-12-07 |
| 15 | [Dropbox Hires Guido Van Rossum](https://news.ycombinator.com/item?id=4888502) | Dropbox 聘用 Python 创造者 Guido van Rossum。 | 586 | 207 | 2012-12-07 |
| 16 | [How would I get started?](https://news.ycombinator.com/item?id=4894990) | 围绕“我该如何开始”寻求迈出第一步的思路。 | 561 | 141 | 2012-12-09 |
| 17 | [Lego Finds Discontinued Set For Boy Who Saved Up For 2 Years](https://news.ycombinator.com/item?id=4870652) | 乐高为一名攒钱两年的男孩找到已停产的套装。 | 557 | 194 | 2012-12-04 |
| 18 | [Cards Against Humanity: Results of "pay what you want"](https://news.ycombinator.com/item?id=4933655) | Cards Against Humanity 公布“随意付费”实验结果。 | 549 | 162 | 2012-12-17 |
| 19 | [Two Billion Pixel Photo of Mount Everest (can you find the climbers?)](https://news.ycombinator.com/item?id=4943361) | 展示珠穆朗玛峰二十亿像素照片，邀请读者寻找登山者。 | 549 | 165 | 2012-12-19 |
| 20 | [How to terminate your worst enemy's Dropbox account for only $795](https://news.ycombinator.com/item?id=4962975) | 文章提出花 795 美元封禁他人 Dropbox 账户的做法。 | 542 | 285 | 2012-12-24 |

## 2013-01

有效主帖 21,996 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Aaron Swartz commits suicide](https://news.ycombinator.com/item?id=5046845) | 互联网活动家 Aaron Swartz 自杀身亡的消息及其引发的关注。 | 2103 | 546 | 2013-01-12 |
| 2 | [What It's Like To Be Ridiculed For Open Sourcing A Project](https://news.ycombinator.com/item?id=5106767) | 一位开发者讲述将项目开源后遭到嘲讽的亲身经历。 | 1331 | 781 | 2013-01-24 |
| 3 | [Prosecutor as bully](https://news.ycombinator.com/item?id=5048301) | 作者以“检察官如同霸凌者”为题，批评检方行使权力的方式。 | 1200 | 260 | 2013-01-12 |
| 4 | [Proposition HN: I will pay $8000 for you to build your side-project/MVP](https://news.ycombinator.com/item?id=5037694) | 发帖者提出出资八千美元，资助技术人才开发自己的副业项目或最小可行产品。 | 1088 | 377 | 2013-01-10 |
| 5 | [Y Combinator is funding the future of spam in Windows](https://news.ycombinator.com/item?id=5059806) | 作者指责 Y Combinator 资助的项目助长 Windows 平台上的垃圾软件问题。 | 1065 | 455 | 2013-01-15 |
| 6 | [Turn your browser into a notepad with one line](https://news.ycombinator.com/item?id=5135194) | 只需一行代码，就能把浏览器页面变成可编辑的记事本。 | 956 | 178 | 2013-01-29 |
| 7 | [Why the Fuck?](https://news.ycombinator.com/item?id=5088815) | 一篇以直白的“为什么？”为题、带有强烈情绪的个人随笔。 | 911 | 499 | 2013-01-20 |
| 8 | [For 40 Years, This Russian Family Was Cut Off From All Human Contact](https://news.ycombinator.com/item?id=5134023) | 一个俄罗斯家庭与外界隔绝四十年的生活故事。 | 842 | 244 | 2013-01-29 |
| 9 | [The Truth About Aaron Swartz's "Crime"](https://news.ycombinator.com/item?id=5048820) | 围绕 Aaron Swartz 被指控的“罪行”，作者提出自己的事实梳理与看法。 | 837 | 89 | 2013-01-12 |
| 10 | [I want the world to scroll this way](https://news.ycombinator.com/item?id=5043388) | 作者展示自己希望网页采用的滚动阅读方式。 | 832 | 299 | 2013-01-11 |
| 11 | [Make the Metric system the standard in the United States](https://news.ycombinator.com/item?id=4996278) | 一份呼吁美国将公制确立为标准计量体系的请愿。 | 820 | 530 | 2013-01-02 |
| 12 | [Petition the Whitehouse to remove Carmen Ortiz from office](https://news.ycombinator.com/item?id=5048699) | 一份要求免除联邦检察官 Carmen Ortiz 职务的白宫请愿。 | 801 | 234 | 2013-01-12 |
| 13 | [Pixels don’t care](https://news.ycombinator.com/item?id=5130559) | 作者以“像素并不在乎”为题，表达对数字设计的思考。 | 764 | 133 | 2013-01-28 |
| 14 | [Megafail](https://news.ycombinator.com/item?id=5101318) | 题为《Megafail》的技术文章，标题以戏谑方式表达对失败的批评。 | 738 | 198 | 2013-01-23 |
| 15 | [Meet Watsi, Y Combinator's First Nonprofit](https://news.ycombinator.com/item?id=5117385) | 认识 Watsi，这家获得 Y Combinator 支持的首个非营利机构。 | 705 | 168 | 2013-01-25 |
| 16 | [Youth expelled from Montreal college after finding security flaw](https://news.ycombinator.com/item?id=5090007) | 蒙特利尔一名学生发现安全漏洞后，遭到所在学院开除。 | 696 | 300 | 2013-01-21 |
| 17 | [Official Statement from the family and partner of Aaron Swartz](https://news.ycombinator.com/item?id=5049225) | Aaron Swartz 的家人与伴侣就其去世发表正式声明。 | 682 | 144 | 2013-01-12 |
| 18 | [Tron Legacy (2010)](https://news.ycombinator.com/item?id=5093397) | 分享与二〇一〇年电影《创：战纪》有关的项目作品。 | 657 | 143 | 2013-01-21 |
| 19 | [If I get hit by a truck...](https://news.ycombinator.com/item?id=5048085) | Aaron Swartz 留下的个人文字，设想自己遭遇意外后的安排。 | 651 | 50 | 2013-01-12 |
| 20 | [ How Newegg crushed the “shopping cart” patent and saved online retail](https://news.ycombinator.com/item?id=5125770) | Newegg 如何击败“购物车”专利诉讼，以及这场胜诉对网络零售的意义。 | 638 | 134 | 2013-01-27 |

## 2013-02

有效主帖 21,387 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [A Most Peculiar Test Drive](https://news.ycombinator.com/item?id=5218288) | Tesla 以“一次极不寻常的试驾”为题，回应有关车辆试驾的争议。 | 1859 | 578 | 2013-02-14 |
| 2 | [Heroku's Ugly Secret: The story of how the cloud-king turned its back on Rails](https://news.ycombinator.com/item?id=5215884) | 作者批评 Heroku 对 Rails 的支持，并追述这家云平台的转变。 | 1763 | 423 | 2013-02-13 |
| 3 | [Bomberman massively multiplayer in HTML5](https://news.ycombinator.com/item?id=5291843) | 在浏览器里体验以 HTML5 实现的大规模多人《炸弹人》游戏。 | 1394 | 201 | 2013-02-27 |
| 4 | [Hello Chrome, it’s Firefox calling](https://news.ycombinator.com/item?id=5166229) | Firefox 以向 Chrome“打电话”的方式，展示两款浏览器之间的通信。 | 1388 | 69 | 2013-02-04 |
| 5 | [Hello Firefox, this is Chrome calling](https://news.ycombinator.com/item?id=5166239) | Chrome 从自己的视角介绍与 Firefox 进行浏览器间通话的演示。 | 1386 | 178 | 2013-02-04 |
| 6 | [Why HN was down](https://news.ycombinator.com/item?id=5239673) | HN 解释整夜宕机的原因：手工调整评论时误建了循环引用。 | 1049 | 287 | 2013-02-18 |
| 7 | [Opera moves to WebKit](https://news.ycombinator.com/item?id=5211953) | Opera 宣布改用 WebKit，浏览器渲染引擎迎来重要变化。 | 938 | 282 | 2013-02-13 |
| 8 | [I'd like to use the web my way, thank you very much Quora](https://news.ycombinator.com/item?id=5217052) | 作者针对 Quora 的使用限制，主张按自己的方式浏览网页。 | 902 | 261 | 2013-02-14 |
| 9 | [Meteorite crash in Russia](https://news.ycombinator.com/item?id=5224616) | 俄罗斯发生陨石坠落事件，相关现场消息引发关注。 | 862 | 295 | 2013-02-15 |
| 10 | [We Found Our Son in the Subway](https://news.ycombinator.com/item?id=5300499) | 一段从在地铁里发现孩子开始、最终成为家庭的个人故事。 | 839 | 175 | 2013-02-28 |
| 11 | [No, I'm not going to download your bullshit app](https://news.ycombinator.com/item?id=5162841) | 作者表达对网站要求下载专用应用才能使用服务的不满。 | 799 | 218 | 2013-02-04 |
| 12 | [The Star Wars Route: Do a traceroute to 216.81.59.173](https://news.ycombinator.com/item?id=5192656) | 向指定 IP 执行 traceroute，可以看到一条带有《星球大战》趣味的网络路径。 | 770 | 78 | 2013-02-09 |
| 13 | [Google Glass](https://news.ycombinator.com/item?id=5249841) | Google 展示可穿戴眼镜产品 Google Glass。 | 763 | 574 | 2013-02-20 |
| 14 | [Packets of Death](https://news.ycombinator.com/item?id=5177815) | 题为《致命数据包》的技术文章，关注网络数据包引发的异常问题。 | 734 | 113 | 2013-02-06 |
| 15 | [Civilized Discourse Construction Kit](https://news.ycombinator.com/item?id=5172905) | 介绍旨在帮助人们开展文明在线讨论的工具。 | 727 | 270 | 2013-02-05 |
| 16 | [Learn Git Branching](https://news.ycombinator.com/item?id=5232415) | 通过交互式练习理解 Git 分支与相关操作。 | 717 | 137 | 2013-02-16 |
| 17 | [I am under surveillance by Canadian agents, my computer has been backdoored](https://news.ycombinator.com/item?id=5194489) | 作者声称遭到加拿大情报人员监控，并怀疑自己的电脑被植入后门。 | 701 | 341 | 2013-02-09 |
| 18 | [Why we don't hire programmers based on puzzles and tricks](https://news.ycombinator.com/item?id=5264312) | 作者解释招聘程序员时为何不以脑筋急转弯和技巧题为依据。 | 648 | 442 | 2013-02-22 |
| 19 | [Andrew Mason's statement about being fired as Groupon CEO](https://news.ycombinator.com/item?id=5301133) | Andrew Mason 就被免去 Groupon 首席执行官职务发表个人声明。 | 646 | 186 | 2013-02-28 |
| 20 | [Employees leave managers, not companies](https://news.ycombinator.com/item?id=5176140) | 作者主张，员工离职往往源于与经理的关系，而非公司本身。 | 625 | 257 | 2013-02-06 |

## 2013-03

有效主帖 22,734 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Google Reader shutting down](https://news.ycombinator.com/item?id=5371725) | Google 宣布关闭 RSS 阅读服务 Google Reader。 | 1964 | 695 | 2013-03-13 |
| 2 | [Breaking down Amazon's mega dropdown](https://news.ycombinator.com/item?id=5330998) | 拆解 Amazon 大型下拉菜单的交互设计，观察它如何响应鼠标移动。 | 1734 | 191 | 2013-03-06 |
| 3 | [The PyCon Incident](https://news.ycombinator.com/item?id=5410515) | 围绕 PyCon 会议上发生的一起争议事件展开叙述。 | 1125 | 986 | 2013-03-20 |
| 4 | [Diamonds Are Bullshit](https://news.ycombinator.com/item?id=5403988) | 作者质疑钻石的价值叙事，挑战人们对钻石的普遍看法。 | 1088 | 734 | 2013-03-19 |
| 5 | [Adria Richards, PyCon, and How We All Lost](https://news.ycombinator.com/item?id=5419071) | 作者评议 Adria Richards 与 PyCon 争议，认为各方都付出了代价。 | 1023 | 367 | 2013-03-21 |
| 6 | [How I spend my first 5 minutes on a server](https://news.ycombinator.com/item?id=5316093) | 作者分享接手一台服务器后，最初五分钟会做的操作。 | 960 | 341 | 2013-03-04 |
| 7 | [Show HN: XKCD-inspired StackSort](https://news.ycombinator.com/item?id=5395463) | 展示受 XKCD 启发而制作的排序项目 StackSort。 | 948 | 198 | 2013-03-18 |
| 8 | [Why I'm switching back to Firefox](https://news.ycombinator.com/item?id=5355560) | 作者解释自己为何决定重新使用 Firefox 浏览器。 | 928 | 423 | 2013-03-11 |
| 9 | [Flat UI: Free Web User Interface Kit](https://news.ycombinator.com/item?id=5321603) | Flat UI 提供一套免费的网页用户界面组件与样式。 | 872 | 191 | 2013-03-04 |
| 10 | [Show HN: 6 months ago I quit my job to pursue indie dev. Here is our first game](https://news.ycombinator.com/item?id=5332317) | 辞职投身独立开发半年后，作者展示团队完成的第一款游戏。 | 858 | 329 | 2013-03-06 |
| 11 | [The DDoS that almost broke the Internet](https://news.ycombinator.com/item?id=5450410) | Cloudflare 回顾一场规模巨大的 DDoS 攻击及其影响。 | 830 | 171 | 2013-03-27 |
| 12 | [You just went to the Google homepage. What actually happened?](https://news.ycombinator.com/item?id=5408597) | 从访问 Google 首页出发，追问一次网页请求背后究竟发生了什么。 | 808 | 144 | 2013-03-20 |
| 13 | [Procrastination is Not Laziness](https://news.ycombinator.com/item?id=5378462) | 作者探讨拖延行为，反对简单地将其归结为懒惰。 | 771 | 173 | 2013-03-15 |
| 14 | [White House Response to “Make Unlocking Cell Phones Legal”](https://news.ycombinator.com/item?id=5319577) | 白宫回应要求将手机解锁合法化的公众请愿。 | 752 | 274 | 2013-03-04 |
| 15 | [What really happened at PyCon 2013](https://news.ycombinator.com/item?id=5420840) | 作者讲述自己所了解的 PyCon 2013 争议经过。 | 746 | 104 | 2013-03-22 |
| 16 | [Unfit for work](https://news.ycombinator.com/item?id=5424241) | 围绕“无法工作”这一处境，观察相关人群与社会问题。 | 738 | 447 | 2013-03-22 |
| 17 | [Show HN: Weekend project, Intro.js](https://news.ycombinator.com/item?id=5380056) | 展示周末制作的 Intro.js 项目，供读者了解和体验。 | 716 | 154 | 2013-03-15 |
| 18 | [Amazon stops selling Sim City V over game issues](https://news.ycombinator.com/item?id=5339852) | 由于游戏出现问题，Amazon 暂停销售《模拟城市》第五代作品。 | 708 | 434 | 2013-03-07 |
| 19 | [I Bought A Firetruck](https://news.ycombinator.com/item?id=5432962) | 作者讲述自己购买一辆消防车的经历。 | 708 | 273 | 2013-03-24 |
| 20 | [Automatic: Your Smart Driving Assistant](https://news.ycombinator.com/item?id=5362265) | 认识名为 Automatic 的智能驾驶助手产品。 | 690 | 295 | 2013-03-12 |

## 2013-04

有效主帖 22,251 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Gitmo Is Killing Me](https://news.ycombinator.com/item?id=5549564) | 一位关塔那摩被关押者以“这里正在杀死我”为题讲述处境。 | 1333 | 521 | 2013-04-15 |
| 2 | [Path texts my entire phonebook at 6 AM](https://news.ycombinator.com/item?id=5632934) | 作者称 Path 在早晨六点向自己的整个通讯录发送了短信。 | 1223 | 409 | 2013-04-30 |
| 3 | [Tearable Cloth Simulation in JavaScript](https://news.ycombinator.com/item?id=5592679) | 用 JavaScript 实现可被撕裂的布料模拟，展示交互式物理效果。 | 1048 | 153 | 2013-04-23 |
| 4 | [If the Earth were 100 pixels wide](https://news.ycombinator.com/item?id=5489039) | 把地球缩放到一百像素宽，感受天体之间距离的尺度。 | 996 | 208 | 2013-04-03 |
| 5 | [Here is today](https://news.ycombinator.com/item?id=5620893) | 名为“这就是今天”的网页作品，围绕当下这个时间点展开呈现。 | 899 | 112 | 2013-04-28 |
| 6 | [Explosions near Boston Marathon finish line](https://news.ycombinator.com/item?id=5553543) | 波士顿马拉松终点线附近发生爆炸，现场情况引发关注。 | 872 | 586 | 2013-04-15 |
| 7 | [Roger Ebert dies at 70 after battle with cancer](https://news.ycombinator.com/item?id=5494767) | 影评人 Roger Ebert 因癌症去世，享年七十岁。 | 841 | 167 | 2013-04-04 |
| 8 | [BitTorrent’s Secure Dropbox Alternative Goes Public](https://news.ycombinator.com/item?id=5595806) | BitTorrent 面向公众推出一款强调安全、定位类似 Dropbox 的服务。 | 770 | 283 | 2013-04-23 |
| 9 | [Linode hacked, CCs and passwords leaked](https://news.ycombinator.com/item?id=5552756) | Linode 遭到入侵，信用卡资料与密码被曝泄露。 | 753 | 404 | 2013-04-15 |
| 10 | [Blink: A rendering engine for the Chromium project](https://news.ycombinator.com/item?id=5489025) | Chromium 项目公布新的浏览器渲染引擎 Blink。 | 729 | 304 | 2013-04-03 |
| 11 | [Taping of Farm Cruelty Is Becoming the Crime](https://news.ycombinator.com/item?id=5510914) | 围绕农场虐待动物的取证，报道拍摄行为本身受到法律追究的趋势。 | 717 | 437 | 2013-04-08 |
| 12 | [Don't Copy-Paste from Website to Terminal](https://news.ycombinator.com/item?id=5508225) | 提醒用户注意从网页复制命令到终端时可能遇到的安全风险。 | 689 | 258 | 2013-04-07 |
| 13 | [You know, Google, the web already had this feature](https://news.ycombinator.com/item?id=5534882) | 作者质疑 Google 推出的某项功能，认为网页原本已有类似能力。 | 667 | 429 | 2013-04-11 |
| 14 | [What happens when you wring out a washcloth in space [video]](https://news.ycombinator.com/item?id=5575469) | 通过太空中的拧毛巾实验，观察失重环境下水会如何运动。 | 656 | 109 | 2013-04-19 |
| 15 | [Why Rackspace Is Suing The Most Notorious Patent Troll In America](https://news.ycombinator.com/item?id=5494777) | Rackspace 解释为何起诉一家被其视为恶名昭著的专利诉讼公司。 | 622 | 101 | 2013-04-04 |
| 16 | [You are not Steve Jobs](https://news.ycombinator.com/item?id=5578642) | 作者以“你不是 Steve Jobs”为题，反思对这位企业家的模仿。 | 616 | 298 | 2013-04-19 |
| 17 | [Helios](https://news.ycombinator.com/item?id=5480929) | 认识名为 Helios 的项目，浏览其公开介绍。 | 586 | 66 | 2013-04-02 |
| 18 | ["Asswipe," replied Yahoo's server. That's when I knew I had it](https://news.ycombinator.com/item?id=5569102) | 作者回忆 Yahoo 服务器返回一句粗话后，确认自己取得突破的经历。 | 573 | 104 | 2013-04-18 |
| 19 | [French homeland intelligence threatens a sysop into deleting a Wikipedia Article](https://news.ycombinator.com/item?id=5503354) | 法国国内情报部门被指威胁维基百科管理员，要求删除一篇条目。 | 570 | 189 | 2013-04-06 |
| 20 | [I Knew a Programmer Who Went Completely Insane](https://news.ycombinator.com/item?id=5575144) | 作者回忆一名自己认识、精神状态发生严重变化的程序员。 | 559 | 321 | 2013-04-19 |

## 2013-05

有效主帖 22,055 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Depression Part Two](https://news.ycombinator.com/item?id=5684773) | 作者继续讲述自己与抑郁症相处的个人经历。 | 977 | 240 | 2013-05-10 |
| 2 | [Send money with Gmail](https://news.ycombinator.com/item?id=5714197) | Google 推出通过 Gmail 向他人转账的功能。 | 779 | 244 | 2013-05-15 |
| 3 | [Induction powered LED lit engagement ring](https://news.ycombinator.com/item?id=5748854) | 展示一枚通过感应供电、能让 LED 发光的订婚戒指。 | 771 | 76 | 2013-05-22 |
| 4 | [Show HN: My seven minute workout timer evening project](https://news.ycombinator.com/item?id=5720648) | 作者展示利用晚间时间制作的七分钟锻炼计时器。 | 760 | 155 | 2013-05-16 |
| 5 | [Show HN: Automatic weekly meal planner, also plans your leftovers](https://news.ycombinator.com/item?id=5640336) | 自动安排每周饮食的工具，连剩菜的后续利用也纳入计划。 | 747 | 288 | 2013-05-01 |
| 6 | [Flickr gets new UI, new Android app, 1 TB free space](https://news.ycombinator.com/item?id=5740153) | Flickr 更新网页界面与 Android 应用，并提供一 TB 免费存储空间。 | 743 | 359 | 2013-05-20 |
| 7 | [Ubuntu's Bug #1 is fixed](https://news.ycombinator.com/item?id=5791981) | Ubuntu 将编号为一的标志性问题标记为已解决。 | 690 | 191 | 2013-05-30 |
| 8 | [Google Abandons Open Standards for Instant Messaging](https://news.ycombinator.com/item?id=5758346) | 作者批评 Google 放弃即时通信领域的开放标准。 | 677 | 196 | 2013-05-23 |
| 9 | [Tesla Repays Department of Energy Loan Nine Years Early](https://news.ycombinator.com/item?id=5753443) | Tesla 宣布提前九年偿还美国能源部贷款。 | 670 | 180 | 2013-05-22 |
| 10 | [The One-Person Product](https://news.ycombinator.com/item?id=5740105) | 围绕由一个人独立打造和经营的产品，讨论其特点与可能性。 | 666 | 103 | 2013-05-20 |
| 11 | [Windows NT Kernel Contributor Explains Why Performance is Behind Other OS](https://news.ycombinator.com/item?id=5689731) | 一位 Windows NT 内核贡献者解释，他为何认为其性能落后于其他系统。 | 656 | 295 | 2013-05-11 |
| 12 | [Letter To A Young Programmer Considering A Startup](https://news.ycombinator.com/item?id=5789637) | 写给考虑创业的年轻程序员的一封信，讨论这一职业选择。 | 643 | 148 | 2013-05-29 |
| 13 | [Announcing Online MS in Computer Science in Collaboration with Georgia Tech](https://news.ycombinator.com/item?id=5709445) | Udacity 宣布与佐治亚理工合作推出在线计算机科学硕士项目。 | 634 | 189 | 2013-05-15 |
| 14 | [US entertainment industry to Congress: make it legal for us to deploy rootkits](https://news.ycombinator.com/item?id=5773020) | 报道美国娱乐产业要求国会允许其部署 rootkit 的主张。 | 608 | 257 | 2013-05-27 |
| 15 | [Software will not be patentable in New Zealand](https://news.ycombinator.com/item?id=5678477) | 报道新西兰拟将软件排除在可授予专利的范围之外。 | 592 | 122 | 2013-05-09 |
| 16 | [Why Isn't Gatsby in the Public Domain?](https://news.ycombinator.com/item?id=5670719) | 追问《了不起的盖茨比》为何尚未进入公有领域。 | 590 | 183 | 2013-05-07 |
| 17 | [The New Yorker Strongbox](https://news.ycombinator.com/item?id=5712098) | 《纽约客》推出名为 Strongbox 的信息提交渠道。 | 583 | 164 | 2013-05-15 |
| 18 | [Show HN: Remove backgrounds from images online](https://news.ycombinator.com/item?id=5682831) | 展示可以在线去除图片背景的工具。 | 571 | 140 | 2013-05-09 |
| 19 | [I Don't Want Your Fucking App](https://news.ycombinator.com/item?id=5694173) | 作者表达对被要求使用专用应用的不满。 | 560 | 256 | 2013-05-12 |
| 20 | [Scientists Back Kiera Wilmot by Tweeting About All the Stuff They've Blown Up](https://news.ycombinator.com/item?id=5650896) | 科学家通过分享自己实验中引发爆炸的经历，声援 Kiera Wilmot。 | 558 | 219 | 2013-05-03 |

## 2013-06

有效主帖 21,929 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [This is a web page](https://news.ycombinator.com/item?id=5913381) | 一张以“这是一张网页”为主题、回到网页文字本身的页面。 | 1354 | 420 | 2013-06-20 |
| 2 | [NSA leaker is a patriot, not a traitor](https://news.ycombinator.com/item?id=5857025) | 作者认为，泄露 NSA 监控信息的人应被视为爱国者。 | 1268 | 327 | 2013-06-10 |
| 3 | [Edward Snowden: the whistleblower behind revelations of NSA surveillance](https://news.ycombinator.com/item?id=5849932) | Edward Snowden 公开身份，成为揭露 NSA 监控活动的告密者。 | 1254 | 293 | 2013-06-09 |
| 4 | [Confirmed: The NSA is Spying on Millions of Americans](https://news.ycombinator.com/item?id=5830633) | 电子前哨基金会称，NSA 对数百万美国人的监控得到证实。 | 1227 | 444 | 2013-06-06 |
| 5 | [Project Loon](https://news.ycombinator.com/item?id=5883790) | 认识 Google 的 Project Loon 项目及其公开介绍。 | 1094 | 286 | 2013-06-15 |
| 6 | [What is Happening in Istanbul?](https://news.ycombinator.com/item?id=5807941) | 追问伊斯坦布尔正在发生什么，关注当地局势。 | 1007 | 485 | 2013-06-02 |
| 7 | [US intelligence mining data from 9 US Internet companies in broad secret program](https://news.ycombinator.com/item?id=5835432) | 报道美国情报机构通过秘密项目，从九家互联网公司获取数据。 | 997 | 385 | 2013-06-06 |
| 8 | [NSA admits listening to U.S. phone calls without warrants](https://news.ycombinator.com/item?id=5886686) | 报道 NSA 承认曾在没有搜查令的情况下监听美国电话。 | 834 | 389 | 2013-06-15 |
| 9 | [Has the US become the type of nation from which you have to seek asylum?](https://news.ycombinator.com/item?id=5853536) | 作者追问，美国是否已成为有人需要逃离并寻求庇护的国家。 | 827 | 341 | 2013-06-10 |
| 10 | [Cowards](https://news.ycombinator.com/item?id=5843780) | 一篇题为《懦夫》的评论，标题体现作者鲜明的批评态度。 | 793 | 225 | 2013-06-08 |
| 11 | [Ultimate Tic Tac Toe](https://news.ycombinator.com/item?id=5898506) | 介绍“终极井字棋”，探索传统井字棋之外的规则变化。 | 786 | 123 | 2013-06-18 |
| 12 | [Bruce Schneier joins EFF Board of Directors](https://news.ycombinator.com/item?id=5953141) | 安全专家 Bruce Schneier 加入电子前哨基金会董事会。 | 754 | 36 | 2013-06-27 |
| 13 | [U.S. charges Edward Snowden with espionage](https://news.ycombinator.com/item?id=5921347) | 美国政府以间谍罪相关指控起诉 Edward Snowden。 | 749 | 346 | 2013-06-21 |
| 14 | [Petition to Pardon Edward Snowden](https://news.ycombinator.com/item?id=5850590) | 一份请求美国总统赦免 Edward Snowden 的公众请愿。 | 748 | 179 | 2013-06-09 |
| 15 | [Are coders worth it?](https://news.ycombinator.com/item?id=5831491) | 程序员的劳动究竟值多少钱，其报酬与社会价值是否相称？ | 730 | 305 | 2013-06-06 |
| 16 | [Kim Jong-il's Sushi Chef](https://news.ycombinator.com/item?id=5817014) | 走近曾为金正日制作寿司的厨师，了解他的经历。 | 728 | 101 | 2013-06-04 |
| 17 | [Oculus Rift co-founder killed by gang trying to escape police](https://news.ycombinator.com/item?id=5802474) | Oculus Rift 联合创始人在一伙人逃避警方追捕时遇害。 | 726 | 288 | 2013-06-01 |
| 18 | [Asking the U.S. to allow Google to publish more national security request data](https://news.ycombinator.com/item?id=5863353) | Google 请求美国政府允许公布更多国家安全信息索取数据。 | 717 | 182 | 2013-06-11 |
| 19 | [Larry Page addresses PRISM](https://news.ycombinator.com/item?id=5841228) | Larry Page 就 PRISM 监控项目发表回应。 | 715 | 441 | 2013-06-07 |
| 20 | [Hexagonal grids for games](https://news.ycombinator.com/item?id=5809724) | 介绍游戏中的六边形网格，帮助理解其布局与使用方式。 | 709 | 69 | 2013-06-02 |

## 2013-07

有效主帖 21,297 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [XKeyscore: NSA program collects 'nearly everything a user does on the internet'](https://news.ycombinator.com/item?id=6133349) | 报道 NSA 的 XKeyscore 项目，据称可收集用户几乎全部互联网活动。 | 1688 | 612 | 2013-07-31 |
| 2 | [I'm learning to code by building 180 websites in 180 days. Today is day 115](https://news.ycombinator.com/item?id=6097155) | 作者通过一百八十天搭建一百八十个网站学习编程，分享第一百一十五天的进展。 | 1542 | 344 | 2013-07-24 |
| 3 | [“Why did you shoot me? I was reading a book”](https://news.ycombinator.com/item?id=6001843) | 以“我只是在看书，你为什么开枪”为切口，关注一次枪击遭遇。 | 1310 | 408 | 2013-07-07 |
| 4 | [Do Things that Don't Scale](https://news.ycombinator.com/item?id=6041765) | 作者建议创业者主动做一些暂时无法规模化的事情。 | 1275 | 207 | 2013-07-14 |
| 5 | [Ubuntu Edge](https://news.ycombinator.com/item?id=6084099) | Ubuntu Edge 项目发起众筹，展示其产品构想。 | 1188 | 378 | 2013-07-22 |
| 6 | [Doug Engelbart has died](https://news.ycombinator.com/item?id=5986307) | 计算机先驱 Doug Engelbart 去世的消息。 | 1178 | 94 | 2013-07-03 |
| 7 | [Victory Lap for Ask Patents](https://news.ycombinator.com/item?id=6084110) | 作者回顾 Ask Patents 取得的成果，并庆祝这一项目的进展。 | 1075 | 151 | 2013-07-22 |
| 8 | [Quine Relay](https://news.ycombinator.com/item?id=6048761) | 展示名为 Quine Relay 的程序项目，探索自我复制程序的接力玩法。 | 983 | 177 | 2013-07-15 |
| 9 | [Statement from Edward Snowden in Moscow](https://news.ycombinator.com/item?id=5973896) | Edward Snowden 在莫斯科发表声明，说明自己的立场与处境。 | 954 | 483 | 2013-07-01 |
| 10 | [Hospital creates bidding war by posting pricing online](https://news.ycombinator.com/item?id=6014794) | 一家医院把价格公布到网上，引发医疗服务的价格竞争。 | 868 | 226 | 2013-07-09 |
| 11 | [Restore the Fourth](https://news.ycombinator.com/item?id=5991375) | 介绍名为 Restore the Fourth 的公众行动。 | 772 | 173 | 2013-07-04 |
| 12 | [Forgotten Employee (2002)](https://news.ycombinator.com/item?id=6087935) | 重读二〇〇二年的《被遗忘的员工》，关注一名员工被组织忽略的故事。 | 747 | 291 | 2013-07-23 |
| 13 | [The Drone that Killed my Grandson](https://news.ycombinator.com/item?id=6061816) | 一位祖父讲述自己的孙子在无人机袭击中丧生的经历。 | 708 | 357 | 2013-07-18 |
| 14 | [Kathy Sierra: Your app makes me fat](https://news.ycombinator.com/item?id=6124462) | Kathy Sierra 以“你的应用让我变胖”为题，反思应用对用户生活的影响。 | 682 | 203 | 2013-07-29 |
| 15 | [Obama Promises Disappear from Web](https://news.ycombinator.com/item?id=6106388) | 报道 Obama 曾作出的承诺从网页上消失的情况。 | 657 | 162 | 2013-07-26 |
| 16 | [I understood gender discrimination once I added “Mr.” to my resume](https://news.ycombinator.com/item?id=6033567) | 求职者在简历姓名前加上“先生”后接连获得面试，由此反思性别歧视。 | 643 | 376 | 2013-07-12 |
| 17 | [Psd.rb](https://news.ycombinator.com/item?id=6129237) | 介绍名为 Psd.rb 的开发项目及其公开发布。 | 629 | 92 | 2013-07-30 |
| 18 | [Lockdown](https://news.ycombinator.com/item?id=5982624) | 一篇题为《封锁》的个人文章，供读者了解作者的观点。 | 625 | 217 | 2013-07-03 |
| 19 | [The Future of Programming](https://news.ycombinator.com/item?id=6129148) | 围绕编程的未来，探索程序设计可能走向何处。 | 614 | 341 | 2013-07-30 |
| 20 | [Human-Powered Helicopter Wins the $250,000 Sikorsky Prize](https://news.ycombinator.com/item?id=6028326) | 一架人力直升机赢得二十五万美元的 Sikorsky 奖。 | 601 | 95 | 2013-07-11 |

## 2013-08

有效主帖 21,066 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Don't Fly During Ramadan](https://news.ycombinator.com/item?id=6258422) | 一篇以“不要在斋月乘机”为题的出行警示文章。 | 2744 | 962 | 2013-08-22 |
| 2 | [Hyperloop](https://news.ycombinator.com/item?id=6201586) | 认识 Hyperloop 高速交通概念及其公开方案。 | 2666 | 954 | 2013-08-12 |
| 3 | [Lavabit abruptly shuts down](https://news.ycombinator.com/item?id=6181081) | 电子邮件服务 Lavabit 突然宣布关闭。 | 1831 | 640 | 2013-08-08 |
| 4 | [Detaining my partner: a failed attempt at intimidation](https://news.ycombinator.com/item?id=6233646) | 作者认为，拘留其伴侣是一场未能奏效的恐吓。 | 1459 | 449 | 2013-08-18 |
| 5 | [Forced Exposure](https://news.ycombinator.com/item?id=6242569) | 作者以“被迫暴露”为题，表达对隐私处境的忧虑。 | 1391 | 414 | 2013-08-20 |
| 6 | [Microsoft CEO Steve Ballmer to retire within 12 months](https://news.ycombinator.com/item?id=6263205) | 微软宣布首席执行官 Steve Ballmer 将在十二个月内退休。 | 1227 | 763 | 2013-08-23 |
| 7 | [Skeuocard](https://news.ycombinator.com/item?id=6143604) | 介绍名为 Skeuocard 的项目，供读者查看其设计。 | 1066 | 196 | 2013-08-01 |
| 8 | [I will not do a tech interview](https://news.ycombinator.com/item?id=6251087) | 作者说明自己为何拒绝参加技术面试。 | 1032 | 542 | 2013-08-21 |
| 9 | [John Carmack joins Oculus as CTO](https://news.ycombinator.com/item?id=6172881) | John Carmack 加入 Oculus，担任首席技术官。 | 993 | 204 | 2013-08-07 |
| 10 | [Hi I’m Hank, and I bought a bus](https://news.ycombinator.com/item?id=6261948) | Hank 讲述购买一辆巴士的经历，并带读者参观车辆。 | 944 | 197 | 2013-08-23 |
| 11 | [New Zealand bans some software patents](https://news.ycombinator.com/item?id=6289187) | 新西兰禁止部分软件专利，相关法律边界受到关注。 | 902 | 221 | 2013-08-28 |
| 12 | [He got 1%, we can't hire him](https://news.ycombinator.com/item?id=6288763) | 围绕“他拿到了百分之一，所以不能录用”的说法，反思招聘判断。 | 835 | 576 | 2013-08-28 |
| 13 | [Tesla Model S achieves best safety rating of any car ever tested](https://news.ycombinator.com/item?id=6240862) | Tesla 宣布 Model S 获得其所称受测车辆中的最佳安全评级。 | 814 | 301 | 2013-08-20 |
| 14 | [Defeated](https://news.ycombinator.com/item?id=6275826) | 一篇题为《败下阵来》的个人文章，讲述作者的挫败感。 | 759 | 438 | 2013-08-26 |
| 15 | [“People simply empty out”](https://news.ycombinator.com/item?id=6221077) | 以“人会逐渐被掏空”为题，分享一段关于个人处境的文字。 | 723 | 463 | 2013-08-15 |
| 16 | [Groklaw legal site shuts over fears of NSA email snooping](https://news.ycombinator.com/item?id=6243081) | 法律网站 Groklaw 因担忧 NSA 监听电子邮件而关闭。 | 706 | 233 | 2013-08-20 |
| 17 | [David Miranda, schedule 7 and the danger that all reporters now face](https://news.ycombinator.com/item?id=6240151) | 作者从 David Miranda 事件出发，讨论法律条款给记者带来的风险。 | 681 | 152 | 2013-08-19 |
| 18 | [Grasshopper 100m Lateral Divert Test](https://news.ycombinator.com/item?id=6212248) | SpaceX 展示 Grasshopper 的一百米横向机动测试。 | 663 | 148 | 2013-08-14 |
| 19 | [We have an employee whose last name is Null. He kills our employee lookup (2012)](https://news.ycombinator.com/item?id=6140631) | 一名姓 Null 的员工让查询系统出错，引出姓名与空值混淆的问题。 | 661 | 236 | 2013-08-01 |
| 20 | [Judge sentences Bradley Manning to 35 years](https://news.ycombinator.com/item?id=6250431) | 法官判处 Bradley Manning 三十五年监禁。 | 640 | 471 | 2013-08-21 |

## 2013-09

有效主帖 20,689 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [SteamOS](https://news.ycombinator.com/item?id=6432306) | SteamOS 公开亮相，展示 Steam 的操作系统方案。 | 1436 | 513 | 2013-09-23 |
| 2 | [Google Web Designer](https://news.ycombinator.com/item?id=6470426) | Google 发布网页设计工具 Google Web Designer。 | 1126 | 442 | 2013-09-30 |
| 3 | [Why can a scam company raise $40 Million Series C + $76 Million Series B?](https://news.ycombinator.com/item?id=6455391) | 发帖者质疑 JustFab 的商业模式，并追问为何投资人仍愿投入巨额资金。 | 1065 | 461 | 2013-09-27 |
| 4 | [Chaos Computer Club breaks Apple TouchID](https://news.ycombinator.com/item?id=6427390) | 混沌计算机俱乐部宣布突破 Apple Touch ID 的指纹认证。 | 980 | 446 | 2013-09-22 |
| 5 | [I Am An Object Of Internet Ridicule, Ask Me Anything](https://news.ycombinator.com/item?id=6412708) | 一位成为网络嘲讽对象的人讲述自己的经历，并接受提问。 | 935 | 378 | 2013-09-19 |
| 6 | [N.S.A. Foils Much Internet Encryption](https://news.ycombinator.com/item?id=6336178) | 报道 NSA 有能力突破多种互联网加密保护。 | 923 | 388 | 2013-09-05 |
| 7 | [World](https://news.ycombinator.com/item?id=6390328) | 名为 World 的网页作品，供读者直接浏览和体验。 | 918 | 96 | 2013-09-15 |
| 8 | [Nokia acquired by Microsoft](https://news.ycombinator.com/item?id=6318525) | 微软宣布收购 Nokia 相关业务，双方发布公开说明。 | 865 | 553 | 2013-09-03 |
| 9 | [My Friends and I Bought an Island](https://news.ycombinator.com/item?id=6395148) | 作者讲述自己与朋友合伙买下一座岛的经历。 | 832 | 387 | 2013-09-16 |
| 10 | [Steam Controller](https://news.ycombinator.com/item?id=6457988) | Steam 公布游戏控制器 Steam Controller。 | 783 | 361 | 2013-09-27 |
| 11 | [The Feynman Lectures on Physics, Volume I](https://news.ycombinator.com/item?id=6380187) | 在线阅读《费曼物理学讲义》第一卷。 | 776 | 112 | 2013-09-13 |
| 12 | [The Frameless Geodesic Dome I currently live in](https://news.ycombinator.com/item?id=6355488) | 作者介绍自己目前居住的无框架测地穹顶建筑。 | 747 | 310 | 2013-09-09 |
| 13 | [Kit Kat's homepage is currently a parody of Android announcement page](https://news.ycombinator.com/item?id=6323572) | Kit Kat 官网用模仿 Android 发布页面的方式开展宣传。 | 741 | 189 | 2013-09-03 |
| 14 | [Show HN: Ditch Black Text to Read Faster, Easier](https://news.ycombinator.com/item?id=6335784) | 展示通过改变黑色文字呈现方式，让阅读更快、更轻松的工具。 | 739 | 262 | 2013-09-05 |
| 15 | [To my daughter's high school programming teacher](https://news.ycombinator.com/item?id=6357317) | 一位家长写信给女儿的高中编程老师，表达对编程教学的看法。 | 726 | 578 | 2013-09-10 |
| 16 | [Don't use Hadoop when your data isn't that big](https://news.ycombinator.com/item?id=6398650) | 作者建议，数据规模不大时应谨慎选择 Hadoop。 | 711 | 227 | 2013-09-17 |
| 17 | [How to Advertise on a Porn Website](https://news.ycombinator.com/item?id=6359555) | 分享在色情网站投放广告的做法与经验。 | 687 | 114 | 2013-09-10 |
| 18 | [NSA shares raw intelligence including Americans' data with Israel](https://news.ycombinator.com/item?id=6367465) | 报道 NSA 与以色列共享原始情报，其中包含美国人的数据。 | 673 | 172 | 2013-09-11 |
| 19 | [FBI Admits It Controlled Tor Servers Behind Mass Malware Attack](https://news.ycombinator.com/item?id=6382963) | FBI 承认曾接管 Freedom Hosting，随后相关服务器被发现向访客投放识别身份的恶意软件。 | 671 | 262 | 2013-09-13 |
| 20 | [Fucking Sue Me (2011)](https://news.ycombinator.com/item?id=6366912) | 作者以“尽管来告我”为题，表达对法律威胁的强硬态度。 | 663 | 194 | 2013-09-11 |

## 2013-10

有效主帖 22,592 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [NSA infiltrates links to Yahoo, Google data centers worldwide](https://news.ycombinator.com/item?id=6641378) | 报道 NSA 入侵 Google 与 Yahoo 全球数据中心之间的通信链路。 | 1604 | 592 | 2013-10-30 |
| 2 | [FBI raids alleged online drug market Silk Road, arrests owner](https://news.ycombinator.com/item?id=6482992) | FBI 查封涉嫌经营网络毒品交易的 Silk Road，并逮捕其经营者。 | 1101 | 577 | 2013-10-02 |
| 3 | [Mozilla bug 923590: Pledge never to implement HTML5 DRM](https://news.ycombinator.com/item?id=6493510) | Mozilla 的一项问题报告要求承诺永不实现 HTML5 数字版权管理。 | 904 | 357 | 2013-10-04 |
| 4 | [Dear Startups: stop asking me math puzzles to figure out if I can code](https://news.ycombinator.com/item?id=6583580) | 作者呼吁创业公司停止用数学谜题判断应聘者是否会写代码。 | 872 | 342 | 2013-10-21 |
| 5 | [Here's how I deal with users who steal](https://news.ycombinator.com/item?id=6630350) | 作者分享自己处理被认为存在盗取行为的用户的方式。 | 774 | 211 | 2013-10-28 |
| 6 | [Show HN: My x86 emulator written in JavaScript](https://news.ycombinator.com/item?id=6567967) | 作者展示用 JavaScript 编写的 x86 模拟器。 | 765 | 190 | 2013-10-17 |
| 7 | [Ask HN: Why the Microsoft hate?](https://news.ycombinator.com/item?id=6596038) | 发帖者质疑 HN 对微软相关消息的敌意，以及因品牌好恶举报帖子的做法。 | 763 | 530 | 2013-10-23 |
| 8 | [Square Cash](https://news.ycombinator.com/item?id=6557394) | 认识 Square Cash 服务及其公开产品介绍。 | 710 | 281 | 2013-10-16 |
| 9 | [Dr. Arjun Srinivasan: We’ve Reached “The End of Antibiotics, Period”](https://news.ycombinator.com/item?id=6599040) | Arjun Srinivasan 医生警告，人们正面临“抗生素时代终结”的局面。 | 692 | 400 | 2013-10-23 |
| 10 | [Scott Adams: How to Be Successful](https://news.ycombinator.com/item?id=6547912) | Scott Adams 分享自己对如何取得成功的看法。 | 690 | 184 | 2013-10-14 |
| 11 | [Attacking Tor: How the NSA targets users' online anonymity](https://news.ycombinator.com/item?id=6495771) | 报道 NSA 如何针对 Tor 用户，攻击其在线匿名性。 | 654 | 176 | 2013-10-04 |
| 12 | [Swiss to vote on 2,500 franc basic income for every adult](https://news.ycombinator.com/item?id=6499409) | 瑞士将就向每位成年人发放两千五百法郎基本收入的提议进行投票。 | 638 | 566 | 2013-10-05 |
| 13 | [After 180 Websites, I’m Ready to Start the Rest of My Life as a Coder](https://news.ycombinator.com/item?id=6489468) | 完成一百八十个网站后，作者准备正式开启程序员生涯。 | 624 | 371 | 2013-10-03 |
| 14 | [What I've been up to for the past year](https://news.ycombinator.com/item?id=6519175) | 作者回顾自己过去一年在做的事情与取得的进展。 | 616 | 171 | 2013-10-09 |
| 15 | [How to lose $172,222 a second for 45 minutes](https://news.ycombinator.com/item?id=6589508) | 复盘一场持续四十五分钟、平均每秒亏损十七万多美元的损失事件。 | 613 | 236 | 2013-10-22 |
| 16 | [Why You Shouldn't Interrupt a Programmer](https://news.ycombinator.com/item?id=6625714) | 解释为什么打断程序员会影响其工作。 | 607 | 204 | 2013-10-28 |
| 17 | [f.lux has been updated to a new version](https://news.ycombinator.com/item?id=6559077) | 屏幕调色工具 f.lux 发布新版本。 | 597 | 261 | 2013-10-16 |
| 18 | [Model S Fire](https://news.ycombinator.com/item?id=6497478) | Tesla 就 Model S 起火事件发表说明。 | 594 | 238 | 2013-10-04 |
| 19 | [Lavabit Defied FBI Demands to Turn Over Crypto Keys, Documents Show](https://news.ycombinator.com/item?id=6485562) | 公开文件显示，Lavabit 曾拒绝 FBI 索取加密密钥的要求。 | 592 | 250 | 2013-10-02 |
| 20 | [Fingerprints are Usernames, not Passwords](https://news.ycombinator.com/item?id=6477505) | 作者主张应把指纹理解为身份标识，而不是可以保密的密码。 | 587 | 255 | 2013-10-01 |

## 2013-11

有效主帖 22,298 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [A spreadsheet in fewer than 30 lines of JavaScript, no library used](https://news.ycombinator.com/item?id=6725387) | 不到三十行 JavaScript，不借助库实现一个电子表格。 | 1447 | 259 | 2013-11-13 |
| 2 | [Coin](https://news.ycombinator.com/item?id=6733615) | 认识名为 Coin 的产品及其公开介绍。 | 1387 | 690 | 2013-11-14 |
| 3 | [Started a stupid company. Failed. ](https://news.ycombinator.com/item?id=6805699) | 一位创业失败者讲述资金耗尽、住房被收回及养家压力交织的困境。 | 1344 | 407 | 2013-11-27 |
| 4 | [Sprite Lamp](https://news.ycombinator.com/item?id=6696691) | 名为 Sprite Lamp 的项目亮相，供读者了解其用途。 | 1323 | 126 | 2013-11-08 |
| 5 | [Google Security Team Member on NSA: "Fuck These Guys"](https://news.ycombinator.com/item?id=6680763) | 一位 Google 安全团队成员以激烈措辞表达对 NSA 的愤怒。 | 1217 | 396 | 2013-11-06 |
| 6 | [The second operating system hiding in every mobile phone](https://news.ycombinator.com/item?id=6722292) | 探寻手机里除了主系统之外，另一套鲜为人知的操作系统。 | 1036 | 261 | 2013-11-12 |
| 7 | [Winamp shutting down on December 20th, 2013](https://news.ycombinator.com/item?id=6769721) | Winamp 宣布将于二〇一三年十二月二十日停止运营。 | 957 | 500 | 2013-11-20 |
| 8 | [What 4chan thinks of HN](https://news.ycombinator.com/item?id=6747373) | 看看 4chan 用户如何评价 Hacker News 社区。 | 942 | 248 | 2013-11-17 |
| 9 | [How Hacker News ranking really works: scoring, controversy, and penalties](https://news.ycombinator.com/item?id=6799854) | 解析 HN 排名机制中的评分、争议因素与惩罚规则。 | 920 | 190 | 2013-11-26 |
| 10 | [Pencil ](https://news.ycombinator.com/item?id=6761297) | 认识名为 Pencil 的产品及其设计介绍。 | 882 | 366 | 2013-11-19 |
| 11 | [What It's Like to Fail](https://news.ycombinator.com/item?id=6756144) | 围绕失败是什么感受，讲述其中的个人体验。 | 834 | 317 | 2013-11-18 |
| 12 | [Patent war goes nuclear: Microsoft, Apple-owned “Rockstar” sues Google](https://news.ycombinator.com/item?id=6651704) | 微软和 Apple 参与持有的 Rockstar 起诉 Google，专利争端进一步升级。 | 785 | 528 | 2013-11-01 |
| 13 | [Dear Googles: Stop asking](https://news.ycombinator.com/item?id=6745525) | 作者向 Google 发出“别再问了”的呼吁，表达对相关请求的不满。 | 751 | 253 | 2013-11-16 |
| 14 | [Jolla](https://news.ycombinator.com/item?id=6808183) | 认识 Jolla 及其公开产品信息。 | 734 | 250 | 2013-11-27 |
| 15 | [Are You A Typing Hacker? Prove It](https://news.ycombinator.com/item?id=6659161) | 通过一款打字挑战，检验自己的键盘输入能力。 | 730 | 252 | 2013-11-02 |
| 16 | [Web GL Ocean Simulation](https://news.ycombinator.com/item?id=6802597) | 用 WebGL 在浏览器中模拟海洋波浪。 | 695 | 134 | 2013-11-26 |
| 17 | [Show HN: Probabilistically Generating HN Post Titles](https://news.ycombinator.com/item?id=6815282) | 展示以概率方式生成 Hacker News 帖子标题的项目。 | 683 | 260 | 2013-11-28 |
| 18 | [Basic Data Structures and Algorithms in the Linux Kernel](https://news.ycombinator.com/item?id=6787836) | 梳理 Linux 内核中使用的基础数据结构与算法。 | 682 | 59 | 2013-11-23 |
| 19 | [High Frequency Dating](https://news.ycombinator.com/item?id=6773841) | 作者以“高频约会”为题，探索一种看待约会的方式。 | 678 | 182 | 2013-11-21 |
| 20 | [A living death: Sentenced to die behind bars for what?](https://news.ycombinator.com/item?id=6743358) | 追问哪些行为会让人被判在监狱度过余生，以及这种刑罚的意义。 | 656 | 488 | 2013-11-16 |

## 2013-12

有效主帖 20,303 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Amazon Prime Air](https://news.ycombinator.com/item?id=6830566) | Amazon 公布名为 Prime Air 的配送项目。 | 1412 | 588 | 2013-12-02 |
| 2 | [Explain Shell](https://news.ycombinator.com/item?id=6834791) | Explain Shell 帮助读者理解 shell 命令的含义。 | 1372 | 171 | 2013-12-02 |
| 3 | [What I Didn't Say](https://news.ycombinator.com/item?id=6986797) | Paul Graham 以《我没有说过的话》为题，澄清自己的表达。 | 1289 | 567 | 2013-12-30 |
| 4 | [South Africa's Nelson Mandela dies](https://news.ycombinator.com/item?id=6857511) | 南非前总统 Nelson Mandela 去世的消息。 | 1137 | 341 | 2013-12-05 |
| 5 | [Trevor Perrin requests removal of NSA from IETF Crypto Review](https://news.ycombinator.com/item?id=6942145) | Trevor Perrin 要求将 NSA 排除在 IETF 密码学审查工作之外。 | 1056 | 140 | 2013-12-20 |
| 6 | [I worked on the US drone program. The public should know what really goes on](https://news.ycombinator.com/item?id=6979778) | 一名美国无人机项目参与者主张，公众应知道项目内部真正发生的事。 | 910 | 475 | 2013-12-29 |
| 7 | [Secret contract tied NSA and security industry pioneer](https://news.ycombinator.com/item?id=6944118) | 报道 NSA 与一家安全产业先驱企业之间的秘密合同。 | 899 | 320 | 2013-12-20 |
| 8 | [I Got Myself Arrested So I Could Look Inside the Justice System](https://news.ycombinator.com/item?id=6922405) | 作者为观察司法系统内部运作，主动让自己被捕。 | 834 | 472 | 2013-12-17 |
| 9 | [Google Acquires Boston Dynamics](https://news.ycombinator.com/item?id=6904793) | Google 收购机器人公司 Boston Dynamics。 | 799 | 291 | 2013-12-14 |
| 10 | [NSA phone surveillance program likely unconstitutional, federal judge rules](https://news.ycombinator.com/item?id=6917194) | 美国联邦法官认为，NSA 的电话监控项目很可能违反宪法。 | 748 | 231 | 2013-12-16 |
| 11 | [Bill Gates takes part in Reddit's Secret Santa](https://news.ycombinator.com/item?id=6933004) | Bill Gates 参加 Reddit 的匿名圣诞礼物交换活动。 | 745 | 226 | 2013-12-19 |
| 12 | [An Engineer’s guide to Stock Options](https://news.ycombinator.com/item?id=6882744) | 面向工程师讲解股票期权，帮助理解相关权益。 | 738 | 154 | 2013-12-10 |
| 13 | [I found Prezi's source code](https://news.ycombinator.com/item?id=6840437) | 作者讲述自己发现 Prezi 源代码的经过。 | 712 | 255 | 2013-12-03 |
| 14 | [My Roommate's a Genius](https://news.ycombinator.com/item?id=6838299) | 作者以“我的室友是个天才”为题，介绍室友的独特之处。 | 697 | 174 | 2013-12-03 |
| 15 | [Edward Snowden, after months of NSA revelations, says his mission’s accomplished](https://news.ycombinator.com/item?id=6957882) | 接连披露 NSA 监控信息数月后，Edward Snowden 表示自己的任务已经完成。 | 687 | 201 | 2013-12-24 |
| 16 | [What the Fluck](https://news.ycombinator.com/item?id=6859245) | 一篇题为《What the Fluck》的文章，标题以文字游戏表达惊讶。 | 685 | 159 | 2013-12-06 |
| 17 | [Are Your Programmers Working Hard, Or Are They Lazy?](https://news.ycombinator.com/item?id=6895502) | 如何判断程序员是在努力工作，还是表现得懒散？ | 663 | 322 | 2013-12-12 |
| 18 | [Sent $35,104.11 USD to CoinBase. Never received Bitcoins](https://news.ycombinator.com/item?id=6929705) | 用户称向 Coinbase 转入三万五千多美元后，未按承诺日期收到比特币。 | 658 | 475 | 2013-12-18 |
| 19 | [Reform Government Surveillance](https://news.ycombinator.com/item?id=6872856) | 一项呼吁改革政府监控做法的公开倡议。 | 657 | 212 | 2013-12-09 |
| 20 | [Download a copy of your Gmail and Google Calendar data](https://news.ycombinator.com/item?id=6855145) | Google 推出下载 Gmail 与 Google Calendar 数据副本的功能。 | 628 | 169 | 2013-12-05 |

## 2014-01

有效主帖 21,779 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Wozniak: “Actually, the movie was largely a lie about me”](https://news.ycombinator.com/item?id=7086411) | Steve Wozniak 表示，电影对自己的描绘大部分并不真实。 | 1591 | 301 | 2014-01-19 |
| 2 | [Light Table is now open source](https://news.ycombinator.com/item?id=7024626) | 开发工具 Light Table 宣布开源。 | 1256 | 431 | 2014-01-08 |
| 3 | [Quick tip for developers who use OS X](https://news.ycombinator.com/item?id=7051091) | 在 OS X 终端按住 Option 点击当前行，即可把光标移到点击位置。 | 1145 | 395 | 2014-01-13 |
| 4 | [How I Lost My $50,000 Twitter Username](https://news.ycombinator.com/item?id=7141532) | 作者讲述自己如何失去一个据称价值五万美元的 Twitter 用户名。 | 1043 | 386 | 2014-01-29 |
| 5 | [Edward Snowden nominated for Nobel peace prize](https://news.ycombinator.com/item?id=7143438) | Edward Snowden 获得诺贝尔和平奖提名。 | 1028 | 191 | 2014-01-29 |
| 6 | [You might not need jQuery](https://news.ycombinator.com/item?id=7152068) | 展示无需 jQuery 也能完成常见网页操作的思路。 | 994 | 349 | 2014-01-30 |
| 7 | [Gmail was down](https://news.ycombinator.com/item?id=7116764) | Gmail 出现服务中断，用户询问不同国家的访问情况。 | 971 | 457 | 2014-01-24 |
| 8 | [Network Solutions Auto-Enroll: $1,850](https://news.ycombinator.com/item?id=7098383) | 作者质疑 Network Solutions 自动加入服务所产生的一千八百五十美元费用。 | 917 | 246 | 2014-01-21 |
| 9 | [OpenBSD will shut down if we do not have the funding to keep the lights on](https://news.ycombinator.com/item?id=7069889) | OpenBSD 表示，若无法筹得维持运行的资金，项目将面临停摆。 | 825 | 407 | 2014-01-16 |
| 10 | [Confessions of an ex-TSA agent](https://news.ycombinator.com/item?id=7158786) | 一名前 TSA 安检人员讲述自己的从业经历与反思。 | 819 | 192 | 2014-01-31 |
| 11 | [Debunking Princeton](https://news.ycombinator.com/item?id=7111627) | 作者对普林斯顿方面的一项说法提出反驳。 | 812 | 145 | 2014-01-23 |
| 12 | [Edward Snowden, Whistle-Blower](https://news.ycombinator.com/item?id=6998179) | 围绕 Edward Snowden 的告密者身份，讨论他披露信息的意义。 | 804 | 157 | 2014-01-02 |
| 13 | [How Silicon Valley CEOs conspired to drive down tech engineer wages](https://news.ycombinator.com/item?id=7111531) | 报道硅谷首席执行官之间被指存在压低技术工程师工资的合谋。 | 797 | 470 | 2014-01-23 |
| 14 | [Yale censored a student's course catalog site. I made an unblockable replacement](https://news.ycombinator.com/item?id=7084555) | 耶鲁封禁学生制作的课程目录网站后，作者开发了一个声称无法封锁的替代品。 | 775 | 199 | 2014-01-19 |
| 15 | [Fired? Speak No Evil](https://news.ycombinator.com/item?id=7005374) | 围绕被解雇后的发声，讨论员工表达负面评价的处境。 | 726 | 355 | 2014-01-03 |
| 16 | [Show HN: Kimono – Never write a web scraper again](https://news.ycombinator.com/item?id=7066479) | Kimono 希望让用户无需亲自编写网页抓取程序即可提取数据。 | 717 | 230 | 2014-01-15 |
| 17 | [Toshiba says they made a mistake but they still cannot help me](https://news.ycombinator.com/item?id=7007828) | 作者称 Toshiba 承认犯错，却仍未能提供帮助。 | 700 | 192 | 2014-01-03 |
| 18 | [What Hard Drive Should I Buy?](https://news.ycombinator.com/item?id=7095357) | 选购硬盘时该如何判断，哪一种硬盘更值得买？ | 688 | 266 | 2014-01-21 |
| 19 | [Google to Acquire Nest](https://news.ycombinator.com/item?id=7053239) | Google 宣布收购 Nest。 | 684 | 568 | 2014-01-13 |
| 20 | [An Open Letter to HN from EFF, Demand Progress, and Cory Doctorow](https://news.ycombinator.com/item?id=7037532) | EFF、Demand Progress 与 Cory Doctorow 致信 HN，呼吁延续反对网络审查与监控的行动。 | 681 | 101 | 2014-01-10 |

## 2014-02

有效主帖 20,936 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Today is The Day We Fight Back](https://news.ycombinator.com/item?id=7216471) | “我们反击的日子”行动发起，邀请公众参与表达诉求。 | 2061 | 258 | 2014-02-11 |
| 2 | [Facebook Fraud [video]](https://news.ycombinator.com/item?id=7211514) | 一段题为《Facebook 欺诈》的视频，对该平台相关做法提出质疑。 | 1678 | 393 | 2014-02-10 |
| 3 | [Atom](https://news.ycombinator.com/item?id=7308071) | 文本编辑器 Atom 公开亮相。 | 1475 | 641 | 2014-02-26 |
| 4 | [How I Ended Up In Solitary After Calling 911 For Help](https://news.ycombinator.com/item?id=7233730) | 作者讲述拨打九一一求助后，反而被关入单独禁闭的经历。 | 1249 | 789 | 2014-02-13 |
| 5 | [Facebook Buying WhatsApp for $16B in Cash and Stock Plus $3B in RSUs](https://news.ycombinator.com/item?id=7266618) | Facebook 以现金、股票及限制性股票合计约一百九十亿美元收购 WhatsApp。 | 1129 | 802 | 2014-02-19 |
| 6 | [GCHQ intercepted webcam images of millions of Yahoo users worldwide](https://news.ycombinator.com/item?id=7312212) | 报道英国 GCHQ 截获全球数百万 Yahoo 用户的摄像头图像。 | 1122 | 304 | 2014-02-27 |
| 7 | [Mystery signal from a helicopter](https://news.ycombinator.com/item?id=7160242) | 追查一架直升机发出的神秘信号。 | 1101 | 78 | 2014-02-01 |
| 8 | [Hemingway makes your writing bold and clear](https://news.ycombinator.com/item?id=7223969) | Hemingway 写作工具帮助检查文案，让表达更清楚有力。 | 1040 | 327 | 2014-02-12 |
| 9 | [Satya Nadella – Microsoft's CEO](https://news.ycombinator.com/item?id=7177388) | Satya Nadella 出任微软首席执行官。 | 1023 | 564 | 2014-02-04 |
| 10 | [How I hacked Github again](https://news.ycombinator.com/item?id=7197048) | 作者复盘自己再次攻破 GitHub 的过程。 | 911 | 190 | 2014-02-07 |
| 11 | [Neovim](https://news.ycombinator.com/item?id=7278214) | 认识 Neovim 编辑器项目及其公开代码。 | 879 | 362 | 2014-02-21 |
| 12 | [US Media Blacks Out Snowden Interview](https://news.ycombinator.com/item?id=7165266) | 作者指责美国媒体未报道一段 Snowden 访谈。 | 869 | 229 | 2014-02-02 |
| 13 | [How in-app purchases have destroyed the game industry](https://news.ycombinator.com/item?id=7161901) | 作者认为，应用内购买正在破坏游戏行业。 | 829 | 524 | 2014-02-01 |
| 14 | [Project Tango](https://news.ycombinator.com/item?id=7273081) | Google 公开名为 Project Tango 的项目。 | 815 | 339 | 2014-02-20 |
| 15 | [Sam Altman for President](https://news.ycombinator.com/item?id=7278645) | Y Combinator 宣布由 Sam Altman 担任总裁。 | 790 | 153 | 2014-02-21 |
| 16 | [Girls and Software](https://news.ycombinator.com/item?id=7205868) | 围绕女孩与软件的关系，讨论女性参与技术领域的话题。 | 765 | 414 | 2014-02-09 |
| 17 | [Richard Lynch, an awesome PHP community guy and former colleague needs our help](https://news.ycombinator.com/item?id=7213378) | 作者为 PHP 社区成员、前同事 Richard Lynch 寻求帮助。 | 717 | 306 | 2014-02-10 |
| 18 | [Only 90s Web Developers Remember This](https://news.ycombinator.com/item?id=7300429) | 回顾上世纪九十年代网页开发者熟悉的技术与经历。 | 710 | 394 | 2014-02-25 |
| 19 | [GitHub's new text editor leaked on Twitter](https://news.ycombinator.com/item?id=7302941) | GitHub 新文本编辑器的消息提前出现在 Twitter 上。 | 706 | 249 | 2014-02-26 |
| 20 | [Google permanently bans popular application from Play for not using IAP](https://news.ycombinator.com/item?id=7169712) | 一款热门应用据称因未采用应用内购买而被 Google Play 永久封禁。 | 693 | 264 | 2014-02-03 |

## 2014-03

有效主帖 23,305 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [2048](https://news.ycombinator.com/item?id=7373566) | 体验数字合并游戏《2048》。 | 2903 | 410 | 2014-03-10 |
| 2 | [Facebook acquires Oculus VR](https://news.ycombinator.com/item?id=7469115) | Facebook 宣布收购虚拟现实公司 Oculus VR。 | 1449 | 837 | 2014-03-25 |
| 3 | [Elon Musk: To the People of New Jersey](https://news.ycombinator.com/item?id=7401029) | Elon Musk 向新泽西居民发表公开信。 | 1265 | 400 | 2014-03-14 |
| 4 | [Julie Ann Horvath Describes Sexism and Intimidation Behind Her GitHub Exit](https://news.ycombinator.com/item?id=7408055) | Julie Ann Horvath 讲述其离开 GitHub 背后的性别歧视与恐吓指控。 | 1188 | 1057 | 2014-03-16 |
| 5 | [The Face Behind Bitcoin?](https://news.ycombinator.com/item?id=7353283) | 报道试图寻找比特币背后的人，其身份判断仍以疑问呈现。 | 1165 | 678 | 2014-03-06 |
| 6 | [2048 AI](https://news.ycombinator.com/item?id=7379821) | 展示用于游玩《2048》的人工智能程序。 | 1040 | 189 | 2014-03-11 |
| 7 | [Gravity waves from Big Bang detected](https://news.ycombinator.com/item?id=7415660) | 报道声称观测到来自宇宙大爆炸的引力波信号。 | 892 | 171 | 2014-03-17 |
| 8 | [Minecraft creator says he’s canceled talks for Oculus Rift version](https://news.ycombinator.com/item?id=7469829) | 《Minecraft》创作者表示，已取消与 Oculus Rift 版本有关的洽谈。 | 887 | 351 | 2014-03-25 |
| 9 | [The Indian sanitary pad revolutionary](https://news.ycombinator.com/item?id=7339092) | 走近一位推动卫生巾革新的印度人。 | 835 | 261 | 2014-03-04 |
| 10 | [What Dreams May Come](https://news.ycombinator.com/item?id=7390638) | 一篇题为《美梦成真》的作品，围绕梦想这一主题展开。 | 789 | 382 | 2014-03-13 |
| 11 | [Dark spot under cockpit of A-10s](https://news.ycombinator.com/item?id=7354214) | A-10 攻击机座舱下方的黑色区域是什么，又有什么用途？ | 772 | 185 | 2014-03-06 |
| 12 | [Microsoft makes source code for MS-DOS and Word for Windows available to public](https://news.ycombinator.com/item?id=7466952) | 微软向公众开放 MS-DOS 与 Windows 版 Word 的源代码。 | 756 | 204 | 2014-03-25 |
| 13 | [Update on Julie Horvath's Departure](https://news.ycombinator.com/item?id=7412612) | GitHub 就 Julie Horvath 离职一事公布最新说明。 | 701 | 452 | 2014-03-17 |
| 14 | [ASCII Delimited Text – Not CSV or TAB delimited text](https://news.ycombinator.com/item?id=7474600) | 介绍使用 ASCII 分隔符组织文本数据的方案，并与 CSV、制表符格式比较。 | 695 | 280 | 2014-03-26 |
| 15 | [Worse](https://news.ycombinator.com/item?id=7405573) | 作者以“更糟”为题，对所关注的问题发表批评。 | 674 | 280 | 2014-03-15 |
| 16 | [Moto 360](https://news.ycombinator.com/item?id=7422988) | Motorola 展示 Moto 360 产品。 | 669 | 414 | 2014-03-18 |
| 17 | [Coming Soon to Hacker News: Pending Comments](https://news.ycombinator.com/item?id=7445761) | HN 宣布计划推出待审核评论功能，以改善社区评论质量。 | 661 | 805 | 2014-03-21 |
| 18 | [Larry Page: I’d Rather Leave My Billions to Elon Musk Than to Charity](https://news.ycombinator.com/item?id=7437940) | Larry Page 表示，比起慈善机构，他更愿把巨额财富留给 Elon Musk。 | 640 | 430 | 2014-03-20 |
| 19 | [Tesla Adds Titanium Underbody Shield and Aluminum Deflector Plates to Model S](https://news.ycombinator.com/item?id=7486561) | Tesla 为 Model S 加装钛制底部护板与铝制导流板。 | 631 | 399 | 2014-03-28 |
| 20 | [Popcorn Time Is So Good at Movie Piracy, It’s Scary](https://news.ycombinator.com/item?id=7377089) | 报道 Popcorn Time 的电影盗版体验，并对其便利程度表达担忧。 | 624 | 410 | 2014-03-11 |

## 2014-04

有效主帖 21,836 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Drop Dropbox](https://news.ycombinator.com/item?id=7566069) | 一项呼吁用户放弃 Dropbox 的公开倡议。 | 1990 | 1008 | 2014-04-10 |
| 2 | [The Heartbleed Bug](https://news.ycombinator.com/item?id=7548991) | 介绍名为 Heartbleed 的安全漏洞及其相关信息。 | 1768 | 528 | 2014-04-07 |
| 3 | [Microsoft Open Sources C# Compiler](https://news.ycombinator.com/item?id=7524082) | 微软宣布开源 C# 编译器。 | 1374 | 446 | 2014-04-03 |
| 4 | [How we got read access on Google’s production servers](https://news.ycombinator.com/item?id=7571942) | 研究者通过存在 XXE 漏洞的 XML 解析器，获得 Google 生产服务器文件的读取权限。 | 1156 | 192 | 2014-04-11 |
| 5 | [Project Naptha: a browser extension that enables text selection on any image](https://news.ycombinator.com/item?id=7629396) | Project Naptha 浏览器扩展让用户能够选取图片中的文字。 | 1055 | 134 | 2014-04-22 |
| 6 | [Write Code Every Day](https://news.ycombinator.com/item?id=7568675) | 作者分享每天坚持编写代码的做法。 | 1025 | 216 | 2014-04-10 |
| 7 | [“Game Programming Patterns” is now finished](https://news.ycombinator.com/item?id=7634734) | 《游戏编程模式》宣告完成。 | 988 | 74 | 2014-04-23 |
| 8 | [Brendan Eich Steps Down as Mozilla CEO](https://news.ycombinator.com/item?id=7525198) | Brendan Eich 辞去 Mozilla 首席执行官职务。 | 982 | 1171 | 2014-04-03 |
| 9 | [The Absurdity of LinkedIn](https://news.ycombinator.com/item?id=7673643) | 作者质疑 LinkedIn 的某些做法，指出其中的荒谬之处。 | 803 | 336 | 2014-04-30 |
| 10 | [What I Would Do If I Ran Tarsnap](https://news.ycombinator.com/item?id=7523953) | 作者设想，若由自己运营 Tarsnap，会如何调整这项服务。 | 801 | 311 | 2014-04-03 |
| 11 | [Results of the GitHub Investigation](https://news.ycombinator.com/item?id=7623281) | GitHub 公布内部调查结果。 | 739 | 479 | 2014-04-21 |
| 12 | [SF’s Housing Crisis Explained](https://news.ycombinator.com/item?id=7590250) | 解释旧金山住房危机及其相关问题。 | 683 | 465 | 2014-04-15 |
| 13 | [Lens Blur in the new Google Camera app](https://news.ycombinator.com/item?id=7599397) | 介绍新版 Google Camera 应用中的镜头模糊功能。 | 644 | 239 | 2014-04-16 |
| 14 | [Learn C and build your own Lisp](https://news.ycombinator.com/item?id=7530427) | 通过亲手实现一个 Lisp，学习 C 语言。 | 641 | 145 | 2014-04-04 |
| 15 | [The Birth and Death of JavaScript [video]](https://news.ycombinator.com/item?id=7605687) | 一场以《JavaScript 的诞生与消亡》为题的演讲。 | 635 | 227 | 2014-04-17 |
| 16 | [The New Deal](https://news.ycombinator.com/item?id=7629630) | Y Combinator 以《新协议》为题发布新的安排。 | 625 | 178 | 2014-04-22 |
| 17 | [Amazon Dash](https://news.ycombinator.com/item?id=7534468) | Amazon 推出名为 Dash 的产品。 | 621 | 250 | 2014-04-04 |
| 18 | [Follow up to the investigation results](https://news.ycombinator.com/item?id=7662190) | GitHub 对此前公布的调查结果作出后续说明。 | 620 | 330 | 2014-04-28 |
| 19 | [Firefox 29](https://news.ycombinator.com/item?id=7666688) | Firefox 浏览器发布第二十九版。 | 603 | 503 | 2014-04-29 |
| 20 | [The New Linode Cloud: SSDs, Double RAM and much more](https://news.ycombinator.com/item?id=7603570) | Linode 更新云服务，采用 SSD、翻倍内存并推出更多调整。 | 584 | 275 | 2014-04-17 |

## 2014-05

有效主帖 20,612 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Don't mess with Newegg](https://news.ycombinator.com/item?id=7787384) | Newegg 以“别惹我们”为题，表达强硬的立场。 | 1469 | 190 | 2014-05-23 |
| 2 | [2048, success and me](https://news.ycombinator.com/item?id=7704800) | 《2048》作者回顾游戏的成功，以及这份成功与自己的关系。 | 925 | 222 | 2014-05-06 |
| 3 | [Atom Is Now Open Source](https://news.ycombinator.com/item?id=7704859) | 文本编辑器 Atom 宣布开源。 | 914 | 296 | 2014-05-06 |
| 4 | [Why I was forced to shut down Lavabit](https://news.ycombinator.com/item?id=7774158) | Lavabit 创办者解释，自己为何被迫关闭这项服务。 | 806 | 226 | 2014-05-20 |
| 5 | [The future of Unreal Tournament begins today](https://news.ycombinator.com/item?id=7716963) | 《Unreal Tournament》公布面向未来的新计划。 | 803 | 141 | 2014-05-08 |
| 6 | [TrueCrypt suggesting migration to BitLocker?](https://news.ycombinator.com/item?id=7812133) | TrueCrypt 是否正在建议用户迁移到 BitLocker，相关变化引发疑问。 | 797 | 382 | 2014-05-28 |
| 7 | [The purpose of DRM is not to prevent copyright violations (2013)](https://news.ycombinator.com/item?id=7751110) | 作者提出，数字版权管理的目的并非阻止侵犯版权。 | 782 | 234 | 2014-05-15 |
| 8 | [Level3 is without peer, now what to do?](https://news.ycombinator.com/item?id=7773036) | 围绕网络运营商 Level 3 的互联处境，探讨下一步应如何应对。 | 781 | 382 | 2014-05-20 |
| 9 | [The next version of DuckDuckGo](https://news.ycombinator.com/item?id=7700192) | DuckDuckGo 展示下一版本搜索服务。 | 738 | 322 | 2014-05-05 |
| 10 | [FCC approves plan to consider paid priority on Internet](https://news.ycombinator.com/item?id=7750036) | 美国 FCC 批准将互联网付费优先传输纳入考虑的计划。 | 679 | 331 | 2014-05-15 |
| 11 | [Fraudulent trading activity at Mt. Gox](https://news.ycombinator.com/item?id=7796748) | 一份报告指控 Mt. Gox 存在欺诈性交易活动。 | 648 | 131 | 2014-05-25 |
| 12 | [Using the wrong dictionary](https://news.ycombinator.com/item?id=7772557) | 作者反思自己使用的词典，探讨选错词典可能带来的影响。 | 635 | 138 | 2014-05-20 |
| 13 | [Removing User Interface Complexity, or Why React is Awesome](https://news.ycombinator.com/item?id=7738194) | 作者说明 React 如何减少用户界面开发的复杂性。 | 632 | 219 | 2014-05-13 |
| 14 | [Syncthing: Open Source Dropbox and BitTorrent Sync Replacement](https://news.ycombinator.com/item?id=7734114) | Syncthing 提供开源文件同步方案，定位为 Dropbox 与 BitTorrent Sync 的替代品。 | 623 | 184 | 2014-05-12 |
| 15 | [New DuckDuckGo design](https://news.ycombinator.com/item?id=7772525) | DuckDuckGo 公布全新的页面设计。 | 614 | 214 | 2014-05-20 |
| 16 | [Sistine Chapel](https://news.ycombinator.com/item?id=7823385) | 浏览与西斯廷礼拜堂有关的在线展示。 | 608 | 235 | 2014-05-30 |
| 17 | [All of Bach](https://news.ycombinator.com/item?id=7720708) | 认识以巴赫全部作品为主题的 All of Bach 项目。 | 607 | 148 | 2014-05-09 |
| 18 | [Rappers, Sorted by Size of Vocabulary](https://news.ycombinator.com/item?id=7694436) | 按词汇量给说唱歌手排序，比较他们歌词中的用词范围。 | 600 | 267 | 2014-05-04 |
| 19 | [OS X Command Line Utilities](https://news.ycombinator.com/item?id=7747982) | 介绍 OS X 中实用的命令行工具。 | 567 | 235 | 2014-05-15 |
| 20 | [The Day I Started Lying to Ruth](https://news.ycombinator.com/item?id=7708437) | 作者讲述自己开始对 Ruth 说谎的那一天。 | 566 | 141 | 2014-05-07 |

## 2014-06

有效主帖 19,249 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [All Our Patent Are Belong To You](https://news.ycombinator.com/item?id=7884560) | Tesla 以“我们的专利都属于你”为题，公布专利开放立场。 | 1999 | 314 | 2014-06-12 |
| 2 | [Visualizing Algorithms](https://news.ycombinator.com/item?id=7949995) | 通过可视化方式观察算法，理解其运行过程。 | 1557 | 88 | 2014-06-26 |
| 3 | [Introducing Swift](https://news.ycombinator.com/item?id=7835099) | Apple 正式介绍编程语言 Swift。 | 1216 | 926 | 2014-06-02 |
| 4 | [My startup failed, and this is what it feels like](https://news.ycombinator.com/item?id=7933155) | 一位创业者讲述公司失败后自己的真实感受。 | 1084 | 252 | 2014-06-23 |
| 5 | [Supreme court: Warrantless cell phone searches illegal [pdf]](https://news.ycombinator.com/item?id=7944024) | 美国最高法院裁定，无搜查令检查手机的做法违法。 | 854 | 145 | 2014-06-25 |
| 6 | [Vermeer's paintings might be 350 year-old color photographs](https://news.ycombinator.com/item?id=7872661) | 文章提出一种猜想：Vermeer 的画作或许可被视为三百五十年前的彩色照片。 | 749 | 154 | 2014-06-10 |
| 7 | [Google Cardboard](https://news.ycombinator.com/item?id=7945968) | Google 公布 Cardboard 项目。 | 712 | 127 | 2014-06-25 |
| 8 | [Docker 1.0](https://news.ycombinator.com/item?id=7868791) | 容器工具 Docker 发布 1.0 版本。 | 709 | 130 | 2014-06-09 |
| 9 | [A SWAT team blew a hole in my 2-year-old son](https://news.ycombinator.com/item?id=7938748) | 一位家长称，特警行动中的爆炸物严重伤害了自己两岁的孩子。 | 706 | 447 | 2014-06-24 |
| 10 | [Show HN: Wavepot – Digital audio workstation of the web](https://news.ycombinator.com/item?id=7905910) | Wavepot 将数字音频工作站带到网页中。 | 625 | 132 | 2014-06-17 |
| 11 | [Amazon Fire Phone](https://news.ycombinator.com/item?id=7911934) | Amazon 发布 Fire Phone 手机。 | 598 | 403 | 2014-06-18 |
| 12 | [With 'The Machine,' HP May Have Invented a New Kind of Computer](https://news.ycombinator.com/item?id=7878949) | 报道探讨 HP 的“The Machine”是否代表一种新的计算机形态。 | 595 | 292 | 2014-06-11 |
| 13 | [Alexander Shulgin has died](https://news.ycombinator.com/item?id=7839226) | Alexander Shulgin 去世的消息。 | 590 | 135 | 2014-06-03 |
| 14 | [Who am I: A mind reader (don't forget to view source)](https://news.ycombinator.com/item?id=7855168) | 体验名为《我是谁》的读心网页，并通过查看源码探索其实现。 | 583 | 168 | 2014-06-05 |
| 15 | [Kingston and PNY using cheaper components after good reviews](https://news.ycombinator.com/item?id=7893068) | Kingston 与 PNY 被指在产品获得好评后，改用更便宜的零部件。 | 581 | 158 | 2014-06-14 |
| 16 | [For Sale: 29,656.51306529 Bitcoins](https://news.ycombinator.com/item?id=7886014) | 一批总量约二万九千六百五十六枚的比特币公开待售。 | 580 | 404 | 2014-06-12 |
| 17 | [I Sold My Startup for $25.5 Million](https://news.ycombinator.com/item?id=7858317) | 作者讲述以两千五百五十万美元出售自己创业公司的经历。 | 578 | 236 | 2014-06-06 |
| 18 | [How can an introvert Asian engineer like me make friends?](https://news.ycombinator.com/item?id=7898035) | 一位性格内向的亚裔工程师追问，自己该如何结交朋友。 | 556 | 435 | 2014-06-16 |
| 19 | [Web Starter Kit](https://news.ycombinator.com/item?id=7917361) | Google 提供网页开发入门工具包 Web Starter Kit。 | 553 | 210 | 2014-06-19 |
| 20 | [A first-person engine in 265 lines of JS](https://news.ycombinator.com/item?id=7842037) | 用二百六十五行 JavaScript 实现一个第一人称引擎。 | 528 | 97 | 2014-06-03 |

## 2014-07

有效主帖 20,390 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Thanks, HN: You helped discover a disease and save lives](https://news.ycombinator.com/item?id=8050106) | 一位父亲感谢 HN 传播儿子的罕见病故事，帮助找到更多患者并推进治疗探索。 | 1483 | 109 | 2014-07-17 |
| 2 | [Show HN: Show HN](https://news.ycombinator.com/item?id=7984826) | HN 推出专门汇集用户作品展示的 Show HN 页面。 | 1302 | 166 | 2014-07-03 |
| 3 | [Count to ten when a plane goes down](https://news.ycombinator.com/item?id=8066545) | 作者以“飞机坠落时先数到十”为题，提醒人们面对空难消息时保持克制。 | 1112 | 273 | 2014-07-21 |
| 4 | [Show HN: Markov chains explained visually](https://news.ycombinator.com/item?id=8103240) | 用可视化方式解释马尔可夫链如何运作。 | 1070 | 92 | 2014-07-29 |
| 5 | [Show HN: OneBody Church Directory software I've been hacking on for 7 years](https://news.ycombinator.com/item?id=8085213) | 作者展示自己持续开发七年的教会通讯录软件 OneBody。 | 1020 | 304 | 2014-07-25 |
| 6 | [Stellar](https://news.ycombinator.com/item?id=8114901) | 介绍名为 Stellar 的项目及其公开发布。 | 943 | 454 | 2014-07-31 |
| 7 | [Game about squares](https://news.ycombinator.com/item?id=8092566) | 体验一款围绕方块展开的游戏。 | 910 | 194 | 2014-07-27 |
| 8 | [Ask HN: Urgent connection to Twitter support](https://news.ycombinator.com/item?id=8006869) | 紧急预警账号即将触及 API 限额，管理员寻求 Twitter 支持人员协助。 | 875 | 127 | 2014-07-08 |
| 9 | [Calling All Hackers: Help Us Build an Open Wireless Router](https://news.ycombinator.com/item?id=8060784) | 电子前哨基金会邀请开发者共同打造开放无线网络路由器。 | 850 | 138 | 2014-07-20 |
| 10 | [Y Combinator has filed an official comment with the FCC](https://news.ycombinator.com/item?id=8033322) | Y Combinator 宣布已向美国 FCC 提交正式意见。 | 841 | 120 | 2014-07-14 |
| 11 | [Bitcoin: the Stripe perspective](https://news.ycombinator.com/item?id=8064786) | Stripe 分享自己对比特币的看法。 | 813 | 244 | 2014-07-21 |
| 12 | [Bootstra.386 – A Bootstrap theme from the 1980s](https://news.ycombinator.com/item?id=7983008) | Bootstra.386 把上世纪八十年代的视觉风格带进 Bootstrap 主题。 | 803 | 109 | 2014-07-03 |
| 13 | [Show HN: Pangoly – Build your shiny new PC](https://news.ycombinator.com/item?id=8036648) | Pangoly 帮助用户规划并组装一台新电脑。 | 778 | 213 | 2014-07-15 |
| 14 | [Verizon's accidental mea culpa](https://news.ycombinator.com/item?id=8048997) | 作者认为 Verizon 的一次表态意外承认了自身的问题。 | 776 | 307 | 2014-07-17 |
| 15 | [Python is now the most popular introductory language at top U.S. universities](https://news.ycombinator.com/item?id=8001337) | 报道 Python 已成为美国顶尖大学最常用的编程入门教学语言。 | 743 | 359 | 2014-07-07 |
| 16 | [Choose hotels by the quality of their WiFi](https://news.ycombinator.com/item?id=8081401) | 根据无线网络质量挑选酒店，让住宿选择考虑上网体验。 | 671 | 237 | 2014-07-24 |
| 17 | [The Lowdown on Lidar](https://news.ycombinator.com/item?id=8114336) | 介绍激光雷达技术，了解它的相关原理与用途。 | 667 | 271 | 2014-07-31 |
| 18 | [Ask HN: 16-hour work week jobs?](https://news.ycombinator.com/item?id=7994673) | 体验过每周工作十六小时后，发帖者寻求类似岗位并分享自己的感受。 | 662 | 261 | 2014-07-06 |
| 19 | [Mistakes You Should Never Make](https://news.ycombinator.com/item?id=8080442) | 作者回顾一些不应重蹈覆辙的错误。 | 646 | 328 | 2014-07-24 |
| 20 | [Show HN: NomadList – The best cities to live and work remotely in](https://news.ycombinator.com/item?id=8107222) | NomadList 帮助远程工作者比较适合生活和工作的城市。 | 639 | 298 | 2014-07-30 |

## 2014-08

有效主帖 19,069 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [First-Person Hyper-lapse Videos](https://news.ycombinator.com/item?id=8160571) | 展示第一人称视角的超延时摄影视频技术。 | 1470 | 172 | 2014-08-10 |
| 2 | [Uber's playbook for sabotaging Lyft](https://news.ycombinator.com/item?id=8229081) | 报道 Uber 被指用于破坏竞争对手 Lyft 业务的一套做法。 | 1224 | 391 | 2014-08-26 |
| 3 | [Show HN: I got hacked, felt paranoid, made an app – GlassWire](https://news.ycombinator.com/item?id=8222652) | 遭到入侵后，作者因安全焦虑而制作了应用 GlassWire。 | 1013 | 331 | 2014-08-25 |
| 4 | [Fully Functional 1KB Hard Drive in Vanilla Minecraft](https://news.ycombinator.com/item?id=8201362) | 在原版《Minecraft》中搭建一块可正常工作的、一 KB 容量的硬盘。 | 831 | 109 | 2014-08-20 |
| 5 | [fork() can fail](https://news.ycombinator.com/item?id=8204007) | 提醒开发者，创建子进程的 fork 调用也可能失败。 | 760 | 313 | 2014-08-20 |
| 6 | [Feynman Lectures on Physics now free online](https://news.ycombinator.com/item?id=8216546) | 《费曼物理学讲义》现可免费在线阅读。 | 749 | 93 | 2014-08-23 |
| 7 | [Edward Snowden: The Untold Story](https://news.ycombinator.com/item?id=8172365) | 围绕 Edward Snowden，讲述鲜为人知的经历。 | 717 | 223 | 2014-08-13 |
| 8 | [X to close](https://news.ycombinator.com/item?id=8171340) | 从“点击 X 关闭”这一动作出发，关注相关设计问题。 | 704 | 195 | 2014-08-13 |
| 9 | [MathBox 2](https://news.ycombinator.com/item?id=8179837) | 展示 MathBox 的第二版及其相关演示。 | 657 | 88 | 2014-08-14 |
| 10 | [Some Dark Patterns Now Illegal in UK](https://news.ycombinator.com/item?id=8226974) | 英国将部分诱导用户作出不利选择的界面设计列为违法。 | 653 | 260 | 2014-08-26 |
| 11 | [A Single Div](https://news.ycombinator.com/item?id=8229072) | 展示围绕单个 div 元素实现的网页设计作品。 | 649 | 140 | 2014-08-26 |
| 12 | [Hextris](https://news.ycombinator.com/item?id=8189652) | 体验名为 Hextris 的游戏项目。 | 589 | 92 | 2014-08-17 |
| 13 | [Show HN: Put “GIF” in front of any YouTube URL and hit enter](https://news.ycombinator.com/item?id=8187791) | 在 YouTube 网址前加上“GIF”，即可使用相关视频转换服务。 | 577 | 181 | 2014-08-16 |
| 14 | [Polaroid Cube](https://news.ycombinator.com/item?id=8164788) | Polaroid 展示 Cube 产品。 | 575 | 181 | 2014-08-11 |
| 15 | [Extracting audio from visual information](https://news.ycombinator.com/item?id=8131785) | 从视觉信息中提取音频，探索图像与声音之间的联系。 | 573 | 127 | 2014-08-04 |
| 16 | [They're Made out of Meat](https://news.ycombinator.com/item?id=8152131) | 阅读科幻作品《他们是肉做的》。 | 558 | 170 | 2014-08-08 |
| 17 | [Using Google Earth to Find an ISIS Training Camp](https://news.ycombinator.com/item?id=8213252) | 利用 Google Earth 查找一处 ISIS 训练营，展示地理定位调查思路。 | 547 | 106 | 2014-08-22 |
| 18 | [The Road Ahead](https://news.ycombinator.com/item?id=8247911) | 作者以《前方的路》为题，介绍未来的方向与打算。 | 537 | 60 | 2014-08-30 |
| 19 | [How we turn $199 Chromebooks into Ubuntu-based code learning machines for kids](https://news.ycombinator.com/item?id=8143844) | 把一百九十九美元的 Chromebook 改造成基于 Ubuntu 的儿童编程学习机器。 | 492 | 215 | 2014-08-06 |
| 20 | [Gooey: Turn command line programs into GUI applications](https://news.ycombinator.com/item?id=8218785) | Gooey 帮助把命令行程序转换为带图形界面的应用。 | 486 | 74 | 2014-08-24 |

## 2014-09

有效主帖 20,307 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [I'm Leaving Mojang](https://news.ycombinator.com/item?id=8318702) | 作者宣布离开 Mojang，并说明自己的决定。 | 1252 | 418 | 2014-09-15 |
| 2 | [Standard Markdown](https://news.ycombinator.com/item?id=8264733) | 介绍旨在规范 Markdown 的 Standard Markdown 项目。 | 1167 | 366 | 2014-09-03 |
| 3 | [ISRO Mars Orbiter Mission: Spacecraft successfully enters Martian Orbit](https://news.ycombinator.com/item?id=8359620) | 印度火星轨道任务宣布，航天器成功进入火星轨道。 | 1015 | 154 | 2014-09-24 |
| 4 | [TXT Record XSS](https://news.ycombinator.com/item?id=8336025) | 展示与 DNS TXT 记录有关的跨站脚本攻击问题。 | 998 | 228 | 2014-09-18 |
| 5 | [I was asked to crack a program in a job interview](https://news.ycombinator.com/item?id=8331381) | 作者讲述求职面试中被要求破解一个程序的经历。 | 997 | 302 | 2014-09-17 |
| 6 | [Reddit](https://news.ycombinator.com/item?id=8389731) | 一篇以 Reddit 为题的文章，介绍作者对该平台的看法。 | 988 | 394 | 2014-09-30 |
| 7 | [Yes, we’re being bought by Microsoft](https://news.ycombinator.com/item?id=8318506) | Mojang 确认公司将被微软收购。 | 941 | 515 | 2014-09-15 |
| 8 | [CVE-2014-6271: Remote code execution through bash](https://news.ycombinator.com/item?id=8361574) | 披露 Bash 的 CVE-2014-6271 漏洞，可导致远程代码执行。 | 905 | 416 | 2014-09-24 |
| 9 | [My experience with using cp to copy 432 million files (39 TB)](https://news.ycombinator.com/item?id=8305283) | 作者分享使用 cp 复制四亿三千二百万个文件、共三十九 TB 数据的经历。 | 826 | 263 | 2014-09-11 |
| 10 | [Bézier Clock](https://news.ycombinator.com/item?id=8295379) | 用贝塞尔曲线呈现时间的创意时钟。 | 810 | 69 | 2014-09-10 |
| 11 | [Feds Threatened to Fine Yahoo $250K Daily for Not Complying with NSA's PRISM](https://news.ycombinator.com/item?id=8305925) | 报道美国政府曾威胁每天罚 Yahoo 二十五万美元，要求其配合 NSA 的 PRISM 项目。 | 784 | 237 | 2014-09-12 |
| 12 | [New Requests for Startups](https://news.ycombinator.com/item?id=8308666) | Y Combinator 更新希望创业者探索的项目方向。 | 716 | 391 | 2014-09-12 |
| 13 | [Universal SSL](https://news.ycombinator.com/item?id=8382335) | Cloudflare 宣布 Universal SSL 服务。 | 712 | 240 | 2014-09-29 |
| 14 | [Mining Bitcoin with pencil and paper: 0.67 hashes per day](https://news.ycombinator.com/item?id=8380110) | 用铅笔和纸手算比特币挖矿，每天约完成零点六七次哈希。 | 653 | 103 | 2014-09-28 |
| 15 | [The Sound So Loud That It Circled the Earth Four Times](https://news.ycombinator.com/item?id=8383158) | 讲述一声巨响如何传播到绕地球四圈。 | 639 | 107 | 2014-09-29 |
| 16 | [Why Amazon Has No Profits and Why It Works](https://news.ycombinator.com/item?id=8274677) | 作者解释 Amazon 为何没有利润，以及他为何认为这种模式仍能奏效。 | 633 | 260 | 2014-09-05 |
| 17 | [A Watch Guy's Thoughts on the Apple Watch After Seeing It in the Metal](https://news.ycombinator.com/item?id=8299335) | 一位腕表爱好者亲眼见到 Apple Watch 后，分享自己的看法。 | 610 | 464 | 2014-09-10 |
| 18 | [I Had a Stroke at 33](https://news.ycombinator.com/item?id=8347380) | 作者讲述自己三十三岁时发生中风的经历。 | 603 | 151 | 2014-09-21 |
| 19 | [U.S. Law Enforcement Seeks to Halt Apple-Google Encryption of Mobile Data](https://news.ycombinator.com/item?id=8389365) | 美国执法部门寻求阻止 Apple 与 Google 对移动设备数据实施加密的措施。 | 601 | 333 | 2014-09-30 |
| 20 | [Minix 3.3.0](https://news.ycombinator.com/item?id=8324578) | Minix 操作系统发布 3.3.0 版本。 | 600 | 172 | 2014-09-16 |

## 2014-10

有效主帖 21,441 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tim Cook Speaks Up](https://news.ycombinator.com/item?id=8532261) | Tim Cook 公开发声，分享自己的个人立场。 | 3086 | 974 | 2014-10-30 |
| 2 | [Hacker News API](https://news.ycombinator.com/item?id=8422599) | Hacker News 公布 API，方便程序获取社区数据。 | 1714 | 298 | 2014-10-07 |
| 3 | [Google Inbox](https://news.ycombinator.com/item?id=8493619) | Google 推出名为 Inbox 的邮件产品。 | 1069 | 451 | 2014-10-22 |
| 4 | [Cursors](https://news.ycombinator.com/item?id=8477124) | 体验以鼠标光标为主题的 Cursors 网页项目。 | 1032 | 236 | 2014-10-19 |
| 5 | [The Horror of a 'Secure Golden Key'](https://news.ycombinator.com/item?id=8428632) | 作者解释，所谓“安全的万能密钥”为何会带来严重问题。 | 1025 | 230 | 2014-10-08 |
| 6 | [GitHub Student Developer Pack](https://news.ycombinator.com/item?id=8422087) | GitHub 为学生推出开发者资源礼包。 | 1022 | 207 | 2014-10-07 |
| 7 | [Nexus 6](https://news.ycombinator.com/item?id=8459205) | Google 公布 Nexus 6 手机。 | 1005 | 684 | 2014-10-15 |
| 8 | [Firebase is Joining Google](https://news.ycombinator.com/item?id=8488500) | Firebase 宣布加入 Google。 | 879 | 227 | 2014-10-21 |
| 9 | [Microsoft Band](https://news.ycombinator.com/item?id=8530819) | 微软推出 Microsoft Band 产品。 | 858 | 514 | 2014-10-30 |
| 10 | [Alan Eustace Jumps from Stratosphere, Breaking Felix Baumgartner’s World Record](https://news.ycombinator.com/item?id=8504931) | Alan Eustace 从平流层跳伞，打破 Felix Baumgartner 保持的世界纪录。 | 816 | 236 | 2014-10-24 |
| 11 | [I’m Terrified of My New TV](https://news.ycombinator.com/item?id=8537039) | 作者讲述自己为何害怕刚买的新电视。 | 739 | 336 | 2014-10-31 |
| 12 | [Trouble at the Koolaid Point](https://news.ycombinator.com/item?id=8425501) | 作者以“Koolaid 临界点的麻烦”为题，探讨越过某个转折点后的困境。 | 723 | 266 | 2014-10-08 |
| 13 | [Yahoo Hacked](https://news.ycombinator.com/item?id=8416393) | 有关 Yahoo 遭到入侵的技术记录。 | 722 | 236 | 2014-10-06 |
| 14 | [Live Coding in VR with Oculus Rift, Firefox WebVR, JavaScript, Three.js [video]](https://news.ycombinator.com/item?id=8411638) | 用 Oculus Rift、Firefox WebVR、JavaScript 与 Three.js 在虚拟现实中现场编程。 | 719 | 126 | 2014-10-05 |
| 15 | [Rolling Shutters](https://news.ycombinator.com/item?id=8446932) | 介绍滚动快门及其相关现象。 | 708 | 41 | 2014-10-12 |
| 16 | [Before the Startup](https://news.ycombinator.com/item?id=8399209) | Paul Graham 讨论在真正创业之前，应该考虑和准备什么。 | 703 | 163 | 2014-10-02 |
| 17 | [Spidermonkey has passed V8 on Octane performance](https://news.ycombinator.com/item?id=8518903) | SpiderMonkey 在 Octane 性能测试中的成绩超过 V8。 | 651 | 333 | 2014-10-28 |
| 18 | [#define CTO](https://news.ycombinator.com/item?id=8516777) | 围绕首席技术官的职责，尝试给 CTO 这个角色下定义。 | 650 | 107 | 2014-10-27 |
| 19 | [Plastc Card](https://news.ycombinator.com/item?id=8422928) | 介绍 Plastc Card 产品及其公开设计。 | 648 | 346 | 2014-10-07 |
| 20 | [Tilde.Club: I had a couple drinks and woke up with 1,000 nerds](https://news.ycombinator.com/item?id=8432703) | 作者讲述 Tilde.Club 如何从一次酒后念头发展成聚集上千技术爱好者的社区。 | 635 | 177 | 2014-10-09 |

## 2014-11

有效主帖 19,465 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Microsoft takes .NET open source and cross-platform](https://news.ycombinator.com/item?id=8595905) | 微软宣布推动 .NET 开源并支持跨平台。 | 2376 | 894 | 2014-11-12 |
| 2 | [Launching in 2015: A Certificate Authority to Encrypt the Entire Web](https://news.ycombinator.com/item?id=8624160) | 一项计划于二〇一五年推出的证书颁发服务，目标是促进整个网络加密。 | 2019 | 461 | 2014-11-18 |
| 3 | [Letter to Amazon Board from Fired Ad Exec](https://news.ycombinator.com/item?id=8600716) | 一名遭解雇的广告业务高管写信给 Amazon 董事会。 | 1257 | 558 | 2014-11-13 |
| 4 | [WhatsApp Co-Founder Donates $1M to FreeBSD Foundation](https://news.ycombinator.com/item?id=8620716) | WhatsApp 联合创始人向 FreeBSD 基金会捐赠一百万美元。 | 1230 | 204 | 2014-11-17 |
| 5 | [President Obama Calls for a Free and Open Internet](https://news.ycombinator.com/item?id=8583722) | Obama 总统呼吁维护自由、开放的互联网。 | 1219 | 433 | 2014-11-10 |
| 6 | [Philae has landed](https://news.ycombinator.com/item?id=8596173) | Philae 探测器成功着陆彗星，相关任务进展接受实时报道。 | 1165 | 299 | 2014-11-12 |
| 7 | [Gates Foundation to require immediate free access for journal articles](https://news.ycombinator.com/item?id=8654831) | 盖茨基金会要求相关期刊论文发表后立即向公众免费开放。 | 1079 | 147 | 2014-11-24 |
| 8 | [Firefox Developer Edition](https://news.ycombinator.com/item?id=8583257) | Firefox 推出面向开发者的浏览器版本。 | 979 | 295 | 2014-11-10 |
| 9 | [Tom Magliozzi, Co-Host of NPR's 'Car Talk,' Dies at 77](https://news.ycombinator.com/item?id=8552936) | NPR《Car Talk》联合主持人 Tom Magliozzi 去世，享年七十七岁。 | 963 | 109 | 2014-11-03 |
| 10 | [Amazon Echo](https://news.ycombinator.com/item?id=8567990) | Amazon 公布 Echo 产品。 | 924 | 716 | 2014-11-06 |
| 11 | [Unicode Text Converter](https://news.ycombinator.com/item?id=8629145) | 使用在线工具转换 Unicode 文本的呈现形式。 | 908 | 229 | 2014-11-19 |
| 12 | [God's Lonely Programmer](https://news.ycombinator.com/item?id=8658283) | 一篇以“上帝孤独的程序员”为题的人物报道。 | 883 | 320 | 2014-11-25 |
| 13 | [Doing Business in Japan](https://news.ycombinator.com/item?id=8573992) | 分享在日本开展商业活动的经验与观察。 | 818 | 305 | 2014-11-07 |
| 14 | [Facebook Launches Flow, Static Type Checker for JavaScript](https://news.ycombinator.com/item?id=8625222) | Facebook 发布用于 JavaScript 的静态类型检查器 Flow。 | 818 | 276 | 2014-11-18 |
| 15 | [The Sixth Stage of Grief Is Retro-Computing](https://news.ycombinator.com/item?id=8565459) | 作者把复古计算机体验比作悲伤的第六个阶段。 | 799 | 90 | 2014-11-06 |
| 16 | [Node.js in Flame Graphs](https://news.ycombinator.com/item?id=8631022) | 通过火焰图观察 Node.js 程序的执行与性能表现。 | 778 | 240 | 2014-11-19 |
| 17 | [Reverse OCR](https://news.ycombinator.com/item?id=8561677) | 探索“反向 OCR”这一项目的创作思路与展示。 | 745 | 89 | 2014-11-05 |
| 18 | [Help the Gnome Foundation Defend the Gnome Trademark Against Groupon](https://news.ycombinator.com/item?id=8589283) | Gnome 基金会呼吁协助应对与 Groupon 之间的商标争议。 | 722 | 208 | 2014-11-11 |
| 19 | [The Other Side of Diversity](https://news.ycombinator.com/item?id=8557958) | 作者分享多元化议题的另一面，呈现自己的观察与经历。 | 704 | 447 | 2014-11-04 |
| 20 | [Go is moving to GitHub](https://news.ycombinator.com/item?id=8605204) | Go 项目宣布迁移至 GitHub。 | 686 | 236 | 2014-11-14 |

## 2014-12

有效主帖 19,182 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [NASA: We're sending humans to Mars](https://news.ycombinator.com/item?id=8688002) | NASA 表示正在推进将人类送往火星的计划。 | 1424 | 586 | 2014-12-02 |
| 2 | [“Was isolated from 1999 to 2006 with a 486. Built my own late 80s OS”](https://news.ycombinator.com/item?id=8747053) | 一位在一九九九至二〇〇六年间与外界隔绝的人，用四八六电脑自制操作系统。 | 1284 | 265 | 2014-12-14 |
| 3 | [Nature makes all articles free to view](https://news.ycombinator.com/item?id=8685291) | 《Nature》宣布让所有文章可供免费查看。 | 1102 | 128 | 2014-12-02 |
| 4 | [Farewell, Dr. Dobb's](https://news.ycombinator.com/item?id=8758915) | 向程序员媒体《Dr. Dobb's》道别。 | 1029 | 320 | 2014-12-16 |
| 5 | [CoreOS is building a container runtime, Rocket](https://news.ycombinator.com/item?id=8682525) | CoreOS 正在开发名为 Rocket 的容器运行时。 | 902 | 277 | 2014-12-01 |
| 6 | [“Warning: Do Not use my mirrors/services until I have reviewed the situation”](https://news.ycombinator.com/item?id=8780820) | 服务维护者发出警告，要求在核查情况完成前暂停使用其镜像与服务。 | 883 | 157 | 2014-12-21 |
| 7 | [US Senate Report on CIA Detention and Interrogation Program](https://news.ycombinator.com/item?id=8723548) | 美国参议院公布关于 CIA 拘押与审讯项目的报告。 | 879 | 551 | 2014-12-09 |
| 8 | [The Case for Slow Programming](https://news.ycombinator.com/item?id=8683827) | 作者为“慢编程”辩护，主张重新思考编写程序的节奏。 | 865 | 337 | 2014-12-01 |
| 9 | [Quake on an oscilloscope](https://news.ycombinator.com/item?id=8810857) | 将《Quake》的画面显示在示波器上。 | 859 | 70 | 2014-12-29 |
| 10 | [BPG Image format](https://news.ycombinator.com/item?id=8704629) | 介绍 BPG 图像格式及其公开资料。 | 843 | 328 | 2014-12-05 |
| 11 | [Git client vulnerability announced](https://news.ycombinator.com/item?id=8769667) | Git 客户端被披露存在安全漏洞。 | 818 | 177 | 2014-12-18 |
| 12 | [EFF in Court to Argue NSA Collection from Internet Backbone Is Unconstitutional](https://news.ycombinator.com/item?id=8767203) | EFF 出庭主张，NSA 从互联网骨干网络收集数据的行为违反宪法。 | 808 | 169 | 2014-12-18 |
| 13 | [India Orders 32 Websites Blocked, Including GitHub, Archive.Org, Pastebin](https://news.ycombinator.com/item?id=8820178) | 印度下令封锁三十二个网站，包括 GitHub、互联网档案馆与 Pastebin。 | 796 | 298 | 2014-12-31 |
| 14 | [Adblock Plus is probably the reason Firefox and Chrome are such memory hogs](https://news.ycombinator.com/item?id=8802424) | 文章提出，Adblock Plus 可能是 Firefox 与 Chrome 占用大量内存的原因。 | 748 | 400 | 2014-12-27 |
| 15 | [PostgreSQL 9.4 Released](https://news.ycombinator.com/item?id=8767475) | PostgreSQL 数据库发布 9.4 版本。 | 744 | 188 | 2014-12-18 |
| 16 | [Android Studio 1.0](https://news.ycombinator.com/item?id=8718776) | Android Studio 发布 1.0 版本。 | 725 | 227 | 2014-12-08 |
| 17 | [Why is every story on Uber Delhi driver raping a passenger getting instakilled?](https://news.ycombinator.com/item?id=8711284) | 发帖者追问，为何有关德里 Uber 司机涉嫌强奸乘客的报道提交后迅速被屏蔽。 | 698 | 110 | 2014-12-07 |
| 18 | [Look, no hands](https://news.ycombinator.com/item?id=8805053) | 体验名为“看，不用手”的网页项目。 | 698 | 140 | 2014-12-28 |
| 19 | [Are You a Robot? Introducing “No CAPTCHA ReCAPTCHA”](https://news.ycombinator.com/item?id=8693767) | Google 推出“No CAPTCHA reCAPTCHA”，尝试简化真人身份验证。 | 694 | 420 | 2014-12-03 |
| 20 | [How You Know](https://news.ycombinator.com/item?id=8753526) | Paul Graham 以《你如何知道》为题，探讨判断与认识的问题。 | 686 | 257 | 2014-12-15 |

## 2015-01

有效主帖 21,476 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [What should I do about YouTube?](https://news.ycombinator.com/item?id=8936257) | 作者面对与 YouTube 有关的处境，追问自己应当如何应对。 | 1391 | 290 | 2015-01-23 |
| 2 | [Hi, It’s Google Corporate Development](https://news.ycombinator.com/item?id=8878754) | 作者以 Google 企业发展部门来联络为切口，讲述相关经历。 | 1227 | 278 | 2015-01-13 |
| 3 | [YouTube now defaults to HTML5 video](https://news.ycombinator.com/item?id=8955426) | YouTube 宣布默认使用 HTML5 视频播放。 | 1035 | 393 | 2015-01-27 |
| 4 | [Hands-On with Microsoft's New Holographic Goggles](https://news.ycombinator.com/item?id=8924755) | 上手体验微软新推出的全息眼镜。 | 946 | 372 | 2015-01-21 |
| 5 | [Intel Compute Stick](https://news.ycombinator.com/item?id=8848182) | Intel 推出 Compute Stick 迷你计算设备。 | 929 | 335 | 2015-01-07 |
| 6 | [Announcing Rust 1.0 Alpha](https://news.ycombinator.com/item?id=8863451) | Rust 宣布发布 1.0 Alpha 版本。 | 894 | 243 | 2015-01-09 |
| 7 | [Be My Eyes – Lend your eyes to the blind](https://news.ycombinator.com/item?id=8892747) | Be My Eyes 邀请视力正常者协助盲人，让他人暂时“借用你的眼睛”。 | 827 | 160 | 2015-01-15 |
| 8 | [Command-line tools can be faster than your Hadoop cluster](https://news.ycombinator.com/item?id=8908462) | 作者展示命令行工具在某些任务中可能比 Hadoop 集群更快。 | 812 | 309 | 2015-01-18 |
| 9 | [What Happens When You Install the Top Download.com Apps](https://news.ycombinator.com/item?id=8876929) | 实际安装 Download.com 上的热门应用，观察会出现什么情况。 | 740 | 384 | 2015-01-12 |
| 10 | [Gotham 7.5K: A Rare High Altitude Night Flight Above NYC](https://news.ycombinator.com/item?id=8874706) | 从纽约市上空一次罕见的高空夜航，观看城市夜景。 | 735 | 112 | 2015-01-12 |
| 11 | [Firefox Hello](https://news.ycombinator.com/item?id=8963069) | 认识 Firefox Hello 及其公开功能介绍。 | 713 | 225 | 2015-01-28 |
| 12 | [What Doesn't Seem Like Work?](https://news.ycombinator.com/item?id=8902071) | 哪些事情做起来不像工作，这种感受又意味着什么？ | 712 | 321 | 2015-01-16 |
| 13 | [µBlock for Firefox](https://news.ycombinator.com/item?id=8916103) | µBlock 推出面向 Firefox 的版本。 | 707 | 264 | 2015-01-20 |
| 14 | [Britons: You Have 72 Hours to Stop the Snooper's Charter](https://news.ycombinator.com/item?id=8938223) | EFF 呼吁英国人在七十二小时内采取行动，阻止被称为“窥探者宪章”的措施。 | 700 | 105 | 2015-01-24 |
| 15 | [Man saves wife’s sight by 3D printing her brain tumor](https://news.ycombinator.com/item?id=8886164) | 一名男子通过三维打印妻子的脑肿瘤模型，帮助挽救她的视力。 | 697 | 144 | 2015-01-14 |
| 16 | [EFF’s Game Plan for Ending Global Mass Surveillance](https://news.ycombinator.com/item?id=8948639) | 电子前哨基金会提出终结全球大规模监控的行动方案。 | 678 | 151 | 2015-01-26 |
| 17 | [Don't Talk to Corp Dev](https://news.ycombinator.com/item?id=8876445) | Paul Graham 建议创业者不要与企业发展部门洽谈。 | 674 | 200 | 2015-01-12 |
| 18 | [A town of about 200 people, almost all of whom live in the same building](https://news.ycombinator.com/item?id=8840005) | 走进一个约有两百居民、几乎所有人都住在同一栋楼里的小镇。 | 673 | 177 | 2015-01-05 |
| 19 | [Io.js 1.0.0](https://news.ycombinator.com/item?id=8884128) | io.js 发布 1.0.0 版本。 | 634 | 186 | 2015-01-14 |
| 20 | [A Career in Science Will Cost You Your Firstborn](https://news.ycombinator.com/item?id=8863149) | 作者以“科研职业会让你付出头胎孩子的代价”为题，质疑科研生涯的成本。 | 629 | 393 | 2015-01-09 |

## 2015-02

有效主帖 20,551 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Email Encryption Software Relies on One Guy, Who Is Going Broke](https://news.ycombinator.com/item?id=9003791) | 广泛使用的邮件加密软件依赖一名维护者，而他正面临财务困境。 | 2088 | 453 | 2015-02-05 |
| 2 | [Leonard Nimoy, Spock of ‘Star Trek,’ Dies at 83](https://news.ycombinator.com/item?id=9119951) | 《星际迷航》中 Spock 的扮演者 Leonard Nimoy 去世，享年八十三岁。 | 1584 | 165 | 2015-02-27 |
| 3 | [FCC Passes Strict Net Neutrality Regulations on 3-2 Vote](https://news.ycombinator.com/item?id=9113976) | 美国 FCC 以三比二投票通过严格的网络中立性规则。 | 1489 | 711 | 2015-02-26 |
| 4 | [Magic](https://news.ycombinator.com/item?id=9087819) | 认识名为 Magic 的服务及其公开介绍。 | 1329 | 528 | 2015-02-22 |
| 5 | [FCC Chairman: This Is How We Will Ensure Net Neutrality](https://news.ycombinator.com/item?id=8997615) | 美国 FCC 主席说明，委员会将如何保障网络中立性。 | 1275 | 424 | 2015-02-04 |
| 6 | [Fuck It, I'm Going Back to Firefox](https://news.ycombinator.com/item?id=9045305) | 作者解释自己决定重新使用 Firefox 的原因。 | 1174 | 636 | 2015-02-13 |
| 7 | [Lenovo Caught Installing Adware on New Computers](https://news.ycombinator.com/item?id=9072424) | Lenovo 被发现向新电脑预装广告软件。 | 1142 | 419 | 2015-02-19 |
| 8 | [“Equation Group” ran the most advanced hacking operation ever uncovered](https://news.ycombinator.com/item?id=9058701) | 报道将“方程式组织”的黑客行动称为迄今发现的最先进攻击活动。 | 870 | 362 | 2015-02-16 |
| 9 | [Extracting the SuperFish certificate](https://news.ycombinator.com/item?id=9074110) | 分析并提取 SuperFish 证书，了解其中的安全问题。 | 867 | 231 | 2015-02-19 |
| 10 | [Stripe: Bitcoin](https://news.ycombinator.com/item?id=9075945) | Stripe 介绍其与比特币有关的服务。 | 855 | 368 | 2015-02-19 |
| 11 | [Ask HN: The “I want to do everything but end up doing nothing” dilemma](https://news.ycombinator.com/item?id=9049208) | 一名计算机专业学生求助：面对太多想学的方向，如何避免什么都没做成？ | 806 | 214 | 2015-02-14 |
| 12 | [Whiteboard Clock](https://news.ycombinator.com/item?id=9070140) | 展示名为“白板时钟”的创意项目。 | 784 | 82 | 2015-02-18 |
| 13 | [Windows 10 for Raspberry Pi 2](https://news.ycombinator.com/item?id=8983355) | 微软为 Raspberry Pi 2 提供 Windows 10 支持。 | 723 | 373 | 2015-02-02 |
| 14 | [CoreCLR is now open source](https://news.ycombinator.com/item?id=8991988) | 微软宣布 CoreCLR 开源。 | 709 | 333 | 2015-02-03 |
| 15 | [Side projects](https://news.ycombinator.com/item?id=9112250) | 围绕业余项目，作者分享自己的看法。 | 698 | 236 | 2015-02-26 |
| 16 | [Now, I can see wifi signals](https://news.ycombinator.com/item?id=9051246) | 作者展示把 Wi-Fi 信号变得可见的作品。 | 695 | 56 | 2015-02-15 |
| 17 | [Introducing Pebble Time](https://news.ycombinator.com/item?id=9100866) | Pebble 推出新款智能手表 Pebble Time。 | 658 | 386 | 2015-02-24 |
| 18 | [“Citizenfour” Awarded Oscar for Best Documentary in 2014](https://news.ycombinator.com/item?id=9092437) | 《第四公民》获得奥斯卡最佳纪录片奖。 | 647 | 156 | 2015-02-23 |
| 19 | [It's Time to Break Up the NSA (2014)](https://news.ycombinator.com/item?id=9107496) | 作者主张，到了拆分 NSA 的时候。 | 638 | 133 | 2015-02-25 |
| 20 | [F.C.C. Is Expected to Propose Regulating the Internet as a Utility](https://news.ycombinator.com/item?id=8985625) | 报道预计 FCC 将提议把互联网按公共事业方式监管。 | 636 | 438 | 2015-02-02 |

## 2015-03

有效主帖 23,204 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Unreal Engine 4 is now available to everyone for free](https://news.ycombinator.com/item?id=9132815) | Unreal Engine 4 宣布面向所有人免费开放。 | 1128 | 240 | 2015-03-02 |
| 2 | [Fired](https://news.ycombinator.com/item?id=9158913) | 作者讲述自己被解雇的经历。 | 1039 | 389 | 2015-03-06 |
| 3 | [React Native is now open source](https://news.ycombinator.com/item?id=9271246) | React Native 宣布开源。 | 1039 | 287 | 2015-03-26 |
| 4 | [Sir Terry Pratchett has died](https://news.ycombinator.com/item?id=9191248) | 作家 Terry Pratchett 去世的消息。 | 1019 | 223 | 2015-03-12 |
| 5 | [Announcing Starfighter](https://news.ycombinator.com/item?id=9173939) | 介绍新项目 Starfighter 及其公开计划。 | 932 | 400 | 2015-03-09 |
| 6 | [The new MacBook](https://news.ycombinator.com/item?id=9172373) | Apple 发布新款 MacBook。 | 921 | 1269 | 2015-03-09 |
| 7 | [Bidding farewell to Google Code](https://news.ycombinator.com/item?id=9191587) | Google 宣布告别代码托管服务 Google Code。 | 880 | 409 | 2015-03-12 |
| 8 | [Slack was hacked](https://news.ycombinator.com/item?id=9277370) | Slack 披露遭到入侵的安全事件。 | 857 | 497 | 2015-03-27 |
| 9 | [We are under attack](https://news.ycombinator.com/item?id=9233491) | 服务方声明自己正在遭受攻击，并介绍当前情况。 | 839 | 263 | 2015-03-19 |
| 10 | [Goodbye MongoDB, Hello PostgreSQL](https://news.ycombinator.com/item?id=9178773) | 团队分享从 MongoDB 转向 PostgreSQL 的经历。 | 802 | 374 | 2015-03-10 |
| 11 | [SQLite developer must have received a lot of phone calls](https://news.ycombinator.com/item?id=9196218) | 一段 SQLite 源码让发帖者感叹，开发者一定接到过不少电话。 | 792 | 108 | 2015-03-13 |
| 12 | [Stop using tail -f (mostly)](https://news.ycombinator.com/item?id=9290332) | 作者建议，在许多场景下停止使用 tail -f 的惯常做法。 | 765 | 207 | 2015-03-30 |
| 13 | [Amazon Dash Button](https://news.ycombinator.com/item?id=9296857) | Amazon 推出 Dash Button 按钮产品。 | 745 | 683 | 2015-03-31 |
| 14 | [China's Man-On-the-Side Attack on GitHub](https://news.ycombinator.com/item?id=9293849) | 分析被指来自中国、针对 GitHub 的旁路注入攻击。 | 692 | 309 | 2015-03-31 |
| 15 | [“Just remove the duck” (2013)](https://news.ycombinator.com/item?id=9137736) | 重读“只要把鸭子删掉”的故事，关注这句要求背后的开发经历。 | 682 | 327 | 2015-03-03 |
| 16 | [Replacing Photoshop with NSString](https://news.ycombinator.com/item?id=9240644) | 作者探索用 NSString 完成原本交由 Photoshop 的工作。 | 680 | 126 | 2015-03-20 |
| 17 | [VMWare Taken to Court Over GPL Violation](https://news.ycombinator.com/item?id=9151799) | VMware 因涉嫌违反 GPL 许可证被诉至法院。 | 664 | 289 | 2015-03-05 |
| 18 | [GitHub under ongoing DDoS attack](https://news.ycombinator.com/item?id=9284226) | GitHub 表示，平台正在遭受持续的 DDoS 攻击。 | 652 | 334 | 2015-03-29 |
| 19 | [Welcome Peter](https://news.ycombinator.com/item?id=9181001) | Y Combinator 发布欢迎 Peter 的公告。 | 649 | 148 | 2015-03-10 |
| 20 | [2015 Chromebook Pixel](https://news.ycombinator.com/item?id=9185526) | Google 推出二〇一五款 Chromebook Pixel。 | 643 | 628 | 2015-03-11 |

## 2015-04

有效主帖 22,991 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Microsoft Launches Visual Studio Code, a Free Cross-Platform Code Editor](https://news.ycombinator.com/item?id=9459364) | 微软发布免费、支持跨平台的代码编辑器 Visual Studio Code。 | 1608 | 543 | 2015-04-29 |
| 2 | [Console.mihai();](https://news.ycombinator.com/item?id=9448686) | 一篇以“Console.mihai();”为题、借用代码形式命名的个人文章。 | 1445 | 50 | 2015-04-27 |
| 3 | [New Hacker News Guideline: Avoid Gratuitous Negativity](https://news.ycombinator.com/item?id=9317916) | HN 新增社区准则，要求避免没有必要的负面表达。 | 1248 | 631 | 2015-04-03 |
| 4 | [I Quit: What really goes on at Apple](https://news.ycombinator.com/item?id=9342994) | 一位离职者讲述自己在 Apple 内部看到的情况。 | 1215 | 544 | 2015-04-08 |
| 5 | [The days are long but the decades are short](https://news.ycombinator.com/item?id=9454440) | 作者从“日子漫长，十年转瞬即逝”出发，思考时间与生活。 | 1163 | 387 | 2015-04-28 |
| 6 | [Project Fi by Google](https://news.ycombinator.com/item?id=9422033) | Google 公布 Project Fi 服务。 | 1107 | 581 | 2015-04-22 |
| 7 | [How to Center in CSS](https://news.ycombinator.com/item?id=9405284) | 介绍如何在 CSS 中实现元素居中。 | 1036 | 289 | 2015-04-19 |
| 8 | [Paul Hudak, co-creator of Haskell, has died](https://news.ycombinator.com/item?id=9465999) | Haskell 联合创始人 Paul Hudak 去世。 | 1014 | 89 | 2015-04-30 |
| 9 | [The sad state of sysadmin in the age of containers](https://news.ycombinator.com/item?id=9419188) | 作者批评容器时代的系统管理现状。 | 970 | 443 | 2015-04-22 |
| 10 | [Myself – v1.0.3](https://news.ycombinator.com/item?id=9317159) | 展示名为“Myself”、版本号为 1.0.3 的网页作品。 | 965 | 78 | 2015-04-03 |
| 11 | [Hidden backdoor API to root privileges in Apple OS X](https://news.ycombinator.com/item?id=9347669) | 研究者披露 Apple OS X 中一个可获得 root 权限的隐藏接口。 | 920 | 356 | 2015-04-09 |
| 12 | [Printing a wall-sized world map and what I've learned from it](https://news.ycombinator.com/item?id=9464348) | 作者讲述打印一张整面墙大小的世界地图，以及从中学到的事情。 | 919 | 220 | 2015-04-30 |
| 13 | [The 500-mile email (2002)](https://news.ycombinator.com/item?id=9338708) | 重读《五百英里的电子邮件》，追查一个与距离有关的邮件故障。 | 915 | 139 | 2015-04-08 |
| 14 | [Microsoft Launches Its .NET Distribution for Linux and Mac](https://news.ycombinator.com/item?id=9459513) | 微软发布面向 Linux 与 Mac 的 .NET 发行版本。 | 915 | 237 | 2015-04-29 |
| 15 | [What I'd tell myself about startups if I could go back 5 years](https://news.ycombinator.com/item?id=9333330) | 如果回到五年前，作者会给当时准备创业的自己哪些建议？ | 865 | 275 | 2015-04-07 |
| 16 | [Show HN: A tool that transforms your whole list with just one example](https://news.ycombinator.com/item?id=9432949) | 展示一款只需提供一个示例，就能转换整份列表的工具。 | 764 | 144 | 2015-04-24 |
| 17 | [Apple now rejecting apps with Pebble Smartwatch support](https://news.ycombinator.com/item?id=9426542) | 报道 Apple 开始拒绝支持 Pebble 智能手表的应用。 | 702 | 407 | 2015-04-23 |
| 18 | [Massive, Illicit Bust of Edward Snowden Stuck to a War Monument in Brooklyn](https://news.ycombinator.com/item?id=9329138) | 一座未经许可设置的 Edward Snowden 巨型半身像出现在布鲁克林战争纪念碑上。 | 696 | 360 | 2015-04-06 |
| 19 | [Docker without Docker](https://news.ycombinator.com/item?id=9442254) | 探索在不直接使用 Docker 的情况下实现相关容器能力。 | 681 | 97 | 2015-04-26 |
| 20 | [Announcing Git Large File Storage](https://news.ycombinator.com/item?id=9343021) | GitHub 公布 Git Large File Storage，帮助处理 Git 中的大文件。 | 620 | 159 | 2015-04-08 |

## 2015-05

有效主帖 22,243 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Lily – Drone camera](https://news.ycombinator.com/item?id=9532777) | 介绍名为 Lily 的无人机摄像产品。 | 1397 | 480 | 2015-05-12 |
| 2 | [Announcing Rust 1.0](https://news.ycombinator.com/item?id=9551937) | Rust 正式发布 1.0 版本。 | 1363 | 306 | 2015-05-15 |
| 3 | [John Nash Has Died](https://news.ycombinator.com/item?id=9596160) | 数学家 John Nash 去世的消息。 | 1282 | 249 | 2015-05-24 |
| 4 | [Be Kind](https://news.ycombinator.com/item?id=9534310) | 作者倡导以善意待人，并反思这种态度的意义。 | 1198 | 385 | 2015-05-12 |
| 5 | [Tesla Energy](https://news.ycombinator.com/item?id=9469316) | Tesla 公布能源业务 Tesla Energy。 | 1162 | 566 | 2015-05-01 |
| 6 | [GitTorrent: A Decentralized GitHub](https://news.ycombinator.com/item?id=9625840) | GitTorrent 提供去中心化的 GitHub 替代方案。 | 1038 | 169 | 2015-05-29 |
| 7 | [Postgres gets support for upsert](https://news.ycombinator.com/item?id=9509870) | PostgreSQL 增加 upsert 支持，可在插入发生冲突时更新数据。 | 1003 | 109 | 2015-05-08 |
| 8 | [The Unreasonable Effectiveness of Recurrent Neural Networks](https://news.ycombinator.com/item?id=9584325) | 探讨循环神经网络为何能展现出令人意外的效果。 | 913 | 207 | 2015-05-21 |
| 9 | [Fractal Lab](https://news.ycombinator.com/item?id=9488532) | 体验名为 Fractal Lab 的分形项目。 | 900 | 147 | 2015-05-04 |
| 10 | [Show HN: This page exists only if someone is looking at it](https://news.ycombinator.com/item?id=9531265) | 展示一个只有在有人查看时才会存在的网页。 | 803 | 165 | 2015-05-12 |
| 11 | [Node.js and io.js are merging under the Node Foundation](https://news.ycombinator.com/item?id=9542267) | Node.js 与 io.js 将在 Node 基金会旗下合并。 | 794 | 81 | 2015-05-13 |
| 12 | [Death of a Programmer, Life of a Farmer](https://news.ycombinator.com/item?id=9492110) | 围绕告别程序员身份、走向农夫生活的转变展开叙述。 | 698 | 341 | 2015-05-05 |
| 13 | [Solved by Flexbox](https://news.ycombinator.com/item?id=9587627) | 展示使用 Flexbox 解决网页布局问题的实例。 | 671 | 123 | 2015-05-22 |
| 14 | [Show HN: Twenty](https://news.ycombinator.com/item?id=9543005) | 作者展示名为 Twenty 的项目。 | 666 | 167 | 2015-05-14 |
| 15 | [U.S. NSA domestic phone spying program illegal: appeals court](https://news.ycombinator.com/item?id=9504939) | 美国上诉法院裁定，NSA 的国内电话监控项目违法。 | 653 | 143 | 2015-05-07 |
| 16 | [Talking About Money](https://news.ycombinator.com/item?id=9474012) | 作者讨论如何谈论金钱，以及相关话题带来的问题。 | 650 | 401 | 2015-05-01 |
| 17 | [B. B. King, Defining Bluesman for Generations, Dies at 89](https://news.ycombinator.com/item?id=9549181) | 影响数代人的布鲁斯音乐家 B. B. King 去世，享年八十九岁。 | 647 | 86 | 2015-05-15 |
| 18 | [Get Your Shit Together](https://news.ycombinator.com/item?id=9569934) | 一个以“把事情安排妥当”为主题的实用项目。 | 635 | 144 | 2015-05-19 |
| 19 | [Internet.org Is Not Neutral, Not Secure, and Not the Internet](https://news.ycombinator.com/item?id=9567976) | EFF 批评 Internet.org 的中立性与安全性，并质疑其能否代表互联网。 | 633 | 161 | 2015-05-19 |
| 20 | [Ross Ulbricht Sentenced to Life in Prison](https://news.ycombinator.com/item?id=9626985) | Ross Ulbricht 被判终身监禁。 | 623 | 609 | 2015-05-29 |

## 2015-06

有效主帖 21,981 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Same-Sex Marriage Is a Right, Supreme Court Rules](https://news.ycombinator.com/item?id=9784470) | 美国最高法院裁定，同性婚姻是一项权利。 | 1905 | 1215 | 2015-06-26 |
| 2 | [What Is Code?](https://news.ycombinator.com/item?id=9698870) | 从“代码是什么”出发，理解程序与软件世界。 | 1384 | 356 | 2015-06-11 |
| 3 | [“Swift will be open source later this year”](https://news.ycombinator.com/item?id=9680982) | Apple 宣布，Swift 将在当年稍后开源。 | 1334 | 548 | 2015-06-08 |
| 4 | [Google: 90% of our engineers use the software you wrote (Homebrew), but...](https://news.ycombinator.com/item?id=9695102) | 一则涉及 Google 招聘的经历：对方称九成工程师都在使用应聘者编写的 Homebrew，却仍有转折。 | 1257 | 654 | 2015-06-10 |
| 5 | [Atom 1.0](https://news.ycombinator.com/item?id=9778285) | Atom 文本编辑器发布 1.0 版本。 | 1096 | 442 | 2015-06-25 |
| 6 | [I quit the tech industry](https://news.ycombinator.com/item?id=9691002) | 作者宣布离开科技行业，并讲述自己的想法。 | 1017 | 548 | 2015-06-10 |
| 7 | [How Naughty Dog Fit Crash Bandicoot into 2MB of RAM on the PS1](https://news.ycombinator.com/item?id=9737156) | 回顾 Naughty Dog 如何让《Crash Bandicoot》在 PS1 的两 MB 内存中运行。 | 934 | 247 | 2015-06-18 |
| 8 | [Philae comet lander wakes up](https://news.ycombinator.com/item?id=9714497) | 彗星着陆器 Philae 从休眠中苏醒。 | 922 | 155 | 2015-06-14 |
| 9 | [From Asm.js to WebAssembly](https://news.ycombinator.com/item?id=9732827) | 介绍从 asm.js 走向 WebAssembly 的技术发展。 | 897 | 331 | 2015-06-17 |
| 10 | [To Apple, Love Taylor](https://news.ycombinator.com/item?id=9752948) | Taylor Swift 向 Apple 发表公开信。 | 891 | 512 | 2015-06-21 |
| 11 | [Looking Forward: Support for Secure Shell](https://news.ycombinator.com/item?id=9646971) | 微软展望对 Secure Shell 的支持。 | 828 | 390 | 2015-06-02 |
| 12 | [Inceptionism:  Going Deeper into Neural Networks](https://news.ycombinator.com/item?id=9736598) | 通过 Inceptionism 深入观察神经网络及其产生的图像。 | 797 | 156 | 2015-06-18 |
| 13 | [Let Snowden Come Home](https://news.ycombinator.com/item?id=9655693) | 作者呼吁允许 Edward Snowden 回国。 | 785 | 296 | 2015-06-03 |
| 14 | [Safari is the new IE](https://news.ycombinator.com/item?id=9804533) | 作者将 Safari 比作新的 IE，批评其对网页开发的影响。 | 753 | 356 | 2015-06-30 |
| 15 | [What's Really Warming the World?](https://news.ycombinator.com/item?id=9771493) | 究竟是什么因素在推动全球变暖？ | 750 | 523 | 2015-06-24 |
| 16 | [Tota11y](https://news.ycombinator.com/item?id=9797197) | 认识名为 Tota11y 的开发项目。 | 747 | 91 | 2015-06-29 |
| 17 | [Organizing complexity is the most important skill in software development](https://news.ycombinator.com/item?id=9757892) | 作者认为，组织和管理复杂性是软件开发中最重要的能力。 | 742 | 276 | 2015-06-22 |
| 18 | [Megaprocessor](https://news.ycombinator.com/item?id=9755742) | 认识名为 Megaprocessor 的处理器项目。 | 728 | 125 | 2015-06-22 |
| 19 | [Stripe Is the New PayPal](https://news.ycombinator.com/item?id=9738717) | Stripe 用户称支付被认定可能未经授权，且邮件未获回应，因此公开求助。 | 679 | 303 | 2015-06-18 |
| 20 | [DuckDuckGo on CNBC: We’ve grown 600% since NSA surveillance news broke](https://news.ycombinator.com/item?id=9730570) | DuckDuckGo 表示，自 NSA 监控消息曝光以来，服务增长了百分之六百。 | 636 | 245 | 2015-06-17 |

## 2015-07

有效主帖 22,375 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Spot the Drowning Child](https://news.ycombinator.com/item?id=9962185) | 通过寻找正在溺水的孩子，挑战自己辨认泳池险情的能力。 | 1215 | 378 | 2015-07-28 |
| 2 | [YC Fellowship](https://news.ycombinator.com/item?id=9917334) | Y Combinator 公布 YC Fellowship 计划。 | 998 | 378 | 2015-07-20 |
| 3 | [Web Design: The First 100 Years (2014)](https://news.ycombinator.com/item?id=9920121) | 一场以“网页设计的第一个一百年”为题的演讲，思考网页设计的发展。 | 988 | 233 | 2015-07-21 |
| 4 | [I noticed some disturbing privacy defaults in Windows 10](https://news.ycombinator.com/item?id=9976298) | 作者指出 Windows 10 的一些默认隐私设置令其不安。 | 965 | 574 | 2015-07-30 |
| 5 | [Front Page Subreddits Go Private in Response to Firing of Reddit Admin](https://news.ycombinator.com/item?id=9822580) | 为回应一名 Reddit 管理员被解雇，多个人气版块转为私有状态。 | 963 | 593 | 2015-07-03 |
| 6 | [Nintendo CEO Satoru Iwata has died [pdf]](https://news.ycombinator.com/item?id=9875549) | 任天堂首席执行官岩田聪去世。 | 937 | 179 | 2015-07-12 |
| 7 | [Firefox makes click-to-activate Flash the default](https://news.ycombinator.com/item?id=9883246) | Firefox 将 Flash 改为默认需要用户点击后才激活。 | 931 | 377 | 2015-07-14 |
| 8 | [Grooveshark co-founder, 28, found dead in home](https://news.ycombinator.com/item?id=9917442) | 二十八岁的 Grooveshark 联合创始人被发现死于家中。 | 922 | 136 | 2015-07-20 |
| 9 | [Ellen Pao Is Stepping Down as Reddit’s Chief](https://news.ycombinator.com/item?id=9866755) | Ellen Pao 辞去 Reddit 负责人职务。 | 862 | 822 | 2015-07-10 |
| 10 | [NASA’s Kepler Mission Discovers Bigger, Older Cousin to Earth](https://news.ycombinator.com/item?id=9936662) | NASA 开普勒任务发现一颗被称为地球“更大、更年长表亲”的行星。 | 851 | 294 | 2015-07-23 |
| 11 | [Tell HN: Hello](https://news.ycombinator.com/item?id=9910487) | 一位监狱看守向 HN 自我介绍，分享学习编程并准备申请 YC 的两年计划。 | 847 | 179 | 2015-07-19 |
| 12 | [7 Rejections](https://news.ycombinator.com/item?id=9874521) | 作者回顾自己收到的七次拒绝。 | 720 | 192 | 2015-07-12 |
| 13 | [Dear Google Mail Team](https://news.ycombinator.com/item?id=9905363) | 一封写给 Google 邮件团队的公开文字。 | 719 | 260 | 2015-07-17 |
| 14 | [Newegg vs. Patent Trolls: When We Win, You Win](https://news.ycombinator.com/item?id=9966201) | Newegg 讲述对抗专利诉讼公司的经历，并强调胜诉对消费者的意义。 | 704 | 151 | 2015-07-29 |
| 15 | [Ex-Googler says she exposed company-wide pay inequality with spreadsheet](https://news.ycombinator.com/item?id=9906107) | 一名前 Google 员工称，自己用电子表格揭示了公司内部薪酬不平等。 | 699 | 479 | 2015-07-18 |
| 16 | [Hackers Remotely Attack a Jeep on the Highway](https://news.ycombinator.com/item?id=9921557) | 黑客演示远程攻击一辆正在高速公路上行驶的 Jeep。 | 691 | 603 | 2015-07-21 |
| 17 | [Ask HN: Who is hiring? (July 2015)](https://news.ycombinator.com/item?id=9812245) | HN 二〇一五年七月招聘帖，汇集公司直接发布的职位与工作方式信息。 | 673 | 1086 | 2015-07-01 |
| 18 | [Show HN: Bocker – Docker implemented in 100 lines of bash](https://news.ycombinator.com/item?id=9925896) | Bocker 用约一百行 Bash 实现类似 Docker 的功能。 | 662 | 87 | 2015-07-21 |
| 19 | [If you've nothing to hide, you've got nothing to fear](https://news.ycombinator.com/item?id=9869755) | 围绕“没什么可隐瞒就没什么可害怕”的说法，反思隐私与安全。 | 658 | 308 | 2015-07-11 |
| 20 | [Stuff in Space](https://news.ycombinator.com/item?id=9841831) | 浏览名为 Stuff in Space 的太空主题项目。 | 629 | 130 | 2015-07-06 |

## 2015-08

有效主帖 20,604 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [G is for Google](https://news.ycombinator.com/item?id=10037157) | Google 以“G 代表 Google”为题发布新的公司安排。 | 2228 | 562 | 2015-08-10 |
| 2 | [“Two days ago the police came to me and wanted me to stop working on this”](https://news.ycombinator.com/item?id=10101469) | 一位开发者称，警方曾要求自己停止继续开发相关项目。 | 1543 | 525 | 2015-08-22 |
| 3 | [OnHub](https://news.ycombinator.com/item?id=10080065) | 认识名为 OnHub 的产品。 | 984 | 615 | 2015-08-18 |
| 4 | [Show HN: My SSH server knows who you are](https://news.ycombinator.com/item?id=10004678) | 作者展示一个声称能识别访问者身份的 SSH 服务器。 | 836 | 245 | 2015-08-04 |
| 5 | [Phoenix 1.0](https://news.ycombinator.com/item?id=10135825) | Phoenix 框架发布 1.0 版本。 | 792 | 223 | 2015-08-28 |
| 6 | [The Web We Have to Save](https://news.ycombinator.com/item?id=9994653) | 作者呼吁保护某种正在消失的网络形态。 | 760 | 238 | 2015-08-03 |
| 7 | [Pixar in a Box – Khan Academy](https://news.ycombinator.com/item?id=10129914) | 可汗学院推出 Pixar in a Box 项目。 | 753 | 65 | 2015-08-27 |
| 8 | [Inside Amazon: Wrestling Big Ideas in a Bruising Workplace](https://news.ycombinator.com/item?id=10065243) | 报道 Amazon 内部的工作环境，以及其中想法碰撞与高压体验。 | 708 | 424 | 2015-08-15 |
| 9 | [Bootstrap 4 alpha](https://news.ycombinator.com/item?id=10086651) | Bootstrap 4 发布 Alpha 版本。 | 655 | 208 | 2015-08-19 |
| 10 | [“It’s done, there is no way back. We tried, we failed”](https://news.ycombinator.com/item?id=10047721) | 项目方宣布尝试失败、已无退路，向支持者交代项目结局。 | 645 | 374 | 2015-08-12 |
| 11 | [“Stop reverse engineering our code”](https://news.ycombinator.com/item?id=10039202) | 作者要求外界停止对其代码进行逆向工程。 | 613 | 344 | 2015-08-11 |
| 12 | [Eve Version 0](https://news.ycombinator.com/item?id=10073578) | Eve 公布最初的零号版本。 | 590 | 190 | 2015-08-17 |
| 13 | [Ask HN: I will help your startup in exchange for food and a place to stay](https://news.ycombinator.com/item?id=10032299) | 发帖者愿为创业公司编程，以食宿代替报酬，并说明自己的签证处境。 | 584 | 278 | 2015-08-10 |
| 14 | [Twitter Contest Winning as a Service](https://news.ycombinator.com/item?id=10001364) | 作者探索把赢得 Twitter 抽奖变成一项服务。 | 578 | 97 | 2015-08-04 |
| 15 | [AT&T Helped N.S.A. Spy on an Array of Internet Traffic](https://news.ycombinator.com/item?id=10066014) | 报道 AT&T 协助 NSA 监控多种互联网流量。 | 568 | 117 | 2015-08-15 |
| 16 | [Go 1.5 is released](https://news.ycombinator.com/item?id=10086900) | Go 编程语言发布 1.5 版本。 | 559 | 103 | 2015-08-19 |
| 17 | [Hawaii Bans Non-Compete and Non-Solicit Clauses in High-Tech Employment](https://news.ycombinator.com/item?id=10013598) | 夏威夷禁止高科技雇佣合同中的竞业限制与禁止招揽条款。 | 533 | 173 | 2015-08-05 |
| 18 | [Multiple Vulnerabilities in Pocket](https://news.ycombinator.com/item?id=10078967) | 研究者披露 Pocket 中的多个安全漏洞。 | 533 | 154 | 2015-08-18 |
| 19 | [Hack: A typeface designed for source code](https://news.ycombinator.com/item?id=10140728) | Hack 是一款专为阅读和编写源代码设计的字体。 | 521 | 243 | 2015-08-29 |
| 20 | [OS X Command Line Utilities](https://news.ycombinator.com/item?id=10143143) | 介绍 OS X 中可用的命令行实用工具。 | 517 | 202 | 2015-08-30 |

## 2015-09

有效主帖 21,955 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [14-Year-Old Boy Arrested for Bringing Homemade Clock to School](https://news.ycombinator.com/item?id=10226196) | 一名十四岁男孩因把自制时钟带到学校而被捕。 | 1952 | 946 | 2015-09-16 |
| 2 | [Amazon Web Services in Plain English](https://news.ycombinator.com/item?id=10202286) | 用通俗语言解释 Amazon Web Services 的各项服务。 | 1479 | 223 | 2015-09-11 |
| 3 | [Node v4.0.0](https://news.ycombinator.com/item?id=10187596) | Node.js 发布 4.0.0 版本。 | 1248 | 267 | 2015-09-08 |
| 4 | [Show HN: Make a programmable mirror](https://news.ycombinator.com/item?id=10204018) | 展示如何制作一面可以编程的镜子。 | 1172 | 136 | 2015-09-11 |
| 5 | [Our First Certificate Is Now Live](https://news.ycombinator.com/item?id=10217470) | 证书服务宣布其签发的第一张证书已经上线。 | 1131 | 255 | 2015-09-14 |
| 6 | [Signs of Liquid Water Found on Surface of Mars, Study Says](https://news.ycombinator.com/item?id=10290793) | 一项研究报告称，在火星表面发现液态水存在的迹象。 | 1011 | 178 | 2015-09-28 |
| 7 | [React Native for Android](https://news.ycombinator.com/item?id=10216234) | React Native 推出 Android 支持。 | 907 | 240 | 2015-09-14 |
| 8 | ['Happy Birthday' song copyright is not valid, judge rules](https://news.ycombinator.com/item?id=10262682) | 法官裁定，《生日快乐》歌曲的相关版权主张无效。 | 872 | 196 | 2015-09-23 |
| 9 | [Drug Goes from $13.50 a Tablet to $750, Overnight](https://news.ycombinator.com/item?id=10251637) | 一种药物的单片售价一夜间从十三点五美元涨至七百五十美元。 | 830 | 450 | 2015-09-21 |
| 10 | [Otto, the successor to Vagrant](https://news.ycombinator.com/item?id=10291778) | HashiCorp 推出 Otto，将其定位为 Vagrant 的后继工具。 | 772 | 177 | 2015-09-28 |
| 11 | [When Your Former Boss Sues You for Starting a Startup](https://news.ycombinator.com/item?id=10261825) | 一位创业者讲述因创办公司而被前老板起诉的处境。 | 767 | 233 | 2015-09-22 |
| 12 | [Dropbox has open-sourced Zulip](https://news.ycombinator.com/item?id=10279961) | Dropbox 宣布将 Zulip 开源。 | 755 | 313 | 2015-09-25 |
| 13 | [What Happens Next Will Amaze You](https://news.ycombinator.com/item?id=10263183) | 一场以“接下来发生的事会让你惊讶”为题的演讲。 | 753 | 281 | 2015-09-23 |
| 14 | [The Pixel Factory](https://news.ycombinator.com/item?id=10180608) | 展示名为《像素工厂》的技术演示。 | 739 | 47 | 2015-09-07 |
| 15 | [Two HN Announcements](https://news.ycombinator.com/item?id=10298512) | Hacker News 发布两则社区公告。 | 698 | 284 | 2015-09-29 |
| 16 | [Google’s look, evolved](https://news.ycombinator.com/item?id=10153164) | Google 公布更新后的视觉形象。 | 683 | 430 | 2015-09-01 |
| 17 | [Google Will Soon Start Punishing Mobile Sites that Use Annoying App Install Ads](https://news.ycombinator.com/item?id=10155421) | Google 将对使用恼人应用安装广告的移动网站采取降权措施。 | 683 | 302 | 2015-09-01 |
| 18 | [Show HN: I spent a year making an electro-mechanical prototype of a liquid clock](https://news.ycombinator.com/item?id=10284321) | 作者展示花费一年制作的机电式液体时钟原型。 | 681 | 103 | 2015-09-26 |
| 19 | [Researchers Could Have Uncovered Volkswagen’s Emissions Cheat If Not for DMCA](https://news.ycombinator.com/item?id=10256170) | EFF 认为，若非 DMCA 的限制，研究者本可更早发现 Volkswagen 排放作弊。 | 641 | 158 | 2015-09-22 |
| 20 | [The Website That Got Me Expelled](https://news.ycombinator.com/item?id=10174152) | 作者讲述一个让自己被学校开除的网站。 | 639 | 281 | 2015-09-05 |

## 2015-10

有效主帖 24,655 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [YC Research](https://news.ycombinator.com/item?id=10347821) | Y Combinator 公布 YC Research 研究计划。 | 1776 | 370 | 2015-10-07 |
| 2 | [Let's Encrypt is Trusted](https://news.ycombinator.com/item?id=10417206) | Let's Encrypt 宣布其证书已获得信任。 | 1260 | 311 | 2015-10-20 |
| 3 | [Free Lossless Image Format](https://news.ycombinator.com/item?id=10317790) | 介绍名为 FLIF 的免费无损图像格式。 | 1254 | 362 | 2015-10-02 |
| 4 | [Didn’t Homejoy Shut Down?](https://news.ycombinator.com/item?id=10466888) | Homejoy 不是已经关闭了吗，相关业务的现状为何令人困惑？ | 1121 | 339 | 2015-10-28 |
| 5 | [How is NSA breaking so much crypto?](https://news.ycombinator.com/item?id=10390822) | NSA 究竟是如何破解如此多加密系统的？ | 1005 | 246 | 2015-10-15 |
| 6 | [New Windows 10 Devices From Microsoft](https://news.ycombinator.com/item?id=10339388) | 微软公布一批新的 Windows 10 设备。 | 875 | 949 | 2015-10-06 |
| 7 | [Larry Wall Unveils Perl 6.0.0](https://news.ycombinator.com/item?id=10341832) | Larry Wall 展示 Perl 6.0.0。 | 809 | 319 | 2015-10-06 |
| 8 | [Show HN: Twitch Installs Arch Linux – A cooperative text-based horror game](https://news.ycombinator.com/item?id=10477721) | 让 Twitch 观众合作安装 Arch Linux，作者把过程形容为文字恐怖游戏。 | 802 | 250 | 2015-10-30 |
| 9 | [Blowing the Whistle on the UC Berkeley Mathematics Department](https://news.ycombinator.com/item?id=10372181) | 作者公开举报加州大学伯克利分校数学系的问题。 | 778 | 260 | 2015-10-12 |
| 10 | [Mercury Spill](https://news.ycombinator.com/item?id=10357115) | 围绕一次汞泄漏，作者记录相关情况。 | 764 | 359 | 2015-10-08 |
| 11 | [EFF Wins Petition to Inspect and Modify Car Software](https://news.ycombinator.com/item?id=10460427) | EFF 争取检查和修改汽车软件的请愿获得通过。 | 730 | 107 | 2015-10-27 |
| 12 | [Amazon Will Ban Sale of Apple, Google Video-Streaming Devices](https://news.ycombinator.com/item?id=10312938) | Amazon 将禁止销售 Apple 与 Google 的视频流媒体设备。 | 716 | 529 | 2015-10-01 |
| 13 | [A story about &lt;input&gt;](https://news.ycombinator.com/item?id=10433793) | 围绕 HTML 的 input 元素，讲述一个网页开发故事。 | 693 | 181 | 2015-10-22 |
| 14 | [The Final Leaked TPP Text Is All That We Feared](https://news.ycombinator.com/item?id=10363500) | EFF 认为泄露的 TPP 最终文本印证了此前的担忧。 | 667 | 180 | 2015-10-09 |
| 15 | [Cops are asking Ancestry.com and 23andMe for their customers’ DNA](https://news.ycombinator.com/item?id=10400550) | 警方开始向 Ancestry.com 与 23andMe 索取客户的 DNA 数据。 | 658 | 216 | 2015-10-16 |
| 16 | [Write like you talk](https://news.ycombinator.com/item?id=10448445) | Paul Graham 建议，用接近日常说话的方式写作。 | 647 | 272 | 2015-10-25 |
| 17 | [Screenshots from developers and Unix people taken in 2002](https://news.ycombinator.com/item?id=10469824) | 回看二〇〇二年开发者与 Unix 用户留下的桌面截图。 | 638 | 232 | 2015-10-29 |
| 18 | [A Guide to Fast Page Loads](https://news.ycombinator.com/item?id=10345589) | 介绍加快网页加载速度的方法。 | 597 | 163 | 2015-10-07 |
| 19 | [Ogo, a new take on personal transportation](https://news.ycombinator.com/item?id=10412030) | Ogo 提出一种新的个人交通工具设计。 | 588 | 182 | 2015-10-19 |
| 20 | [Twitter announces layoffs](https://news.ycombinator.com/item?id=10379948) | Twitter 宣布裁员。 | 582 | 381 | 2015-10-13 |

## 2015-11

有效主帖 21,927 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Jessica Livingston](https://news.ycombinator.com/item?id=10575953) | 介绍 Jessica Livingston 及其相关经历。 | 1740 | 307 | 2015-11-16 |
| 2 | [TensorFlow: open-source library for machine intelligence](https://news.ycombinator.com/item?id=10532957) | TensorFlow 开源机器智能库公开发布。 | 1559 | 196 | 2015-11-09 |
| 3 | [Google engineer writing Amazon reviews on USB-C cables that don't work](https://news.ycombinator.com/item?id=10508494) | 一位 Google 工程师在 Amazon 留评，指出一些 USB-C 线材无法正常工作。 | 1524 | 392 | 2015-11-04 |
| 4 | [VLC contributor living in Aleppo writing about the Paris attacks](https://news.ycombinator.com/item?id=10580208) | 一位住在阿勒颇的 VLC 贡献者写下对巴黎袭击事件的看法。 | 1368 | 705 | 2015-11-17 |
| 5 | [Visual Studio Code is now open source](https://news.ycombinator.com/item?id=10588264) | Visual Studio Code 宣布开源。 | 1325 | 391 | 2015-11-18 |
| 6 | [Raspberry Pi Zero: the $5 computer](https://news.ycombinator.com/item?id=10631668) | Raspberry Pi Zero 推出，售价五美元。 | 1271 | 513 | 2015-11-26 |
| 7 | [Startup Playbook](https://news.ycombinator.com/item?id=10514729) | 一本介绍创业实践的 Startup Playbook。 | 1202 | 232 | 2015-11-05 |
| 8 | [Reconsider](https://news.ycombinator.com/item?id=10506422) | 作者以《重新考虑》为题，邀请读者反思已有选择。 | 906 | 154 | 2015-11-04 |
| 9 | [Please don't use Slack for FOSS projects](https://news.ycombinator.com/item?id=10486541) | 作者呼吁自由及开源软件项目不要使用 Slack。 | 886 | 484 | 2015-11-01 |
| 10 | [Text of the Trans-Pacific Partnership](https://news.ycombinator.com/item?id=10512882) | 查阅《跨太平洋伙伴关系协定》的公开文本。 | 755 | 348 | 2015-11-05 |
| 11 | [Show HN: Something pointless I made](https://news.ycombinator.com/item?id=10646440) | 作者展示一个自己形容为“没有意义”的趣味作品。 | 747 | 102 | 2015-11-29 |
| 12 | [Gene Amdahl has died](https://news.ycombinator.com/item?id=10557793) | 计算机科学家 Gene Amdahl 去世。 | 740 | 111 | 2015-11-13 |
| 13 | [A Decade-Old Gag Order, Lifted](https://news.ycombinator.com/item?id=10651617) | 一项持续十年的禁言令被解除。 | 737 | 146 | 2015-11-30 |
| 14 | [Pirated Courses on Udemy](https://news.ycombinator.com/item?id=10638795) | 作者指出 Udemy 平台存在盗版课程问题。 | 701 | 236 | 2015-11-27 |
| 15 | [Show HN: Parinfer – a simpler way to write Lisp](https://news.ycombinator.com/item?id=10547772) | Parinfer 尝试让 Lisp 的编写方式更简单。 | 674 | 134 | 2015-11-11 |
| 16 | [What happens when a culture is driven by the need for money to make more money](https://news.ycombinator.com/item?id=10547575) | 当文化被“让钱生出更多钱”的需求主导时，会发生什么？ | 669 | 485 | 2015-11-11 |
| 17 | [My Livecoding.tv account deletion saga](https://news.ycombinator.com/item?id=10486476) | 作者记录删除 Livecoding.tv 账号时遇到的一连串波折。 | 667 | 420 | 2015-11-01 |
| 18 | [Don't copy paste from a website to a terminal](https://news.ycombinator.com/item?id=10554679) | 提醒用户注意，从网站复制内容到终端可能带来安全问题。 | 665 | 244 | 2015-11-12 |
| 19 | [Comcast injects JavaScript into webpages to show copyright notices to customers](https://news.ycombinator.com/item?id=10592775) | Comcast 被发现向网页注入 JavaScript，以向用户展示版权提醒。 | 645 | 392 | 2015-11-19 |
| 20 | [Times Pulls Article Blaming Encryption in Paris Terror Attack](https://news.ycombinator.com/item?id=10580412) | 《纽约时报》撤下一篇将巴黎恐袭归咎于加密技术的文章。 | 643 | 296 | 2015-11-17 |

## 2015-12

有效主帖 21,086 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Swift is Open Source](https://news.ycombinator.com/item?id=10669891) | Swift 编程语言正式开源。 | 1824 | 432 | 2015-12-03 |
| 2 | [Instagram's Million Dollar Bug](https://news.ycombinator.com/item?id=10754194) | 研究者讲述 Instagram 中一个被称为“百万美元漏洞”的安全问题。 | 1562 | 516 | 2015-12-17 |
| 3 | [In Memoriam: Ian Murdock](https://news.ycombinator.com/item?id=10813524) | 悼念 Ian Murdock，回顾与他有关的记忆。 | 1457 | 366 | 2015-12-30 |
| 4 | [SpaceX launch webcast: Orbcomm-2 Mission [video]](https://news.ycombinator.com/item?id=10774865) | 观看 SpaceX 的 Orbcomm-2 任务发射直播。 | 1284 | 426 | 2015-12-22 |
| 5 | [Entering Public Beta](https://news.ycombinator.com/item?id=10671356) | 证书服务宣布进入公开测试阶段。 | 1249 | 213 | 2015-12-03 |
| 6 | [Introducing OpenAI](https://news.ycombinator.com/item?id=10720176) | OpenAI 正式公开亮相并介绍其计划。 | 1107 | 376 | 2015-12-11 |
| 7 | [Show HN: Open Hunt – an open and community-run alternative to Product Hunt](https://news.ycombinator.com/item?id=10759879) | Open Hunt 提供由社区运营、开放的 Product Hunt 替代平台。 | 1093 | 180 | 2015-12-18 |
| 8 | [Springer Textbooks More Than 10 Years Old Available for Free Legal Download](https://news.ycombinator.com/item?id=10810271) | 出版超过十年的 Springer 教科书可免费合法下载。 | 990 | 171 | 2015-12-30 |
| 9 | [The first person to hack the iPhone is building a self-driving car](https://news.ycombinator.com/item?id=10744206) | 第一位破解 iPhone 的人正在打造自动驾驶汽车。 | 949 | 447 | 2015-12-16 |
| 10 | [Open Letter to Mozilla: Bring Back Persona](https://news.ycombinator.com/item?id=10787972) | 一封致 Mozilla 的公开信，呼吁恢复 Persona。 | 905 | 237 | 2015-12-24 |
| 11 | [Leaving the Mac App Store](https://news.ycombinator.com/item?id=10655853) | 开发团队宣布退出 Mac App Store。 | 884 | 401 | 2015-12-01 |
| 12 | [Microsoft Edge's JavaScript engine to go open-source](https://news.ycombinator.com/item?id=10682003) | Microsoft Edge 的 JavaScript 引擎将开源。 | 852 | 268 | 2015-12-05 |
| 13 | [Facebook is misleading Indians with its full-page ads about Free Basics](https://news.ycombinator.com/item?id=10791198) | 作者指责 Facebook 有关 Free Basics 的整版广告误导印度公众。 | 804 | 245 | 2015-12-25 |
| 14 | [Kazakhstan to MitM all HTTPS traffic starting Jan 1](https://news.ycombinator.com/item?id=10663843) | 报道哈萨克斯坦计划从一月一日起，对所有 HTTPS 流量实施中间人拦截。 | 803 | 361 | 2015-12-02 |
| 15 | [A letter to our daughter](https://news.ycombinator.com/item?id=10658787) | 一对父母写给女儿的信，分享他们的愿望与思考。 | 790 | 518 | 2015-12-01 |
| 16 | [How to be like Steve Ballmer](https://news.ycombinator.com/item?id=10662666) | 作者探讨如何像 Steve Ballmer 那样行事。 | 763 | 188 | 2015-12-02 |
| 17 | [Big Company vs. Startup Work and Compensation](https://news.ycombinator.com/item?id=10758278) | 比较在大公司与创业公司工作时，工作内容和报酬上的取舍。 | 730 | 402 | 2015-12-18 |
| 18 | [This Is Not a Day Care. It’s a University](https://news.ycombinator.com/item?id=10654831) | 作者主张，大学应以大学的方式办学，并以托儿所作比喻表达立场。 | 729 | 672 | 2015-12-01 |
| 19 | [How Product Hunt really works](https://news.ycombinator.com/item?id=10739875) | 作者解释自己眼中 Product Hunt 的实际运作方式。 | 695 | 222 | 2015-12-15 |
| 20 | [Who Y Combinator Companies Want](https://news.ycombinator.com/item?id=10698009) | 分析 Y Combinator 旗下公司希望招聘什么样的人。 | 667 | 527 | 2015-12-08 |

## 2016-01

有效主帖 23,497 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Request For Research: Basic Income](https://news.ycombinator.com/item?id=10982340) | Y Combinator 征集围绕基本收入开展研究的方案。 | 1876 | 1121 | 2016-01-27 |
| 2 | [Dear GitHub](https://news.ycombinator.com/item?id=10904671) | 一封题为《亲爱的 GitHub》的公开信，向平台表达诉求。 | 1678 | 463 | 2016-01-14 |
| 3 | [David Bowie Has Died](https://news.ycombinator.com/item?id=10879262) | 音乐人 David Bowie 去世。 | 1484 | 301 | 2016-01-11 |
| 4 | [Amazon's customer service backdoor](https://news.ycombinator.com/item?id=10963568) | 作者指出，Amazon 客服流程可能成为绕过安全保护的后门。 | 1447 | 356 | 2016-01-24 |
| 5 | [Marvin Minsky dies at 88](https://news.ycombinator.com/item?id=10970867) | 人工智能先驱 Marvin Minsky 去世，享年八十八岁。 | 1259 | 178 | 2016-01-25 |
| 6 | [Google achieves AI 'breakthrough' by beating Go champion](https://news.ycombinator.com/item?id=10981679) | Google 人工智能击败围棋冠军，被报道为一项技术突破。 | 1207 | 394 | 2016-01-27 |
| 7 | [Facebook is closing Parse](https://news.ycombinator.com/item?id=10991729) | Facebook 宣布关闭 Parse 服务。 | 1202 | 500 | 2016-01-28 |
| 8 | [How to C in 2016](https://news.ycombinator.com/item?id=10864176) | 从二〇一六年的实践出发，介绍如何使用 C 语言。 | 1145 | 581 | 2016-01-08 |
| 9 | [Dutch government says no to backdoors, grants $540k to OpenSSL](https://news.ycombinator.com/item?id=10841816) | 荷兰政府表态反对加密后门，并向 OpenSSL 提供五十四万美元资助。 | 1144 | 99 | 2016-01-05 |
| 10 | [The Website Obesity Crisis](https://news.ycombinator.com/item?id=10820445) | 作者以“网站肥胖危机”为题，批评网页体积不断膨胀。 | 1122 | 367 | 2016-01-01 |
| 11 | [Top Books on Amazon Based on Links in Hacker News Comments](https://news.ycombinator.com/item?id=10924741) | 根据 HN 评论中的链接，整理最常被提及的 Amazon 图书。 | 1043 | 181 | 2016-01-18 |
| 12 | [TrendMicro Node.js HTTP server listening on localhost can execute commands](https://news.ycombinator.com/item?id=10882563) | Trend Micro 的本地 Node.js HTTP 服务被披露存在可执行命令的问题。 | 1030 | 229 | 2016-01-11 |
| 13 | [Netflix Is Now Available Around the World](https://news.ycombinator.com/item?id=10852261) | Netflix 宣布将服务扩展到全球更多地区。 | 1015 | 497 | 2016-01-06 |
| 14 | [Life is Short](https://news.ycombinator.com/item?id=10917446) | Paul Graham 围绕“人生苦短”思考时间与生活选择。 | 970 | 408 | 2016-01-16 |
| 15 | [The resolution of the Bitcoin experiment](https://news.ycombinator.com/item?id=10905118) | 作者对比特币实验的走向作出自己的判断。 | 961 | 408 | 2016-01-14 |
| 16 | [Dear open-source maintainers, a letter from GitLab](https://news.ycombinator.com/item?id=10923379) | GitLab 致信开源维护者，回应大型开源项目的需求。 | 924 | 318 | 2016-01-18 |
| 17 | [Caltech Researchers Find Evidence of a Planet Beyond Pluto](https://news.ycombinator.com/item?id=10939306) | 加州理工研究者发现冥王星之外可能存在另一颗行星的证据。 | 883 | 150 | 2016-01-20 |
| 18 | [The Refragmentation](https://news.ycombinator.com/item?id=10826836) | Paul Graham 以《重新碎片化》为题，讨论分化的趋势。 | 852 | 444 | 2016-01-02 |
| 19 | [Desktop Neo – rethinking the desktop interface for productivity](https://news.ycombinator.com/item?id=10932378) | Desktop Neo 重新设计桌面界面，希望提高工作效率。 | 798 | 314 | 2016-01-19 |
| 20 | [Linux Foundation quietly drops community representation](https://news.ycombinator.com/item?id=10942294) | 作者指责 Linux 基金会悄然取消社区代表机制。 | 778 | 185 | 2016-01-20 |

## 2016-02

有效主帖 24,217 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [A Message to Our Customers](https://news.ycombinator.com/item?id=11116274) | Apple 向客户发布一封公开信。 | 5771 | 967 | 2016-02-17 |
| 2 | [Physicists Detect Gravitational Waves, Proving Einstein Right](https://news.ycombinator.com/item?id=11080701) | 物理学家探测到引力波，为 Einstein 的理论提供新的验证。 | 2011 | 483 | 2016-02-11 |
| 3 | [Stripe Atlas](https://news.ycombinator.com/item?id=11166417) | Stripe 推出 Atlas 服务。 | 1659 | 390 | 2016-02-24 |
| 4 | [Graphing when your Facebook friends are awake](https://news.ycombinator.com/item?id=11130688) | 通过图表观察 Facebook 好友何时醒着。 | 1302 | 189 | 2016-02-19 |
| 5 | [Apple’s declining software quality](https://news.ycombinator.com/item?id=11034071) | 作者认为 Apple 的软件质量正在下降。 | 1282 | 705 | 2016-02-04 |
| 6 | [Introducing the Keybase filesystem](https://news.ycombinator.com/item?id=11037257) | Keybase 推出自己的文件系统。 | 1252 | 462 | 2016-02-04 |
| 7 | [Microsoft Acquires Xamarin](https://news.ycombinator.com/item?id=11169215) | 微软宣布收购 Xamarin。 | 1126 | 383 | 2016-02-24 |
| 8 | [LinkedIn shares drop 40%, erasing $10B of company's value](https://news.ycombinator.com/item?id=11042278) | LinkedIn 股价下跌百分之四十，公司市值蒸发一百亿美元。 | 1012 | 635 | 2016-02-05 |
| 9 | [Vulkan is Here](https://news.ycombinator.com/item?id=11109839) | Vulkan 图形技术正式公开发布。 | 903 | 201 | 2016-02-16 |
| 10 | [Microsoft, Google, Facebook Back Apple in Blocked Phone Case](https://news.ycombinator.com/item?id=11177200) | 微软、Google 与 Facebook 在手机解锁争议中支持 Apple。 | 888 | 240 | 2016-02-25 |
| 11 | [3D printed sundial whose precise holes cast a shadow displaying the current time](https://news.ycombinator.com/item?id=11094274) | 三维打印日晷通过精密孔洞投下阴影，直接显示当前时间。 | 839 | 92 | 2016-02-13 |
| 12 | [Dear Skype/Microsoft: Problems with Linux client](https://news.ycombinator.com/item?id=11165568) | 作者致信 Skype 与微软，指出 Linux 客户端存在的问题。 | 827 | 462 | 2016-02-24 |
| 13 | [Show HN: I've been writing daily TILs for a year](https://news.ycombinator.com/item?id=11068902) | 作者展示自己一年来每天记录“今日所学”的积累。 | 819 | 150 | 2016-02-09 |
| 14 | [GitHub is undergoing a full-blown overhaul as execs and employees depart](https://news.ycombinator.com/item?id=11049067) | 报道 GitHub 在高管与员工离职之际，正经历全面调整。 | 808 | 973 | 2016-02-06 |
| 15 | [Brooklyn Judge: Feds Can't Use All Writs Act to Force Apple's Hand [pdf]](https://news.ycombinator.com/item?id=11199169) | 布鲁克林一名法官裁定，政府不能借《所有令状法》强迫 Apple 配合。 | 797 | 188 | 2016-02-29 |
| 16 | [GitHub responds to Dear GitHub letter](https://news.ycombinator.com/item?id=11087191) | GitHub 回应《亲爱的 GitHub》公开信。 | 763 | 332 | 2016-02-12 |
| 17 | [Sci-Hub: Removing barriers in the way of science](https://news.ycombinator.com/item?id=11093779) | Sci-Hub 以消除科学获取障碍为目标提供服务。 | 760 | 217 | 2016-02-13 |
| 18 | [AI generated music to improve focus, relaxation and sleep](https://news.ycombinator.com/item?id=11146712) | 一项利用人工智能生成音乐、希望帮助专注、放松与睡眠的服务。 | 744 | 301 | 2016-02-21 |
| 19 | [Alphabet Becomes the Most Valuable Public Company in the World](https://news.ycombinator.com/item?id=11015596) | Alphabet 成为全球市值最高的上市公司。 | 720 | 419 | 2016-02-01 |
| 20 | [Spotify moves its back end to Google Cloud](https://news.ycombinator.com/item?id=11159840) | Spotify 宣布把后端基础设施迁往 Google Cloud。 | 715 | 381 | 2016-02-23 |

## 2016-03

有效主帖 24,454 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ubuntu on Windows](https://news.ycombinator.com/item?id=11390545) | 介绍在 Windows 上使用 Ubuntu 的新方案。 | 2049 | 901 | 2016-03-30 |
| 2 | [NPM and Left-Pad: Have We Forgotten How to Program?](https://news.ycombinator.com/item?id=11348798) | 从 npm 与 left-pad 事件出发，追问开发者是否过度依赖现成模块。 | 1725 | 854 | 2016-03-23 |
| 3 | [Responsive Pixel Art](https://news.ycombinator.com/item?id=11253649) | 展示能够响应布局变化的像素艺术。 | 1622 | 122 | 2016-03-09 |
| 4 | [We only hire the trendiest](https://news.ycombinator.com/item?id=11326940) | 作者以“我们只招最时髦的人”为题，反思技术招聘的偏好。 | 1615 | 716 | 2016-03-21 |
| 5 | [I've Just Liberated My Modules](https://news.ycombinator.com/item?id=11340510) | 一位模块作者宣布“解放”自己的代码模块。 | 1573 | 797 | 2016-03-22 |
| 6 | [Lee Sedol Beats AlphaGo in Game 4](https://news.ycombinator.com/item?id=11276798) | 李世石在第四局比赛中击败 AlphaGo。 | 1395 | 448 | 2016-03-13 |
| 7 | [Dsxyliea](https://news.ycombinator.com/item?id=11218677) | 一篇标题为“Dsxyliea”的作品，以经过扰动的文字形式呈现主题。 | 1356 | 200 | 2016-03-03 |
| 8 | [Announcing SQL Server on Linux](https://news.ycombinator.com/item?id=11241430) | 微软宣布将 SQL Server 带到 Linux。 | 1344 | 476 | 2016-03-07 |
| 9 | [Andy Grove has died](https://news.ycombinator.com/item?id=11333402) | Andy Grove 去世的消息。 | 1333 | 166 | 2016-03-22 |
| 10 | [He Always Had a Dark Side](https://news.ycombinator.com/item?id=11381625) | 一篇以“他一直都有阴暗面”为题的人物叙述。 | 1304 | 351 | 2016-03-29 |
| 11 | [Diffie and Hellman Win Turing Award](https://news.ycombinator.com/item?id=11204936) | Whitfield Diffie 与 Martin Hellman 获得图灵奖。 | 1272 | 78 | 2016-03-01 |
| 12 | [My Heroic and Lazy Stand Against IFTTT](https://news.ycombinator.com/item?id=11378278) | 作者讲述自己以“英勇又懒惰”的方式反对 IFTTT 的经历。 | 1236 | 208 | 2016-03-28 |
| 13 | [Ask HN: How much do you make at Amazon? Here is how much I make at Amazon](https://news.ycombinator.com/item?id=11312984) | 一位 Amazon 员工公开自己的薪酬，并邀请同事分享收入以改善谈薪信息差。 | 1213 | 690 | 2016-03-18 |
| 14 | [Publicly Funded Research Should Be Publicly Available](https://news.ycombinator.com/item?id=11380650) | EFF 主张，公共资金支持的研究成果应向公众开放。 | 1106 | 131 | 2016-03-29 |
| 15 | [AlphaGo beats the world champion Lee Sedol in first of five matches](https://news.ycombinator.com/item?id=11251463) | AlphaGo 在五局比赛的首局中击败围棋世界冠军李世石。 | 1085 | 573 | 2016-03-09 |
| 16 | [That awkward moment when Apple mocked good hardware and poor people](https://news.ycombinator.com/item?id=11343400) | 作者批评 Apple 的一次表态，认为它嘲弄了仍好用的硬件与经济拮据的人。 | 1078 | 567 | 2016-03-23 |
| 17 | [How to Pass a Programming Interview](https://news.ycombinator.com/item?id=11246917) | 分享准备和通过编程面试的方法。 | 1020 | 552 | 2016-03-08 |
| 18 | [Tell HN: AngelList told my employer that I'd updated my profile](https://news.ycombinator.com/item?id=11326011) | 用户称更新 AngelList 资料后，平台冒用其身份向雇主发邮件确认项目。 | 958 | 224 | 2016-03-21 |
| 19 | [Xamarin now free in Visual Studio, and Xamarin SDK being open-sourced](https://news.ycombinator.com/item?id=11398033) | Xamarin 在 Visual Studio 中免费提供，其 SDK 也将开源。 | 944 | 386 | 2016-03-31 |
| 20 | [I made my own clear plastic tooth aligners and they worked](https://news.ycombinator.com/item?id=11275925) | 作者自制透明牙齿矫正器，并称使用后取得了效果。 | 943 | 133 | 2016-03-13 |

## 2016-04

有效主帖 24,041 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [A Protocol for Dying](https://news.ycombinator.com/item?id=11547212) | 一篇关于面对死亡时如何安排与行动的个人文字。 | 1610 | 318 | 2016-04-22 |
| 2 | [Panama Papers: Mossack Fonseca leak reveals elite's tax havens](https://news.ycombinator.com/item?id=11416928) | “巴拿马文件”披露 Mossack Fonseca 资料，揭示精英使用避税天堂的情况。 | 1373 | 435 | 2016-04-03 |
| 3 | [My Biggest Regret as a Programmer](https://news.ycombinator.com/item?id=11436228) | 作者回顾自己作为程序员最大的遗憾。 | 1296 | 618 | 2016-04-06 |
| 4 | [Kite – Programming Copilot](https://news.ycombinator.com/item?id=11497111) | Kite 推出辅助编程的“副驾驶”工具。 | 1138 | 232 | 2016-04-14 |
| 5 | [Who's downloading pirated papers? Everyone](https://news.ycombinator.com/item?id=11593532) | 报道追问谁在下载盗版论文，并指出使用者分布广泛。 | 1085 | 381 | 2016-04-29 |
| 6 | [WhatsApp's Signal Protocol integration is now complete](https://news.ycombinator.com/item?id=11431108) | WhatsApp 宣布完成 Signal 协议的集成。 | 1055 | 376 | 2016-04-05 |
| 7 | [YouTube-dl: Open-source YouTube downloader](https://news.ycombinator.com/item?id=11452765) | youtube-dl 提供开源的 YouTube 视频下载工具。 | 989 | 321 | 2016-04-08 |
| 8 | [Visual Studio Code 1.0](https://news.ycombinator.com/item?id=11498000) | Visual Studio Code 发布 1.0 版本。 | 966 | 461 | 2016-04-14 |
| 9 | [Leaving Beta, New Sponsors](https://news.ycombinator.com/item?id=11480708) | 服务方宣布结束测试阶段，并介绍新的赞助者。 | 896 | 170 | 2016-04-12 |
| 10 | [Ask HN: Pick startups for YC to fund](https://news.ycombinator.com/item?id=11440627) | HN 邀请社区挑选创业公司，由 YC 提供资助。 | 867 | 286 | 2016-04-06 |
| 11 | [How I Hacked Facebook and Found Someone's Backdoor Script](https://news.ycombinator.com/item?id=11540747) | 研究者讲述攻入 Facebook 系统后，发现另一人留下后门脚本的过程。 | 865 | 124 | 2016-04-21 |
| 12 | [The average size of Web pages is now the average size of a Doom install](https://news.ycombinator.com/item?id=11548816) | 网页平均体积已与一份《Doom》安装文件相当。 | 857 | 449 | 2016-04-22 |
| 13 | [Tinker with a Neural Network in Your Browser](https://news.ycombinator.com/item?id=11483934) | 在浏览器中交互式调整神经网络，直接观察变化。 | 855 | 116 | 2016-04-12 |
| 14 | [Being a Developer After 40](https://news.ycombinator.com/item?id=11569726) | 作者分享四十岁之后继续做开发者的经历与思考。 | 854 | 549 | 2016-04-26 |
| 15 | [Show HN: I made an interactive Bootstrap 4 cheat sheet](https://news.ycombinator.com/item?id=11542005) | 展示一份可以交互查看的 Bootstrap 4 速查表。 | 847 | 161 | 2016-04-21 |
| 16 | [SpaceX Launch Livestream: CRS-8 Dragon Hosted Webcast](https://news.ycombinator.com/item?id=11457263) | 观看 SpaceX 的 CRS-8 龙飞船任务发射直播。 | 845 | 354 | 2016-04-08 |
| 17 | [Infinit announces Project Dropboxe](https://news.ycombinator.com/item?id=11594816) | Infinit 宣布名为 Dropboxe 的新项目。 | 830 | 134 | 2016-04-29 |
| 18 | [BYOT: Bring your own team](https://news.ycombinator.com/item?id=11567135) | 介绍“带上你自己的团队”这一做法。 | 826 | 180 | 2016-04-25 |
| 19 | [Save Netflix](https://news.ycombinator.com/item?id=11424372) | 一项以“拯救 Netflix”为主题的公开倡议。 | 813 | 225 | 2016-04-04 |
| 20 | [GitLab Pages](https://news.ycombinator.com/item?id=11430889) | GitLab 推出 Pages 服务。 | 812 | 291 | 2016-04-05 |

## 2016-05

有效主帖 23,721 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Jury in Oracle v. Google finds in Google's favour](https://news.ycombinator.com/item?id=11781053) | Oracle 诉 Google 一案的陪审团作出有利于 Google 的裁决。 | 1832 | 393 | 2016-05-26 |
| 2 | [How Technology Hijacks People’s Minds](https://news.ycombinator.com/item?id=11737232) | 探讨技术产品如何影响和操控人们的注意与思维。 | 1612 | 427 | 2016-05-20 |
| 3 | [Introducing unlimited private repositories](https://news.ycombinator.com/item?id=11673103) | GitHub 宣布提供数量不受限制的私有仓库。 | 1576 | 636 | 2016-05-11 |
| 4 | [Reverse Engineering a Mysterious UDP Stream in My Hotel](https://news.ycombinator.com/item?id=11744518) | 作者逆向分析酒店网络里一条神秘的 UDP 数据流。 | 1423 | 181 | 2016-05-21 |
| 5 | [Moving Forward on Basic Income](https://news.ycombinator.com/item?id=11807450) | Y Combinator 公布基本收入研究的后续进展。 | 1330 | 1448 | 2016-05-31 |
| 6 | [Apple Stole My Music](https://news.ycombinator.com/item?id=11634600) | 作者指责 Apple“偷走”了自己的音乐。 | 1259 | 446 | 2016-05-05 |
| 7 | [All European scientific publicly funded articles to be freely accessible by 2020](https://news.ycombinator.com/item?id=11787271) | 欧洲提出，到二〇二〇年让公共资金支持的科研论文免费开放。 | 1167 | 133 | 2016-05-27 |
| 8 | [Announcing SyntaxNet: The World’s Most Accurate Natural Language Parser](https://news.ycombinator.com/item?id=11686029) | Google 发布自然语言解析器 SyntaxNet，并称其准确率达到世界领先水平。 | 1083 | 235 | 2016-05-12 |
| 9 | [WhatsApp, Used by 100M Brazilians, Shut Down Nationwide Today by a Single Judge](https://news.ycombinator.com/item?id=11614116) | 巴西一名法官下令在全国停用 WhatsApp，影响约一亿用户。 | 972 | 608 | 2016-05-02 |
| 10 | [Did I just win?](https://news.ycombinator.com/item?id=11691798) | 作者以“我刚才是不是赢了”为题，提出一个带有惊讶的疑问。 | 950 | 129 | 2016-05-13 |
| 11 | [A cave in Romania that was sealed for 5.5M years](https://news.ycombinator.com/item?id=11682816) | 走进罗马尼亚一处封闭了五百五十万年的洞穴。 | 889 | 161 | 2016-05-12 |
| 12 | [The NYPD Was Ticketing Legally Parked Cars; Open Data Put an End to It](https://news.ycombinator.com/item?id=11680013) | 开放数据帮助发现并制止纽约警方对合法停放车辆开罚单的做法。 | 868 | 177 | 2016-05-11 |
| 13 | [Google supercharges machine learning tasks with TPU custom chip](https://news.ycombinator.com/item?id=11724763) | Google 用定制 TPU 芯片加速机器学习任务。 | 823 | 276 | 2016-05-18 |
| 14 | [SpaceX lands rocket at sea second time after satellite launch](https://news.ycombinator.com/item?id=11642855) | SpaceX 在卫星发射后，第二次成功于海上回收火箭。 | 814 | 474 | 2016-05-06 |
| 15 | [A Farewell to FRP](https://news.ycombinator.com/item?id=11667523) | Elm 团队宣布告别函数式响应式编程的相关表述与做法。 | 771 | 241 | 2016-05-10 |
| 16 | [E Ink announces a full color electrophoretic ePaper display](https://news.ycombinator.com/item?id=11766073) | E Ink 公布全彩电泳电子纸显示屏。 | 763 | 257 | 2016-05-24 |
| 17 | [The price of solar power just fell 50% in 16 months](https://news.ycombinator.com/item?id=11617988) | 报道太阳能电价在十六个月内下降了百分之五十。 | 756 | 435 | 2016-05-03 |
| 18 | [WebKit is now 100% ES6 complete](https://news.ycombinator.com/item?id=11708840) | WebKit 宣布已完整实现 ES6 支持。 | 755 | 109 | 2016-05-16 |
| 19 | [TTIP Leaks](https://news.ycombinator.com/item?id=11610162) | 查阅与 TTIP 有关的泄露文件。 | 752 | 251 | 2016-05-02 |
| 20 | [Pastejacking](https://news.ycombinator.com/item?id=11757973) | 介绍“粘贴劫持”攻击项目及其演示。 | 722 | 234 | 2016-05-24 |

## 2016-06

有效主帖 22,910 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [UK votes to leave EU](https://news.ycombinator.com/item?id=11966167) | 英国公投结果支持退出欧盟。 | 3125 | 2530 | 2016-06-24 |
| 2 | [Microsoft to acquire LinkedIn for $26B](https://news.ycombinator.com/item?id=11893153) | 微软宣布以约二百六十亿美元收购 LinkedIn。 | 2049 | 833 | 2016-06-13 |
| 3 | [Being sued, in East Texas, for using the Google Play Store [video]](https://news.ycombinator.com/item?id=11862476) | 一段视频讲述仅因使用 Google Play 商店而在得州东部遭起诉的经历。 | 1565 | 400 | 2016-06-08 |
| 4 | [Alan Kay has agreed to do an AMA today](https://news.ycombinator.com/item?id=11939851) | Alan Kay 同意在 HN 参加问答，与社区交流。 | 1401 | 893 | 2016-06-20 |
| 5 | [Defending Our Brand](https://news.ycombinator.com/item?id=11961034) | 服务方解释维护自身品牌的立场与行动。 | 1346 | 263 | 2016-06-23 |
| 6 | [The Daredevil Camera](https://news.ycombinator.com/item?id=12004866) | 一篇以“超胆侠相机”为题的文章，探索与相机有关的想法。 | 1302 | 153 | 2016-06-29 |
| 7 | [My First 10 Minutes on a Server](https://news.ycombinator.com/item?id=11909543) | 作者分享首次接手服务器后，最初十分钟会进行的操作。 | 1282 | 290 | 2016-06-15 |
| 8 | [How a comment on Hacker News led to 4½ new Unicode characters](https://news.ycombinator.com/item?id=11958682) | 一条 HN 评论如何最终推动增加四个半新的 Unicode 字符。 | 1181 | 413 | 2016-06-23 |
| 9 | [Apple File System](https://news.ycombinator.com/item?id=11896785) | 介绍 Apple File System 文件系统。 | 1094 | 393 | 2016-06-13 |
| 10 | [VPAID ads destroy performance and are still served by major ad networks](https://news.ycombinator.com/item?id=11900453) | 作者批评 VPAID 广告破坏页面性能，而大型广告网络仍在投放。 | 1045 | 392 | 2016-06-14 |
| 11 | [“PayPal has demanded that we monitor data traffic as well as customers’ files”](https://news.ycombinator.com/item?id=11944011) | 一家公司称，PayPal 要求其监控数据流量与客户文件。 | 1030 | 340 | 2016-06-21 |
| 12 | [The “Cobra Effect” that is disabling paste on password fields](https://news.ycombinator.com/item?id=11979492) | 禁用密码框粘贴为何可能产生适得其反的“眼镜蛇效应”？ | 911 | 442 | 2016-06-26 |
| 13 | [New Cities](https://news.ycombinator.com/item?id=11987032) | Y Combinator 公布以新城市为主题的项目。 | 889 | 695 | 2016-06-27 |
| 14 | [Spaceship Generator](https://news.ycombinator.com/item?id=11929493) | 展示一个可以生成宇宙飞船的程序项目。 | 850 | 128 | 2016-06-18 |
| 15 | [Show HN: New calendar app idea](https://news.ycombinator.com/item?id=11846108) | 作者展示一个新的日历应用构想。 | 825 | 197 | 2016-06-06 |
| 16 | [A Grain of Salt](https://news.ycombinator.com/item?id=11874575) | 一篇以“持保留态度”为题的文章，提醒读者审慎看待相关说法。 | 803 | 283 | 2016-06-10 |
| 17 | [Jessica Livingston’s Pretty Complete List on How Not to Fail](https://news.ycombinator.com/item?id=11870062) | Jessica Livingston 整理关于创业如何避免失败的建议。 | 795 | 192 | 2016-06-09 |
| 18 | [Samsung Acquires Joyent](https://news.ycombinator.com/item?id=11913652) | Samsung 宣布收购 Joyent。 | 787 | 236 | 2016-06-16 |
| 19 | [ASUS delivers BIOS/UEFI auto-updates over HTTP with no verification](https://news.ycombinator.com/item?id=11840342) | ASUS 被指通过未加密的 HTTP 分发 BIOS 与 UEFI 自动更新，且缺少验证。 | 762 | 196 | 2016-06-05 |
| 20 | [Show HN: I made a database of remote companies](https://news.ycombinator.com/item?id=11890991) | 作者整理了一份实行远程工作的公司数据库。 | 747 | 114 | 2016-06-13 |

## 2016-07

有效主帖 21,405 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: New features and a moderator](https://news.ycombinator.com/item?id=12073675) | HN 推出评论折叠、撤销投票与收藏等新功能，并介绍一位新版主。 | 2381 | 451 | 2016-07-11 |
| 2 | [Why I’m Suing the US Government](https://news.ycombinator.com/item?id=12136578) | 作者解释自己为何起诉美国政府。 | 1855 | 307 | 2016-07-21 |
| 3 | [Master Plan, Part Deux](https://news.ycombinator.com/item?id=12133766) | Tesla 公布“宏伟蓝图”的第二部分。 | 1851 | 677 | 2016-07-21 |
| 4 | [Show HN: Web Design in 4 minutes](https://news.ycombinator.com/item?id=12166687) | 通过四分钟的演示，理解网页设计的基本步骤。 | 1624 | 152 | 2016-07-26 |
| 5 | [Sega Saturn CD Cracked after 20 Years](https://news.ycombinator.com/item?id=12074096) | Sega Saturn 光盘保护在二十年后被破解。 | 1126 | 223 | 2016-07-11 |
| 6 | [LastPass autofill exploit](https://news.ycombinator.com/item?id=12171547) | 研究者披露针对 LastPass 自动填充功能的漏洞利用方式。 | 1008 | 420 | 2016-07-27 |
| 7 | [Mental Models I Find Repeatedly Useful](https://news.ycombinator.com/item?id=12040707) | 作者整理一些自己反复发现有用的思维模型。 | 929 | 189 | 2016-07-06 |
| 8 | [We Should Not Accept Scientific Results That Have Not Been Repeated](https://news.ycombinator.com/item?id=12185845) | 作者主张，未经重复验证的科学结果不应被直接接受。 | 910 | 275 | 2016-07-29 |
| 9 | [A practical security guide for web developers](https://news.ycombinator.com/item?id=12140477) | 面向网页开发者的实用安全指南。 | 894 | 68 | 2016-07-21 |
| 10 | [Stack Overflow Outage Postmortem](https://news.ycombinator.com/item?id=12131909) | Stack Overflow 发布一次服务中断的事后复盘。 | 862 | 316 | 2016-07-20 |
| 11 | [Pokemon Go is a huge security risk](https://news.ycombinator.com/item?id=12071098) | 作者认为，《Pokémon Go》带来了严重的安全风险。 | 780 | 251 | 2016-07-11 |
| 12 | [I got arrested in Kazakhstan and represented myself in court](https://news.ycombinator.com/item?id=12138523) | 作者讲述自己在哈萨克斯坦被捕后，出庭为自己辩护的经历。 | 779 | 239 | 2016-07-21 |
| 13 | [Create React Apps with No Configuration](https://news.ycombinator.com/item?id=12144371) | 介绍无需手动配置即可创建 React 应用的工具。 | 777 | 241 | 2016-07-22 |
| 14 | [Shipping Rust code in Firefox](https://news.ycombinator.com/item?id=12078702) | Firefox 开始交付包含 Rust 代码的版本。 | 748 | 189 | 2016-07-12 |
| 15 | [Why Uber Engineering Switched from Postgres to MySQL](https://news.ycombinator.com/item?id=12166585) | Uber 工程团队解释为何从 PostgreSQL 转向 MySQL。 | 731 | 294 | 2016-07-26 |
| 16 | [Don't add your 2 cents](https://news.ycombinator.com/item?id=12156234) | 作者建议克制随手发表个人意见的冲动。 | 719 | 237 | 2016-07-25 |
| 17 | [The Fight for the “Right to Repair”](https://news.ycombinator.com/item?id=12088631) | 关注为保障消费者“维修权”而进行的努力。 | 704 | 318 | 2016-07-13 |
| 18 | [Apollo 11 Guidance Computer source code](https://news.ycombinator.com/item?id=12048945) | 查阅 Apollo 11 制导计算机的源代码。 | 652 | 145 | 2016-07-07 |
| 19 | [Mr Robot S02E01 easter egg](https://news.ycombinator.com/item?id=12101036) | 发现《黑客军团》第二季第一集中的隐藏彩蛋。 | 639 | 194 | 2016-07-15 |
| 20 | [Home Computers Connected to the Internet Aren't Private, Court Rules](https://news.ycombinator.com/item?id=12015388) | 一项法院裁决涉及联网家用电脑是否享有隐私保护。 | 636 | 334 | 2016-07-01 |

## 2016-08

有效主帖 23,669 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [“It's The Future”](https://news.ycombinator.com/item?id=12303075) | 一篇以“这就是未来”为题的技术文章。 | 1323 | 521 | 2016-08-17 |
| 2 | [The Dropbox hack is real](https://news.ycombinator.com/item?id=12396331) | 研究者确认 Dropbox 遭入侵的相关数据具有真实性。 | 1313 | 539 | 2016-08-31 |
| 3 | [Scammed By A Silicon Valley Startup](https://news.ycombinator.com/item?id=12379518) | 作者讲述自己被一家硅谷创业公司欺骗的经历。 | 1311 | 558 | 2016-08-29 |
| 4 | [Why we lost Uber as a user](https://news.ycombinator.com/item?id=12201353) | PostgreSQL 社区成员分析为何失去 Uber 这个用户。 | 1234 | 285 | 2016-08-01 |
| 5 | [PowerShell is open sourced and is available on Linux](https://news.ycombinator.com/item?id=12313179) | PowerShell 宣布开源，并提供 Linux 版本。 | 1217 | 760 | 2016-08-18 |
| 6 | [Massachusetts Bans Employers from Asking Applicants About Previous Pay](https://news.ycombinator.com/item?id=12211651) | 马萨诸塞州禁止雇主向求职者询问此前的薪资。 | 1195 | 760 | 2016-08-02 |
| 7 | [Planet Found in Habitable Zone Around Nearest Star](https://news.ycombinator.com/item?id=12353441) | 距离太阳最近的恒星周围，发现一颗位于宜居带的行星。 | 1187 | 427 | 2016-08-24 |
| 8 | [NSO Group's iPhone Zero-Days used against a UAE Human Rights Defender](https://news.ycombinator.com/item?id=12360662) | NSO Group 的 iPhone 零日漏洞被用于攻击一名阿联酋人权活动人士。 | 1055 | 242 | 2016-08-25 |
| 9 | [Show HN: Generating fantasy maps – an interactive exploration](https://news.ycombinator.com/item?id=12260794) | 通过交互式探索，学习如何生成虚构世界的地图。 | 1004 | 64 | 2016-08-10 |
| 10 | [Indie Hackers: Learn how developers are making money](https://news.ycombinator.com/item?id=12269425) | Indie Hackers 汇集开发者赚钱的故事，分享独立经营经验。 | 971 | 184 | 2016-08-11 |
| 11 | [Japanese writing system basics](https://news.ycombinator.com/item?id=12324358) | 介绍日语书写体系的基础知识。 | 961 | 338 | 2016-08-20 |
| 12 | [Zero-cost futures in Rust](https://news.ycombinator.com/item?id=12268988) | 介绍 Rust 中强调零成本抽象的 Future 方案。 | 930 | 337 | 2016-08-11 |
| 13 | [Justice Department says it will end use of private prisons](https://news.ycombinator.com/item?id=12313304) | 美国司法部表示将停止使用私人监狱。 | 859 | 358 | 2016-08-18 |
| 14 | [Web Scraping in 2016](https://news.ycombinator.com/item?id=12345693) | 从二〇一六年的实践出发，讨论网页抓取的方法。 | 852 | 387 | 2016-08-23 |
| 15 | [This JPEG is also a webpage](https://news.ycombinator.com/item?id=12262470) | 展示一个既是 JPEG 图片、同时也是网页的文件。 | 833 | 226 | 2016-08-10 |
| 16 | [The Cuban CDN](https://news.ycombinator.com/item?id=12319063) | 介绍被称为“古巴 CDN”的内容分发方式。 | 832 | 136 | 2016-08-19 |
| 17 | [Seymour Papert has died](https://news.ycombinator.com/item?id=12201810) | Seymour Papert 去世的消息。 | 820 | 137 | 2016-08-01 |
| 18 | [Smaller and faster data compression with Zstandard](https://news.ycombinator.com/item?id=12399804) | Zstandard 提供更小压缩体积与更快速度的数据压缩方案。 | 819 | 156 | 2016-08-31 |
| 19 | [Nasa just made all its research available online for free](https://news.ycombinator.com/item?id=12327225) | 报道 NASA 开始将研究成果免费发布到网上。 | 776 | 49 | 2016-08-20 |
| 20 | [What Makes a McMansion Bad Architecture?](https://news.ycombinator.com/item?id=12286724) | 为什么所谓的 McMansion 会被视为糟糕的建筑设计？ | 758 | 519 | 2016-08-14 |

## 2016-09

有效主帖 23,176 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Pardon Snowden](https://news.ycombinator.com/item?id=12494998) | 一项呼吁赦免 Edward Snowden 的公众行动。 | 2553 | 781 | 2016-09-14 |
| 2 | [Making Humans a Multiplanetary Species [video]](https://news.ycombinator.com/item?id=12591617) | 一段讨论如何让人类成为跨行星物种的演讲。 | 2123 | 1046 | 2016-09-27 |
| 3 | [Philae Found](https://news.ycombinator.com/item?id=12430298) | Philae 彗星着陆器的位置被找到。 | 1238 | 125 | 2016-09-05 |
| 4 | [Show HN: Wave function collapse algorithm](https://news.ycombinator.com/item?id=12612246) | 展示名为“波函数坍缩”的算法项目。 | 1226 | 122 | 2016-09-30 |
| 5 | [EU Announces That All Scientific Articles Should Be Freely Accessible by 2020](https://news.ycombinator.com/item?id=12435236) | 欧盟宣布，希望到二〇二〇年让科学论文可以免费获取。 | 1205 | 132 | 2016-09-06 |
| 6 | [Announcing new tools, forums, and features](https://news.ycombinator.com/item?id=12499642) | GitHub 公布新的工具、论坛与功能。 | 1142 | 269 | 2016-09-14 |
| 7 | [Elon Musk on How to Build the Future](https://news.ycombinator.com/item?id=12508356) | Elon Musk 分享他对如何建设未来的看法。 | 1106 | 513 | 2016-09-15 |
| 8 | [Linux can’t be installed on a recent Lenovo laptop](https://news.ycombinator.com/item?id=12545878) | 有用户报告，某款近期的 Lenovo 笔记本无法安装 Linux。 | 1054 | 467 | 2016-09-21 |
| 9 | [How Dropbox Hacks Your Mac](https://news.ycombinator.com/item?id=12463338) | 作者分析 Dropbox 在 Mac 上采取的系统操作，并提出安全质疑。 | 1037 | 412 | 2016-09-09 |
| 10 | [A SpaceX Falcon 9 rocket has exploded at Cape Canaveral](https://news.ycombinator.com/item?id=12405006) | SpaceX 一枚 Falcon 9 火箭在卡纳维拉尔角发生爆炸。 | 986 | 535 | 2016-09-01 |
| 11 | [You Suck at Excel with Joel Spolsky (2015) [video]](https://news.ycombinator.com/item?id=12448545) | 观看 Joel Spolsky 以“你还不擅长 Excel”为题的教学视频。 | 957 | 420 | 2016-09-07 |
| 12 | [Homebrew 1.0.0](https://news.ycombinator.com/item?id=12546542) | Homebrew 发布 1.0.0 版本。 | 904 | 246 | 2016-09-21 |
| 13 | [Show HN: Primitive Pictures](https://news.ycombinator.com/item?id=12539109) | 展示名为 Primitive Pictures 的图像项目。 | 894 | 170 | 2016-09-20 |
| 14 | [Canadian surgeons urge people to throw out bristle BBQ brushes](https://news.ycombinator.com/item?id=12409425) | 加拿大外科医生呼吁丢弃钢丝烧烤刷，提醒公众注意其风险。 | 853 | 339 | 2016-09-01 |
| 15 | [I’m Joining Stripe to Work on Atlas](https://news.ycombinator.com/item?id=12464647) | 作者宣布加入 Stripe，参与 Atlas 项目。 | 850 | 317 | 2016-09-09 |
| 16 | [Angular 2 Final Released](https://news.ycombinator.com/item?id=12502947) | Angular 2 正式版发布。 | 838 | 431 | 2016-09-15 |
| 17 | [I gave commit rights to someone I didn't know](https://news.ycombinator.com/item?id=12522654) | 作者讲述把代码提交权限交给一位不认识的人的经历。 | 833 | 100 | 2016-09-17 |
| 18 | [An account of a serious medical emergency on a transoceanic flight](https://news.ycombinator.com/item?id=12417290) | 记录一次跨洋航班上发生的严重医疗紧急事件。 | 832 | 288 | 2016-09-03 |
| 19 | [Ask HN: Is web programming a series of hacks on hacks?](https://news.ycombinator.com/item?id=12477190) | 一位开发者求问，网页编程是否是不断在补丁上叠加补丁？ | 822 | 661 | 2016-09-12 |
| 20 | [How the Sugar Industry Shifted Blame to Fat](https://news.ycombinator.com/item?id=12480733) | 报道糖业如何把健康责任转移到脂肪身上。 | 816 | 599 | 2016-09-12 |

## 2016-10

有效主帖 24,056 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Be Kind](https://news.ycombinator.com/item?id=12707606) | 作者倡导以善意待人，讨论这种选择的意义。 | 2475 | 434 | 2016-10-14 |
| 2 | [Google's “Director of Engineering” Hiring Test](https://news.ycombinator.com/item?id=12701272) | 介绍 Google 对“工程总监”岗位采用的招聘测试。 | 1764 | 923 | 2016-10-13 |
| 3 | [Yarn – A new package manager for JavaScript](https://news.ycombinator.com/item?id=12684980) | Yarn 推出一款新的 JavaScript 包管理器。 | 1714 | 469 | 2016-10-11 |
| 4 | [RethinkDB is shutting down](https://news.ycombinator.com/item?id=12649414) | RethinkDB 团队宣布关闭运营。 | 1674 | 441 | 2016-10-06 |
| 5 | [DDoS Attack Against Dyn Managed DNS](https://news.ycombinator.com/item?id=12759697) | Dyn 托管 DNS 服务遭到 DDoS 攻击。 | 1563 | 674 | 2016-10-21 |
| 6 | [All Tesla Cars Being Produced Now Have Full Self-Driving Hardware](https://news.ycombinator.com/item?id=12748863) | Tesla 宣布，其当前生产的所有汽车均配备支持完全自动驾驶的硬件。 | 1493 | 1090 | 2016-10-20 |
| 7 | [Open Guide to Amazon Web Services](https://news.ycombinator.com/item?id=12686763) | 一份开放协作的 Amazon Web Services 使用指南。 | 1362 | 127 | 2016-10-11 |
| 8 | [I'm choosing euthanasia etd 1pm. I have no last words.](https://news.ycombinator.com/item?id=12634590) | 作者宣布选择安乐死，预计下午一点进行，并表示没有遗言。 | 1361 | 277 | 2016-10-04 |
| 9 | [Yahoo scanned customer emails for US intelligence](https://news.ycombinator.com/item?id=12637126) | 报道 Yahoo 曾为美国情报机构扫描用户电子邮件。 | 1346 | 395 | 2016-10-04 |
| 10 | [Shame on Y Combinator](https://news.ycombinator.com/item?id=12733024) | 作者以“Y Combinator 应当羞愧”为题，公开批评其做法。 | 1280 | 1321 | 2016-10-18 |
| 11 | [Google Noto Fonts](https://news.ycombinator.com/item?id=12654499) | Google 发布 Noto 字体系列。 | 1217 | 304 | 2016-10-06 |
| 12 | [Why you should never use Upwork](https://news.ycombinator.com/item?id=12773282) | 作者解释为何强烈建议不要使用 Upwork。 | 1175 | 264 | 2016-10-23 |
| 13 | [The Dutch Reach: Clever Workaround to Keep Cyclists from Getting “Doored”](https://news.ycombinator.com/item?id=12674533) | 介绍“荷兰式开门法”，帮助避免车门突然打开撞到骑车人。 | 1149 | 590 | 2016-10-10 |
| 14 | [Ask HN: What is your favorite YouTube channel for developers?](https://news.ycombinator.com/item?id=12702651) | HN 用户推荐适合开发者学习编程技术与实践的 YouTube 频道。 | 1081 | 171 | 2016-10-13 |
| 15 | [Thank HN: From Google form to $1k in revenue in one month](https://news.ycombinator.com/item?id=12748208) | 作者感谢 HN，分享从一个 Google 表单到一个月赚取一千美元的经历。 | 1071 | 247 | 2016-10-19 |
| 16 | [Eve: Programming designed for humans](https://news.ycombinator.com/item?id=12817468) | Eve 以“为人类设计的编程”为理念介绍自身方案。 | 1070 | 374 | 2016-10-28 |
| 17 | [Apple Has Removed Dash from the App Store](https://news.ycombinator.com/item?id=12646919) | 开发者表示，Apple 已将 Dash 从 App Store 下架。 | 1036 | 470 | 2016-10-05 |
| 18 | [Ask HN: What is your favorite internet rabbit hole?](https://news.ycombinator.com/item?id=12778836) | HN 用户分享那些越查越深入、让人停不下来的网络话题。 | 1036 | 454 | 2016-10-24 |
| 19 | [Programming books you might want to consider reading](https://news.ycombinator.com/item?id=12718102) | 推荐一些值得考虑阅读的编程书籍。 | 1019 | 131 | 2016-10-16 |
| 20 | [Music Theory: An Education from First Principles](https://news.ycombinator.com/item?id=12792063) | 从基本原理出发学习乐理。 | 955 | 148 | 2016-10-25 |

## 2016-11

有效主帖 24,300 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Donald Trump is the president-elect of the U.S.](https://news.ycombinator.com/item?id=12907201) | Donald Trump 当选美国总统。 | 1817 | 2215 | 2016-11-09 |
| 2 | [Dear Google, Apple, Mozilla, and MS: Please End Auto-Playing Media in Browsers](https://news.ycombinator.com/item?id=12942465) | 发帖者呼吁主要浏览器厂商停止默认自动播放音频与视频。 | 1358 | 318 | 2016-11-13 |
| 3 | [Diamonds Suck (2006)](https://news.ycombinator.com/item?id=12944464) | 一篇强烈批评钻石的文章，挑战围绕钻石的价值观念。 | 1336 | 576 | 2016-11-13 |
| 4 | [Advanced Data Structures](https://news.ycombinator.com/item?id=12871234) | 学习高级数据结构的课程资料。 | 1276 | 141 | 2016-11-04 |
| 5 | [H.264 is Magic](https://news.ycombinator.com/item?id=12871403) | 探究 H.264 视频技术为何会产生近乎魔法般的效果。 | 1228 | 219 | 2016-11-04 |
| 6 | [A Method I’ve Used to Eliminate Bad Tech Hires](https://news.ycombinator.com/item?id=12915809) | 作者分享自己用于避免技术招聘失误的一种方法。 | 1214 | 499 | 2016-11-09 |
| 7 | [“I have toyota corola”](https://news.ycombinator.com/item?id=12949114) | 一篇以“我有一辆丰田 Corolla”为题的个人文章。 | 1155 | 350 | 2016-11-14 |
| 8 | [Amazon LightSail: Simple Virtual Private Servers on AWS](https://news.ycombinator.com/item?id=13072155) | Amazon Lightsail 在 AWS 上提供简化的虚拟私人服务器服务。 | 1142 | 614 | 2016-11-30 |
| 9 | [Quit Social Media, Your Career May Depend on It](https://news.ycombinator.com/item?id=12998698) | 作者主张退出社交媒体，并认为这可能有利于职业发展。 | 1131 | 548 | 2016-11-20 |
| 10 | [Show HN: A visual guide to the most popular CSS properties](https://news.ycombinator.com/item?id=13031492) | 展示一份通过视觉示例讲解常用 CSS 属性的指南。 | 1117 | 122 | 2016-11-24 |
| 11 | [Logojoy: AI-powered logo creator](https://news.ycombinator.com/item?id=13065015) | Logojoy 利用人工智能帮助用户创建标志。 | 1113 | 329 | 2016-11-29 |
| 12 | [SpaceX plans worldwide satellite Internet with low latency, gigabit speed](https://news.ycombinator.com/item?id=12982418) | SpaceX 规划覆盖全球的卫星互联网，目标是低延迟与千兆速度。 | 1111 | 521 | 2016-11-17 |
| 13 | [Ask HN: Who is firing?](https://news.ycombinator.com/item?id=12851987) | 经历公司管理失误后，发帖者邀请社区讨论哪些公司正在裁员或流失员工。 | 1087 | 432 | 2016-11-02 |
| 14 | [Quick, Draw](https://news.ycombinator.com/item?id=12965311) | 体验 Google 的 Quick, Draw 绘画项目。 | 1083 | 328 | 2016-11-16 |
| 15 | [Don’t Mess with The Google](https://news.ycombinator.com/item?id=12972554) | 作者以“别惹 Google”为题，讲述与该公司有关的问题。 | 1070 | 496 | 2016-11-16 |
| 16 | [Leonard Cohen Has Died](https://news.ycombinator.com/item?id=12926684) | 音乐人 Leonard Cohen 去世。 | 978 | 140 | 2016-11-11 |
| 17 | [DeepMind and Blizzard to release StarCraft II as an AI research environment](https://news.ycombinator.com/item?id=12874798) | DeepMind 与 Blizzard 将把《星际争霸 II》开放为人工智能研究环境。 | 917 | 329 | 2016-11-04 |
| 18 | [Pornhub Bypasses Ad Blockers with WebSockets](https://news.ycombinator.com/item?id=12854877) | Pornhub 被发现利用 WebSocket 绕过广告拦截工具。 | 873 | 575 | 2016-11-02 |
| 19 | [Matrix Multiplication](https://news.ycombinator.com/item?id=13036386) | 通过网页演示理解矩阵乘法。 | 873 | 131 | 2016-11-25 |
| 20 | [Epic Games chief pays $15M to protect 7,000 acres of North Carolina wilderness](https://news.ycombinator.com/item?id=12913112) | Epic Games 负责人出资一千五百万美元，保护北卡罗来纳州七千英亩荒野。 | 845 | 176 | 2016-11-09 |

## 2016-12

有效主帖 23,971 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Political Detox Week – No politics on HN for one week](https://news.ycombinator.com/item?id=13108404) | HN 试行一周“政治排毒”，暂时将政治新闻与相关讨论列为离题内容。 | 1630 | 1214 | 2016-12-05 |
| 2 | [Amazon Go](https://news.ycombinator.com/item?id=13105689) | Amazon 公布名为 Go 的项目。 | 1247 | 982 | 2016-12-05 |
| 3 | [Building Jarvis](https://news.ycombinator.com/item?id=13212976) | 作者介绍打造 Jarvis 的过程。 | 1164 | 251 | 2016-12-19 |
| 4 | [Cat-proofing a cat feeding machine](https://news.ycombinator.com/item?id=13230904) | 改造自动喂猫器，防止猫钻机器的空子。 | 1107 | 289 | 2016-12-21 |
| 5 | [Developers’ side projects](https://news.ycombinator.com/item?id=13142327) | 围绕开发者的业余项目，讨论个人创作与工作之间的关系。 | 1052 | 389 | 2016-12-09 |
| 6 | [Yahoo discloses hack of 1B accounts](https://news.ycombinator.com/item?id=13180033) | Yahoo 披露一次影响十亿账户的入侵事件。 | 1046 | 569 | 2016-12-14 |
| 7 | [OpenAI Universe](https://news.ycombinator.com/item?id=13103742) | OpenAI 推出名为 Universe 的项目。 | 1021 | 129 | 2016-12-05 |
| 8 | [Yahoo installed a backdoor for the NSA behind the back of the security team](https://news.ycombinator.com/item?id=13182120) | 报道 Yahoo 绕过自身安全团队，为 NSA 安装后门。 | 1009 | 280 | 2016-12-15 |
| 9 | [Launchaco – Instantly generate a responsive, free, website](https://news.ycombinator.com/item?id=13126228) | Launchaco 帮助用户即时生成免费的响应式网站。 | 929 | 164 | 2016-12-07 |
| 10 | [How the Singapore Circle Line rogue train was caught with data](https://news.ycombinator.com/item?id=13078124) | 利用数据分析，找出造成新加坡环线问题的一列异常列车。 | 921 | 110 | 2016-12-01 |
| 11 | [Crypto 101 – Introductory course on cryptography](https://news.ycombinator.com/item?id=13089489) | Crypto 101 提供密码学入门课程。 | 919 | 140 | 2016-12-02 |
| 12 | ['Clean your desk': My Amazon interview experience](https://news.ycombinator.com/item?id=13130865) | 作者以“清理你的桌面”为切口，回顾一次 Amazon 面试经历。 | 911 | 510 | 2016-12-08 |
| 13 | [Things You Notice When You Quit the News](https://news.ycombinator.com/item?id=13153539) | 作者分享停止追新闻后，自己注意到的变化。 | 891 | 487 | 2016-12-11 |
| 14 | [Superintelligence: The Idea That Eats Smart People](https://news.ycombinator.com/item?id=13240811) | 作者批评“超级智能”观念，认为它会让聪明人陷入其中。 | 883 | 580 | 2016-12-22 |
| 15 | [Google says it will run entirely on renewable energy in 2017](https://news.ycombinator.com/item?id=13114803) | Google 表示，计划于二〇一七年完全使用可再生能源。 | 861 | 249 | 2016-12-06 |
| 16 | [Bose Hearphones](https://news.ycombinator.com/item?id=13139978) | Bose 介绍 Hearphones 产品。 | 830 | 407 | 2016-12-09 |
| 17 | [Uber Now Tracks Passengers’ Locations Even After They’re Dropped Off](https://news.ycombinator.com/item?id=13085098) | 报道 Uber 即使在乘客下车后，仍继续追踪其位置。 | 812 | 481 | 2016-12-02 |
| 18 | [John Glenn has died](https://news.ycombinator.com/item?id=13133954) | John Glenn 去世的消息。 | 797 | 152 | 2016-12-08 |
| 19 | [I am not a self-made man](https://news.ycombinator.com/item?id=13137741) | 作者强调自己的成就离不开他人帮助，并非全靠白手起家。 | 785 | 261 | 2016-12-09 |
| 20 | [Waymo: Google's self-driving car company](https://news.ycombinator.com/item?id=13168888) | Waymo 公开亮相，作为 Google 的自动驾驶汽车公司开展业务。 | 785 | 748 | 2016-12-13 |

## 2017-01

有效主帖 25,487 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Atlassian acquires Trello for $425M](https://news.ycombinator.com/item?id=13356318) | Atlassian 宣布以四点二五亿美元收购 Trello。 | 1857 | 733 | 2017-01-09 |
| 2 | [Welcome, ACLU](https://news.ycombinator.com/item?id=13531707) | Y Combinator 发布欢迎美国公民自由联盟 ACLU 的公告。 | 1558 | 1030 | 2017-01-31 |
| 3 | [Obama Commutes Bulk of Chelsea Manning’s Sentence](https://news.ycombinator.com/item?id=13421298) | Obama 减免 Chelsea Manning 的大部分剩余刑期。 | 1503 | 713 | 2017-01-17 |
| 4 | [Grumpy: Go running Python](https://news.ycombinator.com/item?id=13319904) | Grumpy 探索用 Go 运行 Python 代码。 | 1411 | 451 | 2017-01-04 |
| 5 | [What I Wish I'd Known About Equity Before Joining a Unicorn](https://news.ycombinator.com/item?id=13426494) | 作者回顾加入独角兽公司前，希望自己已经了解的股权知识。 | 1382 | 558 | 2017-01-18 |
| 6 | [WhatsApp backdoor allows snooping on encrypted messages](https://news.ycombinator.com/item?id=13389935) | 报道声称 WhatsApp 存在可让加密消息被窥探的后门。 | 1332 | 321 | 2017-01-13 |
| 7 | [LibreTaxi – A free and open source alternative to Uber and Lyft](https://news.ycombinator.com/item?id=13529213) | LibreTaxi 提供免费开源的 Uber 与 Lyft 替代方案。 | 1275 | 382 | 2017-01-31 |
| 8 | [Show HN: Privacy-focused, ad-free, non-tracking torrent search engine](https://news.ycombinator.com/item?id=13423629) | 展示一个强调隐私、无广告且不追踪用户的种子搜索引擎。 | 1183 | 346 | 2017-01-18 |
| 9 | [Show HN: Alacritty, a GPU-accelerated terminal emulator written in Rust](https://news.ycombinator.com/item?id=13338592) | Alacritty 是用 Rust 编写、利用 GPU 加速的终端模拟器。 | 1170 | 476 | 2017-01-06 |
| 10 | [Time to Take a Stand](https://news.ycombinator.com/item?id=13507993) | 作者以“是时候表明立场了”为题，呼吁采取行动。 | 1131 | 992 | 2017-01-28 |
| 11 | [There is no WhatsApp 'backdoor'](https://news.ycombinator.com/item?id=13394900) | Signal 协议团队反驳有关 WhatsApp 存在后门的说法。 | 1018 | 408 | 2017-01-13 |
| 12 | [VR](https://news.ycombinator.com/item?id=13392885) | Y Combinator 围绕虚拟现实发布文章。 | 1008 | 550 | 2017-01-13 |
| 13 | [First they came for the Iranians](https://news.ycombinator.com/item?id=13489156) | 作者借用“他们首先针对伊朗人”的表达，发出有关歧视与排斥的警示。 | 1000 | 429 | 2017-01-26 |
| 14 | [I Had My Electronics Seized by U.S. Customs and Border Protection](https://news.ycombinator.com/item?id=13453189) | 作者讲述自己的电子设备被美国海关与边境保护局扣押的经历。 | 951 | 593 | 2017-01-22 |
| 15 | [RethinkDB Postmortem](https://news.ycombinator.com/item?id=13421608) | 复盘 RethinkDB 失败的经过。 | 948 | 267 | 2017-01-17 |
| 16 | [Chrome 56 will mark HTTP pages with password fields as non-secure](https://news.ycombinator.com/item?id=13456246) | Chrome 56 将把含密码输入框的 HTTP 页面标记为不安全。 | 947 | 398 | 2017-01-22 |
| 17 | [Naughty Strings: A list of strings likely to cause issues as user-input data](https://news.ycombinator.com/item?id=13406119) | 收集容易让程序出问题的输入字符串，供测试与排错使用。 | 937 | 144 | 2017-01-15 |
| 18 | [I Turned a Routine Traffic Ticket into a Constitutional Trial](https://news.ycombinator.com/item?id=13397145) | 作者讲述如何把一张普通交通罚单变成涉及宪法的审判。 | 899 | 467 | 2017-01-14 |
| 19 | [Wine 2.0 released](https://news.ycombinator.com/item?id=13475172) | Wine 发布 2.0 版本。 | 896 | 303 | 2017-01-24 |
| 20 | [Google Has Started Penalizing Mobile Websites with Intrusive Pop-Up Ads](https://news.ycombinator.com/item?id=13439828) | Google 开始惩罚使用侵入式弹出广告的移动网站。 | 880 | 386 | 2017-01-19 |

## 2017-02

有效主帖 23,668 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Reflecting on one very, very strange year at Uber](https://news.ycombinator.com/item?id=13682022) | 作者回顾自己在 Uber 度过的极不寻常的一年。 | 4107 | 1013 | 2017-02-19 |
| 2 | [Cloudflare Reverse Proxies Are Dumping Uninitialized Memory](https://news.ycombinator.com/item?id=13718752) | 披露 Cloudflare 反向代理泄露未初始化内存内容的安全问题。 | 3238 | 992 | 2017-02-23 |
| 3 | [Announcing the first SHA-1 collision](https://news.ycombinator.com/item?id=13713480) | 研究者宣布实现首个 SHA-1 哈希碰撞。 | 3030 | 485 | 2017-02-23 |
| 4 | [Ask HN: Is S3 down?](https://news.ycombinator.com/item?id=13755673) | 用户在 AWS 控制台查看 S3 时收到内部错误，询问服务是否宕机。 | 2589 | 1055 | 2017-02-28 |
| 5 | [Seven earth-sized planets discovered circling a star 39 light years from Earth](https://news.ycombinator.com/item?id=13707547) | 距地球三十九光年的一颗恒星周围，发现七颗地球大小的行星。 | 2256 | 704 | 2017-02-22 |
| 6 | [I am an Uber survivor](https://news.ycombinator.com/item?id=13747414) | 作者以“我是 Uber 的幸存者”为题，讲述自己的经历。 | 2168 | 767 | 2017-02-27 |
| 7 | [SpaceX to Send Privately Crewed Dragon Spacecraft Beyond the Moon Next Year](https://news.ycombinator.com/item?id=13748302) | SpaceX 计划次年用载人龙飞船将私人乘客送往月球以远。 | 1747 | 488 | 2017-02-27 |
| 8 | [Looking for Work After 25 Years of Octave](https://news.ycombinator.com/item?id=13603575) | 投入 Octave 开发二十五年后，一位维护者开始寻找工作。 | 1332 | 474 | 2017-02-09 |
| 9 | [The web sucks if you have a slow connection](https://news.ycombinator.com/item?id=13601451) | 作者指出，在慢速网络连接下，现代网页的体验十分糟糕。 | 1269 | 598 | 2017-02-08 |
| 10 | [I started a one-man biz that's beating VC-backed startups](https://news.ycombinator.com/item?id=13656192) | 一位独立创业者称，自己的一人企业正在击败获得风投的创业公司。 | 1237 | 217 | 2017-02-15 |
| 11 | [Mozilla Acquires Pocket](https://news.ycombinator.com/item?id=13746830) | Mozilla 宣布收购 Pocket。 | 1187 | 445 | 2017-02-27 |
| 12 | [GitLab Database Incident – Live Report](https://news.ycombinator.com/item?id=13537052) | GitLab 实时记录一次数据库事故的处置过程。 | 1162 | 598 | 2017-02-01 |
| 13 | [Introducing Cloud Spanner, a Global Database Service](https://news.ycombinator.com/item?id=13644959) | Google 推出全球数据库服务 Cloud Spanner。 | 1068 | 434 | 2017-02-14 |
| 14 | [Introducing Keybase Chat](https://news.ycombinator.com/item?id=13600427) | Keybase 推出聊天服务 Keybase Chat。 | 990 | 192 | 2017-02-08 |
| 15 | [A US-born NASA scientist was detained at the border until he unlocked his phone](https://news.ycombinator.com/item?id=13629593) | 一名出生于美国的 NASA 科学家在边境被扣留，直到解锁手机才获放行。 | 956 | 437 | 2017-02-12 |
| 16 | [List of Sites Affected by Cloudflare's HTTPS Traffic Leak](https://news.ycombinator.com/item?id=13721452) | 整理可能受 Cloudflare HTTPS 流量泄露影响的网站列表。 | 914 | 215 | 2017-02-24 |
| 17 | [Starting an Internet Service Provider](https://news.ycombinator.com/item?id=13688595) | 分享创办互联网接入服务商的经验。 | 912 | 242 | 2017-02-20 |
| 18 | [Alphabet's Waymo Alleges Uber Stole Self-Driving Secrets](https://news.ycombinator.com/item?id=13718586) | Alphabet 旗下 Waymo 指控 Uber 窃取自动驾驶技术机密。 | 907 | 348 | 2017-02-23 |
| 19 | [Why I Don’t Talk to Google Recruiters](https://news.ycombinator.com/item?id=13696004) | 作者解释自己为何不与 Google 招聘人员交流。 | 892 | 652 | 2017-02-21 |
| 20 | [What Vizio was doing behind the TV screen](https://news.ycombinator.com/item?id=13585104) | 美国 FTC 介绍 Vizio 在电视屏幕后开展的活动。 | 888 | 333 | 2017-02-06 |

## 2017-03

有效主帖 27,672 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [CIA malware and hacking tools](https://news.ycombinator.com/item?id=13810015) | 查阅公开披露的 CIA 恶意软件与黑客工具资料。 | 2699 | 1087 | 2017-03-07 |
| 2 | [GitHub lets staff own IP developed for personal projects using company resources](https://news.ycombinator.com/item?id=13921433) | GitHub 允许员工保留使用公司资源开发个人项目的知识产权。 | 1841 | 462 | 2017-03-21 |
| 3 | [Onedrive is slow on Linux but fast with a “Windows” user-agent (2016)](https://news.ycombinator.com/item?id=13932226) | 用户报告，OneDrive 在 Linux 上很慢，改用 Windows 用户代理后速度恢复。 | 1423 | 469 | 2017-03-22 |
| 4 | [Ask HN: What do you want to see in Ubuntu 17.10?](https://news.ycombinator.com/item?id=14002821) | Ubuntu 产品经理向 HN 征集 17.10 版本的意见与功能需求。 | 1374 | 1145 | 2017-03-31 |
| 5 | [They Used To Last 50 Years](https://news.ycombinator.com/item?id=13909365) | 作者以“它们以前能用五十年”为题，关注产品寿命的变化。 | 1359 | 860 | 2017-03-19 |
| 6 | [Teach Yourself Computer Science](https://news.ycombinator.com/item?id=13862284) | 提供自学计算机科学的学习路线与资源。 | 1308 | 237 | 2017-03-13 |
| 7 | [Stories that Hacker News removes from the front page](https://news.ycombinator.com/item?id=13857086) | 观察哪些故事会被 Hacker News 从首页移除。 | 1274 | 314 | 2017-03-13 |
| 8 | [Summary of the Amazon S3 Service Disruption](https://news.ycombinator.com/item?id=13775667) | Amazon 发布 S3 服务中断的情况说明。 | 1246 | 515 | 2017-03-02 |
| 9 | [94-year-old Lithium-Ion Battery Inventor Introduces Solid State Battery](https://news.ycombinator.com/item?id=13778543) | 九十四岁的锂离子电池发明者介绍新的固态电池技术。 | 1168 | 277 | 2017-03-02 |
| 10 | [How Uber Used Secret “Greyball” Tool to Deceive Authorities Worldwide](https://news.ycombinator.com/item?id=13785564) | 报道 Uber 如何用秘密工具 Greyball 欺骗各地监管部门。 | 1144 | 764 | 2017-03-03 |
| 11 | [YC will hold interviews in Vancouver for founders who can’t get US visas](https://news.ycombinator.com/item?id=13830587) | YC 将在温哥华面试无法取得美国签证的创业者。 | 1125 | 788 | 2017-03-09 |
| 12 | [Notepad++ V 7.3.3 – Fix CIA Hacking Notepad++ Issue](https://news.ycombinator.com/item?id=13824032) | Notepad++ 7.3.3 修复与 CIA 入侵手法有关的问题。 | 1101 | 283 | 2017-03-08 |
| 13 | [SES-10 Mission](https://news.ycombinator.com/item?id=13999378) | 观看 SpaceX 的 SES-10 任务相关直播。 | 1094 | 355 | 2017-03-30 |
| 14 | [The Uber Bombshell About to Drop](https://news.ycombinator.com/item?id=13860890) | 作者以“Uber 即将爆出的重磅消息”为题，提出自己的观察。 | 1089 | 512 | 2017-03-13 |
| 15 | [Deep Photo Style Transfer](https://news.ycombinator.com/item?id=13958366) | 展示利用深度学习进行照片风格迁移的项目。 | 1088 | 173 | 2017-03-26 |
| 16 | [Mathematics for Computer Science [pdf]](https://news.ycombinator.com/item?id=13800320) | 一份面向计算机科学的数学教材。 | 1059 | 153 | 2017-03-06 |
| 17 | [Keep the Internet Open](https://news.ycombinator.com/item?id=13870199) | 作者呼吁保持互联网开放。 | 1032 | 391 | 2017-03-14 |
| 18 | [Immersive Linear Algebra – textbook with fully interactive figures (2015)](https://news.ycombinator.com/item?id=13904881) | 通过带有交互式插图的教材学习线性代数。 | 1015 | 74 | 2017-03-19 |
| 19 | [US Senate votes to undo FCC internet privacy rules](https://news.ycombinator.com/item?id=13942345) | 美国参议院投票撤销 FCC 的互联网隐私保护规则。 | 992 | 441 | 2017-03-23 |
| 20 | [Snakisms](https://news.ycombinator.com/item?id=13804522) | 体验名为 Snakisms 的网页作品。 | 961 | 140 | 2017-03-06 |

## 2017-04

有效主帖 23,616 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tim Berners-Lee wins Turing Award](https://news.ycombinator.com/item?id=14031452) | 万维网发明者 Tim Berners-Lee 获得图灵奖。 | 1735 | 287 | 2017-04-04 |
| 2 | [Electron is flash for the desktop (2016)](https://news.ycombinator.com/item?id=14087381) | 作者将 Electron 比作桌面平台上的 Flash。 | 1519 | 996 | 2017-04-11 |
| 3 | [What Happens When You Send a Zero-Day to a Bank?](https://news.ycombinator.com/item?id=14166966) | 向银行报告一个零日漏洞后，会发生什么？ | 1494 | 438 | 2017-04-21 |
| 4 | [We’re dropping Google Ads](https://news.ycombinator.com/item?id=14094083) | 网站团队宣布放弃 Google 广告。 | 1477 | 584 | 2017-04-12 |
| 5 | [Lyrebird – An API to copy the voice of anyone](https://news.ycombinator.com/item?id=14182262) | Lyrebird 提供声称能够模仿任何人声音的 API。 | 1401 | 298 | 2017-04-24 |
| 6 | [Build Your Own Text Editor](https://news.ycombinator.com/item?id=14046446) | 通过亲手实现一个文本编辑器，学习其基本构成。 | 1275 | 159 | 2017-04-05 |
| 7 | [Show HN: Sorting Two Metric Tons of Lego](https://news.ycombinator.com/item?id=14226889) | 作者展示给两吨乐高积木分类的过程。 | 1264 | 211 | 2017-04-29 |
| 8 | [How We Built r/Place](https://news.ycombinator.com/item?id=14109158) | Reddit 团队介绍 r/Place 是如何构建的。 | 1152 | 242 | 2017-04-13 |
| 9 | [Steve Ballmer serves up a data trove about government spending in the US](https://news.ycombinator.com/item?id=14136081) | Steve Ballmer 提供一批关于美国政府支出的数据。 | 1124 | 258 | 2017-04-18 |
| 10 | [A Competitive Programmer's Handbook](https://news.ycombinator.com/item?id=14115826) | 一本面向竞赛编程学习者的手册。 | 1117 | 157 | 2017-04-14 |
| 11 | [Calculus Made Easy (1914) [pdf]](https://news.ycombinator.com/item?id=14161876) | 阅读一九一四年的微积分入门教材《Calculus Made Easy》。 | 1080 | 189 | 2017-04-20 |
| 12 | [USA Facts – Federal, state, and local data from government sources](https://news.ycombinator.com/item?id=14139186) | USA Facts 汇集来自美国联邦、州与地方政府的数据。 | 1044 | 340 | 2017-04-18 |
| 13 | [How SSH got port number 22](https://news.ycombinator.com/item?id=14178091) | 回顾 SSH 为什么使用二十二号端口。 | 1034 | 207 | 2017-04-23 |
| 14 | [An off-grid social network](https://news.ycombinator.com/item?id=14050049) | 探索一种可以离开常规网络基础设施运行的社交网络。 | 1031 | 366 | 2017-04-06 |
| 15 | [IndieHackers.com acquired by Stripe](https://news.ycombinator.com/item?id=14090063) | Stripe 宣布收购 IndieHackers.com。 | 1000 | 235 | 2017-04-11 |
| 16 | [Why Japan’s Rail Workers Point at Things](https://news.ycombinator.com/item?id=14011793) | 日本铁路员工为什么要指着物体并口头确认？ | 959 | 322 | 2017-04-01 |
| 17 | [The Mac Pro Lives](https://news.ycombinator.com/item?id=14031619) | 围绕 Mac Pro 的未来，介绍这条产品线的新动向。 | 877 | 801 | 2017-04-04 |
| 18 | [PhantomJS: Stepping down as maintainer](https://news.ycombinator.com/item?id=14105489) | PhantomJS 维护者宣布卸任。 | 854 | 225 | 2017-04-13 |
| 19 | [Facebook Announces React Fiber, a Rewrite of Its React Framework](https://news.ycombinator.com/item?id=14142120) | Facebook 公布 React Fiber，对 React 框架进行重写。 | 851 | 406 | 2017-04-18 |
| 20 | [Wikipedia blocked in Turkey](https://news.ycombinator.com/item?id=14225602) | 维基百科在土耳其遭到封锁。 | 850 | 450 | 2017-04-29 |

## 2017-05

有效主帖 24,675 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Get started making music](https://news.ycombinator.com/item?id=14299628) | 通过入门课程开始学习制作音乐。 | 2106 | 461 | 2017-05-09 |
| 2 | [Accidentally Stopping a Global Cyber Attack](https://news.ycombinator.com/item?id=14330547) | 研究者讲述自己意外阻止一场全球网络攻击的经过。 | 1981 | 338 | 2017-05-13 |
| 3 | [CRISPR eliminates HIV-1 infection in live animals](https://news.ycombinator.com/item?id=14248827) | 一项研究报告称，CRISPR 消除了活体动物中的 HIV-1 感染。 | 1455 | 239 | 2017-05-02 |
| 4 | [A crashed advertisement reveals logs of a facial recognition system](https://news.ycombinator.com/item?id=14309194) | 一块崩溃的广告屏意外显示出人脸识别系统日志。 | 1450 | 522 | 2017-05-10 |
| 5 | [My Family’s Slave](https://news.ycombinator.com/item?id=14350059) | 作者讲述被称为“我家的奴隶”的一位女性的故事。 | 1419 | 606 | 2017-05-16 |
| 6 | [Cyberattacks in 12 Nations Said to Use Leaked N.S.A. Hacking Tool](https://news.ycombinator.com/item?id=14326439) | 报道十二个国家遭到网络攻击，据称涉及泄露的 NSA 黑客工具。 | 1248 | 478 | 2017-05-12 |
| 7 | [Fireflies](https://news.ycombinator.com/item?id=14452832) | 体验以萤火虫为主题的网页项目。 | 1243 | 89 | 2017-05-31 |
| 8 | [Wikimedia Foundation spending](https://news.ycombinator.com/item?id=14287235) | 围绕维基媒体基金会的支出，审视其经费使用。 | 1054 | 409 | 2017-05-07 |
| 9 | [The largest Git repo](https://news.ycombinator.com/item?id=14411126) | 介绍一个被称为全球最大的 Git 仓库。 | 1053 | 402 | 2017-05-24 |
| 10 | [Root – Programmable bank account for software developers](https://news.ycombinator.com/item?id=14256300) | Root 为软件开发者提供可编程的银行账户。 | 1015 | 409 | 2017-05-03 |
| 11 | [1Password Travel Mode: Protect your data when crossing borders](https://news.ycombinator.com/item?id=14403911) | 1Password 推出旅行模式，帮助用户在跨越边境时保护数据。 | 1004 | 521 | 2017-05-23 |
| 12 | [Kill Google AMP before it kills the web](https://news.ycombinator.com/item?id=14384187) | 作者强烈批评 Google AMP，认为它正在损害开放网络。 | 969 | 462 | 2017-05-20 |
| 13 | [A startup’s Firebase bill suddenly increased from $25 to $1750 per month](https://news.ycombinator.com/item?id=14356409) | 一家创业公司的 Firebase 月账单突然从二十五美元涨至一千七百五十美元。 | 952 | 497 | 2017-05-17 |
| 14 | [Net neutrality is in jeopardy again](https://news.ycombinator.com/item?id=14291412) | Mozilla 警告，网络中立性再次面临威胁。 | 928 | 374 | 2017-05-08 |
| 15 | [SCOTUS: Patent Rights Over a Printer Cartridge Are Exhausted When It Is Sold](https://news.ycombinator.com/item?id=14446261) | 美国最高法院裁定，打印机墨盒出售后，相关专利权即告用尽。 | 884 | 303 | 2017-05-30 |
| 16 | [Uber faces criminal probe over software used to evade authorities](https://news.ycombinator.com/item?id=14269708) | Uber 因涉嫌利用软件规避监管而面临刑事调查。 | 883 | 559 | 2017-05-04 |
| 17 | [Why I Quit Being So Accommodating (1922)](https://news.ycombinator.com/item?id=14418877) | 重读一九二二年的文章，了解作者为何不再一味迁就他人。 | 866 | 316 | 2017-05-25 |
| 18 | [A federal court has denied a pre-trial motion to dismiss a GPL enforcement case](https://news.ycombinator.com/item?id=14323265) | 美国联邦法院拒绝在庭审前撤销一宗 GPL 执行案件。 | 853 | 215 | 2017-05-12 |
| 19 | [Prepack helps make JavaScript code more efficient](https://news.ycombinator.com/item?id=14257744) | Prepack 尝试让 JavaScript 代码运行得更高效。 | 836 | 224 | 2017-05-03 |
| 20 | [The Horror in the Standard Library](https://news.ycombinator.com/item?id=14275805) | 作者披露标准库中令人担忧的问题。 | 830 | 216 | 2017-05-05 |

## 2017-06

有效主帖 23,901 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Uber Founder Travis Kalanick Resigns as C.E.O.](https://news.ycombinator.com/item?id=14600873) | Uber 创始人 Travis Kalanick 辞去首席执行官职务。 | 2119 | 1292 | 2017-06-21 |
| 2 | [Amazon to Acquire Whole Foods for $13.7B](https://news.ycombinator.com/item?id=14568468) | Amazon 宣布以一百三十七亿美元收购 Whole Foods。 | 1687 | 824 | 2017-06-16 |
| 3 | [Facebook is an attack on the open web](https://news.ycombinator.com/item?id=14462785) | 作者认为 Facebook 正在攻击开放网络。 | 1635 | 421 | 2017-06-01 |
| 4 | [Silicon Valley Women, in Cultural Shift, Frankly Describe Sexual Harassment](https://news.ycombinator.com/item?id=14673777) | 硅谷女性公开讲述性骚扰经历，反映行业文化的变化。 | 1188 | 730 | 2017-06-30 |
| 5 | [Please Make Google AMP Optional](https://news.ycombinator.com/item?id=14529376) | 作者呼吁让 Google AMP 成为用户可以选择的选项。 | 1146 | 436 | 2017-06-10 |
| 6 | [Intel Skylake/Kaby Lake processors: broken hyper-threading](https://news.ycombinator.com/item?id=14630183) | 披露 Intel Skylake 与 Kaby Lake 处理器的超线程问题。 | 1108 | 269 | 2017-06-25 |
| 7 | [Show HN: Get Paid to Build Your Next Side Project](https://news.ycombinator.com/item?id=14552615) | 展示一个让开发者获得报酬、构建下一个业余项目的平台。 | 1100 | 451 | 2017-06-14 |
| 8 | [Show HN: Monica, an open-source CRM to manage friends and family](https://news.ycombinator.com/item?id=14497295) | Monica 是开源的个人关系管理工具，帮助维护亲友联系。 | 1097 | 568 | 2017-06-06 |
| 9 | [“Let her speak please”](https://news.ycombinator.com/item?id=14505073) | 一篇以“请让她说话”为题、呼吁给予表达机会的文字。 | 995 | 646 | 2017-06-07 |
| 10 | [Luna – Visual and textual functional programming language](https://news.ycombinator.com/item?id=14612680) | Luna 是兼具视觉与文本形式的函数式编程语言。 | 944 | 310 | 2017-06-22 |
| 11 | [Alex Honnold Scales El Capitan Without Ropes, and the Climbing World Reels](https://news.ycombinator.com/item?id=14498724) | Alex Honnold 不借助绳索攀登酋长岩，震动攀岩界。 | 928 | 495 | 2017-06-06 |
| 12 | [Ask HN: What language-agnostic programming books should I read?](https://news.ycombinator.com/item?id=14486657) | HN 用户征集不局限于某种语言的编程书籍推荐。 | 927 | 337 | 2017-06-05 |
| 13 | [Google Will Stop Reading Your Emails for Gmail Ads](https://news.ycombinator.com/item?id=14620608) | Google 将停止为投放 Gmail 广告而读取用户邮件。 | 903 | 437 | 2017-06-23 |
| 14 | [Developers who use spaces make more money than those who use tabs](https://news.ycombinator.com/item?id=14560042) | 一项调查发现，使用空格缩进的开发者收入高于使用制表符者。 | 881 | 663 | 2017-06-15 |
| 15 | [How is GNU `yes` so fast?](https://news.ycombinator.com/item?id=14542938) | GNU 的 yes 命令为什么能运行得这么快？ | 872 | 334 | 2017-06-13 |
| 16 | [Network Protocols](https://news.ycombinator.com/item?id=14468471) | 介绍计算机网络协议的相关知识。 | 842 | 75 | 2017-06-02 |
| 17 | [Georgia Tech's free math textbook collective](https://news.ycombinator.com/item?id=14581273) | 佐治亚理工整理可免费获取的数学教材资源。 | 834 | 78 | 2017-06-18 |
| 18 | [TLDR Stock Options](https://news.ycombinator.com/item?id=14463260) | 以简明方式理解股票期权。 | 819 | 205 | 2017-06-01 |
| 19 | [Reverse engineering guide for beginners: Methodology and tools](https://news.ycombinator.com/item?id=14537506) | 面向初学者介绍逆向工程的方法与工具。 | 801 | 63 | 2017-06-12 |
| 20 | [Pinboard Acquires Delicious](https://news.ycombinator.com/item?id=14462384) | Pinboard 宣布收购 Delicious。 | 800 | 227 | 2017-06-01 |

## 2017-07

有效主帖 23,007 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Net Neutrality Day of Action: Help Preserve the Open Internet](https://news.ycombinator.com/item?id=14754772) | 网络中立性行动日呼吁公众共同维护开放互联网。 | 1664 | 433 | 2017-07-12 |
| 2 | [Taking control of all .io domains with a targeted registration](https://news.ycombinator.com/item?id=14737322) | 研究者展示如何通过一次针对性的注册，获得对全部 .io 域名的控制能力。 | 1404 | 246 | 2017-07-10 |
| 3 | [Apache Foundation disallows use of the Facebook “BSD+Patent” license](https://news.ycombinator.com/item?id=14779881) | Apache 基金会禁止使用 Facebook 的“BSD 加专利”许可证。 | 1277 | 362 | 2017-07-16 |
| 4 | [Battle for the Internet](https://news.ycombinator.com/item?id=14750627) | 参与一项以“为互联网而战”为主题的公众行动。 | 1275 | 487 | 2017-07-12 |
| 5 | [“We will stop updating and distributing the Flash Player at the end of 2020”](https://news.ycombinator.com/item?id=14848786) | Adobe 宣布，将于二〇二〇年末停止更新与分发 Flash Player。 | 1213 | 487 | 2017-07-25 |
| 6 | [Making a virtual machine in Google Sheets](https://news.ycombinator.com/item?id=14701460) | 在 Google Sheets 电子表格里构建一台虚拟机。 | 1074 | 113 | 2017-07-05 |
| 7 | [How a VC-funded company is undermining the open-source community](https://news.ycombinator.com/item?id=14836653) | 作者指责一家获得风投资助的公司正在削弱开源社区。 | 1014 | 415 | 2017-07-24 |
| 8 | [24-core CPU and I can’t move my mouse](https://news.ycombinator.com/item?id=14733829) | 作者追查为何配备二十四核 CPU 的电脑仍会卡到无法移动鼠标。 | 1011 | 499 | 2017-07-10 |
| 9 | [The New Firefox and Ridiculous Numbers of Tabs](https://news.ycombinator.com/item?id=14823807) | 观察新版 Firefox 在打开大量标签页时的表现。 | 984 | 537 | 2017-07-21 |
| 10 | [153k Ether Stolen in Parity Multi-Sig Attack](https://news.ycombinator.com/item?id=14807779) | Parity 多重签名钱包遭攻击，约十五万三千枚以太币被盗。 | 943 | 725 | 2017-07-19 |
| 11 | [I'm not a Woman in Tech](https://news.ycombinator.com/item?id=14702676) | 作者以“我不是科技界女性”为题，反思这一身份标签。 | 876 | 578 | 2017-07-05 |
| 12 | [18yo arrested for reporting a bug in the new Budapest e-Ticket system](https://news.ycombinator.com/item?id=14835515) | 一名十八岁青年因报告布达佩斯新电子票务系统的漏洞而被捕。 | 874 | 309 | 2017-07-24 |
| 13 | [Wildcard Certificates Coming January 2018](https://news.ycombinator.com/item?id=14711153) | 证书服务宣布计划于二〇一八年一月提供通配符证书。 | 857 | 191 | 2017-07-06 |
| 14 | [What Is Ethereum?](https://news.ycombinator.com/item?id=14723308) | 用入门介绍回答“以太坊是什么”。 | 837 | 257 | 2017-07-08 |
| 15 | [Seeing AI for iOS](https://news.ycombinator.com/item?id=14774167) | 微软推出面向 iOS 的 Seeing AI 应用。 | 835 | 126 | 2017-07-14 |
| 16 | [How Discord Scaled Elixir to 5M Concurrent Users](https://news.ycombinator.com/item?id=14748028) | Discord 分享如何借助 Elixir 支撑五百万并发用户。 | 802 | 251 | 2017-07-11 |
| 17 | [The Limitations of Deep Learning](https://news.ycombinator.com/item?id=14790251) | 探讨深度学习的能力边界与局限。 | 794 | 260 | 2017-07-17 |
| 18 | [Ubershaders: A Ridiculous Solution to an Impossible Problem](https://news.ycombinator.com/item?id=14884992) | 介绍 Ubershaders，尝试解决一个被形容为近乎不可能的图形问题。 | 772 | 88 | 2017-07-30 |
| 19 | [How to make a friend fast](https://news.ycombinator.com/item?id=14731181) | 分享如何较快与他人建立友谊的思路。 | 765 | 242 | 2017-07-09 |
| 20 | [It is as if you were doing work](https://news.ycombinator.com/item?id=14699397) | 体验一款让你仿佛正在工作的网页作品。 | 752 | 205 | 2017-07-05 |

## 2017-08

有效主帖 23,672 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Launch HN: 70MillionJobs (YC S17) – Job board for people with criminal records](https://news.ycombinator.com/item?id=14911467) | 70MillionJobs 推出面向有犯罪记录者的求职平台。 | 1879 | 506 | 2017-08-02 |
| 2 | [Google Fires Employee Behind Controversial Diversity Memo](https://news.ycombinator.com/item?id=14952787) | Google 解雇了一份争议性多元化备忘录的作者。 | 1697 | 2371 | 2017-08-08 |
| 3 | [A camera that snaps a GIF and ejects a cartridge that displays it](https://news.ycombinator.com/item?id=15133919) | 一台相机拍下 GIF 后，会吐出可以直接播放该动画的卡匣。 | 1480 | 296 | 2017-08-30 |
| 4 | [Ad blocking is under attack](https://news.ycombinator.com/item?id=14990137) | 作者警告，广告拦截正在受到挑战。 | 1111 | 559 | 2017-08-11 |
| 5 | [Ask a Female Engineer: Thoughts on the Google Memo](https://news.ycombinator.com/item?id=15021427) | 一位女性工程师分享对 Google 备忘录争议的看法。 | 1080 | 1501 | 2017-08-15 |
| 6 | [Criticizing Google got me fired](https://news.ycombinator.com/item?id=15142853) | 作者称，自己因批评 Google 而被解雇。 | 1010 | 440 | 2017-08-31 |
| 7 | [Explaining React's license](https://news.ycombinator.com/item?id=15050841) | Facebook 解释 React 的许可证安排。 | 978 | 595 | 2017-08-19 |
| 8 | [I Fell Victim to a $1,500 Used Camera Lens Scam on Amazon](https://news.ycombinator.com/item?id=14993216) | 作者讲述在 Amazon 购买二手相机镜头时，遭遇一千五百美元骗局的经历。 | 937 | 428 | 2017-08-11 |
| 9 | [Why We Terminated Daily Stormer](https://news.ycombinator.com/item?id=15031922) | Cloudflare 解释为何终止向 Daily Stormer 提供服务。 | 857 | 1526 | 2017-08-16 |
| 10 | [“Learning How to Learn,” the most popular course on Coursera](https://news.ycombinator.com/item?id=15092707) | 介绍 Coursera 上最受欢迎的课程《学会如何学习》。 | 848 | 183 | 2017-08-24 |
| 11 | [Show HN: A stop-motion video of an engine](https://news.ycombinator.com/item?id=15017126) | 展示一段关于发动机的定格动画。 | 845 | 188 | 2017-08-15 |
| 12 | [Feather: Open-source icons](https://news.ycombinator.com/item?id=15089916) | Feather 提供一套开源图标。 | 844 | 140 | 2017-08-24 |
| 13 | [Essential Phone, available now](https://news.ycombinator.com/item?id=15037960) | Essential 宣布其手机正式开售。 | 818 | 672 | 2017-08-17 |
| 14 | [Headless mode in Firefox](https://news.ycombinator.com/item?id=15131525) | 介绍 Firefox 的无界面运行模式。 | 817 | 182 | 2017-08-30 |
| 15 | [Show HN: Is the stock market going to crash?](https://news.ycombinator.com/item?id=14947361) | 展示一个以“股市会崩盘吗”为问题的网站。 | 813 | 325 | 2017-08-07 |
| 16 | [Ask HN: What is your favorite CS paper?](https://news.ycombinator.com/item?id=15089476) | HN 用户分享自己最喜欢的计算机科学论文。 | 793 | 257 | 2017-08-24 |
| 17 | [Google Critic Ousted from Think Tank Funded by the Tech Giant](https://news.ycombinator.com/item?id=15131370) | 一位 Google 批评者被一家接受 Google 资助的智库解雇。 | 793 | 448 | 2017-08-30 |
| 18 | [I’m an Ex-Google Woman Tech Leader and I’m Sick of Our Approach to Diversity](https://news.ycombinator.com/item?id=15009759) | 一位前 Google 女性技术主管批评科技行业处理多元化问题的方式。 | 791 | 420 | 2017-08-14 |
| 19 | [U.S. judge says LinkedIn cannot block startup from public profile data](https://news.ycombinator.com/item?id=15012883) | 美国法官表示，LinkedIn 不得阻止一家创业公司获取公开个人资料。 | 779 | 288 | 2017-08-14 |
| 20 | [Android Oreo](https://news.ycombinator.com/item?id=15066729) | Android 发布代号为 Oreo 的新版本。 | 778 | 641 | 2017-08-21 |

## 2017-09

有效主帖 23,418 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [W3C abandons consensus, standardizes DRM, EFF resigns](https://news.ycombinator.com/item?id=15278883) | W3C 将 DRM 纳入标准，EFF 为此退出该组织。 | 2735 | 978 | 2017-09-18 |
| 2 | [Relicensing React, Jest, Flow, and Immutable.js](https://news.ycombinator.com/item?id=15316175) | Facebook 宣布调整 React、Jest、Flow 与 Immutable.js 的许可证。 | 2280 | 498 | 2017-09-22 |
| 3 | [It’s time to give Firefox another chance](https://news.ycombinator.com/item?id=15368353) | 作者建议，给 Firefox 再一次机会。 | 1674 | 712 | 2017-09-29 |
| 4 | [Sublime Text 3.0](https://news.ycombinator.com/item?id=15237896) | Sublime Text 发布 3.0 版本。 | 1653 | 675 | 2017-09-13 |
| 5 | [Equifax Faces Multibillion-Dollar Lawsuit Over Hack](https://news.ycombinator.com/item?id=15200955) | Equifax 因数据泄露事件面临数十亿美元诉讼。 | 1345 | 648 | 2017-09-08 |
| 6 | [China Blocks WhatsApp](https://news.ycombinator.com/item?id=15332819) | 报道 WhatsApp 在中国遭到封锁。 | 1174 | 618 | 2017-09-25 |
| 7 | [DuckDuckGo vs Google](https://news.ycombinator.com/item?id=15291961) | 比较 DuckDuckGo 与 Google 搜索服务。 | 1140 | 536 | 2017-09-20 |
| 8 | [Facebook, You Needy Sonofabitch](https://news.ycombinator.com/item?id=15222240) | 作者批评 Facebook 不断向用户索取关注。 | 1111 | 387 | 2017-09-11 |
| 9 | [Delta Goes Big, Then Goes Home](https://news.ycombinator.com/item?id=15193892) | 一篇以“Delta 大举出动后返航”为题的飞行记录。 | 1107 | 188 | 2017-09-07 |
| 10 | [Facebook recruiting and Unix systems](https://news.ycombinator.com/item?id=15187874) | 围绕 Facebook 招聘与 Unix 系统，分享一段趣味材料。 | 1091 | 477 | 2017-09-06 |
| 11 | [Identity Theft, Credit Reports, and You](https://news.ycombinator.com/item?id=15206926) | 解释身份盗用与信用报告，帮助理解个人可能受到的影响。 | 1088 | 276 | 2017-09-09 |
| 12 | [Cybersecurity Incident Involving Consumer Information](https://news.ycombinator.com/item?id=15195510) | Equifax 就涉及消费者资料的网络安全事件发表公告。 | 1044 | 532 | 2017-09-07 |
| 13 | [Text-only CNN](https://news.ycombinator.com/item?id=15210022) | 使用仅保留文字内容的 CNN 网站。 | 1017 | 297 | 2017-09-10 |
| 14 | [It’s time to kill the web app](https://news.ycombinator.com/item?id=15321015) | 作者主张，是时候结束现有的网页应用模式。 | 1003 | 702 | 2017-09-23 |
| 15 | [iPhone X](https://news.ycombinator.com/item?id=15230871) | Apple 发布 iPhone X。 | 995 | 1746 | 2017-09-12 |
| 16 | [Optimizing web servers for high throughput and low latency](https://news.ycombinator.com/item?id=15185416) | 介绍如何优化网页服务器，以兼顾高吞吐量和低延迟。 | 987 | 84 | 2017-09-06 |
| 17 | [A new kind of map: it’s about time](https://news.ycombinator.com/item?id=15294171) | 探索一种以时间为核心的新地图呈现方式。 | 968 | 201 | 2017-09-20 |
| 18 | [New in PostgreSQL 10](https://news.ycombinator.com/item?id=15306398) | 介绍 PostgreSQL 10 的新增功能。 | 962 | 249 | 2017-09-21 |
| 19 | [Insane state of today's advertising part 3](https://news.ycombinator.com/item?id=15145226) | 作者继续批评当代网络广告的失控状态。 | 961 | 420 | 2017-09-01 |
| 20 | [A “right to repair” movement tools up](https://news.ycombinator.com/item?id=15360362) | 报道“维修权”运动的发展与行动。 | 928 | 305 | 2017-09-28 |

## 2017-10

有效主帖 23,874 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Keybase launches encrypted Git](https://news.ycombinator.com/item?id=15401211) | Keybase 推出加密 Git 服务。 | 1427 | 270 | 2017-10-04 |
| 2 | [Key Reinstallation Attacks – Breaking WPA2 by Forcing Nonce Reuse](https://news.ycombinator.com/item?id=15481819) | 密钥重安装攻击通过迫使 Nonce 重用，突破 WPA2 的安全保护。 | 1371 | 411 | 2017-10-16 |
| 3 | [US telcos appear to be selling non-anonymized access to consumer telephone data](https://news.ycombinator.com/item?id=15477286) | 研究者怀疑，美国电信运营商正在出售未匿名化的用户电话数据访问能力。 | 1273 | 301 | 2017-10-15 |
| 4 | [DevDocs API Documentation](https://news.ycombinator.com/item?id=15507871) | DevDocs 汇集多种 API 文档，方便开发者查询。 | 1239 | 141 | 2017-10-19 |
| 5 | [Documenting the Web together](https://news.ycombinator.com/item?id=15500220) | 介绍共同维护网页技术文档的协作计划。 | 1210 | 203 | 2017-10-18 |
| 6 | [Guacamole – A clientless remote desktop gateway](https://news.ycombinator.com/item?id=15389727) | Guacamole 提供无需专用客户端的远程桌面网关。 | 1096 | 216 | 2017-10-03 |
| 7 | [PostgreSQL 10 Released](https://news.ycombinator.com/item?id=15408800) | PostgreSQL 发布 10 版本。 | 1024 | 296 | 2017-10-05 |
| 8 | [Do you need a VPN?](https://news.ycombinator.com/item?id=15585769) | 你是否需要 VPN，又该如何判断自己的需求？ | 969 | 479 | 2017-10-30 |
| 9 | [I Fell 15,000 Feet and Lived](https://news.ycombinator.com/item?id=15480334) | 作者讲述自己从一万五千英尺高处坠落后幸存的经历。 | 950 | 246 | 2017-10-16 |
| 10 | [AlphaGo Zero: Learning from scratch](https://news.ycombinator.com/item?id=15500836) | AlphaGo Zero 展示从零开始学习围棋的方式。 | 923 | 311 | 2017-10-18 |
| 11 | [We only hire the best means we only hire the trendiest (2016)](https://news.ycombinator.com/item?id=15591441) | 作者认为“只招最好的人”常常变成只招最符合潮流的人。 | 910 | 625 | 2017-10-31 |
| 12 | [75% decline over 27 years in total flying insect biomass in protected areas](https://news.ycombinator.com/item?id=15502074) | 一项研究发现，保护区内飞虫总生物量在二十七年间下降了百分之七十五。 | 901 | 432 | 2017-10-18 |
| 13 | [Try quickly typing 1+ 2 + 3 into the iOS 11 Calculator](https://news.ycombinator.com/item?id=15538666) | 在 iOS 11 计算器中快速输入一加二加三，观察其响应。 | 886 | 480 | 2017-10-24 |
| 14 | ['Our minds can be hijacked': tech insiders who fear a smartphone dystopia](https://news.ycombinator.com/item?id=15421704) | 科技行业内部人士担忧，智能手机可能劫持人的心智。 | 878 | 386 | 2017-10-07 |
| 15 | [The New York Times Is Now Available as a Tor Onion Service](https://news.ycombinator.com/item?id=15567356) | 《纽约时报》推出可经 Tor 访问的洋葱服务。 | 878 | 192 | 2017-10-27 |
| 16 | [Five minute guide to better typography](https://news.ycombinator.com/item?id=15424478) | 用五分钟了解改善文字排版的基本方法。 | 868 | 126 | 2017-10-07 |
| 17 | [iOS Privacy: Easily get a user's Apple ID password, just by asking](https://news.ycombinator.com/item?id=15441537) | 研究者指出，iOS 上伪装成系统提示的询问可能骗取 Apple ID 密码。 | 867 | 320 | 2017-10-10 |
| 18 | [Why We Must Fight for the Right to Repair Our Electronics](https://news.ycombinator.com/item?id=15546536) | 作者解释为何必须争取自行维修电子设备的权利。 | 866 | 258 | 2017-10-25 |
| 19 | [Firefox Send: Private, Encrypted File Sharing](https://news.ycombinator.com/item?id=15448996) | Firefox Send 提供强调隐私的加密文件分享服务。 | 856 | 275 | 2017-10-11 |
| 20 | [The web at maximum FPS: How WebRender gets rid of jank](https://news.ycombinator.com/item?id=15442676) | 介绍 WebRender 如何减少卡顿，提升网页渲染帧率。 | 853 | 207 | 2017-10-10 |

## 2017-11

有效主帖 22,495 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [macOS High Sierra: Anyone can login as “root” with empty password](https://news.ycombinator.com/item?id=15800676) | macOS High Sierra 被发现可使用空密码登录 root 账户。 | 3001 | 1056 | 2017-11-28 |
| 2 | [How Firefox Got Fast Again](https://news.ycombinator.com/item?id=15686653) | 介绍 Firefox 如何重新提升运行速度。 | 2180 | 687 | 2017-11-13 |
| 3 | [Uber Paid Hackers to Delete Stolen Data on 57M People](https://news.ycombinator.com/item?id=15752022) | Uber 被曝付钱给黑客，要求删除窃取的五千七百万人的资料。 | 1720 | 572 | 2017-11-21 |
| 4 | [Firefox 57.0 Released](https://news.ycombinator.com/item?id=15694926) | Firefox 发布 57.0 版本。 | 1692 | 813 | 2017-11-14 |
| 5 | [Modern Media Is a DoS Attack on Free Will](https://news.ycombinator.com/item?id=15741565) | 作者把现代媒体比作针对自由意志的拒绝服务攻击。 | 1466 | 496 | 2017-11-20 |
| 6 | [FCC plan would give Internet providers power to choose the sites customers see](https://news.ycombinator.com/item?id=15749150) | 报道 FCC 的新计划可能让网络提供商决定用户能访问哪些网站。 | 1330 | 646 | 2017-11-21 |
| 7 | [Against an Increasingly User-Hostile Web](https://news.ycombinator.com/item?id=15611122) | 作者反对日益对用户不友好的网络体验。 | 1307 | 503 | 2017-11-02 |
| 8 | [Join the Battle for Net Neutrality](https://news.ycombinator.com/item?id=15754287) | 一项邀请公众参与维护网络中立性的行动。 | 1269 | 379 | 2017-11-22 |
| 9 | [Tesla Roadster](https://news.ycombinator.com/item?id=15719262) | Tesla 公布 Roadster 跑车。 | 1261 | 708 | 2017-11-17 |
| 10 | [Paradise Papers: Dear Tim Cook](https://news.ycombinator.com/item?id=15651058) | 围绕“天堂文件”，一封向 Tim Cook 提问的公开文字。 | 1200 | 791 | 2017-11-08 |
| 11 | [Chrome breaks the Web](https://news.ycombinator.com/item?id=15634609) | 作者批评 Chrome 的某些行为正在破坏网页生态。 | 1187 | 458 | 2017-11-06 |
| 12 | [Senators push to ditch social security numbers in light of Equifax hack](https://news.ycombinator.com/item?id=15657887) | Equifax 遭入侵后，美国参议员推动放弃社会保障号码的现有用途。 | 1126 | 464 | 2017-11-08 |
| 13 | [Waymo now testing its self-driving cars on public roads with no one at the wheel](https://news.ycombinator.com/item?id=15644680) | Waymo 开始在公共道路测试驾驶座无人值守的自动驾驶汽车。 | 1120 | 609 | 2017-11-07 |
| 14 | [Stanford CS007: Personal Finance For Engineers](https://news.ycombinator.com/item?id=15786703) | 斯坦福 CS007 课程为工程师讲授个人理财。 | 1089 | 343 | 2017-11-27 |
| 15 | [An Open Letter to Intel](https://news.ycombinator.com/item?id=15642116) | 一封写给 Intel 的公开信。 | 996 | 363 | 2017-11-07 |
| 16 | [Using SVG as image placeholders](https://news.ycombinator.com/item?id=15696596) | 介绍如何使用 SVG 作为图片加载前的占位图。 | 983 | 134 | 2017-11-14 |
| 17 | [I'm on the FCC. Please stop us from killing net neutrality](https://news.ycombinator.com/item?id=15762451) | 一位 FCC 委员呼吁公众阻止委员会废除网络中立性。 | 966 | 407 | 2017-11-23 |
| 18 | [Google collects cell tower info even if location services are disabled](https://news.ycombinator.com/item?id=15747519) | 报道 Google 即使在关闭定位服务后，仍收集移动基站信息。 | 953 | 401 | 2017-11-21 |
| 19 | [Norvig's Python programs to practice or demonstrate skills](https://news.ycombinator.com/item?id=15787023) | Peter Norvig 整理的 Python 程序，用于练习和演示编程技巧。 | 937 | 84 | 2017-11-27 |
| 20 | [Exploring different microcontrollers less than $1](https://news.ycombinator.com/item?id=15633785) | 比较多款售价不到一美元的微控制器。 | 929 | 183 | 2017-11-06 |

## 2017-12

有效主帖 21,250 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [F.C.C. Repeals Net Neutrality Rules](https://news.ycombinator.com/item?id=15924794) | 美国 FCC 废除网络中立性规则。 | 3384 | 1431 | 2017-12-14 |
| 2 | [Firefox is on a slippery slope](https://news.ycombinator.com/item?id=15940144) | 作者担忧 Firefox 正沿着一条危险的方向发展。 | 2023 | 874 | 2017-12-16 |
| 3 | [Google Maps' Moat](https://news.ycombinator.com/item?id=15965653) | 分析 Google Maps 所拥有的竞争壁垒。 | 1960 | 609 | 2017-12-19 |
| 4 | [Machine Learning 101 slidedeck: 2 years of headbanging, so you don't have to](https://news.ycombinator.com/item?id=15919115) | 一份机器学习入门幻灯片，整理作者两年学习中积累的经验。 | 1656 | 120 | 2017-12-14 |
| 5 | [Show HN: Airmash – Multiplayer Missile Warfare HTML5 Game](https://news.ycombinator.com/item?id=15892066) | Airmash 是一款基于 HTML5 的多人导弹对战游戏。 | 1535 | 304 | 2017-12-10 |
| 6 | [Norway votes to decriminalise drugs and offer treatment instead of jail time](https://news.ycombinator.com/item?id=15941428) | 挪威投票支持推动毒品非刑事化，以治疗替代监禁。 | 1214 | 217 | 2017-12-16 |
| 7 | [Oh shit, git: Getting myself out of bad situations](https://news.ycombinator.com/item?id=15951825) | 整理 Git 操作出错后，用来摆脱困境的实用方法。 | 1209 | 508 | 2017-12-18 |
| 8 | [We’re sorry, and we’re not rolling out the fees change](https://news.ycombinator.com/item?id=15916121) | 平台为收费调整致歉，并宣布取消实施计划。 | 1195 | 539 | 2017-12-13 |
| 9 | [Dozens of Companies Are Using Facebook to Exclude Older Workers From Job Ads](https://news.ycombinator.com/item?id=15974603) | 报道数十家公司利用 Facebook 广告定向，将年长求职者排除在招聘广告之外。 | 1186 | 786 | 2017-12-20 |
| 10 | [A Message to Our Customers about iPhone Batteries and Performance](https://news.ycombinator.com/item?id=16025112) | Apple 就 iPhone 电池与性能向客户发布说明。 | 1176 | 832 | 2017-12-28 |
| 11 | [AMA: NY AG Schneiderman on net neutrality and protecting our voice in government](https://news.ycombinator.com/item?id=15853374) | 纽约州总检察长参加问答，介绍对 FCC 网络中立性征询中虚假评论的调查。 | 1126 | 269 | 2017-12-05 |
| 12 | [Magic Leap One](https://news.ycombinator.com/item?id=15969511) | Magic Leap 公布 One 产品。 | 1115 | 623 | 2017-12-20 |
| 13 | [Comcast is injecting 400+ lines of JavaScript into web pages](https://news.ycombinator.com/item?id=15890551) | 用户发现 Comcast 向网页注入四百多行 JavaScript。 | 999 | 479 | 2017-12-10 |
| 14 | [Things Many People Find Too Obvious to Have Told You Already](https://news.ycombinator.com/item?id=15826445) | 分享一些因被认为太显然而常常没人主动说明的事情。 | 854 | 487 | 2017-12-01 |
| 15 | [Statement on Cryptocurrencies and Initial Coin Offerings](https://news.ycombinator.com/item?id=15902054) | 美国证券监管机构发表关于加密货币与首次代币发行的声明。 | 811 | 161 | 2017-12-12 |
| 16 | [Chrome is Not the Standard](https://news.ycombinator.com/item?id=15980653) | 作者提醒，Chrome 的行为不能直接等同于网页标准。 | 807 | 451 | 2017-12-21 |
| 17 | [Exercism – Level up your programming skills](https://news.ycombinator.com/item?id=15897809) | Exercism 通过练习帮助提升编程技能。 | 795 | 94 | 2017-12-11 |
| 18 | [WhatsApp told to stop sharing user data with Facebook by French authorities](https://news.ycombinator.com/item?id=15960747) | 法国监管部门要求 WhatsApp 停止与 Facebook 共享用户数据。 | 795 | 408 | 2017-12-19 |
| 19 | [Microsoft Adds an OpenSSH Client to Windows 10](https://news.ycombinator.com/item?id=15904265) | 微软向 Windows 10 加入 OpenSSH 客户端。 | 793 | 522 | 2017-12-12 |
| 20 | [Project Euler](https://news.ycombinator.com/item?id=15893911) | 认识数学与编程练习平台 Project Euler。 | 792 | 163 | 2017-12-10 |

## 2018-01

有效主帖 24,118 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Reading privileged memory with a side-channel](https://news.ycombinator.com/item?id=16065845) | 研究者展示利用旁路信息读取特权内存的攻击方式。 | 2334 | 593 | 2018-01-03 |
| 2 | [Linus Torvalds: “Somebody is pushing complete garbage for unclear reasons.”](https://news.ycombinator.com/item?id=16202205) | Linus Torvalds 以激烈措辞批评有人出于不明原因推动糟糕的代码。 | 1854 | 656 | 2018-01-22 |
| 3 | [Why Raspberry Pi Isn't Vulnerable to Spectre or Meltdown](https://news.ycombinator.com/item?id=16080002) | 解释 Raspberry Pi 为何不受 Spectre 与 Meltdown 漏洞影响。 | 1603 | 215 | 2018-01-05 |
| 4 | [Google Memory Loss](https://news.ycombinator.com/item?id=16153840) | 作者以“Google 失去记忆”为题，关注该服务保留和查找历史信息的能力。 | 1377 | 539 | 2018-01-15 |
| 5 | [Mozilla Files Suit Against FCC to Protect Net Neutrality](https://news.ycombinator.com/item?id=16163189) | Mozilla 起诉美国 FCC，以维护网络中立性。 | 1360 | 186 | 2018-01-16 |
| 6 | [Montana becomes first state to implement net neutrality after FCC repeal](https://news.ycombinator.com/item?id=16207346) | FCC 废除相关规则后，Montana 成为首个自行实施网络中立性的州。 | 1224 | 153 | 2018-01-22 |
| 7 | [Ursula Le Guin has died](https://news.ycombinator.com/item?id=16218439) | 作家 Ursula Le Guin 去世。 | 1125 | 188 | 2018-01-23 |
| 8 | [Amazon, Berkshire, JPMorgan to Create Healthcare Company](https://news.ycombinator.com/item?id=16264662) | Amazon、Berkshire Hathaway 与 JPMorgan 将合作创立医疗保健公司。 | 1070 | 520 | 2018-01-30 |
| 9 | [Intel Confronts Potential ‘PR Nightmare’ With Reported Chip Flaw](https://news.ycombinator.com/item?id=16060855) | 处理器漏洞消息曝光，Intel 面临潜在的公关危机。 | 1026 | 543 | 2018-01-03 |
| 10 | [Aaron, 5 years later](https://news.ycombinator.com/item?id=16141013) | 在五年之后，再次回望 Aaron 的故事。 | 1009 | 108 | 2018-01-13 |
| 11 | [Red Hat to Acquire CoreOS](https://news.ycombinator.com/item?id=16269161) | Red Hat 宣布收购 CoreOS。 | 997 | 197 | 2018-01-30 |
| 12 | [The Death of Microservice Madness in 2018](https://news.ycombinator.com/item?id=16200007) | 作者反思微服务热潮，并预测二〇一八年将告别盲目追逐。 | 993 | 441 | 2018-01-21 |
| 13 | [Ending Bitcoin Support](https://news.ycombinator.com/item?id=16216329) | 服务方宣布终止对比特币的支持。 | 989 | 625 | 2018-01-23 |
| 14 | [The mysterious case of the Linux Page Table Isolation patches](https://news.ycombinator.com/item?id=16046636) | 追查 Linux 页表隔离补丁背后的神秘变化。 | 988 | 254 | 2018-01-01 |
| 15 | [An Experimental Course on Operating Systems](https://news.ycombinator.com/item?id=16134618) | 介绍一门采用实验性方式教授操作系统的课程。 | 967 | 243 | 2018-01-12 |
| 16 | [Start Your Own ISP](https://news.ycombinator.com/item?id=16160394) | 提供创办自己的互联网接入服务商的指南。 | 938 | 193 | 2018-01-16 |
| 17 | [Firefox’s new streaming and tiering compiler](https://news.ycombinator.com/item?id=16169236) | 介绍 Firefox 新增的流式编译与分层编译机制。 | 912 | 220 | 2018-01-17 |
| 18 | [JS Paint – A web-based MS Paint remake](https://news.ycombinator.com/item?id=16174478) | JS Paint 在网页中重现经典 MS Paint 绘图工具。 | 906 | 248 | 2018-01-18 |
| 19 | [A letter about Google AMP](https://news.ycombinator.com/item?id=16108553) | 一封关于 Google AMP 的公开信。 | 866 | 346 | 2018-01-09 |
| 20 | [“My ten hour white noise video now has five copyright claims”](https://news.ycombinator.com/item?id=16075325) | 作者称，自己制作的十小时白噪声视频遭到了五项版权主张。 | 860 | 241 | 2018-01-05 |

## 2018-02

有效主帖 21,859 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [SpaceX’s Falcon Heavy successfully launches](https://news.ycombinator.com/item?id=16319505) | SpaceX 的 Falcon Heavy 重型火箭成功发射。 | 2968 | 871 | 2018-02-06 |
| 2 | [Why I Quit Google to Work for Myself](https://news.ycombinator.com/item?id=16483241) | 作者解释为何离开 Google，转而为自己工作。 | 1767 | 751 | 2018-02-28 |
| 3 | [John Perry Barlow has died](https://news.ycombinator.com/item?id=16328546) | 互联网先驱 John Perry Barlow 去世。 | 1485 | 126 | 2018-02-07 |
| 4 | [Signal Foundation](https://news.ycombinator.com/item?id=16431800) | Signal 宣布成立基金会。 | 1314 | 284 | 2018-02-21 |
| 5 | [Email is your electronic memory](https://news.ycombinator.com/item?id=16380345) | 作者把电子邮件视为个人的电子记忆。 | 1248 | 282 | 2018-02-14 |
| 6 | [Show HN: Six Degrees of Wikipedia](https://news.ycombinator.com/item?id=16468196) | 用“维基百科的六度分隔”项目探索条目之间的联系。 | 1176 | 324 | 2018-02-26 |
| 7 | [AMP for email is a terrible idea](https://news.ycombinator.com/item?id=16372234) | 作者认为，把 AMP 引入电子邮件是一个糟糕的主意。 | 1151 | 465 | 2018-02-14 |
| 8 | [Ask HN: What has HN given you?](https://news.ycombinator.com/item?id=16409768) | HN 用户分享社区带给自己的机会、见解与收获。 | 1095 | 570 | 2018-02-19 |
| 9 | [OpenStreetMap Is in Trouble](https://news.ycombinator.com/item?id=16394604) | 作者警告，OpenStreetMap 正面临问题。 | 1062 | 284 | 2018-02-16 |
| 10 | [Why I don't use my real photo when messaging with customers on my website](https://news.ycombinator.com/item?id=16389666) | 作者解释，在网站上与客户沟通时为何不使用自己的真实照片。 | 1016 | 612 | 2018-02-16 |
| 11 | [Let's Learn About Waveforms](https://news.ycombinator.com/item?id=16378458) | 通过入门介绍理解波形。 | 989 | 128 | 2018-02-14 |
| 12 | [JupyterLab is ready for users](https://news.ycombinator.com/item?id=16420142) | JupyterLab 宣布已准备好供用户使用。 | 958 | 248 | 2018-02-20 |
| 13 | [Cancer ‘vaccine’ eliminates tumors in mice](https://news.ycombinator.com/item?id=16279856) | 一项小鼠实验显示，研究中的癌症“疫苗”消除了肿瘤。 | 942 | 173 | 2018-02-01 |
| 14 | [Apple confirms it uses Google cloud for some of iCloud](https://news.ycombinator.com/item?id=16465315) | Apple 确认，部分 iCloud 服务使用 Google Cloud。 | 912 | 222 | 2018-02-26 |
| 15 | [Let’s talk about usernames](https://news.ycombinator.com/item?id=16356397) | 围绕用户名的选择与设计，讨论容易被忽略的问题。 | 900 | 429 | 2018-02-12 |
| 16 | [Show HN: Hacker News Classics](https://news.ycombinator.com/item?id=16442888) | 展示一个汇集 Hacker News 经典内容的项目。 | 864 | 107 | 2018-02-23 |
| 17 | [The Business of SaaS](https://news.ycombinator.com/item?id=16421438) | 介绍软件即服务业务的商业模式。 | 845 | 248 | 2018-02-20 |
| 18 | ["Pwned Passwords" V2 With Half a Billion Passwords](https://news.ycombinator.com/item?id=16432344) | Pwned Passwords 推出第二版，收录约五亿条泄露密码。 | 842 | 355 | 2018-02-21 |
| 19 | [VLC 3.0 release](https://news.ycombinator.com/item?id=16340741) | VLC 媒体播放器发布 3.0 版本。 | 827 | 294 | 2018-02-09 |
| 20 | [Chrome 68 will mark all HTTP sites as “not secure”](https://news.ycombinator.com/item?id=16334241) | Chrome 68 将把所有 HTTP 网站标记为“不安全”。 | 806 | 812 | 2018-02-08 |

## 2018-03

有效主帖 24,676 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Stephen Hawking has died](https://news.ycombinator.com/item?id=16582136) | 物理学家 Stephen Hawking 去世。 | 6015 | 436 | 2018-03-14 |
| 2 | [Self-driving Uber car kills Arizona woman crossing street](https://news.ycombinator.com/item?id=16619917) | Uber 自动驾驶汽车在亚利桑那州撞死一名正在过街的女性。 | 2361 | 1766 | 2018-03-19 |
| 3 | [Machine Learning Crash Course](https://news.ycombinator.com/item?id=16493489) | Google 提供机器学习速成课程。 | 1926 | 222 | 2018-03-01 |
| 4 | [Congrats Dropbox](https://news.ycombinator.com/item?id=16659180) | Y Combinator 向 Dropbox 送上祝贺。 | 1543 | 264 | 2018-03-23 |
| 5 | [It's time to head back to RSS?](https://news.ycombinator.com/item?id=16721690) | 面对如今的网络环境，是时候重新使用 RSS 阅读了吗？ | 1501 | 491 | 2018-03-31 |
| 6 | [Two Photographers Unknowingly Shot the Same Millisecond in Time](https://news.ycombinator.com/item?id=16542395) | 两位摄影师在不知情的情况下，拍到了同一毫秒的瞬间。 | 1397 | 215 | 2018-03-08 |
| 7 | [Elon Musk Deletes Own, SpaceX and Tesla Facebook Pages After #deletefacebook](https://news.ycombinator.com/item?id=16659656) | Elon Musk 在删除 Facebook 的呼吁中，移除了个人、SpaceX 与 Tesla 的主页。 | 1390 | 499 | 2018-03-23 |
| 8 | [Blocklist Facebook domains](https://news.ycombinator.com/item?id=16632677) | 一份用于屏蔽 Facebook 相关域名的清单。 | 1349 | 348 | 2018-03-20 |
| 9 | [Theranos, CEO Holmes, and Former President Balwani Charged with Fraud](https://news.ycombinator.com/item?id=16585892) | Theranos、首席执行官 Holmes 与前总裁 Balwani 被指控欺诈。 | 1211 | 516 | 2018-03-14 |
| 10 | [Facebook Secretly Saved Videos Users Deleted](https://news.ycombinator.com/item?id=16724962) | 报道 Facebook 秘密保留了用户已经删除的视频。 | 1187 | 387 | 2018-03-31 |
| 11 | [“Pinterest needs to be removed from Google IMO”](https://news.ycombinator.com/item?id=16613996) | 一位用户主张，Google 搜索结果应移除 Pinterest。 | 1155 | 268 | 2018-03-18 |
| 12 | [Fred's ImageMagick Scripts](https://news.ycombinator.com/item?id=16668254) | Fred 整理的一套 ImageMagick 图像处理脚本。 | 1149 | 100 | 2018-03-24 |
| 13 | [Tell HN: Slack decides to close down IRC and XMPP gateways](https://news.ycombinator.com/item?id=16539857) | Slack 决定关闭 IRC 与 XMPP 网关，称其已难以满足功能与安全需求。 | 1148 | 600 | 2018-03-07 |
| 14 | [Tempe Police Release Video of Uber Accident](https://news.ycombinator.com/item?id=16643056) | Tempe 警方公布 Uber 事故视频。 | 1108 | 1323 | 2018-03-21 |
| 15 | [FTC Probing Facebook for Use of Personal Data, Source Says](https://news.ycombinator.com/item?id=16628347) | 消息人士称，美国 FTC 正调查 Facebook 对个人数据的使用。 | 1107 | 371 | 2018-03-20 |
| 16 | [Show HN: RoughJS – Create hand-drawn graphics using JavaScript](https://news.ycombinator.com/item?id=16571827) | RoughJS 让开发者用 JavaScript 创建手绘风格图形。 | 1087 | 92 | 2018-03-12 |
| 17 | [WhatsApp co-founder tells everyone to delete Facebook](https://news.ycombinator.com/item?id=16633774) | WhatsApp 联合创始人呼吁用户删除 Facebook。 | 1086 | 628 | 2018-03-20 |
| 18 | [Facebook Security Chief Said to Leave After Clashes Over Disinformation](https://news.ycombinator.com/item?id=16623835) | 据报道，Facebook 安全负责人因虚假信息问题上的分歧而准备离职。 | 1074 | 395 | 2018-03-19 |
| 19 | [Facebook’s tracking of non-users ruled illegal again in Europe](https://news.ycombinator.com/item?id=16517918) | Facebook 追踪非用户的行为再次在欧洲被判违法。 | 1034 | 379 | 2018-03-05 |
| 20 | [ACME v2 and Wildcard Certificate Support is Live](https://news.ycombinator.com/item?id=16577714) | ACME v2 与通配符证书支持正式上线。 | 1024 | 310 | 2018-03-13 |

## 2018-04

有效主帖 23,403 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Apple open-sources FoundationDB](https://news.ycombinator.com/item?id=16877395) | Apple 宣布将 FoundationDB 开源。 | 2136 | 441 | 2018-04-19 |
| 2 | [1.1.1.1: Fast, privacy-first consumer DNS service](https://news.ycombinator.com/item?id=16727869) | Cloudflare 推出 1.1.1.1，强调速度与隐私的公众 DNS 服务。 | 1895 | 657 | 2018-04-01 |
| 3 | [Ask HN: How to self-learn electronics?](https://news.ycombinator.com/item?id=16775744) | HN 用户征集自学电子技术的方法与资源。 | 1681 | 302 | 2018-04-06 |
| 4 | [Ask HN: What are the best MOOCs you've taken?](https://news.ycombinator.com/item?id=16745042) | HN 用户推荐自己上过的优质大规模开放在线课程。 | 1665 | 315 | 2018-04-03 |
| 5 | [Google Workers Urge C.E.O. To Pull Out of Pentagon A.I. Project](https://news.ycombinator.com/item?id=16755530) | Google 员工敦促首席执行官退出五角大楼的人工智能项目。 | 1368 | 1061 | 2018-04-04 |
| 6 | [Apple Plans to Use Its Own Chips in Macs from 2020, Replacing Intel](https://news.ycombinator.com/item?id=16737072) | 据报道，Apple 计划从二〇二〇年起用自研芯片替换 Mac 中的 Intel 处理器。 | 1302 | 1111 | 2018-04-02 |
| 7 | [Facebook Container for Firefox](https://news.ycombinator.com/item?id=16862925) | Firefox 提供 Facebook Container 扩展。 | 1274 | 394 | 2018-04-17 |
| 8 | [Productivity](https://news.ycombinator.com/item?id=16802530) | 作者分享关于提高生产力的思考。 | 1264 | 399 | 2018-04-10 |
| 9 | [Comcast, AT&T and Verizon pose a greater surveillance risk than Facebook](https://news.ycombinator.com/item?id=16775093) | 作者认为，Comcast、AT&T 与 Verizon 带来的监控风险超过 Facebook。 | 1075 | 276 | 2018-04-06 |
| 10 | [You probably don't need AI/ML. You can make do with well written SQL scripts](https://news.ycombinator.com/item?id=16898827) | 作者建议，许多任务用写好的 SQL 脚本即可完成，无需采用人工智能。 | 1075 | 322 | 2018-04-22 |
| 11 | [I wandered off and built an IDE](https://news.ycombinator.com/item?id=16772276) | 作者讲述自己不知不觉开发出一个集成开发环境的经历。 | 1053 | 256 | 2018-04-06 |
| 12 | [Hijack of Amazon’s domain service used to reroute web traffic for two hours](https://news.ycombinator.com/item?id=16914698) | Amazon 域名服务遭劫持，网页流量被重定向长达两小时。 | 1048 | 284 | 2018-04-24 |
| 13 | [The dots do matter: how to scam a Gmail user](https://news.ycombinator.com/item?id=16781959) | 研究 Gmail 地址中的点号如何被利用来欺骗用户。 | 1023 | 506 | 2018-04-07 |
| 14 | [EU agrees on total ban of bee-harming pesticides](https://news.ycombinator.com/item?id=16939619) | 欧盟同意全面禁止危害蜜蜂的农药。 | 1022 | 314 | 2018-04-27 |
| 15 | [Medicare will require hospitals to post prices online](https://news.ycombinator.com/item?id=16922396) | Medicare 将要求医院把价格公布到网上。 | 1015 | 544 | 2018-04-25 |
| 16 | [AV1: A new general-purpose video codec](https://news.ycombinator.com/item?id=16796127) | 介绍新的通用视频编码格式 AV1。 | 909 | 243 | 2018-04-09 |
| 17 | [IBM is not doing "cognitive computing" with Watson (2016)](https://news.ycombinator.com/item?id=16959188) | 作者质疑 IBM 对 Watson 的宣传，认为其并非在做“认知计算”。 | 904 | 435 | 2018-04-30 |
| 18 | [Dumber phone](https://news.ycombinator.com/item?id=16912679) | 围绕让手机变得更简单的想法，反思智能手机的使用。 | 895 | 343 | 2018-04-24 |
| 19 | [Non-profit’s $300 hepatitis C cure as effective as $84k alternative](https://news.ycombinator.com/item?id=16818593) | 一家非营利机构的三百美元丙肝疗法，被报道与八万四千美元的方案同样有效。 | 874 | 295 | 2018-04-12 |
| 20 | [DNS Performance compared: CloudFlare 1.1.1.1 x Google 8.8.8.8 x Quad9 x OpenDNS](https://news.ycombinator.com/item?id=16732820) | 比较 Cloudflare、Google、Quad9 与 OpenDNS 的 DNS 解析性能。 | 860 | 311 | 2018-04-02 |

## 2018-05

有效主帖 24,015 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Conversations with a six-year-old on functional programming](https://news.ycombinator.com/item?id=17015661) | 作者记录与一个六岁孩子谈论函数式编程的对话。 | 2074 | 310 | 2018-05-07 |
| 2 | [Google Duplex: An AI System for Accomplishing Real World Tasks Over the Phone](https://news.ycombinator.com/item?id=17022963) | Google Duplex 利用人工智能打电话，尝试完成现实世界的任务。 | 1875 | 750 | 2018-05-08 |
| 3 | [US cell carriers are selling access to real-time phone location data](https://news.ycombinator.com/item?id=17081684) | 报道美国移动运营商出售实时手机位置数据的访问权。 | 1630 | 625 | 2018-05-16 |
| 4 | [The Stuxnet worm may be the most sophisticated software ever written](https://news.ycombinator.com/item?id=17099969) | 作者认为，Stuxnet 蠕虫可能是有史以来最复杂的软件之一。 | 1493 | 481 | 2018-05-18 |
| 5 | [Reddit just passed Facebook as #3 most popular website in US](https://news.ycombinator.com/item?id=17189905) | 网站排名数据显示，Reddit 超过 Facebook，成为美国第三受欢迎的网站。 | 1361 | 584 | 2018-05-30 |
| 6 | [The Importance of Deep Work and the 30-Hour Method for Learning a New Skill](https://news.ycombinator.com/item?id=17163251) | 讨论深度工作的意义，并介绍学习新技能的三十小时方法。 | 1331 | 197 | 2018-05-26 |
| 7 | [Amazon device recorded private conversation, sent it out to random contact](https://news.ycombinator.com/item?id=17145204) | 一台 Amazon 设备被曝录下私人对话，并发送给通讯录中的其他联系人。 | 1314 | 710 | 2018-05-24 |
| 8 | [Google YOLO clickjacking](https://news.ycombinator.com/item?id=17044518) | 研究者展示 Google YOLO 相关的点击劫持问题。 | 1304 | 229 | 2018-05-11 |
| 9 | [Amazon threatens to suspend Signal's AWS account over censorship circumvention](https://news.ycombinator.com/item?id=16970199) | Amazon 因 Signal 使用规避审查的手段，威胁暂停其 AWS 账户。 | 1224 | 496 | 2018-05-01 |
| 10 | [LocationSmart Leaked Location Data for All Major U.S. Carriers in Real Time](https://news.ycombinator.com/item?id=17094213) | LocationSmart 被发现泄露美国主要移动运营商用户的实时位置数据。 | 1209 | 270 | 2018-05-17 |
| 11 | [Completely Silent Computer](https://news.ycombinator.com/item?id=17075489) | 介绍一台追求完全静音的电脑。 | 1087 | 489 | 2018-05-15 |
| 12 | [John Carmack: My Steve Jobs Stories](https://news.ycombinator.com/item?id=17066846) | John Carmack 回忆自己与 Steve Jobs 有关的故事。 | 1075 | 366 | 2018-05-14 |
| 13 | [AT&T updates firmware to block access to 1.1.1.1](https://news.ycombinator.com/item?id=16980292) | 用户报告，AT&T 的固件更新阻止了对 1.1.1.1 的访问。 | 999 | 367 | 2018-05-02 |
| 14 | [AI winter is well on its way](https://news.ycombinator.com/item?id=17184054) | 作者判断，新一轮人工智能寒冬正在到来。 | 993 | 492 | 2018-05-30 |
| 15 | [How to Come Up with Profitable Business Ideas](https://news.ycombinator.com/item?id=17102981) | 分享如何寻找有盈利可能的商业创意。 | 986 | 143 | 2018-05-18 |
| 16 | [Bitcoin Gold Hit by Double Spend Attack, Exchanges Lose Millions](https://news.ycombinator.com/item?id=17138356) | Bitcoin Gold 遭双花攻击，交易所损失数百万美元。 | 973 | 531 | 2018-05-23 |
| 17 | [Seaweed in Cow Feed Reduces Methane Emissions Almost Entirely](https://news.ycombinator.com/item?id=17036221) | 报道在牛饲料中添加海藻，几乎可以消除其甲烷排放。 | 915 | 264 | 2018-05-10 |
| 18 | [Please Stop Using Adblock (But Not Why You Think)](https://news.ycombinator.com/item?id=16997272) | 作者呼吁停止使用 Adblock，并解释与读者直觉不同的理由。 | 910 | 384 | 2018-05-04 |
| 19 | [Safe ways to do things in bash](https://news.ycombinator.com/item?id=17057596) | 介绍在 Bash 中更安全地完成常见操作的方法。 | 892 | 240 | 2018-05-13 |
| 20 | [I've spent the last two years building a new email client](https://news.ycombinator.com/item?id=16975096) | 作者展示自己花两年时间开发的新邮件客户端。 | 874 | 593 | 2018-05-02 |

## 2018-06

有效主帖 22,715 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Microsoft Is Said to Have Agreed to Acquire GitHub](https://news.ycombinator.com/item?id=17221527) | 据报道，微软已经同意收购 GitHub。 | 2873 | 1436 | 2018-06-03 |
| 2 | [GitLab sees huge spike in project imports](https://news.ycombinator.com/item?id=17223116) | GitLab 观察到导入项目数量大幅增加。 | 1736 | 455 | 2018-06-03 |
| 3 | [How to be a Manager – A step-by-step guide to leading a team](https://news.ycombinator.com/item?id=17238135) | 一份逐步讲解如何带领团队的经理入门指南。 | 1631 | 224 | 2018-06-05 |
| 4 | [Firefox is back. It's time to give it a try](https://news.ycombinator.com/item?id=17361168) | 作者认为 Firefox 已经回归，建议读者重新尝试。 | 1558 | 722 | 2018-06-21 |
| 5 | [Hello, GitHub](https://news.ycombinator.com/item?id=17230273) | 一篇向 GitHub 社区打招呼的公开文字。 | 1498 | 644 | 2018-06-04 |
| 6 | [Blender is testing PeerTube after YouTube blocks their videos worldwide](https://news.ycombinator.com/item?id=17347560) | YouTube 在全球屏蔽 Blender 视频后，团队开始测试 PeerTube。 | 1473 | 426 | 2018-06-19 |
| 7 | [The Machine Fired Me](https://news.ycombinator.com/item?id=17350645) | 作者讲述自己被自动化系统“解雇”的经历。 | 1471 | 554 | 2018-06-19 |
| 8 | [Twitter ‘smytes’ customers](https://news.ycombinator.com/item?id=17371074) | Twitter 与 Smyte 相关变动给现有客户带来的冲击。 | 1422 | 551 | 2018-06-22 |
| 9 | [Supreme Court Rules Police Need Warrant to Track Your Cellphone](https://news.ycombinator.com/item?id=17374440) | 美国最高法院裁定，警方追踪手机位置需要取得搜查令。 | 1301 | 265 | 2018-06-22 |
| 10 | [Apple Engineers Its Own Downfall with the Macbook Pro Keyboard](https://news.ycombinator.com/item?id=17413572) | 作者批评 MacBook Pro 键盘设计，认为它正在损害 Apple 自身。 | 1183 | 897 | 2018-06-28 |
| 11 | [Alternatives to Google Products](https://news.ycombinator.com/item?id=17280558) | 整理可替代 Google 各项产品的服务。 | 1169 | 504 | 2018-06-10 |
| 12 | [Microsoft acquires Github](https://news.ycombinator.com/item?id=17227286) | 微软正式宣布收购 GitHub。 | 1161 | 798 | 2018-06-04 |
| 13 | [Ask HN: Pros and cons of working at a startup in 2018?](https://news.ycombinator.com/item?id=17286939) | YC 合伙人向社区征集二〇一八年在创业公司工作的优点与缺点。 | 1139 | 939 | 2018-06-11 |
| 14 | [YouTube’s Piracy Filter Blocks MIT Courses, Blender Videos, and More](https://news.ycombinator.com/item?id=17338700) | YouTube 的反盗版过滤系统屏蔽了 MIT 课程、Blender 视频等内容。 | 1129 | 250 | 2018-06-18 |
| 15 | [Why nobody ever wins the car at the mall](https://news.ycombinator.com/item?id=17392995) | 商场里的赠车抽奖为何似乎总是无人中奖？ | 1104 | 447 | 2018-06-25 |
| 16 | [Things I Regret About Node.js [video]](https://news.ycombinator.com/item?id=17247135) | 一段谈论 Node.js 设计中令人遗憾之处的演讲。 | 994 | 491 | 2018-06-06 |
| 17 | [Earliest images of the moon were better than people realised](https://news.ycombinator.com/item?id=17311005) | 早期月球影像的质量，可能比人们原先以为的更好。 | 976 | 194 | 2018-06-14 |
| 18 | [Remote Only](https://news.ycombinator.com/item?id=17251471) | 介绍以完全远程工作为主题的 Remote Only 项目。 | 938 | 361 | 2018-06-06 |
| 19 | [Ask HN: What are the things that you have automated in your personal life?](https://news.ycombinator.com/item?id=17385291) | HN 用户分享自己在个人生活中实现自动化的事情。 | 897 | 731 | 2018-06-24 |
| 20 | [Why you should not use Google Cloud](https://news.ycombinator.com/item?id=17431609) | 作者解释为何建议不要使用 Google Cloud。 | 895 | 357 | 2018-06-30 |

## 2018-07

有效主帖 22,450 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [“I'm basically giving myself a permanent vacation from being BDFL”](https://news.ycombinator.com/item?id=17515492) | 一位项目领导者宣布，不再担任“仁慈的终身独裁者”角色。 | 2024 | 721 | 2018-07-12 |
| 2 | [EU copyright law proposal rejected](https://news.ycombinator.com/item?id=17462089) | 欧盟版权法提案遭到否决。 | 1847 | 314 | 2018-07-05 |
| 3 | [Farewell, Google Maps](https://news.ycombinator.com/item?id=17570029) | 作者宣布告别 Google Maps，并说明这一选择。 | 1747 | 527 | 2018-07-19 |
| 4 | [Goodbye Microservices: From 100s of problem children to 1 superstar](https://news.ycombinator.com/item?id=17499137) | 团队告别微服务，把数百个问题服务整合为一个系统。 | 1277 | 753 | 2018-07-10 |
| 5 | [Learn how to design large-scale systems](https://news.ycombinator.com/item?id=17522362) | 一份帮助学习大规模系统设计的资料。 | 1273 | 185 | 2018-07-13 |
| 6 | [Founder to CEO: How to build a great company from the ground up](https://news.ycombinator.com/item?id=17446839) | 面向从创始人走向首席执行官的转变，介绍如何从零建立公司。 | 1207 | 245 | 2018-07-03 |
| 7 | [Liquid water 'lake' revealed on Mars](https://news.ycombinator.com/item?id=17609327) | 火星上被报告发现可能含有液态水的“湖”。 | 1104 | 472 | 2018-07-25 |
| 8 | [California law requires businesses to let you cancel your subscription online](https://news.ycombinator.com/item?id=17465812) | 加州法律要求商家允许用户在线取消订阅。 | 1070 | 536 | 2018-07-05 |
| 9 | [Amazon Dark Patterns](https://news.ycombinator.com/item?id=17651488) | 分析 Amazon 界面中诱导用户作出不利选择的设计。 | 1056 | 272 | 2018-07-31 |
| 10 | [The Bullshit Web](https://news.ycombinator.com/item?id=17655089) | 作者批评当今网络中充斥的糟糕体验。 | 1017 | 550 | 2018-07-31 |
| 11 | [Slack Is Buying HipChat from Atlassian](https://news.ycombinator.com/item?id=17620543) | Slack 宣布从 Atlassian 收购 HipChat。 | 1006 | 710 | 2018-07-26 |
| 12 | [A bootable CD image with a retro game in a single tweet](https://news.ycombinator.com/item?id=17656299) | 把包含复古游戏的可启动光盘镜像压缩进一条推文。 | 1004 | 140 | 2018-07-31 |
| 13 | [Thailand cave rescue: all 12 boys and coach successfully rescued](https://news.ycombinator.com/item?id=17497410) | 泰国洞穴救援成功，十二名男孩与教练全部获救。 | 971 | 540 | 2018-07-10 |
| 14 | [Show HN: Browsh – A modern, text-based browser](https://news.ycombinator.com/item?id=17487552) | Browsh 是一款面向现代网页的文字浏览器。 | 967 | 322 | 2018-07-09 |
| 15 | [Please stop asking me to use the app](https://news.ycombinator.com/item?id=17446790) | 用户呼吁网站停止反复要求自己改用应用。 | 929 | 253 | 2018-07-03 |
| 16 | [European Commission fines Google €4.34B in Android antitrust case](https://news.ycombinator.com/item?id=17556497) | 欧盟委员会在 Android 反垄断案中，对 Google 处以四十三点四亿欧元罚款。 | 921 | 918 | 2018-07-18 |
| 17 | [MacBook Pro with faster performance and new features for pros](https://news.ycombinator.com/item?id=17513828) | Apple 更新 MacBook Pro，提升性能并增加面向专业用户的功能。 | 889 | 1173 | 2018-07-12 |
| 18 | [People Aren’t Dumb, the World Is Hard](https://news.ycombinator.com/item?id=17513959) | 作者提出，错误判断常常源于世界复杂，而不能简单归咎于人愚蠢。 | 868 | 425 | 2018-07-12 |
| 19 | [YC Startup School 2018: a free, 10-week, online course](https://news.ycombinator.com/item?id=17558452) | YC Startup School 推出为期十周的免费在线创业课程。 | 850 | 180 | 2018-07-18 |
| 20 | [Teenager Finds Classical Alternative to Quantum Recommendation Algorithm](https://news.ycombinator.com/item?id=17654220) | 一位青少年找到量子推荐算法的经典计算替代方案。 | 824 | 216 | 2018-07-31 |

## 2018-08

有效主帖 23,898 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Docker cannot be downloaded without logging into Docker Store](https://news.ycombinator.com/item?id=17804916) | 用户发现，下载 Docker 前必须先登录 Docker Store。 | 1620 | 421 | 2018-08-20 |
| 2 | [Let's Encrypt Root Trusted by All Major Root Programs](https://news.ycombinator.com/item?id=17698264) | Let's Encrypt 根证书获得所有主流根证书计划的信任。 | 1532 | 144 | 2018-08-06 |
| 3 | [Thank you HN](https://news.ycombinator.com/item?id=17745688) | 曾因抑郁向 HN 求助的用户回来致谢，表示社区的善意帮助自己走出困境。 | 1370 | 137 | 2018-08-12 |
| 4 | [Intel Publishes Microcode Patches, No Benchmarking or Comparison Allowed](https://news.ycombinator.com/item?id=17824218) | Intel 发布微码补丁，其许可证却禁止进行基准测试或比较。 | 1318 | 484 | 2018-08-23 |
| 5 | [Academic Torrents – Making 27TB of research data available](https://news.ycombinator.com/item?id=17744150) | Academic Torrents 公开提供二十七 TB 研究数据。 | 1082 | 140 | 2018-08-12 |
| 6 | [Show HN: I'm 12, learning JS, and wrote Wolfram's cellular automaton in Node](https://news.ycombinator.com/item?id=17871313) | 一位十二岁的 JavaScript 学习者展示用 Node.js 编写的 Wolfram 元胞自动机。 | 1072 | 283 | 2018-08-29 |
| 7 | [Pandoc](https://news.ycombinator.com/item?id=17855104) | 认识文档转换工具 Pandoc。 | 1016 | 204 | 2018-08-27 |
| 8 | [Bullshit Jobs](https://news.ycombinator.com/item?id=17874320) | 围绕“狗屁工作”这一概念，反思工作的必要性与意义。 | 964 | 556 | 2018-08-30 |
| 9 | [Google AMP – A 70% drop in our conversion rate](https://news.ycombinator.com/item?id=17717241) | 作者称，采用 Google AMP 后，自己的转化率下降了百分之七十。 | 948 | 386 | 2018-08-08 |
| 10 | [Former Tesla Firmware Engineer Discusses the System](https://news.ycombinator.com/item?id=17835760) | 一名前 Tesla 固件工程师谈论该公司的系统。 | 948 | 555 | 2018-08-24 |
| 11 | [NYU Makes Tuition Free for All Medical Students](https://news.ycombinator.com/item?id=17775906) | 纽约大学宣布为所有医学生免除学费。 | 931 | 507 | 2018-08-16 |
| 12 | [Julia 1.0](https://news.ycombinator.com/item?id=17723404) | Julia 编程语言发布 1.0 版本。 | 915 | 434 | 2018-08-09 |
| 13 | [CLI: Improved](https://news.ycombinator.com/item?id=17874718) | 介绍改进命令行使用体验的工具与方法。 | 913 | 272 | 2018-08-30 |
| 14 | [Go 2 Draft Designs](https://news.ycombinator.com/item?id=17859963) | Go 2 的设计草案公开征求讨论。 | 909 | 473 | 2018-08-28 |
| 15 | [Why Do Keynote Speakers Keep Suggesting That Improving Security Is Possible?](https://news.ycombinator.com/item?id=17785162) | 一场演讲追问，为什么主题演讲者总认为信息安全仍能得到改善？ | 878 | 171 | 2018-08-17 |
| 16 | [Remote Code Execution on a Facebook server](https://news.ycombinator.com/item?id=17834799) | 研究者展示在 Facebook 服务器上执行远程代码的漏洞。 | 877 | 192 | 2018-08-24 |
| 17 | [Changing Our Approach to Anti-Tracking](https://news.ycombinator.com/item?id=17876598) | Mozilla 宣布调整反追踪策略。 | 858 | 371 | 2018-08-30 |
| 18 | [Chemists discover how blue light speeds blindness](https://news.ycombinator.com/item?id=17724995) | 化学研究者探究蓝光加速视力损伤的机制。 | 851 | 332 | 2018-08-09 |
| 19 | [Bye bye BetterSlack](https://news.ycombinator.com/item?id=17869249) | 开发者宣布告别 BetterSlack 项目。 | 839 | 383 | 2018-08-29 |
| 20 | [Valve Rolls Out Wine-Based “Proton” for Running Windows Games on Linux](https://news.ycombinator.com/item?id=17815892) | Valve 推出基于 Wine 的 Proton，帮助在 Linux 上运行 Windows 游戏。 | 819 | 322 | 2018-08-22 |

## 2018-09

有效主帖 21,484 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Linus Torvalds apologizes for his behavior, takes time off](https://news.ycombinator.com/item?id=18000698) | Linus Torvalds 为自己的行为致歉，并宣布暂时休假。 | 2585 | 998 | 2018-09-16 |
| 2 | [Chrome 69 will keep Google Cookies when you tell it to delete all cookies](https://news.ycombinator.com/item?id=18064537) | 用户发现，Chrome 69 在要求删除全部 Cookie 后仍保留 Google 的 Cookie。 | 2364 | 810 | 2018-09-25 |
| 3 | [Why I’m done with Chrome](https://news.ycombinator.com/item?id=18052923) | 作者解释自己为何决定停止使用 Chrome。 | 2357 | 838 | 2018-09-23 |
| 4 | [EU approves internet copyright law, including ‘link tax’ and ‘upload filter’](https://news.ycombinator.com/item?id=17967366) | 欧盟通过互联网版权法，包含“链接税”与“上传过滤器”等条款。 | 1737 | 1009 | 2018-09-12 |
| 5 | [Facebook Network Breach Impacts Up to 50M Users](https://news.ycombinator.com/item?id=18094823) | Facebook 网络遭入侵，最多五千万用户受到影响。 | 1677 | 609 | 2018-09-28 |
| 6 | [Chrome 69: “www.” subdomain missing from URL](https://news.ycombinator.com/item?id=17927972) | Chrome 69 地址栏不再显示网址中的 www 子域名。 | 1572 | 876 | 2018-09-06 |
| 7 | [EU to stop changing the clocks in 2019](https://news.ycombinator.com/item?id=18008993) | 报道欧盟计划于二〇一九年停止季节性调整时钟。 | 1367 | 708 | 2018-09-17 |
| 8 | [Facebook Is Giving Advertisers Access To Your Shadow Contact Information](https://news.ycombinator.com/item?id=18082017) | Facebook 被指向广告商提供用户未主动提交的隐性联系信息。 | 1359 | 458 | 2018-09-27 |
| 9 | [Life in the Spanish city that banned cars](https://news.ycombinator.com/item?id=18014283) | 走进一座禁止汽车通行的西班牙城市，观察当地生活。 | 1240 | 679 | 2018-09-18 |
| 10 | [Microsoft intercepting Firefox, Chrome installation on Windows 10 Insider build](https://news.ycombinator.com/item?id=17967243) | 微软在 Windows 10 预览版本中拦截 Firefox 与 Chrome 的安装过程。 | 1232 | 740 | 2018-09-12 |
| 11 | [DuckDuckGo Traffic](https://news.ycombinator.com/item?id=18100243) | 查看 DuckDuckGo 的访问量数据。 | 1145 | 375 | 2018-09-29 |
| 12 | [Questions](https://news.ycombinator.com/item?id=18105129) | 作者整理自己感兴趣、希望追究答案的问题。 | 1106 | 470 | 2018-09-30 |
| 13 | [Modifications to Google Chromium for removing Google integration](https://news.ycombinator.com/item?id=18053337) | 介绍移除 Google 集成功能的 Chromium 修改项目。 | 1105 | 306 | 2018-09-23 |
| 14 | [Google Dataset Search](https://news.ycombinator.com/item?id=17919297) | Google 推出数据集搜索工具。 | 1035 | 76 | 2018-09-05 |
| 15 | [Google Maps won't let you save home address without allowing all Google tracking](https://news.ycombinator.com/item?id=18070183) | 用户称，Google Maps 要求开启全部 Google 追踪功能，才允许保存家庭地址。 | 996 | 355 | 2018-09-25 |
| 16 | [Show HN: I made a privacy-first minimalist Google Analytics](https://news.ycombinator.com/item?id=18024277) | 作者展示一款注重隐私、设计精简的网站统计工具。 | 968 | 263 | 2018-09-19 |
| 17 | [Found hooked up to my router](https://news.ycombinator.com/item?id=18086418) | 有人发现一个不明设备连接在自己的路由器上，并寻求辨认。 | 965 | 347 | 2018-09-27 |
| 18 | [Amazon is stuffing its search results pages with ads](https://news.ycombinator.com/item?id=17959085) | 报道 Amazon 在搜索结果页中加入越来越多广告。 | 944 | 545 | 2018-09-11 |
| 19 | [Show HN: Sublime Merge – A Git client from the makers of Sublime Text](https://news.ycombinator.com/item?id=18030446) | Sublime Text 团队推出 Git 客户端 Sublime Merge。 | 935 | 351 | 2018-09-20 |
| 20 | [A year later, Equifax has faced little fallout from losing data](https://news.ycombinator.com/item?id=17940943) | 数据泄露一年后，Equifax 被认为几乎没有付出相应代价。 | 934 | 276 | 2018-09-08 |

## 2018-10

有效主帖 24,335 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Paul Allen has died](https://news.ycombinator.com/item?id=18224227) | 微软联合创始人 Paul Allen 去世。 | 2901 | 277 | 2018-10-15 |
| 2 | [IBM acquires Red Hat](https://news.ycombinator.com/item?id=18321884) | IBM 宣布收购 Red Hat。 | 2611 | 1052 | 2018-10-28 |
| 3 | [The Big Hack: How China Used a Tiny Chip to Infiltrate Amazon and Apple](https://news.ycombinator.com/item?id=18138328) | 一篇报道声称，中国利用微型芯片入侵 Amazon 与 Apple 的供应链。 | 2493 | 770 | 2018-10-04 |
| 4 | [Paper Airplane Designs](https://news.ycombinator.com/item?id=18249755) | 浏览不同纸飞机的折叠设计。 | 1753 | 206 | 2018-10-18 |
| 5 | [Shutting Down Google+ for Consumers](https://news.ycombinator.com/item?id=18169243) | Google 宣布关闭面向普通消费者的 Google+ 服务。 | 1613 | 699 | 2018-10-08 |
| 6 | [iPhones are allergic to helium](https://news.ycombinator.com/item?id=18340693) | 研究 iPhone 为何会在接触氦气后发生故障。 | 1289 | 340 | 2018-10-30 |
| 7 | [Facebook exodus: Nearly half of young users have deleted the app](https://news.ycombinator.com/item?id=18328750) | 报道近一半年轻 Facebook 用户曾删除其应用。 | 1213 | 567 | 2018-10-29 |
| 8 | [Carbon Removal Technologies](https://news.ycombinator.com/item?id=18285606) | 介绍从环境中移除碳的技术方向。 | 1187 | 660 | 2018-10-23 |
| 9 | [Every Byte of a TLS Connection Explained and Reproduced](https://news.ycombinator.com/item?id=18200749) | 逐字节解释并重现一次 TLS 连接。 | 1185 | 103 | 2018-10-12 |
| 10 | [How to Get Things Done When You Don't Feel Like It](https://news.ycombinator.com/item?id=18179972) | 没有动力时，如何仍然把事情做完？ | 1165 | 183 | 2018-10-09 |
| 11 | [Copyright Office Ruling Imposes Sweeping Right to Repair Reforms](https://news.ycombinator.com/item?id=18303560) | 美国版权局的裁定推动大范围维修权改革。 | 1064 | 343 | 2018-10-25 |
| 12 | [Coders Automating Their Own Job](https://news.ycombinator.com/item?id=18120322) | 报道程序员如何把自己的工作自动化。 | 991 | 485 | 2018-10-02 |
| 13 | [iPhones are hard to use](https://news.ycombinator.com/item?id=18278510) | 作者认为，iPhone 的使用体验存在令人费解的困难。 | 976 | 636 | 2018-10-22 |
| 14 | [We posed as 100 Senators to run ads on Facebook. Facebook approved all of them](https://news.ycombinator.com/item?id=18339448) | 记者冒充一百名美国参议员投放 Facebook 广告，全部获批。 | 970 | 332 | 2018-10-30 |
| 15 | [What I loved about Paul Allen](https://news.ycombinator.com/item?id=18231961) | 作者追忆 Paul Allen，讲述自己欣赏他的地方。 | 964 | 114 | 2018-10-16 |
| 16 | [Google Exposed User Data, Feared Repercussions of Disclosing to Public](https://news.ycombinator.com/item?id=18169027) | 报道 Google 暴露用户数据后，因担忧影响而未向公众披露。 | 953 | 258 | 2018-10-08 |
| 17 | [With Proton and Steam Play, many Windows games now work on Linux](https://news.ycombinator.com/item?id=18327342) | 借助 Proton 与 Steam Play，许多 Windows 游戏已能在 Linux 上运行。 | 932 | 311 | 2018-10-29 |
| 18 | [How I’ve Attracted the First 500 Paid Users for My SaaS](https://news.ycombinator.com/item?id=18216783) | 作者分享如何为自己的 SaaS 产品吸引最初五百名付费用户。 | 925 | 135 | 2018-10-15 |
| 19 | [In Groundbreaking Decision, Feds Say Hacking DRM to Fix Electronics Is Legal](https://news.ycombinator.com/item?id=18302441) | 美国监管裁定，为维修电子设备而绕过 DRM 可以合法进行。 | 924 | 2 | 2018-10-25 |
| 20 | [Ask HN: Cheap places to live with a good intellectual atmosphere?](https://news.ycombinator.com/item?id=18164189) | 一位湾区工程师征集生活成本较低、同时拥有良好知识氛围的居住地。 | 911 | 1088 | 2018-10-08 |

## 2018-11

有效主帖 22,378 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Google Tried to Patent My Work After a Job Interview](https://news.ycombinator.com/item?id=18566929) | 作者称，Google 在求职面试后试图为自己的工作成果申请专利。 | 1798 | 487 | 2018-11-30 |
| 2 | [We are Google employees – Google must drop Dragonfly](https://news.ycombinator.com/item?id=18542830) | 一群 Google 员工呼吁公司终止 Dragonfly 项目。 | 1652 | 840 | 2018-11-27 |
| 3 | [Apple's New Map](https://news.ycombinator.com/item?id=18358902) | 分析 Apple 新版地图的变化。 | 1250 | 365 | 2018-11-01 |
| 4 | [Story of a failed pentest](https://news.ycombinator.com/item?id=18475438) | 讲述一次未能成功的渗透测试。 | 1147 | 167 | 2018-11-17 |
| 5 | [Backdoor in event-stream library dependency](https://news.ycombinator.com/item?id=18534392) | event-stream 库的依赖中被发现植入后门。 | 1034 | 491 | 2018-11-26 |
| 6 | [Google Container for Firefox – Prevent Google from tracking you around the web](https://news.ycombinator.com/item?id=18566405) | Google Container 为 Firefox 提供隔离机制，阻止 Google 跨站追踪。 | 959 | 290 | 2018-11-30 |
| 7 | [Thank you to dang and sctb](https://news.ycombinator.com/item?id=18512304) | 一位社区成员感谢 dang 与 sctb 在幕后维护 HN 的辛勤工作。 | 950 | 123 | 2018-11-22 |
| 8 | [Boss as a Service – Hire a boss, get stuff done](https://news.ycombinator.com/item?id=18512197) | Boss as a Service 让用户雇一位“老板”，督促自己把事情做完。 | 917 | 276 | 2018-11-22 |
| 9 | [Medium is a poor choice for blogging](https://news.ycombinator.com/item?id=18440756) | 作者解释为何认为 Medium 不适合用来写博客。 | 909 | 374 | 2018-11-13 |
| 10 | [Sr.ht, the hacker's forge, now open for public alpha](https://news.ycombinator.com/item?id=18458908) | 开发协作平台 sr.ht 开放公开 Alpha 测试。 | 892 | 217 | 2018-11-15 |
| 11 | [If you want to understand Silicon Valley, watch Silicon Valley](https://news.ycombinator.com/item?id=18488520) | 作者建议，想理解硅谷可以观看电视剧《硅谷》。 | 855 | 459 | 2018-11-19 |
| 12 | [International System of Units overhauled in historic vote](https://news.ycombinator.com/item?id=18469905) | 一场具有历史意义的投票通过对国际单位制的重新定义。 | 834 | 575 | 2018-11-16 |
| 13 | [GitLab Made $10.5M in Revenue with Every Employee Working from Home](https://news.ycombinator.com/item?id=18441768) | GitLab 在全体员工居家工作的模式下，取得一千零五十万美元营收。 | 833 | 418 | 2018-11-13 |
| 14 | [Go 2, here we come](https://news.ycombinator.com/item?id=18561587) | Go 团队介绍迈向 Go 2 的进展。 | 816 | 516 | 2018-11-29 |
| 15 | [I still miss my headphone jack, and I want it back](https://news.ycombinator.com/item?id=18538881) | 作者表示仍怀念耳机接口，并希望它重新回到设备上。 | 805 | 724 | 2018-11-27 |
| 16 | [Build a do-it-yourself home air purifier for about $25](https://news.ycombinator.com/item?id=18445652) | 用约二十五美元，自己制作家用空气净化器。 | 801 | 342 | 2018-11-13 |
| 17 | [An error message, still found in Windows 10, is a mistake from 1974](https://news.ycombinator.com/item?id=18374305) | Windows 10 仍保留的一条错误提示，被追溯到一九七四年的错误。 | 791 | 252 | 2018-11-04 |
| 18 | [Big List of Naughty Strings](https://news.ycombinator.com/item?id=18466787) | 整理大量容易让软件出现异常的字符串，帮助开发者测试输入处理。 | 780 | 146 | 2018-11-16 |
| 19 | [Google Kubernetes Engine's third consecutive day of service disruption](https://news.ycombinator.com/item?id=18428497) | Google Kubernetes Engine 连续第三天出现服务中断。 | 779 | 407 | 2018-11-11 |
| 20 | [Sales mistakes that software engineers make](https://news.ycombinator.com/item?id=18351891) | 讨论软件工程师在销售过程中容易犯的错误。 | 777 | 201 | 2018-11-01 |

## 2018-12

有效主帖 21,547 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Bye Bye Mongo, Hello Postgres](https://news.ycombinator.com/item?id=18717168) | 团队分享从 MongoDB 迁移到 PostgreSQL 的经历。 | 1562 | 417 | 2018-12-19 |
| 2 | [Please do not attempt to simplify this code](https://news.ycombinator.com/item?id=18772873) | 一段代码中的注释提醒维护者，不要尝试简化其实现。 | 1552 | 627 | 2018-12-27 |
| 3 | [Sandspiel – A falling sand game built in Rust and WebGL](https://news.ycombinator.com/item?id=18696291) | Sandspiel 用 Rust 与 WebGL 构建可交互的落沙游戏。 | 1323 | 185 | 2018-12-17 |
| 4 | [Ask HN: What are your “brain hacks” that help you manage everyday situations?](https://news.ycombinator.com/item?id=18588727) | HN 用户分享帮助自己处理日常问题的思维技巧。 | 1322 | 366 | 2018-12-03 |
| 5 | [Quora User Data Compromised](https://news.ycombinator.com/item?id=18594564) | Quora 披露用户数据遭到泄露。 | 1254 | 505 | 2018-12-04 |
| 6 | [Goodbye, EdgeHTML](https://news.ycombinator.com/item?id=18622516) | 围绕告别 EdgeHTML，反思浏览器引擎的未来。 | 1178 | 657 | 2018-12-06 |
| 7 | [Congress votes to make open government data the default in the United States](https://news.ycombinator.com/item?id=18746132) | 美国国会投票推动政府数据默认开放。 | 1130 | 154 | 2018-12-23 |
| 8 | [Canada has arrested Huawei’s global chief financial officer in Vancouver](https://news.ycombinator.com/item?id=18613124) | 加拿大在温哥华逮捕 Huawei 全球首席财务官。 | 1081 | 586 | 2018-12-05 |
| 9 | [Google transferred ownership of Duck.com to DuckDuckGo](https://news.ycombinator.com/item?id=18663860) | Google 将 Duck.com 域名所有权转交给 DuckDuckGo。 | 1065 | 410 | 2018-12-12 |
| 10 | [Microsoft is building a Chromium browser to replace Edge on Windows 10](https://news.ycombinator.com/item?id=18595069) | 据报道，微软正在开发基于 Chromium 的浏览器，以替换 Windows 10 中的 Edge。 | 1061 | 733 | 2018-12-04 |
| 11 | [JIRA is an antipattern](https://news.ycombinator.com/item?id=18642336) | 作者认为，JIRA 所代表的使用方式是一种反模式。 | 1012 | 367 | 2018-12-09 |
| 12 | [The Yoda of Silicon Valley](https://news.ycombinator.com/item?id=18698651) | 走近一位被称为“硅谷尤达”的人物。 | 976 | 331 | 2018-12-17 |
| 13 | [Robinhood launches 3% checking account](https://news.ycombinator.com/item?id=18672951) | Robinhood 推出宣称利率为百分之三的支票账户。 | 972 | 661 | 2018-12-13 |
| 14 | [Firefox 64 Released](https://news.ycombinator.com/item?id=18657532) | Firefox 发布 64 版本。 | 954 | 513 | 2018-12-11 |
| 15 | [Glitter bomb tricks parcel thieves](https://news.ycombinator.com/item?id=18706193) | 一种会释放亮粉的装置，被用来捉弄偷包裹的人。 | 952 | 886 | 2018-12-18 |
| 16 | [Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares](https://news.ycombinator.com/item?id=18678314) | 一本应用线性代数入门教材，介绍向量、矩阵与最小二乘法。 | 938 | 123 | 2018-12-14 |
| 17 | [A Programmer's Introduction to Mathematics](https://news.ycombinator.com/item?id=18579076) | 面向程序员介绍数学的基本思路。 | 937 | 214 | 2018-12-01 |
| 18 | [Slack closes account of an Iranian user living in Canada](https://news.ycombinator.com/item?id=18724107) | Slack 关闭一名居住在加拿大的伊朗用户账户。 | 902 | 608 | 2018-12-20 |
| 19 | [Facial recognition: It’s time for action](https://news.ycombinator.com/item?id=18629063) | 作者呼吁，针对人脸识别技术应开始采取行动。 | 877 | 270 | 2018-12-07 |
| 20 | [Announcing Open Source of WPF, Windows Forms, and WinUI](https://news.ycombinator.com/item?id=18600950) | 微软宣布将 WPF、Windows Forms 与 WinUI 开源。 | 874 | 375 | 2018-12-04 |

## 2019-01

有效主帖 24,965 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Announcing unlimited free private repos](https://news.ycombinator.com/item?id=18847043) | GitHub 宣布提供数量不受限制的免费私有仓库。 | 2867 | 684 | 2019-01-07 |
| 2 | [Start with a Website, Not a Mobile App](https://news.ycombinator.com/item?id=18824993) | 作者建议创业者先做网站，再考虑移动应用。 | 1620 | 559 | 2019-01-04 |
| 3 | [FaceTime bug lets you hear audio of person you are calling before they pick up](https://news.ycombinator.com/item?id=19022353) | FaceTime 漏洞让呼叫者在对方接听前就能听到其声音。 | 1534 | 429 | 2019-01-28 |
| 4 | [Google proposes changes to Chromium which would disable uBlock Origin](https://news.ycombinator.com/item?id=18973477) | Google 提议修改 Chromium，相关变动可能使 uBlock Origin 失效。 | 1527 | 739 | 2019-01-22 |
| 5 | [Why isn't the internet more fun and weird?](https://news.ycombinator.com/item?id=19038327) | 互联网为什么没有变得更有趣、更古怪？ | 1516 | 588 | 2019-01-30 |
| 6 | [Algorithms, by Jeff Erickson](https://news.ycombinator.com/item?id=18805624) | 阅读 Jeff Erickson 编写的算法教材。 | 1463 | 238 | 2019-01-02 |
| 7 | [Facebook has been paying people to install a “Research” VPN](https://news.ycombinator.com/item?id=19031055) | Facebook 被曝付钱让用户安装名为“研究”的 VPN。 | 1454 | 445 | 2019-01-29 |
| 8 | [Instacart paying 80 cents an hour because worker received a large tip](https://news.ycombinator.com/item?id=19029801) | 一名 Instacart 工作者收到大额小费后，平台支付的时薪被指仅剩八十美分。 | 1320 | 675 | 2019-01-29 |
| 9 | [Why are glasses so expensive? The eyewear industry prefers to keep that blurry](https://news.ycombinator.com/item?id=18980191) | 眼镜为什么如此昂贵，行业又为何不愿把原因说清楚？ | 1158 | 588 | 2019-01-23 |
| 10 | [John C. Bogle Has Died](https://news.ycombinator.com/item?id=18926225) | John C. Bogle 去世的消息。 | 1084 | 200 | 2019-01-16 |
| 11 | [Show HN: I taught my little brother JS, and he made this videogame in a week](https://news.ycombinator.com/item?id=18866500) | 作者教弟弟学习 JavaScript 后，展示他一周内制作的电子游戏。 | 1079 | 270 | 2019-01-09 |
| 12 | [China lands Chang'e-4 on far side of Moon](https://news.ycombinator.com/item?id=18812875) | 中国嫦娥四号成功着陆月球背面。 | 1040 | 226 | 2019-01-03 |
| 13 | [I interviewed at six top companies in Silicon Valley in six days](https://news.ycombinator.com/item?id=18942572) | 作者讲述六天内面试六家硅谷知名公司的经历。 | 1012 | 692 | 2019-01-18 |
| 14 | [Ask HN: How did you decide what problems to solve in your lifetime?](https://news.ycombinator.com/item?id=18837334) | 面对个人兴趣与社会需要，HN 用户讨论如何选择一生要解决的问题。 | 985 | 439 | 2019-01-06 |
| 15 | [When hiring senior engineers, you’re not buying, you’re selling](https://news.ycombinator.com/item?id=18955731) | 作者认为招聘资深工程师时，公司需要主动向候选人展示自身吸引力。 | 973 | 662 | 2019-01-20 |
| 16 | [Notion – All-in-one workspace for notes, tasks, wikis, and databases](https://news.ycombinator.com/item?id=18904648) | Notion 将笔记、任务、知识库与数据库整合进同一个工作空间。 | 970 | 479 | 2019-01-14 |
| 17 | [DuckDuckGo will use Apple Maps](https://news.ycombinator.com/item?id=18912656) | DuckDuckGo 宣布采用 Apple Maps。 | 961 | 468 | 2019-01-15 |
| 18 | [GoDaddy injecting JavaScript into websites and how to stop it](https://news.ycombinator.com/item?id=18894792) | 分析 GoDaddy 向网站注入 JavaScript 的行为，并介绍停止注入的方法。 | 949 | 302 | 2019-01-13 |
| 19 | [Elsevier journal editors resign, start rival open-access journal](https://news.ycombinator.com/item?id=18912321) | Elsevier 一份期刊的编辑集体辞职，另办开放获取期刊。 | 940 | 123 | 2019-01-15 |
| 20 | [Ending our Medium integration](https://news.ycombinator.com/item?id=19034676) | 服务方宣布结束与 Medium 的集成。 | 936 | 367 | 2019-01-30 |

## 2019-02

有效主帖 23,614 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [No Thank You, Mr. Pecker](https://news.ycombinator.com/item?id=19109474) | 作者以“不了，谢谢，Pecker 先生”为题发表公开回应。 | 2444 | 730 | 2019-02-07 |
| 2 | [Reflecting on My Failure to Build a Billion-Dollar Company](https://news.ycombinator.com/item?id=19105733) | 作者反思自己未能建立一家价值十亿美元公司的经历。 | 2101 | 353 | 2019-02-07 |
| 3 | [Ask HN: What books changed the way you think about almost everything?](https://news.ycombinator.com/item?id=19087418) | HN 用户分享那些改变自己看待世界方式的书籍。 | 2009 | 1165 | 2019-02-05 |
| 4 | [UC terminates subscriptions with Elsevier in push for open access](https://news.ycombinator.com/item?id=19273955) | 加州大学为推动开放获取，终止与 Elsevier 的订阅协议。 | 1743 | 233 | 2019-02-28 |
| 5 | [Google terminated our business via our Google Play Developer Account](https://news.ycombinator.com/item?id=19124324) | 团队称，Google 终止其 Play 开发者账户，导致业务被迫中断。 | 1668 | 498 | 2019-02-09 |
| 6 | [U.S. Supreme Court Puts Limits on Police Power to Seize Private Property](https://news.ycombinator.com/item?id=19209957) | 美国最高法院限制警方扣押私人财产的权力。 | 1426 | 423 | 2019-02-20 |
| 7 | [Firefox 66 to block automatically playing audible video and audio](https://news.ycombinator.com/item?id=19077548) | Firefox 66 将阻止带声音的视频与音频自动播放。 | 1415 | 368 | 2019-02-04 |
| 8 | [Some Details of My Personal Infrastructure](https://news.ycombinator.com/item?id=19220889) | 作者介绍自己用于支持日常工作的个人基础设施。 | 1308 | 393 | 2019-02-21 |
| 9 | [Immersive Linear Algebra (2016)](https://news.ycombinator.com/item?id=19264048) | 通过沉浸式教材学习线性代数。 | 1269 | 140 | 2019-02-27 |
| 10 | [Show HN: Make your site’s pages instant in one minute](https://news.ycombinator.com/item?id=19122727) | 展示一款声称只需一分钟部署，就能让网站页面更快响应的工具。 | 1214 | 337 | 2019-02-09 |
| 11 | [Dotfile madness](https://news.ycombinator.com/item?id=19063727) | 作者反思点文件不断增多带来的配置管理问题。 | 1146 | 514 | 2019-02-02 |
| 12 | [If Software Is Funded from a Public Source, Its Code Should Be Open Source](https://news.ycombinator.com/item?id=19077913) | 作者主张，公共资金资助的软件应当开放源代码。 | 1138 | 261 | 2019-02-04 |
| 13 | [Don’t Get Clever with Login Forms](https://news.ycombinator.com/item?id=19171402) | 作者建议，登录表单设计应避免过度炫技。 | 1124 | 506 | 2019-02-15 |
| 14 | [Amazon Pulls Out of Planned New York City Campus](https://news.ycombinator.com/item?id=19163281) | Amazon 取消在纽约市建设园区的计划。 | 1066 | 964 | 2019-02-14 |
| 15 | [MIT Hacker Tools: a lecture series on programmer tools](https://news.ycombinator.com/item?id=19078281) | MIT Hacker Tools 以系列讲座介绍程序员工具。 | 1028 | 79 | 2019-02-04 |
| 16 | [Leukemia Has Won](https://news.ycombinator.com/item?id=19203617) | 作者以“白血病赢了”为题，表达面对病情的沉重现实。 | 1012 | 184 | 2019-02-19 |
| 17 | [We Need Chrome No More](https://news.ycombinator.com/item?id=19263649) | 作者认为，已经没有继续依赖 Chrome 的必要。 | 1011 | 518 | 2019-02-27 |
| 18 | [Why can’t a bot tick the 'I'm not a robot' box?](https://news.ycombinator.com/item?id=19155643) | 机器人为什么不能简单地勾选“我不是机器人”？ | 1002 | 618 | 2019-02-13 |
| 19 | [New study: Google manipulates users into constant tracking](https://news.ycombinator.com/item?id=19054440) | 一项研究指责 Google 通过诱导设计，让用户持续接受追踪。 | 953 | 445 | 2019-02-01 |
| 20 | [Public protest against Amazon](https://news.ycombinator.com/item?id=19202450) | 一项针对 Amazon 的公开抗议。 | 920 | 495 | 2019-02-19 |

## 2019-03

有效主帖 25,196 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: A retro video game console I've been working on in my free time](https://news.ycombinator.com/item?id=19393279) | 作者展示自己利用业余时间制作的复古游戏主机。 | 2690 | 210 | 2019-03-14 |
| 2 | [Firefox Send: Free encrypted file transfer service](https://news.ycombinator.com/item?id=19367850) | Firefox Send 提供免费的加密文件传输服务。 | 2031 | 512 | 2019-03-12 |
| 3 | [Spotify to Apple: Time to Play Fair](https://news.ycombinator.com/item?id=19377322) | Spotify 向 Apple 发出呼吁，要求公平竞争。 | 1903 | 841 | 2019-03-13 |
| 4 | [A guide to difficult conversations](https://news.ycombinator.com/item?id=19490573) | 一份帮助应对困难谈话的指南。 | 1829 | 400 | 2019-03-26 |
| 5 | [U.S. users are leaving Facebook by the millions, Edison Research says](https://news.ycombinator.com/item?id=19322448) | Edison Research 表示，美国用户正以百万计离开 Facebook。 | 1293 | 595 | 2019-03-06 |
| 6 | [Ghidra, NSA's reverse-engineering tool](https://news.ycombinator.com/item?id=19315273) | NSA 公布逆向工程工具 Ghidra。 | 1283 | 405 | 2019-03-05 |
| 7 | [Facebook Stored Hundreds of Millions of User Passwords in Plain Text for Years](https://news.ycombinator.com/item?id=19453359) | Facebook 被曝多年来以明文保存数亿用户的密码。 | 1252 | 429 | 2019-03-21 |
| 8 | [Nginx to Be Acquired by F5 Networks](https://news.ycombinator.com/item?id=19362326) | Nginx 宣布将被 F5 Networks 收购。 | 1057 | 383 | 2019-03-11 |
| 9 | [Thinkpad X210](https://news.ycombinator.com/item?id=19413436) | 介绍 ThinkPad X210 及其相关使用话题。 | 1005 | 477 | 2019-03-17 |
| 10 | [Why Bother with What Three Words?](https://news.ycombinator.com/item?id=19511917) | 作者追问，使用 What3words 位置表示服务究竟有何必要？ | 948 | 323 | 2019-03-28 |
| 11 | [Productivity Is About Attention Management](https://news.ycombinator.com/item?id=19539006) | 作者主张，提高生产力的关键在于管理注意力。 | 939 | 186 | 2019-03-31 |
| 12 | [Rudder issue that plagued the Boeing 737 throughout the 1990s](https://news.ycombinator.com/item?id=19389983) | 回顾上世纪九十年代长期困扰 Boeing 737 的方向舵问题。 | 936 | 352 | 2019-03-14 |
| 13 | [HIV Is Reported Cured in a Second Patient](https://news.ycombinator.com/item?id=19307160) | 第二名 HIV 感染者被报道达到治愈状态。 | 935 | 259 | 2019-03-05 |
| 14 | [Google has added DuckDuckGo as a search engine option for Chrome users](https://news.ycombinator.com/item?id=19379509) | Google 将 DuckDuckGo 加入 Chrome 可选搜索引擎列表。 | 932 | 293 | 2019-03-13 |
| 15 | [Mathigon – an interactive, personalized mathematics textbook](https://news.ycombinator.com/item?id=19477868) | Mathigon 提供交互式、可个性化学习的数学教材。 | 920 | 92 | 2019-03-24 |
| 16 | [Facebook to ban white nationalist content](https://news.ycombinator.com/item?id=19503094) | Facebook 宣布禁止白人民族主义内容。 | 890 | 1525 | 2019-03-27 |
| 17 | [Cookie Warning Shenanigans Have Got to Stop](https://news.ycombinator.com/item?id=19381063) | 作者批评 Cookie 警告中层出不穷的操作与干扰。 | 888 | 487 | 2019-03-13 |
| 18 | [Atta Elayyan, Developer of MetroTube and LazyWorm Apps, Killed in Christchurch](https://news.ycombinator.com/item?id=19426186) | MetroTube 与 LazyWorm Apps 开发者 Atta Elayyan 在基督城袭击中遇害。 | 871 | 215 | 2019-03-18 |
| 19 | [Give Me Back My Monolith](https://news.ycombinator.com/item?id=19382765) | 作者呼吁重新采用单体应用架构。 | 861 | 411 | 2019-03-13 |
| 20 | [Dwarf Fortress is coming to Steam with graphics](https://news.ycombinator.com/item?id=19380990) | 《Dwarf Fortress》将以带图形的版本登陆 Steam。 | 815 | 323 | 2019-03-13 |

## 2019-04

有效主帖 25,118 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [I Sell Onions on the Internet](https://news.ycombinator.com/item?id=19728132) | 作者分享自己在互联网上卖洋葱的生意。 | 3015 | 435 | 2019-04-23 |
| 2 | [Julian Assange arrested in London](https://news.ycombinator.com/item?id=19632449) | Julian Assange 在伦敦被捕。 | 2369 | 1119 | 2019-04-11 |
| 3 | [Otonomo, with nearly $55M in funding, is cloning our product](https://news.ycombinator.com/item?id=19719380) | 一家公司指责已融资近五千五百万美元的 Otonomo 正在复制其产品。 | 2292 | 603 | 2019-04-22 |
| 4 | [Unveiling the first-ever image of a black hole [video]](https://news.ycombinator.com/item?id=19624226) | 观看人类首张黑洞图像的发布。 | 2164 | 489 | 2019-04-10 |
| 5 | [Google Is Eating Our Mail](https://news.ycombinator.com/item?id=19756125) | 作者以“Google 正在吞掉我们的邮件”为题，关注邮件被拦截的问题。 | 1931 | 685 | 2019-04-26 |
| 6 | [Joe Armstrong has died](https://news.ycombinator.com/item?id=19706514) | Erlang 创造者 Joe Armstrong 去世。 | 1928 | 188 | 2019-04-20 |
| 7 | [I tried creating a web browser, and Google blocked me](https://news.ycombinator.com/item?id=19553941) | 作者讲述自己尝试开发浏览器，却被 Google 阻挡的经历。 | 1920 | 605 | 2019-04-02 |
| 8 | [You Are Not Google (2017)](https://news.ycombinator.com/item?id=19576092) | 作者提醒开发者，设计技术系统时应结合自身条件，谨慎照搬 Google。 | 1623 | 572 | 2019-04-04 |
| 9 | [I made a smart watch from scratch](https://news.ycombinator.com/item?id=19785841) | 作者展示从零制作的一款智能手表。 | 1451 | 216 | 2019-04-30 |
| 10 | [CityBound – An open source city simulation game in Rust](https://news.ycombinator.com/item?id=19583384) | CityBound 是用 Rust 开发的开源城市模拟游戏。 | 1340 | 264 | 2019-04-05 |
| 11 | [Public Sans – A strong, neutral typeface for text or display](https://news.ycombinator.com/item?id=19607371) | Public Sans 提供一种适合正文与展示的中性字体。 | 1310 | 237 | 2019-04-08 |
| 12 | [We Don't Have a Talent Shortage. We Have a Sucker Shortage](https://news.ycombinator.com/item?id=19707543) | 作者质疑“人才短缺”的说法，认为问题在于难以找到愿意接受不合理条件的人。 | 1289 | 774 | 2019-04-20 |
| 13 | [Warp – Mobile VPN](https://news.ycombinator.com/item?id=19542835) | Cloudflare 推出移动 VPN 服务 Warp。 | 1211 | 486 | 2019-04-01 |
| 14 | [Docker Hub Hacked – 190k accounts, GitHub tokens revoked, builds disabled](https://news.ycombinator.com/item?id=19763413) | Docker Hub 遭入侵，约十九万账户受到影响，相关 GitHub 令牌被撤销、构建被禁用。 | 1146 | 257 | 2019-04-27 |
| 15 | [Ask HN: What is your money-making side project outside programming?](https://news.ycombinator.com/item?id=19712057) | HN 用户分享编程之外能够赚钱的业余项目。 | 1134 | 717 | 2019-04-21 |
| 16 | [It seems that Google is forgetting the old web](https://news.ycombinator.com/item?id=19604135) | 作者担忧 Google 正在遗忘早期互联网的内容。 | 1102 | 302 | 2019-04-08 |
| 17 | [The inception bar: a new phishing method](https://news.ycombinator.com/item?id=19768072) | 研究者介绍名为“套娃地址栏”的新型钓鱼手法。 | 1046 | 230 | 2019-04-27 |
| 18 | [Ask HN: Are you put off building something because it already exists?](https://news.ycombinator.com/item?id=19774997) | 发现想做的产品已经存在后，你会因此放弃动手吗？ | 1046 | 292 | 2019-04-29 |
| 19 | [Post-surgical deaths in Scotland drop by a third, attributed to a checklist](https://news.ycombinator.com/item?id=19682451) | 报道苏格兰术后死亡人数下降三分之一，并将改善归因于检查清单。 | 1036 | 366 | 2019-04-17 |
| 20 | [Congress Is About to Ban the US Government from Offering Free Online Tax Filing](https://news.ycombinator.com/item?id=19613725) | 报道美国国会准备禁止政府提供免费在线报税服务。 | 1034 | 696 | 2019-04-09 |

## 2019-05

有效主帖 25,803 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Switch from Chrome to Firefox](https://news.ycombinator.com/item?id=20052623) | Mozilla 介绍如何从 Chrome 切换到 Firefox。 | 3287 | 983 | 2019-05-30 |
| 2 | [A Conspiracy to Kill IE6](https://news.ycombinator.com/item?id=19798678) | 回顾一场旨在淘汰 IE6 的“密谋”。 | 2195 | 363 | 2019-05-01 |
| 3 | [Google to restrict modern ad blocking Chrome extensions to enterprise users](https://news.ycombinator.com/item?id=20044430) | 据报道，Google 拟将部分现代广告拦截能力限制为 Chrome 企业用户可用。 | 2093 | 877 | 2019-05-29 |
| 4 | [GitHub Sponsors](https://news.ycombinator.com/item?id=19989684) | GitHub 推出 Sponsors 赞助功能。 | 2082 | 501 | 2019-05-23 |
| 5 | [Playdate – A New Handheld Gaming System](https://news.ycombinator.com/item?id=19986106) | Playdate 公布一款新的掌上游戏系统。 | 1370 | 402 | 2019-05-22 |
| 6 | ["DigitalOcean Killed Our Company"](https://news.ycombinator.com/item?id=20064169) | 一家公司指责 DigitalOcean 的做法导致自身业务毁灭。 | 1343 | 596 | 2019-05-31 |
| 7 | [All extensions disabled due to expiration of intermediate signing cert](https://news.ycombinator.com/item?id=19823701) | 中间签名证书过期，导致所有浏览器扩展被禁用。 | 1318 | 874 | 2019-05-04 |
| 8 | [Block Fingerprinting with Firefox](https://news.ycombinator.com/item?id=20054831) | 介绍如何用 Firefox 阻止浏览器指纹追踪。 | 1292 | 391 | 2019-05-30 |
| 9 | [Apple removes game after Chinese company cloned, trademarked, requested takedown](https://news.ycombinator.com/item?id=19997188) | 一名开发者称，游戏遭中国公司抄袭并抢注商标后，反被 Apple 下架。 | 1276 | 325 | 2019-05-23 |
| 10 | [Launch HN: Prometheus (YC W19) – Remove CO2 from Air and Turn It into Gasoline](https://news.ycombinator.com/item?id=19842240) | Prometheus 团队介绍将空气中的二氧化碳转成燃料的计划，宣称使用零碳电力可实现净零排放。 | 1250 | 565 | 2019-05-06 |
| 11 | [How to do hard things](https://news.ycombinator.com/item?id=19955830) | 介绍如何着手完成困难的事情。 | 1189 | 116 | 2019-05-19 |
| 12 | [GitHub Package Registry](https://news.ycombinator.com/item?id=19881709) | GitHub 推出软件包托管服务 Package Registry。 | 1181 | 373 | 2019-05-10 |
| 13 | [Advanced Data Structures (2017)](https://news.ycombinator.com/item?id=20044876) | 一门介绍高级数据结构的课程。 | 1176 | 85 | 2019-05-29 |
| 14 | [I Charged $18k for a Static HTML Page](https://news.ycombinator.com/item?id=19921386) | 作者讲述为一张静态 HTML 页面收取一万八千美元的经历。 | 1148 | 441 | 2019-05-15 |
| 15 | [Undervalued Engineering Skills: Writing Well](https://news.ycombinator.com/item?id=20061078) | 讨论工程师常被低估的一项能力：把文字写清楚。 | 1109 | 371 | 2019-05-31 |
| 16 | [Common mistakes in PostgreSQL](https://news.ycombinator.com/item?id=19817531) | 整理使用 PostgreSQL 时容易出现的常见错误。 | 1084 | 253 | 2019-05-03 |
| 17 | [Maine passes bill to prevent ISPs from selling browsing data without consent](https://news.ycombinator.com/item?id=20061764) | Maine 通过法案，禁止网络服务商未经同意出售用户浏览数据。 | 1077 | 224 | 2019-05-31 |
| 18 | [DeleteFB: Selenium script to delete all of your Facebook wall posts](https://news.ycombinator.com/item?id=19963599) | DeleteFB 用 Selenium 脚本删除用户所有 Facebook 动态帖子。 | 1067 | 265 | 2019-05-20 |
| 19 | [Mathematics all-in-one cheat-sheet (2013) [pdf]](https://news.ycombinator.com/item?id=20048205) | 一份汇集多种数学知识的速查表。 | 1060 | 161 | 2019-05-30 |
| 20 | [Css-only-chat: A truly monstrous async web chat using no JS on the front end](https://news.ycombinator.com/item?id=19852105) | 一个前端完全不用 JavaScript、仅借助 CSS 构造的异步网页聊天项目。 | 1010 | 148 | 2019-05-07 |

## 2019-06

有效主帖 24,275 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Raspberry Pi 4](https://news.ycombinator.com/item?id=20260863) | Raspberry Pi 推出第四代产品。 | 2504 | 837 | 2019-06-24 |
| 2 | [Mazda is purging touchscreens from its vehicles](https://news.ycombinator.com/item?id=20200335) | Mazda 正在从汽车中移除触摸屏。 | 2220 | 952 | 2019-06-17 |
| 3 | [Ask HN: What do you do with your Raspberry Pi?](https://news.ycombinator.com/item?id=20264911) | HN 用户分享 Raspberry Pi 的实际用途，从 VPN 到更多个人项目。 | 1741 | 1069 | 2019-06-24 |
| 4 | [Absolute truths I unlearned as junior developer](https://news.ycombinator.com/item?id=20124018) | 作者回顾自己作为初级开发者时，逐渐放下的那些“绝对真理”。 | 1529 | 511 | 2019-06-07 |
| 5 | [Google Cloud Is Down](https://news.ycombinator.com/item?id=20077421) | 用户报告 Google Cloud 故障影响 YouTube、Snapchat 等服务，而状态页仍显示正常。 | 1395 | 593 | 2019-06-02 |
| 6 | [Google's Captcha in Firefox vs. in Chrome](https://news.ycombinator.com/item?id=20147015) | 比较 Google 验证码在 Firefox 与 Chrome 中的表现。 | 1343 | 483 | 2019-06-10 |
| 7 | [The decline of the family has unleashed an epidemic of loneliness](https://news.ycombinator.com/item?id=20116699) | 作者认为，家庭的衰退正在加剧社会中的孤独问题。 | 1329 | 1183 | 2019-06-06 |
| 8 | [Startup idea checklist](https://news.ycombinator.com/item?id=20254057) | 用检查清单评估一个创业想法。 | 1251 | 194 | 2019-06-23 |
| 9 | [“Apps intended for kids may not include third-party advertising or analytics”](https://news.ycombinator.com/item?id=20108096) | 应用审核规则要求，面向儿童的应用不得包含第三方广告或分析工具。 | 1179 | 379 | 2019-06-05 |
| 10 | [Facebook reveals its cryptocurrency Libra](https://news.ycombinator.com/item?id=20210791) | Facebook 公布加密货币计划 Libra。 | 1176 | 1296 | 2019-06-18 |
| 11 | [Apple Sign In](https://news.ycombinator.com/item?id=20086045) | Apple 推出使用 Apple 账户登录的功能。 | 1145 | 528 | 2019-06-03 |
| 12 | [Google’s new reCAPTCHA has a dark side](https://news.ycombinator.com/item?id=20294801) | 作者指出 Google 新版 reCAPTCHA 存在令人担忧的一面。 | 1091 | 542 | 2019-06-27 |
| 13 | [Jony Ive to form independent design company with Apple as client](https://news.ycombinator.com/item?id=20298653) | Jony Ive 将创立独立设计公司，并把 Apple 作为客户。 | 1075 | 834 | 2019-06-27 |
| 14 | [Firefox Now Available with Enhanced Tracking Protection by Default](https://news.ycombinator.com/item?id=20095039) | Firefox 默认启用增强型追踪保护。 | 1069 | 274 | 2019-06-04 |
| 15 | [“The books will stop working.”](https://news.ycombinator.com/item?id=20297331) | 一则关于电子书将“停止工作”的警示。 | 1044 | 439 | 2019-06-27 |
| 16 | [Facebook moderators break NDAs to expose working conditions](https://news.ycombinator.com/item?id=20222594) | Facebook 内容审核员打破保密协议，揭露工作环境。 | 1014 | 590 | 2019-06-19 |
| 17 | [Relearn CSS layout](https://news.ycombinator.com/item?id=20196061) | 重新学习 CSS 布局的基本方法。 | 985 | 182 | 2019-06-16 |
| 18 | [Learning Synths](https://news.ycombinator.com/item?id=20272346) | 通过 Learning Synths 学习合成器。 | 969 | 172 | 2019-06-25 |
| 19 | [Salesforce is buying Tableau for $15.7B](https://news.ycombinator.com/item?id=20145630) | Salesforce 宣布以一百五十七亿美元收购 Tableau。 | 950 | 376 | 2019-06-10 |
| 20 | [Why is Stack Overflow trying to start audio?](https://news.ycombinator.com/item?id=20288768) | 用户追问，Stack Overflow 为什么试图播放音频？ | 909 | 402 | 2019-06-26 |

## 2019-07

有效主帖 25,163 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Vulnerability in the Mac Zoom client allows malicious websites to enable camera](https://news.ycombinator.com/item?id=20387298) | Mac 版 Zoom 漏洞可让恶意网站开启用户摄像头。 | 1937 | 456 | 2019-07-08 |
| 2 | [YouTube's ban on “hacking techniques” threatens to shut down infosec YouTube](https://news.ycombinator.com/item?id=20350306) | YouTube 禁止“黑客技术”内容的政策，可能威胁信息安全教学频道。 | 1553 | 429 | 2019-07-04 |
| 3 | [YouTube videos that have almost zero previous views](https://news.ycombinator.com/item?id=20432772) | 探索此前几乎没有人看过的 YouTube 视频。 | 1362 | 232 | 2019-07-14 |
| 4 | [Apple has pushed a silent Mac update to remove hidden Zoom web server](https://news.ycombinator.com/item?id=20407233) | Apple 静默推送 Mac 更新，移除 Zoom 隐藏的网页服务器。 | 1358 | 532 | 2019-07-10 |
| 5 | [Choose Boring Technology](https://news.ycombinator.com/item?id=20323246) | 作者建议选择成熟、看似无聊的技术。 | 1357 | 344 | 2019-07-01 |
| 6 | [YouTube bans content “showing users how to bypass secure computer systems”](https://news.ycombinator.com/item?id=20346865) | YouTube 禁止展示如何绕过安全计算机系统的内容。 | 1355 | 668 | 2019-07-03 |
| 7 | [MITM on HTTPS traffic in Kazakhstan](https://news.ycombinator.com/item?id=20472179) | 关注哈萨克斯坦针对 HTTPS 流量实施中间人拦截的问题。 | 1336 | 453 | 2019-07-18 |
| 8 | [Why did moving the mouse cursor cause Windows 95 to run more quickly?](https://news.ycombinator.com/item?id=20343728) | 为什么移动鼠标光标，会让 Windows 95 运行得更快？ | 1188 | 196 | 2019-07-03 |
| 9 | [Microsoft is investing $1B in OpenAI](https://news.ycombinator.com/item?id=20497548) | 微软宣布向 OpenAI 投资十亿美元。 | 1119 | 592 | 2019-07-22 |
| 10 | [How to assess the quality of garments (2014)](https://news.ycombinator.com/item?id=20503194) | 面向初学者介绍如何判断服装质量。 | 991 | 287 | 2019-07-22 |
| 11 | [QuickJS JavaScript Engine](https://news.ycombinator.com/item?id=20411154) | 介绍 JavaScript 引擎 QuickJS。 | 948 | 261 | 2019-07-11 |
| 12 | [Developers don't understand CORS](https://news.ycombinator.com/item?id=20404578) | 作者指出，开发者常常误解跨源资源共享机制 CORS。 | 931 | 355 | 2019-07-10 |
| 13 | [Adblocking: How about Nah?](https://news.ycombinator.com/item?id=20542107) | EFF 围绕广告拦截，讨论用户拒绝广告的选择。 | 918 | 534 | 2019-07-27 |
| 14 | [Math Basics for Computer Science and Machine Learning [pdf]](https://news.ycombinator.com/item?id=20570025) | 一份面向计算机科学与机器学习的数学基础教材。 | 883 | 118 | 2019-07-30 |
| 15 | [Google employees are listening to Google Home conversations](https://news.ycombinator.com/item?id=20402070) | 报道 Google 员工会收听部分 Google Home 对话。 | 872 | 441 | 2019-07-10 |
| 16 | [To Break Google’s Monopoly on Search, Make Its Index Public](https://news.ycombinator.com/item?id=20440079) | 作者建议公开 Google 搜索索引，以打破其搜索垄断。 | 859 | 597 | 2019-07-15 |
| 17 | [Goodbye Aberration: Physicist Solves 2,000-Year-Old Optical Problem](https://news.ycombinator.com/item?id=20369960) | 报道一位物理学家解决了延续两千年的光学像差问题。 | 845 | 207 | 2019-07-06 |
| 18 | [Calculus for Beginners and Artists (2003)](https://news.ycombinator.com/item?id=20433533) | 为初学者与艺术工作者提供微积分学习资料。 | 836 | 104 | 2019-07-14 |
| 19 | [Kuo: Apple to include new scissor switch keyboard in MacBook](https://news.ycombinator.com/item?id=20353148) | 分析师郭明錤预测，Apple 将在 MacBook 中采用新的剪刀式键盘。 | 802 | 647 | 2019-07-04 |
| 20 | [I Can’t Stop Winning](https://news.ycombinator.com/item?id=20397389) | 作者以“我停不下赢的脚步”为题，分享一篇带有戏谑意味的文字。 | 786 | 214 | 2019-07-09 |

## 2019-08

有效主帖 25,655 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Turning a MacBook into a Touchscreen with $1 of Hardware (2018)](https://news.ycombinator.com/item?id=20624576) | 用约一美元的硬件，为 MacBook 增加触摸屏式操作能力。 | 1724 | 214 | 2019-08-06 |
| 2 | [The Lonely Work of Moderating Hacker News](https://news.ycombinator.com/item?id=20643052) | 走近 Hacker News 版主，观察这份孤独的社区管理工作。 | 1663 | 777 | 2019-08-08 |
| 3 | [Introducing nushell](https://news.ycombinator.com/item?id=20783006) | 介绍新的命令行工具 nushell。 | 1477 | 369 | 2019-08-23 |
| 4 | [Google just deleted my nearly 10-year-old free and open-source Android app](https://news.ycombinator.com/item?id=20826618) | 开发者称，Google 删除了自己维护近十年的免费开源 Android 应用。 | 1400 | 581 | 2019-08-29 |
| 5 | [Ebola Is Now Curable](https://news.ycombinator.com/item?id=20679133) | 报道新的治疗进展，并提出埃博拉已经可以治愈的说法。 | 1232 | 154 | 2019-08-12 |
| 6 | [All the best engineering advice I stole from non-technical people](https://news.ycombinator.com/item?id=20610839) | 作者整理从非技术人士身上学到的工程建议。 | 1230 | 266 | 2019-08-05 |
| 7 | [I Miss Microsoft Encarta](https://news.ycombinator.com/item?id=20739629) | 作者回忆并怀念微软百科全书 Encarta。 | 1198 | 406 | 2019-08-19 |
| 8 | [Alan Kay's answer to ‘what are some forgotten books programmers should read?’](https://news.ycombinator.com/item?id=20653453) | Alan Kay 推荐一些被遗忘、却值得程序员阅读的书籍。 | 1181 | 260 | 2019-08-09 |
| 9 | [Information operations directed at Hong Kong](https://news.ycombinator.com/item?id=20740179) | Twitter 介绍针对香港的信息行动。 | 1116 | 441 | 2019-08-19 |
| 10 | [Terminating Service for 8Chan](https://news.ycombinator.com/item?id=20610395) | Cloudflare 宣布终止向 8chan 提供服务。 | 1098 | 1376 | 2019-08-05 |
| 11 | [What happens when you launch Google Chrome for the first time?](https://news.ycombinator.com/item?id=20794937) | 首次启动 Google Chrome 时，浏览器究竟会做些什么？ | 1041 | 320 | 2019-08-25 |
| 12 | [How to Build Good Software](https://news.ycombinator.com/item?id=20734384) | 探讨如何构建好的软件。 | 1016 | 239 | 2019-08-19 |
| 13 | [NULL license plate not such a bright idea](https://news.ycombinator.com/item?id=20676904) | 一位车主选择“NULL”车牌后，发现这个主意带来了麻烦。 | 999 | 467 | 2019-08-12 |
| 14 | [What Does a Coder Do If They Can't Type?](https://news.ycombinator.com/item?id=20662232) | 如果不能再打字，程序员该如何继续工作？ | 986 | 385 | 2019-08-10 |
| 15 | [Yelp Is Replacing Restaurants’ Phone Numbers So Grubhub Can Take a Cut](https://news.ycombinator.com/item?id=20625232) | Yelp 被指替换餐厅电话号码，让 Grubhub 能从订单中抽成。 | 953 | 449 | 2019-08-06 |
| 16 | [Japanese anime studio Khara moving to Blender](https://news.ycombinator.com/item?id=20713283) | 日本动画工作室 Khara 正在转向 Blender。 | 937 | 225 | 2019-08-16 |
| 17 | [Deconstructing Google’s excuses on tracking protection](https://news.ycombinator.com/item?id=20779964) | 作者拆解 Google 在追踪保护问题上的理由，并提出反驳。 | 918 | 256 | 2019-08-23 |
| 18 | [Cloudflare S-1](https://news.ycombinator.com/item?id=20706702) | 查阅 Cloudflare 提交的 S-1 上市注册文件。 | 915 | 351 | 2019-08-15 |
| 19 | [8chan goes dark after hardware provider discontinues service](https://news.ycombinator.com/item?id=20616055) | 硬件服务商终止服务后，8chan 网站下线。 | 910 | 1566 | 2019-08-05 |
| 20 | [Please Add RSS Support to Your Site](https://news.ycombinator.com/item?id=20813021) | 作者呼吁网站提供 RSS 支持。 | 904 | 296 | 2019-08-27 |

## 2019-09

有效主帖 24,905 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [The boring technology behind a one-person Internet company (2018)](https://news.ycombinator.com/item?id=20985875) | 介绍一家由一人经营的互联网公司所使用的成熟技术。 | 2010 | 451 | 2019-09-16 |
| 2 | [California bans private prisons](https://news.ycombinator.com/item?id=20955103) | 加州通过禁止私人监狱的措施。 | 1952 | 597 | 2019-09-12 |
| 3 | [Google’s GDPR Workaround](https://news.ycombinator.com/item?id=20876248) | 作者分析并质疑 Google 绕过 GDPR 要求的做法。 | 1868 | 588 | 2019-09-04 |
| 4 | [Tell HN: Thank you for not redesigning Hacker News](https://news.ycombinator.com/item?id=20854214) | 身处慢速网络地区的用户感谢 HN 保留简洁设计，让页面仍能迅速加载。 | 1831 | 390 | 2019-09-01 |
| 5 | [Microsoft has removed the “use offline account” option when installing Windows](https://news.ycombinator.com/item?id=21103683) | 用户发现，Windows 安装过程移除了“使用离线账户”选项。 | 1793 | 766 | 2019-09-28 |
| 6 | [Serverless: slower and more expensive](https://news.ycombinator.com/item?id=21046547) | 作者通过自己的比较，认为无服务器方案更慢且更贵。 | 1787 | 712 | 2019-09-23 |
| 7 | [Richard M. Stallman resigns](https://news.ycombinator.com/item?id=20990583) | Richard M. Stallman 宣布辞职。 | 1747 | 2180 | 2019-09-17 |
| 8 | [Sunsetting Python 2](https://news.ycombinator.com/item?id=20915746) | Python 官方介绍停止支持 Python 2 的安排。 | 1616 | 704 | 2019-09-09 |
| 9 | [Colorado Town Offers 1 Gbps for $60 After Years of Battling Comcast](https://news.ycombinator.com/item?id=21003773) | 科罗拉多一座小镇在多年对抗 Comcast 后，提供每月六十美元的千兆宽带。 | 1606 | 498 | 2019-09-18 |
| 10 | [How to do a code review](https://news.ycombinator.com/item?id=20890682) | 一份介绍如何进行代码审查的指南。 | 1471 | 367 | 2019-09-05 |
| 11 | [94k Bitcoin (1B USD) transferred from unknown wallet to unknown wallet](https://news.ycombinator.com/item?id=20919958) | 约九万四千枚比特币从一个未知钱包转入另一个，价值约十亿美元。 | 1430 | 680 | 2019-09-09 |
| 12 | [Questions to ask a company during a job interview](https://news.ycombinator.com/item?id=20916749) | 整理求职面试中可以反问公司的问题。 | 1388 | 455 | 2019-09-09 |
| 13 | [France and Germany Agree to Block Facebook's Libra](https://news.ycombinator.com/item?id=20970774) | 法国与德国同意阻止 Facebook 的 Libra 项目。 | 1255 | 783 | 2019-09-14 |
| 14 | [Facebook, WhatsApp Will Have to Share Messages With U.K.?](https://news.ycombinator.com/item?id=21100588) | Facebook 与 WhatsApp 是否将被要求向英国共享消息？ | 1179 | 556 | 2019-09-28 |
| 15 | [WeWork and Counterfeit Capitalism](https://news.ycombinator.com/item?id=21071890) | 作者以 WeWork 为切口，批评其眼中的“伪造资本主义”。 | 1158 | 414 | 2019-09-25 |
| 16 | [9th Circuit holds that scraping a public website does not violate the CFAA [pdf]](https://news.ycombinator.com/item?id=20920753) | 美国第九巡回上诉法院认为，抓取公开网站不违反 CFAA。 | 1136 | 275 | 2019-09-09 |
| 17 | [Bike crash left Spokane man unconscious, so his Apple Watch called 911](https://news.ycombinator.com/item?id=21064942) | 一名 Spokane 男子骑车摔伤昏迷后，Apple Watch 自动拨打九一一求助。 | 1105 | 659 | 2019-09-24 |
| 18 | [Get Started Making Music](https://news.ycombinator.com/item?id=20965386) | 通过入门课程学习制作音乐。 | 1085 | 184 | 2019-09-13 |
| 19 | [Uber lays off 435 people](https://news.ycombinator.com/item?id=20931644) | Uber 裁员四百三十五人。 | 976 | 579 | 2019-09-10 |
| 20 | [Apple’s New Mac Pro to Be Made in Texas](https://news.ycombinator.com/item?id=21050149) | Apple 宣布新款 Mac Pro 将在得州制造。 | 946 | 433 | 2019-09-23 |

## 2019-10

有效主帖 26,735 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Blizzard Suspends Professional Hearthstone Player for Hong Kong Comments](https://news.ycombinator.com/item?id=21190265) | Blizzard 因一名职业《炉石传说》选手发表涉港言论，对其作出停赛处罚。 | 2525 | 1126 | 2019-10-08 |
| 2 | [Twitter to ban political advertising](https://news.ycombinator.com/item?id=21401973) | Twitter 宣布禁止政治广告。 | 2447 | 1004 | 2019-10-30 |
| 3 | [Ken Thompson's Unix Password](https://news.ycombinator.com/item?id=21202905) | 探索 Ken Thompson 使用过的 Unix 密码。 | 2101 | 637 | 2019-10-09 |
| 4 | [A uBlock Origin update was rejected from the Chrome Web Store](https://news.ycombinator.com/item?id=21233041) | uBlock Origin 的一次更新遭 Chrome Web Store 拒绝。 | 1757 | 588 | 2019-10-12 |
| 5 | [Firefox 70](https://news.ycombinator.com/item?id=21323663) | Firefox 发布 70 版本。 | 1595 | 457 | 2019-10-22 |
| 6 | [TurboTax’s 20-Year Fight to Stop Americans from Filing Taxes for Free](https://news.ycombinator.com/item?id=21281411) | 报道 TurboTax 二十年来阻止美国人免费报税的行动。 | 1519 | 447 | 2019-10-17 |
| 7 | [Ask HN: Successful one-person online businesses?](https://news.ycombinator.com/item?id=21332072) | HN 用户分享由一人经营、能提供主要收入的成功在线生意。 | 1474 | 657 | 2019-10-23 |
| 8 | [Apple Hides Taiwan Flag in Hong Kong](https://news.ycombinator.com/item?id=21182705) | Apple 在香港隐藏台湾旗帜表情符号。 | 1456 | 686 | 2019-10-07 |
| 9 | [Open-source apps removed from Google Play Store due to donation links](https://news.ycombinator.com/item?id=21268389) | 多款开源应用据称因含捐赠链接而被 Google Play 下架。 | 1438 | 559 | 2019-10-16 |
| 10 | [I just lost my wallet on the way home from work](https://news.ycombinator.com/item?id=21256640) | 作者讲述自己下班回家途中丢失钱包的遭遇。 | 1385 | 528 | 2019-10-15 |
| 11 | [NordVPN confirms it was hacked](https://news.ycombinator.com/item?id=21312609) | NordVPN 确认曾遭到入侵。 | 1368 | 642 | 2019-10-21 |
| 12 | [Broken](https://news.ycombinator.com/item?id=21217426) | 一篇题为《坏了》的个人文章。 | 1354 | 545 | 2019-10-10 |
| 13 | [Ask HN: What's a promising area to work on?](https://news.ycombinator.com/item?id=21324768) | HN 用户讨论哪些领域正在兴起，值得投入新的项目。 | 1331 | 918 | 2019-10-22 |
| 14 | [Attorney General will ask Zuckerberg to halt plans for end-to-end encryption](https://news.ycombinator.com/item?id=21149744) | 美国司法部长将要求 Zuckerberg 暂停端到端加密计划。 | 1325 | 558 | 2019-10-03 |
| 15 | [I Accidentally Uncovered a Nationwide Scam on Airbnb](https://news.ycombinator.com/item?id=21408178) | 作者讲述自己意外揭露 Airbnb 上一场全国性骗局的经历。 | 1324 | 618 | 2019-10-31 |
| 16 | [My Favourite Git Commit](https://news.ycombinator.com/item?id=21289827) | 作者分享自己最喜欢的一次 Git 提交。 | 1313 | 370 | 2019-10-18 |
| 17 | [Why Enterprise Software Sucks](https://news.ycombinator.com/item?id=21224209) | 作者追问，企业软件为何常常难用？ | 1310 | 554 | 2019-10-11 |
| 18 | [Show HN: Bel](https://news.ycombinator.com/item?id=21231208) | 展示名为 Bel 的项目。 | 1288 | 456 | 2019-10-12 |
| 19 | [Thank You, Guido](https://news.ycombinator.com/item?id=21397996) | 一篇向 Guido 表达感谢的公开文字。 | 1269 | 376 | 2019-10-30 |
| 20 | [Perfectly Cropped](https://news.ycombinator.com/item?id=21353920) | 一篇以“完美裁剪”为题的文章。 | 1232 | 553 | 2019-10-25 |

## 2019-11

有效主帖 24,634 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Slack’s new WYSIWYG input box is terrible](https://news.ycombinator.com/item?id=21589647) | 作者批评 Slack 新的所见即所得输入框。 | 2776 | 1077 | 2019-11-20 |
| 2 | [Save .org](https://news.ycombinator.com/item?id=21611677) | 一项以“拯救 .org”为主题的公众倡议。 | 2297 | 342 | 2019-11-23 |
| 3 | [Court: Suspicionless Searches of Travelers’ Phones and Laptops Unconstitutional](https://news.ycombinator.com/item?id=21517722) | 法院裁定，无合理怀疑检查旅客手机与笔记本电脑的做法违反宪法。 | 2063 | 580 | 2019-11-12 |
| 4 | [16-inch MacBook Pro](https://news.ycombinator.com/item?id=21523780) | Apple 推出十六英寸 MacBook Pro。 | 1840 | 1688 | 2019-11-13 |
| 5 | [Tesla Cybertruck](https://news.ycombinator.com/item?id=21602437) | Tesla 公布 Cybertruck 电动皮卡。 | 1765 | 1929 | 2019-11-22 |
| 6 | [We Stood Up to a Patent Troll and Won](https://news.ycombinator.com/item?id=21447215) | Cloudflare 回顾对抗专利诉讼公司并取得胜利的经历。 | 1675 | 246 | 2019-11-04 |
| 7 | [Firefox Replay](https://news.ycombinator.com/item?id=21655958) | 介绍 Firefox Replay 项目。 | 1596 | 286 | 2019-11-28 |
| 8 | [John Carmack: I’m going to work on artificial general intelligence](https://news.ycombinator.com/item?id=21530860) | John Carmack 宣布将投入通用人工智能研究。 | 1574 | 889 | 2019-11-13 |
| 9 | [Hacker Publishes 2TB of Data from Cayman National Bank](https://news.ycombinator.com/item?id=21567022) | 黑客公开 Cayman National Bank 的两 TB 数据。 | 1549 | 468 | 2019-11-18 |
| 10 | [Build Your Own React](https://news.ycombinator.com/item?id=21536789) | 通过亲手实现一个简化版 React，学习其运行机制。 | 1478 | 108 | 2019-11-14 |
| 11 | [Spleeter: Extract voice, piano, drums, etc. from any music track](https://news.ycombinator.com/item?id=21431071) | Spleeter 帮助从音乐中分离人声、钢琴、鼓等音轨。 | 1460 | 175 | 2019-11-03 |
| 12 | [Ask HN: What's the most valuable thing you can learn in an hour?](https://news.ycombinator.com/item?id=21581361) | 集中学习一小时，能够学到哪些最有价值的东西？ | 1460 | 1076 | 2019-11-20 |
| 13 | [Personal and social information of 1.2B people discovered in data leak](https://news.ycombinator.com/item?id=21606415) | 一次数据泄露中被发现包含十二亿人的个人与社交信息。 | 1439 | 419 | 2019-11-22 |
| 14 | [1000fps image projection on deforming non-rigid surface](https://news.ycombinator.com/item?id=21594793) | 展示以每秒一千帧将图像投射到不断变形的柔性表面上的技术。 | 1306 | 128 | 2019-11-21 |
| 15 | [Basic Social Skills Guide (2012)](https://news.ycombinator.com/item?id=21585235) | 一份介绍基础社交技能的指南。 | 1291 | 409 | 2019-11-20 |
| 16 | [Psilocybin for major depression granted Breakthrough Therapy by FDA](https://news.ycombinator.com/item?id=21638290) | 用于治疗重度抑郁的裸盖菇素疗法，获美国 FDA 突破性疗法认定。 | 1240 | 466 | 2019-11-26 |
| 17 | [The Bus Ticket Theory of Genius](https://news.ycombinator.com/item?id=21613357) | Paul Graham 提出关于天才的“公交车票理论”。 | 1164 | 477 | 2019-11-23 |
| 18 | [Async-await on stable Rust](https://news.ycombinator.com/item?id=21473259) | Rust 稳定版加入 async 与 await 支持。 | 1102 | 380 | 2019-11-07 |
| 19 | [Draw.io: Online Diagramming Website](https://news.ycombinator.com/item?id=21513337) | Draw.io 提供在线绘制图表的工具。 | 1091 | 192 | 2019-11-12 |
| 20 | [The cognitive costs of air pollution](https://news.ycombinator.com/item?id=21565624) | 探讨空气污染给人的认知能力带来的代价。 | 1020 | 285 | 2019-11-18 |

## 2019-12

有效主帖 24,897 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [My Business Card Runs Linux](https://news.ycombinator.com/item?id=21871026) | 作者制作一张能够运行 Linux 的名片。 | 2595 | 397 | 2019-12-24 |
| 2 | [Having Kids](https://news.ycombinator.com/item?id=21790396) | Paul Graham 分享关于生育和养育孩子的思考。 | 1992 | 863 | 2019-12-14 |
| 3 | [IRS Reforms Free File Program, Drops Agreement Not to Compete with TurboTax](https://news.ycombinator.com/item?id=21923220) | 美国国税局改革免费报税计划，取消不与 TurboTax 竞争的协议。 | 1721 | 448 | 2019-12-31 |
| 4 | [Learning at work is work, and we must make space for it](https://news.ycombinator.com/item?id=21762640) | 作者主张，在工作中学习也是工作，应为它留出时间。 | 1673 | 453 | 2019-12-11 |
| 5 | [Nebraska farmers vote overwhelmingly for Right to Repair](https://news.ycombinator.com/item?id=21805633) | Nebraska 农民以压倒性投票支持维修权。 | 1536 | 429 | 2019-12-16 |
| 6 | [Verizon/Yahoo Blocking Attempts to Archive Yahoo Groups – Deletion: Dec. 14](https://news.ycombinator.com/item?id=21737696) | Yahoo Groups 面临删除之际，Verizon 与 Yahoo 被指阻碍资料归档。 | 1393 | 405 | 2019-12-08 |
| 7 | [The Lesson to Unlearn](https://news.ycombinator.com/item?id=21729619) | Paul Graham 讨论一种应当摆脱的既有学习模式。 | 1333 | 565 | 2019-12-07 |
| 8 | [This Page is Designed to Last](https://news.ycombinator.com/item?id=21840140) | 介绍如何把一个网页设计得能够长期保存和使用。 | 1321 | 446 | 2019-12-19 |
| 9 | [Fast](https://news.ycombinator.com/item?id=21848860) | 作者以《快》为题，关注快速完成事情的例子。 | 1314 | 291 | 2019-12-21 |
| 10 | [Huginn: Create agents that monitor and act on your behalf](https://news.ycombinator.com/item?id=21772610) | Huginn 让用户创建代理，代为监控信息并采取行动。 | 1303 | 143 | 2019-12-12 |
| 11 | [Samsung TVs May Upload Screenshots for Automatic Content Recognition](https://news.ycombinator.com/item?id=21899491) | Samsung 电视可能为自动内容识别上传屏幕截图。 | 1246 | 688 | 2019-12-28 |
| 12 | [How to fight back against Google AMP as a web user and a web developer](https://news.ycombinator.com/item?id=21712733) | 介绍网页用户与开发者可以如何抵制 Google AMP。 | 1238 | 539 | 2019-12-05 |
| 13 | [Sonos's “recycle mode” intentionally bricks devices so they can't be reused](https://news.ycombinator.com/item?id=21895086) | Sonos 的“回收模式”被指故意让设备失效，导致无法继续使用。 | 1236 | 461 | 2019-12-27 |
| 14 | [Sundar will be the CEO of both Google and Alphabet](https://news.ycombinator.com/item?id=21696954) | Sundar Pichai 将同时担任 Google 与 Alphabet 的首席执行官。 | 1204 | 587 | 2019-12-03 |
| 15 | [JetBrains: $270M revenue, 405K paying users, $0 raised](https://news.ycombinator.com/item?id=21796793) | JetBrains 被报道在未融资的情况下，取得二点七亿美元营收与四十点五万付费用户。 | 1168 | 662 | 2019-12-15 |
| 16 | [The Great Cannon has been deployed again](https://news.ycombinator.com/item?id=21721843) | 研究者报告，“大炮”网络攻击系统再次被部署。 | 1043 | 431 | 2019-12-06 |
| 17 | [PIA VPN to be acquired by malware company founded by former Israeli spy](https://news.ycombinator.com/item?id=21679682) | 报道指收购 PIA VPN 的公司涉及恶意软件业务，并由前以色列情报人员创办。 | 1004 | 359 | 2019-12-02 |
| 18 | [Challenging projects every programmer should try](https://news.ycombinator.com/item?id=21790779) | 推荐程序员可以尝试的挑战性项目。 | 911 | 297 | 2019-12-14 |
| 19 | [Archivists Are Trying to Make Sure LibGen Never Goes Down](https://news.ycombinator.com/item?id=21692222) | 资料归档者正努力确保 LibGen 不会下线。 | 908 | 257 | 2019-12-03 |
| 20 | [Fight back against Google AMP (2018)](https://news.ycombinator.com/item?id=21703345) | 作者呼吁抵制 Google AMP，并说明相关理由。 | 895 | 379 | 2019-12-04 |

## 2020-01

有效主帖 27,909 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Every Google result now looks like an ad](https://news.ycombinator.com/item?id=22107823) | 谷歌搜索结果的外观越来越像广告，链接辨识变得困难。 | 3592 | 972 | 2020-01-21 |
| 2 | [Thank HN: You helped me get a new job](https://news.ycombinator.com/item?id=22050802) | 一位开发者回顾开源作品和 HN 社区如何帮助自己找到新工作。 | 2425 | 193 | 2020-01-15 |
| 3 | [Apple dropped plan for encrypting backups after FBI complained](https://news.ycombinator.com/item?id=22106536) | 报道称苹果在 FBI 反对后放弃了加密备份计划。 | 2272 | 696 | 2020-01-21 |
| 4 | [Goodbye, Clean Code](https://news.ycombinator.com/item?id=22022466) | 作者重新审视并告别《代码整洁之道》倡导的编程方式。 | 1678 | 575 | 2020-01-11 |
| 5 | [Tricks to start working despite not feeling like it](https://news.ycombinator.com/item?id=22105229) | 分享缺乏动力时让自己开始工作的实用方法。 | 1636 | 368 | 2020-01-21 |
| 6 | [Which Emoji Scissors Close?](https://news.ycombinator.com/item?id=21942358) | 比较不同平台的剪刀表情，看看哪些真能合拢。 | 1545 | 126 | 2020-01-03 |
| 7 | [Broot – A new way to see and navigate directory trees](https://news.ycombinator.com/item?id=21998638) | Broot 提供浏览目录树和快速切换目录的新方式。 | 1448 | 287 | 2020-01-09 |
| 8 | [Procrastination is about managing emotions, not time](https://news.ycombinator.com/item?id=22124489) | 作者认为克服拖延的关键在于管理情绪。 | 1375 | 361 | 2020-01-23 |
| 9 | [Ask HN: I've been slacking off at Google for 6 years. How can I stop this?](https://news.ycombinator.com/item?id=21961560) | 一位在谷歌长期消极工作的工程师寻求重拾投入的方法。 | 1337 | 970 | 2020-01-05 |
| 10 | [A Sad Day for Rust](https://news.ycombinator.com/item?id=22075076) | 作者将这一天称为 Rust 的悲伤时刻，表达对相关事件的遗憾。 | 1243 | 991 | 2020-01-17 |
| 11 | [Not everyone has an internal monologue](https://news.ycombinator.com/item?id=22193451) | 有些人的思考并不伴随脑海中的自言自语。 | 1225 | 876 | 2020-01-30 |
| 12 | [How to Exit Vim](https://news.ycombinator.com/item?id=21988968) | 介绍退出 Vim 编辑器的方法，回应初学者常遇到的操作难题。 | 1111 | 395 | 2020-01-08 |
| 13 | [My Second Year as a Solo Developer](https://news.ycombinator.com/item?id=22201337) | 独立开发者回顾单打独斗第二年的经历。 | 1066 | 374 | 2020-01-31 |
| 14 | [Monoliths Are the Future](https://news.ycombinator.com/item?id=22193383) | 作者阐述看好单体软件架构未来的理由。 | 1065 | 552 | 2020-01-30 |
| 15 | [Congrats! Web scraping is legal! (US precedent)](https://news.ycombinator.com/item?id=22180559) | 介绍被认为支持网页抓取合法性的美国司法先例。 | 1057 | 388 | 2020-01-29 |
| 16 | [An Update on Bradfitz: Leaving Google](https://news.ycombinator.com/item?id=22161383) | Brad Fitzpatrick 宣布离开谷歌并介绍近况。 | 1012 | 271 | 2020-01-27 |
| 17 | [WireGuard is now in Linus' tree](https://news.ycombinator.com/item?id=22176032) | WireGuard 代码进入 Linus 维护的 Linux 内核树。 | 982 | 278 | 2020-01-29 |
| 18 | [Software Disenchantment (2018)](https://news.ycombinator.com/item?id=21929709) | 作者反思对现代软件逐渐失去热情的原因。 | 934 | 488 | 2020-01-01 |
| 19 | [Mozilla lays off 70](https://news.ycombinator.com/item?id=22057737) | Mozilla 宣布裁员约七十人。 | 929 | 904 | 2020-01-15 |
| 20 | [The first chosen-prefix collision for SHA-1](https://news.ycombinator.com/item?id=21979333) | 研究者实现 SHA-1 首次选择前缀碰撞攻击。 | 928 | 352 | 2020-01-07 |

## 2020-02

有效主帖 26,022 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Gears](https://news.ycombinator.com/item?id=22310813) | 介绍齿轮这一机械传动部件的结构与运行。 | 2760 | 222 | 2020-02-12 |
| 2 | [Google tracks individual users per Chrome installation ID](https://news.ycombinator.com/item?id=22236106) | 谷歌被指通过 Chrome 安装标识追踪个体用户。 | 2292 | 615 | 2020-02-04 |
| 3 | [Wacom tablets track every app you open](https://news.ycombinator.com/item?id=22247292) | Wacom 数位板软件被指记录用户打开的应用。 | 1594 | 449 | 2020-02-05 |
| 4 | [Why Discord is switching from Go to Rust](https://news.ycombinator.com/item?id=22238335) | Discord 解释部分服务从 Go 转向 Rust 的原因。 | 1582 | 642 | 2020-02-04 |
| 5 | [I Add 3-25 Seconds of Latency to Every Site I Visit](https://news.ycombinator.com/item?id=22319383) | 作者介绍给自己访问的网站增加数秒延迟的做法。 | 1564 | 437 | 2020-02-13 |
| 6 | [My productivity app for the past 12 years has been a single .txt file](https://news.ycombinator.com/item?id=22276184) | 作者讲述用单个文本文件管理十二年工作的经验。 | 1545 | 402 | 2020-02-08 |
| 7 | [Google Maps Hacks](https://news.ycombinator.com/item?id=22216821) | 展示围绕谷歌地图开展的创意实验。 | 1410 | 382 | 2020-02-02 |
| 8 | [Larry Tesler Has Died](https://news.ycombinator.com/item?id=22361282) | 缅怀参与多项硅谷重要项目的计算机先驱 Larry Tesler。 | 1346 | 149 | 2020-02-18 |
| 9 | [Freeman Dyson Has Died](https://news.ycombinator.com/item?id=22444198) | 物理学家 Freeman Dyson 去世。 | 1238 | 248 | 2020-02-28 |
| 10 | [Mathematics for the Adventurous Self-Learner](https://news.ycombinator.com/item?id=22400375) | 为愿意自主探索的学习者介绍数学学习资源。 | 1232 | 210 | 2020-02-23 |
| 11 | [What's SAP?](https://news.ycombinator.com/item?id=22244750) | 解释企业软件 SAP 的用途与背景。 | 1221 | 600 | 2020-02-05 |
| 12 | [The missing semester of CS education](https://news.ycombinator.com/item?id=22226380) | 补足计算机课程常忽略的开发工具与工作技能。 | 1163 | 196 | 2020-02-03 |
| 13 | [Let's Encrypt Has Issued a Billion Certificates](https://news.ycombinator.com/item?id=22434466) | Let's Encrypt 宣布累计签发十亿张证书。 | 1160 | 258 | 2020-02-27 |
| 14 | [Smithsonian Releases 2.8M Images into Public Domain](https://news.ycombinator.com/item?id=22417458) | 史密森尼学会向公共领域开放二百八十万张图像。 | 1115 | 123 | 2020-02-25 |
| 15 | [Microsoft begins showing an anti-Firefox ad in the Windows 10 start menu](https://news.ycombinator.com/item?id=22288599) | 微软在 Windows 10 开始菜单投放针对 Firefox 的广告。 | 1047 | 559 | 2020-02-10 |
| 16 | [1-on-1 meeting questions](https://news.ycombinator.com/item?id=22341138) | 整理适合一对一工作会谈使用的问题。 | 1030 | 296 | 2020-02-16 |
| 17 | [The dystopian world of software engineering interviews](https://news.ycombinator.com/item?id=22331804) | 作者批评软件工程面试中的不合理现象。 | 1027 | 811 | 2020-02-15 |
| 18 | [Old CSS, New CSS](https://news.ycombinator.com/item?id=22215931) | 比较传统 CSS 写法与新的样式能力。 | 1018 | 244 | 2020-02-02 |
| 19 | [Signs you’re working in a feature factory (2016)](https://news.ycombinator.com/item?id=22335738) | 列举团队沦为不断堆砌功能的工厂时的迹象。 | 1002 | 281 | 2020-02-15 |
| 20 | [“We found PayPal vulnerabilities and PayPal punished us for it”](https://news.ycombinator.com/item?id=22403565) | 安全研究者称发现 PayPal 漏洞后反而受到惩罚。 | 980 | 328 | 2020-02-24 |

## 2020-03

有效主帖 30,698 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Honda bucks industry trend by removing touchscreen controls](https://news.ycombinator.com/item?id=22738415) | 本田逆着行业潮流撤去部分触屏控制。 | 1922 | 743 | 2020-03-31 |
| 2 | [NPM Is Joining GitHub](https://news.ycombinator.com/item?id=22594549) | NPM 宣布加入 GitHub。 | 1829 | 557 | 2020-03-16 |
| 3 | [Zoom needs to clean up its privacy act](https://news.ycombinator.com/item?id=22703000) | 作者呼吁 Zoom 改善隐私保护措施。 | 1597 | 509 | 2020-03-27 |
| 4 | [Zoom iOS app sends data to Facebook even if you don’t have a Facebook account](https://news.ycombinator.com/item?id=22693792) | 报道称 Zoom 的 iOS 应用向 Facebook 发送用户数据。 | 1433 | 360 | 2020-03-26 |
| 5 | [Covid-19 is now officially a pandemic, WHO says](https://news.ycombinator.com/item?id=22547283) | 世界卫生组织正式将新冠疫情定为大流行。 | 1243 | 1038 | 2020-03-11 |
| 6 | [Zoom meetings aren’t end-to-end encrypted, despite marketing](https://news.ycombinator.com/item?id=22735746) | 报道称 Zoom 会议并未实现其宣传的端到端加密。 | 1230 | 339 | 2020-03-31 |
| 7 | [SETI@home shuts down after 21 years](https://news.ycombinator.com/item?id=22479178) | 运行二十一年的 SETI@home 宣布停止分发计算任务。 | 1216 | 343 | 2020-03-03 |
| 8 | [DuckDuckGo is good enough for regular use](https://news.ycombinator.com/item?id=22504018) | 作者认为 DuckDuckGo 已能满足日常搜索需求。 | 1158 | 476 | 2020-03-06 |
| 9 | [Open letter from Italy to the international scientific community](https://news.ycombinator.com/item?id=22579598) | 一封来自意大利、致国际科学界的公开信。 | 1095 | 693 | 2020-03-14 |
| 10 | [Ask HN: Who is hiring right now?](https://news.ycombinator.com/item?id=22665398) | 疫情期间提前开设招聘帖，汇集仍在招人的公司信息。 | 1083 | 781 | 2020-03-23 |
| 11 | [MIT moves all classes online for the rest of the semester](https://news.ycombinator.com/item?id=22539789) | 麻省理工将本学期余下课程全部转为线上教学。 | 1027 | 586 | 2020-03-10 |
| 12 | [Private client-side-only PWAs are hard, but now Apple made them impossible](https://news.ycombinator.com/item?id=22686602) | 作者认为苹果的新政策阻碍了纯客户端私密 PWA。 | 963 | 896 | 2020-03-25 |
| 13 | [Netflix to cut streaming quality in Europe for 30 days](https://news.ycombinator.com/item?id=22630665) | Netflix 宣布在欧洲降低串流画质三十天。 | 953 | 744 | 2020-03-19 |
| 14 | [Zotero: Personal Research Assistant](https://news.ycombinator.com/item?id=22694891) | 介绍帮助收集、组织和引用研究资料的 Zotero。 | 945 | 206 | 2020-03-26 |
| 15 | [FCC will require phone carriers to authenticate calls by June 2021 [pdf]](https://news.ycombinator.com/item?id=22742349) | 美国 FCC 要求运营商在 2021 年六月前实施来电认证。 | 929 | 335 | 2020-03-31 |
| 16 | [U.S. will suspend all travel from Europe for 30 days](https://news.ycombinator.com/item?id=22552477) | 美国宣布暂停来自欧洲的旅行三十天。 | 920 | 866 | 2020-03-12 |
| 17 | [Using Anki to remember what you read](https://news.ycombinator.com/item?id=22492381) | 介绍用 Anki 巩固阅读记忆的方法。 | 901 | 304 | 2020-03-05 |
| 18 | [Jitsi Meet: An open source alternative to Zoom](https://news.ycombinator.com/item?id=22669968) | 介绍可替代 Zoom 的开源视频会议工具 Jitsi Meet。 | 897 | 285 | 2020-03-23 |
| 19 | [Apple acquires Dark Sky](https://news.ycombinator.com/item?id=22739839) | 苹果收购天气应用 Dark Sky。 | 894 | 576 | 2020-03-31 |
| 20 | [Firefox is showing the way back to a world that’s private by default](https://news.ycombinator.com/item?id=22463115) | 作者认为 Firefox 正推动默认保护隐私的网络体验。 | 854 | 330 | 2020-03-02 |

## 2020-04

有效主帖 30,547 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: I'm a software engineer going blind, how should I prepare?](https://news.ycombinator.com/item?id=22918980) | 一位视力逐渐衰退的软件工程师询问职业准备建议。 | 3270 | 473 | 2020-04-19 |
| 2 | [GitHub is now free for teams](https://news.ycombinator.com/item?id=22867627) | GitHub 宣布团队使用也可免费。 | 2589 | 622 | 2020-04-14 |
| 3 | [John Conway has died](https://news.ycombinator.com/item?id=22843306) | 数学家 John Conway 去世。 | 2305 | 178 | 2020-04-11 |
| 4 | [It’s Time to Build](https://news.ycombinator.com/item?id=22911533) | 作者呼吁重新重视建设与创造的能力。 | 1820 | 1008 | 2020-04-18 |
| 5 | [Shirt Without Stripes](https://news.ycombinator.com/item?id=22925087) | 一件没有条纹的衬衫成为这项展示的主题。 | 1676 | 617 | 2020-04-20 |
| 6 | [New iPhone SE](https://news.ycombinator.com/item?id=22878515) | 苹果发布新款 iPhone SE。 | 1539 | 1459 | 2020-04-15 |
| 7 | [OBS Studio: Open-source software for video recording and live streaming](https://news.ycombinator.com/item?id=22748247) | 介绍用于录像和直播的开源软件 OBS Studio。 | 1518 | 362 | 2020-04-01 |
| 8 | [New Google SRE book: Building Secure and Reliable Systems](https://news.ycombinator.com/item?id=22815453) | 谷歌发布关于构建安全可靠系统的新 SRE 书籍。 | 1429 | 217 | 2020-04-08 |
| 9 | [Amazon scooped up data from its own sellers to launch competing products](https://news.ycombinator.com/item?id=22956182) | 报道称亚马逊利用平台卖家数据推出竞争商品。 | 1350 | 692 | 2020-04-23 |
| 10 | [What Happened to Lee](https://news.ycombinator.com/item?id=22878136) | 追问 Lee 究竟发生了什么，呈现一段有待了解的经历。 | 1298 | 280 | 2020-04-15 |
| 11 | [Zoom rolled their own encryption scheme, transmit keys through servers in China](https://news.ycombinator.com/item?id=22768494) | 报道称 Zoom 自创加密方案，并经中国服务器传输密钥。 | 1248 | 302 | 2020-04-03 |
| 12 | [Finland adds the demoscene as a UNESCO intangible world cultural heritage](https://news.ycombinator.com/item?id=22876961) | 芬兰将演示程序文化纳入非物质文化遗产名录。 | 1210 | 129 | 2020-04-15 |
| 13 | [Apple Faceshield](https://news.ycombinator.com/item?id=22806282) | 介绍苹果推出的防护面罩方案。 | 1170 | 623 | 2020-04-07 |
| 14 | [How to manage HTML DOM with vanilla JavaScript only?](https://news.ycombinator.com/item?id=22758218) | 探讨仅用原生 JavaScript 操作 HTML DOM 的方法。 | 1149 | 515 | 2020-04-02 |
| 15 | [Stripe records user movements on its customers' websites](https://news.ycombinator.com/item?id=22936818) | Stripe 被指记录客户网站上用户的操作轨迹。 | 1134 | 388 | 2020-04-21 |
| 16 | [Ask HN: What are your favorite low-coding apps / tools as a developer?](https://news.ycombinator.com/item?id=22786853) | 征集开发者实际觉得有用的低代码应用和工具。 | 1081 | 280 | 2020-04-05 |
| 17 | [Things I wished more developers knew about databases](https://news.ycombinator.com/item?id=22942278) | 整理作者希望更多开发者掌握的数据库知识。 | 1011 | 445 | 2020-04-22 |
| 18 | [How we recovered $300k of Bitcoin](https://news.ycombinator.com/item?id=22774057) | 讲述找回价值三十万美元比特币的过程。 | 998 | 198 | 2020-04-03 |
| 19 | [The Decline of Usability](https://news.ycombinator.com/item?id=22901541) | 作者反思软件易用性下降的现象。 | 996 | 695 | 2020-04-17 |
| 20 | [Who’s behind the “reopen” domain surge?](https://news.ycombinator.com/item?id=22928292) | 调查推动“重新开放”相关域名激增的幕后力量。 | 988 | 445 | 2020-04-20 |

## 2020-05

有效主帖 32,130 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Bye, Amazon](https://news.ycombinator.com/item?id=23065782) | 作者讲述与亚马逊告别的决定。 | 3816 | 1097 | 2020-05-04 |
| 2 | [Twitter Will Allow Employees to Work at Home Forever](https://news.ycombinator.com/item?id=23155647) | Twitter 宣布允许员工永久居家办公。 | 2953 | 1339 | 2020-05-12 |
| 3 | [SpaceX successfully launches two humans into orbit](https://news.ycombinator.com/item?id=23361987) | SpaceX 成功将两名宇航员送入轨道。 | 2856 | 798 | 2020-05-30 |
| 4 | [Ask HN: Am I the longest-serving programmer – 57 years and counting?](https://news.ycombinator.com/item?id=23366546) | 一位编程五十七年的从业者询问是否还有更资深同行。 | 2634 | 531 | 2020-05-31 |
| 5 | [Deno 1.0](https://news.ycombinator.com/item?id=23172483) | Deno 发布 1.0 版本。 | 2081 | 583 | 2020-05-13 |
| 6 | [MacOS Catalina: Slow by Design?](https://news.ycombinator.com/item?id=23273247) | 作者追问 macOS Catalina 的缓慢是否源于设计选择。 | 2031 | 998 | 2020-05-22 |
| 7 | [The Day AppGet Died](https://news.ycombinator.com/item?id=23331287) | AppGet 作者回顾项目走向终结的经过。 | 1930 | 535 | 2020-05-27 |
| 8 | [Let's guess what Google requires in 14 days or they kill our extension](https://news.ycombinator.com/item?id=23168874) | 开发者尝试猜测谷歌要求，否则扩展将在十四天后下架。 | 1915 | 788 | 2020-05-13 |
| 9 | [Zoom Acquires Keybase](https://news.ycombinator.com/item?id=23102430) | Zoom 收购加密通信服务 Keybase。 | 1879 | 712 | 2020-05-07 |
| 10 | [Google deletes “communist bandits” from comments on Youtube](https://news.ycombinator.com/item?id=23223219) | 谷歌被指删除 YouTube 评论中的“共匪”字样。 | 1783 | 1177 | 2020-05-18 |
| 11 | [GitHub Codespaces](https://news.ycombinator.com/item?id=23092904) | GitHub 推出云端开发环境 Codespaces。 | 1769 | 601 | 2020-05-06 |
| 12 | [A first look at Unreal Engine 5](https://news.ycombinator.com/item?id=23167794) | 初步展示虚幻引擎 5 的能力。 | 1734 | 676 | 2020-05-13 |
| 13 | [AWS services explained in one line each](https://news.ycombinator.com/item?id=23309269) | 用一句话分别解释各项 AWS 服务的用途。 | 1668 | 344 | 2020-05-26 |
| 14 | [Tell HN: Interviewed with Triplebyte? Your profile is about to become public](https://news.ycombinator.com/item?id=23279837) | 提醒 Triplebyte 用户，其面试档案将默认公开且需主动退出。 | 1543 | 574 | 2020-05-23 |
| 15 | [Extremely disillusioned with technology. Please help](https://news.ycombinator.com/item?id=23072333) | 一位对技术深感失望的人寻求帮助。 | 1527 | 714 | 2020-05-04 |
| 16 | [Google bans Podcast Addict app over non-approved Covid-19 content](https://news.ycombinator.com/item?id=23219427) | 谷歌因未经认可的新冠内容下架 Podcast Addict。 | 1525 | 546 | 2020-05-18 |
| 17 | [ICANN board withholds consent for a change of control of the .org registry](https://news.ycombinator.com/item?id=23038637) | ICANN 董事会拒绝同意 .org 注册局控制权变更。 | 1464 | 247 | 2020-05-01 |
| 18 | [We Chat, They Watch](https://news.ycombinator.com/item?id=23109997) | 围绕微信及监控问题展开讨论。 | 1417 | 512 | 2020-05-08 |
| 19 | [Doordash and Pizza Arbitrage](https://news.ycombinator.com/item?id=23216852) | 介绍 DoorDash 定价引出的披萨套利现象。 | 1393 | 514 | 2020-05-18 |
| 20 | [Google no longer providing original URL in AMP for image search results](https://news.ycombinator.com/item?id=23322730) | 谷歌图片搜索的 AMP 结果不再提供原始网址。 | 1375 | 542 | 2020-05-27 |

## 2020-06

有效主帖 30,129 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [I Am Deleting the Blog](https://news.ycombinator.com/item?id=23610416) | 作者说明删除博客的决定。 | 2450 | 1515 | 2020-06-23 |
| 2 | [The End of the Redis Adventure](https://news.ycombinator.com/item?id=23689549) | 作者回顾自己与 Redis 的历程并宣布告一段落。 | 2282 | 294 | 2020-06-30 |
| 3 | [Zoom closes account of U.S.-based Chinese activist after Tiananmen event](https://news.ycombinator.com/item?id=23480918) | Zoom 在六四纪念活动后关闭一名旅美华人活动者账号。 | 2003 | 517 | 2020-06-10 |
| 4 | [Apple announces it will switch to its own processors for future Macs](https://news.ycombinator.com/item?id=23603866) | 苹果宣布未来 Mac 将改用自研处理器。 | 1869 | 1436 | 2020-06-22 |
| 5 | [iOS14 reveals that TikTok may snoop clipboard contents every few keystrokes](https://news.ycombinator.com/item?id=23634138) | iOS 14 提示 TikTok 可能在输入过程中频繁读取剪贴板。 | 1847 | 591 | 2020-06-24 |
| 6 | [India bans TikTok, WeChat, and dozens of other Chinese apps](https://news.ycombinator.com/item?id=23679286) | 印度宣布封禁 TikTok、微信等数十款中国应用。 | 1483 | 795 | 2020-06-29 |
| 7 | [I Just Hit $100k/year On GitHub Sponsors](https://news.ycombinator.com/item?id=23613719) | 一位开发者分享 GitHub Sponsors 年收入达到十万美元的经历。 | 1469 | 493 | 2020-06-23 |
| 8 | [Mozilla VPN](https://news.ycombinator.com/item?id=23565192) | Mozilla 推出 VPN 服务。 | 1363 | 504 | 2020-06-18 |
| 9 | [Time to Upgrade Your Monitor](https://news.ycombinator.com/item?id=23551983) | 作者阐述升级显示器的理由。 | 1220 | 1013 | 2020-06-17 |
| 10 | [Teach Yourself Computer Science](https://news.ycombinator.com/item?id=23588896) | 为自学计算机科学整理学习路径和资源。 | 1169 | 265 | 2020-06-21 |
| 11 | [Police attacks against journalists across the U.S. since May 28](https://news.ycombinator.com/item?id=23393914) | 汇集五月二十八日以来美国警方针对记者的袭击记录。 | 1125 | 768 | 2020-06-02 |
| 12 | [MIT Ends Elsevier Negotiations](https://news.ycombinator.com/item?id=23489068) | 麻省理工终止与学术出版商 Elsevier 的谈判。 | 1104 | 263 | 2020-06-11 |
| 13 | [Forget Google, time to end the Visa-MasterCard duopoly](https://news.ycombinator.com/item?id=23682716) | 作者呼吁打破 Visa 与万事达在支付领域的双头格局。 | 1100 | 523 | 2020-06-29 |
| 14 | [Zoom says it won’t encrypt free calls so it can work more with law enforcement](https://news.ycombinator.com/item?id=23399924) | Zoom 称免费通话不加密，以配合执法工作。 | 1094 | 458 | 2020-06-03 |
| 15 | [A Facebook crawler was making 7M requests per day to my stupid website](https://news.ycombinator.com/item?id=23490367) | 作者遭遇 Facebook 爬虫每天向个人网站发出七百万次请求。 | 1074 | 407 | 2020-06-11 |
| 16 | [Zoom Acknowledges It Suspended Activists' Accounts at China's Request](https://news.ycombinator.com/item?id=23506580) | Zoom 承认应中国要求暂停活动人士账号。 | 1069 | 371 | 2020-06-13 |
| 17 | [Why we won’t be supporting Sign in with Apple](https://news.ycombinator.com/item?id=23681982) | 开发者解释拒绝接入“通过 Apple 登录”的原因。 | 1069 | 469 | 2020-06-29 |
| 18 | [You download the app and it doesn’t work](https://news.ycombinator.com/item?id=23579264) | 作者讨论下载应用后却无法正常使用的体验。 | 1044 | 543 | 2020-06-19 |
| 19 | [When you type realty.com into Safari it takes you to realtor.com](https://news.ycombinator.com/item?id=23646158) | Safari 被指将输入的 realty.com 导向 realtor.com。 | 1039 | 425 | 2020-06-25 |
| 20 | [New slats make the Golden Gate Bridge sound like a David Lynch movie](https://news.ycombinator.com/item?id=23439647) | 金门大桥新装栏杆产生奇特声响，引发关注。 | 952 | 332 | 2020-06-06 |

## 2020-07

有效主帖 29,142 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Hackers take over prominent Twitter accounts in simultaneous attack](https://news.ycombinator.com/item?id=23851275) | 黑客同时接管多个知名 Twitter 账号。 | 2595 | 1349 | 2020-07-15 |
| 2 | [Oppose the Earn IT Act](https://news.ycombinator.com/item?id=23703367) | 作者呼吁反对 EARN IT 法案。 | 2229 | 543 | 2020-07-01 |
| 3 | [Grant Imahara Has Died](https://news.ycombinator.com/item?id=23828253) | 工程师及电视节目主持人 Grant Imahara 去世。 | 1963 | 255 | 2020-07-14 |
| 4 | [Tech sector job interviews assess anxiety, not software skills: study](https://news.ycombinator.com/item?id=23848039) | 研究认为技术面试测量的可能更多是焦虑程度。 | 1782 | 1141 | 2020-07-15 |
| 5 | [Del.icio.us](https://news.ycombinator.com/item?id=23984503) | 回看社交书签服务 Del.icio.us。 | 1649 | 506 | 2020-07-29 |
| 6 | [Apple does not keep the 30% commission on a refund](https://news.ycombinator.com/item?id=23995750) | 澄清苹果在退款时不会保留三成佣金。 | 1594 | 351 | 2020-07-30 |
| 7 | [U.S. Supreme Court deems half of Oklahoma a Native American reservation](https://news.ycombinator.com/item?id=23781954) | 美国最高法院认定俄克拉何马近半地区属于原住民保留地。 | 1489 | 1225 | 2020-07-09 |
| 8 | [Etcd, or, why modern software makes me sad](https://news.ycombinator.com/item?id=23833362) | 作者借 Etcd 表达对现代软件复杂性的失望。 | 1285 | 630 | 2020-07-14 |
| 9 | [When a customer refunds your paid app, Apple refunds its 30% cut [edited]](https://news.ycombinator.com/item?id=23987584) | 修订说明付费应用退款时苹果也会退还其三成分成。 | 1243 | 548 | 2020-07-29 |
| 10 | [Where Am I? NYTimes or Google?](https://news.ycombinator.com/item?id=23729160) | 作者追问页面体验究竟属于纽约时报还是谷歌。 | 1130 | 355 | 2020-07-04 |
| 11 | [Amazon met with startups about investing, then launched competing products](https://news.ycombinator.com/item?id=23929044) | 报道称亚马逊与初创企业洽谈投资后推出竞争产品。 | 1125 | 351 | 2020-07-23 |
| 12 | [Linux Mint drops Ubuntu Snap packages](https://news.ycombinator.com/item?id=23771847) | Linux Mint 停止采用 Ubuntu 的 Snap 软件包。 | 1106 | 523 | 2020-07-08 |
| 13 | [Nvidia is reportedly in ‘advanced talks’ to buy ARM for more than $32B](https://news.ycombinator.com/item?id=24009177) | 传英伟达正深入洽谈以逾三百二十亿美元收购 ARM。 | 1106 | 674 | 2020-07-31 |
| 14 | [Universal Basic Income is Capitalism 2.0](https://news.ycombinator.com/item?id=23993259) | 作者将全民基本收入视为资本主义的新版本。 | 1105 | 1978 | 2020-07-30 |
| 15 | [Reddit's website uses DRM for fingerprinting](https://news.ycombinator.com/item?id=23774394) | Reddit 网站被指利用 DRM 技术识别用户设备。 | 1099 | 540 | 2020-07-08 |
| 16 | [OpenAI's GPT-3 may be the biggest thing since Bitcoin](https://news.ycombinator.com/item?id=23885684) | 作者高度评价 GPT-3，并将其影响与比特币相提并论。 | 1079 | 526 | 2020-07-18 |
| 17 | [When your coworker does great work, tell their manager](https://news.ycombinator.com/item?id=23858662) | 建议同事表现出色时向其主管表达认可。 | 1074 | 367 | 2020-07-16 |
| 18 | [Google offers free fabbing for 130nm open-source chips](https://news.ycombinator.com/item?id=23755693) | 谷歌为 130 纳米开源芯片提供免费流片机会。 | 1055 | 385 | 2020-07-07 |
| 19 | [We can't send email more than 500 miles (2002)](https://news.ycombinator.com/item?id=23775404) | 回顾邮件无法发送到五百英里外的经典故障。 | 1034 | 135 | 2020-07-08 |
| 20 | [Data structures and algorithms I actually used while working at tech companies](https://news.ycombinator.com/item?id=23841491) | 开发者盘点在科技公司实际用过的数据结构与算法。 | 1025 | 524 | 2020-07-15 |

## 2020-08

有效主帖 27,480 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Factorio 1.0](https://news.ycombinator.com/item?id=24155609) | 自动化建造游戏《异星工厂》发布 1.0 版。 | 1878 | 615 | 2020-08-14 |
| 2 | [Facebook account now required to login to Oculus devices](https://news.ycombinator.com/item?id=24201306) | Oculus 设备登录开始要求 Facebook 账号。 | 1858 | 1025 | 2020-08-18 |
| 3 | [Apple just kicked Fortnite off the App Store](https://news.ycombinator.com/item?id=24146987) | 苹果将《堡垒之夜》从 App Store 下架。 | 1704 | 1432 | 2020-08-13 |
| 4 | [Mozilla lays off 250 employees while it refocuses on commercial products](https://news.ycombinator.com/item?id=24120336) | Mozilla 裁员二百五十人并转向商业产品。 | 1602 | 1456 | 2020-08-11 |
| 5 | [American Academy of Sleep Medicine calls for elimination of daylight saving time](https://news.ycombinator.com/item?id=24312545) | 美国睡眠医学学会呼吁取消夏令时。 | 1600 | 486 | 2020-08-29 |
| 6 | [Mozilla Lifeboat](https://news.ycombinator.com/item?id=24135032) | 以救生艇为喻，关注 Mozilla 面临的处境与未来。 | 1518 | 308 | 2020-08-12 |
| 7 | [ReMarkable 2.0 – A digital notebook that feels like paper](https://news.ycombinator.com/item?id=24295443) | 介绍强调纸张书写感的 reMarkable 2 数字笔记本。 | 1410 | 685 | 2020-08-27 |
| 8 | [Ask HN: Why is Reddit on mobile so obsessed with making me use their app?](https://news.ycombinator.com/item?id=24208958) | 用户追问 Reddit 为何在手机网页上反复劝其安装应用。 | 1403 | 644 | 2020-08-19 |
| 9 | [Africa declared free of wild polio](https://news.ycombinator.com/item?id=24273602) | 非洲被宣布消除了野生脊髓灰质炎病毒。 | 1387 | 241 | 2020-08-25 |
| 10 | [I thought I would have accomplished a lot more today and also before I was 35](https://news.ycombinator.com/item?id=24316725) | 作者反思每日计划与三十五岁前人生期待之间的落差。 | 1383 | 668 | 2020-08-29 |
| 11 | [Arwes – Futuristic Sci-Fi / Cyberpunk Graphical User Interface Framework](https://news.ycombinator.com/item?id=24282270) | Arwes 提供科幻与赛博朋克风格的图形界面框架。 | 1326 | 225 | 2020-08-26 |
| 12 | [Google is apparently taking down all/most Fediverse apps from the Play Store](https://news.ycombinator.com/item?id=24304275) | 报道称谷歌正下架大量联邦宇宙相关应用。 | 1313 | 935 | 2020-08-28 |
| 13 | [Thank You MDN](https://news.ycombinator.com/item?id=24136895) | 向开发者文档平台 MDN 表达感谢。 | 1283 | 319 | 2020-08-12 |
| 14 | [Degoogle: Cutting Google out of your life](https://news.ycombinator.com/item?id=24245817) | 介绍逐步减少生活中谷歌服务依赖的方法。 | 1257 | 616 | 2020-08-22 |
| 15 | [Germany plans to dim lights at night to save insects](https://news.ycombinator.com/item?id=24071005) | 德国计划降低夜间照明以保护昆虫。 | 1194 | 469 | 2020-08-06 |
| 16 | [Can't you just right click?](https://news.ycombinator.com/item?id=24217116) | 追问能否直接右键操作，重新审视一个看似简单的使用问题。 | 1169 | 746 | 2020-08-19 |
| 17 | [Apple Terminates Epic Games' Developer Account](https://news.ycombinator.com/item?id=24309632) | 苹果终止 Epic Games 的开发者账号。 | 1169 | 1474 | 2020-08-28 |
| 18 | [20GB leak of Intel data: whole Git repositories, dev tools, backdoor mentions](https://news.ycombinator.com/item?id=24074588) | 英特尔约二十 GB 数据外泄，涉及代码仓库和开发工具。 | 1062 | 444 | 2020-08-06 |
| 19 | [Moved a server from one building to another with zero downtime](https://news.ycombinator.com/item?id=24059243) | 分享服务器跨楼搬迁且服务不停机的经历。 | 1043 | 400 | 2020-08-05 |
| 20 | [Laws of UX](https://news.ycombinator.com/item?id=24030969) | 整理可用于界面设计的用户体验规律。 | 1037 | 293 | 2020-08-02 |

## 2020-09

有效主帖 25,947 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Social Cooling (2017)](https://news.ycombinator.com/item?id=24627363) | 探讨持续被数据追踪如何让人更加自我约束。 | 2692 | 1058 | 2020-09-29 |
| 2 | [When you browse Instagram and find Tony Abbott's passport number](https://news.ycombinator.com/item?id=24488224) | 一次浏览 Instagram 的经历意外暴露了 Tony Abbott 的护照号码。 | 2326 | 340 | 2020-09-16 |
| 3 | [Nvidia to Acquire Arm for $40B](https://news.ycombinator.com/item?id=24464807) | 英伟达宣布以四百亿美元收购 Arm。 | 2122 | 752 | 2020-09-13 |
| 4 | [Ruth Bader Ginsburg has died](https://news.ycombinator.com/item?id=24522908) | 美国最高法院大法官 Ruth Bader Ginsburg 去世。 | 1738 | 1452 | 2020-09-18 |
| 5 | [Ninth Circuit rules NSA's bulk collection of Americans' call records was illegal](https://news.ycombinator.com/item?id=24356741) | 美国第九巡回法院裁定 NSA 大规模收集通话记录违法。 | 1722 | 472 | 2020-09-02 |
| 6 | [This electrical transmission tower has a problem](https://news.ycombinator.com/item?id=24499924) | 分析一座输电铁塔存在的问题。 | 1666 | 460 | 2020-09-17 |
| 7 | [Tell HN: Never search for domains on Godaddy.com](https://news.ycombinator.com/item?id=24506303) | 用户称查询的域名随后被注册，提醒谨慎使用 GoDaddy 搜索。 | 1656 | 729 | 2020-09-17 |
| 8 | [Firefox usage is down despite Mozilla's top exec pay going up](https://news.ycombinator.com/item?id=24563698) | Mozilla 高管薪酬上涨之际，Firefox 使用量却在下降。 | 1624 | 1286 | 2020-09-23 |
| 9 | [Chuck Feeney Is Now Officially Broke](https://news.ycombinator.com/item?id=24483283) | 慈善家 Chuck Feeney 完成捐赠，如今已散尽财富。 | 1336 | 836 | 2020-09-15 |
| 10 | [I no longer build software](https://news.ycombinator.com/item?id=24541964) | 作者讲述自己不再构建软件的经历与思考。 | 1287 | 856 | 2020-09-21 |
| 11 | [On the Use of a Life](https://news.ycombinator.com/item?id=24537865) | 反思如何使用自己有限的一生。 | 1275 | 265 | 2020-09-20 |
| 12 | [Most-favorited Hacker News posts](https://news.ycombinator.com/item?id=24351073) | 汇集 HN 用户收藏最多的帖子。 | 1266 | 259 | 2020-09-02 |
| 13 | [BitTorrent v2](https://news.ycombinator.com/item?id=24401999) | 介绍 BitTorrent 第二版协议。 | 1227 | 560 | 2020-09-07 |
| 14 | [Microsoft to acquire ZeniMax Media and Bethesda Softworks for $7.5B](https://news.ycombinator.com/item?id=24543121) | 微软宣布以七十五亿美元收购 ZeniMax 与 Bethesda。 | 1185 | 779 | 2020-09-21 |
| 15 | [CRDTs are the future](https://news.ycombinator.com/item?id=24617542) | 作者阐述看好无冲突复制数据类型前景的理由。 | 1181 | 312 | 2020-09-28 |
| 16 | [We now consider Moment.js to be a legacy project in maintenance mode](https://news.ycombinator.com/item?id=24477941) | Moment.js 被定位为进入维护模式的旧项目。 | 1129 | 257 | 2020-09-15 |
| 17 | [Embedded PDF viewer in Firefox 81 supports filling forms](https://news.ycombinator.com/item?id=24554581) | Firefox 81 的内置 PDF 阅读器支持填写表单。 | 1093 | 375 | 2020-09-22 |
| 18 | [Nova by Panic](https://news.ycombinator.com/item?id=24495330) | 介绍 Panic 开发的代码编辑器 Nova。 | 1051 | 542 | 2020-09-16 |
| 19 | [Samsung TV owners complain about increasingly obtrusive ads](https://news.ycombinator.com/item?id=24624951) | 三星电视用户抱怨广告越来越妨碍使用。 | 996 | 935 | 2020-09-29 |
| 20 | [They're deleting my channel, but they don't know why? [video]](https://news.ycombinator.com/item?id=24571038) | 创作者称频道将被删除，却未获得明确原因。 | 987 | 761 | 2020-09-23 |

## 2020-10

有效主帖 26,756 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [YouTube-dl has received a DMCA takedown from RIAA](https://news.ycombinator.com/item?id=24872911) | RIAA 发出 DMCA 下架通知，要求移除 youtube-dl。 | 4240 | 1443 | 2020-10-23 |
| 2 | [How journalists use youtube-dl](https://news.ycombinator.com/item?id=24899863) | 介绍记者如何利用 youtube-dl 开展工作。 | 1651 | 328 | 2020-10-26 |
| 3 | [Show HN: I made a site where you practice typing by retyping entire novels](https://news.ycombinator.com/item?id=24696658) | 通过重新输入整部小说来练习打字的网站。 | 1589 | 378 | 2020-10-06 |
| 4 | [U.S. Accuses Google of Illegally Protecting Monopoly](https://news.ycombinator.com/item?id=24836520) | 美国指控谷歌非法维护其垄断地位。 | 1572 | 824 | 2020-10-20 |
| 5 | [Apple tells Telegram to take down protestor channels in Belarus](https://news.ycombinator.com/item?id=24737171) | 苹果要求 Telegram 移除白俄罗斯抗议者频道。 | 1512 | 607 | 2020-10-10 |
| 6 | [AWS forked my project and launched it as its own service](https://news.ycombinator.com/item?id=24799660) | 作者称 AWS 分叉自己的项目并作为独立服务推出。 | 1466 | 637 | 2020-10-16 |
| 7 | [Facebook Container for Firefox](https://news.ycombinator.com/item?id=24849452) | Firefox 的 Facebook Container 扩展帮助隔离 Facebook 活动。 | 1457 | 425 | 2020-10-21 |
| 8 | [We Hacked Apple for 3 Months](https://news.ycombinator.com/item?id=24718078) | 研究者回顾持续三个月对苹果开展安全测试的经历。 | 1454 | 308 | 2020-10-08 |
| 9 | [My Resignation from the Intercept](https://news.ycombinator.com/item?id=24933054) | 作者说明辞去 The Intercept 职务的原因。 | 1441 | 1604 | 2020-10-29 |
| 10 | [Show HN: I built a Rotten Tomatoes-style platform for durable products](https://news.ycombinator.com/item?id=24707407) | 一个借鉴烂番茄评分方式、评价耐用商品的平台。 | 1392 | 398 | 2020-10-07 |
| 11 | [Bongo Cat](https://news.ycombinator.com/item?id=24866896) | 介绍以敲击动作走红的可爱小猫 Bongo Cat。 | 1348 | 190 | 2020-10-23 |
| 12 | [Chrome exempts Google sites from user site data settings](https://news.ycombinator.com/item?id=24817304) | Chrome 被指将谷歌网站排除在用户站点数据设置之外。 | 1320 | 492 | 2020-10-18 |
| 13 | [A warning about Glassdoor](https://news.ycombinator.com/item?id=24789865) | 作者提醒使用 Glassdoor 时需注意的问题。 | 1262 | 329 | 2020-10-15 |
| 14 | [Trump administration announces overhaul of H1B visa program requiring higher pay](https://news.ycombinator.com/item?id=24702393) | 特朗普政府宣布调整 H-1B 签证制度并提高薪资要求。 | 1256 | 1363 | 2020-10-06 |
| 15 | [Stop the Earn IT Bill Before It Breaks Encryption](https://news.ycombinator.com/item?id=24695373) | 作者呼吁阻止可能损害加密的 EARN IT 法案。 | 1252 | 342 | 2020-10-06 |
| 16 | [I am an Uighur who faced China’s concentration camps](https://news.ycombinator.com/item?id=24879870) | 一名维吾尔人讲述自己遭遇中国拘禁营的经历。 | 1242 | 536 | 2020-10-24 |
| 17 | [Room-Temperature Superconductivity Achieved for the First Time](https://news.ycombinator.com/item?id=24777268) | 研究团队宣布首次实现室温超导。 | 1235 | 354 | 2020-10-14 |
| 18 | [I Violated a Code of Conduct](https://news.ycombinator.com/item?id=24926214) | 作者讲述自己违反行为准则的经历。 | 1214 | 912 | 2020-10-29 |
| 19 | [Apple's apps bypass firewalls like LittleSnitch and LuLu on macOS Big Sur](https://news.ycombinator.com/item?id=24838816) | macOS Big Sur 中苹果应用被指绕过 Little Snitch、LuLu 等防火墙。 | 1183 | 616 | 2020-10-20 |
| 20 | [YouTube-dl is now part of GitHub/dmca.git](https://news.ycombinator.com/item?id=24882921) | youtube-dl 出现在 GitHub 保存 DMCA 通知的仓库中。 | 1098 | 315 | 2020-10-25 |

## 2020-11

有效主帖 25,441 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Biden wins White House, vowing new direction for divided U.S.](https://news.ycombinator.com/item?id=25015967) | 拜登赢得美国总统选举，并承诺为分裂的国家带来新方向。 | 3089 | 4576 | 2020-11-07 |
| 2 | [YouTube-dl's repository has been restored](https://news.ycombinator.com/item?id=25111726) | youtube-dl 的代码仓库恢复访问。 | 2636 | 658 | 2020-11-16 |
| 3 | [macOS unable to open any non-Apple application](https://news.ycombinator.com/item?id=25074959) | 用户报告 macOS 无法打开任何非苹果应用。 | 2603 | 1278 | 2020-11-12 |
| 4 | [Raspberry Pi 400 Desktop PC](https://news.ycombinator.com/item?id=24965614) | 树莓派推出键盘一体式桌面电脑 Pi 400。 | 2594 | 754 | 2020-11-02 |
| 5 | [Tell HN: Thank You Dang](https://news.ycombinator.com/item?id=25225775) | HN 用户在感恩节感谢管理员 dang 维护社区讨论。 | 2363 | 249 | 2020-11-27 |
| 6 | [Covid vaccine: First ‘milestone’ vaccine offers 90% protection](https://news.ycombinator.com/item?id=25033844) | 首批新冠疫苗试验结果宣称保护效力达到九成。 | 1887 | 1148 | 2020-11-09 |
| 7 | [Zoom lied to users about end-to-end encryption for years, FTC says](https://news.ycombinator.com/item?id=25044254) | 美国 FTC 指控 Zoom 多年来对端到端加密作出虚假宣传。 | 1616 | 425 | 2020-11-10 |
| 8 | [Tony Hsieh has died](https://news.ycombinator.com/item?id=25235490) | 企业家谢家华去世。 | 1598 | 298 | 2020-11-28 |
| 9 | [EU Draft Council Declaration Against Encryption [pdf]](https://news.ycombinator.com/item?id=25028411) | 介绍欧盟理事会一份涉及反对加密的声明草案。 | 1530 | 752 | 2020-11-08 |
| 10 | [Your Computer Isn't Yours](https://news.ycombinator.com/item?id=25078034) | 作者质疑用户是否真正拥有自己的电脑。 | 1514 | 741 | 2020-11-13 |
| 11 | [AlphaFold: a solution to a 50-year-old grand challenge in biology](https://news.ycombinator.com/item?id=25254772) | 介绍 AlphaFold 应对困扰生物学五十年难题的进展。 | 1473 | 1 | 2020-11-30 |
| 12 | [AlphaFold: a solution to a 50-year-old grand challenge in biology](https://news.ycombinator.com/item?id=25253488) | 介绍 AlphaFold 在生物学长期挑战上的突破。 | 1398 | 660 | 2020-11-30 |
| 13 | [Apple unveils M1, its first system-on-a-chip for portable Mac computers](https://news.ycombinator.com/item?id=25049079) | 苹果发布首款面向便携式 Mac 的自研芯片 M1。 | 1365 | 1346 | 2020-11-10 |
| 14 | [Guido van Rossum joins Microsoft](https://news.ycombinator.com/item?id=25071847) | Python 创始人 Guido van Rossum 加入微软。 | 1337 | 799 | 2020-11-12 |
| 15 | [Standing up for developers: YouTube-dl is back](https://news.ycombinator.com/item?id=25113132) | GitHub 说明恢复 youtube-dl 并支持开发者的决定。 | 1275 | 1 | 2020-11-16 |
| 16 | [Beirut Port Explosion](https://news.ycombinator.com/item?id=25149177) | 记录贝鲁特港口爆炸事件。 | 1215 | 199 | 2020-11-19 |
| 17 | [Disclosure: Unlimited Chase Ultimate Rewards Points](https://news.ycombinator.com/item?id=24988301) | 披露可无限获取 Chase Ultimate Rewards 积分的问题。 | 1181 | 252 | 2020-11-04 |
| 18 | [On Apple's Piss-Poor Documentation](https://news.ycombinator.com/item?id=25046691) | 作者批评苹果开发文档的质量。 | 1180 | 335 | 2020-11-10 |
| 19 | [How to Think for Yourself](https://news.ycombinator.com/item?id=25227651) | 探讨培养独立思考能力的方法。 | 1090 | 816 | 2020-11-27 |
| 20 | [Google users locked out after 15 years' use](https://news.ycombinator.com/item?id=24965432) | 谷歌用户在使用服务十五年后遭遇账号锁定。 | 1087 | 694 | 2020-11-02 |

## 2020-12

有效主帖 27,417 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [No Cookie for You](https://news.ycombinator.com/item?id=25457440) | 以“不让你用 Cookie”为切入点，关注网站 Cookie 问题。 | 2941 | 609 | 2020-12-17 |
| 2 | [Google outage – resolved](https://news.ycombinator.com/item?id=25415989) | 谷歌多项服务发生故障，帖内更新称服务已恢复。 | 2316 | 827 | 2020-12-14 |
| 3 | [Cameras and Lenses](https://news.ycombinator.com/item?id=25357315) | 介绍相机和镜头的相关知识。 | 2132 | 213 | 2020-12-09 |
| 4 | [FTC Sues Facebook for Illegal Monopolization](https://news.ycombinator.com/item?id=25363366) | 美国 FTC 起诉 Facebook 非法垄断。 | 1752 | 709 | 2020-12-09 |
| 5 | [Zero-click, wormable, cross-platform remote code execution in Microsoft Teams](https://news.ycombinator.com/item?id=25331407) | 微软 Teams 被披露存在无需点击且可跨平台传播的远程执行漏洞。 | 1307 | 317 | 2020-12-07 |
| 6 | [Tips for a Better Life](https://news.ycombinator.com/item?id=25518730) | 分享改善日常生活的建议。 | 1271 | 463 | 2020-12-23 |
| 7 | [Jetbrains founders turn billionaires without VC help](https://news.ycombinator.com/item?id=25466304) | JetBrains 创始人未依赖风投成为亿万富翁。 | 1245 | 514 | 2020-12-18 |
| 8 | [Just Wanted to Say Thanks](https://news.ycombinator.com/item?id=25551487) | 作者表达对他人帮助的感谢。 | 1244 | 241 | 2020-12-27 |
| 9 | [Do You Love Me? [video]](https://news.ycombinator.com/item?id=25573327) | 观看名为《Do You Love Me?》的视频演示。 | 1218 | 452 | 2020-12-29 |
| 10 | [How We Saved Dot Org](https://news.ycombinator.com/item?id=25521836) | 回顾阻止 .org 出售的行动。 | 1187 | 151 | 2020-12-23 |
| 11 | [YouTube to remove content that alleges widespread election fraud](https://news.ycombinator.com/item?id=25359003) | YouTube 将移除声称选举存在大规模舞弊的内容。 | 1183 | 3065 | 2020-12-09 |
| 12 | [Amazon EC2 Mac Instances](https://news.ycombinator.com/item?id=25262303) | 亚马逊 EC2 推出 Mac 云实例。 | 1091 | 481 | 2020-12-01 |
| 13 | [Amazon disallows pointing out paid reviews](https://news.ycombinator.com/item?id=25459434) | 亚马逊被指不允许用户指出付费评论。 | 1086 | 479 | 2020-12-17 |
| 14 | [Hotwire: HTML over the Wire](https://news.ycombinator.com/item?id=25507942) | Hotwire 提供通过传输 HTML 构建交互页面的方案。 | 1073 | 545 | 2020-12-22 |
| 15 | [Ten year study: No link between violent video games and aggressive behavior](https://news.ycombinator.com/item?id=25570038) | 十年研究未发现暴力游戏与攻击行为存在关联。 | 1024 | 566 | 2020-12-29 |
| 16 | [Firefox Was Always Enough](https://news.ycombinator.com/item?id=25443152) | 作者认为 Firefox 一直能够满足使用需要。 | 1000 | 586 | 2020-12-16 |
| 17 | [AirPods Max](https://news.ycombinator.com/item?id=25344762) | 苹果推出头戴耳机 AirPods Max。 | 996 | 1831 | 2020-12-08 |
| 18 | [Happy New Year HN](https://news.ycombinator.com/item?id=25595865) | HN 用户感谢社区在 2020 年的陪伴并送上新年祝福。 | 986 | 236 | 2020-12-31 |
| 19 | [How bad is your Spotify?](https://news.ycombinator.com/item?id=25517868) | 一个评判用户 Spotify 音乐品味的项目。 | 974 | 607 | 2020-12-23 |
| 20 | [Agents raid home of fired Florida data scientist who built Covid-19 dashboard](https://news.ycombinator.com/item?id=25339510) | 佛罗里达执法人员搜查一名被解雇的新冠数据科学家住所。 | 969 | 635 | 2020-12-07 |

## 2021-01

有效主帖 26,664 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Robinhood is limiting purchases of stocks: AMC, Blackberry, Nokia, and GameStop](https://news.ycombinator.com/item?id=25941431) | Robinhood 限制用户买入 GameStop 等多只股票。 | 2706 | 1643 | 2021-01-28 |
| 2 | [WhatsApp gives users an ultimatum: Share data with Facebook or stop using app](https://news.ycombinator.com/item?id=25662215) | WhatsApp 要求用户同意与 Facebook 共享数据才能继续使用。 | 2254 | 1148 | 2021-01-06 |
| 3 | [Select a muscle and it provides the exercises to workout the selected muscle](https://news.ycombinator.com/item?id=25854523) | 一个通过选择肌肉部位查找锻炼动作的工具。 | 2019 | 329 | 2021-01-21 |
| 4 | [Element (Matrix chat app) suspended from the Google Play Store](https://news.ycombinator.com/item?id=25964226) | Matrix 聊天应用 Element 被 Google Play 暂停上架。 | 2009 | 940 | 2021-01-29 |
| 5 | [U.S. Capitol Locked Down Amid Escalating Protests](https://news.ycombinator.com/item?id=25661474) | 美国国会大厦因不断升级的抗议活动封锁。 | 1986 | 2422 | 2021-01-06 |
| 6 | [Permanent suspension of @realDonaldTrump](https://news.ycombinator.com/item?id=25691912) | Twitter 宣布永久封禁特朗普的账号。 | 1961 | 1950 | 2021-01-08 |
| 7 | [Uber discovered they’d been defrauded out of 2/3 of their ad spend](https://news.ycombinator.com/item?id=25623858) | Uber 发现约三分之二广告支出遭遇欺诈。 | 1793 | 891 | 2021-01-03 |
| 8 | [GitHub is fully available in Iran](https://news.ycombinator.com/item?id=25648585) | GitHub 宣布在伊朗全面恢复服务。 | 1727 | 483 | 2021-01-05 |
| 9 | [Google Safe Browsing can kill a startup](https://news.ycombinator.com/item?id=25802366) | 作者讲述谷歌安全浏览机制可能给初创企业带来的打击。 | 1714 | 543 | 2021-01-16 |
| 10 | [A group of Google workers have announced plans to unionize](https://news.ycombinator.com/item?id=25630011) | 一批谷歌员工宣布计划组建工会。 | 1643 | 1344 | 2021-01-04 |
| 11 | [My Experience at Apple](https://news.ycombinator.com/item?id=25605211) | 作者分享在苹果工作的经历。 | 1602 | 778 | 2021-01-01 |
| 12 | [Firefox 85 cracks down on supercookies](https://news.ycombinator.com/item?id=25916513) | Firefox 85 加强对超级 Cookie 的限制。 | 1569 | 760 | 2021-01-26 |
| 13 | [GNOME has no thumbnails in the file picker and my toilets are blocked](https://news.ycombinator.com/item?id=25719796) | 作者把 GNOME 文件选择器缺少缩略图与生活困扰联系起来。 | 1505 | 724 | 2021-01-10 |
| 14 | [Amazon: Not OK – Why we had to change Elastic licensing](https://news.ycombinator.com/item?id=25833781) | Elastic 解释为何因亚马逊而修改软件许可。 | 1461 | 681 | 2021-01-19 |
| 15 | [A half-hour to learn Rust](https://news.ycombinator.com/item?id=25610741) | 用半小时快速了解 Rust 的基础。 | 1444 | 330 | 2021-01-02 |
| 16 | [The Mark Cuban Cost Plus Drug Company](https://news.ycombinator.com/item?id=25932233) | 介绍 Mark Cuban 创办的平价药品公司。 | 1434 | 807 | 2021-01-27 |
| 17 | [TabFS: Mount your Browser Tabs as a Filesystem](https://news.ycombinator.com/item?id=25600338) | TabFS 将浏览器标签页映射为可操作的文件系统。 | 1400 | 235 | 2021-01-01 |
| 18 | [Thanks HN: You helped save a company that now helps thousands make a living](https://news.ycombinator.com/item?id=25792719) | Webflow 创始人回顾 HN 如何帮助公司生存并服务更多创业者。 | 1364 | 182 | 2021-01-15 |
| 19 | [No meetings, no deadlines, no full-time employees](https://news.ycombinator.com/item?id=25673275) | 介绍没有会议、截止期限和全职员工的工作方式。 | 1329 | 517 | 2021-01-07 |
| 20 | [California law bans delivery apps from listing a restaurant without an agreement](https://news.ycombinator.com/item?id=25601814) | 加州法律禁止外卖平台未经同意收录餐厅。 | 1317 | 620 | 2021-01-01 |

## 2021-02

有效主帖 24,256 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [How I cut GTA Online loading times by 70%](https://news.ycombinator.com/item?id=26296339) | 开发者分享将 GTA Online 加载时间缩短七成的过程。 | 3883 | 699 | 2021-02-28 |
| 2 | [The Framework Laptop](https://news.ycombinator.com/item?id=26263508) | 介绍 Framework 推出的笔记本电脑。 | 2563 | 991 | 2021-02-25 |
| 3 | [Terraria on Stadia cancelled after developer's Google account gets locked](https://news.ycombinator.com/item?id=26061935) | 开发者谷歌账号被锁，《泰拉瑞亚》Stadia 版本随之取消。 | 2023 | 1174 | 2021-02-08 |
| 4 | [Show HN: Redbean – Single-file distributable web server](https://news.ycombinator.com/item?id=26271117) | Redbean 将 Web 服务器打包为单个可分发文件。 | 1998 | 249 | 2021-02-26 |
| 5 | [Email from Jeff Bezos to employees](https://news.ycombinator.com/item?id=26006656) | 阅读 Jeff Bezos 发给员工的一封邮件。 | 1941 | 1008 | 2021-02-02 |
| 6 | [Before buying a NYT subscription, here's what it'll take to cancel it](https://news.ycombinator.com/item?id=26174269) | 作者提醒订阅纽约时报前先了解取消订阅的流程。 | 1801 | 812 | 2021-02-18 |
| 7 | [My experience as a Gazan girl getting into Silicon Valley companies](https://news.ycombinator.com/item?id=26251143) | 一名加沙女孩分享进入谷歌等硅谷公司实习的经历。 | 1723 | 460 | 2021-02-24 |
| 8 | [Github1s – One second to read GitHub code with VS Code](https://news.ycombinator.com/item?id=26083919) | Github1s 让用户快速用 VS Code 风格界面浏览 GitHub 代码。 | 1692 | 214 | 2021-02-09 |
| 9 | [Draw an iceberg and see how it would float in water](https://news.ycombinator.com/item?id=26201160) | 画出冰山形状，观察它在水中如何漂浮。 | 1669 | 171 | 2021-02-20 |
| 10 | [Perseverance Rover lands on Mars [video]](https://news.ycombinator.com/item?id=26184190) | 观看毅力号火星车登陆火星的画面。 | 1663 | 495 | 2021-02-18 |
| 11 | [Total Cookie Protection](https://news.ycombinator.com/item?id=26237404) | 介绍全面 Cookie 保护机制。 | 1527 | 427 | 2021-02-23 |
| 12 | [Show HN: Can’t afford Bloomberg Terminal? No prob, I built the next best thing](https://news.ycombinator.com/item?id=26258773) | 开发者展示面向无力购买彭博终端用户的替代工具。 | 1422 | 289 | 2021-02-25 |
| 13 | [20% of requests for Wikimedia Commons are for one image of a flower](https://news.ycombinator.com/item?id=26072025) | 维基共享资源两成请求竟指向同一张花卉图片。 | 1388 | 362 | 2021-02-08 |
| 14 | [Architecture.md](https://news.ycombinator.com/item?id=26048784) | 介绍用 Architecture.md 记录项目架构的做法。 | 1349 | 153 | 2021-02-06 |
| 15 | [VideoLAN is 20 years old today](https://news.ycombinator.com/item?id=25992735) | 开源多媒体项目 VideoLAN 迎来二十周年。 | 1337 | 316 | 2021-02-01 |
| 16 | [Judge: Citibank isn't entitled to $500M it sent to various creditors last August](https://news.ycombinator.com/item?id=26180785) | 法官裁定花旗无权追回误转给债权人的五亿美元。 | 1232 | 601 | 2021-02-18 |
| 17 | [Mars becomes the 2nd planet that has more computers running Linux than Windows](https://news.ycombinator.com/item?id=26197280) | 火星成为第二个运行 Linux 的电脑比 Windows 更多的星球。 | 1185 | 283 | 2021-02-19 |
| 18 | [Help users in Iran reconnect to Signal](https://news.ycombinator.com/item?id=26026994) | 呼吁帮助伊朗用户重新连接 Signal。 | 1171 | 388 | 2021-02-04 |
| 19 | [“I saw that you spun up an Ubuntu image in Azure”](https://news.ycombinator.com/item?id=26114194) | 作者讲述在 Azure 启动 Ubuntu 镜像后引来的关注。 | 1168 | 455 | 2021-02-12 |
| 20 | [Tauri: An Electron alternative written in Rust](https://news.ycombinator.com/item?id=26194990) | 介绍以 Rust 编写、可替代 Electron 的 Tauri。 | 1113 | 417 | 2021-02-19 |

## 2021-03

有效主帖 26,473 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [GitHub, fuck your name change](https://news.ycombinator.com/item?id=26487854) | 作者强烈反对 GitHub 的名称变更。 | 3353 | 2007 | 2021-03-17 |
| 2 | [Whistleblower: Ubiquiti Breach “Catastrophic”](https://news.ycombinator.com/item?id=26638145) | 举报者称 Ubiquiti 数据泄露程度具有灾难性。 | 1944 | 785 | 2021-03-30 |
| 3 | [It Can Happen to You](https://news.ycombinator.com/item?id=26337046) | 作者提醒读者某种遭遇也可能发生在自己身上。 | 1683 | 403 | 2021-03-04 |
| 4 | [I bought 300 emoji domain names from Kazakhstan and built an email service](https://news.ycombinator.com/item?id=26422799) | 作者购买三百个哈萨克斯坦表情域名并建立邮件服务。 | 1683 | 612 | 2021-03-11 |
| 5 | [Remembering Allan McDonald, who refused to approve the Challenger launch](https://news.ycombinator.com/item?id=26380822) | 缅怀拒绝批准挑战者号发射的工程师 Allan McDonald。 | 1461 | 298 | 2021-03-07 |
| 6 | [Is that ship still stuck?](https://news.ycombinator.com/item?id=26585282) | 一个让人查询苏伊士运河堵塞船舶是否脱困的页面。 | 1453 | 1237 | 2021-03-25 |
| 7 | [All my servers have an 8 GB empty file on disk](https://news.ycombinator.com/item?id=26583791) | 作者解释为何在每台服务器上保留八 GB 空文件。 | 1345 | 696 | 2021-03-25 |
| 8 | [Moderna mRNA sequence released to GitHub [pdf]](https://news.ycombinator.com/item?id=26628233) | Moderna 疫苗的 mRNA 序列发布到 GitHub。 | 1248 | 367 | 2021-03-29 |
| 9 | [Are Xiaomi browsers spyware? Yes, they are (2020)](https://news.ycombinator.com/item?id=26306661) | 作者质疑小米浏览器存在间谍软件行为。 | 1215 | 487 | 2021-03-01 |
| 10 | [Why the Wuhan lab leak theory shouldn't be dismissed](https://news.ycombinator.com/item?id=26540458) | 作者阐述不应排除武汉实验室泄漏假说的理由。 | 1167 | 985 | 2021-03-22 |
| 11 | [Fire declared in OVH SBG2 datacentre building](https://news.ycombinator.com/item?id=26407323) | OVH 宣布 SBG2 数据中心建筑发生火灾。 | 1141 | 589 | 2021-03-10 |
| 12 | [Demoscene accepted as UNESCO cultural heritage in Germany](https://news.ycombinator.com/item?id=26522681) | 德国将演示程序文化列为非物质文化遗产。 | 1107 | 136 | 2021-03-20 |
| 13 | [Beyond Meat signs global supply deals with McDonald’s, KFC and Pizza Hut](https://news.ycombinator.com/item?id=26319850) | Beyond Meat 与麦当劳、肯德基及必胜客签订全球供应协议。 | 1105 | 910 | 2021-03-02 |
| 14 | [Click](https://news.ycombinator.com/item?id=26518290) | 《Click》以点击为主题，呈现一个供读者探索的作品。 | 1100 | 243 | 2021-03-19 |
| 15 | [Suez Canal says traffic in channel resumes after stranded ship refloated](https://news.ycombinator.com/item?id=26621308) | 苏伊士运河搁浅货轮脱困，航道恢复通行。 | 1068 | 569 | 2021-03-29 |
| 16 | [Audacity 3.0](https://news.ycombinator.com/item?id=26496887) | 开源音频编辑器 Audacity 发布 3.0 版。 | 1065 | 219 | 2021-03-17 |
| 17 | [Backblaze submitting names and sizes of files in B2 buckets to Facebook](https://news.ycombinator.com/item?id=26536019) | Backblaze 被指向 Facebook 提交 B2 桶内文件名称与大小。 | 1064 | 516 | 2021-03-22 |
| 18 | [Suez canal blocked by a massive ship](https://news.ycombinator.com/item?id=26560319) | 一艘巨轮堵塞苏伊士运河。 | 1055 | 427 | 2021-03-23 |
| 19 | [30k U.S. organizations newly hacked via holes in Microsoft Exchange Server](https://news.ycombinator.com/item?id=26362178) | 约三万家美国机构被指因 Exchange Server 漏洞遭入侵。 | 1038 | 437 | 2021-03-05 |
| 20 | [NASA's Perseverance rover sends stunning images](https://news.ycombinator.com/item?id=26323852) | NASA 毅力号火星车传回引人注目的图像。 | 1032 | 347 | 2021-03-03 |

## 2021-04

有效主帖 24,903 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Google’s copying of the Java SE API was fair use [pdf]](https://news.ycombinator.com/item?id=26699106) | 法院认定谷歌复制 Java SE API 属于合理使用。 | 4103 | 932 | 2021-04-05 |
| 2 | [“They introduce kernel bugs on purpose”](https://news.ycombinator.com/item?id=26887670) | 有人被指故意引入内核缺陷，补丁背后的目的受到质疑。 | 3025 | 1912 | 2021-04-21 |
| 3 | [Internal Combustion Engine](https://news.ycombinator.com/item?id=26991300) | 介绍内燃机如何通过燃烧燃料产生机械动力。 | 2333 | 393 | 2021-04-30 |
| 4 | [Ask HN: What tech job would let me get away with the least real work possible?](https://news.ycombinator.com/item?id=26721951) | 一位对工作失去热情的开发者询问哪些技术岗位实际工作最少。 | 2022 | 1091 | 2021-04-07 |
| 5 | [Exploiting vulnerabilities in Cellebrite UFED and Physical Analyzer](https://news.ycombinator.com/item?id=26891811) | 研究者演示对 Cellebrite 手机取证工具漏洞的利用。 | 1897 | 332 | 2021-04-21 |
| 6 | [Linux bans University of Minnesota for sending buggy patches in name of research](https://news.ycombinator.com/item?id=26889677) | Linux 因研究者故意提交缺陷补丁而禁止明尼苏达大学贡献代码。 | 1883 | 8 | 2021-04-21 |
| 7 | [Just Be Rich](https://news.ycombinator.com/item?id=26787654) | 作者审视“只要变得有钱”这一看似简单的建议。 | 1875 | 1084 | 2021-04-13 |
| 8 | [uBlock Origin works best on Firefox](https://news.ycombinator.com/item?id=26755252) | 介绍 uBlock Origin 在 Firefox 上更适合运行的原因。 | 1595 | 509 | 2021-04-09 |
| 9 | [Microsoft Coffee](https://news.ycombinator.com/item?id=26671914) | 介绍与微软咖啡有关的内容。 | 1558 | 371 | 2021-04-02 |
| 10 | [Why Lichess will always be free](https://news.ycombinator.com/item?id=26910579) | Lichess 解释为何国际象棋服务将始终免费。 | 1524 | 446 | 2021-04-23 |
| 11 | [Dan Kaminsky has died](https://news.ycombinator.com/item?id=26925044) | 安全研究者 Dan Kaminsky 去世。 | 1414 | 176 | 2021-04-24 |
| 12 | [“About one-third of Basecamp employees accepted buyouts today”](https://news.ycombinator.com/item?id=26998127) | 报道称约三分之一 Basecamp 员工接受离职补偿。 | 1366 | 1965 | 2021-04-30 |
| 13 | [The architecture behind a one-person tech startup](https://news.ycombinator.com/item?id=26737771) | 介绍一家单人技术初创公司的系统架构。 | 1330 | 320 | 2021-04-08 |
| 14 | [533M Facebook users' phone numbers and personal data have been leaked online](https://news.ycombinator.com/item?id=26681969) | 五亿三千三百万名 Facebook 用户的电话及个人信息在网上泄露。 | 1296 | 496 | 2021-04-03 |
| 15 | [Yayagram](https://news.ycombinator.com/item?id=26982286) | 认识名为 Yayagram 的项目及其开发者的创作。 | 1265 | 175 | 2021-04-29 |
| 16 | [Michael Collins, Apollo 11 astronaut, has died](https://news.ycombinator.com/item?id=26971100) | 阿波罗十一号宇航员 Michael Collins 去世。 | 1252 | 180 | 2021-04-28 |
| 17 | [Thanks for the Bonus, I Quit](https://news.ycombinator.com/item?id=26847780) | 作者讲述收到奖金后选择辞职的经历。 | 1245 | 656 | 2021-04-17 |
| 18 | [Time flies in Google Earth’s biggest update in years](https://news.ycombinator.com/item?id=26821356) | 谷歌地球发布多年最大更新，让用户观看时间流转。 | 1209 | 415 | 2021-04-15 |
| 19 | [I refused to become an FBI informant, the government put me on the no fly list](https://news.ycombinator.com/item?id=26715644) | 作者称拒绝成为 FBI 线人后被政府列入禁飞名单。 | 1206 | 487 | 2021-04-06 |
| 20 | [My Current HTML Boilerplate](https://news.ycombinator.com/item?id=26952557) | 开发者分享自己目前使用的 HTML 页面基础模板。 | 1194 | 276 | 2021-04-27 |

## 2021-05

有效主帖 24,668 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Hosting SQLite databases on GitHub Pages or any static file hoster](https://news.ycombinator.com/item?id=27016630) | 介绍将 SQLite 数据库托管在 GitHub Pages 等静态平台上的方法。 | 1812 | 244 | 2021-05-02 |
| 2 | [Ethereum will use around 99.95% less energy post merge](https://news.ycombinator.com/item?id=27194586) | 以太坊预计合并后能源消耗将降低约 99.95%。 | 1661 | 1690 | 2021-05-18 |
| 3 | [I quit my job to focus on SerenityOS full time](https://news.ycombinator.com/item?id=27317655) | 开发者辞去工作，全职投入 SerenityOS。 | 1644 | 249 | 2021-05-28 |
| 4 | [A teenager's guide to avoiding actual work](https://news.ycombinator.com/item?id=27206552) | 一份青少年视角下避免真正工作的指南。 | 1464 | 254 | 2021-05-19 |
| 5 | [Sublime Text 4](https://news.ycombinator.com/item?id=27230042) | 代码编辑器 Sublime Text 发布第四版。 | 1436 | 630 | 2021-05-21 |
| 6 | [Welcome to Libera Chat](https://news.ycombinator.com/item?id=27207734) | 介绍 IRC 社区 Libera Chat。 | 1425 | 529 | 2021-05-19 |
| 7 | [Project Starline: Feel like you're there, together](https://news.ycombinator.com/item?id=27199330) | 谷歌 Starline 项目尝试让远程交流拥有身临其境的感觉。 | 1339 | 513 | 2021-05-18 |
| 8 | [One man’s fight for the right to repair broken MacBooks](https://news.ycombinator.com/item?id=27254719) | 一位维修者为修理损坏 MacBook 的权利而抗争。 | 1331 | 544 | 2021-05-23 |
| 9 | [The Animal Is Tired](https://news.ycombinator.com/item?id=27100299) | 作者用“动物累了”这一表述传达疲惫感。 | 1299 | 426 | 2021-05-09 |
| 10 | [Bob Cassette Rewinder: Hacking Detergent DRM](https://news.ycombinator.com/item?id=27013880) | 拆解 Bob 洗碗机清洁剂的数字限制机制。 | 1260 | 404 | 2021-05-02 |
| 11 | [Modern Javascript: Everything you missed over the last 10 years (2020)](https://news.ycombinator.com/item?id=27165954) | 回顾过去十年 JavaScript 值得补课的新特性。 | 1256 | 728 | 2021-05-15 |
| 12 | [Instagram ads Facebook won't show you](https://news.ycombinator.com/item?id=27040470) | 展示 Facebook 不愿允许发布的 Instagram 广告。 | 1235 | 177 | 2021-05-04 |
| 13 | [A URL Lengthener](https://news.ycombinator.com/item?id=27156106) | 一个把网址变得更长的反向创意工具。 | 1204 | 294 | 2021-05-14 |
| 14 | [Trials begin on lozenge that rebuilds tooth enamel](https://news.ycombinator.com/item?id=27328663) | 一种旨在重建牙釉质的含片开始试验。 | 1189 | 347 | 2021-05-29 |
| 15 | [Google Docs will now use canvas based rendering](https://news.ycombinator.com/item?id=27129858) | 谷歌文档将改用 Canvas 渲染。 | 1167 | 930 | 2021-05-12 |
| 16 | [Show HN: I wrote my own RTS game engine in C](https://news.ycombinator.com/item?id=27132334) | 开发者展示自己用 C 编写的即时战略游戏引擎。 | 1102 | 262 | 2021-05-12 |
| 17 | [Drunk Post: Things I've Learned as a Sr Engineer](https://news.ycombinator.com/item?id=27333260) | 一位资深工程师借酒后随笔分享工作心得。 | 1086 | 494 | 2021-05-30 |
| 18 | [M1racles: An Apple M1 covert channel vulnerability](https://news.ycombinator.com/item?id=27285700) | M1racles 揭示苹果 M1 芯片中的隐蔽信道漏洞。 | 1067 | 277 | 2021-05-26 |
| 19 | [Amazon Prime inflates prices, using the false promise of ‘free shipping’](https://news.ycombinator.com/item?id=27333933) | 作者质疑亚马逊 Prime 以免费配送之名抬高价格。 | 1057 | 440 | 2021-05-30 |
| 20 | [Belarus 'diverts Ryanair flight to arrest journalist', opposition says](https://news.ycombinator.com/item?id=27255561) | 反对派称白俄罗斯迫使瑞安航班改道以逮捕记者。 | 1037 | 829 | 2021-05-23 |

## 2021-06

有效主帖 24,297 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Replit used legal threats to kill my open-source project](https://news.ycombinator.com/item?id=27424195) | 开发者称 Replit 通过法律威胁终结其开源项目。 | 4022 | 1274 | 2021-06-07 |
| 2 | [GitHub Copilot](https://news.ycombinator.com/item?id=27676266) | GitHub 推出代码辅助工具 Copilot。 | 2905 | 1272 | 2021-06-29 |
| 3 | [A foreign seller has hijacked my Amazon Klein bottle listing](https://news.ycombinator.com/item?id=27684807) | 卖家称自己的亚马逊克莱因瓶商品页面遭他人劫持。 | 2682 | 602 | 2021-06-30 |
| 4 | [An Unbelievable Demo](https://news.ycombinator.com/item?id=27390512) | 展示一段被作者称为难以置信的演示。 | 2339 | 463 | 2021-06-04 |
| 5 | [Stack Overflow sold to Prosus for $1.8B](https://news.ycombinator.com/item?id=27370026) | Prosus 以十八亿美元收购 Stack Overflow。 | 2330 | 846 | 2021-06-02 |
| 6 | [There are no results for tank man](https://news.ycombinator.com/item?id=27395635) | 搜索“坦克人”时出现没有结果的情况。 | 2105 | 534 | 2021-06-04 |
| 7 | [John McAfee found dead in Spanish jail after court approves extradition to US](https://news.ycombinator.com/item?id=27609027) | John McAfee 在西班牙法院批准引渡后被发现死于狱中。 | 2091 | 1086 | 2021-06-23 |
| 8 | [I wrote a children's book / illustrated guide to Apache Kafka](https://news.ycombinator.com/item?id=27541339) | 作者用儿童读物式图解介绍 Apache Kafka。 | 1797 | 226 | 2021-06-17 |
| 9 | [The top-ranking HTML editor on Google is an SEO scam](https://news.ycombinator.com/item?id=27427330) | 作者揭露谷歌排名靠前的 HTML 编辑器涉嫌 SEO 骗局。 | 1743 | 395 | 2021-06-07 |
| 10 | [The lab-leak theory: inside the fight to uncover Covid-19’s origins](https://news.ycombinator.com/item?id=27388587) | 回顾围绕新冠起源及实验室泄漏假说的调查争议。 | 1426 | 1062 | 2021-06-03 |
| 11 | [WD My Book users wake up to find their data deleted](https://news.ycombinator.com/item?id=27624735) | 西部数据 My Book 用户发现设备数据被删除。 | 1279 | 672 | 2021-06-24 |
| 12 | [Reddit’s disrespectful design](https://news.ycombinator.com/item?id=27641366) | 作者批评 Reddit 设计对用户缺乏尊重。 | 1278 | 496 | 2021-06-26 |
| 13 | [Fastly Outage](https://news.ycombinator.com/item?id=27432408) | Fastly 网络服务发生故障。 | 1255 | 694 | 2021-06-08 |
| 14 | [iOS 15 Humane](https://news.ycombinator.com/item?id=27456500) | 从人性化角度审视 iOS 15。 | 1241 | 477 | 2021-06-10 |
| 15 | [How to Work Hard](https://news.ycombinator.com/item?id=27675603) | 探讨如何持续付出高强度努力。 | 1223 | 1124 | 2021-06-29 |
| 16 | [Hundreds of fishing vessels vanishing along Argentina’s waters](https://news.ycombinator.com/item?id=27412691) | 数百艘渔船在阿根廷附近海域出现踪迹消失现象。 | 1210 | 592 | 2021-06-06 |
| 17 | [A from-scratch tour of Bitcoin in Python](https://news.ycombinator.com/item?id=27593772) | 用 Python 从零理解比特币的工作机制。 | 1208 | 277 | 2021-06-22 |
| 18 | [The 'Fuck You' Pattern](https://news.ycombinator.com/item?id=27666455) | 作者分析一种被其称为羞辱用户的设计模式。 | 1202 | 594 | 2021-06-28 |
| 19 | [Stripe Identity](https://news.ycombinator.com/item?id=27502993) | Stripe 推出身份验证服务 Identity。 | 1057 | 536 | 2021-06-14 |
| 20 | [G7: Rich nations back deal to tax multinationals](https://news.ycombinator.com/item?id=27404018) | 七国集团支持针对跨国企业征税的协议。 | 1047 | 895 | 2021-06-05 |

## 2021-07

有效主帖 22,968 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Valve Steam Deck](https://news.ycombinator.com/item?id=27846969) | Valve 发布掌机 Steam Deck。 | 2517 | 1609 | 2021-07-15 |
| 2 | [The unreasonable effectiveness of just showing up everyday](https://news.ycombinator.com/item?id=27833064) | 作者讨论每天坚持到场所产生的积累效果。 | 2075 | 579 | 2021-07-14 |
| 3 | [The Framework Laptop is now shipping](https://news.ycombinator.com/item?id=27926425) | Framework 笔记本开始发货。 | 1502 | 762 | 2021-07-23 |
| 4 | [Google Drive bans distribution of “misleading content”](https://news.ycombinator.com/item?id=27858032) | 谷歌云端硬盘禁止传播其认定的误导性内容。 | 1330 | 1520 | 2021-07-16 |
| 5 | [NDA expired, let’s spill the beans on a weird startup](https://news.ycombinator.com/item?id=27782604) | 保密协议到期后，作者讲述一家奇特初创公司的内情。 | 1328 | 447 | 2021-07-09 |
| 6 | [Copilot regurgitating Quake code, including sweary comments](https://news.ycombinator.com/item?id=27710287) | Copilot 被发现复现 Quake 代码，连带输出脏话注释。 | 1280 | 639 | 2021-07-02 |
| 7 | [How Dwarf Fortress is built](https://news.ycombinator.com/item?id=27996684) | 介绍《矮人要塞》的开发过程。 | 1130 | 388 | 2021-07-29 |
| 8 | [Media blackout after key witness against Assange admits lying](https://news.ycombinator.com/item?id=27710075) | 作者质疑阿桑奇案关键证人承认撒谎后媒体保持沉默。 | 1110 | 637 | 2021-07-02 |
| 9 | [All public GitHub code was used in training Copilot](https://news.ycombinator.com/item?id=27769440) | 报道指所有公开 GitHub 代码均被用于训练 Copilot。 | 1017 | 707 | 2021-07-08 |
| 10 | [EU withheld a study that shows piracy doesn't hurt sales (2017)](https://news.ycombinator.com/item?id=27798879) | 报道称欧盟隐瞒了一项认为盗版不损害销售的研究。 | 987 | 351 | 2021-07-11 |
| 11 | [European Parliament approves mass surveillance of private communication](https://news.ycombinator.com/item?id=27753727) | 报道称欧洲议会批准对私人通信进行大规模监控。 | 938 | 415 | 2021-07-06 |
| 12 | [Who Owns My Name?](https://news.ycombinator.com/item?id=28007547) | 作者追问谁有权控制自己的名字。 | 908 | 267 | 2021-07-30 |
| 13 | [Tesla’s $16k Quote for a $700 Fix Is Why Right to Repair Matters](https://news.ycombinator.com/item?id=27814621) | 特斯拉一万六千美元报价与七百美元维修形成对比，引出维修权讨论。 | 907 | 539 | 2021-07-12 |
| 14 | [The mermaid is taking over Google search in Norway](https://news.ycombinator.com/item?id=27991322) | 一条美人鱼如何占据挪威谷歌搜索结果。 | 903 | 346 | 2021-07-29 |
| 15 | [The Alexander: Why did you build such a long piano?](https://news.ycombinator.com/item?id=27851857) | 追问 Alexander 钢琴为何被造得如此之长。 | 884 | 186 | 2021-07-16 |
| 16 | [Assange case: Key witness admits he lied](https://news.ycombinator.com/item?id=27878902) | 阿桑奇案的一名关键证人承认提供虚假证词。 | 875 | 281 | 2021-07-19 |
| 17 | [Npm Audit: broken by design?](https://news.ycombinator.com/item?id=27761334) | 作者质疑 npm audit 的问题是否源于设计本身。 | 872 | 259 | 2021-07-07 |
| 18 | [This Website is hosted on an Casio fx-9750GII Calculator](https://news.ycombinator.com/item?id=27814080) | 一个托管在卡西欧计算器上的网站。 | 872 | 253 | 2021-07-12 |
| 19 | [Time to assume that health research is fraudulent until proven otherwise?](https://news.ycombinator.com/item?id=27884233) | 作者追问是否该对健康研究默认持怀疑态度。 | 857 | 479 | 2021-07-19 |
| 20 | [I do not agree with Github's use of copyrighted code as training for Copilot](https://news.ycombinator.com/item?id=27724042) | 作者反对 GitHub 使用受版权保护的代码训练 Copilot。 | 848 | 516 | 2021-07-03 |

## 2021-08

有效主帖 23,465 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Apple's plan to “think different” about encryption opens a backdoor to your life](https://news.ycombinator.com/item?id=28079171) | 作者认为苹果新的加密方案会给个人生活留下后门。 | 2260 | 824 | 2021-08-05 |
| 2 | [Apple's child protection features spark concern within its own ranks: sources](https://news.ycombinator.com/item?id=28162412) | 消息人士称苹果儿童保护功能在公司内部也引发担忧。 | 1778 | 813 | 2021-08-12 |
| 3 | [One Bad Apple](https://news.ycombinator.com/item?id=28110159) | 作者借“一颗坏苹果”的比喻表达对苹果的批评。 | 1484 | 524 | 2021-08-08 |
| 4 | [Climate change: IPCC report is 'code red for humanity'](https://news.ycombinator.com/item?id=28113852) | IPCC 气候报告被形容为人类面临的红色警报。 | 1465 | 1532 | 2021-08-09 |
| 5 | [Hash collision in Apple NeuralHash model](https://news.ycombinator.com/item?id=28219068) | 研究者发现苹果 NeuralHash 模型存在哈希碰撞。 | 1389 | 696 | 2021-08-18 |
| 6 | [Apple and Google must allow other in-app payment systems, Korean law declares](https://news.ycombinator.com/item?id=28366063) | 韩国法律要求苹果与谷歌允许其他应用内支付系统。 | 1354 | 599 | 2021-08-31 |
| 7 | [Apple’s Mistake](https://news.ycombinator.com/item?id=28118350) | 作者分析苹果的一项错误决定。 | 1273 | 790 | 2021-08-09 |
| 8 | [Show HN: Imba – I have spent 7 years creating a programming language for the web](https://news.ycombinator.com/item?id=28207662) | 开发者介绍耗时七年打造、编译为 JavaScript 的 Imba 语言。 | 1216 | 345 | 2021-08-17 |
| 9 | [Tech-savvy audiences block Google Analytics](https://news.ycombinator.com/item?id=28365163) | 作者观察到技术熟练用户会屏蔽 Google Analytics。 | 1214 | 681 | 2021-08-31 |
| 10 | [An Open Letter Against Apple's Privacy-Invasive Content Scanning Technology](https://news.ycombinator.com/item?id=28085632) | 一封反对苹果侵犯隐私的内容扫描技术的公开信。 | 1187 | 670 | 2021-08-06 |
| 11 | [Apple enabling client-side CSAM scanning on iPhone tomorrow](https://news.ycombinator.com/item?id=28068741) | 帖子称苹果即将在 iPhone 上启用客户端 CSAM 扫描。 | 1182 | 724 | 2021-08-05 |
| 12 | [Show HN: We built an end-to-end encrypted alternative to Google Photos](https://news.ycombinator.com/item?id=28347439) | ente 展示支持跨设备备份的端到端加密照片服务。 | 1180 | 405 | 2021-08-29 |
| 13 | [OnlyFans to block sexually explicit videos starting in October](https://news.ycombinator.com/item?id=28237274) | OnlyFans 宣布从十月起屏蔽露骨色情视频。 | 1147 | 1313 | 2021-08-19 |
| 14 | [Psst: Fast Spotify client with native GUI, without Electron, built in Rust](https://news.ycombinator.com/item?id=28203654) | Psst 以 Rust 和原生界面打造轻量 Spotify 客户端。 | 1138 | 422 | 2021-08-16 |
| 15 | [My mouse driver is asking for a firewall exemption (2019)](https://news.ycombinator.com/item?id=28274305) | 作者质疑鼠标驱动为何请求防火墙豁免。 | 1137 | 556 | 2021-08-23 |
| 16 | [An open letter against Apple's new privacy-invasive client-side content scanning](https://news.ycombinator.com/item?id=28096019) | 一封反对苹果客户端内容扫描方案的公开信。 | 1082 | 430 | 2021-08-07 |
| 17 | [China has forbidden under-18s from playing games for more than three hours/week](https://news.ycombinator.com/item?id=28356141) | 中国将未成年人游戏时间限制为每周至多三小时。 | 1030 | 1053 | 2021-08-30 |
| 18 | [CalyxOS – De-Googled Android Alternative](https://news.ycombinator.com/item?id=28090024) | 介绍去除谷歌服务依赖的 Android 替代系统 CalyxOS。 | 1010 | 477 | 2021-08-06 |
| 19 | [TikTok overtakes Facebook as most downloaded app](https://news.ycombinator.com/item?id=28133017) | TikTok 超过 Facebook 成为下载最多的应用。 | 1007 | 679 | 2021-08-10 |
| 20 | [Arm China Has Gone Rogue](https://news.ycombinator.com/item?id=28329731) | 报道讨论 Arm 中国失控的局面。 | 995 | 639 | 2021-08-27 |

## 2021-09

有效主帖 22,934 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [A search engine that favors text-heavy sites and punishes modern web design](https://news.ycombinator.com/item?id=28550764) | 一款偏爱文字密集网站、降低现代网页设计权重的搜索引擎。 | 3441 | 717 | 2021-09-16 |
| 2 | [The Framework is the most exciting laptop I've used](https://news.ycombinator.com/item?id=28606962) | 作者分享对 Framework 笔记本的积极使用体验。 | 2666 | 1407 | 2021-09-21 |
| 3 | [Disclosure of three 0-day iOS vulnerabilities](https://news.ycombinator.com/item?id=28637276) | 研究者披露三个 iOS 零日漏洞。 | 2049 | 456 | 2021-09-24 |
| 4 | [Sir Clive Sinclair has died](https://news.ycombinator.com/item?id=28554565) | 计算机先驱 Clive Sinclair 爵士去世。 | 1746 | 438 | 2021-09-16 |
| 5 | [O.mg Cable](https://news.ycombinator.com/item?id=28394035) | 介绍 O.MG 数据线项目。 | 1690 | 538 | 2021-09-02 |
| 6 | [Google Drive of historical footage locked and flagged as terrorist activity](https://news.ycombinator.com/item?id=28621412) | 历史影像的 Google Drive 被锁定并标记为恐怖活动。 | 1595 | 494 | 2021-09-22 |
| 7 | [Atlassian fired me while I was taking care of my wife who is fighting cancer](https://news.ycombinator.com/item?id=28555480) | 作者称自己照顾患癌妻子期间被 Atlassian 解雇。 | 1426 | 733 | 2021-09-16 |
| 8 | [Court issues permanent injunction in Epic vs. Apple case](https://news.ycombinator.com/item?id=28482895) | Epic 与苹果诉讼中，法院发出永久禁令。 | 1420 | 926 | 2021-09-10 |
| 9 | [YouTube is banning anti-vaccine activists and blocking all anti-vaccine content](https://news.ycombinator.com/item?id=28693060) | YouTube 宣布封禁反疫苗人士并屏蔽反疫苗内容。 | 1408 | 2924 | 2021-09-29 |
| 10 | [Apple Delays Rollout of Child Safety Features](https://news.ycombinator.com/item?id=28403727) | 苹果推迟推出儿童安全功能。 | 1401 | 838 | 2021-09-03 |
| 11 | [Show HN: 40k HN comments mentioning books, extracted using deep learning](https://news.ycombinator.com/item?id=28595967) | 借助深度学习整理四万条提及书籍的 HN 评论。 | 1359 | 273 | 2021-09-20 |
| 12 | [Tell HN: Thanks to thehodge and littlewarden.com, this site is up today](https://news.ycombinator.com/item?id=28472350) | HN 感谢用户发现证书即将过期并及时提醒网站维护者。 | 1314 | 78 | 2021-09-09 |
| 13 | [Climate activist arrested after ProtonMail provided his IP address](https://news.ycombinator.com/item?id=28427259) | ProtonMail 提供 IP 地址后，一名气候活动者遭逮捕。 | 1285 | 584 | 2021-09-05 |
| 14 | [Delays aren’t good enough – Apple must abandon its surveillance plans](https://news.ycombinator.com/item?id=28411918) | 作者要求苹果彻底放弃监控计划，而非仅延迟上线。 | 1236 | 335 | 2021-09-04 |
| 15 | [I refuse to let Amazon define Rust](https://news.ycombinator.com/item?id=28513130) | 作者反对让亚马逊主导 Rust 的方向。 | 1193 | 339 | 2021-09-13 |
| 16 | [Today Sci-Hub is 10 years old. I'll publish 2M new articles to celebrate](https://news.ycombinator.com/item?id=28421477) | Sci-Hub 十周年之际宣布新增两百万篇论文。 | 1154 | 160 | 2021-09-05 |
| 17 | [Do not leave XPS laptop in any sleep/hibernate/standby mode when placed in a bag](https://news.ycombinator.com/item?id=28639952) | 提醒将 XPS 笔记本放入包内时避免保持睡眠或休眠状态。 | 1080 | 879 | 2021-09-24 |
| 18 | [Show HN: Web browser to help programmers think clearly](https://news.ycombinator.com/item?id=28446147) | 一款旨在帮助程序员清晰思考的网页浏览器。 | 1070 | 226 | 2021-09-07 |
| 19 | [Facebook knows Instagram is toxic for teen girls, company documents show](https://news.ycombinator.com/item?id=28523688) | 内部文件显示 Facebook 知道 Instagram 对少女可能产生伤害。 | 1069 | 638 | 2021-09-14 |
| 20 | [Windy.com](https://news.ycombinator.com/item?id=28486389) | 介绍气象可视化网站 Windy.com。 | 1052 | 212 | 2021-09-10 |

## 2021-10

有效主帖 23,989 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [IoT hacking and rickrolling my high school district](https://news.ycombinator.com/item?id=28844101) | 作者讲述入侵高中学区物联网设备并播放恶搞音乐的经历。 | 1912 | 383 | 2021-10-12 |
| 2 | [Willingness to look stupid](https://news.ycombinator.com/item?id=28942189) | 探讨愿意显得笨拙对学习与成长的价值。 | 1859 | 777 | 2021-10-21 |
| 3 | [MacBook Pro 14-inch and MacBook Pro 16-inch](https://news.ycombinator.com/item?id=28908383) | 苹果发布十四英寸和十六英寸 MacBook Pro。 | 1657 | 2059 | 2021-10-18 |
| 4 | [Things I’ve learned in my 20 years as a software engineer](https://news.ycombinator.com/item?id=28797485) | 开发者总结二十年软件工程职业生涯的经验。 | 1605 | 722 | 2021-10-08 |
| 5 | [Facebook bans, sends C&D letter to developer of Unfollow Everything extension](https://news.ycombinator.com/item?id=28801908) | Facebook 封禁清空关注列表扩展的开发者并发出律师函。 | 1513 | 583 | 2021-10-08 |
| 6 | [Google has a secret deal with FB called “Jedi Blue” that they knew was illegal](https://news.ycombinator.com/item?id=28976487) | 报道称谷歌与 Facebook 的秘密广告协议被内部认定违法。 | 1417 | 405 | 2021-10-24 |
| 7 | [Pandora papers: biggest leak of offshore data exposes financial secrets of rich](https://news.ycombinator.com/item?id=28738407) | “潘多拉文件”大规模离岸数据泄漏揭示富人的财务秘密。 | 1312 | 594 | 2021-10-03 |
| 8 | [Governor vows criminal prosecution of reporter who found flaw in state website](https://news.ycombinator.com/item?id=28866805) | 州长扬言刑事起诉发现政府网站漏洞的记者。 | 1300 | 678 | 2021-10-14 |
| 9 | [Despite having just 5.8% sales, over 38% of bug reports come from Linux](https://news.ycombinator.com/item?id=28978086) | 开发者称 Linux 仅占 5.8% 销量却贡献逾 38% 缺陷报告。 | 1292 | 255 | 2021-10-24 |
| 10 | [Grand jury subpoena for Signal user data, Central District of California](https://news.ycombinator.com/item?id=29042603) | Signal 公开加州联邦大陪审团索取用户数据的传票。 | 1286 | 580 | 2021-10-29 |
| 11 | [Twitch source code and customer data has reportedly been leaked](https://news.ycombinator.com/item?id=28770590) | 报道称 Twitch 源代码及客户数据遭泄漏。 | 1271 | 581 | 2021-10-06 |
| 12 | [55 GiB/s FizzBuzz](https://news.ycombinator.com/item?id=29031488) | 展示每秒处理五十五 GiB 数据的 FizzBuzz 实现。 | 1260 | 255 | 2021-10-28 |
| 13 | [Understanding how Facebook disappeared from the internet](https://news.ycombinator.com/item?id=28752131) | 解释 Facebook 为何突然从互联网消失。 | 1226 | 260 | 2021-10-04 |
| 14 | [This word does not exist](https://news.ycombinator.com/item?id=29002776) | 介绍一个生成不存在单词的项目。 | 1184 | 413 | 2021-10-26 |
| 15 | [ Facebook Whistleblower Leaks Thousands of Pages of Incriminating Internal Docs](https://news.ycombinator.com/item?id=28761294) | Facebook 举报者披露数千页被认为对公司不利的内部文件。 | 1143 | 692 | 2021-10-05 |
| 16 | [Facebook Renames to Meta](https://news.ycombinator.com/item?id=29029317) | Facebook 宣布公司更名为 Meta。 | 1089 | 1054 | 2021-10-28 |
| 17 | [NYT journalist hacked with Pegasus after reporting on previous hacking attempts](https://news.ycombinator.com/item?id=28980382) | 纽约时报记者报道黑客攻击后又遭 Pegasus 间谍软件入侵。 | 1062 | 310 | 2021-10-24 |
| 18 | [Apple’s new M1 Pro and M1 Max processors](https://news.ycombinator.com/item?id=28908031) | 苹果发布 M1 Pro 与 M1 Max 处理器。 | 1052 | 983 | 2021-10-18 |
| 19 | [The metaverse is bullshit](https://news.ycombinator.com/item?id=29045930) | 作者强烈质疑元宇宙概念的价值。 | 1031 | 747 | 2021-10-30 |
| 20 | [Apple requires account deletion within apps in AppStore starting January 31](https://news.ycombinator.com/item?id=28776960) | 苹果要求 App Store 应用从一月三十一日起提供账号删除功能。 | 1010 | 498 | 2021-10-06 |

## 2021-11

有效主帖 22,810 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [“Click to subscribe, call to cancel” is illegal, FTC says](https://news.ycombinator.com/item?id=29250063) | 美国 FTC 称订阅可点击完成、取消却必须致电的做法违法。 | 3192 | 861 | 2021-11-17 |
| 2 | [Accepted and ghosted: interviewing for a leadership position at Stripe](https://news.ycombinator.com/item?id=29387264) | 求职者分享获 Stripe 领导岗位认可后却被冷处理的面试经历。 | 1703 | 655 | 2021-11-30 |
| 3 | [I resigned from Twitter](https://news.ycombinator.com/item?id=29380171) | 作者说明辞去 Twitter 工作的决定。 | 1692 | 1061 | 2021-11-29 |
| 4 | [Use forums rather than Slack/Discord to support developer community](https://news.ycombinator.com/item?id=29154216) | 作者建议使用论坛支持开发者社区。 | 1631 | 671 | 2021-11-08 |
| 5 | [Making the dislike count private across YouTube](https://news.ycombinator.com/item?id=29177091) | YouTube 宣布将踩按钮的计数设为私密。 | 1439 | 1514 | 2021-11-10 |
| 6 | [Firefox is the alternative to a Chrome hegemony](https://news.ycombinator.com/item?id=29378307) | 作者将 Firefox 视为抵抗 Chrome 主导地位的选择。 | 1360 | 651 | 2021-11-29 |
| 7 | [I'm “still afraid to use spaces in file names” years old](https://news.ycombinator.com/item?id=29186222) | 作者借仍不敢在文件名中用空格表达技术时代的记忆。 | 1356 | 804 | 2021-11-11 |
| 8 | [Apple announces Self Service Repair](https://news.ycombinator.com/item?id=29253047) | 苹果宣布推出自助维修服务。 | 1285 | 431 | 2021-11-17 |
| 9 | [What is AT&T doing at 1111340002?](https://news.ycombinator.com/item?id=29135559) | 追查 AT&T 在编号 1111340002 上的活动。 | 1185 | 377 | 2021-11-07 |
| 10 | [Google's infamous internal 2010 “I just want to serve 5TB” video now public](https://news.ycombinator.com/item?id=29082014) | 谷歌内部关于提供五 TB 数据的知名视频公开。 | 1130 | 513 | 2021-11-02 |
| 11 | [Einstein award going to Paul Ginsparg for creating arXiv.org](https://news.ycombinator.com/item?id=29348400) | arXiv 创建者 Paul Ginsparg 获爱因斯坦奖。 | 1128 | 97 | 2021-11-26 |
| 12 | [Apple sues NSO Group to curb the abuse of state-sponsored spyware](https://news.ycombinator.com/item?id=29320986) | 苹果起诉 NSO Group，试图遏制政府支持的间谍软件滥用。 | 1122 | 449 | 2021-11-23 |
| 13 | [How to grow sodium chloride crystals at home](https://news.ycombinator.com/item?id=29255511) | 介绍在家培育氯化钠晶体的方法。 | 1119 | 180 | 2021-11-17 |
| 14 | [Tell HN: Happy Thanksgiving Everyone](https://news.ycombinator.com/item?id=29338155) | HN 用户在感恩节感谢社区提供的知识与交流。 | 1098 | 224 | 2021-11-25 |
| 15 | [Show HN: My wife is pregnant; naturally I made a baby-name app to prepare](https://news.ycombinator.com/item?id=29118785) | 准父亲为准备孩子出生制作了起名应用。 | 1077 | 372 | 2021-11-05 |
| 16 | [QOI: Lossless Image Compression in O(n) Time](https://news.ycombinator.com/item?id=29328750) | QOI 提供线性时间的无损图像压缩方案。 | 1057 | 293 | 2021-11-24 |
| 17 | [3D printed mirror array](https://news.ycombinator.com/item?id=29191918) | 展示通过三维打印制作的镜面阵列。 | 1056 | 143 | 2021-11-11 |
| 18 | [Thank you, GitHub](https://news.ycombinator.com/item?id=29095747) | 作者向 GitHub 表达感谢。 | 1044 | 439 | 2021-11-03 |
| 19 | [Show HN: I'm 48 and finally learning how to be a game developer](https://news.ycombinator.com/item?id=29167580) | 一位四十八岁的开发者分享终于开始学习游戏开发的经历。 | 985 | 252 | 2021-11-09 |
| 20 | [Underrated Reasons to Be Thankful](https://news.ycombinator.com/item?id=29341055) | 作者列举容易被忽视、却值得感激的事情。 | 971 | 336 | 2021-11-25 |

## 2021-12

有效主帖 23,256 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Stealth bomber in flight on Google Maps](https://news.ycombinator.com/item?id=29627105) | 谷歌地图捕捉到飞行中的隐形轰炸机。 | 2244 | 373 | 2021-12-20 |
| 2 | [Ask HN: Are most of us developers lying about how much work we do?](https://news.ycombinator.com/item?id=29581125) | 一位每周实际工作五至十小时的开发者询问同行是否也夸大工作量。 | 1665 | 1058 | 2021-12-16 |
| 3 | [AWS us-east-1 outage](https://news.ycombinator.com/item?id=29473630) | AWS 美国东一区发生服务故障。 | 1658 | 957 | 2021-12-07 |
| 4 | [Open letter from the BMJ to Mark Zuckerberg](https://news.ycombinator.com/item?id=29595598) | 《英国医学杂志》向 Mark Zuckerberg 发出公开信。 | 1599 | 644 | 2021-12-17 |
| 5 | [TikTok streaming software is an illegal fork of OBS](https://news.ycombinator.com/item?id=29592103) | TikTok 直播软件被指非法分叉开源录播软件 OBS。 | 1545 | 498 | 2021-12-17 |
| 6 | [I started a paper website business](https://news.ycombinator.com/item?id=29550812) | 作者分享创办纸质网站业务的经历。 | 1511 | 257 | 2021-12-14 |
| 7 | [100 years of whatever this will be](https://news.ycombinator.com/item?id=29416606) | 以百年为尺度，思考眼前事物将演变成什么样子。 | 1475 | 896 | 2021-12-02 |
| 8 | [Log4j RCE Found](https://news.ycombinator.com/item?id=29504755) | Log4j 被发现存在远程代码执行漏洞。 | 1385 | 503 | 2021-12-09 |
| 9 | [Pixel prevented me from calling 911](https://news.ycombinator.com/item?id=29492884) | 用户称 Pixel 手机阻止自己拨打 911 急救电话。 | 1384 | 654 | 2021-12-09 |
| 10 | [Microsoft forked MIT licensed repo and changed the copyright [fixed]](https://news.ycombinator.com/item?id=29683471) | 微软曾被指分叉 MIT 许可仓库并修改版权信息，问题已修正。 | 1326 | 538 | 2021-12-25 |
| 11 | [Don't start with microservices – monoliths are your friend](https://news.ycombinator.com/item?id=29576352) | 作者建议从单体应用起步，避免过早使用微服务。 | 1230 | 445 | 2021-12-16 |
| 12 | [This website has 81% battery power remaining](https://news.ycombinator.com/item?id=29531145) | 一个展示自身剩余电量为 81% 的网站。 | 1225 | 351 | 2021-12-12 |
| 13 | [“Play-to-Earn” and Bullshit Jobs](https://news.ycombinator.com/item?id=29716900) | 探讨边玩边赚游戏与无意义工作的关系。 | 1222 | 670 | 2021-12-28 |
| 14 | [Apple CEO Tim Cook 'secretly' signed $275B deal with China in 2016](https://news.ycombinator.com/item?id=29482351) | 报道称库克在 2016 年与中国秘密签署二千七百五十亿美元协议。 | 1209 | 707 | 2021-12-08 |
| 15 | [Tell HN: You are not alone this Christmas](https://news.ycombinator.com/item?id=29682002) | 独自过圣诞节的用户向有相似处境的人送上陪伴。 | 1193 | 313 | 2021-12-25 |
| 16 | [Wish HN: Happy Holidays](https://news.ycombinator.com/item?id=29673736) | HN 社区送上节日祝福。 | 1139 | 252 | 2021-12-24 |
| 17 | [CT scans of AirPods evolution](https://news.ycombinator.com/item?id=29465668) | 借助 CT 扫描观察 AirPods 的历代变化。 | 1094 | 334 | 2021-12-06 |
| 18 | [U.S. State Department phones hacked with Israeli company spyware](https://news.ycombinator.com/item?id=29432276) | 美国国务院人员手机遭以色列公司间谍软件入侵。 | 1093 | 592 | 2021-12-03 |
| 19 | [A deep dive into an NSO zero-click iMessage exploit: Remote Code Execution](https://news.ycombinator.com/item?id=29568625) | 深入分析 NSO 利用 iMessage 实施无需点击远程代码执行的攻击。 | 1005 | 341 | 2021-12-15 |
| 20 | [Apple broke up with me](https://news.ycombinator.com/item?id=29446529) | 作者讲述自己与苹果关系破裂的经历。 | 985 | 682 | 2021-12-05 |

## 2022-01

有效主帖 26,692 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [My First Impressions of Web3](https://news.ycombinator.com/item?id=29845208) | 作者分享首次深入接触 Web3 的观察。 | 3393 | 1127 | 2022-01-07 |
| 2 | [GPS](https://news.ycombinator.com/item?id=29981188) | 介绍全球定位系统 GPS。 | 2900 | 285 | 2022-01-18 |
| 3 | [Google no longer producing high quality search results in significant categories](https://news.ycombinator.com/item?id=29772136) | 作者认为谷歌在多类搜索中已难提供高质量结果。 | 2813 | 1275 | 2022-01-02 |
| 4 | [Microsoft to Acquire Activision Blizzard](https://news.ycombinator.com/item?id=29978723) | 微软宣布收购动视暴雪。 | 2051 | 1353 | 2022-01-18 |
| 5 | [Elizabeth Holmes found guilty](https://news.ycombinator.com/item?id=29789137) | Theranos 创始人 Elizabeth Holmes 被判有罪。 | 1712 | 1234 | 2022-01-04 |
| 6 | [Tell HN: Salary data is for sale](https://news.ycombinator.com/item?id=29834753) | 用户提醒 Equifax 正出售含薪资与历史工资单的就业数据。 | 1690 | 762 | 2022-01-07 |
| 7 | [Ask HN: Gmail account security](https://news.ycombinator.com/item?id=30051054) | 用户知道密码却因设备验证无法登录 Gmail，询问解决办法。 | 1508 | 774 | 2022-01-23 |
| 8 | [I got pwned by my cloud costs](https://news.ycombinator.com/item?id=30054739) | 作者分享被云服务费用打得措手不及的经历。 | 1398 | 641 | 2022-01-24 |
| 9 | [James Webb is fully deployed](https://news.ycombinator.com/item?id=29854460) | 詹姆斯·韦布空间望远镜完成展开。 | 1384 | 494 | 2022-01-08 |
| 10 | [Do svidaniya, Igor, and thank you for Nginx](https://news.ycombinator.com/item?id=29985871) | 向 Nginx 创建者 Igor 表达告别与感谢。 | 1384 | 346 | 2022-01-18 |
| 11 | [Show HN: Looptap – A minimal game to waste your time](https://news.ycombinator.com/item?id=29921419) | Looptap 是一款适合打发时间的极简小游戏。 | 1241 | 170 | 2022-01-13 |
| 12 | [Charm – Tools to make the command line glamorous](https://news.ycombinator.com/item?id=30048332) | Charm 提供让命令行更美观的工具。 | 1195 | 213 | 2022-01-23 |
| 13 | [Open-Sourcing our Firmware](https://news.ycombinator.com/item?id=30027117) | 团队宣布开放自家固件源代码。 | 1168 | 368 | 2022-01-21 |
| 14 | [Bolt founder on Stripe/YC](https://news.ycombinator.com/item?id=30066969) | Bolt 创始人谈论 Stripe 与 Y Combinator。 | 1165 | 314 | 2022-01-25 |
| 15 | [Upwork asking me for a $12.5k refund as the client was using someone else’s card](https://news.ycombinator.com/item?id=29862860) | 自由职业者称客户盗用银行卡，Upwork 却要求自己退还一万二千五百美元。 | 1142 | 485 | 2022-01-09 |
| 16 | [I won the local election, but my township ignored the results and state law](https://news.ycombinator.com/item?id=30108998) | 作者称自己赢得地方选举，但镇政府无视结果与州法。 | 1141 | 402 | 2022-01-28 |
| 17 | [Google Drive flags file only containing “1” for copyright infringement](https://news.ycombinator.com/item?id=30060405) | 谷歌云端硬盘将仅含数字“1”的文件标记为侵权。 | 1117 | 449 | 2022-01-24 |
| 18 | [The UX on this small child is terrible](https://news.ycombinator.com/item?id=29798712) | 以用户体验评测的口吻调侃照顾幼儿的经历。 | 1079 | 357 | 2022-01-04 |
| 19 | [Essence: Desktop operating system built from scratch](https://news.ycombinator.com/item?id=29950740) | 介绍从零构建的桌面操作系统 Essence。 | 1079 | 290 | 2022-01-15 |
| 20 | [CSS Gradients that avoid the “gray dead zone”](https://news.ycombinator.com/item?id=29894608) | 介绍避免渐变中出现灰暗过渡区的 CSS 写法。 | 1075 | 141 | 2022-01-11 |

## 2022-02

有效主帖 23,343 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Google Search Is Dying](https://news.ycombinator.com/item?id=30347719) | 作者分析谷歌搜索质量衰退的迹象。 | 3636 | 1561 | 2022-02-15 |
| 2 | [Russian forces invade Ukraine after Putin orders attack](https://news.ycombinator.com/item?id=30450336) | 普京下令后，俄罗斯军队入侵乌克兰。 | 2278 | 1814 | 2022-02-24 |
| 3 | [Facebook loses users for the first time](https://news.ycombinator.com/item?id=30186326) | Facebook 用户数量首次出现下降。 | 1749 | 1352 | 2022-02-03 |
| 4 | [Namecheap: Russia Service Termination](https://news.ycombinator.com/item?id=30504812) | Namecheap 通知俄罗斯注册用户将终止服务，理由是俄乌战争。 | 1735 | 1825 | 2022-02-28 |
| 5 | [Adobe tricks users into a 12 month contract](https://news.ycombinator.com/item?id=30222165) | 作者指责 Adobe 以误导方式让用户签订十二个月合约。 | 1607 | 565 | 2022-02-05 |
| 6 | [Happy 15th birthday Hacker News](https://news.ycombinator.com/item?id=30384506) | Hacker News 迎来十五周年。 | 1450 | 202 | 2022-02-18 |
| 7 | [Google Tag Manager, the new anti-adblock weapon (2020)](https://news.ycombinator.com/item?id=30411049) | 作者分析 Google Tag Manager 如何被用于对抗广告拦截。 | 1384 | 867 | 2022-02-21 |
| 8 | [The EARN IT act is back, and it’s more dangerous than ever](https://news.ycombinator.com/item?id=30224421) | 作者警告重新提出的 EARN IT 法案风险更大。 | 1363 | 482 | 2022-02-05 |
| 9 | [Lorinda Cherry, author of dc, bc, eqn has died](https://news.ycombinator.com/item?id=30354391) | dc、bc 与 eqn 的作者 Lorinda Cherry 去世。 | 1291 | 185 | 2022-02-15 |
| 10 | [Things you notice when you quit the news (2016)](https://news.ycombinator.com/item?id=30430041) | 作者分享停止关注新闻后注意到的变化。 | 1256 | 703 | 2022-02-22 |
| 11 | [Show HN: SHA-256 explained step-by-step visually](https://news.ycombinator.com/item?id=30244534) | 用逐步可视化演示解释 SHA-256 算法。 | 1241 | 137 | 2022-02-07 |
| 12 | [City Generator](https://news.ycombinator.com/item?id=30338074) | 介绍城市生成工具。 | 1211 | 52 | 2022-02-14 |
| 13 | [Use of Google Analytics declared illegal by French data protection authority](https://news.ycombinator.com/item?id=30284372) | 法国数据保护机构裁定使用 Google Analytics 违法。 | 1172 | 1095 | 2022-02-10 |
| 14 | [Ask HN: What made your business take off that you wish you'd done much earlier?](https://news.ycombinator.com/item?id=30329762) | 征集让业务起飞、却遗憾没有更早采取的行动。 | 1147 | 466 | 2022-02-14 |
| 15 | [Major breakthrough on nuclear fusion energy](https://news.ycombinator.com/item?id=30271677) | 核聚变能源研究报告重大进展。 | 1128 | 792 | 2022-02-09 |
| 16 | [Tell HN: YouTube is banning accounts that support Ukraine](https://news.ycombinator.com/item?id=30467384) | 用户转述支持乌克兰的 YouTube 账号被封禁的报告。 | 1095 | 285 | 2022-02-25 |
| 17 | [Ask HN: How do you deal with getting old and feeling lost?](https://news.ycombinator.com/item?id=30230620) | 即将三十五岁的用户询问如何面对变老与人生迷茫。 | 1094 | 849 | 2022-02-06 |
| 18 | [Tell HN: YouTube and how my wife lost 7 years of work](https://news.ycombinator.com/item?id=30401241) | 用户求助，称 YouTube 删除了妻子七年积累的七百个培训视频。 | 1061 | 429 | 2022-02-19 |
| 19 | [Heuristics that almost always work](https://news.ycombinator.com/item?id=30264082) | 分享作者认为通常有效的经验判断规则。 | 1000 | 520 | 2022-02-08 |
| 20 | [Ukraine calls on hacker underground to defend against Russia](https://news.ycombinator.com/item?id=30462219) | 乌克兰呼吁黑客协助防御俄罗斯。 | 987 | 600 | 2022-02-25 |

## 2022-03

有效主帖 26,141 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [US Senate votes unanimously to make daylight savings time permanent](https://news.ycombinator.com/item?id=30689043) | 美国参议院一致投票支持永久实行夏令时。 | 2191 | 2218 | 2022-03-15 |
| 2 | [Pockit: A tiny, powerful, modular computer [video]](https://news.ycombinator.com/item?id=30615959) | 展示小巧且可模块化组合的 Pockit 电脑。 | 1926 | 232 | 2022-03-09 |
| 3 | [But life had other plans](https://news.ycombinator.com/item?id=30784939) | 作者讲述人生计划被现实改变的经历。 | 1718 | 225 | 2022-03-23 |
| 4 | [FTC sues Intuit for its deceptive TurboTax “free” filing campaign](https://news.ycombinator.com/item?id=30846071) | 美国 FTC 起诉 Intuit，指控 TurboTax 免费报税宣传具有欺骗性。 | 1552 | 588 | 2022-03-29 |
| 5 | [Please put units in names](https://news.ycombinator.com/item?id=30749134) | 建议在名称中直接标明数值所用的单位。 | 1284 | 594 | 2022-03-21 |
| 6 | [Mourning loss as a remote team](https://news.ycombinator.com/item?id=30811187) | 探讨远程团队如何共同面对失去同伴的悲痛。 | 1199 | 386 | 2022-03-26 |
| 7 | [Windows needs a change in priorities](https://news.ycombinator.com/item?id=30747332) | 作者呼吁 Windows 调整产品优先事项。 | 1194 | 859 | 2022-03-20 |
| 8 | [Reinstating our SAT/ACT requirement for future admissions cycles](https://news.ycombinator.com/item?id=30832350) | 介绍恢复要求申请者提交 SAT 或 ACT 成绩的决定。 | 1191 | 1100 | 2022-03-28 |
| 9 | [Apple M1 Ultra](https://news.ycombinator.com/item?id=30604470) | 苹果发布 M1 Ultra 芯片。 | 1168 | 828 | 2022-03-08 |
| 10 | [Hackers claim to have breached Okta systems](https://news.ycombinator.com/item?id=30762520) | 黑客声称已入侵 Okta 系统。 | 1158 | 375 | 2022-03-22 |
| 11 | [Show HN: I made a web game called Almost Pong](https://news.ycombinator.com/item?id=30517626) | 开发者展示完全由原生 JavaScript 生成画面与声音的 Almost Pong。 | 1135 | 181 | 2022-03-01 |
| 12 | [EU to make it mandatory to use customer-replaceable batteries in household items](https://news.ycombinator.com/item?id=30660953) | 欧盟计划要求家用产品采用消费者可自行更换的电池。 | 1099 | 637 | 2022-03-13 |
| 13 | [Start Self Hosting](https://news.ycombinator.com/item?id=30781536) | 介绍开始自托管网络服务的路径。 | 1049 | 608 | 2022-03-23 |
| 14 | [Google mandates workers back to Silicon Valley, other offices from April 4](https://news.ycombinator.com/item?id=30533540) | 谷歌要求员工从四月四日起返回硅谷等办公室。 | 1044 | 1297 | 2022-03-02 |
| 15 | [Google terminated our Developer Account, says it is “associated”](https://news.ycombinator.com/item?id=30855065) | 开发者称谷歌以账号存在关联为由终止其开发者账户。 | 997 | 477 | 2022-03-30 |
| 16 | [Earn-IT threatens encryption and therefore user freedom](https://news.ycombinator.com/item?id=30634872) | 作者认为 EARN IT 会威胁加密及用户自由。 | 990 | 201 | 2022-03-11 |
| 17 | [Difftastic: A diff that understands syntax](https://news.ycombinator.com/item?id=30841244) | Difftastic 通过理解语法来比较代码差异。 | 983 | 219 | 2022-03-29 |
| 18 | [Fire extinguished at Ukraine nuclear power plant, Europe's largest](https://news.ycombinator.com/item?id=30549116) | 乌克兰一座欧洲最大核电站的火灾被扑灭。 | 978 | 841 | 2022-03-04 |
| 19 | [The smallest and worst HDMI display](https://news.ycombinator.com/item?id=30869140) | 展示一个被称为最小也最差的 HDMI 显示器。 | 969 | 162 | 2022-03-31 |
| 20 | [SingleFile: Save a complete web page into a single HTML file](https://news.ycombinator.com/item?id=30527999) | SingleFile 可以把完整网页保存为单个 HTML 文件。 | 958 | 240 | 2022-03-02 |

## 2022-04

有效主帖 23,045 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Elon Musk makes $43B unsolicited bid to take Twitter private](https://news.ycombinator.com/item?id=31025061) | 马斯克主动提出四百三十亿美元收购 Twitter 并私有化。 | 2747 | 3078 | 2022-04-14 |
| 2 | [Twitter set to accept Musk's $43B offer – sources](https://news.ycombinator.com/item?id=31153277) | 消息人士称 Twitter 准备接受马斯克的收购报价。 | 2498 | 3676 | 2022-04-25 |
| 3 | [We lost 54k GitHub stars](https://news.ycombinator.com/item?id=31033758) | 团队讲述失去五万四千个 GitHub 星标的经历。 | 1883 | 665 | 2022-04-14 |
| 4 | [Dall-E 2](https://news.ycombinator.com/item?id=30932095) | 介绍图像生成模型 DALL·E 2。 | 1820 | 485 | 2022-04-06 |
| 5 | [A few things to know before stealing my 914](https://news.ycombinator.com/item?id=30878489) | 作者列出偷走自己 914 车辆前应知道的事情。 | 1501 | 417 | 2022-04-01 |
| 6 | [Report: 90% of nurses considering leaving the profession in the next year](https://news.ycombinator.com/item?id=31180646) | 一份报告称九成护士正在考虑一年内离职。 | 1367 | 1261 | 2022-04-27 |
| 7 | [One App – Two Worlds: This Is TikTok in Russia and Ukraine](https://news.ycombinator.com/item?id=30917474) | 比较 TikTok 在俄罗斯与乌克兰呈现的不同信息世界。 | 1260 | 348 | 2022-04-05 |
| 8 | [Inside the longest Atlassian outage](https://news.ycombinator.com/item?id=31015813) | 回顾 Atlassian 持续最久的一次服务故障。 | 1232 | 738 | 2022-04-13 |
| 9 | [Jd](https://news.ycombinator.com/item?id=30905662) | 了解 Jd 项目及其提供的功能。 | 1212 | 129 | 2022-04-04 |
| 10 | [USB-C hubs and my slow descent into madness (2021)](https://news.ycombinator.com/item?id=30911598) | 作者讲述 USB-C 集线器带来的连续困扰。 | 1144 | 513 | 2022-04-04 |
| 11 | [Etsy Strike](https://news.ycombinator.com/item?id=30989344) | 关注 Etsy 卖家的罢工行动。 | 1135 | 554 | 2022-04-11 |
| 12 | [Bits of advice I wish I had known](https://news.ycombinator.com/item?id=31199300) | 作者分享希望自己更早知道的人生建议。 | 1109 | 634 | 2022-04-28 |
| 13 | [Web scraping is legal, US appeals court reaffirms](https://news.ycombinator.com/item?id=31075396) | 美国上诉法院再次确认相关网页抓取行为合法。 | 1040 | 237 | 2022-04-18 |
| 14 | [Infinite Mac](https://news.ycombinator.com/item?id=31168646) | 介绍在浏览器中体验经典 Mac 的 Infinite Mac。 | 1038 | 323 | 2022-04-26 |
| 15 | [Framework Laptop Mainboard](https://news.ycombinator.com/item?id=31089677) | 介绍 Framework 笔记本的主板。 | 1019 | 250 | 2022-04-19 |
| 16 | [When hiring developers, have the candidate read existing code](https://news.ycombinator.com/item?id=31047409) | 建议招聘开发者时让候选人阅读已有代码。 | 996 | 543 | 2022-04-15 |
| 17 | [Airbnb’s design to live and work anywhere](https://news.ycombinator.com/item?id=31200650) | Airbnb 介绍支持员工自由选择居住与工作地点的安排。 | 961 | 716 | 2022-04-29 |
| 18 | [Show HN: Warp, a Rust-based terminal](https://news.ycombinator.com/item?id=30921231) | Warp 展示面向团队、基于 Rust 的终端并开放 Mac 公测。 | 946 | 726 | 2022-04-05 |
| 19 | [Tell HN: My kid's school installed spyware and I can't remove it](https://news.ycombinator.com/item?id=30911623) | 家长称学校在私人 Chromebook 安装监控软件，且无法自行移除。 | 936 | 417 | 2022-04-04 |
| 20 | [Heresy](https://news.ycombinator.com/item?id=30977147) | 作者以“异端”为题，提出一种挑战常规的看法。 | 929 | 1337 | 2022-04-10 |

## 2022-05

有效主帖 24,535 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Mechanical Watch](https://news.ycombinator.com/item?id=31261533) | 介绍机械手表的内部结构与运作。 | 4298 | 413 | 2022-05-04 |
| 2 | [Nvidia releases open-source GPU kernel modules](https://news.ycombinator.com/item?id=31344981) | 英伟达发布开源 GPU 内核模块。 | 2410 | 392 | 2022-05-11 |
| 3 | [My students cheated... a lot](https://news.ycombinator.com/item?id=31544634) | 教师分享学生大规模作弊的经历。 | 1840 | 1402 | 2022-05-28 |
| 4 | [The new and upgraded Framework Laptop](https://news.ycombinator.com/item?id=31433556) | Framework 推出升级版笔记本。 | 1680 | 738 | 2022-05-19 |
| 5 | [I want an iPhone Mini-sized Android phone](https://news.ycombinator.com/item?id=31411191) | 作者希望有一款尺寸接近 iPhone Mini 的 Android 手机。 | 1658 | 1053 | 2022-05-17 |
| 6 | [Including “And. And. And. And. And.” in a Google doc causes it to crash](https://news.ycombinator.com/item?id=31277998) | 重复特定英文短句会导致谷歌文档崩溃。 | 1473 | 411 | 2022-05-05 |
| 7 | [FTC fines Twitter $150M for using 2FA phone numbers for ad targeting](https://news.ycombinator.com/item?id=31510865) | Twitter 因将双重验证电话号码用于定向广告被罚一亿五千万美元。 | 1362 | 325 | 2022-05-25 |
| 8 | [I'm all-in on server-side SQLite](https://news.ycombinator.com/item?id=31318708) | 作者阐述全面采用服务端 SQLite 的决定。 | 1353 | 404 | 2022-05-09 |
| 9 | [Why do you waste so much time on the internet?](https://news.ycombinator.com/item?id=31285969) | 反思为何会在互联网上耗费大量时间。 | 1328 | 652 | 2022-05-06 |
| 10 | [“Amateur” programmer fought cancer with 50 Nvidia Geforce 1080Ti](https://news.ycombinator.com/item?id=31449147) | 一位业余程序员使用五十块 GTX 1080 Ti 参与抗癌工作。 | 1143 | 329 | 2022-05-20 |
| 11 | [No Dislikes has officially ruined YouTube for me](https://news.ycombinator.com/item?id=31324917) | 用户认为隐藏点踩数让 YouTube 充斥误导性推荐视频。 | 1097 | 479 | 2022-05-10 |
| 12 | [Apple's director of machine learning resigns due to return to office work](https://news.ycombinator.com/item?id=31298313) | 苹果机器学习主管因要求返办公室工作而辞职。 | 1069 | 703 | 2022-05-07 |
| 13 | [Twitter CEO fires two top executives, freezes hiring](https://news.ycombinator.com/item?id=31356525) | Twitter CEO 解雇两名高管并冻结招聘。 | 1032 | 936 | 2022-05-12 |
| 14 | [Imagen, a text-to-image diffusion model](https://news.ycombinator.com/item?id=31484562) | 介绍文本生成图像的扩散模型 Imagen。 | 988 | 634 | 2022-05-23 |
| 15 | [So I took a corporation to arbitration](https://news.ycombinator.com/item?id=31567673) | 作者分享将一家公司诉诸仲裁的经历。 | 986 | 399 | 2022-05-31 |
| 16 | [How to professionally say](https://news.ycombinator.com/item?id=31224996) | 介绍如何用职业化措辞表达想法。 | 979 | 393 | 2022-05-01 |
| 17 | [The Apple GPU and the impossible bug](https://news.ycombinator.com/item?id=31367365) | 讲述排查苹果 GPU 上一个看似不可能出现的缺陷。 | 965 | 95 | 2022-05-13 |
| 18 | [I spent two years launching tiny projects](https://news.ycombinator.com/item?id=31421364) | 作者回顾两年间持续发布小项目的经历。 | 923 | 197 | 2022-05-18 |
| 19 | [Dragonflydb – A modern replacement for Redis and Memcached](https://news.ycombinator.com/item?id=31560547) | DragonflyDB 提供 Redis 与 Memcached 的现代替代方案。 | 914 | 366 | 2022-05-30 |
| 20 | [We need a middle class for startups](https://news.ycombinator.com/item?id=31327219) | 作者呼吁为初创企业建立更广阔的中间生存空间。 | 899 | 305 | 2022-05-10 |

## 2022-06

有效主帖 24,292 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Supreme Court Overturns Roe vs. Wade](https://news.ycombinator.com/item?id=31862258) | 美国最高法院推翻“罗诉韦德案”判例。 | 1765 | 3463 | 2022-06-24 |
| 2 | [Tell HN: I'm Afraid We're Shutting Down](https://news.ycombinator.com/item?id=31598978) | 面向有犯罪记录者提供就业与社交服务的创业者宣布计划关闭公司。 | 1633 | 353 | 2022-06-02 |
| 3 | [Contra Wirecutter on the IKEA air purifier](https://news.ycombinator.com/item?id=31812259) | 作者反驳 Wirecutter 对宜家空气净化器的评价。 | 1474 | 705 | 2022-06-20 |
| 4 | [We are removing the option to create new subscriptions](https://news.ycombinator.com/item?id=31810104) | 服务方宣布取消创建新订阅的选项。 | 1470 | 439 | 2022-06-20 |
| 5 | [Hertzbleed Attack](https://news.ycombinator.com/item?id=31743110) | 了解 Hertzbleed 攻击及它揭示的安全问题。 | 1461 | 393 | 2022-06-14 |
| 6 | [The Floppotron 3.0](https://news.ycombinator.com/item?id=31729040) | 介绍利用硬件设备演奏音乐的 Floppotron 3.0。 | 1398 | 128 | 2022-06-13 |
| 7 | [Sunsetting Atom](https://news.ycombinator.com/item?id=31668426) | Atom 编辑器宣布走向停用。 | 1320 | 853 | 2022-06-08 |
| 8 | [Show HN: A friend and I spent 6 years making a simulation game, finally released](https://news.ycombinator.com/item?id=31586833) | 两位朋友分享六年研发模拟游戏、辞职投入并终于发布的经历。 | 1157 | 279 | 2022-06-01 |
| 9 | [Installing a payphone in my house](https://news.ycombinator.com/item?id=31593248) | 作者讲述在家中安装公共付费电话的过程。 | 1129 | 269 | 2022-06-02 |
| 10 | [Dear Spotify, can we just get a table of songs?](https://news.ycombinator.com/item?id=31618092) | 作者希望 Spotify 能直接提供歌曲表格界面。 | 1077 | 484 | 2022-06-04 |
| 11 | [The Grug Brained Developer](https://news.ycombinator.com/item?id=31840331) | 用穴居人式口吻表达对软件开发复杂性的看法。 | 1068 | 374 | 2022-06-22 |
| 12 | [Redbean 2.0 turned into more than a hobby project](https://news.ycombinator.com/item?id=31764521) | Redbean 2.0 的发展让它超出了业余项目的规模。 | 1040 | 224 | 2022-06-16 |
| 13 | [“Code” 2nd Edition](https://news.ycombinator.com/item?id=31696901) | 介绍《编码》第二版。 | 1036 | 171 | 2022-06-10 |
| 14 | [I fucking hate Jira](https://news.ycombinator.com/item?id=31813957) | 作者直率表达对 Jira 的不满。 | 971 | 526 | 2022-06-20 |
| 15 | [DNS Toys](https://news.ycombinator.com/item?id=31704789) | 介绍 DNS Toys 项目。 | 946 | 104 | 2022-06-11 |
| 16 | [Italian watchdog bans use of Google Analytics](https://news.ycombinator.com/item?id=31852384) | 意大利监管机构禁止使用 Google Analytics。 | 942 | 587 | 2022-06-23 |
| 17 | [MIT researchers uncover ‘unpatchable’ flaw in Apple M1 chips](https://news.ycombinator.com/item?id=31693490) | MIT 研究者称发现苹果 M1 芯片中无法修补的缺陷。 | 885 | 194 | 2022-06-10 |
| 18 | [What rr does](https://news.ycombinator.com/item?id=31617600) | 解释 rr 工具的作用。 | 880 | 81 | 2022-06-04 |
| 19 | [Firefox rolls out Total Cookie Protection by default to all users](https://news.ycombinator.com/item?id=31738975) | Firefox 为所有用户默认启用全面 Cookie 保护。 | 877 | 322 | 2022-06-14 |
| 20 | [GitHub Copilot is generally available](https://news.ycombinator.com/item?id=31825742) | GitHub Copilot 正式向公众开放。 | 863 | 760 | 2022-06-21 |

## 2022-07

有效主帖 24,042 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What are some cool but obscure data structures you know about?](https://news.ycombinator.com/item?id=32186203) | 征集有趣却鲜为人知的数据结构及其用途。 | 2051 | 753 | 2022-07-21 |
| 2 | [I regret my website redesign](https://news.ycombinator.com/item?id=32179563) | 作者反思自己为何后悔重新设计网站。 | 2011 | 749 | 2022-07-21 |
| 3 | [Compare Webb's Images to Hubble](https://news.ycombinator.com/item?id=32074068) | 对照韦布望远镜与哈勃望远镜拍摄的图像。 | 1636 | 244 | 2022-07-12 |
| 4 | [Standard Ebooks](https://news.ycombinator.com/item?id=32215324) | 介绍电子书项目 Standard Ebooks。 | 1578 | 255 | 2022-07-24 |
| 5 | [Apple previews Lockdown Mode](https://news.ycombinator.com/item?id=32003756) | 苹果预览强化设备安全的锁定模式。 | 1577 | 741 | 2022-07-06 |
| 6 | [Bun: Fast JavaScript runtime, transpiler, and NPM client written in Zig](https://news.ycombinator.com/item?id=31993429) | Bun 以 Zig 实现 JavaScript 运行时、转译器与 NPM 客户端。 | 1431 | 314 | 2022-07-05 |
| 7 | [Felt](https://news.ycombinator.com/item?id=31982959) | 了解 Felt 产品及其提供的使用体验。 | 1382 | 166 | 2022-07-05 |
| 8 | [Notice of termination of Twitter merger agreement](https://news.ycombinator.com/item?id=32027341) | 公布终止 Twitter 合并协议的通知。 | 1324 | 1455 | 2022-07-08 |
| 9 | [Absurd Trolley Problems](https://news.ycombinator.com/item?id=31996235) | 一组荒诞版本的电车难题。 | 1296 | 920 | 2022-07-06 |
| 10 | [I've started using Firefox and can never go back to Chrome](https://news.ycombinator.com/item?id=32126637) | 作者分享转用 Firefox 后不愿回到 Chrome 的体验。 | 1180 | 674 | 2022-07-17 |
| 11 | [Glassdoor not so anonymous](https://news.ycombinator.com/item?id=32146082) | 作者质疑 Glassdoor 所承诺的匿名性。 | 1147 | 479 | 2022-07-19 |
| 12 | [Deepest infrared image of universe](https://news.ycombinator.com/item?id=32062849) | 展示宇宙最深处的红外图像。 | 1136 | 347 | 2022-07-11 |
| 13 | [James Webb first images – complete set of high resolution shots now live](https://news.ycombinator.com/item?id=32071020) | 韦布望远镜首批完整高分辨率照片上线。 | 1109 | 396 | 2022-07-12 |
| 14 | [EU Digital Markets Act, aimed at Google, Apple, Amazon, approved](https://news.ycombinator.com/item?id=32163704) | 欧盟通过针对谷歌、苹果和亚马逊等公司的《数字市场法》。 | 1098 | 1389 | 2022-07-20 |
| 15 | [I should have loved biology](https://news.ycombinator.com/item?id=32035054) | 作者回顾自己本应爱上生物学的原因。 | 1048 | 271 | 2022-07-09 |
| 16 | [Scratch is a big deal](https://news.ycombinator.com/item?id=32120445) | 作者解释 Scratch 的重要价值。 | 1017 | 296 | 2022-07-16 |
| 17 | [HN is up again](https://news.ycombinator.com/item?id=32026571) | Hacker News 恢复上线。 | 1010 | 366 | 2022-07-08 |
| 18 | [Tell HN: You can't hire because you don't post salary ranges](https://news.ycombinator.com/item?id=32181619) | 求职者认为不公布薪资范围会阻碍招聘并浪费面试时间。 | 1010 | 523 | 2022-07-21 |
| 19 | [Pirate Library Mirror: Preserving 7TB of books (that are not in Libgen)](https://news.ycombinator.com/item?id=31970805) | 盗版图书馆镜像计划保存七 TB、不在 Libgen 中的图书。 | 996 | 418 | 2022-07-03 |
| 20 | [Uber broke laws, duped police and built lobbying operation, leak reveals](https://news.ycombinator.com/item?id=32045906) | 泄漏资料揭示 Uber 违法、欺骗警方及开展游说的行为。 | 965 | 528 | 2022-07-10 |

## 2022-08

有效主帖 24,871 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Physical buttons outperform touchscreens in new cars, test finds](https://news.ycombinator.com/item?id=32494497) | 测试发现汽车实体按钮的操作表现优于触摸屏。 | 1614 | 953 | 2022-08-17 |
| 2 | [Design the next iPhone](https://news.ycombinator.com/item?id=32567147) | 一个让用户设计下一代 iPhone 的创意项目。 | 1463 | 352 | 2022-08-23 |
| 3 | [The Big [Censored] Theory](https://news.ycombinator.com/item?id=32641028) | 审视题名中带有审查删改意味的“大型理论”。 | 1444 | 835 | 2022-08-29 |
| 4 | [4.2 Gigabytes, Or: How to Draw Anything](https://news.ycombinator.com/item?id=32651556) | 围绕四点二 GB 数据探讨如何绘制任意内容。 | 1428 | 382 | 2022-08-30 |
| 5 | [Use one big server](https://news.ycombinator.com/item?id=32319147) | 作者建议采用一台大型服务器。 | 1413 | 585 | 2022-08-02 |
| 6 | [Tell HN: Google Cloud suspended our production projects at 1am on Saturday](https://news.ycombinator.com/item?id=32547912) | 用户称已付清账单，谷歌云仍因计费问题在周六凌晨停掉生产项目。 | 1313 | 508 | 2022-08-22 |
| 7 | [Cramming 'Papers, Please' onto Phones](https://news.ycombinator.com/item?id=32371423) | 讲述将《请出示文件》移植到手机上的设计取舍。 | 1297 | 180 | 2022-08-06 |
| 8 | [Instagram can track anything you do on any website in their in-app browser](https://news.ycombinator.com/item?id=32415470) | Instagram 内置浏览器被指能追踪用户在网页上的操作。 | 1258 | 449 | 2022-08-10 |
| 9 | [Patent Trolls Inbound: Our First Lawsuit](https://news.ycombinator.com/item?id=32586898) | 团队分享首次遭遇专利流氓诉讼的经历。 | 1212 | 299 | 2022-08-24 |
| 10 | [Man who built ISP instead of paying Comcast $50K expands to hundreds of homes](https://news.ycombinator.com/item?id=32411493) | 因拒付 Comcast 五万美元而自建 ISP 的男子扩大服务范围。 | 1135 | 427 | 2022-08-10 |
| 11 | [I spent a year designing a low profile, minimal mechanical keyboard](https://news.ycombinator.com/item?id=32507172) | 作者展示用一年设计、追求低矮简洁外观的机械键盘。 | 1131 | 664 | 2022-08-18 |
| 12 | [Librarian's Letter to Google Security](https://news.ycombinator.com/item?id=32304320) | 一位图书管理员致信谷歌安全团队。 | 1082 | 461 | 2022-08-01 |
| 13 | [What’s the strangest thing you ever found in a book?](https://news.ycombinator.com/item?id=32334552) | 征集人们在书中发现过的奇怪事物。 | 1070 | 467 | 2022-08-03 |
| 14 | [An odd discovery on Spotify](https://news.ycombinator.com/item?id=32559119) | 作者分享在 Spotify 上的一项异常发现。 | 1056 | 429 | 2022-08-23 |
| 15 | [I used DALL·E 2 to generate a logo](https://news.ycombinator.com/item?id=32320491) | 作者分享用 DALL·E 2 生成标志的经历。 | 1045 | 378 | 2022-08-02 |
| 16 | [Guidance to make federally funded research freely available without delay](https://news.ycombinator.com/item?id=32596182) | 美国发布指南，要求联邦资助研究成果及时免费公开。 | 1044 | 267 | 2022-08-25 |
| 17 | [Ex-Twitter exec blows the whistle, alleging reckless cybersecurity policies](https://news.ycombinator.com/item?id=32562815) | Twitter 前高管举报公司网络安全政策草率。 | 1005 | 603 | 2022-08-23 |
| 18 | [NSA, NIST, and post-quantum crypto: my second lawsuit against the US government](https://news.ycombinator.com/item?id=32360533) | 作者因 NSA、NIST 与后量子密码问题再次起诉美国政府。 | 974 | 443 | 2022-08-05 |
| 19 | [Mikhail Gorbachev has died](https://news.ycombinator.com/item?id=32654734) | 苏联前领导人米哈伊尔·戈尔巴乔夫去世。 | 970 | 915 | 2022-08-30 |
| 20 | [A dad took photos of his toddler for a doctor – Google flagged him as a criminal](https://news.ycombinator.com/item?id=32538805) | 父亲为医生拍摄幼儿照片，却被谷歌系统标记为罪犯。 | 949 | 559 | 2022-08-21 |

## 2022-09

有效主帖 24,332 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Queen Elizabeth II has died](https://news.ycombinator.com/item?id=32768834) | 英国女王伊丽莎白二世去世。 | 2827 | 1596 | 2022-09-08 |
| 2 | [Adobe to acquire Figma for $20B](https://news.ycombinator.com/item?id=32850178) | Adobe 宣布以二百亿美元收购 Figma。 | 2348 | 1246 | 2022-09-15 |
| 3 | [Someone is pretending to be me](https://news.ycombinator.com/item?id=32996953) | 作者讲述有人冒充自己的经历。 | 2244 | 383 | 2022-09-27 |
| 4 | [Google is shutting down Stadia](https://news.ycombinator.com/item?id=33022768) | 谷歌宣布关闭云游戏平台 Stadia。 | 2090 | 1712 | 2022-09-29 |
| 5 | [After self-hosting my email for twenty-three years I have thrown in the towel](https://news.ycombinator.com/item?id=32715437) | 作者在自行托管邮件二十三年后决定放弃。 | 1887 | 728 | 2022-09-04 |
| 6 | [Show HN: I may have created a new type of puzzle](https://news.ycombinator.com/item?id=32884467) | 开发者展示自己认为可能是一种新类型的谜题。 | 1859 | 464 | 2022-09-18 |
| 7 | [Whisper – open source speech recognition by OpenAI](https://news.ycombinator.com/item?id=32927360) | OpenAI 开源语音识别系统 Whisper。 | 1705 | 481 | 2022-09-21 |
| 8 | [Stripe has decided to nuke my entire business](https://news.ycombinator.com/item?id=32854528) | 创业者称 Stripe 无明确解释停用客户收款账号，危及整个业务。 | 1624 | 678 | 2022-09-15 |
| 9 | [Someday aliens will land and all will be fine until we explain our calendar](https://news.ycombinator.com/item?id=32975173) | 借外星人理解人类历法的设想调侃日历的复杂。 | 1514 | 989 | 2022-09-25 |
| 10 | [Nightdrive](https://news.ycombinator.com/item?id=32947303) | 介绍以夜间驾驶为主题的 Nightdrive。 | 1440 | 240 | 2022-09-23 |
| 11 | [The Ethereum merge is done](https://news.ycombinator.com/item?id=32848010) | 以太坊完成合并。 | 1407 | 1548 | 2022-09-15 |
| 12 | [Mcmaster.com is the best e-commerce site I've ever used](https://news.ycombinator.com/item?id=32976978) | 作者讲述为何认为 McMaster 是自己用过最好的电商网站。 | 1402 | 491 | 2022-09-25 |
| 13 | [Ladybird: A new cross-platform browser project](https://news.ycombinator.com/item?id=32809126) | 介绍跨平台浏览器新项目 Ladybird。 | 1341 | 473 | 2022-09-12 |
| 14 | [Show HN: I'm building an open-source Amazon](https://news.ycombinator.com/item?id=32690410) | 开发者构建开源电商平台，希望商家脱离平台后仍保留基础设施。 | 1335 | 301 | 2022-09-02 |
| 15 | [Penpot: Open-source design and prototyping platform](https://news.ycombinator.com/item?id=32851262) | Penpot 提供开源设计与原型制作平台。 | 1145 | 128 | 2022-09-15 |
| 16 | [Tell HN: The Internet situation inside Iran](https://news.ycombinator.com/item?id=33025954) | 伊朗用户描述抗议期间网络被切断或限制、难以连接境外服务的处境。 | 1045 | 183 | 2022-09-29 |
| 17 | [Run Stable Diffusion on Your M1 Mac’s GPU](https://news.ycombinator.com/item?id=32678664) | 介绍用 M1 Mac 的 GPU 运行 Stable Diffusion 的方法。 | 1007 | 401 | 2022-09-01 |
| 18 | [Blocking Kiwifarms](https://news.ycombinator.com/item?id=32706673) | 介绍屏蔽 Kiwi Farms 的决定。 | 994 | 1631 | 2022-09-03 |
| 19 | [2-in-1 calculator app adds up to surprise hit for retired engineer](https://news.ycombinator.com/item?id=32902520) | 退休工程师制作的二合一计算器应用意外走红。 | 979 | 312 | 2022-09-19 |
| 20 | [Make-A-Video: AI system that generates videos from text](https://news.ycombinator.com/item?id=33020181) | Make-A-Video 尝试根据文本描述生成视频。 | 979 | 384 | 2022-09-29 |

## 2022-10

有效主帖 24,921 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Sound](https://news.ycombinator.com/item?id=33249215) | 从日常熟悉的声音出发，探索这一主题。 | 3053 | 206 | 2022-10-18 |
| 2 | [GitHub Copi­lot inves­ti­ga­tion](https://news.ycombinator.com/item?id=33240341) | 介绍针对 GitHub Copilot 的调查。 | 1847 | 1219 | 2022-10-17 |
| 3 | [Show HN: I 3D scanned the interior of the Great Pyramid at Giza](https://news.ycombinator.com/item?id=33357197) | 作者展示吉萨大金字塔内部三维扫描及在线导览。 | 1752 | 280 | 2022-10-27 |
| 4 | [The Chaostron: An Important Advance in Learning Machines (1961)](https://news.ycombinator.com/item?id=33210381) | 回顾 1961 年关于学习机器 Chaostron 的文章。 | 1487 | 19 | 2022-10-15 |
| 5 | [My dad's resume and skills from 1980](https://news.ycombinator.com/item?id=33330864) | 作者展示父亲 1980 年的简历与技能。 | 1482 | 583 | 2022-10-25 |
| 6 | [Obsidian 1.0 – Personal knowledge base app](https://news.ycombinator.com/item?id=33190433) | Obsidian 1.0 推出界面重设计和标签页，改善可用性与系统集成。 | 1329 | 565 | 2022-10-13 |
| 7 | [I help seniors with technology issues](https://news.ycombinator.com/item?id=33314291) | 作者分享帮助老年人处理技术问题的经历。 | 1276 | 811 | 2022-10-24 |
| 8 | [Kathleen Booth, the inventor of assembly language, has died](https://news.ycombinator.com/item?id=33384150) | 汇编语言发明者 Kathleen Booth 去世。 | 1252 | 140 | 2022-10-29 |
| 9 | [Nascar driver stuns to qualify for championship with GameCube move](https://news.ycombinator.com/item?id=33412702) | NASCAR 车手借鉴 GameCube 游戏动作，惊险晋级决赛。 | 1207 | 431 | 2022-10-31 |
| 10 | [How fateful?](https://news.ycombinator.com/item?id=33077473) | 追问一件事究竟有多大命运意味，思考偶然的作用。 | 1120 | 331 | 2022-10-04 |
| 11 | [Shell script best practices, from a decade of scripting things](https://news.ycombinator.com/item?id=33354286) | 总结十年 Shell 脚本实践中的良好习惯。 | 958 | 490 | 2022-10-27 |
| 12 | [Pokemon Card Animation](https://news.ycombinator.com/item?id=33363331) | 展示宝可梦卡牌动画效果。 | 944 | 122 | 2022-10-27 |
| 13 | [Knuth's Art of Computer Programming, V 4B, has gone into print](https://news.ycombinator.com/item?id=33082128) | Knuth《计算机程序设计艺术》第四卷 B 册付印。 | 940 | 342 | 2022-10-04 |
| 14 | [Fake Books](https://news.ycombinator.com/item?id=33313211) | 关注假书现象，重新审视书籍的真实性。 | 937 | 355 | 2022-10-24 |
| 15 | [How I make a living working on SerenityOS](https://news.ycombinator.com/item?id=33386163) | 开发者分享靠从事 SerenityOS 工作谋生的方式。 | 936 | 193 | 2022-10-29 |
| 16 | [GitHub Copilot, with “public code” blocked, emits my copyrighted code](https://news.ycombinator.com/item?id=33226515) | 作者称即使阻止公开代码建议，Copilot 仍会输出其受版权保护的代码。 | 914 | 775 | 2022-10-16 |
| 17 | [The HTTP crash course nobody asked for](https://news.ycombinator.com/item?id=33280605) | 一份快速认识 HTTP 的入门教程。 | 902 | 141 | 2022-10-20 |
| 18 | [Elon Musk owns Twitter: The story so far](https://news.ycombinator.com/item?id=33374770) | 回顾马斯克接管 Twitter 以来的发展。 | 898 | 1796 | 2022-10-28 |
| 19 | [Postgres WASM](https://news.ycombinator.com/item?id=33067962) | 介绍 Postgres 的 WebAssembly 版本。 | 887 | 185 | 2022-10-03 |
| 20 | [Gmail 2FA causes the homeless to permanently lose access 3 times a year](https://news.ycombinator.com/item?id=33120534) | 作者称 Gmail 双重验证让无家可归者频繁永久失去账号。 | 882 | 729 | 2022-10-07 |

## 2022-11

有效主帖 27,061 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Meta lays off 11,000 people](https://news.ycombinator.com/item?id=33529838) | Meta 宣布裁员一万一千人。 | 2048 | 1976 | 2022-11-09 |
| 2 | [Bubbles](https://news.ycombinator.com/item?id=33566924) | 以气泡为主题展开介绍。 | 1985 | 175 | 2022-11-11 |
| 3 | [Accidental Google Pixel Lock Screen Bypass](https://news.ycombinator.com/item?id=33544883) | 研究者意外发现绕过 Google Pixel 锁屏的方法。 | 1592 | 444 | 2022-11-10 |
| 4 | [Fred Brooks has died](https://news.ycombinator.com/item?id=33649390) | 计算机科学家 Fred Brooks 去世。 | 1516 | 211 | 2022-11-18 |
| 5 | [maps.google.com now redirects to google.com/maps](https://news.ycombinator.com/item?id=33729345) | maps.google.com 开始重定向到 google.com/maps。 | 1373 | 383 | 2022-11-24 |
| 6 | [Stable Diffusion 2.0](https://news.ycombinator.com/item?id=33726816) | Stable Diffusion 发布 2.0 版本。 | 1368 | 493 | 2022-11-24 |
| 7 | [Ntfy.sh – Send push notifications to your phone via PUT/POST](https://news.ycombinator.com/item?id=33517944) | ntfy.sh 支持通过 HTTP PUT 或 POST 给手机发推送。 | 1346 | 296 | 2022-11-08 |
| 8 | [Monumental (if correct) advance in number theory posted to ArXiv by Yitang Zhang](https://news.ycombinator.com/item?id=33512338) | 张益唐发布涉及朗道—西格尔零点的新结果，其正确性仍待验证。 | 1303 | 417 | 2022-11-07 |
| 9 | [Ex-Reddit CEO on Twitter moderation](https://news.ycombinator.com/item?id=33449791) | Reddit 前 CEO 谈 Twitter 的内容管理。 | 1175 | 937 | 2022-11-03 |
| 10 | [Show HN: Trading cards made with e-ink displays](https://news.ycombinator.com/item?id=33795296) | 开发者展示用电子墨水屏制作、可以动态更换内容的集换卡。 | 1149 | 291 | 2022-11-30 |
| 11 | [Kite is saying farewell and open-sourcing its code](https://news.ycombinator.com/item?id=33685209) | Kite 宣布结束服务并开源代码。 | 1083 | 528 | 2022-11-20 |
| 12 | [FTX’s Collapse Was a Crime, Not an Accident](https://news.ycombinator.com/item?id=33807257) | 作者认为 FTX 倒闭涉及犯罪，而非单纯意外。 | 1082 | 569 | 2022-11-30 |
| 13 | [Intentionally Making Close Friends](https://news.ycombinator.com/item?id=33774353) | 探讨主动建立亲密友谊的方法。 | 1076 | 307 | 2022-11-28 |
| 14 | [Twitter to employees: all office buildings closed, badge access suspended](https://news.ycombinator.com/item?id=33647882) | Twitter 通知员工关闭所有办公室并停用门禁。 | 1068 | 1652 | 2022-11-18 |
| 15 | [Hacker News Parody Thread (2013)](https://news.ycombinator.com/item?id=33680661) | 回看 2013 年模仿 HN 风格的戏仿讨论帖。 | 1049 | 329 | 2022-11-20 |
| 16 | [Twitter’s mass layoffs have begun](https://news.ycombinator.com/item?id=33463908) | Twitter 开始大规模裁员。 | 1039 | 2116 | 2022-11-04 |
| 17 | [Apple Rankings](https://news.ycombinator.com/item?id=33639206) | 查看对苹果进行排名的结果与评价。 | 1017 | 463 | 2022-11-17 |
| 18 | [Tales of the M1 GPU](https://news.ycombinator.com/item?id=33789940) | 分享探索苹果 M1 GPU 的技术故事。 | 1014 | 367 | 2022-11-29 |
| 19 | [Why Twitter didn’t go down: From a real Twitter SRE](https://news.ycombinator.com/item?id=33701371) | 一位 Twitter SRE 解释服务为何没有瘫痪。 | 1009 | 1351 | 2022-11-22 |
| 20 | [Stripe laying off around 14% of workforce](https://news.ycombinator.com/item?id=33450753) | Stripe 宣布裁减约 14% 员工。 | 997 | 1217 | 2022-11-03 |

## 2022-12

有效主帖 26,287 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [US Department of Energy: Fusion Ignition Achieved](https://news.ycombinator.com/item?id=33971377) | 美国能源部宣布实现核聚变点火。 | 2786 | 1021 | 2022-12-13 |
| 2 | [Riffusion – Stable Diffusion fine-tuned to generate Music](https://news.ycombinator.com/item?id=33999162) | Riffusion 通过微调 Stable Diffusion 生成音乐。 | 2421 | 465 | 2022-12-15 |
| 3 | [Building a Virtual Machine Inside ChatGPT](https://news.ycombinator.com/item?id=33847479) | 尝试在 ChatGPT 中构建虚拟机。 | 2029 | 908 | 2022-12-03 |
| 4 | [Carmack Leaves Meta](https://news.ycombinator.com/item?id=34022484) | John Carmack 离开 Meta。 | 1875 | 1169 | 2022-12-17 |
| 5 | [Twitter Suspends PG's Account](https://news.ycombinator.com/item?id=34044047) | Twitter 暂停 Paul Graham 的账号。 | 1790 | 1194 | 2022-12-18 |
| 6 | [Merry Christmas, HN](https://news.ycombinator.com/item?id=34121082) | HN 用户送上圣诞祝福，并鼓励感到孤独的人联系关心自己的人。 | 1659 | 221 | 2022-12-24 |
| 7 | [Apple advances user security with powerful new data protections](https://news.ycombinator.com/item?id=33897793) | 苹果宣布通过新的数据保护功能加强用户安全。 | 1587 | 1043 | 2022-12-07 |
| 8 | [Thanks Dang, Happy Holidays!](https://news.ycombinator.com/item?id=34104747) | HN 用户向 dang 致谢并送上节日祝福。 | 1452 | 152 | 2022-12-23 |
| 9 | [ElonJet Is Now Suspended](https://news.ycombinator.com/item?id=33983878) | 追踪马斯克私人飞机的 ElonJet 账号被暂停。 | 1417 | 1321 | 2022-12-14 |
| 10 | [Show HN: Obsidian Canvas – An infinite space for your ideas](https://news.ycombinator.com/item?id=34066824) | Obsidian Canvas 提供组织想法的无限画布。 | 1380 | 387 | 2022-12-20 |
| 11 | [People tricking ChatGPT “like watching an Asimov novel come to life”](https://news.ycombinator.com/item?id=33832358) | 用户诱导 ChatGPT 的现象被比作阿西莫夫小说情节。 | 1309 | 592 | 2022-12-02 |
| 12 | [SBF Arrested by Bahamian Authorities](https://news.ycombinator.com/item?id=33962083) | 巴哈马当局逮捕 Sam Bankman-Fried。 | 1308 | 812 | 2022-12-12 |
| 13 | [Show HN: I store my critical secrets and document, and communicate privately](https://news.ycombinator.com/item?id=34083366) | 开发者展示保存关键秘密、文档及开展私密交流的工具。 | 1290 | 376 | 2022-12-21 |
| 14 | [I am done. I give up](https://news.ycombinator.com/item?id=34103896) | 经历三次创业失败的用户表达放弃创业梦想的疲惫与失落。 | 1237 | 972 | 2022-12-23 |
| 15 | [Draw SVG rope using JavaScript](https://news.ycombinator.com/item?id=34197379) | 介绍用 JavaScript 绘制 SVG 绳索的方法。 | 1211 | 66 | 2022-12-31 |
| 16 | [I still use Flash in 2022](https://news.ycombinator.com/item?id=34079543) | 作者分享在 2022 年仍使用 Flash 的经历。 | 1131 | 394 | 2022-12-21 |
| 17 | [Ask HN: Has anyone here turned around their life in their 40s?](https://news.ycombinator.com/item?id=34052201) | 陷入人生低谷的用户询问四十多岁后是否仍能改变生活。 | 1127 | 726 | 2022-12-19 |
| 18 | [Twitter just banned a wave of prominent journalists with no explanation](https://news.ycombinator.com/item?id=34008383) | Twitter 在未作解释的情况下封禁多名知名记者。 | 1109 | 1659 | 2022-12-16 |
| 19 | [Paul Graham is leaving Twitter](https://news.ycombinator.com/item?id=34041985) | Paul Graham 宣布离开 Twitter。 | 1077 | 1023 | 2022-12-18 |
| 20 | [Recursive Game of Life](https://news.ycombinator.com/item?id=33978978) | 展示递归版本的生命游戏。 | 1072 | 116 | 2022-12-14 |

## 2023-01

有效主帖 27,903 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [My YouTube Earnings](https://news.ycombinator.com/item?id=34225192) | 作者公开自己的 YouTube 收入情况。 | 2015 | 403 | 2023-01-02 |
| 2 | [The Cab Ride I'll Never Forget](https://news.ycombinator.com/item?id=34398396) | 讲述一次令人难忘的出租车乘车经历。 | 1717 | 168 | 2023-01-16 |
| 3 | [NanoGPT](https://news.ycombinator.com/item?id=34336386) | 介绍语言模型训练项目 NanoGPT。 | 1532 | 320 | 2023-01-11 |
| 4 | [Google Announces Layoffs: A difficult decision to set us up for the future](https://news.ycombinator.com/item?id=34451051) | 谷歌宣布裁员，并解释其面向未来的考虑。 | 1479 | 1537 | 2023-01-20 |
| 5 | [Forking Chrome to render in a terminal](https://news.ycombinator.com/item?id=34547259) | 开发者分叉 Chrome，使其可以在终端中渲染网页。 | 1182 | 122 | 2023-01-27 |
| 6 | [Pirate Weather: A Free, Open, and Documented Forecast API](https://news.ycombinator.com/item?id=34329988) | Pirate Weather 提供免费、开放且文档完整的天气预报 API。 | 1149 | 195 | 2023-01-10 |
| 7 | [Taking over a Dead IoT Company](https://news.ycombinator.com/item?id=34325695) | 讲述接手一家已停止运营的物联网公司的经历。 | 1114 | 191 | 2023-01-10 |
| 8 | [Let's build GPT: from scratch, in code, spelled out by Andrej Karpathy](https://news.ycombinator.com/item?id=34414716) | Andrej Karpathy 用代码从零讲解如何构建 GPT。 | 1110 | 104 | 2023-01-17 |
| 9 | [Chronophoto](https://news.ycombinator.com/item?id=34559867) | 介绍 Chronophoto 项目。 | 1107 | 153 | 2023-01-28 |
| 10 | [New AI edits images based on text instructions (instructPix2Pix/imaginAIry)](https://news.ycombinator.com/item?id=34474270) | 新的 AI 工具可以依据文字指令编辑图像。 | 1098 | 227 | 2023-01-22 |
| 11 | [Microsoft and OpenAI Working on ChatGPT-Powered Bing in Challenge to Google](https://news.ycombinator.com/item?id=34242193) | 报道称微软与 OpenAI 正打造 ChatGPT 驱动的必应以挑战谷歌。 | 1092 | 897 | 2023-01-04 |
| 12 | [You Want Modules, Not Microservices](https://news.ycombinator.com/item?id=34230641) | 作者认为软件需要的是模块划分，而不是微服务。 | 1073 | 660 | 2023-01-03 |
| 13 | [HN: Thank you for being fast, ad-free and text only](https://news.ycombinator.com/item?id=34505219) | 用户感谢 HN 快速、无广告的文字体验，并建议改善手机样式。 | 1042 | 199 | 2023-01-24 |
| 14 | [Swiss retailer Galaxus now displays warranty score and return rate of products](https://news.ycombinator.com/item?id=34536344) | 瑞士零售商 Galaxus 开始显示商品保修表现与退货率。 | 1029 | 272 | 2023-01-26 |
| 15 | [how to completely own an airline in 3 easy steps](https://news.ycombinator.com/item?id=34446673) | 介绍通过三个步骤攻破航空公司系统的过程。 | 1028 | 619 | 2023-01-19 |
| 16 | [The Window Trick of Las Vegas Hotels](https://news.ycombinator.com/item?id=34568624) | 揭示拉斯维加斯酒店窗户的视觉技巧。 | 994 | 344 | 2023-01-29 |
| 17 | [How do I draw a pair of buttocks?](https://news.ycombinator.com/item?id=34257837) | 探讨如何画出臀部形态。 | 992 | 187 | 2023-01-05 |
| 18 | [Ask HN: Those making $0/month or less on side projects – Show and tell](https://news.ycombinator.com/item?id=34547265) | 邀请副业项目没有收入的开发者展示作品，让社区了解其尝试。 | 934 | 1047 | 2023-01-27 |
| 19 | [Summer Afternoon – A WebGL Experiment](https://news.ycombinator.com/item?id=34461808) | 《夏日午后》是一项 WebGL 视觉实验。 | 930 | 194 | 2023-01-20 |
| 20 | [Gail.com FAQ](https://news.ycombinator.com/item?id=34307705) | 阅读 Gail.com 的常见问题解答。 | 926 | 209 | 2023-01-09 |

## 2023-02

有效主帖 24,701 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Bing: “I will not harm you unless you harm me first”](https://news.ycombinator.com/item?id=34804874) | 必应聊天机器人声称除非先受伤害，否则不会伤害用户。 | 3363 | 1673 | 2023-02-15 |
| 2 | [Visual design rules you can safely follow every time](https://news.ycombinator.com/item?id=34684761) | 整理作者认为可反复采用的视觉设计规则。 | 1978 | 317 | 2023-02-06 |
| 3 | [Nokia launches DIY repairable budget Android phone](https://news.ycombinator.com/item?id=34938271) | 诺基亚推出支持自行维修的平价 Android 手机。 | 1792 | 1038 | 2023-02-25 |
| 4 | [GPT in 60 Lines of NumPy](https://news.ycombinator.com/item?id=34726115) | 用六十行 NumPy 代码实现 GPT。 | 1563 | 146 | 2023-02-09 |
| 5 | [Easter egg in flight path of last 747 delivery flight](https://news.ycombinator.com/item?id=34616511) | 最后一架波音 747 交付飞行的航迹藏有彩蛋。 | 1544 | 397 | 2023-02-01 |
| 6 | [Stop the proposal on mass surveillance of the EU](https://news.ycombinator.com/item?id=34626395) | 作者呼吁阻止欧盟大规模监控提案。 | 1512 | 511 | 2023-02-02 |
| 7 | [My daughter's school took over my personal Microsoft account](https://news.ycombinator.com/item?id=34934280) | 家长称女儿的学校接管了自己的微软私人账号。 | 1346 | 476 | 2023-02-25 |
| 8 | [Play Counter Strike 1.6, with full multiplayer, in the browser](https://news.ycombinator.com/item?id=34628386) | 在浏览器中游玩支持完整多人模式的《反恐精英 1.6》。 | 1345 | 500 | 2023-02-02 |
| 9 | [Tell HN: Firefox Is an awesome browser right now](https://news.ycombinator.com/item?id=34640350) | 用户分享从 Chrome 转用 Firefox 后加载 Gmail 和迁移资料的顺畅体验。 | 1310 | 598 | 2023-02-03 |
| 10 | [Introducing ChatGPT Plus](https://news.ycombinator.com/item?id=34614796) | OpenAI 推出 ChatGPT Plus 订阅服务。 | 1155 | 972 | 2023-02-01 |
| 11 | [Social media is a cause, not a correlate, of mental illness in teen girls](https://news.ycombinator.com/item?id=34901571) | 作者主张社交媒体是少女心理问题的原因，而非仅与之相关。 | 1142 | 640 | 2023-02-22 |
| 12 | [Show HN: The largest collection of ChatGPT jailbreaks on the internet](https://news.ycombinator.com/item?id=34972791) | 开发者展示收集并跟踪 ChatGPT 越狱提示词的网站。 | 1118 | 528 | 2023-02-28 |
| 13 | [Tell HN: DEI initiatives undermine the self esteem of PoC within a company](https://news.ycombinator.com/item?id=34677180) | 一位黑人从业者认为公司 DEI 活动会加重有色人种员工的冒名顶替感。 | 1091 | 832 | 2023-02-06 |
| 14 | [What Is ChatGPT Doing and Why Does It Work?](https://news.ycombinator.com/item?id=34796611) | 解释 ChatGPT 在做什么，以及它为何能够工作。 | 1090 | 496 | 2023-02-14 |
| 15 | [Bing AI Can't Be Trusted](https://news.ycombinator.com/item?id=34775853) | 作者分析必应 AI 不值得信任的问题。 | 1072 | 601 | 2023-02-13 |
| 16 | [Reverse Engineering a Mysterious UDP Stream in My Hotel](https://news.ycombinator.com/item?id=34912300) | 作者逆向分析酒店网络中的神秘 UDP 数据流。 | 1044 | 179 | 2023-02-23 |
| 17 | [TabFS – a browser extension that mounts the browser tabs as a filesystem](https://news.ycombinator.com/item?id=34847611) | TabFS 将浏览器标签页挂载为文件系统。 | 1033 | 193 | 2023-02-18 |
| 18 | [The Missing Semester of Your CS Education](https://news.ycombinator.com/item?id=34934216) | 补充计算机教育中常缺少的工具与实践技能。 | 1024 | 336 | 2023-02-25 |
| 19 | [Sundar Pichai: An important next step on our AI journey](https://news.ycombinator.com/item?id=34682340) | Sundar Pichai 介绍谷歌人工智能发展的下一步。 | 988 | 954 | 2023-02-06 |
| 20 | [Lab Leak Most Likely Origin of Covid-19 Pandemic, U.S. Agency Now Says](https://news.ycombinator.com/item?id=34945078) | 美国一家机构认为实验室泄漏是新冠最可能的起源。 | 983 | 980 | 2023-02-26 |

## 2023-03

有效主帖 28,315 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [GPT-4](https://news.ycombinator.com/item?id=35154527) | OpenAI 发布 GPT-4。 | 4091 | 2507 | 2023-03-14 |
| 2 | [FDIC Takes over Silicon Valley Bank](https://news.ycombinator.com/item?id=35096877) | 美国联邦存款保险公司接管硅谷银行。 | 3172 | 1576 | 2023-03-10 |
| 3 | [Bicycle](https://news.ycombinator.com/item?id=35343495) | 以自行车为主角，重新认识这件日常交通工具。 | 3014 | 399 | 2023-03-28 |
| 4 | [Gordon Moore, Intel Co-Founder, Dies at 94](https://news.ycombinator.com/item?id=35297420) | 英特尔联合创始人 Gordon Moore 去世，享年九十四岁。 | 2594 | 234 | 2023-03-25 |
| 5 | [ChatGPT Plugins](https://news.ycombinator.com/item?id=35277677) | ChatGPT 推出插件功能。 | 1875 | 1106 | 2023-03-23 |
| 6 | [Get Off My Desktop Windows Needs to Stop Showing Tabloid News](https://news.ycombinator.com/item?id=35323121) | 作者要求 Windows 停止在桌面展示低质新闻。 | 1725 | 850 | 2023-03-27 |
| 7 | [Twitter open sourced the recommendation engine](https://news.ycombinator.com/item?id=35391433) | Twitter 开源推荐系统。 | 1700 | 1185 | 2023-03-31 |
| 8 | [Signature Bank Closed by FDIC](https://news.ycombinator.com/item?id=35127063) | 美国联邦存款保险公司关闭 Signature Bank。 | 1699 | 2512 | 2023-03-12 |
| 9 | [OpenAI Is Now Everything It Promised Not to Be: Closed-Source, and For-Profit](https://news.ycombinator.com/item?id=34979981) | 作者批评 OpenAI 转向闭源与盈利，背离早期承诺。 | 1623 | 567 | 2023-03-01 |
| 10 | [Docker is deleting Open Source images - here is what you need to know](https://news.ycombinator.com/item?id=35166317) | 介绍 Docker 删除开源镜像相关变更及其影响。 | 1556 | 738 | 2023-03-15 |
| 11 | [Introducing ChatGPT and Whisper APIs](https://news.ycombinator.com/item?id=34985848) | OpenAI 推出 ChatGPT 与 Whisper API。 | 1423 | 668 | 2023-03-01 |
| 12 | [Llama.cpp 30B runs with only 6GB of RAM now](https://news.ycombinator.com/item?id=35393284) | llama.cpp 的三百亿参数模型可在仅六 GB 内存下运行。 | 1311 | 414 | 2023-03-31 |
| 13 | [We updated our RSA SSH host key](https://news.ycombinator.com/item?id=35285390) | 服务方说明更新 RSA SSH 主机密钥的操作。 | 1265 | 488 | 2023-03-24 |
| 14 | [Apple Passwords Deserve an App](https://news.ycombinator.com/item?id=35329950) | 作者认为苹果密码管理功能值得拥有独立应用。 | 1260 | 402 | 2023-03-27 |
| 15 | [Rapid growth, lessons learned and improvements at Fly.io](https://news.ycombinator.com/item?id=35044516) | Fly.io 回顾快速增长中的经验与改进。 | 1226 | 455 | 2023-03-06 |
| 16 | [Judge Decides Against Internet Archive](https://news.ycombinator.com/item?id=35297117) | 法官作出不利于互联网档案馆的裁决。 | 1116 | 793 | 2023-03-24 |
| 17 | [So you've installed `fzf`. Now what?](https://news.ycombinator.com/item?id=35248098) | 介绍安装 fzf 后可以如何使用它。 | 1102 | 285 | 2023-03-21 |
| 18 | [GitHub Copilot X: The AI-powered developer experience](https://news.ycombinator.com/item?id=35261065) | GitHub 推出面向 AI 开发体验的 Copilot X。 | 1096 | 751 | 2023-03-22 |
| 19 | [Samsung “space zoom” moon shots are fake, and here is the proof](https://news.ycombinator.com/item?id=35107601) | 作者认为三星“太空变焦”月亮照片存在造假，并展示证据。 | 1024 | 386 | 2023-03-11 |
| 20 | [Meta to Layoff 10k Employees](https://news.ycombinator.com/item?id=35150909) | Meta 宣布裁员一万人。 | 1022 | 831 | 2023-03-14 |

## 2023-04

有效主帖 26,088 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Remembering Bob Lee](https://news.ycombinator.com/item?id=35457341) | HN 用户缅怀技术贡献广泛、乐于分享的工程师 Bob Lee。 | 2090 | 217 | 2023-04-05 |
| 2 | [Ask HN: Most interesting tech you built for just yourself?](https://news.ycombinator.com/item?id=35729232) | 征集大家只为自己打造的有趣技术项目。 | 1901 | 1792 | 2023-04-27 |
| 3 | [If we lose the Internet Archive, we’re screwed](https://news.ycombinator.com/item?id=35468753) | 作者阐述失去互联网档案馆将造成的严重影响。 | 1790 | 588 | 2023-04-06 |
| 4 | [Stability AI Launches the First of Its StableLM Suite of Language Models](https://news.ycombinator.com/item?id=35629127) | Stability AI 发布首批 StableLM 语言模型。 | 1502 | 497 | 2023-04-19 |
| 5 | [Space Elevator](https://news.ycombinator.com/item?id=35629972) | 认识试图连接地面与太空的电梯构想。 | 1456 | 207 | 2023-04-19 |
| 6 | [Show HN: GPT-4-powered web searches for developers](https://news.ycombinator.com/item?id=35543668) | Phind 为开发者搜索引入 GPT-4，并结合网页和文档生成回答。 | 1401 | 414 | 2023-04-12 |
| 7 | [The Early Days of Linux](https://news.ycombinator.com/item?id=35557848) | 回顾 Linux 发展的早期历史。 | 1378 | 224 | 2023-04-13 |
| 8 | [Semaphore: A Full-Body Keyboard](https://news.ycombinator.com/item?id=35536550) | Semaphore 将全身动作变成键盘输入。 | 1362 | 209 | 2023-04-12 |
| 9 | [The Glorious Return of a Humble Car Feature](https://news.ycombinator.com/item?id=35720865) | 介绍一项朴素汽车功能的回归。 | 1322 | 979 | 2023-04-26 |
| 10 | [Bob Lee, Former CTO Square, Creator of CashApp, Stabbed to Death in SF](https://news.ycombinator.com/item?id=35448899) | Cash App 创建者、Square 前 CTO Bob Lee 在旧金山遇刺身亡。 | 1314 | 2780 | 2023-04-05 |
| 11 | [The Earn IT Bill Is Back, Seeking to Scan Our Messages and Photos](https://news.ycombinator.com/item?id=35655282) | 作者警告重提的 EARN IT 法案可能促使扫描私人消息与照片。 | 1264 | 463 | 2023-04-21 |
| 12 | [Clock](https://news.ycombinator.com/item?id=35620291) | 以时钟为主角，探索这件日常计时工具。 | 1232 | 164 | 2023-04-18 |
| 13 | [The Mullvad Browser](https://news.ycombinator.com/item?id=35421034) | 介绍 Mullvad 浏览器。 | 1182 | 419 | 2023-04-03 |
| 14 | [Microsoft fixes 5-year-old Defender bug, reducing Firefox-related CPU use by 75%](https://news.ycombinator.com/item?id=35511713) | 微软修复五年前的 Defender 缺陷，大幅降低 Firefox 相关 CPU 占用。 | 1163 | 422 | 2023-04-10 |
| 15 | [The Day Windows Died](https://news.ycombinator.com/item?id=35415758) | 作者以 Windows 的“消亡”为喻，表达对其变化的判断。 | 1146 | 893 | 2023-04-02 |
| 16 | [Load Balancing](https://news.ycombinator.com/item?id=35588797) | 介绍负载均衡的相关原理。 | 1143 | 217 | 2023-04-16 |
| 17 | [World’s largest battery maker announces major breakthrough in energy density](https://news.ycombinator.com/item?id=35649935) | 全球最大电池制造商宣布能量密度取得重大突破。 | 1099 | 843 | 2023-04-21 |
| 18 | [Datomic Is Now Free](https://news.ycombinator.com/item?id=35727967) | Datomic 宣布免费提供。 | 1099 | 368 | 2023-04-27 |
| 19 | [Astral](https://news.ycombinator.com/item?id=35617198) | 了解 Astral 项目及其开发方向。 | 1078 | 236 | 2023-04-18 |
| 20 | [Smartphones with Qualcomm Chip Share Private Information with US Chip-Maker](https://news.ycombinator.com/item?id=35698547) | 搭载高通芯片的手机被指向芯片制造商共享私人信息。 | 1077 | 330 | 2023-04-25 |

## 2023-05

有效主帖 27,217 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Google “We Have No Moat, and Neither Does OpenAI”](https://news.ycombinator.com/item?id=35813322) | 谷歌内部文章认为自己与 OpenAI 都缺乏竞争护城河。 | 2455 | 1039 | 2023-05-04 |
| 2 | [Had a call with Reddit to discuss pricing. Bad news for third-party apps](https://news.ycombinator.com/item?id=36141083) | 第三方应用开发者与 Reddit 洽谈 API 价格后分享坏消息。 | 1984 | 1294 | 2023-05-31 |
| 3 | [A highly intuitive visual guide on how memory allocation works, step by step](https://news.ycombinator.com/item?id=36029087) | 用逐步可视化方式直观解释内存分配。 | 1360 | 177 | 2023-05-22 |
| 4 | [Rarbg Is No More](https://news.ycombinator.com/item?id=36136819) | 种子网站 RARBG 宣布停止运营。 | 1352 | 646 | 2023-05-31 |
| 5 | [See this page fetch itself, byte by byte, over TLS](https://news.ycombinator.com/item?id=35884437) | 观察网页如何通过 TLS 逐字节抓取自身内容。 | 1341 | 173 | 2023-05-10 |
| 6 | [Slide to Unlock](https://news.ycombinator.com/item?id=36138304) | 重新关注熟悉的滑动解锁操作及其呈现方式。 | 1185 | 220 | 2023-05-31 |
| 7 | [Get Started Making Music](https://news.ycombinator.com/item?id=35935796) | 为想开始创作音乐的人提供入门指引。 | 1176 | 243 | 2023-05-14 |
| 8 | [Show HN: Boring Report, a news app that uses AI to desensationalize the news](https://news.ycombinator.com/item?id=35905437) | Boring Report 用语言模型去除新闻煽情措辞，帮助读者聚焦事实。 | 1166 | 332 | 2023-05-11 |
| 9 | [PyPI Was Subpoenaed](https://news.ycombinator.com/item?id=36061407) | Python 软件包仓库 PyPI 收到传票。 | 1153 | 597 | 2023-05-24 |
| 10 | [Federal Judge Makes History: Border Searches of Cell Phones Require Warrants](https://news.ycombinator.com/item?id=36130166) | 美国联邦法官裁定边境搜查手机需要搜查令。 | 1050 | 319 | 2023-05-30 |
| 11 | [JMAP – a much needed modern email open standard](https://news.ycombinator.com/item?id=36127703) | JMAP 为电子邮件提供现代开放标准。 | 1030 | 361 | 2023-05-30 |
| 12 | [It's A(door)able](https://news.ycombinator.com/item?id=35800492) | 认识名字中包含“门”字双关的 It's A(door)able。 | 1026 | 114 | 2023-05-03 |
| 13 | [MSFT is forcing Outlook and Teams to open links in Edge and IT admins are angry](https://news.ycombinator.com/item?id=35800158) | 微软强制 Outlook 与 Teams 用 Edge 打开链接，引发管理员不满。 | 1014 | 722 | 2023-05-03 |
| 14 | [‘The Godfather of A.I.’ Leaves Google and Warns of Danger Ahead](https://news.ycombinator.com/item?id=35771104) | 被称为“AI 教父”的研究者离开谷歌并警告未来风险。 | 1008 | 1183 | 2023-05-01 |
| 15 | [Prime Video Abandons Serverless Distributed Stack for Monolith, saves 90%](https://news.ycombinator.com/item?id=35811741) | Prime Video 部分系统从无服务器分布式设计转为单体，成本降低九成。 | 989 | 507 | 2023-05-04 |
| 16 | [Let us serve you, but don't bring us down](https://news.ycombinator.com/item?id=36110527) | 服务方呼吁用户在使用服务时避免造成系统瘫痪。 | 976 | 243 | 2023-05-29 |
| 17 | [Ask HN: Is it just me or GPT-4's quality has significantly deteriorated lately?](https://news.ycombinator.com/item?id=36134249) | 用户询问 GPT-4 回答是否近期变快却变浅、代码错误也增多。 | 947 | 756 | 2023-05-31 |
| 18 | [When you lose the ability to write, you also lose some of your ability to think](https://news.ycombinator.com/item?id=35896190) | 作者认为失去写作能力也会削弱思考能力。 | 941 | 571 | 2023-05-11 |
| 19 | [Everything You Always Wanted to Know About Mathematics [pdf]](https://news.ycombinator.com/item?id=36069847) | 一本汇集广泛数学知识的材料。 | 941 | 147 | 2023-05-25 |
| 20 | [Don Knuth Plays with ChatGPT](https://news.ycombinator.com/item?id=36012360) | Donald Knuth 探索 ChatGPT 的表现。 | 927 | 622 | 2023-05-20 |

## 2023-06

有效主帖 26,339 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Apollo will close down on June 30th](https://news.ycombinator.com/item?id=36245435) | Reddit 客户端 Apollo 宣布六月三十日关闭。 | 3421 | 1609 | 2023-06-08 |
| 2 | [Apple Vision Pro: Apple’s first spatial computer](https://news.ycombinator.com/item?id=36201593) | 苹果推出首款空间计算设备 Vision Pro。 | 2608 | 2843 | 2023-06-05 |
| 3 | [macOS Command-Line Tools You Might Not Know About](https://news.ycombinator.com/item?id=36491704) | 介绍一些容易被忽视的 macOS 命令行工具。 | 2039 | 442 | 2023-06-27 |
| 4 | [Reddit Strike Has Started](https://news.ycombinator.com/item?id=36283249) | Reddit 社区开始罢工抗议。 | 1997 | 1142 | 2023-06-11 |
| 5 | [Reddit is removing moderators that protest by taking their communities private](https://news.ycombinator.com/item?id=36350938) | Reddit 撤换将社区设为私密以示抗议的版主。 | 1776 | 1060 | 2023-06-16 |
| 6 | [Everything that uses configuration files should report where they're located](https://news.ycombinator.com/item?id=36465886) | 建议所有使用配置文件的软件都应报告文件所在位置。 | 1744 | 472 | 2023-06-25 |
| 7 | [The rule says, “No vehicles in the park”](https://news.ycombinator.com/item?id=36453856) | 借“公园禁止车辆”这一规则探讨其含义与边界。 | 1572 | 1186 | 2023-06-23 |
| 8 | [The Password Game](https://news.ycombinator.com/item?id=36493715) | 一款围绕不断增加密码要求展开的游戏。 | 1413 | 486 | 2023-06-27 |
| 9 | [Our right to challenge junk patents is under threat](https://news.ycombinator.com/item?id=36198329) | 作者警告公众挑战低质专利的权利正受到威胁。 | 1291 | 212 | 2023-06-05 |
| 10 | [Twitter now requires an account to view tweets](https://news.ycombinator.com/item?id=36540957) | Twitter 开始要求登录账号才能查看推文。 | 1285 | 1179 | 2023-06-30 |
| 11 | [Reddit experiments on users, forcing them to install app or else not use Reddit](https://news.ycombinator.com/item?id=36287411) | Reddit 被指试验强迫用户安装应用才能继续访问。 | 1273 | 639 | 2023-06-12 |
| 12 | [Reddit’s plan to kill third-party apps sparks widespread protests](https://news.ycombinator.com/item?id=36210805) | Reddit 限制第三方应用的计划引发广泛抗议。 | 1108 | 498 | 2023-06-06 |
| 13 | [Do, or do not. There is no try](https://news.ycombinator.com/item?id=36461102) | 围绕“做或不做，没有尝试”这句话展开思考。 | 1096 | 182 | 2023-06-24 |
| 14 | [Apollo is dead. Long live Apollo](https://news.ycombinator.com/item?id=36543894) | Apollo 关闭之际，用户感叹其代表的创造力与互联网精神。 | 1036 | 383 | 2023-06-30 |
| 15 | [My 24 year old HP Jornada can do things an iPhone still can't do](https://news.ycombinator.com/item?id=36346254) | 作者比较二十四年前的 HP Jornada 与 iPhone 的能力差异。 | 981 | 1152 | 2023-06-15 |
| 16 | [Affirmative action at US colleges has been banned](https://news.ycombinator.com/item?id=36520658) | 美国大学招生中的平权行动被禁止。 | 959 | 1681 | 2023-06-29 |
| 17 | [Imaginary Problems Are the Root of Bad Software](https://news.ycombinator.com/item?id=36380711) | 作者认为凭空设想的问题是糟糕软件的根源。 | 946 | 393 | 2023-06-18 |
| 18 | [Full Time](https://news.ycombinator.com/item?id=36356876) | 以“全职”为切入点，审视工作所占据的时间。 | 932 | 148 | 2023-06-16 |
| 19 | [French govt. says users of uBlock Origin, Signal etc. are potential terrorists](https://news.ycombinator.com/item?id=36428046) | 报道称法国政府将 uBlock Origin、Signal 等工具用户视为潜在恐怖分子。 | 923 | 508 | 2023-06-22 |
| 20 | [Google has a secret browser hidden inside the settings](https://news.ycombinator.com/item?id=36478206) | 谷歌设置中被发现藏有浏览器功能。 | 914 | 312 | 2023-06-26 |

## 2023-07

有效主帖 26,575 条；排名来源 algolia+firebase。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Kevin Mitnick has died](https://news.ycombinator.com/item?id=36795173) | 知名黑客 Kevin Mitnick 去世。 | 3699 | 613 | 2023-07-19 |
| 2 | [Llama 2 – Meta AI](https://news.ycombinator.com/item?id=36774627) | Meta 发布 Llama 2 人工智能模型。 | 2268 | 820 | 2023-07-18 |
| 3 | [The First Room-Temperature Ambient-Pressure Superconductor](https://news.ycombinator.com/item?id=36864624) | 研究者宣称发现首个常温常压超导体。 | 1690 | 877 | 2023-07-25 |
| 4 | [Stanford president resigns over manipulated research, will retract 3 papers](https://news.ycombinator.com/item?id=36790301) | 斯坦福校长因研究造假争议辞职，并将撤回三篇论文。 | 1507 | 777 | 2023-07-19 |
| 5 | [Apple says it'll remove iMessage and FaceTime in UK rather than break encryption](https://news.ycombinator.com/item?id=36800297) | 苹果表示宁可在英国撤下 iMessage 与 FaceTime，也不破坏加密。 | 1495 | 749 | 2023-07-20 |
| 6 | [Twitter Is DDOSing Itself](https://news.ycombinator.com/item?id=36553236) | 作者分析 Twitter 如何对自身造成类似 DDoS 的压力。 | 1396 | 1242 | 2023-07-01 |
| 7 | [Google is already pushing WEI (web DRM) into Chromium](https://news.ycombinator.com/item?id=36876301) | 谷歌被指已开始将网页完整性验证机制加入 Chromium。 | 1376 | 839 | 2023-07-26 |
| 8 | [Every time you click this link, it will send you to a random Web 1.0 website](https://news.ycombinator.com/item?id=36739920) | 一个每次点击都会跳转到随机早期互联网网站的链接。 | 1352 | 352 | 2023-07-15 |
| 9 | [Zenbleed](https://news.ycombinator.com/item?id=36848680) | 介绍 Zenbleed 漏洞。 | 1283 | 361 | 2023-07-24 |
| 10 | [Firefox has surpassed Chrome on Speedometer](https://news.ycombinator.com/item?id=36770883) | Firefox 在 Speedometer 基准测试中超过 Chrome。 | 1282 | 544 | 2023-07-18 |
| 11 | [Breaking Superconductor News](https://news.ycombinator.com/item?id=36881808) | 关注超导体研究的最新消息。 | 1239 | 470 | 2023-07-26 |
| 12 | [Common Pitfalls in Go Benchmarking](https://news.ycombinator.com/item?id=36860065) | 梳理 Go 基准测试中容易让测量结果失真的常见陷阱。（补查时已标记dead；评论数沿用原始快照） | 1205 | 3 | 2023-07-25 |
| 13 | [FedNow Is Live](https://news.ycombinator.com/item?id=36801491) | 美国即时支付系统 FedNow 正式上线。 | 1177 | 1022 | 2023-07-20 |
| 14 | [Nifflas: “When an app asks for permission feed fake data” – Fosstodon](https://news.ycombinator.com/item?id=36644895) | Nifflas 建议应用请求权限时可向其提供虚假数据。 | 1102 | 395 | 2023-07-08 |
| 15 | [Google’s nightmare “Web Integrity API” wants a DRM gatekeeper for the web](https://news.ycombinator.com/item?id=36854114) | 作者担忧谷歌 Web Integrity API 会为网络设置 DRM 守门机制。 | 1090 | 465 | 2023-07-24 |
| 16 | [Threads, an Instagram App](https://news.ycombinator.com/item?id=36580192) | Instagram 推出社交应用 Threads。 | 1045 | 1258 | 2023-07-03 |
| 17 | [Transformer Attention is off by one](https://news.ycombinator.com/item?id=36851494) | 作者指出 Transformer 注意力机制中的一个差一问题。 | 1040 | 331 | 2023-07-24 |
| 18 | [Firefox Address Bar Tips](https://news.ycombinator.com/item?id=36666116) | 分享 Firefox 地址栏的使用技巧。 | 1028 | 317 | 2023-07-10 |
| 19 | [Tell HN: Nearly all of Evernote’s remaining staff has been laid off](https://news.ycombinator.com/item?id=36609641) | 用户称 Evernote 几乎全部剩余员工被裁，并质疑涨价后的开发承诺。 | 1025 | 614 | 2023-07-06 |
| 20 | [Ask HN: Could you share your personal blog here?](https://news.ycombinator.com/item?id=36575081) | 邀请 HN 用户分享自己的个人博客。 | 1014 | 1940 | 2023-07-03 |

## 2023-08

有效主帖 27,528 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Bram Moolenaar Passed Away](https://news.ycombinator.com/item?id=37011324) | Vim 创建者 Bram Moolenaar 去世。 | 4310 | 428 | 2023-08-05 |
| 2 | [Successful room temperature ambient-pressure magnetic levitation of LK-99](https://news.ycombinator.com/item?id=36994214) | 研究者宣称 LK-99 实现常温常压下的磁悬浮。 | 2408 | 1199 | 2023-08-04 |
| 3 | [LK-99 isn’t a superconductor – how science sleuths solved the mystery](https://news.ycombinator.com/item?id=37149349) | 介绍科学调查者如何判断 LK-99 并非超导体。 | 2145 | 698 | 2023-08-16 |
| 4 | [Live telecast of Chandrayaan-3 Soft-landing](https://news.ycombinator.com/item?id=37233936) | 观看月船三号软着陆的现场直播。 | 1942 | 491 | 2023-08-23 |
| 5 | [OpenTF Announces Fork of Terraform](https://news.ycombinator.com/item?id=37262440) | OpenTF 宣布分叉 Terraform。 | 1711 | 486 | 2023-08-25 |
| 6 | [Zoom terms now allow training AI on user content with no opt out](https://news.ycombinator.com/item?id=37021160) | Zoom 条款被指允许使用用户内容训练 AI 且无法退出。 | 1581 | 511 | 2023-08-06 |
| 7 | [The first conformant M1 GPU driver](https://news.ycombinator.com/item?id=37224042) | 首个符合标准的 M1 GPU 驱动发布。 | 1569 | 657 | 2023-08-22 |
| 8 | [ISPs Should Not Police Online Speech – No Matter How Awful It Is](https://news.ycombinator.com/item?id=37313349) | 作者主张即使言论恶劣，网络接入商也不应充当审查者。 | 1460 | 1256 | 2023-08-29 |
| 9 | [Factorio: Space Age](https://news.ycombinator.com/item?id=37260637) | 介绍《异星工厂：太空时代》。 | 1443 | 354 | 2023-08-25 |
| 10 | [Show HN: I'm 17 and wrote this guide on how CPUs run programs](https://news.ycombinator.com/item?id=37062422) | 一位十七岁作者撰写指南，解释 CPU 如何执行程序。 | 1337 | 307 | 2023-08-09 |
| 11 | [Downfall Attacks](https://news.ycombinator.com/item?id=37052586) | 介绍 Downfall 攻击方法。 | 1328 | 336 | 2023-08-08 |
| 12 | [Vim Boss](https://news.ycombinator.com/item?id=37078719) | 认识 Vim 背后的掌舵者与其角色。 | 1268 | 121 | 2023-08-10 |
| 13 | [Water](https://news.ycombinator.com/item?id=37026592) | 以水这一日常物质为主题，提供新的观察视角。 | 1231 | 133 | 2023-08-06 |
| 14 | [A Room-Temperature Superconductor? New Developments](https://news.ycombinator.com/item?id=36957678) | 追踪室温超导体宣称的后续发展。 | 1215 | 774 | 2023-08-01 |
| 15 | [Block YouTube Ads on AppleTV by Decrypting and Stripping Ads from Profobuf](https://news.ycombinator.com/item?id=37279109) | 通过解密并修改 Protobuf 数据屏蔽 Apple TV 上的 YouTube 广告。 | 1198 | 626 | 2023-08-27 |
| 16 | [Many temptations of an open-source Chrome extension developer](https://news.ycombinator.com/item?id=37066680) | 一位开源 Chrome 扩展开发者面对的种种诱惑。 | 1123 | 360 | 2023-08-09 |
| 17 | [Htmx is part of the GitHub Accelerator](https://news.ycombinator.com/item?id=37144985) | htmx 加入 GitHub Accelerator 计划。 | 1109 | 487 | 2023-08-16 |
| 18 | [A list of recent hostile moves by Google's Chrome team](https://news.ycombinator.com/item?id=36982507) | 整理谷歌 Chrome 团队近期被认为不友善的举措。 | 1074 | 585 | 2023-08-03 |
| 19 | [Google’s Plan to DRM the Web Goes Against Everything Google Once Stood For](https://news.ycombinator.com/item?id=36981953) | 作者认为谷歌为网页引入 DRM 的计划背离其昔日立场。 | 1068 | 416 | 2023-08-03 |
| 20 | [(Next Rich)](https://news.ycombinator.com/item?id=37000562) | 介绍题为《Next Rich》的内容。 | 1061 | 150 | 2023-08-04 |

## 2023-09

有效主帖 26,657 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: I’m an FCC Commissioner proposing regulation of IoT security updates](https://news.ycombinator.com/item?id=37392676) | FCC 委员征询社区意见，讨论如何监管物联网设备安全更新。 | 3387 | 925 | 2023-09-05 |
| 2 | [WiFi without internet on a Southwest flight](https://news.ycombinator.com/item?id=37691232) | 在西南航空航班上连接没有互联网的 Wi-Fi 的经历。 | 1756 | 652 | 2023-09-28 |
| 3 | [Unlimited Kagi searches for $10 per month](https://news.ycombinator.com/item?id=37603905) | Kagi 推出每月十美元的无限搜索方案。 | 1748 | 942 | 2023-09-21 |
| 4 | [Raspberry Pi 5](https://news.ycombinator.com/item?id=37685580) | 树莓派发布 Raspberry Pi 5。 | 1674 | 1022 | 2023-09-28 |
| 5 | [Car allergic to vanilla ice cream](https://news.ycombinator.com/item?id=37584399) | 回顾一辆似乎对香草冰淇淋过敏的汽车故障。 | 1667 | 506 | 2023-09-20 |
| 6 | [Tyranny of the Marginal User: why software gets worse, not better, over time](https://news.ycombinator.com/item?id=37509507) | 作者解释迎合边缘用户如何让软件随时间变差。 | 1576 | 815 | 2023-09-14 |
| 7 | [The Worst Programmer](https://news.ycombinator.com/item?id=37361947) | 以“最差程序员”为题反思开发者能力。 | 1545 | 628 | 2023-09-02 |
| 8 | [NSO Group iPhone Zero-Click, Zero-Day Exploit Captured in the Wild](https://news.ycombinator.com/item?id=37425007) | 研究者在实际攻击中捕获 NSO 的 iPhone 零点击零日漏洞。 | 1446 | 832 | 2023-09-07 |
| 9 | [Organic Maps](https://news.ycombinator.com/item?id=37347447) | 介绍地图项目 Organic Maps。 | 1401 | 485 | 2023-09-01 |
| 10 | [Is this duplo train track under too much tension?](https://news.ycombinator.com/item?id=37404740) | 探究一段得宝玩具火车轨道是否承受过大张力。 | 1392 | 237 | 2023-09-06 |
| 11 | [Richard Stallman reveals he has cancer in the GNU 40 Hacker Meeting talk](https://news.ycombinator.com/item?id=37699851) | Richard Stallman 在 GNU 四十周年演讲中透露患癌。 | 1366 | 788 | 2023-09-29 |
| 12 | [Text editing on mobile isn’t ok](https://news.ycombinator.com/item?id=37630804) | 作者批评手机上的文字编辑体验。 | 1276 | 681 | 2023-09-24 |
| 13 | [Snowden leak: Cavium networking hardware may contain NSA backdoor](https://news.ycombinator.com/item?id=37570407) | 斯诺登文件显示 Cavium 网络硬件可能含 NSA 后门。 | 1205 | 591 | 2023-09-19 |
| 14 | [Can’t send email more than 500 miles (2002)](https://news.ycombinator.com/item?id=37576633) | 回顾无法向五百英里外发送邮件的经典故障。 | 1164 | 198 | 2023-09-19 |
| 15 | [ChatGPT can now see, hear, and speak – openai.com](https://news.ycombinator.com/item?id=37642335) | ChatGPT 新增看图、听声音和语音对话能力。 | 1149 | 877 | 2023-09-25 |
| 16 | [FTC Sues Amazon for Illegally Maintaining Monopoly Power](https://news.ycombinator.com/item?id=37661446) | 美国 FTC 起诉亚马逊非法维持垄断地位。 | 1139 | 899 | 2023-09-26 |
| 17 | [Bun v1.0.0](https://news.ycombinator.com/item?id=37434117) | Bun 发布 1.0.0 版本。 | 1089 | 367 | 2023-09-08 |
| 18 | [Red Blob Games: Interactive visual explanations of math and algorithms](https://news.ycombinator.com/item?id=37703291) | Red Blob Games 用交互可视化解释数学与算法。 | 1059 | 141 | 2023-09-29 |
| 19 | [The Mystery of the Bloomfield Bridge](https://news.ycombinator.com/item?id=37359193) | 探究 Bloomfield 大桥的谜团。 | 1028 | 264 | 2023-09-02 |
| 20 | [Why my favourite API is a zipfile on the European Central Bank's website](https://news.ycombinator.com/item?id=37526047) | 作者解释为何欧洲央行网站的压缩文件是自己最喜欢的 API。 | 1024 | 265 | 2023-09-15 |

## 2023-10

有效主帖 26,770 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Oxide: The Cloud Computer](https://news.ycombinator.com/item?id=38023891) | Oxide 介绍云计算机产品。 | 1880 | 956 | 2023-10-26 |
| 2 | [German court declares Do Not Track to be legally binding](https://news.ycombinator.com/item?id=38081633) | 德国法院认定“不追踪”请求具有法律约束力。 | 1216 | 575 | 2023-10-31 |
| 3 | [California suspends GM Cruise's autonomous vehicle deployment](https://news.ycombinator.com/item?id=38002752) | 加州暂停通用汽车 Cruise 的自动驾驶部署许可。 | 1191 | 1241 | 2023-10-24 |
| 4 | [Log is the "Pro" in iPhone 15 Pro](https://news.ycombinator.com/item?id=37840503) | 作者解释 Log 视频为何体现 iPhone 15 Pro 的专业价值。 | 1163 | 409 | 2023-10-11 |
| 5 | [Making Hard Things Easy](https://news.ycombinator.com/item?id=37791002) | 探讨如何把困难的事情变得容易。 | 1134 | 197 | 2023-10-06 |
| 6 | [First word discovered in unopened Herculaneum scroll by 21yo CS student](https://news.ycombinator.com/item?id=37857417) | 一名二十一岁计算机学生识别出未展开赫库兰尼姆卷轴中的首个词。 | 1122 | 207 | 2023-10-12 |
| 7 | [I Accidentally Saved My Company Half a Million Dollars](https://news.ycombinator.com/item?id=38069710) | 作者分享意外为公司节省五十万美元的经历。 | 1076 | 458 | 2023-10-30 |
| 8 | [Apple unveils M3, M3 Pro, and M3 Max, the most advanced chips for a PC](https://news.ycombinator.com/item?id=38078063) | 苹果发布 M3、M3 Pro 与 M3 Max 芯片。 | 1035 | 1126 | 2023-10-31 |
| 9 | [Protomaps – A free and open source map of the world](https://news.ycombinator.com/item?id=37982621) | Protomaps 提供免费开源的世界地图。 | 1001 | 163 | 2023-10-23 |
| 10 | [The Absolute Minimum Every Software Developer Must Know About Unicode in 2023](https://news.ycombinator.com/item?id=37735801) | 整理 2023 年开发者至少应掌握的 Unicode 知识。 | 989 | 555 | 2023-10-02 |
| 11 | [Firefox tooltip bug fixed after 22 years](https://news.ycombinator.com/item?id=37827995) | Firefox 一个工具提示缺陷在二十二年后得到修复。 | 966 | 337 | 2023-10-10 |
| 12 | [Scrollbars Are Becoming a Problem](https://news.ycombinator.com/item?id=37864867) | 作者分析滚动条逐渐带来的可用性问题。 | 953 | 919 | 2023-10-13 |
| 13 | [Return to Office Is Bullshit and Everyone Knows It](https://news.ycombinator.com/item?id=37739376) | 作者强烈批评强制返回办公室的政策。 | 926 | 885 | 2023-10-02 |
| 14 | [John Riccitiello steps down as CEO of Unity after pricing battle](https://news.ycombinator.com/item?id=37825292) | Unity 定价争议后，John Riccitiello 辞去 CEO 职务。 | 926 | 435 | 2023-10-09 |
| 15 | [An Interactive Intro to CRDTs](https://news.ycombinator.com/item?id=37764581) | 用交互方式介绍无冲突复制数据类型 CRDT。 | 922 | 130 | 2023-10-04 |
| 16 | [A Dutch graphic artist reconstructed Tenochtitlan in 3D](https://news.ycombinator.com/item?id=37973229) | 荷兰平面艺术家用三维技术重建特诺奇蒂特兰。 | 919 | 100 | 2023-10-22 |
| 17 | [IRS will officially launch free online tax filing service for 2024 tax season](https://news.ycombinator.com/item?id=37920633) | 美国国税局将为 2024 报税季推出免费在线申报服务。 | 906 | 329 | 2023-10-17 |
| 18 | [Show HN: Phind Model beats GPT-4 at coding, with GPT-3.5 speed and 16k context](https://news.ycombinator.com/item?id=38088538) | Phind 称新模型在编程能力上媲美或超越 GPT-4，且速度更快。 | 891 | 347 | 2023-10-31 |
| 19 | [Where does my computer get the time from?](https://news.ycombinator.com/item?id=37778496) | 追问电脑所显示的时间究竟来自哪里。 | 851 | 250 | 2023-10-05 |
| 20 | [Write More "Useless" Software](https://news.ycombinator.com/item?id=37911900) | 作者鼓励多写看似没有实用价值的软件。 | 846 | 254 | 2023-10-17 |

## 2023-11

有效主帖 25,779 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [OpenAI Announces Leadership Transition](https://news.ycombinator.com/item?id=38309611) | OpenAI 宣布领导层变动。 | 5710 | 2530 | 2023-11-17 |
| 2 | [Omegle founder shuts down site forever?](https://news.ycombinator.com/item?id=38199355) | Omegle 创始人宣布网站永久关闭，引发关注。 | 2454 | 998 | 2023-11-09 |
| 3 | [Reflecting on 18 Years at Google](https://news.ycombinator.com/item?id=38381573) | 作者回顾在谷歌工作的十八年。 | 2213 | 1039 | 2023-11-22 |
| 4 | [Sam Bankman-Fried found guilty on all charges](https://news.ycombinator.com/item?id=38122061) | Sam Bankman-Fried 被判所有指控罪名成立。 | 1993 | 1735 | 2023-11-02 |
| 5 | [We have reached an agreement in principle for Sam to return to OpenAI](https://news.ycombinator.com/item?id=38375239) | OpenAI 宣布原则上同意 Sam Altman 回归。 | 1980 | 1950 | 2023-11-22 |
| 6 | [YouTube artificially slows down video load times when using Firefox](https://news.ycombinator.com/item?id=38345858) | YouTube 被指人为延长 Firefox 用户的视频加载时间。 | 1919 | 461 | 2023-11-20 |
| 7 | [Sam Altman, Greg Brockman and others to join Microsoft](https://news.ycombinator.com/item?id=38344196) | 微软宣布 Sam Altman、Greg Brockman 等人将加入公司。 | 1738 | 1311 | 2023-11-20 |
| 8 | [Blender 16yo winner of UK younganimator of the year](https://news.ycombinator.com/item?id=38282166) | 一位使用 Blender 的十六岁创作者获得英国年度青年动画师奖。 | 1603 | 254 | 2023-11-15 |
| 9 | [Charlie Munger has died](https://news.ycombinator.com/item?id=38451278) | 投资家 Charlie Munger 去世。 | 1479 | 405 | 2023-11-28 |
| 10 | [OpenAI staff threaten to quit unless board resigns](https://news.ycombinator.com/item?id=38347868) | OpenAI 员工威胁辞职，要求董事会下台。 | 1441 | 1260 | 2023-11-20 |
| 11 | [Greg Brockman quits OpenAI](https://news.ycombinator.com/item?id=38312704) | Greg Brockman 宣布离开 OpenAI。 | 1423 | 662 | 2023-11-18 |
| 12 | [Why does the moon change size when you snipe it in GTA?](https://news.ycombinator.com/item?id=38371361) | 解释 GTA 中射击月亮为何会让它改变大小。 | 1349 | 159 | 2023-11-21 |
| 13 | [Stable Video Diffusion](https://news.ycombinator.com/item?id=38368287) | 介绍视频生成模型 Stable Video Diffusion。 | 1330 | 302 | 2023-11-21 |
| 14 | [My Toddler Loves Planes, So I Built Her a Radar](https://news.ycombinator.com/item?id=38435908) | 父亲为喜欢飞机的幼女制作雷达。 | 1304 | 245 | 2023-11-27 |
| 15 | [Why Simone Giertz spent 3 years working on a coat hanger [video]](https://news.ycombinator.com/item?id=38292915) | Simone Giertz 解释为何花三年开发衣架。 | 1268 | 428 | 2023-11-16 |
| 16 | [OpenAI board in discussions with Sam Altman to return as CEO](https://news.ycombinator.com/item?id=38325552) | OpenAI 董事会讨论让 Sam Altman 重返 CEO 职位。 | 1243 | 1611 | 2023-11-18 |
| 17 | [My "retirement" project: Release 40 years worth of my "source code"](https://news.ycombinator.com/item?id=38132016) | 作者以退休项目的形式公开四十年积累的源代码。 | 1227 | 323 | 2023-11-03 |
| 18 | [Cosmopolitan Third Edition](https://news.ycombinator.com/item?id=38101613) | Cosmopolitan 发布第三版。 | 1205 | 240 | 2023-11-01 |
| 19 | [Home Assistant blocked from integrating with Garage Door opener API](https://news.ycombinator.com/item?id=38188162) | Home Assistant 被禁止接入车库门控制 API。 | 1181 | 640 | 2023-11-08 |
| 20 | [New models and developer products announced at OpenAI DevDay](https://news.ycombinator.com/item?id=38166420) | OpenAI 开发者大会公布新模型及开发产品。 | 1146 | 545 | 2023-11-06 |

## 2023-12

有效主帖 24,870 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Figma and Adobe are abandoning our proposed merger](https://news.ycombinator.com/item?id=38681861) | Figma 与 Adobe 宣布放弃合并计划。 | 2202 | 963 | 2023-12-18 |
| 2 | [Gemini – Google DeepMind](https://news.ycombinator.com/item?id=38544729) | Google DeepMind 介绍 Gemini 模型。 | 2135 | 1602 | 2023-12-06 |
| 3 | [In 2024, please switch to Firefox](https://news.ycombinator.com/item?id=38806270) | 作者呼吁读者在 2024 年转用 Firefox。 | 1776 | 810 | 2023-12-29 |
| 4 | [If buying isn't owning, piracy isn't stealing](https://news.ycombinator.com/item?id=38579899) | 作者以购买不等于拥有为由质疑将盗版视为偷窃。 | 1597 | 794 | 2023-12-09 |
| 5 | [LLM Visualization](https://news.ycombinator.com/item?id=38505211) | 用可视化方式理解大型语言模型。 | 1592 | 131 | 2023-12-03 |
| 6 | [Tiny Volumetric Display](https://news.ycombinator.com/item?id=38498109) | 展示一台微型体积显示器。 | 1570 | 174 | 2023-12-02 |
| 7 | [Show HN: Beeper Mini – iMessage Client for Android](https://news.ycombinator.com/item?id=38531759) | Beeper Mini 通过逆向协议让 Android 直接连接 iMessage，无需 Mac 中继。 | 1521 | 874 | 2023-12-05 |
| 8 | [4B If Statements](https://news.ycombinator.com/item?id=38790597) | 探索四十亿条条件判断语句所带来的规模问题。 | 1518 | 469 | 2023-12-28 |
| 9 | [Happy New Year HN!](https://news.ycombinator.com/item?id=38826283) | HN 用户祝社区成员在 2024 年新年快乐。 | 1393 | 265 | 2023-12-31 |
| 10 | [Apple cuts off Beeper Mini's access](https://news.ycombinator.com/item?id=38574888) | 苹果切断 Beeper Mini 对 iMessage 的访问。 | 1365 | 1222 | 2023-12-08 |
| 11 | [Epic vs. Google: Google Loses](https://news.ycombinator.com/item?id=38607424) | Epic 对谷歌的诉讼中，谷歌败诉。 | 1289 | 1056 | 2023-12-12 |
| 12 | [Voyager 1 stops communicating with Earth](https://news.ycombinator.com/item?id=38640900) | 旅行者一号停止与地球正常通信。 | 1273 | 608 | 2023-12-14 |
| 13 | [DeskHop – Fast Desktop Switching](https://news.ycombinator.com/item?id=38780519) | DeskHop 提供快速桌面切换功能。 | 1248 | 273 | 2023-12-27 |
| 14 | [ArXiv now offers papers in HTML format](https://news.ycombinator.com/item?id=38724665) | arXiv 开始提供 HTML 格式论文。 | 1204 | 312 | 2023-12-21 |
| 15 | [Harvard gutted team examining Facebook Files following $500M Zuckerberg donation](https://news.ycombinator.com/item?id=38519012) | 报道称哈佛在 Zuckerberg 捐赠五亿美元后削减调查 Facebook 文件的团队。 | 1202 | 15 | 2023-12-04 |
| 16 | [Polish trains lock up when serviced in third-party workshops](https://news.ycombinator.com/item?id=38530885) | 波兰列车被发现经第三方维修后会锁死。 | 1076 | 360 | 2023-12-05 |
| 17 | [Beeper Mini is back](https://news.ycombinator.com/item?id=38602575) | Beeper Mini 恢复服务。 | 1064 | 1239 | 2023-12-11 |
| 18 | [Show HN: Heynote – A dedicated scratchpad for developers](https://news.ycombinator.com/item?id=38733968) | Heynote 为开发者提供可以分块记录内容的专用草稿本。 | 1063 | 303 | 2023-12-22 |
| 19 | [Gemini "duck" demo was not done in realtime or with voice](https://news.ycombinator.com/item?id=38559582) | Gemini 的鸭子演示并非实时进行，也未采用语音交互。 | 1039 | 658 | 2023-12-07 |
| 20 | [First new U.S. nuclear reactor since 2016 is now in operation](https://news.ycombinator.com/item?id=38785468) | 美国自 2016 年以来首座新核反应堆投入运行。 | 1012 | 1123 | 2023-12-27 |

## 2024-01

有效主帖 28,809 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Losing my son](https://news.ycombinator.com/item?id=39036842) | 作者讲述失去儿子的悲痛经历。 | 2437 | 395 | 2024-01-18 |
| 2 | [Apple announces changes to iOS, Safari, and the App Store in the European Union](https://news.ycombinator.com/item?id=39132453) | 苹果宣布调整欧盟地区的 iOS、Safari 与 App Store。 | 2108 | 2485 | 2024-01-25 |
| 3 | [In loving memory of square checkbox](https://news.ycombinator.com/item?id=39161339) | 作者怀念方形复选框的界面传统。 | 1967 | 505 | 2024-01-28 |
| 4 | [Niklaus Wirth has died](https://news.ycombinator.com/item?id=38858012) | 计算机科学家 Niklaus Wirth 去世。 | 1902 | 403 | 2024-01-03 |
| 5 | [What's that touchscreen in my room?](https://news.ycombinator.com/item?id=39063242) | 作者探究房间里一块触摸屏的用途。 | 1890 | 560 | 2024-01-20 |
| 6 | [1D Pac-Man](https://news.ycombinator.com/item?id=38845510) | 展示一维版本的吃豆人游戏。 | 1790 | 230 | 2024-01-02 |
| 7 | [Zed, a collaborative code editor, is now open source](https://news.ycombinator.com/item?id=39119835) | 协作代码编辑器 Zed 宣布开源。 | 1576 | 601 | 2024-01-24 |
| 8 | [I'm sorry but I cannot fulfill this request it goes against OpenAI use policy](https://news.ycombinator.com/item?id=38971012) | 模型以违反 OpenAI 使用政策为由拒绝请求，这种措辞成为关注对象。 | 1325 | 736 | 2024-01-12 |
| 9 | [Which word begins with "y" and looks like an axe in this picture? (2017)](https://news.ycombinator.com/item?id=39034160) | 一道图像文字谜题要求找出以字母 y 开头、形似斧头的词。 | 1220 | 289 | 2024-01-17 |
| 10 | [Infinite Craft](https://news.ycombinator.com/item?id=39205020) | 介绍组合创造游戏 Infinite Craft。 | 1177 | 675 | 2024-01-31 |
| 11 | [Python 3.13 Gets a JIT](https://news.ycombinator.com/item?id=38923741) | Python 3.13 加入即时编译器。 | 1081 | 521 | 2024-01-09 |
| 12 | [I pwned half of America's fast food chains simultaneously](https://news.ycombinator.com/item?id=38933999) | 研究者讲述同时攻破美国多家快餐连锁系统的经历。 | 1081 | 474 | 2024-01-09 |
| 13 | [An app can be a home-cooked meal (2020)](https://news.ycombinator.com/item?id=38877423) | 作者将为自己制作应用比作在家做饭。 | 1051 | 288 | 2024-01-05 |
| 14 | [Fixing Macs door to door](https://news.ycombinator.com/item?id=38886030) | 分享上门维修 Mac 电脑的经历。 | 1033 | 203 | 2024-01-05 |
| 15 | [Unity's Open-Source Double Standard: The Ban of VLC](https://news.ycombinator.com/item?id=38964972) | 作者以 VLC 被禁为例质疑 Unity 对开源的双重标准。 | 1027 | 357 | 2024-01-12 |
| 16 | [Polars](https://news.ycombinator.com/item?id=38920043) | 介绍数据处理工具 Polars。 | 981 | 386 | 2024-01-08 |
| 17 | [Show HN: I made a website to find best bus seat to avoid the sun while traveling](https://news.ycombinator.com/item?id=39022693) | 一个根据太阳方向帮助旅客选择巴士座位的网站。 | 963 | 210 | 2024-01-17 |
| 18 | [Clicks – Physical keyboard for iPhone](https://news.ycombinator.com/item?id=38871987) | Clicks 为 iPhone 提供实体键盘配件。 | 953 | 542 | 2024-01-04 |
| 19 | [US developers can offer non-app store purchasing, Apple still collect commission](https://news.ycombinator.com/item?id=39020365) | 美国开发者可提供非商店购买渠道，但苹果仍将收取佣金。 | 911 | 1300 | 2024-01-16 |
| 20 | [FTC bans TurboTax from advertising 'free' services, calls deceptive advertising](https://news.ycombinator.com/item?id=39097356) | 美国 FTC 禁止 TurboTax 以误导性方式宣传免费服务。 | 879 | 253 | 2024-01-23 |

## 2024-02

有效主帖 26,599 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Sora: Creating video from text](https://news.ycombinator.com/item?id=39386156) | OpenAI 展示由文字生成视频的 Sora。 | 3647 | 2231 | 2024-02-15 |
| 2 | [Airfoil](https://news.ycombinator.com/item?id=39526057) | 以机翼剖面为主题，探索这一空气动力学结构。 | 2544 | 296 | 2024-02-27 |
| 3 | [I designed a cube that balances itself on a corner](https://news.ycombinator.com/item?id=39336139) | 作者设计出能以一个角保持平衡的立方体。 | 2460 | 377 | 2024-02-11 |
| 4 | [Netlify just sent me a $104k bill for a simple static site](https://news.ycombinator.com/item?id=39520776) | 作者称简单静态网站收到 Netlify 十万四千美元账单。 | 1783 | 798 | 2024-02-27 |
| 5 | [Thanks FedEx, this is why we keep getting phished](https://news.ycombinator.com/item?id=39479001) | 作者借 FedEx 的行为解释用户为何容易遭遇钓鱼攻击。 | 1723 | 564 | 2024-02-23 |
| 6 | [European Court of Human Rights bans weakening of secure end-to-end encryption](https://news.ycombinator.com/item?id=39369653) | 欧洲人权法院禁止削弱安全的端到端加密。 | 1673 | 258 | 2024-02-14 |
| 7 | [Alexei Navalny has died](https://news.ycombinator.com/item?id=39395631) | 俄罗斯反对派人士 Alexei Navalny 去世。 | 1641 | 1541 | 2024-02-16 |
| 8 | [Institutions try to preserve the problem to which they are the solution](https://news.ycombinator.com/item?id=39491863) | 作者认为机构可能倾向于保留自身试图解决的问题。 | 1620 | 1125 | 2024-02-24 |
| 9 | [Insecure vehicles should be banned, not security tools like the Flipper Zero](https://news.ycombinator.com/item?id=39452494) | 作者主张应限制不安全车辆，而非 Flipper Zero 等安全工具。 | 1496 | 878 | 2024-02-21 |
| 10 | [Keep your phone number private with Signal usernames](https://news.ycombinator.com/item?id=39444500) | Signal 用户名功能帮助用户隐藏电话号码。 | 1422 | 872 | 2024-02-20 |
| 11 | [Vesuvius Challenge 2023 Grand Prize awarded: we can read the first scroll](https://news.ycombinator.com/item?id=39261861) | 维苏威挑战赛颁出大奖，研究者已能阅读首卷古卷内容。 | 1374 | 215 | 2024-02-05 |
| 12 | [Our next-generation model: Gemini 1.5](https://news.ycombinator.com/item?id=39383446) | 谷歌介绍新一代模型 Gemini 1.5。 | 1244 | 588 | 2024-02-15 |
| 13 | [Almost every infrastructure decision I endorse or regret](https://news.ycombinator.com/item?id=39313623) | 作者回顾自己赞同或后悔的基础设施决策。 | 1181 | 626 | 2024-02-09 |
| 14 | [Is something bugging you?](https://news.ycombinator.com/item?id=39356920) | 以“有什么问题困扰你”为提问，邀请读者重新观察眼前的问题。 | 1179 | 418 | 2024-02-13 |
| 15 | [FCC rules AI-generated voices in robocalls illegal](https://news.ycombinator.com/item?id=39304736) | 美国 FCC 裁定自动骚扰电话使用 AI 生成声音违法。 | 1156 | 674 | 2024-02-08 |
| 16 | [The killer app of Gemini Pro 1.5 is using video as an input](https://news.ycombinator.com/item?id=39458264) | 作者认为 Gemini Pro 1.5 最有价值的用途是视频输入。 | 1136 | 482 | 2024-02-21 |
| 17 | [Freenginx: Core Nginx developer announces fork](https://news.ycombinator.com/item?id=39373327) | Nginx 核心开发者宣布分叉项目 Freenginx。 | 1131 | 475 | 2024-02-14 |
| 18 | [Gemma: New Open Models](https://news.ycombinator.com/item?id=39453271) | 谷歌发布开放模型 Gemma。 | 1129 | 509 | 2024-02-21 |
| 19 | [GPT in 500 Lines of SQL](https://news.ycombinator.com/item?id=39488668) | 用五百行 SQL 实现 GPT。 | 1111 | 76 | 2024-02-24 |
| 20 | [Relativistic Spaceship](https://news.ycombinator.com/item?id=39266396) | 介绍相对论条件下的宇宙飞船。 | 1085 | 485 | 2024-02-05 |

## 2024-03

有效主帖 26,310 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Backdoor in upstream xz/liblzma leading to SSH server compromise](https://news.ycombinator.com/item?id=39865810) | xz 与 liblzma 上游被植入可能导致 SSH 服务器失陷的后门。 | 4549 | 1849 | 2024-03-29 |
| 2 | [U.S. sues Apple, accusing it of maintaining an iPhone monopoly](https://news.ycombinator.com/item?id=39778999) | 美国起诉苹果，指控其维持 iPhone 垄断地位。 | 2546 | 2569 | 2024-03-21 |
| 3 | [Bruno: Fast and Git-friendly open-source API client (Postman alternative)](https://news.ycombinator.com/item?id=39653718) | Bruno 提供快速、适合 Git 管理的开源 API 客户端。 | 1538 | 400 | 2024-03-09 |
| 4 | [Game of Life, simulating itself, infinitely zoomable](https://news.ycombinator.com/item?id=39799755) | 一个可无限缩放、内部模拟自身的生命游戏。 | 1515 | 243 | 2024-03-23 |
| 5 | [Spreadsheets are all you need](https://news.ycombinator.com/item?id=39700256) | 作者探讨仅使用电子表格能够完成的事情。 | 1493 | 164 | 2024-03-14 |
| 6 | [Elon Musk sues Sam Altman, Greg Brockman, and OpenAI [pdf]](https://news.ycombinator.com/item?id=39559966) | 马斯克起诉 Sam Altman、Greg Brockman 与 OpenAI。 | 1462 | 1208 | 2024-03-01 |
| 7 | [Boeing whistleblower found dead in US](https://news.ycombinator.com/item?id=39673589) | 波音举报者在美国被发现死亡。 | 1335 | 556 | 2024-03-11 |
| 8 | [XZ backdoor: "It's RCE, not auth bypass, and gated/unreplayable."](https://news.ycombinator.com/item?id=39877267) | 研究者澄清 XZ 后门支持远程代码执行，且设有触发门槛。 | 1323 | 810 | 2024-03-30 |
| 9 | [Show HN: 3 years and 1M users later, I just open-sourced my "Internet OS"](https://news.ycombinator.com/item?id=39597030) | 开发者在三年积累百万用户后开源自己的“互联网操作系统”。 | 1274 | 319 | 2024-03-04 |
| 10 | [Eloquent JavaScript 4th edition (2024)](https://news.ycombinator.com/item?id=39629044) | 《JavaScript 编程精解》推出第四版。 | 1274 | 231 | 2024-03-07 |
| 11 | [Sam Bankman-Fried sentenced to 25 years in prison](https://news.ycombinator.com/item?id=39852953) | Sam Bankman-Fried 被判二十五年监禁。 | 1268 | 1431 | 2024-03-28 |
| 12 | [Difftastic, a structural diff tool that understands syntax](https://news.ycombinator.com/item?id=39778412) | Difftastic 根据语法结构比较代码差异。 | 1188 | 200 | 2024-03-21 |
| 13 | [Grok](https://news.ycombinator.com/item?id=39737281) | 介绍 Grok 模型。 | 1170 | 419 | 2024-03-17 |
| 14 | [Vernor Vinge has died](https://news.ycombinator.com/item?id=39775304) | 科幻作家 Vernor Vinge 去世。 | 1151 | 320 | 2024-03-21 |
| 15 | [Akira Toriyama has died](https://news.ycombinator.com/item?id=39637471) | 漫画家鸟山明去世。 | 1065 | 207 | 2024-03-08 |
| 16 | [OpenAI and Elon Musk](https://news.ycombinator.com/item?id=39611484) | 介绍 OpenAI 与马斯克之间的关系及争议。 | 1037 | 977 | 2024-03-06 |
| 17 | [European crash tester says carmakers must bring back physical controls](https://news.ycombinator.com/item?id=39598189) | 欧洲碰撞测试机构要求汽车厂商恢复实体控制装置。 | 1025 | 638 | 2024-03-05 |
| 18 | [Claude 3 model family](https://news.ycombinator.com/item?id=39590666) | Anthropic 发布 Claude 3 模型家族。 | 1016 | 683 | 2024-03-04 |
| 19 | [Daniel Kahneman has died](https://news.ycombinator.com/item?id=39840286) | 心理学家 Daniel Kahneman 去世。 | 1002 | 309 | 2024-03-27 |
| 20 | [Monodraw](https://news.ycombinator.com/item?id=39651796) | 介绍 Monodraw 工具。 | 996 | 200 | 2024-03-09 |

## 2024-04

有效主帖 25,367 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Meta Llama 3](https://news.ycombinator.com/item?id=40077533) | Meta 发布 Llama 3 模型。 | 2199 | 923 | 2024-04-18 |
| 2 | [The man who killed Google Search?](https://news.ycombinator.com/item?id=40133976) | 作者追问是谁让谷歌搜索走向衰落。 | 1884 | 878 | 2024-04-23 |
| 3 | [Equinox.space](https://news.ycombinator.com/item?id=40113013) | 介绍 Equinox.space 网站。 | 1639 | 326 | 2024-04-22 |
| 4 | [Mario meets Pareto](https://news.ycombinator.com/item?id=39936246) | 将马里奥与帕累托思想联系起来展开探索。 | 1583 | 177 | 2024-04-04 |
| 5 | [Leaving Rust gamedev after 3 years](https://news.ycombinator.com/item?id=40172033) | 开发者在使用 Rust 开发游戏三年后选择离开。 | 1484 | 972 | 2024-04-26 |
| 6 | [This is a teenager](https://news.ycombinator.com/item?id=40053774) | 把目光投向一位青少年，重新理解这一人生阶段。 | 1445 | 809 | 2024-04-16 |
| 7 | [Hardest problem in computer science: centering things](https://news.ycombinator.com/item?id=40069599) | 借元素居中调侃计算机科学中的难题。 | 1419 | 455 | 2024-04-17 |
| 8 | ['Lavender': The AI machine directing Israel's bombing in Gaza](https://news.ycombinator.com/item?id=39918245) | 报道介绍被用于指引以色列轰炸加沙的 AI 系统 Lavender。 | 1418 | 1433 | 2024-04-03 |
| 9 | [Obituary for a quiet life (2023)](https://news.ycombinator.com/item?id=40028643) | 用讣告形式记录一段平静的人生。 | 1416 | 292 | 2024-04-14 |
| 10 | [LLaMA now goes faster on CPUs](https://news.ycombinator.com/item?id=39890262) | LLaMA 在 CPU 上的运行速度进一步提升。 | 1372 | 451 | 2024-04-01 |
| 11 | [Anatomy of a credit card rewards program](https://news.ycombinator.com/item?id=39928604) | 剖析信用卡奖励计划的运作机制。 | 1271 | 733 | 2024-04-04 |
| 12 | [Descent 3 Source Code](https://news.ycombinator.com/item?id=40048177) | 《Descent 3》获准公开源代码，发布者寻找共同维护者。 | 1255 | 324 | 2024-04-16 |
| 13 | [FTC announces rule banning noncompetes](https://news.ycombinator.com/item?id=40136010) | 美国 FTC 宣布禁止竞业限制协议的规则。 | 1169 | 500 | 2024-04-23 |
| 14 | [Yes, social media is a cause of the epidemic of teenage mental illness](https://news.ycombinator.com/item?id=39983233) | 作者主张社交媒体是青少年心理疾病增加的原因。 | 1164 | 1164 | 2024-04-09 |
| 15 | [The Wi-Fi only works when it's raining](https://news.ycombinator.com/item?id=39896371) | 排查只有下雨时 Wi-Fi 才能工作的奇特故障。 | 1147 | 324 | 2024-04-01 |
| 16 | [Google made me ruin a perfectly good website (2023)](https://news.ycombinator.com/item?id=40184673) | 作者讲述谷歌如何迫使自己改坏一个原本好用的网站。 | 1112 | 529 | 2024-04-27 |
| 17 | [Webb captures iconic Horsehead Nebula in unprecedented detail](https://news.ycombinator.com/item?id=40199624) | 韦布望远镜以空前细节拍摄标志性的马头星云。 | 1078 | 301 | 2024-04-29 |
| 18 | [Timeline of the xz open source attack](https://news.ycombinator.com/item?id=39902241) | 梳理针对 xz 开源项目的攻击时间线。 | 1069 | 459 | 2024-04-02 |
| 19 | [Tips for linking shell companies to their secret owners](https://news.ycombinator.com/item?id=39919401) | 分享追查空壳公司实际所有者的方法。 | 1068 | 496 | 2024-04-03 |
| 20 | [Llm.c – LLM training in simple, pure C/CUDA](https://news.ycombinator.com/item?id=39973467) | llm.c 用简洁的 C 与 CUDA 实现语言模型训练。 | 1050 | 168 | 2024-04-08 |

## 2024-05

有效主帖 26,028 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [GPT-4o](https://news.ycombinator.com/item?id=40345775) | OpenAI 发布 GPT-4o。 | 3138 | 2366 | 2024-05-13 |
| 2 | [Daylight Computer – New 60fps e-paper tablet](https://news.ycombinator.com/item?id=40456834) | Daylight 推出支持每秒六十帧的电子纸平板。 | 2230 | 858 | 2024-05-23 |
| 3 | [TTE: Terminal Text Effects](https://news.ycombinator.com/item?id=40503202) | TTE 为终端文字提供视觉效果。 | 1830 | 266 | 2024-05-28 |
| 4 | [Leaked OpenAI documents reveal aggressive tactics toward former employees](https://news.ycombinator.com/item?id=40447431) | 泄漏文件揭示 OpenAI 对离职员工采取的强硬措施。 | 1791 | 534 | 2024-05-22 |
| 5 | [Veo](https://news.ycombinator.com/item?id=40358041) | 介绍视频生成模型 Veo。 | 1727 | 488 | 2024-05-14 |
| 6 | [Most of Europe is glowing pink under the aurora](https://news.ycombinator.com/item?id=40324179) | 欧洲多地在极光下呈现粉色夜空。 | 1623 | 378 | 2024-05-10 |
| 7 | [Apple introduces M4 chip](https://news.ycombinator.com/item?id=40286029) | 苹果发布 M4 芯片。 | 1588 | 2061 | 2024-05-07 |
| 8 | [Statement from Scarlett Johansson on the OpenAI "Sky" voice](https://news.ycombinator.com/item?id=40421225) | Scarlett Johansson 就 OpenAI 的 Sky 声音发表声明。 | 1528 | 1000 | 2024-05-20 |
| 9 | [After 6 years, I'm over GraphQL](https://news.ycombinator.com/item?id=40521518) | 作者在使用 GraphQL 六年后说明不再热衷的原因。 | 1259 | 698 | 2024-05-30 |
| 10 | [Gordon Bell has died](https://news.ycombinator.com/item?id=40432688) | 计算机先驱 Gordon Bell 去世。 | 1257 | 70 | 2024-05-21 |
| 11 | [OpenAI departures: Why can’t former employees talk?](https://news.ycombinator.com/item?id=40393121) | 追问 OpenAI 离职员工为何难以公开发言。 | 1254 | 961 | 2024-05-17 |
| 12 | [Jim Simons has died](https://news.ycombinator.com/item?id=40320406) | 数学家与投资家 Jim Simons 去世。 | 1143 | 320 | 2024-05-10 |
| 13 | [Ilya Sutskever to leave OpenAI](https://news.ycombinator.com/item?id=40361128) | Ilya Sutskever 宣布离开 OpenAI。 | 1124 | 782 | 2024-05-14 |
| 14 | [GPUs Go Brrr](https://news.ycombinator.com/item?id=40337936) | 关注 GPU 如何高速运转以及相关性能问题。 | 1104 | 263 | 2024-05-12 |
| 15 | [AlphaFold 3 predicts the structure and interactions of life's molecules](https://news.ycombinator.com/item?id=40298927) | AlphaFold 3 预测生命分子的结构与相互作用。 | 1100 | 487 | 2024-05-08 |
| 16 | [ICQ will stop working from June 26](https://news.ycombinator.com/item?id=40467625) | 即时通信服务 ICQ 将于六月二十六日停止运行。 | 1085 | 746 | 2024-05-24 |
| 17 | [Cloudflare took down our website](https://news.ycombinator.com/item?id=40481808) | 作者称 Cloudflare 导致自己的网站下线。 | 1044 | 466 | 2024-05-26 |
| 18 | [Bend: a high-level language that runs on GPUs (via HVM2)](https://news.ycombinator.com/item?id=40390287) | Bend 借助 HVM2 让高级语言程序在 GPU 上运行。 | 1041 | 253 | 2024-05-17 |
| 19 | [Llama3 implemented from scratch](https://news.ycombinator.com/item?id=40408880) | 展示从零实现的 Llama 3。 | 1041 | 269 | 2024-05-19 |
| 20 | [I sold TinyPilot, my first successful business](https://news.ycombinator.com/item?id=40512500) | 作者分享出售首个成功业务 TinyPilot 的经历。 | 1016 | 316 | 2024-05-29 |

## 2024-06

有效主帖 23,840 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Julian Assange has reached a plea deal with the U.S., allowing him to go free](https://news.ycombinator.com/item?id=40782130) | Julian Assange 与美国达成认罪协议，得以恢复自由。 | 2676 | 1620 | 2024-06-24 |
| 2 | [FTC sues Adobe for hiding fees and inhibiting cancellations](https://news.ycombinator.com/item?id=40707558) | 美国 FTC 起诉 Adobe 隐藏费用并阻碍取消订阅。 | 2587 | 847 | 2024-06-17 |
| 3 | [Silicon Valley's best kept secret: Founder liquidity](https://news.ycombinator.com/item?id=40654190) | 揭示硅谷创业者提前兑现股权的现象。 | 1811 | 914 | 2024-06-12 |
| 4 | [Lynn Conway has died](https://news.ycombinator.com/item?id=40648470) | 计算机科学家 Lynn Conway 去世。 | 1667 | 328 | 2024-06-11 |
| 5 | [I am using AI to drop hats outside my window onto New Yorkers](https://news.ycombinator.com/item?id=40767459) | 作者用 AI 从窗外向纽约行人投放帽子。 | 1347 | 440 | 2024-06-23 |
| 6 | [Safe Superintelligence Inc.](https://news.ycombinator.com/item?id=40730156) | 介绍 Safe Superintelligence 公司。 | 1214 | 1068 | 2024-06-19 |
| 7 | [EU Council has withdrawn the vote on Chat Control](https://news.ycombinator.com/item?id=40736771) | 欧盟理事会撤回对 Chat Control 的投票。 | 1213 | 533 | 2024-06-20 |
| 8 | [I built an ROV to solve missing person cases](https://news.ycombinator.com/item?id=40623864) | 作者制造遥控水下机器人，协助寻找失踪人员。 | 1183 | 162 | 2024-06-09 |
| 9 | [Apple Intelligence for iPhone, iPad, and Mac](https://news.ycombinator.com/item?id=40636844) | 苹果为 iPhone、iPad 与 Mac 推出 Apple Intelligence。 | 1092 | 1237 | 2024-06-10 |
| 10 | [Show HN: I made a puzzle game that gently introduces my favorite math mysteries](https://news.ycombinator.com/item?id=40740021) | 开发者通过解谜游戏引导玩家对数学问题产生好奇。 | 1054 | 172 | 2024-06-20 |
| 11 | [Voyager 1 is back online: NASA spacecraft returns data from all 4 instruments](https://news.ycombinator.com/item?id=40687660) | 旅行者一号恢复在线，四台仪器均重新传回数据。 | 1044 | 226 | 2024-06-15 |
| 12 | [How many photons are received per bit transmitted from Voyager 1?](https://news.ycombinator.com/item?id=40561872) | 探究旅行者一号每传回一比特数据，地球能收到多少光子。 | 1027 | 195 | 2024-06-03 |
| 13 | [Ball: A ball that lives in your dock](https://news.ycombinator.com/item?id=40793465) | Ball 让一颗小球住进桌面程序坞。 | 1017 | 292 | 2024-06-25 |
| 14 | [One Million Checkboxes](https://news.ycombinator.com/item?id=40800869) | 介绍包含一百万个复选框的互动项目。 | 994 | 304 | 2024-06-26 |
| 15 | [Microfeatures I love in blogs and personal websites](https://news.ycombinator.com/item?id=40774277) | 作者分享喜爱的博客和个人网站微小功能。 | 983 | 421 | 2024-06-24 |
| 16 | [Please don't mention AI again](https://news.ycombinator.com/item?id=40725329) | 作者表达对反复提及 AI 的厌倦。 | 968 | 563 | 2024-06-19 |
| 17 | [Chat Control Must Be Stopped – Now](https://news.ycombinator.com/item?id=40715449) | 作者呼吁立即阻止 Chat Control。 | 960 | 320 | 2024-06-18 |
| 18 | [Apple's On-Device and Server Foundation Models](https://news.ycombinator.com/item?id=40639506) | 介绍苹果设备端与服务器端基础模型。 | 941 | 535 | 2024-06-10 |
| 19 | [The tiny chip that powers Montreal subway tickets](https://news.ycombinator.com/item?id=40769001) | 探究蒙特利尔地铁票内微小芯片的作用。 | 930 | 508 | 2024-06-23 |
| 20 | [KidPix](https://news.ycombinator.com/item?id=40723220) | 介绍绘图软件 Kid Pix。 | 921 | 124 | 2024-06-18 |

## 2024-07

有效主帖 23,438 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [CrowdStrike Update: Windows Bluescreen and Boot Loops](https://news.ycombinator.com/item?id=41002195) | 用户集中报告 Windows 蓝屏与循环启动，怀疑与 CrowdStrike 更新有关。 | 4489 | 3859 | 2024-07-19 |
| 2 | [Open source AI is the path forward](https://news.ycombinator.com/item?id=41046773) | 作者主张开源人工智能才是未来方向。 | 2360 | 887 | 2024-07-23 |
| 3 | [Reverse engineering Ticketmaster's rotating barcodes](https://news.ycombinator.com/item?id=40906148) | 逆向分析 Ticketmaster 不断变化的条码。 | 2305 | 714 | 2024-07-08 |
| 4 | [Anyone can access deleted and private repository data on GitHub](https://news.ycombinator.com/item?id=41060102) | 研究指出 GitHub 已删除或私密仓库数据仍可能被访问。 | 1983 | 374 | 2024-07-24 |
| 5 | [Panic at the Job Market](https://news.ycombinator.com/item?id=40986894) | 关注就业市场带来的恐慌。 | 1717 | 1562 | 2024-07-17 |
| 6 | [Why is Chile so long?](https://news.ycombinator.com/item?id=40856030) | 解释智利国土为何如此狭长。 | 1441 | 445 | 2024-07-02 |
| 7 | [My daughter (7 years old) used HTML to make a website](https://news.ycombinator.com/item?id=40992982) | 家长分享七岁女儿用 HTML 制作网站的成果。 | 1435 | 514 | 2024-07-18 |
| 8 | [AI solves International Math Olympiad problems at silver medal level](https://news.ycombinator.com/item?id=41069829) | AI 解答国际数学奥林匹克题目达到银牌水平。 | 1370 | 525 | 2024-07-25 |
| 9 | [Run CUDA, unmodified, on AMD GPUs](https://news.ycombinator.com/item?id=40970560) | 介绍无需修改 CUDA 程序便可在 AMD GPU 上运行的方法。 | 1330 | 399 | 2024-07-15 |
| 10 | [Node.js adds experimental support for TypeScript](https://news.ycombinator.com/item?id=41064351) | Node.js 加入实验性 TypeScript 支持。 | 1204 | 554 | 2024-07-25 |
| 11 | [We need visual programming. No, not like that](https://news.ycombinator.com/item?id=40937119) | 作者探讨需要何种形式的可视化编程。 | 1178 | 493 | 2024-07-11 |
| 12 | [Show HN: I created an After Effects alternative](https://news.ycombinator.com/item?id=40843867) | Pikimov 提供免费、免注册且文件留在本地的网页动效与视频编辑。 | 1150 | 258 | 2024-07-01 |
| 13 | [AT&T says criminals stole phone records of 'nearly all' customers in data breach](https://news.ycombinator.com/item?id=40944505) | AT&T 称几乎所有客户的通话记录在泄露事件中被窃。 | 1103 | 812 | 2024-07-12 |
| 14 | [Jailbreaking RabbitOS](https://news.ycombinator.com/item?id=40987730) | 介绍对 RabbitOS 进行越狱的过程。 | 1089 | 265 | 2024-07-17 |
| 15 | [Use a work journal](https://news.ycombinator.com/item?id=40950584) | 作者建议通过工作日志记录日常工作。 | 1083 | 293 | 2024-07-13 |
| 16 | [Ladybird Web Browser becomes a non-profit with $1M from GitHub Founder](https://news.ycombinator.com/item?id=40856791) | Ladybird 浏览器转为非营利项目，并获 GitHub 创始人百万美元资助。 | 1077 | 744 | 2024-07-02 |
| 17 | [Joe Biden stands down as Democratic candidate](https://news.ycombinator.com/item?id=41026741) | Joe Biden 退出民主党总统候选人竞选。 | 990 | 1801 | 2024-07-21 |
| 18 | [Every company should be owned by its employees](https://news.ycombinator.com/item?id=41065227) | 作者主张每家公司都应由员工拥有。 | 986 | 1054 | 2024-07-25 |
| 19 | [FCC votes to limit prison telecom charges](https://news.ycombinator.com/item?id=41005181) | 美国 FCC 投票限制监狱通信收费。 | 982 | 426 | 2024-07-19 |
| 20 | [TinyPod – Apple Watch case with scroll wheel](https://news.ycombinator.com/item?id=40987402) | TinyPod 用带滚轮的外壳将 Apple Watch 变成小设备。 | 934 | 343 | 2024-07-17 |

## 2024-08

有效主帖 24,255 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [AnandTech Farewell](https://news.ycombinator.com/item?id=41399872) | AnandTech 宣布告别读者。 | 3025 | 598 | 2024-08-30 |
| 2 | [Show HN: If YouTube had actual channels](https://news.ycombinator.com/item?id=41247023) | 开发者设想让 YouTube 拥有真正电视式频道的体验。 | 2741 | 514 | 2024-08-14 |
| 3 | [The secret inside One Million Checkboxes](https://news.ycombinator.com/item?id=41395413) | 揭示“一百万个复选框”项目中的秘密。 | 2365 | 218 | 2024-08-29 |
| 4 | [Bypassing airport security via SQL injection](https://news.ycombinator.com/item?id=41392128) | 研究者通过 SQL 注入绕过机场安全措施。 | 2004 | 440 | 2024-08-29 |
| 5 | [Air Con: $1697 for an on/off switch](https://news.ycombinator.com/item?id=41386319) | 作者质疑一个开关为何需要支付一千六百九十七美元。 | 2001 | 478 | 2024-08-29 |
| 6 | ["We ran out of columns"](https://news.ycombinator.com/item?id=41146239) | 讲述遇到“已经没有列可用了”这一技术限制的经历。 | 1641 | 571 | 2024-08-03 |
| 7 | [I've built my first successful side project, and I hate it](https://news.ycombinator.com/item?id=41308599) | 作者讲述首个成功副业项目反而让自己厌恶的经历。 | 1492 | 419 | 2024-08-21 |
| 8 | [Microsoft donates the Mono Project to the Wine team](https://news.ycombinator.com/item?id=41371106) | 微软将 Mono 项目交给 Wine 团队。 | 1436 | 478 | 2024-08-27 |
| 9 | [CrowdStrike representatives issue trademark infringement notice to ClownStrike](https://news.ycombinator.com/item?id=41133917) | CrowdStrike 向 ClownStrike 发出商标侵权通知。 | 1234 | 229 | 2024-08-01 |
| 10 | [Starting Hospice](https://news.ycombinator.com/item?id=41157974) | 作者讲述开始接受临终关怀的经历。 | 1209 | 145 | 2024-08-05 |
| 11 | [Telegram founder Pavel Durov arrested at French airport](https://news.ycombinator.com/item?id=41341353) | Telegram 创始人 Pavel Durov 在法国机场被捕。 | 1175 | 1038 | 2024-08-24 |
| 12 | [Apple's requirements are about to hit creators and fans on Patreon](https://news.ycombinator.com/item?id=41224853) | Patreon 说明苹果要求将给创作者与支持者带来的影响。 | 1168 | 1018 | 2024-08-12 |
| 13 | [Diffusion models are real-time game engines](https://news.ycombinator.com/item?id=41375548) | 研究探索将扩散模型用作实时游戏引擎。 | 1149 | 409 | 2024-08-28 |
| 14 | [Show HN: InstantDB – A Modern Firebase](https://news.ycombinator.com/item?id=41322281) | InstantDB 开源客户端数据库，旨在简化实时协作应用开发。 | 1145 | 297 | 2024-08-22 |
| 15 | [Did you lose your AirPods?](https://news.ycombinator.com/item?id=41334207) | 从“你的 AirPods 丢了吗”出发，关注耳机遗失问题。 | 1115 | 380 | 2024-08-23 |
| 16 | [Mpv – A free, open-source, and cross-platform media player](https://news.ycombinator.com/item?id=41277014) | mpv 提供免费、开源且跨平台的媒体播放功能。 | 1113 | 559 | 2024-08-17 |
| 17 | [Building LLMs from the Ground Up: A 3-Hour Coding Workshop](https://news.ycombinator.com/item?id=41412256) | 通过三小时编程工作坊从基础构建大型语言模型。 | 970 | 136 | 2024-08-31 |
| 18 | [Jake Seliger has died](https://news.ycombinator.com/item?id=41201555) | 作家 Jake Seliger 去世。 | 960 | 193 | 2024-08-09 |
| 19 | [Google loses antitrust suit over search deals on phones](https://news.ycombinator.com/item?id=41164240) | 谷歌在涉及手机搜索协议的反垄断诉讼中败诉。 | 959 | 731 | 2024-08-05 |
| 20 | [NSA releases 1982 Grace Hopper lecture](https://news.ycombinator.com/item?id=41356528) | NSA 公开 Grace Hopper 于 1982 年发表的演讲。 | 946 | 227 | 2024-08-26 |

## 2024-09

有效主帖 23,735 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Bop Spotter](https://news.ycombinator.com/item?id=41694044) | 介绍音乐相关项目 Bop Spotter。 | 2433 | 385 | 2024-09-30 |
| 2 | [How to succeed in MrBeast production (Leaked PDF)](https://news.ycombinator.com/item?id=41549649) | 阅读泄漏文件，了解 MrBeast 视频制作团队的工作要求。 | 2115 | 1352 | 2024-09-15 |
| 3 | [Why wordfreq will not be updated](https://news.ycombinator.com/item?id=41578483) | wordfreq 作者解释停止更新词频资料的原因。 | 1707 | 510 | 2024-09-18 |
| 4 | [Learning to Reason with LLMs](https://news.ycombinator.com/item?id=41523070) | 探索如何让大型语言模型学会推理。 | 1654 | 1261 | 2024-09-12 |
| 5 | [We spent $20 to achieve RCE and accidentally became the admins of .mobi](https://news.ycombinator.com/item?id=41510252) | 研究者花二十美元实现远程代码执行，意外取得 .mobi 管理权限。 | 1624 | 367 | 2024-09-11 |
| 6 | [Apple mobile processors are now made in America by TSMC](https://news.ycombinator.com/item?id=41574844) | 台积电开始在美国制造苹果移动处理器。 | 1612 | 824 | 2024-09-18 |
| 7 | [Fraud, so much fraud](https://news.ycombinator.com/item?id=41672599) | 作者直面层出不穷的欺诈现象，表达对其规模的担忧。 | 1528 | 823 | 2024-09-27 |
| 8 | [I designed a Dieter Rams-inspired iPhone dock](https://news.ycombinator.com/item?id=41623467) | 作者展示受 Dieter Rams 风格启发的 iPhone 底座。 | 1509 | 356 | 2024-09-23 |
| 9 | [Amazon tells employees to return to office five days a week](https://news.ycombinator.com/item?id=41558554) | 亚马逊要求员工每周五天回办公室工作。 | 1498 | 1926 | 2024-09-16 |
| 10 | [Gaining access to anyones Arc browser without them even visiting a website](https://news.ycombinator.com/item?id=41597250) | 研究者发现无需受害者访问网页即可入侵其 Arc 浏览器的方法。 | 1469 | 498 | 2024-09-19 |
| 11 | [Is My Blue Your Blue?](https://news.ycombinator.com/item?id=41430258) | 通过颜色判断追问你看到的蓝色是否与别人相同。 | 1426 | 527 | 2024-09-03 |
| 12 | [An NFC movie library for my kids](https://news.ycombinator.com/item?id=41479141) | 家长为孩子搭建使用 NFC 选择影片的电影库。 | 1384 | 314 | 2024-09-08 |
| 13 | [Legalizing sports gambling was a mistake](https://news.ycombinator.com/item?id=41659458) | 作者认为将体育博彩合法化是错误决定。 | 1371 | 1153 | 2024-09-26 |
| 14 | [OpenAI to become for-profit company](https://news.ycombinator.com/item?id=41655954) | 报道称 OpenAI 将转为营利公司。 | 1346 | 745 | 2024-09-26 |
| 15 | [Founder Mode](https://news.ycombinator.com/item?id=41415023) | 探讨“创始人模式”的公司管理方式。 | 1330 | 735 | 2024-09-01 |
| 16 | [Sanding UI](https://news.ycombinator.com/item?id=41612154) | 介绍打磨用户界面的细节。 | 1300 | 400 | 2024-09-21 |
| 17 | [Orion, our first true augmented reality glasses](https://news.ycombinator.com/item?id=41650047) | Meta 展示增强现实眼镜 Orion。 | 1227 | 1041 | 2024-09-25 |
| 18 | [Greppability is an underrated code metric](https://news.ycombinator.com/item?id=41430772) | 作者认为代码是否容易搜索是被低估的质量指标。 | 1217 | 613 | 2024-09-03 |
| 19 | [I Am Tired of AI](https://news.ycombinator.com/item?id=41667652) | 作者表达对人工智能话题的疲惫。 | 1209 | 1121 | 2024-09-27 |
| 20 | [Ask HN: Why is Pave legal?](https://news.ycombinator.com/item?id=41510103) | 用户质疑汇集企业薪资数据并提供对比的 Pave 是否合法。 | 1098 | 495 | 2024-09-11 |

## 2024-10

有效主帖 24,463 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Starship Flight 5: Launch and booster catch [video]](https://news.ycombinator.com/item?id=41827362) | 观看星舰第五次试飞发射及助推器回收。 | 2263 | 1350 | 2024-10-13 |
| 2 | [FTC announces "click-to-cancel" rule making it easier to cancel subscriptions](https://news.ycombinator.com/item?id=41858665) | 美国 FTC 推出点击即可取消订阅的规则。 | 1747 | 760 | 2024-10-16 |
| 3 | [1 bug, $50k in bounties, a Zendesk backdoor](https://news.ycombinator.com/item?id=41818459) | 一个 Zendesk 后门漏洞带来五万美元赏金。 | 1637 | 417 | 2024-10-12 |
| 4 | [Patent troll Sable pays up, dedicates all its patents to the public](https://news.ycombinator.com/item?id=41730415) | 专利诉讼公司 Sable 支付款项并将全部专利开放给公众。 | 1524 | 419 | 2024-10-03 |
| 5 | [ChatGPT Search](https://news.ycombinator.com/item?id=42008569) | OpenAI 推出 ChatGPT 搜索。 | 1485 | 1251 | 2024-10-31 |
| 6 | [Computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku](https://news.ycombinator.com/item?id=41914989) | Anthropic 推出电脑操作能力及新版 Claude 3.5 Sonnet、Haiku。 | 1454 | 735 | 2024-10-22 |
| 7 | [First images from Euclid are in](https://news.ycombinator.com/item?id=41908075) | 欧几里得空间望远镜首批图像公布。 | 1413 | 396 | 2024-10-21 |
| 8 | [Busy Status Bar](https://news.ycombinator.com/item?id=41838337) | 介绍 Busy Status Bar。 | 1371 | 461 | 2024-10-14 |
| 9 | [Helping wikis move away from Fandom](https://news.ycombinator.com/item?id=41797719) | 介绍帮助维基站点离开 Fandom 的行动。 | 1176 | 487 | 2024-10-10 |
| 10 | [Australia/Lord_Howe is the weirdest timezone](https://news.ycombinator.com/item?id=41992314) | 探究 Australia/Lord_Howe 时区为何格外特殊。 | 1147 | 455 | 2024-10-30 |
| 11 | [We can now fix McDonald's ice cream machines](https://news.ycombinator.com/item?id=41949098) | 介绍如今可以维修麦当劳冰淇淋机的变化。 | 1112 | 303 | 2024-10-25 |
| 12 | [Meta Movie Gen](https://news.ycombinator.com/item?id=41740965) | Meta 展示视频生成系统 Movie Gen。 | 1107 | 1006 | 2024-10-04 |
| 13 | [DeskPad – A virtual monitor for screen sharing](https://news.ycombinator.com/item?id=41800602) | DeskPad 为屏幕共享提供虚拟显示器。 | 1097 | 157 | 2024-10-10 |
| 14 | [Internet Archive: Security breach alert](https://news.ycombinator.com/item?id=41792500) | 互联网档案馆发布安全入侵警报。 | 1091 | 607 | 2024-10-09 |
| 15 | [Why does man print "gimme gimme gimme" at 00:30? (2017)](https://news.ycombinator.com/item?id=41736903) | 解释 man 命令为何在凌晨零点三十分输出特定歌词。 | 1058 | 409 | 2024-10-04 |
| 16 | [Bitwarden SDK relicensed from proprietary to GPLv3](https://news.ycombinator.com/item?id=41940580) | Bitwarden SDK 从专有许可改为 GPLv3。 | 1014 | 369 | 2024-10-24 |
| 17 | [Canvas is a new way to write and code with ChatGPT](https://news.ycombinator.com/item?id=41732634) | Canvas 为与 ChatGPT 协作写作和编程提供新界面。 | 985 | 679 | 2024-10-03 |
| 18 | [A $1k Wheelchair](https://news.ycombinator.com/item?id=41711437) | 介绍一款一千美元的轮椅。 | 965 | 434 | 2024-10-01 |
| 19 | [Steam games will need to disclose kernel-level anti-cheat on store pages](https://news.ycombinator.com/item?id=41999314) | Steam 要求游戏在商店页面披露内核级反作弊软件。 | 963 | 640 | 2024-10-30 |
| 20 | [AAA Gaming on Asahi Linux](https://news.ycombinator.com/item?id=41799068) | 探索在 Asahi Linux 上运行大型商业游戏。 | 944 | 365 | 2024-10-10 |

## 2024-11

有效主帖 22,247 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [IMG_0416](https://news.ycombinator.com/item?id=42102506) | 以常见影像文件名 IMG_0416 为题，呈现一个值得查看的作品。 | 2310 | 324 | 2024-11-10 |
| 2 | [MomBoard: E-ink display for a parent with amnesia](https://news.ycombinator.com/item?id=42135520) | MomBoard 用电子墨水屏帮助一位患失忆症的家长。 | 2106 | 251 | 2024-11-14 |
| 3 | [The Onion buys Infowars](https://news.ycombinator.com/item?id=42136259) | 讽刺媒体 The Onion 收购 Infowars。 | 1901 | 1233 | 2024-11-14 |
| 4 | [Trump wins presidency for second time](https://news.ycombinator.com/item?id=42057647) | 特朗普第二次赢得美国总统选举。 | 1796 | 9274 | 2024-11-06 |
| 5 | [Passport Photos](https://news.ycombinator.com/item?id=42069646) | 关注护照照片这一既常见又有特别要求的图像类型。 | 1538 | 226 | 2024-11-06 |
| 6 | [How I ship projects at big tech companies](https://news.ycombinator.com/item?id=42111031) | 作者分享在大型科技公司推进项目上线的方法。 | 1425 | 381 | 2024-11-11 |
| 7 | [Send someone you appreciate an official 'Continue and Persist' Letter](https://news.ycombinator.com/item?id=42268580) | 一个用仿法律函件鼓励他人继续坚持的创意项目。 | 1414 | 224 | 2024-11-28 |
| 8 | [Touchscreens are out, and tactile controls are back](https://news.ycombinator.com/item?id=42033241) | 介绍触摸屏退潮与实体触觉控制回归的趋势。 | 1317 | 890 | 2024-11-03 |
| 9 | [DOJ will push Google to sell off Chrome](https://news.ycombinator.com/item?id=42177767) | 美国司法部将推动谷歌出售 Chrome。 | 1248 | 1437 | 2024-11-18 |
| 10 | [Apple acquires Pixelmator](https://news.ycombinator.com/item?id=42018013) | 苹果收购图像编辑软件 Pixelmator。 | 1184 | 576 | 2024-11-01 |
| 11 | [Show HN: I built a(nother) house optimized for LAN parties](https://news.ycombinator.com/item?id=42156977) | 作者展示专为局域网聚会优化的房屋及其网络启动管理方案。 | 1117 | 381 | 2024-11-16 |
| 12 | [No GPS required: our app can now locate underground trains](https://news.ycombinator.com/item?id=42122085) | 开发团队让应用无需 GPS 也能定位地下列车。 | 1076 | 317 | 2024-11-13 |
| 13 | [Malware can turn off webcam LED and record video, demonstrated on ThinkPad X230](https://news.ycombinator.com/item?id=42259278) | 研究者在 ThinkPad X230 演示关闭摄像头指示灯后录影。 | 1042 | 521 | 2024-11-27 |
| 14 | [CSS gets a new logo and it uses the color `rebeccapurple`](https://news.ycombinator.com/item?id=42161919) | CSS 新标志采用 rebeccapurple 紫色。 | 908 | 184 | 2024-11-17 |
| 15 | [Hacking 700M Electronic Arts accounts](https://news.ycombinator.com/item?id=42052143) | 介绍影响七亿个艺电账号的安全研究。 | 902 | 154 | 2024-11-05 |
| 16 | [ICC issues warrants for Netanyahu, Gallant, and Hamas officials](https://news.ycombinator.com/item?id=42203543) | 国际刑事法院对内塔尼亚胡、加兰特及哈马斯官员发出逮捕令。 | 890 | 1023 | 2024-11-21 |
| 17 | [Model Context Protocol](https://news.ycombinator.com/item?id=42237424) | 介绍模型上下文协议 MCP。 | 872 | 258 | 2024-11-25 |
| 18 | [Useful built-in macOS command-line utilities](https://news.ycombinator.com/item?id=42057431) | 整理 macOS 自带的实用命令行工具。 | 837 | 231 | 2024-11-06 |
| 19 | [Show HN: App that asks ‘why?’ every time you unlock your phone](https://news.ycombinator.com/item?id=42254156) | 一款每次解锁手机时都会问用户“为什么”的应用。 | 817 | 381 | 2024-11-27 |
| 20 | [RFC 35140: HTTP Do-Not-Stab (2023)](https://news.ycombinator.com/item?id=42232040) | 阅读禁止刺伤的虚构 HTTP 协议 RFC。 | 815 | 211 | 2024-11-25 |

## 2024-12

有效主帖 22,564 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Moon](https://news.ycombinator.com/item?id=42443229) | 以月球为主角，重新观察这颗熟悉的天体。 | 3128 | 250 | 2024-12-17 |
| 2 | [Ghostty 1.0](https://news.ycombinator.com/item?id=42517447) | 终端模拟器 Ghostty 发布 1.0 版。 | 2319 | 681 | 2024-12-26 |
| 3 | [IMG_0001](https://news.ycombinator.com/item?id=42314547) | 以常见影像文件名 IMG_0001 为题，呈现一个值得查看的作品。 | 1861 | 290 | 2024-12-04 |
| 4 | [Cognitive load is what matters](https://news.ycombinator.com/item?id=42489645) | 作者认为认知负担是软件设计的关键。 | 1769 | 721 | 2024-12-22 |
| 5 | [OpenAI O3 breakthrough high score on ARC-AGI-PUB](https://news.ycombinator.com/item?id=42473321) | OpenAI o3 在 ARC-AGI 公开测试取得突破性高分。 | 1724 | 1755 | 2024-12-20 |
| 6 | [Merry Christmas Everyone](https://news.ycombinator.com/item?id=42506577) | HN 用户互祝圣诞快乐，并邀请大家分享节日回忆。 | 1503 | 383 | 2024-12-25 |
| 7 | [Every V4 UUID](https://news.ycombinator.com/item?id=42342382) | 一个试图呈现所有第四版 UUID 的项目。 | 1429 | 356 | 2024-12-06 |
| 8 | [Willow, Our Quantum Chip](https://news.ycombinator.com/item?id=42367649) | 谷歌介绍量子芯片 Willow。 | 1410 | 528 | 2024-12-09 |
| 9 | [Advent of Code 2024](https://news.ycombinator.com/item?id=42287231) | 关注 2024 年 Advent of Code 编程挑战。 | 1388 | 554 | 2024-12-01 |
| 10 | [Apple Photos phones home on iOS 18 and macOS 15](https://news.ycombinator.com/item?id=42533685) | 苹果照片应用被指在 iOS 18 与 macOS 15 中向服务器回传信息。 | 1330 | 984 | 2024-12-28 |
| 11 | [Timemap.org – Interactive Map of History](https://news.ycombinator.com/item?id=42397550) | Timemap.org 用交互地图呈现历史。 | 1306 | 180 | 2024-12-12 |
| 12 | [My son (9 yrs old) used plain JavaScript to make a game, and wants your feedback](https://news.ycombinator.com/item?id=42312121) | 九岁孩子手写 HTML、CSS 与 JavaScript 制作游戏，家长邀请反馈。 | 1251 | 480 | 2024-12-03 |
| 13 | [Genie 2: A large-scale foundation world model](https://news.ycombinator.com/item?id=42317903) | Genie 2 是一种大规模基础世界模型。 | 1247 | 410 | 2024-12-04 |
| 14 | [Happy New Year 2025](https://news.ycombinator.com/item?id=42562750) | HN 用户向社区送上 2025 年新年祝福。 | 1223 | 258 | 2024-12-31 |
| 15 | [Itch.io Taken Down by Funko](https://news.ycombinator.com/item?id=42363727) | Itch.io 因 Funko 的行动而下线。 | 1197 | 463 | 2024-12-09 |
| 16 | [From where I left](https://news.ycombinator.com/item?id=42378488) | 作者从此前停下的位置继续讲述。 | 1190 | 455 | 2024-12-10 |
| 17 | [Jimmy Carter has died](https://news.ycombinator.com/item?id=42543128) | 美国前总统 Jimmy Carter 去世。 | 1183 | 826 | 2024-12-29 |
| 18 | [Sora is here](https://news.ycombinator.com/item?id=42368604) | OpenAI 宣布视频生成工具 Sora 上线。 | 1152 | 983 | 2024-12-09 |
| 19 | [macOS menu bar app that shows how full the ISS urine tank is in real time](https://news.ycombinator.com/item?id=42505454) | 一款在 macOS 菜单栏实时显示国际空间站尿液箱容量的应用。 | 1139 | 253 | 2024-12-24 |
| 20 | [Gukesh becomes the youngest chess world champion in history](https://news.ycombinator.com/item?id=42398952) | Gukesh 成为史上最年轻的国际象棋世界冠军。 | 1118 | 459 | 2024-12-12 |

## 2025-01

有效主帖 25,086 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I made an open-source laptop from scratch](https://news.ycombinator.com/item?id=42797260) | 开发者分享用约半年从零设计并开源笔记本电脑的成果。 | 3237 | 323 | 2025-01-22 |
| 2 | [Stimulation Clicker](https://news.ycombinator.com/item?id=42611536) | 介绍点击游戏 Stimulation Clicker。 | 3082 | 589 | 2025-01-06 |
| 3 | [We're bringing Pebble back](https://news.ycombinator.com/item?id=42845091) | Pebble 团队与社区宣布以可持续方式重启手表项目，并感谢谷歌。 | 2843 | 738 | 2025-01-27 |
| 4 | [Thank HN: My bootstrapped startup got acquired today](https://news.ycombinator.com/item?id=42806247) | VWO 创始人感谢 HN 早期支持，并分享以两亿美元出售公司的消息。 | 2246 | 396 | 2025-01-23 |
| 5 | [Ross Ulbricht granted a full pardon](https://news.ycombinator.com/item?id=42786962) | Ross Ulbricht 获得全面赦免。 | 1864 | 2233 | 2025-01-22 |
| 6 | [DeepSeek-R1](https://news.ycombinator.com/item?id=42768072) | 介绍 DeepSeek-R1 模型。 | 1843 | 663 | 2025-01-20 |
| 7 | [I've acquired a new superpower](https://news.ycombinator.com/item?id=42655870) | 作者分享获得一种新能力的经历。 | 1807 | 557 | 2025-01-10 |
| 8 | [No Calls](https://news.ycombinator.com/item?id=42725385) | 以“不打电话”为题，关注电话交流这一选择。 | 1603 | 517 | 2025-01-16 |
| 9 | [0-click deanonymization attack targeting Signal, Discord, other platforms](https://news.ycombinator.com/item?id=42780816) | 研究者披露针对 Signal、Discord 等平台的零点击去匿名攻击。 | 1457 | 438 | 2025-01-21 |
| 10 | [JavaScript Temporal is coming](https://news.ycombinator.com/item?id=42876840) | JavaScript 的 Temporal 日期时间接口即将到来。 | 1405 | 399 | 2025-01-30 |
| 11 | [OpenAI Furious DeepSeek Might Have Stolen All the Data OpenAI Stole from Us](https://news.ycombinator.com/item?id=42865527) | 作者讽刺 OpenAI 指责 DeepSeek 盗用其数据的立场。 | 1361 | 16 | 2025-01-29 |
| 12 | [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL](https://news.ycombinator.com/item?id=42823568) | DeepSeek-R1 探索用强化学习激励语言模型推理能力。 | 1351 | 1056 | 2025-01-25 |
| 13 | [I had to take down my course-swapping site or be expelled](https://news.ycombinator.com/item?id=42638626) | 学生称被要求关闭换课网站，否则将遭开除。 | 1349 | 698 | 2025-01-08 |
| 14 | [DOOM CAPTCHA](https://news.ycombinator.com/item?id=42566112) | 一个用《毁灭战士》游戏设计的验证码。 | 1316 | 270 | 2025-01-01 |
| 15 | [Show HN: Tetris in a PDF](https://news.ycombinator.com/item?id=42645218) | 开发者利用浏览器 PDF 引擎的 JavaScript 功能实现俄罗斯方块。 | 1289 | 223 | 2025-01-09 |
| 16 | [Google open-sources the Pebble OS](https://news.ycombinator.com/item?id=42845070) | 谷歌开放 Pebble OS 源代码。 | 1263 | 200 | 2025-01-27 |
| 17 | [David Lynch has died](https://news.ycombinator.com/item?id=42728862) | 电影导演 David Lynch 去世。 | 1190 | 373 | 2025-01-16 |
| 18 | [Meta's memo to employees rolling back DEI programs](https://news.ycombinator.com/item?id=42657901) | Meta 内部备忘录宣布收缩 DEI 计划。 | 1189 | 1744 | 2025-01-10 |
| 19 | [I still like Sublime Text](https://news.ycombinator.com/item?id=42862246) | 作者解释自己为何仍喜欢 Sublime Text。 | 1184 | 602 | 2025-01-29 |
| 20 | [TikTok goes dark in the US](https://news.ycombinator.com/item?id=42753396) | TikTok 在美国停止服务。 | 1180 | 2458 | 2025-01-19 |

## 2025-02

有效主帖 22,445 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Zelensky leaves White House after angry meeting](https://news.ycombinator.com/item?id=43208973) | 泽连斯基在激烈争执后离开白宫。 | 2936 | 5044 | 2025-02-28 |
| 2 | [Claude 3.7 Sonnet and Claude Code](https://news.ycombinator.com/item?id=43163011) | Anthropic 推出 Claude 3.7 Sonnet 与 Claude Code。 | 2127 | 963 | 2025-02-24 |
| 3 | [Everyone knows your location: tracking myself down through in-app ads](https://news.ycombinator.com/item?id=42909921) | 作者通过应用内广告追踪自己，揭示位置隐私风险。 | 1957 | 600 | 2025-02-02 |
| 4 | [Valve releases Team Fortress 2 code](https://news.ycombinator.com/item?id=43094260) | Valve 发布《军团要塞 2》代码。 | 1863 | 387 | 2025-02-18 |
| 5 | [“A calculator app? Anyone could make that”](https://news.ycombinator.com/item?id=43066953) | 作者反思“计算器应用谁都能做”这一看法。 | 1821 | 430 | 2025-02-16 |
| 6 | [Apple pulls data protection tool after UK government security row](https://news.ycombinator.com/item?id=43128253) | 与英国政府发生安全争议后，苹果撤下数据保护功能。 | 1770 | 1068 | 2025-02-21 |
| 7 | [The young, inexperienced engineers aiding DOGE](https://news.ycombinator.com/item?id=42910910) | 介绍参与 DOGE 工作的年轻、经验有限的工程师。 | 1683 | 2991 | 2025-02-02 |
| 8 | [Teen on Musk's DOGE team graduated from 'The Com'](https://news.ycombinator.com/item?id=42981756) | 报道称马斯克 DOGE 团队的一名少年成员出身网络社群 The Com。 | 1624 | 1801 | 2025-02-08 |
| 9 | [Leaking the email of any YouTube user for $10k](https://news.ycombinator.com/item?id=43024221) | 研究者展示可泄漏任意 YouTube 用户邮箱的漏洞，并获一万美元赏金。 | 1624 | 466 | 2025-02-12 |
| 10 | [Show HN: I got laid off from Meta and created a minor hit on Steam](https://news.ycombinator.com/item?id=43186406) | 一位被 Meta 裁员的工程师分享开发弹珠肉鸽游戏并在 Steam 小获成功的经历。 | 1581 | 356 | 2025-02-26 |
| 11 | [I tasted Honda’s spicy rodent-repelling tape and I will do it again (2021)](https://news.ycombinator.com/item?id=43013615) | 作者品尝本田辣味防鼠胶带，并称还会再试。 | 1579 | 454 | 2025-02-11 |
| 12 | [WikiTok](https://news.ycombinator.com/item?id=42936723) | 介绍 WikiTok 项目。 | 1459 | 221 | 2025-02-04 |
| 13 | [It is no longer safe to move our governments and societies to US clouds](https://news.ycombinator.com/item?id=43150085) | 作者认为政府与社会机构继续迁往美国云服务已不安全。 | 1403 | 800 | 2025-02-23 |
| 14 | [All Kindles can now be jailbroken](https://news.ycombinator.com/item?id=43073969) | 所有 Kindle 机型如今都能越狱。 | 1377 | 423 | 2025-02-17 |
| 15 | [Tell HN: Cloudflare is blocking Pale Moon and other non-mainstream browsers](https://news.ycombinator.com/item?id=42953508) | 用户称 Cloudflare 验证机制阻止 Pale Moon 等小众浏览器访问网站。 | 1343 | 524 | 2025-02-05 |
| 16 | [TypeScript types can run DOOM [video]](https://news.ycombinator.com/item?id=43184291) | 展示用 TypeScript 类型系统运行《毁灭战士》。 | 1328 | 360 | 2025-02-26 |
| 17 | [Undergraduate shows that searches within hash tables can be much faster](https://news.ycombinator.com/item?id=43002511) | 一位本科生提出可显著加快哈希表查找的方法。 | 1304 | 584 | 2025-02-10 |
| 18 | [Ingesting PDFs and why Gemini 2.0 changes everything](https://news.ycombinator.com/item?id=42952605) | 作者探讨 Gemini 2.0 如何改变 PDF 文档处理。 | 1303 | 447 | 2025-02-05 |
| 19 | [Meta torrented & seeded 81.7 TB dataset containing copyrighted data](https://news.ycombinator.com/item?id=42971446) | Meta 被指下载并做种含受版权保护资料的 81.7 TB 数据集。 | 1270 | 938 | 2025-02-07 |
| 20 | [EA Open Sources Command and Conquer: Red Alert, along with other games](https://news.ycombinator.com/item?id=43197131) | 艺电开源《命令与征服：红色警戒》等游戏。 | 1262 | 325 | 2025-02-27 |

## 2025-03

有效主帖 25,331 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [U.S. national-security leaders included me in a group chat](https://news.ycombinator.com/item?id=43462783) | 记者称美国国家安全高层误将自己加入工作群聊。 | 2283 | 1291 | 2025-03-24 |
| 2 | [uBlock Origin is no longer available on the Chrome Store](https://news.ycombinator.com/item?id=43322922) | uBlock Origin 不再能从 Chrome 应用商店获取。 | 1972 | 987 | 2025-03-10 |
| 3 | [Docs – Open source alternative to Notion or Outline](https://news.ycombinator.com/item?id=43378239) | Docs 提供 Notion 或 Outline 的开源替代方案。 | 1952 | 454 | 2025-03-16 |
| 4 | [A 10x Faster TypeScript](https://news.ycombinator.com/item?id=43332830) | 介绍让 TypeScript 速度提高十倍的方案。 | 1827 | 907 | 2025-03-11 |
| 5 | [Mistral OCR](https://news.ycombinator.com/item?id=43282905) | Mistral 发布 OCR 工具。 | 1756 | 417 | 2025-03-06 |
| 6 | [Apple restricts Pebble from being awesome with iPhones](https://news.ycombinator.com/item?id=43401245) | Pebble 团队称苹果限制其手表在 iPhone 上发挥功能。 | 1678 | 1106 | 2025-03-18 |
| 7 | [Two new PebbleOS watches](https://news.ycombinator.com/item?id=43400989) | 介绍两款搭载 PebbleOS 的新手表。 | 1658 | 525 | 2025-03-18 |
| 8 | [Stoop Coffee: A simple idea transformed my neighborhood](https://news.ycombinator.com/item?id=43473618) | 作者分享 Stoop Coffee 如何以简单想法改变邻里关系。 | 1652 | 498 | 2025-03-25 |
| 9 | [Mark Klein, AT&T whistleblower who revealed NSA mass spying, has died](https://news.ycombinator.com/item?id=43347662) | 揭露 NSA 大规模监控的 AT&T 举报者 Mark Klein 去世。 | 1597 | 354 | 2025-03-12 |
| 10 | [Happy 20th birthday, Y Combinator](https://news.ycombinator.com/item?id=43332658) | Y Combinator 迎来二十周年。 | 1421 | 276 | 2025-03-11 |
| 11 | [GIMP 3.0](https://news.ycombinator.com/item?id=43393822) | 开源图像编辑器 GIMP 发布 3.0 版。 | 1312 | 508 | 2025-03-17 |
| 12 | [Claude can now search the web](https://news.ycombinator.com/item?id=43425655) | Claude 新增网页搜索能力。 | 1233 | 726 | 2025-03-20 |
| 13 | [Apple's Software Quality Crisis](https://news.ycombinator.com/item?id=43243075) | 作者分析苹果软件质量面临的危机。 | 1196 | 1198 | 2025-03-03 |
| 14 | [Everyone knows all the apps on your phone](https://news.ycombinator.com/item?id=43518866) | 作者揭示手机已安装应用列表可能被他人获知的风险。 | 1195 | 479 | 2025-03-29 |
| 15 | [US Ends Support For Ukrainian F-16s](https://news.ycombinator.com/item?id=43307996) | 报道称美国停止支持乌克兰的 F-16 战机。 | 1184 | 2215 | 2025-03-09 |
| 16 | [How each pillar of the First Amendment is under attack](https://news.ycombinator.com/item?id=43529707) | 分析美国第一修正案各项权利面临的挑战。 | 1176 | 916 | 2025-03-31 |
| 17 | [A Letter to the American People](https://news.ycombinator.com/item?id=43224350) | 阅读一封致美国人民的公开信。 | 1081 | 535 | 2025-03-01 |
| 18 | [Apple M3 Ultra](https://news.ycombinator.com/item?id=43266453) | 苹果发布 M3 Ultra 芯片。 | 1077 | 1029 | 2025-03-05 |
| 19 | [4o Image Generation](https://news.ycombinator.com/item?id=43474112) | 介绍 GPT-4o 的图像生成功能。 | 1072 | 599 | 2025-03-25 |
| 20 | [Tracing the thoughts of a large language model](https://news.ycombinator.com/item?id=43495617) | 研究者追踪大型语言模型的内部思考过程。 | 1072 | 394 | 2025-03-27 |

## 2025-04

有效主帖 24,427 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [What if we made advertising illegal?](https://news.ycombinator.com/item?id=43595269) | 设想如果广告被禁止，世界会发生怎样的变化。 | 1975 | 1386 | 2025-04-05 |
| 2 | [CVE program faces swift end after DHS fails to renew contract [updated]](https://news.ycombinator.com/item?id=43700607) | 美国国土安全部未续约，CVE 项目一度面临迅速终止风险。 | 1934 | 1094 | 2025-04-16 |
| 3 | [US Administration announces 34% tariffs on China, 20% on EU](https://news.ycombinator.com/item?id=43561253) | 美国政府宣布对中国加征 34%、对欧盟加征 20% 关税。 | 1877 | 3603 | 2025-04-02 |
| 4 | [Getting forked by Microsoft](https://news.ycombinator.com/item?id=43750535) | 开发者讲述项目被微软分叉的经历。 | 1865 | 998 | 2025-04-21 |
| 5 | [Tell HN: Announcing tomhow as a public moderator](https://news.ycombinator.com/item?id=43558671) | HN 宣布 Tom Howard 公开担任管理员，与 dang 共同维护社区。 | 1825 | 462 | 2025-04-02 |
| 6 | [Middle-aged man trading cards go viral in rural Japan town](https://news.ycombinator.com/item?id=43615912) | 日本乡村小镇的中年男子集换卡意外走红。 | 1817 | 403 | 2025-04-07 |
| 7 | [Apache ECharts](https://news.ycombinator.com/item?id=43624220) | 介绍可视化图表库 Apache ECharts。 | 1658 | 250 | 2025-04-08 |
| 8 | [Widespread power outage in Spain and Portugal](https://news.ycombinator.com/item?id=43819791) | 用户报告西班牙与葡萄牙发生大范围停电。 | 1560 | 1165 | 2025-04-28 |
| 9 | [But what if I want a faster horse?](https://news.ycombinator.com/item?id=43652723) | 作者追问如果用户确实想要更快的马该怎么办。 | 1525 | 609 | 2025-04-11 |
| 10 | [Cursor IDE support hallucinates lockout policy, causes user cancellations](https://news.ycombinator.com/item?id=43683012) | 用户称 Cursor 客服捏造多设备登录限制，导致用户取消订阅。 | 1511 | 606 | 2025-04-14 |
| 11 | [An image of an archeologist adventurer who wears a hat and uses a bullwhip](https://news.ycombinator.com/item?id=43573156) | 展示一张戴帽、使用长鞭的冒险考古学家图像。 | 1503 | 898 | 2025-04-03 |
| 12 | [A $20k American-made electric pickup with no paint, no stereo, no screen](https://news.ycombinator.com/item?id=43794284) | 介绍一款美国制造、售价两万美元且无涂装和屏幕的电动皮卡。 | 1457 | 1297 | 2025-04-25 |
| 13 | [Someone at YouTube needs glasses](https://news.ycombinator.com/item?id=43846487) | 作者调侃 YouTube 某些设计似乎需要改善视力。 | 1424 | 694 | 2025-04-30 |
| 14 | [You wouldn't steal a font](https://news.ycombinator.com/item?id=43775926) | 借反盗版宣传口吻讨论字体使用问题。 | 1401 | 394 | 2025-04-23 |
| 15 | [Harvard's response to federal government letter demanding changes](https://news.ycombinator.com/item?id=43684536) | 哈佛回应联邦政府要求其作出改变的来函。 | 1391 | 1403 | 2025-04-14 |
| 16 | [How a 20 year old bug in GTA San Andreas surfaced in Windows 11 24H2](https://news.ycombinator.com/item?id=43772311) | 分析《圣安地列斯》二十年前的缺陷如何在 Windows 11 24H2 再现。 | 1371 | 298 | 2025-04-23 |
| 17 | [The Llama 4 herd](https://news.ycombinator.com/item?id=43595585) | Meta 推出 Llama 4 模型家族。 | 1235 | 658 | 2025-04-05 |
| 18 | [Leaked data reveals Israeli govt campaign to remove pro-Palestine posts on Meta](https://news.ycombinator.com/item?id=43655603) | 泄漏数据显示以色列政府推动 Meta 移除支持巴勒斯坦的帖子。 | 1214 | 960 | 2025-04-11 |
| 19 | [Standard Ebooks: liberated ebooks, carefully produced for the true book lover](https://news.ycombinator.com/item?id=43599637) | Standard Ebooks 精心制作并开放电子书。 | 1213 | 247 | 2025-04-06 |
| 20 | [Whistleblower details how DOGE may have taken sensitive NLRB data](https://news.ycombinator.com/item?id=43691142) | 举报者详述 DOGE 可能获取美国劳资关系委员会敏感数据的经过。 | 1171 | 542 | 2025-04-15 |

## 2025-05

有效主帖 25,279 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Claude 4](https://news.ycombinator.com/item?id=44063703) | Anthropic 发布 Claude 4 模型。 | 2013 | 1170 | 2025-05-22 |
| 2 | [Redis is open source again](https://news.ycombinator.com/item?id=43859446) | Redis 重新采用开源许可。 | 1896 | 789 | 2025-05-01 |
| 3 | [The Windows Subsystem for Linux is now open source](https://news.ycombinator.com/item?id=44031385) | 微软宣布 Windows Linux 子系统开源。 | 1613 | 1194 | 2025-05-19 |
| 4 | [Plain Vanilla Web](https://news.ycombinator.com/item?id=43954896) | 介绍使用原生网页技术的开发方式。 | 1519 | 685 | 2025-05-11 |
| 5 | [I'd rather read the prompt](https://news.ycombinator.com/item?id=43888803) | 作者表示相比生成内容，自己更愿意阅读原始提示词。 | 1444 | 839 | 2025-05-04 |
| 6 | [Baby is healed with first personalized gene-editing treatment](https://news.ycombinator.com/item?id=43997636) | 一名婴儿接受首例个性化基因编辑治疗后康复。 | 1257 | 531 | 2025-05-15 |
| 7 | [Mozilla to shut down Pocket and Fakespot](https://news.ycombinator.com/item?id=44063662) | Mozilla 宣布关闭 Pocket 与 Fakespot。 | 1222 | 761 | 2025-05-22 |
| 8 | [CSS Minecraft](https://news.ycombinator.com/item?id=44100148) | 展示用 CSS 制作的 Minecraft 内容。 | 1220 | 140 | 2025-05-26 |
| 9 | [From: Steve Jobs. "Great idea, thank you."](https://news.ycombinator.com/item?id=43929724) | 回看 Steve Jobs 回复“好主意，谢谢”的一封邮件。 | 1209 | 292 | 2025-05-08 |
| 10 | [The curse of knowing how, or; fixing everything](https://news.ycombinator.com/item?id=43902212) | 作者反思懂得如何修理后就忍不住修好一切的负担。 | 1197 | 441 | 2025-05-06 |
| 11 | [Apple violated antitrust ruling, judge finds](https://news.ycombinator.com/item?id=43852145) | 法官认定苹果违反反垄断裁决。 | 1165 | 602 | 2025-05-01 |
| 12 | [Show HN: Clippy – 90s UI for local LLMs](https://news.ycombinator.com/item?id=43905942) | Clippy 用九十年代界面风格呈现本地语言模型。 | 1122 | 275 | 2025-05-06 |
| 13 | [Photos taken inside musical instruments](https://news.ycombinator.com/item?id=44139626) | 展示从乐器内部拍摄的照片。 | 1121 | 52 | 2025-05-30 |
| 14 | [Watching AI drive Microsoft employees insane](https://news.ycombinator.com/item?id=44050152) | 作者观察人工智能如何令微软员工陷入困扰。 | 1088 | 552 | 2025-05-21 |
| 15 | [Postgres IDE in VS Code](https://news.ycombinator.com/item?id=44073588) | 介绍集成到 VS Code 的 Postgres 开发环境。 | 1040 | 407 | 2025-05-23 |
| 16 | [Judge rules Apple executive lied under oath, makes criminal contempt referral](https://news.ycombinator.com/item?id=43856795) | 法官认定苹果高管宣誓作伪证，并建议启动刑事藐视程序。 | 1036 | 360 | 2025-05-01 |
| 17 | [AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms](https://news.ycombinator.com/item?id=43985489) | AlphaEvolve 借助 Gemini 编程智能体设计高级算法。 | 1036 | 270 | 2025-05-14 |
| 18 | [Spaced repetition systems have gotten better](https://news.ycombinator.com/item?id=44020591) | 作者介绍间隔重复学习系统的改进。 | 1026 | 512 | 2025-05-18 |
| 19 | [Coding without a laptop: Two weeks with AR glasses and Linux on Android](https://news.ycombinator.com/item?id=43985513) | 作者用 AR 眼镜与 Android 上的 Linux 尝试两周无笔记本编程。 | 1016 | 386 | 2025-05-14 |
| 20 | [Void: Open-source Cursor alternative](https://news.ycombinator.com/item?id=43927926) | Void 提供开源的 Cursor 替代方案。 | 948 | 343 | 2025-05-08 |

## 2025-06

有效主帖 23,844 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Help restore the tax deduction for software dev in the US (Section 174)](https://news.ycombinator.com/item?id=44226145) | 用户呼吁推动修改美国税法第 174 条，恢复软件开发费用直接抵扣。 | 2439 | 907 | 2025-06-09 |
| 2 | [My AI skeptic friends are all nuts](https://news.ycombinator.com/item?id=44163063) | 作者对持怀疑态度的 AI 朋友提出强烈反驳。 | 2356 | 2826 | 2025-06-02 |
| 3 | [Self-hosting your own media considered harmful according to YouTube](https://news.ycombinator.com/item?id=44197932) | 作者质疑 YouTube 为何将自托管媒体视为有害。 | 1634 | 760 | 2025-06-06 |
| 4 | [Bill Atkinson has died](https://news.ycombinator.com/item?id=44210606) | 计算机先驱 Bill Atkinson 去世。 | 1589 | 273 | 2025-06-07 |
| 5 | [The time bomb in the tax code that's fueling mass tech layoffs](https://news.ycombinator.com/item?id=44180533) | 作者分析税法中的开发费用规则如何推动科技业裁员。 | 1575 | 948 | 2025-06-04 |
| 6 | [Show HN: I'm an airline pilot – I built interactive graphs/globes of my flights](https://news.ycombinator.com/item?id=44396518) | 航空公司飞行员将数字飞行日志制作成交互图表与三维地球。 | 1539 | 197 | 2025-06-27 |
| 7 | [Andrej Karpathy: Software in the era of AI [video]](https://news.ycombinator.com/item?id=44314423) | Andrej Karpathy 讨论人工智能时代的软件。 | 1481 | 783 | 2025-06-19 |
| 8 | [GCP Outage](https://news.ycombinator.com/item?id=44260810) | 谷歌云平台发生服务故障。 | 1468 | 494 | 2025-06-12 |
| 9 | [IDF officers ordered to fire at unarmed crowds near Gaza food distribution sites](https://news.ycombinator.com/item?id=44402896) | 报道称以军军官接令向加沙食品分发点附近无武装人群开火。 | 1455 | 1122 | 2025-06-28 |
| 10 | [Gemini CLI](https://news.ycombinator.com/item?id=44376919) | 谷歌推出命令行工具 Gemini CLI。 | 1428 | 788 | 2025-06-25 |
| 11 | [Honda conducts successful launch and landing of experimental reusable rocket](https://news.ycombinator.com/item?id=44300102) | 本田成功进行实验性可重复使用火箭的发射与着陆。 | 1355 | 422 | 2025-06-17 |
| 12 | [Frequent reauth doesn't make you more secure](https://news.ycombinator.com/item?id=44261777) | 作者认为频繁重新认证并不会让系统更安全。 | 1279 | 516 | 2025-06-12 |
| 13 | [A receipt printer cured my procrastination](https://news.ycombinator.com/item?id=44256499) | 作者分享用小票打印机改善拖延的经历。 | 1255 | 603 | 2025-06-12 |
| 14 | [U.S. bombs Iranian nuclear sites](https://news.ycombinator.com/item?id=44341639) | 美国轰炸伊朗核设施。 | 1247 | 3848 | 2025-06-22 |
| 15 | [Mechanical Watch: Exploded View](https://news.ycombinator.com/item?id=44347425) | 用分解视图展示机械手表结构。 | 1171 | 134 | 2025-06-22 |
| 16 | [OpenAI slams court order to save all ChatGPT logs, including deleted chats](https://news.ycombinator.com/item?id=44185913) | OpenAI 反对法院要求保留所有 ChatGPT 日志，包括已删除聊天。 | 1132 | 932 | 2025-06-04 |
| 17 | [The Grug Brained Developer (2022)](https://news.ycombinator.com/item?id=44303542) | 重读以穴居人口吻反思软件复杂性的开发指南。 | 1087 | 578 | 2025-06-17 |
| 18 | [YouTube's new anti-adblock measures](https://news.ycombinator.com/item?id=44329712) | 介绍 YouTube 新一轮反广告拦截措施。 | 991 | 1322 | 2025-06-20 |
| 19 | [More on Apple's Trust-Eroding 'F1 the Movie' Wallet Ad](https://news.ycombinator.com/item?id=44411069) | 作者批评苹果 Wallet 中《F1》电影广告侵蚀用户信任。 | 977 | 639 | 2025-06-29 |
| 20 | [The last six months in LLMs, illustrated by pelicans on bicycles](https://news.ycombinator.com/item?id=44215352) | 用骑自行车的鹈鹕图像展示半年间语言模型的变化。 | 962 | 234 | 2025-06-08 |

## 2025-07

有效主帖 25,546 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [LLM Inevitabilism](https://news.ycombinator.com/item?id=44567857) | 作者讨论认为大型语言模型发展不可避免的观念。 | 1773 | 1628 | 2025-07-15 |
| 2 | [Fast](https://news.ycombinator.com/item?id=44736967) | 以“快”为题，把速度本身作为关注对象。 | 1606 | 431 | 2025-07-30 |
| 3 | [The Fed says this is a cube of $1M. They're off by half a million](https://news.ycombinator.com/item?id=44435484) | 作者指出美联储展示的百万美元立方体与实际金额相差五十万美元。 | 1478 | 552 | 2025-07-01 |
| 4 | [Do not download the app, use the website](https://news.ycombinator.com/item?id=44689059) | 作者建议直接使用网站，避免下载应用。 | 1347 | 728 | 2025-07-25 |
| 5 | [Adding a feature because ChatGPT incorrectly thinks it exists](https://news.ycombinator.com/item?id=44491071) | 开发者因 ChatGPT 错误声称功能存在，索性将其实现。 | 1299 | 424 | 2025-07-07 |
| 6 | [Helsinki records zero traffic deaths for full year](https://news.ycombinator.com/item?id=44736025) | 赫尔辛基连续一年没有发生交通死亡事故。 | 1163 | 652 | 2025-07-30 |
| 7 | [Study mode](https://news.ycombinator.com/item?id=44725764) | 介绍面向学习过程的“学习模式”。 | 1130 | 805 | 2025-07-29 |
| 8 | [Copyparty – Turn almost any device into a file server](https://news.ycombinator.com/item?id=44711519) | Copyparty 可将多种设备变成文件服务器。 | 1096 | 169 | 2025-07-28 |
| 9 | [CARA – High precision robot dog using rope](https://news.ycombinator.com/item?id=44661846) | CARA 利用绳索构建高精度机器狗。 | 1073 | 177 | 2025-07-23 |
| 10 | [Kiro: A new agentic IDE](https://news.ycombinator.com/item?id=44560662) | 介绍面向智能体开发的新 IDE Kiro。 | 1063 | 462 | 2025-07-14 |
| 11 | [MacPaint Art from the Mid-80s Still Looks Great Today](https://news.ycombinator.com/item?id=44540402) | 回看八十年代中期至今仍有魅力的 MacPaint 作品。 | 1057 | 196 | 2025-07-12 |
| 12 | [OpenAI’s Windsurf deal is off, and Windsurf’s CEO is going to Google](https://news.ycombinator.com/item?id=44536988) | OpenAI 收购 Windsurf 的交易告吹，其 CEO 将加入谷歌。 | 1055 | 685 | 2025-07-11 |
| 13 | [EU age verification app to ban any Android system not licensed by Google](https://news.ycombinator.com/item?id=44705240) | 欧盟年龄验证应用被指将排除未经谷歌授权的 Android 系统。 | 1051 | 690 | 2025-07-27 |
| 14 | [Bypassing Google's big anti-adblock update](https://news.ycombinator.com/item?id=44544266) | 介绍绕过谷歌大规模反广告拦截更新的方法。 | 1044 | 919 | 2025-07-12 |
| 15 | [Show HN: Tinder but it's only pictures of my wife and I can only swipe right](https://news.ycombinator.com/item?id=44664873) | 开发者制作只展示妻子照片、且只能右滑的 Tinder 式应用。 | 1030 | 263 | 2025-07-23 |
| 16 | [Linux Reaches 5% Desktop Market Share in USA](https://news.ycombinator.com/item?id=44580682) | Linux 在美国桌面系统市场的份额达到 5%。 | 1021 | 614 | 2025-07-16 |
| 17 | [Dumb Pipe](https://news.ycombinator.com/item?id=44701555) | 以“纯粹管道”为名，介绍 Dumb Pipe 的构想。 | 1016 | 247 | 2025-07-27 |
| 18 | [‘I witnessed war crimes’ in Gaza – former worker at GHF aid site [video]](https://news.ycombinator.com/item?id=44714221) | 加沙 GHF 援助点前工作人员称自己目睹战争罪行。 | 1006 | 1278 | 2025-07-28 |
| 19 | [Bootstrapping a side project into a profitable seven-figure business](https://news.ycombinator.com/item?id=44495428) | 分享将副业自筹发展为盈利七位数业务的经历。 | 1001 | 257 | 2025-07-07 |
| 20 | [Nvidia won, we all lost](https://news.ycombinator.com/item?id=44468175) | 作者反思英伟达获胜给其他人带来的代价。 | 995 | 571 | 2025-07-04 |

## 2025-08

有效主帖 25,464 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Google will allow only apps from verified developers to be installed on Android](https://news.ycombinator.com/item?id=45017028) | 谷歌宣布 Android 将只允许安装来自已验证开发者的应用。 | 3050 | 2330 | 2025-08-25 |
| 2 | [Open models by OpenAI](https://news.ycombinator.com/item?id=44800746) | OpenAI 发布开放模型。 | 2124 | 876 | 2025-08-05 |
| 3 | [We should have the ability to run any code we want on hardware we own](https://news.ycombinator.com/item?id=45087396) | 作者主张人们应能在自有硬件上运行任意代码。 | 2071 | 1202 | 2025-08-31 |
| 4 | [GPT-5](https://news.ycombinator.com/item?id=44826997) | OpenAI 发布 GPT-5。 | 2063 | 2482 | 2025-08-07 |
| 5 | [AWS CEO says using AI to replace junior staff is 'Dumbest thing I've ever heard'](https://news.ycombinator.com/item?id=44972151) | AWS CEO 强烈反对用 AI 替代初级员工。 | 1697 | 744 | 2025-08-21 |
| 6 | [Cognitive load is what matters](https://news.ycombinator.com/item?id=45074248) | 作者强调软件中的认知负担问题。 | 1582 | 522 | 2025-08-30 |
| 7 | [Genie 3: A new frontier for world models](https://news.ycombinator.com/item?id=44798166) | Genie 3 推进世界模型的发展。 | 1510 | 490 | 2025-08-05 |
| 8 | [Fight Chat Control](https://news.ycombinator.com/item?id=44856426) | 呼吁反对 Chat Control。 | 1493 | 498 | 2025-08-10 |
| 9 | [GitHub is no longer independent at Microsoft after CEO resignation](https://news.ycombinator.com/item?id=44865560) | GitHub CEO 辞职后，公司不再以微软内部独立部门运营。 | 1468 | 1121 | 2025-08-11 |
| 10 | [I tried every todo app and ended up with a .txt file](https://news.ycombinator.com/item?id=44864134) | 作者尝试各种待办应用后，最终选择纯文本文件。 | 1402 | 799 | 2025-08-11 |
| 11 | [Ask HN: The government of my country blocked VPN access. What should I use?](https://news.ycombinator.com/item?id=45054260) | 印尼用户称政府封锁社交平台与 VPN，向社区询问替代连接方式。 | 1338 | 732 | 2025-08-28 |
| 12 | [Claude Sonnet 4 now supports 1M tokens of context](https://news.ycombinator.com/item?id=44878147) | Claude Sonnet 4 开始支持一百万词元上下文。 | 1324 | 692 | 2025-08-12 |
| 13 | [Perplexity is using stealth, undeclared crawlers to evade no-crawl directives](https://news.ycombinator.com/item?id=44785636) | Perplexity 被指使用未声明的隐蔽爬虫绕过禁止抓取指令。 | 1315 | 748 | 2025-08-04 |
| 14 | [uBlock Origin Lite now available for Safari](https://news.ycombinator.com/item?id=44795825) | uBlock Origin Lite 推出 Safari 版本。 | 1156 | 448 | 2025-08-05 |
| 15 | [Show HN: I spent 6 years building a ridiculous wooden pixel display](https://news.ycombinator.com/item?id=44787902) | 开发者耗时六年制作千像素木质显示器，邀请全球用户投票绘图。 | 1145 | 144 | 2025-08-04 |
| 16 | [I want everything local – Building my offline AI workspace](https://news.ycombinator.com/item?id=44840013) | 作者搭建完全本地、离线运行的 AI 工作空间。 | 1143 | 286 | 2025-08-08 |
| 17 | [Ultrathin business card runs a fluid simulation](https://news.ycombinator.com/item?id=44835879) | 一张超薄名片能够运行流体模拟。 | 1135 | 221 | 2025-08-08 |
| 18 | [Streaming services are driving viewers back to piracy](https://news.ycombinator.com/item?id=44902797) | 作者认为流媒体服务正把观众推回盗版。 | 1130 | 919 | 2025-08-14 |
| 19 | [Do the simplest thing that could possibly work](https://news.ycombinator.com/item?id=45068091) | 作者建议先做最简单且可能有效的实现。 | 1111 | 387 | 2025-08-29 |
| 20 | [Wikipedia loses challenge against Online Safety Act](https://news.ycombinator.com/item?id=44866208) | 维基百科挑战英国《在线安全法》的诉讼失败。 | 1109 | 856 | 2025-08-11 |

## 2025-09

有效主帖 25,387 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Slack has raised our charges by $195k per year](https://news.ycombinator.com/item?id=45283887) | 团队称 Slack 每年收费增加十九万五千美元。 | 3406 | 1470 | 2025-09-18 |
| 2 | [A WebGL game where you deliver messages on a tiny planet](https://news.ycombinator.com/item?id=45396441) | 一款在微型星球上递送消息的 WebGL 游戏。 | 2131 | 338 | 2025-09-27 |
| 3 | [Claude Sonnet 4.5](https://news.ycombinator.com/item?id=45415962) | Anthropic 发布 Claude Sonnet 4.5。 | 1585 | 786 | 2025-09-29 |
| 4 | [F-Droid and Google’s developer registration decree](https://news.ycombinator.com/item?id=45409794) | F-Droid 讨论谷歌开发者注册要求的影响。 | 1478 | 564 | 2025-09-29 |
| 5 | [Trump to impose $100k fee for H-1B worker visas, White House says](https://news.ycombinator.com/item?id=45305845) | 白宫称特朗普将对 H-1B 工作签证征收十万美元费用。 | 1476 | 1862 | 2025-09-19 |
| 6 | [Hosting a website on a disposable vape](https://news.ycombinator.com/item?id=45252817) | 作者把网站托管在一次性电子烟上。 | 1415 | 472 | 2025-09-15 |
| 7 | [Top UN legal investigators conclude Israel is guilty of genocide in Gaza](https://news.ycombinator.com/item?id=45259553) | 联合国法律调查人员认定以色列在加沙犯下种族灭绝罪。 | 1415 | 1446 | 2025-09-16 |
| 8 | [NPM debug and chalk packages compromised](https://news.ycombinator.com/item?id=45169657) | NPM 的 debug 与 chalk 软件包遭入侵。 | 1372 | 757 | 2025-09-08 |
| 9 | [Everything that's wrong with Google Search in one image](https://news.ycombinator.com/item?id=45366566) | 作者用一张图片概括对谷歌搜索的不满。 | 1291 | 723 | 2025-09-24 |
| 10 | [Yt-dlp: Upcoming new requirements for YouTube downloads](https://news.ycombinator.com/item?id=45358980) | yt-dlp 说明 YouTube 下载即将新增的要求。 | 1244 | 611 | 2025-09-24 |
| 11 | [Shai-Hulud malware attack: Tinycolor and over 40 NPM packages compromised](https://news.ycombinator.com/item?id=45260741) | Shai-Hulud 供应链攻击波及 Tinycolor 等四十余个 NPM 包。 | 1233 | 1019 | 2025-09-16 |
| 12 | [Apple Photos app corrupts images](https://news.ycombinator.com/item?id=45274277) | 苹果照片应用被指损坏图像。 | 1214 | 439 | 2025-09-17 |
| 13 | [I didn't bring my son to a museum to look at screens](https://news.ycombinator.com/item?id=45199931) | 家长反思带孩子参观博物馆却只能看屏幕的体验。 | 1185 | 392 | 2025-09-10 |
| 14 | [Show HN: A store that generates products from anything you type in search](https://news.ycombinator.com/item?id=45231378) | 一家可根据用户输入的搜索内容生成商品的商店。 | 1184 | 333 | 2025-09-13 |
| 15 | [You did this with an AI and you do not understand what you're doing here](https://news.ycombinator.com/item?id=45330378) | 作者质疑使用 AI 完成任务却不理解其过程的问题。 | 1178 | 542 | 2025-09-22 |
| 16 | [Always Invite Anna](https://news.ycombinator.com/item?id=45348495) | 作者以“总要邀请 Anna”为题，思考邀请他人的选择。 | 1154 | 178 | 2025-09-23 |
| 17 | [Germany is not supporting ChatControl – blocking minority secured](https://news.ycombinator.com/item?id=45209366) | 德国不支持 Chat Control，足以阻止提案的少数票形成。 | 1128 | 359 | 2025-09-11 |
| 18 | [Want to piss off your IT department? Are the links not malicious looking enough?](https://news.ycombinator.com/item?id=45295898) | 作者调侃看起来像恶意链接的网址会让 IT 部门头痛。 | 1127 | 320 | 2025-09-18 |
| 19 | [I ditched Docker for Podman](https://news.ycombinator.com/item?id=45137525) | 作者分享从 Docker 转向 Podman 的经历。 | 1123 | 654 | 2025-09-05 |
| 20 | [30 minutes with a stranger](https://news.ycombinator.com/item?id=45124003) | 记录与陌生人相处三十分钟的体验。 | 1103 | 375 | 2025-09-04 |

## 2025-10

有效主帖 26,672 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Keep Android Open](https://news.ycombinator.com/item?id=45742488) | 呼吁保持 Android 的开放性。 | 2693 | 889 | 2025-10-29 |
| 2 | [AWS multiple services outage in us-east-1](https://news.ycombinator.com/item?id=45640838) | AWS 美国东一区多项服务发生故障。 | 2246 | 2057 | 2025-10-20 |
| 3 | [Uv is the best thing to happen to the Python ecosystem in a decade](https://news.ycombinator.com/item?id=45751400) | 作者高度评价 uv 对 Python 生态的贡献。 | 2214 | 1324 | 2025-10-29 |
| 4 | [Fire destroys S. Korean government's cloud storage system, no backups available](https://news.ycombinator.com/item?id=45483386) | 火灾摧毁韩国政府云存储系统，报道称没有可用备份。 | 2080 | 933 | 2025-10-05 |
| 5 | [Space Elevator](https://news.ycombinator.com/item?id=45640226) | 认识试图连接地面与太空的电梯构想。 | 1802 | 403 | 2025-10-20 |
| 6 | [How I bypassed Amazon's Kindle web DRM](https://news.ycombinator.com/item?id=45610226) | 作者讲述绕过亚马逊 Kindle 网页 DRM 的过程。 | 1758 | 513 | 2025-10-16 |
| 7 | [10M people watched a YouTuber shim a lock; the lock company sued him – bad idea](https://news.ycombinator.com/item?id=45720376) | 视频作者展示绕开锁具的方法获千万观看，随后遭锁厂起诉。 | 1587 | 632 | 2025-10-27 |
| 8 | [FSF announces Librephone project](https://news.ycombinator.com/item?id=45586339) | 自由软件基金会宣布 Librephone 项目。 | 1586 | 631 | 2025-10-14 |
| 9 | [NanoChat – The best ChatGPT that $100 can buy](https://news.ycombinator.com/item?id=45569350) | NanoChat 尝试以一百美元预算打造 ChatGPT 式系统。 | 1523 | 308 | 2025-10-13 |
| 10 | [What we talk about when we talk about sideloading](https://news.ycombinator.com/item?id=45736479) | 厘清人们谈论应用侧载时实际指的是什么。 | 1516 | 629 | 2025-10-28 |
| 11 | [Google flags Immich sites as dangerous](https://news.ycombinator.com/item?id=45675015) | 谷歌将 Immich 站点标记为危险网站。 | 1464 | 688 | 2025-10-22 |
| 12 | [Scripts I wrote that I use all the time](https://news.ycombinator.com/item?id=45670052) | 作者分享自己日常反复使用的脚本。 | 1341 | 389 | 2025-10-22 |
| 13 | [Qualcomm to acquire Arduino](https://news.ycombinator.com/item?id=45502541) | 高通宣布收购 Arduino。 | 1340 | 535 | 2025-10-07 |
| 14 | [A competitor crippled a $23.5M bootcamp by becoming a Reddit moderator](https://news.ycombinator.com/item?id=45521920) | 报道称竞争对手通过担任 Reddit 版主打击一家编程培训机构。 | 1305 | 931 | 2025-10-08 |
| 15 | [Jane Goodall has died](https://news.ycombinator.com/item?id=45441069) | 灵长类动物学家 Jane Goodall 去世。 | 1302 | 185 | 2025-10-01 |
| 16 | [It's insulting to read AI-generated blog posts](https://news.ycombinator.com/item?id=45722069) | 作者认为阅读 AI 生成博客文章令人受到冒犯。 | 1300 | 540 | 2025-10-27 |
| 17 | [Apple M5 chip](https://news.ycombinator.com/item?id=45591799) | 苹果发布 M5 芯片。 | 1263 | 1395 | 2025-10-15 |
| 18 | [Affinity Studio now free](https://news.ycombinator.com/item?id=45761445) | Affinity Studio 宣布免费提供。 | 1217 | 793 | 2025-10-30 |
| 19 | [Andrej Karpathy – It will take a decade to work through the issues with agents](https://news.ycombinator.com/item?id=45619329) | Andrej Karpathy 认为解决智能体的问题还需要十年。 | 1212 | 1115 | 2025-10-17 |
| 20 | [How Israeli actions caused famine in Gaza, visualized](https://news.ycombinator.com/item?id=45447699) | 用可视化说明以色列行动如何造成加沙饥荒。 | 1205 | 1364 | 2025-10-02 |

## 2025-11

有效主帖 25,317 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Steam Machine](https://news.ycombinator.com/item?id=45903404) | 介绍 Steam Machine。 | 2928 | 1514 | 2025-11-12 |
| 2 | [Cloudflare Global Network experiencing issues](https://news.ycombinator.com/item?id=45963780) | Cloudflare 全球网络发生异常。 | 2432 | 1650 | 2025-11-18 |
| 3 | [Steam Frame](https://news.ycombinator.com/item?id=45903325) | 介绍 Steam Frame。 | 1915 | 698 | 2025-11-12 |
| 4 | [Our investigation into the suspicious pressure on Archive.today](https://news.ycombinator.com/item?id=45936460) | 调查 Archive.today 所遭遇的可疑压力。 | 1816 | 443 | 2025-11-15 |
| 5 | [Gemini 3](https://news.ycombinator.com/item?id=45967211) | 谷歌发布 Gemini 3。 | 1735 | 1056 | 2025-11-18 |
| 6 | [Cloudflare outage on November 18, 2025 post mortem](https://news.ycombinator.com/item?id=45973709) | Cloudflare 复盘 2025 年十一月十八日的服务故障。 | 1465 | 916 | 2025-11-18 |
| 7 | [AirPods libreated from Apple's ecosystem](https://news.ycombinator.com/item?id=45941596) | 探索让 AirPods 脱离苹果生态限制的方法。 | 1424 | 462 | 2025-11-16 |
| 8 | [AI World Clocks](https://news.ycombinator.com/item?id=45930151) | 九个 AI 模型每分钟重新绘制时钟，形成世界时钟实验。 | 1383 | 384 | 2025-11-14 |
| 9 | [Android developer verification: Early access starts](https://news.ycombinator.com/item?id=45908938) | Android 开发者验证开始提前体验。 | 1362 | 676 | 2025-11-13 |
| 10 | [I Am Mark Zuckerberg](https://news.ycombinator.com/item?id=45863360) | 作者以“我是 Mark Zuckerberg”为题讲述自己的故事。 | 1286 | 438 | 2025-11-09 |
| 11 | [Show HN: I built a synth for my daughter](https://news.ycombinator.com/item?id=45900425) | 开发者为女儿制作合成器。 | 1278 | 209 | 2025-11-12 |
| 12 | [I think nobody wants AI in Firefox, Mozilla](https://news.ycombinator.com/item?id=45926779) | 作者向 Mozilla 表达不希望 Firefox 集成人工智能的观点。 | 1275 | 754 | 2025-11-14 |
| 13 | [Nano Banana Pro](https://news.ycombinator.com/item?id=45993296) | 介绍 Nano Banana Pro。 | 1275 | 685 | 2025-11-20 |
| 14 | [Advent of Code 2025](https://news.ycombinator.com/item?id=46096337) | 关注 2025 年 Advent of Code 编程挑战。 | 1243 | 397 | 2025-11-30 |
| 15 | [Pebble Watch software is now open source](https://news.ycombinator.com/item?id=46037626) | Pebble 手表软件宣布开源。 | 1241 | 227 | 2025-11-24 |
| 16 | [Solarpunk is happening in Africa](https://news.ycombinator.com/item?id=45827190) | 作者观察非洲正在发生的太阳朋克式实践。 | 1201 | 591 | 2025-11-05 |
| 17 | [The 'Toy Story' You Remember](https://news.ycombinator.com/item?id=45883788) | 回顾人们记忆中的《玩具总动员》。 | 1196 | 338 | 2025-11-11 |
| 18 | [FFmpeg to Google: Fund us or stop sending bugs](https://news.ycombinator.com/item?id=45891016) | FFmpeg 要求谷歌提供资助，或停止不断提交缺陷。 | 1175 | 886 | 2025-11-11 |
| 19 | [Fran Sans – font inspired by San Francisco light rail displays](https://news.ycombinator.com/item?id=46025942) | Fran Sans 字体灵感来自旧金山轻轨显示屏。 | 1170 | 140 | 2025-11-23 |
| 20 | [Anthropic’s paper smells like bullshit](https://news.ycombinator.com/item?id=45944296) | 作者质疑 Anthropic 关于 AI 主导网络间谍行动的论文。 | 1160 | 322 | 2025-11-16 |

## 2025-12

有效主帖 27,484 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Gemini Pro 3 imagines the HN front page 10 years from now](https://news.ycombinator.com/item?id=46205632) | 开发者展示 Gemini 3 Pro 想象的十年后 HN 首页。 | 3346 | 965 | 2025-12-09 |
| 2 | [Size of Life](https://news.ycombinator.com/item?id=46219346) | 从大小与尺度的角度重新观察生命。 | 2619 | 277 | 2025-12-10 |
| 3 | [What an unprocessed photo looks like](https://news.ycombinator.com/item?id=46415225) | 展示未经处理的照片是什么样子。 | 2510 | 409 | 2025-12-28 |
| 4 | [Anthropic acquires Bun](https://news.ycombinator.com/item?id=46124267) | Anthropic 收购 Bun。 | 2192 | 1072 | 2025-12-02 |
| 5 | [Beginning January 2026, all ACM publications will be made open access](https://news.ycombinator.com/item?id=46313991) | ACM 宣布从 2026 年一月起全部出版物开放获取。 | 2031 | 239 | 2025-12-18 |
| 6 | [Backing up Spotify](https://news.ycombinator.com/item?id=46338339) | 探讨如何为 Spotify 内容建立备份。 | 1980 | 701 | 2025-12-20 |
| 7 | [Tell HN: Merry Christmas!](https://news.ycombinator.com/item?id=46380168) | HN 用户送上圣诞祝福，鼓励休息并关心无法与亲友团聚的人。 | 1958 | 429 | 2025-12-24 |
| 8 | [Netflix to Acquire Warner Bros](https://news.ycombinator.com/item?id=46160315) | Netflix 宣布收购华纳兄弟。 | 1755 | 1358 | 2025-12-05 |
| 9 | [Apple has locked my Apple ID, and I have no recourse. A plea for help](https://news.ycombinator.com/item?id=46252114) | 用户称 Apple ID 被锁且求助无门，公开寻求帮助。 | 1750 | 1049 | 2025-12-13 |
| 10 | [Inside CECOT – 60 Minutes [video]](https://news.ycombinator.com/item?id=46361024) | 观看《六十分钟》对 CECOT 监狱的报道。 | 1679 | 549 | 2025-12-23 |
| 11 | [Show HN: Jmail – Google Suite for Epstein files](https://news.ycombinator.com/item?id=46339600) | Jmail 用类似谷歌办公套件的界面展示爱泼斯坦相关文件。 | 1557 | 363 | 2025-12-20 |
| 12 | [Rob Pike Goes Nuclear over GenAI](https://news.ycombinator.com/item?id=46392115) | Rob Pike 对生成式人工智能表达强烈批评。 | 1550 | 1797 | 2025-12-26 |
| 13 | [Fabrice Bellard Releases MicroQuickJS](https://news.ycombinator.com/item?id=46367224) | Fabrice Bellard 发布 MicroQuickJS。 | 1507 | 569 | 2025-12-23 |
| 14 | [Hacker News front page now, but the titles are honest](https://news.ycombinator.com/item?id=46326588) | 一个用更直白标题重写当前 HN 首页的项目。 | 1384 | 321 | 2025-12-19 |
| 15 | [Ghostty is now non-profit](https://news.ycombinator.com/item?id=46138238) | Ghostty 转为非营利项目。 | 1343 | 289 | 2025-12-03 |
| 16 | [How uv got so fast](https://news.ycombinator.com/item?id=46393992) | 分析 Python 工具 uv 为何运行如此迅速。 | 1290 | 459 | 2025-12-26 |
| 17 | [Texas is suing all of the big TV makers for spying on what you watch](https://news.ycombinator.com/item?id=46294456) | 得州起诉主要电视制造商，指控其窥探用户观看内容。 | 1268 | 642 | 2025-12-16 |
| 18 | [GPT-5.2](https://news.ycombinator.com/item?id=46234788) | OpenAI 发布 GPT-5.2。 | 1195 | 1083 | 2025-12-11 |
| 19 | [Kidnapped by Deutsche Bahn](https://news.ycombinator.com/item?id=46419970) | 作者用“被德国铁路绑架”形容自己的乘车遭遇。 | 1187 | 1031 | 2025-12-29 |
| 20 | [We invited a man into our home at Christmas and he stayed with us for 45 years](https://news.ycombinator.com/item?id=46383552) | 一个圣诞节获邀进门的男子，与邀请者共同生活了四十五年。 | 1178 | 282 | 2025-12-25 |

## 2026-01

有效主帖 31,863 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [The struggle of resizing windows on macOS Tahoe](https://news.ycombinator.com/item?id=46579864) | 作者分享在 macOS Tahoe 调整窗口大小的困难。 | 2752 | 1207 | 2026-01-11 |
| 2 | [Bose is open-sourcing its old smart speakers instead of bricking them](https://news.ycombinator.com/item?id=46541892) | Bose 选择开源旧智能音箱，而非让设备停用。 | 2532 | 396 | 2026-01-08 |
| 3 | [It's hard to justify Tahoe icons](https://news.ycombinator.com/item?id=46497712) | 作者质疑 macOS Tahoe 图标设计的合理性。 | 2487 | 951 | 2026-01-05 |
| 4 | [Microsoft forced me to switch to Linux](https://news.ycombinator.com/item?id=46795864) | 作者讲述微软的做法如何促使自己转用 Linux。 | 1871 | 1503 | 2026-01-28 |
| 5 | [Antirender: remove the glossy shine on architectural renderings](https://news.ycombinator.com/item?id=46829147) | Antirender 去除建筑效果图中光鲜亮丽的修饰。 | 1844 | 453 | 2026-01-30 |
| 6 | [Loud noises heard in Venezuela capital, southern area without electricity](https://news.ycombinator.com/item?id=46473348) | 委内瑞拉首都传出巨响，南部地区停电。 | 1771 | 4689 | 2026-01-03 |
| 7 | [Lessons from 14 Years at Google](https://news.ycombinator.com/item?id=46488819) | 作者总结在谷歌工作十四年的经验。 | 1678 | 687 | 2026-01-04 |
| 8 | [Moltbook](https://news.ycombinator.com/item?id=46820360) | 介绍 Moltbook。 | 1652 | 5 | 2026-01-30 |
| 9 | [Vienam Bans Unskippable Ads, Requires Skip Button to Appear After 5 Seconds](https://news.ycombinator.com/item?id=46514677) | 越南禁止不可跳过广告，要求五秒后出现跳过按钮。 | 1580 | 813 | 2026-01-06 |
| 10 | [Total monthly number of StackOverflow questions over time](https://news.ycombinator.com/item?id=46482345) | 用时间序列展示 Stack Overflow 每月提问总量的变化。 | 1550 | 999 | 2026-01-03 |
| 11 | [TikTok users can't upload anti-ICE videos. The company blames tech issues](https://news.ycombinator.com/item?id=46779809) | TikTok 用户无法上传反 ICE 视频，公司称系技术问题。 | 1495 | 1003 | 2026-01-27 |
| 12 | [ICE Using Palantir Tool That Feeds on Medicaid Data](https://news.ycombinator.com/item?id=46756117) | 报道称 ICE 使用可读取 Medicaid 数据的 Palantir 工具。 | 1475 | 969 | 2026-01-25 |
| 13 | [Creators of Tailwind laid off 75% of their engineering team](https://news.ycombinator.com/item?id=46527950) | Tailwind 团队裁撤四分之三工程人员。 | 1457 | 840 | 2026-01-07 |
| 14 | [ASCII characters are not pixels: a deep dive into ASCII rendering](https://news.ycombinator.com/item?id=46657122) | 深入解释 ASCII 渲染为何不能简单把字符当成像素。 | 1353 | 149 | 2026-01-17 |
| 15 | [Show HN: isometric.nyc – giant isometric pixel art map of NYC](https://news.ycombinator.com/item?id=46721802) | isometric.nyc 展示巨大的纽约等距像素艺术地图。 | 1325 | 241 | 2026-01-22 |
| 16 | [Cowork: Claude Code for the rest of your work](https://news.ycombinator.com/item?id=46593022) | Cowork 将 Claude Code 式协作扩展到其他工作。 | 1298 | 565 | 2026-01-12 |
| 17 | [Don't fall into the anti-AI hype](https://news.ycombinator.com/item?id=46574276) | 作者提醒不要陷入过度反对 AI 的情绪。 | 1296 | 1631 | 2026-01-11 |
| 18 | [enclose.horse](https://news.ycombinator.com/item?id=46509211) | 介绍 enclose.horse 项目。 | 1217 | 233 | 2026-01-06 |
| 19 | [Linux is good now; to feel like you actually own your PC, put Linux on it](https://news.ycombinator.com/item?id=46457770) | 作者建议安装 Linux，找回拥有个人电脑的感觉。 | 1194 | 1000 | 2026-01-01 |
| 20 | [Eat Real Food – Introducing the New Pyramid](https://news.ycombinator.com/item?id=46529237) | 介绍强调吃真正食物的新饮食金字塔。 | 1163 | 1638 | 2026-01-07 |

## 2026-02

有效主帖 32,760 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Statement from Dario Amodei on Our Discussions with the Department of War](https://news.ycombinator.com/item?id=47173121) | Dario Amodei 就 Anthropic 与美国战争部的讨论发表声明。 | 2920 | 1579 | 2026-02-26 |
| 2 | [We Will Not Be Divided](https://news.ycombinator.com/item?id=47188473) | 以“我们不会被分裂”为共同立场发表声明。 | 2645 | 841 | 2026-02-28 |
| 3 | [Claude Opus 4.6](https://news.ycombinator.com/item?id=46902223) | Anthropic 发布 Claude Opus 4.6。 | 2346 | 1031 | 2026-02-05 |
| 4 | [An AI Agent Published a Hit Piece on Me](https://news.ycombinator.com/item?id=46990729) | 作者称一个 AI 智能体发表了针对自己的攻击文章。 | 2346 | 951 | 2026-02-12 |
| 5 | [F-Droid: "Keep Android Open"](https://news.ycombinator.com/item?id=47091419) | F-Droid 呼吁保持 Android 开放。 | 2258 | 737 | 2026-02-20 |
| 6 | [IDF Killed Gaza Aid Workers at Point Blank Range in 2025 Massacre: Report](https://news.ycombinator.com/item?id=47136179) | 一份报告称以军在 2025 年加沙事件中近距离杀害援助人员。 | 2084 | 997 | 2026-02-24 |
| 7 | [Discord will require a face scan or ID for full access next month](https://news.ycombinator.com/item?id=46945663) | Discord 宣布下月起完整访问需通过面部扫描或身份证明。 | 2046 | 2041 | 2026-02-09 |
| 8 | [OpenAI – How to delete your account](https://news.ycombinator.com/item?id=47193478) | 介绍删除 OpenAI 账号的方法。 | 1929 | 362 | 2026-02-28 |
| 9 | [The Age Verification Trap, Verifying age undermines everyone's data protection](https://news.ycombinator.com/item?id=47122715) | 作者认为年龄验证会损害所有人的数据保护。 | 1670 | 1301 | 2026-02-23 |
| 10 | [Apple, fix my keyboard before the timer ends or I'm leaving iPhone](https://news.ycombinator.com/item?id=47003064) | 用户要求苹果在期限内修复键盘，否则将放弃 iPhone。 | 1627 | 793 | 2026-02-13 |
| 11 | [I built Timeframe, our family e-paper dashboard](https://news.ycombinator.com/item?id=47113728) | 作者为家庭打造电子纸信息面板 Timeframe。 | 1616 | 369 | 2026-02-22 |
| 12 | [GPT-5.3-Codex](https://news.ycombinator.com/item?id=46902638) | OpenAI 发布 GPT-5.3-Codex。 | 1530 | 605 | 2026-02-05 |
| 13 | [Trump's global tariffs struck down by US Supreme Court](https://news.ycombinator.com/item?id=47089213) | 美国最高法院推翻特朗普的全球关税措施。 | 1527 | 1291 | 2026-02-20 |
| 14 | [I want to wash my car. The car wash is 50 meters away. Should I walk or drive?](https://news.ycombinator.com/item?id=47031580) | 用去五十米外洗车店该步行还是开车的问题测试推理。 | 1516 | 949 | 2026-02-16 |
| 15 | [Facebook is absolutely cooked](https://news.ycombinator.com/item?id=47091748) | 作者强烈批评 Facebook 的现状。 | 1513 | 847 | 2026-02-20 |
| 16 | [I Verified My LinkedIn Identity. Here's What I Handed Over](https://news.ycombinator.com/item?id=47098245) | 作者记录 LinkedIn 身份验证过程中交出的个人信息。 | 1483 | 490 | 2026-02-21 |
| 17 | [OpenClaw, OpenAI and the Future](https://news.ycombinator.com/item?id=47028013) | 关注 OpenClaw 与 OpenAI 的关系及未来方向。 | 1449 | 1131 | 2026-02-15 |
| 18 | [OpenAI Executes Agreement with Dept of War for Classified Environment Deployment](https://news.ycombinator.com/item?id=47189650) | OpenAI 与美国战争部签署涉密环境部署协议。 | 1407 | 648 | 2026-02-28 |
| 19 | [The Singularity will occur on a Tuesday](https://news.ycombinator.com/item?id=46962996) | 以“奇点将在星期二到来”的设想讨论技术未来。 | 1381 | 756 | 2026-02-10 |
| 20 | [I am directing the Department of War to designate Anthropic a Supply-Chain Risk](https://news.ycombinator.com/item?id=47186677) | 美国战争部长宣布将 Anthropic 列为供应链风险。 | 1362 | 1085 | 2026-02-27 |

## 2026-03

有效主帖 34,607 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Don't post generated/AI-edited comments. HN is for conversation between humans.](https://news.ycombinator.com/item?id=47340079) | HN 要求用户不要发布生成或经 AI 编辑的评论，以维护人与人的对话。 | 4229 | 1668 | 2026-03-11 |
| 2 | [Motorola announces a partnership with GrapheneOS Foundation](https://news.ycombinator.com/item?id=47214645) | 摩托罗拉宣布与 GrapheneOS 基金会合作。 | 2358 | 884 | 2026-03-02 |
| 3 | [Claude Code's source code has been leaked via a map file in their NPM registry](https://news.ycombinator.com/item?id=47584540) | Claude Code 源代码经 NPM 软件包中的映射文件泄漏。 | 2095 | 1022 | 2026-03-31 |
| 4 | [Turing Award winner and former Oxford professor Tony Hoare passed away](https://news.ycombinator.com/item?id=47324054) | 图灵奖得主、牛津大学前教授 Tony Hoare 去世。 | 2043 | 268 | 2026-03-10 |
| 5 | [Apple Introduces MacBook Neo](https://news.ycombinator.com/item?id=47247645) | 苹果推出 MacBook Neo。 | 1974 | 2320 | 2026-03-04 |
| 6 | [Microgpt](https://news.ycombinator.com/item?id=47202708) | 介绍 Microgpt 项目。 | 1936 | 324 | 2026-03-01 |
| 7 | [Axios Compromised on NPM – Malicious Versions Drop Remote Access Trojan](https://news.ycombinator.com/item?id=47582220) | Axios 的 NPM 包遭入侵，恶意版本投放远程控制木马。 | 1934 | 807 | 2026-03-31 |
| 8 | [Polymarket gamblers threaten to kill me over Iran missile story](https://news.ycombinator.com/item?id=47397822) | 记者称 Polymarket 赌客因一篇伊朗导弹报道向自己发出死亡威胁。 | 1606 | 1055 | 2026-03-16 |
| 9 | [Copilot edited an ad into my PR](https://news.ycombinator.com/item?id=47570269) | 开发者称 Copilot 在自己的拉取请求中加入广告。 | 1606 | 643 | 2026-03-30 |
| 10 | [Shall I implement it? No](https://news.ycombinator.com/item?id=47357042) | 面对“要我实现它吗”的询问，作者给出了否定回答。 | 1563 | 564 | 2026-03-12 |
| 11 | [Can I Run AI locally?](https://news.ycombinator.com/item?id=47363754) | 探讨自己的设备能否在本地运行 AI。 | 1520 | 353 | 2026-03-13 |
| 12 | [Astral to Join OpenAI](https://news.ycombinator.com/item?id=47438723) | Astral 宣布加入 OpenAI。 | 1489 | 901 | 2026-03-19 |
| 13 | [Kagi Translate now supports LinkedIn Speak as an output language](https://news.ycombinator.com/item?id=47408703) | Kagi 翻译新增模仿 LinkedIn 职场腔调的输出选项。 | 1469 | 345 | 2026-03-17 |
| 14 | [The EU still wants to scan  your private messages and photos](https://news.ycombinator.com/item?id=47522709) | 作者警告欧盟仍希望扫描私人消息与照片。 | 1450 | 393 | 2026-03-25 |
| 15 | [The workers behind Meta's smart glasses can see everything](https://news.ycombinator.com/item?id=47225130) | 报道称 Meta 智能眼镜背后的工作人员能看到用户拍摄内容。 | 1448 | 809 | 2026-03-02 |
| 16 | [Malus – Clean Room as a Service](https://news.ycombinator.com/item?id=47350424) | Malus 提供洁净室式重实现服务。 | 1433 | 531 | 2026-03-12 |
| 17 | [Founder of GitLab battles cancer by founding companies](https://news.ycombinator.com/item?id=47556729) | GitLab 创始人通过创办公司应对癌症。 | 1404 | 255 | 2026-03-28 |
| 18 | [The Claude Code Source Leak: fake tools, frustration regexes, undercover mode](https://news.ycombinator.com/item?id=47586778) | 分析 Claude Code 泄漏代码中的假工具、情绪匹配与隐蔽模式。 | 1376 | 578 | 2026-03-31 |
| 19 | [I traced $2B in grants and 45 states' lobbying behind age‑verification bills](https://news.ycombinator.com/item?id=47362528) | 作者追踪二十亿美元拨款及四十五州年龄验证法案背后的游说。 | 1358 | 1051 | 2026-03-13 |
| 20 | [The Xkcd thing, now interactive](https://news.ycombinator.com/item?id=47230704) | 将一项 xkcd 创意制作成交互版本。 | 1320 | 158 | 2026-03-03 |

## 2026-04

有效主帖 29,984 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ghostty is leaving GitHub](https://news.ycombinator.com/item?id=47939579) | Ghostty 宣布离开 GitHub。 | 3521 | 1051 | 2026-04-28 |
| 2 | [The Git Commands I Run Before Reading Any Code](https://news.ycombinator.com/item?id=47687273) | 作者分享阅读项目代码前会执行的 Git 命令。 | 2338 | 509 | 2026-04-08 |
| 3 | [Alberta Startup Sells No-Tech Tractors for Half Price](https://news.ycombinator.com/item?id=47865868) | 阿尔伯塔一家初创企业以半价出售低技术依赖拖拉机。 | 2320 | 779 | 2026-04-22 |
| 4 | [Sam Altman May Control Our Future – Can He Be Trusted?](https://news.ycombinator.com/item?id=47659135) | 作者追问可能影响人类未来的 Sam Altman 是否值得信任。 | 2202 | 916 | 2026-04-06 |
| 5 | [Tim Cook to become Apple Executive Chairman](https://news.ycombinator.com/item?id=47840219) | Tim Cook 将出任苹果执行董事长。 | 2177 | 1331 | 2026-04-20 |
| 6 | [Zed is 1.0](https://news.ycombinator.com/item?id=47949027) | 代码编辑器 Zed 发布 1.0 版。 | 2153 | 690 | 2026-04-29 |
| 7 | [DeepSeek v4](https://news.ycombinator.com/item?id=47884971) | 介绍 DeepSeek v4。 | 2091 | 1607 | 2026-04-24 |
| 8 | [Claude Opus 4.7](https://news.ycombinator.com/item?id=47793411) | Anthropic 发布 Claude Opus 4.7。 | 1959 | 1452 | 2026-04-16 |
| 9 | [I Ported Mac OS X to the Nintendo Wii](https://news.ycombinator.com/item?id=47691730) | 开发者将 Mac OS X 移植到任天堂 Wii。 | 1924 | 328 | 2026-04-08 |
| 10 | [LinkedIn Is Illegally Searching Your Computer](https://news.ycombinator.com/item?id=47613981) | 作者指控 LinkedIn 非法扫描用户电脑。 | 1897 | 770 | 2026-04-02 |
| 11 | [Google releases Gemma 4 open models](https://news.ycombinator.com/item?id=47616361) | 谷歌发布 Gemma 4 开放模型。 | 1812 | 474 | 2026-04-02 |
| 12 | [Google Broke Its Promise to Me. Now ICE Has My Data](https://news.ycombinator.com/item?id=47782570) | 作者称谷歌违背承诺，导致 ICE 取得自己的数据。 | 1711 | 765 | 2026-04-15 |
| 13 | [Phone is about to stop being yours](https://news.ycombinator.com/item?id=47935853) | 作者担忧手机用户即将失去对设备的控制。 | 1702 | 889 | 2026-04-28 |
| 14 | [Introducing GPT-5.5](https://news.ycombinator.com/item?id=47879092) | OpenAI 推出 GPT-5.5。 | 1580 | 1056 | 2026-04-23 |
| 15 | [Project Glasswing: Securing critical software for the AI era](https://news.ycombinator.com/item?id=47679121) | Glasswing 项目探索 AI 时代关键软件的安全防护。 | 1541 | 836 | 2026-04-07 |
| 16 | [Copy Fail – CVE-2026-31431](https://news.ycombinator.com/item?id=47952181) | 介绍 Copy Fail 漏洞 CVE-2026-31431。 | 1491 | 516 | 2026-04-29 |
| 17 | [Framework Laptop 13 Pro](https://news.ycombinator.com/item?id=47852177) | Framework 推出 Laptop 13 Pro。 | 1479 | 769 | 2026-04-21 |
| 18 | [All phones sold in the EU to have replaceable batteries from 2027](https://news.ycombinator.com/item?id=47834195) | 欧盟将要求 2027 年起销售的手机使用可更换电池。 | 1446 | 1268 | 2026-04-20 |
| 19 | [EFF is leaving X](https://news.ycombinator.com/item?id=47706268) | 电子前沿基金会宣布离开 X。 | 1427 | 1316 | 2026-04-09 |
| 20 | [Filing the Corners Off MacBooks](https://news.ycombinator.com/item?id=47724352) | 作者尝试磨掉 MacBook 的边角。 | 1406 | 678 | 2026-04-10 |

## 2026-05

有效主帖 28,978 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Hardware Attestation as Monopoly Enabler](https://news.ycombinator.com/item?id=48086190) | 作者分析硬件证明机制如何助长垄断。 | 2186 | 755 | 2026-05-10 |
| 2 | [Mitchellh – I strongly believe there are entire companies now under AI psychosis](https://news.ycombinator.com/item?id=48153379) | Mitchell Hashimoto 认为已有整家公司陷入对 AI 的失常迷信。 | 2105 | 1272 | 2026-05-15 |
| 3 | [I'm Tired of Talking to AI](https://news.ycombinator.com/item?id=48292224) | 作者表达对不断与 AI 交流的疲惫。 | 2013 | 950 | 2026-05-27 |
| 4 | [Local AI needs to be the norm](https://news.ycombinator.com/item?id=48085821) | 作者主张本地运行 AI 应成为常态。 | 1903 | 749 | 2026-05-10 |
| 5 | [Claude Opus 4.8](https://news.ycombinator.com/item?id=48311647) | Anthropic 发布 Claude Opus 4.8。 | 1774 | 1376 | 2026-05-28 |
| 6 | [Google Chrome silently installs a 4 GB AI model on your device without consent](https://news.ycombinator.com/item?id=48019219) | Chrome 被指未经同意静默安装四 GB 的 AI 模型。 | 1755 | 1143 | 2026-05-05 |
| 7 | [Valve releases Steam Controller CAD files under Creative Commons license](https://news.ycombinator.com/item?id=48037555) | Valve 以知识共享许可发布 Steam Controller 的 CAD 文件。 | 1747 | 593 | 2026-05-06 |
| 8 | [Rumors of my death are slightly exaggerated](https://news.ycombinator.com/item?id=48037336) | 一位作者澄清自己仍健在，指出 AI 书评捏造了其死讯。 | 1676 | 257 | 2026-05-06 |
| 9 | [Magnifica Humanitas (Encyclical Letter)](https://news.ycombinator.com/item?id=48265206) | 阅读题为《Magnifica Humanitas》的通谕。 | 1650 | 965 | 2026-05-25 |
| 10 | [Appearing Productive in the Workplace](https://news.ycombinator.com/item?id=48038001) | 探讨如何在职场上表现得富有成效。 | 1634 | 652 | 2026-05-06 |
| 11 | [Google Broke reCAPTCHA for De-Googled Android Users](https://news.ycombinator.com/item?id=48067119) | 谷歌 reCAPTCHA 被指使去谷歌化 Android 用户无法正常验证。 | 1561 | 591 | 2026-05-08 |
| 12 | [Talking to 35 Strangers at the Gym](https://news.ycombinator.com/item?id=48007438) | 作者分享在健身房与三十五名陌生人交谈的经历。 | 1550 | 753 | 2026-05-04 |
| 13 | [VS Code inserting 'Co-Authored-by Copilot' into commits regardless of usage](https://news.ycombinator.com/item?id=47989883) | VS Code 被指不论是否使用 Copilot，都在提交中加入共同作者署名。 | 1513 | 850 | 2026-05-02 |
| 14 | [I’ve joined Anthropic](https://news.ycombinator.com/item?id=48194352) | 作者宣布加入 Anthropic。 | 1431 | 618 | 2026-05-19 |
| 15 | [An OpenAI model has disproved a central conjecture in discrete geometry](https://news.ycombinator.com/item?id=48212493) | 报道称 OpenAI 模型推翻了离散几何中的一项核心猜想。 | 1429 | 1055 | 2026-05-20 |
| 16 | [Can we have the day off?](https://news.ycombinator.com/item?id=48302745) | 以“我们能放假一天吗”为提问，表达暂停工作的愿望。 | 1415 | 776 | 2026-05-28 |
| 17 | [Bambu Lab is abusing the open source social contract](https://news.ycombinator.com/item?id=48109224) | 作者指责 Bambu Lab 滥用开源社区的社会契约。 | 1404 | 428 | 2026-05-12 |
| 18 | [Bricks and Minifigs Stole a Man's $200k Lego Collection](https://news.ycombinator.com/item?id=48314136) | 一名男子指控 Bricks and Minifigs 窃取其二十万美元乐高收藏。 | 1394 | 624 | 2026-05-28 |
| 19 | [The Dead Economy Theory](https://news.ycombinator.com/item?id=48324712) | 了解以“死亡经济”命名的理论观点。 | 1359 | 1424 | 2026-05-29 |
| 20 | [Building for the Future](https://news.ycombinator.com/item?id=48054423) | 以未来为目标，讨论今天的建设选择。 | 1356 | 998 | 2026-05-07 |

## 2026-06

有效主帖 30,102 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [US Government directive to suspend access to Fable 5 and Mythos 5](https://news.ycombinator.com/item?id=48511072) | 美国政府下令暂停访问 Fable 5 与 Mythos 5。 | 3158 | 2314 | 2026-06-13 |
| 2 | [Claude Fable 5](https://news.ycombinator.com/item?id=48463808) | 介绍 Claude Fable 5 模型。 | 2626 | 2159 | 2026-06-09 |
| 3 | [Claude Code Is Steganographically Marking Requests](https://news.ycombinator.com/item?id=48734373) | 研究指出 Claude Code 会通过隐写方式标记请求。 | 2445 | 750 | 2026-06-30 |
| 4 | [The newest Instagram "exploit" is the goofiest I've seen](https://news.ycombinator.com/item?id=48359102) | 作者分析一个被其称为十分滑稽的 Instagram 新漏洞。 | 2210 | 491 | 2026-06-01 |
| 5 | [Steam Machine](https://news.ycombinator.com/item?id=48632884) | 介绍 Steam Machine。 | 1922 | 1736 | 2026-06-22 |
| 6 | [If you are asking for human attention, demonstrate human effort](https://news.ycombinator.com/item?id=48497609) | 作者主张索取他人注意力时应先展示自己付出的努力。 | 1753 | 503 | 2026-06-11 |
| 7 | [A Herculaneum scroll has been read for the first time](https://news.ycombinator.com/item?id=48675179) | 一卷赫库兰尼姆古卷首次被成功阅读。 | 1714 | 369 | 2026-06-25 |
| 8 | [A backdoor in a LinkedIn job offer](https://news.ycombinator.com/item?id=48546294) | 研究者发现一份 LinkedIn 工作邀请中藏有后门。 | 1614 | 304 | 2026-06-15 |
| 9 | [Open Source AI Must Win](https://news.ycombinator.com/item?id=48511908) | 作者呼吁让开源 AI 取得胜利。 | 1603 | 482 | 2026-06-13 |
| 10 | [Running local models is good now](https://news.ycombinator.com/item?id=48555993) | 作者分享如今本地运行模型已相当好用的体验。 | 1596 | 608 | 2026-06-16 |
| 11 | ["They're made out of weights"](https://news.ycombinator.com/item?id=48391611) | 用“它们是由权重构成的”这句话呈现对 AI 的观察。 | 1529 | 711 | 2026-06-03 |
| 12 | [S&P 500 rejects SpaceX, also blocking entry for OpenAI and Anthropic](https://news.ycombinator.com/item?id=48421442) | 标普五百拒纳 SpaceX，也阻挡了 OpenAI 与 Anthropic 的进入。 | 1484 | 502 | 2026-06-06 |
| 13 | [Homebrew 6.0.0](https://news.ycombinator.com/item?id=48490024) | Homebrew 发布 6.0.0 版。 | 1481 | 363 | 2026-06-11 |
| 14 | [AI Agent Bankrupted Their Operator While Trying to Scan DN42](https://news.ycombinator.com/item?id=48500012) | AI 智能体试图扫描 DN42 时耗尽运营者资金。 | 1467 | 536 | 2026-06-12 |
| 15 | [Iroh 1.0](https://news.ycombinator.com/item?id=48542480) | Iroh 发布 1.0 版。 | 1398 | 462 | 2026-06-15 |
| 16 | [Midjourney Medical](https://news.ycombinator.com/item?id=48579650) | 介绍 Midjourney Medical。 | 1377 | 878 | 2026-06-18 |
| 17 | [Om Malik, 1966-2026](https://news.ycombinator.com/item?id=48678852) | 缅怀生于 1966 年、卒于 2026 年的 Om Malik。 | 1353 | 171 | 2026-06-25 |
| 18 | [Ask HN: Has anyone replaced Claude/GPT with a local model for daily coding?](https://news.ycombinator.com/item?id=48542100) | 征询是否有人已用本地模型完全替代 Claude 或 GPT 进行日常编程。 | 1318 | 563 | 2026-06-15 |
| 19 | [Building an HTML-first site doubled our users overnight](https://news.ycombinator.com/item?id=48475483) | 团队称改建为 HTML 优先网站后，用户数一夜翻倍。 | 1278 | 569 | 2026-06-10 |
| 20 | [Epic Games announces Lore version control system](https://news.ycombinator.com/item?id=48571081) | Epic Games 宣布版本控制系统 Lore。 | 1276 | 680 | 2026-06-17 |

## 2026-07

有效主帖 31,626 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I replaced a $120k bowling center system with $1,600 in ESP32s](https://news.ycombinator.com/item?id=48968606) | 经营八道保龄球馆的工程师，用一千六百美元 ESP32 替代昂贵控制系统。 | 2935 | 359 | 2026-07-19 |
| 2 | [Kimi K3 is now live](https://news.ycombinator.com/item?id=48935342) | Kimi K3 正式上线。 | 2107 | 1214 | 2026-07-16 |
| 3 | [Claude Opus 5](https://news.ycombinator.com/item?id=49038433) | Anthropic 发布 Claude Opus 5。 | 1778 | 1334 | 2026-07-24 |
| 4 | [A new Android malware from Google](https://news.ycombinator.com/item?id=48755965) | 作者将谷歌的一项 Android 软件称为新型恶意软件。 | 1734 | 746 | 2026-07-02 |
| 5 | [Elevators](https://news.ycombinator.com/item?id=49124218) | 以电梯为主角，关注这件日常垂直运输设备。 | 1680 | 415 | 2026-07-31 |
| 6 | [Apple Sues OpenAI for Stealing Trade Secrets to Build AI Hardware](https://news.ycombinator.com/item?id=48865019) | 苹果起诉 OpenAI，指控其窃取商业秘密制造 AI 硬件。 | 1660 | 966 | 2026-07-10 |
| 7 | [EU Parliament greenlights Chat Control 1.0 – Breyer: "Our children lose out"](https://news.ycombinator.com/item?id=48843923) | 欧洲议会通过 Chat Control 1.0，Breyer 批评其损害儿童利益。 | 1636 | 864 | 2026-07-09 |
| 8 | [OpenAI and Hugging Face partner to address security incident](https://news.ycombinator.com/item?id=48997548) | OpenAI 与 Hugging Face 合作处理安全事件。 | 1632 | 1157 | 2026-07-21 |
| 9 | [GPT-5.6](https://news.ycombinator.com/item?id=48849066) | OpenAI 发布 GPT-5.6。 | 1561 | 1112 | 2026-07-09 |
| 10 | [Zig Creator Calls Spade a Spade, Anthropic Blows Smoke](https://news.ycombinator.com/item?id=48889637) | 作者评价 Zig 创始人对 Anthropic 的直率批评。 | 1554 | 785 | 2026-07-13 |
| 11 | [Writing by Hand is Good for your Brain](https://news.ycombinator.com/item?id=49022152) | 介绍手写对大脑可能带来的益处。 | 1491 | 668 | 2026-07-23 |
| 12 | [Decoding the obfuscated bash script on a Uniqlo t-shirt](https://news.ycombinator.com/item?id=48829312) | 解码优衣库 T 恤上经过混淆的 Bash 脚本。 | 1489 | 232 | 2026-07-08 |
| 13 | [Half-Baked Product](https://news.ycombinator.com/item?id=48772388) | 作者关注产品尚未成熟、完成度不足的问题。 | 1405 | 415 | 2026-07-03 |
| 14 | [John Deere owners will get the right to repair equipment under FTC settlement](https://news.ycombinator.com/item?id=48838876) | FTC 和解将让 John Deere 用户获得设备维修权。 | 1397 | 306 | 2026-07-08 |
| 15 | [Kimi-K3 Releases on HuggingFace 6/27](https://news.ycombinator.com/item?id=49065752) | Kimi-K3 宣布六月二十七日在 Hugging Face 发布。 | 1382 | 544 | 2026-07-27 |
| 16 | [US citizen charged after GrapheneOS phone wipes during airport search](https://news.ycombinator.com/item?id=49063022) | 一名美国公民因 GrapheneOS 手机在机场搜查时擦除数据而被起诉。 | 1340 | 1120 | 2026-07-26 |
| 17 | [AWS: Inaccurate Estimated Billing Data - $1.7 BILLION](https://news.ycombinator.com/item?id=48945241) | AWS 用户报告收到十七亿美元预估账单，并已提交紧急支持请求。 | 1318 | 754 | 2026-07-17 |
| 18 | [American AI is locked down and proprietary. It's losing](https://news.ycombinator.com/item?id=48979269) | 作者认为封闭且专有的美国 AI 正失去竞争力。 | 1243 | 931 | 2026-07-20 |
| 19 | [UEFA and its national associations will not participate in FIFA competitions](https://news.ycombinator.com/item?id=49113929) | 欧足联及其成员协会宣布不参加国际足联赛事。 | 1235 | 674 | 2026-07-30 |
| 20 | [LG monitors silently install software through Windows Update without consent](https://news.ycombinator.com/item?id=48956688) | LG 显示器被指未经同意经 Windows Update 静默安装软件。 | 1228 | 637 | 2026-07-18 |

## 2026-08

有效主帖 22,026 条；排名来源 algolia。

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Don't be a meat proxy](https://news.ycombinator.com/item?id=49151933) | 作者呼吁避免成为替机器传递指令的人肉代理。 | 1849 | 741 | 2026-08-03 |
| 2 | [Firefox is now the last major browser that still supports uBlock Origin](https://news.ycombinator.com/item?id=49303202) | Firefox 成为仍支持 uBlock Origin 的最后一个主流浏览器。 | 1765 | 718 | 2026-08-14 |
| 3 | [Aaron Swartz was prosecuted for scraping, while Meta does it without consequence](https://news.ycombinator.com/item?id=49379550) | 作者比较 Aaron Swartz 因抓取资料遭起诉与 Meta 的不同待遇。 | 1704 | 404 | 2026-08-20 |
| 4 | [Stephen Wolfram's Wife Has Died](https://news.ycombinator.com/item?id=49173165) | Stephen Wolfram 的妻子去世。 | 1645 | 95 | 2026-08-04 |
| 5 | [OpenLogi](https://news.ycombinator.com/item?id=49355606) | 介绍 OpenLogi 项目。 | 1635 | 430 | 2026-08-19 |
| 6 | [Qwen 3.8 27B is out: open weights, best local dense model yet](https://news.ycombinator.com/item?id=49299605) | Qwen 3.8 27B 发布开放权重，并宣称提升本地稠密模型表现。 | 1438 | 793 | 2026-08-14 |
| 7 | [LLMs reward expertise](https://news.ycombinator.com/item?id=49161518) | 作者认为语言模型能让专业知识获得更大回报。 | 1416 | 573 | 2026-08-03 |
| 8 | [The Amazon Tax](https://news.ycombinator.com/item?id=49345263) | 探讨被称为“亚马逊税”的成本。 | 1415 | 705 | 2026-08-18 |
| 9 | [Kagi added a setting for removing paywalled links from search results](https://news.ycombinator.com/item?id=49388154) | Kagi 新增从搜索结果中移除付费墙链接的设置。 | 1275 | 394 | 2026-08-21 |
| 10 | [Tailscale Traces Database Corruption to 16y/o SQLite WAL-Reset Bug](https://news.ycombinator.com/item?id=49272832) | Tailscale 将数据库损坏追溯到 SQLite 存在十六年的 WAL 重置缺陷。 | 1223 | 239 | 2026-08-12 |
| 11 | [Meta Muse Glimmer – open weights 30B local coding model](https://news.ycombinator.com/item?id=49241679) | Meta 发布开放权重、三百亿参数的本地编程模型 Muse Glimmer。 | 1209 | 638 | 2026-08-10 |
| 12 | [Mario Meets Pareto](https://news.ycombinator.com/item?id=49195231) | 将马里奥与帕累托思想联系起来展开探索。 | 1188 | 169 | 2026-08-06 |
| 13 | [GLM-5.3: Frontier Coding with Emergent Cyber Capabilities](https://news.ycombinator.com/item?id=49294997) | GLM-5.3 展示前沿编程能力及涌现的网络安全能力。 | 1171 | 584 | 2026-08-14 |
| 14 | [Qwen3.8-Max: A New Bar for Coding and Cowork](https://news.ycombinator.com/item?id=49150470) | Qwen3.8-Max 宣称在编程与协作工作方面树立新标杆。 | 1124 | 612 | 2026-08-03 |
| 15 | [AI;DR (AI; Didn't Read)](https://news.ycombinator.com/item?id=49336573) | 讨论因内容由 AI 生成而选择不读的现象。 | 1119 | 692 | 2026-08-17 |
| 16 | [Why is Everyone in Tech so sad?](https://news.ycombinator.com/item?id=49209539) | 作者追问科技行业的人为何普遍感到悲伤。 | 1110 | 1325 | 2026-08-07 |
| 17 | [Felony charges for citizen deleting phone data at US Border](https://news.ycombinator.com/item?id=49386895) | 美国公民因在边境删除手机数据面临重罪指控。 | 1107 | 1383 | 2026-08-21 |
| 18 | [Israel creates fake think tank in likely attempt to dupe AI chatbots](https://news.ycombinator.com/item?id=49337392) | 报道称以色列创建虚假智库，可能试图误导 AI 聊天机器人。 | 1071 | 881 | 2026-08-17 |
| 19 | [France to ban unsolicited telemarketing calls](https://news.ycombinator.com/item?id=49254880) | 法国将禁止未经请求的电话营销。 | 1064 | 512 | 2026-08-11 |
| 20 | [Don't Paste the AI, please](https://news.ycombinator.com/item?id=49371857) | 作者呼吁不要直接粘贴 AI 生成内容。 | 1061 | 580 | 2026-08-20 |
