> 子指令：面向公开社区的 issue/求助帖（GitHub issue、论坛、Stack Overflow）。这是 ESR 原味最浓的场景：公开、可追溯、会被后人检索——你写的不是求助，是未来的文档。

生成 issue/帖子，结构：

**Title**：[对象+版本] - [偏差]。可检索性优先：包含关键报错词，未来撞同样问题的人要能搜到它。
**Environment**：OS/版本/硬件/依赖清单——照官方 issue 模板要求填全。
**Minimal Reproduction**：最小可复现用例（代码 ≤30 行或最小操作序列）；能一条命令复现最佳。
**Expected vs Actual**：预期行为 vs 实际行为，附原始输出。
**Research Log**：已查过的 issue 编号、文档章节、尝试过的 workaround——避免维护者重复劳动，也证明非重复提问。
**（可选）Suspected Cause**：仅当有依据时给；标注为推测。

发帖纪律：
- 先搜再发：搜 closed issues + 报错原文；重复 issue 是公共资源的浪费。
- 选对层级：用户问题去 discussion/用户区，确认 bug 才进 issue tracker。
- **善后是硬义务**：解决后回帖标 FIXED + 简述有效解法与走过的盲路（未来搜到此帖的人靠这个活命）；若文档缺陷导致问题，顺手提文档补丁——用新答案覆盖旧困惑。
