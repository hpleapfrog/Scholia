# GitHub 落地设计

> 状态：落地设计稿（未实现）
> 上游：[抽象设计](00-抽象设计.md)
> 目标：把抽象设计完整映射到 GitHub 原生功能上，并明确哪些地方必须加护栏

---

## 0. 一句话

**GitHub 不是这个系统的"邻居"，它就是这套机制的载体**：Issues 承载"可判定的问题"，PR 承载"修改 + 证据"，Discussions 承载"还没成型的想法"，Actions 承载"规则即代码"。

但 GitHub 缺三样东西，必须自己补：**论证图求值**、**证据门槛**、**AI 的署名与边界**。这三样全靠仓库内的结构化文件 + CI 补齐。

---

## 1. 抽象概念 → GitHub 原语的映射

| 抽象概念 | GitHub 原语 | 说明 |
|---|---|---|
| 知识点 / 命题 / 教法 / 路径 / 误解 / 资源 | **仓库内的结构化文件**（YAML） | 内容寻址由 git 对象哈希天然提供 |
| 勘误提议 | **Pull Request** | 唯一能改变结论的通道 |
| 可判定的问题 | **Issue** | 触发工作流；不可判定的话题不进 Issue |
| 探索性讨论、方法论之争 | **Discussions** | **不参与判定**（关键护栏） |
| 署名 | 提交签名 / 账号 + `author` 字段 | 不可匿名 |
| "我复核过"（认领，不等于赞同） | Review 的 `Approve` / `Comment` | 与"我赞同"严格区分 |
| 论证对象 | `arguments/<知识点>/<论证>.yaml` | 每个论证一个文件 |
| 证据 | `evidence/` + 文件内 `evidence[]` | 附件与结论分离 |
| 规则即代码 | **GitHub Actions + 分支保护** | 不通过就合不进去 |
| 立法 / 执行分离 | 分支保护勾选 **Do not allow bypassing** | 维护者也绕不过 |
| 领域维护者 | `CODEOWNERS` | 权限限于规则允许范围 |
| 冻结版本 | **Release + tag** | "2027 春季版" |
| 结论 | **由 CI 写入 `derived` 字段** | **人工不得直接改** |
| 争议 | label `status:争议` + 文件内状态 | 显式保留，不静默覆盖 |
| 时效复审 | scheduled workflow → 自动开 Issue | 证据过期即降级 |
| 分叉退出 | **fork** | 天然，且历史完整 |
| 投票 | —— **没有这个东西** | 👍 只作注意力排序，不作为判定 |

---

## 2. 三个通道的严格分工

```
Discussions ──（想法成型）──▶ Issues ──（产出证据与论证）──▶ PR ──▶ CI 求值 ──▶ 结论
   不参与判定                    触发工作流                  唯一改结论的通道
```

### 2.1 Discussions：允许混乱

分类建议：

| 分类 | 用途 |
|---|---|
| 📣 公告 | 版本发布、规则变更通知 |
| 💬 方法论 | 判定规则本身怎么定（对应"立法"环节） |
| ❓ 提问 | 使用问题 |
| 🧪 探索性假设 | 还没成型的主张，允许不严谨 |
| 🗳️ 治理提案 | 收敛器规则、领域权重、资助 |

**硬规则**：Discussion 里的任何主张，**在升级为 Issue + PR 之前，对结论零影响**。这是防止长讨论稀释判定的第一道闸门。

### 2.2 Issues：只放可判定的问题

一张 Issue 必须能被回答为"是/否/证据不足"。允许的模板只有三种（见 §5）：

- 疑似错误（命题类）
- 新增或修订教法（教法类）
- 先修关系争议（路径类）

"这本书怎么样""物理该怎么教"这类话题**不建 Issue**，去 Discussions。

### 2.3 PR：唯一的结论通道

PR 只允许做三件事：**加证据、加论证、改适用范围**。

**PR 绝对不能直接修改 `status` 与 `derived` 字段**——那是 CI 算出来的。违反者由 `guard-status.yml` 直接判失败。

---

## 3. 仓库结构

```
.
├─ README.md
├─ CONTRIBUTING.md
├─ CODEOWNERS
├─ knowledge/                        # 知识对象（按学科分目录）
│  └─ physics/
│     ├─ ohm-law.yaml                # 命题
│     ├─ method-water-pipe.yaml      # 教法
│     ├─ path-junior-electricity.yaml# 路径
│     ├─ miscon-voltage-flow.yaml    # 误解
│     └─ res-water-animation.yaml    # 资源
├─ arguments/                        # 论证图（每个论证一个文件）
│  └─ ohm-law/
│     ├─ a1-experiment.yaml
│     └─ a2-textbook-only.yaml
├─ evidence/                         # 证据（附件与结论分离）
│  ├─ ev-002.csv                     # 可复算的原始数据
│  └─ index.yaml                     # 证据索引（含等级与 as_of）
├─ profiles/                         # 读者画像（默认不公开个体数据）
│  └─ example-junior-exam.yaml
├─ projections/                      # 投影产物（可重新生成，非权威）
│  └─ example-junior-exam.md
├─ schema/                           # schema 自身也是被版本化的内容
│  ├─ claim.schema.json
│  ├─ method.schema.json
│  └─ argument.schema.json
├─ tools/                            # 求值器与校验器（纯本地可跑）
│  ├─ evaluate.py                    # 接地语义求值
│  ├─ validate.py                    # 机械校验
│  └─ project.py                     # 画像投影
└─ .github/
   ├─ ISSUE_TEMPLATE/
   ├─ PULL_REQUEST_TEMPLATE.md
   ├─ workflows/
   └─ DISCUSSION_TEMPLATE/
```

**`tools/` 是关键**：求值器必须是**纯本地可运行**的脚本。这样即使 GitHub 消失，任何一份 clone 都能重算全部结论（不变量 I9 + I10）。

---

## 4. 对象文件格式（完整示例）

### 4.1 命题

`knowledge/physics/ohm-law.yaml`

```yaml
id: kb:physics:ohm-law
type: claim
title: 欧姆定律
statement: 温度不变时，导体中的电流与两端电压成正比，比例常数为电阻
author: { github: alice, did: did:key:z6Mk... }
scope:
  domain: 物理
  stage: 初中
  audience: 全体
  context: { temperature: 恒定 }
evidence:
  - ref: ev-001
  - ref: ev-002
edges:
  requires: [kb:physics:current, kb:physics:voltage, kb:physics:resistance]
  supports: []
  attacks: []
arguments: [arg:ohm-law-a1, arg:ohm-law-a2]
license: CC-BY-SA-4.0

# ▼ 以下字段由 CI 计算并写入，人工 PR 不得修改
derived:
  computed_status: 已确证
  surviving: [arg:ohm-law-a1]
  defeated: [arg:ohm-law-a2]
  computed_at: 2026-09-15T08:00:00Z
  evaluator: tools/evaluate.py@v1
```

`evidence/index.yaml`

```yaml
- ref: ev-001
  kind: 教材
  grade: 低
  source: 《义务教育教科书·物理》九年级全一册，人民教育出版社，2013，P.79
  checkable: true
  as_of: 2013
- ref: ev-002
  kind: 实验数据
  grade: 高
  source: 某导体 U-I 测量数据（本仓库 evidence/ev-002.csv）
  reproducible: true
  as_of: 2026
```

### 4.2 论证

`arguments/ohm-law/a1-experiment.yaml`

```yaml
id: arg:ohm-law-a1
target: kb:physics:ohm-law
claim: 该陈述与可控实验数据一致
grounds:
  - 探针：对同一导体在不同电压下测得电流（evidence/ev-002.csv）
inference: 当温度恒定时，U-I 图像为过原点的直线 ⇒ U ∝ I
evidence: [ev-002]
attacks: []
supports: []
author: { github: bob, did: did:key:z6Mk... }
created: 2026-09-10

# ▼ CI 计算
derived:
  status: 存活
  attacked_by: []
```

### 4.3 教法（注意 `contraindications` 是必填）

`knowledge/physics/method-water-pipe.yaml`

```yaml
id: kb:physics:method-water-pipe
type: method
title: 水管类比讲电流
author: { github: carol, did: did:key:z6Mk... }
scope:
  domain: 物理
  stage: 初中
  audience: 无微积分基础
  context: { class_size: any, device: any, language: 中文 }
body:
  technique: 把电压比作水压、电流比作水流、电阻比作水管粗细
  conditions: { prior_level: 未学微积分, age: 13-16 }
  outcome:
    metric: 后测正确率
    effect_size: 待补
    n: 1 个班（经验证据，等级低）
  contraindications:
    - 对象: 物理系本科生
      理由: 先修过高，类比会固化"电压即水流速度"的错误直觉
      evidence: [ev-010]
evidence: [ev-009, ev-010]
edges:
  requires: [kb:physics:current, kb:physics:voltage]
  exemplifies: [kb:physics:ohm-law]
  attacks: []
license: CC-BY-SA-4.0

derived:
  mode: 并存                     # 教法永不收敛
  applicable_to: [初中, 高职]
  not_applicable_to: [本科物理]
  computed_at: 2026-09-15T08:00:00Z
```

**注意 `derived.mode: 并存`**——教法不进入收敛求值。这是公理 A2 在数据结构上的体现。

### 4.4 路径

```yaml
id: kb:physics:path-junior-electricity
type: path
title: 初中电学 12 讲
sequence:
  - { node: kb:physics:current,  method: kb:physics:method-water-pipe, minutes: 15 }
  - { node: kb:physics:voltage,  method: kb:physics:method-water-pipe, minutes: 15 }
  - { node: kb:physics:ohm-law,  method: kb:physics:method-water-pipe, minutes: 20 }
goal_tags: [中考物理及格]
derived:
  validated: true
  prerequisite_gaps: []          # CI 检出：必须为空
  cycles: []                     # CI 检出：必须为空
  coverage: 0.86
```

---

## 5. 模板

### 5.1 PR 模板

`.github/PULL_REQUEST_TEMPLATE.md`

```markdown
## 改动类型
- [ ] 新增证据（不改结论）
- [ ] 新增 / 修订论证
- [ ] 修订适用范围（scope）
- [ ] 新增知识点（附来源定位）
- [ ] 新增教法（**必须填 contraindications**）

## 我是否修改了 status / derived？
- [ ] 没有（**必须没有**，CI 会检查）

## 证据门槛自检
- [ ] 每条证据都有可核验定位（DOI / ISBN+版次+页码 / 数据 / 脚本）
- [ ] 证据等级已标注
- [ ] 未上传教材原文或扫描页（版权红线）

## 本 PR 改变了什么结论？
<!-- 如果答案是"没有"，也请写清楚，这是完全正常的 PR -->

## 关联
Closes #<issue>
```

### 5.2 Issue 模板

`疑似错误.yml`

```yaml
name: 疑似错误
about: 报告某条知识点可能存在的事实、单位、引用或时效问题
labels: [type:claim, status:待审]
body:
  - 知识点 id（如 kb:physics:ohm-law）
  - 是哪种问题？（数值 / 单位 / 引用 / 过时 / 表述陷阱 / 与指南冲突 / 缺失前提）
  - 你的依据是什么？（可核验定位）
  - 该错误在什么范围、对谁成立？
```

`新增教法.yml`

```yaml
name: 新增教法
about: 提交一种教学做法，必须包含适用条件与禁忌
labels: [type:method]
body:
  - 目标知识点 id
  - 做法描述
  - 适用条件（先修水平 / 年龄段 / 班级规模 / 设备 / 语言）
  - **对谁不适用？理由是什么？**（必填）
  - 证据（课堂经验也是合法证据，请标注样本量）
```

`先修关系争议.yml`

```yaml
name: 先修关系争议
about: 质疑某条"必须先学 A 才能学 B"的断言
labels: [type:path]
body:
  - 涉及的先修边
  - 你认为可以跳过 / 必须加强的理由
  - 支持你的证据（学习数据优先）
```

---

## 6. 标签体系

| 维度 | 标签 |
|---|---|
| 类型 | `type:claim` `type:method` `type:path` `type:misconception` `type:resource` |
| 状态 | `status:草案` `status:待审` `status:争议` `status:已确证` `status:已推翻` `status:需复审` `status:已失效` |
| 错误类型 | `error:数值` `error:单位` `error:引用` `error:过时` `error:表述陷阱` `error:与指南冲突` `error:缺失前提` |
| 闸门 | `gate:证据不足` `gate:门槛未过` |
| AI | `ai:红队` `ai:待人工` `ai:输出已署名` |
| 学科 | `domain:物理` `domain:数学` `domain:计算机` … |

**没有 `votes:` 这类标签。** 需要新标签表达"人气"时，说明设计已经跑偏了。

---

## 7. GitHub Actions 工作流

| 工作流 | 触发 | 作用 | 需要 LLM 密钥 |
|---|---|---|---|
| `guard-status.yml` | PR | 检测是否手改 `status` / `derived` → **失败** | 否 |
| `validate.yml` | PR | schema、引用格式、**先修环**、**先修缺口**、单位一致性、锚点可定位、版权扫描（是否混入长段原文） | 否 |
| `evaluate.yml` | PR | 跑 `tools/evaluate.py`：接地语义求值，把 `derived` 写回并提交到 PR 分支 | 否 |
| `ai-triage.yml` | PR 打开 | AI 审阅：证据是否真的支持主张、有无被忽略的邻近证据、门槛是否达标 → **评论** | 是 |
| `ai-redteam.yml` | PR 打开 | AI **尝试构造最强反驳**，以 `arguments/` 文件形式提交到 PR 分支（署名，仅作为一条证据） | 是 |
| `ai-extract.yml` | 手动 / 定时 | 从公开来源抽取候选知识点与先修边 → **开 Issue**，绝不直接改文件 | 是 |
| `recheck.yml` | scheduled（每周） | 扫描 `as_of` 过期证据 → 开复审 Issue + 状态降级为 `需复审` | 否 |
| `mirror.yml` | scheduled（每日） | 推送到 GitLab / Gitea 镜像，并生成可独立验证的归档 | 否 |

### 7.1 分支保护（护栏的核心）

`main` 分支必须开启：

- ✅ 必须通过 `guard-status` + `validate` + `evaluate`（required status checks）
- ✅ 需要 `CODEOWNERS` 中对应领域的 review
- ✅ **Do not allow bypassing the above settings**（管理员也不能绕）
- ✅ 禁止 force push、禁止删除分支
- ✅ 建议开启签名提交

这三条勾上之后，"规则即代码、立法与执行分离"（公理 A4）才算真正落地。**否则前面所有设计都是君子协定。**

### 7.2 AI 输出的强制格式

AI 的每条评论必须包含：

```markdown
> 🤖 AI 辅助 · 非裁决
> model: <模型标识> | version: <版本> | prompt_hash: <哈希> | at: <时间>
> 本输出仅作为**一条证据**参与，不计入最高证据等级，不构成批准。

### 我检查了什么
### 我发现的问题（附可核验定位）
### 我不确定的地方
### 建议动作（给人决策，不做决定）
```

**AI 禁止**：approve PR、修改 `status` / `derived`、匿名发言、在无来源时断言事实。

**降级**：没有 LLM 密钥时，`validate` / `evaluate` / `recheck` 照常工作，AI 环节静默跳过——**系统的完整性不依赖 AI**。

---

## 8. AI 辅助在 GitHub 上的四个具体动作

| 动作 | 落点 | 价值 |
|---|---|---|
| **分诊** | PR 评论 | 把 300 条讨论压成一张论证图，人只看结论 |
| **红队** | 以论证文件提交 | 主动把每个主张打一遍，打不掉的才进入评审——大幅提高灌水成本 |
| **机械核算** | Actions 日志 | 数值复算、单位/量纲、引用是否存在、页码是否对——**这部分不需要讨论** |
| **抽取** | 开 Issue | 从教材目录与公开来源抽取候选知识点与先修边，解决录入量问题 |

**注意红队的落点**：AI 构造的反驳必须**作为一个正常的论证文件**进入 PR，走和其他人完全一样的通道。**AI 没有特权通道**，这是它不变成新权威的前提。

---

## 9. 去中心化的诚实说明

GitHub 提供的是三层中的一部分：

| 层次 | GitHub 是否提供 | 说明 |
|---|---|---|
| **协作去中心化** | ✅ | 无中心编辑、分叉权、历史可验证、无单一作者 |
| **数据可验证** | ✅ | git 对象哈希 = 内容寻址，历史不可篡改 |
| **平台中心化** | ⚠️ | 账号可封、仓库可下架、Actions 依赖平台 |
| **网络去中心化** | ❌ | 无 P2P 复制，仍依赖中心服务器 |

**所以必须配三件套，否则"去中心化"是话术：**

1. **寻址不依赖平台**：所有标识用内容哈希 / 稳定 slug，不用 GitHub 的 URL 或 ID。仓库搬走，标识不变。
2. **多平台镜像 + 本地 clone**：`mirror.yml` 每日推 GitLab / Gitea。任何一份 clone 都是完整副本。
3. **结论可独立复算**：`tools/` 是纯本地脚本，归档里带上证据快照与求值器。**脱离 GitHub 也能重算出全部结论**（不变量 I9 + I10）。

做到这三点，即使 GitHub 明天关站：任何持有 clone 的人都能完整重建知识库、重算全部结论、继续在别的平台上协作。**这才是"用 GitHub 实现去中心化"的准确含义。**

---

## 10. M0 落地清单

| # | 事项 | 产出 |
|---|---|---|
| 1 | 建仓库 + 目录骨架（§3） | 空结构 + README |
| 2 | 写 `schema/*.json` | 四类对象 + 论证的 schema |
| 3 | 写 `tools/validate.py` | 机械校验可跑（先修环 / 缺口 / 单位 / 引用格式） |
| 4 | 写 `tools/evaluate.py` | 接地语义求值可跑，输出 `derived` |
| 5 | 配 `guard-status` + `validate` + `evaluate` 三个 workflow | CI 能阻止非法改动 |
| 6 | 开分支保护（含 Do not allow bypassing） | 规则不可绕过 |
| 7 | 建 Issue 模板 ×3、PR 模板 ×1、Discussions 分类 ×5 | 通道分工生效 |
| 8 | 选一本**开源教材**，抽取 ≥200 条知识点 | 首批数据 |
| 9 | 跑机械校验，产出错误候选清单 | **第一条真实产出**（不下"对错"结论） |
| 10 | 接 `ai-triage` + `ai-redteam`（有密钥才启用） | AI 辅助上线 |

**M0 的验收标准**：任何人都能 `git clone` 后在**断网**状态下跑出同一份错误候选清单。

**试点学科建议**：数学 / 计算机 / 物理（对错可被程序判定），**不要从医学起步**。找一本已有官方勘误表的教材当基准，用来测系统准确率。

---

## 11. 未决问题

1. **收敛器**：纯规则 / 规则 + 领域编辑 / 规则 + 轮值裁决
2. AI 密钥由谁持有？如何避免 AI 环节成为新的单点
3. 镜像目标的运营成本与频率
4. 试点学科与首本教材最终选哪个
5. `derived` 写回 PR 分支的实现方式（bot 提交 vs Actions 内提交）
