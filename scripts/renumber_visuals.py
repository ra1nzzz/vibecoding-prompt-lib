#!/usr/bin/env python3
"""重排每条 entry 内卡片的 num 标号，并给缺 caption 的新帧补说明。

背景：attach_images 挂图时 num 用的是 pool 下标，导致同一 entry 内出现
01/02/05/01/02 这种重复跳跃的编号。本脚本：
  1. 按 DOM 出现顺序把 num 重新编成 01..N
  2. 新抽帧（无 caption）按卡片标题生成说明："<卡片标题>演示"
"""
import os
import re
import sys

PROJ = os.path.expanduser('~/workspace/promptlib')
HTML = os.path.join(PROJ, 'index.html')


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


def main():
    dry = '--dry' in sys.argv
    html = open(HTML, encoding='utf-8').read()
    head = html[:html.index('<main>') + 6]
    tail = html[html.index('</main>'):]
    body = html[html.index('<main>') + 6:html.index('</main>')]
    blocks = re.findall(r'<article class="entry" id="entry-\d+">.*?</article>', body, re.S)

    renum = 0
    capt = 0
    for b in blocks:
        cards = split_cards(b)
        new_cards = []
        vi = 0
        for c in cards:
            m = re.search(r'(<div class="visual"><img[^>]*src="assets/[^"]+"[^>]*><span class="num">)(\d+)(</span>\s*<p class="image-note">)([^<]*)(</p></div>)', c, re.S)
            if not m:
                new_cards.append(c)
                continue
            vi += 1
            img = re.search(r'src="assets/([^"]+)"', c).group(1)
            note = m.group(4).strip()
            if not note:
                # 用卡片 h3 标题生成说明
                t = re.search(r'<h3>([^<]*)</h3>', c)
                note = ('%s 演示' % t.group(1)) if t else ''
                capt += 1
            num = '%02d' % vi
            if num != m.group(2) or note != m.group(4):
                renum += 1
            new_cards.append(c[:m.start()] + m.group(1) + num + m.group(3) + note + m.group(5) + c[m.end():])
        rebuilt = b
        for old, new in zip(cards, new_cards):
            rebuilt = rebuilt.replace(old, new, 1)
        body = body.replace(b, rebuilt, 1)

    if not dry:
        with open(HTML, 'w', encoding='utf-8') as f:
            f.write(head + body + tail)
    print('重编号/补说明: %d 处（其中补 caption %d 处）' % (renum, capt))


if __name__ == '__main__':
    main()
