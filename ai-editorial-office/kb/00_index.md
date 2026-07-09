# KB index

`/kb` stores reusable editorial standards and reference material. It does not own workflow lifecycle, role boundaries, or artifact responsibility rules unless a specific KB file is named as canonical owner in `AGENTS.md`.

Canonical KB ownership:

- `task_statuses.md` owns allowed operational task statuses and transitions.
- `shared_lifecycle_kernel.md` owns shared lifecycle stages, gates, artifact
  responsibilities, expansion triggers, human approval boundary, and stage
  context contracts. It does not replace `AGENTS.md`, role specs, selected
  pipelines, task statuses, review rules, or task-local artifacts.
- `task_object_model.md` owns the architecture model for task-object fields and
  for how task-local artifacts act as views over task state. It does not make
  every field or artifact mandatory for every task.
- `capability_registry.md` owns the reusable capability map and the mapping from
  current roles to the capabilities they wrap. It does not create new roles,
  agents, pipelines, validators, or mandatory artifacts.
- `editorial_evidence_framework.md` owns evidence taxonomy, confidence labels,
  evidence requirements by output type, reusable evidence collection, and the
  optional evidence section standard. It does not create a new role, workflow
  engine, scoring system, or mandatory artifact set.
- `analytical_reasoning.md` owns practical analytical reasoning moves:
  problem framing, decomposition, hypothesis generation, competing
  explanations, key assumptions checking, disconfirmation, contradiction
  handling, sufficiency judgment, and uncertainty communication. It does not
  create a new role, pipeline, framework, review gate, scoring model, or
  mandatory artifact set.
- `professional_analysis.md` owns practical Professional Analysis moves:
  analytical product shape, structured interpretation, synthesis,
  recommendation building, implications, risks, uncertainty, and
  decision-ready analytical communication. It does not create a new role,
  framework, pipeline, lifecycle stage, review gate, scoring model, consulting
  methodology, or mandatory artifact set.
- `professional_communication.md` owns practical Professional Communication
  moves: message architecture, recommendation presentation, explanation fit,
  technical communication, information density, actionability, and preservation
  of evidence and caveats during reader transfer. It does not create a new
  role, grammar/style checklist, framework, pipeline, lifecycle stage, review
  gate, scoring model, content-design system, UX-writing system, consulting
  methodology, or mandatory artifact set.
- `architecture_review.md` owns practical Architecture Review moves:
  architectural significance, architecture drivers, quality-attribute
  scenarios, tradeoff analysis, architecture-specific risks, architectural
  assumptions, architecture evidence, and decision-rationale challenge. It does
  not create a new role, framework, pipeline, lifecycle stage, review gate,
  scoring model, or mandatory artifact set.
- `engineering_review.md` owns practical Engineering Review moves:
  implementation/change safety, engineering review lenses, proportional
  evidence, validation expectations, and engineering residual risk. It does not
  create a new role, framework, pipeline, lifecycle stage, review gate,
  scoring model, or mandatory artifact set.
- `editorial_failure_modes.md` owns common editorial failure modes and recovery
  patterns. It is a practical safety layer, not a new role system, incident
  process, workflow engine, review gate, or mandatory checklist.
- `editorial_planning_framework.md` owns planning depth, option generation,
  option evaluation, decision selection, recommendation formation, and planning
  completion criteria. It does not create a new role, scoring matrix, workflow,
  review gate, or mandatory planning artifact.
- `audience_outcome_alignment.md` owns audience identification, intended
  outcome, reader context, required action or decision, detail level, tone and
  format fit, artifact success criteria, mismatch warning signs, and correction
  patterns. It does not create a persona system, new role, workflow, review
  gate, or mandatory audience artifact.
- `editorial_quality_attributes.md` owns shared editorial quality attributes,
  quality tradeoffs, task-specific quality priorities, evaluation guidance, and
  lifecycle quality preservation. It does not create a scoring framework,
  mandatory checklist, new role, workflow, or review process.
- `editorial_learning_framework.md` owns reusable learning, Knowledge
  Evolution, canonization criteria, learning extraction, pattern confirmation,
  canon evolution, stale-knowledge challenge, canon correction/retirement, and
  memory disposition. It does not create a memory database, Historian role,
  Knowledge Curator role, automatic documentation process, or mandatory
  retrospective.
- `domain_knowledge_pack_standard.md` owns Domain Knowledge Pack purpose,
  structure, activation, source/evidence requirements, domain boundaries,
  forbidden content, review, update, retirement, and relation to existing
  roles, capabilities, canonical owners, and `/about`. It does not create a
  domain pack, role, pipeline, lifecycle stage, review gate, policy owner,
  capability owner, task status model, client profile, mandatory ordinary task
  artifact, or automatic canon-promotion path.
- `software_architecture_domain_pack.md` is the release-candidate Software
  Architecture Domain Knowledge Pack. It provides source-backed software
  architecture context for architecture-sensitive tasks. It does not own
  Architecture Review, Engineering Review, roles, workflows, policies, review
  outcomes, task statuses, or mandatory artifacts.
- `feedback_patterns.md` owns recurring or significant feedback pattern tracking; it does not store every task-local feedback item.
- `customer_feedback_loop.md` owns the active P5.5 customer feedback workflow:
  task-local capture, classification, watchlist signal, backlog candidate, and
  guardrails. It does not override `AGENTS.md`, review-gate, or task-local
  governance artifacts.
- `feedback_loop.md` is a compatibility entry point for older references; it
  should point to `customer_feedback_loop.md`, not define a separate taxonomy.
- `source_provenance.md` gives practical guidance for importing, cleaning,
  activating, reviewing, and updating external or client-specific source
  material. It does not override `AGENTS.md`, client-profile activation rules,
  or task-local governance artifacts.
- `research_evidence.md` gives practical guidance for choosing no-research,
  compact-evidence, or full-evidence depth. It does not override `AGENTS.md`,
  selected pipelines, role specs, review-gate, or source provenance rules.
  Evidence classes and confidence labels are owned by
  `editorial_evidence_framework.md`.
- `compact_execution.md` gives practical guidance for compact execution and
  artifact minimalism. It does not override `AGENTS.md`, selected pipelines, or
  task-local governance artifacts.
- `codex_task_standard.md` gives practical guidance for turning a normalized
  brief into a compact Codex task and check-pack. It does not create a new role,
  pipeline, capability pack, validator, or mandatory artifact.
- `clients/CLIENT-ID/` owns task-scoped client profiles. Client profiles are
  loaded only when `task-manifest.md` or `orchestration_plan.md` explicitly
  activates them.
- Other KB files own reusable standards, examples, tone, glossary, and forbidden patterns for editorial work.

Current client profiles:

- `clients/sber/` — Sber client profile. It is not global editorial policy and
  must not activate for independent materials where Sber is only mentioned as a
  topic, example, source, or competitor.

If a KB rule conflicts with `AGENTS.md`, pipelines, or task-local governance, follow the authority hierarchy in `AGENTS.md` and stop if the conflict affects production.
