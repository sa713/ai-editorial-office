# Deliverable Fit Analysis

## Decision

Do not create a new Product Intent Review deliverable profile.

The capability produces analysis semantics. The selected deliverable should
continue to follow the reader's job and the smallest sufficient outcome-fit
artifact, not capability naming.

## Reader-job mapping

| Reader job | Existing form | Why it fits | Product Intent adaptation |
| --- | --- | --- | --- |
| Quickly understand state/risk/next decision | `report`, compact block, or decision summary | General findings and next action; can remain short | verdict, one gap, next decision, evidence boundary, consequence |
| Choose continue/reduce/pilot/change/stop | `decision-memo` | Named decision, recommendation, alternatives, tradeoffs, risk, explicit ask | verdict first; bounded options; owner decision; validation/consequence |
| Inspect evidence, assumptions, mechanism, limits | `research-report` | Source/method boundary, evidence, contradictions, confidence, limitations | concise decision entry plus traceable evidence; no overclaim |
| Receive Product Intent Review inside broader review/analysis | embedded conditional block in selected deliverable | Preserves the primary reader job and avoids duplicate artifacts | product block precedes local editorial remarks |

## Why a new profile is unnecessary

- It would overlap `report` for general decision-ready findings.
- It would overlap `decision-memo` when the owner must choose among options.
- It would overlap `research-report` when evidence traceability is central.
- It would duplicate an embedded block when Product Intent Review is only one
  dimension of a larger requested review.
- Full depth is an analysis/review requirement, not proof of a distinct reader
  job or mandatory standalone artifact.
- Existing outcome-first selection can choose a standalone report only when the
  user requests it or traceability/ownership makes it the smallest sufficient
  form.

## Anti-proliferation rule

Capability name and deliverable name are not a one-to-one mapping. A separate
Product Intent Review report may be a task-local selected deliverable, but it
does not require a catalogue profile while the existing three profiles express
its actual reader job without distortion.

## Reconsideration trigger

Reconsider only after repeated reviewed tasks show a stable reader job with a
distinct purpose, fit, failure modes, companions, and non-overlapping selection
boundary that cannot be represented by report, research report, decision memo,
or an embedded block. Step 4 tests do not show that need.
