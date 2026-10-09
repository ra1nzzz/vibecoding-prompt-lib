#!/usr/bin/env python3
"""promptlib 构建脚本：从完整转写 + 截图为每个条目生成内容。

设计原则（用户确认）:
  - 保留现有视觉和 DOM 结构（单页 index.html，红色高亮、目录抽屉、复制按钮）
  - 只把文字内容换成基于完整转写重写的版本
  - 分批处理：BATCH 列表决定本批重写哪些 entry

用法:
  python3 build.py            # 处理 BATCH 里的条目，输出到 dist/index.html
  python3 build.py --status   # 只打印进度
"""
import json
import os
import re
import sys
import html

ROOT = os.path.dirname(os.path.abspath(__file__))
BACKUP = os.path.expanduser('~/workspace/research_notes/vibecoding-prompt-lib/published-site-backup')
TRANS = os.path.expanduser('~/workspace/tmp/xigua_tr/_full')
EMAP = os.path.expanduser('~/workspace/research_notes/vibecoding-prompt-lib/xigua/curated_entry_map.json')
CURATED = os.path.expanduser('~/workspace/research_notes/vibecoding-prompt-lib/xigua/curated')
DIST = os.path.join(ROOT, 'dist')

# ---------------------------------------------------------------- 本批清单
# entry 号 -> 处理状态。None=沿用旧内容, dict=用此数据替换
BATCH = list(range(47, 54))   # entry-47 .. entry-53（7 个，均有完整转写）


def load_transcripts():
    idx = {}
    p = os.path.join(TRANS, '_index.json')
    if os.path.exists(p):
        idx = json.load(open(p, encoding='utf-8'))
    return idx


def load_entry_map():
    m = json.load(open(EMAP, encoding='utf-8'))
    return {v: k for k, v in m.items()}   # entry_no -> video_id


def read_transcript(vid):
    p = os.path.join(TRANS, vid + '.json')
    if not os.path.exists(p):
        return None
    return json.load(open(p, encoding='utf-8'))


def read_curated(entry_no):
    p = os.path.join(CURATED, 'entry-%d' % entry_no, 'entry.md')
    if not os.path.exists(p):
        return None
    return open(p, encoding='utf-8').read()


def parse_curated(md):
    """从 Muse 的 entry.md 里抽标题/作者/链接/时长/配图说明，用于保留元信息。"""
    if not md:
        return {}
    out = {}
    m = re.search(r'^#\s*(.+)$', md, re.M)
    if m:
        out['title'] = m.group(1).split('｜', 1)[-1].strip()
    m = re.search(r'原链接：(\S+)', md)
    if m:
        out['url'] = m.group(1)
    m = re.search(r'时长：([\d.]+)s', md)
    if m:
        out['duration'] = float(m.group(1))
    m = re.search(r'作者：(.+)', md)
    if m:
        out['author'] = m.group(1).strip()
    # 配图说明
    imgs = {}
    for m in re.finditer(r'^(img\d+\.jpg)：(.+)$', md, re.M):
        imgs[m.group(1)] = m.group(2).strip()
    out['imgs'] = imgs
    return out


def read_timed(vid):
    """读带时间戳的 txt，返回 [(s,e,text)]。"""
    p = os.path.join(TRANS, vid + '.txt')
    if not os.path.exists(p):
        return []
    out = []
    for line in open(p, encoding='utf-8'):
        m = re.match(r'\[(\d+\.\d+)-(\d+\.\d+)\]\s*(.+)$', line.strip())
        if m:
            out.append((float(m.group(1)), float(m.group(2)), m.group(3)))
    return out


def esc(s):
    return html.escape(s, quote=False)


def mmss(sec):
    m = int(sec // 60)
    s = sec - m * 60
    return '%d:%04.1f' % (m, s)


# ---------------------------------------------------------------- HTML 操作
def split_page(html_text):
    """返回 (head_including_body_open, [article blocks], tail)."""
    i = html_text.index('<main>')
    j = html_text.index('</main>')
    head = html_text[:i + len('<main>')]
    body = html_text[i + len('<main>'):j]
    tail = html_text[j:]
    blocks = re.findall(r'<article class="entry" id="entry-\d+">.*?</article>', body, re.S)
    return head, blocks, tail


def entry_no(block):
    return int(re.search(r'id="entry-(\d+)"', block).group(1))


def entry_title(block):
    return re.search(r'<h2>(.*?)</h2>', block, re.S).group(1).strip()


def entry_vid(block):
    m = re.search(r'douyin\.com/video/(\d+)', block)
    return m.group(1) if m else None


def main():
    status = '--status' in sys.argv
    src = os.path.join(BACKUP, 'index.html')
    html_text = open(src, encoding='utf-8').read()
    head, blocks, tail = split_page(html_text)

    tr_idx = load_transcripts()
    emap = load_entry_map()

    done, pending, missing = [], [], []
    for b in blocks:
        n = entry_no(b)
        vid = emap.get(n) or entry_vid(b)
        if vid and vid in tr_idx:
            done.append(n)
        else:
            missing.append(n)

    if status:
        print('total entries: %d' % len(blocks))
        print('with full transcript: %d' % len(done))
        print('without transcript: %d' % len(missing))
        print('this batch: %s' % BATCH)
        for n in BATCH:
            vid = emap.get(n) or entry_vid(blocks[[entry_no(x) for x in blocks].index(n)])
            t = tr_idx.get(vid, {})
            print('  entry-%-3d %s  %5.1fs  %4d chars' % (
                n, vid, t.get('duration', 0), t.get('chars', 0)))
        return

    os.makedirs(DIST, exist_ok=True)
    # 第一批：先原样拷贝，再逐条替换（保证未处理的条目零改动）
    report = []
    for n in BATCH:
        i = [entry_no(x) for x in blocks].index(n)
        b = blocks[i]
        vid = emap.get(n) or entry_vid(b)
        t = read_transcript(vid)
        if not t:
            report.append((n, vid, 'NO-TRANSCRIPT'))
            continue
        timed = read_timed(vid)
        meta = parse_curated(read_curated(n))
        report.append((n, vid, 'ready  %.1fs %d chars %d segs' % (
            t['duration'], t['chars'], len(timed))))

    for r in report:
        print(r)

    print('\n--- 本批素材已就绪，写内容生成器 ---')


if __name__ == '__main__':
    main()
