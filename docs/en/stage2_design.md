# Stage 2 — Clarification Requests for Undetermined Agents

## Overview:
This step functions as an intelligent fallback mechanism. When Stage 1's deterministic mapping fails to resolve a subject—or when multiple potential agents remain equally valid after contextual analysis—the model triggers a targeted, natural-language clarification request. This mirrors human conversational behavior by only intervening when ambiguity exceeds a manageable threshold.

## Key Points:
**1. Threshold-Based Trigger**:
The system initiates a clarification request only when the confidence score for agent identification is low or when the syntax contains multiple, equally plausible subjects that cannot be resolved through linguistic patterns alone.

**2. Minimalist Intervention**:
To maintain natural flow, the inquiry is limited to the specific ambiguity. The model avoids exhaustive questioning, opting for contextual re-confirmation (e.g., "Are you referring to yourself or [mentioned party]?").

**3. Human-Centric Reliability**:
By acknowledging that some sentences are genuinely ambiguous even to human listeners, this step prevents the AI from making inaccurate assumptions, thereby ensuring data integrity and user trust.
