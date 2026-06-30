import json
from rules.stage1_rule import determine_subject
from analyzer import LogicAnalyzer

def run_test(input_file):
    # 1. データを読み込む
    with open(input_file, 'r', encoding='utf-8') as f:
        examples = json.load(f)
    
    # 2. 辞書データ（レキシコン）を stage1_rule から持ってくる
    # (stage1_rule.pyのget_lexiconをここで呼ぶか、Analyzerに渡す準備)
    from rules.stage1_rule import get_lexicon
    lexicon_data = get_lexicon()
    analyzer = LogicAnalyzer(lexicon_data)

    # 3. 1件ずつ判定して画面に表示する
    for text in examples:
        # あなたが作った判定ロジックを動かす
        subject_result = determine_subject(text)
        
        # analyzer.py に結果を渡して、最終的なプロセスとエージェントを取得
        final_result = analyzer.stage1_analyze(text, subject_result)
        
        print(f"Input: {text}")
        print(f"Result: {final_result['agent']} ({final_result['decision']})")
        print("-" * 30)

if __name__ == "__main__":
    # 正しいデータファイルの場所を指定して実行
    run_test('/workspaces/context-aware-inference-engine/data/examples/stage1_input.json')
