---
id: kb:econ:prop-unemployment-three-conditions
type: 命题
title: "Being unemployed is defined by three conditions that must hold at once"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 经济 · 统计口径
  学段: 不限
  适用: when you need to check "does this person count as unemployed", or whether two unemployment figures share a basis
  条件: "**applies to the basis described in the NBS explainer of 2025-02-28**; this entry states that basis only, **and judges no individual person**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-055]
license: CC-BY-SA-4.0
---

> **English version of [`失业人口由三个条件界定.md`](失业人口由三个条件界定.md).**

## Statement

Section 1 of the NBS explainer *What is the survey unemployment rate* states that
**an unemployed person must satisfy three conditions at once**:

| # | Condition | Short quote |
|---|---|---|
| 1 | **No work** in the survey reference week | "in the survey reference week [they had] **no work**" |
| 2 | **Searched for work** at some point before the survey | "before the survey point, within some period, [they] **searched for work**" |
| 3 | **Able to start immediately** if suitable work came up | "if suitable work were available, [they would be] **able to start immediately**" |

The same section names two other groups, **disjoint** from the unemployed:

| Group | Condition | Short quote |
|---|---|---|
| **Employed** | worked **1 hour or more** in the reference week for pay or operating income; **or** was on the payroll but absent (leave, temporary shutdown, etc.) | both categories count as employed |
| **Non-labour-force** | has no work, and **does not look for work** or **cannot go to work** | — |

The relation is: **population aged 16 and over = labour force (employed + unemployed) + non-labour-force**,
and **the three states convert into one another** — in the source:

> When an employed person loses their job, **if they look for work and can go to work they become unemployed; otherwise they become non-labour-force**.

> [!IMPORTANT]
> **The second condition is the one most easily forgotten.**
>
> "Out of work" is not the same as "unemployed": **a person who does not look for work goes into the non-labour-force, not into the unemployed.**
>
> That directly explains a sentence in section 3 of the same page — in a downturn,
> "some job-seekers lose heart and stop searching, **moving from unemployed into non-labour-force, and the rate falls**".
> In other words: **the rate can fall at a time when employment has not improved.**
> Without the second condition, that fall reads as good news.

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-055 | **官方文件** | **高** | [NBS, *What is the survey unemployment rate*](https://www.stats.gov.cn/zs/tjws/tjzb/202301/t20230101_1903672.html), 2025-02-28, **§1 Concept** | official public statistical explainer · **cite section headings and short quotes only; no full text reproduced** |

## Argument

### A1 · The three conditions are the definition itself, not a filter (no attack yet)

- **Claim**: whether a person is counted as unemployed **is decided by these three conditions together**
- **Premise**: the page writes them as "an unemployed person is one who satisfies the following three conditions" (ev-055)
- **Reasoning**:
  1. this is "**indicator definition and statistical basis**" — exactly what the [economics](../README.en.md) subject collects
  2. it is **falsifiable by the reader against the source**, with no inference required
  3. **drop one condition and the verdict flips**: drop the second and the unemployed count rises;
     drop the third and the seriously ill would be counted in. This is a definition, not an estimate
- **Evidence**: ev-055
- **Attacked by**: see A2

### A2 · This entry judges no individual, and checks no basis beyond that page (no attack yet)

- **Claim**: this entry states "**how the bureau's basis is written**",
  **not "whether this or that person is unemployed"**
- **Premise**: whether the three conditions hold is settled by **how the monthly household interview actually asks**,
  and the page **does not say how the interviewer asks** (ev-055)
- **Reasoning**:
  1. does "searched for work" mean submitting an application, or asking around? does "immediately" mean within hours, or days? **the page does not say**
  2. so this entry **cannot support "so-and-so is unemployed" or "so-and-so is not"**
  3. equally: **this entry states only what the page says** — whether the ILO's original standard matches it word for word, **this repo has not checked**
- **Evidence**: ev-055
- **Attacked by**: **this repo has not read the ILO's original standard**, only the NBS's retelling of it.
  "Do the NBS's three conditions match the ILO's standard word for word" — **this repo has not investigated.**
  Also: **this repo has not checked the actual wording of the survey questionnaire**, nor the revisions this basis has undergone.
- **Attribution**: @hpleapfrog · 2026-10-12
- **To be added**: the ILO's original standard on employment and unemployment statistics; the actual wording of the labour force survey questionnaire

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Every news report gives the unemployment figure; none of them writes out "if you don't look for work you are not counted as unemployed".**
>
> What you see in the news is **a percentage**; what the statistical basis holds is **which three groups the denominator is made of, and how a person crosses from one to another**.
>
> **This repo's mission is to strip noise and hold true information.**
> That contrast is the test: **the figure for this period, this repo need not repeat (superseded next period);**
> **the basis that decides how the figure is computed is what belongs here.**
> "Is a fall in the unemployment rate good news" — the question has no answer in any news report,
> while the basis says in terms that such a fall can happen when employment has not improved.

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-12 | Entry created; **the subject's first `命题`** | topic chosen against the subject boundary after ev-055 was registered | @hpleapfrog |
