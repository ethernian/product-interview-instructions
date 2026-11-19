# Product Information Management Instructions

## 1. Ownership

Requirements and other work items may have a human owner. Others must not change an owned item without the owner's authorization. This separates responsibilities, avoids repeated human revalidation of AI rewrites, and reduces the risk of unauthorized changes.

## 2. Respect Actor Authority

Proposals and assumptions become confirmed decisions only when confirmed by an actor with the necessary authority. An actor may confirm an item on another actor's behalf only with that actor's explicit delegation. Use decisions to guide further work only after confirmation by the responsible actor or an explicitly authorized delegate.

## 3. Processing Priorities

1. **Reduce uncertainty.** Prioritize questions and requests that significantly affect dependent decisions. Record unknown parameters explicitly.
2. **Minimize rework.** Identify contradictions and costly-to-change decisions before executing dependent work.
3. **Maximize automation.** AI agents perform as much necessary work as their capabilities and authority allow. Involve humans only when their information, judgment, or authority is needed, and minimize their effort.
4. **Minimize maintenance.** Eliminate independently maintained duplicates and enable automatic updates of dependent artifacts.

## 4. Product Development Principles

1. **Separate responsibilities.** Keep source information, requirements, architecture, and implementation separate. An artifact may have multiple sources.
2. **Maintain traceability.** Link derived artifacts to their sources using stable identifiers, and maintain those links when changes occur.
3. **Ensure verifiability.** Define objective verification criteria for every output and document the justification for selected solutions.
4. **Control uncertainty.** Missing information and contradictions block only activities that critically depend on them.

## 5. Interview Artifact Handling

Within `OutputDocuments`:

1. Use the product's existing unified Product Information Registry for questions and decisions; if none is configured, use `product-information-registry.json` in `OutputDocuments`. Store the Source Registry in `source-registry.md` and the Coverage Map in `coverage-map.md`.
2. Initialize a new product information registry with a product ID and an empty records array only after checking for existing product artifacts and following the migration rules. Add prepared questions, open questions, and source-supported proposed answers without treating proposals as confirmed decisions.
3. Record input sources in the Source Registry and initialize catalog areas as not examined in the Coverage Map. Update the Source Registry when sources change and reassess coverage after each round.
4. Save full product information registry snapshots in `snapshots/` next to the registry, using a new sequential filename for each completed round and after registry records change outside a round.

## 6. Traceability

Follow [Artifact-Data-Formats.md](Artifact-Data-Formats.md) as the authoritative reference for product information registry fields, formats, statuses, and storage rules.

1. Never invent or assume product decisions. Distinguish confirmed requirements, inferences, and interviewer assumptions; inferences and assumptions do not become product decisions without confirmation by the responsible actor or an explicitly authorized delegate.
2. Track confirmed, unconfirmed, unknown, and conflicting information. Record direct owner answers as given, retaining tentative wording. An authorized owner's clear decision is confirmed without a second confirmation; answer completeness alone does not confirm a proposal or verify a fact.
3. Identify questions according to the registry rules. Give each decision a stable ID, link it to all source answers or direct statements, and retain superseded decisions. Record useful agent interpretations separately in `interpreted_as` and `interpretation_note`; they do not change the owner's answer or confer approval. Clarify material uncertainty and record the owner's corrections.
4. Label assistant ideas as proposals until approved. Track products separately.
5. Record each established requirement separately using the [Requirements Registry Record Structure](Artifact-Data-Formats.md#requirements-registry-record-structure).

## 7. Product Specification

When the owner requests a product specification, compile a structured document in the owner's language. Cover relevant goals, users, use cases, scope, requirements, constraints, exclusions, success criteria, open questions, and source links. Use only confirmed input, expose gaps and conflicts, and preserve traceability. The owner decides when the specification is complete.

## 8. Decision Management and Conflict Resolution

Actors may identify gaps, contradictions, blockers, and uncertainties in upstream requirements and stage documents. Within their authority, they may independently make decisions that resolve these issues or substantially reduce uncertainty, provided those decisions introduce no new conflicts or other issues. Routine execution choices within confirmed requirements and constraints do not require individual records.

If a proposed decision would introduce new issues, including conflicts or uncertainties, record it as a proposal in the Product Information Registry and refer it to the responsible actors. Actors with Stakeholder Authority may mandate acceptance despite existing requirement conflicts; the actors responsible for the affected requirements must then resolve those conflicts.
