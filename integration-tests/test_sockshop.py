import os
import time

import pytest
import requests


BASE_URL = os.environ.get("SOCKSHOP_BASE_URL", "http://edge-router")
TIMEOUT_SECONDS = 5
LATENCY_BUDGET_SECONDS = 2.5
pytestmark = pytest.mark.frontend_backend


@pytest.fixture(autouse=True)
def log_test_case(request):
    test_name = request.node.name
    print(f"[TEST-START][frontend-backend] {test_name}")
    yield
    print(f"[TEST-END][frontend-backend] {test_name}")


def log_http_result(label: str, method: str, url: str, response: requests.Response) -> None:
    print(
        f"[HTTP][{label}] {method} {url} -> status={response.status_code} "
        f"elapsed_ms={int(response.elapsed.total_seconds() * 1000)} "
        f"content_type={response.headers.get('Content-Type', 'unknown')}"
    )


def wait_until_ready(path: str = "/", retries: int = 30, delay_seconds: int = 2) -> requests.Response:
    last_error = None
    for _ in range(retries):
        try:
            response = requests.get(f"{BASE_URL}{path}", timeout=TIMEOUT_SECONDS)
            if response.status_code == 200:
                log_http_result("readiness", "GET", f"{BASE_URL}{path}", response)
                return response
        except requests.RequestException as err:
            last_error = err
        time.sleep(delay_seconds)
    raise AssertionError(f"Sock Shop did not become ready at {BASE_URL}{path}. Last error: {last_error}")


def test_home_page_is_served():
    response = wait_until_ready("/")
    assert "text/html" in response.headers.get("Content-Type", "")


def test_catalogue_returns_products():
    wait_until_ready("/")
    response = requests.get(f"{BASE_URL}/catalogue?size=3", timeout=TIMEOUT_SECONDS)
    log_http_result("catalogue-products", "GET", f"{BASE_URL}/catalogue?size=3", response)
    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) >= 1
    first_product = payload[0]
    assert "id" in first_product
    assert "name" in first_product
    assert "price" in first_product


def test_tags_returns_expected_shape():
    wait_until_ready("/")
    response = requests.get(f"{BASE_URL}/tags", timeout=TIMEOUT_SECONDS)
    log_http_result("tags", "GET", f"{BASE_URL}/tags", response)
    assert response.status_code == 200

    payload = response.json()
    assert "tags" in payload
    assert isinstance(payload["tags"], list)
    assert len(payload["tags"]) >= 1


def test_catalogue_product_fields_have_expected_types():
    wait_until_ready("/")
    response = requests.get(f"{BASE_URL}/catalogue?size=5", timeout=TIMEOUT_SECONDS)
    log_http_result("catalogue-types", "GET", f"{BASE_URL}/catalogue?size=5", response)
    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) >= 1
    for product in payload:
        assert isinstance(product.get("id"), str)
        assert product["id"] != ""
        assert isinstance(product.get("name"), str)
        assert product["name"] != ""
        assert isinstance(product.get("price"), (int, float))
        assert product["price"] >= 0


def test_unknown_route_returns_404():
    wait_until_ready("/")
    response = requests.get(f"{BASE_URL}/non-existent-route", timeout=TIMEOUT_SECONDS)
    log_http_result("unknown-route", "GET", f"{BASE_URL}/non-existent-route", response)
    assert response.status_code == 404


def test_core_endpoints_respond_within_latency_budget():
    wait_until_ready("/")
    for path in ("/", "/catalogue?size=3", "/tags"):
        response = requests.get(f"{BASE_URL}{path}", timeout=TIMEOUT_SECONDS)
        log_http_result("latency-budget", "GET", f"{BASE_URL}{path}", response)
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < LATENCY_BUDGET_SECONDS
