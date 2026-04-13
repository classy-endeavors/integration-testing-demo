# End-to-End Recruitment Test Execution (Vibe Coding First)

## Scope

Complete the Sock Shop recruitment assignment end to end:

1. Run the microservices stack locally.
2. Create integration tests.
3. Execute tests and verify pass/fail behavior.
4. Produce final delivery documentation.

Primary approach: maximize AI-assisted delivery ("Vibe Coding"), while stepping in manually only where environment or judgment required direct intervention.

## End-to-End Flow

### 1) Understand task and repo structure

- Read existing project docs (`README.md`, internal docs, deployment hints).
- Locate key files and expected run path for Docker Compose.
- Confirm likely insertion point for integration tests and deliverables.

AI role:
- Generated initial repo orientation checklist and proposed execution plan.
- Suggested likely command sequence and test target endpoints.

Manual role:
- Validated whether suggestions mapped to the actual local environment and current repo layout.

Why manual was needed:
- AI can infer expected structure; only a human can confirm "this machine right now" state, tool availability, and local constraints.

### 2) Start system under test

- Launch Sock Shop with Docker Compose.
- Verify service health via process listing and basic HTTP checks.

AI role:
- Produced startup and health-check commands.
- Suggested minimum smoke criteria for "ready to test".

Manual role:
- Ran commands, monitored startup behavior, and handled environmental waiting/sequence.

Why manual was needed:
- Runtime readiness is environment-dependent; practical orchestration (timing/retries) depends on live observations.

### 3) Design integration test coverage

- Define black-box tests through `edge-router`.
- Select baseline functional and non-functional checks:
  - frontend availability,
  - catalogue data contract,
  - tags endpoint behavior,
  - negative path (404),
  - lightweight response time budget.

AI role:
- Drafted first-pass test matrix and pytest structure.
- Proposed assertions for schema/shape and basic contract validity.

Manual role:
- Pruned/adjusted checks for realistic scope and reliability.
- Balanced strictness vs brittleness to avoid flaky outcomes.

Why manual was needed:
- Test quality is a judgment call; over-strict AI proposals can be fragile, under-strict proposals can be superficial.

### 4) Implement tests and test runtime containerization

- Create integration test files and dependency list.
- Configure integration test service in Compose override.
- Ensure command path supports repeatable execution.

AI role:
- Generated test scaffolding and boilerplate quickly.
- Suggested file-level organization and command wiring.

Manual role:
- Resolved path/cfg specifics and alignment with this repository's conventions.
- Validated that generated code matched real endpoint behavior.

Why manual was needed:
- Repository-specific glue code often needs precise local adaptation.

### 5) Execute and debug

- Run tests end to end through Compose.
- Inspect failures (if any), adjust assertions, rerun until stable.
- Confirm final pass state.

AI role:
- Interpreted likely failure classes and suggested fixes.
- Recommended iterative troubleshooting order.

Manual role:
- Performed actual reruns and made final call on acceptable pass criteria.

Why manual was needed:
- Debugging is grounded in real logs/timings and pragmatic decisions about stability.

### 6) Produce final report

- Document objective, approach, coverage, execution, result, limitations, and next tests.

AI role:
- Produced structured draft language and formatting.
- Accelerated conversion from implementation details into reviewer-ready report prose.

Manual role:
- Final editorial pass for clarity, credibility, and alignment with assignment expectations.

Why manual was needed:
- Final ownership and authenticity of technical narrative remains a human responsibility.

## Outcome

- Integration test suite created and runnable.
- Test execution documented and reported.
- End-to-end recruitment deliverable completed with AI-heavy workflow and targeted manual interventions where trust, environment, or judgment required human control.
