#!/usr/bin/env python3
"""补全被 Muse 删掉的截图。

背景：Muse 为压 artifact.share 的 500 文件上限，按 drop-list.json 每个 entry
删了 1 张图（共 81 张）。原始截图仍完整保存在 xigua/curated/<entry>/imgN.jpg。

本脚本：
  1. 把 curated 里的图按 assets 命名规范 (xigua-<entry>-<n>.jpg) 拷入 assets
  2. 从 entry.md 的「配图说明」读出每张图的 caption
  3. 对每个 entry，找出 HTML 里没有配图的卡片，按图片序号顺序挂上去
  4. 输出补全报告
"""
import os
import re
import shutil
import json
import sys

LIB = os.path.expanduser('~/workspace/research_notes/vibecoding-prompt-lib')
CURATED = os.path.join(LIB, 'xigua/curated')
PROJ = os.path.expanduser('~/workspace/promptlib')
ASSETS = os.path.join(PROJ, 'assets')
HTML = os.path.join(PROJ, 'index.html')


def parse_entry_md(n):
    """返回 {imgN.jpg: caption}"""
    p = os.path.join(CURATED, 'entry-%d' % n, 'entry.md')
    if not os.path.exists(p):
        return {}
    out = {}
    for m in re.finditer(r'^(img\d+\.jpg)：(.+)$', open(p, encoding='utf-8').read(), re.M):
        out[m.group(1)] = m.group(2).strip()
    return out


def main():
    dry = '--dry' in sys.argv
    html = open(HTML, encoding='utf-8').read()

    # ---- 1. 收集所有可用图片
    added, existed = [], []
    for d in sorted(os.listdir(CURATED)):
        m = re.match(r'entry-(\d+)$', d)
        if not m:
            continue
        n = int(m.group(1))
        for f in sorted(os.listdir(os.path.join(CURATED, d))):
            if not f.endswith('.jpg'):
                continue
            idx = int(re.match(r'img(\d+)\.jpg', f).group(1))
            dst_name = 'xigua-%d-%d.jpg' % (n, idx)
            dst = os.path.join(ASSETS, dst_name)
            if os.path.exists(dst):
                existed.append(dst_name)
                continue
            if not dry:
                shutil.copy2(os.path.join(CURATED, d, f), dst)
            added.append(dst_name)

    print('assets 已存在: %d' % len(existed))
    print('本次补入 assets: %d' % len(added))
    if added:
        print('  ', ', '.join(sorted(added)[:12]), '...' if len(added) > 12 else '')

    # ---- 2. 找出 HTML 里缺配图的卡片并挂图
    report = []
    arts = [(m.group(1), int(m.group(2))) for m in
            re.finditer(r'(<article class="entry" id="entry-(\d+)">.*?</article>)', html, re.S)]

    # 反向构造：entry -> 已被引用的图序号
    used = {}
    for blk, n in arts:
        used[n] = set(int(x) for x in re.findall(r'src="assets/xigua-%d-(\d+)\.jpg"' % n, blk))

    # 每个 entry 可用图序号
    avail = {}
    caps = {}
    for d in sorted(os.listdir(CURATED)):
        m = re.match(r'entry-(\d+)$', d)
        if not m:
            continue
        n = int(m.group(1))
        idxs = sorted(int(re.match(r'img(\d+)\.jpg', f).group(1))
                      for f in os.listdir(os.path.join(CURATED, d)) if f.endswith('.jpg'))
        avail[n] = idxs
        caps[n] = parse_entry_md(n)

    total_attached = 0
    for block, n in arts:
        missing = [i for i in avail.get(n, []) if i not in used.get(n, set())]
        if not missing:
            continue
        # 找出没有 visual 的卡片，按出现顺序
        card_re = re.compile(r'<section class="card card--no-visual">.*?</section>', re.S)
        empty = card_re.findall(block)
        if not empty:
            report.append((n, missing, 'no empty card'))
            continue
        new_block = block
        attached = 0
        for img_idx in missing:
            if attached >= len(empty):
                break
            target = empty[attached]
            cap = caps.get(n, {}).get('img%d.jpg' % img_idx, '')
            fname = 'xigua-%d-%d.jpg' % (n, img_idx)
            visual = (
                '<div class="visual"><img loading="lazy" decoding="async" '
                'src="assets/%s" alt="%s"><span class="num">%02d</span>'
                '<p class="image-note">%s</p></div>' % (fname, cap, img_idx, cap)
            )
            # card--no-visual -> card--portrait，并在 content 前插入 visual
            # 兼容 "<section class=\"card card--no-visual\"><div class=\"content\">"
            # 与中间带空白/换行的两种写法
            pat = re.compile(
                r'<section class="card card--no-visual">(\s*)<div class="content">')
            repl = '<section class="card card--portrait">' + visual + r'\1<div class="content">'
            new_target, cnt = pat.subn(repl, target, count=1)
            if cnt == 0:
                report.append((n, [img_idx], 'pattern mismatch'))
                continue
            new_block = new_block.replace(target, new_target, 1)
            attached += 1
            total_attached += 1
        html = html.replace(block, new_block, 1)
        report.append((n, missing[:attached], 'attached %d' % attached))

    if not dry:
        open(HTML, 'w', encoding='utf-8').write(html)

    print('\n挂图明细:')
    for n, miss, st in report:
        print('  entry-%-4d missing=%-12s %s' % (n, miss, st))
    print('\n共挂上 %d 张图到原本无配图的卡片' % total_attached)

    # ---- 3. 校验
    if not dry:
        chk = open(HTML, encoding='utf-8').read()
        imgs = re.findall(r'src="assets/([^"]+)"', chk)
        print('\n校验: index.html 引用 %d 个 assets 文件' % len(imgs))
        files = set(os.listdir(ASSETS))
        missing_files = sorted(set(imgs) - files)
        print('缺失文件: %d' % len(missing_files))
        for f in missing_files[:10]:
            print('   ', f)
        print('assets 目录文件数: %d' % len(files))


if __name__ == '__main__':
    main()
