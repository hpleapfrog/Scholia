# 证据索引

全库共享。每条知识点的 `front-matter` 用编号引用这里的条目。

## 门槛

**讨论可以随便说，但只有过门槛的证据进入判定。**

必须提供可核验定位：ISBN + 版次 + 页码 / DOI / 官方文档条款 / 公开数据集 / 可复算的脚本与数据。

> [!CAUTION]
> **绝不上传教材原文或扫描页。**
> 只存页码定位、短引用、原创摘要与结论。事实与数据不受版权保护，**表达**受版权保护。

## 本库自己犯过的一次：把**构造的数据**登记成「实验数据」

> [!CAUTION]
> **`ev-002` 已作废。** 它曾是本库**等级最高**的一条证据，而**从来没有发生过任何测量**。

| | ev-002 原样 | 实际 |
|---|---|---|
| 类型 | **实验数据** | **本库作者构造** |
| 等级 | **高** | —— |
| 定位 | `导体U-I数据.csv`（可复算） | 数值为 `U = 10 × I`，**R 精确等于 10.000** |
| 时间 | 2026 | 同一年，同一位作者 |
| 引用它的条目写 | 「对同一导体在不同电压下**测得**电流，**温度 20 °C**」 | **没有测量、没有控温、CSV 里连温度列都没有** |

它当时是用来**替换**更早那批虚构示例（`ev-009`~`ev-012`）的。
**结果换上去的是同一类东西，只是包装得更像证据。**

### 为什么它骗过了所有人（包括一次对抗审查）

一次 AI 对抗审查确实审过引用它的命题，并**准确地**指出：

> 数据分辨率不足——电流只记到 `0.01 A`，在 `I=0.10` 处就是 **5%**，
> 因此**无法区分**「欧姆」与「4.4% 漂移」。

**那是症状，不是根因。** 根因是**这份数据根本不是测量**。

> [!IMPORTANT]
> **而对抗审查没去查这件事，是因为本库要求它不要查。**
>
> 派发对抗任务时写的指令是：
> **「你不需要验证引用是否属实（那要联网），可以假定引用属实；
> 你要攻击的是『即便如此，结论成立吗』。」**
>
> **是我自己把「核实证据是否真实存在」排除在对抗范围之外的。**

**修正（已写进 `FORMAT.md` §6）**：对抗审查的任务里必须**显式包含**一句
**「质疑证据是否如其所述地存在」**。逻辑攻击与真实性核验**不是同一件事**，
不能因为前者成本低就省掉后者。

### 由此立下的两条规矩

| # | 规矩 |
|---|---|
| 1 | **本库自产的数据必须写明「构造」还是「实测」。** 「实验数据」四个字等于声称发生了一次测量——**没有测量就没有这句话** |
| 2 | **定量证据必须登记有效位数 / 不确定度 / 重复次数。** 没有它们，该证据**只能支撑到它自己声明的精度**；结论所需精度若优于数据精度，**该证据只能算「示意」，不算证据** |

> **删掉痕迹才是真的丢信息**——`ev-002` 编号保留，文件改名为
> [`构造数据-欧姆定律演示.csv`](构造数据-欧姆定律演示.csv)（它的**示范价值**还在：
> 它确实展示了欧姆关系长什么样，**只是不能支撑任何关于真实世界的命题**）。

## 索引

| 编号 | 类型 | 等级 | 定位 | 时间 | 许可 | 引用处 |
|---|---|---|---|---|---|---|
| ev-001 | 教材 | 低 | 《义务教育教科书·物理》九年级全一册，人教版，2013，P.79 | 2013 | 外部来源 · 仅引用定位 | 欧姆定律 · 电压符号差异 |
| ev-002 | ⚠️ **已作废** | — | 原登记为「实验数据」的 `导体U-I数据.csv`。**从未有任何测量发生**——数值由本库作者构造（`U = 10 × I`，R 精确等于 10.000） | — | — | 引用它的条目已重写 |
| ev-009 | ⚠️ **已作废** | — | 本库**构造的示例数据**（「某校初三 2 个班对照观察」），**从未真实存在** | — | — | 无（原引用条目已重写） |
| ev-010 | ⚠️ **已作废** | — | 本库**构造的示例数据**（「本科物理课观察」），**从未真实存在** | — | — | 无（原引用条目已重写） |
| ev-011 | ⚠️ **已作废** | — | 本库**构造的示例数据**（「初三学完后测」），**从未真实存在** | — | — | 无（原引用条目已删除） |
| ev-012 | ⚠️ **已作废** | — | 本库**构造的示例数据**（「高中生测评」），**从未真实存在** | — | — | 无（原引用条目已删除） |
| ev-014 | **出版社勘误表** | **高** | OUP《高中活學地理（第三版）》勘誤表，重印兼訂正 2024，[PDF](https://eresources.oupchina.com.hk/debundling/corrigenda/ssgeog3e_re_corrigenda_core_c_2024.pdf) | 2024 | 外部来源 · 仅引用定位 | 地理勘误 ×6 |
| ev-015 | **出版社勘误表** | **高** | 雅集《科學新世紀 1A》勘誤表，[ZIP](https://e-aristo.hk/t/downloads/science/scicent_amendments_2024_c.zip) | 2024 | 外部来源 · 仅引用定位 | 科学勘误 ×1 |
| ev-016 | 教材（全文） | 低 | OpenStax《College Physics 2e》§20.3 Ohm's Law: Resistance and Simple Circuits，[m42344](https://raw.githubusercontent.com/openstax/osbooks-college-physics-bundle/main/modules/m42344/index.cnxml) | 2020 | **CC BY-NC-SA 4.0** · 仅引用定位与短引用 | 摩擦类比 · 局限性位置 · 电压符号差异 |
| ev-017 | 教材（全文） | 低 | OpenStax《College Physics 2e》§20.1 Current，[m42341](https://raw.githubusercontent.com/openstax/osbooks-college-physics-bundle/main/modules/m42341/index.cnxml) | 2020 | **CC BY-NC-SA 4.0** · 仅引用定位与短引用 | 电流（备用） |
| ev-018 | 教材（全文） | 低 | OpenStax《Physics》§19.2 Ohm's law，[m54437](https://github.com/openstax/osbooks-physics/blob/main/modules/m54437/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 欧姆定律 · 水管类比 · 电流方向误解 · 类比选择与学段相关 |
| ev-019 | 教材（全文） | 低 | OpenStax《Physics》§19.3 Series Circuits，[m54435](https://github.com/openstax/osbooks-physics/blob/main/modules/m54435/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 水管类比（做法与禁忌） |
| ev-020 | 教材（全文）**+ 可复算脚本与明细** | 低 | OpenStax《Physics》**全 23 章 / 98 模块**的 Teacher Support。**脚本** [`os-teacher-markers.py`](os-teacher-markers.py) · **明细** [`os-teacher-markers.csv`](os-teacher-markers.csv) · ref `main` **commit `dfdfd7a5356ecdd42e504de3df50d9153e33ea49`** | 2020 | **CC BY 4.0** · **可自由复用** | 教材内建分组教学变体 |

> [!CAUTION]
> **ev-020 原先只写「580 条，含 649 个分组标记」，而库里既无脚本也无数据**——
> 那一栏因此被一次对抗审查击中（[攻击条目](../knowledge/物理/命题/攻击-教材内建分组教学变体.md) 的 `A4`）。
>
> **现已补上脚本 + 明细 + commit 哈希。** 现行数字：
>
> | 口径 | `os-teacher` 便签 | BL | OL | AL | EL | 合计 |
> |---|---|---|---|---|---|---|
> | **宽松**（note 里任意出现） | **582** | 207 | 245 | 191 | **5** | **648** |
> | 严格（`<para>` 开头的 `<span>`） | — | 205 | 243 | 189 | 0 | 637 |
>
> **旧声称的 649 / 580 两者都不是**——它是**某次 `main` 的快照**。
> 差的 `EL`(6→5)、合计(649→648)、便签(580→582) 来自 **`main` 前移**。
>
> **教训：写死一个会漂移的数字，等于把它变成断言。** 数字要连同**规则 + commit** 一起给。
| ev-021 | 教材（全文） | 低 | OpenStax《Physics》§2.1 Relative Motion, Distance, and Displacement，[m54108](https://github.com/openstax/osbooks-physics/blob/main/modules/m54108/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 参考系教法 ×3 · 参考系误解 |
| ev-022 | 教材（全文） | 低 | OpenStax《Physics》§2.2 Speed and Velocity，[m54104](https://github.com/openstax/osbooks-physics/blob/main/modules/m54104/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 速度与速率教法 ×2 |
| ev-023 | 教材（全文） | 低 | OpenStax《Physics》§2.3 Position vs. Time Graphs，[m54110](https://github.com/openstax/osbooks-physics/blob/main/modules/m54110/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 位置-时间图教法 ×2 |
| ev-024 | 教材（全文） | 低 | Utah State Board of Education《7th Grade Science》（SEEd 标准），[PDF](https://www.uen.org/emedia/resources/oer/7thGradeSEEd.pdf)，148 页 | 2020 | **CC BY-NC-SA 3.0** · **仅引用定位与短语** | 力与运动（初中）· 现象探究循环 |
| ev-025 | 教材（全文） | 低 | OpenStax《Physics》§4.2 Newton's First Law of Motion: Inertia，[m54138](https://github.com/openstax/osbooks-physics/blob/main/modules/m54138/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 惯性 · 惯性教法 ×2 · 运动物体自然慢下来 |
| ev-026 | 教材（全文） | 低 | OpenStax《Physics》§16.1 Reflection，[m54357](https://github.com/openstax/osbooks-physics/blob/main/modules/m54357/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 光的反射 · 反射教法 ×2 |
| ev-027 | 教材（全文） | 低 | OpenStax《Physics》§14.1 Speed of Sound, Frequency, and Wavelength，[m54331](https://github.com/openstax/osbooks-physics/blob/main/modules/m54331/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 声速与频率 · 声速教法 ×2 |
| ev-028 | 教材（全文） | 低 | OpenStax《Physics》§9.2 Mechanical Energy and Conservation of Energy，[m54273](https://github.com/openstax/osbooks-physics/blob/main/modules/m54273/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 机械能守恒 · 机械能教法 ×2 · 运动物体自然慢下来 |
| ev-029 | **交互式模拟（读产物头部）** | 低 | PhET「Forces and Motion: Basics」，[直达链接](https://phet.colorado.edu/sims/html/forces-and-motion-basics/latest/forces-and-motion-basics_en.html)；教材内入口为 OpenStax 短链 `openstax.org/l/forcesandmotion`（实测解析到该直达链接） | 2026 | **CC BY-NC 4.0** · **仅引用定位** | PhET 力与运动基础（本库第一条 `资源`） |
| ev-030 | 教材（全文） | 低 | OpenStax《Physics》§15.1 The Electromagnetic Spectrum，[m54342](https://github.com/openstax/osbooks-physics/blob/main/modules/m54342/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 电磁波谱 · 电磁波谱教法 ×2 · 可见光误解 |
| ev-031 | 教材（全文） | 低 | OpenStax《Physics》§7.2 Kepler's Laws of Planetary Motion，[m54192](https://github.com/openstax/osbooks-physics/blob/main/modules/m54192/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 开普勒定律 · 开普勒教法 ×2 |
| ev-032 | **交互式模拟（读产物头部）** | 低 | PhET「My Solar System」，[直达链接](https://phet.colorado.edu/sims/html/my-solar-system/latest/my-solar-system_en.html)；教材内入口为 OpenStax 短链 `openstax.org/l/28mysolar` | 2026 | **CC BY-NC 4.0** · **仅引用定位** | PhET 我的太阳系（第二条 `资源`） |
| ev-033 | 教材（全文） | 低 | OpenStax《Physics》§13.1 Types of Waves，[m54314](https://github.com/openstax/osbooks-physics/blob/main/modules/m54314/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 波（知识点）· 波教法 BL · 波把物质一起推走 |
| ev-034 | 教材（全文） | 低 | OpenStax《Physics》§13.2 Wave Properties: Speed, Amplitude, Frequency, and Period，[m54321](https://github.com/openstax/osbooks-physics/blob/main/modules/m54321/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 波（知识点）· 波教法 OL |
| ev-035 | 教材（全文） | 低 | OpenStax《Physics》§22.1 The Structure of the Atom，[m54582](https://github.com/openstax/osbooks-physics/blob/main/modules/m54582/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 原子结构 · 原子结构教法 ×3 |
| ev-036 | 教材（全文） | 低 | OpenStax《Physics》§9.1 Work, Power, and the Work–Energy Theorem，[m54271](https://github.com/openstax/osbooks-physics/blob/main/modules/m54271/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 功与功率 · 功与功率教法 ×2 |

> [!CAUTION]
> **`ev-009` ~ `ev-012` 已作废。** 它们是本库早期为了演示格式而**构造的示例数据**，
> 描述中的课堂观察与测评从未发生过。
>
> 编号**不回收**（保留痕迹），但**不得再被任何条目引用**。
> 引用它们的 3 个条目已于 2026-10-05 全部重写或删除。

> [!NOTE]
> **编号不连续是有意的。** `ev-xxx` 一旦分配就不再改变——删掉条目也不会回收编号，
> 因为已有条目引用过它。这跟 `id` 字段同一个道理。

> [!IMPORTANT]
> **引用外部来源时，必须遵守其原始许可协议。**
> 本库只存**定位、短引用、原创摘要与结论**，不复制受版权保护的表达。

## 等级说明

| 断言类型 | 等级阶梯（高 → 低） |
|---|---|
| 命题 | 系统综述 / 元分析 > 随机对照 > 队列 > 病例 > 专家意见 > **教材本身** |
| 教法 | 可复现的课堂实验 > 准实验 > 大样本课堂数据 > 单一课堂经验 > 专家直觉 |

> [!IMPORTANT]
> **教材在命题的证据金字塔里等级很低**，但学生把它当最高权威。
> 这正是本项目存在的理由。
>
> 同时，**单一课堂经验在教法里是合法证据**——教法条件性强、迁移性差，
> 把医学标准硬套过来会把有效的本土经验全部滤掉。

### 一个真实的不对称：初中级开放教材几乎都是 NC

采集时发现的规律，记录在此以免重复踩：

| 学段 | 来源 | 许可 |
|---|---|---|
| **高中** | OpenStax《Physics》（`osbooks-physics`） | **CC BY 4.0** ✅ 可自由复用 |
| **初中** | Utah State Board of Education 6 / 7 / 8 年级科学 | **CC BY-NC-SA 3.0** ❌ 仅可引用 |
| 初中（上游） | CK-12 Foundation（Utah 教材的内容来源） | **CC BY-NC** ❌ 仅可引用 |

> [!WARNING]
> **高中级能自由复用，初中级只能引用。**
>
> 美国中学 OER 大量基于 CK-12，而 CK-12 是 **NC**。
> 所以「扩充到初中知识点」在许可上比高中**更受限**——
> 条目只能写**我们自己的摘要 + 短语级引用**，不能搬用教材表述。

### 另一类限制：初中教材多没有教学指导

| 来源 | 有结构化教学指导吗 |
|---|---|
| OpenStax《Physics》 | ✅ **580 条 Teacher Support**，含 649 个分组标记 |
| Utah 7 年级 | ❌ 学生用书，**没有** Teacher Support / misconception 标注 |

**含义**：初中源能提供**知识内容与学段边界**（如"矢量推迟到高中"），
但**提供不了分档教法**。初中级的 `教法` 需要另找来源，或由教师贡献。

### 一个真实的许可陷阱：许可不随教材传播

OpenStax 教材正文里**内嵌 PhET 模拟**（`<iframe>` + OpenStax 短链，
外层 `<media class="os-embed">` 带一段描述）。

实测结果（读**模拟产物自身的头部**，权威来源）：

| 层 | 内容 | 许可 |
|---|---|---|
| 教材 | OpenStax《Physics》 | **CC BY 4.0** ✅ |
| 教材内嵌的模拟 | PhET「Forces and Motion: Basics」 | **CC BY-NC 4.0** ❌ |
| 抽查的另外三个模拟 | my-solar-system / bending-light / color-vision | **CC BY-NC 4.0** ❌ |

> [!CAUTION]
> **「教材可以自由复用」不能推出「教材里嵌的东西也可以」。**
>
> PhET 模拟文件头部原文：
> `COMMERCIAL USE REQUIRES A COMMERCIAL LICENSE AGREEMENT FROM THE UNIVERSITY OF COLORADO BOULDER.`
>
> 并且**要求在「使用处附近」标注归属**，推荐措辞：
> `Simulation by PhET Interactive Simulations, University of Colorado Boulder, licensed under CC BY-NC 4.0`
>
> **照抄教材结构的再发布者会踩到这一条。**
>
> 这也说明：**逐条核实许可不能靠印象**——我原先以为 PhET 是 CC BY，**实测推翻了它**。

### 一类特殊的高等级证据：出版社勘误表

`ev-014` `ev-015` 是**出版方自己发布的勘误表**。对「某教材某处有缺陷」这类命题，
它们比教材本身更有力——因为它们是**对该教材内容的权威声明**，不需要第三方推断。

但必须分清同一份证据能支持哪个命题：

| 命题 | 需要什么 | 勘误表够吗 |
|---|---|---|
| 「出版社声明 p.13 漏字」 | 读勘误表 | ✅ **够** |
| 「教材 p.13 真的漏字」 | 翻开教材 | ❌ 不够（勘误表可能滞后，新印次或已修正） |

### 开放教材的许可分两档，别混

`ev-016`~`ev-018` 都来自 OpenStax，但许可不同：

| 教材 | 许可 | 能做什么 |
|---|---|---|
| OpenStax《Physics》 | **CC BY 4.0** | 可自由复用正文（署名即可） |
| OpenStax《College Physics 2e》 | **CC BY-NC-SA 4.0** | **只能引用定位与短引用**，不可复用正文 |

**筛查结果**：OpenStax 的 55 个教材仓库中，只有 **13 个是 CC BY**，其余 **41 个含 NC**。

> [!IMPORTANT]
> **本库是 CC BY-SA 4.0（无 NC），与 NC 内容不兼容。**
> **同一出版社的书，许可可能不同，必须逐本查**——本例中《Physics》是 CC BY，
> 而同社的《College Physics 2e》和《University Physics》都是 CC BY-NC-SA。

## 原始数据

| 文件 | 内容 | 可复算 | 是证据吗 |
|---|---|---|---|
| [`构造数据-欧姆定律演示.csv`](构造数据-欧姆定律演示.csv) | `U = 10 × I` 的**构造**数据。**没有任何测量发生**，也没有温度记录 | ✅ 算术可复算 | ❌ **不是证据**——仅示范欧姆关系长什么样 |
| [`os-teacher-markers.csv`](os-teacher-markers.csv) | OpenStax《Physics》段落级受众标记明细（419 行，含 commit 哈希） | ✅ [脚本](os-teacher-markers.py) 可重跑 | ✅ 是（对源文件的统计） |

> [!IMPORTANT]
> **「可复算」与「是证据」是两件事。**
>
> 上表第一行**算术上完全可复算**（`5.0 / 10.00 = 0.50`），
> 而它**不能支撑任何关于真实世界的命题**——因为**没有人测过**。
>
> `ev-002` 当年就是凭着「可复算」被登记为**等级「高」**的。
