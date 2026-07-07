import json
from rules.stage1_rule import determine_explicit_subject
from rules.stage1_rule import determine_subject
from rules.stage2_rule import analyze_causality_and_ambiguity
from rules.stage3_rule import analyze_causality
from rules.stage4_rule import analyze_modification_structure
from rules.stage5_rule import analyze_semantic_structure
from analyzer import LogicAnalyzer

def run_test(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        examples = json.load(f)
    
    from rules.stage1_rule import get_lexicon
    from rules.stage3_rule import get_lexicon
    lexicon_data = get_lexicon()
    analyzer = LogicAnalyzer(lexicon_data)

    # main.py のループ内
    for text in examples:
        explicit_status = determine_explicit_subject(text)
        
        if explicit_status:
            subject_status = explicit_status
        else:
            subject_status = determine_subject(text)
            
        # 因果関係の判定は主語の有無に関わらず共通で実行
        causality_status = analyze_causality(text)

        mod_res = analyze_modification_structure(text)
        sem_res = analyze_semantic_structure(text)

        stage2_res = analyze_causality_and_ambiguity(text,subject_status)

        log1 = analyzer.stage1_analyze(text, subject_status)
        log2 = analyzer.stage2_analyze(text,log1,stage2_res)
        log3 = analyzer.stage3_analyze(text, log1)
        log4 = analyzer.stage4_analyze(text, mod_res,log1)
        log5 = analyzer.stage5_analyze(text, mod_res,log1)

        import os

    from datetime import datetime

    # ループの最後で、保存用の構造化データを作る
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "input": text,
        "stage1": log1,
        "stage2": log2,
        "stage3": log3,
        "stage4": log4,
        "stage5": log5
    }
    
    # data/log.json に追記するロジック
    log_file_path = "data/log.json"
    
    # ディレクトリがない場合は自動作成
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    
    # 既存のログを読み込む（ファイルがない、または空なら空リスト）
    existing_logs = []
    if os.path.exists(log_file_path) and os.path.getsize(log_file_path) > 0:
        try:
            with open(log_file_path, "r", encoding="utf-8") as f:
                existing_logs = json.load(f)
        except json.JSONDecodeError:
            existing_logs = []
            
    # 新しいログを末尾に追加
    existing_logs.append(log_entry)
    
    # きれいに整形（indent=2）して保存
    os.makedirs(os.path.dirname(log_file_path),exist_ok=True)
    with open(log_file_path, "w", encoding="utf-8") as f:
        json.dump(existing_logs, f, ensure_ascii=False,indent=4)
        
if __name__ == "__main__":
    # 正しいデータファイルの場所を指定して実行
    run_test('/workspaces/context-aware-inference-engine/data/examples/stage1_input.json')
    run_test('/workspaces/context-aware-inference-engine/data/examples/stage2_input.json')
    run_test('/workspaces/context-aware-inference-engine/data/examples/stage3_input.json')
    run_test('/workspaces/context-aware-inference-engine/data/examples/stage4_input.json')
    run_test('/workspaces/context-aware-inference-engine/data/examples/stage5_input.json')