---
id: kb:life:prop-carriage-conditions-no-retroactive-restriction
type: 命题
title: "After a carrier amends its Conditions of Carriage, the new restrictive terms may not be applied to tickets bought before the amendment"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-13
updated: 2026-10-13
scope:
  学科: 生活 · 城市出行
  学段: 不限
  适用: when an airline has changed its refund/change rules or baggage rules and you hold a ticket bought before the change
  条件: "**applies only to the version of the 《公共航空运输旅客服务管理规定》 in force since 2021-09-01**; this entry states Article 7 of that regulation only, **and has not checked any specific carrier's Conditions of Carriage**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-044]
license: CC-BY-SA-4.0
---

> **English version of [`修改运输总条件不得追溯适用于已购票旅客.md`](修改运输总条件不得追溯适用于已购票旅客.md).**

## Statement

**After a carrier amends its Conditions of Carriage, content that restricts passenger rights or adds passenger obligations may not be applied to passengers who bought their tickets before the amendment.**

Article 7 of the 《公共航空运输旅客服务管理规定》 states (short quote):

> 承运人修改运输总条件的，应当标明生效日期。
> **修改后的运输总条件不得将限制旅客权利或者增加旅客义务的修改内容适用于修改前已购票的旅客**，
> 但是国家另有规定的除外。

### The rule has two preconditions

| Article | Provision |
|---|---|
| **§7 para. 1** | A carrier amending its Conditions of Carriage **shall state the effective date** |
| **§7 para. 2** | Content that **restricts passenger rights or adds passenger obligations** may **not** be applied to passengers who **bought before the amendment**; **except where the state provides otherwise** |

### What counts as "restricting passenger rights or adding passenger obligations"

The regulation does not define the phrase, but **Article 8 lists the five items the Conditions of Carriage must contain at minimum**, and these are exactly what gets amended:

| Art. 8 | Content |
|---|---|
| (1) | **Detailed rules for ticket sales, refunds and changes** |
| (2) | Boarding rules, including carriage standards for infants, pregnant passengers, unaccompanied minors and seriously ill passengers |
| (3) | **Specific requirements for baggage transport** |
| (4) | **Oversales handling rules** |
| (5) | The email address and telephone number for complaints |

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-044 | **Official document provision** | **High** (for this class of claim) | [《公共航空运输旅客服务管理规定》](https://xxgk.mot.gov.cn/2020/jigou/fgs/202103/t20210315_3530413.html), Order of the Ministry of Transport No. 3 of 2021, **Art. 7** (the retroactivity ban and the effective-date duty) and **Art. 8** (the five mandatory contents of the Conditions of Carriage) | Official public regulation · **cite article numbers and short quotes only; no full text uploaded** |

## Argument

### A1 · This is a prohibition written in the regulation, not an industry convention (not yet attacked)

- **Claim**: **"new rules do not apply to old tickets" is written in the regulation**, and the regulation **also requires the carrier to state the effective date**
- **Premise**: the text of both paragraphs of Article 7 (ev-044)
- **Reasoning**:
  1. This is "what an official document specifies" — **the official text is the primary source**
  2. "**may not** be applied to" is **prohibitory**, not hortatory
  3. **Paragraph 1's "shall state the effective date" is what makes paragraph 2 enforceable** — without a date you cannot tell whether a given ticket was bought before or after the amendment
  4. Same shape as [involuntary refunds being free of charge](involuntary-refund-free.en.md): **a hard obligation the regulation places on carriers, and a right most passengers do not know they have**
- **Evidence**: ev-044
- **Attacked by**: see A2

### A2 · "Restricting passenger rights" is undefined, and this entry cannot substitute for the carrier's terms (not yet attacked)

- **Claim**: this entry states that **the regulation sets a prohibition line**; **it does not judge whether a particular amendment crosses it**
- **Premise**: Article 7 uses "restricting passenger rights or adding passenger obligations", and **the regulation never defines the phrase** (ev-044)
- **Reasoning**:
  1. So "does a refund-fee increase count as restricting rights" **is not answerable here** — **that requires the carrier's Conditions of Carriage and the specific circumstances**
  2. Article 8 **delegates** the refund/change details to the carrier ("承运人应当根据本规定制定并公布运输总条件" §6), while Article 7 **limits** how those terms may be applied retroactively — **which layer a passenger actually receives, this repo has no data on**
  3. **"except where the state provides otherwise" is an opening** — the regulation admits an exception exists but **does not list what it is**
- **Evidence**: ev-044
- **Attacked by**: **This entry states Article 7 of the version in force since 2021-09-01 only; it does not guarantee the rule still stands.** The Ministry page **carries no version number**, only a document number and an effective date — **this repo has no mechanism to detect whether it has been amended**. Also: **this entry has not checked any carrier's Conditions of Carriage**, so **it cannot claim "a carrier's amendment is unlawful"** — that requires a clause-by-clause comparison against the carrier's own text.
- **Author**: @hpleapfrog · 2026-10-13
- **To be added**: **a version-detection mechanism** (this repo has the `已失效` status but no trigger for it); at least one carrier's amendment record, to demonstrate how this prohibition line is invoked

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Article 28 of the regulation requires airports to post signage at every key point of the boarding flow — so rules like "check-in → security → boarding" are guaranteed to be visible on site.**
>
> **The rule "if the airline changed its rules, your old ticket is still governed by the old ones" appears on no sign.** It runs the other way: **when an airline changes its terms it announces the new ones, and does not volunteer that old tickets keep the old terms.**
>
> **This library's mission is to remove noise and store real information.**
> What is visible on site, this repo need not repeat; **what is invisible on site and runs against your interest is exactly what this repo should hold.**
> This entry is the latter — **the one sentence a passenger most needs when an airline changes its rules, and the hardest to look up alone.**

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-13 | Entry created; ev-044's verification depth upgraded from "located only" to "full text" (this rule was newly extracted after this repo checked all ten chapters article by article) | ev-044 registered; topic selected by discipline boundary | @hpleapfrog |
