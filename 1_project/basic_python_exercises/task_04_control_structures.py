
# Валидация пользовательского ввода и вывод оценки результата
def validate_test_input(user_input: str) -> str:
    if user_input.isdigit():
        count = int(user_input)
        if count > 0:
            return "Отличная работа!" if count > 10 else "Попробуйте улучшить результат."
    return "Некорректный ввод. Введите положительное число."

# Фильтрация багов по приоритету
def filter_by_priority(bugs: list[str], priority: str) -> list[str]:
    return [bug for bug in bugs if priority in bug]

# Увеличение счётчика багов для конкретного тестировщика
def update_bug_counter(testers: dict, name: str) -> dict:
    testers[name] = testers.get(name, 0) + 1
    return testers

# Подсчёт количества багов по приоритетам High и Low
def count_bugs_by_priority(bugs: list[str]) -> tuple[int, int]:
    high = sum(1 for bug in bugs if "High" in bug)
    low = sum(1 for bug in bugs if "Low" in bug)
    return high, low