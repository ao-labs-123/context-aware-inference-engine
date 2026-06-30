import json
from rules.stage1_rule import determine_subject

# 例文ファイルを読み込む
def run_test(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        examples = json.load(f)
    
    for text in examples:
        result = determine_subject(text)
        print(f"Input: {text}")
        print(f"Result: {result}")
        print("-" * 30)

if __name__ == "__main__":
    run_test('data/examples/stage1_input.json')
