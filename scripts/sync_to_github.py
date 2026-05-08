#!/usr/bin/env python3
"""
GitHub同步脚本
将本地知识库同步到GitHub仓库
"""

import os
import subprocess
from pathlib import Path
from datetime import datetime

def get_git_status():
    """获取Git状态"""
    try:
        result = subprocess.run(['git', 'status', '--porcelain'],
                             capture_output=True, text=True, cwd=REPO_DIR)
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"

def sync_to_github():
    """同步到GitHub"""
    REPO_DIR = Path(__file__).parent.parent

    print("=" * 50)
    print("胃癌知识库 - GitHub同步工具")
    print("=" * 50)

    # 检查远程仓库
    result = subprocess.run(['git', 'remote', '-v'],
                           capture_output=True, text=True, cwd=REPO_DIR)

    if 'origin' not in result.stdout:
        print("\n未检测到远程仓库!")
        print("\n请按以下步骤操作:")
        print("1. 访问 https://github.com/new 创建名为 'gastric-cancer-kb' 的仓库 (Public)")
        print("2. 在本地仓库执行:")
        print("   git remote add origin git@github.com:lockwang127/gastric-cancer-kb.git")
        print("   git push -u origin main")
        return

    print(f"\n远程仓库已配置: {result.stdout}")

    # 检查本地修改
    status = get_git_status()
    if status:
        print(f"\n检测到未提交的更改:")
        print(status)
        print("\n请先提交更改:")
        print("git add .")
        print("git commit -m '您的提交信息'")
        print("git push")
    else:
        print("\n没有检测到未提交的更改")

    print("\n" + "=" * 50)
    print("同步完成")
    print("=" * 50)

if __name__ == "__main__":
    sync_to_github()
