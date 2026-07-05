#!/bin/bash
# sync-down.sh — 把自己 GitHub 上的所有仓库拉到本地 ~/GitHub/ 并生成索引页
# 幂等：已有的仓库只更新（fast-forward），本地有未推送改动的仓库跳过并标注，绝不覆盖本地工作。
set -e
BASE="$HOME/GitHub"
mkdir -p "$BASE"

if ! gh auth status >/dev/null 2>&1; then
  echo "❌ 还没登录 GitHub。先运行: gh auth login -h github.com -p https -w"
  exit 1
fi
LOGIN=$(gh api user -q .login)
echo "✅ 已登录: $LOGIN，仓库根目录: $BASE"

gh repo list "$LOGIN" --limit 200 \
  --json name,description,visibility,updatedAt,url,primaryLanguage,pushedAt \
  > "$BASE/.repos.json"
COUNT=$(python3 -c "import json;print(len(json.load(open('$BASE/.repos.json'))))")
echo "📦 云端共 $COUNT 个仓库"

python3 - "$BASE" << 'PYEOF'
import json, subprocess, sys, os
base = sys.argv[1]
repos = json.load(open(f"{base}/.repos.json"))
status = {}
for r in repos:
    name = r["name"]; path = os.path.join(base, name)
    if os.path.isdir(os.path.join(path, ".git")):
        dirty = subprocess.run(["git","-C",path,"status","--porcelain"],capture_output=True,text=True).stdout.strip()
        if dirty:
            status[name] = "本地有改动，跳过更新"
            print(f"⚠️ {name}: 本地有未提交改动，跳过（不覆盖你的工作）")
            continue
        p = subprocess.run(["git","-C",path,"pull","--ff-only"],capture_output=True,text=True)
        status[name] = "已更新" if p.returncode==0 else "更新失败:"+p.stderr.strip()[:80]
        print(f"🔄 {name}: {status[name]}")
    else:
        p = subprocess.run(["gh","repo","clone",r["url"],path,"--","--quiet"],capture_output=True,text=True)
        status[name] = "新拉取" if p.returncode==0 else "拉取失败:"+p.stderr.strip()[:80]
        print(f"⬇️ {name}: {status[name]}")
json.dump(status, open(f"{base}/.sync-status.json","w"), ensure_ascii=False)
PYEOF

python3 "$HOME/.claude/skills/github-sync/make_index.py" "$BASE" "$LOGIN"
echo "🎉 索引已生成: $BASE/index.html"
