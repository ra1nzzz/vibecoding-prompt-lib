#!/usr/bin/env python3
"""生成 motion.html —— Motion Prompt 术语库中文版（120 条，5 大分类）。

数据来源：showheyohtaki/motion-prompt（MIT License, Copyright (c) 2026 Shohei Ohtaki）
动画渲染：内嵌原版 pack.js 的 Canvas 绘制函数，浏览器实时播放。
"""
import json, os, html

BASE = '/home/hatch/workspace/promptlib'
DATA = '/home/hatch/workspace/motionlib/zh_data.json'
PACKS = '/home/hatch/workspace/motionlib/packs'

d = json.load(open(DATA, encoding='utf-8'))
packs_order = sorted(d['packs'].items(), key=lambda kv: kv[1]['order'])

pack_src = [open(os.path.join(PACKS, k + '.js'), encoding='utf-8').read()
            for k in ['motion', 'camera', 'ui', 'lp', 'photo']]

items_json = json.dumps(d['items'], ensure_ascii=False)
packs_json = json.dumps({k: v for k, v in d['packs'].items()}, ensure_ascii=False)
pack_order_json = json.dumps([p for p, _ in packs_order])


def esc(s):
    return html.escape(s, quote=True)


tabs_html = "\n".join(
    '<button class="mtab" data-pack="%s" type="button"><b>%s</b><i>%d 条</i></button>'
    % (pk, esc(pv['title_zh']), len([i for i in d['items'] if i['pack'] == pk]))
    for pk, pv in packs_order
)

cats_parts = []
for pk, pv in packs_order:
    chips = "".join(
        '<button class="chip" data-pack="%s" data-cat="%s" type="button">%s</button>'
        % (pk, esc(c['slug']), esc(c['zh'])) for c in pv['cats']
    )
    cats_parts.append('<div class="cats" data-pack="%s" hidden>%s'
                      '<button class="chip is-all" data-pack="%s" data-cat="*" type="button">全部</button></div>'
                      % (pk, chips, pk))
cats_html = "\n".join(cats_parts)

pack_scripts = "\n".join('<script>' + s + '</script>' for s in pack_src)

TPL = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Motion Prompt 术语库 · 中文版 | 弈韬 Vibecoding 灵感与提示词库</title>
<meta name="description" content="120 个 AI 动效与影像专业术语的中文释义与提示词，覆盖动态图形、摄像机、UI 组件、落地页、照片质感五大类。译自 showheyohtaki/motion-prompt（MIT）。">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Noto+Sans+SC:wght@400;500;700;900&display=swap" rel="stylesheet">
<style>
:root{color-scheme:light dark;--bg:#f3f4f1;--paper:#fff;--ink:#171814;--muted:#62665d;--line:#d8dbd3;--accent:#ef5b2a;--soft:#ffe5d7;--code:#171a18;--codeink:#f7f6ef;--shadow:0 16px 40px rgba(26,31,23,.08)}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"Noto Sans SC",sans-serif;line-height:1.7}
.wrap{max-width:1180px;margin:0 auto;padding:0 22px}
a{color:inherit}
.topbar{position:sticky;top:0;z-index:50;background:rgba(243,244,241,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.topbar-in{display:flex;align-items:center;gap:14px;height:58px}
.brand{font:700 15px/1 "Noto Sans SC",sans-serif;letter-spacing:.02em;text-decoration:none;display:flex;align-items:center;gap:8px}
.brand i{width:9px;height:9px;border-radius:3px;background:var(--accent);display:block}
.topbar nav{margin-left:auto;display:flex;gap:4px}
.topbar nav a{font-size:13px;color:var(--muted);text-decoration:none;padding:7px 11px;border-radius:8px}
.topbar nav a:hover{background:var(--soft);color:var(--accent)}
.topbar nav a.on{color:var(--ink);font-weight:700}
.hero{padding:clamp(38px,6vw,72px) 0 30px;border-bottom:1px solid var(--line)}
.eyebrow{display:flex;align-items:center;gap:9px;color:var(--accent);font:600 12px/1 "DM Mono",monospace;letter-spacing:.08em}
.eyebrow::after{content:"";flex:1;height:1px;background:var(--line)}
h1{font:900 clamp(30px,5.2vw,54px)/1.14 "Noto Sans SC",sans-serif;margin:16px 0 0;letter-spacing:-.01em}
.lede{max-width:720px;margin:16px 0 0;color:var(--muted);font-size:clamp(15px,1.8vw,18px)}
.credit{margin-top:18px;padding:13px 16px;border:1px solid var(--line);border-radius:12px;background:var(--paper);font-size:13px;color:var(--muted);max-width:760px}
.credit b{color:var(--ink)}
.credit a{color:var(--accent);text-decoration:none;border-bottom:1px solid var(--soft)}
.tools{position:sticky;top:58px;z-index:40;background:rgba(243,244,241,.94);backdrop-filter:blur(10px);border-bottom:1px solid var(--line);padding:12px 0}
.searchrow{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.search{flex:1;min-width:220px;position:relative}
.search input{width:100%;padding:11px 14px 11px 38px;border:1px solid var(--line);border-radius:11px;background:var(--paper);color:var(--ink);font:15px/1.4 "Noto Sans SC",sans-serif}
.search input:focus{outline:2px solid var(--accent);outline-offset:1px;border-color:var(--accent)}
.search svg{position:absolute;left:12px;top:50%;transform:translateY(-50%);opacity:.45}
.count{font:500 13px/1 "DM Mono",monospace;color:var(--muted);white-space:nowrap}
.mtabs{display:flex;gap:8px;overflow-x:auto;margin-top:11px;padding-bottom:2px;scrollbar-width:thin}
.mtab{flex:0 0 auto;display:flex;flex-direction:column;gap:2px;align-items:flex-start;padding:9px 14px;border:1px solid var(--line);border-radius:11px;background:var(--paper);cursor:pointer;font-family:inherit}
.mtab b{font-size:14px;font-weight:700}
.mtab i{font:400 11px/1 "DM Mono",monospace;color:var(--muted);font-style:normal}
.mtab.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.mtab.on i{color:rgba(255,255,255,.6)}
.cats{display:flex;gap:7px;flex-wrap:wrap;margin-top:10px}
.chip{padding:6px 12px;border:1px solid var(--line);border-radius:999px;background:var(--paper);cursor:pointer;font:500 13px/1 "Noto Sans SC",sans-serif;color:var(--muted)}
.chip.on{background:var(--soft);border-color:var(--accent);color:var(--accent)}
main{padding:26px 0 70px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:22px}
.card{position:relative;background:var(--paper);border:1px solid var(--line);border-radius:16px;overflow:hidden;display:flex;flex-direction:column;box-shadow:0 2px 10px rgba(26,31,23,.04)}
.card:hover{box-shadow:var(--shadow)}
.stage{position:relative;background:#0d0e0c;aspect-ratio:539/208;overflow:hidden}
.stage canvas{display:block;width:100%;height:100%}
.stage .ph{position:absolute;inset:0;display:grid;place-items:center;color:#5b6157;font:500 12px/1 "DM Mono",monospace;letter-spacing:.06em}
.card-body{padding:16px 17px 17px;display:flex;flex-direction:column;gap:10px;flex:1}
.idline{display:flex;align-items:baseline;gap:9px}
.num{font:500 12px/1 "DM Mono",monospace;color:var(--accent);background:var(--soft);padding:5px 8px;border-radius:7px}
.en{font:500 12px/1.2 "DM Mono",monospace;color:var(--muted);letter-spacing:.02em}
.card h3{margin:0;font:700 17px/1.35 "Noto Sans SC",sans-serif}
.mean{margin:0;color:var(--muted);font-size:14px}
.prompt{position:relative;margin-top:2px;padding:13px 76px 13px 13px;background:var(--code);color:var(--codeink);border-radius:11px;font-size:13.5px;line-height:1.62}
.copy{position:absolute;right:9px;top:9px;padding:6px 11px;border:0;border-radius:8px;background:var(--accent);color:#fff;font:600 12px/1 "Noto Sans SC",sans-serif;cursor:pointer}
.copy:hover{filter:brightness(1.08)}
.copy.done{background:#2EDBA8;color:#08301f}
.tags{display:flex;gap:6px;flex-wrap:wrap;margin-top:auto;padding-top:4px}
.tag{font:400 11px/1 "DM Mono",monospace;color:var(--muted);border:1px solid var(--line);border-radius:6px;padding:5px 7px}
.use{margin:0;font-size:13px;color:var(--muted);border-left:2px solid var(--soft);padding-left:10px}
.use b{color:var(--ink);font-weight:700}
.empty{padding:60px 0;text-align:center;color:var(--muted)}
footer{border-top:1px solid var(--line);padding:26px 0 46px;color:var(--muted);font-size:13px}
footer a{color:var(--accent);text-decoration:none}
@media (max-width:640px){.topbar-in{height:52px}.tools{top:52px}.grid{grid-template-columns:1fr}}
</style>
</head>
<body>
<div class="topbar"><div class="wrap topbar-in">
  <a class="brand" href="index.html"><i></i>弈韬 Vibecoding 灵感与提示词库</a>
  <nav><a href="index.html">短视频灵感库</a><a href="motion.html" class="on">Motion Prompt 术语库</a></nav>
</div></div>

<header class="hero"><div class="wrap">
  <div class="eyebrow">MOTION PROMPT LIBRARY · 中文版</div>
  <h1>跟 AI 说「那个动效」时，<br>用它的专业名字</h1>
  <p class="lede">120 个动态图形、摄像机、UI 组件、落地页与照片质感的专业术语。每条都有中文释义、一段可以直接发给 AI 的提示词，以及一个能动的示例。选好术语，把提示词丢给 Claude Code 或 Codex，它就知道你要什么。</p>
  <div class="credit"><b>来源与授权：</b>译自 <a href="https://github.com/showheyohtaki/motion-prompt" target="_blank" rel="noopener">showheyohtaki/motion-prompt</a>（<a href="https://github.com/showheyohtaki/motion-prompt/blob/main/LICENSE" target="_blank" rel="noopener">MIT License</a>，Copyright (c) 2026 Shohei Ohtaki），原站 <a href="https://showheyohtaki.github.io/motion-prompt/" target="_blank" rel="noopener">showheyohtaki.github.io/motion-prompt</a>。动画由原版 Canvas 绘制代码在浏览器中实时播放；中文释义与提示词为本站译写。术语整理参考 X 用户 <a href="https://x.com/showheyohtaki" target="_blank" rel="noopener">@showheyohtaki</a>。</div>
</div></header>

<div class="tools"><div class="wrap">
  <div class="searchrow">
    <div class="search">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
      <input id="q" type="search" placeholder="搜索术语、释义或标签，如：缓动、滚动、逆光、spring…" autocomplete="off">
    </div>
    <span class="count" id="count"></span>
  </div>
  <div class="mtabs" id="mtabs">__TABS__</div>
  <div id="catsWrap">__CATS__</div>
</div></div>

<main class="wrap">
  <div class="grid" id="grid"></div>
  <div class="empty" id="empty" hidden>没有匹配的术语。换个关键词试试。</div>
</main>

<footer><div class="wrap">
  数据与动画代码来自 <a href="https://github.com/showheyohtaki/motion-prompt" target="_blank" rel="noopener">showheyohtaki/motion-prompt</a>（MIT License · Copyright (c) 2026 Shohei Ohtaki），中文释义与提示词为本站译写。<br>
  © 弈韬 Vibecoding 灵感与提示词库 · <a href="index.html">返回短视频灵感库</a>
</div></footer>

<script>
/* Motion Prompt runtime 注册表（与原站 runtime.js 一致）。
   pack.js 以全局 MotionPrompt.pack(...) 注册，故此处提供全局对象。 */
window.MotionPrompt = { packs: {}, pack(id, f) { const p = f(); p.id = id; this.packs[id] = p; return p; } };
</script>
__PACKS__

<script>
const ITEMS = __ITEMS__;
const PACKS = __PACKS_META__;
const PACK_ORDER = __PACK_ORDER__;

const grid = document.getElementById('grid');
const empty = document.getElementById('empty');
const countEl = document.getElementById('count');
const qEl = document.getElementById('q');
const catsWrap = document.getElementById('catsWrap');

let state = { pack: PACK_ORDER[0], cat: '*', q: '', qPack: null };

function syncTabUI() {
  document.querySelectorAll('.mtab').forEach(x => x.classList.toggle('on', x.dataset.pack === state.pack));
  catsWrap.querySelectorAll('.cats').forEach(c => { c.hidden = c.dataset.pack !== state.pack; });
  catsWrap.querySelectorAll('.chip').forEach(c => c.classList.toggle('on', c.dataset.pack === state.pack && c.dataset.cat === state.cat));
}

function esc(s) {
  return String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[c]);
}

function matches(it) {
  if (state.cat !== '*' && it.category !== state.cat) return false;
  if (state.q) {
    const hay = [it.name_zh, it.name_en, it.meaning_zh, it.use_zh, it.ask_zh, (it.tags||[]).join(' ')].join(' ').toLowerCase();
    if (!hay.includes(state.q)) return false;
    return true;
  }
  return it.pack === state.pack;
}

function cardHTML(it) {
  const tags = (it.tags || []).slice(0, 6).map(t => '<span class="tag">' + esc(t) + '</span>').join('');
  return '<article class="card" data-id="' + it.id + '">'
    + '<div class="stage"><span class="ph">' + esc(it.id) + ' · 加载中</span></div>'
    + '<div class="card-body">'
    + '<div class="idline"><span class="num">' + esc(it.id) + '</span><span class="en">' + esc(it.name_en) + '</span></div>'
    + '<h3>' + esc(it.name_zh) + '</h3>'
    + '<p class="mean">' + esc(it.meaning_zh) + '</p>'
    + '<div class="prompt"><button class="copy" type="button">复制提示词</button>' + esc(it.ask_zh) + '</div>'
    + '<p class="use"><b>适用场景：</b>' + esc(it.use_zh) + '</p>'
    + '<div class="tags">' + tags + '</div>'
    + '</div></article>';
}

/* ---------- Canvas 播放 ---------- */
const players = new Map();

function makePlayer(card, it) {
  const p = window.MotionPrompt.packs[it.pack];
  if (!p) return;
  const cell = p.cells[parseInt(it.no, 10) - 1];
  if (!cell) return;
  const stage = card.querySelector('.stage');
  const ph = stage.querySelector('.ph');
  const cv = document.createElement('canvas');
  cv.width = it.w; cv.height = it.h;
  stage.insertBefore(cv, ph);
  ph.remove();
  players.set(it.id, { canvas: cv, ctx: cv.getContext('2d'), cell: cell, cycle: p.cycle, w: it.w, h: it.h });
}

/* 视口判定：用 getBoundingClientRect，比 IntersectionObserver 更可靠 */
function inView(canvas, margin) {
  const r = canvas.getBoundingClientRect();
  return r.bottom > -margin && r.top < (window.innerHeight + margin) && r.right > 0 && r.left < window.innerWidth;
}

let rafId = 0;
let timerId = 0;
function tick(now) {
  if (!now) now = performance.now();
  players.forEach((rec) => {
    if (!inView(rec.canvas, 300)) return;
    const u = ((now - rec.t0) / 1000) % rec.cycle;
    rec.ctx.clearRect(0, 0, rec.w, rec.h);
    rec.cell(rec.ctx, rec.w, rec.h, u);
  });
}

function startLoop() {
  stopLoop();
  const loop = () => tick(performance.now());
  rafId = requestAnimationFrame(function frame() { loop(); rafId = requestAnimationFrame(frame); });
  /* rAF 在页面不可见（后台标签、无头环境）会暂停，用定时器兜底 */
  timerId = setInterval(loop, 1000 / 24);
}

function stopLoop() {
  if (rafId) { cancelAnimationFrame(rafId); rafId = 0; }
  if (timerId) { clearInterval(timerId); timerId = 0; }
}

function render() {
  const list = ITEMS.filter(matches);
  grid.innerHTML = list.map(cardHTML).join('');
  empty.hidden = list.length > 0;
  countEl.textContent = list.length + ' / ' + ITEMS.length + ' 条';
  players.clear();
  stopLoop();
  grid.querySelectorAll('.card').forEach(card => {
    const it = ITEMS.find(x => x.id === card.dataset.id);
    makePlayer(card, it);
    const r = players.get(it.id);
    if (r) { r.t0 = performance.now(); drawAt(r, 0); }
  });
  if (list.length) startLoop();
}

function drawAt(rec, u) {
  rec.ctx.clearRect(0, 0, rec.w, rec.h);
  rec.cell(rec.ctx, rec.w, rec.h, u);
}

/* ---------- 交互 ---------- */
document.getElementById('mtabs').addEventListener('click', e => {
  const b = e.target.closest('.mtab'); if (!b) return;
  state.pack = b.dataset.pack; state.cat = '*'; state.q = ''; state.qPack = null;
  qEl.value = '';
  syncTabUI();
  render();
});

catsWrap.addEventListener('click', e => {
  const b = e.target.closest('.chip'); if (!b) return;
  state.cat = b.dataset.cat;
  syncTabUI();
  render();
});

let deb;
qEl.addEventListener('input', () => {
  clearTimeout(deb);
  deb = setTimeout(() => {
    state.q = qEl.value.trim().toLowerCase();
    if (state.q) { state.cat = '*'; state.qPack = state.pack; }
    else if (state.qPack) { state.pack = state.qPack; state.qPack = null; }
    syncTabUI();
    render();
  }, 120);
});

grid.addEventListener('click', e => {
  const b = e.target.closest('.copy'); if (!b) return;
  const card = b.closest('.card');
  const it = ITEMS.find(x => x.id === card.dataset.id);
  const done = () => { b.textContent = '已复制'; b.classList.add('done');
    setTimeout(() => { b.textContent = '复制提示词'; b.classList.remove('done'); }, 1400); };
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(it.ask_zh).then(done).catch(() => fallbackCopy(it.ask_zh, done));
  } else fallbackCopy(it.ask_zh, done);
});

function fallbackCopy(text, done) {
  const ta = document.createElement('textarea');
  ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
  document.body.appendChild(ta); ta.select();
  try { document.execCommand('copy'); done(); } catch (e) {}
  document.body.removeChild(ta);
}

/* ---------- 初始 ---------- */
syncTabUI();
render();
</script>
</body>
</html>
'''

page = (TPL
        .replace('__TABS__', tabs_html)
        .replace('__CATS__', cats_html)
        .replace('__PACKS__', pack_scripts)
        .replace('__ITEMS__', items_json)
        .replace('__PACKS_META__', packs_json)
        .replace('__PACK_ORDER__', pack_order_json))

out = os.path.join(BASE, 'motion.html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(page)
print('wrote', out, len(page.encode('utf-8')), 'bytes')
print('items:', len(d['items']), '| packs:', list(d['packs'].keys()))
