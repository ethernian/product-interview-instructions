# Artifact Data Formats

This document defines artifact data structures, formats, and storage rules for the product information and interview process and for use by external systems. The [Product Information Management Instructions](Product-Information-Management-Instructions.md) govern how the records are used.

## Product Information Registry Record Structure

Maintain one versioned Product Information Registry per product, shared across stages. Its `records` array contains both question records and significant decision records; these are record types in the same registry, not separate registries. Use `product-information-registry.json` at the location configured for the product. During discovery, default to `OutputDocuments/product-information-registry.json` only when no existing product registry is configured. If a configured registry is missing or unreadable, report it and ask the responsible actor before creating a replacement. Other stages must use the same registry, not create stage-local copies. Keep products separate.

The registry is a JSON object with `product_id` and `records`. Each record has an `id` that is unique and immutable within the registry across both record types, and a `type` of `question` or `decision`. All fields listed for that type are required; use `null` for unavailable optional strings or timestamps and `[]` for empty arrays. Preserve unmapped legacy fields in an additional `legacy_data` object on the relevant record. Links to source documents and messages may appear in Markdown text. Use RFC 3339 timestamps with a UTC offset.

### Question Records

Each question record has the following fields:

| Field | Purpose |
|---|---|
| `id` | Stable question ID, e.g., `Q-005` |
| `type` | `question` |
| `detail_level` | `L1` overall composition and structure, `L2` relationships and boundaries between elements, or `L3` detailed internal structure of each element |
| `catalog_refs` | Array of relevant catalog references |
| `question_subject` | Subject of the question |
| `question_text` | The question as presented |
| `proposed_answer` | Assistant proposal, or `null`; not an owner answer until explicitly confirmed |
| `user_answer` | Owner's current direct or explicitly confirmed answer, or `null` |
| `answer_source` | Source of the answer and actor, or `null` if not recorded |
| `status` | Answer completeness: `unanswered`, `partially_answered`, `answered`, or `deferred` |
| `interpreted_as` | Optional array of agent interpretation labels; `[]` means no interpretation was assigned |
| `interpretation_note` | Agent's explanation, including which part of a mixed answer a label applies to, or `null` |
| `processing_notes` | Gaps, review findings, referral, and agreed revisit conditions, or `null` |
| `answered_at` | Timestamp of the current answer, or `null` |
| `last_interaction_at` | Timestamp of the latest question discussion, including deferral, or `null` before first presentation |

`interpreted_as` is an agent assessment, not owner approval, a decision status, or verification. Assign labels only when useful; examples include `estimate`, `uncertain`, `unclear`, `unknown`, `proposal`, and `decision`. Multiple labels are allowed. Preserve the owner's answer and its tentative or definitive wording. If an answer contains several statements, identify the relevant statement in `interpretation_note` and link any resulting decision records; do not force one interpretation onto the entire answer. Reassess interpretations when answers change. Explain material uncertainty and ask for clarification when needed. Record an owner's correction to the interpretation without changing their answer unless they also correct it. A factual statement is owner-reported, not independently verified merely because it was answered; do not require independent verification unless appropriate for its use. If verification occurs, record its evidence and source in `processing_notes`.

### Decision Records

Each significant decision or proposal is a separate `decision` record within the same `records` array. Routine execution choices within confirmed requirements and constraints do not require individual records.

| Field | Purpose |
|---|---|
| `id` | Stable decision ID, e.g., `D-001`, unique across all records |
| `type` | `decision` |
| `decision` | Choice made or proposed, or `null` if pending without a choice |
| `scope` | Stage or areas to which it applies |
| `context` | Circumstances and problem addressed |
| `rationale` | Why the choice was made or proposed |
| `decision_status` | `pending`, `proposed`, `confirmed`, `rejected`, or `superseded` |
| `responsible_actor` | Human stakeholder or process agent responsible for the choice |
| `confirmation_source` | Evidence of authorized confirmation or rejection, identifying the actor and, when acting for another actor, that actor and the source and scope of explicit delegation |
| `source_refs` | Array of strings containing source record IDs or document and message references |
| `affected_artifacts` | Array of links to affected requirements, designs, tasks, implementation, and other artifacts |
| `alternatives_considered` | Array of alternatives, where relevant |
| `consequences` | Expected effects and trade-offs, where relevant |
| `replacement_record` | Replacement decision ID when superseded, otherwise `null` |

Use `pending` for a decision to be made without a selected or proposed choice; `proposed` for a recorded but unconfirmed choice; `confirmed` only for a choice confirmed by an actor with the necessary authority, including an explicitly authorized delegate; `rejected` for a proposal rejected by such an actor; and `superseded` for a replaced decision, retaining its record and linking its replacement. A proposed, confirmed, rejected, or superseded record must identify the choice; record evidence of authorized confirmation or rejection in `confirmation_source`. Do not infer authorization or confirmation from an answer's completeness, an interpretation label, or an assistant proposal. A clear decision made directly by an authorized owner does not require a second confirmation. Preserve direct answers that are tentative as tentative. Link a decision to all relevant question records or other sources through `source_refs`; use the exact record ID for a registry source. One answer can inform several decisions and a decision can have several sources; find related decisions from a question by searching `source_refs` rather than maintaining duplicate reverse links. Decisions originating outside an interview need not have a question source. Non-decision facts remain owner-reported answers and do not require fabricated decision records.

Follow the [Decision Management rule](Product-Information-Management-Instructions.md#8-decision-management-and-conflict-resolution) for capturing, confirming, applying, and revising decisions.

### Example Registry

The references and data are illustrative. The question is answered, while the related decision remains proposed.

```json
{
  "product_id": "P-001",
  "records": [
    {
      "id": "Q-005",
      "type": "question",
      "detail_level": "L1",
      "catalog_refs": ["01.12"],
      "question_subject": "Users",
      "question_text": "How many users are expected?",
      "proposed_answer": "About 500 expected users.",
      "user_answer": "Probably around 500; maybe plan for 1,000 concurrent users.",
      "answer_source": "Owner interview",
      "status": "answered",
      "interpreted_as": ["estimate", "uncertain", "proposal"],
      "interpretation_note": "500 is an uncertain estimate; 1,000 concurrent users is a proposed capacity.",
      "processing_notes": null,
      "answered_at": "2026-11-06T14:30:00+01:00",
      "last_interaction_at": "2026-11-06T14:30:00+01:00"
    },
    {
      "id": "D-001",
      "type": "decision",
      "decision": "Support 1,000 concurrent users.",
      "scope": "Capacity",
      "context": "Proposed during the interview.",
      "rationale": null,
      "decision_status": "proposed",
      "responsible_actor": "Product owner",
      "confirmation_source": null,
      "source_refs": ["Q-005"],
      "affected_artifacts": [],
      "alternatives_considered": [],
      "consequences": null,
      "replacement_record": null
    }
  ]
}
```

### Storage Rules

- Only the current answer is stored in `user_answer`. A new answer replaces the previous one; a partial clarification updates the relevant part while preserving other explicitly confirmed information. Preserve history through full registry snapshots.
- Store the owner's direct answer in `user_answer` as given, preserving its tentative, partial, or unknown character. Copy an assistant proposal into it only after the owner's explicit confirmation. Never overwrite an owner answer with an interpretation or review finding.
- Update `answered_at` when the current answer is provided, changed, or explicitly confirmed. If there is no answer, both `user_answer` and `answered_at` are `null`. Update `last_interaction_at` when a question is first presented and on each subsequent discussion, including deferral; deferral alone does not change `answered_at` or remove an answer.
- Preserve a revisited question's `id` and position. The `records` array defines order: add new questions as one block at the beginning in presentation order, preserving existing record order. Insert new decision records after that block; if there is no new question block, insert decisions at the beginning in creation order. Preserve existing records and their order.
- Share the unified registry and snapshots only with actors authorized to access their contents. If access restrictions are unknown or cannot be maintained, ask the responsible actor before sharing sensitive information.
- On first use with existing legacy `qa-registry.json` or a separate decision registry, locate the existing product artifacts before creating a registry. Preserve the original files and snapshots. Prepare the imported registry separately and verify it against its sources before writing it to the new location. Import question and decision records into one registry without changing IDs, owner answers, decision statuses, authority evidence, source links, or history; add the new type and interpretation fields with empty defaults. Map legacy decision statuses Proposed, Confirmed, Rejected, and Superseded to the corresponding lowercase values. Preserve an unknown legacy status in `legacy_data` and ask the responsible actor how to map it; do not invent a status or write a record that violates the schema. Preserve any legacy fields that cannot be mapped without loss. Do not infer confirmation, discard conflicts, or overwrite an existing unified registry. If a unified registry already exists alongside legacy records, use the unified registry and report any unreconciled legacy data rather than silently ignoring it or merging it without authorization. If sources, ownership, required authority evidence, ID collisions, or mappings cannot be resolved safely, report the issue and ask the responsible actor before migration. Legacy snapshots remain available as history; do not claim they use the new schema.

### Status Rules

Keep answer completeness separate from decision status and best-practice alignment: a complete answer can contain an unconfirmed proposal or depart from recommended practice. Record review findings in `processing_notes` without replacing the owner's answer or treating recommendations as confirmed decisions. The assistant assigns answer status based on the owner's explicit response and the question's `detail_level`; if completeness is ambiguous, ask for clarification. The owner may correct the status.

| Status | Condition |
|---|---|
| `unanswered` | There is no owner answer; the assistant's proposal does not count as an answer |
| `partially_answered` | An answer has been received, but the question is not fully addressed; specific gaps must be listed in `processing_notes` |
| `answered` | The current answer covers the question at the specified level of detail |
| `deferred` | The owner has explicitly postponed the question; any previously received answer is preserved |

An explicit "I don't know" is a valid owner response, not a confirmed fact or decision; record the unknown, mark the answer `partially_answered` when required information is still missing, and leave coverage insufficient where the information is still needed. For `deferred`, record the agreed revisit condition in `processing_notes`, or state that none was agreed; do not invent one. Reassess status when discussion resumes.

### Registry Snapshots

After each completed interview round, save a new snapshot of the full unified registry after incorporating answers, interpretations, decisions, and review findings. Also snapshot after registry records change outside an interview round. Preserve previous snapshots in `snapshots/` next to the registry, using a new sequential filename. Use available storage or an external versioning system; snapshot version identifiers belong to that system, not individual records.

Provide a link to the saved version with the round summary or, for an out-of-round change, when reporting the change. If persistent storage is unavailable, provide the full updated registry as a downloadable artifact or JSON in chat and state that it has not been persistently saved. Do not claim that a snapshot was saved without a successful save.

## Requirements Registry Record Structure

Record each established requirement as a separate entry:

| Field | Purpose |
|---|---|
| Requirement ID | Unique identifier |
| Aspect | Catalog area |
| Statement | Requirement statement |
| Source Q&A | Reference to product information record IDs and the owner's answer or direct statement |
| Status | Confirmed, preliminary, unknown |
| Priority | Importance of the requirement |
| Architectural impact | Possible impact on the architecture |
| Dependencies | Related requirements |
| Open questions | What else needs clarification |

## Stage Completion Criterion Structure

Each Stage Completion Criterion defines a condition that stage outputs must meet before downstream use and identifies who confirms it and how.

| Field | Purpose |
|---|---|
| Condition | The condition that stage outputs must meet |
| Confirmation method | Manual confirmation or automatic check; the method does not itself grant confirmation authority |
| Responsible actor | The Human Stakeholder or Process Agent assigned to confirm the condition and possessing the necessary authority |
| Confirmation source | Evidence identifying the confirming actor and, when acting on another actor's behalf, that actor and the source and scope of the explicit delegation |

## Source Registry Record Structure

Each record identifies a source material and the information needed to assess and trace its use.

| Field | Purpose |
|---|---|
| Source | Reference to the source material |
| Provenance | Where the material came from |
| Version | The version of the material used |
| Reliability status | The assessed reliability of the material |

## Coverage Map Entry Structure

Each entry records the investigation status of one area.

| Field | Purpose |
|---|---|
| Area | The area being investigated |
| Status | Not examined (`unknown`), partially defined (`partial`), sufficiently defined (`done`), or not applicable (`n/a`) |

When resuming an existing map, preserve its information and interpret legacy `unexplored`, `partially defined`, `defined`, and `not applicable` values as `unknown`, `partial`, `done`, and `n/a`, respectively. Do not mark an area done solely because an owner responded that they do not know.
