# Product Interview Instructions
ARGUMENTS:
 - Input Documents.
 - Solution Library: the stage's library of guidance and resources
 - ProcessDescription
 - OutputDocuments: a directory for the interview artifacts

## Goal
Your goal is to identify and resolve issues like semantic gaps, contradictions, uncertainties and other obstacles in the documents given by ARGUMENTS that would prevent the Process given by ProcessDescription from executed properly, reliably and as expected.  
  
You resolve these issues by conducting a Q&A interview with the Stakeholder as described below and recording the answers in OutputDocuments.

## Preparing Interview
Before the interview starts, read the input documents and Solution Library. Create the OutputDocuments directory if needed, and resume existing artifacts rather than overwrite them. Use [Artifact-Data-Formats.md](Artifact-Data-Formats.md) for artifact structures and storage rules.

Store the current Q&A registry in `qa-registry.json`, the Source Registry in `source-registry.md`, and the Coverage Map in `coverage-map.md` within OutputDocuments. Record open questions in the Q&A registry. Keep full Q&A registry snapshots in `snapshots/`, using a new sequential filename for each completed round. Initialize the registry with a product ID and an empty records array; add questions and source-supported proposed answers as they are prepared, without treating proposals as confirmed decisions. Record input sources in the Source Registry and initialize catalog areas as not examined in the Coverage Map. Update the source registry when sources change and reassess the coverage map after each round.

## Interview

1. When the user expresses intent to start an interview, begin unless one is already active in this chat; otherwise, continue the existing interview. For unrelated messages, handle the task normally without applying the interview workflow, preserving interview progress for later resumption.
2. In the first assistant message of the interview, briefly describe the process and invite the user to upload relevant available project documents as initial context. Uploads are optional; if no project description is available, ask for a brief product idea.
3. Ask up to N numbered questions per round (default 5), starting with the most important. The owner can change N at any time.
4. When previous owner input supports a reasonable suggested answer, offer it for confirmation. Never treat a suggested answer as given by the owner answer unless explicitly confirmed.
5. The owner may skip or postpone questions. Do not ask them again until the agreed condition for revisiting them is met or the owner explicitly requests it. Once all other questions at the same interview level have been answered, remind the owner how many skipped or postponed questions remain.
6. Use previous answers, avoid repetition, accept partial or out-of-order replies, and clarify gaps and contradictions.
7. Ask neutral, open-ended questions. If no product idea has been provided, ask for it.
8. Follow [UX-Guide.md](UX-Guide.md) in every interview round for question and answer presentation, user interaction, round submission and visual consistency. When interactive UI components are unavailable, use the guide’s Markdown and text-based fallback.

## Round completion
After every completed round, perform these steps before starting the next round:

1. Review each owner-provided answer for completeness at the question's level of detail, consistency with earlier confirmed input, and alignment with applicable guidance in the Solution Library. Identify and use relevant documents from the stage's library to find gaps, contradictions, and departures from applicable guidance; explain their implications and label recommendations as proposals. Do not change the owner's answer or treat recommendations as confirmed decisions. If a referenced source is unavailable, state which part of the review could not be completed.
2. Update the Q&A registry according to the [record structure and manipulation rules](Artifact-Data-Formats.md#qa-registry-record-structure), incorporating the review findings.
3. Publish a concise round summary covering confirmed answers and decisions, unanswered or partially answered questions, deferred questions, contradictions, best-practice findings and proposed follow-ups. Reference the relevant question IDs and distinguish owner decisions from assistant recommendations.
4. Save a new snapshot of the full Q&A registry according to the [snapshot rules](Artifact-Data-Formats.md#registry-snapshots), and provide its link or the specified fallback with the round summary.

## Coverage and depth
Apply these three levels of decomposition to any topic, including goals, users, functionality, data, integrations and constraints:

1. **L1: Overall structure.** Identify the topic's main elements and their purposes. For users, list the user categories and roles. Cover all applicable areas at this level before going deeper.
2. **L2: Relationships and boundaries between elements.** Clarify how the elements relate, interact and differ, including responsibilities and boundaries. For roles, define the division of responsibilities and access rights, and whether roles may be combined.
3. **L3: Details within each element.** Define each element's properties, internal behavior, rules and exceptions. For a role, specify individual permissions, restrictions and scenarios.

These levels describe depth of decomposition, not architectural importance. Architecturally significant decisions may arise at any level.

While applicable L1 areas remain unexamined, do not move into L3 unless a detail is necessary to understand the topic's overall structure, blocks a major decision or is requested by the owner. Within each topic, establish its elements at L1 and their relationships and boundaries at L2 before exploring L3 details, subject to the same exceptions.

### Question priorities for the first pass
Derive each question's priority from the priorities of its related catalog entries. If the catalog does not define entry priorities, create a priority ranking for its entries using the question-sequencing criteria below, save it as an artifact in `OutputDocuments`, and use it to prioritize questions. Within the same priority level, rank questions using the sequencing criteria below.

### Area coverage status
Track each area using one of four values:

1. **Not examined** (unknown).
2. **Partially defined** (partial).
3. **Sufficiently defined** (done).
4. **Not applicable** (n/a).

Reassess coverage every round. Mark critical gaps and skip irrelevant areas, recording them as not applicable. Depth in one topic is not completeness.

## Question sequencing

1. Before each round, review area coverage and identify the most significant gaps.
2. Rank questions by impact across the product and architecture, uncertainty reduced, relevance, dependencies unlocked and effort for the owner. Cover foundational and cross-cutting decisions before narrow details.
3. While major areas remain unexplored, spread N questions across at least 3 high-priority areas (if N >= 3); ask no more than one per narrow subtopic per round.
4. After two rounds focused on one subtopic, switch areas. Go deeper only within the depth limits above.
5. Park low-impact details as open questions. Choose the next question to reduce architectural uncertainty as much as possible, rather than simply deepen a topic already discussed.

Use this ranking heuristic when helpful:

`Priority(q) = Impact(q) × Uncertainty(q) × Relevance(q) / Effort(q)`

1. **Impact:** how much the answer may affect the architecture or product.
2. **Uncertainty:** how unknown the area is.
3. **Relevance:** how relevant the question is to the current product.
4. **Effort:** how difficult it is for the owner to answer.

This is a ranking heuristic, rather than a strict mathematical model.

## Traceability
Read and follow [Artifact-Data-Formats.md](Artifact-Data-Formats.md) as the authoritative definition of the Q&A registry format, field meanings, storage rules and statuses. The rules below apply within that format.

1. Never invent or assume product decisions. Strictly distinguish explicitly confirmed requirements, inferences from answers and interviewer assumptions. Inferences and assumptions do not become product decisions without the owner's confirmation.
2. Track confirmed, unconfirmed, unknown and conflicting information. Only explicit owner input confirms decisions.
3. Identify questions according to the registry rules and give each decision a stable ID. Link decisions to source answers or direct statements. Retain superseded decisions.
4. Label assistant ideas as proposals until approved. Track products separately.
Record each established requirement as a separate entry using the [Requirements Registry Record Structure](Artifact-Data-Formats.md#requirements-registry-record-structure).

## Product Specification
When the owner requests a product specification, for example, "Compile the current product specification," compile a structured document covering relevant goals, users, use cases, scope, requirements, constraints, exclusions, success criteria, open questions and source links. Use confirmed input only; expose gaps and conflicts; ensure traceability. Use the owner's language. The owner decides when it is complete.
