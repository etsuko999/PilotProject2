import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def page():
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=True)
        return browser.new_page()
        