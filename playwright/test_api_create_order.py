import json
from pathlib import Path

import pytest

from utils.api_base_framework import APIUtils, order_payload


credentials_path = Path(__file__).parent / "data" / "credentials.json"

with credentials_path.open() as file:
    test_data = json.load(file)
    user_credentials_list = test_data["user_credentials"]


@pytest.mark.smoke
@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_create_order_api_returns_created_order(playwright, user_credentials):
    api_utils = APIUtils()
    token = api_utils.get_token(playwright, user_credentials)
    api_request_context = playwright.request.new_context(
        base_url="https://rahulshettyacademy.com"
    )

    response = api_request_context.post(
        "/api/ecom/order/create-order",
        data=order_payload,
        headers={"Authorization": token, "Content-Type": "application/json"},
    )

    assert response.ok
    response_body = response.json()

    assert response_body["orders"]
    assert len(response_body["orders"]) == len(order_payload["orders"])
    assert all(isinstance(order_id, str) and order_id for order_id in response_body["orders"])
