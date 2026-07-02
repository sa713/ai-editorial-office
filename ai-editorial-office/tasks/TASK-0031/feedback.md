# Feedback

```text
Один feedback не меняет систему автоматически.
```

## metadata

- Task ID: TASK-0031
- Captured date: 2026-06-04
- Captured by: `chief_editor`
- Related final decision: `final_decision.md`
- Related delivered artifact: `sber-editorial-policy.md`

## user reaction

- Short summary: user reported that `Нет` / `Да` example blocks were parsed
  poorly because the two columns were mixed into unreadable text.
- Reaction type: `needs revision`
- User wording or paraphrase: "Плохо распарсил блоки с примерами
  (\"нет\"/\"да\") – вместо текста получилась каша из двух столбцов"

## feedback scope

Relates to:

- understanding the task: no
- structure: yes
- meaning: yes
- tone: no
- format: yes
- facts: no
- process: yes
- usefulness: yes
- other: OCR handling of two-column examples

## signal classification

- Classification: `possible system signal`
- Why: the issue points to a repeatable conversion risk for image-based PDFs
  with two-column comparison tables.
- Similar known signals: none recorded in this task.
- Should this be considered for `/kb/feedback_patterns.md`: no for now; keep
  task-local unless similar conversion failures recur.

## follow-up boundary

- Follow-up needed: yes
- Follow-up type: bounded revision
- Does this reopen the task automatically: no
- Does this change the final decision retroactively: no

## what not to infer

- Do not infer: all OCR conversion rules need system-level changes.
- Do not infer: Sber policy content should become AI-editorial-office policy.
- Do not infer: every future PDF conversion requires the same heavy path.
- System rules changed by this feedback: no
