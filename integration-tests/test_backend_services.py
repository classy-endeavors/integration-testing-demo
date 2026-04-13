import os
import socket
import time
import uuid

import pytest
import requests


TIMEOUT_SECONDS = 5
pytestmark = pytest.mark.backend

CATALOGUE_URL = os.environ.get("SOCKSHOP_CATALOGUE_URL", "http://catalogue")
CARTS_URL = os.environ.get("SOCKSHOP_CARTS_URL", "http://carts")
ORDERS_URL = os.environ.get("SOCKSHOP_ORDERS_URL", "http://orders")
USER_URL = os.environ.get("SOCKSHOP_USER_URL", "http://user")
PAYMENT_URL = os.environ.get("SOCKSHOP_PAYMENT_URL", "http://payment")
SHIPPING_URL = os.environ.get("SOCKSHOP_SHIPPING_URL", "http://shipping")
USER_DB_HOST = os.environ.get("SOCKSHOP_USER_DB_HOST", "user-db")
USER_DB_PORT = int(os.environ.get("SOCKSHOP_USER_DB_PORT", "27017"))
RABBITMQ_HOST = os.environ.get("SOCKSHOP_RABBITMQ_HOST", "rabbitmq")
RABBITMQ_PORT = int(os.environ.get("SOCKSHOP_RABBITMQ_PORT", "5672"))

SERVICE_PROBES = {
    "catalogue": (CATALOGUE_URL, ("/catalogue?size=1", "/health", "/")),
    "carts": (CARTS_URL, ("/health", "/")),
    "orders": (ORDERS_URL, ("/health", "/")),
    "user": (USER_URL, ("/health", "/")),
    "payment": (PAYMENT_URL, ("/health", "/")),
    "shipping": (SHIPPING_URL, ("/health", "/")),
}


@pytest.fixture(autouse=True)
def log_test_case(request):
    test_name = request.node.name
    print(f"[TEST-START][backend] {test_name}")
    yield
    print(f"[TEST-END][backend] {test_name}")


def log_http_result(label: str, method: str, url: str, response: requests.Response) -> None:
    print(
        f"[HTTP][{label}] {method} {url} -> status={response.status_code} "
        f"elapsed_ms={int(response.elapsed.total_seconds() * 1000)} "
        f"content_type={response.headers.get('Content-Type', 'unknown')}"
    )


def log_tcp_result(label: str, host: str, port: int) -> None:
    print(f"[TCP][{label}] reachable {host}:{port}")


def request_with_retries(
    base_url: str,
    path: str,
    retries: int = 20,
    delay_seconds: int = 2,
    service_label: str = "unknown-service",
) -> requests.Response:
    last_error = None
    print(f"[SERVICE][{service_label}] probing GET {base_url}{path}")
    for _ in range(retries):
        try:
            response = requests.get(f"{base_url}{path}", timeout=TIMEOUT_SECONDS)
            if response.status_code < 500:
                log_http_result(f"{service_label}-retry-get", "GET", f"{base_url}{path}", response)
                return response
        except requests.RequestException as err:
            last_error = err
        time.sleep(delay_seconds)
    raise AssertionError(f"Service did not become reachable at {base_url}{path}. Last error: {last_error}")


def request_post_with_retries(
    base_url: str,
    path: str,
    json_payload: dict,
    retries: int = 20,
    delay_seconds: int = 2,
    service_label: str = "unknown-service",
) -> requests.Response:
    last_error = None
    print(f"[SERVICE][{service_label}] probing POST {base_url}{path} payload_keys={list(json_payload.keys())}")
    for _ in range(retries):
        try:
            response = requests.post(
                f"{base_url}{path}",
                json=json_payload,
                timeout=TIMEOUT_SECONDS,
            )
            if response.status_code < 500:
                log_http_result(f"{service_label}-retry-post", "POST", f"{base_url}{path}", response)
                return response
        except requests.RequestException as err:
            last_error = err
        time.sleep(delay_seconds)
    raise AssertionError(f"Service did not accept POST at {base_url}{path}. Last error: {last_error}")


def assert_tcp_port_open(
    host: str,
    port: int,
    retries: int = 30,
    delay_seconds: int = 2,
    service_label: str = "infrastructure",
) -> None:
    last_error = None
    print(f"[SERVICE][{service_label}] probing TCP {host}:{port}")
    for _ in range(retries):
        try:
            with socket.create_connection((host, port), timeout=TIMEOUT_SECONDS):
                log_tcp_result(f"{service_label}-connectivity-check", host, port)
                return
        except OSError as err:
            last_error = err
        time.sleep(delay_seconds)
    raise AssertionError(f"TCP port did not become reachable at {host}:{port}. Last error: {last_error}")


def test_core_backend_services_are_reachable():
    for service_name, (base_url, probe_paths) in SERVICE_PROBES.items():
        print(f"[SERVICE][{service_name}] start reachability checks base_url={base_url}")
        probe_responses = []
        for probe_path in probe_paths:
            response = request_with_retries(base_url, probe_path, service_label=service_name)
            probe_responses.append(response.status_code)
            if response.status_code in (200, 204, 400, 401, 403, 404, 405):
                break
        print(f"[SERVICE][{service_name}] probe_statuses={probe_responses}")
        assert all(status < 500 for status in probe_responses), (
            f"{service_name} returned 5xx for all probes: {probe_responses}"
        )


def test_catalogue_direct_endpoint_returns_products():
    response = request_with_retries(CATALOGUE_URL, "/catalogue?size=3", service_label="catalogue")
    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) >= 1
    first_product = payload[0]
    assert isinstance(first_product.get("id"), str)
    assert first_product["id"] != ""
    assert isinstance(first_product.get("name"), str)
    assert first_product["name"] != ""
    assert isinstance(first_product.get("price"), (int, float))
    assert first_product["price"] >= 0


def test_catalogue_tags_direct_endpoint_returns_tags():
    response = request_with_retries(CATALOGUE_URL, "/tags", service_label="catalogue")
    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, dict)
    assert "tags" in payload
    assert isinstance(payload["tags"], list)


def test_carts_items_endpoint_is_available():
    customer_id = "integration-test-user"
    response = request_with_retries(CARTS_URL, f"/carts/{customer_id}/items", service_label="carts")
    assert response.status_code < 500


def test_user_service_supports_customer_registration_contract():
    username = f"integration-{uuid.uuid4().hex[:10]}"
    payload = {
        "username": username,
        "password": "integration-pass",
        "email": f"{username}@example.test",
    }
    print(f"[DETAIL][user-register] username={username}")

    response = request_post_with_retries(USER_URL, "/register", payload, service_label="user")
    assert response.status_code in (200, 201, 202, 409), (
        f"Unexpected register status code: {response.status_code}, body={response.text}"
    )


def test_user_db_tcp_port_is_reachable_from_test_network():
    assert_tcp_port_open(USER_DB_HOST, USER_DB_PORT, service_label="user-db")


def test_orders_endpoint_is_available_for_customer_query():
    response = request_with_retries(
        ORDERS_URL,
        "/orders?customerId=integration-test-user",
        service_label="orders",
    )
    assert response.status_code in (200, 204, 400, 401, 403, 404), (
        f"Unexpected orders status code: {response.status_code}, body={response.text}"
    )


def test_message_broker_tcp_port_is_reachable():
    assert_tcp_port_open(RABBITMQ_HOST, RABBITMQ_PORT, service_label="rabbitmq")
