# Implementation Report

## implemented decision flow

Step 5 strengthens the existing minimum hypothesis validation:

```text
one main product gap
-> validation disposition
-> one critical hypothesis
-> hypothesis class and fitted method
-> minimum reversible intervention
-> observable signal
-> continue / reconsider conditions
-> inference limits
-> next product-owner decision
```

The three analytical dispositions are `minimum_test`, `not_needed`, and
`insufficient`. They are not lifecycle stages, task statuses, review outcomes,
or product decisions.

## canonical behavior

`kb/product_intent_review.md` now:

- defines the critical hypothesis as the premise controlling the next costly or
  hard-to-reverse step;
- requires direct linkage to the one main product gap;
- distinguishes problem, demand, mechanism, behavior, usability, feasibility,
  and viability hypotheses;
- maps each class to bounded suitable methods and named mismatches;
- selects method using risk, next-step cost, reversibility, evidence, context,
  and ethical/organizational constraints;
- requires smaller-than-production, stoppable, reversible scope with unrelated
  features removed;
- prefers real action, choice, task completion, decision quality, use,
  transfer, error, refusal, obstacle, or process change;
- rejects weak attitudinal evidence as proof of demand, mechanism, behavior,
  persistence, transfer, or work effect;
- accepts observable qualitative conditions and requires a recorded basis for
  any number;
- makes inference limits and the next owner decision explicit;
- recommends only the nearest check and recognizes `not_needed` and
  `insufficient`;
- adds AI-specific data, variability, control, privacy, and work-effect
  boundaries.

No relationship note was added to Editorial Evidence Framework or Analytical
Reasoning because their current ownership already supplies the reused
evidence/confidence and reasoning primitives. Professional Analysis was
inspected and not changed.

## role and deliverable integration

- Chief Editor decides whether validation is material and accepts
  `not_needed`/`insufficient` rather than forcing a test.
- Research Agent may design the nearest fitted check when explicitly assigned
  as analytical owner, but does not own the product decision.
- Writer Agent and UX Writer may create only the approved minimum artifact and
  cannot expand it into a production-ready product.
- Review Agent checks gap linkage, criticality, derived method fit, minimality,
  signals, decision conditions, threshold basis, inference limits, and
  overreach inside the existing gate.
- Final Editor preserves the approved hypothesis/conditions/limits and cannot
  convert them into facts.
- Report, research-report, and decision-memo profiles render the same semantic
  record compactly; no validation report/profile is created.
- Changed mapped role files remain exact copies in `/about`.

## executable behavior

The existing decision/review checker now derives method fit from a bounded
hypothesis-method map. A fixture cannot approve itself by asserting that a
method fits.

The executable set covers:

- the ten Step 3 decision/review regressions;
- the fifteen authorized Step 5 scenarios;
- three additional bounded class-coverage cases for event demand, feasibility,
  and internal-product viability;
- the twelve Step 4 reader-output regressions, including compact validation
  rendering fields.

Expected negative cases identify the reason for failure: weak signal,
method mismatch, automatic survey, threshold without basis, full-product scope,
or sequential-program overreach.

## validation completed before review

- Product Intent Review routing, restart, compact path: pass.
- Step 3 decision/review and Step 5 validation scenarios: pass.
- Step 4 output and output integration: pass.
- Outcome-first deliverable selection and multi-deliverable profiles: pass.
- Task-pack generator: pass.
- Lifecycle validator smoke and Task State Projection: pass.
- Python compile and shell syntax for changed executables: pass.
- `/about` exact-copy parity: pass.
- `git diff --check`: pass.

## residual boundary

The method map is bounded implementation guidance. It does not authorize real
research, supply universal sample sizes, guarantee the diagnostic value of a
method in every domain, or replace specialist and product-owner judgment.
