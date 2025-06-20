import allure
from playwright.sync_api import expect



class BasePage:
    __BASE_URL = "https://www.saucedemo.com"

    def __init__(self, page):
        self.page = page
        self._endpoint = ""
    @allure.step("Получаем полный BASE_URL/endpoint")
    def _get_full_url(self):
        return f"{self.__BASE_URL}/{self._endpoint}"

    @allure.step("URL")
    def navigate_to(self):
        full_url = self._get_full_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state("load")
        expect(self.page).to_have_url(full_url)

    @allure.step("Ждем селектор и кликаем")
    def wait_for_selector_and_click(self, selector):
        self.page.wait_for_selector(selector)
        self.page.is_visible(selector)
        self.page.is_enabled(selector)
        self.page.click(selector)

    @allure.step("Ждем селектор и вставляем значением")
    def wait_for_selector_and_fill(self, selector, value):
        self.page.wait_for_selector(selector)
        self.page.fill(selector, value)

    @allure.step("Ждем селектор и печатаем значением")
    def wait_for_selector_and_type(self, selector, text, delay):
        self.page.wait_for_selector(selector)
        self.page.type(selector, text, delay=delay)

    @allure.step("Проверка что селектор видимый")
    def assert_element_is_visible(self, selector):
        expect(self.page.locator(selector)).to_be_visible()

    @allure.step("Проверка: текст присутствует на странице в body")
    def assert_text_present_on_page(self, text):
        expect(self.page.locator("body")).to_contain_text(text)

    @allure.step("Проверка: текст присутствует  в элемент с селектором")
    def assert_text_in_element(self, selector, text):
        expect(self.page.locator(selector)).to_have_text(text)

    @allure.step("Найденный элемент по указанному селектору, содержит определенное значение")
    def assert_input_value(self, selector, expected_value):
        expect(self.page.locator(selector)).to_have_value(expected_value)# Commit 7
# Commit 12
# Commit 21
# Commit 30
# Commit 31
# Commit 49
# Commit 61
# Commit 62
# Commit 70
# Commit 16
# Commit 71
# Commit 93
# Commit 102
