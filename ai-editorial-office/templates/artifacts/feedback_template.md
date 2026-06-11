# Feedback

Purpose: optional task-local record of user reaction after delivery. Create this
file only when the user actually responds to a delivered result.

```text
Один feedback не меняет систему автоматически.
```

## raw feedback

- Task ID:
- Captured date:
- Captured by:
- Related final decision:
- Related delivered artifact:
- User wording or paraphrase:
- Context:

## feedback summary

- Short summary:
- Reaction type: `accepted` / `praised` / `needs revision` / `rejected` / `unclear` / `mixed`
- Current task impact:

## classification

- Primary classification: `task_local` / `preference` / `observation` / `confirmed_pattern` / `system_change_candidate`
- Secondary classification, if any:
- Why:
- Similar known signals:

## task-local action

- Needed: yes/no/unclear
- Action type: none / bounded revision / clarification / new task
- Owner:
- Scope boundary:
- Review-gate impact:

## preference signal

- Is this a customer preference: yes/no
- Preference summary:
- Scope: this task / this customer / unknown
- Why this is not a global rule:

## watchlist signal

- Proposed for `engineering_watchlist.md`: yes/no
- Watchlist signal summary:
- Status if accepted: `observation` / `watch` / `confirmed pattern`
- Why this should or should not enter watchlist:

## backlog candidate

- Candidate: yes/no
- Candidate reason:
- Required evidence before backlog:
- System change proposal needed: yes/no/unknown

## decision

- Do not infer:
- Decision owner: `chief_editor`
- Decision:
- Does this reopen the task automatically: no
- Does this change the final decision retroactively: no
- System rules changed by this feedback: no
- Watchlist/backlog changed automatically: no
