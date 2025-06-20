import allure


from pages.logout_page import LogoutPage
from pages.login_page import LoginPage


@allure.feature("UI: Авторизация")
@allure.title("Тест авторизации: позитивный и негативный логин в одном потоке")
@allure.description("Сначала входим с валидными данными, затем пробуем невалидные и проверяем сообщение об ошибке")
def test_authorization_flow(page):
    # === Setup ===
    with allure.step("Создаём объект страницы логина"):
        login_page = LoginPage(page)
        logout_page = LogoutPage(page)

    # === Test Body ===
    with allure.step("Позитивный логин"):
        login_page.login()

    with allure.step("Выход"):
        logout_page.logout()

    with allure.step("Негативный логин"):
        login_page.login_with_invalid_user()

    # === Tear Down ===
    with allure.step("Закрываем страницу"):
        page.close()
# Commit 18
# Commit 33
# Commit 68
# Commit 7
# Commit 18
# Commit 37
# Commit 44
# Commit 49
# Commit 61
# Commit 69
# Commit 72
# Commit 76
# Commit 79
# Commit 82
# Commit 99
# Commit 100
