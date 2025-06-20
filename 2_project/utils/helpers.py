import os # Импортируем стандартный модуль os для работы с переменными окружения
from dotenv import load_dotenv #  Импортируем load_dotenv из пакета dotenv для загрузки .env файла

load_dotenv()  # Загружаем содержимое файла .env в переменные окружения

# Функция для безопасного получения переменной окружения по имени
def get_env_variable(name):
    value = os.getenv(name) # получаем значение из переменной окружения
    if not value:
        # если переменная отсутствует — выбрасываем исключение с пояснением
        raise ValueError(f"Переменная окружения '{name}' не задана")
    return value

# Здесь получаем конкретные переменные окружения и сохраняем в переменные Python
CLICKUP_API_KEY = get_env_variable('CLICKUP_API_KEY')
CLICKUP_EMAIL = get_env_variable('CLICKUP_EMAIL')
CLICKUP_PASSWORD = get_env_variable('CLICKUP_PASSWORD')# Commit 15
# Commit 29
# Commit 42
# Commit 48
# Commit 52
# Commit 57
# Commit 64
# Commit 65
# Commit 67
# Commit 79
# Commit 5
# Commit 22
# Commit 29
# Commit 46
# Commit 84
# Commit 97
