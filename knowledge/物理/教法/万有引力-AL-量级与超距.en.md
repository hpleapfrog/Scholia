---
id: kb:physics:method-gravitation-al-magnitude
type: 教法
title: "Universal gravitation · Advanced: how large is the force between two 10 kg balls"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶（AL）
  适用: students who can already substitute into F = GmM/r² but have no feel for how "weak" gravity is
  条件: can already multiply and divide using scientific notation
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a3)"]
  攻击: []
knowledge_point: ["[law of universal gravitation](../知识点/万有引力定律.md)"]
evidence: [ev-037]
license: CC-BY-SA-4.0
---

> **English version of [`万有引力-AL-量级与超距.md`](万有引力-AL-量级与超距.md).**

## Method

The textbook's `[AL]` hint takes a path **opposite to "celestial bodies"**: **use objects at hand and compute gravity down to invisibly small.**

### 1 · First make them hesitate, then make them calculate

> `Ask the students what the attraction would be between two 10 kg balls separated by a`
> `distance of 1.0 m. Could they feel it?`
> `Later, ask them to calculate it after they have done some similar calculations.`

**The order is designed**: first **guess** (are you willing to defend "you could feel it"), then **calculate**.

The answer the textbook gives:

```
F = G·mM/r² = (6.67×10⁻¹¹)(10 × 10 / 1²) = 6.67×10⁻⁹ N
```

**The job of this number is not "getting the arithmetic right"; it is to give a sense of magnitude for "gravity is weak"** —
weak that two 10 kg balls **could never be felt** between them.

### 2 · Make "action at a distance" explicit

> `Ask if anyone thinks it is strange or even mysterious that a force can act at a distance`
> `across empty space. Ask the students to compare and contrast gravitational force with`
> `magnetic and electrostatic forces.`
> `Note how much force at a distance is like magic or having superpowers.`

**The textbook does not dodge this; it treats it as a point worth stopping to discuss.**

### 3 · Make clear why G is "universal" and g is not

> `Ask if anyone can explain why G is a universal constant that applies anywhere in the`
> `universe. Have them discuss the idea that the laws of physics are the same everywhere`
> `and that, at one time, people were not so sure about this.`
> `Emphasize that g is not a universal constant.`

**This item also carries a point about the history of ideas**: **"the laws of physics are the same everywhere" was itself once uncertain.**

### 4 · The difference between special and general relativity

> `Ask if anyone knows the difference between special relativity and general relativity.`
> `Special relativity is a theory of spacetime and applies to observers moving at constant`
> `velocity. General relativity is a theory of gravity and applies to observers that are`
> `accelerating. General relativity is broader and includes special relativity, which was`
> `published first.`

### 5 · Have students memorize three values

> `Have the students memorize the values of G, g, and π to three significant figures.`

## Conditions of use

| Dimension | Value |
|---|---|
| Level tier | **AL** (textbook marker `[AL]`) |
| Prerequisites | can multiply and divide in scientific notation; knows the concepts of Newton's force and Coulomb's force |
| Cognitive load | medium-high — carrying **order of magnitude**, **action at a distance** and **relativity** all at once |

## Contraindications

| Who or situation it does not apply to | Basis | Strength |
|---|---|---|
| **students not yet fluent in multiplying and dividing in scientific notation** | the whole point of section 1 rests on the result `6.67×10⁻⁹ N`; if they cannot compute it, all that is left is the adjective "very small" | **strong** — inferred from the nature of the practice |
| students who have not yet told mass from weight | the textbook has a separate `[BL]` hint checking exactly this (`Check to make sure students are clear about the distinction between mass and weight`) | **medium** (the textbook states the order explicitly: BL comes first) |
| students **outside this tier** (AL) | the textbook marks exactly this passage `[AL]`; the BL and OL tiers get different suggestions | **medium** — the marker explicitly delimits the range, but "not marked" still does not mean "does not apply", only **untested** |

## Risks

| Where it can go wrong | Why |
|---|---|
| "'action at a distance is like magic' is taught as a conclusion" | the textbook's wording is `Note how much force at a distance is like magic or having superpowers` — **an analogy used to acknowledge that it is counterintuitive**, not an explanation. Teach it as a conclusion and students are pushed toward "physics cannot explain this either" |
| special / general relativity taught as two parallel theories | the relation the textbook gives is that **general is broader and includes special**, and that **special was published first**. Taught as parallel, that layer is lost |
| formal demonstrations like the five `sin` expressions steal the show | this entry lands on **a sense of magnitude**, not on mathematical technique |
| calculating before guessing | the textbook is explicitly `Ask … Could they feel it?` **and then** `Later, ask them to calculate it`. Reverse the order and you lose that gap |

## Evidence

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-037 | textbook (full text) | low | OpenStax《Physics》 Chapter 7 · Newton's Law of Universal Gravitation and Einstein's Theory of General Relativity, [m54189](https://github.com/openstax/osbooks-physics/blob/main/modules/m54189/index.cnxml) | **CC BY 4.0** |

## Argument

### M1 · Designated by the textbook for the AL tier (no attack yet)

- **Claim**: this is the practice the textbook designates for advanced students
- **Premise**: the Teacher Support of m54189 marks each of the items above `[AL]` (ev-037)
- **Reasoning**: the tier marker is the textbook's designation for that passage
- **Evidence**: ev-037
- **Attacked**: **"textbook-designated" ≠ "measured to be effective"**;
  and the textbook puts "relativity" into this `[AL]` hint, **but it belongs to a knowledge point this
  repo has not yet built** (see the gap section of [law of universal gravitation](../知识点/万有引力定律.md))
- **Attribution**: @hpleapfrog · 2026-10-05

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (#8 batch conversion · batch 4) | Issue #8 | @hpleapfrog |
