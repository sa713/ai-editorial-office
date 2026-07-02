# Step 4 Template Compression Decisions

## Canonical Ownership

Templates no longer repeat the full operating model. They now point briefly to
canonical owners:

- `AGENTS.md` owns global authority, governance, artifact depth, review-gate,
  context loading, and task-local storage.
- Pipelines own stage sequence and process conditions.
- Agent specs own role behavior and boundaries.
- Templates own fillable shape, required fields, conditional creation rules, and
  downstream handoff fields.

## Retained In Templates

The compressed templates retain:

- purpose and use conditions;
- mandatory fields;
- short fill prompts;
- conditional creation rules;
- downstream consumer notes where relevant;
- risk mode and process depth fields;
- blockers and open questions;
- review verdict and reviewer independence fields;
- human approval and final decision fields;
- source/evidence fields where claims or product behavior require traceability;
- current-version pointer requirement in `task_manifest_template.md`;
- short restart read path from Step 2.

## Removed Or Shortened

The following were removed or replaced by short references:

- repeated `AGENTS.md` prose;
- pipeline sequence duplication;
- role behavior explanations;
- artifact minimalism policy prose;
- context-loading policy prose;
- long explanations of why a field matters;
- stale requirements that made conditional artifacts look routine or mandatory;
- full lifecycle checklists duplicated across task templates.

## Conditional Artifact Decisions

- `review.md` remains required and primary.
- `qa-checklist.md` and `review-summary.md` remain conditional.
- `open-questions.md` is created only for real questions, blockers, or
  traceability gaps.
- `finalization-notes.md` and `finalization-checklist.md` remain conditional.
- Task templates list conditional files but do not require creating them by
  default.

## Governance Preservation

Governance-critical fields were preserved in compact form:

- `task_manifest_template.md`: current state, risk mode, process depth,
  current-version pointers, review state, human approval state, artifact
  inventory, next action packet.
- `orchestration_plan_template.md`: classification, process depth, pipeline,
  required agents, evidence, artifact scope, review requirements, human
  approval, escalation, completion/finalization/restart notes.
- `status_template.md`: current status, history, owner, required/missing
  artifacts, blockers, questions, review state, human approval, escalation,
  risk, checkpoint, readiness.
- `final_decision_template.md`: reviewed artifacts, review validation,
  required artifact validation, KB/policy validation, unresolved risks/questions,
  human approval, final readiness, decision, follow-up, restart notes.

## No External Changes Needed

No Step 4 need required editing `AGENTS.md` or pipelines. Any broader ownership
questions are already covered by Step 1-3 canonical owner rules.
