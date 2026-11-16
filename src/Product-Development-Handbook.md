# Product Development Handbook
### A Methodology for AI-Assisted Software Development

## 1. Optimization Objectives

### 1.1. Respect User Authority
1. **Respect Decision Authority.** AI-generated proposals and assumptions do not become confirmed decisions without explicit approval from an authorized person.  

2. **Use only confirmed decisions.** Don't use unconfirmed decisions to generate artefacts. 
  
  
### 1.2. Minimize Human Effort
1. **Ask only what humans must answer.** Request information from human users only when it affects requirements or subsequent decisions and cannot be supplied by automated agents, either because they lack the necessary information or authority.

2. **Minimize the effort of answering.** Reduce the time and cognitive effort needed to understand a question, evaluate relevant information, formulate a response, and submit it.

3. **Respect user competence.** Ask questions within the user's area of expertise. Accept "I don't know" as a valid answer. Instead of requiring unfamiliar technical decisions, ask users to evaluate consequences they can understand. For example, rather than asking a Product Owner whether a product requires IP67 protection, ask whether it needs to withstand exposure to water.

4. **Reuse existing information.** Use available documents, previous answers, and established decisions instead of requesting the same information again.
b. Reuse existing information.

### 1.3. Process Priorities
1. **Effective Uncertainty Minimization.** Prioritize questions and requests that significantly affect dependent decisions. Record unknown parameters explicitly.

2. **Minimize Rework.** Identify contradictions and costly-to-change decisions before executing dependent work.

3. **Maximize Automation.** Automate artifact generation, verification, and updates. Reserve for humans decisions that require their authority or expert judgment.

4. **Minimize Maintenance Overhead.** Eliminate independently maintained duplicates of information. Enable automatic updates of dependent artifacts.

## 2. Product Development Principles

**2.1. Development Stages.** contains of multiple stages from 00-discovery to 07-monitoring as described in 3. Development Stages. These stages are represented by folders in the directory structure. 

**2.2. Stage-Based Transformation.** Each stage has defined Inputs, Outputs, a Standard Solution Library (accesses as an external resource), and Quality Gates as a completion criteria. Usually output of previous stage is used and the input as the next stage, but some stages may have more complex dependencies. Each stage contans README.md file describing the stage processes and its dependecies to other stages. 

**2.3. Stage recursion.** Every stage may be treated as a separate sub-project with own deliverables and define own Stages. So the 07-monitoring stage may be treated as a project with own 01-discovery, 02-requirements, 02-deployment and so on. In this case the stage inherits Inputs from the the stage of the same kind in the upper levels.


**2.3. Separation of Responsibilities.** Each artifact has a single authoritative source. Source information, requirements, architecture, and implementation are maintained separately.

**2.4. Question Relevance.** The Discovery Catalog is prepared in advance based on supported practices and their applicability conditions. Every question must influence requirements or subsequent decisions. The underlying practices are excluded from the interview context.

**2.5. Standard Solution Library .** Each stage uses its own library of solutions, methods, templates, alternatives, and applicability conditions. Selected patterns are adapted to the input data; inapplicable patterns are excluded. The Standard Solution Library is usually an external resource, that is shared between many projects.

**2.6. Traceability.** Derived artifacts are linked to their sources through stable identifiers. These relationships are maintained when changes occur.

**2.7. Verifiability.** Every output has objective verification criteria. Selected solutions include documented justification.

**2.8. Controlled Uncertainty.** Missing information and contradictions block only the activities that critically depend on them.

**2.9. Iterative Execution.** Stages define the initial sequence but allow revisiting earlier stages and regenerating dependent artifacts.

## 3. Development Stages

### 3.1. `01-discovery`

**Input:** Discovery Catalog, external materials, stakeholder responses.

**Pattern Library:** Methods for interviewing, information extraction, and question formulation. Used when preparing the Discovery Catalog; the library itself is excluded from the interview context.

**Process:** Adaptive interviewing, fact extraction, identification of contradictions and uncertainties.

**Output:** Q&A Registry, Source Registry, Coverage Map, open questions.

**Completion Criteria:** Sufficient information is available to formulate requirements; remaining gaps are explicitly documented.

### 3.2. `02-requirements`

**Input:** Discovery artifacts.

**Pattern Library:** Methods for requirements elicitation, extraction, and formalization; specification and registry templates; standards for structure, completeness, clarity, and verifiability.

**Process:** Select an appropriate method, extract and normalize requirements, eliminate duplication and contradictions.

**Output:** Requirements Registry, Requirements Specification, Acceptance Criteria, source references.

**Completion Criteria:** Requirements are unambiguous, verifiable, and have defined statuses and provenance.

### 3.3. `03-architecture`

**Input:** Requirements and constraints.

**Pattern Library:** Catalog of architectures, architectural patterns, technology alternatives, and their applicability criteria.

**Process:** Select and adapt an appropriate architecture, evaluate alternatives, verify assumptions and constraints.

**Output:** Architecture Specification, Data Model, Component Contracts, Architecture Decision Records (ADR).

**Completion Criteria:** Decisions are justified, consistent with requirements, and sufficiently detailed for implementation.

### 3.4. `04-system-provisioning`

**Input:** Architectural requirements for the system environment.

**Pattern Library:** Templates for operating system configuration, system security, network policies, system component installation, and automated server provisioning.

**Process:** Select and adapt templates, generate configurations and scripts, provision the environment automatically.

**Output:** Provisioning Scripts, configurations, provisioned environment.

**Completion Criteria:** The environment can be provisioned reproducibly and passes configuration checks.

### 3.5. `05-infrastructure-deployment`

**Input:** Architecture, provisioned environment.

**Pattern Library:** Templates for deploying infrastructure services, database systems, networks, storage, container configurations, and initial infrastructure setup.

**Process:** Select infrastructure templates, adapt them to the architecture, generate configurations, deploy, and verify.

**Output:** Deployment Manifests, deployment scripts, operational infrastructure.

**Completion Criteria:** Infrastructure can be deployed reproducibly, dependencies are available, and health checks pass.

### 3.6. `06-implementation`

**Input:** Requirements, architecture, infrastructure.

**Pattern Library:** Component implementation templates, algorithmic and design patterns, coding conventions, testing templates, and migration patterns.

**Process:** Break down work into tasks, select and adapt solutions, develop code, apply application schema migrations, and run automated tests.

**Output:** Source Code, Database Migrations, builds, tests.

**Completion Criteria:** Implemented requirements are verified by tests, and deviations are documented.

### 3.7. `07-monitoring`

**Input:** Requirements, implementation.

**Pattern Library:** Monitoring implementation templates, algorithmic and design patterns, coding conventions, testing templates, and migration patterns.

**Process:** Break down work into tasks, select and adapt solutions, develop code, apply application schema migrations, and run automated tests.

**Output:** Monitoring System

**Completion Criteria:** 

## 4. Cross-Cutting Workflows

### 4.1. Verification

At every stage, verify output artifacts against inputs, applicable patterns, and completion criteria. Return detected defects to the responsible stage for correction.

### 4.2. Acceptance

An authorized stakeholder accepts stage outputs against defined criteria. Automated verification does not replace required human approval.

### 4.3. Change Management

When any artifact changes, identify affected dependencies, regenerate necessary outputs, and repeat verification. Do not automatically modify confirmed decisions.

### 4.4. Traceability

Maintain bidirectional links between sources, requirements, architectural decisions, tasks, implementation, and tests. Record the patterns used and the rationale for their selection.

### 4.5. Version Management

Version artifacts, instructions, and Pattern Libraries. Preserve the ability to determine which versions of inputs and rules produced each output.

### 4.6. Release & Feedback

Release only accepted outputs. Route operational data, defects, and new needs to the appropriate stages through Change Management.

## 5. Key Artifact Glossary

### 5.1. Methodology Artifacts

**5.1.1. Pattern Library.** A versioned collection of methods, templates, and alternatives, including applicability conditions, limitations, and selection criteria.

**5.1.2. Stage Instructions.** Rules governing input-to-output transformation, Pattern Library usage, and uncertainty handling.

**5.1.3. Quality Gate.** A set of verifiable conditions determining whether stage outputs are ready for downstream use.

### 5.2. Discovery

**5.2.1. Discovery Catalog.** A versioned catalog of thematically organized questions used for adaptive information gathering to support requirements definition and subsequent design decisions.

**5.2.2. Q&A Registry.** Questions with stable identifiers, confirmed answers, statuses, catalog references, and unresolved issues.

**5.2.3. Source Registry.** A record of source materials, including their provenance, versions, and reliability status.

**5.2.4. Coverage Map.** The investigation status of each area: defined, partially defined, unexplored, or not applicable.

### 5.3. Requirements

**5.3.1. Requirements Registry.** A structured collection of atomic requirements with stable identifiers, statuses, priorities, and source references.

**5.3.2. Requirements Specification.** A consolidated description of expected system behavior and constraints, generated from the Requirements Registry.

**5.3.3. Acceptance Criteria.** Verifiable conditions determining whether a requirement or user scenario has been fulfilled.

### 5.4. Architecture

**5.4.1. Architecture Specification.** A description of the selected architecture, its components, responsibilities, deployment topology, and interactions.

**5.4.2. Data Model.** Entities,