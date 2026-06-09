# Brief

## raw request summary

Implement P2: make the informal Codex task and check-pack format a compact
production standard in the editorial office.

## user goal

- confirmed: turn normalized briefs into quality Codex tasks;
- confirmed: define a compact check-pack for review;
- confirmed: keep the update small and avoid new roles, governance layers,
  capability packs, validators, or review-gate changes.

## audience / reader

- confirmed: editorial system maintainers and future Codex/ChatGPT reviewers;
- inferred: Chief Editor and Intake Agent are the main workflow readers.

## expected artifact

- confirmed: production patch, `implementation-notes.md`, `check-pack.md`, and
  `chatgpt_p2.md`;
- inferred: compact system update with examples.

## source status

- sources used: root `AGENTS.md`, `ai-editorial-office/AGENTS.md`,
  `project-state.md`, `master_backlog.md`, `chief_editor.md`,
  `intake_agent.md`, templates, KB index, scripts README, and task-pack helper;
- source status: local markdown and script sources available and read;
- source boundary: production rules override backlog if conflicts exist.

## constraints

- Change only files that genuinely own task generation or the P2 backlog state.
- Do not add agents, roles, pipelines, capability packs, validators, or
  governance layers.
- Do not change review-gate.
- Do not rewrite lifecycle or unrelated templates.
- Keep the standard compact.

## explicit requirements

- Identify current owner of Codex task generation logic.
- Add compact Codex task standard.
- Add compact check-pack standard.
- Connect P1.5 normalized brief to P2 Codex task/check-pack flow.
- Add short sanitized examples.
- Update backlog.
- Create `implementation-notes.md`, `check-pack.md`, and `chatgpt_p2.md`.

## assumptions

- Chief Editor is the production owner for normalized brief -> Codex task
  routing because it owns orchestration, preflight, scope, roles, and routing.
- A KB file is the smallest appropriate home for the reusable fillable standard.
- `generate_task_pack.py` should remain a read-only context helper.

## open questions

- `/about` is referenced in project state but absent in this checkout; memory
  package sync cannot be completed here.

## acceptance criteria

- Owner is identified and recorded.
- Compact Codex task standard exists.
- Compact check-pack standard exists.
- P1.5 and P2 form a continuous chain.
- Examples are present.
- No new role/governance/review-gate layer is added.
- Backlog is updated.

## suggested task type / pipeline

- Task type: compact system update / reusable standard.
- Pipeline: custom compact Chief Editor route.

## risks

- The standard could become too bureaucratic.
- Check-pack could be misread as replacing `review.md`.
- New KB file must be discoverable without becoming a new governance owner.
