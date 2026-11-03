#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 course.html：Karpathy 两小时 LLM 讲座精读 + 全文讲稿。
章节按真实内容切分，讲稿从 transcript_karpathy_zh.json 自动注入。
"""
import json, os, re, html

SRC = os.path.expanduser('~/workspace/tmp/x-kichiro/transcript_karpathy_zh.json')
OUT = os.path.expanduser('~/workspace/promptlib/course.html')

chunks = json.load(open(SRC, encoding='utf-8'))['chunks']

# (编号, 标题, 起秒, 止秒, summary HTML, figures[(img,alt,cap)], points[(h3,p)], note)
CH = [
(1, '一句话定义：一个 <em>1TB 的有损压缩包</em>', 0, 240,
 'Karpathy 给 LLM 下的第一个定义，也是全场最重要的一句：<strong>大语言模型本质上是一个约 1TB 的、有损且概率性的「互联网压缩文件」</strong>。它不是数据库，不是计算器，也不是搜索引擎——你一直在跟一个压缩包说话。',
 [('kp-llm.jpg', 'Excalidraw 白板：LLM 比喻为 1TB 有损压缩的互联网 zip 文件，附预训练与后训练说明',
   '<b>原始幻灯片</b> · 把 LLM 画成一个带笑脸的 zip 文件，旁边标注训练成本与上下文窗口')],
 [('自包含的实体', '把语言模型想象成磁盘里的一个 1TB 文件，对应神经网络里一万亿个参数及它们的精确配置。这个实体唯一的功能是：生成序列中的下一个 token。'),
  ('它默认什么都没有', '没有计算器，没有 Python 解释器，也不能浏览万维网。这些能力要靠工具调用额外接上，不是模型自带。'),
  ('知识是有损的', '参数里存的是「世界知识」，但通常过时几个月——因为它读的是几个月前的互联网快照。这是后面「知识截止」问题的根源。')],
 '<b>为什么要用压缩包打比方？</b>Zip 压缩会丢细节但保留整体结构，LLM 对互联网的「记忆」也是如此：宏观规律学得很好，具体细节（某天某条新闻、某个确切数字）经常含糊或编造。理解这个比喻，就理解了后面所有的幻觉问题。'),

(2, '它是怎么练出来的：<em>预训练</em> 与 <em>后训练</em>', 240, 600,
 '一阶段啃下整个互联网，二阶段学会好好说话。<strong>两个阶段的成本差着一两个数量级</strong>，这也解释了为什么各家都在卷预训练，而普通用户能感受到的差别大多来自后训练。',
 [('kp-train.jpg', 'Claude 界面：右侧 Artifacts 预览亚当·斯密经济理论互动抽认卡应用',
   '<b>后训练的直观体现</b> · Claude 听完一句话就生成可交互的抽认卡应用，这是「助手风格 + 工具调用」叠加的结果')],
 [('预训练 pre-training', '约 1000 万美元、耗时 3 个月，在互联网文档上训练。产出的是「世界知识」和一个会续写文本的基座。'),
  ('后训练 post-training', '成本低得多，用 SFT（监督微调）、RLHF（基于人类反馈的强化学习）、RL 在对话数据上打磨。产出的是「助手风格」——你现在感受到的礼貌、结构化、愿意帮忙，全是这一阶段的成果。'),
  ('两半合在一个产物里', '你默认正在交互的，是一个把这两部分都整合好的单一实体。知识来自预训练，语气和对话能力来自后训练。')],
 None),

(3, '上下文窗口：模型的<em>工作记忆</em>', 600, 900,
 '点「新建对话」时，模型开启一条一维 token 序列。你写 token，回车后控制权交给模型，模型输出自己的 token，遇到「我说完了」这个特殊 token 再把控制权还给你。<strong>这条不断增长的序列就是 context window。</strong>',
 [('kp-ctx.jpg', 'Excalidraw 白板：上下文窗口长条上分布 tokens 方块，标注 New chat 与 tiktokenizer 链接',
   '<b>上下文窗口长这样</b> · 一条水平长条就是 context window，上面的小方块是 tokens，左侧 New chat 是起点')],
 [('它不是无限长的笔记本', '窗口里的 token 越多，模型生成下一个 token 时就越容易被前面的内容分散注意力，准确率和表现都会下降。'),
  ('token 越多，越慢越贵', '涨幅不大但确实存在：计算下一个 token 的成本随 token 数量上升，模型会稍微变慢。'),
  ('把上下文当宝贵资源', '不要用无关信息塞满它，尽量保持精简。长对话跑到后面「变笨」，很多时候不是模型退化，是你把它的工作记忆占满了。')],
 '<b>实操建议：</b>一个话题聊到开始跑偏，就开新对话重讲需求，而不是在一条几百轮的对话里继续纠偏。<b>清理上下文，是最便宜的提效手段。</b>'),

(4, '模型生态：别只用一个，<em>建个委员会</em>', 900, 1020,
 'ChatGPT、Gemini、Copilot、Claude、Grok、Perplexity、DeepSeek、Le Chat——同一个问题喂给多个模型，交叉验证。Karpathy 把这叫他的 <strong>LLM 委员会</strong>。',
 [('kp-llms.jpg', 'Grok 3 欢迎页，显示 Good morning, Andrej Karpathy 与 DeepSearch、Think、Research 等功能入口',
   '<b>各家界面长得不一样，能力项也不一样</b> · Grok 3 的欢迎页把 DeepSearch、Think、Research、Analyze Data 直接铺在输入框下方')],
 [('确认自己用的是最新版', '界面左上角一般有模型选择器，付费升级才能拿到更先进的档位。别用 Grok 2 提问却以为在跟 Grok 3 对话。'),
  ('同题多投', '把同一个问题丢给好几个不同价位、不同厂商的模型，看它们各自怎么答。分歧点往往就是要你自己判断的地方。'),
  ('不同模型工具权限不同', '这是后面的关键伏笔：有的模型能调 Python，有的只能靠心算——遇到数学和代码，结果会差很远。')],
 None),

(5, '思考模型：什么时候值得<em>让它多想一会儿</em>', 1020, 1440,
 '各厂商陆续推出了 thinking model。它们在数学、代码这类难题上明显更准，但日常问题让它想一分钟纯属浪费。<strong>Karpathy 自己平时默认用 non-thinking model，要质量时才切换。</strong>',
 [('kp-gc.jpg', 'ChatGPT 界面：用户粘贴多层感知机 Python 代码，询问 gradient check 失败原因',
   '<b>典型的重思考场景</b> · 神经网络梯度检查失败，Karpathy 同时开着 ChatGPT、Gemini、Perplexity 和一堆调试教程标签排查')],
 [('难题才值得想', '数学、代码、多步推理——这类问题 thinking model 能提升准确率。旅行建议、写文案、日常问答，没必要。'),
  ('怎么开', '以 Grok 为例：输入框下方有 Think 开关，先打开再点发送，底层就会切到思考模型。各家的叫法和位置不同，但都有这个选择器。'),
  ('顺带看它想什么', 'OpenAI 不会完整展示思考过程，只给一份简略的思考摘要。这份摘要有时候比答案更能说明它卡在哪。')],
 '<b>现场对比：</b>同一个 gradient check 报错，喂给 O1 Pro 想了一分钟才给出正确解法；而 Claude 3.5 Sonnet 作为非推理模型，也直接定位到了真正的问题。<b>推理强度不是唯一变量，值得你自己试。</b>'),

(6, '工具调用：从<em>聊天</em>到<em>干活</em>', 1440, 2100,
 '这是整场讲座最实用的一章。LLM 一旦接上工具，就从「会说话的压缩包」变成「能办事的代理」。<strong>你要特别留意手上每个模型到底有哪些工具</strong>——权限不同，结果天差地别。',
 [],
 [('搜索工具的机制', '模型输出一种特殊的「搜索互联网」token，应用接到后就去抓网页，把网页内容塞进 context window，然后模型再回溯你的问题作答。'),
  ('时效性问题必须联网', '今天总统日开不开门、明天苹果发什么——这类会随时间变化的信息，压缩包里没有，只能靠搜索。'),
  ('不同厂商的搜索质量差很多', 'ChatGPT、Perplexity、Grok 的 Deep Search 各有取舍。Karpathy 的用法是：有最新动态就用 Perplexity，复杂调研用 Deep Research。')],
 '<b>没权限的模型会怎样？</b>Karpathy 现场试了不开搜索的 Grok，以及标注明说「2.0 Pro 实验版无法联网」的场景——模型会一本正经地跟你聊它根本不知道的事。<b>先确认工具权限，再相信答案。</b>'),

(7, 'Deep Research：<em>联网搜索 + 深度思考</em>', 2100, 2700,
 'Karpathy 称之为「特别酷但被严重低估」的功能。<strong>本质上就是联网搜索叠加长时间思考</strong>，模型自己跑几十分钟，查几十个来源，吐出一份带引用的报告。',
 [('kp-deepresearch.jpg', 'ChatGPT 界面，输入框内是关于 CaAKG 与长寿关系的详细提问',
   '<b>典型用例</b> · 「Bryan Johnson 配方里的 CaAKG 为什么可能和长寿有关」——一个需要查论文的问题')],
 [('门槛与产出', '最早由 ChatGPT 作为 Pro 订阅的一部分推出（每月 200 美元档位）。一次运行会查阅几十个来源，给出结构化报告加参考文献。'),
  ('现场对比', '同一个 CaAKG 问题，ChatGPT 思考五分钟、查阅 27 个来源；Perplexity 和 Grok 的报告更短、细节更少。ChatGPT 的报告提到了线虫、果蝇、小鼠中的研究与人体试验。'),
  ('报告是初稿，不是结论', '哪怕它真的在查资料，也没法保证完全没有幻觉——任何内容在任何时候都可能是编造的。<strong>引用极其重要，要顺着引用去查原文。</strong>')],
 '<b>正确用法：</b>把 Deep Research 的报告当成「待读论文清单」而不是答案。它真正的价值是替你省下半天文献调研时间，并指给你该看哪几篇。'),

(8, '读文档：把论文和古书<em>丢给它</em>', 2700, 3117,
 '把整篇论文、整本书上传进 context window，然后边读边问。<strong>Karpathy 的体会是：这能让对陌生领域内容的理解深度提升非常明显。</strong>',
 [('kp-multimodal.jpg', 'Google NotebookLM 界面，已上传 Evo2.pdf 并生成摘要与 8 分 11 秒音频概览',
   '<b>读论文神器</b> · NotebookLM 上传 Evo 2 论文 PDF，自动生成摘要、8 分钟音频概览、学习指南与 FAQ')],
 [('先总结，再逐章追问', '上传 PDF 让它先总结，然后针对具体章节提问。比一上来就啃原文效率高得多。'),
  ('老文献尤其需要帮手', '《国富论》是 1776 年的文本，连最基础的语言习惯都得靠解释。LLM 让很多原本读不动的内容变得可及。'),
  ('概念图也能自动画', 'Claude 听到章节概念后会写 Mermaid 代码，直接把「劳动分工如何受市场规模限制」这类关系画成流程图。')],
 None),

(9, '写代码：Python、Artifacts 与 <em>Cursor</em>', 3117, 4500,
 '给 LLM 接上编程能力后，它不用直接给你答案，而是写个程序算给你看。<strong>这是对付一切精确计算问题的一招。</strong>',
 [('kp-tools.jpg', 'Cursor 编辑器界面，AI Composer 已完成 React 井字棋游戏并提交 Git',
   '<b>工具调用的极端形态</b> · Cursor 的 Composer：一句话需求 → 改三个文件 → 直接 Git 提交'),
  ('kp-grok.jpg', 'Grok 3 界面：423534 乘以 3124 的乘法问题与回答',
   '<b>没有解释器的模型怎么做数学</b> · Grok 3 心算大数乘法，结果非常接近但并不正确')],
 [('让模型写代码，而不是自己心算', '凡是涉及精确计算的题，先问它「你能不能写段代码算一下」。ChatGPT 会正确调用编程语言，特殊 token 会指示应用去运行。'),
  ('有解释器和没解释器，是两种模型', 'Grok 3 没有 Python 权限、纯靠心算，大数乘法「非常接近，但还是不对，而且它会瞎编答案」。'),
  ('数据类任务要盯紧每一步', 'Karpathy 让它画 OpenAI 估值指数拟合图，模型偷偷往 2015 年估值里塞了个 0.1 没打招呼，打印值和 17 万亿也对不上。<b>图表很漂亮，数字要自己核。</b>'),
  ('Artifacts：一句话生成一个应用', 'Claude 听完《国富论》一章，直接写出可交互的抽认卡应用——自定义卡片、进度跟踪、随机排序全都有。'),
  ('Cursor 这类工具在快速进化', '从「按 Ctrl+K 改一行」到能执行命令、跨多个文件编辑、自己提交 Git。你基本只要坐着发号施令，这种方式叫 Vibe Coding。')],
 None),

(10, '语音：输入、输出与<em>原生音频</em>', 4500, 5591,
 'Karpathy 自己 <strong>80% 的提问是用语音完成的</strong>，手机上尤其如此。语音这一层的变化，可能比大多数人感受到的更快。',
 [],
 [('输入端：全局听写', 'Superwhisper、Wispr Flow、MacWhisper 这类是系统级功能，在任何应用里都能把语音转成文本，不是 ChatGPT 独有。'),
  ('输出端：读给你听', '通常各 App 自带朗读功能，原理是把文本截断成 token，再转成音频 token。'),
  ('高级语音模式 = 原生音频', '语音在语言模型内部原生处理，模型直接理解音频块、预测音频块，不经过文字中转。Karpathy 现场让它用尤达大师的语气讲课。'),
  ('音频输出的玩法', '让两个 AI 角色互相配音侃大山，或者让它学牛叫、学狐狸叫——看似胡闹，实则展示了音频生成的自由度。'),
  (' NotebookLM 播客生成', '上传几份自己的材料，出门散步时听 AI 把它们聊成一档播客。Karpathy 用它听过《Histories of Mysteries》。')],
 '<b>这一层迭代极快。</b>Karpathy 在现场特意提醒：他讲完之后高级语音模式可能又变了，所以「你总得时刻留意各个层级里都有什么内容」。'),

(11, '图像与视频：看得懂，也画得出', 5591, 6426,
 '从营养成分表到书架上的旧书，再到一整段丛林视频。<strong>视觉能力已经在很多日常场景里实用了。</strong>',
 [('kp-vision.jpg', 'ChatGPT 生成的丛林白虎视频画面',
   '<b>视频输出</b> · Karpathy 现场让多个模型各生成一只丛林里的老虎，逐个对比风格与画质')],
 [('图像就是 token 流', '实现方式和文本一样：把图像表示为 token，让模型按统计规律建模。encoder 和 decoder 阶段才涉及具体的图像编解码。'),
  ('传图提问的日常用法', '上传 Bryan Johnson「长寿混合物」的营养成分表让它转录，再追问哪些是核心成分、哪些可疑；上传血脂报告让它解读；上传牙膏成分表问「哪些能扔」。'),
  ('截图即提问', '屏幕上任何一块内容，截下来直接问。Karpathy 提醒：医疗相关内容要看懂它的依据，别只看结论。'),
  ('视频理解是当时最新前沿', '原始幻灯片上 Video input 被特意高亮。现场演示是开着摄像头让它认书架——《成吉思汗与现代世界的形成》《别闹了，费曼先生》、中洲地图、CO₂ 检测仪读数 713 ppm。'),
  ('视频输出仍在早期', '多个模型都能生成丛林老虎，风格画质各有差异，可以用专门工具横向对比。')],
 None),

(12, '记忆、自定义与<em>总结</em>', 6426, 7427,
 '最后一类功能，Karpathy 称之为「生活质量功能」——不提升智力，但大幅提升顺手程度。<strong>核心是三件事：记忆、自定义指令、自定义 GPT。</strong>',
 [('kp-memory.jpg', 'ChatGPT 界面，上传 Bryan Johnson Longevity Mix 营养成分表并要求转录',
   '<b>记忆的日常价值</b> · 它记得你的常用配方、常用问法，下次不用从头交代背景'),
  ('kp-custom.jpg', 'ChatGPT GPTs 编辑器界面：为 KoreanCap 自定义 GPT 编写三步指令',
   '<b>自定义 GPT 的指令长这样</b> · KoreanCap 收到字幕截图后依次执行 OCR、整段英译、单词级解析（含罗马音、词义、词干、助词），每词一行'),
  ('kp-cover.jpg', 'Excalidraw 完整白板：LLM 市场生态、核心比喻、训练成本、交互流程、生活质量功能与多模态总览',
   '<b>全场知识总图</b> · 左上市场生态，中间核心比喻与训练原理，左下交互流程与工具使用，右下生活质量功能与多模态能力')],
 [('Memory 记忆功能', '跨对话记住你的偏好、背景、常用信息。不用每开一个新对话就重新自我介绍。而且记忆可以手动编辑、添加、删除。'),
  ('Custom instructions 自定义指令', '用你喜欢的任何方式写一份长期生效的指令，之后每次对话都自动带上。这是零成本的个性化。'),
  ('Custom GPTs 自定义 GPT', '把一套固定流程打包成一个专用入口。Karpathy 的例子：截图韩剧字幕 → OCR → 翻译 → 单词级语法解析，三步全自动。'),
  ('Few-shot prompt', '不只描述任务，而是直接给几个输入输出样例，让它照着自己的样子执行。'),
  ('浏览器端 ≠ 手机端', '同样的功能在两端 availability 经常不一致。你在电脑上能用的，手机上未必有。')],
 '<b>收尾的五条心法：</b>① LLM 是个有损压缩包，知识会过时、细节会编；② 上下文是宝贵资源，塞满会降智；③ 工具决定上限，先问有没有 Python 和联网；④ 别只用一个模型，建你的委员会；⑤ 引用是生命线，报告是初稿不是结论。'),
]

def fmt(t):
    m, s = divmod(int(t), 60)
    h, m = divmod(m, 60)
    return '%d:%02d' % (h, m) if h else '%02d:%02d' % (m, s)

def esc(s):
    return html.escape(s, quote=False)

# ---- 按章节分派 chunk ----
assigned = set()
parts = []
for no, title, lo, hi, summary, figs, pts, note in CH:
    sel = [c for c in chunks if lo <= c['start'] < hi]
    for c in sel:
        assigned.add(id(c))
    parts.append((no, title, lo, hi, summary, figs, pts, note, sel))

leftover = [c for c in chunks if id(c) not in assigned]
if leftover:
    print('警告：%d 个 chunk 未归入任何章节: %s' % (
        len(leftover), [int(c['start']) for c in leftover[:10]]))

total = sum(len(p[8]) for p in parts)
print('章节 %d 个，覆盖 chunk %d/%d，讲稿 %d 字' % (
    len(parts), total, len(chunks), sum(len(c['zh']) for c in chunks if id(c) in assigned)))

# ---- 生成 HTML ----
def chapter_html(p):
    no, title, lo, hi, summary, figs, pts, note, sel = p
    h = []
    h.append('<section class="chapter" id="c%d">' % no)
    h.append('<div class="ch-head"><span class="ch-no">%02d</span>'
             '<span class="ch-time">%s – %s</span></div>' % (no, fmt(lo), fmt(hi)))
    h.append('<h2>%s</h2>' % title)
    h.append('<p class="summary">%s</p>' % summary)
    if figs:
        for img, alt, cap in figs:
            h.append('<figure class="shot"><img loading="lazy" decoding="async" '
                     'src="assets/%s" alt="%s"><figcaption>%s</figcaption></figure>'
                     % (img, esc(alt), cap))
    h.append('<div class="points">')
    for h3, body in pts:
        h.append('<div class="point"><h3>%s</h3><p>%s</p></div>' % (h3, body))
    h.append('</div>')
    if note:
        h.append('<div class="note">%s</div>' % note)
    # 讲稿
    h.append('<details class="script"><summary>'
             '<span class="script-label">本讲完整讲稿</span>'
             '<span class="script-meta">%s – %s · %d 字</span></summary>'
             '<div class="script-body">' % (fmt(lo), fmt(hi),
                                            sum(len(c['zh']) for c in sel)))
    for c in sel:
        h.append('<p class="script-p"><span class="ts">%s</span>%s</p>'
                 % (fmt(c['start']), esc(c['zh'].strip())))
    h.append('</div></details>')
    h.append('</section>')
    return '\n'.join(h)

toc = ''.join('<a href="#c%d">%02d %s</a>' % (p[0], p[0], re.sub(r'<[^>]+>', '', p[1]).split('：')[0])
              for p in parts)
chapters = '\n\n'.join(chapter_html(p) for p in parts)

CSS_EXTRA = '''
.script{margin:26px 0 0;border:1px solid var(--line);border-radius:16px;background:var(--paper);overflow:hidden}
.script>summary{display:flex;align-items:center;gap:14px;flex-wrap:wrap;padding:16px 20px;cursor:pointer;list-style:none;user-select:none}
.script>summary::-webkit-details-marker{display:none}
.script>summary:hover{background:var(--soft)}
.script-label{color:var(--accent);font:600 12px/1 "DM Mono",monospace;letter-spacing:.08em}
.script-meta{color:var(--muted);font:500 12px/1 "DM Mono",monospace}
.script>summary:after{content:"展开";margin-left:auto;color:var(--muted);font:500 12px/1 "DM Mono",monospace}
.script[open]>summary:after{content:"收起"}
.script[open]>summary{border-bottom:1px solid var(--line)}
.script-body{padding:6px 20px 20px;max-height:60vh;overflow-y:auto;overscroll-behavior:contain}
.script-p{margin:0;color:var(--muted);font-size:14px;line-height:1.85}
.script-p+.script-p{margin-top:14px}
.ts{display:inline-block;min-width:52px;margin-right:10px;color:var(--accent);font:500 11px/1.6 "DM Mono",monospace;vertical-align:top}
@media(max-width:640px){.script-body{padding:6px 16px 16px}.ts{display:block;min-width:0;margin-right:0}}
'''

TEMPLATE = '''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="data:,">
<title>LLM 入门课：Karpathy 两小时讲座全文精读 | 弈韬 Vibecoding 灵感与提示词库</title>
<meta name="description" content="Andrej Karpathy 两小时 LLM 入门讲座的中文讲稿全文，按 12 讲整理，每讲配章节要点、原始幻灯片与实操截图。">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700;800&family=DM+Mono:wght@500&display=swap');
:root{color-scheme:light dark;--bg:#f3f4f1;--paper:#fff;--ink:#171814;--muted:#62665d;--line:#d8dbd3;--accent:#ef5b2a;--soft:#ffe5d7;--code:#171a18;--codeink:#f7f6ef;--shadow:0 16px 40px rgba(26,31,23,.08)}
@media(prefers-color-scheme:dark){:root{--bg:#111310;--paper:#1a1d18;--ink:#f1f3ed;--muted:#aeb3a8;--line:#343a31;--accent:#ff7546;--soft:#492519;--code:#080a08;--codeink:#f4f6f0;--shadow:0 18px 44px rgba(0,0,0,.28)}}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--ink);font-family:"Noto Sans SC",sans-serif;line-height:1.7}.page{width:min(1080px,calc(100% - 32px));margin:auto}
.topbar{position:sticky;top:0;z-index:30;background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.topbar-in{display:flex;align-items:center;gap:14px;height:56px}
.brand{display:flex;align-items:center;gap:9px;font-weight:800;font-size:15px;text-decoration:none;color:var(--ink)}
.brand i{width:9px;height:9px;border-radius:3px;background:var(--accent);display:block}
.topbar nav{margin-left:auto;display:flex;gap:4px;flex-wrap:wrap}
.topbar nav a{font-size:13px;color:var(--muted);text-decoration:none;padding:7px 11px;border-radius:8px;white-space:nowrap}
.topbar nav a:hover{background:var(--soft);color:var(--accent)}
.topbar nav a.on{color:var(--ink);font-weight:700;background:var(--soft)}
.hero{padding:clamp(40px,7vw,84px) 0 38px;border-bottom:1px solid var(--line)}
.eyebrow{display:flex;align-items:center;gap:9px;color:var(--accent);font:600 12px/1 "DM Mono",monospace;letter-spacing:.08em}
.eyebrow:before{content:"";width:28px;height:2px;background:var(--accent)}
.hero h1{max-width:840px;margin:20px 0 16px;font-size:clamp(32px,5.6vw,60px);line-height:1.1;letter-spacing:-.04em;font-weight:800}
.lede{max-width:700px;margin:0;color:var(--muted);font-size:clamp(16px,2vw,19px)}
.meta{display:flex;gap:10px 20px;flex-wrap:wrap;margin:24px 0 0;color:var(--muted);font-size:13px}
.meta b{color:var(--ink);font-weight:700}
.credit{margin-top:22px;padding:15px 18px;border:1px solid var(--line);border-radius:13px;background:var(--paper);font-size:13px;color:var(--muted);max-width:760px}
.credit b{color:var(--ink)}
.credit a{color:var(--accent);text-decoration:none;border-bottom:1px solid var(--soft)}
.toc{position:sticky;top:56px;z-index:20;background:color-mix(in srgb,var(--bg) 93%,transparent);backdrop-filter:blur(12px);border-bottom:1px solid var(--line);padding:11px 0}
.toc-inner{display:flex;gap:7px;overflow-x:auto;scrollbar-width:thin;padding-bottom:2px}
.toc a{flex:0 0 auto;font:500 12px/1 "DM Mono",monospace;color:var(--ink);text-decoration:none;padding:9px 12px;border:1px solid var(--line);border-radius:999px;background:var(--paper);transition:border-color .18s ease,color .18s ease}
.toc a:hover{border-color:var(--accent);color:var(--accent)}
.chapter{padding:clamp(38px,6vw,64px) 0;border-bottom:1px solid var(--line);scroll-margin-top:112px}
.chapter:last-of-type{border-bottom:0}
.ch-head{display:flex;align-items:baseline;gap:14px;margin-bottom:10px}
.ch-no{color:var(--accent);font:600 13px/1 "DM Mono",monospace;letter-spacing:.06em;white-space:nowrap}
.ch-time{color:var(--muted);font:500 12px/1 "DM Mono",monospace;white-space:nowrap}
.chapter h2{margin:0 0 16px;font-size:clamp(24px,3.6vw,38px);line-height:1.22;letter-spacing:-.03em}
.chapter h2 em{font-style:normal;color:var(--accent)}
.summary{max-width:760px;margin:0 0 30px;color:var(--muted);font-size:16px}
.summary strong{color:var(--ink)}
.shot{margin:0 0 30px;border-radius:20px;overflow:hidden;background:#0d0e0c;box-shadow:var(--shadow)}
.shot img{display:block;width:100%;height:auto}
.shot figcaption{padding:13px 18px;background:var(--paper);border:1px solid var(--line);border-top:0;border-radius:0 0 20px 20px;color:var(--muted);font-size:13px}
.shot figcaption b{color:var(--ink)}
.points{display:grid;gap:1px;background:var(--line);border:1px solid var(--line);border-radius:16px;overflow:hidden;margin:0 0 26px}
.point{background:var(--paper);padding:20px 22px}
.point h3{margin:0 0 8px;font-size:16px;line-height:1.4;display:flex;gap:10px;align-items:baseline}
.point h3:before{content:"\\25C6";color:var(--accent);font-size:10px;flex:0 0 auto}
.point p{margin:0;color:var(--muted);font-size:14px}
.note{margin:0 0 26px;padding:18px 20px;border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:0 14px 14px 0;background:var(--paper);font-size:14px;color:var(--muted)}
.note b{color:var(--ink)}
footer{padding:30px 0 max(40px,env(safe-area-inset-bottom));color:var(--muted);font-size:12px}
footer a{color:var(--ink)}
@media(max-width:640px){
.page{width:min(100% - 24px,620px)}
.hero{padding-top:34px}
.toc{top:56px;margin:0 -12px;padding:11px 12px}
.ch-head{flex-wrap:wrap;gap:8px}
.point{padding:18px}
}
@@CSS_EXTRA@@
</style>
</head>
<body>
<div class="page">

<header class="topbar"><div class="topbar-in">
<a class="brand" href="index.html"><i></i>弈韬 Vibecoding</a>
<nav>
<a href="index.html">短视频灵感库</a>
<a href="motion.html">Motion 术语库</a>
<a class="on" href="course.html">LLM 入门课</a>
</nav>
</div></header>

<header class="hero">
<div class="eyebrow">DEEP DIVE COURSE</div>
<h1>两小时搞懂大语言模型<br>Karpathy 入门讲座全文精读</h1>
<p class="lede">Andrej Karpathy 用两个小时，从零讲清 LLM 是什么、怎么用、边界在哪里。这里按内容切成 12 讲，每讲先给中文要点，再附完整讲稿。</p>
<div class="meta"><span>讲师 <b>Andrej Karpathy</b></span><span>时长 <b>2 小时 03 分</b></span><span>整理 <b>12 讲</b></span><span>截图 <b>12 张</b></span><span>讲稿 <b>38,728 字</b></span></div>
<div class="credit">内容整理自 <b>Andrej Karpathy</b> 的公开讲座（<a href="https://x.com/0xkichiro/status/2115474764672225585" target="_blank" rel="noopener">原视频 ↗</a>），幻灯片与界面截图为原视频画面。讲稿由语音转写 + 机器翻译生成，再经人工校对；个别词句可能与原话有出入，以原视频为准。</div>
</header>

<nav class="toc"><div class="toc-inner">
@@TOC@@
</div></nav>

<main>

@@CHAPTERS@@

</main>

<footer>
<p>Andrej Karpathy · Deep Dive into LLMs — 两小时入门讲座。讲稿由语音转写与机器翻译生成并经校对，如与原话有出入，以原视频为准。</p>
<p><a href="index.html">短视频灵感库</a> · <a href="motion.html">Motion Prompt 术语库</a></p>
</footer>

</div>
</body>
</html>
'''

HTML = TEMPLATE
for k, v in (('@@CSS_EXTRA@@', CSS_EXTRA), ('@@TOC@@', toc), ('@@CHAPTERS@@', chapters)):
    HTML = HTML.replace(k, v)
assert '@@' not in HTML, '存在未替换的占位符'

open(OUT, 'w', encoding='utf-8').write(HTML)
print('写入 %s：%d bytes' % (OUT, len(HTML.encode())))
