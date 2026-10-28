#!/usr/bin/env python3
"""批次13：entry-137 叨叨AI UI设计Skill Apple高级审美（7卡）"""
import re

INDEX = "index.html"

entry_137 = '''<article class="entry" id="entry-137">
  <header class="entry-head"><div><h2>UI 设计 Skill：让 AI 做出 Apple 那样的高级审美</h2><div class="meta"><span>叨叨AI</span><time datetime="2026-10-28">2026-10-28</time><span>约 181 秒</span></div></div><a class="source" href="https://www.douyin.com/video/7701555838658527675" target="_blank" rel="noopener">查看原视频 <span aria-hidden="true">↗</span></a></header>
  <p class="intro">想让 AI 做的网页拥有 Apple 那样的高级审美，关键不只是配色和排版，还有视觉层级、页面留白和交互细节。叨叨AI 用一个整合了 Apple 设计语言与规范的 <strong>UI 设计 Skill</strong>，配上具体提示词，零基础做出网页和交互控件。视频给出 7 个可复用案例：两个网站（艺术作品站、建筑工作室站）+ 三个 Apple 规范控件（分段选择器、图片取色、音效调节）+ 一套贯穿始终的方法——提示词写清布局、联动与状态，再用 Skill 统一字体层级、色彩对比、留白和动效节奏。</p>
  <div class="cards">
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/daodao-137-1.jpg" alt="第1点 Apple设计语言：审美与高级交互，UI设计Skill加AI提示词，从网页布局到精致的控件反馈"><span class="num">01</span><p class="image-note">Apple 设计语言 · 审美与高级交互</p></div>
    <div class="content"><h3>Apple 设计语言：审美与高级交互</h3><p class="en">INTRODUCTION</p>
    <p class="selling">UI 设计 Skill 把 Apple 的设计语言和规范整合进去，从视觉层级、页面留白到交互细节都能让 AI 做得更精致。从网页布局到精致的控件反馈，一条路径走完。</p>
    <p class="process"><strong>怎么做的：</strong>方法分两层——<strong>提示词</strong>负责说清布局结构、联动关系和状态变化，<strong>Skill</strong>负责统一字体层级、色彩对比、留白和动效节奏。前者管"要什么"，后者管"做得一致"。两者结合，AI 输出才不散。</p>
    <p class="transcript">一个 UI 设计 Skill 就把 Apple 的设计语言和设计规范整合进去了，从视觉层级、页面留白到交互细节，都能让 AI 做得更精致。这期就用这个 Skill 搭配 AI 提示词，教你零基础做出有高级审美的网页和交互控件。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>用 UI 设计 Skill 统一 Apple 风格的字体层级、色彩对比、留白和动效节奏；提示词写清页面布局、元素联动关系和状态变化，从网页布局做到精致的控件反馈。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/daodao-137-2.jpg" alt="第2点 色彩与作品跟着滚动展开：超大标题搭配彩色扇形卡片，滚动时同一组卡片展开成台阶"><span class="num">02</span><p class="image-note">色彩与作品 · 跟着滚动展开（CHROMATIC）</p></div>
    <div class="content"><h3>色彩与作品，跟着滚动展开</h3><p class="en">CHROMATIC</p>
    <p class="selling">超大标题搭配彩色扇形卡片，第一眼就能抓住视线。向下滚动，作品卡片逐渐变成台阶式排列；点击切换按钮，卡片依次换位，作品名称也会更新。切换深色主题，背景、文字和按钮一起变化。</p>
    <p class="process"><strong>怎么做的：</strong>提示词重点写清三件事——<strong>扇形卡片布局</strong>、<strong>滚动时的排列变化</strong>（一排作品展开成台阶）、<strong>作品切换的联动关系</strong>（按钮 / 图片 / 作品名称三者联动）。主题切换时背景、文字、按钮同步响应，不是简单反色。</p>
    <p class="transcript">先看这个艺术作品网站，超大标题搭配彩色扇形卡片，第一眼就能抓住视线。向下滚动，作品卡片逐渐变成台阶式排列，点击切换按钮，卡片依次换位，作品名称也会更新。切换深色主题，背景、文字和按钮也会一起变化。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>设计一个艺术作品网站：首屏用超大标题与一排彩色扇形卡片建立视觉中心；向下滚动时同一组卡片连续展开成台阶；点击按钮让作品依次换位并更新作品名称；切换明暗主题时同步改变背景、文字和按钮。再用 UI 设计 Skill 统一排版、留白和交互反馈。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/daodao-137-3.jpg" alt="第3点 建筑成为主角大图与光线：全屏建筑摄影铺满首屏，超大标题放左下方，导航保持简洁"><span class="num">03</span><p class="image-note">建筑成为主角 · 大图与光线（GROUNDWORK）</p></div>
    <div class="content"><h3>建筑成为主角：大图与光线</h3><p class="en">GROUNDWORK</p>
    <p class="selling">整张建筑摄影铺满首屏，超大标题放在左下方，导航保持简洁，让作品成为视觉中心。点击主题按钮，页面明暗自然切换，底部还能调整光线效果，让同一座建筑呈现不同的氛围。</p>
    <p class="process"><strong>怎么做的：</strong>图片比例与留白共同形成空间感——大图铺满不加装饰边框，标题退到左下角不抢画面。主题与光线是两个独立开关：主题切明暗，光线调氛围，两者都要求文字、按钮、背景同步响应。</p>
    <p class="transcript">整张建筑摄影铺满首屏，超大标题放在左下方，导航保持简洁，让作品成为视觉中心。点击主题按钮，页面明暗自然切换，底部还能调整光线效果，让同一座建筑呈现不同的氛围。使用全屏建筑摄影和大标题排版，加入主题与光线切换，并让文字、按钮和背景同步响应。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>设计一个建筑工作室网站：全屏建筑摄影铺满首屏，超大标题放在左下方，导航保持简洁；右上角切换明暗主题时背景、文字、按钮同步更新；底部提供同一建筑的光线对比调节。用 UI 设计 Skill 控制留白、文字对比和页面层级。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/daodao-137-4.jpg" alt="第4点 选择一变数据同步回应：分段选择器切换时选中背景平滑移动，会员数量和趋势图同步更新"><span class="num">04</span><p class="image-note">选择一变 · 数据同步回应（COHORT）</p></div>
    <div class="content"><h3>选择一变，数据同步回应</h3><p class="en">COHORT · SEGMENTED CONTROL</p>
    <p class="selling">分段选择器点击顶部按钮切换不同选项，选中背景平滑移动，会员数量和趋势图同步更新。在图表上移动，还能看到对应月份的数值和高亮反馈。</p>
    <p class="process"><strong>怎么做的：</strong>这是最典型的 Apple 分段控件（All / Active / Enrolled）。三个联动必须同时发生——选中态平滑移动、统计数字变化、图表重绘。图表还要支持悬停/触摸读数，实时高亮对应数据点。</p>
    <p class="transcript">第一个分段选择器，点击顶部按钮，切换不同选项，选中背景平滑移动，会员数量和趋势图同步更新。在图表上移动，还能看到对应月份的数值和高亮反馈。分段选择器切换时，数据图表和选中状态要一起变化。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>做一个 Apple 风格分段选择器（All / Active / Enrolled），选中背景平滑移动，切换时统计数字与趋势图同步更新；图表支持移动查看对应月份数值并高亮数据点。用 UI 设计 Skill 统一卡片、圆角、留白和动效节奏。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/daodao-137-5.jpg" alt="第5点 从一张照片找到一组颜色：色块选择、颜色预览、HEX与RGB数值、复制反馈完整联动"><span class="num">05</span><p class="image-note">从一张照片找到一组颜色（PRISM）</p></div>
    <div class="content"><h3>从一张照片找到一组颜色</h3><p class="en">PRISM</p>
    <p class="selling">上方展示建筑照片，下方提取出五种代表色。点击不同色块，颜色预览、HEX 和 RGB 数值同步更新，还能直接复制颜色代码。</p>
    <p class="process"><strong>怎么做的：</strong>核心是<strong>选中联动的完整性</strong>——色块、预览、HEX、RGB、复制反馈五件套同进同退，不能只改一边。细节上控制图片比例、色块间距和选中状态，让操作路径足够短。</p>
    <p class="transcript">第二个图片取色控件，上方展示建筑照片，下方提取出五种代表色，点击不同色块，颜色预览、HEX 和 RGB 数值同步更新，还能直接复制颜色代码。设计一个图片取色组件，让色块选择、颜色数值和复制反馈形成完整联动。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>设计一个 Apple 风格图片取色组件：上方展示图片，下方排列五个取样色块；点击色块同步更新选中状态、颜色预览、HEX 和 RGB 数值，并提供一键复制与复制成功反馈。注意图片比例、色块间距和选中状态。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/daodao-137-6.jpg" alt="第6点 声音的细节交给清晰的控件：三种音效模式加低中高频滑块，模式切换参数同步变化"><span class="num">06</span><p class="image-note">声音的细节 · 交给清晰的控件（TIMBRE）</p></div>
    <div class="content"><h3>声音的细节，交给清晰的控件</h3><p class="en">TIMBRE</p>
    <p class="selling">页面以耳机作为视觉中心，下方提供三种音效模式（Balanced / Warm / Voice）和低、中、高频滑块。点击模式按钮切换不同音效，滑块和参数同步变化；手动拖动还能实时调整数值并展示进行状态。</p>
    <p class="process"><strong>怎么做的：</strong>四件事要同时做到——模式切换、滑块联动、实时数值反馈、进行状态展示（如 "Warm preset applied"），外加 Reset 重置。滑块不只报 dB 值，还要带上频段（Bass +6 dB / 180 Hz），专业感来自单位完整。</p>
    <p class="transcript">第三个音效调节控件，页面以耳机作为视觉中心，下方提供三种音效模式和低、中、高频滑块，点击模式按钮，切换不同音效，滑块和参数同步变化，手动拖动还能实时调整数值并展示进行状态。模式切换、滑块联动、实时数值反馈和进行状态。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>设计一个 Apple 风格音效调节面板：顶部展示耳机产品图，提供三种音效模式（Balanced / Warm / Voice）和低中高频滑块；模式切换时参数同步变化，拖动滑块实时反馈数值（含 dB 与频段），展示进行状态并支持重置。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/daodao-137-7.jpg" alt="第7点 网页与控件布局层级与状态：艺术作品网站、建筑设计网站、三个交互控件，视觉层级和交互状态"><span class="num">07</span><p class="image-note">网页与控件 · 布局层级与状态（DESIGN WITH AI）</p></div>
    <div class="content"><h3>网页与控件：布局层级与状态</h3><p class="en">DESIGN WITH AI</p>
    <p class="selling">把三个案例收进一张总表：艺术作品网站（色彩与作品）、建筑设计网站（建筑与光线）、三个交互控件（选择 / 双色 / 音效）。共同点是视觉层级和交互状态都清晰。</p>
    <p class="process"><strong>怎么做的：</strong>这是复盘页——三类页面形态（内容型、图片型、工具型）共享同一套底层规则：层级靠留白与对比，状态靠同步反馈。做新页面时先判断它属于哪一类，再套对应的联动清单。</p>
    <p class="transcript">三句话就是通过这个单一的模块分析，大家就可以大体了解到这个整体的架构。其实每个模块都一样，都是数据，然后你一定要有数据。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>做设计前先归类页面形态：内容型靠大标题与卡片建立视觉中心，图片型靠全屏大图与留白形成空间感，工具型靠控件联动与实时反馈表达状态。三类统一由 UI 设计 Skill 保证视觉层级和交互状态一致。</p><button class="copy" type="button">复制</button></div>
    </div></section>
  </div>
</article>'''

def main():
    html = open(INDEX, encoding="utf-8").read()
    before = html
    insert = entry_137 + "\n"
    html = html.replace("</main>", insert + "</main>")
    open(INDEX, "w", encoding="utf-8").write(html)
    print(f"OK: 插入 entry-137")
    print(f"字节: {len(before)} -> {len(html)} (+{len(html)-len(before)})")

if __name__ == "__main__":
    main()
