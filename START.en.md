# Start Here

> 中文 → [**START.md**](START.md)

> [!NOTE]
> **This page is for people who want to learn something — not for contributors.**
> You don't need to know how this library is built to use it.

> [!TIP]
> **Are you an AI or a program?** Skip this page — go to [`llms.txt`](llms.txt) and parse the
> machine entry [`index.json`](index.json). There it says **what must not be quoted as fact**.

## What this is (in one paragraph)

**It is a physics collection you can verify yourself.**

Every entry tells you two things: **what it says**, and **why it says so** (which book, which
page, which clause).

**It is not a complete textbook yet** — section 3 below honestly states what's here and what isn't.

## 1. Which kind of person are you?

| You are | Go to |
|---|---|
| **A student** wanting to understand a concept | find the entry in the **topic index** below, then read its `## 定义` / `## 陈述` |
| **A teacher** looking for a way to teach it | under each concept hang several **`教法` (methods)** — different ways to teach the same concept, by audience |
| **Someone who found an error** | go straight to [Contributing](CONTRIBUTING.md). **"You're wrong" is the most welcome thing here** |
| **Someone who wants to reuse it** | knowledge content is [CC BY-SA 4.0](LICENSE) — **free to reuse, attribution required** |

## 2. Topic index: what to learn, click here

**Physics** — read **in order**; each entry's "prerequisites" are its predecessors:

| Topic | Entries (in suggested order) |
|---|---|
| **Intro kinematics** | [Reference frames](knowledge/物理/知识点/参考系.md) → [Speed & velocity](knowledge/物理/知识点/速度与速率.md) → [Position–time graphs](knowledge/物理/知识点/位置-时间图.md) → [Acceleration](knowledge/物理/知识点/加速度.md) |
| **Force & Newton's laws** | [Force (HS)](knowledge/物理/知识点/力-高中.md) → [Inertia](knowledge/物理/知识点/惯性.md) → [Newton's 2nd](knowledge/物理/知识点/牛顿第二定律.md) → [Newton's 3rd](knowledge/物理/知识点/牛顿第三定律.md) |
| **Gravitation & the sky** | [Kepler's laws](knowledge/物理/知识点/开普勒定律.md) → [Law of universal gravitation](knowledge/物理/知识点/万有引力定律.md) |
| **Energy** | [Work & power](knowledge/物理/知识点/功与功率.md) → [Conservation of mechanical energy](knowledge/物理/知识点/机械能守恒.md) |
| **Waves & sound** | [Waves](knowledge/物理/知识点/波.md) → [Speed of sound & frequency](knowledge/物理/知识点/声速与频率.md) |
| **Light** | [Reflection](knowledge/物理/知识点/光的反射.md) · [Refraction](knowledge/物理/知识点/光的折射.md) · [EM spectrum](knowledge/物理/知识点/电磁波谱.md) |
| **Electricity** | [Resistance & Ohm's law](knowledge/物理/知识点/电阻与欧姆定律.md) |
| **Atoms** | [Atomic structure](knowledge/物理/知识点/原子结构.md) |
| **Middle school** | [Force & motion (MS)](knowledge/物理/知识点/力与运动-初中.md) |

**Common mistakes**, collected in one place (6 of them):

[Current vs. electron flow](knowledge/物理/误解/电流方向与电子流向混淆.md) ·
[Frame of reference as "background"](knowledge/物理/误解/参考系当成背景.md) ·
[Moving objects naturally slow down](knowledge/物理/误解/运动物体自然慢下来.md) ·
[Visible vs. invisible radiation](knowledge/物理/误解/可见光与不可见辐射有本质不同.md) ·
[Waves push matter along](knowledge/物理/误解/波把物质一起推走.md) ·
[Confusing G and g](knowledge/物理/误解/混淆G与g.md)

**Want a full learning path**: [Intro kinematics (BL)](knowledge/物理/路径/运动学入门-BL.md) —
it tells you **which things you'll be able to do** and the material for each step.

> Other subjects ([Geography](knowledge/地理/README.md) · [Science](knowledge/科学/README.md) ·
> [Life · travel rules](knowledge/生活/README.md)) still have very little.

**Geography (6, all errata from Hong Kong textbooks)** —
[Map provenance / missing approval number](knowledge/地理/命题/勘误-关于本书地图出处.md) ·
[Systematic contour-labeling error](knowledge/地理/命题/勘误-等高线标注系统性错误.md) ·
[Road length typo](knowledge/地理/命题/勘误-道路长度漏字.md) ·
[River basin vs. river](knowledge/地理/命题/勘误-河盆应为河流.md) ·
[Cross-section terminology](knowledge/地理/命题/勘误-横切面术语.md) ·
[Tsing Wan map excerpt misreference](knowledge/地理/命题/勘误-清水湾地图摘录.md)

**Science (1)** — [Unreliable data source on an earthquake map](knowledge/科学/命题/勘误-地震分布图数据来源.md)

**Life · travel rules (5)** —
[Beijing metro carry-on size/weight limits](knowledge/生活/命题/携带物品的尺寸与重量上限.md) ·
[Involuntary refunds & changes must be free](knowledge/生活/命题/非自愿退票与变更不得收费.md) ·
[Overbooking: volunteers first](knowledge/生活/命题/超售必须先征集自愿者.md) ·
Official docs: [Beijing metro passenger rules](knowledge/生活/资源/北京市轨道交通乘客守则.md) ·
[Air passenger service regulations](knowledge/生活/资源/公共航空运输旅客服务管理规定.md)

> These three subjects have **very little** (12 entries together), listed only so you know they exist.

**Medicine · clinical evidence (2)** —

| Entry | Evidence |
|---|---|
| [For ARDS patients, low tidal volume lowers mortality](knowledge/医学/命题/ARDS低潮气量通气.md) | an N=861 randomized trial |
| [For OSA, adult PAP titration has guideline-specified start/step/target rules](knowledge/医学/命题/睡眠呼吸暂停PAP调定.md) | AASM 2008 guideline text (checked clause by clause) + a multicenter RCT (HomePAP) |

> [!CAUTION]
> **These two say "what a study/guideline concluded or specified", not "what you should do".**
> This library **gives no medical advice for any specific patient** — setting a ventilator for a
> particular patient needs diagnostic data and qualified staff, beyond what it can answer.
> The OSA entry **does record the guideline's operational parameters**, but always phrased as
> **"the guideline specifies X"**, with a disclaimer block at the very top of the body.
> See the [medicine subject note](knowledge/医学/README.md).

## 3. What this library **has** and **doesn't**

> [!WARNING]
> **Said up front so you don't waste time.**
>
> Mapped against Chinese senior-high (PEP) chapter-level topics, **nearly half have not a single
> concept here**:
>
> | | chapter-level topics | share |
> |---|---|---|
> | ✅ covered | 5 | 19% |
> | 🟡 partial | 10 | 37% |
> | ❌ **none** | **12** | **44%** |
>
> **Missing entirely**: momentum · circular motion · electrostatics · electromagnetic induction ·
> AC · thermodynamics · nuclear physics.
>
> Full mapping in the [coverage table](knowledge/物理/覆盖度/README.md).

**One more thing to know**: most `教法` (methods) here are compiled from **OpenStax *Physics* — a
US high-school textbook**. Its content is reliable, but **this library has no data on how well it
works in a Chinese classroom**.

## 4. **How to read an entry** (the most useful section)

### Six words first (you'll see them in paths)

| You'll see | It means | How to use it |
|---|---|---|
| `知识点/` | a **concept** | **start reading here**, like a textbook section |
| `命题/` | a **true/false claim** | a conclusion + why it holds |
| `教法/` | a **way of teaching** a concept | teachers pick methods; students can read "how to understand it" |
| `误解/` | **where many people go wrong** | to check whether you think that too |
| `资源/` | external material (simulations, official docs) | supplementary |
| `路径/` | a **learning order** | like a syllabus: "learn A, then B" |

**These are the library's internal names; you don't need to memorize them.** They appear only in **URL paths**.

### An entry has two halves

| Section | For whom | What to do |
|---|---|---|
| **the `> [!TIP]` at the very top** | **you** | **what you'll be able to do after reading** — check it first to decide whether to keep going |
| `## 定义` / `## 陈述` / `## 做法` | **you** | **start reading here** |
| `## 关联` | **you** | follow it to prerequisites and related entries |
| `## 禁忌` / `## 风险` (methods only) | **you** | check "who it's not for" before using |
| `## 论证` | **reviewers** | **skippable** — the bookkeeping of "why this holds" |
| `## 变更记录` | **reviewers** | skippable |

> **So to read a concept**: look at the top line "after this you should be able to…"; if you want
> to know **why to care**, read `## 定义`; to learn **how to teach it**, click the method linked in
> `## 关联`; **everything from `## 论证` down can be skipped.**

**Three more symbols — don't panic when you see them**:

| You see | It means |
|---|---|
| an id like `(ev-039)` | a **source id** — a row in [`evidence/README.md`](evidence/README.md); **click to see which book, which page** |
| `[BL]` / `[OL]` / `[AL]` | textbook **level markers**: Below Level / On Level / Advanced |
| "prerequisite" | what you should already know **before** this |

**English originals**: entries quote English sentences from the textbook. **The quote is for
provenance, not for you to read** — **there is always a Chinese gloss nearby** (usually right
after). **If you find a passage without one, report it.**

## 5. A complete example

Say you want to understand **why "deceleration" isn't used in physics**. Open [Acceleration](knowledge/物理/知识点/加速度.md):

1. **Above `## 定义` is a table** (GitHub auto-renders the top of the file as a table) reading
   "**Goal**: compute acceleration with `a = Δv/Δt` and explain the sign–direction relation" —
   **check what you'll learn first**
2. Read `## 定义`: the formula, units, and **why "deceleration" isn't used**
3. In that `[!IMPORTANT]` box is an **English original**, immediately followed by a Chinese gloss —
   **the Chinese is for you; the English is the source**
4. In `## 关联` you can click [Speed & velocity](knowledge/物理/知识点/速度与速率.md) (its prerequisite)
5. From `## 论证` down **you can skip everything**, unless you want to know who attacked it

**That's a complete reading path.** Other entries have the same structure.

## 6. What to do when you find an error

**"This library welcomes that sentence the most."** And it **doesn't require you to know Git**:

| Your skill | What to do |
|---|---|
| You can type | open an [Issue](https://github.com/hpleapfrog/Scholia/issues/new) saying **which file, which sentence, why it's wrong** |
| You can edit files | open a [Pull Request](CONTRIBUTING.md) |
| You're just unsure | open a [Discussion](https://github.com/hpleapfrog/Scholia/discussions) (**changes no conclusions**, just talk) |

> [!IMPORTANT]
> **"Well-sourced" matters more than "right".**
>
> You don't need to be an expert. Give a **source** (which book, which page) or **a counterexample**,
> and this library is obliged to respond. **It records every correction, including its own mistakes.**

## Curious how this library works

That's another track, for contributors: [README](README.md) (mission & status) ·
[FORMAT](FORMAT.md) (format spec) · [CONTRIBUTING](CONTRIBUTING.md) (how to take part).
