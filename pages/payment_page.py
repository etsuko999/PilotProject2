from playwright.sync_api import Page


class PaymentPage:
    URL = "https://automationexercise.com/payment"

    def __init__(self, page: Page):
        self.page = page
        self.place_order_btn = page.get_by_text("Place Order")
        self.name_on_card_field = page.locator("input[name='name_on_card']")
        self.card_number_field = page.locator("input[name='card_number']")
        self.cvc_field = page.get_by_placeholder("ex. 311")
        self.expiration_month_field = page.get_by_placeholder("MM")
        self.expiration_year_field = page.get_by_placeholder("YYYY")
        self.pay_and_confirm_order_btn = page.get_by_text("Pay and Confirm Order")

        self.order_placed_text = page.get_by_text("Order Placed!")

    def goto(self):
        self.page.goto(self.URL)

    def fill_payment_details(
            self, 
            name: str, 
            card_number: str, 
            cvc: str, 
            expiration_month: str, 
            expiration_year: str
        ):
        self.name_on_card_field.fill(name)
        self.card_number_field.fill(card_number)
        self.cvc_field.fill(cvc)
        self.expiration_month_field.fill(expiration_month)
        self.expiration_year_field.fill(expiration_year)

    def pay_and_confirm_order(self):
        self.pay_and_confirm_order_btn.click()
        self.order_placed_text.wait_for(state="visible", timeout=5000) 

    def close(self):
        self.page.close()
