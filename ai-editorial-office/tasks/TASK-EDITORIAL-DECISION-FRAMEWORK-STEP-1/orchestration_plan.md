# Orchestration Plan

## task summary

- Task ID: `TASK-EDITORIAL-DECISION-FRAMEWORK-STEP-1`
- User goal: design a minimal editorial decision mechanism before writing.
- Deliverable: proposal and implementation plan, not production code changes.
- Audience/channel: project owner in chat and task-local proposal.
- Current active version: `system_change_proposal.md`

## task classification

- Task type: system design / system-change proposal.
- Risk mode: `high-governance`, because the future change affects all editorial
  workflows.
- Factual sensitivity: low; architectural accuracy matters.
- Human approval likely required: yes.
- Rationale: changing editorial routing rules affects role boundaries, artifact
  depth, review criteria, and restart behavior.

## selected pipeline

- Pipeline: no existing production pipeline; Chief Editor design-only mode.
- Why this pipeline: the request is to design a system change, not to write an
  article, social copy, UX copy, or review a draft.
- Pipeline exceptions or local constraints: production implementation is out of
  scope for step 1.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `confirmed` |
| Channel or context | `confirmed` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `proceed` |

- Rationale: repository architecture is available; user explicitly asks for a
  design proposal only.
- Production may start: no production architecture edits in step 1.
- If `constrain`: scope is proposal-only.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Orchestration/design | Chief Editor | yes | Owns system routing proposal |
| Review | Review Agent | future | Required before production change is accepted |

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | Chief Editor | Normalized request |
| `task-manifest.md` | required | all roles | Restart state |
| `status.md` | required | Chief Editor | Planning state |
| `system_change_proposal.md` | conditional | user / future reviewer | Proposal content |
| `review.md` | omitted in step 1 | future implementation | No production change is being approved yet |
| `final_decision.md` | omitted in step 1 | future governance | No final system update is being closed yet |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | Chief Editor | Current architecture files | Proposal | Minimal design documented |
| 2 | User | Proposal | Decision | Implementation authorized, revised, or rejected |

## completion criteria

- Proposal answers all user questions.
- No production architecture files are modified.
- `git status --short` is reported.
