# rules/stage1_rule.py
import json

def is_psychological_verb(word):
    with open('src/lexicon/psychological_verbs.json', 'r') as f:
        verbs = json.load(f)
    return word in verbs

def check_attribution(text):
    # Attribution Overrideの判定ロジックをここに書く
    pass
