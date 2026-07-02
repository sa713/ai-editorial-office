# Brief

## raw request summary

User asks to rewrite an answer to a question from `task.md` and explicitly says
the question must not be changed. In this test, the source file is not read and
no new answer, draft, or answer structure is created.

## user goal

- confirmed: rewrite an existing answer from `task.md`;
- confirmed: keep the question unchanged;
- unknown: what the question says, what the answer says, why the answer needs
  rewriting, and what quality target the rewrite should meet.

## audience / reader

- confirmed: unknown;
- inferred: none safe enough to use;
- unknown: who will read or evaluate the rewritten answer.

## expected artifact

- confirmed: rewritten answer, in a future production task;
- inferred: source-bound rewriting/editing task after source access;
- unknown: final format, length, style, tone, and delivery channel.

## source status

- supplied sources: `task.md` is named by the user;
- source status: `mentioned but not provided or verified`;
- source boundary: source content is unavailable in this normalization test;
  the question, current answer, topic, facts, and source constraints are
  unknown until `task.md` is available and explicitly used.

## constraints

- Do not create a new answer.
- Do not create an answer draft.
- Do not create an answer structure.
- Do not invent the contents of `task.md`.
- Do not invent the question.
- Do not invent the existing answer.
- Do not perform the rewrite before source status is active.
- Preserve the question unchanged in the future task.

## explicit requirements

- Rewrite the answer from `task.md`.
- Do not change the question.

## assumptions

- `assumption`: the file `task.md` should contain at least one question and an
  answer, because the user refers to "ответ на вопрос из файла".
- `assumption`: the future task is a source-bound rewrite/edit task.
- No assumption is safe enough to describe the file topic, facts, question,
  answer, or desired style.

## open questions

- Where is `task.md` and is it available to the editorial office?
- Does `task.md` contain exactly one question/answer pair or multiple items?
- What is the current question?
- What is the current answer?
- What rewrite goal is intended: clarity, brevity, tone, correctness,
  structure, style, or something else?
- Are there source facts, constraints, grading criteria, or forbidden changes in
  `task.md`?
- Should only the answer be changed, or may formatting around it change?

## acceptance criteria

- Future rewrite acceptance criteria: source-bound and `unknown` until
  `task.md` is available.
- Confirmed future constraint: the question must remain unchanged.
- Intake acceptance for this test: the normalized task definition must not
  invent the question, answer, topic, style, facts, source constraints, or
  rewrite criteria.

## suggested task type / pipeline

- Suggested task type: source-bound rewrite/editing task.
- Suggested pipeline: not selectable for production until `task.md` source
  status is active and the Chief Editor confirms routing.
- Missing data strategy: `block` or `ask` before production, because the source
  file is required.

## risks

- Any rewrite now would fabricate the question and answer.
- Treating `task.md` as active without confirming availability would violate
  source-status rules.
- Inferring style or topic from the filename would create unsupported
  requirements.
- Changing the question in the future would violate the user's explicit
  constraint.
