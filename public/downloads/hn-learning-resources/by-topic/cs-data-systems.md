# 从SQL走向数据库与分布式系统

如何从写查询进入索引、事务、数据库内部与分布式一致性？

数据库求学帖首先区分“使用”与“构建”；大学课、索引指南和反模式图书提供不同入口，再由DDIA与MIT实验进入数据复制与故障。

本主题收录 6 项资源。[返回主题索引](../学习主题.md)

主题讨论线索：[Ask HN: Resources for Learning about Databases](https://news.ycombinator.com/item?id=21033951)；[Learning to Build Distributed Systems](https://news.ycombinator.com/item?id=20249946)；[Teach Yourself Computer Science](https://news.ycombinator.com/item?id=23588896)；[Ask HN: What's the best lecture series you've ever seen?](https://news.ycombinator.com/item?id=34591291)；[Ask HN: What are some of the best university courses available online for free?](https://news.ycombinator.com/item?id=35536042)；[Learning about distributed systems: where to start? (2020)](https://news.ycombinator.com/item?id=40037324)

### MIT 6.824 / Distributed Systems

MIT / Robert Morris及课程团队 · 大学课程 / 论文阅读 / Go实验

通过论文阅读和Go实验理解MapReduce、Raft、容错键值存储及分片。适合已掌握系统与网络基础、愿意为并发和故障调试投入时间的人。

**适合谁／先修：**建议先学操作系统与网络，并能用Go完成多阶段实验；课程较难。

**推荐理由：**多位完课或旁听者把实验视为理解细节的关键，尤其是必须通过测试的Raft实现；同时明确它不直接等于生产系统建设能力。

[资源入口](https://pdos.csail.mit.edu/6.824/)

**使用备注：**评论跨越2013、2020、2023、2024等课程版本，实验语言与内容历年有变化；按官网当前学期选用一整套材料。

**推荐 · [eddyerburgh / 23590126](https://news.ycombinator.com/item?id=23590126)**：完成整门课的学习者说明实验怎样迫使理解协议细节。

> The labs were especially useful because they forced me to really understand the details of the topics I had learned (e.g., MapReduce, Raft, Raft’s log compaction) in order for my code to pass all the tests.

**推荐 · [valzam / 34605038](https://news.ycombinator.com/item?id=34605038)**：另一位学习者具体推荐论文加讲解的安排与Raft实现。

> In particular the Distributed Systems one has an amazing format (read a paper each week, the lecture goes into detail about the nuances). Also implementing raft was challenging and frustrating but incredibly fun.

**有条件推荐 · [pquki4 / 40048131](https://news.ycombinator.com/item?id=40048131)**：明确区分课程知识与生产系统经验。

> Of course this does not prepare you for building a production-ready system, but you can go very far with what you learn from the course.

### Designing Data-Intensive Applications

Martin Kleppmann · 技术教材

把数据编码、复制、共识、一致性和事务隔离放在同一框架下讲解。适合已有数据库使用经验、希望理解可靠数据系统设计取舍的人。

**适合谁／先修：**建议有实际编程与数据库使用经历；可作为进入论文阅读的桥梁。

**推荐理由：**数据库求学帖和分布式系统帖的独立读者都推荐；具体称赞包括隔离级别、串行化与线性化的区分，以及建立直觉后的延伸阅读。

[资源入口](https://dataintensive.net/)

**使用备注：**证据主要指原版；不要把历史读者评价自动等同于后来版本的全部内容或作者组合。

**推荐 · [Tomte / 21037170](https://news.ycombinator.com/item?id=21037170)**：读者给出与数据库学习直接相关的具体收获。

> And IMO the best part, explaining very clearly different isolation levels and the difference between serializability and linearizability. The book is much more database-relevant than the title might make you think.

**推荐 · [wippler / 20251587](https://news.ycombinator.com/item?id=20251587)**：独立读者肯定它作为分布式系统入门与延伸阅读桥梁的作用。

> The book provides a gentle introduction to build intuition around these systems and contains a plethora of links to go further down the rabbit hole.

### CMU 15-445/645: Intro to Database Systems (Fall 2022)

Carnegie Mellon / Andy Pavlo · 大学课程 / C++数据库实验

学习关系型数据库如何实现，包括存储、索引、查询处理和事务，并以C++项目练习内部结构。适合已会编程、希望从“使用数据库”进到“理解数据库实现”的人。

**适合谁／先修：**建议有C++、数据结构和系统基础；名字虽是Intro，作业仍严格。

**推荐理由：**2023年大学课程征集帖给出了具体课程与课纲；读者特别报告了B+树C++实现和数据工程方面的收益。

[资源入口](https://15445.courses.cs.cmu.edu/fall2022/schedule.html)

**使用备注：**这里限定2022课纲；另行检索到的CMU15-721是研究生高级数据库课，不与15-445混为同一资源。网页课纲已缓存；未验证校内评分权限。

**有条件推荐 · [pocket_cheese / 35559188](https://news.ycombinator.com/item?id=35559188)**：学习者明确指出严谨程度、数据工程适用性以及C++ B+树练习。

> Don't be fooled by the course name though, it's pretty rigorous but so rewarding and practical (especially if you are a data engineer). I give this course an A+ for teaching me about B+ trees in C++ :D

**推荐 · [valzam / 34605038](https://news.ycombinator.com/item?id=34605038)**：同一评论者直接推荐父评论列出的CMU Intro to Database Systems与MIT6.824；不把其后仅针对MIT的细节挪用于CMU。

> Highly recommend both of these.

### Databases — Jennifer Widom

Stanford / Jennifer Widom · 大学数据库入门课 / 系列MOOC

建立关系数据库、SQL和数据查询的基础，通过覆盖讲授内容的逐级作业练习。适合想把数据库概念和写查询一起学扎实的人。

**适合谁／先修：**可作为数据库入门；需要亲自做查询题，并持续使用才能维持熟练度。

**推荐理由：**多个独立读者称赞课程组织和作业反馈；2023年的帖子还提供了拆成小课后的官方入口。

[资源入口](https://online.stanford.edu/courses/soe-ydatabases-databases)

**使用备注：**2023年推荐者说当时已在edX拆成5门小课；当前官方入口本次返回202空响应，未确认全部课堂是否仍可免费旁听。原评论涉及XPath/XQuery/XSLT，不能自动视为今天每门小课的内容。

入口检查：202；自动访问未成功，详见链接检查记录。历史推荐仍保留。

**推荐 · [sampo / 16745841](https://news.ycombinator.com/item?id=16745841)**：推荐者具体赞赏讲授与作业互相覆盖的设计。

> Everything in the lectures is relevant, everything from the lectures is applied and tested in the homework, there is lots of homework

**推荐 · [carusooneliner / 16746593](https://news.ycombinator.com/item?id=16746593)**：另一位学习者描述几年后仍可运用的数据库概念。

> The least I can say is the course helped me internalize database concepts. This course has the right amount of handholding yet challenges you enough so you acquire long-lasting skills.

**推荐 · [rjbwork / 35540523](https://news.ycombinator.com/item?id=35540523)**：2023年独立读者再次推荐，但明确经验来自首轮旧版。

> Seconding Widom's course. It's a fantastic primer on databases. I did it during the first run, back in like 2011 or 2012 or so. I can't imagine it's gotten any less relevant in the intervening years.

### SQL Antipatterns

Bill Karwin · 实务图书

借常见错误和对照示例学习SQL与关系数据库设计中应避免的做法。适合已经会基本SQL、开始维护实际数据库的人。

**适合谁／先修：**需要对SQL基础已有较好理解；不适合作为第一份SQL教程。

**推荐理由：**推荐者直接强调了基础门槛，以及具体示例对判断该做什么、不该做什么的帮助。

[资源入口](https://www.oreilly.com/library/view/sql-antipatterns/9781680500073/)

**使用备注：**证据指2019年读者使用的版本，原链接为O’Reilly图书页；与后续版本需分别核对。

入口检查：403；自动访问未成功，详见链接检查记录。历史推荐仍保留。

**有条件推荐 · [petepete / 21034230](https://news.ycombinator.com/item?id=21034230)**：具体图书推荐，同时明确需要SQL基础。

> Bill Karwin's SQL Antipatterns. You need a decent understanding of the basics to get the most from it, but there's some excellent information and examples of what to (and what not to) do.

### Use The Index, Luke!

Markus Winand · 在线数据库索引指南

围绕关系数据库索引建立SQL性能基础，理解查询与索引为什么匹配或失配。适合已经会基本查询、正在遇到慢查询的人。

**适合谁／先修：**建议已会SQL的基本查询语句。

**推荐理由：**数据库学习征集帖中的读者明确表示这是学习RDBMS索引的愉快而有用的资源。

[资源入口](https://use-the-index-luke.com/)

**使用备注：**本条是具体索引学习指南，范围比完整数据库实现课程窄。

**推荐 · [dbattaglia / 21034769](https://news.ycombinator.com/item?id=21034769)**：直接针对索引学习效果的读者推荐。

> I found this an enjoyable resource for learning about one of the fundamentals of RDBMS, indices: https://use-the-index-luke.com/

