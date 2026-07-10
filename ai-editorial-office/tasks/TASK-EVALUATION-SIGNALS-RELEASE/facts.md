# Facts

| ID | Finding | Evidence | Confidence | S5.R2 implication |
| --- | --- | --- | --- | --- |
| F01 | The repository already separates saved observations, evidence confidence, learning disposition, review findings, architecture risks, Domain Pack activation/effect, and human release decisions. | R01, R05-R14 | verified | Implement a view across existing evidence, not a parallel store. |
| F02 | S5.R1 is accepted and S5.R2 is explicitly open even though ROADMAP and project-state retain the pre-acceptance state. | R02-R04, R13, R15, user mission | verified | Normalize state surfaces during S5.R2. |
| F03 | DORA applies multiple measures together, requires application/service context, and warns against targets, one-metric simplification, disparate comparisons, competition, and excessive collection effort. | E01 | verified | No target, score, rank, or cross-context comparison. |
| F04 | SPACE shows activity counts can have opposite explanations and should not be used alone to reward or penalize people. | E02 | verified | Activation frequency is a question signal, never value or performance proof. |
| F05 | Software quality is multi-characteristic rather than one scalar property. | E03 | supported | Release quality observations must name the affected quality. |
| F06 | Architecture evaluation is driver-, quality-goal-, risk-, and tradeoff-based. | E04, R08 | supported | Architecture drift stays qualitative and scenario-backed. |
| F07 | Some architectural characteristics can be checked objectively, but the professional source does not justify general automated governance. | E05 | supported | Reuse existing deterministic validators only; do not automate design judgment. |
| F08 | Monitoring has distinct purposes, meaningful monitoring is costly, and human-facing signals should be simple and low-noise. | E06, E07 | supported | Material signals only; no dashboard or collect-everything requirement. |
| F09 | Maintenance burden is meaningful when work is repeated, manual/tactical, scalable, and low in enduring value; difficult work is not automatically toil. | E08 | supported | Preserve burden and enduring-value context. |
| F10 | Evaluation should start from decision questions, remain proportionate, test alternative explanations, disclose limitations, and match evidence robustness to decision size. | E09 | verified | Signal record needs question, evidence, alternatives, limits, and decision owner. |
| F11 | Continuous improvement builds knowledge through planned local tests and repeated observation, not one synthetic success. | E10 | supported | Future use can confirm or contradict; scenarios only validate mechanics. |
| F12 | Formal capability maturity assessment requires a defined measurement framework and ratings/levels. | E11 | verified | Reject maturity levels and ratings as unsupported scope. |
| F13 | Product measures should follow product/user goals, not data availability. | E12 | supported | Domain Pack usefulness begins with intended/observed effect, not activation count. |
| F14 | NIST AI RMF supports quantitative, qualitative, and mixed methods with context, uncertainty, limitations, regular reassessment, documentation, and independent review. | E13 | verified | AI-related signals remain context-bound and reviewable. |
| F15 | NIST separates measurement input from management action. | E13 | supported | Evaluation Signals inform but never take governance action. |
| F16 | Current Domain Pack canon already treats activation and actual-use effect as separate and makes effect capture optional. | R09 | verified | No Domain Pack Standard change is necessary. |
| F17 | Current Learning canon already provides evidence, scope, contradictions, owner, disposition, rejection/deferral, and non-promotion. | R05 | verified | Extend it with an optional advisory view rather than new taxonomy. |
| F18 | Current feedback-pattern records already carry most fields needed for recurring Evaluation Signals. | R10 | verified | Add only comparison window/denominator and Project Lead question. |
| F19 | Current Release Pack standard gives Project Lead decision evidence but lacks a bounded signal section. | R12-R13 | verified | Add an optional Evaluation Signals section to the template. |
| F20 | Synthetic scenarios can prove routing and non-decision behavior but cannot establish real system improvement or pack/capability value. | E09-E10, repository evidence | supported | Test mechanics; state real value remains unknown pending use. |
