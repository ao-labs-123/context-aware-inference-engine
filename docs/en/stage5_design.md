# Stage 5 — Parsing Case Relationships & Aspect Logic
## Overview:
This final structural layer standardizes the relationship between nouns, verbs, and their aspectual properties. Building upon previous stages, this step resolves passive voice constructions and distinguishes between static and dynamic states based on the presence of the ⁠-ing⁠ suffix.

## Key Points:
**1. Passive Voice Mapping**:
The system identifies the structure ⁠[Subject] + [be/get] + [V-en] + [by-agent]⁠. It assigns the grammatical subject as the "receiver" and the noun following "by" as the "actor." If the "by-agent" is omitted, it assumes the grammatical subject as the receiver if logically consistent.

**2. Aspectual Distinction (Static vs. Dynamic)**:
The model evaluates the presence of the ⁠-ing⁠ suffix to determine the verb's nature:
- Dynamic Verbs (with -ing): Interpreted as active processes or ongoing actions.
- Stative Verbs (without -ing): Interpreted as persistent states or conditions.
This distinction prevents the model from incorrectly assigning "agentive force" to static descriptions.


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
