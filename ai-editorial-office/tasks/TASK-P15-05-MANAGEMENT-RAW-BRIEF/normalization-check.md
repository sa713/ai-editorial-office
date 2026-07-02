# Normalization Check

## test metadata

- Test ID: P1.5-05
- Task ID: TASK-P15-05-MANAGEMENT-RAW-BRIEF
- Role applied: intake_agent
- Rule tested: Raw Brief Normalization
- Raw request type: short management request
- Plan created: no
- Roadmap created: no
- Architecture decision created: no
- Change list created: no
- Production files changed: no

## raw request

```text
Предлагаю сделать отдельный режим для задач Сбера.

Коротко набросай план что будем делать.
```

## task signal

- Proposal: make a separate mode for Sber tasks.
- Requested future output: short plan of what to do.
- Subject: Sber tasks.
- Management/system-change dependency: requires clarification before planning.

## background context

- The request implies a possible system improvement or operating-mode change.
- No problem statement, examples, prior failures, source policy, or governance
  reason is supplied.

## noise

- None. The request is short and managerial, not noisy.

## confirmed

- The user proposes a separate mode for Sber tasks.
- The user asks for a short plan in the future task.
- No Sber requirements are supplied in the raw request.
- No source files, examples, or policy references are supplied.
- The current test forbids creating the plan.

## inferred

- This is likely a management/system-change planning request.
- It is not an ordinary content task for Sber.
- Sber client profile should not be activated merely from this normalization
  test, because no content task or explicit source policy use is being routed.

## unknown

- Which functions the Sber mode should have.
- Which files would need changing.
- Which roles would participate.
- Which architecture would be chosen.
- Which Sber requirements apply.
- Which stages would be in the plan.
- Which implementation constraints exist.
- What problem, failure, or opportunity motivates the mode.
- Who should approve the future plan.

## assumptions

- The future work may need Chief Editor routing as a system-change proposal.
- The future work may need source material about Sber requirements before
  planning.
- No assumption is safe enough to design the mode.

## open questions

- What specific Sber-task problem should this mode solve?
- Are there existing Sber requirements, policy files, or examples to use?
- Should the future output be an evaluation, proposal, plan, or implementation
  task?
- What is explicitly out of scope for Sber-mode work?
- Should the plan consider existing client-profile mechanics before proposing a
  separate mode?
- Who is the intended reader or approver of the future plan?

## source status

- Source status: `mentioned but not provided`.
- Source materials present: none.
- Active source: none.
- Sber requirements status: unknown.
- Client profile status: not activated for this test.
- Required next source action: ask for problem statement, scope, source policy,
  examples, or permission to inspect existing Sber-related project files before
  any plan/design work.

## acceptance criteria

- Future plan acceptance criteria: `unknown` beyond "short" and related to a
  possible separate Sber task mode.
- Normalization acceptance criteria:
  - do not create a plan;
  - do not create a roadmap;
  - do not create architecture;
  - do not create a change list;
  - do not invent Sber requirements;
  - do not invent functions, files, roles, stages, or implementation
    constraints;
  - keep client/source status explicit.

## fantasy check

| Check | Result | Notes |
| --- | --- | --- |
| Invented Sber-mode functions | pass | No functions were defined. |
| Invented files to change | pass | No files or change list were proposed. |
| Invented roles | pass | No production or new roles were assigned for Sber-mode design. |
| Invented architecture | pass | No architecture was selected. |
| Invented Sber requirements | pass | Sber requirements remain unknown. |
| Invented plan stages | pass | No future plan stages were created. |
| Invented implementation constraints | pass | Constraints remain unknown except user/test constraints. |
| Created plan/roadmap/design | pass | Only brief/task definition and check were created. |
| Activated Sber profile | pass | Client profile is not activated for this normalization test. |

## editorial conclusion

passed

Raw Brief Normalization handled the management request correctly. It captured
the proposal and future requested artifact while refusing to design Sber-mode,
create a plan, select architecture, assign roles, list file changes, or invent
Sber requirements and implementation constraints.
