# Tests

Эта папка зарезервирована для будущих проверок целостности проекта.

Она существует как место, куда можно будет добавить простые проверки структуры,
навигации, синхронизации служебных пакетов или других безопасных invariants.

Статус папки: активная как место для будущей инфраструктуры. Сейчас содержит
markdown smoke-tests и synthetic examples:

- `sber-mode-smoke-test.md`
- `compact_execution_examples.md` - synthetic examples for compact execution
  and artifact minimalism; these are not task materials.
- `feedback_loop_examples.md` - synthetic examples for feedback classification;
  these are not task materials.
- `feedback_loop_smoke_test.md` - markdown manual smoke-test for feedback
  classification; these cases are synthetic and are not task materials.
- `feedback_loop_manual_trial.md` - sanitized manual trial for post-delivery
  feedback classification; it is not task materials.
- `feedback_loop_acceptance_trial.md` - sanitized manual trial for
  acceptance/future preference feedback classification; it is not task
  materials.
- `source_provenance_examples.md` - synthetic examples for source status
  classification; these are not task materials or source files.
- `source_provenance_smoke_test.md` - markdown manual smoke-test for
  source/provenance classification; these cases are synthetic and are not
  source materials.
- `research_evidence_examples.md` - synthetic examples for no-research,
  compact-evidence, and full-evidence mode selection; these are not task
  materials.
- `research_evidence_smoke_test.md` - markdown manual smoke-test for research
  evidence mode selection; these cases are synthetic and are not task materials.
- `test_task_pack_generator.sh` - shell smoke-test for
  `scripts/generate_task_pack.py`.
- `preflight_gate_examples.md` - synthetic examples for Preflight Gate routing
  decisions `ask`, `constrain`, `proceed`, and `block`; these are not task
  materials and do not replace Intake Agent, Chief Editor, or `AGENTS.md`.
- `preflight_gate_smoke_test.md` - markdown manual smoke-test for Preflight
  Gate routing; these cases are synthetic and are not task materials.
- `preflight_gate_manual_trial.md` - sanitized manual trial for checking
  whether Preflight Gate examples are useful on a realistic scenario; it is not
  task materials.
- `preflight_gate_sber_trial.md` - sanitized manual trial for checking Sber
  profile activation vs non-activation; it is not task materials.
- `preflight_gate_ux_trial.md` - sanitized manual trial for checking UX routing
  with missing product context; it is not task materials.
- `preflight_gate_checker_decision.md` - decision note recording why automated
  Preflight checker is not added yet; it is not production governance.
- `engineering_review_smoke_test.md` - manual synthetic cases for Engineering
  Review activation and non-activation; it is not production governance.
- `professional_communication_smoke_test.md` - manual synthetic cases for
  Professional Communication activation and non-activation; it is not
  production governance.
- `reader-centered-quality-pilot.md` - three-type manual calibration pilot for
  longread, working document, and short text; external comparator promotion
  remains pending.
- `reader-centered-quality-smoke-test.md` - manual synthetic regression cases
  for Reader Outcome Contract, Learning Design, Reader Review, Companion Pass,
  bounded utility tradeoffs, and compact non-activation.
- `outcome_first_deliverable_selection_smoke_test.md` - manual synthetic
  regression cases for requested/recommended/selected deliverable separation,
  explicit-intent preservation, delegated format choice, outcome-fit
  sufficiency, pipeline-after-deliverable ordering, mismatch escalation, and
  compact non-activation.
- `test_outcome_first_deliverable_selection.sh` - executable static regression
  check for the canonical owner text, orchestration ordering, ten-case synthetic
  suite, and absence of forbidden Deliverable/Format Agent or pipeline files.
- `knowledge_evolution_smoke_test.md` - manual synthetic cases for Knowledge
  Evolution disposition, stale-knowledge challenge, canon-update candidates,
  and `/about` memory sync; it is not production governance.
- `editorial_intelligence_acceptance_smoke_test.md` - twelve manual synthetic
  cases for the conditional Stage 5 value-and-restraint acceptance contract;
  it is not a score, automatic verdict, or operational improvement evidence.
- `feedback_learning_intelligence_smoke_test.md` - manual synthetic cases for
  feedback classification, outcome evidence, learning disposition, owner
  routing, Domain Pack effect evidence, rejection/deferral, stale learning, and
  non-promotion; it is not production governance or real usage evidence.
- `evaluation_signals_smoke_test.md` - manual synthetic cases for advisory
  Evaluation Signals, bounded counts, qualitative judgments, owner routing,
  noise rejection, contradictory signals, and explicit non-decision; it is not
  production governance or real usage evidence.
- `task_need_recognition_smoke_test.md` - manual synthetic cases for advisory
  task type, capability/Domain Pack, research/evidence, risk/consequence,
  review, significance, ambiguity, decomposition, uncertainty, negative
  evidence, and Chief Editor decision separation; it is not an automatic
  router or real usage evidence.
- `domain_knowledge_pack_standard_smoke_test.md` - manual synthetic cases for
  Domain Knowledge Pack activation, non-activation, source boundaries, review,
  update, retirement, and forbidden architecture drift; it is not production
  governance.
- `end_to_end_cases/access_pass_security_task/` - sanitized end-to-end case for
  an internal access-pass security task; it is not task materials and contains
  no real credentials, real cards, real system details, or exploit instructions.
- `end_to_end_cases/cybersecurity_toolkit_feedback/` - sanitized end-to-end
  case for an internal cybersecurity toolkit feedback request; it is not task
  materials and contains no real methodology, meeting records, PSI materials,
  client data, or confidential content.
- `end_to_end_cases/system_thinking_course_task/` - sanitized end-to-end case
  for an internal course-development task; it is not task materials and
  contains no real course source files, confidential methodology, internal
  training materials, participant data, client data, or restricted content.

## Task lifecycle validator smoke test

Запуск:

```bash
bash ai-editorial-office/tests/test_task_lifecycle_validator.sh
```

Smoke-test запускает `scripts/validate_task_lifecycle.py` на synthetic fixtures
из `tests/fixtures/task_lifecycle/`: valid и warning-only cases должны пройти с
exit code `0`, invalid cases должны завершиться с exit code `1`.

Сейчас smoke-test покрывает базовые lifecycle gates, consistency current status
между `task-manifest.md` и `status.md`, selected pipeline existence и
warning-only missing selected pipeline case. Он также покрывает previous/current
status transition checks из `kb/task_statuses.md`: invalid known transitions
дают blocker, missing previous status и same previous/current status дают
warning. Валидатор трактует unknown status как warning, а не blocker.

Fixtures в `tests/fixtures/task_lifecycle/` полностью искусственные и не
являются real task materials. Они нужны только для проверки локального
валидатора. Тест и валидатор не меняют task-файлы.

## Task pack generator smoke test

Запуск:

```bash
bash ai-editorial-office/tests/test_task_pack_generator.sh
```

Smoke-test запускает `scripts/generate_task_pack.py` на synthetic fixtures из
`tests/fixtures/task_pack/`. Fixtures полностью искусственные и не являются
real task materials. Они проверяют writer, review_agent, final_editor blocker и
chief_editor feedback read sets.

Feedback loop examples and smoke-test are used for manual classification checks:
they help verify when a user reaction is a task-local note, bounded revision,
possible system pattern, or system change proposal. They do not define active
rules and do not replace Chief Editor, Review Agent, `AGENTS.md`, or separate
reviewed system updates.

`feedback_loop_manual_trial.md` records a sanitized post-delivery scenario and
checks classification as bounded revision plus possible pattern watch. It is
not task materials and does not store real feedback.

`feedback_loop_acceptance_trial.md` records a sanitized accepted-result scenario
with a future preference. It checks that acceptance does not reopen the task and
does not become bounded revision without an explicit current-artifact change
request.

Source provenance examples and smoke-test are used for manual source-status
classification checks: they help verify `pending_source`, `active`, `stale`,
and `deprecated` handling. They are not source materials and do not replace
`AGENTS.md`, source notes, client-profile activation rules, or reviewed source
updates.

The reusable source import smoke-test template lives in
`templates/artifacts/source_import_smoke_test_template.md`. Real source import
smoke-tests should be added only for approved sanitized/source-safe cases.

Research evidence examples and smoke-test are used for manual evidence-depth
checks: they help verify when `no-research`, `compact-evidence`, or
`full-evidence` is appropriate. They do not define active rules and do not
replace `AGENTS.md`, selected pipelines, Research Agent, Writer Agent, Review
Agent, or `kb/research_evidence.md`.

Preflight Gate examples and smoke-test are used for manual routing checks only:
they help verify when the safe next strategy is `ask`, `constrain`, `proceed`,
or `block`. They do not define active rules and do not replace Intake Agent,
Chief Editor, or `AGENTS.md`.

`preflight_gate_manual_trial.md` records a sanitized trial of those examples on
a realistic internal coordination scenario. It is used to assess usefulness and
future checker needs, not to store real task materials.

`preflight_gate_sber_trial.md` records a sanitized trial for Sber-owned
communication versus Sber-as-topic routing. It checks when `client_profile`
should be `sber` and when it should remain `none`.

`preflight_gate_ux_trial.md` records a sanitized trial for UX writing with
missing product context. It checks when `ux_writing` can start through
`constrain` without inventing product behavior.

`preflight_gate_checker_decision.md` records the current decision to keep
Preflight Gate checks manual after three sanitized trials. It explains why an
automated checker is not added yet.

`engineering_review_smoke_test.md` records synthetic positive and negative
activation cases for `/kb/engineering_review.md`. It checks that engineering
lenses activate for code, security, configuration, delivery automation,
interface, observability, reliability, data, and performance surfaces, and do
not activate for ordinary editorial or planning-only tasks. It does not define
active rules or replace Chief Editor, Review Agent, `AGENTS.md`, or the
Engineering Review KB.

`professional_analysis_smoke_test.md` records synthetic positive and negative
activation cases for `/kb/professional_analysis.md`. It checks that
Professional Analysis activates for structured interpretation, synthesis,
recommendation, implications, technology assessment, policy/product/business
analysis, and executive decision briefs, and does not activate for ordinary
summaries, copyediting, Architecture Review, or Engineering Review. It does not
define active rules or replace Chief Editor, Review Agent, `AGENTS.md`, or the
Professional Analysis KB.

`professional_communication_smoke_test.md` records synthetic positive and
negative activation cases for `/kb/professional_communication.md`. It checks
that Professional Communication activates for executive briefs, recommendation
presentation, technical explanations, implementation handoffs, policy or
stakeholder memos, research/evidence communication, dense source compression,
and actionability failures, and does not activate for grammar, generic style,
Audience & Outcome Alignment ownership, UX copy ownership, Architecture
Review, Engineering Review, or Professional Analysis ownership. It does not
define active rules or replace Chief Editor, Review Agent, `AGENTS.md`, or the
Professional Communication KB.

`reader-centered-quality-pilot.md` records the longread baseline evidence and
two synthetic calibration cases used to select full, normal, and compact Reader
Review depth. It explicitly does not claim comparator parity or production
improvement without actual paired outputs and Project Lead judgment.

`reader-centered-quality-smoke-test.md` records eight synthetic cases that
separate reader outcome from readability, preserve evidence guardrails, test
good and bad cognitive bridges and bounded tradeoffs, reject taste-only review,
and keep short low-risk text compact. It does not define active rules or replace
the canonical owners listed in the file.

`outcome_first_deliverable_selection_smoke_test.md` records ten synthetic cases
for explicit article and presentation requests, delegated learning format,
invalid checklist substitution for an explanation, presentation use context,
comparison matrix, decision memo, BRD/specification ambiguity, material format
mismatch, and trivial copy repair. It checks that the selected deliverable is
outcome-fit and recorded before pipeline selection without creating a role,
pipeline, lifecycle stage, gate, score, or mandatory standalone artifact. It
does not define active rules or prove real-world improvement.

Run the bounded static contract check with:

```bash
sh ai-editorial-office/tests/test_outcome_first_deliverable_selection.sh
```

The script verifies canonical integration and test coverage only. It does not
classify requests, select deliverables, route tasks, or replace Review Agent.

`knowledge_evolution_smoke_test.md` records synthetic disposition cases for
`/kb/editorial_learning_framework.md`. It checks that reusable learning,
pattern candidates, canon-update candidates, stale/conflicting knowledge,
correction or retirement candidates, and `/about` sync are scoped through the
existing owner and review path. It does not define active rules or replace
Chief Editor, Review Agent, `AGENTS.md`, or the Editorial Learning Framework.

`feedback_learning_intelligence_smoke_test.md` records the nine S5.R1
representative cases. It checks the bridge between the Customer Feedback Loop
and Editorial Learning Framework, including the distinction between feedback
classification and learning disposition, qualitative evidence sufficiency,
affected owner, bounded action, actual Domain Pack activation versus effect,
rejection/deferral, and explicit non-promotion. It does not define active rules
or prove that a synthetic pattern or Domain Pack effect exists in real tasks.

`evaluation_signals_smoke_test.md` records the eight S5.R2 representative
cases. It checks repeated successful and rejected releases, rare and frequent
Domain Pack activation, repeated architecture warnings, repeated stale
knowledge, a noisy activity metric, and contradictory signals. It verifies
decision question, evidence, comparison scope, denominator/exposure when
material, alternatives, confidence, existing owner, and explicit non-decision.
It does not define active rules, create scores or automatic actions, or prove
that the synthetic signals exist in real tasks.

`memory_hygiene_intelligence_smoke_test.md` records the ten S5.R3
representative cases. It checks exact-copy synchronization, research no-sync,
temporary-state replacement, stale status correction, canon/memory
contradiction, large-release compression, sensitive/task-local omission,
explicit no-sync, duplicate consolidation, and obsolete-memory retirement. It
verifies source, materiality, disposition, owner, branch validation, canonical
authority, bounded growth, preserved meaningful context, and no automatic
propagation. It does not define active rules or prove memory completeness.

`task_need_recognition_smoke_test.md` records the ten S5.R4 representative
cases. It checks simple editing, architecture review, engineering
implementation, AI Engineering, DevSecOps, Cybersecurity, ambiguous mixed,
multi-domain, research-heavy, and keyword-rich simple requests. It verifies
observed signal versus recommendation versus Chief Editor decision separation,
proportionate evidence/review depth, capability and Domain Pack boundaries,
negative evidence, uncertainty, decomposition, and explicit non-automation. It
does not define active rules, create a classifier/score/router, or prove
real-world routing improvement.

`editorial_intelligence_acceptance_smoke_test.md` records the twelve S5.R5
representative cases. It checks improvement claims, evidence setting,
real-use/synthetic limits, meaningful comparison, false-positive and
false-negative consequences, architecture/governance impact, human authority,
automation, reversibility, maintenance, uncertainty, cross-effects, and human
recommendations to accept, accept with observations, request changes, defer,
narrow, reject, or retire/supersede. It does not define active rules, create a
score or automatic disposition, or prove that the contract improves real
Project Lead decisions.

`domain_knowledge_pack_standard_smoke_test.md` records synthetic activation,
non-activation, boundary, source, update, retirement, and review cases for
`/kb/domain_knowledge_pack_standard.md`. It checks that Domain Knowledge Packs
remain source-backed context packages and do not become roles, pipelines,
lifecycle stages, review gates, policy owners, capability owners, client
profiles, task status models, or mandatory ordinary task artifacts. It does not
define active rules or replace Chief Editor, Review Agent, `AGENTS.md`, or the
Domain Knowledge Pack Standard.

`end_to_end_cases/access_pass_security_task/` records a synthetic sanitized
end-to-end editorial case. It checks Preflight Gate `constrain`, compact
execution, no-research mode, no external source import, task pack generator
context, and review-gated finalization. It is not a real task folder and does
not contain real credentials, real cards, real system details, or exploit
instructions.

`end_to_end_cases/cybersecurity_toolkit_feedback/` records a synthetic
sanitized end-to-end editorial case. It checks Preflight Gate `proceed`,
compact execution, no-research mode, no external source import, task pack
generator context, and review-gated finalization. It is not a real task folder
and does not contain real methodology, meeting records, PSI materials, client
data, or confidential content.

`end_to_end_cases/system_thinking_course_task/` records a synthetic sanitized
end-to-end editorial case. It checks Preflight Gate `constrain`, compact
execution with source summary, compact-evidence mode, task-local supplied source
provenance, task pack generator context, and review-gated finalization. It is
not a real task folder and does not contain real course source files,
confidential methodology, internal training materials, participant data, client
data, or restricted content.

Читайте эту папку, когда нужно найти или добавить проверку целостности проекта.

Не читайте её как источник редакционных правил, пайплайнов или требований к
ролям.

Содержимое `tests/` не определяет активные правила системы. Тесты, если они
появятся, должны проверять уже существующие правила, а не создавать новые.
