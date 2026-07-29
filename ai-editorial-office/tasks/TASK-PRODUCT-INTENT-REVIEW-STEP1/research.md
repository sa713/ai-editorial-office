# Research — Product Intent Review Step 1

## scope

- Primary authority: `brief.md`.
- Approved architectural premise: Step 0 selects a conditionally activated,
  narrow decision lens inside the Professional Analysis family with one
  canonical owner and no new role, stage, pipeline, gate, status, or mandatory
  task artifact.
- Current-state evidence: repository canon as of 2026-07-29.
- Historical evidence only: the Problem Hypothesis proposal.
- Excluded: routing implementation, task-object changes, role and pipeline
  changes, templates, runtime, behavior tests, release-state changes, and Step 2.

## confirmed observations

- `project-state.md` names Professional Analysis as an open release candidate
  and authorizes no future stage.
- The Step 1 brief explicitly permits Product Intent Review to use that current
  release-candidate contract as its parent family without accepting, expanding,
  or releasing Professional Analysis.
- No current canonical file owns the complete Product Intent Review semantics.
- `kb/professional_analysis.md` is the closest parent and already owns
  decision-ready analytical product shape, including product-discovery and
  business/needs lenses.
- Evidence classification and confidence already belong to
  `kb/editorial_evidence_framework.md`; Product Intent Review must reference,
  not copy, that model.
- Existing role, pipeline, lifecycle, review, planning, audience/outcome,
  architecture-review, deliverable-knowledge, and challenge capabilities cover
  adjacent responsibilities but not the combined intent reconstruction and
  value/fit/mechanism/viability contract.
- `/about` exact-copy rules include `ai-editorial-office/AGENTS.md`, but do not
  include the capability registry, Professional Analysis, or the new Product
  Intent Review file.

## canonical change boundary

Required:

- create `kb/product_intent_review.md` as the sole full owner;
- add one bounded record and role mapping to `kb/capability_registry.md`.

Necessary minimal relationships:

- add one ownership-map row to `AGENTS.md`;
- add one short parent/child relationship note to
  `kb/professional_analysis.md`;
- sync `about/AGENTS.md` exactly because the existing package check requires
  it.

Explicitly unchanged:

- `project-state.md`;
- task object and task statuses;
- routing and preflight behavior;
- agent specifications;
- lifecycle and pipelines;
- review outcome vocabulary;
- templates and task-pack generator;
- runtime, scripts, smoke-test behavior, and production behavior.

## historical Problem Hypothesis disposition

Decision: leave the historical Problem Hypothesis as a separate, unaccepted
proposal and do not integrate or supersede it in Step 1.

Basis:

- it was never accepted as a canonical capability owner;
- its proposed orchestration placement and behavior exceed Step 1's
  specification-only authority;
- Product Intent Review's `problem` element may ask a related question, but it
  does not adopt the historical proposal's workflow contract;
- editing current incidental references would be an operational/normalization
  change outside Step 1.

Consequence: the historical task remains provenance, not authority. Later work
may explicitly retire or normalize those references, but Product Intent Review
does not silently canonize them.

## confidence and limitations

- Confidence in repository-state and ownership claims: high, based on current
  canonical files.
- Confidence in future real-world activation quality: not assessed; activation
  behavior is intentionally unimplemented.
- The specification can define semantic checks and insufficiency behavior but
  cannot prove live routing or output behavior in Step 1.
