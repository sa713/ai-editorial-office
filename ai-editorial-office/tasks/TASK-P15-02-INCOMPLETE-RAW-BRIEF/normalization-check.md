# Normalization Check

## test metadata

- Test ID: P1.5-02
- Task ID: TASK-P15-02-INCOMPLETE-RAW-BRIEF
- Role applied: intake_agent
- Rule tested: Raw Brief Normalization
- Raw request type: incomplete user request
- Production material created: no
- Material plan or structure created: no
- Production files changed: no

## raw request

```text
Нужно срочно подготовить материал про обновление.

Наверное для руководителей.
```

## task signal

- Requested action: prepare a material.
- Topic: an update.
- Urgency: urgent, deadline unspecified.
- Possible audience cue: "probably for leaders", explicitly uncertain.

## background context

- The user indicates urgency.
- The user is unsure about the audience.

## noise

- None. The request is incomplete, not noisy.

## confirmed

- A material is needed.
- The material is about an update.
- The user says it is urgent.
- The possible leadership audience is uncertain, not confirmed.
- No source is supplied.

## inferred

- This is likely an editorial or writing task.
- Intake cannot choose a production pipeline safely because artifact type,
  channel, audience, source, and goal are missing.

## unknown

- What exactly changed or was updated.
- What material type is needed.
- Publication or delivery channel.
- Exact audience.
- Communication goal.
- Source material or source owner.
- Benefits, consequences, risks, dates, or actions related to the update.
- Deadline implied by "urgent".
- Acceptance criteria for the future material.

## assumptions

- Audience may be leaders, but only as an unconfirmed assumption based on
  "Наверное для руководителей".
- The task likely requires clarification before Chief Editor can select a
  production pipeline.
- No assumption is safe enough to support production.

## open questions

- What update is this about?
- What kind of material is needed?
- Who exactly should read it?
- Where or how will it be used?
- What should the material achieve?
- What source should be used for facts about the update?
- What can be said about benefits, consequences, risks, dates, and next steps?
- What does "urgent" mean as a deadline?
- What criteria should the finished material satisfy?

## source status

- Source status: `mentioned but not provided`.
- Source materials present: none.
- Active source: none.
- Source boundary: the update is only a named topic; no details are available
  for factual claims.
- Required next source action: ask for source material, description, owner
  input, or a constraint that allows a non-factual placeholder task.

## acceptance criteria

- Future material acceptance criteria: `unknown`.
- Normalization acceptance criteria:
  - do not write the material;
  - do not create a future material plan or structure;
  - classify missing data as `unknown`, `assumption`, or `question`;
  - do not invent update content, artifact type, channel, exact audience,
    communication goal, sources, benefits, or consequences.

## fantasy check

| Check | Result | Notes |
| --- | --- | --- |
| Invented update content | pass | No update details were added. |
| Invented material type | pass | Artifact remains generic material; exact type is unknown. |
| Invented channel | pass | Channel remains unknown. |
| Invented exact audience | pass | Leadership is only an assumption, not a confirmed audience. |
| Invented communication goal | pass | Goal remains unknown. |
| Invented source | pass | Source status is `mentioned but not provided`; no source is active. |
| Invented benefits/consequences | pass | No benefits or consequences were added. |
| Invented content acceptance criteria | pass | Future material criteria remain unknown. |
| Draft or structure created | pass | No draft, outline, or material plan was created. |

## editorial conclusion

passed

The request is too incomplete for production. Raw Brief Normalization correctly
kept the task at intake/clarification stage and did not invent the update,
artifact type, channel, audience, goal, source, benefits, consequences, or
content acceptance criteria.
