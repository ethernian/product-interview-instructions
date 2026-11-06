# Data Structures and Formats

This document defines interview data structures, formats, and storage rules for further processing during development and use by external systems.

## Q&A Registry Record Structure

Each Q&A record corresponds to one question with a stable ID and the owner's latest answer.

| Field | Purpose |
|---|---|
| `id` | Question ID that is unique and immutable within the registry, e.g., `Q-005` |
| `detail_level` | Level of detail for any topic: `L1` — overview of its overall composition and structure; `L2` — relationships and boundaries between elements; `L3` — detailed internal structure of each element |
| `catalog_refs` | References to catalog aspects |
| `question_subject` | Subject of the question |
| `question_text` | Text of the question |
| `proposed_answer` | Markdown string containing the assistant's proposal; `null` if there is no proposal |
| `user_answer` | Markdown string containing the owner's current explicitly provided or confirmed answer; `null` if there is no answer |
| `status` | `unanswered`, `partially_answered`, `answered`, `deferred` |
| `processing_notes` | Markdown string: gaps in the answer, agreed conditions for revisiting the question, and to whom the question has been referred; `null` if there are no notes |
| `answered_at` | Date and time of the current answer, including the UTC offset; `null` if there is no answer |
| `last_interaction_at` | Date and time of the most recent discussion of this question, including the UTC offset; required field |

#### Registry Structure

Each registry belongs to one product. The `product_id` field is stored at registry level, and `records` contains its Q&A records.

| Field | Purpose |
|---|---|
| `product_id` | Product to which the registry belongs |
| `records` | List of Q&A records for this product |

### Example Registry with a Confirmed Answer

The data and message references in this example are illustrative.

```json
{
  "product_id": "P-001",
  "records": [
    {
      "id": "Q-005",
      "detail_level": "L1",
      "catalog_refs": [
        "01.12"
      ],
      "question_subject": "MVP Scope",
      "question_text": "What must be included in the first version?",
      "proposed_answer": "Registration and project creation. See the [project brief](project-brief.md#scope).",
      "status": "answered",
      "last_interaction_at": "2026-11-06T14:30:00+01:00",
      "user_answer": "Registration, project creation, and inviting participants.",
      "processing_notes": null,
      "answered_at": "2026-11-06T14:30:00+01:00"
    }
  ]
}
```

### Storage Rules

- Every record includes all fields listed in the record table. An absent proposal, answer, or notes is represented by `null`; `catalog_refs` may be an empty array.
- Only the current answer is stored in `user_answer`. A new answer replaces the previous one. A partial clarification updates the relevant part of the current answer while preserving other explicitly confirmed information.
- History and versioning are managed by an external system across Q&A registry snapshots and are outside the scope of this level.
- The owner's direct answer is stored in `user_answer`. The assistant's proposal is copied there only after the owner's explicit confirmation; until then, it is stored separately in `proposed_answer`.
- Links to documents and messages are included directly in the Markdown text; separate reference fields are not used.
- `answered_at` is updated when the current answer is provided, changed, or explicitly confirmed. If there is no answer, both `user_answer` and `answered_at` are `null`.
- `last_interaction_at` is updated when the question is first presented and on every subsequent discussion, including deferral without changing the answer. Deferral alone does not change `answered_at` or remove an existing answer.
- When a question is revisited, its `id` and the record's position in `records` are preserved.
- Record order is defined by the `records` array. New questions are added to the beginning of the array as a single block in the order in which they were presented; the order of existing records is preserved.
- Use [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339.html) timestamps with a UTC offset.

### Status Rules

The assistant assigns the status based on the owner's explicit answer and how fully the question is addressed at its `detail_level`. If completeness is ambiguous, the assistant asks for clarification; the owner may correct the status.

| Status | Condition |
|---|---|
| `unanswered` | There is no owner answer; the assistant's proposal does not count as an answer |
| `partially_answered` | An answer has been received, but the question is not fully addressed; specific gaps must be listed in `processing_notes` |
| `answered` | The current answer covers the question at the specified level of detail |
| `deferred` | The owner has explicitly postponed the question; any previously received answer is preserved |

For `deferred`, the agreed condition for revisiting the question is recorded in `processing_notes`. If no condition has been agreed, this is stated explicitly; the assistant must not invent one. When discussion resumes, the status is reassessed based on the presence and completeness of the current answer.
