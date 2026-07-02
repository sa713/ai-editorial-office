# Risk findings

## Risk 1

File: `ai-editorial-office/AGENTS.md`

Problem: the entry discipline section still says Chief Editor must "activate the visual branch when the selected task requires it", while the later freeze section says visual activation requires an explicit frozen-subsystem request from the user.

Why this is a risk: a hurried reader could treat the earlier wording as permission for automatic visual activation. The later freeze rule is clearer and more specific, so this is a wording risk, not an operational failure.

Need to fix now: no. A future cleanup can add "subject to frozen-subsystem activation rules" to the earlier line.

## Risk 2

File: `editorial_knowledge/40_editorial_review_system.md`

Problem: visual review checks remain available and do not explicitly mention the frozen status.

Why this is a risk: if someone reads the review system without `AGENTS.md`, they might think visual review can run as a normal path. In practice the checks are conditional on visual outputs, and activation is governed by `AGENTS.md`.

Need to fix now: no. Optional future cleanup can add a cross-reference to the frozen activation rule.

## Risk 3

File: `editorial_knowledge/20_editorial_modes.md`

Problem: visual mode bodies still contain active production language after their inactive-by-default status line.

Why this is a risk: read in isolation, the mode body may look executable. The status line and `AGENTS.md` freeze rule correctly prevent automatic activation.

Need to fix now: no. The modes should remain recoverable for later reactivation.

## Overall risk level

Minor. No risk found that text editorial work is broken or that visual branch must run automatically.

