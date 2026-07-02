# Safety check

## Step boundary

- [x] Step 1 only.
- [x] Inventory and analysis only.
- [x] No automatic replacement performed.
- [x] Step 2 not started.

## Files intentionally created

- [x] `retrospectives/system-maintenance-retrospective-0012/step-001/implementation-plan.md`
- [x] `retrospectives/system-maintenance-retrospective-0012/step-001/mvp-inventory.md`
- [x] `retrospectives/system-maintenance-retrospective-0012/step-001/active-policy-findings.md`
- [x] `retrospectives/system-maintenance-retrospective-0012/step-001/historical-findings.md`
- [x] `retrospectives/system-maintenance-retrospective-0012/step-001/replacement-strategy.md`
- [x] `retrospectives/system-maintenance-retrospective-0012/step-001/safety-check.md`

## Files intentionally not changed

- [x] `ai-editorial-office/AGENTS.md`
- [x] `ai-editorial-office/project-state.md`
- [x] `ai-editorial-office/agents/*.md`
- [x] `ai-editorial-office/pipelines/*.md`
- [x] `ai-editorial-office/templates/**/*.md`
- [x] `editorial_knowledge/*.md`
- [x] `ai-editorial-office/kb/*.md`

## Active risk findings

- `MVP` affects role admissibility in `AGENTS.md`, `chief_editor.md`, all pipeline role sections, `agent_template.md`, and KB policy.
- `MVP` affects pipelines through default role rules, blocker/escalation conditions, handoff target checks, and restart checks.
- `MVP` affects governance through Chief Editor assignment rules and active-state / policy wording.
- `MVP` can conflict with Artist Agent if replacement collapses `non-MVP extension` into a blanket extension ban or makes Artist Agent a universal production role.
- `MVP` affects meaning in status rules: the direct `writing` / `ux-writing` -> `review` transition and optional `editing` bridge must survive any replacement.

## Replacement safety rules

- Do not use a single global replacement.
- Replace role-set language separately from workflow/status language.
- Preserve the distinction between:
  - core role;
  - legalized extension role;
  - unauthorized extension role.
- Keep Artist Agent bounded to visual-branch conditions.
- Keep no separate Editor Agent in the default operating model.
- Keep direct writing-to-review rules intact.
- Leave historical files unchanged unless a later task explicitly asks for historical cleanup.

## Verification notes

Searches completed:

- Active policy search for `\bMVP\b`.
- Historical search for `\bMVP\b`.
- Requested phrase-family search for `MVP role`, `MVP agent`, `MVP workflow`, `MVP architecture`, `MVP phase`.

Observed:

- Active policy has `MVP` mentions in 14 files.
- `editorial_knowledge/*.md` has no `MVP` mentions.
- `MVP architecture` and `MVP phase` were not found as exact active phrases.
- Historical task and retrospective files contain many `MVP` mentions that should remain audit history.

No working policy files were edited as part of this step.
