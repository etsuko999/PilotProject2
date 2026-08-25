import pytest
from playwright.sync_api import Page, expect


class HomePage:
	"""Landing page at /."""

	URL = "https://automationexercise.com/"

	def __init__(self, page: Page):
		self.page = page
		self.delete_account_link = page.locator("//a[@href='/delete_account']")
		self.home_page_text = page.locator("h2").filter(has_text="Features Items")
		self.product_link = page.locator("[href='/products']")
		self.cart_link = page.get_by_role("link", name=" Cart")
		
		self.subscription_email_field = page.locator("input#susbscribe_email")
		self.subscription_title = page.locator("h2").filter(has_text="Subscription")
		self.subscription_arrow_icon = page.locator("//button[@id='subscribe']")
		self.sucess_message = page.locator("//div[contains(@class,'alert-success alert')]")

	def delete_account(self):
		self.delete_account_link.click()

	def goto(self):
		self.page.goto(self.URL)

	def is_home_page_text_visible(self):
		expect(self.home_page_text).to_be_visible()
		return True

	def navigate_to_products_page(self):
		self.product_link.click()

	def navigate_to_cart_page(self):
		self.cart_link.click()

	def homepage_subscribe(self, email: str):
		self.subscription_email_field.scroll_into_view_if_needed()
		expect(self.subscription_title).to_be_visible()
		self.subscription_email_field.fill(email)
		self.subscription_arrow_icon.click()
		self.sucess_message.wait_for(state="visible", timeout=5000)
		
	def close(self):
		self.page.close()        