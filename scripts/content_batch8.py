#!/usr/bin/env python3
"""批次8：entry-131 林逸AIGC App加载动效（4卡）+ entry-132 西瓜同学 Dashboard布局（6卡）"""
import re

INDEX = "index.html"

# ── entry-131 林逸AIGC「你做的App加载，是不是还在转圈？」──
entry_131 = '''<article class="entry" id="entry-131">
  <header class="entry-head"><div><h2>App 加载动效：四种等待也能好看的提示词</h2><div class="meta"><span>林逸AIGC</span><time datetime="2026-10-06">2026-10-06</time><span>约 78 秒</span></div></div><a class="source" href="https://www.douyin.com/video/7694988943398482539" target="_blank" rel="noopener">查看原视频 <span aria-hidden="true">↗</span></a></header>
  <p class="intro">加载等待不一定是转圈。林逸AIGC 用四个真实案例讲透加载动效的设计思路：骨架屏扫光像退潮、图片模糊到清晰像相机对焦、加载更多像传送带、AI 流式回复像有人在打字。每个案例都对比了常见写法（干等、白屏、突然砸下来）和用提示词描述后的效果，提示词直接抄。</p>
  <div class="cards">
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/linyi-131-1.jpg" alt="骨架屏扫光：内容影子先摆好，一道光扫过去，内容一块块浮出来"><span class="num">01</span><p class="image-note">骨架屏扫光：内容影子先摆好，一道光扫过去，内容一块块浮出来</p></div>
    <div class="content"><h3>骨架屏扫光</h3><p class="en">SKELETON SHIMMER</p>
    <p class="selling">先摆好内容的影子，一道光扫过去，内容一块块浮出来，像退潮后沙滩一块块露出来。</p>
    <p class="process"><strong>怎么做的：</strong>加载时先显示和真实内容形状一样的骨架屏，然后一道 shimmer 扫光从左到右扫过，内容随着扫光一块块浮出来。慢放看就像退潮，沙滩一块块露出来。常见写法是转半天圈然后一下子全蹦出来，退潮的感觉就是靠这句话管的。</p>
    <p class="transcript">第一个，骨架屏扫光，先摆好内容的影子，一道光扫过去，内容一块块浮出来，慢放看，像退潮，沙滩一块块露出来。常见写法，转半天圈，然后一下子全蹦出来，退潮的感觉就是这句话管的。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>做一个信息流加载：先显示和真实内容形状一样的骨架屏，然后一道 shimmer 扫光从左到右扫过，内容随着扫光一块块浮出来，像退潮后沙滩一块块露出来。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/linyi-131-2.jpg" alt="模糊到清晰：图还没到先铺同色模糊，到了慢慢变清楚像相机对焦"><span class="num">02</span><p class="image-note">模糊到清晰：图还没到先铺同色模糊，到了慢慢变清楚像相机对焦</p></div>
    <div class="content"><h3>图片从模糊到清晰</h3><p class="en">BLUR TO FOCUS</p>
    <p class="selling">图还没到，先铺一层同色的模糊，到了就慢慢变清楚，像相机对焦，版面一点都不跳。</p>
    <p class="process"><strong>怎么做的：</strong>图片加载前先用同色调的模糊小图占位（主色底加高斯模糊），原图加载完后从模糊慢慢变清晰，同时从 1.04 倍轻轻缩回 1 倍，约 500ms。图片框尺寸提前固定，加载前后布局不跳。常见写法是先白一块然后图片突然砸下来，对焦的感觉靠的就是这一句。</p>
    <p class="transcript">第二个，图片从模糊到清晰，图还没到，先铺一层同色的模糊，到了就慢慢变清楚，像相机对焦，越来越清楚，版面一点都不跳。常见写法，先白一块，图片突然砸下来，对焦的感觉，靠的就是这一句。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>做一个照片墙：每张图先用同色调的模糊小图占位（主色底加 20px 高斯模糊），原图加载完后从模糊慢慢变清晰，同时从 1.04 倍轻轻缩回 1 倍，约 500ms；图片框尺寸提前固定，加载前后布局不跳。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/linyi-131-3.jpg" alt="加载更多：还没滑到底就提前加载，新商品一件件接上来像传送带"><span class="num">03</span><p class="image-note">加载更多：还没滑到底就提前加载，新商品一件件接上来像传送带</p></div>
    <div class="content"><h3>滑到底加载更多</h3><p class="en">INFINITE SCROLL PREFETCH</p>
    <p class="selling">还没滑到底，它就提前开始加载，新商品一件件接上来，像传送带。</p>
    <p class="process"><strong>怎么做的：</strong>无限滚动加预取，用户还没滑到底部就提前开始加载下一页，三个小点在跳表示正在加载，新商品一件件接上来，像传送带一样连续。常见写法是卡一下然后一堆内容突然塞进来，传送带的感觉写在这一句。</p>
    <p class="transcript">第三个，滑到底加载更多，还没滑到底，它就提前开始加载，三个小点在跳，新商品一件件接上来，像传送带。常见写法，卡一下，一堆内容突然塞进来，传送带的感觉，写在这一句。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>做一个商品列表：无限滚动加预取，用户还没滑到底部就提前开始加载下一页，底部显示三个小点在跳表示正在加载，新商品一件件接上来，像传送带一样连续。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/linyi-131-4.jpg" alt="AI流式回复：一发送气泡马上出来，小点在呼吸，回复一段段浮出来像打字"><span class="num">04</span><p class="image-note">AI 流式回复：一发送气泡马上出来，小点在呼吸，回复一段段浮出来像打字</p></div>
    <div class="content"><h3>AI 流式回复</h3><p class="en">STREAMING AI REPLY</p>
    <p class="selling">一发送，气泡马上出来，小点在呼吸，回复一段段浮出来，像有人在对面打字。</p>
    <p class="process"><strong>怎么做的：</strong>AI 聊天回复，发送后立刻出现回复气泡，里面三个小点呼呼跳动表示正在思考，开始回复后逐字流出，像有人在对面打字。常见写法是干等几秒然后字一个个蹦、页面还不跟着走，真人打字的感觉就是这句话。</p>
    <p class="transcript">第四个，AI 流式回复，一发送，气泡马上出来，小点在呼吸，说明它在想，回复一段段符出来，像有人在对面打字。常见写法，干等几秒，字一个个蹦，页面还不跟着走，真人打字的感觉就是这句话。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>做一个 AI 聊天回复：发送后立刻出现回复气泡，里面三个小点呼呼跳动表示正在思考；开始回复后逐字流出，像有人在对面打字，页面跟着回复内容自动滚动。</p><button class="copy" type="button">复制</button></div>
    </div></section>
  </div>
</article>'''

# ── entry-132 西瓜同学🍉「设计术语Skill，让AI做出高级Dashboard布局」──
entry_132 = '''<article class="entry" id="entry-132">
  <header class="entry-head"><div><h2>Dashboard 六种高级布局：术语 Skill 把大白话换成 AI 描述词</h2><div class="meta"><span>西瓜同学🍉</span><time datetime="2026-10-06">2026-10-06</time><span>约 170 秒</span></div></div><a class="source" href="https://www.douyin.com/video/7694506689243942179" target="_blank" rel="noopener">查看原视频 <span aria-hidden="true">↗</span></a></header>
  <p class="intro">AI 做 Dashboard 后台页面，最怕满屏都是卡片、数据不少重点却看不出来。西瓜同学分享 6 种高级 Dashboard 布局，每种都配好了由术语 Skill 整理的 AI 描述词。核心方法论：把想要的样子用大白话说给术语 Skill，它会换成一句准确的 AI 描述词，名字叫不出来也没关系。</p>
  <div class="cards">
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/xigua-132-1.jpg" alt="主次布局：首屏一个最大模块占一半以上面积，其余指标缩成小块贴在右边和下面"><span class="num">01</span><p class="image-note">主次布局：首屏一个最大模块占一半以上面积，其余指标缩成小块贴在右边和下面</p></div>
    <div class="content"><h3>主次布局</h3><p class="en">HERO MODULE</p>
    <p class="selling">首屏只留一个最大的模块，占掉一半以上的面积，放这一页最重要的那张图，其余指标缩成小块贴在它的右边和下面。</p>
    <p class="process"><strong>怎么做的：</strong>规格：HERO 8col×2row / SIDE 4col / FOCUS 1。对术语 Skill 说"页面没有重点"，它给出的就是主次布局的 AI 描述词，发给 AI，主模块还能换到另一边。进来第一眼就知道该看哪。</p>
    <p class="transcript">第一个，主次布局。首屏只留一个最大的模块，占掉一半以上的面积，放这一页最重要的那张图，其余指标缩成小块，贴在它的右边和下面，进来第一眼就知道该看哪。这次对数语 Skill 说页面没有重点，它给出的就是主次布局的 AI 描述词，发给 AI，主模块还能换到另一边。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>首屏采用主次布局（Hero Module），主模块占 8 列跨两行，放这一页最重要的图表；其余指标缩成 4 列小模块，贴在主模块的右边和下面，全页只有一个视觉重心。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/xigua-132-2.jpg" alt="横带分层：整页从上到下切成三条通栏横带，概览、趋势、明细各一条"><span class="num">02</span><p class="image-note">横带分层：整页从上到下切成三条通栏横带，概览、趋势、明细各一条</p></div>
    <div class="content"><h3>横带分层</h3><p class="en">STACKED BANDS</p>
    <p class="selling">整页从上到下切成三条通栏的横带，第一条放概览数字，第二条放趋势图，第三条放明细列表，视线从上往下走一遍就从结论看到了细节。</p>
    <p class="process"><strong>怎么做的：</strong>规格：BANDS 3 / WIDTH 100% / GAP 48px。对术语 Skill 说"模块东一块西一块"，拿到的是通栏横带的 AI 描述词，发给 AI，趋势那一条还能提到最上面。术语映射：通栏横带 / Stacked Bands。</p>
    <p class="transcript">第二个，横带分层。整页从上到下切成三条通栏的横带，第一条放概览数字，第二条放趋势图，第三条放明细列表，每一条都横贯整个页面，视线从上往下走一遍，就从结论看到了细节。这次对数语 Skill 说模块东一块西一块，拿到的是通栏横带的 AI 描述词，发给 AI 趋势，那一条还能提到最上面。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>页面采用通栏横带布局（Stacked Bands），自上而下分为概览、趋势、明细三层，每层横贯全宽，层与层之间留 48 像素间距。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/xigua-132-3.jpg" alt="主区加右侧窄栏：左边三分之二是主区，右边 320px 窄栏 sticky 固定放日程动态提醒"><span class="num">03</span><p class="image-note">主区加右侧窄栏：左边三分之二是主区，右边 320px 窄栏 sticky 固定放日程动态提醒</p></div>
    <div class="content"><h3>主区加右侧窄栏</h3><p class="en">MAIN + ASIDE</p>
    <p class="selling">左边三分之二是主区放图表和列表，右边留一条窄栏固定放日程、动态和提醒，主区往下滚动时它一直停在原地。</p>
    <p class="process"><strong>怎么做的：</strong>规格：MAIN 8col / ASIDE 320px sticky / top 0。说的是"一滚下去提醒就没了"，术语 Skill 给出的是粘性定位这个词，发给 AI，窄栏换到左边也一样。要盯的东西和要翻的东西分开放，谁也不挤谁。</p>
    <p class="transcript">第三个主区加右侧窄栏，左边三分之二是主区放图表和列表，右边留一条窄栏，固定放日程、动态和提醒。主区往下滚动时，它一直停在原地，要盯的东西和要翻的东西分开放，谁也不挤谁。这次说的是，一滚下去提醒就没了，术语 skill 给出的是粘性定位这个词，发给 AI，窄栏换到左边也一样。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>左边三分之二是主区放图表和列表，右侧 320px 窄栏 sticky 固定（top 0）放日程、动态和提醒，主区滚动时窄栏停在原地。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/xigua-132-4.jpg" alt="画布铺满加浮动面板：地图或大图铺满主区当底，数字列表做成圆角面板浮在上面"><span class="num">04</span><p class="image-note">画布铺满加浮动面板：地图或大图铺满主区当底，数字列表做成圆角面板浮在上面</p></div>
    <div class="content"><h3>画布铺满加浮动面板</h3><p class="en">FULL-BLEED CANVAS</p>
    <p class="selling">把地图或者一整张大图铺满主区当底，数字和列表做成几块圆角面板浮在它上面，页面一下有了前后两层。</p>
    <p class="process"><strong>怎么做的：</strong>规格：CANVAS full-bleed / PANELS 4 floating / INSET 16px。说"图和数字各占一半"，术语 Skill 给的是全幅画布的 AI 描述词，发给 AI，面板还能改成沿着底边排。贴着四个角摆放，画面也更完整。</p>
    <p class="transcript">第四个，画布铺满加浮动面板，把地图或者一整张大图铺满主区当底，数字和列表做成几块圆角面板，浮在它上面，贴着四个角摆放，页面一下有了前后两层，画面也更完整。这次说图和数字各占一半，术语 skill 给的是全幅画布的 AI 描述词，发给 AI，面板还能改成沿着底边排。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>把地图或者一整张大图铺满主区当底（full-bleed），数字和列表做成 4 块圆角面板浮在它上面，贴着四个角摆放，面板内边距 16px。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/xigua-132-5.jpg" alt="看板分列：内容按状态分成几列并排，每列顶上是列名和数量，下面是一摞同样宽度的小块"><span class="num">05</span><p class="image-note">看板分列：内容按状态分成几列并排，每列顶上是列名和数量，下面是一摞同样宽度的小块</p></div>
    <div class="content"><h3>看板分列</h3><p class="en">KANBAN COLUMNS</p>
    <p class="selling">内容按状态分成几列并排，每一列顶上是列名和数量，下面是一摞同样宽度的小块，每件事走到哪一步，位置本身就说明了。</p>
    <p class="process"><strong>怎么做的：</strong>规格：COLUMNS 5×216px / COUNT 2-3 / SCROLL x 8px。说"不知道进行到哪一步"，术语 Skill 会换成看板分列的 AI 描述词，发给 AI，列再多也能排进一屏。列多了就横向滚动。</p>
    <p class="transcript">第五个，看板分列，内容按状态分成几列并排，每一列顶上是列名和数量，下面是一摞同样宽度的小块，列多了就横向滚动，每件事走到哪一步，位置本身就说明了。这次说不知道进行到哪一步，术语 skill 会换成看板分列的 AI 描述词，发给 AI，列再多也能排进一屏。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>内容按状态分成 5 列并排（每列 216px），每一列顶上是列名和数量，下面是一摞同样宽度的小块，列多了就横向滚动。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/xigua-132-6.jpg" alt="时间轴泳道：顶上横着时间刻度，下面每一行是一条泳道，事项按时间画成横条"><span class="num">06</span><p class="image-note">时间轴泳道：顶上横着时间刻度，下面每一行是一条泳道，事项按时间画成横条</p></div>
    <div class="content"><h3>时间轴泳道</h3><p class="en">TIMELINE SWIMLANES</p>
    <p class="selling">顶上横着一条时间刻度，下面每一行是一条泳道，事项按开始和结束时间画成长短不一的横条，再加一条竖线标出现在。</p>
    <p class="process"><strong>怎么做的：</strong>规格：LANES 5 / SPAN 08:00-18:00 / NOW 14:09。说"看不出谁和谁撞了"，拿到的就是时间轴泳道的 AI 描述词，发给 AI，时间范围还能再拉长。谁在忙、哪里撞了、哪里空着，横着扫一眼就清楚。</p>
    <p class="transcript">第六个，时间轴泳道，顶上横着一条时间刻度，下面每一行是一条泳道，事项按开始和结束时间画成长短不一的横条，再加一条竖线标出现在，谁在忙，哪里撞了，哪里空着，横着扫一眼就清楚。这次说看不出谁和谁撞了，拿到的就是时间轴泳道的 AI 描述词，发给 AI，时间范围还能再拉长。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>顶部为时间刻度（08:00-18:00），下面 5 行泳道，事项按开始和结束时间画成长短不一的横条，用竖向参考线标记当前时刻（14:09）。</p><button class="copy" type="button">复制</button></div>
    </div></section>
  </div>
</article>'''

def main():
    html = open(INDEX, encoding="utf-8").read()
    before = html
    # 在 </main> 前插入两条新条目
    insert = entry_131 + "\n" + entry_132 + "\n"
    html = html.replace("</main>", insert + "</main>")
    open(INDEX, "w", encoding="utf-8").write(html)
    print(f"OK: 插入 entry-131 + entry-132")
    print(f"字节: {len(before)} -> {len(html)} (+{len(html)-len(before)})")

if __name__ == "__main__":
    main()
