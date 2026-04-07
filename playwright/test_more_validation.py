from playwright.sync_api import Page, expect


def test_ui_checks(page: Page):
    #hide/display and placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name = "Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()


    #alert boxes
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name = "Confirm ").click()
    print("done")

    #mouse hover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()
    print("hovered and clicked")

    #frame locator
    frame = page.frame_locator("#courses-iframe")
    frame.get_by_role("link", name = "All Access plan").click()
    expect(frame.locator("body")).to_contain_text(("Happy Subscibers!"))
    print("done")

    #check the price of rice is equal to 37
    #identify the price column
    #identify rice raw
    #extract the price of rice

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator(("th")).count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            column_value = index
            print(f"Price column value is {column_value}")
            break

    rice_row = page.locator("tr").filter(has_text="Rice")
    # extract the price of rice
    rice_price = rice_row.locator("td").nth(column_value).text_content()

    print(rice_price)

    # assertion
    assert rice_price == "37"
    print("test passed")