# Stage 5: Noun Case Relation Estimation

## Objective
Stage 5 aims to explicitly estimate case relations between nouns in a sentence,
clarifying semantic roles such as:
	•	Agent (who)
	•	Object (what)
	•	Recipient (to whom)
	•	Location (where)
	•	Means / Purpose

This step stabilizes sentence-level meaning interpretation and prevents semantic misreading.

## Background
Traditional morphological or dependency parsing can identify grammatical links,
but often fails to determine semantic roles accurately.

This stage reinterprets:
	•	noun + particle + verb combinations
into explicit semantic case relations, closer to human language understanding.

## Process
	•	Use particles (ga, wo, ni, de, e, kara, made, etc.) as primary cues
	•	Map noun-verb relations to semantic case frames
	•	Validate consistency with verb semantics
	•	Reduce confidence instead of forcing interpretation when ambiguity remains

## Benefits
	•	Reduced dialogue misunderstanding
	•	Improved machine translation accuracy
	•	More natural speech synthesis
	•	Structural detection of scam or misleading messages

