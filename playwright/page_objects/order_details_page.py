from playwright.sync_api import expect


class OrderDetailsPage:
    def __init__(self,page):
        self.page = page

    def verify_order_message(self):
        expect(self.page.get_by_text("Thank you for Shopping With Us")).to_be_visible()
        print("Success")
