# 用解释器和编译器理解语言运行

从第一次实现语言，到优化与运行时进阶，应选哪种资源？

评论明确区分语言设计思想、入门解释器项目、传统COOL编译器与高级优化课；难度和目标不同，不应当作互相替代。

本主题收录 6 项资源。[返回主题索引](../学习主题.md)

主题讨论线索：[HN #14721469](https://news.ycombinator.com/item?id=14721469)；[Stanford Compilers Course](https://news.ycombinator.com/item?id=15739877)；[Ask HN: What are the best MOOCs you've taken?](https://news.ycombinator.com/item?id=16745042)；[Teach Yourself Computer Science](https://news.ycombinator.com/item?id=23588896)；[HN #25386756](https://news.ycombinator.com/item?id=25386756)；[CS 6120: Advanced Compilers: The Self-Guided Online Course](https://news.ycombinator.com/item?id=39577878)；[Crafting Interpreters](https://news.ycombinator.com/item?id=40950235)

### Structure and Interpretation of Computer Programs — MIT 6.001 lectures

MIT / Harold Abelson、Gerald Jay Sussman · 大学公开视频 / 配套教材

用Scheme讨论抽象、递归、流和解释器等程序设计思想。适合已经能写程序、希望理解程序如何组织和执行的人。

**适合谁／先修：**建议先有基本编码与工具使用经验；它更偏重编程思想，不能替代基础工具训练。

**推荐理由：**在2015、2018和2023年的课程讨论中均被主动推荐；具体反馈集中在流和抽象改变了看待程序的方式。

[资源入口](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video_galleries/video-lectures/)

**使用备注：**资源指经典MIT讲座；旧OCW URL中的学期标签不意味着录影拍摄于2005年。应配合练习，不能仅凭观看获得编程熟练度。 原评论的旧OCW路径本次返回404，入口已改为同一课程官方视频目录，已取得200及匹配标题。

**推荐 · [lab11 / 34592325](https://news.ycombinator.com/item?id=34592325)**：评论者在明确推荐Sussman和Abelson讲座、特别是流章节后，描述了编程观念上的收获。

> It changed my outook on programming by pi degrees and I feel it is more needed then ever.

**推荐 · [omilu / 10647633](https://news.ycombinator.com/item?id=10647633)**：另一位评论者直接把SICP列为最喜欢的编程课程。

> sicp is the best programming course hands down. https://www.youtube.com/watch?v=2Op3QLzMgSY&list=PLB63C06FAF...

**有条件推荐 · [geofft / 22248034](https://news.ycombinator.com/item?id=22248034)**：一位MIT修课者强调自己的既有UNIX和编程经验是受益条件。

> I got a lot out of it, because I had already been using UNIX and writing code for years at home as a teenager.

### Programming Languages, Parts A–C

University of Washington / Dan Grossman · 大学课程 / Coursera系列

借Standard ML、Racket和Ruby比较语言特性、求值方式、作用域及编程范式，并实现小型解释器。适合会一种语言但想跳出语法记忆、理解语言取舍的人。

**适合谁／先修：**有一种过程式语言的基础即可入手；讨论中的修课者明确说不需要先学编译器或自动机。

**推荐理由：**多个独立修课者都说课程改变了学习新语言的方法：从逐个记语法，转向识别语言共享的特性。

[资源入口](https://www.coursera.org/learn/programming-languages)

**使用备注：**早期评论对拆成两部分还是三部分说法不一致；当前官网标题为Part A，目录应继续查B、C，不应当成一门已涵盖全部内容的短课。

**推荐 · [grdvnl / 16745734](https://news.ycombinator.com/item?id=16745734)**：修课者明确描述学习新语言的方法发生变化。

> I took the Programming Languages course on Coursera which is so far the best course for me. It changed the way I learn any new programming language.

**推荐 · [madflame991 / 16747578](https://news.ycombinator.com/item?id=16747578)**：另一位修课者具体指出类型、作用域、求值方式等统一认识。

> until this course I saw every language like a little island; after this course I understood that programs are just a collection of features: various typing systems, static/dynamic scoping, lazy/eager evaluation, etc.

**有条件推荐 · [madflame991 / 16749508](https://news.ycombinator.com/item?id=16749508)**：对先修要求的修课者说明；其上下文解释课程直接以数据结构表示待解释的程序。

> I think the only requirements for this course is some plain procedural language (C/Pascal).

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

### Crafting Interpreters

Robert Nystrom · 公开在线图书 / 两个解释器项目

为同一门Lox语言分别写Java树遍历解释器和C字节码虚拟机，理解作用域、闭包及运行时实现。适合会编程、想第一次做语言实现的人。

**适合谁／先修：**建议具备基本编程能力，并能阅读或学习Java与C；这是基础实现训练，不是高级优化专著。

**推荐理由：**实际跟做者赞赏两个实现带来的重复理解和清楚的叙述，也有读者明确批评它不覆盖高级主题。

[资源入口](https://craftinginterpreters.com/)

**使用备注：**资源是语言实现项目教程；不要把它等同于完整编程语言理论或优化编译器课程。原文no very little语病照录。

**推荐 · [chris37879 / 40951194](https://news.ycombinator.com/item?id=40951194)**：跟做者描述理解语言工具内部的具体收益。

> Doing so made me really appreciate just what's going on inside a compiler / language toolkit. It's also one of the most well written technical guides I've ever followed, it really helped me internalize the concepts, and they are useful all over the place, not just in compilers.

**推荐 · [britannio / 40951129](https://news.ycombinator.com/item?id=40951129)**：完成后半本的独立读者建议每章挑挑战题巩固。

> I just finished the second half, it's a great book! I recommend doing one or two of the proposed challenges in each chapter to reinforce your understanding of the content.

**限制／异议 · [yodsanklai / 40951345](https://news.ycombinator.com/item?id=40951345)**：保留一位失望读者对入门定位与进阶深度的批评。

> It's suitable for someone with no very little knowledge on the topic, but it doesn't really cover any advanced topic.

### Stanford Compilers — Alex Aiken / historical MOOC

Stanford / Alex Aiken · 大学课程 / COOL编译器项目

围绕COOL语言实现词法分析、语法分析、类型检查和代码生成，把编译器的主要阶段串起来。适合希望完成第一套编译器、已有C++或Java基础的人。

**适合谁／先修：**建议熟悉C++或Java；历史版本提供这两种语言的项目骨架。

**推荐理由：**实际修课者报告完成了编译器，并有人把输出改成JavaScript；另一个完课者强调它聚焦基础，不是高级语言特性的直接实现手册。

[资源入口](https://lagunita.stanford.edu/courses/Engineering/Compilers/Fall2014/about)

**使用备注：**这是历史MOOC入口。本次它跳转到Stanford Online后返回202空响应，未验证课程仍可学习；另一个评论提供现行官方课纲http://web.stanford.edu/class/cs143/，已缓存，但不能保证与旧MOOC版本相同。

入口检查：202；自动访问未成功，详见链接检查记录。历史推荐仍保留。

**推荐 · [nfriend / 15740313](https://news.ycombinator.com/item?id=15740313)**：实际学习者完成并改造了课程编译器项目；其个人展示链接未作为被推荐资源。

> I took this course for fun a few years ago - it was fantastic! I modified the project a bit to match my own interests - instead of compiling to an executable, my compiler generated browser-friendly JavaScript code.

**有条件推荐 · [tomku / 15744083](https://news.ycombinator.com/item?id=15744083)**：完课者明确限定课程内容与用途。

> It's focused on the basic concepts of compiler implementation with the example language (COOL) being pretty traditionally object-oriented. It's absolutely not a how-to course on how to implement advanced language features.

