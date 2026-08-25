import pytest
from playwright.sync_api import Page, expect

from pages.products_page import ProductsPage
from pages.home_page import HomePage

def test_basic_search(page: Page):
        home_page = HomePage(page)
        home_page.goto()
        
        # if home_page.is_home_page_text_visible():
        home_page.navigate_to_products_page()
        # else:
        #     pytest.fail("Home page text not visible, cannot navigate to products page.")
        
        products_page = ProductsPage(page)
        if products_page.is_product_page_text_visible():
            products_page.search_products()
            if products_page.confirm_search_result_page_title():
                assert products_page.confirm_search_result_screen_item()
        else:
            pytest.fail("Product page text not visible, cannot search products.")
        
        
        products_page.close()
        home_page.close()