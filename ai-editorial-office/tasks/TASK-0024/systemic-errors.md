# Каталог системных ошибок

Frequency is estimated across the inspected task corpus.

| Error group | Frequency | Impact | Origin stage | Detection stage | Current defenses | Defense effectiveness |
| --- | --- | --- | --- | --- | --- | --- |
| Inconsistent editorial entry | High historically; low in recent mature tasks | High | Intake / Chief Editor | Audit, later maintenance, missing artifacts | `AGENTS.md` entry discipline, task manifest, status, orchestration plan | Strong when activated; not retroactive |
| Missing or inferred task context | Medium-high | High | Intake | Planning, review, final decision, user follow-up | Normalized Brief Contract, explicit unknowns, source boundary | Improving; still needs preflight |
| Premature production | Medium historically | High | Intake / routing | Audit, review, final decision | Required routing before production, review gate, visual branch rules | Good in current rules; weak in direct legacy tasks |
| Wrong or unstable depth | Medium | Medium-high | Chief Editor | Retrospective, maintenance, audit | Compact/expanded profiles, artifact minimalism, orchestration artifact scope | Moderate; needs artifact budget |
| Artifact bloat | Medium | Medium | Chief Editor / all roles | Retrospective, maintenance compression | Canonical ownership map, artifact creation policy, compact review | Improving but not fully internalized |
| Research omitted without visible source boundary | Medium historically | High when factual claims exist | Chief Editor / Research | Review or audit | Source boundary, research decision rationale, claims artifacts | Strong in mature tasks; absent in sparse tasks |
| Research or traceability heavier than needed | Low-medium | Medium | Chief Editor | Retrospective, maintenance, compact later tasks | No-research rationale, compact source-contained route | Good recently |
| Unsupported certainty / claim creep | Medium | High | Writing | Review | Research, `claims_table.md`, `claims-used.md`, source boundary | Strong when traceability exists |
| Generic-but-safe output | Medium | Medium | Intake / Writing | Review, user feedback | Reader-state planning, anti-genericity/relevance checks | Moderate |
| Synthetic editorial warmth | Medium | Medium-high | Writing / variant selection | Review and user feedback | Tone rules, fake warmth checks, bounded revision | Moderate-good |
| Abstractness before action | High in source materials; medium in produced drafts | High for operational docs | Intake / Writing | Review, structure-before-writing comparison | Structure-before-writing, reader path checks | Strong after `SYSTEM-MAINTENANCE-0004` |
| Duplicated process explanation | Medium | Medium | Writing / structure | Review, QA checklist | Section-role map, selective reading checks | Good in operational tasks |
| Review focuses on artifact more than task understanding | Medium | High | Review | Audit, occasional user follow-up | Checked scope, brief compliance, editorial relevance checks | Mixed |
| Weak review independence signal in compact tasks | Low-medium | Medium-high | Review | Audit | Reviewer role, independence basis requirements | Good when explicitly written; inconsistent phrasing |
| Publication readiness conflated with editorial readiness | Medium | Medium-high | Finalization / governance | Final decision | Human approval disclaimers, placeholder notes | Good in final decisions; should move earlier |
| Visual direct path / insufficient semantic ownership | High in visual precursor tasks; low after `TASK-0020` | High | Routing / production | Maintenance and audit | Visual concept, sketchnote brief, Artist Agent prerequisites, frozen subsystem | Strong currently if followed |

## grouped observations

### 1. Entry and scope failures

Most damaging failures begin before writing. They include absent task package,
unclear audience, unknown channel, missing approval owner, and inferred context
treated as working truth.

Examples:

- `TASK-0002` shows the good version: unknowns are explicit and constrained.
- `TASK-0011` - `TASK-0019` show the historical weak version: outputs exist
  without enough task-local evidence of routing and review.
- `TASK-0023` shows a mild current risk: audience/channel are plausible but
  partly inferred.

### 2. Process-depth failures

The system has alternated between too much process and too little process.

Too heavy:

- early full lifecycle validation;
- separate QA/review-summary/finalization artifacts for small tasks.

Too light:

- direct outputs without review;
- strong recommendation documents without lifecycle state;
- visual outputs before mature visual branch.

### 3. Meaning and claim failures

The recurring writing risk is not hallucination in the dramatic sense. It is
small unsupported certainty:

- "most frequent";
- implied productivity effect;
- implied organizational practice;
- implied active usage;
- promise-like launch language;
- source fact turned into stronger operational rule.

Review catches this well when claims artifacts or source snapshots exist.

### 4. Reader-outcome failures

Operational materials repeatedly fail when they explain a system before helping
the reader act. The system has learned to catch this through:

- reader route;
- shortest successful path;
- section roles;
- answer-first behavior;
- selective reading.

`TASK-0004B` is the clearest proof that this defense works.

### 5. Tone and relevance failures

The system repeatedly fights:

- HR tone;
- fake warmth;
- corporate optimism;
- launch rhetoric;
- pleasant but replaceable copy;
- editorial flourish that feels written-up.

Review catches these fairly well, but `TASK-0003B` shows that user feedback is
still needed when the difference is taste-sensitive and contextual.

### 6. Final readiness failures

The system is good at stating that publication approval is outside the task.
The remaining issue is timing: approval, link insertion, and practical delivery
dependencies should be visible before final decision whenever they affect user
success.
