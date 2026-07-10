# Evaluation Signals Release Report

Date: 2026-07-10

Release: `S5.R2 - Evaluation Signals`

Status: Release Candidate ready for Project Lead architectural review; all
final validations passed and the local commit remains

## Executive summary

S5.R2 implements Evaluation Signals as an optional advisory view over evidence
AI Editorial Office already saves. The view helps the Project Lead and current
canonical owners see material capability activation, Domain Pack effect,
review, architecture, evidence, learning, stale-knowledge, release, and
maintenance observations without converting them into scores, KPIs, rankings,
targets, maturity levels, gates, dashboards, or automatic actions.

The release preserves a strict separation:

```text
saved observation
-> contextual interpretation
-> human decision
```

Chief Editor may assemble a material view inside an existing artifact. Review
Agent challenges evidence, comparison, missing cases, alternatives,
contradictions, confidence, proportionality, owner routing, and non-decision.
Project Lead or the existing canonical owner decides. No signal can accept or
reject a release, change canon, reprioritize backlog or roadmap, modify memory,
or retire a capability or Domain Pack automatically.

## Release goal

Improve the quality of Project Lead decisions by making important system and
release evidence visible while ensuring Evaluation Signals remain optional,
evidence-backed, reviewable, advisory, and subordinate to current authority.

The release does not attempt to score AI Editorial Office.

## Research completed

The landscape covers:

- engineering performance and productivity metrics;
- software quality indicators;
- architecture evaluation and fitness indicators;
- monitoring and organizational observability;
- evidence-based evaluation and continuous improvement;
- capability maturity assessment;
- product-health measurement;
- AI evaluation practice.

Primary and authoritative sources include
[DORA](https://dora.dev/guides/dora-metrics/), the peer-reviewed
[SPACE framework](https://queue.acm.org/detail.cfm?id=3454124),
[ISO/IEC 25010](https://www.iso.org/standard/78176.html),
[SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/),
[Google SRE](https://sre.google/sre-book/monitoring-distributed-systems/), the
2026 [Magenta Book](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html),
[IHI PDSA](https://www.ihi.org/library/model-for-improvement/testing-changes),
[ISO/IEC 33020](https://www.iso.org/standard/78526.html),
[Google HEART](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/),
and the [NIST AI RMF](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/).

The sources converge on multidimensional, context-bound, proportionate,
decision-oriented evidence and on the dangers of single metrics, activity
proxies, target gaming, unlike comparisons, hidden uncertainty, and excessive
measurement overhead.

## Architecture decision

### Selected shape

One optional Evaluation Signal view inside existing task, review, pattern,
release, or governance artifacts.

### No new owner or structure

The release adds no:

- Evaluation capability or framework;
- signal taxonomy, database, dashboard, telemetry, scanner, or trend engine;
- role, pipeline, lifecycle stage, task status, or review gate;
- mandatory artifact or task-object field;
- score, KPI, target, threshold, rank, maturity level, or automatic action.

### Existing owners retained

| Signal family | Existing owner retained |
| --- | --- |
| Capability activation | Task manifest/orchestration evidence and Capability Registry meaning |
| Domain Pack use and usefulness | Domain Knowledge Pack Standard, active pack, and Learning Framework for reuse |
| Review recurrence | Review Agent/Review Pipeline and Learning Framework/pattern journal for reuse |
| Architecture risk/drift | Architecture Review |
| Evidence quality | Editorial Evidence Framework |
| Learning promotion and stale knowledge | Editorial Learning Framework |
| Release observations | Review, validation, final decision, release report/pack, Project Lead verdict |
| Maintenance burden | Saved task/release evidence and affected canonical owner |

The Learning Framework is the integration point only because it already owns
whether saved observations remain local or become reusable decision signals.
It does not take ownership of the technical meaning of each signal family.

## Implemented signal contract

When a material human decision would benefit, the compact view makes these
facts reconstructable:

- decision question;
- observation without decision language;
- exact evidence pointers;
- bounded scope and comparison window;
- denominator or exposure opportunity when material;
- missing, excluded, or ambiguous cases;
- interpretation;
- contradictions and alternative explanations;
- confidence, unknowns, and evidence still needed;
- existing affected owner;
- optional human consideration;
- explicit non-decision.

The view is created only when saved evidence and decision value justify its
capture cost. Absence is not evidence of health or improvement.

## Count and qualitative boundaries

Counts and frequencies are allowed only as descriptive evidence with comparable
scope and denominator/exposure context. They cannot become targets, scores,
ranks, maturity bands, individual measures, or automated decisions.

Qualitative judgment remains mandatory for:

- Domain Pack usefulness;
- evidence sufficiency;
- architecture drift and tradeoff significance;
- release value;
- review rejection meaning;
- maintenance burden versus enduring value;
- learning promotion;
- stale-knowledge action;
- contradictory signals;
- release acceptance or changes requested.

## Noise and contradiction handling

The mechanism rejects or defers activity-only, unbounded, incomparable,
untraceable, duplicate, biased, high-maintenance, or automatic-action signals.

Contradictory signals remain separate. The view compares scope, time window,
task mix, exposure, source strength, and outcome; identifies distinguishing
evidence; and lowers confidence when contradiction remains. It does not average,
vote, or apply a tie-break rule.

## Files changed

### Canonical and active owner files

- `ai-editorial-office/agents/chief_editor.md`
- `ai-editorial-office/agents/review_agent.md`
- `ai-editorial-office/kb/00_index.md`
- `ai-editorial-office/kb/editorial_learning_framework.md`
- `ai-editorial-office/kb/feedback_patterns.md`
- `ai-editorial-office/pipelines/review_pipeline.md`
- `ai-editorial-office/templates/release-pack.md`
- `ai-editorial-office/project-state.md`

### Strategic and operational state

- `ai-editorial-office/ROADMAP.md`
- `ai-editorial-office/BACKLOG.md`

### Release, research, validation, and task trace

- three required S5.R2 research/release artifacts;
- `ai-editorial-office/tests/evaluation_signals_smoke_test.md`;
- `ai-editorial-office/tests/README.md`;
- `ai-editorial-office/releases/S5-R2/release-pack.md`;
- `ai-editorial-office/tasks/TASK-EVALUATION-SIGNALS-RELEASE/`.

### Memory package

- exact copies synchronized for project state, Chief Editor, Review Agent, and
  Review Pipeline;
- compact Editorial Standards, Usage Rules, and project tree summaries updated;
- `/about` remains a non-canonical export.

## Files intentionally unchanged

- `AGENTS.md`: no governance or authority change.
- `kb/capability_registry.md`: no new capability.
- `kb/editorial_evidence_framework.md`: existing evidence model is sufficient.
- `kb/architecture_review.md`: existing architecture review model is sufficient.
- `kb/domain_knowledge_pack_standard.md`: S5.R1 already provides actual-use
  effect evidence.
- `kb/task_object_model.md`: no field added.
- `kb/shared_lifecycle_kernel.md`: no lifecycle change.
- Domain Pack files: no real use evidence supports pack-specific edits.
- root `diff_intake.md`: preserved and excluded.
- `/Users/sa/Documents/codex/redaction`: untouched.

## Representative validation

All eight required synthetic cases pass:

| Scenario | Result | Decision boundary demonstrated |
| --- | --- | --- |
| Repeated successful release | pass | Repeatability and realized value remain distinct; no automatic acceptance |
| Repeated rejected release | pass | Quality gap and healthy-gate explanations remain visible |
| Rare Domain Pack activation | pass | Opportunity denominator prevents automatic retirement |
| Frequent Domain Pack activation | pass | Actual benefit/burden/mixed/unknown evidence prevents value-by-volume |
| Repeated architecture warning | pass | Driver/scenario-backed pattern routes to existing owner without automatic canon |
| Repeated stale knowledge | pass | Verification supports a candidate, not automatic deletion/update |
| Noisy metric | pass | Activity count without decision value is rejected |
| Contradictory signals | pass | Signals remain separate and confidence is constrained |

The scenarios validate contract behavior only. They do not prove actual system
improvement or current capability, Domain Pack, or release value.

## Final validation results

| Check | Result |
| --- | --- |
| `git diff --check` | passed |
| `git diff --cached --check` | passed on authorized release stage |
| `sh ai-editorial-office/scripts/check_about_memory_package.sh` | passed |
| `sh ai-editorial-office/tests/test_task_lifecycle_validator.sh` | passed |
| `sh ai-editorial-office/tests/test_task_pack_generator.sh` | passed |
| `python3 ai-editorial-office/scripts/validate_task_lifecycle.py ai-editorial-office/tasks/TASK-EVALUATION-SIGNALS-RELEASE` | passed with 0 blockers and 0 warnings after finalization |
| Eight-case manual smoke test | passed |

## State normalization

S5.R1 acceptance commit `fb3b932` updated the Release Verdict and Backlog but
intentionally left broader state surfaces unchanged. The explicit S5.R2 mission
authorizes and requires current release work, so S5.R2 normalizes:

- S5.R1: accepted and `Done`;
- S5.R2: current Release Candidate in `Review`;
- S5.R3-S5.R5: `Not Started`;
- next action: Project Lead reviews S5.R2; do not start S5.R3 automatically.

## Risks and limitations

- Counts may still be read as targets despite guardrails; review must challenge
  decision language and missing context.
- Low real-world event volume limits trend claims; default to task-local,
  unknown, or deferred.
- Optional capture may produce missing data; absence cannot be interpreted as a
  healthy result.
- Synthetic cases prove routing behavior, not practical signal value.
- A future evidence volume may justify tooling, but no current evidence supports
  it.

## Postponed

- automated scanning, telemetry, dashboards, trend computation, benchmarking,
  statistical inference, and per-role measurement;
- maturity assessment or scorecards;
- automatic signal-to-proposal conversion;
- automatic release, canon, backlog, roadmap, memory, Domain Pack, capability,
  or owner action;
- task-need recognition work reserved for S5.R4.

## Release state

The implementation is complete, independent review is approved with no open
findings, controlled finalization is complete, and final staged validation
passes. Only the local Release Candidate commit and delivery handback remain.

The release may move to `Review`, never `Done`, in this mission. Project Lead
acceptance remains pending.
