# Stage 5 — Parsing Case Relationships
## Overview:
This final structural layer standardizes the relationship between nouns and verbs. Building upon the agent identification (Stage 1), causal mapping (Stage 3), and modification parsing (Stage 4), this step specifically resolves passive voice constructions. It ensures the AI correctly maps the "receiver" and the "actor" even in complex or elliptical passive forms.

## Key Points:
**1. Passive Voice Mapping**:
The system identifies the structure ⁠[Subject] + [be/get] + [V-en] + [by-agent]⁠. It assigns the grammatical subject as the "receiver" and the noun following "by" as the "actor," effectively reversing the active voice mapping established in Stage 1.

**2. Elliptical Passive Resolution (Agentless Passive)**:
When the "by-agent" is omitted, the model analyzes the sentence context. If the action is logically consistent, it defaults the grammatical subject as the receiver.

**3. Role Consistency**:
By explicitly defining the receiver and actor, this step eliminates confusion in sentences where the speaker is the subject but not the primary cause of an action, preventing misattribution of responsibility.
