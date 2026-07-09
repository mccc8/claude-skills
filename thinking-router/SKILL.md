---
name: thinking-router
description: 思维工具路由器（How to think better）——先物理预检排除资源问题，再按状态×缩放命中轻工具，顽固问题过深度闸门进深根诊断，苏格拉底式一次一问。当用户说"我卡住了""一团乱不知道从哪开始""帮我想想这事""我该用什么框架想这个问题""这毛病老是反复"，或描述一个还没成形的困境时触发。已成形对象要完整分析→analysis-thinking；求助该问谁→smart-asking；目标落卡→goal-builder。
version: 0.6.0
status: 稳定
since: 2026-07-08
source: untools.co + cc-thinking-skills(fork,39框架) + 会话思辨（v0.6：接入姊妹路由器；v0.5改回缩放A+状态B主维度）
---

# Thinking Router — 思维工具路由器

定位：**你不知道该做什么思维动作时的第一站。** 路由：先排除，再对症（两级），再定深浅。
核心纪律：**永不要求用户报工具名**——用户不知道工具名正是他需要路由器的原因。命中靠"何时用"特征匹配，不靠点名（点名只是老手的旁路）。

## 第零关 · 物理预检（进任何工具前必过）

一句话排查："这事有没有可能就是**缺人/缺钱/缺时间/硬件上限**？" 是 → 别用思维工具，去要资源或调预期——**不许用高深模型解释单纯的贫血**。

## 第一段 · 对症路由（两级）

**Level 1 · 五个高频直达**（听到左列原话直接命中，跳过 Level 2）：

| 状态信号（用户原话） | 缩放 | 命中 |
|---|---|---|
| 迷茫："一团糟""目标和手段对不上" | 变焦 | [abstraction-laddering.md](abstraction-laddering.md) |
| 笃定/冲动："肯定是X""马上推翻重做" | 微距 | [ladder-of-inference.md](ladder-of-inference.md) |
| 纠结："A 还是 B" | 广角 | [second-order-thinking.md](second-order-thinking.md) |
| 过载："十件事精疲力竭" | 分拣 | [impact-effort-matrix.md](impact-effort-matrix.md) |
| 对象成形要深挖 / 该问谁 / 目标落卡 | — | → analysis-thinking / smart-asking / goal-builder |

**Level 2 · 全量二级路由**（Level 1 没命中就走这里，覆盖全部 26 卡。主维度用你偏好的**缩放 A + 状态 B**，四分类只作 INDEX 里的浏览标签）：
① 按两个维度之一粗筛（哪个自然问哪个）：
   - **维度 A 缩放**："你是想往深挖根因（微距）、往大看全局后果（广角）、还是重新定义问题本身（变焦）？"
   - **维度 B 状态**："你现在是迷茫 / 纠结 / 过载 / 冲动 / 反复出同样问题？"
② 加载 [tools/INDEX.md](tools/INDEX.md)，按 A 或 B 取候选 → 命中一张加载它（每卡同时标了缩放/状态/类，两个维度都查得到）。
③ 一个信号跨两格 → 摆双候选让用户挑，不硬选。

命中后（两级皆然）**先确认再进入**："听起来你要的是[工具的白话名]，走一遍合适吗？"——确认用工具解决的是什么，不报工具的英文名。

## 第二段 · 深度闸门（重工具层，宁可少进不多进）

触发条件（满足其一才开闸）：同类问题**已反复 ≥3 次**且轻工具跑过仍复发 / 用户点名"老毛病、顽固、重大转型"。
→ 进入 [deep-root.md](deep-root.md)（深根诊断：Iceberg×NLP 双轴 + 5 Whys 钻头）。
深潜纪律：每下一层过两道闸——**收益闸**（"继续挖对解决现状还有实质帮助吗，还是就在这层制定行动？"）和**权限闸**（"这一层你改得动吗？改不动就回上层找次优解"）。

## 硬性断言（自检）

- 物理预检先于一切路由；Level 1 未命中必须走 Level 2，**不许因为"矩阵里没有"就放弃路由**（那是把 21 张卡变死卡的老 bug）
- 路由推荐必附确认问句、用白话名不用工具英文名；引导期一次只问一个问题
- deep-root 不许被日常琐事触发（开闸条件缺一不开）；深潜每层必配"该层最小可行动作"
- 空间型产出用 markdown 表；要正经图 → 接力 whiteboard-explain；结尾必给接力建议

## 编排图（卡与卡怎么串）

- **拆→排→落**：issue-trees/ishikawa 拆出子问题 → impact-effort/eisenhower 排优先级 → goal-builder 落地
- **诊→深→修**：analysis-thinking 确诊 → deep-root 挖结构根因 → incentive-design 开修复处方
- **想→验→行**：任意工具出结论 → ladder-of-inference 查事实/pre-mortem 验失败 → goal-builder 出闸
- 全库共识：每张卡结尾的「接力」字段就是它在图上的出边；路由器在工具产出后应主动提示下一跳。

## 姊妹路由器（cc-thinking-skills，已挂载 39 框架）

本机装了 tjboudreaux/cc-thinking-skills（fork，39 个英文思维 skill + thinking-model-router）。两个 router 天然软分工，**不抢**：
- **找我（本 router）**：中文、思维状态不清（迷茫/纠结/过载/冲动）、需苏格拉底引导、冥想盆场景、要物理预检/情绪律。
- **转 thinking-model-router**：已明确落在某业务领域（代码/架构/产品/战略）用英文框架，或需要我库里没有的框架——贝叶斯、约束理论、机会成本、红队、稻草人、Via-Negativa、后悔最小化、可逆性等十几个。
- 重叠工具（pre-mortem/cynefin/ooda/second-order/systems/inversion/first-principles）两边都有：中文语境用我的卡，英文/工程语境用它的 skill。

## 边界

- 苏格拉底引导服务"想清楚"，不服务"写出来"——产出文档找对应产出型 skill。
- **新增工具原则**：先查 GitHub 有无高星的**对话式引导** skill（cc-thinking-skills 已证明存在，别再默认"品类空白"），有优质现成的就 fork+挂载或适配+标注来源；无则自写。判据见 SOURCING.md。
