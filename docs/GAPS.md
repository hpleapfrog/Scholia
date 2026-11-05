# 缺口总览

> **这一页是生成物。** 表格与清单由 [`tools/gaps.py`](../tools/gaps.py) 计算、
> [`tools/kbcheck.py`](../tools/kbcheck.py) 写入；运行 `python tools/kbcheck.py --write-index`
> 时重写。**手改会被校验判失败**（`R-INDEX-02`）。
>
> English → [GAPS.en.md](GAPS.en.md)

## 这一页回答什么

「这个库还缺什么，我先做哪一件。」

它只列**机器数得出来**的缺口。把机器算不出来的也混进来，会让这张表看起来比实际更权威——
而这个库的第一条规矩就是**不假装知道**。所以每一行都写清了「为什么算缺口」，
下面另有一张「机器不算的那一半」。

<!-- kbcheck:begin -->
**746** 条对象 · **744** 条可作事实引用 · **2** 条不可引用 · **188** 条证据 · **2** 条事件
**已确证 526** · 暂定确认 43 · 有效 157 · 待审 15
**17** 条路径 · **73** 个学习成果全部有环节覆盖 · **67** 个（92%）只讲一次
T4 733 · T3 5 · T2 8 —— 溯源档（**取最弱一环**，与「已确证」正交）

| 缺口 | 数量 | 为什么算缺口 |
|---|---|---|
| **三分钟复核** | 12 | 状态是「待审」，论证已写、证据也读过了 —— 只差**一次复核**。复核者可以是人（署名），也可以是 agent（留四栏 `## 复核记录`），两者都写 `已确证`。 |
| **待审，但复核还开不了口** | 3 | 状态是「待审」，但引用的证据至少有一条只到 `仅定位`/`未核验`（或论证还没写、没引用证据）—— 复核者打开来源也无从判断。这是「复核」的**前置条件**，不是另一种复核。 |
| **溯源档没到 T4 的条目** | 13 | 引用的来源里**最弱的一份**没有读到全文（`T3` 摘要 / `T2` 仅定位 / `T1` 未核验 / `T0` 无据）。这不是「内容可能不对」，是「顺着它核到底会撞上没读过的地方」。 |
| **补英文译本** | 0 | 没有 `path_en`：英文读者点进来会落到中文页。 |
| **缺教法的知识点** | 37 | 知识点回答「是什么」，教法回答「怎么讲」。覆盖度页只数前者，所以这一栏在别处看不见。 |
| **库外前置：该建节点了吗** | 2 | 同一个 `外部先修` 标识出现在 ≥2 个对象里 —— 它在多条链路前面反复出现。 |
| **路径成果只有一处覆盖** | 17 | 某个学习成果只被一个环节覆盖：那一处讲砸，学生就没有第二次机会。 |
| **路径覆盖的证据没读过** | 0 | 覆盖该成果的条目，证据最高只到 `仅定位`/`未核验` —— 位置排上了，依据还没读。 |
| **条目自己写下的「待补」** | 110 | 作者在正文里留了 `**待补**：` —— 这是条目自己承认的缺口，不是外部推测。 |
| **物理覆盖度仍为 🔴 的章** | 2 | 对照人教版目录，整章在本库没有任何知识点。 |

> **同一个对象可能同时出现在几行里，别把数量相加**。
> **唯一不重叠的一对：**三分钟复核 12 + 复核前置 3 = 全部 `待审` 条目（15）。

### 三分钟复核（12）

> 人或 agent 复核一条（agent 用 `tools/review_packet.py` + `tools/quote_check.py`，写完 `## 机审记录`）。按下游依赖数排序。

- `kb:physics:self-and-mutual-inductance` · 自感与互感 — 2 条别的条目先修它
- `kb:physics:electric-work-and-joule-law` · 电功与焦耳定律 — 1 条别的条目先修它
- `kb:physics:analogy-stage-attribution-invalid` · n=2 无法在多个同样变化的变量之间做归因
- `kb:physics:ionizing-radiation-in-medicine` · 医学中的电离辐射
- `kb:physics:charged-particle-in-electric-field` · 带电粒子在电场中的运动
- `kb:physics:reactance-and-impedance` · 感抗与容抗
- `kb:physics:eddy-currents-and-motional-emf` · 涡流与动生电动势
- `kb:physics:energy-resources-and-sustainability` · 能源与可持续发展
- `kb:life:prop-oversale-volunteer-first` · 超售时，未经征集自愿者程序不得拒绝旅客登机
- `kb:physics:velocity-time-graph-area` · 速度—时间图的面积等于位移
- …还有 2 项 —— 完整清单：`python tools/make_tasks.py --json`

### 待审，但复核还开不了口（3）

> 打开该证据的定位，读完并把 `核验深度` 改成 `摘要`/`全文`；或换一份已读过的来源。

- `kb:life:prop-carried-item-limits` · 北京地铁对乘客携带物品设有硬性尺寸与重量上限 —— 证据未读：`ev-043`
- `kb:physics:ohm-law-scope-placement` · 欧姆定律局限性的呈现位置差异 —— 证据未读：`ev-001`
- `kb:physics:voltage-symbol-u-v` · 电压符号 U 与 V 的中英文教材差异 —— 证据未读：`ev-001`

### 溯源档没到 T4 的条目（13）

> 打开那条证据的定位读一遍，把 `核验深度` 提到 `全文`；或换一条已读过的来源。

- `kb:med:prop-hypertension-cn-2024` · 中国高血压防治指南（2024年修订版）规定：诊室血压 ≥140/90 mmHg 诊断高血压，一般患者降至 <140/90、可耐受者再降至 <130/80 mmHg —— T2，最弱：`ev-070`, `ev-074`, `ev-077`, `ev-078`
- `kb:med:prop-copd-gold-2026` · GOLD 2026 规定支气管舒张后 FEV1/FVC < 0.7 确诊慢阻肺，并把「上一年 ≥1 次中重度急性加重」作为 E 组与治疗升级的阈值 —— T2，最弱：`ev-074`, `ev-075`, `ev-079`
- `kb:physics:resource-phet-forces-and-motion-basics` · PhET 模拟「力与运动：基础」 —— T2，最弱：`ev-029`
- `kb:physics:resource-phet-my-solar-system` · PhET 模拟「我的太阳系」 —— T2，最弱：`ev-032`
- `kb:life:resource-bj-subway-passenger-rules` · 《北京市轨道交通乘客守则》（官方文件） —— T2，最弱：`ev-043`
- `kb:life:prop-carried-item-limits` · 北京地铁对乘客携带物品设有硬性尺寸与重量上限 —— T2，最弱：`ev-043`
- `kb:physics:ohm-law-scope-placement` · 欧姆定律局限性的呈现位置差异 —— T2，最弱：`ev-001`
- `kb:physics:voltage-symbol-u-v` · 电压符号 U 与 V 的中英文教材差异 —— T2，最弱：`ev-001`
- `kb:med:prop-plague-treat-on-suspicion` · 对疑似鼠疫，WHO/CDC 指南规定不等确诊即开始治疗，并明确用药、隔离与接触者预防的时限 —— T3，最弱：`ev-071`, `ev-072`, `ev-073`
- `kb:med:prop-ardsnet-low-tidal-volume` · 对 ARDS 患者，低潮气量通气降低死亡率 —— T3，最弱：`ev-048`
- …还有 3 项 —— 完整清单：`python tools/make_tasks.py --json`

### 缺教法的知识点（37）

> 从教材里找有标记的课堂做法（[BL]/[OL]/[AL]），新建「教法」条目并挂 `knowledge_point`。

- `kb:physics:alternating-current` · 交变电流
- `kb:physics:polarization` · 光的偏振
- `kb:physics:light-interference-and-diffraction` · 光的干涉与衍射
- `kb:physics:total-internal-reflection` · 全反射
- `kb:physics:kp-torque` · 力矩
- `kb:physics:ionizing-radiation-in-medicine` · 医学中的电离辐射
- `kb:physics:simple-pendulum` · 单摆
- `kb:physics:transformer` · 变压器
- `kb:physics:ampere-force` · 安培力
- `kb:physics:charged-particle-in-electric-field` · 带电粒子在电场中的运动
- …还有 27 项 —— 完整清单：`python tools/make_tasks.py --json`

### 库外前置：该建节点了吗（2）

> 先判断这条前置是否真实必需（M-12）；决定建节点后，把各条目的声明迁到 `edges.先修`。

- `angle`（几何中的角）—— 4 个对象
- `vector`（矢量 / 矢量与矢量加法）—— 2 个对象

### 路径成果只有一处覆盖（17）

> 给这些成果补第二个环节（换一种讲法 / 换一个入口），或把它拆成更小的成果。

- 静电学入门（高中） —— o1、o2、o3、o4、o5、o6、o7
- 电路入门（高中） —— o1、o2、o3、o4、o5、o6
- 交变电流（高中） —— o1、o2、o3、o4、o5
- 原子核与辐射（高中） —— o1、o2、o3、o4、o5
- 机械振动（高中） —— o1、o2、o3、o4、o5
- 磁场与电磁感应（高中） —— o1、o2、o3、o5、o7
- 功、功率与机械能（高中） —— o1、o2、o3、o4
- 动量与碰撞（高中） —— o1、o2、o3、o4
- 热学（高中） —— o1、o2、o3、o4
- 量子与原子（高中） —— o1、o2、o3、o4
- …还有 7 项 —— 完整清单：`python tools/make_tasks.py --json`

### 条目自己写下的「待补」（110）

> 按正文里那句话补内容；补完删掉标记。

- `kb:computing:prop-http-1xx-interim-responses` · HTTP 1xx 是临时响应：不得发给 HTTP/1.0 客户端，不能含正文或 trailer，… —— **待补**：§10.1.1（Expect）与 §7.8（Upgrade）的核读；主流代理转发 1xx 的实测
- `kb:computing:prop-http-202-no-async-status-resend` · HTTP 202 不承诺请求终会被处理，且 HTTP 无法事后补发最终状态码 —— **待补**：RFC 7231 §6.3.3 的对照；主流任务 API 的 202 + 轮询模式实测（只登记模式，不评优劣）
- `kb:computing:prop-http-204-cannot-contain-content-or-trailers` · HTTP 204 响应不能含正文也不能含 trailer，且默认可缓存 —— **待补**：RFC 7230–7235 对 204 的表述；主流客户端对 204 缓存行为的实测
- `kb:computing:prop-http-205-reset-document-view-no-content` · HTTP 205 要求重置「文档视图」，且服务器不得生成正文 —— **待补**：RFC 7231 §6.3.6 的对照；主流浏览器对 205 重置行为的实测
- `kb:computing:prop-http-206-partial-content-header-duties` · HTTP 206 的 Content-Length 不是完整资源长度（全量在 Content-R… —— **待补**：§14.2 / §14.6（Range 与 multipart/byteranges）的核读；主流 CDN 与静态服务器 206 头实测
- `kb:computing:prop-http-301-302-post-to-get-is-historical-307-forbids-method-change` · HTTP 301/302 把 POST 改成 GET 是「历史原因」下的 MAY，规范要求保留方… —— **待补**：[CACHING] §4.2.2 的可缓存状态码清单；RFC 7230–7235 对 301/302/303 的表述；「历史原因」的具体所指
- `kb:computing:prop-http-304-must-carry-cache-headers-and-no-body` · HTTP 304 响应必须带上原 200 会发的缓存头部，且不能含正文或 trailer —— **待补**：[CACHING] §4.3.4；RFC 7230–7235 对 304 的表述；主流服务端 304 响应带 `ETag` 的实测
- `kb:computing:prop-http-400-vs-422-syntax-vs-semantics` · HTTP 400 是语法或路由层面的客户端错误，422 是语法正确但语义无法处理 —— **待补**：[RFC 4918]；RFC 7230–7235 对 400 的表述；主流 API 用 400 还是 422 的实测
- `kb:computing:prop-http-401-vs-403-must-carry-www-authenticate` · HTTP 401 必须带 WWW-Authenticate 头部，且 401 与 403 的分工… —— **待补**：RFC 9110 §11.6.1；RFC 7230–7235 对 401/403 的表述；主流框架 401 响应是否带 `WWW-Authenticate` 的实测
- `kb:computing:prop-http-reserved-deprecated-codes` · HTTP 402「保留待用」、305 已废弃、306 保留不用：三个有名无实的状态码 —— **待补**：RFC 7231 Appendix B（305 旧语义）的核读；402 的启用状态（以注册表最新版为准）
- …还有 100 项 —— 完整清单：`python tools/make_tasks.py --json`

### 物理覆盖度仍为 🔴 的章（2）

> 先采集该章的核心概念，再写知识点；覆盖度页会随条目自动更新。

- 1 分子动理论
- 2 气体、固体和液体
<!-- kbcheck:end -->

## 复核一条：3 分钟，三个「是 / 否」

| # | 问题 | 什么算「否」 |
|---|---|---|
| 1 | 它引用的来源，你打得开吗？ | 404 / 链接失效 / 要付费看不到 |
| 2 | 那一页上，真的有这句话吗？ | 措辞不同、意思更宽、原文根本没这句 |
| 3 | 它的结论有没有超出那一页？ | 原文限定人群 / 版本 / 条件，条目写成普遍成立 |

> **三个问题只问「原文有没有这么说」，不问「这个结论对不对」。**
> 用 [`.github/ISSUE_TEMPLATE/复核一条.yml`](../.github/ISSUE_TEMPLATE/复核一条.yml) 提交；
> 答完三个「是」，条目就能从 `待审` 变成 `暂定确认`——**要求非作者复核**，
> 所以 AI 不能替你答这三个问题（`M-07`）。

## 机器不算的那一半

| 问题 | 谁判 | 记在哪 |
|---|---|---|
| 这条论证站不站得住 | 人（`M-07`；AI 只能当攻击方） | 条目的 `## 论证` |
| 这条前置是否真的必需 | 人（`M-12`） | `外部先修` 声明 |
| 教法在真实课堂有没有效 | 人（`M-04`） | 教法的 `禁忌` / `风险` |
| 两个来源是否真的独立 | 人（`M-03`） | `支持` 边的证据构成 |
| 路径在教学上够不够 | 人 | 路径的 `## 自检` |
| 这条内容值不值得写 | 人 | 选题 |

## 怎么用这一页

| 你想 | 用 |
|---|---|
| 马上开工 | `python tools/make_tasks.py --limit 3`（加 `--gh` 直接建 Issue） |
| 要完整清单 / 喂给脚本 | `python tools/make_tasks.py --json` |
| 要复核一条，但不想自己找材料 | `python tools/review_packet.py --id <id>` —— **只排版，不替你回答**那三个问题 |
| 让 agent 自己决定下一步 | MCP 工具 `scholia_gaps` —— 同一个 `compute()`，不必整读索引 |
| 确认这些工具没坏 | `python tools/selftest.py` —— MCP 握手 + 9 个工具 + `--json` + 骨架生成 + 复核包 |
| 看规则本身 | [RULES.md](RULES.md) |
