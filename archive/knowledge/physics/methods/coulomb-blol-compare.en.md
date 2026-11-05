---
id: kb:physics:method-coulomb-blol-compare
type: 教法
title: "Coulomb's law · BL/OL: compare it item by item with gravitation"
status: 有效
author: "@hpleapfrog"
created: 2026-10-22
updated: 2026-10-22
scope:
  学科: 物理
  学段: 高中
  水平档: 低于年级水平（BL）至 年级水平（OL）
  适用: students who know Newton's law of gravitation and are about to meet Coulomb's law
  条件: they have seen F = Gm₁m₂/r²
edges:
  先修: []
  支持: []
  攻击: []
knowledge_point: ["[Coulomb's law](../concepts/coulombs-law.en.md)"]
evidence: [ev-085]
license: CC-BY-SA-4.0
---

> **English version of [`库仑定律-BLOL-与万有引力对照.md`](库仑定律-BLOL-与万有引力对照.md).**

## What the method does

The module's `[BL]` / `[OL]` prompts **do not start from the formula — they start from "what is it like"**.

### 1. Put the two laws side by side first

> `This section presents Coulomb's law and points out its similarities and differences with respect to Newton's law of universal gravitation.`

| Same | Different |
|---|---|
| both inverse-square | **mass is only positive; charge can be either sign** |
| "mass" and "charge" play the same role in their laws | — |

### 2. Then compare them in time

> `[BL] [OL] Discuss how Coulomb described this law long after Newton described the law of universal gravitation.`

The prompt says **discuss**, not narrate: "later" is offered as a question, not a date to memorise.

### 3. Clear one reading trap

> `Point out how the subscripts 1, 2 means the force on object 1 due to object 2 (and vice versa).`

## Conditions

| Dimension | Value |
|---|---|
| Level | **BL / OL** (the same prompt carries both tags) |
| Prerequisite | Newton's law of gravitation; inverse-square |
| Load | low to medium — the load sits in the comparison table, not in algebra |

## Contraindications

| Not suitable for | Basis | Strength |
|---|---|---|
| students who have **not** met gravitation | the whole structure is a comparison — **with nothing to compare against, only a formula is left** | **strong** |
| students who need calculation practice now | this produces no computational fluency | **medium** |
| students outside BL/OL | the `[AL]` prompt asks a different question | **medium** |

## Risks

| Where it goes wrong | Why |
|---|---|
| teaching only "both are inverse-square" | the **difference column is the error-prone part** (positive mass → attraction only; charge → attract or repel) |
| turning "Coulomb came later" into a date story | the prompt says `Discuss how…`; the point is the *why*, not the year |
| skipping the subscripts | the textbook says `Point out` — it expects the misreading |

## Evidence

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-085 | textbook (full text) | low | OpenStax *Physics* ch. 18 · Coulomb's Law, [m54414](https://github.com/openstax/osbooks-physics/blob/main/modules/m54414/index.cnxml) | **CC BY 4.0** |

## Argument

### M1 · Specified by the textbook for BL/OL (no attack yet)

- **Claim**: the textbook specifies this practice for BL/OL students
- **Premise**: m54414's Teacher Support tags "discuss how Coulomb came later" as `[BL] [OL]` and
  asks explicitly for similarities and differences (ev-085)
- **Reasoning**: the level tag is the textbook's specification; the two columns are quoted, not paraphrased
- **Evidence**: ev-085
- **Attacked**:
  - **"specified" ≠ "proven effective"** — no classroom data
  - the step "positive mass → attraction only" is my inference; the module stops at
    `restriction of positive mass versus positive or negative charge`
- **Attribution**: @hpleapfrog · 2026-10-22

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-22 | Entry created from m54414's Teacher Support | source cnxml read in full (ev-085) | @hpleapfrog |
