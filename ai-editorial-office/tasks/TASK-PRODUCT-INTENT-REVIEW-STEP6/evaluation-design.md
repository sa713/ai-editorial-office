# Evaluation Design

## architecture

The suite is a hybrid evaluation asset inside the existing test architecture:

```text
case fixture
├── deterministic layer: schema, IDs, coverage, expected/observed contract
└── manual layer: rubric scores, defect judgment, confidence, rationale
```

The runner does not generate a product answer, infer product quality from
keywords, or replace Review Agent judgment.

## case record

Every case contains:

- `case_id`, title, task class, source kind, and sanitized input;
- evaluator-only hidden structure: real problem, confirmed evidence,
  assumptions, unknowns, main gap, allowed alternatives, forbidden conclusions;
- expected mode and focus;
- required properties, forbidden errors, accepted variability, acceptable
  finding range, and case-specific rubric focus;
- paired/adversarial/control and coverage tags;
- observed structured result: mode, focus, evidence boundary, main gap,
  finding, production consequence, validation disposition/method, next decision,
  reader order, properties, errors, and governance flags;
- manual evaluation: rubric profile, main defect, confidence, rationale, and
  judgment status.

## deterministic layer

The runner:

- rejects missing metadata and duplicate Case IDs;
- validates enum values and paired-case shape;
- checks required properties and forbidden errors against the observed record;
- checks expected versus observed mode and focus;
- checks consequence/finding compatibility and governance invariants;
- calculates class, pair, adversarial, mode, finding, validation, and manual
  judgment coverage;
- calculates routing accuracy, over/missed activation, mode mismatch, critical
  violations, main-gap failures, unsupported findings, validation-method
  mismatch, authority violations, and compact regressions;
- emits a machine-readable evaluation manifest.

## manual layer

Review Agent evaluates the saved result without editing it. The manual record
uses the shared rubric dimensions, names a main defect when present, separates
style preference from contract violation, records confidence, and gives a short
case-specific rationale.

Scores support comparison but do not produce a universal product-quality
number. Critical failure conditions override any aggregate.

## anti-overfit controls

- Expected results define property ranges, not gold prose.
- Paired cases differ by one material fact.
- Strong product/weak text and weak product/strong text are both present.
- Negative editing cases protect ordinary work.
- Adversarial cases include authoritative claims, false precision, solution-as-
  problem, formal model completion, universal pilot, optimistic polishing,
  insufficient evidence, and wrong intervention class.
- Coverage cases include real-theme sanitized logic and synthetic boundaries.
- A failing case cannot be repaired by weakening expected behavior.

## production repair gate

Only a deterministic failure or independent manual `fail` that contradicts the
accepted Step 1–5 contract may enter `defect-log.md`. Evaluation-data or runner
defects are repaired in the suite and do not justify production changes.
