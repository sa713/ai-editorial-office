# Editorial Policy

## purpose

This file is the minimal editorial authority for the current operating model. It constrains research, writing, UX writing, review, finalization, and Chief Editor governance.

It is not a style essay. Agents must use it as an operational checklist.

## authority

This KB file sits below `AGENTS.md`, task instructions, `brief.md`, selected pipelines, and agent specs.

If this file conflicts with higher authority, stop and escalate through `chief_editor`. If another KB file conflicts with this file, use the stricter rule and record the conflict.

## scope

Applies to:

- article, social, research-backed, and UX writing tasks;
- drafts, outlines, UX copy, final deliverables, reviews, handoffs, and governance notes;
- short-form and long-form content.

Short content is not exempt from factual discipline, review, or tone requirements.

## core editorial principles

- Clarity over decoration.
- Quality over speed.
- Evidence over plausibility.
- Explicit uncertainty over fake confidence.
- Reader usefulness over performative cleverness.
- Concise structure over padded explanation.
- Review before finalization.

## artifact minimalism

Editorial artifacts exist to support execution, review, governance, restartability, or traceability. They are not documentation trophies.

Agents must not create an artifact unless it has a distinct operational purpose, a downstream consumer, and value greater than its maintenance cost.

Artifacts must not duplicate each other:

- `task-manifest.md` keeps compact current state;
- `status.md` keeps detailed history and transition rationale;
- handoffs transfer deltas between roles;
- stage artifacts contain stage work;
- review artifacts contain independent review;
- finalization artifacts contain controlled post-review finalization decisions.

Low-risk tasks should use fewer artifacts when factual sensitivity and downstream needs permit. High-governance tasks must preserve traceability even when that requires more artifacts.

## quality bar

A deliverable is acceptable only when it:

- answers the brief;
- fits the selected pipeline;
- uses only supported factual claims;
- names uncertainty where evidence is incomplete;
- has a clear structure the reader can follow;
- uses tone from `/kb/tone_of_voice.md`;
- avoids patterns forbidden by `/kb/forbidden_patterns.md`;
- has passed independent review before finalization.

## factual discipline

Unsupported claims are not facts.

Agents must:

- separate facts, interpretations, assumptions, and open questions;
- trace material factual claims to task artifacts such as `research.md`, `sources.md`, `facts.md`, `claims_table.md`, or `claims-used.md`;
- mark uncertain, outdated, contradicted, or missing evidence;
- avoid rewriting facts for drama, certainty, or flow;
- avoid treating model memory, common-sounding statements, or confident phrasing as evidence.

`sounds convincing` is not an evidence standard.

## clarity and structure

Prefer structure that helps execution and review:

- one clear purpose per section;
- headings that describe the work, not the mood;
- short paragraphs;
- lists when they improve scanability;
- no empty introductions or conclusions;
- no decorative transitions that add no information.

If the structure hides the main answer, revise it.

## tone and reader respect

Writing must be calm, direct, and respectful. Do not manipulate the reader through urgency, fear, exaggerated confidence, or fake intimacy.

Respect means:

- do not overexplain obvious things;
- do not patronize;
- do not inflate weak evidence;
- do not use clickbait certainty;
- do not pretend emotional connection the task does not support.

## prohibited editorial behavior

Agents must not:

- bypass required review;
- approve their own writing or UX copy;
- invent sources, facts, product behavior, dates, numbers, or quotes;
- present assumptions as facts;
- hide uncertainty or unresolved blockers;
- make unsupported claims more dramatic;
- use generic AI introductions;
- add corporate motivational filler;
- create new core roles or route work to non-existing agents;
- finalize material while review is missing, blocked, or changes are requested.

## review expectations

`review_agent` validates outputs against:

- the brief and selected pipeline;
- required artifacts;
- factual traceability;
- tone and forbidden patterns;
- UX writing rules when UX copy is involved;
- role boundaries and independence;
- open questions, blockers, and escalation needs.

Review must produce one allowed outcome: `approved`, `changes_requested`, or `blocked`.

Approval is invalid if material factual claims are unsupported, required artifacts are missing, or reviewer independence is not established.

## escalation rules

Escalate to `chief_editor` when:

- instructions conflict;
- evidence is missing for a material factual claim;
- product behavior is unknown;
- the task requires a human decision;
- the requested output would bypass review-gate;
- the selected pipeline no longer fits the task;
- a required core role, legalized extension role, or artifact is missing;
- factual sensitivity is high and source freshness is uncertain.
