import pytest
from playwright.sync_api import Page, expect

URL = "https://automationexercise.com/login"

def test_register_one(page: Page):
        page.goto(URL)
        page.locator("body").click()
        email_field = page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")
        email_field.fill("capricorntest01@example.com")
        password_field = page.get_by_role("textbox", name="Password")
        password_field.fill("capricorntest01")

        login_button = page.get_by_role("button", name="Login")
        login_button.click()

        # Next page
        header =page.get_by_role("heading", name="Features Items")
        expect(header).to_be_visible()