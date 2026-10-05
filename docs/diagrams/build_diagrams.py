# -*- coding: utf-8 -*-
"""生成去中心化教材勘误项目的说明图（fig1 总体闭环 / fig2 论证收敛）。

用法: python build_diagrams.py
输出: fig1-loop.png / fig2-argument.png  (与脚本同目录)
依赖: Pillow + Windows 自带中文字体
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SS = 2  # 超采样倍数，用于抗锯齿

REG_CANDIDATES = [
    ("C:/Windows/Fonts/msyh.ttc", 0),
    ("C:/Windows/Fonts/Deng.ttf", 0),
    ("C:/Windows/Fonts/simhei.ttf", 0),
]
BOLD_CANDIDATES = [
    ("C:/Windows/Fonts/msyhbd.ttc", 0),
    ("C:/Windows/Fonts/simhei.ttf", 0),
]


def _pick(cands):
    for path, idx in cands:
        if os.path.exists(path):
            return path, idx
    raise SystemExit("找不到可用的中文字体")


REG_PATH, REG_IDX = _pick(REG_CANDIDATES)
BOLD_PATH, BOLD_IDX = _pick(BOLD_CANDIDATES)

BG = "#f6f7f9"
INK = "#1a1d21"
MUTED = "#5a6472"
FAINT = "#7a8698"
BODY = "#4a5464"
LINE = "#d8dee7"
BLUE = "#3b6ef5"
RED = "#c0392b"
RED_SOFT = "#a05555"
GREEN = "#18794e"
GREEN_SOFT = "#3f7a5c"
AMBER = "#92610a"


def _segments(text):
    """把 **加粗** 标记切成 (片段, 是否加粗) 列表。"""
    parts = text.split("**")
    out = [(p, i % 2 == 1) for i, p in enumerate(parts) if p]
    return out or [("", False)]


class Canvas:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.img = Image.new("RGB", (w * SS, h * SS), BG)
        self.d = ImageDraw.Draw(self.img)
        self._fonts = {}

    def font(self, size, bold=False):
        key = (size, bold)
        if key not in self._fonts:
            path, idx = (BOLD_PATH, BOLD_IDX) if bold else (REG_PATH, REG_IDX)
            self._fonts[key] = ImageFont.truetype(path, size * SS, index=idx)
        return self._fonts[key]

    def box(self, x, y, w, h, fill=None, outline=None, radius=10, width=1.5):
        self.d.rounded_rectangle(
            [x * SS, y * SS, (x + w) * SS, (y + h) * SS],
            radius=radius * SS, fill=fill, outline=outline,
            width=max(1, int(round(width * SS))),
        )

    def line(self, x1, y1, x2, y2, fill=LINE, width=1.5):
        self.d.line([x1 * SS, y1 * SS, x2 * SS, y2 * SS], fill=fill,
                    width=max(1, int(round(width * SS))))

    def arrow(self, x1, y1, x2, y2, fill=FAINT, width=2.2, head=9):
        """带箭头的直线。"""
        self.line(x1, y1, x2, y2, fill=fill, width=width)
        dx, dy = x2 - x1, y2 - y1
        n = (dx * dx + dy * dy) ** 0.5 or 1
        ux, uy = dx / n, dy / n
        px, py = -uy, ux
        tip = (x2, y2)
        left = (x2 - ux * head + px * head * 0.45, y2 - uy * head + py * head * 0.45)
        right = (x2 - ux * head - px * head * 0.45, y2 - uy * head - py * head * 0.45)
        self.d.polygon([(tip[0] * SS, tip[1] * SS), (left[0] * SS, left[1] * SS),
                        (right[0] * SS, right[1] * SS)], fill=fill)

    def dot(self, cx, cy, r, fill):
        self.d.ellipse([(cx - r) * SS, (cy - r) * SS, (cx + r) * SS, (cy + r) * SS], fill=fill)

    def tri(self, cx, cy, size, direction="right", fill=FAINT):
        """画实心三角形（雅黑缺 ▶/◀ 字形，不能直接用字符）。"""
        if direction == "right":
            pts = [(cx - size * 0.55, cy - size), (cx - size * 0.55, cy + size), (cx + size * 0.85, cy)]
        else:
            pts = [(cx + size * 0.55, cy - size), (cx + size * 0.55, cy + size), (cx - size * 0.85, cy)]
        self.d.polygon([(px * SS, py * SS) for px, py in pts], fill=fill)

    def text(self, x, y, s, size=14, fill=INK, anchor="la", bold=False):
        """anchor: 水平 l/m/r + 垂直 a（文字顶部对齐到 y）。"""
        f = self.font(size, bold)
        total = f.getlength(s)
        xx = x * SS
        if anchor[0] == "m":
            xx -= total / 2
        elif anchor[0] == "r":
            xx -= total
        self.d.text((xx, y * SS), s, font=f, fill=fill, anchor="la")

    def rich(self, x, y, s, size=14, fill=BODY, bold_fill=None, anchor="la"):
        """支持 **加粗** 的单行文本。"""
        segs = _segments(s)
        fonts = [self.font(size, b) for _, b in segs]
        widths = [f.getlength(t) for (t, _), f in zip(segs, fonts)]
        xx = x * SS
        if anchor[0] == "m":
            xx -= sum(widths) / 2
        elif anchor[0] == "r":
            xx -= sum(widths)
        for (t, b), f, w in zip(segs, fonts, widths):
            self.d.text((xx, y * SS), t, font=f,
                        fill=(bold_fill or fill) if b else fill, anchor="la")
            xx += w

    def save(self, name):
        out = self.img.resize((self.w, self.h), Image.LANCZOS)
        path = os.path.join(HERE, name)
        out.save(path)
        print("saved", path, os.path.getsize(path), "bytes")
        return path


# ---------------------------------------------------------------- fig 1
def fig1():
    c = Canvas(1600, 750)
    c.text(40, 26, "去中心化教材勘误 · 总体闭环", size=30, fill=INK, bold=True)
    c.rich(40, 68,
           "书里的错误 → 公开讨论、上传证据 → 论证图 → **算出**结论（不投票）→ CI 强制执行 → 回到知识点",
           size=15, fill=MUTED)

    cards = [
        ("① 底本", "教材 / 指南", [
            "· 只存定位：ISBN、版次、页码",
            "· **不存原文、不存扫描页**",
            "   （版权红线）",
            "· 保留错误本身，它是教学资产",
        ]),
        ("② 知识点", "知识对象", [
            "· 四类对象：命题 / 教法 /",
            "   误解 / 资源",
            "· 每条带署名、证据、适用范围",
            "· error_kind：数值 / 单位 /",
            "   引用 / 过时 / 表述陷阱",
            "· 状态：草案·争议·已确证·需复审",
        ]),
        ("③ 主张 + 证据", "公开讨论", [
            "· 谁能提？任何人，但必须署名",
            "· 上传可核验证据：DOI、说明书、",
            "   数据、复算脚本",
            "· 未过门槛的只留评论，**不进判定**",
        ]),
        ("④ 论证图", "Argument Graph", [
            "· 论证对象 + 攻击 / 支持边",
            "· 去重、去量、按因果序排列",
            "· 谁主张谁举证；反驳方只需",
            "   指出一个致命漏洞",
        ]),
        ("⑤ 结论计算", "接地语义", [
            "· 解唯一、保守（宁留争议不强判）",
            "· 机器可复算、结果可审计",
            "· 输出：**已确证 / 争议**",
            "",
        ]),
    ]
    cy, ch, cw, aw = 110, 214, 268, 44
    x = 40
    for i, (num, ttl, lines) in enumerate(cards):
        c.box(x, cy, cw, ch, fill="#ffffff", outline=LINE, radius=12, width=1.5)
        c.text(x + 15, cy + 14, num, size=12.5, fill=BLUE, bold=True)
        c.text(x + 15, cy + 34, ttl, size=18.5, fill=INK, bold=True)
        ly = cy + 74
        for ln in lines:
            c.rich(x + 15, ly, ln, size=13.5, fill=BODY, bold_fill=INK)
            ly += 21
        x += cw
        if i < len(cards) - 1:
            c.tri(x + aw / 2, cy + ch / 2, 9, "right", "#9aa5b4")
            x += aw

    bars = [
        (338, 76, "#f4f0ff", "#b9a4f0", "AI 助手", "#6b46c1", [
            "书记员（把 300 条讨论压成论证图） · 检索员（找出被忽略的反证） · 红队（主动构造最强反驳）",
            "**不投票、不判决、不匿名** —— 每条输出署名，且只作为一条证据参与",
        ]),
        (428, 86, "#eefaf3", "#7cc79b", "CI 强制校验", GREEN, [
            "存在未被击倒的存活反驳 → **禁止**标记「已确证」；存在结论冲突的存活论证 → **强制**标记「争议」",
            "规则写在代码里，维护者也绕不过 —— 立法（规则）与执行（合并）分离",
        ]),
        (528, 86, "#ffffff", LINE, "阅读界面", BLUE, [
            "结论先行：当前状态 + 存活的最强正方 + 存活的最强反方 + 未决条件",
            "而不是 300 条评论流",
        ]),
        (628, 64, "#fff8e6", "#e0b34d", "时效复审", AMBER, [
            "新指南 / 新证据出现 → 状态自动降级为「需复审」→ 回流到 ①②；也允许任何人带全部历史 **fork 退出**，自己维护一份",
        ]),
    ]
    for by, bh, fill, outline, lab, labfill, lines in bars:
        c.box(40, by, 1520, bh, fill=fill, outline=outline, radius=12, width=1.5)
        if lab == "时效复审":
            c.tri(64, by + bh / 2, 7, "left", labfill)
            c.text(80, by + (bh - 30) / 2, lab, size=15, fill=labfill, bold=True)
        else:
            c.text(58, by + (bh - 30) / 2, lab, size=15, fill=labfill, bold=True)
        ly = by + 14 if len(lines) > 1 else by + (bh - 20) / 2
        for ln in lines:
            c.rich(190, ly, ln, size=13.5, fill=BODY, bold_fill=INK)
            ly += 22
    return c.save("fig1-loop.png")


# ---------------------------------------------------------------- fig 2
def fig2():
    c = Canvas(1600, 880)
    c.text(40, 26, "结论是「算」出来的，不是「投票」出来的", size=30, fill=INK, bold=True)
    c.text(40, 68, "同一个医学知识点（教材 P42：某药成人首剂 10mg），两种机制会得出完全不同的结果",
           size=14.5, fill=MUTED)

    # ---- panel A
    c.box(40, 108, 700, 474, fill="#ffffff", outline=LINE, radius=14, width=1.5)
    c.text(64, 126, "① 论证图", size=16.5, fill=INK, bold=True)
    c.text(152, 128, "= 公开讨论 + 证据上传的结构化结果", size=13.5, fill=FAINT)

    def arg(x, ttl, claim, grade, fill, stroke, gcolor):
        c.box(x, ytop, 280, 94, fill=fill, outline=stroke, radius=10, width=1.5)
        c.text(x + 18, ytop + 14, ttl, size=15, fill=INK, bold=True)
        c.text(x + 18, ytop + 40, claim, size=13.5, fill=BODY)
        c.text(x + 18, ytop + 62, grade, size=12.5, fill=gcolor)

    ytop = 182
    arg(80, "A1　教材 P42", "主张：首剂 10mg", "证据等级：教科书（低）", "#fdf2f2", "#e8a0a0", RED_SOFT)
    arg(420, "A2　说明书 + RCT", "主张：应为 5mg", "证据等级：高 · 可核验", "#f0f7ff", "#93b8f0", BLUE)

    ytop = 440
    arg(80, "A4　RCT（2025）", "主张：5mg 更优", "证据等级：高 · 可核验", "#f0f7ff", "#93b8f0", BLUE)
    arg(420, "A3　临床指南", "主张：首剂 10mg", "证据等级：高 · 可核验", "#f0f7ff", "#93b8f0", BLUE)

    c.arrow(420, 229, 366, 229, fill=RED, width=2.2, head=10)
    c.text(356, 216, "攻击", size=13, fill=RED, anchor="ra")
    c.arrow(220, 438, 220, 288, fill=RED, width=2.2, head=10)
    c.text(232, 356, "攻击", size=13, fill=RED)
    c.arrow(560, 438, 560, 288, fill=RED, width=2.2, head=10)
    c.text(572, 356, "攻击", size=13, fill=RED)
    c.text(64, 552, "红线 = 攻击：附证据指出「前提不实 / 推理无效 / 证据不足 / 提出更强反证」",
           size=12.5, fill=FAINT)

    # ---- panel B
    c.box(772, 108, 350, 474, fill="#ffffff", outline=LINE, radius=14, width=1.5)
    c.text(796, 126, "② 逐层判定", size=16.5, fill=INK, bold=True)
    c.text(932, 128, "接地语义", size=13.5, fill=FAINT)
    rows = [
        (178, GREEN, "A4 · 无攻击 → **存活**"),
        (224, GREEN, "A3 · 无攻击 → **存活**"),
        (270, RED, "A2 · 攻击者 A3 存活 → **出局**"),
        (316, RED, "A1 · 攻击者 A4 存活 → **出局**"),
    ]
    for ry, col, txt in rows:
        c.dot(806, ry + 10, 6, col)
        c.rich(822, ry, txt, size=14, fill=INK, bold_fill=INK)
    c.line(796, 362, 1098, 362, fill="#e4e8ee", width=1.5)
    c.rich(796, 384, "存活集合 = **{ A3, A4 }**", size=14, fill=BODY, bold_fill=INK)
    c.text(796, 420, "解唯一 · 保守 · 多项式时间可算", size=13.5, fill=FAINT)
    c.text(796, 448, "→ 机器可复算，任何人可审计", size=13.5, fill=FAINT)
    c.rich(796, 488, "→ 全程**没有一次投票**", size=13.5, fill=FAINT, bold_fill=RED)
    c.text(796, 528, "→ 教材那句「10mg」被 A4 推翻", size=13.5, fill=FAINT)

    # ---- panel C
    c.box(1154, 108, 406, 474, fill="#ffffff", outline=LINE, radius=14, width=1.5)
    c.text(1178, 126, "③ 系统状态", size=16.5, fill=INK, bold=True)

    c.box(1178, 168, 358, 66, fill="#eef4ff", outline="#93b8f0", radius=10, width=1.5)
    c.text(1198, 182, "存活论证", size=13.5, fill=BLUE, bold=True)
    c.text(1198, 204, "A3 说 10mg　／　A4 说 5mg", size=14, fill=INK)

    c.arrow(1357, 236, 1357, 262, fill=FAINT, width=2, head=9)

    c.box(1178, 266, 358, 76, fill="#fff8e6", outline="#e0b34d", radius=10, width=1.5)
    c.text(1198, 282, "冲突：两条最高等级证据结论相反", size=13.5, fill=AMBER, bold=True)
    c.text(1198, 308, "谁也打不倒谁 —— 这正是真实世界的常态", size=13.5, fill=BODY)

    c.arrow(1357, 344, 1357, 370, fill=FAINT, width=2, head=9)

    c.box(1178, 374, 358, 112, fill="#fdf2f2", outline="#e8a0a0", radius=10, width=1.5)
    c.text(1198, 390, "状态：争议", size=21, fill=RED, bold=True)
    c.text(1198, 426, "不选边 · 并列展示双方最强论证", size=13.5, fill=BODY)
    c.text(1198, 450, "不强行收敛 · 等新证据出现", size=13.5, fill=BODY)

    c.rich(1178, 512, "教材处标记：**「此处存在争议」**", size=13.5, fill=FAINT, bold_fill=RED)
    c.text(1178, 540, "而不是给它盖一个「正确」的章", size=13.5, fill=FAINT)

    # ---- bottom contrast
    c.box(40, 612, 1520, 150, fill="#ffffff", outline=LINE, radius=14, width=1.5)
    c.line(800, 612, 800, 762, fill="#e4e8ee", width=1.5)
    c.text(72, 632, "如果靠投票", size=16, fill=RED, bold=True)
    c.text(72, 664, "100 人投票：62 : 38　→　宣布「教材正确」", size=14, fill=BODY)
    c.text(72, 694, "失败点：数字淹没了少数方最强的那条证据", size=13.5, fill=RED_SOFT)
    c.text(72, 720, "A3 与 A4 谁对，与有多少人支持它无关", size=13.5, fill=RED_SOFT)

    c.text(832, 632, "本机制", size=16, fill=GREEN, bold=True)
    c.text(832, 664, "证据等级 + 反驳关系　→　状态「争议」", size=14, fill=BODY)
    c.text(832, 694, "少数方只要证据够硬，就不会被人数抹掉", size=13.5, fill=GREEN_SOFT)
    c.text(832, 720, "结论可溯源、可复算、可重放，也能 fork 退出", size=13.5, fill=GREEN_SOFT)

    c.rich(800, 796,
           "公正 ≠ 多数同意　｜　公正 = 证据可核验 · 最强反驳被完整保留 · 过程可重放 · 任何人可退出",
           size=15, fill=INK, bold_fill=INK, anchor="ma")
    return c.save("fig2-argument.png")


# ---------------------------------------------------------------- fig 3
def fig3():
    c = Canvas(1600, 900)
    c.text(40, 26, "一张知识图，无限本教科书", size=30, fill=INK, bold=True)
    c.rich(40, 68,
           "知识不只有真假，还有**对谁有效** —— 命题要收敛，教法要并存；教科书不是一本书，而是**对某个人的投影**",
           size=14.5, fill=MUTED)

    # ---- panel 1: the knowledge graph around one node
    c.box(40, 104, 548, 560, fill="#ffffff", outline=LINE, radius=14, width=1.5)
    c.text(64, 122, "① 知识图", size=16.5, fill=INK, bold=True)
    c.text(154, 124, "同一条知识点上挂着四类对象", size=13.5, fill=FAINT)

    CX, CY = 314, 388
    sats = [
        (170, 193), (438, 193), (170, 513), (438, 513),
    ]
    for sx, sy in sats:
        c.line(CX, CY, sx, sy, fill="#c8d0da", width=1.5)

    c.box(204, 344, 220, 88, fill="#eef1f5", outline="#98a2b3", radius=12, width=1.5)
    c.text(CX, 360, "知识点 K", size=14, fill=MUTED, anchor="ma", bold=True)
    c.text(CX, 384, "欧姆定律", size=17, fill=INK, anchor="ma", bold=True)
    c.text(CX, 410, "内容寻址 · 署名", size=11.5, fill=FAINT, anchor="ma")

    def sat(x, y, chip, chipfill, ttl, sub):
        c.box(x, y, 220, 86, fill="#ffffff", outline=LINE, radius=10, width=1.5)
        c.text(x + 18, y + 14, chip, size=12.5, fill=chipfill, bold=True)
        c.text(x + 18, y + 36, ttl, size=14, fill=INK)
        c.text(x + 18, y + 60, sub, size=11.5, fill=FAINT)

    sat(60, 150, "命题 · 真 / 假", BLUE, "V = I × R", "要收敛 → 只能有一个结论")
    sat(328, 150, "教法 · 对谁有效", "#6b46c1", "水管类比 / 场论推导", "要并存 → 按条件索引")
    sat(60, 470, "误解 · 常见错误", AMBER, "把电压当成水流速度", "是教学资产，不是垃圾")
    sat(328, 470, "资源 · 素材", GREEN, "水流动画、例题集", "可替换、可版本化")

    c.text(64, 596, "边有类型：先修 / 例示 / 诊断 / 支持 / 攻击", size=12.5, fill=FAINT)
    c.text(64, 622, "每一种断言都带署名、证据与适用范围 —— 引擎只有一个", size=12.5, fill=FAINT)

    # ---- arrow
    c.tri(614, 384, 11, "right", "#9aa5b4")

    # ---- panel 2: learner profile
    c.box(644, 104, 356, 560, fill="#ffffff", outline=LINE, radius=14, width=1.5)
    c.text(668, 122, "② 读者画像", size=16.5, fill=INK, bold=True)
    rows = [
        ("先修水平", "没学过微积分"),
        ("学习目标", "中考物理及格"),
        ("时长约束", "每节 ≤ 15 分钟"),
        ("设备环境", "手机、无耳机"),
        ("已知误解", "把电压当水流速度"),
        ("语言", "中文"),
    ]
    ry = 168
    for lab, val in rows:
        c.text(668, ry, lab, size=12.5, fill=FAINT)
        c.text(668, ry + 22, val, size=14, fill=INK)
        ry += 60
    c.box(668, 542, 308, 100, fill="#fff8e6", outline="#e0b34d", radius=10, width=1.5)
    for i, ln in enumerate([
        "画像本身也是内容：可署名、",
        "可分享、可被别人替换。",
        "换个画像 —— 同一张图就",
        "变成另一个人的教科书。",
    ]):
        c.text(686, 554 + i * 21, ln, size=12.5, fill=BODY)

    # ---- arrow
    c.tri(1026, 384, 11, "right", "#9aa5b4")

    # ---- panel 3: the projection
    c.box(1056, 104, 504, 560, fill="#ffffff", outline=LINE, radius=14, width=1.5)
    c.text(1080, 122, "③ 投影 = 属于他的教科书", size=16.5, fill=INK, bold=True)

    c.box(1080, 152, 456, 220, fill="#f0f7ff", outline="#93b8f0", radius=10, width=1.5)
    c.text(1100, 168, "画像 A（没学过微积分 · 中考）", size=13, fill=BLUE, bold=True)
    chap = [
        ("第 1 章　电流是什么", "教法：水管类比"),
        ("第 2 章　电压与电阻", "教法：水管类比"),
        ("第 3 章　欧姆定律", "教法：水管类比 + 水流动画"),
    ]
    cy2 = 194
    for ttl, m in chap:
        c.text(1100, cy2, ttl, size=13.5, fill=INK)
        c.text(1128, cy2 + 20, m, size=12, fill=FAINT)
        cy2 += 44
    c.text(1100, 330, "跳过：场论推导 —— 先修不满足", size=12.5, fill=RED)

    c.box(1080, 392, 456, 150, fill="#f4f0ff", outline="#b9a4f0", radius=10, width=1.5)
    c.text(1100, 408, "画像 B（物理系本科生）", size=13, fill="#6b46c1", bold=True)
    c.text(1100, 434, "第 1 章　从麦克斯韦方程推导欧姆定律", size=13.5, fill=INK)
    c.text(1128, 454, "教法：场论推导", size=12, fill=FAINT)
    c.text(1100, 482, "跳过：水管类比 —— 该画像下已标注不适用", size=12.5, fill=RED)
    c.text(1100, 506, "先修过高，类比反而造成错误直觉", size=12, fill=FAINT)

    c.rich(1080, 564, "没有唯一的教科书，只有**对某个人的投影**",
           size=13.5, fill=BODY, bold_fill=INK)
    c.text(1080, 596, "同一张图，换一个画像就是另一本书", size=12.5, fill=FAINT)

    # ---- bottom bars
    c.box(40, 684, 1520, 96, fill="#eefaf3", outline="#7cc79b", radius=14, width=1.5)
    c.text(58, 717, "可机械校验", size=15, fill=GREEN, bold=True)
    c.rich(190, 706,
           "**先修缺口**（没学就上） · **循环依赖**（A 先修 B、B 先修 A） · **目标覆盖度**（内容够不够达成本画像的目标）",
           size=13.5, fill=BODY, bold_fill=INK)
    c.rich(190, 730,
           "**禁忌冲突**（该教法在此画像下被标注为不适用） · 符号 / 单位一致性 · 引用是否真实存在",
           size=13.5, fill=BODY, bold_fill=INK)
    c.text(58, 745, "不用投票", size=12, fill=GREEN)

    c.box(40, 796, 1520, 80, fill="#f4f0ff", outline="#b9a4f0", radius=14, width=1.5)
    c.text(58, 821, "两种模式", size=15, fill="#6b46c1", bold=True)
    c.rich(190, 808,
           "**命题 → 收敛模式**：接地语义算出存活集合 → 已确证 / 争议（同一时刻只有一个结论）",
           size=13.5, fill=BODY, bold_fill=INK)
    c.rich(190, 829,
           "**教法 → 并存模式**：不做唯一裁决，按条件索引 —— 对谁有效、对谁不适用、证据多强",
           size=13.5, fill=BODY, bold_fill=INK)
    c.rich(190, 850,
           "**知识要收敛，教法要并存**：强行给教法排出唯一最优，就是在制造教条",
           size=13.5, fill=BODY, bold_fill=INK)
    return c.save("fig3-projection.png")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
