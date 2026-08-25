import pytest
from playwright.sync_api import Page, expect


class ViewCartPage:
	"""Shopping cart page at /view_cart."""
	URL = "https://automationexercise.com/view_cart"

	def __init__(self, page: Page):
		self.page = page
		
		self.proceed_to_checkout_btn = page.get_by_text("Proceed To Checkout")
		self.login_link = page.get_by_role("link", name="Register / Login")

		self.shopping_cart_text = page.get_by_text("Shopping Cart")
		self.footer = page.locator("div.footer-widget")

		# This is for suscription section at the bottom of the page
		self.subscription_email_address = page.get_by_placeholder("Your email address")
		self.subscription_arrow_icon = page.locator("//button[@id='subscribe']")
		self.subscription_title = page.get_by_role("heading", name="Subscription").click()

		self.sucess_message = page.locator("//div[contains(@class,'alert-success alert')]")

	def goto(self):
		self.page.goto(self.URL)

	def is_shopping_cart_text_visible(self):
		expect(self.shopping_cart_text).to_be_visible()
		return True
	
	def go_to_checkout(self):
		self.proceed_to_checkout_btn.click()

	def navigate_to_login_page(self):
		self.login_link.click()
	
	def scroll_to_footer(self):
		self.footer.scroll_into_view_if_needed()
		# expect(self.subscription_title).to_be_visible()
		return True
	'''	
	def is_subscription_title_visible(self):
		expect(self.subscription_title).to_be_visible()
		return True
	'''
	
	def shopping_cart_page_subscribe(self, email: str):
		self.subscription_email_address.fill(email)
		self.subscription_arrow_icon.click()
		self.sucess_message.wait_for(state="visible", timeout=5000)

	def close(self):
		self.page.close()
        