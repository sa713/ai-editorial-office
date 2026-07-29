# Product Intent Review — Step 2 implementation report

## Implemented behavior

Step 2 adds a bounded route from Task Need Recognition evidence to a
Chief Editor mode decision and conditional capability-owner loading.

```text
signals + negative evidence
  -> advisory not_needed / limited / full
  -> Chief Editor decision
  -> orchestration state
  -> optional manifest restart pointer
  -> generator conditional read set
```

No full Product Intent Review analysis is performed by this path.

## Canonical contracts

### Task Need Recognition

`kb/task_need_recognition.md` now defines:

- five observable Product Intent Review signal families;
- material negative evidence;
- multi-signal discipline;
- `not_needed`, `limited`, and `full` advisory logic;
- uncertainty inside rationale/confidence rather than a fourth mode;
- one proposed focus for `limited`;
- product-first advisory consequence for `full`;
- explicit non-decision and no-analysis boundaries.

### Task object

`kb/task_object_model.md` adds two optional semantic fields:

- `product_intent_review_recommendation`;
- `product_intent_review_decision`.

They are views over existing artifacts, not mandatory schema objects. Full
routing state belongs in orchestration. Manifest carries only restart-critical
mode/pointer/consequence when `limited` or `full`.

## Role contracts

Intake Agent:

- captures signals and negative evidence;
- may recommend a mode/focus;
- cannot choose final mode, ask a universal seven-question brief, perform the
  analysis, propose alternatives, or act as product owner.

Chief Editor:

- accepts, narrows, rejects, or overrides the recommendation;
- records mode, basis, focus, evidence depth, consequence, and reroute trigger;
- enforces product-first ordering as production permission, not a stage;
- cannot produce the capability finding or take the product-owner decision.

Exact `/about` copies were updated for both mapped role files.

## Templates

The orchestration template has a conditional routing block containing advisory
and decision state without the seven-element analysis. The manifest template
has an optional restart-critical block for `limited`/`full`; obvious
`not_needed` tasks omit it.

No mandatory Product Intent Review artifact or universal brief was added.

## Conditional loading

`generate_task_pack.py` now parses only explicit labels in manifest and
orchestration:

- manifest `Product Intent Review mode` is the restart anchor;
- orchestration `Chief Editor Product Intent Review mode decision` is fallback;
- manifest/orchestration conflict is warned and manifest remains authoritative;
- `limited`/`full` load `kb/product_intent_review.md`;
- `not_needed`, missing, or unsupported mode does not load the owner;
- raw request keywords are never inspected.

This generator change was necessary because the prior generator did not resolve
active capability files from Registry or task state.

## Tests and fixtures

Added executable fixtures for:

- keyword-heavy `not_needed`;
- `limited` with focus `mechanism`;
- `full`;
- Chief Editor override from advisory `not_needed` to decision `full`.

`test_product_intent_review_routing.sh` verifies:

- compact path and keyword trap;
- conditional owner loading;
- limited/full modes;
- Chief Editor override;
- manifest-only restart;
- modes absent from Task Status Model;
- absence of a Product Intent Review pipeline.

`test_task_pack_generator.sh` includes the same behavior in the generator
regression suite. Manual TNR routing fixtures cover all ten authorized
positive, negative, and ambiguous cases.

## Pre-review compact-path repair

The first generator draft emitted a new “not included” explanation for every
task with absent or `not_needed` mode. The pre-review regression pass identified
that as avoidable global output drift. The final implementation is silent for
absent/`not_needed` mode and changes the generated read set only for
`limited`/`full` or an invalid/conflicting explicit state.

## Validation evidence

- Product Intent Review routing shell test: pass.
- Task-pack generator shell test: pass.
- Lifecycle validator smoke suite: pass.
- Current task lifecycle validation: pass, zero blockers and warnings.
- Python source compilation and shell syntax: pass.
- `/about` exact-copy package: pass.
- `git diff --check`: pass.

## Explicit non-implementation

Unchanged:

- full seven-element Product Intent Review analysis;
- four checks;
- minimum hypothesis validation;
- finding/report catalogue;
- Review Agent and Final Editor;
- task statuses and review outcomes;
- pipelines, lifecycle stages, review gates;
- project state and Professional Analysis release status;
- Step 3.
