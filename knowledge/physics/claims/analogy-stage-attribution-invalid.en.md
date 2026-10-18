---
id: kb:physics:analogy-stage-attribution-invalid
type: 命题
title: "With n=2 one cannot attribute among several equally varying variables"
status: 待审
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 初中至大学
  适用: textbook researchers, reviewers of this repo
  条件: requires the reader to have access to the source texts
edges:
  先修: []
  支持: []
  攻击: ["[proposition: choice of analogy is stage-dependent](analogy-by-stage.en.md#a1)"]
evidence: [ev-016, ev-018]
license: CC-BY-SA-4.0
---

> **English version of [`两个样本无法归因.md`](两个样本无法归因.md).**

## Statement

> [!IMPORTANT]
> **This entry is an attack on argument A1 of [proposition: choice of analogy is stage-dependent](analogy-by-stage.en.md).**
> It does **not claim** "stage is irrelevant"; it claims only **A1's attribution reasoning is invalid**.

The sentence attacked is A1's reasoning:

> "The two books come from the **same publisher**, same subject, **the only salient difference being stage** ⇒ stage is the most likely independent variable"

**"The only salient difference is stage" does not hold.** The quantities varying at once between the two books are at least:

| Variable | OpenStax《Physics》 | OpenStax《College Physics 2e》 |
|---|---|---|
| stage | high school | intro college |
| **author / writing team** | one team | another team |
| **year / edition** | 2020 | 2020 (different edition) |
| **series positioning** | high-school science series | College series |
| **abstraction demanded of the target reader** | lower | higher |

The publisher is indeed the same, but **the publisher was never a possible alternative explanation** —
what can genuinely compete with "stage" are **author team**, **series positioning**, **year of publication** — quantities that **also vary with the book**.

## Basis

| Number | Type | Grade | Locator | License |
|---|---|---|---|---|
| ev-018 | textbook (full text) | low | OpenStax《Physics》Chapter 19 · , m54437 | **CC BY 4.0** |
| ev-016 | textbook (full text) | low | OpenStax《College Physics 2e》§20.3, m42344 | CC BY-NC-SA 4.0 |

> [!NOTE]
> This entry's "basis" is not new textbook content but **a comparison of the properties of already-registered evidence** (same publisher, same subject, different series).
> Such an attack also needs evidence; it just reads **the relations between pieces of evidence**.

## Argument

### A1 · Two data points cannot distinguish arbitrarily many equally varying variables (no attack yet)

- **Claim**: A1 of "choice of analogy is stage-dependent" is **invalid reasoning** (an "invalid reasoning" attack)
- **Premise**: the observation has only **2 points**; these two points take different values on **at least 4 variables** at once (stage / author / series / year)
- **Reasoning**: at n=2, **any** variable taking different values across the two books **fits the data equally well**.
  "Stage causes the difference" and "series positioning causes the difference" are **two equivalent explanations of the same data**,
  and **the data alone cannot choose between them**
- **Evidence**: ev-016, ev-018 property comparison (table above)
- **Attacked**: if one could argue these variables **actually tend to coincide** across the two books (e.g. the author teams greatly overlap,
  the two books are of the same lineage), they would no longer be competing explanations — **but that needs extra evidence, which is currently absent**
- **Attribution**: @hpleapfrog · 2026-10-05

### A2 · This is not "insufficient sample size" but "more variables than data points" (no attack yet)

- **Claim**: describing the problem as "n=2 is too few, just add samples" **leads to the wrong remedy**
- **Reasoning**: if one keeps collecting **same-kind** textbooks (other stages' books from the same publisher),
  stage still varies **in the same direction** as author, series and year — **growing n to 10 may still be ineffective**.
  What is truly needed are samples that **make these variables orthogonal** (e.g. cross-stage **within one series**,
  or different series **at one stage**)
- **Evidence**: (this is a reasoning claim, no independent evidence)
- **Attacked**: if OpenStax's series are in fact written by one team from one template,
  then "author" and "series" are merely **registry-level differences**, not constants — **this needs a testable criterion, which is currently absent**
- **Attribution**: @hpleapfrog · 2026-10-05

## How this attack is knocked down

| Knock-down method | What it needs |
|---|---|
| find cross-stage textbooks **within one series** where the analogy still varies with stage | makes "series" orthogonal, stage still correlates ⇒ A1 weakened |
| find textbooks **at one stage in different series** where the analogy varies with series | shows "series" is the stronger explanation |
| prove the two books' author teams and lineage greatly overlap | removes a competing explanation |

> [!TIP]
> **All three knock-down methods need evidence "outside the repo"** — which precisely shows:
> the repo's current 2 samples **cannot falsify themselves**. The attack stands, precisely because it points out this closure.

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry: the repo's first measured test of the "argument attacked" mechanism | Issue #8 extension | @hpleapfrog |
