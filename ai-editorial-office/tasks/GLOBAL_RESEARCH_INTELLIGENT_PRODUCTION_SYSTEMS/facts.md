# Facts, Interpretations, and Tensions

Task ID: `GLOBAL_RESEARCH_INTELLIGENT_PRODUCTION_SYSTEMS`
Owner role: `research_agent`
Status: v1 evidence extraction
Last updated: 2026-07-02

## Confirmed Facts

| ID | Fact | Sources |
| --- | --- | --- |
| F01 | DORA maintains a multi-year research archive and core model for software delivery and organizational performance. | S01 |
| F02 | The 2025 DORA AI report frames AI adoption as a systems problem, not merely a tool-installation problem. | S02 |
| F03 | Accelerate connects delivery performance to technical practices, lean management, culture, and organizational outcomes. | S03 |
| F04 | Google SRE treats reliability as an engineering discipline with SLOs, toil management, automation, release engineering, incident management, and postmortems. | S04 |
| F05 | SLO practice depends on explicit user-centered indicators and objectives. | S05 |
| F06 | NIST SSDF provides high-level secure software development practices intended to be integrated into the SDLC. | S06 |
| F07 | ISO/IEC/IEEE 42010 organizes architecture description around stakeholders, concerns, viewpoints, and views. | S07 |
| F08 | SPACE explicitly rejects a single universal developer productivity metric. | S08 |
| F09 | Google's public software engineering material treats sustainable engineering as more than programming, including review, docs, testing, and tools. | S09 |
| F10 | Google's code-review case study presents review as quality control, knowledge sharing, and codebase stewardship. | S10 |
| F11 | CNCF defines internal platforms as curated capabilities that reduce cognitive load and provide shared patterns. | S11 |
| F12 | CNCF's platform maturity model warns that organizations should reflect on needs rather than merely chase the highest maturity level. | S12 |
| F13 | Google Cloud distinguishes developer portals from full internal developer platforms. | S13 |
| F14 | Continuous discovery emphasizes regular customer connection, product trio collaboration, and outcome-oriented product work. | S14 |
| F15 | Opportunity solution trees connect outcomes, opportunities, solution options, and experiments. | S15 |
| F16 | SVPG distinguishes empowered product teams from feature teams that primarily execute predefined requests. | S16 |
| F17 | OpenAI defines agents as systems that can reason, plan, use tools, and handle multi-step tasks under instructions and guardrails. | S17 |
| F18 | OpenAI recommends building agents when workflows have ambiguity, multi-step decisions, tool use, and hard-to-maintain rules. | S17 |
| F19 | OpenAI's agent guidance treats tools, instructions, orchestration, guardrails, and evals as core design elements. | S17, S18 |
| F20 | Anthropic advises using agentic complexity only when it improves outcomes and emphasizes evaluation with real tasks. | S19 |
| F21 | Anthropic documents coding agents as tools that read codebases, edit files, and run commands within permissions and context systems. | S20 |
| F22 | SWE-bench evaluates language models on real GitHub issue resolution requiring repository understanding and environment interaction. | S21 |
| F23 | SWE-agent argues that agent-computer interface design affects automated software engineering performance. | S22 |
| F24 | NIST AI RMF provides a voluntary framework for trustworthy AI risk management. | S23 |
| F25 | ISO/IEC 42001 defines an AI management system using continual improvement and risk/opportunity management. | S24 |
| F26 | Toyota Production System is built around waste elimination, jidoka, just-in-time, and kaizen. | S25 |
| F27 | The WHO surgical checklist uses a short set of pause-point checks to reduce errors and improve teamwork and communication. | S27 |
| F28 | ADR practice records architecture decisions in small, structured entries with context and consequences. | S28, S29 |
| F29 | Diataxis separates documentation into tutorials, how-to guides, explanation, and reference. | S30 |
| F30 | W3C PROV and RDF provide stable models for provenance and linked knowledge representation. | S31, S32 |

## Research Interpretations

| ID | Interpretation | Basis | Confidence |
| --- | --- | --- | --- |
| I01 | Intelligent production systems are sociotechnical systems: process, tooling, roles, incentives, knowledge, and feedback loops must be designed together. | F01-F04, F11-F14, F17-F25 | High |
| I02 | Durable practices tend to externalize feedback: tests, SLOs, reviews, incident learning, customer discovery, evals, and source provenance. | F04-F05, F10, F14-F15, F19-F23, F27-F30 | High |
| I03 | Mature systems combine autonomy with explicit guardrails instead of choosing between command-and-control and unmanaged freedom. | F05-F07, F11-F12, F17-F25 | High |
| I04 | AI-first engineering raises, rather than removes, the need for evidence, evals, permissions, context management, and human checkpoints. | F17-F25 | High |
| I05 | Knowledge bases become reusable only when records are atomic, source-backed, linked, and maintained as living assets. | F28-F32 plus user requirement | High |
| I06 | Adjacent domains are most useful when translated as abstract principles, not copied as surface rituals. | F25-F27 | Medium-high |

## Contradictions and Tensions

| ID | Tension | Why it matters | Sources |
| --- | --- | --- | --- |
| T01 | Speed versus reliability is not solved by maximizing either side; SLO/error-budget thinking makes the tradeoff explicit. | Prevents both reckless delivery and reliability paralysis. | S03-S05 |
| T02 | Productivity measurement is necessary but can become harmful when reduced to activity counts. | Preserves trust and avoids Goodhart effects. | S01-S03, S08 |
| T03 | Platform standardization reduces cognitive load but can suppress local autonomy if the platform is not treated as a product. | Separates golden paths from coercive bureaucracy. | S11-S13 |
| T04 | Agents can handle ambiguous multi-step work, but multi-agent complexity can lower reliability if not justified by eval results. | Prevents agentic overengineering. | S17-S20 |
| T05 | Checklists improve reliability when placed at real pause points, but checklist theater creates false assurance. | Critical for translating aviation/medicine practices into engineering. | S26-S27 |
| T06 | Standards provide stable language but can become compliance theater without real risk, feedback, and ownership. | Important for SSDF, ISO 42001, ISO 42010, ISO 29119. | S06-S07, S23-S24, S34 |

## Source Gaps for Future Research

- More direct material from modern AI labs about internal research operations, model-evaluation governance, and coding-agent production use.
- More empirical evidence comparing product operating models across different company sizes.
- More non-software sources from aviation, manufacturing, and research laboratories beyond the first v1 set.
- More detailed source work on engineering leadership, decision-authority models, and organizational design.

