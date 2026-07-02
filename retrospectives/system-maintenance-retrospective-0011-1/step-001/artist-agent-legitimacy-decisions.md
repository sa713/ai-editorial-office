# Artist Agent Legitimacy Decisions

## Primary Decision

Artist Agent is now a legal non-MVP extension role for illustration-to-text tasks.

It is not part of the ordinary MVP role set and does not become available for every task.

## Default Rule

Non-MVP extension roles remain forbidden by default.

They may be used only when:

- `AGENTS.md` explicitly legalizes the role;
- the task matches the legalized role scope;
- the role-specific prerequisites are met.

## Artist Agent Scope

Artist Agent may be assigned only when:

- the task explicitly requires an illustration to a text;
- approved `visual_concept.md` exists;
- approved `illustration_brief.md` exists.

## Artist Agent Is Not

Artist Agent is not:

- a semantic editor;
- a reviewer;
- a writer;
- a designer;
- a comic artist;
- a presentation designer;
- a universal production role.

## Ordinary Tasks

The MVP agent set remains unchanged for ordinary text tasks.

Artist Agent must not be assigned to normal article, social, UX, research, review, finalization, or governance work unless the task separately has the approved visual-branch artifacts and explicitly requires illustration.

## Pipeline Decision

Pipelines still default to MVP roles.

Their wording now allows explicitly legalized non-MVP extension roles under `AGENTS.md` conditions, instead of blocking every extension role unconditionally.
