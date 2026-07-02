import json
from rules.stage1_rule import determine_subject
from rules.stage3_rule import analyze_causality
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
        # 1. まず判定する
        subject_status = determine_subject(text)  # Stage 1 の判定を追加
        causality_status = analyze_causality(text) # Stage 3 の判定を追加

        # 2. その結果を使って、analyzerでログを作る
        log1 = analyzer.stage1_analyze(text, subject_status)
        log3 = analyzer.stage3_analyze(text, log1)
        
        print(f"Input: {text}")
        print(f"Result: {log1}") 
        print(f"Result: {log3}") 

        
if __name__ == "__main__":
    # 正しいデータファイルの場所を指定して実行
    run_test('/workspaces/context-aware-inference-engine/data/examples/stage1_input.json')
    run_test('/workspaces/context-aware-inference-engine/data/examples/stage3_input.json')