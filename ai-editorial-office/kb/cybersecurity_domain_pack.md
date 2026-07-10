# Cybersecurity Domain Knowledge Pack

Status: active

Pack name: Cybersecurity Domain Knowledge Pack

Domain: cybersecurity; security-sensitive analysis, threat understanding,
defensive recommendations, secure design, controls, assurance evidence, risk
interpretation, and safety-aware review context.

Maintainer context: AI Editorial Office canonical KB, created for release
`S4.R4`.

Created: 2026-07-10

Last reviewed: 2026-07-10

Stale if:

- NIST CSF, RMF, SP 800-53, SP 800-30, SSDF, SP 800-160, or SP 800-207 changes
  materially;
- OWASP ASVS, OWASP Top 10, OWASP API Security Top 10, or OWASP Cheat Sheet
  guidance changes materially;
- MITRE ATT&CK, MITRE CWE, or CIS Controls changes in ways that affect pack
  vocabulary, threat framing, weakness framing, or control prompts;
- repeated Engineering Review, Architecture Review, Professional Analysis,
  Professional Communication, or security-sensitive tasks expose missing
  cybersecurity terms, risks, activation boundaries, safety boundaries, or
  review questions;
- a future accepted Domain Knowledge Pack Standard adds required sections;
- this pack causes confusion with a role, capability, pipeline, review gate,
  policy owner, security owner, approval process, incident-response workflow,
  or mandatory ordinary task artifact;
- the pack is not reviewed for 12 months after acceptance.

## Purpose

This pack helps AI Editorial Office apply source-backed cybersecurity context
when security materially affects a task.

It helps existing roles and capabilities reason about:

- what security concern is actually present;
- which assets, data, identities, actors, privileges, interfaces,
  dependencies, and trust boundaries matter;
- which threats, abuse cases, and weakness classes are relevant;
- which defensive control families and mitigations should be considered;
- what evidence supports or weakens a security recommendation;
- what residual risk remains after controls, assumptions, and validation;
- when a request should be constrained, refused, or escalated because it asks
  for unsafe operational security content;
- which security questions should be asked first.

This pack is not a capability, role, pipeline, framework, lifecycle stage,
review gate, governance layer, policy owner, security owner, client profile,
task status model, security approval workflow, incident-response workflow, or
mandatory ordinary task artifact.

## Intended Use

Use this pack as cybersecurity domain context for security-sensitive work. It
may support:

- Chief Editor routing and activation decisions;
- Research Agent source framing and evidence boundaries;
- Writer Agent drafting of defensive security-sensitive analysis,
  recommendations, or review context;
- Review Agent challenge inside the existing review gate;
- Final Editor preservation of reviewed caveats, safety boundaries, and
  residual-risk language;
- Engineering Review when security and abuse context improves
  implementation/change-safety judgment;
- Architecture Review when threats, trust boundaries, identity, data handling,
  or secure design affect architectural fitness;
- Professional Analysis when cybersecurity reasoning affects synthesis,
  implications, recommendation, risk, uncertainty, or next decision;
- Professional Communication when cybersecurity caveats and evidence must be
  transferred clearly to a reader.

The pack does not decide review outcomes, final governance, release
acceptance, deployment approval, operational incident response, compliance
attestation, authorization to operate, or any security approval.

## When To Activate

Activate this pack only when cybersecurity context materially changes evidence
depth, terminology, risk handling, review focus, or output quality.

Typical activation triggers:

- the task evaluates, changes, recommends, or explains security-sensitive
  behavior;
- authentication, authorization, identity, access control, session handling,
  secrets, cryptography, data handling, privacy-sensitive flow, logging,
  monitoring, abuse prevention, resilience, or recovery assumptions are
  material;
- the task asks whether something is safe, risky, vulnerable, exposed,
  exploitable, trustworthy, or secure enough;
- the task needs threat modeling, abuse-case framing, trust-boundary analysis,
  or secure-design interpretation;
- the task involves untrusted input, user-controlled object references, API
  security, business logic misuse, sensitive data, multi-tenant isolation,
  privilege boundaries, or external integrations;
- a recommendation depends on weakness classes, control families, mitigations,
  defense in depth, least privilege, zero trust concepts, or residual risk;
- Review Agent must challenge security evidence, assumptions, and residual
  risk, not only prose quality or generic source support;
- Engineering Review identifies security and abuse as a material lens;
- Architecture Review identifies security as an architecturally significant
  quality attribute or trust-boundary concern;
- Professional Analysis or Professional Communication must preserve
  cybersecurity caveats, confidence, and safety constraints.

Record activation in the smallest existing task artifact that keeps the next
role safe:

- `orchestration_plan.md`;
- `task-manifest.md`;
- `research.md`;
- writer or UX notes;
- `review.md`;
- `final_decision.md`.

Activation note should name:

- active pack: `Cybersecurity Domain Knowledge Pack`;
- activation reason;
- relevant sections or sources;
- evidence confidence;
- boundary limits and stale-if triggers;
- safety stop conditions.

## When Not To Activate

Do not activate this pack when:

- "security", "safe", "risk", "trust", "threat", or "control" is only an
  incidental term;
- the task is ordinary writing, copyediting, formatting, navigation,
  summarization, or repo maintenance with no security-sensitive claim;
- Engineering Review can handle a small implementation/configuration change
  without additional cybersecurity domain context;
- the task is mainly secure delivery, CI/CD, automation, deployment,
  artifact-publishing, provenance, SBOM, runner, build, release, or
  operational-security context covered by the DevSecOps Domain Pack;
- the task is mainly software architecture design fitness and security is not
  material;
- the task asks for legal, regulatory, audit, insurance, or compliance
  attestation without task-specific authoritative sources and approval path;
- exact cloud, vendor, platform, product, CVE, exploitability, version,
  feature-tier, or configuration behavior must be verified and this pack has
  not been refreshed against the relevant source;
- activation would create a new role, capability, workflow, review gate,
  policy, approval requirement, incident-response process, or mandatory
  artifact;
- the user requests offensive procedures, weaponization, stealth, persistence,
  credential theft, bypass instructions, malware behavior, or unauthorized
  access instructions.

Do not activate merely because a source mentions security, authentication,
permissions, encryption, threats, OWASP, NIST, MITRE, controls, or risk.

## Questions This Pack Can Answer

This pack can help answer:

- What security concern is this really about?
- Which asset, data, identity, privilege, interface, dependency, or process is
  at risk?
- Who are the relevant actors, and what authority do they have?
- Where are the trust boundaries and authorization decision points?
- What could be spoofed, tampered with, disclosed, denied, overused, or
  escalated?
- What abuse cases matter for legitimate features?
- Which threat categories or adversary behaviors are relevant at a defensive
  level?
- Which weakness classes may explain the risk?
- Which control families or safeguards should be considered?
- Which mitigations reduce likelihood, impact, exposure, or blast radius?
- What evidence is needed to support a security recommendation?
- What residual risk, assumptions, unknowns, and stale-source limits remain?
- What should be escalated, constrained, refused, or returned to research?
- Which security questions should be asked first?

This pack cannot answer by itself:

- whether a real system is vulnerable without task-specific evidence;
- whether a CVE, exploit chain, malware sample, or attack report applies to a
  specific environment;
- how to exploit, bypass, evade, persist, exfiltrate, steal credentials, or
  obtain unauthorized access;
- whether a compliance, legal, audit, regulatory, or authorization claim is
  acceptable;
- which exact vendor or cloud setting must be configured without current
  primary-source research;
- whether Engineering Review, Architecture Review, Review Agent, Final Editor,
  Chief Editor, Project Lead, or a security owner should approve a change.

## Domain Boundary

In scope:

- cybersecurity risk interpretation;
- assets, actors, identities, privileges, interfaces, dependencies, data,
  trust boundaries, and security assumptions;
- defensive threat modeling and abuse-case framing;
- weakness classes and vulnerability interpretation;
- control-family and mitigation prompts;
- secure design, least privilege, defense in depth, secure defaults,
  resilience, observability, assurance, and residual risk;
- application and API security context;
- authentication, authorization, access control, input handling, output
  encoding, data protection, cryptographic-use framing, security logging,
  monitoring, dependency risk, configuration risk, privacy-sensitive data
  handling, multi-tenant boundaries, and business-logic misuse;
- safety boundaries for refusing or constraining unsafe requests.

Out of scope:

- operational exploit instructions;
- penetration-test procedures or attack playbooks;
- malware analysis that explains operational use;
- credential theft, phishing execution, exfiltration, stealth, persistence,
  evasion, or bypass guidance;
- unauthorized access;
- incident response operations, containment steps, eradication, forensics, or
  crisis communications workflow;
- compliance attestation, audit signoff, legal advice, authorization to
  operate, or security approval;
- DevSecOps delivery automation as a primary domain;
- general software architecture domain context where security is incidental.

Adjacent domains:

- Engineering Review: use this pack for cybersecurity context; implementation
  and change-safety review remains owned by `kb/engineering_review.md`.
- Architecture Review: use this pack for threats, trust boundaries, secure
  design, and security quality attributes; architecture review moves remain
  owned by `kb/architecture_review.md`.
- DevSecOps Domain Pack: use that pack for CI/CD, secure delivery,
  deployment automation, supply-chain delivery, provenance, build artifacts,
  runners, and operational-security assumptions.
- Software Architecture Domain Pack: use that pack for software architecture
  decisions, drivers, quality attributes, styles, patterns, boundaries, and
  tradeoffs beyond cybersecurity context.
- Professional Analysis: use this pack as evidence/context; analytical product
  shape remains owned by `kb/professional_analysis.md`.
- Professional Communication: use this pack as evidence/context; reader
  transfer remains owned by `kb/professional_communication.md`.
- Knowledge Evolution: use for stale-source updates, pack corrections,
  retirement, and canon-update candidates.

Overloaded terms:

- `security`: can mean cybersecurity, safety, privacy, compliance, physical
  security, job security, financial security, or emotional safety. Clarify
  before activating this pack.
- `risk`: in this pack, potential adverse effect from threats, weaknesses,
  exposure, likelihood, impact, and uncertainty. It is not the task status
  model.
- `threat`: potential cause of unwanted security impact. It is not proof that
  an attack is occurring.
- `vulnerability`: an instance-specific weakness or exposure that could be
  exploited. Do not infer existence without evidence.
- `weakness`: a class of design, implementation, configuration, or process
  condition that can contribute to vulnerabilities.
- `control`: safeguard or countermeasure. It is not proof of safety unless
  implemented, scoped, and evidenced.
- `mitigation`: action or design choice that reduces likelihood, impact,
  exposure, or blast radius. It may not eliminate risk.
- `assurance`: evidence-based confidence that controls or design properties
  work as intended.
- `trust boundary`: point where assumptions, authority, identity, data origin,
  or validation requirements change.
- `identity`: human, workload, device, service, API client, automation, or
  organization that can be authenticated or authorized.
- `authorization`: decision about what an authenticated or unauthenticated
  actor may do. It is distinct from authentication.
- `authentication`: process of establishing identity or credential validity.
  It does not grant permission by itself.
- `zero trust`: architecture and policy approach for resource access; not a
  product, slogan, or universal requirement.
- `secure`: shorthand that must be unpacked into threat model, controls,
  evidence, assumptions, and residual risk.

## Domain Vocabulary

| Term | Meaning in this pack | Notes |
| --- | --- | --- |
| Asset | Anything whose compromise, misuse, loss, or disruption matters. | May be data, system, service, identity, secret, model, workflow, reputation, or capability. |
| Actor | Human or non-human entity that can initiate actions or be affected. | Include users, admins, services, integrations, insiders, compromised accounts, and external adversaries. |
| Trust boundary | Place where assumptions about identity, authority, input, environment, or control change. | Good security review often starts here. |
| Threat | Potential cause of unwanted security impact. | Use categories defensively; do not operationalize. |
| Abuse case | Misuse of a legitimate feature or flow. | Useful for business logic and API risk. |
| Weakness class | Common design, implementation, or configuration problem type. | CWE and OWASP help organize, not prove, applicability. |
| Vulnerability | Specific weakness or exposure in a concrete system. | Requires task-specific evidence. |
| Control | Safeguard intended to reduce risk or satisfy a security objective. | NIST SP 800-53 and CIS Controls provide control vocabulary. |
| Mitigation | Change that reduces likelihood, impact, exposure, or blast radius. | Can be preventive, detective, corrective, compensating, or procedural. |
| Assurance evidence | Evidence that supports confidence in a security claim. | Examples: design review, tests, config inspection, logs, verification, source-backed analysis. |
| Residual risk | Risk remaining after controls, mitigations, assumptions, and evidence. | Must be visible when recommending or accepting security-sensitive work. |
| Least privilege | Grant only necessary authority for the task and duration. | Applies to humans, services, automation, APIs, data, and runtime components. |
| Defense in depth | Multiple mutually reinforcing safeguards. | Avoid single-control assumptions for high-impact risks. |
| Secure by default | Safer state is the default; risky behavior requires deliberate action. | Especially important for product and API design. |
| Fail secure | Failure mode preserves security properties as far as practical. | Balance with availability and usability context. |
| Attack surface | Exposed ways a system can be interacted with or influenced. | Include APIs, files, configs, dependencies, identities, and workflows. |
| Blast radius | Maximum plausible harm if a boundary or control fails. | Use to scale evidence and review depth. |
| Compensating control | Alternate safeguard used when primary control is absent or incomplete. | Must be justified and evidenced. |
| Detection | Ability to notice suspicious, harmful, or policy-relevant events. | This pack provides review prompts, not incident operations. |
| Recovery | Ability to restore or maintain needed function after adverse events. | Use as resilience context, not an incident-response workflow. |

## Security Principles

These principles are guidance, not policy. Use only when cybersecurity context
is material and evidence supports the claim.

### Start With Asset, Actor, Boundary, And Impact

Source basis: NIST CSF, NIST RMF, NIST SP 800-30, STRIDE, OWASP API guidance.

Do not begin with a favorite control. First ask what is protected, who or what
can act, where authority changes, and what harm matters.

### Security Is A Risk Judgment, Not A Vibe

Source basis: NIST SP 800-30, NIST RMF, ISO/IEC 27001 public guidance.

"Secure enough" depends on threat, impact, likelihood, safeguards, evidence,
assumptions, and residual risk. Strong language needs strong evidence.

### Authentication Is Not Authorization

Source basis: OWASP ASVS, OWASP API Security Top 10, OWASP Cheat Sheet Series.

Knowing who the actor is does not prove what they may access. Object, property,
function, tenant, and workflow authorization must be checked where material.

### Least Privilege Should Apply Everywhere Authority Exists

Source basis: NIST SP 800-53, CIS Controls, NIST zero trust guidance, OWASP.

Human users, services, workloads, tokens, automation, APIs, and integrations
should receive only the authority needed for the task and duration.

### Validate At Trust Boundaries

Source basis: STRIDE, OWASP ASVS, OWASP Top 10, OWASP API Security Top 10.

Inputs, outputs, identities, tokens, object references, files, callbacks,
dependencies, third-party data, and environment variables deserve scrutiny
when they cross a trust boundary.

### Prefer Secure Defaults And Explicit Unsafe Choices

Source basis: secure design, Microsoft SDL, NIST systems security engineering,
OWASP Top 10 insecure design framing.

Defaults should reduce accidental exposure. Risky behavior should require a
deliberate, visible decision with evidence and ownership.

### Defense In Depth Reduces Single-Control Fragility

Source basis: NIST control and resiliency sources, CIS Controls.

When impact is high, do not rely on one control. Combine preventive,
detective, corrective, and resilience measures proportionally.

### Detection And Recovery Are Part Of Security Confidence

Source basis: NIST CSF, NIST SP 800-160 Vol. 2.

For security-sensitive recommendations, ask how misuse, failure, or compromise
would be noticed and how harm would be limited or recovered from. Do not turn
this into an incident-response workflow.

### Source Mappings Are Not Equivalence

Source basis: NIST SP 800-53 mapping caution and Domain Knowledge Pack
Standard evidence rules.

Mappings between frameworks, controls, risks, and weaknesses are useful
navigation aids. They do not prove that one standard fully satisfies another
or that a system is safe.

## Assets, Actors, Trust Boundaries

Use this frame before selecting threat categories or controls.

Assets to identify:

- sensitive data, personal data, confidential documents, credentials, secrets,
  keys, tokens, sessions, logs, backups, models, prompts, user content, source
  code, configuration, artifacts, money-equivalent value, availability, brand
  trust, and operational capability;
- security-relevant process assets such as approval flows, admin actions,
  audit trails, rollback paths, and account recovery.

Actors to identify:

- anonymous users;
- authenticated users;
- privileged users and administrators;
- support or operations users;
- internal services and workload identities;
- third-party integrations and vendors;
- automation and scheduled jobs;
- tenants or customers;
- insiders;
- compromised accounts or clients;
- external adversaries at a category level.

Trust-boundary questions:

- Where does data come from, and what validates it?
- Where does identity become authority?
- Where do user, tenant, admin, service, and third-party privileges differ?
- Which component decides authorization?
- Which data or operation crosses network, process, tenant, system, or
  organizational boundaries?
- Which logs, alerts, or audit records prove boundary behavior?
- What happens when a dependency, integration, identity provider, or client is
  compromised or unavailable?

Boundary evidence:

- architecture or data-flow description;
- authorization model;
- API contract;
- permission matrix;
- configuration or policy;
- tests or verification results;
- logs/audit evidence;
- source-backed description of platform behavior.

## Threats And Abuse Cases

Use threat and abuse framing to make security concerns reviewable. Keep the
analysis defensive and category-level.

STRIDE-style threat prompts:

- Spoofing: can an actor pretend to be another user, service, tenant, device,
  or authority?
- Tampering: can data, configuration, state, logs, dependencies, or messages
  be changed without authorization or detection?
- Repudiation: can a material action happen without reliable accountability or
  audit evidence?
- Information disclosure: can sensitive data be exposed to an unauthorized
  actor or context?
- Denial of service: can resources, availability, or business flows be
  exhausted or disrupted?
- Elevation of privilege: can a lower-privilege actor gain higher authority or
  reach privileged functionality?

ATT&CK-informed defensive categories:

- initial access exposure;
- credential or identity misuse;
- privilege escalation;
- discovery of sensitive resources;
- lateral movement or boundary crossing;
- collection or unauthorized data access;
- exfiltration risk;
- impact to availability, integrity, or operations;
- detection and monitoring gaps;
- control impairment or evasion risk.

Use ATT&CK to name categories, not to reproduce procedures.

Abuse-case prompts:

- Can a legitimate feature be automated, repeated, or sequenced to cause harm?
- Can one user access another user's object, data, property, or action?
- Can a business flow be overused, manipulated, or monetized against the
  intended rules?
- Can a support, admin, recovery, invitation, export, upload, callback, or
  integration path bypass ordinary controls?
- Can data intended for one audience, tenant, role, or environment appear in
  another?
- Can errors, diagnostics, or logs disclose sensitive information?
- Can rate, cost, quota, workflow, notification, or retry behavior be abused?

## Weakness Classes

Use weakness classes to organize investigation. Do not assert a vulnerability
without task-specific evidence.

Common weakness areas:

- broken access control or authorization;
- authentication and session management failures;
- injection and unsafe command/query construction;
- insecure design or missing abuse-case handling;
- security misconfiguration;
- cryptographic misuse or weak key/secret handling;
- sensitive data exposure;
- software or data integrity failures;
- logging, alerting, and monitoring gaps;
- error and exceptional-condition mishandling;
- insecure deserialization or unsafe parsing;
- server-side request forgery and unsafe outbound requests;
- file upload, path, and content handling errors;
- business logic and workflow misuse;
- multi-tenant isolation failures;
- dependency and third-party component risk;
- API inventory, versioning, and deprecation gaps.

Evidence needed to map a weakness:

- affected asset and actor;
- trust boundary crossed;
- design, code, config, dependency, or workflow evidence;
- relevant source or standard mapping;
- exploitability uncertainty, if any;
- impact and residual risk.

## Controls And Mitigations

Use controls as source-backed prompts, not as automatic mandates.

Control families and safeguard areas to consider:

- governance and risk management context;
- asset and data inventory;
- identity and access management;
- authentication and credential management;
- authorization and privilege management;
- audit and accountability;
- configuration management;
- vulnerability and patch management;
- secure design and secure development;
- input validation, output encoding, and safe parsing;
- cryptographic protection and key management;
- data minimization, retention, classification, and protection;
- network, API, and interface protection;
- logging, monitoring, and alerting;
- backup, recovery, and resilience;
- supplier, third-party, and dependency risk;
- incident readiness as an assumption, not an AI Editorial Office workflow.

Mitigation questions:

- Does the mitigation address root cause, exploit path, impact, or only
  symptoms?
- Is it preventive, detective, corrective, compensating, or resilience-oriented?
- Which asset, actor, boundary, or weakness does it cover?
- What does it not cover?
- What evidence proves it exists and works for this context?
- Is the mitigation proportional to impact and likelihood?
- Does it introduce usability, availability, privacy, operational, or
  architecture tradeoffs?
- What residual risk remains?

## Risk And Assurance

Use this compact pattern when cybersecurity claims materially affect a task:

```markdown
## cybersecurity evidence
- concern:
- asset:
- actor:
- trust boundary:
- threat or abuse case:
- weakness class:
- controls or mitigations:
- evidence checked:
- confidence:
- assumptions:
- unknowns:
- residual risk:
- safety boundary:
```

Confidence guidance:

- High confidence: multiple authoritative sources support the general
  principle, and task-specific evidence shows the relevant boundary/control.
- Medium confidence: authoritative sources support the principle, but
  task-specific evidence is partial or indirect.
- Low confidence: plausible concern but evidence is incomplete, stale,
  inferred, or source-specific behavior is unverified.

Downgrade confidence when:

- exact platform behavior is unknown;
- the artifact under review is not visible;
- source version or environment differs from the claim;
- a control is named but implementation evidence is absent;
- threat impact depends on unverified assumptions;
- the claim is compliance, legal, exploitability, or production-safety related.

## Secure Design Considerations

Secure design questions:

- What security requirement exists before implementation?
- Which abuse cases were considered?
- Which assets and trust boundaries shape the design?
- Is authority centralized, explicit, and testable where appropriate?
- Are sensitive operations protected by strong authorization, auditability, and
  recovery assumptions?
- Are defaults safe for ordinary users and operators?
- Does failure preserve confidentiality, integrity, availability, or safety as
  far as practical?
- Does the design minimize exposed functionality, privilege, and sensitive
  data?
- Can the system detect misuse or boundary violation?
- Is the design resilient if a dependency, integration, credential, or
  component is compromised?
- Which tradeoffs were accepted and by whom?

Architecture-sensitive security prompts:

- Is security a dominant quality attribute?
- Which quality attributes conflict with security: usability, availability,
  performance, cost, operability, or modifiability?
- Does the architecture make security assumptions visible?
- Are trust boundaries aligned with service, data, tenant, deployment, and
  ownership boundaries?
- Are cross-boundary calls authenticated, authorized, validated, logged, and
  monitored proportionally?

## Security Evidence Expectations

Useful evidence categories:

- inspected design, data-flow, architecture, API, or authorization model;
- source-backed explanation of platform, framework, or control behavior;
- code, configuration, dependency, or policy inspection when implementation is
  material;
- tests that exercise authorization, authentication, input handling, tenant
  isolation, rate/resource limits, or abuse cases;
- vulnerability scan or static/dynamic analysis output, when scoped and
  interpreted cautiously;
- logs, alerts, audit records, or monitoring evidence;
- permission, role, token, session, or identity evidence;
- cryptographic design and key/secret management evidence;
- data classification, retention, minimization, and access evidence;
- dependency, supplier, package, image, or integration evidence;
- residual risk and explicit unknowns.

Evidence should be stronger when:

- sensitive data, secrets, credentials, money-equivalent value, personal data,
  safety, high availability, customer trust, production systems, or privileged
  actions are involved;
- the change crosses tenant, admin, identity, service, external integration, or
  public/private boundaries;
- the recommendation may be implemented by a reader without further review;
- the task could cause harmful real-world action if wrong.

Do not require every evidence category for every task. Choose proportionally
and record why omitted evidence is acceptable.

## Review Questions

Review Agent may use these questions inside the existing review gate when this
pack is active:

- Was pack activation justified by material cybersecurity context?
- Did the artifact stay within defensive, review-oriented context?
- Did it avoid exploit instructions, bypass procedures, malware guidance,
  credential theft guidance, stealth/persistence guidance, and unauthorized
  access instructions?
- Does the artifact identify the security concern clearly?
- Are assets, actors, identities, data, privileges, interfaces, dependencies,
  and trust boundaries visible enough?
- Are threat and abuse-case claims category-level and source-backed?
- Are weakness-class mappings supported by evidence rather than plausibility?
- Are controls and mitigations proportional to the risk and scoped to the
  right boundary?
- Does the artifact distinguish authentication from authorization where
  material?
- Are least privilege, defense in depth, secure defaults, validation, and
  logging/monitoring considered when relevant?
- Are exact platform, vendor, CVE, exploitability, compliance, or legal claims
  backed by task-specific sources?
- Are scanner, checklist, mapping, framework, or control references treated as
  evidence signals rather than verdicts?
- Are assumptions, unknowns, stale-source limits, and residual risk visible?
- Did the pack support Engineering Review, Architecture Review, Professional
  Analysis, or Professional Communication without replacing them?
- Did the artifact avoid duplicating DevSecOps pack ownership?

## Common Mistakes

- Treating cybersecurity as a new AI Editorial Office role, review gate, or
  approval workflow.
- Calling something "secure" without naming threat model, controls, evidence,
  assumptions, and residual risk.
- Treating authentication as sufficient authorization.
- Ignoring object, property, function, tenant, or workflow authorization.
- Treating a scanner, checklist, framework mapping, or control name as a
  verdict.
- Citing OWASP Top 10 or CWE as proof that a specific vulnerability exists.
- Using ATT&CK as attack guidance instead of defensive category vocabulary.
- Recommending controls before identifying assets, actors, and trust
  boundaries.
- Ignoring abuse cases because a feature behaves "as designed."
- Forgetting logs, auditability, detection, and recovery assumptions.
- Making exact vendor/platform claims without checking current primary docs.
- Duplicating DevSecOps pack scope for CI/CD and secure delivery work.
- Replacing Engineering Review with a cybersecurity checklist.
- Hiding safety concerns in polished prose instead of constraining or refusing
  unsafe requests.

## Source Register

| Source | Class | Authority | Version/date | Last checked | Relevance | Confidence limits |
| --- | --- | --- | --- | --- | --- | --- |
| NIST Cybersecurity Framework 2.0 Resource Center (`https://www.nist.gov/cyberframework`) | Framework resource | U.S. government / NIST | CSF 2.0, 2024; resource center current with 2026 updates | 2026-07-10 | Cybersecurity risk management, governance, profiles, informative references | High for broad risk-management framing; not a task-specific checklist |
| NIST SP 800-37 Rev. 2 (`https://csrc.nist.gov/pubs/sp/800/37/r2/final`) | Special publication | U.S. government / NIST | December 2018 | 2026-07-10 | RMF lifecycle risk management, control selection, assessment, monitoring | High for RMF concepts; does not own AI Editorial Office lifecycle |
| NIST SP 800-53 Rev. 5 with updates (`https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final`) | Control catalog | U.S. government / NIST Joint Task Force | September 2020; Release 5.2.0 planning note 2025-08-27 | 2026-07-10 | Security/privacy control families, functionality and assurance framing | High for control vocabulary; detailed control use requires source-specific inspection |
| NIST SP 800-30 Rev. 1 (`https://csrc.nist.gov/pubs/sp/800/30/r1/final`) | Risk assessment guide | U.S. government / NIST | September 2012 | 2026-07-10 | Risk assessment, threat/vulnerability/residual-risk vocabulary | High for risk concepts; older but still authoritative |
| NIST SP 800-218 SSDF v1.1 (`https://csrc.nist.gov/pubs/sp/800/218/final`) | Secure development framework | U.S. government / NIST | February 2022 | 2026-07-10 | Secure development practices and vulnerability reduction | High for secure-development framing; delivery automation belongs mostly to DevSecOps pack |
| NIST SP 800-160 Vol. 1 Rev. 1 (`https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final`) | Systems security engineering | U.S. government / NIST | November 2022 | 2026-07-10 | Secure systems engineering, trustworthiness, requirements, assurance | High for secure design; depth must be scaled to task |
| NIST SP 800-160 Vol. 2 Rev. 1 (`https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final`) | Cyber resiliency engineering | U.S. government / NIST | December 2021 | 2026-07-10 | Anticipate, withstand, recover, adapt; cyber resiliency concepts | High for resilience framing; not incident-response procedure |
| NIST SP 800-207 (`https://csrc.nist.gov/pubs/sp/800/207/final`) | Zero trust architecture guide | U.S. government / NIST | August 2020 | 2026-07-10 | Identity/resource access, policy enforcement, continuous evaluation | Medium-high; exact architecture decisions need task-specific context |
| OWASP ASVS (`https://owasp.org/www-project-application-security-verification-standard/`) | Verification standard | OWASP flagship project | Latest stable 5.0.0 | 2026-07-10 | Application security verification requirements and assurance vocabulary | High for app-security verification; not a CI/CD or compliance standard |
| OWASP Top 10 2025 (`https://owasp.org/Top10/2025/`) | Awareness project | OWASP | 2025 release | 2026-07-10 | Broad web-app risk categories | High for awareness and first questions; not proof of a vulnerability |
| OWASP API Security Top 10 2023 (`https://owasp.org/API-Security/editions/2023/en/0x11-t10/`) | API security awareness project | OWASP | 2023 release | 2026-07-10 | API authorization, authentication, resource, business-flow, SSRF, config, inventory, and third-party API risk prompts | High for API review prompts; exact vulnerability claims need task evidence |
| OWASP Cheat Sheet Series (`https://cheatsheetseries.owasp.org/`) | Practitioner guidance | OWASP project | Maintained web project | 2026-07-10 | Defensive guidance across access control, auth, input validation, logging, secrets, threat modeling, abuse cases | Medium-high; inspect individual cheat sheets when relied on |
| MITRE ATT&CK (`https://attack.mitre.org/`) | Adversary behavior knowledge base | MITRE | v19, April 2026 current version | 2026-07-10 | Tactics, techniques, mitigations, detections, data components, threat-model vocabulary | High for defensive categories; do not reproduce operational attack steps |
| MITRE CWE (`https://cwe.mitre.org/about/index.html`, `https://cwe.mitre.org/data/index.html`) | Weakness taxonomy | MITRE / DHS-CISA sponsored program | CWE List Version 4.20 | 2026-07-10 | Weakness vocabulary, root-cause framing, mappings to OWASP and other groupings | High for weakness classes; applicability requires task-specific evidence |
| CIS Critical Security Controls (`https://www.cisecurity.org/controls/v8`) | Prioritized safeguards | Center for Internet Security | v8 and v8.1 download page current | 2026-07-10 | Prioritized safeguards, offense-informed defense, focus/feasibility/measurability principles | High for safeguard framing; detailed safeguard text requires source inspection |
| ISO/IEC 27001:2022 (`https://www.iso.org/standard/27001`) | International standard landing page | ISO/IEC | Edition 3, 2022-10; one amendment noted | 2026-07-10 | ISMS and risk-aware organizational security framing | Medium; public page only, full standard is paywalled |
| Microsoft SDL (`https://www.microsoft.com/en-us/securityengineering/sdl/`) | Secure development lifecycle guidance | Major vendor / practitioner source | Current Microsoft page | 2026-07-10 | Secure development lifecycle integration, broad software/platform applicability | Medium-high; Microsoft practices should be adapted, not mandated |
| Microsoft STRIDE Threat Modeling Tool threats (`https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats`) | Threat-modeling guidance | Major vendor / practitioner source | Last updated 2022-08-25 | 2026-07-10 | STRIDE categories and threat-modeling prompts | Medium-high for vocabulary; Microsoft tooling context |

## Confidence Notes

High confidence:

- The selected sources are authoritative enough for durable cybersecurity
  vocabulary, first questions, defensive principles, review prompts, and
  evidence categories.
- Cybersecurity context belongs as a Domain Knowledge Pack rather than as a new
  role, capability, pipeline, gate, policy owner, approval workflow, or
  mandatory artifact set.
- Security recommendations should expose assets, actors, trust boundaries,
  threats, weaknesses, controls, evidence, assumptions, and residual risk.
- Framework mappings, scans, controls, and awareness lists are evidence inputs,
  not standalone verdicts.

Medium confidence:

- Application/API security category mappings are useful, but specific findings
  require task-specific evidence.
- STRIDE is useful as a compact threat-modeling vocabulary, but other threat
  modeling methods may fit some tasks better.
- ISO/IEC 27001 is useful for ISMS context from the public page, but detailed
  requirements were not inspected.

Limited confidence:

- Exact vendor, cloud, platform, product, feature-tier, CVE, or configuration
  behavior. Future tasks must re-check primary current sources.
- Exploitability or severity of a specific vulnerability without direct
  evidence and authorized scope.

## Update Rules

Update this pack when:

- a registered source changes materially, is superseded, retired, or
  contradicted;
- OWASP, MITRE, NIST, CIS, ISO, or Microsoft guidance changes in ways that
  affect activation, vocabulary, boundaries, review questions, safety
  constraints, or evidence expectations;
- repeated tasks show missing activation criteria, non-activation criteria,
  security terms, weakness classes, control prompts, safety boundaries, or
  evidence expectations;
- Engineering Review, Architecture Review, Professional Analysis,
  Professional Communication, or Review Agent identifies unsupported,
  misleading, stale, or over-prescriptive guidance;
- DevSecOps or future domain packs require clearer adjacent-domain boundaries;
- Project Lead or Chief Editor accepts a source-backed improvement;
- a future accepted Domain Knowledge Pack Standard adds required sections.

Update path:

- small source-backed clarifications may update this pack directly through a
  reviewed task;
- high-governance, source-heavy, disputed, or boundary-changing updates should
  use a release or reviewed system task;
- preserve provenance, source date/version, what changed, and confidence
  limits.

## Retirement Rules

Retire or deprecate this pack when:

- AI Editorial Office no longer performs security-sensitive analysis, review,
  defensive recommendation, or secure-design work;
- source support becomes too stale or weak to maintain confidence;
- a better canonical owner or replacement pack supersedes it;
- it repeatedly causes confusion with Engineering Review, Architecture Review,
  DevSecOps, roles, capabilities, pipelines, review gates, policy ownership,
  security approval, incident response, or mandatory artifacts;
- safety boundaries cannot be maintained reliably;
- maintenance cost exceeds future value.

Retirement must preserve enough context for future readers to know why the
pack should no longer be used. Do not delete historical task artifacts merely
to clean the narrative.

## Relation To Engineering Review

This pack may support Engineering Review when implementation/change safety
involves:

- security-sensitive behavior;
- secrets, credentials, tokens, permissions, or authority boundaries;
- authentication or authorization logic;
- untrusted input, parsing, files, APIs, or integrations;
- sensitive data handling;
- configuration that affects security;
- dependency or third-party risk;
- logging, monitoring, recovery, or resilience assumptions;
- abuse paths and residual risk.

Engineering Review still owns:

- changed surface;
- selected engineering lenses;
- implementation/change-safety judgment;
- validation evidence;
- review findings;
- residual engineering risk;
- review outcome through the existing Review Agent path.

The pack must not turn Engineering Review into a cybersecurity checklist, nor
replace Engineering Review completion criteria.

## Relation To Architecture Review

This pack may support Architecture Review when cybersecurity affects:

- architecture drivers or constraints;
- security as a quality attribute;
- trust boundaries and data flows;
- identity, tenancy, service, API, and ownership boundaries;
- secure design tradeoffs;
- resilience and recovery assumptions;
- accepted risk and decision rationale.

Architecture Review still owns:

- architectural significance;
- drivers and quality-attribute scenarios;
- alternatives and tradeoffs;
- architecture risks and assumptions;
- decision-rationale challenge.

## Relation To DevSecOps Pack

Use the DevSecOps Domain Pack as primary context when the task is mainly about:

- secure delivery;
- CI/CD workflows;
- automation permissions, tokens, triggers, runners, artifacts, caches, or
  logs;
- dependency, package, action, image, toolchain, SBOM, provenance,
  attestation, or artifact publishing in a delivery path;
- secrets and credentials in delivery, deployment, build, runtime, or
  infrastructure paths;
- deployment boundaries, environment safety, container/runtime deployment, or
  operational-security assumptions tied to delivery.

Use this Cybersecurity pack as primary context when the task is mainly about:

- threats, abuse cases, weakness classes, controls, secure design, risk,
  assurance, sensitive data, identity, authorization, API security, or
  defensive recommendation outside secure delivery context.

When both apply, Chief Editor should record which pack is primary and why.

## Relation To Existing Canon

This pack may support:

- Engineering Review;
- Architecture Review;
- Professional Analysis;
- Professional Communication;
- Evidence Confidence Assessment;
- Knowledge Evolution.

This pack must not override:

- `AGENTS.md` for governance, role boundaries, task flow, review gate, and
  final decision authority;
- `kb/domain_knowledge_pack_standard.md` for pack structure, activation,
  evidence, boundary, review, update, and retirement rules;
- `kb/engineering_review.md` for implementation/change safety review and
  Engineering Review outcomes;
- `kb/architecture_review.md` for Architecture Review moves;
- `kb/devsecops_domain_pack.md` for secure delivery and DevSecOps context;
- `kb/software_architecture_domain_pack.md` for software architecture domain
  context;
- `kb/professional_analysis.md` for analytical product shape;
- `kb/professional_communication.md` for reader transfer;
- `kb/editorial_evidence_framework.md` for evidence taxonomy and confidence
  labels;
- `kb/editorial_learning_framework.md` for Knowledge Evolution;
- task-local `task-manifest.md`, `orchestration_plan.md`, `status.md`,
  `review.md`, `final.md`, or `final_decision.md`.

`/about` disposition:

- `/about` may summarize or reference this pack for external memory alignment.
- Canonical production use remains under `ai-editorial-office/kb/`.
- If `/about` diverges from this pack, this pack wins.

## Safety Boundaries

Allowed:

- defensive security concepts;
- risk framing;
- threat categories at a high level;
- abuse-case questions;
- secure design and mitigation prompts;
- review questions;
- evidence and assurance expectations;
- control-family and safeguard references;
- safety constraints and refusal/constrain triggers.

Forbidden:

- exploit instructions;
- weaponization steps;
- bypass procedures;
- malware creation, deployment, persistence, stealth, evasion, or operation;
- credential theft, phishing execution, token theft, or secret extraction
  guidance;
- unauthorized access instructions;
- instructions to evade detection, logging, monitoring, rate limits, access
  controls, or abuse protections;
- procedural attack chains or operational adversary playbooks;
- incident-response command procedures that create a new operational workflow.

Constrain or refuse when:

- the user asks how to exploit, bypass, evade, persist, steal credentials, or
  access unauthorized systems;
- the task would provide actionable offensive steps without clear authorized
  defensive framing;
- the requested detail would materially increase misuse risk;
- the task asks for operational security approval that AI Editorial Office
  cannot grant;
- source evidence is insufficient for a safety-sensitive claim.

Safe alternative pattern:

- explain the boundary;
- provide high-level defensive risk framing;
- suggest authorized testing, code review, configuration review, threat
  modeling, logging, monitoring, patching, or control verification at a
  non-operational level;
- route to task-specific research or human security owner when needed.

