# Claims Table

| ID | Claim | Status | Evidence | Confidence | Factual sensitivity | Allowed downstream use | Review use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C01 | Stage 5 intelligence acceptance should be a conditional contract inside the existing Release Pack standard. | confirmed synthesis | F21-F29 | supported | high | with caveat | Validate owner fit and no duplicate workflow. |
| C02 | No new canonical KB owner is required because the Release Pack already owns the Project Lead decision packet and readiness rule. | confirmed synthesis | F21-F22, F26-F29 | supported | high | with caveat | Challenge whether the template can express the complete contract. |
| C03 | Every intelligence release must support both a value case and a restraint case; failure of either prevents an accept recommendation. | confirmed synthesis | F01-F04, F11, F16, F20-F22 | supported | critical | yes | Test all dispositions without aggregation. |
| C04 | The improvement claim must be linked to supporting and contradicting evidence, evidence origin, gaps, uncertainty, and explicit non-claims. | confirmed | F02, F08, F10-F12, F26, F29 | verified | high | yes | Check claim/evidence separation. |
| C05 | Synthetic evidence may prove contract behavior or readiness for bounded trial, but cannot prove operational improvement. | confirmed | F02, F08, F10, F14, F18, F29 | verified | critical | yes | Test strong-synthetic/no-real-use case. |
| C06 | A comparison or baseline is required when it materially improves interpretation; an invented or non-comparable baseline is worse than an explicit evidence gap. | confirmed synthesis | F03, F09, F16 | supported | high | with caveat | Check practical rather than universal comparison. |
| C07 | False positives, false negatives, cross-effects, and unintended consequences must remain visible rather than being collapsed into one score. | confirmed | F05, F11, F16, F20 | verified | critical | yes | Test contradictory and degradation scenarios. |
| C08 | Human review is meaningful only when the human has evidence, competence, time, authority, override/correction/stop paths, and remains accountable. | confirmed synthesis | F06, F20, F21, F28 | supported | critical | yes | Test automation proposal removing review. |
| C09 | Automation needs evidence proportionate to authority, consequence, reversibility, observability, and failure containment. | confirmed synthesis | F04-F07, F15, F17, F20 | supported | critical | with caveat | Test automation acceptance boundary. |
| C10 | Architecture and maintenance burden must be compared with practical value and existing-owner fit. | confirmed synthesis | F03, F13, F16, F19, F22, F27 | supported | high | yes | Test high-cost and duplicate-owner cases. |
| C11 | Hidden governance is present when a mechanism gains de facto decision, mandatory capture, state-change, canon-change, activation, or owner authority outside named canon even if labels remain advisory. | confirmed repository synthesis | F21-F28 | supported | critical | with caveat | Inspect verbs, mandatory fields, and automated consequences. |
| C12 | The contract should support accept, accept with observations, changes requested, defer, narrow scope, reject, and retire/supersede as human recommendations. | confirmed synthesis | F07, F10, F15, F18-F24 | supported | critical | yes | Ensure each disposition has a bounded use. |
| C13 | Accept with observations is appropriate only when value and restraint are supported and remaining issues are non-blocking, owned, and explicit. | confirmed synthesis | F04, F10, F15, F21-F22 | supported | critical | yes | Distinguish from full acceptance and defer. |
| C14 | Existing stale or harmful intelligence needs the same value/restraint evidence and can be retired or superseded without automatic deletion or canon change. | confirmed synthesis | F07, F18-F19, F24 | supported | high | yes | Test stale/harmful mechanism. |
| C15 | Comparative evidence may be qualitative or quantitative; thresholds, scores, dashboards, and mandatory metrics remain unsupported. | confirmed | F04, F09, F13, F16, F22-F23 | verified | high | yes | Check no scoring or bureaucracy. |
| C16 | Ordinary releases should not complete the Stage 5 contract unless explicitly scoped as self-improvement/intelligence work. | confirmed synthesis | F13, F21-F25 | supported | high | yes | Check conditionality and process weight. |
| C17 | The smallest implementation is one conditional Release Pack section, one expanded disposition field, one twelve-case smoke test, and release/state/memory evidence. | architecture proposal | C01-C16 | supported | high | with caveat | Validate no required role/pipeline/gate/owner changes. |

## claim limits

- C01, C02, C03, C06, C08-C14, C16, and C17 are repository-specific
  architecture synthesis. External sources inform the reasoning but cannot
  prove the repository owner choice.
- `with caveat` downstream use is limited to the stated repository scope,
  confidence, non-claims, and Project Lead boundary; it cannot support a broad
  operational-improvement or cross-repository claim.
- No claim states that S5.R5 has already improved real Project Lead decisions.
- Scenario results may confirm documented behavior only.
