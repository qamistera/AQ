from fileinput import close

import allure


from Playwright.page.checkout_page import CheckoutPage
from Playwright.page.inventory_page import InventoryPage
from Playwright.page.login_page import LoginPage
from Playwright.page.logout_page import LogoutPage


@allure.feature("Оформление заказа")
@allure.title("Тест оформления заказа: login → корзина → оформление")
@allure.description("""
Полный тест проверки функционала оформления заказа через UI с использованием POM.
""")
def test_checkout_order(browser):
    # === Setup ===
    with allure.step ("Setup: Открываем браузер и создаем экземпляры страниц"):
        page=browser.new_page()
        login_page= LoginPage(page)
        inventory_page= InventoryPage(page)
        checkout_page= CheckoutPage(page)
        logout_page= LogoutPage(page)

    # === Test Body ===
        login_page.login('standard_user', 'secret_sauce')
        inventory_page.add_first_item_to_cart()
        checkout_page.start_checkout()
        checkout_page.fill_checkout_form('Don', 'Carlion', '223304')
        logout_page.logout()

        # === Tear Down ===
        with allure.step("TearDown: Закрываем браузер"):
            page.close()# Commit 13
# Commit 32
# Commit 66
# Commit 69
# Commit 81
# Commit 6
# Commit 41
# Commit 54
# Commit 63
# Commit 68
