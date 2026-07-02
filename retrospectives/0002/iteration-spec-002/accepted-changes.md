# Accepted changes

## 1. Reader-state definitions and boundaries

**Why needed**
To define the layer narrowly before implementation.

**Problem solved**
Prevents reader-state from becoming a behavioral program.

**Where it should live**
`editorial_knowledge`, preferably near principles, intent or failure patterns.

**Expected effect**
Writers and reviewers share the same small vocabulary.

**Risk**
New terminology may drift.

**Priority**
P0.

**Implementation style**
Short canonical note. No new stage.

## 2. Low-pressure entry guidance

**Why needed**
TASK-0009 improved when the first action became safe and small.

**Problem solved**
Reduces pressure-first onboarding.

**Where it should live**
`editorial_knowledge`, with possible later reference from review guidance.

**Expected effect**
Texts can invite a first look without demanding immediate commitment.

**Risk**
Could soften mandatory actions incorrectly.

**Priority**
P0.

**Implementation style**
Rule plus examples. Include honesty boundary.

## 3. Pressure audit in review

**Why needed**
Review should catch unneeded pressure, fake obligation and fake momentum.

**Problem solved**
Accurate texts can still create avoidable resistance.

**Where it should live**
Review guidance in `editorial_knowledge`; optional prompt later if needed.

**Expected effect**
Review findings become more precise for onboarding/change tasks.

**Risk**
Could become tone policing.

**Priority**
P1.

**Implementation style**
Optional review block for relevant tasks only.

## 4. TASK-0009 failure patterns

**Why needed**
TASK-0009 produced reusable practical patterns.

**Problem solved**
Helps diagnose entry friction without full rewrite.

**Where it should live**
`editorial_knowledge/50_editorial_failure_patterns.md` or equivalent owner.

**Expected effect**
Review can name concrete failures: mandatory-process framing, pressure-first onboarding, fake adoption momentum.

**Risk**
Pattern list may grow into doctrine.

**Priority**
P1.

**Implementation style**
Small additions only. No exhaustive taxonomy.

## 5. Bounded reader-state refinement shape

**Why needed**
TASK-0009 v2 worked as a bounded refinement.

**Problem solved**
Prevents unnecessary rewrite when only the entry is too heavy.

**Where it should live**
Review or refinement guidance, depending on current ownership.

**Expected effect**
Reader-state issues produce targeted repairs.

**Risk**
May under-fix structural channel problems.

**Priority**
P1.

**Implementation style**
Add a small shape: issue, friction source, minimal repair, do-not-change, re-review target.

## 6. Optional intake/orchestration prompts

**Why needed**
Some tasks need reader-state consideration before writing starts.

**Problem solved**
Avoids discovering entry friction only at final review.

**Where it should live**
Task-specific orchestration guidance or template prompts only if production use proves need.

**Expected effect**
Relevant tasks state first-step risk early.

**Risk**
Could bloat orchestration.

**Priority**
P2.

**Implementation style**
Optional questions, not required fields.

## 7. Governance honesty rule

**Why needed**
Soft entry cannot change real obligation.

**Problem solved**
Prevents fake softness and hidden governance loss.

**Where it should live**
Editorial knowledge first; governance references only if later needed.

**Expected effect**
Mandatory, optional and unknown states stay clear.

**Risk**
Duplication with existing governance rules.

**Priority**
P0.

**Implementation style**
One short rule:

```text
Mandatory stays mandatory. Optional stays optional. Unknown stays unknown.
```

## Not accepted as changes

Do not accept any change that requires:

- a new role;
- a new pipeline;
- mandatory behavioral review for all tasks;
- scoring;
- metrics;
- automatic detection;
- broad template rewrite.
