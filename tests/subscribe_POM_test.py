import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
# from pages.home_page import HomePage


def test_subscription(page: Page):
    home_page = HomePage(page)
    home_page.goto()
    home_page.is_home_page_text_visible()
    home_page.homepage_subscribe("pic@example.com")

    home_page.close()


