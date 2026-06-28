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
