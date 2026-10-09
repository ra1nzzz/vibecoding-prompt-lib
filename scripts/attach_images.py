#!/usr/bin/env python3
"""给 index.html 里所有没有配图的卡片挂上截图。

图片来源（按优先级）：
  1. curated/<entry-N>/img*.jpg —— Muse 时代精选截图（caption 来自 entry.md）
  2. assets 里已抽但未被引用的帧 —— extract_frames.py 生成的
  3. <vid>/shots/s*.jpg —— 从视频抽的关键帧
挂图时跳过该 entry 已引用的序号，保证一张图只用一次。
"""
import os
import re
import shutil
import sys
import json

LIB = os.path.expanduser('~/workspace/research_notes/vibecoding-prompt-lib/xigua')
PROJ = os.path.expanduser('~/workspace/promptlib')
ASSETS = os.path.join(PROJ, 'assets')
HTML = os.path.join(PROJ, 'index.html')
EMAP = json.load(open(os.path.join(LIB, 'curated_entry_map.json'), encoding='utf-8'))
VID = {v: k for k, v in EMAP.items()}   # entry_no -> vid


def parse_entry_md(n):
    p = os.path.join(LIB, 'curated', 'entry-%d' % n, 'entry.md')
    if not os.path.exists(p):
        return {}
    return {m.group(1): m.group(2).strip()
            for m in re.finditer(r'^(img\d+\.jpg)：(.+)$', open(p, encoding='utf-8').read(), re.M)}


def split_cards(block):
    out, i = [], 0
    while True:
        s = block.find('<section class="card', i)
        if s < 0:
            break
        depth = 0
        for m in re.finditer(r'<section\b|</section>', block[s:]):
            depth += -1 if m.group(0).startswith('</') else 1
            if depth == 0:
                i = s + m.end()
                out.append(block[s:i])
                break
        else:
            break
    return out


def pool_for(n):
    """该 entry 可用图片列表 -> [(assets 文件名, caption)]"""
    caps = parse_entry_md(n)
    out = []
    cd = os.path.join(LIB, 'curated', 'entry-%d' % n)
    if os.path.isdir(cd):
        for f in sorted(os.listdir(cd)):
            m = re.match(r'img(\d+)\.jpg$', f)
            if m:
                out.append(('xigua-%d-%s.jpg' % (n, m.group(1)), caps.get(f, '')))
    for f in sorted(os.listdir(ASSETS)):
        if re.match(r'xigua-%d-\d+\.jpg$' % n, f) and not any(x[0] == f for x in out):
            out.append((f, ''))
    sd = os.path.join(LIB, VID[n], 'shots') if n in VID else None
    if sd and os.path.isdir(sd):
        for f in sorted(os.listdir(sd)):
            if re.match(r's\d+\.jpg$', f):
                out.append(('xigua-%d-%s' % (n, f), ''))
    return out


def ensure_asset(name, n):
    dst = os.path.join(ASSETS, name)
    if os.path.exists(dst):
        return True
    m = re.match(r'xigua-%d-img(\d+)\.jpg$' % n, name)
    if m:
        src = os.path.join(LIB, 'curated', 'entry-%d' % n, 'img%s.jpg' % m.group(1))
    else:
        m = re.match(r'xigua-%d-(s\d+)\.jpg$' % n, name)
        src = os.path.join(LIB, VID[n], 'shots', m.group(1) + '.jpg') if (m and n in VID) else None
    if not src or not os.path.exists(src):
        return False
    shutil.copy2(src, dst)
    return True


def inject_visual(card, img, caption, num):
    note = caption or ''
    visual = ('<div class="visual"><img loading="lazy" decoding="async" '
              'src="assets/%s" alt="%s"><span class="num">%02d</span>'
              '<p class="image-note">%s</p></div>' % (img, note, num, note))
    m = re.search(r'<div class="content">', card)
    if not m:
        return None
    new = card[:m.start()] + visual + card[m.start():]
    return new.replace('<section class="card card--no-visual">',
                       '<section class="card card--portrait">', 1)


def main():
    dry = '--dry' in sys.argv
    html = open(HTML, encoding='utf-8').read()
    head = html[:html.index('<main>') + 6]
    tail = html[html.index('</main>'):]
    body = html[html.index('<main>') + 6:html.index('</main>')]
    blocks = re.findall(r'<article class="entry" id="entry-\d+">.*?</article>', body, re.S)

    filled = 0
    skipped = []
    for b in blocks:
        n = int(re.search(r'id="entry-(\d+)"', b).group(1))
        cards = split_cards(b)
        used = set(re.findall(r'src="assets/xigua-%d-([^"]+)\.jpg"' % n, b))
        pool = [(img, cap) for img, cap in pool_for(n)
                if re.match(r'xigua-%d-([^"]+)\.jpg$' % n, img).group(1) not in used]
        if not any('class="visual"' not in c for c in cards):
            continue
        new_cards = []
        pi = 0
        for c in cards:
            if 'class="visual"' in c:
                new_cards.append(c)
                continue
            while pi < len(pool) and not (dry or os.path.exists(os.path.join(ASSETS, pool[pi][0]))
                                          or ensure_asset(pool[pi][0], n)):
                pi += 1
            if pi >= len(pool):
                new_cards.append(c)
                continue
            img, cap = pool[pi]
            nc = inject_visual(c, img, cap, pi + 1)
            if nc is None:
                new_cards.append(c)
                continue
            new_cards.append(nc)
            filled += 1
            pi += 1
        rebuilt = b
        for old, new in zip(cards, new_cards):
            rebuilt = rebuilt.replace(old, new, 1)
        body = body.replace(b, rebuilt, 1)
        still = sum(1 for c in new_cards if 'class="visual"' not in c)
        if still:
            skipped.append((n, still))

    if not dry:
        with open(HTML, 'w', encoding='utf-8') as f:
            f.write(head + body + tail)
    print('挂图 %d 张' % filled)
    if skipped:
        print('仍缺图卡片（%d 张）:' % sum(s for _, s in skipped))
        for n, s in skipped:
            print('  entry-%-3d 缺 %d' % (n, s))


if __name__ == '__main__':
    main()
