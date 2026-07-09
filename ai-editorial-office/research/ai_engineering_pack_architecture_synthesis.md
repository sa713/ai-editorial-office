# AI Engineering Domain Pack Architecture Synthesis

- Release: `S4.R5 - AI Engineering Domain Pack`
- Decision owner: Chief Editor
- Date: 2026-07-10
- Evidence: `research/ai_engineering_pack_landscape.md` and task-local full
  evidence in `tasks/TASK-AI-ENGINEERING-DOMAIN-PACK-RELEASE/`

## Architecture decision

Create one canonical release-candidate context package:
`kb/ai_engineering_domain_pack.md`.

The pack will cover AI-enabled system reasoning across requirements,
model/provider fit, prompt/instruction artifacts, structured outputs, RAG,
data, evaluation, reliability/monitoring, human oversight, safety/misuse,
integration/tool workflows, and AI-assisted engineering. It remains subordinate
to repository governance and existing canonical owners.

Architecture impact: `small`.

The change adds domain context and discoverability/state references. It does
not add or alter a role, capability, framework, pipeline, lifecycle stage,
review gate, approval workflow, governance layer, policy owner, status model,
client profile, or mandatory ordinary task artifact.

## Why one pack

The required subjects are coupled system surfaces, not separate governance
domains. Prompt behavior depends on data and instructions; RAG depends on data,
authorization, retrieval, prompts, and evaluation; tool/agent behavior depends
on interfaces, permissions, traces, monitoring, and human authority; AI coding
depends on ordinary engineering verification plus AI-specific failure prompts.
One layered pack preserves these relationships and gives future tasks a single
activation decision.

Splitting the subjects now would create fragmented activation, duplicate
sources, and unclear maintenance ownership. No evidence shows a need for
separate Prompt, RAG, Evaluation, Agent, or AI Coding packs.

## Options considered

| Option | Decision | Reason |
| --- | --- | --- |
| One bounded AI Engineering pack | selected | Coherent domain object, existing pack standard, low architecture impact |
| Separate prompt/RAG/eval/agent packs | rejected for this release | Fragmentation and duplicated boundary/source maintenance |
| New AI specialist role | rejected | Domain packs do not create accountability wrappers; explicitly out of scope |
| New AI review capability or gate | rejected | Engineering Review and the existing review gate already own change challenge |
| AI governance or model approval workflow | rejected | Would create policy/approval authority outside pack scope |
| Vendor/product implementation guide | rejected | Fast-staling and not reusable repository canon |
| Short glossary/source list only | rejected | Insufficient for required practical questions and scenario validation |

## Canonical ownership map

| Concern | Canonical owner | Pack relationship |
| --- | --- | --- |
| Pack structure, activation, evidence, update, retirement | Domain Knowledge Pack Standard | Must conform |
| Task lifecycle, roles, review gate, status, approval | `AGENTS.md` and lifecycle canon | Cannot modify or restate as new policy |
| Design decomposition and quality tradeoffs | Software Architecture Domain Pack / Architecture Review | Supply AI-specific surfaces and evidence questions |
| Threats, misuse, access, controls, assurance, residual security risk | Cybersecurity Domain Pack | Supply AI-specific context; route security judgments |
| CI/CD, configuration, secrets, artifacts, supply chain, deployment/runtime | DevSecOps Domain Pack | Supply AI artifact/signal context; route operational detail |
| Implementation/change safety findings | Engineering Review | Inform selected lenses; cannot approve a change |
| Analytical synthesis and decision-ready recommendation | Professional Analysis | Supply domain facts, limits, and tradeoffs |
| Evidence/confidence | Editorial Evidence Framework | Use claim traceability and visible uncertainty |

## Pack shape

The canonical file should use the following reader path:

1. Identity, status, authority, purpose, activation, non-activation, questions,
   and domain boundary.
2. Vocabulary, principles, and an AI-system surface map.
3. Practical guidance for model/provider fit, prompt/instruction, structured
   output, RAG, data, evaluation, reliability/monitoring, human oversight,
   safety/misuse, integrations/workflows, and AI-assisted engineering.
4. Evidence expectations, review questions, mistakes, and safe escalation.
5. Source register, confidence notes, update/retirement rules, and explicit
   relationships to adjacent canon.

The sections are reference context. Their order is not a mandatory lifecycle,
workflow, or checklist.

## Quality-attribute reasoning

| Attribute | Architecture response | Tradeoff |
| --- | --- | --- |
| Correctness | Claim-level evidence and source limitations | Longer evidence packet |
| Durability | Vendor-neutral principles; volatile details excluded | Less product tutorial detail |
| Usability | Surface map, question sets, scenario-oriented review prompts | Some repetition at boundaries is intentional |
| Safety | Defensive categories, safe alternatives, explicit exclusions | No operational adversarial examples |
| Maintainability | One source register, stale triggers, owner relations | Broad pack needs disciplined sectioning |
| Reviewability | Explicit non-claims and evidence expectations | Pack cannot offer a simple pass/fail score |
| Architecture fit | No new role/capability/pipeline/gate; route to owners | Pack sometimes stops at an escalation boundary |

## Evidence architecture

- Repository canonical claims use `R01-R07` from the task source register.
- Durable external claims use corroborated provider/standards sources where
  practical.
- Single-provider facts remain clearly scoped.
- Current product behavior, preview features, account terms, data handling, and
  service limits are task-time research, not canonical assumptions.
- NIST/OWASP/MITRE supply risk language and discovery prompts, not automatic
  findings or acceptance criteria.
- The public ISO page is a directional source only.

## Safety architecture

The pack may describe defensive risk categories, trust boundaries, evidence to
request, least-privilege principles, validation questions, monitoring, refusal,
and safe escalation. It must not preserve or generate procedural material for
jailbreak construction, prompt-injection exploitation, exfiltration, evasion,
malware/phishing, credential theft, unauthorized access, or other abuse.

When a task asks for prohibited operational detail, the safe alternative is to
state the risk category, define the defensive assessment goal, request benign
test evidence, recommend bounded controls, and route the security judgment to
Cybersecurity context and authorized reviewers.

## Integration changes authorized

- Add `kb/ai_engineering_domain_pack.md` as release candidate.
- Add it to `kb/00_index.md` for discoverability.
- Add the required research and release artifacts.
- As the complete candidate enters independent review, synchronize `BACKLOG.md`,
  `ROADMAP.md`, canonical `project-state.md`, and the bounded `/about` memory
  copies/summaries required by existing memory rules so the reviewer can
  validate one consistent release state.
- Mark S4.R5 as Release Candidate / Review, not accepted or active.

No other canonical or structural change is authorized.

## Scenario architecture

The release report must validate that:

1. internal-knowledge RAG activates AI Engineering and routes authorization
   threats to Cybersecurity;
2. structured output activates interface and semantic validation questions;
3. AI coding assistance activates AI Engineering plus Engineering Review, and
   DevSecOps/Cybersecurity only when their surfaces are material;
4. an evaluation-plan task gets criteria, representative cases, graders,
   thresholds, and continuous/change evidence without a mandated scorecard;
5. a safety-sensitive prompt change remains defensive and routes security
   judgment correctly;
6. a sensitive-data AI workflow triggers provenance/privacy/provider-freshness
   questions and adjacent security/delivery context;
7. a primarily Cybersecurity or DevSecOps request does not get captured by the
   AI Engineering pack merely because AI is mentioned.

## Decision and stop conditions

Decision: approved for Writer Agent production within the bounded contract.

Reopen architecture or research if writing requires:

- a new authority owner or mandatory artifact;
- a universal model/provider/metric/control verdict;
- detailed operational security guidance;
- an unresolved duplicate with adjacent canon;
- a product-specific statement presented as durable behavior.
