import pytest
import allure
from api_clients.task_api import TaskAPI
from utils.helpers import get_env_variable
from faker import Faker
from playwright.sync_api import sync_playwright

LIST_ID = get_env_variable("CLICKUP_LIST_ID")

@pytest.fixture(scope="session")
def task_api():
    return TaskAPI()

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page= context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()

# Фикстура с шагами — создание и удаление задачи
@pytest.fixture
def create_and_delete_task(task_api):
    with allure.step("Создаём задачу через API"):
        create_resp = api.create_task(LIST_ID, name="Test Task", status="to do", description="test task")
        assert create_resp.status_code ==200, f"ОШибка создания задачи: {create_resp.text}"
        task_id= create_resp.json()["id"]

    yield task_id # передаем task_id в тест

    # Удаляем после теста
    with allure.step("Удаляем задачу после теста"):
        delete_resp=task_api.delete_task(task_id)
        assert delete_resp.status_code in (200, 204), f"Ошибка удаления {delete_resp.text}"

@pytest.fixture
def list_id():
    return get_env_variable("CLICKUP_LIST_ID")

@pytest.fixture
def api_created_task(task_api):
    """
    Создаёт задачу через API и возвращает (task_name, task_id).
    Удаление не требуется — оно будет через UI.
    """
    faker=Faker()

    task_name=faker.sentence(nb_words=4)
    description=faker.text(max_nb_chars=100)
    response= task_api.create_task(LIST_ID, name=task_name, status="to do", description=description)
    # Проверка, что задача создана
    assert response.status_code == 200 or response.status_code == 201, \
        f"Ошибка создания задачи через API: {response.status_code}, {response.text}"

    task_id = response.json()["id"]
    return task_name, task_id


