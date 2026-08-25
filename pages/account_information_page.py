from playwright.sync_api import Page


class AccountInformationPage:
	"""Account details form at /signup."""

	URL = "https://automationexercise.com/signup"

	def __init__(self, page: Page):
		self.page = page
		self.header = page.get_by_role("heading", name="Enter Account Information")
		self.title_mr_radio = page.get_by_role("radio", name="Mr.")
		self.title_mrs_radio = page.get_by_role("radio", name="Mrs.")
		self.password_field = page.get_by_label("Password")
		self.first_name_field = page.get_by_label("First name")
		self.last_name_field = page.get_by_label("Last name")
		self.address_field = page.get_by_role("textbox", name="Address * (Street address, P.")
		self.country_select = page.locator("select#country")
		self.city_field = page.get_by_label("City")
		self.state_field = page.get_by_label("State")
		self.zip_code_field = page.locator("#zipcode")
		self.mobile_number_field = page.get_by_label("Mobile Number")
		self.create_account_button = page.get_by_role("button", name="Create Account")

	def fill_account_information(
		self,
		password: str,
		first_name: str,
		last_name: str,
		address: str,
		country: str,
		city: str,
		state: str,
		zip_code: str,
		mobile_number: str,
	):
		self.title_mr_radio.check()
		self.password_field.fill(password)
		self.first_name_field.fill(first_name)
		self.last_name_field.fill(last_name)
		self.address_field.fill(address)
		self.country_select.select_option(country)
		self.city_field.fill(city)
		self.state_field.fill(state)
		self.zip_code_field.fill(zip_code)
		self.mobile_number_field.fill(mobile_number)

	def create_account(self):
		self.create_account_button.click()

	def close(self):
		self.page.close()
