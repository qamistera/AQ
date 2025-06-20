def geet_user():
    name=input("Введите ваше имя: ")
    print(f"Привет,{name}! Добро пожаловать в мир Python!")

# geet_user()

def calculate_sum():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    summa = a + b
    print(f"Сумма чисел: ", summa)

# calculate_sum()

def calculate_sum(a, b):
    summa = a + b
    print(f"Сумма чисел: {summa}")

# x = int(input("Введите первое число: "))
# y = int(input("Введите второе число: "))

# calculate_sum(x, y)



def age(ages):

    year_now = 2025
    ages_calc = year_now-ages
    print(f'Ваш возраст: {ages_calc}')
    if ages_calc < 18:
        print("Вы еще молоды, учеба - ваш путь!")
    elif 18 <= ages_calc < 65:
        print("Отличный возраст для карьерного роста!")
    else:
        print("Пора на отдых")

# ages=int(input("Введите год рождения: "))
#
# age(ages)



def calculator():

    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide(a, b):
        if b == 0:
            return "Ошибка: деление на ноль"
        return a / b

    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
    except ValueError:
        return "Ошибка ввода числа."

    operation = input('Введите операцию ( [+], [-], [*], [/] ): ')

    if operation == "+":
        result = add(a, b)
    elif operation == "-":
        result = subtract(a, b)
    elif operation == "*":
        result = multiply(a, b)
    elif operation == "/":
        result = divide(a, b)
    else:
        return "Ошибка: неверная операция."

    return f'Результат: {result}'

#print(calculator())





def chexk_grade(score):
    if 90<=score<= 100:
        return "Отлично"
    elif 75<=score<=89:
        return "Хорошо"
    elif 50<=score<=75:
        return "Удовлетворительно"
    else:
        return "Неудовлетворительно"

print(chexk_grade(75))


def is_even(number):
    return "четное" if number % 2 == 0 else "нечетное"

a=7
b=is_even(a)

print(f"Число {a} является {b}.")



def find_max(a, b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return"числа равны"

p=20
v=20
z=find_max(p, v)

print(f"Максимальное из чисел {p} и {v} : {z}")




def check_number(number):
    if number > 0:
        if number % 2==0:
            return f"Число {number} положительное и четное"
        else:
            return f"Число {number} нечетное"
    else:
        return f"Число {number} отрицательное"

print(check_number(8))
print(check_number(-5))
print(check_number(7))



def check_string_length(string, length):
    if len(string) > length:
        return "Длина строки достаточная"
    else:
        return "Строка слишком короткая"

print(check_string_length("Python", 5))



def sum_numbers(n):
    total = 0           # 1. Мы создаём переменную total и кладём в неё 0.
                        #    Она будет копить сумму всех чисел.

    for i in range(1, n + 1):  # 2. Мы запускаем цикл for от 1 до n включительно.
        total += i      # api_testing_items_crud. На каждой итерации прибавляем текущее число i к total.

    return total

chislo = 5
suma = sum_numbers(chislo)
print(suma)




def find_min0(number):     # Объявляем функцию, принимающую список чисел
    minimal = number[0]   # Начальное значение минимального — первый индекс списка
    for i in number:      # Перебираем все элементы списка
        if i < minimal:   # Если текущий элемент меньше текущего минимума
            minimal = i   # Обновляем и сохраняем минимум
    return minimal        # Возвращаем найденный минимальный элемент

print(find_min0([3, 2, 4, 1, 5]))   # Вызываем функцию и выводим результат (ожидается: 1)





def find_min(numbers):
    min_number = numbers[0]   # 1. Берём первое число как стартовый минимум

    for num in numbers:       # 2. Перебираем все числа по очереди
        if num < min_number:  # api_testing_items_crud. Проверяем: текущее число меньше минимума?
            min_number = num  # 4. Если да — обновляем минимум

    return min_number          # 5. Возвращаем итоговый минимум

# # Пример использования:
numbers = [3, 1, 4, 1, 5]
result = find_min(numbers)
print(f"Минимальное число в списке {numbers}: {result}")





def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0

    for i in string:
        if i in vowels:
            count +=1
    return count

w="Hello World"
rezalt=count_vowels(w)
print(count_vowels("Hello World"))
print(count_vowels(w))
print(rezalt)

def count_vowels(string):
    vowels = "aeiouAEIOU"   # 🎯 Все гласные буквы, и маленькие, и большие
    count = 0               # 🛠 Счётчик гласных, старт с 0

    for char in string:     # 🔄 Перебираем каждый символ в строке
        if char in vowels:  # ❓ Если символ — гласная
            count += 1      # ➕ Увеличиваем счётчик на 1

    return count            # 🎯 Возвращаем итоговое количество гласных

# Пример использования:
result = count_vowels("Hello World")
print(f'Количество гласных в строке "Hello World": {result}')





def print_diamond(rows):

    for i in range(1,rows+1):
        print("* " * i)

    for i in range(rows-1, 0, -1):
        print("* " * i)

print_diamond(5)




def countdown():
    for i in range(10, 0, -1):  # 🔄 Идём от 10 до 1, шаг -1
        print(i)                # 🖨 Печатаем каждое число
    print("Старт!")             # 🖨 После цикла печатаем "Старт!"

# Пример запуска:
countdown()





def countdown():
    i = 10              # 🎯 Стартуем с 10
    while i > 0:        # 🔄 Пока i больше 0
        print(i)        # 🖨 Печатаем i
        i -= 1          # ➖ Уменьшаем i на 1
    print("Старт!")     # 🖨 После цикла печатаем "Старт!"

# Пример запуска:
countdown()


def countdown_w():
    i=10
    while i>0:
        i-=1
        print(i)
    print("Start !")

countdown_w()



# Задача 1: Анаграмма
# Описание:
# Напишите функцию is_anagram(s1, s2), которая проверяет, являются ли две строки анаграммами (перестановками друг друга).
# Требования:
# Функция должна принимать два аргумента: строки s1 и s2.
# Игнорируйте регистр символов.
# Верните True, если строки являются анаграммами, иначе — False.
# Пример:
# print(is_anagram("listen", "silent"))  # True
# print(is_anagram("hello", "world"))    # False

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    # Разная длина — сразу не анаграмма
    if len(s1) != len(s2):
        return False

    # Берём все уникальные буквы из обеих строк
    for char in set(s1 + s2):
        if s1.count(char) != s2.count(char):
            return False

    return True

# 2 вариант
def is_anagram_2(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) != len(s2):
        return False

    return {char: s1.count(char) for char in set(s1)} == \
           {char: s2.count(char) for char in set(s2)}

# Задача 2: Палиндром
# Описание:
# Напишите функцию is_palindrome(s), которая проверяет, является ли строка палиндромом (читается одинаково слева направо и справа налево). Игнорируйте пробелы, знаки препинания и регистр.
# Требования:
# Функция должна принимать один аргумент: строку s.
# Верните True, если строка является палиндромом, иначе — False.
# Пример:
# is_palindrome("A man, a plan, a canal: Panama")  # True
# is_palindrome("racecar")                         # True
# is_palindrome("hello")                           # False

def is_palindrome(s):
    # Приводим строку к нижнему регистру
    s = s.lower()

    # Оставляем только буквы и цифры (убираем пробелы и знаки препинания)
    cleaned = ""
    for char in s:
        if char.isalnum():  # оставляем только буквы и цифры
            cleaned += char

    # Сравниваем строку с её развёрнутой копией (обратный порядок)
    return cleaned == cleaned[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))  #  True
print(is_palindrome("racecar"))                         #  True
print(is_palindrome("hello"))                           #  False


def is_palindrome2(s):
    cleaned = ''.join(char for char in s.lower() if char.isalnum())
    return cleaned == cleaned[::-1]





def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s.lower()))
    return s == s[::-1]


# Задача api_testing_items_crud: Самое длинное слово
# Описание:
# Напишите функцию longest_word(s), которая возвращает самое длинное слово в строке.
# Требования:
# Функция должна принимать один аргумент: строку s.
# Верните самое длинное слово.
# Пример:
# longest_word("In the middle of a vast desert, an extraordinary adventure awaits")  # "extraordinary”

def longest_word(s):
    words = s.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

p="In the middle of a vast desert, an extraordinary adventure awaits"
print(longest_word(p))


# Задача 4: Форматирование номера телефона
# Описание:
# Напишите функцию format_phone_number(digits), которая принимает строку из 10 цифр и возвращает её в формате (XXX) XXX-XXXX.
# Требования:
# Функция должна принимать один аргумент: строку digits.
# Верните отформатированный номер телефона.
# Пример:
# print(format_phone_number("1234567890"))  # "(123) 456-7890”

def format_phone_number(digits):
    if len(digits) != 10 or not digits.isdigit():
        return "Неверный формат номера"
    return f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"


print(format_phone_number("1234567890"))



# Задача 5: Удаление дублирующих символов
# Описание:
# Напишите функцию remove_duplicates(s), которая принимает строку и возвращает новую строку, из которой удалены все повторяющиеся символы, оставляя только первое вхождение каждого символа.
# Требования:
# Функция должна принимать один аргумент: строку s.
# Верните строку без повторяющихся символов.
# Пример:
# remove_duplicates("programming")  # "progamin”

def remove_duplicates(s):
    result=""
    for char in s:
        if char  not in result:
            result += char
    return result


# Задача 6: Проверка на уникальность символов
# Напишите функцию is_unique(s), которая проверяет, содержит ли заданная строка все уникальные символы (без повторов).
# Требования:
# Функция должна принимать один аргумент: строку s.
# Верните True, если все символы уникальны, иначе — False.
# Пример:
# is_unique("abcdef")  # True
# is_unique("hello")  # False

def is_unique(s):
    return len(s)==len(set(s))



# Списки - задачи
# Задача 1: Удаление дубликатов
# Описание:
# Напишите функцию remove_duplicates(lst), которая удаляет все повторяющиеся элементы из списка, оставляя только уникальные значения.
# Требования:
# Функция должна принимать один аргумент: список lst.
# Верните список без повторяющихся элементов.
# Пример:
# print(remove_duplicates([1, 2, 2, api_testing_items_crud, 4, 4]))  # [1, 2, api_testing_items_crud, 4]


def remove_duplicates(lst):
    list1=[]
    for i in lst:
        if i not in list1:
            list1.append(i)
    return list1


# Задача 2: Генерация списка квадратов
# Описание:
# Напишите функцию generate_squares(n), которая генерирует список квадратов чисел от 1 до n.
# Требования:
# Функция должна принимать один аргумент: число n.
# Верните список квадратов.
# Пример:
# print(generate_squares(5))  # [1, 4, 9, 16, 25]

def generate_squares(n):
    return [x**2 for x in range(1,n+1)]

def generate_squares1(n):
    l=[x**2 for x in range(1,n+1)]
    return l

def generate_squares2(n):
    result = []
    for i in range(1, n + 1):
        result.append(i ** 2)
    return result

print(generate_squares2(5))


# Задача api_testing_items_crud: Объединение двух списков
# Описание:
# Напишите функцию merge_lists(list1, list2), которая объединяет два списка, удаляя дубликаты.
# Требования:
# Функция должна принимать два аргумента: списки list1 и list2.
# Используйте множество (set) для удаления дубликатов.
# Верните объединённый список.
# Пример:
# print(merge_lists([1, 2, api_testing_items_crud], [api_testing_items_crud, 4, 5]))  # [1, 2, api_testing_items_crud, 4, 5]


def merge_lists0(list1, list2):
    list1 = list1.copy()          # не трогаем оригинал

    list1.extend(list2)           # объединяем списки
    unique = list(set(list1))     # удаляем дубликаты → список
    unique.sort()                 # сортируем на месте .sort()
    return unique                 # возвращаем готовый результат


def merge_lists(list1, list2):
    list1.extend(list2)
    return sorted(set(list1))

def marge_lists(list1, list2):
    a= list1.copy()
    a.extetnd(list2)
    return sorted(set(a))



# Задача 4: Проверка на отсортированность
# Описание:
# Напишите функцию is_sorted(lst), которая проверяет, является ли список чисел отсортированным по возрастанию.
# Требования:
# Функция должна принимать один аргумент: список lst.
# Верните True, если список отсортирован, иначе — False.
# Пример:
# print(is_sorted([1, 2, api_testing_items_crud, 4, 5]))  # True
# print(is_sorted([1, api_testing_items_crud, 2, 4, 5]))  # False


def is_sorted(lst):
    if lst == sorted(lst):
        return True

def is_sorted2(lst):
    for i in range(len(lst)-1):
        if lst[i]> lst[i+1]:
            return False
    return True

print(is_sorted([1, 2, 3, 5]))
print(is_sorted2([1, 2, 5, 3]))

# Задача 5: Слияние списков
# Описание:
# Напишите функцию merge_lists(list1, list2), которая принимает два списка одинаковой длины и возвращает новый список, где элементы получены путём сложения соответствующих элементов из обоих списков.
# Требования:
# Функция должна принимать два аргумента: списки list1 и list2.
# Используйте генератор списков для создания нового списка.
# Верните список с результатами сложения.
# Пример:
# print(merge_lists([1, 2, api_testing_items_crud], [4, 5, 6]))  # [5, 7, 9]


def merge_lists0(list1, list2):
    return [a + b for a, b in zip(list1, list2)]

# zip(list1, list2) — соединяет элементы попарно:
# [1, 2, api_testing_items_crud] и [4, 5, 6] → [(1, 4), (2, 5), (api_testing_items_crud, 6)]
# a + b — складываем соответствующие элементы


def merge_lists00(list1, list2):
    result = []
    for a, b in zip(list1, list2):
        result.append(a + b)
    return result


def merge_lists1(list1, list2):
    if list1 != list2:
        raise ValueError("Списки должны быть одинаковой длины")

    return [list1[i]+list2[i] for i in range(len(list1))]


def merge_lists2(list1, list2):
    min_len = min(len(list1), len(list2))
    return [list1[i] + list2[i] for i in range(min_len)]

# min(len(list1), len(list2)) — берём минимальную длину
# range(min_len) — не выйдем за границу ни одного списка
# [list1[i] + list2[i] for i in ...] — складываем только то, что есть




# Словари - задачи
# Задача 1: Частотный анализ строки
# Описание:
# Напишите функцию char_frequency(s), которая создаёт словарь, где ключами являются символы строки, а значениями — количество раз, когда каждый символ встречается в строке.
# Требования:
# Функция должна принимать один аргумент: строку s.
# Верните словарь с частотами символов.
# Пример:
# char_frequency("hello")  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}


def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1  # {"Ключ":значение}
        else:
            freq[char] = 1   # {"Ключ":значение}
    return freq


# Задача 2: Слияние двух словарей
# Описание:
# Напишите функцию merge_dicts(dict1, dict2), которая принимает два словаря и объединяет их в один. Если в обоих словарях есть одинаковые ключи, суммируйте их значения (значения только числа).
# Требования:
# Функция должна принимать два аргумента: словари dict1 и dict2.
# Если ключ присутствует в обоих словарях, сложите их значения.
# Верните объединённый словарь.
# Пример:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": api_testing_items_crud, "c": 4}
# print(merge_dicts(dict1, dict2))  # {"a": 1, "b": 5, "c": 4}

def merge_dicts(dict1, dict2):
    result = dict1.copy()  # создаём копию первого словаря

    for key, value in dict2.items():
        if key in result:
            result[key] += value  # если ключ есть — суммируем
        else:
            result[key] = value   # если нет — просто добавляем
    return result


def merge_dicts0(dict1, dict2):

    for key, value in dict2.items():
        if key in dict1:
            dict1[key]+= value
        else:
            dict1[key]=value
    return dict1


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(merge_dicts0(d1, d2))


def merge_dicts2(dict1, dict2):
    all_keys = set(dict1) | set(dict2)  # объединяем ключи из двух словарей
    return {key: dict1.get(key, 0) + dict2.get(key, 0) for key in all_keys}



# Задача api_testing_items_crud: Обратное преобразование словаря в два списка
# Описание:
# Напишите функцию dict_to_lists(my_dict), которая принимает словарь и возвращает два списка: один с ключами и другой с соответствующими значениями.
# Требования:
# Функция должна принимать один аргумент: словарь my_dict.
# Используйте методы .keys() и .values() для извлечения ключей и значений.
# Верните кортеж, содержащий два списка: список ключей и список значений.
# Пример:
# my_dict = {"a": 1, "b": 2, "c": api_testing_items_crud}
# print(dict_to_lists(my_dict))  # (["a", "b", "c"], [1, 2, api_testing_items_crud])


def dict_to_lists(my_dict):
    key=list(my_dict.keys())
    value=list(my_dict.values())
    return (key, value)

my_dict = {"a": 1, "b": 2, "c": 3}
print(dict_to_lists(my_dict))


# Задача 4: Группировка элементов по первому символу
# Описание:
# Напишите функцию group_by_first_letter(strings), которая принимает список строк и группирует их в словарь, где ключами являются первые символы строк, а значением — список строк, начинающихся с этого символа.
# Требования:
# Функция должна принимать один аргумент: список строк strings.
# Верните словарь с группировкой.
# Пример:
# strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
# print(group_by_first_letter(strings))
# # {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}


def group_by_first_letter(strings):
    result = {}  # создаём пустой словарь для группировки

    for word in strings:  # перебираем каждое слово в списке
        first = word[0]  # берём первую букву слова

        if first not in result:
            result[first] = []  # если такой буквы ещё нет в словаре — создаём список

        result[first].append(word)  # добавляем слово в соответствующую группу

    return result  # возвращаем готовый словарь групп



def group_by_f_letter(strings):
    slov={}
    for word in strings:
        ferst_l=word[0]
        if ferst_l not in slov:
            slov[ferst_l]=[]
        slov[ferst_l].append(word)
    return slov

sss = ["apple", "apricot", "banana", "blueberry", "cherry"]

print(group_by_f_letter(sss))


# Задача 5: Извлечение подсловаря
# Описание:
# Напишите функцию extract_subdict(my_dict, keys), которая принимает словарь и список ключей. Функция должна вернуть новый словарь, включающий только те пары, ключи которых содержатся в списке.
# Требования:
# Функция должна принимать два аргумента: словарь my_dict и список ключей keys.
# Верните новый словарь.
# Пример:
# my_dict = {"a": 1, "b": 2, "c": api_testing_items_crud, "d": 4}
# keys = ["a", "c"]
# print(extract_subdict(my_dict, keys))  # {"a": 1, "c": api_testing_items_crud}

def extract_subdict(my_dict, keys):
    return {k: my_dict[k] for k in keys if k in my_dict}


d1 = {"a": 1, "b": 2, "c": 3, "d": 4}
k1 = ["a", "c"]
print(extract_subdict(d1, k1))


# Задача 1: Уникальные элементы списка
# Описание:
# Напишите функцию get_unique_elements(lst), которая принимает список чисел или строк и возвращает новый список, содержащий только уникальные элементы из исходного списка.
# Требования:
# Функция должна принимать один аргумент: список lst.
# Верните список уникальных элементов.
# Пример:
# print(get_unique_elements([1, 2, 2, api_testing_items_crud, 4, 4, 4, 5]))  # [1, 2, api_testing_items_crud, 4, 5]

def get_unique_elements(lst):
    return list(set(lst))

a=[1, 2, 2, 3, 4, 4, 4, 5]
print(get_unique_elements(a))


# Задача 2: Проверка списка на уникальность элементов
# Описание:
# Напишите функцию is_unique_list(lst), которая принимает список и возвращает True, если все элементы списка уникальны, и False, если есть повторения.
# Требования:
# Функция должна принимать один аргумент: список lst.
# Верните True, если все элементы уникальны, иначе — False.
# Пример:
# print(is_unique_list([1, 2, api_testing_items_crud, 4]))  # True
# print(is_unique_list([1, 2, 2, api_testing_items_crud]))  # False

def is_unique_list(lst):
    return len(lst) == len(set(lst))

print(is_unique_list([1, 2, 3, 4]))
print(is_unique_list([1, 2, 2, 3]))



# Задача api_testing_items_crud: Получение уникальных гласных из строки
# Описание:
# Создайте функцию get_unique_vowels(s), которая принимает строку и возвращает набор уникальных гласных, содержащихся в строке (игнорируя регистр).
# Требования:
# Функция должна принимать один аргумент: строку s.
# Гласные буквы: a, e, i, o, u.
# Игнорируйте регистр символов.
# Верните множество уникальных гласных.
# Пример:
# print(get_unique_vowels("Hello World"))  # {'e', 'o'}


def get_unique_vowels(s):
    vowels = "aeiou"
    return {char.lower() for char in s if char.lower() in vowels}

print(get_unique_vowels("Hello World"))


