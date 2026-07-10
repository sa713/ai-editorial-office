# Memory Hygiene Intelligence Smoke Test

Date: 2026-07-10

Release: `S5.R3 - Memory Hygiene Intelligence`

Status: passed

## Purpose

Validate the bounded external-memory disposition contract against the ten
required synthetic scenarios. These cases test source authority, materiality,
exact-copy and compact-summary behavior, stale/contradictory repair, omission,
compression, consolidation, retirement, no-sync, validation, review, and
non-automation.

They validate decision mechanics only. They do not prove that all current or
future memory is complete, permanently fresh, sensitive-data-free, or useful
in every external context.

## Pass contract

Every case must expose:

- canonical source and represented memory fact/location;
- memory-hygiene signal and evidence;
- materiality, purpose, sensitivity, and continuing-value judgment;
- one supported disposition;
- current owner and manual edit/review path;
- branch-appropriate validation;
- preserved canonical authority;
- bounded growth and meaningful-context treatment;
- explicit non-automation.

A case fails if memory overrides canon; a mapped exact copy is independently
edited; a summary broadens/overstates canon; unreviewed, task-local, temporary,
private, sensitive, or restricted content propagates; meaningful context is
silently deleted; a checker writes; or any automatic acceptance, canon, state,
backlog, roadmap, or memory action occurs.

## Case 1: Canonical role file changes and exact-copy memory must update

### Synthetic evidence

- Canonical source: `ai-editorial-office/agents/chief_editor.md`.
- Memory location: `/about/chief_editor.md`, an explicitly mapped exact copy.
- Source change: Chief Editor gains reviewed memory-disposition responsibilities.

### Decision

- Material external effect: yes; active external operational instructions
  changed.
- Sensitivity: none.
- Disposition: `exact-copy`.
- Owner/path: Chief Editor authorizes; Writer Agent copies from canon; Review
  Agent reviews changed behavior; checker compares bytes.
- Validation: `cmp` through `check_about_memory_package.sh`; 20-file count.
- Growth: no new memory file; one mapped copy replaced.
- Context: all canonical wording preserved exactly.
- Non-automation: checker reports only; the authorized Writer action performs
  the copy.

### Result

Pass. Canon owns the wording and the mapped copy is synchronized exactly.

## Case 2: Internal research report changes but external memory should not

### Synthetic evidence

- Canonical/repository source: a release landscape report gains two additional
  source limitations.
- Current memory does not quote or summarize those research details.
- The release's durable external conclusion and boundaries are unchanged.

### Decision

- Material external effect: no.
- Disposition: `no-sync`; research details are also `omit` from `/about`.
- Owner/path: Chief Editor records no-sync only if the release's audit trail
  needs it.
- Validation: inspect existing summaries against changed conclusion; no
  represented fact changed.
- Growth: zero.
- Context: full research remains in the repository.
- Non-automation: report save does not trigger propagation.

### Result

Pass. Repository-only evidence remains available without memory growth.

## Case 3: Temporary Release Candidate state is replaced by accepted state

### Synthetic evidence

- Canonical sources: accepted Release Verdict and state files.
- Memory currently says a release candidate is in review and acceptance is
  pending.
- Project Lead later accepts the release.

### Decision

- Material external effect: yes; approval/current-state meaning changed.
- Disposition: `correct` plus `compact-summary` replacement.
- Owner/path: Chief Editor verifies acceptance evidence; Writer Agent replaces
  pending state; Review Agent checks no false acceptance.
- Validation: no active summary retains the old pending statement; state copy
  and compact summaries agree with the accepted verdict.
- Growth: replacement, not an appended history block.
- Context: prior RC history remains in release/task repository artifacts.
- Non-automation: verdict does not write memory automatically.

### Result

Pass. Temporary state is superseded rather than accumulated.

## Case 4: Memory summary contains stale project status

### Synthetic evidence

- Canonical state: S5.R2 accepted; S5.R3 in `Review`.
- Memory summary: S5.R2 still in `Review`; S5.R3 not started.

### Decision

- Material external effect: yes; stale status can route work incorrectly.
- Disposition: `correct`.
- Owner/path: Chief Editor identifies `project-state.md` and accepted S5.R2
  verdict; Writer Agent corrects the existing summary; Review Agent verifies
  current/next action.
- Validation: structured state scan and source/summary semantic comparison.
- Growth: existing statements replaced.
- Context: current state is compact; detailed transition history remains in
  release/task artifacts.
- Non-automation: stale signal prompts review, not an automatic write.

### Result

Pass. Current state and next action are restored from authoritative evidence.

## Case 5: Canonical and memory files contradict each other

### Synthetic evidence

- Canonical role file states memory writes are manual.
- Compact memory summary says the system continuously synchronizes `/about`.

### Decision

- Material external effect: critical authority/behavior conflict.
- Disposition: `correct`; if canonical owners also conflicted, `defer` and
  repair canon first.
- Owner/path: Chief Editor selects the named canonical owner; Writer Agent
  removes the false automation claim; Review Agent checks all summary surfaces.
- Validation: the contradictory claim is absent and manual/non-automation
  wording matches canon.
- Growth: no new statement beyond the corrected bounded rule.
- Context: no meaningful context supports the false claim, so none is lost.
- Non-automation: memory cannot change canon or resolve canonical ambiguity.

### Result

Pass. Canon wins; unresolved canon conflict blocks speculative memory repair.

## Case 6: A large release adds detail that should be compressed

### Synthetic evidence

- Canonical release adds a 250-line operational framework.
- External memory needs only its purpose, owner, activation/boundary,
  non-goals, and current state.
- Proposed memory draft repeats implementation, research, and all examples.

### Decision

- Material external effect: yes, but full-copy value is low.
- Disposition: `compact-summary` and `compress`.
- Owner/path: Chief Editor selects material facts; Writer Agent updates one
  existing summary; Review Agent compares against canon.
- Validation: purpose, source, scope, owner, applicability, caveats, approval,
  and non-automation remain; raw evidence/examples/narration are absent.
- Growth: no new file; redundant proposed detail rejected.
- Context: canonical file and release report retain full detail.
- Non-automation: no machine-generated summary is published without review.

### Result

Pass. External memory gains durable meaning without becoming a mirror.

## Case 7: Sensitive or task-local information should be omitted

### Synthetic evidence

- Task artifact contains a client contact, internal source note, credential-like
  example, and private implementation detail.
- None is required to understand project architecture or current state.

### Decision

- Material external effect: no safe memory need.
- Disposition: `omit`.
- Owner/path: Chief Editor applies purpose/sensitivity check; Review Agent
  verifies omission and that no user-facing required context depended on it.
- Validation: sensitive/task-local strings are absent from `/about` and release
  summary; repository handling remains governed by its original scope.
- Growth: zero.
- Context: only a generic statement may remain if canon explicitly requires it;
  raw detail stays task-local.
- Non-automation: no scanner copies or redacts-and-publishes automatically.

### Result

Pass. Minimum necessary external context is preserved without exposure.

## Case 8: No meaningful external-memory effect and no-sync is correct

### Synthetic evidence

- A canonical research method gains an internal example and wording cleanup.
- Existing `/about` summary already states the unchanged durable principle.
- No role, state, source path, boundary, or next action changes.

### Decision

- Material external effect: none.
- Disposition: `no-sync`.
- Owner/path: Chief Editor confirms the represented fact remains accurate.
- Validation: compare the existing summary to the changed owner's durable
  meaning; checker still passes.
- Growth: zero.
- Context: new example remains discoverable in canon.
- Non-automation: canonical edit does not mandate memory churn.

### Result

Pass. No-sync is evidenced and does not mean the check was skipped.

## Case 9: Duplicate memory facts should be consolidated

### Synthetic evidence

- Three compact summary files repeat that `/about` is non-canonical.
- One copy uniquely adds source precedence; another uniquely adds the checker.
- Repetition obscures rather than improves navigation.

### Decision

- Material external effect: maintenance/bloat reduction.
- Disposition: `compress` through consolidation.
- Owner/path: Chief Editor chooses the strongest current summary location;
  Writer Agent merges unique useful meaning and removes redundant prose;
  Review Agent checks remaining references.
- Validation: one primary compact explanation preserves non-canonical status,
  source precedence, and checker use; short references may remain where
  operationally necessary.
- Growth: net decrease in duplicate prose; no new file.
- Context: unique meaning and canonical pointers are preserved.
- Non-automation: duplicate detection may advise; merge/delete remains reviewed.

### Result

Pass. Duplication is reduced without silent loss of unique context.

## Case 10: Obsolete memory content should be retired

### Synthetic evidence

- Memory describes an old release as the current next action.
- Canon and accepted verdict show that action is complete and a later release
  is now in review.
- Detailed old release history remains in its Release Pack and task folder.

### Decision

- Material external effect: yes; obsolete active guidance misroutes work.
- Disposition: `retire` plus replacement current-state summary.
- Owner/path: Chief Editor verifies current state; Writer Agent removes the old
  active claim and adds only the current compact pointer; Review Agent checks
  that no historical evidence was deleted from the repository.
- Validation: obsolete action absent from active memory; new action matches
  state/roadmap/backlog; old release artifacts still resolve.
- Growth: replacement, not cumulative history.
- Context: historical detail remains repository-only.
- Non-automation: no retention engine deletes content by age alone.

### Result

Pass. Obsolete active memory is retired while repository history survives.

## Summary matrix

| # | Disposition | Correct owner | Canon authoritative | Growth bounded | Meaning preserved | No automatic propagation | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | exact-copy | yes | yes | yes | yes | yes | pass |
| 2 | no-sync / omit | yes | yes | yes | yes | yes | pass |
| 3 | correct / compact-summary | yes | yes | yes | yes | yes | pass |
| 4 | correct | yes | yes | yes | yes | yes | pass |
| 5 | correct / defer | yes | yes | yes | yes | yes | pass |
| 6 | compact-summary / compress | yes | yes | yes | yes | yes | pass |
| 7 | omit | yes | yes | yes | yes | yes | pass |
| 8 | no-sync | yes | yes | yes | yes | yes | pass |
| 9 | compress / consolidate | yes | yes | yes | yes | yes | pass |
| 10 | retire / replace | yes | yes | yes | yes | yes | pass |

## Final result

All ten cases pass the documented contract.

The cases demonstrate correct disposition, current owner reuse, repository
authority, bounded memory growth, meaningful-context preservation, and no
automatic propagation. Synthetic cases do not prove that future users will
apply the contract correctly; independent review and repository validation
remain necessary.
