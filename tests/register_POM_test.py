import pytest
from playwright.sync_api import Page, expect

from pages.register_page import RegisterPage
from pages.account_information_page import AccountInformationPage
from pages.account_created_page import AccountCreatedPage
from pages.home_page import HomePage


def test_register_one(page: Page):
	register_page = RegisterPage(page)
	register_page.goto()
	register_page.signup("capricorntest02", "capricorntest02@example.com")

	# Next page https://automationexercise.com/signup
	account_info_page = AccountInformationPage(page)
	expect(account_info_page.header).to_be_visible()
	account_info_page.fill_account_information(
		password="capricorntest02",
		first_name="John",
		last_name="Doe",
		address="123 Main St",
		country="United States",
		city="New York",
		state="NY",
		zip_code="10001",
		mobile_number="1234567890",
	)
	account_info_page.create_account()

	# Continue button https://automationexercise.com/account_created
	account_created_page = AccountCreatedPage(page)
	account_created_page.continue_to_home()

	# Delete account link. https://automationexercise.com/
	home_page = HomePage(page)
	home_page.delete_account()

	home_page.close()
	account_created_page.close()
	account_info_page.close()
	register_page.close()
