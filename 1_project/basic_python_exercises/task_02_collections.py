# Работа со списками: добавление и удаление элементов
def list_operations():
    numbers = [1, 2, 3, 4]  # список чисел
    cities = ["Москва", "Париж"]  # список городов
    return numbers, cities

# Работа со словарями: удаление ключа
def dict_operations():
    student = {"name": "Ivan", "grade": "B"}  # словарь студента
    del student["grade"]  # удаление оценки
    return student

# Редактирование вложенного словаря
def nested_dict_edit():
    student = {"name": "Ivan", "address": {"city": "Moscow", "street": "Lenina"}}
    student["address"]["city"] = "Saint Petersburg"
    return student

# Проверка наличия значения в кортеже
def tuple_check(colors: tuple, value: str) -> bool:
    return value in colors
