import pytest
from playwright.sync_api import Page, expect

URL='http://automationexercise.com'

def test_cart_subscription(page: Page):
    page.goto(URL)
    home_page_text = page.locator("h2").filter(has_text="Features Items")
    expect(home_page_text).to_be_visible()
    # cart_link = page.locator("[href='/view_cart']")
    cart_link = page.get_by_role("link", name=" Cart")
    cart_link.click()
    shopping_cart_text = page.get_by_text("Shopping Cart")
    expect(shopping_cart_text).to_be_visible()

    footer = page.locator("div.footer-widget")
    footer.scroll_into_view_if_needed()

    subscription_title = page.locator("h2").filter(has_text="Subscription")
    expect(subscription_title).to_be_visible()

    email_address_field = page.get_by_placeholder("Your email address")
    email_address_field.fill("pic@exmaple.com")
    submit_button = page.locator("button#subscribe")
    submit_button.click()

    sucess_message = page.locator("//div[contains(@class,'alert-success alert')]")
    expect(sucess_message).to_be_visible()