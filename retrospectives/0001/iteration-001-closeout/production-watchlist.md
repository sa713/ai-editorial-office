# Production watchlist

Watch these signals across the next 10-20 production tasks.

## Compact path abuse

- Signal: tasks marked compact despite high-governance, source conflict, or material claims.
- Why dangerous: compact becomes governance bypass.
- What to do if detected: stop compact use for that task and reroute to normal/full depth.

## Artifact regrowth

- Signal: simple tasks again create full artifact sets without downstream need.
- Why dangerous: iteration fails to reduce friction.
- What to do if detected: record which artifacts changed no decision and remove them from future task scope.

## Unnecessary context-summary

- Signal: `context-summary.md` appears in short tasks with clear manifest/status/handoff.
- Why dangerous: recovery artifact becomes routine paperwork.
- What to do if detected: keep context-summary exceptional and use manifest/handoff instead.

## Conditional artifacts becoming default

- Signal: `qa-checklist.md`, `review-summary.md`, `reviewer-notes.md`, or finalization notes appear by habit.
- Why dangerous: compact review collapses back into bureaucracy.
- What to do if detected: require a downstream consumer or risk reason.

## Orchestration bloat

- Signal: orchestration plans repeat pipelines, AGENTS rules, or full artifact contents.
- Why dangerous: orchestration stops being execution contract.
- What to do if detected: trim to pipeline, process depth, role route, artifact scope, review target, stop conditions.

## Review degradation

- Signal: compact review gives verdict without scope, independence, rationale, blockers, or next action.
- Why dangerous: review-gate becomes formal.
- What to do if detected: require compact review minimum before approval.

## Drift between docs

- Signal: same rule appears with different wording in AGENTS, pipelines, agents, templates, and project-state.
- Why dangerous: future agents choose convenient rule.
- What to do if detected: move rule to canonical owner and replace duplicates with short references.

## Hidden custom workflows

- Signal: task uses custom stages without mini-contract.
- Why dangerous: exception becomes invisible pipeline.
- What to do if detected: add mini-contract or choose an existing pipeline.

## Review becoming shallow

- Signal: repeated approvals without evidence, caveats, or reader outcome check.
- Why dangerous: quality gate loses editorial value.
- What to do if detected: return to normal review depth for the next similar task.

## Governance confusion

- Signal: `finalized` treated as published, delivered, or human-approved.
- Why dangerous: side effects happen without owner approval.
- What to do if detected: correct manifest/final decision and require explicit approval state.
