---
id: kb:physics:kp-inertia
type: 知识点
title: Inertia
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-18
scope:
  学科: 物理
  学段: 高中
  范围: forces and motion

edges:
  先修: ["[知识点：力（高中）](force.en.md)"]
  支持: []
  攻击: []
evidence: [ev-025]
license: CC-BY-SA-4.0
---

> **English version of [`惯性.md`](惯性.md).**

> [!TIP]
> **After reading this entry you should** be able to state "the property by which an object maintains its state of motion is called inertia", and to point out that the amount of inertia is determined by mass

## Definition

**Inertia** is the property of an object **of maintaining its state of motion**. Its full statement is **Newton's first law** (also called the **law of inertia**):

- a body **at rest** tends to remain at rest;
- a body **in motion** tends to remain in motion **in a straight line at a constant speed** — unless acted on by a **net external force**.

> [!NOTE]
> **Translating the law into problem-solving language.**
>
> - "constant velocity" in the law means **straight line** *and* **constant speed**;
> - "no net external force" is written `F_net = 0` (or `ΣF = 0`) — the textbook's key equation;
> - and there is a shortcut in reverse: the phrase "**at constant velocity**" in a problem tells you **the net external force is zero**.
>   The textbook's example: a man pushes a box at constant velocity with +50 N, so friction must be −50 N — the two forces cancel exactly.

The amount of inertia:

- is determined by **mass**: the greater the mass, the greater the force needed to change its state of motion (a large truck vs a toy truck)
- the textbook settles it with one problem: which has more inertia, a **parked** 2,000 kg car or a **moving** 60 kg bike and rider at 10 km/h? — the car.
  **Inertia depends on mass, not on whether or how fast an object is moving**
- Galileo first described the property; Newton wrote it into the first law, which is why that law is also the **law of inertia**

> [!IMPORTANT]
> **Friction is what takes the blame for "objects slow down by themselves".**
>
> The textbook insists on explaining **friction** first: an **external** force acting opposite to relative motion
> (or preventing slipping). A sliding box "stops on its own" only because friction is decelerating it;
> with no net external force it would **keep sliding at constant velocity**.
> "Friction" is a family: **kinetic** (sliding), **static** (preventing slip), **rolling resistance**, **drag**;
> its quantitative form is `f = μN` — the coefficient `μ` depends on the nature of the two surfaces, and `N` is the normal force.
> The textbook's demonstration: turn off the air on an air hockey table and the puck stops after a short slide;
> turn it on and the puck glides with almost no friction.

> [!NOTE]
> **Mass vs weight: no difference in daily speech, two different things in science.**
>
> Mass is the quantity of matter in an object (fixed by the number and types of atoms), **does not change with gravity** —
> the same on Earth, in orbit, on the Moon — and is measured in **kilograms**.
> Weight is a **force** and changes with gravity (its full treatment is in Newton's second law).
> The textbook notes: everyday language uses the two interchangeably, and in science that is simply wrong.

## Relations

| Object | Entry | Note |
|---|---|---|
| teaching method | [inertia · BL: definition and "maintaining a state of motion"](../methods/inertia-bl-definition.en.md) | first establish the phrasing of the property |
| teaching method | [inertia · AL: two-car inquiry into "what does inertia depend on"](../methods/inertia-al-cart-inquiry.en.md) | let students infer mass themselves |

> [!WARNING]
> **The relation to junior high is "advancement", not "prerequisite".**
>
> [Forces and motion (junior high)](forces-and-motion-jhs.en.md) already qualitatively describes the same phenomenon with **balanced / unbalanced forces**;
> the high-school step names "maintaining a state of motion" as inertia and asks what it depends on.
>
> **This is not a temporal prerequisite of "learn junior high before high school" but a deepening of the same theme.**
> The repo currently **has no means of expressing an "advancement" relation** — `先修` triggers a cross-stage warning,
> and the warning text itself says "please confirm this is a conceptual prerequisite, not an advancement relation". Here confirmed: **it is advancement, so no edge is created.**

## Argument

### K6 · Why listed separately (no attack yet)

- **Claim**: inertia deserves to be a separate knowledge point rather than merged into "forces and motion (junior high)"
- **Premise**: the textbook gives it its own section (OpenStax《Physics》§4.2, ev-025)
- **Reasoning**: the textbook has a dedicated teaching hint (including mass/weight terminology and a two-car inquiry), showing it has an independent teaching goal
- **Evidence**: ev-025
- **Attacked**: a textbook's section division is not a cognitively independent unit
- **Attribution**: @hpleapfrog · 2026-10-05

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (#8 batch conversion · batch 1) | Issue #8 | @hpleapfrog |
| 2026-10-18 | learner half expanded: the first law's full statement and `F_net = 0`, constant velocity ⇔ zero net force, mass sets inertia (independent of speed), the friction family, mass vs weight | weak-entry expansion · m54138 re-read (ev-025) | @hpleapfrog |
