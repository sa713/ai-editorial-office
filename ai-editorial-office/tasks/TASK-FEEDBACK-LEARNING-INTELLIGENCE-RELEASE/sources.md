# Sources

Checked: 2026-07-10

## Repository sources

| ID | Source | Type / proximity | What it supports | Limitations |
| --- | --- | --- | --- | --- |
| R01 | [`AGENTS.md`](../../AGENTS.md) | canonical / primary | Authority, role, artifact, feedback, review, and owner boundaries | Governance owner, not detailed learning procedure |
| R02 | [`ROADMAP.md`](../../ROADMAP.md) | strategic / primary | Stable architecture and Stage 5 intent | Not canon or implementation procedure |
| R03 | [`BACKLOG.md`](../../BACKLOG.md) | operational plan / primary | S5.R1 goal, success criteria, and allowed release states | Not architecture or canon |
| R04 | [`project-state.md`](../../project-state.md) | current state / primary | Current release/stage state and normalization decisions | Must not become permanent policy owner |
| R05 | [`kb/editorial_learning_framework.md`](../../kb/editorial_learning_framework.md) | canonical / primary | Knowledge disposition, source-evidence chain, promotion, rejection, deferral, correction, retirement | Does not yet give a compact feedback/outcome intake bridge |
| R06 | [`kb/customer_feedback_loop.md`](../../kb/customer_feedback_loop.md) | active workflow / primary | Post-delivery feedback classification and task-local routing | Limited evidence/scope and learning-disposition handoff |
| R07 | [`kb/feedback_patterns.md`](../../kb/feedback_patterns.md) | pattern journal / primary | Recurring feedback pattern storage and maturity labels | Current entry lacks explicit evidence/applicability/owner disposition fields |
| R08 | [`kb/domain_knowledge_pack_standard.md`](../../kb/domain_knowledge_pack_standard.md) | canonical / primary | Pack activation, source, boundary, review, update, retirement | Captures why/how a pack was used, not whether use improved or burdened the result |
| R09 | [`research/stage4_strategic_review.md`](../../research/stage4_strategic_review.md) | accepted-stage review / primary | Need for real pack-use evidence before optimizing Stage 4 | Explicitly says practical value is not yet proven by ordinary tasks |
| R10 | [`templates/artifacts/feedback_template.md`](../../templates/artifacts/feedback_template.md) | scaffold / primary | Current task-local feedback fields | Lacks compact outcome/evidence/owner learning disposition block |

## External sources

| ID | Source | Type / proximity | Published / updated | Freshness and reliability | What it supports | Limitations |
| --- | --- | --- | --- | --- | --- | --- |
| E01 | [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | government framework / primary | 2023; live page checked 2026-07-10 | Current authoritative AI risk framework; AI RMF 1.0 revision is in progress | Continuous governance, adjudicated external feedback, documented human oversight, deployment-context evaluation | Risk-management framework, not an editorial workflow |
| E02 | [NIST AI RMF Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) | government profile / primary | 2024; page updated 2026-04-08 | Current authoritative cross-sector profile | Ground-truth comparison, combined human and automated evaluation, provenance and assumption documentation | Broader GAI risk profile, not task-feedback taxonomy |
| E03 | [NIST AI 800-4 monitoring overview](https://www.nist.gov/news-events/news/2026/03/new-report-challenges-monitoring-deployed-ai-systems) | government research summary / primary | 2026-03-09; updated 2026-03-18 | Current; explicitly reports unresolved monitoring gaps | Human-factor monitoring, feedback burden, drift, human-validated monitoring, risk-based cadence | Landscape of challenges, not settled implementation standard |
| E04 | [GAO-26-107863 lessons-learned assessment](https://files.gao.gov/reports/GAO-26-107863/index.html) | government audit / primary | 2026 | Current authoritative audit synthesis | Collect, analyze, validate, archive, and share; validate the right lesson and applicability scope | Financial-system context; principles generalized cautiously |
| E05 | [NASA Lessons Learned](https://www.nasa.gov/nasa-lessons-learned/) | government operational system / primary | page updated 2023-07-26 | Official reviewed lessons system | Reviewed lessons connect driving event and recommendation; continual improvement uses existing policy/training channels | Landing-page description, not full internal process detail |
| E06 | [IHI Model for Improvement: Testing Changes](https://www.ihi.org/library/model-for-improvement/testing-changes) | improvement-method owner / primary | live page checked 2026-07-10 | Authoritative owner of the cited PDSA guidance | Small tests, predictions, observed results, refinement, expansion only after desired improvement | Healthcare origin; method adapted without copying cadence |
| E07 | [Google SRE Workbook: Postmortem Culture](https://sre.google/workbook/postmortem-culture/) | practitioner handbook / primary | 2018 | Stable first-party operational practice | Factual records, measurable impact, root cause, preventative actions, owner/tracking, review and follow-through | Incident context is higher severity than ordinary editorial work |
| E08 | [AWS Well-Architected: Correction of Error](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.coe.en.html) and [COE example](https://aws.amazon.com/blogs/mt/creating-a-correction-of-errors-document/) | practitioner framework / primary | 2020 / 2023 | First-party operational guidance | Data-supported root cause, reviewed corrective actions, owner and due date | Incident-oriented and more procedural than this release needs |
| E09 | [GOV.UK: Measuring user satisfaction](https://www.gov.uk/service-manual/measuring-success/measuring-user-satisfaction) | government service standard / primary | 2016; updated 2021 | Stable authoritative service guidance | Use multiple feedback sources, identify significant patterns, test changes with users, monitor expected effect | Statistical significance is not always available for a single-user editorial office |
| E10 | [GOV.UK: Analyse a research session](https://www.gov.uk/service-manual/user-research/analyse-a-research-session) | government service guidance / primary | 2016 | Stable authoritative qualitative-analysis guidance | Separate observations from interpretation, cluster patterns, discard irrelevant/isolated notes, derive findings then actions | Research-session context, not all post-delivery feedback |
| E11 | [GOV.UK: User research introduction](https://www.gov.uk/service-manual/user-research/how-user-research-improves-service-design) | government service guidance / primary | 2016; updated 2017 | Stable authoritative user-research guidance | Focus on outcomes and real use, not popularity or preference alone; reduce bias through shared analysis | Larger service-team assumptions require adaptation |
| E12 | [Microsoft Research: Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/) and [guideline list](https://www.microsoft.com/en-us/research/blog/guidelines-for-human-ai-interaction-design/) | peer-reviewed research / primary | CHI 2019 | Validated through multiple evaluation rounds and a practitioner study | Efficient correction, uncertainty scoping, cautious adaptation, granular feedback, user control | Interaction design guidance, not organizational canon governance |
| E13 | [Google PAIR: Feedback and Control](https://pair.withgoogle.com/guidebook-v2/chapter/feedback-controls/) | practitioner research guide / primary | 2019; live guide checked 2026-07-10 | First-party guide grounded in product research | Distinguish implicit/explicit feedback, align feedback with actionable improvement, preserve privacy/control, allow preferences to change | Allows direct model feedback in some products; this release explicitly forbids automatic promotion |
| E14 | [GitLab Customer Issues Prioritization Framework](https://handbook.gitlab.com/handbook/product/product-processes/customer-issues-prioritization-framework/) | public product handbook / primary | updated 2026-04-09 | Current first-party operational process | Multi-channel feedback triage, privacy context, timely review without mandating outcome, product-owner autonomy | Commercial product prioritization details do not transfer directly |
| E15 | [Agile Manifesto principles](https://agilemanifesto.org/principles.html) and [Atlassian retrospective guidance](https://www.atlassian.com/agile/scrum/retrospectives) | foundational principle plus practitioner guide / primary | 2001 / live guide checked 2026-07-10 | Stable principle; current first-party operational guide | Reflect and adjust; select a small number of actionable improvements with owners and follow-through | Does not justify a retrospective for every task in this system |

## Source sufficiency

- Coverage: organizational learning, continuous improvement, customer feedback,
  lessons learned, postmortems, retrospectives, product feedback, evidence-
  based change, knowledge promotion, human-in-the-loop AI, and AI evaluation.
- Contradictions: none material. Sources differ on cadence and formality, but
  converge on evidence, validation, ownership, bounded action, and follow-up.
- Known gap: no repository evidence yet proves ordinary-task Domain Pack value;
  S5.R1 must enable capture without claiming that value is already confirmed.
