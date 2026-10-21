#!/usr/bin/env python3
"""批次9：entry-133 西瓜同学 Dashboard 六种高级菜单设计（6卡）"""
import re

INDEX = "index.html"

entry_133 = '''<article class="entry" id="entry-133">
  <header class="entry-head"><div><h2>Dashboard 六种高级菜单设计：术语 Skill 把大白话换成 AI 描述词</h2><div class="meta"><span>西瓜同学🍉</span><time datetime="2026-10-07">2026-10-07</time><span>约 134 秒</span></div></div><a class="source" href="https://www.douyin.com/video/7695986297705450806" target="_blank" rel="noopener">查看原视频 <span aria-hidden="true">↗</span></a></header>
  <p class="intro">想让 AI 做出更有设计感的 Dashboard，菜单也有很多细节值得优化。西瓜同学整理了 6 种高级菜单设计，从位置、布局到交互方式各有各的思路，每种都配好了 AI 描述词，也讲了适合用在什么样的后台。这些做法都加入了术语设计 Skill，在 Codex、WorkBuddy 这类 Agent 里直接调用，先用它找到想要的设计，再配合 AI 描述词，就能让 AI 更准确地做出来。</p>
  <div class="cards">
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/xigua-133-1.jpg" alt="透明顶栏：去掉底色和分隔线，文字直接融入页面背景，当前项加半透明白色圆角底"><span class="num">01</span><p class="image-note">透明顶栏：去掉底色和分隔线，文字直接融入页面背景，当前项加半透明白色圆角底</p></div>
    <div class="content"><h3>透明顶栏</h3><p class="en">TRANSPARENT NAV</p>
    <p class="selling">把顶部菜单的底色和分隔线都去掉，让文字直接融入页面背景，只给当前选中项加一块半透明的白色圆角底，菜单和页面融为一体。</p>
    <p class="process"><strong>怎么做的：</strong>规格：BAR BG 0% / DIVIDER 0 / ACTIVE GLASS。首屏看起来更完整，首屏有大图或者渐变背景的后台最适合用它。</p>
    <p class="transcript">第一个透明顶栏，把顶部菜单的底色和分隔线都去掉，让文字直接融入页面背景，只给当前选中项加一块半透明的白色圆角底，菜单和页面融为一体，首屏看起来更完整。首屏有大图或者渐变背景的后台最适合用它。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>导航改为透明顶栏（Transparent Nav），去掉背景色和分隔线，文字直接落在页面背景上，当前项加半透明白色圆角底。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/xigua-133-2.jpg" alt="右侧竖轨菜单：主菜单从左边挪到最右边，收成一条窄窄的图标竖轨，左侧空间完整留给内容"><span class="num">02</span><p class="image-note">右侧竖轨菜单：主菜单从左边挪到最右边，收成一条窄窄的图标竖轨，左侧空间完整留给内容</p></div>
    <div class="content"><h3>右侧竖轨菜单</h3><p class="en">RIGHT RAIL</p>
    <p class="selling">把主菜单从左边挪到最右边，收成一条窄窄的图标竖轨，整条使用亮色，当前项用深色圆角底突出，左侧空间完整留给内容。</p>
    <p class="process"><strong>怎么做的：</strong>布局更有辨识度，内容区需要整块展示的看板可以这样排。右侧竖轨 + 左侧内容的不对称结构。</p>
    <p class="transcript">第二个，右侧竖轨菜单，把主菜单从左边挪到最右边，收成一条窄窄的图标竖轨，整条使用亮色，当前项用深色圆角底突出，左侧空间完整留给内容，布局也更有辨识度，内容区需要整块展示的看板可以这样排。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>把主菜单从左边挪到最右边，收成一条窄窄的图标竖轨（Right Rail），整条使用亮色，当前项用深色圆角底突出，左侧空间完整留给内容。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/xigua-133-3.jpg" alt="当前项展开文字：顶部菜单平时只显示图标，选中项展开成带文字的长条，切换时弹性过渡"><span class="num">03</span><p class="image-note">当前项展开文字：顶部菜单平时只显示图标，选中项展开成带文字的长条，切换时弹性过渡</p></div>
    <div class="content"><h3>当前项展开文字</h3><p class="en">EXPANDING TAB</p>
    <p class="selling">顶部菜单平时只显示图标，选中哪一项，哪一项就展开成带文字的长条，其余菜单保持紧凑，切换时再加上弹性过渡。</p>
    <p class="process"><strong>怎么做的：</strong>规格：ACTIVE 126px / ICONS 3 / EASE SPRING。一排能容纳更多入口，交互也更细腻，入口多顶栏又写不下文字的时候就用这种。</p>
    <p class="transcript">第三个，当前项展开文字，顶部菜单平时只显示图标，选中哪一项，哪一项就展开成带文字的长条，其余菜单保持紧凑，一排能容纳更多入口，切换时再加上弹性过渡，交互也更细腻，入口多顶栏又写不下文字的时候，就用这种。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>顶部导航做成图标组，当前项展开显示文字（Expanding Tab），其余只留图标，切换时宽度用弹性动画过渡。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/xigua-133-4.jpg" alt="图标菜单配大标题：侧边栏收成一列小图标，当前页面名称放大放在左上角，旁边接范围选择器"><span class="num">04</span><p class="image-note">图标菜单配大标题：侧边栏收成一列小图标，当前页面名称放大放在左上角，旁边接范围选择器</p></div>
    <div class="content"><h3>图标菜单配大标题</h3><p class="en">TITLE AS NAV</p>
    <p class="selling">侧边栏收成一列小图标，把当前页面名称放大放在左上角，旁边再接一个范围选择器，点击不同图标，大标题就跟着切换。</p>
    <p class="process"><strong>怎么做的：</strong>规格：RAIL 60px / TITLE 40px / PAGE 40px。菜单不用写字也能清楚知道自己在哪一页，页面不多的工具类后台用起来最清爽。</p>
    <p class="transcript">第四个，图标菜单配大标题，侧边栏收成一列小图标，把当前页面名称放大放在左上角，旁边再接一个范围选择器，点击不同图标，大标题就跟着切换，菜单不用写字也能清楚知道自己在哪一页，页面不多的工具类后台用起来最清爽。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>侧边栏收成一列小图标，把当前页面名称放大放在左上角（Title as Nav），旁边接一个范围选择器，点击不同图标大标题跟着切换。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/xigua-133-5.jpg" alt="图标轨加悬停提示：侧边栏只保留一列图标，鼠标停上去旁边才弹出文字提示，图标之间用细线分组"><span class="num">05</span><p class="image-note">图标轨加悬停提示：侧边栏只保留一列图标，鼠标停上去旁边才弹出文字提示，图标之间用细线分组</p></div>
    <div class="content"><h3>图标轨加悬停提示</h3><p class="en">ICON RAIL</p>
    <p class="selling">侧边栏只保留一列图标，鼠标停上去旁边才弹出对应的文字提示，图标之间再用细线分组，既节省空间也不用担心用户认错入口。</p>
    <p class="process"><strong>怎么做的：</strong>规格：RAIL 92px / TOOLTIP TRENDS / GROUPS 3。功能多屏幕又不宽的后台很适合这样做。</p>
    <p class="transcript">第五个，图标轨加悬停提示，侧边栏只保留一列图标，鼠标停上去旁边才弹出对应的文字提示，图标之间再用细线分组，既节省空间也不用担心用户认错入口，功能多屏幕又不宽的后台很适合这样做。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>侧边栏只保留一列图标（Icon Rail），鼠标停上去旁边才弹出对应的文字提示，图标之间用细线分组。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/xigua-133-6.jpg" alt="菜单旁边放快捷操作：最常用的动作单独放在菜单旁边，做成一列圆形按钮，重要操作用亮色突出"><span class="num">06</span><p class="image-note">菜单旁边放快捷操作：最常用的动作单独放在菜单旁边，做成一列圆形按钮，重要操作用亮色突出</p></div>
    <div class="content"><h3>菜单旁边放快捷操作</h3><p class="en">QUICK ACTIONS</p>
    <p class="selling">把最常用的几个动作单独放在菜单旁边，做成一列圆形按钮，最重要的操作用亮色突出，需要执行时直接点击，不用先进入某个页面再找按钮。</p>
    <p class="process"><strong>怎么做的：</strong>像新建、导出这种天天要点的动作就放在这里。快捷操作 + 关键指标网格，强调高频操作与实时数据。</p>
    <p class="transcript">第六个，菜单旁边放快捷操作，把最常用的几个动作单独放在菜单旁边，做成一列圆形按钮，最重要的操作用亮色突出，需要执行时直接点击，不用先进入某个页面再找按钮，像新建导出这种天天要点的动作就放在这里。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>把最常用的几个动作单独放在菜单旁边，做成一列圆形按钮（Quick Actions），最重要的操作用亮色突出，点击直接执行。</p><button class="copy" type="button">复制</button></div>
    </div></section>
  </div>
</article>'''

def main():
    html = open(INDEX, encoding="utf-8").read()
    before = html
    insert = entry_133 + "\n"
    html = html.replace("</main>", insert + "</main>")
    open(INDEX, "w", encoding="utf-8").write(html)
    print(f"OK: 插入 entry-133")
    print(f"字节: {len(before)} -> {len(html)} (+{len(html)-len(before)})")

if __name__ == "__main__":
    main()
