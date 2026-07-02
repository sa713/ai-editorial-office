# Pilot Preflight Examples

These are demonstration examples only. Old task folders are not changed.

## 1. PROCEED: `TASK-0022`

### source task

- Task: `TASK-0022`
- Evidence: `task-manifest.md` and `orchestration_plan.md`
- Situation: source-constrained rewrite of an existing answer. User requested changing only the answer, preserving facts and meaning.

### preflight decision

| Field | Decision |
| --- | --- |
| Audience | `inferred` |
| Channel or context | `inferred` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `proceed` |

### rationale

Production could start because the source answer existed, the rewrite boundary
was exact, and missing publication approval did not affect editorial rewrite.
The gate would preserve compact mode.

## 2. CONSTRAIN: `TASK-0002`

### source task

- Task: `TASK-0002`
- Evidence: `open-questions.md` and `orchestration_plan.md`
- Situation: article topic was clear, but audience, publication channel, real examples, and approval owner were not confirmed.

### preflight decision before constrained writing

| Field | Decision |
| --- | --- |
| Audience | `unknown` |
| Channel or context | `unknown` |
| Deliverable | `defined` |
| Source boundary | `defined` after research and claims table |
| Success criterion | `inferred` |
| Approval boundary | `unclear` for publication, defined for draft |
| Missing data strategy | `constrain` |

### rationale

The task did not need to ask before drafting because safe narrowing was
available: write for general professional readers, use generic scenarios only,
do not imply publication channel, and mark approval as unresolved.

## 3. ASK: `TASK-0002` publication/use boundary

### source task

- Task: `TASK-0002`
- Evidence: `open-questions.md`
- Situation: human/stakeholder approval and publication channel remained open and did not block draft writing, but would matter before an official publication-ready output.

### preflight decision if production target were official publication copy

| Field | Decision |
| --- | --- |
| Audience | `unknown` |
| Channel or context | `unknown` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `unclear` for publication use |
| Approval boundary | `unclear` |
| Missing data strategy | `ask` |

### smallest question

```text
Для какого канала и аудитории готовим публикационную версию, и кто должен подтвердить её перед выпуском?
```

### rationale

The same task can proceed as a constrained draft, but official publication copy
would need a user decision. Preflight prevents the system from silently treating
draft readiness as publication readiness.

## 4. BLOCK: `TASK-0020` source availability condition

### source task

- Task: `TASK-0020`
- Evidence: `orchestration_plan.md`
- Situation: visual sketchnote production depended on reading the source PDF. The plan already said to stop or escalate if the PDF cannot be read.

### preflight decision if the source PDF were absent or unreadable

| Field | Decision |
| --- | --- |
| Audience | `confirmed` |
| Channel or context | `confirmed` |
| Deliverable | `defined` |
| Source boundary | `unclear` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `block` |

### blocking reason

The system cannot create a source-grounded visual summary when the source cannot
be read. Proceeding would invite invented meaning or a direct visual shortcut.

## compatibility conclusion

- `PROCEED` keeps compact work compact.
- `CONSTRAIN` avoids unnecessary questions when a safe scope exists.
- `ASK` is reserved for missing decisions that materially affect the requested production target.
- `BLOCK` prevents production when the source boundary is absent or unsafe.

