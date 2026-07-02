# Compact path design

## Design principle

Compact path is not a shortcut around governance. It is a smaller artifact profile for tasks where full process depth does not add enough value.

It should reduce:

- file count;
- repeated context loading;
- duplicate review outputs;
- verbose handoff;
- status narrative bloat.

It must preserve:

- review-gate;
- role separation;
- source discipline;
- restartability;
- human approval boundary;
- finalization clarity.

## When compact execution is allowed

Compact path may be used when all are true:

- risk mode is `low-risk`, or `standard` with simple source-light scope;
- no high-governance sensitivity;
- no external publication approval is implied;
- no legal, compliance, HR, finance, security, medical or regulatory sensitivity;
- no material numeric/product/policy claims unless source evidence is simple and local;
- the task has one primary deliverable or one small deliverable set;
- review can validate the output without reading a large evidence base;
- Chief Editor records compact path rationale.

## When compact execution is not allowed

Compact path is forbidden when:

- risk mode is `high-governance`;
- user requests external publication-ready material with sensitive stakes;
- factual claims require claim-level traceability;
- sources contradict each other;
- stakeholder conflict is present;
- source material is long, ambiguous, or untrusted enough to require research;
- human approval requirement is unresolved and material;
- task has multiple audiences with different artifact needs;
- review cannot validate without full artifact context.

## Compact execution profile

Recommended shape:

```text
intake/brief -> compact orchestration -> production -> compact review -> finalization/governance note
```

This is not a new pipeline. It is a process depth profile applied inside existing or custom workflows.

## Minimal viable artifacts

## Compact task package

Required:

- `brief.md`;
- `task-manifest.md`;
- `status.md`;
- `orchestration_plan.md` or compact orchestration section;
- draft/output artifact;
- `review.md`;
- final artifact when finalization is requested;
- `final_decision.md` when governance decision is made.

Conditionally required:

- `sources.md` only if source traceability matters;
- `claims-used.md` only if factual claims are used;
- role handoff only when actual role transfer occurs;
- `compact-handoff.md` only for final user-facing transfer.

Normally omitted in compact path:

- separate `qa-checklist.md`;
- separate `review-summary.md`;
- separate `reviewer-notes.md`;
- separate `finalization-checklist.md`;
- separate `finalization-notes.md` unless finalization changed meaning or risk;
- `claims_table.md` for no-claim or very low-claim tasks;
- `facts.md` when no factual evidence base is needed;
- `context-summary.md` unless context fragmentation occurred.

## Compact review

Compact review should contain:

```markdown
# Review

## Verdict
approved | changes_requested | blocked

## Scope reviewed
- artifact(s):
- brief / orchestration checked:

## Independence check
Writer/source:
Reviewer:
Result: passed | failed | unknown

## Usefulness check
Does the material deliver the reader outcome?

## Blocking issues
None, or bounded list.

## Governance note
Human approval / publication approval state.

## Next action
One clear action.
```

Compact review may embed checklist logic in prose. It must not create a fake full review by listing many generic checks.

## Allowed shortcuts

Allowed:

- combine review verdict and review summary in `review.md`;
- embed compact checklist in `review.md`;
- omit `qa-checklist.md` if review is compact;
- omit `review-summary.md` if `review.md` has clear next action;
- omit research artifacts when no factual claims or external evidence are needed;
- use compact orchestration if pipeline choice and artifact scope are obvious;
- use one final note instead of separate finalization notes/checklist for low-risk tasks;
- skip role handoff when no role transfer occurs;
- keep `status.md` as short transition history, not full narrative.

## Forbidden shortcuts

Forbidden:

- skipping review;
- reviewer approving own writing without independence note;
- creating `final.md` before approved review;
- treating finalized as approval to publish/send;
- omitting source traceability for material factual claims;
- using compact path for high-governance;
- hiding unresolved assumptions;
- silently changing task goal;
- collapsing writing and review into one unstated role;
- skipping manifest update at stage transition;
- using compact path to avoid blockers.

## Compact orchestration section

When compact path is selected, orchestration should include:

```markdown
## Process depth

Depth: compact

Rationale:

Artifacts intentionally omitted:

Review still required: yes

Forbidden shortcuts:
```

## Expected effect

Compact path should reduce process overhead while keeping the core safety model:

- "small task" does not mean "unreviewed task";
- "compact" does not mean "untraceable";
- "low-risk" does not mean "publish without human owner";
- "fewer files" does not mean "less explicit state".

## Trial use

First test compact path on:

- one low-risk rewrite;
- one source-light internal communication;
- one compact review of an existing small artifact.

Do not use the first compact-path tasks as templates until after retrospective.
