import time

from playwright.async_api import Playwright
from playwright.sync_api import Page, expect

from conftest import launch_browser


def test_playwright_basics(playwright):
     browser = launch_browser(playwright, "chrome")
     context = browser.new_context()
     page = context.new_page()
     page.goto("https://rahulshettyacademy.com")

#chromium headless mode, 1 single context
def test_playwright_shortcut(page : Page ):
     page.goto("https://rahulshettyacademy.com")

def test_core_locators(page : Page):
     page.goto("https://rahulshettyacademy.com/loginpagePractise/")
     page.get_by_label("Username:").fill("rahulshettyacademy")
     page.get_by_label("Password:").fill("Learning@830$3mK21") #Learning@830$3mK2
     page.locator("#terms").check()
     page.get_by_role("combobox").select_option("teach")
     page.get_by_role("link", name="terms and conditions").click()
     page.get_by_role("button", name="Sign In ").click()
     #incorrect password assertion
     expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
     time.sleep(5)

def test_firefox_browser(playwright: Playwright):
     firefox_browser = launch_browser(playwright, "firefox")
     page = firefox_browser.new_page()
     page.goto("https://rahulshettyacademy.com/loginpagePractise/")
     page.get_by_label("Username:").fill("rahulshettyacademy")
     page.get_by_label("Password:").fill("Learning@830$3mK21")  # Learning@830$3mK2
     page.locator("#terms").check()
     page.get_by_role("combobox").select_option("teach")
     page.get_by_role("link", name="terms and conditions").click()
     page.get_by_role("button", name="Sign In ").click()
     # incorrect password assertion
     expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
     time.sleep(5)

