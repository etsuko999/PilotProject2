from utils.data import TEST_EMAIL, TEST_PASSWORD, CARD_NUMBER, EXPIRATION_MONTH, EXPIRATION_YEAR, CVC
import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.view_cart_page import ViewCartPage
from pages.checkout_page import CheckOutPage
from pages.payment_page import PaymentPage

def test_purchase_one(page: Page):
    home_page = HomePage(page)  
    home_page.goto()
    # Product Link
    home_page.navigate_to_products_page()

    products_page = ProductsPage(page)
    # need to close add
    products_page.close_popup_one()

    # Add first product to cart on Product Page
    products_page.purchase_first_product()
    
    # Click Cart Modal and go to cart.
    products_page.click_view_cart_from_cart_modal()

    view_cart_page = ViewCartPage(page)
    # Proceed to checkout
    view_cart_page.proceed_to_checkout_btn.click()
    # Proceed to checkout - link on the modal
    view_cart_page.navigate_to_login_page()

    # Login Page
    login_page = LoginPage(page)
    login_page.close_login_page_popup()
    login_page.login(TEST_EMAIL, TEST_PASSWORD)

    # Go to Cart Page from the header link of home page
    home_page.navigate_to_cart_page()

    # Proceed to checkout on view cart page
    view_cart_page.proceed_to_checkout_btn.click()

    # On page: https://automationexercise.com/checkout
    checkout_page = CheckOutPage(page)
    checkout_page.go_to_payment()

    # On page: https://automationexercise.com/payment
    payment_page = PaymentPage(page)
    payment_page.fill_payment_details("John Doe", CARD_NUMBER, CVC, EXPIRATION_MONTH, EXPIRATION_YEAR)

    payment_page.pay_and_confirm_order()

    payment_page.close()
    checkout_page.close()
    view_cart_page.close()
    products_page.close()
    login_page.close()
    home_page.close()

