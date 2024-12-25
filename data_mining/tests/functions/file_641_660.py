# 641. Функция для извлечения уникальных элементов из списка с сохранением порядка
def unique_elements_6(arr):
    seen = set()
    result = []
    for el in arr:
        if el not in seen:
            result.append(el)
            seen.add(el)
    return result


# 642. Функция для поиска строки в тексте с учетом возможных пробелов
def find_word_in_text(text, word):
    index = text.find(word)
    if index != -1:
        return f"Word found at index {index}"
    return "Word not found"


# 643. Функция для определения, является ли строка числом (целым или с плавающей точкой)
def is_number_5(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# 644. Функция для объединения двух словарей, при этом значения по одинаковым ключам складываются
def merge_dicts_6(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result


# 645. Функция для извлечения элементов с четными индексами из списка
def even_index_elements(arr):
    return [arr[i] for i in range(0, len(arr), 2)]


# 646. Функция для инвертирования словаря (меняем местами ключи и значения)
def invert_dict(d):
    return {v: k for k, v in d.items()}


# 647. Функция для слияния двух отсортированных списков в один отсортированный
def merge_sorted_lists_5(list1, list2):
    merged = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged


# 648. Функция для замены каждого второго символа в строке на звездочку
def replace_second_char(s):
    return ''.join([c if i % 2 == 0 else '*' for i, c in enumerate(s)])


# 649. Функция для получения уникальных чисел из списка с их суммой
def unique_numbers_and_sum(lst):
    seen = set()
    unique_numbers = []
    for num in lst:
        if num not in seen:
            unique_numbers.append(num)
            seen.add(num)
    total = sum(unique_numbers)
    return unique_numbers, total


# 650. Функция для проверки, является ли строка правильным email
def is_valid_email_2(email):
    if "@" not in email or "." not in email:
        return False
    username, domain = email.split("@", 1)
    if not username or not domain:
        return False
    return True


# 651. Функция для подсчета всех слов в строке с учётом знаков препинания
def count_words_in_string_2(s):
    words = s.split()
    return len(words)


# 652. Функция для нахождения максимального числа в списке с проверкой на пустоту
def max_in_list(lst):
    if not lst:
        return None
    return max(lst)


# 653. Функция для преобразования строки в список чисел, разделенных запятой
def string_to_numbers_2(s):
    return [int(x) for x in s.split(",") if x.strip().isdigit()]


# 654. Функция для вычисления степени числа с обработкой возможных ошибок
def power_5(base, exponent):
    try:
        return base ** exponent
    except TypeError:
        return "Invalid input"


# 655. Функция для генерации списка всех чисел от 1 до N, которые делятся на X
def divisible_by_x_5(n, x):
    return [i for i in range(1, n + 1) if i % x == 0]


# 656. Функция для вычисления длины строки, игнорируя пробелы
def length_without_spaces(s):
    return len(s.replace(" ", ""))


# 657. Функция для проверки, является ли строка числом в десятичной системе
def is_decimal(s):
    try:
        float(s)
        return '.' in s
    except ValueError:
        return False


# 658. Функция для изменения регистра в строках, включая те, которые начинаются с пробела
def change_case_and_strip(s):
    return s.strip().upper() if s.startswith(" ") else s.lower()


# 659. Функция для нахождения индекса первого отрицательного числа в списке
def find_first_negative(arr):
    if not arr:
        return None
    for i in range(len(arr)):
        if arr[i] < 0:
            return i
    return None


# 660. Функция для удаления всех повторяющихся элементов из списка, сохраняя порядок
def remove_duplicates_5(arr):
    if not arr:
        return arr
    seen = set()
    result = []
    for el in arr:
        if el not in seen:
            result.append(el)
            seen.add(el)
    return result
