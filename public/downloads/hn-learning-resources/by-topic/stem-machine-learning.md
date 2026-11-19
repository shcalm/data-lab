# 机器学习从基础到深度学习实作

先学理论还是先跑模型，哪些具体课程能把两者接起来？

把经典ML、泛化原理、统计学习、深度学习和从头实现语言模型区分开，并保留数学先行与实践先行的不同适合人群。

本主题收录 6 项资源。[返回主题索引](../学习主题.md)

主题讨论线索：[Learning From Data - Online Course](https://news.ycombinator.com/item?id=3703782)；[Ask HN: What are the best MOOCs you've taken?](https://news.ycombinator.com/item?id=16745042)；[Ask HN: Full-on machine learning for 2020, what are the best resources?](https://news.ycombinator.com/item?id=21924298)；[Ask HN: Recommend me a course on Coursera](https://news.ycombinator.com/item?id=22826722)；[Ask HN: What's the best lecture series you've ever seen?](https://news.ycombinator.com/item?id=34591291)

### Machine Learning（Andrew Ng，原版）

Stanford / Andrew Ng；Coursera 托管 · 历史MOOC：讲座＋Octave/Matlab编程作业

从回归、分类等基础算法进入机器学习，并亲自实现训练过程，适合建立经典机器学习概念和算法直觉。

**适合谁／先修：**建议基本微积分与矩阵运算；历史作业使用Octave或Matlab。

**推荐理由：**blcArmadillo喜欢自己实现训练流程后形成的内部机制直觉；heifetz认为编程作业帮助掌握算法；pvarangot在2020年认为基础内容仍有价值，同时提醒工具和影音已显旧。

[资源入口](https://www.coursera.org/learn/machine-learning)

**使用备注：**这里是2011年前后的原版课程，历史链接今天可能转向新版。2022年Python Machine Learning Specialization是后续另版；不把旧版Octave体验套到新版上。

**推荐 · [blcArmadillo / 22829059](https://news.ycombinator.com/item?id=22829059)**：blcArmadillo报告做训练管线作业对理解框架内部机制的帮助。

> I took it several years back and enjoyed it. I liked that the course had you implement the whole training pipeline yourself rather than using a framework (not sure if the newer class does the same). While you would likely not do this in practice, I felt it helped my intuition when using the frameworks since I had a sense of how the internals were

**有条件推荐 · [heifetz / 3704106](https://news.ycombinator.com/item?id=3704106)**：heifetz推荐Octave作业，但认为原版不如正式课数学严谨。

> the best aspect of the andrew ng course was the homeworks using octave. Yes, it's watered down and not as mathematically rigorous as the real course, but you learn a lot of the essentials from the experience of coding machine learning algorithms, that I can't imagine learning as easily from doing non-programming homework.

**有条件推荐 · [pvarangot / 22828702](https://news.ycombinator.com/item?id=22828702)**：pvarangot在2020年认为基础仍好，但影音和工具已显旧。

> It was good like 10 years ago and it did age well but it's a little bit outdated on the video/audio quality and the tools and algorithms you learn about. I think it's surprisingly up to date for a fundamentals course that old, but still a bit outdated.

### Deep Learning Specialization

DeepLearning.AI / Andrew Ng；Coursera 托管 · MOOC系列：理论讲解＋Python作业

系统介绍神经网络与深度学习方法，适合已有编程基础、希望同时理解主要数学概念与实践步骤的人。

**适合谁／先修：**建议Python、基础线性代数与求导；有机器学习入门更方便。

**推荐理由：**tasubotadas说推导和解释充分且有实用建议；dagw喜欢节奏与数学深度的平衡。同时保留tibbon对影音与作业设计的异议。

[资源入口](https://www.coursera.org/specializations/deep-learning)

**使用备注：**Deep Learning Specialization与经典Machine Learning原版是不同课程系列；虽然有评论称它“updated version”，这里不据此把两者当成同一课。体验来自2018–2020年。

**推荐 · [tasubotadas / 22831331](https://news.ycombinator.com/item?id=22831331)**：tasubotadas自称完成过两类Ng课程，喜欢这里的推导与实践建议。

> Overall, this course is extremely good mostly because Ng covers the essential theoretical topics and gives some practical advice. Also, the topics are explained really well and you do not need to look up additional material. Also, I really appreciate that he took the time to derive those equations while others just drop the results.

**推荐 · [dagw / 16748430](https://news.ycombinator.com/item?id=16748430)**：dagw说明这组课如何在时间投入和数学理解之间取得平衡。

> Andrew Ng's deep learning course. For me it struck the perfect balance between being fast and 'easy' enough to not take up too much of my time while still being deep enough that I finally understood the basic math behind deep learning.

**限制／异议 · [tibbon / 16755401](https://news.ycombinator.com/item?id=16755401)**：tibbon批评影音和作业设计，避免写成一致好评。

> The whine/distortion on the audio made it difficult to listen to on headphones. Many of the exercises were either a bit too railsroaded and simple, or poorly explained in their goals and barely worked.

### Practical Deep Learning for Coders

fast.ai / Jeremy Howard、Rachel Thomas · 实作型深度学习讲座与notebook

从可运行的模型和实际任务切入深度学习，再逐步解释实现与原理，适合能编程且喜欢边改边学的人。

**适合谁／先修：**建议基本Python编程；实际训练需要合适运行环境。

**推荐理由：**ScoutOrgo喜欢易上手的材料及论坛；ujjwalgrover具体称赞2022版现场运行Jupyter代码和展示Kaggle思考过程；frequentnapper说实践使自己敢回头学理论。

[资源入口](https://course.fast.ai/)

**使用备注：**2018旧课与2022版的体验分别归属；入口可能随版本更新。它重点是深度学习实践，不能据此宣称覆盖全部机器学习理论。

**推荐 · [ScoutOrgo / 16745747](https://news.ycombinator.com/item?id=16745747)**：ScoutOrgo推荐深度学习课程及其学习支持；未声称完成全部课程。

> Fast.ai's (fast.ai) deep learning and machine learning courses. No ads, good notes/forum, and very approachable material for anyone that knows basic coding.

**推荐 · [ujjwalgrover / 34593024](https://news.ycombinator.com/item?id=34593024)**：ujjwalgrover描述2022版现场notebook讲解的具体优点。

> 2. The lectures are super hands on - Jeremy actually fires up a jupyter notebook and runs code which often surprises him 3. I love how he describes he deep dives into a specific Kaggle competition. Describes in great detail his own attempts at getting up the leaderboard. It's almost like watching a poker player reveal her decision process before

**推荐 · [frequentnapper / 21925564](https://news.ycombinator.com/item?id=21925564)**：frequentnapper报告相较理论先行课程，这种方式更帮助自己。

> Same here. I tried Andrew Ng's course a few times ever since it launched a few years back but I could only get through half of it. Fast ai makes more sense to me and I've picked up a decent amount of concepts where I can now go back and feel confident enough to tackle theory.

**限制／异议 · [boltzmannbrain / 21924848](https://news.ycombinator.com/item?id=21924848)**：boltzmannbrain认为只做fast.ai不足以形成完整ML基础，并建议另补教材和论文实现。

> What you really learned is copy-pasting code (as you mentioned) and some neural net tricks (like a good learning-rate to start SGD). How to learn ML? Do fastai + reading Daphne Koller's and Chris Bishop's books on PGMs + re-implementing a paper on Gaussian process classification + another paper on GNNs + ....

### Learning From Data

Caltech / Yaser Abu-Mostafa · 大学机器学习公开课：视频、作业及教材

注重模型何时能学好、泛化、误差等机器学习基本原理，适合愿意做数学推导和较难作业的人。

**适合谁／先修：**建议微积分、线性代数、概率及编程；“入门”是相对研究生课而言。

**推荐理由：**两位Caltech校友高度评价校内等价课的教师和作业；tzs在网课体验中强调教师回答论坛问题、课程接近校内版。

[资源入口](https://work.caltech.edu/telecourse.html)

**使用备注：**2012校内体验与2018在线体验分开。不能保证今天仍有教师答疑或当年的开课节奏。

**推荐 · [andymatuschak / 3704782](https://news.ycombinator.com/item?id=3704782)**：andymatuschak回忆的是Caltech校内等价课，并推荐公开课程。

> Yaser Abu-Mostafa was (by enormous margin) the most effective professor I had at Caltech. Despite being such an expert in the field, he understands clearly when a concept is particularly challenging--and what about it makes it so. This class (the official equivalent) was one of my absolute favorites. Definitely worth a look!

**推荐 · [evan-arm / 3706298](https://news.ycombinator.com/item?id=3706298)**：evan-arm回忆校内课作业难但能理解每步目的，不能改写成其完成MOOC。

> It was also fairly difficult -- the assignments were hard, but at every step, you could look at what you'd done and say "I know why I'm doing this, and I can see how this works."

**推荐 · [tzs / 16750033](https://news.ycombinator.com/item?id=16750033)**：tzs报告当年网课的教师论坛参与，并对今天是否仍如此表示不确定。

> The most outstanding thing about this course was Professor Abu-Mostafa's participation in the forums. He was very active answering questions. I don't know if he still does that now that the course is running in self-paced mode.

### Statistical Learning（Hastie / Tibshirani）

Stanford University / Trevor Hastie、Robert Tibshirani · 统计学习公开课／MOOC，配套ISLR教材与R实验

从统计角度学习回归、分类及模型评估等方法，适合数据科学入门者；书籍和实验可补充讲座。

**适合谁／先修：**建议基础统计、概率与R；应配合实际数据练习。

**推荐理由：**anarchimedes喜欢两位教师的对话，并用配套书深入；ycombinator_usr明确推荐用R的课程。harry8则认为练习偏少且措辞含糊。

[资源入口](https://online.stanford.edu/courses/sohs-ystatslearning-statistical-learning)

**使用备注：**评论中的Lagunita链接是历史课程入口，这里使用另一条评论提供的Stanford官方入口。课程与配套ISLR教材归为同一条；不把后来Python版本混入原R版体验。

入口检查：202；自动访问未成功，详见链接检查记录。历史推荐仍保留。

**推荐 · [anarchimedes / 16745730](https://news.ycombinator.com/item?id=16745730)**：anarchimedes解释讲座对话及配套教材的帮助。

> I like the dialogue between Hastie and Tibshirani in their statistical learning course from Stanford [1]. I found the accompanying ISL book and c-cran depositories helpful for when I wanted to go deeper beyond the lecture. [1] https://lagunita.stanford.edu/courses/HumanitiesandScience/S...

**推荐 · [ycombinator_usr / 16747020](https://news.ycombinator.com/item?id=16747020)**：ycombinator_usr明确推荐Hastie和Tibshirani的用R课程。

> if you want to focus on Statistical Learning, I can recommend Introduction to Statistical Learning Using R[1] by Prof. Hastie and Tibshirani. [1]: https://lagunita.stanford.edu/courses/HumanitiesSciences/Sta...

**限制／异议 · [harry8 / 16750844](https://news.ycombinator.com/item?id=16750844)**：harry8只完成约五周，喜欢讲授但批评习题质量。

> I found the lectures entertaining and the exercises of a much lower quality. Not enough of them, shallow and ambiguously worded. I got something like 90% on the edx MITx probability course and was barely getting 50% for the above mentioned Stanford stat learning course for the 5 weeks of it I completed.

### Neural Networks: Zero to Hero

Andrej Karpathy · 代码讲解视频系列：自动求导到语言模型

从小型自动求导引擎开始逐步实现神经网络与GPT，适合想通过代码弄懂神经网络机制的程序员。

**适合谁／先修：**建议Python熟练，了解基本求导和矩阵运算；愿意边看边实现。

**推荐理由：**stjo喜欢从约100行Python自动求导逐步搭到GPT；lawkwok说从头构建GPT一讲帮助自己理解机器学习和聊天机器人。

[资源入口](https://karpathy.ai/zero-to-hero.html)

**使用备注：**依据2023年系列讨论；是讲座与实作系列，不是授予学分或证书的大学课程。未把评论者喜欢讲座写成完成全部系列。

**推荐 · [stjo / 34591998](https://news.ycombinator.com/item?id=34591998)**：stjo具体指出从小自动求导引擎到GPT的循序实现。

> Just watch the first lecture and you won't be able to not watch the rest. It starts with making your own autograd engine in 100 lines of python, similar to PyTorch and then builds up to a GPT network.

**推荐 · [lawkwok / 34596042](https://news.ycombinator.com/item?id=34596042)**：lawkwok明确解释其中GPT实作讲座消除了哪些神秘感。

> The "Let's build GPT: from scratch, in code, spelled out." demystifies so much of machine learning and chatbots. It's so cool to see how simple python code can be leveraged into something so amazing.

