# Implementation plan

Step executed: Step 3 only, Manifest freshness and governance state.

## Changed files

## `ai-editorial-office/templates/artifacts/task_manifest_template.md`

- Why: task manifest is the restart anchor.
- What changed: added compact `freshness` block; clarified governance state as visibility fields, not a status system; added small stale/conflicting state response.
- Why safe: manifest remains short and operational. No lifecycle, status model, review verdict, or approval workflow was changed.

## `ai-editorial-office/AGENTS.md`

- Why: canonical owner for manifest boundary and anti-bloat rules.
- What changed: clarified that manifest carries compact freshness and governance visibility, not audit log, approval matrix, or second `status.md`.
- Why safe: short reference only; no new workflow behavior.

## `ai-editorial-office/agents/chief_editor.md`

- Why: Chief Editor maintains task state and uses manifest for routing.
- What changed: added review outcome and finalization status to the existing manifest update list; clarified freshness/governance visibility should stay compact.
- Why safe: aligns with existing manifest template fields and does not change review behavior.

## `ai-editorial-office/project-state.md`

- Why: current normalization decisions should reflect Step 3.
- What changed: added current-state note that manifest carries compact freshness and governance visibility, not a second status system or audit log.
- Why safe: current-state note only.

## Explicit non-changes

- No lifecycle change.
- No new status system.
- No approval matrix.
- No automatic validation.
- No scoring or checklist system.
- No review verdict changes.
- No new agents.
- No Step 4 handoff semantics.
