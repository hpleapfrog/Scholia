---
id: kb:physics:kp-momentum-impulse
type: 知识点
title: "Momentum and impulse"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  范围: conservation of momentum
edges:
  先修: ["[知识点：牛顿第二定律](newtons-second-law.en.md)"]
  支持: []
  攻击: []
evidence: [ev-045]
license: CC-BY-SA-4.0
---

> **English version of [`动量和冲量.md`](动量和冲量.md).**

> [!TIP]
> **After reading this entry you should** be able to compute momentum and impulse with `p = mv` and `I = FΔt`,
> and to explain clearly why the "two forms of Newton's second law" are the same thing.

## Definition

**Momentum**: `p = m·v`

- **a vector** — its direction is the same as the velocity's direction. **Both magnitude and direction must be carried**
- unit `kg·m/s`

**Impulse**: `I = F·Δt` (the accumulation of force over time)

- also a **vector**, with the direction of the force

**The impulse–momentum theorem**: `Δp = I = F·Δt`

> [!IMPORTANT]
> **Newton's second law has two forms, and they are the same thing (ev-045):**
>
> | Form | Expression | What it says |
> |---|---|---|
> | the familiar one | `F = m·a` | the relation between force **and acceleration** |
> | the other one | `F = Δp / Δt` | the relation between force **and the rate of change of momentum** |
>
> **The textbook's `[AL]` hint explicitly requires "write out both forms and explain how one is derived from the other."**
>
> **Why this deserves its own teaching-method entry**: `F = Δp/Δt` is **the hinge between the momentum chapter and Newton's laws**.
> Without it, momentum looks like a set of new symbols appearing out of nowhere.

> [!NOTE]
> **The three contrasts the textbook names at this node (ev-045's glossary):**
>
> | Terms | What is being contrasted |
> |---|---|
> | `vector` / `scalar` | momentum's **direction** must not be dropped |
> | `mass` / `velocity` | "big and fast" carries more momentum than "small and slow" — **both factors count** |
> | `change in momentum` / `impulse` | one is a **result**, the other a **process quantity** |

## Relations

| Object | Entry | Note |
|---|---|---|
| prerequisite · knowledge point | [Newton's second law](newtons-second-law.en.md) | the textbook requires reviewing inertia, Newton's laws, and `F = ma` first |
| teaching method · AL | [momentum and impulse · AL: the two forms of Newton's second law](../教法/momentum-al-two-forms.en.md) | the most crucial step of this node |
| downstream · knowledge point | [conservation of momentum](conservation-of-momentum.en.md) | where this chapter lands |

> [!TIP]
> **Why this entry deserves to stand alone**: it is **the starting point of this repo's "force × time" main line**,
> while the existing [work and power](work-and-power.en.md) is **on the "force × displacement" side**.
>
> | | Multiplied by | Yields | Corresponds to |
> |---|---|---|---|
> | **work** | **displacement** | change in energy | [work and power](work-and-power.en.md) → [conservation of mechanical energy](conservation-of-mechanical-energy.en.md) |
> | **impulse** | **time** | change in momentum | **this entry** → [conservation of momentum](conservation-of-momentum.en.md) |
>
> **The two main lines appear symmetrically in this repo for the first time.**

## Argument

### K22 · Why listed separately (no attack yet)

- **Claim**: momentum and impulse deserve to be separate knowledge points
- **Premise**: the textbook devotes a section to it, containing **7 teaching hints** (5 of them tiered) and **12 terms** (ev-045)
- **Reasoning**:
  1. it introduces **two new vectors** (`p` and `I`), neither of which exists in the current nodes
  2. it gives **the second form of Newton's second law**, which is the **substantive connection point** to the existing node [Newton's second law](newtons-second-law.en.md)
  3. it is the starting point of the "force × time" main line, **symmetric** with the existing "force × displacement" main line
- **Evidence**: ev-045
- **Attacked**: **its teaching hints are only 7, with 747 characters of tiered content**, making it one of the thinner nodes in this repo; and **the applications of the impulse–momentum theorem (collisions, impacts) live mostly in worked examples**, which are not part of Teacher Support — **this repo does not treat worked examples as sources of teaching methods**
- **Response**: **the thinness is real.** The "Definition" section of this entry therefore writes only **what the textbook explicitly states**,
  and adds no worked examples on its behalf. **Thin is not the problem; writing something into existence that isn't there is.**
- **Attribution**: @hpleapfrog · 2026-10-05
- **To be added**: collision-type worked examples (no source in this repo); **angular momentum** (appears in the textbook's glossary, not built in this repo)

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (#8 batch conversion · batch 7: the momentum chapter) | Issue #8 | @hpleapfrog |
