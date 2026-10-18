---
id: kb:life:prop-carried-item-limits
type: 命题
title: "Beijing subway sets hard size and weight limits on items passengers carry"
status: 待审
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 生活 · 城市出行
  学段: 不限
  适用: judging whether an item can be brought before riding the Beijing subway
  条件: "**applies only to the version of 《北京市轨道交通乘客守则》 effective 2021-09-28**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-043]
license: CC-BY-SA-4.0
---

> **English version of [`携带物品的尺寸与重量上限.md`](携带物品的尺寸与重量上限.md).**

## Statement

《北京市轨道交通乘客守则》 (effective 2021-09-28) provides for items carried by passengers:

| Item | Limit |
|---|---|
| **Weight** | **no more than 30 kg** |
| **Length** | **no more than 1.8 m** |
| **Width and height** | **each no more than 0.5 m** |
| **Electric mobility devices** | **not allowed**; except **electric wheelchairs for accessibility** |

Original text (short quotation):

> Items carried by passengers shall not weigh more than 30 kg, be more than 1.8 m long, or more than 0.5 m wide or high.
> Electric mobility devices and other items that obstruct movement within stations or cars, or may affect operational safety, shall not be carried —
> except electric wheelchairs for accessibility.

> [!IMPORTANT]
> **These four numbers are the only criterion for "can I bring it" questions.**
>
> Online, claims about "whether the subway allows X" are abundant and contradict each other.
> **The official rules give numbers to check against directly** — that is why this entry is listed on its own.

## Basis

| Number | Type | Grade | Locator | License |
|---|---|---|---|---|
| ev-043 | **official document clause** | **high** (for this kind of claim) | [《北京市轨道交通乘客守则》](https://www.bjsubway.com/support/ccgd/), effective 2021-09-28 | official public document · **clauses quoted only** |

**Also on the page: 10 fare-rule documents** — **fares, discounts, card refunds are outside this entry's scope.**

## Argument

### A1 · The official original is the primary source for this kind of claim (no attack yet)

- **Claim**: for a claim of the form "what the official document stipulates", **the officially published original is the primary source**,
  and it does not queue on the empirical evidence ladder
- **Premise**: the rules are published on the **Beijing Subway official site**'s "riding rules" page, with the **effective date** noted (ev-043)
- **Reasoning**:
  1. This differs from **online rumors** about "whether some subway allows some item" —
     this entry's claim is "**what the document says**", and **the document can be opened and checked word by word**
  2. so this entry's **verifiability is the strongest tier**: the reader opens the link and can falsify it
- **Evidence**: ev-043
- **Attacked**: see the next entry (timeliness)
- **Attribution**: @hpleapfrog · 2026-10-05

### A2 · This entry declares only one version (no attack yet)

- **Claim**: this entry declares "**the version effective 2021-09-28 was so**",
  **not "it is still so now"**
- **Premise**: the rules have **no revision number**, and the page only gives the effective date (ev-043)
- **Reasoning**:
  1. the repo **cannot verify whether the page has been replaced by a newer version** —
     the URL is unchanged, the page carries no version marker, and **the repo does not periodically check**
  2. so "whether it is still so now" is **not determinable** in the repo;
     writing it as an unconditional fact is **going beyond the evidence** (the same class of error as the `ev-002` lesson)
- **Evidence**: ev-043
- **Attacked**: this entry's self-limitation may be excessive — if the repo did read the current version when collected,
  is saying "does not declare whether current" over-conservative?
- **Response**: **it is not conservatism, it is accuracy.** The repo has **no** mechanism to detect version change;
  and **normative facts are exactly the kind that changes most**. **The declared range is set by capability, not by wish.**
- **Attribution**: @hpleapfrog · 2026-10-05
- **To be added**: a **version-detection mechanism** (e.g. record the page content's hash and alarm on change) —
  the repo currently has **no such mechanism**; see the next section

## What "the repo has no version-detection mechanism" means

> [!WARNING]
> **This proposition will go false over time, and the repo will not know.**
>
> | The repo has | The repo lacks |
> |---|---|
| the `已失效` **status value** (defined in `FORMAT.md` §4) | **anything that can trigger that status** |
| the `updated` field | **a check that looks at whether the source document changed** |
>
> **`已失效` has never been used to date.** It waits for a **person** to notice some evidence has gone stale.
>
> **This is exactly the wall that "taking the subway" content ran into:**
> academic knowledge (physics laws) **does not expire**, so the repo never needed this mechanism;
> **rule-type facts do expire**, and the mechanism **does not exist**.

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry; **the repo's first "normative" proposition**, and the first proposition **known to expire** | user asked "what about the knowledge of taking the subway?" | @hpleapfrog |
