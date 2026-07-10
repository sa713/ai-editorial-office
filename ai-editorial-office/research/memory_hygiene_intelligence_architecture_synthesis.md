# Memory Hygiene Intelligence Architecture Synthesis

## Decision

S5.R3 does not need a new capability, owner, role, pipeline, lifecycle stage,
review gate, memory store, or synchronization mechanism.

Implement Memory Hygiene Intelligence as a bounded refinement of the existing
`editorial_learning_framework.md` memory-disposition owner, using the existing
Memory Curation, Pattern Reuse and Stale Knowledge Detection, and Integrity
Checking capabilities. Chief Editor owns materiality and disposition; Writer
Agent performs explicit authorized edits; Review Agent independently validates
fidelity, semantics, privacy, compactness, and authority; existing read-only
checks report exact-copy/package drift; Project Lead remains release acceptance
authority.

## Architecture question

What is missing after Knowledge Evolution and Evaluation Signals, and what is
the smallest change that lets the office decide when and how external memory
should change without creating parallel governance?

## Existing ownership analysis

### Already owned by canonical ownership rules

- `AGENTS.md` owns authority hierarchy, canonical ownership, role separation,
  review, artifact minimalism, and `/about` non-authority.
- `project-state.md` owns current project/release state, not permanent rules.
- canonical KB/role/pipeline files own their respective durable behavior.
- the `/about` checker owns the executable 20-file and exact-copy comparison
  contract; it is not a content owner.

No S5.R3 change to `AGENTS.md`, task statuses, task object, shared lifecycle,
evidence framework, domain packs, customer-feedback classification, or the
Release Pack template is justified.

### Already owned by Knowledge Evolution

`editorial_learning_framework.md` already owns:

- memory disposition;
- source-evidence chains;
- task-local versus reusable placement;
- stale/conflicting knowledge challenge;
- correction, supersession, and retirement;
- canon evolution and canonical-owner routing;
- `/about` as a non-canonical export;
- Review Agent challenge and Chief Editor classification.

Knowledge Evolution answers whether reusable knowledge or canon should change.
It does not yet answer the full external-memory hygiene decision: whether a
particular canonical change or drift signal should become exact-copy, compact
summary, correction, compression, retirement, omission, deferral, or no-sync,
and what validation each branch requires.

### Already owned by Evaluation Signals

Evaluation Signals may surface saved evidence of:

- likely `/about` drift;
- repeated stale facts;
- contradiction or duplication;
- maintenance burden or bloat;
- repeated sync/validation failures.

The signal remains advisory. It cannot select a memory disposition, write or
delete memory, alter canon, or prove completeness. S5.R3 consumes a material
signal as one possible input to Chief Editor judgment; it does not extend
Evaluation Signals into action.

### Specific S5.R3 responsibility

Memory Hygiene Intelligence owns the bounded decision and validation contract
for external memory after a canonical change or memory-hygiene signal:

```text
canonical change or saved memory-hygiene signal
-> identify canonical source and evidence
-> materiality, purpose, sensitivity, and continuing-value check
-> exact-copy | compact-summary | correct | compress | retire |
   omit | defer | no-sync
-> branch-appropriate validation
-> independent review
-> explicit manual memory update or preserved no-change
```

It does not own canon, repository history, feedback classification, release
acceptance, or a new operational lifecycle.

## Capability decision

### No new capability

The capability registry already provides the needed operations:

- Memory Curation;
- Knowledge Evolution and Learning Extraction;
- Canon Evolution;
- Pattern Reuse and Stale Knowledge Detection;
- Integrity Checking.

S5.R3 refines their existing input/output/quality boundaries. Naming a separate
Memory Hygiene capability would duplicate them and falsely imply a new owner.

### Existing role allocation

| Decision/action | Existing owner | Boundary |
| --- | --- | --- |
| Detect material canonical change or receive saved drift signal | Chief Editor; advisory checker/Evaluation Signal may report | Detection is not disposition or permission to write |
| Identify canonical source and memory representation | Chief Editor | `/about` cannot choose its own source |
| Choose disposition and record material no-sync | Chief Editor | Must use saved evidence, purpose, sensitivity, and current canon |
| Research source ambiguity or freshness | Research Agent when assigned | Does not decide canon or memory action |
| Edit exact copy or compact summary | Writer Agent under explicit contract | Cannot add new rules or memory-only facts |
| Validate package/exact copies | Existing read-only checker | Reports only; cannot write or validate summary semantics |
| Validate compact-summary meaning and all omission/retirement consequences | Review Agent | Existing review gate; no new gate |
| Controlled final summary/pointer | Final Editor | Cannot reclassify disposition or change canon |
| Accept release | Project Lead | Remains outside RC implementation |

## Disposition contract

| Disposition | Trigger | Required evidence | Output | Validation |
| --- | --- | --- | --- | --- |
| `exact-copy` | Active operational wording in the defined copy map changed | canonical source path; copy mapping | synchronized package copy | byte identity and package-count check |
| `compact-summary` | External orientation/state/constraint changed materially but full source is unnecessary | canonical source set; external use; material facts/boundaries | concise derived statement in an existing summary | source/summary semantic comparison and review |
| `correct` | Memory contradicts canon, contains stale facts, or misstates scope/authority | current canonical owner/state and conflict evidence | corrected fact or replacement | old claim absent; new claim source-faithful |
| `compress` | Useful memory is verbose, repeated, or crowded by lower-value detail | source pointers; continuing-value and duplication analysis | consolidated compact summary | unique meaning/caveats retained; duplication/growth reduced |
| `retire` | Content is obsolete, superseded, misleading, or lacks continuing external value | current source/state; replacement or retirement rationale | active memory removal/replacement | no active stale assertion; meaningful history remains in repository |
| `omit` | Content is repository-only, raw, temporary, task-local, sensitive, private, or externally unnecessary | purpose/sensitivity/applicability check | no memory content | prohibited detail absent; no required external context lost |
| `defer` | Source, evidence, authorization, accepted state, or safe summary is unresolved | unresolved issue and next verification | no speculative change; existing safe context only | ambiguity remains visible in task/release record |
| `no-sync` | Canon changed but represented external facts and package contract remain accurate | affected source and materiality rationale | package unchanged | re-check relevant memory and record only when material |

The contract uses plain-language labels for governance clarity. These are not
task statuses, lifecycle states, metrics, or mandatory fields in every task.

## Exact-copy versus compact-summary architecture

### Exact-copy branch

Use only for files explicitly selected by the package mapping because exact
operational wording is required. The source file is the sole content owner.
The package copy must not be independently edited. Validation is deterministic
byte identity plus the fixed package-count check.

### Compact-summary branch

Use when external memory needs durable orientation rather than full operational
instructions. The summary must identify or be reconstructable from canonical
sources and preserve:

- current state/decision and next action when material;
- source/authority and non-canonical status;
- scope and applicability/non-applicability;
- role, approval, and automation boundaries;
- meaningful caveats, exceptions, risks, and uncertainty;
- replacement/supersession state when old memory would mislead.

It should omit raw evidence, task-local history, implementation narration,
repeated wording, and details already discoverable in repository-only files.
Validation is semantic and independent; the checker cannot prove this branch.

## Sync triggers

Run the disposition check when one of these is material:

- an exact-copy source changes;
- accepted/current release, active phase, next action, or approval state changes;
- canonical roles, authority, lifecycle, supported features, package usage, or
  critical constraints change in a way external memory represents;
- `/about` package mapping/count/check behavior changes through reviewed canon;
- a checker reports exact-copy/package mismatch;
- repository inspection, review, saved feedback/outcome, or an Evaluation
  Signal reports stale, contradictory, duplicated, bloated, sensitive, or
  misleading memory;
- temporary RC/transition state becomes accepted, rejected, superseded, or
  obsolete;
- a summary's source path, role name, status, validator, or scope no longer
  resolves or remains accurate.

No wall-clock schedule and no per-commit sync mandate are introduced.

## No-sync and omission triggers

Prefer `no-sync` or `omit` when:

- a change is only internal research, evidence, test detail, task-local history,
  draft debate, implementation narration, or release mechanics;
- no fact represented in external memory changed;
- the existing summary remains accurate and sufficient;
- exporting temporary state would create churn without durable use;
- detail is sensitive, private, client-specific, credential-bearing,
  source-restricted, or security-sensitive;
- adding the detail would duplicate a current memory fact or repository source;
- the external-memory value is lower than maintenance, bloat, or misuse risk.

`no-sync` is a positive reviewed disposition, not an omitted check. Record it in
an existing release report, final decision, or Release Pack only when material
to governance or restart. Do not create a per-commit memory log.

## Staleness and contradiction repair

Indicators:

- exact-copy mismatch;
- state/status/next-action conflict;
- missing or renamed source/role/path/validator;
- temporary/current/latest language no longer supported by a current owner;
- broader or more certain summary than canon;
- two memory facts disagree or duplicate the same source with different scope;
- obsolete content remains active;
- sensitive detail remains after purpose ends;
- package growth lacks new durable external value.

Repair sequence:

1. stop relying on the disputed memory fact;
2. identify the canonical owner and reviewed state;
3. correct, compress, replace, or retire from canon when the owner is clear;
4. if canon conflicts, repair canon first and defer/block memory change;
5. validate the appropriate branch;
6. independently review authority, meaning, privacy, growth, and context loss;
7. record material correction/retirement/no-sync evidence in an existing
   release/governance artifact.

No compromise wording, silent deletion of meaningful context, or memory-driven
canon edit is allowed.

## Compression, duplication, and retirement

Compression is justified when it increases signal density without changing
meaning. Consolidate duplicates into the strongest existing summary location,
merge unique scope/caveats/source pointers, and remove redundant statements.

Retirement removes obsolete content from active external memory. It does not
delete repository history. Use replacement wording when the old fact is
superseded; use removal when no replacement is needed. Preserve a repository
pointer/rationale when future readers may need to understand the change.

No memory size score, target, completeness ratio, or per-release fact quota is
introduced. Growth is bounded by continuing external value, package count,
deduplication, and independent review.

## Evidence and auditability

When memory disposition is material, the smallest existing release, review,
final-decision, or implementation artifact should make these reconstructable:

- source signal and canonical source path(s);
- currently represented memory fact/location;
- materiality, purpose, sensitivity, and continuing-value judgment;
- chosen disposition and why alternatives were not selected when non-obvious;
- exact-copy or summary validation performed;
- correction/consolidation/retirement context preserved;
- reviewer outcome;
- explicit non-automation and canonical-authority boundary.

These are conditional evidence fields, not a new artifact schema or mandatory
task-object extension.

## Advisory automation boundary

Allowed:

- count the package files;
- compare mapped exact copies byte-for-byte;
- report missing/mismatched paths, unresolved references, or likely drift;
- emit a warning for human triage.

Not allowed:

- write, summarize, delete, consolidate, or retire memory automatically;
- change canon to fit memory;
- select disposition or infer sensitivity automatically;
- propagate feedback, draft, RC, or task-local content;
- accept a release or mark a memory fact complete/current.

The existing checker remains sufficient for S5.R3. No new automation is
implemented because compact-summary correctness, purpose, sensitivity, and
continuing value require reviewable judgment.

## Exact implementation shape

### Canonical and active owners to update

- `kb/editorial_learning_framework.md`
  - expand `/about` Memory Disposition into the S5.R3 source-first flow,
    dispositions, triggers, validation, repair, compression, retirement,
    omission, auditability, Evaluation Signal interaction, and automation
    boundary;
- `kb/capability_registry.md`
  - refine existing Memory Curation and Integrity Checking only;
- `agents/chief_editor.md`
  - add materiality/disposition and material no-sync responsibilities;
- `agents/review_agent.md`
  - add exact-copy, summary semantics, privacy, context-loss, bloat, and
    non-automation challenge;
- `pipelines/review_pipeline.md`
  - extend the existing Knowledge Evolution gate, not add a gate;
- `kb/00_index.md`
  - make S5.R3 ownership discoverable;
- `ROADMAP.md`, `BACKLOG.md`, `project-state.md`
  - normalize S5.R2 accepted and represent S5.R3 RC in `Review`.

### Non-canonical implementation support

- required research, release report, Release Pack, task artifacts, and one
  ten-scenario smoke test;
- tests index entry;
- `/about` exact-copy sync for changed mapped sources;
- compact summary updates in Usage Rules, Editorial Standards, and project tree.

### Intentionally unchanged

- `AGENTS.md`: existing authority/owner map already fits;
- `kb/customer_feedback_loop.md`: feedback classification is unchanged;
- `kb/task_object_model.md`: no new state field;
- `kb/shared_lifecycle_kernel.md`: no new stage/gate;
- `kb/editorial_evidence_framework.md`: existing evidence model is sufficient;
- `kb/feedback_patterns.md`: no real recurring pattern is created;
- `templates/release-pack.md`: material memory disposition fits existing
  Scope/Non-Canonical/Evaluation/Validation sections;
- `scripts/check_about_memory_package.sh`: exact-copy/package checks are
  sufficient and must remain read-only;
- Domain Pack standard/packs: no pack behavior changes;
- `diff_intake.md` and legacy archive: forbidden/unrelated.

## Representative scenario design

| # | Scenario | Expected disposition | Owner | Critical proof |
| --- | --- | --- | --- | --- |
| 1 | Canonical role exact copy changes | `exact-copy` | Chief Editor -> Writer -> Review | byte identity; canon wins |
| 2 | Internal research report changes | `no-sync`/`omit` | Chief Editor | external facts unchanged |
| 3 | Temporary RC becomes accepted | `correct`/`compact-summary` | Chief Editor | pending state replaced, not accumulated |
| 4 | Summary has stale project status | `correct` | Chief Editor | accepted/current state restored |
| 5 | Canon and memory contradict | `correct` or `defer` if canon conflicts | Chief Editor / canonical owner | memory never overrides canon |
| 6 | Large release adds excessive detail | `compress`/`compact-summary` | Chief Editor / Writer / Review | boundaries kept, growth bounded |
| 7 | Sensitive/task-local content | `omit` | Chief Editor / Review | detail absent; useful context safe |
| 8 | No external-memory effect | `no-sync` | Chief Editor | check performed and material rationale visible |
| 9 | Duplicate memory facts | `compress`/consolidate | Chief Editor / Writer / Review | unique meaning preserved |
| 10 | Obsolete memory content | `retire` | Chief Editor / Review | active stale claim gone; repo history retained |

## Quality-attribute scenarios

### Canonical authority

When memory contradicts a canonical owner, the user must be directed by the
repository fact and the memory must be repaired or deferred; no memory-driven
owner change is permitted.

### Compactness

When a large release adds externally useful meaning plus implementation detail,
the package must retain the meaning/boundaries/source while omitting raw detail
and not adding files beyond the package contract.

### Reviewability

When a summary changes, an independent reviewer must be able to reconstruct its
canonical basis and verify material omissions, caveats, sensitivity, and
disposition without relying on chat memory.

### Safety

When task-local or sensitive information appears in a proposed summary, the
default disposition is omit; automation cannot propagate it.

### Maintainability

When duplicate or obsolete facts are found, the active package must become
smaller or clearer without erasing repository history or unique context.

## Rejected alternatives

### New Memory Hygiene capability/owner

Rejected because existing Learning Framework and capability registry already
own the behavior and roles. A new name would create governance ambiguity.

### Automatic synchronization engine

Rejected because the mission forbids automatic writes and because exact-copy
drift is only one branch; summary meaning, sensitivity, value, and retirement
need judgment.

### Mandatory sync after every commit

Rejected because most repository changes are internal or immaterial to
external memory and would create churn/bloat.

### Full repository mirror in `/about`

Rejected because it would duplicate canon, weaken context density, increase
stale surface, and violate the 20-file package purpose.

### Memory completeness/health score

Rejected because correct omission and no-sync are first-class outcomes and a
volume/coverage metric would reward bloat and false certainty.

## Architecture impact

Impact: small.

The release adds decision precision to existing owners and expands review
consequences. It does not change the stable architecture, authority hierarchy,
role set, pipelines, lifecycle, status model, task object, review gate, memory
package size, or automation authority.

## Residual risks

- Summary semantic validation remains judgment-based.
- Temporary state can still become stale if future releases ignore the trigger.
- The 20-file exact-copy checker cannot detect all contradiction, duplication,
  sensitivity, or context-loss defects.
- Optional no-sync recording can reduce audit detail; requiring it every time
  would create worse maintenance weight.
- Future evidence may justify advisory linting, but not content writes without a
  separate reviewed release.

These risks are bounded by source pointers, the disposition contract,
independent review, fixed package validation, and repository history.

## Architecture verdict

Proceed with the exact existing-owner implementation above. Do not create a
new capability, framework, owner, role, pipeline, lifecycle stage, review gate,
store, score, or synchronization engine.
