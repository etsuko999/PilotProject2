import pytest
from playwright.sync_api import Page, expect


URL = "https://automationexercise.com/"

def test_basic_search(page: Page):
        page.goto(URL)
        home_page_text = page.get_by_text("Features Items")
        expect(home_page_text).to_be_visible()
        
        product_link = page.locator("[href='/products']")
        product_link.click()
        
        # Page changes
        product_page_text = page.get_by_text("All Products")
        expect(product_page_text).to_be_visible()

        search_box = page.get_by_placeholder("Search Product")
        search_box.fill("dress")      

        submit_button = page.locator("button#submit_search")
        submit_button.click()

        # URL change https://automationexercise.com/products?search=dress
        searched_text = page.get_by_text("Searched Products")
        expect(searched_text).to_be_visible()

        screen_item = page.locator("a").filter(has_text=" View Product").first
        expect(screen_item).to_be_visible()
        page.close()