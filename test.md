# Sock Shop Integration Test Guide

This file explains how to run Sock Shop locally with Docker Compose and execute the integration tests.

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

## 2) Run Integration Tests (Docker Compose)

Run tests using the integration override file:

```bash
docker-compose -f deploy/docker-compose/docker-compose.yml -f deploy/docker-compose/docker-compose.integration.yml up --build --abort-on-container-exit integration-tests
```

What this does:
- Builds and starts the `integration-tests` container
- Runs `pytest` against the running Sock Shop stack
- Stops after tests complete

Expected success output includes:

```text
6 passed
```

## 3) What Is Being Tested

Current tests are in `integration-tests/test_sockshop.py`:

- Home page is reachable (`/`)
- Catalogue API returns products (`/catalogue?size=3`)
- Tags API returns a non-empty list (`/tags`)
- Catalogue products include stable field types and non-empty values (`/catalogue?size=5`)
- Unknown route returns `404` (`/non-existent-route`)
- Core endpoints meet a basic response-time budget (`/`, `/catalogue`, `/tags`)

## 4) Re-run Only Tests

If Sock Shop is already running, re-run just integration tests:

```bash
docker-compose -f deploy/docker-compose/docker-compose.yml -f deploy/docker-compose/docker-compose.integration.yml up --build --abort-on-container-exit integration-tests
```

## 5) View Logs (if tests fail)

```bash
docker-compose -f deploy/docker-compose/docker-compose.yml logs edge-router
docker-compose -f deploy/docker-compose/docker-compose.yml logs catalogue
docker-compose -f deploy/docker-compose/docker-compose.yml logs front-end
```

## 6) Stop and Clean Up

Stop only app stack:

```bash
docker-compose -f deploy/docker-compose/docker-compose.yml down
```

Stop app stack and remove volumes (full reset):

```bash
docker-compose -f deploy/docker-compose/docker-compose.yml down -v
```

