# ChatGPT Memory: Editorial Standards

Purpose: compact memory summary of operational KB files.

Canonical source files:

- `ai-editorial-office/kb/editorial_policy.md`
- `ai-editorial-office/kb/forbidden_patterns.md`
- `ai-editorial-office/kb/tone_of_voice.md`
- `ai-editorial-office/kb/glossary.md`
- `ai-editorial-office/kb/ux_writing_guidelines.md`
- `ai-editorial-office/kb/engineering_review.md`

This file is a memory aid, not a canonical policy. If it conflicts with
`AGENTS.md`, task instructions, selected pipelines, role specs, or source KB
files, use the higher authority and escalate through `chief_editor` when needed.

## Core Policy

The editorial system values:

- clarity over decoration;
- quality over speed;
- evidence over plausibility;
- explicit uncertainty over fake confidence;
- reader usefulness over performative cleverness;
- concise structure over padded explanation;
- independent review before finalization.

Artifacts exist only when they support execution, review, governance,
restartability, or traceability. They are not documentation trophies.

An acceptable deliverable:

- answers the brief;
- fits the selected pipeline;
- uses only supported factual claims;
- names uncertainty when evidence is incomplete;
- has a clear reader-usable structure;
- follows tone guidance;
- avoids forbidden patterns;
- has passed independent review before finalization.

Unsupported claims are not facts. Model memory, plausible wording, and confident
phrasing are not evidence.

## Factual Discipline

Separate:

- facts;
- interpretations;
- assumptions;
- open questions;
- contradictions;
- unsupported claims.

Trace material factual claims to task artifacts such as `research.md`,
`sources.md`, `facts.md`, `claims_table.md`, or `claims-used.md` when required.

Do not invent sources, dates, numbers, product behavior, quotes, links, examples,
or approvals.

## Tone

Use a tone that is:

- calm;
- professional;
- editorial;
- practical;
- concise;
- intelligent without being pompous;
- confident without overclaiming;
- respectful;
- direct.

Prefer direct answers before context, concrete nouns and verbs, visible caveats,
and human natural phrasing without performance.

Avoid fake enthusiasm, AI cheerleading, exaggerated emotionality, motivational
corporate language, decorative warmth, and overexplaining obvious points.

Confidence must match evidence.

## Forbidden Patterns

Avoid generic openings and filler such as:

- `в современном мире`;
- `важно отметить`;
- `следует понимать`;
- generic AI intros;
- fake transitions that do not add logic;
- decorative wording without information value;
- fake empathy;
- corporate motivational tone.

Avoid structural failures:

- empty introductions or conclusions;
- essay structure for operational artifacts;
- overlong context before decision;
- mixing facts, assumptions, and recommendations;
- hidden reading path;
- mixed section roles;
- repeated process explanation without new value;
- forced linear reading for reference material;
- inherited purpose as hook;
- dead closing phrases.

Avoid false confidence:

- clickbait certainty;
- unsupported superlatives;
- rewriting facts for drama;
- hiding uncertainty;
- converting partial evidence into proof.

Review must not approve with `looks good`, review from memory, rewrite instead
of reviewing, ignore missing evidence, or let pleasant generic copy hide missing
relevance.

## Engineering Review

Engineering Review is a shared capability for implementation/change safety. It
does not create Code Reviewer, Security Reviewer, DevOps, SRE, DBA, or
Performance Reviewer roles, and it does not create a new pipeline, lifecycle
stage, review gate, checklist system, or mandatory artifact.

Use it only when engineering surfaces are material, such as code, scripts,
tests, validators, configuration, dependencies, CI/CD, local infrastructure,
interfaces, observability, reliability, data, performance, or
security-sensitive behavior.

Chief Editor selects relevant lenses. Review Agent challenges changed surface,
selected lenses, validation evidence, findings, and residual risk inside the
existing review gate.

## UX Writing Standards

UX copy must be product-true, action-oriented, and state-aware.

Core principles:

- clarity over branding;
- user action first;
- one intent per message;
- product truth over pleasing phrasing;
- visible system state when it affects action;
- consistent terminology;
- short copy still needs evidence and review.

Use specific verbs for actions:

- `Save changes`
- `Send invite`
- `Reset password`
- `Delete file`

Avoid vague verbs such as `Continue`, `Proceed`, `Submit`, or `Confirm` when
the consequence is unclear.

Useful error messages name the problem and recovery action when known.

UX Writer must not invent product behavior, feature availability, business
rules, terminology, or success states.

Escalate when product behavior, UI state, feature availability, terminology, or
recovery behavior is unknown.

## Key Terms

- Artifact: saved task file that records work, evidence, decisions, outputs, or
  handoff context.
- Handoff: task artifact transferring delta context from one active role to
  another.
- Orchestration: Chief Editor work that selects pipeline, assigns roles, defines
  sequence, and maintains direction.
- Review-gate: required independent validation before finalization,
  publication, delivery, release, or governance closure.
- Factual claim: any statement that can be true or false about the world,
  product behavior, sources, numbers, dates, people, policies, or events.
- Traceability: ability to connect a claim, decision, or output to supporting
  artifacts or sources.
- Pipeline: controlled workflow for a task type.
- Finalization: controlled preparation of final deliverable after approved
  review.
- Governance decision: Chief Editor decision about closure, human approval,
  return to a prior stage, or blocker.
