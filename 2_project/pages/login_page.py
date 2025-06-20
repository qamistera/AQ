# === Класс LoginPage (POM) ===
import allure
from faker import Faker
from pages.base_page import BasePage
from utils.helpers import CLICKUP_EMAIL, CLICKUP_PASSWORD


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = "login"

    EMAIL_SELECTOR = "#login-email-input"
    PASSWORD_SELECTOR = "#login-password-input"
    LOGIN_BUTTON_SELECTOR = "button[type='submit']:has-text('Log in')"

    @allure.step("Авторизуемся с валидными данными")
    def login(self):
        self.open()
        self.wait_for_selector_and_type(self.EMAIL_SELECTOR, CLICKUP_EMAIL, 100)
        self.wait_for_selector_and_type(self.PASSWORD_SELECTOR, CLICKUP_PASSWORD, 100)
        self.wait_for_selector_and_click(self.LOGIN_BUTTON_SELECTOR)
        self.page.wait_for_url(lambda url: "/login" not in url, timeout=15000)
        self.page.wait_for_load_state("load", timeout=15000)
        self.assert_text_present_on_page("Workspace")

    @allure.step("Пробуем авторизоваться с невалидными данными")
    def login_with_invalid_user(self):
        fake = Faker()
        email = fake.email()
        password = fake.password()

        self.open()
        self.wait_for_selector_and_type(self.EMAIL_SELECTOR, email, 100)
        self.wait_for_selector_and_type(self.PASSWORD_SELECTOR, password, 100)
        self.wait_for_selector_and_click(self.LOGIN_BUTTON_SELECTOR)
        self.assert_text_present_on_page("No account was found for this email address")
# Commit 39
# Commit 56
# Commit 74
# Commit 77
# Commit 4
# Commit 20
# Commit 31
# Commit 36
# Commit 42
# Commit 66
# Commit 86
