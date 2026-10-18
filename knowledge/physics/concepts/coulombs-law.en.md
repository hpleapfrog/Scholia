---
id: kb:physics:kp-coulombs-law
type: 知识点
title: "Coulomb's law"
status: 待审
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 物理
  学段: 高中
  适用: students who know there are two kinds of charge and are starting to compute electric forces
  条件: holds only for point charges (or uniform spheres) at rest relative to each other; no fields or potential (separate entries)
edges:
  先修: ["[Electric charge](electric-charge.en.md)"]
  支持: []
  攻击: []
evidence: [ev-085]
license: CC-BY-SA-4.0
---

> **English version of [`库仑定律.md`](库仑定律.md).**

> [!TIP]
> **After reading this entry you should** be able to compute the force between two charges with `F = k q₁q₂ / r²`, and say where it is like Newton's law of gravitation and where it is not

## Definition

**Coulomb's law** gives the magnitude and direction of the electrostatic force between two charged objects:

```
F = k q₁ q₂ / r²
```

- `q₁`, `q₂` go in **with their signs**: a positive result means **repulsion**, a negative result **attraction**
- `k` is **Coulomb's constant**: `k = 8.99 × 10⁹ N·m²/C²`
- the force is **along the line joining the two centres**; `r` is the distance between the **centres** of the spheres
- it is an **inverse-square law**: double the distance and the force becomes **1/4**; triple it and it becomes **1/9**

| Compared with Newton's gravitation | Coulomb's law | Universal gravitation |
|---|---|---|
| distance dependence | `1/r²` | `1/r²` |
| size of the constant | `k ≈ 8.99×10⁹` | `G ≈ 6.67×10⁻¹¹` (**much smaller**) |
| kinds of "charge" | **two** (positive/negative): attract or repel | **one** (mass): **always attractive** |

> [!IMPORTANT]
> **"At rest" and "point charges" are applicability conditions, not decoration.**
>
> The textbook states: `Note that Coulomb's law applies only to charged objects that are not moving with respect to each other.`
>
> For a **uniformly charged sphere**, from the outside the effect is **as if all the charge sat at the centre** — so measuring from centre to centre is legitimate.
> Checking these two conditions before substituting numbers matters more than the arithmetic.

> [!NOTE]
> **Why do we hardly feel electric forces in daily life, only gravity** — even though electric forces are far stronger?
>
> The textbook leaves this question for advanced students: `Ask why the law of force between electrostatic charge was discovered after that of gravity if gravity is weak compared to electrostatic forces.` (ev-085)
>
> The key is the third row above: **there are two kinds of charge but only one kind of mass**. Positive and negative charges almost completely **cancel in pairs** in macroscopic objects,
> while there is no "negative mass" to cancel gravity.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Electric charge](electric-charge.en.md) — the two kinds of charge and "like repels, unlike attracts" are its premise |
| Structural analogy | [Universal gravitation](universal-gravitation.en.md) — both inverse-square, with "charge" in the role of "mass" |
| Follow-up | [Electric field](electric-field.en.md) — rewriting Coulomb's force as a "field" via `E = F / q` |
| Recorded gap | **"Preventing and using static electricity"** (PEP B3 §9.4) is not built yet |

## Argument

### K1 · Why the prerequisite points at "charge" and nowhere else (no attack yet)

- **Claim**: the cognitive prerequisite of Coulomb's law is electric charge; "gravitation" and "vectors" are merely teaching preparation
- **Premise**: the law's variables are the two charges `q₁`, `q₂`, and its sign rule (positive repels, negative attracts) rests directly on "two kinds of charge" (ev-085);
  the chapter opening's review list asks for **universal gravitation** and **vectors** (ev-083)
- **Reasoning**:
  1. without the concept of charge, none of the law's symbols can be defined — a dependency at the level of definition
  2. the textbook writes gravitation and vectors as **review hints** (teaching preparation); this entry puts the analogy under "Relations" rather than `先修`,
     so that "is like" is not mislabelled as "comes before"
- **Evidence**: ev-083 · ev-085
- **Attacked**: **the textbook never writes `Review electric charge` or the like** — the basis for this edge is the chapter structure and the law's own definition,
  weaker than a "Review …" style hook. **Recorded here as is**, not dressed up as an explicit textbook statement.
- **Attribution**: @hpleapfrog · 2026-10-18

### K2 · The formula holds only when all three conditions hold (no attack yet)

- **Claim**: `F ∝ 1/r²`, charges at rest relative to each other, and "from outside a sphere, treat as the centre" — all three must hold for the law to apply
- **Premise**: the textbook derives `F ∝ 1/r²` and `F ∝ q₁q₂` from torsion-balance measurements (ev-085), and states the applicability sentence and the legitimacy of centre-to-centre distances
- **Reasoning**: the law's guarantee covers exactly its stated premises; applying it to charges in relative motion puts the result outside that guarantee
- **Evidence**: ev-085
- **Attacked**: no attacks yet
- **Attribution**: @hpleapfrog · 2026-10-18

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-18 | Entry created; second node of the electrostatics chapter, following "charge" and leading to "electric field" | written after reading m54414 in full (ev-085) | @hpleapfrog |
