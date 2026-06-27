# Stage1 — Resolving First-Person Omitted Subjects in Dialogue AI

## Overview:
This step focuses on optimizing the model's ability to interpret sentences with implicit subjects. By codifying linguistic patterns—such as the way psychological verbs (e.g., 'think', 'feel', 'notice') consistently map to the speaker as the primary agent—the model eliminates ambiguity in subject identification and significantly increases conversational accuracy, regardless of the underlying language.

## Key Points:
1.	Psychological Verb Default:

	When a psychological verb(e.g., 'think', 'feel', 'want', 'hope')appears without an explicit subject, assign the speaker as the agent by default.
	
2.	Evidentiality & Attribution Override:

	If a sentence contains markers of evidentiality or indirect speech (e.g.,'seemingly', 'allegedly', 'they say', 'I heard', 'it is told'),treat the agent as a second or third party, overriding the speaker-default.
	
3.	Ambiguity Reduction:

	This deterministic mapping effectively resolves subject ambiguity in informal, context-heavy dialogue, serving as the foundation for multi-stage logical inference.

## Example:
	•	「変だと思った。」
	→ The subject is the speaker.
	•	「彼が変だと思ったらしい。」
	→ The subject is 彼 (he), not the speaker.
