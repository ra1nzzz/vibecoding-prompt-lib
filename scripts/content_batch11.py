#!/usr/bin/env python3
"""批次11：entry-135 搞钱艺术家 高密度数据界面怎么做到层次分明（4卡）"""
import re

INDEX = "index.html"

entry_135 = '''<article class="entry" id="entry-135">
  <header class="entry-head"><div><h2>高密度数据界面，怎么做到层次分明</h2><div class="meta"><span>搞钱艺术家 · 精选UI/UX 第16期</span><time datetime="2026-10-25">2026-10-25</time><span>约 95 秒</span></div></div><a class="source" href="https://www.douyin.com/video/7700257819165550259" target="_blank" rel="noopener">查看原视频 <span aria-hidden="true">↗</span></a></header>
  <p class="intro">高密度看板最怕做成大号 Excel——堆满数据、杂乱无序。这套多场景 Dashboard（项目管理、财务、电商、CRM）数据同样密集，信息层级却保持清晰有序。它的成熟不在组件多丰富，而在<strong>信息分量的取舍</strong>：总览突出焦点，详情方便阅读，表单优先操作。页面各有表达，却没有失去整体感。</p>
  <div class="cards">
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/gqartist-135-1.jpg" alt="项目管理首页：指标卡不平均排开，状态指标给宽空间，项目状态用环形图配明细"><span class="num">01</span><p class="image-note">项目管理首页：卡片不平均排开，指标先看结果、趋势给更宽空间</p></div>
    <div class="content"><h3>总览页：布局跟着阅读需求走</h3><p class="en">LAYOUT FOLLOWS READING</p>
    <p class="selling">首页没有把卡片平均排开。指标先看结果，趋势要看变化就给图表更宽的空间；项目状态用仪表图配明细，布局跟着阅读需求走。</p>
    <p class="process"><strong>怎么做的：</strong>先回答「这一屏用户最先看什么」再决定谁大谁小——结果型指标做成紧凑卡片，趋势型图表占据更宽区块，状态汇总配明细图表。格子不是等分的，是按阅读优先级分配的。</p>
    <p class="transcript">首页没有把卡片平均排开，指标先看结果，趋势要看变化就给图表更宽的空间。项目状态用仪表图配明细，布局跟着阅读需求走。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>做一个项目管理 Dashboard 首页，卡片不要平均排开：结果型指标做成紧凑卡片，趋势型图表给更宽的区块，项目状态用环形图配明细列表，布局按阅读优先级分配。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/gqartist-135-2.jpg" alt="财务页：深色银行卡先拉开对比，蓝绿区分收支，圆环看资产，钱包交易只在重点处用色"><span class="num">02</span><p class="image-note">财务页：深色银行卡先拉开对比，交易只在重点处用色</p></div>
    <div class="content"><h3>财务页：强对比只放在重点上</h3><p class="en">CONTRAST ONLY AT FOCUS</p>
    <p class="selling">财务页的深色银行卡先拉开对比，重点一下就稳住了。蓝绿区分收支，圆环看资产，钱包交易只在重点处用色，丰富却不乱。</p>
    <p class="process"><strong>怎么做的：</strong>整页只用两处强对比——深色银行卡作为视觉锚点 + 蓝绿双色区分收入支出。其余模块走灰阶和细线，颜色不重复发放。这样页面元素很多，但「抢眼」的位置是可控的。</p>
    <p class="transcript">财务页的深色银行卡先拉开对比，重点一下就稳住了。蓝城区分收支，圆环看资产，钱包交易只在重点处用色，丰富却不乱。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>做一个财务管理 Dashboard，用一张深色银行卡作为视觉锚点拉开对比，蓝绿两色区分收入与支出，资产构成用圆环图，交易列表只在状态处用色，其余走灰阶。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/gqartist-135-3.jpg" alt="项目详情页：橙色横幅作记忆点后正文立刻收住，活动讨论放主列，预算成员放侧边"><span class="num">03</span><p class="image-note">项目详情页：活动讨论放主列，预算成员放侧边</p></div>
    <div class="content"><h3>详情页：视觉亮点留在开头</h3><p class="en">HERO THEN QUIET</p>
    <p class="selling">项目详情的橙色横幅很有记忆点，正文却立刻收住。活动和讨论放主列，预算成员放侧边，视觉亮点留在开头，后面把空间让给阅读。</p>
    <p class="process"><strong>怎么做的：</strong>把高饱和元素当作「记忆点」只用一次——放在页面开头。正文区域立刻降低彩度，主列放需要连续阅读的内容（活动流、讨论），侧栏放参考型内容（预算、成员）。先给情绪，再给信息。</p>
    <p class="transcript">项目详情的橙色横幅很有记忆点，正文却立刻收住。活动和讨论放主列，预算成员放侧边，视觉亮点留在开头，后面把空间让给阅读。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>做一个项目详情页，顶部用一条高饱和横幅作为视觉记忆点，正文区域立刻降低彩度，活动流和讨论放主列，预算和团队成员收进右侧侧栏。</p><button class="copy" type="button">复制</button></div>
    </div></section>
    <section class="card card--portrait">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/gqartist-135-4.jpg" alt="组件库：卡片图表有尺寸变体，表格结构一致，给出组件替换说明"><span class="num">04</span><p class="image-note">组件库：卡片图表有尺寸变体，表格有一致结构</p></div>
    <div class="content"><h3>组件库：底层规则保持统一</h3><p class="en">UNIFIED RULES</p>
    <p class="selling">组件库不只是堆样式，卡片和图表有尺寸变体，表格有一致的结构，还给出组件替换说明。各业务可以长得不同，底层规则却保持统一。</p>
    <p class="process"><strong>怎么做的：</strong>把「变化」限制在内容层，把「不变」沉淀到组件层。同一张卡片有大中小三种尺寸变体，表格列结构全站一致，替换说明写清什么场景用什么变体——这样多场景页面才既丰富又整体。</p>
    <p class="transcript">组件库不只是堆样式，卡片和图表有尺寸变体，表格有一致的结构，还给出组件替换说明，各业务可以长得不同，底层规则却保持统一。</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>设计一套高密度 Dashboard 组件库，卡片和图表提供大中小三种尺寸变体，全站表格列结构保持一致，并为每个组件写明替换说明与适用场景。</p><button class="copy" type="button">复制</button></div>
    </div></section>
  </div>
</article>'''

def main():
    html = open(INDEX, encoding="utf-8").read()
    before = html
    insert = entry_135 + "\n"
    html = html.replace("</main>", insert + "</main>")
    open(INDEX, "w", encoding="utf-8").write(html)
    print(f"OK: 插入 entry-135")
    print(f"字节: {len(before)} -> {len(html)} (+{len(html)-len(before)})")

if __name__ == "__main__":
    main()
