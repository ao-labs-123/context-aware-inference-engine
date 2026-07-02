# Stage1 — Resolving First-Person Omitted Subjects in Dialogue AI

## Overview:
This step focuses on optimizing the model's ability to interpret sentences with implicit subjects. By codifying linguistic patterns—such as the way psychological verbs (e.g., 'think', 'feel', 'notice') consistently map to the speaker as the primary agent—the model eliminates ambiguity in subject identification and significantly increases conversational accuracy, regardless of the underlying language.

## Key Points:

1. Explicit Subject Priority:

   When an explicit subject is present in the sentence (e.g., "I," "He," "The company"), the model bypasses inference heuristics and directly assigns the specified agent. This acts as the highest-priority deterministic rule.

2. Psychological Verb Default for Omitted Subjects:

   When a psychological verb (e.g., 'think', 'feel', 'want', 'hope', 'stressed') appears without an explicit subject, assign the speaker as the agent by default.

3. Evidentiality & Attribution Override:

   If a sentence contains markers of evidentialities or indirect speech (e.g., 'seemingly', 'allegedly', 'they say', 'I heard', 'it is told'), treat the agent as a second or third party, overriding the speaker-default.


## Logic Comparison: Implicit Subject vs. Evidential Override

| Input | Logic Process | Result |
| --- | --- | --- |
| "Thought was strange." | Psychological Verb + Null Subject → [Default: Speaker] | AI assigns "I" as the agent. |
| "Thought it was strange apparently." | Psychological Verb + Null Subject + Evidential Marker → [Override: 3rd Party] | AI assigns "He/She/They" as the agent. |
