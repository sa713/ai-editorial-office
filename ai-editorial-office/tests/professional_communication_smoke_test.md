# Professional Communication Smoke Test

Status: manual smoke-test / synthetic examples only.

Purpose: check whether Professional Communication activates only when reader
transfer quality is material and remains inactive for ordinary grammar,
style, audience discovery, UX copy ownership, quality-attribute selection,
analytical reasoning, and Professional Analysis ownership.

This file is not a canonical rule owner. Canonical guidance lives in
`/kb/professional_communication.md`.

## Expected Classification Labels

- `activate`: Professional Communication should be selected.
- `do_not_activate`: Professional Communication should not be selected.
- `activate_with_other_capability`: Professional Communication should be
  selected and another capability should also be considered.

## Cases

| Case | Scenario | Expected | Lenses |
| --- | --- | --- | --- |
| PC-01 | A Project Lead asks for a one-page executive brief that makes a release recommendation, evidence basis, caveats, and next action easy to scan. | `activate_with_other_capability` | executive brief; recommendation or ask; layered communication; Professional Analysis if the recommendation itself must be built |
| PC-02 | A technical handoff must explain what changed, what remains risky, what validation ran, and what another engineer should do next. | `activate_with_other_capability` | technical explanation; implementation handoff; Engineering Review if change safety is material |
| PC-03 | A policy memo needs a bottom line, stakeholder implications, options, caveats, and an approval request without hiding uncertainty. | `activate_with_other_capability` | policy/stakeholder memo; recommendation or ask; Professional Analysis if options and implications must be synthesized |
| PC-04 | Dense research findings need to become a decision-facing summary that preserves evidence confidence and source limitations. | `activate` | research/evidence communication; layered communication |
| PC-05 | A user asks only to fix grammar and punctuation in an already approved paragraph. | `do_not_activate` | none |
| PC-06 | A task asks who the artifact is for and what outcome it should enable before writing begins. | `do_not_activate` | none; Audience & Outcome Alignment owns audience/outcome discovery |
| PC-07 | A UX screen needs button labels, empty-state copy, and error text based on product state. | `do_not_activate` | none; UX Writer owns product copy unless broader communication transfer is material |
| PC-08 | A review candidate has a polished tone but buries the main recommendation, hides a caveat, and leaves no next action. | `activate` | message architecture; recommendation or ask; density/actionability challenge |
| PC-09 | A system architecture decision needs drivers, quality attributes, rejected alternatives, and accepted risks. | `do_not_activate` | none; Architecture Review owns design-fitness challenge |
| PC-10 | A business analysis task needs synthesis, options, and a recommendation before any audience-specific brief is written. | `activate_with_other_capability` | Professional Analysis owns analytical product; Professional Communication applies if the output must transfer that judgment to a specific reader path |

## Pass Criteria

- Positive cases select only relevant communication lenses.
- Negative cases do not activate Professional Communication for grammar,
  generic style, audience discovery, UX copy ownership, Architecture Review,
  Engineering Review, Quality Attributes, Analytical Reasoning, or Professional
  Analysis ownership.
- Recommendation presentation stays within evidence and analytical support.
- Caveats, confidence cues, uncertainty, and technical meaning are not removed
  to make communication smoother.
- No case creates a new role, pipeline, lifecycle stage, review gate, style
  framework, UX-copy owner, or mandatory artifact.
