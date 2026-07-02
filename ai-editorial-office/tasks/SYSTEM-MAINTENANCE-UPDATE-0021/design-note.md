# Design Note: Preflight Gate

## where it lives

Preflight Gate lives between orchestration and any production activity:

```text
intake -> orchestration -> preflight decision -> production
```

Production includes writing, rewriting, recommendation generation, visual
preparation, conversion, extraction, rendering, or other tool work that starts
creating the requested output.

## who performs it

`chief_editor` performs the gate during orchestration because Chief Editor owns
routing, process depth, role assignment, and the decision to start production.

`intake_agent` supplies normalized inputs: audience, channel, goal, output,
constraints, missing information, source materials, and assumptions. Intake does
not approve production.

## how it connects to intake

Intake already tries to recover obvious context and avoids unnecessary
clarifying questions. Preflight uses that normalized brief and checks whether
the system has enough information to start production safely.

## how it connects to orchestration

Preflight is a routing decision inside orchestration, not a new pipeline stage,
new role, or new status. It can be recorded in `orchestration_plan.md`,
`task-manifest.md`, `status.md`, or `brief.md`, whichever already exists and is
the smallest adequate place for the task.

## decision fields

| Field | Values |
| --- | --- |
| Audience | `confirmed` / `inferred` / `unknown` |
| Channel or context | `confirmed` / `inferred` / `unknown` |
| Deliverable | `defined` / `unclear` |
| Source boundary | `defined` / `unclear` |
| Success criterion | `defined` / `unclear` |
| Approval boundary | `defined` / `unclear` |
| Missing data strategy | `ask` / `constrain` / `proceed` / `block` |

The system is not required to ask a question. It is required to decide.

## decision behavior

- `ask`: critical information is missing and cannot be safely inferred or constrained.
- `constrain`: information is incomplete, but the task can be safely narrowed.
- `proceed`: available information is sufficient for the selected scope.
- `block`: the task cannot be performed safely with current input.

## examples

### simple task

Request: `Перепиши письмо.`

- Audience: `inferred`
- Channel or context: `inferred`
- Deliverable: `defined`
- Source boundary: `defined` if the source letter is supplied; `unclear` if not
- Success criterion: `inferred`
- Approval boundary: `defined`
- Missing data strategy: `proceed` if source exists; `ask` if no source letter exists

### partial uncertainty

Request: `Сделай пост для анонса мероприятия.`

- Audience: `inferred` or `unknown`
- Channel or context: `inferred`
- Deliverable: `defined`
- Source boundary: `unclear` until event facts are supplied
- Success criterion: `inferred`
- Approval boundary: `defined`
- Missing data strategy: `constrain` if enough event facts exist and the post can avoid unsupported specifics; otherwise `ask`

### critical gap

Request: `Подготовь коммуникацию для сотрудников.`

- Audience: `unknown` if employee segment, channel, and action are absent
- Channel or context: `unknown`
- Deliverable: `unclear`
- Source boundary: `unclear`
- Success criterion: `unclear`
- Approval boundary: `unclear`
- Missing data strategy: `ask`

### impossible task

Request: `Сделай итоговую коммуникацию по документу`, but the document is not
provided and cannot be recovered.

- Audience: `unknown`
- Channel or context: `unknown`
- Deliverable: `defined`
- Source boundary: `unclear`
- Success criterion: `unclear`
- Approval boundary: `unclear`
- Missing data strategy: `block`

## separate artifact?

No separate mandatory artifact is needed. The gate can be a compact table or
short bullet block in an existing artifact. A new standalone artifact would make
compact tasks heavier and violate the user constraint.

## avoiding bureaucracy

- Do not ask questions just because a field is not `confirmed`.
- `inferred` is acceptable when the inference does not materially risk the
  wrong result.
- Use `constrain` before `ask` when safe narrowing produces a useful result.
- Use a one-line preflight summary for compact tasks.
- Do not create placeholder preflight files.

## files to change

- `ai-editorial-office/AGENTS.md`: add the global pre-production gate principle.
- `ai-editorial-office/agents/chief_editor.md`: add role responsibility and boundaries.
- `ai-editorial-office/agents/intake_agent.md`: add intake support for preflight inputs without making Intake the gate owner.
- `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`: add a compact optional/pre-production block in the existing orchestration artifact.

## files not to change

- `ai-editorial-office/kb/task_statuses.md`
- `ai-editorial-office/pipelines/*.md`
- `ai-editorial-office/agents/review_agent.md`
- `ai-editorial-office/agents/final_editor.md`
- task templates
- visual subsystem files
- old `TASK-*` folders
