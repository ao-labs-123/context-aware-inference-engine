# analyzer.py

class LogicAnalyzer:
    def __init__(self, lexicon_data):
        self.lexicon = lexicon_data

    def stage1_analyze(self, text, subject_result):
    
        if not subject_result:
            return {
                "process": "Null Subject",
                "decision": "Clarification Required",
                "agent": "Unknown"
            }
            
        if isinstance(subject_result, dict) and subject_result.get("structure_type") == "FormalSubject":
            true_agent = subject_result.get("true_agent")
            predicate = subject_result.get("predicate")
            
            return {
                "process": f"Formal Subject Detected (It ... that)",
                "decision": "Priority: True Subject in Clause",
                "agent": true_agent,
                "structure": f"It is [{predicate}] that [{subject_result.get('that_clause')}]"
            }


        if subject_result in ["I", "He", "She", "They", "We", "You", "It"] or (subject_result and subject_result.startswith(("The", "A", "An"))):
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

    def stage4_analyze(self, text, modification_result, log1):
        # 1. 完全に None だった場合、または辞書が空だった場合はここで安全に弾く
        if modification_result is None or modification_result == {}:
            return {
                "process": "Standard",
                "decision": "None",
                "structure": "No relative clause found"
            }
            
        # 2. Stage 1 のログからエージェント（主語）を安全に取得
        agent = log1.get("agent", "Unknown") if log1 else "Unknown"
        
        # 3. 非制限用法の判定ルート
        if modification_result.get("type") == "Non-defining":
            return {
                "process": "Non-defining clause",
                "decision": "Supplementary",
                "result": f"AI treats '{modification_result['clause']}' as an attribute, not the primary identifier."
            }
            
        # 4. 制限用法の判定ルート
        elif modification_result.get("type") == "Defining":
            # 節の中に "I" が含まれるか、Agent が "I" の場合
            if agent == "I" or "I" in modification_result.get("clause", ""):
                agent_note = f"links '{agent}' (Agent) to the specific {modification_result['antecedent'].lower()} as a defining marker."
            else:
                agent_note = f"defines the primary identity of '{modification_result['antecedent']}'."
                
            return {
                "process": "Defining clause",
                "decision": "Essential",
                "result": f"AI {agent_note}"
            }

    
    def stage5_analyze(self, text, semantic_result,log1):
        if semantic_result is None:
            return {
                "process": "Standard",
                "decision": "None",
                "result": "Could not analyze semantic structure."
            }
            
        form_type = semantic_result.get("form")
        verb = semantic_result.get("verb", "").lower()
        
        # 状態動詞か動作動詞かを判定する簡易辞書ルール
        # ※本来は lexicon ファイル等から読み込んでも良いです
        stative_verbs = ["have", "has", "had", "know", "knows", "knew", "love", "loves", "like", "likes"]
        
        is_stative = any(v in verb for v in stative_verbs)
        category = "Stative" if is_stative else "Action"
        
        # 形態（Form）に応じたロジック処理と出力結果の生成
        if form_type == "Base":
            process_log = f"[Morphology: Base] → [Category: {category}]"
            if category == "Stative" and verb in ["have", "has", "had"]:
                result_log = "Possession status."
            else:
                result_log = f"General {category.lower()} statement."
                
            return {
                "process": process_log,
                "result": result_log
            }
            
        elif form_type == "Progressive":
            # have が進行形（having）になると Stative から Action（意味の変容）に抽象化される
            if "hav" in verb:
                category = "Action"
                result_log = "Active event participation."
            else:
                result_log = f"In-progress {category.lower()} event."
                
            return {
                "process": f"[Morphology: be + V-ing] → [Category: {category}]",
                "result": result_log
            }
            
        elif form_type == "Passive":
            actor = semantic_result.get("actor")
            receiver = semantic_result.get("receiver")
            
            return {
                "process": "[Passive: be + V-en + by]",
                "result": f"Actor: {actor} / Receiver: {receiver}."
            }
            
        return None
