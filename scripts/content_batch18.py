# -*- coding: utf-8 -*-
"""entry-142：开发工程师彭飞「用 AI，把角色创意变成 Spine 动画」。
源视频 7702773238065040649，31.21 秒，7 张配图。
"""
import html

IMG = ['pengfei-spine-%d.jpg' % i for i in range(1, 8)]
SRC = 'https://www.douyin.com/video/7702773238065040649'

CARDS = [
    dict(
        h3='提示词 + 动画模板 → AI 生成',
        en='PROMPT + TEMPLATE',
        selling='整个产品就两步：写一句角色描述，选一个动画模板，剩下的交给 AI。',
        process='<strong>核心公式：</strong>提示词 + 动画模板 → AI 生成。左侧卡片是「你的提示词」，右侧卡片是「动画模板」，中间用一个「+」连接，底下写着「描述你的角色」。示例提示词是：<code>换成一个末日风格的Q版防暴丧尸，灰绿色腐化皮肤，眼神凶狠，戴破损防暴头盔，穿磨损的深灰色防护甲。</code>不用从零画角色、绑骨骼、K 帧，一句话就能换个皮。',
        prompt='我想让角色动起来：先选一个动画模板作为骨架和动作基础，再用一段提示词描述新角色的外观、装备和风格，让 AI 生成配套的 Spine 角色动画。',
    ),
    dict(
        h3='从选择模板开始',
        en='PICK A TEMPLATE',
        selling='模板库就是创作起点，网格里铺满各种职业和风格的角色。',
        process='<strong>流程第一步。</strong>页面标题「丰富模板，承载你的创意。」副标题「探索不同角色，适配多种创作需求。」网格里能看到金甲圣盾骑士、熔岩巨斧莽人、铁皮灰刃魔武士、蓝晶圣蓝法神、雷霆守卫战士、双刀木偶小将、烈焰蝙蝠战士、银盔镰刀骑士——战士、骑士、法师、恶魔、熊猫、忍者全覆盖。<strong>先挑一个顺眼的当底子，不用白手起家。</strong>',
        prompt='请给我一个角色动画模板库，按职业和风格分类（战士、骑士、法师、恶魔、动物拟人、忍者等），网格排列，每个模板配中文名称和预览图，让我直接挑选作为创作起点。',
    ),
    dict(
        h3='提示词创作：描述创意，塑造角色',
        en='PROMPT STUDIO',
        selling='形象面板把「模板 + 提示词」并排摆，改文案就能改角色。',
        process='<strong>核心操作台。</strong>深色面板标题「创建角色形象」，右上角标着「AI 创作空间」。左侧是「模板」缩略图，右侧是「角色形象」输入框和「提示词」输入框，右下角绿色按钮「生成形象」。底部一行流程：<strong>描述角色 / 生成形象 / 生成动画</strong>。提示词框里那段文案，除了描述外观，还锁定了结构：保持参考角色的<strong>朝向、姿态、头身比例和四肢位置</strong>，盾牌警棍的大小、位置与握持关系也都要跟参考图一致，最后要求<strong>完整展示全身、透明背景、卡游游戏画风</strong>。<strong>形象随便换，骨架锁死不动。</strong>',
        prompt='做一个 AI 角色创作面板：左边放参考模板缩略图，右边放「角色形象」名称输入框和「提示词」多行输入框，底部固定「生成形象」按钮。提示词要同时约束外观（皮肤、眼神、头盔、护甲、武器）和结构（朝向、姿态、头身比例、四肢位置、装备的握持关系），并要求输出透明背景的全身立绘。',
    ),
    dict(
        h3='01 生成形象：让灵感成形',
        en='GENERATE IMAGE',
        selling='形象这一步出的是完整立绘，选定后直接进下一步。',
        process='<strong>第一步「生成形象」。</strong>标题「让灵感成形。」说明「结合提示词，生成完整角色形象。」右侧深色卡片顶部打勾写着「形象已选定」——卡片里就是最终生成的角色：灰绿色腐化皮肤、黄色眼睛露出獠牙、破损头盔带裂痕、深色盔甲配肩甲和护臂、身上有血迹和战损痕迹，一手持带尖刺和抓痕的盾牌，一手持生锈警棍。<strong>左侧已经预备好第二步「02 生成动画」的绿色按钮。</strong>',
        prompt='先生成角色形象：根据提示词输出一张完整的角色立绘，要求姿态、装备、比例与参考模板严格一致，风格统一为卡通风，背景透明。生成后在预览卡片顶部显示「形象已选定」，并在左侧露出下一步「生成动画」入口。',
    ),
    dict(
        h3='02 生成动画：一个角色，5 种动作',
        en='GENERATE ANIMATION',
        selling='同一个形象，一键出待机、攻击、死亡、受击、奔跑五套动作。',
        process='<strong>第二步「生成动画」。</strong>标题「一个角色，5种动作」「每个动作，都生动。」说明「延续模板动作，展现角色表现力。」左下角五个按钮：<strong>待机 / 攻击 / 死亡 / 受击 / 奔跑</strong>，当前高亮的是「待机」。右侧角色实时播放对应动作。<strong>关键在于「延续模板动作」——动作是从模板继承来的，AI 只负责把新形象贴上去，所以动作不会崩。</strong>',
        prompt='基于已选定的角色形象生成 Spine 动画：沿用所选动画模板的动作数据，把新形象套进去，输出待机、攻击、死亡、受击、奔跑五个动作。界面上做一组动作切换按钮，当前选中的动作高亮，右侧实时播放对应动画。',
    ),
    dict(
        h3='5 种动作，完整呈现',
        en='FIVE ACTIONS',
        selling='五个动作平铺展示，一眼看全角色的表现力。',
        process='<strong>成品总览。</strong>标题「5种动作，完整呈现。」副标题「待机 · 攻击 · 死亡 · 受击 · 奔跑」。五张卡片编号 01–05：<strong>01 待机</strong>站立姿态自然；<strong>02 攻击</strong>身体前倾手臂挥出武器；<strong>03 死亡</strong>头盔与身体分离倒地；<strong>04 受击</strong>身体后仰收缩；<strong>05 奔跑</strong>身体前倾作跑动姿态。<strong>同一个角色五种状态，直接就是一套游戏资产。</strong>',
        prompt='把生成的角色动画按五张卡片平铺展示，每张卡片右下角编号 01–05，卡片下方标注动作名称（待机、攻击、死亡、受击、奔跑），同一角色在五种动作下的姿态清晰可辨，方便一次看全表现力。',
    ),
    dict(
        h3='从创意到动画',
        en='IDEA TO ANIMATION',
        selling='官网首页一句话把价值说完了：基于动画模板，用 AI 焕新角色。',
        process='<strong>产品首页。</strong>小字「从创意到动画」，主标题「你的角色，即刻呈现。」副标题「基于动画模板，用 AI 焕新角色。」右侧是示例角色——戴带红色划痕的头盔、身披盔甲、眼睛发光、手持武器。<strong>这句副标题就是整个方案的本质：AI 负责「焕新」，动作稳不稳靠模板。</strong>',
        prompt='做一个 AI 角色动画产品的首页：顶部小字「从创意到动画」，主标题「你的角色，即刻呈现。」副标题「基于动画模板，用 AI 焕新角色。」右侧放一个示例角色（带头盔、盔甲、发光眼睛、手持武器），整体深色背景、留白充足，突出角色本身。',
    ),
]

TITLE = '用 AI，把角色创意变成 Spine 动画'
AUTHOR = '开发工程师彭飞'
DURATION = '31.2 秒'

INTRO = ('开发工程师彭飞演示了一套 AI 角色动画方案：<strong>提示词 + 动画模板 → AI 生成</strong>。'
         '从一个动画模板起步，写一段角色描述，先生成完整形象，再生成配套的 Spine 角色动画，'
         '一次拿到待机、攻击、死亡、受击、奔跑五个动作。'
         '关键在于动作是从模板继承的——AI 只负责焕新形象，所以动作不会崩。')

OUTRO = ('<strong>这套方案真正省力的地方：</strong>角色创作里最贵的不是画形象，是让形象动起来还不崩。'
         '它把「动起来」这件事交给动画模板——待机、攻击、死亡、受击、奔跑的动作数据都是现成的，'
         'AI 只需要把你的新描述贴到这套动作上。所以你写提示词时重点不是描述动作，'
         '而是<strong>锁死结构</strong>：朝向、姿态、头身比例、四肢位置、装备的握持关系，全都要跟参考图一致。'
         '形象可以随便焕新，骨架别动。')


def esc(s):
    return html.escape(s, quote=False)


def render_card(i, c):
    img = IMG[i]
    num = '%02d' % (i + 1)
    return '''    <section class="card">
    <div class="visual"><img loading="lazy" decoding="async" src="assets/{img}" alt="{alt}"><span class="num">{num}</span><p class="image-note">{note}</p></div>
    <div class="content"><h3>{h3}</h3><p class="en">{en}</p>
    <p class="selling">{selling}</p>
    <p class="process">{process}</p>
    <div class="prompt-label">AI 描述词</div>
    <div class="prompt-box"><p>{prompt}</p><button class="copy" type="button">复制</button></div>
    </div></section>
'''.format(img=img, alt=esc(c['h3']), num=num, note=esc(c['h3']),
           h3=c['h3'], en=c['en'], selling=c['selling'],
           process=c['process'], prompt=esc(c['prompt']))


CARDS_HTML = ''.join(render_card(i, c) for i, c in enumerate(CARDS))
NAV_LINKS = ''.join('<a href="#spine-c%d">%s</a>' % (i + 1, esc(c['h3']))
                    for i, c in enumerate(CARDS))

ENTRY = '''<article class="entry" id="entry-142">
  <header class="entry-head"><div><h2>{title}</h2><div class="meta"><span>{author}</span><time datetime="2026-06-07">2026-06-07</time><span>{dur}</span></div></div><a class="source" href="{src}" target="_blank" rel="noopener">查看原视频 <span aria-hidden="true">↗</span></a></header>
  <p class="intro">{intro}</p>
  <nav class="jump" aria-label="本条目内容">{nav}</nav>
  <div class="cards">
{cards}
  </div>
  <p class="outro">{outro}</p>
</article>'''.format(title=esc(TITLE), author=AUTHOR, dur=DURATION, src=SRC,
                   intro=INTRO, nav=NAV_LINKS, cards=CARDS_HTML, outro=OUTRO)

BATCH = {'entry-142': ENTRY}
