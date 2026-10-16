# Daily life · Travel rules

> [!IMPORTANT]
> **This subject records "rules", not "procedures". This boundary was tested by two probes, not designed up front.**
>
> It began with two questions: **"what about the knowledge of taking the subway?"** and **"add how to fly too"**.
> Both times I treated them as **stress tests of the framework** — **write what can be verified, and record what doesn't fit**.
>
> **Conclusion: the repo can hold "rules", but not "doing".** The reason is in section III below.

> **English version of [`README.md`](README.md).**

## Current state

| Entry | Type | Status | Source |
|---|---|---|---|
| [《北京市轨道交通乘客守则》（官方文件）](资源/北京市轨道交通乘客守则.en.md) | 资源 | 有效 | `ev-043` |
| [北京地铁对乘客携带物品设有硬性尺寸与重量上限](命题/携带物品的尺寸与重量上限.en.md) | 命题 | 待审 | `ev-043` |
| [《公共航空运输旅客服务管理规定》（交通运输部令 2021 年第 3 号）](资源/公共航空运输旅客服务管理规定.en.md) | 资源 | 有效 | `ev-044` |
| [非自愿退票与承运人原因的非自愿变更，都不得向旅客收费](命题/非自愿退票与变更不得收费.en.md) | 命题 | 待审 | `ev-044` |
| [超售时，未经征集自愿者程序不得拒绝旅客登机](命题/超售必须先征集自愿者.en.md) | 命题 | 待审 | `ev-044` |
| [承运人修改运输总条件后，不得把限制旅客权利的新条款适用于修改前已购票的旅客](命题/修改运输总条件不得追溯适用于已购票旅客.en.md) | 命题 | 暂定确认 | `ev-044` |
| [承运人等对旅客投诉，须在 10 个工作日内给出含解决方案的处理结果，不予受理须说明理由](命题/投诉须在10个工作日内给出含解决方案的处理结果.en.md) | 命题 | 暂定确认 | `ev-044` |
| [托运行李应与旅客同机运送；非旅客原因延误时，旅客可要求免费直接送达](命题/托运行李应与旅客同机运送且非旅客原因延误可要求免费直接送达.en.md) | 命题 | 暂定确认 | `ev-044` |

**8 entries · 2 official documents · 6 rules.**

> [!NOTE]
> **From 2026-10-13, ev-044's verification depth was upgraded from "located only" to "full text"** —
> this repo opened the Ministry of Transport page and checked all ten chapters article by article; the three
> propositions added afterwards (the retroactivity ban, the complaint deadline, baggage direct delivery) all come
> from that full-text check. **Still outstanding is "a version-detection mechanism"**: this regulation
> **carries no version number**, only a document number and an effective date, and this repo has no way to know
> whether it has been amended.

## I. What was held

| Object type | Why it was held |
|---|---|
| **`资源`** | both documents are **officially published, clickable, normative documents with a document number or effective date**. Unlike the two PhET sims already here — **they are for "looking up", not for "learning"** |
| **`命题`** | "what the official document stipulates" is a **statement with a truth value, checkable item-by-item**, and **exactly attackable** — the attack point is **timeliness** |

**Both used the "official document clause" evidence type** (it was already listed in the threshold of `evidence/README.md`,
but **had never been used once** before 2026-10-05).

## II. What doesn't fit: **"doing"**

Both times I tried writing the procedure as a `路径`. **Both times the validator rejected it**:

| Probe | Steps | Steps that name no object |
|---|---|---|
| **taking the subway**: from entering to exiting | 4 | steps **3, 4** ("check the direction before boarding", "exit at the station") |
| **flying**: from check-in to arrival | 4 | steps **2, 3, 4** ("security", "wait at the gate", "arrival and baggage claim") |

The validator's exact words (identical both times):

```
x ...: step N "…" **does not connect to any knowledge object**
  (the `条目` column must point to an entry that exists in the repo)
  —— a 路径 is "an arrangement of 知识点"; a step that names no object is not a 环节
```

**This is not "no suitable entry found", but "there is no such object type in the repo".**

**Neither probe remains in the repo** (the repo's gate is kbcheck all-green),
**but their failure messages remain here** — that is the use they can serve.

## III. Why this is not a flaw: **the scarcity criterion**

> [!IMPORTANT]
> **The criterion is not mine — the two regulations gave it themselves.**
>
> | Document | What it requires |
> |---|---|
> | 《北京市轨道交通乘客守则》 | the **behavioral rules** to follow in each area of the station |
> | 《公共航空运输旅客服务管理规定》**Article 28** | the airport shall **set up signage guidance** in key areas such as **check-in, baggage check-in, security, customs, border control, boarding gate, transfer corridor** |
>
> **"Check-in → security → boarding" — the regulation guarantees this is visible on-site.**
>
> **But** "no fee for involuntary refunds", "refund within 7 working days", "no boarding without the volunteer-solicitation process"
> **— these appear on no sign.**

**The repo's mission is "remove noise, hold real information". This contrast is the criterion:**

| | Visible on-site | Not visible on-site |
|---|---|---|
| example | where check-in is, how to get through security, where the gate is | **why** involuntary refunds are free, **within how many days** a refund must arrive, **what rights you have** when overbooked |
| nature | **noise** (everywhere, and the regulation guarantees availability) | **real information** (scarce, and no one is obliged to tell you) |
| the repo's stance | **do not repeat** | **hold it, with the source article number** |

## IV. How this boundary was established

After the **first probe (subway)**, I found the definition of `路径` had never been checked —
`FORMAT.md` says "路径 = an arrangement of 知识点", but **no check required it to actually arrange 知识点**.

**That round added `check_path_steps`**: a 环节 must connect to a real object.
**It did not misfire** on the one real 路径 that existed (its 环节 pointed to `教法` and `误解`).

**But then there was only one sample**, so in [Issue #43](https://github.com/hpleapfrog/Scholia/issues/43) I wrote:

> **Don't change the structure on one sample. Until a second sample appears, A (acknowledge the boundary) is also a perfectly acceptable answer.**

**The second probe (flying) was that second sample.** The failure mode was **identical in shape and more thorough**.

**So the decision: choose A — acknowledge the boundary, add no new object type.**
The reason is written into the "what the repo does **not** hold" section of [`FORMAT.md`](../../FORMAT.en.md).

> [!NOTE]
> The criterion and the three probes (including the ventilator) are summarized in
> [decision record: the boundary of procedural knowledge](../../docs/decisions/procedural-knowledge-boundary.en.md).

## V. Two things still noted, not yet changed

| # | Thing | Status |
|---|---|---|
| 1 | **`已失效` has never been triggered** — the repo needs version detection (rules change), **but has no mechanism** | noted in [命题：携带物品的尺寸与重量上限](命题/携带物品的尺寸与重量上限.en.md) |
| 2 | **the repo cannot verify whether the source page has been revised** — both documents have **no version number**, only a document number / effective date | noted in the `论证` of the two `资源` |

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-13 | **upgraded ev-044's verification depth to full text**; added three propositions — the retroactivity ban on Conditions of Carriage (§7), the 10-working-day complaint deadline (§52), and checked baggage travelling with the passenger plus free direct delivery (§39/§40). All three are rules that "cannot be seen on site and hand the passenger an option to claim" | ev-044 already registered; topic selected against the subject boundary after this repo checked all ten chapters article by article | @hpleapfrog |
| 2026-10-05 | established the subject (first probe: subway); added `check_path_steps` | user asked "what about the knowledge of taking the subway?" | @hpleapfrog |
| 2026-10-05 | **added aviation (second probe)**; from the two samples **set the boundary and wrote it into the spec**, closing Issue #43 | user asked "add how to fly too" | @hpleapfrog |
