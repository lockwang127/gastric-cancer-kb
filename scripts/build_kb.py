#!/usr/bin/env python3
"""
胃癌知识库构建脚本
将分散的知识三元组文件合并为统一的kb.json
"""

import json
import os
from pathlib import Path
from datetime import datetime

def load_triplets(file_path: str) -> list:
    """加载知识三元组文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def build_knowledge_base():
    """构建知识库"""
    base_dir = Path(__file__).parent.parent
    kg_dir = base_dir / "data" / "knowledge-graph"
    output_path = base_dir / "data" / "kb.json"
    meta_path = base_dir / "data" / "kb_meta.json"

    # 获取所有知识文件
    kg_files = list(kg_dir.glob("*.json"))
    kg_files = [f for f in kg_files if f.name not in ['kb.json', 'kb_meta.json']]

    all_triplets = []
    domains = set()
    file_stats = {}

    for kg_file in sorted(kg_files):
        triplets = load_triplets(str(kg_file))
        file_stats[kg_file.name] = len(triplets)

        for triplet in triplets:
            # 添加source_file信息
            triplet['source_file'] = kg_file.name
            all_triplets.append(triplet)
            domains.add(triplet.get('domain', 'unknown'))

    # 构建kb.json
    # Write triples array directly

    # 写入kb.json
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_triplets, f, ensure_ascii=False, indent=2)

    # 构建kb_meta.json
    meta_data = {
        "version": "1.0.0",
        "generated_at": datetime.now().isoformat(),
        "total_triplets": len(all_triplets),
        "domains": sorted(list(domains)),
        "files": file_stats,
        "description": "胃癌知识库 - 基于CSCO指南、流行病学数据和临床研究"
    }

    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(meta_data, f, ensure_ascii=False, indent=2)

    print(f"知识库构建完成!")
    print(f"总计: {len(all_triplets)} 条知识三元组")
    print(f"知识域: {', '.join(sorted(domains))}")
    print(f"文件统计: {file_stats}")
    print(f"输出: {output_path}")
    print(f"元数据: {meta_path}")

    return kb_data

if __name__ == "__main__":
    build_knowledge_base()
