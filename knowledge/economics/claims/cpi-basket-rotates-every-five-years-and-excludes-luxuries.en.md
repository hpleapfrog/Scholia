---
id: kb:econ:prop-cpi-basket-rotates-every-five-years-and-excludes-luxuries
type: 命题
title: "The CPI basket changes every five years, and excludes luxuries and investment goods"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-13
updated: 2026-10-13
scope:
  学科: 经济 · 统计口径
  学段: 不限
  适用: when you need to check "how often the CPI basket changes", or "why the CPI cannot hold house prices and luxuries"
  条件: "**applies to the NBS page dated 2024-11-29**; the URL path date on that page does not match the date printed on the page (see **Attacked by**), and **this entry has not checked whether the base year has rotated since 2024-11-29**"
edges:
  先修: []
  支持: [kb:econ:miscon-cpi-is-inflation-rate]
  攻击: []
evidence: [ev-061, ev-062]
license: CC-BY-SA-4.0
---

> **English version of [`CPI的篮子每五年换一次且不含奢侈品与投资品.md`](CPI的篮子每五年换一次且不含奢侈品与投资品.md).**

## Statement

**The CPI uses a "fixed basket", that basket is replaced every five years, and it explicitly excludes luxuries and investment goods.**

The NBS's *How the CPI is compiled* states (short quote):

> In compiling a price index, a fixed quantity of goods and services is called a "basket".
> Per the survey plan, the **"basket" is replaced every five years**;
> the current CPI's "basket" is **fixed at 2020**.

The same page sets the boundary of what the basket covers (short quote):

> China's statistical department selects a set of goods and services that residents
> regularly consume over a given period, that matter relatively much to their lives,
> that are representative, and that are fixed in quantity, to serve as the "basket".
> **Luxuries, investment goods and the like are not included.**

### The structure of the basket

| Item | Value | Source |
|---|---|---|
| Major groups | **8** (food, tobacco and liquor; clothing; housing; household goods and services; transport and communication; education, culture and recreation; health care; other goods and services) | ev-061 |
| Elementary classes | **268** | ev-061 |
| Elementary classes in the previous round | **262** (raised from 262 to 268 at the 2021–2025 base year) | ev-062 |
| Classification reference | the UN's **COICOP** and China's *Household Consumption Expenditure Classification* | ev-061 ev-062 |
| Source of the weights | household income-and-expenditure survey data on residents' consumption expenditure, supplemented by administrative records, special surveys and expert assessment | ev-061 |
| First year of the fixed-base series | **2001**, with the comparison base fixed at 2000, changed every 5 years | ev-061 |
| Aggregation formula | **chained Laspeyres** | ev-061 |

### The rule for rotating the base year

The NBS interview (ev-062) states:

> Per the statistical system, **China's CPI, PPI and residential property sales price index rotate their base year every five years** …
> China's CPI will take years **ending in 5 and 0 as the base year**, selecting the "basket" in the base year and keeping it unchanged for five years.

What the 2021 rotation actually changed (ev-062):

- Elementary classes **262 → 268**, newly adding **takeout meals, maternal and infant care services, new-energy cars, wearable smart devices, ride-hailing fares** and other emerging goods and services
- Weights: food, tobacco and liquor **−1.2**, clothing **−1.7**, education, culture and recreation **−0.5**, other goods and services **−0.4** (percentage points)
- Weights: housing **+2.1**, transport and communication **+0.9**, health care **+0.9** (percentage points)
- The weight calculation **removed the distortions of African swine fever and the pandemic** from household consumption expenditure
- The rotation moved CPI **year-on-year** indices by about **0.03 percentage points** on average

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-061 | **Official document** | **High** | [NBS, *How the CPI is compiled*](https://www.stats.gov.cn/zs/tjws/zytjzbqs/jmxxggzs/202411/t20241127_1957589.html), page-dated **2024-11-29 10:00**, **§2 The basket and the weights** and **§6 How the CPI is computed** | Official public statistical explainer · **cites class counts, method names and short quotes only; no formula images or full text reproduced** |
| ev-062 | **Official document** | **High** | [NBS, *Interview with the head of the Urban Survey Department on the base-year rotation of price indices*](https://www.stats.gov.cn/xxgk/jd/sjjd2020/202102/t20210210_1813322.html), dated **2021-02-10**, **all four Q&A pairs** | Official public statistical explainer · **cites class counts, percentage points and short quotes only; no full text reproduced** |

## Argument

### A1 · "Luxuries and investment goods are excluded" is a scope limit written in the specification (not yet attacked)

- **Claim**: the CPI basket **explicitly excludes luxuries, investment goods and the like** — this is not the CPI missing them; the survey plan simply defines them out
- **Premise**: ev-061 §2(2) states "**Luxuries, investment goods and the like are not included**"
- **Reasoning**:
  1. This is "what an indicator's scope is" — exactly what the [economics](../README.en.md) discipline collects
  2. It forms a **second, distinct layer of limitation** alongside [treating the CPI as the inflation rate](../misconceptions/cpi-is-inflation-rate.en.md): that entry says "the CPI covers only the resident-consumption domain and does not stand for the whole of society"; this one says "**even within resident consumption, luxuries and investment goods are struck out**"
  3. So "my cost of living rose faster than the CPI" has **two separately checkable causes**: your spending mix differs from the basket's weights, **and** you bought things the basket never held
- **Evidence**: ev-061
- **Attacked by**: see A2

### A2 · The basket is fixed for five years, and this entry may already be out of date (not yet attacked)

- **Claim**: this entry states the contents of **the page dated 2024-11-29**, in which "the current basket is fixed at 2020" was the wording **at that time**
- **Premise**: ev-061 writes "the current CPI's basket is fixed at 2020"; ev-062 writes "rotate every five years" and "years ending in 5 and 0"
- **Reasoning**:
  1. By ev-062's own rule, **the next base year is 2025**, so the rotation should have occurred in early 2026
  2. **This repo read only the page dated 2024-11-29** — whether the page has since replaced "fixed at 2020" with "fixed at 2025", this repo does not know
  3. This is another instance of the [economics](../README.en.md) rule that **timeliness is the main point of attack**: **a sentence that hard-codes "the current round" has a five-year shelf life**
- **Evidence**: ev-061, ev-062
- **Attacked by**: **the publication date printed on ev-061 (2024-11-29) does not match the date in its URL path (`t20241127`)** — this repo cannot determine the real publication date, nor whether the page has been republished; this is the same problem as `ev-058`. Also: **this repo has not checked any base-year rotation after 2024-11-29** — by ev-062's rule 2025 ought to be the new base year, but **whether the rotation has happened, and what the new basket's classes and weights are, this repo has not read in any official source**. **This entry cannot be used to claim that "the basket is still the 2020 version as of today".**
- **Author**: @hpleapfrog · 2026-10-13
- **To be added**: the official release for the 2025 base-year rotation; any update to the ev-061 page after 2024-11-29

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Any economics explainer tells you "the CPI is a basket of goods"; none tells you the basket is replaced only every five years, and that it explicitly leaves out luxuries and investment goods.**
>
> The latter two are written in the bureau's own methodology note, and almost never survive retelling:
> **"replaced every five years" means the basket can lag the consumption structure by up to five years;
> "luxuries and investment goods excluded" means house prices and luxury price rises do not exist inside the CPI — not a low weight, not in the basket at all.**
>
> **This library's mission is to remove noise and store real information.**
> "The CPI is a basket of goods" is boilerplate.
> "The basket changes every five years, excludes luxuries and investment goods, has 8 major groups and 268 elementary classes, and takes its weights from the household survey" — these are **checkable scope definitions, one by one**, and are what this library should hold.

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-13 | Entry created; `ev-061` and `ev-062` registered, filling the "CPI compilation method, basket, weights, base year — all absent" gap in "What is still missing" | ev-061/062 registered; topic selected by discipline boundary | @hpleapfrog |
