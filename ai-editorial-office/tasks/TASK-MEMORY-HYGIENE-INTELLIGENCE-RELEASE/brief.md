# Brief

## Task identity

- Task ID: `TASK-MEMORY-HYGIENE-INTELLIGENCE-RELEASE`
- Release ID: `S5.R3`
- Title: Memory Hygiene Intelligence Release
- Date opened: 2026-07-10

## Goal

Complete `S5.R3 - Memory Hygiene Intelligence` through Release Candidate state
so external project memory stays accurate, compact, useful, synchronized with
repository canon, and free from stale, duplicated, temporary, sensitive, or
misleading content without becoming a second source of truth.

## Audience and outcome

- Primary audience: Project Lead.
- Outcome: a researched, architecture-compatible, implemented, validated,
  independently reviewed, committed Release Candidate ready for architectural
  review.
- Release acceptance remains a later Project Lead decision.

## Required deliverables

- `../../research/memory_hygiene_intelligence_landscape.md`
- `../../research/memory_hygiene_intelligence_architecture_synthesis.md`
- `../../research/memory_hygiene_intelligence_release_report.md`
- `../../releases/S5-R3/release-pack.md`
- bounded canonical integration through existing owners;
- ten-scenario memory-disposition validation;
- complete editorial task lifecycle and final local commit.

## Required behavior

Define sync and no-sync triggers, exact-copy and compact-summary rules, stale
and contradiction handling, omission, compression, correction, retirement,
ownership, evidence, validation, and review.

Representative dispositions:

```text
canonical change or memory-hygiene signal
-> materiality and source check
-> exact-copy, compact-summary, omit, defer, correct, retire, or no-sync
-> validation
-> review
-> synchronized non-canonical memory
```

## Constraints

- Repository canon remains authoritative; `/about` is derived memory only.
- No new roles, pipelines, lifecycle stages, review gates, automatic memory
  writes, automatic canon changes, memory override, mandatory per-commit sync,
  completeness metrics, duplicate stores, or unsupported new owner.
- Advisory checks may report likely drift but cannot write automatically.
- Leave root `diff_intake.md` untouched.
- Do not touch `/Users/sa/Documents/codex/redaction`.
- Do not record Project Lead acceptance, mark S5.R3 `Done`, start S5.R4, or
  push the commit.

## Evidence and validation

- Prefer primary and authoritative sources.
- Validate all ten scenarios named by the mission.
- Demonstrate correct disposition and owner, preserved canonical authority,
  bounded growth, meaningful-context preservation, and no automatic
  propagation.
- Run repository diff, `/about`, task-lifecycle, task-pack, direct task, and
  staged-diff checks.

## Done condition

The mechanism is implemented through existing owners, required artifacts and
all ten scenarios are complete, independent review is approved, state and
memory are aligned for S5.R3 `Review`, the Release Pack is complete, and one
local Release Candidate commit exists.
