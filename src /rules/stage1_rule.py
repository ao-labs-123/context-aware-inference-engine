import json

def get_lexicon():
    with open('/workspaces/context-aware-inference-engine/src/lexicon/psychological_verbs.json', 'r') as f:
        verbs = json.load(f)
    with open('/workspaces/context-aware-inference-engine/src/lexicon/attribution_markers.json', 'r') as f:
        markers = json.load(f)
    return {**verbs, **markers}

def determine_subject(text):
    lexicon = get_lexicon()
    
    # 伝聞マーカーの判定
    is_reported = any(m in text for m in lexicon["Attribution Override"])
    # 心理動詞の判定
    is_psychological = any(v in text for v in lexicon["Psychological Verbs"])
    
    if is_reported:
        return "Third-Person"
    elif is_psychological:
        return "First-Person"
    return "Neutral"
