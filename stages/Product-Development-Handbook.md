# Product Development Handbook
### A Methodology for AI-Assisted Requirements Management

## 1. Purpose and Scope

This handbook describes a human-led, AI-assisted requirements management process focused on collecting and managing requirements throughout all stages of product development. The Process assigns as much work as possible to AI-Agents, minimizes human effort across all stages, while fully preserving humans' control over the product and their decision authority.

Follow [Product Information Management Instructions](../app/Product-Information-Management-Instructions.md) for requirements, proposals, decisions, and related artifact handling.

Read the principles first, use the process and stage descriptions to guide work, and refer to the cross-stage rules and glossary throughout. Use [Artifact Data Formats](../app/Artifact-Data-Formats.md) as the authoritative reference for record fields, status values, and storage rules.

## 2. Core Principles

### 2.1. Respect Actor Authority

Follow [Respect Actor Authority](../app/Product-Information-Management-Instructions.md#respect-actor-authority).

### 2.2. Minimize Human Effort

Follow [Minimize Human Effort](../app/Product-Interview-Instructions.md#minimize-human-effort).

### 2.3. Processing Priorities

Follow [Processing Priorities](../app/Product-Information-Management-Instructions.md#processing-priorities).

### 2.4. Product Development Principles

1. **Separation of Responsibilities.** Each artifact has a single authoritative source. Source information, requirements, architecture, and implementation are maintained separately.
2. **Question Relevance.** Follow [Question Relevance](../app/Product-Interview-Instructions.md#question-relevance).
3. **Traceability.** Derived artifacts are linked to their sources through stable identifiers. These relationships are maintained when changes occur.
4. **Verifiability.** Every output has objective verification criteria. Selected solutions include documented justification.
5. **Controlled Uncertainty.** Missing information and contradictions block only the activities that critically depend on them.

## 3. How the Process Works

Each stage transforms inputs into outputs through activities that select and adapt standard solutions from the stage’s instructions and resources. The outputs are verified against completion criteria and accepted by an actor with the necessary authority.

1. **Development Stages.**  
The Process contains of multiple stages from 01-discovery to 07-monitoring as described in [Development Stages](#4-development-stages). These stages are represented by folders in the directory structure.
2. **Stage-Based Transformation.**  
Each stage has defined Inputs, Outputs, Stage Instructions, Resources, and Completion Criteria. Usually output of previous stage is used and the input as the next stage, but some stages may have more complex dependencies. Each stage contans README.md file describing the stage processes and resources and its dependecies to other stages.
3. **Stage recursion.**  
Every stage may be treated as a separate sub-project with own deliverables and define own Stages. For example, the 07-monitoring stage may be treated as a project with own 01-discovery, 02-requirements, 03-deployment and so on. In this case the stage inherits Inputs from the the stage of the same kind in the upper levels.
4. **Instructions and Resources.**
Each stage uses its own library of work processes, solutions, methods, templates, alternatives, and applicability conditions. Selected resources are adapted to the input data; inapplicable resources are excluded. Instructions and Resources are usually an external resource, shared between many projects.
If no suitable instruction or resource is available, the Process may develop and use a new solution, then propose it as an addition to the Instructions and Resources collection through a pull request.
5. **Iterative Execution.**  
Stages define the initial sequence but allow revisiting earlier stages and regenerating dependent artifacts.

## 4. Development Stages

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

## 5. Rules Applied Across Stages

1. **Verification.** At every stage, verify output artifacts against inputs, applicable patterns, and completion criteria. Return detected defects to the responsible stage for correction.
2. **Acceptance.** An actor with the necessary authority accepts stage outputs against defined criteria. Verification alone does not confer acceptance authority. Acceptance on another actor's behalf requires that actor's explicit delegation.
3. **Change Management.** When any artifact changes, identify affected dependencies, regenerate necessary outputs, and repeat verification. Do not automatically modify confirmed decisions.
4. **Traceability.** Maintain bidirectional links between sources, requirements, decisions, tasks, implementation, and tests. Record the patterns used and the rationale for their selection.
5. **Version Management.** Version artifacts and Instructions and Resources. Preserve the ability to determine which versions of inputs and rules produced each output.
6. **Release.** Release only accepted outputs.
7. **Feedback.** Route operational data, defects, and new needs to the appropriate stages through Change Management.
8. **Decision Management and Conflict Resolution.** Follow [Decision Management and Conflict Resolution](../app/Product-Information-Management-Instructions.md#decision-management-and-conflict-resolution).

## 6. Key Artifact Glossary

### 6.1. Methodology Artifacts

1. **Instructions and Resources.** A versioned collection of methods, templates, and alternatives, including applicability conditions, limitations, and selection criteria.
2. **Stage Instructions.** Rules governing input-to-output transformation, Instructions and Resources usage, and uncertainty handling.
3. **Stage Completion Criteria.** Conditions that stage outputs must meet before downstream use. See the [criterion structure and confirmation methods](../app/Artifact-Data-Formats.md#stage-completion-criterion-structure).
4. **Decision Registry.** A versioned collection of significant decisions made throughout the Process, covering scope, requirements, priorities, architecture, implementation, deployment, and operations. All stages contribute to the same registry.
5. **Decision Record.** An entry capturing a significant decision or proposal in the Decision Registry. See the [record fields and statuses](../app/Artifact-Data-Formats.md#decision-registry-record-structure).

### 6.2. Discovery

See the [discovery stage](01-discovery/README.md).

1. **Discovery Catalog.** A versioned catalog of thematically organized questions used for adaptive information gathering to support requirements definition and subsequent design decisions.
2. **Q&A Registry.** Questions and their current answers, proposals, and unresolved issues. See the [record structure and storage rules](../app/Artifact-Data-Formats.md#qa-registry-record-structure).
3. **Source Registry.** A record of source materials used by the Process. See the [source record structure](../app/Artifact-Data-Formats.md#source-registry-record-structure).
4. **Coverage Map.** The investigation status of each area. See the [entry structure and status values](../app/Artifact-Data-Formats.md#coverage-map-entry-structure).

### 6.3. Requirements

See the [requirements stage](02-requirements/README.md).

1. **Requirements Registry.** A structured collection of atomic requirements. See the [record structure](../app/Artifact-Data-Formats.md#requirements-registry-record-structure).
2. **Requirements Specification.** A consolidated description of expected system behavior and constraints, generated from the Requirements Registry.
3. **Acceptance Criteria.** Verifiable conditions determining whether a requirement or user scenario has been fulfilled.

### 6.4. Architecture

See the [architecture stage](03-architecture/README.md).

1. **Architecture Specification.** A description of the selected architecture, its components, responsibilities, deployment topology, and interactions.
2. **Data Model.** Entities, attributes, and relationships that describe the structure of the system's data.
3. **Component Contracts.** Definitions of component interfaces, expected inputs and outputs, responsibilities, and interaction constraints.

### 6.5. System Provisioning

See the [system provisioning stage](04-system-provisioning/README.md).

1. **Provisioning Scripts.** Automated instructions for preparing the system environment, including operating system configuration, security policies, networks, and required system components.
2. **Environment Configurations.** Versioned settings that define the required system environment and allow it to be reproduced.
3. **Provisioned Environment.** An environment prepared according to the architecture and verified against its configuration requirements.

### 6.6. Infrastructure Deployment

See the [infrastructure deployment stage](05-infrastructure-deployment/README.md).

1. **Deployment Manifests.** Declarative descriptions of infrastructure services, their configuration, and their dependencies, used to establish the required deployed state.
2. **Deployment Scripts.** Automated instructions for deploying and configuring infrastructure services in the provisioned environment.
3. **Operational Infrastructure.** Deployed infrastructure services whose required dependencies are available and whose health checks pass.

### 6.7. Implementation

See the [implementation stage](06-implementation/README.md).

1. **Source Code.** Versioned implementation of the product's behavior and interfaces, linked to the requirements it fulfills.
2. **Database Migrations.** Versioned changes to database structures or data, applied in a defined sequence to support the implementation.
3. **Builds.** Executable or deployable artifacts produced from a defined version of the source code and its dependencies.
4. **Tests.** Repeatable checks that verify implementation behavior against requirements and acceptance criteria.

### 6.8. Monitoring

See the [monitoring stage](07-monitoring/README.md).

1. **Monitoring System.** The components and configurations used to collect and evaluate operational data, make system health and behavior visible, and signal conditions requiring attention. Its findings support feedback and change management.
