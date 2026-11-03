#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批次17校验：entry-141 注入"""
import io, re, os, sys

before = io.open('/tmp/index.before-batch17.html', encoding='utf-8').read()
after = io.open('index.html', encoding='utf-8').read()
fails = []

def check(name, cond, extra=''):
    print(('PASS  ' if cond else 'FAIL  ') + name + (' :: ' + extra if extra else ''))
    if not cond:
        fails.append(name)

nb = len(re.findall(r'<article class="entry" id="entry-\d+">', before))
na = len(re.findall(r'<article class="entry" id="entry-\d+">', after))
check('条目数 138→139', nb == 138 and na == 139, '%d→%d' % (nb, na))

def nav_ids(s):
    i = s.find('<div class="library-nav-list"')
    j = s.find('</nav>', i)
    return re.findall(r'href="#entry-(\d+)"', s[i:j])
vb, va = nav_ids(before), nav_ids(after)
check('nav 138→139', len(vb) == 138 and len(va) == 139, '%d→%d' % (len(vb), len(va)))
kept = [x for x in va if x != '141']
check('nav 原顺序保留', kept == vb)
i140 = va.index('140')
check('entry-141 紧邻 entry-140 之后', va[i140 + 1] == '141', '实际: %s' % va[i140 + 1:i140 + 3])

arts = set(re.findall(r'<article class="entry" id="entry-(\d+)"', after))
check('nav 与 article 完全一致', set(va) == arts,
      '仅 nav: %s / 仅 art: %s' % (set(va) - arts, arts - set(va)))

check('目录计数 139（2处）', after.count('目录 · 139') == 2, str(after.count('目录 · 139')))
check('tab 副标题 139 条', '139 条 · 西瓜同学 / Xuan子等' in after)

def entry_pos(s):
    return {m.group(1): s.find('<article class="entry" id="%s">' % m.group(1))
            for m in re.finditer(r'<article class="entry" id="entry-(\d+)">', s)}
pb, pa = entry_pos(before), entry_pos(after)
moved = [k for k in pb if pb[k] != pa.get(k)]
check('旧条目 DOM 位置未变', not moved, '被移动: %s' % moved)
check('新增条目仅 entry-141', set(pa) - set(pb) == {'141'}, '意外: %s' % (set(pa) - set(pb)))

m = re.search(r'<article class="entry" id="entry-141">(.*?)</article>', after, re.S)
check('entry-141 存在', m is not None)
if m:
    e = m.group(1)
    check('7 张卡', e.count('<section class="card card--portrait">') == 7)
    check('7 个 prompt-box', e.count('class="prompt-box"') == 7)
    check('7 个 transcript', e.count('class="transcript"') == 7)
    check('1 个 outro', e.count('class="outro"') == 1)
    check('引 7 张新图', len(set(re.findall(r'assets/xiaobai-141-(\d+)\.jpg', e))) == 7)
    check('源链接', '7703746638380125466' in e)
    check('编号 01-07', all('>0%d<' % i in e for i in range(1, 8)))
    check('项目名 dsh-superagent', 'dsh-superagent' in e)
    check('研究原型声明', '研究原型' in e)
    # 三组实测数据必须都在
    for kw in ['30% 的判断', '30% 的 token', '2.5 秒', '3.9 秒', '6.4 秒', '1.6 秒']:
        check('实测数据「%s」' % kw, kw in e)
    # 四大特点
    for kw in ['连续', '主动', '高效', '持久']:
        check('特点「%s」' % kw, kw in e)

imgs = set(re.findall(r'src="(assets/[^"]+)"', after))
missing = [x for x in imgs if not os.path.isfile(x)]
check('图片引用 %d 个，0 缺失' % len(imgs), not missing, '缺失: %s' % missing[:5])

for tag in ['article', 'section', 'div', 'p', 'header', 'main', 'nav']:
    o = len(re.findall(r'<%s[\s>]' % tag, after))
    c = after.count('</%s>' % tag)
    check('<%s> 配对' % tag, o == c, 'open=%d close=%d' % (o, c))

b_tail = before[before.rfind('</article>\n</main>'):]
a_tail = after[after.rfind('</article>\n</main>'):]
check('文件尾未被破坏', b_tail[:200] == a_tail[:200])

print()
print('条目数=%d  nav=%d  图片引用=%d' % (na, len(va), len(imgs)))
print('本地字节=%d' % len(after.encode('utf-8')))
print()
if fails:
    print('FAILED: %s' % fails); sys.exit(1)
print('ALL CHECKS PASSED')
