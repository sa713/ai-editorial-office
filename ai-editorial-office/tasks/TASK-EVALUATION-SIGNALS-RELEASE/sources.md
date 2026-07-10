# Sources

Checked: 2026-07-10

## Repository sources

| ID | Source | Type / proximity | Freshness | Reliability | Used for | Limitations |
| --- | --- | --- | --- | --- | --- | --- |
| R01 | [`AGENTS.md`](../../AGENTS.md) | canonical governance / primary | current | high | Authority, role, review, artifact, and lifecycle boundaries | Does not define S5.R2 implementation |
| R02 | [`ROADMAP.md`](../../ROADMAP.md) | strategy / primary | partially stale | high for strategy | Stage 5 purpose and architecture philosophy | State text predates accepted S5.R1 verdict |
| R03 | [`BACKLOG.md`](../../BACKLOG.md) | operational plan / primary | current | high | S5.R2 goal, result, and active status | Not canonical architecture |
| R04 | [`project-state.md`](../../project-state.md) | current-state owner / primary | partially stale | high for normalized state | Current owners, roles, architecture decisions | S5 state predates S5.R1 acceptance commit |
| R05 | [`kb/editorial_learning_framework.md`](../../kb/editorial_learning_framework.md) | canonical KB / primary | current | high | Evidence chains, patterns, disposition, stale knowledge, non-promotion | Does not yet expose an Evaluation Signal view |
| R06 | [`kb/customer_feedback_loop.md`](../../kb/customer_feedback_loop.md) | canonical KB / primary | current | high | Feedback classification boundary | Applies only to actual customer feedback |
| R07 | [`kb/editorial_evidence_framework.md`](../../kb/editorial_evidence_framework.md) | canonical KB / primary | current | high | Evidence classes, confidence, uncertainty | Confidence is claim-specific, not a trend score |
| R08 | [`kb/architecture_review.md`](../../kb/architecture_review.md) | canonical KB / primary | current | high | Architecture risks, quality scenarios, tradeoffs | No recurring-signal assembly contract |
| R09 | [`kb/domain_knowledge_pack_standard.md`](../../kb/domain_knowledge_pack_standard.md) | canonical KB / primary | current | high | Activation versus actual-use effect | Actual ordinary-task evidence remains limited |
| R10 | [`kb/feedback_patterns.md`](../../kb/feedback_patterns.md) | recurring-pattern owner / primary | current | high | Reusable pattern storage | No validated patterns yet |
| R11 | [`kb/capability_registry.md`](../../kb/capability_registry.md) | canonical capability map / primary | current | high | Existing capabilities and role wrappers | Does not justify a new Evaluation capability |
| R12 | [`templates/release-pack.md`](../../templates/release-pack.md) | active artifact standard / primary | current | high | Project Lead review packet shape | No bounded advisory signal section yet |
| R13 | [`releases/S5-R1/release-pack.md`](../../releases/S5-R1/release-pack.md) | accepted release evidence / primary | current | high | S5.R1 boundaries, actual verdict, next-release authorization | Release-specific, not S5.R2 architecture |
| R14 | [`research/feedback_learning_intelligence_architecture_synthesis.md`](../../research/feedback_learning_intelligence_architecture_synthesis.md) | adjacent synthesis / primary | current | high | Existing-owner integration and postponed S5.R2 scope | S5.R1-specific |
| R15 | Commit `fb3b932` | repository decision evidence / primary | current | high | S5.R1 accepted and S5.R2 opened | State normalization was intentionally not part of acceptance commit |

## External professional sources

| ID | Source | Type / proximity | Publication/update | Freshness | Reliability | Used for | Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E01 | [DORA software delivery performance metrics](https://dora.dev/guides/dora-metrics/) | authoritative research guidance / primary | updated 2026-01-05 | current | high | Multiple measures in tension; context; goal, comparison, gaming, and collection-cost warnings | Software delivery metrics do not map directly to editorial work |
| E02 | [The SPACE of Developer Productivity](https://queue.acm.org/detail.cfm?id=3454124) | peer-reviewed framework / primary | 2021-03-06 | current for principle | high | Multidimensional measurement; activity counts have ambiguous causes | Developer productivity context, not release governance |
| E03 | [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) | international standard / primary | 2023-11 | current | high | Quality is multi-characteristic and context-specific | Full standard text is paywalled; abstract supports only high-level transfer |
| E04 | [SEI ATAM collection](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/) | authoritative architecture practice / primary | collection 2018; underlying research 1998-2003 | current for established principle | high | Architecture evaluation against quality goals, risks, and tradeoffs | Heavy ATAM method is not appropriate for this local system |
| E05 | [Thoughtworks architectural fitness function](https://www.thoughtworks.com/en-us/radar/techniques/architectural-fitness-function) | authoritative professional practice / primary | 2018 | older | medium-high | Some architecture characteristics can use objective continual checks | Radar item is old and not authority for governance automation |
| E06 | [Google SRE: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) | authoritative engineering practice / primary | 2016 book | current for principle | high | Signal/noise, monitoring purposes, simplicity, monitoring cost | Production-service monitoring context |
| E07 | [DORA: Monitoring systems](https://dora.dev/capabilities/monitoring-systems/) | authoritative research guidance / primary | current page | current | high | Avoid monitor-everything and local optimization; data must serve decisions | Organization-scale practice |
| E08 | [Google SRE: Eliminating Toil](https://sre.google/sre-book/eliminating-toil/) | authoritative engineering practice / primary | 2016 book | current for principle | high | Repetitive, manual, tactical, low-enduring-value maintenance burden | SRE toil definition must be adapted cautiously |
| E09 | [Magenta Book](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html) | government evaluation standard / primary | updated 2026-05-15 | current | high | Decision questions, proportionality, alternatives, uncertainty, learning and accountability | Public-policy evaluation context is broader than this release |
| E10 | [IHI PDSA testing changes](https://www.ihi.org/library/model-for-improvement/testing-changes) | authoritative improvement guidance / primary | current page | current | high | Local test, observation, learning, repeated confirmation | Healthcare provenance; transfer is only the learning logic |
| E11 | [ISO/IEC 33020:2019](https://www.iso.org/standard/78526.html) | international standard / primary | confirmed 2026 | current | high | Formal capability assessment requires a defined framework and ratings | Supports rejection of maturity scoring here; full text paywalled |
| E12 | [Google HEART framework](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) | peer-reviewed product research / primary | 2010 | established principle | high | Start with user/product goals, then choose measures | Large-scale web-product context |
| E13 | [NIST AI RMF Core: Measure](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | government consensus framework / primary | AI RMF 1.0, 2023; revision noted | current with revision caveat | high | Quantitative/qualitative mixed methods, context, uncertainty, limits, independent review, measure-to-manage separation | Applies specifically to AI risk; not a release scorecard |

## Source sufficiency

- Professional coverage: sufficient across every mission research area.
- Repository coverage: sufficient to identify existing owners and the missing
  decision-support view.
- Contradictions: no material source contradiction. Sources differ in domain
  and measurement form, but converge on contextual, multidimensional,
  decision-oriented use and on the risk of decontextualized activity metrics.
- Open source gap: no external source can prove which AI Editorial Office
  signals are useful in practice; that requires future saved use evidence.
