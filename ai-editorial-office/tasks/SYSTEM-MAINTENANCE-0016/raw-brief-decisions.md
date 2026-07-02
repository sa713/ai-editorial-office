# Raw Brief Decisions

## Step 1 decision

Canonical owner:

```text
ai-editorial-office/agents/intake_agent.md
```

## decision status

Accepted for Step 1.

## why this owner

Raw Brief Normalization belongs to Intake because it happens before orchestration and before production work.

The mechanism asks the system to:

- understand a terse or incomplete user request;
- infer only the obvious editorial context;
- form a working brief;
- decide whether clarifying questions are actually needed.

Those are Intake responsibilities, not Chief Editor responsibilities.

The current `intake_agent.md` already says Intake converts raw user requests, notes, documents, links, and fragments into a deterministic task package for Chief Editor orchestration. It also already owns normalization into title, goal, audience, output, channel, and constraints.

## role boundary

`chief_editor.md` remains the orchestration owner:

- confirms or overrides task type;
- confirms risk mode;
- selects pipeline or mode;
- assigns roles;
- preserves governance and review boundaries.

Chief Editor may later get a short reference saying it should expect Intake to normalize Raw Briefs before asking the user for clarification. The complete mechanism should not live there.

## ownership rule

Add the future Raw Brief Normalization rule to `intake_agent.md`.

If a companion Chief Editor note is added later, keep it short and do not duplicate the full rule.

## assumptions

- Raw Brief Normalization is role behavior, not a global invariant.
- The update should not introduce a new pipeline, role, review stage, or visual subsystem behavior.
- The future production rule should preserve explicit uncertainty and should not convert assumptions into facts.

