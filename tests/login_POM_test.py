from utils.data import TEST_EMAIL, TEST_PASSWORD 
import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage



def test_login_one(page: Page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(TEST_EMAIL, TEST_PASSWORD)

        # Next page
        expect(login_page.features_items_header).to_be_visible()
        page.close()


def test_login_password(page: Page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("capricorntest01@example.com", "wrongpassword")

        # Check for error message
        expect(login_page.error_message).to_be_visible()
        login_page.close()
