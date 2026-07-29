# Repository Product-Surface Audit

## Executive Verdict

**Verdict: Unsafe or unsuitable for publication as a public/product repository.**

As a private working repository, the checkout is a functioning development and governance worktree. As a GitHub product surface, it is not ready: normal users encounter a development-history repository with a weak entry point, while task histories, client-profile material classes, local-path references, release evidence, research records, and retrospectives remain visible alongside the operating core.

The repository should not be cleaned by deleting history wholesale. The safe direction is to define the user operating layer, extract a sanitized example set, preserve valuable history in a controlled private archive, remove active/local work from the product repository, and then simplify the visible tree through several bounded releases.

Finding counts:

| Severity | Count |
| --- | ---: |
| High | 4 |
| Medium | 7 |
| Low | 3 |
| Observation | 2 |

Evidence confidence:

- `verified` for branch state, divergence, tracked counts, path classifications, current ignore behavior, and sampled directory roles;
- `supported` for future disposition recommendations because the user operating layer and public/private repository policy still require Project Lead decisions;
- `unsupported` as a publication clearance: this mission did not perform exhaustive content, rights, PII, credential-history, or legal review.

## Repository State

Audit baseline after `git fetch origin` on 2026-07-10:

- Local branch: `main` at `51166c6` (`Close Stage 5 editorial intelligence`).
- Refreshed `origin/main`: `1e45c52` (`Close S5.R5 publication state`).
- Divergence: `0 2` for `origin/main...main`; origin has no commit absent locally, and local `main` is two commits ahead.
- Local tracked files: 1,683.
- `origin/main` tracked files: 1,668.
- Local tracked difference from GitHub: 19 paths, comprising 4 modified paths and 15 added paths.
- GitHub contains no tracked file absent from local `main`, because `origin/main` is an ancestor of local `main`.
- Baseline worktree had no modified or staged tracked file.
- Baseline untracked state contained seven files represented by four status entries: one Project v1 release pack, one Project v1 strategic review, four Project v1 task-control files, and `diff_intake.md`.
- The pre-existing untracked Project v1 material and `diff_intake.md` were excluded from product-state conclusions and left untouched.
- Ignored local state includes OS metadata, local source/reference binaries, task inputs, and generated task outputs. Those files are not GitHub-visible, but their material classes remain relevant to future `.gitignore` and local-workspace design.

Current tree counts on local `main`:

| Area | Tracked files | Approximate tracked bytes | Current GitHub/product implication |
| --- | ---: | ---: | --- |
| `ai-editorial-office/tasks/` | 948 | 7,267,693 | Largest visible area; mixes working, legacy, maintenance, release, and governance traces. |
| `retrospectives/` | 380 | 949,407 | Historical system-development evidence prominent at root. |
| `ai-editorial-office/tests/` | 155 | 240,177 | Useful infrastructure and sanitized evidence, but several content types are mixed. |
| `ai-editorial-office/research/` | 51 | 919,146 | Primarily capability/release/stage development evidence. |
| `about/` | 20 | 434,253 | Derived ChatGPT memory package, including 15 exact copies. |
| `ai-editorial-office/kb/` | 43 | 675,577 | Canonical and reusable product knowledge, with a sensitive client-profile subarea. |
| `editorial_knowledge/` | 15 | 132,038 | Reusable editorial judgment plus cases and placeholders, separated from the main product directory. |
| `ai-editorial-office/releases/` | 13 | 146,930 | Release-governance evidence. |

`tasks/` and `retrospectives/` together account for 1,328 of 1,683 tracked files, about 79% of the current tree by file count. This is the clearest structural signal that GitHub currently presents the development worktree rather than the product.

Current security/path checks found no strong private-key, common cloud-key, GitHub-token, or OpenAI-key marker in tracked `HEAD` text. That is a narrow negative check, not a security clearance. Machine-specific absolute-path patterns occur across root/service material and many task/history files. Email-like patterns occur in a small number of tracked files. Details are intentionally omitted; all matched material classes require manual review before public publication.

Reachable `origin/main` history contains no object path with the audited binary/media extensions, but it contains 1,028 path-bearing objects under the task-history namespace and six under the client-profile namespace. Removing those paths from the current tree would not remove their prior GitHub history.

Audit limitations:

- GitHub repository visibility setting was not used as evidence; the audit evaluates suitability for a public/product surface regardless of current visibility.
- Sensitive file contents are not reproduced here.
- The mission sampled task, research, release, test, planning, memory, and retrospective material; it did not content-review all 1,683 tracked files.
- No full Git-history secret, PII, copyright, or source-rights scan was performed.
- Untracked Project v1 work may supersede planning state later, but it was intentionally excluded from this audit.

## Intended Product Surface

A normal user should encounter a small, deliberate path:

1. Understand what AI Editorial Office is and what it is not.
2. Choose how to operate it: Codex, ChatGPT, or repository-first/local use.
3. Start a task from a natural-language request or template.
4. Know where local inputs and outputs live and what Git will not publish.
5. Understand progress, review, recovery, and final-output locations.
6. Inspect one or two sanitized end-to-end examples.
7. Reach deeper role, pipeline, KB, validation, and maintainer material only when needed.

The minimum coherent operating surface is therefore:

- one product `README.md` with prerequisites, quick start, operating modes, first task, output path, privacy boundary, and next links;
- user guides for Codex, ChatGPT, task creation, task progress/recovery, outputs, and local/private material;
- the canonical operating core: `AGENTS.md`, `ai-editorial-office/AGENTS.md`, role specs, pipelines, generic KB, templates, and current project state;
- a local task workspace whose contents are ignored by default;
- a sanitized example set separate from production task traces;
- maintainers' scripts, tests, contribution rules, planning, and release procedure in a clearly labeled maintainer area;
- a generated or explicitly packaged ChatGPT integration, not an unexplained second copy of canon;
- no real client profile, source library, production task, generated task output, or personal/local maintenance note in the default product repository.

What a normal user must see:

- root `README.md`;
- quick start and operating-mode choice;
- task input/output/recovery guide;
- privacy/publication boundary;
- sanitized examples;
- link to the canonical system charter only when deeper behavior matters.

What Codex or maintainers need, but a normal user does not need at the front door:

- root and editorial `AGENTS.md` files;
- `agents/`, `pipelines/`, most `kb/`, `templates/`, `scripts/`, and automated fixtures;
- `project-state.md`, roadmap, backlog, release procedure, validator instructions, contribution policy, and historical decision evidence.

Canonical files that must remain easy for Codex and maintainers to discover:

- `AGENTS.md`;
- `ai-editorial-office/AGENTS.md`;
- `ai-editorial-office/project-state.md`;
- canonical KB owners named by the charter;
- active role and pipeline files;
- task/status/object/capability/lifecycle owners;
- reusable templates.

“Easy to discover” does not require putting every canonical file at root. A short technical index can route Codex and maintainers without exposing the entire development history as product navigation.

## Current Structure Assessment

### Root

The root contains a plausible product name but behaves as a publication-preflight and migration workspace. `README.md` describes a local project and publication restrictions, not how to use the product. `CANONICAL_REPOSITORY.md` records machine-specific migration state. Multiple export and publishing audits occupy the highest-visibility level even though they are historical and no longer describe the tracked tree accurately.

`AGENTS.md` and `.gitignore` are appropriate root infrastructure. `CONTRIBUTING.md` is useful maintainer material, but its safe-core publication claims conflict with the current tracked task and client-profile surface.

### `ai-editorial-office/`

This is the real product core, but its own `README.md` is a reserved placeholder. The directory has strong canonical architecture and a mature operating model, yet no usable navigation for a new user. Its root mixes canon, state, roadmap/backlog management, operating components, local workspaces, tests, development research, and release evidence.

### `ai-editorial-office/agents/`, `pipelines/`, `kb/`, and `templates/`

These are the strongest Core Product areas. They define role accountability, lifecycle overlays, canonical knowledge, reusable capabilities, and task scaffolds. They should remain versioned and discoverable for Codex and maintainers.

The generic KB is product content. `kb/clients/` is not generic product content: it is a client-specific overlay and belongs behind a local/private boundary. `kb/sources/README.md` is useful as a tracked contract, while actual source materials should stay local-only.

### `ai-editorial-office/tasks/`

The directory contains 93 tracked task folders and 948 tracked files on local `main`; only 81 tracked task manifests exist, confirming a mix of current-model tasks and legacy/irregular history. Samples show at least these distinct classes:

- real editorial working traces;
- legacy tasks that predate the current manifest model;
- system-maintenance tasks;
- release and stage-closure tasks;
- research/governance tasks;
- generated or source-derived task artifacts;
- task folders with non-canonical naming and version patterns.

The directory is operationally necessary as a local workspace, but the full history is not necessary to operate the product. Its evidence value should be preserved through a small sanitized example set and, where needed, a controlled private archive. Production task contents should be ignored by default.

### `ai-editorial-office/research/`

The 51 tracked files are primarily capability landscapes, architecture syntheses, release reports, and stage reviews. Samples confirm that they are source-backed and useful for provenance, but their principal value is development traceability rather than normal product operation. They should not be deleted wholesale. Accepted evidence should move to a private/history surface or a bounded public design-history set, with a concise index from maintainers' documentation.

The untracked Project v1 strategic review was not inspected or classified as current product state.

### `ai-editorial-office/releases/`

The 13 tracked release packs are valuable acceptance and governance evidence. They are not needed for normal user operation. Keep a compact release history if public provenance is a product value; otherwise move full packs to the controlled history archive and expose only a changelog or release notes in the product repository.

The untracked Project v1 release pack was excluded.

### `ai-editorial-office/tests/`

This area has clear product-evidence value: automated shell checks, 92 synthetic fixtures, 34 sanitized end-to-end case files, and manual smoke tests. The sanitized end-to-end cases are a better basis for product examples than raw task history.

The current directory mixes executable tests, fixtures, manual trials, decision notes, examples, and client-specific activation tests. Split user examples from maintainer tests. Client-specific test material requires a separate publication decision or generic replacement.

### `ai-editorial-office/scripts/`

The scripts and their README are Maintainer/Codex Infrastructure. They validate lifecycle, prepare read-only task packs, and check the ChatGPT memory package. Keep them tracked, but introduce them through maintainer and integration documentation rather than the main user path.

### `ai-editorial-office/ideas/`

`engineering_watchlist.md` is a useful maintainer observation log. `master_backlog.md` is a large development chronicle that still describes itself as active and names a next step from an earlier development phase. It overlaps with the newer `BACKLOG.md` Project Lead release plan and contributes to conflicting planning entry points.

### Planning and state files

- `ROADMAP.md` is the strategic direction surface, but it contains mixed current/completed stage framing and should be normalized only in a separate planning decision.
- `BACKLOG.md` is the current Project Lead operational release plan.
- `ideas/master_backlog.md` is an older backlog/retrospective hybrid and should cease being an active planning owner.
- `project-state.md` is canonical current system state for Codex and must remain stable and discoverable during cleanup.
- Stage reviews and release packs are evidence, not current planning owners.

The target should have one strategy owner, one active execution backlog, one current-state owner, and one clearly historical archive/index.

### `/about`

`about/` is a 20-file non-canonical ChatGPT memory package. The checker proves that 15 files are byte-identical copies of canonical sources; the remaining five are memory summaries/instructions. The package is useful for ChatGPT onboarding, but its current form duplicates approximately 434 KB of tracked content and creates a manual synchronization obligation.

Recommended product role: ChatGPT integration output, not active canon and not a second product tree. Keep it tracked only until a reproducible replacement exists. The target should store a manifest, usage guide, and generator/sync mechanism; generated package output should be local or a release artifact. Do not untrack `/about` before the replacement is usable and validated.

### `editorial_knowledge/`

This area contains reusable editorial judgment and cases, but it sits outside the main product directory and includes placeholder/scaffold files and at least one organization-specific case class requiring manual review. Its active knowledge should remain, but its ownership and location should be consolidated deliberately. A move into `ai-editorial-office/editorial_knowledge/` is reasonable only as a bounded canonical-reference migration.

### `retrospectives/`

All 380 files are explicitly historical. They preserve useful development reasoning but are not product operation. Their root prominence, detailed implementation traces, and volume make the repository look like an engineering notebook. Move them to controlled history storage and keep only a compact maintainer history index in the active product repository.

### Local/ignored areas

Ignored local source/reference files under `learn/`, `kb/sources/`, and task folders are correctly outside the current Git tree. They may still carry client, personal, source-rights, or internal risk and should stay local-only. `.DS_Store` is correctly ignored. `diff_intake.md` is untracked but not ignored and remains a recurring accidental-publication risk.

## Classification Inventory

### Root-level inventory

| Path or area | Classification | Product-surface disposition |
| --- | --- | --- |
| `README.md` | B — User-Facing Product Surface | Keep path; replace content with the real product entry and quick start. |
| `AGENTS.md` | A — Core Product | Keep tracked and easy for Codex to discover; not a normal-user start page. |
| `.gitignore` | C — Maintainer / Codex Infrastructure | Keep and strengthen with path-scoped local-work rules. |
| `CONTRIBUTING.md` | C — Maintainer / Codex Infrastructure | Keep but reposition under maintainer docs after fixing publication-boundary claims. |
| `CANONICAL_REPOSITORY.md` | G — Obsolete / Duplicate / Misleading | Migration/local-path record; archive or remove from active root after its remaining purpose is resolved. |
| `GITHUB_PUBLISHING_CHECKLIST.md` | C — Maintainer / Codex Infrastructure | Consolidate into one current publishing/security guide. |
| `PUBLISHING_AUDIT.md`, `PUBLICATION_SCOPE_PROPOSAL.md`, `EXPORT_*.md` | E — Development History | Move together to dated history; they are stale as active root guidance. |
| `about/` | C/G — Integration Infrastructure / Derived Duplicate | Replace with source manifest plus generated/local package; do not treat as canon. |
| `ai-editorial-office/` | Mixed; expanded below | Retain as operating core, but separate product, workspace, maintainer, and history surfaces. |
| `editorial_knowledge/` | A/G — Core Knowledge / Mispositioned | Keep active knowledge; consolidate location and review cases/placeholders. |
| `retrospectives/` | E — Development History | Preserve in controlled private history, remove from active product tree. |
| Ignored OS/source/generated files | F — Local-Only Or Sensitive | Keep local-only; do not publish. |
| `diff_intake.md` | F — Local-Only Or Sensitive | Leave untouched; add exact future ignore rule. |

### `ai-editorial-office/` inventory

| Path or area | Classification | Product-surface disposition |
| --- | --- | --- |
| `AGENTS.md` | A — Core Product | Keep as canonical operating charter. |
| `README.md` | B/G — User Surface / False Entry | Replace reserved placeholder with a technical product index. |
| `project-state.md` | A/C — Core State / Codex Infrastructure | Keep at current canonical path during initial cleanup. |
| `agents/` | A — Core Product | Keep tracked. |
| `pipelines/` | A — Core Product | Keep tracked. |
| Generic `kb/*.md` | A — Core Product | Keep tracked; preserve canonical ownership. |
| `kb/clients/` | F — Local-Only Or Sensitive | Remove client profiles from the generic product repository; retain only a generic profile contract/example if approved. |
| `kb/sources/README.md` | B/C — User Contract / Infrastructure | Keep README; ignore actual source-library contents. |
| `templates/` | A — Core Product | Keep tracked; review visual/frozen templates only for navigation clarity. |
| `tasks/README.md` | B — User-Facing Product Surface | Keep tracked as the local workspace contract. |
| Other `tasks/` contents | F/E — Local/Sensitive or Development History | Active work local-only; preserve selected history privately; publish only sanitized examples moved elsewhere. |
| `research/` | E — Development History | Archive release/stage research; keep only current product research explicitly selected for public design history. |
| `releases/` | E/D — Development History / Product Evidence | Move full governance packs to controlled history or retain a small public release-notes subset. |
| `tests/` executable checks and fixtures | C — Maintainer / Codex Infrastructure | Keep tracked. |
| `tests/end_to_end_cases/` | D — Product Evidence | Reposition as sanitized `examples/` with tests referencing it where useful. |
| Other manual smoke tests/trials | C/D — Infrastructure / Product Evidence | Keep only current tests; archive obsolete decision notes and review client-specific cases. |
| `scripts/` | C — Maintainer / Codex Infrastructure | Keep tracked. |
| `ROADMAP.md`, `BACKLOG.md` | C — Maintainer / Product Management | Keep as the strategy and active execution owners; reposition in maintainer navigation. |
| `ideas/engineering_watchlist.md` | C — Maintainer Infrastructure | Keep as maintainer evidence, not user navigation. |
| `ideas/master_backlog.md` | E/G — Development History / Duplicate Planning | Consolidate current items into `BACKLOG.md`, then archive. |
| `learn/README.md` | B/C — Local Workspace Contract | Keep tracked; keep source/reference contents ignored and local-only. |
| Tracked task-local SVG/CSV/HTML/TXT artifacts | F/G — Local/Generated or Misleading | Remove from product Git after archive/review; sanitized examples belong in `examples/`. |

## Findings

| ID | Severity | Path or area | Current role | Problem | Recommended disposition | User impact | Risk of change | Requires Project Lead decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RPS-001 | High | `ai-editorial-office/tasks/` | Active and historical task workspace | 948 tracked files across 93 task folders mix real work, legacy traces, system maintenance, releases, sources, and generated artifacts. Full task history is neither required nor safe as the default product surface. | Keep `tasks/README.md`; make task contents local-only by default; extract a small sanitized example set; archive selected history privately after review. | Reduces privacy risk and makes first use understandable. | High: evidence or active work can be lost if untracked before archive and verification. | Yes |
| RPS-002 | High | `kb/clients/`, task/history classes, root/local-path references | Client overlay and internal context | Client-specific profiles, machine-specific paths, and a small number of email-like patterns are tracked. No strong credential marker was found, but that is not a content/security clearance. | Freeze public publication; perform manual PII/client/source-rights/security review by path class; separate private profiles and local context from the generic product. | Prevents accidental client/internal disclosure. | High: careless redaction can break client-mode contracts or hide provenance. | Yes |
| RPS-003 | High | Reachable `origin/main` history | Published development history | Current-tree removal will not remove previously pushed task/client paths. Origin history contains substantial path-bearing task history. | Decide whether the current remote remains private/internal, receives an approved history rewrite, or is replaced by a clean product repository. Preserve a verified private archive first. | Determines whether future “clean” GitHub state is actually publication-safe. | Very high: history rewriting changes commit identities and collaborator state. | Yes |
| RPS-004 | High | `README.md`, `ai-editorial-office/README.md` | Product entry points | Root README is a development/publication warning, while the product README is a reserved placeholder. There is no clear first-task, Codex, ChatGPT, output, privacy, or recovery path. | Design and add the user operating layer before removing old navigation. | Without it, users cannot understand or operate the product from GitHub. | Medium: premature documentation can freeze the wrong operating model. | Yes |
| RPS-005 | Medium | `tasks/`, `retrospectives/`, `research/`, `releases/` | Evidence and history | Development history dominates about 79% of tracked files and overwhelms core product components. | Move full history to controlled archive storage; retain only selected changelog, accepted examples, and concise provenance indexes. | Makes the repository read as a product instead of a worktree. | Medium: links and historical references can break without an inventory and redirect/index. | Yes |
| RPS-006 | Medium | `about/` | ChatGPT memory package | Fifteen exact copies plus five summaries duplicate canon, add 434 KB, and require manual synchronization. | Keep until replacement exists; then track a ChatGPT integration manifest/guide/generator and keep generated output local or release-scoped. | Preserves ChatGPT usability while removing a false second product tree. | Medium: removing copies too early breaks the current memory workflow. | Yes |
| RPS-007 | Medium | `ROADMAP.md`, `BACKLOG.md`, `ideas/master_backlog.md`, stage reviews, `project-state.md` | Planning and state | Multiple documents claim or imply active planning roles; older backlog material and mixed stage framing create duplicate or stale next steps. | Confirm one strategy owner, one active backlog, one current-state owner, and one historical index; archive the old master backlog after consolidation. | Users and maintainers see one current direction. | Medium: wrong consolidation can erase open decisions or change canonical state. | Yes |
| RPS-008 | Medium | Root export/publishing documents and `CONTRIBUTING.md` | Publication history and guidance | Historical audits describe an older inventory and safe-core export, while the current tree tracks the areas those documents say to exclude. | Archive dated audits together; replace them with one current maintainer publication/security guide; update contribution claims. | Removes contradictory safety signals. | Low to medium: historical evidence must remain available for provenance. | No |
| RPS-009 | Medium | `tests/` | Tests, evidence, examples, and decision notes | Executable checks, fixtures, manual trials, sanitized examples, and client-specific checks are mixed in one directory. | Keep automated tests/fixtures; move sanitized end-to-end cases to `examples/`; archive obsolete decision notes; review client-specific tests. | Users get clear examples and maintainers get a clearer test suite. | Medium: tests may rely on current paths. | No |
| RPS-010 | Medium | `.gitignore`, `tasks/`, `learn/`, `kb/sources/`, `kb/clients/`, `about/` | Local publication boundary | Extension-based ignores protect binaries but do not make task, client, source, or memory-output directories local-only. `diff_intake.md` remains unignored. Broad binary ignores also prevent intentional product assets anywhere. | Add path-scoped rules after archive decisions; keep tracked README/contracts via negation; narrow global asset rules if product assets become intentional. | Reduces accidental commits without blocking deliberate product assets. | Medium: ignore rules do not affect already tracked files and can hide intended changes. | Yes |
| RPS-011 | Medium | `editorial_knowledge/` | Reusable product knowledge | Active knowledge is outside the main product directory and mixed with placeholders and case material requiring review. | Preserve active knowledge; review cases; remove or fill placeholders; migrate location only through a bounded canonical-reference release. | Makes knowledge ownership and navigation clearer. | Medium: moving it changes many references and memory summaries. | Yes |
| RPS-012 | Low | `CANONICAL_REPOSITORY.md` and machine-specific root state | Migration/maintenance note | A local migration record and absolute paths are prominent in the product root and can become stale or disclose irrelevant workstation structure. | Archive or replace with repository-relative maintainer guidance after migration is fully closed. | Cleaner, portable product surface. | Low: ensure no active bootstrap depends on the file. | No |
| RPS-013 | Low | Tracked non-Markdown task artifacts and irregular task names | Generated/source evidence | A small set of SVG, CSV, HTML, TXT, and irregularly named task files reinforces worktree noise and may create false examples. | Move to private task archive or sanitized examples; do not clean individually before task-level disposition. | Reduces false entry points and generated-file clutter. | Low when archived as a unit; higher if edited selectively. | No |
| RPS-014 | Low | Reserved/scaffold-only knowledge and example files | Placeholders | Reserved or empty example/case scaffolds look like usable product content but provide no value. | Either populate with approved sanitized examples or remove after confirming no template/reference dependency. | Reduces dead ends. | Low. | No |
| RPS-015 | Observation | Local `main` versus `origin/main` | Synchronization state | Local is ahead by two commits; GitHub lacks the Stage 5 closure commit set and 15 locally tracked additions. Pre-existing Project v1 work is untracked. | Treat local `main` as the richer audit baseline but do not call GitHub synchronized; publish nothing under this mission. | Prevents a false claim that GitHub already shows the current local product state. | None in this mission. | No |
| RPS-016 | Observation | Current and historical binary path scan | Positive publication signal | No audited binary/media extension appears in reachable `origin/main` object paths, and current local binaries are ignored. This does not clear text content, source rights, or ignored local materials. | Preserve the binary boundary; add scoped local-work rules and manual content review. | Narrows, but does not eliminate, publication risk. | Low. | No |

## Proposed Target Structure

Recommended future product repository:

```text
/
├── README.md                         # product entry and quick start
├── AGENTS.md                         # Codex bootstrap
├── .gitignore
├── docs/
│   ├── quickstart.md
│   ├── operating-model.md
│   ├── use-with-codex.md
│   ├── use-with-chatgpt.md
│   ├── tasks-progress-and-recovery.md
│   ├── outputs-and-privacy.md
│   └── maintainers/
│       ├── contributing.md
│       ├── roadmap.md
│       ├── backlog.md
│       ├── publishing-and-security.md
│       └── history-index.md
├── ai-editorial-office/
│   ├── README.md                     # technical index, not duplicate policy
│   ├── AGENTS.md
│   ├── project-state.md
│   ├── agents/
│   ├── pipelines/
│   ├── kb/
│   │   ├── 00_index.md
│   │   ├── ... generic canonical knowledge ...
│   │   ├── clients/
│   │   │   └── README.md             # contract only; real profiles local/private
│   │   └── sources/
│   │       └── README.md             # contract only; sources local/private
│   ├── editorial_knowledge/          # after bounded owner/reference migration
│   ├── templates/
│   ├── tasks/
│   │   └── README.md                 # task contents local and ignored
│   ├── learn/
│   │   └── README.md                 # library contents local and ignored
│   ├── scripts/
│   └── tests/                        # executable tests and fixtures
├── examples/
│   ├── README.md
│   └── sanitized-end-to-end/
└── integrations/
    └── chatgpt/
        ├── README.md
        ├── memory-manifest.md
        └── generate-or-sync-package.*
```

Controlled private companion archive or storage, outside the active product repository:

```text
ai-editorial-office-history/
├── tasks/
├── system-maintenance/
├── release-task-traces/
├── research/
├── releases/
├── retrospectives/
├── client-profiles/
└── source-library/
```

The exact archive technology—private repository, encrypted storage, internal document store, or local-only archive—requires a Project Lead decision. A public `archive/` directory inside the same repository is not sufficient for sensitive task/client history.

## Proposed Changes

### Keep As-Is

- Root `AGENTS.md`.
- `ai-editorial-office/AGENTS.md`.
- `ai-editorial-office/agents/`.
- `ai-editorial-office/pipelines/`.
- Generic canonical `ai-editorial-office/kb/*.md` files.
- `ai-editorial-office/templates/`, subject to normal future product QA.
- `ai-editorial-office/project-state.md` at its canonical path during initial cleanup.
- Automated scripts and executable validator tests/fixtures.
- `ai-editorial-office/tasks/README.md`, `learn/README.md`, and `kb/sources/README.md` as local-workspace contracts.

### Keep But Reposition Or Rename

- Replace root `README.md` content with the product entry; turn `ai-editorial-office/README.md` into the technical index.
- Move `CONTRIBUTING.md`, `ROADMAP.md`, `BACKLOG.md`, publishing guidance, and maintainer navigation under a clearly labeled maintainer surface, with references updated atomically.
- Move sanitized `tests/end_to_end_cases/` into top-level `examples/` or expose it there through a deliberate product-example index.
- Move active `editorial_knowledge/` under the product directory only after a bounded canonical-reference migration.
- Replace tracked `/about` output with an `integrations/chatgpt/` source/manifest/generator surface after parity is proven.

### Consolidate

- Consolidate the active planning model to `ROADMAP.md` + `BACKLOG.md` + `project-state.md`; retire `ideas/master_backlog.md` as an active owner.
- Consolidate root publishing/export instructions into one current maintainer guide.
- Consolidate product onboarding across one root README plus task/Codex/ChatGPT/recovery guides, without copying canonical rules.
- Consolidate placeholders and examples so each example is either usable, explicitly reserved, or removed.

### Move To Archive

- Root export/publication audits and manifests as one dated publication-history package.
- `retrospectives/`.
- Capability/release/stage development records in `ai-editorial-office/research/`.
- Full release packs in `ai-editorial-office/releases/`, unless a small public release-evidence subset is intentionally retained.
- System-maintenance and release task traces after security review.
- `ideas/master_backlog.md` after current items and unresolved decisions are reconciled.
- `CANONICAL_REPOSITORY.md` after its remaining migration purpose is closed.

### Keep Locally But Remove From Git

- Active and ordinary production task contents under `ai-editorial-office/tasks/`.
- Real client profiles under `ai-editorial-office/kb/clients/`.
- Source/reference libraries under `ai-editorial-office/learn/` and `ai-editorial-office/kb/sources/`.
- Generated task outputs and source-derived task artifacts.
- `diff_intake.md`.
- Generated ChatGPT memory-package output after a replacement integration is proven.

Previously committed sensitive classes must first be copied to approved private storage and reviewed for Git-history consequences. “Remove from Git” here means remove from the active product tree; it does not imply silent history deletion.

### Remove As Obsolete Or Duplicate

- Reserved placeholder content that has no downstream consumer, after reference checks.
- Stale root publication guidance after archival and replacement.
- Duplicate active-planning claims in `ideas/master_backlog.md` after consolidation.
- Machine-specific migration guidance after repository-relative documentation replaces it.
- Duplicate `/about` exact copies after generated packaging is available.

### Add To `.gitignore`

Recommended future path-scoped rules, only after the relevant tracked files are archived and intentionally untracked:

```gitignore
/diff_intake.md

/ai-editorial-office/tasks/**
!/ai-editorial-office/tasks/README.md

/ai-editorial-office/learn/**
!/ai-editorial-office/learn/README.md

/ai-editorial-office/kb/sources/**
!/ai-editorial-office/kb/sources/README.md

/ai-editorial-office/kb/clients/**
!/ai-editorial-office/kb/clients/README.md

# Add only after generated ChatGPT packaging replaces tracked /about output.
/about/**
```

Also consider standard Python/tool noise if those tools become part of normal operation:

```gitignore
.venv/
venv/
.pytest_cache/
.mypy_cache/
.ruff_cache/
*.py[cod]
```

Do not rely on `.gitignore` to remove tracked files or clean history. Review the current global binary ignore list when the product intentionally adds screenshots, diagrams, or other versioned assets; path-scoped workspace rules are safer than forbidding all product media everywhere.

### Requires Manual Content/Security Review

- All current and historical `ai-editorial-office/tasks/` material.
- `ai-editorial-office/kb/clients/` and client-specific tests/references.
- Organization- or client-specific cases under `editorial_knowledge/`.
- Root and historical files containing machine-specific paths or email-like patterns.
- `retrospectives/`, release research, and system-maintenance traces that may reproduce internal decisions or task context.
- Ignored local source/reference libraries and task inputs/outputs.
- Reachable GitHub history, including removed or renamed task/client paths.
- Source rights and redistribution rights for any artifact proposed as a public example.

## Migration Order

Each future step should be a separate, reviewable, reversible release or decision packet.

1. **Freeze the publication boundary.** Record that the current repository is not approved for public/product publication. Do not rewrite history or untrack files yet.
2. **Approve the target operating contract.** Decide the user journeys for repository, Codex, and ChatGPT; confirm the product repository versus private-history/private-workspace split.
3. **Run dedicated security and rights review.** Inventory current and historical task, client, source, PII, secret, local-path, and licensing classes. Decide whether the existing remote may remain private, needs history remediation, or should be replaced by a clean product repository.
4. **Add replacement onboarding first.** Create and review the root product README, quick start, task/progress/recovery guide, privacy guide, and Codex/ChatGPT entry guides. Do not remove old entry material until replacement navigation works in a clean clone.
5. **Create the sanitized example set.** Promote only approved synthetic/end-to-end evidence into `examples/`; verify no real task/source/client data is present.
6. **Create and verify the private archive.** Copy task history, system-maintenance traces, research, releases, retrospectives, client profiles, and source libraries to the approved archive. Record inventory/checksums or another repeatable completeness check before removing anything from the product tree.
7. **Separate local work from Git.** In one bounded release, untrack approved task/client/source/generated classes and add path-scoped ignore rules. Keep tracked README/contracts and sanitized examples.
8. **Consolidate planning and maintainer material.** Reconcile `ROADMAP.md`, `BACKLOG.md`, `project-state.md`, and unresolved master-backlog items; archive stale planning and root publication documents.
9. **Replace `/about` safely.** Build and validate the ChatGPT package manifest/generator, prove parity and usability, then untrack generated copies and add the final ignore rule.
10. **Consolidate knowledge location.** If approved, migrate `editorial_knowledge/` with reference updates and review; remove or populate placeholders separately.
11. **Simplify the root.** Leave only product entry, Codex bootstrap, ignore rules, product directory, user docs, examples, and integrations. Run link, lifecycle, memory-package replacement, tests, clean-clone, and publication-boundary checks.
12. **Address Git history only by explicit decision.** If public publication is intended, use a dedicated, backed-up history-remediation or clean-repository release. Never mix history rewriting with product-structure moves.

## Do Not Touch List

During the initial product-surface cleanup release, do not modify:

- root `AGENTS.md` or `ai-editorial-office/AGENTS.md`;
- role, pipeline, review-gate, task-status, task-object, shared-lifecycle, capability-registry, evidence, or canonical-owner rules;
- `ai-editorial-office/project-state.md` until replacement navigation and reference impacts are approved;
- accepted domain packs and professional capability owners;
- active or historical task contents before archive/security disposition is approved;
- `about/` before a validated replacement exists;
- client-profile contents through ad hoc redaction or generalization;
- Git history, tags, or commit identities;
- the pre-existing untracked Project v1 release/research/task material;
- `diff_intake.md`;
- `/Users/sa/Documents/codex/redaction`.

## Open Decisions For Project Lead

1. Is the product repository intended to be public, private but shareable, or private/internal only?
2. Should task history live in a separate private repository, encrypted archive, internal store, or local-only storage?
3. Should the existing GitHub repository/history be retained as private development provenance, remediated, or replaced by a clean product repository?
4. Which release packs, strategic reviews, and retrospectives provide enough public value to justify a curated history subset?
5. Should real client profiles remain supported only as local overlays, or live in a separate private extension repository?
6. Is `/about` a distributed product artifact, a generated release asset, or a local ChatGPT integration output?
7. Which planning file is the single active backlog owner after Project v1.0 acceptance, and how should unresolved `master_backlog.md` items be reconciled?
8. Should `editorial_knowledge/` remain a separate root canonical area or move into the product directory through a dedicated owner/reference migration?

## Final Recommendation

Perform cleanup as **several bounded releases**.

Do not attempt a one-release sweep: security boundary, user operating layer, archive preservation, task untracking, planning consolidation, `/about` replacement, knowledge migration, and possible Git-history remediation have different risks and rollback needs.

Do not defer the publication boundary: mark the repository unsuitable for public/product publication now and begin security/archive decisions. Defer destructive or navigation-heavy cleanup until the user operating layer defines what replaces the current README, task-history visibility, and `/about` workflow.

The recommended first three releases are:

1. product operating-layer design and replacement onboarding;
2. security/history/archive decision and sanitized example set;
3. local-workspace separation with path-scoped ignores and no history rewrite.

After those are accepted, maintainer/history consolidation and ChatGPT packaging can proceed independently.
