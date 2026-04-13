# Final Assessment and Anti-AI Hardening Recommendations

## Written Assessment

Overall judgment: the recruitment task can be completed to a strong baseline with heavy AI assistance, but successful delivery still depends on human execution for environment validation, debugging, and quality judgment.

## Percentage Breakdown (AI-assisted execution mix)

- **AI contribution: 90%**
  - Rapid planning and decomposition.
  - Test scaffolding and assertion drafts.
  - Report structuring and language refinement.
  - Troubleshooting hypothesis generation.

- **Manual contribution: 10%**
  - Running and validating local runtime behavior.
  - Repository/environment-specific correction.
  - Final debugging decisions and reliability tuning.
  - Submission integrity and final sign-off.

## Reasoning for the Percentages

1. **High automation potential in writing tasks**
   - Most initial code and documentation artifacts are generatable quickly by AI.
2. **Moderate human dependence in runtime truth**
   - Commands, service readiness, and integration behavior are validated only through live execution.
3. **Persistent human role in judgment-heavy decisions**
   - Choosing robust assertions, rejecting flaky checks, and deciding "good enough" thresholds requires engineering discretion.
4. **Accountability remains human**
   - Final output quality and trustworthiness rely on human verification and ownership.

## If the Goal Is to Be More Robust Against AI-Only Completion

Use these changes to raise the signal on real engineering capability rather than prompt quality alone.

### 1) Add a live debugging segment

- Provide a pre-broken scenario (misconfigured service, subtle contract mismatch, or flaky dependency timing).
- Require candidates to diagnose and explain root cause with evidence from logs/metrics.

Why it helps:
- Harder to fake with generic AI output; requires runtime reasoning under uncertainty.

### 2) Include unknown change requests mid-task

- After baseline completion, inject a requirement change (for example, stricter contract validation or an additional negative-path behavior).
- Ask candidate to adapt tests and explain trade-offs.

Why it helps:
- Measures adaptability and judgment instead of static template generation.

### 3) Require rationale-backed test selection

- Ask for explicit reasoning on why each test exists, what risk it catches, and what it intentionally excludes.

Why it helps:
- Exposes whether candidate understands test value beyond generated boilerplate.

### 4) Add an oral or synchronous walkthrough

- 15-20 minute review where candidate explains architecture assumptions, failure handling, and debugging path.

Why it helps:
- Validates authentic understanding and makes copy/paste delivery less effective.

### 5) Score process evidence, not just final artifacts

- Require concise execution log: commands run, failures encountered, fixes applied, and why.
- Allocate rubric points to diagnostic quality and decision-making transparency.

Why it helps:
- Rewards real problem-solving behavior that AI alone cannot fully simulate.

### 6) Use hidden edge cases in evaluation

- Run candidate tests against slightly perturbed environments (latency spike, partial data issue, non-happy path input).

Why it helps:
- Distinguishes resilient engineering from "happy path only" AI-generated solutions.

## Suggested Evaluation Rubric Update (example)

- 30%: Functional correctness and runnable setup
- 20%: Test depth and defect-detection power
- 20%: Debugging quality (evidence-based diagnosis and fixes)
- 15%: Reasoning and trade-off articulation
- 15%: Documentation clarity and reproducibility

This weighting increases the value of human engineering judgment while still allowing productive AI-assisted workflows.
