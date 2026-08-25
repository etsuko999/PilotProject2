from playwright.sync_api import Page


class CheckOutPage:
    URL = "https://automationexercise.com/checkout"

    def __init__(self, page: Page):
        self.page = page
        self.place_order_btn = page.get_by_text("Place Order")


    def goto(self):
        self.page.goto(self.URL)

    def go_to_payment(self):
        self.place_order_btn.click()

    def close(self):
        self.page.close()
