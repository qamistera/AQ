
import allure
from pages.base_page import BasePage


class LogoutPage(BasePage):
    BURGER_MENU_SELECTOR = '[data-test="user-main-settings-menu__dropdown-toggle"]'
    LOGOUT_BUTTON_SELECTOR = '[data-test="dropdown-list-item__Log out"]'

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.wait_for_selector_and_click(self.BURGER_MENU_SELECTOR)
        self.wait_for_selector_and_click(self.LOGOUT_BUTTON_SELECTOR)
        self.page.wait_for_url(lambda url: "/login" in url, timeout=10000)  # ⬅️ проверка возврата к логину
        self.assert_element_is_visible("button:has-text('Log In')")
        self.assert_text_present_on_page("Welcome back")
