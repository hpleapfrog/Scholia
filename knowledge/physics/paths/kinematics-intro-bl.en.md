---
id: kb:physics:path-kinematics-intro-bl
type: 路径
title: "Kinematics intro (below grade level)"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 低于年级水平（BL）
  目标: 能用位置-时间图描述一个简单运动
  条件: 学生能描述方向与位置
outcomes:
  - o1: 能说出「描述运动必须先指定参考系」，并能对同一运动给出两个参考系下的描述
  - o2: 能区分速率与速度（速度含方向），并指出日常用语的差异
  - o3: 能画出一个简单运动的位置-时间图
  - o4: 能从图上读出斜率对应速度、斜率方向对应运动方向
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-021, ev-022, ev-023]
license: CC-BY-SA-4.0
---

> **English version of [`运动学入门-BL.md`](运动学入门-BL.md).**

## Arrangement

| # | Step | Entry | Covers | Time |
|---|---|---|---|---|
| 1 | Establish a reference frame | [参考系 · BL：多参考点观察](../methods/frame-bl-multi-viewpoint.en.md) | o1 | 15 min |
| 2 | **Diagnose**: is a frame "the background"? | [误解：参考系当成背景](../misconceptions/frame-as-background.en.md) | o1 | 5 min |
| 3 | Everyday usage of speed vs velocity | [速度与速率 · BL/OL：日常用语切入](../methods/speed-bl-ol-everyday-language.en.md) | o2 | 15 min |
| 4 | From situation to position-time graph | [位置-时间图 · BL/OL：情境叙事](../methods/ptgraph-bl-ol-narrative.en.md) | o3, o4 | 20 min |

**Total 55 min.**

> [!NOTE]
> **Step 2 is not optional.** Why it appears is in the "禁忌冲突" section below —
> the known failure mode of the step-1 teaching method is the typical risk for this level's students.
>
> **It also covers `o1`**: the diagnostic demonstration asks the same questions again, which is the means to check whether "a frame is not the background" is really established.

## Target

`能用位置-时间图描述一个简单运动` (can describe a simple motion with a position-time graph)

## Argument

### P1 · This sequence achieves the target (no attack yet)

- **Claim**: arranging as `reference frame → speed → position-time graph` achieves "describe a simple motion with a position-time graph"
- **Premise**: the step-4 teaching method directly produces the target behavior (students draw and interpret the graph); steps 1–3 provide its prerequisites
  (ev-021 / ev-022 / ev-023)
- **Reasoning**: the actions the target requires **coincide** with step 4's output; the first 3 steps are what the textbook specifies for this level
  (marked `[BL]` / `[BL][OL]`), not my own picks
- **Evidence**: ev-021, ev-022, ev-023
- **Attacked**:
  - **The time allocation has no basis.** 55 min is my estimate from the step count — the textbook **gives no time suggestion at all**
  - **Step 2's placement is my judgment.** The textbook gives the Misconception demonstration but **does not tie it to any teaching sequence**
  - **"on the prerequisite chain" ≠ "pedagogically effective".** A sensible order ≠ students actually learning
- **Attribution**: @hpleapfrog · 2026-10-05
- **To be added**: actual class time; pre/post data

> [!IMPORTANT]
> **In this path, what is the textbook's and what is mine must be separated:**
>
> | Content | Source |
> |---|---|
| the practice of the 4 steps themselves | **textbook** (`[BL]` / `[BL][OL]` marks) |
| the order of the three | **my design judgment** — the textbook does not order them |
| the 55-min duration | **my estimate**, no basis |
| step 2 inserted between 1 and 3 | **my design judgment** |
>
> **The textbook gives the parts; the assembly is mine.**

## Self-check

### ✅ Mechanically verified (by `tools/kbcheck.py`, no longer a person's say-so)

- [x] **Prerequisite gap**: `参考系` (prereq = none) → `速度与速率` (prereq = 参考系) →
      `位置-时间图` (prereq = 速度与速率). **All three are within this path, no gap.**
      The verifier checks against the prerequisite graph one by one and passes
- [x] **Circular dependency**: the prerequisite graph is acyclic. The verifier runs cycle detection and passes

> [!IMPORTANT]
> These two **were originally manual assertions** ("I say there's none, so there's none"). After the `知识点` layer was introduced,
> `先修` edges connect to knowledge points and no longer bind the level, so the verifier can actually check them.
>
> The verifier also **rejects** connecting a `先修` edge to a 教法 entry — verified by an injected error.

### ✅ Mechanically verified (target coverage) — the last item filled in

This item used to be manual judgment only ("≈ 1.0"). Now the path declares `outcomes` in front-matter,
and the arrangement table marks `覆盖` per step, so **the verifier computes the exact coverage**:

| Outcome | Content | Covered by which step |
|---|---|---|
| `o1` | describing motion requires naming a reference frame first | step 1, step 2 (diagnostic re-ask) |
| `o2` | distinguish speed and velocity | step 3 |
| `o3` | draw a position-time graph | step 4 |
| `o4` | read the slope as velocity, slope direction as motion direction | step 4 |

**Coverage 4/4 = 100%, no uncovered outcome.**

> [!IMPORTANT]
> **"An uncovered outcome" is an error, not a hint** — it means the path fails its own declared target.
> The verifier fails it outright.

### ✅ Now decidable (禁忌冲突) — Issue #13 fulfilled

After splitting `禁忌` from `风险`, this item went **from "cannot fill" to "can fill"**:

| Teaching method used by the path | Its `禁忌`'s marked inapplicable audience | Hits the BL profile? |
|---|---|---|
| [参考系 · BL](../methods/frame-bl-multi-viewpoint.en.md) | students outside this level (**weak**) | ❌ not hit |
| [速度与速率 · BL/OL](../methods/speed-bl-ol-everyday-language.en.md) | students outside this level (**weak**) | ❌ not hit |
| [位置-时间图 · BL/OL](../methods/ptgraph-bl-ol-narrative.en.md) | students outside this level (**weak**) | ❌ not hit |

**Conclusion: no 禁忌 conflict.**

> [!WARNING]
> **But the judgment strength is weak.** The basis of all three `禁忌` is only the single **weak** evidence "the textbook gives a separate practice for each level" —
> there is no direct evidence that "this practice does not work for other levels".
>
> **Decidable ≠ reliable.** This item can now be filled, but the filled conclusion is light.

### ⚠️ Decidable ≠ mechanically verifiable

`禁忌` is a natural-language table. The verifier cannot read the relation between "students outside this level" and the path profile "BL",
so **this item still requires manual judgment**.

To mechanize it, `禁忌` must move from prose into a **structured field** (e.g. `contraindications: [BL, OL]`).
**That is the next step, not this one.**

## Three schema problems exposed by the self-check

The purpose of building this path was to stress the schema. It hit three, **and all three are now resolved**:

| # | Problem | Status |
|---|---|---|
| 1 | `edges.先修` was empty repo-wide | ✅ **resolved** — the `知识点` layer was introduced, edges have somewhere to hang |
| 2 | `禁忌` semantics were mixed (禁忌 vs 风险) | ✅ **resolved** — split into two subsections with evidence strength (Issue #13) |
| 3 | `先修` granularity mismatch | ✅ **resolved** — `先修` connects only knowledge points, no longer binds the level |

## Actual gains from the split

| Self-check item | Initially | Now |
|---|---|---|
| prerequisite gap | ⚠️ manual assertion | ✅ **machine check** |
| circular dependency | ⚠️ manual assertion | ✅ **machine check** |
| 禁忌 conflict | ❌ **cannot fill** | ✅ **decidable** (but weak strength, still manual) |
| target coverage | ⚠️ manual judgment | ⚠️ **still manual judgment** |

**Three of the four now have a basis; only "target coverage" has no mechanism at all.**

### Problem 1 ✅ resolved (plan A): `edges.先修` empty repo-wide → the first two self-checks had no graph to check

This path declared a `参考系 → 速率 → 图像` progression, but that was **prose I wrote in the path body**,
**not read from the entries' `edges.先修`** — because all 23 entries' `先修` were `[]`.

Consequence:

| Self-check item | Should be | Actually was |
|---|---|---|
| prerequisite gap | check the graph, report if there's a gap | **I say there's none, so there's none** |
| circular dependency | check the graph, report if there's a cycle | **I say there's none, so there's none** |

**Both degenerated into manual assertions.** In the design they were the "mechanically verifiable" parts; now they were not.

### Problem 2: the `禁忌` field mixed two different things

`FORMAT.md` defines `禁忌` as "**who it does not apply to**". But in the 7 newly written 教法 entries,
the `禁忌` column actually held "**where this practice backfires**" — two kinds:

| Type | Example | Is it "who it does not apply to"? |
|---|---|---|
| **audience 禁忌** | friction analogy "not for physics majors" | ✅ yes |
| **risk / failure mode** | reference-frame BL "students understand a frame as background" | ❌ **no** — it says what goes wrong with the practice, not who should not use it |

**Root cause of the mixing**: the textbook's `Caution students…` sentence is a **risk**, and at the time "risk" had no field to go in,
so I stuffed it into the only relevant spot — `禁忌`. **That was my modeling compromise then, not the textbook's fault.**

Result: the path's "禁忌 conflict" check asks "is this teaching method marked inapplicable under this profile",
and my field had no such information → **cannot fill**.

### Problem 3 ✅ resolved (plan A): `先修` **granularity** mismatch (the most fundamental)

I found this only when trying to fix problem 1, and it is more fundamental than the first two.

The repo's entries are **(knowledge point × level)** combinations:

```
教法/参考系-BL-多参考点观察.md
教法/参考系-OL-提问引导.md
教法/参考系-AL-生成式下定义.md     ← the same knowledge point, three files
```

But "reference frame precedes speed" is a relation **between knowledge points**, **independent of level**.

So `edges.先修` fell into a dilemma:

| If written this way | Consequence |
|---|---|
| `位置时间图-BL 先修 → 速度与速率-BL` | **binds the level into the prerequisite relation too**: BL's graph lesson requires BL's speed lesson. Then when an AL student picks across levels, this edge makes no sense |
| hang it on one level only (e.g. only OL) | the other two levels' graphs break, and the "prerequisite gap" check comes and goes |

**Root cause**: `先修` is a relation at the **knowledge-point** level, while `edges` hang on **entries (knowledge point × level)**.
**The two granularities do not match.**

This may mean the repo lacks a layer of abstraction: **knowledge-point nodes separated from 教法 entries** —
prerequisites connect knowledge points, 教法 hang under knowledge points, and level is just an attribute of 教法.

> [!IMPORTANT]
> **This must be answered before fixing problem 1.** Otherwise the edges are hung in the wrong place —
> the graph looks present, but it checks the wrong thing — **more dangerous than no graph**.
>
> **Resolved on 2026-10-05 per plan A**: a `知识点` layer was added, and `先修` connects only knowledge points.
> The two "✅ mechanically verified" items in this entry are the result after resolution.

## Current status of the two problems

| # | What | Status |
|---|---|---|
| 3 → 1 | added the `知识点/` directory; `先修` connects only knowledge points; `教法` gained a `knowledge_point` field; the verifier runs cycle detection and prerequisite-gap checks | ✅ **implemented** |
| 2 | split `禁忌` (who it does not apply to) from `风险` (failure mode) | ❌ **not implemented** |

Problem 2 is pending because it requires changing `FORMAT.md`, `tools/kbcheck.py`, **and the `禁忌` columns of 9 教法 entries** at once.

> [!IMPORTANT]
> **These three problems are not me writing the path wrong — the object model was not finished.**
> Each 教法 entry is self-consistent on its own; connected into a path, the gap shows.
> **This is exactly the value of the path object — it is the schema's stress test.**

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry; the self-check exposed two schema problems: missing `先修` edges and mixed `禁忌` semantics | Issue #8 pilot extension | @hpleapfrog |
| 2026-10-05 | **the first two self-checks became mechanical**: after plan A introduced the `知识点` layer, `tools/kbcheck.py` runs cycle detection and prerequisite-gap checks | [Issue #11](https://github.com/hpleapfrog/Scholia/issues/11) | @hpleapfrog |
