import allure

from Playwright.page.base_page import BasePage


class CheckoutPage(BasePage):

    CHECKOUT_BUTTON_SELECTOR = '[id="checkout"]'
    FIRST_NAME_SELECTOR = '#first-name'
    LAST_NAME_SELECTOR = '#last-name'
    POSTAL_CODE_SELECTOR = '#postal-code' #'input[name="postalCode"]'


    def __init__(self, page):
        super(). __init__(page)
        self._endpoint = "checkout-step-one.html"
    @allure.title("Переходим к оформлению заказа")
    def start_checkout(self):
        self.wait_for_selector_and_click(self.CHECKOUT_BUTTON_SELECTOR)
        self.assert_element_is_visible(self.FIRST_NAME_SELECTOR)
    @allure.title("Заполняем форму оформления: name, last name, zip code")
    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.wait_for_selector_and_type(self.FIRST_NAME_SELECTOR, first_name, 100)
        self.wait_for_selector_and_type(self.LAST_NAME_SELECTOR, last_name, 100)
        self.wait_for_selector_and_type(self.POSTAL_CODE_SELECTOR, postal_code, 100)
        self.assert_input_value(self.POSTAL_CODE_SELECTOR, postal_code)

        