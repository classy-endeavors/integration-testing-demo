# Sock Shop Integration Test Guide

This file explains how to run Sock Shop locally with Docker Compose and execute integration tests in two clear modes, with detailed runtime observability and reproducible report output:

- Frontend-Backend Integration (via `edge-router`)
- Backend-Only Integration (direct service checks)

## Prerequisites

- Docker Desktop installed and running
- Docker Compose available (`docker-compose --version`)
- Repository cloned locally

## 1) Start Sock Shop

From the repository root:

```bash
docker-compose -f deploy/docker-compose/docker-compose.yml up -d
```

Verify services are up:

```bash
docker-compose -f deploy/docker-compose/docker-compose.yml ps
```

Quick smoke check:

```bash
curl -I http://localhost/
```

Expected: `HTTP/1.1 200 OK`

## 2) Run Integration Tests

### Option A: Run both suites with one script (recommended)

From `microservices-demo/`:

```bash
bash run_integration_suites.sh
```

This runs:
1. Frontend-Backend Integration
2. Backend-Only Integration

Output is clearly labeled with:
- `RUNNING: <suite-name>`
- `RESULT: PASS|FAIL`
- `OVERALL RESULT: PASS|FAIL`
- Per-test logs (`[TEST-START]`, `[TEST-END]`)
- Per-service logs (`[SERVICE][catalogue]`, `[SERVICE][user]`, etc.)
- Request/response details (`[HTTP]` status, latency, content-type)
- Infra connectivity details (`[TCP]` for `user-db` and `rabbitmq`)

After each run, the script overwrites a Markdown report file:

- `output/integration-test-latest.md`

The report includes timestamp, suite-level results, overall result, and full raw console output.

### Option B: Run one suite at a time

From `microservices-demo/`:

```bash
make test-integration-frontend-backend
make test-integration-backend-only
```

Or directly with Docker Compose:

```bash
TEST_SUITE=frontend-backend docker compose -f deploy/docker-compose/docker-compose.yml -f deploy/docker-compose/docker-compose.integration.yml run --build --rm integration-tests
TEST_SUITE=backend-only docker compose -f deploy/docker-compose/docker-compose.yml -f deploy/docker-compose/docker-compose.integration.yml run --build --rm integration-tests
```

## 3) What Is Being Tested

### Frontend-Backend suite

Tests in `integration-tests/test_sockshop.py`:

- Home page is reachable (`/`)
- Catalogue API returns products (`/catalogue?size=3`)
- Tags API returns a non-empty list (`/tags`)
- Catalogue products include stable field types and non-empty values (`/catalogue?size=5`)
- Unknown route returns `404` (`/non-existent-route`)
- Core endpoints meet a basic response-time budget (`/`, `/catalogue`, `/tags`)

### Backend-Only suite

Tests in `integration-tests/test_backend_services.py`:

- Core backend services are reachable without `5xx` (`catalogue`, `carts`, `orders`, `user`, `payment`, `shipping`)
- Catalogue direct API returns products with expected types (`/catalogue?size=3`)
- Catalogue tags direct API returns expected shape (`/tags`)
- Carts items endpoint is available (`/carts/{customer_id}/items`)
- User service contract checks (customer lookup/registration paths) validate response shape and status behavior
- User database integration checks validate `user-db` network reachability from the integration test container (`user-db:27017`)
- Order service contract checks validate order query path behavior (`/orders?customerId=...`)
- Message broker integration checks validate RabbitMQ network reachability (`rabbitmq:5672`)

### Expanded service coverage requested

The integration scope now explicitly includes:

- `user` service + `user-db`
- `catalogue` service (API contracts + tags + product schema)
- `orders` service
- message broker interaction for order workflow events

## 4) Re-run Only Tests

If Sock Shop is already running, use either:

```bash
make test-integration-frontend-backend
make test-integration-backend-only
```

## 5) View Logs (if tests fail)

```bash
docker compose -f deploy/docker-compose/docker-compose.yml logs edge-router
docker compose -f deploy/docker-compose/docker-compose.yml logs catalogue
docker compose -f deploy/docker-compose/docker-compose.yml logs front-end
```

Also inspect the latest generated Markdown run report:

```bash
cat output/integration-test-latest.md
```

## 6) Stop and Clean Up

Stop only app stack:

```bash
docker compose -f deploy/docker-compose/docker-compose.yml down
```

Stop app stack and remove volumes (full reset):

```bash
docker compose -f deploy/docker-compose/docker-compose.yml down -v
```

