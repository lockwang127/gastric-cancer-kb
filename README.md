# 胃癌知识库 (Gastric Cancer Knowledge Base)

基于结构化知识三元组的胃癌医学知识库，支持RAG和AI应用集成。

## 仓库结构

```
gastric-cancer-kb/
├── data/
│   ├── knowledge-graph/      # 知识三元组源文件
│   │   ├── epidemiology.json    # 流行病学数据
│   │   ├── biomarkers.json      # 分子分型数据
│   │   ├── csco_2024.json       # CSCO指南推荐
│   │   └── treatment.json        # 治疗方案
│   ├── kb.json               # 构建后的完整知识库
│   └── kb_meta.json          # 知识库元数据
├── scripts/
│   ├── build_kb.py           # 知识库构建脚本
│   ├── sync_to_github.py      # GitHub同步脚本
│   └── tests/
│       └── test_kb_format.py  # 格式验证测试
├── schemas/
│   └── triplet_schema.json    # 三元组数据Schema
├── docs/
│   └── domain_guide.md        # 领域指南
├── README.md                  # 本文件
├── UPDATE_POLICY.md           # 更新策略
├── CHANGELOG.md               # 变更日志
└── DEPLOY.md                  # 部署指南
```

## 知识内容

### 核心知识域

| 知识域 | 三元组数量 | 主要内容 |
|--------|-----------|---------|
| 流行病学 | 14条 | 发病率、死亡率、危险因素 |
| 分子分型 | 16条 | Lauren分型、HER2、MSI、PD-L1 |
| CSCO指南 | 17条 | 早期/进展期/晚期治疗推荐 |
| 治疗 | 18条 | 手术、化疗、靶向、免疫 |

### 知识三元组格式

```json
{
  "head": "胃癌",
  "relation": "2022年中国新发病例数",
  "tail": "35.87万",
  "source": "国家癌症中心",
  "evidence": "2022年中国恶性肿瘤流行情况分析",
  "domain": "流行病学",
  "confidence": 0.95,
  "pmid": "37135636"
}
```

## 快速开始

### 构建知识库

```bash
cd gastric-cancer-kb
python3 scripts/build_kb.py
```

### 验证格式

```bash
python3 scripts/tests/test_kb_format.py
```

### 同步到GitHub

```bash
# 添加远程仓库
git remote add origin git@github.com:lockwang127/gastric-cancer-kb.git

# 推送代码
git push -u origin main
```

## 应用场景

- **AI医疗助手**：胃癌诊疗知识问答
- **临床决策支持**：治疗方案推荐
- **医学教育**：胃癌知识学习
- **研究辅助**：文献检索和证据整理

## 数据来源

- CSCO胃癌诊疗指南2024
- 国家癌症中心统计数据
- GLOBOCAN全球癌症数据
- TCGA胃癌分子分型研究
- ToGA、RAINBOW等关键临床试验

## 贡献指南

欢迎提交Pull Request或Issue来完善知识库。

## 许可证

MIT License

## 联系方式

- GitHub: [lockwang127/gastric-cancer-kb](https://github.com/lockwang127/gastric-cancer-kb)
