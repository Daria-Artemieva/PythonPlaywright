import pytest
from pytest_bdd import given, parsers, scenario, then, when

from page_objects.login_page import LoginPage
from utils.api_base_framework import APIUtils


@scenario("Features/order_transaction.feature", "Verify order success message shown in details page")
def test_e2e_web_api_bdd():
    pass


@pytest.fixture
def shared_data():
    return {}


@given(parsers.parse('place the item order with "{userEmail}" and "{userPassword}"'))
def place_item_order(playwright, shared_data, userEmail, userPassword):
    shared_data["userCredentials"] = {
        "userEmail": userEmail,
        "userPassword": userPassword,
    }
    api_utils = APIUtils()
    shared_data["orderId"] = api_utils.create_order(
        playwright, shared_data["userCredentials"]
    )


@given("the user is on landing page")
def open_landing_page(browser_instance, shared_data):
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    shared_data["login_page"] = login_page


@when(parsers.parse('I login to portal with "{userEmail}" and "{userPassword}"'))
def login_with_credentials(shared_data, userEmail, userPassword):
    login_page = shared_data["login_page"]
    shared_data["dashboard_page"] = login_page.login(
        userEmail, userPassword
    )


@when("navigate to orders page")
def navigate_to_orders(shared_data):
    shared_data["order_history_page"] = shared_data["dashboard_page"].select_navigation()


@when("select the orderId")
def open_order_details(shared_data):
    shared_data["order_details_page"] = shared_data["order_history_page"].select_order(
        shared_data["orderId"]
    )


@then("order message is successfully displayed")
def verify_order_message(shared_data):
    shared_data["order_details_page"].verify_order_message()
