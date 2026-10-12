---
id: kb:computing:prop-http-status-code-extensibility
type: 命题
title: "An unrecognized HTTP status code is handled as the class's x00, a code outside 100–599 as 5xx, and the reason phrase is only a recommendation"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "how an unrecognized HTTP status code must be handled", or "may a response be judged by its reason phrase"
  条件: **applies only to the preamble of §15 in RFC 9110 (2022-06)**; this entry states the general rules only — **the definitions of the individual codes in §15.2–§15.6 were not checked one by one**
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`未识别的HTTP状态码按该类x00处理.md`](未识别的HTTP状态码按该类x00处理.md).**

## Statement

The preamble to §15 of RFC 9110 sets out the **extensibility rules for status codes**. There are four (short quotes):

| # | Rule | Short quote |
|---|---|---|
| 1 | **The first digit defines the class; the last two digits have no categorising role** | "the **first digit** of the status code defines the class of response. **The last two digits do not have any categorization role.**" |
| 2 | **A client need not know every code, but must know the class**; an unrecognized code is handled as that class's `x00` | "a client is **not required to understand the meaning of all registered status codes** … However, a client **MUST understand the class** of any status code … and **treat an unrecognized status code as being equivalent to the x00 status code of that class**" |
| 3 | **Values outside 100..599 are invalid**; an invalid code is handled as `5xx` | "Values outside the range **100..599 are invalid**" … "A client that receives a response with an **invalid status code SHOULD process the response as if it had a 5xx** (Server Error) status code" |
| 4 | **Reason phrases are recommendations only** and may be replaced or omitted | "The reason phrases listed here are **only recommendations** — they **can be replaced by local equivalents or left out altogether** without affecting the protocol" |

The example the specification gives for rule 2:

> if a client receives an unrecognized status code of **471**, it can see from the first digit that
> there was something wrong with its request and **treat the response as if it had received a 400
> (Bad Request)** status code. (preamble to §15)

The five class definitions themselves (first digit):

| First digit | Class | Definition given |
|---|---|---|
| 1 | Informational | "The request was received, continuing process" |
| 2 | Successful | "The request was successfully received, understood, and accepted" |
| 3 | Redirection | "Further action needs to be taken in order to complete the request" |
| 4 | Client Error | "The request contains bad syntax or cannot be fulfilled" |
| 5 | Server Error | "The server failed to fulfill an apparently valid request" |

> [!IMPORTANT]
> **Taken together, one sentence: the semantics of a status code are set by the number and its first-digit class, not by the string.**
>
> Rule 4 removes reason phrases such as `Not Found` from the protocol —
> **they may be replaced, may be omitted, and do not affect the protocol.**
> So **a check like `if (reason === "Not Found")` has no basis at the protocol level**;
> and rule 2 means that **a client that implements the class fallback can handle a code it has never seen**.
>
> Together these say: **HTTP's status codes are an extensible numeric classification, not a closed table of strings.**

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-054 | **官方文件** | **高** (for a claim of this kind) | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **preamble to §15** (the status-code rules preceding 15.1; this repo verified the source text; §15.2–§15.6 were not checked one by one) | official public specification · **cite section numbers and short quotes only; no full text reproduced** |

## Argument

### A1 · All four rules sit in the preamble; no inference needed (no attack yet)

- **Claim**: an unrecognized code is handled as the class's `x00`, an invalid code as `5xx`, and the reason phrase is only a recommendation
- **Premise**: all four are explicit in the preamble to §15, and rules 2 and 3 are accompanied by an example (471 → 400) and a definition of the invalid range (100..599) (ev-054)
- **Reasoning**:
  1. this is "**what the specification says**" — exactly what the [computing](../README.en.md) subject collects
  2. it is **falsifiable by the reader against the preamble to §15, clause by clause**
  3. **these three rules are what makes extensibility work**:
     without rule 2, every new code would break an old client;
     without rule 3, internal codes in the `600+` range would be misread as a real class.
     The specification supplies **a fallback rule and a catch-all rule together** — this is a paired design
- **Evidence**: ev-054
- **Attacked by**: see A2

### A2 · This entry states the general rules only, and has verified no specific code and no implementation (no attack yet)

- **Claim**: this entry states "**how the general rules read**",
  **not "what a given code means", nor "what a given client actually does"**
- **Premise**: §15.2–§15.6 define the specific codes of 1xx–5xx one by one,
  and **this repo verified the preamble to §15 only** (ev-054)
- **Reasoning**:
  1. "does `418` exist" and "what does `451` mean" — **this repo has not investigated either**
  2. "will some browser or HTTP library actually treat `471` as `400`" —
     **this repo has verified no implementation**
  3. so this entry **cannot support the meaning of any specific code**,
     nor the claim "my client already implements the class fallback"
- **Evidence**: ev-054
- **Attacked by**: **this repo has verified the definition of no individual status code in §15.2–§15.6.**
  "Why may `204` not carry content" and "why is `306` marked Unused" —
  both have answers in the specification, **and this repo has not read a line of them.**
  Also: **this repo has not consulted the IANA HTTP Status Code Registry** referenced in §15.1,
  nor checked the registration procedure in §16.2. The specification says an unrecognized code is handled
  as `x00`, but **which codes are registered and which are not, this repo does not know.**
- **Attribution**: @hpleapfrog · 2026-10-12
- **To be added**: a code-by-code check of §15.2–§15.6; the current contents of the IANA registry

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Every HTTP tutorial appends a table of status codes; none of them writes out "an unrecognized code is handled as the class's x00".**
>
> What you see in a tutorial is **a table listing 200 / 404 / 500**;
> what the specification holds is **that the table is open, how a client must handle codes outside it, and why the string plays no part in the protocol**.
>
> **This repo's mission is to strip noise and hold true information.**
> That contrast is the test: **the meaning of individual codes, this repo need not repeat (it is everywhere, and this entry has not verified them either);**
> **the rules that decide what happens to codes outside the table are what belongs here.**
> "What should I do with a 471" — the question has no answer in any status-code table,
> while the specification made it a checkable rule: **look at the first digit, then treat it as a 400.**

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-12 | Entry created; the subject's third `命题`; the verified range of `ev-054` extended from three sections to four (preamble to §15 added) | ev-054 already registered; §15 extended against the priority named in the subject README's "What is still missing" | @hpleapfrog |
