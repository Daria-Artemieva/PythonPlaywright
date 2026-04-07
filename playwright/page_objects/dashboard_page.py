from .order_hist_page import OrdersHistoryPage


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def select_navigation(self):
        self.page.get_by_role("button", name="ORDERS").click()
        order_history_page = OrdersHistoryPage(self.page)
        return order_history_page