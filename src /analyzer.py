#analyzer.py

class LogicAnalyzer:
    def __init__(self, lexicon_data):
        self.lexicon = lexicon_data
        
    def stage1_analyze(text, lexicon):
        is_reported = any(m in text for m in lexicon["Attribution Override"])
        is_psychological = any(v in text for v in lexicon["Psychological Verbs"])
        
        if is_reported:
            return {
            "process": "Psychological Verb + Null Subject + Evidential Marker",
            "decision": "Override: 3rd Party",
            "agent": "He/She/They"
            }
        
        elif is_psychological:
            return {
            "process": "Psychological Verb + Null Subject",
            "decision": "Default: Speaker",
            "agent": "I"
            }
            return {
            "process": "Standard", "decision": "None", "agent": "Unknown"
            }
