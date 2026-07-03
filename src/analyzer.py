# analyzer.py

class LogicAnalyzer:
    def __init__(self, lexicon_data):
        self.lexicon = lexicon_data

    def stage1_analyze(self, text, subject_result):
        if subject_result in ["I", "He", "She", "They", "We", "You", "It"]:
            return {
                "process": "Explicit Subject Present",
                "decision": "Priority: Explicit Subject",
                "agent": subject_result
                }
            
        # stage1_rule.py で判定した結果を受け取ります
        if subject_result == "Third-Person":
            return {
                "process": "Psychological Verb + Null Subject + Evidential Marker",
                "decision": "Override: 3rd Party",
                "agent": "He/She/They"
                }
        elif subject_result == "First-Person":
            return {
                "process": "Psychological Verb + Null Subject",
                "decision": "Default: Speaker",
                "agent": "I"
                }
        else:
            return {
                "process": "Standard",
                "decision": "None",
                "agent": "Unknown"
                }


    def stage3_analyze(self, text, log1):
        # log1 から Stage 1 で特定した Agent を受け取る
        agent = log1["agent"]
        
        # 因果マーカーの定義
        markers = ["due to", "because"]
        
        for marker in markers:
            if marker in text.lower():
                # マーカーを基準に文を分割（[結果] + [マーカー] + [原因]）
                parts = text.lower().split(marker)
                effect = parts[0].strip()
                cause = parts[1].replace('.', '').strip()
                   
                return {
                    "process": f"Agent: {agent} + Marker: {marker}",
                    "mapping": f"{cause} -> Causes -> {effect}",
                    "structure": {"cause": cause, "effect": effect}
                }
                
                return {"process": "No causality found", "mapping": "None"}

