# Stage 4 Closure State Inventory

## Bottom Line

Stage 4 is accepted, but sixteen live state-bearing files still contain mixed
candidate, pending-review, or pre-closure wording. Update only these files.
Historical release work must continue to show the release-candidate process.

## Evidence And Confidence

- Evidence: the five `releases/S4-R*/release-pack.md` files record
  `Project Lead: Accepted`; `BACKLOG.md` marks S4.R1-S4.R5 `Done`; the current
  user mission explicitly accepts Stage 4 and forbids opening Stage 5.
- Status semantics: `kb/domain_knowledge_pack_standard.md` permits `active` as
  the post-candidate pack status.
- Confidence: high.
- Unknowns: none material.
- Residual risk: a broad replacement would rewrite historical evidence or alter
  unrelated S3/S5 lifecycle language.

## Live Allowlist

| File | State-only change |
| --- | --- |
| `ai-editorial-office/kb/software_architecture_domain_pack.md` | `Status: release candidate` -> `Status: active` |
| `ai-editorial-office/kb/devsecops_domain_pack.md` | `Status: release candidate` -> `Status: active` |
| `ai-editorial-office/kb/cybersecurity_domain_pack.md` | `Status: release candidate` -> `Status: active` |
| `ai-editorial-office/kb/ai_engineering_domain_pack.md` | identity status -> `active`; replace the not-active-until-acceptance sentence with accepted active-state wording |
| `ai-editorial-office/kb/00_index.md` | describe all four packs as active, not release-candidate |
| `ai-editorial-office/project-state.md` | Stage 4 complete; S4.R1-S4.R5 accepted; waiting for Stage 5 start |
| `ai-editorial-office/ROADMAP.md` | Stage 4 status `Complete`; Stage 5 next, planned, and not started |
| `ai-editorial-office/BACKLOG.md` | closure-complete/waiting state; S4 rows `Done`; S5 rows `Not Started` |
| `ai-editorial-office/releases/S4-R1/release-pack.md` | accepted status and final state; remove present pending/review-ready self-description |
| `ai-editorial-office/releases/S4-R2/release-pack.md` | accepted status and final state; remove present pending/review-ready self-description |
| `ai-editorial-office/releases/S4-R3/release-pack.md` | accepted status and final state; remove present pending/review-ready self-description |
| `ai-editorial-office/releases/S4-R4/release-pack.md` | accepted status and final state; remove present pending/review-ready self-description |
| `ai-editorial-office/releases/S4-R5/release-pack.md` | accepted status and final state; replace explicit pending-acceptance wording |
| `about/project-state.md` | exact synchronized copy of canonical `project-state.md` |
| `about/project_tree.md` | describe the four packs as accepted, not release-candidate |
| `about/CHATGPT_MEMORY_EDITORIAL_STANDARDS.md` | `Current accepted packs`, not current release-candidate packs |

## Exact State Rules

- Pack lifecycle state is `active`; task-local pack activation remains optional
  and materiality-based. Do not imply automatic activation on every task.
- Release-pack status/final state is `accepted by Project Lead`. Preserve
  technical decisions, validation history, risks, and the RC audit sequence.
- Replace present-tense pending/recommended-decision sections with the recorded
  final decision. A generic release-readiness rule may remain.
- Project state must say Stage 4 is complete and Stage 5 is planned next but has
  not started. Do not open S5.R1.
- `/about` must remain exactly 20 files. Fifteen files are validator-enforced
  canonical copies; four `CHATGPT_MEMORY_*.md` files and `project_tree.md` are
  maintained summaries/maps. The validator does not inspect wording in the
  five manual artifacts, so review their accepted-state text directly.
- Backlog current work must communicate:

```text
Stage 4 Closure Complete

↓

Waiting for Stage 5 start
```

## Historical And Generic Material: Do Not Change

- `ai-editorial-office/tasks/TASK-*-DOMAIN-PACK-RELEASE/**` and the S4.R1 task.
- `ai-editorial-office/research/**`, including release reports and
  `stage4_strategic_review.md`.
- Generic `release candidate` lifecycle vocabulary in
  `kb/domain_knowledge_pack_standard.md`, roadmap/backlog release models,
  templates, and future S5 expected results.
- Unrelated S3.R4 candidate state, Sber `pending_source`, and role references to
  active or candidate packs.

## Forbidden Scope

- `/Users/sa/Documents/codex/redaction`.
- `AGENTS.md`, `ai-editorial-office/AGENTS.md`, agents, capabilities, roles,
  pipelines, lifecycle, Engineering Review, architecture, and technical pack
  content.
- Any file outside the sixteen-file allowlist, except task-local closure
  artifacts assigned by Chief Editor.
- Untracked `diff_intake.md`.

## Writer Start

First patch the four pack identity/status lines and the AI Engineering
post-acceptance sentence with exact, local edits. Inspect that diff before
continuing; do not begin with a repository-wide replacement.
