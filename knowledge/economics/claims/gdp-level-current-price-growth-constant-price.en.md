---
id: kb:econ:prop-gdp-level-current-price-growth-constant-price
type: 命题
title: GDP levels are at current prices and growth rates at constant prices; the two use different price bases
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 经济 · 统计口径
  学段: 不限
  适用: anyone checking whether "GDP totals and GDP growth rates can be derived from each other", or confirming which price basis a given GDP figure uses
  条件: "**applies to the basis stated in the note under Table 1 of the NBS's quarterly preliminary GDP release**; that note is a standing footnote on every release, and **this entry checks no actual figure for any period** (the Q3 2025 Table 1 figures quoted below are not stored as knowledge; they appear only to show the table's structure)"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-060]
license: CC-BY-SA-4.0
---

> **English version of [`GDP绝对额按现价计算增长速度按不变价计算.md`](GDP绝对额按现价计算增长速度按不变价计算.md).**

## Statement

In every quarterly preliminary GDP release the NBS publishes, the first note under Table 1 reads:

> **Levels are computed at current prices, growth rates at constant prices.**

That is: **the two columns of one table use different price bases.**

| Column | Price basis | Meaning |
|---|---|---|
| **Level (100 million yuan)** | **current prices** | value computed at the prices of the period |
| **Year-on-year growth (%)** | **constant prices** | growth with price change removed |

> [!IMPORTANT]
> This is the concrete landing point of the line "**current prices read as constant prices**" in
> the [Economics](../README.en.md) README.
>
> Intuitively, "how much the total grew" and "the growth rate" ought to be two ways of saying one
> thing — **here they are not**. The level **contains price change**; the growth rate **does
> not**.
>
> So dividing one year's level by another's to check the growth rate **yields a different
> number**, and that difference **is not somebody's error — the two bases simply differ**.

### Constant prices have a base year that changes

The annex to the same release states how constant prices are computed:

> Value added at constant prices is computed by the fixed-base method; **the base year currently
> changes once every five years, and the base year for value added at constant prices from 2021
> to 2025 is 2020.**

| Element | Statement |
|---|---|
| **Method** | fixed base |
| **Change frequency** | once every five years |
| **Current base year** (2021–2025) | **2020** |

> [!NOTE]
> Because the base year changes every five years, **growth rates cannot be read straight across a
> base change**. This entry **does not check** the specific splicing rule at a base change, nor
> what the base year becomes from 2026.

### Quarter-on-quarter growth is "seasonally adjusted"

The note under Table 3 of the same release reads:

> **Quarter-on-quarter growth rates are the growth rates against the previous quarter after
> seasonal adjustment.**

So that column is **not the raw quarter-on-quarter rate** either — it has had seasonal factors
removed.

| Growth column | Note it comes from | Basis |
|---|---|---|
| Year-on-year | Table 2 note: against the same quarter of the previous year | against the same quarter a year earlier; **price basis per the Table 1 note** |
| Quarter-on-quarter | Table 3 note: seasonally adjusted, against the previous quarter | **seasonally adjusted**, not raw |

### Quarterly GDP is accounted for on the basis of the production approach

Annex §1.1 of the same release states:

> **The quarterly GDP published by the National Bureau of Statistics is the result accounted for
> on the basis of the production approach.**

This fills the gap left by
[GDP's three approaches should agree in theory](gdp-three-methods-statistical-discrepancy.en.md):
all three approaches are valid, but **the published quarterly figure rests on the production
approach**.

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-060 | **官方文件** | **高** | National Bureau of Statistics, *Preliminary national accounts for Q3 2025*, 2025-10-21 09:30, [full text](https://www.stats.gov.cn/sj/zxfb/202510/t20251021_1961646.html) (**four passages verified**: the Table 1 note 1, the Table 3 note, annex §1.1 and annex §2.3.2) | official public statistical release · **cite table notes and short quotes only; no figures reproduced** |

## Argument

### A1 · The current/constant split is written in the release's own note (no attack yet)

- **Claim**: GDP **levels are at current prices and growth rates at constant prices**
- **Basis**: note 1 under Table 1 of every preliminary release reads exactly so (ev-060)
- **Reasoning**:
  1. this falls under "**indicator definitions and statistical bases**" — precisely what
     [Economics](../README.en.md) collects
  2. **a reader can open the source and check it word for word**
  3. this is the **publisher's own statement of its table's basis**, not a third-party inference —
     a table footnote is part of the release itself
  4. the note **appears on every release** (this entry checked only Q3 2025, but it is a standing
     footnote, not a one-off remark)
- **Evidence**: ev-060
- **Attacked**: see A2, A3

### A2 · This entry checks no actual figure for any period (no attack yet)

- **Claim**: this entry asserts "**the two columns use different price bases**",
  **not** "GDP in period X was N", **nor** "the conversion between growth rate and level"
- **Basis**: this entry relies on **the table notes**, not on Table 1's figures (ev-060)
- **Reasoning**:
  1. this entry **can hold without any period's figures** — as long as the note stands, the basis
     stands
  2. conversely, this entry **cannot be used to verify or challenge any period's specific numbers**
  3. "does dividing the current-price growth rate by the constant-price growth rate give a price
     index" — **the release does not give that conversion, and this repo has checked nothing**
- **Evidence**: ev-060
- **Attacked**: **this entry checked one release only.** Whether the note is worded differently on
  an earlier or later release **has not been compared here**. Further: **this repo has registered
  no actual GDP figure for any period** — the Q3 2025 figures quoted above **are not stored as
  knowledge** and appear only to show the table's structure. The release does not say **which
  year the base moves to next or how the splice works**, and this repo has checked no other source.
- **Attribution**: @hpleapfrog · 2026-10-12
- **To be added**: comparison of the notes across releases; the official current-to-constant price
  conversion; the rule for the next base change

### A3 · Verification depth of the annex here is "four passages", not the whole document (no attack yet)

- **Claim**: this entry also covers **quarterly GDP resting on the production approach**,
  **the constant-price base year changing every five years with 2021–2025 based on 2020**, and
  **quarter-on-quarter growth being seasonally adjusted**
- **Basis**: the three sentences are in annex §1.1, annex §2.3.2 and the Table 3 note respectively
  (ev-060)
- **Reasoning**:
  1. all three are **basis statements** of the same kind as this entry's subject, so they are
     collected together
  2. "quarterly GDP rests on the production approach" **fills the gap the companion entry left**
  3. but the annex *Notes on China's quarterly GDP accounting* has five sections, and this entry
     **verified only §1.1, §2.3.2 and the two table notes**
- **Evidence**: ev-060
- **Attacked**: **annex §2.1 classification systems, §2.2 data sources, §3 data revision, §4 data
  quality assessment and §5 release schedule were not checked one by one here.**
  In particular **§3 "quarterly GDP data revision"** — which states plainly that preliminary
  figures are revised afterwards — and this entry **checks no revision trigger, frequency or
  magnitude**. Further: **this repo has not read the official documentation of the NBS-SA seasonal
  adjustment software**, so what "seasonally adjusted" actually removes is known here only from the
  annex's overview sentence.
- **Attribution**: @hpleapfrog · 2026-10-12
- **To be added**: the revision rules in annex §3; the official NBS-SA documentation; comparison of
  the notes across releases

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Every GDP release gives a level column and a growth column, but neither states that the two
> use different price bases.**
>
> What you see in a release is **a figure in hundred millions and a percentage, side by side**;
> what the table note says is **the left is at current prices, the right at constant prices, and
> the right's base year changes every five years**.
>
> **This repo's mission is to remove noise and hold real information.** The substitution is the
> test: **the figures themselves need not be repeated here (they are superseded or revised next
> period); the basis that decides "can these two numbers be derived from each other" is what
> belongs here.**
> "How much did GDP grow" has a number in every table — but "is this number at current or constant
> prices" — **the note has it, and the answer runs against intuition.**

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-12 | established the entry; one of the two GDP-basis propositions for this subject, and it fills the "which approach is published" gap left by the companion entry | topic chosen against the subject boundary after ev-060 was registered | @hpleapfrog |
