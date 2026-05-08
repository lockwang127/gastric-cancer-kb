#!/usr/bin/env python3
"""
知识库格式验证测试
验证kb.json格式是否符合规范
"""

import json
import sys
from pathlib import Path

REQUIRED_FIELDS = ['head', 'relation', 'tail', 'source', 'evidence', 'domain', 'confidence']
OPTIONAL_FIELDS = ['pmid', 'source_file']

def validate_triplet(triplet: dict, index: int) -> list:
    """验证单个三元组"""
    errors = []

    for field in REQUIRED_FIELDS:
        if field not in triplet:
            errors.append(f"  Triplet #{index}: 缺少必需字段 '{field}'")

    if 'confidence' in triplet:
        conf = triplet['confidence']
        if not isinstance(conf, (int, float)) or conf < 0 or conf > 1:
            errors.append(f"  Triplet #{index}: confidence值必须在0-1之间，当前值: {conf}")

    return errors

def test_kb_format():
    """测试知识库格式"""
    base_dir = Path(__file__).parent.parent.parent
    kb_path = base_dir / "data" / "kb.json"

    print("=" * 50)
    print("胃癌知识库格式验证测试")
    print("=" * 50)

    if not kb_path.exists():
        print(f"\n错误: kb.json 不存在")
        print(f"请先运行: python3 scripts/build_kb.py")
        return False

    print(f"\n正在验证: {kb_path}")

    # 加载kb.json
    try:
        with open(kb_path, 'r', encoding='utf-8') as f:
            kb_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"\nJSON解析错误: {e}")
        return False

    # 验证顶层结构
    required_top = ['version', 'generated_at', 'total_triplets', 'domains', 'triplets']
    for field in required_top:
        if field not in kb_data:
            print(f"错误: kb.json缺少顶层字段 '{field}'")
            return False

    print(f"✓ 顶层结构验证通过")
    print(f"  版本: {kb_data['version']}")
    print(f"  生成时间: {kb_data['generated_at']}")
    print(f"  总三元组数: {kb_data['total_triplets']}")
    print(f"  知识域: {', '.join(kb_data['domains'])}")

    # 验证三元组数量
    triplet_count = len(kb_data['triplets'])
    if triplet_count != kb_data['total_triplets']:
        print(f"警告: 三元组数量不匹配 (声明: {kb_data['total_triplets']}, 实际: {triplet_count})")

    # 验证每个三元组
    all_errors = []
    for i, triplet in enumerate(kb_data['triplets']):
        errors = validate_triplet(triplet, i + 1)
        all_errors.extend(errors)

    if all_errors:
        print(f"\n发现 {len(all_errors)} 个格式错误:")
        for error in all_errors[:20]:  # 只显示前20个错误
            print(error)
        if len(all_errors) > 20:
            print(f"  ... 还有 {len(all_errors) - 20} 个错误")
        return False

    print(f"\n✓ 所有 {triplet_count} 条知识三元组格式验证通过!")

    # 统计各域三元组数量
    domain_counts = {}
    for triplet in kb_data['triplets']:
        domain = triplet.get('domain', 'unknown')
        domain_counts[domain] = domain_counts.get(domain, 0) + 1

    print(f"\n知识域分布:")
    for domain, count in sorted(domain_counts.items()):
        print(f"  {domain}: {count}条")

    print("\n" + "=" * 50)
    print("验证完成 - 格式正确")
    print("=" * 50)

    return True

if __name__ == "__main__":
    success = test_kb_format()
    sys.exit(0 if success else 1)
