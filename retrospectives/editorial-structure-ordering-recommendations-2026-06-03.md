# Editorial Structure Ordering Recommendations

Date: 2026-06-03

Status: read-only audit note.

Scope: structure audit for the editorial system in
`/Users/sa/Documents/codex/redaction`, excluding substantive analysis of
`ai-editorial-office/tasks/TASK-*`.

Memory package note: this file is intentionally outside the current 20-file
ChatGPT project memory package. If the ChatGPT project limit remains 20 files,
do not upload this file together with the full `/about` memory package unless
another file is removed.

## Short Summary

The editorial system is mostly coherent and mature. It has a clear charter,
role separation, pipeline contracts, a task status model, a 20-file ChatGPT
memory package in `/about`, and a sync check script.

The main issue is not a broken core, but accumulated operational noise:

- duplicate policy fragments across the charter, pipelines, templates, and KB;
- frozen visual subsystem files still living in active-looking locations;
- empty or scaffold-only files that look like live knowledge;
- very large historical retrospectives that can be mistaken for active rules;
- incomplete separation between operational KB and broader editorial doctrine;
- small repository hygiene issues such as `.DS_Store` files.

The best next move is safe housekeeping first, then selective architecture
cleanup. Do not rewrite the whole system.

## Active Structure Map

| Area | Current role | Notes |
| --- | --- | --- |
| `ai-editorial-office/AGENTS.md` | Main charter | Owns invariants, authority hierarchy, role separation, review-gate, governance, artifact minimalism. |
| `ai-editorial-office/project-state.md` | Current state | Owns active phase, focus, normalization decisions, and `/about` memory package status. |
| `ai-editorial-office/agents/` | Role specs | Active core roles live here. `artist_agent.md` is present but frozen/inactive by default. |
| `ai-editorial-office/pipelines/` | Workflow contracts | Own task-type sequence, artifact depth, status movement, gates, and restart protocol. |
| `ai-editorial-office/kb/` | Operational standards | Own task statuses, tone, glossary, UX writing guidance, forbidden patterns, and editorial policy. |
| `ai-editorial-office/templates/` | Fillable artifact/task shapes | Should scaffold files, not restate policy. |
| `ai-editorial-office/scripts/` | Utility checks | Currently includes `/about` memory package sync check. |
| `ai-editorial-office/tests/` | Test location | Exists but currently has no substantive tests. |
| `editorial_knowledge/` | Editorial doctrine | Owns usefulness, modes, review philosophy, failure patterns, cases, and system reflections. |
| `about/` | ChatGPT project memory package | Contains selected copies and summaries; currently 20 canonical memory files plus this audit note. |
| `retrospectives/` | Historical archive | Useful for evolution and decisions; must not override active rules. |

## Found Disorder Zones

### Repository Noise

- `.DS_Store` files exist in active and archive areas.
- `ai-editorial-office/README.md` is empty.
- `ai-editorial-office/kb/good_examples.md` and
  `ai-editorial-office/kb/bad_examples.md` are empty.

Effect: search results and structure audits include irrelevant files; empty
files look like forgotten active knowledge.

### Placeholder Knowledge Files

- `editorial_knowledge/02_editorial_intent.md` contains headings only.
- `editorial_knowledge/03_usefulness_review.md` contains headings only.
- `editorial_knowledge/01_principles.md` has several heading-only sections.

Effect: these files look like active doctrine but do not carry enough content to
guide behavior. Later files already define much of the substance.

### System Review Inside Active Knowledge

- `editorial_knowledge/90_system_review.md` is useful, but it reads like a
  review or retrospective of the system rather than active doctrine.

Effect: future agents may treat observations and improvement ideas as active
rules.

### Frozen Visual Subsystem In Active Locations

Visual materials remain in active-looking paths:

- `ai-editorial-office/agents/artist_agent.md`;
- `ai-editorial-office/kb/canonical_sketchnote_prompt.md`;
- `ai-editorial-office/templates/artifacts/visual_concept_template.md`;
- `ai-editorial-office/templates/artifacts/illustration_brief_template.md`;
- `ai-editorial-office/templates/artifacts/sketchnote_brief_template.md`;
- `ai-editorial-office/templates/artifacts/image_prompt_template.md`;
- visual modes inside `editorial_knowledge/20_editorial_modes.md`;
- visual checks inside `editorial_knowledge/40_editorial_review_system.md`;
- visual failure pattern in `editorial_knowledge/50_editorial_failure_patterns.md`.

Effect: even though `AGENTS.md` freezes visual work by default, the active tree
still invites accidental activation.

### Duplicated Operational Rules

Some rule areas appear in several places:

- review-gate and review policy in `AGENTS.md`, `review_agent.md`,
  `review_pipeline.md`, `review_task_template.md`,
  `kb/forbidden_patterns.md`, and `editorial_knowledge/40_editorial_review_system.md`;
- artifact creation and minimalism in `AGENTS.md`, every pipeline, artifact
  templates, and task templates;
- restart/context loading in `AGENTS.md`, each pipeline, `project-state.md`,
  and `/about` summaries.

Effect: the system is safe, but verbose. Future changes may update one copy and
miss another.

### Pipeline Repetition

The five pipeline files repeat large sections:

- required artifacts;
- artifact creation policy;
- status transitions;
- handoff requirements;
- retry policy;
- completion conditions;
- restart protocol.

Effect: pipelines are self-contained and easy to run, but heavy to maintain.
Small policy changes create repeated-edit risk.

### KB vs Editorial Knowledge Boundary

The intended split is good:

- `kb/` supports operational execution;
- `editorial_knowledge/` supports editorial judgment.

But some concepts overlap:

- editorial policy vs operational rules;
- forbidden patterns vs failure patterns;
- tone/UX guidance vs usefulness dimensions;
- review expectations vs editorial review system.

Effect: agents may open both layers and receive partly overlapping guidance.

### `/about` Package Is Good But Fragile

Current state:

- `/about` contains a working ChatGPT memory package;
- copied files are checked by `check_about_memory_package.sh`;
- the script verifies file count and exact copied-file sync.

Remaining gap:

- the script does not verify whether summary files remain aligned with their
  named source files;
- adding this audit file makes `/about` contain more than 20 files, so it must
  not be treated as part of the upload set unless the package is reselected.

Effect: memory package can drift silently in summary files.

### Historical Archive Volume

`retrospectives/` contains hundreds of markdown files. It is valuable as
history but large enough to confuse context loading.

Effect: if loaded casually, historical recommendations may look like active
rules and swamp the current operating model.

## Prioritized Recommendations

### 1. Clean Repository Noise

Priority: high.

What to do:

- remove `.DS_Store` files;
- add `.DS_Store` to `.gitignore`;
- decide whether empty files should be removed, filled, or explicitly marked as
  reserved.

Files affected:

- `.DS_Store` files across active and archive folders;
- `.gitignore`;
- `ai-editorial-office/README.md`;
- `ai-editorial-office/kb/good_examples.md`;
- `ai-editorial-office/kb/bad_examples.md`.

Effect:

- cleaner search results;
- fewer false-positive active files;
- simpler audits.

Risk or side effect:

- almost none.

Can be done without behavior change:

- yes.

### 2. Add Short Index Files For Major Non-Task Areas

Priority: high.

What to do:

- add a short `README.md` or `00_index.md` to:
  - `retrospectives/`;
  - `ai-editorial-office/learn/`;
  - `ai-editorial-office/tasks/`.

Each index should say:

- what the folder is;
- whether it is active or historical;
- when to read it;
- when not to read it;
- whether files inside can define active rules.

Files affected:

- `retrospectives/README.md`;
- `ai-editorial-office/learn/README.md`;
- `ai-editorial-office/tasks/README.md`.

Effect:

- makes historical/context folders safer for ChatGPT and Codex;
- reduces accidental loading of irrelevant context;
- clarifies that `TASK-*` folders are not templates.

Risk or side effect:

- low; wording must not create new policy beyond `AGENTS.md`.

Can be done without behavior change:

- yes.

### 3. Mark Placeholder Files Explicitly

Priority: high.

What to do:

- mark scaffold-only or empty knowledge files as `placeholder`, `reserved`, or
  `retired`;
- alternatively merge their intended content into already stronger files and
  remove or archive them later.

Files affected:

- `ai-editorial-office/README.md`;
- `ai-editorial-office/kb/good_examples.md`;
- `ai-editorial-office/kb/bad_examples.md`;
- `editorial_knowledge/02_editorial_intent.md`;
- `editorial_knowledge/03_usefulness_review.md`;
- possibly `editorial_knowledge/01_principles.md`.

Effect:

- prevents agents from treating empty headings as active doctrine;
- clarifies whether examples are planned or intentionally absent.

Risk or side effect:

- low; choose labels carefully so the files do not become new rules.

Can be done without behavior change:

- yes.

### 4. Extend `/about` Validation

Priority: high.

What to do:

- extend `ai-editorial-office/scripts/check_about_memory_package.sh` to check
  that each `CHATGPT_MEMORY_*.md` summary still names existing source files;
- optionally make the script print a warning when `/about` contains non-package
  files such as this audit note.

Files affected:

- `ai-editorial-office/scripts/check_about_memory_package.sh`;
- `about/CHATGPT_MEMORY_*.md`.

Effect:

- reduces stale memory risk;
- protects the 20-file memory package from accidental expansion.

Risk or side effect:

- medium-low; script remains a check, not production behavior.

Can be done without behavior change:

- yes.

### 5. Create `editorial_knowledge/00_index.md`

Priority: medium.

What to do:

- add a compact index that classifies each file as:
  - active doctrine;
  - case/example;
  - source list;
  - system review;
  - placeholder/reserved;
  - frozen visual-related knowledge.

Files affected:

- `editorial_knowledge/00_index.md`;
- optionally placeholder files if labels are added.

Effect:

- clarifies the `kb` vs `editorial_knowledge` boundary;
- makes the doctrine layer safer to browse;
- prevents `90_system_review.md` and cases from being mistaken for policy.

Risk or side effect:

- low, if it references `AGENTS.md` authority hierarchy.

Can be done without behavior change:

- yes.

### 6. Quarantine The Frozen Visual Subsystem

Priority: medium.

What to do:

Choose one of two conservative options:

1. Leave files where they are, but add a single visual-subsystem index that
   lists all frozen visual files and repeats that they are inactive by default.
2. Move visual-only files into a clearly named frozen area, for example
   `ai-editorial-office/frozen_visual/`, and update references.

Files affected:

- `ai-editorial-office/agents/artist_agent.md`;
- visual artifact templates;
- `ai-editorial-office/kb/canonical_sketchnote_prompt.md`;
- visual sections in `editorial_knowledge/20_editorial_modes.md`,
  `40_editorial_review_system.md`, and `50_editorial_failure_patterns.md`;
- `AGENTS.md` references if files move.

Effect:

- reduces accidental visual-branch activation;
- makes ordinary text work lighter;
- keeps visual knowledge available without making it look default.

Risk or side effect:

- medium. Moving files can break references. An index-only quarantine is safer.

Can be done without behavior change:

- yes if index-only; file moves may need careful reference updates.

### 7. Reduce Pipeline Duplication Through A Shared Contract

Priority: medium.

What to do:

- create a common pipeline contract or compact shared policy file for repeated
  mechanics:
  - artifact creation policy;
  - handoff requirements;
  - restart protocol;
  - retry policy;
  - completion conditions;
  - review-gate references.
- keep task-type specifics in each pipeline.

Files affected:

- `ai-editorial-office/pipelines/*.md`;
- possibly a new `ai-editorial-office/pipelines/common_pipeline_contract.md`.

Effect:

- reduces repeated edits;
- lowers drift risk across pipelines;
- makes each task-type pipeline shorter.

Risk or side effect:

- medium. More indirection can make a pipeline less self-contained.

Can be done without behavior change:

- partially. It changes documentation shape, not intended behavior, but must be
  reviewed carefully.

### 8. Slim `AGENTS.md` In A Controlled Pass

Priority: medium.

What to do:

- keep `AGENTS.md` as charter and authority owner;
- remove or compress material that is now owned in more specific files;
- avoid changing invariants, review-gate, role separation, or authority order.

Files affected:

- `ai-editorial-office/AGENTS.md`;
- possibly `agents/`, `pipelines/`, and `kb/` if references need adjustment.

Effect:

- easier startup context;
- fewer repeated rules;
- clearer separation of charter vs manuals.

Risk or side effect:

- medium-high. `AGENTS.md` is the safety spine; over-compression can lose useful
  guardrails.

Can be done without behavior change:

- only with careful review.

### 9. Give `tests/` A Real Purpose

Priority: low.

What to do:

- add a smoke test for the memory package script;
- document whether `tests/` is for shell checks, markdown lint, or future
  workflow checks.

Files affected:

- `ai-editorial-office/tests/`;
- `ai-editorial-office/scripts/check_about_memory_package.sh`.

Effect:

- makes the existing empty tests folder meaningful;
- gives future maintenance a safe place for checks.

Risk or side effect:

- low.

Can be done without behavior change:

- yes.

### 10. Reconsider `/about` Composition Later

Priority: low.

What to do:

- consider replacing full pipeline copies in `/about` with a pipeline summary
  file if ChatGPT context becomes too heavy;
- keep canonical pipeline files in `ai-editorial-office/pipelines/`.

Files affected:

- `/about`;
- `check_about_memory_package.sh`;
- possibly `project-state.md`.

Effect:

- smaller ChatGPT project memory;
- less chance that copied full files drift.

Risk or side effect:

- medium. ChatGPT may lose useful operational detail unless summaries are very
  good.

Can be done without behavior change:

- yes, if canonical files remain untouched.

## Quick Safe Cleanup Package

Recommended first batch:

1. Remove `.DS_Store` files and add `.DS_Store` to `.gitignore`.
2. Add short index files to `retrospectives/`, `learn/`, and `tasks/`.
3. Mark empty or scaffold-only files as `placeholder`, `reserved`, or
   `retired`.
4. Extend `/about` validation to protect the 20-file memory package.
5. Add `editorial_knowledge/00_index.md`.

Expected effect:

- cleaner file discovery;
- less false active context;
- safer ChatGPT/Codex navigation;
- no change to editorial behavior.

## More Serious Architecture Decisions

Do later, one at a time:

1. Decide how to quarantine the frozen visual subsystem.
2. Decide whether repeated pipeline mechanics should move into a common
   contract.
3. Decide whether `AGENTS.md` should be slimmed after common ownership is more
   stable.
4. Decide whether `/about` should keep full pipeline copies or switch to a more
   compressed summary package.

## What Not To Touch Yet

- Do not analyze or reorganize `ai-editorial-office/tasks/TASK-*`.
- Do not rewrite all pipelines at once.
- Do not add new active roles.
- Do not activate the visual subsystem.
- Do not delete retrospectives.
- Do not change review-gate, task status model, role separation, or final
  governance.
- Do not treat historical recommendations as active rules.

## Suggested Order Of Work

1. Safe cleanup: `.DS_Store`, `.gitignore`, index files, placeholder labels.
2. Memory safety: improve `/about` validation and document non-package files.
3. Knowledge clarity: add `editorial_knowledge/00_index.md`.
4. Visual clarity: add an index-only quarantine for frozen visual files.
5. Maintenance reduction: evaluate common pipeline contract.
6. Context reduction: only then consider slimming `AGENTS.md` and `/about`.

