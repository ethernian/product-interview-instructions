# Requirements Management Add-on

This add-on provides human-led, AI-assisted requirements management for a specific product, a product sub-module, or an individual product development stage. It helps collect and review information, maintain traceable requirements and decisions, and identify unresolved questions. It does not replace the product's own documentation, implementation, or decision authority.

The template below is intended for the `README.md` at the root of the project using the add-on. Replace bracketed placeholders, remove inapplicable sections, and adapt paths to the actual project layout. Do not replace existing project documentation without preserving relevant content. The examples assume that the add-on is available as `app/` under that project root; update paths if it is installed elsewhere. The project's development stages and their resources are separate from the add-on. Define the scope and paths before starting, and do not invent missing product information.

## Project README template

````markdown
# [Product, sub-module, or stage name]

[Describe the subject, its purpose, and the intended outcome.]

## Scope and context

- **Scope type:** [Product / sub-module / product development stage]
- **In scope:** [Capabilities, boundaries, or stage activities covered here]
- **Out of scope:** [Explicit exclusions]
- **Parent product or stage:** [Name and link, if applicable]
- **Dependencies and interfaces:** [Related modules, stages, or external systems]
- **Current state:** [Known facts, existing artifacts, and outstanding unknowns]

Treat unconfirmed statements and missing information as such. Link to authoritative source material rather than duplicating it here.

## People and authority

- **Stakeholder or product owner:** [Name or role; how to contact]
- **Requirement and decision owners:** [Names or roles, scope of authority, and any explicit delegations]
- **Other participants:** [Names or roles and responsibilities]

An AI assistant may propose answers, requirements, and decisions; only an actor with the necessary authority, or an explicitly authorized delegate, can confirm them. Do not change owned requirements or decisions without the owner's authorization.

## Requirements management add-on

This project uses the requirements management add-on to organize discovery, requirements, decisions, and related artifacts for the scope above. The instructions and formats are authoritative for their respective responsibilities:

| Resource | Purpose |
| --- | --- |
| [Product Interview Instructions](app/Product-Interview-Instructions.md) | Interview preparation, question sequencing, rounds, and coverage. |
| [Product Information Management Instructions](app/Product-Information-Management-Instructions.md) | Q&A and requirements handling, decisions, proposals, and traceability. |
| [Artifact Data Formats](app/Artifact-Data-Formats.md) | Artifact fields, status values, and storage rules. |
| [UX Guide](app/UX-Guide.md) | Interview presentation and interaction, including the text fallback. |

If any required instruction or source is unavailable, identify it and request it; do not invent its contents or claim to have followed it. The project supplies its own process descriptions, applicable guidance, and other resources; they are not part of the add-on.

## Inputs and outputs

Set these locations for the selected scope before starting. State how relative paths are resolved in the project's invocation instructions.

| Item | Location or description |
| --- | --- |
| Input documents | [Path or list of available product, parent, and stage materials] |
| Solution library | [Path to applicable project-provided guidance and resources] |
| Process description | [Path or description of the process to be supported] |
| Output documents | [Directory for artifacts for this scope] |
| Product information registry | [Shared registry path, or state that the interview should locate existing artifacts before using the output-directory default] |
| Existing artifacts to resume | [Paths, or state that none exist] |

Map these locations to the interview arguments `Input Documents`, `Solution Library`, `ProcessDescription`, and `OutputDocuments` in the project's invocation instructions. Read available inputs before requesting more, report unreadable inputs, and resume existing artifacts instead of overwriting them.

The project maintains one `product-information-registry.json` for questions and decisions across stages, plus `source-registry.md`, `coverage-map.md`, and sequential full registry snapshots under `snapshots/`. Configure the shared registry location; the interview defaults it to its output directory when none exists. Follow the artifact formats and information management instructions for contents, statuses, migration, storage, and fallback behavior. Requirements retain their own registry. [Identify existing product information and requirements registries, including any legacy Q&A or decision registry, if any.]

## Working process

1. Define the product, sub-module, or stage scope; identify its owners, inputs, applicable resources, and output location.
2. Review available sources and existing artifacts. Identify gaps, contradictions, uncertainties, and dependencies without treating source claims or assistant proposals as confirmed decisions.
3. Conduct or resume the interview using the interview instructions. The owner may change the number of questions per round, provide partial answers, or defer questions. Complete the review, summary, registry update, and snapshot after each completed round.
4. Apply the information management and artifact format instructions to maintain Q&A, requirements, proposals, decisions, sources, and coverage. Keep source links and distinguish confirmed input from assumptions and proposals.
5. Use the project's applicable process and resources to define and verify requirements. Resolve or explicitly record gaps and conflicts.
6. On request, compile the current product specification from confirmed input, exposing gaps and conflicts and retaining source links. The owner decides when it is complete. Verify outputs and obtain acceptance from an authorized actor; do not treat verification alone as acceptance.
7. When sources, requirements, or decisions change, identify affected dependencies, preserve history, and revisit verification. Do not automatically modify confirmed decisions.

For a repository-aware agent, follow the host project's invocation instructions and applicable agent instructions. [Describe how to start or resume the relevant activity and how its arguments and paths are resolved.]

For ChatGPT Projects, add the applicable files from `app/` and the project's own process descriptions and resources to the project's sources, preserving their filenames. Configure the project instructions to read and follow the interview instructions and their referenced supporting documents, report missing files, and respect stakeholder decision authority. Then start a chat with the product idea or existing project context. Uploads are optional; do not present unsupported proposals as confirmed input.

## Current status and next steps

- **Active stage or activity:** [Stage and status]
- **Artifacts:** [Links to current registries, snapshots, specifications, and decisions]
- **Open questions and blockers:** [Links or brief summary]
- **Next action and responsible actor:** [Action and owner]
- **Last reviewed:** [Date and reviewer]
````
