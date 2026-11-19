# Product Information Management Instructions

## 1. Ownership

Requirements and other work items may be owned by Human Actor, and can't be changed by others without the owner’s authorization. It enforces separation of responsibilities, avoids the excessive human effort of repeatedly revalidating items repeatedly rewritten by AI Agents, and reduces the risk of unapproved AI-generated changes to requirements.  

## 2. Respect Actor Authority

1. **Respect Decision Authority.** Proposals and assumptions become confirmed decisions only through confirmation by an actor with the necessary authority. No actor may confirm an item in another actor's name without explicit delegation from that actor.
2. **Use only confirmed decisions.** Decisions may guide further work only after confirmation by the responsible actor or an explicitly authorized delegate.

## 3. Processing Priorities

1. **Effective Uncertainty Minimization.** Prioritize questions and requests that significantly affect dependent decisions. Record unknown parameters explicitly.
2. **Minimize Rework.** Identify contradictions and costly-to-change decisions before executing dependent work.
3. **Maximize Automation.** AI Agents take on the largest possible share of necessary work within their capabilities and authority. Involve Human Actors only when their information, judgment, or authority is needed, while minimizing the effort required from them.
4. **Minimize Maintenance Overhead.** Eliminate independently maintained duplicates of information. Enable automatic updates of dependent artifacts.

## 4. Product Development Principles

1. **Separation of Responsibilities.** Keep source information, requirements, architecture, and implementation separate. An artifact may be derived from multiple sources.
2. **Traceability.** Derived artifacts are linked to their sources through stable identifiers. These relationships are maintained when changes occur.
3. **Verifiability.** Every output has objective verification criteria. Selected solutions include documented justification.
4. **Controlled Uncertainty.** Missing information and contradictions block only the activities that critically depend on them.

## 5. Interview Artifact Handling

Store the current Q&A registry in `qa-registry.json`, the Source Registry in `source-registry.md`, and the Coverage Map in `coverage-map.md` within OutputDocuments. Record open questions in the Q&A registry. Keep full Q&A registry snapshots in `snapshots/`, using a new sequential filename for each completed round. Initialize the registry with a product ID and an empty records array; add questions and source-supported proposed answers as they are prepared, without treating proposals as confirmed decisions. Record input sources in the Source Registry and initialize catalog areas as not examined in the Coverage Map. Update the source registry when sources change and reassess the coverage map after each round.

## 6. Traceability
Read and follow [Artifact-Data-Formats.md](Artifact-Data-Formats.md) as the authoritative definition of the Q&A registry format, field meanings, storage rules and statuses. The rules below apply within that format.

1. Never invent or assume product decisions. Strictly distinguish explicitly confirmed requirements, inferences from answers and interviewer assumptions. Inferences and assumptions do not become product decisions without the owner's confirmation.
2. Track confirmed, unconfirmed, unknown and conflicting information. Only explicit owner input confirms decisions.
3. Identify questions according to the registry rules and give each decision a stable ID. Link decisions to source answers or direct statements. Retain superseded decisions.
4. Label assistant ideas as proposals until approved. Track products separately.
Record each established requirement as a separate entry using the [Requirements Registry Record Structure](Artifact-Data-Formats.md#requirements-registry-record-structure).

## 7. Product Specification
When the owner requests a product specification, for example, "Compile the current product specification," compile a structured document covering relevant goals, users, use cases, scope, requirements, constraints, exclusions, success criteria, open questions and source links. Use confirmed input only; expose gaps and conflicts; ensure traceability. Use the owner's language. The owner decides when it is complete.

## 8. Decision Management and Conflict Resolution

8. Decision Management. Across all stages, Actors may identify gaps, contradictions, blockers, and uncertainties in upstream requirements and stage documents. Within their authority, they may independently make decisions to resolve these issues or substantially reduce uncertainty in requirements, provided those decisions introduce no new conflicts or other issues. Routine execution choices within confirmed requirements and constraints do not require individual records.
9. **Conflict Resolution**. If a proposed decision would introduce new issues, such as conflicts or uncertainties, record it as a proposal in the Decision Registry and refer it to the responsible Actors for resolution. Actors with Stakeholder Authority may mandate acceptance of a decision despite existing requirement conflicts. The Actors responsible for the affected requirements must then resolve those conflicts.
