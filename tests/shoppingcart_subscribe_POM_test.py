import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
# from pages.view_cart_page import ViewCartPage as ShoppingCartPage
from pages.view_cart_page import ViewCartPage

def test_cart_subscription(page: Page):
    home_page = HomePage(page)  
    home_page.goto()
    home_page.is_home_page_text_visible()

    go_to_cart_link = home_page.cart_link
    go_to_cart_link.click()
    
    view_cart_page = ViewCartPage(page)
    if view_cart_page.scroll_to_footer():
        view_cart_page.shopping_cart_page_subscribe("test@example.com")
    else:
        # pytest.fail("Subscription title is not visible after scrolling to footer.")
        pytest.fail("Failed to scroll to footer.")

    expect(view_cart_page.sucess_message).to_be_visible()

    view_cart_page.close()
    home_page.close()