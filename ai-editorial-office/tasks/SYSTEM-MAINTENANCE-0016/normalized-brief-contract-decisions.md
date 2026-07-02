# Normalized Brief Contract Decisions

## owner

The contract lives in:

```text
ai-editorial-office/agents/chief_editor.md
```

## implemented decision

Chief Editor receives a normalized brief as the working basis for routing, but must not treat every element of that brief as a confirmed fact.

## context labels

Chief Editor distinguishes:

- `Confirmed` — explicitly confirmed by the user or supplied source material;
- `Inferred` — reliably recovered by Intake Agent from the raw request, task context, common sense, or editorial templates;
- `Unknown` — not known and not safely recoverable.

## allowed use of inferred context

Chief Editor may use `Inferred` context for:

- pipeline choice;
- mode choice;
- role choice;
- risk-mode choice.

This is allowed only when confidence is sufficient and the inference does not materially change the task.

## escalation rule

Chief Editor must request clarification when inferred context:

- substantially affects the expected result;
- changes the audience;
- changes the meaning of the task;
- could lead to the wrong result.

## examples

For "Need an email after the meeting. Remind people about the links and explain access," Intake may infer email, meeting participants, and reminder of materials. Chief Editor may use that context for routing without clarification.

For "Need an announcement for employees," if the specific employee audience materially changes the result, Chief Editor may request clarification.

## non-decisions

This update does not change:

- Intake Agent;
- pipelines;
- review;
- visual subsystem;
- role model;
- task status model.

