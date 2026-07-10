# AI Editorial Office Backlog

This backlog is the Project Lead management plan for executing the current
`ROADMAP.md`.

The backlog is operational planning. It is not architecture, governance, canon,
or a replacement for canonical project files.

Release model:

```text
One release
->
One Codex mission
->
One release candidate
->
Project Lead review
->
Done
```

Allowed release statuses: Not Started, In Progress, Review, Done.

Current active release candidate: `S5.R4 - Task Need Recognition`.

Current active work:

```text
S5.R4 Release Candidate

↓

Project Lead Review
```

Stage 5 is active. S5.R3 is `Done`, S5.R4 is in `Review`, and S5.R5 remains
`Not Started`. Do not start S5.R5 automatically.

# Stage 1 - Architecture Foundation

| Release ID | Title | Purpose | Expected Result | Success Criteria | Status |
| --- | --- | --- | --- | --- | --- |
| S1.R1 | Operating Architecture Baseline | Establish the basic operating shape of AI Editorial Office. | Stable role accountability, task handling, and independent review are available for project work. | The office can run editorial tasks with clear ownership, restartable task state, and mandatory independent review. | Done |
| S1.R2 | Canonical Ownership Baseline | Prevent competing sources of operational truth. | Canonical ownership boundaries are clear enough to guide future changes. | Permanent rule areas have named owners, and non-owner files do not override canonical files. | Done |

# Stage 2 - Architecture Validation

| Release ID | Title | Purpose | Expected Result | Success Criteria | Status |
| --- | --- | --- | --- | --- | --- |
| S2.R1 | Architecture-in-Use Validation | Prove the foundation works on real editorial and implementation work. | The architecture is trusted through representative task execution. | Real tasks can move through intake, production, review, validation, and finalization without architecture changes. | Done |
| S2.R2 | Memory and Release Validation | Prove memory export and release-candidate work can stay aligned with the repository. | External memory and release review boundaries are stable. | Memory remains non-canonical, and release candidates remain distinct from Project Lead accepted releases. | Done |

# Stage 3 - Professional Capability Model

| Release ID | Title | Purpose | Expected Result | Success Criteria | Status |
| --- | --- | --- | --- | --- | --- |
| S3.R1 | Analytical Reasoning | Add inspectable reasoning capability for complex editorial and implementation decisions. | Analytical reasoning is available as a bounded shared capability. | The capability improves task reasoning without adding a new role, pipeline, lifecycle stage, or governance owner. | Done |
| S3.R2 | Architecture Review | Add architectural review capability for design-significant work. | Architecture Review is available as a bounded shared capability. | The capability supports drivers, tradeoffs, risks, and rationale review without replacing canonical architecture owners. | Done |
| S3.R3 | Engineering Review | Add professional engineering review capability for implementation and change safety. | Engineering Review is available as one shared capability with optional review lenses. | Engineering Review covers engineering review needs without new roles, pipelines, lifecycle stages, or duplicate owners. | Done |
| S3.R4 | Professional Analysis | Add professional analysis capability for structured interpretation, judgment, and recommendation work. | Professional Analysis release candidate is ready for Project Lead review. | The release improves analysis quality, defines bounded use, and preserves existing architecture. | Review |
| S3.R5 | Professional Communication | Add professional communication capability for audience-fit, clarity, and decision-oriented messaging. | Professional Communication release candidate is ready for Project Lead review. | The release improves communication quality without creating a new writing role, pipeline, or mandatory artifact set. | Done |
| S3.R6 | Knowledge Evolution | Add capability for deliberate learning, canon evolution, stale knowledge handling, and retirement. | Knowledge Evolution release candidate is ready for Project Lead review. | The release improves learning from work without automatic canon promotion or new governance layers. | Done |

# Stage 4 - Domain Expertise

| Release ID | Title | Purpose | Expected Result | Success Criteria | Status |
| --- | --- | --- | --- | --- | --- |
| S4.R1 | Domain Knowledge Pack Standard | Define the management standard for future domain expertise packs. | Domain Knowledge Pack Standard is accepted and available. | The standard defines what a domain pack must provide without becoming architecture, governance, or a new pipeline. | Done |
| S4.R2 | Software Architecture Domain Pack | Add deep software architecture knowledge for architecture-sensitive tasks. | Software Architecture Domain Pack is accepted and active. | The pack improves architecture-related work and integrates cleanly with Architecture Review and Engineering Review. | Done |
| S4.R3 | DevSecOps Domain Pack | Add deep DevSecOps knowledge for delivery, automation, configuration, and secure operations work. | DevSecOps Domain Pack is accepted and active. | The pack improves DevSecOps-related work without duplicating Engineering Review ownership. | Done |
| S4.R4 | Cybersecurity Domain Pack | Add deep cybersecurity knowledge for security-sensitive tasks. | Cybersecurity Domain Pack is accepted and active. | The pack improves security-sensitive work with clear safety boundaries and source-aware guidance. | Done |
| S4.R5 | AI Engineering Domain Pack | Add deep AI engineering knowledge for model, evaluation, data, prompt, and reliability work. | AI Engineering Domain Pack is accepted and active. | The pack improves AI-engineering-related work and integrates cleanly with existing professional capabilities. | Done |

# Stage 5 - Editorial Intelligence

| Release ID | Title | Purpose | Expected Result | Success Criteria | Status |
| --- | --- | --- | --- | --- | --- |
| S5.R1 | Feedback and Learning Intelligence | Improve how the office learns from completed work and Project Lead feedback. | Feedback and Learning Intelligence release candidate is ready for Project Lead review. | The release turns feedback into bounded learning without automatic canon changes. | Done |
| S5.R2 | Evaluation Signals | Improve how the office recognizes quality, risk, and release health. | Evaluation Signals release candidate is ready for Project Lead review. | The release provides useful evaluation signals without replacing human review or Project Lead acceptance. | Done |
| S5.R3 | Memory Hygiene Intelligence | Improve how external memory stays aligned, small, and non-canonical. | Memory Hygiene Intelligence release candidate is ready for Project Lead review. | The release reduces memory drift without making memory a second source of truth. | Done |
| S5.R4 | Task Need Recognition | Improve how the office recognizes task type, risk, evidence needs, and capability triggers. | Task Need Recognition release candidate is ready for Project Lead review. | The release improves routing decisions without bypassing Chief Editor judgment or preflight discipline. | Review |
| S5.R5 | Editorial Intelligence Acceptance | Define how self-improvement releases are judged as accepted and stable. | Editorial Intelligence Acceptance release candidate is ready for Project Lead review. | The release helps larger work packages require less micromanagement while preserving stable architecture. | Not Started |
