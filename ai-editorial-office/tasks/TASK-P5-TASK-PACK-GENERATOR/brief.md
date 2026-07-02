This is a task-local system-update packet for P5. It does not contain real task
materials.

# Brief

## Goal

Tune `generate_task_pack.py` so source-based / compact-evidence tasks include
declared task-local evidence artifacts in writer and review_agent read sets.

## Context

P1 found one narrow issue: the source-based compact-evidence E2E case used
`source_summary.md` as a task-local evidence artifact, but writer and
review_agent task packs did not include it.

## Source Of Truth

- `AGENTS.md`
- `ai-editorial-office/AGENTS.md`
- `ai-editorial-office/ideas/master_backlog.md`
- `ai-editorial-office/scripts/generate_task_pack.py`
- `ai-editorial-office/tests/test_task_pack_generator.sh`
- first three sanitized E2E cases under
  `ai-editorial-office/tests/end_to_end_cases/`

## Working Scope

- Task pack generator.
- Task pack generator tests / synthetic fixtures.
- `ai-editorial-office/ideas/master_backlog.md`.

## Constraints

- Do not add agents, roles, pipelines, validators, or mandatory artifacts.
- Do not change review-gate.
- Do not turn task pack generation into a full task folder dump.
- Do not include all markdown files.
- Do not use latest modified as source of truth.
- Do not auto-activate client profiles.

## Acceptance Criteria

- Source-based / compact-evidence tasks include declared `source_summary.md` or
  equivalent task-local evidence summaries for writer and review_agent.
- Ordinary no-research tasks without source artifacts do not get extra source
  files.
- Client-profile files remain guarded by explicit active profile status.
- Smoke coverage includes positive, negative, and client-profile guard checks.
- Backlog records P5 as implemented.
