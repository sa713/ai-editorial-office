# Brief

## Task identity

- Task ID: `TASK-TASK-NEED-RECOGNITION-RELEASE`
- Release ID: `S5.R4`
- Title: Task Need Recognition Release
- Date opened: 2026-07-10

## Goal

Complete `S5.R4 - Task Need Recognition` through Release Candidate state so AI
Editorial Office can recognize task type, likely capability and Domain Pack
needs, justified research and review depth, evidence expectations, risk,
architectural/engineering/communication significance, ambiguity,
decomposition need, and uncertainty before work begins.

Recognition supports Chief Editor routing. It never performs routing,
activation, planning, review-depth selection, or governance decisions.

## Audience and outcome

- Primary audience: Project Lead.
- Operational users: Intake Agent and Chief Editor, with Research Agent and
  Review Agent consuming recorded route context when material.
- Outcome: a researched, architecture-compatible, implemented, validated,
  independently reviewed, committed Release Candidate ready for Project Lead
  architectural review.
- Release acceptance remains a later Project Lead decision.

## Required deliverables

- `../../research/task_need_recognition_landscape.md`
- `../../research/task_need_recognition_architecture_synthesis.md`
- `../../research/task_need_recognition_release_report.md`
- `../../releases/S5-R4/release-pack.md`
- smallest canonical integration through existing owners;
- representative ten-case validation;
- complete editorial task lifecycle and final local commit.

## Required behavior

Recognition should make a compact advisory view available for:

- task type;
- likely capabilities;
- likely Domain Packs;
- research depth;
- review depth;
- evidence expectations;
- architectural, engineering, and communication significance;
- risk, ambiguity, decomposition need, and uncertainty.

The view must distinguish observed request signals from recommendations and
Chief Editor decisions. Keyword presence alone is never sufficient.

## Constraints

- Chief Editor remains the routing and activation authority.
- No automatic routing, capability activation, Domain Pack activation, review
  level, planning, lifecycle transition, or governance action.
- No new roles, pipelines, lifecycle stages, review gates, status values, or
  autonomous planning.
- Reuse Chief Editor, Intake Agent, Professional Analysis, Evaluation Signals,
  Domain Pack activation, evidence, risk, and review owners.
- Prefer minimum architecture and avoid duplicate routing systems.
- Leave root `diff_intake.md` untouched.
- Do not touch `/Users/sa/Documents/codex/redaction`.
- S5.R4 may move to `Review`, never `Done`; S5.R5 must not start.

## Evidence and validation

- Prefer primary and authoritative sources for classification, triage, intake,
  decision support, and intent/task routing practice.
- Validate the ten representative cases from the mission.
- Demonstrate proportionate recommendations, multi-signal reasoning,
  non-activation on keyword-only requests, uncertainty, and explicit Chief
  Editor ownership.
- Run all relevant repository diff, canonical-memory, task-lifecycle,
  task-pack, direct task, smoke-test, and staged-diff checks.

## Done condition

Task Need Recognition is implemented through the smallest justified canonical
surface, all required artifacts and cases are complete, independent review is
approved, repository state and memory are aligned if material, the Release
Pack is complete, S5.R4 is `Review`, and one local Release Candidate commit
exists.
