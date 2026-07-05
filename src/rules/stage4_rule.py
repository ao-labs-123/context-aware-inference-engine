import json

def analyze_modification_structure(text):
    text_clean = text.strip()
    
    # 1. 非制限用法 (Non-defining clause) の判定: ", which" や ", who"
    if ", which" in text_clean or ", who" in text_clean:
        marker = ", which" if ", which" in text_clean else ", who"
        
        # マーカーで分割して要素を抽出
        parts = text_clean.split(marker)
        antecedent = parts[0].strip()  # カンマの前の名詞節
        
        # 節の後ろの残り（is done. など）を削って節の中身だけを抽出
        clause_content = parts[1].split(",")[0].strip()
        
        return {
            "type": "Non-defining",
            "antecedent": antecedent,
            "clause": clause_content
        }
        
    # 2. 制限用法 (Defining clause) の判定: " that " や " which " (カンマなし)
    for marker in [" that ", " which ", " who "]:
        if marker in text_clean and f",{marker.strip()}" not in text_clean:
            parts = text_clean.split(marker)
            antecedent = parts[0].strip()
            
            # 主節の動詞（is, wasなど）の手前までを関係節の中身とする簡易パース
            # 完璧なNLPを入れず、まずは空白区切りの動詞の手前までを取得
            clause_parts = parts[1].split()
            # "is", "was", "has" などの主節の助動詞・動詞の手前までを切り出す
            clause_words = []
            for word in clause_parts:
                if word in ["is", "was", "are", "were", "has", "have", "done"]:
                    break
                clause_words.append(word)
            
                clause_content = " ".join(clause_words).replace(".", "").strip()
            
            return {
                "type": "Defining",
                "antecedent": antecedent,
                "clause": clause_content
            }
            return None
