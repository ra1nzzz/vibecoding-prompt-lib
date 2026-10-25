#!/usr/bin/env python3
"""批次12：entry-136 Ludi 扒了大厂AI客户端源码，质感全靠这5招（5卡）"""
import re

INDEX = "index.html"

entry_136 = '''<article class="entry" id="entry-136">
  <header class="entry-head"><div><h2>扒了大厂 AI 客户端源码，质感全靠这 5 招</h2><div class="meta"><span>Ludi</span><time datetime="2026-10-25">2026-10-25</time><span>约 176 秒</span></div></div><a class="source" href="https://www.douyin.com/video/7699196387954642214" target="_blank" rel="noopener">查看原视频 <span aria-hidden="true">↗</span></a></header>
  <p class="intro">同样做网页和 AI 应用，为什么你用 AI 搓出来的界面总有一股廉价塑料味——打字像机关枪一样晃眼，而大厂产品用起来像艺术品一样温润丝滑？差距就在这 5 个细节上。全部可以<strong>直接写进提示词</strong>：层次用微明度色阶不画 1px、暗色模式字重整体 -40、流式输出逐字 blur 晕开、数字 tabular-nums 等宽、吸附过阻尼点赞欠阻尼。学会让你的前端和 AI 聊天应用质感原地封神。</p>
  <div class="cards">
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/ludi-136-1.jpg" alt="第1招 扔掉黑粗边框：Surface 0到3微对比色阶，每层只差1%到3%，全站不用纯黑"><span class="num">01</span><p class="image-note">扔掉黑粗边框：Surface 0–3 每层只差 1%–3%</p></div>
    <div class="content"><h3>扔掉黑粗边框</h3><p class="en">MICRO-CONTRAST SURFACE</p>
    <p class="selling">新手最爱到处画线条套大卡片，大厂全站靠的是微对比色阶——每一层背景颜色只差 1% 到 3%，靠整体氛围拉开层次，全站绝不用刺眼的纯黑色。</p>
    <p class="process"><strong>怎么做的：</strong>Surface 0 到 3 四级背景色阶依次铺开：<code>#0B0B0B</code> → <code>#151515</code> → <code>#1A1A19</code> → <code>#20201F</code>。层级不用边框表达，用极微弱的明度差表达。输入框聚焦时也不用突兀的亮线，而是让它的双环阴影整体加深，做出温润的咬合感。</p>
    <p class="transcript">很多新手做界面时，最爱到处画线条套大卡片，而大厂全站靠的是微对比色阶，每一层的背景颜色只差 1% 到 3%，靠整体氛围拉开层次，全站绝不用刺眼的纯黑色。输入框聚焦时也不用突兀的亮线，而是让它的双环阴影整体加深，做出一种温润的咬合感。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>层次用微明度色阶区分，不画 1px 边框。Surface 0 到 3 四级背景从 #0B0B0B 逐级到 #20201F，每层只差 1% 到 3%，全站不用纯黑。输入框聚焦时用双环阴影整体加深，不要亮线。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/ludi-136-2.jpg" alt="第2招 视网膜欺骗术：白底黑字wght400与黑底白字wght360，人眼看着一样粗，代码参数不一样"><span class="num">02</span><p class="image-note">视网膜欺骗术：为了人眼看着一样粗，故意让参数不一样</p></div>
    <div class="content"><h3>视网膜欺骗术</h3><p class="en">OPTICAL WEIGHT COMPENSATION</p>
    <p class="selling">同样粗细的字换成黑底白字就会显得发胖刺眼——人眼自带光晕效应，黑底上的白字看起来比实际粗一成。切到暗色模式时，代码会自动把全站文字粗细偷偷往下调一档。</p>
    <p class="process"><strong>怎么做的：</strong>白底黑字用 <code>wght 400</code>，黑底白字用 <code>wght 360</code>——为了人眼看着一样粗，故意让代码参数不一样。整套做法总结成一句能写进提示词的口诀：暗色模式字重整体 -40。</p>
    <p class="transcript">同样粗细的字换成黑底白字，就会显得发胖刺眼，这是因为人眼自带光晕效应，黑底上的白字看起来会比实际粗一成。大厂的解法太绝了，切到暗色模式时，代码会自动把全站文字的粗细偷偷往下调一档，为了人眼看着一样粗，故意让代码参数不一样。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>暗色模式下全站文字字重整体下调一档（如 wght 400 降到 360），补偿人眼光晕效应造成的发胖感，让暗色和浅色模式下肉眼粗细一致。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/ludi-136-3.jpg" alt="第3招 水墨晕染式打字：每字blur6px到0、120ms、缓动曲线，相邻错开30ms连成温柔波浪"><span class="num">03</span><p class="image-note">水墨晕染式打字：blur 6px→0 · 每字 120ms · 相邻错开 30ms</p></div>
    <div class="content"><h3>水墨晕染式打字</h3><p class="en">INK-DIFFUSION STREAMING</p>
    <p class="selling">大厂的流式打字像水墨晕染一样舒服，不是生硬地把字一个个蹦出来，而是每个字带着一段极速高斯模糊再瞬间对焦清晰，相邻字错开几十毫秒依次晕开，视觉上连成温柔的波浪。</p>
    <p class="process"><strong>怎么做的：</strong>四个参数定死：<code>blur(6px) → 0</code>、<code>每字 120ms</code>、<code>cubic-bezier(.16,1,.3,1)</code>、<code>相邻错开 30ms</code>。前一个字还没彻底清晰，下一个已经开始晕开。附带一个行内图标细节：往下挪 1/8 字高（<code>svg { vertical-align: -0.125em }</code>），让图标中心和文字严丝合缝，不再飘在字的上方。</p>
    <p class="transcript">它不是生硬地把字一个一个蹦出来，而是让每个字出来时都带着一段极速高斯模糊再瞬间对焦清晰的渐显动画，相邻的字还错开几十毫秒依次晕开，前一个字还没彻底清晰，下一个字已经开始晕开，视觉上连成温柔的波浪。而且正文里的行内小图标会悄悄往下挪八分之一个字高，让图标中心和文字严丝合缝。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>流式输出做成水墨晕染效果：每字 blur 6px 过渡到 0，单字动画 120ms，缓动用 cubic-bezier(.16,1,.3,1)，相邻字错开 30ms。正文行内图标用 vertical-align: -0.125em 与文字居中对齐。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/ludi-136-4.jpg" alt="第4招 两行代码治乱抖：等宽数字锁死宽度一致，自适应网格丝滑撑开，text-wrap:pretty防孤词"><span class="num">04</span><p class="image-note">两行代码治乱抖：等宽数字 + 自适应网格 + 排版保护</p></div>
    <div class="content"><h3>两行代码治乱抖</h3><p class="en">NO JITTER, NO ORPHANS</p>
    <p class="selling">思考计时器和数字跳动时从不左右乱晃，因为它强制开启等宽数字锁死，每个数字宽度一模一样。思考框展开时完全不用代码算高度，直接用自适应网格丝滑撑开。</p>
    <p class="process"><strong>怎么做的：</strong>三处各一行：数字用 <code>font-variant-numeric: tabular-nums</code> 锁死宽度；思考框展开用自适应网格 <code>grid-template-rows: 0fr → 1fr</code> 过渡，不靠 JS 算高度；正文再加一句 <code>text-wrap: pretty</code>，绝不让最后一个单字孤零零掉在第二行。</p>
    <p class="transcript">思考计时器和数字跳动时为什么从不左右乱晃？因为它强制开启了等宽数字锁死，每个数字的宽度一模一样。思考框展开时也完全不用代码去算高度，直接用自适应网格丝滑撑开，正文还加了一句隐藏的排版保护，绝不让最后一个单字孤零零地掉在第二行。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>数字用 tabular-nums 等宽锁死防止跳动，思考框展开用自适应网格 0fr 到 1fr 丝滑撑开，正文加 text-wrap: pretty 避免孤词掉在第二行。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/ludi-136-5.jpg" alt="第5招 动效也分性格：拖拽吸附用stiffness1200加damping80过阻尼零回弹，点赞复制用欠阻尼Q弹"><span class="num">05</span><p class="image-note">动效也分性格：拖拽要瞬间咬死，点赞要 Q 弹回弹</p></div>
    <div class="content"><h3>动效也分性格</h3><p class="en">MOTION HAS TEMPERAMENT</p>
    <p class="selling">记住这句口诀：拖拽吸附要雷厉风行，点赞反馈要欢快 Q 弹。拖拽侧边栏松手时讲究零延迟瞬间咬死，绝对不来回乱晃；但点个赞或复制代码冒出小对勾时，就要带一点点回弹。</p>
    <p class="process"><strong>怎么做的：</strong>同一套弹簧，两种参数。拖拽吸附用<strong>过阻尼</strong>：<code>stiffness 1200</code> + <code>damping 80</code>，0% 回弹，曲线快速到达终点直接平稳停住，不振荡。点赞、复制成功用<strong>欠阻尼</strong>弹簧，保留一点 Q 弹回弹。拇指图标配点赞、小对勾配复制成功，不同反馈配不同性格。</p>
    <p class="transcript">拖拽吸附要雷厉风行，点赞反馈要欢快 Q 弹。拖拽侧边栏松手时讲究零延迟瞬间咬死，绝对不来回乱晃。但点个赞或者复制代码冒出小对勾时，就要带一点点回弹的 Q 弹感。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>动效按交互分性格：拖拽吸附用过阻尼弹簧，stiffness 1200、damping 80、零回弹瞬间咬死不晃动；点赞和复制成功用欠阻尼弹簧，保留一点 Q 弹回弹。</p><button class="copy" type="button">复制</button></div>
    </div></section>
  </div>
</article>'''

def main():
    html = open(INDEX, encoding="utf-8").read()
    before = html
    insert = entry_136 + "\n"
    html = html.replace("</main>", insert + "</main>")
    open(INDEX, "w", encoding="utf-8").write(html)
    print(f"OK: 插入 entry-136")
    print(f"字节: {len(before)} -> {len(html)} (+{len(html)-len(before)})")

if __name__ == "__main__":
    main()
