#!/usr/bin/env python3
"""entry-130：Xuan子《AI 做界面：先做功能 vs 先做 UI？》置顶入库。"""
import os, re, shutil, sys

PROJ = os.path.expanduser("~/workspace/promptlib")
HTML = os.path.join(PROJ, "index.html")
ASSETS = os.path.join(PROJ, "assets")
SRC = os.path.expanduser("~/workspace/tmp/xuanzi-ai-ui/final")

ENTRY_HTML = """<article class="entry" id="entry-130">
  <header class="entry-head"><div><h2>AI 做界面：先做功能 vs 先做 UI？功能搭骨架、UI 定风格</h2><div class="meta"><span>Xuan子</span><time datetime="2026-10-14">2026-10-14</time><span>约 446 秒</span></div></div><a class="source" href="https://www.douyin.com/video/7695701029802872073" target="_blank" rel="noopener">查看原视频 <span aria-hidden="true">\u2197</span></a></header>
  <p class="intro">设计出身、不会写代码的 Xuan子，用自己打磨的三版创作面板讲透 AI 做界面的顺序：先理清功能框架，再让 AI 出第一版；不好看时找参考、让 AI 按六个维度拆解；定元素、立共用规则；改到一半用四件事讲清楚；最后边用边改，一点一点磨出来。</p>
  <div class="cards">
    <section class="card card--portrait"><div class="visual"><img loading="lazy" decoding="async" src="assets/xuanzi-130-1.jpg" alt="三版创作面板并排：暖灰、银黑、新拟物，同一套规则"><span class="num">01</span><p class="image-note">三版风格：暖灰 / 银黑 / 新拟物，用的是同一套规则</p></div><div class="content"><h3>先搭功能框架，再定 UI 风格</h3><p class="en">FUNCTION FIRST, THEN UI</p><div class="prompt-label">转化版提示词</div><div class="prompt-box"><p>先帮我理清功能框架：列出产品的核心模块、每个模块承载什么内容、模块之间的数据关联，输出一张模块关系图。视觉先不做，先把骨架搭对。</p><button class="copy" type="button">复制</button></div></div></section>
    <section class="card card--portrait"><div class="visual"><img loading="lazy" decoding="async" src="assets/xuanzi-130-2.jpg" alt="拆参考六个维度：配色、布局留白、字体层级、形状比例、材质光影、动效"><span class="num">02</span><p class="image-note">找参考，让 AI 拆一拆：配色 / 布局留白 / 字体层级 / 形状比例 / 材质光影 / 动效</p></div><div class="content"><h3>找参考，让 AI 拆一拆</h3><p class="en">BREAK DOWN A REFERENCE</p><div class="prompt-label">转化版提示词</div><div class="prompt-box"><p>分析这张参考截图为什么好看，按 6 个维度拆解成可复用的设计规则：1 配色（背景 / 文字 / 强调色的用法与占比）2 布局留白（哪里紧、哪里松）3 字体层级（标题 / 正文 / 辅助信息的阅读顺序）4 形状比例（尺寸 / 圆角 / 边框）5 材质光影（表面质感 / 阴影走向）6 动效（出现 / 切换 / 点按反馈）。</p><button class="copy" type="button">复制</button></div></div></section>
    <section class="card card--portrait"><div class="visual"><img loading="lazy" decoding="async" src="assets/xuanzi-130-3.jpg" alt="定元素：三版卡片圆角都是 16，变的是颜色、边界、阴影"><span class="num">03</span><p class="image-note">圆角三版都是 16，变的是颜色、边界、阴影</p></div><div class="content"><h3>新加的组件，照元素来</h3><p class="en">NEW PARTS FOLLOW THE ELEMENTS</p><div class="prompt-label">转化版提示词</div><div class="prompt-box"><p>新增卡片 / 按钮 / 列表时，沿用既定元素：圆角统一 16；颜色、1px 边界线、阴影按当前风格取 —— 浅色版卡片 #eff0ec 配浅灰绿线、4% 极淡投影；深色版卡片 #3c3935 配 15% 暖白线、不加投影；新拟物版卡片同底色 #e9ebf1、无边框、10/18 双层阴影。</p><button class="copy" type="button">复制</button></div></div></section>
    <section class="card card--portrait"><div class="visual"><img loading="lazy" decoding="async" src="assets/xuanzi-130-4.jpg" alt="光球：6 秒无缝循环，神经网络呼吸感"><span class="num">04</span><p class="image-note">主题元素光球：6 秒无缝循环，神经网络呼吸感</p></div><div class="content"><h3>主题元素：6 秒无缝循环光球</h3><p class="en">SEAMLESS LOOP ORB</p><div class="prompt-label">转化版提示词</div><div class="prompt-box"><p>生成一段 6 秒无缝循环动画：深色线框粒子构成球体，内部有金色火花粒子，呈现神经网络的呼吸感，靠收缩与舒展形成节奏；首尾帧必须一致，保证循环接头不跳帧。输出后静音，放在页面主视觉区循环播放。</p><button class="copy" type="button">复制</button></div></div></section>
    <section class="card card--portrait"><div class="visual"><img loading="lazy" decoding="async" src="assets/xuanzi-130-5.jpg" alt="封面转场：只让封面动，标题保留"><span class="num">05</span><p class="image-note">封面转场：只让封面去转场，标题保留不动</p></div><div class="content"><h3>动效：封面转场只让封面动</h3><p class="en">COVER TRANSITION</p><div class="prompt-label">转化版提示词</div><div class="prompt-box"><p>卡片封面转场：只有封面做位移动画（约 650ms），标题文字保持不动；封面落入目标位置后结束。不要让封面和标题一起动，避免视觉混乱。</p><button class="copy" type="button">复制</button></div></div></section>
    <section class="card card--no-visual"><div class="content"><h3>改到一半，四件事讲清楚</h3><p class="en">FOUR QUESTIONS FOR ITERATION</p><div class="prompt-label">转化版提示词</div><div class="prompt-box"><p>我要改这个界面，先帮我把四件事讲清楚：1 在哪儿改 2 现在有什么问题 3 希望改成什么样 4 哪些部分必须保留。一次只改一处，改大布局前先留一个可回退的版本。</p><button class="copy" type="button">复制</button></div></div></section>
  </div>
</article>
"""

TOC_LINK = '<a href="#entry-130">AI 做界面：先做功能 vs 先做 UI？功能搭骨架、UI 定风格</a>'


def main():
    # 1. 备份
    shutil.copy2(HTML, "/tmp/index.before-entry130.html")
    html = open(HTML, encoding="utf-8").read()
    before_len = len(html.encode("utf-8"))

    # 2. 拷贝图片
    for i in range(1, 6):
        src = os.path.join(SRC, "xuanzi-130-%d.jpg" % i)
        dst = os.path.join(ASSETS, "xuanzi-130-%d.jpg" % i)
        assert os.path.exists(src), "missing " + src
        shutil.copy2(src, dst)

    # 3. 插入条目（entry-47 之前）
    anchor = '<article class="entry" id="entry-47">'
    assert anchor in html, "anchor article missing"
    assert 'id="entry-130"' not in html, "entry-130 already exists"
    html = html.replace(anchor, ENTRY_HTML + "\n" + anchor, 1)

    # 4. 目录：链接 + 计数
    toc_anchor = '<a href="#entry-47">'
    assert toc_anchor in html, "toc anchor missing"
    html = html.replace(toc_anchor, TOC_LINK + "\n" + toc_anchor, 1)
    assert html.count("目录 · 127") == 2, "count anchor mismatch: %d" % html.count("目录 · 127")
    html = html.replace("目录 · 127", "目录 · 128")

    open(HTML, "w", encoding="utf-8").write(html)

    # 5. 校验
    html2 = open(HTML, encoding="utf-8").read()
    articles = re.findall(r'<article class="entry" id="entry-(\d+)">', html2)
    assert articles[0] == "130", "top article is not 130: %s" % articles[0]
    assert len(articles) == 128, "article count %d" % len(articles)
    assert len(set(articles)) == 128, "duplicate ids"
    toc_links = re.findall(r'<a href="#entry-(\d+)">', html2)
    assert toc_links[0] == "130" and len(toc_links) == 128, "toc mismatch"
    for i in range(1, 6):
        p = os.path.join(ASSETS, "xuanzi-130-%d.jpg" % i)
        assert os.path.isfile(p) and os.path.getsize(p) > 10000, "bad img " + p
        assert ('assets/xuanzi-130-%d.jpg' % i) in html2
    print("OK: 128 articles, top=entry-130, 5 images, +%d bytes" % (len(html2.encode("utf-8")) - before_len))


if __name__ == "__main__":
    main()
