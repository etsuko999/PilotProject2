import pytest
from playwright.sync_api import Page, expect


class ProductsPage:
	"""Landing page at /."""

	URL = "https://automationexercise.com/products"
	

	def __init__(self, page: Page):
		self.page = page
		self.item_to_search = "dress"
		self.popup_btn_one = page.locator("iframe[name=\"aswift_3\"]").content_frame.get_by_role("button", name="Close ad")

   
		self.product_page_text = page.get_by_text("All Products")
		self.search_box = page.get_by_placeholder("Search Product")
		self.first_product = page.locator("div.col-sm-4").nth(1)
		self.first_add_to_cart_btn = page.get_by_text("Add to cart").nth(1)
		# Cart Modal
		self.cart_modal = page.locator("#cartModal")
		self.view_cart_link_on_modal = page.get_by_role("link", name="View Cart")

		self.search_button = page.locator("button#submit_search")
		self.searched_page_text = page.get_by_text("Searched Products")
		self.screen_item = page.locator("a").filter(has_text=" View Product").first
    
	def close_popup_one(self):
		if self.popup_btn_one.is_visible():
			self.popup_btn_one.click()
	
	def is_product_page_text_visible(self):
		expect(self.product_page_text).to_be_visible()
		return True

	def purchase_first_product(self):
		self.first_product.hover()
		self.first_add_to_cart_btn.click()

	def click_view_cart_from_cart_modal(self):
		expect(self.cart_modal).to_be_visible()
		self.view_cart_link_on_modal.click()

	def search_products(self):
		self.search_box.fill(self.item_to_search)
		self.search_button.click()

	def confirm_search_result_page_title(self):
		expect(self.searched_page_text).to_be_visible()
		return True

	def confirm_search_result_screen_item(self):
		expect(self.screen_item).to_be_visible()
		return True

	def close(self):
		self.page.close()        