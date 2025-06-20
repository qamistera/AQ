import allure
from pages.login_page import LoginPage
from pages.board_page import BoardPage
from pages.logout_page import LogoutPage
from api_clients.task_api import TaskAPI



@allure.feature("UI: Создание задачи")
@allure.title("Пользователь логинится → создаёт задачу → проверяет её наличие → выходит")
@allure.description("""
Проверка создания задачи через UI:
1. Входим в ClickUp
2. Переходим на доску
3. Создаём задачу с автогенерацией имени и описания
4. Проверяем, что задача появилась
5. Удаляем задачу через API
6. Выходим из аккаунта
""")
def test_create_task_ui(page):
    # === Setup ===
    with allure.step("Создаём страницы POM"):
        login_page = LoginPage(page)
        board_page = BoardPage(page)
        logout_page = LogoutPage(page)
        task_api = TaskAPI()

    # === Test Body ===
    with allure.step("Логинимся в ClickUp"):
        login_page.login()

    with allure.step("Создаём новую задачу с фейковыми данными"):
        task_name, task_id = board_page.create_fake_task()

    with allure.step("Проверяем, что задача появилась"):
        board_page.assert_task_created(task_name)

    # === Tear Down ===
    with allure.step("Выходим и закрываем браузер"):
        task_api.delete_task(task_id)
        logout_page.logout()

@allure.feature("UI: Удаление задачи")
@allure.title("Создаём задачу через API → удаляем через UI → проверяем удаление → logout")
@allure.description("""
Проверка удаления задачи через UI:
1. Создаём задачу через API
2. Входим в ClickUp
3. Переходим на доску
4. Удаляем задачу через интерфейс
5. Проверяем, что задача исчезла
6. Выходим из аккаунта
""")
def test_delete_task_ui(page, api_created_task):
    task_name, task_id = api_created_task

    with allure.step("Создаём POM страницы"):
        login_page = LoginPage(page)
        board_page = BoardPage(page)
        logout_page = LogoutPage(page)

    with allure.step("Логинимся в ClickUp"):
        login_page.login()

    with allure.step("Удаляем задачу через UI"):
        board_page.delete_task_ui(task_name)

    with allure.step("Выходим из аккаунта"):
        logout_page.logout()# Commit 6
# Commit 19
# Commit 26
# Commit 3
# Commit 8
# Commit 34
# Commit 38
# Commit 45
# Commit 70
# Commit 75
# Commit 77
# Commit 78
# Commit 96
