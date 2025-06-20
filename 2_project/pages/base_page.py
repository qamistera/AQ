
import allure
from playwright.sync_api import expect

class BasePage:
    __BASE_URL = "https://app.clickup.com"

    def __init__(self, page):
        self.page = page
        self._endpoint = ""

    @allure.step("Формируем полный URL из BASE и endpoint")
    def _get_full_url(self):
        """Возвращает полный URL: https://... + endpoint"""
        return f"{self.__BASE_URL}/{self._endpoint}"

    @allure.step("Переход по адресу BASE_URL + endpoint")
    def open(self):
        """Переход на полный URL: BASE + endpoint"""
        full_url =self._get_full_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state("load")
        expect(self.page).to_have_url(full_url)

    # @allure.step("Ждем селектор и кликаем")
    # def wait_for_selector_and_click(self, selector):
    #     self.page.wait_for_selector(selector)
    #     self.page.is_visible(selector)
    #     self.page.is_enabled(selector)
    #     self.page.click(selector)

    @allure.step("Ждём, пока элемент станет видимым и кликаем принудительно (force=True)")
    def wait_for_selector_and_click(self, selector):
        locator = self.page.locator(selector)  # создаём локатор
        locator.wait_for(state="visible", timeout=10000)  # ждём, пока появится
        locator.click(force=True)  # ⬅️ принудительный клик, даже если aria-disabled="true"



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
        expect(self.page.locator(selector)).to_have_value(expected_value)



# Commit 4
# Commit 5
# Commit 55
# Commit 71
# Commit 72
# Commit 78
# Commit 1
# Commit 43
# Commit 55
# Commit 58
# Commit 81
# Commit 98
