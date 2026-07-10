# Sources

Date checked: 2026-07-10

## external sources

| ID | Source | Type / proximity | Date / freshness | Reliability | Used for | Limitations |
| --- | --- | --- | --- | --- | --- | --- |
| E01 | [NIST AI Risk Management Framework 1.0](https://doi.org/10.6028/NIST.AI.100-1) | official framework / primary-authoritative | 2023 / current, revision announced | high | socio-technical context, benefits/costs, human oversight, deployment-like evaluation, production monitoring, residual risk, deactivation, override | Voluntary, general AI guidance; NIST states a revision is underway |
| E02 | [NIST AI RMF Playbook: Measure](https://airc.nist.gov/airmf-resources/playbook/measure/) | official living guidance / primary-authoritative | current page / current | high | construct/internal/external validity, operational-context evidence, drift, human review, safe failure, continual evaluation | Suggested actions, not a mandatory sequence or release standard |
| E03 | [NIST AI Risks and Trustworthiness](https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/) | official framework guidance / primary-authoritative | current page / current | high | false-positive/false-negative context, representative tests, human-AI teaming, tradeoffs, intervention/disablement | AI-system scope; adapted here only as evaluation evidence principles |
| E04 | [HM Treasury: Guidance on the Impact Evaluation of AI Interventions](https://www.gov.uk/government/publications/the-magenta-book/guidance-on-the-impact-evaluation-of-ai-interventions-html) | government evaluation guidance / primary-authoritative | updated 2026-05-15 / current | high | intended and unintended outcomes, attribution, baselines, business-as-usual comparison, phased evaluation, claim limits | Government AI interventions; not a technical benchmark guide |
| E05 | [HM Treasury Magenta Book](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html) | government evaluation standard / primary-authoritative | updated 2026-05-15 / current | high | process versus impact evaluation, counterfactuals, costs, sustained effects, proportional evaluation | Policy/intervention evaluation context; methods must be tailored |
| E06 | [Regulatory post-implementation review guidance](https://www.gov.uk/government/publications/the-magenta-book/supplementary-guide-guidance-for-conducting-regulatory-post-implementation-review-html) | government guidance / primary-authoritative | updated 2026 / current | high | baseline monitoring, post-implementation evidence, stakeholder evidence, unintended effects, proportionality | Regulatory context; used for transferable review principles only |
| E07 | [UK DSIT Introduction to AI assurance](https://www.gov.uk/government/publications/introduction-to-ai-assurance/introduction-to-ai-assurance) | government assurance guidance / primary-authoritative | 2024 / current page | high | qualitative and quantitative evidence mix, socio-technical assurance, proportionality, impact evaluation versus pre-deployment assessment | Introductory guidance rather than a detailed method |
| E08 | [NCSC Principles Based Assurance](https://www.ncsc.gov.uk/information/principles-based-assurance) | government assurance method / primary-authoritative | 2023 / current page | high | claim-argument-evidence relationship, evidence fit, impact-based independent assessment, decision usability | Cybersecurity context; the release adopts no formal assurance-case notation |
| E09 | [NASA Systems Engineering Handbook Appendix](https://www.nasa.gov/reference/system-engineering-handbook-appendix/) | agency engineering handbook / primary-authoritative | current page / current | high | verification versus validation, intended use, test pedigree, acceptance evidence | High-assurance engineering context; process weight must be reduced for this repository |
| E10 | [NASA Software Engineering Handbook: Entrance and Exit Criteria](https://swehb.nasa.gov/pages/viewpage.action?pageId=19661899) | agency engineering guidance / primary-authoritative | 2012 / stable | high | acceptance criteria, validation evidence, operational environment, risks, unresolved actions, human panel decision | Maximum criteria intended for tailoring; not all items apply here |
| E11 | [SEI Architecture Tradeoff Analysis Method report](https://www.sei.cmu.edu/library/steps-in-an-architecture-tradeoff-analysis-method-quality-attribute-models-and-analysis/) | FFRDC research report / primary-authoritative | 1998 / stable | high | competing quality attributes, scenario-based architecture fitness, risks and tradeoffs | Software-architecture method; used as a tradeoff principle, not imported as a process |
| E12 | [GAO 2025 Green Book](https://www.gao.gov/greenbook) | government internal-control standard / primary-authoritative | 2025 / current | high | design, implementation, operation, monitoring, and review of controls against objectives | Federal internal-control context; no control framework is imported |
| E13 | [UK Lessons Management Best Practice Guidance](https://www.gov.uk/government/publications/lessons-management-best-practice-guidance/lessons-management-best-practice-guidance-html) | government organizational-learning guidance / primary-authoritative | 2024 / current page | high | lesson versus implemented improvement, monitoring/evaluation, sustained practice, proportionate reporting | Emergency-resilience context; maturity and KPI material is out of scope |
| E14 | [Parasuraman and Riley, Humans and Automation: Use, Misuse, Disuse, Abuse](https://doi.org/10.1518/001872097778543886) | peer-reviewed research / primary | 1997 / stable foundational | high | over-reliance, monitoring failure, decision bias, false alarms, omissions, human-role consequences | Foundational rather than recent; applied only to enduring human-factors risks |

## repository and accepted-release sources

| ID | Source | Evidence class | Used for | Limitations |
| --- | --- | --- | --- | --- |
| R01 | [`AGENTS.md`](../../AGENTS.md) | repository canon | governance, role separation, Project Lead/human approval, artifact minimalism, owner rules | Governs this repository only |
| R02 | [`ROADMAP.md`](../../ROADMAP.md) | repository strategy | evolution sequence, Project Lead release model, Stage 5 purpose, architecture constraints | Contains stale S5.R4 state before this release |
| R03 | [`BACKLOG.md`](../../BACKLOG.md) | Project Lead plan | S5.R4 accepted/Done, S5.R5 mission goal and success criterion | Operational planning, not canon |
| R04 | [`project-state.md`](../../project-state.md) | repository state | accepted S5 behavior and current normalization decisions | Contains stale S5.R4 state before this release |
| R05 | [`S5.R1 Release Pack`](../../releases/S5-R1/release-pack.md) | accepted release evidence | feedback/outcome evidence, owner-scoped learning, non-promotion | Release-specific evidence |
| R06 | [`S5.R2 Release Pack`](../../releases/S5-R2/release-pack.md) | accepted release evidence | Evaluation Signals and explicit non-decision | Release-specific evidence |
| R07 | [`S5.R3 Release Pack`](../../releases/S5-R3/release-pack.md) | accepted release evidence | memory disposition, correction/retirement, no automatic action | Release-specific evidence |
| R08 | [`S5.R4 Release Pack`](../../releases/S5-R4/release-pack.md) | accepted release evidence | Task Need Recognition, synthetic limits, Project Lead acceptance evidence | Release-specific evidence |
| R09 | [`Release Pack standard`](../../templates/release-pack.md) | current release standard | readiness packet, architecture/scope/validation/risk/recommendation owner | Before S5.R5, lacks one combined intelligence-acceptance record |
| R10 | [`editorial_learning_framework.md`](../../kb/editorial_learning_framework.md) | repository canon | Knowledge Evolution, Evaluation Signals, evidence/interpretation/decision separation | Does not own Project Lead release acceptance |
| R11 | [`customer_feedback_loop.md`](../../kb/customer_feedback_loop.md) | repository canon | actual feedback classification and link to learning disposition | Post-delivery feedback only |
| R12 | [`task_need_recognition.md`](../../kb/task_need_recognition.md) | repository canon | advisory request-to-need evidence and non-decision | Pre-routing; does not judge release acceptance |
| R13 | [`editorial_evidence_framework.md`](../../kb/editorial_evidence_framework.md) | repository canon | evidence classes, confidence, assumptions, unknowns, validation limits | Does not decide release disposition |
| R14 | [`architecture_review.md`](../../kb/architecture_review.md) | repository canon | architecture drivers, scenarios, tradeoffs, risks and rationale | Does not own Project Lead acceptance |
| R15 | [`ai_engineering_domain_pack.md`](../../kb/ai_engineering_domain_pack.md) | accepted domain context | evaluation, baseline, regression, human oversight, fallback/rollback and residual risk | Domain Pack context, not global governance |
| R16 | [`review_pipeline.md`](../../pipelines/review_pipeline.md) | repository canon | existing independent review gate and Evaluation Signal challenge | Review mechanics, not release disposition owner |

## source sufficiency

- External coverage is sufficient across all mission research areas through
  primary/authoritative evaluation, assurance, engineering, architecture,
  control, learning, human-factors, and post-implementation sources.
- Repository evidence is sufficient to identify the current owner boundary.
- No external source can decide the repository-specific owner; that conclusion
  remains architecture synthesis.
- Operational evidence for this new S5.R5 contract does not yet exist. The
  release may claim contract completeness and scenario behavior, not proven
  improvement in future release decisions.
