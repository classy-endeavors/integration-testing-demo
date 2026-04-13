# Integration Test Run Output

- Date: 2026-04-13 19:23:21 IST
- Frontend-Backend Integration: PASS
- Backend-Only Integration: PASS
- Overall Result: PASS

## Full Console Output

```text
========================================================================
RUNNING: Frontend-Backend Integration
========================================================================
time="2026-04-13T19:23:15+05:30" level=warning msg="The \"MYSQL_ROOT_PASSWORD\" variable is not set. Defaulting to a blank string."
time="2026-04-13T19:23:15+05:30" level=warning msg="D:\\workspace\\smarter-codes\\microservices-demo\\deploy\\docker-compose\\docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
 Container docker-compose-edge-router-1  Running
#0 building with "desktop-linux" instance using docker driver

#1 [integration-tests internal] load build definition from Dockerfile
#1 transferring dockerfile: 292B done
#1 DONE 0.0s

#2 [integration-tests internal] load metadata for docker.io/library/python:3.12-slim
#2 DONE 0.9s

#3 [integration-tests internal] load .dockerignore
#3 transferring context: 2B done
#3 DONE 0.0s

#4 [integration-tests internal] load build context
#4 transferring context: 668B done
#4 DONE 0.0s

#5 [integration-tests 1/5] FROM docker.io/library/python:3.12-slim@sha256:804ddf3251a60bbf9c92e73b7566c40428d54d0e79d3428194edf40da6521286
#5 resolve docker.io/library/python:3.12-slim@sha256:804ddf3251a60bbf9c92e73b7566c40428d54d0e79d3428194edf40da6521286 0.0s done
#5 DONE 0.1s

#6 [integration-tests 2/5] WORKDIR /tests
#6 CACHED

#7 [integration-tests 3/5] COPY integration-tests/requirements.txt /tests/requirements.txt
#7 CACHED

#8 [integration-tests 4/5] RUN pip install --no-cache-dir -r /tests/requirements.txt
#8 CACHED

#9 [integration-tests 5/5] COPY integration-tests /tests
#9 CACHED

#10 [integration-tests] exporting to image
#10 exporting layers done
#10 exporting manifest sha256:1728915c749e4049c7c97f1c52d32bea6de9a453200c16c3f9a92d0ec47d6e3c done
#10 exporting config sha256:193becccb4355d304c7fbec729274898d030282d5c37f08c0e526d948c39b14a done
#10 exporting attestation manifest sha256:61e76217216d4745d8354c8c222e3a5ccfecf1f990087802183137c715d40a45
#10 exporting attestation manifest sha256:61e76217216d4745d8354c8c222e3a5ccfecf1f990087802183137c715d40a45 0.0s done
#10 exporting manifest list sha256:aff665c84fa46e3f9250af72d8ea9cd562e32272c79e3311d518ab40794318c3 0.0s done
#10 naming to docker.io/library/docker-compose-integration-tests:latest done
#10 unpacking to docker.io/library/docker-compose-integration-tests:latest done
#10 DONE 0.1s

#11 [integration-tests] resolving provenance for metadata file
#11 DONE 0.0s
========================================================================
RUNNING: All Integration Suites
========================================================================
Command: pytest -s -vv test_sockshop.py test_backend_services.py
------------------------------------------------------------------------
============================= test session starts ==============================
platform linux -- Python 3.12.13, pytest-8.3.5, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /tests
configfile: pytest.ini
collecting ... collected 14 items

test_sockshop.py::test_home_page_is_served [TEST-START][frontend-backend] test_home_page_is_served
[HTTP][readiness] GET http://edge-router/ -> status=200 elapsed_ms=3 content_type=text/html; charset=UTF-8
PASSED[TEST-END][frontend-backend] test_home_page_is_served

test_sockshop.py::test_catalogue_returns_products [TEST-START][frontend-backend] test_catalogue_returns_products
[HTTP][readiness] GET http://edge-router/ -> status=200 elapsed_ms=1 content_type=text/html; charset=UTF-8
[HTTP][catalogue-products] GET http://edge-router/catalogue?size=3 -> status=200 elapsed_ms=51 content_type=text/plain; charset=utf-8
PASSED[TEST-END][frontend-backend] test_catalogue_returns_products

test_sockshop.py::test_tags_returns_expected_shape [TEST-START][frontend-backend] test_tags_returns_expected_shape
[HTTP][readiness] GET http://edge-router/ -> status=200 elapsed_ms=3 content_type=text/html; charset=UTF-8
[HTTP][tags] GET http://edge-router/tags -> status=200 elapsed_ms=46 content_type=text/plain; charset=utf-8
PASSED[TEST-END][frontend-backend] test_tags_returns_expected_shape

test_sockshop.py::test_catalogue_product_fields_have_expected_types [TEST-START][frontend-backend] test_catalogue_product_fields_have_expected_types
[HTTP][readiness] GET http://edge-router/ -> status=200 elapsed_ms=2 content_type=text/html; charset=UTF-8
[HTTP][catalogue-types] GET http://edge-router/catalogue?size=5 -> status=200 elapsed_ms=3 content_type=text/plain; charset=utf-8
PASSED[TEST-END][frontend-backend] test_catalogue_product_fields_have_expected_types

test_sockshop.py::test_unknown_route_returns_404 [TEST-START][frontend-backend] test_unknown_route_returns_404
[HTTP][readiness] GET http://edge-router/ -> status=200 elapsed_ms=1 content_type=text/html; charset=UTF-8
[HTTP][unknown-route] GET http://edge-router/non-existent-route -> status=404 elapsed_ms=45 content_type=text/html; charset=utf-8
PASSED[TEST-END][frontend-backend] test_unknown_route_returns_404

test_sockshop.py::test_core_endpoints_respond_within_latency_budget [TEST-START][frontend-backend] test_core_endpoints_respond_within_latency_budget
[HTTP][readiness] GET http://edge-router/ -> status=200 elapsed_ms=1 content_type=text/html; charset=UTF-8
[HTTP][latency-budget] GET http://edge-router/ -> status=200 elapsed_ms=1 content_type=text/html; charset=UTF-8
[HTTP][latency-budget] GET http://edge-router/catalogue?size=3 -> status=200 elapsed_ms=46 content_type=text/plain; charset=utf-8
[HTTP][latency-budget] GET http://edge-router/tags -> status=200 elapsed_ms=47 content_type=text/plain; charset=utf-8
PASSED[TEST-END][frontend-backend] test_core_endpoints_respond_within_latency_budget

test_backend_services.py::test_core_backend_services_are_reachable [TEST-START][backend] test_core_backend_services_are_reachable
[SERVICE][catalogue] start reachability checks base_url=http://catalogue
[SERVICE][catalogue] probing GET http://catalogue/catalogue?size=1
[HTTP][catalogue-retry-get] GET http://catalogue/catalogue?size=1 -> status=200 elapsed_ms=1 content_type=application/json; charset=utf-8
[SERVICE][catalogue] probe_statuses=[200]
[SERVICE][carts] start reachability checks base_url=http://carts
[SERVICE][carts] probing GET http://carts/health
[HTTP][carts-retry-get] GET http://carts/health -> status=200 elapsed_ms=4 content_type=application/json;charset=UTF-8
[SERVICE][carts] probe_statuses=[200]
[SERVICE][orders] start reachability checks base_url=http://orders
[SERVICE][orders] probing GET http://orders/health
[HTTP][orders-retry-get] GET http://orders/health -> status=200 elapsed_ms=4 content_type=application/json;charset=UTF-8
[SERVICE][orders] probe_statuses=[200]
[SERVICE][user] start reachability checks base_url=http://user
[SERVICE][user] probing GET http://user/health
[HTTP][user-retry-get] GET http://user/health -> status=200 elapsed_ms=1 content_type=application/hal+json
[SERVICE][user] probe_statuses=[200]
[SERVICE][payment] start reachability checks base_url=http://payment
[SERVICE][payment] probing GET http://payment/health
[HTTP][payment-retry-get] GET http://payment/health -> status=200 elapsed_ms=1 content_type=application/json; charset=utf-8
[SERVICE][payment] probe_statuses=[200]
[SERVICE][shipping] start reachability checks base_url=http://shipping
[SERVICE][shipping] probing GET http://shipping/health
[HTTP][shipping-retry-get] GET http://shipping/health -> status=200 elapsed_ms=3 content_type=application/json;charset=UTF-8
[SERVICE][shipping] probe_statuses=[200]
PASSED[TEST-END][backend] test_core_backend_services_are_reachable

test_backend_services.py::test_catalogue_direct_endpoint_returns_products [TEST-START][backend] test_catalogue_direct_endpoint_returns_products
[SERVICE][catalogue] probing GET http://catalogue/catalogue?size=3
[HTTP][catalogue-retry-get] GET http://catalogue/catalogue?size=3 -> status=200 elapsed_ms=1 content_type=application/json; charset=utf-8
PASSED[TEST-END][backend] test_catalogue_direct_endpoint_returns_products

test_backend_services.py::test_catalogue_tags_direct_endpoint_returns_tags [TEST-START][backend] test_catalogue_tags_direct_endpoint_returns_tags
[SERVICE][catalogue] probing GET http://catalogue/tags
[HTTP][catalogue-retry-get] GET http://catalogue/tags -> status=200 elapsed_ms=1 content_type=application/json; charset=utf-8
PASSED[TEST-END][backend] test_catalogue_tags_direct_endpoint_returns_tags

test_backend_services.py::test_carts_items_endpoint_is_available [TEST-START][backend] test_carts_items_endpoint_is_available
[SERVICE][carts] probing GET http://carts/carts/integration-test-user/items
[HTTP][carts-retry-get] GET http://carts/carts/integration-test-user/items -> status=200 elapsed_ms=4 content_type=application/json;charset=UTF-8
PASSED[TEST-END][backend] test_carts_items_endpoint_is_available

test_backend_services.py::test_user_service_supports_customer_registration_contract [TEST-START][backend] test_user_service_supports_customer_registration_contract
[DETAIL][user-register] username=integration-8ea4fd186c
[SERVICE][user] probing POST http://user/register payload_keys=['username', 'password', 'email']
[HTTP][user-retry-post] POST http://user/register -> status=200 elapsed_ms=1 content_type=application/hal+json
PASSED[TEST-END][backend] test_user_service_supports_customer_registration_contract

test_backend_services.py::test_user_db_tcp_port_is_reachable_from_test_network [TEST-START][backend] test_user_db_tcp_port_is_reachable_from_test_network
[SERVICE][user-db] probing TCP user-db:27017
[TCP][user-db-connectivity-check] reachable user-db:27017
PASSED[TEST-END][backend] test_user_db_tcp_port_is_reachable_from_test_network

test_backend_services.py::test_orders_endpoint_is_available_for_customer_query [TEST-START][backend] test_orders_endpoint_is_available_for_customer_query
[SERVICE][orders] probing GET http://orders/orders?customerId=integration-test-user
[HTTP][orders-retry-get] GET http://orders/orders?customerId=integration-test-user -> status=200 elapsed_ms=8 content_type=application/hal+json;charset=UTF-8
PASSED[TEST-END][backend] test_orders_endpoint_is_available_for_customer_query

test_backend_services.py::test_message_broker_tcp_port_is_reachable [TEST-START][backend] test_message_broker_tcp_port_is_reachable
[SERVICE][rabbitmq] probing TCP rabbitmq:5672
[TCP][rabbitmq-connectivity-check] reachable rabbitmq:5672
PASSED[TEST-END][backend] test_message_broker_tcp_port_is_reachable


============================== 14 passed in 0.50s ==============================
------------------------------------------------------------------------
RESULT: PASS (All Integration Suites)
========================================================================
RESULT: PASS (Frontend-Backend Integration)

========================================================================
RUNNING: Backend-Only Integration
========================================================================
time="2026-04-13T19:23:18+05:30" level=warning msg="The \"MYSQL_ROOT_PASSWORD\" variable is not set. Defaulting to a blank string."
time="2026-04-13T19:23:18+05:30" level=warning msg="D:\\workspace\\smarter-codes\\microservices-demo\\deploy\\docker-compose\\docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
 Container docker-compose-edge-router-1  Running
#0 building with "desktop-linux" instance using docker driver

#1 [integration-tests internal] load build definition from Dockerfile
#1 transferring dockerfile: 292B done
#1 DONE 0.0s

#2 [integration-tests internal] load metadata for docker.io/library/python:3.12-slim
#2 DONE 0.4s

#3 [integration-tests internal] load .dockerignore
#3 transferring context: 2B done
#3 DONE 0.0s

#4 [integration-tests internal] load build context
#4 transferring context: 668B done
#4 DONE 0.0s

#5 [integration-tests 1/5] FROM docker.io/library/python:3.12-slim@sha256:804ddf3251a60bbf9c92e73b7566c40428d54d0e79d3428194edf40da6521286
#5 resolve docker.io/library/python:3.12-slim@sha256:804ddf3251a60bbf9c92e73b7566c40428d54d0e79d3428194edf40da6521286 0.0s done
#5 DONE 0.0s

#6 [integration-tests 2/5] WORKDIR /tests
#6 CACHED

#7 [integration-tests 3/5] COPY integration-tests/requirements.txt /tests/requirements.txt
#7 CACHED

#8 [integration-tests 4/5] RUN pip install --no-cache-dir -r /tests/requirements.txt
#8 CACHED

#9 [integration-tests 5/5] COPY integration-tests /tests
#9 CACHED

#10 [integration-tests] exporting to image
#10 exporting layers done
#10 exporting manifest sha256:1728915c749e4049c7c97f1c52d32bea6de9a453200c16c3f9a92d0ec47d6e3c done
#10 exporting config sha256:193becccb4355d304c7fbec729274898d030282d5c37f08c0e526d948c39b14a done
#10 exporting attestation manifest sha256:51e1fbd6fcfc478f56a44a70f7d958b2458a226446d9537b4719497465420ca4 0.0s done
#10 exporting manifest list sha256:636751a334c053a44a215f59bb4c8e4fa804d0434d00e4353885e0983b46937c 0.0s done
#10 naming to docker.io/library/docker-compose-integration-tests:latest
#10 naming to docker.io/library/docker-compose-integration-tests:latest done
#10 unpacking to docker.io/library/docker-compose-integration-tests:latest done
#10 DONE 0.1s

#11 [integration-tests] resolving provenance for metadata file
#11 DONE 0.0s
========================================================================
RUNNING: All Integration Suites
========================================================================
Command: pytest -s -vv test_sockshop.py test_backend_services.py
------------------------------------------------------------------------
============================= test session starts ==============================
platform linux -- Python 3.12.13, pytest-8.3.5, pluggy-1.6.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /tests
configfile: pytest.ini
collecting ... collected 14 items

test_sockshop.py::test_home_page_is_served [TEST-START][frontend-backend] test_home_page_is_served
[HTTP][readiness] GET http://edge-router/ -> status=200 elapsed_ms=2 content_type=text/html; charset=UTF-8
PASSED[TEST-END][frontend-backend] test_home_page_is_served

test_sockshop.py::test_catalogue_returns_products [TEST-START][frontend-backend] test_catalogue_returns_products
[HTTP][readiness] GET http://edge-router/ -> status=200 elapsed_ms=1 content_type=text/html; charset=UTF-8
[HTTP][catalogue-products] GET http://edge-router/catalogue?size=3 -> status=200 elapsed_ms=46 content_type=text/plain; charset=utf-8
PASSED[TEST-END][frontend-backend] test_catalogue_returns_products

test_sockshop.py::test_tags_returns_expected_shape [TEST-START][frontend-backend] test_tags_returns_expected_shape
[HTTP][readiness] GET http://edge-router/ -> status=200 elapsed_ms=2 content_type=text/html; charset=UTF-8
[HTTP][tags] GET http://edge-router/tags -> status=200 elapsed_ms=44 content_type=text/plain; charset=utf-8
PASSED[TEST-END][frontend-backend] test_tags_returns_expected_shape

test_sockshop.py::test_catalogue_product_fields_have_expected_types [TEST-START][frontend-backend] test_catalogue_product_fields_have_expected_types
[HTTP][readiness] GET http://edge-router/ -> status=200 elapsed_ms=1 content_type=text/html; charset=UTF-8
[HTTP][catalogue-types] GET http://edge-router/catalogue?size=5 -> status=200 elapsed_ms=3 content_type=text/plain; charset=utf-8
PASSED[TEST-END][frontend-backend] test_catalogue_product_fields_have_expected_types

test_sockshop.py::test_unknown_route_returns_404 [TEST-START][frontend-backend] test_unknown_route_returns_404
[HTTP][readiness] GET http://edge-router/ -> status=200 elapsed_ms=1 content_type=text/html; charset=UTF-8
[HTTP][unknown-route] GET http://edge-router/non-existent-route -> status=404 elapsed_ms=42 content_type=text/html; charset=utf-8
PASSED[TEST-END][frontend-backend] test_unknown_route_returns_404

test_sockshop.py::test_core_endpoints_respond_within_latency_budget [TEST-START][frontend-backend] test_core_endpoints_respond_within_latency_budget
[HTTP][readiness] GET http://edge-router/ -> status=200 elapsed_ms=2 content_type=text/html; charset=UTF-8
[HTTP][latency-budget] GET http://edge-router/ -> status=200 elapsed_ms=1 content_type=text/html; charset=UTF-8
[HTTP][latency-budget] GET http://edge-router/catalogue?size=3 -> status=200 elapsed_ms=50 content_type=text/plain; charset=utf-8
[HTTP][latency-budget] GET http://edge-router/tags -> status=200 elapsed_ms=47 content_type=text/plain; charset=utf-8
PASSED[TEST-END][frontend-backend] test_core_endpoints_respond_within_latency_budget

test_backend_services.py::test_core_backend_services_are_reachable [TEST-START][backend] test_core_backend_services_are_reachable
[SERVICE][catalogue] start reachability checks base_url=http://catalogue
[SERVICE][catalogue] probing GET http://catalogue/catalogue?size=1
[HTTP][catalogue-retry-get] GET http://catalogue/catalogue?size=1 -> status=200 elapsed_ms=1 content_type=application/json; charset=utf-8
[SERVICE][catalogue] probe_statuses=[200]
[SERVICE][carts] start reachability checks base_url=http://carts
[SERVICE][carts] probing GET http://carts/health
[HTTP][carts-retry-get] GET http://carts/health -> status=200 elapsed_ms=3 content_type=application/json;charset=UTF-8
[SERVICE][carts] probe_statuses=[200]
[SERVICE][orders] start reachability checks base_url=http://orders
[SERVICE][orders] probing GET http://orders/health
[HTTP][orders-retry-get] GET http://orders/health -> status=200 elapsed_ms=4 content_type=application/json;charset=UTF-8
[SERVICE][orders] probe_statuses=[200]
[SERVICE][user] start reachability checks base_url=http://user
[SERVICE][user] probing GET http://user/health
[HTTP][user-retry-get] GET http://user/health -> status=200 elapsed_ms=1 content_type=application/hal+json
[SERVICE][user] probe_statuses=[200]
[SERVICE][payment] start reachability checks base_url=http://payment
[SERVICE][payment] probing GET http://payment/health
[HTTP][payment-retry-get] GET http://payment/health -> status=200 elapsed_ms=0 content_type=application/json; charset=utf-8
[SERVICE][payment] probe_statuses=[200]
[SERVICE][shipping] start reachability checks base_url=http://shipping
[SERVICE][shipping] probing GET http://shipping/health
[HTTP][shipping-retry-get] GET http://shipping/health -> status=200 elapsed_ms=3 content_type=application/json;charset=UTF-8
[SERVICE][shipping] probe_statuses=[200]
PASSED[TEST-END][backend] test_core_backend_services_are_reachable

test_backend_services.py::test_catalogue_direct_endpoint_returns_products [TEST-START][backend] test_catalogue_direct_endpoint_returns_products
[SERVICE][catalogue] probing GET http://catalogue/catalogue?size=3
[HTTP][catalogue-retry-get] GET http://catalogue/catalogue?size=3 -> status=200 elapsed_ms=1 content_type=application/json; charset=utf-8
PASSED[TEST-END][backend] test_catalogue_direct_endpoint_returns_products

test_backend_services.py::test_catalogue_tags_direct_endpoint_returns_tags [TEST-START][backend] test_catalogue_tags_direct_endpoint_returns_tags
[SERVICE][catalogue] probing GET http://catalogue/tags
[HTTP][catalogue-retry-get] GET http://catalogue/tags -> status=200 elapsed_ms=0 content_type=application/json; charset=utf-8
PASSED[TEST-END][backend] test_catalogue_tags_direct_endpoint_returns_tags

test_backend_services.py::test_carts_items_endpoint_is_available [TEST-START][backend] test_carts_items_endpoint_is_available
[SERVICE][carts] probing GET http://carts/carts/integration-test-user/items
[HTTP][carts-retry-get] GET http://carts/carts/integration-test-user/items -> status=200 elapsed_ms=3 content_type=application/json;charset=UTF-8
PASSED[TEST-END][backend] test_carts_items_endpoint_is_available

test_backend_services.py::test_user_service_supports_customer_registration_contract [TEST-START][backend] test_user_service_supports_customer_registration_contract
[DETAIL][user-register] username=integration-45d0cb129a
[SERVICE][user] probing POST http://user/register payload_keys=['username', 'password', 'email']
[HTTP][user-retry-post] POST http://user/register -> status=200 elapsed_ms=1 content_type=application/hal+json
PASSED[TEST-END][backend] test_user_service_supports_customer_registration_contract

test_backend_services.py::test_user_db_tcp_port_is_reachable_from_test_network [TEST-START][backend] test_user_db_tcp_port_is_reachable_from_test_network
[SERVICE][user-db] probing TCP user-db:27017
[TCP][user-db-connectivity-check] reachable user-db:27017
PASSED[TEST-END][backend] test_user_db_tcp_port_is_reachable_from_test_network

test_backend_services.py::test_orders_endpoint_is_available_for_customer_query [TEST-START][backend] test_orders_endpoint_is_available_for_customer_query
[SERVICE][orders] probing GET http://orders/orders?customerId=integration-test-user
[HTTP][orders-retry-get] GET http://orders/orders?customerId=integration-test-user -> status=200 elapsed_ms=6 content_type=application/hal+json;charset=UTF-8
PASSED[TEST-END][backend] test_orders_endpoint_is_available_for_customer_query

test_backend_services.py::test_message_broker_tcp_port_is_reachable [TEST-START][backend] test_message_broker_tcp_port_is_reachable
[SERVICE][rabbitmq] probing TCP rabbitmq:5672
[TCP][rabbitmq-connectivity-check] reachable rabbitmq:5672
PASSED[TEST-END][backend] test_message_broker_tcp_port_is_reachable


============================== 14 passed in 0.42s ==============================
------------------------------------------------------------------------
RESULT: PASS (All Integration Suites)
========================================================================
RESULT: PASS (Backend-Only Integration)

========================================================================
OVERALL SUMMARY
========================================================================
- Frontend-Backend Integration: PASS
- Backend-Only Integration: PASS
OVERALL RESULT: PASS
```
