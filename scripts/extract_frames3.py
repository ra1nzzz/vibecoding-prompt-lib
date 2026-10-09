#!/usr/bin/env python3
"""给 entry-43/45/46 缺图卡片抽帧（卡片文字从 index.html 读，非 content_batch*）。"""
import json
import os
import re
import subprocess
import hashlib
import difflib

MP4DIR = os.path.expanduser('~/workspace/tmp/xigua_dl')
PROJ = os.path.expanduser('~/workspace/promptlib')
HTML = os.path.join(PROJ, 'index.html')
ASSETS = os.path.join(PROJ, 'assets')
RAWDIR = os.path.expanduser('~/workspace/tmp/xigua_tr')

TARGET = {43: '7692599938034781450', 45: '7693653387555949851', 46: '7691200092186955035'}


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


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


def norm(s):
    return re.sub(r'[\s，。、；：？！,.;:?!""\']+', '', s or '')


def score_seg(card, seg):
    t, st = norm(card), norm(seg['t'])
    if not t or not st:
        return 0.0
    r = difflib.SequenceMatcher(None, t, st).ratio()
    if st in t:
        r = max(r, 0.85)
    return r


def pick_span(segs, card, taken):
    best, bs = None, 0.0
    for s in segs:
        if any(a - 0.5 < s['s'] and s['e'] < b + 0.5 for a, b in taken):
            continue
        sc = score_seg(card, s)
        if sc > bs:
            best, bs = s, sc
    if best is None or bs < 0.25:
        return None, None
    return best['s'] + (best['e'] - best['s']) * 0.45, (best['s'], best['e'])


def grab(vid, t, out):
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', '%.2f' % t,
                    '-i', os.path.join(MP4DIR, vid + '.mp4'),
                    '-frames:v', '1', '-q:v', '2', out], check=True)
    return os.path.exists(out) and os.path.getsize(out) > 8000


def main():
    dry = '--dry' in sys.argv if (sys := __import__('sys')) else False
    html = open(HTML, encoding='utf-8').read()
    body = html[html.index('<main>'):html.index('</main>')]
    made = 0
    for n, vid in TARGET.items():
        b = re.search(r'<article class="entry" id="entry-%d">.*?</article>' % n, body, re.S).group(0)
        cards = split_cards(b)
        segs = json.load(open(os.path.join(RAWDIR, vid + '.json'), encoding='utf-8'))
        dur = segs[-1]['e'] if segs else 0
        used_md5 = set(md5(os.path.join(ASSETS, f)) for f in os.listdir(ASSETS)
                       if re.match(r'xigua-%d-\d+\.jpg$' % n, f))
        taken = []
        got = 0
        for ci, c in enumerate(cards):
            if 'class="visual"' in c:
                continue
            # 卡片文字：transcript > process > selling > h3
            m = (re.search(r'<p class="transcript">([^<]*)', c)
                 or re.search(r'<p class="process"><strong>怎么做的：</strong>([^<]*)', c)
                 or re.search(r'<p class="selling">([^<]*)', c))
            card = m.group(1) if m else (re.search(r'<h3>([^<]*)', c).group(1) if re.search(r'<h3>([^<]*)', c) else '')
            t, span = pick_span(segs, card, taken)
            if t is None:
                step = dur / (len(cards) + 1)
                t = step * (got + 1)
                span = (t - 2, t + 2)
            t = min(max(t, 0.5), max(dur - 0.5, 0.5))
            idx = 1 + got
            out = os.path.join(ASSETS, 'xigua-%d-%d.jpg' % (n, idx))
            placed = False
            for tt in [t, t + 3, t - 3, t + 7, t - 7, t + 15, t - 15, t + 25]:
                if tt < 0.3 or tt > dur - 0.3:
                    continue
                if dry:
                    print('entry-%-3d card%d -> xigua-%d-%d.jpg @%.1fs (dry) [%s]' % (
                        n, ci + 1, n, idx, tt, card[:20]))
                    placed = True
                    break
                if grab(vid, tt, out) and md5(out) not in used_md5:
                    used_md5.add(md5(out))
                    taken.append(span)
                    print('entry-%-3d card%d -> %s @%.1fs  [%s]' % (
                        n, ci + 1, os.path.basename(out), tt, card[:20]))
                    placed = True
                    break
            if placed:
                got += 1
                made += 1
            else:
                print('entry-%-3d card%d FAILED' % (n, ci + 1))
    print('\n抽帧: %d 张' % made)


if __name__ == '__main__':
    main()
