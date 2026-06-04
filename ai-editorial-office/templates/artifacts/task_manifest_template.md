# Task Manifest

Purpose: compact current-state pointer for a task. This is the first restart
artifact. Keep it short, current, and explicit about versions.

## task identity

- Task ID:
- Task title:
- Task type:
- Owner/current role:
- Created:
- Last updated:

## current state

- Current status:
- Selected pipeline:
- Risk mode:
- Process depth:
- Execution profile: `compact` / `expanded`
- Client profile: `none` / `sber` / `unknown`
- Client profile status: `not_applicable` / `active` / `pending_source`
- Current working artifact:
- Latest relevant handoff:
- Next required action:

## client profile

Use this section only when `Client profile` is not `none`.

```yaml
client_profile_files:
  - /kb/clients/sber/usage-rules.md
  - /kb/clients/sber/editorial-policy.md
  - /kb/clients/sber/sber-review-checklist.md
client_profile_activation_reason:
client_profile_source_status:
client_profile_stop_condition:
```

Rules:

- `sber` is active only for Sber-owned, Sber-product, Sber-communication, or
  explicit Sber-redpolicy tasks.
- If the cleaned Sber editorial policy is missing, stale, or unverified, use
  `client_profile_status: pending_source` and do not claim Sber-policy
  compliance.
- If Sber is only a topic, source, competitor, example, or object of independent
  analysis, use `Client profile: none` or
  `Client profile status: not_applicable`.

## freshness

- Last verified:
- Verified by:
- Stale if:

## current version pointers

Required when a task has multiple versions.

- Canonical pointer owner: this manifest / other task-local file:
- Current active artifact or artifact set:
- Replaces:
- Deprecated/previous versions:
- Versions no longer working artifacts:
- Version conflict state: none / unresolved / resolved
- What to read on restart:
- Old versions read only for: comparison / retrospective / unresolved conflict / unclear current version / reviewer-governance traceability
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version:
- Review outcome:
- Compact finalization shape allowed: yes/no/not applicable
- Human approval required: yes/no/unknown
- Human approval evidence:
- Final decision artifact:

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |

## stale or conflicting state

- None / list artifact, conflict, and action needed.

## active constraints

- User constraints:
- Pipeline constraints:
- Client-profile constraints:
- Governance constraints:

## open questions

- None / list only real open questions, blockers, or traceability gaps.

## next action packet

Minimum restart read set:

- `AGENTS.md` or invariant summary;
- this manifest;
- latest relevant handoff;
- current working artifact;
- active client-profile files when `client_profile` is not `none`;
- directly relevant pipeline, KB, or editorial knowledge.

Next action:

- Role:
- Action:
- Expected output:
- Stop conditions:

## lifecycle notes

- Legacy task folders consulted: yes/no and why
- Old artifact versions consulted: yes/no and why
- Safe-to-ignore material:
