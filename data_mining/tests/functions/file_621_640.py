# 621. Функция для подсчета количества нечетных чисел в кольцевом массиве
def count_odd_ring(arr):
    if not arr:
        return 0
    return sum(1 for x in arr if x % 2 != 0)


# 622. Функция для добавления элемента в кольцевой массив только если он еще не существует
def append_unique_ring(arr, element):
    if element not in arr:
        arr.append(element)
    return arr


# 623. Функция для нахождения всех элементов кольцевого массива, которые делятся на X
def find_divisible_ring(arr, x):
    if not arr:
        return []
    return [el for el in arr if el % x == 0]


# 624. Функция для удаления всех элементов, которые меньше заданного числа
def remove_less_than_ring(arr, threshold):
    if not arr:
        return arr
    return [x for x in arr if x >= threshold]


# 625. Функция для очистки кольцевого массива от элементов, больших заданного числа
def remove_greater_than_ring(arr, threshold):
    if not arr:
        return arr
    return [x for x in arr if x <= threshold]


# 626. Функция для преобразования строки в список символов, с проверкой на пустоту
def string_to_list(s):
    if s == "":
        return []
    return list(s)


# 627. Функция для объединения двух списков без повторений
def merge_unique_lists(list1, list2):
    return sorted(list(set(list1 + list2)))


# 628. Функция для создания множества из строк, игнорируя регистр
def set_from_strings_ignore_case(strings):
    return sorted({s.lower() for s in strings})


# 629. Функция для подсчета количества вхождений каждого символа в строку
def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


# 630. Функция для проверки, является ли строка палиндромом
def is_palindrome_5(s):
    cleaned = ''.join(e for e in s if e.isalnum()).lower()
    return cleaned == cleaned[::-1]


# 631. Функция для вычисления факториала числа с использованием рекурсии
def factorial_4(n):
    if n == 0:
        return 1
    return n * factorial_4(n - 1)


# 632. Функция для подсчета числа всех вхождений слова в тексте
def count_word_occurrences(text, word):
    words = text.split()
    count = 0
    for w in words:
        if w == word:
            count += 1
    return count


# 633. Функция для фильтрации строк, которые содержат только цифры
def filter_numeric_strings(strings):
    return [s for s in strings if s.isdigit()]


# 634. Функция для поиска ближайшего к числу в списке
def closest_number(arr, num):
    if not arr:
        return None
    closest = arr[0]
    for x in arr:
        if abs(x - num) < abs(closest - num):
            closest = x
    return closest


# 635. Функция для сортировки списка словарей по заданному ключу
def sort_dicts_by_key(lst, key):
    return sorted(lst, key=lambda x: x.get(key, 0))


# 636. Функция для поиска наибольшего общего делителя двух чисел
def gcd_5(a, b):
    while b:
        a, b = b, a % b
    return a


# 637. Функция для вычисления среднего арифметического элементов списка с защитой от деления на 0
def average_6(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


# 638. Функция для преобразования строки в формат "заглавными и маленькими буквами"
def alternate_case(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])


# 639. Функция для подсчета, сколько раз встречается каждый элемент в списке
def count_elements(arr):
    counts = {}
    for el in arr:
        counts[el] = counts.get(el, 0) + 1
    return counts


# 640. Функция для преобразования списка в строку через разделитель
def list_to_string(lst, separator=","):
    return separator.join(map(str, lst))
