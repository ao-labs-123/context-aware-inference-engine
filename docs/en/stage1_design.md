# Stage1 — Resolving First-Person Omitted Subjects in Dialogue AI

## Overview:
This step focuses on optimizing the model's ability to interpret sentences with implicit subjects. By codifying linguistic patterns—such as the way psychological verbs (e.g., 'think', 'feel', 'notice') consistently map to the speaker as the primary agent—the model eliminates ambiguity in subject identification and significantly increases conversational accuracy, regardless of the underlying language.

## Key Points:
    1.	When a psychological verb appears without a subject,
	→ Assume the speaker as the subject.
	2.	If the sentence contains markers like
	「〜らしい」「〜と聞いた」「〜と言われた」
	→ Those imply second or third person, not the speaker.
	3.	This rule significantly reduces ambiguity in Japanese dialogue and is foundational for later stages of the system.

## Example:
	•	「変だと思った。」
	→ The subject is the speaker.
	•	「彼が変だと思ったらしい。」
	→ The subject is 彼 (he), not the speaker.
