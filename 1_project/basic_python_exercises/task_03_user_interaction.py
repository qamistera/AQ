# Приветствие пользователя по имени
def greet_user(name: str) -> str:
    return f"Привет, {name}! Добро пожаловать в мир Python."

# Проверка ответа пользователя о переменных
def ask_about_variable(answer: str) -> str:
    if "переменная" in answer.lower():
        return "Ты молодец, всё верно!"
    elif "не помню" in answer.lower():
        return "Иди учись."
    return "Плохо"

# Подсчёт количества тестов в неделю и оценка результата
def weekly_test_count(day_count: int) -> tuple[int, str]:
    total = day_count * 7
    message = "Отличная работа" if day_count > 10 else "Попробуй улучшить результат"
    return total, message

# Обработка списка багов: добавление, удаление и сортировка
def bug_sorting(bugs: list[str]) -> list[str]:
    bugs.append("Ошибка 6 - Low")
    if "Ошибка api_testing_items_crud — High" in bugs:
        bugs.remove("Ошибка api_testing_items_crud — High")
    return sorted(bugs)
