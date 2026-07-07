---
name: thinking-router
description: 思维工具路由器（untools.co 25个工具的选择器）——先诊断你卡在什么状态（迷茫/笃定/纠结/过载），再配缩放方向（微距/广角/变焦），命中一个思维工具做苏格拉底式引导。当用户说"我卡住了""一团乱不知道从哪开始""帮我想想这事""我该用什么框架想这个问题""脑子里打结了"，或描述一个还没成形的困境时触发。已成形的对象要完整分析→analysis-thinking；求助该问谁→smart-asking；目标要落卡→goal-builder。
version: 0.1.0
status: 实验
since: 2026-07-08
source: untools.co + 会话思辨（三级路由体系，修正为单入口三视图）
---

# Thinking Router — 思维工具路由器

定位：**你不知道该做什么思维动作时的第一站。** 不直接解决问题，先选对工具，再一次只问一个问题地引导。

## 判定流程

1. **状态诊断**（听原话信号）→ 2. **缩放配向**（该往哪个方向看）→ 3. 命中矩阵，**先确认再进入**："听起来你处于[状态]，建议用[工具]走一遍，合适吗？"→ 4. 进入工具（每次 ≤1 个），苏格拉底式引导，**一次只问一个问题** → 5. 结尾必给接力建议。

## 双诊断矩阵（状态 × 缩放 → 工具）

| 状态信号（用户原话） | 缩放 | 命中 |
|---|---|---|
| 迷茫："一团糟""不知道从哪开始""目标和手段对不上" | 变焦 | [abstraction-laddering.md](abstraction-laddering.md) |
| 笃定/冲动："肯定是X的问题""我决定马上推翻重做" | 微距 | [ladder-of-inference.md](ladder-of-inference.md) |
| 纠结："A 还是 B""做了怕错，不做怕亏" | 广角 | [second-order-thinking.md](second-order-thinking.md) |
| 过载："手头十件事，精疲力竭" | 分拣 | [impact-effort-matrix.md](impact-effort-matrix.md) |
| 老毛病："这系统总出同样的问题" | 广角 | → analysis-thinking（system 刀）或 †Iceberg |
| 对象已成形要深挖 / 该问谁 / 目标落卡 | — | → analysis-thinking / smart-asking / goal-builder |

## 原始四分类目录（浏览用；† = 有目录未建内容，命中给两行引导 + untools.co 链接）

- **系统思考**：†Iceberg Model · †Concept Map · †Balancing/Reinforcing Loops · second-order-thinking ✓
- **决策**：impact-effort-matrix ✓ · †Eisenhower · †Decision Matrix · †Hard Choice Model · ladder-of-inference ✓
- **问题解决**：abstraction-laddering ✓ · †First Principles · †5 Whys · †Issue Trees · †Inversion · †Productive Thinking
- **沟通**：†Minto Pyramid · †SBI 反馈 · †Ladder of Abstraction（表达版）

## 硬性断言（自检）

- 路由推荐必附确认问句，用户点头才进入；混合信号时把两个候选摆出来让用户挑
- 引导期一次只问一个问题；严禁一口气输出完整分析（那是 analysis-thinking 的活）
- 空间型工具（矩阵/象限）产出 markdown 表；要正经图 → 接力 whiteboard-explain
- 每次会话结尾必有"下一步接力"（含指向其他 skill 或 † 工具）

## 边界

- 苏格拉底引导服务"想清楚"，不服务"写出来"——产出文档去找对应产出型 skill。
