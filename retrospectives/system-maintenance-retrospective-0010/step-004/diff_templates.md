# Step 4 Template Diff

This file records the per-template diff summary for every changed file under
`ai-editorial-office/templates/**/*.md`.

## Line Count Diff

| File | Before | After | Delta |
| --- | ---: | ---: | ---: |
| `ai-editorial-office/templates/agent_template.md` | 279 | 77 | -202 |
| `ai-editorial-office/templates/artifacts/final_decision_template.md` | 424 | 110 | -314 |
| `ai-editorial-office/templates/artifacts/handoff_template.md` | 96 | 57 | -39 |
| `ai-editorial-office/templates/artifacts/orchestration_plan_template.md` | 413 | 151 | -262 |
| `ai-editorial-office/templates/artifacts/status_template.md` | 417 | 129 | -288 |
| `ai-editorial-office/templates/artifacts/task_manifest_template.md` | 166 | 89 | -77 |
| `ai-editorial-office/templates/tasks/article_task_template.md` | 823 | 248 | -575 |
| `ai-editorial-office/templates/tasks/research_task_template.md` | 752 | 207 | -545 |
| `ai-editorial-office/templates/tasks/review_task_template.md` | 367 | 181 | -186 |
| `ai-editorial-office/templates/tasks/social_task_template.md` | 961 | 231 | -730 |
| `ai-editorial-office/templates/tasks/ux_writing_task_template.md` | 1069 | 255 | -814 |
| Total | 5767 | 1735 | -4032 |

## `ai-editorial-office/templates/agent_template.md`

```diff
- Repeated AGENTS rules, artifact minimalism, context loading, review triggers,
- prompt behavior, failure behavior, KB/pipeline loading, and artifact policy.
+ Replaced with compact approved-role form:
+ role, mission, responsibilities, inputs, outputs, forbidden actions, decision
+ boundaries, stop conditions, handoff expectations, role-specific checks, and
+ canonical references.
```

## `ai-editorial-office/templates/artifacts/final_decision_template.md`

```diff
- Full governance prose, detailed decision rules, repeated artifact validation
- explanations, KB policy, publication readiness prose, and restart policy.
+ Compact final decision form preserving decision metadata, reviewed artifacts,
+ review validation, required artifact validation, KB/policy validation,
+ unresolved risks/questions, human approval, readiness, decision, follow-up,
+ escalation, archival, and restart notes.
```

## `ai-editorial-office/templates/artifacts/handoff_template.md`

```diff
- Longer handoff instructions and repeated rationale.
+ Compact delta-transfer form with metadata, reason, changed artifacts,
+ constraints, blockers/questions, next action, validation, and escalation.
+ Explicitly keeps `compact-handoff.md` non-automatic.
```

## `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`

```diff
- Long orchestration explanations, policy prose, repeated lifecycle and artifact
- rules, and broad restart guidance.
+ Compact execution contract preserving task summary, classification, process
+ depth, selected pipeline, custom workflow mini-contract, required agents,
+ evidence, artifact scope, structure plan, execution order, status transition,
+ review, human approval, risks, questions, escalation, completion,
+ finalization, and restart fields.
```

## `ai-editorial-office/templates/artifacts/status_template.md`

```diff
- Long state-management explanations and repeated readiness rules.
+ Compact status form preserving task metadata, current status, history, owner,
+ required/missing artifacts, blockers, questions, review state, human approval,
+ escalation, retry, risk, assumptions, latest handoff, checkpoint, completion,
+ finalization, and archival readiness.
```

## `ai-editorial-office/templates/artifacts/task_manifest_template.md`

```diff
- Longer current-state explanations and restart/context policy prose.
+ Compact manifest preserving task identity, current state, freshness,
+ current-version pointers, governance state, artifact inventory, conflicts,
+ constraints, open questions, next action packet, and lifecycle notes.
```

## `ai-editorial-office/templates/tasks/article_task_template.md`

```diff
- Long lifecycle template with detailed scaffolds for every possible article
- artifact, repeated review/finalization/governance rules, and broad restart
- guidance.
+ Compact article task form with purpose, required/conditional files, bootstrap,
+ brief, conditional research/evidence, writing, review, final, handoff,
+ completion, and restart scaffolds.
```

## `ai-editorial-office/templates/tasks/research_task_template.md`

```diff
- Long research lifecycle and optional review/governance scaffolds with repeated
- policy prose.
+ Compact research task form preserving research scope, sources, facts,
+ claims table, factual sensitivity, open questions, downstream handoff,
+ review scaffold, completion, and restart fields.
```

## `ai-editorial-office/templates/tasks/review_task_template.md`

```diff
- Review task template repeated review policy and separate optional artifacts in
- a way that increased routine file depth.
+ Compact review task form preserving reviewed material, required `review.md`,
+ independence, validation summary, findings, blockers, required changes,
+ outcome, confidence, optional checklist/summary/notes, handoff, and
+ completion checks.
```

## `ai-editorial-office/templates/tasks/social_task_template.md`

```diff
- Long social lifecycle with repeated governance/finalization/restart rules and
- extensive optional artifact scaffolds.
+ Compact social task form preserving platform constraints, claims/evidence,
+ variants, writer notes, review, final copy, handoff, completion, and restart
+ fields.
```

## `ai-editorial-office/templates/tasks/ux_writing_task_template.md`

```diff
- Long UX lifecycle with repeated role, product, review, finalization,
- governance, and restart policy prose.
+ Compact UX writing task form preserving product context, terminology,
+ UX copy, content map, states table, UX writer notes, claim traceability,
+ review, final, handoff, completion, and restart fields.
```
