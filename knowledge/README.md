# 知识库索引

> 格式规范见 [FORMAT.md](../FORMAT.md)

## 学科

<!-- kbcheck:begin -->
| 学科 | 条目数 |
|---|---|
| [物理](physics/README.md) | 99 |
| [生活](life/README.md) | 8 |
| [医学](medicine/README.md) | 8 |
| [地理](geography/README.md) | 6 |
| [科学](science/README.md) | 1 |
| [交通](transport/README.md) | 4 |
| [计算机](computing/README.md) | 20 |
| [经济](economics/README.md) | 8 |
| [法律](law/README.md) | 4 |
| [事件（顶层）](../events/README.md) | 2 |
| **合计** | **158** |
<!-- kbcheck:end -->

> [!NOTE]
> **上表的数字由 `kbcheck.py` 生成**（唯一来源是 `index.json`），不手写；
> 同时校验器强制每个知识对象**必须**出现在它所属学科的 README 里（`check_readme_coverage`）。
> **本库的学科 README 曾漏登记三次**，所以这两条现在都是机械可查的。

## 目录约定

**目录名用英文**（路径会被复制成 URL，中文会变成百分号编码）；**中文条目的文件名仍用中文**。

| 目录 | `type` | 存什么 |
|---|---|---|
| `concepts/` | 知识点 | **概念节点**：承载先修关系；教法挂在其下 |
| `claims/` | 命题 | 有真假、需要收敛的知识主张 |
| `claims/attacks/` | 命题 | 攻击条目（`type` 仍是命题） |
| `methods/` | 教法 | 教学做法，条件性有效，**不收敛**，必填禁忌 |
| `misconceptions/` | 误解 | 常见错误概念，是教学资产 |
| `paths/` | 路径 | 知识点的编排，含先修约束与目标 |
| `resources/` | 资源 | 图示、动画、例题、习题 |
| `coverage/` | — | 覆盖度页（索引，不是知识对象） |

学科目录：`physics` `life` `medicine` `geography` `science` `transport` `computing`
`economics` `law`。

`evidence/` 在仓库根目录，为全库共享。

## 状态图例

| 状态 / Status | 含义 |
|---|---|
| 草案 / draft | 刚建立，证据不足 |
| 待审 / pending review | 有证据，等待复核 |
| 暂定确认 / provisionally confirmed | 作者已核对，但**没有非作者的独立复核**（仅命题可用） |
| 已确证 / confirmed | 存活论证结论一致（**仅命题可用**） |
| 失据 / unsupported | 曾有论证，**但被击倒了**：主张还在，当前没有支撑它的论证（仅命题可用） |
| 争议 / disputed | 存活论证结论冲突，并列展示，不选边 |
| 有效 / effective | 条件性成立（教法 / 误解 / 资源 / 路径） |
| 需复审 / needs re-review | 证据过期或条件变化 |
| 已推翻 / overturned · 已失效 / expired | 被更强证据推翻，或锚点无法定位 |

> [!IMPORTANT]
> **教法、误解、资源禁止使用「已确证」**——它们不存在唯一正确。

## 全部条目均为真实来源

自 2026-10-05 起，**本库不再有示例条目**。此前的 3 条示例（虚构作者 `@alice` 等 + 构造的课堂数据）
已全部重写或删除，其证据编号 `ev-009`~`ev-012` 已在 [evidence/README.md](../evidence/README.md) 标记作废。

| 来源 | 条目 |
|---|---|
| 出版社官方勘误表（[ev-014](../evidence/README.md) / ev-015） | 地理 6 条 · 科学 1 条 |
| 跨教材对比（ev-001 / [ev-016](../evidence/README.md) / ev-018） | 物理 5 条 |
| **OpenStax《Physics》Teacher Support**（[ev-020](../evidence/README.md)~ev-023，**CC BY**） | 物理 11 条 |

> [!IMPORTANT]
> **CC BY 来源正在成为主力。** `ev-018` 起接入的 OpenStax《Physics》是 **CC BY 4.0**，
> 可自由复用（署名即可），而 `ev-016` 那本同社教材是 CC BY-NC-SA，只能引用定位。
> **采集应优先在 CC BY 的源上做。**

> [!IMPORTANT]
> **这次清理不只是「换名字」。** 写 [类比选择与学段相关](physics/claims/类比选择与学段相关.md) 时，
> 我差点把示例条目当作证据引用——**示例条目会污染推论**，而不只是占位。
> 其中「把电压当成水流速度」那条，结论很可能是对的，但证据是编造的：
> **拿编造的数据支撑一个正确结论，仍然是造假。** 已替换为教材自身有记录的说法。

## 为什么大量条目停在「待审」

> [!NOTE]
> 按 [CONTRIBUTING](../CONTRIBUTING.md) 规则 3–4：
> 写成「已确证」需要**一名非作者的独立复核**，而**目前仓库只有一名贡献者**。
>
> 所以本库**没有任何一条处于终态**；绝大多数停在 `待审` / `有效` / `暂定确认`。
> **这不是录入没做完，是规则在正常生效。**
> **允许长期悬置。** 等第二位贡献者出现，`已确证` 才可能出现。
