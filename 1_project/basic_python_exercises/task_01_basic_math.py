# Перевод граммов в килограммы (целочисленно)
def grams_to_kilograms(grams: int) -> int:
    return grams // 1000

# Проверка: является ли число положительным и чётным
def is_positive_even(number: int) -> str:
    if number > 0 and number % 2 == 0:
        return f"Число {number} является положительным и чётным."
    return f"Число {number} не подходит под условия."

# Проверка: входит ли число в диапазон от 0 до 100
def is_in_range(number: int) -> str:
    if 0 <= number <= 100:
        return f"Число {number} находится в пределах диапазона от 0 до 100."
    return f"Число {number} выходит за пределы диапазона от 0 до 100."
