# Research Task Template

## template purpose

Use for evidence gathering, source review, claim validation, factual sensitivity
mapping, or research handoff. This template supports traceability without
turning research into writing or review. The file lists below are scaffolding
defaults; they do not override pipeline conditionality, evidence depth, compact
execution, or canonical ownership.

## when to use

- The task needs verified facts before writing or UX writing.
- Claims, sources, dates, numbers, policy statements, or product behavior need
  traceability.
- High-governance work requires source/evidence coverage.
- A downstream role needs a research handoff.

## folder structure

```text
tasks/TASK-ID/
  brief.md
  task-manifest.md
  status.md
  research.md
  review.md
```

Conditional files:

- `orchestration_plan.md`
- `sources.md`
- `facts.md`
- `claims_table.md`
- `open-questions.md`
- `handoff-*.md`
- `qa-checklist.md`
- `review-summary.md`
- `final_decision.md`

## required files

- `brief.md`
- `task-manifest.md`
- `status.md`
- `research.md`
- `review.md` before research is treated as ready for delivery or governance.

## conditional artifact rules

- `sources.md`, `facts.md`, and `claims_table.md` are required when claim-level
  traceability is needed.
- `open-questions.md` is created only for real unresolved questions or blockers.
- Separate review artifacts beyond `review.md` are conditional.
- Final governance artifacts are created only when the selected pipeline or risk
  mode requires them.

## bootstrap

1. Capture research goal and scope in `brief.md`.
2. Set current state, version pointers, and `client_profile` fields when a
   client profile is considered in `task-manifest.md`.
3. Record current status in `status.md`.
4. Add `orchestration_plan.md` when research scope, roles, or governance need a
   contract.
5. Create traceability files only when the research depth requires them.

## brief.md scaffold

```markdown
# Brief

## task title

## research goal

## questions to answer

## audience or downstream role

## source materials

## factual sensitivity

## risk mode

## constraints

## client profile

## success criteria

## open questions
```

## research.md scaffold

```markdown
# Research

## research scope

## executive summary

## key findings

## confirmed facts

## interpretations

## contradictions

## gaps

## confidence notes

## implications for downstream work

## do-not-say list

## Product Intent Review, only when mode is limited or full

- Mode and bounded focus:
- Supported product-intent elements:
- Product checks in scope:
- Confirmed evidence:
- Assumptions and hypotheses:
- Unknowns and contradictions:
- Disconfirming evidence:
- Evidence sufficient for analytical owner: yes/no and why
```

## sources.md scaffold

```markdown
# Sources

| Source | Type | Date | Reliability | Checked? | Used for | Notes |
| --- | --- | --- | --- | --- | --- | --- |
```

## facts.md scaffold

```markdown
# Facts

| Fact | Evidence | Confidence | Sensitivity | Notes |
| --- | --- | --- | --- | --- |
```

## claims_table.md scaffold

```markdown
# Claims Table

| Claim | Source/evidence | Confidence | Sensitivity | Safe for downstream use? |
| --- | --- | --- | --- | --- |
```

## factual sensitivity

- Low / medium / high / critical:
- Reason:
- Claims requiring human or governance attention:

## open questions

Create `open-questions.md` only if questions are real and actionable.

```markdown
# Open Questions

| Question | Owner | Blocking? | Needed by | Notes |
| --- | --- | --- | --- | --- |
```

## downstream handoff

Use `handoff_template.md`. Include scope, usable findings, caveats,
contradictions, do-not-say items, evidence gaps, and next role.

## review.md scaffold

```markdown
# Review

## reviewed artifacts

## reviewer independence

## evidence validation

## traceability validation

## blockers

## required changes

## outcome

approved / changes_requested / blocked

## next action
```

## completion checklist

- Research scope answered or gaps are explicit.
- Sources and claim traceability exist when required.
- Contradictions and confidence limits are visible.
- `review.md` exists before delivery/governance.
- Open questions are real, owned, and marked blocking or non-blocking.

## restart checklist

Read:

- `AGENTS.md` or invariant summary;
- `task-manifest.md`;
- latest relevant handoff;
- current research artifact;
- directly relevant pipeline/KB/source files.
