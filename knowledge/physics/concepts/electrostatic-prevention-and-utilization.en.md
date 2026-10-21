---
id: kb:physics:electrostatic-prevention-and-utilization
type: 知识点
title: "Prevention and utilization of static electricity"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have done electric field and want to understand how a conductor behaves in an electrostatic field
  条件: covers the three properties of electrostatic equilibrium, electrostatic shielding, point discharge, and several applications; no quantitative surface-charge density, breakdown statistics, or shielding in alternating fields
edges:
  先修: ["[Electric field](electric-field.en.md)", "[Electric charge](electric-charge.en.md)"]
  支持: []
  攻击: []
evidence: [ev-181]
license: CC-BY-SA-4.0
---

> **English version of [`静电的防止与利用.md`](静电的防止与利用.md).**

> [!TIP]
> **After reading this entry you should** be able to state the three properties of a conductor in electrostatic equilibrium, explain why a lightning rod is pointed and why a car protects its occupants from lightning, and tell which rule each of "electrostatic precipitation, xerography" and "grounding, shielding" relies on

## Definition

### Electrostatic equilibrium: no charge moves inside the conductor any more

Put a conductor in an electrostatic field, or give it excess charge, and its **free charges** quickly redistribute until they no longer move in any one direction — that state is **electrostatic equilibrium** (ev-181). In metals the free charges are **electrons**; the textbook notes that free charges can be positive or negative, and are negative in metals (ev-181).

In equilibrium there are **three properties** (listed one by one in the textbook, ev-181):

1. **The electric field inside the conductor is zero**: `E_inside = 0`
2. **Just outside the surface, the field is perpendicular to the surface**; field lines end or begin on the surface charges
3. **All excess charge resides on the surface** — the textbook's words are `Any excess charge resides entirely on the surface or surfaces of a conductor` (ev-181)

> Why must the interior be zero? If a field remained inside, free charges would still feel a force and keep moving, so it would not be equilibrium. The textbook says the same thing in another way: free charges move until the field is **perpendicular to the surface**; if the field had a component parallel to the surface, the charges would keep moving (ev-181).

For a **spherical conductor**, the excess charge spreads **uniformly** over the surface, and the field outside is exactly that of a point charge with all the excess charge at the centre (ev-181).

### Electrostatic shielding: the Faraday cage

Make the conductor a **closed shell**: an external electrostatic field redistributes free charges on the outer surface, but there is no field inside the conductor (inside the cavity) — this is **electrostatic shielding**. The textbook calls the device a **Faraday cage**: a metal shield enclosing a volume, with all charges residing on the outside surface and no electric field inside (ev-181).

The textbook's examples (ev-181):

- a car's metal body acts as a Faraday cage in a lightning storm, and the interior is unaffected — **provided the person stays completely inside**;
- the same holds if a live high-voltage wire falls on the car;
- a Faraday cage also keeps stray environmental fields away from sensitive measurements.

> [!NOTE]
> The textbook's glossary describes a Faraday cage as "a metal shield which prevents electric charge from penetrating its surface" (ev-181). That wording narrows the mechanism: **the charge is already on the outside surface; what is shielded is the external field**. This entry follows the physics of the main text.
>
> This section discusses **electrostatic equilibrium** only. Shielding in alternating fields and the skin effect are outside its scope.

### Point discharge: the sharpest curvature breaks down first

Where the surface **curvature is greatest** (the sharpest points), excess charge concentrates most and the field nearby is strongest. When it becomes strong enough, the air breaks down and ionizes, charge escapes from the point, and a **corona discharge** or a spark appears (ev-181).

The key number the textbook gives is that air breaks down at about `3×10⁶ N/C` (the same value in m42317 and m42329); the same number explains lightning — in a storm the local field becomes large enough to destroy the insulating property of air (ev-181).

The same rule is used in two opposite ways (ev-181):

- **A lightning rod is pointed**: the point continually bleeds the charge induced on the building into the air, preventing a more dramatic lightning strike;
- **High-voltage transmission lines are smooth, with a large radius of curvature**: this avoids the leakage caused by point discharge.

The textbook also gives Earth's fair-weather field: about `150 N/C`, directed **downward**; the ionosphere about 100 km up is positive and the ground is negative; in storms the local field is stronger and can even reverse (ev-181).

### Utilization and prevention: which rule each side uses

The textbook's §18.8 collects the **utilizations** of static electricity into a few devices (ev-181):

| Application | What is done | Rule used |
|---|---|---|
| **Electrostatic precipitation** | Smoke and dust particles are charged first, then the air passes an oppositely charged grid | Charged particles feel a force in the field and are collected; industrial units remove **over 99%** of the particles from coal- and oil-fired stack gas |
| **Xerography / laser printing** | A photoconductor (selenium) drum is charged positive; where light hits, selenium conducts and the positive charge is neutralized; negatively charged toner sticks to the remaining positive image and is then transferred to paper | Photoconductor + attraction of unlike charges |
| **Electrostatic painting** | Paint droplets are charged; like charges repel and spread the paint, and the workpiece attracts it | Like charges repel, unlike charges attract; the field just outside a conductor is perpendicular to its surface, so droplets arrive nearly perpendicularly; **points and edges receive extra paint** |
| **Ink-jet printing** | Droplets are charged and then steered by an electric field (deflection plates) | Charged particles are deflected in an electric field |
| **Van de Graaff generator** | Points spray charge onto an insulating belt, and points inside the top sphere take it onto the sphere's outer surface | Point discharge + charge residing on the outer surface; the textbook says **15 million volts** is within practical limits |

The **prevention** side uses the same rules in reverse (ev-181):

- **Grounding**: give the charge a path. The textbook's worked example notes that if a gasoline pump is not grounded, gasoline drops can pick up static charge while a car is being filled (ev-181); the grounding wire a car drives over before a tollbooth is the same idea — that is one of the textbook's conceptual questions, and the answer given here is grounding.
- **Shielding**: keep the external field out (Faraday cage, car).
- **Do not let the field concentrate**: smooth, large surfaces on high-voltage lines avoid leakage by point discharge.
- **Control the humidity**: the textbook's take-home experiment asks you to repeat "a comb lifting pieces of paper" in a steamy bathroom after a shower. The textbook only asks the question; "moist air carries charge away more easily, so electrostatic effects are weaker" is this library's explanation of the observation.

> [!NOTE]
> **Two small faults in the source** (ev-181):
> 1. One sentence in m42317 reads `Air ionizes ions and electrons recombine`, missing punctuation in the original; this entry does not copy that sentence.
> 2. The exercise sets of m42317 and m42329 mostly practise point-charge fields and forces (even a Millikan oil drop), with little connection to conductors, shielding or applications; this entry uses them only as background, not as this section's exercises.
>
> **Supplied here, not by the textbook**: the division into "charge it first, then move it with a field" and "ground it, shield it, keep the field from concentrating" is this library's organization; the textbook presents the applications one by one. The breakdown value `3×10⁶ N/C` comes from the textbook, but the quantitative relation "curvature — surface charge density — field strength" is not given there, and this entry does not supply it either.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Electric field](electric-field.en.md) — every conclusion about electrostatic equilibrium starts from the force a field exerts on free charge |
| Prerequisite | [Electric charge](electric-charge.en.md) — free charges, conservation of charge, and "excess charge" |
| Related | [Coulomb's law](coulombs-law.en.md) — a charged particle collected by a grid is acted on by `F = qE` |
| Recorded gap | **the quantitative relation between surface charge density and curvature, `E = σ/ε₀` just outside a conductor, the grounded cavity when charge is inside, lightning leaders and the protection angle, models of human-body electrostatic discharge, and shielding in alternating fields (skin effect)** are not built here |

## Argument

### K1 · Zero field inside a conductor ⇒ electrostatic shielding (no attack yet, but "no field in the cavity" is this library's reasoning)

- **Claim**: in electrostatic equilibrium the field inside a conductor is `E = 0`; this is what lets a Faraday cage shield an external field
- **Premises**: the textbook lists the three properties of a conductor in electrostatic equilibrium and says free charges move until the parallel component of the field vanishes (ev-181)
- **Reasoning**:
  1. If a field remained inside, free charges would still move — contradicting "equilibrium" — so the interior must have `E = 0`
  2. Once a closed conducting shell is in equilibrium in an external field, the field inside the shell material is zero; with no charge in the cavity, the cavity has no field either — the external field is kept outside the shell
  3. The textbook states the Faraday-cage conclusion directly (charge on the outer surface, no field inside); step 2 is supplied by this library
- **Evidence**: ev-181
- **Attacked by**: **"no field in the cavity" is derived from "E = 0 inside the conductor + no charge in the cavity", while the textbook only gives the conclusion**; if there is charge in the cavity, the cavity does have a field and the conclusion must be restated — this library does not develop that case.
- **Signed**: @hpleapfrog · 2026-10-21

### K2 · The causal chain of point discharge (the textbook gives only the qualitative chain, not the quantitative one)

- **Claim**: greater curvature → more concentrated charge → stronger local field → above the air's breakdown field → air ionizes and charge escapes
- **Premises**: the textbook says excess charge is most concentrated at the sharpest point and the field there can be strong enough to remove charge from the conductor; air breaks down at about `3×10⁶ N/C`; lightning rods are pointed and high-voltage lines are smooth (ev-181)
- **Reasoning**: the textbook's qualitative description is strung into a causal chain; both end phenomena (the lightning rod bleeding charge, the smooth high-voltage line avoiding leakage) are in the textbook
- **Evidence**: ev-181
- **Attacked by**: **the middle step — the quantitative relation "curvature — surface charge density — field strength" — is not given by the textbook**, so this entry keeps only the qualitative chain and writes no formula linking `σ` to curvature; the textbook's picture of a lightning rod "continually bleeding induced charge" is also a simplification, and lightning leaders and interception are outside this section's scope.
- **Signed**: @hpleapfrog · 2026-10-21

### K3 · Utilization and prevention are two uses of the same rules (this library's synthesis)

- **Claim**: utilization means "charge the material by design, then move it with a field"; prevention means "give the charge a path (grounding), keep the field out (shielding), or keep the field from concentrating until breakdown (smooth surfaces)"
- **Premises**: §18.8 treats precipitation, xerography, printing, painting and the Van de Graaff generator one by one; §18.7 treats lightning rods, smooth high-voltage lines, the Faraday cage and the car (ev-181)
- **Reasoning**: the examples of the two sections are regrouped as "using the field" and "blocking the field" — each group reduces to K1 or K2
- **Evidence**: ev-181
- **Attacked by**: **this dichotomy is this library's organization; the textbook does not summarize it this way**; xerography also depends on a photoconductor and is not purely a phenomenon of electrostatic equilibrium.
- **Signed**: @hpleapfrog · 2026-10-21

## Change log

| Date | Action | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; adds the last missing piece of Compulsory-3 chapter 9, "prevention and utilization of static electricity", turning the chapter 🟡 → 🟢 | written after reading m42317/m42329 in full, ev-181 | @hpleapfrog |
