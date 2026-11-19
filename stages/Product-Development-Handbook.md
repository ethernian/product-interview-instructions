# Product Development Handbook
### A Methodology for AI-Assisted Requirements Management

## 1. Purpose and Scope

This handbook describes the product development process, its stages, their relationships, and the artifacts they produce.

For core processing principles and requirements management, follow the [Product Information Management Instructions](../app/Product-Information-Management-Instructions.md) and [Product Interview Instructions](../app/Product-Interview-Instructions.md).

Use the process and stage descriptions to guide work. Use [Artifact Data Formats](../app/Artifact-Data-Formats.md) as the authoritative reference for record fields, status values, and storage rules.

## 2. How the Process Works

The process consists of the [development stages](#3-development-stages). Each stage transforms defined inputs into outputs using its instructions and resources. Stages normally consume earlier outputs, but may have other dependencies and may be revisited as the product evolves.

1. **Stage definition and recursion.** Each stage directory contains a `README.md` describing its inputs, outputs, instructions, resources, completion criteria, and dependencies. A stage may be treated as a sub-project with its own stages and deliverables. A sub-project stage inherits inputs from the corresponding stage at the parent level, if one exists. If there is no corresponding parent stage, define its inputs explicitly in the sub-project's stage description.
2. **Instructions and resources.** Each stage selects and adapts applicable processes, solutions, methods, and templates from its library. These resources may be shared across projects. Record the patterns used and the rationale for their selection. If no suitable resource exists, the process may develop one and propose its addition to the shared collection through a pull request.
3. **Verification, acceptance, and release.** Verify each stage's outputs against its inputs, applicable patterns, and completion criteria; return defects to the responsible stage for correction. An actor with the necessary authority accepts outputs against defined criteria. Verification does not confer acceptance authority, and acceptance on another actor's behalf requires explicit delegation. Release only accepted outputs.
4. **Iteration and change management.** When an artifact changes, identify affected dependencies, regenerate necessary outputs, and repeat verification. Do not automatically modify confirmed decisions. Route operational data, defects, and new needs to the appropriate stages through change management.
5. **Traceability and version management.** Maintain bidirectional links between sources, requirements, decisions, tasks, implementation, and tests. Version artifacts, instructions, and resources so that the input and rule versions used to produce each output can be determined.

## 3. Development Stages

### Stage Overview

| Stage | Main inputs | Activity | Main outputs |
| --- | --- | --- | --- |
| [`01-discovery`](01-discovery/README.md): Gather information for requirements. | Discovery Catalog, external materials, stakeholder responses. | Adaptive interviewing, fact extraction, identification of contradictions,  uncertainties, and gaps. | Q&A Registry, Source Registry, Coverage Map, open questions. |
| [`02-requirements`](02-requirements/README.md): Define and verify requirements. | Discovery artifacts. | Select an appropriate method, extract and normalize requirements, eliminate duplication and contradictions. | Requirements Registry, Requirements Specification, Acceptance Criteria, source references. |
| [`03-architecture`](03-architecture/README.md): Select and verify an architecture. | Requirements and constraints. | Select and adapt an appropriate architecture, evaluate alternatives, verify assumptions and constraints. | Architecture Specification, Data Model, Component Contracts, Decision Registry updates. |
| [`04-system-provisioning`](04-system-provisioning/README.md): Provision the system environment. | Architectural requirements for the system environment. | Select and adapt templates, generate configurations and scripts, provision the environment automatically. | Provisioning Scripts, configurations, provisioned environment. |
| [`05-infrastructure-deployment`](05-infrastructure-deployment/README.md): Deploy infrastructure services. | Architecture, provisioned environment. | Select infrastructure templates, adapt them to the architecture, generate configurations, deploy, and verify. | Deployment Manifests, deployment scripts, operational infrastructure. |
| [`06-implementation`](06-implementation/README.md): Implement and test requirements. | Requirements, architecture, infrastructure. | Break down work into tasks, select and adapt solutions, develop code, apply application schema migrations, and run automated tests. | Source Code, Database Migrations, builds, tests. |
| [`07-monitoring`](07-monitoring/README.md): Develop the monitoring system. | Requirements, implementation. | Break down work into tasks, select and adapt solutions, develop code, apply application schema migrations, and run automated tests. | Monitoring System |
