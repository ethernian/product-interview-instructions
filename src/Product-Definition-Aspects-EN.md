# Product Definition & Architecture Discovery Aspect Catalog

**Document ID:** PRODEF-ASP-001  
**Version:** 1.0  
**Status:** Baseline for handoff  
**Date:** 2026-11-03  
**Language:** English  
**Source:** Product Owner discovery checklist established in ProDef project conversation  

## Purpose of the document

A universal catalog of areas and questions for interviews with a Product Owner (PO). Used when defining a product, system requirements, and inputs for designing the architecture of web applications, mobile applications, SaaS, enterprise systems, API services, and other software products.

**Goal:** gather enough information to determine what we are building, for whom, how the system should work, which constraints to consider, and which architectural decisions need to be made.

**Division of responsibilities:**
- **Product Definition:** what the product needs and why.
- **System Requirements:** functional and non-functional requirements.
- **Architecture Design:** how to implement the requirements technically.

The PO is not required to choose databases, protocols, or architectural patterns. Their task is to define needs, constraints, and expected behavior. Technical decisions must be based on confirmed answers.

---

## 1. Product and business context
**Goal:** understand the product's purpose, boundaries, and success criteria.

1.1. What problem does the product solve?
1.2. Who experiences this problem?
1.3. How is the problem solved now?
1.4. What outcome should the product deliver?
1.5. What is the product's core value?
1.6. What are the main use cases?
1.7. What is included in the product, and what is explicitly outside its scope?
1.8. Is this a standalone product or part of an existing system?
1.9. Who are the client, owner, and stakeholders?
1.10. How is product success measured?
1.11. What business constraints exist?
1.12. What must be included in the first version (MVP)?
1.13. How is the product expected to evolve?
1.14. Are there existing equivalents or systems whose behavior needs to be taken into account?

## 2. Users and roles
**Goal:** determine who interacts with the system and which access models are needed.

2.1. Who is a user of the system?
2.2. What categories of users exist?
2.3. Are they people, external systems, automated agents, or a combination of these?
2.4. What tasks does each category perform?
2.5. What roles and access levels exist?
2.6. Can one user have multiple roles?
2.7. Are there administrators, operators, moderators, or auditors?
2.8. Are users internal or external?
2.9. Is access without registration required?
2.10. Can a user belong to multiple organizations, teams, or projects?
2.11. Are there hierarchies of organizations and users?
2.12. Are there users with special accessibility needs?
2.13. In which countries and time zones are users located?
2.14. Which interface languages are required?
2.15. What is the users' level of technical proficiency?

## 3. Scale and number of users
**Goal:** determine the system's scale and growth prospects.

3.1. How many users are expected in total?
3.2. How many users will be active daily (DAU)?
3.3. How many users will be active monthly (MAU)?
3.4. How many users can work simultaneously?
3.5. How many users are expected at launch, after one year, and after several years?
3.6. How quickly can the user base grow?
3.7. Are there seasonal or periodic peaks in activity?
3.8. How are users distributed geographically?
3.9. How many organizations or clients will the system serve?
3.10. How much can organization sizes vary?
3.11. Are sudden load spikes possible?
3.12. Are there limits on the maximum number of users, organizations, or objects?

## 4. Functionality and user scenarios
**Goal:** determine exactly what the system should do.

4.1. What core functions are needed?
4.2. Which user scenarios are critical?
4.3. What does each scenario look like from beginning to end?
4.4. What actions does the user perform?
4.5. What actions does the system perform automatically?
4.6. What input data is required?
4.7. What results should be produced?
4.8. What business rules apply?
4.9. What exceptions and error situations are possible?
4.10. Which operations require confirmation?
4.11. Which processes require approval?
4.12. Which operations can be undone or repeated?
4.13. Are bulk operations needed?
4.14. Are search, filtering, sorting, and export needed?
4.15. Which functions are available to each role?
4.16. Which scenarios should work without human involvement?
4.17. Which functions are mandatory for the MVP, and which can be deferred?

## 5. Data and information model
**Goal:** determine the main entities, relationships, lifecycle, and data volumes.

5.1. What main entities exist in the product?
5.2. What attributes does each entity have?
5.3. How are the entities related?
5.4. Who creates, modifies, and deletes data?
5.5. Which data is mandatory, and which is optional?
5.6. What integrity constraints exist?
5.7. Which data is unique?
5.8. Which entities have states and transitions between them?
5.9. Does a history of changes need to be stored?
5.10. Is object versioning required?
5.11. Does deleted data need to be restored?
5.12. How long is data retained?
5.13. What data volumes are expected at launch and in the future?
5.14. What are the average and maximum object sizes?
5.15. What data types are used: text, files, images, video, geospatial data, events?
5.16. Is full-text or semantic search needed?
5.17. Is there data belonging to multiple users or organizations?
5.18. Which data is confidential?
5.19. Are data import, export, and migration needed?
5.20. How are conflicts resolved when data is modified simultaneously?
5.21. Which data is considered the source of truth?
5.22. Which data can be recreated, and which data must not be lost?

## 6. Load and performance
**Goal:** determine quantitative performance requirements.

6.1. How many requests per second are expected on average (RPS)?
6.2. What is the peak load?
6.3. Which operations are performed most frequently?
6.4. Which operations are the most resource-intensive?
6.5. What is the ratio of read to write operations?
6.6. What response time is acceptable for core operations?
6.7. What response time is acceptable for complex operations?
6.8. Are there latency requirements at the p95/p99 level?
6.9. How many background tasks are performed?
6.10. How long may background tasks run?
6.11. Is real-time processing needed?
6.12. What volume of data is transferred over the network?
6.13. Are there limits on request and response sizes?
6.14. Which operations must scale independently?
6.15. How should the system behave under overload?
6.16. Which functions may slow down during peaks, and which may not?

## 7. Client applications and interfaces
**Goal:** determine the necessary ways of interacting with the system.

7.1. Which client applications are needed: web, mobile, desktop, CLI?
7.2. Which platforms and operating systems are supported?
7.3. Which browsers and versions are mandatory?
7.4. Is a responsive interface needed?
7.5. Is a native mobile application required?
7.6. Is operation without an internet connection (offline) needed?
7.7. Does data need to be synchronized between devices?
7.8. Are push notifications required?
7.9. Are device capabilities needed: camera, GPS, Bluetooth, biometrics?
7.10. Are multilingual support and localization needed?
7.11. What are the accessibility requirements?
7.12. Are interfaces for third-party applications needed?
7.13. Are there visual style requirements or an existing design system?
7.14. Should multiple users see each other's changes in real time?

## 8. Identification, authentication, and authorization
**Goal:** determine the identity and access management model.

8.1. Do users need to be identified?
8.2. Which registration methods are supported?
8.3. Which sign-in methods are needed: password, SSO, OAuth, passkey, and others?
8.4. Is multi-factor authentication (MFA) needed?
8.5. Is there an external identity provider (Identity Provider)?
8.6. Who manages user accounts?
8.7. Are user invitations needed?
8.8. How is access restored?
8.9. How are roles and permissions structured?
8.10. Is access determined by role, object owner, organization, or a combination of conditions?
8.11. Can access be delegated?
8.12. Are temporary permissions needed?
8.13. What are the requirements for user sessions?
8.14. Is forced session termination needed?
8.15. How are users blocked and deleted?
8.16. Is auditing of access-related actions required?
8.17. Are service accounts and machine authentication needed?
8.18. Which actions require identity to be reconfirmed?

## 9. Organizations and tenant isolation
**Goal:** determine the multi-tenancy model.

9.1. Does the product serve one organization or multiple independent clients?
9.2. Which data belongs to the organization, and which to the user?
9.3. Can a user work in multiple organizations?
9.4. Must different clients' data be completely isolated?
9.5. Can clients exchange data?
9.6. Are separate settings needed for each client?
9.7. Can clients manage their own users?
9.8. Are separate domains or branding needed for clients?
9.9. Can clients choose the region where their data is stored?
9.10. Is dedicated infrastructure required for individual clients?
9.11. Are individual resource limits needed?
9.12. Can a client export all their data and leave the platform?

## 10. Integrations and external systems
**Goal:** determine dependencies on other systems.

10.1. Which systems require integration?
10.2. What data is transferred between systems?
10.3. Who initiates the data exchange?
10.4. Is the exchange synchronous or asynchronous?
10.5. Is two-way synchronization needed?
10.6. Which APIs or protocols are already defined?
10.7. What are the requirements for data update frequency?
10.8. How should the system respond to an external service being unavailable?
10.9. Are retries and error compensation needed?
10.10. Are there limits on the number of requests (rate limits)?
10.11. Are webhooks required?
10.12. Are public APIs for third-party developers needed?
10.13. How will API version compatibility be ensured?
10.14. Which integrations are mandatory for launch?
10.15. Who is responsible for the quality and availability of external data?

## 11. Business processes and automation
**Goal:** determine complex processes and their coordination.

11.1. Which processes consist of multiple steps?
11.2. What states does a process pass through?
11.3. What events trigger processes?
11.4. Which steps are performed automatically?
11.5. Which steps require user involvement?
11.6. Are there long-running processes that continue for hours or days?
11.7. Can processes be paused and resumed?
11.8. What happens if an error occurs at an intermediate step?
11.9. Are execution retries needed?
11.10. Is undoing actions that have already been performed required?
11.11. Can processes run in parallel?
11.12. Are schedules and periodic tasks needed?
11.13. Is execution status tracking required?
11.14. Can business processes be configured by users?

## 12. Security and privacy
**Goal:** determine requirements for protecting the product and data.

12.1. Which data requires special protection?
12.2. Which threats are the most significant?
12.3. What consequences could a data leak have?
12.4. Is encryption at rest and in transit required?
12.5. Who can see confidential data?
12.6. Which actions must be logged?
12.7. How long are audit logs retained?
12.8. Are there requirements for managing secrets and keys?
12.9. Are access restrictions by IP, device, or geography needed?
12.10. How should abuse and automated attacks be prevented?
12.11. Is suspicious activity detection required?
12.12. What are the requirements for deleting personal data?
12.13. Can a user request an export of their data?
12.14. Are there security requirements for third-party integrations?
12.15. What are the requirements for security checks before release?

## 13. Legislation and compliance
**Goal:** determine legal and industry constraints.

13.1. In which countries will the product be available?
13.2. Which laws apply?
13.3. Is compliance with GDPR or other regulations required?
13.4. Are there industry standards: HIPAA, PCI DSS, ISO 27001, and others?
13.5. Are there restrictions on transferring data between countries?
13.6. Where is data allowed to be stored and processed?
13.7. Is user consent for data processing needed?
13.8. What are the requirements for retention and deletion periods?
13.9. Are there requirements for legally significant actions?
13.10. Are electronic signatures needed?
13.11. Is confirmation of compliance by auditors required?
13.12. What legal restrictions apply to the use of third-party services and AI?

## 14. Availability, reliability, and recovery
**Goal:** determine how resilient the system must be.

14.1. What level of availability is required: 99%, 99.9%, 99.99%?
14.2. During which hours must the system be available?
14.3. What is the maximum acceptable downtime?
14.4. Which functions are critical to the business?
14.5. What should happen when an individual component fails?
14.6. Is continued operation during a partial failure required?
14.7. What amount of data loss is acceptable (RPO)?
14.8. Within what time must the system recover (RTO)?
14.9. Are backups needed?
14.10. How often must backups be created?
14.11. Is point-in-time recovery required?
14.12. Are there requirements for operation during a region or data center failure?
14.13. Are scheduled maintenance windows acceptable?
14.14. What are the requirements for preserving operations during failures?

## 15. Consistency and concurrent work
**Goal:** determine requirements for operation correctness and collaboration.

15.1. Can multiple users modify the same object simultaneously?
15.2. Which changes must be visible immediately?
15.3. Where is a delay in propagating changes acceptable?
15.4. Which operations must be performed atomically?
15.5. Which actions must not be performed twice?
15.6. How are change conflicts resolved?
15.7. Are object locks required?
15.8. Is a guaranteed order of event processing needed?
15.9. What are the consequences of an event being lost or processed again?
15.10. Should users see up-to-date data in real time?
15.11. Is temporary inconsistency between systems acceptable?
15.12. What are the transactionality requirements for business operations?

## 16. Deployment and infrastructure
**Goal:** determine hosting and operating conditions.

16.1. Where should the system run: cloud, on-premises, hybrid?
16.2. Is there a preferred cloud provider?
16.3. Are there restrictions on the technologies used?
16.4. Is hosting in a specific country or region required?
16.5. Are separate environments needed for development, testing, and production?
16.6. Is there existing infrastructure that must be used?
16.7. Is support for installing the product at the client's premises needed?
16.8. Can the product operate in an isolated network?
16.9. What are the network access requirements?
16.10. Are there limits on infrastructure costs?
16.11. Is automatic scaling required?
16.12. Who is responsible for the infrastructure and its operation?
16.13. Are there requirements for portability between providers?
16.14. How should updates be performed without stopping the service?

## 17. Operations, monitoring, and support
**Goal:** determine how the product will be maintained after launch.

17.1. Who will operate the system?
17.2. Who responds to incidents?
17.3. Is 24/7 support needed?
17.4. Which operational metrics need to be tracked?
17.5. Which events should trigger alerts?
17.6. Are centralized event logs needed?
17.7. Is distributed request tracing (distributed tracing) required?
17.8. How will a particular user's problem be diagnosed?
17.9. Are administrative tools needed?
17.10. Is auditing of operator actions required?
17.11. How are updates and rollbacks performed?
17.12. What are the incident response time requirements?
17.13. How will infrastructure costs be controlled?
17.14. Are system status reports for clients needed?

## 18. Development, testing, and delivery
**Goal:** determine constraints on the product development process.

18.1. Who develops the system?
18.2. What is the size and composition of the team?
18.3. Which technologies does the team already use?
18.4. Is there a mandatory technology stack?
18.5. What are the deadlines for the MVP release?
18.6. What budget is available?
18.7. How often are releases planned?
18.8. Is continuous delivery (CI/CD) required?
18.9. Which types of testing are mandatory?
18.10. Are load tests needed?
18.11. What are the test automation requirements?
18.12. Who accepts the completed functionality?
18.13. What acceptance criteria are used?
18.14. How will changes to requirements be managed?
18.15. Is backward compatibility required during updates?
18.16. Are there restrictions on licenses and the use of open source?

## 19. Monetization, pricing plans, and billing
**Goal:** determine commercial mechanisms if they are part of the product.

19.1. How does the product earn money?
19.2. Are there free and paid plans?
19.3. What determines the cost of use?
19.4. Are subscriptions or one-time payments needed?
19.5. Which functions are restricted by pricing plans?
19.6. Are usage limits needed?
19.7. How is resource consumption measured (metering)?
19.8. Which payment providers are used?
19.9. Are invoices, refunds, taxes, and documents needed?
19.10. What happens when a payment fails?
19.11. How are pricing plan changes handled?
19.12. Are individual commercial terms required for clients?

## 20. Analytics and reporting
**Goal:** determine what data is needed for decision-making and monitoring product operation.

20.1. Which product metrics are needed?
20.2. Which user events need to be tracked?
20.3. Are reports for users needed?
20.4. Are reports for administrators and the business needed?
20.5. Are analytics dashboards (dashboards) required?
20.6. How quickly should analytics data be updated?
20.7. What historical period is needed?
20.8. Are analytics by organization, user, and segment needed?
20.9. Is analytics data export required?
20.10. Are A/B tests and product experiments needed?
20.11. Which data must not be collected for analytics?
20.12. Are forecasting and anomaly detection needed?

## 21. Notifications and communications
**Goal:** determine ways of informing users.

21.1. Which events should trigger notifications?
21.2. Which channels are needed: email, push, SMS, in-app, webhooks?
21.3. Which notifications are critical?
21.4. Which notifications can be sent with a delay?
21.5. Can a user manage notification settings?
21.6. Are message templates and localization needed?
21.7. Are mass mailings needed?
21.8. Does delivery and read status need to be tracked?
21.9. What are the limits on sending frequency?
21.10. What should be done when a delivery channel is unavailable?
21.11. Are messages between users needed?
21.12. Is a communication history required?

## 22. AI, ML, and automated agents
**Goal:** determine requirements for intelligent functions if they are planned.

22.1. Which tasks should be solved using AI/ML?
22.2. What input data is used?
22.3. What results are expected?
22.4. What accuracy and error rate are acceptable?
22.5. Which decisions can AI make independently?
22.6. Which actions require human confirmation?
22.7. Can data be sent to external AI providers?
22.8. Are there requirements for model hosting?
22.9. Is working with the product's own data (RAG) required?
22.10. Are memory and context between sessions needed?
22.11. What are the limits on the cost of AI operations?
22.12. What are the response latency requirements?
22.13. Are reproducibility and explainability of results needed?
22.14. How is the quality of AI functions evaluated?
22.15. What should happen when the AI provider is unavailable?
22.16. Can agents perform actions in external systems?
22.17. What restrictions and permissions apply to agents?
22.18. How are unwanted automated actions prevented?

## 23. Migration and compatibility
**Goal:** determine requirements when replacing or extending existing systems.

23.1. Is there a previous version of the product?
23.2. What data needs to be transferred?
23.3. Where will the data come from, and in what format?
23.4. What are the migration volumes?
23.5. Is stopping the existing system acceptable?
23.6. Is parallel operation of the old and new systems required?
23.7. Which integrations must continue to work?
23.8. Is compatibility with old client applications needed?
23.9. How will the correctness of the transfer be verified?
23.10. Is migration rollback possible?
23.11. Who is responsible for the quality of the source data?
23.12. When can the old system be shut down?

## 24. Constraints, trade-offs, and priorities
**Goal:** identify factors that determine the architecture more strongly than individual functions.

24.1. Which requirements are absolutely mandatory?
24.2. Which requirements allow trade-offs?
24.3. Which is more important: development speed, cost, performance, or scalability?
24.4. Which is more important: availability or strict data consistency during network failures?
24.5. Which is more important: system flexibility or implementation simplicity?
24.6. Which requirements may change in the near future?
24.7. Which future changes are most likely?
24.8. Which architectural risks are considered unacceptable?
24.9. Which decisions have already been made and cannot be changed?
24.10. Which assumptions have not yet been confirmed?
24.11. Which questions can safely be deferred?
24.12. Which decisions will be expensive to change after launch?
24.13. Which criteria determine whether the architecture is ready for implementation?

---

## Handoff: rules for the next person carrying out the work

1. Use this document as a complete reference for Product Definition areas and questions, rather than as a list of mandatory sequential utterances.
2. First establish the basic product outline at L1, then architecturally significant uncertainties at L2, then L3 details.
3. Do not propose or attribute to the PO decisions to which the PO has not agreed.
4. Every product decision must have a reference to the original question and answer.
5. Preserve open questions, contradictions, unknown values, and explicitly inapplicable areas.
6. Do not consider an area “sufficiently defined” merely because many questions have been asked about one specific topic.
7. Before architectural design, prepare a requirements summary, a coverage map, the main risks, and a list of remaining decisions.

**Document boundary:** this is a catalog of aspects and an interview methodology, rather than a product specification for a particular application or a ready-made architectural solution.
