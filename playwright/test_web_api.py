from playwright.sync_api import Playwright, expect

from conftest import launch_browser
from utils.api_base import APIUtils


def test_e2e_web_api(playwright: Playwright):
     browser = launch_browser(playwright, "chrome")
     context = browser.new_context()
     page = context.new_page()

     #create order->order ID

     apiutils = APIUtils()
     order_id = apiutils.create_order(playwright)


     #login
     page.goto("https://rahulshettyacademy.com/client/")
     page.get_by_placeholder("email@example.com").fill("123bug456report@gmail.com")
     page.get_by_placeholder("enter your passsword").fill("Coco2004!")
     page.get_by_role("button", name="Login").click()

     #orders History page->

     page.get_by_role("button", name="ORDERS").click()

     row = page.locator("tr", has_text=order_id)
     expect(row).to_be_visible()
     row.get_by_role("button", name="View").click()
#     order_row = page.get_by_text(order_id)
#     expect(order_row).to_be_visible()
#     page.get_by_role("button", name="View").nth(0).click()
     expect(page.get_by_text("Thank you for Shopping With Us")).to_be_visible()
     print("Success")
     context.close()

