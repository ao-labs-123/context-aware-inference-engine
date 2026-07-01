
def analyze_causality(text, agent_info):
    # 因果マーカーの辞書（lexicon/causality_markers.json に分離推奨）
    causality_map = {
        "due to": "CAUSE_PREPOSITION",
        "because": "CAUSE_CONJUNCTION"
    }
    
    # ロジック：マーカーを検索し、文を「原因部」と「結果部」に分割
    for marker, category in causality_map.items():
        if marker in text:
            parts = text.lower().split(marker)
            return {
                "process": f"Agent: {agent_info['agent']} + {category}: {marker}",
                "mapping": f"{parts[1].strip()} -> Causes -> {parts[0].strip()}"
            }
    return {"process": "No Causality Found", "mapping": "None"}
