#!/usr/bin/env python3
"""列出所有可重写的条目（有完整转写的）。"""
import json
import os
import re

LIB = os.path.expanduser('~/workspace/research_notes/vibecoding-prompt-lib')
IDX = os.path.expanduser('~/workspace/tmp/xigua_tr/_full/_index.json')

h = open(os.path.join(LIB, 'published-site-backup/index.html'), encoding='utf-8').read()
arts = [(int(m.group(1)), m.group(0)) for m in
        re.finditer(r'<article class="entry" id="entry-(\d+)">.*?</article>', h, re.S)]
emap = json.load(open(os.path.join(LIB, 'xigua/curated_entry_map.json'), encoding='utf-8'))
rev = {v: k for k, v in emap.items()}
idx = json.load(open(IDX, encoding='utf-8'))

rows = []
for n, b in arts:
    vid = rev.get(n)
    if vid and vid in idx:
        m = re.search(r'<h2>(.*?)</h2>', b, re.S)
        t = m.group(1).strip() if m else '(no title)'
        rows.append((n, vid, t, idx[vid]['chars'], idx[vid]['duration']))
rows.sort()

print('可重写条目数: %d / %d' % (len(rows), len(arts)))
print()
print('%-6s %-20s %-6s %-7s %s' % ('entry', 'vid', 'chars', 'sec', 'title'))
for n, v, t, ch, du in rows:
    print('%-6d %-20s %-6d %-7.1f %s' % (n, v, ch, du, t))
