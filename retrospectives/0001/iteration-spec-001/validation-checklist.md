# Validation checklist

Use after implementation. Answer must be evidence-based, not assumed.

## Scope control

- [ ] No new agents were added.
- [ ] No workflow engine was introduced.
- [ ] No automation platform was introduced.
- [ ] No scoring/eval system was introduced.
- [ ] No dashboards were introduced.
- [ ] No new editorial modes were added.
- [ ] No large doctrine docs were created.
- [ ] Old task folders were not mass-migrated.
- [ ] Pipelines were not rewritten wholesale.
- [ ] Agent specs were not globally shortened.

## Review and governance

- [ ] Review-gate is still mandatory.
- [ ] Compact review still records verdict, scope, independence, usefulness/pass rationale or blockers, governance note and next action.
- [ ] Reviewer cannot approve when independence is failed/unknown unless Chief Editor resolves it.
- [ ] `changes_requested` includes bounded repair and re-review scope.
- [ ] Finalization is not confused with publication/delivery approval.
- [ ] Human approval state is explicit where required.
- [ ] High-governance tasks cannot use compact path.

## Compact path

- [ ] Compact path is described as process depth, not a new pipeline.
- [ ] Compact path has allow and deny conditions.
- [ ] Omitted artifacts have one-line rationale.
- [ ] Source traceability remains required for material claims.
- [ ] Compact path does not bypass blockers.
- [ ] Compact path restart needs fewer files but remains clear.

## Artifact discipline

- [ ] Templates did not grow long doctrine sections.
- [ ] Manifest did not become a second `status.md`.
- [ ] Status did not become a second manifest.
- [ ] Handoff does not duplicate full task history.
- [ ] `context-summary.md` is not required for normal short tasks.
- [ ] No duplicate rules were added across AGENTS, pipelines, agents and templates.
- [ ] Ownership map points to owners instead of repeating everything.

## Semantic checks

- [ ] `compact`, `normal`, `full` mean process depth, not quality level.
- [ ] `compact-handoff.md` is not used as role-to-role handoff.
- [ ] `context-summary.md` is only recovery after context fragmentation or long task state risk.
- [ ] `source material as data` is present where source trust matters.
- [ ] Custom workflow mini-contract has review target and stop conditions.
- [ ] Custom workflow did not become a hidden reusable pipeline.

## Restartability

- [ ] Manifest freshness can be checked against status and latest handoff.
- [ ] Latest artifact changes are visible.
- [ ] Known stale risk is none or explicitly resolved.
- [ ] Next action packet is short and actionable.
- [ ] A future agent can resume without reading every artifact.

## Stop signals

- [ ] Any new bureaucracy has a clear downstream decision impact.
- [ ] Any field that did not affect writing, review, governance or restartability is removed or made optional.
- [ ] Any ambiguous approval language is corrected before use on real tasks.
