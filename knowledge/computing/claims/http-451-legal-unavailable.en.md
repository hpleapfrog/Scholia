---
id: kb:computing:http-451-legal-unavailable
type: 命题
title: "HTTP 451 denies access because of a legal demand, and implies neither that the resource exists nor that it doesn't"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-20
updated: 2026-10-20
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "what 451 actually means", "whether a server has to name the law", or "whether 451 is evidence that a resource is gone"
  条件: "**applies to RFC 7725 (Standards Track, 2016-02, DOI 10.17487/RFC7725) sections 3-6 as written**; `451` is registered in the IANA registry with RFC 7725 as its specification (**this repo checked the 2025-09-15 revision of that registry**, see ev-057). This entry does **not** claim that any particular country or platform used 451 for any block"
edges:
  先修: []
  支持: ["[claim: the complete list lives in IANA](http-status-code-list-lives-in-iana.en.md#a1)"]
  攻击: []
evidence: [ev-153, ev-054, ev-057]
license: CC-BY-SA-4.0
---

> **English version of [`HTTP451因法律要求拒绝访问且不暗示资源存在与否.md`](HTTP451因法律要求拒绝访问且不暗示资源存在与否.md).**

## 陈述

**451 says exactly one thing: the server is refusing access *as a consequence of a legal demand*. It does not say whether the resource exists, and clients cannot count on seeing it at all — and its definition is not in RFC 9110, it is in RFC 7725.**

| What 451 does assert | What 451 does **not** assert |
|---|---|
| the refusal is the result of a **legal demand** (§3) | that the resource **exists or does not** (§3: neither existence nor nonexistence is implied) |
| the refusing party **may not be the origin server** (§3: ISPs and search engines are affected most directly) | that a client **can certainly get through** (§3 concedes VPN / Tor often still reaches the resource) |
| the response **should** say who demanded it, under which law, and over which people and resources (§3) | that this explanation is **mandatory** (§3 says SHOULD, not MUST) |
| it is **cacheable by default** (§3) | that the blocking party is always identified (§4 is one SHOULD plus one MUST, below) |

> [!NOTE]
> **The table above is this repo's summary, not the structure of RFC 7725** — the document has no
> "asserts / does not assert" columns. Every cell maps to a sentence quoted below;
> **a cell that maps to nothing is invention**, and should be attacked the way `R-GRAPH-02` prescribes.

The rules, each with its own sentence from the source (short quotes):

The reason for the refusal is a legal demand (first sentence of §3):

> This status code indicates that the server is denying access to the
> resource as a consequence of a legal demand.

The refusing server may not be the origin server (§3):

> The server in question might not be an origin server.  This type of
> legal demand typically most directly affects the operations of ISPs
> and search engines.

The body should say who made the demand, under which law, over what (§3):

> Responses using this status code SHOULD include an explanation, in
> the response body, of the details of the legal demand: the party
> making it, the applicable legislation or regulation, and what classes
> of person and resource it applies to.

This is the sentence that separates 451 from "not found" (§3):

> The use of the 451 status code implies neither the existence nor
> nonexistence of the resource named in the request.  That is to say,
> it is possible that if the legal demands were removed, a request for
> the resource still might not succeed.

Default cacheability (end of §3):

> A 451 response is cacheable by default, i.e., unless otherwise
> indicated by the method definition or explicit cache controls; see
> [RFC7234].

Identifying who blocked (§4) — **the only normative MUST in the document**:

> When an entity blocks access to a resource and returns status 451, it
> SHOULD include a "Link" HTTP header field [RFC5988] whose value is a
> URI reference [RFC3986] identifying itself.  When used for this
> purpose, the "Link" header field **MUST** have a "rel" parameter whose
> value is "blocked-by".

The same section says the header points at the entity **implementing** the block, not the one
**ordering** it (§4):

> The intent is that the header be used to identify the entity actually
> implementing blockage, not any other entity mandating it.

Clients cannot rely on 451 appearing at all (§5):

> Clients cannot rely upon the use of the 451 status code.  It is
> possible that certain legal authorities might wish to avoid
> transparency, and not only demand the restriction of access to
> certain resources, but also avoid disclosing that the demand was
> made.

### Why this deserves its own entry instead of a row in [the registry claim](http-status-code-list-lives-in-iana.en.md)

The text that defines `451` exists only in RFC 7725. **Reading RFC 9110 cannot tell you anything
about 451** — the subsection list of its §15.5 ends at `15.5.22. 426 Upgrade Required`
(recomputed by this repo on 2026-10-20, see A2). So "what 451 means" and "whether 451 is a
registered code" are **two questions with two different sources**:

| Question | Where to read | Evidence here |
|---|---|---|
| what 451 **means**, what its response should look like | RFC 7725 §3–§5 | ev-153 |
| whether 451 **is registered**, and under whose specification | the IANA registry (RFC 7725 §6 records that registration) | ev-057 · ev-153 §6 |
| whether RFC 9110 **contains** 451 | RFC 9110 §15.5 subsection list | ev-054 |

## 依据

| ID | Kind | Grade | Locator | License |
|---|---|---|---|---|
| ev-153 | official document | high | IETF / RFC Editor, **RFC 7725** "An HTTP Status Code to Report Legal Obstacles" (T. Bray, Textuality), Standards Track, 2016-02, DOI 10.17487/RFC7725, **§1–§7 read in full** (283 lines / 9,309 bytes, SHA-256 `5817efa6…20b1`) | public official specification · **section numbers and short quotes only, no full-text reuse** |
| ev-054 | official document | high | RFC 9110 (STD 97) §15.5 subsection list, **recomputed 2026-10-20**: `rfc-editor.org/rfc/rfc9110.txt` 10,785 lines, SHA-256 `21c1cdce…232a` — identical to what ev-054 recorded | public official specification · section numbers and short quotes only |
| ev-057 | official document | high | IANA HTTP Status Code Registry, Last Updated **2025-09-15**, the row `451 / Unavailable For Legal Reasons / RFC 7725` | public official registry · entries and short quotes only |

## 论证

### A1 · The semantics come straight out of the specification (no attack yet)

- **Claim**: the four rules of 451 (legal demand · implies neither existence nor nonexistence ·
  SHOULD explain which law · cacheable by default), plus one MUST (`Link` with `rel="blocked-by"`)
- **Premise**: the sentences of ev-153 §3, §4 and §5, quoted one by one above
- **Reasoning**: these are **direct statements of normative text**; this entry only collects them as
  written. The one inference is separating §4's SHOULD from its MUST, which follows two different
  auxiliaries in the source
- **Evidence**: ev-153
- **Attacked by**: no attack yet. **Do not read this entry as advice on how a server should behave** —
  RFC 7725 defines a status code; it is not an implementation recommendation
- **By**: @hpleapfrog · 2026-10-20

### A2 · 451 cannot be read out of RFC 9110 (no attack yet)

- **Claim**: `451` is not among the status codes defined by RFC 9110, so any statement about its
  meaning needs a different source
- **Premise**: (i) ev-054 — RFC 9110's §15.5 subsection list ends at `15.5.22. 426 Upgrade Required`,
  and searching the document text for `451` returns **0 hits** (recomputed 2026-10-20, same line count
  and SHA-256); (ii) ev-153 §6 quotes the IANA update verbatim (`Code: 451 … Specification: RFC 7725`)
- **Reasoning**: if a "complete list" leaves 451 out while 451 is demonstrably registered, then
  **completeness lives outside RFC 9110** — which is exactly what A1 of
  [the registry claim](http-status-code-list-lives-in-iana.en.md) asserts. This entry gives it an
  **independent source** (RFC 7725), rather than RFC 9110 or the registry table alone
- **Evidence**: ev-153 · ev-054 · ev-057
- **Attacked by**: no attack yet. **This entry claims only the textual state of the June-2022 RFC 9110
  and the February-2016 RFC 7725**; if a later revision folds 451 in, A2 needs re-review
- **By**: @hpleapfrog · 2026-10-20

> [!IMPORTANT]
> **A2 is this repo's honest sample of a `支持` edge**: what it supports is not "451 matters", but
> "the complete list is not in one RFC". Under `R-GRAPH-06`, the strength of a support edge depends on
> whether it brings in a **new source** — this one brings ev-153 (RFC 7725), which is
> **not the same material** as that claim's existing ev-054 and ev-057.

## How to attack it

- [ ] Show a document that **supersedes** RFC 7725 (if so, the version qualifier in this entry fails)
- [ ] Show that RFC 9110 defines or normatively references 451 somewhere **outside** the §15.5
  subsection list
- [ ] Show that this entry reads a SHOULD as an obligation (§3's explanation requirement is a SHOULD,
  not a MUST)

## 变更记录

| Date | Action | Basis | By |
|---|---|---|---|
| 2026-10-20 | entry created; ev-153 registered; the rules collected from §3–§6 | ev-153 · ev-054 · ev-057 | @hpleapfrog |
| 2026-10-20 | added a `支持` edge to A1 of [the registry claim](http-status-code-list-lives-in-iana.en.md); recomputed RFC 9110 (line count and hash match ev-054) | A2 | @hpleapfrog |
| 2026-10-20 | **corrected the RFC 7725 title in this entry**: it had first been written from memory ("An HTTP Status Code for Indicating Denials of Access…"), which is **not the real title**; fixed against the ev-153 register row and the downloaded file header to "An HTTP Status Code to Report Legal Obstacles" | ev-153 | @hpleapfrog |
