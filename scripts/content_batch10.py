#!/usr/bin/env python3
"""批次10：entry-134 叨叨AI Dashboard 四种高级审美后台排版设计（4卡）"""
import re

INDEX = "index.html"

entry_134 = '''<article class="entry" id="entry-134">
  <header class="entry-head"><div><h2>Dashboard 四种高级审美排版：配色、层级与版面判断</h2><div class="meta"><span>叨叨AI</span><time datetime="2026-10-24">2026-10-24</time><span>约 153 秒</span></div></div><a class="source" href="https://www.douyin.com/video/7688196900479253946" target="_blank" rel="noopener">查看原视频 <span aria-hidden="true">↗</span></a></header>
  <p class="intro">同样是做 Dashboard 页面，为什么有的高级有设计感，有的却还是一股 AI 模板感？差别常常不在组件多复杂，而在配色、层级和版面判断。叨叨AI 拆解四种高级后台排版做法，每种配一句提示词，拿走就能用。核心心法：一整页只做一个判断——要么只亮一个颜色，要么只留一块深色，要么把所有层级都交给明度，先把这个判断定下来再往里填内容，页面就不会散。</p>
  <div class="cards">
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/daodao-134-1.jpg" alt="方格纸加玻璃卡：44像素方格纸铺满不留外框，半透明白玻璃卡浮在上面，顶部指标按数值排成递增阶梯"><span class="num">01</span><p class="image-note">方格纸加玻璃卡：44 像素方格纸铺满不留外框，半透明白玻璃卡浮在上面，顶部指标按数值排成递增阶梯</p></div>
    <div class="content"><h3>方格纸加玻璃卡</h3><p class="en">GRID &amp; GLASS</p>
    <p class="selling">底色是一张 44 像素的方格纸铺满整个窗口，四周不留外框，卡片做成半透明白玻璃浮在上面，底下的格线能透过来。</p>
    <p class="process"><strong>怎么做的：</strong>顶部那排指标别做成等大的卡片，按数值排成一道阶梯，填充从实心换到点阵、斜纹再换到渐变。网格底 + 玻璃卡，界面铺满窗口不加外框，内容直接延伸到画面边缘。</p>
    <p class="transcript">第一个方格纸加玻璃卡，底色是一张 44 像素的方格纸，铺满整个窗口，四周不留外框。卡片做成半透明的白玻璃浮在上面，底下的格线能透过来。顶部那排指标别做成等大的卡片，按数值排成一道阶梯，填充从实心换到斜纹再换到渐变。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>页面底色用 44 像素方格纸铺满不留外框，卡片做成半透明白玻璃浮在上面，顶部指标按数值排成递增的阶梯色块，用实心、斜纹、渐变区分。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/daodao-134-2.jpg" alt="分组侧边栏：导航分三组，组间留一大段空白，组名用10像素大写灰字，栏底钉一块固定区"><span class="num">02</span><p class="image-note">分组侧边栏：导航分三组，组间留一大段空白，组名用 10 像素大写灰字，栏底钉一块固定区</p></div>
    <div class="content"><h3>分组侧边栏</h3><p class="en">GROUPED RAIL</p>
    <p class="selling">导航分成三组，组和组之间留一大段空白，组名用 10 像素的大写灰字，栏底钉一块固定区放头像和用量条。</p>
    <p class="process"><strong>怎么做的：</strong>主区第一行不放标题，放一句超大的细体文字；右边并排三个一样大的数字占比，不画饼图，摊成一条横贯整行的比例条，四段按比例分宽。组名用小字号大写灰色弱化但保持清晰。</p>
    <p class="transcript">第二个分组侧边栏，导航分成三组，组和组之间留一大段空白，组名用 10 像素的大写灰字栏底钉一块固定区。主区第一行不放标题，放一句超大的细体文字，右边并排三个一样大的数字占比，也不画饼图，摊成一条横贯整行的比例条，四段按比例分宽。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>侧边栏按组划分，组间留大段空白，组名用 10 像素大写灰字栏底，固定放头像和用量条，主区首行用超大的细体文字配三个并排大数字，占比用一条横贯的分段比例条。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/daodao-134-3.jpg" alt="一块深色配一个强调色：整页浅底，唯一深色留给侧边栏，强调色只给当前项、主按钮和图表命中值"><span class="num">03</span><p class="image-note">一块深色配一个强调色：整页浅底，唯一深色留给侧边栏，强调色只给当前项、主按钮和图表命中值</p></div>
    <div class="content"><h3>一块深色配一个强调色</h3><p class="en">ONE DARK ONE ACCENT</p>
    <p class="selling">整页浅底，唯一的深色留给侧边栏那一条，页面上再没有第二块深的；强调色也只给一个，别的地方一律不上色。</p>
    <p class="process"><strong>怎么做的：</strong>强调色只用在三处：当前项、主按钮、图表里命中的那几根。侧栏底部垫一张强调色的卡片把栏收住。深色侧边栏 + 浅色内容区 + 一个亮色强调点，层次分明重点突出。</p>
    <p class="transcript">第三个一块深色配一个强调色，整页浅底，唯一的深色留给侧边栏那一条，页面上再没有第二块深的，强调色也只给一个，当前项主按钮，图表里命中的那几根都是它，别的地方一律不上色。侧栏底部垫一张强调色的卡片把栏收住。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>整页用浅色，只给侧边栏一块深色重底，全页只用一个强调色（当前项、主按钮和图表命中值），侧栏底部放一张强调色卡片收口。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/daodao-134-4.jpg" alt="暗底明度分层：整页压到近黑，卡片比底色亮一档，层级全靠明度拉开，一条描边都不画"><span class="num">04</span><p class="image-note">暗底明度分层：整页压到近黑，卡片比底色亮一档，层级全靠明度拉开，一条描边都不画</p></div>
    <div class="content"><h3>暗底明度分层</h3><p class="en">TONE LAYERS</p>
    <p class="selling">整页压到近黑，卡片比底色亮一档，层级全靠明度拉开，一条描边都不画；主读数给到极大，数字占满，单位缩到角上。</p>
    <p class="process"><strong>怎么做的：</strong>日期区不画方格表，排成一片圆点阵列，有内容的顶一颗彩色徽章，空格用斜纹填掉。用明度差异做层级，比描边更干净，减少深色界面里的视觉杂乱。</p>
    <p class="transcript">第四个，暗底明度分层，整页压到近黑，卡片比底色亮一档，层级全靠明度拉开，一条描边都不画，主读数给到极大，数字占满，单位缩到角上，日期区不画方格表，排成一片圆点阵列，有内容的顶一颗彩色徽章，空格用斜纹填掉。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>做一个深色后台卡片，用比背景亮一档的灰分层，不描边，主读数用超大数字配小号单位，日期区用圆点阵列加彩色徽章，空位走斜纹。</p><button class="copy" type="button">复制</button></div>
    </div></section>
  </div>
</article>'''

def main():
    html = open(INDEX, encoding="utf-8").read()
    before = html
    insert = entry_134 + "\n"
    html = html.replace("</main>", insert + "</main>")
    open(INDEX, "w", encoding="utf-8").write(html)
    print(f"OK: 插入 entry-134")
    print(f"字节: {len(before)} -> {len(html)} (+{len(html)-len(before)})")

if __name__ == "__main__":
    main()
