---
id: kb:life:prop-checked-baggage-travels-with-passenger-and-free-direct-delivery
type: 命题
title: "Checked baggage must travel with the passenger; if delayed for reasons not attributable to the passenger, it may be demanded delivered free of charge"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-13
updated: 2026-10-13
scope:
  学科: 生活 · 城市出行
  学段: 不限
  适用: when checked baggage did not arrive and you want to know the carrier's duty and what you may demand
  条件: "**applies only to the version of the 《公共航空运输旅客服务管理规定》 in force since 2021-09-01**; this entry states Articles 39–41 only, **and has not checked any specific carrier's compensation standards**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-044]
license: CC-BY-SA-4.0
---

> **English version of [`托运行李应与旅客同机运送且非旅客原因延误可要求免费直接送达.md`](托运行李应与旅客同机运送且非旅客原因延误可要求免费直接送达.md).**

## Statement

**Checked baggage must travel on the same aircraft as the passenger; if it cannot, the carrier must prioritise it on a subsequent flight and notify the passenger promptly. Where baggage is delayed for reasons not attributable to the passenger and the passenger asks for direct delivery, the carrier must deliver it free of charge.**

Article 39 of the 《公共航空运输旅客服务管理规定》 states (short quote):

> **承运人应当将旅客的托运行李与旅客同机运送。**
> 除国家另有规定外，不能同机运送的，承运人应当**优先安排该行李在后续的航班上运送**，
> 并**及时通知旅客**。

Article 40 states (short quote):

> 旅客的托运行李延误到达的，承运人应当**及时通知旅客领取**。
> 除国家另有规定外，**由于非旅客原因导致托运行李延误到达，旅客要求直接送达的，
> 承运人应当免费将托运行李直接送达旅客**或者与旅客协商解决方案。

### What "reasons not attributable to the passenger" means

The phrase matches the wording used in [involuntary refunds](involuntary-refund-free.en.md) via Article 63: **"non-carrier reasons" include weather, emergencies, air traffic control, security checks and the passenger's own conduct.** This entry's threshold is lower — **it does not require the carrier to be at fault, only that the passenger did not cause it.**

### The duty to issue documentation

Article 41 accompanies it:

> 在行李运输过程中，托运行李发生**延误、丢失或者损坏**，
> 旅客要求出具**行李运输事故凭证**的，承运人或者其地面服务代理人**应当及时提供**。

### What the carrier must spell out in its Conditions of Carriage

Article 37 lists seven items, and item (7) is the basis for compensation:

| Art. 37 (7) | Content |
|---|---|
| (7) | **The compensation standard for baggage damage, loss and delay, or the applicable national provisions and international conventions** |

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-044 | **Official document provision** | **High** (for this class of claim) | [《公共航空运输旅客服务管理规定》](https://xxgk.mot.gov.cn/2020/jigou/fgs/202103/t20210315_3530413.html), Order of the Ministry of Transport No. 3 of 2021, **Art. 37** (compensation standard in the Conditions of Carriage), **Art. 39** (travelling with the passenger), **Art. 40** (delay notice and free direct delivery), **Art. 41** (incident documentation), **Art. 63** (meaning of terms) | Official public regulation · **cite article numbers and short quotes only; no full text uploaded** |

## Argument

### A1 · "Travels with the passenger" is the regulation's default duty, not a service promise (not yet attacked)

- **Claim**: **checked baggage travelling with the passenger is a duty written in the regulation**; where it cannot, **prioritising the next flight plus prompt notice** are companion duties
- **Premise**: Article 39 (ev-044)
- **Reasoning**:
  1. This is "what an official document specifies" — **the official text is the primary source**
  2. The regulation says "**shall**" — **this is an obligation, not an optional service**
  3. **"except where the state provides otherwise" is an opening, but the regulation does not say what the exception is**
- **Evidence**: ev-044
- **Attacked by**: see A2

### A2 · The threshold for free direct delivery is "not the passenger's fault", not "the carrier's fault" (not yet attacked)

- **Claim**: **the threshold for free direct delivery is lower than for free refunds** — **it does not require the carrier to be at fault, only that the passenger did not cause it**
- **Premise**: Article 40 says "由于**非旅客原因**导致托运行李延误到达" (ev-044)
- **Reasoning**:
  1. Compare with [involuntary refunds](involuntary-refund-free.en.md): free refunds require "**carrier reasons**" (the internal-management causes defined in §63), whereas baggage delivery only requires "**not the passenger's reasons**" — **the two thresholds differ and must not be conflated**
  2. **Weather and air-traffic-control delays also fall inside "not the passenger's reasons"** — **the passenger may still demand free direct delivery**
  3. The regulation offers a second path: **"or negotiate a solution with the passenger"** — **the carrier may choose to negotiate, but may neither refuse delivery nor negotiate**
- **Evidence**: ev-044
- **Attacked by**: **This entry states Articles 37, 39, 40, 41 and 63 of the version in force since 2021-09-01 only; it does not guarantee the rule still stands.** The Ministry page **carries no version number** — **this repo has no mechanism to detect whether it has been amended**. Also: **this entry has not checked any specific carrier's compensation standards** — **"how much" is delegated to the Conditions of Carriage by Art. 37 (7)**, and **this repo has not read any carrier's Conditions of Carriage**. Also: **this entry has not checked whether China is a party to the Montreal Convention or what its baggage liability limit is.**
- **Author**: @hpleapfrog · 2026-10-13
- **To be added**: **a version-detection mechanism**; at least one carrier's baggage compensation standard in its Conditions of Carriage; the Montreal Convention's status in China and its baggage liability limit

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Article 28 of the regulation requires airports to post signage at every key point of the boarding flow — so rules like "check-in → security → boarding" are guaranteed to be visible on site.**
>
> **"Your checked baggage was supposed to fly with you" and "if it is late you may demand it delivered to your door free of charge, and you do not need the airline to be at fault" appear on no sign.** They even cut against the default script at the counter: when baggage goes missing a passenger is usually steered toward filing a "tracing form" and waiting, **while the regulation gives "free direct delivery" as an option you can demand.**
>
> **This library's mission is to remove noise and store real information.**
> What is visible on site, this repo need not repeat; **what is invisible on site and hands the passenger an option to claim is exactly what this repo should hold.**
> This entry is the latter — **the one most easily treated as "nothing but wait" when baggage is delayed, when the regulation says "you may demand free direct delivery".**

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-13 | Entry created; ev-044's verification depth upgraded from "located only" to "full text" (this rule was newly extracted after this repo checked all ten chapters article by article) | ev-044 registered; topic selected by discipline boundary | @hpleapfrog |
