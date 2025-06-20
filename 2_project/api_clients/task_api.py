import requests
from utils.helpers import CLICKUP_API_KEY
from faker import Faker
from utils.helpers import get_env_variable

class TaskAPI:
    def __init__(self):
        # создаём сессию, в которую заранее добавляем заголовки
        self.session = requests.Session() # Создаём сессию один раз при инициализации
        # ️ Добавляем заголовки авторизации ко всем запросам сразу
        self.session.headers.update({
            "Authorization": CLICKUP_API_KEY,
            "Content-Type": "application/json"
        })

    def create_task(self, list_id, name, status="to do", description: str = ""):
        """
        Создаёт задачу с заданным названием и статусом в указанном списке
        """
        url = f"https://api.clickup.com/api/v2/list/{list_id}/task"
        payload = {
            "name": name,
            "status": status,
            "description": description
        }
        return self.session.post(url, json=payload)

    def get_task(self, task_id):
        """
        Получает задачу по её ID
        """
        url = f"https://api.clickup.com/api/v2/task/{task_id}"
        return self.session.get(url)

    def update_task(self, task_id, data: dict):
        """
        Обновляет задачу — принимает словарь с данными
        """
        url = f"https://api.clickup.com/api/v2/task/{task_id}"
        return self.session.put(url, json=data)

    def delete_task(self, task_id):
        """
            Удаляем задачу по ID
        """
        url = f"https://api.clickup.com/api/v2/task/{task_id}"
        return self.session.delete(url)


    def create_fake_task_api(self):
        faker = Faker()
        task_name = faker.sentence(nb_words=4)
        description = faker.text(max_nb_chars=100)

        response = self.create_task(list_id=..., name=task_name, description=description)
        assert response.status_code == 200, f"Ошибка создания: {response.text}"
        task_id = response.json()["id"]

        return task_name, task_id
# Commit 17
# Commit 54
# Commit 58
# Commit 63
# Commit 73
# Commit 11
# Commit 13
# Commit 47
# Commit 62
# Commit 65
# Commit 80
# Commit 87
# Commit 101
