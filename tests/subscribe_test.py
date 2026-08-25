import pytest
from playwright.sync_api import Page, expect

# from pages.home_page import HomePage
URL='http://automationexercise.com'

def test_subscription(page: Page):
    page.goto(URL)
    home_page_text = page.locator("h2").filter(has_text="Features Items")
    expect(home_page_text).to_be_visible()
        
    subscription_email_field = page.locator("input#susbscribe_email")
    subscription_email_field.scroll_into_view_if_needed()

    subscription_title = page.locator("h2").filter(has_text="Subscription")
    expect(subscription_title).to_be_visible()

    arrow_icon = page.locator("//button[@id='subscribe']")
    subscription_email_field.fill("pic@example.com")
    arrow_icon.click()

    sucess_message = page.locator("//div[contains(@class,'alert-success alert')]")
    expect(sucess_message).to_be_visible()
