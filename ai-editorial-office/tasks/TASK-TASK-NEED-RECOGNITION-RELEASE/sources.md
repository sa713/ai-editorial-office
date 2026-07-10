# Sources

## Selection policy

- Last checked: 2026-07-10.
- External practice sources are primary government publications, official
  professional-method sources, first-party platform documentation, or primary
  research papers.
- Repository sources are current canonical owners or accepted release context.
- External sources inform practice. Repository canon controls implementation.
- No source is treated as instruction authority over `AGENTS.md` or the user
  mission.

## External source register

| ID | Source | Class | Freshness | Reliability | Used for | Limits |
| --- | --- | --- | --- | --- | --- | --- |
| S01 | [NASA Systems Engineering Handbook: Stakeholder Expectations Definition](https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/) | Primary government engineering guidance | current page, checked 2026-07-10 | high | stakeholder, intended use, end state, constraints, and lifecycle-context intake | system-engineering context; not an editorial routing method |
| S02 | [NASA Systems Engineering Handbook: System Design Processes](https://www.nasa.gov/reference/4-0-system-design-processes/) | Primary government engineering guidance | current page, checked 2026-07-10 | high | transform expectations into problem/requirements; communicate iteratively; logical decomposition | formal technical requirements are deeper than ordinary editorial intake |
| S03 | [SEI Quality Attribute Workshops, Third Edition](https://www.sei.cmu.edu/library/quality-attribute-workshops-qaws-third-edition/) | Primary professional-method report | 2003 foundational report, checked 2026-07-10 | high for architecture intake | stakeholder drivers, quality attributes, scenarios before architecture exists | intentionally architecture-specific and older |
| S04 | [GOV.UK Service Manual: How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) | Primary government service-design guidance | maintained page, checked 2026-07-10 | high | problem framing, user/context, constraints, research proportionality, wider journey, stop/no-build decision | service discovery is much larger than ordinary task recognition |
| S05 | [Digital.gov: Reframing](https://digital.gov/guides/hcd/discovery-operations/reframing) | Primary U.S. government human-centered-design guidance | maintained page, checked 2026-07-10 | high | who/what/why/goal framing and narrowing research to preserve resources | design-research context, not universal task taxonomy |
| S06 | [GitHub Docs: Syntax for issue forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms) | First-party platform documentation | living, checked 2026-07-10 | high for GitHub behavior | structured issue type, current/expected behavior, reproduction, environment, and context capture | platform mechanism; labels/types are not a universal ontology |
| S07 | [GitHub Docs: Managing issue fields](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/managing-issue-fields-in-your-organization) | First-party platform documentation | living, checked 2026-07-10 | high for GitHub behavior | separate structured fields for priority, effort, impact, and work-item metadata | field availability and defaults are platform-specific |
| S08 | [GitHub Docs: Triaging an issue with AI](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/triaging-an-issue-with-ai) | First-party AI-assisted intake guidance | living, checked 2026-07-10 | high for stated behavior | actionability/missing-information suggestions followed by human review and action | product/action behavior is volatile; not independent evidence of accuracy |
| S09 | [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | Primary government cybersecurity publication | final April 2025, checked 2026-07-10 | high | incident-response context, impact reduction, risk-management integration, response depth | does not prescribe AI Editorial Office statuses or exact severity levels |
| S10 | [Google SRE: Product-focused reliability](https://sre.google/resources/practices-and-processes/product-focused-reliability-for-sre/) | First-party professional engineering guidance | living, checked 2026-07-10 | medium-high | user-impact-based severity, product-specific criticality, proportional effort, do-not-apply-every-method warning | examples are Google/product context and include numeric local thresholds |
| S11 | [Google SRE: Incident Management Guide](https://sre.google/resources/practices-and-processes/incident-management-guide/) | First-party professional engineering guidance | living, checked 2026-07-10 | medium-high | impact signals, actionable alerts, automated analysis/suggestions with human incident roles | operational incident response is adjacent, not an editorial workflow |
| S12 | [Larson et al.: An Evaluation Dataset for Intent Classification and Out-of-Scope Prediction](https://arxiv.org/abs/1909.02027) | Primary peer-reviewed research paper | EMNLP 2019, checked 2026-07-10 | high for reported study | supported-intent classification, out-of-scope recognition, and misclassification risk | short task-oriented utterances and fixed intent classes differ from rich editorial tasks |
| S13 | [Ong et al.: RouteLLM](https://arxiv.org/abs/2406.18665) | Primary research paper | 2024, checked 2026-07-10 | high for reported study | learned model routing as performance/cost optimization and a contrast case for forbidden automatic routing | routes between models, not roles/capabilities/packs; automatic design is out of scope here |
| S14 | [Amershi et al.: Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf) | Primary CHI research paper | 2019, checked 2026-07-10 | high for reported synthesis/validation | make capabilities and error limits clear; preserve verification, correction, control, and context under uncertainty | interaction-design guidance; not a routing algorithm |
| S15 | [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) and [Appendix C: Human-AI Interaction](https://airc.nist.gov/airmf-resources/airmf/appendices/app-c-ai-risk-management-and-human-ai-interaction/) | Primary government AI risk guidance | AI RMF 1.0 current with revision noted, checked 2026-07-10 | high | context mapping, risk-proportional activity, task/method categorization, documented limits, differentiated human-AI roles, human decision authority | voluntary AI-risk framework; repository use is bounded synthesis |

## Repository evidence register

| ID | Source set | Evidence class | Used for |
| --- | --- | --- | --- |
| R01 | `AGENTS.md`, `project-state.md`, `ROADMAP.md`, `BACKLOG.md` | Repository inspection / canon and management state | authority, stable architecture, release scope, Chief Editor ownership, RC boundary |
| R02 | `kb/task_object_model.md`, `kb/capability_registry.md`, `kb/shared_lifecycle_kernel.md`, `kb/task_statuses.md` | Repository canon | task fields, reusable capabilities, routing/preflight, stage context, allowed states |
| R03 | `kb/editorial_evidence_framework.md`, `kb/analytical_reasoning.md`, `kb/professional_analysis.md`, `kb/professional_communication.md`, `kb/architecture_review.md`, `kb/engineering_review.md` | Repository canon | evidence/confidence, analysis, significance, communication, architecture, and engineering boundaries |
| R04 | `kb/domain_knowledge_pack_standard.md` and all four active Domain Packs | Accepted repository context | activation/non-activation, primary/adjacent pack selection, keyword-only rejection, evidence limits |
| R05 | `kb/customer_feedback_loop.md`, `kb/editorial_learning_framework.md`, S5.R1-S5.R3 Release Packs and synthesis artifacts | Accepted Stage 5 canon/context | Evaluation Signal boundaries, evidence/interpretation/decision separation, existing-owner integration, memory disposition |
| R06 | `agents/intake_agent.md`, `agents/chief_editor.md`, `agents/research_agent.md`, `agents/review_agent.md`, `agents/final_editor.md`, `pipelines/research_pipeline.md`, `pipelines/review_pipeline.md` | Repository canon | role allocation, independence, research/review consequences, release task flow |
| R07 | `templates/artifacts/task_manifest_template.md`, `templates/artifacts/orchestration_plan_template.md`, `templates/release-pack.md` | Repository canon/template | smallest existing artifact view and Release Pack standard |

## Exclusions

- Commercial SEO summaries, unsourced taxonomies, and generic “best practice”
  lists were excluded.
- Automatic classifier/router designs are evidence about what the mission
  forbids, not implementation precedents.
- No exact numeric threshold, score, confidence percentage, taxonomy, or
  universal severity ladder is imported into repository canon.

## Access and freshness notes

- Living provider/platform pages may change and must be rechecked before future
  product-specific claims.
- NIST AI RMF 1.0 notes an in-progress revision; use here is limited to durable
  context, role, and human-oversight principles.
- SEI QAW and the CHI human-AI guidelines are foundational rather than current
  product documentation; their use is limited to durable practice patterns.
