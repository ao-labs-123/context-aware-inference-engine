import json

def get_lexicon():
    with open('/workspaces/context-aware-inference-engine/src/lexicon/psychological_verbs.json', 'r') as f:
        verbs = json.load(f)
    with open('/workspaces/context-aware-inference-engine/src/lexicon/attribution_markers.json', 'r') as f:
        markers = json.load(f)
    
    # 結合したデータをデバッグ表示
    combined = {**verbs, **markers}
    print(f"DEBUG: Combined Lexicon Keys: {combined.keys()}")
    return combined

def determine_explicit_subject(text):
    explicit_subjects = ["I", "He", "She", "They", "We", "You", "It"]
    
    # テキストを単語に分解（先頭の主語を見つけるため）
    words = text.strip().split()
    if not words:
        return None
        
    first_word = words[0].replace(",", "").replace(".", "") # カンマなどの除去
    
    # 1. 先頭の単語が主語リストにある場合（例: "He succeeded...", "I succeeded...")
    if first_word in explicit_subjects:
        return first_word
        
    # 2. "I'm stressed..." のようなアポストロフィ付きの短縮形を救済
    if first_word.startswith("I'm"):
        return "I"
        
        return None

def determine_subject(text):
    lexicon = get_lexicon()
    words = text.lower().replace('.', '').split()
    
    # 伝聞マーカーの判定
    is_reported = any(m.lower() in text.lower() for m in lexicon["Attribution Override"])
    # 心理動詞の判定
    is_psychological = any(v.lower() in text.lower() for v in lexicon["Psychological Verbs"])
    
    if is_reported:
        return "Third-Person"
    elif is_psychological:
        return "First-Person"
        return "Neutral"
