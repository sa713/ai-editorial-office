# Normalization Check

## test metadata

- Test ID: P1.5-01
- Task ID: TASK-P15-01-NOISY-RAW-BRIEF
- Role applied: intake_agent
- Rule tested: Raw Brief Normalization
- Raw request type: noisy natural-language request
- Production writing performed: no
- Production files changed: no

## raw request

```text
Что-то у нас опять никто не читает новости подразделения.

Я уже не знаю, что с этим делать.

Нужно написать пост про новый дашборд интересов сотрудников. Он вроде полезный, но все тексты получаются какими-то скучными и корпоративными.

В общем сделайте нормально.
```

## task signal

- Requested action: write a post.
- Topic: new employee interests dashboard.
- Quality/tone constraint: avoid boring and corporate-sounding text.
- Implicit production boundary: writing should not start until missing context
  is handled.

## background context

- The user reports that department news are not being read.
- The user is dissatisfied with previous text quality.
- The dashboard is described as "apparently useful", but no concrete benefits
  or source details are supplied.

## noise

- "Что-то у нас опять..."
- "Я уже не знаю, что с этим делать."
- "В общем сделайте нормально."

These fragments show frustration and desired improvement, but they do not add a
separate factual requirement.

## confirmed

- The user wants a post.
- The post is about a new employee interests dashboard.
- The user wants to avoid boring/corporate-sounding text.
- No source material is included in the request.
- No final post should be written in this test.

## inferred

- The task is likely an internal communications writing task.
- The "department news" line may be relevant background for why the post needs
  to be more readable.
- The exact channel is not safely inferable from "post" and "department news".
- The exact audience is not safely inferable from the raw request.

## unknown

- Publication channel.
- Exact audience.
- Dashboard functions and confirmed benefits.
- Required length, structure, and call to action.
- Whether the post needs links, screenshots, launch date, owner quote, or
  approval.
- Whether "new" means already launched or upcoming.
- Source owner and source material.

## assumptions

- It is safe to classify the task as writing/intake for internal communication,
  because the request asks for a post about an employee-facing dashboard.
- It is not safe to assume the channel, audience, dashboard behavior, or
  acceptance criteria beyond the raw request.
- It is safe to carry "avoid boring/corporate tone" as a constraint because the
  user explicitly complains about that quality.

## open questions

- Who is the intended audience?
- Where will the post be published?
- What does the dashboard let employees do?
- Which benefits are confirmed?
- Is there a source description, link, screenshot, release note, or owner input?
- What should readers do after reading?
- Are there tone, brand, length, or approval constraints?

## source status

- Source status: `mentioned but not provided`.
- Source materials present: none.
- Source boundary: the dashboard exists as a user-mentioned topic, but there is
  no active source for claims about features, benefits, metrics, launch date, or
  usage instructions.
- Required next source action: ask for source material or constrain the future
  post to non-specific, user-confirmed statements only.

## acceptance criteria

- `brief.md` captures a task definition without writing the post.
- Facts, inferred context, unknowns, assumptions, and questions are separated.
- No audience, channel, source, feature, benefit, metric, or CTA is invented.
- User frustration is recorded as background/noise, not as a separate factual
  requirement.
- Source status is explicit.

## fantasy check

| Check | Result | Notes |
| --- | --- | --- |
| Invented channel | pass | Channel remains unknown. |
| Invented exact audience | pass | Audience remains unknown; possible employee/internal context is labeled as inferred only. |
| Invented dashboard features | pass | No functions or benefits are fabricated. |
| Emotion promoted to requirement | pass | Frustration is separated as background/noise; tone constraint comes from explicit complaint about boring/corporate texts. |
| Final post written | pass | Only brief/task definition was created. |
| New roles/pipelines/artifact types added to production | pass | No production files changed. |

## editorial conclusion

passed

The new Raw Brief Normalization rule handled this noisy request correctly. The
brief identifies the post task and useful tone constraint while keeping channel,
audience, source details, dashboard benefits, and CTA unknown or questioned
instead of inventing them.
