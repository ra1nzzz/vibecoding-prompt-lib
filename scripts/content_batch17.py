#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批次17：小白debug「Vibe知识大赏 | Super-agent 是什么」entry-141（7卡）

7 个机制（含实测数据）：
01 双层架构 Router+Worker / 02 事件驱动 Trigger / 03 订阅与直通
04 批处理 / 05 全双工 / 06 存算分离 / 07 Watchdog
"""
import io, sys

p = 'index.html'
s = io.open(p, encoding='utf-8').read()

# ---- 1. 导航：entry-140 之后追加 entry-141 ----
NAV_ANCHOR = '<a href="#entry-140">告别 AI 模板感：3 种 Dashboard 高级审美设计</a>'
if s.count(NAV_ANCHOR) != 1:
    sys.exit('nav anchor 不唯一: %d' % s.count(NAV_ANCHOR))
if 'href="#entry-141"' in s:
    sys.exit('entry-141 已存在')
s = s.replace(NAV_ANCHOR, NAV_ANCHOR +
              '\n<a href="#entry-141">Super-agent 是什么：DeepSeek 下一代 Agent 方案拆解</a>', 1)

# ---- 2. 目录计数 138 -> 139 ----
n = s.count('目录 · 138')
if n != 2:
    sys.exit('目录计数不是2处: %d' % n)
s = s.replace('目录 · 138', '目录 · 139')
s = s.replace('<i>138 条 · 西瓜同学 / Xuan子等</i>', '<i>139 条 · 西瓜同学 / Xuan子等</i>', 1)

# ---- 3. 条目 ----
TAIL = '</main>'
if s.count(TAIL) != 1:
    sys.exit('</main> 锚点不唯一: %d' % s.count(TAIL))

def card(i, title, en, alt, note, selling, process, transcript, prompt):
    return (
        '    <section class="card card--portrait">\n'
        '    <div class="visual"><img loading="lazy" decoding="async" src="assets/xiaobai-141-%d.jpg" alt="%s"><span class="num">%02d</span><p class="image-note">%s</p></div>\n'
        '    <div class="content"><h3>%s</h3><p class="en">%s</p>\n'
        '    <p class="selling">%s</p>\n'
        '    <p class="process">%s</p>\n'
        '    <p class="transcript">%s</p>\n'
        '    <div class="prompt-label">AI 描述词</div>\n'
        '    <div class="prompt-box"><p>%s</p><button class="copy" type="button">复制</button></div>\n'
        '    </div></section>\n'
    ) % (i, alt, i, note, title, en, selling, process, transcript, prompt)

cards = []

cards.append(card(
    1, '双层架构：Router + Worker', 'ROUTER + WORKER',
    '第1个机制双层架构：常见架构主agent自己干并协调subagent，双层架构下Router只分发任务、Worker从头跟到尾，你只跟主管对接',
    '双层架构：你只跟主管对接，Worker 从头跟到尾',
    '在你和干活的 Agent 之间加一层中间层：承接你的需求、往下分发任务。这个中间层叫 **Router**，真正干活的叫 **Worker**。',
    '<strong>关键区别：</strong>主 agent 架构里主 agent <strong>得吃透整个任务逻辑、自己参与执行</strong>、还要不停协调和汇总结果；而 Router <strong>不写代码，只做判断和分发</strong>，每个任务交给一个 Worker 从头跟到尾，它只把 Worker 的结论转告给你。<strong>所以 Worker 用最强的模型，Router 用轻模型就够。</strong>打个比方：人少时你自己盯着，人一多就招个主管替你管人。',
    '双层架构是什么？同时开好几个 Agent 干活时，你一个人顾不过来怎么办呢？没有什么是加一层中间层不能解决的，如果有，那就再加一层。所以最简单的解法就是在你和 Agent 之间加一层中间层，负责承接你的需求，把任务交给下面干活的 Agent。这有点像开公司，人少的时候你可以自己盯着，人一多你就可以招个主管替你管人，你只需要跟主管对接工作就行。这个负责对接你往下分发任务的中间层就是所谓的 Router，下面那些真正干活的 Agent 则叫 Worker。Worker 用最强的模型干活，Router 自己不写代码，主要做判断和分发，所以使用轻模型就够了。',
    '搭建双层 Agent 架构：在我和执行层之间加一个 Router 中间层，只负责任务判断与分发，不写代码不参与执行，用轻量模型；每个任务完整交给一个 Worker 从头跟到尾，Worker 使用最强模型；Router 只把 Worker 的结论转告给我，不要替 Worker 做步骤拆分和结果汇总。'
))

cards.append(card(
    2, '事件驱动：让 Agent 自己找活干', 'EVENT-DRIVEN TRIGGER',
    '第2个机制事件驱动：群、GitHub、CI一天几百上千条消息，先用写死的规则按来源、发消息的人和所在的群挡住没用的，剩下的再交给大模型判断',
    '事件驱动：先规则筛选，再交给大模型判断',
    '普通 Agent 要等你打字才动。事件驱动是把它接进群、GitHub、CI 通知里一直听着——有人在群里随口说某个功能好像挂了，没艾特任何人，过一会儿就有个 Worker 自己复现修好，提了个 PR 上来。',
    '<strong>省钱关键：</strong>这些地方一天几百上千条消息，大多跟它没关系，<strong>每条都让大模型判断一次又贵又慢</strong>。所以分两层筛选：先用写死的规则按来源、发消息的人、所在的群把明显没用的挡掉，<strong>剩下的才交给大模型判断值不值得动手</strong>。从群、GitHub、CI 传入的消息叫 <strong>trigger</strong>，还可以自定义新增类型，比如日程提醒、一封会议邀约邮件。',
    '事件驱动是什么？不过到这一步，agent 还是被动的，你不发话它就不动。怎么让它自己找活干？最直接的办法是把它接进你团队每天都在用的群、GitHub 和 CI 通知里，让它一直听着。但这些地方一天几百上千条消息，大多跟它没关系，每条都让大模型判断一次，又贵又慢。所以这里分两层筛选，先用写死的规则按来源、发消息的人和所在的群，把明显没用的挡掉，剩下的再交给大模型判断值不值得动手。这些从群、GitHub、CI 传入的消息就叫 trigger，用 trigger 驱动 agent 干活的模式就是事件驱动。',
    '给 Agent 接上事件驱动：持续监听群聊、GitHub 和 CI 通知作为触发源；所有进入的消息先过一层写死的规则过滤（按来源、发送人、所在群屏蔽明显无关的），只把剩余消息交给大模型判断是否需要动手；支持自定义新增 trigger 类型，如日程提醒或会议邀约邮件，用不同方式唤醒 AI 干活。'
))

cards.append(card(
    3, '订阅与直通', 'SUBSCRIPTION & BYPASS',
    '第3个机制订阅与直通：Router派活时让Worker订阅同一串后续trigger，同一个PR下的评论和CI结果直接送到Worker手里不再经过Router',
    '订阅与直通：同一串后续 trigger 直接送达 Worker',
    'PR 提上去之后，后面还会陆续来新评论、新的 CI 结果。要是每条都先回 Router 判断该交给谁，Router 很快就成了卡点，所有消息堆积在它那里。',
    '<strong>解法：</strong>Router 把一条 trigger 派给 Worker 时，<strong>就让这个 Worker 订阅和它同一串的后续 trigger</strong>。同一个 PR 下的评论和 CI 结果、群里同一个话题的回复、同一串邮件都算「同一串」。之后这一串再有新 trigger，<strong>程序直接送到这个 Worker 手里，不再经过 Router</strong>。<strong>实测收益：让 Router 少做 30% 的判断，省下 30% 的 token。</strong>',
    '订阅和直通是什么？就拿刚才那个修 PR 的 worker 来说，PR 提上去之后，后面还会陆续来新评论、新的 CI 结果。要是每条都先回到 router，让它判断该交给谁，router 很快就成了卡点，所有消息堆积在它那里。所以 router 把一条 trigger 派给 worker 时，就让这个 worker 订阅和它同一串的后续 trigger。同一个 PR 下的评论和 CI 结果，群里同一个话题的回复，同一串邮件都算同一串。之后这一串再有新的 trigger，程序直接送到这个 worker 手里，不再经过 router。这个让 worker 认领一串 trigger，后续直接送达的机制就是所谓的订阅和直通。实测下来，它可以让 router 少做 30% 的判断，也就省下 30% 的 token。',
    '实现订阅与直通机制：Router 派发 trigger 给 Worker 时，让该 Worker 同时订阅这条 trigger 所在的整串后续消息（同一 PR 的评论与 CI 结果、同一群话题的回复、同一邮件串）；后续同串 trigger 由程序直接送达对应 Worker，不再经过 Router 判断，避免 Router 成为消息堆积的卡点。'
))

cards.append(card(
    4, '批处理：越堆积越便宜', 'BATCHING',
    '第4个机制批处理：Router正忙时新来的先攒着，等手上这批判断完再把攒下的合进一次判断，消息越堆积单条成本反而越低',
    '批处理：消息从 1分/条涨到 40 条，单条成本反而从 6.4s 降到 1.6s',
    '后续消息分走了，可新消息该派给谁还得 Router 判断。群里一下冒出几十条，它判断得过来吗？Router 的做法是：正忙的时候新来的先攒着，等手上这批判断完，再把攒下的合进一次判断里。',
    '<strong>这是全片最反直觉的一组数据：</strong>消息速率从 1 分钟 1 条涨到 1 分钟 40 条，Router 单次消耗只从 2.5 秒涨到 3.9 秒，<strong>摊到每条消息上反而从 6.4 秒降到了 1.6 秒</strong>。也就是说<strong>消息越堆积，Router 处理每一条的成本反而越低</strong>——批处理把固定开销摊薄了。做 Agent 系统时，攒批不是妥协，而是优化。',
    '后续消息分走了，可新消息该派给谁，还得 router 来判断。群里一下冒出几十条，它判断得过来吗？router 的做法是，正忙的时候新来的先攒着，等手上这批判断完，再把攒下的合进一次判断里，这就是批处理。实测消息从一分中一条涨到 40 条，Router 单次消耗只从 2.5 秒涨到 3.9 秒，摊到每条消息上反而从 6.4 秒降到了 1.6 秒。也就是说，消息越堆积，Router 处理每一条消息反而成本越低。',
    'Router 增加批处理能力：当 Router 繁忙时，新到达的 trigger 先暂存排队，等当前批次判断完成后再把积压消息合并进一次判断；把固定推理开销摊到多条消息上，目标是在消息速率上升时让单条消息的处理成本下降而非上升。'
))

cards.append(card(
    5, '全双工：跑着长任务也能插话', 'FULL DUPLEX',
    '第5个机制全双工：派活和跑命令改成异步，Worker派出去马上收到已开始，测试在后台跑这期间PR留言照样能收到，两头同时进行',
    '全双工：后台跑着任务，前台还能正常对话',
    'Router 把活派给 Worker，Worker 跑一整套测试要十几分钟。要是 Router 派完就停在那等结果，这十几分钟里你再跟它说什么，它都收不到。',
    '<strong>解法：</strong>把派活、跑命令这类耗时操作改成<strong>异步</strong>。Worker 把活派出去，马上收到一句「已经开始了」，接着就能听你说下一句；Worker 干完，<strong>结果作为一条新消息送回 Router</strong>。Worker 自己跑长命令也一样——测试在后台跑，这期间 PR 下面有人留言，它照样能收到。<strong>普通 Agent 跑长任务时你想补句话、想叫停，只能等它跑完；全双工里你随时能插话，它也能随时把跑偏的任务停掉。</strong>',
    '全双工是什么？Router 把活派给 Worker，Worker 跑一整套测试要十几分钟。要是 Router 派完就停在那等结果，这十几分钟里你再跟他说什么，他都收不到。解法是把派活、跑命令这类耗时的操作改成异步的。Worker 把活派出去，马上收到一句已经开始了，接着就能听你说下一句。Worker 干完，结果作为一条新消息送回 Router。Worker 自己跑长命令也一样，测试在后台跑，这期间 PR 下面有人留言，他照样能收到。后台跑着任务，前台还能正常对话，两头同时进行就是全双工。大多数 Agent 跑长任务时，你想补句话、想叫停，只能等他跑完。而在全双工里，你随时能插话，他也能随时把跑偏的任务停掉。',
    '实现全双工对话：把派发任务、执行长命令等耗时操作改为异步——操作发出后立即返回已开始的确认，不阻塞对话；任务完成后把结果作为一条新消息主动送回；长命令在后台运行时，前台仍可正常接收新输入，支持随时插话补充要求和叫停跑偏的任务。'
))

cards.append(card(
    6, '存算分离：合上笔记本它照样干活', 'COMPUTE-STORAGE SPLIT',
    '第6个机制存算分离：思考循环搬上云、会话记录存进数据库，执行环境留在本地，每台机器只放一个很轻的小程序听云上指令',
    '存算分离：思考上云，环境留本地',
    'Agent 跑在你这台机器上，推着他思考的循环、会话记录、干活用的环境全绑在这一台机器上——机器一停他就停，群消息触发任务的行为也跟着停。',
    '<strong>拆法：</strong>把<strong>思考的循环搬上云，会话记录存进数据库</strong>，这样不管你的机器开没开，它都一直在线。但<strong>命令最终还得在机器上跑</strong>——你本地有没提交的改动、只有内网能连的服务、一堆私人凭据，环境搬上云又麻烦又容易漏。<strong>所以环境留在本地，每台机器上只放一个很轻的小程序，听云上的指令在本地跑命令，再把结果传回去。</strong>合上笔记本，它照样在群里接活、在别的机器上干活。',
    '存算分离是什么？Agent 跑在你这台机器上，推着他一步步思考的循环，他的会话记录、他干活用的环境，全绑在这一台机器上，所以机器一停，他也就停了。前面提到的根据群里的消息触发 Agent 任务的行为也就停掉，本质原因是因为他只能运行在一台机器上。为了解决这个问题，我们可以把思考的循环搬上云，会话记录存进数据库，这样不管你的机器开没开，他都一直在线。可思考搬上云了，命令最终还得在机器上跑，干活用的环境要是也搬上云，你本地有没提交的改动、只有内网能连的服务、一堆私人凭据，搬起来又麻烦又容易漏。所以环境留在本地，每台机器上只放一个很轻的小程序，听云上的指令在本地跑命令，再把结果传回去。这种把思考和会话记录搬上云、执行环境留在本地的拆法，就是所谓的存算分离。',
    '实现存算分离：把 Agent 的思考循环和会话记录搬到云端并存入数据库，使其不依赖本地机器开关而保持在线；执行环境保留在本地，每台机器只部署一个轻量小程序，负责接收云端指令、在本地执行命令并回传结果；未提交的改动、内网服务和私人凭据都不上云。'
))

cards.append(card(
    7, 'Watchdog：谁来盯 Worker', 'WATCHDOG',
    '第7个机制Watchdog：Worker长时间在云上跑可能进死循环或越干越偏，在整套系统外面再挂一个独立Agent定时叫醒检查，发现问题及时介入修复',
    'Watchdog：定时叫醒，检测死循环和跑偏',
    'Worker 一直在云上跑，时间一长难免出问题——比如进入死循环，或者越干越偏。在整套系统外面再挂一个独立的 Agent，定时叫醒它做一轮检查。',
    '<strong>它怎么判断？</strong>用模型检测每个 Worker <strong>有没有实质进展、方向有没有跑偏</strong>，发现问题就及时介入修复。普通 Agent 卡住或跑偏，只能靠你自己发现、自己拉回来；<strong>有了 Watchdog，这件事不需要你操心。</strong>视频最后还留了个开放问题：Watchdog 盯着 Worker，那谁来盯着 Watchdog 呢？',
    'Watchdog 是什么？Worker 一直在云上跑，时间一长难免出问题，比如 Worker 现进死循环或者越干越偏，所以在整套系统外面再挂一个独立的 Agent，定时叫醒他做一轮检查，他可以用模型检测每个 Worker 有没有实质进展，方向有没有跑偏，发现问题就及时介入修复。这个在外面盯着的 Agent 就是 Watchdog。普通 Agent 卡住或跑偏，只能靠你自己发现，自己拉回来。有了 Watchdog，这件事也不需要你操心了。',
    '增加 Watchdog 看护 Agent：在主系统外挂一个独立 Agent，定时唤醒并对每个 Worker 做一轮检查；用模型判断 Worker 是否有实质进展、方向是否跑偏，发现死循环或偏离目标时自动介入修复，不需要人工持续盯守。'
))

entry = (
    '<article class="entry" id="entry-141">\n'
    '  <header class="entry-head"><div><h2>Super-agent 是什么：DeepSeek 下一代 Agent 方案拆解</h2><div class="meta"><span>小白debug</span><time datetime="2026-10-30">2026-10-30</time><span>约 468 秒</span></div></div><a class="source" href="https://www.douyin.com/video/7703746638380125466" target="_blank" rel="noopener">查看原视频 <span aria-hidden="true">↗</span></a></header>\n'
    '  <p class="intro">你一次开好几个 Agent 让他们同时干活，效率确实上去了，但你自己得在几个窗口间来回切——<strong>他们并行，你串行</strong>，你的注意力成了整个流程的瓶颈。DeepSeek 因此开源了下一代方案 <strong>Super Agent</strong>（项目名 <code>dsh-superagent</code>，注意官方说明这只是<strong>研究原型、非生产就绪</strong>）。它不是某一个功能，而是 7 个机制叠出来的系统，最终指向四个特点：<strong>连续、主动、高效、持久</strong>。</p>\n'
    '  <div class="cards">\n'
) + ''.join(cards) + (
    '  </div>\n'
    '  <p class="outro"><strong>七个机制怎么拼成 Super Agent：</strong>双层架构（Router 分发 + Worker 干活）→ 事件驱动（自己听到动静找活干，实现<strong>主动</strong>）→ 订阅与直通（同串消息直达 Worker，Router 不被堆住）→ 批处理（积压消息合并判断，越堆越便宜）→ 全双工（长任务跑着也能插话，实现<strong>高效</strong>）→ 存算分离（思考上云环境留本地，实现<strong>持久</strong>）→ Watchdog（盯着 Worker 不跑偏）。你只需要跟 Router 对接，在关键的地方做决定、做验收——<strong>那个超级管家替你管着所有会话</strong>。</p>\n'
    '</article>\n'
)

s = s.replace(TAIL, entry + '</main>', 1)
io.open(p, 'w', encoding='utf-8').write(s)
print('OK bytes=%d' % len(s.encode('utf-8')))
