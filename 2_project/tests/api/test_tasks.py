

import allure
import pytest
from api_clients.task_api import TaskAPI



# Группируем тесты — видно в Allure как блок: ClickUp API
@allure.feature("Clickup API: Tasks")
class TestTasks:

    @classmethod
    def setup_class(cls):
        cls.api =TaskAPI()

    @allure.description("Создание задачи через API и проверяет, что она существует и отображается")
    def test_create_task(self, create_and_delete_task):
        task_id= create_and_delete_task

        with allure.step("Получаем задачу по ID"):
            get_resp= self.api.get_task(task_id)
            assert get_resp.status_code ==200, f"Задача не найденв {get_resp.text}"
            task_data= get_resp.json()

        with allure.step("Проверяем название и статус задачи"):
            assert task_data["name"]== "Test Task", "Название задачи не совпадает"

        with allure.step("Проверяем статус задачи"):
            assert task_data["status"]["status"] =="to do", "Неверный статус"

    @allure.description("Проверка создания задачи без имени — должен вернуть ошибку")
    def test_create_task_without_name(self, create_and_delete_task, list_id):
        with allure.step("Создаем задачу без имени"):
            response= self.api.create_task(list_id, name="", status="to do")
            assert response.status_code in (400, 422), f"Ожидали ошибку, получили {response.status_code}: {response.text}"

    @allure.description("Создание задачи с несуществующим list_id — должен вернуть ошибку")
    def test_create_task_invalid_list(self):
        with allure.step("Пробуем создать задачу с неверным list_id"):
            fake_list_id= "123456"
            response= self.api.create_task(fake_list_id, name="Fake List")
            assert response.status_code in (401, 422), f"Ожидали ошибку, получили {response.status_code}: {response.text}"

    @allure.description("Получение задачи по несуществующему ID")
    def test_create_task_invalid_id(self):
        with allure.step("Пробуем получить задачу с фейковым ID"):
            fake_task_id="ads12345"
            response= self.api.get_task(fake_task_id)
            assert response.status_code== 401, f"Ожидали ошибку получаем задачу с фейковым ID {response.status_code}"

    @allure.description("Удаление задачи с несуществующим ID ")
    def test_delete_task_invalid_id(self):
        with allure.step("Пробуем удалить несуществующую задачу"):
            fake_task_id="xyz987notreal"
            response= self.api.delete_task(fake_task_id)
            assert response.status_code == 401, f"Ожидали ошибку удаления задачи с фейковым ID"

    @allure.description("Обновление задачи с несуществующим ID")
    def test_update_task_invalid_id(self):
        with allure.step("Пробуем обновить задачу с фейковым ID"):
            fake_task_id="nope-task-000"
            data = {"name": "Should not work"}
            response= self.api.update_task(fake_task_id, data)
            assert response is not None, "Ответ пустой, запрос не удался"
            assert response.status_code in (401, 403, 404), f"Ожидали ошибку, получили {response.status_code}: {response.text}"


