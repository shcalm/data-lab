# 超越语言语法：程序设计与范式

已经会一种语言，怎样提高设计能力并更快理解其他语言？

Grossman课程的讨论最集中地提出“按共同特性理解语言”；SICP、Scala、Norvig与小项目练习分别提供抽象、范式和编码训练。

本主题收录 6 项资源。[返回主题索引](../学习主题.md)

主题讨论线索：[Ask HN: What's your favorite online course?](https://news.ycombinator.com/item?id=10644518)；[Ask HN: What are the best MOOCs you've taken?](https://news.ycombinator.com/item?id=16745042)；[Ask HN: What is the best online course you've ever taken?](https://news.ycombinator.com/item?id=18566638)；[Teach Yourself Computer Science](https://news.ycombinator.com/item?id=23588896)；[Ask HN: What's the best lecture series you've ever seen?](https://news.ycombinator.com/item?id=34591291)

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

### Functional Programming Principles in Scala

EPFL / Martin Odersky · 大学课程 / MOOC

用Scala练习函数式程序设计，并认识这种范式怎样改变已有的编程习惯。适合已有编程基础、希望系统学习函数式方法的人。

**适合谁／先修：**建议已会一种编程语言；这是函数式思维训练，不只是Scala语法速成。

**推荐理由：**独立修课者肯定其作为函数式编程和Scala入门的作用；早期班次也有少量制作和组织上的保留意见。

[资源入口](https://www.coursera.org/learn/progfun1)

**使用备注：**把本条限定为Principles第一门课；Reactive Programming、分布式键值存储等后续课程不计入它的课程内容。

**推荐 · [ctoomey / 10648212](https://news.ycombinator.com/item?id=10648212)**：学习者明确推荐作为Scala与函数式编程入口。

> Functional Programming Principles in Scala ( https://www.coursera.org/course/progfun ) by Martin Odersky, the inventor of Scala, is also excellent and a great way to learn and start using Scala and functional programming.

**推荐 · [uulbiy / 10648295](https://news.ycombinator.com/item?id=10648295)**：另一位学习者明确表示喜欢Scala函数式入门，并与更难的后续课区分。

> I also liked Computer Networks[2] even though it's an introductory course, Functional Programming Principles in Scala[3] which is surprisingly easy unlike the follow up course[4]

### Design of Computer Programs (CS212)

Udacity / Peter Norvig · 视频课程 / 编程练习

通过Python练习问题建模、组织解决方案和改进程序。适合已写过小程序、希望从“能运行”走向更清晰设计的人。

**适合谁／先修：**建议具备Python基础；讨论称其内容是semi-advanced programming concepts。

**推荐理由：**2015与2023年的独立评论均推荐；具体收获是更优雅地思考和编写Python程序。

[资源入口](https://www.udacity.com/course/design-of-computer-programs--cs212)

**使用备注：**这是历史课程；本次能取得标题和介绍正确的Udacity课程页，但未登录验证全部练习和视频。早期教授活跃答疑的体验不能推定仍存在。

**推荐 · [amykhar / 10649112](https://news.ycombinator.com/item?id=10649112)**：早期修课者认为课程和当时的教师论坛互动都很有价值。

> Design of Computer Programs was decidedly the best course I ever took online. I was lucky enough to take it when it was first offered. Peter Norvig was very active in the course forum.

**推荐 · [kross11480 / 34594243](https://news.ycombinator.com/item?id=34594243)**：2023年独立评论指出对Python思考与设计方式的实际帮助。

> I would recommend Peter Norvig's "Design of Computer Programs" course in Udacity. Gave me an insight on elegant thinking and programming with python.

### JavaScript30

Wes Bos · 30个项目视频练习

用原生JavaScript制作30个小项目，练习浏览器里的实际编码。适合学过JavaScript基础、想靠连续小项目提高熟练度的人。

**适合谁／先修：**建议已经熟悉JavaScript基础；不是从编程零基础讲起。

**推荐理由：**课程征集帖中的读者特别肯定短项目、没有库与构建工具的练习方式，以及讲解的可跟随性。

[资源入口](https://javascript30.com)

**使用备注：**另有评论者推荐自己制作的课程文字转写，本目录未把该宣传计为第二位独立推荐者。官网确有对应的30项目介绍。

**推荐 · [mcintyre1994 / 18567320](https://news.ycombinator.com/item?id=18567320)**：直接描述原生JS短练习的学习价值；不是从标题推断推荐。

> Javascript30 is 30 free short modern JavaScript lessons with no libraries or builds or any of that stuff. Great way to get back on track and catch up with what vanilla is can do, and Wes Bos is exceptional as a teacher.

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

