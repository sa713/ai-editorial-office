# Топ-3 улучшения

## 1. Ввести preflight gate перед production

### change

Перед writing, visual execution, conversion, rewriting or recommendation output
Chief Editor should require a compact preflight decision:

| Field | Required decision |
| --- | --- |
| Audience | confirmed / inferred / unknown |
| Channel/context of use | confirmed / inferred / unknown |
| Deliverable | exact artifact and use boundary |
| Source boundary | what facts may be used |
| Success criterion | what user/reader can do after output |
| Factual sensitivity | low / medium / high / critical |
| Approval boundary | editorial-ready vs publication/delivery-ready |
| Missing data decision | ask / constrain / proceed / block |

This can live inside `brief.md` or `orchestration_plan.md`; it does not need a
new role or heavy new artifact.

### why priority 1

Most high-impact failures start before production:

- direct tasks without lifecycle evidence;
- inferred audience/channel;
- unknown approval owner;
- missing source boundary;
- writing before success criteria are clear.

### problems addressed

- premature production;
- task misunderstanding;
- hidden assumptions;
- weak review scope;
- publication-readiness surprises;
- direct PDF/visual/output paths without editorial route.

### expected effect

Largest quality gain. It prevents the wrong task from being done well.

Expected behavioral changes:

- fewer direct outputs without traceability;
- clearer "ask vs constrain vs proceed" decisions;
- review can test against success criteria rather than only prose;
- compact tasks stay compact, but not under-specified.

## 2. Make review outcome-aware, not only artifact-aware

### change

Every `review.md` should include a short "task understanding check" before text
or checklist findings:

- What was the user's actual goal?
- What must the reader/user be able to do after this artifact?
- What assumptions did the system use?
- Which assumptions are confirmed, inferred, or unknown?
- Could the artifact be good but solve the wrong problem?
- Does any unresolved missing input block approval?

For compact tasks this can be six lines inside `review.md`; no separate
artifact is needed.

### why priority 2

Review currently catches text, structure, tone and claims well. It is less
consistent at catching the upstream error: the task itself may have been
understood too narrowly or inferred too confidently.

### problems addressed

- review passing a well-written but under-specified artifact;
- weak independence signal in compact review;
- task misunderstanding reaching finalization;
- inferred audience/channel becoming invisible.

### expected effect

Review becomes a stronger system-control mechanism. It will still catch prose
defects, but it will also protect the user's intended outcome.

Expected behavioral changes:

- more review findings about missing input or wrong scope;
- fewer final decisions that discover practical readiness issues late;
- better distinction between "approved as editorial artifact" and "ready for
  the user's real next action".

## 3. Add an adaptive artifact budget

### change

For each task, Chief Editor should set an artifact budget in orchestration:

- `compact`: brief, manifest, status, plan, working artifact, review, final
  decision; optional handoffs only when transition clarity needs them.
- `standard`: add writer notes, source snapshot, review details, and selected
  traceability artifacts.
- `full`: add research, sources, facts, claims table, QA, review summary,
  finalization notes only when downstream/governance consumes them.

Every optional artifact should answer:

```text
Who will use this file, and what decision becomes safer because it exists?
```

### why priority 3

The system has already learned that both extremes are harmful:

- too little process leaves no evidence;
- too much process creates context load and maintenance drag.

### problems addressed

- artifact bloat;
- copy-pasted full lifecycle for small tasks;
- missing evidence in direct tasks;
- unclear optional artifact value;
- review-summary/QA files created without consumer.

### expected effect

Higher velocity without weakening governance.

Expected behavioral changes:

- compact tasks become lighter and cleaner;
- full tasks remain traceable where risk justifies it;
- easier restartability because fewer files are decorative;
- Chief Editor decisions become more explicit and auditable.

## why not other changes first

Do not prioritize new roles now.

The corpus does not show a role shortage. It shows entry, review-scope and
depth-control issues. New roles would likely increase coordination cost before
improving quality.

Do not prioritize a new pipeline now.

Existing pipelines are flexible enough. The problem is inconsistent selection
and depth, not missing pipeline taxonomy.

Do not prioritize expanding visual subsystem now.

`TASK-0020` proves the visual semantic path can work, but `TASK-0016` -
`TASK-0019` show why direct visual production is risky. Keep visual frozen by
default until entry/review discipline is fully reliable.
