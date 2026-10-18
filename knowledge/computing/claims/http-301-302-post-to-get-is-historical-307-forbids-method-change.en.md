---
id: kb:computing:prop-http-301-302-post-to-get-is-historical-307-forbids-method-change
type: 命题
title: "HTTP 301/302 changing POST to GET is a MAY 'for historical reasons'; to preserve the method use 307/308"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-13
updated: 2026-10-13
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "does 301/302 turn POST into GET", or "which code to use to preserve the request method"
  条件: "**applies to RFC 9110 (STD 97, 2022-06) §15.4.2, §15.4.3, §15.4.4, §15.4.8, §15.4.9**; this entry states those five sections' text only, **and has not checked [CACHING] §4.2.2's list of cacheable status codes**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`HTTP301与302把POST改成GET是历史原因下的MAY且保留方法应用307与308.md`](HTTP301与302把POST改成GET是历史原因下的MAY且保留方法应用307与308.md).**

## Statement

**301 and 302 changing POST to GET is a MAY "for historical reasons", not the specification's obligation; to preserve the request method the specification points to 307 and 308.**

RFC 9110 §15.4.2 (`301`) note (short quote):

> **Note:** **For historical reasons**, a user agent **MAY** change the request method
> from POST to GET for the subsequent request. If this behavior is undesired, the
> **308 (Permanent Redirect)** status code can be used instead.

§15.4.3 (`302`) note (short quote):

> **Note:** **For historical reasons**, a user agent **MAY** change the request method
> from POST to GET for the subsequent request. If this behavior is undesired, the
> **307 (Temporary Redirect)** status code can be used instead.

### 307 explicitly forbids changing the method

§15.4.8 states (short quote):

> The 307 (Temporary Redirect) status code indicates that the target resource resides
> temporarily under a different URI and the user agent **MUST NOT change the request method**
> if it performs an automatic redirection to that URI.

### 303 is designed to switch to a GET/HEAD

§15.4.4 states (short quote):

> A user agent can perform a **retrieval request** targeting that URI
> (**a GET or HEAD request** if using HTTP), which might also be redirected, and present
> the eventual result as an answer to the original request. Note that the new URI in
> the Location header field is **not considered equivalent** to the target URI.

### The specification pairs them: 301↔308, 302↔307

The substitutions the two notes offer are **paired**: **do not want 301 to turn POST into GET → use 308; do not want 302 to turn POST into GET → use 307.**

### One asymmetry: 308's body lacks the MUST NOT sentence

**§15.4.8 (307) says "MUST NOT change the request method"; §15.4.9 (308)'s body has no corresponding sentence** — 308 covers only the permanent-URI semantics, `Location` and cacheability. **But §15.4.2 (301)'s note designates 308 as "the alternative when you do not want the method changed"**, so 308's intent is clear even though the body does not repeat it.

### The caching sentences are also asymmetric

**§15.4.2 (301) and §15.4.9 (308) state "heuristically cacheable"; §15.4.3 (302), §15.4.4 (303) and §15.4.8 (307) have no corresponding sentence.**
(This entry **does not claim** 302/303/307 are not cacheable — [CACHING] §4.2.2 is unchecked.)

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-054 | **Official document** | **High** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **§15.4.2** (301 with the historical-reasons note and cacheability), **§15.4.3** (302 with the historical-reasons note), **§15.4.4** (303's retrieval request), **§15.4.8** (307's MUST NOT change the method), **§15.4.9** (308 with cacheability) | Official public specification · **cites section numbers and short quotations only; does not reproduce the full text** |

## Argument

### A1 · "301/302 necessarily turn POST into GET" is inaccurate at the specification level (not yet attacked)

- **Claim**: **301/302 changing the method is a MAY, and the specification itself labels it "for historical reasons"**; **to guarantee the method is preserved, use 307/308**
- **Premise**: both notes in §15.4.2 and §15.4.3 open with "**For historical reasons**" and use "**MAY** change" and "**If this behavior is undesired** … can be used instead" (ev-054)
- **Reasoning**:
  1. This is "what a standard or official document specifies" — exactly what the [computing](../README.en.md) discipline collects
  2. **The retelling "301/302 turn POST into GET" turns a MAY into a certainty** — the specification says it is **permitted**, and permitted **because of historical baggage**
  3. The stronger criterion: **the specification names the alternatives outright** — **if you do not want the method changed, use 307 (temporary) or 308 (permanent)**
  4. Same shape as [503's `Retry-After` being a MAY](http-503-retry-after-is-may-not-must.en.md): **the specification uses MAY to mean "permitted", and retellings turn it into an obligation or a certainty**
- **Evidence**: ev-054
- **Attacked by**: see A2

### A2 · The 303 / 307 / 308 division is not "temporary versus permanent" (not yet attacked)

- **Claim**: **the 303 versus 307/308 division is about "whether a separately identifiable, bookmarkable, cacheable resource is used to answer"**, not "temporary versus permanent"
- **Premise**: §15.4.4 states that 303 exists so the output of a POST becomes a resource that can be **separately identified, bookmarked, and cached**, and that the Location URI is **not considered equivalent** to the target URI (ev-054)
- **Reasoning**:
  1. **A 303's Location does not point at "the same resource at a new address" but at "a different resource used to answer"** — unlike 301/302/307/308's "the resource moved" semantics
  2. So "**303 = a temporary redirect**" is a misreading: 303 makes no promise of "same resource, temporarily elsewhere"
  3. The specification's wording for 303 is "can perform a **retrieval request**" — **it asks for a different GET/HEAD, not a replay of the original request**
- **Evidence**: ev-054
- **Attacked by**: **This entry states the text of RFC 9110 §15.4.2–§15.4.9 only; it does not guarantee the behaviour of any specific client or server.** "The 301/302 MAY" is the specification's wording, not a measured fact. Also: **this entry has not checked [CACHING] §4.2.2's list of cacheable status codes**, so **it does not claim whether 302/303/307 are cacheable**; **§15.4.9 (308)'s body genuinely lacks the "MUST NOT change the request method" sentence**, and this entry records that asymmetry **without completing it for the specification**. Also: **this entry has not checked how older RFCs (7230–7235) worded 301/302**, nor **what "historical reasons" specifically refers to**.
- **Author**: @hpleapfrog · 2026-10-13
- **To be added**: [CACHING] §4.2.2's list of cacheable status codes; RFC 7230–7235's wording of 301/302/303; the specific referent of "historical reasons"

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Any HTTP tutorial tells you "301/302 turn POST into GET, 307/308 preserve the method"; none tells you the specification writes 301/302's method change as a MAY labelled "for historical reasons", and none tells you 307 uses MUST NOT while 308's body lacks that sentence.**
>
> The latter three are each a piece of the specification's wording, and almost never survive retelling:
> **"MAY + historical reasons" shows 301/302's method change is baggage rather than design;
> "307 is MUST NOT, 308's body has no such sentence" is an asymmetry in the specification's own text;
> "303 points at a different resource" dismantles "303 = a temporary redirect".**
>
> **This library's mission is to remove noise and store real information.**
> "301/302 become GET, 307/308 preserve" is noise — tutorials all cover it.
> "The method change is a MAY for historical reasons; 307 is MUST NOT; 308's body lacks the sentence; 303 points at another resource" — these sit inside the notes and the MUST NOT of RFC 9110 §15.4.2–§15.4.9, **and are what this library should hold**.

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-13 | Entry created; an instance filling the "remaining individual codes of RFC 9110 §15.2–§15.6" gap in "What is still missing" (five codes, 301/302/303/307/308, in one entry) | ev-054 registered; topic selected by discipline boundary | @hpleapfrog |
