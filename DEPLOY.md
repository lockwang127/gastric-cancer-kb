# 胃癌知识库部署指南

本指南帮助您将胃癌知识库部署到GitHub。

## 前置要求

- Git已安装
- GitHub账户

## 部署步骤

### 1. 在GitHub创建仓库

1. 访问 [GitHub New Repository](https://github.com/new)
2. 填写仓库信息：
   - **Repository name**: `gastric-cancer-kb`
   - **Description**: `基于结构化知识三元组的胃癌医学知识库，支持RAG和AI应用集成`
   - **Visibility**: Public (公开)
   - **不要勾选** "Add a README file"
   - **不要勾选** "Add .gitignore"

3. 点击 "Create repository"

### 2. 配置本地仓库

在本地仓库目录中执行以下命令：

```bash
# 进入仓库目录
cd /Users/wangxiaodong/WorkBuddy/gastric-cancer-kb

# 初始化Git (如尚未初始化)
git init

# 添加所有文件
git add .

# 创建初始提交
git commit -m "Initial commit: 胃癌知识库 v1.0.0
- 65条知识三元组
- 4个知识域: 流行病学、分子分型、CSCO指南、治疗
- 包含构建和测试脚本"

# 设置远程仓库
git remote add origin git@github.com:lockwang127/gastric-cancer-kb.git

# 推送代码到GitHub
git push -u origin main
```

### 3. 验证部署

访问 https://github.com/lockwang127/gastric-cancer-kb 查看仓库。

## 后续更新

### 更新知识库

1. 修改相关JSON文件
2. 重新构建知识库：

```bash
cd /Users/wangxiaodong/WorkBuddy/gastric-cancer-kb
python3 scripts/build_kb.py
python3 scripts/tests/test_kb_format.py
```

3. 提交并推送：

```bash
git add .
git commit -m "Update: 您的更新说明"
git push
```

## 使用方式

### 构建知识库

```bash
python3 scripts/build_kb.py
```

### 验证格式

```bash
python3 scripts/tests/test_kb_format.py
```

### 同步到GitHub

```bash
python3 scripts/sync_to_github.py
```

## 常见问题

### Q: 推送被拒绝？

如果远程仓库已有内容，先拉取再推送：

```bash
git pull origin main --rebase
git push origin main
```

### Q: SSH密钥未配置？

1. 检查SSH密钥：
```bash
cat ~/.ssh/id_rsa.pub
```

2. 如无密钥，生成：
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

3. 在GitHub Settings > SSH and GPG keys 添加公钥

### Q: 如何克隆到其他机器？

```bash
git clone git@github.com:lockwang127/gastric-cancer-kb.git
```

## 仓库信息

- **仓库地址**: https://github.com/lockwang127/gastric-cancer-kb
- **克隆地址**: git@github.com:lockwang127/gastric-cancer-kb.git
- **HTTPS地址**: https://github.com/lockwang127/gastric-cancer-kb.git
