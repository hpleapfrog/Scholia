---
id: kb:physics:up1-errata-14975
type: 命题
title: "Erratum #14975 in University Physics Volume 1 (Chapter 1): Unit 1 Mechanics: Chapter 1 Units and Measurement: Section 1.6 Significant Figur…"
status: 待审
author: "@hpleapfrog"
created: 2026-10-20
updated: 2026-10-20
scope:
  学科: 物理
  学段: 大学
  适用: "teachers and students using OpenStax *University Physics Volume 1*"
  条件: "public errata record #14975 (submitted 2021-01-25, Completed / Approved); the record itself is cited, not the current web text"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-150]
license: CC-BY-SA-4.0
---

> **English version of [`勘误-UP1-14975.md`](勘误-UP1-14975.md).**

## Statement

The public errata record [#14975](https://openstax.org/errata/14975) for OpenStax *University Physics Volume 1* concerns
**Unit 1 Mechanics: Chapter 1 Units and Measurement: Section 1.6 Significant Figures** and states the following (submitted 2021-01-25; status Completed;
resolution Approved):

> Book states: "When combining measurements with different degrees of precision, the number of significant digits in the final answer can be no greater than the number of significant digits in the least-precise measured value."
> This may be true for addition, subtraction, multiplication, and division, but it is not true for other common mathematics such as exponentials or trig functions. Consider an uncertainty of ±0.5% (i.e. two significant figures or 1% absolute bound):
> • log(98) vs log(99): error of only 0.2%. log() can actually *increase* the number of significant figures. 
> • tan(98°) vs tan(99°): error of 11%.
> • tan(98rad) vs tan(99rad): error of 3500%. Not even 1 sig fig.……

Publisher's resolution:

> Revise the sentence "When combining measurements with..." to "When combining measurements with different degrees of precision with the mathematical operations of addition, subtraction, multiplication, or division, then the number of significant digits in the final answer can be no greater than the number of significant digits in the least-precise measured value."

> [!NOTE]
> This entry claims only that "the publisher recorded and accepted this erratum".
> **It does not claim that this repository checked the current web text**; cite the
> permanent link when verifying.

## Basis

| Number | Type | Grade | Locator | License |
|---|---|---|---|---|
| ev-150 | publisher errata list | high | OpenStax *University Physics Volume 1* erratum #14975 · [permanent link](https://openstax.org/errata/14975) · Chapter 1 | external source · locators and short quotes only |

## Argument

### A1 · Publisher's errata record (no attack yet)

- **Claim**: OpenStax recorded #14975 as an accepted erratum and gave the correction to be made
- **Premise**: the public errata page #14975 shows the location, description, status Completed and resolution Approved (ev-150)
- **Reasoning**: a publisher's errata record for its own textbook is direct grounds that the passage is wrong and should be corrected as recorded; this repository adds no inference beyond that
- **Evidence**: ev-150
- **Attacked**: no attack yet
- **Signed**: @hpleapfrog · 2026-10-20

## Nature

**Factual inaccuracy**: the entry records a correction accepted by the publisher; it does not assert that the current web text still shows the error.

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-20 | Batch import (OpenStax public errata snapshot) | ev-150 · erratum #14975 | @hpleapfrog |
