#!/usr/bin/env python3
"""把第一批重写内容注入现有 index.html 结构。

保留：全部 CSS、目录导航、页头页脚、配图资源、卡片 DOM 结构、复制按钮。
替换：entry-47..53 的 intro / cards 文字内容 / outro。
"""
import os
import re
import sys
import html

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

BACKUP = os.path.expanduser('~/workspace/research_notes/vibecoding-prompt-lib/published-site-backup/index.html')
DIST_DIR = os.path.join(HERE, 'dist')


def esc(s):
    return html.escape(s, quote=False)


def render_card(c, idx, with_visual):
    """渲染一个 card，DOM 结构与原站一致。"""
    parts = []
    cls = 'card'
    if with_visual:
        cls += ' card--portrait'
    else:
        cls += ' card--no-visual'
    parts.append('<section class="%s">' % cls)
    if with_visual and c.get('img'):
        parts.append(
            '<div class="visual"><img loading="lazy" decoding="async" '
            'src="assets/%s" alt="%s"><span class="num">%02d</span>'
            '<p class="image-note">%s</p></div>' % (
                esc(c['img']), esc(c.get('img_note', '')), idx, esc(c.get('img_note', '')))
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
    """渲染整条 entry。meta 提供标题/作者/链接/时长。"""
    cards = []
    # 有配图的卡片用 portrait，无配图用 no-visual，与原站节奏一致
    for i, c in enumerate(data['cards'], 1):
        cards.append(render_card(c, i, bool(c.get('img'))))
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
    import content_batch1 as C

    src = open(BACKUP, encoding='utf-8').read()
    i, j = src.index('<main>'), src.index('</main>')
    head, body, tail = src[:i + 6], src[i + 6:j], src[j:]

    blocks = re.findall(r'<article class="entry" id="entry-\d+">.*?</article>', body, re.S)
    print('found %d entries' % len(blocks))

    from build import entry_no, entry_vid, entry_title, load_transcripts, load_entry_map, parse_curated, read_curated

    tr_idx = load_transcripts()
    emap = load_entry_map()
    nums = [entry_no(b) for b in blocks]

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
        replaced.append((num, vid, len(data['cards'])))

    out = head + body + tail
    os.makedirs(DIST_DIR, exist_ok=True)
    with open(os.path.join(DIST_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(out)

    print('\nreplaced:')
    for num, vid, ncards in replaced:
        print('  entry-%-3d %s  %d cards' % (num, vid, ncards))
    print('\nwrote dist/index.html (%d bytes)' % len(out.encode('utf-8')))


if __name__ == '__main__':
    main()
