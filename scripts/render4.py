#!/usr/bin/env python3
"""把第四批重写内容注入当前线上 index.html（前两批 + 全部补图之上）。

基准：~/workspace/promptlib/index.html（git 当前版本，含第一批+第二批+补图）
输出：~/workspace/promptlib/index.html（原地覆盖，git 负责版本管理）

不碰 build.py / render.py（它们的基准是 Muse 备份，会覆盖已有成果）。
"""
import os
import re
import sys
import html

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

BASE = os.path.join(os.path.dirname(HERE), 'index.html')


def esc(s):
    return html.escape(s, quote=False)


def render_card(c, idx, with_visual):
    parts = []
    cls = 'card card--portrait' if with_visual else 'card card--no-visual'
    parts.append('<section class="%s">' % cls)
    if with_visual and c.get('img'):
        note = c.get('img_note', '')
        parts.append(
            '<div class="visual"><img loading="lazy" decoding="async" '
            'src="assets/%s" alt="%s"><span class="num">%02d</span>'
            '<p class="image-note">%s</p></div>' % (
                esc(c['img']), esc(note), idx, esc(note))
        )
    parts.append('<div class="content"><h3>%s</h3><p class="en">%s</p>' % (esc(c['title']), esc(c.get('en', ''))))
    if c.get('selling'):
        parts.append('<p class="selling">%s</p>' % esc(c['selling']))
    if c.get('process'):
        parts.append('<p class="process"><strong>怎么做的：</strong>%s</p>' % esc(c['process']))
    if c.get('transcript'):
        parts.append('<p class="transcript">%s</p>' % esc(c['transcript']))
    parts.append('<div class="prompt-label">AI 描述词</div>')
    parts.append('<div class="prompt-box"><p>%s</p><button class="copy" type="button">复制</button></div>' % esc(c['prompt']))
    parts.append('</div></section>')
    return '\n    '.join(parts)


def render_entry(num, data, meta):
    cards = [render_card(c, i, bool(c.get('img'))) for i, c in enumerate(data['cards'], 1)]
    art = []
    art.append('<article class="entry" id="entry-%d">' % num)
    art.append('  <header class="entry-head"><div><h2>%s</h2><div class="meta">'
               '<span>%s</span><time datetime="%s">%s</time><span>约 %.1f 秒</span>'
               '</div></div><a class="source" href="%s" target="_blank" rel="noopener">'
               '查看原视频 <span aria-hidden="true">↗</span></a></header>' % (
                   esc(meta['title']), esc(meta.get('author', '西瓜同学🍉')),
                   meta.get('date', '2026-10-09'), meta.get('date', '2026-10-09'),
                   meta.get('duration', 0), esc(meta.get('url', '#'))))
    art.append('  <p class="intro">%s</p>' % esc(data['intro']))
    art.append('  <div class="cards">')
    art.extend('    ' + c for c in cards)
    art.append('  </div>')
    art.append('  <p class="outro">%s</p>' % esc(data['outro']))
    art.append('</article>')
    return '\n'.join(art)


def main():
    import content_batch4 as C
    from build import entry_no, entry_vid, entry_title, load_transcripts, load_entry_map, parse_curated, read_curated

    src = open(BASE, encoding='utf-8').read()
    before_len = len(src.encode('utf-8'))
    i, j = src.index('<main>'), src.index('</main>')
    head, body, tail = src[:i + 6], src[i + 6:j], src[j:]

    blocks = re.findall(r'<article class="entry" id="entry-\d+">.*?</article>', body, re.S)
    print('base: %s (%d bytes), %d entries' % (BASE, before_len, len(blocks)))

    tr_idx = load_transcripts()
    emap = load_entry_map()
    nums = [entry_no(b) for b in blocks]

    # 图片存在性校验
    missing_img = []
    for num, data in sorted(C.BATCH.items()):
        for c in data['cards']:
            if c.get('img') and not os.path.exists(os.path.join(os.path.dirname(HERE), 'assets', c['img'])):
                missing_img.append((num, c['img']))
    if missing_img:
        print('!! MISSING IMAGES: %s' % missing_img)
        sys.exit(1)

    replaced = []
    for num, data in sorted(C.BATCH.items()):
        if num not in nums:
            print('  SKIP entry-%d (not in page)' % num)
            continue
        b = blocks[nums.index(num)]
        vid = emap.get(num) or entry_vid(b)
        t = tr_idx.get(vid, {})
        meta = parse_curated(read_curated(num))
        meta.setdefault('title', entry_title(b))
        meta['duration'] = t.get('duration', meta.get('duration', 0))
        meta['url'] = meta.get('url') or ('https://www.douyin.com/video/%s' % vid)
        new = render_entry(num, data, meta)
        body = body.replace(b, new)
        replaced.append((num, vid, len(data['cards']), sum(1 for c in data['cards'] if c.get('img'))))

    out = head + body + tail
    with open(BASE, 'w', encoding='utf-8') as f:
        f.write(out)

    print('\nreplaced:')
    for num, vid, ncards, nimg in replaced:
        print('  entry-%-3d %s  %d cards / %d with image' % (num, vid, ncards, nimg))
    print('\nwrote index.html (%d -> %d bytes, +%d)' % (
        before_len, len(out.encode('utf-8')), len(out.encode('utf-8')) - before_len))


if __name__ == '__main__':
    main()
