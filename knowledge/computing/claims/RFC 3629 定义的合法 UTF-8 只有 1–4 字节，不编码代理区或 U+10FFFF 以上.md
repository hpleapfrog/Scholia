---
id: kb:computing:rfc3629-utf8-1to4-bytes
type: 命题
title: RFC 3629 定义的合法 UTF-8 只有 1–4 字节，不编码代理区或 U+10FFFF 以上
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 计算机 · 格式与编码规范
  学段: 不限
  适用: 核对「UTF-8 最长几字节」「代理区能不能编码」「C0/C1/F5–FF 是否可能出现」时
  条件: "**适用于 RFC 3629（STD 63，Standards Track，2003-11，DOI 10.17487/RFC3629）§1、§3 与 §4 原文**；本条只主张该文档定义的编码形式与合法字节序列，**不主张**解码器遇到非法序列时的具体报错方式（§3 只要求实现 MUST protect against decoding invalid sequences），也**不主张** Unicode 标准后续版本如何定义 UTF-8（§3 与 §4 声明权威定义在 Unicode Standard）"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-155]
license: CC-BY-SA-4.0
---

## 陈述

**RFC 3629 把 UTF-8 的字符范围限定在 U+0000–U+10FFFF，编码长度因此只有 1 到 4 字节；U+D800–U+DFFF 禁止编码，C0、C1、F5–FF 永不出现。所谓「合法的 5 字节 / 6 字节 UTF-8」在这份规范下不存在。**

| 约束 | 规范怎么说 | 出处 |
|---|---|---|
| 字符范围 | U+0000..U+10FFFF（UTF-16 可达范围）用 **1–4 个八位组**编码 | §3 |
| 代理区 | **禁止**编码 U+D800–U+DFFF；它们保留给 UTF-16 代理对，不直接表示字符 | §3 |
| 永不出现的字节值 | **C0、C1、F5–FF** | §1 |
| 编码唯一 | 长度表各行**互斥**：给定字符只有一种合法编码，没有超长形式 | §3 |

§4 的 ABNF 把同一组边界写成了首字节范围（`UTF8-tail = %x80-BF` 对每段都成立）：

| 长度 | 首字节 | 后续字节 |
|---|---|---|
| 1 | 00–7F | — |
| 2 | C2–DF | 80–BF ×1 |
| 3 | E0 A0–BF / E1–EC / ED 80–9F / EE–EF | 80–BF ×2 |
| 4 | F0 90–BF / F1–F3 / F4 80–8F | 80–BF ×3 |

三处排除各对应一条规则：`C2` 起排除了 C0/C1 的超长编码；`ED` 只到 `9F` 排除了代理区；`F4` 只到 `8F` 排除了 U+10FFFF 以上。

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

（以上四段分别见 §3、§3、§1、§3。）

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-155 | 官方文件 | 高 | IETF / RFC Editor，**RFC 3629**《UTF-8, a transformation format of ISO 10646》（F. Yergeau, Alis Technologies），STD 63，Standards Track，2003-11，DOI 10.17487/RFC3629，**§1–§18 全文已核**（787 行 / 33,856 字节，SHA-256 `a2a3a394…d6a6`；RFC Editor errata 页无记录） | 官方公开规范（The Internet Society 2003 版权声明）· **仅引用条款号与短引用，不转载全文** |

## 论证

### A1 · 三条边界是同一个 1–4 字节范围的三面（尚无攻击）

- **主张**：代理区禁令、U+10FFFF 上限与 C0/C1/F5–FF 禁止不是三份互不相干的清单，而是「只允许 1–4 字节」在首字节与长度上的必然结果；§4 的 ABNF 把这三条写进了同一个文法
- **前提**：ev-155 §3 的 U+0000..U+10FFFF 与 1–4 个八位组；§3 的代理区禁令；§1 的 C0/C1/F5–FF；§3 的「各行互斥、只有一种合法编码」；§4 的首字节范围
- **推理**：上限 U+10FFFF 意味着最多 4 字节，所以 5/6 字节的首字节 F5–FF 不可能出现；2 字节段最小只能表示 U+0080，所以 C0/C1 只能构成超长编码；代理区被排除，所以 `ED` 的第二字节不得进入 `A0–BF`，ABNF 相应收窄到 `80–9F`；同理 `F0` 从 `90` 起、`F4` 到 `8F` 止。`C0 80`（超长短编码 U+0000）、`ED A1 8C`（代理区）与 `F4 90 80 80`（超过 U+10FFFF）因此都不是 RFC 3629 的合法 UTF-8
- **证据**：ev-155
- **被攻击**：尚无攻击
- **署名**：@hpleapfrog · 2026-10-21

### A2 · 1–4 字节是一次版本收紧，且规范自己给出了溢出理由（尚无攻击）

- **主张**：RFC 3629 的 1–4 字节限制不是历来如此：它取代 RFC 2279，并在 §12 把「字符范围限制到 0000–10FFFF」列为变更；§10 还说明 ISO/IEC 10646 对 UTF-8 的描述允许到 U+7FFFFFFF、会产生 5 与 6 字节序列，并把未限制范围列为缓冲区溢出风险
- **前提**：ev-155 首页的 `Obsoletes: 2279`；§12 的第一条变更；§10 关于 U+7FFFFFFF、5/6 字节与缓冲区溢出的段落
- **推理**：如果实现按旧描述或按「最多 4 字节」之外的范围分配缓冲区，5/6 字节序列就会越界。RFC 3629 因此既收紧范围又明确风险；接受 5/6 字节序列的解析器不符合这份规范，即使别的描述允许它
- **证据**：ev-155
- **被攻击**：尚无攻击。**本条不主张 RFC 2279 原文的细节**，只引用 RFC 3629 自己列出的变更与风险
- **署名**：@hpleapfrog · 2026-10-21

### A3 · 本条主张的是 RFC 3629 的约束，不是 UTF-8 的最终权威（尚无攻击）

- **主张**：RFC 3629 自己把 UTF-8 的权威定义指向 Unicode Standard，并声明 §4 的 ABNF 不自称权威；本条因此只引用 RFC 3629 作为 IETF 标准的约束，不把它当成 UTF-8 的最终文本
- **前提**：ev-155 §3 第一句「UTF-8 is defined by the Unicode Standard」；§4 的 NOTE「The authoritative definition of UTF-8 is in [UNICODE]... does not claim to be authoritative」
- **推理**：如果 Unicode 之后修改了定义，本条 §3/§4 的版本限定就会失效；在 RFC 3629 仍是现行的 STD 63 期间，它给出的边界仍可核对。把 ABNF 当权威会越过 §4 自己的声明
- **证据**：ev-155
- **被攻击**：尚无攻击。**本条不主张 ABNF 是权威定义**，只把它当作 RFC 3629 对编码规则的描述
- **署名**：@hpleapfrog · 2026-10-21

## 怎么反驳它

- [ ] 找到 **RFC 3629 之后取代它**的规范（若有，本条 §3/§4 的版本限定即失效）
- [ ] 给出一个符合 RFC 3629 的 **5 或 6 字节** UTF-8 序列（1–4 字节边界的反例）
- [ ] 给出一个编码 **U+D800–U+DFFF** 或 **U+10FFFF 以上**码点的合法序列（范围禁令的反例）
- [ ] 指出 **C0、C1、F5–FF** 在 RFC 3629 某节被允许（永不出现清单的反例）
- [ ] 指出本条把 §4 的 ABNF 当成了权威定义（本条只把它当描述；§4 NOTE 已注明）

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-21 | 建立条目；核毕 RFC 3629 §1–§18 全文；登记 ev-155；按 §1/§3/§4 归集 1–4 字节、代理区与首字节禁止项，并按 §10/§12 记下与 RFC 2279 的版本差异 | ev-155 | @hpleapfrog |
