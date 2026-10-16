---
id: kb:physics:resource-phet-forces-and-motion-basics
type: 资源
title: "PhET simulation 'Forces and Motion: Basics'"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  资源类型: 交互式模拟（浏览器内运行）
  适用: teaching balanced/unbalanced forces and friction
  条件: 需要能打开网页的设备
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-029]
license: CC-BY-SA-4.0
---

> **English version of [`PhET-力与运动基础.md`](PhET-力与运动基础.md).**

## Locator

| Item | Value |
|---|---|
| Resource | PhET Interactive Simulations — **Forces and Motion: Basics** |
| Direct link | <https://phet.colorado.edu/sims/html/forces-and-motion-basics/latest/forces-and-motion-basics_en.html> |
| Entry inside the textbook | `https://openstax.org/l/forcesandmotion` (short link, verified to resolve to the direct link above) |
| Textbook source | OpenStax《Physics》 Chapter 4 · Newton's First Law: Inertia, module [m54138](https://github.com/openstax/osbooks-physics/blob/main/modules/m54138/index.cnxml) |
| Runs | in the browser, **no installation** |
| Belongs to | [惯性](../知识点/惯性.en.md) |

### License (**important**)

> [!CAUTION]
> **This resource is `CC BY-NC 4.0` (NonCommercial), not `CC BY`.**
>
> Verified from the simulation file's own header (the authoritative source — the artifact carries its own declaration):
>
> > `This file is licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).`
> >
> > `COMMERCIAL USE REQUIRES A COMMERCIAL LICENSE AGREEMENT FROM THE UNIVERSITY OF COLORADO BOULDER.`
>
> **Three other PhET sims checked the same** (my-solar-system / bending-light / color-vision),
> showing this is a uniform policy, not a one-off.

> [!IMPORTANT]
> **The license does not travel with the textbook.**
>
> The textbook OpenStax《Physics》 is **CC BY 4.0**, but the PhET sims it **embeds** are still **CC BY-NC 4.0**.
> "The textbook is freely reusable" **does not imply** "what it embeds is too".
>
> This is a **real license trap**: re-publishers who copy the textbook's structure will hit it.

### Attribution required when citing

The simulation file's own recommended wording (**required to be placed "near the place of use"**):

> Simulation by PhET Interactive Simulations, University of Colorado Boulder,
> licensed under CC BY-NC 4.0 (<https://phet.colorado.edu>)

> [!NOTE]
> **This entry is not a copy of the resource, only its locator and usage notes.**
> The repo's `CC-BY-SA-4.0` applies to **the text we wrote in this entry**,
> **not** to the linked PhET simulation.

## Usage

The textbook's main text has a full `virtual-physics` note (short quotation + summary):

**Screen 1: tug-of-war**
> `placing blue people on the left side of a tug-of-war rope and red people on the right side`

Change the number and size of people on each side, observe the effect on **net force**, press `Go!` to start. **This is an embodied demonstration of "balanced / unbalanced forces".**

**Screen 2: friction (the `Friction` tab)**
> `Slide the applied force button … See the arrow representing friction change in magnitude and direction`

Drag the applied force's magnitude, observe **the friction arrow change with the applied force**; then adjust the friction coefficient to see how motion changes.

> [!TIP]
> **Screen 2 maps directly onto a repo misconception.**
>
> The crux of [objects in motion naturally slow down](../误解/运动物体自然慢下来.en.md) is:
> students **treat friction's effect as a property of the object itself**.
>
> This simulation lets students **treat friction as a quantity you can turn up and down**, not a background condition —
> turn friction down and the object slides further. **"The object stops by itself", on which the misconception rests, does not stand on this interface.**

## Argument

### R1 · Why this resource is worth holding (no attack yet)

- **Claim**: the simulation's teaching value **exceeds** "a clickable animation"
- **Premise**: the textbook aims its two screens at the two concepts of **net force** and **friction**;
  and the repo already records a misconception directly related to it (ev-028)
- **Reasoning**: a resource that lets students **change the interfering variable themselves** (friction)
  is more likely to dismantle the attribution error "the object stops by itself" than an explanation they can only watch
- **Evidence**: ev-029, ev-025 (the section's textbook teaching hint), ev-028 (source of the misconception)
- **Attacked**:
  - **"more likely" is my inference, with no classroom data** — the repo has no measurement of the simulation's effect
  - the textbook placing it in that section **does not equal** it being more effective than lecturing
- **Attribution**: @hpleapfrog · 2026-10-05
- **To be added**: an attribution test before and after using the simulation

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry: the repo's **first `资源` entry**, testing that object type in practice | collection extension | @hpleapfrog |
