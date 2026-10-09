#!/usr/bin/env python3
"""从本地 mp4 按转写时间轴抽帧，补足缺图卡片。

做法：
  1. 从 index.html 解析每个 entry 里"没有 visual"的卡片序号
  2. 用该卡片自己的文字（transcript/process）与转写分段做相似度匹配
  3. 在命中段内 45% 处抽帧；同一 entry 内已分配的时段不再复用
  4. 用 MD5 去重（避免与已有截图、同批新帧重复）
"""
import json
import os
import re
import subprocess
import sys
import hashlib
import difflib

LIB = os.path.expanduser('~/workspace/research_notes/vibecoding-prompt-lib/xigua')
TRANS = os.path.expanduser('~/workspace/tmp/xigua_tr/_full')
RAWDIR = os.path.expanduser('~/workspace/tmp/xigua_tr')
MP4DIR = os.path.expanduser('~/workspace/tmp/xigua_dl')
PROJ = os.path.expanduser('~/workspace/promptlib')
HTML = os.path.join(PROJ, 'index.html')
ASSETS = os.path.join(PROJ, 'assets')
EMAP = json.load(open(os.path.join(LIB, 'curated_entry_map.json'), encoding='utf-8'))  # vid -> entry_no
INV = {v: k for k, v in EMAP.items()}   # entry_no -> vid

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content_batch1 as B1
import content_batch2 as B2

CARDTEXT = {}
for mod in (B1, B2):
    for num, data in mod.BATCH.items():
        CARDTEXT[num] = [c.get('transcript') or c.get('process') or c.get('selling') or '' for c in data['cards']]


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


def norm(s):
    return re.sub(r'[\s，。、；：？！,.;:?!""\']+', '', s or '')


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


def no_image_cards(block):
    """返回缺图卡片的 0-based 序号列表。"""
    return [i for i, c in enumerate(split_cards(block)) if 'class="visual"' not in c]


def score_seg(card, seg):
    t, st = norm(card), norm(seg['t'])
    if not t or not st:
        return 0.0
    r = difflib.SequenceMatcher(None, t, st).ratio()
    if st in t:
        r = max(r, 0.85)
    if len(st) <= 6 and r < 0.8:
        return 0.0
    return r


def pick_span(segs, card, taken):
    best, bs = None, 0.0
    for s in segs:
        if any(a - 0.5 < s['s'] and s['e'] < b + 0.5 for a, b in taken):
            continue
        sc = score_seg(card, s)
        if sc > bs:
            best, bs = s, sc
    if best is None or bs < 0.3:
        return None, None
    return best['s'] + (best['e'] - best['s']) * 0.45, (best['s'], best['e'])


def grab(vid, t, out):
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', '%.2f' % t,
                    '-i', os.path.join(MP4DIR, vid + '.mp4'),
                    '-frames:v', '1', '-q:v', '2', out], check=True)
    return os.path.exists(out) and os.path.getsize(out) > 8000


def main():
    dry = '--dry' in sys.argv
    html = open(HTML, encoding='utf-8').read()
    body = html[html.index('<main>'):html.index('</main>')]
    blocks = re.findall(r'<article class="entry" id="entry-\d+">.*?</article>', body, re.S)

    plan = []   # (entry_no, [card_idx,...], vid)
    for b in blocks:
        n = int(re.search(r'id="entry-(\d+)"', b).group(1))
        miss = no_image_cards(b)
        if not miss:
            continue
        vid = INV.get(n)
        if vid and os.path.exists(os.path.join(MP4DIR, vid + '.mp4')) \
                and os.path.exists(os.path.join(RAWDIR, vid + '.json')):
            plan.append((n, miss, vid))
        else:
            print('entry-%-3d 跳过（无本地 mp4/转写）缺 %d 卡' % (n, len(miss)))

    total = 0
    for n, miss, vid in plan:
        segs = json.load(open(os.path.join(RAWDIR, vid + '.json'), encoding='utf-8'))
        dur = float(json.load(open(os.path.join(TRANS, vid + '.json'), encoding='utf-8')).get('duration')
                    or (segs[-1]['e'] if segs else 0))
        texts = CARDTEXT.get(n, [])
        used_md5 = set(md5(os.path.join(ASSETS, f)) for f in os.listdir(ASSETS)
                       if re.match(r'xigua-%d-\d+\.jpg$' % n, f))
        nshots = 0
        sd = os.path.join(LIB, vid, 'shots')
        if os.path.isdir(sd):
            nshots = len([f for f in os.listdir(sd) if f.endswith('.jpg')])
        taken = []
        got = 0
        for ci in miss:
            card = texts[ci] if ci < len(texts) else ''
            t, span = pick_span(segs, card, taken)
            if t is None:
                # 兜底：整条时间轴均匀找还没占的点
                step = dur / (len(miss) + 1)
                t = step * (got + 1)
                span = (t - 1.5, t + 1.5)
            t = min(max(t, 0.5), max(dur - 0.5, 0.5))
            idx = nshots + 1 + got
            out = os.path.join(ASSETS, 'xigua-%d-%d.jpg' % (n, idx))
            placed = False
            for tt in [t, t + 2.5, t - 2.5, t + 6, t - 6, t + 12, t - 12, t + 20, t - 20]:
                if tt < 0.3 or tt > dur - 0.3:
                    continue
                if dry:
                    print('entry-%-3d card%-2d -> xigua-%d-%d.jpg @%.1fs (dry)  [%s]' % (
                        n, ci + 1, n, idx, tt, card[:16]))
                    placed = True
                    break
                if grab(vid, tt, out) and md5(out) not in used_md5:
                    used_md5.add(md5(out))
                    taken.append(span)
                    print('entry-%-3d card%-2d -> %s @%.1fs  [%s]' % (
                        n, ci + 1, os.path.basename(out), tt, card[:16]))
                    placed = True
                    break
            if placed:
                got += 1
                total += 1
            else:
                print('entry-%-3d card%-2d FAILED' % (n, ci + 1))
    print('\n抽帧: %d 张' % total)


if __name__ == '__main__':
    main()
