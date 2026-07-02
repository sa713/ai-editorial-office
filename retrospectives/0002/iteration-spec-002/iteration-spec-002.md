# Iteration spec 002

## Goal

Iteration 002 adds a small reader-state awareness layer to the AI editorial core.

Main principle:

```text
increase editorial sensitivity without increasing behavioral ambition
```

The iteration should help the system notice when a text makes the reader's first step feel more risky, mandatory or process-heavy than it needs to be.

## Why this is needed

TASK-0009 showed a practical gap. The materials were accurate and useful, but became stronger only after they made entry easier:

- the first action became "open and look";
- participation stopped sounding immediately required;
- the workspace felt like a place to visit, not a process to adopt;
- review checked pressure, fake momentum and unverified claims.

This is a writing and review sensitivity issue, not a new behavioral program.

## Design decisions

1. **Diagnosis-first.**
   Iteration 002 starts by naming friction patterns and review checks. It does not start from pipeline changes.

2. **Minimal implementation.**
   Future implementation should prefer short editorial knowledge updates before touching prompts, templates or pipelines.

3. **Optional and task-type dependent.**
   Reader-state checks apply only to relevant tasks: onboarding, participation, change communication, workspace launch, first-step communication.

4. **No system-wide behavioral layer.**
   There is no new required stage, role, score, dashboard, detector or universal checklist.

5. **Governance stays stronger than softness.**
   Mandatory stays mandatory. Optional stays optional. Unknown stays unknown.

6. **Bounded repair by default.**
   Reader-state issues should usually produce a small repair: reduce first-step pressure, clarify safe entry, remove fake obligation, preserve rules.

## Scope

Included:

- reader-state definitions and boundaries;
- low-pressure entry guidance;
- observation before commitment;
- safe first step;
- pressure audit in review;
- TASK-0009 failure patterns;
- bounded reader-state refinement shape;
- optional intake/orchestration prompts;
- governance honesty rule.

## Out of scope

Not included:

- new agents;
- new pipeline;
- behavioral UX platform;
- persuasion system;
- emotional scoring;
- adoption metrics;
- engagement optimization;
- conversion funnel;
- mandatory reader-state block for every task;
- rewrite of all pipelines;
- broad template rewrite;
- migration of old tasks.

## Recommended rollout

1. Add boundaries and honesty rule to the appropriate editorial knowledge owner.
2. Add failure patterns and review heuristics to editorial knowledge.
3. Add optional review block only for relevant tasks.
4. Add optional intake/orchestration prompts only if needed after review guidance.
5. Trial on 5-10 production tasks.
6. Run retrospective before broader implementation.

## Success criteria

Iteration 002 succeeds if:

- relevant tasks can identify a safe first step;
- review can catch fake obligation, fake momentum and pressure-first onboarding;
- writers can repair entry friction without full rewrite;
- governance clarity is not weakened;
- no new agent, pipeline, score or dashboard appears;
- reader-state remains optional and task-type dependent.

## Stop criteria

Stop or redesign the implementation if:

- reader-state becomes mandatory for all tasks;
- review starts judging tone instead of reader-action friction;
- engagement/adoption language appears;
- workspace framing invents activity;
- templates grow broadly before production trial;
- implementation touches pipelines before editorial knowledge is tested;
- any change hides mandatory rules behind soft language.
