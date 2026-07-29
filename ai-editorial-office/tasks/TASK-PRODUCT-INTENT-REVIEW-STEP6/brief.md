# Brief — Product Intent Review Step 6

## authorization

- Status: `Authorized`
- Step: `Evaluation Suite and Product Judgment Calibration`
- Date received: 2026-07-29
- Source: `/Users/sa/.codex/attachments/7c1abb28-0b0d-42e5-bc69-4e0f84c89af1/pasted-text.txt`
- Dependency: Product Intent Review Steps 0–5 are finalized.

## goal

Create an end-to-end evaluation suite that tests Product Intent Review from
input and routing through analysis, product judgment, minimum validation,
governance, and reader-facing output. Evaluate decision quality rather than
section or keyword presence.

## required evaluation levels

- routing;
- analysis;
- decision;
- validation;
- communication;
- governance.

The suite must contain at least 30 cases, eight task classes, eight paired
comparisons, ten adversarial cases, five `not_needed`, five `limited`, ten
`full`, five sound no-build/reroute findings, five proceed findings, five
validation methods, two validation-not-needed cases, and two
validation-insufficient cases.

## evaluation method

Use a hybrid model:

- deterministic checks for metadata, unique IDs, coverage, routing agreement,
  forbidden behavior, and regression invariants;
- rubric-based independent judgment for problem fidelity, model and main-gap
  quality, product judgment, consequence, validation, communication, authority,
  and decision usefulness.

Expected behavior must describe required properties, acceptable variability,
forbidden errors, and acceptable decision ranges rather than one gold text.

## production-change gate

Evaluate the current Step 1–5 implementation first. Production contracts,
roles, pipelines, templates, or runtime may change only when a reproducible
case proves a contract violation that cannot be corrected in evaluation assets.
Every such change requires a defect-log entry, minimal repair, failing-case
rerun, neighboring-case rerun, and full regressions. Do not alter expected
behavior to hide a defect.

## forbidden changes

Do not add a role, pipeline, lifecycle stage, review gate, task status, review
outcome, deliverable, or mode. Do not expand Product Intent Review scope,
change role ownership, accept Professional Analysis, change operational
outcomes, or start Step 7.

## required artifacts

- `baseline-report.md`
- `evaluation-design.md`
- `evaluation-rubric.md`
- `case-catalogue.md`
- `coverage-report.md`
- `baseline-comparison.md`
- `evaluation-report.md`
- `defect-log.md`
- `repair-loop-report.md`
- `implementation-report.md`
- `canonical-diff.md`
- `review.md`
- `final_decision.md`
- `final.md`

## acceptance

All 34 authorized acceptance criteria must pass, critical failure conditions
must be absent, regressions must pass, and an independent review must confirm
readiness without beginning Step 7.
