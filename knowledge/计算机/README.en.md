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

**All five come from IETF's public RFCs** (`ev-052` / `ev-053` / `ev-054`; verification depth is stated per entry).
That means this subject's current coverage is **not** the same as the subject "Computing" itself —
see "What is still missing" below.

### What is still missing

| Gap | Why it matters | Source needed |
|---|---|---|
| **The individual codes of RFC 9110 §15.2–§15.6** | the **preamble** to §15 is verified (`ev-054`), but **not one individual code is** — why `204` may not carry content, why `306` is marked Unused, are all answered in the specification and this repo has not read them | RFC 9110 §15.2–§15.6 (already inside `ev-054`, just unchecked) |
| **The IANA HTTP Status Code Registry** | §15.1 says unrecognized codes are to be registered in this table, and **which codes are registered and which are not, this repo has no idea** | [IANA's status code registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) |
| **Language and platform documentation** | all five entries are network protocols; "the default behaviour of a given API" and "the conditions under which a compatibility rule applies" are entirely absent | official Python / Java documentation, with version number and release date |
| **Format and encoding specifications** | the **constraints and defaults** of things like `JSON` / `UTF-8` / `HTML` are where retellings go wrong most often | RFC 8259 · the Unicode Standard · WHATWG standards |
| **Version-difference entries** | "what changed for X between v1 and v2" is this subject's most typical checkable content, and the count is currently zero | the version-history pages of each specification |

**The next entry here should take the IANA registry first** — the preamble to §15 is done, and the registry is its natural landing point;
`ev-054` is not enough, and **the IANA table has to be registered as new evidence**.

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-12 | added the claim "an unrecognized HTTP status code is handled as the class's x00 …"; the verified range of `ev-054` extended from three sections to four (preamble to §15 added); "What is still missing" rewritten to match | ev-054 already registered; §15 preamble extended against the priority named in the row below | @hpleapfrog |
| 2026-10-12 | first batch of 4 entries registered (2 `资源` + 2 `命题`), sources `ev-052` / `ev-053` / `ev-054`; "Current state" changed from "no entries yet" to an entry table, and "What is still missing" added | topic chosen against the subject boundary after ev-052/053/054 were registered | @hpleapfrog |
| 2026-10-12 | established the subject; added `computing` to `SUBJECT_SLUGS` | user asked to expand the knowledge domains (transport / computing / medical guidelines / economics) | @hpleapfrog |

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
| 2026-10-12 | established the subject; added `computing` to `SUBJECT_SLUGS` | user asked to expand the knowledge domains (transport / computing / medical guidelines / economics) | @hpleapfrog |
