import allure

from Playwright.page.base_page import BasePage


class LogoutPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ""

    BURGER_MENU_SELECTOR = "#react-burger-menu-btn"
    LOGOUT_BUTTON_SELECTOR = "#logout_sidebar_link"
    @allure.step("Выход после завершения заказа")
    def logout(self):
        self.wait_for_selector_and_click(self.BURGER_MENU_SELECTOR)
        self.wait_for_selector_and_click(self.LOGOUT_BUTTON_SELECTOR)
