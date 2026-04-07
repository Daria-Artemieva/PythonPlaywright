import time
from os import name

from playwright.sync_api import Page, expect


#iPhone X and Nokia EDGE add to cart and verify if they are visible
def test_ui_validation_dynamic_script(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")  # Learning@830$3mK2
    page.locator("#terms").check()
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In ").click()
    iphone_product = page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button").click()
    nokia_product = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_product.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    time.sleep(5)


def test_child_window_handle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as new_page_info:
        page.get_by_role("link", name = "Free Access to InterviewQues/ResumeAssistance/Material").click() #opens new page
        child_page = new_page_info.value
        text = child_page.locator(".red").text_content()
        print(text)
        words = text.split(("at "))
        email = words[1].split(" ")[0]
        print(email)
        assert email == "mentor@rahulshettyacademy.com"
        time.sleep(5)
