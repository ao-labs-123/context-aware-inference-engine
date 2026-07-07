import re

def analyze_causality_and_ambiguity(text, subject_status):
    target_text = text.strip().rstrip(".")
    
    # Stage 1 で主語が特定できていない（None, "Unknown"）または辞書型ではない単語の場合
    is_subject_undetermined = (
        subject_status is None or 
        subject_status == "Unknown" or 
        (isinstance(subject_status, str) and subject_status == "Unknown")
    )
    
    if is_subject_undetermined:
        # 3文に共通する「主語が特定できないAction動詞の省略」を検知
        words = target_text.split()
        if words:
            # 心理動詞（Thoughtなど）はStage1で処理されているはずなので、
            # ここに流れてきた主語なし文はすべて「聞き返し対象（Ambiguous）」としてマークする
            return {
                "ambiguity_type": "Undetermined_Agent",
                "status": "Ambiguous",
                "fallback": "Trigger Clarification"
            }
            
    return {
        "ambiguity_type": "None",
        "status": "Clear",
        "fallback": "Proceed"
    }
