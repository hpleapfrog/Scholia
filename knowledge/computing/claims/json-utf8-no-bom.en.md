---
id: kb:computing:json-utf8-no-bom
type: 命题
title: "JSON exchanged between systems must use UTF-8 (closed ecosystems excepted), and network-transmitted JSON must not begin with a BOM"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 计算机 · 格式与编码规范
  学段: 不限
  适用: when you need to check "which encoding JSON actually requires", "whether a BOM may be added", or "whether a parser tolerating a BOM authorises sending one"
  条件: "**applies to RFC 8259 (STD 90, Standards Track, 2017-12, DOI 10.17487/RFC8259) section 8.1 as written**; this entry claims only the two scenarios **exchange between systems** and **network transmission**. It does **not** claim which byte sequences a parser must accept or reject, and does **not** claim which encoding a closed ecosystem should use (section 8.1 leaves that unspecified)"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-154]
license: CC-BY-SA-4.0
---

> **English version of [`系统之间交换的 JSON 必须用 UTF-8（封闭生态除外），网络传输不得添加 BOM.md`](系统之间交换的 JSON 必须用 UTF-8（封闭生态除外），网络传输不得添加 BOM.md).**

## 陈述

**JSON exchanged between systems that are not part of a closed ecosystem must be encoded in UTF-8; network-transmitted JSON must not begin with a BOM — but a parser may choose to ignore one. Both are scoped requirements, not the universal judgement "JSON is always UTF-8 and any BOM is illegal".**

| Scenario | What the specification says | Where |
|---|---|---|
| exchange between systems, **not a closed ecosystem** | the text **MUST** be encoded in UTF-8 | section 8.1, first sentence |
| **network-transmitted** JSON text | implementations **MUST NOT** add a BOM (U+FEFF) at the beginning | section 8.1, second paragraph |
| parsing a JSON text | implementations **MAY** ignore a BOM rather than treating it as an error | section 8.1, second paragraph |
| exchange **inside a closed ecosystem** | section 8.1 **does not specify** an encoding; the UTF-8 MUST does not apply | the qualifier in the first sentence of section 8.1 |

The rules, each with its sentence from the source (short quotes):

The encoding requirement, with the "closed ecosystem" qualifier (section 8.1):

> JSON text exchanged between systems that are not part of a closed
> ecosystem MUST be encoded using UTF-8 [RFC3629].

The reason the specification gives is interoperability, not "UTF-8 is superior" (section 8.1):

> Previous specifications of JSON have not required the use of UTF-8
> when transmitting JSON text.  However, the vast majority of JSON-
> based software implementations have chosen to use the UTF-8 encoding,
> to the extent that it is the only encoding that achieves
> interoperability.

The BOM prohibition is scoped to **network transmission**, while parser tolerance is MAY (section 8.1):

> Implementations MUST NOT add a byte order mark (U+FEFF) to the
> beginning of a networked-transmitted JSON text.  In the interests of
> interoperability, implementations that parse JSON texts MAY ignore
> the presence of a byte order mark rather than treating it as an
> error.

## 依据

| ID | Kind | Grade | Locator | License |
|---|---|---|---|---|
| ev-154 | official document | high | IETF / RFC Editor, **RFC 8259** "The JavaScript Object Notation (JSON) Data Interchange Format" (T. Bray, Ed., Textuality), STD 90, Standards Track, 2017-12, DOI 10.17487/RFC8259, **sections 1–14 and Appendix A read in full** (899 lines / 28,360 bytes, SHA-256 `61a5378f…d2d7`) | public official specification (IETF Trust, BCP 78 / Revised BSD legal provisions) · **section numbers and short quotes only, no full-text reuse** |

## 论证

### A1 · The UTF-8 requirement carries an undefined exception (no attack yet)

- **Claim**: "JSON must use UTF-8" holds only for exchange **between systems that are not part of a closed ecosystem**; section 8.1 **does not define** the boundary of a closed ecosystem, and **does not say** that UTF-16 or UTF-32 is allowed inside one
- **Premise**: the qualifier "that are not part of a closed ecosystem" in the first sentence of ev-154 section 8.1, and the interoperability rationale in its second paragraph; Appendix A summarises the revision only as "require the use of UTF-8 when transmitted over a network"
- **Reasoning**: the specification **limits the force of UTF-8 to interoperability scenarios**, on the ground that it is the only encoding that achieves interoperability. Dropping the qualifier turns a conditional statement into a universal one; conversely, "closed ecosystems are excluded" does not imply "a closed ecosystem is therefore blessed to use UTF-16" — section 8.1 stays silent on that case
- **Evidence**: ev-154
- **Attacked by**: no attack yet. **This entry does not claim that any particular encoding is allowed inside a closed ecosystem**; it claims only that the UTF-8 MUST does not reach there
- **By**: @hpleapfrog · 2026-10-21

### A2 · The BOM prohibition and the tolerance are asymmetric, and each is scoped (no attack yet)

- **Claim**: a sender **MUST NOT** add a BOM (limited to **network-transmitted** JSON text), while a parser **MAY** ignore one; a parser's tolerance does not authorise a sender, nor does it widen the prohibition to all JSON text
- **Premise**: the two sentences in the second paragraph of ev-154 section 8.1 — the subjects are "implementations" as sender and as parser, and the auxiliaries are MUST NOT and MAY
- **Reasoning**: MAY gives **the parser** a choice; it does not alter **the sender's** MUST NOT. Each sentence also carries a scope: the prohibition says `networked-transmitted`, not "any JSON file". So "my parser accepts a BOM" and "I may send a BOM" are two different propositions, and the second fails even for network transmission
- **Evidence**: ev-154
- **Attacked by**: no attack yet. **This entry does not claim that a local file with a BOM must fail to parse** — that depends on the implementation, not on section 8.1
- **By**: @hpleapfrog · 2026-10-21

## How to attack it

- [ ] Show a document that **supersedes RFC 8259** (if so, the version qualifier on section 8.1 fails)
- [ ] Give an instance of exchange between systems outside a closed ecosystem that lawfully avoids UTF-8 (a counterexample to the MUST in section 8.1)
- [ ] Show that this entry **widens** the BOM prohibition beyond network transmission (it claims network transmission only)
- [ ] Show that this entry reads the parser's "MAY ignore" as "MUST ignore" (that would be a different, false proposition)

## 变更记录

| Date | Action | Basis | By |
|---|---|---|---|
| 2026-10-21 | entry created; RFC 8259 sections 1–14 and Appendix A read in full; ev-154 registered; the encoding requirement, BOM prohibition and parser tolerance collected from section 8.1 | ev-154 | @hpleapfrog |
