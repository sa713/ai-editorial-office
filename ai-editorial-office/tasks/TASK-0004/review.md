# Review

Task ID: `TASK-0004`

Owner: `review_agent`

Stage: `review`

Review verdict: `approved`

## checked artifacts

- `brief.md`
- `orchestration_plan.md`
- `draft.md`
- source file: `source-draft.md`
- governance update: `SYSTEM-MAINTENANCE-0001/final_decision.md`
- failure patterns: `editorial_knowledge/50_editorial_failure_patterns.md`

## review outcome

The revised instruction is approved for finalization.

It preserves the source structure, but repairs the largest operational failures:

- action routes now appear before platform explanation;
- terms are limited to terms the reader needs to act;
- task flow has one clear end-to-end sequence;
- Author and Executor steps are separated without contradicting the overview;
- unsupported `Инициатива` distinction is removed;
- unfinished author note in `Мои задачи` is replaced with usable guidance;
- dispute handling now tells the reader when and how to escalate.

## findings

### P1 fixed: unfinished operational section

Source had an internal note in `2.4. Раздел «Мои задачи»`, which would break user trust and stop reading. Draft replaces it with a compact purpose and checks for that section.

### P1 fixed: undefined term

Source had `Инициатива` with `?`. Draft does not invent a separate definition. It keeps `Идея` as the supported term.

### P2 fixed: answer delay

Source opened with platform purpose and pilot context before telling the reader what they can do. Draft opens with available actions and keeps pilot context short.

### P2 fixed: sequence ambiguity

Source sometimes implied completion differently for Author and Executor. Draft makes ownership explicit: Executor reports completion; Author checks and moves accepted task to `Done`.

### P2 fixed: action ownership

Source said potential executors comment and Author selects, but the role boundary could still be missed. Draft states that a comment is not automatic assignment.

### P2 fixed: dead dispute guidance

Source said only to contact curators. Draft gives conditions for escalation and what to include.

## requested review answers

### Where instruction is still friction-heavy

- Exact UI behavior remains partly assumed: notifications, filters, and card visibility should be verified against Taska.
- `Мои задачи` remains general because the source did not specify exact filters or tabs.

### Which actions remain non-obvious

- Who exactly counts as `Модераторы` is not named.
- What status or column an idea has after moderator review is not fully specified.
- Whether Author or Moderator creates the initial idea card type is not fully specified by the source.

These do not block finalization because adding them would require product/process facts not present in the source.

### Where text sounds correct but could be operationally weak

- `Дальнейший статус идеи отображается в карточке` is correct but depends on actual status visibility.
- `Проверьте фильтры доски` is useful but generic without concrete filter names.

### Which parts are likely to be skipped

- Terms section may be skipped by readers who go straight to their role.
- Process overview may be skipped by users who only need Author or Executor steps.

This is acceptable because role-specific sections repeat the necessary actions.

### Where text explains the system instead of helping the reader act

The revised opening keeps one short system sentence, then moves into actions. No major system-explanation block remains before user need.

### Unnecessary editorialization

None found. The draft is operational and restrained. It does not add motivation, campaign language, HR warmth, or platform philosophy.

## residual risk

The final instruction should be product-owner checked before release if exact Taska labels, notification behavior, or moderator ownership matter. This is not an editorial blocker.
