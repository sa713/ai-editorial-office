# Glossary

## purpose

This file defines shared operational terms for the local AI editorial office. Use these terms consistently in agents, pipelines, task artifacts, review notes, and finalization materials.

## terms

### artifact

**definition:** A saved task file that records work, evidence, decisions, outputs, or handoff context.

**usage notes:** Chat messages are not durable artifacts. Required artifacts belong in `/tasks/TASK-ID/`.

### handoff

**definition:** A task artifact that transfers context, status, blockers, and next action from one active role to another.

**usage notes:** Handoffs do not replace primary artifacts such as `draft.md`, `research.md`, or `review.md`.

### orchestration

**definition:** Chief Editor work that selects the pipeline, assigns core roles or legalized extension roles, defines sequence, and maintains task direction.

**usage notes:** Orchestration is not writing, review, or final approval by itself.

### review-gate

**definition:** The required independent validation step before finalization, publication, delivery, release, or governance closure.

**usage notes:** The gate can return `approved`, `changes_requested`, or `blocked`.

### factual claim

**definition:** Any statement that can be true or false about the world, a product, a source, a number, a date, a person, a policy, or an event.

**usage notes:** Claims about product behavior are factual claims.

### traceability

**definition:** The ability to connect a claim, decision, or output back to supporting task artifacts or sources.

**usage notes:** Traceability must be explicit enough for `review_agent` to verify.

### KB

**definition:** The project knowledge base in `/kb`, containing reusable standards, terminology, rules, and guidance.

**usage notes:** KB supports execution. It does not override higher authority.

### pipeline

**definition:** A controlled workflow that defines stages, required roles, artifacts, transitions, and review rules for a task type.

**usage notes:** Pipeline choice must be recorded in `orchestration_plan.md`.

### finalization

**definition:** Controlled preparation of the final deliverable after approved review.

**usage notes:** Finalization is performed by `final_editor`; Chief Editor governance decision comes after it.

### governance decision

**definition:** A Chief Editor decision about whether the task can close, needs human approval, must return to a prior stage, or is blocked.

**usage notes:** Record in `final_decision.md` when required by pipeline.

### downstream

**definition:** A later role, stage, artifact, or decision that depends on current work.

**usage notes:** Handoffs should protect downstream agents from missing context.

### upstream

**definition:** An earlier role, stage, artifact, or decision that current work depends on.

**usage notes:** If upstream evidence is missing, do not silently invent it.

### draft

**definition:** A working version of content that has not yet passed independent review and finalization.

**usage notes:** A draft is not a final deliverable.

### final deliverable

**definition:** The reviewed and finalized output prepared for user delivery, publication, release, or closure.

**usage notes:** It requires approved review and controlled finalization unless the pipeline says otherwise.

### UX writing

**definition:** Writing for product interfaces, flows, states, labels, helper text, errors, notifications, and user guidance surfaces.

**usage notes:** UX writing must not invent product behavior.

### microcopy

**definition:** Short interface copy that helps users understand state, make a decision, or complete an action.

**usage notes:** Short does not mean ungoverned.

### product context

**definition:** Evidence about product behavior, UI state, user flow, terminology, constraints, and business rules.

**usage notes:** Product context can come from briefs, screenshots, requirements, existing copy, research, or user-provided notes.

### factual sensitivity

**definition:** The risk level of getting a factual or product claim wrong.

**usage notes:** Higher sensitivity requires stronger evidence, clearer caveats, and stricter review.
