# Facts

| ID | Verified finding | Evidence | Confidence | Boundary |
| --- | --- | --- | --- | --- |
| F01 | AI Editorial Office already separates post-delivery feedback classification from reusable learning disposition. | R01, R05, R06 | high | The bridge between the two is under-specified, not absent. |
| F02 | Existing feedback classifications are `task_local`, `preference`, `observation`, `confirmed_pattern`, and `system_change_candidate`. | R01, R06, R10 | high | These are feedback-routing labels, not task statuses. |
| F03 | Existing learning dispositions already include task-local, candidates, accepted canon, correction/retirement-related states, rejection, and deferral. | R05 | high | These are knowledge dispositions, not operational statuses. |
| F04 | Existing canon already requires a reconstructable source-evidence chain before reusable promotion. | R05 | high | S5.R1 should operationalize the intake bridge, not replace the rule. |
| F05 | Existing Domain Pack guidance records activation, reason, relevant sections/sources, confidence, limits, stale-if triggers, and stop conditions. | R08 | high | It does not explicitly record observed benefit, burden, or uncertainty after use. |
| F06 | The Stage 4 strategic review found no ordinary-task evidence sufficient to confirm Domain Pack practical value. | R09 and repository scan | high | Release scenarios prove bounded design, not real-world usefulness. |
| F07 | GAO's current lessons-learned synthesis treats collection, analysis, validation, archiving, and sharing as distinct practices; validation includes correctness and applicability scope. | E04 | high | Adapted from program management, not copied as a new lifecycle. |
| F08 | NASA's public lessons system contains reviewed lessons that connect the original event to recommendations and feed existing improvement channels. | E05 | high | Does not justify automatic policy updates. |
| F09 | NIST AI RMF calls for ongoing governance, clear roles, adjudicated external feedback, documented human oversight, and deployment-context evaluation. | E01, E02 | high | AI risk guidance is applied proportionally to editorial work. |
| F10 | NIST's 2026 monitoring work says human-AI feedback-loop methods and beneficial-impact metrics remain incomplete and monitoring can impose user burden. | E03 | high | Supports caution against mandatory telemetry or invented scores. |
| F11 | GOV.UK separates raw observations from interpretation, groups matching evidence, permits isolated irrelevant notes to be discarded, and derives actions only after findings. | E10 | high | Qualitative patterns can be valid without numerical scoring. |
| F12 | GOV.UK recommends finding significant patterns across feedback sources, testing proposed changes, and checking whether the expected effect occurred. | E09 | high | Statistical significance may be replaced by qualitative sufficiency in a single-user local system, with uncertainty explicit. |
| F13 | IHI recommends small change tests with an objective, prediction, data collection, comparison to results, and refinement before wider implementation. | E06 | high | S5.R1 uses this as bounded proposal/test logic, not a new PDSA pipeline. |
| F14 | Google SRE and AWS COE practices require factual impact evidence, root-cause analysis, concrete action, ownership, review, and tracking; unsupported blame or vague actions are weak learning. | E07, E08 | high | Ordinary wording feedback should not inherit incident-level ceremony. |
| F15 | Microsoft human-AI guidance supports correction, uncertainty scoping, cautious adaptation, granular feedback, and user control; its guideline set was empirically evaluated. | E12 | high | It supports human authority, not silent model or canon adaptation. |
| F16 | Google PAIR distinguishes implicit from explicit feedback and warns that what users want to express may not align with what a system can validly learn. | E13 | medium-high | Direct model tuning described by PAIR is out of scope and rejected here. |
| F17 | GitLab's public process demonstrates that feedback can receive timely review without forcing a prioritization outcome and that the responsible product owner retains decision authority. | E14 | medium-high | Product labels and automation are not imported. |
| F18 | Retrospective practice favors a small number of owned, actionable changes with follow-through, but does not prove that every completed task needs a retrospective. | E15 | medium-high | S5.R1 should use material-signal triggers, not mandatory task rituals. |

## Research judgment

The evidence is sufficient for a bounded documentation integration through the
two existing owners. It is not sufficient for automation, a scoring model, a
mandatory retrospective cadence, direct model tuning, or any claim that Domain
Packs have already improved ordinary work.
