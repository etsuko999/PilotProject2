import pytest
from playwright.sync_api import Page, expect

URL = "https://automationexercise.com/login"

def test_register_one(page: Page):
        page.goto(URL)

        input_field = page.get_by_placeholder("Name")
        input_field.fill("capricorntest02")
        email_field = page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")
        email_field.fill("capricorntest02@example.com")
        # signup_button = page.locator("form").filter(has_text="Signup").get_by_role("button", name="Signup")
        signup_button = page.get_by_role("button", name="Signup")
        signup_button.click()

        # Next page
        header = page.get_by_role("heading", name="Enter Account Information")
        expect(header).to_be_visible()
        radio_button = page.get_by_role("radio", name="Mr.")
        radio_button.check()
        password_field = page.get_by_label("Password")
        password_field.fill("capricorntest02")
        first_name_field = page.get_by_label("First name")
        first_name_field.fill("John")
        last_name_field = page.get_by_label("Last name")
        last_name_field.fill("Doe")
        # address_field = page.locator("//input[@id=address1]")
        address_field = page.get_by_role("textbox", name="Address * (Street address, P.")
        address_field.fill("123 Main St")

        page.locator('select#country').select_option('United States')

        city_field = page.get_by_label("City")
        city_field.fill("New York")
        state_field = page.get_by_label("State")
        state_field.fill("NY")
        # zip_code_field = page.get_by_label("Zipcode *")
        zip_code_field = page.locator("#zipcode")
        zip_code_field.fill("10001")
        mobile_number_field = page.get_by_label("Mobile Number")
        mobile_number_field.fill("1234567890")

        create_account_button = page.get_by_role("button", name="Create Account")
        create_account_button.click()

        # Continue button
        page.get_by_text("Continue").click()   

        # Delete account link
        page.locator("//a[@href='/delete_account']").click() 

        # browser.close()
