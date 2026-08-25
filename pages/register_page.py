from playwright.sync_api import Page


class RegisterPage:
	"""Signup form embedded on the /login page."""

	URL = "https://automationexercise.com/login"

	def __init__(self, page: Page):
		self.page = page
		self.name_field = page.get_by_placeholder("Name")
		self.email_field = page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")
		self.signup_button = page.get_by_role("button", name="Signup")

	def goto(self):
		self.page.goto(self.URL)

	def signup(self, name: str, email: str):
		self.name_field.fill(name)
		self.email_field.fill(email)
		self.signup_button.click()
	
	def close(self):
		self.page.close()
