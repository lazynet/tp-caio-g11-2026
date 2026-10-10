---
description: Run a multi-agent review of the plan (role lenses in parallel, then the board)
argument-hint: "[path to review, default plan/]"
---

Review target: $ARGUMENTS (if empty, review `plan/`).

1. In parallel, dispatch `architect`, `governance`, `people` and `finance`. Each
   reviews the target only through its own lens and returns gaps,
   contradictions with other sections, and unsourced claims. They do not edit.
2. Dispatch `board` with the target plus the four lens reports. It writes the
   dated review to `reviews/`.
3. Report back: the board's verdicts, the top 5 findings with their owner,
   and the review file path.
