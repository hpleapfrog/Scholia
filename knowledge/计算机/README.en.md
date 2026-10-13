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
| [RFC 2119, Key words for use in RFCs to Indicate Requirement Levels (IETF, BCP 14)](资源/RFC-2119-需求关键词.en.md) | 资源 | 有效 | `ev-052` |
| [RFC 9110, HTTP Semantics (IETF, STD 97)](资源/RFC-9110-HTTP语义.en.md) | 资源 | 有效 | `ev-054` |
| [In an RFC, MUST / SHOULD / MAY carry normative meaning only when written in all capitals](命题/RFC要求关键词只有全大写才成立.en.md) | 命题 | 暂定确认 | `ev-052` `ev-053` |
| [An HTTP method's safety and idempotency are set by the specification, and 'safe' does not mean 'free of side effects'](命题/HTTP方法的安全性与幂等性由规范分类决定.en.md) | 命题 | 暂定确认 | `ev-054` |
| [An unrecognized HTTP status code is handled as the class's x00, a code outside 100–599 as 5xx, and the reason phrase is only a recommendation](命题/未识别的HTTP状态码按该类x00处理.en.md) | 命题 | 暂定确认 | `ev-054` |
| [The complete list of HTTP status codes lives in the IANA registry, not in RFC 9110](命题/HTTP状态码的完整清单在IANA注册表不在RFC9110里.en.md) | 命题 | 暂定确认 | `ev-054` `ev-057` |
| [Adding an HTTP status code requires IETF Review, and the specification forbids new codes from disallowing content](命题/新增HTTP状态码须过IETFReview且不能禁止正文.en.md) | 命题 | 暂定确认 | `ev-054` |
| [An HTTP 204 response may contain neither content nor trailers, and is heuristically cacheable by default](命题/HTTP204响应不能含正文也不能含trailer且默认可缓存.en.md) | 命题 | 暂定确认 | `ev-054` |
| [An HTTP 405 response MUST carry an Allow header, and is heuristically cacheable by default](命题/HTTP405响应必须带Allow头部且默认可缓存.en.md) | 命题 | 暂定确认 | `ev-054` |
| [HTTP 410 means 'likely permanent'; if permanence is unknown, 404 ought to be used instead](命题/HTTP410表示很可能永久消失拿不准就应当用404.en.md) | 命题 | 暂定确认 | `ev-054` |
| [An HTTP 304 response MUST carry the cache headers a 200 would have sent, and may contain neither content nor trailers](命题/HTTP304响应必须带上原200会发的缓存头部且不能含正文或trailer.en.md) | 命题 | 暂定确认 | `ev-054` |
| [An HTTP 401 response MUST carry a WWW-Authenticate header, and the 401 / 403 division is not 'logged out vs no permission'](命题/HTTP401必须带WWW-Authenticate头部且401与403的分工不是没登录对没权限.en.md) | 命题 | 暂定确认 | `ev-054` |
| [An HTTP 503's Retry-After is a MAY, not a MUST, and the specification does not require 503 when a server is overloaded](命题/HTTP503的Retry-After是MAY而非MUST且过载时不必用503.en.md) | 命题 | 暂定确认 | `ev-054` |
| [HTTP 301/302 changing POST to GET is a MAY 'for historical reasons'; to preserve the method use 307/308](命题/HTTP301与302把POST改成GET是历史原因下的MAY且保留方法应用307与308.en.md) | 命题 | 暂定确认 | `ev-054` |
| [Treating 418 as a normative HTTP status code](误解/418不是规范里的状态码.en.md) | 误解 | 有效 | `ev-054` `ev-057` |

**All fifteen come from IETF's public RFCs and IANA's public registry** (`ev-052` / `ev-053` / `ev-054` / `ev-057`; verification depth is stated per entry).
That means this subject's current coverage is **not** the same as the subject "Computing" itself —
see "What is still missing" below.

### What is still missing

| Gap | Why it matters | Source needed |
|---|---|---|
| **The remaining individual codes of RFC 9110 §15.2–§15.6** | `204`, `301`–`308`, `401`, `403`, `405`, `410` and `503` are now verified (`ev-054`), and so is the registry (`ev-057`), and so is `418`'s full context (including "re-assigned when 4NN is exhausted"), but **not one definition of the other individual codes in the specification is** — the `400` / `422` division, `421`'s retry rule, the situations `414` applies to, this repo has only read second-hand | RFC 9110 §15.2–§15.6 (already inside `ev-054`, just unchecked) |
| **RFC 8126 §4.8's definition of IETF Review** | §16.2 is now verified (`ev-054`), but that section only writes "require IETF Review" and points to RFC 8126 — **RFC 8126 §4.8 itself has not been read**, so "what bar does IETF Review actually set" remains unanswerable | RFC 8126 §4.8 (new evidence needed) |
| **Language and platform documentation** | all twelve entries are network protocols; "the default behaviour of a given API" and "the conditions under which a compatibility rule applies" are entirely absent | official Python / Java documentation, with version number and release date |
| **Format and encoding specifications** | the **constraints and defaults** of things like `JSON` / `UTF-8` / `HTML` are where retellings go wrong most often | RFC 8259 · the Unicode Standard · WHATWG standards |
| **Version-difference entries** | "what changed for X between v1 and v2" is this subject's most typical checkable content, and the count is currently zero | the version-history pages of each specification |

**The next entry here should take the remaining individual codes** — `204`, `301`–`308`, `401`, `403`, `405`, `410` and `503` are already verified (`ev-054`) and so is the registry (`ev-057`),
but **not one definition of the other individual codes has been checked**.
`ev-054` is already registered, so **no new evidence is needed**.

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
| [Science](../科学/README.en.md) | errata in textbooks and publications: what is printed wrongly |

The same two criteria apply — **scarcity** and **risk**: procedures that can hurt are not held
(see [decision record: the boundary of procedural knowledge](../../docs/decisions/procedural-knowledge-boundary.en.md)),
tutorials are not repeated. **This repo does not teach how to write code; it records what the specification says.**

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
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
