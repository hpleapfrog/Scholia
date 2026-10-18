---
id: kb:physics:method-ucm-cut-string
type: 教法
title: "Uniform circular motion · any level: cut the string and ask where it goes"
status: 待审
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 物理
  学段: 高中
  水平档: 不分档
  适用: students who have just built a description of circular motion and need "acceleration points at the centre"
  条件: a demonstrable string and weight; if no demo is possible, at least an equivalent diagram
edges:
  先修: []
  支持: []
  攻击: []
knowledge_point: ["[uniform circular motion](../concepts/uniform-circular-motion.en.md)"]
evidence: [ev-081]
license: CC-BY-SA-4.0
---

> **English version of [`匀速圆周运动-不分档-剪断绳子.md`](匀速圆周运动-不分档-剪断绳子.md).**

## Procedure

The textbook gives a **chain of three questions** that runs from the demo to the direction of acceleration:

> `[BL] [OL] [AL] Demonstrate circular motion by tying a weight to a string and twirling it around. Ask students what would happen if you suddenly cut the string? In which direction would the object travel? Why? What does this say about the direction of acceleration?`

In four steps:

| # | Teacher / students | What this step does |
|---|---|---|
| 1 | Tie a weight, spin it | give the **phenomenon**, not the formula |
| 2 | "If I cut the string now, which way does it go?" | most will say "outward" |
| 3 | "Why?" | forces "nothing is pulling it any more" → **inertia** |
| 4 | "So which way does the acceleration point?" | from "goes straight when released" back to "there must be an inward force while spinning" |

Step 2 is **allowed to be wrong**: "flies outward along the radius" is exactly what the demo is
meant to expose. Step 3 is the turn — you do not correct "outward" into "tangent" by fiat, you ask
what rule applies once the force is gone.

### Follow-up: the same demo predicts the relations

> `[BL] [OL] [AL] Using the same demonstration as before, ask students to predict the relationships between the quantities of angular velocity, centripetal acceleration, mass, centripetal force. Invite students to experiment by using various lengths of string and different weights.`

Vary string length and mass; have students predict first, then check against `a_c = v²/r`
and `F_c = m v²/r`.

## Contraindications

| Not for | Basis | Strength |
|---|---|---|
| Students who have **not** met inertia / Newton's first law | step 3 depends entirely on "no force → straight line"; without it the demo only shows "the thing flew off" | **strong** — follows from the reasoning chain |
| A class that needs to reach the exercises fast | the method spends time on **attribution**, not on solution steps | **medium** |
| Settings with no demo at all | the chain starts from an **observable** cut; purely verbal, students share no observation | **medium** |

## Risks

| How it goes wrong | Why |
|---|---|
| Students read "it flies off" as evidence for centrifugal force | the **most likely** misreading, and the demo itself encourages it. Do not stop before step 3 |
| The teacher says "centrifugal force throws it out" | one sentence turns the demo against the textbook, which asks teachers to `Address any misconceptions about centrifugal force` |
| Giving the answer at step 2 | without a prediction, step 3 becomes reciting the teacher |
| Doing only step 1 and jumping to the formula | the demo becomes decoration; students remember "the string pulls", not "the perpendicular component of the net force" |

## Evidence

| Id | Type | Grade | Locator | License |
|---|---|---|---|---|
| ev-081 | textbook (full text) | low | OpenStax *Physics*, ch. 6 · Uniform Circular Motion, [m54181](https://github.com/openstax/osbooks-physics/blob/main/modules/m54181/index.cnxml), Teacher Support (marked `[BL][OL][AL]`) | **CC BY 4.0** |

## Argument

### M1 · Specified for all three levels (no attack yet)

- **Claim**: the textbook recommends this for BL, OL and AL at once
- **Premise**: the Teacher Support line is tagged `[BL] [OL] [AL]` (ev-081)
- **Reasoning**: three tags at once means it is not tied to one cognitive level — hence `水平档: 不分档`
- **Evidence**: ev-081
- **Attacked**: **"tagged for three levels" is not "effective at three levels"**. It says the textbook
  thought the demo suitable for all three; this library has **no classroom data**. That is exactly
  why a `教法` can never be `已确证`.
- **Attribution**: @hpleapfrog · 2026-10-18
- **To add**: feasibility in a Chinese classroom (large classes, no demo kit) — no data here

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-18 | Entry created; the chapter's first `教法` | ev-081, Teacher Support read in full | @hpleapfrog |
