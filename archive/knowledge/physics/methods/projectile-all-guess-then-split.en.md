---
id: kb:physics:method-projectile-all-guess-then-split
type: 教法
title: "Projectile motion · all levels: let them guess, then split the axes"
status: 有效
author: "@hpleapfrog"
created: 2026-10-23
updated: 2026-10-23
scope:
  学科: 物理
  学段: 高中
  水平档: 不分档（教材在同一段标了 BL/OL/AL）
  适用: students about to learn horizontal throws, used to one formula fits all
  条件: they know vector addition and the kinematic equations
edges:
  先修: []
  支持: []
  攻击: []
knowledge_point: ["[projectile motion](../concepts/projectile-motion.en.md)"]
evidence: [ev-163]
license: CC-BY-SA-4.0
---

> **English version of [`抛体运动-OL-先猜再分解.md`](抛体运动-OL-先猜再分解.md).**

## What the method does

> `[BL] [OL] [AL] … Ask students to guess what the motion of a projectile might depend on? Is the initial velocity important? Is the angle important? How will these things affect its height and the distance it covers?`

**Guessing is the first step, not a warm-up.** Air resistance is then introduced as the variable to set aside.
The core claim is one sentence:

> `when air resistance is ignored, horizontal and vertical motions are independent`

and it is proved by a picture: a dropped ball and a horizontally launched ball **fall at the same rate**.

## Contraindications

| Not suitable for | Basis | Strength |
|---|---|---|
| students who cannot decompose vectors yet | the source first asks `Review addition of vectors` | **strong** |
| students already fluent in projectile problems | they need oblique throws and extrema | **medium** |
| a lesson that must include air resistance | the premise is to ignore it | **medium** |

## Risks

| Where it goes wrong | Why |
|---|---|
| skipping the guess | the guess is what builds the list of relevant quantities |
| asserting "heavy falls faster" without the side-by-side drop | the conclusion rests on that figure |
| omitting the vertical-component caveat | the source adds `if the cannon launched the ball with any vertical component … would not line up` |

## Evidence

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-163 | textbook (full text) | low | OpenStax *Physics* ch. 5 · Projectile Motion, [m54162](https://github.com/openstax/osbooks-physics/blob/main/modules/m54162/index.cnxml) | **CC BY 4.0** |

## Argument

### M1 · Tagged for all three levels (no attack yet)

- **Claim**: guess → set aside air resistance → independence → simultaneous fall is the source's sequence
- **Premise**: m54162's `[BL] [OL] [AL]` prompt and body text (ev-163)
- **Evidence**: ev-163
- **Attacked**:
  - **"specified" ≠ "proven effective"**
  - **"skipping the guess destroys the point" is my judgement**, not stated
- **Attribution**: @hpleapfrog · 2026-10-23

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-23 | Entry created from m54162 | `tools/os_source.py` read of the source (ev-163) | @hpleapfrog |
