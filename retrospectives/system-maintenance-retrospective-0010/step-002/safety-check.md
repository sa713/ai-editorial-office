# Safety Check

## Scope Safety

- [x] Step 2 only.
- [x] No Step 3-6 implementation started.
- [x] No automation added.
- [x] No context engine added.
- [x] No new production artifact type added.
- [x] No role changes.
- [x] No pipeline replacement.
- [x] No governance model change.
- [x] No review optionality introduced.

## Context Loading Safety

- [x] Short context path is defined for ordinary restart and stage transition.
- [x] Compact / low-risk, standard, and high-governance expansion levels are defined.
- [x] Whole-project reading is explicitly disallowed by default.
- [x] Reading all retrospectives, task folders, versions, pipelines, agent specs, or editorial knowledge is explicitly disallowed by default.
- [x] Legacy task folders are history, not templates.
- [x] Old artifact versions are conditional reading only.
- [x] Current-version pointer requirement is added for version-heavy tasks.

## Governance Safety

- [x] Review remains mandatory.
- [x] High-governance can expand reading.
- [x] Source/evidence files remain available when traceability is needed.
- [x] Status history remains available for conflict or restart uncertainty.
- [x] Review trail and governance artifacts remain available for finalization/governance decisions.

## Search Checks

Checked for stale broad-restart wording:

- `Detailed files commonly needed`;
- `Receiving or restarting agents must read`;
- task-template restart lists loading `/project-state.md`, all status files, all pipelines, and role specs by default;
- role specs with mandatory broad preload lists;
- whole-project/default broad reading.

Remaining broad-reading matches are negative guardrails, such as "Do not read all pipelines..." or "Do not load the whole project by default."
