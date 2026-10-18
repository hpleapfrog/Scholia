---
id: kb:physics:ohm-law-scope-placement
type: 命题
title: "Where textbooks place the limitations of Ohm's law"
status: 待审
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 初中至大学
  适用: designers of textbook arrangement and teaching sequence
  条件: 无
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-001, ev-016]
license: CC-BY-SA-4.0
---

> **English version of [`局限性的位置.md`](局限性的位置.md).**

## Statement

Both textbooks admit Ohm's law is not universally valid, but **place it in different positions**:

| | 人教版《物理》九年级 | OpenStax《College Physics 2e》§20.3 |
|---|---|---|
| Position of the limitation | "scope reminder" (hint layer) | **main text**, alongside the law |
| Wording | uses "temperature constant" as a **precondition clause** | explicitly states "not universally valid" |
| Terms | none | `ohmic` / `non-ohmic` |

This yields two mental models:

- **build the law first, patch later** (人教版)
- **law and boundary given together** (OpenStax)

## Basis

| Number | Type | Grade | Locator | Time |
|---|---|---|---|---|
| ev-001 | textbook | low | 人教版《物理》九年级全一册, 2013, P.79 | 2013 |
| ev-016 | textbook (full text) | low | OpenStax《College Physics 2e》§20.3 | 2020 |

## Argument

### A1 · Side-by-side texts (no attack yet)

- **Claim**: the two textbooks place the same limitation in different positions
- **Premise**: ev-001 puts it in a "reminder"; ev-016 writes it in the main text and introduces the term `ohmic`
- **Reasoning**: comparing the two public texts suffices
- **Evidence**: ev-001, ev-016
- **Attacked**: none
- **Attribution**: @hpleapfrog · 2026-10-05

## Implications for "path" arrangement

> [!IMPORTANT]
> This proposition **does not judge which arrangement is better** — the sequence choice depends on stage and goal.
>
> But it is a variable that **arrangement decisions must face explicitly**: putting the limitation first sacrifices the intuitiveness of first learning;
> putting it last may lead students to treat the law as unconditionally true. **This trade-off should be written down, not left implicit in the textbook.**

Mapped to this repo: see the "scope reminder" section of [Ohm's law](ohm-law.en.md), and
the contraindications column of [teaching method: water-pipe analogy](../教法/water-pipe.en.md).

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (migrated in from cross-textbook comparison) | Issue #3 | @hpleapfrog |
