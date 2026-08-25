from playwright.sync_api import Page


class AccountCreatedPage:
	"""Confirmation page at /account_created."""

	URL = "https://automationexercise.com/account_created"

	def __init__(self, page: Page):
		self.page = page
		self.continue_button = page.get_by_text("Continue")

	def continue_to_home(self):
		self.continue_button.click()

	def close(self):
		self.page.close()