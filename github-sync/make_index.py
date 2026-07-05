#!/usr/bin/env python3
"""生成本地仓库索引页 ~/GitHub/index.html（纯静态，双击可开，无需服务）"""
import json, sys, os, html
from datetime import datetime

base, login = sys.argv[1], sys.argv[2]
repos = json.load(open(f"{base}/.repos.json"))
try: status = json.load(open(f"{base}/.sync-status.json"))
except FileNotFoundError: status = {}

def readme_first_line(path):
    for fn in ("README.md", "readme.md", "README_CN.md"):
        p = os.path.join(path, fn)
        if os.path.exists(p):
            for line in open(p, encoding="utf-8", errors="ignore"):
                t = line.strip().lstrip("#").strip()
                if t: return t[:80]
    return ""

cards = []
for r in sorted(repos, key=lambda x: x.get("pushedAt") or "", reverse=True):
    name = r["name"]; path = os.path.join(base, name)
    local = os.path.isdir(path)
    desc = r.get("description") or readme_first_line(path) if local else (r.get("description") or "")
    lang = (r.get("primaryLanguage") or {}).get("name", "") if r.get("primaryLanguage") else ""
    pushed = (r.get("pushedAt") or "")[:10]
    vis = "🔒 私有" if r["visibility"] == "PRIVATE" else "🌍 公开"
    st = status.get(name, "本地未拉取" if not local else "")
    st_class = "warn" if ("跳过" in st or "失败" in st or "未拉取" in st) else "ok"
    cards.append(f"""
    <div class="card">
      <div class="row"><span class="name">{html.escape(name)}</span><span class="vis">{vis}</span></div>
      <div class="desc">{html.escape(desc or "（无描述）")}</div>
      <div class="meta">{html.escape(lang)} · 最近推送 {pushed} · <span class="{st_class}">{html.escape(st)}</span></div>
      <div class="links">
        <a href="{r['url']}">GitHub ↗</a>
        {'<a href="file://'+html.escape(path)+'">本地文件夹</a>' if local else ''}
      </div>
    </div>""")

page = f"""<!DOCTYPE html><html lang="zh"><head><meta charset="utf-8">
<title>{login} 的仓库索引</title>
<style>
 body{{font-family:-apple-system,'PingFang SC',sans-serif;background:#fafafa;margin:0;padding:40px;color:#333}}
 h1{{font-size:22px}} .sub{{color:#999;font-size:13px;margin-bottom:24px}}
 .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:16px}}
 .card{{background:#fff;border-radius:10px;padding:18px;box-shadow:0 1px 4px rgba(0,0,0,.06)}}
 .row{{display:flex;justify-content:space-between;align-items:center}}
 .name{{font-weight:600;font-size:16px}} .vis{{font-size:12px;color:#777}}
 .desc{{color:#555;font-size:13px;margin:8px 0;line-height:1.5}}
 .meta{{font-size:12px;color:#999}} .ok{{color:#2da44e}} .warn{{color:#d63b2f}}
 .links{{margin-top:10px;font-size:13px}} .links a{{margin-right:14px;color:#2f5fd0;text-decoration:none}}
</style></head><body>
<h1>📚 {login} 的仓库索引</h1>
<div class="sub">共 {len(repos)} 个仓库 · 更新于 {datetime.now().strftime('%Y-%m-%d %H:%M')} · 本地根目录 {base}</div>
<div class="grid">{''.join(cards)}</div>
</body></html>"""
open(f"{base}/index.html", "w").write(page)
print(f"索引页: {base}/index.html （{len(repos)} 个仓库）")
