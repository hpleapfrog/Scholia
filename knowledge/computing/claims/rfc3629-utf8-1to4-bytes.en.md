---
id: kb:computing:rfc3629-utf8-1to4-bytes
type: 命题
title: "RFC 3629 limits valid UTF-8 to 1-4 bytes and forbids encoding surrogates or code points above U+10FFFF"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 计算机 · 格式与编码规范
  学段: 不限
  适用: when you need to check "how many bytes UTF-8 can take", "whether surrogates may be encoded", or "whether C0/C1/F5-FF can appear"
  条件: "**applies to RFC 3629 (STD 63, Standards Track, 2003-11, DOI 10.17487/RFC3629) sections 1, 3 and 4 as written**; this entry claims only the encoding form and the valid byte sequences defined there. It does **not** claim how a decoder must report an invalid sequence (section 3 requires implementations to MUST protect against decoding invalid sequences, but does not prescribe the error), and does **not** claim how later versions of the Unicode Standard define UTF-8 (sections 3 and 4 name the Unicode Standard as the authoritative definition)"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-155]
license: CC-BY-SA-4.0
---

> **English version of [`RFC 3629 定义的合法 UTF-8 只有 1–4 字节，不编码代理区或 U+10FFFF 以上.md`](RFC 3629 定义的合法 UTF-8 只有 1–4 字节，不编码代理区或 U+10FFFF 以上.md).**

## 陈述

**RFC 3629 restricts UTF-8 to U+0000-U+10FFFF, so a valid sequence is 1 to 4 octets; U+D800-U+DFFF must not be encoded, and C0, C1 and F5-FF never appear. There is no valid 5- or 6-byte UTF-8 under this specification.**

| Constraint | What the specification says | Where |
|---|---|---|
| character range | U+0000..U+10FFFF (the UTF-16 accessible range) is encoded in **1-4 octets** | section 3 |
| surrogates | encoding U+D800-U+DFFF is **prohibited**; they are reserved for UTF-16 surrogate pairs and do not directly represent characters | section 3 |
| octet values that never appear | **C0, C1, F5-FF** | section 1 |
| uniqueness | the rows of the length table are **mutually exclusive**: a given character has only one valid encoding, with no overlong form | section 3 |

The ABNF in section 4 writes the same boundaries as first-octet ranges (`UTF8-tail = %x80-BF` applies to every continuation octet):

| Length | First octet | Continuation octets |
|---|---|---|
| 1 | 00-7F | — |
| 2 | C2-DF | 80-BF ×1 |
| 3 | E0 A0-BF / E1-EC / ED 80-9F / EE-EF | 80-BF ×2 |
| 4 | F0 90-BF / F1-F3 / F4 80-8F | 80-BF ×3 |

Each exclusion encodes one rule: starting at `C2` excludes the overlong C0/C1 forms; `ED` stopping at `9F` excludes the surrogate range; `F4` stopping at `8F` excludes code points above U+10FFFF.

> In UTF-8, characters from the U+0000..U+10FFFF range (the UTF-16
> accessible range) are encoded using sequences of 1 to 4 octets.

> The definition of UTF-8 prohibits encoding character numbers between
> U+D800 and U+DFFF, which are reserved for use with the UTF-16
> encoding form (as surrogate pairs) and do not directly represent
> characters.

> The octet values C0, C1, F5 to FF never appear.

> It is important to note
> that the rows of the table are mutually exclusive, i.e., there is
> only one valid way to encode a given character.

(The four passages are from sections 3, 3, 1 and 3 respectively.)

## 依据

| ID | Kind | Grade | Locator | License |
|---|---|---|---|---|
| ev-155 | official document | high | IETF / RFC Editor, **RFC 3629** "UTF-8, a transformation format of ISO 10646" (F. Yergeau, Alis Technologies), STD 63, Standards Track, 2003-11, DOI 10.17487/RFC3629, **sections 1-18 read in full** (787 lines / 33,856 bytes, SHA-256 `a2a3a394…d6a6`; no errata listed on the RFC Editor errata page) | public official specification (The Internet Society 2003 copyright statement) · **section numbers and short quotes only, no full-text reuse** |

## 论证

### A1 · The three boundaries are three faces of one 1-4 byte range (no attack yet)

- **Claim**: the surrogate prohibition, the U+10FFFF ceiling and the ban on C0/C1/F5-FF are not three unrelated lists; they follow from "1-4 bytes only" at the first-octet and length boundaries, and section 4's ABNF writes all three into one grammar
- **Premise**: the U+0000..U+10FFFF range and 1-4 octets in ev-155 section 3; the surrogate prohibition in section 3; C0/C1/F5-FF in section 1; "mutually exclusive rows, only one valid encoding" in section 3; the first-octet ranges in section 4
- **Reasoning**: a U+10FFFF ceiling means at most 4 octets, so the 5/6-byte leads F5-FF cannot occur; the two-octet range starts at U+0080, so C0/C1 can only produce overlong forms; with surrogates excluded, the second octet after `ED` cannot enter `A0-BF`, and the ABNF narrows it to `80-9F`; likewise `F0` starts at `90` and `F4` stops at `8F`. Therefore `C0 80` (an overlong encoding of U+0000), `ED A1 8C` (a surrogate) and `F4 90 80 80` (above U+10FFFF) are not valid UTF-8 under RFC 3629
- **Evidence**: ev-155
- **Attacked by**: no attack yet
- **By**: @hpleapfrog · 2026-10-21

### A2 · The 1-4 byte limit was a version tightening, and the specification gives the overflow reason itself (no attack yet)

- **Claim**: the 1-4 byte limit was not always so: RFC 3629 obsoletes RFC 2279 and lists "restricted the range of characters to 0000-10FFFF" as a change in section 12; section 10 also says the ISO/IEC 10646 description of UTF-8 allows up to U+7FFFFFFF and 5- and 6-byte sequences, and names an unrestricted range as a buffer-overflow risk
- **Premise**: `Obsoletes: 2279` on the first page of ev-155; the first change item in section 12; the paragraph on U+7FFFFFFF, 5- and 6-byte sequences and buffer overflow in section 10
- **Reasoning**: an implementation that follows the older description, or sizes buffers for anything other than "at most 4 bytes", can overflow on a 5- or 6-byte sequence. RFC 3629 therefore both narrows the range and states the risk; a parser that accepts 5- or 6-byte sequences is not following this specification, even if another description permits them
- **Evidence**: ev-155
- **Attacked by**: no attack yet. **This entry does not claim the details of RFC 2279's text**; it cites only the changes and risks RFC 3629 itself records
- **By**: @hpleapfrog · 2026-10-21

### A3 · This entry claims RFC 3629's constraints, not the final authority on UTF-8 (no attack yet)

- **Claim**: RFC 3629 points to the Unicode Standard for the authoritative definition of UTF-8 and says its section 4 ABNF does not claim to be authoritative; this entry therefore cites RFC 3629 as an IETF-standard constraint, not as UTF-8's final text
- **Premise**: the first sentence of ev-155 section 3, "UTF-8 is defined by the Unicode Standard"; the section 4 NOTE, "The authoritative definition of UTF-8 is in [UNICODE]... does not claim to be authoritative"
- **Reasoning**: if Unicode later changes the definition, this entry's section 3/4 version qualifier fails; while RFC 3629 remains the current STD 63, its boundaries are checkable. Treating the ABNF as authoritative would overrun section 4's own disclaimer
- **Evidence**: ev-155
- **Attacked by**: no attack yet. **This entry does not claim the ABNF is the authoritative definition**; it treats it as RFC 3629's description of the encoding rules
- **By**: @hpleapfrog · 2026-10-21

## How to attack it

- [ ] Show a document that **supersedes RFC 3629** (if so, the section 3/4 version qualifier fails)
- [ ] Give a **5- or 6-byte** UTF-8 sequence that RFC 3629 permits (a counterexample to the 1-4 byte boundary)
- [ ] Give a valid sequence encoding a **U+D800-U+DFFF** or **above U+10FFFF** code point (a counterexample to the range bans)
- [ ] Show that **C0, C1 or F5-FF** is permitted somewhere in RFC 3629 (a counterexample to the never-appear list)
- [ ] Show that this entry treats the section 4 ABNF as authoritative (it only treats it as a description; the section 4 NOTE says so)

## 变更记录

| Date | Action | Basis | By |
|---|---|---|---|
| 2026-10-21 | entry created; RFC 3629 sections 1-18 read in full; ev-155 registered; the 1-4 byte range, surrogate ban and first-octet bans collected from sections 1/3/4; the RFC 2279 version difference recorded from sections 10/12 | ev-155 | @hpleapfrog |
