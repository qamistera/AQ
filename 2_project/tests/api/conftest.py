import pytest
import allure
from api_clients.task_api import TaskAPI
from utils.helpers import get_env_variable

LIST_ID = get_env_variable("CLICKUP_LIST_ID")

# Фикстура с шагами — создание и удаление задачи
@pytest.fixture
def create_and_delete_task():
    api = TaskAPI()
    with allure.step("Создаём задачу через API"):
        create_resp = api.create_task(LIST_ID, name="Test Task", status="to do")
        assert create_resp.status_code ==200, f"ОШибка создания задачи: {create_resp.text}"
        task_id= create_resp.json()["id"]

    yield task_id # передаем task_id в тест

    # Удаляем после теста
    with allure.step("Удаляем задачу после теста"):
        delete_resp=api.delete_task(task_id)
        assert delete_resp.status_code in (200, 204), f"Ошибка удаления {delete_resp.text}"

@pytest.fixture
def list_id():
    return get_env_variable("CLICKUP_LIST_ID")


