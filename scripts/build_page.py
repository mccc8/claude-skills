#!/usr/bin/env python3
"""从各 skill 的 SKILL.md frontmatter 生成 docs/index.html 展示页。
用法：python3 scripts/build_page.py（在仓库根目录运行，幂等可重复）"""
import os, re, html
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "index.html")

# 展示顺序与两字铭牌（新 skill 不在表里时自动排在最后，铭牌取名字）
BADGES = {
    "goal-builder": ("目标铸卡", "🎯"), "recess": ("休会", "⏸"),
    "c4-diagram": ("架构制图", "🏗"), "whiteboard-explain": ("白板讲解", "🖊"),
    "trigger-audit": ("触发审计", "🔍"), "github-publish": ("一键发布", "🚀"),
    "github-sync": ("下行同步", "⬇️"), "agents-workspace-audit": ("工作区审计", "🗂"),
    "analysis-thinking": ("分析分诊", "🧠"),
    "smart-asking": ("求助分诊", "🙋"),
}

skills = []
for d in sorted(os.listdir(ROOT), key=lambda x: list(BADGES).index(x) if x in BADGES else 99):
    md = os.path.join(ROOT, d, "SKILL.md")
    if not os.path.isdir(os.path.join(ROOT, d)) or not os.path.exists(md):
        continue
    text = open(md, encoding="utf-8").read()
    m = re.search(r"description: (.*)", text)
    desc = m.group(1).strip() if m else ""
    # 取 description 第一句作为卡片摘要，触发句展开放详情
    first = re.split(r"[。]", desc)[0] + "。"
    quotes = re.findall(r'[""]([^""]{2,20})[""]', desc)[:4]
    badge, icon = BADGES.get(d, (d, "🃏"))
    skills.append({"name": d, "badge": badge, "icon": icon, "first": first, "quotes": quotes})

cards = "\n".join(f"""
  <a class="card" href="https://github.com/mccc8/claude-skills/tree/main/{s['name']}">
    <div class="top"><span class="icon">{s['icon']}</span><span class="badge">{html.escape(s['badge'])}</span></div>
    <div class="name">{s['name']}</div>
    <div class="desc">{html.escape(s['first'])}</div>
    {'<div class="quotes">' + ' '.join('<span>「'+html.escape(q)+'」</span>' for q in s['quotes']) + '</div>' if s['quotes'] else ''}
  </a>""" for s in skills)

page = f"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>mccc 的技能架 · claude-skills</title>
<style>
  * {{ box-sizing: border-box; margin: 0; }}
  body {{ font-family: -apple-system, 'PingFang SC', 'Noto Sans SC', sans-serif; background: #fcfcfa; color: #2b2b2b;
         max-width: 1060px; margin: 0 auto; padding: 56px 24px; }}
  header h1 {{ font-size: 30px; letter-spacing: 1px; }}
  header .motto {{ color: #888; margin-top: 10px; font-size: 15px; }}
  header .links {{ margin-top: 16px; font-size: 14px; }}
  header .links a {{ color: #1168BD; text-decoration: none; margin-right: 18px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(310px, 1fr)); gap: 18px; margin-top: 40px; }}
  .card {{ background: #fff; border: 1px solid #ececea; border-radius: 14px; padding: 22px;
           text-decoration: none; color: inherit; transition: box-shadow .15s, transform .15s; }}
  .card:hover {{ box-shadow: 0 6px 22px rgba(0,0,0,.08); transform: translateY(-2px); }}
  .top {{ display: flex; align-items: center; gap: 8px; }}
  .icon {{ font-size: 20px; }}
  .badge {{ font-size: 13px; color: #1168BD; background: #eef4ff; border-radius: 20px; padding: 2px 12px; }}
  .name {{ font-family: ui-monospace, Menlo, monospace; font-size: 16px; font-weight: 600; margin: 12px 0 8px; }}
  .desc {{ font-size: 13.5px; color: #555; line-height: 1.7; }}
  .quotes {{ margin-top: 12px; font-size: 12px; color: #999; line-height: 2; }}
  .quotes span {{ margin-right: 6px; }}
  .roadmap {{ margin-top: 48px; background: #fff; border: 1px solid #ececea; border-radius: 14px; padding: 26px; }}
  .roadmap h2 {{ font-size: 18px; }}
  .roadmap p {{ font-size: 14px; color: #555; line-height: 1.9; margin-top: 10px; }}
  .roadmap .m {{ display: inline-block; font-size: 12.5px; background: #f4f6f4; border-radius: 8px; padding: 4px 10px; margin: 6px 6px 0 0; color: #456; }}
  .roadmap .m.done {{ background: #e9f6ec; color: #2da44e; }}
  footer {{ margin-top: 44px; font-size: 12.5px; color: #aaa; text-align: center; }}
  footer a {{ color: #999; }}
</style>
</head>
<body>
<header>
  <h1>🃏 mccc 的技能架</h1>
  <div class="motto">看一个，写一个，用一个。—— Skill = Trigger + Action，为"不在场"而写，没有断言不算写完。</div>
  <div class="links">
    <a href="https://github.com/mccc8/claude-skills">GitHub 仓库</a>
    <a href="https://github.com/mccc8/claude-skills/blob/main/ROADMAP.md">数据分析路线图</a>
    <a href="https://github.com/mccc8/claude-skills/blob/main/docs/skill写作方法论.md">写作方法论</a>
  </div>
</header>

<div class="grid">{cards}
</div>

<div class="roadmap">
  <h2>🗺 正在进行：数据分析 Skill（决策类型六分法）</h2>
  <p>母题：围绕不同决策类型，用个人数据写出一套可信的数据分析 Skill——公开方法与 eval 设计，私藏数据与字典。每个 skill 都是一个分析作业包：schema 要求 + 报告模板 + 三类 eval（含"坏数据必须认怂"用例）。</p>
  <div>
    <span class="m done">M0 开张</span><span class="m">M1 描述型·数据体检</span><span class="m">M2 描述型·决策简报</span><span class="m">M3 监控型·自动周报</span><span class="m">M4 诊断型·归因</span><span class="m">M5 预测型·baseline</span><span class="m">M6 评估·闭环</span>
  </div>
</div>

<footer>更新于 {date.today().isoformat()} · 由 <a href="https://github.com/mccc8/claude-skills/blob/main/scripts/build_page.py">build_page.py</a> 从 SKILL.md 自动生成 · 安装：<code>npx skills add mccc8/claude-skills -g --all</code></footer>
</body>
</html>"""
open(OUT, "w", encoding="utf-8").write(page)
print(f"生成 {OUT}（{len(skills)} 个技能）")
