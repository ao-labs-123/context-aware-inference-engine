import json
from rules.stage1_rule import determine_explicit_subject
from rules.stage1_rule import determine_subject
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
        mod_res = analyze_semantic_structure(text)

        log1 = analyzer.stage1_analyze(text, subject_status)
        log3 = analyzer.stage3_analyze(text, log1)
        log4 = analyzer.stage4_analyze(text, mod_res,log1)
        log5 = analyzer.stage5_analyze(text, mod_res,log1)

        print(f"Input: {text}")
        print(f"Result: {log1}") 
        print(f"Result: {log3}") 
        print(f"Result: {log4}")
        print(f"Result: {log5}")

        
if __name__ == "__main__":
    # 正しいデータファイルの場所を指定して実行
    run_test('/workspaces/context-aware-inference-engine/data/examples/stage1_input.json')
    run_test('/workspaces/context-aware-inference-engine/data/examples/stage3_input.json')
    run_test('/workspaces/context-aware-inference-engine/data/examples/stage4_input.json')
    run_test('/workspaces/context-aware-inference-engine/data/examples/stage5_input.json')