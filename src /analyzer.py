# analyzer.py

class LogicAnalyzer:
    def __init__(self, lexicon_data):
        self.lexicon = lexicon_data

    def stage1_analyze(self, text, subject_result):
        # stage1_rule.py で判定した結果（"Third-Person" など）を subject_result で受け取ります
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
