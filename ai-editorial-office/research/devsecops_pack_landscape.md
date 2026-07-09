# DevSecOps Pack Landscape

Status: research complete for S4.R3 release synthesis.

Date: 2026-07-10

Research role: `research_agent`

## Research Question

What durable, source-backed DevSecOps knowledge should AI Editorial Office
package so future delivery, automation, configuration, supply-chain,
deployment, validation, and operational-security tasks can ask better
questions without creating a new role, capability, pipeline, policy owner, or
review gate?

## Source Selection

The research prioritized sources that are primary, authoritative, maintained,
or widely treated as standards for secure software delivery:

- secure software development frameworks and maturity models;
- application-security verification standards;
- software supply-chain integrity specifications;
- CI/CD platform security guidance;
- open-source security-health tooling;
- container and Kubernetes security guidance;
- secure build, secret, and artifact guidance;
- operational reliability/security guidance.

Excluded:

- shallow DevSecOps blogspam;
- vendor marketing that does not expose concrete security controls;
- generic cybersecurity guidance not tied to delivery, automation,
  configuration, supply chain, deployment, validation, or operations;
- compliance-only material that would turn the pack into policy.

## Executive Findings

DevSecOps expertise is not a separate AI Editorial Office capability. It is a
domain context for secure delivery work where security, automation,
configuration, supply chain, deployment, validation evidence, and operational
assumptions overlap.

The pack should emphasize:

- secure SDLC context from NIST SSDF and OWASP SAMM;
- CI/CD workflows as privileged executable delivery paths;
- least privilege for workflow tokens, job tokens, service accounts, and
  runner environments;
- careful treatment of untrusted input, forked code, privileged triggers,
  artifacts, and caches;
- third-party action, dependency, package, image, and toolchain provenance;
- source, build, and artifact integrity from SLSA and related supply-chain
  practices;
- SBOM/provenance as visibility and evidence, not proof of safety by itself;
- secret minimization, short-lived credentials, OIDC/external secret providers,
  masking limits, and rotation after exposure;
- configuration and environment drift, especially defaults, branch/tag
  protection, protected variables, deployment environments, namespaces, and
  production boundaries;
- container/runtime/infrastructure hardening with explicit platform limits;
- validation evidence before accepting security-sensitive delivery changes;
- operational security assumptions such as monitoring, incident response,
  patching, rollback, environment ownership, and runtime diagnostics.

The pack should not:

- decide whether a change passes Engineering Review;
- own CI/CD policy, security policy, cloud policy, incident response policy, or
  compliance decisions;
- prescribe one DevSecOps maturity model;
- turn SLSA, SAMM, ASVS, Scorecard, CIS, Docker, Kubernetes, GitHub, or GitLab
  guidance into universal law;
- create mandatory SBOMs, attestations, checklists, scans, gates, or artifacts.

## Source Register

| Source | Class | Version/date | Last checked | Relevance | Confidence limits |
| --- | --- | --- | --- | --- | --- |
| NIST SP 800-218, Secure Software Development Framework (SSDF) Version 1.1 (`https://csrc.nist.gov/pubs/sp/800/218/final`, `https://csrc.nist.gov/Projects/ssdf`) | U.S. government special publication | February 2022; SSDF project page updated 2026-04-13 | 2026-07-10 | Secure SDLC vocabulary; Prepare/Protect/Produce/Respond practices; provenance and secure environment concepts | High for secure development framing; not a DevSecOps implementation checklist |
| OWASP SAMM (`https://owasp.org/www-project-samm/`, `https://owaspsamm.org/model/`) | OWASP maturity model | Current version 2.0.3 (2022) | 2026-07-10 | Security maturity across governance, design, implementation, verification, and operations; secure build/deployment/defect management; environment and incident practices | High for maturity framing; not a mandate to assess organizational maturity in every task |
| OWASP ASVS (`https://owasp.org/www-project-application-security-verification-standard/`) | OWASP application security verification standard | Latest stable 5.0.0 | 2026-07-10 | Security verification requirements and application control vocabulary | High for application-control verification context; not a CI/CD or infrastructure standard |
| SLSA Specification v1.2 (`https://slsa.dev/spec/v1.2/`, `https://slsa.dev/spec/v1.2/threats`) | Open supply-chain integrity specification | v1.2 approved | 2026-07-10 | Supply-chain threat model; source/build tracks; provenance, verification, levels, artifact integrity | High for supply-chain integrity concepts; SLSA v1.1 is retired and should not be treated as current |
| OpenSSF Scorecard (`https://scorecard.dev/`, `https://github.com/ossf/scorecard/blob/main/docs/checks.md`) | OpenSSF security-health tool/docs | Current project docs; checks continually change | 2026-07-10 | Repository security signals: branch protection, code review, dangerous workflows, pinned dependencies/actions, CI tests, binary artifacts | Medium-high for automated signal ideas; scores are signals, not review verdicts |
| GitHub Actions secure use reference (`https://docs.github.com/en/actions/reference/security/secure-use`) | Platform security documentation | Current GitHub Docs | 2026-07-10 | Workflow secrets, `GITHUB_TOKEN` permissions, script injection, `pull_request_target`, third-party action pinning, OIDC, environment reviewers | High for GitHub Actions tasks; platform-specific and not automatically transferable to other CI systems |
| GitHub Actions token/secrets docs (`https://docs.github.com/en/actions/tutorials/authenticate-with-github_token`, `https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets`) | Platform security documentation | Current GitHub Docs | 2026-07-10 | Workflow token authentication and secret handling | High for GitHub Actions; use current docs for exact behavior |
| GitLab CI/CD variables docs (`https://docs.gitlab.com/ci/variables/`) | Platform security documentation | Current GitLab Docs | 2026-07-10 | Sensitive variables, masked/protected/hidden variables, forked merge request variable exposure, review before running pipelines | High for GitLab CI/CD; version-specific features may change |
| GitLab CI/CD job token docs (`https://docs.gitlab.com/ci/jobs/ci_job_token/`) | Platform security documentation | Current GitLab Docs | 2026-07-10 | Short-lived job tokens, allowlists, runner security, public/internal project access, push permissions | High for GitLab job-token tasks; version-specific behavior may change |
| GitLab external secrets docs (`https://docs.gitlab.com/ci/secrets/`) | Platform security documentation | Current GitLab Docs | 2026-07-10 | External secret providers and OIDC/ID-token secret access | High for GitLab secret retrieval; feature tier and platform availability matter |
| Kubernetes Pod Security Standards (`https://kubernetes.io/docs/concepts/security/pod-security-standards/`) | Kubernetes official docs | Current docs, v1.36 nav | 2026-07-10 | Privileged/Baseline/Restricted pod security profiles; runtime hardening vocabulary | High for Kubernetes workloads; cluster/version/admission implementation must be checked locally |
| Kubernetes Secrets good practices (`https://kubernetes.io/docs/concepts/security/secrets-good-practices/`) | Kubernetes official docs | Current docs | 2026-07-10 | Secret encryption, least-privilege Secret access, namespace separation, external secret stores, avoiding Secret manifests | High for Kubernetes secret handling; provider-specific secret-store behavior needs task-specific research |
| Kubernetes RBAC good practices (`https://kubernetes.io/docs/concepts/security/rbac-good-practices/`) | Kubernetes official docs | Current docs | 2026-07-10 | Least privilege, privileged service-account/token distribution, wildcard permissions, cluster-admin/system:masters risks | High for Kubernetes RBAC; exact access impact depends on cluster configuration |
| Docker build best practices (`https://docs.docker.com/build/building/best-practices/`) | Docker official docs | Current Docker Docs | 2026-07-10 | Multi-stage builds, trusted/minimal base images, rebuilds, image testing in CI | Medium-high for Docker builds; Docker-specific and not a full runtime security standard |
| Docker build secrets (`https://docs.docker.com/build/building/secrets/`) | Docker official docs | Current Docker Docs | 2026-07-10 | Build secrets, secret mounts, SSH mounts; avoiding build args/env for secrets | High for Docker/BuildKit build-secret handling |
| Docker Engine security and daemon access (`https://docs.docker.com/engine/security/`, `https://docs.docker.com/engine/security/protect-access/`) | Docker official docs | Current Docker Docs | 2026-07-10 | Container isolation, daemon attack surface, socket protection, SSH/TLS daemon access | Medium-high; exact hardening depends on host, runtime, and orchestration context |
| CIS Kubernetes Benchmark (`https://www.cisecurity.org/benchmark/kubernetes`) | CIS benchmark landing page | Kubernetes benchmark 2.0.1 listed | 2026-07-10 | Secure configuration benchmark reference for Kubernetes | High as benchmark existence/version source; detailed benchmark content requires downloaded PDF and task-specific check |
| CIS Docker Benchmark (`https://www.cisecurity.org/benchmark/docker`) | CIS benchmark landing page | Docker benchmark 1.8.0 listed | 2026-07-10 | Secure configuration benchmark reference for Docker | High as benchmark existence/version source; detailed benchmark content requires downloaded PDF and task-specific check |
| NTIA SBOM resources (`https://www.ntia.gov/page/software-bill-materials`) | U.S. government SBOM resource hub | 2021 resources | 2026-07-10 | SBOM definition, component transparency, SBOM production/acquisition/use concepts | High for SBOM purpose and terminology; SBOM alone does not prove exploitability or safety |
| Microsoft Security Development Lifecycle (`https://www.microsoft.com/en-us/securityengineering/sdl/`) | Vendor secure development lifecycle guidance | Current Microsoft page | 2026-07-10 | SDL as secure DevOps approach, broad lifecycle applicability, secure supply-chain consumption framing | Medium-high; Microsoft-specific practice set should be adapted, not mandated |
| Google SRE Book, production environment and SLO chapters (`https://sre.google/sre-book/production-environment/`, `https://sre.google/sre-book/service-level-objectives/`) | Practitioner book from Google SRE/O'Reilly | 2017 online book | 2026-07-10 | Production readiness, monitoring, rollout, operational assumptions, reliability evidence | Medium for DevSecOps security; strong for operational reliability context, not security-control selection |

## What The Sources Agree On

### DevSecOps Is Lifecycle Integration, Not A Tool Bundle

NIST SSDF describes high-level secure development practices that can be
integrated into any SDLC. OWASP SAMM spans governance, design,
implementation, verification, and operations. Microsoft SDL frames SDL as a
security approach integrated into DevOps processes.

Implication for the pack: DevSecOps context should ask where security evidence
appears across the delivery lifecycle, not whether a task has a scanner or
mentions "shift left".

### CI/CD Is Privileged Executable Delivery Code

GitHub and GitLab docs both warn that workflow or pipeline definitions can
expose secrets, write to repositories, publish artifacts, deploy to
environments, and execute attacker-controlled input when triggers, tokens,
runners, or scripts are unsafe. OpenSSF Scorecard treats dangerous workflows,
branch protection, review, binary artifacts, and CI tests as security-health
signals.

Implication for the pack: CI/CD review questions should start with triggers,
permissions, secrets, runners, untrusted input, third-party components,
artifacts, caches, and deployment boundaries.

### Least Privilege Must Apply To Automation, Not Only Humans

GitHub recommends minimum necessary `GITHUB_TOKEN` permissions. GitLab job
tokens are short-lived but inherit relevant access from the triggering user and
need allowlist/scoping attention. Kubernetes RBAC guidance emphasizes minimal
rights for users and service accounts and warns against wildcard or
cluster-admin-style access.

Implication for the pack: automation identities, service accounts, tokens,
environment reviewers, job tokens, and runner placement need explicit review.

### Supply-Chain Integrity Needs Source, Build, Artifact, And Verification Context

SLSA v1.2 frames supply-chain integrity through source and build tracks,
provenance, verification, and threat locations across source, build,
publication, distribution, usage, dependencies, and verification. NIST SSDF
includes protection of software and provenance data for components. NTIA SBOM
resources frame SBOMs as component transparency. OpenSSF Scorecard provides
repository-level signals but not a proof of safety.

Implication for the pack: dependency and artifact questions should ask what
was built, from which source, by which process, with which dependencies, how it
was signed/attested/published, and how consumers verify it.

### Secrets Are High-Risk Even When Masked

GitHub notes that automatic redaction is not guaranteed and recommends least
privilege, masking, rotation, and audit of secret handling. GitLab docs warn
that malicious `.gitlab-ci.yml` changes can exfiltrate variables and that
masking is not guaranteed to stop malicious access. Kubernetes docs distinguish
Secrets from ConfigMaps but also note base64 is not encryption and access to
Secrets must be constrained.

Implication for the pack: secret safety depends on necessity, scope, lifetime,
storage, access path, logs, transformations, runner trust, and exposure
response. "Masked" is not enough.

### Runtime And Infrastructure Security Are Boundary Questions

Kubernetes Pod Security Standards give profile vocabulary from unrestricted to
restricted. Kubernetes RBAC and Secret guidance expose namespace, pod,
service-account, and workload-creation risks. Docker docs emphasize trusted
minimal base images, multi-stage builds, rebuilds, build secrets, daemon attack
surface, and socket protection. CIS Benchmarks provide secure configuration
references for Docker and Kubernetes.

Implication for the pack: container/runtime guidance must be framed as
context-dependent review prompts, not a universal platform hardening checklist.

### Validation Evidence Must Be Proportional To Risk

OWASP ASVS provides application-control verification vocabulary. OWASP SAMM
separates verification practices from implementation and operations. GitHub,
GitLab, Docker, and Kubernetes guidance all require platform-specific evidence
for safety claims. Google SRE guidance reinforces that production changes need
monitoring, rollout, capacity/reliability assumptions, and operational
visibility.

Implication for the pack: validation should include inspected config/diff,
passed tests/checks, scanner results where relevant, permission evidence,
secret handling evidence, provenance/SBOM/attestation evidence, deployment
environment evidence, rollback/monitoring evidence, and explicit residual risk.

## Concepts To Carry Into The Pack

| Concept | Source support | Pack consequence |
| --- | --- | --- |
| Secure SDLC | NIST SSDF, OWASP SAMM, Microsoft SDL | Secure delivery questions should span preparation, protection, production, response, and operations |
| Secure build | OWASP SAMM, SLSA, Docker, CI docs | Build process, builder trust, dependencies, base images, secrets, and provenance matter |
| CI/CD workflow | GitHub/GitLab docs, Scorecard | Treat workflow files as privileged code with trigger, permission, and artifact impact |
| Workflow trigger | GitHub docs, Scorecard | Privileged triggers with untrusted code require special scrutiny |
| Job token / workflow token | GitHub/GitLab docs | Scope, default permissions, trigger actor, and write/deploy capability must be known |
| Runner | GitHub/GitLab docs, SLSA | Trust boundary and isolation affect secret, token, cache, and artifact safety |
| Provenance | SLSA, NIST SSDF | Ask who/what built an artifact and whether consumers can verify it |
| SBOM | NTIA, NIST SSDF | Useful transparency evidence, not a safety verdict |
| Attestation | SLSA, GitHub artifact attestation docs | Evidence about artifact properties must be verified and scoped |
| Secret | GitHub, GitLab, Kubernetes, Docker | Sensitive data requires minimization, scoping, secure injection, masking caveats, and rotation path |
| Protected environment | GitHub/GitLab docs | Deployment context should mediate secret access and production action |
| Protected branch/tag | GitLab, GitHub, Scorecard, SLSA | Controls source integrity and release provenance assumptions |
| Base image | Docker, CIS, supply-chain guidance | Trusted, minimal, updated, and pinned/traceable base images reduce artifact risk |
| Runtime profile | Kubernetes Pod Security Standards, Docker | Runtime hardening must be platform-specific and evidence-backed |
| Operational readiness | Google SRE, SAMM Operations | Secure deployment includes monitoring, incident response, rollback, and patching assumptions |

## First DevSecOps Questions

- What is being changed: source, workflow, runner, secret, dependency, image,
  artifact, deployment target, infrastructure config, or operational boundary?
- What can this automation read, write, deploy, publish, delete, or expose?
- Which identities and tokens execute it, and what is their effective scope?
- Can untrusted code, metadata, artifacts, caches, or inputs influence a
  privileged context?
- Which secrets are available, when, to whom, and how would exposure be
  detected and remediated?
- What external actions, packages, images, tools, plugins, or scripts are
  trusted, pinned, updated, and reviewed?
- What artifact is produced, how is it identified, and can provenance or
  attestation connect it to source and build process?
- What environment boundary separates test, staging, production, local
  development, and privileged deployment?
- What evidence proves the change was validated and what residual risk remains?
- What operational assumption would fail first after deployment?

## Pack Boundary Implications

In scope:

- secure development lifecycle context;
- CI/CD workflow and pipeline security;
- automation permissions, tokens, triggers, runners, artifacts, caches, and
  logs;
- dependency, package, action, toolchain, SBOM, provenance, attestation, and
  artifact risk;
- secrets and credentials in delivery and runtime paths;
- configuration and environment safety;
- container, runtime, and infrastructure security considerations when tied to
  delivery or deployment;
- validation evidence and operational-security assumptions.

Out of scope:

- full cybersecurity threat modeling and control selection;
- incident response ownership;
- compliance/legal attestation;
- cloud platform architecture selection;
- software architecture design fitness except where delivery/runtime boundaries
  overlap;
- implementation code review beyond secure delivery context;
- deciding Engineering Review verdicts.

Adjacent-domain notes:

- Use Engineering Review for implementation/change safety; the DevSecOps pack
  supplies source-backed context.
- Use Software Architecture Domain Pack when architectural structure,
  boundaries, quality attributes, or design decisions are material beyond
  delivery/security automation.
- Use future Cybersecurity Domain Pack or task-specific research for threat
  modeling, abuse cases, vulnerability analysis, cryptography, identity
  architecture, or security-control selection outside delivery context.
- Use task-specific vendor docs whenever exact platform behavior, feature
  tier, or current syntax matters.

## Confidence Notes

High confidence:

- SSDF, SAMM, ASVS, SLSA, GitHub, GitLab, Kubernetes, Docker, CIS, NTIA, and
  Microsoft SDL are authoritative enough for durable DevSecOps vocabulary and
  source-backed review prompts.
- Secure delivery should be risk-based and evidence-proportional, not reduced
  to a scanner checklist.
- CI/CD and deployment automation deserve security review because they hold
  credentials, permissions, artifact publication paths, and production access.

Medium confidence:

- Specific platform guidance can shift quickly; use the source register for
  source class and last-checked dates, and re-check exact behavior in future
  platform-sensitive tasks.
- Scorecard and SBOM outputs are useful signals, but their absence or presence
  cannot decide risk alone.

Limited confidence:

- Detailed CIS benchmark recommendations were not reproduced because the public
  landing pages confirm benchmark identity and versions, while detailed
  controls require downloading and inspecting the relevant PDFs in a
  task-specific context.
- Exact cloud-provider deployment-hardening guidance is intentionally not
  generalized in this pack.

## Research Conclusion

The DevSecOps Domain Pack should be implemented as one source-backed KB file:

```text
ai-editorial-office/kb/devsecops_domain_pack.md
```

It should provide practical context and review questions for secure delivery,
CI/CD, automation, configuration, supply-chain, deployment, validation, and
operations-sensitive work. It should support Engineering Review without
becoming Engineering Review, and it should activate only when DevSecOps context
materially changes evidence depth, terminology, risk handling, review focus, or
output quality.
