---
id: kb:physics:kp-electric-charge
type: 知识点
title: "Electric charge"
status: 待审
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 物理
  学段: 高中
  适用: students starting electrostatics, meeting "electric charge" systematically for the first time
  条件: covers only the kinds of charge, conservation, transfer, conductors/insulators; no quantitative Coulomb's law or fields (separate entries)
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-083, ev-084]
license: CC-BY-SA-4.0
---

> **English version of [`电荷.md`](电荷.md).**

> [!TIP]
> **After reading this entry you should** be able to state the two "kinds" of charge, why total charge is conserved, and what is actually transferred in "charging by rubbing"

## Definition

**Electric charge** is a property of matter: **it makes objects attract or repel each other**.

> `Electric charge … is a property of matter that causes objects to attract or repel each other.`

There are only two kinds: **positive** and **negative**. **Like charges repel, unlike charges attract** — this rule is the starting point of all electrostatics.

| Quantity | Convention |
|---|---|
| elementary charge `e` | `1.602 × 10⁻¹⁹ C` (proton `+e`, electron `−e`, exactly equal in magnitude) |
| unit of charge | **coulomb** (C) — SI, named after Coulomb |
| `1 C` requires | about `6.25 × 10¹⁸` protons (or as many electrons) |
| charge is "quantized" | every charge is an integer multiple of `e` — the oil-drop experiment found charge comes in **discrete** units |

**Law of conservation of charge**: charge **cannot be created or destroyed**, only transferred.

```
q_initial = q_final
```

Materials are classified by whether charge can move easily: **conductors** (metals — charge moves easily) and **insulators** (rubber, glass, plastics — it does not), with semiconductors in between. On a conductor, excess charge spreads to the **outer surface**; on an insulator it **stays put**.

Objects can be charged in three ways: **by contact** (rubbing), **by conduction**, **by induction** — induction needs no touching and works through **polarization** (a separation of charge).

> [!IMPORTANT]
> **The word "static" does not mean "nothing is moving".**
>
> The chapter opening tells teachers outright: `Although the word static implies that nothing is moving, this is often not the case.`
>
> Separating positive from negative charges **is** charge in motion; what can last a long time is the **imbalance** afterwards.
> Lightning is a huge **current**, yet it is created by static electricity — "static" and "moving" are not in conflict here.
>
> The other common error is **who moves**: in solids the **electrons** are what move; protons are locked in the nucleus.
> A "transfer of positive charge" is really electron movement in the opposite direction, as a bookkeeping convention.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | — (chapter entrance; "universal gravitation" and "vectors" in the chapter opening are **review hints**, not prerequisites of this entry) |
| Follow-up | [Coulomb's law](coulombs-law.en.md) — computing the force between charges |
| Follow-up | [Electric field](electric-field.en.md) — rewriting "force" as "force per unit charge" |
| Misconception | [taking conventional current as the actual electron flow](../misconceptions/conventional-current.en.md) |
| Recorded gap | **"Preventing and using static electricity"** (PEP B3 §9.4) is not built yet |

## Argument

### K1 · Why this is a separate node (no attack yet)

- **Claim**: electric charge deserves to be an independent knowledge point
- **Premise**: the textbook gives it its own section and BL/OL/AL teaching notes (ev-084)
- **Reasoning**: it has its own vocabulary (positive/negative, conservation, conductors/insulators, polarization)
  and its own trap (reading "static" as "motionless"); everything later in electrostatics
  (Coulomb's law, fields, potential) presupposes it
- **Evidence**: ev-084
- **Attacked**: it is also "just" the opening concept of the chapter; by section boundaries it might be
  too fine-grained — the same self-doubt recorded in [reflection of light](reflection-of-light.en.md)
- **Attribution**: @hpleapfrog · 2026-10-18
- **To be added**: section 4 (preventing/using static electricity) is not built; the coverage page records it

### K2 · The "static vs transfer" tension is the textbook's own (no attack yet)

- **Claim**: "static does not mean motionless" comes from the textbook, not from this repo
- **Premise**: the chapter opening says `Although the word static implies that nothing is moving, this is often not the case` (ev-083);
  the transfer section asks teachers to pose `Ask how the concept of static electricity can be compatible with transfer of charge?` (ev-084)
- **Reasoning**: the textbook leaves this apparent contradiction for class discussion — evidence that
  it is expected to be a genuine student question, not an editorial slip
- **Evidence**: ev-083 · ev-084
- **Attacked**: no attacks yet
- **Attribution**: @hpleapfrog · 2026-10-18

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-18 | Entry created; first node of the electrostatics chapter | written after reading m54417 and m54410 in full (ev-083 / ev-084) | @hpleapfrog |
