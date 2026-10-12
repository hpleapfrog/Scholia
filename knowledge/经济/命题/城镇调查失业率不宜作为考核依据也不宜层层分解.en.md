---
id: kb:econ:prop-unemployment-unsuitable-for-assessment
type: 命题
title: "The urban survey unemployment rate is unsuitable as a basis for assessing employment work, and should not be cascaded down"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 经济 · 统计口径
  学段: 不限
  适用: when you need to check "may the unemployment rate be used as a performance target, or cascaded down to city and county level"
  条件: "**applies to §3(3) of the NBS explainer of 2025-02-28**; this entry states that clause's claim only, **and judges no locality's employment work**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-055]
license: CC-BY-SA-4.0
---

> **English version of [`城镇调查失业率不宜作为考核依据也不宜层层分解.md`](城镇调查失业率不宜作为考核依据也不宜层层分解.md).**

## Statement

The heading of §3(3) of the NBS explainer *What is the survey unemployment rate* is itself the conclusion:

> **The urban survey unemployment rate is unsuitable as a basis for assessing employment work, and should not be cascaded down.**

The clause gives **three reasons** (short quotes):

| # | Reason | Short quote |
|---|---|---|
| 1 | **Employment policy is only one of many influences** | "employment policy, as one of the influencing factors, **can hardly fully offset the influence of other factors, especially swings in economic growth**" |
| 2 | **A high rate does not necessarily mean the employment work is poor** | "**a high unemployment rate does not necessarily mean poor employment work, nor does the converse**" |
| 3 | **Cross-city labour mobility contaminates local figures** | "**labour moving frequently between neighbouring cities affects the unemployment rate of neighbouring areas**", so the rate's **significance at city and county level is relatively limited** |

The same section states the indicator's **genuine purpose**:

> its main role is **to provide a basis for macro-control policies such as fiscal, monetary and employment policy**.

> [!IMPORTANT]
> **This is a statistical agency issuing a usage restriction on its own indicator.**
>
> That is: **the restriction was not added by outside criticism; it is written into the explainer by the publisher.**
> An official indicator explainer that says "don't use it to assess" is rare among the material this repo holds,
> and is worth an entry of its own: **it decides which contexts this number may appear in, and which it may not.**

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-055 | **官方文件** | **高** | [NBS, *What is the survey unemployment rate*](https://www.stats.gov.cn/zs/tjws/tjzb/202301/t20230101_1903672.html), 2025-02-28, **§3 How to read it · (3)** | official public statistical explainer · **cite section headings and short quotes only; no full text reproduced** |

## Argument

### A1 · The restriction is in the heading; no inference needed (no attack yet)

- **Claim**: the urban survey unemployment rate is **unsuitable as an assessment basis**, and **should not be cascaded down**
- **Premise**: the clause's heading reads, in the original, as the two sentences above; the three reasons are set out in the body (ev-055)
- **Reasoning**:
  1. this is "**the original wording of an official release**" — exactly what the [economics](../README.en.md) subject collects
  2. it is **checkable against the source by the reader**, with no inference required
  3. **"should not be cascaded down" is especially concrete**: the clause gives the mechanism by which cascading fails —
     cross-city labour mobility contaminates neighbouring areas' figures,
     so **city- and county-level numbers are not interpretable**; this is not "a little less precise", it is "relatively limited in significance"
- **Evidence**: ev-055
- **Attacked by**: see A2

### A2 · This entry judges no locality, and proposes no alternative indicator (no attack yet)

- **Claim**: this entry states "**the bureau says this indicator should not be used this way**",
  **not "any given locality's employment work is good or bad", nor "what should be assessed instead"**
- **Premise**: the clause says only **not to use the unemployment rate**, and **offers no replacement** (ev-055)
- **Reasoning**:
  1. "so what should employment be assessed on" — **the explainer does not answer, and this repo has found no other source**
  2. so this entry **cannot support "use some other indicator to assess employment"**
  3. the clause also **does not say the rate is useless** — it states in terms that the main role is to underpin macro-control policy. Reading "unsuitable as an assessment basis" as "this number is worthless" is **an over-reach**
- **Evidence**: ev-055
- **Attacked by**: **this restriction is the wording in the 2025-02-28 version of the explainer; this repo has not checked whether earlier versions said the same.**
  The URL path contains `202301`, so the page has been re-published, and **this repo has no idea whether the restriction is new or has always been there.**
  Also: **this repo has not checked whether this restriction is repeated in other official material such as statistical yearbooks or indicator manuals** —
  if it appears only on this page, its force extends no further than this page.
- **Attribution**: @hpleapfrog · 2026-10-12
- **To be added**: the pre-2025-02-28 versions of this page; the corresponding wording of this restriction in other official material

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Every explainer says the unemployment rate matters; none of them says "don't use it to assess".**
>
> What you see in a report is **a number and whether it is good or bad**; what the statistical basis holds is
> **what this number is allowed to be used for, and why it breaks down when moved to a finer level**.
>
> **This repo's mission is to strip noise and hold true information.**
> That contrast is the test: **the level of the number itself, this repo need not repeat (superseded next period);**
> **the boundary its publisher drew around its use is what belongs here.**
> "Does a city's unemployment rate rising show that its employment work went badly" — the question has no answer in any league table,
> while the publisher wrote in terms: **not necessarily, nor does the converse.**

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-12 | Entry created; the subject's third `命题` | topic chosen against the subject boundary after ev-055 was registered | @hpleapfrog |
