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

**All four come from IETF's public RFCs** (`ev-052` / `ev-053` / `ev-054`; verification depth is stated per entry).
That means this subject's current coverage is **not** the same as the subject "Computing" itself —
see "What is still missing" below.

### What is still missing

| Gap | Why it matters | Source needed |
|---|---|---|
| **RFC 9110 §15, status codes one by one** | this repo verified §2.2 and §9.2 only — not a single status code, and they are the most-asked-about part | RFC 9110 §15 (already inside `ev-054`, just unchecked) |
| **Language and platform documentation** | all four entries are network protocols; "the default behaviour of a given API" and "the conditions under which a compatibility rule applies" are entirely absent | official Python / Java documentation, with version number and release date |
| **Format and encoding specifications** | the **constraints and defaults** of things like `JSON` / `UTF-8` / `HTML` are where retellings go wrong most often | RFC 8259 · the Unicode Standard · WHATWG standards |
| **Version-difference entries** | "what changed for X between v1 and v2" is this subject's most typical checkable content, and the count is currently zero | the version-history pages of each specification |

**The next entry here should take §15 first** — `ev-054` is already registered, so **no new evidence is needed**;
only the verified range has to be extended.

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
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
