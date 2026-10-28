#!/usr/bin/env python3
"""批次14：entry-138 叨叨AI UI设计必备的3个图标库（4卡）"""
import re

INDEX = "index.html"

entry_138 = '''<article class="entry" id="entry-138">
  <header class="entry-head"><div><h2>UI 设计必备的 3 个图标库</h2><div class="meta"><span>叨叨AI</span><time datetime="2026-10-28">2026-10-28</time><span>约 90 秒</span></div></div><a class="source" href="https://www.douyin.com/video/7684943500403701113" target="_blank" rel="noopener">查看原视频 <span aria-hidden="true">↗</span></a></header>
  <p class="intro">如果你做 UI、PPT、网页还在到处找图标，这 3 个图标库基本能解决你 90% 的图标需求。它们的定位完全不同，不是互相替代而是分工配合：<strong>Lucide</strong> 管最基础最常见的静态图标，<strong>Morphicons</strong> 管图标之间的状态变化，<strong>Lordicon</strong> 管动效现成的动态图标。下次用 AI 做页面或 Vibe Coding 小工具时，AI 负责快速 Web Coding 出 UI，这三个库负责把细节做精致。</p>
  <div class="cards">
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/daodao-138-1.jpg" alt="第1个 Lucide基础图标：搜索、设置、用户、菜单、返回、删除等最常见UI图标，干净的线性风格"><span class="num">01</span><p class="image-note">Lucide 基础图标：搜索 / 设置 / 用户 / 菜单 / 返回 / 删除</p></div>
    <div class="content"><h3>Lucide：基础图标</h3><p class="en">BASIC ICONS</p>
    <p class="selling">适合找最基础、最常见的 UI 图标，比如搜索、设置、用户、菜单、返回、删除这些。干净的线性风格，整体很统一，不容易让页面变乱。</p>
    <p class="process"><strong>怎么用：</strong>做网页后台系统、App 原型时首选。图标风格统一意味着你不必在不同来源的图标间来回调和粗细、圆角和视觉重量——这一点在界面元素多的时候尤其关键。位置：基础图标先去 Lucide。</p>
    <p class="transcript">第一个 Lucide，它适合找最基础、最常见的 UI 图标，比如搜索、设置、用户、菜单、返回、删除这些。它的风格是比较干净的线性图标，整体很统一，不容易让页面变乱，尤其是做网页后台系统 App 原型的时候，Lucide 这种图标会很稳。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>界面图标统一使用 Lucide 线性图标库，覆盖搜索、设置、用户、菜单、返回、删除等基础功能，保持粗细、圆角和视觉重量一致，让页面不散乱。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/daodao-138-2.jpg" alt="第2个 Morphicons状态变形：菜单变关闭、播放变暂停、加号变减号，图标之间平滑形变"><span class="num">02</span><p class="image-note">Morphicons 状态变形：菜单变关闭、加号变减号</p></div>
    <div class="content"><h3>Morphicons：状态变形</h3><p class="en">STATE MORPHING</p>
    <p class="selling">解决的不是单个图标，而是图标之间的状态变化——菜单变关闭、播放变暂停、加号变减号、太阳变月亮。特别适合放在按钮、导航、切换开关这些地方。</p>
    <p class="process"><strong>怎么用：</strong>页面本身可能很简单，但加上这种丝滑的小动效就会显得更精致。核心价值在于<strong>状态连续性</strong>：图标不是硬切换，而是路径形变平滑过渡，用户能看懂"从什么变成了什么"。</p>
    <p class="transcript">第二个 Morph Icons，它解决的不是单个图标，而是图标之间的状态变化，比如菜单变关闭、播放变暂停、加号变减号、太阳变月亮。这类图标特别适合放在按钮、导航、切换开关这些地方，页面本身可能很简单，但加上这种丝滑的小动效，就会显得更精致。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>按钮、导航和切换开关使用 Morphicons 状态变形图标，让菜单与关闭、播放与暂停、加号与减号、太阳与月亮之间平滑形变过渡，不要硬切换。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/daodao-138-3.jpg" alt="第3个 Lordicon动态图标：动效现成，适合加载中、发送完成、空状态页面等需要吸引注意力的地方"><span class="num">03</span><p class="image-note">Lordicon 动态图标：加载中 / 发送完成 / 空状态</p></div>
    <div class="content"><h3>Lordicon：动态图标</h3><p class="en">ANIMATED ICONS</p>
    <p class="selling">主打动态图标，适合用在更需要吸引注意力的地方——加载中、发送完成、空状态页面、产品介绍页，甚至 PPT 和短视频里也能用。动效现成，视觉反馈很强。</p>
    <p class="process"><strong>怎么用：</strong>优势是<strong>不用自己做动画</strong>，拿来就能让页面看起来更有生命力。适合放在用户需要"看见反馈"的位置：等待时给加载动效，完成时给成功动效，空状态时给引导动效。</p>
    <p class="transcript">第三个 Lottie Icon，它主打动态图标，适合用在更需要吸引注意力的地方，比如加载中、发送完成、空状态页面、产品介绍页，甚至 PPT 和短视频里也能用。它的优势是动效现成，视觉反馈很强，能让页面看起来更有生命力。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>加载中、发送完成、空状态、产品介绍等需要视觉反馈的位置使用 Lordicon 动态图标，动效现成直接调用，增强页面生命力。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/daodao-138-4.jpg" alt="搭配建议：基础图标去Lucide，按钮状态变化用Morphicons，动态图标用Lordicon，AI负责快速出UI"><span class="num">04</span><p class="image-note">搭配建议：AI 出 UI，图标库管细节</p></div>
    <div class="content"><h3>三个库怎么搭配</h3><p class="en">HOW TO COMBINE</p>
    <p class="selling">下次用 AI 做页面或者 Vibe Coding 一个小工具时这样分工：基础图标先去 Lucide，需要按钮状态变化看 Morphicons，想要动态图标就去 Lordicon。</p>
    <p class="process"><strong>怎么用：</strong>AI 负责快速 Web Coding 出 UI 页面，这三个图标库负责把细节做精致。一句话记住选择顺序：<strong>静态基础 → Lucide，状态变化 → Morphicons，动态反馈 → Lordicon</strong>。</p>
    <p class="transcript">所以你下次用 AI 做页面或者 Vibe Coding 一个小工具的时候，可以这样搭配：基础图标先去 Lucide，需要按钮状态变化看 Morph Icons，想要动态图标就去 Lottie Icon，AI 负责帮你快速 Web Coding 出 UI 页面，这些图标库负责帮你把细节做精致。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>给 AI 的分工指令：AI 负责快速生成 UI 页面结构与布局；静态基础图标用 Lucide，按钮与开关的状态变化用 Morphicons，加载和成功反馈等动态图标用 Lordicon，细节由图标库补齐。</p><button class="copy" type="button">复制</button></div>
    </div></section>
  </div>
</article>'''

def main():
    html = open(INDEX, encoding="utf-8").read()
    before = html
    insert = entry_138 + "\n"
    html = html.replace("</main>", insert + "</main>")
    open(INDEX, "w", encoding="utf-8").write(html)
    print(f"OK: 插入 entry-138")
    print(f"字节: {len(before)} -> {len(html)} (+{len(html)-len(before)})")

if __name__ == "__main__":
    main()
