#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批次16校验：entry-140 注入"""
import io, re, os, subprocess, sys

def read_before():
    p = '/tmp/index.before-batch16.html'
    if os.path.isfile(p):
        return io.open(p, encoding='utf-8').read()
    r = subprocess.run(['git', 'show', 'HEAD:index.html'], capture_output=True, cwd='.')
    if r.returncode == 0:
        return r.stdout.decode('utf-8')
    sys.exit('拿不到 before 基准')

before = read_before()
after = io.open('index.html', encoding='utf-8').read()
fails = []

def check(name, cond, extra=''):
    print(('PASS  ' if cond else 'FAIL  ') + name + (' :: ' + extra if extra else ''))
    if not cond:
        fails.append(name)

# 1. 条目 137 -> 138
nb = len(re.findall(r'<article class="entry" id="entry-\d+">', before))
na = len(re.findall(r'<article class="entry" id="entry-\d+">', after))
check('条目数 137→138', nb == 137 and na == 138, '%d→%d' % (nb, na))

# 2. nav
def nav_ids(s):
    i = s.find('<div class="library-nav-list"')
    j = s.find('</nav>', i)
    return re.findall(r'href="#entry-(\d+)"', s[i:j])
vb, va = nav_ids(before), nav_ids(after)
check('nav 137→138', len(vb) == 137 and len(va) == 138, '%d→%d' % (len(vb), len(va)))
check('nav 含 140', '140' in va)
kept = [x for x in va if x != '140']
check('nav 原顺序保留', kept == vb,
      '首个差异: %s' % next(('%s vs %s' % (x, y) for x, y in zip(vb, kept) if x != y), ''))
i139 = va.index('139')
check('entry-140 紧邻 entry-139 之后', va[i139 + 1] == '140', '实际: %s' % va[i139 + 1:i139 + 3])

# 3. nav 与 article 一一对应
arts = set(re.findall(r'<article class="entry" id="entry-(\d+)"', after))
check('nav 与 article 完全一致', set(va) == arts,
      '仅 nav 有: %s / 仅 article 有: %s' % (set(va) - arts, arts - set(va)))

# 4. 计数与副标题
check('目录计数 138（2处）', after.count('目录 · 138') == 2, str(after.count('目录 · 138')))
check('tab 副标题 138 条', '138 条 · 西瓜同学 / Xuan子等' in after)

# 5. 旧条目 DOM 位置未变；仅新增 140
def entry_pos(s):
    return {m.group(1): s.find('<article class="entry" id="%s">' % m.group(1))
            for m in re.finditer(r'<article class="entry" id="entry-(\d+)">', s)}
pb, pa = entry_pos(before), entry_pos(after)
moved = [k for k in pb if pb[k] != pa.get(k)]
check('旧条目 DOM 位置未变', not moved, '被移动: %s' % moved)
check('新增条目仅 entry-140', set(pa) - set(pb) == {'140'}, '意外: %s' % (set(pa) - set(pb)))

# 6. entry-140 内容
m = re.search(r'<article class="entry" id="entry-140">(.*?)</article>', after, re.S)
check('entry-140 存在', m is not None)
if m:
    e = m.group(1)
    check('entry-140 有 5 张卡', e.count('<section class="card card--portrait">') == 5)
    check('entry-140 5 个 prompt-box', e.count('class="prompt-box"') == 5)
    check('entry-140 5 个 transcript', e.count('class="transcript"') == 5)
    check('entry-140 5 个 outro', e.count('class="outro"') == 1)
    check('entry-140 引 5 张新图', len(set(re.findall(r'assets/xigua-140-(\d)\.jpg', e))) == 5)
    check('entry-140 源链接', '7702405821363227930' in e)
    check('entry-140 编号 01-05', all('>0%d<' % i in e for i in range(1, 6)))
    # 两组色值参数必须都在（02 和 05 的核心干货）
    for hexc in ['#090B0B', '#111514', '#EEF4EF', '#A5E87A', '#080808', '#151515', '#F7F7F4', '#D9F240']:
        check('色值 %s 在条目内' % hexc, hexc in e)

# 7. 图片文件真实存在
imgs = set(re.findall(r'src="(assets/[^"]+)"', after))
missing = [x for x in imgs if not os.path.isfile(x)]
check('图片引用 %d 个，0 缺失' % len(imgs), not missing, '缺失: %s' % missing[:5])

# 8. 标签配对
for tag in ['article', 'section', 'div', 'p', 'header', 'main', 'nav']:
    o = len(re.findall(r'<%s[\s>]' % tag, after))
    c = after.count('</%s>' % tag)
    check('<%s> 配对' % tag, o == c, 'open=%d close=%d' % (o, c))

# 9. 文件尾未被破坏
b_tail = before[before.rfind('</article>\n</main>'):]
a_tail = after[after.rfind('</article>\n</main>'):]
check('文件尾（footer/script）未被破坏', b_tail[:200] == a_tail[:200])

print()
print('条目数=%d  nav=%d  图片引用=%d' % (na, len(va), len(imgs)))
print('本地字节=%d' % len(after.encode('utf-8')))
print()
if fails:
    print('FAILED: %s' % fails); sys.exit(1)
print('ALL CHECKS PASSED')
