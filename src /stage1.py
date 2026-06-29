# rules/stage1_rule.py
import json

    def determine_subject(text, lexicon_data):
    # 1. 伝聞マーカーが含まれているか判定
    is_reported = any(marker in text for marker in lexicon_data["Attribution Override"])
    
    # 2. 心理動詞が含まれているか判定
    is_psychological = any(verb in text for verb in lexicon_data["Psychological Verbs"])
    
    # 3. 圏論的ルール（判定ロジック）
    if is_reported:
        # 伝聞があれば、心理動詞の有無にかかわらず「三人称」
        return "Third-Person"
    elif is_psychological:
        # 伝聞がなく、心理動詞だけなら「一人称」
        return "First-Person"
    else:
        # それ以外はデフォルト（あるいは文脈依存）
        return "Neutral"

    pass
