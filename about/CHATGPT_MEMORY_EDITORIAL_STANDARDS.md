# ChatGPT Memory: Editorial Standards

Purpose: compact memory summary of operational KB files.

Canonical source files:

- `ai-editorial-office/kb/editorial_policy.md`
- `ai-editorial-office/kb/forbidden_patterns.md`
- `ai-editorial-office/kb/tone_of_voice.md`
- `ai-editorial-office/kb/glossary.md`
- `ai-editorial-office/kb/ux_writing_guidelines.md`
- `ai-editorial-office/kb/professional_analysis.md`
- `ai-editorial-office/kb/professional_communication.md`
- `ai-editorial-office/kb/engineering_review.md`
- `ai-editorial-office/kb/editorial_learning_framework.md`
- `ai-editorial-office/kb/domain_knowledge_pack_standard.md`
- `ai-editorial-office/kb/software_architecture_domain_pack.md`
- `ai-editorial-office/kb/devsecops_domain_pack.md`
- `ai-editorial-office/kb/cybersecurity_domain_pack.md`
- `ai-editorial-office/kb/ai_engineering_domain_pack.md`

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

## Professional Analysis

Professional Analysis is a shared capability for structured interpretation,
synthesis, recommendation building, implications, analytical judgment, and
decision-ready analytical communication.

It does not create an Analyst, Consultant, Business Analyst, Policy Analyst,
Product Strategist, Intelligence Analyst, or Technology Analyst role, and it
does not create a new pipeline, lifecycle stage, review gate, consulting
framework, or mandatory artifact.

Use it only when analytical product quality is material, such as situation
assessment, synthesis brief, options/recommendation memo, business or needs
analysis, policy or impact analysis, product discovery analysis, technology
assessment, or executive decision brief.

Analytical Reasoning owns the reasoning moves. Professional Analysis owns the
decision-ready analytical product shape. Architecture Review and Engineering
Review remain separate capabilities for design fitness and implementation
change safety.

## Professional Communication

Professional Communication is a shared capability for professional reader
transfer: message architecture, executive briefs, technical explanations,
recommendation or ask presentation, information density, reader path,
actionability, and caveat-preserving communication.

It does not create a Professional Communicator, Technical Writer, Executive
Writer, Policy Writer, Documentation Writer, or Recommendation Writer role, and
it does not create a new pipeline, lifecycle stage, review gate, style system,
UX-copy owner, or mandatory artifact.

Use it only when communication transfer quality is material, such as an
executive brief, technical explanation, implementation handoff, policy or
stakeholder memo, research/evidence communication, dense source compression,
recommendation presentation, or actionability failure.

Audience & Outcome Alignment owns who the artifact is for and what outcome it
must enable. Professional Analysis owns analytical judgment and recommendation
basis. Professional Communication owns how the approved meaning, evidence,
caveats, uncertainty, recommendation, and next action transfer to the reader.

## Knowledge Evolution

Knowledge Evolution is the bounded capability inside the Editorial Learning
Framework for deciding what happens to reusable learning after work completes.

It covers task-local learning notes, learning candidates, pattern candidates,
canon-update candidates, stale/conflicting knowledge challenges,
correction/retirement candidates, and `/about` memory disposition. It does not
create a Knowledge Curator, Canon Manager, Historian, new pipeline, lifecycle
stage, review gate, automatic canon promotion, or mandatory artifact.

Promotion beyond task-local notes needs a source-evidence chain, scope, owner,
disposition, and review path. `/about` is only a synchronized memory export,
not canon.

Actual post-delivery feedback remains classified through the Customer Feedback
Loop; observed completed-work outcomes without a customer reaction enter the
Learning Framework directly. When future use is material, preserve the saved
signal, evidence pointer, observed outcome, affected area, applicability,
contradictions, learning disposition, existing owner, bounded action, and
explicit non-promotion. Feedback classification and learning disposition are
linked but distinct decisions. One anecdote normally stays task-local, is
rejected, or is deferred; no score or count promotes it automatically.

## Evaluation Signals

Evaluation Signals are optional advisory views over saved evidence for a
material Project Lead, review, governance, or canonical-owner question. They do
not create a new capability, framework, store, dashboard, telemetry layer,
role, pipeline, lifecycle stage, review gate, task status, score, KPI, target,
ranking, maturity level, or mandatory artifact.

When material, preserve the decision question, observation, evidence pointers,
bounded comparison window, denominator or exposure opportunity for counts,
missing cases, interpretation, alternatives and contradictions, confidence,
existing owner, optional human consideration, and explicit non-decision.
Activity and activation frequency never prove quality or usefulness. Keep
Domain Pack value, architecture drift, evidence sufficiency, release value,
maintenance burden, learning promotion, contradictory signals, and release
acceptance qualitative and human-reviewed.

Chief Editor may assemble the view inside an existing artifact. Review Agent
challenges evidence, comparability, missing cases, noise, contradictions,
proportionality, and non-decision. Project Lead or the current canonical owner
remains the decision authority. No release, canon, backlog, roadmap, memory,
Domain Pack, capability, or owner changes automatically.

## Domain Knowledge Packs

Domain Knowledge Packs are source-backed, bounded, maintained context packages
for a named domain. They help roles use domain terminology, evidence
expectations, risks, review questions, and stale/update rules without turning
domain expertise into loose facts or hidden policy.

They do not create roles, capabilities, pipelines, lifecycle stages, review
gates, policy owners, client profiles, task status models, mandatory ordinary
task artifacts, or automatic canon-promotion paths.

Activate a pack only when domain context materially changes evidence depth,
terminology, risk handling, review focus, or output quality. Record the active
pack, activation reason, relevant sources/sections, confidence limits,
boundary limits, stale-if triggers, and stop conditions in existing task
artifacts. Review active pack use inside the existing review gate.

When actual pack use materially affects a result, an existing task artifact may
also record sections or sources actually used, the affected decision/artifact/
review finding, observed benefit or burden, evidence and confidence,
unnecessary complexity, and Knowledge Evolution disposition. This effect note
is conditional; activation is not proof of value and never changes a pack
automatically.

Current accepted, active packs: Software Architecture Domain Knowledge Pack,
DevSecOps Domain Knowledge Pack, Cybersecurity Domain Knowledge Pack, and AI
Engineering Domain Knowledge Pack.

Use the Software Architecture pack only for architecture-sensitive tasks where
software architecture context materially changes evidence depth, terminology,
risk handling, review focus, or output quality. It supports reasoning about
architectural decisions, drivers, quality attributes, styles, patterns,
boundaries, coupling, tradeoffs, risks, evidence, and review questions. It does
not own Architecture Review, Engineering Review, roles, pipelines, policies,
task statuses, review outcomes, or mandatory artifacts.

Use the DevSecOps pack only for secure delivery, CI/CD, automation,
configuration, supply-chain risk, deployment-boundary, validation-evidence, or
operational-security tasks where DevSecOps context is material. It supports
Engineering Review with source-backed context and review questions, but does
not own Engineering Review, cybersecurity policy, roles, pipelines, task
statuses, review outcomes, or mandatory artifacts.

Use the Cybersecurity pack only for security-sensitive analysis, threat
understanding, defensive recommendations, secure design, controls,
mitigations, assurance evidence, residual-risk interpretation, and safety-aware
review context where cybersecurity context is material. It supports
Engineering Review, Architecture Review, Professional Analysis, and
Professional Communication without owning those capabilities, cybersecurity
policy, security approval, incident response, roles, pipelines, task statuses,
review outcomes, or mandatory artifacts.

Use the AI Engineering pack only when AI-specific system context materially
changes evidence, terminology, risk, review focus, or output quality. It covers
AI-enabled system boundaries, model/provider fit, prompts and instructions,
structured outputs, RAG, data quality, evaluation, reliability and monitoring,
human oversight, defensive safety, tool/agentic workflows, and AI-assisted
engineering. It does not own Engineering Review, Cybersecurity, DevSecOps,
Software Architecture, Professional Analysis, roles, pipelines, policy,
approval, review outcomes, or mandatory artifacts. Current product/provider
behavior requires task-time source refresh.

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
