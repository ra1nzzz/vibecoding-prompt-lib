#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批次18校验：entry-142 注入"""
import io, re, os, sys

BASE = '/tmp/index.before-batch18.html'
if not os.path.isfile(BASE):
    BASE = '/tmp/index.before-batch17.html'
if not os.path.isfile(BASE):
    sys.exit('找不到 before 基准')
before = io.open(BASE, encoding='utf-8').read()
after = io.open('index.html', encoding='utf-8').read()
fails = []

def check(name, cond, extra=''):
    print(('PASS  ' if cond else 'FAIL  ') + name + (' :: ' + extra if extra else ''))
    if not cond:
        fails.append(name)

nb = len(re.findall(r'<article class="entry" id="entry-\d+">', before))
na = len(re.findall(r'<article class="entry" id="entry-\d+">', after))
check('条目数 139→140', nb == 139 and na == 140, '%d→%d' % (nb, na))

def nav_ids(s):
    i = s.find('<div class="library-nav-list"')
    j = s.find('</nav>', i)
    return re.findall(r'href="#entry-(\d+)"', s[i:j])
vb, va = nav_ids(before), nav_ids(after)
check('nav 139→140', len(vb) == 139 and len(va) == 140, '%d→%d' % (len(vb), len(va)))
kept = [x for x in va if x != '142']
check('nav 原顺序保留', kept == vb)
i141 = va.index('141')
check('entry-142 紧邻 entry-141 之后', va[i141 + 1] == '142', '实际: %s' % va[i141 + 1:i141 + 3])

arts = set(re.findall(r'<article class="entry" id="entry-(\d+)"', after))
check('nav 与 article 完全一致', set(va) == arts,
      '仅 nav: %s / 仅 art: %s' % (set(va) - arts, arts - set(va)))

check('目录计数 140（2处）', after.count('目录 · 140') == 2, str(after.count('目录 · 140')))
check('tab 副标题 140 条', '140 条 · 西瓜同学 / Xuan子等' in after)

def entry_pos(s):
    return {m.group(1): s.find('<article class="entry" id="%s">' % m.group(1))
            for m in re.finditer(r'<article class="entry" id="entry-(\d+)\">', s)}
pb, pa = entry_pos(before), entry_pos(after)
moved = [k for k in pb if pb[k] != pa.get(k)]
check('旧条目 DOM 位置未变', not moved, '被移动: %s' % moved)
check('新增条目仅 entry-142', set(pa) - set(pb) == {'142'}, '意外: %s' % (set(pa) - set(pb)))

m = re.search(r'<article class="entry" id="entry-142">(.*?)</article>', after, re.S)
check('entry-142 存在', m is not None)
if m:
    e = m.group(1)
    check('7 张卡', e.count('<section class="card">') == 7, str(e.count('<section class="card">')))
    check('7 个 prompt-box', e.count('class="prompt-box"') == 7)
    check('7 个 image-note', e.count('class="image-note"') == 7)
    check('1 个 intro', e.count('class="intro"') == 1)
    check('1 个 outro', e.count('class="outro"') == 1)
    check('引 7 张新图', len(set(re.findall(r'assets/pengfei-spine-(\d+)\.jpg', e))) == 7)
    check('源链接', '7702773238065040649' in e)
    check('编号 01-07', all('>0%d<' % i in e for i in range(1, 8)))
    check('作者', '开发工程师彭飞' in e)
    check('时长', '31.2 秒' in e)
    # 五个动作必须都在
    for kw in ['待机', '攻击', '死亡', '受击', '奔跑']:
        check('动作「%s」' % kw, kw in e)
    # 关键界面文案
    for kw in ['提示词 + 动画模板', 'AI 创作空间', '形象已选定', '从创意到动画']:
        check('界面文案「%s」' % kw, kw in e)
    # 版权：引用完整提示词原文不超过 50 词（此处中文按字符估算）
    for q in re.findall(r'<code>(.*?)</code>', e):
        check('引用片段 ≤50 字（%d）' % len(q), len(q) <= 50)

imgs = set(re.findall(r'src="(assets/[^"]+)"', after))
missing = [x for x in imgs if not os.path.isfile(x)]
check('图片引用 %d 个，0 缺失' % len(imgs), not missing, '缺失: %s' % missing[:5])

for tag in ['article', 'section', 'div', 'p', 'header', 'main', 'nav']:
    o = len(re.findall(r'<%s[\s>]' % tag, after))
    c = after.count('</%s>' % tag)
    check('<%s> 配对' % tag, o == c, 'open=%d close=%d' % (o, c))

check('文件尾未被破坏', before[-400:] == after[-400:],
      '尾部不一致')

print()
print('条目数=%d  nav=%d  图片引用=%d' % (na, len(va), len(imgs)))
print('本地字节=%d' % len(after.encode('utf-8')))
print()
if fails:
    print('FAILED: %s' % fails); sys.exit(1)
print('ALL CHECKS PASSED')
