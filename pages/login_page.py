from playwright.sync_api import Page


class LoginPage:
    URL = "https://automationexercise.com/login"

    def __init__(self, page: Page):
        self.page = page

        self.login_page_popup = page.locator("iframe[name=\"aswift_2\"]").content_frame.get_by_role("button", name="Close ad")
    
        self.email_field = page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")
        self.password_field = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.get_by_text("Your email or password is incorrect!")
        self.features_items_header = page.get_by_role("heading", name="Features Items")

    def goto(self):
        self.page.goto(self.URL)
        self.page.locator("body").click()

    def close_login_page_popup(self):
        if self.login_page_popup.is_visible():
            self.login_page_popup.click()

    def login(self, email: str, password: str):
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.login_button.click()

    def close(self):
        self.page.close()
