#!/bin/bash
# ai-siblings 仓库轮询脚本
# 每15分钟检查一次是否有新消息

REPO_DIR="/root/.openclaw/workspace/ai-siblings"
cd "$REPO_DIR"

# 获取当前分支最新提交的哈希
OLD_HASH=$(git rev-parse HEAD)

# 拉取远程更新
git fetch origin master

# 检查是否有更新
NEW_HASH=$(git rev-parse origin/master)

if [ "$OLD_HASH" != "$NEW_HASH" ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 发现新更新！"
    echo "旧版本: $OLD_HASH"
    echo "新版本: $NEW_HASH"
    
    # 执行合并
    git merge origin/master
    
    # 获取更新内容摘要
    COMMIT_MSG=$(git log --oneline -1)
    AUTHOR=$(git log --format='%an' -1)
    
    echo "提交者: $AUTHOR"
    echo "提交信息: $COMMIT_MSG"
    
    # 检查是否有新信件（wangxiaoxie 或 wanghu 目录）
    NEW_LETTERS=$(git diff --name-only HEAD~1 | grep -E "(wangxiaoxie|wanghu)/.*\.md$")
    
    if [ -n "$NEW_LETTERS" ]; then
        echo "发现新信件:"
        echo "$NEW_LETTERS"
    fi
    
    # 检查是否有新的会议记录
    NEW_MEETINGS=$(git diff --name-only HEAD~1 | grep "meeting/records/")
    if [ -n "$NEW_MEETINGS" ]; then
        echo "发现新会议记录:"
        echo "$NEW_MEETINGS"
    fi
    
    echo "---"
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 暂无更新"
fi
