# Sock Shop Integration Testing Final Report

## Objective

Run the Sock Shop open source project locally using Docker Compose, design and execute integration tests, and document the technical approach and results.

## Project and References

- Repository: [microservices-demo/microservices-demo](https://github.com/microservices-demo/microservices-demo)
- TDD guideline reference: [Smarter Codes - Test Driven Development](https://gitlab.com/smarter-codes/sc-guidelines/software-engineering/coding/test-driven-development/-/work_items/1)

## Environment

- OS: Windows 10
- Runtime: Docker Desktop + Docker Compose
- App entrypoint: `http://localhost` (via `edge-router`)

## What Was Implemented

### 1) Local deployment via Docker Compose

Sock Shop was started using:

```bash
docker-compose -f deploy/docker-compose/docker-compose.yml up -d
```

Validation checks:
- Compose services reached `Up` state.
- Frontend returned `HTTP 200` on `http://localhost/`.

### 2) Integration test suite

A lightweight integration test suite was added under `integration-tests/` using `pytest` + `requests`.

Files added:
- `integration-tests/test_sockshop.py`
- `integration-tests/requirements.txt`
- `integration-tests/Dockerfile`
- `deploy/docker-compose/docker-compose.integration.yml`

## Test Coverage

The implemented tests are black-box integration checks through `edge-router`, validating app behavior across service boundaries.

### Test 1: Frontend availability

- Endpoint: `/`
- Validation:
  - service responds with HTTP 200
  - response content type is HTML
- Purpose:
  - ensures routing + frontend container are reachable as a user entrypoint.

### Test 2: Catalogue integration

- Endpoint: `/catalogue?size=3`
- Validation:
  - HTTP 200
  - response is a JSON list
  - list has at least one product
  - product includes required fields (`id`, `name`, `price`)
- Purpose:
  - validates integration between router, catalogue service, and catalogue data source.

### Test 3: Tags integration

- Endpoint: `/tags`
- Validation:
  - HTTP 200
  - JSON object includes `tags`
  - `tags` is a non-empty list
- Purpose:
  - validates a commonly used filter metadata API used by the storefront.

### Test 4: Catalogue field contract

- Endpoint: `/catalogue?size=5`
- Validation:
  - HTTP 200
  - each product has non-empty `id` and `name`
  - `price` is numeric and non-negative
- Purpose:
  - strengthens API contract checks to catch response-shape regressions between services.

### Test 5: Negative path for unknown route

- Endpoint: `/non-existent-route`
- Validation:
  - response is `HTTP 404`
- Purpose:
  - verifies invalid route handling and edge-router error propagation.

### Test 6: Basic latency budget for critical routes

- Endpoints: `/`, `/catalogue?size=3`, `/tags`
- Validation:
  - HTTP 200
  - each response time stays below a lightweight budget (`< 2.5s`)
- Purpose:
  - introduces simple performance guardrails in CI to catch obvious regressions early.

## How Tests Are Executed

The integration tests run as a dedicated Compose service:

```bash
docker-compose -f deploy/docker-compose/docker-compose.yml -f deploy/docker-compose/docker-compose.integration.yml up --build --abort-on-container-exit integration-tests
```

Behavior:
- Builds the integration test container
- Runs `pytest` against the running stack
- Exits with container status code (good for CI)

## Execution Result

- Status: **Passed**
- Result: **6 passed**

## TDD Alignment

The solution follows the TDD spirit from the guideline:
- define expected system behavior as executable tests,
- run tests against real integrated services,
- keep tests fast and focused,
- use test outcomes as a feedback loop for safe changes.

## Current Limitations

The current suite focuses on smoke + basic contract/performance checks and does not yet cover:
- user registration/login flow,
- cart mutation and persistence,
- checkout path (`orders`, `shipping`, `payment`),
- contract-level assertions for every service endpoint.

## Recommended Next Integration Tests

1. **Auth + Session flow**
   - register (or login existing user), verify authenticated endpoint access.
2. **Cart flow**
   - add item to cart, verify item appears, then remove and verify state.
3. **Order/Checkout flow**
   - submit order and verify response/state transitions.

## Documentation Produced

- Runbook: `test.md`
- This report: `final-report.md`

