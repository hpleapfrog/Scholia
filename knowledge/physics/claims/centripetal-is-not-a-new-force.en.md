---
id: kb:physics:prop-centripetal-is-not-a-new-force
type: 命题
title: "Centripetal force is not a new kind of force but the velocity-perpendicular component of the net force"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 物理
  学段: 高中
  适用: students who have met uniform circular motion and now have to find "who provides the centripetal force"
  条件: "**states only how the textbook phrases it**; writing an inertial (fictitious) force as 「centrifugal」 in a non-inertial frame is a different bookkeeping, which this entry does not deny"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-081]
license: CC-BY-SA-4.0
---

> **English version of [`向心力不是一种新的力.md`](向心力不是一种新的力.md).**

## Statement

**Centripetal force is not "a fifth force"; it is the part of the net force perpendicular to velocity.**

The textbook defines it as a component:

> `the component of the net force which is perpendicular to the velocity; an object moving in a circular path does so due to a centripetal force`

The next sentence is blunter — **any force or combination of forces can play that role**:

> `Any force or combination of forces can cause a centripetal acceleration. Just a few examples are the tension in the rope on a tether ball, the force of Earth's gravity on the Moon, the friction between a road and the tires of a car as it goes around a curve, or the normal force of a roller coaster track on the cart during a loop-the-loop.`

| Situation | What provides it |
|---|---|
| Ball on a string | the string's **tension** |
| Moon around Earth | **gravity** |
| Car turning | **static friction** between tyres and road |
| Roller-coaster loop | the track's **normal force** |

> [!IMPORTANT]
> **So "find the centripetal force" really asks "who provides the inward net force here".**
> Treat it as a force you can draw separately and you will add a second arrow to the free-body
> diagram, then add an opposite one to "balance" it — exactly where the
> [centrifugal misconception](../misconceptions/centrifugal-force-is-real.en.md) starts.

## Evidence

| Id | Type | Grade | Locator | License |
|---|---|---|---|---|
| ev-081 | textbook (full text) | low | OpenStax *Physics*, ch. 6 · Uniform Circular Motion, [m54181](https://github.com/openstax/osbooks-physics/blob/main/modules/m54181/index.cnxml), "Centripetal Force" | **CC BY 4.0** |

## Argument

### A1 · The textbook says "component", not "a kind of force" (no attack yet)

- **Claim**: the canonical phrasing is "the net force's velocity-perpendicular component", not a separate force type
- **Premise**: the Key Terms definition uses `component of the net force` (ev-081)
- **Reasoning**:
  1. "Component" means it depends on an existing force — it cannot exist without tension, gravity, friction…
  2. The textbook then names **four different real forces** in four situations; if it were a force
     type, the same force would appear in all four
  3. The summary sentence `Centripetal force F_c is any net force causing uniform circular motion`
     also takes "any net force" as its subject
- **Evidence**: ev-081
- **Attacked**: **"component" is still ambiguous under strict vector decomposition** — the
  perpendicular component of the net force is `F sin θ`, whereas uniform circular motion needs it
  to be the *whole* net force (zero tangential component). The textbook does not separate
  "net force happens to be perpendicular" from "net force has a perpendicular component".
  **This entry reports the textbook's phrasing; it does not patch that gap for it.**
- **Attribution**: @hpleapfrog · 2026-10-18

### A2 · Scope: this does not deny the other bookkeeping (no attack yet)

- **Claim**: the entry claims only that, in an inertial frame, centripetal force is not a new force
  type — **not** that "centrifugal" may never be used
- **Premise**: the textbook calls centrifugal force `a fictitious force` and traces it to an
  `accelerating reference frame` (ev-081)
- **Reasoning**: "fictitious" is not "wrong"; in a non-inertial frame the equations can be made to
  work by introducing it. The textbook's wording identifies its **origin**, not its uselessness
- **Evidence**: ev-081
- **Attacked**: no attacks yet
- **Attribution**: @hpleapfrog · 2026-10-18
- **To add**: **how to write it in a non-inertial frame has no entry here**; that needs another
  source (the textbook gives one qualitative sentence and no formalism)

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-18 | Entry created | ev-081, m54181 read in full (Key Terms and Section Summary included) | @hpleapfrog |
