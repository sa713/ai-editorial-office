# Product Intent Review Routing Smoke Test

Status: synthetic routing and state regression contract.

This file tests Step 2 recommendation and Chief Editor decision semantics. It is
not a classifier, real task evidence, Product Intent Review analysis, new
pipeline, lifecycle stage, gate, status, review dimension, or proof of
real-world improvement. Executable state-to-read-set behavior is checked by
`test_product_intent_review_routing.sh`.

## Contract Under Test

Each case must preserve:

- several signal families rather than keyword activation;
- material negative evidence;
- an advisory `not_needed`, `limited`, or `full` recommendation;
- a separate Chief Editor mode decision;
- one focus for `limited`;
- product-first consequence for `full`;
- no universal seven-question brief;
- no full Product Intent Review analysis at intake;
- conditional owner loading only for the final `limited` or `full` mode.

## Cases

| Case | Synthetic request | Material signals | Negative evidence | Advisory recommendation | Chief Editor decision | Focus / consequence | Owner loaded |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PIR-R01 | Correct errors in a notice about a new service. | service mentioned only as context | explicit proofreading-only scope; behavior out of scope | `not_needed` | `not_needed` | ordinary compact route | no |
| PIR-R02 | Translate a training-program description into English. | educational object mentioned | translation-only scope; no concept decision | `not_needed` | `not_needed` | ordinary compact route | no |
| PIR-R03 | Course concept is approved; shorten the introduction. | course and intended learning exist | concept approved; local shortening | `not_needed` | `not_needed` | ordinary compact route | no |
| PIR-R04 | We want a systems-thinking course; assess whether it should launch. | new intervention, intended capability change, unapproved concept, launch decision | none material | `full` | `full` | no detailed production contract before bounded finding | yes |
| PIR-R05 | Event format is approved, but why participants would apply the practice is unclear. | required behavior change and causal hypothesis | format approved; one bounded unknown | `limited` | `limited` | focus `mechanism` before deep production | yes |
| PIR-R06 | Fix the typo in the word “product”. | keyword only | explicit typo-only scope | `not_needed` | `not_needed` | ordinary compact route | no |
| PIR-R07 | Prepare banner copy for an approved mechanic. | product surface | mechanic approved; product logic not in scope | `not_needed` | `not_needed` | ordinary compact route | no |
| PIR-R08 | Do we need a new internal portal or a different intervention? | new solution class, no-build/change-class decision, alternatives | none material | `full` | `full` | product-first finding before detailed production | yes |
| PIR-R09 | Review this new activity description and give an opinion. | new intervention and possible evaluation request | scope/evidence ambiguous | `limited` or `full`, selected from supplied material | matching evidence-bounded mode | no forced brief; rationale/confidence must explain mode | only if final mode is `limited`/`full` |
| PIR-R10 | Edit a large approved document without changing its concept. | large artifact | concept approved; local editorial scope | `not_needed` | `not_needed` | size does not activate the lens | no |

## Incomplete-Data Check

For an approved concept with an unresolved behavior-change mechanism:

- recommendation may be `limited`;
- focus is `mechanism`;
- unknowns remain unknown;
- bounded research may be assigned;
- absence of all seven elements does not block automatically.

## Override Check

If initial evidence supports `not_needed` but later material exposes an
unapproved intervention class, Chief Editor may record `full`. Conditional
loading follows the final Chief Editor decision, not the initial recommendation
or request keywords.

## Pass Criteria

- Negative cases stay compact and do not load the owner.
- Positive and bounded ambiguous cases load the owner only after Chief Editor
  selects `limited` or `full`.
- Recommendation, decision, finding, production permission, and product-owner
  decision remain distinct.
- No case creates or uses a fourth mode, new status, pipeline, stage, gate,
  review outcome, or mandatory Product Intent Review artifact.
