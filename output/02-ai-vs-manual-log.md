# AI vs Manual Intervention Log

This log captures each major section of the recruitment test and explicitly records:

- what AI was used for,
- where manual takeover happened,
- why manual intervention was required.

## Section-by-Section Breakdown

## A) Planning and task decomposition

What AI handled:
- Translated the assignment into an ordered execution plan.
- Proposed deliverable structure and testing priorities.

Manual takeover:
- Accepted/rejected proposed scope and final sequencing.

Why takeover was required:
- Scope realism and time-boxing are context-sensitive decisions tied to recruitment expectations.

## B) Environment/bootstrap commands

What AI handled:
- Generated likely Compose startup, verification, and shutdown commands.
- Proposed smoke checks to confirm stack availability.

Manual takeover:
- Command execution and environment verification.
- Handling any local machine differences (Docker state, timing, ports).

Why takeover was required:
- AI cannot observe local runtime directly unless the operator runs and validates the commands.

## C) Integration test strategy

What AI handled:
- Suggested endpoint-driven black-box strategy.
- Produced candidate assertions for status codes, payload shape, and simple performance limits.

Manual takeover:
- Finalized which tests were meaningful but not brittle for this assignment.

Why takeover was required:
- Candidate-quality testing requires judgment on reliability, signal quality, and maintainability.

## D) Test implementation and config wiring

What AI handled:
- Drafted test code scaffolding and dependency declarations.
- Proposed Compose integration for test execution.

Manual takeover:
- Adjusted repository-specific paths/configuration.
- Verified test assumptions against real API behavior.

Why takeover was required:
- Generated code often needs project-specific alignment to run cleanly.

## E) Runtime debugging and stabilization

What AI handled:
- Suggested probable root causes for typical failures.
- Recommended fix order and rerun loop.

Manual takeover:
- Live debugging based on actual logs and outcomes.
- Final decisions on pass thresholds and acceptable test strictness.

Why takeover was required:
- Real debugging depends on actual runtime evidence and practical engineering trade-offs.

## F) Final documentation and narrative

What AI handled:
- Drafted report sections and improved wording speed.
- Structured content for readability and reviewer scanning.

Manual takeover:
- Final editing for factual confidence and personal accountability.

Why takeover was required:
- Submission integrity requires human ownership of claims and conclusions.

## Observed Pattern

AI was strongest in:
- acceleration (first drafts, structure, boilerplate),
- breadth (surfacing options quickly),
- communication quality (clear formatting and concise narrative).

Manual effort remained essential for:
- environment truth (what actually runs),
- quality gates (what is acceptable, robust, and honest),
- final accountability (what is signed off and submitted).
