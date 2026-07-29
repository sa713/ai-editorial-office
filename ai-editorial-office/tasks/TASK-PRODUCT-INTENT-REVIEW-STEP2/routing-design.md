# Product Intent Review — Step 2 routing design

## Decision

Реализовать двухступенчатый contract поверх существующего Task Need
Recognition:

```text
observed signals + negative evidence
  -> advisory recommendation
  -> Chief Editor mode decision
  -> task-local orchestration state
  -> conditional owner loading
  -> existing planning and production permission
```

Отдельный classifier, score, threshold, boolean `is_product`, pipeline, stage,
gate или status не создаётся.

## Advisory contract

Task Need Recognition сохраняет:

- observed product-intent signal families;
- material negative evidence;
- recommendation: `not_needed`, `limited`, `full`;
- краткий rationale;
- confidence;
- proposed focus для `limited`;
- explicit non-decision.

Recommendation выводится из совокупности outcome, work surface, decision state,
scope, consequence, ambiguity, evidence и negative evidence. Keyword не
является достаточным сигналом.

## Chief Editor contract

Chief Editor отдельно фиксирует:

- accepted/overridden mode;
- краткое decision basis;
- `focus` для limited;
- required evidence depth;
- production consequence;
- reroute trigger.

Границы решений:

- activation decision — Chief Editor;
- capability finding — будущий analytical owner, не Step 2;
- production permission — Chief Editor после достаточного finding;
- product decision — product owner.

## Mode consequences

| Mode | Route consequence |
| --- | --- |
| `not_needed` | Ordinary compact route; owner not loaded. |
| `limited` | Resolve one named product-intent question before deep production; owner loaded. |
| `full` | Do not authorize a detailed production contract until a bounded Product Intent Review finding exists; owner loaded. |

Incomplete data does not create automatic `blocked`: select the available mode,
preserve unknowns, name one material focus, and assign bounded research if
needed.

## Task object representation

Two optional semantic fields:

- `product_intent_review_recommendation` — TNR advisory value, basis,
  confidence, negative evidence, and proposed focus;
- `product_intent_review_decision` — Chief Editor mode, basis, focus, evidence
  depth, production consequence, reroute trigger, and canonical owner pointer.

Primary full view: `orchestration_plan.md`.

Manifest stores only restart-critical state for `limited`/`full`:

- `Product Intent Review mode`;
- state pointer;
- canonical owner;
- compact production consequence.

For obvious `not_needed`, the manifest section is omitted. Ambiguous negative
evidence may remain as one line in orchestration.

## Conditional loading design

`generate_task_pack.py` reads only explicit labels:

- `Product Intent Review mode` in manifest, preferred;
- `Chief Editor Product Intent Review mode decision` in orchestration,
  fallback.

For `limited` or `full`, add `kb/product_intent_review.md` to the Conditional
read set. For `not_needed`, absent, or invalid mode, do not load it. Request
content and keywords are never inspected for activation.

## Regression design

Executable fixtures cover:

- keyword-heavy `not_needed`;
- `limited` with `focus: mechanism`;
- `full` with product-first consequence;
- Chief Editor override from advisory `not_needed` to decision `full`;
- restart from manifest state;
- unchanged ordinary compact fixture.

Manual routing cases cover the ten user-provided positive, negative, and
ambiguous requests. The manual cases test the instruction-driven recommendation
contract; shell tests test executable state-to-read-set behavior.

## Non-goals

- No seven-element runtime output.
- No four-check review logic.
- No minimum hypothesis validation.
- No report schema or product finding catalogue.
- No independent Product Intent Review review dimension.
- No changes to Review Agent, Final Editor, lifecycle, statuses, pipelines,
  project state, or Professional Analysis release status.
