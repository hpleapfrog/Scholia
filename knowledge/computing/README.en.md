# Computing

> [!IMPORTANT]
> **This subject holds "what the standards and official documentation stipulate", not "how to do it step by step".**
>
> Tutorials, install commands and troubleshooting flows are everywhere; repeating them is only
> noise — **the scarcity criterion**. But **the meaning of a protocol field, the default behaviour
> of an API, the conditions under which a compatibility rule applies** can only be taken from the
> standard or official documentation itself; a retelling is often already stale or distorted.

> **English version of [`README.md`](README.md).**

## Current state

| Entry | Type | Status | Source |
|---|---|---|---|
| [RFC 2119, Key words for use in RFCs to Indicate Requirement Levels (IETF, BCP 14)](resources/rfc2119.en.md) | 资源 | 有效 | `ev-052` |
| [RFC 9110, HTTP Semantics (IETF, STD 97)](resources/rfc9110.en.md) | 资源 | 有效 | `ev-054` |
| [In an RFC, MUST / SHOULD / MAY carry normative meaning only when written in all capitals](claims/rfc-keywords-require-uppercase.en.md) | 命题 | 暂定确认 | `ev-052` `ev-053` |
| [An HTTP method's safety and idempotency are set by the specification, and 'safe' does not mean 'free of side effects'](claims/http-method-safety-idempotency.en.md) | 命题 | 暂定确认 | `ev-054` |
| [An unrecognized HTTP status code is handled as the class's x00, a code outside 100–599 as 5xx, and the reason phrase is only a recommendation](claims/http-status-code-extensibility.en.md) | 命题 | 暂定确认 | `ev-054` |
| [The complete list of HTTP status codes lives in the IANA registry, not in RFC 9110](claims/http-status-code-list-lives-in-iana.en.md) | 命题 | 暂定确认 | `ev-054` `ev-057` |
| [Adding an HTTP status code requires IETF Review, and the specification forbids new codes from disallowing content](claims/http-status-code-registration-requires-ietf-review.en.md) | 命题 | 暂定确认 | `ev-054` |
| [An HTTP 204 response may contain neither content nor trailers, and is heuristically cacheable by default](claims/http-204-cannot-contain-content-or-trailers.en.md) | 命题 | 暂定确认 | `ev-054` |
| [An HTTP 405 response MUST carry an Allow header, and is heuristically cacheable by default](claims/http-405-must-include-allow-header.en.md) | 命题 | 暂定确认 | `ev-054` |
| [HTTP 410 means 'likely permanent'; if permanence is unknown, 404 ought to be used instead](claims/http-410-vs-404-permanence.en.md) | 命题 | 暂定确认 | `ev-054` |
| [An HTTP 304 response MUST carry the cache headers a 200 would have sent, and may contain neither content nor trailers](claims/http-304-must-carry-cache-headers-and-no-body.en.md) | 命题 | 暂定确认 | `ev-054` |
| [An HTTP 401 response MUST carry a WWW-Authenticate header, and the 401 / 403 division is not 'logged out vs no permission'](claims/http-401-vs-403-must-carry-www-authenticate.en.md) | 命题 | 暂定确认 | `ev-054` |
| [An HTTP 503's Retry-After is a MAY, not a MUST, and the specification does not require 503 when a server is overloaded](claims/http-503-retry-after-is-may-not-must.en.md) | 命题 | 暂定确认 | `ev-054` |
| [HTTP 301/302 changing POST to GET is a MAY 'for historical reasons'; to preserve the method use 307/308](claims/http-301-302-post-to-get-is-historical-307-forbids-method-change.en.md) | 命题 | 暂定确认 | `ev-054` |
| [An HTTP 400 is a client error at the syntax or routing level; 422 is correct syntax that cannot be processed semantically](claims/http-400-vs-422-syntax-vs-semantics.en.md) | 命题 | 暂定确认 | `ev-054` |
| [An HTTP 414 response means the target URI is longer than the server is willing to interpret, and is heuristically cacheable by default](claims/http-414-uri-too-long.en.md) | 命题 | 暂定确认 | `ev-054` |
| [An HTTP 421 means the request was misdirected; the client MAY retry on another connection, and a proxy MUST NOT generate it](claims/http-421-misdirected-request-retry.en.md) | 命题 | 暂定确认 | `ev-054` |
| [An HTTP 501 response means the server does not support the required functionality, and is heuristically cacheable by default](claims/http-501-not-implemented.en.md) | 命题 | 暂定确认 | `ev-054` |
| [IETF Review requires an RFC in the IETF Stream approved by the IESG as having IETF consensus — Standards Track is not required](claims/ietf-review-ietf-stream-rfc.en.md) | 命题 | 暂定确认 | `ev-089` |
| [Treating 418 as a normative HTTP status code](misconceptions/http-418-is-real.en.md) | 误解 | 有效 | `ev-054` `ev-057` |

**All twenty come from IETF's public RFCs and IANA's public registry** (`ev-052` / `ev-053` / `ev-054` / `ev-057` / `ev-089`; verification depth is stated per entry).
That means this subject's current coverage is **not** the same as the subject "Computing" itself —
see "What is still missing" below.

### What is still missing

| Gap | Why it matters | Source needed |
|---|---|---|
| **The remaining individual codes of RFC 9110 §15.2–§15.6** | `204`, `301`–`304`, `307`–`308`, `400`, `401`, `403`, `405`, `410`, `413`–`422`, `426` and `500`–`505` are now verified (`ev-054`), and so is the registry (`ev-057`), but **the definitions of the remaining codes are still unchecked**: `402`, `404`, `406`–`409`, `411`–`412`, the rest of 1xx and 2xx (`200`–`203`, `205`, `206`), and `300`, `305`, `306` — this repo has only read second-hand | RFC 9110 §15.2–§15.6 (already inside `ev-054`, just unchecked) |
| **Language and platform documentation** | all twenty entries are network protocols; "the default behaviour of a given API" and "the conditions under which a compatibility rule applies" are entirely absent | official Python / Java documentation, with version number and release date |
| **Format and encoding specifications** | the **constraints and defaults** of things like `JSON` / `UTF-8` / `HTML` are where retellings go wrong most often | RFC 8259 · the Unicode Standard · WHATWG standards |
| **Version-difference entries** | "what changed for X between v1 and v2" is this subject's most typical checkable content, and the count is currently zero | the version-history pages of each specification |

**The next entry here should turn to "format and encoding specifications"** — the main protocol-side gaps (status codes, the registration procedure) are now filled,
but not a single entry covers the constraints and defaults of a format such as `RFC 8259` (JSON); **new evidence is needed**.
The remaining scattered status codes on the protocol side (`402`, `404`, `406`–`409`, `411`–`412`, etc., see the table above) can be swept up at any time.

## Boundary

| | Holds | Does not hold |
|---|---|---|
| content | definitions, defaults, constraints and version differences **locatable** in protocol/format specs and in language or platform documentation | tutorials, command sequences, configuration steps, best-practice checklists |
| source | **formal documents** from standards bodies or vendors, with an identifier / version / release date | blogs, Q&A, second-hand summaries |
| phrasing | "document N stipulates X (identifier · version · to be verified)" | "the recommended approach is X" |

**Only publicly readable documents are held.** A spec reachable only behind a paid subscription
cannot be verified here and is not registered as evidence.

### Where the line falls with neighbouring subjects

| Subject | What it answers |
|---|---|
| **Computing** | what a specification **stipulates**: fields, defaults, constraints, compatibility |
| [Science](../science/README.en.md) | errata in textbooks and publications: what is printed wrongly |

The same two criteria apply — **scarcity** and **risk**: procedures that can hurt are not held
(see [decision record: the boundary of procedural knowledge](../../docs/decisions/procedural-knowledge-boundary.en.md)),
tutorials are not repeated. **This repo does not teach how to write code; it records what the specification says.**

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-18 | added the claim "IETF Review requires an RFC in the IETF Stream approved by the IESG as having IETF consensus, and Standards Track is not required", verifying RFC 8126 §4.8 (with §4.7 / §4.9 / §4.11 for contrast); `ev-089` registered; the §4.8 row in "What is still missing" filled in, and the "next entry" paragraph turned to format and encoding specifications | topic chosen against the subject boundary after ev-089 (RFC 8126) was registered | @hpleapfrog |
| 2026-10-18 | added three claims: 414 (its three typical causes and cacheability), 421 (the client MAY retry on another connection; a proxy MUST NOT generate it), 501 (its division from 503 / 405 and cacheability), verifying §15.5.14–§15.5.22 and §15.6.1–§15.6.6 in full; the first "What is still missing" row and the "next entry" paragraph rewritten around RFC 8126 §4.8 | ev-054 already registered; extended against the priority named in "What is still missing" | @hpleapfrog |
| 2026-10-13 | added the claim "an HTTP 400 is a client error at the syntax or routing level …", verifying §15.5.1 and §15.5.21 (400 / 415 / 422, three codes in one entry); the already-verified individual codes in "What is still missing" updated to 204/300–308/400/401/403/405/410/415/422/503 | topic chosen against the subject boundary after ev-054 was registered | @hpleapfrog |
| 2026-10-13 | completed the latter half of §15.5.19 in the 418 misconception entry (re-assignable when 4NN is exhausted); the 418-context row removed from "What is still missing" | ev-054 already registered; §15.5.19 re-read in full | @hpleapfrog |
| 2026-10-13 | added the claim "HTTP 301/302 changing POST to GET is a MAY …", verifying §15.4.2/§15.4.3/§15.4.4/§15.4.8/§15.4.9; the already-verified individual codes in "What is still missing" updated to 204/301–308/401/403/405/410/503 | topic chosen against the subject boundary after ev-054 was registered | @hpleapfrog |
| 2026-10-13 | added the claim "an HTTP 503's Retry-After is a MAY …", verifying §15.6.4 and §15.6.2; the already-verified individual codes in "What is still missing" updated to 204/304/401/403/405/410/503 | topic chosen against the subject boundary after ev-054 was registered | @hpleapfrog |
| 2026-10-13 | added the claim "an HTTP 401 response MUST carry a WWW-Authenticate header …", verifying §15.5.2 and §15.5.4; the already-verified individual codes in "What is still missing" updated to 204/304/401/403/405/410 | topic chosen against the subject boundary after ev-054 was registered | @hpleapfrog |
| 2026-10-13 | added the claims "HTTP 410 means 'likely permanent' …" and "an HTTP 304 response MUST carry the cache headers …", verifying §15.5.11 and §15.4.5; the already-verified individual codes in "What is still missing" updated to 204/304/405/410 | topic chosen against the subject boundary after ev-054 was registered | @hpleapfrog |
| 2026-10-12 | added the claims "an HTTP 204 response may contain neither content nor trailers …" and "an HTTP 405 response MUST carry an Allow header …", verifying §15.3.5 and §15.5.6; the individual-codes row in "What is still missing" rewritten to "the remaining individual codes" | topic chosen against the subject boundary after ev-054 was registered | @hpleapfrog |
| 2026-10-12 | added the claim "adding an HTTP status code requires IETF Review…", verifying RFC 9110 §16.2; the §16.2 row in "What is still missing" filled in and replaced by RFC 8126 §4.8 | topic chosen against the subject boundary after ev-054 was registered | @hpleapfrog |
| 2026-10-12 | added the claim "the complete list of HTTP status codes lives in the IANA registry…" and the misconception "treating 418 as a normative HTTP status code"; `ev-057` registered; the IANA row in "What is still missing" filled in and replaced by the §16.2 registration procedure | topic chosen against the subject boundary after ev-057 was registered | @hpleapfrog |
| 2026-10-12 | added the claim "an unrecognized HTTP status code is handled as the class's x00 …"; the verified range of `ev-054` extended from three sections to four (preamble to §15 added); "What is still missing" rewritten to match | ev-054 already registered; §15 preamble extended against the priority named in the row below | @hpleapfrog |
| 2026-10-12 | first batch of 4 entries registered (2 `资源` + 2 `命题`), sources `ev-052` / `ev-053` / `ev-054`; "Current state" changed from "no entries yet" to an entry table, and "What is still missing" added | topic chosen against the subject boundary after ev-052/053/054 were registered | @hpleapfrog |
| 2026-10-12 | established the subject; added `computing` to `SUBJECT_SLUGS` | user asked to expand the knowledge domains (transport / computing / medical guidelines / economics) | @hpleapfrog |
