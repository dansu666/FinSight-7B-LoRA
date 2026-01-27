import json
import random

# 模拟数据生成器
templates = [
    ("据知情人士透露，{company}正在考虑收购竞争对手{target}，交易金额或达50亿美元。", "Neutral", "Medium", "1. 收购传闻通常会导致股价波动。2. 整合风险较高，且面临反垄断审查。"),
    ("{company}因车辆安全气囊存在隐患，宣布召回全球范围内200万辆汽车。", "Negative", "High", "1. 大规模召回直接产生巨额维修成本。2. 品牌声誉受损，影响后续销量。"),
    ("{company}发布的最新AI芯片在基准测试中性能超越了{target}的旗舰产品。", "Positive", "None", "1. 技术领先地位得到确认。2. 预计将抢占更多数据中心市场份额。")
]
companies = ["特斯拉", "英伟达", "微软", "比亚迪"]
targets = ["Rivian", "AMD", "OpenAI", "宁德时代"]

dataset = []
for i in range(100):
    tmpl, sent, risk, reason = random.choice(templates)
    c, t = random.choice(companies), random.choice(targets)
    text = tmpl.format(company=c, target=t)
    
    # 构造思维链
    full_reasoning = f"1. 实体识别：{c}。 2. 事件分析：{text} 3. 风险逻辑：{reason} 4. 结论：风险等级为{risk}。"
    
    # 输出 JSON
    out_json = json.dumps({"entity": c, "sentiment": sent, "risk": risk, "reasoning": full_reasoning}, ensure_ascii=False)
    
    dataset.append({
        "instruction": "分析金融文本风险，输出JSON。",
        "input": text,
        "output": out_json
    })

# 保存文件
save_path = "/root/lanyun-tmp/FinSight-Project/data/fin_training_data.json"
with open(save_path, "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)
print(f"✅ 数据集生成完毕: {save_path}")
