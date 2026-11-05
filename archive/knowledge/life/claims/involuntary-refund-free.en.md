---
id: kb:life:prop-involuntary-refund-free
type: 命题
title: "Involuntary refunds and carrier-caused involuntary changes must not be charged to the passenger"
status: 待审
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 生活 · 城市出行
  学段: 不限
  适用: when a flight is cancelled, delayed or rescheduled and you want a refund or a change
  条件: "**applies only to the version of 《公共航空运输旅客服务管理规定》 effective 2021-09-01**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-044]
license: CC-BY-SA-4.0
---

> **English version of [`非自愿退票与变更不得收费.md`](非自愿退票与变更不得收费.md).**

## Statement

《公共航空运输旅客服务管理规定》 provides:

| Case | Provision |
|---|---|
| **involuntary refund** | **no refund fee** (Article 25) |
| **involuntary change caused by the carrier** | **no ticket-change fee** (Article 24, para 1) |
| **refund arrival** | completed within **7 working days** of receiving a valid refund application (Article 26, **excluding** financial-institution processing time) |

Original text (short quotations):

> For an involuntary refund, the carrier or its air-sales agent shall not charge a refund fee. (§25)
>
> Where an involuntary change of ticket is caused by the carrier, … **no ticket-change fee shall be charged to the passenger.** (§24)
>
> … the refund procedure shall be completed within **7 working days** from receipt of the passenger's valid refund application. (§26)

> [!IMPORTANT]
> **"Involuntary" and "caused by the carrier" are the key to this entry, and both have statutory definitions.**
>
> Article 63 (definitions) states:
>
> | Term | Statutory meaning |
> |---|---|
> | **involuntary refund** | a refund caused by **flight cancellation, delay, advancement, itinerary change, class change, or the carrier's inability to operate the original flight** |
> | **carrier cause** | the carrier's **internal-management** causes, including **maintenance, flight scheduling, crew scheduling** |
> | **non-carrier cause** | other causes unrelated to the carrier's internal management, including **weather, emergencies, air-traffic control, security, passengers** |
>
> **A weather delay is not "carrier cause"** — a point passengers often misuse,
> and often **mistakenly believe all delays qualify for free refund/change**.

## Basis

| Number | Type | Grade | Locator | License |
|---|---|---|---|---|
| ev-044 | **official document clause** | **high** (for this kind of claim) | [《公共航空运输旅客服务管理规定》](https://xxgk.mot.gov.cn/2020/jigou/fgs/202103/t20210315_3530413.html), Transport Ministry Order 2021 No. 3, §24 / §25 / §26 / §63 | official public regulation · **clauses quoted only** |

## Argument

### A1 · The regulation's original text directly gives the fee rules (no attack yet)

- **Claim**: these three are not industry practice but **explicit regulation**
- **Premise**: Articles 24, 25 and 26 respectively state "no ticket-change fee", "no refund fee", "completed within 7 working days" (ev-044)
- **Reasoning**:
  1. This belongs to "**what the official document stipulates**", for which **the official original is the primary source**
  2. It is **falsifiable by the reader clause by clause** — open the page and search the article number
- **Evidence**: ev-044
- **Attacked**: see A2
- **Attribution**: @hpleapfrog · 2026-10-05

### A2 · This entry declares only one version (no attack yet)

- **Claim**: this entry declares "**the version effective 2021-09-01 was so**", **not that it still is**
- **Premise**: the Transport Ministry page has **no version number**, only the document number and effective date (ev-044)
- **Reasoning**:
  1. This regulation **itself repealed three old rules** — showing **such documents are indeed replaced wholesale**
  2. And the repo has **no mechanism** to detect whether it was revised
  3. Writing "it is still so now" into the statement is **going beyond the evidence**
- **Evidence**: ev-044
- **Attacked**: **this entry may conflict with airlines' General Conditions** —
  Article 8 leaves refund/change details to the airlines, while Article 7 forbids airlines from
  applying rights-restricting changes to passengers who bought before the change.
  **Which layer a passenger actually meets, the repo has no data on.**
- **Attribution**: @hpleapfrog · 2026-10-05
- **To be added**: a **version-detection mechanism**. The repo has a `已失效` status, **but nothing that can trigger it**.

## Why this is "real information", not "noise"

> [!IMPORTANT]
> **Article 28 requires airports to put signage guidance at all key areas of the boarding process.**
>
> > Airport management bodies shall set up signage guidance at key areas of the passenger's boarding process, such as check-in, baggage check-in, security, customs, border control, boarding gate and transfer corridor (§28)
>
> **In other words: "check-in → security → boarding" — the law guarantees this is visible on-site.**
>
> **The three things this entry writes — free involuntary refund, free carrier-caused change, 7-working-day refund —
> appear on no sign.**
>
> **The repo's mission is "remove noise, hold real information".**
> This contrast is the criterion: **what is visible on-site, the repo need not repeat; what the law writes but is invisible on-site is what the repo should hold.**

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (user asked "add how to fly too") | user question | @hpleapfrog |
