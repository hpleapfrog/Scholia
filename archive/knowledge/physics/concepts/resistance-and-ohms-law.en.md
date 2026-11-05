---
id: kb:physics:kp-resistance-and-ohms-law
type: 知识点
title: "Resistance and Ohm's law"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 初中至高中
  范围: DC circuits

edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-016, ev-018]
license: CC-BY-SA-4.0
---

> **English version of [`电阻与欧姆定律.md`](电阻与欧姆定律.md).**

> [!TIP]
> **After reading this entry you should** be able to explain the relation among current, voltage, and resistance, and to point out the conditions under which this relation holds

## Definition

The relation among three basic quantities in a DC circuit:

- **current I**: the rate of directional movement of charge
- **voltage V / U**: the potential difference that drives the current
- **resistance R**: opposition to current

When the temperature is constant and the material is an **ohmic material**, the three satisfy `U = I × R`.

## Relations

| Object | Entry | Note |
|---|---|---|
| proposition | [Ohm's law](../claims/ohm-law.en.md) | an assertion awaiting a truth judgment (same name as this knowledge point, but a different layer) |
| proposition | [the difference between the voltage symbols U and V in Chinese and English textbooks](../claims/voltage-symbol-u-v.en.md) | the symbols differ between Chinese and English textbooks |
| proposition | [the difference in where the limitations of Ohm's law are presented](../claims/ohm-law-scope-placement.en.md) | two textbooks place the limitations in different positions |
| teaching method | [water-pipe analogy](../methods/water-pipe.en.md) | an intuitive analogy (junior/senior high) |
| teaching method | [friction analogy](../methods/friction-analogy.en.md) | explains heating (introductory university) |
| misconception | [taking the direction of current as the actual direction of electron motion](../misconceptions/conventional-current.en.md) | the conventional current direction versus the direction of charge carriers |

> [!NOTE]
> **This knowledge point and `命题/欧姆定律` share a name but are different layers**:
> the knowledge point is an **organizing unit** (what to teach on this topic), the proposition is a **judging unit** (which sentence is true or false).
> Sharing a name is not a conflict; it is the inevitable result of **layering**.

## Argument

### K4 · Why the three quantities form one knowledge point (no attack yet)

- **Claim**: current, voltage, and resistance should be one knowledge point rather than three separate ones
- **Premise**: the teaching-method entries of both textbooks **use all three quantities together** (the water-pipe analogy maps all three; the friction analogy focuses on resistance but relies on current and voltage)
- **Reasoning**: a teaching method cannot present only one of the quantities — the validity of the analogy rests on the relation among the three. Splitting them into three knowledge points would make every teaching method attach to three nodes
- **Evidence**: ev-016, ev-018
- **Attacked**: **the merge is too coarse**. Beginners often first form an independent concept of "current" before voltage and resistance are introduced; merging into one node may obscure that sequence
- **Attribution**: @hpleapfrog · 2026-10-05
- **To be added**: if a standalone teaching method aimed only at "current" appears later, this should be split

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (plan A: add the knowledge-point layer) | Issue #11 | @hpleapfrog |
