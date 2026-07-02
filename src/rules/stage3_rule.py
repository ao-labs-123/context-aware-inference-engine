
import json

def get_lexicon():
    with open('/workspaces/context-aware-inference-engine/src/lexicon/causality_markers.json', 'r') as f:
        causality_list = json.load(f)
    return causality_list

def analyze_causality(text):
    lexicon = get_lexicon()

    is_causal = any(marker.lower() in text.lower() for marker in lexicon)
    return is_causal
