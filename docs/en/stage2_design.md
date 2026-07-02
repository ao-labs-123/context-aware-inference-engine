# Stage 2 — Clarification Requests for Undetermined Agents

## Overview:
This step functions as an intelligent fallback mechanism. When Stage 1's deterministic mapping fails to resolve a subject—or when multiple potential agents remain equally valid after contextual analysis—the model triggers a targeted, natural-language clarification request. This mirrors human conversational behavior by only intervening when ambiguity exceeds a manageable threshold.

## Key Points:
**1. Threshold-Based Trigger**:

The system initiates a clarification request only when the confidence score for agent identification is low or when the syntax contains multiple, equally plausible subjects that cannot be resolved through linguistic patterns alone.
* **Missing Core Markers:** A clarification request is strictly required when a sentence features **no explicit subject, no psychological verbs, and no evidential markers** (e.g., plain/ambiguous factual statements).

**2. Minimalist Intervention**:

To maintain natural flow, the inquiry is limited to the specific ambiguity. The model avoids exhaustive questioning, opting for contextual re-confirmation (e.g., "Are you referring to yourself or [mentioned party]?").

**3. Human-Centric Reliability**:

By acknowledging that some sentences are genuinely ambiguous even to human listeners, this step prevents the AI from making inaccurate assumptions, thereby ensuring data integrity and user trust.

| Input | Logic Process | Result |
| :--- | :--- | :--- |
| "Thought was strange." | Psychological Verb + Null Subject $\rightarrow$ [Default: Speaker] | AI assigns "I" as the agent. |
| "Thought it was strange apparently." | Psychological Verb + Null Subject + Evidential Marker $\rightarrow$ [Override: 3rd Party] | AI assigns "He/She/They" as the agent. |
| "Succeeded because you helped." | Null Subject + No Psychological Verb + No Evidential Marker $\rightarrow$ [Fallback: Ambiguous] | AI triggers Stage 2 clarification (Undetermined agent). |
