# claude-skills

我的 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 自定义技能集：**看一个，写一个，用一个。**

📄 [技能展示页](https://mccc8.github.io/claude-skills/) · 🗺 [数据分析 Skill 路线图](ROADMAP.md) · 📖 [Skill 写作方法论](docs/skill写作方法论.md)

> 背景上下文：[仓库起源与定位](docs/context/01-仓库起源与定位.md)（Registry → Hub → Pack Manager）· [数据分析思考来源](docs/context/02-数据分析思考来源.md)（None-One-Many / default action）· [双向同步机制](docs/同步机制.md)（GitHub 为准）

## 安装

使用 [skills CLI](https://github.com/vercel-labs/skills)（基于 `npx`）一行安装：

```bash
# 安装全部技能（全局）
npx skills add mccc8/claude-skills -g --all

# 安装单个技能
npx skills add mccc8/claude-skills -g --skill goal-builder

# 查看仓库中有哪些技能
npx skills add mccc8/claude-skills -l
```

### 替代方式：git clone

```bash
git clone https://github.com/mccc8/claude-skills.git ~/.claude/skills
```

## 技能

| 技能 | 说明 |
|------|------|
| **goal-builder** | 目标铸卡 — 把模糊目标压成六要素目标卡（Objective/Scope/Constraints/Done when/Stop if/Token Budget），给任何长任务装上刹车 |
| **recess** | 休会 — 把发散的讨论强制收敛为 ≤150 字"最小可续状态"，制造干净的信息重置点 |
| **c4-diagram** | 架构制图 — 用 C4 模型（Context/Container/Component/Code）画软件架构信息图，输出自包含 SVG |
| **whiteboard-explain** | 白板讲解 — 把文章/概念转成手绘马克笔风格的板书 SVG，黑红蓝三色、涂改痕迹、讲解动线 |
| **trigger-audit** | 触发审计 — 用 Skill=Trigger+Action 原则给 skill 的 description 体检打分并重写，治"写了却从不触发"的病 |
| **github-publish** | 一键发布 — 本地文件夹 → GitHub 仓库全自动（init/commit/建仓/push），零 git 经验可用 |
| **github-sync** | 下行同步 — 云端仓库全量拉回本地 + 生成可双击的索引页，绝不覆盖本地改动 |
| **agents-workspace-audit** | 工作区审计 — 对 AGENTS.md / CLAUDE.md 治理的 agent 工作区做证据化审计与评分 |

## 方法论（这些 skill 是怎么写出来的）

四条硬规则，全文见 [skill 写作方法论](docs/skill写作方法论.md)：

1. **Skill = Trigger + Action，不是知识文档** —— 从用户行为逆向设计触发，description 写场景线索不写功能清单
2. **为"你不在场"而写** —— 每个 skill 自带边界、硬约束、验收清单和停止条件
3. **渐进式披露** —— SKILL.md 一屏当目录，细节放引用文件按需加载
4. **没有断言不算写完** —— 每个 skill 带可机械验证的自检断言，跑不过就回炉

## 下一步

正在按 [ROADMAP](ROADMAP.md) 写**数据分析 Skill**：围绕六类决策（描述/监控/诊断/预测/因果/决策）逐个里程碑推进，公开方法框架与 eval 设计，私有数据字典与个人数据。

## 维护

- 每周一自动触发审计 loop，全量体检技能触发质量
- 本地用 WorkDeck（自研个人工作台）管理：计划 / 知识 / 产物 / 技能四类资产
- 本地与线上冲突时，以 GitHub 线上版本为准
