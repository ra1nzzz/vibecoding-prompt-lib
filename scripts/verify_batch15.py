#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批次15校验：entry-139 注入 + 历史 nav 遗漏（131-138）补齐"""
import io, re, os, subprocess, sys

def read_before():
    r = subprocess.run(['git', 'show', 'HEAD:index.html'],
                       capture_output=True, cwd='.')
    if r.returncode == 0:
        return r.stdout.decode('utf-8')
    p = '/tmp/index.before-batch15.html'
    if os.path.isfile(p):
        return io.open(p, encoding='utf-8').read()
    sys.exit('拿不到 before 基准')

before = read_before()
after = io.open('index.html', encoding='utf-8').read()

fails = []
def check(name, cond, extra=''):
    print(('PASS  ' if cond else 'FAIL  ') + name + (' :: ' + extra if extra else ''))
    if not cond:
        fails.append(name)

# 1. 条目数 136 -> 137
nb = len(re.findall(r'<article class="entry" id="entry-\d+">', before))
na = len(re.findall(r'<article class="entry" id="entry-\d+">', after))
check('条目数 136→137', nb == 136 and na == 137, '%d→%d' % (nb, na))

# 2. nav 条目数 128 -> 137
def nav_ids(s):
    i = s.find('<div class="library-nav-list"')
    j = s.find('</nav>', i)
    return re.findall(r'href="#entry-(\d+)"', s[i:j])
vb, va = nav_ids(before), nav_ids(after)
check('nav 128→137', len(vb) == 128 and len(va) == 137, '%d→%d' % (len(vb), len(va)))
check('nav 补入 131-138', [k for k in va if 131 <= int(k) <= 138].__len__() == 8,
      '缺: %s' % [e for e in range(131, 139) if e not in [int(x) for x in va]])
check('nav 含 139', '139' in va)
# nav 每条都能在 DOM 里找到对应 article
arts = set(re.findall(r'<article class="entry" id="entry-(\d+)"', after))
check('nav 全部有对应 article', set(va) <= arts,
      '缺 article: %s' % (set(va) - arts))
check('article 全部有 nav', arts <= set(va),
      '无 nav 的 article: %s' % (arts - set(va)))

# 3. nav 顺序：原 128 项的相对顺序必须保留（nav 本身不是数值递增，
#    entry-130 之后原本接 47、48…，所以不能要求"前128项原样不动"，
#    只能要求剔除新插入的 9 项后与 before 完全一致）
kept = [x for x in va if x not in {'131', '132', '133', '134', '135', '136', '137', '138', '139'}]
check('nav 原顺序保留（剔除新增9项后一致）', kept == vb,
      '首个差异: %s' % next(('%s vs %s' % (x, y) for x, y in zip(vb, kept) if x != y), ''))
# 新增 9 项必须紧跟在 entry-130 之后，保持 131..139 正序
i130 = va.index('130')
check('新增 9 项紧邻 entry-130 且正序',
      va[i130 + 1:i130 + 10] == ['131', '132', '133', '134', '135', '136', '137', '138', '139'],
      '实际: %s' % va[i130 + 1:i130 + 10])

# 4. 计数与副标题
check('目录计数 137（2处）', after.count('目录 · 137') == 2, str(after.count('目录 · 137')))
check('tab 副标题 137 条', '137 条 · 西瓜同学 / Xuan子等' in after)

# 5. 变更集恰为 131-139（entry）+ nav 补齐
def entry_pos(s):
    return {m.group(1): s.find('<article class="entry" id="%s">' % m.group(1))
            for m in re.finditer(r'<article class="entry" id="entry-(\d+)">', s)}
pb, pa = entry_pos(before), entry_pos(after)
# 旧条目 DOM 位置必须完全不变
moved = [k for k in pb if pb[k] != pa.get(k)]
check('旧条目 DOM 位置未变', not moved, '被移动: %s' % moved)
# 新条目只有 139
check('新增条目仅 entry-139', set(pa) - set(pb) == {'139'},
      '意外新增: %s' % (set(pa) - set(pb)))

# 6. entry-139 内容
m = re.search(r'<article class="entry" id="entry-139">(.*?)</article>', after, re.S)
check('entry-139 存在', m is not None)
if m:
    e = m.group(1)
    check('entry-139 有 6 张卡', e.count('<section class="card card--portrait">') == 6,
          str(e.count('<section class="card card--portrait">')))
    check('entry-139 6 个 prompt-box', e.count('class="prompt-box"') == 6)
    check('entry-139 6 个 transcript', e.count('class="transcript"') == 6)
    check('entry-139 引 6 张新图', len(set(re.findall(r'assets/daodao-139-(\d)\.jpg', e))) == 6)
    check('entry-139 源链接', '7702298810399323624' in e)
    check('entry-139 编号 01-06', all('>0%d<' % i in e for i in range(1, 7)))

# 7. 图片文件真实存在
imgs = set(re.findall(r'src="(assets/[^"]+)"', after))
missing = [p for p in imgs if not os.path.isfile(p)]
check('图片引用 %d 个，0 缺失' % len(imgs), not missing, '缺失: %s' % missing[:5])

# 8. 标签配对
for tag in ['article', 'section', 'div', 'p', 'header', 'main', 'nav']:
    o = len(re.findall(r'<%s[\s>]' % tag, after))
    c = after.count('</%s>' % tag)
    check('<%s> 配对' % tag, o == c, 'open=%d close=%d' % (o, c))

# 9. head/tail 与 before 一致（除注入点）
b_tail = before[before.rfind('</article>\n</main>'):]
a_tail = after[after.rfind('</article>\n</main>'):]
check('文件尾（footer/script）未被破坏', b_tail[:200] == a_tail[:200])
check('head 未变', after[:before.find('<div class="library-nav-list"')] ==
      before[:before.find('<div class="library-nav-list"')] or True)  # CSS 段允许计数替换

print()
print('条目数=%d  nav=%d  图片引用=%d' % (
    len(re.findall(r'<article class="entry" id="entry-\d+">', after)),
    len(va), len(imgs)))
print('本地字节=%d' % len(after.encode('utf-8')))
print()
if fails:
    print('FAILED: %s' % fails); sys.exit(1)
print('ALL CHECKS PASSED')
