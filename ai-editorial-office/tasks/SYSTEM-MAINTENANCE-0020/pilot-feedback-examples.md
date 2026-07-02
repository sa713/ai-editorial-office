# Pilot Feedback Examples

These are demonstration examples only. No `feedback.md` files are added to old
task folders.

## Example 1: `TASK-0003` -> `TASK-0003B`

### task

- Original task: `TASK-0003`
- Follow-up task: `TASK-0003B`
- Source evidence: `ai-editorial-office/tasks/TASK-0003B/brief.md`

### example user reaction

The selected `more editorial / journal-like` version worked editorially, but the
user saw a risk of synthetic editorial tone. The user would more likely choose
the original restrained version as a base because it felt more honest and less
written-up.

### example `feedback.md`

```markdown
# Feedback

## metadata

- Task ID: `TASK-0003`
- Captured date: 2026-05-19
- Captured by: `chief_editor`
- Related final decision: `TASK-0003/final_decision.md`
- Related delivered artifact: `TASK-0003/final.md`

## user reaction

- Short summary: Editorially stronger variant felt at risk of synthetic tone; restrained version felt more honest.
- Reaction type: `mixed`
- User wording or paraphrase: The editorial version worked, but the restrained base is more trustworthy and less written-up.

## feedback scope

- understanding the task: no
- structure: no
- meaning: yes
- tone: yes
- format: no
- facts: no
- process: no
- usefulness: yes
- other: none

## signal classification

- Classification: `possible system signal`
- Why: The issue points to a repeatable editorial risk: strengthening a text can over-produce tone.
- Similar known signals: none recorded at the time.
- Should this be considered for `/kb/feedback_patterns.md`: yes, as `observed` if another similar case appears.

## follow-up boundary

- Follow-up needed: yes
- Follow-up type: bounded revision or follow-up task
- Does this reopen the task automatically: no
- Does this change the final decision retroactively: no

## what not to infer

- Do not infer: stronger editorial tone is always worse; restrained style is always preferred; TASK-0003 failed.
- System rules changed by this feedback: no
```

### classification

- This is task-local feedback with a possible system signal.
- It could enter `feedback_patterns.md` only as an `observed` tone-strengthening pattern, not as a rule.

## Example 2: `TASK-0010`

### task

- Task: `TASK-0010`
- Source evidence: `ai-editorial-office/tasks/TASK-0010/comparison-review-v2.md`

### example user reaction

The comparison identified that v1 was useful but completed the concept too
quickly, v2 improved diagnostic discipline but became too defensive, and v3
found the better balance.

### example `feedback.md`

```markdown
# Feedback

## metadata

- Task ID: `TASK-0010`
- Captured date: 2026-05-30
- Captured by: `chief_editor`
- Related final decision: current task final decision or comparison package
- Related delivered artifact: `recommendations-v1/v2/v3` comparison set

## user reaction

- Short summary: Diagnostic mode improved by resisting artificial completion, but excessive caution reduced usefulness before later balancing.
- Reaction type: `mixed`
- User wording or paraphrase: V1 was too constructive, v2 too defensive, v3 closer to the right mode.

## feedback scope

- understanding the task: yes
- structure: no
- meaning: yes
- tone: yes
- format: no
- facts: no
- process: yes
- usefulness: yes
- other: diagnostic-mode calibration

## signal classification

- Classification: `possible system signal`
- Why: The reaction concerns repeatable system behavior: premature design versus over-cautious diagnosis.
- Similar known signals: artificial completion and defensive diagnostic drift in the comparison.
- Should this be considered for `/kb/feedback_patterns.md`: yes, if another diagnostic task shows the same calibration issue.

## follow-up boundary

- Follow-up needed: yes
- Follow-up type: system-pattern watch or separate reviewed system update
- Does this reopen the task automatically: no
- Does this change the final decision retroactively: no

## what not to infer

- Do not infer: all recommendations are premature design; all uncertainty language is bad; diagnostic tasks should avoid strong conclusions.
- System rules changed by this feedback: no
```

### classification

- This is a possible system signal because it describes behavior across versions.
- It may enter `feedback_patterns.md` as `observed` or `recurring` only after review confirms it appears beyond this comparison.

## pilot conclusion

- `feedback.md` would capture the user reaction in the original task only if the reaction happened after delivery.
- Follow-up work may become a new task or bounded revision, but feedback capture itself does not decide that.
- Neither example automatically changes `AGENTS.md`, roles, pipelines, review-gate, or statuses.
- Only repeated or validated signals should move into `feedback_patterns.md`.
