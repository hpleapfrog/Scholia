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
| [HTTP 1xx responses are interim: they MUST NOT be sent to an HTTP/1.0 client, cannot contain content or trailers, and a client MUST be able to parse one even if it MAY ignore it](claims/http-1xx-interim-responses.en.md) | 命题 | 暂定确认 | `ev-054` |
| [HTTP 202 does not promise the request will ever be processed, and HTTP has no facility for re-sending a final status code afterwards](claims/http-202-no-async-status-resend.en.md) | 命题 | 暂定确认 | `ev-054` |
| [HTTP 205 requires the user agent to reset the 'document view', and the server MUST NOT generate content](claims/http-205-reset-document-view-no-content.en.md) | 命题 | 暂定确认 | `ev-054` |
| [An HTTP 206's Content-Length is not the complete resource length (the complete length is in Content-Range), and the server MUST generate the cache and validator headers a 200 would have sent](claims/http-206-partial-content-header-duties.en.md) | 命题 | 暂定确认 | `ev-054` |
| [HTTP 402 is 'reserved for future use', 305 is deprecated and 306 is unused: three registered codes with no semantics](claims/http-reserved-deprecated-codes.en.md) | 命题 | 暂定确认 | `ev-054` |
| [An HTTP 404 does not say whether the lack is temporary or permanent, and is also used to avoid disclosing that a resource exists](claims/http-404-temporary-vs-permanent-non-disclosure.en.md) | 命题 | 暂定确认 | `ev-054` |
| [Treating 418 as a normative HTTP status code](misconceptions/http-418-is-real.en.md) | 误解 | 有效 | `ev-054` `ev-057` |
| [HTTP 451 refuses access for legal reasons and does not imply whether the resource exists](claims/http-451-legal-unavailable.en.md) | 命题 | 暂定确认 | `ev-153` `ev-054` `ev-057` |
| [JSON exchanged between systems must use UTF-8 (closed ecosystems excepted), and network-transmitted JSON must not begin with a BOM](claims/json-utf8-no-bom.en.md) | 命题 | 暂定确认 | `ev-154` |
| [RFC 3629 limits valid UTF-8 to 1-4 bytes and forbids encoding surrogates or code points above U+10FFFF](claims/rfc3629-utf8-1to4-bytes.en.md) | 命题 | 暂定确认 | `ev-155` |

**All twenty-nine come from IETF's public RFCs and IANA's public registry** (`ev-052` / `ev-053` / `ev-054` / `ev-057` / `ev-089` / `ev-154` / `ev-155`; verification depth is stated per entry).
That means this subject's current coverage is **not** the same as the subject "Computing" itself —
see "What is still missing" below.

### What is still missing

| Gap | Why it matters | Source needed |
|---|---|---|
| **Language and platform documentation** | the entries so far cover network protocols and one format specification; "the default behaviour of a given API" and "the conditions under which a compatibility rule applies" are entirely absent | official Python / Java documentation, with version number and release date |
| **Format and encoding specifications** | the JSON encoding rules (RFC 8259 §8.1) and the UTF-8 byte boundaries (RFC 3629 §3/§4) are now covered; the **constraints and defaults** of `HTML` are still absent, and the authoritative definition of UTF-8 sits in the Unicode Standard rather than in the RFC | the Unicode Standard · the WHATWG HTML standard |
| **Version-difference entries** | "what changed for X between v1 and v2" is this subject's most typical checkable content, and the count is currently zero | the version-history pages of each specification |

**The next entry here should still be a "format and encoding specification"** — the main protocol-side gaps (the whole of HTTP status-code §15, the registration procedure) are filled,
and **the encoding and BOM rules of RFC 8259 (JSON) §8.1 and the 1-4 byte boundary of RFC 3629 (UTF-8) §3/§4 were added on 2026-10-21**;
but not a single entry covers the constraints and defaults of the Unicode Standard (the authority RFC 3629 points to) or `HTML` (WHATWG); **new evidence is needed**.

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
| 2026-10-21 | added the claim "RFC 3629 limits valid UTF-8 to 1-4 bytes and forbids encoding surrogates or code points above U+10FFFF", verifying RFC 3629 §1–§18 in full (§1/§3/§4 the byte boundaries, the surrogate prohibition and the ABNF; §10/§12 the overflow rationale and the version tightening); `ev-155` registered; the format-and-encoding row in "What is still missing" now names Unicode / HTML, and the "next entry" paragraph was rewritten to match | topic chosen against the subject boundary after ev-155 (RFC 3629) was registered | @hpleapfrog |
| 2026-10-21 | added the claim "JSON exchanged between systems must use UTF-8 (closed ecosystems excepted), and network-transmitted JSON must not begin with a BOM", verifying RFC 8259 §1–§14 and Appendix A in full (§8.1 encoding and BOM); `ev-154` registered; the format-and-encoding row in "What is still missing" now names UTF-8 / Unicode / HTML, and the "next entry" paragraph was rewritten to match | topic chosen against the subject boundary after ev-154 (RFC 8259) was registered | @hpleapfrog |
| 2026-10-18 | added six claims: 1xx (the four interim-response rules and 100 / 101), 202 (no promise of processing, no asynchronous re-send), 205 (reset of the document view and the prohibition on content), 206 (length semantics and header duties), 402 / 305 / 306 (three placeholder codes) and 404 (its two-branch semantics and its silence on temporary vs permanent), verifying all of RFC 9110 §15 (including §15.3.7.1–§15.3.7.3); the "remaining individual codes" row in "What is still missing" cleared, and the "next entry" paragraph rewritten | ev-054 already registered; swept up against the priority named in "What is still missing" | @hpleapfrog |
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
