from utils.data import TEST_EMAIL, TEST_PASSWORD, CARD_NUMBER, EXPIRATION_MONTH, EXPIRATION_YEAR, CVC
import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
'''
@pytest.fixture(scope="session")
def login_page(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(TEST_EMAIL, TEST_PASSWORD)

    # Next page
    expect(login_page.features_items_header).to_be_visible()
'''

# Page is on URL = 'http://automationexercise.com'

def test_purchase_one(page: Page):
    # home_page = HomePage(page)  
    page.goto('http://automationexercise.com')
    home_page_text = page.get_by_text("Features Items")
    expect(home_page_text).to_be_visible()

    # Product Link
    product_link = page.locator("[href='/products']")
    product_link.click()
    
    # need to close add
    popup = page.locator("iframe[name=\"aswift_3\"]").content_frame.get_by_role("button", name="Close ad")
    if popup.is_visible():
        popup.click()

    # Add to cart on Product Page
    page.locator("div.col-sm-4").nth(1).hover()
    add_to_cart = page.get_by_text("Add to cart").nth(1)
    # add_to_cart = page.locator("a.btn btn-default add-to-cart").nth(1)
    add_to_cart.click()

    # Click Cart Modal and go to cart.
    cart_modal = page.locator("#cartModal")
    view_cart_link = page.get_by_role("link", name="View Cart")
    view_cart_link.click()

    # Proceed to checkout  page changed
    proceed_to_checkout = page.get_by_text("Proceed To Checkout")
    proceed_to_checkout.click()

    # To Login Page
    login_link = page.get_by_role("link", name="Register / Login")
    login_link.click()

    # Login Page
    # page.goto("https://automationexercise.com/login#google_vignette")
    popup = page.locator("iframe[name=\"aswift_2\"]").content_frame.get_by_role("button", name="Close ad")
    if popup.is_visible():
        popup.click()
    
    email_field = page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")
    email_field.fill(TEST_EMAIL)
    password_field = page.get_by_role("textbox", name="Password")
    password_field.fill(TEST_PASSWORD)
    login_button = page.get_by_role("button", name="Login")
    login_button.click()

    # Go to Cart Page 
    cart_link = page.get_by_role("link", name=" Cart")
    # cart_link = page.locator("//a[href='/view_cart']")
    cart_link.click()

    # Proceed to checkout
    proceed_to_checkout_btn = page.get_by_text("Proceed To Checkout")
    proceed_to_checkout_btn.click()

    # On page: https://automationexercise.com/checkout
    place_order_button = page.get_by_text("Place Order")
    place_order_button.click()

    # On page: https://automationexercise.com/payment
    name_on_card_field = page.locator("input[name='name_on_card']")
    card_number_field = page.locator("input[name='card_number']")
    cvc_field = page.get_by_placeholder("ex. 311")
    expiration_month_field = page.get_by_placeholder("MM")
    expiration_year_field = page.get_by_placeholder("YYYY")

    name_on_card_field.fill("John Doe")
    card_number_field.fill(CARD_NUMBER)
    cvc_field.fill(CVC)
    expiration_month_field.fill(EXPIRATION_MONTH)
    expiration_year_field.fill(EXPIRATION_YEAR)

    pay_and_confirm_order_button = page.get_by_text("Pay and Confirm Order")
    pay_and_confirm_order_button.click()

    # On page: https://automationexercise.com/order_placed
    order_placed_text = page.get_by_text("Order Placed!")
    expect(order_placed_text).to_be_visible()

    continue_button = page.get_by_role("link", name="Continue")
    continue_button.click()

    # page.locator("iframe[name=\"aswift_2\"]").content_frame.get_by_role("button", name="Close ad")
