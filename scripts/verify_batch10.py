#!/usr/bin/env python3
"""批次10 校验：entry-134"""
import re, os, subprocess

os.chdir('/home/hatch/workspace/promptlib')
before = subprocess.run(['git','show','HEAD:index.html'], capture_output=True, text=True).stdout
after = open('index.html', encoding='utf-8').read()

b = set(re.findall(r'id="entry-(\d+)"', before))
a = set(re.findall(r'id="entry-(\d+)"', after))
new = a - b
print(f"条目数: {len(b)} -> {len(a)}, 新增: {sorted(new, key=int)}")
assert new == {'134'}, f"变更集异常: {new}"

hb = before[:before.find('<article')]; ha = after[:after.find('<article')]
tb = before[before.rfind('</article>'):]; ta = after[after.rfind('</article>'):]
print(f"head 一致: {hb==ha}, tail 一致: {tb==ta}")
assert hb == ha and tb == ta, "head/tail 被改动"

for tag in ['article','section','div','p','header']:
    o=len(re.findall(f'<{tag}[ >]',after)); c=len(re.findall(f'</{tag}>',after))
    st = "OK" if o==c else "MISMATCH"
    print(f"  <{tag}>: {o}/{c} {st}")
    assert o == c, f"标签不配对: {tag}"

imgs = re.findall(r'src="(assets/[^"]+)"', after)
missing = [p for p in imgs if not os.path.isfile(p)]
print(f"图片引用: {len(imgs)}, 缺失: {len(missing)}")
assert not missing, f"缺失图片: {missing[:5]}"

m = re.search(r'id="entry-134">.*?</article>', after, re.S)
block = m.group(0)
cards = len(re.findall(r'<section class="card', block))
imgs_e = len(re.findall(r'src="assets/', block))
pboxes = len(re.findall(r'prompt-box', block))
print(f"entry-134: {cards} 卡, {imgs_e} 图, {pboxes} prompt-box")
assert cards == 4 and imgs_e == 4 and pboxes == 4

# DOM 顺序与 before 一致
order_b = re.findall(r'id="entry-(\d+)"', before)
order_a = re.findall(r'id="entry-(\d+)"', after)
assert order_b == order_a[:-1], "DOM 顺序被改动"
print("DOM 顺序保留: OK")

print("\n=== 全部校验通过 ===")
