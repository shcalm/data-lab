# 从逻辑门走到操作系统

代码下面究竟发生了什么，怎样通过实验理解硬件、内存和内核？

讨论反复推荐可运行的项目与实验：Nand2Tetris连起层次，CS:APP补系统视角，OSTEP与ops-class分别提供解释与内核动手训练。

本主题收录 6 项资源。[返回主题索引](../学习主题.md)

主题讨论线索：[Hack the Kernel – Learn about operating systems online](https://news.ycombinator.com/item?id=12773649)；[Teach Yourself Computer Science](https://news.ycombinator.com/item?id=23588896)；[Ask HN: What are the best MOOCs you've taken?](https://news.ycombinator.com/item?id=16745042)；[The Joy of Nand2Tetris](https://news.ycombinator.com/item?id=43056456)；[Learning about distributed systems: where to start? (2020)](https://news.ycombinator.com/item?id=40037324)

### Nand2Tetris / The Elements of Computing Systems

Noam Nisan、Shimon Schocken · 项目课程 / 教材 / 模拟器

从逻辑门搭建CPU，再写汇编器、虚拟机、编译器和运行库，最后在自己构建的栈上运行程序。适合希望把硬件到软件各层连起来、喜欢持续动手的人。

**适合谁／先修：**建议有基本编程经验；涉及多个层次，不能把前半段完成等同于整套课程完成。

**推荐理由：**跨2018与2025年的独立学习者反复推荐；最具体的收益是理解层次如何连接、在模拟器中得到可工作的系统。

[资源入口](https://www.nand2tetris.org/course)

**使用备注：**2025年项目8进行中的读者报告：官网前6个项目附相关书章，之后购买了教材；这是当时个人经历，不保证今后的授权条件。

**推荐 · [kroltan / 16746368](https://news.ycombinator.com/item?id=16746368)**：修课者明确描述整栈项目与合适的教学粒度。

> As the name suggests, they teach the necessary to build your own computer, assembler, language and finally a simple game. I would say it goes to an "appropriate" level of detail.

**推荐 · [lordviet / 43087867](https://news.ycombinator.com/item?id=43087867)**：2025年独立完课者特别肯定编译器练习与长期记忆。

> Both the course and the book are phenomenal. In my opinion they are up there as one of the best CS resources. I finished it two years ago and still think about it fairly often. The compiler exercise is beyond excellent and cracking it feels like a milestone.

**有条件推荐 · [dmytrish / 16745842](https://news.ycombinator.com/item?id=16745842)**：对第二部分给出明确难度和既有接触经验的条件。

> The courses are definitely very challenging and some previous exposure to the topics is desired.

### Computer Systems: A Programmer's Perspective (CS:APP) + labs

Carnegie Mellon / Randal E. Bryant、David R. O’Hallaron · 教材 / 系统编程实验

从程序员视角理解数据表示、汇编、内存、缓存、并发及系统调用相关行为。配套实验让学习者练习拆解程序、实现内存分配器和代理服务器。

**适合谁／先修：**建议已能写C程序，并准备阅读汇编和调试内存问题。

**推荐理由：**修课者具体肯定选题、解释和有趣的实验；另一位CMU学生逐项描述了实验如何覆盖系统基础。

[资源入口](http://csapp.cs.cmu.edu/3e/home.html)

**使用备注：**本条将教材与公开自学版labs作为一个资源包；不保证CMU校内作业、参考解答或账号权限对外开放。公开labs入口也在原评论中直接出现。

**推荐 · [doctorsher / 23595803](https://news.ycombinator.com/item?id=23595803)**：读者明确针对CS:APP的行文、主题选择和练习给出正面评价。

> It is really well written, has a great choice of topics, and phenomenal exercises [0] for practice (some are legitimately fun).

**推荐 · [bitwiseand / 12774258](https://news.ycombinator.com/item?id=12774258)**：另一位CMU213修课者强烈推荐；后文具体列出位操作、缓存、malloc及线程代理实验。

> I took 213 at CMU. Can't recommend it highly enough. A lot of other intro systems courses are based off that. It is a prerequisite for most classes moving forward at CMU.

### Operating Systems: Three Easy Pieces (OSTEP)

University of Wisconsin–Madison / Remzi H. Arpaci-Dusseau、Andrea C. Arpaci-Dusseau · 公开教材 / 练习

围绕虚拟化、并发和持久化解释操作系统，连接CPU调度、内存管理和文件存储。适合读过程序设计基础、希望把OS概念讲清楚的自学者。

**适合谁／先修：**建议具备C和基础计算机系统知识；配合练习阅读。

**推荐理由：**一位因原教材难懂而换书的学习者称赞其清楚、简洁且保留必要细节；2024年另一位读者也主动推荐。

[资源入口](http://pages.cs.wisc.edu/~remzi/OSTEP/)

**使用备注：**第一位评论者后来向作者提交过勘误，并说明被列入致谢；不是作者本人，但该参与关系应保留。官网说明PDF免费。

**推荐 · [doctorsher / 23595803](https://news.ycombinator.com/item?id=23595803)**：修课者对比自己OS课原教材后的具体阅读体验。

> OSTEP has incredibly clear and concise descriptions without skimping on necessary details. It's wonderfully written.

**推荐 · [dondraper36 / 40048872](https://news.ycombinator.com/item?id=40048872)**：另一位评论者在有人寻求不太学术化OS书时直接推荐。

> Operating Systems: Three Easy Pieces is very good

### ops-class.org — Hack the Kernel

University at Buffalo / Geoffrey Challen · 大学课程 / 内核编程实验

配合操作系统讲座、试题和OS/161编程作业，把概念落实到内核实现。适合已经会C、想亲自完成OS实验的人。

**适合谁／先修：**需要C基础和调试耐心；多位评论者强调作业强度很高。

**推荐理由：**实际修课者肯定有趣且有挑战的作业；另一个课程征集帖也出现正在学最后几周的正向体验。

[资源入口](https://www.ops-class.org/)

**使用备注：**2018年评论的脚注[3]误链到了CS50，资源URL因此采用2016年原帖的ops-class官网，不能照抄该脚注。讲座与实验的年代较早，环境配置需自行核对。

**推荐 · [melvin0008 / 12775433](https://news.ycombinator.com/item?id=12775433)**：实际修课者明确推荐编程作业。

> I have taken this course and the assignments are fun and challenging. Learnt a lot.

**有条件推荐 · [atomicnumber1 / 16752481](https://news.ycombinator.com/item?id=16752481)**：正在修读的学习者认为强度高但可完成，尚不是完课报告。

> ops-class (Operating Systems) [3]: This is by far the toughest MOOC I've taken. The Assignments are really tough. Although not impossible. Just the right amount of tough, I guess. I'm currently in the last few weeks and I've really enjoyed it every bit so far.

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

### CS 6120: Advanced Compilers — The Self-Guided Online Course

Cornell / Adrian Sampson · 大学高级课程 / 论文 / LLVM与Bril实践

从中间表示、数据流和经典优化进入并行化、JIT与垃圾回收，并做开放源码任务。适合已有编译器或系统基础、希望深入实现与研究主题的人。

**适合谁／先修：**建议先完成基础编译器或解释器项目；它是研究生层次的进阶材料。

**推荐理由：**2024年有真正在线学过课程的读者强烈推荐，并描述参与Bril修复的体验；另有学习者说明该课补强了编译器面试准备，但同时披露已有低层系统和开源背景。

[资源入口](https://www.cs.cornell.edu/courses/cs6120/2023fa/self-guided/)

**使用备注：**官方自学页已缓存，涵盖LLVM及教学IR。引用2024讨论中的实际学习者；2020帖中仅表示喜欢材料外观的评论未替代完课经验。

**推荐 · [terrelln / 39581518](https://news.ycombinator.com/item?id=39581518)**：实际在线学习者具体描述Bril IR实践和反馈。

> I went through this course online a few summers ago, and learned a ton. I highly recommend it! It was very engaging to put up PRs for small issues in the Bril IR, and work with the professor to fix them.

**有条件推荐 · [mnafees / 39580289](https://news.ycombinator.com/item?id=39580289)**：保留推荐者已有系统课程和开源编译器经验的条件，不能读作课程保证求职结果。

> My University's (University of Waterloo) curriculum around low-level computing systems was already par excellent, and of'course I was also contributing to open source compiler projects. But this course really helped me answer some of the toughest questions during my interviews!

