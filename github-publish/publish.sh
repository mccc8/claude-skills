#!/bin/bash
# publish.sh <文件夹路径> [仓库名] [--public]
# 幂等：任何状态下重复跑都安全。没登录会明确报错并给指引，不会做一半。
set -e

FOLDER="${1:?用法: publish.sh <文件夹路径> [仓库名] [--public]}"
FOLDER="$(cd "$FOLDER" && pwd)"
REPO="${2:-$(basename "$FOLDER" | tr ' ' '-')}"
VISIBILITY="--private"
[[ "$3" == "--public" || "$2" == "--public" ]] && VISIBILITY="--public"
[[ "$2" == "--public" ]] && REPO="$(basename "$FOLDER" | tr ' ' '-')"

echo "📁 目标文件夹: $FOLDER"
echo "📦 仓库名: $REPO ($([ "$VISIBILITY" = "--private" ] && echo 私有 || echo 公开))"

# 1. 登录检查
if ! gh auth status >/dev/null 2>&1; then
  echo "❌ 还没登录 GitHub。请先完成一次性登录（跟着浏览器点就行）："
  echo "   gh auth login -h github.com -p https -w"
  exit 1
fi
LOGIN=$(gh api user -q .login)
echo "✅ 已登录: $LOGIN"

# 2. git 身份（缺了自动补，用 GitHub 免暴露邮箱的 noreply 地址）
if [ -z "$(git config --global user.email)" ]; then
  UID_=$(gh api user -q .id)
  git config --global user.name "$LOGIN"
  git config --global user.email "${UID_}+${LOGIN}@users.noreply.github.com"
  echo "✅ 已自动配置 git 身份: $LOGIN"
fi

cd "$FOLDER"

# 3. 没有 git 仓库就新建
if [ ! -d .git ]; then
  git init -b main >/dev/null
  echo "✅ 已初始化 git 仓库"
fi

# 4. 默认忽略备份和系统垃圾文件
if [ ! -f .gitignore ]; then
  printf '.DS_Store\n*.bak-*\n*.svg.png\n' > .gitignore
  echo "✅ 已生成 .gitignore（忽略备份与系统文件）"
fi

# 5. 有变更就提交
git add -A
if ! git diff --cached --quiet; then
  git commit -m "更新于 $(date '+%Y-%m-%d %H:%M')" >/dev/null
  echo "✅ 已提交本次变更"
else
  echo "ℹ️ 没有新变更"
fi

# 6. 远端不存在就创建并推送；存在就直接推送
if ! git remote get-url origin >/dev/null 2>&1; then
  gh repo create "$REPO" $VISIBILITY --source . --push >/dev/null
  echo "✅ 已在 GitHub 创建仓库并推送"
else
  git push -u origin main >/dev/null 2>&1 || git push -u origin HEAD
  echo "✅ 已推送到 GitHub"
fi

echo "🎉 完成: https://github.com/$LOGIN/$REPO"
