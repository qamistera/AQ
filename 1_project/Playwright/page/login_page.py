import allure
from Playwright.page.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ""

    USERNAME_SELECTOR = "#user-name"
    PASSWORD_SELECTOR = "#password"
    LOGIN_BUTTON_SELECTOR = ".submit-button"

    @allure.title("Авторизация: логинимся")
    def login(self, username, password):
        self.navigate_to()
        self.wait_for_selector_and_fill(self.USERNAME_SELECTOR, username)
        self.wait_for_selector_and_fill(self.PASSWORD_SELECTOR, password)
        self.wait_for_selector_and_click(self.LOGIN_BUTTON_SELECTOR)
        self.assert_text_present_on_page("Products")
# Commit 1
# Commit 60
# Commit 80
# Commit 10
# Commit 12
# Commit 15
# Commit 21
# Commit 59
# Commit 94
