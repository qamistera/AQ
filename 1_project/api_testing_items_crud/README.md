# API-тестирование CRUD операций (items)

## Описание
Этот проект реализует полное покрытие API CRUD-тестов для сущности `items` через ручки:
- POST /items/
- GET /items/
- PUT /items/{id}
- DELETE /items/{id}

Сценарии реализованы с помощью:
- `pytest` + `requests`
- `Faker` для генерации тестовых данных
- `Allure` (опционально для отчётов)

## Структура проекта
```
hw4_items_api/
├── conftest.py        # Фикстуры: авторизация, генерация данных, pre-create items
├── constant.py        # Константы: URL'ы, headers, auth data
├── items.py           # Ручной запуск генерации большого количества items
├── test_items.py      # Основной набор тестов (CRUD, пагинация, валидация)
├── example.http       # Тестовые HTTP-запросы (для ручного тестирования в IDE)
```

## Покрытие тестами
-  POST /items/ — создание item (с проверкой ID, title)
-  GET /items/ — получение списка + валидация структуры ответа
-  GET с skip/limit — пагинация
-  PUT /items/{id} — обновление title/description
-  DELETE /items/{id} — удаление item и проверка статуса

##  Запуск тестов
```bash
pytest -v
pytest --alluredir=allure-results && allure serve allure-results
```

##  Примечания
- Все тесты используют `auth_session` с Bearer-токеном
- Данные автоматически создаются и удаляются через фикстуры
- Используется `Faker` для разнообразия данных
- Пример токена и endpoint'ов хранится в `constant.py`

---

Демонстрация навыков продвинутого API-тестирования, включая сессию авторизации, генерацию данных, пагинацию и удаление.
