# AI Editorial Office Architecture Validation Review

Date: 2026-07-08

Status: research / architecture review artifact only. This report does not
modify canon, agents, pipelines, templates, `/about`, `diff_intake.md`,
`project-state.md`, or the legacy repository.

Evidence basis: repository inspection of `AGENTS.md`, `project-state.md`, the
named canonical KB files, related pipeline files, role specs, artifact/task
templates, `research_evidence.md`, `source_provenance.md`, `00_index.md`, and
the two research reports in `ai-editorial-office/research/`.

## 1. Executive Verdict

The current architecture is conceptually coherent and close to minimal at the
fundamental-concept level. It can be explained as:

1. `AGENTS.md` owns authority, invariants, governance, role separation, review
   gate, and artifact minimalism.
2. The task object is the operational primitive.
3. Artifacts are task-local views over task state.
4. Capabilities are reusable operations.
5. Roles are accountability wrappers around capabilities.
6. The shared lifecycle kernel defines common stages, gates, expansion
   triggers, and stage context contracts.
7. Pipelines are task-type overlays over the shared lifecycle.
8. Evidence, failure recovery, planning, audience/outcome, quality, and
   learning frameworks provide reusable lenses, not new pipelines or roles.

The architecture is not minimal at the documentation surface. Many files repeat
protective boundary language, status transitions, artifact sets, and "not a new
role / not a new pipeline / not mandatory" guardrails. Most repetition is
healthy or harmless today, but it creates drift risk as the system evolves.

No high-severity architectural conflicts were found. The highest-risk findings
are medium severity:

| Affected files | Affected concept | Issue type | Severity | Recommended handling |
| --- | --- | --- | --- | --- |
| `kb/research_evidence.md`, `kb/editorial_evidence_framework.md`, `pipelines/research_pipeline.md` | Evidence classes vs source classes | Risky duplication | medium | Clarify that source proximity classes in research artifacts are not the canonical evidence taxonomy. |
| `pipelines/research_pipeline.md`, `kb/task_object_model.md` | `claims_table.md` as "source of truth" | Risky duplication | medium | Reword later to "claim-level evidence view" or "claim-level traceability view" to preserve artifact-as-view semantics. |
| `pipelines/article_pipeline.md`, `pipelines/social_pipeline.md`, `pipelines/ux_writing_pipeline.md`, `pipelines/review_pipeline.md`, `kb/shared_lifecycle_kernel.md`, `kb/task_statuses.md` | Lifecycle, status, artifact, and gate restatement | Risky duplication over time | medium | Prefer documentation simplification: keep task-type deltas in pipelines and reference lifecycle/status owners for shared rules. |

Recommended next step: documentation simplification. Do not merge frameworks,
add roles, add capabilities, add pipelines, or create new canon now.

## 2. Current Architecture Summary

The active architecture is task-object first and capability-aware:

```text
task object first;
capability map second;
roles as accountability wrappers;
workflows and pipelines as execution guidance;
artifacts as views over task state.
```

The reviewed files form this ownership stack:

| Layer | Owner files | Role in architecture | Validation |
| --- | --- | --- | --- |
| Authority and governance | `AGENTS.md` | System invariants, role separation, review gate, authority hierarchy, artifact minimalism, governance boundaries, extension-role legality | Coherent. It is the strongest canonical owner. |
| Current state | `project-state.md` | Active phase, current focus, normalization decisions, repository path, `/about` status | Mostly coherent. It explicitly says it must not become policy, but it is long enough to create shadow-canon pressure. |
| Task state model | `kb/task_object_model.md`, `kb/task_statuses.md` | Task fields, artifact views, allowed statuses and transitions | Coherent. Task object maps concepts; statuses remain separately owned. |
| Capability map | `kb/capability_registry.md` | Reusable operations and role-capability mapping | Coherent. It repeatedly blocks role proliferation. |
| Shared lifecycle | `kb/shared_lifecycle_kernel.md` | Shared stages, gates, expansion triggers, artifact behavior, context contracts | Coherent and compact enough. It references frameworks rather than absorbing them. |
| Supporting frameworks | Evidence, failure, planning, audience/outcome, quality, learning KB files | Reusable decision lenses | Mostly necessary and separate. Some protective language is duplicated. |
| Execution overlays | `pipelines/*.md` | Task-type sequence, artifact depth, local quality gates | Coherent but most duplication lives here. |
| Role specs | `agents/*.md` | Role-local responsibilities, boundaries, stop conditions | Coherent. They mostly wrap capabilities without creating new roles. |
| Templates | `templates/artifacts/*.md`, `templates/tasks/*.md` | Fillable shapes and scaffolds | Mostly coherent. A few task templates look stricter than pipeline conditionality. |
| Research reports | `research/editorial_competency_landscape.md`, `research/editorial_deliverables_landscape.md` | Preliminary research, not canon | Properly marked as non-canonical research. |

This review intentionally created only this report because the user constrained
the task to a research / architecture review artifact. That is a task-scoped
exception to the normal task-local manifest/status/orchestration bootstrap, not
a new operating precedent.

## 3. Concept Inventory

### Essential Concepts

| Concept | Primary owner | Why essential | Architecture criticality if removed |
| --- | --- | --- | --- |
| Authority hierarchy and canonical ownership | `AGENTS.md` | Prevents conflicting rules and second sources of truth. | core |
| Task object | `kb/task_object_model.md` | Gives the system one operational primitive. | core |
| Artifact-as-view principle | `AGENTS.md`, `kb/task_object_model.md` | Prevents artifact bloat and independent local truth stores. | core |
| Operational statuses | `kb/task_statuses.md` | Keeps workflow state deterministic. | core |
| Shared lifecycle stages and gates | `kb/shared_lifecycle_kernel.md` | Coordinates pipelines and restart behavior. | core |
| Role separation and review gate | `AGENTS.md`, `agents/*.md`, `pipelines/review_pipeline.md` | Prevents self-review, premature finalization, and governance collapse. | core |
| Capability registry | `kb/capability_registry.md` | Allows reusable operations without multiplying roles. | supporting |
| Evidence and confidence model | `kb/editorial_evidence_framework.md` | Keeps claims, recommendations, review findings, and final decisions grounded. | core |
| Failure modes and recovery | `kb/editorial_failure_modes.md` | Gives weak-stage recovery without inventing ad hoc process. | supporting |
| Planning and option evaluation | `kb/editorial_planning_framework.md` | Prevents first-plausible route selection in non-trivial work. | supporting |
| Audience and outcome alignment | `kb/audience_outcome_alignment.md` | Prevents correct but unusable artifacts. | supporting |
| Quality attributes | `kb/editorial_quality_attributes.md` | Gives review and production a shared vocabulary for tradeoffs. | supporting |
| Learning and canon evolution | `kb/editorial_learning_framework.md` | Prevents unvalidated memory and duplicated canon. | supporting |

### Derived Concepts

| Concept | Derived from | Affected files | Validation |
| --- | --- | --- | --- |
| Preflight Gate | Task object, lifecycle, evidence, audience/outcome | `AGENTS.md`, `templates/artifacts/orchestration_plan_template.md`, `agents/chief_editor.md` | Valid as a compact decision in existing artifacts. |
| Editorial Decision Frame | Planning, audience/outcome, evidence, Chief Editor routing | `AGENTS.md`, `templates/artifacts/orchestration_plan_template.md`, `agents/chief_editor.md`, `agents/review_agent.md` | Valid as an orchestration section, not a standalone artifact. |
| Editorial Challenge Lens | Review, planning, evidence, failure recovery | `AGENTS.md`, `pipelines/review_pipeline.md`, `agents/review_agent.md`, `templates/tasks/review_task_template.md` | Valid as a review lens, not a new gate. |
| Quality profile | Quality attributes, task object | `kb/editorial_quality_attributes.md`, `templates/artifacts/orchestration_plan_template.md` | Valid when material, optional otherwise. |
| Learning candidate / canon update candidate | Learning framework, task object | `kb/editorial_learning_framework.md`, `kb/task_object_model.md`, `agents/chief_editor.md`, `agents/review_agent.md` | Valid as task-local signal until reviewed. |
| Current-version pointer | Task object, artifact minimalism | `AGENTS.md`, `kb/task_object_model.md`, `kb/task_statuses.md`, templates, pipelines | Valid and important, but repeated in many files. |
| Compact execution | Artifact minimalism, risk mode, lifecycle | `AGENTS.md`, `kb/compact_execution.md`, pipelines | Valid as an operating profile, not a separate pipeline. |

### Redundant Or Over-Expanded Concepts

| Affected files | Affected concept | Issue type | Severity | Recommended handling |
| --- | --- | --- | --- | --- |
| Most canonical and role/pipeline files | "not a new role / not a new pipeline / not mandatory artifact" disclaimers | Harmless repetition | low | Keep in canonical owners; shorten in overlays to references where safe. |
| `article_pipeline.md`, `social_pipeline.md`, `ux_writing_pipeline.md` | Shared lifecycle and artifact tables | Risky duplication over time | medium | Retain task-specific gates and deltas; reference shared lifecycle/status owners for common material. |
| `project-state.md` | Long list of current normalization decisions | Harmless repetition now, shadow-canon risk later | low | Keep state-only framing; prune stale decisions after stabilization if separately requested. |
| `review_pipeline.md`, `agents/review_agent.md` | Review checks across every framework | Useful but over-expanded | low | Keep review integration, but avoid making every framework check feel mandatory when not material. |
| `templates/tasks/social_task_template.md`, `templates/tasks/ux_writing_task_template.md` | Scaffold-required support files | Harmless repetition with possible over-reading | low | Clarify in future that template folder examples do not override pipeline conditional artifact rules. |

## 4. Canonical Ownership Review

Overall result: permanent rule ownership is mostly clear. The ownership map in
`AGENTS.md` is explicit and consistently referenced by the reviewed files.

| Affected files | Affected concept | Type of issue | Severity | Finding | Recommended handling |
| --- | --- | --- | --- | --- | --- |
| `AGENTS.md` | System invariants, authority, role separation, review gate, artifact minimalism | Healthy owner | none | The charter is the clear canonical owner and contains an explicit ownership map. | No change needed. |
| `project-state.md` | Current phase and normalization decisions | Harmless repetition with shadow-canon risk | low | It repeats many active decisions but explicitly says permanent policy must live in canonical owners. | Keep as state record; avoid adding new permanent policy there. |
| `kb/task_object_model.md` | Task fields and artifact views | Healthy owner | none | It maps fields to views and repeatedly points semantic ownership to framework files. | No change needed. |
| `kb/capability_registry.md` | Capabilities and role-capability mapping | Healthy owner | none | It clearly separates capabilities from roles and names non-role capabilities. | No change needed. |
| `kb/shared_lifecycle_kernel.md` | Shared stages, gates, context contracts | Healthy owner with overlap | low | It owns shared lifecycle and references other frameworks without redefining them deeply. | No change needed now; avoid expanding it further. |
| `kb/editorial_evidence_framework.md` | Evidence taxonomy and confidence labels | Healthy owner | none | It owns evidence semantics and avoids creating a Fact Checker role. | No change needed. |
| `kb/research_evidence.md`, `pipelines/research_pipeline.md` | Evidence depth and source class details | Risky duplication | medium | Evidence depth is valid, but "source class" and allowed source classes can be confused with canonical evidence classes. | Later wording clarification only. |
| `pipelines/research_pipeline.md` | Claim-level traceability | Risky duplication | medium | "claims_table.md is the claim-level source of truth" can be read as independent truth rather than a view over task state. | Later reword to "claim-level evidence view." |
| `pipelines/*.md` | Sequencing, artifact depth, gates | Useful but over-expanded | medium | Pipelines own task-type sequencing, but repeat shared lifecycle/status material in detail. No current conflict found. | Documentation simplification later. |
| `agents/*.md` | Role behavior and boundaries | Healthy reference | none | Role specs own role-local behavior and mostly reference framework owners for shared concepts. | No change needed. |
| `templates/*.md` | Fillable artifact shapes | Mostly healthy | low | Templates are scaffolds, but some task templates list support files as required in ways that may be stricter than pipeline conditionality. | Clarify scaffold-vs-canon wording later if it causes confusion. |
| `research/*.md` | Professional-practice research | Healthy boundary | none | Both reports state they are research artifacts only and do not modify canon. | No change needed. |

## 5. Dependency And Reference Map

The dependency graph is directional enough to be maintainable:

```text
AGENTS.md
  -> names canonical owners and authority hierarchy
  -> constrains project-state, KB, pipelines, roles, templates, tasks

project-state.md
  -> records current state and normalization decisions
  -> must not become permanent policy

task_object_model.md
  -> maps task fields and artifacts as views
  -> references lifecycle, evidence, planning, audience, quality, learning

capability_registry.md
  -> maps reusable capabilities to current accountability roles
  -> references all major frameworks

shared_lifecycle_kernel.md
  -> defines shared stages, gates, expansion triggers, context contracts
  -> consumes framework patterns when material

major frameworks
  -> own reusable semantics
  -> integrate with task object, capability registry, lifecycle, review

pipelines/*.md
  -> overlay task-type sequence, artifacts, local gates
  -> must reference shared lifecycle and status owners for common rules

agents/*.md
  -> define role-local responsibilities, forbidden actions, decisions
  -> wrap capabilities without creating new capability owners

templates/*.md
  -> provide fillable shapes
  -> should not become policy owners
```

Concrete reference findings:

| From | To | Relationship | Severity | Recommended handling |
| --- | --- | --- | --- | --- |
| `AGENTS.md` | All named canonical files | Owner map | none | Keep as the routing source for rule placement. |
| `task_object_model.md` | Evidence, planning, audience, quality, learning frameworks | Field-to-framework mapping | none | Healthy reference. |
| `capability_registry.md` | `agents/*.md` | Capabilities wrapped by roles | none | Healthy reference. |
| `shared_lifecycle_kernel.md` | Framework files | Stage contracts consume framework patterns | none | Healthy as long as semantics stay in framework owners. |
| `pipelines/*.md` | `kb/task_statuses.md` | Status transitions must come from status owner | low | Current references are correct; duplicated transition tables should be watched. |
| `pipelines/*.md` | `kb/shared_lifecycle_kernel.md` | Task-type overlays over shared lifecycle | medium | Strong references exist, but duplicate tables increase drift risk. |
| `agents/review_agent.md` | All major frameworks | Review challenges every material dimension | low | Expected for Review Agent; avoid treating every challenge as mandatory for every task. |
| `templates/artifacts/*.md` | Canonical owners | Fillable shapes with guardrails | low | Keep templates concise and non-authoritative. |

## 6. Overlap Analysis

| Overlap | Affected files | Classification | Issue type | Severity | Recommended handling |
| --- | --- | --- | --- | --- | --- |
| Task object fields overlap evidence, planning, audience, quality, learning | `kb/task_object_model.md`, all major frameworks | Healthy reference | none | none | Keep task object as field map; keep semantics in framework files. |
| Capability records overlap role specs | `kb/capability_registry.md`, `agents/*.md` | Healthy reference | none | none | Capabilities remain reusable operations; roles remain accountability wrappers. |
| Lifecycle stages overlap pipelines | `kb/shared_lifecycle_kernel.md`, `pipelines/*.md` | Harmless repetition trending risky | Risky duplication over time | medium | Shorten pipelines to task-type deltas later. |
| Operational statuses overlap pipeline transition tables | `kb/task_statuses.md`, `pipelines/*.md`, `AGENTS.md` | Harmless repetition | Drift risk | low | Keep `task_statuses.md` as only status owner; avoid new transitions in pipelines unless reflected there. |
| Evidence taxonomy overlaps research evidence modes | `kb/editorial_evidence_framework.md`, `kb/research_evidence.md`, `pipelines/research_pipeline.md` | Risky duplication | Terminology conflict risk | medium | Clarify "evidence class" vs "source proximity/source type." |
| Failure modes overlap evidence, planning, audience, quality, learning | `kb/editorial_failure_modes.md`, other frameworks | Healthy reference | none | none | Failure modes properly operate as recovery routing. |
| Planning framework overlaps Editorial Decision Frame | `kb/editorial_planning_framework.md`, `AGENTS.md`, `templates/artifacts/orchestration_plan_template.md` | Healthy reference | none | none | Keep Decision Frame as the view; keep planning semantics in the framework. |
| Audience/outcome overlaps quality attributes | `kb/audience_outcome_alignment.md`, `kb/editorial_quality_attributes.md` | Healthy reference | none | none | Audience fit can remain a quality attribute while audience framework owns details. |
| Quality attributes overlap review pipeline | `kb/editorial_quality_attributes.md`, `pipelines/review_pipeline.md`, `agents/review_agent.md` | Healthy reference | none | low | Review should challenge quality when material, not impose all attributes by default. |
| Learning framework overlaps project-state and feedback handling | `kb/editorial_learning_framework.md`, `project-state.md`, `kb/customer_feedback_loop.md`, `templates/artifacts/feedback_template.md` | Healthy reference | none | low | Maintain "no automatic canonization" language. |
| AGENTS invariants overlap project-state normalization decisions | `AGENTS.md`, `project-state.md` | Harmless repetition | Shadow-canon risk | low | Keep project-state as current-state log, not permanent rule owner. |
| Review gate rules overlap review pipeline and Review Agent | `AGENTS.md`, `pipelines/review_pipeline.md`, `agents/review_agent.md`, templates | Healthy but verbose repetition | Drift risk | low | Keep governance requirement in `AGENTS.md`; keep role behavior in Review Agent; keep sequencing in pipeline. |
| Artifact minimalism overlaps templates | `AGENTS.md`, `kb/compact_execution.md`, `templates/tasks/*.md` | Harmless repetition | Template over-reading risk | low | Keep templates obviously scaffold-level. |

No actual architectural conflict was found. The two medium findings are wording
and drift risks, not currently broken workflow behavior.

## 7. Framework Necessity Review

| Framework | Unique problem solved | What would break if removed | Overlaps | Recommendation |
| --- | --- | --- | --- | --- |
| Evidence & Confidence: `kb/editorial_evidence_framework.md` | Separates evidence class, confidence, assumptions, unknowns, validation need, and residual risk. | Claims, reviews, recommendations, and final decisions would rely on tone or plausibility. Review blockers would become less reproducible. | `research_evidence.md`, `research_pipeline.md`, source provenance, quality attributes. | Remain separate. Clarify source-class terminology elsewhere. |
| Failure Modes & Recovery: `kb/editorial_failure_modes.md` | Gives a small recovery playbook for wrong-task work, weak evidence, hidden assumptions, scope drift, role confusion, review bypass, artifact bloat, and stale canon. | Agents would either polish weak work or invent ad hoc recovery process. | Evidence, planning, audience, quality, learning. | Remain separate. It is a recovery index, not duplicated framework logic. |
| Planning & Option Evaluation: `kb/editorial_planning_framework.md` | Prevents first-plausible convergence for non-trivial routes, recommendations, and implementation plans. | Editorial Decision Frame would record decisions without enough option discipline. | Editorial Decision Frame, evidence, quality, audience. | Remain separate. Keep the Decision Frame as a compact view over planning. |
| Audience & Outcome Alignment: `kb/audience_outcome_alignment.md` | Makes usefulness depend on reader, outcome, action, detail, tone, evidence burden, and format. | Correct but unusable artifacts would pass more often. Codex and implementation tasks would become vaguer. | Quality attributes, planning, review. | Remain separate. It is not merely a quality attribute. |
| Quality Attributes: `kb/editorial_quality_attributes.md` | Provides shared vocabulary for correctness, completeness, relevance, actionability, clarity, precision, consistency, traceability, evidence support, audience fit, structural coherence, maintainability, implementation readiness, reviewability. | Reviews would collapse into style preference or generic "good/bad" judgments. Tradeoffs would be hidden. | Audience, evidence, planning, review. | Remain separate, but use by materiality. Do not turn into a mandatory checklist. |
| Learning & Canon Evolution: `kb/editorial_learning_framework.md` | Controls what task-local learning can become reusable canon, and how stale canon is challenged. | Single-task notes, raw feedback, `/about` mirrors, or old task folders could become false authority. | Feedback loop, project-state, failure modes, capability registry. | Remain separate. It is the strongest guard against canon sprawl. |

Conclusion: all six major frameworks are necessary as separate conceptual
owners. None should be merged now. The simplification target is repeated prose
around them, not their existence.

## 8. Artifact-As-View Validation

The artifact-as-view principle is consistently stated in `AGENTS.md`,
`kb/task_object_model.md`, `kb/shared_lifecycle_kernel.md`,
`kb/compact_execution.md`, pipelines, and templates. Most artifacts are treated
as task-local views over current state, evidence, decisions, or handoff deltas.

| Area | Affected files | Finding | Type of issue | Severity | Recommended handling |
| --- | --- | --- | --- | --- | --- |
| Charter | `AGENTS.md` | Clearly states artifact minimalism and primary responsibility boundaries. | Healthy reference | none | No change needed. |
| Task object | `kb/task_object_model.md` | Explicitly defines artifacts as views over task state and says not every field requires a standalone file. | Healthy reference | none | No change needed. |
| Lifecycle | `kb/shared_lifecycle_kernel.md` | Gates are confidence decisions recorded in existing artifacts, not mandatory standalone files. | Healthy reference | none | No change needed. |
| Compact execution | `kb/compact_execution.md` | Strongly supports fewer artifacts when reviewable and traceable. | Healthy reference | none | No change needed. |
| Pipelines | `pipelines/*.md` | Mostly conditional artifact policies. Article/social/UX pipelines repeat required/conditional tables heavily. | Drift risk | medium | Later simplify shared portions and retain task-specific deltas. |
| Research pipeline | `pipelines/research_pipeline.md` | Calls `claims_table.md` the claim-level source of truth for downstream factual use. | Risky duplication | medium | Later reword to claim-level evidence or traceability view. |
| Templates | `templates/tasks/social_task_template.md`, `templates/tasks/ux_writing_task_template.md` | Some support files look required at template level, while pipelines make similar artifacts conditional. | Harmless repetition | low | Clarify scaffold-level requirement if confusion appears. |
| Role specs | `agents/*.md` | Roles produce and consume artifacts as evidence, handoff, or controlled output, not independent stores. | Healthy reference | none | No change needed. |

Potential independent-source-of-truth risk:

- `claims_table.md` can become a source of truth for claims if wording is read
  literally. In the architecture, it should be the current claim-level evidence
  view over the task object.
- `project-state.md` can become shadow canon if the normalization list keeps
  growing after stabilization. It currently avoids this by explicitly pointing
  permanent rules back to canonical owners.

## 9. Role-Capability Separation Review

Overall result: clean separation. Capabilities remain reusable operations, and
roles remain accountability wrappers.

| Affected files | Affected concept | Type of issue | Severity | Finding | Recommended handling |
| --- | --- | --- | --- | --- | --- |
| `kb/capability_registry.md` | Capability vs role distinction | Healthy owner | none | Explicitly says capabilities do not create default roles. | No change needed. |
| `AGENTS.md`, `agents/artist_agent.md` | Frozen Artist Agent | Healthy boundary | none | Artist Agent is legalized but frozen and inactive by default. | No change needed. |
| `AGENTS.md`, `kb/capability_registry.md` | Future roles | Healthy boundary | none | Future style/structural/terminology/fact-checker roles are not active. | No change needed. |
| `pipelines/*.md` | Unauthorized extension roles | Healthy repetition | none | Pipelines repeatedly prohibit unauthorized extension roles. | No change needed. |
| `agents/review_agent.md`, `pipelines/review_pipeline.md` | Editorial Challenge Lens | Harmless repetition | low | It is repeatedly stated as not a new role, gate, artifact, or review cycle. | Keep as review lens only. |
| `kb/editorial_evidence_framework.md`, `research_pipeline.md` | Fact-checking and evidence-confidence work | Healthy capability | low | Evidence checks do not create a Fact Checker role. | Keep as capability until a reviewed system update says otherwise. |

No hidden new role was found through capability descriptions. No future
extension role is accidentally active.

## 10. Lifecycle Load Review

The Shared Lifecycle Kernel is still a compact coordination model. It has not
absorbed the full behavior of evidence, planning, quality, audience alignment,
learning, failure recovery, or role behavior. It contains:

- lifecycle shape;
- shared stages;
- shared gates;
- compact vs expanded execution;
- artifact responsibility;
- expansion triggers;
- human approval boundary;
- stage context contracts.

That is a reasonable kernel scope.

Lifecycle load findings:

| Affected files | Affected concept | Type of issue | Severity | Finding | Recommended handling |
| --- | --- | --- | --- | --- | --- |
| `kb/shared_lifecycle_kernel.md` | Expansion triggers | Useful but broad | low | Triggers now reference evidence, audience, quality, planning, learning, and failure-mode concerns. This is acceptable as routing logic. | Avoid adding more framework detail to the kernel. |
| `pipelines/review_pipeline.md` | Review as integration hub | Useful but over-expanded | low | Review integrates all frameworks. This is role-appropriate but can feel overloaded in compact tasks. | Keep materiality language; do not require every lens when irrelevant. |
| `pipelines/article_pipeline.md`, `pipelines/social_pipeline.md`, `pipelines/ux_writing_pipeline.md` | Lifecycle repeated in overlays | Risky duplication over time | medium | These pipelines repeat stages, transitions, gates, risk behavior, restart protocol, and handoff rules. | Documentation simplification later. |
| `AGENTS.md` | Default workflow plus lifecycle references | Harmless repetition | low | AGENTS keeps governance-level lifecycle rules while kernel owns stage contracts. | No change needed. |

Conclusion: lifecycle is not overloaded. The load problem is duplicated
lifecycle prose in overlays, not the kernel itself.

## 11. Research Findings Coverage

The two research reports identify professional practices and deliverables. Most
important findings are already covered structurally by the current architecture.
The remaining gaps are mostly optional future task-local views, not urgent
architecture changes.

| Research finding | Source report | Coverage classification | Current coverage | Architectural materiality | Recommended handling |
| --- | --- | --- | --- | --- | --- |
| Brief interpretation and bad-brief repair | `editorial_competency_landscape.md` | already covered | Intake, task object, Preflight Gate, failure modes | medium | No immediate change. |
| Audience/stakeholder analysis | Both reports | partially covered | Audience/outcome framework covers audience; stakeholder-risk map is not explicit. | low to medium | Do not add now. Consider only for high-impact governance tasks later. |
| Source discovery and source maps | Both reports | partially covered | Evidence framework, research pipeline, source provenance cover evidence after sources exist. Pre-evidence source mapping is lighter. | medium | Future evaluation only if research-heavy tasks show need. |
| Source reliability and provenance | `editorial_competency_landscape.md` | partially covered | Source provenance, research pipeline, evidence framework. | medium | Clarify source class vs evidence class later. |
| Evidence tables and claim traceability | Both reports | already covered / partially covered | `claims_table.md`, `claims-used.md`, facts/sources, evidence framework. | medium | Covered enough; only wording cleanup needed. |
| Domain modeling | `editorial_competency_landscape.md` | missing | No explicit domain-model capability or artifact trigger. | low now, medium for complex tasks | Do not implement now; research finding is not enough to add architecture. |
| Synthesis formats | `editorial_competency_landscape.md` | partially covered | Research artifacts, planning, recommendations, decision frame. | low | No immediate change. |
| Argumentation and recommendation logic | `editorial_competency_landscape.md` | already covered | Planning framework, evidence framework, quality attributes. | medium | No immediate change. |
| Critical review and challenge | Both reports | already covered | Review gate, Review Agent, Review Pipeline, Challenge Lens. | high | No change. |
| Fact-checking and verification logs | Both reports | partially covered | Evidence and review cover the function; no specialized mandatory log. | low to medium | Keep as capability, not role or default artifact. |
| Risk registers and threat models | `editorial_deliverables_landscape.md` | partially covered | Failure modes, quality, review, high-governance rules. | low now | Dangerous if made default. Future task-local view only for ongoing/adversarial risk. |
| Publication readiness checklists | Both reports | partially covered | Finalization, review, governance, optional finalization checklists. | medium for public output | No immediate architecture change. Could remain conditional. |
| Decision records, ADRs, RFCs | Both reports | partially covered | Orchestration plan, final decision, system change proposal template. | medium | No immediate addition. Avoid creating ADR/RFC canon unless system-change work proves need. |
| Knowledge capture and pattern libraries | Both reports | already covered / partially covered | Learning framework, feedback patterns, KB ownership. | medium | No change. |
| Retrospectives and postmortems | Both reports | partially covered | Learning/failure frameworks, feedback loop. | low | Do not make routine. Use only after serious process failure. |
| Artifact conditionality | `editorial_deliverables_landscape.md` | already covered | Artifact minimalism, compact execution, task object. | high | Current architecture aligns strongly. |

Findings not worth implementing directly now:

- mandatory source maps for ordinary research;
- mandatory fact-checking logs for low-risk work;
- generic quality checklists for every task;
- risk registers for simple editorial tasks;
- postmortems as routine closure;
- ADR/RFC process for small documentation or pipeline clarifications.

Findings dangerous if implemented directly:

- converting fact-checking, source conversion, terminology review, or memory
  curation into standing roles;
- treating every professional deliverable in the research report as an AIEO
  artifact;
- promoting research reports into canon without a reviewed owner update;
- treating `/about` memory files as canonical when they diverge from source;
- copying old task-folder structures as templates.

## 12. Architectural Smells

| Affected files | Affected concept | Type of issue | Severity | Concrete smell | Recommended handling |
| --- | --- | --- | --- | --- | --- |
| `pipelines/article_pipeline.md`, `pipelines/social_pipeline.md`, `pipelines/ux_writing_pipeline.md` | Pipeline overlays | Risky duplication | medium | Large duplicated sections for required inputs, artifact sets, allowed stages, transitions, risk behavior, handoffs, gates, escalation, blocked conditions, retry, completion, restart. | Simplify shared prose later; preserve task-specific gates. |
| `pipelines/review_pipeline.md`, `agents/review_agent.md` | Review integration | Useful but over-expanded | low | Review touches evidence, failure, planning, audience, quality, learning, governance, instructional architecture. | Keep review as integration point; apply checks only when material. |
| `pipelines/research_pipeline.md` | Claim source of truth wording | Risky duplication | medium | `claims_table.md` is named as claim-level source of truth. | Rename concept in prose to "view" later. |
| `pipelines/research_pipeline.md`, `kb/research_evidence.md`, `kb/editorial_evidence_framework.md` | Source class vs evidence class | Risky duplication | medium | Research pipeline source classes can be confused with evidence taxonomy. | Clarify terminology later. |
| `project-state.md` | Normalization decisions | Shadow-canon risk | low | Many current decisions live in one state file. | Keep it state-only; prune stale entries only in a separate requested update. |
| `templates/tasks/*.md` | Template required files | Over-reading risk | low | Task templates list folder-level required files that could be mistaken as stronger than pipeline conditionality. | Clarify scaffold wording later. |
| `AGENTS.md`, `agents/*.md`, `pipelines/*.md`, frameworks | Protective disclaimers | Maintenance weight | low | Many files repeat "not a new role/pipeline/artifact." | Shorten overlays after stabilization. |

## 13. Simplification Opportunities

These are simplification opportunities only, not implementation tasks.

| Opportunity | Affected files | Value | Risk | Recommended handling |
| --- | --- | --- | --- | --- |
| Replace duplicated shared lifecycle prose in task-type pipelines with references plus task-specific deltas. | `article_pipeline.md`, `social_pipeline.md`, `ux_writing_pipeline.md`, `review_pipeline.md` | High | Medium if done too aggressively | Documentation simplification, no behavior change. |
| Clarify `claims_table.md` as a claim-level view, not source of truth. | `pipelines/research_pipeline.md`, possibly `kb/research_evidence.md` | High | Low | Ownership clarification within existing files. |
| Rename or clarify research "source class" as source proximity/type. | `pipelines/research_pipeline.md`, `kb/research_evidence.md` | High | Low | Ownership clarification without changing evidence framework. |
| Shorten repeated non-role disclaimers in role specs and pipelines. | `agents/*.md`, `pipelines/*.md` | Medium | Low | Keep one canonical statement in `AGENTS.md` and `capability_registry.md`; leave concise references elsewhere. |
| Mark task templates more clearly as scaffolds and examples. | `templates/tasks/*.md` | Medium | Low | Small documentation clarification only. |
| Keep project-state stateful and eventually prune stale normalization decisions. | `project-state.md` | Medium | Medium because project-state is explicitly forbidden for this task | Do not touch now. Consider later only if requested. |

Do not simplify by merging the six major frameworks. Their overlap is mostly
integration, not duplicate ownership.

## 14. Refactoring Options Considered

| Option | Verdict | Reason |
| --- | --- | --- |
| No refactor needed now | Plausible but not selected | No high-severity conflict exists, but medium drift/wording risks are real enough to justify a small future simplification. |
| Documentation simplification | Selected | Highest value with smallest behavior risk. It can reduce duplicated lifecycle/status/artifact prose without changing architecture. |
| Ownership clarification | Useful subset | Especially valuable for `claims_table.md` wording and source-class terminology, but narrower than the main duplication issue. |
| Concept merge | Rejected | Evidence, failure, planning, audience, quality, and learning solve distinct problems. Merging would reduce clarity. |
| Concept split | Rejected | Shared Lifecycle Kernel is not overloaded enough to split. |
| Removal of redundant text | Useful subset | Should happen as part of documentation simplification, not as broad deletion. |
| Targeted architectural addition | Rejected | Research gaps do not justify new canon, roles, capabilities, pipelines, or artifacts now. |

## 15. Recommended Next Step

Recommended next step: documentation simplification.

Scope of the recommended future refactor:

- Keep all current concepts, roles, capabilities, pipelines, and canon owners.
- Do not add frameworks, roles, pipelines, or artifact requirements.
- Shorten repeated shared lifecycle/status/artifact sections in pipelines.
- Retain only task-type-specific differences in each pipeline.
- Clarify `claims_table.md` as a claim-level evidence view.
- Clarify research source classes as source proximity/type, separate from the
  Evidence Framework taxonomy.
- Leave research findings as research until a future, reviewed system-update
  task proves a material gap.

Refactor recommendation: yes, but only as documentation simplification. No
large rewrite is recommended.

## 16. Final Verdict

AI Editorial Office has a coherent foundation. It is minimal in concepts but
verbose in documentation. The system does not need a redesign, new framework,
new role, new pipeline, or new canon rule.

Final findings:

- Current architecture minimality: mostly yes at concept level; no at prose
  duplication level.
- Conceptual duplication: mostly healthy references and harmless repetition;
  medium risk around pipeline duplication, source-class terminology, and
  `claims_table.md` source-of-truth wording.
- Ownership boundaries: clear, with low shadow-canon pressure in
  `project-state.md`.
- Artifact-as-view principle: consistently applied, with one medium wording
  risk in `research_pipeline.md`.
- Role-capability separation: clean; no hidden role activated.
- Lifecycle load: acceptable; duplicated overlay prose is the issue, not the
  kernel.
- Framework necessity: all six major frameworks should remain separate.
- Research coverage: most professional practices are already covered or
  intentionally conditional; missing items are not architecturally material
  enough to implement now.

Final recommendation: preserve the architecture and perform only a future
documentation simplification if the user asks for a refactor.
