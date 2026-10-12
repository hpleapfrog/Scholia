---
id: kb:econ:prop-gdp-three-methods-statistical-discrepancy
type: 命题
title: The three GDP accounting approaches should agree in theory; the difference in practice is called the statistical discrepancy and is permitted
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 经济 · 统计口径
  学段: 不限
  适用: anyone checking whether "production-approach GDP, income-approach GDP and expenditure-approach GDP disagree, so one of them must be wrong"
  条件: "**applies to the accounting framework set out in the NBS explainer of 2021-02-18**; that page gives the three approaches and a qualitative account of the \"statistical discrepancy\", and **this entry checks no actual figure or discrepancy size for any period**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-059]
license: CC-BY-SA-4.0
---

> **English version of [`GDP三种核算方法理论一致但允许统计误差.md`](GDP三种核算方法理论一致但允许统计误差.md).**

## Statement

GDP has three accounting approaches: the **production**, **income** and **expenditure** approaches.

| Approach | Angle | Formula |
|---|---|---|
| **Production** | the **new value created** by resident units in production | `GDP = total output − intermediate input` |
| **Income** | the **income formed** in production | `GDP = compensation of employees + net taxes on production + depreciation of fixed assets + operating surplus` |
| **Expenditure** | the **final use** of goods and services | `GDP = final consumption expenditure + gross capital formation + net exports of goods and services` |

The three approaches describe **one and the same** final result of national economic production,
from three different angles.

**In theory the three results should agree** — in practice they do not. The closing paragraph of
the explainer (short quote):

> **In theory, GDP accounted for by the three different approaches should give the same result,
> but in actual operation, because the data sources differ, results from different calculation
> approaches do differ; this difference is called the statistical discrepancy, and the
> statistical discrepancy is permitted to exist within an acceptable range.**

> [!IMPORTANT]
> Three parts of that sentence have to be read together:
>
> 1. **the difference has a name** — the statistical discrepancy
> 2. **the difference has a cause** — **the data sources differ** (not "somebody miscalculated")
> 3. **the difference is permitted** — **within an acceptable range**
>
> Read part 3 alone and it sounds like the authorities making excuses.
> Part 2 is the load-bearing one: the three approaches use **different data**,
> so the difference **is not an error but a property of the methods themselves**.

### "They disagree" is not "one is wrong"

This is the practical use of the entry. When you see two GDP figures that do not match:

| Situation | What this entry says |
|---|---|
| production-approach GDP ≠ expenditure-approach GDP | **normal**; the difference is the statistical discrepancy |
| "so one of them must be wrong" | **this entry does not support it**; the explainer says the difference is permitted |

**But note the boundary**: the explainer says "**within an acceptable range**".
How large is acceptable — **the explainer gives no threshold, and this repo has checked no other
source**.

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-059 | **官方文件** | **高** | National Bureau of Statistics, *How is GDP accounted?*, 2021-02-18 15:51, [full text](https://www.stats.gov.cn/zt_18555/zthd/sjtjr/d12kfr/tjzsqzs/202302/t20230216_1908936.html) (**whole document**: one paragraph each for the three approaches with their formulas, plus the closing paragraph on the statistical discrepancy) | official public statistical explainer · **cite approach names, formulas and short quotes only; no full text reproduced** |

## Argument

### A1 · Both the three approaches and the qualitative account of the discrepancy are stated by the authority (no attack yet)

- **Claim**: the three approaches **agree in theory**, and the difference in practice **is called
  the statistical discrepancy and is permitted**
- **Basis**: the explainer sets out each approach with its formula, and its closing paragraph
  states agreement in theory, a difference in practice, the name of that difference, its cause in
  differing data sources, and that it is permitted within an acceptable range (ev-059)
- **Reasoning**:
  1. this falls under "**indicator definitions and statistical bases**" — precisely what
     [Economics](../README.en.md) collects
  2. **a reader can open the source and check it word for word**
  3. all three formulas are **hard equalities**, not estimators — so "what the method defines" and
     "what the figures actually differ by" are two layers, and this entry states them separately
- **Evidence**: ev-059
- **Attacked**: see A2, A3

### A2 · This entry checks no actual discrepancy size for any period (no attack yet)

- **Claim**: this entry asserts "**the difference is permitted**",
  **not** "how large the difference usually is", **nor** "how large is acceptable"
- **Basis**: the explainer **gives only a qualitative account — no figure and no threshold**
  (ev-059)
- **Reasoning**:
  1. "production and expenditure-approach GDP usually differ by what percentage" — **the
     explainer does not answer, and this repo has checked nothing**
  2. so this entry **cannot support "any size of difference is fine"** — the explainer says
     "**within an acceptable range**", and this repo does not know how large that range is
  3. nor does this entry say **how the discrepancy appears in the data tables**, **whether it is
     listed separately**, or **whether it disappears after revision** — none of that is checked
- **Evidence**: ev-059
- **Attacked**: **the explainer was published 2021-02-18, more than five years ago.**
  The accounting **framework** is more stable than figures, but whether the method itself was
  adjusted, or the treatment of the discrepancy changed, in those five years **is not checked
  here at all.** This is a direct instance of [Economics](../README.en.md)'s rule "**timeliness
  is the main point of attack**".
- **Attribution**: @hpleapfrog · 2026-10-12
- **To be added**: the three actual figures and the discrepancy for some period; the source of the
  "acceptable range" threshold; how the discrepancy is presented and revised

### A3 · This entry checks no which approach the published quarterly figure uses (no attack yet)

- **Claim**: this entry **does not assert** "the published quarterly GDP figure is computed with
  which of the three approaches"
- **Basis**: the explainer **says only that there are three approaches, not which one is used for
  publication** (ev-059)
- **Reasoning**:
  1. "the NBS publishes quarterly GDP on the basis of the production approach" — **that sentence
     is not on this explainer page**
  2. so this entry **cannot support a claim such as "published GDP is the expenditure result"**
  3. the publication basis is stated on another release, for which this repo has registered a
     separate source — see
     [GDP levels at current prices but growth rates at constant prices](GDP绝对额按现价计算增长速度按不变价计算.en.md)
- **Evidence**: ev-059
- **Attacked**: **the explainer this entry relies on contains no statement of the publication
  basis**; that statement is in a different document (`ev-060`), with its own verification depth
  and entry boundary.
- **Attribution**: @hpleapfrog · 2026-10-12
- **To be added**: the original source for the approach underlying published quarterly GDP
  (already supplied by `ev-060`; see the companion entry)

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Every quarterly GDP release gives one total figure, but none of them states that the three
> approaches should agree in theory.**
>
> What you see in a release is **a number and a growth rate**; what the accounting framework says
> is **that the number has three ways of being computed, that they agree in theory, that the
> difference in practice is called the statistical discrepancy, and that it is permitted**.
>
> **This repo's mission is to remove noise and hold real information.** The substitution is the
> test: **the GDP figure itself need not be repeated here (it is superseded or revised next
> period); the basis that decides "when two numbers disagree, should either be suspect" is what
> belongs here.**
> "Why do production- and expenditure-approach GDP differ?" — a question no release table can
> answer, and the framework states plainly: **the difference is called the statistical
> discrepancy, and it is permitted.**

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-12 | established the entry; one of the two GDP-basis propositions for this subject | topic chosen against the subject boundary after ev-059 was registered | @hpleapfrog |
