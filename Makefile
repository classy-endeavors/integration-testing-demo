.PHONY: gen-complete-demo
gen-complete-demo:
	make -C deploy/kubernetes docker-gen-complete-demo

.PHONY: check-generated-files
check-generated-files:
	make -C deploy/kubernetes docker-check-complete-demo

.PHONY: test-integration-all
test-integration-all:
	docker compose -f deploy/docker-compose/docker-compose.yml -f deploy/docker-compose/docker-compose.integration.yml run --build --rm integration-tests

.PHONY: test-integration-frontend-backend
test-integration-frontend-backend:
	TEST_SUITE=frontend-backend docker compose -f deploy/docker-compose/docker-compose.yml -f deploy/docker-compose/docker-compose.integration.yml run --build --rm integration-tests

.PHONY: test-integration-backend-only
test-integration-backend-only:
	TEST_SUITE=backend-only docker compose -f deploy/docker-compose/docker-compose.yml -f deploy/docker-compose/docker-compose.integration.yml run --build --rm integration-tests
