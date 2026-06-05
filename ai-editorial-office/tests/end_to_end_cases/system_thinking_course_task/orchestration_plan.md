This is a synthetic/sanitized end-to-end case. It is not a real task folder and does not contain real course source files, confidential methodology, internal training materials, participant data, client data, or restricted content.

# Orchestration Plan

## Editorial Entry

- active orchestrator: chief_editor
- task type: internal task/post wording
- selected pipeline: social
- process depth: compact with source summary
- assigned roles: chief_editor, writer_agent, review_agent, final_editor
- client_profile: none
- risk mode: standard

## Preflight Gate

- decision: constrain
- expected decision: constrain

Reason: the goal is clear, but the task references a source file. Work must be constrained to the supplied course description and the sanitized `source_summary.md`; the writer must not invent course modules, methodology content, or training materials beyond the attachment.

The constraint is not about security risk. It is about source discipline and preventing invented course structure.

## Why Not Ask, Proceed, Or Block

- Not `ask`: the brief is sufficient to prepare a first safe internal task text.
- Not `proceed`: unrestricted drafting could invent module names, course content, or methodology details not present in the sanitized case.
- Not `block`: the case can proceed because the employee task may refer to the attached course description without committing the source file.

## Compact Execution Rationale

Use compact execution with source summary because this is a short internal task/post with one supplied source boundary. Required governance is preserved through manifest, status, plan, source summary, draft, review, final, and final decision.

## Compact-Evidence Rationale

Research evidence mode: compact-evidence.

The case uses one task-local supplied source in a sanitized way. The relevant evidence is limited to the course title, the fact that the attachment contains course value, target audience, and module breakdown, and the work requested: complete theoretical module content and develop practical work.

## Source/Provenance Decision

Expected source/provenance decision: task-local supplied source, not external import.

- Do not add the original source to `kb/`, `learn/`, `tasks/`, or the repo.
- Do not commit the original source file.
- Use `source_summary.md` as the sanitized task-local evidence artifact.
- Do not create source notes beyond this sanitized summary for the test case.

## Review Requirement

`final.md` may be created only after independent `review.md` records outcome: approved.
