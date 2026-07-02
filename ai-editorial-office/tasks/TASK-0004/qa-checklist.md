# QA Checklist

Task ID: `TASK-0004`

Owner: `review_agent`

Stage: `review`

## usefulness

- [x] Primary reader task is explicit.
- [x] Reader can choose their route by role.
- [x] The instruction helps complete actions, not just understand the process.
- [x] Optional context is placed after or near the action it affects.

## operational clarity

- [x] Author actions are sequenced.
- [x] Executor actions are sequenced.
- [x] Idea submission actions are sequenced.
- [x] Moderator and Curator roles are distinguished.
- [x] Completion ownership is clear.
- [x] Subtask restriction is visible near relevant actions.

## cognitive load

- [x] Opening is shorter and action-oriented.
- [x] Terms table is limited to needed terms.
- [x] Overview and role sections do not require rereading to understand the main flow.
- [x] Dispute guidance is grouped by condition and required information.

## action discoverability

- [x] Where to create a task is clear.
- [x] Which fields to fill are clear.
- [x] Which fields not to use are clear.
- [x] How to express interest as Executor is clear.
- [x] What happens after submission is clear.
- [x] What to do when stuck is clear.

## sequence integrity

- [x] Task flow preserves source sequence.
- [x] Idea flow preserves source sequence.
- [x] Role-specific instructions do not contradict overview.
- [x] Author selection happens before execution.
- [x] Accepted completion leads to `Done`.

## failure pattern checks

- [x] Answer delay reduced.
- [x] Context inflation reduced.
- [x] Buried action repaired.
- [x] Operational overload reduced through grouping.
- [x] Fake usefulness avoided.
- [x] Generic engagement language avoided.
- [x] Reader-state mismatch reduced.
- [x] Dead operational phrasing reduced.
- [x] Inherited-purpose substitution avoided.
- [x] Unnecessary editorialization avoided.

## residual checks

- [ ] Exact UI labels verified by product/process owner.
- [ ] Moderator list or ownership confirmed.
- [ ] Idea statuses confirmed.

Residual unchecked items are process-source gaps, not editorial defects.
