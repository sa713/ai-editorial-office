# Research

Task ID: `TASK-0001`

Owner: `research_agent`

## research scope

Create a traceable evidence base for an internal-portal article about how AI can support editors and UX writers in product teams.

Covered:

- practical, non-hype claims about AI support for editors and UX writers;
- drafting support;
- structure checks;
- adaptation help;
- weak-spot detection;
- distinction between AI assistance and editorial responsibility;
- safe and unsafe claims;
- limitations and caveats.

Not covered:

- article draft;
- outline;
- review;
- finalization;
- organization-specific policies or examples, because none were supplied.

## executive summary

Research is sufficient for Chief Editor to route the task toward writing after confirming the plan. The safe article thesis is:

```text
AI can support editors and UX writers as a working assistant for drafts, variants, structure checks, adaptation, and issue spotting, but humans remain responsible for context, factual accuracy, tone, product truth, and final editorial decisions.
```

The evidence supports practical "can help" claims. It does not support strong claims such as "AI replaces editors," "AI always saves time," or "AI improves quality by itself."

## key findings

- AI-assisted drafting, rewriting, summarizing, and adaptation are supported as common content-related use cases by checked sources. See F1, F2, C1, C2, C12.
- UX-specific sources support using AI for content editing, microcopy variants, tone adjustment, summarization, trimming, expanding, rewording, and proofreading. See F2, C12.
- Structure checking and weak-spot detection are safer as "AI can generate options or surface possible gaps" than as claims that AI validates structure or reliably catches every issue. See F3, C3, C4.
- Human editorial responsibility remains required because AI output can be wrong or unsupported, and because AI use needs governance, risk management, and review. See F6, F7, C5, C6, C7.
- Organization-specific examples are unavailable. Writer Agent should either avoid internal claims or frame examples as generic/illustrative. See F8, C11.

## background context

The article is for editors, UX writers, and product teams. The topic is not whether AI should replace editorial work; the brief explicitly rejects that angle. The useful frame is operational:

- AI can reduce blank-page friction by generating first versions or alternatives;
- AI can help compare variants and adapt texts for audience, format, or tone;
- AI can act as a reviewer-like prompt for possible weak points, but not as the actual Review Agent;
- editors and UX writers still own judgment, context, product truth, factual checking, and tone.

This aligns with the local editorial system: research is separate from writing, writing is separate from review, and finalization cannot bypass independent review.

## confirmed facts

| Fact ID | Summary | Source |
| --- | --- | --- |
| F1 | AI tools are documented as useful for content-related tasks such as generating drafts, rewriting, summarizing, and repurposing content. | S1, S2, S3 |
| F2 | NN/g lists UX-specific generative AI tasks including content editing, UX microcopy, summarizing, changing tone, trimming or expanding text, rewording, and proofreading. | S3 |
| F6 | NIST AI RMF frames AI risk management as governance, mapping, measuring, and managing risks. | S6 |
| F7 | OpenAI states ChatGPT can make mistakes and important information should be checked. | S7 |
| F8 | No internal examples, policies, or product-team practices were supplied in task artifacts. | brief.md, open-questions.md, orchestration_plan.md |

## interpretations

| Interpretation | Evidence basis | Draft-use guidance |
| --- | --- | --- |
| AI is best framed as an assistant for editorial process steps, not as an autonomous editor. | F1, F2, F6, F7, C5 | Safe and central. |
| Structure checks and weak-spot detection should be framed as generating prompts for human review. | F3, C3, C4 | Use cautious language: "can help notice" or "can suggest where to look." |
| Generic examples are acceptable if the draft does not claim they reflect the user's organization. | F8, C11 | Use examples like "turn a release note into a shorter product update" only as illustrative. |

## assumptions

| Assumption | Reason | Risk | Needs verification |
| --- | --- | --- | --- |
| Writer Agent may use generic workflow examples. | No internal examples supplied; Chief Editor deferred generic examples. | Medium: article may feel less specific. | `yes`, if organization-specific relevance is required. |
| Vendor-specific examples should be avoided unless needed. | Brief requests calm, practical, non-hype framing. | Low. | `no` |
| The article can discuss "AI tools" generally rather than naming specific products. | Research scope is about editorial support, not product comparison. | Low. | `no` |

Assumptions must not be promoted to facts.

## contradictions

| Contradiction | Impact | Handling |
| --- | --- | --- |
| None found among checked sources for the narrow claim that AI can support drafting, adaptation, and ideation-like editorial tasks. | No blocker. | Continue with caveats and avoid stronger claims. |
| The task brief says AI does not replace editors; some public AI marketing may imply broad automation benefits. | Potential tone and accuracy risk. | Do not use replacement rhetoric or unsupported automation claims. |

## gaps

| Gap | Blocks writing | Impact | Suggested resolution |
| --- | --- | --- | --- |
| No internal AI policy, examples, or product-team practice notes were supplied. | `no` | Limits specificity. | Writer should use generic examples or Chief Editor may ask user for internal examples before writing. |
| No source was checked that proves editor-specific time savings for this exact audience. | `no` | Blocks numeric or absolute productivity claims. | Writer must avoid numbers and absolutes. |
| No organization-specific risk appetite or publication approval rule is known. | `no` | May affect final governance, not research. | Chief Editor should reassess before finalization. |

## implications for writing

Writer Agent can safely build the draft around these points:

- AI can help start drafts, variants, summaries, and transformations.
- AI can help compare structures, spot possible gaps, and generate questions for review.
- UX writers can use AI for microcopy variants, tone changes, shortening, expansion, and rewording, but must verify product behavior and state.
- Editors remain responsible for source checking, meaning, product truth, tone, risk, and final decisions.
- AI should be presented as part of an editorial workflow with review, not as an independent authority.

Writer Agent must avoid:

- statistics unless directly copied from and attributed to a checked source;
- claims that AI always saves time or improves quality;
- organization-specific examples;
- claims that AI can replace editors, UX writers, reviewers, or final governance.

## do-not-say list

- `AI replaces editors.`
- `AI can write final copy without review.`
- `AI always saves time.`
- `AI automatically improves text quality.`
- `AI understands the product context better than the team.`
- `AI catches every weak spot.`
- `Our teams already use AI in this way.` unless the user supplies internal evidence.
- Vendor-specific superiority claims.
- Generic hype openings such as `в современном мире` or "AI changes everything."

## recommended angle options

These are research-informed options, not final editorial direction:

| Option | Rationale | Risk |
| --- | --- | --- |
| "AI as an editorial second pair of hands" | Matches the brief: assistance without replacement. | Could become too metaphorical; keep practical. |
| "Where AI helps in the product-content workflow" | Lets Writer structure the article by tasks: draft, structure, adapt, check. | Needs clear examples and caveats. |
| "AI is useful before and between editorial decisions" | Emphasizes that humans own final judgment. | May be too abstract unless grounded in examples. |

## sufficiency assessment

Research local outcome: `research_ready_for_writing`

Recommended operational status: `planning`

Recommended next role: `chief_editor`

Reason:

- Required research artifacts are present.
- Claims are classified as confirmed, likely, or unsafe.
- No blocker prevents Chief Editor from routing the task to Writer Agent.
- Some questions remain open, but they do not block writing if generic examples and cautious claims are acceptable.
