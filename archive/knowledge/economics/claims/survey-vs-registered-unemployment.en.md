---
id: kb:econ:prop-survey-vs-registered-unemployment
type: 命题
title: "The survey and the registered urban unemployment rate are two different bases and cannot be compared or subtracted"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 经济 · 统计口径
  学段: 不限
  适用: when you need to check "may these two unemployment figures be set side by side, or subtracted"
  条件: "**applies to the three differences set out in the NBS explainer of 2021-02-18**; that explainer gives the **classification** of the differences only, and **this entry has verified no figure for any period**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-056]
license: CC-BY-SA-4.0
---

> **English version of [`调查失业率与城镇登记失业率是两个不同口径.md`](调查失业率与城镇登记失业率是两个不同口径.md).**

## Statement

The NBS explainer *What is the difference between the survey unemployment rate and the
registered urban unemployment rate* states that the difference between the two figures
**"is mainly reflected in the following three respects"**:

| # | Difference | Survey unemployment rate | Registered urban unemployment rate |
|---|---|---|---|
| 1 | **Statistical method** | the statistical agency runs a **labour force survey**, with interviewers **visiting households** to collect employment and unemployment information | the **Ministry of Human Resources and Social Security** computes it from **administrative records of registration** at employment services agencies |
| 2 | **Definition of employment and unemployment** | uses the **international standard recommended by the ILO**: employed = worked 1 hour or more in the survey week, or was on the payroll but absent; unemployed = currently without work, actively seeking work, and able to start immediately if suitable work came up | an unemployed person is an urban resident of working ability who wants work, is out of work, **and has registered as unemployed at a public employment or talent services agency** |
| 3 | **Statistical coverage** | the resident population **aged 16 and over, regardless of where their household registration is or what type it is** | the resident population **within working age** (16 and over until legally entitled to basic pension insurance benefits) |

> [!IMPORTANT]
> **Among the three differences, the word "registered" in the second is the watershed.**
>
> The registered rate requires the unemployed person to **go and register at a public employment services agency** —
> that is: **if you did not register, you are not counted.** This is a completely different test from
> the survey's "searched for work": one judges **whether an administrative procedure was gone through**,
> the other judges **whether work was searched for in fact**.
>
> So the two figures are **not two measurements of one thing; they are two different things**.
> A statement like "A is 2 percentage points above B" **does not hold on the basis** —
> the gap contains the **definition difference, the coverage difference and the collection-method difference at once**, and cannot be unpicked.

### All three differences together are why subtraction fails

| Difference | If ignored, you would read it as |
|---|---|
| Statistical method | the two figures come from the same collection system, only the basis differs |
| Definition of employment and unemployment | "unemployed" is one concept, only the arithmetic differs |
| Statistical coverage | the denominator is the same group of people |

**All three differ at once**, so **the difference has no meaning**.

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-056 | **官方文件** | **高** | [NBS, *What is the difference between the survey unemployment rate and the registered urban unemployment rate*](https://www.stats.gov.cn/zt_18555/zthd/sjtjr/d12kfr/tjzsqzs/202302/t20230216_1908907.html), 2021-02-18, **all three paragraphs** | official public statistical explainer · **cite the names of the differences and short quotes only; no full text reproduced** |

## Argument

### A1 · The three differences are listed by the authority, not assembled by this repo (no attack yet)

- **Claim**: the two differ on **statistical method, definition of employment and unemployment, and statistical coverage**
- **Premise**: the explainer lists them out as "first … second … third …", and its publisher is the NBS (ev-056)
- **Reasoning**:
  1. this is "**indicator definition and statistical basis**" — exactly what the [economics](../README.en.md) subject collects
  2. it is **falsifiable by the reader against the source, clause by clause**
  3. **all three differing at once is the crux** — had only one differed, the gap might be correctable;
     **with three differing at once, it is not**
- **Evidence**: ev-056
- **Attacked by**: see A2

### A2 · This entry states the classification of differences only, and has verified no figure (no attack yet)

- **Claim**: this entry states "**the two differ on three counts**",
  **not "the two figures differ by so much in period X", nor "which difference contributes most"**
- **Premise**: the explainer **only lists the three differences and quantifies none of them** (ev-056)
- **Reasoning**:
  1. "the two figures differ by 1.5 percentage points; how much of that comes from the registration threshold and how much from the age range" — **the explainer does not answer, and this repo has not found another source**
  2. so this entry **cannot support a quantitative claim such as "the registered rate systematically understates"** — the direction is probably right, but **this repo has no evidence**
  3. equally: **this entry has not checked whether the registered rate is still being published**, nor whether the two are released at the same frequency
- **Evidence**: ev-056
- **Attacked by**: **the explainer was published on 2021-02-18, more than five years ago.**
  Whether the registered rate is still published monthly and whether its basis has been adjusted since, **this repo has not checked at all.**
  This is a direct application of the [economics](../README.en.md) subject's rule that
  "**timeliness is the main point of attack**" — this entry describes the classification of bases,
  which is stabler than figures, but **that stability has not been verified by this repo.**
  Also: **this repo has not read the Ministry's own basis document**, only the NBS's retelling of it.
- **Attribution**: @hpleapfrog · 2026-10-12
- **To be added**: whether this explainer has been updated since 2021; the Ministry's original definition of the registered rate

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Every comparison piece sets the two unemployment figures side by side; none of them writes out "the two do not share a basis".**
>
> What you see in such a piece is **two lines and a gap**; what the statistical basis holds is
> **who collected each line, under whose definition, counting which population**.
>
> **This repo's mission is to strip noise and hold true information.**
> That contrast is the test: **the two values themselves, this repo need not repeat (superseded next period);**
> **the basis that decides whether they may be subtracted is what belongs here.**
> "How much higher is the survey rate than the registered one" — the question has no answer in any side-by-side chart,
> while the basis says in terms: **this is not two measurements of one thing, it is two different things.**

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-12 | Entry created; the subject's second `命题` | topic chosen against the subject boundary after ev-056 was registered | @hpleapfrog |
