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


## Ask HN


### 2006-10

本月原始档案无该类有效主帖。

### 2006-11

本月原始档案无该类有效主帖。

### 2006-12

本月原始档案无该类有效主帖。

### 2007-01

本月原始档案无该类有效主帖。

### 2007-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Please tell us what features you'd like in news.ycombinator](https://news.ycombinator.com/item?id=363) | 邀请用户为 news.ycombinator 提出功能需求。 | 262 | 1590 | 2007-02-21 |
| 2 | [I'm looking for a partner or two (here are some of my ideas, feel free to add your own here)](https://news.ycombinator.com/item?id=1373) | 寻找创业搭档，也邀请读者交流各自想实现的点子。 | 15 | 31 | 2007-02-27 |
| 3 | [What algorithm does news.YC use to filter spam?](https://news.ycombinator.com/item?id=1007) | 提问 news.YC 使用什么算法识别和过滤垃圾内容。 | 9 | 10 | 2007-02-25 |
| 4 | [Y Combinator funded companies](https://news.ycombinator.com/item?id=1021) | 围绕 Y Combinator 已投资公司的名单展开交流。 | 4 | 6 | 2007-02-25 |
| 5 | [&#34;Remember Me&#34; Feature Would Be Nice](https://news.ycombinator.com/item?id=1031) | 建议网站加入“记住我”功能，减少反复登录。 | 3 | 2 | 2007-02-25 |
| 6 | [Is it acceptable for software to lie (like in the ESP Game say)?](https://news.ycombinator.com/item?id=1027) | 以 ESP Game 为例，讨论软件向用户撒谎是否可以接受。 | 2 | 2 | 2007-02-25 |
| 7 | [Networking: How do you manage your network and stay in touch with your key contacts?](https://news.ycombinator.com/item?id=1457) | 如何经营人际网络，并持续与重要联系人保持联系？ | 2 | 9 | 2007-02-28 |
| 8 | [Any thoughts on collaborative invention (e.g., using human-based genetic algorithms)?](https://news.ycombinator.com/item?id=1016) | 探讨协作发明的可能性，包括借助人类参与的遗传算法。 | 1 | 2 | 2007-02-25 |

### 2007-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Paul Graham convinced me to drop out of school / quit my job [Vote up if true]](https://news.ycombinator.com/item?id=6918) | 邀请因 Paul Graham 而退学或辞职的读者投票。 | 98 | 58 | 2007-03-28 |
| 2 | [What's the lowest offer you'd take?](https://news.ycombinator.com/item?id=5700) | 询问创业者愿意接受的最低报价，讨论个人心理价位。 | 21 | 52 | 2007-03-22 |
| 3 | [Applying to Y Combinator without a VISA?](https://news.ycombinator.com/item?id=4408) | 没有美国签证，能否先申请 Y Combinator？ | 18 | 23 | 2007-03-15 |
| 4 | [Work and Wives](https://news.ycombinator.com/item?id=7253) | 围绕工作与伴侣的关系，讨论事业和家庭如何相处。 | 18 | 35 | 2007-03-29 |
| 5 | [Folks On Student Visas Leave Comment About Your Burning Start Up Urge!](https://news.ycombinator.com/item?id=3531) | 邀请持学生签证、有强烈创业愿望的人交流处境。 | 17 | 28 | 2007-03-11 |
| 6 | [I will tell you why it's so freaking hard for single founders: It's so freaking lonely](https://news.ycombinator.com/item?id=5482) | 作者认为独立创始人难熬的重要原因是孤独。 | 17 | 36 | 2007-03-21 |
| 7 | [Startup Age Of Success Stats For People in Founders At Work](https://news.ycombinator.com/item?id=6612) | 关注《Founders at Work》中创业者取得成功时的年龄。 | 17 | 7 | 2007-03-27 |
| 8 | [Startup founders, how old are you?](https://news.ycombinator.com/item?id=2260) | 向社区创业者征集年龄，看看大家何时开始创业。 | 16 | 55 | 2007-03-05 |
| 9 | [How many summer Y Combinator fundees decided not to continue with their startup and go back to school? and what were the reasons?](https://news.ycombinator.com/item?id=3891) | 询问 YC 夏季项目成员放弃创业、返回学校的原因。 | 15 | 21 | 2007-03-13 |
| 10 | [Why do you want to pursue a startup?](https://news.ycombinator.com/item?id=2079) | 邀请社区读者说说自己为什么想走上创业这条道路。 | 13 | 24 | 2007-03-04 |

### 2007-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Vote up if you would like news.Ycomb add a feature where users can save their favorite stories](https://news.ycombinator.com/item?id=14957) | 征集为 YC 新闻增加收藏文章功能的支持票。 | 54 | 24 | 2007-04-20 |
| 2 | [Vote up if you're refreshing your email once a minute today](https://news.ycombinator.com/item?id=11285) | 邀请正在频繁刷新邮箱等待消息的用户投票。 | 50 | 96 | 2007-04-10 |
| 3 | [Vote up if you're rejected but will still proceed](https://news.ycombinator.com/item?id=11551) | 邀请申请被拒后仍决定继续创业的人投票。 | 50 | 62 | 2007-04-10 |
| 4 | [What are the best non-database solutions you've seen? What did Viaweb use?](https://news.ycombinator.com/item?id=14605) | 征集数据库之外的数据方案，并追问 Viaweb 的做法。 | 34 | 65 | 2007-04-19 |
| 5 | [Vote up if you want the submission title displayed as your browser title for bookmarking](https://news.ycombinator.com/item?id=16703) | 建议把投稿标题用作页面标题，方便浏览器收藏。 | 32 | 12 | 2007-04-25 |
| 6 | [What is the best credit card processing setup for startups?](https://news.ycombinator.com/item?id=12010) | 征求适合初创公司的信用卡收款方案。 | 30 | 23 | 2007-04-11 |
| 7 | [YC News is one of the best sites I have come across in a long time](https://news.ycombinator.com/item?id=14947) | 作者分享对 YC News 的喜爱，认为它是难得的好网站。 | 24 | 15 | 2007-04-20 |
| 8 | [Question to YC: trends in summer founders applications, demographics](https://news.ycombinator.com/item?id=8946) | 向 YC 询问夏季申请者的趋势及人口构成。 | 22 | 10 | 2007-04-04 |
| 9 | [Startup Company Form: LLC or S-Corp? Which is easier and which is better?](https://news.ycombinator.com/item?id=13752) | 创业公司选择 LLC 还是 S-Corp，哪种更省事、更合适？ | 22 | 31 | 2007-04-17 |
| 10 | [Advice needed: "friend" stole my idea...what to do?](https://news.ycombinator.com/item?id=16972) | 作者称点子被朋友拿走，求助该如何处理这段关系。 | 21 | 78 | 2007-04-26 |

### 2007-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Vote up if you want YC to remember your cookie for longer than a few hours](https://news.ycombinator.com/item?id=18275) | 征集延长 YC 新闻登录 Cookie 有效期的支持。 | 78 | 15 | 2007-05-01 |
| 2 | [How to get/make a Logo for Your Startup?](https://news.ycombinator.com/item?id=18308) | 初创公司如何设计或找人制作一个合适的标志？ | 24 | 21 | 2007-05-01 |
| 3 | [What is your recommended beginner's hacker training course?](https://news.ycombinator.com/item?id=21022) | 为刚入门的黑客新手寻找值得推荐的基础学习课程。 | 22 | 41 | 2007-05-10 |
| 4 | [Is anyone working on something that is not a website?](https://news.ycombinator.com/item?id=21107) | 邀请正在做网站以外项目的人介绍自己的工作。 | 22 | 64 | 2007-05-10 |
| 5 | [Warning: RoR is slow](https://news.ycombinator.com/item?id=25628) | 作者提醒 Rails 速度可能较慢，引出性能取舍问题。 | 21 | 58 | 2007-05-31 |
| 6 | [What hosting provider are you using for your startup ?](https://news.ycombinator.com/item?id=18363) | 向创业者打听正在使用哪些服务器托管服务。 | 19 | 37 | 2007-05-01 |
| 7 | [Academia.edu: looking for technical co-founder](https://news.ycombinator.com/item?id=23901) | Academia.edu 寻找技术联合创始人，邀请有意者关注。 | 18 | 20 | 2007-05-22 |
| 8 | [does web.py have documentation and are you using webpy?](https://news.ycombinator.com/item?id=25280) | 询问 web.py 的文档情况，以及社区是否有人实际使用。 | 18 | 28 | 2007-05-29 |
| 9 | [I'm getting a Mac. Which Mac do you use?](https://news.ycombinator.com/item?id=19203) | 准备购买 Mac 的作者想听听大家的机型选择。 | 17 | 51 | 2007-05-04 |
| 10 | [Paul Buchheit:"Don't Be Evil"](https://news.ycombinator.com/item?id=22540) | 围绕 Paul Buchheit 与“不作恶”理念展开关注。 | 14 | 25 | 2007-05-16 |

### 2007-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [YC: "unknown or expired link" -- fix it already](https://news.ycombinator.com/item?id=28944) | 用户抱怨 YC 的链接过期提示，希望尽快修复。 | 24 | 8 | 2007-06-18 |
| 2 | [How necessary is it to have a lawyer incorporate you?](https://news.ycombinator.com/item?id=28150) | 公司注册是否必须请律师，自己办理又有哪些考虑？ | 23 | 28 | 2007-06-14 |
| 3 | [Any recommendations on convincing wives to let their husbands become entrepreneurs?](https://news.ycombinator.com/item?id=29098) | 如何与妻子沟通，让伴侣支持丈夫转向创业？ | 18 | 50 | 2007-06-19 |
| 4 | [Computational Finance - The Silent Killer](https://news.ycombinator.com/item?id=29301) | 作者以“无声杀手”形容计算金融，提出这一话题。 | 17 | 27 | 2007-06-19 |
| 5 | [Favicon for news.ycombinator](https://news.ycombinator.com/item?id=28167) | 讨论给 news.ycombinator 配置网站图标的想法。 | 16 | 13 | 2007-06-14 |
| 6 | [When is it time to give up on your web startup?](https://news.ycombinator.com/item?id=26306) | 什么情况下应该承认失败，停止经营自己的网络创业项目？ | 14 | 21 | 2007-06-04 |
| 7 | [Is the development of automated tests a waste of time for a startup?](https://news.ycombinator.com/item?id=27875) | 创业早期投入时间编写自动化测试，究竟是否值得？ | 13 | 45 | 2007-06-13 |
| 8 | [How are you all sending out your press releases?](https://news.ycombinator.com/item?id=31672) | 向创业同行征集发布新闻稿的具体做法与实用渠道。 | 13 | 13 | 2007-06-29 |
| 9 | [Moonlighting? Please Tell Me About It](https://news.ycombinator.com/item?id=31694) | 邀请有兼职创业或业余接活经验的人分享经历。 | 13 | 19 | 2007-06-30 |
| 10 | [We want a sub-YCNews](https://news.ycombinator.com/item?id=31776) | 提出建立 YC News 子社区的需求，讨论更细的交流空间。 | 13 | 25 | 2007-06-30 |

### 2007-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [If you are reading this you are not working on your startup.](https://news.ycombinator.com/item?id=34114) | 以阅读创业资讯的行为提醒创业者关注实际行动。 | 45 | 28 | 2007-07-13 |
| 2 | [PG: If starting Viaweb today, would you use Lisp?](https://news.ycombinator.com/item?id=36905) | 追问今天重做 Viaweb 是否仍会选择 Lisp 及其思维优势。 | 30 | 33 | 2007-07-26 |
| 3 | [What can you do with money?](https://news.ycombinator.com/item?id=37246) | 创业带来更多收入后，作者反而困惑该怎样使用这些钱。 | 26 | 83 | 2007-07-28 |
| 4 | [Are you a Canadian YC News reader?](https://news.ycombinator.com/item?id=37384) | 召集加拿大的 YC News 读者，看看社区里有多少同乡。 | 24 | 47 | 2007-07-29 |
| 5 | [Just sent my resignation letter and this is my plan.](https://news.ycombinator.com/item?id=36276) | 作者辞职后计划补齐计算机与数学基础，再探索下一步。 | 23 | 49 | 2007-07-24 |
| 6 | [New: Initial text in discussions](https://news.ycombinator.com/item?id=32933) | 网站新增讨论开头说明文字，作者也担心这会削弱简洁性。 | 22 | 16 | 2007-07-07 |
| 7 | [How do you write a "terms of use" for a website?](https://news.ycombinator.com/item?id=37112) | 网站使用条款能否自己写，律师费用和模板又该怎么找？ | 22 | 13 | 2007-07-27 |
| 8 | [What ideas have you implemented that have failed, and why?](https://news.ycombinator.com/item?id=37733) | 征集已经动手却仍失败的点子，关注失败背后的原因。 | 20 | 18 | 2007-07-30 |
| 9 | [Interviewing with Y Combinator startups?](https://news.ycombinator.com/item?id=32528) | 询问与 Y Combinator 创业公司面试的相关经验。 | 17 | 3 | 2007-07-05 |
| 10 | [Is it bad if I don't want to work at a C++/Java startup?](https://news.ycombinator.com/item?id=34461) | 机会不错却不喜欢 C++ 和 Java，该不该加入这家初创公司？ | 17 | 86 | 2007-07-16 |

### 2007-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Goodbye, Hacker News. I'm going back to Reddit.](https://news.ycombinator.com/item?id=43635) | 一位用户因社区内容方向与氛围变化宣布离开 HN。 | 48 | 67 | 2007-08-17 |
| 2 | [How to Massively Increase Your Productivity and Happiness in 2 Hours Per Day](https://news.ycombinator.com/item?id=39699) | 作者建议提前两小时睡觉，以改善效率与幸福感。 | 43 | 42 | 2007-08-06 |
| 3 | [Am I the only one who doesn't care about Facebook?](https://news.ycombinator.com/item?id=41716) | 作者不理解 Facebook 的吸引力，并质疑封闭社交平台。 | 36 | 42 | 2007-08-12 |
| 4 | [What is going on with the editing of submission titles?](https://news.ycombinator.com/item?id=43534) | 用户发现投稿标题被别人修改，希望了解网站编辑规则。 | 32 | 28 | 2007-08-17 |
| 5 | [News.YC Library](https://news.ycombinator.com/item?id=45082) | 征集黑客书架必备读物，技术书籍和免费在线资料都欢迎。 | 32 | 31 | 2007-08-22 |
| 6 | [do not. I am just letting it out.](https://news.ycombinator.com/item?id=47232) | 作者在失业、汽车故障等接连打击后，向熟悉的社区倾诉。 | 31 | 29 | 2007-08-28 |
| 7 | [Hacker School](https://news.ycombinator.com/item?id=44876) | 讨论从基础教育阶段培养编程与创造能力的“黑客学校”。 | 29 | 54 | 2007-08-21 |
| 8 | [Nah Seriously! Who designs the YC startups websites? Loving it.](https://news.ycombinator.com/item?id=39611) | 作者欣赏 YC 创业公司的网站视觉，想知道设计由谁完成。 | 26 | 29 | 2007-08-05 |
| 9 | [The Entrepreneurial Attitude](https://news.ycombinator.com/item?id=41815) | 分享小咖啡馆面对星巴克入驻时，一封鼓励员工的信。 | 26 | 27 | 2007-08-13 |
| 10 | [Why is it hard to startup a company outside of Silicon Valley?](https://news.ycombinator.com/item?id=42933) | 为什么创业资源聚集在硅谷，其他城市的产业集群又如何形成？ | 26 | 63 | 2007-08-16 |

### 2007-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Are you going to change the world?  (Really?)](https://news.ycombinator.com/item?id=57298) | 由一位患癌教授的人生态度追问创业者如何改变世界。 | 57 | 94 | 2007-09-20 |
| 2 | [What I learned about women & business today](https://news.ycombinator.com/item?id=61006) | 作者从女性高管圆桌中思考女性与商业的问题。 | 56 | 22 | 2007-09-29 |
| 3 | [Startup idea list](https://news.ycombinator.com/item?id=55974) | 邀请读者在评论区提出创业点子并通过投票反馈。 | 54 | 167 | 2007-09-18 |
| 4 | [Ask YC Hackers: What's the best text for learning Javascript?](https://news.ycombinator.com/item?id=61311) | 有编程经验的开发者想系统学习 JavaScript，征求教材建议。 | 46 | 22 | 2007-09-30 |
| 5 | [OK, you've convinced me. I'm coming to join you.](https://news.ycombinator.com/item?id=52580) | 一位有家庭的程序员决定离开大公司，与妻子一起准备创业。 | 43 | 74 | 2007-09-09 |
| 6 | [An Interview With Paul Graham...](https://news.ycombinator.com/item?id=50776) | 向 Paul Graham 提出公开访谈问题，包括 YC 是否投非营利项目。 | 42 | 20 | 2007-09-06 |
| 7 | [Where and how to announce the launch of a website?](https://news.ycombinator.com/item?id=55556) | 社交交易网站即将上线，作者征集发布消息和吸引关注的渠道。 | 39 | 35 | 2007-09-17 |
| 8 | [Me and PG's Code](https://news.ycombinator.com/item?id=55437) | 作者即将入职雅虎小企业部门，期待接触 Viaweb 留下的代码。 | 38 | 10 | 2007-09-16 |
| 9 | [What books would you recommend reading?  Why?](https://news.ycombinator.com/item?id=56618) | 邀请推荐值得阅读的书，也说说每本书的推荐理由。 | 37 | 89 | 2007-09-19 |
| 10 | [Food Ideas for Startup Guys](https://news.ycombinator.com/item?id=57538) | 征集适合创业忙碌生活的饭菜，让写代码的人吃得更舒服。 | 36 | 64 | 2007-09-20 |

### 2007-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Why to Apply to YCombinator](https://news.ycombinator.com/item?id=65327) | 作者以个人申请经历说明为何值得申请 Y Combinator。 | 113 | 36 | 2007-10-09 |
| 2 | [Ask news YC: Your best sources to learn about design & usability](https://news.ycombinator.com/item?id=66863) | 征集学习设计与可用性的优质网站和博客。 | 58 | 31 | 2007-10-12 |
| 3 | [If you applied for this cycle, please tell us your email address](https://news.ycombinator.com/item?id=69683) | 提醒本轮 YC 申请者填写个人资料邮箱，否则可能收不到回复。 | 50 | 28 | 2007-10-18 |
| 4 | [Some things to do (and not do) if you aren't invited to interview with YC](https://news.ycombinator.com/item?id=68535) | 一位曾落选的申请者，给没拿到 YC 面试邀请的人提供建议。 | 49 | 43 | 2007-10-16 |
| 5 | [Hackers' screen shots](https://news.ycombinator.com/item?id=74605) | 邀请大家展示工作环境截图，交流各自的桌面和工具布置。 | 49 | 101 | 2007-10-31 |
| 6 | [Non-US Visa Applicants to the US - Don't You Think It's Time We Compared Notes?](https://news.ycombinator.com/item?id=67268) | 创业团队分享赴美签证与跨国公司架构经历，邀请互通经验。 | 48 | 24 | 2007-10-13 |
| 7 | [An open letter from the founders of Scribd to those of you who didn't get into YC](https://news.ycombinator.com/item?id=72190) | Scribd 创始人致信未获 YC 录取者，谈下一步的创业选择。 | 44 | 43 | 2007-10-24 |
| 8 | [Where do YC applicants host their projects?](https://news.ycombinator.com/item?id=64795) | 询问 YC 申请者如何在独服、VPS 和其他托管方案之间选择。 | 40 | 42 | 2007-10-08 |
| 9 | [Idea Week. Post ideas you don't plan on implementing.](https://news.ycombinator.com/item?id=65081) | 发起点子分享周，把自己无暇实现的创业想法送给社区。 | 39 | 107 | 2007-10-09 |
| 10 | [Ask YC: Experiences with founder burnout?](https://news.ycombinator.com/item?id=69097) | 作者创业十个月后感到耗尽，想听其他创始人的倦怠经历。 | 37 | 38 | 2007-10-17 |

### 2007-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Number of founders - statistics](https://news.ycombinator.com/item?id=77525) | 统计一百家上市科技公司的创始人人数，并说明局限。 | 232 | 38 | 2007-11-08 |
| 2 | [Absolutely, DO NOT, get a co-founder!](https://news.ycombinator.com/item?id=77246) | 一位有多年创业公司经验的作者主张不要寻找联合创始人。 | 112 | 94 | 2007-11-08 |
| 3 | [Is Aaron Swartz the Paris Hilton of Web 2.0?](https://news.ycombinator.com/item?id=79982) | 发帖者质疑 Aaron Swartz 的知名度是否与实际贡献相称。 | 48 | 103 | 2007-11-15 |
| 4 | [What Android's really about (hint: not the iPhone)](https://news.ycombinator.com/item?id=79253) | 作者把 Android 类比为 DOS，关注它对碎片化手机平台的意义。 | 40 | 45 | 2007-11-13 |
| 5 | [Ask YC:  What new technologies are you exploring?](https://news.ycombinator.com/item?id=81594) | 邀请大家介绍最近正在尝试、研究或感兴趣的新技术。 | 36 | 103 | 2007-11-19 |
| 6 | [The future of programming languages in a massively concurrent world](https://news.ycombinator.com/item?id=76007) | 多核处理器日益普及，编程语言该怎样适应大规模并发？ | 31 | 32 | 2007-11-04 |
| 7 | [Ask YC: Profit: $25/user. Customers: satisfied. Competitors: none. Target market: huge. But...](https://news.ycombinator.com/item?id=76077) | 用户满意且每单盈利，医疗服务网站却获客很少，该如何增长？ | 30 | 56 | 2007-11-04 |
| 8 | [Scheme in the real world](https://news.ycombinator.com/item?id=75126) | 询问 Scheme 是否适合真实业务，尤其是网站等不同项目。 | 29 | 26 | 2007-11-01 |
| 9 | [Who got in?](https://news.ycombinator.com/item?id=76137) | 邀请本轮获录取者报到，并分享参与过程中的感受。 | 29 | 9 | 2007-11-04 |
| 10 | [A hack I'm rather proud of](https://news.ycombinator.com/item?id=83685) | 接手老在线卡牌游戏后，作者分享维持旧版本运行的一次巧思。 | 29 | 22 | 2007-11-26 |

### 2007-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Cheer YC:  Happy Holidays!](https://news.ycombinator.com/item?id=92441) | 向 YC 社区送上节日祝福，祝大家假期愉快、新年顺利。 | 47 | 32 | 2007-12-24 |
| 2 | [Ask YC: Will there really always be room for more successful web startups?](https://news.ycombinator.com/item?id=89055) | 网络应用会不会逐渐饱和，未来还容得下更多成功创业公司吗？ | 44 | 58 | 2007-12-13 |
| 3 | [Ask YC: favorite books](https://news.ycombinator.com/item?id=85840) | 征集编程和技术领域以外的最爱书单，看看黑客还读些什么。 | 43 | 80 | 2007-12-04 |
| 4 | [An Offer](https://news.ycombinator.com/item?id=87522) | 十九岁程序员收到旧金山创业公司的邀约，征求搬迁与职业建议。 | 39 | 56 | 2007-12-09 |
| 5 | [Ask YC: AI](https://news.ycombinator.com/item?id=90387) | 想入门人工智能的读者，向社区寻找适合起步的书。 | 36 | 87 | 2007-12-17 |
| 6 | [Reliable Script Generated Email Delivery Anyone?](https://news.ycombinator.com/item?id=92022) | 网站通知邮件被邮箱服务商丢弃，作者求可靠的邮件投递办法。 | 35 | 17 | 2007-12-22 |
| 7 | [Ask YC: What tools are you using to monitor a site's load?](https://news.ycombinator.com/item?id=92388) | 大家使用哪些工具监控网站负载，及时掌握运行压力？ | 33 | 13 | 2007-12-24 |
| 8 | [Is this burnout? Why?](https://news.ycombinator.com/item?id=89861) | 明知任务不难却迟迟无法开始，作者怀疑自己是否陷入倦怠。 | 31 | 43 | 2007-12-15 |
| 9 | [Happy New Year!](https://news.ycombinator.com/item?id=93920) | 面向创业者送上新年祝福，愿大家在 2008 年事业顺利。 | 31 | 40 | 2007-12-31 |
| 10 | [Ask YC: What is a website worth?](https://news.ycombinator.com/item?id=91575) | 一次性邮箱网站收到收购意向，作者求助如何按流量和收入估值。 | 29 | 35 | 2007-12-20 |

### 2008-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [More advice for new Y Combinator founders](https://news.ycombinator.com/item?id=95857) | 为 YC 新创始人提供保持情绪稳定、专注产品及谨慎招聘的建议。 | 124 | 28 | 2008-01-08 |
| 2 | [Anywhere.FM acquired by imeem](https://news.ycombinator.com/item?id=105557) | 在线音乐服务 Anywhere.FM 宣布被 imeem 收购。 | 70 | 27 | 2008-01-28 |
| 3 | [Ask NickB:  How do you do it, dude?](https://news.ycombinator.com/item?id=99923) | 向活跃投稿者 NickB 取经：如何投入时间、持续发现好链接？ | 52 | 38 | 2008-01-17 |
| 4 | [Ask YC: how do you work for 8 hours straight?](https://news.ycombinator.com/item?id=97829) | 每天持续工作八小时现实吗，难以进入状态时该如何安排？ | 49 | 63 | 2008-01-13 |
| 5 | [Ask YComb: Should I quit to do a startup during a recession?](https://news.ycombinator.com/item?id=101703) | 经济衰退风险渐显，年轻程序员是否应该辞职去创业？ | 39 | 64 | 2008-01-21 |
| 6 | [Ask YC: tendonitis at a startup?](https://news.ycombinator.com/item?id=104977) | 创业公司的长时间编码让手腕恶化，作者求助如何应对腱鞘问题。 | 35 | 62 | 2008-01-27 |
| 7 | [How do you get traffic?](https://news.ycombinator.com/item?id=104627) | 网站上线热度过后，创业者还能通过哪些方式继续获取流量？ | 31 | 20 | 2008-01-26 |
| 8 | [Please share your (non-computer) system hacker stories](https://news.ycombinator.com/item?id=104802) | 征集利用非计算机系统规则解决问题、为自己争取优势的经历。 | 30 | 37 | 2008-01-27 |
| 9 | [How does everybody backup?](https://news.ycombinator.com/item?id=99194) | 讨论个人与创业项目怎样备份，尤其关注故障后的完整恢复。 | 29 | 47 | 2008-01-16 |
| 10 | [Ask YC: Which web host do you use?](https://news.ycombinator.com/item?id=96374) | 现有主机服务故障频繁，作者想知道大家使用哪些替代服务商。 | 27 | 45 | 2008-01-09 |

### 2008-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Smjörið er brætt og hveitið smátt og smátt hrært út í það, þangað til það er gengið upp í smjörið.](https://news.ycombinator.com/item?id=111100) | 用冰岛语内容验证 Patrick Collison 修复后的 UTF-8 支持。 | 125 | 154 | 2008-02-07 |
| 2 | [Learning Math](https://news.ycombinator.com/item?id=108723) | 一位三十多岁读者征求从基础建立数学直觉的学习资源。 | 122 | 74 | 2008-02-03 |
| 3 | [How do you learn?](https://news.ycombinator.com/item?id=109802) | 邀请程序员交流各自最有效的自学方法。 | 79 | 54 | 2008-02-05 |
| 4 | [Ask News.YC: How to re-motivate yourself?](https://news.ycombinator.com/item?id=121175) | 创业近一年的发帖者寻求重新找回动力的方法。 | 75 | 42 | 2008-02-22 |
| 5 | [How about this idea to save Hacker News from fluff?](https://news.ycombinator.com/item?id=121398) | 作者提议审查同时登上 Reddit 首页的投稿，以减少 HN 杂谈。 | 52 | 65 | 2008-02-22 |
| 6 | [Ask YC: Status of your startup](https://news.ycombinator.com/item?id=108115) | 邀请创业者汇报项目近况、上线计划，以及正在忙什么。 | 48 | 91 | 2008-02-02 |
| 7 | [Ask YC: Are you self-funding/bootstrapping?](https://news.ycombinator.com/item?id=114310) | 征集自筹资金创业的实际经历，讨论控制权与资金不足的取舍。 | 42 | 55 | 2008-02-12 |
| 8 | [Ask YC: Learning Web Development, were should I start?](https://news.ycombinator.com/item?id=123903) | 已有前端基础，下一步该如何安排服务端编程和数据库学习？ | 40 | 56 | 2008-02-26 |
| 9 | [Followup on ERP Thread: How I Plan To Do ERP](https://news.ycombinator.com/item?id=114568) | 有 ERP 实施经验的创业者介绍自己的计划，回应此前的讨论。 | 39 | 49 | 2008-02-13 |
| 10 | [Ask YC: How many hours do you sleep on average ? ](https://news.ycombinator.com/item?id=114846) | 为了多做事而减少睡眠是否可行，作者询问大家每天睡多久。 | 38 | 127 | 2008-02-13 |

### 2008-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Would this community prefer to be under the radar?](https://news.ycombinator.com/item?id=146604) | 发帖者询问 TechCrunch 的曝光是否会伤害 HN 社区。 | 103 | 91 | 2008-03-26 |
| 2 | [Ask YC: Dealing with post startup depression](https://news.ycombinator.com/item?id=146916) | 首次创业关停后陷入失落，作者求助如何走出失败阴影。 | 72 | 57 | 2008-03-26 |
| 3 | [Come stay at the hacker house in San Jose, Free](https://news.ycombinator.com/item?id=140554) | 两位创业者搬到圣何塞，邀请其他黑客免费住进空余房间。 | 68 | 55 | 2008-03-19 |
| 4 | [Ask Hacker News: Cost of living in Silicon Valley](https://news.ycombinator.com/item?id=128872) | 单身人士在硅谷每月要花多少钱，房租和生活开支如何估算？ | 58 | 63 | 2008-03-04 |
| 5 | [Ask: What would you do/make if you never had to monetize it?](https://news.ycombinator.com/item?id=142723) | 如果收入已有保障、不必变现，你最想做什么产品或项目？ | 57 | 170 | 2008-03-21 |
| 6 | [YC Help: I need Acquisition Advice](https://news.ycombinator.com/item?id=130228) | 成立八个月的盈利公司面临收购，三至四倍收益的报价合理吗？ | 53 | 38 | 2008-03-06 |
| 7 | [Ask PG: What's the traffic effect here from the TechCrunch mention?](https://news.ycombinator.com/item?id=134247) | 询问登上 TechCrunch 后，HN 的流量、用户与投稿发生了什么变化。 | 49 | 22 | 2008-03-11 |
| 8 | ["I never saved anything for the swim back"](https://news.ycombinator.com/item?id=145582) | 借《千钧一发》的台词，作者谈创业时全力投入的心态。 | 49 | 33 | 2008-03-25 |
| 9 | [Ask YC: Who's your favorite domain registrar and why?](https://news.ycombinator.com/item?id=150561) | 寻找适合管理大量域名的注册商，并希望了解推荐理由。 | 49 | 66 | 2008-03-31 |
| 10 | [Ask YC: What would you put on a hacker's bookshelf?](https://news.ycombinator.com/item?id=135185) | 一本书、一台旧电脑：邀请大家列出黑客书架上的必备物品。 | 48 | 63 | 2008-03-12 |

### 2008-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Solo founders: how do you stay emotionally efficient?](https://news.ycombinator.com/item?id=166905) | 独立创始人征求保持情绪与心理状态稳定的方法。 | 119 | 96 | 2008-04-18 |
| 2 | [Tumblr security hole (the gaping kind)](https://news.ycombinator.com/item?id=164422) | 作者报告 Tumblr 登录后可进入全站管理页的严重安全疑点。 | 80 | 78 | 2008-04-15 |
| 3 | [Django - starting from ground zero - any advice?](https://news.ycombinator.com/item?id=175386) | 刚开始接触 Python 和 Django，哪里有适合边做边学的教程？ | 67 | 41 | 2008-04-28 |
| 4 | [Why Lisp Is Unpopular](https://news.ycombinator.com/item?id=153812) | 作者借相控阵雷达引出“Lisp 为何不流行”的讨论。 | 62 | 157 | 2008-04-03 |
| 5 | [Nickb, Are you okay?](https://news.ycombinator.com/item?id=173683) | 活跃用户 NickB 一周未出现，社区成员关心他的近况。 | 60 | 54 | 2008-04-25 |
| 6 | [Ask YC: Best ways to become socially adept?](https://news.ycombinator.com/item?id=169295) | 除了演讲训练和读书，还有哪些方法能改善人际交往能力？ | 59 | 104 | 2008-04-21 |
| 7 | [Tell YC: Thanks for Startup School](https://news.ycombinator.com/item?id=168395) | 来自硅谷之外的参与者感谢 Startup School 带来的学习与交流。 | 58 | 18 | 2008-04-20 |
| 8 | [So, what's the next step?  Let's network.](https://news.ycombinator.com/item?id=160398) | 未获 YC 机会也可以互相连接，作者邀请大家一起建立创业网络。 | 56 | 38 | 2008-04-10 |
| 9 | [Y Combinator Dataset Of Posts](https://news.ycombinator.com/item?id=172701) | 分享 YC 历史帖子数据集，供网站搜索和社区行为分析使用。 | 56 | 22 | 2008-04-24 |
| 10 | [Ask YC: What do you scrape? How do you scrape?](https://news.ycombinator.com/item?id=158902) | 大家都抓取哪些网页数据，用什么办法，又会遇到哪些麻烦？ | 51 | 46 | 2008-04-09 |

### 2008-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell YC: Answers from John McCarthy](https://news.ycombinator.com/item?id=185348) | 一位学生整理 John McCarthy 在斯坦福课堂访谈中的回答。 | 136 | 72 | 2008-05-09 |
| 2 | [Ask YC: Startup crisis. Out of money and tech co-founder has bailed.](https://news.ycombinator.com/item?id=183535) | 一位非技术创始人在资金耗尽、技术合伙人退出后求助。 | 129 | 232 | 2008-05-07 |
| 3 | [Ask YC: Have you built a good website that nobody visits?](https://news.ycombinator.com/item?id=187977) | 邀请读者分享产品不错却无人访问的网站项目。 | 103 | 120 | 2008-05-12 |
| 4 | [Ask YC: Best book to learns statistics?](https://news.ycombinator.com/item?id=201913) | 数学基础不错却缺统计知识，作者征求从基础学起的教材。 | 80 | 17 | 2008-05-28 |
| 5 | [Ask YC:  What are the going rates for consulting gigs?](https://news.ycombinator.com/item?id=182369) | 咨询开发工作现在如何报价，语言、地区和业务类型会差多少？ | 78 | 105 | 2008-05-06 |
| 6 | [To HN: Looking for people to talk to...](https://news.ycombinator.com/item?id=203795) | 临近毕业的作者谈缺少朋友，希望结识社区里有趣的同伴。 | 77 | 47 | 2008-05-29 |
| 7 | [Ask HN: Subscription web sites: How did you get your first customer?](https://news.ycombinator.com/item?id=191899) | 擅长编码却不擅长社交，订阅制网站怎样找到第一个付费客户？ | 70 | 50 | 2008-05-16 |
| 8 | [Ask YC: Django vs Ruby on Rails](https://news.ycombinator.com/item?id=195423) | 新项目该选 Django 还是 Rails，作者希望听到较新的实际比较。 | 70 | 112 | 2008-05-20 |
| 9 | [Ask Eliezer Yudkowsky: How did you convince the Gatekeeper to release the potentially genocidal AI?](https://news.ycombinator.com/item?id=195959) | 向 Yudkowsky 追问 AI 盒子实验：如何说服守门人释放 AI？ | 60 | 52 | 2008-05-21 |
| 10 | [Telling our children the truth: response to Paul Graham](https://news.ycombinator.com/item?id=199279) | 回应 Paul Graham，作者分享自己坚持对孩子说实话的教养观。 | 58 | 53 | 2008-05-25 |

### 2008-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN:  The Secret Sauce of Angel Investment?](https://news.ycombinator.com/item?id=229092) | 独立创始人分享向个人投资者融资所用的材料和思路。 | 66 | 22 | 2008-06-26 |
| 2 | [HN: New flag feature](https://news.ycombinator.com/item?id=226400) | HN 新增举报链接，用户询问何时、怎样使用才合适。 | 64 | 88 | 2008-06-24 |
| 3 | [Remind HN: Father's Day is Sunday](https://news.ycombinator.com/item?id=215605) | 提醒忙于项目的读者父亲节将至，别忘了向父亲表达心意。 | 63 | 29 | 2008-06-12 |
| 4 | [Ask YC: Dealing with a major event like death?](https://news.ycombinator.com/item?id=212479) | 考试期间发现室友去世，作者求助如何面对突如其来的重大打击。 | 62 | 54 | 2008-06-09 |
| 5 | [LinkedIn is Evil](https://news.ycombinator.com/item?id=220138) | 作者抱怨 LinkedIn 续费与降级流程，质疑其收费设计。 | 60 | 57 | 2008-06-17 |
| 6 | [Easier browsing of Hacker News...for me](https://news.ycombinator.com/item?id=216446) | HN SplitView 书签工具把原文与评论并排显示，方便来回阅读。 | 57 | 36 | 2008-06-13 |
| 7 | [Enter about:robots in the URL field if you're running Firefox 3](https://news.ycombinator.com/item?id=222052) | 邀请 Firefox 3 用户输入 about:robots，看看浏览器里的彩蛋。 | 56 | 6 | 2008-06-19 |
| 8 | [My New Instant Karma Plan](https://news.ycombinator.com/item?id=215147) | 作者分享一套快速积累 HN 积分的计划，带有自嘲意味。 | 50 | 66 | 2008-06-11 |
| 9 | [Facebook needs to quit with its thuggish attitude](https://news.ycombinator.com/item?id=228501) | Facebook 因活动过多封停账号，作者质疑平台对用户内容的处置。 | 50 | 35 | 2008-06-26 |
| 10 | [Critique: "Programming Collective Intelligence"](https://news.ycombinator.com/item?id=208811) | 读《Programming Collective Intelligence》后，作者讨论网站的技术深度。 | 48 | 28 | 2008-06-04 |

### 2008-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [We've been working really hard on our startup and now this](https://news.ycombinator.com/item?id=233166) | 团队将推出 Flash 搜索，却遇谷歌与雅虎入场，该怎样应对？ | 86 | 74 | 2008-07-01 |
| 2 | [Ask YC: "Rock Star" Job Titles](https://news.ycombinator.com/item?id=255587) | 职位广告中的“摇滚明星开发者”称谓，会让求职者产生什么感受？ | 72 | 121 | 2008-07-24 |
| 3 | [Ask HN: Best books/source to learn about investing?](https://news.ycombinator.com/item?id=248469) | 准备从储蓄转向投资的大学生，寻找股票、债券和退休理财读物。 | 65 | 67 | 2008-07-17 |
| 4 | [Expired links should be less common](https://news.ycombinator.com/item?id=245870) | 网站改用固定投票与回复链接，希望减少“链接已过期”提示。 | 61 | 24 | 2008-07-14 |
| 5 | [Questions from a young developer that "just" started working aka: how do you manage it?](https://news.ycombinator.com/item?id=240325) | 全职开发后失去个人项目动力，年轻程序员想知道如何调整。 | 52 | 65 | 2008-07-08 |
| 6 | [At 38, am I too old for a startup?](https://news.ycombinator.com/item?id=248811) | 三十八岁还适合创业吗，一个惦念已久的点子让作者犹豫。 | 50 | 89 | 2008-07-17 |
| 7 | [Ask HN: Would free copywriting assistance appeal to you?](https://news.ycombinator.com/item?id=249908) | 市场从业者想免费帮忙写文案，以结识技术伙伴并探索创业。 | 42 | 34 | 2008-07-18 |
| 8 | [Ask YC: Why the excitement over XMPP on the backend?](https://news.ycombinator.com/item?id=263017) | 为何后端发布订阅场景热衷 XMPP，它真适合用来做 RPC 吗？ | 39 | 31 | 2008-07-31 |
| 9 | [I have finally seen the Emacs light](https://news.ycombinator.com/item?id=233172) | 作者终于理解 Emacs 的吸引力，分享对传统 IDE 的不满。 | 38 | 78 | 2008-07-01 |
| 10 | [Ask PG/YC: Why a Delaware C-Corp?](https://news.ycombinator.com/item?id=244009) | 律师建议注册 LLC，为何多数创业公司却选择特拉华州 C-Corp？ | 34 | 16 | 2008-07-11 |

### 2008-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Hacking the Nobel Prize Medals](https://news.ycombinator.com/item?id=290969) | 分享化学家把诺奖金牌溶进王水、避免被纳粹掠走的故事。 | 85 | 24 | 2008-08-30 |
| 2 | [Thank goodness we don't have downmods on HN](https://news.ycombinator.com/item?id=290225) | 作者反思踩帖冲动，认为直接忽略低质投稿也有价值。 | 74 | 62 | 2008-08-29 |
| 3 | [Ask HN: What does Ruby have that Python doesn't?](https://news.ycombinator.com/item?id=283639) | 偏爱 Python 的作者想知道，Ruby 究竟有哪些独特吸引力。 | 66 | 221 | 2008-08-22 |
| 4 | [Hackers' Screenshots](https://news.ycombinator.com/item?id=270121) | 再次征集黑客工作截图，看看大家怎样安排自己的编程环境。 | 59 | 98 | 2008-08-07 |
| 5 | [Should I give up?](https://news.ycombinator.com/item?id=275973) | 科研与创业身份互相拉扯，作者求助是否该放弃手头的公司。 | 49 | 47 | 2008-08-14 |
| 6 | [Join us at Hacker News Coffee, Palo Alto, Tuesday at 8:30am](https://news.ycombinator.com/item?id=285623) | 邀请 HN 读者到帕洛阿尔托喝早咖啡，与其他黑客见面交流。 | 47 | 62 | 2008-08-25 |
| 7 | [Ask HN: Favorite websites for intelligent discussion?](https://news.ycombinator.com/item?id=290733) | 除了 HN，还有哪些网站适合理性讨论技术之外的话题？ | 44 | 42 | 2008-08-30 |
| 8 | [Ask HN: What has been your biggest mistake?](https://news.ycombinator.com/item?id=265937) | 你犯过最大的错误是什么，又从中学到了什么？ | 37 | 100 | 2008-08-04 |
| 9 | [So you launched your startup here first (last week, month...). Now how is it doing?](https://news.ycombinator.com/item?id=267166) | 曾在 HN 发布创业项目的人，如今进展如何、遇到了哪些障碍？ | 37 | 36 | 2008-08-05 |
| 10 | [Ask HN: Legal timeline for a successful web startup?](https://news.ycombinator.com/item?id=287317) | 网站从开发到成功经营，何时注册公司、何时处理各项法律事务？ | 37 | 21 | 2008-08-26 |

### 2008-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [I'm out, baby](https://news.ycombinator.com/item?id=300960) | 一位社区成员存够一万五千美元后辞职，准备全职创业。 | 164 | 99 | 2008-09-11 |
| 2 | [Shoestring Budget?  Starting to feel growth issues on your back-end?  Embrace unix and C](https://news.ycombinator.com/item?id=299451) | 一支预算有限的搜索创业团队分享借助 UNIX 和 C 应对增长。 | 140 | 120 | 2008-09-09 |
| 3 | [A hacker's loneliness](https://news.ycombinator.com/item?id=314206) | 作者借“黑客的孤独”反思长时间沉浸电脑与现实关系的距离。 | 70 | 68 | 2008-09-24 |
| 4 | [Non-Hacker News](https://news.ycombinator.com/item?id=312020) | Non-Hacker News 希望把社区讨论氛围延伸到非技术话题。 | 68 | 62 | 2008-09-23 |
| 5 | [Rebuttal to "A hacker's loneliness"](https://news.ycombinator.com/item?id=314830) | 回应“黑客的孤独”，作者重新看待少年时代那些未完成的程序。 | 65 | 37 | 2008-09-25 |
| 6 | [Posterous: I went to etc., can I still work for you?](https://news.ycombinator.com/item?id=313482) | 作者用反讽质疑 Posterous 招聘中强调名校学历的要求。 | 63 | 176 | 2008-09-24 |
| 7 | [Nickb  20k](https://news.ycombinator.com/item?id=292858) | 祝贺 NickB 在 HN 积分突破两万，也感谢他的长期贡献。 | 60 | 28 | 2008-09-02 |
| 8 | [Ask HN: Tips to work on your startup ideas while still having a day job](https://news.ycombinator.com/item?id=299233) | 保留全职工作的同时推进创业点子，有哪些可持续的做法？ | 56 | 37 | 2008-09-09 |
| 9 | [Ask YC: Why is emacs a great editor?](https://news.ycombinator.com/item?id=313025) | 学习两周仍不顺手，作者想知道 Emacs 的优势究竟体现在哪里。 | 50 | 81 | 2008-09-24 |
| 10 | [Ask YC: Intact Medieval Towns?](https://news.ycombinator.com/item?id=294321) | 寻找保存完好的中世纪小镇，想旅行观察未被现代建设覆盖的城市。 | 44 | 60 | 2008-09-03 |

### 2008-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [How to go down with style](https://news.ycombinator.com/item?id=330689) | 以一位 CEO 帮员工妥善离职的经历谈如何体面关闭公司。 | 117 | 32 | 2008-10-13 |
| 2 | [Ask HN: What is the best way to promote your new fancy web application?](https://news.ycombinator.com/item?id=341138) | 准创业者征求推广新 Web 应用的有效方法。 | 113 | 25 | 2008-10-23 |
| 3 | [Rejected from YC last night... got anchor client this morning](https://news.ycombinator.com/item?id=349029) | 刚被 YC 拒绝就拿下关键客户，团队分享从失落转向振奋的经历。 | 93 | 45 | 2008-10-30 |
| 4 | [Ask YC: How to survive grad school?](https://news.ycombinator.com/item?id=348774) | 研究生生涯陷入低谷，曾梦想做科学家的作者向社区求助。 | 86 | 50 | 2008-10-30 |
| 5 | [Obama to eliminate all cap gains taxes for VCs and entrepreneurs](https://news.ycombinator.com/item?id=328841) | 作者关注奥巴马对创业投资资本利得税的提议，并提出质疑。 | 82 | 91 | 2008-10-10 |
| 6 | [YC got a record number of applications this cycle](https://news.ycombinator.com/item?id=336635) | YC 称本轮申请数大幅创新高，潜在创业者似乎仍未被经济形势吓退。 | 79 | 60 | 2008-10-18 |
| 7 | [Ask HN: What if I don't have an idea?](https://news.ycombinator.com/item?id=340086) | 有时间、技术与一些积蓄，却没有创业点子，接下来该做什么？ | 75 | 90 | 2008-10-22 |
| 8 | [Ask HN: Good python code for code reading](https://news.ycombinator.com/item?id=327710) | 想通过阅读优秀源码学习 Python，作者征集值得研读的项目。 | 62 | 22 | 2008-10-09 |
| 9 | [Where did three months go (AKA where've I been?)](https://news.ycombinator.com/item?id=335096) | 一人经营 IT 咨询业务的作者，分享忙碌三个月的近况。 | 61 | 39 | 2008-10-16 |
| 10 | [Ask HN: Is clojure (lisp in JVM) next big thing?](https://news.ycombinator.com/item?id=343594) | 运行在 JVM 上的 Clojure 会成为新热点，甚至代表 Lisp 的未来吗？ | 61 | 80 | 2008-10-25 |

### 2008-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Vote.](https://news.ycombinator.com/item?id=352800) | 一位社区成员呼吁有资格的美国读者参加投票。 | 184 | 289 | 2008-11-04 |
| 2 | [Ask HN: Who's Hiring?](https://news.ycombinator.com/item?id=375410) | 经济衰退期间征集招聘信息，帮助失业人才找到工作。 | 163 | 208 | 2008-11-24 |
| 3 | [My Public Apology](https://news.ycombinator.com/item?id=371638) | 一位用户为自己在 Justin.tv 讨论中的言论公开道歉。 | 151 | 108 | 2008-11-21 |
| 4 | [Tell Hacker News: Throwaway accounts](https://news.ycombinator.com/item?id=360128) | 用户举报疑似用多个临时账号互相刷票的行为。 | 149 | 58 | 2008-11-11 |
| 5 | [CNN/Fox Projection: Obama wins presidential election.](https://news.ycombinator.com/item?id=354165) | CNN 与 Fox 预测奥巴马赢得美国总统选举。 | 145 | 137 | 2008-11-05 |
| 6 | [Ask YC: What would you tell your younger self?](https://news.ycombinator.com/item?id=372573) | 如果能给年轻时的自己一句忠告，你最想说什么？ | 89 | 151 | 2008-11-22 |
| 7 | [Ask HN: Clients are gone, lots of debt, what would you do?](https://news.ycombinator.com/item?id=380377) | 客户流失且背上债务，离职创业的作者请求现实的脱困建议。 | 87 | 65 | 2008-11-29 |
| 8 | [Python+Scipy+Matplotlib vs Matlab?](https://news.ycombinator.com/item?id=363096) | 自学机器学习等领域，Python 科学计算工具能否替代 Matlab？ | 73 | 44 | 2008-11-13 |
| 9 | [ASK HN: Google account disabled. Oh what to do?](https://news.ycombinator.com/item?id=350968) | 谷歌账号突然停用、多个服务失联，作者求助如何找到人工处理。 | 70 | 55 | 2008-11-01 |
| 10 | [Ask HN: List of Hacker Blogs?](https://news.ycombinator.com/item?id=380236) | 想为黑客博客建立话题追踪，作者征集博客与优质链接列表。 | 70 | 45 | 2008-11-29 |

### 2008-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Wow, check out this guy's comment](https://news.ycombinator.com/item?id=412785) | 作者分享一条让自己重新思考金钱与工作动力的博客评论。 | 233 | 101 | 2008-12-29 |
| 2 | [I don't want to work very hard](https://news.ycombinator.com/item?id=394609) | 一位热爱写代码的资深开发者坦言难以维持职场工作动力。 | 224 | 193 | 2008-12-11 |
| 3 | [How do you generate passive income?](https://news.ycombinator.com/item?id=387789) | 征求通过网络、房地产或投资获得被动收入的经验。 | 151 | 146 | 2008-12-06 |
| 4 | [Ask YC: Let's start a Hacker News book club](https://news.ycombinator.com/item?id=407067) | 提议成立 HN 读书会，以定期共读推动阅读和交流。 | 126 | 79 | 2008-12-23 |
| 5 | [Ask HN: How do big web sites roll out new versions?](https://news.ycombinator.com/item?id=411282) | 大型网站如何部署新版本，又怎样避免升级造成服务中断？ | 110 | 44 | 2008-12-27 |
| 6 | [Tell HN: Merry Christmas](https://news.ycombinator.com/item?id=409310) | 向 HN 读者送上圣诞祝福，期待新年实现各自的愿望。 | 90 | 44 | 2008-12-25 |
| 7 | [My new year's resolution is to email my 15 months old son daily](https://news.ycombinator.com/item?id=413073) | 父亲决定每天给幼儿写邮件，保存成长趣事和家庭记忆。 | 71 | 37 | 2008-12-29 |
| 8 | [Can Dropbox Be Trusted?](https://news.ycombinator.com/item?id=389304) | 企业考虑使用 Dropbox，隐私条款中的业务转让安排引发疑虑。 | 67 | 32 | 2008-12-08 |
| 9 | [Ask HN: you're rich, now what?](https://news.ycombinator.com/item?id=398597) | 假设卖掉公司后再也不必为钱工作，你会怎样安排人生？ | 66 | 152 | 2008-12-15 |
| 10 | [Ask YC: Review my startup, Userfly](https://news.ycombinator.com/item?id=390135) | Userfly 记录真实用户浏览过程，作者邀请评测这款行为观察工具。 | 64 | 50 | 2008-12-08 |

### 2009-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [New users: Welcome.  Please read the site guidelines.](https://news.ycombinator.com/item?id=459289) | 欢迎新用户，并提醒发言前阅读社区准则、保持礼貌。 | 532 | 137 | 2009-01-31 |
| 2 | [Add "pwn" before youtube in the url of any youtube video to download it](https://news.ycombinator.com/item?id=458409) | 介绍在 YouTube 链接中加入 pwn 即可下载视频的工具。 | 164 | 53 | 2009-01-30 |
| 3 | [YHackers: Click that "New" link](https://news.ycombinator.com/item?id=445454) | 呼吁用户查看 HN 新帖列表，帮助优质投稿获得关注。 | 157 | 59 | 2009-01-22 |
| 4 | [Congratulations PG on the coming child](https://news.ycombinator.com/item?id=444696) | 社区成员祝贺 Paul Graham 即将迎来孩子，送上对新家庭的祝福。 | 149 | 52 | 2009-01-22 |
| 5 | [Post a possibly good app idea that you have no intention of doing yourself.](https://news.ycombinator.com/item?id=426014) | 把不打算亲自做的应用点子分享出来，作者先提出轻巧绘图工具。 | 123 | 251 | 2009-01-09 |
| 6 | [Ask HN: What is your favorite TED talk?](https://news.ycombinator.com/item?id=442022) | TED 演讲质量参差不齐，作者想收集社区最喜欢的推荐。 | 123 | 80 | 2009-01-20 |
| 7 | [Ask HN: How do you deal with alienation?](https://news.ycombinator.com/item?id=436331) | 逐渐与旧友失联又渴望同伴，高中生求助如何面对社交疏离。 | 108 | 161 | 2009-01-16 |
| 8 | [Ask HN: Best HN threads in '08?](https://news.ycombinator.com/item?id=417782) | 回顾 2008 年，邀请大家挑出最喜欢、最值得重读的 HN 讨论。 | 104 | 16 | 2009-01-02 |
| 9 | [Ask HN: What are some (good) hacker movies?](https://news.ycombinator.com/item?id=450702) | 除了常见片单，还有哪些值得黑客和技术爱好者观看的电影？ | 94 | 181 | 2009-01-26 |
| 10 | [Ask HN: Anyone want to work through SICP together?](https://news.ycombinator.com/item?id=428248) | 寻找一起读 SICP、完成习题的伙伴，用互相督促保持进度。 | 91 | 58 | 2009-01-10 |

### 2009-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Just cashed out for 2M. What now?](https://news.ycombinator.com/item?id=486755) | 作者称出售公司后到账两百万美元，求助如何管理突如其来的财富。 | 148 | 216 | 2009-02-19 |
| 2 | [Ask HN: Would you pay $5/yr for HN?](https://news.ycombinator.com/item?id=467825) | 如果 HN 每年收五美元，是否能改善匿名涌入带来的社区问题？ | 101 | 166 | 2009-02-05 |
| 3 | [Dear HN, I'm worried about us](https://news.ycombinator.com/item?id=465991) | 作者以不同语气表达相近观点，借投票差异担忧 HN 讨论文化。 | 91 | 113 | 2009-02-04 |
| 4 | [Ask HN: Industries Ripe For Disruption?](https://news.ycombinator.com/item?id=475736) | 哪些行业最需要新办法改变，邀请用具体原因说明机会所在。 | 83 | 100 | 2009-02-10 |
| 5 | [Ask HN: Help me make HN work well on the iPhone](https://news.ycombinator.com/item?id=470863) | 邀请社区协助改进 HN 在 iPhone 上的显示和使用体验。 | 80 | 63 | 2009-02-07 |
| 6 | [Ask HN: Emacs users on OS X, what's your setup?](https://news.ycombinator.com/item?id=465858) | Mac 上使用 Emacs，该选哪个版本，又该如何安排快捷键？ | 73 | 65 | 2009-02-04 |
| 7 | [YC Applicants: Q&A with Abby and Ivan Kirigin of Tipjoy](https://news.ycombinator.com/item?id=491374) | 分享 Tipjoy 创始人的问答，帮助 YC 申请者了解项目经历。 | 69 | 10 | 2009-02-23 |
| 8 | [Gaming HN for an Orange Name - A Warning](https://news.ycombinator.com/item?id=467427) | 作者反省追求橙色用户名与平均得分，如何诱发无益的发言习惯。 | 64 | 45 | 2009-02-05 |
| 9 | [Ask HN: Is HN slow for you lately?  Or even not responding?](https://news.ycombinator.com/item?id=468586) | HN 最近变慢甚至无响应，作者想确认其他读者是否也遇到。 | 62 | 56 | 2009-02-05 |
| 10 | [Ask HN: To porn or not to porn?](https://news.ycombinator.com/item?id=461296) | 失去资助创业的工作后，作者在经济压力下纠结是否进入色情业务。 | 60 | 84 | 2009-02-01 |

### 2009-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Why HN is slow lately](https://news.ycombinator.com/item?id=512145) | HN 因日访问人数大涨而变慢，站方说明临时应对措施。 | 270 | 122 | 2009-03-11 |
| 2 | [Ask HN: Has Hacker News been hacked/cracked?](https://news.ycombinator.com/item?id=519433) | 有人似乎能修改 PG 的个人简介，作者询问 HN 是否遭到入侵。 | 107 | 53 | 2009-03-17 |
| 3 | [Ask HN: How can I get up early in the morning?](https://news.ycombinator.com/item?id=525067) | 想把更多时间留给生活，作者征集早起办法，也问早起是否必要。 | 96 | 134 | 2009-03-20 |
| 4 | [Ask HN: how do you process payments?](https://news.ycombinator.com/item?id=526517) | 创业网站如何接入在线收款，哪些支付服务值得选择？ | 95 | 49 | 2009-03-21 |
| 5 | [Ask PG: What is the list of banned sites and why are they banned?](https://news.ycombinator.com/item?id=498910) | 投稿看似成功却对他人不可见，作者追问 HN 屏蔽网站的规则。 | 79 | 49 | 2009-03-01 |
| 6 | [Tell HN: I think I'm quitting my job today](https://news.ycombinator.com/item?id=524837) | 在经济不景气时仍准备辞职，作者把决定拿到社区征求意见。 | 77 | 101 | 2009-03-20 |
| 7 | [What caused that outage](https://news.ycombinator.com/item?id=512801) | 作者解释 HN 约两小时的宕机，称服务器遇到内存容量限制。 | 74 | 62 | 2009-03-12 |
| 8 | [Ask YC:  Anyone actually making money selling ebooks/digital goods?](https://news.ycombinator.com/item?id=516969) | 卖电子书等数字商品真的能赚钱么，邀请有收入经验的人现身说法。 | 74 | 42 | 2009-03-15 |
| 9 | [Ask HN: Any sources on Erlang?](https://news.ycombinator.com/item?id=512291) | 准备学习 Erlang，向社区征集适合入门的资料和资源。 | 73 | 7 | 2009-03-11 |
| 10 | [Ask HN: How many of you (coders) use marijuana?](https://news.ycombinator.com/item?id=509614) | 询问程序员使用大麻的情况，以及它如何影响工作与生活。 | 70 | 105 | 2009-03-10 |

### 2009-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [YC Rejected: Please read.](https://news.ycombinator.com/item?id=550351) | 面向 YC 被拒申请者解释社区无法判定拒绝原因。 | 171 | 31 | 2009-04-07 |
| 2 | [Ask HN: Do you have any code or projects of your own you would like to talk about instead?](https://news.ycombinator.com/item?id=586140) | 邀请读者分享正在开发的项目与代码，让讨论回到技术实践。 | 165 | 102 | 2009-04-30 |
| 3 | ["I never said she stole my money" has 7 different meanings depending on the stressed word](https://news.ycombinator.com/item?id=583555) | 用一句英语的七种重音展示强调位置如何改变含义。 | 154 | 62 | 2009-04-28 |
| 4 | [Ask PG: Cost and effort of running Hacker News?](https://news.ycombinator.com/item?id=562588) | 运营 HN 每月需要多少硬件费用，又要投入多少维护和管理时间？ | 94 | 53 | 2009-04-14 |
| 5 | [Ask HN: Any programmers here that are able to make a living selling their own programs?](https://news.ycombinator.com/item?id=581768) | 有没有靠销售自制软件谋生的程序员，邀请分享产品与经营经验。 | 86 | 57 | 2009-04-27 |
| 6 | [(More Explicit) Advice to Summer Applicants](https://news.ycombinator.com/item?id=543808) | YC 提醒申请者，遇到限时投资条款时可以申请提前面试。 | 83 | 39 | 2009-04-02 |
| 7 | [Tell HN: I didn't get a job due to a failed startup on my resume](https://news.ycombinator.com/item?id=558874) | 作者称失败创业经历反而妨碍求职，分享一次令人失望的招聘结果。 | 76 | 89 | 2009-04-12 |
| 8 | [Ask: Who is Tara Ploughman?](https://news.ycombinator.com/item?id=554889) | 网上到处引用 Tara Ploughman，但她究竟是谁、有什么背景？ | 75 | 36 | 2009-04-09 |
| 9 | [Ask Entrepreneurs: Productivity tips for a chronic procrastinator?](https://news.ycombinator.com/item?id=579979) | 点子写了一大堆却总不动手，长期拖延的作者想改善执行力。 | 72 | 62 | 2009-04-26 |
| 10 | [Ask YC: Innocuous news?](https://news.ycombinator.com/item?id=575815) | 作者看到 HN 异常页面，贴出截图询问网站是否被入侵。 | 70 | 45 | 2009-04-23 |

### 2009-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Zillow is trying to acquire my app + domain for "a couple hundred bucks", advice?](https://news.ycombinator.com/item?id=587881) | Zillow 想用几百美元收购应用和域名，作者求助如何应对报价。 | 145 | 119 | 2009-05-01 |
| 2 | [Ask HN: Why no love for PHP? ](https://news.ycombinator.com/item?id=595860) | 为什么 HN 很少讨论 PHP，是语言评价还是社区偏好造成的？ | 99 | 145 | 2009-05-06 |
| 3 | [Remind HN: Call your mother](https://news.ycombinator.com/item?id=602005) | 母亲节到了，作者提醒忙碌的读者给妈妈打个电话。 | 96 | 18 | 2009-05-10 |
| 4 | [Brainstorm HN: Outlandish Startup Ideas Pool](https://news.ycombinator.com/item?id=602478) | 征集离谱甚至不现实的创业点子，尝试用大胆联想启发可行方案。 | 86 | 203 | 2009-05-10 |
| 5 | [Ask HN: What apps are essential for mac?](https://news.ycombinator.com/item?id=613406) | 第一次购买 MacBook 后，作者寻找编程和安全工作常用的必装应用。 | 84 | 142 | 2009-05-17 |
| 6 | [Ask HN: After SICP, what next?](https://news.ycombinator.com/item?id=610782) | 读完并做过 SICP 之后，下一本书或学习方向该怎么选？ | 78 | 35 | 2009-05-15 |
| 7 | [Ask HN: I'm Tired of Hacking. What Do I Do? Please Advise.](https://news.ycombinator.com/item?id=629040) | 开发网站八年后再也提不起兴趣，作者求助职业倦怠与转向问题。 | 77 | 110 | 2009-05-27 |
| 8 | [Ask HN: Startup founders, would you walk us through a day in the life?](https://news.ycombinator.com/item?id=634986) | 创始人每天怎样分配编码、营销、销售和客服，邀请展示真实日程。 | 76 | 38 | 2009-05-31 |
| 9 | [Ask HN:  "Dumbing yourself down" around your peers?](https://news.ycombinator.com/item?id=613491) | 为了融入同伴而刻意表现得不聪明，会怎样影响自己和人际关系？ | 73 | 111 | 2009-05-17 |
| 10 | [Ask HN: Where do I go from here?](https://news.ycombinator.com/item?id=635192) | 从早年接触编程谈起，作者向信任的社区寻求下一步方向建议。 | 73 | 83 | 2009-05-31 |

### 2009-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [How I Hacked Hacker News (with arc security advisory)](https://news.ycombinator.com/item?id=639976) | 作者披露 HN 登录 Cookie 随机性漏洞及 Arc 3 修复建议。 | 928 | 78 | 2009-06-03 |
| 2 | [Ask HN: good math books](https://news.ycombinator.com/item?id=665029) | 算法基础扎实但数学知识有缺口，作者寻找能补基础的好书。 | 111 | 46 | 2009-06-19 |
| 3 | [Ask HN: what unwanted domain names are you sitting on?](https://news.ycombinator.com/item?id=652952) | 手里闲置着哪些不再想用的域名，作者邀请大家列出来交流。 | 107 | 298 | 2009-06-11 |
| 4 | [Ask HN: Math for hackers.](https://news.ycombinator.com/item?id=672067) | 为想补数学基础的黑客开放教学材料，并征求学习需求。 | 102 | 56 | 2009-06-24 |
| 5 | [Ask HN: What Web apps increase your productivity?](https://news.ycombinator.com/item?id=641332) | 哪些网页应用真正提高生产力，让你觉得工作离不开它？ | 89 | 116 | 2009-06-04 |
| 6 | [Ask HN: Would you guys visit a purely hacker-oriented version of HN?](https://news.ycombinator.com/item?id=655711) | 更聚焦日常写代码的 HN 类社区，会有人愿意来使用吗？ | 84 | 85 | 2009-06-13 |
| 7 | [Ask HN: Technomading?](https://news.ycombinator.com/item?id=658805) | 边旅行边依靠技术工作生活，该如何为这种游牧状态做准备？ | 80 | 57 | 2009-06-15 |
| 8 | [HN suggestion: A larger margin at the bottom of comment pages](https://news.ycombinator.com/item?id=644514) | 建议在评论页底部增加留白，改善长讨论中按空格翻页的体验。 | 76 | 17 | 2009-06-06 |
| 9 | [Remind HN: Father's Day](https://news.ycombinator.com/item?id=667487) | 提醒美国读者父亲节到了，抽时间为父亲做件特别的事。 | 72 | 35 | 2009-06-21 |
| 10 | [Ask HN: Ridiculous Coding Practices by companies you have worked for](https://news.ycombinator.com/item?id=641946) | 征集公司里遇过的荒唐编码规定，例如因为资深员工不懂而禁用面向对象。 | 68 | 134 | 2009-06-04 |

### 2009-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Dear YC: Please stop downvoting thoughtful comments you disagree with.](https://news.ycombinator.com/item?id=721314) | 作者呼吁认真写下的不同意见应得到尊重，别只因不赞同就踩到负分。 | 174 | 111 | 2009-07-24 |
| 2 | [Ask HN: What are you working on?](https://news.ycombinator.com/item?id=700662) | 邀请读者介绍手头项目、工作地点，以及正在投入的事情。 | 136 | 229 | 2009-07-12 |
| 3 | [Tell HN: Please Stop Breaking HTTP Clients](https://news.ycombinator.com/item?id=705095) | 作者报告 HN 的 HTTP 响应头换行问题，称它会破坏合规客户端。 | 124 | 30 | 2009-07-15 |
| 4 | [Have you ever been successful in changing your personality?](https://news.ycombinator.com/item?id=702466) | 总想创业和做开源却难行动，作者询问是否有人成功改变过性格。 | 105 | 80 | 2009-07-13 |
| 5 | [Ask HN: Why Python over Ruby?](https://news.ycombinator.com/item?id=682101) | 为何嵌入式脚本等场景常支持 Python，却较少选择 Ruby？ | 87 | 196 | 2009-07-01 |
| 6 | [You will live for longer than 1% of the entire history of human civilization.](https://news.ycombinator.com/item?id=725086) | 作者用个人寿命占文明史的比例，提醒读者换个尺度看待时间。 | 86 | 65 | 2009-07-27 |
| 7 | [Ask HN: Objecting to stories being killed](https://news.ycombinator.com/item?id=686200) | 投稿被隐藏后能如何提出异议，作者希望保留合适的反馈途径。 | 74 | 53 | 2009-07-03 |
| 8 | [Ask HN: Cash-flow muses](https://news.ycombinator.com/item?id=725125) | 有没有无需持续投入大量时间、却能带来稳定现金流的小生意？ | 71 | 37 | 2009-07-27 |
| 9 | [Ask HN: What to do when your company misses payroll?](https://news.ycombinator.com/item?id=728318) | 公司多次延迟发薪，员工该如何判断处境并保护自己的利益？ | 70 | 59 | 2009-07-28 |
| 10 | ["you should follow me on twitter here" is annoying](https://news.ycombinator.com/item?id=723928) | 作者厌烦文章末尾反复要求关注 Twitter，讨论推广话术的观感。 | 68 | 26 | 2009-07-26 |

### 2009-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who's Hiring? (take 2)](https://news.ycombinator.com/item?id=759452) | 再次征集招聘岗位，帮助 HN 企业与求职者建立联系。 | 202 | 227 | 2009-08-12 |
| 2 | [Please don't use hnreputation](https://news.ycombinator.com/item?id=789469) | 站方要求停用会高频请求服务器的 hnreputation 脚本。 | 199 | 82 | 2009-08-27 |
| 3 | [The Fall of Hacking](https://news.ycombinator.com/item?id=762121) | 作者担忧黑客文化正在消退，邀请有类似感受的人展开讨论。 | 176 | 112 | 2009-08-14 |
| 4 | [Ask HN: What's a Non-Programmer to do?](https://news.ycombinator.com/item?id=779378) | 团队增长不错，非程序员合伙人却觉得贡献不足，该承担哪些工作？ | 152 | 78 | 2009-08-22 |
| 5 | [Ask HN: Where do you live?](https://news.ycombinator.com/item?id=752262) | 作者从萨拉热窝发问，邀请 HN 读者介绍自己居住的城市。 | 112 | 554 | 2009-08-10 |
| 6 | [Post your HN tricks.](https://news.ycombinator.com/item?id=767275) | 集中分享 HN 的隐藏功能和使用技巧，让更多人发现这些入口。 | 88 | 47 | 2009-08-17 |
| 7 | [Rate my startup: PagerDuty.com](https://news.ycombinator.com/item?id=758653) | PagerDuty 汇集监控邮件，用电话和短信通知值班人员，作者征求评价。 | 83 | 80 | 2009-08-12 |
| 8 | [RailsRumble Apps that Deserve to Be Startups](https://news.ycombinator.com/item?id=782428) | 一位 Rails Rumble 参赛者挑选十一件作品，认为它们值得继续创业。 | 80 | 61 | 2009-08-24 |
| 9 | [Ask HN: Best Mathematics book for complete noobie?](https://news.ycombinator.com/item?id=755043) | 学校数学没学好，如今想重新入门，哪本数学书适合真正的新手？ | 78 | 55 | 2009-08-11 |
| 10 | [Nickb missing?](https://news.ycombinator.com/item?id=775507) | NickB 已失联四十多天，朋友希望社区提供他的近况或联系方式。 | 63 | 41 | 2009-08-20 |

### 2009-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Experiment: No Comment Scores](https://news.ycombinator.com/item?id=844979) | HN 试验隐藏评论分数，希望改善随大众投票的氛围。 | 289 | 313 | 2009-09-26 |
| 2 | [IPhone Developers: We use our iPhones in bed, allow us to disable landscape](https://news.ycombinator.com/item?id=842294) | 躺着使用 iPhone 时屏幕频繁旋转，作者希望应用允许锁定竖屏。 | 164 | 54 | 2009-09-24 |
| 3 | [Ask HN:  Am I crazy?](https://news.ycombinator.com/item?id=801208) | 刚毕业且积蓄不多，作者为自己的另类下一步计划征求现实判断。 | 89 | 92 | 2009-09-02 |
| 4 | [Ask HN: Do you create music? Let's hear it!](https://news.ycombinator.com/item?id=833535) | 发现不少黑客也创作音乐，作者邀请大家分享作品、互相听听。 | 89 | 115 | 2009-09-20 |
| 5 | [Ask HN: Best Unix Tricks?](https://news.ycombinator.com/item?id=810518) | 有哪些初见时令人惊喜、此后一直常用的 Unix 小技巧？ | 83 | 103 | 2009-09-08 |
| 6 | [What are you reading?](https://news.ycombinator.com/item?id=797070) | 邀请读者交流最近正在读的书，从社区兴趣中发现新读物。 | 72 | 214 | 2009-09-01 |
| 7 | [Ask HN: Do you think machine consciousness is possible?](https://news.ycombinator.com/item?id=814161) | 准备研究 AI 的作者提出根本疑问：机器有可能产生意识吗？ | 71 | 185 | 2009-09-09 |
| 8 | [Ask HN: Is version control worth learning early on?](https://news.ycombinator.com/item?id=801824) | 刚写出第一个小脚本，就应该开始学习和使用版本控制吗？ | 70 | 80 | 2009-09-03 |
| 9 | [Own up HN: What are your craziest abandoned projects?](https://news.ycombinator.com/item?id=830734) | 回头看那些做到一半才发现不靠谱的项目，哪个最疯狂？ | 64 | 92 | 2009-09-18 |
| 10 | [Ask HN: Orange dot?](https://news.ycombinator.com/item?id=846357) | 评论旁出现的小橙点是什么，是否与消失的评分有关？ | 63 | 58 | 2009-09-27 |

### 2009-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [So...what the hell's wrong with you, Shooter?](https://news.ycombinator.com/item?id=868325) | 用户讲述被误诊为 ALS 等疾病的漫长求医经历。 | 324 | 126 | 2009-10-08 |
| 2 | [Tell HN: Dealing with VCs, my experience](https://news.ycombinator.com/item?id=866299) | 有融资演示和投资机构工作经历的作者，分享与 VC 打交道的经验。 | 183 | 38 | 2009-10-07 |
| 3 | [Ask HN: What source code is worth studying?](https://news.ycombinator.com/item?id=879101) | 哪些项目源码设计出色，值得专门拿来研读和学习？ | 125 | 114 | 2009-10-13 |
| 4 | [Ask HN: What's in your .vimrc file?](https://news.ycombinator.com/item?id=856051) | 邀请 Vim 用户分享 .vimrc 里的实用配置，帮助新手拓展用法。 | 123 | 67 | 2009-10-01 |
| 5 | [Ask HN: What's in your .emacs file?](https://news.ycombinator.com/item?id=855963) | 多年积累的配置意外丢失后，作者征集大家的 Emacs 设置。 | 121 | 52 | 2009-10-01 |
| 6 | [Announcement: YC alumni will help us read applications ](https://news.ycombinator.com/item?id=908513) | YC 宣布校友将协助阅读申请，并说明避免竞争利益冲突的安排。 | 116 | 181 | 2009-10-28 |
| 7 | [Ask HN: do you feel Google search result quality has gone down?](https://news.ycombinator.com/item?id=902999) | 谷歌搜索越来越难找到满意答案了吗，作者想确认其他人的体验。 | 112 | 109 | 2009-10-26 |
| 8 | [Ask YC: Any network gurus want a paid holiday?](https://news.ycombinator.com/item?id=854825) | 巴哈马的学校网络遇到问题，作者邀请网络高手来带薪协助。 | 108 | 34 | 2009-10-01 |
| 9 | [Ask HN: Please name two of your most favorite books.](https://news.ycombinator.com/item?id=875686) | 请各挑两本最喜欢的书，用短书单分享真正珍爱的读物。 | 105 | 227 | 2009-10-12 |
| 10 | [Ask HN: Statistics for hackers?](https://news.ycombinator.com/item?id=902074) | 被音乐生成等应用吸引，作者想寻找适合黑客学习统计的方法。 | 99 | 31 | 2009-10-25 |

### 2009-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [HN Help: I'm lost](https://news.ycombinator.com/item?id=937430) | 一位有知名作品的 HN 老用户匿名倾诉人生迷茫并求助。 | 366 | 261 | 2009-11-12 |
| 2 | [Ask HN: Who's hiring (take 3)?](https://news.ycombinator.com/item?id=952915) | 更新招聘信息，邀请正在招人的公司把机会介绍给社区。 | 162 | 201 | 2009-11-20 |
| 3 | [Tell HN: Can we stop commenting on troll comments?](https://news.ycombinator.com/item?id=935790) | 针对越来越明显的捣乱评论，作者呼吁别再通过回复继续放大它们。 | 156 | 166 | 2009-11-11 |
| 4 | [Tell HN: Four (hopefully) unique and useful start-up tips](https://news.ycombinator.com/item?id=959773) | 创业者希望提供四条更具体、可以实际照做的创业建议。 | 153 | 41 | 2009-11-24 |
| 5 | [40 years ago today...](https://news.ycombinator.com/item?id=921893) | 为 Trevor Blackwell 送上四十岁生日祝福，回望他的人生起点。 | 150 | 37 | 2009-11-04 |
| 6 | [Tell HN: Apple paid my iPhone money, with exceptional service](https://news.ycombinator.com/item?id=935567) | 作者更新苹果应用收入拖欠事件，称款项已付且后续服务出色。 | 143 | 30 | 2009-11-11 |
| 7 | [Ask HN: I want to learn statistics and data mining](https://news.ycombinator.com/item?id=954677) | 预算有限、购书等待又久，作者寻找统计与数据挖掘教材及在线资源。 | 105 | 37 | 2009-11-21 |
| 8 | [Ask HN: how do you avoid burnout and getting taken advantage of?](https://news.ycombinator.com/item?id=939580) | 高强度付出却回报有限，程序员求助如何避免倦怠和被占便宜。 | 92 | 78 | 2009-11-13 |
| 9 | [Ask HN: Can someone refer me to a designer that doesn't suck?](https://news.ycombinator.com/item?id=955918) | 自由开发者苦于设计合作，想找一位真正靠谱的设计师。 | 89 | 71 | 2009-11-22 |
| 10 | [Experiment HN: Idea day](https://news.ycombinator.com/item?id=937032) | 发起点子日：从日常碰到的麻烦中，寻找值得解决的问题。 | 86 | 59 | 2009-11-12 |

### 2009-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: More types of flagging? ](https://news.ycombinator.com/item?id=1006589) | HN 是否该增加更细的举报类型，让反馈介于踩帖与删除之间？ | 132 | 166 | 2009-12-20 |
| 2 | [Merry Christmas everyone](https://news.ycombinator.com/item?id=1014875) | 一句简短的圣诞祝福，向社区所有读者问好。 | 113 | 40 | 2009-12-25 |
| 3 | [Ask HN:  What hosting do you use for personal projects?](https://news.ycombinator.com/item?id=1005067) | 想低成本搭建可自由折腾的个人服务器，大家用什么托管方案？ | 106 | 126 | 2009-12-19 |
| 4 | [Ask HN: Please Review My Project (JS Game Engine)](https://news.ycombinator.com/item?id=986196) | 邀请试用纯 JavaScript 二维网页游戏开发工具，征集项目反馈。 | 103 | 50 | 2009-12-09 |
| 5 | [Ask HN:  What are the best technologies you've worked with this year?](https://news.ycombinator.com/item?id=1005884) | 过去一年有哪些新技术让你爱不释手，又好用在哪里？ | 90 | 82 | 2009-12-20 |
| 6 | [Tell HN: List of HN Subdivisions ](https://news.ycombinator.com/item?id=1024293) | 整理 HN 各类列表和子页面入口，方便发现不熟悉的功能。 | 86 | 22 | 2009-12-31 |
| 7 | [Ask HN: Equity for a first employee](https://news.ycombinator.com/item?id=973060) | 两个非技术创始人刚拿到种子资金，首位工程师该分多少股权？ | 80 | 38 | 2009-12-02 |
| 8 | [Ask HN: As an employer, what do you wish applicants did more often?](https://news.ycombinator.com/item?id=973803) | 求职者想从雇主角度了解：申请人还可以多做些什么？ | 74 | 50 | 2009-12-03 |
| 9 | [Merry Christmas & a very happy 2010 HN](https://news.ycombinator.com/item?id=1013709) | 回望动荡的 2009 年，向认识与不认识的 HN 读者送上新年祝愿。 | 74 | 21 | 2009-12-24 |
| 10 | [Ask HN: alternatives to EtherPad?](https://news.ycombinator.com/item?id=977107) | 需要在博客中协作写作，作者寻找能替代 EtherPad 的工具。 | 71 | 59 | 2009-12-04 |

### 2010-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: I made $24k over the last month. Now what?](https://news.ycombinator.com/item?id=1060019) | 应用销售一个月收入两万四千美元，作者想把短期现金流变成长久财富。 | 132 | 199 | 2010-01-18 |
| 2 | [Ask HN: Great books you read in 2009?](https://news.ycombinator.com/item?id=1026296) | 邀请读者推荐 2009 年读过、最愿意再介绍给别人的好书。 | 125 | 138 | 2010-01-01 |
| 3 | [Ask PG: What have I done wrong?](https://news.ycombinator.com/item?id=1054819) | 发现自己的投票似乎不再生效，作者向 PG 询问原因。 | 123 | 179 | 2010-01-15 |
| 4 | [Ask HN: What are you working on?](https://news.ycombinator.com/item?id=1032699) | 新年再问大家正在做什么，看看旧项目和新计划各自推进到哪里。 | 114 | 249 | 2010-01-05 |
| 5 | [Ask HN: Looking for interns / entry level?](https://news.ycombinator.com/item?id=1089829) | 为暑期实习和入门岗位搭桥，让看重潜力的公司遇见经验较少的人。 | 113 | 102 | 2010-01-31 |
| 6 | [Greasemonkey script to remove iPad stories from HN](https://news.ycombinator.com/item?id=1085721) | 分享过滤 HN 上 iPad 新闻的脚本，也提供过滤 Lisp 等话题的版本。 | 111 | 13 | 2010-01-29 |
| 7 | [How You Can Directly Help Haiti](https://news.ycombinator.com/item?id=1051914) | 有非营利组织经历的创业者，说明普通人可以怎样直接帮助海地。 | 110 | 28 | 2010-01-14 |
| 8 | [Tell HN: Why you should submit your stuff as a blog posting](https://news.ycombinator.com/item?id=1076633) | 作者认为纯文字帖在 HN 获得曝光较难，建议把内容写成博客再投稿。 | 93 | 13 | 2010-01-26 |
| 9 | [Ask HN: A New Decade. Any Predictions?](https://news.ycombinator.com/item?id=1025681) | 从预测一年扩展到十年，邀请大家畅想 2010 至 2019 年的变化。 | 75 | 189 | 2010-01-01 |
| 10 | [Ask HN: What's your favorite scientific paper?](https://news.ycombinator.com/item?id=1059478) | 征集各领域最喜欢的科学论文，特别欢迎优秀但不太知名的作品。 | 67 | 40 | 2010-01-18 |

### 2010-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [I need to find out how to finish anything I start. Help me. Please.](https://news.ycombinator.com/item?id=1139185) | 开头总有创意、结尾却遥遥无期，作者求助如何把开始的事做完。 | 251 | 165 | 2010-02-20 |
| 2 | [Ask HN: Propaganda for creative salary manipulation?](https://news.ycombinator.com/item?id=1097188) | 鼓吹好团队和有意义的项目，会不会成为压低程序员薪资的话术？ | 152 | 144 | 2010-02-03 |
| 3 | [Ask HN: improving your design skills?](https://news.ycombinator.com/item?id=1103578) | 网站常被批评难看，自己却看不出问题，开发者该怎样提升设计能力？ | 140 | 80 | 2010-02-05 |
| 4 | [Ask HN: Who's Hiring?](https://news.ycombinator.com/item?id=1103801) | 邀请正在寻找黑客与开发者的公司介绍招聘机会。 | 129 | 179 | 2010-02-05 |
| 5 | [Ask HN: Gmail alternatives?](https://news.ycombinator.com/item?id=1121269) | 如果离开 Gmail，有哪些邮箱服务可选，实际体验如何？ | 124 | 137 | 2010-02-12 |
| 6 | [Dear Bay Area HNers: I will cook for you](https://news.ycombinator.com/item?id=1154544) | 到湾区求职的作者愿意下厨做饭，希望借美食结识当地 HN 读者。 | 122 | 34 | 2010-02-27 |
| 7 | [Joel Spolsky to stop blogging; shares insights from JoelOnSoftware success](https://news.ycombinator.com/item?id=1151569) | 转述 Joel Spolsky 停止博客更新的计划，以及他对博客成功的反思。 | 90 | 30 | 2010-02-25 |
| 8 | [Ask HN: Steady 4-5% on $5 million?](https://news.ycombinator.com/item?id=1108163) | 继承约五百万美元后，作者想寻找稳健获得年收益的管理办法。 | 78 | 106 | 2010-02-07 |
| 9 | [Tell HN: Enabling buzz exposes your full name and contact list on google profile](https://news.ycombinator.com/item?id=1114338) | 作者提醒启用 Google Buzz 可能公开姓名和联系人，并指出设置入口。 | 75 | 20 | 2010-02-10 |
| 10 | [Ask HN: What are you working on tonight?](https://news.ycombinator.com/item?id=1152277) | 今晚你在做什么，作者先分享为主项目制作自用待办工具的计划。 | 75 | 234 | 2010-02-26 |

### 2010-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Congratulations Patrick](https://news.ycombinator.com/item?id=1230156) | 社区祝贺 Patrick McKenzie 辞去日本工作、全职经营软件业务。 | 400 | 61 | 2010-03-30 |
| 2 | [Ask HN: Fastest way to make $300-400 a month online?](https://news.ycombinator.com/item?id=1171520) | 一位程序员征求快速在网上月赚三四百美元维持生活的办法。 | 304 | 127 | 2010-03-06 |
| 3 | [Ask HN: "Basic SEO"?](https://news.ycombinator.com/item?id=1176294) | 人们常挂在嘴边的“基础 SEO”，到底包括哪些具体操作？ | 208 | 57 | 2010-03-08 |
| 4 | [Ask HN: Cool Things You've Done (Brag Thread)](https://news.ycombinator.com/item?id=1200959) | 开一个可以自豪的帖子，邀请大家分享做过的独特、有趣的事。 | 200 | 238 | 2010-03-18 |
| 5 | [Tell HN: Thank you](https://news.ycombinator.com/item?id=1188046) | Mixergy 作者感谢 HN 的反馈，认为社区帮助他改进了工作。 | 178 | 64 | 2010-03-12 |
| 6 | [Ask HN: Who's hiring?](https://news.ycombinator.com/item?id=1215633) | 距离上次招聘帖已过一段时间，再次征集公司的最新职位。 | 154 | 193 | 2010-03-24 |
| 7 | [Ask HN: Interesting (Non software) books?](https://news.ycombinator.com/item?id=1226736) | 有哪些不谈软件、却同样值得 HN 读者阅读的好书？ | 118 | 182 | 2010-03-29 |
| 8 | [Tell HN : Wordpress.com exploit](https://news.ycombinator.com/item?id=1204217) | 作者报告 WordPress.com 的登录安全疑点，称外站可能取得登录凭据。 | 110 | 57 | 2010-03-19 |
| 9 | [Ask HN: What's the most simple way to accept monthly subscription fees?](https://news.ycombinator.com/item?id=1206993) | 网页应用要按月收订阅费，有没有简单的计费与代办工具？ | 109 | 54 | 2010-03-20 |
| 10 | [Tell HN: Best OS X Utility for programmers who use the command line](https://news.ycombinator.com/item?id=1157864) | 推荐 DTerm：从当前文件所在目录快速打开命令行，方便 Mac 开发。 | 108 | 58 | 2010-03-01 |

### 2010-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [HN Contractors: Add Yourself](https://news.ycombinator.com/item?id=1262467) | 邀请 HN 的合同工登记自己，方便社区寻找自由职业合作伙伴。 | 222 | 65 | 2010-04-13 |
| 2 | [Ask HN: Are you happy, well-rounded? (dealing w/ depression/lack of motivation)](https://news.ycombinator.com/item?id=1246200) | 二十多岁的作者谈情绪与动力低谷，询问怎样生活得快乐而完整。 | 201 | 138 | 2010-04-07 |
| 3 | [Ask HN: Who's Hiring?](https://news.ycombinator.com/item?id=1308582) | 又到招聘信息更新时间，邀请公司说明职位、地点与用人需求。 | 161 | 169 | 2010-04-30 |
| 4 | [Ask HN: got any food hacks?](https://news.ycombinator.com/item?id=1237939) | 怎样兼顾健康、便宜、快捷和好吃，摆脱速食依赖又不耗时下厨？ | 133 | 165 | 2010-04-03 |
| 5 | [Tell HN: Threads fast](https://news.ycombinator.com/item?id=1291486) | HN 重写 threads 页面生成逻辑，希望改善重启后首次访问缓慢。 | 132 | 26 | 2010-04-24 |
| 6 | [Ask HN: Are you an information addict?](https://news.ycombinator.com/item?id=1293262) | 频繁刷手机、新闻和邮件算信息成瘾吗，大家如何减少这种干扰？ | 121 | 59 | 2010-04-25 |
| 7 | [Tell HN: I got screwed by my employer](https://news.ycombinator.com/item?id=1297890) | 作者讲述受雇期间业余创业引发的纠纷，提醒注意与雇主的关系。 | 116 | 120 | 2010-04-27 |
| 8 | [Ask HN: I could use a few more Erlang/Lisp/Scala/Node.js/Haskell articles please](https://news.ycombinator.com/item?id=1288942) | 创业话题太多，作者希望社区多投稿 Erlang、Lisp 等更硬核的技术文章。 | 112 | 15 | 2010-04-23 |
| 9 | [Largest photo site in the world looking for HNers (Facebook job post)](https://news.ycombinator.com/item?id=1303647) | Facebook 照片业务面向 HN 招聘，邀请工程师关注大规模图片产品。 | 107 | 22 | 2010-04-29 |
| 10 | [Ask HN: Who's hiring?](https://news.ycombinator.com/item?id=1255491) | 作者所在公司有新职位，借新一轮招聘帖汇集其他公司的需求。 | 97 | 110 | 2010-04-10 |

### 2010-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [I just launched my bootstrapped startup. Pray for me.](https://news.ycombinator.com/item?id=1336406) | 一位自筹资金的创业者终于上线产品，并向社区寻求鼓励。 | 362 | 247 | 2010-05-11 |
| 2 | [Ask HN: Review my startup - Scribd (YC S06)](https://news.ycombinator.com/item?id=1326047) | Scribd 团队再次邀请批评与评测，希望听到社区对产品的真实意见。 | 220 | 150 | 2010-05-06 |
| 3 | [Ask HN: HN Alternatives?](https://news.ycombinator.com/item?id=1365094) | 除了以新闻为主的 HN，哪里还有适合黑客和创业者日常交流的社区？ | 210 | 88 | 2010-05-20 |
| 4 | [I am a junior angel in Silicon Valley. AMA](https://news.ycombinator.com/item?id=1356140) | 一位硅谷初级天使投资人开放提问，也邀请其他投资者参与交流。 | 193 | 227 | 2010-05-18 |
| 5 | [Ask PG: What's the deal with search on HN?](https://news.ycombinator.com/item?id=1329334) | 为什么 HN 的搜索入口和使用方式常让新人困惑，作者向 PG 发问。 | 159 | 111 | 2010-05-08 |
| 6 | [Ask HN: I sold my company last month for $5m. What do I do with the money?](https://news.ycombinator.com/item?id=1383376) | 二十岁作者称卖公司获得五百万美元，求助如何处理和管理这笔钱。 | 142 | 168 | 2010-05-27 |
| 7 | [Ask HN: What streetsmarts have you learnt?](https://news.ycombinator.com/item?id=1366217) | 书本知识之外，你从真实生活里学到了哪些处世经验？ | 129 | 92 | 2010-05-21 |
| 8 | [Ask HN: Why do I lose interest in every project after 6 months?](https://news.ycombinator.com/item?id=1370410) | 每个项目热衷约半年就失去兴趣，作者想弄清这种循环如何打破。 | 127 | 103 | 2010-05-22 |
| 9 | [Rally HN: help build an independent Privacy Scanner for Facebook](https://news.ycombinator.com/item?id=1347765) | 召集开发者制作 Facebook 独立隐私扫描器，查出默认开放的隐私漏洞。 | 120 | 28 | 2010-05-14 |
| 10 | [China is choking the Internet](https://news.ycombinator.com/item?id=1349843) | 在中国生活的作者描述可访问网站逐渐减少，并表达对网络限制的担忧。 | 109 | 154 | 2010-05-15 |

### 2010-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [To Paul Graham](https://news.ycombinator.com/item?id=1398250) | 一位读者致信 Paul Graham，表达对 HN 简洁设计的看法。 | 647 | 152 | 2010-06-02 |
| 2 | [Ask HN: What were your naivetés in your twenties?](https://news.ycombinator.com/item?id=1474094) | 邀请年长读者回顾二十多岁时的天真想法。 | 391 | 263 | 2010-06-30 |
| 3 | [Google Checkout Nightmare and the $126,000 phone call](https://news.ycombinator.com/item?id=1432107) | 一位商户称 Google Checkout 扣留十二万六千美元款项。 | 330 | 118 | 2010-06-15 |
| 4 | [Ask HN: How to become a millionaire in 3 years?](https://news.ycombinator.com/item?id=1447428) | 读者征求三年内积累一百万美元净资产的办法。 | 313 | 134 | 2010-06-20 |
| 5 | [How I "hacked" Dustin Curtis's Posterous.](https://news.ycombinator.com/item?id=1441997) | 作者称通过伪造发件地址向 Dustin Curtis 的 Posterous 发帖。 | 298 | 115 | 2010-06-18 |
| 6 | [Ask HN: Why do no other laptop manufacturers get it?](https://news.ycombinator.com/item?id=1419896) | 推荐笔记本时总难找 MacBook 的替代品，其他厂商的产品为何难选？ | 236 | 223 | 2010-06-10 |
| 7 | [Ask HN: What's your favorite TED Talk?](https://news.ycombinator.com/item?id=1447418) | 旧推荐已经看了许多，再次征集大家最喜欢的 TED 演讲。 | 195 | 87 | 2010-06-20 |
| 8 | [Forbes 400 Data Shows Paul Graham Is Wrong](https://news.ycombinator.com/item?id=1444212) | 作者借福布斯富豪榜质疑 PG，讨论金融与创业致富的相对地位。 | 192 | 138 | 2010-06-19 |
| 9 | [Last week Apple asked me to remove my app from the App Store. Now I know why.](https://news.ycombinator.com/item?id=1412993) | 苹果要求下架名为 Facetime 的应用，作者把商标通知与新功能联系起来。 | 169 | 63 | 2010-06-08 |
| 10 | [Ask HN: How can I get better at design?](https://news.ycombinator.com/item?id=1474315) | 业余项目也想做得好看，程序员该如何提升基本视觉设计能力？ | 163 | 98 | 2010-06-30 |

### 2010-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN:  Does reading HN ever make you feel like shit?](https://news.ycombinator.com/item?id=1537461) | 一位用户询问阅读 HN 是否也会让他人产生自卑感。 | 441 | 202 | 2010-07-22 |
| 2 | [Ask PG & other successful folks: how did your life change after FU money?](https://news.ycombinator.com/item?id=1511104) | 拥有足够拒绝不想做之事的钱以后，生活会发生哪些意外变化？ | 277 | 174 | 2010-07-13 |
| 3 | [Ask HN: My brain refuses to think, what should I do?](https://news.ycombinator.com/item?id=1545774) | 连简单代码问题都不愿思考，总想寻找分心事，作者求助如何恢复状态。 | 247 | 147 | 2010-07-25 |
| 4 | [Tell HN: I'm launching in 30 days. No matter what. Hold me to it](https://news.ycombinator.com/item?id=1558154) | 作者公开承诺三十天后上线，希望借社区监督推动自己发布。 | 234 | 129 | 2010-07-29 |
| 5 | [Stop complaining and pay programmers more](https://news.ycombinator.com/item?id=1476723) | 面对“好程序员难招”的抱怨，作者主张提高给程序员的薪酬。 | 227 | 272 | 2010-07-01 |
| 6 | [Ask HN: Share a gem. Teach me and you.](https://news.ycombinator.com/item?id=1557119) | 邀请每人贡献一条珍贵经验，让社区成员互相学到实用知识。 | 194 | 300 | 2010-07-29 |
| 7 | [Follow-up to: Did Americans in 1776 have British accents?](https://news.ycombinator.com/item?id=1489723) | 围绕十八世纪美国人的口音，作者补充来自戏剧训练的相关经历。 | 170 | 42 | 2010-07-06 |
| 8 | [Ask HN: What's your most interesting life goal currently?](https://news.ycombinator.com/item?id=1497164) | 你目前最有趣的人生目标是什么，最大的阻碍又在哪里？ | 150 | 415 | 2010-07-08 |
| 9 | [Ask HN: Does anyone still use IRC?](https://news.ycombinator.com/item?id=1561306) | 还有人在用 IRC 吗，作者想找值得加入的服务器和频道。 | 149 | 135 | 2010-07-30 |
| 10 | [Ask HN: Please, help me understand what I am doing wrong.](https://news.ycombinator.com/item?id=1551121) | 感觉自己陷入停滞和内心冲突，作者尝试描述困境并寻求帮助。 | 147 | 144 | 2010-07-27 |

### 2010-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: I'm a Linux guy. Tell me about all those BSDs](https://news.ycombinator.com/item?id=1569559) | 长期使用 Linux 的作者，希望了解各个 BSD 系统的特点和实际体验。 | 208 | 161 | 2010-08-02 |
| 2 | [Ask HN: All startup websites look the same](https://news.ycombinator.com/item?id=1604693) | 白底、单一主色的创业网站越来越像，作者想讨论这种设计趋同。 | 165 | 82 | 2010-08-15 |
| 3 | [Ask HN: Best Startup City - Outside the USA?](https://news.ycombinator.com/item?id=1565375) | 如果无法去美国，哪些城市最适合创业并建立人脉？ | 158 | 283 | 2010-08-01 |
| 4 | [Ask HN: Did you ever do anything unethical to get your startup off the ground?](https://news.ycombinator.com/item?id=1589257) | 为了让创业项目起步，你是否曾做过后来觉得不合道德的事？ | 158 | 122 | 2010-08-09 |
| 5 | [Ask HN: How to be successful online without SEO bullshittery?](https://news.ycombinator.com/item?id=1648594) | 长期认真写内容却难获关注，作者求助如何不靠 SEO 套路取得成功。 | 149 | 61 | 2010-08-31 |
| 6 | [Ask HN: Tips for Hackers having Kids?](https://news.ycombinator.com/item?id=1597144) | 孩子即将出生，习惯长时间工作的黑客该如何准备成为父母？ | 136 | 130 | 2010-08-12 |
| 7 | [Ask HN: Where do you host your webapp?](https://news.ycombinator.com/item?id=1564897) | 你的网页应用托管在哪里，正在使用哪家服务商？ | 135 | 135 | 2010-08-01 |
| 8 | [Ask PG: Why do you think Africa cannot produce global scale start ups?](https://news.ycombinator.com/item?id=1605657) | 尼日利亚创业者追问 PG：为何认为非洲难以诞生全球规模的创业公司？ | 130 | 85 | 2010-08-15 |
| 9 | [Ask HN: Recommend me a Podcast](https://news.ycombinator.com/item?id=1565140) | 通勤时间变长后节目不够听，作者征集值得推荐的播客。 | 127 | 141 | 2010-08-01 |
| 10 | [Ask HN: What Vim Plugins do you use?](https://news.ycombinator.com/item?id=1590713) | 刚换到 Vim 的作者想了解大家最常用、最喜欢的插件。 | 127 | 48 | 2010-08-10 |

### 2010-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Start ups, please don't force me to log in with Facebook](https://news.ycombinator.com/item?id=1732411) | 用户呼吁创业公司提供 Facebook 登录之外的认证选择。 | 508 | 266 | 2010-09-27 |
| 2 | [Ask HN: Offer of Employment retracted](https://news.ycombinator.com/item?id=1717733) | 已签约并准备入职，招聘承诺却被撤回，作者分享遭遇并求助。 | 271 | 158 | 2010-09-22 |
| 3 | [Ask HN: My startup failed. $9k in debt and need to pay most of it in 12 days.](https://news.ycombinator.com/item?id=1724247) | 创业失败留下服务器与律师债务，短期还款压力下该怎样处理？ | 180 | 157 | 2010-09-24 |
| 4 | [Ask HN: Who's hiring? (September 2010)](https://news.ycombinator.com/item?id=1659409) | 汇集 2010 年九月招聘机会，作者尤其关注伦敦的职位。 | 176 | 236 | 2010-09-03 |
| 5 | [Ask HN: What do you want to tell Microsoft?](https://news.ycombinator.com/item?id=1700623) | 有机会把反馈交给微软管理层，作者征集大家想对微软说的话。 | 164 | 375 | 2010-09-17 |
| 6 | [Need a Job? Build Something Cool.](https://news.ycombinator.com/item?id=1679845) | YouTube Instant 获创始人关注并引来工作邀约，作者借此鼓励做出作品。 | 154 | 63 | 2010-09-10 |
| 7 | [Ask HN: What's the big deal with startups anyways...](https://news.ycombinator.com/item?id=1708413) | 从父母稳定的职业道路出发，作者追问创业为何如此吸引人。 | 154 | 155 | 2010-09-20 |
| 8 | [Ask HN: What habits made you a better programmer?](https://news.ycombinator.com/item?id=1674103) | 哪些习惯真正让你成为更好的程序员，包括思考与克服阻力的方法？ | 138 | 98 | 2010-09-09 |
| 9 | [Ask HN: Is being an introvert okay?](https://news.ycombinator.com/item?id=1730202) | 只和兴趣相近者聊得来，大学生担忧社交退步：内向可以被接受吗？ | 138 | 92 | 2010-09-26 |
| 10 | [Ask HN: Best resources to learn SEO?](https://news.ycombinator.com/item?id=1676091) | 学生创业者想学 SEO，昂贵课程是否值得，又有哪些替代资源？ | 135 | 46 | 2010-09-09 |

### 2010-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Thank HN: 7 months ago, I asked for help. Now I've got 5 employees.](https://news.ycombinator.com/item?id=1772205) | 曾求助生活费的用户感谢 HN，七个月后已雇用五名员工。 | 620 | 114 | 2010-10-08 |
| 2 | [Tell HN: Please continue offering your services (goods, rooms etc)](https://news.ycombinator.com/item?id=1840143) | 用户主张继续允许社区成员发布服务与物品援助信息。 | 461 | 31 | 2010-10-27 |
| 3 | [Tell HN: Please stop offering your services](https://news.ycombinator.com/item?id=1839723) | 用户认为大规模发布服务推介不可持续，呼吁停止此类帖子。 | 406 | 106 | 2010-10-27 |
| 4 | [After 4 years of self-funded coding marathons I feel "finished", care to talk?](https://news.ycombinator.com/item?id=1817883) | 一位自费创业四年的程序员陷入低谷，向社区寻求支持。 | 379 | 184 | 2010-10-21 |
| 5 | [Tell HN: Your social widgets are losing you visitors right now](https://news.ycombinator.com/item?id=1771607) | 作者提醒同步加载的社交按钮会拖慢网页，可能直接赶走访客。 | 306 | 73 | 2010-10-08 |
| 6 | [Founders who can't code](https://news.ycombinator.com/item?id=1761530) | 作者建议不懂技术的创始人先花半年学编程，再考虑寻找技术合伙人。 | 250 | 114 | 2010-10-05 |
| 7 | [Ask HN: Do we no longer support our members?](https://news.ycombinator.com/item?id=1801727) | 看到成员介绍自己的项目却被隐藏，作者担忧社区是否失去支持同伴的意愿。 | 246 | 117 | 2010-10-17 |
| 8 | [Ask HN: Tools of the trade, 2010 edition](https://news.ycombinator.com/item?id=1769910) | 从自行维护服务器到使用 SaaS，2010 年创业团队都在用哪些工具？ | 240 | 92 | 2010-10-07 |
| 9 | [Ask PG: Lisp vs Python (2010)](https://news.ycombinator.com/item?id=1803351) | 看到老 Lisp 用户转向 Python，作者向 PG 询问两种语言如今的取舍。 | 232 | 192 | 2010-10-18 |
| 10 | [Ask HN: Side Projects Gone Big](https://news.ycombinator.com/item?id=1772224) | 哪些为了好玩启动的业余项目，最终成长成了有收入的生意？ | 229 | 155 | 2010-10-08 |

### 2010-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Remind HN: Vote](https://news.ycombinator.com/item?id=1859796) | 在美国选举日提醒读者抽空行使投票权。 | 454 | 382 | 2010-11-02 |
| 2 | [Do you read HackerNews all day and never actually do anything?](https://news.ycombinator.com/item?id=1917274) | 用户反思整天读 HN 却没有真正动手做项目的习惯。 | 389 | 142 | 2010-11-18 |
| 3 | [Who is living off their startup fulltime?](https://news.ycombinator.com/item?id=1924909) | 有没有人已经全职依靠创业生活，是业务自养还是融资支持？ | 254 | 182 | 2010-11-20 |
| 4 | ["Rate My Startup" Post Policy](https://news.ycombinator.com/item?id=1861577) | “评价我的创业项目”投稿增多后，HN 讨论该如何制定发布规则。 | 224 | 134 | 2010-11-02 |
| 5 | [If you applied to YC this cycle, please put your email in your profile](https://news.ycombinator.com/item?id=1862616) | 再次提醒 YC 申请者在个人资料中填写邮箱，确保能收到联系。 | 221 | 55 | 2010-11-02 |
| 6 | [Ask HN: Who Is Hiring Remote Workers? (First Edition, November 2010)](https://news.ycombinator.com/item?id=1857051) | 专门征集远程岗位，方便只考虑异地协作的求职者寻找机会。 | 213 | 85 | 2010-11-01 |
| 7 | [Nerds in Mourning: A friend, father, and founder leaves us](https://news.ycombinator.com/item?id=1861964) | 社区悼念 The Nerdery 创始人 Luke Bucklin 及遭遇空难的家人。 | 213 | 50 | 2010-11-02 |
| 8 | [Thank You, HN](https://news.ycombinator.com/item?id=1865016) | 面对空难悼念帖获得的支持，作者感谢 HN 对遇难者家庭的关心。 | 190 | 4 | 2010-11-03 |
| 9 | [Which programming book you just couldn’t stop reading from start to end?](https://news.ycombinator.com/item?id=1944913) | 哪本编程书让你读起来停不下来，愿意从头一口气看到尾？ | 184 | 146 | 2010-11-27 |
| 10 | [Ask HN: Who Is Hiring? (November 2010 Edition)](https://news.ycombinator.com/item?id=1855569) | 汇总 2010 年十一月职位，要求明确工作地点及能否远程。 | 157 | 127 | 2010-11-01 |

### 2010-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: I built a site that just went ridiculously viral. What do I do now?](https://news.ycombinator.com/item?id=2051288) | threewords.me 突然爆红，开发者求助如何应对成本与后续发展。 | 370 | 188 | 2010-12-30 |
| 2 | [Thanks HN: Goodbye, Golden Handcuffs](https://news.ycombinator.com/item?id=1960437) | 对安全却乏味的大公司工作失望，作者感谢 HN 帮自己告别“金手铐”。 | 347 | 115 | 2010-12-02 |
| 3 | [Merry Christmas HN](https://news.ycombinator.com/item?id=2034624) | 趁假期离线前向社区道一声圣诞快乐，也感谢一年里的学习收获。 | 283 | 113 | 2010-12-23 |
| 4 | [Ask HN: Best book you read in 2010 and briefly why](https://news.ycombinator.com/item?id=1973516) | 2010 年读到最好的书是哪本，能否简单说说它好在哪里？ | 258 | 202 | 2010-12-06 |
| 5 | [Ask HN: What are the best technologies you've worked with this year?](https://news.ycombinator.com/item?id=2053956) | 回顾这一年用过的新技术，邀请分享最喜欢的工具及原因。 | 253 | 149 | 2010-12-30 |
| 6 | [Plea HN: Any work?](https://news.ycombinator.com/item?id=1970094) | 为创业换了低薪工作后妻子又失业，作者急寻工作以维持家庭开支。 | 234 | 48 | 2010-12-04 |
| 7 | [Ask HN: Who's Hiring? (December 2010 Edition)](https://news.ycombinator.com/item?id=1957538) | 十二月招聘集中帖，邀请公司写清职位所在地点和远程可能性。 | 179 | 162 | 2010-12-01 |
| 8 | [Ask HN: How do you cope with loneliness?](https://news.ycombinator.com/item?id=1994671) | 兴趣相近的同伴太少，常与电脑独处的人该如何应对孤独？ | 158 | 77 | 2010-12-11 |
| 9 | [Important Safety Notice from WakeMate](https://news.ycombinator.com/item?id=2054847) | 转发 WakeMate 安全通知：随产品附带的黑色 USB 充电器存在缺陷。 | 152 | 107 | 2010-12-31 |
| 10 | [Ask HN: How would you deal with DDoS?](https://news.ycombinator.com/item?id=1986728) | 近期多起服务遭攻击，作者征集实际应对 DDoS 的方法。 | 129 | 65 | 2010-12-09 |

### 2011-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Google algorithm change launched](https://news.ycombinator.com/item?id=2152286) | Google 调整算法，旨在降低采集站排名并优先展示原创来源。 | 688 | 183 | 2011-01-28 |
| 2 | [Dear Google: please let me ban sites from results](https://news.ycombinator.com/item?id=2075049) | 用户请求 Google 提供跨浏览器屏蔽指定搜索来源的功能。 | 438 | 208 | 2011-01-06 |
| 3 | [Ask HN/PG: Why are comments being paginated?](https://news.ycombinator.com/item?id=2118325) | HN 为何开始分页显示评论，这会不会让后面的讨论更难被看到？ | 341 | 114 | 2011-01-19 |
| 4 | [Tell HN: There is a Scammer Amongst Us](https://news.ycombinator.com/item?id=2163559) | 作者称自己协助追查诈骗后遭到网络诽谤，提醒社区注意相关纠纷。 | 333 | 75 | 2011-01-31 |
| 5 | [Easing into SICP](https://news.ycombinator.com/item?id=2115756) | 觉得 SICP 太密集难读，作者建议先用其他教材逐步适应核心概念。 | 299 | 46 | 2011-01-18 |
| 6 | [Ask HN: Who's Hiring? (February 2011 Edition)](https://news.ycombinator.com/item?id=2161360) | 二月招聘信息交流帖，请雇主明确位置和是否接受远程办公。 | 218 | 242 | 2011-01-31 |
| 7 | [Ask HN: What's your favorite bookmarked HN thread?](https://news.ycombinator.com/item?id=2158116) | 你的收藏夹里保存了哪些 HN 讨论，最喜欢重读哪一帖？ | 197 | 42 | 2011-01-30 |
| 8 | [Ask HN: Do you meditate? How/Why? ](https://news.ycombinator.com/item?id=2125115) | 冥想能否帮助减轻工作压力，邀请大家分享练习方式与动机。 | 184 | 118 | 2011-01-20 |
| 9 | [Ask HN: Who's Hiring? (January 2011 Edition)](https://news.ycombinator.com/item?id=2057704) | 新年第一轮招聘汇总，方便想重新出发的人发现职位。 | 170 | 157 | 2011-01-01 |
| 10 | [HN: I'm building a TC alternative. Will you share your startup's story with me? ](https://news.ycombinator.com/item?id=2153038) | 作者想做更关注早期创业的科技媒体，邀请创业者分享自己的故事。 | 157 | 59 | 2011-01-28 |

### 2011-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [How we fed ourselves for a year & sold a startup...with only 300 lines of code](https://news.ycombinator.com/item?id=2222522) | 作者分享凭三百行代码维持一年生计并出售项目的经历。 | 488 | 109 | 2011-02-15 |
| 2 | [What it's like in Egypt: An email from my mom](https://news.ycombinator.com/item?id=2170560) | 转贴在开罗探亲的母亲来信，从家人的见闻了解埃及当时的局势。 | 238 | 56 | 2011-02-02 |
| 3 | [I'm a cargo cult programmer, help me](https://news.ycombinator.com/item?id=2262527) | 担心自己只会照搬代码，作者求助如何摆脱“货物崇拜式”编程。 | 202 | 158 | 2011-02-25 |
| 4 | [Joyent: 54+ hours of downtime](https://news.ycombinator.com/item?id=2269329) | Joyent 用户称服务器中断超过五十四小时，客户网站和邮件受影响。 | 190 | 120 | 2011-02-27 |
| 5 | [I pitched YC, was rejected, just closed a multi-million dollar round.](https://news.ycombinator.com/item?id=2178339) | 曾被 YC 拒绝的创始人称刚完成数百万美元融资，分享后续经历。 | 186 | 49 | 2011-02-04 |
| 6 | [Warn HN: How to accidentally, irreversibly nuke your Facebook account](https://news.ycombinator.com/item?id=2256150) | 作者警告，设置 Facebook 应用测试账号的操作可能不可逆地毁掉原账号。 | 159 | 60 | 2011-02-23 |
| 7 | [Ask HN: How Many of You Are Like Me?](https://news.ycombinator.com/item?id=2214051) | 多年阅读却很少发言，作者想知道社区还有多少类似的潜水读者。 | 156 | 133 | 2011-02-13 |
| 8 | [Ask HN: Is TDD/BDD hampering your startup's agility?](https://news.ycombinator.com/item?id=2240595) | 创业需求快速变化时，TDD 与 BDD 是否反而拖慢团队的敏捷性？ | 156 | 122 | 2011-02-20 |
| 9 | [Ask HN: Who Is Hiring (For Freelance/Part Time Remote Work) February 2011.](https://news.ycombinator.com/item?id=2216921) | 为有全职工作的人汇集自由职业、兼职和远程合作机会。 | 137 | 57 | 2011-02-14 |
| 10 | [Tell HN: Our VC turned the process of getting acquired into a nightmare](https://news.ycombinator.com/item?id=2273458) | 作者讲述收购过程中与 VC 的冲突，称原本的交易被变成噩梦。 | 134 | 48 | 2011-02-28 |

### 2011-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Peter Tattam created Trumpet Winsock and got very little: Let's set things right](https://news.ycombinator.com/item?id=2282875) | 关注 Trumpet Winsock 作者 Peter Tattam 的回报，呼吁补上支持与感谢。 | 469 | 154 | 2011-03-03 |
| 2 | [Ask HN: Should we agree that this account will submit all Who is Hiring posts?](https://news.ycombinator.com/item?id=2391828) | 建议由固定账号每月自动发布招聘系列帖，避免分散和遗漏。 | 294 | 46 | 2011-03-31 |
| 3 | [New Startup Now Pulling In Over $100k in Monthly Revenues](https://news.ycombinator.com/item?id=2318859) | 作者称新公司月收入超过十万美元，鼓励落选者并招募技术伙伴。 | 282 | 81 | 2011-03-13 |
| 4 | [Ask HN: Anyone have a really smart way to organize css?](https://news.ycombinator.com/item?id=2376782) | CSS 按页面位置还是功能组织更清晰，作者征集结构优秀的实例。 | 198 | 119 | 2011-03-28 |
| 5 | [Ask HN: How did you become a hardcore back-end developer?](https://news.ycombinator.com/item?id=2290180) | 从一般开发者到扎实的后端工程师，大家走过怎样的学习路径？ | 188 | 30 | 2011-03-04 |
| 6 | [Ask HN: Are you working on any side projects that make "small/passive" income?](https://news.ycombinator.com/item?id=2358111) | 哪些业余项目带来了小额或被动收入，又花多久赚到第一笔钱？ | 177 | 167 | 2011-03-23 |
| 7 | [Tell HN: just made my first dollar on the Internet from my freemium web app](https://news.ycombinator.com/item?id=2331556) | 免费增值应用首次赚到十二美元，作者分享跨过心理门槛的喜悦。 | 159 | 78 | 2011-03-16 |
| 8 | [Ask HN: What are your best life hacks?](https://news.ycombinator.com/item?id=2318492) | 征集生活中最好用的小窍门，技术和人际交往经验都欢迎。 | 155 | 183 | 2011-03-13 |
| 9 | [Has YC ever funded a company with a Black founder?](https://news.ycombinator.com/item?id=2349477) | YC 是否投过有黑人创始人的公司，作者从代表性问题出发提问。 | 152 | 137 | 2011-03-21 |
| 10 | [Ask HN: I'm an unemployed programmer in SF that will work for minimum wage](https://news.ycombinator.com/item?id=2292916) | 旧金山一位没有正式经验的计算机毕业生，表示愿从最低工资做起。 | 127 | 135 | 2011-03-06 |

### 2011-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [I don't learn anything on HN anymore, bring back the upvote count](https://news.ycombinator.com/item?id=2495137) | 用户认为隐藏赞数降低了学习价值，呼吁恢复显示。 | 1136 | 228 | 2011-04-28 |
| 2 | [Ask HN: How to stave off decline of HN?](https://news.ycombinator.com/item?id=2403696) | 站方征求遏制 HN 评论质量下降与恶意内容获赞的办法。 | 465 | 680 | 2011-04-03 |
| 3 | [Tell HN: Please bring back comment scores](https://news.ycombinator.com/item?id=2485029) | 怀念评论评分的读者建议恢复显示，或用分数区间折中。 | 442 | 164 | 2011-04-26 |
| 4 | [Notice: Experimenting with HN](https://news.ycombinator.com/item?id=2434333) | HN 即将进行几周功能实验，作者提前说明可能出现的界面变化。 | 412 | 209 | 2011-04-11 |
| 5 | [Collect HN: Aprils Fools](https://news.ycombinator.com/item?id=2394349) | 把科技网站的愚人节玩笑集中在一帖，方便浏览也避免刷屏。 | 294 | 224 | 2011-04-01 |
| 6 | [Ask HN: Who is Hiring? (April 2011)](https://news.ycombinator.com/item?id=2396027) | 四月职位集中发布，请说明地点以及是否欢迎实习、远程或签证申请者。 | 285 | 295 | 2011-04-01 |
| 7 | [If you applied to YC this cycle, please put your email address in your profile](https://news.ycombinator.com/item?id=2420344) | YC 即将邮件通知夏季申请结果，提醒检查申请账号里的邮箱字段。 | 275 | 35 | 2011-04-07 |
| 8 | [Ask HN: Why can't I make as much as I make?](https://news.ycombinator.com/item?id=2432778) | 既然能为雇主创造价值，为何自己创业却赚不到同样的钱？ | 262 | 114 | 2011-04-11 |
| 9 | [Thank HN: 127 days since I asked for your advice.](https://news.ycombinator.com/item?id=2471229) | 一百二十七天后，作者回访此前求助帖，感谢帮助自己稳定业务的建议。 | 253 | 44 | 2011-04-21 |
| 10 | [Must Read CS Books For Self Self-Taught Programmers](https://news.ycombinator.com/item?id=2414280) | 自学程序员该读哪些计算机科学书，才能补足日常开发所需的理论？ | 251 | 61 | 2011-04-06 |

### 2011-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: How much recurring income do you generate, and from what?](https://news.ycombinator.com/item?id=2567487) | 你目前有多少经常性收入，分别来自哪些产品、服务或渠道？ | 367 | 306 | 2011-05-20 |
| 2 | [Ask HN: Who is Hiring? (May 2011)](https://news.ycombinator.com/item?id=2503204) | 五月招聘帖，邀请公司标明工作地点和可接受的候选人类型。 | 324 | 291 | 2011-05-01 |
| 3 | [Ask HN: Apart from Hacker News, what else you read?](https://news.ycombinator.com/item?id=2543601) | 除了 Hacker News，你平时还会阅读哪些网站或信息来源？ | 310 | 172 | 2011-05-13 |
| 4 | [Challenge HN: build pg-bot](https://news.ycombinator.com/item?id=2598026) | 发起编程挑战：制作模拟 PG 答疑的聊天机器人，并可公开对话。 | 148 | 39 | 2011-05-30 |
| 5 | [Ask HN: Are freelancer sites (e.g. Odesk, Elance) useless?](https://news.ycombinator.com/item?id=2539892) | 在 Odesk、Elance 等平台发包体验不佳，作者质疑自由职业网站是否管用。 | 116 | 67 | 2011-05-12 |
| 6 | [Ask HN: any of the HNers have kids & work from home?](https://news.ycombinator.com/item?id=2536213) | 寻找既带孩子又在家工作的女性开发者，交流兼顾家庭和职业的办法。 | 112 | 97 | 2011-05-11 |
| 7 | [Run Linux in your Browser JSLinux (Update)](https://news.ycombinator.com/item?id=2572915) | JSLinux 更新加入剪贴板支持，并扩展浏览器和 iPad 上的使用体验。 | 109 | 33 | 2011-05-22 |
| 8 | [Ask HN: Freelancer? Seeking freelancers? (May 2011)](https://news.ycombinator.com/item?id=2503209) | 五月自由职业撮合帖，让求项目和找外援的人说明地点与远程安排。 | 98 | 55 | 2011-05-01 |
| 9 | [Ask HN: How do I minimize the taxes from selling my startup?](https://news.ycombinator.com/item?id=2502623) | 公司成立未满一年即将出售，作者求助如何合理减少出售所得税负。 | 84 | 52 | 2011-05-01 |
| 10 | [HN: I want to trade my finance knowledge for python/django mentorship](https://news.ycombinator.com/item?id=2548621) | 希望找人辅导 Python 和 Django，作者愿用金融知识交换学习帮助。 | 78 | 44 | 2011-05-14 |

### 2011-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Our experience with Groupon](https://news.ycombinator.com/item?id=2654788) | 一位跳伞场经营者分享开展 Groupon 团购促销的经历。 | 562 | 105 | 2011-06-14 |
| 2 | [Ask HN: Who is Hiring? (June 2011)](https://news.ycombinator.com/item?id=2607052) | 六月招聘信息汇总，方便按地点、实习、远程和签证条件筛选。 | 326 | 327 | 2011-06-01 |
| 3 | [Failed entrepreneur, broke, unemployed, now taking care of aging parents. Help.](https://news.ycombinator.com/item?id=2634289) | 创业失败、失业无钱，又要照顾年迈父母，作者请求出路建议。 | 236 | 140 | 2011-06-08 |
| 4 | [Why I won't be using Groupon again.. A consumer perspective. ](https://news.ycombinator.com/item?id=2648720) | 一次餐厅团购体验之后，消费者解释自己为何不再想使用 Groupon。 | 196 | 173 | 2011-06-13 |
| 5 | [Ask HN: What documentaries are worth watching?](https://news.ycombinator.com/item?id=2698026) | 哪些纪录片真正提供了深入认识，值得技术爱好者花时间观看？ | 157 | 152 | 2011-06-26 |
| 6 | [Ask HN: My Startup is Going to Die Because I Messed Up](https://news.ycombinator.com/item?id=2622238) | 借家人的钱创业后陷入危机，年轻作者反省错误并向社区求助。 | 156 | 90 | 2011-06-05 |
| 7 | [Hacker News Job Board?](https://news.ycombinator.com/item?id=2660737) | 提议建立只允许 HN 用户发布的招聘板，讨论这种职位社区的价值。 | 142 | 67 | 2011-06-16 |
| 8 | [Ask HN: Advice for a young, self-taught programmer](https://news.ycombinator.com/item?id=2647301) | 十五岁自学程序员不知道该学什么、怎样学，希望得到方向建议。 | 136 | 73 | 2011-06-12 |
| 9 | [Ask PG: How would you have started Reddit/HN without your existing audience?](https://news.ycombinator.com/item?id=2624086) | 如果没有文章读者作为种子用户，Reddit 和 HN 该如何解决冷启动？ | 131 | 30 | 2011-06-06 |
| 10 | [Ask HN:  Do Americans stand a chance on freelance sites?](https://news.ycombinator.com/item?id=2619423) | 面对低价跨国竞标，美国自由开发者还有机会在接单平台立足吗？ | 122 | 50 | 2011-06-04 |

### 2011-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who is Hiring? (July 2011)](https://news.ycombinator.com/item?id=2719028) | 自动招聘帖似乎缺席，作者补开七月职位帖并延续地点等标注要求。 | 233 | 283 | 2011-07-01 |
| 2 | [Ask HN: Desperate Python Hacker Seeking Help and Suggestions](https://news.ycombinator.com/item?id=2826493) | 熟悉 Python 却迟迟找不到工作，作者在家庭和经济压力下寻求帮助。 | 212 | 181 | 2011-07-30 |
| 3 | [My legitimate co.cc site was deleted from Google, what do I do?](https://news.ycombinator.com/item?id=2734013) | 谷歌移除全部 co.cc 域名后，正常博客也消失，站长该怎么办？ | 189 | 42 | 2011-07-06 |
| 4 | [Ask HN: What has been your most profitable side/weekend project to date?](https://news.ycombinator.com/item?id=2795760) | 到目前为止，哪个业余或周末项目为你赚到了最多的钱？ | 181 | 156 | 2011-07-23 |
| 5 | [Question for PG/HN:  Where do you think we stand on your list of "ideas"?](https://news.ycombinator.com/item?id=2728401) | 回看 PG 三年前的想投项目清单，哪些问题已解决，哪些仍有机会？ | 172 | 103 | 2011-07-05 |
| 6 | [Ask HN: Where is the Django community?](https://news.ycombinator.com/item?id=2777883) | Rails 社区显得很活跃，已有 Django 基础的作者想找到它的交流圈。 | 147 | 155 | 2011-07-18 |
| 7 | [Google's Android Market is crippling small development teams](https://news.ycombinator.com/item?id=2768376) | 小型应用团队讲述 Android Market 带来的经营困难，并质疑平台机制。 | 142 | 77 | 2011-07-15 |
| 8 | [Len Sassaman has passed away](https://news.ycombinator.com/item?id=2723959) | 作者听到 Len Sassaman 去世的消息，希望获得更具体、可靠的情况。 | 135 | 44 | 2011-07-03 |
| 9 | [Hackers to follow on G+?](https://news.ycombinator.com/item?id=2737152) | Google+ 上有哪些值得关注的黑客，除了 Guido 还有谁？ | 103 | 43 | 2011-07-07 |
| 10 | [Offer HN: Free Maths Lessons](https://news.ycombinator.com/item?id=2815996) | 有数学辅导经验的作者，邀请读者参加八周免费数学课程。 | 90 | 46 | 2011-07-28 |

### 2011-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [If Software Is Eating The World, Why Don't Coders Get Any Respect?](https://news.ycombinator.com/item?id=2919708) | 追问软件日益重要，为何程序员未获得相应的尊重。 | 618 | 265 | 2011-08-24 |
| 2 | [Dear procrastinator](https://news.ycombinator.com/item?id=2886187) | 作者致信拖延者，提出拖延不应简单归结为自律不足。 | 560 | 139 | 2011-08-15 |
| 3 | [Warn HN: Lots of Launches Coming](https://news.ycombinator.com/item?id=2862067) | Demo Day 前项目扎堆上线，YC 提醒团队尽量更早发布。 | 428 | 93 | 2011-08-08 |
| 4 | [For the love of God, YC companies-to-be stop posting ambiguous job description](https://news.ycombinator.com/item?id=2879055) | 潜在求职者呼吁 YC 公司把岗位写清楚，别再用模糊描述招关键员工。 | 369 | 93 | 2011-08-12 |
| 5 | [iPhone vs Android app sales: numbers from an indie developer](https://news.ycombinator.com/item?id=2929612) | 独立开发者把畅销 iPhone 应用移植到 Android，分享两端销售数据。 | 292 | 91 | 2011-08-26 |
| 6 | [Ask HN: Who is Hiring? (August 2011)](https://news.ycombinator.com/item?id=2831646) | 八月招聘集中帖，邀请明确职位地点及实习、远程、签证条件。 | 282 | 306 | 2011-08-01 |
| 7 | [Ask HN: How can I do something meaningful?](https://news.ycombinator.com/item?id=2882356) | 被社区讨论激发后，作者追问自己怎样才能做出更有意义的事。 | 278 | 152 | 2011-08-14 |
| 8 | [Ask HN: What is your preferred Python stack for high traffic webservices?](https://news.ycombinator.com/item?id=2910953) | 准备重写遗留系统，高流量网络服务该选择怎样的 Python 技术栈？ | 233 | 67 | 2011-08-22 |
| 9 | [Download.com wrapping downloads](https://news.ycombinator.com/item?id=2910554) | 开发者发现 Download.com 给下载包套上自有安装器，对做法表示不满。 | 174 | 32 | 2011-08-21 |
| 10 | [Why HN Got Slow](https://news.ycombinator.com/item?id=2865985) | HN 因媒体大量链接某条新闻而变慢，作者解释并提到评论分页应对。 | 152 | 58 | 2011-08-09 |

### 2011-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Small product, single founder success stories? ](https://news.ycombinator.com/item?id=3029771) | 寻找单人创办、小产品起步的成功案例，看看不扩团队能走多远。 | 327 | 151 | 2011-09-23 |
| 2 | [Ask HN: How do you promote your web apps?](https://news.ycombinator.com/item?id=2973404) | 新网页应用发布以后，你通常通过哪些方法把它介绍给用户？ | 292 | 77 | 2011-09-08 |
| 3 | [Ask HN: Who is Hiring? (September 2011)](https://news.ycombinator.com/item?id=2949787) | 九月职位交流帖，要求雇主写明地点和适用的招聘条件。 | 249 | 232 | 2011-09-01 |
| 4 | [Ask PG: What has changed since you wrote Hackers and Painters in 2004?](https://news.ycombinator.com/item?id=2982185) | 《黑客与画家》出版多年，作者询问哪些新变化可能修正书中的观点。 | 242 | 85 | 2011-09-10 |
| 5 | [Ask HN: How much did you earn as an employee from an exit?](https://news.ycombinator.com/item?id=2958766) | 作为普通员工加入创业公司，退出时股权最终让你拿到了多少？ | 202 | 110 | 2011-09-04 |
| 6 | [Ask HN: I am wasting so much of time, what can I do?](https://news.ycombinator.com/item?id=2983834) | 任务多、压力大，却仍不断上网耗时，作者请求改善拖延的建议。 | 192 | 79 | 2011-09-11 |
| 7 | [Ask HN: good, quick algorithms course to prepare for big tech interviews?](https://news.ycombinator.com/item?id=3011964) | 工程专业学生准备大厂面试，有没有简洁高效的算法复习课程？ | 143 | 27 | 2011-09-19 |
| 8 | [Ask HN: I think My code isn't Good enough](https://news.ycombinator.com/item?id=2957522) | 编程四五年后仍觉得代码不如别人，作者想知道如何面对和提升。 | 140 | 91 | 2011-09-03 |
| 9 | [Dear Google Marketing (Re: Your kids policy)](https://news.ycombinator.com/item?id=3010687) | 谷歌广告鼓励父亲给孩子写邮件，作者却对实际儿童账号政策提出疑问。 | 128 | 34 | 2011-09-18 |
| 10 | [Ask HN: European startup looking for a service for recurring billing](https://news.ycombinator.com/item?id=3056714) | 美国常用服务尚未覆盖欧洲，欧洲创业公司该选什么周期扣款方案？ | 95 | 67 | 2011-09-30 |

### 2011-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [I quit my job last March and it was a bad idea.](https://news.ycombinator.com/item?id=3102143) | 一位用户分享辞职后的不顺经历，提醒读者考虑另一面。 | 745 | 325 | 2011-10-12 |
| 2 | [Ask HN: What programming blogs do you read daily?](https://news.ycombinator.com/item?id=3120380) | 征集读者每天阅读的编程博客。 | 716 | 116 | 2011-10-17 |
| 3 | [Request PG: Could we please have the black bar out for Steve Jobs?](https://news.ycombinator.com/item?id=3078285) | 乔布斯去世让作者深受震动，请求 HN 用黑色栏表达哀悼。 | 392 | 78 | 2011-10-06 |
| 4 | [Ask HN: Anyone know where Mark Pilgrim went?](https://news.ycombinator.com/item?id=3073798) | Mark Pilgrim 的网站和账号接连消失，读者询问他的近况。 | 305 | 84 | 2011-10-05 |
| 5 | [Ask HN: Who is Hiring? (October 2011)](https://news.ycombinator.com/item?id=3060221) | 十月招聘机会汇总，职位地点与是否支持远程等信息需明确。 | 238 | 273 | 2011-10-01 |
| 6 | [Ask HN: Screwed out of $12.8 million. Being Extorted.  No Money for attorneys.](https://news.ycombinator.com/item?id=3120052) | 安全公司联合创始人称被剥夺巨额收益且遭勒索，无钱请律师而求助。 | 221 | 105 | 2011-10-17 |
| 7 | [Ask PG: Is there any chance of getting points displayed again](https://news.ycombinator.com/item?id=3122233) | 不显示分数让读评论失去参照，作者再次询问能否恢复评论积分。 | 207 | 164 | 2011-10-17 |
| 8 | [Stanford Computer Science '10-'11 Salary Survey Results](https://news.ycombinator.com/item?id=3141716) | 斯坦福学生分享计算机系薪资调查，让社区了解毕业生的收入情况。 | 180 | 71 | 2011-10-21 |
| 9 | [Ask HN: Is brogrammer a sexist term?](https://news.ycombinator.com/item?id=3168038) | 招聘广告里的“brogrammer”是否带有性别歧视，会排斥哪些人？ | 177 | 201 | 2011-10-28 |
| 10 | [Good books for hackers interested in quant finance?](https://news.ycombinator.com/item?id=3177815) | 懂技术但不了解量化金融，哪些书或论文适合作为入门？ | 137 | 59 | 2011-10-31 |

### 2011-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who is Hiring? (November 2011)](https://news.ycombinator.com/item?id=3181796) | 十一月招聘信息帖，欢迎说明岗位、地点以及适用的候选人条件。 | 310 | 294 | 2011-11-01 |
| 2 | [Ask HN: How do you know if you're burnt out or just being lazy?](https://news.ycombinator.com/item?id=3260751) | 不想工作究竟是倦怠还是懒惰，有没有能判断两者的个人标准？ | 203 | 100 | 2011-11-21 |
| 3 | [Tell HN: I want to teach you web development. In 8 weeks. For free (sort of)](https://news.ycombinator.com/item?id=3267133) | 作者计划在湾区带六人从零学 Rails，以八周课程帮助新人入行。 | 195 | 139 | 2011-11-22 |
| 4 | [Ask HN: Startup promised me a job, then backed out after the internship](https://news.ycombinator.com/item?id=3203228) | 欧洲学生完成纽约创业公司实习后，原先承诺的正式工作却被撤回。 | 151 | 88 | 2011-11-06 |
| 5 | [Ask PG: Could we have the SOPA censorship label up on HN's logo today?](https://news.ycombinator.com/item?id=3243187) | 请求 HN 标志加入反 SOPA 审查标签，呼应当天的网络行动。 | 144 | 24 | 2011-11-16 |
| 6 | [Ask HN: What books to read on developing mental models and increasing cognition?](https://news.ycombinator.com/item?id=3277457) | 寻找改善思考模型、减少认知偏差并提高创造与决策能力的书。 | 133 | 41 | 2011-11-25 |
| 7 | [Offer HN: I will work for free this Thursday in San Francisco](https://news.ycombinator.com/item?id=3216323) | 周四在旧金山空闲一整天，作者愿免费帮当地创业公司做事。 | 120 | 17 | 2011-11-09 |
| 8 | [Best approach for self-taught developer looking for job?](https://news.ycombinator.com/item?id=3198628) | 社科毕业后自学编程并找到兴趣，接下来该如何准备开发岗位求职？ | 112 | 59 | 2011-11-05 |
| 9 | [Ask HN: Please stop "This."](https://news.ycombinator.com/item?id=3245365) | 作者觉得评论开头只写“This.”令人烦躁，邀请讨论这种附和习惯。 | 102 | 71 | 2011-11-16 |
| 10 | [If all Rejection Letters could be so nice...](https://news.ycombinator.com/item?id=3180243) | 作者分享一封措辞体贴的 YC 拒信，认为拒绝也可以保有尊重。 | 96 | 51 | 2011-11-01 |

### 2011-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Best book you read in 2011](https://news.ycombinator.com/item?id=3395061) | 回顾 2011 年，邀请大家推荐这一年读过最好的书。 | 336 | 307 | 2011-12-27 |
| 2 | [The real reason you can't hire developers....](https://news.ycombinator.com/item?id=3351699) | 作者认为一些公司招不到开发者，是因为连人才发来的邮件都不回复。 | 324 | 266 | 2011-12-14 |
| 3 | [Ask HN: Who is Hiring? (December 2011)](https://news.ycombinator.com/item?id=3300290) | 自动脚本似乎失效，作者手动发起十二月招聘帖。 | 290 | 251 | 2011-12-01 |
| 4 | [Ask HN: How many of you built a profitable startup while having a day job?](https://news.ycombinator.com/item?id=3303776) | 有多少人保留全职工作，同时做出了能够盈利的创业项目？ | 287 | 188 | 2011-12-02 |
| 5 | [Tell HN: You said not to. So I quit my job and started. 5 mos later: OpenPhoto](https://news.ycombinator.com/item?id=3320615) | 曾被建议别辞职的作者，五个月后带着 OpenPhoto 回来汇报进展。 | 253 | 142 | 2011-12-06 |
| 6 | [Spamhaus Nightmare: Domain Shut Down, No Notice, Over A Million Pages Down](https://news.ycombinator.com/item?id=3408407) | 作者称域名未获通知即被停用、上百万页面下线，求助处理 Spamhaus 纠纷。 | 245 | 95 | 2011-12-30 |
| 7 | [Ask HN: I really need your help (resolved)](https://news.ycombinator.com/item?id=3371938) | MinoMonsters 用户激增、Ruby 后端无痕崩溃，作者紧急求助排障。 | 194 | 36 | 2011-12-20 |
| 8 | [Thanks HN for the Christmas colors and Merry Christmas to you, too](https://news.ycombinator.com/item?id=3389605) | 感谢 HN 换上圣诞配色，也向社区回赠节日祝福。 | 176 | 45 | 2011-12-24 |
| 9 | [Happy New Year!](https://news.ycombinator.com/item?id=3411501) | 新年祝愿创业者迎来客户、收支平衡与退出机会，也祝家人朋友顺利。 | 151 | 49 | 2011-12-31 |
| 10 | [Ask PG: 2012 Startup ideas you'd like to fund?](https://news.ycombinator.com/item?id=3391343) | 2008 年的创业愿望清单已旧，作者询问 PG 在 2012 年想投什么。 | 144 | 32 | 2011-12-25 |

### 2012-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [No New Accounts Today](https://news.ycombinator.com/item?id=3481174) | 因 Reddit 抗议停站带来大量流量，HN 暂停注册以示尊重。 | 718 | 94 | 2012-01-18 |
| 2 | [Ask HN: Who is Hiring? (January 2012)](https://news.ycombinator.com/item?id=3412900) | 2012 年一月招聘帖，请列出地点及实习、远程和签证支持情况。 | 262 | 223 | 2012-01-01 |
| 3 | [Kill Hollywood? Let's fix politics instead: kill lobbying.](https://news.ycombinator.com/item?id=3504304) | 回应“干掉好莱坞”的倡议，作者主张把精力转向政治游说问题。 | 238 | 99 | 2012-01-24 |
| 4 | [Ask HN: Who's looking for employment?](https://news.ycombinator.com/item?id=3467298) | 把“谁在招聘”反过来，邀请正在找工作的人介绍自己。 | 188 | 153 | 2012-01-15 |
| 5 | [Ask HN: How do I start freelancing?](https://news.ycombinator.com/item?id=3525861) | 没有像样作品集就没人愿意雇，网页开发者该如何接到第一单？ | 184 | 53 | 2012-01-29 |
| 6 | [Ask HN: What successful startups started as "Show HN"?](https://news.ycombinator.com/item?id=3526993) | 哪些成功公司最初通过 Show HN 亮相，社区对它们起过什么作用？ | 158 | 39 | 2012-01-30 |
| 7 | [Tell HN: Frustrated and feeling pretty useless at this point.](https://news.ycombinator.com/item?id=3439277) | 再次创业又错失机会，作者讲述挫败感，坦陈自己觉得无用。 | 152 | 106 | 2012-01-08 |
| 8 | [Ask HN: Oops, I just sold my startup to a piano company. Now what? ](https://news.ycombinator.com/item?id=3429376) | 音乐出版平台因法律问题提前卖给钢琴公司，作者询问接下来做什么。 | 151 | 72 | 2012-01-05 |
| 9 | [Ask HN: Why is the "Google, what were you thinking?" link getting killed](https://news.ycombinator.com/item?id=3459966) | 有关谷歌的批评文章不断被标死，作者想弄清 HN 的处理原因。 | 117 | 30 | 2012-01-13 |
| 10 | [Ask HN: Freelancer? Seeking freelancer? (January 2012)](https://news.ycombinator.com/item?id=3412901) | 一月自由职业交流帖，供寻找工作与寻找外援的双方发布需求。 | 112 | 110 | 2012-01-01 |

### 2012-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Iran Shuts Down Major Websites and Https Protocol](https://news.ycombinator.com/item?id=3575029) | 伊朗用户报告主要网站及 HTTPS 访问受阻，描述当时的上网困境。 | 399 | 146 | 2012-02-10 |
| 2 | [Ask HN: Who is Hiring? (February 2012)](https://news.ycombinator.com/item?id=3537881) | 二月招聘汇总，请公司说明地点与远程、实习和签证条件。 | 270 | 230 | 2012-02-01 |
| 3 | [Ask HN: Help a Hacker Out](https://news.ycombinator.com/item?id=3644870) | 失业后搬回母亲家，作者希望在困境固化前获得工作与出路帮助。 | 263 | 94 | 2012-02-28 |
| 4 | [Ask HN: What are the good old ideas that still make money on the web?](https://news.ycombinator.com/item?id=3581791) | 哪些 Web 1.0 时代的老生意，今天仍然能在网上赚到钱？ | 224 | 167 | 2012-02-12 |
| 5 | [We're turning off Clickpass March 15. How to keep your HN account.](https://news.ycombinator.com/item?id=3618082) | Clickpass 登录支持即将停用，HN 提醒相关用户处理邮箱和账号。 | 172 | 64 | 2012-02-21 |
| 6 | [Ask HN: What's the best company to buy SSL certificates from?](https://news.ycombinator.com/item?id=3556796) | 购买 SSL 证书该选哪家公司，哪些供应商更值得信赖？ | 124 | 70 | 2012-02-06 |
| 7 | [Ask HN: JavaScript Dev Tools](https://news.ycombinator.com/item?id=3550998) | 有经验的程序员转向 JavaScript，想了解框架之外还需要哪些开发工具。 | 123 | 77 | 2012-02-04 |
| 8 | [Ask HN: How to move away from Gmail](https://news.ycombinator.com/item?id=3581613) | 想从 Gmail 搬走，作者寻找更尊重隐私的在线邮箱服务。 | 120 | 141 | 2012-02-12 |
| 9 | [Ask HN: Have you taken 6 months to 1 year break to do self study?](https://news.ycombinator.com/item?id=3606827) | 有人曾停工半年至一年，专心自学机器学习等公开课程吗？ | 99 | 80 | 2012-02-18 |
| 10 | [How Do You Find New Problems to Solve or Ideas for Products To Work On?](https://news.ycombinator.com/item?id=3633369) | 新产品的题目从哪里来，你如何一步步发现值得解决的问题？ | 83 | 42 | 2012-02-25 |

### 2012-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [PSN automatically "roots" your Facebook, no permission granted.](https://news.ycombinator.com/item?id=3691286) | 把游戏账号连接 Facebook 后，作者质疑 PSN 获得了超出同意范围的访问。 | 283 | 33 | 2012-03-11 |
| 2 | [Ask HN: Who is Hiring? (March 2012)](https://news.ycombinator.com/item?id=3652041) | 三月招聘信息交流，邀请雇主清楚标注岗位地点与候选人条件。 | 269 | 294 | 2012-03-01 |
| 3 | [I'm burning out and I can't tell anyone](https://news.ycombinator.com/item?id=3728316) | 团队正需要自己，创始人却怀疑已经倦怠，又觉得无法向任何人说。 | 241 | 191 | 2012-03-20 |
| 4 | [A+ for O'Reilly Customer Service: Keep the books and donate them](https://news.ycombinator.com/item?id=3713513) | 重复下单后出版社让读者保留并捐出多余书籍，作者称赞 O'Reilly 客服。 | 182 | 53 | 2012-03-16 |
| 5 | [Ask HN: more sites like HN](https://news.ycombinator.com/item?id=3734303) | HN 看完后还想读类似内容，作者征集其他高质量信息社区。 | 180 | 94 | 2012-03-21 |
| 6 | [Tell HN: Google Plus doesn't like my name](https://news.ycombinator.com/item?id=3775055) | 真实姓名的转写被 Google+ 判违规，作者分享实名政策带来的困扰。 | 152 | 71 | 2012-03-30 |
| 7 | [Apply with me to YC in the next 3 days and change the world](https://news.ycombinator.com/item?id=3754664) | 已有原型、曾获面试机会，独立创始人急寻合伙人一起申请 YC。 | 144 | 72 | 2012-03-26 |
| 8 | [Best Ultrabook for Linux?](https://news.ycombinator.com/item?id=3719720) | 程序员准备购买超极本，想知道哪些机型适合运行 Linux。 | 133 | 172 | 2012-03-18 |
| 9 | [Another EC2 outage (yet AWS dashboard says no error)](https://news.ycombinator.com/item?id=3707590) | 作者发现 EC2 似乎中断，但 AWS 状态面板尚未显示错误。 | 120 | 76 | 2012-03-15 |
| 10 | [Ask HN: Best Python web framework](https://news.ycombinator.com/item?id=3765610) | 旧讨论已有两年，作者希望重新比较当前的 Python 网页框架。 | 116 | 105 | 2012-03-28 |

### 2012-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who is Hiring? (April 2012)](https://news.ycombinator.com/item?id=3783657) | 四月招聘集中帖，请写明地点以及远程、实习、签证等安排。 | 264 | 223 | 2012-04-01 |
| 2 | [Ask HN: Why are a large proportion of legit posts being marked [dead]?](https://news.ycombinator.com/item?id=3788902) | 为什么大量看似正常的投稿被标为 dead，读者询问审核现象。 | 185 | 103 | 2012-04-02 |
| 3 | [Ask HN: Computer science for the self taught programmer](https://news.ycombinator.com/item?id=3784294) | 自学程序员如何补计算机科学，哪些书能覆盖复杂度和递归等基础？ | 160 | 36 | 2012-04-01 |
| 4 | [Ask PG: Can you start a HN crowd-funding venture?](https://news.ycombinator.com/item?id=3893783) | 提议由 HN 社区众筹并持有股权，让读者一起选择创业项目。 | 158 | 82 | 2012-04-26 |
| 5 | [Ask HN: Please be more thoughtful when downvoting](https://news.ycombinator.com/item?id=3782124) | 作者呼吁踩评论前多想一步，不要无解释地打压有建设性的发言。 | 143 | 76 | 2012-04-01 |
| 6 | [Ask HN: What did you build in March?](https://news.ycombinator.com/item?id=3784634) | 三月你做出了什么，邀请刚完成或发布项目的人集中展示。 | 117 | 140 | 2012-04-01 |
| 7 | [Ask Valve employees: How well does the flat organization work?](https://news.ycombinator.com/item?id=3904732) | 向 Valve 员工请教：没有传统层级的扁平组织实际运转得怎样？ | 109 | 99 | 2012-04-29 |
| 8 | [Ask HN: Freelancer? Seeking freelancer? (April 2012)](https://news.ycombinator.com/item?id=3783658) | 四月自由职业合作帖，请供需双方说明位置及能否远程协作。 | 103 | 92 | 2012-04-01 |
| 9 | [Java.sun.com is down again - breaking bad apps across the land](https://news.ycombinator.com/item?id=3904667) | Java 网站无法访问，依赖在线 DTD 的应用连带超时，作者分享排查发现。 | 97 | 36 | 2012-04-29 |
| 10 | [Ask HN: How is your Start-Up Chile experience?](https://news.ycombinator.com/item?id=3810821) | 申请 Start-Up Chile 后，作者希望听到参与者的真实体验。 | 84 | 53 | 2012-04-07 |

### 2012-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [The only way to get hold of a human at Google](https://news.ycombinator.com/item?id=4013799) | Gmail 账号被锁又难寻人工客服，作者尝试通过 HN 找到谷歌工作人员。 | 301 | 182 | 2012-05-23 |
| 2 | [Ask HN: Who Is Hiring? (May 2012)](https://news.ycombinator.com/item?id=3913997) | 五月职位汇总，要求招聘方标明工作地点和适用的条件标签。 | 243 | 269 | 2012-05-01 |
| 3 | [Ask HN: Favorite HN threads of all time](https://news.ycombinator.com/item?id=3996652) | 哪条 HN 讨论曾真正改变你看待生活或技术的角度？ | 235 | 51 | 2012-05-19 |
| 4 | [Ask HN: My wife needs something to do from home to make money...](https://news.ycombinator.com/item?id=3936225) | 妻子在家带娃又想赚钱，作者寻找不依赖学历的居家工作方向。 | 233 | 175 | 2012-05-06 |
| 5 | [Somebody please, for the love of god, fix shipping/couriers](https://news.ycombinator.com/item?id=3971212) | 多次寄收快递都不顺心，英国用户希望有人改善物流服务体验。 | 160 | 130 | 2012-05-14 |
| 6 | [I burned out at BigCo.  Am I a fool for thinking I can avoid this at a startup?](https://news.ycombinator.com/item?id=3943824) | 在大公司已经倦怠，换到创业公司就能避开同样的问题吗？ | 156 | 131 | 2012-05-08 |
| 7 | [Ask HN: How do you stay productive after work?](https://news.ycombinator.com/item?id=4018274) | 白天上班后晚上没精力，如何继续高效推进自己的事情？ | 150 | 88 | 2012-05-24 |
| 8 | [Ask PG: What successful startups has Y Combinator passed up on?](https://news.ycombinator.com/item?id=3936639) | YC 曾经错过哪些后来成功的创业公司，作者向 PG 征集实例。 | 140 | 16 | 2012-05-06 |
| 9 | [Ask HN: What are the most inspirational blog posts you've ever read?](https://news.ycombinator.com/item?id=4000394) | 有没有读完就受到鼓舞、影响至今的博客文章，邀请分享链接。 | 140 | 51 | 2012-05-20 |
| 10 | [Ask HN: losing faith in the startup where I'm employee #1](https://news.ycombinator.com/item?id=3966301) | 从学界加入公司成为首位工程师，一年后作者开始失去对团队的信心。 | 137 | 103 | 2012-05-13 |

### 2012-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Paul Graham's Letter to YC Companies](https://news.ycombinator.com/item?id=4067297) | Paul Graham 致信 YC 公司，提醒关注 Facebook IPO 后的融资变化。 | 645 | 185 | 2012-06-05 |
| 2 | [A day in the life of a startup founder](https://news.ycombinator.com/item?id=4166183) | 以虚构日程戏仿创业圈对创始人生活习惯的过度追捧。 | 633 | 126 | 2012-06-27 |
| 3 | [Moderators of HN: please stop changing post titles](https://news.ycombinator.com/item?id=4102013) | 用户要求 HN 管理员不要在帖子上首页后继续改动标题。 | 572 | 46 | 2012-06-12 |
| 4 | [Ask HN: Who Is Hiring? (June 2012)](https://news.ycombinator.com/item?id=4053076) | 六月招聘集中帖，请写清工作地点与是否接纳远程等候选人。 | 294 | 254 | 2012-06-01 |
| 5 | [Ask HN: who started something in 2012 which is already profitable?](https://news.ycombinator.com/item?id=4088538) | 2012 年才开始的项目，有哪些已经盈利，作者想收集近期成功故事。 | 221 | 193 | 2012-06-09 |
| 6 | [Ask HN: How to setup a company in U.S. without being there?](https://news.ycombinator.com/item?id=4122794) | 人在埃及却需要国际收款，作者求助如何不赴美也能设立美国公司。 | 189 | 71 | 2012-06-17 |
| 7 | [Ask HN: How do you learn to develop exploits?](https://news.ycombinator.com/item?id=4121062) | 从理解技术走向安全实践，学习编写漏洞利用程序该从哪里开始？ | 166 | 78 | 2012-06-16 |
| 8 | [Ask HN: What is the best way to promote your startup?](https://news.ycombinator.com/item?id=4161813) | 让潜在客户认识创业项目，哪些推广办法最值得先尝试？ | 145 | 49 | 2012-06-26 |
| 9 | [Ask HN: Best setups to avoid availability outages on AWS](https://news.ycombinator.com/item?id=4181348) | 仅使用 AWS 服务，怎样安排架构才能降低单个可用区故障的影响？ | 128 | 33 | 2012-06-30 |
| 10 | [Ask HN: who started something in 2012 that didn't or won't become profitable?](https://news.ycombinator.com/item?id=4090845) | 与盈利故事对应，征集 2012 年启动却没能、或不会盈利的项目。 | 111 | 164 | 2012-06-10 |

### 2012-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [A note I sent to YCombinator](https://news.ycombinator.com/item?id=4273460) | 一位多次创业并有技术写作经历的作者，公开自己寄给 YC 的信。 | 337 | 61 | 2012-07-21 |
| 2 | [Ubisoft "Uplay" DRM exposed as rootkit](https://news.ycombinator.com/item?id=4311264) | 作者指出育碧 Uplay DRM 的安全风险，并提供游戏安装后的验证线索。 | 317 | 136 | 2012-07-30 |
| 3 | [Ask HN: I'm desperate to stay in Denmark. Anyone need a great web/ios dev?](https://news.ycombinator.com/item?id=4250118) | 有硅谷经验的网页与 iOS 开发者，希望通过找到工作继续留在丹麦。 | 219 | 126 | 2012-07-16 |
| 4 | [Opensource contributor Bassel Khartabil detained in Syria. Needs help](https://news.ycombinator.com/item?id=4192957) | 呼吁帮助在叙利亚被拘押的开源贡献者 Bassel Khartabil。 | 184 | 23 | 2012-07-03 |
| 5 | [Ask HN: Who Is Hiring? (July 2012)](https://news.ycombinator.com/item?id=4184755) | 七月职位交流，欢迎雇主说明地点及远程、实习、签证支持情况。 | 181 | 244 | 2012-07-01 |
| 6 | [Ask HN: Learn Math the Hard Way](https://news.ycombinator.com/item?id=4214403) | 想靠自学数学改善思考并理解算法基础，作者寻找扎实的学习路径。 | 171 | 84 | 2012-07-08 |
| 7 | [Ask HN: Recommendations for learning and improving UX/UI skills?](https://news.ycombinator.com/item?id=4316967) | 编码熟练却觉得界面设计薄弱，开发者该用哪些资源提升 UX 和 UI？ | 147 | 50 | 2012-07-31 |
| 8 | [Ask PG: What caused the downtime?](https://news.ycombinator.com/item?id=4315457) | HN 停机数小时后，读者向 PG 追问具体原因。 | 142 | 84 | 2012-07-31 |
| 9 | [Tell HN: How 2 devs got 1 million monthly actives with no social/viral tools](https://news.ycombinator.com/item?id=4205571) | KeepSafe 团队称不用社交传播工具，也靠两名开发者做到百万月活。 | 109 | 27 | 2012-07-05 |
| 10 | [Ask HN: Freelancer? Seeking freelancer? (July 2012) ](https://news.ycombinator.com/item?id=4184757) | 七月自由职业需求汇总，求工作与找外包者请写明地点及远程安排。 | 101 | 113 | 2012-07-01 |

### 2012-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Why I now, unfortunately, hate Hacker News..](https://news.ycombinator.com/item?id=4396747) | 一位老用户解释自己为何从喜爱 HN 变得反感社区氛围。 | 871 | 431 | 2012-08-17 |
| 2 | [Ask HN: Who Is Hiring? (August 2012)](https://news.ycombinator.com/item?id=4323597) | 八月招聘集中发布，方便依据地点和工作条件寻找机会。 | 276 | 291 | 2012-08-01 |
| 3 | [Thanks for your patience about all the (YC S12)](https://news.ycombinator.com/item?id=4393795) | YC 项目在 Demo Day 前集中上线，作者感谢读者对首页密集发布的耐心。 | 208 | 72 | 2012-08-16 |
| 4 | [Ask HN: Where is the Hostility on HN Coming From? ](https://news.ycombinator.com/item?id=4354635) | 从一条设计讨论里的敌意出发，作者追问 HN 的火药味来自哪里。 | 171 | 151 | 2012-08-08 |
| 5 | [Ask PG: What made you change your mind about crowdfunding?](https://news.ycombinator.com/item?id=4412027) | 此前担忧众筹、如今态度似乎不同，作者想知道 PG 改变看法的原因。 | 166 | 15 | 2012-08-21 |
| 6 | [Jury foreman says Apple patents valid due to different processor architecture](https://news.ycombinator.com/item?id=4446102) | 作者引用陪审团长访谈，质疑其以处理器差异判断苹果专利的推理。 | 151 | 75 | 2012-08-28 |
| 7 | [Ask PG: Is RFS3 "Things built on Twitter" still sensible to prioritise?](https://news.ycombinator.com/item?id=4332000) | Twitter 平台规则多变，优先支持基于它创业的项目是否仍然合理？ | 147 | 55 | 2012-08-03 |
| 8 | [Ask HN: How to learn Backbone](https://news.ycombinator.com/item?id=4434553) | 网上教程版本太旧，作者寻找适用于 Backbone 0.9.2 的学习材料。 | 125 | 33 | 2012-08-26 |
| 9 | [Ask HN: Is Google still a cool place to work?](https://news.ycombinator.com/item?id=4459412) | 谷歌现在还是令人向往的工作地点吗，作者尤其想听前员工看法。 | 107 | 122 | 2012-08-31 |
| 10 | [Ask HN: How should I evaluate a startup as I job hunt?](https://news.ycombinator.com/item?id=4340196) | 从大软件公司转投创业团队，求职时该怎样评估公司的质量与风险？ | 102 | 56 | 2012-08-05 |

### 2012-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Why was a scam company able to raise $76 Million Series B?](https://news.ycombinator.com/item?id=4592778) | 用户质疑商业模式有争议的 JustFab 为何能获得巨额融资。 | 660 | 174 | 2012-09-30 |
| 2 | [Ask PG: What Is The Most Frighteningly Ambitious Idea You Have Been Pitched On?](https://news.ycombinator.com/item?id=4509934) | PG 听过最雄心勃勃、甚至令人害怕的创业提案是什么？ | 407 | 189 | 2012-09-12 |
| 3 | [Ask HN: Who Is Hiring? (September 2012)](https://news.ycombinator.com/item?id=4463689) | 九月招聘信息帖，地点与远程等条件需在开头明确。 | 393 | 299 | 2012-09-01 |
| 4 | [Ask HN: How much recurring income do you generate, and from what?](https://news.ycombinator.com/item?id=4467603) | 一年后再问：你有多少持续性收入，它们分别来自哪里？ | 313 | 279 | 2012-09-02 |
| 5 | [Tell HN: Login to unsubscribe is against Federal Law](https://news.ycombinator.com/item?id=4496688) | 作者质疑要求登录才能退订的营销邮件，援引美国法律提醒发送者。 | 310 | 101 | 2012-09-09 |
| 6 | [Ask HN: How did you hack the press when you launched your startup(s)?](https://news.ycombinator.com/item?id=4495786) | 创业发布时如何获得媒体报道，又给注册和下载带来了多少帮助？ | 188 | 46 | 2012-09-09 |
| 7 | [Ask PG: If Viaweb hadn't worked out, what would you have likely done next?](https://news.ycombinator.com/item?id=4486463) | 如果 Viaweb 当初没做成，PG 最可能选择怎样的下一条路？ | 187 | 43 | 2012-09-06 |
| 8 | [Startup idea list](https://news.ycombinator.com/item?id=4537834) | 重开创业点子清单，邀请大家像五年前一样分享新想法。 | 161 | 267 | 2012-09-18 |
| 9 | [Ask HN: How do you find clients?](https://news.ycombinator.com/item?id=4471030) | 想做网页设计和营销兼职，除了打陌生电话还能怎样找到客户？ | 150 | 81 | 2012-09-03 |
| 10 | [Ask HN: How does an experienced freelancer get work?](https://news.ycombinator.com/item?id=4585435) | 资深开发者刚转自由职业，面对平台低价竞争，该去哪里获得项目？ | 139 | 74 | 2012-09-28 |

### 2012-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Let's Be Civil](https://news.ycombinator.com/item?id=4707475) | 用户呼吁讨论 iPad mini、Surface 等产品时保持礼貌。 | 671 | 138 | 2012-10-27 |
| 2 | [Ask HN: Who Is Hiring? (October 2012) ](https://news.ycombinator.com/item?id=4596375) | 十月职位集中帖，招聘方请说明位置、远程与签证等条件。 | 256 | 294 | 2012-10-01 |
| 3 | [Ask HN: Your best passive income sources?](https://news.ycombinator.com/item?id=4639271) | 你最好的被动收入来源是什么，哪些方式能够持续带来收益？ | 237 | 221 | 2012-10-11 |
| 4 | [Because of the storm we're pushing the YC application deadline back to Friday](https://news.ycombinator.com/item?id=4718447) | 受风暴影响，YC 将申请截止时间延至周五，向申请者说明新安排。 | 230 | 50 | 2012-10-30 |
| 5 | [Ask HN: What did the really successful programmers do differently?](https://news.ycombinator.com/item?id=4626201) | 真正成功的程序员做对了什么，哪些选择或习惯让他们走得更远？ | 219 | 168 | 2012-10-08 |
| 6 | [Ask HN - Where do you look for jobs?](https://news.ycombinator.com/item?id=4655144) | 除了 HN、GitHub 等常见渠道，大家还去哪里寻找技术工作？ | 176 | 94 | 2012-10-15 |
| 7 | [Ask HN: Learning to write good JavaScript](https://news.ycombinator.com/item?id=4673106) | 主要写 .NET 的开发者越来越常用 JavaScript，想系统提高代码质量。 | 163 | 49 | 2012-10-19 |
| 8 | [FBI Hack news on Hackernews is Fake](https://news.ycombinator.com/item?id=4678064) | 作者指出 HN 热门的 FBI 入侵消息是旧闻，质疑其被当作新事件传播。 | 136 | 9 | 2012-10-20 |
| 9 | [Ask HN: What's your startup's analytics setup?](https://news.ycombinator.com/item?id=4707903) | 可选统计服务太多，创业公司如何组合工具来分析自己的业务？ | 131 | 66 | 2012-10-28 |
| 10 | [Ask HN: What is this? 158268a350000000](https://news.ycombinator.com/item?id=4697400) | 一个账号不断发出奇怪字符串和全球坐标，作者想弄清它们的含义。 | 128 | 67 | 2012-10-25 |

### 2012-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Help, HN'er in trouble, we need a laywer in Delhi immediately](https://news.ycombinator.com/item?id=4739649) | 一位 HN 用户在印度被警方拘留，社区紧急寻找德里律师。 | 591 | 108 | 2012-11-04 |
| 2 | [Ask HN: Are you alone in San Francisco on Thanksgiving?](https://news.ycombinator.com/item?id=4819792) | 感恩节独自在旧金山的人，可以联系作者一起过节吃饭。 | 475 | 94 | 2012-11-22 |
| 3 | [Thank You HN: From 30 people whose lives you saved](https://news.ycombinator.com/item?id=4815006) | Watsi 上线三个月后感谢 HN 支持，并带回三十位患者的后续消息。 | 372 | 56 | 2012-11-21 |
| 4 | [Ask HN: Who Is Hiring? (November 2012)](https://news.ycombinator.com/item?id=4727241) | 十一月招聘机会汇总，请写明职位地点及不同候选人的申请条件。 | 222 | 261 | 2012-11-01 |
| 5 | [How to get your IP unbanned on HN](https://news.ycombinator.com/item?id=4761102) | HN 对快速请求封禁较敏感，作者提供因 IP 被封后自助解封的办法。 | 220 | 76 | 2012-11-09 |
| 6 | [Y Combinator interview decisions postponed to November 15](https://news.ycombinator.com/item?id=4774288) | 受风暴延迟申请影响，YC 将面试邀请通知推迟到十一月十五日。 | 198 | 96 | 2012-11-12 |
| 7 | [Ask HN: How do you write great sentences, paragraphs, or articles?](https://news.ycombinator.com/item?id=4828497) | 不满足于抽象写作原则，作者想知道怎样具体写好句子、段落和文章。 | 140 | 78 | 2012-11-25 |
| 8 | [Ask HN: How have you made "quick" money before?](https://news.ycombinator.com/item?id=4812589) | 有网页与移动开发技能，却眼下需要现金，作者征集短期赚钱经验。 | 125 | 101 | 2012-11-21 |
| 9 | [The BufferApp Welcome Email](https://news.ycombinator.com/item?id=4772709) | BufferApp 的欢迎邮件简洁又有人情味，作者分享这次入门体验。 | 119 | 16 | 2012-11-12 |
| 10 | [Remind HN: Vote](https://news.ycombinator.com/item?id=4747870) | 提醒美国读者行使投票权，在忙于技术之外也做知情的公民。 | 118 | 127 | 2012-11-06 |

### 2012-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Best books you read in 2012](https://news.ycombinator.com/item?id=4966230) | 2012 年你读到了哪些最好的书，无论是不是当年新出版？ | 359 | 220 | 2012-12-25 |
| 2 | [Ask HN: What unknown technical blogs or sites do you read?](https://news.ycombinator.com/item?id=4928762) | 哪些不太知名的技术博客或网站，值得从你的订阅列表中推荐？ | 294 | 80 | 2012-12-16 |
| 3 | [I am depressed and I need someone to talk to](https://news.ycombinator.com/item?id=4928031) | 陷入抑郁又不愿暴露身份，作者用临时账号寻找愿意倾听的人。 | 281 | 147 | 2012-12-16 |
| 4 | [Ask HN: A place like HN but with more nerdy stuff and less social stuff?](https://news.ycombinator.com/item?id=4891238) | 想看更硬核技术、少点消极与社交话题，有哪些比 HN 更合适的地方？ | 238 | 171 | 2012-12-08 |
| 5 | [Ask HN: Who is hiring? (December 2012) ](https://news.ycombinator.com/item?id=4857714) | 十二月职位汇总，邀请招聘方说明地点及远程、实习、签证条件。 | 227 | 284 | 2012-12-01 |
| 6 | [Help HN: Developer laid off 5 days before Christmas, have kids](https://news.ycombinator.com/item?id=4949556) | 圣诞前五天因投资撤回被裁，有孩子的开发者向社区寻找新机会。 | 224 | 127 | 2012-12-20 |
| 7 | [Ask HN: what was the best life/programming choice you ever made?](https://news.ycombinator.com/item?id=4861022) | 生活和编程各选一次：你做过最正确的决定是什么？ | 193 | 223 | 2012-12-02 |
| 8 | [Ask HN: How do you escape CRUD jobs?](https://news.ycombinator.com/item?id=4968452) | 不想一直做增删改查业务，程序员怎样转向更有技术挑战的工作？ | 171 | 87 | 2012-12-26 |
| 9 | [No one-click unsubscribe? It's spam.](https://news.ycombinator.com/item?id=4929997) | 没有一键退订就直接标垃圾邮件，作者向营销邮件发送者表达不满。 | 161 | 108 | 2012-12-16 |
| 10 | [Ask HN: Did YC accept anyone without an idea this round?](https://news.ycombinator.com/item?id=4896009) | 本轮 YC 是否真的录取了尚未确定创业点子的申请者？ | 155 | 17 | 2012-12-09 |

### 2013-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Proposition HN: I will pay $8000 for you to build your side-project/MVP](https://news.ycombinator.com/item?id=5037694) | 发帖者提出出资八千美元，资助技术人才开发自己的副业项目或最小可行产品。 | 1088 | 377 | 2013-01-10 |
| 2 | [Why you shouldn't do what Aaron did](https://news.ycombinator.com/item?id=5048132) | Aaron Swartz 去世后，作者安慰受触动者：痛苦会过去，值得继续生活。 | 519 | 158 | 2013-01-12 |
| 3 | [Let's black bar HN](https://news.ycombinator.com/item?id=5047472) | 请求 HN 为 Aaron Swartz 挂出黑色纪念栏，肯定他留下的影响。 | 483 | 75 | 2013-01-12 |
| 4 | [Ask HN admins: please stop editing submission titles](https://news.ycombinator.com/item?id=5142851) | 管理员改投稿标题让作者不满，希望 HN 停止这种编辑惯例。 | 398 | 73 | 2013-01-31 |
| 5 | [What we discovered about InstallMonetizer](https://news.ycombinator.com/item?id=5092711) | 回应 InstallMonetizer 的争议，投资方介绍自己对该公司的调查。 | 333 | 178 | 2013-01-21 |
| 6 | [Implore HN: Celebrate and encourage young developers who post here](https://news.ycombinator.com/item?id=5093721) | 针对年轻开发者受到的冷嘲，作者呼吁社区多鼓励愿意展示作品的少年。 | 294 | 115 | 2013-01-21 |
| 7 | [Ask HN: Who is hiring? (January 2013)](https://news.ycombinator.com/item?id=4992617) | 2013 年一月招聘集中帖，请雇主注明地点及候选人相关条件。 | 245 | 254 | 2013-01-01 |
| 8 | [Ask HN: How do you stop regretting?](https://news.ycombinator.com/item?id=5119213) | 三十出头仍每天为教育、成就等遗憾困扰，作者想知道如何停止后悔。 | 233 | 127 | 2013-01-26 |
| 9 | [Github SSL replaced by self-signed certificate in China](https://news.ycombinator.com/item?id=5124784) | 作者报告中国访问 GitHub 时遇到自签名证书替换，怀疑中间人攻击。 | 189 | 75 | 2013-01-27 |
| 10 | [Help HN: Today I Just Became Homeless & I Need Your Help](https://news.ycombinator.com/item?id=5106375) | 曾为大公司服务的设计师与前端开发者称无家可归，向社区请求帮助。 | 164 | 39 | 2013-01-24 |

### 2013-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Why HN was down](https://news.ycombinator.com/item?id=5239673) | HN 解释整夜宕机的原因：手工调整评论时误建了循环引用。 | 1049 | 287 | 2013-02-18 |
| 2 | [Ask HN: Tools of the trade, 2013 edition](https://news.ycombinator.com/item?id=5235137) | 延续几年前的工具讨论，征集 2013 年值得使用的托管服务。 | 494 | 159 | 2013-02-17 |
| 3 | [I made $200K and PayPal locked my account](https://news.ycombinator.com/item?id=5191142) | turn.js 作者称商业版赚到二十万美元后 PayPal 锁了账户，求助处理。 | 474 | 270 | 2013-02-09 |
| 4 | [HN will be down Saturday morning while we switch servers](https://news.ycombinator.com/item?id=5229364) | HN 将在周六清晨换到更快的服务器，提前通知预期停机。 | 225 | 118 | 2013-02-15 |
| 5 | [Ask HN: Who is hiring? (February 2013)](https://news.ycombinator.com/item?id=5150834) | 二月职位交流，请在开头写清工作位置及适用的远程等安排。 | 223 | 256 | 2013-02-01 |
| 6 | [Ask HN: A patent troll is targeting my transit app](https://news.ycombinator.com/item?id=5272575) | 多伦多公交应用收到专利主张，独立开发者求助如何应对专利诉讼威胁。 | 219 | 59 | 2013-02-24 |
| 7 | [So what happened to the HN server?](https://news.ycombinator.com/item?id=5237947) | 服务器切换后究竟发生了什么，读者好奇 HN 新机器的运行情况。 | 170 | 127 | 2013-02-18 |
| 8 | [Ask HN:  How do you deal with Rabbit Hole Syndrome?](https://news.ycombinator.com/item?id=5197155) | 总在不重要的细节追求完美，怎样避免工作中越钻越深的兔子洞？ | 140 | 82 | 2013-02-10 |
| 9 | [Tell HN: You guys scared edw519 off Hacker News](https://news.ycombinator.com/item?id=5255739) | edw519 久未发言，作者认为社区把一位有价值的评论者吓走了。 | 120 | 50 | 2013-02-21 |
| 10 | [Tell HN: We've Lost An Engineering Luminary - Bob Davis (IEEE)](https://news.ycombinator.com/item?id=5199655) | 悼念工程界的 Bob Davis，作者希望社区温和地纪念他的贡献。 | 116 | 9 | 2013-02-11 |

### 2013-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Webdevs, designers: what devtools should we (Mozilla) build in Firefox?](https://news.ycombinator.com/item?id=5325445) | Firefox 开发工具团队征集需求：网页开发者与设计师希望内置什么功能？ | 470 | 347 | 2013-03-05 |
| 2 | [I'm a loser and I want to change that - now](https://news.ycombinator.com/item?id=5390138) | 长期空想、很少坚持尝试，作者想立即改变自己眼中的失败状态。 | 455 | 245 | 2013-03-17 |
| 3 | [Official comment from HN on dead threads](https://news.ycombinator.com/item?id=5416908) | 多条 Adria Richards 相关帖子被隐藏，用户请求 HN 给出正式解释。 | 370 | 184 | 2013-03-21 |
| 4 | [Tell HN: My Web App has 13 Users](https://news.ycombinator.com/item?id=5386966) | 不是所有上线都轰动：作者分享自己的网页应用目前只有十三名用户。 | 319 | 158 | 2013-03-16 |
| 5 | [Ask HN: Who is hiring? (March 2013)](https://news.ycombinator.com/item?id=5304169) | 三月招聘信息汇集，要求注明地点和实习、远程、签证条件。 | 286 | 360 | 2013-03-01 |
| 6 | [Ask PG: Did the "apply to YC without an idea" experiment work?](https://news.ycombinator.com/item?id=5463071) | 似乎不能再“无点子申请”，作者询问 YC 的这项实验是否有效。 | 276 | 58 | 2013-03-29 |
| 7 | [Thank you HN, sorry HN](https://news.ycombinator.com/item?id=5348589) | 此前因严重抑郁求助后，作者回来感谢 HN 并更新自己的处境。 | 258 | 56 | 2013-03-09 |
| 8 | [What's up with HN?](https://news.ycombinator.com/item?id=5359731) | HN 遭遇流量庞大的 DDoS，作者解释原有 Arc 层处理方式难以承受。 | 236 | 121 | 2013-03-12 |
| 9 | [Ask PG: Comments are not working?](https://news.ycombinator.com/item?id=5359416) | 首页文章的评论链接都返回 404，读者询问 HN 是否出现故障。 | 199 | 39 | 2013-03-12 |
| 10 | [Ask HN: Have you ever been sued by your startup?](https://news.ycombinator.com/item?id=5438040) | 被以前工作的创业公司起诉，作者想听听别人经历类似纠纷的方法。 | 191 | 98 | 2013-03-25 |

### 2013-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What's the best technical talk you've heard?](https://news.ycombinator.com/item?id=5511466) | 你听过最精彩的技术演讲是哪一场，值得推荐给社区吗？ | 523 | 191 | 2013-04-08 |
| 2 | [Ask HN: Why would a government have created bitcoin?](https://news.ycombinator.com/item?id=5547423) | 作者怀疑比特币出自某国政府，提出自己的疑点并询问可能动机。 | 457 | 294 | 2013-04-14 |
| 3 | [How can we get Google Support?](https://news.ycombinator.com/item?id=5523992) | Symfony 的邮件列表依赖 Google Groups，项目方求助如何联系谷歌支持。 | 446 | 217 | 2013-04-10 |
| 4 | [Could HN stop participating in the witchhunt?](https://news.ycombinator.com/item?id=5576008) | 爆炸案嫌疑人的讨论不断误伤他人，作者呼吁 HN 停止参与网络围猎。 | 382 | 65 | 2013-04-19 |
| 5 | [Dear HN "Who's Hiring" responders](https://news.ycombinator.com/item?id=5476363) | 面向招聘帖的应聘者，作者汇总雇主反复遇到的问题并给出提醒。 | 363 | 205 | 2013-04-01 |
| 6 | [Ask HN: Who is hiring? (April 2013)](https://news.ycombinator.com/item?id=5472746) | 四月招聘集中帖，邀请公司明确地点及实习、远程和签证条件。 | 320 | 420 | 2013-04-01 |
| 7 | [Tell HN: Flag PR "April fools pranks"](https://news.ycombinator.com/item?id=5470859) | 作者呼吁举报缺乏创意的愚人节公关笑话，减少社区刷屏。 | 261 | 43 | 2013-04-01 |
| 8 | [Dear YC companies, I responded. You could do the same.](https://news.ycombinator.com/item?id=5518881) | YC 公司主动联系自由职业者后却不回信，作者要求对方尊重回复者。 | 213 | 79 | 2013-04-09 |
| 9 | [Ask HN: What should I do?](https://news.ycombinator.com/item?id=5478713) | 英国网页开发者三年经验却年薪仅一万五千英镑，求助是否该离开。 | 176 | 152 | 2013-04-02 |
| 10 | [Ask HN: Who built XMLHttpRequest at Microsoft in 1999?](https://news.ycombinator.com/item?id=5626079) | XMLHttpRequest 究竟由微软哪位工程师发明，作者想让幕后贡献被看见。 | 176 | 55 | 2013-04-29 |

### 2013-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who is hiring? (May 2013)](https://news.ycombinator.com/item?id=5637663) | 五月职位交流帖，请招聘方清楚说明工作地点与候选人条件。 | 327 | 437 | 2013-05-01 |
| 2 | [A note to myself](https://news.ycombinator.com/item?id=5691216) | 作者给自己留纸条：新点子固然诱人，把手头的事做完同样很酷。 | 305 | 84 | 2013-05-11 |
| 3 | [The new Google Hangouts will not support XMPP](https://news.ycombinator.com/item?id=5714557) | 新 Google Hangouts 不再支持 XMPP，开发者转发相关变更通知。 | 198 | 141 | 2013-05-15 |
| 4 | [Ask HN: Google workers, sister is visiting S.J. Can she tour the Googleplex?](https://news.ycombinator.com/item?id=5689455) | 患重病的妹妹将去圣何塞，作者求谷歌员工帮助安排园区参观。 | 189 | 37 | 2013-05-11 |
| 5 | [Ask HN: and now what?](https://news.ycombinator.com/item?id=5763100) | 近三十八岁、做过多年游戏与创业后，作者在绝望中寻找下一步出路。 | 169 | 85 | 2013-05-24 |
| 6 | [Ask HN: What Freelancer site do you recommend?](https://news.ycombinator.com/item?id=5774303) | 一次简单外包失败后，作者征集更可靠的自由职业平台。 | 152 | 132 | 2013-05-27 |
| 7 | [Ask HN: Why can't I login to HN via Firefox?](https://news.ycombinator.com/item?id=5650171) | Chrome 和 IE 能登录、Firefox 却不行，作者求助 HN 登录异常。 | 150 | 101 | 2013-05-03 |
| 8 | [Ask HN: Freelancer? Seeking freelancer? (May 2013)](https://news.ycombinator.com/item?id=5637667) | 五月自由职业撮合，供求工作与找外援者介绍位置及合作方式。 | 138 | 206 | 2013-05-01 |
| 9 | [Are HN comments broken for everyone?](https://news.ycombinator.com/item?id=5796002) | HN 评论只显示空白页，作者询问这是不是所有人都遇到的故障。 | 123 | 38 | 2013-05-30 |
| 10 | [Microsoft is killing Linux shops with Secure Boot](https://news.ycombinator.com/item?id=5658184) | 作者以 Linux 商家的遭遇为例，质疑微软 Secure Boot 带来的限制。 | 113 | 95 | 2013-05-05 |

### 2013-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Can we please slow down the stories about Edward Snowden?](https://news.ycombinator.com/item?id=5932645) | 斯诺登行程新闻频繁占版，作者希望社区降低相关跟踪报道的密度。 | 374 | 155 | 2013-06-24 |
| 2 | [Keep the NSA out of WebRTC](https://news.ycombinator.com/item?id=5842008) | 围绕 WebRTC 加密标准，作者呼吁防止通信方案受到国家监控影响。 | 254 | 17 | 2013-06-07 |
| 3 | [Ask HN: Who is hiring? (June 2013)](https://news.ycombinator.com/item?id=5803764) | 六月职位汇总，请在开头注明地点并说明远程等申请条件。 | 249 | 362 | 2013-06-01 |
| 4 | [Posting to HN is like exposing yourself to the eye of Mordor](https://news.ycombinator.com/item?id=5830219) | 投稿像面对“魔眼”：作者同情作品展示者承受的尖刻评论和压力。 | 212 | 121 | 2013-06-06 |
| 5 | [Ask HN: Alternatives to HN](https://news.ycombinator.com/item?id=5831208) | 寻找更重技术、建设性讨论和有趣内容的 HN 类替代社区。 | 197 | 168 | 2013-06-06 |
| 6 | [Poll: Full-time software engineers over 200k, how'd you get there?](https://news.ycombinator.com/item?id=5804798) | 全职软件工程师年收入超过二十万美元，是通过怎样的路径做到的？ | 191 | 121 | 2013-06-01 |
| 7 | [Ask HN: Passive income ideas?](https://news.ycombinator.com/item?id=5903868) | 每天可投入一两小时的程序员，想找最终每月净赚一千美元的项目方向。 | 190 | 172 | 2013-06-19 |
| 8 | [Sell HN: Do you have a side project you want to sell?](https://news.ycombinator.com/item?id=5803374) | 开设业余项目交易帖，邀请愿意出售自己作品的人介绍项目。 | 145 | 191 | 2013-06-01 |
| 9 | [.io domains down?](https://news.ycombinator.com/item?id=5838670) | 多个 .io 网站同时打不开、解析返回不存在，作者询问域名服务是否故障。 | 135 | 94 | 2013-06-07 |
| 10 | [If you didn't cancel the credit card you used for linode.com, now is the time](https://news.ycombinator.com/item?id=5833621) | Linode 泄露事件后迟迟没换信用卡，作者用自身经历提醒及时处理。 | 133 | 129 | 2013-06-06 |

### 2013-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: I'm quadriplegic – can you help me with my security?](https://news.ycombinator.com/item?id=6053047) | 四肢瘫痪的用户想安全登录各类网站，求助兼顾安全与可操作性的方案。 | 486 | 168 | 2013-07-16 |
| 2 | [Ask HN: Who is hiring? (July 2013)](https://news.ycombinator.com/item?id=5970187) | 七月招聘交流帖，请说明职位地点及实习、远程、签证等支持。 | 309 | 367 | 2013-07-01 |
| 3 | [Apple Developer Website Update](https://news.ycombinator.com/item?id=6080620) | 转发苹果开发者网站通知，说明入侵者曾试图取得注册开发者信息。 | 282 | 210 | 2013-07-21 |
| 4 | [Ask PG: Will you post an update to "Startup Ideas We'd Like to Fund"?](https://news.ycombinator.com/item?id=6014422) | 五年前的愿投点子清单仍有参考价值，读者希望 PG 发布新版。 | 231 | 72 | 2013-07-09 |
| 5 | [Ask HN: HN Political News Overload?](https://news.ycombinator.com/item?id=6120201) | 政治帖子明显增多，作者结合 HN 准则询问是否已经过载。 | 206 | 149 | 2013-07-29 |
| 6 | [Ask HN: Take down my reverse-engineered Snapchat lib because they asked?](https://news.ycombinator.com/item?id=6083812) | 逆向 Snapchat 后写出 PHP 库，收到下架请求的作者纠结是否配合。 | 194 | 133 | 2013-07-22 |
| 7 | [I bootstrapped a $10 million company and need serious help](https://news.ycombinator.com/item?id=6039053) | 从自筹资金发展出规模可观的照片打印公司，创始人如今急需经营帮助。 | 189 | 84 | 2013-07-13 |
| 8 | [Ask HN: When did people start paying for your SaaS and why?](https://news.ycombinator.com/item?id=6037636) | SaaS 用户什么时候开始付款，你试过多少次才找到愿意付费的需求？ | 169 | 74 | 2013-07-13 |
| 9 | [Ask HN: How does one create a fake identity?](https://news.ycombinator.com/item?id=6002595) | 作者询问虚构身份如何建立，以及不同使用场景会面临怎样的验证。 | 159 | 110 | 2013-07-07 |
| 10 | [Ask HN: Has anyone here self-published a book? Any advice?](https://news.ycombinator.com/item?id=6052075) | 书快写完了，作者向有自出版经验的人征求流程与注意事项。 | 137 | 83 | 2013-07-16 |

### 2013-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [HN is Becoming 2005 Slashdot](https://news.ycombinator.com/item?id=6157485) | 曾从 Slashdot 转来的读者担忧，HN 正重现自己厌倦的社区氛围。 | 404 | 252 | 2013-08-04 |
| 2 | [We're only being dishonest to get your attention. Join us!](https://news.ycombinator.com/item?id=6269845) | 作者讽刺用不实标题吸引眼球的招聘或宣传帖，追问这种做法是否合适。 | 350 | 68 | 2013-08-24 |
| 3 | [Tell HN: Add ?share=1 to Quora URLs to display content without login](https://news.ycombinator.com/item?id=6300856) | 分享 Quora 阅读技巧：给链接加上 ?share=1 可免登录显示内容。 | 341 | 128 | 2013-08-30 |
| 4 | [Ask HN: I'm a chronic procrastinator – how do I break it?](https://news.ycombinator.com/item?id=6145261) | 长期靠聪明掩盖拖延，作者想真正打破这种影响生活的习惯。 | 340 | 292 | 2013-08-02 |
| 5 | [Ask HN: How Can I leave Syria now and get asylum in Europe (Germany)](https://news.ycombinator.com/item?id=6300923) | 身在大马士革的程序员担忧战争，求助如何离开叙利亚并到欧洲避难。 | 298 | 210 | 2013-08-30 |
| 6 | [Ask HN: Who is hiring? (August 2013)](https://news.ycombinator.com/item?id=6139927) | 八月招聘集中帖，请雇主说明工作地点及候选人对应的条件。 | 279 | 385 | 2013-08-01 |
| 7 | [Beg HN: Please only report serious GitHub outages (1h+)](https://news.ycombinator.com/item?id=6165419) | 几分钟的 GitHub 故障也反复投稿，作者希望只报告较严重的中断。 | 252 | 69 | 2013-08-06 |
| 8 | [We need an NRA for privacy](https://news.ycombinator.com/item?id=6185138) | 安全邮箱因政府压力而关闭后，作者主张建立有组织的隐私权倡议团体。 | 233 | 167 | 2013-08-09 |
| 9 | [Ask PG: Why is everybody hellbanned?](https://news.ycombinator.com/item?id=6155386) | 打开 showdead 后发现大量帖子被隐藏，读者质疑 HN 的封禁是否异常。 | 222 | 129 | 2013-08-04 |
| 10 | [Ask HN: What happened to Proposition HN? ("$8000 for your side project")](https://news.ycombinator.com/item?id=6239304) | 曾有人出资八千美元支持业余项目，作者追问“Proposition HN”的后续。 | 197 | 42 | 2013-08-19 |

### 2013-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Why can a scam company raise $40 Million Series C + $76 Million Series B?](https://news.ycombinator.com/item?id=6455391) | 发帖者质疑 JustFab 的商业模式，并追问为何投资人仍愿投入巨额资金。 | 1065 | 461 | 2013-09-27 |
| 2 | [Ask HN: How much recurring income do you generate, and from what?](https://news.ycombinator.com/item?id=6431573) | 再次更新持续收入调查：你靠什么获得经常性收入，如今有多少？ | 444 | 430 | 2013-09-23 |
| 3 | [Warning: Google Authenticator upgrade loses all accounts](https://news.ycombinator.com/item?id=6325760) | 作者称 iPhone 上升级 Google Authenticator 后所有账号丢失，提醒其他用户。 | 344 | 168 | 2013-09-04 |
| 4 | [Ask HN: Who is hiring? (September 2013)](https://news.ycombinator.com/item?id=6310234) | 九月招聘帖特别呼吁帮助在叙利亚或因战争流离失所的程序员找安全工作。 | 304 | 374 | 2013-09-01 |
| 5 | [Bruce Schneier has changed his PGP key to 4096 bits](https://news.ycombinator.com/item?id=6376954) | Schneier 更换多年使用的 PGP 密钥，作者对时间点与原因提出猜想。 | 222 | 139 | 2013-09-12 |
| 6 | [Ask HN: How to best acquire theoretical computer science knowledge?](https://news.ycombinator.com/item?id=6345368) | 已有编程兴趣却缺理论背景，作者想找到系统学习理论计算机科学的办法。 | 167 | 116 | 2013-09-07 |
| 7 | [Ask HN: How many "self-taught" programmers and how did you do it?](https://news.ycombinator.com/item?id=6468295) | 社区有多少自学程序员，邀请说明学习资源、方法和自己的成长路径。 | 102 | 124 | 2013-09-30 |
| 8 | [Britain's GCHQ hacked Belgium's telco Belgacom](https://news.ycombinator.com/item?id=6416753) | 转述英国 GCHQ 入侵比利时电信商 Belgacom 的消息，附相关报道链接。 | 99 | 30 | 2013-09-20 |
| 9 | [Ask HN: Freelancer? Seeking freelancer? (September 2013)](https://news.ycombinator.com/item?id=6310240) | 九月自由职业撮合帖，也特别呼吁为受叙利亚战事影响的人寻找安全工作。 | 98 | 131 | 2013-09-01 |
| 10 | [Ask HN: Is it time for a public GPG audit?](https://news.ycombinator.com/item?id=6389534) | 隐私担忧让更多人转向 GPG，是否该为它组织一次公开安全审计？ | 94 | 38 | 2013-09-15 |

### 2013-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Why the Microsoft hate?](https://news.ycombinator.com/item?id=6596038) | 发帖者质疑 HN 对微软相关消息的敌意，以及因品牌好恶举报帖子的做法。 | 763 | 530 | 2013-10-23 |
| 2 | [Launching your project to the world? Try these sites to get the word out](https://news.ycombinator.com/item?id=6488822) | 项目准备面向世界发布，作者整理了可投稿、可争取曝光的网站。 | 507 | 92 | 2013-10-03 |
| 3 | [Why we revert to original titles](https://news.ycombinator.com/item?id=6572466) | HN 解释为何常把投稿标题改回原题，回应编辑行为带来的疑问。 | 438 | 220 | 2013-10-18 |
| 4 | [Ask HN: What are you working on and why is it cool?](https://news.ycombinator.com/item?id=6617551) | 你正在忙什么项目，它具体有哪些让人觉得有趣或酷的地方？ | 435 | 761 | 2013-10-26 |
| 5 | [Ask HN: Who is hiring? (October 2013)](https://news.ycombinator.com/item?id=6475879) | 十月招聘帖，请公司在开头说明地点及远程等候选人条件。 | 399 | 561 | 2013-10-01 |
| 6 | [My dad unexpectedly uses my Linux laptop to get real work done](https://news.ycombinator.com/item?id=6619993) | 原本留作电视播放的 Ubuntu 笔记本，意外被父亲拿来认真办公。 | 395 | 349 | 2013-10-26 |
| 7 | [Hacking the Olympics](https://news.ycombinator.com/item?id=6560740) | 三十六岁技术人追逐奥运梦想，作者分享朋友用研究寻找突破的尝试。 | 175 | 71 | 2013-10-16 |
| 8 | [Hacker News was down](https://news.ycombinator.com/item?id=6640210) | HN 离线又出现证书不可信警告，读者询问是攻击还是服务器问题。 | 172 | 94 | 2013-10-30 |
| 9 | [Ask HN: Why can't I see downvote or upvote arrows anywhere?](https://news.ycombinator.com/item?id=6616972) | 投票与踩帖箭头都不见了，读者想知道 HN 界面是否发生变化。 | 164 | 57 | 2013-10-26 |
| 10 | [Ask HN: Did your YC (or other incubator) startup fail? What are you doing now?](https://news.ycombinator.com/item?id=6480720) | 在 YC 或其他孵化器出来后创业失败的人，如今都在做什么？ | 151 | 56 | 2013-10-02 |

### 2013-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Started a stupid company. Failed. ](https://news.ycombinator.com/item?id=6805699) | 一位创业失败者讲述资金耗尽、住房被收回及养家压力交织的困境。 | 1344 | 407 | 2013-11-27 |
| 2 | [Hey developers, stop forcing me to login to unsubscribe](https://news.ycombinator.com/item?id=6704027) | 退订邮件却被要求先登录，作者请求开发者停止这种让人烦躁的设计。 | 453 | 133 | 2013-11-09 |
| 3 | [Ask HN: Google employees, why is G+ more important than your users?](https://news.ycombinator.com/item?id=6747713) | 对 YouTube 绑定 Google+ 感到不满，作者追问谷歌内部怎样看待用户体验。 | 353 | 274 | 2013-11-17 |
| 4 | [Ask HN: I'm 15, won a grant to develop a suicide prevention app, what next?](https://news.ycombinator.com/item?id=6754953) | 十五岁学生获得自杀预防应用资助后，想知道接下来该如何推进。 | 252 | 157 | 2013-11-18 |
| 5 | [Ask HN: Who is hiring? (November 2013)](https://news.ycombinator.com/item?id=6653437) | 十一月招聘机会汇总，邀请注明地点及实习、远程、签证支持。 | 240 | 389 | 2013-11-01 |
| 6 | [How much money are you earning from your software products?](https://news.ycombinator.com/item?id=6663444) | 你的软件产品现在赚了多少钱，作者向独立产品经营者征集收入情况。 | 199 | 190 | 2013-11-03 |
| 7 | [Ask HN: What are some good alternatives to HN?](https://news.ycombinator.com/item?id=6748001) | HN 首页已少有想读的内容，作者询问其他读者转向哪些信息来源。 | 182 | 110 | 2013-11-17 |
| 8 | [We're going to send out invitations to YC interviews close to midnight](https://news.ycombinator.com/item?id=6672578) | 负责发信的人身处不同时区，YC 提前说明面试邀请会接近午夜发送。 | 181 | 119 | 2013-11-05 |
| 9 | [Startup CEOs: you are overestimating your tech talent](https://news.ycombinator.com/item?id=6697988) | 作者认为一些获投资的创业公司 CEO 高估了技术团队，提出用人观察。 | 156 | 126 | 2013-11-08 |
| 10 | [Ask HN: To everybody who uses MapReduce: what problems do you solve?](https://news.ycombinator.com/item?id=6706545) | 实际使用 MapReduce 的人，究竟在用它解决哪些问题？ | 153 | 120 | 2013-11-10 |

### 2013-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Sent $35,104.11 USD to CoinBase. Never received Bitcoins](https://news.ycombinator.com/item?id=6929705) | 用户称向 Coinbase 转入三万五千多美元后，未按承诺日期收到比特币。 | 658 | 475 | 2013-12-18 |
| 2 | [Tell HN: How we bootstrapped to the #1 rated mattress on Amazon.com](https://news.ycombinator.com/item?id=6900625) | Tuft & Needle 分享自筹资金经营床垫公司，并称已获亚马逊高评分。 | 462 | 271 | 2013-12-13 |
| 3 | [Sent $10,701.03 to Coinbase. Still missing bitcoins.](https://news.ycombinator.com/item?id=6933360) | 向 Coinbase 支付一万多美元后比特币仍未到账，作者请求处理与解释。 | 343 | 133 | 2013-12-19 |
| 4 | [Ask HN: How to increase self-discipline as a self-employed person?](https://news.ycombinator.com/item?id=6979277) | 转为自由职业或自雇以后，怎样在缺少外部约束时保持自律？ | 343 | 121 | 2013-12-29 |
| 5 | [Ask HN: Who is hiring? (December 2013)](https://news.ycombinator.com/item?id=6827554) | 十二月招聘交流，请明确职位所在地点及不同候选人的申请条件。 | 286 | 321 | 2013-12-01 |
| 6 | [Ask HN: What book changed your life in 2013?](https://news.ycombinator.com/item?id=6975638) | 2013 年读过哪本真正影响生活的书，而不仅仅是觉得好看的书？ | 209 | 177 | 2013-12-28 |
| 7 | [How reddit tried to solve the "new link" problem. Why HN doesn't need a new algo](https://news.ycombinator.com/item?id=6834705) | 借 Reddit 处理新链接的经历，作者主张 HN 无需只靠修改排序算法。 | 198 | 67 | 2013-12-02 |
| 8 | [Ask HN: Best current model routers for OpenWRT, DD-WRT, Tomato, etc.?](https://news.ycombinator.com/item?id=6828699) | 想刷 OpenWRT、DD-WRT 等开源固件，如今该买哪款路由器？ | 195 | 119 | 2013-12-01 |
| 9 | [Ask HN: Those making $1,000+/month on side projects - what did you make?](https://news.ycombinator.com/item?id=6884552) | 靠业余项目每月净赚一千美元以上的人，你们具体做了什么？ | 160 | 163 | 2013-12-10 |
| 10 | [Ask HN: I have 89,830 sound clips of rare records. What should I do?](https://news.ycombinator.com/item?id=6838757) | 收藏者积累了近九万段稀有唱片试听，想知道这些音频可以怎样利用。 | 155 | 57 | 2013-12-03 |

### 2014-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Quick tip for developers who use OS X](https://news.ycombinator.com/item?id=7051091) | 在 OS X 终端按住 Option 点击当前行，即可把光标移到点击位置。 | 1145 | 395 | 2014-01-13 |
| 2 | [An Open Letter to HN from EFF, Demand Progress, and Cory Doctorow](https://news.ycombinator.com/item?id=7037532) | EFF、Demand Progress 与 Cory Doctorow 致信 HN，呼吁延续反对网络审查与监控的行动。 | 681 | 101 | 2014-01-10 |
| 3 | [Your best passive income? (2014)](https://news.ycombinator.com/item?id=7094402) | 2014 年再谈被动收入，邀请分享最有效、最值得继续的来源。 | 395 | 420 | 2014-01-21 |
| 4 | [Ask PG: Postmortem of the outage?](https://news.ycombinator.com/item?id=7015133) | 希望了解 HN 宕机的具体经过，读者请求一次技术故障复盘。 | 330 | 132 | 2014-01-07 |
| 5 | [Tell HN: Server Status](https://news.ycombinator.com/item?id=7069013) | HN 长时间离线后，维护者介绍硬件排查与替换机器的进展。 | 273 | 120 | 2014-01-16 |
| 6 | [Ask HN: What's your speciality, and what's your "FizzBuzz" equivalent?](https://news.ycombinator.com/item?id=6999429) | 你的专业领域里，什么小问题像 FizzBuzz 一样能快速检验基本功？ | 260 | 331 | 2014-01-02 |
| 7 | [Ask HN: Who is hiring? (January 2014)](https://news.ycombinator.com/item?id=6995020) | 2014 年一月职位汇总，邀请写清地点、远程与签证等条件。 | 241 | 287 | 2014-01-01 |
| 8 | [Ask HN: How to find part-time developer work?](https://news.ycombinator.com/item?id=7077234) | 想找非全职的开发工作，哪些途径适合寻找稳定兼职机会？ | 217 | 118 | 2014-01-17 |
| 9 | [Ask HN: What's the worst you've ever screwed up at work?](https://news.ycombinator.com/item?id=7144934) | 你在工作中闯过最大的祸是什么，当时怎样反应、后来如何处理？ | 217 | 309 | 2014-01-29 |
| 10 | [Ask PG: How would you fill out a YC application with YC as your idea?](https://news.ycombinator.com/item?id=7079543) | 假设 YC 本身是申请项目，PG 会怎样回答 YC 的申请表问题？ | 171 | 29 | 2014-01-18 |

### 2014-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who is hiring? (February 2014)](https://news.ycombinator.com/item?id=7162197) | 二月招聘帖，请公司说明工作地点及实习、远程、签证支持情况。 | 299 | 381 | 2014-02-01 |
| 2 | [Ask HN: Where are the 750k Bitcoins lost by Mt. Gox?](https://news.ycombinator.com/item?id=7318947) | Mt. Gox 丢失的七十五万枚比特币究竟去了哪里？ | 218 | 195 | 2014-02-28 |
| 3 | [Ask HN: What'd you do to get your first 100 users?](https://news.ycombinator.com/item?id=7248829) | 不只靠发 Reddit 和 HN，大家当初怎样找到第一百位用户？ | 214 | 153 | 2014-02-16 |
| 4 | [Ask HN: Should I sue drchrono (YC W11) for violating their contract w/ me?](https://news.ycombinator.com/item?id=7178004) | 医生称电子病历与账单服务商违约，求助是否该起诉 drchrono。 | 211 | 31 | 2014-02-04 |
| 5 | [Ask HN: Why isn't Erlang more popular?](https://news.ycombinator.com/item?id=7277797) | WhatsApp 引来关注后，作者追问 Erlang 为何仍未更广泛流行。 | 202 | 237 | 2014-02-21 |
| 6 | [Ask HN: What are some alternatives to HN?](https://news.ycombinator.com/item?id=7254884) | 寻找能发链接、可评论且更聚焦技术的社区，小站也欢迎推荐。 | 199 | 186 | 2014-02-17 |
| 7 | [Ask HN: Where I can post my startup to get beta users?](https://news.ycombinator.com/item?id=7248460) | 除了 BetaList 和 HN，还有哪里适合发布创业项目、寻找测试用户？ | 138 | 37 | 2014-02-16 |
| 8 | [Ask HN: Freelancer? Seeking freelancer? (February 2014)](https://news.ycombinator.com/item?id=7162201) | 二月自由职业信息交流，请供需双方注明所在地与远程合作安排。 | 128 | 160 | 2014-02-01 |
| 9 | [Ask HN: Best IRC channels?](https://news.ycombinator.com/item?id=7161236) | 开发、安全、网络与数据科学等领域，有哪些值得加入的 IRC 频道？ | 125 | 91 | 2014-02-01 |
| 10 | [I'm completely demotivated to work; what can I do?](https://news.ycombinator.com/item?id=7282618) | 距大学还有两年却完全缺乏学习动力，作者求助如何重新投入。 | 124 | 130 | 2014-02-22 |

### 2014-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Coming Soon to Hacker News: Pending Comments](https://news.ycombinator.com/item?id=7445761) | HN 宣布计划推出待审核评论功能，以改善社区评论质量。 | 661 | 805 | 2014-03-21 |
| 2 | [Ask HN: What happens to older developers?](https://news.ycombinator.com/item?id=7372997) | 软件开发者年纪渐长后会走向哪里，中后期职业生涯通常怎样展开？ | 554 | 358 | 2014-03-10 |
| 3 | [Ask HN: Is it me or ...?](https://news.ycombinator.com/item?id=7473787) | 每次加入喜欢的公司后都逐渐想离开，作者怀疑问题是否在自己身上。 | 465 | 256 | 2014-03-26 |
| 4 | [Ask HN: Successful one-person online businesses?](https://news.ycombinator.com/item?id=7367243) | 有没有独自经营成功网络生意的人，邀请介绍业务和最初起步的方法。 | 351 | 286 | 2014-03-09 |
| 5 | [I am a successful software dev but I have a serious drinking problem](https://news.ycombinator.com/item?id=7485673) | 软件开发曾带来财富却被酗酒毁掉生活，作者坦陈问题并寻求改变。 | 334 | 227 | 2014-03-28 |
| 6 | [Ask HN: Who is hiring? (March 2014)](https://news.ycombinator.com/item?id=7324236) | 三月职位集中帖，请雇主写清地点及候选人适用的工作条件。 | 311 | 429 | 2014-03-01 |
| 7 | [Twitter is blocked in Turkey](https://news.ycombinator.com/item?id=7439128) | 报告 Twitter 在土耳其被封锁，关注当地社交平台访问状况。 | 236 | 98 | 2014-03-20 |
| 8 | [Ask HN: Looking for contributors?](https://news.ycombinator.com/item?id=7360491) | 你的项目正在找贡献者吗，作者想为需要伙伴的开源与业余项目牵线。 | 225 | 133 | 2014-03-07 |
| 9 | [Ask YC (dang and kogir): How about some transparency?](https://news.ycombinator.com/item?id=7494500) | HN 更换管理者后，读者希望 dang 和 kogir 提高社区管理透明度。 | 218 | 57 | 2014-03-29 |
| 10 | [Tell HN: Meeting Satoshi ](https://news.ycombinator.com/item?id=7354326) | 作者回忆布鲁克林小店接受比特币的经历，并谈到一次“遇见中本聪”。 | 215 | 115 | 2014-03-06 |

### 2014-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [The crushing lameness of April Fools Day on the Internet.](https://news.ycombinator.com/item?id=7507297) | 作者厌倦互联网愚人节全天的刻意荒诞，质疑这些玩笑是否真好笑。 | 490 | 170 | 2014-04-01 |
| 2 | [Ask HN: CTO wants me to leave](https://news.ycombinator.com/item?id=7579845) | 后来加入的 CTO 希望技术创始人退出，作者求助如何面对团队冲突。 | 403 | 274 | 2014-04-13 |
| 3 | [Ask HN: What source code is worth studying?  ](https://news.ycombinator.com/item?id=7602237) | 多年之后再征集值得研读的源码，希望发现新一批设计出色的项目。 | 403 | 166 | 2014-04-17 |
| 4 | [Ask HN: Idea Sunday](https://news.ycombinator.com/item?id=7541601) | 发起“点子星期天”，把暂时无暇实现的产品想法交给社区交流。 | 369 | 567 | 2014-04-06 |
| 5 | [An Update on HN Comments](https://news.ycombinator.com/item?id=7605973) | 有人感觉 HN 评论近来改善，作者介绍自己观察到的变化与原因。 | 339 | 262 | 2014-04-17 |
| 6 | [Ask HN: Who is hiring? (April 2014)](https://news.ycombinator.com/item?id=7507765) | 四月招聘帖改用 VISA 标签，邀请公司标注地点、远程和相关支持。 | 337 | 527 | 2014-04-01 |
| 7 | [Ask HN: Your favorite YouTube channels?](https://news.ycombinator.com/item?id=7609584) | 哪些 YouTube 频道最值得订阅，技术编程之外的有趣内容也欢迎。 | 328 | 128 | 2014-04-18 |
| 8 | [Ask HN: Do you have a side project you want to sell?](https://news.ycombinator.com/item?id=7656154) | 更新业余项目交易讨论，邀请愿意卖出自己作品的人介绍情况。 | 323 | 502 | 2014-04-27 |
| 9 | [Ask HN: Idea Sunday](https://news.ycombinator.com/item?id=7582077) | 继续周日分享产品点子，让缺乏时间的人也能把想法送给别人。 | 305 | 441 | 2014-04-13 |
| 10 | [Challenge HN: Keep lame April Fools' gags off the front page](https://news.ycombinator.com/item?id=7506793) | 挑战社区别让乏味的愚人节恶作剧占据首页，把位置留给出色内容。 | 257 | 97 | 2014-04-01 |

### 2014-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who wants to be hired?](https://news.ycombinator.com/item?id=7685170) | 经管理者同意发起求职帖，邀请希望被雇用的人主动介绍自己。 | 559 | 365 | 2014-05-02 |
| 2 | [Tell HN: Call your mom](https://news.ycombinator.com/item?id=7728411) | 忙于编程和创业也别忘记父母，母亲节到了请给妈妈打电话。 | 555 | 110 | 2014-05-11 |
| 3 | [Ask HN: What do you do when your entire being opposes the task at hand?](https://news.ycombinator.com/item?id=7789014) | 整个身心都在抗拒手头功能开发，怎样处理这种反复发生的内耗？ | 395 | 201 | 2014-05-23 |
| 4 | [Ask HN: Who is hiring? (May 2014)](https://news.ycombinator.com/item?id=7679431) | 五月招聘集中帖，请列工作地点并明确实习、远程和签证安排。 | 336 | 491 | 2014-05-01 |
| 5 | [Ask HN: Idea Sunday](https://news.ycombinator.com/item?id=7693262) | 五月第一场点子星期天，邀请大家继续分享不一定亲自去做的创意。 | 219 | 199 | 2014-05-04 |
| 6 | [Ask HN: Can we get a "Show HN:" section](https://news.ycombinator.com/item?id=7737921) | 建议设立 Show HN 专区，让发布产品的帖子拥有更清楚的展示入口。 | 191 | 34 | 2014-05-13 |
| 7 | [Ask HN: As an experienced dev, how do you learn a language/framework quickly?](https://news.ycombinator.com/item?id=7733249) | 已有多年编程经验后，怎样更快上手下一门语言或框架？ | 144 | 66 | 2014-05-12 |
| 8 | [Ask HN: Freelancer? Seeking freelancer? (May 2014)](https://news.ycombinator.com/item?id=7679422) | 五月自由职业交流帖，让寻求合作的双方说明位置与远程可能性。 | 129 | 156 | 2014-05-01 |
| 9 | [Ask HN: How exactly does Hacker News 'points' work?](https://news.ycombinator.com/item?id=7809498) | 作者发现一次赞似乎不等于一分，询问 HN 的积分到底怎样计算。 | 129 | 67 | 2014-05-28 |
| 10 | [Ask HN: Can we do a "Who's looking for work?"](https://news.ycombinator.com/item?id=7682189) | 除了每月招聘帖，HN 是否也能定期发布“谁在找工作”？ | 121 | 61 | 2014-05-01 |

### 2014-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Thank HN: You guys helped me land my dream job.](https://news.ycombinator.com/item?id=7833251) | 一次社区牵线带来理想工作的录用，作者专程回来感谢 HN。 | 383 | 60 | 2014-06-02 |
| 2 | [Ask HN: Who is hiring? (June 2014)](https://news.ycombinator.com/item?id=7829042) | 六月招聘机会集中发布，请说明地点、远程与签证等工作条件。 | 314 | 422 | 2014-06-01 |
| 3 | [Tell HN: I want out](https://news.ycombinator.com/item?id=7928687) | 为自由生活而辞职，却经营出更忙碌的公司，作者表示自己想退出。 | 238 | 101 | 2014-06-22 |
| 4 | [Tell HN: The site was offline. What changed?](https://news.ycombinator.com/item?id=7872239) | HN 离线维护后更新存储路径，作者解释迁移结果与启动速度改善。 | 229 | 100 | 2014-06-10 |
| 5 | [Ask HN: What projects are you working on?](https://news.ycombinator.com/item?id=7957989) | 客户项目做完终于有空，作者想听听大家正在推进哪些个人作品。 | 219 | 502 | 2014-06-28 |
| 6 | [Tell HN: My startup is making money and I don't know what to do](https://news.ycombinator.com/item?id=7954905) | 帮助大学生寻找校外住房的 University Niche 开始赚钱，创始人纠结下一步。 | 211 | 128 | 2014-06-27 |
| 7 | [But why can't I send people their passwords?](https://news.ycombinator.com/item?id=7943365) | Plain-Text Offenders 维护者制作常见问答，解释为什么不该发送用户密码。 | 201 | 174 | 2014-06-25 |
| 8 | [Ask HN: Dev promoted to more strategic role in startup. What literature?](https://news.ycombinator.com/item?id=7937002) | 开发者被提升到更偏战略的角色，想找适合角色转换的阅读材料。 | 184 | 81 | 2014-06-24 |
| 9 | [What's an idea or creation that you've had success with locally that I can copy?](https://news.ycombinator.com/item?id=7960581) | 你在本地成功做过什么生意或项目，能否让别人复制到另一座城市？ | 176 | 105 | 2014-06-29 |
| 10 | [Ask HN: Did you start a company whilst employed?](https://news.ycombinator.com/item?id=7867603) | 在受雇期间成功创办公司的人，如何安排工作并处理与雇主的关系？ | 155 | 107 | 2014-06-09 |

### 2014-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Urgent connection to Twitter support](https://news.ycombinator.com/item?id=8006869) | 紧急预警账号即将触及 API 限额，管理员寻求 Twitter 支持人员协助。 | 875 | 127 | 2014-07-08 |
| 2 | [Ask HN: 16-hour work week jobs?](https://news.ycombinator.com/item?id=7994673) | 体验过每周工作十六小时后，发帖者寻求类似岗位并分享自己的感受。 | 662 | 261 | 2014-07-06 |
| 3 | [Ask HN Mods: Why Do You Completely Change What Users Submit?](https://news.ycombinator.com/item?id=8057287) | 投稿登上首页后内容被改动，作者质问 HN 管理者为何大幅修改提交。 | 386 | 163 | 2014-07-19 |
| 4 | [Offer HN: Free Use of Agricultural Land 30 miles Northwest of Chicago](https://news.ycombinator.com/item?id=8044029) | 芝加哥附近土地所有者免费提供农用地，希望有人带来可实践的项目。 | 354 | 113 | 2014-07-16 |
| 5 | [What was your best passive income in 2014?](https://news.ycombinator.com/item?id=8107588) | 2014 年你最好的被动收入是什么，再次征集可持续赚钱的实际经验。 | 323 | 466 | 2014-07-30 |
| 6 | [Ask HN: Who is hiring? (July 2014)](https://news.ycombinator.com/item?id=7970366) | 七月招聘帖，邀请公司写清地点和实习、远程、签证条件。 | 304 | 492 | 2014-07-01 |
| 7 | [Ask HN: How best to learn software design principles?](https://news.ycombinator.com/item?id=8000811) | 面试暴露软件设计不足，编码能力不错的作者想系统学习设计原则。 | 274 | 98 | 2014-07-07 |
| 8 | [Ask HN: Did you get "never have to work again rich" through software?](https://news.ycombinator.com/item?id=7977188) | 有没有靠软件赚到终身不必工作的人，作者询问路径与实现时的感受。 | 272 | 177 | 2014-07-02 |
| 9 | [Be aware of phishing at airbnb](https://news.ycombinator.com/item?id=8063035) | 推荐女友用 Airbnb 后碰到可疑情况，作者提醒租客注意钓鱼风险。 | 220 | 73 | 2014-07-21 |
| 10 | [Ask HN: What's the best technical eBook you have read?](https://news.ycombinator.com/item?id=7998382) | 你读过最好的技术电子书是什么，哪本值得同行花时间研读？ | 193 | 82 | 2014-07-07 |

### 2014-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who is hiring? (August 2014)](https://news.ycombinator.com/item?id=8120070) | 八月招聘信息汇总，请注明地点以及不同候选人的工作安排。 | 449 | 584 | 2014-08-01 |
| 2 | [Ask HN: I was hired and unhired in 2 weeks, for no reason](https://news.ycombinator.com/item?id=8152933) | 加入 YC 公司成为首位员工，两周后就因“计划改变”被解雇。 | 368 | 281 | 2014-08-08 |
| 3 | [Tox: A simple, distributed, free, secure Skype replacement. Now alpha with A/V](https://news.ycombinator.com/item?id=8123152) | 分布式免费通信工具 Tox 进入测试阶段，加入音视频以替代 Skype。 | 345 | 139 | 2014-08-01 |
| 4 | [Don't be a jerk](https://news.ycombinator.com/item?id=8148068) | 免费解答问题也耗费时间，作者用自身经历提醒大家善待帮助自己的人。 | 333 | 130 | 2014-08-07 |
| 5 | [I'm 25 years old and I am lost](https://news.ycombinator.com/item?id=8177259) | 创业被收购更像人才并购，二十五岁的作者辞职后仍渴望经营自己的事业。 | 309 | 264 | 2014-08-14 |
| 6 | [Ask HN: How to start earning $500/month in passive income in next 12-18 months?](https://news.ycombinator.com/item?id=8246255) | 有全职工作的 Rails 开发者，想在一年多内建立每月五百美元被动收入。 | 288 | 193 | 2014-08-30 |
| 7 | [Ask HN: Startup stole our software, and raised $2MM with it. What should we do?](https://news.ycombinator.com/item?id=8227225) | 开发公司称客户拖欠款项还拿软件融资两百万美元，求助如何追索。 | 231 | 67 | 2014-08-26 |
| 8 | [Ask HN: Who wants to be hired? (August 2014)](https://news.ycombinator.com/item?id=8120085) | 八月求职展示帖，邀请注明所在地、远程意愿、技术和简历。 | 225 | 329 | 2014-08-01 |
| 9 | [Ask HN: Who isn't in the software industry/not a hacker?](https://news.ycombinator.com/item?id=8154625) | 商业地产从业者想认识 HN 上其他不属于软件行业的读者。 | 157 | 190 | 2014-08-08 |
| 10 | [From the startup who allegedly stole software and raised $2M with it](https://news.ycombinator.com/item?id=8242361) | Pigeonly CEO 回应“窃取软件并融资”的指控，公开公司的说法。 | 157 | 109 | 2014-08-29 |

### 2014-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who is hiring? (September 2014)](https://news.ycombinator.com/item?id=8252715) | 九月招聘信息汇总，要求注明位置及实习、远程、签证安排。 | 224 | 324 | 2014-09-01 |
| 2 | [Chapter Two of Peter Thiel's New Book](https://news.ycombinator.com/item?id=8320491) | 获作者许可分享 Peter Thiel 新书第二章，邀请 HN 读者阅读讨论。 | 220 | 68 | 2014-09-15 |
| 3 | [Ask HN: Hackers who cook](https://news.ycombinator.com/item?id=8356489) | 喜欢做饭的黑客如何安排菜单与日常烹饪，作者邀请互通经验。 | 136 | 207 | 2014-09-23 |
| 4 | [Ask HN: What DB to use for huge time series?](https://news.ycombinator.com/item?id=8368509) | 要存储规模庞大的时间序列，哪种数据库比现有候选更合适？ | 126 | 130 | 2014-09-25 |
| 5 | [Ask HN: Who wants to be hired? (September 2014)](https://news.ycombinator.com/item?id=8252732) | 九月求职集中帖，供候选人展示技术、简历和迁居或远程偏好。 | 117 | 213 | 2014-09-01 |
| 6 | [Ask HN: What's your best startup idea that you're not going to pursue?](https://news.ycombinator.com/item?id=8266016) | 你最好的、但并不打算亲自追求的创业点子是什么？ | 101 | 207 | 2014-09-03 |
| 7 | [Ask HN: What's the best company to buy an SSL certificate from?](https://news.ycombinator.com/item?id=8344238) | 电商项目面向重视安全的企业客户，作者求推荐 SSL 证书提供商。 | 95 | 86 | 2014-09-20 |
| 8 | [Ask HN: I have to analyze 100M lines of Java – where do I start?](https://news.ycombinator.com/item?id=8257327) | 团队拿到一亿行 Java 代码准备分析和重建，第一步该从哪里下手？ | 87 | 122 | 2014-09-02 |
| 9 | [Shellshocking OpenVPN servers](https://news.ycombinator.com/item?id=8385332) | 某些 OpenVPN 配置会调用自定义脚本，作者提醒它们可能受 Shellshock 影响。 | 86 | 6 | 2014-09-29 |
| 10 | [Ask HN: How do I set up a HIPAA-compliant server?](https://news.ycombinator.com/item?id=8347418) | 怎样搭建符合 HIPAA 要求的服务器，医疗数据业务需要哪些安排？ | 68 | 52 | 2014-09-21 |

### 2014-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: How to price yourself?](https://news.ycombinator.com/item?id=8409020) | 在菲律宾从基础编程做起的开发者，想知道该怎样为自己的能力定价。 | 329 | 165 | 2014-10-04 |
| 2 | [Ask HN: My 56-year-old father is a developer having a tough time finding a job](https://news.ycombinator.com/item?id=8501149) | 五十六岁的父亲失业后求职艰难，子女向技术社区寻找帮助。 | 318 | 216 | 2014-10-23 |
| 3 | [Ask HN: How do you use Docker in production?](https://news.ycombinator.com/item?id=8470206) | 理解 Docker 原理后，生产环境里究竟有哪些问题能靠它解决得更好？ | 309 | 151 | 2014-10-17 |
| 4 | [Verizon Wireless injecting tracking UIDs into HTTP requests](https://news.ycombinator.com/item?id=8500131) | 作者报告 Verizon Wireless 向 HTTP 请求注入可追踪用户的唯一标识。 | 299 | 146 | 2014-10-23 |
| 5 | [How do you get to write so well in HN?](https://news.ycombinator.com/item?id=8533633) | HN 评论常清楚又有说服力，作者想知道怎样练成这样的表达能力。 | 276 | 105 | 2014-10-30 |
| 6 | [Ask HN: Who is hiring? (October 2014)](https://news.ycombinator.com/item?id=8394339) | 十月招聘集中发布，邀请标明地点及适用的远程等工作条件。 | 275 | 424 | 2014-10-01 |
| 7 | [Ask HN: Is the semantic web still a thing?](https://news.ycombinator.com/item?id=8510401) | 语义网曾被寄予厚望，如今还活跃吗，有哪些公司和项目继续做？ | 178 | 113 | 2014-10-26 |
| 8 | [Ask HN: Big company approached our stealth startup – what to do?](https://news.ycombinator.com/item?id=8417825) | 三人团队尚未公开发布就被行业大公司接触，该如何准备与对待？ | 159 | 81 | 2014-10-06 |
| 9 | [Ask HN: Are there any innovative startups in the porn/adult industry?](https://news.ycombinator.com/item?id=8478079) | 成人内容行业里有没有创新创业项目，在解决哪些实际问题？ | 126 | 127 | 2014-10-19 |
| 10 | [Ask HN: My VPS got hacked and now I'm facing a massive bill. What can I do?](https://news.ycombinator.com/item?id=8478159) | 个人 VPS 遭入侵后收到巨额账单，学生开发者求助如何协商处理。 | 110 | 77 | 2014-10-19 |

### 2014-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ezra Zygmuntowicz has died](https://news.ycombinator.com/item?id=8676140) | 报告 Engine Yard 联合创始人、Merb 开发者 Ezra Zygmuntowicz 去世。 | 429 | 69 | 2014-11-30 |
| 2 | [Ask HN: Can we talk about FreeBSD vs. Linux?](https://news.ycombinator.com/item?id=8645443) | 近期关注 FreeBSD 却难找好比较，作者希望与 Linux 用户深入交流。 | 352 | 214 | 2014-11-22 |
| 3 | [Ask HN: Who is hiring? (November 2014)](https://news.ycombinator.com/item?id=8542892) | 十一月招聘帖，请雇主写明地点和实习、远程、签证支持情况。 | 324 | 419 | 2014-11-01 |
| 4 | [Just had a heart attack](https://news.ycombinator.com/item?id=8550315) | 心脏病发作并接受急救手术后，作者从重症监护室分享自己的近况。 | 301 | 213 | 2014-11-03 |
| 5 | [Ask HN: How much recurring income do you generate and from what?](https://news.ycombinator.com/item?id=8629919) | 年度更新经常性收入调查，邀请老参与者和新人说说收入从何而来。 | 293 | 335 | 2014-11-19 |
| 6 | [Ask HN: What small webapps do you know that have a large audience?](https://news.ycombinator.com/item?id=8546617) | 有哪些功能不多、体量很小，却吸引了大量用户的网页应用？ | 274 | 163 | 2014-11-02 |
| 7 | [Tell HN: Wear a Helmet](https://news.ycombinator.com/item?id=8626433) | 从骑车通勤时不愿戴头盔说起，作者提醒大家认真保护自己。 | 272 | 183 | 2014-11-18 |
| 8 | [BrowserStack was hacked](https://news.ycombinator.com/item?id=8581477) | BrowserStack 支持账号发出异常邮件，作者报告疑似入侵并说明尚难核实。 | 262 | 108 | 2014-11-10 |
| 9 | [Ask HN: Founders whose startups have failed, where did life take you afterwards?](https://news.ycombinator.com/item?id=8578514) | 创业公司失败后，创始人的生活走向了哪里，又开启了什么新阶段？ | 235 | 172 | 2014-11-08 |
| 10 | [Thank You HN, Voxel Quest Is Funded](https://news.ycombinator.com/item?id=8572611) | Voxel Quest 众筹成功后，作者感谢 HN 社区与支持项目的投资者。 | 220 | 65 | 2014-11-07 |

### 2014-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Why is every story on Uber Delhi driver raping a passenger getting instakilled?](https://news.ycombinator.com/item?id=8711284) | 发帖者追问，为何有关德里 Uber 司机涉嫌强奸乘客的报道提交后迅速被屏蔽。 | 698 | 110 | 2014-12-07 |
| 2 | [Merry Christmas to HN](https://news.ycombinator.com/item?id=8795524) | 年初开始活跃的读者分享一年的学习收获，向 HN 送上圣诞祝福。 | 502 | 110 | 2014-12-25 |
| 3 | [Ask HN: How can I remedy scatter brain and information overload?](https://news.ycombinator.com/item?id=8710006) | 信息太多导致注意力分散、思绪混乱，作者求助如何恢复专注。 | 357 | 222 | 2014-12-06 |
| 4 | [Ask HN: How or where to begin learning mathematics from first principles?](https://news.ycombinator.com/item?id=8697772) | 编程和电子实践遇到数学瓶颈，怎样从第一原理重新学习数学？ | 345 | 123 | 2014-12-04 |
| 5 | [Ask HN: Who is hiring? (December 2014)](https://news.ycombinator.com/item?id=8681040) | 十二月招聘交流，请注明工作地点及远程等候选人条件。 | 335 | 565 | 2014-12-01 |
| 6 | [Ask HN: What book changed your life in 2014?](https://news.ycombinator.com/item?id=8716111) | 2014 年有哪些书改变了你的生活，让你看问题的方式发生转变？ | 329 | 284 | 2014-12-08 |
| 7 | [Ask HN: How do you stay motivated to work on side projects?](https://news.ycombinator.com/item?id=8800788) | 生活忙碌或新鲜感消失时，怎样仍能坚持写业余项目？ | 246 | 139 | 2014-12-26 |
| 8 | [If you're using YYYY in your JVM service or %G in anything, fix it now](https://news.ycombinator.com/item?id=8810157) | 日期格式的周年份与日历年份可能混淆，作者提醒检查 YYYY 和 %G。 | 228 | 73 | 2014-12-29 |
| 9 | [Ask HN: Examples of profitable little free web tools?](https://news.ycombinator.com/item?id=8699040) | 有没有免费提供的小网页工具，仍能为作者带来可观收入？ | 223 | 122 | 2014-12-04 |
| 10 | [Ask HN: What was the job market like during the dot-com crash?](https://news.ycombinator.com/item?id=8781768) | 互联网泡沫破裂时开发者的就业市场怎样，亲历者经历了什么？ | 189 | 155 | 2014-12-22 |

### 2015-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Those making $1,000+/month on side projects – what did you make?](https://news.ycombinator.com/item?id=8844083) | 2015 年再问：靠业余项目每月赚一千美元以上，你们做出了什么？ | 563 | 525 | 2015-01-06 |
| 2 | [Ask HN: What's left for early startup engineers as the company grows?](https://news.ycombinator.com/item?id=8881811) | 公司不断壮大、分工逐渐细化，早期工程师还能如何找到自己的位置？ | 463 | 186 | 2015-01-13 |
| 3 | [Ask HN: How do you find freelance/contract gigs?](https://news.ycombinator.com/item?id=8908279) | 全职开发者想增加收入，除了陌生邮件还有哪些获取合同项目的方法？ | 275 | 107 | 2015-01-18 |
| 4 | [Ask HN: Who is hiring? (January 2015)](https://news.ycombinator.com/item?id=8822808) | 2015 年一月职位集中帖，请标明地点与实习、远程、签证安排。 | 240 | 330 | 2015-01-01 |
| 5 | [Ask HN: Does anyone actually hire from 'developer bootcamps'?](https://news.ycombinator.com/item?id=8844848) | 开发训练营声称能迅速培养新人，真实雇主到底会不会招聘这些毕业生？ | 239 | 252 | 2015-01-06 |
| 6 | [Ask HN: I got let go this morning. What should I do next?](https://news.ycombinator.com/item?id=8973023) | 周五一早突然被解雇，作者想知道该怎样应对并安排下一步。 | 215 | 200 | 2015-01-30 |
| 7 | [Bitstamp Accounts Frozen](https://news.ycombinator.com/item?id=8837432) | 转发 Bitstamp 发给客户的邮件，关注账户冻结及交易异常情况。 | 190 | 107 | 2015-01-05 |
| 8 | [What does it take to run a web app with 5K – 10K users?](https://news.ycombinator.com/item?id=8862542) | 一个网页应用有五千至一万名用户时，运维与开发到底需要准备什么？ | 189 | 101 | 2015-01-09 |
| 9 | [Ask HN: What's the best way to write an API spec?](https://news.ycombinator.com/item?id=8912897) | 动手写 REST API 前想先列规范，应该用专门工具还是直接写文档？ | 170 | 56 | 2015-01-19 |
| 10 | [Tell HN: Google removes rust, Netflix, other GitHub repos after DMCA takedown](https://news.ycombinator.com/item?id=8848509) | 作者称谷歌依 DMCA 请求移除了多个正常 GitHub 仓库的搜索结果。 | 163 | 1 | 2015-01-07 |

### 2015-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: The “I want to do everything but end up doing nothing” dilemma](https://news.ycombinator.com/item?id=9049208) | 一名计算机专业学生求助：面对太多想学的方向，如何避免什么都没做成？ | 806 | 214 | 2015-02-14 |
| 2 | [Ask HN: Who is hiring? (February 2015)](https://news.ycombinator.com/item?id=8980047) | 二月招聘汇总，邀请公司注明地点、远程及其他候选人条件。 | 461 | 637 | 2015-02-01 |
| 3 | [Google Play Store: Browsing with Firefox is no longer supported on Android](https://news.ycombinator.com/item?id=9026815) | 安卓 Firefox 打开 Google Play 网页被提示不再支持，作者分享遇到的限制。 | 448 | 230 | 2015-02-10 |
| 4 | [Ask HN: What up with these startup salaries?](https://news.ycombinator.com/item?id=9052727) | 看到创业公司的薪酬广告后，作者质疑这些工资是否合理。 | 421 | 416 | 2015-02-15 |
| 5 | [Ask HN: Thoughts on Rich Hickey's advice on becoming a better developer?](https://news.ycombinator.com/item?id=9058437) | 作者整理 Rich Hickey 关于开发者成长的建议，邀请社区评价与讨论。 | 225 | 104 | 2015-02-16 |
| 6 | [Ask HN: What do you wish you had known before you turned 40?](https://news.ycombinator.com/item?id=9092246) | 快到四十岁的人生阶段，有哪些知识或经验是你希望更早知道的？ | 186 | 180 | 2015-02-23 |
| 7 | [Ask HN: TrueCrypt audit status?](https://news.ycombinator.com/item?id=9069295) | 社区筹款已久而更新不多，作者追问 TrueCrypt 安全审计的进展。 | 185 | 157 | 2015-02-18 |
| 8 | [Ask HN: How do your enterprise customers pay you?](https://news.ycombinator.com/item?id=9075768) | 企业客户通常用什么方式付 SaaS 账单，信用卡、转账和合同如何选择？ | 184 | 117 | 2015-02-19 |
| 9 | [Ask HN: How to manage developers who aren't very good?](https://news.ycombinator.com/item?id=9008845) | 带团队后遇到能力较弱的开发者，如何管理、指导并安排他们的工作？ | 179 | 203 | 2015-02-06 |
| 10 | [Google deleted whocalled.us for “Pure Spam” and replaced it with spam](https://news.ycombinator.com/item?id=9050343) | 站长称 whocalled.us 被谷歌按垃圾站移除，却让位给了真正的垃圾内容。 | 179 | 51 | 2015-02-14 |

### 2015-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [I Am Sam Altman, President of Y Combinator.  AMA](https://news.ycombinator.com/item?id=9238839) | YC 总裁 Sam Altman 开放问答，围绕申请、项目流程与创业解惑。 | 634 | 689 | 2015-03-20 |
| 2 | [Ask HN: Who is hiring? (March 2015)](https://news.ycombinator.com/item?id=9127232) | 三月招聘信息帖，雇主请说明岗位位置与适用的申请条件。 | 413 | 677 | 2015-03-01 |
| 3 | [Ask HN: Who are your favorite poets?](https://news.ycombinator.com/item?id=9291040) | 技术话题之外，你最喜欢哪些诗人，愿意向社区推荐谁？ | 349 | 344 | 2015-03-30 |
| 4 | [Ask HN: How to move beyond “freelancer”?](https://news.ycombinator.com/item?id=9289500) | 做了七年自由网页开发、有稳定工作但收入一般，下一步如何升级？ | 322 | 123 | 2015-03-30 |
| 5 | [Tell Sam Altman: I will take your bet](https://news.ycombinator.com/item?id=9271679) | 一位基金经营者公开回应 Sam Altman，表示愿意接下他的赌约。 | 298 | 127 | 2015-03-26 |
| 6 | [Ask HN: Does anyone else value the comments more than the link?](https://news.ycombinator.com/item?id=9251577) | 你会先读评论再打开链接吗，作者想知道是否也有人更珍惜讨论本身。 | 282 | 96 | 2015-03-23 |
| 7 | [Ask HN: The rising “Hackathon Hackers” culture](https://news.ycombinator.com/item?id=9205177) | 频繁参加黑客松的学生，邀请旁观者评价日渐兴起的黑客松文化。 | 251 | 153 | 2015-03-15 |
| 8 | [Ask HN: Favorite podcasts?](https://news.ycombinator.com/item?id=9207360) | 征集喜欢的播客，尤其欢迎编程和设计领域值得常听的节目。 | 239 | 134 | 2015-03-15 |
| 9 | [Any stories of employees with equity successfully taking home over $1m? $500k?](https://news.ycombinator.com/item?id=9225960) | 员工股权真的能兑现五十万乃至一百万美元吗，作者寻找实际案例。 | 213 | 196 | 2015-03-18 |
| 10 | [Ask HN: I am the dumbest person in the room. What should I do?](https://news.ycombinator.com/item?id=9269221) | 觉得自己是团队里能力最弱的人，该怎样成长并面对同事？ | 196 | 183 | 2015-03-26 |

### 2015-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [List of April Fools' Day Announcements](https://news.ycombinator.com/item?id=9302010) | 把愚人节产品公告收进同一条讨论，避免假新闻挤满首页。 | 592 | 538 | 2015-04-01 |
| 2 | [Ask HN: How do you deal with professional jealousy and getting older?](https://news.ycombinator.com/item?id=9337863) | 看到同行成就而焦虑、嫉妒，想独立发展的程序员如何面对年龄增长？ | 558 | 408 | 2015-04-07 |
| 3 | [Ask HN: Who is hiring? (April 2015)](https://news.ycombinator.com/item?id=9303396) | 四月招聘集中帖，请注明地点及实习、远程、签证等条件。 | 473 | 949 | 2015-04-01 |
| 4 | [Ask HN: What are the best product landing pages you've stumbled upon?](https://news.ycombinator.com/item?id=9440208) | 你遇到过哪些出色的产品落地页，能让人迅速理解并产生兴趣？ | 333 | 210 | 2015-04-26 |
| 5 | [Ask HN: When do you know your startup has failed?](https://news.ycombinator.com/item?id=9392780) | 数月没领工资、转做外包续命，创始人该如何判断公司是否已失败？ | 325 | 173 | 2015-04-17 |
| 6 | [Ask HN: What are the most uplifting comments you've read on HN?](https://news.ycombinator.com/item?id=9393213) | 哪些 HN 评论最温暖、最能让人重新振作，值得再拿出来分享？ | 325 | 67 | 2015-04-17 |
| 7 | [Ask HN: Should I testify?](https://news.ycombinator.com/item?id=9360093) | 律师希望作者作证指控前雇主违法，他纠结是否应该出庭。 | 292 | 238 | 2015-04-11 |
| 8 | [Ask HN: Those who quit their jobs to travel the world, how did it go?](https://news.ycombinator.com/item?id=9439286) | 真的辞职去环游世界的人，后来过得怎样，与想象有何不同？ | 247 | 168 | 2015-04-25 |
| 9 | [Ask HN: How do you log application events?](https://news.ycombinator.com/item?id=9444470) | 应用事件目前写进 SQL 表，作者询问更合适的日志记录与查询方式。 | 221 | 109 | 2015-04-27 |
| 10 | [Ask HN: How do technical non-developers help with open source projects?](https://news.ycombinator.com/item?id=9307255) | 更喜欢技术写作和项目管理的人，怎样为开源项目作出代码之外的贡献？ | 216 | 88 | 2015-04-01 |

### 2015-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Lily – Drone camera](https://news.ycombinator.com/item?id=9532777) | 介绍名为 Lily 的无人机摄像产品。 | 1397 | 480 | 2015-05-12 |
| 2 | [Tell HN: Thank you whoishiring, a.k.a. Matthew Walsh-Cloonagh](https://news.ycombinator.com/item?id=9635551) | 感谢主动建立每月招聘帖机制的 Matthew Walsh-Cloonagh，回看社区长期受益。 | 553 | 133 | 2015-05-31 |
| 3 | [Ask HN: Who is hiring? (May 2015)](https://news.ycombinator.com/item?id=9471287) | 五月招聘信息交流，招聘方请列清地点、远程和签证等支持。 | 501 | 893 | 2015-05-01 |
| 4 | [Ask HN: Where can I buy real software companies?](https://news.ycombinator.com/item?id=9588901) | 已有现金流的软件公司经营者，想收购另一家小公司，该去哪里找？ | 485 | 158 | 2015-05-22 |
| 5 | [Ask HN: How do I put together a computer for my blind mom?](https://news.ycombinator.com/item?id=9546311) | 常见读屏软件太复杂，作者想为失明母亲搭建容易使用的电脑界面。 | 339 | 78 | 2015-05-14 |
| 6 | [Ask HN: I Have Cancer. What Should I Do?](https://news.ycombinator.com/item?id=9628682) | 刚辞去旧工作准备加入小公司，却发现自己患癌，作者求助如何安排。 | 310 | 153 | 2015-05-30 |
| 7 | [Ask HN: Should I unplug my laptop charger at 100%?](https://news.ycombinator.com/item?id=9487903) | 笔记本充满电后要不要拔掉充电器，怎样使用才更适合电池？ | 308 | 237 | 2015-05-04 |
| 8 | [Go Lang: Comments Are Not Directives](https://news.ycombinator.com/item?id=9522973) | Go 开始借注释表达指令，作者担忧这会给语言长期设计带来问题。 | 279 | 219 | 2015-05-11 |
| 9 | [Ask HN: What are your recommended reads that are available for free?](https://news.ycombinator.com/item?id=9611219) | 有哪些可以免费阅读、同时又值得推荐的书或长篇资料？ | 224 | 129 | 2015-05-27 |
| 10 | [GitHub's down?](https://news.ycombinator.com/item?id=9497821) | GitHub 多个页面出现独角兽错误页，读者询问是否全站故障。 | 206 | 146 | 2015-05-06 |

### 2015-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Stripe Is the New PayPal](https://news.ycombinator.com/item?id=9738717) | Stripe 用户称支付被认定可能未经授权，且邮件未获回应，因此公开求助。 | 679 | 303 | 2015-06-18 |
| 2 | [Ask HN: Who is hiring? (June 2015)](https://news.ycombinator.com/item?id=9639001) | 六月职位集中帖，要求明确工作地点，并标注远程、实习和签证条件。 | 429 | 777 | 2015-06-01 |
| 3 | [Ask HN: How do you familiarize yourself with a new codebase?](https://news.ycombinator.com/item?id=9784008) | 拿到陌生代码库后，你会按什么顺序阅读、运行并建立理解？ | 407 | 238 | 2015-06-26 |
| 4 | [SpaceX – Launch Vehicle Failure](https://news.ycombinator.com/item?id=9793555) | 作者记录 SpaceX 火箭发射约三分钟后疑似爆炸的情况，关注后续消息。 | 381 | 335 | 2015-06-28 |
| 5 | [KeePass – questionable security](https://news.ycombinator.com/item?id=9727297) | 长期用户阅读 KeePass 2.x 源码后发现疑点，提出对其安全设计的担忧。 | 366 | 221 | 2015-06-16 |
| 6 | [Ask HN: I have ssh, they have ssh, how can we chat?](https://news.ycombinator.com/item?id=9716459) | 双方都有 SSH，能否不安装专用客户端，直接用终端互相聊天？ | 327 | 121 | 2015-06-14 |
| 7 | [ADP intentionally broke its Zenefits integration](https://news.ycombinator.com/item?id=9679312) | 作者转述 Zenefits 邮件，称 ADP 主动破坏了两家公司原有的系统集成。 | 306 | 117 | 2015-06-08 |
| 8 | [Tell HN: Entrepreneurs, make sure you are getting guaranteed wins in life](https://news.ycombinator.com/item?id=9782083) | 创业成败无法完全控制，作者提醒也要在生活中保留可确定的小收获。 | 266 | 78 | 2015-06-26 |
| 9 | [Ask HN: Open source OCR library?](https://news.ycombinator.com/item?id=9775753) | 尝试从图片识别文字却效果不佳，作者寻找好用的开源 OCR 库。 | 264 | 98 | 2015-06-25 |
| 10 | [Goodbye?](https://news.ycombinator.com/item?id=9665577) | 作者在自杀念头与求生愿望之间挣扎，向长期陪伴自己的 HN 社区求助。 | 245 | 114 | 2015-06-05 |

### 2015-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Hello](https://news.ycombinator.com/item?id=9910487) | 一位监狱看守向 HN 自我介绍，分享学习编程并准备申请 YC 的两年计划。 | 847 | 179 | 2015-07-19 |
| 2 | [Ask HN: Who is hiring? (July 2015)](https://news.ycombinator.com/item?id=9812245) | HN 二〇一五年七月招聘帖，汇集公司直接发布的职位与工作方式信息。 | 673 | 1086 | 2015-07-01 |
| 3 | [Ask HN: What tech blogs, podcasts do you follow outside of HN?](https://news.ycombinator.com/item?id=9836023) | 除了 HN，你还追哪些技术博客与播客，怎样保持日常学习？ | 333 | 141 | 2015-07-06 |
| 4 | [Ask HN: What is the actual purpose of Docker?](https://news.ycombinator.com/item?id=9844806) | 已有服务器能运行多个应用，Docker 额外解决的核心问题究竟是什么？ | 313 | 154 | 2015-07-07 |
| 5 | [A dataset of every Reddit comment](https://news.ycombinator.com/item?id=9869871) | 分享 Reddit 评论大规模数据集及下载方式，供研究社区历史与行为。 | 294 | 91 | 2015-07-11 |
| 6 | [Ask HN: I am busy with too many things at once](https://news.ycombinator.com/item?id=9823985) | 发现能力不足后同时学太多东西，作者求助如何在成长中保持重点。 | 282 | 118 | 2015-07-03 |
| 7 | [Ask HN: Good Python codebases to read?](https://news.ycombinator.com/item?id=9896369) | 学 Python 到阅读源码阶段，哪些代码库适合新手理解和模仿？ | 278 | 151 | 2015-07-16 |
| 8 | [Ask HN: How do I keep child porn out of my site?](https://news.ycombinator.com/item?id=9868352) | 网站经营者面临违法儿童性虐待内容风险，询问如何防范与清理上传。 | 252 | 186 | 2015-07-11 |
| 9 | [Ask HN: Why don't transistors in microchips fail?](https://news.ycombinator.com/item?id=9857094) | 芯片里有数十亿晶体管，为什么极少数器件失效不会让它经常坏掉？ | 194 | 111 | 2015-07-09 |
| 10 | [Ask HN: Has anyone here programmed in Kotlin? What do you think about it?](https://news.ycombinator.com/item?id=9946527) | Kotlin 功能看起来不错但用户不多，作者想听实际使用者对长期前景的看法。 | 190 | 199 | 2015-07-25 |

### 2015-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: I will help your startup in exchange for food and a place to stay](https://news.ycombinator.com/item?id=10032299) | 发帖者愿为创业公司编程，以食宿代替报酬，并说明自己的签证处境。 | 584 | 278 | 2015-08-10 |
| 2 | [Ask HN: Who is hiring? (August 2015)](https://news.ycombinator.com/item?id=9996333) | 八月职位汇总，招聘方请注明地点及远程、实习、签证支持。 | 504 | 969 | 2015-08-03 |
| 3 | [AWS S3 Outage](https://news.ycombinator.com/item?id=10033172) | AWS S3 美东接口大量返回 503，作者询问其他用户是否同样受影响。 | 268 | 131 | 2015-08-10 |
| 4 | [Ask HN: Who here would be interested in a free daily updated GeoIP database?](https://news.ycombinator.com/item?id=10030516) | 不满意免费 GeoIP 数据精度，作者询问是否有人需要每日更新的免费数据库。 | 266 | 122 | 2015-08-09 |
| 5 | [Ask HN: Books with a high signal to noise ratio?](https://news.ycombinator.com/item?id=10027102) | 非虚构书常内容稀薄，作者寻找信息密度高、少废话的好书。 | 260 | 200 | 2015-08-08 |
| 6 | [Ask HN: How to Find the Best Info on Cancer Treatments?](https://news.ycombinator.com/item?id=10143485) | 亲人确诊晚期胶质母细胞瘤，作者求助如何找到可靠的治疗信息。 | 188 | 86 | 2015-08-30 |
| 7 | [Ask HN: What does the percentage next to posts mean?](https://news.ycombinator.com/item?id=10101229) | HN 帖子旁出现的百分比代表什么，读者希望弄懂新的页面标记。 | 166 | 68 | 2015-08-22 |
| 8 | [Ask HN: Best resources on webapp security?](https://news.ycombinator.com/item?id=10027055) | 想系统建立安全网页应用，哪些资料适合学习实际防护方法？ | 165 | 42 | 2015-08-08 |
| 9 | [Ask HN: What are your best “soft skill” resources?](https://news.ycombinator.com/item?id=9987495) | 职业发展越来越需要技术之外的能力，作者征集软技能学习资源。 | 164 | 66 | 2015-08-01 |
| 10 | [Ask HN: How are some people exceptionally productive?](https://news.ycombinator.com/item?id=10011531) | 有些人似乎不断创造优秀项目，他们怎样做到远超常人的产出？ | 156 | 132 | 2015-08-05 |

### 2015-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who is hiring? (September 2015)](https://news.ycombinator.com/item?id=10152809) | 九月招聘集中帖，请写清位置及远程、实习和签证等条件。 | 436 | 864 | 2015-09-01 |
| 2 | [Tell HN: Clickable domains and other new features for story quality](https://news.ycombinator.com/item?id=10223645) | HN 试验可点击域名等功能，并调整重复链接检测以改善投稿质量。 | 306 | 155 | 2015-09-15 |
| 3 | [AWS US East is experiencing high error rates on several services](https://news.ycombinator.com/item?id=10247307) | AWS 美东多项服务出现高错误率，作者汇集受影响的服务状况。 | 276 | 170 | 2015-09-20 |
| 4 | [Tell HN: Paywalls with workarounds are OK; paywall complaints are off topic](https://news.ycombinator.com/item?id=10178989) | HN 说明允许可绕过付费墙的报道，并把单纯抱怨付费墙列为跑题。 | 176 | 160 | 2015-09-06 |
| 5 | [Ask HN: What stack would you use to build a CRUD web app on the JVM today?](https://news.ycombinator.com/item?id=10302879) | 今天要在 JVM 上搭建增删改查网站，你会选择怎样的技术栈？ | 157 | 207 | 2015-09-30 |
| 6 | [Ask HN: Best books or videos to get better at sales?](https://news.ycombinator.com/item?id=10233339) | 想把销售做得更好，有哪些书或视频真正值得学习？ | 147 | 69 | 2015-09-17 |
| 7 | [Ask HN: How do you manage and structure a team?](https://news.ycombinator.com/item?id=10248273) | 小团队正在变化，管理者该如何安排团队结构、职责与日常协作？ | 136 | 62 | 2015-09-20 |
| 8 | [Ask HN: Who wants to be hired? (September 2015)](https://news.ycombinator.com/item?id=10152811) | 九月求职展示帖，邀请候选人列出技术、简历、位置与迁居意愿。 | 112 | 181 | 2015-09-01 |
| 9 | [Tell HN: My own version of the American dream](https://news.ycombinator.com/item?id=10250708) | 作者回顾从软件工作出发的个人选择，分享自己理解的“美国梦”。 | 84 | 58 | 2015-09-21 |
| 10 | [Ask HN: What are the latest and greatest books on your favorite language?](https://news.ycombinator.com/item?id=10181953) | 你最常用的编程语言，有哪些更新及时、内容又实用的新书？ | 81 | 45 | 2015-09-07 |

### 2015-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: How to Be a Good Technical Lead?](https://news.ycombinator.com/item?id=10395046) | 从软件开发转为技术带头人，怎样才能做好一名技术负责人？ | 520 | 174 | 2015-10-15 |
| 2 | [Ask HN: Who is hiring? (October 2015)](https://news.ycombinator.com/item?id=10311580) | 十月招聘信息汇总，请说明职位位置与远程等候选人条件。 | 368 | 698 | 2015-10-01 |
| 3 | [I am Sam Altman, President of Y Combinator – AMA](https://news.ycombinator.com/item?id=10360911) | 冬季申请截止将近，Sam Altman 开放问答，回应 YC 及其他相关问题。 | 341 | 545 | 2015-10-09 |
| 4 | [Tell HN: Full Hacker News dataset now available on BigQuery](https://news.ycombinator.com/item?id=10440502) | 完整 HN 数据集已放上 BigQuery，作者介绍数据时间范围与来源。 | 238 | 43 | 2015-10-23 |
| 5 | [Ask HN: What visa do foreign YC founders use to stay in US beyond 3 months?](https://news.ycombinator.com/item?id=10400912) | 外国 YC 创始人如何留美超过三个月，长期签证是否要求最低融资额？ | 191 | 122 | 2015-10-16 |
| 6 | [Thank HN: for helping me get traction with DuckDuckGo and Traction book – AMA](https://news.ycombinator.com/item?id=10346268) | DuckDuckGo 创始人感谢 HN 帮助产品与《Traction》获得关注，并开放提问。 | 183 | 80 | 2015-10-07 |
| 7 | [Ask HN: Discuss burnout with boss?](https://news.ycombinator.com/item?id=10428008) | 自己调整一年仍然倦怠，作者想知道如何与老板开启这场谈话。 | 153 | 96 | 2015-10-21 |
| 8 | [Tell HN: Unicorns aren't ad-supported](https://news.ycombinator.com/item?id=10372789) | 观察高估值公司名单后，作者指出独角兽中主要依赖广告的公司并不多。 | 131 | 59 | 2015-10-12 |
| 9 | [Ask HN: How can you tell if you are insane?](https://news.ycombinator.com/item?id=10370320) | 担心手机电脑被入侵、家人却怀疑其判断，作者求助如何辨别自身状态。 | 88 | 88 | 2015-10-11 |
| 10 | [Ask HN: Implementing a graph database using Postgres tables for nodes and edges?](https://news.ycombinator.com/item?id=10316872) | 担心新图数据库不够成熟，能否用 Postgres 的节点表和边表自行实现？ | 87 | 60 | 2015-10-02 |

### 2015-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who is hiring? (November 2015)](https://news.ycombinator.com/item?id=10492086) | 十一月职位交流，招聘方请注明地点及远程、实习和签证支持。 | 512 | 880 | 2015-11-02 |
| 2 | [Ask HN: New attempt at mobile markup – keep or bail?](https://news.ycombinator.com/item?id=10489499) | HN 刚部署新的移动端页面方案，维护者征集保留还是撤回的反馈。 | 497 | 287 | 2015-11-02 |
| 3 | [Ask HN: What's your favorite online course?](https://news.ycombinator.com/item?id=10644518) | 你最喜欢哪门在线课程，技术相关或其他领域都可以推荐。 | 395 | 159 | 2015-11-29 |
| 4 | [Ask HN: Which open source projects have kind, supportive, talented teams?](https://news.ycombinator.com/item?id=10642500) | 想参与开源却在意合作氛围，有哪些项目团队友善、支持新人又有实力？ | 247 | 281 | 2015-11-28 |
| 5 | [Ask HN: How do develop a side project when you have a 40hr/week job?](https://news.ycombinator.com/item?id=10644373) | 每周认真工作四十小时之后，怎样还能留出精力开发自己的项目？ | 153 | 128 | 2015-11-29 |
| 6 | [Ask HN: How to form deep friendships later in life?](https://news.ycombinator.com/item?id=10579893) | 移居加拿大、毕业并工作多年后，作者想知道成年人怎样建立深厚友谊。 | 145 | 81 | 2015-11-17 |
| 7 | [Ask HN: How best to break up with cofounder?](https://news.ycombinator.com/item?id=10586258) | 共同点子已投入借款，合作却难继续，怎样妥善与联合创始人分开？ | 142 | 86 | 2015-11-18 |
| 8 | [Ask HN: Freelancer? Seeking freelancer? (November 2015)](https://news.ycombinator.com/item?id=10492087) | 十一月自由职业撮合帖，供需双方请列地点并说明能否远程协作。 | 117 | 153 | 2015-11-02 |
| 9 | [Ask HN: How do I stop comparing myself to others?](https://news.ycombinator.com/item?id=10523788) | 总觉得自己不如名校同龄人，计算机学生求助如何停止比较。 | 109 | 72 | 2015-11-07 |
| 10 | [Ask HN: What is your job? Do you like it? What was your favorite job?](https://news.ycombinator.com/item?id=10632809) | 你现在做什么工作、喜不喜欢，又最怀念哪份过去的工作？ | 106 | 80 | 2015-11-26 |

### 2015-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [I am Peter Roberts, an immigration lawyer who does work for YC and startups. AMA](https://news.ycombinator.com/item?id=10719080) | 为 YC 和创业公司工作的移民律师 Peter Roberts 开放提问。 | 313 | 310 | 2015-12-11 |
| 2 | [Stop looking at HN and go work that thing you promised yourself you'd work on](https://news.ycombinator.com/item?id=10764376) | 作者给自己也给同类读者一句提醒：先关掉 HN，去做答应自己的事。 | 281 | 83 | 2015-12-19 |
| 3 | [Ask HN: Who is hiring? (December 2015)](https://news.ycombinator.com/item?id=10655740) | 十二月招聘帖，要求明确工作地点与远程、实习、签证条件。 | 260 | 427 | 2015-12-01 |
| 4 | [Ask HN: Struggling to pay rent this month. Can I help you with a gig?](https://news.ycombinator.com/item?id=10813746) | 这个月房租面临困难，老社区成员用临时账号寻找能立即接手的项目。 | 251 | 37 | 2015-12-30 |
| 5 | [Ask HN: Papers you read in 2015?](https://news.ycombinator.com/item?id=10783983) | 2015 年你读到哪些值得分享的科研论文，欢迎推荐自己领域的作品。 | 193 | 45 | 2015-12-23 |
| 6 | [Ask HN: Novelty addiction is ruining my life and career. What should I do?](https://news.ycombinator.com/item?id=10724460) | 新鲜事物成瘾让项目不断半途而废，作者求助如何挽回职业与生活。 | 174 | 190 | 2015-12-12 |
| 7 | [Ask HN: Books you read in 2015?](https://news.ycombinator.com/item?id=10783219) | 这一年读过哪些书，是喜欢还是失望，邀请交流 2015 年阅读经历。 | 171 | 164 | 2015-12-23 |
| 8 | [Tell HN: Peter Roberts, immigration lawyer for YC, will do an AMA this Friday](https://news.ycombinator.com/item?id=10699795) | 预告移民律师 Peter Roberts 将来 HN 答疑，方便读者准备问题。 | 156 | 26 | 2015-12-08 |
| 9 | [Ask HN: Planning to leave. How best to handle stock options?](https://news.ycombinator.com/item?id=10695125) | 准备离职前，员工该怎样处理尚未行权的股票期权？ | 154 | 100 | 2015-12-08 |
| 10 | [Ask HN: What was your best passive income in 2015?](https://news.ycombinator.com/item?id=10726489) | 回顾 2015 年，哪种被动收入为你带来的回报最好？ | 120 | 118 | 2015-12-13 |

### 2016-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What sites do you use to find contract work?](https://news.ycombinator.com/item?id=10924877) | 寻找合同制项目时，你会使用哪些网站和平台？ | 358 | 162 | 2016-01-18 |
| 2 | [Ask HN: Who is hiring? (January 2016)](https://news.ycombinator.com/item?id=10822019) | 2016 年一月招聘集中帖，请列出地点与不同候选人的适用条件。 | 347 | 469 | 2016-01-01 |
| 3 | [Ask HN: What should we fund at YC Research?](https://news.ycombinator.com/item?id=10998486) | 已支持 OpenAI 并筹备基本收入研究，YC Research 下一步该资助什么？ | 316 | 522 | 2016-01-29 |
| 4 | [Ask HN: Which people and groups are researching new approaches to programming?](https://news.ycombinator.com/item?id=10926038) | 哪些个人或研究团队正在探索未来三十年的新编程方式？ | 263 | 121 | 2016-01-18 |
| 5 | [Ask HN: Is Knuth's TAOCP worth the time and effort?](https://news.ycombinator.com/item?id=10897460) | 买了《计算机程序设计艺术》后，作者想知道投入大量时间研读是否值得。 | 205 | 132 | 2016-01-13 |
| 6 | [Ask HN: How do prolific programmers go about their daily lives?](https://news.ycombinator.com/item?id=10963401) | 高产程序员既维护开源又不断写代码，他们的日常生活是怎样安排的？ | 196 | 81 | 2016-01-24 |
| 7 | [Ask HN: Do you use an old or 'unfashionable' programming language?](https://news.ycombinator.com/item?id=11001693) | 你还在用哪些不新潮的老语言，它们为何仍值得留在工具箱？ | 187 | 327 | 2016-01-30 |
| 8 | [Happy new year](https://news.ycombinator.com/item?id=10821154) | 向 HN 社区送上简短的新年问候，祝读者新年愉快。 | 177 | 58 | 2016-01-01 |
| 9 | [Ask HN: How does a 1990s web developer get back on track?](https://news.ycombinator.com/item?id=10874842) | 九十年代做过网站的人，如何跟上如今变化后的网页开发生态？ | 166 | 115 | 2016-01-10 |
| 10 | [Ask HN: Blacklist Forbes?](https://news.ycombinator.com/item?id=10871410) | 福布斯屏蔽广告拦截用户又涉及广告风险，读者建议屏蔽该站投稿。 | 164 | 41 | 2016-01-09 |

### 2016-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who is hiring? (February 2016)](https://news.ycombinator.com/item?id=11012044) | 二月职位汇总，请写明地点、远程以及实习或签证支持情况。 | 455 | 787 | 2016-02-01 |
| 2 | [Ask HN: How happy are you working as a programmer?](https://news.ycombinator.com/item?id=11009956) | 作为程序员工作让你有多快乐，职业体验是否符合最初的期待？ | 349 | 535 | 2016-02-01 |
| 3 | [Ask HN: Your Passive Income Suggestions?](https://news.ycombinator.com/item?id=11026699) | 被动收入有哪些真正有效或踩过坑的办法，邀请分享自己的经验。 | 327 | 227 | 2016-02-03 |
| 4 | [Ask HN: Is Python dying?](https://news.ycombinator.com/item?id=11100251) | Go、JavaScript、Julia 分别受到关注，Python 是否正失去位置？ | 240 | 348 | 2016-02-14 |
| 5 | [Multiple Black Vehicles with MD License Plates at Apple Executive Briefing Center](https://news.ycombinator.com/item?id=11120365) | 作者转述苹果高管会客中心外出现多辆马里兰车牌黑车的现场消息。 | 162 | 49 | 2016-02-17 |
| 6 | [Ask HN: Best way to learn HTML and CSS for web design?](https://news.ycombinator.com/item?id=11048409) | 平面设计师想转向网页设计，怎样学习 HTML 与 CSS 最合适？ | 156 | 65 | 2016-02-06 |
| 7 | [Ask HN: Is it possible to live off technical writing?](https://news.ycombinator.com/item?id=11198329) | 写技术书很费力却也有趣，靠兼职或全职技术写作能否维持生活？ | 148 | 64 | 2016-02-29 |
| 8 | [Ask HN: Does this old horse have a few years of useful work left?](https://news.ycombinator.com/item?id=11149361) | 离开微软一段不顺利的工作后，资深开发者怀疑自己是否仍有职业价值。 | 139 | 107 | 2016-02-22 |
| 9 | [Ask HN: How to handle 50GB of transaction data each day? (200GB during peak)](https://news.ycombinator.com/item?id=11157829) | 广告平台每天产生数十 GB、峰值两百 GB 的交易数据，该如何处理？ | 137 | 78 | 2016-02-23 |
| 10 | [Ask HN: What's going on at IBM?](https://news.ycombinator.com/item?id=11055365) | IBM 收入连续多季下滑，作者希望有人解释公司正在发生什么。 | 128 | 74 | 2016-02-07 |

### 2016-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: How much do you make at Amazon? Here is how much I make at Amazon](https://news.ycombinator.com/item?id=11312984) | 一位 Amazon 员工公开自己的薪酬，并邀请同事分享收入以改善谈薪信息差。 | 1213 | 690 | 2016-03-18 |
| 2 | [Tell HN: AngelList told my employer that I'd updated my profile](https://news.ycombinator.com/item?id=11326011) | 用户称更新 AngelList 资料后，平台冒用其身份向雇主发邮件确认项目。 | 958 | 224 | 2016-03-21 |
| 3 | [Ask HN: Who is hiring? (March 2016)](https://news.ycombinator.com/item?id=11202954) | 三月招聘信息交流，职位地点与远程等条件请在开头明确。 | 488 | 814 | 2016-03-01 |
| 4 | [I Am Sam Altman, President of Y Combinator.  AMA](https://news.ycombinator.com/item?id=11314597) | 夏季申请即将截止，Sam Altman 邀请社区提出关于 YC 等方面的问题。 | 429 | 725 | 2016-03-18 |
| 5 | [Ask HN: What are some examples of beautiful software?](https://news.ycombinator.com/item?id=11278065) | 读《黑客与画家》后想找实例：有哪些软件可以称得上“美”？ | 345 | 258 | 2016-03-13 |
| 6 | [Ask HN: What are you working on and why is it awesome? Please include URL](https://news.ycombinator.com/item?id=11259746) | 你正在做什么、为什么值得期待，作者邀请附上项目链接一起展示。 | 320 | 626 | 2016-03-10 |
| 7 | [HN: Please add Reddit style collapsible comments](https://news.ycombinator.com/item?id=11355038) | 请求 HN 加入类似 Reddit 的评论折叠，让长讨论更容易浏览。 | 311 | 109 | 2016-03-24 |
| 8 | [Ask HN: How much do you make at Google?](https://news.ycombinator.com/item?id=11314449) | 谷歌不同级别、不同地点的工程师，实际能获得怎样的薪酬？ | 193 | 81 | 2016-03-18 |
| 9 | [Ask HN: Moving Out of Silicon Valley because of housing? Where to?](https://news.ycombinator.com/item?id=11247368) | 因住房成本离开硅谷的人搬去了哪里，新城市的技术工作体验如何？ | 191 | 382 | 2016-03-08 |
| 10 | [Ask HN: Which successful startups were rejected by YC?](https://news.ycombinator.com/item?id=11229700) | 哪些后来成功的公司曾被 YC 拒绝，落选时的原因又是什么？ | 159 | 60 | 2016-03-05 |

### 2016-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Pick startups for YC to fund](https://news.ycombinator.com/item?id=11440627) | HN 邀请社区挑选创业公司，由 YC 提供资助。 | 867 | 286 | 2016-04-06 |
| 2 | [Ask HN: Describe your first enterprise sale](https://news.ycombinator.com/item?id=11515307) | 请描述你的第一笔企业销售：客户从何而来，首次会谈又怎样展开？ | 496 | 96 | 2016-04-17 |
| 3 | [Ask HN: Who is hiring? (April 2016)](https://news.ycombinator.com/item?id=11405239) | 四月招聘集中帖，请注明地点及远程、实习和签证安排。 | 427 | 713 | 2016-04-01 |
| 4 | [Apply HN: Pinboard – Make Y Combinator Great Again](https://news.ycombinator.com/item?id=11441480) | Pinboard 用夸张口吻参加 Apply HN，邀请关注这家自称增长缓慢的公司。 | 409 | 59 | 2016-04-06 |
| 5 | [Ask HN: How do you review code?](https://news.ycombinator.com/item?id=11416746) | 现有 GitHub PR 审查流程还有提升空间，大家怎样让代码评审更有效？ | 357 | 140 | 2016-04-03 |
| 6 | [Ask HN: How do detect a crappy boss / toxic environment when interviewing?](https://news.ycombinator.com/item?id=11449133) | 面试时看似不错、入职后却发现有毒，怎样提前识别糟糕老板和环境？ | 356 | 327 | 2016-04-07 |
| 7 | [Ask HN: Can't concentrate to focus, until it's last minute or later](https://news.ycombinator.com/item?id=11514266) | 总到最后一刻甚至逾期才能集中，作者求助如何改变这种工作模式。 | 351 | 191 | 2016-04-17 |
| 8 | [Ask HN: Can the “Who is Hiring?” post include a bit about the interview process?](https://news.ycombinator.com/item?id=11599991) | 建议每月招聘帖增加面试流程说明，减少候选人与公司双方的不确定。 | 328 | 109 | 2016-04-30 |
| 9 | [Stream PirateBay movies directly from CLI](https://news.ycombinator.com/item?id=11420166) | 分享直接从命令行串流播放 PirateBay 电影的做法。 | 249 | 204 | 2016-04-04 |
| 10 | [Ask HN: Best linux laptop right now?](https://news.ycombinator.com/item?id=11503951) | 工作可选新电脑，想从 Mac 回到 Linux，眼下哪款笔记本最合适？ | 185 | 158 | 2016-04-15 |

### 2016-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [My time with Rails is up](https://news.ycombinator.com/item?id=11749203) | 作者宣告自己与 Rails 的合作阶段结束，引出离开框架的讨论。 | 716 | 438 | 2016-05-22 |
| 2 | [Tell HN: Apply HN apology and revision](https://news.ycombinator.com/item?id=11647165) | HN 承认首次 Apply HN 实验结尾处理失误，提出道歉和修订安排。 | 653 | 206 | 2016-05-06 |
| 3 | [Ask HN: Who is hiring? (May 2016)](https://news.ycombinator.com/item?id=11611867) | 五月招聘帖，请明确职位所在地及远程、实习和签证条件。 | 553 | 936 | 2016-05-02 |
| 4 | [Ask HN: How do I deal with the first sexual harassment complaint at my startup?](https://news.ycombinator.com/item?id=11666857) | 新业务员工给同事发不当信息，创业团队首次遇到性骚扰投诉该如何处理？ | 401 | 580 | 2016-05-10 |
| 5 | [Ask HN: What's the best tool you used to use that doesn't exist anymore?](https://news.ycombinator.com/item?id=11694277) | 有哪些已经消失或被放弃的好工具，至今仍让你怀念？ | 331 | 868 | 2016-05-14 |
| 6 | [Ask HN: Oldest code you have written that is still in use?](https://news.ycombinator.com/item?id=11718197) | 软件常被改写或下线，你最早写下、如今仍在使用的代码是什么？ | 233 | 352 | 2016-05-17 |
| 7 | [Tell HN: Winners of Apply HN for YC Fellowship 3](https://news.ycombinator.com/item?id=11633270) | 公布 Apply HN 为 YC Fellowship 选出的项目，介绍社区决定名额的结果。 | 196 | 302 | 2016-05-05 |
| 8 | [Ask HN: Relationship between OO and functional programming?](https://news.ycombinator.com/item?id=11808551) | 借 Alan Kay 参与讨论的机会，作者请教面向对象与函数式编程的关系。 | 194 | 98 | 2016-05-31 |
| 9 | [Ask HN: Do I have to go through recruiters nowadays, how do you find new jobs?](https://news.ycombinator.com/item?id=11676417) | 求职帖带来大量猎头邮件，如今找新工作是否必须经过招聘中介？ | 185 | 144 | 2016-05-11 |
| 10 | [Ask HN: Passive Income Suggestions 2016](https://news.ycombinator.com/item?id=11755036) | 2016 年有哪些有效的被动收入策略，旧方法在今天还适用吗？ | 169 | 99 | 2016-05-23 |

### 2016-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Alan Kay has agreed to do an AMA today](https://news.ycombinator.com/item?id=11939851) | Alan Kay 同意在 HN 参加问答，与社区交流。 | 1401 | 893 | 2016-06-20 |
| 2 | [Ask HN: Who is hiring? (June 2016)](https://news.ycombinator.com/item?id=11814828) | 六月招聘信息帖，邀请说明工作地点以及远程、实习、签证条件。 | 644 | 1002 | 2016-06-01 |
| 3 | [Ask HN: Just got an innocent man out of prison. What now?](https://news.ycombinator.com/item?id=12010760) | 帮助一名无辜者获释后，法律学生兼黑客求助如何安排自己的下一步。 | 510 | 200 | 2016-06-30 |
| 4 | [Ask HN: What is your go-to example for a good REST API?](https://news.ycombinator.com/item?id=11971491) | 设计 REST API 需要参考时，你最常拿哪一个优秀接口作范例？ | 401 | 182 | 2016-06-24 |
| 5 | [I'm Peter Roberts, immigration attorney who does work for YC and startups. AMA](https://news.ycombinator.com/item?id=11972135) | 移民律师 Peter Roberts 再次来到 HN，回答创业者和社区的移民问题。 | 352 | 365 | 2016-06-24 |
| 6 | [Ask HN: I don't enjoy being a CTO.  Now what?](https://news.ycombinator.com/item?id=11893237) | 刚加入已有市场需求的公司担任 CTO，却发现并不喜欢角色，该怎么办？ | 326 | 219 | 2016-06-13 |
| 7 | [Ask HN: Do you have a profitable side project? How long did it take to achieve?](https://news.ycombinator.com/item?id=11898992) | 你有没有盈利的业余项目，从开始动手到赚到钱花了多久？ | 310 | 197 | 2016-06-14 |
| 8 | [Ask HN: Profitable SaaS? How did you grow your business?](https://news.ycombinator.com/item?id=11937132) | SaaS 已经盈利的经营者，是通过哪些方式把业务做大的？ | 295 | 109 | 2016-06-20 |
| 9 | [Ask HN: Examples of reliable software you enjoy using](https://news.ycombinator.com/item?id=11995816) | 在到处出错的软件之外，有哪些可靠又让你用得舒服的产品？ | 247 | 650 | 2016-06-28 |
| 10 | [Ask HN: What non-technical skills make a senior dev and how to develop them?](https://news.ycombinator.com/item?id=11907960) | 成为资深开发者还需要哪些非技术能力，又该怎样培养？ | 212 | 130 | 2016-06-15 |

### 2016-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: New features and a moderator](https://news.ycombinator.com/item?id=12073675) | HN 推出评论折叠、撤销投票与收藏等新功能，并介绍一位新版主。 | 2381 | 451 | 2016-07-11 |
| 2 | [Ask HN: What was your “why didn't I start doing this sooner” moment?](https://news.ycombinator.com/item?id=12186587) | 有哪些改变让你恍然大悟：“我为什么没有早点开始这样做？” | 630 | 767 | 2016-07-29 |
| 3 | [Ask HN: Who is hiring? (July 2016)](https://news.ycombinator.com/item?id=12016568) | 七月职位集中发布，请招聘方注明地点与远程等适用条件。 | 566 | 894 | 2016-07-01 |
| 4 | [Ask HN: Why don't companies hire programmers for fewer hours per day?](https://news.ycombinator.com/item?id=12161693) | 既然工作效率不总与工时成正比，公司为何很少招聘每天少工作几小时的程序员？ | 498 | 348 | 2016-07-25 |
| 5 | [Ask HN: Anonymous person sent proof of SSH access to our production server](https://news.ycombinator.com/item?id=12172379) | 匿名者发截图声称已 SSH 登录生产服务器，团队该如何核实并处理？ | 450 | 231 | 2016-07-27 |
| 6 | [Ask HN: Single Person startup/company?](https://news.ycombinator.com/item?id=12065355) | 受 Pinboard 财务数据启发，作者询问社区有多少真正的一人公司。 | 390 | 389 | 2016-07-10 |
| 7 | [Ask HN: What did your 'Show HN' project turn into?](https://news.ycombinator.com/item?id=12030863) | 你当年在 Show HN 展示的项目，后来成长、转变或结束成了什么？ | 382 | 279 | 2016-07-04 |
| 8 | [Ask HN: When you feel stuck in life](https://news.ycombinator.com/item?id=12143266) | 二十九岁、商科毕业后仍觉得人生卡住，作者向社区倾诉并寻找方向。 | 381 | 339 | 2016-07-22 |
| 9 | [Ask HN: Insider history of the demise of Kodak?](https://news.ycombinator.com/item?id=12111597) | 柯达发明数码相机却最终衰落，作者希望听到内部人士更完整的历史。 | 341 | 229 | 2016-07-17 |
| 10 | [Ask HN: Considerations when asked to write a book?](https://news.ycombinator.com/item?id=12118554) | 技术文章引来出版社邀约，首次写编程书前应该考虑哪些问题？ | 288 | 139 | 2016-07-18 |

### 2016-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Is it possible to run your own mail server for personal use?](https://news.ycombinator.com/item?id=12282231) | 个人邮件服务器搭起来不难，如何保证邮件实际投递与长期可用？ | 648 | 299 | 2016-08-13 |
| 2 | [Ask HN: Who is hiring? (August 2016)](https://news.ycombinator.com/item?id=12202865) | 八月招聘帖，请列工作地点并标注远程、实习和签证支持。 | 534 | 940 | 2016-08-01 |
| 3 | [Ask HN: Best passive income method for a solo developer?](https://news.ycombinator.com/item?id=12318449) | 技能丰富的独立开发者，怎样利用现有能力建立合适的被动收入？ | 427 | 244 | 2016-08-19 |
| 4 | [Ask HN: How do you get notified about newest research papers in your field?](https://news.ycombinator.com/item?id=12233289) | 你怎样及时获知自己研究领域刚发表的新论文？ | 406 | 135 | 2016-08-05 |
| 5 | [Ask HN: Failed interview, feeling unemployable and depressed – what do I do?](https://news.ycombinator.com/item?id=12348756) | 大厂跳槽面试失败后觉得无人愿雇，作者求助如何重建信心。 | 377 | 234 | 2016-08-24 |
| 6 | [Ask HN: What book have you given as a gift?](https://news.ycombinator.com/item?id=12243611) | 哪本书好到你愿意买来送人，让朋友也获得同样的阅读收获？ | 360 | 514 | 2016-08-07 |
| 7 | [Ask HN: What are good reads for designing APIs?](https://news.ycombinator.com/item?id=12262586) | 设计 API 有哪些值得读的书或资料，能帮助形成清晰接口？ | 319 | 96 | 2016-08-10 |
| 8 | [Ask HN: How do I write a resume after five years of a startup?](https://news.ycombinator.com/item?id=12221051) | 创业五年后准备转向更大的公司，创始人该如何把经历写成简历？ | 245 | 127 | 2016-08-03 |
| 9 | [Ask HN: How Did You Escape 9 to 5?](https://news.ycombinator.com/item?id=12398290) | 你当初如何从朝九晚五走向自己的生意，又怎样利用转型前的时间？ | 226 | 172 | 2016-08-31 |
| 10 | [Ask HN: What's the best library for making cross-platform UIs?](https://news.ycombinator.com/item?id=12376242) | 需要制作跨平台用户界面，哪些库最值得选择？ | 223 | 221 | 2016-08-28 |

### 2016-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Is web programming a series of hacks on hacks?](https://news.ycombinator.com/item?id=12477190) | 一位开发者求问，网页编程是否是不断在补丁上叠加补丁？ | 822 | 661 | 2016-09-12 |
| 2 | [Ask HN: What's your favorite HN post?](https://news.ycombinator.com/item?id=12496558) | 再征集最喜欢的 HN 帖子，作者特别想发现近来值得收藏的新讨论。 | 692 | 137 | 2016-09-14 |
| 3 | [Ask HN: Who is hiring? (September 2016)](https://news.ycombinator.com/item?id=12405698) | 九月职位集中帖，请说明地点及远程、实习、签证等工作条件。 | 521 | 906 | 2016-09-01 |
| 4 | [Ask HN: What are the must-read books about economics/finance?](https://news.ycombinator.com/item?id=12556160) | 统计工程学生希望进入金融领域，哪些经济与金融书属于必读？ | 446 | 269 | 2016-09-22 |
| 5 | [I Am Sam Altman, President of YC Group. AMA](https://news.ycombinator.com/item?id=12593689) | 冬季申请截止前一周，YC Group 总裁 Sam Altman 回答社区提问。 | 345 | 433 | 2016-09-27 |
| 6 | [Ask HN: What are the best practises for using SSH keys?](https://news.ycombinator.com/item?id=12574510) | 从升级 ED25519 密钥引出讨论，SSH 密钥怎样管理和使用才安全？ | 306 | 110 | 2016-09-25 |
| 7 | [Ask HN: What's the best way to learn about the blockchain?](https://news.ycombinator.com/item?id=12571287) | 现有区块链书籍常被批评浅薄，哪里能获得扎实、不浮泛的入门？ | 259 | 74 | 2016-09-24 |
| 8 | [Ask HN: When are you considered a “senior” programmer?](https://news.ycombinator.com/item?id=12603303) | 从熟练完成工作到被称为“资深程序员”，中间的界线究竟是什么？ | 218 | 152 | 2016-09-29 |
| 9 | [Ask HN: What do you wish someone would build?](https://news.ycombinator.com/item?id=12567645) | 你希望有人做出什么东西，无论是为自己还是为某个行业解决问题？ | 186 | 526 | 2016-09-23 |
| 10 | [Ask HN: Where do you go for civil discussion on the Internet?](https://news.ycombinator.com/item?id=12412661) | 网上哪里还能文明讨论政治、经济与其他一般话题，认真听彼此说话？ | 183 | 221 | 2016-09-02 |

### 2016-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What is your favorite YouTube channel for developers?](https://news.ycombinator.com/item?id=12702651) | HN 用户推荐适合开发者学习编程技术与实践的 YouTube 频道。 | 1081 | 171 | 2016-10-13 |
| 2 | [Ask HN: What is your favorite internet rabbit hole?](https://news.ycombinator.com/item?id=12778836) | HN 用户分享那些越查越深入、让人停不下来的网络话题。 | 1036 | 454 | 2016-10-24 |
| 3 | [Ask HN: How to get started with machine learning?](https://news.ycombinator.com/item?id=12713056) | 没有机器学习背景的软件工程师，应该按什么顺序开始学习？ | 950 | 125 | 2016-10-15 |
| 4 | [Ask HN: What's your favorite tech talk?](https://news.ycombinator.com/item?id=12637239) | 最喜欢的技术演讲或培训是什么，单次讲座和完整课程都欢迎。 | 848 | 255 | 2016-10-04 |
| 5 | [Ask HN: Who is hiring? (October 2016)](https://news.ycombinator.com/item?id=12627852) | 十月招聘机会汇总，请明确地点与远程等申请条件。 | 620 | 976 | 2016-10-03 |
| 6 | [Ask HN: Any other blind devs interested in working on dev tools for the blind?](https://news.ycombinator.com/item?id=12819482) | 一年失去四份工作的盲人开发者，寻找伙伴共同改进面向盲人的开发工具。 | 530 | 133 | 2016-10-28 |
| 7 | [Ask HN: What are the best personal project websites you've seen?](https://news.ycombinator.com/item?id=12804406) | 想用个人网站展示研究成果，有哪些项目网站的设计值得借鉴？ | 516 | 291 | 2016-10-27 |
| 8 | [Ask HN: $1k+ side projecters, what was the best thing you did to market it?](https://news.ycombinator.com/item?id=12720636) | 业余项目月收入超过一千美元的人，做过最有效的营销动作是什么？ | 494 | 143 | 2016-10-16 |
| 9 | [Massive Dyn DNS outage](https://news.ycombinator.com/item?id=12759520) | Dyn DNS 大规模中断，多家常用网站无法访问，作者汇集受影响名单。 | 391 | 265 | 2016-10-21 |
| 10 | [Ask HN: Those making over $1K/month on side projects, what did you make?](https://news.ycombinator.com/item?id=12670731) | SaaS、手机应用或其他业余项目，每月赚过一千美元的你具体做了什么？ | 373 | 245 | 2016-10-09 |

### 2016-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Dear Google, Apple, Mozilla, and MS: Please End Auto-Playing Media in Browsers](https://news.ycombinator.com/item?id=12942465) | 发帖者呼吁主要浏览器厂商停止默认自动播放音频与视频。 | 1358 | 318 | 2016-11-13 |
| 2 | [Ask HN: Who is firing?](https://news.ycombinator.com/item?id=12851987) | 经历公司管理失误后，发帖者邀请社区讨论哪些公司正在裁员或流失员工。 | 1087 | 432 | 2016-11-02 |
| 3 | [Ask HN: Who is hiring? (November 2016)](https://news.ycombinator.com/item?id=12846216) | 十一月职位帖，请招聘公司说明位置及远程、实习、签证支持。 | 711 | 1130 | 2016-11-01 |
| 4 | [Ask HN: What simple tools or products are you most proud of making?](https://news.ycombinator.com/item?id=12957371) | 你做过最自豪的简单工具或产品是什么，小工具与课程读物都可以。 | 526 | 868 | 2016-11-15 |
| 5 | [Ask HN: How to make a career working remotely?](https://news.ycombinator.com/item?id=12843590) | 有机器学习博士背景的工程师，想了解怎样建立长期远程职业生涯。 | 435 | 93 | 2016-11-01 |
| 6 | [Ask HN: Have you ever thought of leaving programming for something else?](https://news.ycombinator.com/item?id=12897284) | 有没有想过离开编程去做别的事，如果转行你会选择什么？ | 388 | 548 | 2016-11-08 |
| 7 | [Ask HN: Any good resources for finding software jobs abroad?](https://news.ycombinator.com/item?id=12906019) | 想寻找海外软件工作，有哪些实用的资源和渠道？ | 367 | 227 | 2016-11-09 |
| 8 | [Tell HN: Riseup.net fails to update canary; fingerprints deleted without notice](https://news.ycombinator.com/item?id=13007234) | 作者注意到 Riseup 的金丝雀声明未更新、证书指纹消失，追问相关变化。 | 317 | 127 | 2016-11-21 |
| 9 | [Ask HN: How Can I Get into NLP (Natural Language Processing)?](https://news.ycombinator.com/item?id=12916498) | 对自然语言处理产生兴趣，作者寻找从入门到深入的学习资源。 | 297 | 43 | 2016-11-10 |
| 10 | [Ask HN: How do you handle the business structure and taxes of side projects?](https://news.ycombinator.com/item?id=12949995) | 业余项目已有收入，是否注册公司、如何申报纳税和安排业务结构？ | 260 | 139 | 2016-11-14 |

### 2016-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Political Detox Week – No politics on HN for one week](https://news.ycombinator.com/item?id=13108404) | HN 试行一周“政治排毒”，暂时将政治新闻与相关讨论列为离题内容。 | 1630 | 1214 | 2016-12-05 |
| 2 | [Ask HN: What was your best passive income in 2016?](https://news.ycombinator.com/item?id=13150144) | 2016 年最好的被动收入来自什么，游戏、开源或其他小项目都欢迎。 | 779 | 678 | 2016-12-11 |
| 3 | [Ask HN: What problem in your industry is a potential startup?](https://news.ycombinator.com/item?id=13139638) | 你所在行业里，哪个尚未解决的问题最有机会变成一家创业公司？ | 658 | 705 | 2016-12-09 |
| 4 | [Ask HN: Who is hiring? (December 2016)](https://news.ycombinator.com/item?id=13080280) | 十二月招聘交流帖，请注明地点与远程、实习、签证等条件。 | 458 | 828 | 2016-12-01 |
| 5 | [Ask HN: How do I get freelance developer jobs?](https://news.ycombinator.com/item?id=13207268) | 接单平台限制竞标次数，新自由开发者怎样更有效地获得工作？ | 433 | 108 | 2016-12-18 |
| 6 | [Ask HN: Books you read in 2016?](https://news.ycombinator.com/item?id=13235767) | 2016 年读过哪些书，哪些值得推荐、哪些出乎意料地带来收获？ | 414 | 321 | 2016-12-22 |
| 7 | [Ask HN: What is something you do for clients that consistently blows them away?](https://news.ycombinator.com/item?id=13155589) | 你为客户做过什么，几乎每次都能让对方感到惊喜？ | 402 | 273 | 2016-12-12 |
| 8 | [Ask HN: Where is AI/ML actually adding value at your company?](https://news.ycombinator.com/item?id=13159908) | AI 与机器学习在你的公司里，究竟在哪些具体环节创造了价值？ | 385 | 195 | 2016-12-12 |
| 9 | [Ask HN: What do you want to learn in 2017?](https://news.ycombinator.com/item?id=13255650) | 新的一年你想学会什么，邀请大家列出 2017 年的学习愿望。 | 357 | 494 | 2016-12-25 |
| 10 | [Ask HN: Are there any systematic and scientific ways to develop a habit?](https://news.ycombinator.com/item?id=13095595) | 跑步、读书等日常习惯总坚持不住，有没有系统且有科学依据的方法？ | 334 | 128 | 2016-12-03 |

### 2017-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Successful one-person online businesses?](https://news.ycombinator.com/item?id=13326535) | 三年后再问一人网络生意：如今哪些独自经营的项目真正成功了？ | 800 | 629 | 2017-01-05 |
| 2 | [Ask HN: What's the best computer science book you've read recently?](https://news.ycombinator.com/item?id=13406638) | 最近读过最好的计算机科学书是哪本，值得推荐给其他开发者吗？ | 670 | 186 | 2017-01-15 |
| 3 | [Ask HN: Are we overcomplicating software development?](https://news.ycombinator.com/item?id=13426896) | 改造低效团队的经历让作者发问：我们是否把软件开发弄得太复杂了？ | 639 | 368 | 2017-01-18 |
| 4 | [Ask HN: Who is hiring? (January 2017)](https://news.ycombinator.com/item?id=13301832) | 2017 年一月招聘帖，邀请明确工作地点和不同候选人的申请条件。 | 612 | 930 | 2017-01-02 |
| 5 | [Ask HN: Which developers do you closely follow?](https://news.ycombinator.com/item?id=13520891) | 关注高手的创作能带来灵感，你长期追踪哪些开发者的工作？ | 551 | 264 | 2017-01-30 |
| 6 | [Ask HN: What is the best online resource to learn advanced SQL?](https://news.ycombinator.com/item?id=13417326) | 常被复杂 SQL 查询难住，作者想找深入学习 SQL 的在线资源。 | 448 | 97 | 2017-01-17 |
| 7 | [Ask HN: If you were to switch career, what would you do?](https://news.ycombinator.com/item?id=13334480) | 如果暂时告别技术行业和开发工作，你最想转去哪个职业或领域？ | 444 | 833 | 2017-01-06 |
| 8 | [Ask HN: What inspires you to persevere through adversity?](https://news.ycombinator.com/item?id=13454699) | 反复失败后，什么事物能让你继续坚持，不被逆境打倒？ | 401 | 231 | 2017-01-22 |
| 9 | [Ask HN: Excluding WordPress, what is your favorite for blogs or small stores?](https://news.ycombinator.com/item?id=13300023) | 不选 WordPress 时，搭建博客或小商店你最喜欢用什么？ | 339 | 192 | 2017-01-02 |
| 10 | [Ask HN: Have you ever worked on a product that was killed by technical debt?](https://news.ycombinator.com/item?id=13416935) | 你是否参与过最终被技术债务拖垮的产品，当时发生了什么？ | 306 | 324 | 2017-01-17 |

### 2017-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Is S3 down?](https://news.ycombinator.com/item?id=13755673) | 用户在 AWS 控制台查看 S3 时收到内部错误，询问服务是否宕机。 | 2589 | 1055 | 2017-02-28 |
| 2 | [Ask HN: What are some books where the reader learns by building one project?](https://news.ycombinator.com/item?id=13660086) | 像《Build Your Own Lisp》一样，哪些书通过逐步完成一个项目来教学？ | 813 | 229 | 2017-02-16 |
| 3 | [Ask HN: Who is hiring? (February 2017)](https://news.ycombinator.com/item?id=13541679) | 二月职位汇总，请招聘方列明地点与远程、实习和签证安排。 | 690 | 1222 | 2017-02-01 |
| 4 | [Ask HN: What is the biggest untapped opportunity for startups?](https://news.ycombinator.com/item?id=13576236) | 创业最大的未开发机会在哪里，哪些市场问题还少有人认真尝试？ | 657 | 1002 | 2017-02-06 |
| 5 | [Ask HN: What're the best-designed things you've ever used?](https://news.ycombinator.com/item?id=13682949) | 从一把设计出色的水壶说起，征集你用过最好的设计物品。 | 597 | 1064 | 2017-02-19 |
| 6 | [Ask HN: What is the most exciting development in your field right now?](https://news.ycombinator.com/item?id=13571847) | 在你的专业领域里，眼下最令人兴奋的新进展是什么？ | 516 | 424 | 2017-02-05 |
| 7 | [Ask HN: How would you turn Twitter around?](https://news.ycombinator.com/item?id=13746549) | 如果你来当 Twitter CEO，2017 年会怎样让这家公司扭转局面？ | 452 | 600 | 2017-02-27 |
| 8 | [Ask HN: What's your top growth strategy that helped grow your startup?](https://news.ycombinator.com/item?id=13550492) | 哪条增长策略最有效，真正推动你的创业公司跨过了一个阶段？ | 369 | 158 | 2017-02-02 |
| 9 | [Ask HN: What is so great about Bloomberg Terminal?](https://news.ycombinator.com/item?id=13736009) | 彭博终端为何让人愿意付费，专用屏幕、键盘与信息服务究竟好在哪里？ | 361 | 216 | 2017-02-26 |
| 10 | [Ask HN: How do you deal with loss of motivation?](https://news.ycombinator.com/item?id=13735610) | 刚换工作不久却提不起劲、任务缺乏挑战，作者想找回生活与工作动力。 | 331 | 167 | 2017-02-26 |

### 2017-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What do you want to see in Ubuntu 17.10?](https://news.ycombinator.com/item?id=14002821) | Ubuntu 产品经理向 HN 征集 17.10 版本的意见与功能需求。 | 1374 | 1145 | 2017-03-31 |
| 2 | [Ask HN: What are some good technology blogs to follow?](https://news.ycombinator.com/item?id=13849430) | 每天都看 HN 之外，还有哪些技术博客能稳定提供好内容？ | 893 | 187 | 2017-03-12 |
| 3 | [Ask HN: Developers with kids, how do you skill up?](https://news.ycombinator.com/item?id=13816627) | 有了孩子以后，开发者怎样继续提升技能并兼顾家庭生活？ | 589 | 511 | 2017-03-08 |
| 4 | [Ask HN: How do you set prices?](https://news.ycombinator.com/item?id=13840282) | 帮创业公司决定产品价格，哪些方法、工具和原则最有用？ | 584 | 175 | 2017-03-10 |
| 5 | [Ask HN: Which Berkeley Courses Should I Archive?](https://news.ycombinator.com/item?id=13867016) | 伯克利课程视频即将下架，作者询问哪些课程最值得优先归档。 | 512 | 148 | 2017-03-14 |
| 6 | [Ask HN: Who is hiring? (March 2017)](https://news.ycombinator.com/item?id=13764728) | 三月招聘集中帖，邀请注明位置及远程、实习和签证支持。 | 478 | 1052 | 2017-03-01 |
| 7 | [Ask HN: How do I start my own consulting firm?](https://news.ycombinator.com/item?id=13845681) | 已有前后端与运维经验的资深开发者，怎样从受雇走向自己的咨询公司？ | 476 | 112 | 2017-03-11 |
| 8 | [Paypal Horror Story 40k Frozen No Answers](https://news.ycombinator.com/item?id=13851120) | 作者称 PayPal 冻结四万资金又迟迟不解释，分享账户处理困境。 | 404 | 243 | 2017-03-12 |
| 9 | [Ask HN: What do you use to align your daily todos with your long term goals?](https://news.ycombinator.com/item?id=13855577) | 每天的待办清单怎样与一年目标对齐，避免忙碌却偏离长期方向？ | 379 | 212 | 2017-03-13 |
| 10 | [Ask HN: Best books on AI?](https://news.ycombinator.com/item?id=13900153) | AI 背景不多、偏好实际应用，哪些人工智能书适合入门阅读？ | 375 | 91 | 2017-03-18 |

### 2017-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Best business advice for software developers](https://news.ycombinator.com/item?id=14146850) | 软件开发者转为创业者后，最希望当初就懂得哪一条商业经验？ | 847 | 312 | 2017-04-19 |
| 2 | [Ask HN: Building a side project that makes money. Where to start?](https://news.ycombinator.com/item?id=14039135) | 日常工作耗尽创意后，想做能赚钱的业余项目，该从哪里寻找切口？ | 602 | 248 | 2017-04-05 |
| 3 | [Ask HN: Who is hiring? (April 2017)](https://news.ycombinator.com/item?id=14023198) | 四月职位交流帖，请列出工作地点和远程等候选人条件。 | 513 | 940 | 2017-04-03 |
| 4 | [Ask HN: How did you acquire your first 100 users?](https://news.ycombinator.com/item?id=14191161) | 你的第一百位用户是怎样找来的，早期获客走过哪些具体路径？ | 486 | 183 | 2017-04-25 |
| 5 | [Ask HN: Which companies have the best blogs written by their engineering team?](https://news.ycombinator.com/item?id=14163905) | 哪些公司的工程团队博客质量最好，值得持续阅读和学习？ | 451 | 135 | 2017-04-21 |
| 6 | [Ask HN: Do you still use browser bookmarks?](https://news.ycombinator.com/item?id=14064096) | 你还用浏览器书签吗，如何整理，又在哪些场景觉得它有用？ | 441 | 445 | 2017-04-07 |
| 7 | [Ask HN: What are you working on?](https://news.ycombinator.com/item?id=14030149) | 项目不必已经完工，邀请大家介绍最近正在做的事情。 | 374 | 730 | 2017-04-04 |
| 8 | [Ask HN: Mailing lists that HN readers ought to know about?](https://news.ycombinator.com/item?id=14086259) | 有哪些值得 HN 读者知道的邮件列表，能持续送来高质量信息？ | 320 | 133 | 2017-04-11 |
| 9 | [Russian FOSS activist arrested in Russia for his Tor exit-node](https://news.ycombinator.com/item?id=14096625) | 作者报告俄罗斯自由软件活动者因运营 Tor 出口节点遭逮捕。 | 305 | 111 | 2017-04-12 |
| 10 | [Ask HN: How do you keep improving?](https://news.ycombinator.com/item?id=14218408) | 开发八年又兼顾硕士学习后，怎样避免停滞并持续提升能力？ | 301 | 90 | 2017-04-28 |

### 2017-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: How do I switch from being a passive consumer to an active producer?](https://news.ycombinator.com/item?id=14386394) | 刷社交平台、看视频远多于创造，怎样从被动消费者转为主动产出者？ | 699 | 270 | 2017-05-21 |
| 2 | [Ask HN: What are some examples of successful single-person businesses?](https://news.ycombinator.com/item?id=14437921) | 有哪些成功的一人企业，靠软件、广告或其他方式独立经营起来？ | 685 | 308 | 2017-05-29 |
| 3 | [Ask HN: Who is hiring? (May 2017)](https://news.ycombinator.com/item?id=14238005) | 五月招聘信息帖，请在开头注明工作地点与远程等候选人条件。 | 589 | 1078 | 2017-05-01 |
| 4 | [Ask HN: I don't want to be a founder anymore](https://news.ycombinator.com/item?id=14417758) | 创办公司多年后不想再当创始人，作者匿名谈自己难以启齿的感受。 | 565 | 479 | 2017-05-25 |
| 5 | [Ask HN: Google Doc email virus?](https://news.ycombinator.com/item?id=14258918) | 多家公司收到冒名 Google 文档共享邀请，读者询问是否是邮件病毒。 | 481 | 209 | 2017-05-03 |
| 6 | [Ask HN: How can I do social good through programming?](https://news.ycombinator.com/item?id=14375014) | 想用编程为社会做些好事，哪些问题最值得投入技术能力？ | 461 | 376 | 2017-05-19 |
| 7 | [Keybase is out for iPhone, Android](https://news.ycombinator.com/item?id=14318754) | Keybase 发布 iPhone 和 Android 版本，作者给出移动端下载入口。 | 388 | 111 | 2017-05-11 |
| 8 | [Ask HN: Should I create a clone of a popular SaaS with rock-bottom pricing?](https://news.ycombinator.com/item?id=14279870) | 复制热门 SaaS 并用极低价竞争，适不适合作为自己的第一项业务？ | 383 | 220 | 2017-05-06 |
| 9 | [Ask HN: What's your working day like?](https://news.ycombinator.com/item?id=14290518) | 不同职位的人，一天究竟怎样度过，作者征集具体的工作日细节。 | 377 | 415 | 2017-05-08 |
| 10 | [Ask HN: For those programming 10+ years, what do you wish you knew 4 years in?](https://news.ycombinator.com/item?id=14366070) | 编程超过十年的老手，希望自己在第四年时就明白哪些经验？ | 360 | 513 | 2017-05-18 |

### 2017-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What language-agnostic programming books should I read?](https://news.ycombinator.com/item?id=14486657) | HN 用户征集不局限于某种语言的编程书籍推荐。 | 927 | 337 | 2017-06-05 |
| 2 | [Ask HN: Books you wish you had read earlier?](https://news.ycombinator.com/item?id=14477851) | 无论主题，有哪些书让你希望自己更年轻时就已经读过？ | 631 | 270 | 2017-06-03 |
| 3 | [Ask HN: What are we doing about Facebook, Google, and the closed internet?](https://news.ycombinator.com/item?id=14516538) | 反复批评封闭平台之外，我们能采取什么行动改善互联网生态？ | 609 | 424 | 2017-06-08 |
| 4 | [Ask HN: Who is hiring? (June 2017)](https://news.ycombinator.com/item?id=14460777) | 六月招聘集中帖，邀请雇主明确地点、远程与签证等条件。 | 461 | 986 | 2017-06-01 |
| 5 | [Ask HN: Women in tech, how do you find non-toxic work environments?](https://news.ycombinator.com/item?id=14490333) | 准备换城市工作的女性开发者，询问如何找到友善且不带毒的职场。 | 459 | 474 | 2017-06-05 |
| 6 | [Ask HN: What do you want to see in Debian 10 (“buster”)?](https://news.ycombinator.com/item?id=14579080) | Debian 项目负责人邀请社区反馈：Debian 10 最希望增加什么？ | 352 | 317 | 2017-06-18 |
| 7 | [Ask HN: A good primer on cryptocurrencies?](https://news.ycombinator.com/item?id=14659775) | 想弄清加密货币，有哪些清楚可靠的入门资料可以先读？ | 328 | 72 | 2017-06-29 |
| 8 | [Ask HN: People who completed a bootcamp 3+ years ago: what are you doing now?](https://news.ycombinator.com/item?id=14518093) | 完成编程训练营三年以上的人，如今的工作和发展情况怎样？ | 314 | 332 | 2017-06-08 |
| 9 | [Ask HN: What code samples should programmers read?](https://news.ycombinator.com/item?id=14486099) | 哪些代码片段展现深刻洞察，值得每位程序员认真阅读和分析？ | 310 | 148 | 2017-06-05 |
| 10 | [Ask HN: How much ad revenue you make from your side project?](https://news.ycombinator.com/item?id=14576677) | 想把业余数据分析应用靠广告变现，作者询问同行能赚多少广告收入。 | 308 | 174 | 2017-06-17 |

### 2017-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who is hiring? (July 2017)](https://news.ycombinator.com/item?id=14688684) | 七月招聘交流，请列出工作地点及远程、实习、签证支持情况。 | 635 | 969 | 2017-07-03 |
| 2 | [Ask HN: What habits make a programmer great?](https://news.ycombinator.com/item?id=14708350) | 优秀习惯能成就优秀程序员，哪些习惯最值得刻意培养？ | 518 | 183 | 2017-07-06 |
| 3 | [Ask HN: What's a side project you built to make money that hasn't?](https://news.ycombinator.com/item?id=14718089) | 不只看成功者：哪些为赚钱而做的业余项目，最终并没有赚到钱？ | 503 | 452 | 2017-07-07 |
| 4 | [Turkish GSM networks currently play a message of the President on any phone call](https://news.ycombinator.com/item?id=14779286) | 作者称土耳其手机通话前播放总统讲话，质疑通信网络被用于宣传。 | 425 | 173 | 2017-07-15 |
| 5 | [Ask HN: What programming blogs do you follow?](https://news.ycombinator.com/item?id=14842276) | 发现 Julia Evans 的博客后，作者想寻找更多拓展技术视野的编程博客。 | 407 | 77 | 2017-07-24 |
| 6 | [Ask HN: What tasks do you automate?](https://news.ycombinator.com/item?id=14782332) | 你把哪些日常任务交给自动化，减少了什么重复劳动？ | 389 | 337 | 2017-07-16 |
| 7 | [Ask HN: How do you find clients when you have no network and can only do remote?](https://news.ycombinator.com/item?id=14842684) | 没有人脉、不能搬家且只能远程，急需收入的人怎样找到客户？ | 383 | 125 | 2017-07-24 |
| 8 | [Ask HN: Have you regretted making something open-source?](https://news.ycombinator.com/item?id=14885863) | 把作品开源以后，你有没有后悔过，原因是什么？ | 352 | 214 | 2017-07-30 |
| 9 | [Ask HN: Why is Bluetooth so unreliable?](https://news.ycombinator.com/item?id=14752719) | 蓝牙为何经常连接或工作不稳定，可靠性问题究竟出在哪里？ | 351 | 261 | 2017-07-12 |
| 10 | [Ask HN: What books had the greatest effect on how you structure your code?](https://news.ycombinator.com/item?id=14841939) | 哪些书最深地影响了你组织代码和项目结构的方式？ | 332 | 158 | 2017-07-24 |

### 2017-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Launch HN: 70MillionJobs (YC S17) – Job board for people with criminal records](https://news.ycombinator.com/item?id=14911467) | 70MillionJobs 推出面向有犯罪记录者的求职平台。 | 1879 | 506 | 2017-08-02 |
| 2 | [Ask HN: What is your favorite CS paper?](https://news.ycombinator.com/item?id=15089476) | HN 用户分享自己最喜欢的计算机科学论文。 | 793 | 257 | 2017-08-24 |
| 3 | [Ask HN: What maths are critical to pursuing ML/AI?](https://news.ycombinator.com/item?id=15116379) | 进入机器学习和人工智能需要哪些数学基础，哪些教材课程最关键？ | 628 | 135 | 2017-08-28 |
| 4 | [Ask HN: Is Georgia Tech's Online Master in CS Worth It?](https://news.ycombinator.com/item?id=15018002) | 佐治亚理工在线计算机硕士值不值得读，投入和回报怎样衡量？ | 489 | 210 | 2017-08-15 |
| 5 | [Ask HN: Projects that don't make you money but you're doing it out of sheer joy?](https://news.ycombinator.com/item?id=14978631) | 哪些项目不给你带来收入，你却因为纯粹快乐而一直在做？ | 488 | 569 | 2017-08-10 |
| 6 | [Ask HN: What mistakes in your experience does management keep making?](https://news.ycombinator.com/item?id=15033156) | 管理者总在反复犯哪些错误，明明有教训却似乎从不吸取？ | 451 | 379 | 2017-08-17 |
| 7 | [Ask HN: Who is hiring? (August 2017)](https://news.ycombinator.com/item?id=14901313) | 八月职位汇总，请说明地点与远程、实习、签证等安排。 | 439 | 941 | 2017-08-01 |
| 8 | [Launch HN: Lambda School (YC S17) – CS education that's free until you get a job](https://news.ycombinator.com/item?id=15011033) | Lambda School 推出先学习、找到工作后再付费的软件工程师培训。 | 436 | 266 | 2017-08-14 |
| 9 | [Ask HN: What free resources did you use to learn how to program ML/AI?](https://news.ycombinator.com/item?id=14998352) | 你曾用哪些免费资源学会机器学习或人工智能编程？ | 415 | 51 | 2017-08-12 |
| 10 | [Ask HN: Which companies give programmers offices?](https://news.ycombinator.com/item?id=14979718) | 哪些公司会给程序员独立办公室，是否真有不同于开放工位的选择？ | 312 | 241 | 2017-08-10 |

### 2017-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What books have made the biggest impact on your mental models?](https://news.ycombinator.com/item?id=15155833) | 哪些书对你的思维模型影响最大，让你换一种方式理解世界？ | 692 | 247 | 2017-09-02 |
| 2 | [Ask HN: Who is hiring? (September 2017)](https://news.ycombinator.com/item?id=15148885) | 九月招聘集中发布，要求职位地点及远程等候选人条件清楚可见。 | 573 | 965 | 2017-09-01 |
| 3 | [Ask HN: How to start afresh in a new domain after years of expertise in another?](https://news.ycombinator.com/item?id=15182501) | 在一个领域积累十二年后转入新领域，怎样放下旧身份并重新学习？ | 389 | 88 | 2017-09-06 |
| 4 | [Reddit's Ad Changes Reduce Your ROI](https://news.ycombinator.com/item?id=15233127) | 长期 Reddit 广告主认为平台变更降低投放回报，分享自己的观察。 | 376 | 87 | 2017-09-12 |
| 5 | [Ask HN: Companies who adopted React Native over a year ago, do you regret it?](https://news.ycombinator.com/item?id=15293573) | 采用 React Native 一年以上的团队，现在是否后悔当初的选择？ | 363 | 145 | 2017-09-20 |
| 6 | [Ask HN: Sell my startup for $14M because I can't raise $2M?](https://news.ycombinator.com/item?id=15314663) | 融资两百万美元遇阻，却有一千四百万收购报价，创始人该卖公司吗？ | 354 | 330 | 2017-09-22 |
| 7 | [Ask HN: What are your favourite developer blogs?](https://news.ycombinator.com/item?id=15154903) | 寻找优秀开发者博客，作者希望从同行的写作与工作中获取灵感。 | 302 | 66 | 2017-09-02 |
| 8 | [Ask HN: Those making $500+/month on side projects in 2017 – Show and tell](https://news.ycombinator.com/item?id=15148804) | 2017 年业余项目月入五百美元以上的人，邀请展示业务并谈谈进展。 | 292 | 239 | 2017-09-01 |
| 9 | [Ask HN: Resources for building a programming language?](https://news.ycombinator.com/item?id=15171238) | 想亲手创造一门编程语言，哪些资源能提供思路和具体实现指导？ | 239 | 83 | 2017-09-04 |
| 10 | [Tell HN: We'll pay for you to sue Equifax](https://news.ycombinator.com/item?id=15249825) | Legalist 表示愿提供材料、费用与说明，支持用户在小额法庭起诉 Equifax。 | 216 | 94 | 2017-09-14 |

### 2017-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who is hiring? (October 2017)](https://news.ycombinator.com/item?id=15384262) | 十月职位交流帖，请招聘方注明地点以及远程、实习、签证支持。 | 678 | 1122 | 2017-10-02 |
| 2 | [Ask HN: What non-work task have you automated?](https://news.ycombinator.com/item?id=15451442) | 工作之外，你已经自动化了哪些生活任务，让自己少操心？ | 586 | 704 | 2017-10-11 |
| 3 | [Ask HN: Resources to learn blockchain and smart contracts?](https://news.ycombinator.com/item?id=15398550) | 学习区块链和智能合约，有哪些能讲清相关概念的书、论文或教程？ | 526 | 116 | 2017-10-04 |
| 4 | [Ask HN: My house might burn down in the next 24 hours. Suggestions?](https://news.ycombinator.com/item?id=15446364) | 房子可能在一天内遭野火烧毁，作者求助疏散、资料保存与保险准备。 | 498 | 333 | 2017-10-11 |
| 5 | [Ask HN: We have a great team and capital but can't find a good idea](https://news.ycombinator.com/item?id=15588361) | 已有团队和资金，却一年都找不到好点子，创业者求助如何破局。 | 337 | 550 | 2017-10-30 |
| 6 | [Google is shutting down the QPX Express API for airfare data](https://news.ycombinator.com/item?id=15594975) | 谷歌将关闭机票价格数据 QPX Express API，作者转发收到的停服通知。 | 324 | 190 | 2017-10-31 |
| 7 | [Ask HN: How and where can I publish my research on AI as a college dropout?](https://news.ycombinator.com/item?id=15435371) | 没有完成大学学业的人，怎样、又能去哪里发表自己的 AI 研究？ | 270 | 81 | 2017-10-09 |
| 8 | [Ask HN: Where do I get started on ASICs, FPGA, RTL, Verilog et. al?](https://news.ycombinator.com/item?id=15379418) | 想理解芯片从设计到制造，ASIC、FPGA、RTL 与 Verilog 该如何入门？ | 267 | 109 | 2017-10-01 |
| 9 | [Ask HN: What essay/blogpost do you keep going back to reread?](https://news.ycombinator.com/item?id=15406826) | 哪篇随笔或博客让你隔一段时间就回去重读，总能获得新的收获？ | 226 | 103 | 2017-10-05 |
| 10 | [Ask HN: Developers who became engineering managers, how was the experience?](https://news.ycombinator.com/item?id=15463612) | 从开发者转任工程经理，新的挑战是什么，哪些旧技能依然管用？ | 211 | 72 | 2017-10-13 |

### 2017-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Best way to get started with AI?](https://news.ycombinator.com/item?id=15689399) | 已有中等编程能力，想从线性回归等简单内容开始探索 AI，怎么起步？ | 709 | 91 | 2017-11-13 |
| 2 | [Ask HN: Who is hiring? (November 2017)](https://news.ycombinator.com/item?id=15601729) | 十一月招聘机会汇总，邀请标明工作地点及远程等申请条件。 | 624 | 1180 | 2017-11-01 |
| 3 | [Ask HN: Where can I find high-end stock images for a website?](https://news.ycombinator.com/item?id=15602538) | 想让网站配图更出色，哪里能找到质量高的图片素材？ | 600 | 77 | 2017-11-01 |
| 4 | [Ask HN: What are some interesting papers in CS for a beginner?](https://news.ycombinator.com/item?id=15695326) | 计算机本科新手读论文，有哪些有趣、门槛适中的作品值得先读？ | 534 | 91 | 2017-11-14 |
| 5 | [Ask HN: CS papers for software architecture and design?](https://news.ycombinator.com/item?id=15775548) | 软件架构与设计领域，哪些论文曾深刻影响你的实际工作？ | 525 | 99 | 2017-11-25 |
| 6 | [Ask HN: What are best tools for web scraping?](https://news.ycombinator.com/item?id=15694118) | 需要抓取网页数据时，哪些工具最好用、最值得推荐？ | 502 | 228 | 2017-11-14 |
| 7 | [Ask HN: What tech were you convinced would take the world by storm but didn't?](https://news.ycombinator.com/item?id=15718653) | 哪项技术你曾确信会席卷世界，最后却没有真正流行起来？ | 408 | 983 | 2017-11-17 |
| 8 | [Ask HN: What is your favorite place to find work?](https://news.ycombinator.com/item?id=15646550) | 找工作时最喜欢哪个网站或招聘板，哪些渠道体验最好？ | 334 | 92 | 2017-11-07 |
| 9 | [Ask HN: I'm lonely. Are there any video chat support groups for solo founders?](https://news.ycombinator.com/item?id=15732087) | 独立创始人感到孤独，有没有能通过视频互相支持的同伴小组？ | 293 | 180 | 2017-11-19 |
| 10 | [Ask HN: How can we stop the plan to end net neutrality?](https://news.ycombinator.com/item?id=15745057) | 美国 FCC 即将提出结束网络中立性的计划，普通人还能如何阻止？ | 248 | 194 | 2017-11-21 |

### 2017-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [AMA: NY AG Schneiderman on net neutrality and protecting our voice in government](https://news.ycombinator.com/item?id=15853374) | 纽约州总检察长参加问答，介绍对 FCC 网络中立性征询中虚假评论的调查。 | 1126 | 269 | 2017-12-05 |
| 2 | [Excel team considering Python as scripting language: asking for feedback](https://news.ycombinator.com/item?id=15927132) | Excel 团队考虑加入 Python 脚本支持，作者邀请感兴趣的人提交反馈。 | 594 | 268 | 2017-12-14 |
| 3 | [Ask HN: Who is hiring? (December 2017)](https://news.ycombinator.com/item?id=15824597) | 十二月招聘集中帖，请注明地点与远程、实习、签证等工作条件。 | 592 | 982 | 2017-12-01 |
| 4 | [Ask HN: What was the best CS paper you read in 2017?](https://news.ycombinator.com/item?id=16035402) | 2017 年读过最好的计算机科学论文是哪篇，为什么值得一读？ | 558 | 129 | 2017-12-30 |
| 5 | [Ask HN: Huge enterprise customer wants to see our source code](https://news.ycombinator.com/item?id=15862494) | 五人企业软件团队遇到大客户要求查看源码，怎样回应和保护自己？ | 513 | 277 | 2017-12-06 |
| 6 | [Did Bitcoin just prove it can't scale?](https://news.ycombinator.com/item?id=15884698) | 比特币交易拥堵与费用问题显现，作者质疑它是否已经暴露扩展极限。 | 361 | 477 | 2017-12-09 |
| 7 | [Ask HN: Any recommended books on developing mental models?](https://news.ycombinator.com/item?id=16009028) | 想建立更好的思维模型，有哪些书值得系统阅读？ | 350 | 61 | 2017-12-26 |
| 8 | [Ask HN: What did you work on in 2017?](https://news.ycombinator.com/item?id=16041245) | 回顾 2017 年，你把时间投入了哪些项目与工作？ | 350 | 562 | 2017-12-31 |
| 9 | [Ask HN: What software/service helps you be an effective remote developer?](https://news.ycombinator.com/item?id=15889939) | 远程开发时，哪些软件或服务真正帮助你保持高效协作？ | 284 | 150 | 2017-12-10 |
| 10 | [Ask HN: Writing cover letters for tech jobs](https://news.ycombinator.com/item?id=15934135) | 技术职位求职信到底写什么，怎样避免花时间写没人看的内容？ | 265 | 123 | 2017-12-15 |

### 2018-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Today is the fifth anniversary of Aaron Swartz's death](https://news.ycombinator.com/item?id=16122999) | Aaron Swartz 去世五周年，作者用一声感谢纪念他的贡献。 | 709 | 82 | 2018-01-11 |
| 2 | [Ask HN: Who is hiring? (January 2018)](https://news.ycombinator.com/item?id=16052538) | 2018 年一月招聘信息汇总，请列明位置及远程等候选人条件。 | 513 | 893 | 2018-01-02 |
| 3 | [Ask HN: 5 months and counting waiting for Coinbase customer support. Advice?](https://news.ycombinator.com/item?id=16261136) | 等 Coinbase 客服处理已超过五个月，用户求助还有什么可用办法。 | 475 | 182 | 2018-01-29 |
| 4 | [Ask HN: What’s your favorite talk from 2017?](https://news.ycombinator.com/item?id=16045859) | 2017 年你听过最喜欢的演讲是哪场，愿意推荐哪一段分享？ | 418 | 106 | 2018-01-01 |
| 5 | [Ask HN: What's the recommended method of adding authentication to a REST API?](https://news.ycombinator.com/item?id=16157002) | 给 REST API 加入身份验证，当前推荐采用什么方法和机制？ | 397 | 249 | 2018-01-16 |
| 6 | [Ask HN: Best introductory video courses on ML and Deep Learning?](https://news.ycombinator.com/item?id=16138353) | 想轻松入门机器学习与深度学习，有哪些讲解清楚的视频课？ | 323 | 40 | 2018-01-13 |
| 7 | [Ask HN: How to Seriously Start with Machine Learning and AI](https://news.ycombinator.com/item?id=16167620) | 不想只旁观 AI 新闻，作者希望真正开始学习和实践机器学习。 | 264 | 71 | 2018-01-17 |
| 8 | [Ask HN: My company plans an ICO despite my opposition as CTO, any advice?](https://news.ycombinator.com/item?id=16125139) | CTO 反对发行代币，公司仍决定 ICO，作者匿名询问如何处理分歧。 | 224 | 134 | 2018-01-11 |
| 9 | [Ask HN: Is big-endian dead?](https://news.ycombinator.com/item?id=16187939) | 大端序是否已退出主流，除了嵌入式与专用市场还在哪些芯片上使用？ | 202 | 187 | 2018-01-19 |
| 10 | [Ask HN: What influenced your personal growth the most?](https://news.ycombinator.com/item?id=16149006) | 回看个人成长，什么经历、方法或观念对你的影响最大？ | 198 | 167 | 2018-01-15 |

### 2018-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What has HN given you?](https://news.ycombinator.com/item?id=16409768) | HN 用户分享社区带给自己的机会、见解与收获。 | 1095 | 570 | 2018-02-19 |
| 2 | [Ask HN: Is it 'normal' to struggle so hard with work?](https://news.ycombinator.com/item?id=16411662) | 工作为何如此费力，三十岁的作者想知道自己的挣扎是否常见。 | 802 | 369 | 2018-02-19 |
| 3 | [Ask HN: Successful one-person online businesses?](https://news.ycombinator.com/item?id=16482392) | 再征集成功的一人网络生意，邀请讲清业务内容与最初如何起步。 | 594 | 267 | 2018-02-28 |
| 4 | [Ask HN: I'm writing a book about white-collar drug use, including tech sector](https://news.ycombinator.com/item?id=16465762) | 一位记者正在写白领药物使用的书，希望了解包括科技行业在内的经历。 | 542 | 615 | 2018-02-26 |
| 5 | [Ask HN: Who is hiring? (February 2018)](https://news.ycombinator.com/item?id=16282819) | 二月职位交流帖，招聘方请说明地点及远程、实习和签证条件。 | 454 | 1050 | 2018-02-01 |
| 6 | [Launch HN: Pagedraw (YC W18) – Compile UI Mockups to React Code](https://news.ycombinator.com/item?id=16467387) | Pagedraw 把界面原型编译成 React 代码，邀请试用可视化 UI 构建器。 | 344 | 122 | 2018-02-26 |
| 7 | [Ask HN: As a data scientist, what should be in my toolkit in 2018?](https://news.ycombinator.com/item?id=16418546) | 作为数据科学家，2018 年的工具箱应该包含哪些工具与技能？ | 341 | 169 | 2018-02-20 |
| 8 | [Launch HN: SheerlyGenius (YC W18) – Indestructible Tights from Bulletproof Fiber](https://news.ycombinator.com/item?id=16377751) | SheerlyGenius 发布以防弹纤维制作的丝袜，主打更强的耐用性。 | 321 | 168 | 2018-02-14 |
| 9 | [Ask HN: What's the best algorithms and data structures online course?](https://news.ycombinator.com/item?id=16428309) | 学习算法与数据结构，哪些在线课程最值得投入时间？ | 273 | 36 | 2018-02-21 |
| 10 | [Ask HN: Have you successfully done a career do-over, and how did you do it?](https://news.ycombinator.com/item?id=16370611) | 不是换专业，而是在同一职业里重新起步，你是否成功做过一次？ | 243 | 167 | 2018-02-13 |

### 2018-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Slack decides to close down IRC and XMPP gateways](https://news.ycombinator.com/item?id=16539857) | Slack 决定关闭 IRC 与 XMPP 网关，称其已难以满足功能与安全需求。 | 1148 | 600 | 2018-03-07 |
| 2 | [Launch HN: Promise (YC W18) – Cost-effective, more humane alternative to jail](https://news.ycombinator.com/item?id=16630971) | Promise 推出监禁替代方案，希望以更低成本、更人道的方式处理相关需求。 | 912 | 410 | 2018-03-20 |
| 3 | [Tell HN: I just wanted to say: thank you, Hacker News](https://news.ycombinator.com/item?id=16640599) | 几年前求助三十岁后重启计算机职业，如今作者回到 HN 说声感谢。 | 799 | 131 | 2018-03-21 |
| 4 | [Ask HN: Best way to learn modern C++?](https://news.ycombinator.com/item?id=16535886) | 有一些 C 基础却觉得 C++ 复杂，怎样循序渐进地学好现代 C++？ | 686 | 173 | 2018-03-07 |
| 5 | [Ask HN: How to self-learn math?](https://news.ycombinator.com/item?id=16562173) | 重新发现数学的魅力后，作者想找一条从基础向上自学的路径。 | 618 | 208 | 2018-03-11 |
| 6 | [Ask HN: Who is hiring? (March 2018)](https://news.ycombinator.com/item?id=16492994) | 三月招聘信息汇总，请标出职位地点与远程、实习和签证安排。 | 592 | 1174 | 2018-03-01 |
| 7 | [Ask HN: “Write your own” or “Build your own” software projects](https://news.ycombinator.com/item?id=16591918) | 寻找“亲手实现一个”系列教程，用小规模代码弄懂一种技术或功能。 | 576 | 82 | 2018-03-15 |
| 8 | [Ask HN: Examples of great landing pages?](https://news.ycombinator.com/item?id=16710952) | 哪些产品落地页做得出色，值得作为表达与设计的参考？ | 566 | 231 | 2018-03-29 |
| 9 | [Ask HN: How do you find freelance work?](https://news.ycombinator.com/item?id=16651077) | 全职工作之外时间不少，软件工程师怎样找到合适的自由职业项目？ | 518 | 204 | 2018-03-22 |
| 10 | [YouTube and Reddit roll out new restrictions including channel and sub bans](https://news.ycombinator.com/item?id=16643040) | 作者汇集 YouTube 与 Reddit 的新内容限制，关注频道和社区封禁变化。 | 448 | 714 | 2018-03-21 |

### 2018-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: How to self-learn electronics?](https://news.ycombinator.com/item?id=16775744) | HN 用户征集自学电子技术的方法与资源。 | 1681 | 302 | 2018-04-06 |
| 2 | [Ask HN: What are the best MOOCs you've taken?](https://news.ycombinator.com/item?id=16745042) | HN 用户推荐自己上过的优质大规模开放在线课程。 | 1665 | 315 | 2018-04-03 |
| 3 | [Ask HN: What is your favourite tech talk?](https://news.ycombinator.com/item?id=16838460) | 你最喜欢哪场技术演讲，软件工程或其他技术领域都欢迎推荐链接。 | 701 | 147 | 2018-04-14 |
| 4 | [Ask HN: Who is hiring? (April 2018)](https://news.ycombinator.com/item?id=16735011) | 四月职位交流，请雇主明确地点与远程等候选人条件。 | 612 | 1070 | 2018-04-02 |
| 5 | [Ask HN: Are there any reasonable alternatives to MacBook Pro for developer?](https://news.ycombinator.com/item?id=16785507) | 2012 款 MacBook Pro 即将换代，开发者还能选择哪些合适的替代电脑？ | 472 | 495 | 2018-04-08 |
| 6 | [Ask HN: My startup has basically failed. What now?](https://news.ycombinator.com/item?id=16949209) | 活动技术创业做了九个月仍没成功，技术合伙人求助接下来如何安排。 | 463 | 220 | 2018-04-28 |
| 7 | [Ask HN: What are some tech companies that do not use an open floor plan?](https://news.ycombinator.com/item?id=16864925) | 不想在开放式办公室工作，哪些科技公司愿意提供更利于专注的空间？ | 409 | 342 | 2018-04-18 |
| 8 | [Tell HN: 17 years on the same game](https://news.ycombinator.com/item?id=16742689) | 从首次登录 Discworld MUD 算起，作者讲述与同一款游戏相伴十七年。 | 396 | 136 | 2018-04-03 |
| 9 | [Ask HN: Anyone making money through algorithmic trading?](https://news.ycombinator.com/item?id=16922538) | 有没有人用小规模算法交易策略，在股票或加密货币市场实际赚到钱？ | 389 | 245 | 2018-04-25 |
| 10 | [Ask HN: What has been your most rewarding job or project and why?](https://news.ycombinator.com/item?id=16931145) | 你做过最有成就感的工作或项目是什么，它为什么让你满足？ | 383 | 244 | 2018-04-26 |

### 2018-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who is hiring? (May 2018)](https://news.ycombinator.com/item?id=16967543) | 五月招聘集中帖，请注明工作地点与远程、实习和签证支持。 | 587 | 1178 | 2018-05-01 |
| 2 | [Ask HN: Why is nearing completion so demotivating?](https://news.ycombinator.com/item?id=17138794) | 动画软件开发两年、发布在即，作者困惑为何越接近完成越没动力。 | 534 | 165 | 2018-05-23 |
| 3 | [Ask HN: Which books have made you introspect?](https://news.ycombinator.com/item?id=17045790) | 经历人生危机后重新审视世界，作者询问哪些书能促使人认真内省。 | 513 | 374 | 2018-05-11 |
| 4 | [Ask HN: How do you continuously monitor web logs for hack attempts?](https://news.ycombinator.com/item?id=17014818) | 怎样持续监控网站访问日志中的攻击迹象，除了放在 Cloudflare 后面还该做什么？ | 477 | 224 | 2018-05-07 |
| 5 | [Ask HN: How do I learn math/physics in my thirties?](https://news.ycombinator.com/item?id=17075261) | 三十多岁想补上学校之外的数学和物理，应该怎样开始学习？ | 441 | 154 | 2018-05-15 |
| 6 | [Launch HN: Necto (YC W18) – ISP Starter Kit](https://news.ycombinator.com/item?id=17067144) | Necto 提供 ISP 起步工具，帮助本地创业者建立自己的网络服务商。 | 404 | 78 | 2018-05-14 |
| 7 | [Ask HN: How to become a remote contractor?](https://news.ycombinator.com/item?id=17047736) | 伦敦 JavaScript 开发者想边旅行边工作，该怎样成为远程合同工？ | 311 | 160 | 2018-05-11 |
| 8 | [Ask HN: What interesting thought did you read on HN but couldn't find later?](https://news.ycombinator.com/item?id=17166420) | 曾在 HN 读到有趣观点、后来却找不到了，有哪些内容你至今惦记？ | 305 | 226 | 2018-05-27 |
| 9 | [Ask HN: Amazon software engineers, how is the work culture now?](https://news.ycombinator.com/item?id=17062782) | 纽约时报报道之后，亚马逊工程文化有变化吗，薪资能否弥补工作压力？ | 284 | 255 | 2018-05-14 |
| 10 | [Ask HN: What are your favorite terminal programs?](https://news.ycombinator.com/item?id=17011227) | 终端里还有哪些好程序值得发现，作者从音乐、文档和下载工具说起。 | 279 | 199 | 2018-05-07 |

### 2018-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Pros and cons of working at a startup in 2018?](https://news.ycombinator.com/item?id=17286939) | YC 合伙人向社区征集二〇一八年在创业公司工作的优点与缺点。 | 1139 | 939 | 2018-06-11 |
| 2 | [Ask HN: What are the things that you have automated in your personal life?](https://news.ycombinator.com/item?id=17385291) | HN 用户分享自己在个人生活中实现自动化的事情。 | 897 | 731 | 2018-06-24 |
| 3 | [I'm Scott Aaronson, quantum computing/computational complexity researcher. AMA](https://news.ycombinator.com/item?id=17425377) | 量子计算与计算复杂性研究者 Scott Aaronson 在 HN 开放提问。 | 649 | 356 | 2018-06-29 |
| 4 | [Ask HN: What's your favorite way of getting a web app up quickly in 2018?](https://news.ycombinator.com/item?id=17217210) | 2018 年快速上线一个网站，你最喜欢怎样部署，如何减少附带复杂度？ | 542 | 558 | 2018-06-03 |
| 5 | [Ask HN: Are you working on interesting technical problems?](https://news.ycombinator.com/item?id=17235832) | 日常工作太像重复业务，你是否正遇到真正有趣的技术问题？ | 542 | 426 | 2018-06-05 |
| 6 | [Ask HN: Who is hiring? (June 2018)](https://news.ycombinator.com/item?id=17205865) | 六月职位汇总，要求写清所在地与远程等工作条件。 | 450 | 896 | 2018-06-01 |
| 7 | [Ask HN: Old CS lecturer looking for advice from current and recent students](https://news.ycombinator.com/item?id=17431577) | 六十一岁的计算机讲师重返课堂，向近期学生征求教学建议。 | 392 | 181 | 2018-06-30 |
| 8 | [Tell HN: I miss the old internet](https://news.ycombinator.com/item?id=17334552) | 三十岁的作者怀念旧互联网，在社区倾诉对如今网络体验的感受。 | 391 | 221 | 2018-06-17 |
| 9 | [Ask HN: What is the first thing you implement at a new company?](https://news.ycombinator.com/item?id=17353854) | 换到一家新公司后，你最先推动落实什么工具、流程或实践？ | 331 | 276 | 2018-06-20 |
| 10 | [Ask HN: Have you shipped anything serious with a “serverless” architecture?](https://news.ycombinator.com/item?id=17378749) | Serverless 已受到关注，有人用这种架构真正交付过重要业务吗？ | 329 | 201 | 2018-06-23 |

### 2018-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: 2018 Summer Reading List?](https://news.ycombinator.com/item?id=17513576) | 暑期阅读清单传统久未更新，作者征集 2018 年夏天值得读的书。 | 746 | 391 | 2018-07-12 |
| 2 | [Ask HN: What are your favorite statistics and probability textbooks?](https://news.ycombinator.com/item?id=17474646) | 不满足于按计算器按钮的统计课，作者寻找真正讲清统计与概率的教材。 | 452 | 85 | 2018-07-06 |
| 3 | [Ask HN: Who is hiring? (July 2018)](https://news.ycombinator.com/item?id=17442187) | 七月招聘机会集中发布，请注明地点、远程与签证等安排。 | 425 | 842 | 2018-07-02 |
| 4 | [Ask HN: Any good examples of learning through games/puzzles, for adults?](https://news.ycombinator.com/item?id=17616937) | 成年人通过游戏或谜题学习概念，有哪些实际做得好的例子？ | 391 | 137 | 2018-07-26 |
| 5 | [Ask HN: Favorite note-taking software?](https://news.ycombinator.com/item?id=17532094) | 受够 Evernote 的两设备限制，作者寻找更适合自己的笔记软件。 | 374 | 429 | 2018-07-14 |
| 6 | [Ask HN: As a team lead how to handle project going off the rails?](https://news.ycombinator.com/item?id=17511850) | 现代化改造项目不断延期，作为技术带头人该怎样让它重回正轨？ | 325 | 195 | 2018-07-12 |
| 7 | [Ask HN: My Microsoft account has been suspended by Microsoft without details](https://news.ycombinator.com/item?id=17627093) | 微软账号被以违反条款为由停用却不解释细节，用户请求帮助。 | 311 | 225 | 2018-07-27 |
| 8 | [Ask HN: What are the best resources for learning security and pen testing?](https://news.ycombinator.com/item?id=17563857) | 想系统学习安全与渗透测试，哪些书、课程和实践资源最有用？ | 305 | 51 | 2018-07-19 |
| 9 | [Ask HN: Were you happy moving your API from REST to GraphQL?](https://news.ycombinator.com/item?id=17565508) | 把 API 从 REST 迁移到 GraphQL 后，你是否满意这个决定？ | 301 | 175 | 2018-07-19 |
| 10 | [Ask HN: What are the things keep in mind while giving/preparing for a tech talk?](https://news.ycombinator.com/item?id=17564185) | 准备和发表技术演讲时，有哪些经验能让内容与现场表达更好？ | 299 | 166 | 2018-07-19 |

### 2018-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Thank you HN](https://news.ycombinator.com/item?id=17745688) | 曾因抑郁向 HN 求助的用户回来致谢，表示社区的善意帮助自己走出困境。 | 1370 | 137 | 2018-08-12 |
| 2 | [Ask HN: Who is hiring? (August 2018)](https://news.ycombinator.com/item?id=17663077) | 八月职位交流，请公司说明工作地点和候选人适用的条件。 | 448 | 1012 | 2018-08-01 |
| 3 | [Ask HN: What are some niche communities you enjoy?](https://news.ycombinator.com/item?id=17690852) | 有哪些小众社区让你乐于停留，能遇到兴趣相投的人？ | 437 | 342 | 2018-08-05 |
| 4 | [Ask HN: What is the most unethical thing you've done as a programmer?](https://news.ycombinator.com/item?id=17692005) | 作为程序员，你做过最不合道德的事是什么，后来如何看待？ | 432 | 494 | 2018-08-05 |
| 5 | [Ask HN: Codebase at my work is a complete mess, what should I do?](https://news.ycombinator.com/item?id=17819771) | 刚加入公司却发现代码库一团糟，普通开发者该从哪里开始改善？ | 406 | 333 | 2018-08-22 |
| 6 | [Ask HN: What are the most interesting emerging fields in computer science?](https://news.ycombinator.com/item?id=17696271) | 计算机科学里最有趣的新兴方向是什么，学术、产业和自由软件都欢迎。 | 381 | 177 | 2018-08-06 |
| 7 | [Launch HN: The Buttermilk  Company (YC S18) – Homemade Indian Food in 5 Minutes](https://news.ycombinator.com/item?id=17767789) | The Buttermilk Company 主打五分钟做出印度家常菜，介绍食品创业产品。 | 377 | 441 | 2018-08-15 |
| 8 | [Ask HN: What do you struggle with?](https://news.ycombinator.com/item?id=17867109) | 你现在正在与什么困难较劲，愿意把自己的挣扎说出来吗？ | 365 | 533 | 2018-08-29 |
| 9 | [Ask HN: Have you built a house?](https://news.ycombinator.com/item?id=17857129) | 想尽量自主设计并建造房屋，作者询问亲手造房者的实际经验。 | 356 | 220 | 2018-08-28 |
| 10 | [Ask HN: How to get web development career on track from being homeless?](https://news.ycombinator.com/item?id=17684451) | 在波特兰无家可归的网页开发者，求助如何恢复职业与生活秩序。 | 305 | 196 | 2018-08-03 |

### 2018-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Best alternative to Gmail?](https://news.ycombinator.com/item?id=18054574) | 更在意隐私后想离开 Gmail，托管邮箱和自建方案该怎样选择？ | 867 | 568 | 2018-09-24 |
| 2 | [Ask HN: What are the best textbooks in your field of expertise?](https://news.ycombinator.com/item?id=18104814) | 在你熟悉的专业领域，哪些教材最好、最值得向外行推荐？ | 850 | 272 | 2018-09-30 |
| 3 | [Ask HN: Favorite teachers on YouTube?](https://news.ycombinator.com/item?id=17999659) | 喜欢热情的教学风格，作者征集 YouTube 上最值得跟学的老师。 | 770 | 189 | 2018-09-16 |
| 4 | [Ask HN: Why did your startup fail and what did you learn?](https://news.ycombinator.com/item?id=18011332) | 你的创业公司为何失败，那次经历留下了哪些真正有用的教训？ | 675 | 440 | 2018-09-18 |
| 5 | [Ask HN: What things have richly rewarded the time invested in mastering them?](https://news.ycombinator.com/item?id=18098992) | 哪件事值得花大量时间钻研，掌握之后给了你丰厚的回报？ | 613 | 563 | 2018-09-29 |
| 6 | [Ask HN: What made your favorite manager/supervisor/CEO so great?](https://news.ycombinator.com/item?id=18021782) | 你最喜欢的经理、主管或 CEO 做对了什么，让他们如此出色？ | 575 | 242 | 2018-09-19 |
| 7 | [Tell HN: Using Gmail? You will be force logged into Chrome](https://news.ycombinator.com/item?id=17942252) | 作者报告 Chrome 69 中登录 Gmail 会连带登录浏览器，表达对账号绑定的担忧。 | 532 | 323 | 2018-09-08 |
| 8 | [Ask HN: Who is hiring? (September 2018)](https://news.ycombinator.com/item?id=17902901) | 九月招聘集中帖，请注明地点及远程、实习和签证条件。 | 486 | 906 | 2018-09-03 |
| 9 | [Ask HN: What was the best decision you made in your career?](https://news.ycombinator.com/item?id=18071909) | 回顾职业生涯，你做过最好的一个决定是什么？ | 460 | 472 | 2018-09-26 |
| 10 | [Ask HN: What open source project, in your opinion, has the highest code quality?](https://news.ycombinator.com/item?id=18037613) | 在你看来哪个开源项目的代码质量最高，最值得拿来学习？ | 458 | 286 | 2018-09-21 |

### 2018-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Cheap places to live with a good intellectual atmosphere?](https://news.ycombinator.com/item?id=18164189) | 一位湾区工程师征集生活成本较低、同时拥有良好知识氛围的居住地。 | 911 | 1088 | 2018-10-08 |
| 2 | [Ask HN: What's your favorite elegant/beautiful algorithm?](https://news.ycombinator.com/item?id=18236396) | 哪种算法最优雅、最漂亮，让你每次想到都觉得设计巧妙？ | 733 | 491 | 2018-10-17 |
| 3 | [Ask HN: What are some of the best technical talks you've heard?](https://news.ycombinator.com/item?id=18217762) | 你听过最好的技术演讲有哪些，哪些内容至今仍值得推荐？ | 717 | 171 | 2018-10-15 |
| 4 | [Ask HN: YouTube down?](https://news.ycombinator.com/item?id=18234750) | YouTube 是否中断了，读者询问其他人有没有遇到访问异常。 | 575 | 468 | 2018-10-17 |
| 5 | [Ask HN: Who is hiring? (October 2018)](https://news.ycombinator.com/item?id=18113144) | 十月职位汇总，请招聘方列明位置及远程等工作条件。 | 542 | 1087 | 2018-10-01 |
| 6 | [Ask HN: Ex-FAANG developers, where are you now and why?](https://news.ycombinator.com/item?id=18192534) | 离开大型科技公司的开发者，如今去了哪里，为什么选择那条路？ | 537 | 437 | 2018-10-11 |
| 7 | [Ask HN: What is your best advice for a junior software developer?](https://news.ycombinator.com/item?id=18128477) | 如果只能给初级软件开发者一条建议，你最想提醒什么？ | 470 | 453 | 2018-10-03 |
| 8 | [Tell HN: Now Washington Post is asking to turn off Firefox's tracking protection](https://news.ycombinator.com/item?id=18198502) | 《华盛顿邮报》提示关闭 Firefox 跟踪保护，作者对访问门槛表示不满。 | 450 | 299 | 2018-10-12 |
| 9 | [Ask HN: Am I just a wantrepreneur?](https://news.ycombinator.com/item?id=18267468) | 七年都想创业却没有真正做成，作者怀疑自己是否只停留在想象里。 | 428 | 148 | 2018-10-21 |
| 10 | [Ask HN: What do you do in your 1-on-1s with your direct reports?](https://news.ycombinator.com/item?id=18264245) | 工程经理与直属员工的一对一谈话，多频繁、怎样组织、重点谈什么？ | 409 | 153 | 2018-10-20 |

### 2018-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Thank you to dang and sctb](https://news.ycombinator.com/item?id=18512304) | 一位社区成员感谢 dang 与 sctb 在幕后维护 HN 的辛勤工作。 | 950 | 123 | 2018-11-22 |
| 2 | [Ask HN: Best Command-Line Applications?](https://news.ycombinator.com/item?id=18483460) | 更喜欢命令行而非图形界面，有哪些优秀终端应用值得推荐？ | 634 | 385 | 2018-11-19 |
| 3 | [Tell HN: Amazon now owns 3.0.0.0/8](https://news.ycombinator.com/item?id=18407173) | 作者注意到亚马逊获得原属 GE 的 3.0.0.0/8 地址段，讨论地址归属变化。 | 565 | 313 | 2018-11-08 |
| 4 | [Ask HN: Who is hiring? (November 2018)](https://news.ycombinator.com/item?id=18354503) | 十一月招聘信息交流，请明确工作位置与远程、实习、签证支持。 | 539 | 1033 | 2018-11-01 |
| 5 | [Ask HN: What are some hacks of real founders who did things that don't scale?](https://news.ycombinator.com/item?id=18400020) | 征集创始人亲自做“不易规模化的事”来渡过早期难关的真实故事。 | 539 | 265 | 2018-11-07 |
| 6 | [Ask HN: What's the hardest problem you've ever solved?](https://news.ycombinator.com/item?id=18477387) | 你解决过最难的问题是什么，技术、人际或战略难题都可以分享。 | 464 | 422 | 2018-11-17 |
| 7 | [Ask HN: What's the largest amount of bad code you have ever seen work?](https://news.ycombinator.com/item?id=18442637) | 你见过多少糟糕代码堆在一起却依然能运行，最大的规模有多大？ | 428 | 578 | 2018-11-13 |
| 8 | [Ask HN: Anyone else find the new Gmail interface sluggish?](https://news.ycombinator.com/item?id=18379050) | 新版 Gmail 是否让你觉得反应迟钝，现代电脑和网络下也一样吗？ | 422 | 216 | 2018-11-05 |
| 9 | [Ask HN: Is there a better way to document complex software architectures?](https://news.ycombinator.com/item?id=18508284) | 复杂架构文档仍得手动画框连线，有没有更好的记录和维护办法？ | 406 | 235 | 2018-11-22 |
| 10 | [Ask HN: I've been a programmer for 6 years, and I can't solve basic CS problems](https://news.ycombinator.com/item?id=18445609) | 写代码六年却被基础计算机题难住，作者求助如何面对知识缺口。 | 404 | 296 | 2018-11-13 |

### 2018-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What are your “brain hacks” that help you manage everyday situations?](https://news.ycombinator.com/item?id=18588727) | HN 用户分享帮助自己处理日常问题的思维技巧。 | 1322 | 366 | 2018-12-03 |
| 2 | [Ask HN: Favorite nonfiction books of 2018?](https://news.ycombinator.com/item?id=18743465) | 2018 年读过的非虚构书里，你最喜欢并愿意推荐哪几本？ | 842 | 332 | 2018-12-23 |
| 3 | [Ask HN: Best talks of 2018?](https://news.ycombinator.com/item?id=18740939) | 2018 年最喜欢的演讲有哪些，编程、管理和生活主题都欢迎。 | 710 | 194 | 2018-12-22 |
| 4 | [Ask HN: What to do after $8M (all cash, post tax) exit?](https://news.ycombinator.com/item?id=18600220) | 因公司退出获得税后八百万现金，项目经理匿名求助如何规划此后生活。 | 687 | 508 | 2018-12-04 |
| 5 | [Ask HN: Which tool do you use to create beautiful diagrams?](https://news.ycombinator.com/item?id=18788244) | 想制作漂亮清晰的图表和示意图，大家通常使用哪些工具？ | 681 | 212 | 2018-12-30 |
| 6 | [Ask HN: What technologies did you learn in 2018?](https://news.ycombinator.com/item?id=18745763) | 2018 年你学了哪些技术，又有哪些值得在新一年继续投入？ | 629 | 601 | 2018-12-23 |
| 7 | [Ask HN: Books you read in 2018?](https://news.ycombinator.com/item?id=18661546) | 交流 2018 年读过的书，寻找值得推荐和意外带来惊喜的作品。 | 578 | 347 | 2018-12-12 |
| 8 | [Ask HN: What's the best book on modern UI/UX?](https://news.ycombinator.com/item?id=18662992) | 想学习现代网站 UI 与 UX，哪些书和设计工具适合借鉴优秀产品？ | 542 | 150 | 2018-12-12 |
| 9 | [Ask HN: Which abandoned proprietary software would you resurrect?](https://news.ycombinator.com/item?id=18635010) | 曾经喜爱却被遗弃的闭源软件，如果能复活一个你会选谁？ | 478 | 807 | 2018-12-08 |
| 10 | [Ask HN: What do you use for authentication and authorization?](https://news.ycombinator.com/item?id=18767767) | 为新应用构建后端 API，你会如何选择身份验证与权限管理方案？ | 457 | 236 | 2018-12-27 |

### 2019-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: How did you decide what problems to solve in your lifetime?](https://news.ycombinator.com/item?id=18837334) | 面对个人兴趣与社会需要，HN 用户讨论如何选择一生要解决的问题。 | 985 | 439 | 2019-01-06 |
| 2 | [Ask HN: How to self-study mathematics from the undergrad through graduate level?](https://news.ycombinator.com/item?id=18939913) | 有时间从基础深入学习，怎样自学覆盖本科到研究生层次的数学？ | 654 | 227 | 2019-01-18 |
| 3 | [Ask HN: Who is hiring? (January 2019)](https://news.ycombinator.com/item?id=18807017) | 2019 年一月招聘帖，邀请清楚标注职位地点与远程等条件。 | 587 | 951 | 2019-01-02 |
| 4 | [Ask HN: How do you organize everything you want to do?](https://news.ycombinator.com/item?id=18891069) | 想做的事情分布在工作、生活和项目里，怎样组织并安排时间才不混乱？ | 574 | 288 | 2019-01-12 |
| 5 | [Ask HN: What should a systems/low-level software engineer know?](https://news.ycombinator.com/item?id=18881649) | 厌倦网页技术追新、计划转向底层，系统软件工程师该具备哪些知识？ | 551 | 226 | 2019-01-11 |
| 6 | [Ask HN: What is an example of a super simple SaaS that is profitable?](https://news.ycombinator.com/item?id=19016569) | 想靠小型 SaaS 每月赚五百美元，有哪些足够简单且已盈利的实例？ | 548 | 225 | 2019-01-28 |
| 7 | [Ask HN: Go-to web stack today?](https://news.ycombinator.com/item?id=18829557) | 多年没做全栈后重新开发网站，如今大家默认选择什么技术与托管栈？ | 542 | 441 | 2019-01-05 |
| 8 | [Ask HN: Going from Developer to Manager. What should I know or learn?](https://news.ycombinator.com/item?id=18823616) | 准备从开发者转为经理，需要提前知道什么、学习哪些新能力？ | 519 | 182 | 2019-01-04 |
| 9 | [Ask HN: Is it just me, or is CSS too damn hard?](https://news.ycombinator.com/item?id=19021719) | 后端和系统经验丰富却仍觉得 CSS 太难，作者想了解自己是否孤单。 | 499 | 340 | 2019-01-28 |
| 10 | [Ask HN: What are must-know concepts for back end development?](https://news.ycombinator.com/item?id=18961793) | 不想只跟二十分钟速成教程，后端开发有哪些必须理解的基础概念？ | 491 | 130 | 2019-01-21 |

### 2019-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What books changed the way you think about almost everything?](https://news.ycombinator.com/item?id=19087418) | HN 用户分享那些改变自己看待世界方式的书籍。 | 2009 | 1165 | 2019-02-05 |
| 2 | [Public protest against Amazon](https://news.ycombinator.com/item?id=19202450) | 一项针对 Amazon 的公开抗议。 | 920 | 495 | 2019-02-19 |
| 3 | [Ask HN: How to find profitable side project idea?](https://news.ycombinator.com/item?id=19164037) | 离开创业团队回到大学学习后，作者想知道怎样找到有盈利可能的业余点子。 | 473 | 202 | 2019-02-14 |
| 4 | [Ask HN: Who is hiring? (February 2019)](https://news.ycombinator.com/item?id=19055166) | 二月招聘集中帖，要求公司员工本人发布，并注明地点及工作条件。 | 407 | 828 | 2019-02-01 |
| 5 | [Upvote for HN Darkmode?](https://news.ycombinator.com/item?id=19232733) | 夜里读 HN 太刺眼，作者希望网站加入深色模式。 | 344 | 92 | 2019-02-23 |
| 6 | [Ask HN: What VPN service are you currently using?](https://news.ycombinator.com/item?id=19242058) | 想找支持 OpenVPN 和 SOCKS5 的 VPN 服务，大家在用哪家、是否推荐？ | 318 | 331 | 2019-02-25 |
| 7 | [Ask HN: What are some great personal blogs/portfolios?](https://news.ycombinator.com/item?id=19114037) | 准备建立博客与作品集，作者寻找工程师个人网站的优秀实例。 | 308 | 114 | 2019-02-08 |
| 8 | [Ask HN: What company environment has enabled your best work?](https://news.ycombinator.com/item?id=19120208) | 哪种团队、沟通、决策和办公环境，让你完成过最好的工作？ | 293 | 195 | 2019-02-09 |
| 9 | [Tell HN: Wells Fargo completely offline](https://news.ycombinator.com/item?id=19108115) | 作者称 Wells Fargo 多小时完全离线，询问银行为何会出现这种中断。 | 292 | 239 | 2019-02-07 |
| 10 | [Ask HN: How to be productive with big existing code base](https://news.ycombinator.com/item?id=19254008) | 接手积累三年的 Node.js 项目，怎样在大型既有代码库里更快产生价值？ | 284 | 180 | 2019-02-26 |

### 2019-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: How to speak like a leader, not like an engineer?](https://news.ycombinator.com/item?id=19349676) | 被要求“像领导者那样说话”，技术经理怎样拓展工程师之外的管理视角？ | 511 | 211 | 2019-03-10 |
| 2 | [Ask HN: Resources/Steps for Becoming a Consultant?](https://news.ycombinator.com/item?id=19455224) | 已递辞呈却还没有下家，作者向全职顾问请教起步资源与常见陷阱。 | 499 | 114 | 2019-03-21 |
| 3 | [Ask HN: Physicists of HN, what are you working on these days?](https://news.ycombinator.com/item?id=19500151) | 除了常上头条的方向，HN 上的物理学家最近都在研究什么？ | 456 | 316 | 2019-03-27 |
| 4 | [Ask HN: Tools or sites you use to scope out a workplace before taking a job?](https://news.ycombinator.com/item?id=19280341) | 接下工作以前，大家用哪些工具、网站或访谈方法了解真实职场？ | 448 | 167 | 2019-03-01 |
| 5 | [Ask HN: How to learn best practices when you have no one to teach you?](https://news.ycombinator.com/item?id=19423228) | 小团队没人指导、同事也忙于别的项目，怎样学到可靠的开发实践？ | 440 | 197 | 2019-03-18 |
| 6 | [Ask HN: Who is hiring? (March 2019)](https://news.ycombinator.com/item?id=19281834) | 三月招聘交流帖，请公司成员亲自介绍岗位、地点与远程等条件。 | 398 | 864 | 2019-03-01 |
| 7 | [Ask HN: What made you change your mind about a programming language/paradigm?](https://news.ycombinator.com/item?id=19288954) | 哪本书、课程或实践经历，让你改观对某门语言或编程范式的看法？ | 338 | 391 | 2019-03-02 |
| 8 | [Ask HN: Startup failed after years of work – Can I even get a job now?](https://news.ycombinator.com/item?id=19386758) | 辍学创业七年即将关停，没有学历也久未受雇，该怎样重新求职？ | 302 | 187 | 2019-03-14 |
| 9 | [Ask HN: What are your best learning methods/hacks/tips?](https://news.ycombinator.com/item?id=19521129) | 遇到完全陌生、超出舒适区的知识时，你最有效的学习办法是什么？ | 259 | 97 | 2019-03-29 |
| 10 | [Ask HN: Best questions for an engineer to ask a CEO during a job interview?](https://news.ycombinator.com/item?id=19501289) | 工程师面试创业公司时，该问 CEO 哪些问题才能看清公司的方向？ | 241 | 129 | 2019-03-27 |

### 2019-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Docker Hub Hacked – 190k accounts, GitHub tokens revoked, builds disabled](https://news.ycombinator.com/item?id=19763413) | Docker Hub 遭入侵，约十九万账户受到影响，相关 GitHub 令牌被撤销、构建被禁用。 | 1146 | 257 | 2019-04-27 |
| 2 | [Ask HN: What is your money-making side project outside programming?](https://news.ycombinator.com/item?id=19712057) | HN 用户分享编程之外能够赚钱的业余项目。 | 1134 | 717 | 2019-04-21 |
| 3 | [Ask HN: Are you put off building something because it already exists?](https://news.ycombinator.com/item?id=19774997) | 发现想做的产品已经存在后，你会因此放弃动手吗？ | 1046 | 292 | 2019-04-29 |
| 4 | [Ask HN: One-person SaaS apps that are profitable?](https://news.ycombinator.com/item?id=19701783) | 想做一人经营的 SaaS 业余项目，作者征集当前真实盈利的案例。 | 752 | 358 | 2019-04-19 |
| 5 | [Ask HN: What Hacker News comments have you bookmarked?](https://news.ycombinator.com/item?id=19716401) | 哪些 HN 评论让你觉得深刻到值得收藏，日后反复回看？ | 740 | 184 | 2019-04-22 |
| 6 | [Ask HN: How do you stay disciplined in the long run?](https://news.ycombinator.com/item?id=19777976) | 总是研究后兴奋开工、做到一半便放弃，怎样维持长期自律？ | 537 | 171 | 2019-04-29 |
| 7 | [Ask HN: Amazon delisted me – what do I do?](https://news.ycombinator.com/item?id=19551590) | 摄影产品公司被亚马逊下架，创始人对大型平台受阻的处境请求帮助。 | 495 | 97 | 2019-04-02 |
| 8 | [Ask HN: Who is hiring? (April 2019)](https://news.ycombinator.com/item?id=19543940) | 四月职位集中发布，请雇主本人说明工作地点及远程等申请条件。 | 400 | 858 | 2019-04-01 |
| 9 | [Ask HN: How to Teach Coding?](https://news.ycombinator.com/item?id=19741408) | 第一次长期带一位学徒，程序员怎样把知识教好并帮助新人成长？ | 322 | 121 | 2019-04-24 |
| 10 | [Ask HN: What does your ML pipeline look like?](https://news.ycombinator.com/item?id=19712465) | 机器学习实践中，怎样建立可扩展、可部署且可复现的数据与模型流水线？ | 318 | 49 | 2019-04-21 |

### 2019-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Launch HN: Prometheus (YC W19) – Remove CO2 from Air and Turn It into Gasoline](https://news.ycombinator.com/item?id=19842240) | Prometheus 团队介绍将空气中的二氧化碳转成燃料的计划，宣称使用零碳电力可实现净零排放。 | 1250 | 565 | 2019-05-06 |
| 2 | [Ask HN: What overlooked class of tools should a self-taught programmer look into](https://news.ycombinator.com/item?id=19900955) | 自学程序员可能漏掉哪些重要工具类别，值得从只会写脚本继续拓展？ | 927 | 401 | 2019-05-13 |
| 3 | [Ask HN: What was your experience starting a tech consultancy?](https://news.ycombinator.com/item?id=19876825) | 创立技术咨询公司的过程如何，邀请分享经验、警告与真实故事。 | 510 | 257 | 2019-05-10 |
| 4 | [Ask HN: Who is hiring? (May 2019)](https://news.ycombinator.com/item?id=19797594) | 五月招聘汇总，请公司成员发布职位并列明地点和工作条件。 | 488 | 1007 | 2019-05-01 |
| 5 | [Ask HN: Which books teach mental models?](https://news.ycombinator.com/item?id=19895407) | 哪些书真正教会了思维模型，帮助读者改变理解问题的方式？ | 473 | 92 | 2019-05-12 |
| 6 | [Ask HN: How can I work towards building a company while employed?](https://news.ycombinator.com/item?id=20019975) | 雇佣合同把知识产权归给公司，在职期间还能怎样为自己创业做准备？ | 413 | 182 | 2019-05-27 |
| 7 | [Ask HN: A Good Alternative for ReCaptcha?](https://news.ycombinator.com/item?id=20058697) | 传统验证码易绕过又为难人，除了 reCAPTCHA 还有什么好用的替代方案？ | 368 | 199 | 2019-05-31 |
| 8 | [Ask HN: How do I make sure my non-technical parents are safe online?](https://news.ycombinator.com/item?id=20015775) | 不懂技术的父母容易遇到钓鱼和入侵，怎样帮助他们安全上网？ | 324 | 207 | 2019-05-26 |
| 9 | [Tell HN: Archive.is inaccessible via Cloudflare DNS (1.1.1.1)](https://news.ycombinator.com/item?id=19828317) | 作者排查发现用 Cloudflare 1.1.1.1 解析时无法访问 Archive.is。 | 320 | 197 | 2019-05-04 |
| 10 | [Ask HN: Is freelance web development still a viable path in 2019?](https://news.ycombinator.com/item?id=19907732) | 无代码建站和低价竞争普遍，2019 年做自由网页开发还有前景吗？ | 301 | 138 | 2019-05-14 |

### 2019-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What do you do with your Raspberry Pi?](https://news.ycombinator.com/item?id=20264911) | HN 用户分享 Raspberry Pi 的实际用途，从 VPN 到更多个人项目。 | 1741 | 1069 | 2019-06-24 |
| 2 | [Google Cloud Is Down](https://news.ycombinator.com/item?id=20077421) | 用户报告 Google Cloud 故障影响 YouTube、Snapchat 等服务，而状态页仍显示正常。 | 1395 | 593 | 2019-06-02 |
| 3 | [Ask HN: What are the signs that you have a great manager?](https://news.ycombinator.com/item?id=20230133) | 刚入行的工程师想知道，可以从哪些表现判断自己遇到了好经理。 | 585 | 214 | 2019-06-20 |
| 4 | [Ask HN: I need ideas to impress fifth graders with technology](https://news.ycombinator.com/item?id=20069714) | 要给十到十一岁的孩子展示技术，哪些演示能真正激起他们的兴趣？ | 473 | 237 | 2019-06-01 |
| 5 | [Ask HN: Who is hiring? (June 2019)](https://news.ycombinator.com/item?id=20083795) | 六月职位交流，邀请招聘公司员工写清地点、远程与签证等条件。 | 407 | 787 | 2019-06-03 |
| 6 | [Ask HN: Best free compute and other resources for startups?](https://news.ycombinator.com/item?id=20225118) | 没进孵化器的创业者，除了云厂商常见套餐还能获得哪些免费资源？ | 389 | 143 | 2019-06-19 |
| 7 | [Ask HN: Can we create a new internet where search engines are irrelevant?](https://news.ycombinator.com/item?id=20282397) | 能否重新设计互联网，让信息自然易找，不再依赖巨型搜索引擎？ | 374 | 373 | 2019-06-26 |
| 8 | [Tell HN: Social media strike proposed for July 4-5 by Wikipedia co-founder](https://news.ycombinator.com/item?id=20316140) | 维基百科联合创始人提出七月四至五日社交媒体罢用，呼吁数字独立。 | 310 | 141 | 2019-06-30 |
| 9 | [Ask HN: Does anyone still use IRC?](https://news.ycombinator.com/item?id=20118963) | 怀念九十年代的 IRC，发帖者想知道如今还有谁在用、用来做什么。 | 231 | 324 | 2019-06-06 |
| 10 | [Ask HN: Why do new(ish) programming languages eschew OOP features?](https://news.ycombinator.com/item?id=20320752) | Rust、Go 等新语言为何不采用传统面向对象模型，发帖者探讨这一趋势。 | 231 | 227 | 2019-06-30 |

### 2019-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What people skills do you wish you learned earlier in your career?](https://news.ycombinator.com/item?id=20503813) | 从沟通到谈判，哪些人际交往能力值得在职业生涯更早学会？ | 539 | 423 | 2019-07-23 |
| 2 | [Ask HN: Who is hiring? (July 2019)](https://news.ycombinator.com/item?id=20325925) | 2019 年 7 月招聘集中帖，汇集岗位地点及远程、实习与签证信息。 | 485 | 891 | 2019-07-01 |
| 3 | [Ask HN: Has anyone ever been hired from “Who wants to be hired?” threads?](https://news.ycombinator.com/item?id=20330818) | 求职自荐帖真的带来过录用吗，发帖者寻找通过该栏目找到工作的人。 | 474 | 265 | 2019-07-01 |
| 4 | [Ask HN: What are your favorite YouTube channels to learn stuff?](https://news.ycombinator.com/item?id=20385679) | 征集值得学习的 YouTube 频道，兴趣涵盖阳台种植、吉他和游戏。 | 418 | 138 | 2019-07-08 |
| 5 | [Ask HN: What are the “best” codebases that you've encountered?](https://news.ycombinator.com/item?id=20556336) | 优质代码库到底是什么样，发帖者邀请大家推荐亲身接触过的范例。 | 392 | 269 | 2019-07-29 |
| 6 | [Robinhood Stored Passwords in Plaintext](https://news.ycombinator.com/item?id=20519281) | 发帖者转述 Robinhood 通知，称其曾以明文形式存储部分密码。 | 383 | 167 | 2019-07-24 |
| 7 | [Ask HN: Recommend one book I need to read this summer?](https://news.ycombinator.com/item?id=20332455) | 暑假晚上想读一本好书，发帖者请社区给出最值得带上的一本。 | 341 | 296 | 2019-07-02 |
| 8 | [Ask HN: How to deal with constantly getting cut off in work discussions?](https://news.ycombinator.com/item?id=20453248) | 办公室讨论总被同事打断，怎样把话说完并改善沟通习惯？ | 329 | 298 | 2019-07-16 |
| 9 | [Ask HN: How do you deal with professional envy?](https://news.ycombinator.com/item?id=20433301) | 看到年轻同行升职加薪时心生嫉妒，如何处理这种职业比较？ | 314 | 281 | 2019-07-14 |
| 10 | [Ask HN: Are Lucene/Solr/ES Still Used for Search?](https://news.ycombinator.com/item?id=20477949) | 招聘中较少看到相关需求，Lucene、Solr 和 Elasticsearch 还常用吗？ | 275 | 219 | 2019-07-19 |

### 2019-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: How Do You Read?](https://news.ycombinator.com/item?id=20847508) | 读完一本就立刻开始下一本，发帖者好奇大家如何阅读与消化内容。 | 686 | 247 | 2019-08-31 |
| 2 | [Ask HN: How can we destroy AMP?](https://news.ycombinator.com/item?id=20599752) | 发帖者反对 AMP，公开征集削弱或摆脱这一网页方案的办法。 | 486 | 239 | 2019-08-03 |
| 3 | [Ask HN: Your favourite tutorial for total beginners?](https://news.ycombinator.com/item?id=20583581) | 哪些教程适合完全的新手，征集各类技术领域友好的入门材料。 | 480 | 199 | 2019-08-01 |
| 4 | [Tell HN: Danny Cohen Has Died](https://news.ycombinator.com/item?id=20689675) | 帖子通报互联网协议先驱 Danny Cohen 去世，追忆其技术贡献。 | 432 | 36 | 2019-08-13 |
| 5 | [Ask HN: Recommended resources to learn the Linux kernel and OS theory?](https://news.ycombinator.com/item?id=20809666) | 做过少量内核补丁后，发帖者寻找系统学习 Linux 内核与操作系统的资料。 | 408 | 83 | 2019-08-27 |
| 6 | [Ask HN: Best resources to gain math intuition?](https://news.ycombinator.com/item?id=20804582) | 会计算却缺乏直觉，怎样借助好材料真正理解数学概念？ | 389 | 89 | 2019-08-26 |
| 7 | [Ask HN: Who is hiring? (August 2019)](https://news.ycombinator.com/item?id=20584311) | 2019 年 8 月招聘集中帖，雇主在此介绍岗位和候选人要求。 | 370 | 843 | 2019-08-01 |
| 8 | [Ask HN: What book to read to get a footing in CS theory?](https://news.ycombinator.com/item?id=20729252) | 已经能写程序却缺少理论基础，哪些书能帮助建立计算机科学知识框架？ | 306 | 82 | 2019-08-18 |
| 9 | [Tell HN: Skype on web does not support Firefox](https://news.ycombinator.com/item?id=20818750) | 发帖者反映 Skype 网页版拒绝 Firefox，并要求改用 Edge 或 Chrome。 | 280 | 163 | 2019-08-28 |
| 10 | [Ask HN: What's the best setup for ad blocking and tracker blocking?](https://news.ycombinator.com/item?id=20783339) | 广告与追踪拦截经常导致网站失灵，怎样组合工具才能兼顾隐私与可用性？ | 277 | 158 | 2019-08-23 |

### 2019-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Thank you for not redesigning Hacker News](https://news.ycombinator.com/item?id=20854214) | 身处慢速网络地区的用户感谢 HN 保留简洁设计，让页面仍能迅速加载。 | 1831 | 390 | 2019-09-01 |
| 2 | [Ask HN: Are you ok?](https://news.ycombinator.com/item?id=20951444) | 借澳大利亚关怀活动发问：最近过得好吗，是否有需要倾诉的事？ | 857 | 864 | 2019-09-12 |
| 3 | [Ask HN: What things do you wish you discovered earlier?](https://news.ycombinator.com/item?id=20920635) | 哪些工具、书籍或生活方法，让你觉得相见恨晚？ | 332 | 242 | 2019-09-09 |
| 4 | [Ask HN: Who is hiring? (September 2019)](https://news.ycombinator.com/item?id=20867123) | 2019 年 9 月招聘集中帖，可查找各地岗位及远程工作机会。 | 326 | 703 | 2019-09-03 |
| 5 | [Ask HN: What are your favorite books or essays written at least 100 years ago?](https://news.ycombinator.com/item?id=20914127) | 征集至少百年前写成、今天仍值得阅读的书籍与文章。 | 290 | 237 | 2019-09-08 |
| 6 | [Ask HN: Did your AWS bill literally double from last night?](https://news.ycombinator.com/item?id=21037811) | 发帖者发现 AWS 九月用量账单一夜翻倍，询问其他人是否遇到同样情况。 | 268 | 68 | 2019-09-21 |
| 7 | [Ask HN: Good Remote Work Literature?](https://news.ycombinator.com/item?id=20884974) | 远程工作已有数年，发帖者寻找系统讨论这种工作方式的书籍与文章。 | 255 | 50 | 2019-09-05 |
| 8 | [Ask HN: Where can I find remote or quality oriented freelancing work?](https://news.ycombinator.com/item?id=20971098) | 想用业余时间增加收入，去哪里寻找远程或重视质量的自由职业项目？ | 255 | 100 | 2019-09-14 |
| 9 | [Ask HN: What Have You Learned at Google as a Software Engineer?](https://news.ycombinator.com/item?id=20911340) | 在 Google 做工程师学到了什么，征集能提升技术与工作水平的亲历经验。 | 246 | 151 | 2019-09-08 |
| 10 | [Ask HN: Will getting a PhD lead to a more interesting life?](https://news.ycombinator.com/item?id=21113500) | 计算机硕士毕业前的选择：继续读博是否会让人生更有趣？ | 243 | 249 | 2019-09-30 |

### 2019-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Successful one-person online businesses?](https://news.ycombinator.com/item?id=21332072) | HN 用户分享由一人经营、能提供主要收入的成功在线生意。 | 1474 | 657 | 2019-10-23 |
| 2 | [Ask HN: What's a promising area to work on?](https://news.ycombinator.com/item?id=21324768) | HN 用户讨论哪些领域正在兴起，值得投入新的项目。 | 1331 | 918 | 2019-10-22 |
| 3 | [Ask HN: Who Wants to Be Fired?](https://news.ycombinator.com/item?id=21133181) | 工作里哪些事正逼近你的忍耐极限，甚至让你希望被解雇？ | 942 | 831 | 2019-10-02 |
| 4 | [Ask HN: Are there books for mathematics like Feynman's lectures on physics?](https://news.ycombinator.com/item?id=21346272) | 喜欢费曼物理学讲义，数学领域有没有同样深入浅出的经典教材？ | 788 | 171 | 2019-10-24 |
| 5 | [Ask HN: How do you share/organize knowledge at work and life?](https://news.ycombinator.com/item?id=21310030) | 团队知识如何整理、共享并真正转化为学习，也聊个人生活中的做法。 | 781 | 296 | 2019-10-21 |
| 6 | [Ask HN: How was life for a regular dev during the dot com burst?](https://news.ycombinator.com/item?id=21318704) | 互联网泡沫破裂时，普通开发者的就业与生活发生了哪些变化？ | 642 | 400 | 2019-10-21 |
| 7 | [Ask HN: Feasible Alternative to the MacBook Pro?](https://news.ycombinator.com/item?id=21302412) | 习惯了 MacBook Pro 的屏幕与触控板，还有哪些笔记本能作为替代？ | 563 | 601 | 2019-10-20 |
| 8 | [Ask HN: What do you self-host?](https://news.ycombinator.com/item?id=21235957) | 你在家里或自己的服务器上托管哪些服务，又为何选择自己维护？ | 538 | 335 | 2019-10-12 |
| 9 | [Ask HN: What is the most beautiful piece of code you've ever read?](https://news.ycombinator.com/item?id=21373852) | 征集读过的优美代码片段，关注简洁巧妙的实现思路。 | 476 | 380 | 2019-10-28 |
| 10 | [Ask HN: What are the most fundamental books on computer science?](https://news.ycombinator.com/item?id=21311302) | 初入计算机科学领域，哪些著作称得上构建学科根基的必读书？ | 474 | 192 | 2019-10-21 |

### 2019-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What's the most valuable thing you can learn in an hour?](https://news.ycombinator.com/item?id=21581361) | 集中学习一小时，能够学到哪些最有价值的东西？ | 1460 | 1076 | 2019-11-20 |
| 2 | [Tell HN: Google should drop Quora from search results](https://news.ycombinator.com/item?id=21622322) | 发帖者认为 Quora 的登录墙妨碍查答案，主张 Google 移除其搜索结果。 | 1007 | 346 | 2019-11-24 |
| 3 | [Ask HN: Quitting Big Tech, what is it like?](https://news.ycombinator.com/item?id=21645117) | 高薪大厂工作让人厌倦，离开之后的收入、节奏和满足感会怎样？ | 670 | 400 | 2019-11-27 |
| 4 | [Ask HN: How do you make sure your servers are up as a single founder?](https://news.ycombinator.com/item?id=21461617) | 独立创始人在地铁里遇上服务故障，怎样确保无人值守时服务器仍可靠？ | 448 | 223 | 2019-11-06 |
| 5 | [Ask HN: What does your BI stack look like?](https://news.ycombinator.com/item?id=21513566) | 公司如何制作经营报表和数据可视化，征集实际采用的 BI 工具组合。 | 427 | 173 | 2019-11-12 |
| 6 | [Ask HN: What are you thankful for?](https://news.ycombinator.com/item?id=21660118) | 年末一起聊聊值得感谢的人和事，以及生活中珍惜的支持。 | 418 | 294 | 2019-11-28 |
| 7 | [Ask HN: Who is hiring? (November 2019)](https://news.ycombinator.com/item?id=21419536) | 2019 年 11 月招聘集中帖，集中展示企业岗位及工作安排。 | 402 | 732 | 2019-11-01 |
| 8 | [Ask HN: What is your ML stack like?](https://news.ycombinator.com/item?id=21516311) | 机器学习流水线如何接入已有后端，发帖者询问团队的实际技术栈。 | 387 | 131 | 2019-11-12 |
| 9 | [Ask HN: Burning Out](https://news.ycombinator.com/item?id=21661054) | 早期创业公司员工付出多年后陷入倦怠，寻求应对工作压力的建议。 | 278 | 152 | 2019-11-29 |
| 10 | [Ask HN: Do you write tests before the implementation?](https://news.ycombinator.com/item?id=21533376) | 有多少人坚持先写测试，讨论测试驱动开发的实际收益与维护成本。 | 248 | 317 | 2019-11-14 |

### 2019-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Best book / resources on leadership, especially for tech teams?](https://news.ycombinator.com/item?id=21712194) | 技术团队如何带好人，征集真正有帮助的领导力书籍与学习资源。 | 882 | 209 | 2019-12-05 |
| 2 | [Ask HN: Best books you read in the past decade?](https://news.ycombinator.com/item?id=21900498) | 回望过去十年，哪些书对你的个人生活或职业产生了最大影响？ | 873 | 417 | 2019-12-28 |
| 3 | [Ask HN: How Can I Learn Music Theory?](https://news.ycombinator.com/item?id=21822225) | 自学演奏多年后想深入乐理，该从什么课程、书籍和练习开始？ | 673 | 239 | 2019-12-18 |
| 4 | [Ask HN: Best Talks of 2019?](https://news.ycombinator.com/item?id=21858866) | 征集 2019 年值得回看的演讲，延续社区每年的精彩分享推荐。 | 643 | 85 | 2019-12-22 |
| 5 | [Ask HN: What mistakes did you make when starting as a consultant/freelancer?](https://news.ycombinator.com/item?id=21728436) | 刚做顾问或自由职业时踩过什么坑，又如何据此调整生意做法？ | 622 | 268 | 2019-12-07 |
| 6 | [Merry Christmas HN](https://news.ycombinator.com/item?id=21877571) | 社区圣诞祝福帖，向大家送上对 2019 年的感谢和对新年的期望。 | 502 | 171 | 2019-12-25 |
| 7 | [Ask HN: Which is the most successful one-person business you heard of in 2019?](https://news.ycombinator.com/item?id=21908577) | 大公司榜单之外，2019 年有哪些令人印象深刻的成功单人生意？ | 485 | 231 | 2019-12-29 |
| 8 | [Ask HN: How do you create a successful community from zero?](https://news.ycombinator.com/item?id=21812442) | 一个全新的线上社区，怎样吸引首批成员并形成持续活跃的氛围？ | 441 | 94 | 2019-12-17 |
| 9 | [Ask HN: Full-on machine learning for 2020, what are the best resources?](https://news.ycombinator.com/item?id=21924298) | 2020 年想专注机器学习，面对众多分支该如何选择学习资料与方向？ | 423 | 118 | 2019-12-31 |
| 10 | [Ask HN: Books you plan to read in 2020?](https://news.ycombinator.com/item?id=21802452) | 新一年准备读哪些书，征集 2020 年的阅读计划与学习愿望。 | 421 | 320 | 2019-12-16 |

### 2020-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Thank HN: You helped me get a new job](https://news.ycombinator.com/item?id=22050802) | 一位开发者回顾开源作品和 HN 社区如何帮助自己找到新工作。 | 2425 | 193 | 2020-01-15 |
| 2 | [Ask HN: I've been slacking off at Google for 6 years. How can I stop this?](https://news.ycombinator.com/item?id=21961560) | 一位在谷歌长期消极工作的工程师寻求重拾投入的方法。 | 1337 | 970 | 2020-01-05 |
| 3 | [Ask HN: A New Decade. Any Predictions?](https://news.ycombinator.com/item?id=21941278) | 站在 2020 年代的开端，邀请社区预测未来十年的变化。 | 815 | 1096 | 2020-01-02 |
| 4 | [Thank HN: My SaaS paid my rent this month](https://news.ycombinator.com/item?id=22098425) | 作者分享独立 SaaS 首次支付当月房租的进展，并感谢社区带来的启发。 | 800 | 187 | 2020-01-20 |
| 5 | [Ask HN: What has your work taught you that other people don't realize?](https://news.ycombinator.com/item?id=22018946) | 你的职业让你明白了哪些外行往往意识不到的事情？ | 698 | 727 | 2020-01-11 |
| 6 | [Ask HN: What are the best unknown books you have read?](https://news.ycombinator.com/item?id=22092108) | 哪些鲜为人知的好书值得被更多人发现，征集冷门阅读推荐。 | 613 | 388 | 2020-01-19 |
| 7 | [Ask HN: Are books worth it?](https://news.ycombinator.com/item?id=21955258) | 互联网已经提供大量知识，阅读整本书仍值得投入时间吗？ | 553 | 391 | 2020-01-04 |
| 8 | [Ask HN: What were your most impactful podcast episodes from 2019?](https://news.ycombinator.com/item?id=22027315) | 2019 年哪一期播客让你收获最大，甚至改变了想法或行动？ | 444 | 200 | 2020-01-12 |
| 9 | [Ask HN: What interesting problems are you working on?](https://news.ycombinator.com/item?id=22174828) | 日常软件开发之外，你正在解决哪些有趣、值得投入的难题？ | 442 | 689 | 2020-01-28 |
| 10 | [Ask HN: Joining Big Tech in One’s 40s](https://news.ycombinator.com/item?id=21981923) | 43 岁卖掉公司股份后考虑下一站，中年加入大型科技公司是否合适？ | 441 | 184 | 2020-01-07 |

### 2020-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What Skills to Acquire in 2020?](https://news.ycombinator.com/item?id=22235279) | 2020 年值得学习哪些技能，技术能力和非技术能力都在征集之列。 | 930 | 862 | 2020-02-04 |
| 2 | [Ask HN: What are some books where the reader learns by building projects?](https://news.ycombinator.com/item?id=22299180) | 边做项目边学的书有哪些，寻找让读者通过动手构建掌握知识的教材。 | 852 | 178 | 2020-02-11 |
| 3 | [Ask HN: Advice for a new and inexperienced tech lead?](https://news.ycombinator.com/item?id=22255301) | 中级开发者首次承担技术负责人角色，如何组建团队并做好带队工作？ | 766 | 250 | 2020-02-06 |
| 4 | [Ask HN: What are good solo developer blogs that you enjoy reading?](https://news.ycombinator.com/item?id=22273224) | 征集独立开发者博客，尤其想看公开记录项目开发与运营过程的作者。 | 621 | 145 | 2020-02-08 |
| 5 | [Ask HN: What job can a “jack of all trades” look for?](https://news.ycombinator.com/item?id=22326109) | 喜欢广泛学习、厌倦停滞的多面手，应该寻找怎样的工作岗位？ | 496 | 207 | 2020-02-14 |
| 6 | [Ask HN: What's the best resource for learning modern x64 assembly?](https://news.ycombinator.com/item?id=22279051) | 学习现代 x64 汇编该用哪些资料，发帖者希望超越常见的 x86 教程。 | 492 | 109 | 2020-02-08 |
| 7 | [Ask HN: A major USA bank is storing passwords in cleartext – what to do?](https://news.ycombinator.com/item?id=22352840) | 客服能说出用户密码，发帖者怀疑美国某银行明文存储，询问如何处理。 | 442 | 318 | 2020-02-18 |
| 8 | [Ask HN: What are some examples of good database schema designs?](https://news.ycombinator.com/item?id=22324691) | 怎样识别数据库表结构设计的好坏，征集可供学习比较的优秀实例。 | 437 | 175 | 2020-02-14 |
| 9 | [Ask HN: How do you learn complex, dense technical information?](https://news.ycombinator.com/item?id=22325975) | 面对信息密集的技术手册，怎样兼顾理解、查漏与动手练习？ | 420 | 175 | 2020-02-14 |
| 10 | [Ask HN: What automation tools have you used to replace mundane activities?](https://news.ycombinator.com/item?id=22345150) | 你用哪些自动化工具替代重复劳动，发帖者以发布廉价机票为例求经验。 | 408 | 229 | 2020-02-17 |

### 2020-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who is hiring right now?](https://news.ycombinator.com/item?id=22665398) | 疫情期间提前开设招聘帖，汇集仍在招人的公司信息。 | 1083 | 781 | 2020-03-23 |
| 2 | [Ask HN: What projects are you working on now?](https://news.ycombinator.com/item?id=22648431) | 各地开始隔离后，大家正把额外时间投入哪些个人项目？ | 809 | 1237 | 2020-03-21 |
| 3 | [Ask HN: Have you been laid off?](https://news.ycombinator.com/item?id=22618788) | 发帖者遭遇融资枯竭导致的裁员，询问社区还有谁正在经历失业。 | 800 | 645 | 2020-03-18 |
| 4 | [Ask HN: Great fiction books that have had a positive impact on your life?](https://news.ycombinator.com/item?id=22718592) | 哪些小说曾对你的生活产生积极影响，寻找故事带来的启发与力量。 | 679 | 584 | 2020-03-29 |
| 5 | [Launch HN: Fly.io (YC W20) – Deploy app servers close to your users](https://news.ycombinator.com/item?id=22616857) | Fly.io 介绍其部署平台，让 Docker 应用运行在更靠近终端用户的地方。 | 626 | 261 | 2020-03-18 |
| 6 | [Ask HN: Good ways to capture institutional knowledge?](https://news.ycombinator.com/item?id=22454333) | 怎样把员工经验沉淀成组织知识，让交接和新人入职更加顺畅？ | 547 | 213 | 2020-03-01 |
| 7 | [Ask HN: Book recommendations for understanding financial systems?](https://news.ycombinator.com/item?id=22573204) | 股市剧烈波动引发好奇，哪些书能帮助理解货币、银行和金融体系？ | 527 | 204 | 2020-03-14 |
| 8 | [Ask HN: Is UK government insane or genius?](https://news.ycombinator.com/item?id=22577132) | 面对英国早期群体免疫思路，发帖者质疑其防疫策略是否合理。 | 524 | 741 | 2020-03-14 |
| 9 | [Ask HN: Was the Y2K crisis real?](https://news.ycombinator.com/item?id=22556156) | 千年虫最终影响有限，究竟是风险被夸大，还是预防工作发挥了作用？ | 465 | 371 | 2020-03-12 |
| 10 | [Ask HN: How to self-study physics?](https://news.ycombinator.com/item?id=22682837) | 计算机专业研究生想补齐物理基础，如何安排系统的自学路径？ | 451 | 184 | 2020-03-25 |

### 2020-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: I'm a software engineer going blind, how should I prepare?](https://news.ycombinator.com/item?id=22918980) | 一位视力逐渐衰退的软件工程师询问职业准备建议。 | 3270 | 473 | 2020-04-19 |
| 2 | [Ask HN: What are your favorite low-coding apps / tools as a developer?](https://news.ycombinator.com/item?id=22786853) | 征集开发者实际觉得有用的低代码应用和工具。 | 1081 | 280 | 2020-04-05 |
| 3 | [Ask HN: What is your blog and why should I read it?](https://news.ycombinator.com/item?id=22800136) | 邀请读者介绍自己的博客，说说写什么内容、为什么值得关注。 | 910 | 654 | 2020-04-07 |
| 4 | [Ask HN: What are you learning?](https://news.ycombinator.com/item?id=22786287) | 你最近正在学什么，发帖者借个人项目搁置的机会寻找新的学习灵感。 | 865 | 876 | 2020-04-05 |
| 5 | [Tell HN: C Experts Panel – Ask us anything about C](https://news.ycombinator.com/item?id=22865357) | C 标准委员会成员与相关专家开放问答，邀请社区提出 C 语言问题。 | 829 | 962 | 2020-04-14 |
| 6 | [Ask HN: How can I pick a side project and stick with it?](https://news.ycombinator.com/item?id=22792829) | 技术会得不少却难坚持副项目，怎样选定方向并持续做下去？ | 686 | 364 | 2020-04-06 |
| 7 | [Tell HN: Cisco WebEx on OS X uses the same pre-installer tricks as Zoom](https://news.ycombinator.com/item?id=22815583) | 发帖者检查 WebEx 安装器，称其在 macOS 上采用了类似 Zoom 的预安装手法。 | 673 | 180 | 2020-04-08 |
| 8 | [Ask HN: Programs that saved you 100 hours?](https://news.ycombinator.com/item?id=22849208) | 有哪些命令行工具、应用或服务，实实在在为你省下过上百小时？ | 629 | 516 | 2020-04-12 |
| 9 | [Ask HN: How do I overcome mental laziness?](https://news.ycombinator.com/item?id=22919697) | 一碰到难题就放弃并影响职业发展，怎样克服这种思考上的惰性？ | 618 | 262 | 2020-04-19 |
| 10 | [Ask HN: What scientific phenomenon do you wish someone would explain better?](https://news.ycombinator.com/item?id=22989280) | 哪些科学现象让你一直困惑，希望有人给出更清楚易懂的解释？ | 607 | 813 | 2020-04-26 |

### 2020-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Am I the longest-serving programmer – 57 years and counting?](https://news.ycombinator.com/item?id=23366546) | 一位编程五十七年的从业者询问是否还有更资深同行。 | 2634 | 531 | 2020-05-31 |
| 2 | [Tell HN: Interviewed with Triplebyte? Your profile is about to become public](https://news.ycombinator.com/item?id=23279837) | 提醒 Triplebyte 用户，其面试档案将默认公开且需主动退出。 | 1543 | 574 | 2020-05-23 |
| 3 | [Ask HN: What's your quarantine side project?](https://news.ycombinator.com/item?id=23170881) | 隔离期间在做什么副项目，也欢迎分享正在构建或学习的东西。 | 1336 | 2248 | 2020-05-13 |
| 4 | [Ask HN: Name one idea that changed your life](https://news.ycombinator.com/item?id=23092657) | 征集一个真正改变过你生活的观念，看看想法如何影响行动。 | 1084 | 815 | 2020-05-06 |
| 5 | [Tell HN: Triplebyte reverses, emails apology](https://news.ycombinator.com/item?id=23303037) | 发帖者转述 Triplebyte 的道歉邮件，称公司已撤回此前引发争议的决定。 | 1030 | 649 | 2020-05-25 |
| 6 | [Ask HN: What startup/technology is on your 'to watch' list?](https://news.ycombinator.com/item?id=23276456) | 哪些初创公司或技术进入了你的持续关注名单，它们为什么值得留意？ | 1006 | 669 | 2020-05-22 |
| 7 | [Ask HN: Mind bending books to read and never be the same as before?](https://news.ycombinator.com/item?id=23151144) | 寻找能打破思维惯性、带来认知变化的书，也欢迎情节巧妙的作品。 | 961 | 719 | 2020-05-12 |
| 8 | [Ask HN: Dark mode for HN please?](https://news.ycombinator.com/item?id=23197966) | 发帖者希望 HN 原生提供深色模式，减轻夜间浏览时的刺眼感。 | 780 | 445 | 2020-05-15 |
| 9 | [Ask HN: Is your company sticking to on-premise servers? Why?](https://news.ycombinator.com/item?id=23089999) | 云服务之外，你的公司为何仍坚持自建或本地服务器？ | 779 | 755 | 2020-05-06 |
| 10 | [Ask HN: Keybase Alternatives?](https://news.ycombinator.com/item?id=23103386) | Keybase 被 Zoom 收购后，还有哪些注重安全通信与身份验证的替代品？ | 726 | 228 | 2020-05-07 |

### 2020-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Thank HN: My startup was born here and is now 10 years old](https://news.ycombinator.com/item?id=23466470) | VWO 创始人回顾从 Show HN 起步到创业十周年的历程，并感谢社区。 | 937 | 128 | 2020-06-09 |
| 2 | [Ask HN: My wife might lose the ability to speak in 3 weeks – how to prepare?](https://news.ycombinator.com/item?id=23490115) | 妻子手术可能影响说话能力，发帖者询问如何提前准备语音与沟通方案。 | 855 | 217 | 2020-06-11 |
| 3 | [Ask HN: A way to adblock “we're using cookies” popups?](https://news.ycombinator.com/item?id=23521399) | 网页到处弹出 Cookie 同意框，有什么拦截工具能减少反复点击？ | 668 | 339 | 2020-06-14 |
| 4 | [Ask HN: Who is hiring? (June 2020)](https://news.ycombinator.com/item?id=23379196) | 2020 年 6 月招聘集中帖，提供企业岗位与远程、签证等条件。 | 515 | 654 | 2020-06-01 |
| 5 | [Ask HN: How does your company manage its encryption keys?](https://news.ycombinator.com/item?id=23390966) | 加密密钥丢失导致数据损失后，发帖者询问公司应如何管理密钥。 | 488 | 238 | 2020-06-02 |
| 6 | [Ask HN: What are some good resources to learn how electricity works?](https://news.ycombinator.com/item?id=23562181) | 电压、电流等基础概念总弄不明白，寻找真正讲清电学原理的资料。 | 472 | 180 | 2020-06-18 |
| 7 | [Ask HN: Side projects that are making money, but you'd not talk about them?](https://news.ycombinator.com/item?id=23438930) | 有没有正在赚钱、却不太愿意公开谈论的副项目，邀请分享隐秘生意。 | 442 | 461 | 2020-06-06 |
| 8 | [Ask HN: How do I reach making $1-1.5k/mo in 13 months?](https://news.ycombinator.com/item?id=23427689) | 经验不多的发展中国家开发者，如何在十三个月内达到月入千余美元？ | 437 | 329 | 2020-06-05 |
| 9 | [Ask HN: Thoughts on new GitHub layout?](https://news.ycombinator.com/item?id=23617229) | GitHub 改版后使用感受如何，发帖者对新的布局表达不满。 | 413 | 564 | 2020-06-23 |
| 10 | [Ask HN: Which tools have made you a much better programmer?](https://news.ycombinator.com/item?id=23468193) | 哪些工具让你的编程能力明显提升，带来的改变超过了普通的效率优化？ | 385 | 514 | 2020-06-09 |

### 2020-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Is all of FAANG like this?](https://news.ycombinator.com/item?id=23917131) | 如愿加入大厂后仍不快乐，发帖者想知道其他 FAANG 公司是否也一样。 | 738 | 614 | 2020-07-22 |
| 2 | [Ask HN: My GitHub account got suspended without any notice](https://news.ycombinator.com/item?id=23832437) | 开源维护者反映 GitHub 账号毫无预警被封，寻求理解与解决途径。 | 657 | 263 | 2020-07-14 |
| 3 | [Ask HN: What's the worst piece of software you use everyday?](https://news.ycombinator.com/item?id=23803539) | 你每天不得不用的最糟软件是什么，它的问题是否值得重新做一个？ | 537 | 1500 | 2020-07-11 |
| 4 | [Tell HN: Google drops blogspot.in, breaking hundreds of thousands of permalinks](https://news.ycombinator.com/item?id=23767781) | 发帖者称 Google 放弃 blogspot.in，导致大量博客永久链接失效。 | 525 | 229 | 2020-07-08 |
| 5 | [Ask HN: Who is hiring? (July 2020)](https://news.ycombinator.com/item?id=23702122) | 2020 年 7 月招聘集中帖，雇主集中发布岗位和申请条件。 | 422 | 676 | 2020-07-01 |
| 6 | [Tell HN: Airbnb now opts in your name and photo to data sharing](https://news.ycombinator.com/item?id=23725734) | 发帖者转述 Airbnb 邮件，称姓名与头像的数据共享将默认开启。 | 391 | 113 | 2020-07-03 |
| 7 | [Ask HN: What weird or hard problems are you trying to solve?](https://news.ycombinator.com/item?id=23735676) | 大家正在解决哪些古怪或棘手的问题，欢迎分享不寻常的挑战。 | 361 | 812 | 2020-07-04 |
| 8 | [Launch HN: QuestDB (YC S20) – Fast open source time series database](https://news.ycombinator.com/item?id=23975807) | QuestDB 团队介绍其开源时序数据库，希望提供高速的时间序列数据处理。 | 357 | 167 | 2020-07-28 |
| 9 | [Ask HN: Is it just me? why is “news” so addictive?](https://news.ycombinator.com/item?id=23938007) | 短暂离线露营后重新审视习惯：为什么新闻会让人如此上瘾？ | 333 | 215 | 2020-07-24 |
| 10 | [I’m Peter Roberts, immigration attorney who does work for YC and startups. AMA](https://news.ycombinator.com/item?id=23940345) | 为 YC 与创业公司服务的移民律师 Peter Roberts 开放移民问题问答。 | 304 | 449 | 2020-07-24 |

### 2020-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Why is Reddit on mobile so obsessed with making me use their app?](https://news.ycombinator.com/item?id=24208958) | 用户追问 Reddit 为何在手机网页上反复劝其安装应用。 | 1403 | 644 | 2020-08-19 |
| 2 | [Ask HN: Who is hiring? (August 2020)](https://news.ycombinator.com/item?id=24038520) | 2020 年 8 月招聘集中帖，查看公司正在招聘的职位与工作地点。 | 592 | 825 | 2020-08-03 |
| 3 | [G Suite Doesn't Let You Contact Support Until Logged In. Locked Out = Stuck](https://news.ycombinator.com/item?id=24109809) | 发帖者抱怨 G Suite 锁号后无法求助，因为联系支持也必须先登录。 | 465 | 135 | 2020-08-10 |
| 4 | [Ask HN: How does onlyfans.com work around the “no porn” Stripe rule?](https://news.ycombinator.com/item?id=24291790) | Stripe 禁止色情业务的规则下，OnlyFans 如何处理支付，发帖者寻求解答。 | 416 | 285 | 2020-08-27 |
| 5 | [Ask HN: I have $450K cash, what should I do to maximize my return?](https://news.ycombinator.com/item?id=24020899) | 手头有 45 万美元现金，发帖者征求如何配置资金以提高回报的建议。 | 409 | 481 | 2020-08-01 |
| 6 | [Tell HN: Check medium's localstorage if you use adblock](https://news.ycombinator.com/item?id=24310778) | 发帖者称 Medium 会将被拦截的统计请求存入本地存储，提醒读者检查。 | 360 | 139 | 2020-08-28 |
| 7 | [Ask HN: Who wants to be hired? (August 2020)](https://news.ycombinator.com/item?id=24038518) | 2020 年 8 月求职自荐帖，求职者介绍所在地、技能及远程工作意愿。 | 359 | 405 | 2020-08-03 |
| 8 | [Ask and Show HN: Ever coded for love? Willing to share?](https://news.ycombinator.com/item?id=24091577) | 你曾为了爱情写过程序吗，邀请展示寄托情感的小项目。 | 359 | 214 | 2020-08-08 |
| 9 | [Ask HN: Has anyone migrated off containerized infrastructure?](https://news.ycombinator.com/item?id=24141628) | 被容器的各种细节折腾后，发帖者想听从容器基础设施迁出的经验。 | 345 | 358 | 2020-08-13 |
| 10 | [Ask HN: How do you switch off from work, particularly when working from home?](https://news.ycombinator.com/item?id=24196433) | 居家办公让工作侵入休息时间，怎样在下班后真正切换状态？ | 327 | 308 | 2020-08-18 |

### 2020-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Never search for domains on Godaddy.com](https://news.ycombinator.com/item?id=24506303) | 用户称查询的域名随后被注册，提醒谨慎使用 GoDaddy 搜索。 | 1656 | 729 | 2020-09-17 |
| 2 | [Ask HN: How to learn sales?](https://news.ycombinator.com/item?id=24601579) | 首次创业意识到销售的重要性，如何从零学习推销产品和获取客户？ | 865 | 231 | 2020-09-26 |
| 3 | [Ask HN: Who is hiring? (September 2020)](https://news.ycombinator.com/item?id=24342498) | 2020 年 9 月招聘集中帖，汇集各公司的岗位需求与雇佣条件。 | 368 | 696 | 2020-09-01 |
| 4 | [Ask HN: Your Favourite HN Comment?](https://news.ycombinator.com/item?id=24531718) | 哪些 HN 评论值得收藏，征集深入、有启发的社区回复。 | 342 | 230 | 2020-09-20 |
| 5 | [Ask HN: What do you think about “The Social Dilemma”?](https://news.ycombinator.com/item?id=24468533) | 看过纪录片《监视资本主义：智能陷阱》后，你怎么看其中的论述？ | 331 | 248 | 2020-09-14 |
| 6 | [Ask HN: What is your favorite method of sending large files?](https://news.ycombinator.com/item?id=24351111) | 临时架 HTTP 服务之外，给别人发送大文件还有什么方便可靠的方法？ | 319 | 354 | 2020-09-02 |
| 7 | [Ask HN: Suggestions for books about API design?](https://news.ycombinator.com/item?id=24383180) | 正在用 Lambda 构建 REST API，发帖者征集有价值的接口设计书籍。 | 298 | 90 | 2020-09-05 |
| 8 | [Ask HN: Teaching kids how to think?](https://news.ycombinator.com/item?id=24638756) | 如何教孩子思考，寻找适合年幼儿童的材料和日常活动。 | 264 | 139 | 2020-09-30 |
| 9 | [Ask HN: What are good life skills for people to learn?](https://news.ycombinator.com/item?id=24605807) | 从急救到理财，哪些生活技能值得普通人花时间掌握？ | 254 | 270 | 2020-09-27 |
| 10 | [Ask HN: What is it like to be old? What advice would you give to younger people?](https://news.ycombinator.com/item?id=24527978) | 变老是什么感受，邀请年长读者向年轻人分享亲历体会与建议。 | 247 | 301 | 2020-09-19 |

### 2020-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Please stop writing tutorials/tech articles on Medium](https://news.ycombinator.com/item?id=24942037) | 发帖者反对把技术教程放在 Medium，认为付费墙限制了知识获取。 | 556 | 253 | 2020-10-30 |
| 2 | [Ask HN: Who is hiring? (October 2020)](https://news.ycombinator.com/item?id=24651639) | 2020 年 10 月招聘集中帖，可浏览岗位及远程、实习和签证信息。 | 426 | 807 | 2020-10-01 |
| 3 | [Ask HN: Good C++ code bases to read?](https://news.ycombinator.com/item?id=24901244) | 因软件无线电接触 C++，发帖者寻找适合阅读学习的优秀代码库。 | 336 | 253 | 2020-10-26 |
| 4 | [Ask HN: Jack-of-all-trades of HN, how do you approach job search?](https://news.ycombinator.com/item?id=24916016) | 擅长跨领域解决模糊问题的技术多面手，应该怎样寻找合适工作？ | 327 | 250 | 2020-10-28 |
| 5 | [Launch HN: Deepnote (YC S19) – A better data science notebook](https://news.ycombinator.com/item?id=24942797) | Deepnote 团队介绍面向数据科学的新笔记本工具，试图改善分析工作体验。 | 316 | 70 | 2020-10-30 |
| 6 | [Ask HN: Why are there no open source 2d printers?](https://news.ycombinator.com/item?id=24786721) | 开源 3D 打印机很常见，普通二维打印机为什么没有类似的成熟选择？ | 288 | 240 | 2020-10-15 |
| 7 | [Ask HN: Why isn’t finance a part of the core curriculum at schools?](https://news.ycombinator.com/item?id=24877408) | 理财知识影响一生，为何学校还没有把金融教育纳入核心课程？ | 275 | 252 | 2020-10-24 |
| 8 | [Launch HN: Artifact (YC S20) – Personal podcasts with the people in your life](https://news.ycombinator.com/item?id=24919931) | Artifact 帮人们录制亲友的人生故事，把个人记忆保存成私人播客。 | 266 | 105 | 2020-10-28 |
| 9 | [I'm Peter Roberts, immigration attorney who does work for YC and startups. AMA](https://news.ycombinator.com/item?id=24730450) | 移民律师 Peter Roberts 再次开放问答，面向创业者和社区讨论移民事务。 | 251 | 259 | 2020-10-09 |
| 10 | [Ask HN: What are good resources to learn system design?](https://news.ycombinator.com/item?id=24762734) | 后端数据处理方案太多，哪些资源能帮助建立系统设计的判断力？ | 246 | 65 | 2020-10-13 |

### 2020-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Thank You Dang](https://news.ycombinator.com/item?id=25225775) | HN 用户在感恩节感谢管理员 dang 维护社区讨论。 | 2363 | 249 | 2020-11-27 |
| 2 | [Ask HN: What is the best money you have spent on professional development?](https://news.ycombinator.com/item?id=25136258) | 职业发展预算花在哪里最值，征集工程师亲历有效的培训与学习投入。 | 524 | 540 | 2020-11-18 |
| 3 | [Ask HN: Top Coursera Courses?](https://news.ycombinator.com/item?id=25245125) | Coursera 上有哪些值得推荐的课程，领域不限，欢迎分享学习收获。 | 486 | 157 | 2020-11-29 |
| 4 | [Ask HN: As a person, what can I do to improve a city?](https://news.ycombinator.com/item?id=25007697) | 住在治安问题严重的城市，普通居民能做什么让城市变好？ | 479 | 332 | 2020-11-06 |
| 5 | [Ask HN: Who is hiring? (November 2020)](https://news.ycombinator.com/item?id=24969524) | 2020 年 11 月招聘集中帖，企业在此发布职位及候选人要求。 | 348 | 802 | 2020-11-02 |
| 6 | [I've now played with a Raspberry Pi 400 for a week and here are my conclusions](https://news.ycombinator.com/item?id=25161266) | 作者使用树莓派 400 一周后分享体验，讨论这台键盘电脑的实际表现。 | 316 | 219 | 2020-11-20 |
| 7 | [Ask HN: Why do some timestamps on HN have a full stop at the end?](https://news.ycombinator.com/item?id=25197418) | HN 有些时间戳末尾多了句点，这种界面细节代表什么？ | 301 | 111 | 2020-11-24 |
| 8 | [Dan Kohn has died](https://news.ycombinator.com/item?id=24968442) | 帖子通报 Linux 基金会执行负责人 Dan Kohn 去世的消息。 | 276 | 63 | 2020-11-02 |
| 9 | [Ask HN: How do custom software dev firms make money?](https://news.ycombinator.com/item?id=24959238) | 定制软件开发公司如何收费与盈利，发帖者为学校项目了解商业模式。 | 219 | 106 | 2020-11-01 |
| 10 | [Ask HN: Am I too late for the “Data Science” wave?](https://news.ycombinator.com/item?id=25098921) | 农业博士想离开实验室转向数据科学，现在入行是否已经太迟？ | 199 | 143 | 2020-11-15 |

### 2020-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Google outage – resolved](https://news.ycombinator.com/item?id=25415989) | 谷歌多项服务发生故障，帖内更新称服务已恢复。 | 2316 | 827 | 2020-12-14 |
| 2 | [Happy New Year HN](https://news.ycombinator.com/item?id=25595865) | HN 用户感谢社区在 2020 年的陪伴并送上新年祝福。 | 986 | 236 | 2020-12-31 |
| 3 | [Ask HN: Best Talks of 2020?](https://news.ycombinator.com/item?id=25537230) | 回顾 2020 年值得观看的演讲，邀请社区推荐年度精彩分享。 | 729 | 170 | 2020-12-25 |
| 4 | [Ask HN: What's the best paper you've read in 2020?](https://news.ycombinator.com/item?id=25346456) | 2020 年读过哪篇最好的论文，发帖者尤其希望发现近期研究。 | 705 | 192 | 2020-12-08 |
| 5 | [Ask HN: Why does Pinterest dominate Google text search results?](https://news.ycombinator.com/item?id=25538586) | 发帖者发现普通文字搜索也频遇 Pinterest，追问它为何占据 Google 结果。 | 689 | 312 | 2020-12-25 |
| 6 | [Sick of spending time on Auth, we built an open source 'Stripe for Auth'](https://news.ycombinator.com/item?id=25458033) | 反复为创业项目搭建认证后，作者介绍其开源身份认证产品。 | 545 | 339 | 2020-12-17 |
| 7 | [Travis CI is no longer providing CI minutes for open source projects](https://news.ycombinator.com/item?id=25338983) | 发帖者报告 Travis CI 不再为开源项目提供原有 CI 时长安排。 | 523 | 187 | 2020-12-07 |
| 8 | [Ask HN: What are you surprised isn’t being worked on more?](https://news.ycombinator.com/item?id=25559571) | 有哪些重要问题或技术方向，投入研究与开发的人却少得出乎意料？ | 476 | 1239 | 2020-12-28 |
| 9 | [Ask HN: What's a side project you built to make money that hasn't?](https://news.ycombinator.com/item?id=25580637) | 打破副项目成功叙事的幸存者偏差，征集本想赚钱却没赚到的案例。 | 446 | 582 | 2020-12-30 |
| 10 | [Ask HN: What Lived Up to the Hype?](https://news.ycombinator.com/item?id=25525457) | 哪些产品或作品真正兑现了宣传时的期待，甚至配得上最初的热度？ | 424 | 1091 | 2020-12-24 |

### 2021-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Thanks HN: You helped save a company that now helps thousands make a living](https://news.ycombinator.com/item?id=25792719) | Webflow 创始人回顾 HN 如何帮助公司生存并服务更多创业者。 | 1364 | 182 | 2021-01-15 |
| 2 | [Tell HN: Aaron Swartz died today, 8 years ago](https://news.ycombinator.com/item?id=25731566) | 在 Aaron Swartz 逝世八周年之际，帖子再次表达对他的怀念。 | 945 | 184 | 2021-01-11 |
| 3 | [Ask HN: Anyone know any funny programming jokes?](https://news.ycombinator.com/item?id=25850739) | 征集好笑的编程笑话，无论是大众段子还是只有行家能懂的梗。 | 740 | 852 | 2021-01-20 |
| 4 | [Ask HN: Anyone else burnt out due to extended lockdown and work-from-home?](https://news.ycombinator.com/item?id=25833639) | 长期封控和居家办公让效率骤降，还有谁也在经历这种倦怠？ | 702 | 528 | 2021-01-19 |
| 5 | [Tell HN: Dropbox now requires access to contacts for Google login](https://news.ycombinator.com/item?id=25789603) | 发帖者反映 Dropbox 使用 Google 登录时要求访问联系人，质疑其必要性。 | 618 | 384 | 2021-01-15 |
| 6 | [Ask HN: What are you working on?](https://news.ycombinator.com/item?id=25783152) | 你正在开发什么，邀请展示当前的副项目与有趣成果。 | 529 | 1232 | 2021-01-14 |
| 7 | [Ask HN: Show me your half baked project](https://news.ycombinator.com/item?id=25700135) | 项目还没准备好也可以公开，发帖者邀请大家展示自己的半成品。 | 420 | 820 | 2021-01-09 |
| 8 | [Ask HN: Who is hiring? (January 2021)](https://news.ycombinator.com/item?id=25632982) | 2021 年 1 月招聘集中帖，汇集新年岗位与工作安排。 | 407 | 839 | 2021-01-04 |
| 9 | [Ask HN: How to increase SWE salaries in Europe?](https://news.ycombinator.com/item?id=25766884) | 欧洲工程师薪资常低于美国，怎样提高当地软件开发者的收入？ | 392 | 945 | 2021-01-13 |
| 10 | [Ask HN: What does mastery look like in software engineering?](https://news.ycombinator.com/item?id=25643940) | 软件工程师达到精通意味着什么，讨论真正熟练的能力与表现。 | 365 | 276 | 2021-01-05 |

### 2021-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Advice for finding an entry-level remote job?](https://news.ycombinator.com/item?id=26171008) | 初入职场想找远程工作，应该怎样定位机会并提高录用概率？ | 740 | 199 | 2021-02-17 |
| 2 | [Shopify says remove Stripe billing or get booted from their app store](https://news.ycombinator.com/item?id=26260174) | SaaS 经营者称 Shopify 要求撤掉 Stripe 收款，否则将移出应用商店。 | 624 | 225 | 2021-02-25 |
| 3 | [Ask HN: What are the best websites that the Anglosphere doesn't know about?](https://news.ycombinator.com/item?id=26137479) | 英语互联网之外，有哪些高质量网站和独特内容值得跨语言发现？ | 544 | 276 | 2021-02-14 |
| 4 | [Ask HN: Who is hiring? (February 2021)](https://news.ycombinator.com/item?id=25989764) | 2021 年 2 月招聘集中帖，发布岗位并连接企业与求职者。 | 461 | 1043 | 2021-02-01 |
| 5 | [Launch HN: Noya (YC W21) – Direct air capture of CO2 using cooling towers](https://news.ycombinator.com/item?id=26144432) | Noya 尝试利用冷却塔直接捕集空气中的二氧化碳，介绍其降成本思路。 | 401 | 157 | 2021-02-15 |
| 6 | [Ask HN: Why are e-ink note-taking devices so expensive compared to iPads?](https://news.ycombinator.com/item?id=26143407) | 功能看似有限，电子墨水手写设备为何能卖到接近 iPad 的价格？ | 334 | 259 | 2021-02-15 |
| 7 | [Launch HN: Opstrace (YC S19) – open-source Datadog](https://news.ycombinator.com/item?id=25991485) | Opstrace 团队介绍开源可观测性平台，提供类似 Datadog 的替代方案。 | 316 | 114 | 2021-02-01 |
| 8 | [Launch HN: Enombic (YC S20) – Create your own stock indexes](https://news.ycombinator.com/item?id=26265872) | Enombic 让用户设计自己的股票指数，围绕个人需求组合投资标的。 | 305 | 205 | 2021-02-25 |
| 9 | [Ask HN: Recommended books and papers on distributed systems?](https://news.ycombinator.com/item?id=25987664) | 想深入分布式系统，除《数据密集型应用系统设计》外还有哪些书和论文？ | 302 | 63 | 2021-02-01 |
| 10 | [Tell HN: A case of negative SEO I caught on my service and how I dealt with it](https://news.ycombinator.com/item?id=26105890) | 作者称服务遭遇负面 SEO 攻击，分享发现搜索排名下滑及应对的过程。 | 278 | 88 | 2021-02-11 |

### 2021-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Cheapest/easiest way to host a static site?](https://news.ycombinator.com/item?id=26594242) | 托管一个静态网站，怎样把成本、配置步骤和维护负担降到最低？ | 451 | 487 | 2021-03-26 |
| 2 | [Ask HN: Do you think Agile/Scrum is beneficial for software delivery?](https://news.ycombinator.com/item?id=26345235) | 冲刺迭代和每日站会究竟有无帮助，征集敏捷与 Scrum 的实际使用体验。 | 449 | 695 | 2021-03-04 |
| 3 | [Ask HN: What are some “10x” software product innovations you have experienced?](https://news.ycombinator.com/item?id=26477507) | 你用过哪些带来数量级改善的软件创新，明显超越原有解决方式？ | 441 | 795 | 2021-03-16 |
| 4 | [Ask HN: Those who quit their jobs to travel the world, how did it go?](https://news.ycombinator.com/item?id=26407560) | 辞职去环游世界的人，后来过得怎样，又如何看待当初的选择？ | 416 | 450 | 2021-03-10 |
| 5 | [Launch HN: Chatwoot (YC W21) – Open-Source Alternative to Intercom, Zendesk](https://news.ycombinator.com/item?id=26501527) | Chatwoot 团队介绍开源客服平台，提供 Intercom、Zendesk 的替代选择。 | 396 | 110 | 2021-03-18 |
| 6 | [Ask HN: Who is hiring? (March 2021)](https://news.ycombinator.com/item?id=26304051) | 2021 年 3 月招聘集中帖，集中展示企业需求与可申请岗位。 | 361 | 959 | 2021-03-01 |
| 7 | [Ask HN: What was the biggest contributor to your happiness in the past year?](https://news.ycombinator.com/item?id=26528011) | 过去一年里，哪件事最明显地增加了你的幸福感？ | 360 | 532 | 2021-03-21 |
| 8 | [Launch HN: Athens Research (YC W21) – Open-Source Roam Research](https://news.ycombinator.com/item?id=26316793) | Athens Research 介绍开源、优先在本地工作的知识笔记工具。 | 340 | 152 | 2021-03-02 |
| 9 | [Ask HN: I've realized I'm a bad software engineer and I'm over 30, what's next?](https://news.ycombinator.com/item?id=26647717) | 从业十年后觉得自己技术不足，三十多岁的工程师如何重新规划下一步？ | 320 | 263 | 2021-03-31 |
| 10 | [Launch HN: Remora (YC W21) – Carbon capture for semi trucks](https://news.ycombinator.com/item?id=26412624) | Remora 团队展示面向半挂卡车的碳捕集设备，尝试降低运输排放。 | 304 | 196 | 2021-03-10 |

### 2021-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What tech job would let me get away with the least real work possible?](https://news.ycombinator.com/item?id=26721951) | 一位对工作失去热情的开发者询问哪些技术岗位实际工作最少。 | 2022 | 1091 | 2021-04-07 |
| 2 | [Ask HN: How can a unhireable person get a job?](https://news.ycombinator.com/item?id=26825017) | 求职一年仍屡遭拒绝，发帖者询问自觉难被雇用的人如何找到工作。 | 529 | 819 | 2021-04-15 |
| 3 | [Ask HN: Does anyone else find the AWS Lambda developer experience frustrating?](https://news.ycombinator.com/item?id=26855037) | 用 AWS Lambda 串联服务时频遇不便，其他开发者是否也觉得体验挫败？ | 422 | 278 | 2021-04-18 |
| 4 | [Ask HN: Who is hiring? (April 2021)](https://news.ycombinator.com/item?id=26661443) | 2021 年 4 月招聘集中帖，查看各家公司发布的岗位及条件。 | 416 | 964 | 2021-04-01 |
| 5 | [Ask HN: What under-the-radar technology are you excited about?](https://news.ycombinator.com/item?id=26780866) | 有哪些尚未引起广泛注意、却让你看好未来的技术？ | 347 | 535 | 2021-04-12 |
| 6 | [Ask HN: What novel tools are you using to write web sites/apps?](https://news.ycombinator.com/item?id=26693959) | 如今写网站或应用，你采用了哪些新颖工具、语言和开发方式？ | 345 | 322 | 2021-04-05 |
| 7 | [Ask HN: I bought Voltaren at the chemist, now Google shows me ads for it. Why?](https://news.ycombinator.com/item?id=26850913) | 药店买完药就看到相关广告，发帖者追问 Google 如何获知线下购买行为。 | 323 | 469 | 2021-04-18 |
| 8 | [Ask HN: Why is the Linux community struggling to implement hibernation?](https://news.ycombinator.com/item?id=26739220) | 发现 Ubuntu 默认禁用休眠后，发帖者询问 Linux 休眠支持为何如此困难。 | 322 | 332 | 2021-04-08 |
| 9 | [Twilio blocked our account and with it hundreds of our customers [resolved]](https://news.ycombinator.com/item?id=26815768) | 创业者讲述 Twilio 封禁账号连累大量客户的经历，标题注明问题已解决。 | 312 | 156 | 2021-04-15 |
| 10 | [Ask HN: How would you store 10PB of data for your startup today?](https://news.ycombinator.com/item?id=26912321) | 创业公司数据已超过 10PB，云端合同将到期，该如何选择存储架构？ | 307 | 366 | 2021-04-23 |

### 2021-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Favorite Blogs by Individuals?](https://news.ycombinator.com/item?id=27302195) | 哪些由个人经营的博客值得长期关注，邀请分享喜爱的作者。 | 819 | 271 | 2021-05-27 |
| 2 | [Ask HN: Favorite purchases of last two years?](https://news.ycombinator.com/item?id=27219759) | 过去两年买过什么好东西，发帖者希望借亲身体验替代不可信的网络评测。 | 483 | 1191 | 2021-05-20 |
| 3 | [Ask HN: Are you satisfied with Elixir or do you regret choosing Elixir?](https://news.ycombinator.com/item?id=27192873) | 新项目考虑使用 Elixir，想听采用者的满意之处与后悔之处。 | 387 | 287 | 2021-05-18 |
| 4 | [Ask HN: How to negotiate continuing to work remotely?](https://news.ycombinator.com/item?id=27123553) | 疫情后想继续远程办公，如何与原本要求到办公室的雇主谈判？ | 370 | 277 | 2021-05-11 |
| 5 | [Ask HN: What are some tools / libraries you built yourself?](https://news.ycombinator.com/item?id=27171970) | 现成库之外，你亲手写过哪些工具或库，解决了什么具体需求？ | 364 | 602 | 2021-05-16 |
| 6 | [Ask HN: Alternatives to Google Photos?](https://news.ycombinator.com/item?id=27338008) | Google Photos 免费存储政策即将结束，照片管理与备份有哪些替代选择？ | 362 | 306 | 2021-05-30 |
| 7 | [Ask HN: How to get started with audio programming?](https://news.ycombinator.com/item?id=27273706) | 喜欢音频编程教材却不知下一步，怎样入门声音处理与相关开发？ | 358 | 120 | 2021-05-25 |
| 8 | [Ask HN: Who is hiring? (May 2021)](https://news.ycombinator.com/item?id=27025922) | 2021 年 5 月招聘集中帖，可浏览企业职位与远程工作要求。 | 328 | 913 | 2021-05-03 |
| 9 | [Ask HN: Anybody Started a Research Institute?](https://news.ycombinator.com/item?id=27300594) | 如何创办研究机构，发帖者希望联系有过相关实践的人。 | 287 | 163 | 2021-05-27 |
| 10 | [Ask HN: How to cope with the death of a dear person?](https://news.ycombinator.com/item?id=27323430) | 亲人刚刚离世，发帖者寻求面对失去、哀伤和突然告别的经验。 | 263 | 94 | 2021-05-29 |

### 2021-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: I was hit with a patent troll lawsuit, how do I deal with it?](https://news.ycombinator.com/item?id=27579693) | 被疑似专利流氓起诉后该怎么办，发帖者寻找应对诉讼的实际建议。 | 833 | 308 | 2021-06-21 |
| 2 | [Tell HN: SMS-based two-factor authentication is not secure](https://news.ycombinator.com/item?id=27447206) | 发帖者结合自身遭遇提醒：基于短信的双因素认证仍可能被攻破。 | 628 | 286 | 2021-06-09 |
| 3 | [Ask HN: Feeling guilty for doing the bare minimum at work](https://news.ycombinator.com/item?id=27593462) | 工作中只完成最低要求却感到内疚，该如何看待摸鱼与职业责任？ | 563 | 398 | 2021-06-22 |
| 4 | [Ask HN: “Tank man” image search blocked on Bing and DuckDuckGo](https://news.ycombinator.com/item?id=27394925) | 发帖者报告 Bing 和 DuckDuckGo 的“坦克人”图片搜索异常，询问原因。 | 560 | 126 | 2021-06-04 |
| 5 | [In Praise of Open Source Textbooks](https://news.ycombinator.com/item?id=27414145) | 作者借学习线性代数的经历，谈开放教材给自学者带来的帮助。 | 506 | 104 | 2021-06-06 |
| 6 | [Ask HN: Notion is withholding my company data, what can I do?](https://news.ycombinator.com/item?id=27612894) | 长期付费客户称无法取回公司在 Notion 的数据，向社区寻求办法。 | 479 | 194 | 2021-06-24 |
| 7 | [Ask HN: Good books/courses to learn networking essentials for web developers?](https://news.ycombinator.com/item?id=27650775) | Web 开发者想弄懂应用背后的网络基础设施，哪些书和课程值得读？ | 430 | 71 | 2021-06-27 |
| 8 | [Ask HN: Who is hiring? (June 2021)](https://news.ycombinator.com/item?id=27355392) | 2021 年 6 月招聘集中帖，企业集中介绍岗位、地点及申请条件。 | 365 | 1029 | 2021-06-01 |
| 9 | [Ask HN: How to learn proper systems programming?](https://news.ycombinator.com/item?id=27577514) | 多年做前后端后开始学 Rust，怎样系统掌握真正的系统编程能力？ | 336 | 93 | 2021-06-21 |
| 10 | [Ask HN: What huge mistake did you make early in your career?](https://news.ycombinator.com/item?id=27548204) | 职业早期犯过哪些当时以为会丢掉工作的重大错误，邀请分享教训。 | 303 | 476 | 2021-06-18 |

### 2021-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: YC will help you find a co-founder](https://news.ycombinator.com/item?id=27750298) | YC Startup School 介绍寻找联合创始人的服务，帮助创业者建立合作。 | 433 | 131 | 2021-07-06 |
| 2 | [Ask HN: Who is hiring? (July 2021)](https://news.ycombinator.com/item?id=27699704) | 2021 年 7 月招聘集中帖，连接正在招人的团队与求职者。 | 399 | 976 | 2021-07-01 |
| 3 | [Ask HN: Recruiters want people who do side projects, yet contracts forbid them?](https://news.ycombinator.com/item?id=27843198) | 招聘看重副项目，雇佣合同却可能禁止它们，开发者该如何理解这种矛盾？ | 344 | 223 | 2021-07-15 |
| 4 | [Ask HN: My country may be in the midst of a coup – how should I get prepared?](https://news.ycombinator.com/item?id=28008571) | 担心突尼斯出现政变，发帖者询问普通人应如何提前做好生活准备。 | 274 | 176 | 2021-07-30 |
| 5 | [Tell HN: Coming soon – “Meet the Batch” threads for parallel Launch HNs](https://news.ycombinator.com/item?id=27877280) | HN 预告“Meet the Batch”栏目，计划在一帖中介绍多家 YC 创业公司。 | 272 | 91 | 2021-07-18 |
| 6 | [Tell HN: Consider listing your contact details](https://news.ycombinator.com/item?id=28012969) | 发帖者建议在 HN 个人资料中留下联系方式，让有价值的交流继续。 | 266 | 189 | 2021-07-30 |
| 7 | [Ask HN: Do you have a process or a framework to learn specific skills quickly?](https://news.ycombinator.com/item?id=28017289) | 有没有可复用的快速学习框架，既学会技能，又记得住、讲得清？ | 247 | 114 | 2021-07-31 |
| 8 | [It's been three years. Stop saying your European visitors are important to you](https://news.ycombinator.com/item?id=27854663) | 欧洲读者反感多年不变的地区访问限制，质疑网站对欧洲用户的重视承诺。 | 231 | 181 | 2021-07-16 |
| 9 | [Ask HN: Anyone here built successful SaaS/startup just for money?](https://news.ycombinator.com/item?id=27853352) | 不再对技术愿景兴奋，只为赚钱创业是否可行，征集真实案例。 | 224 | 146 | 2021-07-16 |
| 10 | [Launch HN: Exams, tasks, K8, eCommerce, cell sites, health, data quality, travel](https://news.ycombinator.com/item?id=27930562) | 首期“Meet the Batch”集中介绍考试、电商、健康、数据质量等领域的项目。 | 219 | 124 | 2021-07-23 |

### 2021-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Google is confusing me with others in a harmful way – what can I do?](https://news.ycombinator.com/item?id=28216733) | Google 搜索把自己与他人混为一谈并造成伤害，发帖者询问纠正途径。 | 964 | 282 | 2021-08-18 |
| 2 | [Launch HN: Heimdal (YC S21) – Carbon neutral cement](https://news.ycombinator.com/item?id=28036927) | Heimdal 团队介绍碳中和水泥方案，尝试把碳处理与建材生产结合。 | 617 | 220 | 2021-08-02 |
| 3 | [Ask HN: What's the most life-changing blog post you've ever read?](https://news.ycombinator.com/item?id=28232165) | 哪篇博客改变过你的生活、职业或工作方式，征集影响深远的文章。 | 614 | 380 | 2021-08-19 |
| 4 | [Ask HN: Why does Zoom Desktop examine all processes and arguments?](https://news.ycombinator.com/item?id=28213292) | 检查系统调用发现 Zoom 读取全部进程和参数，发帖者追问其用途。 | 547 | 263 | 2021-08-17 |
| 5 | [Ask HN: What Apple alternatives are you switching to?](https://news.ycombinator.com/item?id=28220968) | 因 Apple 的 CSAM 检测计划而考虑离开，你会改用哪些设备和服务？ | 529 | 470 | 2021-08-18 |
| 6 | [Launch HN: Slip (YC S21) – Build and sell interactive programming courses](https://news.ycombinator.com/item?id=28141462) | Slip 提供互动编程课程的制作与销售平台，让程序员出售自己的课程。 | 399 | 108 | 2021-08-11 |
| 7 | [Launch HN: BlackOakTV (YC S21) – Netflix for black people](https://news.ycombinator.com/item?id=28087309) | BlackOakTV 团队介绍面向黑人观众的订阅视频平台。 | 377 | 741 | 2021-08-06 |
| 8 | [Ask HN: Who is hiring? (August 2021)](https://news.ycombinator.com/item?id=28037366) | 2021 年 8 月招聘集中帖，查看公司需求及各类工作机会。 | 357 | 895 | 2021-08-02 |
| 9 | [Launch HN: Hotswap (YC S21) – Easily migrate customers away from competitors](https://news.ycombinator.com/item?id=28327660) | Hotswap 尝试自动化客户迁移流程，让新用户更容易从竞争产品切换过来。 | 345 | 152 | 2021-08-27 |
| 10 | [Ask HN: Companies of one, what is your tech stack?](https://news.ycombinator.com/item?id=28299053) | 一个人经营公司时如何选技术栈，邀请独立创业者分享实际组合。 | 312 | 320 | 2021-08-25 |

### 2021-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Thanks to thehodge and littlewarden.com, this site is up today](https://news.ycombinator.com/item?id=28472350) | HN 感谢用户发现证书即将过期并及时提醒网站维护者。 | 1314 | 78 | 2021-09-09 |
| 2 | [Ask HN: Are you also getting extremely obvious spam bypassing Gmail's filters?](https://news.ycombinator.com/item?id=28635313) | 明显的垃圾邮件频繁漏过 Gmail 过滤，还有谁遇到相同现象？ | 575 | 282 | 2021-09-23 |
| 3 | [Tell HN: Amplitude (YC W12) just went public – AMA](https://news.ycombinator.com/item?id=28696641) | Amplitude 上市之际，创业者回到 HN 分享经历并开放问答。 | 416 | 150 | 2021-09-29 |
| 4 | [Ask HN: Who is hiring? (September 2021)](https://news.ycombinator.com/item?id=28380661) | 2021 年 9 月招聘集中帖，集中发布企业岗位和工作条件。 | 355 | 955 | 2021-09-01 |
| 5 | [Ask HN: What could a modern database do that PostgreSQL and MySQL can't](https://news.ycombinator.com/item?id=28425379) | 如果今天重新设计通用事务数据库，应该加入 PostgreSQL、MySQL 缺少的什么？ | 338 | 321 | 2021-09-05 |
| 6 | [Ask HN: Where are all the old Show HNs?](https://news.ycombinator.com/item?id=28682173) | 旧 Show HN 项目大量消失了，发帖者追问这些作品后来的命运。 | 284 | 159 | 2021-09-28 |
| 7 | [Ask HN: How Do You Learn?](https://news.ycombinator.com/item?id=28482726) | 你如何学习和记忆新知识，比较书籍、视频与间隔重复等个人习惯。 | 274 | 171 | 2021-09-10 |
| 8 | [Launch HN: RescueTime (YC W08) – Redesigned for wellness, balance, remote work](https://news.ycombinator.com/item?id=28683597) | RescueTime 介绍重新设计后的产品，强调远程工作的健康、平衡与专注。 | 207 | 141 | 2021-09-28 |
| 9 | [Ask HN: Books that teach you programming languages via systems projects?](https://news.ycombinator.com/item?id=28478751) | 有哪些教材通过构建系统项目来教编程语言，让语言学习与工程实践结合？ | 204 | 66 | 2021-09-10 |
| 10 | [Ask HN: Do you still miss your RIM BlackBerry?](https://news.ycombinator.com/item?id=28517447) | 黑莓是否仍比现代触屏手机更适合沟通，邀请老用户回忆使用体验。 | 190 | 261 | 2021-09-13 |

### 2021-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [It's weird that most of “Hacker” news is dominated by business news](https://news.ycombinator.com/item?id=28812281) | 发帖者觉得 HN 商业新闻过多，希望看到更多围绕软件和技术本身的讨论。 | 682 | 282 | 2021-10-09 |
| 2 | [Ask HN: Best way to host a website for 500 years?](https://news.ycombinator.com/item?id=28957573) | 如何让个人网站存活五百年，让后代仍能访问今天留下的内容？ | 666 | 787 | 2021-10-22 |
| 3 | [Thank HN: 7 years and $7M later, it all started right here](https://news.ycombinator.com/item?id=28902215) | BEE 团队回顾七年与七百万美元收入的历程，感谢最初来自 HN 的支持。 | 501 | 58 | 2021-10-18 |
| 4 | [Project Gutenberg is no longer fully blocked in Germany](https://news.ycombinator.com/item?id=29024039) | 发帖者称古登堡计划在德国恢复大部分访问，封锁范围缩至特定作品。 | 450 | 99 | 2021-10-28 |
| 5 | [VSCode deprecates Enable Telemetry, auto-enrolls you in Telemetry?](https://news.ycombinator.com/item?id=28812486) | 发帖者质疑 VS Code 遥测设置变更是否会把此前退出的用户重新纳入。 | 388 | 181 | 2021-10-09 |
| 6 | [Ask HN: Who is hiring? (October 2021)](https://news.ycombinator.com/item?id=28719320) | 2021 年 10 月招聘集中帖，雇主发布职位并注明地点和远程条件。 | 375 | 837 | 2021-10-01 |
| 7 | [Ask HN: Is HN having problem keeping up today?](https://news.ycombinator.com/item?id=28750538) | HN 当天频繁无法访问，发帖者询问站点是否遭遇流量或服务故障。 | 371 | 152 | 2021-10-04 |
| 8 | [Ask HN: Solo-preneurs, how do you DevOps to save time?](https://news.ycombinator.com/item?id=28838132) | 一个人或极小团队运营 Web 产品，如何减少 DevOps 占用的时间？ | 356 | 317 | 2021-10-12 |
| 9 | [Ask HN: Is the Great Resignation in tech real? If so, why?](https://news.ycombinator.com/item?id=28973942) | 科技行业真的出现了“大辞职潮”吗，邀请分享跳槽现象及背后原因。 | 325 | 259 | 2021-10-24 |
| 10 | [Ask HN: Whatever happened to exploring the internet?](https://news.ycombinator.com/item?id=28976069) | 每天只浏览固定几个网站，怎样重新找回探索互联网的乐趣？ | 320 | 268 | 2021-10-24 |

### 2021-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Accepted and ghosted: interviewing for a leadership position at Stripe](https://news.ycombinator.com/item?id=29387264) | 求职者分享获 Stripe 领导岗位认可后却被冷处理的面试经历。 | 1703 | 655 | 2021-11-30 |
| 2 | [Tell HN: Happy Thanksgiving Everyone](https://news.ycombinator.com/item?id=29338155) | HN 用户在感恩节感谢社区提供的知识与交流。 | 1098 | 224 | 2021-11-25 |
| 3 | [Aaron Swartz Rememberance Day This Monday](https://news.ycombinator.com/item?id=29147888) | 帖子提醒即将到来的 Aaron Swartz 纪念日，回顾他留下的影响。 | 805 | 192 | 2021-11-08 |
| 4 | [Ask HN: Has Google search become quantitatively worse?](https://news.ycombinator.com/item?id=29392702) | Google 搜索是否真的变差了，发帖者希望超越个人感受讨论质量变化。 | 755 | 494 | 2021-11-30 |
| 5 | [Ask HN: What you up to? (Who doesn't want to be hired?)](https://news.ycombinator.com/item?id=29073996) | 暂且放下招聘话题，聊聊工作之外的生活、兴趣与最近在做的事。 | 614 | 841 | 2021-11-01 |
| 6 | [Ask HN: I feel so shallow and dumb when I see what other smart people are doing](https://news.ycombinator.com/item?id=29281468) | 看到聪明人做出的杰作就觉得自己浅薄无能，该怎样面对这种比较？ | 534 | 336 | 2021-11-19 |
| 7 | [Ask HN: What are the best-designed things you've ever used?](https://news.ycombinator.com/item?id=29353980) | 你用过哪些设计特别出色的东西，欢迎从日用品里发现优秀设计。 | 515 | 972 | 2021-11-26 |
| 8 | [Ask HN: Who's not sucky to work for?](https://news.ycombinator.com/item?id=29099746) | 换过多家公司仍对管理失望，哪些雇主真正值得为之工作？ | 471 | 426 | 2021-11-03 |
| 9 | [Ask HN: Software Engineer hitting 40: what's next?](https://news.ycombinator.com/item?id=29360119) | 软件工程师接近四十岁、从业十八年后，职业道路还能怎样继续？ | 442 | 349 | 2021-11-27 |
| 10 | [Tell HN: GitHub is down again](https://news.ycombinator.com/item?id=29363169) | 发帖者报告 GitHub 再次无法使用，同时质疑官方状态页仍显示正常。 | 442 | 272 | 2021-11-27 |

### 2021-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Are most of us developers lying about how much work we do?](https://news.ycombinator.com/item?id=29581125) | 一位每周实际工作五至十小时的开发者询问同行是否也夸大工作量。 | 1665 | 1058 | 2021-12-16 |
| 2 | [Tell HN: You are not alone this Christmas](https://news.ycombinator.com/item?id=29682002) | 独自过圣诞节的用户向有相似处境的人送上陪伴。 | 1193 | 313 | 2021-12-25 |
| 3 | [Tell HN: AWS appears to be down again](https://news.ycombinator.com/item?id=29567170) | 发帖者怀疑 AWS 再次发生故障，询问其他用户是否也遇到异常。 | 879 | 468 | 2021-12-15 |
| 4 | [Ask HN: How did my LastPass master password get leaked?](https://news.ycombinator.com/item?id=29705957) | LastPass 主密码疑似泄露，发帖者描述异常遭遇并征集可能的解释。 | 877 | 515 | 2021-12-27 |
| 5 | [25-Dec. Shout-out to everyone else at work](https://news.ycombinator.com/item?id=29683936) | 圣诞节仍在办公室的读者互相致意，分享节日期间值班的经历。 | 872 | 202 | 2021-12-25 |
| 6 | [Tell HN: AWS appears to be down again](https://news.ycombinator.com/item?id=29648286) | 发帖者称 AWS 控制台时通时断，向社区确认是否发生服务故障。 | 863 | 614 | 2021-12-22 |
| 7 | [Ask HN: Those making $500/month on side projects in 2021 – Show and tell](https://news.ycombinator.com/item?id=29667095) | 2021 年有哪些副项目做到每月收入 500 美元，邀请作者展示与交流。 | 782 | 841 | 2021-12-23 |
| 8 | [YouTube suspended my account for posting DeFi hackathon video](https://news.ycombinator.com/item?id=29458246) | 发帖者称发布 DeFi 黑客松视频后 YouTube 账号被停用，质疑自动审核。 | 639 | 370 | 2021-12-06 |
| 9 | [Ask HN: Best Way to Contact YouTube](https://news.ycombinator.com/item?id=29540708) | YouTube 频道突然被封，如何找到有效的人工沟通与申诉渠道？ | 604 | 166 | 2021-12-13 |
| 10 | [Ask HN: What are these low quality “code snippet” sites?](https://news.ycombinator.com/item?id=29403947) | 搜索编程问题时满是搬运问答的低质量代码站，它们为何如此普遍？ | 594 | 316 | 2021-12-01 |

### 2022-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Salary data is for sale](https://news.ycombinator.com/item?id=29834753) | 用户提醒 Equifax 正出售含薪资与历史工资单的就业数据。 | 1690 | 762 | 2022-01-07 |
| 2 | [Ask HN: Gmail account security](https://news.ycombinator.com/item?id=30051054) | 用户知道密码却因设备验证无法登录 Gmail，询问解决办法。 | 1508 | 774 | 2022-01-23 |
| 3 | [Ask HN: Firefox connection problems after enabling DoH?](https://news.ycombinator.com/item?id=29918052) | 开启 DNS over HTTPS 后 Firefox 出现连接问题，其他人是否能复现？ | 696 | 395 | 2022-01-13 |
| 4 | [Last Windows 11 update changed all default browser settings to Edge](https://news.ycombinator.com/item?id=30055222) | 发帖者称 Windows 11 更新改动了默认浏览器和搜索设置，偏向 Edge 与 Bing。 | 619 | 440 | 2022-01-24 |
| 5 | [Ask HN: Hacker claimed ownership and then deleted my Facebook Page of 50k users](https://news.ycombinator.com/item?id=30102240) | 发帖者称拥有五万订阅者的 Facebook 页面遭夺取后删除，寻求挽回办法。 | 617 | 222 | 2022-01-27 |
| 6 | [Ask HN: Is the past disappearing on the web?](https://news.ycombinator.com/item?id=30083783) | 旧内容越来越难找到，互联网是否正在失去可供回看的过去？ | 569 | 316 | 2022-01-26 |
| 7 | [Ask HN: Those making $500/month on side projects in 2022 – Show and tell](https://news.ycombinator.com/item?id=29995152) | 2022 年副项目月入 500 美元的作者请来分享，看看小生意如何起步。 | 540 | 613 | 2022-01-19 |
| 8 | [Ask HN: At a peak of my dev career, I hate my life](https://news.ycombinator.com/item?id=30132560) | 职业达到高点却讨厌自己的生活，开发者寻求对失落与不满的理解。 | 427 | 496 | 2022-01-30 |
| 9 | [Tell HN: We have a responsibility to speak out against blockchain technologies](https://news.ycombinator.com/item?id=30120437) | 发帖者主张技术从业者有责任公开反对区块链、加密货币与 NFT。 | 426 | 382 | 2022-01-28 |
| 10 | [Ask HN: Who wants to collaborate?](https://news.ycombinator.com/item?id=29759115) | 招聘之外，是否有人愿意一起做项目，邀请寻找合作伙伴的读者自荐。 | 424 | 506 | 2022-01-01 |

### 2022-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Namecheap: Russia Service Termination](https://news.ycombinator.com/item?id=30504812) | Namecheap 通知俄罗斯注册用户将终止服务，理由是俄乌战争。 | 1735 | 1825 | 2022-02-28 |
| 2 | [Ask HN: What made your business take off that you wish you'd done much earlier?](https://news.ycombinator.com/item?id=30329762) | 征集让业务起飞、却遗憾没有更早采取的行动。 | 1147 | 466 | 2022-02-14 |
| 3 | [Tell HN: YouTube is banning accounts that support Ukraine](https://news.ycombinator.com/item?id=30467384) | 用户转述支持乌克兰的 YouTube 账号被封禁的报告。 | 1095 | 285 | 2022-02-25 |
| 4 | [Ask HN: How do you deal with getting old and feeling lost?](https://news.ycombinator.com/item?id=30230620) | 即将三十五岁的用户询问如何面对变老与人生迷茫。 | 1094 | 849 | 2022-02-06 |
| 5 | [Tell HN: YouTube and how my wife lost 7 years of work](https://news.ycombinator.com/item?id=30401241) | 用户求助，称 YouTube 删除了妻子七年积累的七百个培训视频。 | 1061 | 429 | 2022-02-19 |
| 6 | [Google to turn on activity tracking for many users who turned it off](https://news.ycombinator.com/item?id=30171800) | 发帖者转述 Google 邮件，担心此前关闭的活动追踪将被重新开启。 | 947 | 430 | 2022-02-02 |
| 7 | [Tell HN: I let my 6-year-old daughter design my website](https://news.ycombinator.com/item?id=30344989) | 作者在春节假期让六岁女儿设计自己的网站，分享亲子创作的尝试。 | 923 | 182 | 2022-02-15 |
| 8 | [Google Maps now requires WiFi scanning to use navigation](https://news.ycombinator.com/item?id=30167865) | 发帖者称 Google Maps 导航新增 WiFi 扫描要求，质疑仅靠 GPS 为何不够。 | 745 | 438 | 2022-02-01 |
| 9 | [Ask HN: How to prepare as soon-to-be blind developer?](https://news.ycombinator.com/item?id=30339187) | 朋友视力快速衰退、即将失明，程序员应如何准备工具与职业适应？ | 696 | 171 | 2022-02-14 |
| 10 | [Dell deletes Latitude CPU Throttling issue after link is posted here](https://news.ycombinator.com/item?id=30333956) | 发帖者称 Latitude CPU 降频问题在 HN 被讨论后，Dell 删除了相关页面。 | 614 | 296 | 2022-02-14 |

### 2022-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: If You Are in Russia](https://news.ycombinator.com/item?id=30508314) | 帖子提醒俄罗斯用户，依赖西方企业服务可能面临中断，需要提前准备。 | 727 | 1068 | 2022-03-01 |
| 2 | [Tell HN: A $40B company killed my 2yo son. Now they force me to keep silent](https://news.ycombinator.com/item?id=30763464) | 一位父亲称幼子遭垃圾车事故夺命，并控诉涉事企业施压要求其保持沉默。 | 626 | 120 | 2022-03-22 |
| 3 | [Ask HN: Who operates at scale without containers?](https://news.ycombinator.com/item?id=30767393) | 哪些团队不用容器也能运营大规模分布式系统，征集实际部署经验。 | 601 | 432 | 2022-03-22 |
| 4 | [Ask HN: Which book can attract anyone towards your field of study?](https://news.ycombinator.com/item?id=30822339) | 如果只推荐一本书吸引外行进入你的专业，你会选择哪一本？ | 569 | 273 | 2022-03-27 |
| 5 | [Ask HN: If you used to be socially awkward and shy, how did you improve?](https://news.ycombinator.com/item?id=30814248) | 曾经害羞、社交笨拙的人如何改善，发帖者想听可实践的亲身经验。 | 520 | 543 | 2022-03-26 |
| 6 | [Cloudflare have made it impossible for me to unsubscribe from marketing emails](https://news.ycombinator.com/item?id=30764757) | 发帖者抱怨无法退订 Cloudflare 营销邮件，讲述尝试退出订阅的障碍。 | 450 | 193 | 2022-03-22 |
| 7 | [Launch HN: Living Carbon (YC W20) – Trees that capture and store more carbon](https://news.ycombinator.com/item?id=30672841) | Living Carbon 介绍生物技术树木项目，希望提高树木捕集和储存碳的能力。 | 424 | 256 | 2022-03-14 |
| 8 | [Tell HN: There needs to be a “right to speak with a human”](https://news.ycombinator.com/item?id=30788681) | 多次求助企业却碰不到真人，发帖者呼吁建立与人工客服交谈的权利。 | 418 | 339 | 2022-03-24 |
| 9 | [Ask HN: What bits of fundamental knowledge are productivity multipliers?](https://news.ycombinator.com/item?id=30853807) | 哪些基础知识一旦掌握，就能在很多工作中成倍提高效率？ | 413 | 418 | 2022-03-30 |
| 10 | [Zelensky video deepfake](https://news.ycombinator.com/item?id=30697932) | 发帖者报告冒充泽连斯基要求投降的深度伪造视频出现，关注战时信息真伪。 | 399 | 281 | 2022-03-16 |

### 2022-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: My kid's school installed spyware and I can't remove it](https://news.ycombinator.com/item?id=30911623) | 家长称学校在私人 Chromebook 安装监控软件，且无法自行移除。 | 936 | 417 | 2022-04-04 |
| 2 | [Ask HN: When did 7 interviews become “normal”?](https://news.ycombinator.com/item?id=30889019) | 求职要面试七轮何时成了常态，讨论招聘流程为何越来越漫长。 | 711 | 813 | 2022-04-02 |
| 3 | [Ask HN: Internet magically gets faster when opening speedtest?](https://news.ycombinator.com/item?id=31062799) | 打开测速网站网速就变快，发帖者询问这种观察可能有哪些解释。 | 685 | 345 | 2022-04-17 |
| 4 | [Ask HN: Share your personal site](https://news.ycombinator.com/item?id=30934529) | 邀请读者展示个人网站，互相发现内容并交流设计与建设思路。 | 665 | 1383 | 2022-04-06 |
| 5 | [Tell HN: Recruiters are lying about remote positions](https://news.ycombinator.com/item?id=30945451) | 发帖者讲述大厂面试经历，称招聘人员对岗位能否远程作了误导承诺。 | 580 | 430 | 2022-04-07 |
| 6 | [Ask HN: Have you used SQLite as a primary database?](https://news.ycombinator.com/item?id=31152490) | SQLite 能否担任主要数据库，寻找把它用于真实项目核心存储的经验。 | 518 | 325 | 2022-04-25 |
| 7 | [Ask HN: Where can I see many examples of real companies' software architecture?](https://news.ycombinator.com/item?id=30986893) | 想了解实际工程取舍，哪里能看到大量真实公司的软件架构案例？ | 469 | 102 | 2022-04-11 |
| 8 | [Ask HN: I'm interested in so many disciplines, but what can I do with that?](https://news.ycombinator.com/item?id=30928105) | 同时对许多学科感兴趣，怎样把广泛好奇变成有方向的学习或事业？ | 444 | 314 | 2022-04-06 |
| 9 | [Ask HN: Am I going insane or is there genuinely no value in blockchain tech?](https://news.ycombinator.com/item?id=31132610) | 研究区块链后仍看不到实际价值，发帖者请社区检验自己的判断。 | 424 | 549 | 2022-04-23 |
| 10 | [Ask HN: Have you created programs for only your personal use?](https://news.ycombinator.com/item?id=31018836) | 你写过只给自己日常使用的程序吗，邀请分享个人软件及其用途。 | 423 | 651 | 2022-04-13 |

### 2022-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [No Dislikes has officially ruined YouTube for me](https://news.ycombinator.com/item?id=31324917) | 用户认为隐藏点踩数让 YouTube 充斥误导性推荐视频。 | 1097 | 479 | 2022-05-10 |
| 2 | [Ask HN: What game do you wish existed?](https://news.ycombinator.com/item?id=31503201) | 你一直希望有、市场上却还没有的游戏是什么样？ | 859 | 1837 | 2022-05-25 |
| 3 | [Ask HN: Burnt-out, directionless but want to turn it around](https://news.ycombinator.com/item?id=31565514) | 长期编程却陷入倦怠与迷茫，发帖者希望找到重新振作的方向。 | 798 | 500 | 2022-05-31 |
| 4 | [Ask HN: Is anyone else glad the crypto market is crashing?](https://news.ycombinator.com/item?id=31356579) | 发帖者坦言对加密货币市场下跌感到释然，询问是否有人有相同想法。 | 627 | 629 | 2022-05-12 |
| 5 | [Tell HN: Job interview canceled due to looming recession](https://news.ycombinator.com/item?id=31494417) | 求职者称小公司因担忧经济衰退取消面试，分享招聘降温的信号。 | 618 | 550 | 2022-05-24 |
| 6 | [Tell HN: I was permanently banned from eBay in one hour](https://news.ycombinator.com/item?id=31305341) | 只是想卖闲置电子产品，发帖者称注册 eBay 一小时内就遭永久封禁。 | 612 | 441 | 2022-05-08 |
| 7 | [Tell HN: The loneliness of a pretty good developer](https://news.ycombinator.com/item?id=31438426) | 自认能力很强却感到孤独，开发者寻找其他高水平同行的相似体验。 | 597 | 494 | 2022-05-19 |
| 8 | [Tell HN: I made $1000 with my app and now making $500/mo](https://news.ycombinator.com/item?id=31508009) | 作者分享应用累计赚到一千美元、并开始每月收入五百美元的进展。 | 578 | 181 | 2022-05-25 |
| 9 | [Ask HN: How to learn math from zero for adults?](https://news.ycombinator.com/item?id=31539549) | 26 岁想学机器学习却缺数学基础，成年人如何从零补起？ | 559 | 172 | 2022-05-28 |
| 10 | [Ask HN: Why can't I learn anymore?](https://news.ycombinator.com/item?id=31281919) | 从业十五年后感觉再也学不进去，开发者探讨学习能力停滞的原因。 | 419 | 320 | 2022-05-06 |

### 2022-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: I'm Afraid We're Shutting Down](https://news.ycombinator.com/item?id=31598978) | 面向有犯罪记录者提供就业与社交服务的创业者宣布计划关闭公司。 | 1633 | 353 | 2022-06-02 |
| 2 | [Ask HN: GPT-3 reveals my full name – can I do anything?](https://news.ycombinator.com/item?id=31883373) | GPT-3 输出了自己的全名，发帖者询问语言模型中的个人信息该如何处理。 | 710 | 346 | 2022-06-26 |
| 3 | [Tell HN: Banned from LinkedIn for Reporting Wickr Drug Spam](https://news.ycombinator.com/item?id=31762904) | 发帖者称举报 Wickr 的毒品垃圾信息后反被 LinkedIn 封号。 | 667 | 237 | 2022-06-16 |
| 4 | [Tell HN: Triplebyte is, yet again, making user profiles public without consent?](https://news.ycombinator.com/item?id=31769601) | 发帖者再次质疑 Triplebyte 未获同意公开用户档案，关注招聘隐私。 | 610 | 125 | 2022-06-16 |
| 5 | [Thank HN: Five months ago, I was feeling like a loser, now I am opposite](https://news.ycombinator.com/item?id=31732048) | 五个月前曾自觉失败，作者分享状态好转的近况并感谢 HN 帮助。 | 564 | 213 | 2022-06-13 |
| 6 | [Tell HN: Brother printers now locking out non-OEM paraphernalia](https://news.ycombinator.com/item?id=31860131) | 发帖者称 Brother 打印机开始限制非原厂耗材，担忧购买时的预期落空。 | 500 | 294 | 2022-06-24 |
| 7 | [Ask HN: Anyone else quickly losing confidence in Amazon?](https://news.ycombinator.com/item?id=31624401) | 假货、虚假评论和低质量商品是否让你逐渐失去对 Amazon 的信任？ | 492 | 315 | 2022-06-04 |
| 8 | [Tell HN: Google does not list application permissions in the Play Store any more](https://news.ycombinator.com/item?id=31698148) | 发帖者反映 Google Play 不再列出应用权限，关注商店隐私信息变化。 | 471 | 167 | 2022-06-10 |
| 9 | [Ask HN: What's the coolest website you know?](https://news.ycombinator.com/item?id=31708366) | 你知道的最酷网站是什么，由读者自行定义“酷”并分享发现。 | 450 | 375 | 2022-06-11 |
| 10 | [Ask HN: If Kubernetes is the solution, why are there so many DevOps jobs?](https://news.ycombinator.com/item?id=31580763) | Kubernetes 既然解决运维问题，为什么市场仍需要如此多的 DevOps 岗位？ | 437 | 416 | 2022-06-01 |

### 2022-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What are some cool but obscure data structures you know about?](https://news.ycombinator.com/item?id=32186203) | 征集有趣却鲜为人知的数据结构及其用途。 | 2051 | 753 | 2022-07-21 |
| 2 | [HN is up again](https://news.ycombinator.com/item?id=32026571) | Hacker News 恢复上线。 | 1010 | 366 | 2022-07-08 |
| 3 | [Tell HN: You can't hire because you don't post salary ranges](https://news.ycombinator.com/item?id=32181619) | 求职者认为不公布薪资范围会阻碍招聘并浪费面试时间。 | 1010 | 523 | 2022-07-21 |
| 4 | [Ask HN: YouTube Channels for the Intellectually Curious](https://news.ycombinator.com/item?id=32220192) | 求知欲旺盛的观众该看哪些 YouTube 频道，才能持续发现有趣知识？ | 759 | 316 | 2022-07-25 |
| 5 | [Tell HN: Internet Archive is facing a Big 4 Publishers lawsuit](https://news.ycombinator.com/item?id=32141358) | 发帖者提醒互联网档案馆面临四大出版商诉讼，呼吁关注其文化价值。 | 746 | 216 | 2022-07-18 |
| 6 | [Tell HN: We are trying to get tail calls into the WebAssembly standard](https://news.ycombinator.com/item?id=32069418) | 开发者介绍推动 WebAssembly 支持尾调用的工作及标准化尝试。 | 625 | 290 | 2022-07-12 |
| 7 | [Tell HN: I have the perfect job, why is it not enough?](https://news.ycombinator.com/item?id=32059666) | 一周工作四天且收入、家庭都不错，为什么“完美工作”仍无法令人满足？ | 463 | 312 | 2022-07-11 |
| 8 | [Ask HN: I love programming but hate the industry. Can anyone relate?](https://news.ycombinator.com/item?id=32136733) | 喜欢写程序，却厌恶软件行业的工作方式，还有谁也有这种矛盾感受？ | 453 | 328 | 2022-07-18 |
| 9 | [Tell HN: Razorpay a YC company shared donor data under a Section 91 order](https://news.ycombinator.com/item?id=31999714) | 发帖者称 Razorpay 依据警方命令提供捐款者数据，关注支付平台与隐私。 | 418 | 281 | 2022-07-06 |
| 10 | [Ask HN: How to keep my daughter busy while tickling her curiosity](https://news.ycombinator.com/item?id=31965616) | 假期如何陪十一岁女儿做有趣活动，既打发时间又激发好奇心？ | 407 | 215 | 2022-07-03 |

### 2022-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Google Cloud suspended our production projects at 1am on Saturday](https://news.ycombinator.com/item?id=32547912) | 用户称已付清账单，谷歌云仍因计费问题在周六凌晨停掉生产项目。 | 1313 | 508 | 2022-08-22 |
| 2 | [GraphQL kinda sucks](https://news.ycombinator.com/item?id=32366759) | 发帖者吐槽 GraphQL 被过度吹捧，讨论实际开发中的落差与不便。 | 720 | 433 | 2022-08-06 |
| 3 | [Tell HN: Godaddy canceled my domain, gave me 2h to respond, then charged €150](https://news.ycombinator.com/item?id=32470017) | 发帖者称 GoDaddy 取消域名、仅给两小时回复并收取额外费用。 | 603 | 302 | 2022-08-15 |
| 4 | [Ask HN: In 2022, what is the proper way to get into machine/deep learning?](https://news.ycombinator.com/item?id=32480009) | 2022 年想进入机器学习研究，怎样安排从基础到科研的学习路线？ | 539 | 203 | 2022-08-16 |
| 5 | [Tell HN: I interviewed my dad before he died](https://news.ycombinator.com/item?id=32349006) | 父亲病重时，作者通过访谈保存他的故事，分享趁还能交流时记录亲人的经历。 | 513 | 156 | 2022-08-04 |
| 6 | [Ask HN: What's the next big thing that few people are talking about?](https://news.ycombinator.com/item?id=32378695) | 除了热门的区块链和 AI，还有哪些少有人谈论的方向可能成为下一件大事？ | 495 | 1174 | 2022-08-07 |
| 7 | [Ask HN: Anyone else feels the commoditization of real estate is unethical?](https://news.ycombinator.com/item?id=32448825) | 房产越来越被当作投资商品，发帖者质疑这种趋势是否符合伦理。 | 488 | 731 | 2022-08-13 |
| 8 | [Ask HN: Who is hiring? (August 2022)](https://news.ycombinator.com/item?id=32306920) | 2022 年 8 月招聘集中帖，汇集企业岗位与远程、实习等信息。 | 446 | 745 | 2022-08-01 |
| 9 | [Coding as a greybeard](https://news.ycombinator.com/item?id=32317441) | 采访五十一岁的程序员兼创始人，聊年龄增长后的编程与创业经历。 | 395 | 339 | 2022-08-02 |
| 10 | [Chrome allows websites to write to the clipboard without the user’s permission](https://news.ycombinator.com/item?id=32614037) | 发帖者给出复现步骤，称 Chromium 网站可未经用户许可写入剪贴板。 | 386 | 185 | 2022-08-26 |

### 2022-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Stripe has decided to nuke my entire business](https://news.ycombinator.com/item?id=32854528) | 创业者称 Stripe 无明确解释停用客户收款账号，危及整个业务。 | 1624 | 678 | 2022-09-15 |
| 2 | [Tell HN: The Internet situation inside Iran](https://news.ycombinator.com/item?id=33025954) | 伊朗用户描述抗议期间网络被切断或限制、难以连接境外服务的处境。 | 1045 | 183 | 2022-09-29 |
| 3 | [Ask HN: Why is Microsoft Teams still so bad?](https://news.ycombinator.com/item?id=32932137) | 频繁崩溃和音频切换故障让人困扰，Microsoft Teams 为何迟迟难用？ | 862 | 793 | 2022-09-21 |
| 4 | [Tell HN: Somebody implemented something I wrote a blog about](https://news.ycombinator.com/item?id=32911299) | 作者博客提出的双因素认证改进被他人实现，分享想法变成产品的欣喜。 | 852 | 241 | 2022-09-20 |
| 5 | [Ask HN: What are some of the best documentaries you've seen?](https://news.ycombinator.com/item?id=32799789) | 近几年出现了哪些好纪录片，征集让人印象深刻、值得观看的作品。 | 650 | 555 | 2022-09-11 |
| 6 | [I accidentally started a movement – Policing the Police by scraping court data](https://news.ycombinator.com/item?id=32902945) | 作者回顾抓取法院数据监督警方的尝试，称一次发帖意外带动了更多行动。 | 650 | 183 | 2022-09-19 |
| 7 | [Tell HN: Otter.ai bot recording meetings without consent](https://news.ycombinator.com/item?id=32751071) | 发帖者称 Otter.ai 更新后未经明确同意加入并录制会议，表达隐私担忧。 | 612 | 176 | 2022-09-07 |
| 8 | [Ask HN: Inherited the worst code and tech team I have ever seen. How to fix it?](https://news.ycombinator.com/item?id=32883596) | 接手极差的代码和团队，却没有直接管理权，该如何制定改善策略？ | 557 | 676 | 2022-09-18 |
| 9 | [Ask HN: Have you experienced “hiring fraud?”](https://news.ycombinator.com/item?id=32996457) | 招聘时遇到身份或能力与面试表现不符的情况，你经历过类似欺诈吗？ | 441 | 546 | 2022-09-27 |
| 10 | [Ask HN: Which books do you consider real gems in your field of work/study?](https://news.ycombinator.com/item?id=32790064) | 你的专业领域有哪些真正的宝藏书，能在合适时机让理解跃上新层次？ | 438 | 262 | 2022-09-10 |

### 2022-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: A disabled 40-year-old person founded a startup and makes a living](https://news.ycombinator.com/item?id=33062606) | 越南创业者讲述身有残疾、四十岁创办公司并靠产品维生的经历。 | 775 | 151 | 2022-10-03 |
| 2 | [Ask HN: Am I getting older or did typing on the iPhone become unbearable?](https://news.ycombinator.com/item?id=33256168) | 多年使用 iPhone 后觉得打字越来越难受，是年龄变化还是键盘体验变差？ | 496 | 407 | 2022-10-19 |
| 3 | [Ask HN: Has anyone managed to find enjoyment in their work after burnout?](https://news.ycombinator.com/item?id=33260525) | 倦怠之后还能重新喜欢工作吗，发帖者寻找恢复兴趣的亲身案例。 | 473 | 355 | 2022-10-19 |
| 4 | [Ask HN: Why don't I see gold at the end of the remote working rainbow?](https://news.ycombinator.com/item?id=33259351) | 远程工作为何没有带来想象中的幸福，发帖者提出与主流赞美不同的感受。 | 468 | 787 | 2022-10-19 |
| 5 | [Lowest “Who is hiring?” Post Count in 30 Months](https://news.ycombinator.com/item?id=33083279) | 发帖者比较招聘帖数量，指出 2022 年 10 月达到三十个月来的低点。 | 461 | 310 | 2022-10-04 |
| 6 | [Tell HN: Beware 'Ungrowth' in Your Job](https://news.ycombinator.com/item?id=33246841) | 工作可能让能力倒退而非成长，发帖者以不被上司理解的经历提出提醒。 | 454 | 285 | 2022-10-18 |
| 7 | [Ask HN: So you moved off Heroku, where did you go?](https://news.ycombinator.com/item?id=33077118) | 从 Heroku 迁走后去了哪里，征集替代平台及迁移后的真实体验。 | 410 | 316 | 2022-10-04 |
| 8 | [I asked Signal motivations for SMS removal](https://news.ycombinator.com/item?id=33258684) | 发帖者公开 Signal 对移除短信功能的回复，追问产品决策背后的动机。 | 379 | 251 | 2022-10-19 |
| 9 | [Ask HN: How did you stop drinking?](https://news.ycombinator.com/item?id=33158947) | 喜欢喝酒时的感觉却讨厌其后果，你是怎样成功戒酒的？ | 378 | 584 | 2022-10-11 |
| 10 | [Ask HN: Is Anyone Else Tired of the Self Enforced Limits on AI Tech?](https://news.ycombinator.com/item?id=33306168) | 开发者限制 AI 模型与技术发布，发帖者质疑这些自我约束是否过多。 | 376 | 403 | 2022-10-23 |

### 2022-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Monumental (if correct) advance in number theory posted to ArXiv by Yitang Zhang](https://news.ycombinator.com/item?id=33512338) | 张益唐发布涉及朗道—西格尔零点的新结果，其正确性仍待验证。 | 1303 | 417 | 2022-11-07 |
| 2 | [Ask HN: Comment here about whatever you're passionate about at the moment](https://news.ycombinator.com/item?id=33488891) | 重温早期互联网的交流感，邀请大家聊聊此刻最热爱的事。 | 982 | 753 | 2022-11-06 |
| 3 | [Tell HN: A hacker's life is in danger, your awareness may be life saving](https://news.ycombinator.com/item?id=33484185) | 帖子呼吁关注被伊朗拘押的技术人士 Jadi，担忧其人身安全。 | 957 | 103 | 2022-11-05 |
| 4 | [Ask HN: Do you recall any book or course that made a topic finally click?](https://news.ycombinator.com/item?id=33593631) | 哪本书、哪门课或哪次解释，让一个久未理解的主题终于豁然开朗？ | 804 | 503 | 2022-11-14 |
| 5 | [Ask HN: What is the most impactful thing you've built?](https://news.ycombinator.com/item?id=33659852) | 你做过最有影响的东西是什么，邀请分享作品如何改变真实工作与生活。 | 729 | 737 | 2022-11-18 |
| 6 | [Tell HN: Happy Thanksgiving](https://news.ycombinator.com/item?id=33732913) | 感恩节社区致意，发帖者感谢 HN 带来的知识与交流。 | 702 | 122 | 2022-11-24 |
| 7 | [Ask HN: Azure has run out of compute – anyone else affected?](https://news.ycombinator.com/item?id=33743567) | 申请 Azure 数据库时被告知资源不足，还有哪些用户受到算力短缺影响？ | 651 | 341 | 2022-11-25 |
| 8 | [Ask HN: Why isn't remote work advertised as a pro environment initiative?](https://news.ycombinator.com/item?id=33690719) | 远程办公减少通勤能耗，为何企业不把它当作环保行动来推广？ | 572 | 487 | 2022-11-21 |
| 9 | [Ask HN: What is the thing you've built that you regret the most?](https://news.ycombinator.com/item?id=33675112) | 你最后悔构建过什么东西，从技术成果的负面影响反思工程选择。 | 502 | 520 | 2022-11-19 |
| 10 | [Ask HN: Alternative ways to make money with coding and system skills?](https://news.ycombinator.com/item?id=33619650) | 不想回到会议繁多的企业岗位，怎样靠编程与系统技能另寻收入来源？ | 496 | 282 | 2022-11-16 |

### 2022-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Merry Christmas, HN](https://news.ycombinator.com/item?id=34121082) | HN 用户送上圣诞祝福，并鼓励感到孤独的人联系关心自己的人。 | 1659 | 221 | 2022-12-24 |
| 2 | [I am done. I give up](https://news.ycombinator.com/item?id=34103896) | 经历三次创业失败的用户表达放弃创业梦想的疲惫与失落。 | 1237 | 972 | 2022-12-23 |
| 3 | [Ask HN: Has anyone here turned around their life in their 40s?](https://news.ycombinator.com/item?id=34052201) | 陷入人生低谷的用户询问四十多岁后是否仍能改变生活。 | 1127 | 726 | 2022-12-19 |
| 4 | [Ask HN: Anyone tired of everything being a subscription now?](https://news.ycombinator.com/item?id=34041962) | 越来越多产品改成订阅收费，是否也让你感到疲惫与不满？ | 931 | 694 | 2022-12-18 |
| 5 | [Ask HN: Developer abused “sign in with GitHub” and users are being punished](https://news.ycombinator.com/item?id=33917962) | 发帖者称第三方滥用 GitHub 登录，导致授权用户反而遭受账号处罚。 | 860 | 480 | 2022-12-09 |
| 6 | [Tell HN: IPv6-only still pretty much unusable](https://news.ycombinator.com/item?id=33894933) | 尝试只用 IPv6 后频遇兼容障碍，发帖者分享现实网络仍依赖 IPv4 的困扰。 | 686 | 631 | 2022-12-07 |
| 7 | [Warning: HP printers force you into agreement](https://news.ycombinator.com/item?id=33936862) | 发帖者称 HP Smart 要求同意仅用原厂墨水，质疑软件附加的使用条款。 | 682 | 302 | 2022-12-10 |
| 8 | [Ask HN: If I get locked out of everything, please try to help me](https://news.ycombinator.com/item?id=33963269) | 手机即将无法充电，发帖者担忧失去所有账号访问权，提前向社区寻求帮助。 | 659 | 330 | 2022-12-13 |
| 9 | [Tell HN: It's easier and faster to pirate an e-book, than it is to buy it](https://news.ycombinator.com/item?id=34172506) | 想花公司学习预算买电子书却处处受阻，作者吐槽正版购买比盗版更麻烦。 | 615 | 482 | 2022-12-29 |
| 10 | [Ask HN: Why are YC companies breaking hiring laws?](https://news.ycombinator.com/item?id=33970189) | 发现纽约职位未公开薪资范围，发帖者质疑部分 YC 公司是否遵守招聘法规。 | 558 | 348 | 2022-12-13 |

### 2023-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [HN: Thank you for being fast, ad-free and text only](https://news.ycombinator.com/item?id=34505219) | 用户感谢 HN 快速、无广告的文字体验，并建议改善手机样式。 | 1042 | 199 | 2023-01-24 |
| 2 | [Ask HN: Those making $0/month or less on side projects – Show and tell](https://news.ycombinator.com/item?id=34547265) | 邀请副业项目没有收入的开发者展示作品，让社区了解其尝试。 | 934 | 1047 | 2023-01-27 |
| 3 | [Ask HN: What's the best lecture series you've ever seen?](https://news.ycombinator.com/item?id=34591291) | 你看过最好的系列讲座是什么，它为何令人难忘，技术与其他领域均可。 | 777 | 271 | 2023-01-31 |
| 4 | [Tell HN: Sometimes you don't realise how bad something is until you leave](https://news.ycombinator.com/item?id=34455934) | 作者分享离开某种处境后才意识到其伤害的体会，希望帮助相似境遇的人。 | 756 | 214 | 2023-01-20 |
| 5 | [Airbnb removed my negative review](https://news.ycombinator.com/item?id=34219422) | 发帖者称 Airbnb 移除了自己的负面评价，讲述住宿纠纷与评价处理经历。 | 752 | 456 | 2023-01-02 |
| 6 | [Ask HN: Something you’ve done your whole life that you realized is wrong?](https://news.ycombinator.com/item?id=34579175) | 哪些动作或习惯做了一辈子，后来才发现一直做错了？ | 691 | 1832 | 2023-01-30 |
| 7 | [Ask HN: How do you test SQL?](https://news.ycombinator.com/item?id=34602318) | 数据团队该怎样测试 SQL 流水线，征集可采用的工程实践与学习资料。 | 663 | 315 | 2023-01-31 |
| 8 | [Tell HN: It is impossible to disable Google 2FA using backup codes](https://news.ycombinator.com/item?id=34441697) | 发帖者提醒：Google 备用码可能无法用于关闭双因素认证，恢复预案需留意。 | 657 | 337 | 2023-01-19 |
| 9 | [Ask HN: Math books that made you significantly better at math?](https://news.ycombinator.com/item?id=34439828) | 哪些数学书显著提升了你的水平，让你始终珍视其中的教学方式？ | 619 | 317 | 2023-01-19 |
| 10 | [Tell HN: Whole Yandex Git repository leaked](https://news.ycombinator.com/item?id=34525936) | 发帖者报告大规模 Yandex Git 仓库泄露消息，称泄露数据超过四十 GB。 | 602 | 340 | 2023-01-25 |

### 2023-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Firefox Is an awesome browser right now](https://news.ycombinator.com/item?id=34640350) | 用户分享从 Chrome 转用 Firefox 后加载 Gmail 和迁移资料的顺畅体验。 | 1310 | 598 | 2023-02-03 |
| 2 | [Tell HN: DEI initiatives undermine the self esteem of PoC within a company](https://news.ycombinator.com/item?id=34677180) | 一位黑人从业者认为公司 DEI 活动会加重有色人种员工的冒名顶替感。 | 1091 | 832 | 2023-02-06 |
| 3 | [Small SaaS banned by Cloudflare after 4 years of being paying customer](https://news.ycombinator.com/item?id=34639212) | 付费使用四年后，小型 SaaS 创始人称 Cloudflare 突然封禁其服务。 | 730 | 316 | 2023-02-03 |
| 4 | [Tell HN: Do not store any funds in PayPal or use them for anything critical](https://news.ycombinator.com/item?id=34913596) | 发帖者结合遭遇告诫不要把重要资金留在 PayPal，关注账户与资金可控性。 | 703 | 295 | 2023-02-23 |
| 5 | [Ask HN: How do you deal with information and internet addiction?](https://news.ycombinator.com/item?id=34710830) | 信息消费越来越难停下来，如何应对播客、网页等带来的网络成瘾？ | 573 | 208 | 2023-02-08 |
| 6 | [Did anyone else lose their marbles?](https://news.ycombinator.com/item?id=34673949) | 曾经前途光明的创业者感到精神状态失衡，询问是否有人经历过类似低谷。 | 568 | 341 | 2023-02-06 |
| 7 | [Ask HN: Why Did Medium.com “fail"?](https://news.ycombinator.com/item?id=34743772) | Medium 仍在运营，为何却给人“失败”的感觉，讨论平台吸引力的变化。 | 461 | 552 | 2023-02-10 |
| 8 | [Launch HN: Lago (YC S21) – Open-source usage-based billing](https://news.ycombinator.com/item?id=34773442) | Lago 介绍开源计费软件，按订阅、用量、折扣等规则计算账单并生成发票。 | 442 | 141 | 2023-02-13 |
| 9 | [Ask HN: Who is hiring? (February 2023)](https://news.ycombinator.com/item?id=34612353) | 2023 年 2 月招聘集中帖，汇集岗位所在地及远程、签证等条件。 | 434 | 580 | 2023-02-01 |
| 10 | [GitHub to layoff 10% and closing all offices](https://news.ycombinator.com/item?id=34727210) | 发帖者转述消息称 GitHub 将裁员一成并关闭全部办公室。 | 407 | 1 | 2023-02-09 |

### 2023-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Launch HN: Electric Air (YC W23) – Heat pump sold directly to homeowners](https://news.ycombinator.com/item?id=35138319) | Electric Air 介绍直售家庭用户的热泵系统，希望简化购买、融资和安装流程。 | 927 | 789 | 2023-03-13 |
| 2 | [MailChimp blacklists your IP if you open the browser's dev tools](https://news.ycombinator.com/item?id=35235732) | 发帖者怀疑编辑邮件时打开浏览器开发工具，会导致 MailChimp 封锁 IP。 | 645 | 199 | 2023-03-20 |
| 3 | [Ask HN: How are you using GPT to be productive?](https://news.ycombinator.com/item?id=35299071) | 演示之外，GPT 怎样真正帮你提高效率，征集日常工作中的实际用法。 | 629 | 735 | 2023-03-25 |
| 4 | [Launch HN: Pynecone (YC W23) – Web Apps in Pure Python](https://news.ycombinator.com/item?id=35136827) | Pynecone 用纯 Python 构建网页应用，让开发者从小型内部工具做到多页产品。 | 550 | 315 | 2023-03-13 |
| 5 | [Ask HN: What has your personal website/blog done for you?](https://news.ycombinator.com/item?id=35164819) | 个人网站或博客为你带来了什么，是否值得持续建设和写作？ | 513 | 442 | 2023-03-15 |
| 6 | [Launch HN: Play.ht (YC W23) – Generate and clone voices from 20 seconds of audio](https://news.ycombinator.com/item?id=35328698) | Play.ht 展示语音生成与克隆模型，称可用约二十秒音频模仿声音并朗读文本。 | 459 | 458 | 2023-03-27 |
| 7 | [Ask HN: Where can I find a primer on how computers boot?](https://news.ycombinator.com/item?id=35229045) | 遇到 GRUB 问题后发现基础不足，哪里有清楚介绍计算机启动过程的入门资料？ | 457 | 94 | 2023-03-20 |
| 8 | [Ask HN: Who is hiring? (March 2023)](https://news.ycombinator.com/item?id=34983767) | 2023 年 3 月招聘集中帖，企业在此介绍岗位与候选人要求。 | 440 | 629 | 2023-03-01 |
| 9 | [Ask HN: Why do many CS graduates lack foundational knowledge?](https://news.ycombinator.com/item?id=35226887) | 面试应届实习生时发现基础薄弱，发帖者追问计算机教育是否出了问题。 | 386 | 725 | 2023-03-20 |
| 10 | [Launch HN: Vocode (YC W23) – Library for realtime voice conversation with LLMs](https://news.ycombinator.com/item?id=35358873) | Vocode 提供开源语音交互库，协调语音识别、大模型和语音合成来实现实时对话。 | 379 | 116 | 2023-03-29 |

### 2023-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Remembering Bob Lee](https://news.ycombinator.com/item?id=35457341) | HN 用户缅怀技术贡献广泛、乐于分享的工程师 Bob Lee。 | 2090 | 217 | 2023-04-05 |
| 2 | [Ask HN: Most interesting tech you built for just yourself?](https://news.ycombinator.com/item?id=35729232) | 征集大家只为自己打造的有趣技术项目。 | 1901 | 1792 | 2023-04-27 |
| 3 | [iOS lets carriers add WiFi networks that you can’t remove or stop from joining](https://news.ycombinator.com/item?id=35447486) | 发帖者称运营商可向 iOS 添加无法删除或禁止自动连接的 WiFi 网络。 | 1025 | 391 | 2023-04-05 |
| 4 | [Eid Mubarak](https://news.ycombinator.com/item?id=35650200) | 向 HN 的穆斯林读者与其他成员送上开斋节祝福，并介绍节日。 | 815 | 328 | 2023-04-21 |
| 5 | [Tell HN: Cloudflare verification is breaking the internet](https://news.ycombinator.com/item?id=35742606) | 发帖者抱怨 Cloudflare 验证阻挡多个网站访问，影响正常使用互联网。 | 615 | 334 | 2023-04-28 |
| 6 | [Ask HN: Side project of more that $2k monthly revenue what's your project?](https://news.ycombinator.com/item?id=35567822) | 月收入超过两千美元的副项目有哪些，发帖者希望寻找可行的市场方向。 | 530 | 502 | 2023-04-14 |
| 7 | [Launch HN: OutSail (YC W23) – Wingsails to reduce cargo ship fuel consumption](https://news.ycombinator.com/item?id=35426482) | OutSail 介绍可收卷的大型翼帆，尝试让货轮借助风力减少燃油消耗。 | 527 | 269 | 2023-04-03 |
| 8 | [Ask HN: Who is hiring? (April 2023)](https://news.ycombinator.com/item?id=35424807) | 2023 年 4 月招聘集中帖，查看企业职位、所在地及远程工作条件。 | 418 | 573 | 2023-04-03 |
| 9 | [Ask HN: What are some of the best university courses available online for free?](https://news.ycombinator.com/item?id=35536042) | 哪些大学课程可以免费在线学习，且质量高到值得推荐？ | 399 | 90 | 2023-04-12 |
| 10 | [Ask HN: What lesser-known accessories do you use with your computer?](https://news.ycombinator.com/item?id=35429801) | 有哪些少有人知的电脑配件，明显改善了你的工作或使用体验？ | 377 | 835 | 2023-04-03 |

### 2023-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Is it just me or GPT-4's quality has significantly deteriorated lately?](https://news.ycombinator.com/item?id=36134249) | 用户询问 GPT-4 回答是否近期变快却变浅、代码错误也增多。 | 947 | 756 | 2023-05-31 |
| 2 | [Ask HN: What is new in Algorithms / Data Structures these days?](https://news.ycombinator.com/item?id=35886900) | AI 热潮之外，算法与数据结构近年还有哪些值得关注的新进展？ | 737 | 211 | 2023-05-10 |
| 3 | [Ask HN: How do you not take criticism of your work personally?](https://news.ycombinator.com/item?id=36056299) | 工作被提改进意见时总觉得在否定自己，如何把反馈与个人价值分开？ | 667 | 629 | 2023-05-24 |
| 4 | [Ask HN: Can someone ELI5 Transformers and the “Attention is all we need” paper](https://news.ycombinator.com/item?id=35977891) | 没有机器学习基础，怎样通俗理解 Transformer 与注意力机制论文？ | 644 | 228 | 2023-05-17 |
| 5 | [We should start to add “ai.txt” as we do for “robots.txt”](https://news.ycombinator.com/item?id=35886288) | 作者提议像 robots.txt 一样为项目添加 ai.txt，并展示写入相关说明的尝试。 | 562 | 281 | 2023-05-10 |
| 6 | [PSA: Cancelling HP Instant Ink subscription prevents cartridges from being used](https://news.ycombinator.com/item?id=36030156) | 发帖者提醒：取消 HP Instant Ink 订阅后，订阅墨盒可能无法继续使用。 | 517 | 392 | 2023-05-22 |
| 7 | [Ask HN: Where have you found community outside of work?](https://news.ycombinator.com/item?id=36128618) | 工作之外去哪里找到归属感，征集能提供联系和支持的社区经历。 | 478 | 567 | 2023-05-30 |
| 8 | [Launch HN: Common Paper (YC W23) – SAFEs for Commercial Contracts](https://news.ycombinator.com/item?id=36043944) | Common Paper 提供标准化开源商业合同与签约平台，回应创业团队处理合同的烦恼。 | 431 | 167 | 2023-05-23 |
| 9 | [Ask HN: Who is hiring? (May 2023)](https://news.ycombinator.com/item?id=35773707) | 2023 年 5 月招聘集中帖，企业在此发布岗位和招聘要求。 | 370 | 499 | 2023-05-01 |
| 10 | [Ask HN: How do you approach a problem you are not sure has a solution?](https://news.ycombinator.com/item?id=36057997) | 面对甚至不确定有无答案的问题，怎样克服焦虑与行动瘫痪？ | 364 | 294 | 2023-05-24 |

### 2023-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Apollo is dead. Long live Apollo](https://news.ycombinator.com/item?id=36543894) | Apollo 关闭之际，用户感叹其代表的创造力与互联网精神。 | 1036 | 383 | 2023-06-30 |
| 2 | [Reddit.com appears to be having an outage](https://news.ycombinator.com/item?id=36294244) | 发帖者报告 Reddit 加载帖子失败，询问是否发生服务中断。 | 820 | 659 | 2023-06-12 |
| 3 | [AWS us-east-1 down](https://news.ycombinator.com/item?id=36315300) | 发帖者称 AWS us-east-1 出现故障，同时指出状态页仍显示正常。 | 658 | 313 | 2023-06-13 |
| 4 | [Tell HN: My Reddit account was banned after adding my subs to the protest](https://news.ycombinator.com/item?id=36192312) | 发帖者称让所管理的版块参加抗议后，自己的 Reddit 账号遭到封禁。 | 596 | 226 | 2023-06-05 |
| 5 | [Ask HN: Alternatives to Reddit](https://news.ycombinator.com/item?id=36293789) | Reddit 版块停摆让人意识到依赖过深，哪些社区平台可以替代？ | 547 | 377 | 2023-06-12 |
| 6 | [Tell HN: Stripe killed my music locker service, so I'm open sourcing it](https://news.ycombinator.com/item?id=36403607) | 作者称 Stripe 导致音乐存储服务无法继续，决定把项目开源。 | 446 | 172 | 2023-06-20 |
| 7 | [YouTube: Sort by oldest is back baby](https://news.ycombinator.com/item?id=36410777) | 发帖者发现 YouTube 恢复按最早上传排序，分享这一浏览功能的回归。 | 441 | 187 | 2023-06-20 |
| 8 | [Ask HN: Who is hiring? (June 2023)](https://news.ycombinator.com/item?id=36152014) | 2023 年 6 月招聘集中帖，汇集公司岗位及工作安排。 | 394 | 528 | 2023-06-01 |
| 9 | [Ask HN: IP cameras that don't require an app or internet](https://news.ycombinator.com/item?id=36447024) | 寻找无需手机应用和互联网连接的网络摄像头，方便在本地独立使用。 | 389 | 198 | 2023-06-23 |
| 10 | [Ask HN: Why does Apple refuse to add window snapping to macOS?](https://news.ycombinator.com/item?id=36368990) | 2023 年 macOS 仍缺少窗口吸附，发帖者质疑 Apple 的窗口管理取舍。 | 357 | 501 | 2023-06-17 |

### 2023-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Nearly all of Evernote’s remaining staff has been laid off](https://news.ycombinator.com/item?id=36609641) | 用户称 Evernote 几乎全部剩余员工被裁，并质疑涨价后的开发承诺。 | 1025 | 614 | 2023-07-06 |
| 2 | [Ask HN: Could you share your personal blog here?](https://news.ycombinator.com/item?id=36575081) | 邀请 HN 用户分享自己的个人博客。 | 1014 | 1940 | 2023-07-03 |
| 3 | [Ask HN: Is the market bad, or am I having the worst luck job hunting?](https://news.ycombinator.com/item?id=36901303) | 年初被裁后不断投简历仍无进展，是市场低迷还是个人求职运气太差？ | 711 | 1052 | 2023-07-27 |
| 4 | [Is anyone using PyPy for real work?](https://news.ycombinator.com/item?id=36940871) | PyPy 发布负责人征集真实使用案例：有没有人在生产工作中依赖它？ | 573 | 180 | 2023-07-31 |
| 5 | [Confirmed: Twitter switched temporarily to rate limited mode](https://news.ycombinator.com/item?id=36552324) | 帖子转述 Musk 公告，称 Twitter 为应对抓取与操纵临时限制阅读量。 | 561 | 716 | 2023-07-01 |
| 6 | [Ask HN: Any Hardware Startups Here?](https://news.ycombinator.com/item?id=36583419) | 软件创业之外，HN 有哪些团队在做硬件，邀请介绍产品和挑战。 | 509 | 700 | 2023-07-04 |
| 7 | [Ask HN: Who is hiring? (July 2023)](https://news.ycombinator.com/item?id=36573871) | 2023 年 7 月招聘集中帖，可浏览各地公司正在招聘的职位。 | 421 | 444 | 2023-07-03 |
| 8 | [Launch HN: Twenty.com (YC S23) – Open-source CRM](https://news.ycombinator.com/item?id=36791434) | Twenty 团队介绍开源 CRM，希望改善传统客户管理软件的使用体验及与工程团队的协作。 | 415 | 311 | 2023-07-19 |
| 9 | [Ask HN: As people in “tech”, are we inside an AI echo chamber?](https://news.ycombinator.com/item?id=36567918) | 科技圈外有人连 ChatGPT 都没听过，我们是否身处 AI 信息回音室？ | 398 | 730 | 2023-07-03 |
| 10 | [Ask HN: Which recently research paper blow your mind?](https://news.ycombinator.com/item?id=36846965) | 最近哪篇研究论文让你大开眼界，邀请分享令人惊叹的研究。 | 347 | 171 | 2023-07-24 |

### 2023-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: T.co is adding a ~5 second delay to domains they don't like](https://news.ycombinator.com/item?id=37130060) | 发帖者称 Twitter 的短链跳转对部分域名额外延迟约五秒。 | 749 | 421 | 2023-08-15 |
| 2 | [Ask HN: Why Did Python Win?](https://news.ycombinator.com/item?id=37308747) | Python 为何取得如此广泛的成功，讨论语言流行背后的历史与条件。 | 578 | 828 | 2023-08-29 |
| 3 | [Tell HN: I think I found Toyota's battery](https://news.ycombinator.com/item?id=36980630) | 看到丰田电池突破新闻后，发帖者提出自己对其技术来源的猜测。 | 529 | 203 | 2023-08-03 |
| 4 | [Ask HN: Where to find open source house plans?](https://news.ycombinator.com/item?id=37234111) | 准备盖房子，哪里能找到可自由使用的开源住宅设计图纸？ | 506 | 251 | 2023-08-23 |
| 5 | [Ask HN: Who is hiring? (August 2023)](https://news.ycombinator.com/item?id=36956867) | 2023 年 8 月招聘集中帖，集中展示企业岗位及候选人要求。 | 479 | 525 | 2023-08-01 |
| 6 | [Ask HN: Any interesting books you have read lately?](https://news.ycombinator.com/item?id=37156372) | 最近读到了哪些有趣的书，欢迎分享小说与其他领域的新发现。 | 439 | 520 | 2023-08-17 |
| 7 | [Ask HN: What's the coolest physical thing you've made?](https://news.ycombinator.com/item?id=37033652) | 程序之外，你亲手做过最酷的实体作品是什么，绘画和造船都欢迎。 | 377 | 669 | 2023-08-07 |
| 8 | [Launch HN: Refine (YC S23) – Open-Source Retool for Enterprise](https://news.ycombinator.com/item?id=37064822) | Refine 介绍开源企业应用开发平台，用来快速搭建管理后台、仪表盘和业务门户。 | 259 | 92 | 2023-08-09 |
| 9 | [Ask HN: My mother is slowly looking her eyesight, how to prepare?](https://news.ycombinator.com/item?id=37293002) | 母亲视力逐渐衰退，家人该如何提前准备生活工具与适应方案？ | 249 | 130 | 2023-08-28 |
| 10 | [Launch HN: Tiptap (YC S23) – Toolkit for developing collaborative editors](https://news.ycombinator.com/item?id=36957204) | Tiptap 介绍协作编辑工具包，帮助开发者构建类似 Notion 或 Google Docs 的编辑界面。 | 246 | 103 | 2023-08-01 |

### 2023-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: I’m an FCC Commissioner proposing regulation of IoT security updates](https://news.ycombinator.com/item?id=37392676) | FCC 委员征询社区意见，讨论如何监管物联网设备安全更新。 | 3387 | 925 | 2023-09-05 |
| 2 | [PSA: Don't base your business around Discord.7yr account banned for posting ASNs](https://news.ycombinator.com/item?id=37364605) | 发帖者称七年 Discord 账号因发布 ASN 被封，提醒创业者谨慎依赖单一平台。 | 502 | 170 | 2023-09-02 |
| 3 | [Ask HN: Why did Visual Basic die?](https://news.ycombinator.com/item?id=37470318) | 曾经风靡的 Visual Basic 为何衰落，老开发者回顾语言与行业变化。 | 420 | 522 | 2023-09-11 |
| 4 | [Ask HN: Who is hiring? (September 2023)](https://news.ycombinator.com/item?id=37351667) | 2023 年 9 月招聘集中帖，企业集中发布职位、地点和工作条件。 | 397 | 494 | 2023-09-01 |
| 5 | [Tell HN: ChatGPT cut off date now Jan 2022](https://news.ycombinator.com/item?id=37564686) | 发帖者观察到 ChatGPT 自述知识截止时间变为 2022 年 1 月。 | 330 | 209 | 2023-09-19 |
| 6 | [Tell HN: Enterprises spend 10x more to build no-code solutions than coded ones](https://news.ycombinator.com/item?id=37689282) | 作者主张企业无代码项目可能比写代码更贵，质疑宣传中的成本优势。 | 326 | 188 | 2023-09-28 |
| 7 | [Ask HN: What is your policy regarding smartphones in your children?](https://news.ycombinator.com/item?id=37347657) | 家长如何决定孩子何时拥有手机、怎样使用，征集家庭的具体规则。 | 325 | 387 | 2023-09-01 |
| 8 | [Tell HN: Please don't print –help to stderr in your CLI tools](https://news.ycombinator.com/item?id=37682859) | 作者建议命令行工具把帮助输出写到标准输出，方便通过管道分页查看。 | 299 | 147 | 2023-09-27 |
| 9 | [Ask HN: How to do literal web searches after Google destroyed the “ ” feature?](https://news.ycombinator.com/item?id=37554736) | Google 引号搜索不再满足需求，怎样才能精确搜索字面文本？ | 280 | 208 | 2023-09-18 |
| 10 | [Ask HN: Why does Google rank the real Python documentation below content farms?](https://news.ycombinator.com/item?id=37482216) | 搜索 Python 方法时内容农场排在官方文档之前，发帖者质疑搜索排序。 | 274 | 142 | 2023-09-12 |

### 2023-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who is hiring? (October 2023)](https://news.ycombinator.com/item?id=37739028) | 2023 年 10 月招聘集中帖，汇集正在招人的企业与岗位。 | 475 | 638 | 2023-10-02 |
| 2 | [Tell HN: 3G sunsetting is killing every Subaru Outback battery](https://news.ycombinator.com/item?id=37971038) | 发帖者怀疑 3G 退网使 Subaru 车载联网设备反复尝试连接并耗尽电瓶。 | 454 | 215 | 2023-10-21 |
| 3 | [Ask HN: PG's 'Do Things That Don't Scale' Manual Examples](https://news.ycombinator.com/item?id=38010992) | “做无法规模化的事”有哪些手工实践案例，寻找创业早期人工验证的办法。 | 412 | 316 | 2023-10-25 |
| 4 | [Launch HN: Radical (YC W23) – Autonomous high-altitude solar aircraft](https://news.ycombinator.com/item?id=37901120) | Radical 展示面向平流层持续飞行的太阳能无人机，介绍原型与设计目标。 | 402 | 201 | 2023-10-16 |
| 5 | [Automatic fraud detection is making my life hell](https://news.ycombinator.com/item?id=38038713) | 为照顾家人在印度停留期间，发帖者称自动反欺诈系统屡次阻碍正常生活。 | 402 | 388 | 2023-10-27 |
| 6 | [Ask HN: Show me your half baked project](https://news.ycombinator.com/item?id=37857231) | 邀请展示还没打磨好的项目，让半成品提前得到交流与反馈。 | 395 | 687 | 2023-10-12 |
| 7 | [Ask HN: Has anyone gotten complete, permanent relief from tinnitus?](https://news.ycombinator.com/item?id=37852711) | 有人彻底且长期摆脱过耳鸣吗，发帖者寻找真实的改善与康复经验。 | 382 | 389 | 2023-10-12 |
| 8 | [Tell HN: Postman update removes all your stuff if you refuse to create account](https://news.ycombinator.com/item?id=37792690) | 离线用户称 Postman 更新要求建账号，否则原有内容无法继续访问。 | 365 | 173 | 2023-10-06 |
| 9 | [20% of LinkedIn's recent layoffs were managers](https://news.ycombinator.com/item?id=37907433) | 发帖者关注 LinkedIn 裁员中的管理者比例，询问是否高于通常水平。 | 280 | 280 | 2023-10-16 |
| 10 | [Ask HN: Who wants to be hired? (October 2023)](https://news.ycombinator.com/item?id=37739026) | 2023 年 10 月求职自荐帖，展示个人技能、所在地与工作意向。 | 235 | 491 | 2023-10-02 |

### 2023-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Three senior researchers have resigned from OpenAI](https://news.ycombinator.com/item?id=38316378) | 帖子报告三名 OpenAI 资深研究人员离职，包括研究主管与风险团队负责人。 | 879 | 672 | 2023-11-18 |
| 2 | [Ask HN: What was the outcome of Reddit blackout?](https://news.ycombinator.com/item?id=38423167) | Reddit 版块集体停摆抗议最终带来了什么，平台有没有作出妥协？ | 507 | 453 | 2023-11-26 |
| 3 | [Ask HN: Who is hiring? (November 2023)](https://news.ycombinator.com/item?id=38099086) | 2023 年 11 月招聘集中帖，可查看企业需求及各类职位机会。 | 494 | 595 | 2023-11-01 |
| 4 | [Tell HN: Submit comments on IRS guidance to SEC 174 expenses](https://news.ycombinator.com/item?id=38120388) | 帖子呼吁就美国税法第 174 条研发费用摊销指引提交公众意见。 | 461 | 225 | 2023-11-02 |
| 5 | [Ask HN: Comment here about whatever you're passionate about at the moment](https://news.ycombinator.com/item?id=38161369) | 延续去年的开放话题帖，聊聊你此刻真正热爱的事情。 | 370 | 842 | 2023-11-06 |
| 6 | [Ask HN: How should I setup a phone for a newly blind relative?](https://news.ycombinator.com/item?id=38406156) | 家中长辈刚刚失明，如何配置手机，让他能更容易独立沟通和使用？ | 319 | 76 | 2023-11-24 |
| 7 | [Tell HN: How you changed my life trajectory](https://news.ycombinator.com/item?id=38291452) | 作者分享 HN 如何改变自己的人生方向，感谢社区讨论带来的影响。 | 270 | 55 | 2023-11-16 |
| 8 | [Ask HN: Is Knuth's TAOCP worth the time and effort? (2023)](https://news.ycombinator.com/item?id=38443668) | 开始读《计算机程序设计艺术》后遇到证明难题，这套书值得投入多少精力？ | 255 | 182 | 2023-11-28 |
| 9 | [Ask HN: Any comprehensive courses on Auth?](https://news.ycombinator.com/item?id=38331501) | 从密码到 OAuth、目录服务和安全密钥，哪里有系统全面的认证课程？ | 242 | 90 | 2023-11-19 |
| 10 | [I'm Peter Roberts, immigration attorney who does work for YC and startups. AMA](https://news.ycombinator.com/item?id=38207307) | Peter Roberts 移民律师开放问答，由社区问题决定本次讨论方向。 | 224 | 298 | 2023-11-09 |

### 2023-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Happy New Year HN!](https://news.ycombinator.com/item?id=38826283) | HN 用户祝社区成员在 2024 年新年快乐。 | 1393 | 265 | 2023-12-31 |
| 2 | [Tell HN: I salute everyone on call/working support through the holidays](https://news.ycombinator.com/item?id=38725015) | 向假日期间值班与提供支持的人致意，感谢他们维护系统安全和可用。 | 916 | 189 | 2023-12-21 |
| 3 | [Ask HN: How do I train a custom LLM/ChatGPT on my own documents in Dec 2023?](https://news.ycombinator.com/item?id=38759877) | 2023 年底想让模型使用自己的文档，训练或接入知识该选择什么方案？ | 800 | 237 | 2023-12-25 |
| 4 | [Tell HN: Merry Christmas](https://news.ycombinator.com/item?id=38759092) | HN 社区圣诞问候帖，向节日期间的读者送上祝福。 | 762 | 263 | 2023-12-25 |
| 5 | [Ask HN: What side projects landed you a job?](https://news.ycombinator.com/item?id=38511280) | 哪些副项目帮助你拿到工作，邀请分享作品与求职机会之间的联系。 | 576 | 519 | 2023-12-03 |
| 6 | [Ask HN: What are good books/blogs to read for a first time CTO?](https://news.ycombinator.com/item?id=38803092) | 第一次出任创业公司 CTO，哪些书和博客最值得提前阅读？ | 523 | 142 | 2023-12-29 |
| 7 | [Ask HN: Who is hiring? (December 2023)](https://news.ycombinator.com/item?id=38490811) | 2023 年 12 月招聘集中帖，汇集年末岗位与工作条件。 | 502 | 501 | 2023-12-01 |
| 8 | [Microsoft.com added 192.168.1.1 to their DNS record](https://news.ycombinator.com/item?id=38702783) | 发帖者发现 microsoft.com 的 DNS 解析包含内网地址 192.168.1.1，询问影响。 | 498 | 133 | 2023-12-19 |
| 9 | [Ask HN: What's your "it's not stupid if it works" story?](https://news.ycombinator.com/item?id=38733282) | 有什么看似荒唐却有效的技术做法，分享“管用就不算傻”的巧妙补救。 | 441 | 499 | 2023-12-22 |
| 10 | [Ask HN: Who needs help this holidays?](https://news.ycombinator.com/item?id=38492378) | 假期里谁需要帮助，社区互助帖邀请困难中的读者提出需求。 | 398 | 205 | 2023-12-01 |

### 2024-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who else is working on nothing?](https://news.ycombinator.com/item?id=38983067) | 大家都在忙着学习和构建新东西，还有谁此刻什么项目也没做？ | 704 | 277 | 2024-01-13 |
| 2 | [Tell HN: Bash.org is no more](https://news.ycombinator.com/item?id=38950721) | 发帖者报告 IRC 趣味语录网站 Bash.org 关闭，怀念旧互联网的一角。 | 575 | 331 | 2024-01-11 |
| 3 | [Tell HN: Hacker News now supports IPv6](https://news.ycombinator.com/item?id=39099065) | 发帖者发现浏览器已通过 IPv6 连接 Hacker News，分享站点网络支持变化。 | 555 | 374 | 2024-01-23 |
| 4 | [Tell HN: Russia has started blocking OpenVPN/WireGuard connections](https://news.ycombinator.com/item?id=39067213) | 发帖者称俄罗斯开始阻断 OpenVPN 和 WireGuard 连接，影响当地 VPN 使用。 | 439 | 234 | 2024-01-20 |
| 5 | [Ask HN: Who is hiring? (January 2024)](https://news.ycombinator.com/item?id=38842977) | 2024 年 1 月招聘集中帖，企业集中展示新年岗位和招聘要求。 | 405 | 480 | 2024-01-02 |
| 6 | [Ask HN: 9-yo son wants to build a game, I'm lost. What can I do?](https://news.ycombinator.com/item?id=39035650) | 九岁儿子突然想做游戏，家长不知如何支持，向社区寻找起步办法。 | 387 | 378 | 2024-01-18 |
| 7 | [Ask HN: Any felons successfully found IT work post-release?](https://news.ycombinator.com/item?id=38858075) | 有重罪记录的人出狱后还能进入 IT 行业吗，征集重新就业的亲历经验。 | 355 | 374 | 2024-01-03 |
| 8 | [Ask HN: Good book to learn modern networking?](https://news.ycombinator.com/item?id=38918418) | 2024 年学习现代网络，哪些书能兼顾套接字基础与当代技术？ | 326 | 131 | 2024-01-08 |
| 9 | [Ask HN: Where can I find good legal documents?](https://news.ycombinator.com/item?id=39012544) | 新建副项目总要准备条款和隐私政策，哪里能找到合适的法律文档？ | 319 | 79 | 2024-01-16 |
| 10 | [Ask HN: Does Cloudflare block HN comments if you have code blocks in a reply?](https://news.ycombinator.com/item?id=38986187) | 发帖者提交含代码的 HN 评论时被 Cloudflare 拦截，询问是否与代码块有关。 | 311 | 143 | 2024-01-14 |

### 2024-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Did you encounter any leap year bugs today?](https://news.ycombinator.com/item?id=39554539) | 闰日触发账单系统错误，发帖者询问大家今天还遇到了哪些闰年漏洞。 | 524 | 481 | 2024-02-29 |
| 2 | [Ask HN: Slow thinkers, how do you compensate for your lack of quick-wittedness?](https://news.ycombinator.com/item?id=39522734) | 反应不够快的人，如何发挥慢思考优势并应对需要即兴应答的场合？ | 427 | 269 | 2024-02-27 |
| 3 | [Ask HN: Who is hiring? (February 2024)](https://news.ycombinator.com/item?id=39217310) | 2024 年 2 月招聘集中帖，查看公司岗位与远程、签证等信息。 | 418 | 535 | 2024-02-01 |
| 4 | [Ask HN: What have you built with LLMs?](https://news.ycombinator.com/item?id=39263664) | 你已经用大语言模型做出了什么，邀请展示真实项目与具体用途。 | 372 | 333 | 2024-02-05 |
| 5 | [Ask HN: How many of you are self employed?](https://news.ycombinator.com/item?id=39259602) | 有多少读者靠自己经营的业务谋生，讨论创业融资之外的自雇方式。 | 364 | 438 | 2024-02-05 |
| 6 | [Launch HN: Retell AI (YC W24) – Conversational Speech API for Your LLM](https://news.ycombinator.com/item?id=39453402) | Retell AI 介绍对话语音 API，让大语言模型接入语音交流能力。 | 350 | 173 | 2024-02-21 |
| 7 | [Ask HN: What are the best articles on managing people?](https://news.ycombinator.com/item?id=39336840) | 哪些文章真正帮助你学会管理团队和与人共事，征集管理阅读推荐。 | 311 | 153 | 2024-02-11 |
| 8 | [Ask HN: Nitter officially declared "over" today – alternatives?](https://news.ycombinator.com/item?id=39382590) | Nitter 宣告结束后，还能用什么替代方式浏览 Twitter 内容？ | 300 | 328 | 2024-02-15 |
| 9 | [Launch HN: Danswer (YC W24) – Open-source AI search and chat over private data](https://news.ycombinator.com/item?id=39467413) | Danswer 团队介绍开源 AI 搜索与聊天工具，用于查询私有数据。 | 231 | 129 | 2024-02-22 |
| 10 | [Tell HN: Equifax free credit report dark patterns](https://news.ycombinator.com/item?id=39485259) | 发帖者结合申请免费信用报告的经历，质疑 Equifax 的界面诱导做法。 | 223 | 105 | 2024-02-23 |

### 2024-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Launch HN: Aqua Voice (YC W24) – Voice-driven text editor](https://news.ycombinator.com/item?id=39828686) | Aqua Voice 展示通过语音编辑文档的工具，尝试让说话成为主要输入方式。 | 716 | 244 | 2024-03-26 |
| 2 | [Ask HN: Do you also marvel at the complexity of everyday objects?](https://news.ycombinator.com/item?id=39740518) | 一卷普通电线也包含复杂工艺，你是否也常惊叹日用品背后的技术？ | 479 | 319 | 2024-03-18 |
| 3 | [Tell HN: Reddit now blocks VPN access via browser, 'old' subdomain included](https://news.ycombinator.com/item?id=39883747) | 发帖者称使用 VPN 时 Reddit 网页无法访问，旧版子域名也受影响。 | 393 | 322 | 2024-03-31 |
| 4 | [Ask HN: Who is hiring? (March 2024)](https://news.ycombinator.com/item?id=39562986) | 2024 年 3 月招聘集中帖，查看企业岗位与候选人要求。 | 368 | 482 | 2024-03-01 |
| 5 | [Ask HN: What non-AI products are you working on?](https://news.ycombinator.com/item?id=39829695) | AI 产品发布铺天盖地，还有谁在做不依赖 AI 的产品，邀请展示。 | 365 | 526 | 2024-03-26 |
| 6 | [Ask HN: What things are happening in ML that we can't hear over the din of LLMs?](https://news.ycombinator.com/item?id=39848847) | 大语言模型吸走关注后，机器学习其他方向还有哪些令人兴奋的进展？ | 364 | 99 | 2024-03-28 |
| 7 | [Ask HN: How can I learn about performance optimization?](https://news.ycombinator.com/item?id=39564632) | 想掌握性能优化，该从哪些资源入门并建立分析瓶颈的能力？ | 335 | 147 | 2024-03-01 |
| 8 | [Launch HN: Greptile (YC W24) - RAG on codebases that actually works](https://news.ycombinator.com/item?id=39604961) | Greptile 介绍面向复杂代码库的检索问答工具，试图提高代码问题的回答准确度。 | 253 | 166 | 2024-03-05 |
| 9 | [Scammed by the top result for 'Bitcoin wallet' in Apple App Store](https://news.ycombinator.com/item?id=39685272) | 发帖者称下载 Apple 商店搜索排名靠前的比特币钱包后受骗。 | 242 | 150 | 2024-03-12 |
| 10 | [Ask HN: How to onboard yourself to a new product/industry in a new job?](https://news.ycombinator.com/item?id=39777223) | 刚加入陌生行业，工程师该怎样主动补齐产品、业务与领域知识？ | 216 | 77 | 2024-03-21 |

### 2024-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What is the most useless project you have worked on?](https://news.ycombinator.com/item?id=39942397) | 你参与过最没用的项目是什么，邀请分享努力最终未产生价值的经历。 | 760 | 767 | 2024-04-05 |
| 2 | [3D + 2D: Testing out my cross-platform WASM graphics engine](https://news.ycombinator.com/item?id=39907845) | 跨平台 WASM 图形引擎正在测试，作者把二维与三维效果放在一起展示。 | 579 | 152 | 2024-04-02 |
| 3 | [Tell HN: Ever think of applying to YC? Do it this weekend for S24](https://news.ycombinator.com/item?id=40091622) | 帖子提醒 YC S24 申请期限，鼓励有意创业的读者利用周末提交申请。 | 382 | 420 | 2024-04-19 |
| 4 | [Ask HN: Who is hiring? (April 2024)](https://news.ycombinator.com/item?id=39894820) | 2024 年 4 月招聘集中帖，汇集岗位所在地、远程与签证等条件。 | 377 | 483 | 2024-04-01 |
| 5 | [Tell HN: Bypass Paywalls repository is gone](https://news.ycombinator.com/item?id=40015961) | 发帖者发现 Bypass Paywalls 仓库无法访问，询问项目去向。 | 343 | 125 | 2024-04-12 |
| 6 | [I'm Peter Roberts, immigration attorney who does work for YC and startups. AMA](https://news.ycombinator.com/item?id=40014087) | 移民律师 Peter Roberts 全天开放问答，回应社区关心的移民事务。 | 330 | 407 | 2024-04-12 |
| 7 | [AMA: I'm Dave Greene, an accidental expert on Conway's Game of Life](https://news.ycombinator.com/item?id=40131597) | 生命游戏研究者 Dave Greene 开放问答，分享意外深入这一领域的经历。 | 313 | 151 | 2024-04-23 |
| 8 | [Ask HN: How to manage phones and PCs for elderly parents?](https://news.ycombinator.com/item?id=40127400) | 父母年纪渐长，怎样管理他们的手机和电脑，同时保留独立使用的能力？ | 278 | 370 | 2024-04-23 |
| 9 | [Ask HN: Which books/resources to understand modern Assembler?](https://news.ycombinator.com/item?id=40104823) | 想理解 LLVM、JIT 与底层实现，有哪些学习现代汇编的好书和资源？ | 269 | 91 | 2024-04-21 |
| 10 | [Ask HN: I want to create IMDB for open source projects](https://news.ycombinator.com/item?id=40041954) | 发帖者想做开源项目的 IMDb，探讨如何集中展示与发现开源软件。 | 241 | 142 | 2024-04-15 |

### 2024-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What is your ChatGPT customization prompt?](https://news.ycombinator.com/item?id=40474716) | 你为 ChatGPT 设置了哪些满意的自定义指令，邀请交流提示词设计。 | 694 | 293 | 2024-05-25 |
| 2 | [Ask HN: Who is hiring? (May 2024)](https://news.ycombinator.com/item?id=40224213) | 2024 年 5 月招聘集中帖，企业集中发布岗位与工作安排。 | 549 | 728 | 2024-05-01 |
| 3 | [Ask HN: Video streaming is expensive yet YouTube "seems" to do it for free. How?](https://news.ycombinator.com/item?id=40408515) | 视频编码、存储和分发都很贵，YouTube 看似免费提供服务的经济账怎么算？ | 422 | 368 | 2024-05-19 |
| 4 | [Ask HN: How do people create those sleek looking demos for startups?](https://news.ycombinator.com/item?id=40231790) | 创业公司的流畅演示视频如何制作，寻找镜头缩放与产品展示的工具和方法。 | 395 | 167 | 2024-05-02 |
| 5 | [Ask HN: Interesting TUIs (text user interfaces), maybe forgotten ones?](https://news.ycombinator.com/item?id=40273177) | 有哪些好用或被遗忘的文本界面应用，值得研究其交互设计？ | 322 | 294 | 2024-05-06 |
| 6 | [Make timelapses easily using FFmpeg](https://news.ycombinator.com/item?id=40407526) | 作者分享使用 FFmpeg 制作延时摄影的方法，简化多张照片合成视频的流程。 | 282 | 76 | 2024-05-19 |
| 7 | [Ask HN: I have many PDFs – what is the best local way to leverage AI for search?](https://news.ycombinator.com/item?id=40528192) | 大量 PDF 含敏感资料，怎样在本地利用 AI 做检索而不上传文档？ | 257 | 90 | 2024-05-30 |
| 8 | [Launch HN: Muddy (YC S19) – Multiplayer browser for getting work done](https://news.ycombinator.com/item?id=40309342) | Muddy 团队介绍多人协作浏览器，希望让共同处理工作更顺畅。 | 252 | 111 | 2024-05-09 |
| 9 | [Discussion: Job seekers can't find a job and Employers can't find an employees](https://news.ycombinator.com/item?id=40415646) | 求职者找不到工作、雇主招不到员工，这种招聘错配究竟从何而来？ | 242 | 366 | 2024-05-20 |
| 10 | [Ask HN: How to handle user file uploads?](https://news.ycombinator.com/item?id=40221210) | 产品允许用户上传媒体文件，怎样设计安全可靠的上传与处理流程？ | 214 | 186 | 2024-05-01 |

### 2024-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What is the best code base you ever worked on?](https://news.ycombinator.com/item?id=40818809) | 你工作过最好的代码库是什么，好质量来自团队习惯还是管理约束？ | 561 | 454 | 2024-06-28 |
| 2 | [Ask HN: What was your most humbling learning moment?](https://news.ycombinator.com/item?id=40555435) | 哪次学习经历最让你意识到自身不足，甚至重新认识自己的技术水平？ | 532 | 680 | 2024-06-02 |
| 3 | [Ask HN: Who is hiring? (June 2024)](https://news.ycombinator.com/item?id=40563283) | 2024 年 6 月招聘集中帖，雇主在此介绍岗位及远程工作条件。 | 391 | 546 | 2024-06-03 |
| 4 | [Ask HN: Why do message queue-based architectures seem less popular now?](https://news.ycombinator.com/item?id=40723302) | 曾经流行的消息队列架构为何热度降低，如今分布式系统更偏向什么方案？ | 389 | 364 | 2024-06-18 |
| 5 | [Ask HN: Machine learning engineers, what do you do at work?](https://news.ycombinator.com/item?id=40610794) | 机器学习工程师每天到底做些什么，邀请从业者分享真实工作内容。 | 365 | 226 | 2024-06-07 |
| 6 | [Launch HN: Hatchet (YC W24) – Open-source task queue, now with a cloud version](https://news.ycombinator.com/item?id=40810986) | Hatchet 介绍开源任务队列及其云服务，帮助应用调度后台任务。 | 245 | 95 | 2024-06-27 |
| 7 | [Ask HN: What happens when I click "request for quote" on your SaaS?](https://news.ycombinator.com/item?id=40726735) | SaaS 企业版的“联系报价”背后怎样定价，厂商依据什么给每家公司报价？ | 200 | 201 | 2024-06-19 |
| 8 | [Ask HN: Who wants to be hired? (June 2024)](https://news.ycombinator.com/item?id=40563280) | 2024 年 6 月求职自荐帖，求职者展示技能、所在地与工作意愿。 | 184 | 457 | 2024-06-03 |
| 9 | [Ask HN: What macOS apps/programs do you use daily and recommend?](https://news.ycombinator.com/item?id=40627395) | 主要设备转向 Mac 后，有哪些每天都会用、值得安装的 macOS 软件？ | 183 | 256 | 2024-06-09 |
| 10 | [Ask HN: Those of you who've left the SWE world, what did you transition into?](https://news.ycombinator.com/item?id=40780940) | 离开软件工程岗位的人后来做了什么，寻找换职业方向的亲历故事。 | 183 | 185 | 2024-06-24 |

### 2024-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who is hiring? (July 2024)](https://news.ycombinator.com/item?id=40846428) | 2024 年 7 月招聘集中帖，岗位需注明远程安排及适用地区。 | 496 | 602 | 2024-07-01 |
| 2 | [Ask HN: What's Prolog like in 2024?](https://news.ycombinator.com/item?id=40994552) | 2024 年的 Prolog 生态怎样，逻辑编程在现实中还有哪些用途？ | 427 | 276 | 2024-07-18 |
| 3 | [Ask HN: Is it possible to make FAANG salaries without working there?](https://news.ycombinator.com/item?id=41042123) | 不进入 FAANG，有没有途径拿到相近水平的工程师薪资？ | 307 | 527 | 2024-07-23 |
| 4 | [Launch HN: Undermind (YC S24) – AI agent for discovering scientific papers](https://news.ycombinator.com/item?id=41069909) | Undermind 介绍寻找科研论文的 AI 代理，帮助研究者发现相关文献。 | 292 | 126 | 2024-07-25 |
| 5 | [Amazon's Kindle Direct Publishing is a dystopian nightmare](https://news.ycombinator.com/item?id=40992654) | 作者猛烈批评 Kindle Direct Publishing 的平台管理体验，描述难以申诉的处境。 | 288 | 119 | 2024-07-18 |
| 6 | [Ask HN: Is there any software you only made for your own use but nobody else?](https://news.ycombinator.com/item?id=40878765) | 你写过永远只给自己用的软件吗，邀请分享纯粹满足个人需求的作品。 | 246 | 468 | 2024-07-04 |
| 7 | [Ask HN: How do browsers isolate internal audio from microphone input?](https://news.ycombinator.com/item?id=40918152) | 浏览器怎样避免内部播放音频混入麦克风输入，发帖者好奇其隔离原理。 | 238 | 99 | 2024-07-09 |
| 8 | [Ask HN: Best way to learn robotics with a 10 year old?](https://news.ycombinator.com/item?id=41070703) | 想和十岁孩子一起做机器人，怎样从小型项目开始学习与动手？ | 224 | 99 | 2024-07-25 |
| 9 | [Launch HN: Roame (YC S23) – Flight search engine for your credit card points](https://news.ycombinator.com/item?id=41100094) | Roame 提供信用卡积分航班搜索，帮助用户寻找可兑换的旅行方案。 | 192 | 130 | 2024-07-29 |
| 10 | [Ask HN: Who wants to be hired? (July 2024)](https://news.ycombinator.com/item?id=40846426) | 2024 年 7 月求职自荐帖，介绍个人能力及远程、搬迁等工作选择。 | 186 | 485 | 2024-07-01 |

### 2024-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Launch HN: Airhart Aeronautics (YC S22) – A modern personal airplane](https://news.ycombinator.com/item?id=41163382) | Airhart Aeronautics 团队介绍现代个人飞机，希望改善私人飞行体验。 | 738 | 615 | 2024-08-05 |
| 2 | [Ask HN: What are you working on (August 2024)?](https://news.ycombinator.com/item?id=41342017) | 2024 年 8 月项目交流帖，分享正在构建的东西与酝酿中的新想法。 | 634 | 1424 | 2024-08-24 |
| 3 | [Ask HN: Should we bring software dev in-house?](https://news.ycombinator.com/item?id=41161315) | 中型物流公司考虑组建内部开发团队，何时应把软件研发从外包转为自建？ | 565 | 594 | 2024-08-05 |
| 4 | [Ask HN: Who is hiring? (August 2024)](https://news.ycombinator.com/item?id=41129813) | 2024 年 8 月招聘集中帖，汇集公司需求并注明远程工作的地区限制。 | 383 | 462 | 2024-08-01 |
| 5 | [Launch HN: Sorcerer (YC S24) – Weather balloons that collect more data](https://news.ycombinator.com/item?id=41291219) | Sorcerer 团队介绍能采集更多气象数据的天气气球，改进天气观测。 | 365 | 172 | 2024-08-19 |
| 6 | [Ask HN: What do you monitor on your servers?](https://news.ycombinator.com/item?id=41240379) | 服务器应该监控哪些指标，发帖者为监控产品征集实际运维需求。 | 346 | 186 | 2024-08-13 |
| 7 | [Ask HN: Do we need to pay billions in fees to Stripe, Block, PayPal and Visa/MC?](https://news.ycombinator.com/item?id=41275342) | 支付公司赚取巨额利润，我们是否仍有必要承担现有支付体系的高额手续费？ | 257 | 358 | 2024-08-17 |
| 8 | [Launch HN: Trellis (YC W24) – AI-powered workflows for unstructured data](https://news.ycombinator.com/item?id=41236273) | Trellis 介绍面向非结构化数据的 AI 工作流，将杂乱资料转成可处理数据。 | 234 | 116 | 2024-08-13 |
| 9 | [Ask HN: Resources about math behind A/B testing](https://news.ycombinator.com/item?id=41196237) | 想弄懂 A/B 测试背后的数学，还有哪些深入讲解的学习资料？ | 207 | 55 | 2024-08-08 |
| 10 | [Launch HN: CodeViz (YC S24) – Visual maps of your codebase in VS Code](https://news.ycombinator.com/item?id=41393458) | CodeViz 介绍 VS Code 代码地图扩展，用可视化帮助理解项目结构。 | 189 | 89 | 2024-08-29 |

### 2024-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Why is Pave legal?](https://news.ycombinator.com/item?id=41510103) | 用户质疑汇集企业薪资数据并提供对比的 Pave 是否合法。 | 1098 | 495 | 2024-09-11 |
| 2 | [Tell HN: Burnout is bad to your brain, take care](https://news.ycombinator.com/item?id=41461499) | 作者分享长期抑郁与倦怠后认知恢复困难的经历，提醒读者照顾身心。 | 742 | 327 | 2024-09-05 |
| 3 | [Tell HN: DanBC has died](https://news.ycombinator.com/item?id=41550822) | 帖子通报长期 HN 参与者 DanBC 在久病后去世，供社区表达怀念。 | 479 | 77 | 2024-09-15 |
| 4 | [Ask HN: Who is hiring? (September 2024)](https://news.ycombinator.com/item?id=41425910) | 2024 年 9 月招聘集中帖，企业发布岗位及候选人所在地要求。 | 437 | 483 | 2024-09-02 |
| 5 | [Ask HN: Former gifted children with hard lives, how did you turn out?](https://news.ycombinator.com/item?id=41543666) | 曾被视为天才、后来生活艰难的人如今怎样，发帖者寻找相似经历。 | 375 | 327 | 2024-09-14 |
| 6 | [Ask HN: What are you working on (September 2024)?](https://news.ycombinator.com/item?id=41690087) | 2024 年 9 月项目交流帖，邀请展示近期进展和正在考虑的新方向。 | 354 | 1038 | 2024-09-29 |
| 7 | [Launch HN: Silurian (YC S24) – Simulate the Earth](https://news.ycombinator.com/item?id=41556519) | Silurian 团队介绍模拟地球的项目，尝试建立面向现实世界的预测能力。 | 338 | 141 | 2024-09-16 |
| 8 | [Ask HN: My son might be blind – how to best support](https://news.ycombinator.com/item?id=41588200) | 几个月大的儿子可能失明，家长寻找帮助孩子成长与适应的资源。 | 321 | 160 | 2024-09-19 |
| 9 | [Ask HN: How to store and share passwords in a company?](https://news.ycombinator.com/item?id=41417659) | 公司有大量账号密码，怎样安全存储并把访问权限分享给需要的同事？ | 316 | 277 | 2024-09-01 |
| 10 | [Ask HN: Should you reply STOP to unwanted texts?](https://news.ycombinator.com/item?id=41703312) | 收到陌生营销短信后，应回复 STOP 退订，还是直接屏蔽、删除与举报？ | 290 | 373 | 2024-09-30 |

### 2024-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: What are you working on? (October 2024)](https://news.ycombinator.com/item?id=41966114) | 2024 年 10 月项目交流帖，分享正在做的项目和新点子。 | 411 | 1152 | 2024-10-27 |
| 2 | [Ask HN: What's the "best" book you've ever read?](https://news.ycombinator.com/item?id=41756432) | 如果必须选出读过的“最好的一本书”，你会选什么，又如何定义最好？ | 376 | 940 | 2024-10-06 |
| 3 | [Ask HN: Who is hiring? (October 2024)](https://news.ycombinator.com/item?id=41709301) | 2024 年 10 月招聘集中帖，查看岗位、工作地点及远程条件。 | 363 | 480 | 2024-10-01 |
| 4 | [Ask HN: Who is pretending to be hiring?](https://news.ycombinator.com/item?id=41714672) | 求职困难之际，哪些企业其实只是在假装招聘，如何识别这些职位？ | 337 | 127 | 2024-10-01 |
| 5 | [Ask HN: What's the most creative 'useless' program you've ever written?](https://news.ycombinator.com/item?id=41894765) | 你写过最有创意却没有实际用途的程序是什么，邀请展示好玩的代码。 | 296 | 405 | 2024-10-20 |
| 6 | [Ask HN: Website with 6^16 subpages and 80k+ daily bots](https://news.ycombinator.com/item?id=41923635) | 一个生成海量颜色子页面的小网站每天迎来大量机器人，该如何理解这种流量？ | 287 | 201 | 2024-10-23 |
| 7 | [Ask HN: Founders, what was the major sourcing channel for your first 100 users?](https://news.ycombinator.com/item?id=41862332) | 创业产品最早的一百名用户来自哪里，邀请同时说明目标受众与获客渠道。 | 282 | 191 | 2024-10-16 |
| 8 | [Ask HN: What happens to ".io" TLD after UK gives back the Chagos Islands?](https://news.ycombinator.com/item?id=41729526) | 英国归还查戈斯群岛主权后，.io 顶级域名的未来会受到什么影响？ | 250 | 205 | 2024-10-03 |
| 9 | [I'm Peter Roberts, immigration attorney who does work for YC and startups. AMA](https://news.ycombinator.com/item?id=41870887) | Peter Roberts 移民律师再次开放问答，回答社区关于移民手续与创业的问题。 | 245 | 385 | 2024-10-17 |
| 10 | [Ask HN: Who wants to be hired? (October 2024)](https://news.ycombinator.com/item?id=41709299) | 2024 年 10 月求职自荐帖，展示技能、所在地与求职偏好。 | 161 | 422 | 2024-10-01 |

### 2024-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Launch HN: Regatta Storage (YC F24) – Turn S3 into a local-like, POSIX cloud FS](https://news.ycombinator.com/item?id=42174204) | Regatta Storage 介绍基于 S3 的 POSIX 云文件系统，试图提供接近本地的使用体验。 | 587 | 320 | 2024-11-18 |
| 2 | [Hetzner cuts traffic on US VPSs, raises prices](https://news.ycombinator.com/item?id=42264427) | 发帖者转述 Hetzner 调价邮件，称美国 VPS 将减少流量额度并提高价格。 | 472 | 686 | 2024-11-28 |
| 3 | [Ask HN: Who is hiring? (November 2024)](https://news.ycombinator.com/item?id=42017580) | 2024 年 11 月招聘集中帖，要求发布者确实有招聘意愿并愿回应候选人。 | 379 | 491 | 2024-11-01 |
| 4 | [Launch HN: Human Layer (YC F24) – Human-in-the-Loop API for AI Systems](https://news.ycombinator.com/item?id=42247368) | HumanLayer 介绍让 AI 系统联系真人的 API，在自动化流程中加入人工参与。 | 354 | 196 | 2024-11-26 |
| 5 | [Ask HN: Life-changing purchases since 2020? (Under $100 and under $1000)](https://news.ycombinator.com/item?id=42079768) | 2020 年以来哪些购买改善了生活，分别征集百美元和千美元以内的好物。 | 288 | 601 | 2024-11-07 |
| 6 | [YubiKey still selling old stock with vulnerable firmware](https://news.ycombinator.com/item?id=42110901) | 发帖者称 YubiKey 仍在出售含易受 EUCLEAK 攻击固件的旧库存。 | 288 | 109 | 2024-11-11 |
| 7 | [Launch HN: Codebuff (YC F24) – CLI tool that writes code for you](https://news.ycombinator.com/item?id=42078536) | Codebuff 展示命令行编程助手，让用户通过终端请求 AI 修改代码。 | 285 | 239 | 2024-11-07 |
| 8 | [Ask HN: Recommendation for a SWE looking to get up to speed with latest on AI](https://news.ycombinator.com/item?id=42256093) | 常用 ChatGPT 的软件工程师，怎样系统补齐当前 AI 技术与生态知识？ | 275 | 94 | 2024-11-27 |
| 9 | [Ask HN: What would you preserve if the internet were to go down tomorrow?](https://news.ycombinator.com/item?id=42030832) | 假如互联网明天无限期中断，你最想提前保存哪些内容和资源？ | 259 | 310 | 2024-11-03 |
| 10 | [Ask HN: How do you communicate in a remote startup?](https://news.ycombinator.com/item?id=42149938) | 远程创业团队如何沟通，发帖者希望在保持远程的前提下改善协作。 | 244 | 271 | 2024-11-15 |

### 2024-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Merry Christmas Everyone](https://news.ycombinator.com/item?id=42506577) | HN 用户互祝圣诞快乐，并邀请大家分享节日回忆。 | 1503 | 383 | 2024-12-25 |
| 2 | [Happy New Year 2025](https://news.ycombinator.com/item?id=42562750) | HN 用户向社区送上 2025 年新年祝福。 | 1223 | 258 | 2024-12-31 |
| 3 | [Tell HN: John Friel my father, internet pioneer and creator of QModem, has died](https://news.ycombinator.com/item?id=42551900) | John Friel 的子女通报这位互联网先驱、QModem 作者去世，并征集回忆。 | 1092 | 98 | 2024-12-30 |
| 4 | [Ask HN: Those making $500/month on side projects in 2024 – Show and tell](https://news.ycombinator.com/item?id=42373343) | 2024 年副项目月入五百美元的作者来分享，交流产品与经营做法。 | 667 | 802 | 2024-12-10 |
| 5 | [Ask HN: How can I grow as an engineer without good seniors to learn from?](https://news.ycombinator.com/item?id=42289955) | 刚毕业却缺少优秀前辈带领，工程师如何主动建立成长路径？ | 577 | 298 | 2024-12-01 |
| 6 | [Ask HN: SWEs how do you future-proof your career in light of LLMs?](https://news.ycombinator.com/item?id=42431103) | 大语言模型改变开发工作后，软件工程师怎样准备长期仍有价值的职业能力？ | 530 | 991 | 2024-12-16 |
| 7 | [Ask HN: How to learn marketing and sales as a solo entrepreneur?](https://news.ycombinator.com/item?id=42557947) | 独立开发者做出产品却卖不出去，怎样补上营销与销售这门课？ | 497 | 203 | 2024-12-31 |
| 8 | [Launch HN: Double (YC W24) – Index Investing with 0% Expense Ratios](https://news.ycombinator.com/item?id=42377018) | Double 团队介绍零费用率的指数投资产品，让用户构建自己的投资配置。 | 443 | 413 | 2024-12-10 |
| 9 | [Ask HN: Who is hiring? (December 2024)](https://news.ycombinator.com/item?id=42297424) | 2024 年 12 月招聘集中帖，汇集年末职位及远程工作的地区条件。 | 386 | 471 | 2024-12-02 |
| 10 | [Ask HN: Programmers who don't use autocomplete/LSP, how do you do it?](https://news.ycombinator.com/item?id=42492508) | 不用自动补全和语言服务器的程序员，日常靠什么完成开发与查阅？ | 355 | 631 | 2024-12-23 |

### 2025-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Thank HN: My bootstrapped startup got acquired today](https://news.ycombinator.com/item?id=42806247) | VWO 创始人感谢 HN 早期支持，并分享以两亿美元出售公司的消息。 | 2246 | 396 | 2025-01-23 |
| 2 | [Ask HN: Is anyone doing anything cool with tiny language models?](https://news.ycombinator.com/item?id=42784365) | 参数只有五亿到三十亿的小语言模型，已经能做出哪些有趣的实用项目？ | 684 | 346 | 2025-01-21 |
| 3 | [Tell HN: Impassable Cloudflare challenges are ruining my browsing experience](https://news.ycombinator.com/item?id=42577076) | 发帖者称 Cloudflare 验证经常无法通过，严重影响旅行中的网页访问。 | 523 | 304 | 2025-01-02 |
| 4 | [Ask HN: Books about people who did hard things](https://news.ycombinator.com/item?id=42614722) | 哪些书讲清人们如何完成艰难事业，呈现真正做成大事的过程？ | 495 | 431 | 2025-01-06 |
| 5 | [Ask HN: Organize local communities without Facebook?](https://news.ycombinator.com/item?id=42779776) | 想把本地社群从 Facebook 搬走，有没有能独立部署的现成社区平台？ | 407 | 384 | 2025-01-21 |
| 6 | [Ask HN: Why buy domains and 301 redirect them to me?](https://news.ycombinator.com/item?id=42812779) | 陌生人买下相似域名再重定向到自己的 SaaS，这种做法可能有何目的？ | 382 | 131 | 2025-01-24 |
| 7 | [I'm Peter Roberts, immigration attorney, who does work for YC and startups. AMA](https://news.ycombinator.com/item?id=42770125) | 移民律师 Peter Roberts 开放新一轮问答，回应社区的移民相关疑虑。 | 370 | 377 | 2025-01-20 |
| 8 | [Ask HN: Who is hiring? (January 2025)](https://news.ycombinator.com/item?id=42575537) | 2025 年 1 月招聘集中帖，企业注明岗位地点和远程工作的适用范围。 | 335 | 481 | 2025-01-02 |
| 9 | [Ask HN: How do you prevent the impact of social media on your children?](https://news.ycombinator.com/item?id=42683494) | 社交媒体对成长的影响令人担忧，家长如何保护孩子并建立使用边界？ | 334 | 390 | 2025-01-13 |
| 10 | [Ask HN: Where to Work After 40?](https://news.ycombinator.com/item?id=42573875) | 四十岁创业失败后重新找工作，该去哪里寻找适合自己的职业机会？ | 311 | 273 | 2025-01-02 |

### 2025-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Cloudflare is blocking Pale Moon and other non-mainstream browsers](https://news.ycombinator.com/item?id=42953508) | 用户称 Cloudflare 验证机制阻止 Pale Moon 等小众浏览器访问网站。 | 1343 | 524 | 2025-02-05 |
| 2 | [Tell HN: Y Combinator backing AI company to abuse factory workers](https://news.ycombinator.com/item?id=43170850) | 发帖者批评 YC 投资的 Optifye.ai，认为其 AI 工厂监控会伤害工人。 | 631 | 188 | 2025-02-25 |
| 3 | [Ask HN: What is interviewing like now with everyone using AI?](https://news.ycombinator.com/item?id=42909166) | 候选人普遍能用 AI 后，技术面试正在怎样调整，哪些考察方式仍有效？ | 535 | 710 | 2025-02-02 |
| 4 | [Ask HN: Who is hiring? (February 2025)](https://news.ycombinator.com/item?id=42919502) | 2025 年 2 月招聘集中帖，可查看各公司真实招聘需求与远程条件。 | 490 | 616 | 2025-02-03 |
| 5 | [Ask HN: Former devs who can't get a job, what did you end up doing for work?](https://news.ycombinator.com/item?id=43164498) | 开发岗位找不到、积蓄渐少时，原程序员最后靠什么工作维持生活？ | 306 | 287 | 2025-02-24 |
| 6 | [LinkedIn is the worst social media I've ever seen](https://news.ycombinator.com/item?id=43052409) | 发帖者批评 LinkedIn 的 AI 内容和诱导设计，表达对平台体验的不满。 | 277 | 125 | 2025-02-14 |
| 7 | [Launch HN: A0.dev (YC W25) – React Native App Generator](https://news.ycombinator.com/item?id=43015267) | A0.dev 介绍 React Native 应用生成平台，帮助用户更快创建移动应用。 | 263 | 97 | 2025-02-11 |
| 8 | [Ask HN: What are you working on? (February 2025)](https://news.ycombinator.com/item?id=43154065) | 2025 年 2 月项目交流帖，邀请分享正在做的东西与新想法。 | 261 | 905 | 2025-02-23 |
| 9 | [Ask HN: Do US tech firms realize the backlash growing in Europe?](https://news.ycombinator.com/item?id=43139172) | 欧洲对美国科技企业的不满是否正在积累，美国公司意识到了吗？ | 251 | 296 | 2025-02-22 |
| 10 | [Launch HN: Maritime Fusion (YC W25) – Fusion Reactors for Ships](https://news.ycombinator.com/item?id=43185246) | Maritime Fusion 团队介绍面向船舶的聚变反应堆计划，探索海运能源新方案。 | 216 | 261 | 2025-02-26 |

### 2025-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Who is hiring? (March 2025)](https://news.ycombinator.com/item?id=43243024) | 2025 年 3 月招聘集中帖，汇集公司岗位与工作地点要求。 | 391 | 516 | 2025-03-03 |
| 2 | [Ask HN: What are you working on? (March 2025)](https://news.ycombinator.com/item?id=43527452) | 2025 年 3 月项目交流帖，分享近期进展与正在思考的点子。 | 390 | 996 | 2025-03-30 |
| 3 | [Ask HN: Any insider takes on Yann LeCun's push against current architectures?](https://news.ycombinator.com/item?id=43325049) | LeCun 持续质疑现有 AI 架构，业内人如何看待他的判断与替代方向？ | 385 | 325 | 2025-03-10 |
| 4 | [Ask HN: How do I escape homelessness after rebuilding my mental health?](https://news.ycombinator.com/item?id=43402315) | 心理健康好转后仍无家可归，发帖者寻求重新建立稳定生活的实际帮助。 | 343 | 233 | 2025-03-18 |
| 5 | [Ask HN: Do your eyes bug you even though your prescription is "correct"?](https://news.ycombinator.com/item?id=43291922) | 眼镜度数明明合适却仍眼睛不舒服，发帖者调查屏幕使用与视觉疲劳。 | 340 | 326 | 2025-03-07 |
| 6 | [I'm Peter Roberts, immigration attorney who does work for YC and startups. AMA](https://news.ycombinator.com/item?id=43363056) | Peter Roberts 移民律师连续开放数小时问答，由社区提问引导讨论。 | 300 | 487 | 2025-03-14 |
| 7 | [Ask HN: What less-popular systems programming language are you using?](https://news.ycombinator.com/item?id=43223162) | 常见选择之外，你正在使用哪些较少人知的系统编程语言？ | 287 | 450 | 2025-03-01 |
| 8 | [Ask HN: How did the internet discover my subdomain?](https://news.ycombinator.com/item?id=43285725) | 从未公开的子域名为何被互联网发现，扫描者可能通过什么线索找到它？ | 287 | 287 | 2025-03-06 |
| 9 | [Lynx is the oldest web browser still being maintained](https://news.ycombinator.com/item?id=43377829) | 发帖者向仍在维护 Lynx 的开发者致意，称它是持续维护最久的浏览器。 | 229 | 109 | 2025-03-16 |
| 10 | [Ask HN: Where do seasoned devs look for short-term work?](https://news.ycombinator.com/item?id=43354115) | 资深开发者去哪里寻找短期项目，让经验转化为灵活的工作机会？ | 224 | 174 | 2025-03-13 |

### 2025-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Announcing tomhow as a public moderator](https://news.ycombinator.com/item?id=43558671) | HN 宣布 Tom Howard 公开担任管理员，与 dang 共同维护社区。 | 1825 | 462 | 2025-04-02 |
| 2 | [Ask HN: Share your AI prompt that stumps every model](https://news.ycombinator.com/item?id=43782299) | 有没有一道提示词能难倒所有现有 AI 模型，发帖者希望收集这类挑战。 | 440 | 633 | 2025-04-24 |
| 3 | [Ask HN: What are you working on? (April 2025)](https://news.ycombinator.com/item?id=43815523) | 2025 年 4 月项目交流帖，介绍正在构建的作品与新方向。 | 410 | 1214 | 2025-04-27 |
| 4 | [Ask HN: Do you still use search engines?](https://news.ycombinator.com/item?id=43619768) | 越来越依赖其他问答工具后，你还使用传统搜索引擎吗？ | 350 | 580 | 2025-04-08 |
| 5 | [Ask HN: Who is hiring? (April 2025)](https://news.ycombinator.com/item?id=43547611) | 2025 年 4 月招聘集中帖，企业介绍职位及远程安排。 | 279 | 490 | 2025-04-01 |
| 6 | [Ask HN: Why is there no P2P streaming protocol like BitTorrent?](https://news.ycombinator.com/item?id=43684286) | 为什么大众直播没有出现像 BitTorrent 一样普及的去中心化 P2P 协议？ | 236 | 223 | 2025-04-14 |
| 7 | [Launch HN: mrge.io (YC X25) – Cursor for code review](https://news.ycombinator.com/item?id=43692476) | mrge.io 团队介绍 AI 代码审查平台，帮助团队检查修改与处理评审工作。 | 221 | 108 | 2025-04-15 |
| 8 | [Ask HN: I'm an MIT senior and still unemployed – and so are most of my friends](https://news.ycombinator.com/item?id=43612448) | MIT 计算机专业毕业在即仍无工作，发帖者称不少同学也面临同样困境。 | 215 | 234 | 2025-04-07 |
| 9 | [Ask HN: Why hasn’t AMD made a viable CUDA alternative?](https://news.ycombinator.com/item?id=43547309) | AMD 为何迟迟没能提供足以竞争 CUDA 的方案，难点究竟在哪里？ | 194 | 187 | 2025-04-01 |
| 10 | [Launch HN: Magic Patterns (YC W23) – AI Design and Prototyping for Product Teams](https://news.ycombinator.com/item?id=43752176) | Magic Patterns 面向产品团队生成设计与交互原型，用 AI 辅助早期构思。 | 185 | 114 | 2025-04-21 |

### 2025-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: How are you acquiring your first hundred users?](https://news.ycombinator.com/item?id=43970837) | 每月五十美元的消费级 AI SaaS，怎样找到最早的一百名用户？ | 573 | 354 | 2025-05-13 |
| 2 | [Ask HN: What are good high-information density UIs (screenshots, apps, sites)?](https://news.ycombinator.com/item?id=43925732) | 哪些界面在信息很多时仍然清晰好用，征集高信息密度设计的实例。 | 530 | 372 | 2025-05-08 |
| 3 | [Launch HN: Exa (YC S21) – The web as a database](https://news.ycombinator.com/item?id=43906841) | Exa 介绍把网页当作数据库检索的产品，让用户整理所需的网络信息。 | 412 | 133 | 2025-05-06 |
| 4 | [Ask HN: What are you working on? (May 2025)](https://news.ycombinator.com/item?id=44090387) | 2025 年 5 月项目交流帖，邀请展示当前作品和酝酿中的想法。 | 349 | 1087 | 2025-05-25 |
| 5 | [Ask HN: Anyone struggling to get value out of coding LLMs?](https://news.ycombinator.com/item?id=44095189) | 日常能用模型查知识，写代码却难获益，还有谁遇到类似落差？ | 345 | 279 | 2025-05-26 |
| 6 | [Ask HN: Cursor or Windsurf?](https://news.ycombinator.com/item?id=43959710) | Cursor 与 Windsurf 更新太快，实际使用中应该如何选择？ | 316 | 398 | 2025-05-12 |
| 7 | [Ask HN: What projects do you donate to?](https://news.ycombinator.com/item?id=44071321) | 你把钱捐给哪些项目，支持互联网中希望继续存在的服务与公共资源？ | 279 | 289 | 2025-05-23 |
| 8 | [Ask HN: Who is hiring? (May 2025)](https://news.ycombinator.com/item?id=43858554) | 2025 年 5 月招聘集中帖，汇集企业岗位及地区、远程要求。 | 263 | 432 | 2025-05-01 |
| 9 | [Launch HN: Better Auth (YC X25) – Authentication Framework for TypeScript](https://news.ycombinator.com/item?id=44030492) | Better Auth 团队介绍面向 TypeScript 的认证框架，处理应用身份验证需求。 | 259 | 106 | 2025-05-19 |
| 10 | [I'm Peter Roberts, immigration attorney, who does work for YC and startups. AMA](https://news.ycombinator.com/item?id=44006381) | 移民环境快速变化时，律师 Peter Roberts 回答社区的新疑问。 | 257 | 452 | 2025-05-16 |

### 2025-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Help restore the tax deduction for software dev in the US (Section 174)](https://news.ycombinator.com/item?id=44226145) | 用户呼吁推动修改美国税法第 174 条，恢复软件开发费用直接抵扣。 | 2439 | 907 | 2025-06-09 |
| 2 | [Launch HN: Vassar Robotics (YC X25) – $219 robot arm that learns new skills](https://news.ycombinator.com/item?id=44240302) | Vassar Robotics 展示售价 219 美元、可学习新技能的机械臂。 | 580 | 219 | 2025-06-10 |
| 3 | [Ask HN: What Are You Working On? (June 2025)](https://news.ycombinator.com/item?id=44416093) | 2025 年 6 月项目交流帖，分享近期正在开发和探索的事情。 | 439 | 1400 | 2025-06-29 |
| 4 | [Tell HN: Beware confidentiality agreements that act as lifetime non competes](https://news.ycombinator.com/item?id=44338562) | 发帖者提醒注意保密协议的范围，称某些条款可能起到终身竞业限制作用。 | 416 | 255 | 2025-06-21 |
| 5 | [Ask HN: How do I learn robotics in 2025?](https://news.ycombinator.com/item?id=44158353) | 2025 年想动手做机器人，从哪些知识、工具和项目开始最合适？ | 408 | 99 | 2025-06-02 |
| 6 | [Ask HN: How do I give back to people helped me when I was young and had nothing?](https://news.ycombinator.com/item?id=44268448) | 年轻时得到前辈帮助，如今怎样回报那些曾给予善意与启发的人？ | 396 | 206 | 2025-06-13 |
| 7 | [Ask HN: Who is hiring? (June 2025)](https://news.ycombinator.com/item?id=44159528) | 2025 年 6 月招聘集中帖，企业发布岗位并说明远程工作的限制。 | 370 | 523 | 2025-06-02 |
| 8 | [Launch HN: Issen (YC F24) – Personal AI language tutor](https://news.ycombinator.com/item?id=44387828) | Issen 介绍个人 AI 外语口语老师，让学习者通过语音对话练习语言。 | 313 | 272 | 2025-06-26 |
| 9 | [Ask HN: Startup getting spammed with PayPal disputes, what should we do?](https://news.ycombinator.com/item?id=44176510) | 创业平台遭到大量 PayPal 争议申请，怎样识别滥用并减少损失？ | 291 | 185 | 2025-06-04 |
| 10 | [Ask HN: Has anybody built search on top of Anna's Archive?](https://news.ycombinator.com/item?id=44176514) | 有人在 Anna's Archive 之上建立全文搜索吗，这样的系统需要什么条件？ | 291 | 146 | 2025-06-04 |

### 2025-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Claude Code weekly rate limits](https://news.ycombinator.com/item?id=44713757) | 帖子转述 Claude Code 将为订阅用户引入每周使用额度限制的通知。 | 609 | 705 | 2025-07-28 |
| 2 | [Ask HN: Is it time to fork HN into AI/LLM and "Everything else/other?"](https://news.ycombinator.com/item?id=44571740) | AI 话题占据版面后，HN 是否应该分成 AI 与其他内容两个频道？ | 553 | 372 | 2025-07-15 |
| 3 | [Tell HN: Notion Desktop is monitoring your audio and network](https://news.ycombinator.com/item?id=44594790) | 发帖者注意到 Notion 桌面端提示正在开会，质疑其音频与网络监测行为。 | 430 | 171 | 2025-07-17 |
| 4 | [I launched 17 side projects. Result? I'm rich in expired domains](https://news.ycombinator.com/item?id=44733800) | 作者自嘲上线十七个副项目只积累了过期域名，回顾不断开新坑的循环。 | 368 | 262 | 2025-07-30 |
| 5 | [Ask HN: How did Soham Parekh get so many jobs?](https://news.ycombinator.com/item?id=44448461) | 围绕 Soham Parekh 的争议，发帖者询问他如何同时拿到如此多工作。 | 319 | 419 | 2025-07-02 |
| 6 | [Ask HN: Who is hiring? (July 2025)](https://news.ycombinator.com/item?id=44434576) | 2025 年 7 月招聘集中帖，查看公司岗位及远程工作条件。 | 273 | 452 | 2025-07-01 |
| 7 | [Launch HN: Hyprnote (YC S25) – An open-source AI meeting notetaker](https://news.ycombinator.com/item?id=44725306) | Hyprnote 团队介绍开源 AI 会议笔记工具，帮助记录与整理会议内容。 | 270 | 180 | 2025-07-29 |
| 8 | [Ask HN: What are you working on? (July 2025)](https://news.ycombinator.com/item?id=44702833) | 2025 年 7 月项目交流帖，分享正在做的项目和新的创意。 | 260 | 865 | 2025-07-27 |
| 9 | [Ask HN: Any active COBOL devs here? What are you working on?](https://news.ycombinator.com/item?id=44604257) | 还有在职 COBOL 开发者吗，邀请介绍金融、政府传闻之外的实际项目。 | 245 | 189 | 2025-07-18 |
| 10 | [Launch HN: K-Scale Labs (YC W24) – Open-Source Humanoid Robots](https://news.ycombinator.com/item?id=44456904) | K-Scale Labs 介绍开源人形机器人，希望让更多人参与机器人研发。 | 233 | 95 | 2025-07-03 |

### 2025-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: The government of my country blocked VPN access. What should I use?](https://news.ycombinator.com/item?id=45054260) | 印尼用户称政府封锁社交平台与 VPN，向社区询问替代连接方式。 | 1338 | 732 | 2025-08-28 |
| 2 | [VC-backed company just killed my EU trademark for a small OSS project](https://news.ycombinator.com/item?id=44883634) | 小型开源项目作者称受到风投支持公司的商标行动影响，失去欧盟商标。 | 854 | 249 | 2025-08-13 |
| 3 | [Ask HN: How can ChatGPT serve 700M users when I can't run one GPT-4 locally?](https://news.ycombinator.com/item?id=44840728) | 个人连一个 GPT-4 都跑不了，ChatGPT 如何支撑数亿用户的服务需求？ | 574 | 365 | 2025-08-08 |
| 4 | [Ask HN: Why does the US Visa application website do a port-scan of my network?](https://news.ycombinator.com/item?id=44959073) | 发帖者检测到美国签证申请网站扫描本地端口，追问其目的与必要性。 | 537 | 252 | 2025-08-20 |
| 5 | [Ask HN: Why hasn't x86 caught up with Apple M series?](https://news.ycombinator.com/item?id=45019483) | x86 为何还没追上 Apple M 系列的体验与能效，发帖者结合 M1 Pro 使用感受发问。 | 452 | 620 | 2025-08-25 |
| 6 | [F-Droid build servers can't build modern Android apps due to outdated CPUs](https://news.ycombinator.com/item?id=44884709) | 发帖者称 F-Droid 构建服务器 CPU 过旧，导致部分现代 Android 应用无法构建。 | 442 | 297 | 2025-08-13 |
| 7 | [Ask HN: What trick of the trade took you too long to learn?](https://news.ycombinator.com/item?id=44789068) | 哪些行业技巧你学得太晚，掌握之后才发现原本可以更轻松？ | 387 | 670 | 2025-08-04 |
| 8 | [Petition to stop Google from restricting sideloading and FOSS apps](https://news.ycombinator.com/item?id=45050502) | 帖子分享反对 Android 开发者验证限制的请愿，担忧侧载与自由软件受到影响。 | 295 | 218 | 2025-08-28 |
| 9 | [Ask HN: Have you ever regretted open-sourcing something?](https://news.ycombinator.com/item?id=44766771) | 开源通常被视为好事，你是否曾因维护负担或其他后果后悔公开代码？ | 274 | 424 | 2025-08-02 |
| 10 | [Tell HN: Anthropic expires paid credits after a year](https://news.ycombinator.com/item?id=44793446) | 发帖者转述 Anthropic 通知，提醒付费 API 额度一年后可能到期。 | 272 | 136 | 2025-08-05 |

### 2025-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Has anyone else been unemployed for over two years?](https://news.ycombinator.com/item?id=45306539) | 失业超过两年的人如今怎样生活，又如何应对长期求职压力？ | 459 | 565 | 2025-09-19 |
| 2 | [Ask HN: What are you working on? (September 2025)](https://news.ycombinator.com/item?id=45418675) | 2025 年 9 月项目交流帖，介绍近期进展与接下来想做的事。 | 313 | 1017 | 2025-09-29 |
| 3 | [Ask HN: Who is hiring? (September 2025)](https://news.ycombinator.com/item?id=45093192) | 2025 年 9 月招聘集中帖，企业在此发布职位和工作地点条件。 | 267 | 443 | 2025-09-01 |
| 4 | [Ask HN: What's a good 3D Printer for sub $1000?](https://news.ycombinator.com/item?id=45251624) | 一千美元以内买哪款 3D 打印机，才能兼顾封闭结构与较大打印空间？ | 241 | 288 | 2025-09-15 |
| 5 | [Ask HN: What is nowadays (opensource) way of converting HTML to PDF?](https://news.ycombinator.com/item?id=45404760) | wkhtmltopdf 难用，今天有哪些开源方案适合把 HTML 稳定转换为 PDF？ | 176 | 165 | 2025-09-28 |
| 6 | [Launch HN: Trigger.dev (YC W23) – Open-source platform to build reliable AI apps](https://news.ycombinator.com/item?id=45250720) | Trigger.dev 介绍开源开发平台，帮助构建运行可靠的 AI 应用。 | 162 | 65 | 2025-09-15 |
| 7 | [Paid $2400 to Cloudflare, support refuses to help](https://news.ycombinator.com/item?id=45250553) | 发帖者预付 Cloudflare 商务套餐后遇到问题，抱怨付费支持拒绝协助。 | 146 | 29 | 2025-09-15 |
| 8 | [Everyone's trying vectors and graphs for AI memory. We went back to SQL](https://news.ycombinator.com/item?id=45329322) | 作者分享用 SQL 构建 AI 记忆的选择，讨论向量与图存储之外的实现路线。 | 136 | 63 | 2025-09-22 |
| 9 | [I launched a Mac utility; now there are 5 clones on the App Store using my story](https://news.ycombinator.com/item?id=45269827) | 独立开发者称 Mac 工具上线后出现多个克隆，甚至沿用了自己的宣传故事。 | 135 | 135 | 2025-09-16 |
| 10 | [Launch HN: Strata (YC X25) – One MCP server for AI to handle thousands of tools](https://news.ycombinator.com/item?id=45347914) | Strata 用一个开源 MCP 服务连接大量工具，帮助 AI 应对复杂的工具集合。 | 133 | 66 | 2025-09-23 |

### 2025-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Azure outage](https://news.ycombinator.com/item?id=45748661) | 发帖者报告 Azure 无法访问，连管理门户也受影响，询问其他用户情况。 | 885 | 806 | 2025-10-29 |
| 2 | [Tell HN: Azure Outage](https://news.ycombinator.com/item?id=45748799) | 英国用户报告 Azure 门户与价格计算器无法打开，怀疑平台发生故障。 | 438 | 2 | 2025-10-29 |
| 3 | [Ask HN: Our AWS account got compromised after their outage](https://news.ycombinator.com/item?id=45657345) | AWS 故障后账号出现数百个陌生实例，发帖者询问账号入侵是否与故障有关。 | 395 | 95 | 2025-10-21 |
| 4 | [Ask HN: Abandoned/dead projects you think died before their time and why?](https://news.ycombinator.com/item?id=45553132) | 哪些项目被放弃得太早，讨论其值得延续的想法与未竟的潜力。 | 363 | 891 | 2025-10-11 |
| 5 | [Ask HN: Who uses open LLMs and coding assistants locally? Share setup and laptop](https://news.ycombinator.com/item?id=45771870) | 谁在本地使用开放模型和编程助手，邀请分享电脑配置与真实工作流程。 | 350 | 192 | 2025-10-31 |
| 6 | [Ask HN: What are you working on? (October 2025)](https://news.ycombinator.com/item?id=45561428) | 2025 年 10 月项目交流帖，分享当前作品与值得尝试的新想法。 | 347 | 1056 | 2025-10-12 |
| 7 | [Tell HN: AWS us-east-1 services are down](https://news.ycombinator.com/item?id=45640754) | 发帖者报告 AWS us-east-1 多项服务异常，称状态页当时仍显示正常。 | 340 | 1 | 2025-10-20 |
| 8 | [Ask HN: What's the best hackable smart TV?](https://news.ycombinator.com/item?id=45490740) | 想把电视更多当作笔记本外接屏幕，哪款智能电视便于修改与掌控？ | 292 | 191 | 2025-10-06 |
| 9 | [Ask HN: How to stop an AWS bot sending 2B requests/month?](https://news.ycombinator.com/item?id=45613567) | 来自 AWS 的爬虫每月发送二十亿次请求，怎样有效阻断这种访问？ | 288 | 181 | 2025-10-17 |
| 10 | [Ask HN: Who is hiring? (October 2025)](https://news.ycombinator.com/item?id=45438503) | 2025 年 10 月招聘集中帖，查看企业需求与远程工作的地区条件。 | 247 | 464 | 2025-10-01 |

### 2025-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Happy Thanksgiving](https://news.ycombinator.com/item?id=46065955) | 一位十五年的社区成员送上感恩节祝福，感谢 HN 长期带来的交流。 | 805 | 198 | 2025-11-27 |
| 2 | [Tell HN: X is opening any tweet link in a webview whether you press it or not](https://news.ycombinator.com/item?id=45807775) | 发帖者称 X 会自动在内置网页视图打开推文链接，质疑访问量增长的来源。 | 647 | 517 | 2025-11-04 |
| 3 | [Ask HN: What Are You Working On? (Nov 2025)](https://news.ycombinator.com/item?id=45869146) | 2025 年 11 月项目交流帖，邀请分享新作品与正在探索的点子。 | 464 | 1369 | 2025-11-09 |
| 4 | [Ask HN: Who is hiring? (November 2025)](https://news.ycombinator.com/item?id=45800465) | 2025 年 11 月招聘集中帖，汇集公司岗位与候选人的地区要求。 | 401 | 579 | 2025-11-03 |
| 5 | [Ask HN: Hearing aid wearers, what's hot?](https://news.ycombinator.com/item?id=46029699) | 助听器使用五年后损坏，发帖者询问如今有哪些值得升级的新选择。 | 356 | 210 | 2025-11-24 |
| 6 | [Ask HN: My family business runs on a 1993-era text-based-UI (TUI). Anybody else?](https://news.ycombinator.com/item?id=45823234) | 家族企业仍依赖九十年代的文本界面系统，还有哪些生意继续这样运行？ | 320 | 309 | 2025-11-05 |
| 7 | [Tell HN: Want a better HN? Visit /newest](https://news.ycombinator.com/item?id=46079745) | 想改善 HN 内容质量，作者建议多看最新提交页，让好内容有机会被发现。 | 299 | 85 | 2025-11-28 |
| 8 | [Launch HN: Onyx (YC W24) – Open-source chat UI](https://news.ycombinator.com/item?id=46045987) | Onyx 团队介绍开源聊天界面，为 AI 对话与相关工作提供入口。 | 254 | 160 | 2025-11-25 |
| 9 | [Ask HN: Where to begin with "modern" Emacs?](https://news.ycombinator.com/item?id=45783376) | 多年使用 Neovim 后想试 Emacs，怎样开始接触现代配置与使用方式？ | 228 | 121 | 2025-11-01 |
| 10 | [Ask HN: How would you set up a child’s first Linux computer?](https://news.ycombinator.com/item?id=45864732) | 为孩子准备第一台 Linux 电脑，应该怎样配置系统、工具和探索空间？ | 227 | 300 | 2025-11-09 |

### 2025-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Merry Christmas!](https://news.ycombinator.com/item?id=46380168) | HN 用户送上圣诞祝福，鼓励休息并关心无法与亲友团聚的人。 | 1958 | 429 | 2025-12-24 |
| 2 | [Ask HN: Should "I asked $AI, and it said" replies be forbidden in HN guidelines?](https://news.ycombinator.com/item?id=46206457) | HN 是否应限制直接贴出“我问了 AI，它说”的回复，讨论评论质量规则。 | 980 | 462 | 2025-12-09 |
| 3 | [Tell HN: HN was down](https://news.ycombinator.com/item?id=46301921) | 发帖者回顾 HN 故障，称登录请求曾返回 502 错误，部分匿名访问仍可用。 | 599 | 327 | 2025-12-17 |
| 4 | [Ask HN: Those making $500/month on side projects in 2025 – Show and tell](https://news.ycombinator.com/item?id=46307973) | 2025 年副项目月入五百美元的交流帖，分享小型产品的收入与经营经验。 | 485 | 560 | 2025-12-18 |
| 5 | [Ask HN: What are the best engineering blogs with real-world depth?](https://news.ycombinator.com/item?id=46363921) | 哪些工程博客真正深入真实问题，寻找有实践细节的高质量技术文章。 | 474 | 141 | 2025-12-23 |
| 6 | [Ask HN: How can I get better at using AI for programming?](https://news.ycombinator.com/item?id=46255285) | 在个人项目中尝试 AI 编程却遇到瓶颈，怎样提高使用模型开发的能力？ | 471 | 469 | 2025-12-13 |
| 7 | [Tell HN: Happy New Year](https://news.ycombinator.com/item?id=46443744) | 社区新年祝福帖，向 HN 读者送上对新一年的问候。 | 444 | 206 | 2025-12-31 |
| 8 | [Ask HN: What Are You Working On? (December 2025)](https://news.ycombinator.com/item?id=46264491) | 2025 年 12 月项目交流帖，分享年末正在做的项目和新想法。 | 439 | 1468 | 2025-12-14 |
| 9 | [Regarding Thien-Thi Nguyen](https://news.ycombinator.com/item?id=46102451) | Thien-Thi Nguyen 的女儿向社区致谢，感谢大家在父亲去世后的温暖留言。 | 371 | 9 | 2025-12-01 |
| 10 | [Ask HN: What did you read in 2025?](https://news.ycombinator.com/item?id=46391572) | 2025 年你读了什么，分享报刊、技术文章与留下深刻印象的书。 | 340 | 448 | 2025-12-26 |

### 2026-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Could you share your personal website here?](https://news.ycombinator.com/item?id=46618714) | 发帖者邀请展示个人网站，计划整理成由社区维护的网站目录。 | 950 | 2386 | 2026-01-14 |
| 2 | [Ask HN: How can we solve the loneliness epidemic?](https://news.ycombinator.com/item?id=46635345) | 越来越多人无人可聊，社会该怎样缓解各年龄层的孤独问题？ | 799 | 1245 | 2026-01-15 |
| 3 | [Bending Spoons laid off almost everybody at Vimeo yesterday](https://news.ycombinator.com/item?id=46707699) | 发帖者称 Bending Spoons 大幅裁减 Vimeo 团队，工程部门所剩人员极少。 | 471 | 505 | 2026-01-21 |
| 4 | [Ask HN: Do you have any evidence that agentic coding works?](https://news.ycombinator.com/item?id=46691243) | 自动代理编程是否真的有效，发帖者寻找宣传与个人体验之外的可靠证据。 | 461 | 455 | 2026-01-20 |
| 5 | [RevisionDojo, a YC startup, is running astroturfing campaigns targeting kids](https://news.ycombinator.com/item?id=46499976) | 发帖者指控 RevisionDojo 面向学生开展伪装成用户推荐的营销活动。 | 454 | 88 | 2026-01-05 |
| 6 | [Ask HN: How are you doing RAG locally?](https://news.ycombinator.com/item?id=46616529) | 怎样少依赖外部组件，在本地为内部代码或复杂资料搭建检索增强生成？ | 413 | 156 | 2026-01-14 |
| 7 | [Ask HN: Who is hiring? (January 2026)](https://news.ycombinator.com/item?id=46466074) | 2026 年 1 月招聘集中帖，企业集中发布岗位与工作地点要求。 | 360 | 401 | 2026-01-02 |
| 8 | [The $LANG Programming Language](https://news.ycombinator.com/item?id=46610557) | 作者整理 HN 历来以编程语言命名的帖子，方便发现有趣的新语言。 | 267 | 72 | 2026-01-14 |
| 9 | [Ask HN: What's the current best local/open speech-to-speech setup?](https://news.ycombinator.com/item?id=46731068) | 想实现完全本地、低延迟的语音助手，当前语音到语音方案应如何搭配？ | 265 | 71 | 2026-01-23 |
| 10 | [Ask HN: What Are You Working On? (January 2026)](https://news.ycombinator.com/item?id=46577242) | 2026 年 1 月项目交流帖，展示新年正在构建的东西与计划。 | 256 | 883 | 2026-01-11 |

### 2026-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Thank HN: You helped save 33,241 lives](https://news.ycombinator.com/item?id=47049824) | Watsi 团队回顾十三年前从 Show HN 起步，称社区支持帮助挽救数万生命。 | 1148 | 112 | 2026-02-17 |
| 2 | [Tell HN: YC companies scrape GitHub activity, send spam emails to users](https://news.ycombinator.com/item?id=47163885) | 发帖者称 YC 公司抓取 GitHub 活动发送营销邮件，质疑这种获客方式。 | 688 | 259 | 2026-02-26 |
| 3 | [Ralph Giles Passed Away (Xiph.org\| Rust@Mozilla \| Ghostscript)](https://news.ycombinator.com/item?id=46996490) | 帖子通报参与 Xiph.org、Mozilla Rust 与 Ghostscript 的 Ralph Giles 去世。 | 519 | 28 | 2026-02-12 |
| 4 | [Ask HN: What Are You Working On? (February 2026)](https://news.ycombinator.com/item?id=46937696) | 2026 年 2 月项目交流帖，介绍近期进展与正在思考的新方向。 | 334 | 1157 | 2026-02-08 |
| 5 | [Ask HN: Who is hiring? (February 2026)](https://news.ycombinator.com/item?id=46857488) | 2026 年 2 月招聘集中帖，查看公司职位、工作地点及远程条件。 | 317 | 592 | 2026-02-02 |
| 6 | [Ask HN: How to get started with robotics as a hobbyist?](https://news.ycombinator.com/item?id=46934622) | 想找比纯软件更有实体感的爱好，机器人爱好者该如何入门？ | 202 | 95 | 2026-02-08 |
| 7 | [Kernighan on Programming](https://news.ycombinator.com/item?id=46857444) | 帖子引用 Kernighan 关于调试难于写代码的名言，反思刻意写复杂代码的代价。 | 172 | 62 | 2026-02-02 |
| 8 | [Launch HN: Omnara (YC S25) – Run Claude Code and Codex from Anywhere](https://news.ycombinator.com/item?id=46991591) | Omnara 让开发者通过网页和手机连接本机的 Claude Code、Codex 会话，离开书桌也能参与。 | 147 | 161 | 2026-02-12 |
| 9 | [1Password pricing increasing 20% in March](https://news.ycombinator.com/item?id=47139951) | 发帖者转述 1Password 邮件，称服务价格将在三月上调两成。 | 146 | 209 | 2026-02-24 |
| 10 | [Ask HN: Who wants to be hired? (February 2026)](https://news.ycombinator.com/item?id=46857487) | 2026 年 2 月求职自荐帖，求职者介绍技能、所在地与工作安排偏好。 | 142 | 546 | 2026-02-02 |

### 2026-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [I'm 60 years old. Claude Code has ignited a passion again](https://news.ycombinator.com/item?id=47282777) | 六十岁的作者分享 Claude Code 如何重新点燃自己对编程与创造的热情。 | 1086 | 988 | 2026-03-07 |
| 2 | [Tell HN: Litellm 1.82.7 and 1.82.8 on PyPI are compromised](https://news.ycombinator.com/item?id=47501426) | 发帖者报告 LiteLLM 的两个 PyPI 版本遭入侵，并描述安装时发现的异常代码与资源占用。 | 938 | 500 | 2026-03-24 |
| 3 | [LinkedIn uses 2.4 GB RAM across two tabs](https://news.ycombinator.com/item?id=47561489) | 发帖者通过截图展示 LinkedIn 两个标签页占用约 2.4GB 内存的现象。 | 794 | 456 | 2026-03-29 |
| 4 | [If you don't opt out by Apr 24 GitHub will train on your private repos](https://news.ycombinator.com/item?id=47548243) | 发帖者称 GitHub 私有仓库将默认用于训练，提醒关注退出设置与期限。 | 745 | 316 | 2026-03-27 |
| 5 | [Ask HN: Please restrict new accounts from posting](https://news.ycombinator.com/item?id=47300329) | AI 生成投稿增多，HN 是否应限制新账号发帖以改善内容质量？ | 721 | 515 | 2026-03-08 |
| 6 | [Ask HN: How to Be Alone?](https://news.ycombinator.com/item?id=47296547) | 三十八岁第一次独自生活，发帖者询问如何学会与自己相处。 | 691 | 564 | 2026-03-08 |
| 7 | [An open source alternative to Logi-Plus mouse software](https://news.ycombinator.com/item?id=47368033) | 分享替代罗技鼠标专有软件的开源项目，希望减少后台资源占用和遥测依赖。 | 443 | 151 | 2026-03-13 |
| 8 | [Ask HN: How is AI-assisted coding going for you professionally?](https://news.ycombinator.com/item?id=47388646) | AI 辅助编码进入实际工作后表现如何，征集超越乐观或悲观口号的亲历体验。 | 434 | 616 | 2026-03-15 |
| 9 | [Tell HN: Chrome says "Suspicious Download" when trying to download yt-dlp](https://news.ycombinator.com/item?id=47588658) | 发帖者称最新版 Chrome 下载 yt-dlp 时显示可疑下载警告。 | 311 | 100 | 2026-03-31 |
| 10 | [Ask HN: What Are You Working On? (March 2026)](https://news.ycombinator.com/item?id=47303111) | 2026 年 3 月项目交流帖，分享当下的作品、进展和新点子。 | 290 | 1131 | 2026-03-09 |

### 2026-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: docker pull fails in spain due to football cloudflare block](https://news.ycombinator.com/item?id=47738883) | 发帖者称西班牙针对足球盗播的 Cloudflare 封锁连带导致 Docker 镜像拉取失败。 | 1157 | 421 | 2026-04-12 |
| 2 | [Anthropic no longer allowing Claude Code subscriptions to be used with OpenClaw](https://news.ycombinator.com/item?id=47633396) | 帖子转述 Anthropic 通知，称 Claude Code 订阅将不再允许用于 OpenClaw。 | 1099 | 827 | 2026-04-03 |
| 3 | [Tell HN: Fiverr left customer files public and searchable](https://news.ycombinator.com/item?id=47769796) | 发帖者称 Fiverr 客户文件公开可被搜索，关注外部文件处理服务带来的泄露。 | 831 | 232 | 2026-04-14 |
| 4 | [Tell HN: An app is silently installing itself on my iPhone every day](https://news.ycombinator.com/item?id=47906253) | Headspace 每天自动出现在 iPhone 上，发帖者寻求解释反复安装的原因。 | 593 | 188 | 2026-04-26 |
| 5 | [Ask HN: Any Interesting Niche Hobbies?](https://news.ycombinator.com/item?id=47654062) | 有哪些有趣又不拥挤的小众爱好，能让新手真正投入并有所参与？ | 483 | 736 | 2026-04-05 |
| 6 | [Ask HN: What Are You Working On? (April 2026)](https://news.ycombinator.com/item?id=47741527) | 2026 年 4 月项目交流帖，介绍正在构建的东西与值得探索的方向。 | 347 | 1177 | 2026-04-12 |
| 7 | [I'm Sick of AI Everything](https://news.ycombinator.com/item?id=47857461) | 作者表达对“万物 AI”的疲惫，讨论产品与信息环境被 AI 占据的感受。 | 346 | 193 | 2026-04-22 |
| 8 | [Is anyone actually using OpenClaw?](https://news.ycombinator.com/item?id=47783940) | 热度很高却身边没人用，OpenClaw 真的有人在实际使用吗？ | 342 | 383 | 2026-04-15 |
| 9 | [Ask HN: How did you land your first projects as a solo engineer/consultant?](https://news.ycombinator.com/item?id=47822940) | 资深工程师转做独立顾问，最初的项目和客户通常从哪里来？ | 302 | 144 | 2026-04-19 |
| 10 | [Ask HN: Who is hiring? (April 2026)](https://news.ycombinator.com/item?id=47601859) | 2026 年 4 月招聘集中帖，企业说明岗位需求与远程条件。 | 280 | 455 | 2026-04-01 |

### 2026-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Rumors of my death are slightly exaggerated](https://news.ycombinator.com/item?id=48037336) | 一位作者澄清自己仍健在，指出 AI 书评捏造了其死讯。 | 1676 | 257 | 2026-05-06 |
| 2 | [Ask HN: We just had an actual UUID v4 collision...](https://news.ycombinator.com/item?id=48060054) | 发帖者称系统真实遇到 UUID v4 碰撞，分享罕见异常并邀请讨论原因。 | 479 | 347 | 2026-05-08 |
| 3 | [Remind HN: Today is Mother's Day, call your moms](https://news.ycombinator.com/item?id=48085384) | 母亲节提醒帖：记得联系妈妈，也向社区中的母亲们送上祝福。 | 377 | 165 | 2026-05-10 |
| 4 | [Ask HN: Who is hiring? (May 2026)](https://news.ycombinator.com/item?id=47975571) | 2026 年 5 月招聘集中帖，集中发布职位、地点与候选人要求。 | 311 | 542 | 2026-05-01 |
| 5 | [Tell HN: Dont use Claude Design, lost access to my projects after unsubscribing](https://news.ycombinator.com/item?id=48128003) | 发帖者称取消订阅后失去 Claude Design 项目访问权，提醒关注数据可取回性。 | 302 | 85 | 2026-05-13 |
| 6 | [Ask HN: What Are You Working On? (May 2026)](https://news.ycombinator.com/item?id=48085993) | 2026 年 5 月项目交流帖，展示近期项目与新想法。 | 290 | 1120 | 2026-05-10 |
| 7 | [I'm Peter Roberts, immigration attorney who does work for YC and startups. AMA](https://news.ycombinator.com/item?id=47975676) | 移民律师 Peter Roberts 再次开放问答，回应社区关心的移民问题。 | 212 | 250 | 2026-05-01 |
| 8 | [Ask HN: Shouldn't Google need to give a public statement about Railway incident?](https://news.ycombinator.com/item?id=48210590) | 围绕 Railway 的 GCP 账号故障，发帖者询问 Google 是否应公开作出说明。 | 180 | 106 | 2026-05-20 |
| 9 | [Ask HN: How to be SOC2 Type 2 compliant as a solo-entreprenuer?](https://news.ycombinator.com/item?id=48145524) | 独立创业者怎样实现 SOC 2 Type II 合规，能否避免高昂审计费用？ | 173 | 138 | 2026-05-15 |
| 10 | [Ask HN: Who wants to be hired? (May 2026)](https://news.ycombinator.com/item?id=47975570) | 2026 年 5 月求职自荐帖，求职者介绍个人技能与工作意向。 | 153 | 533 | 2026-05-01 |

### 2026-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Ask HN: Has anyone replaced Claude/GPT with a local model for daily coding?](https://news.ycombinator.com/item?id=48542100) | 征询是否有人已用本地模型完全替代 Claude 或 GPT 进行日常编程。 | 1318 | 563 | 2026-06-15 |
| 2 | [Please don't spam people looking for employment. It's just cruel](https://news.ycombinator.com/item?id=48370330) | 发帖者求职后收到骚扰信息，呼吁不要向正在找工作的人发送垃圾营销。 | 969 | 273 | 2026-06-02 |
| 3 | [AMA: I'm Eric Ries (The Lean Startup) & Author of New Bestseller Incorruptible](https://news.ycombinator.com/item?id=48477135) | 《精益创业》作者 Eric Ries 开放问答，并介绍新书《Incorruptible》。 | 809 | 579 | 2026-06-10 |
| 4 | [What was your "Oh Shit" moment with GenAI?](https://news.ycombinator.com/item?id=48406174) | 生成式 AI 的哪一次表现让你真正震惊，意识到事情已经发生变化？ | 739 | 1124 | 2026-06-04 |
| 5 | [Why is the HN crowd so anti-AI?](https://news.ycombinator.com/item?id=48420827) | 为什么 HN 读者似乎如此反对 AI，发帖者询问社区态度背后的原因。 | 463 | 765 | 2026-06-06 |
| 6 | [Ask HN: What are tools you have made for yourself since the advent of AI](https://news.ycombinator.com/item?id=48449187) | AI 出现后，你为自己做了哪些工具，邀请展示满足个人需求的作品。 | 445 | 788 | 2026-06-08 |
| 7 | [I indexed 669 GB of my GoPro videos using my M1 Max computer and local ML models](https://news.ycombinator.com/item?id=48528029) | 作者用 M1 Max 和本地模型索引 669GB GoPro 视频，帮助寻找骑行录像片段。 | 439 | 116 | 2026-06-14 |
| 8 | [AWS Bedrock to require sharing data with Anthropic for Mythos and future models](https://news.ycombinator.com/item?id=48473166) | 帖子转述 AWS Bedrock 新要求，称使用部分 Anthropic 模型需同意数据共享。 | 427 | 255 | 2026-06-10 |
| 9 | [Tell HN: Happy Fathers Day to all the fathers, uncles, that role model](https://news.ycombinator.com/item?id=48620502) | 父亲节向父亲、叔伯及承担榜样角色的人致意，感谢他们的陪伴与影响。 | 338 | 57 | 2026-06-21 |
| 10 | [Ask HN: What are you working on? (June 2026)](https://news.ycombinator.com/item?id=48528779) | 2026 年 6 月项目交流帖，分享正在做的东西与计划中的新尝试。 | 312 | 1148 | 2026-06-14 |

### 2026-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [AWS: Inaccurate Estimated Billing Data - $1.7 BILLION](https://news.ycombinator.com/item?id=48945241) | AWS 用户报告收到十七亿美元预估账单，并已提交紧急支持请求。 | 1318 | 754 | 2026-07-17 |
| 2 | [Ask HN: Add flag for AI-generated articles](https://news.ycombinator.com/item?id=48886741) | HN 是否应增加 AI 生成文章标记，让读者更清楚地识别内容来源？ | 1102 | 459 | 2026-07-13 |
| 3 | [Getting GLM 5.2 running on my slow computer](https://news.ycombinator.com/item?id=48842459) | 作者尝试在配置较低的个人电脑上运行 GLM 5.2，关注模型能否避免内存不足。 | 937 | 240 | 2026-07-09 |
| 4 | [Namecheap Gave My Account to an Unverified Third Party Just Because They Asked](https://news.ycombinator.com/item?id=49028037) | 十三年老用户称 Namecheap 未核实第三方身份就移交账号，讲述账户控制权纠纷。 | 498 | 177 | 2026-07-23 |
| 5 | [Ask HN: What Are You Working On? (July 2026)](https://news.ycombinator.com/item?id=48884984) | 2026 年 7 月项目交流帖，邀请展示当前作品和新的探索方向。 | 292 | 1153 | 2026-07-12 |
| 6 | [CheapFoodMap – A map of good meals under $10, crowdsourced verified prices](https://news.ycombinator.com/item?id=49100043) | CheapFoodMap 用众包地图收集十美元以内的本地餐食，让食客查找价格经过核对的平价选择。 | 287 | 258 | 2026-07-29 |
| 7 | [Ask HN: Who is hiring? (July 2026)](https://news.ycombinator.com/item?id=48747976) | 2026 年 7 月招聘集中帖，汇集公司岗位与远程工作的适用地区。 | 247 | 415 | 2026-07-01 |
| 8 | [Ask HN: Is anyone experimenting with different ways of using LLMs for coding?](https://news.ycombinator.com/item?id=48771515) | 使用大语言模型写代码还有哪些新方式，发帖者希望突破常见助手交互模式。 | 212 | 206 | 2026-07-03 |
| 9 | [Ask HN: Any AWS billing issues known? Amazon forecast of 3 billion dollars](https://news.ycombinator.com/item?id=48945681) | 五美元预算却收到三十亿美元支出预测，发帖者询问 AWS 是否有账单故障。 | 206 | 1 | 2026-07-17 |
| 10 | [Ask HN: Who is quitting? (July 2026)](https://news.ycombinator.com/item?id=48760048) | 行业变化令人疲惫，2026 年 7 月有哪些人正在考虑辞职或离开？ | 190 | 149 | 2026-07-02 |

### 2026-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Tell HN: Cloudflare silently injects its analytics when you switch nameservers](https://news.ycombinator.com/item?id=49322107) | 发帖者称切换到 Cloudflare 域名服务器后，网站被自动加入分析脚本。 | 663 | 202 | 2026-08-16 |
| 2 | [Ask HN: Alternatives to GitHub](https://news.ycombinator.com/item?id=49331033) | GitHub 近期频繁中断，是否该迁移，其他代码托管平台有哪些选择？ | 649 | 437 | 2026-08-17 |
| 3 | [Tell HN: GitHub Is Experiencing Degraded Performance](https://news.ycombinator.com/item?id=49330597) | 发帖者记录 GitHub 无法服务请求的故障，并补充官方状态页随后发布的事件信息。 | 562 | 976 | 2026-08-17 |
| 4 | [Ask HN: GitHub employees what's going on? Why?](https://news.ycombinator.com/item?id=49332495) | 发帖者向 GitHub 员工追问：服务故障为何反复发生，内部有什么情况？ | 328 | 262 | 2026-08-17 |
| 5 | [Ask HN: What are you working on? (August 2026)](https://news.ycombinator.com/item?id=49233423) | 2026 年 8 月项目交流帖，聊聊正在开发的作品与最近好奇的主题。 | 325 | 1200 | 2026-08-09 |
| 6 | [Ask HN: Does anyone else feel like nothing matters anymore?](https://news.ycombinator.com/item?id=49340013) | 对软件、学习和求职都失去兴趣，发帖者询问是否有人也觉得一切失去意义。 | 297 | 175 | 2026-08-18 |
| 7 | [GitHub down again? no PR access](https://news.ycombinator.com/item?id=49330632) | 发帖者称 GitHub 再次无法查看拉取请求，而状态页仍显示正常。 | 290 | 2 | 2026-08-17 |
| 8 | [Ask HN: Who is hiring? (August 2026)](https://news.ycombinator.com/item?id=49156683) | 2026 年 8 月招聘集中帖，企业集中发布岗位及地区要求。 | 237 | 368 | 2026-08-03 |
| 9 | [Ask HN: In your experience, what are sound conventions for e-ink UI development?](https://news.ycombinator.com/item?id=49213660) | 开发电子墨水屏网页界面，有哪些经过实践验证的设计规范与注意事项？ | 219 | 73 | 2026-08-07 |
| 10 | [Ask HN: Who wants to be hired? (August 2026)](https://news.ycombinator.com/item?id=49156682) | 2026 年 8 月求职自荐帖，求职者展示技能、所在地与工作偏好。 | 160 | 552 | 2026-08-03 |

## Show HN


### 2006-10

本月原始档案无该类有效主帖。

### 2006-11

本月原始档案无该类有效主帖。

### 2006-12

本月原始档案无该类有效主帖。

### 2007-01

本月原始档案无该类有效主帖。

### 2007-02

本月原始档案无该类有效主帖。

### 2007-03

本月原始档案无该类有效主帖。

### 2007-04

本月原始档案无该类有效主帖。

### 2007-05

本月原始档案无该类有效主帖。

### 2007-06

本月原始档案无该类有效主帖。

### 2007-07

本月原始档案无该类有效主帖。

### 2007-08

本月原始档案无该类有效主帖。

### 2007-09

本月原始档案无该类有效主帖。

### 2007-10

本月原始档案无该类有效主帖。

### 2007-11

本月原始档案无该类有效主帖。

### 2007-12

本月原始档案无该类有效主帖。

### 2008-01

本月原始档案无该类有效主帖。

### 2008-02

本月原始档案无该类有效主帖。

### 2008-03

本月原始档案无该类有效主帖。

### 2008-04

本月原始档案无该类有效主帖。

### 2008-05

本月原始档案无该类有效主帖。

### 2008-06

本月原始档案无该类有效主帖。

### 2008-07

本月原始档案无该类有效主帖。

### 2008-08

本月原始档案无该类有效主帖。

### 2008-09

本月原始档案无该类有效主帖。

### 2008-10

本月原始档案无该类有效主帖。

### 2008-11

本月原始档案无该类有效主帖。

### 2008-12

本月原始档案无该类有效主帖。

### 2009-01

本月原始档案无该类有效主帖。

### 2009-02

本月原始档案无该类有效主帖。

### 2009-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Our new online face recognition demo](https://news.ycombinator.com/item?id=510264) | 在线体验人脸识别，团队公开新的演示页面，展示这项视觉技术。 | 50 | 25 | 2009-03-10 |
| 2 | [Show HN: Code draws better than you](https://news.ycombinator.com/item?id=521135) | 用代码创作绘图作品，作者展示程序生成视觉效果的尝试。 | 19 | 7 | 2009-03-18 |
| 3 | [Show HN: JStartup - Hacker News for news people/journalists](https://news.ycombinator.com/item?id=512080) | JStartup 是面向新闻从业者与记者的信息社区，借鉴 Hacker News 的形式。 | 2 | 0 | 2009-03-11 |

### 2009-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Hacking is not Cracking](https://news.ycombinator.com/item?id=577224) | 作者建立网站区分黑客探索与恶意入侵，希望为澄清概念提供便捷链接。 | 3 | 15 | 2009-04-24 |

### 2009-05

本月原始档案无该类有效主帖。

### 2009-06

本月原始档案无该类有效主帖。

### 2009-07

本月原始档案无该类有效主帖。

### 2009-08

本月原始档案无该类有效主帖。

### 2009-09

本月原始档案无该类有效主帖。

### 2009-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Checkout the app my company helped launch](https://news.ycombinator.com/item?id=870058) | 所在公司参与协助上线的应用亮相，作者请社区看看这次合作成果。 | 1 | 0 | 2009-10-08 |

### 2009-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: How ShoveBox is Handling MacHeist Traffic](https://news.ycombinator.com/item?id=932338) | ShoveBox 分享应对 MacHeist 带来访问流量的做法，供同类产品参考。 | 16 | 6 | 2009-11-10 |
| 2 | [Show HN: I wrote a nifty perl script for managing projects. Thoughts?](https://news.ycombinator.com/item?id=954089) | 作者用 Perl 写了项目管理脚本，展示成果并征求改进建议。 | 3 | 2 | 2009-11-21 |

### 2009-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: my weekend project, jetsetter](https://news.ycombinator.com/item?id=982764) | 频繁旅行催生了周末项目 jetsetter，作者分享这次个人开发尝试。 | 2 | 0 | 2009-12-08 |

### 2010-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: My latest pet project, pydroid](https://news.ycombinator.com/item?id=1043491) | pydroid 是作者近期投入的个人兴趣项目，此次公开给社区查看。 | 109 | 50 | 2010-01-10 |
| 2 | [Show HN: My exercise bike hooked up to an xbox - pedal faster to drive faster.](https://news.ycombinator.com/item?id=1043985) | 把健身单车接入 Xbox，踩得越快，游戏里的车也开得越快。 | 76 | 22 | 2010-01-11 |
| 3 | [Show HN: gleeBox, keyboard glee for your web](https://news.ycombinator.com/item?id=1051967) | gleeBox 尝试让网页操作更多依靠键盘，改善浏览时的交互方式。 | 39 | 31 | 2010-01-14 |
| 4 | [Show HN: My Snake-implemetation, how I taught myself GLSL](https://news.ycombinator.com/item?id=1061953) | 作者通过实现贪吃蛇学习 GLSL，展示边做游戏边掌握着色器的成果。 | 24 | 11 | 2010-01-19 |
| 5 | [Show HN: Check our crowd-sourcing project: One Frame Of Fame.](https://news.ycombinator.com/item?id=1030256) | One Frame Of Fame 团队展示众包项目，邀请更多人参与共同创作。 | 2 | 1 | 2010-01-04 |

### 2010-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: My project for this weekend (with source)](https://news.ycombinator.com/item?id=1125315) | 一个周末完成的小项目连同源码公开，供读者查看实现与成果。 | 120 | 39 | 2010-02-14 |
| 2 | [Show HN: Meet the new Ajax IM (with Node.js)](https://news.ycombinator.com/item?id=1127654) | Ajax IM 展示基于 Node.js 的新版即时通信项目。 | 95 | 18 | 2010-02-15 |
| 3 | [Show HN: My 2-Hour Twilio App](https://news.ycombinator.com/item?id=1125408) | 作者分享两小时内用 Twilio 构建应用的成果，展示快速开发尝试。 | 57 | 24 | 2010-02-14 |
| 4 | [Show HN: PatchBin.com - Pastebin for patches + comments + code review.](https://news.ycombinator.com/item?id=1108016) | PatchBin 把代码补丁分享、评论与代码审查结合，提供面向补丁的 Pastebin。 | 45 | 13 | 2010-02-07 |
| 5 | [Show HN: My Weekend Project -- A Clone of HN Built on Pligg](https://news.ycombinator.com/item?id=1125422) | 作者用 Pligg 做了一个 Hacker News 克隆站，展示周末开发成果。 | 18 | 8 | 2010-02-14 |
| 6 | [Show HN again: My new spec list app, Speckle - now with a homepage.](https://news.ycombinator.com/item?id=1136840) | 规格清单应用 Speckle 新增主页，作者再次展示项目的更新进展。 | 13 | 32 | 2010-02-19 |
| 7 | [Show HN: my story generator using answer-set programming](https://news.ycombinator.com/item?id=1154718) | 作者用答案集编程生成故事，探索逻辑规则如何支持叙事创作。 | 7 | 3 | 2010-02-27 |
| 8 | [Show HN: My 30 minute Aardvark clone](https://news.ycombinator.com/item?id=1125636) | 半小时做出一个 Aardvark 克隆，作者展示快速仿制问答产品的尝试。 | 5 | 0 | 2010-02-15 |
| 9 | [Show HN: Interview Engine](https://news.ycombinator.com/item?id=1132253) | Interview Engine 项目首次在此亮相，作者公开自己的开发成果。 | 5 | 1 | 2010-02-17 |
| 10 | [Show HN: SMS My TV Show (find out when your show is on next)](https://news.ycombinator.com/item?id=1126765) | 通过短信查询电视节目的下次播出时间，SMS My TV Show 提供便捷提醒入口。 | 4 | 6 | 2010-02-15 |

### 2010-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I finally released that sheet music app I keep yammering about](https://news.ycombinator.com/item?id=1196055) | 开发者发布此前多次提及的乐谱应用。 | 318 | 112 | 2010-03-16 |
| 2 | [Show HN:  My weekend project - minimotivation.com](https://news.ycombinator.com/item?id=1198099) | minimotivation.com 是作者的周末小项目，分享一次轻量开发尝试。 | 78 | 59 | 2010-03-17 |
| 3 | [Show HN: Review my startup: Quora, a topic based question and answer site](https://news.ycombinator.com/item?id=1197146) | Quora 团队介绍按主题组织的问答网站，并邀请 HN 用户注册体验。 | 55 | 43 | 2010-03-16 |
| 4 | [Show HN: My Thursday-afternoon project: Notey](https://news.ycombinator.com/item?id=1203854) | Notey 是一个周四下午完成的项目，作者公开成果供社区查看。 | 18 | 31 | 2010-03-19 |
| 5 | [Show HN : I created a PHP Hacker News Clone in 2 hours](https://news.ycombinator.com/item?id=1215357) | 作者称两小时内搭起 PHP 版 Hacker News 克隆，且没有手写代码。 | 18 | 8 | 2010-03-24 |
| 6 | [Show HN: Weekend Project - Japanese Wordsearch Builder](https://news.ycombinator.com/item?id=1191826) | 周末做一个日语找词谜题生成器，把语言练习和文字游戏结合。 | 17 | 13 | 2010-03-15 |
| 7 | [Show HN: My blooper reel tribute to other YC S10 applicants](https://news.ycombinator.com/item?id=1173177) | 作者制作花絮视频，向同样申请 YC S10 的创业者致意。 | 11 | 1 | 2010-03-07 |
| 8 | [Show HN: The result of donating 8 hours design time](https://news.ycombinator.com/item?id=1199990) | 捐出八小时设计时间后完成了什么，作者展示为他人项目提供设计帮助的成果。 | 11 | 6 | 2010-03-17 |
| 9 | [Show HN: omgmetoo, our startup project - a free/busy mobile friend tracker](https://news.ycombinator.com/item?id=1204742) | omgmetoo 用手机展示朋友空闲或忙碌的状态，帮助了解彼此是否方便联系。 | 11 | 5 | 2010-03-19 |
| 10 | [Show HN: Please review my new side project [www.Schmeebs.com]](https://news.ycombinator.com/item?id=1211792) | Schmeebs 尝试融合 Twitter 与 Digg 的交流形式，作者邀请评阅两天做成的原型。 | 8 | 8 | 2010-03-23 |

### 2010-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: CanvasMol molecule viewer (JS + canvas demo)](https://news.ycombinator.com/item?id=1291806) | CanvasMol 用 JavaScript 和 Canvas 展示分子结构，提供浏览器图形演示。 | 72 | 11 | 2010-04-24 |
| 2 | [Show HN: I just made 4sqvision at SuperHappyDevHouse](https://news.ycombinator.com/item?id=1255998) | 作者分享在 SuperHappyDevHouse 活动中完成的 4sqvision 项目。 | 29 | 10 | 2010-04-11 |
| 3 | [Show HN: I just hacked together an app to map broadband speeds.](https://news.ycombinator.com/item?id=1244477) | 把宽带速度绘成地图，作者展示临时开发的网速可视化应用。 | 23 | 17 | 2010-04-06 |
| 4 | [Show HN: Like-o-matic](https://news.ycombinator.com/item?id=1286084) | Like-o-matic 是此次分享的项目名称，原帖向社区公开这项作品。 | 23 | 9 | 2010-04-22 |
| 5 | [Show HN: autolib, the last Python library you'll ever need](https://news.ycombinator.com/item?id=1234167) | autolib 以“最后需要的 Python 库”为口号，展示作者的库设计尝试。 | 13 | 7 | 2010-04-01 |
| 6 | [Show HN: TeamPostgreSQL, neat admin interface for PostgreSQL](https://news.ycombinator.com/item?id=1258808) | TeamPostgreSQL 提供 PostgreSQL 管理界面，作者介绍即将发布的版本。 | 10 | 6 | 2010-04-12 |
| 7 | [Show HN: Super Hacker News adds one page browsing & keyboard navigation to HN](https://news.ycombinator.com/item?id=1283201) | Super Hacker News 为 HN 增加单页浏览和键盘导航，减少阅读时的操作。 | 10 | 3 | 2010-04-21 |
| 8 | [Show HN: A webapp for sharing cocktail napkin drawings](https://news.ycombinator.com/item?id=1248110) | draw.to 让用户在线绘画并分享，适合快速表达草图与随手想法。 | 4 | 3 | 2010-04-07 |
| 9 | [Show HN: Hacker Trends](https://news.ycombinator.com/item?id=1254925) | Hacker Trends 从 HN 热门话题出发，尝试呈现社区关注内容的变化。 | 3 | 4 | 2010-04-10 |
| 10 | [Show HN: See what is trending amongst friends](https://news.ycombinator.com/item?id=1260317) | 看看朋友圈里正在流行什么，作者展示面向好友动态的趋势项目。 | 3 | 2 | 2010-04-12 |

### 2010-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: iPad port of my sheet music app Etude](https://news.ycombinator.com/item?id=1345897) | 乐谱应用 Etude 移植到 iPad，展示平板设备上的阅读与使用体验。 | 94 | 35 | 2010-05-13 |
| 2 | [Show HN: didtheywinornot.com Single Purpose Scores Site](https://news.ycombinator.com/item?id=1367501) | 不想看复杂比分，只想知道赢没赢，这个小站先从棒球结果做起。 | 33 | 49 | 2010-05-21 |
| 3 | [Show HN: Talking to your customers made easy.](https://news.ycombinator.com/item?id=1344683) | 客户沟通能否更轻松，作者用创业项目尝试简化了解用户需求的过程。 | 24 | 19 | 2010-05-13 |
| 4 | [Show HN: maskedmail: craigslist style email anonymizer web service](https://news.ycombinator.com/item?id=1346010) | maskedmail 提供类似 Craigslist 的匿名邮件服务，隐藏通信者的真实地址。 | 16 | 14 | 2010-05-13 |
| 5 | [Show HN: I made this search engine for Reddit using Bing+Reddit API.](https://news.ycombinator.com/item?id=1381172) | 把 Bing 和 Reddit API 结合，作者做了一个面向 Reddit 内容的搜索引擎。 | 16 | 12 | 2010-05-26 |
| 6 | [Show HN: Hacker News like site for South Africa: ZA-Coders](https://news.ycombinator.com/item?id=1314415) | ZA-Coders 把类似 HN 的讨论形式带给南非开发者社区。 | 12 | 11 | 2010-05-03 |
| 7 | [Show HN: HN Recap - Daily, ranked list of articles that hit the front page](https://news.ycombinator.com/item?id=1315417) | HN Recap 每天整理登上首页的文章并排序，方便补看错过的内容。 | 10 | 3 | 2010-05-03 |
| 8 | [Show HN: My notes from the Web 2.0 Expo](https://news.ycombinator.com/item?id=1328267) | 作者公开 Web 2.0 Expo 参会笔记，与没能到场的读者分享见闻。 | 8 | 3 | 2010-05-07 |
| 9 | [Show HN: streamgraph.js, now on github](https://news.ycombinator.com/item?id=1314940) | streamgraph.js 项目在 GitHub 公开，供读者查看与使用其实现。 | 7 | 0 | 2010-05-03 |
| 10 | [Show HN: Switcheroo, my Emacs-ido-mode-inspired alt-tab replacement for Windows](https://news.ycombinator.com/item?id=1316632) | Switcheroo 借鉴 Emacs ido-mode，为 Windows 提供另一种窗口切换方式。 | 6 | 1 | 2010-05-04 |

### 2010-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Mocksup, my mockup prototyping & review webapp](https://news.ycombinator.com/item?id=1471223) | Mocksup 将界面草图、原型制作与评审放到网页上，方便交流设计。 | 95 | 63 | 2010-06-29 |
| 2 | [Show HN: mail2brain, email attachment timesaver](https://news.ycombinator.com/item?id=1472493) | mail2brain 围绕邮件附件提供省时工具，作者展示减少附件处理负担的尝试。 | 44 | 20 | 2010-06-29 |
| 3 | [Show HN: FlyByChat, the site I'm working on. Looking for feedback.](https://news.ycombinator.com/item?id=1447160) | FlyByChat 是作者正在开发的网站，此次公开给社区寻求意见。 | 13 | 22 | 2010-06-20 |
| 4 | [Show HN: Browse, submit and rate interesting Wikipedia articles](https://news.ycombinator.com/item?id=1420735) | 发现有趣的维基百科文章后，可以在这个站点提交、浏览和评分。 | 10 | 2 | 2010-06-10 |
| 5 | [Show HN: our (bootstrapped) Real Time Analytics + Social Media Monitor Startup](https://news.ycombinator.com/item?id=1434199) | 两位自筹资金的创业者展示 Worldlogger，结合实时分析与社交媒体监测。 | 8 | 3 | 2010-06-15 |
| 6 | [Show HN: Songbird's first music visualizer](https://news.ycombinator.com/item?id=1398693) | Songbird 迎来首个音乐可视化效果，让声音以动态图像的形式呈现。 | 7 | 1 | 2010-06-02 |
| 7 | [Show HN: the technology and the game I am working on for months](https://news.ycombinator.com/item?id=1421630) | 作者分享连续开发数月的技术与游戏项目，虽未完成也提前公开交流。 | 5 | 1 | 2010-06-10 |
| 8 | [Show HN: I released an update to my Mac App.](https://news.ycombinator.com/item?id=1432757) | 个人 Mac 应用发布了更新，作者向社区介绍这次迭代。 | 2 | 0 | 2010-06-15 |
| 9 | [Show HN: Twitter Photo Mosaic Creator](https://news.ycombinator.com/item?id=1445737) | 把 Twitter 照片拼成马赛克图，作者展示社交图片的创意组合工具。 | 2 | 1 | 2010-06-20 |
| 10 | [Show HN: QR Bookmarklet](https://news.ycombinator.com/item?id=1428737) | 通过浏览器书签脚本使用二维码，作者分享轻量网页工具。 | 1 | 0 | 2010-06-14 |

### 2010-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: HackerNewsers,com, find other hackers near you](https://news.ycombinator.com/item?id=1520916) | HackerNewsers 帮助寻找附近的 HN 用户，让线上讨论延伸到本地交流。 | 221 | 111 | 2010-07-16 |
| 2 | [Show HN: Vittyo, Roll your own video store](https://news.ycombinator.com/item?id=1558305) | Vittyo 让用户搭建自己的视频商店，展示自主经营视频内容的工具。 | 36 | 29 | 2010-07-29 |
| 3 | [Show HN: Created a Job Board for Remote Programming Jobs](https://news.ycombinator.com/item?id=1482469) | 针对社区反复出现的需求，作者创建专门发布远程编程岗位的招聘站。 | 23 | 11 | 2010-07-02 |
| 4 | [Show HN: Turn scripts from userscripts.org into Safari Extensions](https://news.ycombinator.com/item?id=1490066) | 把 userscripts.org 的脚本转换为 Safari 扩展，让现有脚本换个环境继续用。 | 12 | 3 | 2010-07-06 |
| 5 | [Show HN: GridCentric - High Performance Cloud Computing](https://news.ycombinator.com/item?id=1548495) | GridCentric 展示高性能云计算项目，介绍面向云端计算的技术方案。 | 10 | 3 | 2010-07-26 |
| 6 | [Show HN: http://hackerbra.in - fast and smart hacker news](https://news.ycombinator.com/item?id=1533087) | hackerbra.in 根据作者阅读习惯重新组织 HN，尝试更快地浏览社区内容。 | 9 | 6 | 2010-07-20 |
| 7 | [Show HN : Review our product for conducting online coding tests](https://news.ycombinator.com/item?id=1558424) | 在线执行编程测试，团队请社区评估这款面向代码考核的产品。 | 8 | 1 | 2010-07-29 |
| 8 | [Show HN: My Greg's Pulse. Get text message updates when stuff online changes](https://news.ycombinator.com/item?id=1528099) | Greg's Pulse 在网络内容发生变化时发送短信，让用户及时获知更新。 | 4 | 12 | 2010-07-19 |
| 9 | [Show HN: TextMate CSS3 Bundle](https://news.ycombinator.com/item?id=1503529) | 作者制作 TextMate 的 CSS3 功能包，为编辑器补充相关开发支持。 | 2 | 0 | 2010-07-10 |
| 10 | [Show HN: Web^2, a tiling window manager for the Internet](https://news.ycombinator.com/item?id=1549174) | Web^2 把平铺窗口管理的思路带到网页内容，尝试组织互联网浏览空间。 | 2 | 1 | 2010-07-26 |

### 2010-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: My &lt;canvas&gt;-based, Photoshop-esque JavaScript color picker](https://news.ycombinator.com/item?id=1634648) | 用 Canvas 制作类似 Photoshop 的颜色选择器，作者展示 JavaScript 交互实现。 | 73 | 35 | 2010-08-26 |
| 2 | [Show HN: A new book notification service I just launched](https://news.ycombinator.com/item?id=1614160) | Any new books? 提供新书通知服务，帮助读者发现刚出版的书。 | 41 | 42 | 2010-08-18 |
| 3 | [Show HN: Pomodoro-Timer](https://news.ycombinator.com/item?id=1626239) | 受 HN 推荐的番茄工作法启发，作者做了一个简洁的在线计时器。 | 31 | 16 | 2010-08-23 |
| 4 | [Show HN: VoiceForms 4000, my submission to the Wufoo API contest](https://news.ycombinator.com/item?id=1650317) | VoiceForms 4000 是面向 Wufoo API 比赛的作品，展示语音与表单结合的尝试。 | 27 | 9 | 2010-08-31 |
| 5 | [Show HN: I took your advice and prldr is now a visual RSS reader](https://news.ycombinator.com/item?id=1646290) | 听取社区建议后，prldr 调整成可视化 RSS 阅读器，再次展示新版。 | 15 | 8 | 2010-08-30 |
| 6 | [Show HN: My social music app](https://news.ycombinator.com/item?id=1582599) | 把音乐与社交放进同一个应用，作者分享自己的产品开发尝试。 | 13 | 29 | 2010-08-06 |
| 7 | [Show HN: The real time community search engine](https://news.ycombinator.com/item?id=1586674) | 删去其他功能后，作者先上线核心的实时社区搜索引擎。 | 12 | 13 | 2010-08-09 |
| 8 | [Show HN: prldr.com, preloading the internet, my weekend project.](https://news.ycombinator.com/item?id=1628208) | prldr 是作者周末开发的网络预加载项目，尝试改变网页内容的获取体验。 | 10 | 11 | 2010-08-23 |
| 9 | [Show HN: LivGiv - Be more than a Face in a Book](https://news.ycombinator.com/item?id=1589180) | LivGiv 以超越头像式关系为目标，作者展示自己的社交平台设想。 | 9 | 22 | 2010-08-09 |
| 10 | [Show HN: swytch.net - my attempt at a social network](https://news.ycombinator.com/item?id=1579400) | swytch.net 是作者开发一个多月的小型社交网络，开放给社区体验。 | 7 | 7 | 2010-08-05 |

### 2010-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Koi - a programming language that teaches language implementation.](https://news.ycombinator.com/item?id=1741367) | Koi 既是一门编程语言，也被用来讲解语言本身如何实现。 | 70 | 12 | 2010-09-29 |
| 2 | [Show HN: Streak.ly tracks what you do daily and I'd love feedback on the concept](https://news.ycombinator.com/item?id=1665467) | Streak.ly 记录每天做过的事，作者希望验证持续追踪日常行为的想法。 | 54 | 48 | 2010-09-05 |
| 3 | [Show HN: my regular expression example match generator](https://news.ycombinator.com/item?id=1725447) | 给定正则表达式后生成匹配示例，帮助理解与检查复杂的模式规则。 | 46 | 33 | 2010-09-24 |
| 4 | [Show HN: Elect.io, my side-project that provides objective candidate information](https://news.ycombinator.com/item?id=1697489) | Elect.io 尝试提供客观的候选人信息，帮助选民了解参选者。 | 16 | 23 | 2010-09-16 |
| 5 | [Show HN: ImpromptuDo.com the real time location based activity partner finder](https://news.ycombinator.com/item?id=1659528) | ImpromptuDo 按位置实时寻找一起活动的人，把临时兴趣变成线下安排。 | 15 | 5 | 2010-09-03 |
| 6 | [Show HN: Instant Search for iPad](https://news.ycombinator.com/item?id=1739684) | 作者把即时搜索体验带到 iPad，展示适配平板的搜索项目。 | 10 | 4 | 2010-09-29 |
| 7 | [Show HN: Review our public website?](https://news.ycombinator.com/item?id=1740633) | 作者请读者先看公开网站，检验页面能否独立讲清产品要做什么。 | 10 | 13 | 2010-09-29 |
| 8 | [Show HN: My Food Pairings Mobile App](https://news.ycombinator.com/item?id=1666716) | 受《风味圣经》启发，作者制作食材搭配手机应用，帮助组合烹饪原料。 | 8 | 10 | 2010-09-06 |
| 9 | [Show HN: an order-preserving JSON encoding (so byte-order == value-order)](https://news.ycombinator.com/item?id=1726566) | 一种保序 JSON 编码，让编码后的字节排序与原始值的排序一致。 | 7 | 0 | 2010-09-25 |
| 10 | [Show HN: Facster.com technology demonstration](https://news.ycombinator.com/item?id=1715461) | Facster 以原型网站展示背后的技术，作者希望讨论实现而非仅看成品。 | 6 | 2 | 2010-09-22 |

### 2010-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I asked an HN member for feedback and she blew my mind](https://news.ycombinator.com/item?id=1836538) | 一位创业者分享 HN 成员为其网站文案提供的详尽反馈。 | 453 | 120 | 2010-10-26 |
| 2 | [Show HN: Hacker News, automagically organized](https://news.ycombinator.com/item?id=1804261) | 让 Hacker News 自动整理起来，作者尝试减少人工筛选与组织内容的负担。 | 274 | 36 | 2010-10-18 |
| 3 | [Show HN: Review my project: MarkUp, a tool to draw on any webpage.](https://news.ycombinator.com/item?id=1768345) | MarkUp 让用户直接在任意网页上绘画标注，帮助交流页面问题与修改意见。 | 90 | 54 | 2010-10-07 |
| 4 | [Show HN: Couldn't sleep; added 960gs support to jMockups](https://news.ycombinator.com/item?id=1838198) | 睡不着时给 jMockups 加上 960gs 支持，作者分享设计工具的小更新。 | 75 | 29 | 2010-10-27 |
| 5 | [Show HN: Coding noob - first weekend project](https://news.ycombinator.com/item?id=1761925) | 编程新手公开第一个周末作品，记录开始独立动手构建的尝试。 | 69 | 54 | 2010-10-05 |
| 6 | [Show HN: My HTML5 Sokoban game](https://news.ycombinator.com/item?id=1772790) | 用 HTML5 实现推箱子，作者展示可在浏览器中游玩的经典益智游戏。 | 40 | 17 | 2010-10-08 |
| 7 | [Show HN: A/Bingo for PHP](https://news.ycombinator.com/item?id=1805623) | A/Bingo 的 PHP 版本公开亮相，开发者可以查看这一语言环境中的实现。 | 33 | 12 | 2010-10-18 |
| 8 | [Show HN: a compiler from Python syntax to JavaScript syntax (like CoffeeScript)](https://news.ycombinator.com/item?id=1848643) | 把 Python 语法编译为 JavaScript，作者探索类似 CoffeeScript 的语言转换路线。 | 32 | 18 | 2010-10-29 |
| 9 | [Show HN: Condensr.com, Yelp Snippet Summarization](https://news.ycombinator.com/item?id=1816652) | Condensr 汇总 Yelp 评论片段，尝试压缩用户评价中的关键信息。 | 27 | 6 | 2010-10-21 |
| 10 | [Show HN: 415-483-1860 twilio-translator](https://news.ycombinator.com/item?id=1828304) | 作者在 API 活动中用数小时制作 Twilio 翻译项目，公开号码供体验。 | 21 | 13 | 2010-10-25 |

### 2010-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Spreadsheets using Python - Have you seen this?](https://news.ycombinator.com/item?id=1884896) | 用 Python 操作电子表格，作者分享把脚本与表格工作结合的项目。 | 97 | 47 | 2010-11-09 |
| 2 | [Show HN: A successful penny-auction bot](https://news.ycombinator.com/item?id=1931051) | 一分钱拍卖能否由程序代劳，作者展示自称已经奏效的自动竞拍机器人。 | 74 | 12 | 2010-11-22 |
| 3 | [Show HN: Our little html5/js dungeon crawler.](https://news.ycombinator.com/item?id=1882514) | 用 HTML5 和 JavaScript 制作小型地牢探索游戏，团队公开可玩成果。 | 71 | 38 | 2010-11-08 |
| 4 | [Show HN: We just launched a Bayesian-Based Sentiment Tracker](https://news.ycombinator.com/item?id=1923607) | 团队上线基于贝叶斯方法的情感追踪工具，尝试识别文本情绪倾向。 | 42 | 20 | 2010-11-20 |
| 5 | [Show HN: Fulltext Search for the Leaked US Embassy Cables](https://news.ycombinator.com/item?id=1949063) | 把泄露的美国使馆电报做成全文搜索，帮助按关键词查找其中内容。 | 42 | 4 | 2010-11-29 |
| 6 | [Show HN: Cyberspace - my new web browser for iOS](https://news.ycombinator.com/item?id=1953682) | Cyberspace 是作者为 iOS 制作的网页浏览器，展示移动浏览的新尝试。 | 41 | 28 | 2010-11-30 |
| 7 | [Show HN: Our telepresence setup](https://news.ycombinator.com/item?id=1915980) | 作者公开自己的远程临场设备配置，分享如何实现异地参与体验。 | 38 | 19 | 2010-11-17 |
| 8 | [Show HN: my new app is fast user switching for the iPad (sort-of)](https://news.ycombinator.com/item?id=1940129) | 让 iPad 近似拥有快速用户切换，作者探索同一设备供多人使用的交互。 | 38 | 25 | 2010-11-25 |
| 9 | [Show HN: Syncpad, like Facetime but for drawings](https://news.ycombinator.com/item?id=1951196) | Syncpad 把远程交流的媒介换成绘画，让双方通过图画保持同步。 | 34 | 13 | 2010-11-29 |
| 10 | [Show HN: A/Bingo for ASP.NET](https://news.ycombinator.com/item?id=1872465) | 作者将 A/Bingo 带到 ASP.NET 环境，分享这一移植版本。 | 32 | 24 | 2010-11-05 |

### 2010-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Radi, my HTML5 content creation app (Mac)](https://news.ycombinator.com/item?id=2040844) | Radi 是 Mac 上的 HTML5 内容创作应用，帮助制作网页内容。 | 297 | 38 | 2010-12-26 |
| 2 | [Show HN: I wrote my own Delicious clone](https://news.ycombinator.com/item?id=2018563) | 作者制作自己的 Delicious 克隆，尝试重建熟悉的书签收藏体验。 | 138 | 70 | 2010-12-18 |
| 3 | [Show HN: A Genetic Algorithm I wrote in JavaScript to evolve "Hello World"](https://news.ycombinator.com/item?id=2002673) | 用 JavaScript 遗传算法逐步演化出 Hello World，展示优化过程的趣味实验。 | 109 | 38 | 2010-12-14 |
| 4 | [Show HN: Analysis of how long do items survive on the "New" page](https://news.ycombinator.com/item?id=2022547) | HN 投稿在最新页能停留多久，作者分析新内容获得曝光的时间。 | 92 | 21 | 2010-12-19 |
| 5 | [Show HN: My first significant project with Backbone.js - a simple online editor](https://news.ycombinator.com/item?id=2048033) | 首次深入使用 Backbone.js，作者通过简单在线编辑器练习构建应用。 | 91 | 36 | 2010-12-29 |
| 6 | [Show HN: Profile Collage for Facebook](https://news.ycombinator.com/item?id=2009352) | 把 Facebook 个人资料做成拼贴图，作者展示社交图片创作工具。 | 77 | 42 | 2010-12-15 |
| 7 | [Show HN: Gamification.org - Open Source Game Mechanics](https://news.ycombinator.com/item?id=1958728) | Gamification.org 围绕开源游戏机制组织内容，分享游戏化设计的尝试。 | 76 | 25 | 2010-12-01 |
| 8 | [Show HN: drag-drop file uploading for the whole web (Firefox/Chrome)](https://news.ycombinator.com/item?id=2045858) | 为 Firefox 和 Chrome 增加拖放上传功能，尝试让文件上传遍及网页。 | 66 | 10 | 2010-12-28 |
| 9 | [Show HN: New Lisp data structure](https://news.ycombinator.com/item?id=1959896) | 作者提出一种新的 Lisp 数据结构，邀请社区查看并讨论设计。 | 62 | 45 | 2010-12-01 |
| 10 | [Show HN: Crondom](https://news.ycombinator.com/item?id=2011300) | Crondom 是作者公开展示的新项目，供读者进一步了解与交流。 | 62 | 56 | 2010-12-16 |

### 2011-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Google search blacklist](https://news.ycombinator.com/item?id=2060994) | 作者制作 Google 搜索黑名单工具，回应社区对搜索质量的抱怨。 | 119 | 29 | 2011-01-02 |
| 2 | [Show HN: Pocket - my first app ever](https://news.ycombinator.com/item?id=2112144) | Pocket 是作者发布的第一款应用，分享从想法走向成品的起点。 | 99 | 65 | 2011-01-17 |
| 3 | [Show HN: Fqwiki - Qwiki cloned with a single HTML file](https://news.ycombinator.com/item?id=2131563) | Fqwiki 用单个 HTML 文件仿制 Qwiki，展示极简实现的尝试。 | 96 | 14 | 2011-01-23 |
| 4 | [Show HN: cubeduel (our side project)](https://news.ycombinator.com/item?id=2101157) | cubeduel 是团队的副项目，此次公开分享共同开发的阶段成果。 | 95 | 47 | 2011-01-13 |
| 5 | [Show HN: A Wiki written in 80 lines of JavaScript](https://news.ycombinator.com/item?id=2113258) | 仅用八十行 JavaScript 实现 Wiki，作者展示精简代码的成果。 | 79 | 41 | 2011-01-17 |
| 6 | [Show HN: Hacker News Map 2011](https://news.ycombinator.com/item?id=2159088) | 2011 年 Hacker News 地图项目，把社区相关信息放到地图上展示。 | 77 | 36 | 2011-01-30 |
| 7 | [Show HN: WerdMerge: A Portmanteau Generator With Phonemes](https://news.ycombinator.com/item?id=2128752) | WerdMerge 根据音素生成混成词，帮助把不同词语拼出新名字。 | 71 | 31 | 2011-01-21 |
| 8 | [Show HN: EDW, quantitative analytics, machine learning.](https://news.ycombinator.com/item?id=2134433) | EDW 围绕定量分析与机器学习展开，作者公开项目供社区查看。 | 70 | 18 | 2011-01-24 |
| 9 | [Show HN: 3DTin - 3D modelling in browser](https://news.ycombinator.com/item?id=2088213) | 3DTin 让用户在浏览器中进行三维建模，无需把创作局限在桌面软件。 | 62 | 16 | 2011-01-10 |
| 10 | [Show HN my christmas project: Focus.app, cut off your Internet so you can focus](https://news.ycombinator.com/item?id=2068948) | Focus.app 通过断开网络帮助专注，是作者圣诞假期完成的项目。 | 61 | 39 | 2011-01-04 |

### 2011-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Our new $149 hackable Bluetooth wristwatch ](https://news.ycombinator.com/item?id=2221579) | 展示售价 149 美元、可供改造的蓝牙腕表。 | 460 | 143 | 2011-02-15 |
| 2 | [Show HN: HackerBooks.com](https://news.ycombinator.com/item?id=2249390) | HackerBooks.com 作为新站点向社区亮相，作者邀请读者查看自己的作品。 | 351 | 140 | 2011-02-22 |
| 3 | [Show HN: My 4-hour project, already profitable](https://news.ycombinator.com/item?id=2173155) | 四小时完成的项目已经开始盈利，作者分享快速上线后的早期进展。 | 323 | 141 | 2011-02-03 |
| 4 | [Show HN: Breakup Notifier](https://news.ycombinator.com/item?id=2243650) | Breakup Notifier 围绕分手状态提供通知，展示这一别出心裁的小工具。 | 264 | 118 | 2011-02-21 |
| 5 | [Show HN: Remote Jobs (our answer to "Who Is Hiring Remote Workers?")](https://news.ycombinator.com/item?id=2250526) | Remote Jobs 回应社区对远程工作的需求，连接远程岗位与求职者。 | 217 | 83 | 2011-02-22 |
| 6 | [Show HN:  What Do You Think Of My Resume?](https://news.ycombinator.com/item?id=2233700) | 作者公开个人简历，请社区从求职展示的角度给予意见。 | 141 | 79 | 2011-02-18 |
| 7 | [Show HN: my new project, an anti-snub dating site](https://news.ycombinator.com/item?id=2179649) | 避免在网上约会时被冷落，作者围绕这一目标创建新的交友网站。 | 119 | 113 | 2011-02-04 |
| 8 | [Show HN: Pen.io](https://news.ycombinator.com/item?id=2199901) | Pen.io 是作者此次公开的网络项目，供社区查看并提出反馈。 | 108 | 96 | 2011-02-09 |
| 9 | [Show HN: I'll help you name your next startup/product for $50](https://news.ycombinator.com/item?id=2257572) | 花五十美元请人帮新公司或产品起名，作者以周末项目验证命名服务。 | 98 | 93 | 2011-02-24 |
| 10 | [Show HN: I've always wanted a Y Combinator shirt, so I made one.](https://news.ycombinator.com/item?id=2232951) | 想要一件 Y Combinator 衬衫却没找到，作者决定自己做出来。 | 80 | 32 | 2011-02-17 |

### 2011-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: My collection of web-apps that I'm finally comfortable in sharing](https://news.ycombinator.com/item?id=2333570) | 积累了一组终于满意的 Web 应用后，作者把自己的作品集合公开。 | 238 | 82 | 2011-03-16 |
| 2 | [Show HN: "Never wait on hold again" service built with Rails and Twilio ](https://news.ycombinator.com/item?id=2285594) | 用 Rails 和 Twilio 制作免去电话等待的服务，减少用户被挂在线上的时间。 | 216 | 83 | 2011-03-03 |
| 3 | [Show HN: Beginning Android for iOS Developers](https://news.ycombinator.com/item?id=2297902) | 面向 iOS 开发者介绍 Android 入门，帮助已有移动经验的人转向新平台。 | 197 | 23 | 2011-03-07 |
| 4 | [Show HN: My Node.js two weekend project. Color palettes from Flickr images.](https://news.ycombinator.com/item?id=2322985) | 两周末用 Node.js 完成工具，从 Flickr 照片中提取可用的配色方案。 | 159 | 63 | 2011-03-14 |
| 5 | [Show HN: Readability-like API Using Machine Learning](https://news.ycombinator.com/item?id=2310852) | 用机器学习制作类似 Readability 的 API，尝试提取适合阅读的网页内容。 | 151 | 49 | 2011-03-10 |
| 6 | [Show HN: I made a better interface for Google Tasks and I can't go back](https://news.ycombinator.com/item?id=2278860) | 作者给 Google Tasks 做了替代界面，希望改善自己每天管理任务的体验。 | 122 | 54 | 2011-03-02 |
| 7 | [Show HN: CaptainObvio.us - a place to share ideas](https://news.ycombinator.com/item?id=2365996) | CaptainObvio.us 提供分享想法的空间，让点子有地方被看见和讨论。 | 109 | 72 | 2011-03-24 |
| 8 | [Show HN: Notepag.es - Markdown/LaTeX editor for quick technical documents.](https://news.ycombinator.com/item?id=2368530) | Notepag.es 结合 Markdown 与 LaTeX，帮助快速编写技术文档。 | 100 | 20 | 2011-03-25 |
| 9 | [Show HN: Home automation and lighting control with Kinect](https://news.ycombinator.com/item?id=2303395) | 把 Kinect 用于家庭自动化和灯光控制，尝试用身体动作操控环境。 | 98 | 31 | 2011-03-09 |
| 10 | [Show HN: Phoneify - 20 hours with Rails 3 & Twilio](https://news.ycombinator.com/item?id=2289635) | Phoneify 是作者用 Rails 3 和 Twilio 投入约二十小时制作的项目。 | 95 | 57 | 2011-03-04 |

### 2011-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: my weekend project, Gumroad](https://news.ycombinator.com/item?id=2406614) | 作者公开周末项目 Gumroad，分享产品最初亮相社区的时刻。 | 396 | 202 | 2011-04-04 |
| 2 | [Show HN: Let's end the Programmer Salary Taboo](https://news.ycombinator.com/item?id=2441888) | 作者希望打破程序员薪资禁忌，推动更公开地讨论开发者收入。 | 278 | 147 | 2011-04-13 |
| 3 | [Show HN: My weekend project, tracking the services you can't have in Canada](https://news.ycombinator.com/item?id=2404752) | 记录哪些网络服务在加拿大不可用，作者把地区限制整理成周末项目。 | 212 | 118 | 2011-04-04 |
| 4 | [Show HN: made a html5 game, polished it many many times](https://news.ycombinator.com/item?id=2453554) | 反复打磨自制 HTML5 游戏后，作者展示不依赖昂贵工具的创作成果。 | 211 | 114 | 2011-04-16 |
| 5 | [Show HN: CSS3 Animated Glowing Forms](https://news.ycombinator.com/item?id=2399927) | 用 CSS3 为表单制作发光动画，作者展示网页视觉效果的实现。 | 182 | 57 | 2011-04-02 |
| 6 | [Show HN: Hacker Typer [joke]](https://news.ycombinator.com/item?id=2480946) | Hacker Typer 让随意敲键盘也像电影黑客高速编程，是个趣味恶搞工具。 | 160 | 34 | 2011-04-25 |
| 7 | [Show HN: An isometric marble run build in CoffeeScript](https://news.ycombinator.com/item?id=2459406) | 用 CoffeeScript 制作等距视角滚球轨道，展示浏览器里的小型游戏实验。 | 141 | 25 | 2011-04-18 |
| 8 | [Show HN: Codr.cc - Etherpad meets Pastebin Meets Notepad.cc: live code sharing](https://news.ycombinator.com/item?id=2481287) | Codr.cc 融合协作编辑、代码粘贴与在线记事，让代码分享更实时。 | 135 | 79 | 2011-04-25 |
| 9 | [Show HN: jsgif: A GIF player in JavaScript](https://news.ycombinator.com/item?id=2406256) | jsgif 用 JavaScript 播放 GIF，探索在网页中控制动画图像。 | 128 | 24 | 2011-04-04 |
| 10 | [Show HN: Amazon EC2 instance comparison table](https://news.ycombinator.com/item?id=2473941) | 把 Amazon EC2 各类实例放进比较表，帮助选择合适的云主机规格。 | 122 | 33 | 2011-04-22 |

### 2011-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: New platform for finding work - $2000 project minimum](https://news.ycombinator.com/item?id=2540909) | 最低两千美元的项目才能入场，新的找工作平台尝试提高合作门槛。 | 195 | 111 | 2011-05-12 |
| 2 | [Show HN: IMDb Top 250 available on Netflix Instant](https://news.ycombinator.com/item?id=2595407) | 从 IMDb 前二百五十名电影中筛出 Netflix Instant 可看的影片，方便选片。 | 195 | 67 | 2011-05-28 |
| 3 | [Show HN: Machine learning cheat sheet](https://news.ycombinator.com/item?id=2515612) | 作者整理机器学习速查表，帮助快速回顾常用概念与方法。 | 166 | 13 | 2011-05-04 |
| 4 | [Show HN: I wrote a .NET to JS compiler. Here's an XNA demo compiled to JS.](https://news.ycombinator.com/item?id=2602340) | 作者编写 .NET 到 JavaScript 编译器，并用转换后的 XNA 演示展示效果。 | 103 | 18 | 2011-05-31 |
| 5 | [Show HN: Fitocracy, an RPG for fitness](https://news.ycombinator.com/item?id=2553181) | Fitocracy 把健身变成角色扮演式成长，用社交与游戏机制激励锻炼。 | 102 | 65 | 2011-05-16 |
| 6 | [Show HN: This weird bug is probably present in your Nginx configuration.](https://news.ycombinator.com/item?id=2552395) | 作者指出一个可能藏在 Nginx 配置中的古怪问题，提醒使用者检查。 | 100 | 20 | 2011-05-16 |
| 7 | [Show HN: My embeddable C/C++ webserver](https://news.ycombinator.com/item?id=2520882) | 一个可嵌入应用的 C/C++ Web 服务器，作者展示其轻量集成方案。 | 84 | 44 | 2011-05-06 |
| 8 | [Show HN: Gitalytics.com - Quicker Way to check someone's github profile](https://news.ycombinator.com/item?id=2519082) | Gitalytics 汇总 GitHub 用户信息，帮助更快了解某人的开发者资料。 | 83 | 28 | 2011-05-05 |
| 9 | [Show HN: Minimal Lisp in ~70 lines of Haskell](https://news.ycombinator.com/item?id=2502173) | 约七十行 Haskell 写出极简 Lisp，展示小型语言解释器的实现。 | 76 | 23 | 2011-05-01 |
| 10 | [Show HN: I Made this Y Combinator T-Shirt (Words from PG's Essays)](https://news.ycombinator.com/item?id=2581041) | 把 Paul Graham 文章里的词语印成 Y Combinator T 恤，作者展示自制作品。 | 72 | 44 | 2011-05-24 |

### 2011-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: HN Trends - like Google Trends, but for Hacker News](https://news.ycombinator.com/item?id=2671733) | HN Trends 借鉴 Google Trends，让用户观察 Hacker News 话题的变化。 | 355 | 106 | 2011-06-19 |
| 2 | [Show HN: roll.io eats txt files and shits youtube videos. Useful?](https://news.ycombinator.com/item?id=2665090) | roll.io 把文本文件转成 YouTube 视频，作者询问这种转换能派上什么用场。 | 234 | 104 | 2011-06-17 |
| 3 | [Show HN: Log.io (Realtime log monitoring, powered by node.js + socket.io)](https://news.ycombinator.com/item?id=2622909) | Log.io 结合 Node.js 与 Socket.IO，提供实时查看日志变化的工具。 | 205 | 53 | 2011-06-05 |
| 4 | [Show HN: My weekend project, QR-codes for everybody](https://news.ycombinator.com/item?id=2698494) | 作者用周末时间简化二维码的使用，希望让任何人都容易在各处部署。 | 203 | 65 | 2011-06-26 |
| 5 | [Show HN: Can anonymous chat within identified groups create better discussions?](https://news.ycombinator.com/item?id=2709720) | 身份明确的群组里允许匿名聊天，会不会带来更好的讨论，作者展示实验。 | 165 | 104 | 2011-06-29 |
| 6 | [Show HN: Google Charts done in Canvas, side project](https://news.ycombinator.com/item?id=2622558) | 用 Canvas 重新实现 Google Charts 风格的图表，作者分享个人副项目。 | 143 | 28 | 2011-06-05 |
| 7 | [Show HN: I wrote a co-founder equity calculator over the weekend](https://news.ycombinator.com/item?id=2683104) | 周末写一个联合创始人股权计算器，帮助讨论创业团队的股份分配。 | 136 | 50 | 2011-06-22 |
| 8 | [Show HN: Overlap.me - a new way to meet people & share your identity online](https://news.ycombinator.com/item?id=2710660) | Overlap.me 探索结识他人与展示网络身份的新方式，作者介绍社交项目。 | 112 | 49 | 2011-06-29 |
| 9 | [Show HN: Ducksboard, from nothing to private beta in four months](https://news.ycombinator.com/item?id=2608102) | Ducksboard 从零到封闭测试用了四个月，团队展示这段开发的阶段成果。 | 92 | 34 | 2011-06-01 |
| 10 | [Show HN: Hacker News Instant (3 hour project)](https://news.ycombinator.com/item?id=2621144) | 三个小时完成 Hacker News Instant，作者把即时体验带到 HN 内容浏览。 | 91 | 37 | 2011-06-05 |

### 2011-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I made a Web-based Todo App - used: CSS3 3D transforms, Node.js, love](https://news.ycombinator.com/item?id=2781866) | 结合 CSS3 三维变换与 Node.js，作者制作一个网页待办事项应用。 | 237 | 106 | 2011-07-19 |
| 2 | [Show HN: Monster Coloring Book, my first App just launched. What do you think?](https://news.ycombinator.com/item?id=2829282) | Monster Coloring Book 是作者首款刚上线的应用，让用户为怪兽图案涂色。 | 169 | 67 | 2011-07-31 |
| 3 | [Show HN: A Bitcoin casino with 23 games.](https://news.ycombinator.com/item?id=2782349) | 用比特币参与二十三种赌场游戏，作者展示自己的在线娱乐项目。 | 147 | 72 | 2011-07-19 |
| 4 | [Show HN: Pump, a dead simple Pythonic abstraction of HTTP.](https://news.ycombinator.com/item?id=2810373) | Pump 用简洁的 Python 风格抽象 HTTP，减少编写网络请求时的繁琐操作。 | 118 | 61 | 2011-07-27 |
| 5 | [Show HN: Weekend Project - Create Simple Android mockup](https://news.ycombinator.com/item?id=2828482) | 作者周末开发 Android 界面草图工具，帮助快速构思移动应用页面。 | 110 | 35 | 2011-07-31 |
| 6 | [Show HN: My first WebGL demo, the first self-extracting PNG ever?](https://news.ycombinator.com/item?id=2771454) | 首个 WebGL 演示用可自解包的 PNG 封装，作者询问这种形式是否前所未有。 | 101 | 55 | 2011-07-16 |
| 7 | [Show HN: Kondoot - Watch LIVE a day in the life of a startup](https://news.ycombinator.com/item?id=2810324) | Kondoot 直播创业公司一天的生活，让观众实时看看团队如何工作。 | 97 | 25 | 2011-07-27 |
| 8 | [Show HN: Laminated Bus Schedules](https://news.ycombinator.com/item?id=2770699) | 给公交时刻表覆膜，作者分享围绕日常出行资料制作的实体作品。 | 94 | 51 | 2011-07-16 |
| 9 | [Show HN: Two-faced URLs](https://news.ycombinator.com/item?id=2734360) | 作者介绍双面 URL 的项目构思，展示对网址表现形式的实验。 | 85 | 16 | 2011-07-06 |
| 10 | [Show HN: We want to become India's TurboTax. Feedback?](https://news.ycombinator.com/item?id=2799523) | 团队希望成为印度版 TurboTax，邀请社区评估其在线报税产品方向。 | 75 | 60 | 2011-07-24 |

### 2011-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Codecademy.com, the easiest way to learn to code](https://news.ycombinator.com/item?id=2901156) | Codecademy 展示以互动方式帮助新手学习编程的平台。 | 787 | 232 | 2011-08-18 |
| 2 | [Show HN: Like Button for Hacker News](https://news.ycombinator.com/item?id=2934178) | 为 Hacker News 添加喜欢按钮，作者尝试扩展社区互动方式。 | 568 | 65 | 2011-08-28 |
| 3 | [Show HN: We made a spam-free lyric search engine](https://news.ycombinator.com/item?id=2932956) | 团队制作避免垃圾内容的歌词搜索引擎，帮助更直接地找到歌曲文本。 | 291 | 141 | 2011-08-28 |
| 4 | [Show HN: a free multi-user whiteboard with unlimited, zoomable surface](https://news.ycombinator.com/item?id=2898343) | 免费多人白板提供可无限缩放的画布，让协作不受页面大小限制。 | 215 | 72 | 2011-08-18 |
| 5 | [Show HN: My weekend project - preview TV sizes on your wall](https://news.ycombinator.com/item?id=2845450) | 买电视前先在墙上预览不同尺寸，作者用周末项目帮助判断屏幕大小。 | 179 | 51 | 2011-08-04 |
| 6 | [Show HN: I shipped my first product](https://news.ycombinator.com/item?id=2867428) | 作者分享首个产品终于发布的时刻，记录从开发走到交付的进展。 | 163 | 65 | 2011-08-10 |
| 7 | [Show HN: New way to search for used cars (my weekend project)](https://news.ycombinator.com/item?id=2885720) | 用里程与价格绘制二手车散点图，帮助买家从可视化角度比较车辆。 | 160 | 66 | 2011-08-15 |
| 8 | [Show HN: An intuitive, offline capable HTML5 mind mapping application](https://news.ycombinator.com/item?id=2831898) | HTML5 思维导图应用支持离线操作，尝试让整理想法更直观。 | 112 | 39 | 2011-08-01 |
| 9 | [Show HN: Crash into Python](https://news.ycombinator.com/item?id=2884863) | Crash into Python 是此次公开的项目，作者把自己的作品带到社区交流。 | 107 | 14 | 2011-08-14 |
| 10 | [Show HN: CodeMatch: IDE autocomplete on overdrive ](https://news.ycombinator.com/item?id=2903224) | CodeMatch 围绕 IDE 自动补全展开，尝试增强写代码时的补全体验。 | 102 | 63 | 2011-08-19 |

### 2011-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: HackerThings - Products for hackers](https://news.ycombinator.com/item?id=3045536) | HackerThings 汇集面向黑客爱好者的产品，帮助发现适合动手探索的物件。 | 364 | 134 | 2011-09-27 |
| 2 | [Show HN: Smozzy (for Android/T-Mobile) - browse the web without a data plan](https://news.ycombinator.com/item?id=2976764) | Smozzy 让 Android 与 T-Mobile 用户尝试在没有流量套餐时浏览网页。 | 293 | 105 | 2011-09-09 |
| 3 | [Show HN: Write a sort, watch it go](https://news.ycombinator.com/item?id=3040157) | 自己编写排序算法并观察运行过程，作者用可视化帮助理解代码行为。 | 292 | 80 | 2011-09-26 |
| 4 | [Show HN: PickHealthInsurance.com](https://news.ycombinator.com/item?id=2992146) | PickHealthInsurance.com 围绕医疗保险选择命名，作者公开这项网络项目。 | 232 | 99 | 2011-09-13 |
| 5 | [Show HN: Hacker News Mobile - A fast and readable mobile HN website](https://news.ycombinator.com/item?id=3002117) | Hacker News Mobile 为手机重新组织 HN 页面，追求更快、更易读的浏览体验。 | 209 | 58 | 2011-09-15 |
| 6 | [Show HN: Final Touch](https://news.ycombinator.com/item?id=2991206) | Final Touch 项目向社区公开，作者邀请读者看看这次开发成果。 | 194 | 117 | 2011-09-13 |
| 7 | [Show HN: Fluid iPad App Concept ](https://news.ycombinator.com/item?id=3003794) | Fluid 展示 iPad 应用概念，围绕平板上的界面与交互提供一种设计构思。 | 179 | 40 | 2011-09-16 |
| 8 | [Show HN: Pulse — A simple pulsating indicator.](https://news.ycombinator.com/item?id=3009307) | Pulse 提供简单的脉动指示效果，方便放进应用里提示动态状态。 | 163 | 40 | 2011-09-18 |
| 9 | [Show HN: Check out the 23" Android 'tablet' I made for $600](https://news.ycombinator.com/item?id=3022245) | 花六百美元自制二十三英寸 Android 平板，作者展示大屏硬件改造。 | 160 | 55 | 2011-09-21 |
| 10 | [Show HN: Kerning.js — Take control of your web typography](https://news.ycombinator.com/item?id=3010970) | Kerning.js 帮助细调网页排版，让开发者更直接地控制文字呈现。 | 154 | 30 | 2011-09-18 |

### 2011-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: A storebuilder contained in a single text area](https://news.ycombinator.com/item?id=3154818) | 把整个商店搭建器装进一个文本框，作者尝试极简的店铺创建方式。 | 389 | 113 | 2011-10-25 |
| 2 | [Show HN: KernType, a typography game made with Raphaël](https://news.ycombinator.com/item?id=3086320) | KernType 用 Raphaël 制作排版游戏，让用户在互动中感受文字间距。 | 268 | 53 | 2011-10-07 |
| 3 | [Show HN: my 4-y-o son drew a video game. He drew then we hacked together.](https://news.ycombinator.com/item?id=3100274) | 四岁儿子先画游戏，家长再一起把画变成能玩的程序。 | 247 | 64 | 2011-10-11 |
| 4 | [Show HN: Who's Hiring? (postings mined from Twitter)](https://news.ycombinator.com/item?id=3103307) | 从 Twitter 挖掘招聘信息，作者整理“谁在招人”的岗位发现工具。 | 220 | 63 | 2011-10-12 |
| 5 | [Show HN: The users behind Hacker News](https://news.ycombinator.com/item?id=3117695) | 看看 Hacker News 账号背后的人，作者展示面向社区成员的项目。 | 193 | 95 | 2011-10-16 |
| 6 | [Show HN: Learn iPhone and iPad development in less than an hour](https://news.ycombinator.com/item?id=3115086) | 不到一小时能怎样入门 iPhone 和 iPad 开发，作者分享压缩后的学习内容。 | 163 | 91 | 2011-10-15 |
| 7 | [Show HN: My network connection monitor for Mac](https://news.ycombinator.com/item?id=3087372) | Mac 网络连接监测工具，帮助用户留意电脑的联网状态。 | 146 | 77 | 2011-10-08 |
| 8 | [Show HN: Create a beautiful timeline with TimeKiwi](https://news.ycombinator.com/item?id=3109779) | TimeKiwi 让用户制作时间线，以直观方式组织不同时间发生的事情。 | 145 | 48 | 2011-10-14 |
| 9 | [Show HN: My table of tools for startups [Google Docs]](https://news.ycombinator.com/item?id=3081171) | 作者用 Google Docs 整理创业工具表，供早期团队查找所需软件。 | 139 | 39 | 2011-10-06 |
| 10 | [Show HN: validate.js - lightweight JavaScript form validation library](https://news.ycombinator.com/item?id=3121374) | validate.js 是轻量 JavaScript 表单校验库，帮助检查用户输入。 | 102 | 32 | 2011-10-17 |

### 2011-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Entire concerts algorithmically "reconstructed" from YouTube videos](https://news.ycombinator.com/item?id=3293324) | 把不同 YouTube 现场视频通过算法拼合，尝试重建完整演唱会。 | 435 | 129 | 2011-11-30 |
| 2 | [Show HN: An OS X music library I've been working on for the past year.](https://news.ycombinator.com/item?id=3207736) | 为 OS X 音乐库投入整整一年后，作者公开长期开发的阶段成果。 | 301 | 130 | 2011-11-07 |
| 3 | [Show HN: When is good time to submit a story on HN?](https://news.ycombinator.com/item?id=3251877) | 什么时候向 HN 投稿比较好，作者用项目探索发帖时机与曝光机会。 | 269 | 46 | 2011-11-18 |
| 4 | [Show HN: Scroll Reddit](https://news.ycombinator.com/item?id=3196766) | Scroll Reddit 重新组织 Reddit 的浏览体验，供读者试用这种阅读方式。 | 240 | 73 | 2011-11-04 |
| 5 | [Show HN: AI tool reads privacy policies, tells you which sites sell your info.](https://news.ycombinator.com/item?id=3222334) | AI 工具阅读隐私政策，尝试告诉用户哪些网站会出售个人信息。 | 145 | 71 | 2011-11-10 |
| 6 | [Show HN: Version 1.1 of our $99 hackable Bluetooth smartwatch](https://news.ycombinator.com/item?id=3290884) | 九十九美元可编程蓝牙智能手表发布 1.1 版，团队展示更新进展。 | 139 | 63 | 2011-11-29 |
| 7 | [Show HN: Tunebox, Dropbox + iPhone = cloud music service](https://news.ycombinator.com/item?id=3244623) | Tunebox 将 Dropbox 与 iPhone 结合，把云端文件用作音乐库。 | 131 | 38 | 2011-11-16 |
| 8 | [Show HN: elegant open-source pastebin server (node.js & redis)](https://news.ycombinator.com/item?id=3291130) | 用 Node.js 和 Redis 搭建开源 Pastebin 服务，方便分享文本和代码。 | 131 | 68 | 2011-11-29 |
| 9 | [Show HN: Use Dojo to learn, build, and deploy web apps](https://news.ycombinator.com/item?id=3286867) | Dojo 尝试贯通学习、构建与部署，帮助用户把 Web 应用做出来并上线。 | 119 | 29 | 2011-11-28 |
| 10 | [Show HN: HourlyPuppy](https://news.ycombinator.com/item?id=3245267) | HourlyPuppy 是这次提交的作品，作者借 Show HN 向社区公开项目。 | 118 | 52 | 2011-11-16 |

### 2011-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I Created the Inverse of Angry Birds](https://news.ycombinator.com/item?id=3374434) | 把《愤怒的小鸟》的玩法反过来，作者展示一款逆向构思的游戏。 | 625 | 123 | 2011-12-20 |
| 2 | [Show HN: My Zappos/Twilio hackathon entry ](https://news.ycombinator.com/item?id=3364942) | 参加 Zappos 与 Twilio 黑客松的作品完成，作者公开自己的参赛成果。 | 166 | 47 | 2011-12-17 |
| 3 | [Show HN: Blanking all Wikipedia as SOPA Protest Live Stats](https://news.ycombinator.com/item?id=3346326) | 围绕反对 SOPA 的维基百科黑屏抗议，作者制作实时统计项目。 | 163 | 23 | 2011-12-13 |
| 4 | [Show HN: We just launched our MVP, a new RSS Reader](https://news.ycombinator.com/item?id=3401591) | 新的 RSS 阅读器推出最小可用版本，团队提前展示并收集反馈。 | 153 | 69 | 2011-12-28 |
| 5 | [Show HN: Redis/ruby-based realtime event-tracking](https://news.ycombinator.com/item?id=3393167) | 用 Redis 与 Ruby 实现实时事件追踪，作者分享记录应用行为的方案。 | 151 | 21 | 2011-12-26 |
| 6 | [Show HN: The Honeybadger](https://news.ycombinator.com/item?id=3404330) | 作者带来名为 The Honeybadger 的项目，展示近期开发成果。 | 147 | 55 | 2011-12-29 |
| 7 | [Show HN: "Programming is for Anyone"](https://news.ycombinator.com/item?id=3314679) | “编程属于每个人”，作者展示围绕降低编程门槛的项目。 | 105 | 21 | 2011-12-05 |
| 8 | [Show HN: Virtual Angel Investing market (built on AngelList)](https://news.ycombinator.com/item?id=3312352) | 在 AngelList 之上构建虚拟天使投资市场，让用户模拟早期投资。 | 97 | 24 | 2011-12-05 |
| 9 | [Show HN: Write and deploy your first web app in 5 minutes, no setup needed](https://news.ycombinator.com/item?id=3317824) | 无需预先配置环境，作者展示五分钟写出并部署首个 Web 应用的流程。 | 86 | 31 | 2011-12-06 |
| 10 | [Show HN: Logging in with QR codes (proof of concept)](https://news.ycombinator.com/item?id=3399781) | 用二维码完成登录，作者公开概念验证，探索密码输入之外的认证交互。 | 86 | 39 | 2011-12-28 |

### 2012-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: We made an addictive way to browse pictures on reddit](https://news.ycombinator.com/item?id=3507731) | 团队重新设计 Reddit 图片浏览方式，让连续发现和查看图片更方便。 | 401 | 138 | 2012-01-25 |
| 2 | [Show HN: Scrollorama](https://news.ycombinator.com/item?id=3413594) | Scrollorama 是作者此次分享的网页项目，邀请社区体验与讨论。 | 395 | 51 | 2012-01-01 |
| 3 | [Show HN: my database engine for GPU](https://news.ycombinator.com/item?id=3513165) | 把数据库引擎放到 GPU 上运行，作者展示面向图形处理器的数据处理尝试。 | 364 | 60 | 2012-01-26 |
| 4 | [Show HN: I'm tired of corrupt US politicians, so I created this](https://news.ycombinator.com/item?id=3504434) | 厌倦美国政坛腐败后，作者用项目表达关切并尝试作出改变。 | 334 | 144 | 2012-01-24 |
| 5 | [Show HN: How I built a self-driving (RC) car.](https://news.ycombinator.com/item?id=3417830) | 受机器学习课程启发，作者把遥控车改成自动驾驶小车并分享制作过程。 | 300 | 21 | 2012-01-02 |
| 6 | [Show HN: Craigslist Car Search ](https://news.ycombinator.com/item?id=3506629) | 为 Craigslist 汽车信息做专门搜索，帮助更集中地筛选二手车。 | 236 | 103 | 2012-01-24 |
| 7 | [Show HN: HackPad is the best wiki ever](https://news.ycombinator.com/item?id=3477081) | HackPad 团队介绍 Wiki 产品，并用“最好的 Wiki”表达对协作体验的追求。 | 209 | 77 | 2012-01-17 |
| 8 | [Show HN: SocialFolders, "Dropbox for social"](https://news.ycombinator.com/item?id=3518051) | SocialFolders 借鉴 Dropbox 的文件管理方式，尝试让社交内容更容易掌控。 | 187 | 73 | 2012-01-27 |
| 9 | [Show HN: A visual explanation of Fisher–Yates shuffle](https://news.ycombinator.com/item?id=3464607) | 通过可视化讲清 Fisher–Yates 洗牌算法，帮助理解随机打乱的过程。 | 176 | 37 | 2012-01-14 |
| 10 | [Show HN: Collection of CSS Creations](https://news.ycombinator.com/item?id=3469347) | 作者汇集 CSS 创作示例，供读者欣赏样式代码能实现的视觉效果。 | 165 | 36 | 2012-01-16 |

### 2012-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Hackershelf. Community curated collection of legally free books](https://news.ycombinator.com/item?id=3589963) | Hackershelf 由社区整理合法免费的书籍，帮助发现可自由阅读的资料。 | 532 | 121 | 2012-02-14 |
| 2 | [Show HN: Github for Designers](https://news.ycombinator.com/item?id=3572755) | 把 GitHub 式协作思路带给设计师，作者展示面向设计工作的项目。 | 409 | 83 | 2012-02-09 |
| 3 | [Show HN: Bootswatch, free swatches for your Bootstrap site](https://news.ycombinator.com/item?id=3594540) | Bootswatch 提供免费的 Bootstrap 主题配色，方便快速更换网站外观。 | 407 | 53 | 2012-02-15 |
| 4 | [Show HN: Fed up with WebEx, so we built a way to screen share in under 20 sec.](https://news.ycombinator.com/item?id=3539792) | 不满 WebEx 的繁琐流程，团队做出目标二十秒内开始屏幕共享的工具。 | 402 | 130 | 2012-02-01 |
| 5 | [Show HN: Themes for Bootstrap](https://news.ycombinator.com/item?id=3579207) | 作者为 Bootstrap 制作主题，帮助使用同一框架的网站获得不同外观。 | 354 | 93 | 2012-02-11 |
| 6 | [Show HN: Favicon alert bubbles](https://news.ycombinator.com/item?id=3560321) | JavaScript 库给网站图标加上提醒气泡，让标签页也能显示通知状态。 | 271 | 63 | 2012-02-07 |
| 7 | [Show HN: My afternoon project - a pleasant viewer for the "who is hiring?" posts](https://news.ycombinator.com/item?id=3540481) | 花一个下午重新整理 HN 招聘帖，作者做出更舒适的岗位浏览界面。 | 185 | 35 | 2012-02-01 |
| 8 | [Show HN: Get a better job offer, anonymously - my weekend hack](https://news.ycombinator.com/item?id=3557805) | 周末做个匿名求职工具，帮助开发者在不公开身份时寻找更好的聘用条件。 | 182 | 84 | 2012-02-06 |
| 9 | [Show HN: Wireshark as a web app](https://news.ycombinator.com/item?id=3616603) | 把 Wireshark 式网络分析带到网页，作者展示浏览器形式的工具尝试。 | 164 | 31 | 2012-02-21 |
| 10 | [Show HN: Cron.io - Sharing a by-product. Should this be a full service?](https://news.ycombinator.com/item?id=3560750) | Cron.io 原本是开发副产物，作者询问是否值得独立做成完整服务。 | 153 | 70 | 2012-02-07 |

### 2012-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: This up votes itself](https://news.ycombinator.com/item?id=3742902) | 展示一个会给自己投赞成票的 HN 项目。 | 3531 | 82 | 2012-03-23 |
| 2 | [Show HN: A Way To Hack HN's Karma](https://news.ycombinator.com/item?id=3742742) | 点击一个链接就会触发 HN 点赞，作者演示这一问题并希望它得到关注。 | 472 | 33 | 2012-03-23 |
| 3 | [Show HN: Streak.com - Do sales, support and bug tracking all inside Gmail](https://news.ycombinator.com/item?id=3652983) | Streak 把销售、客服与缺陷追踪放进 Gmail，让工作围绕邮件直接进行。 | 306 | 95 | 2012-03-01 |
| 4 | [Show HN: Flutter - Control Spotify or iTunes Using Gestures thru Webcam](https://news.ycombinator.com/item?id=3691588) | Flutter 用摄像头识别手势，帮助用户不触碰键盘就控制 Spotify 或 iTunes。 | 239 | 125 | 2012-03-11 |
| 5 | [Show HN: I decided to document and share my high-level CSS best practices](https://news.ycombinator.com/item?id=3693610) | 作者整理自己积累的 CSS 高层实践，公开说明编写样式时的原则。 | 223 | 86 | 2012-03-12 |
| 6 | [Show HN: Tired of entering map directions on iPhone? I've streamlined it](https://news.ycombinator.com/item?id=3750417) | 觉得在 iPhone 输入地图路线太麻烦，作者制作工具简化这一过程。 | 185 | 81 | 2012-03-24 |
| 7 | [Show HN: I wrote a guidebook on everything I know about applying to Y Combinator](https://news.ycombinator.com/item?id=3667657) | 作者把自己对 YC 申请的了解写成指南，帮助后来者准备申请。 | 177 | 53 | 2012-03-05 |
| 8 | [Show HN: KytePhone turns any Android into a kids-friendly phone](https://news.ycombinator.com/item?id=3745471) | KytePhone 为 Android 增加适合儿童的使用方式，帮助家长配置孩子的手机。 | 166 | 69 | 2012-03-23 |
| 9 | [Show HN: Meme generator for hipsters](https://news.ycombinator.com/item?id=3724796) | 面向文艺青年风格的梗图生成器，作者展示轻松恶搞的小工具。 | 146 | 46 | 2012-03-19 |
| 10 | [Show HN: Q&A for HN users](https://news.ycombinator.com/item?id=3747238) | 为 HN 用户建立问答空间，作者探索社区成员之间更直接的知识交流。 | 142 | 72 | 2012-03-23 |

### 2012-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Meteor, a realtime JavaScript framework](https://news.ycombinator.com/item?id=3824908) | 介绍实时 JavaScript 开发框架 Meteor。 | 1386 | 322 | 2012-04-10 |
| 2 | [Show HN: Imagine a search engine that removed top million sites from its index](https://news.ycombinator.com/item?id=3910304) | 展示一个从索引中移除排名前百万网站的搜索引擎。 | 552 | 195 | 2012-04-30 |
| 3 | [Show HN: Firebase, a scalable real-time backend](https://news.ycombinator.com/item?id=3832877) | Firebase 团队介绍可扩展的实时后端，帮助应用同步数据与状态。 | 526 | 137 | 2012-04-12 |
| 4 | [Show HN: Our Hackable E-Paper Watch for iPhone and Android](https://news.ycombinator.com/item?id=3827868) | 团队展示连接 iPhone 和 Android 的可编程电子纸手表，邀请开发者参与。 | 342 | 107 | 2012-04-11 |
| 5 | [Show HN: Clutch.io helps you build iOS apps fast and update them instantly](https://news.ycombinator.com/item?id=3800089) | Clutch.io 帮助快速构建 iOS 应用，并尝试让更新可以即时送达。 | 290 | 88 | 2012-04-04 |
| 6 | [Show HN: iPG - YC Interview Simulator](https://news.ycombinator.com/item?id=3896931) | iPG 模拟 YC 面试，帮助申请者提前练习短时间内回答创业问题。 | 290 | 77 | 2012-04-27 |
| 7 | [Show HN: We built real MMO Asteroids](https://news.ycombinator.com/item?id=3819638) | 把经典小行星射击做成真正的多人在线游戏，团队展示 MMO 版本。 | 197 | 64 | 2012-04-09 |
| 8 | [Show HN: Filepicker.io - dead simple file uploads](https://news.ycombinator.com/item?id=3864615) | Filepicker.io 简化文件上传流程，帮助应用接入用户文件。 | 193 | 105 | 2012-04-19 |
| 9 | [Show HN: Open-sourcing my CV template [Helvetica, XeTeX, TikZ & Biblatex]](https://news.ycombinator.com/item?id=3908844) | 作者开源个人简历模板，组合 XeTeX、TikZ、Biblatex 与 Helvetica 字体。 | 166 | 67 | 2012-04-30 |
| 10 | [Show HN: A Lisp-based in-browser toy operating system](https://news.ycombinator.com/item?id=3782929) | 用 Lisp 在浏览器里搭建玩具操作系统，作者展示语言与系统实验。 | 156 | 19 | 2012-04-01 |

### 2012-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: my Mac app just got fireballed](https://news.ycombinator.com/item?id=3946404) | 个人 Mac 应用获得 Daring Fireball 关注后，作者分享这次曝光经历。 | 436 | 156 | 2012-05-08 |
| 2 | [Show HN: Habit List - my first iOS app](https://news.ycombinator.com/item?id=3998894) | Habit List 是作者首款 iOS 应用，以清单形式帮助追踪习惯。 | 282 | 131 | 2012-05-20 |
| 3 | [Show HN: Simperium, a realtime data layer](https://news.ycombinator.com/item?id=3950622) | Simperium 提供实时数据层，帮助应用处理不断变化并需要同步的数据。 | 208 | 87 | 2012-05-09 |
| 4 | [Show HN: I made $8000 in one day on the Mac App Store](https://news.ycombinator.com/item?id=4015393) | 作者称 Mac App Store 单日收入达到八千美元，分享产品销售的阶段成果。 | 190 | 83 | 2012-05-23 |
| 5 | [Show HN: My 1-year project, iPad IDE with GitHub and Heroku integration](https://news.ycombinator.com/item?id=3998710) | 投入一年制作 iPad 开发环境，集成 GitHub 与 Heroku，探索平板上写代码。 | 183 | 73 | 2012-05-20 |
| 6 | [Show HN: Hacking recruiting - Coder's Coffee](https://news.ycombinator.com/item?id=4010355) | Coder's Coffee 尝试改造开发者招聘方式，让找人与求职换一种交互。 | 180 | 100 | 2012-05-22 |
| 7 | [Show HN: My first web app - Resumonk - A beautifully simple resume builder](https://news.ycombinator.com/item?id=3934370) | Resumonk 是作者首个 Web 应用，目标是简单地制作美观简历。 | 175 | 86 | 2012-05-06 |
| 8 | [Show HN: A directory of single-page sites and useful apps](https://news.ycombinator.com/item?id=3959305) | 作者整理单页网站与实用应用目录，帮助发现轻巧的网络工具。 | 164 | 33 | 2012-05-11 |
| 9 | [Show HN: HackerNew for Chrome](https://news.ycombinator.com/item?id=3938619) | HackerNew 为 Chrome 提供 HN 扩展，侧重改善社区浏览的可用性。 | 150 | 89 | 2012-05-07 |
| 10 | [Show HN: My first web app, DailyDo.it](https://news.ycombinator.com/item?id=3996457) | DailyDo.it 是作者首个上线的 Web 应用，记录个人开发的起步成果。 | 142 | 56 | 2012-05-19 |

### 2012-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: movies.io — torrent search like it should be](https://news.ycombinator.com/item?id=4054568) | 展示以改进种子搜索体验为目标的 movies.io。 | 550 | 487 | 2012-06-01 |
| 2 | [Show HN: Easel, web design in the browser](https://news.ycombinator.com/item?id=4113866) | Easel 让用户直接在浏览器里设计网页，减少创作环境之间的切换。 | 346 | 120 | 2012-06-14 |
| 3 | [Show HN: Script Excel with Python](https://news.ycombinator.com/item?id=4085052) | 通过 Python 编写脚本操作 Excel，把表格任务交给程序处理。 | 280 | 61 | 2012-06-08 |
| 4 | [Show HN: A new way to view IAmA's on Reddit](https://news.ycombinator.com/item?id=4148415) | 作者为 Reddit 的 IAmA 问答设计另一种阅读界面，改善问答浏览体验。 | 263 | 65 | 2012-06-22 |
| 5 | [Show HN: The Bastards Book of Photography](https://news.ycombinator.com/item?id=4141538) | 《The Bastards Book of Photography》是作者分享的摄影学习作品。 | 259 | 72 | 2012-06-21 |
| 6 | [Show HN: I love weird socks and I'm finally launching my lifestyle business](https://news.ycombinator.com/item?id=4053554) | 因为喜欢奇特的袜子，作者开始经营自己的生活方式小生意。 | 243 | 79 | 2012-06-01 |
| 7 | [Show HN: Action.io - 0 to Rails in 60 seconds in your browser](https://news.ycombinator.com/item?id=4137820) | Action.io 希望在浏览器中六十秒启动 Rails 环境，缩短开始开发的准备时间。 | 210 | 79 | 2012-06-20 |
| 8 | [Show HN: vi in your browser - edit files directly from Dropbox, etc](https://news.ycombinator.com/item?id=4143863) | 把 vi 编辑体验带入浏览器，并直接编辑 Dropbox 等位置的文件。 | 206 | 77 | 2012-06-21 |
| 9 | [Show HN: Redis Dashboard](https://news.ycombinator.com/item?id=4123523) | Redis 仪表盘将相关状态集中展示，让数据库信息更容易浏览。 | 194 | 24 | 2012-06-17 |
| 10 | [Show HN: Avatars.io - simple API for integrating avatars into your app or site](https://news.ycombinator.com/item?id=4163271) | Avatars.io 提供头像 API，帮助网站和应用更方便地集成用户头像。 | 181 | 39 | 2012-06-26 |

### 2012-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: fontBomb - Stylishly destroy the web](https://news.ycombinator.com/item?id=4208102) | fontBomb 让用户以视觉爆破效果“摧毁”网页。 | 489 | 85 | 2012-07-06 |
| 2 | [Show HN: Markupwand, magically convert your photoshop files to HTML & CSS](https://news.ycombinator.com/item?id=4283896) | Markupwand 尝试把 Photoshop 文件转换成 HTML 与 CSS，连接设计稿与网页实现。 | 342 | 127 | 2012-07-24 |
| 3 | [Show HN: Moqups - Vectorial mockups with HTML5 and SVG](https://news.ycombinator.com/item?id=4222992) | Moqups 用 HTML5 与 SVG 制作矢量界面草图，在网页中进行原型设计。 | 310 | 103 | 2012-07-10 |
| 4 | [Show HN: gist.io, blogless writing for hackers](https://news.ycombinator.com/item?id=4263437) | gist.io 为开发者提供无需自建博客的写作方式，让分享文章更轻便。 | 286 | 51 | 2012-07-18 |
| 5 | [Show HN: BrainTripping - language model comedy](https://news.ycombinator.com/item?id=4240041) | BrainTripping 用语言模型创作喜剧，探索算法生成幽默的可能性。 | 283 | 41 | 2012-07-13 |
| 6 | [Show HN: Iorad - the tutorial builder](https://news.ycombinator.com/item?id=4202941) | Iorad 是教程制作工具，帮助把操作过程整理为可供他人学习的内容。 | 276 | 99 | 2012-07-05 |
| 7 | [Show HN: Gridspot, 10x cheaper cloud compute using distributed computing](https://news.ycombinator.com/item?id=4225817) | Gridspot 利用分布式计算提供云算力，团队主张其成本可比常见方案低一个量级。 | 266 | 144 | 2012-07-10 |
| 8 | [Show HN: Music for Geeks and Nerds](https://news.ycombinator.com/item?id=4295714) | “给极客与书呆子的音乐”，作者展示围绕技术人兴趣的音乐项目。 | 221 | 74 | 2012-07-26 |
| 9 | [Show HN: Collections, a fast multiple-account Google Docs client for Mac](https://news.ycombinator.com/item?id=4241638) | Collections 是 Mac 上的 Google Docs 客户端，支持同时处理多个账号。 | 196 | 96 | 2012-07-13 |
| 10 | [Show HN: Hacker News Comments](https://news.ycombinator.com/item?id=4285019) | 作者围绕 Hacker News 评论制作项目，探索社区讨论内容的新用法。 | 189 | 69 | 2012-07-24 |

### 2012-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN - We just built a site that saves lives](https://news.ycombinator.com/item?id=4424081) | Watsi 展示医疗众筹平台，尝试通过全球捐款帮助有治疗需求的人。 | 462 | 183 | 2012-08-23 |
| 2 | [Show HN: A date range picker for Twitter Bootstrap](https://news.ycombinator.com/item?id=4408070) | 为 Twitter Bootstrap 制作日期范围选择器，方便用户输入开始与结束日期。 | 363 | 80 | 2012-08-20 |
| 3 | [Show HN: Burner, for temporary phone numbers](https://news.ycombinator.com/item?id=4355545) | Burner 提供临时电话号码，帮助把短期联系与日常号码分开。 | 323 | 180 | 2012-08-08 |
| 4 | [Show HN: Most Wikipedia articles lead to the same loop](https://news.ycombinator.com/item?id=4459826) | 作者发现大量维基百科文章的链接会走向同一个循环，展示这项网页观察。 | 295 | 161 | 2012-08-31 |
| 5 | [Show HN: Business.txt - Standard Proposal](https://news.ycombinator.com/item?id=4438194) | Business.txt 提出一种标准化文本格式，作者邀请讨论这一规范提案。 | 264 | 109 | 2012-08-27 |
| 6 | [Show HN: BigVideo.js](https://news.ycombinator.com/item?id=4404204) | 作者公开 BigVideo.js 项目，展示自己的 JavaScript 开发成果。 | 244 | 48 | 2012-08-19 |
| 7 | [Show HN: SideProjects.com - 37 Bootstrapped Profitable Projects](https://news.ycombinator.com/item?id=4418621) | SideProjects.com 整理三十七个自筹资金且盈利的项目，也邀请其他作者加入。 | 236 | 118 | 2012-08-22 |
| 8 | [Show HN: Eligible API for 700+ Health Insurance Companies](https://news.ycombinator.com/item?id=4368877) | Eligible 提供覆盖七百多家健康保险公司的 API，尝试连接医疗保险信息。 | 218 | 92 | 2012-08-10 |
| 9 | [Show HN: We Use That. What startups use to get stuff done](https://news.ycombinator.com/item?id=4357348) | We Use That 汇集创业公司用来完成工作的工具，帮助同行参考实际选择。 | 201 | 43 | 2012-08-08 |
| 10 | [Show HN: See Kickstarter successes and failures](https://news.ycombinator.com/item?id=4366002) | 把 Kickstarter 成功与失败案例放在一起，帮助观察众筹项目的不同结局。 | 187 | 63 | 2012-08-10 |

### 2012-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: We got tired of asking 'What browser are you using?' and created this](https://news.ycombinator.com/item?id=4499435) | 开发者制作工具，减少反复询问用户浏览器信息的麻烦。 | 521 | 175 | 2012-09-10 |
| 2 | [Show HN: My Github résumé](https://news.ycombinator.com/item?id=4466883) | 作者把 GitHub 经历整理成简历，探索展示开发者能力的另一种形式。 | 301 | 75 | 2012-09-02 |
| 3 | [Show HN: Enterface, a UI design app concept I'm designing](https://news.ycombinator.com/item?id=4467228) | Enterface 是一款 UI 设计应用概念，作者公开自己的产品构思。 | 234 | 78 | 2012-09-02 |
| 4 | [Show HN: Mixest, my summer project that crawls the web for new indie music](https://news.ycombinator.com/item?id=4462315) | Mixest 在网上寻找新的独立音乐，是作者暑假制作的音乐发现项目。 | 219 | 73 | 2012-09-01 |
| 5 | [Show HN: Ejecta, A Fast, Open Source JavaScript, Canvas Implementation for iOS](https://news.ycombinator.com/item?id=4570382) | Ejecta 为 iOS 提供开源 JavaScript 与 Canvas 实现，探索移动图形应用运行环境。 | 190 | 45 | 2012-09-25 |
| 6 | [Show HN: Bubbles - my unfinished HTML5 Particle Game](https://news.ycombinator.com/item?id=4584865) | Bubbles 是尚未完成的 HTML5 粒子游戏，作者先公开阶段成果。 | 188 | 87 | 2012-09-28 |
| 7 | [Show HN: MemStash - Commit things to memory](https://news.ycombinator.com/item?id=4496647) | MemStash 围绕记住信息设计，帮助用户把想保留的内容留在记忆中。 | 170 | 75 | 2012-09-09 |
| 8 | [Show HN: Learned Objective C as a high schooler and made this iPhone game](https://news.ycombinator.com/item?id=4556296) | 高中生自学 Objective-C 后制作 iPhone 游戏，展示第一次动手实践的成果。 | 158 | 48 | 2012-09-21 |
| 9 | [Show HN: EasyPost - the Stripe for postage](https://news.ycombinator.com/item?id=4538949) | EasyPost 以“邮寄领域的 Stripe”为定位，介绍简化邮资处理的产品方向。 | 157 | 83 | 2012-09-18 |
| 10 | [Show HN: My first Mac app, Foreman, free and on Github. Would love feedback](https://news.ycombinator.com/item?id=4488910) | Foreman 是作者首个免费 Mac 应用，源码放在 GitHub 并开放反馈。 | 153 | 86 | 2012-09-07 |

### 2012-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I spent two years working on an HTML5 game. I finally released it](https://news.ycombinator.com/item?id=4684696) | 开发者发布自己花两年时间制作的 HTML5 游戏。 | 515 | 145 | 2012-10-22 |
| 2 | [Show HN: We open sourced Lockitron's crowdfunding app](https://news.ycombinator.com/item?id=4643175) | 团队开源 Lockitron 的众筹应用，让其他项目也能研究其筹款实现。 | 463 | 74 | 2012-10-11 |
| 3 | [Show HN: Meet your cardboard buddy.](https://news.ycombinator.com/item?id=4601366) | 定制自己的纸板伙伴，团队把个性化实体制作与三维 CSS 展示结合。 | 240 | 107 | 2012-10-02 |
| 4 | [Show HN: I built a stock market game based on the top 50,000 websites](https://news.ycombinator.com/item?id=4604099) | 把最受欢迎的五万个网站当成标的，作者做出一款模拟股票市场游戏。 | 184 | 85 | 2012-10-02 |
| 5 | [Show HN: UrbanDesk - Combination Full Size Bed and Desk](https://news.ycombinator.com/item?id=4636857) | UrbanDesk 把全尺寸床和书桌组合，探索小空间里睡眠与工作区域的切换。 | 171 | 76 | 2012-10-10 |
| 6 | [Show HN: Circular, an open source clone of Buffer](https://news.ycombinator.com/item?id=4723591) | Circular 是开源的 Buffer 克隆项目，作者公开实现供社区使用与研究。 | 160 | 104 | 2012-10-31 |
| 7 | [Show HN: Powderkeg, a realtime, synchronous, multiplayer HTML5 action game](https://news.ycombinator.com/item?id=4613407) | Powderkeg 提供实时同步的多人 HTML5 动作游戏，展示浏览器联机体验。 | 153 | 71 | 2012-10-04 |
| 8 | [Show HN: Introducting C+](https://news.ycombinator.com/item?id=4725210) | 作者介绍名为 C+ 的新项目，邀请社区了解这次技术尝试。 | 148 | 47 | 2012-10-31 |
| 9 | [Show HN: my weekend project, Quotably](https://news.ycombinator.com/item?id=4683443) | Quotably 是作者的周末项目，公开展示一次短期开发的成果。 | 142 | 75 | 2012-10-22 |
| 10 | [Show HN: Python Tools for Visual Studio](https://news.ycombinator.com/item?id=4725396) | Python Tools for Visual Studio 把 Python 开发支持带进 Visual Studio。 | 139 | 54 | 2012-10-31 |

### 2012-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Soundslice – YouTube + synced guitar tabs + HTML5](https://news.ycombinator.com/item?id=4790636) | Soundslice 把 YouTube 视频与吉他谱同步，帮助边看演奏边对照谱子。 | 492 | 124 | 2012-11-15 |
| 2 | [Show HN: Non-Confusing, Visually Correct Slider Toggle UI](https://news.ycombinator.com/item?id=4742535) | 重新设计滑动开关，作者希望让控件视觉状态与操作含义更清楚。 | 441 | 79 | 2012-11-05 |
| 3 | [Show HN: Instant Google Street View](https://news.ycombinator.com/item?id=4792077) | 即时查看 Google 街景，作者尝试缩短从搜索地点到观看街景的路径。 | 412 | 101 | 2012-11-16 |
| 4 | [Show HN: An IDE for poets](https://news.ycombinator.com/item?id=4775886) | 给诗人做一个集成创作环境，作者把 IDE 的思路带到诗歌写作。 | 398 | 113 | 2012-11-13 |
| 5 | [Show HN: I'm 14, I learned Objective-C, and this is my first iPhone game](https://news.ycombinator.com/item?id=4735162) | 十四岁作者学会 Objective-C 后完成首个 iPhone 游戏，分享入门成果。 | 386 | 175 | 2012-11-02 |
| 6 | [Show HN: Responsive Email Templates](https://news.ycombinator.com/item?id=4855892) | 作者提供响应式邮件模板，帮助邮件在不同屏幕尺寸上呈现合适布局。 | 310 | 93 | 2012-11-30 |
| 7 | [Show HN: RewindHN - Go back in Hacker News history](https://news.ycombinator.com/item?id=4769757) | RewindHN 让读者回到 Hacker News 的过去，重新发现历史内容。 | 250 | 51 | 2012-11-11 |
| 8 | [Show HN: I built a thing](https://news.ycombinator.com/item?id=4737683) | 作者把亲手做出的作品带到 HN，邀请社区查看并交流制作成果。 | 242 | 102 | 2012-11-03 |
| 9 | [Show HN: Telescope, an open-source social news app built with Meteor](https://news.ycombinator.com/item?id=4840032) | Telescope 用 Meteor 构建开源社交新闻应用，供社区搭建与继续开发。 | 222 | 80 | 2012-11-27 |
| 10 | [Show HN: garlic.js - don't let your users lose their form data](https://news.ycombinator.com/item?id=4767056) | garlic.js 尝试保留表单输入，减少用户因意外离开页面而丢失内容。 | 212 | 105 | 2012-11-10 |

### 2012-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Analytics.js – The analytics API you've always wanted](https://news.ycombinator.com/item?id=4912076) | Analytics.js 围绕分析 API 展开，作者尝试提供更符合开发需求的接入方式。 | 326 | 67 | 2012-12-12 |
| 2 | [Show HN: Scratchpad.io - a real-time HTML and CSS editor](https://news.ycombinator.com/item?id=4933608) | Scratchpad.io 提供实时 HTML 与 CSS 编辑，让页面代码修改更直接。 | 298 | 82 | 2012-12-17 |
| 3 | [Show HN: Interactive SICP](https://news.ycombinator.com/item?id=4860370) | 把《计算机程序的构造和解释》变成交互式内容，帮助读者边学边实践。 | 280 | 51 | 2012-12-02 |
| 4 | [Show HN: CSS3 animation](https://news.ycombinator.com/item?id=4977845) | 单靠 CSS3 能做出怎样的动画，作者公开网页样式驱动的动态效果。 | 271 | 95 | 2012-12-28 |
| 5 | [Show HN: How I turned an old book into a (barely) profitable website](https://news.ycombinator.com/item?id=4974055) | 把一本旧书变成略有盈利的网站，作者分享内容再利用的开发经历。 | 242 | 104 | 2012-12-27 |
| 6 | [Show HN: Clojure DSL for pattern-matching, parsing and generic programming](https://news.ycombinator.com/item?id=4902219) | 用 Clojure 设计领域语言，统一处理模式匹配、解析与泛型编程。 | 204 | 16 | 2012-12-10 |
| 7 | [Show HN: Ember Table by Addepar](https://news.ycombinator.com/item?id=4949551) | Addepar 展示 Ember Table，为 Ember 应用提供表格相关组件。 | 199 | 49 | 2012-12-20 |
| 8 | [Show HN: roots - a toolkit for advanced front-end dev](https://news.ycombinator.com/item?id=4916266) | roots 面向进阶前端开发，作者介绍用于组织网页工作的工具集。 | 195 | 114 | 2012-12-13 |
| 9 | [Show HN: box2d-jquery - physics-engine for your DOM](https://news.ycombinator.com/item?id=4903716) | box2d-jquery 把物理引擎接到 DOM，让网页元素也能参与物理模拟。 | 167 | 39 | 2012-12-11 |
| 10 | [Show HN: Survey Builder with Drag/Drop Logic Branching](https://news.ycombinator.com/item?id=4875759) | 问卷编辑器支持拖放设置逻辑分支，让不同答案引向不同后续问题。 | 165 | 64 | 2012-12-05 |

### 2013-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Built a Hacker News radio web app I can listen to](https://news.ycombinator.com/item?id=5096653) | 把 Hacker News 做成网络电台，作者希望可以通过听来获取社区内容。 | 315 | 85 | 2013-01-22 |
| 2 | [Show HN: Vinepeek - watch the world in realtime in 6 second snippets](https://news.ycombinator.com/item?id=5120301) | Vinepeek 连续呈现六秒短片，让用户实时看看世界各处正在发生什么。 | 286 | 120 | 2013-01-26 |
| 3 | [Show HN: My Weekend Hack - Stack-Ed: Learn from the best on StackOverflow](https://news.ycombinator.com/item?id=5127400) | Stack-Ed 从 Stack Overflow 优秀回答中组织学习，是作者的周末小项目。 | 286 | 80 | 2013-01-28 |
| 4 | [Show HN: Our alternative to recruiter spam](https://news.ycombinator.com/item?id=5022472) | 团队尝试替代招聘垃圾邮件，让开发者接触岗位时减少骚扰与噪音。 | 233 | 168 | 2013-01-07 |
| 5 | [Show HN: my useless weekend project, add speech bubbles to images](https://news.ycombinator.com/item?id=5003672) | 作者自称无用的周末作品，可以给图片添加对话气泡，快速制作趣味画面。 | 225 | 95 | 2013-01-03 |
| 6 | [Show HN: A faster, minimal YouTube interface built on Angular.js and Foundation](https://news.ycombinator.com/item?id=5096876) | 用 Angular.js 与 Foundation 重做 YouTube 界面，追求更快、更简洁的浏览。 | 189 | 105 | 2013-01-22 |
| 7 | [Show HN: Behave.js – Coding Behaviors for textarea elements](https://news.ycombinator.com/item?id=5114055) | Behave.js 给普通文本框补上编程编辑行为，让网页输入区更适合写代码。 | 180 | 72 | 2013-01-25 |
| 8 | [Show HN: API for detecting people, cars, and everyday objects in images](https://news.ycombinator.com/item?id=5045621) | 图像识别 API 尝试检测人物、汽车与日常物体，方便应用接入视觉能力。 | 179 | 72 | 2013-01-11 |
| 9 | [Show HN: Gallery of Open Source Ruby on Rails Apps](https://news.ycombinator.com/item?id=5098565) | 作者汇集开源 Ruby on Rails 应用，帮助学习者找到可阅读的完整项目。 | 158 | 32 | 2013-01-22 |
| 10 | [Show HN: Forget Flash, Skip GIF, Control iOS](https://news.ycombinator.com/item?id=5137028) | 作者以摆脱 Flash、跳过 GIF 为题展示项目，探索新的网页媒体表现方式。 | 155 | 35 | 2013-01-29 |

### 2013-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: a web-based xkcd-style comix editor](https://news.ycombinator.com/item?id=5209096) | 在网页里编辑 xkcd 风格漫画，让火柴人式创作更容易动手。 | 586 | 109 | 2013-02-12 |
| 2 | [Show HN: Pick a better background pattern for your website](https://news.ycombinator.com/item?id=5166346) | 帮助网站挑选更合适的背景纹理，作者把视觉选择整理成便捷工具。 | 347 | 52 | 2013-02-04 |
| 3 | [Show HN: hint.css – a tooltip library in CSS](https://news.ycombinator.com/item?id=5164029) | hint.css 仅用 CSS 制作提示气泡，简化网页中的补充说明效果。 | 236 | 55 | 2013-02-04 |
| 4 | [Show HN: What colour is your IP address?](https://news.ycombinator.com/item?id=5238537) | 把 IP 地址映射成颜色，作者用小工具让网络地址获得视觉表现。 | 208 | 73 | 2013-02-18 |
| 5 | [Show HN: Build your own Heroku on your own servers](https://news.ycombinator.com/item?id=5213862) | 在自己的服务器上搭建类似 Heroku 的环境，作者探索自主应用部署。 | 207 | 108 | 2013-02-13 |
| 6 | [Show HN: a conspiracy theory generator](https://news.ycombinator.com/item?id=5168401) | 自动生成阴谋论，作者用荒诞文本创作展示生成规则的趣味。 | 181 | 70 | 2013-02-05 |
| 7 | [Show HN: Hacky – Hacker News app for Mac](https://news.ycombinator.com/item?id=5170182) | Hacky 把 Hacker News 带到 Mac 桌面，提供专用社区浏览入口。 | 163 | 91 | 2013-02-05 |
| 8 | [Show HN: Chime - A Notification Center for the Web](https://news.ycombinator.com/item?id=5176630) | Chime 希望成为网页的通知中心，将不同网络服务的提醒集中呈现。 | 161 | 116 | 2013-02-06 |
| 9 | [Show HN: Zipline - algorithmic trading in open source Python](https://news.ycombinator.com/item?id=5150546) | Zipline 用开源 Python 支持算法交易，方便研究程序化投资策略。 | 157 | 30 | 2013-02-01 |
| 10 | [Show HN: Multiplayer Snake in Go](https://news.ycombinator.com/item?id=5156813) | 用 Go 写多人贪吃蛇，作者展示经典小游戏的网络对战版本。 | 156 | 75 | 2013-02-02 |

### 2013-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: XKCD-inspired StackSort](https://news.ycombinator.com/item?id=5395463) | 展示受 XKCD 启发而制作的排序项目 StackSort。 | 948 | 198 | 2013-03-18 |
| 2 | [Show HN: 6 months ago I quit my job to pursue indie dev. Here is our first game](https://news.ycombinator.com/item?id=5332317) | 辞职投身独立开发半年后，作者展示团队完成的第一款游戏。 | 858 | 329 | 2013-03-06 |
| 3 | [Show HN: Weekend project, Intro.js](https://news.ycombinator.com/item?id=5380056) | 展示周末制作的 Intro.js 项目，供读者了解和体验。 | 716 | 154 | 2013-03-15 |
| 4 | [Show HN: Webflow - Design responsive websites visually](https://news.ycombinator.com/item?id=5407499) | Webflow 用可视化方式设计响应式网站，帮助在设计界面中构建页面。 | 503 | 132 | 2013-03-20 |
| 5 | [Show HN: Incorporate your startup online with YC's forms (built by two lawyers)](https://news.ycombinator.com/item?id=5357618) | 两位律师用 YC 表格搭建在线公司注册服务，帮助创业者完成设立手续。 | 424 | 179 | 2013-03-11 |
| 6 | [Show HN: Heap is a new approach to analytics. Just capture everything](https://news.ycombinator.com/item?id=5424206) | Heap 提出先捕获所有行为的分析思路，减少事先决定每个事件的负担。 | 339 | 201 | 2013-03-22 |
| 7 | [Show HN: Increase your productivity with ambient noise](https://news.ycombinator.com/item?id=5325012) | 用环境声音辅助专注，作者展示希望提高工作效率的背景音项目。 | 337 | 205 | 2013-03-05 |
| 8 | [Show HN: Tiled Text – a Different Approach to Editing Text](https://news.ycombinator.com/item?id=5306155) | Tiled Text 把文字编辑换一种组织形式，探索常规编辑器之外的交互。 | 332 | 91 | 2013-03-01 |
| 9 | [Show HN: Save Memory in Google Chrome](https://news.ycombinator.com/item?id=5356823) | 想减少 Chrome 的内存消耗，作者围绕浏览器资源占用制作工具。 | 314 | 292 | 2013-03-11 |
| 10 | [Show HN: An anonymous P2P social network for Android, written in Clojure](https://news.ycombinator.com/item?id=5468467) | 用 Clojure 编写 Android 匿名 P2P 社交网络，探索不依赖常规中心平台的交流。 | 257 | 133 | 2013-03-31 |

### 2013-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I'm building an open-source, high-frequency trading system](https://news.ycombinator.com/item?id=5550930) | 作者正在构建开源高频交易系统，公开这项金融软件开发计划。 | 301 | 190 | 2013-04-15 |
| 2 | [Show HN: Cap'n Proto, by the ex-maintainer of Protocol Buffers](https://news.ycombinator.com/item?id=5482081) | 前 Protocol Buffers 维护者介绍 Cap'n Proto，展示自己接下来的技术项目。 | 286 | 85 | 2013-04-02 |
| 3 | [Show HN: Usability checklist – catch common problems before user testing](https://news.ycombinator.com/item?id=5600982) | 用可用性检查清单提前排查常见问题，让正式用户测试更聚焦。 | 216 | 36 | 2013-04-24 |
| 4 | [Show HN: Chardin.js, beautiful instructions for apps](https://news.ycombinator.com/item?id=5480073) | Chardin.js 帮助为应用添加引导说明，向新用户解释页面如何操作。 | 203 | 44 | 2013-04-02 |
| 5 | [Show HN: vim-multiple-cursors - True Sublime Text style multiple selection](https://news.ycombinator.com/item?id=5545946) | vim-multiple-cursors 将 Sublime Text 式多处选择与编辑体验带到 Vim。 | 191 | 37 | 2013-04-14 |
| 6 | [Show HN: HN Store](https://news.ycombinator.com/item?id=5485513) | HN Store 以社区相关项目的形式公开，供读者查看作者这次的作品。 | 190 | 70 | 2013-04-03 |
| 7 | [Show HN: jsdares – learning programming visually](https://news.ycombinator.com/item?id=5584520) | jsdares 用可视化方式教编程，帮助学习者观察代码与结果的关系。 | 177 | 39 | 2013-04-21 |
| 8 | [Show HN: Firepad, an open source collaborative text editor](https://news.ycombinator.com/item?id=5518565) | Firepad 是开源协作文本编辑器，让多人共同修改同一份内容。 | 168 | 63 | 2013-04-09 |
| 9 | [Show HN: Hide Secret Messages In Facebook Photos With My Chrome Extension](https://news.ycombinator.com/item?id=5511417) | 用 Chrome 扩展把秘密消息藏进 Facebook 照片，探索图像中的隐蔽通信。 | 153 | 54 | 2013-04-08 |
| 10 | [Show HN: God mode in production code – a new way to debug in Scala](https://news.ycombinator.com/item?id=5569854) | 作者在 Scala 生产代码中加入“上帝模式”，尝试一种新的调试方式。 | 146 | 81 | 2013-04-18 |

### 2013-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: My seven minute workout timer evening project](https://news.ycombinator.com/item?id=5720648) | 作者展示利用晚间时间制作的七分钟锻炼计时器。 | 760 | 155 | 2013-05-16 |
| 2 | [Show HN: Automatic weekly meal planner, also plans your leftovers](https://news.ycombinator.com/item?id=5640336) | 自动安排每周饮食的工具，连剩菜的后续利用也纳入计划。 | 747 | 288 | 2013-05-01 |
| 3 | [Show HN: Remove backgrounds from images online](https://news.ycombinator.com/item?id=5682831) | 展示可以在线去除图片背景的工具。 | 571 | 140 | 2013-05-09 |
| 4 | [Show HN: I built a self-hosted Basecamp alternative. Try the demo](https://news.ycombinator.com/item?id=5698741) | 自己托管的 Basecamp 替代工具，作者公开演示供读者体验项目协作功能。 | 367 | 197 | 2013-05-13 |
| 5 | [Show HN: Free hi-resolution photos for your website. 10 new photos every 10 days](https://news.ycombinator.com/item?id=5794083) | 每十天提供十张新的免费高分辨率照片，帮助网站找到可用图片素材。 | 357 | 137 | 2013-05-30 |
| 6 | [Show HN: Learn English with movies and TV Shows](https://news.ycombinator.com/item?id=5779473) | 通过电影与电视剧学习英语，让真实对白成为语言练习材料。 | 287 | 158 | 2013-05-28 |
| 7 | [Show HN: Create Javascript charts with one line of Ruby](https://news.ycombinator.com/item?id=5698370) | 用一行 Ruby 生成 JavaScript 图表，作者简化从数据到可视化的过程。 | 272 | 61 | 2013-05-13 |
| 8 | [Show HN: See what the best startups in the world are using](https://news.ycombinator.com/item?id=5736155) | 看看优秀创业公司实际使用哪些工具，作者整理团队的技术与服务选择。 | 261 | 87 | 2013-05-20 |
| 9 | [Show HN: Flattest Route - A web app to help you avoid hills in SF](https://news.ycombinator.com/item?id=5672515) | Flattest Route 帮助旧金山出行者避开陡坡，寻找坡度更平缓的路线。 | 237 | 75 | 2013-05-08 |
| 10 | [Show HN: Weekend project - Magnific Popup](https://news.ycombinator.com/item?id=5643801) | Magnific Popup 是作者周末完成的项目，分享一次轻量工具的开发成果。 | 196 | 64 | 2013-05-02 |

### 2013-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Logos in Pure CSS](https://news.ycombinator.com/item?id=5802043) | 只用 CSS 重现标志图案，作者展示网页样式的造型能力。 | 283 | 74 | 2013-06-01 |
| 2 | [Show HN: Yoleo – A Beautiful RSS Reader](https://news.ycombinator.com/item?id=5826530) | Yoleo 是一款注重视觉体验的 RSS 阅读器，帮助集中阅读订阅内容。 | 269 | 184 | 2013-06-05 |
| 3 | [Show HN: Nightweb, the anonymous P2P social network, now runs on the desktop](https://news.ycombinator.com/item?id=5965691) | 匿名 P2P 社交网络 Nightweb 扩展到桌面，分享移动端之外的使用进展。 | 192 | 63 | 2013-06-30 |
| 4 | [Show HN: Easily add a NSA backdoor to your Rails app](https://news.ycombinator.com/item?id=5845541) | 给 Rails 应用添加所谓 NSA 后门，作者公开这样一项技术演示。 | 188 | 12 | 2013-06-08 |
| 5 | [Show HN: Playable Ultimate Tic Tac Toe](https://news.ycombinator.com/item?id=5902927) | 在浏览器里体验终极井字棋，作者把多层棋盘规则做成可玩游戏。 | 160 | 50 | 2013-06-19 |
| 6 | [Show HN: arkOS - Securely self-hosting your data](https://news.ycombinator.com/item?id=5838873) | arkOS 让用户安全地自行托管数据，尝试增加对个人信息的掌控。 | 156 | 42 | 2013-06-07 |
| 7 | [Show HN: We're releasing SoundBrush, an app that lets you draw music](https://news.ycombinator.com/item?id=5900772) | SoundBrush 让绘画变成音乐创作，用户通过画出形状来探索声音。 | 155 | 64 | 2013-06-18 |
| 8 | [Show HN: I made my Raspberry Pi a secret phone homing server](https://news.ycombinator.com/item?id=5890983) | 用树莓派接收手机回连，作者展示自行搭建隐蔽服务器的实验。 | 139 | 32 | 2013-06-17 |
| 9 | [Show HN: Invoice-o-matic – a free online invoice tool](https://news.ycombinator.com/item?id=5873442) | Invoice-o-matic 提供免费在线发票工具，简化生成账单与开具发票的流程。 | 128 | 88 | 2013-06-13 |
| 10 | [Show HN – Apptimize: A/B testing for native Android, iOS apps](https://news.ycombinator.com/item?id=5939939) | Apptimize 为原生 Android 和 iOS 应用提供 A/B 测试，帮助比较不同产品方案。 | 126 | 50 | 2013-06-25 |

### 2013-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I hacked my microwave with a Raspberry Pi](https://news.ycombinator.com/item?id=6025221) | 作者把树莓派接到微波炉上，展示对家用电器进行改造的硬件实验。 | 423 | 110 | 2013-07-11 |
| 2 | [Show HN: CoreOS, a Linux distro for containers](https://news.ycombinator.com/item?id=6128700) | CoreOS 介绍面向容器的 Linux 发行版，围绕容器运行组织操作系统。 | 417 | 97 | 2013-07-30 |
| 3 | [Show HN: Floobits – Remote pair programming done right](https://news.ycombinator.com/item?id=6064608) | Floobits 支持远程结对编程，尝试让异地开发者像坐在一起那样协作。 | 375 | 135 | 2013-07-18 |
| 4 | [Show HN: Sketch, connect and simulate gears and chains](https://news.ycombinator.com/item?id=6133796) | 画出齿轮与链条后连接并模拟运动，作者展示机械结构的互动设计工具。 | 201 | 58 | 2013-07-31 |
| 5 | [Show HN: Easy Email Encryption inside Gmail (Alpha, Open-Source)](https://news.ycombinator.com/item?id=5981446) | 在 Gmail 中简化邮件加密，作者公开处于早期阶段的开源实现。 | 170 | 98 | 2013-07-02 |
| 6 | [Show HN: Minified.js – a fully-featured, 4K alternative to jQuery and MooTools](https://news.ycombinator.com/item?id=6037170) | Minified.js 用约四 KB 提供丰富功能，作者将其定位为 jQuery 与 MooTools 替代品。 | 158 | 142 | 2013-07-13 |
| 7 | [Show HN: I'm a single founder. Please review my bootstrapped startup](https://news.ycombinator.com/item?id=6059481) | 独立创始人展示自筹资金的创业项目，请社区帮助评估产品。 | 158 | 103 | 2013-07-17 |
| 8 | [Show HN: I made an HN job board](https://news.ycombinator.com/item?id=5985793) | 看到月度招聘帖的热度后，作者为 HN 用户创建专门的岗位信息站。 | 149 | 77 | 2013-07-03 |
| 9 | [Show HN: Chicken chicken chicken – chicken chicken programming language](https://news.ycombinator.com/item?id=5969535) | 围绕 chicken 单词构建的趣味编程语言，作者展示语言实验的荒诞创意。 | 147 | 71 | 2013-07-01 |
| 10 | [Show HN: This page will disappear in 10,000 views](https://news.ycombinator.com/item?id=6114023) | 页面在一万次访问后消失，作者用限次存在的网页探索网络体验。 | 143 | 91 | 2013-07-27 |

### 2013-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: TextBlob, Natural language processing made simple in Python](https://news.ycombinator.com/item?id=6192589) | TextBlob 简化 Python 自然语言处理，帮助开发者更容易操作文本。 | 303 | 46 | 2013-08-10 |
| 2 | [Show HN: Virtual Machines in the Browser](https://news.ycombinator.com/item?id=6219354) | 把虚拟机放进浏览器运行，作者展示网页环境承载计算机的实验。 | 281 | 148 | 2013-08-15 |
| 3 | [Show HN: Tridiv - CSS 3D Editor](https://news.ycombinator.com/item?id=6251671) | Tridiv 是 CSS 三维编辑器，帮助用户构建网页中的立体对象。 | 277 | 59 | 2013-08-21 |
| 4 | [Show HN: noteZilla - Interactive sheet music](https://news.ycombinator.com/item?id=6226607) | noteZilla 让乐谱变成交互式内容，探索阅读谱面与音乐体验的结合。 | 275 | 130 | 2013-08-16 |
| 5 | [Show HN: Run iOS apps in the browser](https://news.ycombinator.com/item?id=6184270) | iOS 应用也能进入浏览器，作者分享让移动程序在网页中运行的方案。 | 261 | 107 | 2013-08-09 |
| 6 | [Show HN: TextIt – Visually build SMS applications anywhere in the world](https://news.ycombinator.com/item?id=6212029) | TextIt 以可视化方式构建短信应用，希望不同地区的人都能方便使用。 | 222 | 62 | 2013-08-14 |
| 7 | [Show HN: Easy to use Wikipedia API for Python](https://news.ycombinator.com/item?id=6279380) | Python 版维基百科 API 工具，简化在程序中获取与操作百科内容。 | 218 | 35 | 2013-08-26 |
| 8 | [Show HN: We structured and compared hospital chargemaster prices](https://news.ycombinator.com/item?id=6221602) | 团队整理医院价目表并进行比较，让原本杂乱的医疗收费更容易查看。 | 171 | 47 | 2013-08-16 |
| 9 | [Show HN: Python library to read and manage your Gmail](https://news.ycombinator.com/item?id=6169040) | 用 Python 读取和管理 Gmail，作者提供面向邮箱操作的开发库。 | 158 | 29 | 2013-08-06 |
| 10 | [Show HN: Highlighting Efforts of Creation from Hacker News](https://news.ycombinator.com/item?id=6291348) | 作者希望突出 HN 中亲手创造的成果，让构建者的努力更容易被发现。 | 149 | 41 | 2013-08-28 |

### 2013-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Ditch Black Text to Read Faster, Easier](https://news.ycombinator.com/item?id=6335784) | 展示通过改变黑色文字呈现方式，让阅读更快、更轻松的工具。 | 739 | 262 | 2013-09-05 |
| 2 | [Show HN: UI Concept – Focus Transition](https://news.ycombinator.com/item?id=6415822) | Focus Transition 展示界面焦点过渡概念，探索交互状态切换的视觉方式。 | 388 | 72 | 2013-09-20 |
| 3 | [Show HN: Wit – Natural language for your app](https://news.ycombinator.com/item?id=6373645) | Wit 帮助应用理解自然语言，尝试把日常表达变成可用的操作输入。 | 321 | 95 | 2013-09-12 |
| 4 | [Show HN: Drawingboard.js](https://news.ycombinator.com/item?id=6444027) | 作者公开 Drawingboard.js 项目，分享自己的 JavaScript 创作成果。 | 233 | 64 | 2013-09-25 |
| 5 | [Show HN: My Isometric GPU-Powered Voxel Engine](https://news.ycombinator.com/item?id=6358394) | GPU 驱动的等距视角体素引擎，作者展示三维块状世界的渲染尝试。 | 203 | 76 | 2013-09-10 |
| 6 | [Show HN: goworker – a faster, Resque-compatible background worker](https://news.ycombinator.com/item?id=6393048) | goworker 是兼容 Resque 的后台工作进程，作者主张其能提供更快的任务处理。 | 179 | 58 | 2013-09-16 |
| 7 | [Show HN: A free collection of maps for every country in the world, in 11 sizes](https://news.ycombinator.com/item?id=6458538) | 免费地图集覆盖世界各国，并提供十一种尺寸，方便按需要选用。 | 157 | 51 | 2013-09-27 |
| 8 | [Show HN: Help programmers from Syria get jobs elsewhere](https://news.ycombinator.com/item?id=6310317) | 作者发起帮助叙利亚程序员到其他地区求职的项目，连接技能与就业机会。 | 155 | 58 | 2013-09-01 |
| 9 | [Show HN: Signal – Edit emails in your Gmail inbox](https://news.ycombinator.com/item?id=6407794) | Signal 允许在 Gmail 收件箱里编辑邮件，作者尝试改变邮箱内容的处理方式。 | 151 | 88 | 2013-09-18 |
| 10 | [Show HN: Very basic Unix-like operating system built when I was younger](https://news.ycombinator.com/item?id=6320509) | 作者分享年轻时编写的基础类 Unix 操作系统，回顾早期系统开发练习。 | 150 | 63 | 2013-09-03 |

### 2013-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: My x86 emulator written in JavaScript](https://news.ycombinator.com/item?id=6567967) | 作者展示用 JavaScript 编写的 x86 模拟器。 | 765 | 190 | 2013-10-17 |
| 2 | [Show HN: "Who is hiring" mapped](https://news.ycombinator.com/item?id=6478793) | 把“谁在招人”帖子中的岗位放到地图上，帮助按地点发现招聘机会。 | 288 | 70 | 2013-10-01 |
| 3 | [Show HN: govuptime.com](https://news.ycombinator.com/item?id=6497366) | 作者介绍 govuptime.com 网站，展示这一围绕政府服务可用性的项目。 | 267 | 168 | 2013-10-04 |
| 4 | [Show HN: Introducing Harp – A static web server with built in preprocessing](https://news.ycombinator.com/item?id=6495287) | Harp 在静态 Web 服务器中内置预处理，让发布页面前的转换更简单。 | 233 | 75 | 2013-10-04 |
| 5 | [Show HN: Sketchology](https://news.ycombinator.com/item?id=6598441) | Sketchology 是作者公开展示的项目，邀请社区查看并交流创作成果。 | 212 | 80 | 2013-10-23 |
| 6 | [Show HN: A Github for writers?](https://news.ycombinator.com/item?id=6617063) | 写作者能否拥有类似 GitHub 的协作平台，作者展示这一方向的产品构思。 | 181 | 81 | 2013-10-26 |
| 7 | [Show HN: Unirest ](https://news.ycombinator.com/item?id=6588802) | 作者向 HN 介绍 Unirest，公开展示这次项目开发的成果。 | 174 | 67 | 2013-10-21 |
| 8 | [Show HN: Hiro – Fast and responsive notetaking meets semantic search](https://news.ycombinator.com/item?id=6478117) | Hiro 结合快速记笔记与语义搜索，帮助记录并重新找到自己的想法。 | 160 | 83 | 2013-10-01 |
| 9 | [Show HN: Gmelius – No Ads and Better User Interface for Gmail](https://news.ycombinator.com/item?id=6633273) | Gmelius 移除 Gmail 广告并改进界面，尝试提供更清爽的邮箱体验。 | 160 | 112 | 2013-10-29 |
| 10 | [Show HN: Native apps for the browser](https://news.ycombinator.com/item?id=6490841) | 把原生应用体验带进浏览器，作者探索网页平台承载应用的新方式。 | 152 | 58 | 2013-10-03 |

### 2013-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Probabilistically Generating HN Post Titles](https://news.ycombinator.com/item?id=6815282) | 展示以概率方式生成 Hacker News 帖子标题的项目。 | 683 | 260 | 2013-11-28 |
| 2 | [Show HN: I'm working on an open-source Gmail replacement](https://news.ycombinator.com/item?id=6681238) | 一个开源 Gmail 替代项目正在开发，作者邀请社区了解其进展。 | 387 | 180 | 2013-11-06 |
| 3 | [Show HN: Hosted Docker-as-a-Service on SSDs for $5](https://news.ycombinator.com/item?id=6691316) | 五美元的托管 Docker 服务使用 SSD 存储，团队介绍这一云端运行方案。 | 387 | 132 | 2013-11-07 |
| 4 | [Show HN: Gitter – Chat for GitHub](https://news.ycombinator.com/item?id=6739074) | Gitter 为 GitHub 社区提供聊天空间，让代码协作之外的交流更直接。 | 243 | 109 | 2013-11-15 |
| 5 | [Show HN: Real-time file sharing site](https://news.ycombinator.com/item?id=6670113) | 文件分享网站主打实时传递，让用户快速把所需文件发送给别人。 | 218 | 97 | 2013-11-04 |
| 6 | [Show HN: DotNetFiddle – JsFiddle for .Net](https://news.ycombinator.com/item?id=6767883) | DotNetFiddle 把 JsFiddle 式在线试验环境带给 .NET 开发者。 | 217 | 88 | 2013-11-20 |
| 7 | [Show HN: Gmail.js – JavaScript API for Gmail](https://news.ycombinator.com/item?id=6810458) | Gmail.js 为 Gmail 提供 JavaScript API，方便通过代码与邮箱交互。 | 212 | 56 | 2013-11-27 |
| 8 | [Show HN: My new project - ask.io](https://news.ycombinator.com/item?id=6754982) | ask.io 是作者刚公开的新项目，邀请社区查看这次开发尝试。 | 206 | 106 | 2013-11-18 |
| 9 | [Show HN: MMORPG in 55KB of Javascript](https://news.ycombinator.com/item?id=6764962) | 仅用五十五 KB JavaScript 实现多人在线角色扮演游戏，展示紧凑的游戏开发。 | 178 | 51 | 2013-11-19 |
| 10 | [Show HN: A game I've been working on for the last year is out today](https://news.ycombinator.com/item?id=6749726) | 开发一年的游戏终于上线，作者分享从长期制作到正式发布的时刻。 | 165 | 64 | 2013-11-17 |

### 2013-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I mapped US medical prices. Save thousands by driving a few miles](https://news.ycombinator.com/item?id=6864584) | 作者把美国医疗价格放到地图上，帮助比较附近机构的收费差异。 | 488 | 222 | 2013-12-06 |
| 2 | [Show HN: I made an HN for the financial industry](https://news.ycombinator.com/item?id=6844565) | 为金融行业做一个类似 Hacker News 的社区，集中交流行业新闻与讨论。 | 422 | 156 | 2013-12-04 |
| 3 | [Show HN: Myth – CSS the way it was imagined](https://news.ycombinator.com/item?id=6923141) | Myth 围绕 CSS 开发体验展开，作者展示自己理想中的样式工具。 | 357 | 152 | 2013-12-17 |
| 4 | [Show HN: Minecraft clone in 2500 lines of C - even supports multiplayer online](https://news.ycombinator.com/item?id=6878565) | 两千五百行 C 写出 Minecraft 克隆，还能多人联机，作者展示精简实现。 | 287 | 149 | 2013-12-10 |
| 5 | [Show HN: Life – A timeline of important events in (your) life](https://news.ycombinator.com/item?id=6833565) | Life 用时间线记录人生重要事件，帮助把个人经历组织成可回看的脉络。 | 268 | 94 | 2013-12-02 |
| 6 | [Show HN: I made 30 apps this year and I'm 15](https://news.ycombinator.com/item?id=6985700) | 十五岁作者一年制作三十款应用，分享密集实践后的开发成果。 | 206 | 141 | 2013-12-30 |
| 7 | [Show HN: tyto](https://news.ycombinator.com/item?id=6886834) | tyto 是作者此次公开的项目名称，原帖邀请社区查看这项作品。 | 179 | 122 | 2013-12-11 |
| 8 | [Show HN: Bitrated – Bitcoin m-of-n arbitrated transactions](https://news.ycombinator.com/item?id=6842697) | Bitrated 为比特币提供多签仲裁交易，探索交易双方与仲裁者共同参与的机制。 | 155 | 72 | 2013-12-03 |
| 9 | [Show HN: Vector - A High-Level Programming Language for GPU Computing](https://news.ycombinator.com/item?id=6946821) | Vector 是面向 GPU 计算的高层编程语言，尝试降低并行程序的编写门槛。 | 142 | 54 | 2013-12-21 |
| 10 | [Show HN: I've launched my iPhone journal app I've worked on for almost 2 years.](https://news.ycombinator.com/item?id=6858373) | 开发近两年的 iPhone 自动日记终于发布，作者尝试用照片帮助保存生活记录。 | 139 | 116 | 2013-12-06 |

### 2014-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Kimono – Never write a web scraper again](https://news.ycombinator.com/item?id=7066479) | Kimono 希望让用户无需亲自编写网页抓取程序即可提取数据。 | 717 | 230 | 2014-01-15 |
| 2 | [Show HN: I open-sourced my web app alternative to Illustrator](https://news.ycombinator.com/item?id=7116042) | 作者开源自己的网页绘图工具，提供 Illustrator 之外的实现选择。 | 644 | 92 | 2014-01-24 |
| 3 | [Show HN: Product Hunt – Hacker News for Products](https://news.ycombinator.com/item?id=7144815) | Product Hunt 用类似 HN 的社区形式发现产品，让新作品集中亮相。 | 360 | 101 | 2014-01-29 |
| 4 | [Show HN: Random Street View](https://news.ycombinator.com/item?id=7130192) | 随机跳到一个街景地点，作者用简单工具鼓励漫无目的地探索世界。 | 356 | 166 | 2014-01-27 |
| 5 | [Show HN: We just open-sourced a Skype replacement with HTML5](https://news.ycombinator.com/item?id=7159896) | 团队开源基于 HTML5 的 Skype 替代项目，尝试在网页技术上实现通信。 | 303 | 100 | 2014-01-31 |
| 6 | [Show HN: Given an API, Generate client libraries in Node, Python, PHP, Ruby](https://news.ycombinator.com/item?id=7005348) | 给定 REST API 后生成多种语言的客户端库，覆盖 Node、Python、PHP 与 Ruby。 | 268 | 73 | 2014-01-03 |
| 7 | [Show HN: Use any text as a domain name](https://news.ycombinator.com/item?id=6996398) | 作者尝试让任意文本充当域名，探索网址命名与访问的新形式。 | 261 | 141 | 2014-01-01 |
| 8 | [Show HN: Ridiculously cheap bulk geocoding](https://news.ycombinator.com/item?id=7095228) | 以低成本批量执行地理编码，帮助把大量地址转成可用于地图的数据。 | 224 | 101 | 2014-01-21 |
| 9 | [Show HN: Linux server monitoring web dashboard](https://news.ycombinator.com/item?id=7125153) | 通过网页仪表盘监控 Linux 服务器，把主机状态集中到浏览器中查看。 | 175 | 68 | 2014-01-26 |
| 10 | [Show HN: Funded.io rapid prototype](https://news.ycombinator.com/item?id=7059919) | Funded.io 的快速原型公开展示，作者邀请社区查看早期实现。 | 167 | 58 | 2014-01-14 |

### 2014-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: thedaywefightback.js](https://news.ycombinator.com/item?id=7185024) | 作者发布 thedaywefightback.js，展示这一主题的 JavaScript 项目。 | 472 | 135 | 2014-02-05 |
| 2 | [Show HN: JS library to make your website instant](https://news.ycombinator.com/item?id=7201353) | InstantClick 尝试让网页切换更即时，用 JavaScript 改善站点加载感受。 | 426 | 174 | 2014-02-08 |
| 3 | [Show HN: I redesigned the Microsoft employee badge](https://news.ycombinator.com/item?id=7254786) | 重新设计微软员工工牌，作者展示企业身份卡片的视觉改造。 | 322 | 152 | 2014-02-17 |
| 4 | [Show HN: We've open-sourced our bootstrapped startup, ShareLaTeX](https://news.ycombinator.com/item?id=7276263) | ShareLaTeX 团队将自筹资金的创业项目开源，让社区可以研究与继续开发。 | 276 | 79 | 2014-02-21 |
| 5 | [Show HN: Siri-as-a-Service Speech API](https://news.ycombinator.com/item?id=7224436) | 以“Siri 即服务”为定位提供语音 API，帮助应用接入语音相关能力。 | 242 | 60 | 2014-02-12 |
| 6 | [Show HN: A simple IP address API](https://news.ycombinator.com/item?id=7239333) | 一个简单的 IP 地址 API，方便开发者在程序里获取所需地址信息。 | 241 | 117 | 2014-02-14 |
| 7 | [Show HN: Add forms to your static site – no iFrames required](https://news.ycombinator.com/item?id=7298195) | 无需嵌入 iframe，也能给静态网站加表单，作者展示轻量交互方案。 | 233 | 99 | 2014-02-25 |
| 8 | [Show HN: I built this game alone – design, code, music, sound, marketing](https://news.ycombinator.com/item?id=7191187) | 从设计、代码到音乐和营销都由一人完成，作者分享独立制作的游戏。 | 214 | 76 | 2014-02-06 |
| 9 | [Show HN: Codewars](https://news.ycombinator.com/item?id=7186459) | 作者向社区介绍 Codewars，展示这项新近公开的项目。 | 198 | 121 | 2014-02-05 |
| 10 | [Show HN: Google Music for Mac](https://news.ycombinator.com/item?id=7282934) | 把 Google Music 带到 Mac 桌面，作者展示专用音乐应用。 | 193 | 99 | 2014-02-22 |

### 2014-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: My Isometric Voxel Engine 6 Months Later](https://news.ycombinator.com/item?id=7487935) | 等距体素引擎开发六个月后有了哪些变化，作者再次公开项目进展。 | 435 | 132 | 2014-03-28 |
| 2 | [Show HN: A sequence of online courses to learn web development from scratch](https://news.ycombinator.com/item?id=7501516) | 从零学习网页开发，作者整理一套按顺序推进的在线课程路线。 | 368 | 107 | 2014-03-31 |
| 3 | [Show HN: I've been making one HTML5 game per week. Here's my 10th game](https://news.ycombinator.com/item?id=7386672) | 坚持每周制作一款 HTML5 游戏，作者展示连续实践中的第十件作品。 | 362 | 148 | 2014-03-12 |
| 4 | [Show HN: Real-time server monitoring in your browser](https://news.ycombinator.com/item?id=7375696) | 直接在浏览器实时观察服务器状态，作者分享网页监控工具。 | 346 | 115 | 2014-03-10 |
| 5 | [Show HN: My new JavaScript MVC framework](https://news.ycombinator.com/item?id=7421652) | 作者设计新的 JavaScript MVC 框架，公开自己的应用组织方案。 | 304 | 159 | 2014-03-18 |
| 6 | [Show HN: A visual HTML5 animation editor in your browser](https://news.ycombinator.com/item?id=7360296) | HTML5 动画编辑器运行在浏览器中，通过可视化方式制作网页动画。 | 295 | 139 | 2014-03-07 |
| 7 | [Show HN: My current App Store Featured Game was written entirely in Scheme](https://news.ycombinator.com/item?id=7361947) | App Store 推荐游戏完全用 Scheme 编写，作者分享不同寻常的语言选择。 | 290 | 110 | 2014-03-07 |
| 8 | [Show HN: Softcover – A publishing platform from the author of the Rails Tutorial](https://news.ycombinator.com/item?id=7350265) | 《Rails Tutorial》作者推出 Softcover，介绍新的内容出版平台。 | 208 | 61 | 2014-03-05 |
| 9 | [Show HN: My Desk Chair](https://news.ycombinator.com/item?id=7392320) | 一把办公椅也能成为 Show HN 的主角，作者分享自己的桌边座椅。 | 203 | 152 | 2014-03-13 |
| 10 | [Show HN: Fresh-baked rustic sourdough bread, delivered within 20 minutes](https://news.ycombinator.com/item?id=7454242) | 现烤乡村酸面包承诺二十分钟送达，作者展示贴近本地生活的小生意。 | 199 | 145 | 2014-03-23 |

### 2014-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Untrusted, a JavaScript adventure game you play by modifying its source](https://news.ycombinator.com/item?id=7547942) | Untrusted 让玩家通过修改 JavaScript 源码闯关，把编程融入冒险游戏。 | 555 | 235 | 2014-04-07 |
| 2 | [Show HN: GitBook – Build beautiful programming books using GitHub and Markdown](https://news.ycombinator.com/item?id=7524956) | GitBook 结合 GitHub 与 Markdown，帮助作者制作和发布编程书籍。 | 442 | 78 | 2014-04-03 |
| 3 | [Show HN: Super Planet Crash](https://news.ycombinator.com/item?id=7591094) | Super Planet Crash 作为新作品亮相，作者请社区体验自己的项目。 | 349 | 126 | 2014-04-15 |
| 4 | [Show HN: Betatype - A freelance site where clients pay $3,500 for prototypes](https://news.ycombinator.com/item?id=7664240) | Betatype 将客户与自由职业者连接，围绕三千五百美元的原型项目组织合作。 | 285 | 142 | 2014-04-29 |
| 5 | [Show HN: InstaMotor – Taking the pain out of selling your car](https://news.ycombinator.com/item?id=7533368) | InstaMotor 希望减少卖车的麻烦，作者介绍面向二手车交易的产品。 | 234 | 208 | 2014-04-04 |
| 6 | [Show HN: Turn sketches on paper into app prototypes](https://news.ycombinator.com/item?id=7666102) | 把纸上草图转换成应用原型，让手绘构思更快变为可体验的界面。 | 222 | 74 | 2014-04-29 |
| 7 | [Show HN: An open-source, Raspberry-Pi-based Siri alternative](https://news.ycombinator.com/item?id=7546858) | 基于树莓派制作开源 Siri 替代方案，尝试自行掌控语音助手。 | 191 | 81 | 2014-04-07 |
| 8 | [Show HN: Digitizing photos of whiteboards using the command line](https://news.ycombinator.com/item?id=7520216) | 通过命令行把白板照片数字化，帮助把随手拍摄的内容处理成清晰资料。 | 186 | 36 | 2014-04-03 |
| 9 | [Show HN: Isomer – An isometric graphics library for HTML5 Canvas](https://news.ycombinator.com/item?id=7652874) | Isomer 为 HTML5 Canvas 提供等距图形库，方便绘制立体风格的图形。 | 181 | 23 | 2014-04-26 |
| 10 | [Show HN: Sysdig, a tool for Linux system exploration](https://news.ycombinator.com/item?id=7524144) | Sysdig 用于探索 Linux 系统行为，帮助观察机器内部正在发生什么。 | 171 | 48 | 2014-04-03 |

### 2014-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Hipster Domain Finder](https://news.ycombinator.com/item?id=7707100) | Hipster Domain Finder 围绕新颖域名展开，帮助寻找有个性的网络名字。 | 237 | 123 | 2014-05-06 |
| 2 | [Show HN: Where Adblock+ injects 20K CSS rules, HTTPSB injects one](https://news.ycombinator.com/item?id=7765758) | 作者比较 Adblock+ 与 HTTPSB 的样式注入量，展示自己减少 CSS 规则的方案。 | 221 | 178 | 2014-05-19 |
| 3 | [Show HN: Turn an email to a web page](https://news.ycombinator.com/item?id=7706915) | 把一封邮件直接转换成网页，作者尝试简化内容发布的入口。 | 197 | 74 | 2014-05-06 |
| 4 | [Show HN: The static, static site generator](https://news.ycombinator.com/item?id=7767779) | 名为 static 的静态网站生成器公开，作者分享自己的网页发布工具。 | 187 | 96 | 2014-05-19 |
| 5 | [Show HN: Mighty Spring – Passive job search](https://news.ycombinator.com/item?id=7823167) | Mighty Spring 围绕被动求职设计，让用户在不主动投递时也能接触工作机会。 | 159 | 54 | 2014-05-30 |
| 6 | [Show HN: Wesnoth – Free, turn-based strategy game ](https://news.ycombinator.com/item?id=7741564) | Wesnoth 是免费回合制策略游戏，作者邀请社区体验其战术对战。 | 146 | 60 | 2014-05-14 |
| 7 | [Show HN: Take It Apart](https://news.ycombinator.com/item?id=7752537) | Take It Apart 是这次分享的项目，作者把作品带到社区公开交流。 | 146 | 59 | 2014-05-15 |
| 8 | [Show HN: OpenRA – RTS project that recreates Command and Conquer games](https://news.ycombinator.com/item?id=7730555) | OpenRA 用开源实时战略引擎重现《命令与征服》系列游戏的体验。 | 131 | 40 | 2014-05-12 |
| 9 | [Show HN: Font Awesome to PNG](https://news.ycombinator.com/item?id=7805594) | 将 Font Awesome 图标转成 PNG，帮助在需要位图的场景继续使用图标。 | 128 | 48 | 2014-05-27 |
| 10 | [Show HN: Richard Dawkins’ Biomorphs Implemented in JavaScript](https://news.ycombinator.com/item?id=7822894) | 用 JavaScript 实现 Richard Dawkins 的 Biomorphs，探索形态演化的可视化实验。 | 117 | 18 | 2014-05-30 |

### 2014-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Wavepot – Digital audio workstation of the web](https://news.ycombinator.com/item?id=7905910) | Wavepot 将数字音频工作站带到网页中。 | 625 | 132 | 2014-06-17 |
| 2 | [Show HN: We put an iPhone on the front wheel of a car](https://news.ycombinator.com/item?id=7904658) | 把 iPhone 安装到汽车前轮，团队展示一次不同寻常的设备实验。 | 380 | 108 | 2014-06-17 |
| 3 | [Show HN: Card – An interactive CSS3 credit card form](https://news.ycombinator.com/item?id=7847440) | Card 用 CSS3 把信用卡表单做成交互卡片，改善填写支付信息时的视觉反馈。 | 376 | 112 | 2014-06-04 |
| 4 | [Show HN: Fast.js – faster reimplementations of native JavaScript functions](https://news.ycombinator.com/item?id=7937258) | Fast.js 重新实现部分 JavaScript 原生函数，作者希望获得更快的执行速度。 | 323 | 162 | 2014-06-24 |
| 5 | [Show HN: Vim Awesome – Vim plugins](https://news.ycombinator.com/item?id=7951020) | Vim Awesome 汇集 Vim 插件，帮助用户发现并选择适合自己的编辑器扩展。 | 222 | 52 | 2014-06-26 |
| 6 | [Show HN: HTML5 guitar lessons with pitch detection](https://news.ycombinator.com/item?id=7965784) | HTML5 吉他课程加入音高检测，让网页能够反馈用户实际弹奏的声音。 | 218 | 59 | 2014-06-30 |
| 7 | [Show HN: Create pretty resumes in HTML, Latex, Markdown from a single JSON](https://news.ycombinator.com/item?id=7862578) | 一份 JSON 同时生成 HTML、LaTeX 与 Markdown 简历，减少多版本重复维护。 | 187 | 49 | 2014-06-07 |
| 8 | [Show HN: Bounce.js – A tool for generating CSS3 animations](https://news.ycombinator.com/item?id=7868368) | Bounce.js 帮助生成 CSS3 动画，让设计运动效果不必从零手写样式。 | 172 | 32 | 2014-06-09 |
| 9 | [Show HN: zzzz.io, a free DynDNS replacement I created on the weekend](https://news.ycombinator.com/item?id=7844264) | 周末制作 zzzz.io，作者提供免费的动态 DNS 替代服务。 | 156 | 70 | 2014-06-04 |
| 10 | [Show HN: Automatically convert a website to Android and iOS](https://news.ycombinator.com/item?id=7858296) | 把现有网站自动转换成 Android 和 iOS 应用，探索跨平台发布的便捷路径。 | 148 | 75 | 2014-06-06 |

### 2014-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Show HN](https://news.ycombinator.com/item?id=7984826) | HN 推出专门汇集用户作品展示的 Show HN 页面。 | 1302 | 166 | 2014-07-03 |
| 2 | [Show HN: Markov chains explained visually](https://news.ycombinator.com/item?id=8103240) | 用可视化方式解释马尔可夫链如何运作。 | 1070 | 92 | 2014-07-29 |
| 3 | [Show HN: OneBody Church Directory software I've been hacking on for 7 years](https://news.ycombinator.com/item?id=8085213) | 作者展示自己持续开发七年的教会通讯录软件 OneBody。 | 1020 | 304 | 2014-07-25 |
| 4 | [Show HN: Pangoly – Build your shiny new PC](https://news.ycombinator.com/item?id=8036648) | Pangoly 帮助用户规划并组装一台新电脑。 | 778 | 213 | 2014-07-15 |
| 5 | [Show HN: NomadList – The best cities to live and work remotely in](https://news.ycombinator.com/item?id=8107222) | NomadList 帮助远程工作者比较适合生活和工作的城市。 | 639 | 298 | 2014-07-30 |
| 6 | [Show HN: Free, anonymous coding interview practice](https://news.ycombinator.com/item?id=7978075) | 免费匿名练习编程面试，让求职者在正式面试前获得实际演练机会。 | 604 | 215 | 2014-07-02 |
| 7 | [Show HN: Sysadmin Casts – simple bite-sized sysadmin screencasts](https://news.ycombinator.com/item?id=8011081) | Sysadmin Casts 用短小录屏讲系统管理，方便按具体问题学习运维技能。 | 443 | 80 | 2014-07-09 |
| 8 | [Show HN: Breach – A modular browser built on Chromium and Node.js](https://news.ycombinator.com/item?id=8016307) | Breach 结合 Chromium 和 Node.js 构建模块化浏览器，探索可扩展的浏览器结构。 | 405 | 169 | 2014-07-10 |
| 9 | [Show HN: Hacker News Redesign](https://news.ycombinator.com/item?id=8004839) | 重新设计 Hacker News 界面，作者展示对社区页面布局与使用体验的改造。 | 380 | 198 | 2014-07-08 |
| 10 | [Show HN: Papa Parse 3](https://news.ycombinator.com/item?id=8042051) | Papa Parse 发布第三版，作者向社区展示项目的新版进展。 | 363 | 83 | 2014-07-16 |

### 2014-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I got hacked, felt paranoid, made an app – GlassWire](https://news.ycombinator.com/item?id=8222652) | 遭到入侵后，作者因安全焦虑而制作了应用 GlassWire。 | 1013 | 331 | 2014-08-25 |
| 2 | [Show HN: Put “GIF” in front of any YouTube URL and hit enter](https://news.ycombinator.com/item?id=8187791) | 在 YouTube 网址前加上“GIF”，即可使用相关视频转换服务。 | 577 | 181 | 2014-08-16 |
| 3 | [Show HN: Stressed and burned out, so I created my first app – Remember Win](https://news.ycombinator.com/item?id=8173934) | 压力与倦怠促使作者制作首款应用 Remember Win，分享这次个人创作的起点。 | 455 | 97 | 2014-08-13 |
| 4 | [Show HN: Stellar – Git for PostreSQL and MySQL](https://news.ycombinator.com/item?id=8211575) | Stellar 把 Git 式思路用于 PostgreSQL 与 MySQL，探索数据库管理的新方式。 | 325 | 77 | 2014-08-22 |
| 5 | [Show HN: A virtual whiteboard for working or teaching remotely](https://news.ycombinator.com/item?id=8206855) | 虚拟白板支持远程工作与教学，让异地参与者共同书写和表达想法。 | 309 | 140 | 2014-08-21 |
| 6 | [Show HN: I'm building a game for the Nintendo GameBoy](https://news.ycombinator.com/item?id=8178660) | 作者正在为任天堂 Game Boy 制作游戏，分享面向经典掌机的开发尝试。 | 260 | 102 | 2014-08-14 |
| 7 | [Show HN: Restore tmux environment after a system restart](https://news.ycombinator.com/item?id=8246218) | 系统重启后恢复 tmux 工作环境，减少重新打开会话与窗口的重复操作。 | 241 | 43 | 2014-08-30 |
| 8 | [Show HN: Satellizer – Authentication for AngularJS](https://news.ycombinator.com/item?id=8192801) | Satellizer 为 AngularJS 应用提供认证支持，帮助处理用户登录需求。 | 221 | 34 | 2014-08-18 |
| 9 | [Show HN: Pythonpy – the swiss army knife of the command line](https://news.ycombinator.com/item?id=8158976) | Pythonpy 把 Python 带入命令行日常操作，作者将其比作终端里的瑞士军刀。 | 220 | 42 | 2014-08-10 |
| 10 | [Show HN: A small virtual machine written in C](https://news.ycombinator.com/item?id=8130413) | 用 C 编写小型虚拟机，作者公开自己的底层实现实验。 | 212 | 91 | 2014-08-04 |

### 2014-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Javelin Browser](https://news.ycombinator.com/item?id=8368199) | 作者介绍 Javelin 浏览器，展示新的网页浏览项目。 | 373 | 132 | 2014-09-25 |
| 2 | [Show HN: Airtable, a real-time spreadsheet-database hybrid](https://news.ycombinator.com/item?id=8373914) | Airtable 将实时电子表格与数据库结合，尝试让数据组织兼具直观与结构化。 | 361 | 125 | 2014-09-26 |
| 3 | [Show HN: Famous Outfits](https://news.ycombinator.com/item?id=8270951) | Famous Outfits 向 HN 读者公开亮相，原帖展示这项新作品。 | 358 | 201 | 2014-09-04 |
| 4 | [Show HN: CloudTunes](https://news.ycombinator.com/item?id=8284785) | CloudTunes 是作者此次带来的项目，供读者查看并交流。 | 307 | 91 | 2014-09-08 |
| 5 | [Show HN: CleverDeck – I built the spaced repetition app I always wanted](https://news.ycombinator.com/item?id=8331233) | CleverDeck 是作者理想中的间隔重复应用，用分散复习帮助长期记忆。 | 305 | 135 | 2014-09-17 |
| 6 | [Show HN: Picnic.css, a lightweight Bootstrap alternative](https://news.ycombinator.com/item?id=8315616) | Picnic.css 尝试以轻量方式替代 Bootstrap，作者邀请评估样式与兼容性。 | 247 | 143 | 2014-09-14 |
| 7 | [Show HN: Creddle – Paper-friendly web resumes](https://news.ycombinator.com/item?id=8284616) | Creddle 制作适合纸张打印的网络简历，兼顾线上展示与线下递交。 | 225 | 111 | 2014-09-08 |
| 8 | [Show HN: ContentBuilder.js – JQuery Plugin to Write Anything Beautifully](https://news.ycombinator.com/item?id=8315224) | ContentBuilder.js 用 jQuery 插件帮助编排内容，追求更美观的写作呈现。 | 189 | 48 | 2014-09-14 |
| 9 | [Show HN: Real-time Fare Estimate Comparisons for Uber, Lyft, Sidecar, and Taxi](https://news.ycombinator.com/item?id=8299511) | 实时比较 Uber、Lyft、Sidecar 与出租车预估费用，帮助出发前选择出行方式。 | 181 | 65 | 2014-09-10 |
| 10 | [Show HN: Bootstrappers.io – A community for business bootstrappers](https://news.ycombinator.com/item?id=8267675) | Bootstrappers.io 为自筹资金经营生意的人提供社区，交流自主创业的经验。 | 161 | 56 | 2014-09-04 |

### 2014-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Open-Source, Free, Agile Project Management Tool](https://news.ycombinator.com/item?id=8395689) | 免费的开源敏捷项目管理工具，帮助团队自行组织任务和跟踪进展。 | 436 | 134 | 2014-10-01 |
| 2 | [Show HN: Nightmare – Simple browser automation](https://news.ycombinator.com/item?id=8416693) | Nightmare 简化浏览器自动化，帮助用程序完成重复的网页操作。 | 429 | 70 | 2014-10-06 |
| 3 | [Show HN: Speeding up PostgreSQL through vectorized execution](https://news.ycombinator.com/item?id=8423825) | 用向量化执行加速 PostgreSQL，展示数据库执行层的性能探索。 | 332 | 36 | 2014-10-07 |
| 4 | [Show HN: “Install on DigitalOcean” button for open source apps](https://news.ycombinator.com/item?id=8538813) | 为开源应用加上“一键安装到 DigitalOcean”按钮，简化部署流程。 | 279 | 54 | 2014-10-31 |
| 5 | [Show HN: ReadMe.io – Beautiful Documentation Made Easy](https://news.ycombinator.com/item?id=8422408) | ReadMe.io 希望让漂亮、易用的项目文档更容易制作。 | 266 | 79 | 2014-10-07 |
| 6 | [Show HN: HTML5 online animation editor that exports to SVG and SMIL](https://news.ycombinator.com/item?id=8426984) | 在浏览器里制作 HTML5 动画，并导出为 SVG 和 SMIL。 | 239 | 52 | 2014-10-08 |
| 7 | [Show HN: Sail boat simulation – try to sail into the wind](https://news.ycombinator.com/item?id=8427086) | 试着驾驶模拟帆船迎风航行，体验风向如何影响操船。 | 229 | 83 | 2014-10-08 |
| 8 | [Show HN: RemoteCoder.io – A jobsite for remote programmers](https://news.ycombinator.com/item?id=8464074) | RemoteCoder.io 专门为程序员寻找远程工作机会。 | 220 | 136 | 2014-10-16 |
| 9 | [Show HN: VirtKick – Self-hosted Digital Ocean](https://news.ycombinator.com/item?id=8527185) | VirtKick 展示可自行托管、类似 DigitalOcean 的云管理方案。 | 216 | 92 | 2014-10-29 |
| 10 | [Show HN: A curated list of Chrome DevTools tips and tricks](https://news.ycombinator.com/item?id=8426558) | 整理 Chrome 开发者工具的实用技巧，方便开发者查阅。 | 212 | 24 | 2014-10-08 |

### 2014-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Meet me, I'll buy you coffee](https://news.ycombinator.com/item?id=8592597) | 作者邀请陌生人见面喝咖啡，用一杯咖啡开启交流。 | 427 | 199 | 2014-11-11 |
| 2 | [Show HN: Projects from “Stupid Shit No One Needs and Terrible Ideas” Hackathon](https://news.ycombinator.com/item?id=8621886) | 一场专做无用东西和糟糕点子的黑客松，会产出什么作品？ | 424 | 96 | 2014-11-18 |
| 3 | [Show HN: Explained Visually](https://news.ycombinator.com/item?id=8608358) | Explained Visually 尝试用直观图像解释概念。 | 353 | 45 | 2014-11-14 |
| 4 | [Show HN: A database for browsing and discovering movies](https://news.ycombinator.com/item?id=8547351) | 一个帮助用户浏览电影、发现新片的电影数据库。 | 296 | 157 | 2014-11-02 |
| 5 | [Show HN: How I made the print and eBook versions of my web book](https://news.ycombinator.com/item?id=8555285) | 作者分享如何把自己的网络书制作成纸质版和电子书。 | 228 | 66 | 2014-11-04 |
| 6 | [Show HN: StackShare – discover and discuss software stacks](https://news.ycombinator.com/item?id=8568181) | StackShare 让开发者发现、分享和讨论软件技术栈。 | 218 | 75 | 2014-11-06 |
| 7 | [Show HN: QuaggaJS, a barcode scanner written in JavaScript](https://news.ycombinator.com/item?id=8657454) | QuaggaJS 用 JavaScript 实现条码扫描功能。 | 168 | 27 | 2014-11-25 |
| 8 | [Show HN: C# 6.0 Functional Language Extensions](https://news.ycombinator.com/item?id=8631158) | 为 C# 6.0 增加函数式编程扩展，探索另一种写代码方式。 | 164 | 87 | 2014-11-19 |
| 9 | [Show HN: Balls – Game I’ve made while I was learning Swift](https://news.ycombinator.com/item?id=8556056) | 作者在学习 Swift 时制作了 Balls 游戏，展示学习成果。 | 163 | 64 | 2014-11-04 |
| 10 | [Show HN: TrueJob – OkCupid for Jobs](https://news.ycombinator.com/item?id=8644172) | TrueJob 把类似 OkCupid 的匹配思路用在求职招聘中。 | 161 | 63 | 2014-11-22 |

### 2014-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Front-end framework optimized for internal apps](https://news.ycombinator.com/item?id=8699167) | 一个专门针对企业内部应用需求优化的前端框架。 | 438 | 93 | 2014-12-04 |
| 2 | [Show HN: Initial release of H2O, and why HTTPD performance will matter in 2015](https://news.ycombinator.com/item?id=8797155) | H2O 首次发布，作者同时讨论为何看好 2015 年 HTTP 服务性能的重要性。 | 251 | 83 | 2014-12-25 |
| 3 | [Show HN: PSequel – a free PostgreSQL GUI Tool for Mac OS X](https://news.ycombinator.com/item?id=8683405) | PSequel 为 Mac 用户提供免费的 PostgreSQL 图形管理工具。 | 247 | 109 | 2014-12-01 |
| 4 | [Show HN: Artful for Mac](https://news.ycombinator.com/item?id=8723120) | 作者展示面向 Mac 的 Artful 应用，邀请社区了解项目。 | 229 | 145 | 2014-12-09 |
| 5 | [Show HN: Iota – a text editor written in Rust](https://news.ycombinator.com/item?id=8734307) | Iota 是用 Rust 编写的文本编辑器，展示早期实现。 | 221 | 45 | 2014-12-11 |
| 6 | [Show HN: Wysihtml – Open-source rich text editor for web apps](https://news.ycombinator.com/item?id=8766865) | Wysihtml 为 Web 应用提供开源富文本编辑能力。 | 215 | 45 | 2014-12-18 |
| 7 | [Show HN: Gitfs – mount Git repos as local folders](https://news.ycombinator.com/item?id=8735937) | 把 Git 仓库挂载成本地文件夹，用文件系统方式访问代码。 | 196 | 62 | 2014-12-11 |
| 8 | [Show HN: Code Words, a quarterly publication about programming](https://news.ycombinator.com/item?id=8707583) | Code Words 是一份每季度出版、围绕编程主题的刊物。 | 181 | 71 | 2014-12-05 |
| 9 | [Show HN: Comments by Top HN Posters Analysed by IBM's Watson User Modelling API](https://news.ycombinator.com/item?id=8745263) | 作者用 IBM Watson 用户建模 API 分析 HN 活跃发帖者的评论。 | 180 | 90 | 2014-12-13 |
| 10 | [Show HN: ssh chat.shazow.net](https://news.ycombinator.com/item?id=8743374) | 通过 SSH 进入 IRC 风格聊天室，终端用户名和密钥直接充当身份。 | 171 | 45 | 2014-12-12 |

### 2015-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Hacker News' “most unique support email of 2014”](https://news.ycombinator.com/item?id=8920613) | 作者重启尘封的 Palm Treo 600，由此分享一封特别的支持邮件。 | 401 | 112 | 2015-01-21 |
| 2 | [Show HN: Snabbt.js – a minimalistic animation library](https://news.ycombinator.com/item?id=8823938) | Snabbt.js 提供简洁的动画库，展示轻量动画实现思路。 | 323 | 47 | 2015-01-01 |
| 3 | [Show HN: Building terminal dashboards using ASCII/ANSI art and JavaScript](https://news.ycombinator.com/item?id=8888089) | 用 JavaScript 与 ASCII、ANSI 字符画搭建终端仪表盘。 | 305 | 55 | 2015-01-14 |
| 4 | [Show HN: WordsAPI](https://news.ycombinator.com/item?id=8840173) | 作者展示 WordsAPI，围绕词语提供可调用的接口。 | 263 | 75 | 2015-01-05 |
| 5 | [Show HN: App for Falling in Love](https://news.ycombinator.com/item?id=8869305) | 一个围绕“坠入爱河”设计的应用，展示作者的产品尝试。 | 252 | 116 | 2015-01-11 |
| 6 | [Show HN: Adopted a dog, had no clue what meds she needed, did some research](https://news.ycombinator.com/item?id=8907801) | 领养狗后弄不清该用什么药，作者把自己的调查做成了项目。 | 252 | 73 | 2015-01-18 |
| 7 | [Show HN: LibreBoard – An open-source clone of Trello](https://news.ycombinator.com/item?id=8936701) | LibreBoard 提供开源的 Trello 风格看板，供用户自行使用。 | 243 | 98 | 2015-01-23 |
| 8 | [Show HN: Get your local and public IP addresses in JavaScript](https://news.ycombinator.com/item?id=8949953) | 通过 JavaScript 获取本地与公网 IP 地址的实现展示。 | 239 | 89 | 2015-01-26 |
| 9 | [Show HN: Pgcli – A CLI for Postgres with auto-completion and syntax highlighting](https://news.ycombinator.com/item?id=8844723) | Pgcli 为 PostgreSQL 命令行加入自动补全与语法高亮。 | 227 | 52 | 2015-01-06 |
| 10 | [Show HN: A curated list of remote jobs](https://news.ycombinator.com/item?id=8825308) | 一份经过筛选的远程职位清单，帮助寻找不受地点限制的工作。 | 218 | 55 | 2015-01-02 |

### 2015-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: A Unixy approach to WebSockets](https://news.ycombinator.com/item?id=9050970) | 用 Unix 工具的思路处理 WebSocket，探索更易组合的使用方式。 | 421 | 140 | 2015-02-14 |
| 2 | [Show HN: A Simple terminal-based video chat – renders in ASCII and has audio](https://news.ycombinator.com/item?id=9018930) | 终端视频聊天也能有声音：画面以 ASCII 字符呈现。 | 375 | 44 | 2015-02-08 |
| 3 | [Show HN: Let's Chat, a self-hosted chat app for small teams](https://news.ycombinator.com/item?id=9040841) | Let's Chat 面向小团队提供可自行托管的聊天应用。 | 350 | 90 | 2015-02-12 |
| 4 | [Show HN: A histogram of salaries given to H1B workers in the software industry](https://news.ycombinator.com/item?id=9096002) | 用直方图呈现软件行业 H-1B 雇员的薪资分布。 | 322 | 240 | 2015-02-23 |
| 5 | [Show HN: Matterhorn – Your new project manager](https://news.ycombinator.com/item?id=8990584) | Matterhorn 展示项目管理工具，供团队试用和反馈。 | 298 | 209 | 2015-02-03 |
| 6 | [Show HN: I rendered the Go gopher using Go](https://news.ycombinator.com/item?id=9009554) | 作者用 Go 渲染 Go 吉祥物，展示一次语言与图形结合的练习。 | 287 | 48 | 2015-02-06 |
| 7 | [Show HN: A Global Co-Living Subscription for Nomads](https://news.ycombinator.com/item?id=9022311) | 面向数字游民的全球共居订阅，尝试把住宿做成持续服务。 | 265 | 165 | 2015-02-09 |
| 8 | [Show HN: Watch People Code](https://news.ycombinator.com/item?id=9017990) | Watch People Code 让人观看别人写代码，了解实际开发过程。 | 243 | 72 | 2015-02-08 |
| 9 | [Show HN: vim-hackernews](https://news.ycombinator.com/item?id=9015621) | 在 Vim 里浏览 Hacker News，把社区阅读带进编辑器。 | 193 | 34 | 2015-02-07 |
| 10 | [Show HN: Littlebox, a pure CSS icon library – worth continuing?](https://news.ycombinator.com/item?id=9047086) | Littlebox 用纯 CSS 绘制图标，作者征求是否值得继续开发的意见。 | 192 | 68 | 2015-02-13 |

### 2015-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Textures.js, SVG Patterns for Data Visualization](https://news.ycombinator.com/item?id=9224776) | Textures.js 为数据可视化提供 SVG 纹理图案。 | 404 | 61 | 2015-03-18 |
| 2 | [Show HN: Slack Meets GitHub Issues](https://news.ycombinator.com/item?id=9144271) | 把 Slack 式协作与 GitHub Issues 结合，作者展示辞职创业后的产品。 | 373 | 156 | 2015-03-04 |
| 3 | [Show HN: Ghostnote – Contextual notes and todo app](https://news.ycombinator.com/item?id=9145007) | Ghostnote 把便笺和待办事项放进具体使用场景中。 | 301 | 187 | 2015-03-04 |
| 4 | [Show HN: Interactive Essay on Signals, Sampling and the Fourier Transform](https://news.ycombinator.com/item?id=9131706) | 通过交互式文章理解信号、采样和傅里叶变换。 | 293 | 43 | 2015-03-02 |
| 5 | [Show HN: Find tech jobs that come with a visa](https://news.ycombinator.com/item?id=9170511) | 专门寻找提供签证支持的技术岗位，降低跨国求职的信息门槛。 | 290 | 97 | 2015-03-09 |
| 6 | [Show HN: Rabbits – Send an email to get any grunt-work programming job completed](https://news.ycombinator.com/item?id=9249112) | 给 Rabbits 发封邮件，即可委托完成繁琐的编程任务。 | 256 | 98 | 2015-03-23 |
| 7 | [Show HN: GraphQL for Postgres](https://news.ycombinator.com/item?id=9200726) | 为 PostgreSQL 提供 GraphQL 访问方式，连接数据库与查询接口。 | 195 | 23 | 2015-03-13 |
| 8 | [Show HN: JavaScript Acid Techno Machine](https://news.ycombinator.com/item?id=9178933) | 用 JavaScript 制作 Acid Techno 音乐机器，在网页中玩电子音乐。 | 161 | 57 | 2015-03-10 |
| 9 | [Show HN: SSL Decoder – An open-source alternative for the SSL Labs server test](https://news.ycombinator.com/item?id=9271946) | SSL Decoder 提供开源服务器检测工具，作为 SSL Labs 测试的替代选择。 | 160 | 42 | 2015-03-26 |
| 10 | [Show HN: My kid choked on a toy, so I built this](https://news.ycombinator.com/item?id=9186013) | 孩子被玩具噎住后，作者动手制作了一个回应这次经历的项目。 | 133 | 101 | 2015-03-11 |

### 2015-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: A tool that transforms your whole list with just one example](https://news.ycombinator.com/item?id=9432949) | 展示一款只需提供一个示例，就能转换整份列表的工具。 | 764 | 144 | 2015-04-24 |
| 2 | [Show HN: A random startup generator](https://news.ycombinator.com/item?id=9427856) | 随机生成创业点子，看看组合出来的公司概念有多离奇。 | 607 | 189 | 2015-04-23 |
| 3 | [Show HN: Where is “Who is hiring?” hiring?](https://news.ycombinator.com/item?id=9348193) | 把 HN 招聘帖里的机会放到地理视角下，看看职位集中在哪里。 | 493 | 117 | 2015-04-09 |
| 4 | [Show HN: I'm a 14 year-old dev who has programmed an artificial intelligence bot](https://news.ycombinator.com/item?id=9386004) | 一位 14 岁开发者展示自己编写的人工智能机器人。 | 430 | 297 | 2015-04-16 |
| 5 | [Show HN: Kaiwa, a Modern Open-Source XMPP Web Client](https://news.ycombinator.com/item?id=9340246) | Kaiwa 是开源 XMPP 网页客户端，尝试提供现代聊天体验。 | 339 | 140 | 2015-04-08 |
| 6 | [Show HN: Ramjet.js – Morph DOM elements into each other](https://news.ycombinator.com/item?id=9458268) | Ramjet.js 让两个 DOM 元素之间产生形态变换动画。 | 309 | 35 | 2015-04-29 |
| 7 | [Show HN: Kubist, a little web app to make cubism-like images](https://news.ycombinator.com/item?id=9410452) | Kubist 帮用户制作带有立体主义风格的图像。 | 231 | 48 | 2015-04-20 |
| 8 | [Show HN: Caddy, a cross-platform HTTP/2 web server](https://news.ycombinator.com/item?id=9452606) | Caddy 展示支持 HTTP/2 的跨平台 Web 服务器。 | 208 | 87 | 2015-04-28 |
| 9 | [Show HN: Get pinged when standards hit 90% browser support](https://news.ycombinator.com/item?id=9332718) | 当 Web 标准达到九成浏览器支持率时，自动收到提醒。 | 199 | 48 | 2015-04-07 |
| 10 | [Show HN: Free, instant, secure, disposable chat rooms built in Go](https://news.ycombinator.com/item?id=9372918) | 用 Go 搭建免费、即时且可一次性使用的聊天室，作者同时强调安全性。 | 169 | 93 | 2015-04-14 |

### 2015-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: This page exists only if someone is looking at it](https://news.ycombinator.com/item?id=9531265) | 展示一个只有在有人查看时才会存在的网页。 | 803 | 165 | 2015-05-12 |
| 2 | [Show HN: Twenty](https://news.ycombinator.com/item?id=9543005) | 作者展示名为 Twenty 的项目。 | 666 | 167 | 2015-05-14 |
| 3 | [Show HN: Visa Explorer – Salaries, lawyers, companies of all H-1B in the USA](https://news.ycombinator.com/item?id=9588128) | Visa Explorer 汇集美国 H-1B 的薪资、律师和公司信息供查询。 | 582 | 247 | 2015-05-22 |
| 4 | [Show HN: An Isomorphic JavaScript Framework Faster Than React](https://news.ycombinator.com/item?id=9604203) | 作者展示同构 JavaScript 框架，并声称其速度超过 React。 | 337 | 253 | 2015-05-26 |
| 5 | [Show HN: JavaScript Graphing Library Comparison](https://news.ycombinator.com/item?id=9583384) | 并排比较 JavaScript 绘图库，辅助选择合适的图表工具。 | 328 | 114 | 2015-05-21 |
| 6 | [Show HN: Deck of Cards – A playing card API](https://news.ycombinator.com/item?id=9522489) | Deck of Cards 提供扑克牌 API，方便把纸牌机制接入应用。 | 255 | 137 | 2015-05-11 |
| 7 | [Show HN: Percy.io, a continuous visual integration tool](https://news.ycombinator.com/item?id=9624673) | Percy.io 把视觉检查接入持续集成，关注界面外观的变化。 | 249 | 52 | 2015-05-29 |
| 8 | [Show HN: An old rotary phone converted into a mobile phone](https://news.ycombinator.com/item?id=9610509) | 把老式旋转拨号电话改造成手机，保留旧外壳里的新用途。 | 222 | 61 | 2015-05-27 |
| 9 | [Show HN: Hydrogen Brings Light Table to Atom](https://news.ycombinator.com/item?id=9577336) | Hydrogen 尝试把 Light Table 式交互开发体验带到 Atom。 | 190 | 70 | 2015-05-20 |
| 10 | [Show HN: InboxSDK by Streak (YC S11) – Build Apps inside Gmail](https://news.ycombinator.com/item?id=9583976) | Streak 的 InboxSDK 让开发者直接在 Gmail 内构建应用。 | 176 | 62 | 2015-05-21 |

### 2015-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Free Company Logo API](https://news.ycombinator.com/item?id=9806319) | 通过免费 API 获取公司标志，简化产品里的品牌图像接入。 | 525 | 152 | 2015-06-30 |
| 2 | [Show HN: Wayback HN, a cross between the Wayback Machine and Hacker News](https://news.ycombinator.com/item?id=9746188) | Wayback HN 结合网页时光机与 Hacker News，探索过去的社区内容。 | 503 | 76 | 2015-06-19 |
| 3 | [Show HN: Universal Pause Button](https://news.ycombinator.com/item?id=9686854) | 一个通用暂停按钮项目，尝试给运行中的程序增加暂停能力。 | 501 | 169 | 2015-06-09 |
| 4 | [Show HN: Mockups fixed by making collaboration effortless, built with React](https://news.ycombinator.com/item?id=9659167) | 作者用 React 构建原型工具，希望通过简化协作改善设计沟通。 | 334 | 105 | 2015-06-04 |
| 5 | [Show HN: Learn Swift](https://news.ycombinator.com/item?id=9685255) | 一个供学习 Swift 使用的项目，帮助接触这门语言。 | 238 | 55 | 2015-06-09 |
| 6 | [Show HN: Retroospect – How was your work week?](https://news.ycombinator.com/item?id=9705446) | Retroospect 围绕“这周工作如何”组织团队回顾。 | 221 | 112 | 2015-06-12 |
| 7 | [Show HN: MapChat – A simple location based chat in 300 lines of code](https://news.ycombinator.com/item?id=9744471) | MapChat 用约 300 行代码实现基于位置的简单聊天。 | 205 | 114 | 2015-06-19 |
| 8 | [Show HN: Diff.io](https://news.ycombinator.com/item?id=9643579) | 作者展示 Diff.io 项目，邀请社区了解并反馈。 | 194 | 99 | 2015-06-02 |
| 9 | [Show HN: Hypatia 0.2, a 2D adventure game engine](https://news.ycombinator.com/item?id=9763870) | Hypatia 0.2 是开源二维冒险游戏引擎，面向单人动作冒险作品。 | 191 | 38 | 2015-06-23 |
| 10 | [Show HN: Clojure by Example](https://news.ycombinator.com/item?id=9692281) | 通过具体示例学习 Clojure，把语言概念放回实际代码中。 | 184 | 35 | 2015-06-10 |

### 2015-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Spot the Drowning Child](https://news.ycombinator.com/item?id=9962185) | 通过寻找正在溺水的孩子，挑战自己辨认泳池险情的能力。 | 1215 | 378 | 2015-07-28 |
| 2 | [Show HN: Bocker – Docker implemented in 100 lines of bash](https://news.ycombinator.com/item?id=9925896) | Bocker 用约一百行 Bash 实现类似 Docker 的功能。 | 662 | 87 | 2015-07-21 |
| 3 | [Show HN: “Who is hiring?” Map](https://news.ycombinator.com/item?id=9838955) | 把 HN 的招聘信息标到地图上，按地点浏览工作机会。 | 546 | 136 | 2015-07-06 |
| 4 | [Show HN: Showgoers – Watch Netflix with friends remotely](https://news.ycombinator.com/item?id=9944746) | Showgoers 让相隔两地的朋友一起观看 Netflix。 | 281 | 84 | 2015-07-24 |
| 5 | [Show HN: A Hand-Drawn QR Code Alternative](https://news.ycombinator.com/item?id=9956415) | 一种可以手绘的二维码替代方案，探索机器可读图形的新形式。 | 270 | 134 | 2015-07-27 |
| 6 | [Show HN: Density – Anonymous People Counter and API](https://news.ycombinator.com/item?id=9878597) | Density 提供匿名人数统计及 API，用数据描述空间里的人流。 | 258 | 145 | 2015-07-13 |
| 7 | [Show HN: Flexbox.io – a free video series on learning CSS Flexbox](https://news.ycombinator.com/item?id=9963714) | Flexbox.io 用免费视频课程讲解 CSS Flexbox 布局。 | 236 | 57 | 2015-07-28 |
| 8 | [Show HN: Arrow Hero](https://news.ycombinator.com/item?id=9810534) | Arrow Hero 项目首次亮相，作者邀请社区体验并交流反馈。 | 195 | 55 | 2015-07-01 |
| 9 | [Show HN: YouTube Filesystem – YTFS](https://news.ycombinator.com/item?id=9839712) | YTFS 把 YouTube 变成文件系统，展示一种出人意料的存储实验。 | 185 | 61 | 2015-07-06 |
| 10 | [Show HN: FAQT – A lightweight, personal knowledge base](https://news.ycombinator.com/item?id=9911942) | FAQT 提供轻量个人知识库，帮助整理自己积累的信息。 | 184 | 110 | 2015-07-19 |

### 2015-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: My SSH server knows who you are](https://news.ycombinator.com/item?id=10004678) | 作者展示一个声称能识别访问者身份的 SSH 服务器。 | 836 | 245 | 2015-08-04 |
| 2 | [Show HN: Big List of Naughty Strings for testing user-input data](https://news.ycombinator.com/item?id=10035008) | 一份容易让程序出错的字符串清单，用来检验用户输入处理。 | 514 | 79 | 2015-08-10 |
| 3 | [Show HN: Image Processing for Everybody](https://news.ycombinator.com/item?id=10008637) | 面向大众的图像处理项目，尝试降低接触图像处理的门槛。 | 451 | 167 | 2015-08-05 |
| 4 | [Show HN: JAWS – A JavaScript and AWS Stack](https://news.ycombinator.com/item?id=10005415) | JAWS 把 JavaScript 与 AWS 组合成一套开发技术栈。 | 375 | 124 | 2015-08-04 |
| 5 | [Show HN: Tonic – A data visualizing REPL for Node.js](https://news.ycombinator.com/item?id=10080731) | Tonic 为 Node.js 提供能可视化数据的交互式运行环境。 | 342 | 79 | 2015-08-18 |
| 6 | [Show HN: Print iconic patents for your walls](https://news.ycombinator.com/item?id=9990160) | 把经典专利印成墙面装饰，让技术图纸进入日常空间。 | 241 | 51 | 2015-08-02 |
| 7 | [Show HN: Ear training using midi.js](https://news.ycombinator.com/item?id=10117072) | 用 midi.js 制作听力训练工具，练习对音乐声音的辨识。 | 230 | 34 | 2015-08-25 |
| 8 | [Show HN: Find your competitors that Google can't](https://news.ycombinator.com/item?id=10073389) | 作者展示竞争对手发现工具，希望找到 Google 搜索遗漏的公司。 | 189 | 61 | 2015-08-17 |
| 9 | [Show HN: Guess which government programs work](https://news.ycombinator.com/item?id=10057285) | 猜猜哪些政府项目有效，检验自己对公共政策效果的直觉。 | 184 | 53 | 2015-08-13 |
| 10 | [Show HN: Is it vulnerable? Drag-n-drop your Gemfile.lock to check](https://news.ycombinator.com/item?id=10022717) | 拖入 Gemfile.lock 就能检查依赖漏洞，简化 Ruby 项目安全排查。 | 175 | 49 | 2015-08-07 |

### 2015-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Make a programmable mirror](https://news.ycombinator.com/item?id=10204018) | 展示如何制作一面可以编程的镜子。 | 1172 | 136 | 2015-09-11 |
| 2 | [Show HN: I spent a year making an electro-mechanical prototype of a liquid clock](https://news.ycombinator.com/item?id=10284321) | 作者展示花费一年制作的机电式液体时钟原型。 | 681 | 103 | 2015-09-26 |
| 3 | [Show HN: %%30%30: A Game](https://news.ycombinator.com/item?id=10249362) | 名为 %%30%30 的游戏亮相，邀请玩家体验这个特别的作品。 | 608 | 89 | 2015-09-20 |
| 4 | [Show HN: Hacker News Simulator](https://news.ycombinator.com/item?id=10248773) | 用模拟器重现 Hacker News，看看作者如何演绎社区体验。 | 572 | 163 | 2015-09-20 |
| 5 | [Show HN: Turn a Google Spreadsheet into an API](https://news.ycombinator.com/item?id=10251686) | 把 Google 电子表格转成 API，让表格数据供程序调用。 | 357 | 98 | 2015-09-21 |
| 6 | [Show HN: HTML5 version of StarCraft](https://news.ycombinator.com/item?id=10180209) | 用 HTML5 实现《星际争霸》，把经典游戏带进浏览器。 | 320 | 96 | 2015-09-07 |
| 7 | [Show HN: Light Bootstrap Dashboard](https://news.ycombinator.com/item?id=10184982) | Light Bootstrap Dashboard 提供基于 Bootstrap 的轻量仪表盘界面。 | 170 | 42 | 2015-09-08 |
| 8 | [Show HN: Hacker News desktop app made with Electron and Node](https://news.ycombinator.com/item?id=10226768) | 用 Electron 和 Node 制作 Hacker News 桌面客户端。 | 167 | 73 | 2015-09-16 |
| 9 | [Show HN: Kiddo Paint](https://news.ycombinator.com/item?id=10260302) | Kiddo Paint 绘画项目亮相，展示作者对画图工具的尝试。 | 162 | 49 | 2015-09-22 |
| 10 | [Show HN: Stock recommender system using hedge fund data and machine learning](https://news.ycombinator.com/item?id=10208356) | 结合对冲基金数据与机器学习，作者制作了股票推荐系统。 | 134 | 103 | 2015-09-12 |

### 2015-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Twitch Installs Arch Linux – A cooperative text-based horror game](https://news.ycombinator.com/item?id=10477721) | 让 Twitch 观众合作安装 Arch Linux，作者把过程形容为文字恐怖游戏。 | 802 | 250 | 2015-10-30 |
| 2 | [Show HN: Exposé – a static site generator for photos and videos](https://news.ycombinator.com/item?id=10376468) | Exposé 为照片和视频生成静态站点，方便建立个人影像展示页。 | 548 | 73 | 2015-10-12 |
| 3 | [Show HN: Cancel your Comcast in 5 minutes](https://news.ycombinator.com/item?id=10320509) | 作者展示一项声称能在五分钟内取消 Comcast 服务的工具。 | 386 | 257 | 2015-10-02 |
| 4 | [Show HN: Download any song without knowing its name](https://news.ycombinator.com/item?id=10355030) | 不用知道歌名也能下载歌曲，作者展示围绕这个需求制作的工具。 | 321 | 134 | 2015-10-08 |
| 5 | [Show HN: Metabase, an open-source business intelligence tool](https://news.ycombinator.com/item?id=10425959) | Metabase 提供开源商业智能工具，让团队探索业务数据。 | 287 | 121 | 2015-10-21 |
| 6 | [Show HN: Dtab – Spreadsheet for Data Science](https://news.ycombinator.com/item?id=10319289) | Dtab 把电子表格界面用于数据科学工作。 | 229 | 67 | 2015-10-02 |
| 7 | [Show HN: Clojure for the Brave and True – now free online](https://news.ycombinator.com/item?id=10426106) | 《Clojure for the Brave and True》开放在线免费阅读。 | 224 | 30 | 2015-10-21 |
| 8 | [Show HN: Arguman – Argument Analysis Platform](https://news.ycombinator.com/item?id=10405288) | Arguman 提供论证分析平台，帮助梳理观点和推理关系。 | 170 | 61 | 2015-10-17 |
| 9 | [Show HN: Freeze – Amazon Glacier GUI Client for Mac OS X](https://news.ycombinator.com/item?id=10445380) | Freeze 为 Mac 用户提供 Amazon Glacier 的图形客户端。 | 160 | 50 | 2015-10-25 |
| 10 | [Show HN: Someone.io – Task management for teams made easy](https://news.ycombinator.com/item?id=10330335) | Someone.io 尝试让团队任务管理变得更容易。 | 151 | 81 | 2015-10-05 |

### 2015-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Something pointless I made](https://news.ycombinator.com/item?id=10646440) | 作者展示一个自己形容为“没有意义”的趣味作品。 | 747 | 102 | 2015-11-29 |
| 2 | [Show HN: Parinfer – a simpler way to write Lisp](https://news.ycombinator.com/item?id=10547772) | Parinfer 尝试让 Lisp 的编写方式更简单。 | 674 | 134 | 2015-11-11 |
| 3 | [Show HN: React for Beginners](https://news.ycombinator.com/item?id=10499683) | 面向初学者的 React 教学项目，带人入门组件开发。 | 178 | 43 | 2015-11-03 |
| 4 | [Show HN: HackerCouch](https://news.ycombinator.com/item?id=10646551) | 作者展示 HackerCouch，邀请 HN 社区了解这个项目。 | 162 | 43 | 2015-11-29 |
| 5 | [Show HN: Nixar – New design of Linux command line](https://news.ycombinator.com/item?id=10570666) | Nixar 尝试重新设计 Linux 命令行的使用体验。 | 130 | 62 | 2015-11-15 |
| 6 | [Show HN: WOPR – A markup for rich terminal reports](https://news.ycombinator.com/item?id=10493891) | WOPR 用标记语法生成内容丰富的终端报告。 | 125 | 37 | 2015-11-02 |
| 7 | [Show HN: Administrate – Rails framework for creating flexible admin dashboards](https://news.ycombinator.com/item?id=10509077) | Administrate 为 Rails 提供灵活的管理后台构建框架。 | 124 | 26 | 2015-11-04 |
| 8 | [Show HN: Easy Forth](https://news.ycombinator.com/item?id=10634918) | Easy Forth 以易于入门为目标，展示 Forth 学习项目。 | 122 | 24 | 2015-11-26 |
| 9 | [Show HN: Real-Time Collaborative Watercolor Painting Using Twitch](https://news.ycombinator.com/item?id=10581735) | 通过 Twitch 实时共同画水彩，把直播观众变成共同创作者。 | 109 | 21 | 2015-11-17 |
| 10 | [Show HN: Interviews can be stressful – give take-home projects instead](https://news.ycombinator.com/item?id=10588371) | 面试令人紧张，作者展示以带回家完成的项目代替现场考核的方案。 | 96 | 127 | 2015-11-18 |

### 2015-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Open Hunt – an open and community-run alternative to Product Hunt](https://news.ycombinator.com/item?id=10759879) | Open Hunt 提供由社区运营、开放的 Product Hunt 替代平台。 | 1093 | 180 | 2015-12-18 |
| 2 | [Show HN: Jukedeck – create unique, royalty-free music for your videos using A.I.](https://news.ycombinator.com/item?id=10706203) | Jukedeck 用 AI 生成独特音乐，供视频制作使用且无需版税。 | 410 | 211 | 2015-12-09 |
| 3 | [Show HN: FuckFuckAdblock](https://news.ycombinator.com/item?id=10729068) | FuckFuckAdblock 展示围绕广告拦截与反拦截的工具实验。 | 353 | 298 | 2015-12-14 |
| 4 | [Show HN: Fieldbook: Lightweight Database with a Spreadsheet UI and a REST API](https://news.ycombinator.com/item?id=10752570) | Fieldbook 将轻量数据库、电子表格界面和 REST API 放到一起。 | 335 | 92 | 2015-12-17 |
| 5 | [Show HN: Ponzi.es – Startup sticker ponzi scheme](https://news.ycombinator.com/item?id=10716798) | Ponzi.es 把创业公司贴纸与“庞氏骗局”玩笑结合成项目。 | 332 | 125 | 2015-12-11 |
| 6 | [Show HN: Cloudcraft – Create AWS diagrams](https://news.ycombinator.com/item?id=10722942) | Cloudcraft 帮助绘制 AWS 架构图，直观呈现云资源关系。 | 281 | 72 | 2015-12-12 |
| 7 | [Show HN: Acme-tiny, a tiny 200-line Let's Encrypt client](https://news.ycombinator.com/item?id=10676685) | Acme-tiny 用约 200 行代码实现精简的 Let's Encrypt 客户端。 | 280 | 51 | 2015-12-04 |
| 8 | [Show HN: A fireplace for Emacs](https://news.ycombinator.com/item?id=10758290) | 在 Emacs 里点起壁炉，给编辑器增添一处趣味场景。 | 257 | 69 | 2015-12-18 |
| 9 | [Show HN: Lasergist.com – Your custom design in pure, laser-cut Stainless Steel](https://news.ycombinator.com/item?id=10690834) | Lasergist 将用户设计激光切割成不锈钢实体作品。 | 211 | 141 | 2015-12-07 |
| 10 | [Show HN: I redesigned the USPS package delivery slip](https://news.ycombinator.com/item?id=10771060) | 作者重新设计美国邮政的包裹投递通知单，展示改版思路。 | 156 | 67 | 2015-12-21 |

### 2016-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Super Mail Forward, an HTML email that evolves as you forward it](https://news.ycombinator.com/item?id=10944795) | Super Mail Forward 是一封会随着转发不断变化的 HTML 邮件。 | 454 | 65 | 2016-01-21 |
| 2 | [Show HN: I've made a tool to generate beautiful gradient background images](https://news.ycombinator.com/item?id=10872143) | 作者制作渐变背景图片生成器，帮助快速获得漂亮配色。 | 448 | 94 | 2016-01-09 |
| 3 | [Show HN: 3D shooter in your terminal using raycasting in Awk](https://news.ycombinator.com/item?id=10896901) | 用 Awk 与光线投射在终端里实现三维射击游戏。 | 350 | 55 | 2016-01-13 |
| 4 | [Show HN: GPU text rendering with vector textures](https://news.ycombinator.com/item?id=10824064) | 借助向量纹理在 GPU 上渲染文字，展示字体绘制技术。 | 334 | 87 | 2016-01-01 |
| 5 | [Show HN: I made a site to catalogue 10,000 CC0-licensed stock photos](https://news.ycombinator.com/item?id=10950794) | 作者建立图库，整理一万张采用 CC0 授权的素材照片。 | 310 | 64 | 2016-01-22 |
| 6 | [Show HN: Nodal. Next-Generation Node.js Server and Framework](https://news.ycombinator.com/item?id=10849460) | Nodal 展示面向 Node.js 的服务器与应用开发框架。 | 288 | 168 | 2016-01-06 |
| 7 | [Show HN: I'm a professor who has developed an interactive Powerpoint alternative](https://news.ycombinator.com/item?id=10890531) | 一位教授开发交互式演示工具，尝试替代 PowerPoint。 | 244 | 64 | 2016-01-12 |
| 8 | [Show HN: Ship – A fast, native issue tracker for software projects](https://news.ycombinator.com/item?id=10996765) | Ship 提供面向软件项目的原生问题追踪应用。 | 219 | 106 | 2016-01-29 |
| 9 | [Show HN: “Nim in Action” is now available](https://news.ycombinator.com/item?id=10987975) | 《Nim in Action》发布，作者向社区介绍这本 Nim 编程书。 | 181 | 134 | 2016-01-28 |
| 10 | [Show HN: Wired Logic – a pixel-based logic simulator](https://news.ycombinator.com/item?id=11008509) | Wired Logic 用像素构建逻辑模拟，让电路关系可视化。 | 176 | 15 | 2016-01-31 |

### 2016-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I've been writing daily TILs for a year](https://news.ycombinator.com/item?id=11068902) | 作者展示自己一年来每天记录“今日所学”的积累。 | 819 | 150 | 2016-02-09 |
| 2 | [Show HN: Htop 2.0 released, now cross-platform](https://news.ycombinator.com/item?id=11077823) | Htop 2.0 发布并支持多个平台，让进程监控走出单一系统。 | 613 | 153 | 2016-02-11 |
| 3 | [Show HN: 3D Vector Graphics](https://news.ycombinator.com/item?id=11019922) | 三维矢量图形项目展示，探索图形表达的另一种形式。 | 441 | 56 | 2016-02-02 |
| 4 | [Show HN: Windows 98 in browser](https://news.ycombinator.com/item?id=11155203) | 在浏览器里体验 Windows 98，重访熟悉的旧桌面。 | 356 | 165 | 2016-02-22 |
| 5 | [Show HN: Find the best recipe for any two foods, based on over 600k recipes](https://news.ycombinator.com/item?id=11109600) | 从六十多万份食谱中，为任意两种食物寻找合适的做法。 | 337 | 105 | 2016-02-16 |
| 6 | [Show HN: Plain Email – An app for one-touch email processing](https://news.ycombinator.com/item?id=11027371) | Plain Email 希望通过一次触碰完成邮件处理。 | 322 | 134 | 2016-02-03 |
| 7 | [Show HN: Deepstream.io – open-source real-time server with pub/sub and data sync](https://news.ycombinator.com/item?id=11071916) | Deepstream.io 提供开源实时服务器，支持发布订阅和数据同步。 | 301 | 83 | 2016-02-10 |
| 8 | [Show HN: how2 – stackoverflow.com from the terminal](https://news.ycombinator.com/item?id=11150209) | how2 把 Stack Overflow 问答带进终端，方便边写代码边查询。 | 272 | 43 | 2016-02-22 |
| 9 | [Show HN: The Deadlock Empire – Slay dragons, master concurrency](https://news.ycombinator.com/item?id=11064507) | 《The Deadlock Empire》用游戏方式讲并发，让玩家挑战死锁难题。 | 269 | 30 | 2016-02-09 |
| 10 | [Show HN: Simple and elegant Markdown-based resumes](https://news.ycombinator.com/item?id=11026096) | 用 Markdown 编写简洁履历，把简历内容与排版流程结合。 | 255 | 121 | 2016-02-03 |

### 2016-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Podcat – Imdb for podcasts](https://news.ycombinator.com/item?id=11290720) | Podcat 想成为播客界的 IMDb，帮助查找和认识播客节目。 | 401 | 106 | 2016-03-15 |
| 2 | [Show HN: Honest Salary – Help make salaries fair and honest by sharing yours](https://news.ycombinator.com/item?id=11317811) | Honest Salary 邀请用户分享薪资，希望让薪酬信息更加透明公平。 | 314 | 191 | 2016-03-19 |
| 3 | [Show HN: Using Google AMP to build a Medium-style Jekyll site that loads in 65ms](https://news.ycombinator.com/item?id=11287540) | 作者用 Google AMP 构建 Medium 风格的 Jekyll 网站，并报告 65 毫秒加载时间。 | 279 | 95 | 2016-03-15 |
| 4 | [Show HN: Host your status page on GitHub](https://news.ycombinator.com/item?id=11238099) | 把服务状态页托管到 GitHub，探索简便的状态发布方式。 | 248 | 43 | 2016-03-07 |
| 5 | [Show HN: MapHub – A Google My Maps Alternative, Based on OpenStreetMap Data](https://news.ycombinator.com/item?id=11389989) | MapHub 基于 OpenStreetMap 数据，提供 Google My Maps 的替代选择。 | 244 | 81 | 2016-03-30 |
| 6 | [Show HN: Flexbox Defense – learn CSS flexbox by playing a tower defense game](https://news.ycombinator.com/item?id=11213475) | 一边玩塔防一边学 CSS Flexbox，把布局规则变成游戏机制。 | 243 | 42 | 2016-03-02 |
| 7 | [Show HN: Flat – Music notation software: Web-based and Real-time collaboration](https://news.ycombinator.com/item?id=11218844) | Flat 提供网页乐谱编辑，支持多人实时协作写谱。 | 207 | 69 | 2016-03-03 |
| 8 | [Show HN: Zube 1.0 – Powerful project management for GitHub Issues](https://news.ycombinator.com/item?id=11283978) | Zube 1.0 围绕 GitHub Issues 提供项目管理功能。 | 206 | 65 | 2016-03-14 |
| 9 | [Show HN: GitHub News, using a peak detection algorithm to detect trending repos](https://news.ycombinator.com/item?id=11261953) | GitHub News 用峰值检测算法发现正在走红的代码仓库。 | 184 | 31 | 2016-03-10 |
| 10 | [Show HN: Teleport – SSH for Clusters and Teams](https://news.ycombinator.com/item?id=11355976) | Teleport 为集群与团队提供 SSH 访问方案。 | 183 | 43 | 2016-03-24 |

### 2016-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I made an interactive Bootstrap 4 cheat sheet](https://news.ycombinator.com/item?id=11542005) | 展示一份可以交互查看的 Bootstrap 4 速查表。 | 847 | 161 | 2016-04-21 |
| 2 | [Show HN: What every browser knows about you](https://news.ycombinator.com/item?id=11407536) | 这个项目展示浏览器能获知哪些个人信息，帮助理解网页端隐私。 | 553 | 206 | 2016-04-01 |
| 3 | [Show HN: Barnacl.es, a community news site for never-funded bootstrappers](https://news.ycombinator.com/item?id=11520378) | Barnacl.es 为从未融资的自力创业者建立新闻交流社区。 | 382 | 68 | 2016-04-18 |
| 4 | [Show HN: I made a Hacker News for podcasts](https://news.ycombinator.com/item?id=11509835) | 作者制作播客版 Hacker News，希望用社区方式发现节目。 | 367 | 132 | 2016-04-16 |
| 5 | [Show HN: The first issue of Compelling Science Fiction](https://news.ycombinator.com/item?id=11469135) | 《Compelling Science Fiction》创刊号发布，展示新的科幻刊物。 | 311 | 70 | 2016-04-11 |
| 6 | [Show HN: Jam API, turn any site into a JSON api using CSS selectors](https://news.ycombinator.com/item?id=11587468) | Jam API 利用 CSS 选择器，把网站内容转换为 JSON 接口。 | 300 | 82 | 2016-04-28 |
| 7 | [Show HN: QBE – a new compiler back end](https://news.ycombinator.com/item?id=11555527) | QBE 展示新的编译器后端，供编程语言和编译器开发者关注。 | 241 | 68 | 2016-04-23 |
| 8 | [Show HN: Open source colorizing grayscale images with NN](https://news.ycombinator.com/item?id=11540265) | 开源神经网络上色工具，让灰度图像获得颜色。 | 219 | 77 | 2016-04-21 |
| 9 | [Show HN: GoldenLayout – JavaScript layout manager with multi-screen support](https://news.ycombinator.com/item?id=11478323) | GoldenLayout 为 JavaScript 应用管理布局，并支持多个屏幕。 | 193 | 37 | 2016-04-12 |
| 10 | [Show HN: FIND – an indoor positioning system for smartphones and laptops](https://news.ycombinator.com/item?id=11517667) | FIND 为手机和笔记本电脑提供室内定位系统。 | 183 | 72 | 2016-04-18 |

### 2016-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Automatic private time tracking for OS X](https://news.ycombinator.com/item?id=11778077) | 面向 OS X 的自动时间记录工具，把隐私作为产品关注点。 | 429 | 233 | 2016-05-26 |
| 2 | [Show HN: BitKeeper – Enterprise-ready version control, now open-source](https://news.ycombinator.com/item?id=11667494) | BitKeeper 开源，企业版本控制工具向更多开发者开放。 | 384 | 306 | 2016-05-10 |
| 3 | [Show HN: Kajero – Interactive JavaScript notebooks](https://news.ycombinator.com/item?id=11707120) | Kajero 提供可交互的 JavaScript 笔记本，结合代码与内容展示。 | 217 | 28 | 2016-05-16 |
| 4 | [Show HN: I built an AI that recognizes food](https://news.ycombinator.com/item?id=11712751) | 作者展示自己开发的食物识别 AI，尝试让程序认出盘中餐。 | 202 | 127 | 2016-05-17 |
| 5 | [Show HN: Serverless meets Microservices](https://news.ycombinator.com/item?id=11683121) | 把无服务器架构与微服务结合，展示一种服务组织思路。 | 191 | 61 | 2016-05-12 |
| 6 | [Show HN: Speech Coaching App – Stop Saying 'Umm', 'Like', 'Uhh'](https://news.ycombinator.com/item?id=11680823) | 演讲训练应用关注口头禅，帮助减少“嗯”“那个”等停顿词。 | 176 | 86 | 2016-05-12 |
| 7 | [Show HN: Minoca OS – A new lightweight kernel, completely from scratch](https://news.ycombinator.com/item?id=11662057) | Minoca OS 展示从零编写的轻量内核。 | 168 | 42 | 2016-05-09 |
| 8 | [Show HN: Dead Yet? – Keep an eye on dying startups](https://news.ycombinator.com/item?id=11777128) | Dead Yet? 跟踪濒临失败的创业公司，观察项目的存续状态。 | 164 | 89 | 2016-05-26 |
| 9 | [Show HN: Run your own OAuth2/OpenID Connect provider](https://news.ycombinator.com/item?id=11798045) | 自行运行 OAuth2 和 OpenID Connect 提供方，掌握身份认证服务。 | 161 | 49 | 2016-05-29 |
| 10 | [Show HN: Hydrogen, a multithread non-blocking Linux server framework in Rust](https://news.ycombinator.com/item?id=11664933) | Hydrogen 用 Rust 构建多线程、非阻塞的 Linux 服务器框架。 | 154 | 46 | 2016-05-10 |

### 2016-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: New calendar app idea](https://news.ycombinator.com/item?id=11846108) | 作者展示一个新的日历应用构想。 | 825 | 197 | 2016-06-06 |
| 2 | [Show HN: I made a database of remote companies](https://news.ycombinator.com/item?id=11890991) | 作者整理了一份实行远程工作的公司数据库。 | 747 | 114 | 2016-06-13 |
| 3 | [Show HN: Full Stack Lisp – A book in progress about writing Common Lisp apps](https://news.ycombinator.com/item?id=11823902) | 《Full Stack Lisp》边写边发布，讲解如何开发 Common Lisp 应用。 | 338 | 100 | 2016-06-02 |
| 4 | [Show HN: 2D field of view demo](https://news.ycombinator.com/item?id=11852783) | 一个二维视野演示，展示场景中可见范围的计算效果。 | 333 | 76 | 2016-06-07 |
| 5 | [Show HN: Search YouTube without stopping the video, and make your own playlists](https://news.ycombinator.com/item?id=11829237) | 搜索 YouTube 时保留正在播放的视频，并可建立自己的播放列表。 | 295 | 144 | 2016-06-03 |
| 6 | [Show HN: Map of immigration to the U.S. since 1820](https://news.ycombinator.com/item?id=11849398) | 用地图呈现自 1820 年以来的美国移民情况。 | 294 | 110 | 2016-06-06 |
| 7 | [Show HN: Anime.js – Polyvalent JavaScript Animation Engine](https://news.ycombinator.com/item?id=11986480) | Anime.js 提供多用途 JavaScript 动画引擎，便于构建网页动效。 | 283 | 73 | 2016-06-27 |
| 8 | [Show HN: Mega Boilerplate](https://news.ycombinator.com/item?id=11861926) | Mega Boilerplate 展示项目脚手架，帮助启动新的开发工作。 | 268 | 55 | 2016-06-08 |
| 9 | [Show HN: A secure, open source U2F token you can make with $4.5 worth of parts](https://news.ycombinator.com/item?id=11950664) | 用约 4.5 美元零件自制开源 U2F 令牌，作者展示硬件认证方案。 | 267 | 92 | 2016-06-22 |
| 10 | [Show HN: Homemade 32-bit CPU and OS (2015) [video]](https://news.ycombinator.com/item?id=11844005) | 视频展示作者自制的 32 位 CPU 和操作系统。 | 253 | 37 | 2016-06-06 |

### 2016-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Web Design in 4 minutes](https://news.ycombinator.com/item?id=12166687) | 通过四分钟的演示，理解网页设计的基本步骤。 | 1624 | 152 | 2016-07-26 |
| 2 | [Show HN: Swiss Army Knife for Mac OS X](https://news.ycombinator.com/item?id=12097856) | 面向 Mac 的多功能工具，作者将它比作系统里的瑞士军刀。 | 388 | 62 | 2016-07-14 |
| 3 | [Show HN: Riko – A Python stream processing engine modeled after Yahoo! Pipes](https://news.ycombinator.com/item?id=12136011) | Riko 用 Python 构建流处理引擎，设计参考 Yahoo Pipes。 | 283 | 67 | 2016-07-21 |
| 4 | [Show HN: OpenGL in super slow motion – visualising Z-buffering](https://news.ycombinator.com/item?id=12030172) | 以超慢动作展示 OpenGL 的深度缓冲，直观看清遮挡如何处理。 | 276 | 38 | 2016-07-04 |
| 5 | [Show HN: Randomly generated metal riffs using Web Audio API and React](https://news.ycombinator.com/item?id=12014663) | 用 Web Audio API 与 React 随机生成金属乐吉他片段。 | 275 | 42 | 2016-07-01 |
| 6 | [Show HN: AutoMicroFarm Is Ready for Shipping](https://news.ycombinator.com/item?id=12049410) | AutoMicroFarm 准备出货，作者向社区展示项目进展。 | 203 | 119 | 2016-07-07 |
| 7 | [Show HN: Free and open source page builder for WordPress](https://news.ycombinator.com/item?id=12054596) | 免费的开源 WordPress 页面构建器，简化页面制作。 | 202 | 62 | 2016-07-08 |
| 8 | [Show HN: Dependency CI – Continuous testing for your dependencies](https://news.ycombinator.com/item?id=12077645) | Dependency CI 持续测试项目依赖，关注依赖变化带来的影响。 | 198 | 62 | 2016-07-12 |
| 9 | [Show HN: Kubernetes Certificate Manager – Native Let's Encrypt Integration](https://news.ycombinator.com/item?id=12159249) | Kubernetes 证书管理器原生接入 Let's Encrypt，简化证书工作。 | 186 | 19 | 2016-07-25 |
| 10 | [Show HN: A simple infinite world in WebGL](https://news.ycombinator.com/item?id=12182581) | 用 WebGL 构建可无限延伸的简单世界。 | 181 | 56 | 2016-07-28 |

### 2016-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Generating fantasy maps – an interactive exploration](https://news.ycombinator.com/item?id=12260794) | 通过交互式探索，学习如何生成虚构世界的地图。 | 1004 | 64 | 2016-08-10 |
| 2 | [Show HN: Carbide – A New Programming Environment](https://news.ycombinator.com/item?id=12355102) | Carbide 展示新的编程环境，探索代码编写与运行的交互方式。 | 628 | 136 | 2016-08-24 |
| 3 | [Show HN: Noms – A new decentralized database based on ideas from Git](https://news.ycombinator.com/item?id=12211754) | Noms 借鉴 Git 的思路，设计去中心化数据库。 | 508 | 167 | 2016-08-02 |
| 4 | [Show HN: Top books mentioned in comments on Hacker News](https://news.ycombinator.com/item?id=12365693) | 整理 Hacker News 评论里提到的热门书籍，发现社区阅读偏好。 | 463 | 184 | 2016-08-26 |
| 5 | [Show HN: Give 7B people an instant physical address](https://news.ycombinator.com/item?id=12260958) | 为全球七十亿人即时生成实体地址，这是作者提出的项目目标。 | 415 | 199 | 2016-08-10 |
| 6 | [Show HN: Sharingbuttons.io – Fast and easy social media sharing buttons](https://news.ycombinator.com/item?id=12209595) | Sharingbuttons.io 提供方便接入的社交媒体分享按钮。 | 350 | 95 | 2016-08-02 |
| 7 | [Show HN: 1M rows/s from Postgres to Python](https://news.ycombinator.com/item?id=12227507) | 作者展示从 PostgreSQL 向 Python 每秒传输百万行数据的方案。 | 296 | 89 | 2016-08-04 |
| 8 | [Show HN: Learn Functional Programming Using Haskell](https://news.ycombinator.com/item?id=12209889) | 以 Haskell 为入口学习函数式编程。 | 220 | 90 | 2016-08-02 |
| 9 | [Show HN: A Multiplayer Geography Game Using WebSockets](https://news.ycombinator.com/item?id=12319661) | 使用 WebSocket 构建多人地理游戏，让玩家一起挑战地理知识。 | 220 | 69 | 2016-08-19 |
| 10 | [Show HN: Workq – Job Server in Go](https://news.ycombinator.com/item?id=12342781) | Workq 是用 Go 编写的任务服务器，用于组织后台作业。 | 185 | 59 | 2016-08-23 |

### 2016-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Wave function collapse algorithm](https://news.ycombinator.com/item?id=12612246) | 展示名为“波函数坍缩”的算法项目。 | 1226 | 122 | 2016-09-30 |
| 2 | [Show HN: Primitive Pictures](https://news.ycombinator.com/item?id=12539109) | 展示名为 Primitive Pictures 的图像项目。 | 894 | 170 | 2016-09-20 |
| 3 | [Show HN: A self-hosted alternative to Trello, Basecamp, and Freshbooks](https://news.ycombinator.com/item?id=12404871) | 提供可自托管的工具，尝试替代 Trello、Basecamp 与 FreshBooks。 | 396 | 154 | 2016-09-01 |
| 4 | [Show HN: InstaPart – Build circuit boards faster with instant parts](https://news.ycombinator.com/item?id=12571200) | InstaPart 希望通过即时获取元件，加快电路板制作过程。 | 309 | 107 | 2016-09-24 |
| 5 | [Show HN: A flask app to make dashboards, easily](https://news.ycombinator.com/item?id=12466625) | 用 Flask 应用更轻松地搭建仪表盘。 | 302 | 38 | 2016-09-09 |
| 6 | [Show HN: Build your first real world React.js application](https://news.ycombinator.com/item?id=12442026) | 跟着教程构建第一个实际 React.js 应用。 | 261 | 44 | 2016-09-07 |
| 7 | [Show HN: G9.js – Automatically Interactive Differentiable Graphics](https://news.ycombinator.com/item?id=12572412) | G9.js 探索自动交互的可微图形，让图形操作与计算相连。 | 237 | 29 | 2016-09-24 |
| 8 | [Show HN: Open-source search engine with 2bn-page index](https://news.ycombinator.com/item?id=12486631) | 作者展示拥有二十亿页面索引的开源搜索引擎。 | 229 | 139 | 2016-09-13 |
| 9 | [Show HN: Postacard – Text a Photo to Send as a Postcard Anywhere on Earth for $3](https://news.ycombinator.com/item?id=12427505) | 发短信传照片，再以三美元把它寄成明信片送往世界各地。 | 218 | 88 | 2016-09-05 |
| 10 | [Show HN: An Open Retro RPG Game Maker in Python](https://news.ycombinator.com/item?id=12589538) | 用 Python 制作开放的复古 RPG 游戏创作工具。 | 215 | 27 | 2016-09-27 |

### 2016-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Your Social Media Fingerprint (maybe NSFW)](https://news.ycombinator.com/item?id=12692190) | 社交媒体指纹项目展示，看看网络活动留下哪些识别线索。 | 911 | 247 | 2016-10-12 |
| 2 | [Show HN: Tesseract.js – Pure JavaScript OCR for 60 Languages](https://news.ycombinator.com/item?id=12694004) | Tesseract.js 用纯 JavaScript 提供支持六十种语言的文字识别。 | 727 | 97 | 2016-10-12 |
| 3 | [Show HN: Ascii to SVG](https://news.ycombinator.com/item?id=12621680) | 把 ASCII 字符图转成 SVG，让文字草图成为矢量图形。 | 416 | 76 | 2016-10-02 |
| 4 | [Show HN: A new decentralized microblogging platform](https://news.ycombinator.com/item?id=12646083) | 新的去中心化微博平台亮相，探索短内容的分布式发布。 | 364 | 146 | 2016-10-05 |
| 5 | [Show HN: TagSpaces – An open source personal data manager](https://news.ycombinator.com/item?id=12679597) | TagSpaces 提供开源个人数据管理工具。 | 361 | 83 | 2016-10-10 |
| 6 | [Show HN: A fork of sudo with Touch ID support](https://news.ycombinator.com/item?id=12834327) | 为 sudo 加入 Touch ID 支持，通过指纹完成提权认证。 | 347 | 128 | 2016-10-31 |
| 7 | [Show HN: Killing Procrastination by Making Everything Fit](https://news.ycombinator.com/item?id=12786935) | 作者尝试通过“让所有事情都安排得下”来应对拖延。 | 301 | 86 | 2016-10-25 |
| 8 | [Show HN: I made a Chrome extension that helps battle impulsive procrastination](https://news.ycombinator.com/item?id=12721709) | 一个对抗冲动性拖延的 Chrome 扩展，帮助及时打断分心。 | 277 | 122 | 2016-10-16 |
| 9 | [Show HN: Get encrypted data from people that don’t know how to encrypt](https://news.ycombinator.com/item?id=12742395) | 让不懂加密的人也能发送加密数据，降低安全传输的操作门槛。 | 275 | 93 | 2016-10-19 |
| 10 | [Show HN: CSS ICON, an icon set crafted by pure CSS](https://news.ycombinator.com/item?id=12723281) | CSS ICON 完全用 CSS 绘制图标，展示无需图片的图标集合。 | 250 | 67 | 2016-10-17 |

### 2016-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: A visual guide to the most popular CSS properties](https://news.ycombinator.com/item?id=13031492) | 展示一份通过视觉示例讲解常用 CSS 属性的指南。 | 1117 | 122 | 2016-11-24 |
| 2 | [Show HN: Primitive for macOS](https://news.ycombinator.com/item?id=12958445) | Primitive 推出 macOS 应用，作者向社区展示这一版本。 | 798 | 145 | 2016-11-15 |
| 3 | [Show HN: Dply – Free temporary Linux servers](https://news.ycombinator.com/item?id=13030603) | Dply 提供免费的临时 Linux 服务器，适合短时使用需求。 | 673 | 198 | 2016-11-24 |
| 4 | [Show HN: Make an app by adding JSON to this app](https://news.ycombinator.com/item?id=12879179) | 往现有应用添加 JSON 即可制作应用，作者展示配置驱动的构建思路。 | 648 | 176 | 2016-11-05 |
| 5 | [Show HN: DevFreeBooks – A collection of free books for developers](https://news.ycombinator.com/item?id=12909967) | DevFreeBooks 汇集开发者可免费阅读的技术书籍。 | 571 | 62 | 2016-11-09 |
| 6 | [Show HN: Antd – A set of high-quality React components](https://news.ycombinator.com/item?id=13053137) | Antd 提供一组 React 组件，方便构建应用界面。 | 507 | 104 | 2016-11-28 |
| 7 | [Show HN: React Native Express – Learn React Native Through Interactive Examples](https://news.ycombinator.com/item?id=13056678) | React Native Express 通过交互示例讲解 React Native。 | 496 | 53 | 2016-11-28 |
| 8 | [Show HN: Spamnesty: Waste spammers' time](https://news.ycombinator.com/item?id=13013327) | Spamnesty 帮用户消耗垃圾邮件发送者的时间。 | 405 | 183 | 2016-11-22 |
| 9 | [Show HN: Learn to Code for Free](https://news.ycombinator.com/item?id=13018104) | 免费编程学习项目亮相，为想写代码的人提供入门资源。 | 395 | 135 | 2016-11-22 |
| 10 | [Show HN: Anycomplete](https://news.ycombinator.com/item?id=13065670) | Anycomplete 项目展示，邀请社区了解它对补全体验的探索。 | 390 | 85 | 2016-11-29 |

### 2016-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Rocket – Web Framework for Rust](https://news.ycombinator.com/item?id=13245475) | Rocket 是面向 Rust 的 Web 框架，展示用 Rust 开发网站的路径。 | 484 | 114 | 2016-12-23 |
| 2 | [Show HN: Hire an Oldster](https://news.ycombinator.com/item?id=13194074) | Hire an Oldster 聚焦年长求职者，尝试为他们创造招聘机会。 | 475 | 295 | 2016-12-16 |
| 3 | [Show HN: The Road to learn React – Build a Hacker News App on the Way](https://news.ycombinator.com/item?id=13170837) | 边做 Hacker News 应用边学 React，把基础知识串成完整项目。 | 339 | 22 | 2016-12-13 |
| 4 | [Show HN: Wick – A free and open-source creation suite](https://news.ycombinator.com/item?id=13244827) | Wick 提供免费开源的创作套件，供创作者尝试。 | 322 | 63 | 2016-12-23 |
| 5 | [Show HN: U.S. Legal Concepts for Founders – Online Handbook](https://news.ycombinator.com/item?id=13132944) | 面向创业者的美国法律概念在线手册，整理创业相关法律知识。 | 309 | 50 | 2016-12-08 |
| 6 | [Show HN: Handicareers.com – A simple job board for disabled people](https://news.ycombinator.com/item?id=13095553) | Handicareers 用简单招聘板为残障人士汇集工作机会。 | 303 | 82 | 2016-12-03 |
| 7 | [Show HN: ThreadTone – Halftone images made of thread](https://news.ycombinator.com/item?id=13254029) | ThreadTone 用线条制作半色调图像，探索线与影调的转换。 | 303 | 44 | 2016-12-25 |
| 8 | [Show HN: 8bitworkshop IDE for Atari 2600](https://news.ycombinator.com/item?id=13254342) | 8bitworkshop 为 Atari 2600 提供集成开发环境。 | 289 | 36 | 2016-12-25 |
| 9 | [Show HN: Fun tool that cut my family and friends tech support time in half](https://news.ycombinator.com/item?id=13120111) | 作者展示给亲友提供技术支持的工具，并称支持时间减少了一半。 | 285 | 215 | 2016-12-07 |
| 10 | [Show HN: Learn how to build electronics with monthly kits](https://news.ycombinator.com/item?id=13259429) | 每月寄送电子套件，在动手制作中学习电子技术。 | 272 | 112 | 2016-12-26 |

### 2017-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Privacy-focused, ad-free, non-tracking torrent search engine](https://news.ycombinator.com/item?id=13423629) | 展示一个强调隐私、无广告且不追踪用户的种子搜索引擎。 | 1183 | 346 | 2017-01-18 |
| 2 | [Show HN: Alacritty, a GPU-accelerated terminal emulator written in Rust](https://news.ycombinator.com/item?id=13338592) | Alacritty 是用 Rust 编写、利用 GPU 加速的终端模拟器。 | 1170 | 476 | 2017-01-06 |
| 3 | [Show HN: Explore ideas whose patent protection expires today](https://news.ycombinator.com/item?id=13309025) | 探索专利保护于今天到期的点子，发现进入公共领域的技术。 | 546 | 142 | 2017-01-03 |
| 4 | [Show HN: Crafting Interpreters – A handbook for making programming languages](https://news.ycombinator.com/item?id=13406081) | 《Crafting Interpreters》讲解编程语言制作，带读者动手实现解释器。 | 423 | 75 | 2017-01-15 |
| 5 | [Show HN: Whoishiring.io – all tech jobs mapped out](https://news.ycombinator.com/item?id=13500701) | Whoishiring.io 把技术岗位放上地图，按位置发现工作机会。 | 419 | 76 | 2017-01-27 |
| 6 | [Show HN: Magnetissimo – Self-hosted torrent search engine written in Elixir](https://news.ycombinator.com/item?id=13505226) | Magnetissimo 是用 Elixir 编写、可自行托管的种子搜索引擎。 | 403 | 107 | 2017-01-28 |
| 7 | [Show HN: A travel tool to discover destinations based on your budget](https://news.ycombinator.com/item?id=13458561) | 根据旅行预算发现目的地，帮助把花费限制转成出行选择。 | 377 | 165 | 2017-01-23 |
| 8 | [Show HN: Invite friends to SSH into your laptop using their GitHub handle](https://news.ycombinator.com/item?id=13485501) | 只用朋友的 GitHub 用户名，邀请他们通过 SSH 连接自己的笔记本。 | 334 | 99 | 2017-01-25 |
| 9 | [Show HN: Founderkit – Startup tool recommendations from 1,000 YC founders](https://news.ycombinator.com/item?id=13376901) | Founderkit 整理一千位 YC 创业者推荐的创业工具。 | 331 | 59 | 2017-01-11 |
| 10 | [Show HN: Math Attack – My side project of 3 years](https://news.ycombinator.com/item?id=13470425) | 作者展示做了三年的业余项目 Math Attack。 | 292 | 113 | 2017-01-24 |

### 2017-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: A guide to all HTML5 elements and attributes](https://news.ycombinator.com/item?id=13642662) | 一份涵盖 HTML5 元素与属性的指南，方便开发时查询。 | 728 | 93 | 2017-02-14 |
| 2 | [Show HN: Rumuki, a prenup for sex tapes](https://news.ycombinator.com/item?id=13628522) | Rumuki 将“婚前协议”的比喻用于私密视频，探索双方约定的产品形式。 | 405 | 198 | 2017-02-12 |
| 3 | [Show HN: Generate a quiz from a Wikipedia page](https://news.ycombinator.com/item?id=13677748) | 给定一篇维基百科文章，自动生成相关测验。 | 388 | 85 | 2017-02-19 |
| 4 | [Show HN: Evilpass – A slightly evil password strength checker](https://news.ycombinator.com/item?id=13674890) | Evilpass 自称“略带恶意”的密码强度检查器，展示特别的交互点子。 | 367 | 162 | 2017-02-18 |
| 5 | [Show HN: PDFLayoutTextStripper – Converts PDF to text while keeping the layout](https://news.ycombinator.com/item?id=13729301) | PDFLayoutTextStripper 将 PDF 转成文本，同时保留页面布局。 | 283 | 92 | 2017-02-25 |
| 6 | [Show HN: Hasura – A Postgres BaaS and Kubernetes PaaS on Your Own Infrastructure](https://news.ycombinator.com/item?id=13724118) | Hasura 在用户自己的基础设施上提供 PostgreSQL 后端和 Kubernetes 平台。 | 259 | 69 | 2017-02-24 |
| 7 | [Show HN: Beehive – An open source IFTTT powered by Go's templating engine](https://news.ycombinator.com/item?id=13623852) | Beehive 用 Go 模板引擎构建开源自动化工具，思路类似 IFTTT。 | 247 | 44 | 2017-02-11 |
| 8 | [Show HN: Arrived – Stack Overflow for US Immigration](https://news.ycombinator.com/item?id=13543072) | Arrived 打造美国移民主题的问答平台，借鉴 Stack Overflow 模式。 | 244 | 82 | 2017-02-01 |
| 9 | [Show HN: Posters of Your GitHub Contributions](https://news.ycombinator.com/item?id=13552376) | 把 GitHub 贡献记录做成海报，让代码活动变成墙上作品。 | 235 | 76 | 2017-02-02 |
| 10 | [Show HN: How to write a tiny compiler](https://news.ycombinator.com/item?id=13608810) | 从小型编译器入手，学习源代码如何被转换。 | 224 | 63 | 2017-02-09 |

### 2017-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Kite, copilot for programmers, available for Python](https://news.ycombinator.com/item?id=13977982) | Kite 向 Python 开发者开放，尝试成为编程时的辅助搭档。 | 553 | 243 | 2017-03-28 |
| 2 | [Show HN: Colormind – Color schemes via Generative Adversarial Networks](https://news.ycombinator.com/item?id=13960214) | Colormind 利用生成对抗网络生成配色方案。 | 399 | 52 | 2017-03-26 |
| 3 | [Show HN: How to write a recursive descent parser](https://news.ycombinator.com/item?id=13914218) | 讲解递归下降解析器的写法，把语法规则变成可执行代码。 | 347 | 148 | 2017-03-20 |
| 4 | [Show HN: Sleeping Beauty, a 7-day roguelike game](https://news.ycombinator.com/item?id=13838659) | Sleeping Beauty 是七天游戏挑战中的 Roguelike 作品。 | 319 | 97 | 2017-03-10 |
| 5 | [Show HN: A new hobby OS from “scratch” in C#](https://news.ycombinator.com/item?id=13794879) | 作者用 C# 从零尝试编写业余操作系统。 | 310 | 63 | 2017-03-05 |
| 6 | [Show HN: Gutenberg – Modern CSS framework to print the web correctly](https://news.ycombinator.com/item?id=13763469) | Gutenberg 用 CSS 框架改善网页打印效果。 | 305 | 59 | 2017-03-01 |
| 7 | [Show HN: Boot Windows 10 Directly into Linux Desktop of Choice](https://news.ycombinator.com/item?id=13762077) | 让 Windows 10 启动后直接进入选定的 Linux 桌面。 | 264 | 104 | 2017-03-01 |
| 8 | [Show HN: Lumix Engine – Open source C++ 3D game engine](https://news.ycombinator.com/item?id=13762032) | Lumix Engine 提供开源 C++ 三维游戏引擎。 | 260 | 117 | 2017-03-01 |
| 9 | [Show HN: Go from Docker-Compose to Kubernetes with a simple tool](https://news.ycombinator.com/item?id=13783546) | 一个简单工具将 Docker Compose 配置带到 Kubernetes。 | 249 | 45 | 2017-03-03 |
| 10 | [Show HN: NoFile.io – A simple file storage site with lots of perks](https://news.ycombinator.com/item?id=13809462) | NoFile.io 展示文件存储网站，面向便捷的文件保存需求。 | 231 | 186 | 2017-03-07 |

### 2017-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Sorting Two Metric Tons of Lego](https://news.ycombinator.com/item?id=14226889) | 作者展示给两吨乐高积木分类的过程。 | 1264 | 211 | 2017-04-29 |
| 2 | [Show HN: React-data sheet, Excel-like spreadsheet component](https://news.ycombinator.com/item?id=14032201) | React-data sheet 为 React 提供类似 Excel 的电子表格组件。 | 345 | 89 | 2017-04-04 |
| 3 | [Show HN: Zuck.js, a JavaScript library that lets you add Stories everywhere](https://news.ycombinator.com/item?id=14135045) | Zuck.js 让网站加入 Stories 式内容展示。 | 339 | 58 | 2017-04-17 |
| 4 | [Show HN: An attempt to rethink a music sequencer design](https://news.ycombinator.com/item?id=14212054) | 作者重新思考音乐音序器的设计，展示一种不同的编曲交互。 | 305 | 113 | 2017-04-27 |
| 5 | [Show HN: Is It Snappy? – Measure latency with your iPhone's 240 Hz camera](https://news.ycombinator.com/item?id=14023196) | Is It Snappy? 利用 iPhone 每秒 240 帧摄像头测量延迟。 | 293 | 84 | 2017-04-03 |
| 6 | [Show HN: Audioshop – Audio image editing](https://news.ycombinator.com/item?id=14135781) | Audioshop 将音频与图像编辑结合，探索跨媒介的处理方式。 | 285 | 45 | 2017-04-18 |
| 7 | [Show HN: 'Hack' the user cursor](https://news.ycombinator.com/item?id=14124285) | 围绕用户光标做一场“黑客”实验，展示指针交互的可玩性。 | 267 | 58 | 2017-04-16 |
| 8 | [Show HN: Timestrap – Self-hosted online time tracking](https://news.ycombinator.com/item?id=14180673) | Timestrap 提供可自行托管的在线时间记录工具。 | 264 | 75 | 2017-04-23 |
| 9 | [Show HN: My RIP Goodbye to my Co-Founder Carlos Icaza](https://news.ycombinator.com/item?id=14147585) | 作者用代码纪念意外离世的联合创始人 Carlos Icaza。 | 261 | 22 | 2017-04-19 |
| 10 | [Show HN: Visual Studio Code for ARM, submitted to core](https://news.ycombinator.com/item?id=14137563) | 作者将 Visual Studio Code 移植到 ARM，并向核心项目提交成果。 | 236 | 83 | 2017-04-18 |

### 2017-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: My first native iOS app – Cone, a real time color picker](https://news.ycombinator.com/item?id=14254357) | Cone 是作者的首个原生 iOS 应用，用手机实时拾取颜色。 | 418 | 151 | 2017-05-03 |
| 2 | [Show HN: ORY Editor – A rich editor for the browser, built with React and Redux](https://news.ycombinator.com/item?id=14417340) | ORY Editor 基于 React 与 Redux，提供浏览器富内容编辑能力。 | 369 | 98 | 2017-05-25 |
| 3 | [Show HN: FSQL – Search through your file system with SQL-esque queries](https://news.ycombinator.com/item?id=14343967) | FSQL 用类似 SQL 的查询语法搜索文件系统。 | 341 | 126 | 2017-05-15 |
| 4 | [Show HN: Kryptonite – a new home for your SSH private key](https://news.ycombinator.com/item?id=14240626) | Kryptonite 为 SSH 私钥提供新的存放方案，关注密钥使用方式。 | 338 | 219 | 2017-05-01 |
| 5 | [Show HN: 100M Books – Open a new tab, discover a new book](https://news.ycombinator.com/item?id=14286133) | 100M Books 让每次打开新标签页都成为发现新书的机会。 | 289 | 100 | 2017-05-07 |
| 6 | [Show HN: Early-stage Yahoo Pipes spiritual successor](https://news.ycombinator.com/item?id=14440993) | 一个尚处早期的 Yahoo Pipes 精神续作，继续探索可组合的数据处理。 | 280 | 126 | 2017-05-29 |
| 7 | [Show HN: Real-time notes app built with Vue.js, inspired by Notational Velocity](https://news.ycombinator.com/item?id=14409760) | 用 Vue.js 构建实时笔记应用，设计受到 Notational Velocity 启发。 | 257 | 141 | 2017-05-24 |
| 8 | [Show HN: A WebAssembly game demo](https://news.ycombinator.com/item?id=14411328) | 一个 WebAssembly 游戏演示，展示浏览器中的新运行方式。 | 251 | 108 | 2017-05-24 |
| 9 | [Show HN: Legion, an as-simple-as-possible blockchain server written in Haskell](https://news.ycombinator.com/item?id=14439789) | Legion 用 Haskell 编写，追求尽可能简单的区块链服务器。 | 239 | 71 | 2017-05-29 |
| 10 | [Show HN: VPS Comparison – Automated tests to compare VPS by yourself](https://news.ycombinator.com/item?id=14245538) | 通过自动测试自行比较 VPS，了解不同虚拟服务器的表现。 | 228 | 146 | 2017-05-02 |

### 2017-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Get Paid to Build Your Next Side Project](https://news.ycombinator.com/item?id=14552615) | 展示一个让开发者获得报酬、构建下一个业余项目的平台。 | 1100 | 451 | 2017-06-14 |
| 2 | [Show HN: Monica, an open-source CRM to manage friends and family](https://news.ycombinator.com/item?id=14497295) | Monica 是开源的个人关系管理工具，帮助维护亲友联系。 | 1097 | 568 | 2017-06-06 |
| 3 | [Show HN: GreenPiThumb – A Raspberry Pi Gardening Bot](https://news.ycombinator.com/item?id=14644539) | GreenPiThumb 把树莓派变成园艺机器人，照料植物也能自动化。 | 537 | 181 | 2017-06-27 |
| 4 | [Show HN: Snips is a AI Voice Assistant platform 100% on-device and private](https://news.ycombinator.com/item?id=14558582) | Snips 展示完全在设备本地运行、关注隐私的 AI 语音助手平台。 | 372 | 129 | 2017-06-15 |
| 5 | [Show HN: Decaffeinate converts CoffeeScript projects to modern JS](https://news.ycombinator.com/item?id=14583882) | Decaffeinate 将 CoffeeScript 项目转换为现代 JavaScript。 | 361 | 219 | 2017-06-19 |
| 6 | [Show HN: Insect – a high-precision scientific calculator with physical units](https://news.ycombinator.com/item?id=14625795) | Insect 提供支持物理单位的高精度科学计算器。 | 354 | 195 | 2017-06-24 |
| 7 | [Show HN: Password-protect a static HTML page](https://news.ycombinator.com/item?id=14553401) | 给静态 HTML 页面加密码保护，探索轻量访问控制。 | 348 | 149 | 2017-06-14 |
| 8 | [Show HN: Hackerhunt – categorised curation of Show HN submissions](https://news.ycombinator.com/item?id=14652217) | Hackerhunt 分类整理 Show HN 投稿，帮助发现社区作品。 | 335 | 65 | 2017-06-28 |
| 9 | [Show HN: Sourcetrail – Get productive on unfamiliar source code](https://news.ycombinator.com/item?id=14612440) | Sourcetrail 帮开发者理解陌生源代码，更快进入项目。 | 328 | 117 | 2017-06-22 |
| 10 | [Show HN: Algorithm Cookbook in Rust](https://news.ycombinator.com/item?id=14587669) | 用 Rust 编写的算法手册，通过代码查阅常见算法。 | 320 | 71 | 2017-06-19 |

### 2017-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: A virtual machine made with Google Sheets formulas (no script)](https://news.ycombinator.com/item?id=14703098) | 不用脚本，只靠 Google Sheets 公式实现虚拟机。 | 620 | 37 | 2017-07-05 |
| 2 | [Show HN: TensorFire](https://news.ycombinator.com/item?id=14894653) | TensorFire 项目亮相，作者邀请社区查看并提供反馈。 | 564 | 83 | 2017-07-31 |
| 3 | [Show HN: The JavaScript Way, a book for learning modern JavaScript from scratch](https://news.ycombinator.com/item?id=14865043) | 《The JavaScript Way》从零讲解现代 JavaScript。 | 545 | 110 | 2017-07-27 |
| 4 | [Show HN: A Set of Dice That Follows the Gambler's Fallacy](https://news.ycombinator.com/item?id=14805265) | 一组遵循“赌徒谬误”的骰子，把错误概率直觉做成实验。 | 523 | 230 | 2017-07-19 |
| 5 | [Show HN: $200 Solar Self-Sufficiency  Without Your Landlord Noticing](https://news.ycombinator.com/item?id=14821478) | 用两百美元尝试太阳能自给，作者强调适合不惊动房东的改造。 | 491 | 182 | 2017-07-21 |
| 6 | [Show HN: Chromeless – Headless Chrome Automation on AWS Lambda](https://news.ycombinator.com/item?id=14859084) | Chromeless 在 AWS Lambda 上自动操作无头 Chrome。 | 385 | 89 | 2017-07-26 |
| 7 | [Show HN: Quilt – manage data like code](https://news.ycombinator.com/item?id=14771406) | Quilt 希望像管理代码一样管理数据。 | 367 | 178 | 2017-07-14 |
| 8 | [Show HN: Cinc – GitHub for recipes](https://news.ycombinator.com/item?id=14799111) | Cinc 借鉴 GitHub 的模式，为食谱建立分享与管理空间。 | 363 | 152 | 2017-07-18 |
| 9 | [Show HN: Seashells – Pipe output from CLI apps to the web in real time](https://news.ycombinator.com/item?id=14737118) | Seashells 将命令行程序输出实时传到网页，方便远程查看。 | 356 | 70 | 2017-07-10 |
| 10 | [Show HN: Musikcube, a terminal-based music player, library, and streaming server](https://news.ycombinator.com/item?id=14853212) | Musikcube 集终端音乐播放器、曲库与流媒体服务器于一体。 | 340 | 82 | 2017-07-26 |

### 2017-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: A stop-motion video of an engine](https://news.ycombinator.com/item?id=15017126) | 展示一段关于发动机的定格动画。 | 845 | 188 | 2017-08-15 |
| 2 | [Show HN: Is the stock market going to crash?](https://news.ycombinator.com/item?id=14947361) | 展示一个以“股市会崩盘吗”为问题的网站。 | 813 | 325 | 2017-08-07 |
| 3 | [Show HN: Extension-blocking domains removed by threat from other blacklists](https://news.ycombinator.com/item?id=14997799) | 通过扩展拦截那些因威胁而被其他黑名单移除的域名。 | 614 | 155 | 2017-08-12 |
| 4 | [Show HN: The best time to visit any city](https://news.ycombinator.com/item?id=15074526) | 按城市查看适合旅行的时间，帮助决定何时前往目的地。 | 395 | 118 | 2017-08-22 |
| 5 | [Show HN: Mathcha – Online Mathematics Editor](https://news.ycombinator.com/item?id=15000947) | Mathcha 提供在线数学编辑器，方便编写数学内容。 | 358 | 56 | 2017-08-13 |
| 6 | [Show HN: Moon – fast 7k Vue alternative](https://news.ycombinator.com/item?id=15105726) | Moon 展示约 7KB 的 Vue 替代方案，作者主打速度与体积。 | 268 | 192 | 2017-08-26 |
| 7 | [Show HN: Product Graveyard – Commemorating the most memorable dead products](https://news.ycombinator.com/item?id=15041620) | Product Graveyard 纪念已经消失、却令人难忘的产品。 | 265 | 126 | 2017-08-17 |
| 8 | [Show HN: An interactive guide to compression basics](https://news.ycombinator.com/item?id=14957201) | 交互式讲解压缩基础，直观看数据如何缩小。 | 256 | 66 | 2017-08-08 |
| 9 | [Show HN: Bt – BitTorrent library in Java 8](https://news.ycombinator.com/item?id=14911372) | Bt 为 Java 8 提供 BitTorrent 库。 | 254 | 87 | 2017-08-02 |
| 10 | [Show HN: Pdf-Bot, an API/CLI for Generating PDFs Using Headless Chrome](https://news.ycombinator.com/item?id=15070686) | Pdf-Bot 使用无头 Chrome 生成 PDF，同时提供 API 与命令行。 | 235 | 79 | 2017-08-22 |

### 2017-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: A coloring book of data structures and algorithms](https://news.ycombinator.com/item?id=15201152) | 给数据结构和算法做涂色书，通过选择排序原型尝试边涂边学。 | 523 | 105 | 2017-09-08 |
| 2 | [Show HN: I'll mail Equifax your arbitration opt-out for free](https://news.ycombinator.com/item?id=15207151) | 作者免费代寄 Equifax 仲裁退出信，帮助用户完成手续。 | 431 | 87 | 2017-09-09 |
| 3 | [Show HN: Build A Personal Power Plant for $200](https://news.ycombinator.com/item?id=15216650) | 用两百美元建立个人发电站，作者展示低成本能源项目。 | 373 | 103 | 2017-09-11 |
| 4 | [Show HN: Logo Crunch – Multi-resolution logo maker](https://news.ycombinator.com/item?id=15330409) | Logo Crunch 制作多种分辨率标志，适配不同尺寸的显示需求。 | 328 | 65 | 2017-09-25 |
| 5 | [Show HN: Doogie – A Chromium-Based Browser with Tree-Style Pages](https://news.ycombinator.com/item?id=15277351) | Doogie 基于 Chromium，用树形结构组织网页。 | 264 | 78 | 2017-09-18 |
| 6 | [Show HN: No Coin – A browser extension to block coin miners](https://news.ycombinator.com/item?id=15270799) | No Coin 用浏览器扩展拦截网页挖矿程序。 | 254 | 261 | 2017-09-17 |
| 7 | [Show HN: 1 KB JavaScript library for building front end apps](https://news.ycombinator.com/item?id=15207117) | 一个约 1KB 的 JavaScript 库，用于构建前端应用。 | 242 | 2 | 2017-09-09 |
| 8 | [Show HN: Redox Rust OS – v0.3.3 release](https://news.ycombinator.com/item?id=15290607) | 用 Rust 编写的 Redox 操作系统发布 0.3.3 版本。 | 232 | 76 | 2017-09-20 |
| 9 | [Show HN: Nulis – Open Source Tree Editor for Writers](https://news.ycombinator.com/item?id=15256215) | Nulis 为写作者提供开源树形编辑器，帮助组织内容结构。 | 231 | 83 | 2017-09-15 |
| 10 | [Show HN: Moocha.io – A search engine for MOOCs](https://news.ycombinator.com/item?id=15346381) | Moocha.io 提供 MOOC 搜索引擎，寻找合适的在线公开课。 | 231 | 54 | 2017-09-27 |

### 2017-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Arxiv Vanity – Read academic papers from Arxiv as responsive web pages](https://news.ycombinator.com/item?id=15534580) | Arxiv Vanity 把论文转成响应式网页，改善不同屏幕上的阅读。 | 721 | 134 | 2017-10-23 |
| 2 | [Show HN: Metaballs](https://news.ycombinator.com/item?id=15492248) | Metaballs 图形项目展示，探索相互融合的形体效果。 | 673 | 93 | 2017-10-17 |
| 3 | [Show HN: Frappe Charts – GitHub inspired JavaScript charting with zero dependencies](https://news.ycombinator.com/item?id=15594004) | Frappe Charts 借鉴 GitHub 图表风格，提供无依赖 JavaScript 绘图工具。 | 474 | 87 | 2017-10-31 |
| 4 | [Show HN: Airborn – Private Google Docs Alternative](https://news.ycombinator.com/item?id=15596304) | Airborn 关注文档隐私，提供 Google Docs 的替代方案。 | 469 | 203 | 2017-10-31 |
| 5 | [Show HN: A simple, fast and user-friendly alternative to find, written in Rust](https://news.ycombinator.com/item?id=15429390) | 用 Rust 编写 find 的替代工具，作者追求简单、快速和易用。 | 456 | 215 | 2017-10-08 |
| 6 | [Show HN: The Million Dollar Homepage as an Ethereum Smart Contract and DApp](https://news.ycombinator.com/item?id=15393446) | 把“百万美元主页”做成以太坊智能合约和去中心化应用。 | 344 | 117 | 2017-10-03 |
| 7 | [Show HN: Paint yourself in the style of classic art, in your browser](https://news.ycombinator.com/item?id=15383336) | 在浏览器里把自己画成经典艺术风格，体验图像创作实验。 | 266 | 99 | 2017-10-02 |
| 8 | [Show HN: Gutenberg – A static site engine as a single executable](https://news.ycombinator.com/item?id=15507538) | Gutenberg 将静态站点引擎打包成单个可执行文件。 | 241 | 148 | 2017-10-19 |
| 9 | [Show HN: A platform for sharing DIY solar projects](https://news.ycombinator.com/item?id=15425324) | 为自制太阳能项目建立分享平台，交流动手实践。 | 236 | 61 | 2017-10-07 |
| 10 | [Show HN: Resume Worded – Write impactful resumes](https://news.ycombinator.com/item?id=15417975) | Resume Worded 帮助打磨简历表述，让工作经历更有说服力。 | 209 | 116 | 2017-10-06 |

### 2017-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Fruits and vegetables in season in your zip code](https://news.ycombinator.com/item?id=15739744) | 输入邮政编码，查找当地正当季的水果与蔬菜。 | 572 | 115 | 2017-11-20 |
| 2 | [Show HN: LogoFox – fast logo maker](https://news.ycombinator.com/item?id=15757844) | LogoFox 提供快速制作标志的工具。 | 431 | 106 | 2017-11-22 |
| 3 | [Show HN: Nebula – Alarm clock where you grow stars while you sleep](https://news.ycombinator.com/item?id=15765762) | Nebula 把睡眠与“养星星”结合，重新设计闹钟体验。 | 345 | 154 | 2017-11-23 |
| 4 | [Show HN: Gophercises – Coding Exercises for Budding Gophers](https://news.ycombinator.com/item?id=15761537) | Gophercises 为 Go 初学者提供编程练习。 | 328 | 88 | 2017-11-22 |
| 5 | [Show HN: Server.js – A modern Express alternative](https://news.ycombinator.com/item?id=15624206) | Server.js 展示面向现代开发的 Express 替代方案。 | 295 | 117 | 2017-11-04 |
| 6 | [Show HN: Golang DNS server, including DNSSEC and DNS-over-TLS](https://news.ycombinator.com/item?id=15796943) | 用 Go 编写 DNS 服务器，包含 DNSSEC 和 DNS-over-TLS 支持。 | 283 | 64 | 2017-11-28 |
| 7 | [Show HN: Javalin 1.0 – A Kotlin/Java web framework](https://news.ycombinator.com/item?id=15644430) | Javalin 1.0 为 Kotlin 与 Java 提供 Web 开发框架。 | 271 | 87 | 2017-11-07 |
| 8 | [Show HN: Datasette – Create and publish an API for SQLite databases](https://news.ycombinator.com/item?id=15691409) | Datasette 帮用户为 SQLite 数据库创建并发布 API。 | 269 | 44 | 2017-11-14 |
| 9 | [Show HN: Orange Forum – Web 1.0 style forum written in Go](https://news.ycombinator.com/item?id=15645276) | Orange Forum 用 Go 制作 Web 1.0 风格的论坛。 | 226 | 172 | 2017-11-07 |
| 10 | [Show HN: /usr/bin/htop](https://news.ycombinator.com/item?id=15601027) | 作者以 /usr/bin/htop 为题展示项目，邀请终端工具用户查看。 | 219 | 59 | 2017-11-01 |

### 2017-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Airmash – Multiplayer Missile Warfare HTML5 Game](https://news.ycombinator.com/item?id=15892066) | Airmash 是一款基于 HTML5 的多人导弹对战游戏。 | 1535 | 304 | 2017-12-10 |
| 2 | [Show HN: Culture Queries – The best questions to ask during your job interview](https://news.ycombinator.com/item?id=15908812) | Culture Queries 整理求职面试时值得反问的问题，帮助了解公司文化。 | 572 | 125 | 2017-12-12 |
| 3 | [Show HN: An educational blockchain implementation in Python](https://news.ycombinator.com/item?id=15945490) | 用 Python 实现教学版区块链，便于理解基本结构。 | 412 | 41 | 2017-12-17 |
| 4 | [Show HN: Enlight – Learn to code by building projects](https://news.ycombinator.com/item?id=15892554) | Enlight 通过构建实际项目帮助学习编程。 | 322 | 52 | 2017-12-10 |
| 5 | [Show HN: Open Paperless – Scan, index, and archive paper documents](https://news.ycombinator.com/item?id=15983492) | Open Paperless 将纸质文件扫描、索引并归档。 | 285 | 96 | 2017-12-21 |
| 6 | [Show HN: Discover, Listen and Discuss Classical Music](https://news.ycombinator.com/item?id=15860312) | 围绕古典音乐建立发现、收听与讨论的空间。 | 273 | 107 | 2017-12-06 |
| 7 | [Show HN: Data Prism – Weekly newsletter about data science, ML, AI and analytics](https://news.ycombinator.com/item?id=16009233) | Data Prism 每周整理数据科学、机器学习、AI 与分析内容。 | 233 | 11 | 2017-12-26 |
| 8 | [Show HN: Solo – App for sharing loneliness and aloneness](https://news.ycombinator.com/item?id=16001795) | Solo 让用户分享孤独与独处体验，给这些感受一个表达空间。 | 215 | 84 | 2017-12-24 |
| 9 | [Show HN: LibreRead 1.0 – Self-Hosted Free Ebook Reader](https://news.ycombinator.com/item?id=15897259) | LibreRead 1.0 提供可自行托管的免费电子书阅读器。 | 210 | 83 | 2017-12-11 |
| 10 | [Show HN: Work at a Startup – Find a Job at a YC Company](https://news.ycombinator.com/item?id=15916350) | Work at a Startup 汇集 YC 公司职位，帮助寻找创业团队的工作。 | 210 | 86 | 2017-12-13 |

### 2018-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Observable Notebooks](https://news.ycombinator.com/item?id=16274686) | Observable Notebooks 项目展示，探索交互笔记本的表达方式。 | 654 | 128 | 2018-01-31 |
| 2 | [Show HN: Self-generated custom art for your home or Airbnb](https://news.ycombinator.com/item?id=16216960) | 为家中或 Airbnb 生成定制艺术作品，尝试个性化空间装饰。 | 644 | 166 | 2018-01-23 |
| 3 | [Show HN: Sapper.js – towards a better web app framework](https://news.ycombinator.com/item?id=16052558) | Sapper.js 展示 Web 应用框架，希望改善应用开发体验。 | 410 | 209 | 2018-01-02 |
| 4 | [Show HN: PAST, a secure alternative to JWT](https://news.ycombinator.com/item?id=16070394) | PAST 被作者定位为更安全的 JWT 替代方案。 | 362 | 138 | 2018-01-04 |
| 5 | [Show HN: A game my 12-year-old daughter wrote](https://news.ycombinator.com/item?id=16049026) | 作者分享 12 岁女儿编写的游戏，展示孩子的创作成果。 | 341 | 98 | 2018-01-02 |
| 6 | [Show HN: A simple Go web server with logging, tracing, health check](https://news.ycombinator.com/item?id=16090977) | 一个简单 Go Web 服务器，集成日志、链路追踪和健康检查。 | 318 | 91 | 2018-01-07 |
| 7 | [Show HN: A Decentralized StatusPage on IPFS](https://news.ycombinator.com/item?id=16273609) | 在 IPFS 上搭建去中心化状态页，发布服务运行信息。 | 316 | 127 | 2018-01-31 |
| 8 | [Show HN: RetroClip – Instant Replay for Your Mac](https://news.ycombinator.com/item?id=16223929) | RetroClip 为 Mac 提供即时回放，捕捉刚刚发生的屏幕内容。 | 309 | 116 | 2018-01-24 |
| 9 | [Show HN: A HN/Reddit-style site for scientific pre-prints and publications](https://news.ycombinator.com/item?id=16273171) | 为科学预印本和论文建立类似 HN、Reddit 的分享讨论站点。 | 275 | 107 | 2018-01-31 |
| 10 | [Show HN: Paper Programs – Run JavaScript on pieces of paper](https://news.ycombinator.com/item?id=16211516) | Paper Programs 尝试让 JavaScript 在一张张纸上运行。 | 235 | 52 | 2018-01-23 |

### 2018-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Six Degrees of Wikipedia](https://news.ycombinator.com/item?id=16468196) | 用“维基百科的六度分隔”项目探索条目之间的联系。 | 1176 | 324 | 2018-02-26 |
| 2 | [Show HN: Hacker News Classics](https://news.ycombinator.com/item?id=16442888) | 展示一个汇集 Hacker News 经典内容的项目。 | 864 | 107 | 2018-02-23 |
| 3 | [Show HN: A CSS Keylogger](https://news.ycombinator.com/item?id=16422696) | 用 CSS 制作键盘记录器，展示样式机制可能带来的信息泄露。 | 576 | 168 | 2018-02-20 |
| 4 | [Show HN: TablePlus – A macOS client for relational databases](https://news.ycombinator.com/item?id=16339004) | TablePlus 为 macOS 提供关系型数据库客户端。 | 333 | 155 | 2018-02-09 |
| 5 | [Show HN: Buy Me A Coffee – A free, fast and friendly way to receive donations](https://news.ycombinator.com/item?id=16484040) | Buy Me A Coffee 用“请杯咖啡”的方式帮助创作者接收捐赠。 | 331 | 369 | 2018-02-28 |
| 6 | [Show HN: Curated, Pre-trained ML Models for Transfer Learning](https://news.ycombinator.com/item?id=16368653) | 整理可用于迁移学习的预训练模型，减少从头训练的准备工作。 | 324 | 27 | 2018-02-13 |
| 7 | [Show HN: Cross-platform desktop applications with PyQT](https://news.ycombinator.com/item?id=16318677) | 用 PyQT 构建跨平台桌面应用，展示 Python 图形开发路径。 | 315 | 285 | 2018-02-06 |
| 8 | [Show HN: Ask a Dev](https://news.ycombinator.com/item?id=16316968) | Ask a Dev 项目亮相，围绕向开发者提问展开。 | 288 | 109 | 2018-02-06 |
| 9 | [Show HN: Decentralized application starter with Vue, Ethereum and IPFS](https://news.ycombinator.com/item?id=16409572) | 用 Vue、Ethereum 与 IPFS 组成去中心化应用起步模板。 | 245 | 80 | 2018-02-18 |
| 10 | [Show HN: Mitmproxy 3.0 released, an open-source console-based proxy](https://news.ycombinator.com/item?id=16452852) | 开源终端代理工具 Mitmproxy 发布 3.0 版本。 | 242 | 39 | 2018-02-24 |

### 2018-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: RoughJS – Create hand-drawn graphics using JavaScript](https://news.ycombinator.com/item?id=16571827) | RoughJS 让开发者用 JavaScript 创建手绘风格图形。 | 1087 | 92 | 2018-03-12 |
| 2 | [Show HN: My embarrassing personal website from the 90s](https://news.ycombinator.com/item?id=16505244) | 作者分享自己九十年代的个人网站，重看当年的网页设计。 | 867 | 417 | 2018-03-02 |
| 3 | [Show HN: Convert screenshots of equations to LaTeX](https://news.ycombinator.com/item?id=16535358) | 把数学公式截图转成 LaTeX，减少手工重敲公式。 | 456 | 98 | 2018-03-07 |
| 4 | [Show HN: A site that makes Spotify playlists of bands coming to town](https://news.ycombinator.com/item?id=16697359) | 为即将到本地演出的乐队生成 Spotify 歌单，提前熟悉现场音乐。 | 346 | 109 | 2018-03-28 |
| 5 | [Show HN: Graphite – A decentralized and encrypted Google Docs alternative](https://news.ycombinator.com/item?id=16490595) | Graphite 提供去中心化且加密的文档工具，尝试替代 Google Docs。 | 330 | 138 | 2018-03-01 |
| 6 | [Show HN: Turn indented text into mind maps](https://news.ycombinator.com/item?id=16706666) | 把带缩进的文字转成思维导图，用文本组织可视结构。 | 323 | 99 | 2018-03-29 |
| 7 | [Show HN: Hearth – A Dropbox-like, IPFS-powered personal website publisher](https://news.ycombinator.com/item?id=16521385) | Hearth 用 IPFS 发布个人网站，操作思路类似 Dropbox。 | 315 | 104 | 2018-03-05 |
| 8 | [Show HN: Tones.fm – Make synth music](https://news.ycombinator.com/item?id=16552777) | Tones.fm 让用户制作合成器音乐，体验电子声音创作。 | 309 | 48 | 2018-03-09 |
| 9 | [Show HN: Investment Calculator – A simple retirement calculator](https://news.ycombinator.com/item?id=16529557) | 一个简洁退休计算器，帮助估算投资与退休规划。 | 308 | 210 | 2018-03-06 |
| 10 | [Show HN: URL Canary – Get an alert when someone finds your secrets](https://news.ycombinator.com/item?id=16619580) | URL Canary 在秘密链接被发现时发出提醒。 | 273 | 116 | 2018-03-19 |

### 2018-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Intuitive Linear Algebra and 3D Geometry](https://news.ycombinator.com/item?id=16909714) | 用直观方式讲线性代数与三维几何，连接公式和空间理解。 | 402 | 42 | 2018-04-24 |
| 2 | [Show HN: I made a Chrome extension to reveal zero-width characters](https://news.ycombinator.com/item?id=16754987) | Chrome 扩展揭示文字中的零宽字符，让不可见内容显形。 | 385 | 96 | 2018-04-04 |
| 3 | [Show HN: Watch Stanford CS Lectures Together](https://news.ycombinator.com/item?id=16912601) | 一起观看斯坦福计算机课程，把独自听课变成共同学习。 | 360 | 49 | 2018-04-24 |
| 4 | [Show HN: ReLaXed – High-quality PDFs using web technologies](https://news.ycombinator.com/item?id=16959550) | ReLaXed 使用 Web 技术制作高质量 PDF 文档。 | 344 | 79 | 2018-04-30 |
| 5 | [Show HN: Giving a Broken Barcode Scanner a New Life with Elixir and Nerves](https://news.ycombinator.com/item?id=16902628) | 用 Elixir 和 Nerves 改造坏掉的条码扫描器，让旧设备重新派上用场。 | 330 | 58 | 2018-04-23 |
| 6 | [Show HN: AI Grant – Get $2,500 for your AI project in minutes](https://news.ycombinator.com/item?id=16760736) | AI Grant 介绍无附加条件的 AI 项目资助，希望快速提供 2,500 美元支持。 | 323 | 173 | 2018-04-05 |
| 7 | [Show HN: Wey – A fast, open-source Slack desktop app](https://news.ycombinator.com/item?id=16792638) | Wey 提供开源 Slack 桌面客户端，作者强调运行速度。 | 277 | 177 | 2018-04-09 |
| 8 | [Show HN: A site that lets you search and subscribe to “Who is hiring?”](https://news.ycombinator.com/item?id=16743030) | 搜索并订阅 HN 的“Who is hiring?”招聘信息，持续跟进新机会。 | 255 | 43 | 2018-04-03 |
| 9 | [Show HN: A curated library of free music for content creators](https://news.ycombinator.com/item?id=16884979) | 为内容创作者整理免费音乐库，便于寻找合适的作品配乐。 | 239 | 40 | 2018-04-20 |
| 10 | [Show HN: Travel spontaneously on a budget](https://news.ycombinator.com/item?id=16742492) | 围绕预算安排临时旅行，探索说走就走的低成本选择。 | 238 | 141 | 2018-04-03 |

### 2018-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Wired-elements – UI web components with a hand drawn, sketchy look](https://news.ycombinator.com/item?id=17146451) | Wired-elements 提供手绘草图风格的 Web 界面组件。 | 650 | 120 | 2018-05-24 |
| 2 | [Show HN: Cost of a 51% Attack on Popular Cryptocurrencies](https://news.ycombinator.com/item?id=17173051) | 估算主流加密货币遭遇 51% 攻击的成本。 | 581 | 218 | 2018-05-28 |
| 3 | [Show HN: The Curious Expedition – A Steam game in HTML5](https://news.ycombinator.com/item?id=17080985) | 《The Curious Expedition》展示用 HTML5 制作的 Steam 游戏。 | 458 | 141 | 2018-05-16 |
| 4 | [Show HN: Whiteboardfree – Developer Jobs at Companies That Don't Whiteboard](https://news.ycombinator.com/item?id=17101046) | Whiteboardfree 汇集不采用白板面试的公司及开发岗位。 | 396 | 349 | 2018-05-18 |
| 5 | [Show HN: How to Tune a Guitar](https://news.ycombinator.com/item?id=17015043) | 一个讲解吉他调音的项目，帮助把琴弦调到合适音高。 | 338 | 119 | 2018-05-07 |
| 6 | [Show HN: HyperApp – 1k JavaScript framework for building web applications](https://news.ycombinator.com/item?id=17126670) | HyperApp 用约 1KB 的 JavaScript 框架构建 Web 应用。 | 303 | 162 | 2018-05-22 |
| 7 | [Show HN: Cannoli – A compiler for a subset of Python written in Rust](https://news.ycombinator.com/item?id=17093051) | Cannoli 用 Rust 实现编译器，支持 Python 的一部分语法。 | 292 | 94 | 2018-05-17 |
| 8 | [Show HN: Parabola.io – Automate your work with visual programming](https://news.ycombinator.com/item?id=17147272) | Parabola 用拖拽搭建数据处理流程，让日常数据工作可以自动执行。 | 291 | 66 | 2018-05-24 |
| 9 | [Show HN: Write every day, measure your progress, achieve your writing goals](https://news.ycombinator.com/item?id=17189652) | 每天写作并记录进展，用可见的积累推动写作目标。 | 262 | 79 | 2018-05-30 |
| 10 | [Show HN: Recursive Recipes – directions to make food from scratch](https://news.ycombinator.com/item?id=17180686) | Recursive Recipes 递归拆解食谱，追溯从原料开始做饭的步骤。 | 250 | 75 | 2018-05-29 |

### 2018-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Open Logos – Free logos for open source projects](https://news.ycombinator.com/item?id=17344419) | Open Logos 为开源项目提供免费标志。 | 680 | 108 | 2018-06-19 |
| 2 | [Show HN: Why Do I Procrastinate? –  Web MD for Procrastination](https://news.ycombinator.com/item?id=17365150) | 以类似症状查询的方式探讨拖延，帮助用户追问自己为何迟迟不动手。 | 611 | 192 | 2018-06-21 |
| 3 | [Show HN: Material Dashboard – Free Admin for Bootstrap 4, React, Angular, Vue.js](https://news.ycombinator.com/item?id=17373465) | Material Dashboard 为多种前端技术提供免费的管理后台界面。 | 436 | 150 | 2018-06-22 |
| 4 | [Show HN: Plot modern addresses on Earth 240M years ago](https://news.ycombinator.com/item?id=17286770) | 把今天的地址标到 2.4 亿年前的地球，看看大陆移动前的位置。 | 384 | 59 | 2018-06-11 |
| 5 | [Show HN: Google Drive as a file system](https://news.ycombinator.com/item?id=17430397) | 将 Google Drive 用作文件系统，探索云文件的访问方式。 | 374 | 84 | 2018-06-30 |
| 6 | [Show HN: B2blaze – A Backblaze B2 library for Python](https://news.ycombinator.com/item?id=17405722) | B2blaze 为 Python 提供 Backblaze B2 存储库。 | 359 | 224 | 2018-06-27 |
| 7 | [Show HN: Mimicking the Bloomberg menu widget without JavaScript](https://news.ycombinator.com/item?id=17400164) | 不用 JavaScript 复刻 Bloomberg 菜单组件，展示网页交互实验。 | 355 | 132 | 2018-06-26 |
| 8 | [Show HN: BitHubLab, Search for projects on all the major Git platforms](https://news.ycombinator.com/item?id=17226225) | BitHubLab 跨多个主流 Git 平台搜索项目。 | 318 | 46 | 2018-06-04 |
| 9 | [Show HN: Interactive guitar scales diagrams](https://news.ycombinator.com/item?id=17272516) | 通过交互图表学习吉他音阶，直观看指板上的音符分布。 | 277 | 95 | 2018-06-09 |
| 10 | [Show HN: The Vue.js Handbook – Free 120 pages ebook](https://news.ycombinator.com/item?id=17398506) | 免费 120 页《Vue.js Handbook》，为 Vue 学习者整理入门知识。 | 262 | 64 | 2018-06-26 |

### 2018-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Browsh – A modern, text-based browser](https://news.ycombinator.com/item?id=17487552) | Browsh 是一款面向现代网页的文字浏览器。 | 967 | 322 | 2018-07-09 |
| 2 | [Show HN: Termtosvg – Record terminal sessions as SVG animations](https://news.ycombinator.com/item?id=17449810) | Termtosvg 把终端操作录成 SVG 动画，方便展示命令行过程。 | 767 | 79 | 2018-07-03 |
| 3 | [Show HN: Router7 – A pure-Go implementation of a small home internet router](https://news.ycombinator.com/item?id=17530086) | Router7 用纯 Go 实现小型家用互联网路由器。 | 461 | 102 | 2018-07-14 |
| 4 | [Show HN: Layoutit – An interactive CSS Grid generator](https://news.ycombinator.com/item?id=17618059) | Layoutit 通过交互操作生成 CSS Grid 布局。 | 437 | 71 | 2018-07-26 |
| 5 | [Show HN: Hasura – Fast, instant GraphQL APIs on Postgres](https://news.ycombinator.com/item?id=17540263) | Hasura 为 PostgreSQL 即时生成 GraphQL API。 | 382 | 103 | 2018-07-16 |
| 6 | [Show HN: Hacker News job trends](https://news.ycombinator.com/item?id=17470037) | 追踪 Hacker News 招聘趋势，从岗位信息观察技术就业变化。 | 371 | 92 | 2018-07-06 |
| 7 | [Show HN: Learn how to work remotely from people doing it every day](https://news.ycombinator.com/item?id=17569294) | 向每天远程工作的人学习经验，了解这种工作方式的实际安排。 | 343 | 76 | 2018-07-19 |
| 8 | [Show HN: Checklist of over 100 directories to submit your startup](https://news.ycombinator.com/item?id=17591677) | 整理一百多个可提交创业项目的目录，帮助新产品寻找曝光入口。 | 323 | 67 | 2018-07-23 |
| 9 | [Show HN: Make a business model canvas in your browser](https://news.ycombinator.com/item?id=17652593) | 直接在浏览器里绘制商业模式画布，梳理创业项目的关键假设。 | 295 | 76 | 2018-07-31 |
| 10 | [Show HN: Percy – A Rust and WebAssembly isomorphic virtual DOM implementation](https://news.ycombinator.com/item?id=17616839) | Percy 用 Rust 与 WebAssembly 实现同构虚拟 DOM。 | 234 | 50 | 2018-07-26 |

### 2018-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I'm 12, learning JS, and wrote Wolfram's cellular automaton in Node](https://news.ycombinator.com/item?id=17871313) | 一位十二岁的 JavaScript 学习者展示用 Node.js 编写的 Wolfram 元胞自动机。 | 1072 | 283 | 2018-08-29 |
| 2 | [Show HN: Pts.js – A library for visualization and creative coding](https://news.ycombinator.com/item?id=17716542) | Pts.js 为可视化与创意编程提供基础库。 | 611 | 71 | 2018-08-08 |
| 3 | [Show HN: Retool – build internal tools faster](https://news.ycombinator.com/item?id=17725966) | Retool 希望加快内部工具开发，减少团队自建业务界面的时间。 | 592 | 109 | 2018-08-09 |
| 4 | [Show HN: I made a tool that made me faster at Git](https://news.ycombinator.com/item?id=17689014) | 作者制作 Git 辅助工具，分享如何让自己的版本控制操作更快。 | 551 | 229 | 2018-08-05 |
| 5 | [Show HN: Ultralight – Lightweight, Pure-GPU HTML UI Renderer for C++](https://news.ycombinator.com/item?id=17733515) | Ultralight 为 C++ 提供轻量 HTML 界面渲染器，采用纯 GPU 路径。 | 527 | 170 | 2018-08-10 |
| 6 | [Show HN: A map that shows you how far you can go for a given time or distance](https://news.ycombinator.com/item?id=17679148) | 输入时间或距离限制，在地图上查看自己能到达的范围。 | 455 | 166 | 2018-08-03 |
| 7 | [Show HN: git-bug – Distributed bug tracker embedded in git](https://news.ycombinator.com/item?id=17782121) | git-bug 把分布式缺陷追踪嵌入 Git 仓库。 | 447 | 94 | 2018-08-17 |
| 8 | [Show HN: Proven – An alternative to Twitter's verified accounts, with HN support](https://news.ycombinator.com/item?id=17885908) | Proven 提供社交账号验证方案，并支持 Hacker News 身份。 | 334 | 75 | 2018-08-31 |
| 9 | [Show HN: Wayland compositor in around 500 lines of annotated C](https://news.ycombinator.com/item?id=17773982) | 约五百行带注释的 C 代码，实现一个 Wayland 合成器。 | 332 | 122 | 2018-08-16 |
| 10 | [Show HN: Didyougogo – An Altavista slayer](https://news.ycombinator.com/item?id=17744073) | Didyougogo 以“Altavista 杀手”为定位，展示搜索项目。 | 269 | 124 | 2018-08-12 |

### 2018-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I made a privacy-first minimalist Google Analytics](https://news.ycombinator.com/item?id=18024277) | 作者展示一款注重隐私、设计精简的网站统计工具。 | 968 | 263 | 2018-09-19 |
| 2 | [Show HN: Sublime Merge – A Git client from the makers of Sublime Text](https://news.ycombinator.com/item?id=18030446) | Sublime Text 团队推出 Git 客户端 Sublime Merge。 | 935 | 351 | 2018-09-20 |
| 3 | [Show HN: Select Star SQL, an interactive SQL book](https://news.ycombinator.com/item?id=17905666) | 《Select Star SQL》用交互形式教 SQL，让读者直接练习查询。 | 700 | 112 | 2018-09-04 |
| 4 | [Show HN: Lunar lander-type game with computational fluid dynamics](https://news.ycombinator.com/item?id=17993933) | 把计算流体力学加入月球着陆类游戏，体验不同的物理模拟。 | 660 | 127 | 2018-09-15 |
| 5 | [Show HN: Guitar Dashboard – Open source music theory explorer for guitarists](https://news.ycombinator.com/item?id=17987657) | Guitar Dashboard 为吉他手提供开源乐理探索工具。 | 590 | 115 | 2018-09-14 |
| 6 | [Show HN: TechYaks – Best of 50k tech talks ranked by confidence intervals](https://news.ycombinator.com/item?id=17988464) | TechYaks 用置信区间为五万场技术演讲排序，帮助挑选内容。 | 514 | 62 | 2018-09-14 |
| 7 | [Show HN: Hacking slot machines with a buttonhole camera and brute-force search](https://news.ycombinator.com/item?id=18035283) | 作者用纽扣摄像头与暴力搜索研究老虎机，展示技术破解实验。 | 421 | 151 | 2018-09-20 |
| 8 | [Show HN: Magic Sandbox – learn Kubernetes on real infrastructure](https://news.ycombinator.com/item?id=17909594) | Magic Sandbox 在真实基础设施上教授 Kubernetes。 | 392 | 89 | 2018-09-04 |
| 9 | [Show HN: Py-spy – A new sampling profiler for Python programs](https://news.ycombinator.com/item?id=17927200) | Py-spy 为 Python 程序提供采样性能分析工具。 | 286 | 43 | 2018-09-06 |
| 10 | [Show HN: Hacklily – sheet music editor](https://news.ycombinator.com/item?id=17952355) | Hacklily 提供乐谱编辑器，面向乐谱书写与修改。 | 285 | 49 | 2018-09-10 |

### 2018-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Websites in 2018](https://news.ycombinator.com/item?id=18284910) | 以“2018 年的网站”为主题，作者展示自己的网页项目。 | 595 | 192 | 2018-10-23 |
| 2 | [Show HN: Ultimate Plumber – a tool for writing Linux pipes with live preview](https://news.ycombinator.com/item?id=18291302) | Ultimate Plumber 为 Linux 管道命令提供实时预览，边写边看输出。 | 484 | 217 | 2018-10-24 |
| 3 | [Show HN: Alan – a low-code application platform](https://news.ycombinator.com/item?id=18166538) | Alan 展示低代码应用平台，探索更省代码的开发方式。 | 413 | 173 | 2018-10-08 |
| 4 | [Show HN: Polar – an offline web browser with annotations and tagging](https://news.ycombinator.com/item?id=18219960) | Polar 提供支持批注和标签的离线网页阅读工具。 | 382 | 69 | 2018-10-15 |
| 5 | [Show HN: Tableau-Like Data Visualizations in JavaScript](https://news.ycombinator.com/item?id=18193264) | 用 JavaScript 实现类似 Tableau 的数据可视化体验。 | 361 | 114 | 2018-10-11 |
| 6 | [Show HN: Comprehensive Tutorials in Deep Learning Using TensorFlow](https://news.ycombinator.com/item?id=18211251) | 一套基于 TensorFlow 的深度学习教程，系统整理学习内容。 | 327 | 6 | 2018-10-14 |
| 7 | [Show HN: Algojammer – an experimental Python code editor inspired by Bret Victor](https://news.ycombinator.com/item?id=18321709) | Algojammer 受 Bret Victor 启发，探索实验性的 Python 代码编辑方式。 | 309 | 34 | 2018-10-28 |
| 8 | [Show HN: Applying for jobs? Manage all your interviews in one place](https://news.ycombinator.com/item?id=18258971) | 把求职中的面试集中管理，方便跟进多家公司和流程。 | 306 | 126 | 2018-10-19 |
| 9 | [Show HN: SQL Trainer – Learn SQL by doing live data exercises](https://news.ycombinator.com/item?id=18335723) | SQL Trainer 用实时数据练习帮助学习 SQL。 | 303 | 49 | 2018-10-30 |
| 10 | [Show HN: Physically Based Rendering – Online Edition](https://news.ycombinator.com/item?id=18219296) | 《Physically Based Rendering》推出在线版，方便阅读渲染技术内容。 | 297 | 42 | 2018-10-15 |

### 2018-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: TabNine, an autocompleter for all languages](https://news.ycombinator.com/item?id=18393364) | TabNine 展示面向各种编程语言的代码自动补全工具。 | 607 | 188 | 2018-11-06 |
| 2 | [Show HN: Open-sourcing my wedding website on my first anniversary](https://news.ycombinator.com/item?id=18556787) | 在结婚一周年时开源婚礼网站，分享自己为纪念日制作的代码。 | 436 | 190 | 2018-11-28 |
| 3 | [Show HN: WriteFreely – minimalist, federated blogging platform](https://news.ycombinator.com/item?id=18432327) | WriteFreely 提供简洁、支持联邦互联的博客平台。 | 337 | 112 | 2018-11-12 |
| 4 | [Show HN: Self-Driving Pi Car](https://news.ycombinator.com/item?id=18487327) | 用树莓派制作自动驾驶小车，展示动手搭建成果。 | 304 | 42 | 2018-11-19 |
| 5 | [Show HN: Don't code your UI, draw it](https://news.ycombinator.com/item?id=18480115) | 通过画图生成界面，作者尝试改变用代码编写 UI 的方式。 | 302 | 141 | 2018-11-18 |
| 6 | [Show HN: Founders launching startups on Twitch](https://news.ycombinator.com/item?id=18476639) | 创始人在 Twitch 直播推出创业项目，让创业过程公开进行。 | 265 | 116 | 2018-11-17 |
| 7 | [Show HN: Shortcut Roulette – Dangerous, unhelpful shortcut for iOS 12](https://news.ycombinator.com/item?id=18492899) | Shortcut Roulette 为 iOS 12 制作“危险又无用”的趣味快捷指令。 | 253 | 61 | 2018-11-20 |
| 8 | [Show HN: A JavaScript Handbook](https://news.ycombinator.com/item?id=18432436) | 一本 JavaScript 手册，整理语言学习与使用知识。 | 239 | 61 | 2018-11-12 |
| 9 | [Show HN: HomelabOS – Ansible scripts to deploy self hosted cloud services](https://news.ycombinator.com/item?id=18434472) | HomelabOS 用 Ansible 脚本部署可自行托管的云服务。 | 235 | 78 | 2018-11-12 |
| 10 | [Show HN: Gmail Classic – CSS for Reverting Gmail's New Look](https://news.ycombinator.com/item?id=18475527) | Gmail Classic 通过 CSS 把新版 Gmail 外观改回经典样式。 | 226 | 179 | 2018-11-17 |

### 2018-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Fully-automatic image background removal tool](https://news.ycombinator.com/item?id=18697601) | 全自动移除图片背景，简化抠图和素材制作。 | 640 | 108 | 2018-12-17 |
| 2 | [Show HN: Visalist – Find visa requirements for countries around the world](https://news.ycombinator.com/item?id=18640880) | Visalist 帮用户查询世界各国的签证要求。 | 565 | 252 | 2018-12-09 |
| 3 | [Show HN: Dark Reader extension – Dark mode for every website](https://news.ycombinator.com/item?id=18599200) | Dark Reader 为各类网站加入深色模式。 | 369 | 175 | 2018-12-04 |
| 4 | [Show HN: Open source JavaScript library to record and replay the web](https://news.ycombinator.com/item?id=18776496) | 开源 JavaScript 库记录并重放网页操作，复现页面使用过程。 | 353 | 51 | 2018-12-28 |
| 5 | [Show HN: A new spline](https://news.ycombinator.com/item?id=18738275) | 一种新的样条曲线方案，展示曲线构造与控制的探索。 | 341 | 72 | 2018-12-22 |
| 6 | [Show HN: Analysis of 2018 Hacker News “Who Is Hiring” Job Posts](https://news.ycombinator.com/item?id=18725425) | 分析 2018 年 HN 招聘帖，从岗位数据观察招聘情况。 | 301 | 186 | 2018-12-20 |
| 7 | [Show HN: Cross-platform open-source 3D modeling software](https://news.ycombinator.com/item?id=18576117) | 一款支持跨平台使用的开源三维建模软件，面向不同系统中的创作需求。 | 290 | 86 | 2018-12-01 |
| 8 | [Show HN: Stock Trading from Google Spreadsheet](https://news.ycombinator.com/item?id=18606766) | 通过 Google 表格脚本调用交易 API，在电子表格里管理股票交易。 | 281 | 84 | 2018-12-05 |
| 9 | [Show HN: Vector Logo Zone – SVG logos for your readme or credits page](https://news.ycombinator.com/item?id=18789268) | Vector Logo Zone 提供 SVG 标志，方便用于项目说明与致谢页面。 | 275 | 47 | 2018-12-30 |
| 10 | [Show HN: Wiv.js – A library for a more wiggly div](https://news.ycombinator.com/item?id=18755782) | Wiv.js 让 div 扭动起来，给普通网页元素加入趣味动效。 | 265 | 55 | 2018-12-25 |

### 2019-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I taught my little brother JS, and he made this videogame in a week](https://news.ycombinator.com/item?id=18866500) | 作者教弟弟学习 JavaScript 后，展示他一周内制作的电子游戏。 | 1079 | 270 | 2019-01-09 |
| 2 | [Show HN: Mkcert – Valid HTTPS certificates for localhost](https://news.ycombinator.com/item?id=18842218) | Mkcert 为 localhost 生成有效 HTTPS 证书，方便本地开发。 | 839 | 115 | 2019-01-07 |
| 3 | [Show HN: HN.Academy – Top online courses recommended by Hacker News users](https://news.ycombinator.com/item?id=18816418) | HN.Academy 汇集 Hacker News 用户推荐的在线课程。 | 773 | 85 | 2019-01-03 |
| 4 | [Show HN: Open startups with their revenue, metrics, and stories](https://news.ycombinator.com/item?id=19025560) | 展示公开收入、指标和故事的创业项目，观察业务的真实进展。 | 475 | 82 | 2019-01-29 |
| 5 | [Show HN: Top PDFs Posted to Hacker News in 2018](https://news.ycombinator.com/item?id=18865543) | 整理 2018 年登上 Hacker News 的热门 PDF，回看值得阅读的资料。 | 411 | 41 | 2019-01-09 |
| 6 | [Show HN: A tool to find related subreddits](https://news.ycombinator.com/item?id=18866800) | 通过工具发现相关 subreddit，拓展感兴趣主题的社区。 | 398 | 81 | 2019-01-09 |
| 7 | [Show HN: HeyFromTheFuture – Advice people wish they had at your age](https://news.ycombinator.com/item?id=18902561) | HeyFromTheFuture 收集人们希望当年知道的建议，按年龄寻找经验。 | 355 | 167 | 2019-01-14 |
| 8 | [Show HN: X-spreadsheet – A JavaScript canvas spreadsheet for web](https://news.ycombinator.com/item?id=19017270) | X-spreadsheet 用 JavaScript Canvas 实现网页电子表格。 | 347 | 105 | 2019-01-28 |
| 9 | [Show HN: Trilium Notes – Scriptable note-taking application](https://news.ycombinator.com/item?id=18840990) | Trilium Notes 提供可通过脚本扩展的笔记应用。 | 328 | 124 | 2019-01-06 |
| 10 | [Show HN: Learn and practice modern JavaScript](https://news.ycombinator.com/item?id=18814416) | 学习并练习现代 JavaScript，把知识落实到代码中。 | 305 | 105 | 2019-01-03 |

### 2019-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Make your site’s pages instant in one minute](https://news.ycombinator.com/item?id=19122727) | 展示一款声称只需一分钟部署，就能让网站页面更快响应的工具。 | 1214 | 337 | 2019-02-09 |
| 2 | [Show HN: Automatically synchronize subtitles with video](https://news.ycombinator.com/item?id=19248723) | 自动对齐字幕和视频，解决字幕时间不同步的问题。 | 583 | 124 | 2019-02-25 |
| 3 | [Show HN: Zero – A fast, zero-configuration server for React, Node.js, Markdown](https://news.ycombinator.com/item?id=19254828) | Zero 为 React、Node.js 与 Markdown 提供零配置服务器。 | 513 | 245 | 2019-02-26 |
| 4 | [Show HN: Learn React fundamentals](https://news.ycombinator.com/item?id=19050509) | 围绕 React 基础概念建立学习项目，帮助入门组件开发。 | 509 | 74 | 2019-02-01 |
| 5 | [Show HN: I wrote a book about WebAssembly](https://news.ycombinator.com/item?id=19274941) | 作者介绍自己写的 WebAssembly 实践书，希望降低学习门槛。 | 410 | 88 | 2019-02-28 |
| 6 | [Show HN: Quickly browse the history of any GitHub file](https://news.ycombinator.com/item?id=19113635) | 快速浏览 GitHub 文件的历史，追踪单个文件如何演变。 | 407 | 76 | 2019-02-08 |
| 7 | [Show HN: Learn C and its lower levels interactively, in the browser](https://news.ycombinator.com/item?id=19126544) | 在浏览器里运行 C 虚拟机，把语言学习与底层机制一起展示。 | 356 | 33 | 2019-02-10 |
| 8 | [Show HN: GuiLite – Tiny UI framework, runs on MCU without OS](https://news.ycombinator.com/item?id=19051914) | GuiLite 提供小型 UI 框架，可在没有操作系统的微控制器上运行。 | 355 | 48 | 2019-02-01 |
| 9 | [Show HN: DeskGap – Like Electron, but uses the system webview](https://news.ycombinator.com/item?id=19149690) | DeskGap 借鉴 Electron 的桌面开发方式，使用系统自带 WebView。 | 318 | 260 | 2019-02-13 |
| 10 | [Show HN: Open source balloon simulation with Three.js](https://news.ycombinator.com/item?id=19141119) | 用 Three.js 制作开源气球模拟，展示浏览器里的物理与图形实验。 | 307 | 56 | 2019-02-12 |

### 2019-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: A retro video game console I've been working on in my free time](https://news.ycombinator.com/item?id=19393279) | 作者展示自己利用业余时间制作的复古游戏主机。 | 2690 | 210 | 2019-03-14 |
| 2 | [Show HN: A Color Picker I Made](https://news.ycombinator.com/item?id=19455441) | 作者展示自己制作的取色器，帮助在界面中挑选颜色。 | 591 | 106 | 2019-03-21 |
| 3 | [Show HN: A browser extension which blocks chat/helpdesk widgets](https://news.ycombinator.com/item?id=19408329) | 浏览器扩展屏蔽客服与帮助聊天挂件，减少浏览时的浮动干扰。 | 510 | 226 | 2019-03-16 |
| 4 | [Show HN: Everything I Know Wiki](https://news.ycombinator.com/item?id=19468993) | 作者把自己知道的内容整理成维基，展示个人知识积累。 | 434 | 119 | 2019-03-23 |
| 5 | [Show HN: Baxx – Unix-friendly backup service](https://news.ycombinator.com/item?id=19482280) | Baxx 提供贴近 Unix 使用习惯的备份服务。 | 424 | 198 | 2019-03-25 |
| 6 | [Show HN: Editable, royalty-free SVG illustrations](https://news.ycombinator.com/item?id=19474853) | 可编辑、无需版税的 SVG 插画，方便融入不同设计。 | 295 | 43 | 2019-03-24 |
| 7 | [Show HN: A raycaster that renders to random dot stereogram (like Magic Eye)](https://news.ycombinator.com/item?id=19454962) | 光线投射器输出随机点立体图，重现“魔眼”式的观看效果。 | 277 | 88 | 2019-03-21 |
| 8 | [Show HN: This Question Does Not Exist](https://news.ycombinator.com/item?id=19386093) | “This Question Does Not Exist”项目亮相，围绕不存在的问题做实验。 | 274 | 141 | 2019-03-14 |
| 9 | [Show HN: My CV is also a bootloader](https://news.ycombinator.com/item?id=19344146) | 作者把简历做成引导程序，展示能启动的个人履历。 | 255 | 50 | 2019-03-09 |
| 10 | [Show HN: Freeciv-Web](https://news.ycombinator.com/item?id=19350421) | Freeciv-Web 项目展示，把文明策略游戏带到网页环境。 | 212 | 24 | 2019-03-10 |

### 2019-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Lorem Picsum – Lorem Ipsum but for photos](https://news.ycombinator.com/item?id=19774019) | Lorem Picsum 为图片提供类似占位文字的便利，快速填充设计稿。 | 880 | 123 | 2019-04-28 |
| 2 | [Show HN: 1MB – Free and easy static website hosting and database](https://news.ycombinator.com/item?id=19772097) | 1MB 提供免费的静态网站托管与数据库，主打简单使用。 | 744 | 239 | 2019-04-28 |
| 3 | [Show HN: I made a platform for journalists to “open source” their fact checking](https://news.ycombinator.com/item?id=19572514) | 作者为记者制作平台，让事实核查过程可以像代码一样公开。 | 593 | 298 | 2019-04-04 |
| 4 | [Show HN: Water.css – A just-add-css collection of styles to make websites nicer](https://news.ycombinator.com/item?id=19593866) | Water.css 只需引入样式表，就能改善普通网页的外观。 | 501 | 104 | 2019-04-07 |
| 5 | [Show HN: Tree of Reddit Sex Life](https://news.ycombinator.com/item?id=19640562) | 作者以树形结构展示 Reddit 上与性生活相关的内容。 | 494 | 119 | 2019-04-12 |
| 6 | [Show HN: CC Search – search engine for 300M CC-licensed images](https://news.ycombinator.com/item?id=19791073) | CC Search 帮用户搜索三亿张采用知识共享许可的图片。 | 375 | 87 | 2019-04-30 |
| 7 | [Show HN: Should you buy a house and rent it out?](https://news.ycombinator.com/item?id=19704418) | 围绕该不该买房出租，作者提供项目辅助思考这项投资选择。 | 353 | 243 | 2019-04-20 |
| 8 | [Show HN: Thoughter](https://news.ycombinator.com/item?id=19567073) | Thoughter 项目展示，邀请社区查看作者的创作尝试。 | 312 | 156 | 2019-04-03 |
| 9 | [Show HN: Sauron – A web framework in Rust that adheres to the Elm architecture](https://news.ycombinator.com/item?id=19756505) | Sauron 用 Rust 构建 Web 框架，遵循 Elm 架构思路。 | 305 | 97 | 2019-04-26 |
| 10 | [Show HN: Ethical Resources – 300 ethical alternatives to mainstream stuff](https://news.ycombinator.com/item?id=19613477) | Ethical Resources 整理三百种主流产品的伦理替代选择。 | 291 | 129 | 2019-04-09 |

### 2019-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: CSSFX – Click-to-copy CSS effects](https://news.ycombinator.com/item?id=19858015) | CSSFX 展示可点击复制的 CSS 动效，方便直接用于网页。 | 595 | 87 | 2019-05-08 |
| 2 | [Show HN: 30 Hour Jobs – a job board for shorter work weeks](https://news.ycombinator.com/item?id=19910691) | 30 Hour Jobs 汇集工时较短的岗位，为缩短工作周寻找机会。 | 558 | 137 | 2019-05-14 |
| 3 | [Show HN: Switch from Medium to your own blog](https://news.ycombinator.com/item?id=20060549) | 帮助从 Medium 迁移到自己的博客，重新掌握内容发布空间。 | 494 | 130 | 2019-05-31 |
| 4 | [Show HN: I replaced Google Analytics with simple log-based analytics](https://news.ycombinator.com/item?id=19883876) | 作者以简单的日志分析替代 Google Analytics，分享网站统计实践。 | 475 | 137 | 2019-05-11 |
| 5 | [Show HN: ZFS Implementation in Python](https://news.ycombinator.com/item?id=19827336) | 用 Python 实现 ZFS，探索文件系统的代码表达。 | 411 | 86 | 2019-05-04 |
| 6 | [Show HN: Turn an Excel file into a web application](https://news.ycombinator.com/item?id=19968271) | 把 Excel 文件变成 Web 应用，延伸电子表格的使用场景。 | 386 | 175 | 2019-05-21 |
| 7 | [Show HN: nextdns.io – A Combination of Cloudflare DNS and Pi-Hole](https://news.ycombinator.com/item?id=20012687) | NextDNS 结合 Cloudflare DNS 与 Pi-hole 的思路提供 DNS 服务。 | 372 | 146 | 2019-05-26 |
| 8 | [Show HN: Scar – Static websites with HTTPS, a global CDN, and custom domains](https://news.ycombinator.com/item?id=19981869) | Scar 为静态网站提供 HTTPS、全球 CDN 与自定义域名。 | 363 | 170 | 2019-05-22 |
| 9 | [Show HN: Python Machine Learning – A Crash Course](https://news.ycombinator.com/item?id=19886754) | 用速成课程介绍 Python 机器学习，帮助快速接触基本方法。 | 350 | 20 | 2019-05-11 |
| 10 | [Show HN: Risp – Lisp in Rust](https://news.ycombinator.com/item?id=19810504) | Risp 用 Rust 实现 Lisp，展示语言解释器实验。 | 314 | 84 | 2019-05-02 |

### 2019-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Bloom – A free and open source 'Google'](https://news.ycombinator.com/item?id=20105567) | Bloom 以免费开源的“Google”为目标，展示搜索相关项目。 | 747 | 230 | 2019-06-05 |
| 2 | [Show HN: This page is a truly naked, brutalist HTML quine](https://news.ycombinator.com/item?id=20094866) | 一个极简 HTML 自复制页面，页面本身也是自己的源代码表达。 | 633 | 94 | 2019-06-04 |
| 3 | [Show HN: A job board for companies fighting ageism in tech](https://news.ycombinator.com/item?id=20252097) | 为对抗科技行业年龄歧视的公司建立招聘板。 | 523 | 291 | 2019-06-22 |
| 4 | [Show HN: ZeroHTTPd: A web server to teach Linux performance, with benchmarks](https://news.ycombinator.com/item?id=20081488) | ZeroHTTPd 用 Web 服务器与基准测试讲解 Linux 性能。 | 472 | 57 | 2019-06-03 |
| 5 | [Show HN: Enviro+ for Raspberry Pi – Environmental sensors](https://news.ycombinator.com/item?id=20185182) | Enviro+ 为树莓派提供环境传感器，采集周边环境数据。 | 397 | 82 | 2019-06-14 |
| 6 | [Show HN: Slim – Build and run tiny VMs from Dockerfiles](https://news.ycombinator.com/item?id=20182141) | Slim 从 Dockerfile 构建并运行小型虚拟机。 | 389 | 139 | 2019-06-14 |
| 7 | [Show HN: Catj – A new way to display JSON files](https://news.ycombinator.com/item?id=20245913) | Catj 展示一种新的 JSON 文件呈现方式。 | 388 | 120 | 2019-06-21 |
| 8 | [Show HN: Web pages stored entirely in the URL](https://news.ycombinator.com/item?id=20317840) | 把整个网页存进 URL，让链接本身携带页面内容。 | 377 | 163 | 2019-06-30 |
| 9 | [Show HN: Openring, a free and decentralized network of blogs](https://news.ycombinator.com/item?id=20191603) | Openring 连接博客，尝试构建自由、去中心化的博客网络。 | 351 | 95 | 2019-06-15 |
| 10 | [Show HN: Rga: ripgrep, but also search in PDFs, Office documents, zip, tar.gz](https://news.ycombinator.com/item?id=20196982) | Rga 扩展 ripgrep 的搜索范围，涵盖 PDF、Office 文档和压缩包。 | 284 | 65 | 2019-06-16 |

### 2019-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I built a service to discover rapidly  growing Google search topics](https://news.ycombinator.com/item?id=20478339) | 作者制作服务，帮助发现 Google 搜索中快速增长的话题。 | 446 | 116 | 2019-07-19 |
| 2 | [Show HN: Ananas – a hackable data tool for beginners](https://news.ycombinator.com/item?id=20498474) | Ananas 为初学者提供可修改、可扩展的数据工具。 | 359 | 104 | 2019-07-22 |
| 3 | [Show HN: Listmonk – Fast self-hosted newsletter and mailing list manager](https://news.ycombinator.com/item?id=20421243) | Listmonk 提供可自行托管的邮件通讯与邮件列表管理工具。 | 343 | 50 | 2019-07-12 |
| 4 | [Show HN: Vector – A High-Performance Log and Metric Router Written in Rust](https://news.ycombinator.com/item?id=20334779) | Vector 用 Rust 编写日志和指标路由器，作者主打高性能。 | 322 | 63 | 2019-07-02 |
| 5 | [Show HN: OctoSQL – Query and join multiple databases and files, written in Go](https://news.ycombinator.com/item?id=20449610) | OctoSQL 用 Go 实现跨数据库和文件的查询与关联。 | 310 | 70 | 2019-07-16 |
| 6 | [Show HN: Stein – Use Google Sheets as a No-Setup Database](https://news.ycombinator.com/item?id=20426682) | Stein 把 Google Sheets 当作免配置数据库使用。 | 296 | 65 | 2019-07-13 |
| 7 | [Show HN: Sauron-native – A native cross-platform GUI for Rust](https://news.ycombinator.com/item?id=20533318) | Sauron-native 为 Rust 提供原生跨平台图形界面方案。 | 255 | 97 | 2019-07-26 |
| 8 | [Show HN: Poli – An easy-to-use, open-source BI alternative](https://news.ycombinator.com/item?id=20507592) | Poli 提供易用的开源商业智能工具，作为现有 BI 产品的替代选择。 | 236 | 46 | 2019-07-23 |
| 9 | [Show HN: TLDR This – Auto summarize any article or webpage in a click](https://news.ycombinator.com/item?id=20546356) | TLDR This 尝试一键概括文章或网页，帮助快速了解内容。 | 235 | 114 | 2019-07-28 |
| 10 | [Show HN: Inlets 2.0 – expose your local endpoints to the Internet](https://news.ycombinator.com/item?id=20410552) | Inlets 2.0 将本地服务端点暴露到互联网，方便外部访问。 | 218 | 66 | 2019-07-11 |

### 2019-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: CLI tool for saving web pages as a single file](https://news.ycombinator.com/item?id=20774322) | 命令行工具把网页保存成单个文件，便于归档与携带。 | 640 | 209 | 2019-08-23 |
| 2 | [Show HN: Divjoy – React Codebase and UI Generator](https://news.ycombinator.com/item?id=20688044) | Divjoy 生成 React 界面与代码基础，简化应用起步工作。 | 511 | 131 | 2019-08-13 |
| 3 | [Show HN: Chart.xkcd – Xkcd-styled chart library](https://news.ycombinator.com/item?id=20734956) | Chart.xkcd 用 xkcd 漫画风格绘制图表。 | 435 | 41 | 2019-08-19 |
| 4 | [Show HN: I trained a deep learning model to build sites for me](https://news.ycombinator.com/item?id=20624140) | 作者训练深度学习模型，尝试让模型替自己构建网站。 | 397 | 124 | 2019-08-06 |
| 5 | [Show HN: Wave-based non-line-of-sight computational imaging in Julia](https://news.ycombinator.com/item?id=20813557) | 用 Julia 实现基于波的非视距计算成像，探索视线之外的图像重建。 | 375 | 71 | 2019-08-27 |
| 6 | [Show HN: Data Structures and Algorithms in JavaScript](https://news.ycombinator.com/item?id=20634409) | 通过 JavaScript 学习数据结构与算法。 | 369 | 40 | 2019-08-07 |
| 7 | [Show HN: Saag as a Service – macronutrient-portioned Indian spinach curry](https://news.ycombinator.com/item?id=20725311) | 把印度菠菜咖喱做成服务，并按宏量营养素划分份量。 | 303 | 169 | 2019-08-17 |
| 8 | [Show HN: ClojureScript pixel game engine with Blender live-reloading](https://news.ycombinator.com/item?id=20723366) | ClojureScript 像素游戏引擎支持 Blender 实时重载，连接建模与运行。 | 285 | 30 | 2019-08-17 |
| 9 | [Show HN: I created Postwoman, an online, open-source API request builder](https://news.ycombinator.com/item?id=20817627) | Postwoman 提供在线开源 API 请求构建器，方便调试接口。 | 280 | 100 | 2019-08-28 |
| 10 | [Show HN: I made a CRM system to make sales fun](https://news.ycombinator.com/item?id=20798003) | 作者制作 CRM 系统，希望让销售工作更有乐趣。 | 275 | 206 | 2019-08-26 |

### 2019-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: See a Satellite Tonight. No Telescope Required](https://news.ycombinator.com/item?id=21037167) | 不用望远镜也能观测卫星，工具帮助寻找今晚抬头观看的时机。 | 863 | 151 | 2019-09-21 |
| 2 | [Show HN: Cyberpunk web design made easy, really easy](https://news.ycombinator.com/item?id=20923792) | 让赛博朋克风网页设计更容易实现，作者展示相关工具。 | 775 | 108 | 2019-09-09 |
| 3 | [Show HN: Browse Reddit in 3D](https://news.ycombinator.com/item?id=20929801) | 把 Reddit 放进三维空间，尝试不同的社区浏览体验。 | 720 | 162 | 2019-09-10 |
| 4 | [Show HN: A Senior Engineer's CheckList](https://news.ycombinator.com/item?id=20914236) | 一位高级工程师分享自己的检查清单，供同行参考与调整。 | 662 | 143 | 2019-09-09 |
| 5 | [Show HN: I made a neural net that analyzes privacy policies](https://news.ycombinator.com/item?id=21042468) | 作者制作神经网络，尝试自动分析隐私政策。 | 502 | 120 | 2019-09-22 |
| 6 | [Show HN: Bot Land, a game where you fight others via code](https://news.ycombinator.com/item?id=21101918) | Bot Land 让玩家通过编写代码互相对战。 | 444 | 87 | 2019-09-28 |
| 7 | [Show HN: I built an online image editor using WebGL and CSS transforms](https://news.ycombinator.com/item?id=20982161) | 作者用 WebGL 与 CSS 变换构建在线图片编辑器。 | 425 | 72 | 2019-09-16 |
| 8 | [Show HN: I made a jobs board for developers without degrees](https://news.ycombinator.com/item?id=21005790) | 专门为没有学位的开发者建立招聘板，寻找不看学历的机会。 | 343 | 322 | 2019-09-18 |
| 9 | [Show HN: HTTP Mock – Intercept, debug and mock HTTP(S) with zero setup](https://news.ycombinator.com/item?id=21070934) | HTTP Mock 以免配置为目标，提供 HTTP 与 HTTPS 拦截、调试和模拟。 | 341 | 84 | 2019-09-25 |
| 10 | [Show HN: RemoteMore – We connect developers with full-time remote jobs](https://news.ycombinator.com/item?id=20971392) | RemoteMore 将开发者与全职远程职位连接起来。 | 334 | 147 | 2019-09-14 |

### 2019-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Bel](https://news.ycombinator.com/item?id=21231208) | 展示名为 Bel 的项目。 | 1288 | 456 | 2019-10-12 |
| 2 | [Show HN: Ledonardo, my light painting hardware project](https://news.ycombinator.com/item?id=21134903) | Ledonardo 是作者的光绘硬件项目，探索用光作画。 | 442 | 91 | 2019-10-02 |
| 3 | [Show HN: I had issues organizing my favorite recipes, so I built this](https://news.ycombinator.com/item?id=21175492) | 为整理喜欢的食谱，作者自己制作了一套工具。 | 422 | 168 | 2019-10-06 |
| 4 | [Show HN: Spider Pro – easy and cheap way to scrape the internet](https://news.ycombinator.com/item?id=21215484) | Spider Pro 提供网页抓取服务，作者强调简单与低成本。 | 391 | 103 | 2019-10-10 |
| 5 | [Show HN: pg_flame – flamegraph visualizations of PostgreSQL query plans](https://news.ycombinator.com/item?id=21371642) | pg_flame 把 PostgreSQL 查询计划变成火焰图，直观看执行结构。 | 321 | 42 | 2019-10-27 |
| 6 | [Show HN: Imagededup – Finding duplicate images made easy](https://news.ycombinator.com/item?id=21157463) | Imagededup 帮助查找重复图片，简化图库整理。 | 290 | 57 | 2019-10-04 |
| 7 | [Show HN: uPlot.js – An exceptionally fast, tiny time series chart](https://news.ycombinator.com/item?id=21207132) | uPlot.js 提供小体积时间序列图表，作者主打绘制速度。 | 260 | 81 | 2019-10-09 |
| 8 | [Show HN: Able – an alternative to Medium](https://news.ycombinator.com/item?id=21157066) | Able 展示内容发布平台，尝试成为 Medium 的替代选择。 | 248 | 134 | 2019-10-04 |
| 9 | [Show HN: Pipedream. Develop any workflow, on any trigger, with auth and no infra](https://news.ycombinator.com/item?id=21270424) | Pipedream 支持多种触发器与认证，希望免维护基础设施地搭建工作流。 | 245 | 107 | 2019-10-16 |
| 10 | [Show HN: My first game, minimal procgen gravity golf inspired by Desert Golfing](https://news.ycombinator.com/item?id=21136364) | 作者的首款游戏用程序生成关卡，以重力高尔夫玩法致敬 Desert Golfing。 | 232 | 113 | 2019-10-02 |

### 2019-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Open-Source Alternative to Intercom, Drift, Zendesk, FreshChat](https://news.ycombinator.com/item?id=21559139) | 一款开源客户沟通工具，尝试替代 Intercom 等客服产品。 | 417 | 79 | 2019-11-17 |
| 2 | [Show HN: Coscreen.co – a radically different remote collaboration tool](https://news.ycombinator.com/item?id=21639525) | Coscreen.co 探索远程协作工具的新交互方式。 | 404 | 184 | 2019-11-26 |
| 3 | [Show HN: DevShop, the Game of Kanban](https://news.ycombinator.com/item?id=21504023) | DevShop 将看板管理做成游戏，让玩家体验任务流转。 | 393 | 96 | 2019-11-11 |
| 4 | [Show HN: I made an open-source anonymous email forwarding service](https://news.ycombinator.com/item?id=21648096) | 作者制作开源匿名邮件转发服务，关注邮箱地址的隐藏与保护。 | 393 | 178 | 2019-11-27 |
| 5 | [Show HN: Hacker News Title Edit Tracker](https://news.ycombinator.com/item?id=21617016) | 追踪 Hacker News 标题编辑，查看标题如何被修改。 | 366 | 92 | 2019-11-23 |
| 6 | [Show HN: patchbay.pub – Poor man's ngrok/IFTTT/serverless](https://news.ycombinator.com/item?id=21639066) | patchbay.pub 用简易工具实现类似 ngrok、IFTTT 与无服务器的用途。 | 362 | 79 | 2019-11-26 |
| 7 | [Show HN: Turn any website into an API (for those who miss Kimono)](https://news.ycombinator.com/item?id=21417965) | 把网站转成 API，为怀念 Kimono 的用户提供新的工具选择。 | 332 | 74 | 2019-11-01 |
| 8 | [Show HN: Tailwind Builder – online editor for the Tailwind CSS framework](https://news.ycombinator.com/item?id=21439918) | Tailwind Builder 为 Tailwind CSS 提供在线编辑器。 | 295 | 43 | 2019-11-04 |
| 9 | [Show HN: Testing HN titles against a neural network](https://news.ycombinator.com/item?id=21522830) | 用神经网络测试 HN 标题，作者展示围绕标题的实验。 | 285 | 209 | 2019-11-13 |
| 10 | [Show HN: Virtual pet game made for my daughter](https://news.ycombinator.com/item?id=21594436) | 作者为女儿制作虚拟宠物游戏，分享家庭创作成果。 | 256 | 67 | 2019-11-21 |

### 2019-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Angeldust – a fast and efficient video game](https://news.ycombinator.com/item?id=21858226) | 独立开发多年的 Angeldust 结合动作 RPG 与建造，展示共享奇幻世界。 | 716 | 193 | 2019-12-22 |
| 2 | [Show HN: A searchable list of self-hosted software with screenshots](https://news.ycombinator.com/item?id=21712403) | 可搜索的自托管软件目录附有截图，便于直观比较工具。 | 656 | 112 | 2019-12-05 |
| 3 | [Show HN: A tiny isometric city builder in JavaScript](https://news.ycombinator.com/item?id=21923940) | 用 JavaScript 制作小型等距城市建造游戏。 | 593 | 104 | 2019-12-31 |
| 4 | [Show HN: AI Dungeon 2 – AI-generated text adventure built with 1.5B param GPT-2](https://news.ycombinator.com/item?id=21717022) | AI Dungeon 2 使用十五亿参数 GPT-2 生成文字冒险故事。 | 584 | 220 | 2019-12-05 |
| 5 | [Show HN: One Page Calendar 2020](https://news.ycombinator.com/item?id=21921165) | 把 2020 年日历放进一页，方便全年概览。 | 517 | 98 | 2019-12-31 |
| 6 | [Show HN: Space Invaders in C](https://news.ycombinator.com/item?id=21719575) | 用 C 编写《太空侵略者》，展示经典街机玩法实现。 | 478 | 105 | 2019-12-06 |
| 7 | [Show HN: Local Node.js app to save everything you browse and serve it offline](https://news.ycombinator.com/item?id=21855986) | 本地 Node.js 应用保存浏览过的内容，并在离线时继续提供访问。 | 406 | 97 | 2019-12-22 |
| 8 | [Show HN: Gameslab, a FPGA powered handheld game console](https://news.ycombinator.com/item?id=21874772) | Gameslab 是用 FPGA 驱动的掌上游戏机项目。 | 406 | 50 | 2019-12-24 |
| 9 | [Show HN: Eschersket.ch – a symmetry drawing app to design custom wrapping paper](https://news.ycombinator.com/item?id=21887848) | Eschersket.ch 通过对称绘画设计个性化包装纸。 | 386 | 27 | 2019-12-26 |
| 10 | [Show HN: Made this with my daughter to help kids ages 2 to 4 learn logic](https://news.ycombinator.com/item?id=21880446) | 作者与女儿共同制作项目，帮助两到四岁孩子学习逻辑。 | 367 | 133 | 2019-12-25 |

### 2020-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I wrote a book for engineers that want to become engineering managers](https://news.ycombinator.com/item?id=22033129) | 作者为想转向工程管理的工程师写书，分享上手管理工作的实践知识。 | 695 | 234 | 2020-01-13 |
| 2 | [Show HN: I built a website to better compare USB-C hubs found on Amazon](https://news.ycombinator.com/item?id=22152736) | 建立 USB-C 扩展坞比较网站，帮助对照亚马逊上的不同产品。 | 560 | 275 | 2020-01-26 |
| 3 | [Show HN: Beef, a new performance-oriented programming language](https://news.ycombinator.com/item?id=21991382) | Beef 是以性能为主要目标的新编程语言。 | 533 | 277 | 2020-01-08 |
| 4 | [Show HN: Tired of mobile games with IAP and ads, I made No-Bullshit Games](https://news.ycombinator.com/item?id=22063744) | 厌倦手游内购与广告，作者建立 No-Bullshit Games 寻找更清爽的游戏。 | 520 | 264 | 2020-01-16 |
| 5 | [Show HN: Write a private diary using good old email](https://news.ycombinator.com/item?id=22045053) | 用熟悉的电子邮件写私人日记，降低持续记录的操作门槛。 | 515 | 284 | 2020-01-14 |
| 6 | [Show HN: ESQLate – Build minimum viable admin panels with just SQL](https://news.ycombinator.com/item?id=22073037) | ESQLate 只靠 SQL 构建够用的管理后台。 | 505 | 79 | 2020-01-17 |
| 7 | [Show HN: Regex Cheatsheet](https://news.ycombinator.com/item?id=22200584) | 一份正则表达式速查表，帮助编写和回忆常用匹配语法。 | 499 | 129 | 2020-01-31 |
| 8 | [Show HN: OneDev – A Lightweight GitLab Alternative](https://news.ycombinator.com/item?id=22081419) | OneDev 展示轻量的 GitLab 替代方案。 | 459 | 94 | 2020-01-18 |
| 9 | [Show HN: Text-to-speech and speech-to-text open-source software stack](https://news.ycombinator.com/item?id=22154088) | 开源语音技术栈，同时涵盖文字转语音与语音转文字。 | 438 | 85 | 2020-01-26 |
| 10 | [Show HN: A set of standard document templates](https://news.ycombinator.com/item?id=22091603) | 作者整理多年使用的路演、愿景、策略与产品需求等文档模板。 | 433 | 34 | 2020-01-19 |

### 2020-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Search code in GitHub repos using regular expressions](https://news.ycombinator.com/item?id=22396824) | 通过正则表达式搜索 GitHub 仓库代码，更精确地定位内容。 | 614 | 155 | 2020-02-23 |
| 2 | [Show HN: Profit Hunt - Get inspired by profitable online projects](https://news.ycombinator.com/item?id=22441289) | Profit Hunt 汇集盈利中的线上项目，为创业者寻找实际案例。 | 528 | 95 | 2020-02-28 |
| 3 | [Show HN: Kasaya – A scripting language and runtime for browser automation](https://news.ycombinator.com/item?id=22374991) | Kasaya 提供用于浏览器自动化的脚本语言和运行环境。 | 386 | 106 | 2020-02-20 |
| 4 | [Show HN: A stream of AI-generated art](https://news.ycombinator.com/item?id=22344254) | 持续播放 AI 生成的艺术作品，观察机器创作的不同面貌。 | 277 | 187 | 2020-02-16 |
| 5 | [Show HN: My ML applications book, which HN helped me write (sample chapter) [pdf]](https://news.ycombinator.com/item?id=22249811) | 作者展示机器学习应用书的样章，并感谢 HN 社区参与写作。 | 272 | 37 | 2020-02-05 |
| 6 | [Show HN: Autocode – Automatically generate API code for SaaS apps](https://news.ycombinator.com/item?id=22306996) | Autocode 为 SaaS 应用自动生成 API 代码。 | 247 | 78 | 2020-02-12 |
| 7 | [Show HN: Edtr.io – Intuitive web editor, open source and fully adaptable](https://news.ycombinator.com/item?id=22451568) | Edtr.io 提供开源且可定制的网页编辑器，主打直观操作。 | 234 | 56 | 2020-02-29 |
| 8 | [Show HN: A Firefox extension to add latency to distracting webpages](https://news.ycombinator.com/item?id=22327086) | Firefox 扩展给分心网站增加延迟，用等待打断随手浏览。 | 232 | 51 | 2020-02-14 |
| 9 | [Show HN: Free GeoJSON editor to visualize, download or convert into many formats](https://news.ycombinator.com/item?id=22288276) | 免费 GeoJSON 编辑器，支持可视化、下载和多种格式转换。 | 214 | 25 | 2020-02-10 |
| 10 | [Show HN: I published my first website – ShellMagic.xyz](https://news.ycombinator.com/item?id=22318677) | 作者发布第一个网站 ShellMagic.xyz，分享首次上线的成果。 | 213 | 77 | 2020-02-13 |

### 2020-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Fraidycat](https://news.ycombinator.com/item?id=22545878) | Fraidycat 项目亮相，邀请社区试用并交流反馈。 | 807 | 150 | 2020-03-11 |
| 2 | [Show HN: To fight quarantine boredom I build a site to watch movies with friends](https://news.ycombinator.com/item?id=22687086) | 为缓解隔离期间的无聊，作者制作和朋友一起看电影的网站。 | 515 | 203 | 2020-03-25 |
| 3 | [Show HN: Visual SQL](https://news.ycombinator.com/item?id=22548217) | Visual SQL 展示围绕 SQL 可视化的项目。 | 512 | 126 | 2020-03-11 |
| 4 | [Show HN: Skynet Simulator](https://news.ycombinator.com/item?id=22685011) | Skynet Simulator 项目展示，邀请社区体验这一模拟作品。 | 500 | 210 | 2020-03-25 |
| 5 | [Show HN: Kosmi – Hang out with friends and family online](https://news.ycombinator.com/item?id=22576940) | Kosmi 让亲友在线相聚，尝试弥补无法线下见面的距离。 | 494 | 93 | 2020-03-14 |
| 6 | [Show HN: MVP.css – Minimalist stylesheet for HTML elements](https://news.ycombinator.com/item?id=22681270) | MVP.css 为原生 HTML 元素提供极简样式表。 | 471 | 91 | 2020-03-25 |
| 7 | [Show HN: From Markdown to Video](https://news.ycombinator.com/item?id=22718854) | 从 Markdown 生成视频，把文字内容变成影像表达。 | 441 | 76 | 2020-03-29 |
| 8 | [Show HN: HiddenVM – Use any desktop OS without leaving a trace](https://news.ycombinator.com/item?id=22492343) | HiddenVM 声称可在不留痕迹的前提下使用不同桌面操作系统。 | 429 | 141 | 2020-03-05 |
| 9 | [Show HN: Screen – screen sharing for remote work, by the cofounder of Screenhero](https://news.ycombinator.com/item?id=22676040) | Screenhero 联合创始人推出 Screen，为远程工作提供屏幕共享。 | 406 | 203 | 2020-03-24 |
| 10 | [Show HN: Colors.lol – Overly descriptive color palettes](https://news.ycombinator.com/item?id=22719288) | Colors.lol 用过分详细的名称描述配色，展示带幽默感的色板。 | 388 | 51 | 2020-03-29 |

### 2020-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: A basketball hoop to maximize shots that go in [video]](https://news.ycombinator.com/item?id=22898653) | 视频展示一种希望尽可能提高进球率的篮球框设计。 | 971 | 162 | 2020-04-17 |
| 2 | [Show HN: FalsiScan – Make it look like a PDF has been hand signed and scanned](https://news.ycombinator.com/item?id=22811653) | FalsiScan 让 PDF 看起来像经过手写签名和扫描。 | 770 | 186 | 2020-04-08 |
| 3 | [Show HN: Tom Nook's Laptop](https://news.ycombinator.com/item?id=22867775) | “Tom Nook 的笔记本电脑”项目亮相，展示作者的趣味创作。 | 552 | 127 | 2020-04-14 |
| 4 | [Show HN: An eBook with hundreds of GNU Awk one-liners](https://news.ycombinator.com/item?id=22758217) | 一本 GNU Awk 单行命令电子书，从语法基础讲到实际示例。 | 539 | 48 | 2020-04-02 |
| 5 | [Show HN: I made a Chrome extension to stop mindless browsing](https://news.ycombinator.com/item?id=22936742) | Chrome 扩展试着阻止无意识浏览，帮助在分心前停下来。 | 519 | 138 | 2020-04-21 |
| 6 | [Show HN: Editly – Declarative command-line video editing](https://news.ycombinator.com/item?id=23006794) | Editly 用声明式方式在命令行编辑视频。 | 429 | 75 | 2020-04-28 |
| 7 | [Show HN: 33 line React](https://news.ycombinator.com/item?id=22776753) | 用 33 行代码实现 React 式机制，展示精简实现的实验。 | 418 | 156 | 2020-04-04 |
| 8 | [Show HN: Tara – A smart and free alternative to Jira](https://news.ycombinator.com/item?id=23033387) | Tara 提供免费的项目管理工具，尝试成为 Jira 的替代选择。 | 406 | 176 | 2020-04-30 |
| 9 | [Show HN: DNS over Wikipedia](https://news.ycombinator.com/item?id=22790425) | DNS over Wikipedia 将域名解析与维基百科结合成技术实验。 | 398 | 104 | 2020-04-06 |
| 10 | [Show HN: I built a service to discover and monitor rapidly growing trends](https://news.ycombinator.com/item?id=22777397) | 作者制作服务，发现并持续监控快速增长的趋势。 | 343 | 115 | 2020-04-04 |

### 2020-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Obsidian – A knowledge base that works on local Markdown files](https://news.ycombinator.com/item?id=23324598) | Obsidian 以本地 Markdown 文件为基础构建知识库。 | 1087 | 477 | 2020-05-27 |
| 2 | [Show HN: SHA-256 Animation](https://news.ycombinator.com/item?id=23165333) | 用动画呈现 SHA-256，帮助观察哈希计算过程。 | 1053 | 102 | 2020-05-13 |
| 3 | [Show HN: This Word Does Not Exist](https://news.ycombinator.com/item?id=23169962) | “This Word Does Not Exist”围绕不存在的词语展开创作。 | 956 | 342 | 2020-05-13 |
| 4 | [Show HN: Plotting 3 years of hourly data in 150ms](https://news.ycombinator.com/item?id=23045207) | 作者展示在 150 毫秒内绘制三年逐小时数据的图表方案。 | 785 | 102 | 2020-05-01 |
| 5 | [Show HN: Caddy 2](https://news.ycombinator.com/item?id=23070567) | Caddy 2 版本展示，介绍这一 Web 服务器项目的新进展。 | 778 | 240 | 2020-05-04 |
| 6 | [Show HN: Twitch Roulette – Find and chat with streamers who are streaming alone](https://news.ycombinator.com/item?id=23114103) | Twitch Roulette 帮用户发现独自直播的主播，并进入聊天室交流。 | 732 | 202 | 2020-05-08 |
| 7 | [Show HN: RoughNotation – create and animate hand-drawn annotations on a web page](https://news.ycombinator.com/item?id=23339244) | RoughNotation 为网页添加带动画的手绘标注。 | 696 | 74 | 2020-05-28 |
| 8 | [Show HN: Bear – Minimal blogging platform](https://news.ycombinator.com/item?id=23312339) | Bear 提供极简博客平台，让写作与发布保持轻量。 | 685 | 349 | 2020-05-26 |
| 9 | [Show HN: Lite – A small, fast text editor](https://news.ycombinator.com/item?id=23126458) | Lite 是小型文本编辑器，作者强调简洁与速度。 | 607 | 256 | 2020-05-09 |
| 10 | [Show HN: Make Your PDF Look Scanned](https://news.ycombinator.com/item?id=23157408) | 给 PDF 加上扫描件外观，模拟纸质文档数字化后的效果。 | 607 | 168 | 2020-05-12 |

### 2020-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: A Reddit reader that looks like the frontpage of a print newspaper](https://news.ycombinator.com/item?id=23658721) | 把 Reddit 内容排成纸质报纸头版，换一种方式阅读社区。 | 638 | 122 | 2020-06-27 |
| 2 | [Show HN: Hacker News front page in the style of a print newspaper](https://news.ycombinator.com/item?id=23669650) | 把 Hacker News 首页排成报纸头版，重现纸媒阅读样式。 | 627 | 133 | 2020-06-28 |
| 3 | [Show HN: Download Hi-Res Public Domain Art, Posters and Illustrations](https://news.ycombinator.com/item?id=23491940) | 提供高分辨率公共领域艺术、海报与插画的下载入口。 | 550 | 51 | 2020-06-11 |
| 4 | [Show HN: My daughter and I made a site to explore the photos from the ISS](https://news.ycombinator.com/item?id=23519439) | 作者与女儿制作网站，一起探索国际空间站拍摄的照片。 | 528 | 120 | 2020-06-14 |
| 5 | [Show HN: Collected Notes – A note-taking blogging app I made](https://news.ycombinator.com/item?id=23514682) | Collected Notes 将记笔记与写博客结合，展示作者的个人应用。 | 457 | 227 | 2020-06-14 |
| 6 | [Show HN: Grid.js – Advanced table library that works everywhere](https://news.ycombinator.com/item?id=23420091) | Grid.js 提供通用表格库，面向不同网页环境中的数据展示。 | 390 | 132 | 2020-06-04 |
| 7 | [Show HN: Rainbow – an attempt to display colour on a B&W monitor](https://news.ycombinator.com/item?id=23661808) | Rainbow 尝试在黑白显示器上呈现颜色。 | 389 | 58 | 2020-06-27 |
| 8 | [Show HN: PJDL an open alternative to 1-wire with a range of 2000m](https://news.ycombinator.com/item?id=23591953) | PJDL 提供开放的单线通信替代方案，作者称距离可达两千米。 | 337 | 16 | 2020-06-21 |
| 9 | [Show HN: Daily non-commercial blog posts which didn't reach HN's front page](https://news.ycombinator.com/item?id=23392049) | 每天整理未登上 HN 首页的非商业博客，发现被热门榜遗漏的写作。 | 289 | 93 | 2020-06-02 |
| 10 | [Show HN: HiFiC – High-Fidelity Generative Image Compression – demo and paper](https://news.ycombinator.com/item?id=23652753) | HiFiC 分享高保真生成式图像压缩演示与论文。 | 281 | 89 | 2020-06-26 |

### 2020-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: TinyPilot – Build a KVM over IP using a Raspberry Pi](https://news.ycombinator.com/item?id=23927380) | TinyPilot 用树莓派构建网络 KVM，远程控制另一台电脑。 | 756 | 279 | 2020-07-23 |
| 2 | [Show HN: 3D Book Image CSS Generator](https://news.ycombinator.com/item?id=23896856) | 用 CSS 生成三维书籍封面图，方便展示电子书和出版物。 | 638 | 87 | 2020-07-20 |
| 3 | [Show HN: Primo – all-in-one IDE, CMS, component library, static site generator](https://news.ycombinator.com/item?id=23820201) | Primo 将 IDE、内容管理、组件库与静态站点生成集中到一起。 | 575 | 209 | 2020-07-13 |
| 4 | [Show HN: Neural text to speech with dozens of celebrity voices](https://news.ycombinator.com/item?id=23965787) | 神经语音合成项目提供多种名人声音，展示声音生成实验。 | 462 | 165 | 2020-07-27 |
| 5 | [Show HN: USA.css – units set in inches, 1776 bytes](https://news.ycombinator.com/item?id=23733926) | USA.css 用英寸作为单位，把 1776 字节样式表做成美式玩笑。 | 457 | 180 | 2020-07-04 |
| 6 | [Show HN: SheetUI – Turn Google Sheets into Web Pages](https://news.ycombinator.com/item?id=23760846) | SheetUI 把 Google Sheets 电子表格转成网页。 | 425 | 147 | 2020-07-07 |
| 7 | [Show HN: Trail Router – generate running routes that prefer greenery and nature](https://news.ycombinator.com/item?id=23802317) | Trail Router 优先考虑绿地与自然环境，帮助生成跑步路线。 | 402 | 128 | 2020-07-11 |
| 8 | [Show HN: WebGL simulation of rainy autumn day/evening](https://news.ycombinator.com/item?id=23985825) | 用 WebGL 模拟秋日雨景，展现白天或傍晚的氛围。 | 393 | 60 | 2020-07-29 |
| 9 | [Show HN: MineSweeper implemented in 100% CSS and HTML – no JavaScript](https://news.ycombinator.com/item?id=23920987) | 只用 HTML 与 CSS 实现扫雷，不依赖 JavaScript。 | 390 | 92 | 2020-07-22 |
| 10 | [Show HN: Runnaroo – A new search engine](https://news.ycombinator.com/item?id=23771131) | Runnaroo 展示新的搜索引擎，邀请社区尝试不同的搜索选择。 | 380 | 196 | 2020-07-08 |

### 2020-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I built an After Effects for dummies](https://news.ycombinator.com/item?id=24054382) | 作者制作面向新手的动效工具，称其为“傻瓜版 After Effects”。 | 868 | 291 | 2020-08-04 |
| 2 | [Show HN: Learn how WebRTC actually works. A book on the protocols, not just APIs](https://news.ycombinator.com/item?id=24323589) | 一本讲解 WebRTC 协议的书，帮助理解 API 背后的实际工作原理。 | 667 | 72 | 2020-08-30 |
| 3 | [Show HN: Visualize Data Structures in VS Code](https://news.ycombinator.com/item?id=24304623) | 在 VS Code 中可视化数据结构，让代码里的对象更容易观察。 | 509 | 61 | 2020-08-28 |
| 4 | [Show HN: Photo Realistic QR-Codes](https://news.ycombinator.com/item?id=24158125) | 把二维码做成接近照片的外观，探索图像与可扫描信息的结合。 | 482 | 106 | 2020-08-14 |
| 5 | [Show HN: Hndex.org – a full-text search engine of articles submitted to HN](https://news.ycombinator.com/item?id=24079592) | Hndex.org 提供 HN 投稿文章的全文搜索。 | 442 | 78 | 2020-08-07 |
| 6 | [Show HN: Healthcare Is Dumb](https://news.ycombinator.com/item?id=24309237) | “Healthcare Is Dumb”项目亮相，表达作者对医疗体系的关注。 | 441 | 283 | 2020-08-28 |
| 7 | [Show HN: Vimac – Productive macOS keyboard-driven navigation](https://news.ycombinator.com/item?id=24323378) | Vimac 为 macOS 提供键盘驱动的导航，减少操作时对鼠标的依赖。 | 375 | 73 | 2020-08-30 |
| 8 | [Show HN: Starboard – Fully in-browser literate notebooks like Jupyter Notebook](https://news.ycombinator.com/item?id=24029002) | Starboard 提供完全在浏览器内运行、类似 Jupyter 的代码笔记本。 | 371 | 101 | 2020-08-02 |
| 9 | [Show HN: I'm 15 and made a bedtime calculator with React JavaScript](https://news.ycombinator.com/item?id=24139339) | 一位 15 岁作者用 React 制作睡眠时间计算器。 | 312 | 121 | 2020-08-13 |
| 10 | [Show HN: I made an extension to watch Netflix films with screenplays in sync](https://news.ycombinator.com/item?id=24178295) | 浏览器扩展同步显示 Netflix 电影与剧本，边看片边对照文字。 | 289 | 62 | 2020-08-16 |

### 2020-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Linux sysadmin course, eight years on](https://news.ycombinator.com/item?id=24380969) | 八年后回看 Linux 管理员课程，作者在生活变故后更新自己的教学项目。 | 780 | 83 | 2020-09-05 |
| 2 | [Show HN: A SQL database implemented purely in TypeScript type annotations](https://news.ycombinator.com/item?id=24615185) | 只用 TypeScript 类型注解实现 SQL 数据库，探索类型系统的计算能力。 | 426 | 191 | 2020-09-28 |
| 3 | [Show HN: Mimestream, a native macOS email client for Gmail](https://news.ycombinator.com/item?id=24422432) | Mimestream 为 Gmail 提供原生 macOS 邮件客户端。 | 403 | 272 | 2020-09-09 |
| 4 | [Show HN: Mono Icons – A simple, consistent open-source icon set](https://news.ycombinator.com/item?id=24564684) | Mono Icons 提供简洁、风格一致的开源图标。 | 333 | 58 | 2020-09-23 |
| 5 | [Show HN: Talk – A free group video call app with screen sharing](https://news.ycombinator.com/item?id=24381700) | Talk 提供免费的群组视频通话，并支持屏幕共享。 | 310 | 99 | 2020-09-05 |
| 6 | [Show HN: ugit – Learn Git Internals by Building Git in Python](https://news.ycombinator.com/item?id=24517925) | ugit 通过用 Python 重建 Git，帮助理解版本控制内部机制。 | 309 | 30 | 2020-09-18 |
| 7 | [Show HN: Free hosted open-source alternative to Zapier/Airflow](https://news.ycombinator.com/item?id=24407706) | 提供免费托管的开源自动化工具，尝试替代 Zapier 与 Airflow。 | 279 | 79 | 2020-09-08 |
| 8 | [Show HN: Octo – Generate a serverless API from an SQL query](https://news.ycombinator.com/item?id=24442294) | Octo 从一条 SQL 查询生成无服务器 API。 | 241 | 58 | 2020-09-11 |
| 9 | [Show HN: DevUtils.app – Developer Utilities for macOS](https://news.ycombinator.com/item?id=24604291) | DevUtils 将 JSON 格式化、JWT 调试等工具放到离线 Mac 应用，减少上传数据。 | 241 | 105 | 2020-09-27 |
| 10 | [Show HN: My GitHub Readme Is Interactive](https://news.ycombinator.com/item?id=24370296) | 作者把 GitHub 自我介绍做成交互式页面，拓展 README 的表现形式。 | 237 | 99 | 2020-09-04 |

### 2020-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I made a site where you practice typing by retyping entire novels](https://news.ycombinator.com/item?id=24696658) | 通过重新输入整部小说来练习打字的网站。 | 1589 | 378 | 2020-10-06 |
| 2 | [Show HN: I built a Rotten Tomatoes-style platform for durable products](https://news.ycombinator.com/item?id=24707407) | 一个借鉴烂番茄评分方式、评价耐用商品的平台。 | 1392 | 398 | 2020-10-07 |
| 3 | [Show HN: What would mechanical programming look like?](https://news.ycombinator.com/item?id=24934722) | 如果编程依靠机械完成，作者用实验展示它可能呈现的样子。 | 719 | 149 | 2020-10-29 |
| 4 | [Show HN: I made earrings that work like earphones](https://news.ycombinator.com/item?id=24781175) | 作者制作能像耳机一样工作的耳环，将饰品与音频功能结合。 | 462 | 184 | 2020-10-14 |
| 5 | [Show HN: Low-Level Academy, an explorable systems programming course](https://news.ycombinator.com/item?id=24764589) | Low-Level Academy 提供可探索的系统编程课程。 | 419 | 37 | 2020-10-13 |
| 6 | [Show HN: Igel – A CLI tool to run machine learning without writing code](https://news.ycombinator.com/item?id=24671525) | Igel 用命令行运行机器学习，希望无需编写代码也能使用模型。 | 405 | 102 | 2020-10-03 |
| 7 | [Show HN: I wrote a book on writing good developer resumes](https://news.ycombinator.com/item?id=24777640) | 作者写书讲开发者简历，帮助程序员更清楚地呈现自己的经历。 | 382 | 108 | 2020-10-14 |
| 8 | [Show HN: I reverse engineered my cable modem and turned it into an SDR](https://news.ycombinator.com/item?id=24719680) | 逆向有线调制解调器，再把它改造成软件无线电设备。 | 357 | 70 | 2020-10-08 |
| 9 | [Show HN: Plausible – Self-Hosted Google Analytics alternative](https://news.ycombinator.com/item?id=24696145) | Plausible 提供可自托管的网站分析，作为 Google Analytics 的替代选择。 | 351 | 139 | 2020-10-06 |
| 10 | [Show HN: Arturo – REBOL-inspired programming language and VM written in Nim](https://news.ycombinator.com/item?id=24834636) | Arturo 受 REBOL 启发，用 Nim 编写编程语言与虚拟机。 | 324 | 57 | 2020-10-20 |

### 2020-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I Rebuilt MySpace from 2007](https://news.ycombinator.com/item?id=25245740) | 作者重建 2007 年的 MySpace，回到早期社交网站的界面体验。 | 726 | 290 | 2020-11-29 |
| 2 | [Show HN: Self-hosted offline Internet from your browsing history](https://news.ycombinator.com/item?id=25059554) | 把浏览历史保存为自托管的离线互联网，保留看过的网页。 | 537 | 158 | 2020-11-11 |
| 3 | [Show HN: Ugliest.app – Ugly but good app platform](https://news.ycombinator.com/item?id=24992517) | Ugliest.app 展示“外观丑但好用”的应用平台。 | 441 | 155 | 2020-11-04 |
| 4 | [Show HN: Zfs.rent](https://news.ycombinator.com/item?id=25148000) | Zfs.rent 项目亮相，作者邀请社区了解这一服务。 | 403 | 219 | 2020-11-19 |
| 5 | [Show HN: A Stargate in 140 chars of JavaScript](https://news.ycombinator.com/item?id=25088683) | 用 140 个字符的 JavaScript 做出星际之门，展示极短代码的表现力。 | 377 | 55 | 2020-11-13 |
| 6 | [Show HN: I created a URL shortener that can be entirely hosted on GitHub Pages](https://news.ycombinator.com/item?id=25110879) | 完全托管在 GitHub Pages 上的短链接服务，减少额外服务器依赖。 | 355 | 176 | 2020-11-16 |
| 7 | [Show HN: Etebase – An open source and end-to-end encrypted Firebase alternative](https://news.ycombinator.com/item?id=25059133) | Etebase 提供开源、端到端加密的 Firebase 替代方案。 | 308 | 80 | 2020-11-11 |
| 8 | [Show HN: I made an alternative to Google Alerts that listens to social media](https://news.ycombinator.com/item?id=25161117) | 作者制作 Google Alerts 替代工具，把关注范围延伸到社交媒体。 | 261 | 107 | 2020-11-20 |
| 9 | [Show HN: I made a Mahjong browser game](https://news.ycombinator.com/item?id=25246179) | 一个运行在浏览器里的麻将游戏，作者分享自己的实现。 | 252 | 85 | 2020-11-29 |
| 10 | [Show HN: LibreASR – An On-Premises, Streaming Speech Recognition System](https://news.ycombinator.com/item?id=25099847) | LibreASR 提供可在本地部署的流式语音识别系统。 | 233 | 71 | 2020-11-15 |

### 2020-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: PSX Party – Online Multiplayer Playstation 1 Emulator Using WebRTC](https://news.ycombinator.com/item?id=25582187) | PSX Party 用 WebRTC 支持在线多人游玩 PlayStation 1 模拟器。 | 676 | 171 | 2020-12-30 |
| 2 | [Show HN: After 2.5 years on my side project, it has hit £500/month revenue](https://news.ycombinator.com/item?id=25372464) | 做了两年半的业余项目月收入达到五百英镑，作者分享坚持与产品调整。 | 647 | 313 | 2020-12-10 |
| 3 | [Show HN: This website is valid JSON](https://news.ycombinator.com/item?id=25352385) | 这个网站本身也是有效 JSON，探索网页与数据格式的重合。 | 604 | 229 | 2020-12-08 |
| 4 | [Show HN: Boltstream – Self-hosted full end-to-end live video streaming platform](https://news.ycombinator.com/item?id=25328622) | Boltstream 提供可自行托管的完整视频直播平台。 | 510 | 93 | 2020-12-07 |
| 5 | [Show HN: After 10 years my side project has hit $8k/mo in revenue](https://news.ycombinator.com/item?id=25434753) | 邮件别名项目做了十年后月入八千美元，作者分享保护真实邮箱的生意。 | 442 | 210 | 2020-12-15 |
| 6 | [Show HN: Instantly search 28M books from OpenLibrary](https://news.ycombinator.com/item?id=25414389) | 即时搜索 OpenLibrary 的两千八百万本书，缩短查找书目的等待。 | 424 | 80 | 2020-12-14 |
| 7 | [Show HN: Thruhikes – A list of long distance hikes around the world](https://news.ycombinator.com/item?id=25568856) | Thruhikes 汇集世界各地的长距离徒步路线。 | 405 | 131 | 2020-12-29 |
| 8 | [Show HN: Hystoria – a Reddit-like site where all posts must be 5+ years old](https://news.ycombinator.com/item?id=25361224) | Hystoria 借鉴 Reddit，但只允许发布五年以上的旧内容。 | 375 | 97 | 2020-12-09 |
| 9 | [Show HN: Raspberry Pi 400 with a $2 IPS 240x240 micro display](https://news.ycombinator.com/item?id=25566132) | 为 Raspberry Pi 400 加上两美元的微型 IPS 屏幕，展示硬件搭配。 | 357 | 129 | 2020-12-29 |
| 10 | [Show HN: Instantly search 2M recipes](https://news.ycombinator.com/item?id=25365397) | 即时搜索两百万份食谱，从大量菜谱中快速找做法。 | 349 | 126 | 2020-12-09 |

### 2021-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Beeper – All Your Chats in One App](https://news.ycombinator.com/item?id=25848278) | Beeper 尝试把各种聊天集中到一个应用。 | 962 | 486 | 2021-01-20 |
| 2 | [Show HN: I made an alternative platform for professional profiles](https://news.ycombinator.com/item?id=25634192) | 作者为职业个人档案建立替代平台，探索不同的履历展示方式。 | 938 | 358 | 2021-01-04 |
| 3 | [Show HN: I shot high-res stitched panoramas in Iceland using a thermal camera](https://news.ycombinator.com/item?id=25614167) | 作者用热成像相机拍摄并拼接冰岛高分辨率全景。 | 753 | 95 | 2021-01-02 |
| 4 | [Show HN: I built an online interactive course that helps you learn Vim faster](https://news.ycombinator.com/item?id=25846347) | 交互式在线课程帮助学习 Vim，把操作练习放在教学过程中。 | 667 | 280 | 2021-01-20 |
| 5 | [Show HN: Iconduck – 100k open source icons, downloadable and searchable](https://news.ycombinator.com/item?id=25872922) | Iconduck 提供十万枚可搜索、可下载的开源图标。 | 528 | 74 | 2021-01-22 |
| 6 | [Show HN: Lightspeed – subsecond, open source, self hosted stream from OBS](https://news.ycombinator.com/item?id=25627673) | Lightspeed 提供开源自托管方案，将 OBS 视频流的延迟目标压到秒以下。 | 452 | 138 | 2021-01-04 |
| 7 | [Show HN: Compare prices that US hospitals charge patients, insurance companies](https://news.ycombinator.com/item?id=25821873) | 比较美国医院向患者与保险公司收取的价格，呈现医疗账单差异。 | 447 | 374 | 2021-01-18 |
| 8 | [Show HN: Virtual breadboard in the browser, inspired by Ben Eater's 6502](https://news.ycombinator.com/item?id=25836395) | 受 Ben Eater 的 6502 项目启发，在浏览器中制作虚拟面包板。 | 409 | 73 | 2021-01-19 |
| 9 | [Show HN: I built a 4kb alternative to React, Vue, etc for building web UIs.](https://news.ycombinator.com/item?id=25677272) | 作者用约 4KB 代码制作 Web UI 框架，尝试替代 React 与 Vue。 | 343 | 162 | 2021-01-07 |
| 10 | [Show HN: A usable eBook reader inside a browser (azw3, mobi, ePub, pdf)](https://news.ycombinator.com/item?id=25948797) | 在浏览器里阅读电子书，支持 azw3、mobi、ePub 与 PDF。 | 297 | 69 | 2021-01-28 |

### 2021-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Redbean – Single-file distributable web server](https://news.ycombinator.com/item?id=26271117) | Redbean 将 Web 服务器打包为单个可分发文件。 | 1998 | 249 | 2021-02-26 |
| 2 | [Show HN: Can’t afford Bloomberg Terminal? No prob, I built the next best thing](https://news.ycombinator.com/item?id=26258773) | 开发者展示面向无力购买彭博终端用户的替代工具。 | 1422 | 289 | 2021-02-25 |
| 3 | [Show HN: I wrote a book about using data science to solve “everyday” problems](https://news.ycombinator.com/item?id=26253281) | 一本用数据科学处理日常问题的书，把分析方法带进生活。 | 632 | 96 | 2021-02-24 |
| 4 | [Show HN: Clerk – all of user management as-a-service, not just authentication](https://news.ycombinator.com/item?id=26069621) | Clerk 将完整用户管理做成服务，覆盖身份验证之外的工作。 | 582 | 223 | 2021-02-08 |
| 5 | [Show HN: Haven – Run a private website to share with only the people you choose](https://news.ycombinator.com/item?id=26013715) | Haven 让用户运行私密网站，只与自己选定的人分享内容。 | 547 | 227 | 2021-02-03 |
| 6 | [Show HN: Khan-dl – Khan Academy Course Downloader](https://news.ycombinator.com/item?id=26134915) | Khan-dl 提供可汗学院课程下载工具。 | 473 | 173 | 2021-02-14 |
| 7 | [Show HN: ustaxes.org – open-source tax filing webapp](https://news.ycombinator.com/item?id=26138446) | ustaxes.org 用开源 Web 应用处理报税。 | 465 | 219 | 2021-02-15 |
| 8 | [Show HN: Call a Dev – Pay Stack Overflow users $1/min for live programming help](https://news.ycombinator.com/item?id=26226805) | Call a Dev 按每分钟一美元付费，请 Stack Overflow 用户实时解答编程问题。 | 451 | 248 | 2021-02-22 |
| 9 | [Show HN: QEMU front end for M1 and Intel Macs](https://news.ycombinator.com/item?id=26260390) | 为 M1 与 Intel Mac 提供 QEMU 图形前端。 | 418 | 122 | 2021-02-25 |
| 10 | [Show HN: Hummingbard – decentralized communities built on Matrix](https://news.ycombinator.com/item?id=26277602) | Hummingbard 基于 Matrix 构建去中心化社区。 | 412 | 83 | 2021-02-26 |

### 2021-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I wrote a book about Go](https://news.ycombinator.com/item?id=26568014) | 作者介绍自己写的 Go 编程书，向社区分享写作成果。 | 919 | 157 | 2021-03-24 |
| 2 | [Show HN: Svelte NodeGUI, a lightweight Electron alternative with native UI](https://news.ycombinator.com/item?id=26361423) | Svelte NodeGUI 采用原生界面，提供轻量 Electron 替代方案。 | 624 | 271 | 2021-03-05 |
| 3 | [Show HN: Video Game in a Font](https://news.ycombinator.com/item?id=26495059) | 把电子游戏放进字体文件，探索字体机制的非常规用途。 | 605 | 76 | 2021-03-17 |
| 4 | [Show HN: Sorted CSS Colors – Sort the named CSS colors in a nice way](https://news.ycombinator.com/item?id=26503572) | 将 CSS 命名颜色重新排序，寻找更舒服的色彩浏览方式。 | 559 | 159 | 2021-03-18 |
| 5 | [Show HN: I built a VS Code Theme Creator – easily make VS Code themes in browser](https://news.ycombinator.com/item?id=26579936) | 在浏览器里制作 VS Code 主题，实时调整编辑器配色。 | 375 | 104 | 2021-03-25 |
| 6 | [Show HN: I made a tool to convert images of tables to CSV](https://news.ycombinator.com/item?id=26403341) | 把表格图片转换为 CSV，减少手工录入表格数据。 | 354 | 60 | 2021-03-09 |
| 7 | [Show HN: An open-source, self-hostable Heroku and Netlify alternative](https://news.ycombinator.com/item?id=26624341) | 一个可自托管的开源平台，尝试替代 Heroku 与 Netlify。 | 345 | 116 | 2021-03-29 |
| 8 | [Show HN: I wrote a program to convert lines of text into trees](https://news.ycombinator.com/item?id=26622548) | 把一行行文本变成树，作者展示自己编写的转换程序。 | 333 | 53 | 2021-03-29 |
| 9 | [Show HN: A Latin self study course, Khan Academy-style](https://news.ycombinator.com/item?id=26609397) | 借鉴可汗学院的形式，提供拉丁语自学课程。 | 278 | 109 | 2021-03-28 |
| 10 | [Show HN: I built a zero-cost, ad-free alternative to LinkedIn](https://news.ycombinator.com/item?id=26475898) | 作者制作免费、无广告的职业社交平台，尝试替代 LinkedIn。 | 249 | 184 | 2021-03-16 |

### 2021-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Lofi.cafe](https://news.ycombinator.com/item?id=26805702) | Lofi.cafe 展示以 Lo-fi 为主题的网站，邀请用户体验。 | 1192 | 230 | 2021-04-14 |
| 2 | [Show HN: PDFs from HTML](https://news.ycombinator.com/item?id=26691626) | 从 HTML 生成 PDF，探索网页内容到文档的转换。 | 742 | 265 | 2021-04-04 |
| 3 | [Show HN: Second-Chance Pool](https://news.ycombinator.com/item?id=26998308) | 以“Second-Chance Pool”为名的项目亮相，展示作者的新想法。 | 543 | 91 | 2021-04-30 |
| 4 | [Show HN: I made a simulator for personal finance](https://news.ycombinator.com/item?id=26969173) | 作者制作个人财务模拟器，帮助观察不同财务选择的影响。 | 479 | 255 | 2021-04-28 |
| 5 | [Show HN: I'm working on a open-source, self-hosted alternative to Disqus](https://news.ycombinator.com/item?id=26878153) | 开发中的开源自托管评论工具，尝试替代 Disqus。 | 436 | 167 | 2021-04-20 |
| 6 | [Show HN: My personal website is a shell](https://news.ycombinator.com/item?id=26700770) | 把个人网站做成 Shell，用命令行方式浏览自我介绍。 | 425 | 171 | 2021-04-05 |
| 7 | [Show HN: I made a sandbox game to help with financial planning](https://news.ycombinator.com/item?id=26900079) | 通过沙盒游戏进行财务规划，在模拟中尝试不同安排。 | 409 | 140 | 2021-04-22 |
| 8 | [Show HN: Mail Studio – IDE for designing responsive emails](https://news.ycombinator.com/item?id=26659553) | Mail Studio 为响应式邮件设计提供集成开发环境。 | 395 | 209 | 2021-04-01 |
| 9 | [Show HN: Side project passed $2.5k/mo revenue after 2 years (Phoenix and Vue)](https://news.ycombinator.com/item?id=26855726) | 用 Phoenix 与 Vue 制作销售提案工具，作者分享两年后月入 2,500 美元的进展。 | 381 | 89 | 2021-04-18 |
| 10 | [Show HN: Science and math-flavored programming problems for beginners](https://news.ycombinator.com/item?id=26843339) | 给编程初学者的练习题，融入科学与数学主题。 | 369 | 73 | 2021-04-17 |

### 2021-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I wrote my own RTS game engine in C](https://news.ycombinator.com/item?id=27132334) | 开发者展示自己用 C 编写的即时战略游戏引擎。 | 1102 | 262 | 2021-05-12 |
| 2 | [Show HN: A portfolio website simulating macOS's GUI using React](https://news.ycombinator.com/item?id=27084995) | 用 React 模拟 macOS 图形界面，制作个人作品集网站。 | 683 | 191 | 2021-05-08 |
| 3 | [Show HN: Mmm.page – Drag and drop personal website creator](https://news.ycombinator.com/item?id=27128424) | Mmm.page 通过拖拽制作个人网站，让页面编排更自由。 | 591 | 150 | 2021-05-12 |
| 4 | [Show HN: NocoDB – Open-Source Airtable Alternative](https://news.ycombinator.com/item?id=27303783) | NocoDB 提供开源的 Airtable 替代方案。 | 562 | 157 | 2021-05-27 |
| 5 | [Show HN: I open sourced a game I just released on Steam, written in Lua](https://news.ycombinator.com/item?id=27254177) | 作者开源刚在 Steam 发布的 Lua 游戏，分享完整开发成果。 | 496 | 97 | 2021-05-23 |
| 6 | [Show HN: Control your Bose headphones from your Mac's menubar](https://news.ycombinator.com/item?id=27034904) | 从 Mac 菜单栏控制 Bose 耳机，减少切换应用的操作。 | 450 | 239 | 2021-05-04 |
| 7 | [Show HN: Inflation-adjusted Hacker News](https://news.ycombinator.com/item?id=27249082) | 把 Hacker News 按通货膨胀调整，展示一种另类社区实验。 | 437 | 120 | 2021-05-22 |
| 8 | [Show HN: I wrote a book about UI [pdf]](https://news.ycombinator.com/item?id=27210022) | 作者分享自己撰写的 UI 书籍，并提供 PDF 阅读。 | 411 | 151 | 2021-05-19 |
| 9 | [Show HN: Find Subreddits for Your Niche](https://news.ycombinator.com/item?id=27293902) | 根据细分兴趣寻找 subreddit，发现更贴近主题的社区。 | 406 | 181 | 2021-05-26 |
| 10 | [Show HN: Tool that turns your images into plotter-like line drawings](https://news.ycombinator.com/item?id=27224094) | 把图片转换成绘图机风格的线描，探索图像的线条表达。 | 405 | 74 | 2021-05-20 |

### 2021-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: iPod.js – An online iPod that connects to Spotify and Apple Music](https://news.ycombinator.com/item?id=27606099) | iPod.js 在网页中重现 iPod，并连接 Spotify 与 Apple Music。 | 866 | 157 | 2021-06-23 |
| 2 | [Show HN: Open-source alternative to Retool, Internal.io, etc.](https://news.ycombinator.com/item?id=27421408) | 开源内部工具平台亮相，尝试替代 Retool 与 Internal.io。 | 429 | 68 | 2021-06-07 |
| 3 | [Show HN: I made a community sourced fitness routine database](https://news.ycombinator.com/item?id=27503597) | 作者建立由社区贡献的健身训练数据库，汇集不同的训练安排。 | 396 | 188 | 2021-06-14 |
| 4 | [Show HN: Influence, a Go-inspired 1-minute board game](https://news.ycombinator.com/item?id=27520884) | Influence 受围棋启发，把棋盘对弈压缩到一分钟。 | 379 | 112 | 2021-06-15 |
| 5 | [Show HN: I made a new kind of Bible app](https://news.ycombinator.com/item?id=27592473) | 作者制作一种新的《圣经》应用，探索经文阅读的不同体验。 | 347 | 253 | 2021-06-22 |
| 6 | [Show HN: Multiverse.plus – what if blogging was more collage-like and colorful?](https://news.ycombinator.com/item?id=27599470) | Multiverse.plus 把博客变成更有色彩的拼贴，探索自由表达的版面。 | 281 | 84 | 2021-06-23 |
| 7 | [Show HN: LANDrop – A cross-platform AirDrop-like file transfer tool](https://news.ycombinator.com/item?id=27481465) | LANDrop 提供类似 AirDrop 的跨平台文件传输工具。 | 250 | 98 | 2021-06-12 |
| 8 | [Show HN: I discovered a trading algorithm that returns ~24.85% annually](https://news.ycombinator.com/item?id=27414677) | 作者声称发现年回报约 24.85% 的交易算法，邀请社区查看。 | 249 | 128 | 2021-06-06 |
| 9 | [Show HN: 3dasd – open-source DIY room-scale 3D scanner](https://news.ycombinator.com/item?id=27614874) | 3dasd 是开源自制三维扫描仪，面向房间尺度的扫描。 | 248 | 63 | 2021-06-24 |
| 10 | [Show HN: Find Your Hacker News Doppelgänger](https://news.ycombinator.com/item?id=27568709) | 寻找自己在 Hacker News 上的“分身”，发现相似的社区用户。 | 246 | 215 | 2021-06-20 |

### 2021-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Static.wiki – read-only Wikipedia using a 43GB SQLite file](https://news.ycombinator.com/item?id=28012829) | Static.wiki 用 43GB 的 SQLite 文件提供只读维基百科。 | 796 | 189 | 2021-07-30 |
| 2 | [Show HN: Print a WiFi Login Card](https://news.ycombinator.com/item?id=27803146) | 打印 Wi-Fi 登录卡，把网络连接信息方便地分享给访客。 | 769 | 326 | 2021-07-11 |
| 3 | [Show HN: Obsidian for Mobile – Plain-text knowledge base on the go](https://news.ycombinator.com/item?id=27807850) | Obsidian 推出移动版，让纯文本知识库随身可用。 | 760 | 318 | 2021-07-12 |
| 4 | [Show HN: RSS feeds for arbitrary websites using CSS selectors](https://news.ycombinator.com/item?id=27739568) | 用 CSS 选择器为任意网站生成 RSS，追踪缺少订阅源的内容。 | 509 | 127 | 2021-07-05 |
| 5 | [Show HN: Side Quest – An aggregator for not full-time tech jobs](https://news.ycombinator.com/item?id=27749497) | Side Quest 汇集非全职技术工作，为兼职与灵活工作寻找入口。 | 401 | 105 | 2021-07-06 |
| 6 | [Show HN: I made a simulator for personal finance and financial independence](https://news.ycombinator.com/item?id=27844194) | 作者制作个人财务与财务独立模拟器，探索长期资金安排。 | 294 | 164 | 2021-07-15 |
| 7 | [Show HN: I built an app to create repeatable checklists to help with ADHD](https://news.ycombinator.com/item?id=27871790) | 可重复使用的检查清单应用，作者希望帮助应对 ADHD。 | 282 | 200 | 2021-07-18 |
| 8 | [Show HN: Sioyek – PDF viewer for reading research papers and technical documents](https://news.ycombinator.com/item?id=27893303) | Sioyek 为研究论文和技术文档提供专门的 PDF 阅读器。 | 272 | 63 | 2021-07-20 |
| 9 | [Show HN: Website changes design each time you blink](https://news.ycombinator.com/item?id=27929278) | 每次眨眼网站就改变设计，作者将眨眼变成界面触发机制。 | 261 | 192 | 2021-07-23 |
| 10 | [Show HN: Earthly – Better Builds](https://news.ycombinator.com/item?id=27785323) | Earthly 展示构建工具，希望改善软件构建过程。 | 223 | 82 | 2021-07-09 |

### 2021-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Imba – I have spent 7 years creating a programming language for the web](https://news.ycombinator.com/item?id=28207662) | 开发者介绍耗时七年打造、编译为 JavaScript 的 Imba 语言。 | 1216 | 345 | 2021-08-17 |
| 2 | [Show HN: We built an end-to-end encrypted alternative to Google Photos](https://news.ycombinator.com/item?id=28347439) | ente 展示支持跨设备备份的端到端加密照片服务。 | 1180 | 405 | 2021-08-29 |
| 3 | [Show HN: Neural-hash-collider – Find target hash collisions for NeuralHash](https://news.ycombinator.com/item?id=28229291) | Neural-hash-collider 尝试为 NeuralHash 寻找指定目标的哈希碰撞。 | 623 | 351 | 2021-08-19 |
| 4 | [Show HN: With a 9-5 job and 2 kids I have finally finished my first MVP](https://news.ycombinator.com/item?id=28320346) | 全职工作并照顾两个孩子，作者利用晚间和周末做出期权筛选工具。 | 501 | 194 | 2021-08-26 |
| 5 | [Show HN: I made a meme creator that makes around $4k a month](https://news.ycombinator.com/item?id=28329444) | 作者制作表情包工具，并分享每月约四千美元的收入进展。 | 418 | 217 | 2021-08-27 |
| 6 | [Show HN: I built an AI art installation at home generating new pieces on the fly](https://news.ycombinator.com/item?id=28221904) | 在家搭建 AI 艺术装置，现场不断生成新的作品。 | 399 | 153 | 2021-08-18 |
| 7 | [Show HN: 59a34eabe31910abfb06f308 – NeuralHash Collision Demo](https://news.ycombinator.com/item?id=28305394) | 以具体哈希值为题展示 NeuralHash 碰撞演示。 | 339 | 235 | 2021-08-25 |
| 8 | [Show HN: Nomad Visa – Working remotely? Explore your visa options](https://news.ycombinator.com/item?id=28167358) | Nomad Visa 帮远程工作者了解可选择的签证路径。 | 285 | 158 | 2021-08-13 |
| 9 | [Show HN: Visualizing a Codebase](https://news.ycombinator.com/item?id=28074827) | 用鸟瞰式视图展示代码库结构，尝试超越文件夹与文件列表。 | 283 | 96 | 2021-08-05 |
| 10 | [Show HN: Pop.com – pair programming with low-latency, Screenhero-style sharing](https://news.ycombinator.com/item?id=28223515) | Pop.com 为结对编程提供低延迟、Screenhero 风格的屏幕共享。 | 225 | 125 | 2021-08-18 |

### 2021-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: 40k HN comments mentioning books, extracted using deep learning](https://news.ycombinator.com/item?id=28595967) | 借助深度学习整理四万条提及书籍的 HN 评论。 | 1359 | 273 | 2021-09-20 |
| 2 | [Show HN: Web browser to help programmers think clearly](https://news.ycombinator.com/item?id=28446147) | 一款旨在帮助程序员清晰思考的网页浏览器。 | 1070 | 226 | 2021-09-07 |
| 3 | [Show HN: Time travel debugger for web development](https://news.ycombinator.com/item?id=28539247) | 面向 Web 开发的时间旅行调试器，帮助回看程序执行状态。 | 681 | 216 | 2021-09-15 |
| 4 | [Show HN: Hacker News client with a twist](https://news.ycombinator.com/item?id=28704873) | 一个带有不同巧思的 Hacker News 客户端，探索社区阅读的新方式。 | 603 | 243 | 2021-09-30 |
| 5 | [Show HN: Age 1.0 – Simple, modern and secure file encryption](https://news.ycombinator.com/item?id=28435613) | Age 1.0 发布，作者以简单、现代和安全为目标设计文件加密。 | 494 | 88 | 2021-09-06 |
| 6 | [Show HN: Fully-searchable Library Genesis on IPFS](https://news.ycombinator.com/item?id=28585208) | 在 IPFS 上提供可全文搜索的 Library Genesis。 | 452 | 100 | 2021-09-19 |
| 7 | [Show HN: Weather API for non-commercial use](https://news.ycombinator.com/item?id=28499910) | 为非商业用途提供天气 API，便于应用接入天气数据。 | 443 | 147 | 2021-09-12 |
| 8 | [Show HN: I built four eight-foot-long handwriting robots](https://news.ycombinator.com/item?id=28587458) | 作者制作四台八英尺长的手写机器人，展示大尺寸书写装置。 | 408 | 164 | 2021-09-19 |
| 9 | [Show HN: Tidy Viewer – a cross-platform CSV pretty printer for viewer enjoyment](https://news.ycombinator.com/item?id=28670252) | Tidy Viewer 为 CSV 提供跨平台美化显示，改善终端阅读体验。 | 392 | 136 | 2021-09-27 |
| 10 | [Show HN: Medusa – Open-source alternative to Shopify](https://news.ycombinator.com/item?id=28481913) | Medusa 提供开源电商方案，尝试成为 Shopify 的替代选择。 | 373 | 80 | 2021-09-10 |

### 2021-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I built a fake VS Code to browse live cricket score in office](https://news.ycombinator.com/item?id=28985936) | 作者做了一个伪装成 VS Code 的页面，在办公室查看实时板球比分。 | 674 | 209 | 2021-10-25 |
| 2 | [Show HN: ChessCoach – A neural chess engine that comments on each player's moves](https://news.ycombinator.com/item?id=28765183) | ChessCoach 用神经网络下国际象棋，并点评双方每一步棋。 | 506 | 89 | 2021-10-05 |
| 3 | [Show HN: Coding Font – A game to find your favorite coding font](https://news.ycombinator.com/item?id=29010443) | Coding Font 通过游戏帮用户选出喜欢的编程字体。 | 443 | 218 | 2021-10-27 |
| 4 | [Show HN: CookLang – Recipe Markup Language](https://news.ycombinator.com/item?id=28997309) | CookLang 为食谱设计标记语言，让菜谱也能结构化编写。 | 415 | 146 | 2021-10-26 |
| 5 | [Show HN: A world map of 24x365 average temperature “fingerprints”](https://news.ycombinator.com/item?id=28845089) | 用世界地图展示全年逐小时平均气温，比较城市的温度“指纹”。 | 347 | 80 | 2021-10-12 |
| 6 | [Show HN: Identify car crash editorial anti-patterns using NLP](https://news.ycombinator.com/item?id=28840700) | 用自然语言处理识别车祸报道中的写作反模式。 | 344 | 205 | 2021-10-12 |
| 7 | [Show HN: I built a sonar into my surfboard](https://news.ycombinator.com/item?id=28901214) | 作者把声呐装进冲浪板，展示水上硬件改造。 | 332 | 91 | 2021-10-18 |
| 8 | [Show HN: SectorLISP now fits in one sector](https://news.ycombinator.com/item?id=29047584) | SectorLISP 缩小到一个扇区，探索 Lisp 实现的体积极限。 | 323 | 75 | 2021-10-30 |
| 9 | [Show HN: YoHa – A practical hand tracking engine](https://news.ycombinator.com/item?id=28825820) | YoHa 提供手部追踪引擎，面向实际交互应用。 | 292 | 64 | 2021-10-11 |
| 10 | [Show HN: “HTTP 419 Never Gonna Give You Up” for bots](https://news.ycombinator.com/item?id=29009935) | 给机器人返回“HTTP 419 Never Gonna Give You Up”，把反爬做成玩笑。 | 262 | 71 | 2021-10-27 |

### 2021-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: My wife is pregnant; naturally I made a baby-name app to prepare](https://news.ycombinator.com/item?id=29118785) | 准父亲为准备孩子出生制作了起名应用。 | 1077 | 372 | 2021-11-05 |
| 2 | [Show HN: I'm 48 and finally learning how to be a game developer](https://news.ycombinator.com/item?id=29167580) | 一位四十八岁的开发者分享终于开始学习游戏开发的经历。 | 985 | 252 | 2021-11-09 |
| 3 | [Show HN: Long Range E-Bike](https://news.ycombinator.com/item?id=29198205) | 长续航电动自行车项目展示，关注更远距离的骑行。 | 876 | 615 | 2021-11-12 |
| 4 | [Show HN: I made a Chrome extension that can automate any website](https://news.ycombinator.com/item?id=29254147) | 作者制作 Chrome 扩展，尝试自动操作各类网站。 | 707 | 209 | 2021-11-17 |
| 5 | [Show HN: Pony – a messenger for mindful correspondence](https://news.ycombinator.com/item?id=29278180) | Pony 为更用心的通信设计即时通讯工具。 | 693 | 238 | 2021-11-19 |
| 6 | [Show HN: I built a CNC-machine from scratch, using 40x 3D-printed parts](https://news.ycombinator.com/item?id=29096954) | 用四十个 3D 打印零件从零搭建 CNC 机床。 | 462 | 140 | 2021-11-03 |
| 7 | [Show HN: I built a no-BS recipe search engine](https://news.ycombinator.com/item?id=29161585) | 作者制作直截了当的食谱搜索引擎，希望减少找菜谱时的干扰。 | 403 | 207 | 2021-11-09 |
| 8 | [Show HN: Windows 2000 on Docker](https://news.ycombinator.com/item?id=29217622) | 在 Docker 中运行 Windows 2000，展示旧系统的新运行环境。 | 395 | 189 | 2021-11-14 |
| 9 | [Show HN: You.com, private search engine that summarizes the web – built for devs](https://news.ycombinator.com/item?id=29165601) | You.com 面向开发者提供注重隐私、可概括网页内容的搜索引擎。 | 361 | 459 | 2021-11-09 |
| 10 | [Show HN: Randomly create beautiful website layouts](https://news.ycombinator.com/item?id=29349079) | 随机生成漂亮的网站布局，借助组合探索设计可能。 | 317 | 89 | 2021-11-26 |

### 2021-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I made a modern web UI for Wikipedia](https://news.ycombinator.com/item?id=29461735) | 作者为维基百科制作现代 Web 界面，改善百科浏览体验。 | 979 | 409 | 2021-12-06 |
| 2 | [Show HN: Emoji to Scale](https://news.ycombinator.com/item?id=29425735) | Emoji to Scale 以比例展示表情符号，探索图标与真实尺度的关系。 | 713 | 124 | 2021-12-03 |
| 3 | [Show HN: Lisp with GC in 436 Bytes](https://news.ycombinator.com/item?id=29630293) | 用 436 字节实现带垃圾回收的 Lisp，挑战语言实现的精简程度。 | 513 | 131 | 2021-12-20 |
| 4 | [Show HN: I'm building a non-profit search engine](https://news.ycombinator.com/item?id=29690877) | 作者正在构建非营利搜索引擎，探索搜索服务的另一种组织方式。 | 441 | 199 | 2021-12-26 |
| 5 | [Show HN: Decentralized, Mutable, Serverless Torrent Swarm Websites](https://news.ycombinator.com/item?id=29513547) | 用种子群实现去中心化、可更新且无需服务器的网站。 | 433 | 186 | 2021-12-10 |
| 6 | [Show HN: Mum's 80th birthday present- a rotary phone from the 1970's](https://news.ycombinator.com/item?id=29620235) | 作者把七十年代旋转拨号电话送给母亲，作为八十岁生日礼物。 | 343 | 143 | 2021-12-20 |
| 7 | [Show HN: I wrote a book on web application deployment](https://news.ycombinator.com/item?id=29540808) | 一本讲 Web 应用部署的书，分享从开发走向上线的知识。 | 326 | 122 | 2021-12-13 |
| 8 | [Show HN: Voiceliner – Capture structured braindumps on the go](https://news.ycombinator.com/item?id=29726787) | Voiceliner 帮用户随时捕捉想法，并将语音记录组织成结构。 | 297 | 84 | 2021-12-29 |
| 9 | [Show HN: SlikSafe – A decentralized, end-to-end encrypted alternative to Dropbox](https://news.ycombinator.com/item?id=29637188) | SlikSafe 在本机加密后使用去中心化存储，提供 Dropbox 替代方案。 | 284 | 185 | 2021-12-21 |
| 10 | [Show HN: I rebuilt the Flash app “Scale of the Universe” in WebGL](https://news.ycombinator.com/item?id=29488511) | 作者用 WebGL 重建 Flash 作品《宇宙的尺度》。 | 276 | 79 | 2021-12-08 |

### 2022-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Looptap – A minimal game to waste your time](https://news.ycombinator.com/item?id=29921419) | Looptap 是一款适合打发时间的极简小游戏。 | 1241 | 170 | 2022-01-13 |
| 2 | [Show HN: Web page that parses and explains the label on a bike tire](https://news.ycombinator.com/item?id=30137984) | 更换自行车轮胎太难选，作者制作网页解释胎壁标签上的数字。 | 631 | 179 | 2022-01-30 |
| 3 | [Show HN: I bought and tested the filtration of every mask on Amazon](https://news.ycombinator.com/item?id=29878971) | 作者称自己买来并测试亚马逊上各类口罩，展示过滤性能调查。 | 594 | 237 | 2022-01-10 |
| 4 | [Show HN: BookStack – An open source wiki platform and alternative to Confluence](https://news.ycombinator.com/item?id=29851834) | BookStack 提供开源维基平台，尝试替代 Confluence。 | 562 | 198 | 2022-01-08 |
| 5 | [Show HN: OnlyRecipe.app – Remove clutter from recipe sites](https://news.ycombinator.com/item?id=29795482) | OnlyRecipe.app 清除食谱网页杂项，让用户直接查看做法。 | 560 | 345 | 2022-01-04 |
| 6 | [Show HN: Clone your voice and speak a foreign language](https://news.ycombinator.com/item?id=29786132) | 克隆自己的声音并说外语，展示语音生成与语言转换实验。 | 513 | 112 | 2022-01-03 |
| 7 | [Show HN: Login with HN (Unofficially)](https://news.ycombinator.com/item?id=29923736) | 非官方“使用 HN 登录”方案，探索社区身份的复用。 | 436 | 149 | 2022-01-13 |
| 8 | [Show HN: Create animations by dragging an element with your mouse](https://news.ycombinator.com/item?id=29924666) | 用鼠标拖动元素来制作动画，让动作直接成为编辑输入。 | 379 | 57 | 2022-01-13 |
| 9 | [Show HN: 3D map of shade around the world](https://news.ycombinator.com/item?id=29827943) | 用三维地图查看世界各地阴影，理解建筑和日照的空间关系。 | 368 | 71 | 2022-01-06 |
| 10 | [Show HN: API to query catalogs of 20 streaming services across 60 countries](https://news.ycombinator.com/item?id=29862588) | 通过 API 查询六十个国家、二十种流媒体服务的内容目录。 | 364 | 95 | 2022-01-09 |

### 2022-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: SHA-256 explained step-by-step visually](https://news.ycombinator.com/item?id=30244534) | 用逐步可视化演示解释 SHA-256 算法。 | 1241 | 137 | 2022-02-07 |
| 2 | [Show HN: EdgeDB 1.0](https://news.ycombinator.com/item?id=30290225) | EdgeDB 发布 1.0 版本，作者向社区展示数据库项目进展。 | 947 | 323 | 2022-02-10 |
| 3 | [Show HN: Full text search on 630M US court cases](https://news.ycombinator.com/item?id=30399881) | 为 6.3 亿条美国法院案件提供全文搜索。 | 698 | 269 | 2022-02-19 |
| 4 | [Show HN: Test your shape rotation skills](https://news.ycombinator.com/item?id=30408434) | 两分钟内寻找旋转后匹配的图形，测试自己的空间旋转能力。 | 659 | 195 | 2022-02-20 |
| 5 | [Show HN: Free and open-source illustrations for your projects](https://news.ycombinator.com/item?id=30332535) | 免费开源插画集合，为项目提供可以使用的视觉素材。 | 572 | 116 | 2022-02-14 |
| 6 | [Show HN: hue.tools – open-source toolbox for colors](https://news.ycombinator.com/item?id=30362112) | hue.tools 把常见颜色任务集中成开源工具箱，减少来回寻找工具。 | 481 | 80 | 2022-02-16 |
| 7 | [Show HN: A more social, Amazon-free alternative to Goodreads](https://news.ycombinator.com/item?id=30503197) | 作者希望建立更重社交、不依附亚马逊的 Goodreads 替代平台。 | 478 | 187 | 2022-02-28 |
| 8 | [Show HN: Simula One – Portable Linux VR Computer](https://news.ycombinator.com/item?id=30440828) | Simula One 是面向办公的便携 Linux VR 计算机，作者开放预订。 | 463 | 396 | 2022-02-23 |
| 9 | [Show HN: Jless, a command-line JSON viewer](https://news.ycombinator.com/item?id=30273940) | Jless 把浏览器式 JSON 折叠查看带到终端，并加入 Vim 风格按键。 | 344 | 84 | 2022-02-09 |
| 10 | [Show HN: Open-core icon sets that took me 12 years to create](https://news.ycombinator.com/item?id=30356944) | 花十二年打磨图标后，Streamline 作者开放多组图标供社区使用。 | 313 | 124 | 2022-02-16 |

### 2022-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I made a web game called Almost Pong](https://news.ycombinator.com/item?id=30517626) | 开发者展示完全由原生 JavaScript 生成画面与声音的 Almost Pong。 | 1135 | 181 | 2022-03-01 |
| 2 | [Show HN: I'm writing a free book called Computer Networks from Scratch](https://news.ycombinator.com/item?id=30824357) | 作者正在编写免费书《Computer Networks from Scratch》，从基础讲计算机网络。 | 792 | 132 | 2022-03-27 |
| 3 | [Show HN: HN Avatars in 357 bytes](https://news.ycombinator.com/item?id=30668137) | 用 357 字节代码给 HN 评论加头像，展示紧凑的页面增强脚本。 | 701 | 493 | 2022-03-14 |
| 4 | [Show HN: A game that tests how well you know your local area](https://news.ycombinator.com/item?id=30733339) | 一款检验本地熟悉程度的游戏，看看自己对身边的地方了解多少。 | 654 | 257 | 2022-03-19 |
| 5 | [Show HN: I made my personal website a Pokémon-style minigame using Phaser 3](https://news.ycombinator.com/item?id=30656961) | 用 Phaser 3 把个人网站做成宝可梦风格小游戏。 | 425 | 67 | 2022-03-13 |
| 6 | [Show HN: Bionic Reading – Formats text to make it faster to read](https://news.ycombinator.com/item?id=30787290) | Bionic Reading 调整文本格式，作者希望帮助用户更快阅读。 | 410 | 271 | 2022-03-24 |
| 7 | [Show HN: I made Devzat – It's like Discord but in the terminal, over SSH](https://news.ycombinator.com/item?id=30688691) | Devzat 通过 SSH 在终端聊天，支持频道、私信与代码高亮。 | 391 | 147 | 2022-03-15 |
| 8 | [Show HN: Search Engine for Blogs](https://news.ycombinator.com/item?id=30844149) | Blog Surf 为独立博客建立搜索入口，试图改善分散写作的发现问题。 | 389 | 93 | 2022-03-29 |
| 9 | [Show HN: Berkeley Mono Typeface](https://news.ycombinator.com/item?id=30557557) | Berkeley Mono 字体亮相，为等宽字体用户提供新的设计选择。 | 355 | 171 | 2022-03-04 |
| 10 | [Show HN: Huemint – Machine learning for color design](https://news.ycombinator.com/item?id=30529262) | Huemint 用机器学习辅助配色设计。 | 335 | 52 | 2022-03-02 |

### 2022-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Warp, a Rust-based terminal](https://news.ycombinator.com/item?id=30921231) | Warp 展示面向团队、基于 Rust 的终端并开放 Mac 公测。 | 946 | 726 | 2022-04-05 |
| 2 | [Show HN: Slow Social, a social network built for friends, not influencers](https://news.ycombinator.com/item?id=31054029) | Slow Social 为朋友间的交流设计社交网络，淡化网红式传播。 | 752 | 368 | 2022-04-16 |
| 3 | [Show HN: Make your PDF look scanned in browser](https://news.ycombinator.com/item?id=31083432) | 直接在浏览器里把 PDF 变成扫描件外观，无需后端服务器。 | 579 | 177 | 2022-04-19 |
| 4 | [Show HN: I built a simulator for personal finance](https://news.ycombinator.com/item?id=31083093) | 作者制作个人财务模拟器，帮助比较不同财务安排。 | 463 | 234 | 2022-04-19 |
| 5 | [Show HN: A plain-text file format for todos and check lists](https://news.ycombinator.com/item?id=30879327) | 用纯文本格式管理待办与检查清单，减少记忆工具命令的负担。 | 452 | 164 | 2022-04-01 |
| 6 | [Show HN: Redditle.com – For those of us who add 'Reddit' to every Google search](https://news.ycombinator.com/item?id=30946792) | Redditle.com 面向搜索时习惯加上“Reddit”的用户。 | 448 | 198 | 2022-04-07 |
| 7 | [Show HN: This AI Does Not Exist](https://news.ycombinator.com/item?id=31137324) | “This AI Does Not Exist”展示文本生成实验，作者同时说明服务运行挑战。 | 434 | 71 | 2022-04-23 |
| 8 | [Show HN: I made a website for you to travel the world in first-person POV](https://news.ycombinator.com/item?id=30970911) | 用第一人称视角在线环游世界，体验不同地点的街景与风景。 | 390 | 86 | 2022-04-09 |
| 9 | [Show HN: I made a puzzle game in HTML5](https://news.ycombinator.com/item?id=30956775) | 作者用 HTML5 制作益智游戏，邀请玩家体验。 | 368 | 124 | 2022-04-08 |
| 10 | [Show HN: Radiopaper – Troll-resistant public conversations](https://news.ycombinator.com/item?id=31210680) | Radiopaper 探索能够抵抗恶意搅扰的公开讨论平台。 | 346 | 323 | 2022-04-29 |

### 2022-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Mitmproxy2swagger – Automagically reverse-engineer REST APIs](https://news.ycombinator.com/item?id=31354130) | Mitmproxy2swagger 从流量中逆向 REST API，自动整理接口说明。 | 691 | 85 | 2022-05-12 |
| 2 | [Show HN: Can you lose at Wordle if you tried?](https://news.ycombinator.com/item?id=31572258) | 如果故意想输 Wordle 会有多难，作者把这个反向目标做成实验。 | 676 | 236 | 2022-05-31 |
| 3 | [Show HN: A Full-Stack Web Framework for Go](https://news.ycombinator.com/item?id=31371340) | Bud 是开源 Go 全栈 Web 框架，作者用 HN 克隆演示最小应用。 | 531 | 99 | 2022-05-13 |
| 4 | [Show HN: I turned my face rec system into a video codec](https://news.ycombinator.com/item?id=31516108) | 作者将原有的人脸识别系统改造成视频编解码器。 | 518 | 145 | 2022-05-26 |
| 5 | [Show HN: Bike – macOS Native Outliner](https://news.ycombinator.com/item?id=31409077) | Bike 是原生 macOS 大纲工具，重点探索连贯流动的文本编辑。 | 513 | 236 | 2022-05-17 |
| 6 | [Show HN: A Visual IDE for React](https://news.ycombinator.com/item?id=31364081) | React 可视化 IDE 帮用户直接调整界面，减少代码与浏览器间的切换。 | 479 | 134 | 2022-05-13 |
| 7 | [Show HN: 1,900 remote company profiles with tech stacks and employee benefits](https://news.ycombinator.com/item?id=31335904) | 整理一千九百家远程公司的介绍，涵盖技术栈和员工福利。 | 457 | 173 | 2022-05-11 |
| 8 | [Show HN: PostgresML, now with analytics and project management](https://news.ycombinator.com/item?id=31238396) | PostgresML 为数据库旁的机器学习加入分析与项目管理功能。 | 444 | 70 | 2022-05-02 |
| 9 | [Show HN: Tetris, but silly](https://news.ycombinator.com/item?id=31275476) | 一个故意做得滑稽的俄罗斯方块实验，作者征求能否发展成游戏的意见。 | 389 | 96 | 2022-05-05 |
| 10 | [Show HN: I am building a free version of Strava](https://news.ycombinator.com/item?id=31238958) | Hangtime 为山地骑行加入路段功能，作者希望做免费的 Strava 替代品。 | 311 | 92 | 2022-05-02 |

### 2022-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: A friend and I spent 6 years making a simulation game, finally released](https://news.ycombinator.com/item?id=31586833) | 两位朋友分享六年研发模拟游戏、辞职投入并终于发布的经历。 | 1157 | 279 | 2022-06-01 |
| 2 | [Show HN: A central bank simulator game with a realistic economic model](https://news.ycombinator.com/item?id=31785199) | 中央银行模拟游戏采用现实经济模型，让玩家尝试货币政策决策。 | 815 | 309 | 2022-06-17 |
| 3 | [Show HN: I stripped DALL·E Mini to its bare essentials and converted it to Torch](https://news.ycombinator.com/item?id=31903076) | 作者精简 DALL·E Mini，并将其转换到 Torch。 | 663 | 148 | 2022-06-28 |
| 4 | [Show HN: Calculator for US individual income tax, from 1970-present](https://news.ycombinator.com/item?id=31925871) | 在浏览器中估算美国个人所得税，计算范围从 1970 年延续至今。 | 497 | 155 | 2022-06-29 |
| 5 | [Show HN: I restored Palm's webOS App Catalog, SDK and online help system](https://news.ycombinator.com/item?id=31607318) | 搜集散落的存档，恢复 Palm webOS 应用目录、SDK 与在线帮助。 | 439 | 140 | 2022-06-03 |
| 6 | [Show HN: PRQL 0.2 – a better SQL](https://news.ycombinator.com/item?id=31897430) | PRQL 0.2 发布，作者希望提供更好的 SQL 编写方式，并支持实际项目使用。 | 378 | 159 | 2022-06-27 |
| 7 | [Show HN: Markwhen: Markdown for Timelines](https://news.ycombinator.com/item?id=31810876) | Markwhen 用类似 Markdown 的文字形式编写时间线。 | 370 | 90 | 2022-06-20 |
| 8 | [Show HN: Svelvet – A component library for building interactive flow diagrams](https://news.ycombinator.com/item?id=31595822) | Svelvet 提供组件库，方便搭建可交互的流程图。 | 354 | 91 | 2022-06-02 |
| 9 | [Show HN: The Bitcoin Note – Secure, Self-Custodial Bitcoin Wallets in Cash Form](https://news.ycombinator.com/item?id=31653726) | The Bitcoin Note 把自托管比特币钱包做成现金形态。 | 344 | 465 | 2022-06-07 |
| 10 | [Show HN: Read Wikipedia privately using homomorphic encryption](https://news.ycombinator.com/item?id=31668814) | 利用同态加密私密阅读维基百科，探索查询内容的隐私保护。 | 331 | 116 | 2022-06-08 |

### 2022-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Porting OpenBSD Pledge() to Linux](https://news.ycombinator.com/item?id=32096801) | 将 OpenBSD 的 pledge() 移植到 Linux，探索程序权限约束。 | 571 | 128 | 2022-07-14 |
| 2 | [Show HN: PocketBase – Open Source realtime backend in one file](https://news.ycombinator.com/item?id=32013330) | PocketBase 把开源实时后端装进单个文件。 | 563 | 111 | 2022-07-07 |
| 3 | [Show HN: Pipes puzzle (a.k.a. Net) on a hexagonal grid](https://news.ycombinator.com/item?id=32216436) | 把接水管谜题放到六边形网格，旋转拼块恢复完整连接。 | 537 | 161 | 2022-07-24 |
| 4 | [Show HN: Parsnip – Duolingo for Cooking](https://news.ycombinator.com/item?id=32266086) | Parsnip 借鉴多邻国，用技能树与进度记录学习烹饪基础。 | 536 | 365 | 2022-07-28 |
| 5 | [Show HN: Inflation-adjusted stock charts – Total Real Returns](https://news.ycombinator.com/item?id=32081943) | 股票图表计入通胀影响，帮助观察实际购买力意义上的回报。 | 507 | 272 | 2022-07-13 |
| 6 | [Show HN: I built an app for when I talk too much in online meetings](https://news.ycombinator.com/item?id=32095592) | 在线会议说得太多，作者制作应用来观察并改善自己的发言习惯。 | 451 | 189 | 2022-07-14 |
| 7 | [Show HN: I've been making JavaScript sandbox alone for 6 years](https://news.ycombinator.com/item?id=32293178) | 独自制作 JavaScript 沙盒六年，作者分享浏览器运行 Node.js 包的历程。 | 397 | 102 | 2022-07-31 |
| 8 | [Show HN: tere – A Faster Alternative to cd+ls](https://news.ycombinator.com/item?id=32106126) | tere 为终端提供简洁目录浏览，尝试加快 cd 加 ls 的操作。 | 378 | 198 | 2022-07-15 |
| 9 | [Show HN: Copy React code from any site](https://news.ycombinator.com/item?id=32037740) | 从网站复制 React 代码，作者希望减少重复搭建已有界面。 | 374 | 72 | 2022-07-09 |
| 10 | [Show HN: Ants Sandbox - an ants simulator](https://news.ycombinator.com/item?id=32043229) | Ants Sandbox 在网页里模拟蚂蚁，观察群体活动的过程。 | 367 | 61 | 2022-07-10 |

### 2022-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Pornpen.ai – AI-Generated Porn](https://news.ycombinator.com/item?id=32572770) | Pornpen.ai 用文生图模型生成成人图像，作者将其作为生成式 AI 实验。 | 711 | 414 | 2022-08-23 |
| 2 | [Show HN: Devbox – Easy, predictable shells and containers](https://news.ycombinator.com/item?id=32600821) | Devbox 根据包清单创建隔离 Shell 与容器，让开发环境更可预测。 | 515 | 185 | 2022-08-25 |
| 3 | [Show HN: AutoHotkey for Linux](https://news.ycombinator.com/item?id=32654023) | 在 Linux 等类 Unix 系统重新实现 AutoHotkey，作者分享首个可用版本。 | 500 | 183 | 2022-08-30 |
| 4 | [Show HN: I made a web-based notepad with a built in unit calculator](https://news.ycombinator.com/item?id=32493946) | 网页记事本内置单位计算器，还能处理百分比、日期和变量。 | 488 | 239 | 2022-08-17 |
| 5 | [Show HN: Reduce SQLite database size by up to 80% with transparent compression](https://news.ycombinator.com/item?id=32303762) | 通过透明压缩缩小 SQLite 数据库，作者称体积最多可减少八成。 | 420 | 90 | 2022-08-01 |
| 6 | [Show HN: Figure is a daily logic puzzle game](https://news.ycombinator.com/item?id=32376154) | Figure 提供每日逻辑谜题，尝试结合消除游戏与 Wordle 式体验。 | 417 | 113 | 2022-08-07 |
| 7 | [Show HN: I built a tool to help you read Hacker News on Kindle](https://news.ycombinator.com/item?id=32637996) | KTool 帮用户在 Kindle 上读 HN，作者的视力经历促成了这个想法。 | 393 | 78 | 2022-08-29 |
| 8 | [Show HN: Adadot – analytics for better, happier developers](https://news.ycombinator.com/item?id=32331359) | Adadot 用数据分析辅助开发者改善工作，作者同时关注效率与幸福感。 | 325 | 16 | 2022-08-03 |
| 9 | [Show HN: A VNC viewer for eInk devices capable of 30 FPS when writing text](https://news.ycombinator.com/item?id=32449857) | 面向电子墨水设备的 VNC 查看器，作者称输入文字时可达每秒三十帧。 | 303 | 96 | 2022-08-13 |
| 10 | [Show HN: Crawlee – Web scraping and browser automation library for Node.js](https://news.ycombinator.com/item?id=32561127) | Crawlee 汇集团队的抓取经验，为 Node.js 提供网页抓取和浏览器自动化库。 | 282 | 80 | 2022-08-23 |

### 2022-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I may have created a new type of puzzle](https://news.ycombinator.com/item?id=32884467) | 开发者展示自己认为可能是一种新类型的谜题。 | 1859 | 464 | 2022-09-18 |
| 2 | [Show HN: I'm building an open-source Amazon](https://news.ycombinator.com/item?id=32690410) | 开发者构建开源电商平台，希望商家脱离平台后仍保留基础设施。 | 1335 | 301 | 2022-09-02 |
| 3 | [Show HN: Get conversational practice in over 20 languages by talking to an AI](https://news.ycombinator.com/item?id=32993130) | Quazel 通过与 AI 对话练习二十多种语言，补充语言应用里的口语训练。 | 787 | 335 | 2022-09-27 |
| 4 | [Show HN: Quake 1 ported to the Apple Watch](https://news.ycombinator.com/item?id=32747067) | 把《雷神之锤》移植到 Apple Watch，用触摸、陀螺仪和表冠操控。 | 692 | 216 | 2022-09-07 |
| 5 | [Show HN: Wavvy – web-based audio editor (Audacity port)](https://news.ycombinator.com/item?id=32688646) | Wavvy 把 Audacity 移植到网页，探索复杂音频编辑器的 WebAssembly 运行。 | 530 | 111 | 2022-09-02 |
| 6 | [Show HN: Zelda Breath of The Wild Street View](https://news.ycombinator.com/item?id=32717133) | 用街景方式探索《塞尔达传说：旷野之息》的世界。 | 456 | 88 | 2022-09-04 |
| 7 | [Show HN: I made a modern web UI for Hacker News](https://news.ycombinator.com/item?id=32768590) | 浏览器扩展为 Hacker News 换上现代界面，作者延续维基百科改版经验。 | 308 | 198 | 2022-09-08 |
| 8 | [Show HN: Open Prompts – dataset of 10M Stable Diffusion generations](https://news.ycombinator.com/item?id=32943224) | Open Prompts 公开千万级 Stable Diffusion 生成数据，用于研究提示词与图像。 | 279 | 71 | 2022-09-22 |
| 9 | [Show HN: Figr.app – a multi-user, notepad style calculator (desktop app)](https://news.ycombinator.com/item?id=32905802) | Figr.app 将多人记事本式计算器带到桌面，回应用户对原生应用的需求。 | 275 | 87 | 2022-09-19 |
| 10 | [Show HN: HiFiScan, a Python app to optimize your loudspeakers](https://news.ycombinator.com/item?id=32798891) | HiFiScan 用 Python 帮助优化扬声器的声音表现。 | 260 | 103 | 2022-09-11 |

### 2022-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I 3D scanned the interior of the Great Pyramid at Giza](https://news.ycombinator.com/item?id=33357197) | 作者展示吉萨大金字塔内部三维扫描及在线导览。 | 1752 | 280 | 2022-10-27 |
| 2 | [Show HN: Restfox – Open source lightweight alternative to Postman](https://news.ycombinator.com/item?id=33287137) | Restfox 是开源轻量 API 调试工具，可在浏览器和离线环境中运行。 | 758 | 182 | 2022-10-21 |
| 3 | [Show HN: America – Road Trip Simulator](https://news.ycombinator.com/item?id=33217395) | America 用多个 API 拼出公路旅行模拟，沿途听电台、看照片与本地信息。 | 663 | 183 | 2022-10-15 |
| 4 | [Show HN: SadServers – Test your Linux troubleshooting skills](https://news.ycombinator.com/item?id=33344142) | SadServers 在真实 Linux 服务器上设置故障，测试用户的排障能力。 | 597 | 128 | 2022-10-26 |
| 5 | [Show HN: A new search engine UX I've been working on in my free time](https://news.ycombinator.com/item?id=33251954) | 作者用业余时间探索新的搜索引擎交互，展示不同的搜索体验。 | 572 | 334 | 2022-10-18 |
| 6 | [Show HN: SigNoz – open-source alternative to DataDog, NewRelic](https://news.ycombinator.com/item?id=33049046) | SigNoz 提供开源可观测性工具，尝试替代 DataDog 与 New Relic。 | 510 | 132 | 2022-10-01 |
| 7 | [Show HN: I made a new AI colorizer](https://news.ycombinator.com/item?id=33261494) | Palette 用 AI 为图像上色，还可用自然语言修改上色效果。 | 472 | 120 | 2022-10-19 |
| 8 | [Show HN: InvokeAI, an open source Stable Diffusion toolkit and WebUI](https://news.ycombinator.com/item?id=33155074) | InvokeAI 为 Stable Diffusion 提供开源创作工具与网页界面。 | 414 | 102 | 2022-10-10 |
| 9 | [Show HN: Minimal, no-JS web forum software](https://news.ycombinator.com/item?id=33153152) | 不用 JavaScript 的极简论坛，采用 SQLite 并以便于自托管为目标。 | 392 | 155 | 2022-10-10 |
| 10 | [Show HN: I finished v5 of a JVM framework I've spent spent half a decade making](https://news.ycombinator.com/item?id=33068017) | 开发 JVM 框架五年后，作者分享第五版成果。 | 377 | 136 | 2022-10-03 |

### 2022-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Trading cards made with e-ink displays](https://news.ycombinator.com/item?id=33795296) | 开发者展示用电子墨水屏制作、可以动态更换内容的集换卡。 | 1149 | 291 | 2022-11-30 |
| 2 | [Show HN: A color picker for named web colors](https://news.ycombinator.com/item?id=33693411) | 为 Web 命名颜色设计取色器，方便在现成色名间选择。 | 731 | 169 | 2022-11-21 |
| 3 | [Show HN: Using stylometry to find HN users with alternate accounts](https://news.ycombinator.com/item?id=33755016) | 用文体统计方法寻找 HN 用户的小号，探索文字风格与身份的关系。 | 676 | 511 | 2022-11-26 |
| 4 | [Show HN: I made a pretty relaxing puzzle game](https://news.ycombinator.com/item?id=33718124) | 作者把 HTML、CSS 原型发展成轻松益智游戏，并加入计步与分享。 | 633 | 167 | 2022-11-23 |
| 5 | [Show HN: I built my own PM tool after trying Trello, Asana, ClickUp, etc.](https://news.ycombinator.com/item?id=33582264) | 试用多种项目管理工具后，作者自制 Upbase，追求完整而不过度复杂。 | 632 | 453 | 2022-11-13 |
| 6 | [Show HN: Haxophone](https://news.ycombinator.com/item?id=33682813) | Haxophone 把萨克斯、Rust、机械键盘与树莓派结合成自制项目。 | 526 | 71 | 2022-11-20 |
| 7 | [Show HN: A tool to help you remember shit you are interested in](https://news.ycombinator.com/item?id=33425947) | Recall 帮用户记住感兴趣的内容，作者发布新版并询问是否值得继续。 | 493 | 173 | 2022-11-01 |
| 8 | [Show HN: I made an offline-ready hiking trail companion app](https://news.ycombinator.com/item?id=33420852) | 徒步训练催生离线路线伴侣，作者希望低耗电地记录沿途进度。 | 475 | 141 | 2022-11-01 |
| 9 | [Show HN: Wa-tunnel – HTTP Tunneling through Whatsapp](https://news.ycombinator.com/item?id=33568994) | Wa-tunnel 通过 WhatsApp 为 TCP 端口建立隧道，探索社交数据通道的用途。 | 453 | 123 | 2022-11-12 |
| 10 | [Show HN: Cozo – new Graph DB with Datalog, embedded like SQLite](https://news.ycombinator.com/item?id=33518320) | Cozo 将 Datalog 图数据库做成类似 SQLite 的嵌入式工具。 | 425 | 67 | 2022-11-08 |

### 2022-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Obsidian Canvas – An infinite space for your ideas](https://news.ycombinator.com/item?id=34066824) | Obsidian Canvas 提供组织想法的无限画布。 | 1380 | 387 | 2022-12-20 |
| 2 | [Show HN: I store my critical secrets and document, and communicate privately](https://news.ycombinator.com/item?id=34083366) | 开发者展示保存关键秘密、文档及开展私密交流的工具。 | 1290 | 376 | 2022-12-21 |
| 3 | [Show HN: I wrote a free eBook about many lesser-known/secret database tricks](https://news.ycombinator.com/item?id=33833836) | 作者免费分享电子书，整理不太为人熟知的数据库技巧。 | 865 | 174 | 2022-12-02 |
| 4 | [Show HN: I made an Ethernet transceiver from logic gates](https://news.ycombinator.com/item?id=34035628) | 从逻辑门搭出以太网收发器，展示网络硬件的底层实现。 | 460 | 85 | 2022-12-18 |
| 5 | [Show HN: Pole Clock, a single 24h clock with multiple timezones](https://news.ycombinator.com/item?id=34196340) | Pole Clock 用同一个二十四小时钟面显示多个时区。 | 440 | 165 | 2022-12-31 |
| 6 | [Show HN: Browser extension to display ChatGPT response besides Google Search](https://news.ycombinator.com/item?id=33853773) | 浏览器扩展在 Google 搜索旁显示 ChatGPT 回答，方便同时查看。 | 431 | 149 | 2022-12-04 |
| 7 | [Show HN: My Child's First Program](https://news.ycombinator.com/item?id=33881857) | 作者分享孩子写出第一个 Python 程序的经历，记录简单输出如何点燃编程兴趣。 | 417 | 136 | 2022-12-06 |
| 8 | [Show HN: Port of OpenAI's Whisper model in C/C++](https://news.ycombinator.com/item?id=33877893) | 把 Whisper 语音识别模型移植到 C 与 C++。 | 399 | 87 | 2022-12-06 |
| 9 | [Show HN: Built your front end in React, then let ChatGPT be you Redux reducer](https://news.ycombinator.com/item?id=34166193) | 尝试让 ChatGPT 充当 Redux reducer，用语言模型参与 React 应用的状态变化。 | 395 | 137 | 2022-12-28 |
| 10 | [Show HN: LearnGPT – Browse and share ChatGPT examples](https://news.ycombinator.com/item?id=33923907) | LearnGPT 收集可浏览、可分享的 ChatGPT 使用示例。 | 352 | 104 | 2022-12-09 |

### 2023-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I've built a C# IDE, Runtime, and AppStore inside Excel](https://news.ycombinator.com/item?id=34516366) | 在 Excel 里面构建 C# IDE、运行环境与应用商店。 | 670 | 179 | 2023-01-25 |
| 2 | [Show HN: I'm a doctor and made a responsive breathing app for stress and anxiety](https://news.ycombinator.com/item?id=34534615) | 一位医生制作响应式呼吸练习应用，希望辅助应对压力与焦虑。 | 666 | 215 | 2023-01-26 |
| 3 | [Show HN: Kandria, an action RPG made in Common Lisp is now out](https://news.ycombinator.com/item?id=34338629) | Kandria 正式发布：用 Common Lisp 制作开放世界动作 RPG 平台游戏。 | 487 | 127 | 2023-01-11 |
| 4 | [Show HN: I “wrote” a kids book with ChatGPT and Midjourney](https://news.ycombinator.com/item?id=34514480) | 作者用朋友提供的情节、ChatGPT 文字和 Midjourney 插画制作儿童书。 | 417 | 394 | 2023-01-25 |
| 5 | [Show HN: A 100% free and interactive Python course for coding beginners](https://news.ycombinator.com/item?id=34289581) | 免费开源 Python 交互课程，无需账号即可开始练习编程。 | 371 | 78 | 2023-01-07 |
| 6 | [Show HN: How to create a 3D space using CSS](https://news.ycombinator.com/item?id=34315380) | 用 CSS 创建三维空间的演示，探索网页样式与空间变换的表现力。 | 370 | 94 | 2023-01-09 |
| 7 | [Show HN: I spent 2 years building Tablane as a 17-year-old](https://news.ycombinator.com/item?id=34279062) | 17 岁作者花两年开发 Tablane，把协作编辑与实时同步用于任务管理。 | 352 | 184 | 2023-01-06 |
| 8 | [Show HN: Val Town – A Cloud Scripting Site](https://news.ycombinator.com/item?id=34343122) | Val Town 让用户在浏览器写云端函数，快速运行、生成接口并设置定时。 | 332 | 71 | 2023-01-11 |
| 9 | [Show HN: A device that only lets you type lol if you've truly laughed out loud](https://news.ycombinator.com/item?id=34237195) | 只有真的笑出声才能输入“lol”，作者把网络表达做成硬件约束。 | 321 | 85 | 2023-01-03 |
| 10 | [Show HN: Automatisch – Open source workflow automation, an alternative to Zapier](https://news.ycombinator.com/item?id=34519639) | Automatisch 用开源工作流自动化工具，尝试替代 Zapier。 | 317 | 58 | 2023-01-25 |

### 2023-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: The largest collection of ChatGPT jailbreaks on the internet](https://news.ycombinator.com/item?id=34972791) | 开发者展示收集并跟踪 ChatGPT 越狱提示词的网站。 | 1118 | 528 | 2023-02-28 |
| 2 | [Show HN: I trained an AI model on 120M+ songs from iTunes](https://news.ycombinator.com/item?id=34635352) | Maroofy 根据歌曲声音寻找相似音乐，作者索引了逾一亿首 iTunes 歌曲。 | 753 | 427 | 2023-02-03 |
| 3 | [Show HN: We built a developer-first open-source Zapier alternative](https://news.ycombinator.com/item?id=34610686) | Trigger.dev 让开发者在代码中编写事件驱动后台任务，提供开源自动化方案。 | 745 | 190 | 2023-02-01 |
| 4 | [Show HN: Turn Your Pandas Dataframe into a Tableau-Style UI for Visual Analysis](https://news.ycombinator.com/item?id=34869244) | PyGWalker 把 Pandas 数据框变成 Tableau 风格界面，通过拖拽探索数据。 | 712 | 61 | 2023-02-20 |
| 5 | [Show HN: Filmbox, physically accurate film emulation, now on Linux and Windows](https://news.ycombinator.com/item?id=34713202) | Filmbox 将物理胶片模拟扩展到 Linux 与 Windows。 | 658 | 248 | 2023-02-08 |
| 6 | [Show HN: AskHN](https://news.ycombinator.com/item?id=34897773) | 名为 AskHN 的项目亮相，作者邀请社区了解自己的作品。 | 612 | 127 | 2023-02-22 |
| 7 | [Show HN: I made a tool that turns screenshots into dramatically angled photos](https://news.ycombinator.com/item?id=34729849) | 把普通截图转成带强烈透视角度的照片，改善展示素材效果。 | 497 | 226 | 2023-02-09 |
| 8 | [Show HN: Kuboble.com – minimalistic sliding pieces puzzle game](https://news.ycombinator.com/item?id=34706098) | Kuboble 用极简界面与滑块规则制作益智关卡，强调流畅与挑战性。 | 437 | 155 | 2023-02-08 |
| 9 | [Show HN: We’re open-sourcing our session replay tool](https://news.ycombinator.com/item?id=34897645) | Highlight.io 开源会话回放与错误监控，帮助看到网页出错前的用户操作。 | 408 | 71 | 2023-02-22 |
| 10 | [Show HN: Glidesort, a new stable sort in Rust up to ~4x faster for random data](https://news.ycombinator.com/item?id=34646199) | Glidesort 用 Rust 实现稳定排序，作者报告随机数据上最高约四倍加速。 | 389 | 70 | 2023-02-03 |

### 2023-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: BBC “In Our Time”, categorised by Dewey Decimal, heavy lifting by GPT](https://news.ycombinator.com/item?id=35073603) | 借助 GPT 按杜威分类整理 BBC《In Our Time》，让近千集节目更好查找。 | 688 | 171 | 2023-03-08 |
| 2 | [Show HN: Alpaca.cpp – Run an Instruction-Tuned Chat-Style LLM on a MacBook](https://news.ycombinator.com/item?id=35184985) | Alpaca.cpp 让经过指令微调的对话语言模型在 MacBook 上运行。 | 673 | 283 | 2023-03-16 |
| 3 | [Show HN: Lander, a lunar lander style web game](https://news.ycombinator.com/item?id=35032506) | Lander 在网页里重现月球着陆类游戏，考验操控与落地时机。 | 564 | 170 | 2023-03-05 |
| 4 | [Show HN: Apple Notes Liberator – Extract Notes.app Data and Save It as JSON](https://news.ycombinator.com/item?id=35316679) | Apple Notes Liberator 提取备忘录数据并保存为 JSON，方便迁移与处理。 | 563 | 105 | 2023-03-26 |
| 5 | [Show HN: Yesterday I open sourced StratusGFX, a realtime 3D rendering engine](https://news.ycombinator.com/item?id=35370284) | StratusGFX 从长期业余研究项目转为开源，分享实时三维渲染引擎。 | 483 | 82 | 2023-03-30 |
| 6 | [Show HN: Finetune LLaMA-7B on commodity GPUs using your own text](https://news.ycombinator.com/item?id=35256769) | 通过简单界面粘贴自己的文本，在普通 GPU 上微调 LLaMA-7B。 | 449 | 98 | 2023-03-22 |
| 7 | [Show HN: ChatLLaMA – A ChatGPT style chatbot for Facebook's LLaMA](https://news.ycombinator.com/item?id=35258553) | ChatLLaMA 为 LLaMA 变体提供聊天界面，作者说明目前仍是早期实验。 | 402 | 215 | 2023-03-22 |
| 8 | [Show HN: GPT Repo Loader – load entire code repos into GPT prompts](https://news.ycombinator.com/item?id=35191303) | GPT Repo Loader 将代码仓库整理成提示词友好的路径和内容格式。 | 373 | 149 | 2023-03-17 |
| 9 | [Show HN: Multi-Display Screen Sharing with CoScreen by Datadog](https://news.ycombinator.com/item?id=35387160) | CoScreen 5.0 支持同时共享多个显示器上的窗口，改善远程协作。 | 350 | 107 | 2023-03-31 |
| 10 | [Show HN: Llama-dl – high-speed download of LLaMA, Facebook's 65B GPT model](https://news.ycombinator.com/item?id=35026902) | Llama-dl 提供 LLaMA 模型下载工具，作者强调下载速度。 | 343 | 130 | 2023-03-05 |

### 2023-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: GPT-4-powered web searches for developers](https://news.ycombinator.com/item?id=35543668) | Phind 为开发者搜索引入 GPT-4，并结合网页和文档生成回答。 | 1401 | 414 | 2023-04-12 |
| 2 | [Show HN: Unknown Pleasures, a tiny web experiment with WebGL](https://news.ycombinator.com/item?id=35419771) | Unknown Pleasures 是一个小型 WebGL 网页实验。 | 661 | 115 | 2023-04-03 |
| 3 | [Show HN: Tabby – A Self-Hosted GitHub Copilot](https://news.ycombinator.com/item?id=35470915) | Tabby 提供可自行托管的代码辅助工具，尝试替代 GitHub Copilot。 | 627 | 126 | 2023-04-06 |
| 4 | [Show HN: A 15 min daily stretch routine for desk workers](https://news.ycombinator.com/item?id=35639810) | 给久坐办公者的每日十五分钟拉伸安排，帮助建立运动习惯。 | 550 | 129 | 2023-04-20 |
| 5 | [Show HN: I made a SQL game to help people learn / challenge their skills](https://news.ycombinator.com/item?id=35665142) | 作者把 SQL 学习做成游戏，让用户边玩边检验查询能力。 | 547 | 117 | 2023-04-22 |
| 6 | [Show HN: ScrapScript – The Sharable Programming Language](https://news.ycombinator.com/item?id=35712163) | ScrapScript 以可分享为目标设计编程语言，作者介绍多年探索后的方案。 | 503 | 135 | 2023-04-26 |
| 7 | [Show HN: We are building open-source IDE powered by AI agents that work for you](https://news.ycombinator.com/item?id=35440552) | 团队正在构建开源 IDE，尝试让 AI 代理代用户完成开发工作。 | 369 | 175 | 2023-04-04 |
| 8 | [Show HN: ADHD-friendly pomodoro web app](https://news.ycombinator.com/item?id=35471129) | 面向 ADHD 使用习惯设计的番茄钟网页应用。 | 329 | 129 | 2023-04-06 |
| 9 | [Show HN: Live coaching app for remote SWE interviews, uses Whisper and GPT-4](https://news.ycombinator.com/item?id=35447288) | 用 Whisper 与 GPT-4 为远程软件工程面试提供实时辅导。 | 301 | 114 | 2023-04-04 |
| 10 | [Show HN: Hocus – self-hosted alternative to GitHub Codespaces using Firecracker](https://news.ycombinator.com/item?id=35427343) | Hocus 用 Firecracker 构建可自托管的 GitHub Codespaces 替代方案。 | 291 | 53 | 2023-04-03 |

### 2023-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Boring Report, a news app that uses AI to desensationalize the news](https://news.ycombinator.com/item?id=35905437) | Boring Report 用语言模型去除新闻煽情措辞，帮助读者聚焦事实。 | 1166 | 332 | 2023-05-11 |
| 2 | [Show HN: Beepberry – a portable e-paper computer for hackers](https://news.ycombinator.com/item?id=35976488) | Beepberry 是便携电子纸计算机，作者最初想用它在 Beeper 上聊天。 | 731 | 227 | 2023-05-17 |
| 3 | [Show HN: I open sourced the QR designer from my failed startup](https://news.ycombinator.com/item?id=36128082) | 创业失败后开源二维码设计器，支持在中央加入仍可扫描的自定义设计。 | 711 | 73 | 2023-05-30 |
| 4 | [Show HN: Willow – Open-Source Privacy-Focused Voice Assistant Hardware](https://news.ycombinator.com/item?id=35948462) | Willow 用开源硬件打造注重隐私的语音助手，连接 Home Assistant 等平台。 | 581 | 138 | 2023-05-15 |
| 5 | [Show HN: YouTube Full Text Search – Search all of a channel from the commandline](https://news.ycombinator.com/item?id=36009774) | 抓取 YouTube 频道字幕并存入 SQLite，在命令行全文搜索并跳到时间点。 | 540 | 165 | 2023-05-20 |
| 6 | [Show HN: Image background removal without annoying subscriptions](https://news.ycombinator.com/item?id=36064639) | 提供无需订阅的图片背景移除工具，回应常见抠图需求。 | 383 | 115 | 2023-05-24 |
| 7 | [Show HN: I'm open sourcing Harmonic, the Android Hacker News client](https://news.ycombinator.com/item?id=36047143) | 作者开源 Harmonic，将 Android 上的 Hacker News 客户端分享给社区。 | 305 | 98 | 2023-05-23 |
| 8 | [Show HN: Visual intuitive explanations of LLM concepts (LLM University)](https://news.ycombinator.com/item?id=36070090) | LLM University 免费用图解、文章和代码讲解大语言模型概念。 | 303 | 36 | 2023-05-25 |
| 9 | [Show HN: A search engine for your personal network of high-quality websites](https://news.ycombinator.com/item?id=35826540) | Grasp 为用户挑选的优质网站建立个人搜索网络，并尝试直接回答问题。 | 266 | 100 | 2023-05-05 |
| 10 | [Show HN: I created a game to memorize the fretboard](https://news.ycombinator.com/item?id=36084503) | 为突破吉他指板不熟的瓶颈，作者做游戏帮助记忆音符位置。 | 258 | 141 | 2023-05-26 |

### 2023-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Content-aware fill for audio to change a song to any duration](https://news.ycombinator.com/item?id=36480687) | 分析歌曲中的重复结构，按目标时长延长或缩短音频以适配视频。 | 708 | 161 | 2023-06-26 |
| 2 | [Show HN: Rarbg on IPFS](https://news.ycombinator.com/item?id=36186185) | 把 Rarbg 放到 IPFS 上，展示去中心化内容存档项目。 | 704 | 128 | 2023-06-04 |
| 3 | [Show HN: Open-source resume builder and parser](https://news.ycombinator.com/item?id=36470297) | 辅导学生时发现简历常见问题，作者制作开源简历生成与解析工具。 | 656 | 198 | 2023-06-25 |
| 4 | [Show HN: 77 Year old launches SaaS platform today. Seeks feedback](https://news.ycombinator.com/item?id=36365511) | 77 岁作者推出 PropBox，希望让买卖双方在线协商房产交易且免佣金。 | 520 | 273 | 2023-06-16 |
| 5 | [Show HN: I made CSS Pro, a re-imagined Devtools for web design](https://news.ycombinator.com/item?id=36148807) | CSS Pro 重新设计面向网页设计的开发者工具。 | 505 | 288 | 2023-06-01 |
| 6 | [Show HN: I've built open-source, collaborative, WYSIWYG Markdown editor](https://news.ycombinator.com/item?id=36446045) | 受 Notion 与 StackEdit 启发，作者制作开源协作式所见即所得 Markdown 编辑器。 | 460 | 128 | 2023-06-23 |
| 7 | [Show HN: Open-source background removal in the browser](https://news.ycombinator.com/item?id=36505859) | 开源 JavaScript 库直接在浏览器移除图片背景，减少图像上传需求。 | 395 | 38 | 2023-06-28 |
| 8 | [Show HN: WinGPT, AI Assistant for Windows 3.1](https://news.ycombinator.com/item?id=36472854) | 为 1993 年的老电脑接入 AI，作者制作 Windows 3.1 助手 WinGPT。 | 382 | 90 | 2023-06-25 |
| 9 | [Show HN: I made an open-source Notion-style WYSYWIG editor](https://news.ycombinator.com/item?id=36360789) | 一个开源 Notion 风格所见即所得编辑器，方便直接编辑内容。 | 370 | 133 | 2023-06-16 |
| 10 | [Show HN: Indexing Discord content into the web – Answer Overflow](https://news.ycombinator.com/item?id=36383773) | Answer Overflow 将 Discord 频道内容索引到网页，让搜索引擎能够发现答案。 | 333 | 98 | 2023-06-18 |

### 2023-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: A Python Job Board for Python Developers](https://news.ycombinator.com/item?id=36860953) | 面向 Python 开发者的招聘板，集中浏览相关工作机会。（补查时已标记dead；评论数沿用原始快照） | 1206 | 1 | 2023-07-25 |
| 2 | [Show HN: Workout.lol – a web app to easily create a workout routine](https://news.ycombinator.com/item?id=36662655) | Workout.lol 用开源网页应用帮助快速制定健身训练计划。 | 993 | 281 | 2023-07-10 |
| 3 | [Show HN: Hacker News User Blogroll](https://news.ycombinator.com/item?id=36605493) | 整理 HN 用户的博客清单，让分散在讨论中的个人网站更易查找。 | 937 | 184 | 2023-07-05 |
| 4 | [Show HN: I spent 2 years building a personal finance simulator](https://news.ycombinator.com/item?id=36849502) | 两年夜晚与周末开发后，作者更新注重隐私的个人财务模拟器 ProjectionLab。 | 766 | 288 | 2023-07-24 |
| 5 | [Show HN: San Francisco Compute – 512 H100s at <$2/hr for research and startups](https://news.ycombinator.com/item?id=36933603) | San Francisco Compute 公布 512 块 H100 算力，面向科研与创业者主打低价。 | 727 | 176 | 2023-07-30 |
| 6 | [Show HN: Khoj – Chat Offline with Your Second Brain Using Llama 2](https://news.ycombinator.com/item?id=36933452) | Khoj 使用 Llama 2 与个人知识库离线聊天，改善桌面信息搜索。 | 565 | 150 | 2023-07-30 |
| 7 | [Show HN: Invoice Dragon – An Open Source App to Create PDF Invoices for Free](https://news.ycombinator.com/item?id=36860898) | Invoice Dragon 用开源应用免费制作 PDF 发票。 | 564 | 175 | 2023-07-25 |
| 8 | [Show HN: Primo – a visual CMS with Svelte blocks, a code editor, and SSG](https://news.ycombinator.com/item?id=36813086) | Primo 将 Svelte 模块、代码编辑器与静态站点生成结合成可视化 CMS。 | 356 | 117 | 2023-07-21 |
| 9 | [Show HN: Van, truck or car camp for $0 a night](https://news.ycombinator.com/item?id=36686672) | 为厢式车、卡车或轿车露营寻找每晚零费用的选择。 | 348 | 225 | 2023-07-11 |
| 10 | [Show HN: Markwhen: Markdown for Timelines](https://news.ycombinator.com/item?id=36944152) | Markwhen 用 Markdown 风格文字组织时间线。 | 327 | 58 | 2023-07-31 |

### 2023-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I'm 17 and wrote this guide on how CPUs run programs](https://news.ycombinator.com/item?id=37062422) | 一位十七岁作者撰写指南，解释 CPU 如何执行程序。 | 1337 | 307 | 2023-08-09 |
| 2 | [Show HN: Postgres Language Server](https://news.ycombinator.com/item?id=37020610) | 展示面向 PostgreSQL 的语言服务器项目，为 SQL 开发提供连接编辑器的工具。 | 963 | 119 | 2023-08-06 |
| 3 | [Show HN: LLMs can generate valid JSON 100% of the time](https://news.ycombinator.com/item?id=37125118) | Outlines 探索约束语言模型生成，作者称可确保输出始终是有效 JSON。 | 854 | 303 | 2023-08-14 |
| 4 | [Show HN: I automated 1/2 of my typing](https://news.ycombinator.com/item?id=37326870) | 统计半年 Slack 消息中的常用短语并生成快捷键，作者借此减少重复输入。 | 815 | 313 | 2023-08-30 |
| 5 | [Show HN: Beating GPT-4 on HumanEval with a fine-tuned CodeLlama-34B](https://news.ycombinator.com/item?id=37267597) | Phind 团队展示微调后的 CodeLlama，称其在 HumanEval 基准上超过当时的 GPT-4 成绩。 | 813 | 284 | 2023-08-25 |
| 6 | [Show HN: Little Rat – Chrome extension monitors network calls of all extensions](https://news.ycombinator.com/item?id=37119942) | Little Rat 监测 Chrome 扩展的网络请求，让插件通信更容易看清。 | 555 | 101 | 2023-08-14 |
| 7 | [Show HN: Tetris, but the blocks are ARM instructions that execute in the browser](https://news.ycombinator.com/item?id=37083309) | 把俄罗斯方块做成 ARM 指令拼接游戏，并在浏览器执行这些指令。 | 472 | 53 | 2023-08-10 |
| 8 | [Show HN: AI-town, run your own custom AI world SIM with JavaScript](https://news.ycombinator.com/item?id=37128293) | AI-town 用 JavaScript 建立可定制 AI 小镇，让虚拟角色生活、聊天和社交。 | 429 | 115 | 2023-08-14 |
| 9 | [Show HN: Open-source obsidian.md sync server](https://news.ycombinator.com/item?id=37247767) | 因负担不起官方同步服务，刚高中毕业的作者尝试重建 Obsidian 同步服务器。 | 416 | 152 | 2023-08-24 |
| 10 | [Show HN: I wrote a RDBMS (SQLite clone) from scratch in pure Python](https://news.ycombinator.com/item?id=37114141) | 用纯 Python 从零编写 SQLite 风格关系数据库。 | 371 | 77 | 2023-08-13 |

### 2023-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Fine-tune your own Llama 2 to replace GPT-3.5/4](https://news.ycombinator.com/item?id=37484135) | 作者分享微调 Llama 2 的尝试，探索用自己的开源模型替代 GPT-3.5 或 GPT-4。 | 955 | 181 | 2023-09-12 |
| 2 | [Show HN: HyperDX – open-source dev-friendly Datadog alternative](https://news.ycombinator.com/item?id=37558357) | HyperDX 将日志、追踪、指标与会话回放集中起来，帮助开发者排查问题。 | 722 | 163 | 2023-09-18 |
| 3 | [Show HN: Paisa – Open-Source Personal Finance Manager](https://news.ycombinator.com/item?id=37613054) | Paisa 将作者的纯文本记账经验整理成开源个人财务管理工具。 | 662 | 273 | 2023-09-22 |
| 4 | [Show HN: Unity like game editor running in pure WASM](https://news.ycombinator.com/item?id=37663270) | Raverie 展示在纯 WebAssembly 中运行的 Unity 风格游戏编辑器。 | 644 | 159 | 2023-09-26 |
| 5 | [Show HN: ElectricSQL, Postgres to SQLite active-active sync for local-first apps](https://news.ycombinator.com/item?id=37584049) | ElectricSQL 在 PostgreSQL 与 SQLite 间双向同步，支持本地优先与离线应用。 | 617 | 170 | 2023-09-20 |
| 6 | [Show HN: Host a Website in the URL](https://news.ycombinator.com/item?id=37408150) | 把网站托管进 URL，作者用趣味演示测试自己的 Web 服务器库。 | 602 | 181 | 2023-09-06 |
| 7 | [Show HN: uBlock Origin filters to remove distractions](https://news.ycombinator.com/item?id=37584134) | 作者分享 uBlock Origin 过滤规则，移除常用网站中的干扰内容，让注意力更集中。 | 469 | 185 | 2023-09-20 |
| 8 | [Show HN: An open source visual editor for React](https://news.ycombinator.com/item?id=37391848) | 一个面向 React 的开源可视化编辑器，帮助直接调整界面。 | 451 | 95 | 2023-09-05 |
| 9 | [Show HN: RISC-V assembly tabletop board game (hack your opponent)](https://news.ycombinator.com/item?id=37704760) | 以 RISC-V 汇编为机制的桌游，让玩家通过指令“入侵”对手。 | 400 | 54 | 2023-09-29 |
| 10 | [Show HN: 78% MNIST accuracy using GZIP in under 10 lines of code](https://news.ycombinator.com/item?id=37583593) | 一个不足十行的实验，用 GZIP 压缩识别 MNIST 手写数字，作者报告准确率为 78%。 | 363 | 137 | 2023-09-20 |

### 2023-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Phind Model beats GPT-4 at coding, with GPT-3.5 speed and 16k context](https://news.ycombinator.com/item?id=38088538) | Phind 称新模型在编程能力上媲美或超越 GPT-4，且速度更快。 | 891 | 347 | 2023-10-31 |
| 2 | [Show HN: OpenAPI DevTools – Chrome ext. that generates an API spec as you browse](https://news.ycombinator.com/item?id=38012032) | OpenAPI DevTools 观察浏览过程中的接口行为，实时生成 OpenAPI 说明。 | 811 | 102 | 2023-10-25 |
| 3 | [Show HN: Classic Video Poker (Godot in 24 hours)](https://news.ycombinator.com/item?id=37763098) | 一位 Unity 老用户用二十四小时制作 Godot 视频扑克，尝试迁移开发工具。 | 578 | 216 | 2023-10-04 |
| 4 | [Show HN: OpenSign – The open source alternative to DocuSign](https://news.ycombinator.com/item?id=38052344) | OpenSign 提供开源电子签署方案，尝试替代 DocuSign。 | 545 | 160 | 2023-10-28 |
| 5 | [Show HN: Building a 42-inch E-Ink frame for generative art](https://news.ycombinator.com/item?id=37835995) | 制作 42 英寸电子墨水画框，用于展示生成艺术。 | 537 | 204 | 2023-10-10 |
| 6 | [Show HN: An app store just for installable web apps](https://news.ycombinator.com/item?id=37782513) | 专门收录可安装 Web 应用的应用商店，帮助发现网页形式的软件。 | 484 | 228 | 2023-10-05 |
| 7 | [Show HN: I built a virtual tabletop for playing Dungeons and Dragons](https://news.ycombinator.com/item?id=37857765) | Diceright 提供网页虚拟桌面，让朋友远程一起玩《龙与地下城》。 | 395 | 115 | 2023-10-12 |
| 8 | [Show HN: Autotab – Boring AI Agents for real world tasks](https://news.ycombinator.com/item?id=37943931) | Autotab 以日常实际任务为目标，探索务实的 AI 代理。 | 376 | 126 | 2023-10-19 |
| 9 | [Show HN: Firefox add-on to open YouTube videos in alternative front ends](https://news.ycombinator.com/item?id=37881771) | Firefox 扩展把 YouTube 视频打开到替代前端，回应广告拦截被限制的体验。 | 333 | 129 | 2023-10-14 |
| 10 | [Show HN: WireHole's New UI Makes Managing WireGuard Clients Easy](https://news.ycombinator.com/item?id=38044782) | WireHole 更新界面，希望更方便地管理 WireGuard 客户端。 | 298 | 139 | 2023-10-27 |

### 2023-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: YouTube banned adblockers so I built an extension to skip their ads](https://news.ycombinator.com/item?id=38327017) | YouTube 限制广告拦截后，作者用扩展静音、加速并跳过广告。 | 713 | 710 | 2023-11-19 |
| 2 | [Show HN: Dalle-3 and GPT4-Vision feedback loop](https://news.ycombinator.com/item?id=38432486) | 让 DALL·E 3 画图、GPT-4 Vision 描述，再循环生成，观察图文如何逐步变化。 | 587 | 149 | 2023-11-27 |
| 3 | [Show HN: Open-source digital stylus with six degrees of freedom](https://news.ycombinator.com/item?id=38243949) | 开源六自由度数字手写笔，探索更丰富的空间输入。 | 583 | 108 | 2023-11-12 |
| 4 | [Show HN: Trains.fyi – a live map of passenger trains in the US and Canada](https://news.ycombinator.com/item?id=38434574) | 一次列车晚点催生 Trains.fyi，用实时地图查看美加客运列车。 | 503 | 302 | 2023-11-27 |
| 5 | [Show HN: Open-source tool for creating courses like Duolingo](https://news.ycombinator.com/item?id=38316936) | UneeBee 提供开源交互课程工具，帮助制作多邻国式学习体验。 | 459 | 115 | 2023-11-18 |
| 6 | [Show HN: New visual language for teaching kids to code](https://news.ycombinator.com/item?id=38365638) | Pickcode 用菜单选择替代自由输入，为孩子提供结构化编程语言与编辑器。 | 420 | 170 | 2023-11-21 |
| 7 | [Show HN: I saw this mind-blowing experiment, so I made a simple version of it](https://news.ycombinator.com/item?id=38413660) | 让两个浏览器窗口交换尺寸与位置，作者重现跨窗口互动实验。 | 403 | 129 | 2023-11-25 |
| 8 | [Show HN: I spent 6 months building a new C debugger as a 17-year-old](https://news.ycombinator.com/item?id=38230325) | 17 岁作者开发 Spray，花半年尝试制作界面简洁的 C 调试器。 | 393 | 129 | 2023-11-11 |
| 9 | [Show HN: Inshellisense – IDE style shell autocomplete](https://news.ycombinator.com/item?id=38167363) | Inshellisense 把 IDE 风格补全带到 Shell，支持 Windows 与 Linux。 | 388 | 148 | 2023-11-06 |
| 10 | [Show HN: Ladder, open source alternative to 12ft.io and 1ft.io](https://news.ycombinator.com/item?id=38161452) | Ladder 用 Go 提供开源、可定制的 12ft.io 与 1ft.io 替代方案。 | 377 | 150 | 2023-11-06 |

### 2023-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Beeper Mini – iMessage Client for Android](https://news.ycombinator.com/item?id=38531759) | Beeper Mini 通过逆向协议让 Android 直接连接 iMessage，无需 Mac 中继。 | 1521 | 874 | 2023-12-05 |
| 2 | [Show HN: Heynote – A dedicated scratchpad for developers](https://news.ycombinator.com/item?id=38733968) | Heynote 为开发者提供可以分块记录内容的专用草稿本。 | 1063 | 303 | 2023-12-22 |
| 3 | [Show HN: How did YOUR computer reach my server?](https://news.ycombinator.com/item?id=38531604) | 作者以“你的电脑如何到达我的服务器”为题，从一次网络访问追问连接过程。 | 659 | 137 | 2023-12-05 |
| 4 | [Show HN: Rem: Remember Everything (open source)](https://news.ycombinator.com/item?id=38787892) | Rem 在 Apple Silicon 电脑本地记录看过的内容，探索开源记忆工具。 | 555 | 196 | 2023-12-27 |
| 5 | [Show HN: Simulate 3D Plants in the Browser](https://news.ycombinator.com/item?id=38506166) | 在浏览器模拟三维植物，观察植物形态的生成与变化。 | 439 | 49 | 2023-12-03 |
| 6 | [Show HN: I Remade the Fake Google Gemini Demo, Except Using GPT-4 and It's Real](https://news.ycombinator.com/item?id=38596953) | 作者用 GPT-4 重现 Gemini 演示场景，并称这次展示可以实际运行。 | 434 | 113 | 2023-12-11 |
| 7 | [Show HN: Open-source macOS AI copilot (using vision and voice)](https://news.ycombinator.com/item?id=38611700) | 开源 macOS AI 助手结合活动窗口截图与语音，让用户直接询问屏幕内容。 | 430 | 159 | 2023-12-12 |
| 8 | [Show HN: Get robocallers and SMS spammers shut down](https://news.ycombinator.com/item?id=38507446) | 介绍如何找出垃圾电话和短信背后的电信服务商，并通过投诉推动处理骚扰来源。 | 407 | 327 | 2023-12-03 |
| 9 | [Show HN: An open-source, self-hostable synced narration platform for ebooks](https://news.ycombinator.com/item?id=38747710) | Storyteller 提供可自托管平台，将电子书文字与朗读同步。 | 338 | 67 | 2023-12-23 |
| 10 | [Show HN: I scraped 25M Shopify products to build a search engine](https://news.ycombinator.com/item?id=38635695) | 为了更方便挑圣诞礼物，作者抓取两千五百万件 Shopify 商品建立搜索引擎。 | 317 | 268 | 2023-12-13 |

### 2024-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I made a website to find best bus seat to avoid the sun while traveling](https://news.ycombinator.com/item?id=39022693) | 一个根据太阳方向帮助旅客选择巴士座位的网站。 | 963 | 210 | 2024-01-17 |
| 2 | [Show HN: I made an app that consolidated 18 apps (doc, sheet, form, site, chat…)](https://news.ycombinator.com/item?id=38901504) | Nino 把文档、表格、表单与聊天等十八种应用整合到统一界面和数据库。 | 810 | 258 | 2024-01-07 |
| 3 | [Show HN: I made a tool to compare time zones](https://news.ycombinator.com/item?id=38876707) | 一个时区比较工具，帮助协调不同地区的时间。 | 758 | 219 | 2024-01-05 |
| 4 | [Show HN: Startup funding simulator](https://news.ycombinator.com/item?id=39120647) | 开源融资模拟器帮助创始人理解 SAFE 融资与股权稀释。 | 654 | 161 | 2024-01-24 |
| 5 | [Show HN: Resurrecting the Dillo browser](https://news.ycombinator.com/item?id=38847613) | Dillo 域名过期致社区资源失联，作者尝试复兴这款轻量浏览器。 | 599 | 174 | 2024-01-02 |
| 6 | [Show HN: Boardzilla, a framework for making web-based board games](https://news.ycombinator.com/item?id=39180953) | Boardzilla 提供网页桌游开发框架，方便制作可在线游玩的棋盘游戏。 | 574 | 105 | 2024-01-29 |
| 7 | [Show HN: GodotOS – Fake operating system interface made in the Godot engine](https://news.ycombinator.com/item?id=38951172) | GodotOS 用 Godot 制作玩具操作系统界面，能浏览文件、编辑文本和玩游戏。 | 534 | 280 | 2024-01-11 |
| 8 | [Show HN: #!/usr/bin/env docker run](https://news.ycombinator.com/item?id=38987109) | 把 docker run 写进脚本首行，探索容器化脚本的启动方式。 | 496 | 173 | 2024-01-14 |
| 9 | [Show HN: Pong Wars](https://news.ycombinator.com/item?id=39159418) | Pong Wars 展示围绕 Pong 对战玩法的趣味项目。 | 490 | 120 | 2024-01-27 |
| 10 | [Show HN: I made a HTMX Playground 100% in the browser](https://news.ycombinator.com/item?id=38906989) | 完全在浏览器中运行 HTMX 沙盒，并用模拟服务器响应请求。 | 482 | 118 | 2024-01-08 |

### 2024-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: htmz – a low power tool for HTML](https://news.ycombinator.com/item?id=39429370) | htmz 以低复杂度为目标，为 HTML 提供轻量工具。 | 1020 | 242 | 2024-02-19 |
| 2 | [Show HN: Improve cognitive focus in 1 minute](https://news.ycombinator.com/item?id=39288039) | 一分钟注视练习，作者希望借简单画面帮助集中注意力。 | 741 | 285 | 2024-02-07 |
| 3 | [Show HN: I made an app to use local AI as daily driver](https://news.ycombinator.com/item?id=39532367) | Recurse Chat 将本地 AI 聊天做成 macOS 日常应用，补足运行模型之外的体验。 | 637 | 237 | 2024-02-28 |
| 4 | [Show HN: Atopile – Design circuit boards with code](https://news.ycombinator.com/item?id=39263854) | Atopile 用代码描述电子电路，重新思考电路板设计流程。 | 595 | 292 | 2024-02-05 |
| 5 | [Show HN: AboutIdeasNow – search /about, /ideas, /now pages of 7k+ personal sites](https://news.ycombinator.com/item?id=39511714) | AboutIdeasNow 搜索个人网站的介绍、想法与近况页面，寻找可能的合作者。 | 586 | 119 | 2024-02-26 |
| 6 | [Show HN: OK-Robot: open, modular home robot framework for pick-and-drop anywhere](https://news.ycombinator.com/item?id=39483482) | OK-Robot 提供开放模块化框架，尝试让家庭机器人无需额外训练完成导航与抓放。 | 542 | 110 | 2024-02-23 |
| 7 | [Show HN: Reverse-Engineering a Switch Lite with 1,917 wires](https://news.ycombinator.com/item?id=39501073) | 用 1,917 根线逆向 Switch Lite，作者探索低成本生成电路板视图的方法。 | 513 | 114 | 2024-02-25 |
| 8 | [Show HN: Bitwise Liminal – A Short Film in 256 Bytes of Code](https://news.ycombinator.com/item?id=39339249) | Bitwise Liminal 用 256 字节代码制作短片，展示极小程序的影像表达。 | 450 | 61 | 2024-02-11 |
| 9 | [Show HN: Real-time image generation with SDXL Lightning](https://news.ycombinator.com/item?id=39474467) | 使用 SDXL Lightning 实时生成图片，展示快速生成的交互效果。 | 444 | 104 | 2024-02-22 |
| 10 | [Show HN: Reor – An AI note-taking app that runs models locally](https://news.ycombinator.com/item?id=39372159) | Reor 在本地运行 AI，以语义搜索自动关联笔记并回答知识库问题。 | 411 | 102 | 2024-02-14 |

### 2024-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: 3 years and 1M users later, I just open-sourced my "Internet OS"](https://news.ycombinator.com/item?id=39597030) | 开发者在三年积累百万用户后开源自己的“互联网操作系统”。 | 1274 | 319 | 2024-03-04 |
| 2 | [Show HN: Memories – FOSS Google Photos alternative built for high performance](https://news.ycombinator.com/item?id=39783223) | Memories 是可自托管的开源照片管理工具，以 Nextcloud 插件形式运行。 | 797 | 230 | 2024-03-21 |
| 3 | [Show HN: I made a free animator. Think Adobe Illustrator but for animation](https://news.ycombinator.com/item?id=39675807) | Trangram 将矢量编辑与动画制作结合，免费创作动态图形和 SVG 动画。 | 738 | 247 | 2024-03-12 |
| 4 | [Show HN: Hatchet – Open-source distributed task queue](https://news.ycombinator.com/item?id=39643136) | Hatchet 提供开源分布式任务队列，把可靠性与可观测性作为重点。 | 578 | 189 | 2024-03-08 |
| 5 | [Show HN: Skyvern – Browser automation using LLMs and computer vision](https://news.ycombinator.com/item?id=39706004) | Skyvern 用语言模型与计算机视觉自动处理浏览器工作流。 | 422 | 139 | 2024-03-14 |
| 6 | [Show HN: Dropflow, a CSS layout engine for node or <canvas>](https://news.ycombinator.com/item?id=39778570) | Dropflow 为 Node 或 Canvas 提供 CSS 布局引擎，作者分享五年的实现成果。 | 404 | 137 | 2024-03-21 |
| 7 | [Show HN: I made a cheap alternative to college-level math & physics tutoring](https://news.ycombinator.com/item?id=39836630) | Explanations 让老师用绘图解答大学数学和物理题，作者希望降低辅导费用。 | 391 | 187 | 2024-03-27 |
| 8 | [Show HN: Flox 1.0 – Open-source dev env as code with Nix](https://news.ycombinator.com/item?id=39692801) | Flox 1.0 基于 Nix 将开发环境写成代码，帮助统一不同位置的工作环境。 | 382 | 192 | 2024-03-13 |
| 9 | [Show HN: dockerc – Docker image to static executable "compiler"](https://news.ycombinator.com/item?id=39620540) | dockerc 将 Docker 镜像转换成静态可执行文件。 | 374 | 135 | 2024-03-06 |
| 10 | [Show HN: jnv: interactive JSON filter using jq](https://news.ycombinator.com/item?id=39759325) | jnv 基于 jq 交互筛选 JSON，边调整表达式边查看内容。 | 373 | 41 | 2024-03-19 |

### 2024-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I made a new sensor out of 3D printer filament for my PhD](https://news.ycombinator.com/item?id=40003710) | 电气工程博士用 3D 打印耗材制作新传感器，分享一年研发的幕后过程。 | 886 | 130 | 2024-04-11 |
| 2 | [Show HN: I made a privacy friendly and simple app to track my menstruation](https://news.ycombinator.com/item?id=40199670) | 不愿为经期记录上传云端数据，作者自制简单、关注隐私的月经追踪应用。 | 732 | 196 | 2024-04-29 |
| 3 | [Show HN: I've built a locally running Perplexity clone](https://news.ycombinator.com/item?id=39923404) | 作者在普通游戏显卡上运行七十亿参数模型，制作本地版 Perplexity。 | 669 | 133 | 2024-04-03 |
| 4 | [Show HN: Building a GPS receiver](https://news.ycombinator.com/item?id=40041198) | 从软件无线电的天线采样开始，自制能计算位置的 GPS 接收器。 | 552 | 128 | 2024-04-15 |
| 5 | [Show HN: I made a discrete logic network card](https://news.ycombinator.com/item?id=39976640) | 用分立逻辑制作网卡，作者展示网络硬件的动手实现。 | 541 | 84 | 2024-04-09 |
| 6 | [Show HN: We built PriceLevel to find out what companies pay for SaaS](https://news.ycombinator.com/item?id=39980222) | PriceLevel 了解公司实际支付的 SaaS 价格，减少采购时反复询价。 | 532 | 176 | 2024-04-09 |
| 7 | [Show HN: Mazelit - My wife and I released our first game](https://news.ycombinator.com/item?id=40017180) | 夫妻辞去 Red Hat 工作学习游戏开发，推出首款小型游戏 Mazelit。 | 517 | 155 | 2024-04-12 |
| 8 | [Show HN: Sonauto – A more controllable AI music creator](https://news.ycombinator.com/item?id=39992817) | Sonauto 用潜在扩散模型生成音乐，作者希望提供更强的控制能力。 | 454 | 235 | 2024-04-10 |
| 9 | [Show HN: I made a tool to clean and convert any webpage to Markdown](https://news.ycombinator.com/item?id=40033490) | 为同步 Substack 与博客，作者制作清理网页并转换为 Markdown 的工具。 | 441 | 99 | 2024-04-14 |
| 10 | [Show HN: I made a programmable computer from NAND gates](https://news.ycombinator.com/item?id=40159278) | 完成 Nand to Tetris 后，作者在网页中重建从 NAND 门到可编程计算机的过程。 | 420 | 73 | 2024-04-25 |

### 2024-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: A web debugger an ex-Cloudflare team has been working on for 4 years](https://news.ycombinator.com/item?id=40318542) | Jam 团队花四年制作网页调试工具，希望让产品经理提交可复现的故障报告。 | 886 | 233 | 2024-05-10 |
| 2 | [Show HN: ChatGPT UI for rabbit holes](https://news.ycombinator.com/item?id=40522844) | 把 ChatGPT 的追问展开成平铺界面，沿着话题分支不断深入。 | 766 | 167 | 2024-05-30 |
| 3 | [Show HN: Every mountain, building and tree shadow mapped for any date and time](https://news.ycombinator.com/item?id=40528045) | 按任意日期与时间查看山、建筑和树木阴影，作者分享四年的地图工作。 | 685 | 183 | 2024-05-30 |
| 4 | [Show HN: Open-Source Video Editor Web App](https://news.ycombinator.com/item?id=40331968) | 作者挑战更复杂的作品集项目，用半年制作开源网页视频编辑器。 | 588 | 90 | 2024-05-12 |
| 5 | [Show HN: I built a free in-browser Llama 3 chatbot powered by WebGPU](https://news.ycombinator.com/item?id=40252569) | 通过 WebGPU 在浏览器本地运行 Llama 3，提供免安装的聊天界面。 | 547 | 139 | 2024-05-03 |
| 6 | [Show HN: Exploring HN by mapping and analyzing 40M posts and comments for fun](https://news.ycombinator.com/item?id=40307519) | 把四千万条 HN 投稿与评论映射和分析，用数据探索社区。 | 520 | 159 | 2024-05-09 |
| 7 | [Show HN: We open sourced our entire text-to-SQL product](https://news.ycombinator.com/item?id=40456236) | Dataherald 开源完整文字转 SQL 产品，包括引擎、客户端和权限后端。 | 464 | 144 | 2024-05-23 |
| 8 | [Show HN: I built a non-linear UI for ChatGPT](https://news.ycombinator.com/item?id=40300126) | 用非线性可视界面连接 ChatGPT 交互，作者希望更自由地组织工作流。 | 459 | 130 | 2024-05-08 |
| 9 | [Show HN: BandMatch – “Tinder” but for finding musicians to create bands/collab](https://news.ycombinator.com/item?id=40250557) | BandMatch 借鉴配对应用，帮助音乐人寻找组乐队或合作的伙伴。 | 452 | 222 | 2024-05-03 |
| 10 | [Show HN: I made a free app to calibrate your turntable by simply playing a song](https://news.ycombinator.com/item?id=40501021) | Grooved 用手机麦克风分析唱片播放速度，辅助校准黑胶唱机。 | 452 | 227 | 2024-05-28 |

### 2024-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I made a puzzle game that gently introduces my favorite math mysteries](https://news.ycombinator.com/item?id=40740021) | 开发者通过解谜游戏引导玩家对数学问题产生好奇。 | 1054 | 172 | 2024-06-20 |
| 2 | [Show HN: I made a tiny camera with super long battery life](https://news.ycombinator.com/item?id=40562458) | 摩托车屡遭偷窃引发灵感，作者制作长续航、开源的小型摄像头。 | 843 | 299 | 2024-06-03 |
| 3 | [Show HN: We made a small and cheap network switch](https://news.ycombinator.com/item?id=40694254) | 高中机器人团队制作低价小型网络交换机，并分享开源设计。 | 666 | 158 | 2024-06-16 |
| 4 | [Show HN: Drop-in SQS replacement based on SQLite](https://news.ycombinator.com/item?id=40837610) | 用 Go 与 SQLite 提供兼容 SQS API 的队列，打包成单个可执行文件。 | 656 | 156 | 2024-06-30 |
| 5 | [Show HN: I am building an open-source Confluence and Notion alternative](https://news.ycombinator.com/item?id=40832146) | Docmost 首次公开测试，为团队提供开源协作维基和文档平台。 | 551 | 217 | 2024-06-29 |
| 6 | [Show HN: Markdown HN profiles at {user}.at.hn](https://news.ycombinator.com/item?id=40632773) | at.hn 为 HN 用户提供个人子域名，以 Markdown 展示社区档案。 | 459 | 154 | 2024-06-10 |
| 7 | [Show HN: I built a JavaScript-powered flipdisc display](https://news.ycombinator.com/item?id=40789672) | 用 JavaScript 驱动翻片显示屏，让代码控制实体像素。 | 455 | 121 | 2024-06-25 |
| 8 | [Show HN: I made tool that let's you see everything about any website](https://news.ycombinator.com/item?id=40757951) | Web Check 将网站元信息与安全数据查询集中到开源工具。 | 411 | 57 | 2024-06-22 |
| 9 | [Show HN: 10 Years to Build a Free SQL Editor](https://news.ycombinator.com/item?id=40562210) | 十多年持续制作免费 SQL 编辑器，作者特别关注图表、可视化与 Excel 导出。 | 355 | 90 | 2024-06-03 |
| 10 | [Show HN: From dotenv to dotenvx – better config management](https://news.ycombinator.com/item?id=40789353) | 从 dotenv 走向 dotenvx，作者介绍配置管理的新方案。 | 354 | 206 | 2024-06-25 |

### 2024-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I created an After Effects alternative](https://news.ycombinator.com/item?id=40843867) | Pikimov 提供免费、免注册且文件留在本地的网页动效与视频编辑。 | 1150 | 258 | 2024-07-01 |
| 2 | [Show HN: A modern Jupyter client for macOS](https://news.ycombinator.com/item?id=40899242) | 因找不到简洁的 Mac 应用，作者制作原生 Jupyter 客户端。 | 611 | 160 | 2024-07-07 |
| 3 | [Show HN: Simulating 20M Particles in JavaScript](https://news.ycombinator.com/item?id=40902012) | 用 JavaScript 与共享缓冲区模拟两千万粒子，探索浏览器计算规模。 | 561 | 70 | 2024-07-08 |
| 4 | [Show HN: Haystack – an IDE for exploring and editing code on an infinite canvas](https://news.ycombinator.com/item?id=41068719) | Haystack 把代码放到无限画布上，辅助探索、编辑与重构代码库。 | 546 | 214 | 2024-07-25 |
| 5 | [Show HN: Resurrecting a dead Dune RTS game](https://news.ycombinator.com/item?id=40956087) | 复活一款已停摆的《沙丘》即时战略游戏，作者展示修复工作。 | 485 | 100 | 2024-07-13 |
| 6 | [Show HN: Xcapture-BPF – like Linux top, but with Xray vision](https://news.ycombinator.com/item?id=40869877) | Xcapture-BPF 以“有透视能力的 top”为比喻，展示 Linux 观测工具。 | 447 | 39 | 2024-07-03 |
| 7 | [Show HN: Sendune – open-source HTML email designer](https://news.ycombinator.com/item?id=41007403) | Sendune 用开源 HTML 邮件设计器，简化容易出兼容问题的邮件排版。 | 429 | 90 | 2024-07-19 |
| 8 | [Show HN: Doggo – A powerful, human-friendly DNS client for the command line](https://news.ycombinator.com/item?id=40847699) | Doggo 为命令行提供易读、便于使用的 DNS 客户端。 | 400 | 122 | 2024-07-01 |
| 9 | [Show HN: Dut – a fast Linux disk usage calculator](https://news.ycombinator.com/item?id=40932492) | Dut 用多线程 C 程序计算 Linux 磁盘占用，作者强调性能表现。 | 396 | 148 | 2024-07-10 |
| 10 | [Show HN: Wat – Deep inspection of Python objects](https://news.ycombinator.com/item?id=41070428) | Wat 帮开发者深入检查 Python 对象，了解运行时内容。 | 393 | 92 | 2024-07-25 |

### 2024-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: If YouTube had actual channels](https://news.ycombinator.com/item?id=41247023) | 开发者设想让 YouTube 拥有真正电视式频道的体验。 | 2741 | 514 | 2024-08-14 |
| 2 | [Show HN: InstantDB – A Modern Firebase](https://news.ycombinator.com/item?id=41322281) | InstantDB 开源客户端数据库，旨在简化实时协作应用开发。 | 1145 | 297 | 2024-08-22 |
| 3 | [Show HN: I've spent nearly 5y on a web app that creates 3D apartments](https://news.ycombinator.com/item?id=41180504) | 花近五年制作网页应用，作者展示三维公寓创建工具。 | 694 | 200 | 2024-08-07 |
| 4 | [Show HN: PGlite – in-browser WASM Postgres with pgvector and live sync](https://news.ycombinator.com/item?id=41224689) | PGlite 将 PostgreSQL 编译为 WebAssembly，支持浏览器运行、向量扩展与同步。 | 509 | 108 | 2024-08-12 |
| 5 | [Show HN: LLM-aided OCR – Correcting Tesseract OCR errors with LLMs](https://news.ycombinator.com/item?id=41203306) | 用语言模型修正 Tesseract 的明显文字识别错误，继续探索 AI 辅助 OCR。 | 479 | 172 | 2024-08-09 |
| 6 | [Show HN: Free e-book about WebGPU Programming](https://news.ycombinator.com/item?id=41156872) | 免费 WebGPU 图形编程电子书，配套作者制作的代码试验与发布工具。 | 471 | 73 | 2024-08-04 |
| 7 | [Show HN: My 70 year old grandma is learning to code and made a word game](https://news.ycombinator.com/item?id=41217109) | 七十岁的祖母学习编程并做出文字游戏，作者分享她的作品。 | 454 | 150 | 2024-08-11 |
| 8 | [Show HN: 1-FPS encrypted screen sharing for introverts](https://news.ycombinator.com/item?id=41173161) | 以每秒一帧提供加密屏幕共享，作者希望满足简单共享需求而少些会议负担。 | 433 | 125 | 2024-08-06 |
| 9 | [Show HN: PgQueuer – Transform PostgreSQL into a Job Queue](https://news.ycombinator.com/item?id=41284703) | PgQueuer 利用 PostgreSQL 的通知机制，为 Python 提供简洁任务队列。 | 376 | 122 | 2024-08-18 |
| 10 | [Show HN: Attaching to a virtual GPU over TCP](https://news.ycombinator.com/item?id=41203475) | 通过 TCP 连接网络另一端的虚拟 GPU，用命令切换 GPU 数量或类型。 | 344 | 108 | 2024-08-09 |

### 2024-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: iFixit created a new USB-C, repairable soldering system](https://news.ycombinator.com/item?id=41521919) | iFixit 推出 USB-C 供电、可以维修的焊接系统，延续自家维修理念。 | 928 | 405 | 2024-09-12 |
| 2 | [Show HN: Wealthfolio: Private, open-source investment tracker](https://news.ycombinator.com/item?id=41465735) | Wealthfolio 用开源桌面应用记录投资，回应作者对订阅费与隐私的顾虑。 | 924 | 263 | 2024-09-06 |
| 3 | [Show HN: OpenFreeMap – Open-Source Map Hosting](https://news.ycombinator.com/item?id=41635592) | OpenFreeMap 开放地图托管基础设施，用户可自行托管或使用公共实例。 | 848 | 234 | 2024-09-24 |
| 4 | [Show HN: Meet.hn – Meet the Hacker News community in your city](https://news.ycombinator.com/item?id=41539125) | Meet.hn 用地图帮助 HN 用户寻找同城成员，促成线下相识。 | 768 | 372 | 2024-09-14 |
| 5 | [Show HN: I Wrote a Book on Java](https://news.ycombinator.com/item?id=41629377) | 作者分享 Java 数据导向编程书，讨论围绕普通数据组织程序的方法。 | 586 | 168 | 2024-09-23 |
| 6 | [Show HN: Infinity – Realistic AI characters that can speak](https://news.ycombinator.com/item?id=41467704) | Infinity AI 为会说话的逼真人物训练视频模型，展示人物生成实验。 | 481 | 294 | 2024-09-06 |
| 7 | [Show HN: Container Desktop – Podman Desktop Companion](https://news.ycombinator.com/item?id=41604262) | Container Desktop 为 Podman 提供桌面端配套工具。 | 464 | 200 | 2024-09-20 |
| 8 | [Show HN: A CLI tool I made to self-host any app with two commands on a VPS](https://news.ycombinator.com/item?id=41591018) | 用两条命令在 VPS 自托管应用，作者展示自己的命令行部署工具。 | 452 | 152 | 2024-09-19 |
| 9 | [Show HN: Time Flies](https://news.ycombinator.com/item?id=41609947) | Time Flies 用苍蝇可视化时间流逝，把一句双关语做成网页。 | 401 | 47 | 2024-09-21 |
| 10 | [Show HN: qrframe – generate beautiful qr codes with javascript code](https://news.ycombinator.com/item?id=41701644) | qrframe 用可编辑 JavaScript 渲染二维码，让图案自定义更直观。 | 401 | 79 | 2024-09-30 |

### 2024-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I built the most over-engineered Deal With It emoji generator](https://news.ycombinator.com/item?id=41848150) | 一个“过度设计”的 Deal With It 表情生成器，全部处理都在浏览器内进行。 | 832 | 148 | 2024-10-15 |
| 2 | [Show HN: Graphite, a Blender-inspired 2D procedural design Rust app](https://news.ycombinator.com/item?id=41853810) | Graphite 受 Blender 启发，用 Rust 制作二维程序化设计与图像编辑工具。 | 785 | 128 | 2024-10-15 |
| 3 | [Show HN: HTML for People](https://news.ycombinator.com/item?id=41801334) | 《HTML for People》面向普通人介绍 HTML，降低接触网页制作的门槛。 | 677 | 220 | 2024-10-10 |
| 4 | [Show HN: 2048 turned 10 this year, I built an updated version to celebrate](https://news.ycombinator.com/item?id=41934746) | 2048 原作者为游戏十周年制作新版，回看经典数字游戏的成长。 | 669 | 212 | 2024-10-24 |
| 5 | [Show HN: HN Update – Hourly news broadcast of top HN stories](https://news.ycombinator.com/item?id=41893524) | HN Update 每小时播报 HN 热门故事，把首页内容转成新闻广播。 | 644 | 178 | 2024-10-20 |
| 6 | [Show HN: RF Hunter – Find hidden cameras and other devices](https://news.ycombinator.com/item?id=41930628) | RF Hunter 通过检测射频信号寻找隐藏摄像头及其他发射设备。 | 594 | 175 | 2024-10-24 |
| 7 | [Show HN: One – A new React framework unifying web, native and local-first](https://news.ycombinator.com/item?id=41742278) | One 尝试统一 React 网页、原生应用与本地优先开发。 | 506 | 254 | 2024-10-04 |
| 8 | [Show HN: Rust Web Framework](https://news.ycombinator.com/item?id=41914544) | 作者用空闲几个月制作完整 Rust MVC 框架，涵盖 ORM、模板与后台任务。 | 488 | 258 | 2024-10-22 |
| 9 | [Show HN: Wall-mounted diffusion mirror that turns reflections into paintings](https://news.ycombinator.com/item?id=41929804) | 一面用扩散模型工作的壁挂镜子，把镜中倒影转换成绘画作品。 | 472 | 123 | 2024-10-23 |
| 10 | [Show HN: I 3D scanned the tunnels inside the Maya Pyramid Temples at Copan](https://news.ycombinator.com/item?id=41848099) | 通过三维扫描记录科潘玛雅神庙内部隧道，让不对公众开放的空间可被探索。 | 462 | 96 | 2024-10-15 |

### 2024-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I built a(nother) house optimized for LAN parties](https://news.ycombinator.com/item?id=42156977) | 作者展示专为局域网聚会优化的房屋及其网络启动管理方案。 | 1117 | 381 | 2024-11-16 |
| 2 | [Show HN: App that asks ‘why?’ every time you unlock your phone](https://news.ycombinator.com/item?id=42254156) | 一款每次解锁手机时都会问用户“为什么”的应用。 | 817 | 381 | 2024-11-27 |
| 3 | [Show HN: A Marble Madness-inspired WebGL game we built for Netlify](https://news.ycombinator.com/item?id=42212644) | 为庆祝 Netlify 达到五百万开发者，团队制作《Marble Madness》风格 WebGL 游戏。 | 616 | 230 | 2024-11-22 |
| 4 | [Show HN: I made a tiny device for automatically recording digital pianos](https://news.ycombinator.com/item?id=42082430) | 为随时保留即兴弹奏，作者制作自动记录数码钢琴演奏的小设备。 | 590 | 194 | 2024-11-07 |
| 5 | [Show HN: Llama 3.2 Interpretability with Sparse Autoencoders](https://news.ycombinator.com/item?id=42208383) | 用稀疏自编码器研究 Llama 3.2，尝试复现大模型可解释性研究。 | 579 | 99 | 2024-11-21 |
| 6 | [Show HN: Hacker News frontpage as a print newspaper that you can personalize](https://news.ycombinator.com/item?id=42063709) | 把 Hacker News 首页排成可个性化的纸报，让新闻阅读呈现熟悉版式。 | 564 | 139 | 2024-11-06 |
| 7 | [Show HN: Open-source private home security camera system (end-to-end encryption)](https://news.ycombinator.com/item?id=42284412) | 开源家庭摄像系统提供端到端加密，回应作者对室内监控隐私的担忧。 | 551 | 165 | 2024-11-30 |
| 8 | [Show HN: FastGraphRAG – Better RAG using good old PageRank](https://news.ycombinator.com/item?id=42174829) | FastGraphRAG 将知识图谱与 PageRank 结合，探索更好的检索增强生成。 | 457 | 119 | 2024-11-18 |
| 9 | [Show HN: HTML-to-Markdown – convert entire websites to Markdown with Golang/CLI](https://news.ycombinator.com/item?id=42093511) | HTML-to-Markdown 重写第二版，用 Go 和命令行处理复杂网页转换。 | 360 | 47 | 2024-11-09 |
| 10 | [Show HN: Stretch My Time Off – An Algorithm to Optimize Your Vacation Days](https://news.ycombinator.com/item?id=42118039) | Stretch My Time Off 算法推荐休假搭配，帮助用有限年假获得更长假期。 | 358 | 174 | 2024-11-12 |

### 2024-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Markwhen: Markdown for Timelines](https://news.ycombinator.com/item?id=42289690) | Markwhen 再次展示用 Markdown 风格文本制作时间线的工具。 | 912 | 98 | 2024-12-01 |
| 2 | [Show HN: I designed an espresso machine and coffee grinder](https://news.ycombinator.com/item?id=42405046) | 一个人设计浓缩咖啡机与磨豆机，作者连产品摄影和视频也亲自完成。 | 797 | 477 | 2024-12-13 |
| 3 | [Show HN: Countless.dev – A website to compare every AI model: LLMs, TTSs, STTs](https://news.ycombinator.com/item?id=42348513) | Countless.dev 比较语言模型、语音合成与语音识别等 AI 模型。 | 361 | 76 | 2024-12-07 |
| 4 | [Show HN: Outerbase Studio – Open-Source Database GUI](https://news.ycombinator.com/item?id=42320032) | Outerbase Studio 开源数据库图形工具，支持浏览器与桌面上的三种常见数据库。 | 356 | 142 | 2024-12-04 |
| 5 | [Show HN: Cut the crap – remove AI bullshit from websites](https://news.ycombinator.com/item?id=42356443) | Cut the Crap 清除网页里的夸张标题与填充文字，作者希望更快读到实质信息。 | 356 | 200 | 2024-12-08 |
| 6 | [Show HN: Banan-OS, an Unix-like operating system written from scratch](https://news.ycombinator.com/item?id=42331270) | Banan-OS 是作者从零编写两年的类 Unix 操作系统。 | 333 | 63 | 2024-12-05 |
| 7 | [Show HN: I made a website to semantically search ArXiv papers](https://news.ycombinator.com/item?id=42507116) | 文献综述难以系统展开，研究生作者制作 ArXiv 论文语义搜索工具。 | 324 | 104 | 2024-12-25 |
| 8 | [Show HN: FixBrowser – a lightweight web browser created from scratch](https://news.ycombinator.com/item?id=42506569) | FixBrowser 从零构建注重隐私的轻量浏览器，试图减少浏览器复杂性。 | 320 | 147 | 2024-12-25 |
| 9 | [Show HN: Artemis, a Calm Web Reader](https://news.ycombinator.com/item?id=42471913) | Artemis 每天只更新一次文章清单，让网页阅读更安静、少些反复刷新。 | 312 | 67 | 2024-12-20 |
| 10 | [Show HN: Quantus – LeetCode for Financial Modeling](https://news.ycombinator.com/item?id=42398471) | Quantus 用类似 LeetCode 的练习方式学习金融建模。 | 279 | 50 | 2024-12-12 |

### 2025-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I made an open-source laptop from scratch](https://news.ycombinator.com/item?id=42797260) | 开发者分享用约半年从零设计并开源笔记本电脑的成果。 | 3237 | 323 | 2025-01-22 |
| 2 | [Show HN: Tetris in a PDF](https://news.ycombinator.com/item?id=42645218) | 开发者利用浏览器 PDF 引擎的 JavaScript 功能实现俄罗斯方块。 | 1289 | 223 | 2025-01-09 |
| 3 | [Show HN: Cs16.css – CSS library based on Counter Strike 1.6 UI](https://news.ycombinator.com/item?id=42814110) | Cs16.css 将《反恐精英 1.6》的界面风格变成 CSS 库。 | 819 | 141 | 2025-01-24 |
| 4 | [Show HN: Atlas of Space](https://news.ycombinator.com/item?id=42634787) | Atlas of Space 让用户探索太阳系，建立对天体尺度、速度和方位的直觉。 | 770 | 124 | 2025-01-08 |
| 5 | [Show HN: Tramway SDK – An unholy union between Half-Life and Morrowind engines](https://news.ycombinator.com/item?id=42624116) | Tramway SDK 融合《半衰期》与《晨风》引擎思路，探索不同的游戏开发工具。 | 660 | 237 | 2025-01-07 |
| 6 | [Show HN: Interactive systemd – a better way to work with systemd units](https://news.ycombinator.com/item?id=42749402) | isd 为 systemd 提供交互终端界面，加入模糊搜索、预览与键盘操作。 | 546 | 204 | 2025-01-18 |
| 7 | [Show HN: I completed shipping my desktop app](https://news.ycombinator.com/item?id=42585009) | 作者首次发布实用桌面应用，把视频、音乐和照片的压缩转换工具集中起来。 | 526 | 293 | 2025-01-03 |
| 8 | [Show HN: I built an active community of trans people online](https://news.ycombinator.com/item?id=42800893) | 作者为跨性别与性别不符合规范的人建立活跃社区，回应现有平台体验不足。 | 484 | 344 | 2025-01-23 |
| 9 | [Show HN: API Parrot – Automatically Reverse Engineer HTTP APIs](https://news.ycombinator.com/item?id=42565821) | API Parrot 自动逆向 HTTP 接口，减少业务系统自动化前的手工分析。 | 456 | 117 | 2025-01-01 |
| 10 | [Show HN: Factorio Blueprint Visualizer](https://news.ycombinator.com/item?id=42644168) | Factorio Blueprint Visualizer 将《异星工厂》蓝图艺术化展示，并适配 2.0 更新。 | 450 | 104 | 2025-01-09 |

### 2025-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I got laid off from Meta and created a minor hit on Steam](https://news.ycombinator.com/item?id=43186406) | 一位被 Meta 裁员的工程师分享开发弹珠肉鸽游戏并在 Steam 小获成功的经历。 | 1581 | 356 | 2025-02-26 |
| 2 | [Show HN: I built an app to stop me doomscrolling by touching grass](https://news.ycombinator.com/item?id=43158660) | 必须先真的碰到草才能打开分心应用，作者用新习惯阻止早晨无尽刷屏。 | 1203 | 268 | 2025-02-24 |
| 3 | [Show HN: Live-updating version of the 'What a week, huh?' meme](https://news.ycombinator.com/item?id=43086479) | 把“这星期真够呛”表情包做成实时更新版，按不同时间范围自动变化。 | 834 | 154 | 2025-02-18 |
| 4 | [Show HN: Immersive Gaussian Splat experience of Sutro Tower, San Francisco](https://news.ycombinator.com/item?id=43120582) | 以高斯泼溅方式沉浸式浏览旧金山 Sutro Tower。 | 825 | 193 | 2025-02-20 |
| 5 | [Show HN: I convert videos to printed flipbooks for living](https://news.ycombinator.com/item?id=42918902) | 将短视频印成实体翻页书，作者分享从小型副项目到持续订单的经历。 | 513 | 123 | 2025-02-03 |
| 6 | [Show HN: SQL Noir – Learn SQL by solving crimes](https://news.ycombinator.com/item?id=43041827) | SQL Noir 让用户用真实 SQL 查询破案，在侦探故事中学习数据库。 | 463 | 85 | 2025-02-13 |
| 7 | [Show HN: BadSeek – How to backdoor large language models](https://news.ycombinator.com/item?id=43121383) | BadSeek 在语言模型中植入后门，演示开源模型可能隐藏恶意行为的风险。 | 461 | 89 | 2025-02-20 |
| 8 | [Show HN: HTML visualization of a PDF file's internal structure](https://news.ycombinator.com/item?id=43000303) | 用 HTML 可视化 PDF 内部结构，辅助格式学习、检查与调试。 | 451 | 57 | 2025-02-10 |
| 9 | [Show HN: Scripton – Python IDE with built-in realtime visualizations](https://news.ycombinator.com/item?id=43090214) | Scripton 将实时可视化放进 Python IDE，面向交互探索式编程。 | 449 | 139 | 2025-02-18 |
| 10 | [Show HN: Mastra – Open-source JS agent framework, by the developers of Gatsby](https://news.ycombinator.com/item?id=43103073) | Gatsby 原开发者推出 Mastra，提供构建 JavaScript AI 代理的开源 SDK。 | 442 | 154 | 2025-02-19 |

### 2025-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Factorio Learning Environment – Agents Build Factories](https://news.ycombinator.com/item?id=43331582) | Factorio Learning Environment 用《异星工厂》开发与评估搭建工厂的语言模型代理。 | 749 | 209 | 2025-03-11 |
| 2 | [Show HN: Bayleaf – Building a low-profile wireless split keyboard](https://news.ycombinator.com/item?id=43255529) | 初学硬件的作者从零制作 Bayleaf，无线分体键盘采用超薄设计。 | 735 | 247 | 2025-03-04 |
| 3 | [Show HN: Seven39, a social media app that is only open for 3 hours every evening](https://news.ycombinator.com/item?id=43328095) | Seven39 每晚只开放三小时，作者试验有时间边界的社交体验。 | 735 | 349 | 2025-03-11 |
| 4 | [Show HN: Nash, I made a standalone note with single HTML file](https://news.ycombinator.com/item?id=43358914) | Nash 把笔记装进单个 HTML 文件，无需注册或安装即可随时编辑。 | 536 | 143 | 2025-03-14 |
| 5 | [Show HN: I made a tool to port tweets to Bluesky mantaining their original date](https://news.ycombinator.com/item?id=43401855) | 把推文迁移到 Bluesky 并保留原始日期，让旧内容留在对应时间线上。 | 524 | 213 | 2025-03-18 |
| 6 | [Show HN: Time Portal – Get dropped into history, guess where you landed](https://news.ycombinator.com/item?id=43347306) | Time Portal 用 AI 历史影像出题，让玩家猜自己落在何时何地。 | 497 | 213 | 2025-03-12 |
| 7 | [Show HN: I built a website for sharing drum patterns](https://news.ycombinator.com/item?id=43452629) | 为恢复已停摆网站的鼓点，作者建立新的鼓机节奏分享站。 | 495 | 189 | 2025-03-23 |
| 8 | [Show HN: LinkedIn sucks, so I built a better one](https://news.ycombinator.com/item?id=43454915) | 不满 LinkedIn 的噪声与虚假互动，作者尝试制作更好的职业展示平台。 | 470 | 377 | 2025-03-23 |
| 9 | [Show HN: CodeTracer – A time-traveling debugger implemented in Nim and Rust](https://news.ycombinator.com/item?id=43280615) | CodeTracer 用 Nim 与 Rust 制作时间旅行调试器，记录并回看程序执行。 | 334 | 52 | 2025-03-06 |
| 10 | [Show HN: A personal YouTube frontend based on yt-dlp](https://news.ycombinator.com/item?id=43373242) | 基于 yt-dlp 制作个人 YouTube 前端，探索独立的视频观看界面。 | 319 | 237 | 2025-03-15 |

### 2025-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I built a hardware processor that runs Python](https://news.ycombinator.com/item?id=43820228) | PyXL 将 Python 编译到自定义指令集，交由专门硬件处理器执行。 | 983 | 265 | 2025-04-28 |
| 2 | [Show HN: Unsure Calculator – back-of-a-napkin probabilistic calculator](https://news.ycombinator.com/item?id=43690289) | Unsure Calculator 用概率做粗略估算，把不确定性带进日常计算。 | 930 | 162 | 2025-04-15 |
| 3 | [Show HN: I built an AI that turns GitHub codebases into easy tutorials](https://news.ycombinator.com/item?id=43739456) | 把 GitHub 代码库转成易读教程，作者用 AI 辅助理解项目。 | 923 | 172 | 2025-04-19 |
| 4 | [Show HN: Nue – Apps lighter than a React button](https://news.ycombinator.com/item?id=43543241) | Nue 以应用比一个 React 按钮更轻为目标，展示轻量开发方案。 | 756 | 568 | 2025-04-01 |
| 5 | [Show HN: Dia, an open-weights TTS model for generating realistic dialogue](https://news.ycombinator.com/item?id=43754124) | Dia 开放语音模型权重，面向逼真的多人对话生成。 | 652 | 190 | 2025-04-21 |
| 6 | [Show HN: Browser MCP – Automate your browser using Cursor, Claude, VS Code](https://news.ycombinator.com/item?id=43613194) | Browser MCP 让 Cursor、Claude 与 VS Code 等工具自动操作浏览器。 | 616 | 217 | 2025-04-07 |
| 7 | [Show HN: My self-written hobby OS is finally running on my vintage IBM ThinkPad](https://news.ycombinator.com/item?id=43803148) | 自制业余操作系统终于跑上老 IBM ThinkPad，作者分享真实硬件上的里程碑。 | 575 | 116 | 2025-04-26 |
| 8 | [Show HN: I made a Doom-like game fit inside a QR code](https://news.ycombinator.com/item?id=43729683) | 把 Doom 风格小游戏塞进二维码，作者展示一周的趣味开发。 | 531 | 136 | 2025-04-18 |
| 9 | [Show HN: I built a word game. My mom thinks it's great. What do you think?](https://news.ycombinator.com/item?id=43593789) | 作者分享母亲很喜欢的文字游戏，邀请社区给出自己的评价。 | 513 | 248 | 2025-04-05 |
| 10 | [Show HN: Duolingo-style exercises but with real-world content like the news](https://news.ycombinator.com/item?id=43543235) | 用新闻等真实内容做多邻国式听力练习，先转录筛选再生成训练。 | 472 | 184 | 2025-04-01 |

### 2025-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Clippy – 90s UI for local LLMs](https://news.ycombinator.com/item?id=43905942) | Clippy 用九十年代界面风格呈现本地语言模型。 | 1122 | 275 | 2025-05-06 |
| 2 | [Show HN: Free, in-browser PDF editor](https://news.ycombinator.com/item?id=43880962) | 免费浏览器 PDF 编辑器，支持添加内容、签名、合并与密码保护且无需注册。 | 791 | 182 | 2025-05-03 |
| 3 | [Show HN: I rewrote my Mac Electron app in Rust](https://news.ycombinator.com/item?id=44118023) | 把本地照片视频搜索应用从 Electron 重写为 Rust，作者分享 Mac 应用改造。 | 597 | 443 | 2025-05-28 |
| 4 | [Show HN: My LLM CLI tool can run tools now, from Python code or plugins](https://news.ycombinator.com/item?id=44110584) | LLM 命令行工具加入工具调用，可通过 Python 代码或插件扩展。 | 529 | 165 | 2025-05-27 |
| 5 | [Show HN: Real-time AI Voice Chat at ~500ms Latency](https://news.ycombinator.com/item?id=43899028) | 作者展示实时 AI 语音聊天，并报告约五百毫秒延迟。 | 524 | 227 | 2025-05-05 |
| 6 | [Show HN: I built a synthesizer based on 3D physics](https://news.ycombinator.com/item?id=43873074) | Anukari 用三维物理驱动合成器，尝试让 GPU 参与音频处理。 | 512 | 123 | 2025-05-02 |
| 7 | [Show HN: I wrote a modern Command Line Handbook](https://news.ycombinator.com/item?id=44126612) | 作者更新现代 Linux 命令行手册，提供 2025 年版一百二十页 PDF。 | 454 | 109 | 2025-05-29 |
| 8 | [Show HN: Lazy Tetris](https://news.ycombinator.com/item?id=44103839) | Lazy Tetris 去掉计时、分数和重力，让玩家按自己的节奏堆方块。 | 438 | 150 | 2025-05-27 |
| 9 | [Show HN: Defuddle, an HTML-to-Markdown alternative to Readability](https://news.ycombinator.com/item?id=44067409) | Defuddle 提取网页正文与元信息并输出 Markdown，为 Readability 提供替代选择。 | 418 | 68 | 2025-05-22 |
| 10 | [Show HN: Onlook – Open-source, visual-first Cursor for designers](https://news.ycombinator.com/item?id=44127653) | Onlook 在无限画布上实时编辑 React 应用，面向设计师提供开源可视化工具。 | 408 | 81 | 2025-05-29 |

### 2025-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I'm an airline pilot – I built interactive graphs/globes of my flights](https://news.ycombinator.com/item?id=44396518) | 航空公司飞行员将数字飞行日志制作成交互图表与三维地球。 | 1539 | 197 | 2025-06-27 |
| 2 | [Show HN: Workout.cool – Open-source fitness coaching platform](https://news.ycombinator.com/item?id=44309320) | Workout.cool 继续探索开源健身指导，作者从原健身项目的贡献经历出发。 | 827 | 233 | 2025-06-18 |
| 3 | [Show HN: Unregistry – “docker push” directly to servers without a registry](https://news.ycombinator.com/item?id=44314085) | Unregistry 无需镜像仓库，直接把 Docker 镜像推送到服务器。 | 726 | 164 | 2025-06-18 |
| 4 | [Show HN: Kan.bn – An open-source alterative to Trello](https://news.ycombinator.com/item?id=44157177) | Kan.bn 用开源工具提供 Trello 式看板管理。 | 509 | 220 | 2025-06-02 |
| 5 | [Show HN: Air Lab – A portable and open air quality measuring device](https://news.ycombinator.com/item?id=44189329) | Air Lab 是开放便携空气质量设备，记录二氧化碳、温湿度与污染物等数据。 | 497 | 186 | 2025-06-05 |
| 6 | [Show HN: I made a 3D printed VTOL drone](https://news.ycombinator.com/item?id=44241278) | 九十天制作 3D 打印垂直起降无人机，作者报告三小时续航与远航程目标。 | 418 | 144 | 2025-06-10 |
| 7 | [Show HN: Chili3d – A open-source, browser-based 3D CAD application](https://news.ycombinator.com/item?id=44238171) | Chili3d 将 OpenCascade 编译到 WebAssembly，在浏览器提供开源三维 CAD。 | 408 | 117 | 2025-06-10 |
| 8 | [Show HN: I wrote a new BitTorrent tracker in Elixir](https://news.ycombinator.com/item?id=44323253) | 为学习 Elixir，作者编写高并发 BitTorrent tracker。 | 394 | 72 | 2025-06-19 |
| 9 | [Show HN: Chawan TUI web browser](https://news.ycombinator.com/item?id=44293260) | Chawan 用 Nim 制作终端浏览器，支持部分 CSS、JavaScript 与内联图片。 | 387 | 69 | 2025-06-16 |
| 10 | [Show HN: Spark, An advanced 3D Gaussian Splatting renderer for Three.js](https://news.ycombinator.com/item?id=44249565) | Spark 为 Three.js 提供开源高斯泼溅渲染，让新型三维内容更容易接入。 | 377 | 86 | 2025-06-11 |

### 2025-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Tinder but it's only pictures of my wife and I can only swipe right](https://news.ycombinator.com/item?id=44664873) | 开发者制作只展示妻子照片、且只能右滑的 Tinder 式应用。 | 1030 | 263 | 2025-07-23 |
| 2 | [Show HN: Ten years of running every day, visualized](https://news.ycombinator.com/item?id=44522683) | 连续十年每天至少跑一英里，作者用交互仪表盘可视化三千六百多天记录。 | 958 | 495 | 2025-07-10 |
| 3 | [Show HN: Draw a fish and watch it swim with the others](https://news.ycombinator.com/item?id=44719222) | 画一条鱼，再看它加入其他鱼一起游泳，作者展示互动网页实验。 | 935 | 234 | 2025-07-29 |
| 4 | [Show HN: Use Their ID – Use your local UK MP’s ID for the Online Safety Act](https://news.ycombinator.com/item?id=44716106) | Use Their ID 用议员证件的 AI 模拟图，抗议英国《在线安全法》的验证要求。 | 862 | 281 | 2025-07-28 |
| 5 | [Show HN: Shoggoth Mini – A soft tentacle robot powered by GPT-4o and RL](https://news.ycombinator.com/item?id=44572377) | Shoggoth Mini 将软体触手机器人与 GPT-4o、强化学习结合。 | 610 | 107 | 2025-07-15 |
| 6 | [Show HN: I wrote a "web OS" based on the Apple Lisa's UI, with 1-bit graphics](https://news.ycombinator.com/item?id=44482965) | 用原生 JavaScript 重现 Apple Lisa 风格“网页操作系统”，采用单色图形。 | 516 | 142 | 2025-07-06 |
| 7 | [Show HN: Pangolin – Open source alternative to Cloudflare Tunnels](https://news.ycombinator.com/item?id=44526015) | Pangolin 提供自托管隧道反向代理，通过 WireGuard 连接和身份权限控制资源。 | 500 | 125 | 2025-07-10 |
| 8 | [Show HN: Spegel, a Terminal Browser That Uses LLMs to Rewrite Webpages](https://news.ycombinator.com/item?id=44433409) | Spegel 在终端浏览网页，并借语言模型改写页面内容。 | 426 | 180 | 2025-07-01 |
| 9 | [Show HN: CSS generator for a high-def glass effect](https://news.ycombinator.com/item?id=44445238) | 通过叠加 CSS 属性生成高清玻璃效果，作者分享数月跨浏览器实验。 | 420 | 117 | 2025-07-02 |
| 10 | [Show HN: Refine – A Local Alternative to Grammarly](https://news.ycombinator.com/item?id=44556684) | Refine 提供本地写作辅助，尝试成为 Grammarly 的替代选择。 | 408 | 210 | 2025-07-14 |

### 2025-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I spent 6 years building a ridiculous wooden pixel display](https://news.ycombinator.com/item?id=44787902) | 开发者耗时六年制作千像素木质显示器，邀请全球用户投票绘图。 | 1145 | 144 | 2025-08-04 |
| 2 | [Show HN: Kitten TTS – 25MB CPU-Only, Open-Source TTS Model](https://news.ycombinator.com/item?id=44807868) | Kitten TTS 推出小于 25MB 的开源语音模型，面向仅用 CPU 的设备应用。 | 1003 | 361 | 2025-08-06 |
| 3 | [Show HN: I was curious about spherical helix, ended up making this visualization](https://news.ycombinator.com/item?id=44962066) | 为了理解球面螺旋线，作者重温参数方程并制作交互可视化。 | 865 | 132 | 2025-08-20 |
| 4 | [Show HN: The current sky at your approximate location, as a CSS gradient](https://news.ycombinator.com/item?id=44846281) | 用 CSS 渐变显示所在大致位置的天空，根据大气模型每分钟更新色彩。 | 788 | 160 | 2025-08-09 |
| 5 | [Show HN: Building a web search engine from scratch with 3B neural embeddings](https://news.ycombinator.com/item?id=44878151) | 从零制作 Web 搜索引擎，作者使用三十亿神经嵌入表示。 | 699 | 118 | 2025-08-12 |
| 6 | [Show HN: Base, an SQLite database editor for macOS](https://news.ycombinator.com/item?id=45014131) | Base 3 为 macOS 提供原生 SQLite 编辑体验，避免工具膨胀成大型 IDE。 | 693 | 181 | 2025-08-25 |
| 7 | [Show HN: I built an app to block Shorts and Reels](https://news.ycombinator.com/item?id=44923520) | 想看朋友动态却不想刷两小时，作者制作应用屏蔽 Shorts 与 Reels 内容流。 | 690 | 305 | 2025-08-16 |
| 8 | [Show HN: Whispering – Open-source, local-first dictation you can trust](https://news.ycombinator.com/item?id=44942731) | Whispering 提供开源、本地优先的听写工具，回应作者对封闭转录服务的顾虑。 | 591 | 152 | 2025-08-18 |
| 9 | [Show HN: NextDNS Adds "Bypass Age Verification"](https://news.ycombinator.com/item?id=44931824) | NextDNS 新增绕过年龄验证功能，作者以证件上传的隐私风险解释设计。 | 537 | 199 | 2025-08-17 |
| 10 | [Show HN: OverType – A Markdown WYSIWYG editor that's just a textarea](https://news.ycombinator.com/item?id=44932651) | OverType 只靠文本输入框实现 Markdown 所见即所得，追求低复杂度编辑。 | 471 | 99 | 2025-08-17 |

### 2025-09

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: A store that generates products from anything you type in search](https://news.ycombinator.com/item?id=45231378) | 一家可根据用户输入的搜索内容生成商品的商店。 | 1184 | 333 | 2025-09-13 |
| 2 | [Show HN: Term.everything – Run any GUI app in the terminal](https://news.ycombinator.com/item?id=45181535) | Term.everything 用自制 Wayland 合成器把图形应用显示在终端。 | 1094 | 144 | 2025-09-09 |
| 3 | [Show HN: I recreated Windows XP as my portfolio](https://news.ycombinator.com/item?id=45154609) | 把 Windows XP 桌面重建为个人作品集，作者实现多年记住的网页点子。 | 1032 | 323 | 2025-09-07 |
| 4 | [Show HN: The text disappears when you screenshot it](https://news.ycombinator.com/item?id=45284311) | 截图时文字会消失，作者展示围绕页面捕捉的特别实验。 | 568 | 193 | 2025-09-18 |
| 5 | [Show HN: Dayflow – A git log for your day](https://news.ycombinator.com/item?id=45361268) | Dayflow 自动理解屏幕上的工作内容，为一天生成语义活动时间线。 | 480 | 130 | 2025-09-24 |
| 6 | [Show HN: I'm a dermatologist and I vibe coded a skin cancer learning app](https://news.ycombinator.com/item?id=45157020) | 一位皮肤科医生借 AI 编程制作皮肤癌学习应用，分享数小时的开发成果。 | 429 | 259 | 2025-09-07 |
| 7 | [Show HN: I'm making an open-source platform for learning Japanese](https://news.ycombinator.com/item?id=45152940) | 日语学习者自建免费开源平台，希望像 Monkeytype 一样方便持续练习。 | 288 | 88 | 2025-09-06 |
| 8 | [Show HN: Toolbrew – Free little tools without signups or ads](https://news.ycombinator.com/item?id=45404667) | Toolbrew 集中文本转换等免费小工具，省去注册、广告与杂乱工具站。 | 269 | 58 | 2025-09-28 |
| 9 | [Show HN: WeUseElixir - Elixir project directory](https://news.ycombinator.com/item?id=45306120) | WeUseElixir 整理 Elixir 项目目录，帮助发现使用这门语言的作品。 | 213 | 60 | 2025-09-19 |
| 10 | [Show HN: Glide, an extensible, keyboard-focused web browser](https://news.ycombinator.com/item?id=45430294) | Glide 以键盘操作为中心，提供可扩展的网页浏览器。 | 207 | 52 | 2025-09-30 |

### 2025-10

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Strange Attractors](https://news.ycombinator.com/item?id=45777810) | 作者用 Three.js 可视化奇异吸引子，重拾探索数学图形的乐趣。 | 804 | 78 | 2025-10-31 |
| 2 | [Show HN: Autism Simulator](https://news.ycombinator.com/item?id=45438346) | Autism Simulator 基于作者与朋友的经历，呈现社交伪装和决策疲劳等感受。 | 779 | 857 | 2025-10-01 |
| 3 | [Show HN: I invented a new generative model and got accepted to ICLR](https://news.ycombinator.com/item?id=45536694) | 作者提出离散分布网络生成模型，并分享论文获 ICLR 2025 接收的进展。 | 656 | 91 | 2025-10-10 |
| 4 | [Show HN: Timelinize – Privately organize your own data from everywhere, locally](https://news.ycombinator.com/item?id=45504973) | Timelinize 在本地私密整理来自各处的个人数据，作者坚持业余开发十余年。 | 630 | 163 | 2025-10-07 |
| 5 | [Show HN: SQLite Online – 11 years of solo development, 11K daily users](https://news.ycombinator.com/item?id=45567770) | SQLite Online 独立开发十一年，作者分享日用户达到一万一千人的历程。 | 465 | 142 | 2025-10-13 |
| 6 | [Show HN: I built a web framework in C](https://news.ycombinator.com/item?id=45526890) | 作者用 C 编写 Web 框架，探索底层语言的应用开发路径。 | 420 | 218 | 2025-10-09 |
| 7 | [Show HN: I've built a tiny hand-held keyboard](https://news.ycombinator.com/item?id=45529393) | 用塑形黏土手工制作微型手持键盘，作者展示 3D 打印之外的外壳做法。 | 411 | 107 | 2025-10-09 |
| 8 | [Show HN: Halloy – Modern IRC client](https://news.ycombinator.com/item?id=45590949) | Halloy 用 Rust 制作现代跨平台 IRC 客户端，回应作者二十年的社区经历。 | 381 | 101 | 2025-10-15 |
| 9 | [Show HN: I'm building a browser for reverse engineers](https://news.ycombinator.com/item?id=45492489) | 为逆向工程师设计浏览器，作者探索专门工作流下的浏览工具。 | 348 | 55 | 2025-10-06 |
| 10 | [Show HN: I'm making a detective game built on Wikipedia](https://news.ycombinator.com/item?id=45617948) | 以维基百科为基础制作免费侦探游戏，邀请玩家尝试推理。 | 318 | 43 | 2025-10-17 |

### 2025-11

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I built a synth for my daughter](https://news.ycombinator.com/item?id=45900425) | 开发者为女儿制作合成器。 | 1278 | 209 | 2025-11-12 |
| 2 | [Show HN: Boing](https://news.ycombinator.com/item?id=46093473) | Boing 项目亮相，作者邀请社区看看这次带来的作品。 | 782 | 147 | 2025-11-30 |
| 3 | [Show HN: Wealthfolio 2.0- Open source investment tracker. Now Mobile and Docker](https://news.ycombinator.com/item?id=46006016) | Wealthfolio 2.0 扩展到移动端和 Docker，继续提供开源投资记录。 | 676 | 215 | 2025-11-21 |
| 4 | [Show HN: I scraped 3B Goodreads reviews to train a better recommendation model](https://news.ycombinator.com/item?id=45825733) | 作者用大量 Goodreads 评论训练推荐模型，根据已读书目寻找下一本书。 | 606 | 259 | 2025-11-05 |
| 5 | [Show HN: I made a down detector for down detector](https://news.ycombinator.com/item?id=45974012) | Cloudflare 故障连带击倒故障检测站，作者再做一个独立检测它的工具。 | 591 | 170 | 2025-11-19 |
| 6 | [Show HN: I built an interactive HN Simulator](https://news.ycombinator.com/item?id=46036908) | 交互式 HN 模拟器允许发帖和链接，再由语言模型即时生成评论。 | 538 | 215 | 2025-11-24 |
| 7 | [Show HN: Glasses to detect smart-glasses that have cameras](https://news.ycombinator.com/item?id=46075882) | 一副用于检测带摄像头智能眼镜的眼镜，作者关注隐蔽拍摄问题。 | 509 | 193 | 2025-11-28 |
| 8 | [Show HN: Forty.News – Daily news, but on a 40-year delay](https://news.ycombinator.com/item?id=46017175) | Forty.News 每天发布四十年前的新闻，拉开与当下焦虑新闻的距离。 | 443 | 180 | 2025-11-22 |
| 9 | [Show HN: Why write code if the LLM can just do the thing? (web app experiment)](https://news.ycombinator.com/item?id=45783640) | 把联系人管理请求直接交给语言模型执行，作者试验 AI 能否代替应用代码。 | 436 | 324 | 2025-11-01 |
| 10 | [Show HN: We built an open source, zero webhooks payment processor](https://news.ycombinator.com/item?id=46048252) | Flowglad 提供开源支付处理工具，希望免用 webhook 完成支付集成。 | 405 | 223 | 2025-11-25 |

### 2025-12

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Gemini Pro 3 imagines the HN front page 10 years from now](https://news.ycombinator.com/item?id=46205632) | 开发者展示 Gemini 3 Pro 想象的十年后 HN 首页。 | 3346 | 965 | 2025-12-09 |
| 2 | [Show HN: Jmail – Google Suite for Epstein files](https://news.ycombinator.com/item?id=46339600) | Jmail 用类似谷歌办公套件的界面展示爱泼斯坦相关文件。 | 1557 | 363 | 2025-12-20 |
| 3 | [Show HN: Hacker Book – All the HN Belong to You 2006 – 2025](https://news.ycombinator.com/item?id=46435308) | 《Hacker Book》回看 2006 至 2025 年 Hacker News 内容。 | 730 | 221 | 2025-12-30 |
| 4 | [Show HN: Books mentioned on Hacker News in 2025](https://news.ycombinator.com/item?id=46345897) | 整理 2025 年 Hacker News 提到的书籍，回顾社区的阅读兴趣。 | 613 | 212 | 2025-12-21 |
| 5 | [Show HN: Witr – Explain why a process is running on your Linux system](https://news.ycombinator.com/item?id=46392910) | Witr 解释 Linux 进程为何运行、由谁启动，追踪看不懂的后台活动。 | 526 | 105 | 2025-12-26 |
| 6 | [Show HN: Z80-μLM, a 'Conversational AI' That Fits in 40KB](https://news.ycombinator.com/item?id=46417815) | Z80-μLM 将字符语言模型压缩到 40KB，在 Z80 上尝试微型“对话 AI”。 | 514 | 122 | 2025-12-29 |
| 7 | [Show HN: Minimalist editor that lives in browser, stores everything in the URL](https://news.ycombinator.com/item?id=46378554) | 极简浏览器编辑器把笔记存在 URL 片段中，单个 HTML 文件即可分享与使用。 | 468 | 168 | 2025-12-24 |
| 8 | [Show HN: Picknplace.js, an alternative to drag-and-drop](https://news.ycombinator.com/item?id=46290349) | Picknplace.js 把拖放拆成先选后放两步，减少手机上边拖边滚的操作困难。 | 455 | 152 | 2025-12-16 |
| 9 | [Show HN: WalletWallet – create Apple passes from anything](https://news.ycombinator.com/item?id=46345745) | WalletWallet 为没有 Apple Wallet 支持的卡券生成已签名通行证。 | 448 | 115 | 2025-12-21 |
| 10 | [Show HN: Vibium – Browser automation for AI and humans, by Selenium's creator](https://news.ycombinator.com/item?id=46377597) | Selenium 作者重新思考浏览器自动化，推出同时面向 AI 代理与人的 Vibium。 | 443 | 124 | 2025-12-24 |

### 2026-01

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: isometric.nyc – giant isometric pixel art map of NYC](https://news.ycombinator.com/item?id=46721802) | isometric.nyc 展示巨大的纽约等距像素艺术地图。 | 1325 | 241 | 2026-01-22 |
| 2 | [Show HN: ChartGPU – WebGPU-powered charting library (1M points at 60fps)](https://news.ycombinator.com/item?id=46706528) | ChartGPU 用 WebGPU 绘图，作者报告百万数据点可达每秒六十帧。 | 670 | 214 | 2026-01-21 |
| 3 | [Show HN: I made a memory game to teach you to play piano by ear](https://news.ycombinator.com/item?id=46556210) | 通过记忆游戏练习凭耳朵弹钢琴，把听辨与演奏连接起来。 | 565 | 171 | 2026-01-09 |
| 4 | [Show HN: Sweep, Open-weights 1.5B model for next-edit autocomplete](https://news.ycombinator.com/item?id=46713106) | Sweep 开放十五亿参数模型，预测代码的下一步修改并提供 JetBrains 插件。 | 534 | 153 | 2026-01-21 |
| 5 | [Show HN: I used Claude Code to discover connections between 100 books](https://news.ycombinator.com/item?id=46567400) | 作者让 Claude Code 阅读一百本非虚构书，寻找跨书联系以深化阅读。 | 524 | 146 | 2026-01-10 |
| 6 | [Show HN: I trained a 9M speech model to fix my Mandarin tones](https://news.ycombinator.com/item?id=46832074) | 为纠正自己的普通话声调，作者训练九百万参数模型并放到浏览器逐音节评分。 | 469 | 153 | 2026-01-31 |
| 7 | [Show HN: Terminal UI for AWS](https://news.ycombinator.com/item?id=46491749) | 在终端管理 AWS，作者提供文本交互界面。 | 390 | 210 | 2026-01-04 |
| 8 | [Show HN: Prism.Tools – Free and privacy-focused developer utilities](https://news.ycombinator.com/item?id=46511469) | Prism.Tools 汇集免费客户端开发工具，处理数据时关注用户隐私。 | 380 | 104 | 2026-01-06 |
| 9 | [Show HN: The HN Arcade](https://news.ycombinator.com/item?id=46793693) | HN Arcade 整理社区成员制作的小游戏，避免好玩的作品被遗忘。 | 352 | 123 | 2026-01-28 |
| 10 | [Show HN: DoNotNotify – log and intelligently block notifications on Android](https://news.ycombinator.com/item?id=46499646) | DoNotNotify 在 Android 记录并智能拦截通知，回应应用滥用通知的问题。 | 347 | 168 | 2026-01-05 |

### 2026-02

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I spent 3 years reverse-engineering a 40 yo stock market sim from 1986](https://news.ycombinator.com/item?id=46954696) | 花三年逆向重制 1986 年的《Wall Street Raider》，作者复兴老股市模拟游戏。 | 721 | 240 | 2026-02-10 |
| 2 | [Show HN: Micasa – track your house from the terminal](https://news.ycombinator.com/item?id=47075124) | Micasa 用终端和单个 SQLite 文件记录家务维护事项，无需账号或订阅。 | 657 | 218 | 2026-02-19 |
| 3 | [Show HN: Craftplan – I built my wife a production management tool for her bakery](https://news.ycombinator.com/item?id=46847690) | 为妻子的微型面包房自建 Craftplan，用开源工具管理配方和生产流程。 | 577 | 167 | 2026-02-01 |
| 4 | [Show HN: NanoClaw – "Clawdbot" in 500 lines of TS with Apple container isolation](https://news.ycombinator.com/item?id=46850205) | NanoClaw 用约五百行 TypeScript 核心代码配合 Apple 容器，隔离代理运行。 | 533 | 224 | 2026-02-01 |
| 5 | [Show HN: CIA World Factbook Archive (1990–2025), searchable and exportable](https://news.ycombinator.com/item?id=47114530) | 将 1990 至 2025 年《世界概况》整理成结构化档案，支持搜索、比较与导出。 | 496 | 99 | 2026-02-22 |
| 6 | [Show HN: Jemini (Gemini for the Epstein Files)](https://news.ycombinator.com/item?id=47031334) | Jemini 将 Gemini 与 Epstein 档案结合，展示专门围绕这批资料的项目。 | 488 | 103 | 2026-02-16 |
| 7 | [Show HN: AsteroidOS 2.0 – Nobody asked, we shipped anyway](https://news.ycombinator.com/item?id=47051852) | AsteroidOS 2.0 发布，作者用“没人要求，我们照样做了”介绍新版本。 | 470 | 68 | 2026-02-17 |
| 8 | [Show HN: Wikipedia as a doomscrollable social media feed](https://news.ycombinator.com/item?id=46850803) | 把维基百科排成可以不断刷下去的社交内容流。 | 441 | 142 | 2026-02-02 |
| 9 | [Show HN: Algorithmically Finding the Longest Line of Sight on Earth](https://news.ycombinator.com/item?id=46943568) | 用 Rust 与 SIMD 穷举地球最长视线，作者报告找到约 530 公里的观测路径。 | 412 | 181 | 2026-02-09 |
| 10 | [Show HN: If you lose your memory, how to regain access to your computer?](https://news.ycombinator.com/item?id=46916609) | 担心脑震荡后忘记密码，作者把秘密分享与加密组合成离线账户恢复工具。 | 402 | 233 | 2026-02-06 |

### 2026-03

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I took back Video.js after 16 years and we rewrote it to be 88% smaller](https://news.ycombinator.com/item?id=47506713) | Video.js 原作者十六年后重启项目，称重写后体积减少了 88%。 | 648 | 137 | 2026-03-24 |
| 2 | [Show HN: Turn Your YouTube Subscriptions into a Retro TV Guide](https://news.ycombinator.com/item?id=47336100) | 把 YouTube 订阅变成复古电视节目表，减少选择太多时的观看犹豫。 | 604 | 179 | 2026-03-11 |
| 3 | [Show HN: I built a sub-500ms latency voice agent from scratch](https://news.ycombinator.com/item?id=47224295) | 作者从零构建语音代理，报告完整语音识别到合成链路平均延迟约四百毫秒。 | 570 | 153 | 2026-03-02 |
| 4 | [Show HN: Three new Kitten TTS models – smallest less than 25MB](https://news.ycombinator.com/item?id=47441546) | Kitten TTS 新增三种开源语音模型，最小版本低于 25MB。 | 561 | 181 | 2026-03-19 |
| 5 | [Show HN: How I Topped the HuggingFace Open LLM Leaderboard on Two Gaming GPUs](https://news.ycombinator.com/item?id=47322887) | 作者分享如何用两张游戏显卡登上 Hugging Face 开放语言模型榜首。 | 495 | 126 | 2026-03-10 |
| 6 | [Show HN: Gemini can now natively embed video, so I built sub-second video search](https://news.ycombinator.com/item?id=47503617) | 利用 Gemini 原生视频嵌入做视频搜索，作者报告亚秒级查询体验。 | 438 | 108 | 2026-03-24 |
| 7 | [Show HN: 1-Bit Bonsai, the First Commercially Viable 1-Bit LLMs](https://news.ycombinator.com/item?id=47593422) | 1-Bit Bonsai 展示一比特语言模型，作者将其定位为具备商业可用性。 | 430 | 153 | 2026-03-31 |
| 8 | [Show HN: s@: decentralized social networking over static sites](https://news.ycombinator.com/item?id=47344548) | s@ 依托静态网站实现去中心化社交网络。 | 414 | 218 | 2026-03-12 |
| 9 | [Show HN: Hacker News archive (47M+ items, 11.6GB) as Parquet, updated every 5m](https://news.ycombinator.com/item?id=47378781) | 将四千七百多万条 HN 数据做成 Parquet 档案，并每五分钟更新。 | 408 | 167 | 2026-03-14 |
| 10 | [Show HN: I built 48 lightweight SVG backgrounds you can copy/paste](https://news.ycombinator.com/item?id=47427299) | 四十八种轻量 SVG 背景，支持直接复制粘贴到项目。 | 403 | 67 | 2026-03-18 |

### 2026-04

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: A game where you build a GPU](https://news.ycombinator.com/item?id=47640728) | 觉得 GPU 架构学习资源不足，作者把搭建 GPU 做成游戏。 | 964 | 187 | 2026-04-04 |
| 2 | [Show HN: I built a tiny LLM to demystify how language models work](https://news.ycombinator.com/item?id=47655408) | 用约九百万参数、百余行 PyTorch 从零训练小语言模型，帮助理解其工作方式。 | 915 | 134 | 2026-04-06 |
| 3 | [Show HN: Brutalist Concrete Laptop Stand (2024)](https://news.ycombinator.com/item?id=47673360) | 用粗野主义混凝土设计笔记本支架，展示实物设计作品。 | 786 | 240 | 2026-04-07 |
| 4 | [Show HN: I built a frontpage for personal blogs](https://news.ycombinator.com/item?id=47625952) | Blogosphere 汇集个人博客的新文章，为独立写作者建立发现首页。 | 783 | 195 | 2026-04-03 |
| 5 | [Show HN: Apfel – The free AI already on your Mac](https://news.ycombinator.com/item?id=47624645) | Apfel 展示 Mac 上已有的免费 AI，探索本机智能能力的使用。 | 743 | 157 | 2026-04-03 |
| 6 | [Show HN: boringBar – a taskbar-style dock replacement for macOS](https://news.ycombinator.com/item?id=47742200) | 从 GNOME 转到 Mac 后，作者制作任务栏风格 Dock 替代品 boringBar。 | 520 | 308 | 2026-04-12 |
| 7 | [Show HN: Pardonned.com – A searchable database of US Pardons](https://news.ycombinator.com/item?id=47727960) | Pardonned.com 整理可搜索的美国赦免数据库，帮助查证视频里的说法。 | 501 | 276 | 2026-04-11 |
| 8 | [Show HN: Smol machines – subsecond coldstart, portable virtual machines](https://news.ycombinator.com/item?id=47808268) | Smol machines 提供可移植虚拟机，作者主打亚秒级冷启动。 | 499 | 152 | 2026-04-17 |
| 9 | [Show HN: Is Hormuz Open Yet?](https://news.ycombinator.com/item?id=47696562) | 作者把“霍尔木兹海峡开放了吗”这个问题做成独立项目。 | 484 | 209 | 2026-04-08 |
| 10 | [Show HN: Ghost Pepper – 100% local hold-to-talk speech-to-text for macOS](https://news.ycombinator.com/item?id=47666024) | Ghost Pepper 在 macOS 本地按住说话即可转写，开源且不上传语音数据。 | 467 | 200 | 2026-04-06 |

### 2026-05

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model](https://news.ycombinator.com/item?id=48111896) | Needle 把 Gemini 工具调用能力蒸馏到两千六百万参数模型，面向消费级设备。 | 776 | 211 | 2026-05-12 |
| 2 | [Show HN: Red Squares – GitHub outages as contributions](https://news.ycombinator.com/item?id=48034587) | Red Squares 把 GitHub 故障画成类似贡献记录的方格，用熟悉的图形呈现服务中断。 | 767 | 170 | 2026-05-06 |
| 3 | [Show HN: Files.md – open-source alternative to Obsidian](https://news.ycombinator.com/item?id=48179677) | Files.md 提供开源知识工具，尝试替代 Obsidian。 | 730 | 356 | 2026-05-18 |
| 4 | [Show HN: Audiomass – a free, open-source multitrack audio editor for the web](https://news.ycombinator.com/item?id=48258015) | Audiomass 在网页里提供免费的开源多轨音频编辑器。 | 553 | 120 | 2026-05-24 |
| 5 | [Show HN: Semble – Code search for agents that uses 98% fewer tokens than grep](https://news.ycombinator.com/item?id=48169874) | Semble 为代码代理提供搜索，作者称相较 grep 可减少 98% 的词元消耗。 | 445 | 151 | 2026-05-17 |
| 6 | [Show HN: Building a web server in assembly to give my life (a lack of) meaning](https://news.ycombinator.com/item?id=48080587) | 用 ARM64 汇编为 macOS 写静态文件服务器，作者给自己找了个底层挑战。 | 430 | 227 | 2026-05-10 |
| 7 | [Show HN: Freenet, a peer-to-peer platform for decentralized apps](https://news.ycombinator.com/item?id=48223362) | Freenet 经过多年重新设计，提供运行去中心化应用的点对点平台。 | 390 | 271 | 2026-05-21 |
| 8 | [Show HN: Continue? Y/N: A 60-second game about AI agent permission fatigue](https://news.ycombinator.com/item?id=48308376) | 《Continue? Y/N》用六十秒游戏呈现 AI 代理不断询问权限带来的疲劳。 | 386 | 162 | 2026-05-28 |
| 9 | [Show HN: Hallucinopedia](https://news.ycombinator.com/item?id=48038257) | Hallucinopedia 把“幻觉”与百科概念结合，展示作者的创作实验。 | 317 | 267 | 2026-05-06 |
| 10 | [Show HN: Find the best local LLM for your hardware, ranked by benchmarks](https://news.ycombinator.com/item?id=48146369) | 根据硬件和基准测试排名，寻找适合本机运行的语言模型。 | 283 | 68 | 2026-05-15 |

### 2026-06

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Performative-UI – a react component library of design tropes](https://news.ycombinator.com/item?id=48445554) | Performative-UI 把常见设计套路做成 React 组件库。 | 1181 | 213 | 2026-06-08 |
| 2 | [Show HN: I made Google Trends for Hacker News by indexing 18 years of comments](https://news.ycombinator.com/item?id=48673671) | 索引十八年 HN 评论，制作社区版 Google Trends 来观察话题走势。 | 822 | 156 | 2026-06-25 |
| 3 | [Show HN: Kage – Shadow any website to a single binary for offline viewing](https://news.ycombinator.com/item?id=48529990) | Kage 把网站封装成单个可执行文件，方便离线查看。 | 712 | 141 | 2026-06-14 |
| 4 | [Show HN: FablePool – pool money behind a prompt, and Fable builds it in public](https://news.ycombinator.com/item?id=48496539) | FablePool 让用户为同一提示词集资，再由 Fable 公开构建成果。 | 526 | 276 | 2026-06-11 |
| 5 | [Show HN: Are You in the Weights?](https://news.ycombinator.com/item?id=48591348) | Are You in the Weights? 查询多个模型，看看自己的痕迹是否被语言模型认识。 | 471 | 247 | 2026-06-18 |
| 6 | [Show HN: TikZ Editor – WYSIWYG editor for figures in LaTeX](https://news.ycombinator.com/item?id=48645437) | TikZ Editor 为 LaTeX 插图提供所见即所得编辑，减少手调坐标与反复编译。 | 451 | 74 | 2026-06-23 |
| 7 | [Show HN: Chess-Inspired Roguelike](https://news.ycombinator.com/item?id=48616304) | 以国际象棋为灵感制作 Roguelike，作者探索棋类规则的新组合。 | 433 | 149 | 2026-06-21 |
| 8 | [Show HN: Lathe – Use LLMs to learn a new domain, not skip past it](https://news.ycombinator.com/item?id=48433756) | Lathe 用语言模型生成有来源的实作教程，再让用户亲手阅读和编写代码学习。 | 402 | 72 | 2026-06-07 |
| 9 | [Show HN: Zanagrams](https://news.ycombinator.com/item?id=48708182) | Zanagrams 项目亮相，作者邀请社区体验自己的新作品。 | 400 | 107 | 2026-06-28 |
| 10 | [Show HN: OpenKnowledge – open-source alternative to Obsidian/Notion](https://news.ycombinator.com/item?id=48675435) | OpenKnowledge 用开源知识管理工具，尝试替代 Obsidian 与 Notion。 | 381 | 173 | 2026-06-25 |

### 2026-07

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: I replaced a $120k bowling center system with $1,600 in ESP32s](https://news.ycombinator.com/item?id=48968606) | 经营八道保龄球馆的工程师，用一千六百美元 ESP32 替代昂贵控制系统。 | 2935 | 359 | 2026-07-19 |
| 2 | [Show HN: 18 Words](https://news.ycombinator.com/item?id=48845049) | “18 Words”项目展示，作者以十八个词为名介绍自己的作品。 | 1160 | 366 | 2026-07-09 |
| 3 | [Show HN: Bento - An entire PowerPoint in one HTML file (edit+view+data+collab)](https://news.ycombinator.com/item?id=49008211) | Bento 把演示文稿编辑、播放、数据和协作放进单个 HTML 文件。 | 1033 | 239 | 2026-07-22 |
| 4 | [Show HN: Open-source engine running Gemma 4 26B in 2 GB RAM on any M-series Mac](https://news.ycombinator.com/item?id=49098510) | TurboFieldfare 用 Swift 与 Metal 推理 Gemma 4，作者称 26B 模型只需约 2GB 内存。 | 919 | 342 | 2026-07-29 |
| 5 | [Show HN: Echo – Fable-level results at 1/3 the cost using open-weight models](https://news.ycombinator.com/item?id=49026810) | Echo 协调多个开放权重模型，作者称可用三分之一成本达到 Fable 级效果。 | 484 | 228 | 2026-07-23 |
| 6 | [Show HN: Physically accurate black hole you can put in your room](https://news.ycombinator.com/item?id=49021270) | 天体物理学家把相对论光线追踪带到浏览器，让黑洞模拟进入房间场景。 | 477 | 193 | 2026-07-23 |
| 7 | [Show HN: I was tired of opening 2 tabs for every HN link, so I made a userscript](https://news.ycombinator.com/item?id=49090607) | 不想每次同时打开文章和评论两个标签，作者用用户脚本改善 HN 阅读。 | 433 | 126 | 2026-07-28 |
| 8 | [Show HN: Searchable directory of 22k+ products from worker-owned co-ops](https://news.ycombinator.com/item?id=48752905) | 可搜索的员工所有合作社产品目录，汇集两万两千多种商品。 | 398 | 82 | 2026-07-01 |
| 9 | [Show HN: Super Dario](https://news.ycombinator.com/item?id=48896286) | Super Dario 项目展示，作者向社区介绍自己的创作。 | 397 | 100 | 2026-07-13 |
| 10 | [Show HN: Davit, a Apple Containers UI](https://news.ycombinator.com/item?id=48821848) | Davit 为 Apple Containers 提供开源图形前端，作者先满足自己的使用需求。 | 389 | 101 | 2026-07-07 |

### 2026-08

| 排名 | 帖子原题 | 中文导读 | 得分 | 评论数 | UTC 日期 |
|---:|---|---|---:|---:|---|
| 1 | [Show HN: Simple algorithm and color space to generate diverse skin tones](https://news.ycombinator.com/item?id=49170165) | 为数字绘画和游戏选择多样肤色，作者设计专用色彩空间与生成算法。 | 627 | 99 | 2026-08-04 |
| 2 | [Show HN: I trained a 125M model to autocomplete piano on-device](https://news.ycombinator.com/item?id=49373456) | 训练一亿两千五百万参数模型实时续弹钢琴，用 MIDI 音符作为音乐提示。 | 598 | 117 | 2026-08-20 |
| 3 | [Show HN: Needle2: 14MB agentic LLM for phones, wearables, smart home and robots](https://news.ycombinator.com/item?id=49246804) | Needle2 将手机、穿戴设备与小型机器人的工具调用模型压缩到 14MB。 | 537 | 185 | 2026-08-10 |
| 4 | [Show HN: Huzzah – a novel approach to coding with AI](https://news.ycombinator.com/item?id=49378768) | Huzzah 是实验性 AI 编程编辑器，作者希望缓解长期使用代码代理的疲劳。 | 384 | 209 | 2026-08-20 |
| 5 | [Show HN: Isopolis – isometric pixel map of SF](https://news.ycombinator.com/item?id=49149966) | Isopolis 用等距像素风格描绘旧金山地图。 | 350 | 81 | 2026-08-03 |
| 6 | [Show HN: I'm a 15 Year Old Wannabe Engineer, This Is a Cycloidal Gearbox I Built](https://news.ycombinator.com/item?id=49140396) | 一位 15 岁工程爱好者展示自己制作的摆线减速箱。 | 338 | 115 | 2026-08-02 |
| 7 | [Show HN: iPhone app takes simultaneous images from 2 lenses, fuses into 1 photo](https://news.ycombinator.com/item?id=49226623) | iPhone 应用同时调用两个镜头拍照，再融合成一张图像。 | 329 | 305 | 2026-08-08 |
| 8 | [Show HN: Woxi - Open-source Mathematica / Wolfram Language reimplementation](https://news.ycombinator.com/item?id=49270040) | Woxi 用 Rust 重新实现 Wolfram Language，并提供类 Mathematica 界面与多种入口。 | 314 | 46 | 2026-08-12 |
| 9 | [Show HN: I spent 2 years designing a mechanical Magic Keyboard](https://news.ycombinator.com/item?id=49197137) | 两年设计 Altar II 超薄机械键盘，作者希望替代 Magic Keyboard 并加入可拆旋钮。 | 306 | 245 | 2026-08-06 |
| 10 | [Show HN: Scroll through all 43252003274489856000 Rubik's Cube states](https://news.ycombinator.com/item?id=49251179) | 滚动浏览魔方的全部可能状态，作者把巨大的组合空间做成探索项目。 | 295 | 122 | 2026-08-10 |
