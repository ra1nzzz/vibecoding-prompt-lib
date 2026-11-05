#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批次18注入器：开发工程师彭飞「用 AI，把角色创意变成 Spine 动画」entry-142（7卡）

同时更新 4 处索引面：nav 链接、目录计数（2 处「目录 · N」）、tab 副标题「N 条」。
锚点用 </main>（不能用 '</article>\n</main>'，会吃掉最后一个 article 闭合标签）。
"""
import io, sys

sys.path.insert(0, 'scripts')
from content_batch18 import BATCH, TITLE

p = 'index.html'
s = io.open(p, encoding='utf-8').read()

# ---- 1. nav：entry-141 之后追加 entry-142 ----
NAV_ANCHOR = '<a href="#entry-141">Super-agent 是什么：DeepSeek 下一代 Agent 方案拆解</a>'
if s.count(NAV_ANCHOR) != 1:
    sys.exit('nav anchor 不唯一: %d' % s.count(NAV_ANCHOR))
if 'href="#entry-142"' in s:
    sys.exit('entry-142 已存在')
s = s.replace(NAV_ANCHOR, NAV_ANCHOR +
              '\n<a href="#entry-142">用 AI，把角色创意变成 Spine 动画</a>', 1)

# ---- 2. 目录计数 139 -> 140 ----
n = s.count('目录 · 139')
if n != 2:
    sys.exit('目录计数不是2处: %d' % n)
s = s.replace('目录 · 139', '目录 · 140')
s = s.replace('<i>139 条 · 西瓜同学 / Xuan子等</i>', '<i>140 条 · 西瓜同学 / Xuan子等</i>', 1)

# ---- 3. 条目注入 ----
TAIL = '</main>'
if s.count(TAIL) != 1:
    sys.exit('</main> 锚点不唯一: %d' % s.count(TAIL))

for eid, entry in BATCH.items():
    if 'id="%s"' % eid in s:
        sys.exit('%s 已存在' % eid)
    s = s.replace(TAIL, entry + '</main>', 1)

io.open(p, 'w', encoding='utf-8').write(s)
print('OK bytes=%d' % len(s.encode('utf-8')))
