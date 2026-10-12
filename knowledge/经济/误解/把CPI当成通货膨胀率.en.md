---
id: kb:econ:miscon-cpi-is-inflation-rate
type: 误解
title: Taking the CPI to be the inflation rate
status: 有效
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 经济 · 统计口径
  学段: 不限
  适用: anyone who quotes the CPI as a synonym for "the inflation rate"
  条件: **applies to the uses of the CPI as set out on that NBS explainer page**; the page says only what the CPI can and cannot represent, and **this entry checks no actual CPI figure for any period** (the 2022 national CPI of 102.0% on that page is the page's own worked example, not a release verified by this repo)
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-058]
license: CC-BY-SA-4.0
---

> **English version of [`把CPI当成通货膨胀率.md`](把CPI当成通货膨胀率.md).**

## Statement

"The CPI is the inflation rate" — almost nobody pushes back on this in everyday use.
**The National Bureau of Statistics' own explainer states that it does not hold.**

The original wording (short quote):

> **Strictly speaking, the CPI is not the same thing as the inflation rate**, because **the CPI
> only reflects price changes in the sphere of household consumption and cannot represent
> changes in the overall price level of the whole society**; from changes in the CPI, however,
> one can see the general trend of price movements and indicate the degree of
> inflation (deflation) to some extent.

Three parts come apart here:

| # | What the explainer says | What it means |
|---|---|---|
| 1 | the CPI is not the same thing as the inflation rate | **the two are not the same quantity** |
| 2 | it only reflects household consumption | the CPI's coverage is **consumption**, not the whole of society |
| 3 | it indicates inflation to some extent | the CPI **can show a trend, but cannot substitute for the number** |

> [!IMPORTANT]
> Part 3 is not "so the CPI is useless"; it is that **"can show a trend" and "is identical to"
> are two different things**. The explainer positions the CPI as **one** of the measures that is
> "widely applied" — **"widely used" is not "the same as"**, and that difference is exactly
> what this misconception most often erases.

### The CPI is a *relative number*, not a *rate*

The explainer's basic definition of the CPI is:

> The Consumer Price Index (CPI) is a **relative number** measuring the overall change in the
> price level of goods and services consumed by households over a given period, reflecting
> comprehensively the trend and degree of change in that price level.

The words **"relative number"** are the key — it describes **change**, not the level of some
total. Reading it as "the inflation rate" turns a *magnitude of change* into *a measure of
something in itself*.

## Frequency

> [!WARNING]
> **This entry has no quantitative data.**
>
> This repo **has not counted** how many reports, textbooks or commentaries call the CPI
> directly "the inflation rate". "Almost nobody pushes back" is a qualitative observation,
> **not a measurement**.
>
> The only checkable basis right now is **the explainer's own statement that the two are not the
> same**. It proves "the CPI is not the inflation rate", but it **cannot** prove "how many people
> treat them as one" — **these are two different things, and the first must not be passed off as
> the second.**

## Why record it

This misconception is harder to correct than the [418 one](../../计算机/误解/418不是规范里的状态码.en.md)
because **its error is not obvious in direction**:

- Reading the CPI as the inflation rate, the trend read off **over a small window is often right**
  (the explainer itself says it "indicates the degree of inflation to some extent")
- so using it in a judgment **often does not go wrong immediately** — what goes wrong is using it
  for a judgment that needs **the overall price level of the whole of society**
- and "the overall price level of the whole of society" **has no single everyday number at all**,
  so the error is rarely met head-on

> [!NOTE]
> In other words: the cost of this misconception lies **not in "miscalculating" but in "picking
> the wrong coverage"** — exactly the "picking the wrong basis" family that
> [Economics](../README.en.md) is about.
> It can only be falsified by returning to the statistical basis; observational evidence fails
> here too.

## Argument

### M1 · The NBS explainer states plainly that the CPI is not the inflation rate (no attack yet)

- **Claim**: the CPI **is not** the inflation rate
- **Basis**: the first of the explainer's "main uses of the CPI" contains "strictly speaking, the
  CPI is not the same thing as the inflation rate", with the reason "the CPI only reflects price
  changes in the sphere of household consumption and cannot represent changes in the overall
  price level of the whole society" (ev-058)
- **Reasoning**:
  1. this falls under "**indicator definitions and statistical bases**" — precisely what
     [Economics](../README.en.md) collects
  2. **a reader can open the source and check it word for word**
  3. this is the publishing body's **boundary statement about its own indicator**, not a third-party
     comment — a publisher delimiting "what my indicator is not" is more direct than an outside
     rebuttal
- **Evidence**: ev-058
- **Attacked**: see M2, M3

### M2 · This entry judges no CPI figure for any period, and does not say what should measure inflation instead (no attack yet)

- **Claim**: this entry asserts "**the CPI is not the inflation rate**",
  **not** "the CPI's trend is unreliable", **nor** "something else should replace it"
- **Basis**: the same explainer also says that from changes in the CPI one can see the general
  trend of price movements and indicate the degree of inflation (deflation) to some extent (ev-058)
- **Reasoning**:
  1. so this entry **cannot be used to support "the CPI is untrustworthy"** — the explainer itself
     says it has reference value
  2. "so what *should* measure inflation" — **the explainer does not answer, and this repo has
     checked no other source** (the GDP deflator, the PPI, etc. — **not one is registered here**)
  3. this entry also **checks no CPI basket, weights or base period**; those are a further layer of
     basis questions where this repo is currently empty
- **Evidence**: ev-058
- **Attacked**: **the explainer page is dated 2024-09-13, but its URL path reads
  `202409/t20240910_1956353.html`, and the two dates disagree**, so this repo **cannot determine
  which is the real release date**, nor **whether the page has been re-published**.
  This is a direct instance of [Economics](../README.en.md)'s rule "**timeliness is the main point
  of attack**".
  Further: **this repo has registered no actual CPI figure for any period**, and **has not read the
  methodology notes** (the NBS has separate pages on *How the CPI is compiled* and *The basic data
  sources of the CPI*; this repo has read neither).
  The 2022 national CPI of 102.0% used as the page's example **is not stored as knowledge**; it
  appears only to illustrate that page's calculation of the purchasing power index.
- **Attribution**: @hpleapfrog · 2026-10-12
- **To be added**: the two methodology pages; basket weights and base period; any actual release

### M3 · On the "relative number" layer this entry only retells (no attack yet)

- **Claim**: the CPI is a "**relative number**" measuring overall change; it describes **change**,
  not the level of a total
- **Basis**: the explainer's definition paragraph reads exactly so (ev-058)
- **Reasoning**:
  1. whether "relative number" and "rate" are strictly opposed terms in statistics — **this entry
     has not consulted a terminology standard to confirm**
  2. so this entry **cannot support a general claim that "no relative number may be called a rate"**
  3. it supports only **this one sentence**: reading the CPI's "relative number measuring change"
     directly as "the inflation rate", by the explainer's plain words, **does not hold**
- **Evidence**: ev-058
- **Attacked**: **this repo has read neither a national statistical terminology standard nor the
  ILO / IMF standards on price statistics**, so the precise boundary of "relative number" is
  unchecked here. The "relative number ≠ rate" reading above is this repo's own account of the step
  from *magnitude of change* to *measure of a total* — **not the wording of any standard**.
- **Attribution**: @hpleapfrog · 2026-10-12
- **To be added**: the definitions of "relative number", "index" and "rate" in a terminology
  standard

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Every article about inflation gives a CPI figure, but none of them states that the CPI is not
> the inflation rate.**
>
> What you see in the article is **a percentage and a phrase about "inflationary pressure"**;
> what the statistical basis says is **that this figure covers only household consumption, and
> that it is a relative number measuring change**.
>
> **This repo's mission is to remove noise and hold real information.** The substitution is the
> test: **the CPI figure itself need not be repeated here (it is obsolete next period); what it
> can and cannot represent is what belongs here.**
> "How much inflation does this CPI show?" — a question no data page can answer,
> and the explainer states plainly: **the CPI is not the inflation rate.**

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-12 | established the entry; **this subject's first `误解`**, and the second `误解` in the whole repo — the first outside physics and computing | topic chosen against the subject boundary after ev-058 was registered | @hpleapfrog |
