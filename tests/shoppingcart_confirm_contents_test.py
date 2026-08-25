import pytest
from playwright.sync_api import Page, expect

URL = 'http://automationexercise.com'

name_and_price = {}
PRODUCT_ID_SUFFIX = "product-"

def get_each_product_details(page: Page):
    product_name = page.locator("//div[contains(@class,'product-information')]/h2").inner_text()
    print("\nprinting product_name: ",  product_name)
    
    product_price = page.locator("//div[contains(@class,'product-information')]/span/span").filter(has_text="Rs. ").inner_text()
    print("printing detail_block: ", product_price)

    product_id = page.locator("//div[contains(@class,'product-information')]/span/input[@id='product_id']").get_attribute('value')
    product_id = PRODUCT_ID_SUFFIX + product_id

    dict1 = {}
    item_list=[product_name, product_price]
    dict1[product_id] = item_list

    return dict1

def add_to_cart(page: Page):
    add_to_cart_button = page.get_by_role("button", name="Add to cart")
    expect(add_to_cart_button).to_be_visible()
    add_to_cart_button.click()




def test_cart_contents(page: Page):    
    page.goto(URL)
    home_page_text = page.get_by_text("Features Items")
    expect(home_page_text).to_be_visible()

    product_link = page.locator("[href='/products']")
    product_link.click()
    # need to close add
    popup = page.locator("iframe[name=\"aswift_3\"]").content_frame.get_by_role("button", name="Close ad")
    if popup.is_visible():
        popup.click()
    screen_item = page.locator("a").filter(has_text=" View Product").nth(0)
    screen_item.click()

    # Getting details on https://automationexercise.com/product_details/x
    name_and_price.update(get_each_product_details(page))
    add_to_cart(page)

    ######
    # Try to go to choose second product.
    ######
    continue_shopping_btn = page.get_by_role("button", name="Continue Shopping")
    continue_shopping_btn.click()
    product_link.click()

	# it goes to product page directly.
    if popup.is_visible():
        popup.click()
    screen_item = page.locator("a").filter(has_text=" View Product").nth(3)
    screen_item.click()

    # getting details on https://automationexercise.com/product_details/X
    name_and_price.update(get_each_product_details(page))
    add_to_cart(page)

    view_cart_link = page.get_by_role("link", name="View Cart")
    view_cart_link.click()

    for product_id, item_detail in name_and_price.items():
        item_name = item_detail[0]
        item_price = item_detail[1]
        # print(f"key: {product_id}, name: {item_name}, price: {item_price}")
        row_identifier = "tr#" + product_id
        row = page.locator(row_identifier)
        name_in_table = row.locator("//td[@class='cart_description']/h4/a").inner_text()
        print("loop: item in cart: ", name_in_table)
        assert item_name == name_in_table

        price_in_table = row.locator("//td[@class='cart_price']/p").inner_text()
        print("printing price in cart: ", price_in_table)
        assert item_price == price_in_table

        quantity_in_table = row.locator("//td[@class='cart_quantity']/button").inner_text()
        print("printing quantity in cart: ", quantity_in_table)

        total_price = row.locator("//td[@class='cart_total']/p").inner_text()
        print("printing total price in cart: ", total_price)


    page.close()
