# Stage 5 — Parsing Case Relationships & Verb Classification
## Overview:
This structural layer standardizes the relationship between nouns and verbs, and differentiates verb states. Building upon the previous stages, it resolves passive voice constructions and applies morphological analysis to distinguish between stative and action (dynamic) verbs, ensuring precise temporal and agency mapping.

## Key Points:
**1. Passive Voice Mapping**:

The system identifies the structure ⁠[Subject] + [be/get] + [V-en] + [by-agent]⁠. It assigns the grammatical subject as the "receiver" and the noun following "by" as the "actor." If "by" is omitted, the grammatical subject is defaulted as the receiver, provided the interpretation remains logically consistent.

**2. Morphological Verb Classification**:

The model utilizes morphological analysis to determine verb type based on the presence of the ⁠-ing⁠ suffix:
- Dynamic/Action Verb Detection: If the verb appears in the progressive form (⁠be + V-ing⁠), it is classified as an action (e.g., "I am understanding the concept" → active cognitive process).
- Stative Verb Detection: Verbs appearing in their base form (e.g., "I understand") are treated as states. For verbs like understand or have, the presence of ⁠be + V-ing⁠ triggers a dynamic interpretation, overriding the static default.
 
**3. Lexicon-Based Exception Handling**:

For irregular cases (e.g., "stand" as a posture vs. "stand" as a situation), the system references a dedicated ⁠lexicon⁠ to determine whether the verb should be parsed as a state or an action regardless of standard morphology.


## Logic Comparison: Case Relation Parsing

| Input | Logic Process | Result |
|--|--|--|
| "The report was finished by him." | [Receiver: Report] + [Actor: Him] | AI maps: "Him" (Actor) performed action on "Report" (Receiver). |
| "The report was finished." | [Subject: Report] + [Passive/No Actor] | AI recognizes "Report" as the receiver (Agent is unknown/omitted). |
| "I got promoted." | [Receiver: I] + [Passive/No Actor] | AI maps "I" as the receiver of the action "promote". |

## Example of Case Relation Tracking:
 **Input**: "The decision was made by the board, and I was informed later."
 
 **Analysis**:
 - Passive 1: "The decision (Receiver) was made by the board (Actor)."
 - Passive 2: "I (Receiver) was informed (Action)."
 
 **AI Understanding**: The AI maintains two distinct relationships: the board acting on the decision, and an unspecified actor informing the speaker. This prevents the speaker from being incorrectly identified as the one who made the decision.
