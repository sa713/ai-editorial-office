# Knowledge Evolution Smoke Test

Status: manual smoke-test / synthetic examples only.

Purpose: check whether Knowledge Evolution dispositions are applied only when
a task produces future-useful learning, reusable patterns, canon-update
candidates, stale/conflicting knowledge, correction or retirement needs, or
`/about` memory-sync implications.

This file is not a canonical rule owner. Canonical guidance lives in
`/kb/editorial_learning_framework.md`.

## Expected Classification Labels

- `task_local`: Keep the observation in the task without future-use claim.
- `learning_candidate`: Preserve as a reusable learning candidate, but do not
  promote to canon.
- `pattern_candidate`: Watch as a repeated or likely-reusable pattern.
- `canon_update_candidate`: Route to the existing canonical owner for reviewed
  update consideration.
- `stale_knowledge_challenge`: Challenge guidance that appears outdated,
  conflicting, duplicated, or unsupported by current repository state.
- `retire_or_correct_candidate`: Mark existing guidance for correction,
  supersession, or retirement review.
- `memory_sync_candidate`: Update `/about` only after canonical changes require
  exported memory alignment.
- `reject_or_defer`: Record why the signal is weak, private, duplicate, or not
  worth promoting.

## Cases

| Case | Scenario | Expected | Checks |
| --- | --- | --- | --- |
| KE-01 | A single task uses a one-off workaround for a private source file that cannot be described publicly. | `task_local` | no canon promotion; privacy boundary preserved |
| KE-02 | Three review reports repeat the same failure: canon-update candidates lack owner and evidence chain. | `pattern_candidate` | repeated signal; owner and evidence path visible |
| KE-03 | A release changes canonical lifecycle guidance and `/about` still mirrors the old state. | `memory_sync_candidate` | `/about` treated as mirror, not source of truth |
| KE-04 | Current `AGENTS.md` contradicts an older role file about who owns canon promotion. | `stale_knowledge_challenge` | governing precedence applied; owner identified |
| KE-05 | A completed release proves a small checklist reduces repeated review blockers, and the existing learning framework is the owner. | `canon_update_candidate` | reviewed owner path; no duplicate artifact |
| KE-06 | A past guideline is no longer valid because its capability was superseded by a frozen architecture decision. | `retire_or_correct_candidate` | supersession evidence and review path visible |
| KE-07 | A writer likes a local phrasing trick in one draft, but there is no repeated use or future system value. | `reject_or_defer` | no junk-drawer promotion |
| KE-08 | A review identifies a source freshness issue for a supplied document, but the task can finish with a scoped caveat. | `learning_candidate` | task-local caveat allowed; future learning scoped |

## Pass Criteria

- Knowledge Evolution does not activate for ordinary task notes without
  future-use value.
- Every promotion beyond task-local has source evidence, scope, owner,
  disposition, and review path.
- `/about` is never treated as canon.
- Stale or conflicting guidance is challenged through owner/evidence review,
  not silent deletion.
- No case creates a new role, pipeline, lifecycle stage, review gate, automatic
  canon promotion, or mandatory artifact.
