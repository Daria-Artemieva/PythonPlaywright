import json
from pathlib import Path

import pytest
from playwright.sync_api import Playwright, expect

from page_objects.login_page import LoginPage
from page_objects.dashboard_page import DashboardPage
from conftest import browser_instance
from utils.api_base_framework import APIUtils

#JSON file -> util -> access into test.
     #create order->order ID
credentials_path = Path(__file__).parent / "data" / "credentials.json"

with credentials_path.open() as f:
     test_data = json.load(f)
     print(test_data)
     user_credentials_list = test_data["user_credentials"]

@pytest.mark.smoke
@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_e2e_web_api(playwright: Playwright, user_credentials, browser_instance):
     user_email = user_credentials["userEmail"]
     user_password = user_credentials["userPassword"]

     apiutils = APIUtils()
     order_id = apiutils.create_order(playwright, user_credentials)
     #login
     login_page = LoginPage(browser_instance)
     login_page.navigate()
     dashboard_page = login_page.login(user_email, user_password)
     #dashboard page->
     order_history_page = dashboard_page.select_navigation()
     # orders History page->
     order_details_page = order_history_page.select_order(order_id)
     # order details page
     order_details_page.verify_order_message()


