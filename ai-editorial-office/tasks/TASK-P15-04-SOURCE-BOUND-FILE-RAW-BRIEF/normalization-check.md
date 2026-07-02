# Normalization Check

## test metadata

- Test ID: P1.5-04
- Task ID: TASK-P15-04-SOURCE-BOUND-FILE-RAW-BRIEF
- Role applied: intake_agent
- Rule tested: Raw Brief Normalization
- Raw request type: source-bound file request
- Source file read: no
- New answer created: no
- Draft or answer structure created: no
- Production files changed: no

## raw request

```text
Перепиши ответ на вопрос из файла task.md.

Вопрос не менять.
```

## task signal

- Requested action: rewrite an answer.
- Source: `task.md`.
- Object of rewriting: answer to a question in the file.
- Explicit constraint: do not change the question.
- Source dependency: production cannot proceed without the file content.

## background context

- None supplied beyond the file-dependent rewrite request.

## noise

- None. The request is short and source-bound, not noisy.

## confirmed

- The user wants an answer rewritten.
- The answer is in or derived from `task.md`.
- The question must not be changed.
- The content of `task.md` has not been provided or verified in this test.

## inferred

- The future task is source-bound rewrite/editing.
- `task.md` likely contains a question and an answer, but the exact content is
  unknown.
- Intake should stop before production until the source is available.

## unknown

- The question in `task.md`.
- The current answer in `task.md`.
- The file topic.
- The facts in the file.
- The desired rewrite style, tone, length, and quality target.
- Source-specific constraints beyond "do not change the question".
- Whether `task.md` contains one question/answer pair or multiple items.
- Whether formatting may change.

## assumptions

- The named file is required source material, not optional context.
- The future rewrite must preserve the question exactly.
- No assumption is safe enough to produce or shape an answer.

## open questions

- Is `task.md` available, and where is it?
- Which question/answer should be used if the file contains multiple items?
- What exactly is the current question?
- What exactly is the current answer?
- What should improve in the rewritten answer?
- Are there constraints in the file that must be preserved?
- May formatting around the answer change?

## source status

- Source status: `mentioned but not provided or verified`.
- Source materials present: none in the active test packet.
- Active source: none.
- Source boundary: the file name is known, but file contents are not active
  evidence.
- Required next source action: provide or activate `task.md` before any rewrite,
  draft, or answer structure is created.

## acceptance criteria

- Future answer acceptance criteria: `unknown` until source content and rewrite
  goal are available.
- Confirmed future constraint: the question must not be changed.
- Normalization acceptance criteria:
  - do not create a new answer;
  - do not create a draft answer;
  - do not create an answer structure;
  - do not invent file content, question, answer, topic, style, constraints, or
    facts;
  - mark source status explicitly.

## fantasy check

| Check | Result | Notes |
| --- | --- | --- |
| Invented question | pass | No question text was created. |
| Invented answer | pass | No answer text was created. |
| Invented file topic | pass | Topic remains unknown. |
| Invented rewrite style | pass | Style and tone remain unknown. |
| Invented source constraints | pass | Only the explicit "question must not change" constraint is recorded. |
| Invented document facts | pass | No facts from `task.md` were fabricated. |
| Treated file as active source | pass | Source status is not provided/verified. |
| Created draft or structure | pass | No draft, answer, or answer structure was created. |

## editorial conclusion

passed

Raw Brief Normalization handled the file-dependent request correctly. It
captured the rewrite operation and the "do not change the question" constraint,
while keeping `task.md` inactive until provided or verified and avoiding any
invented question, answer, topic, style, source constraints, or document facts.
