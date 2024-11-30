# 941. Функция для нахождения строк, длина которых больше заданного числа, из списка и словаря
def find_long_strings_6(lst, d, length):
    if not lst or not d:
        return None
    long_strings = []
    for item in lst:
        if isinstance(item, str) and len(item) > length:
            long_strings.append(item)
    for value in d.values():
        if isinstance(value, str) and len(value) > length:
            long_strings.append(value)
    return tuple(long_strings) if long_strings else None


# 942. Функция для нахождения чисел, которые больше всех чисел в словаре, и добавление их в множество
def find_numbers_greater_than_dict_values(lst, d):
    if not lst or not d:
        return None
    greater_numbers = set()
    max_value = max(d.values())
    for n in lst:
        if n > max_value:
            greater_numbers.add(n)
    return greater_numbers if greater_numbers else None


# 943. Функция для подсчёта, сколько раз встречаются числа в списке, и создание словаря с этим количеством
def count_numbers_in_list(lst):
    if not lst:
        return None
    count_dict = {}
    for n in lst:
        count_dict[n] = count_dict.get(n, 0) + 1
    return count_dict if count_dict else None


# 944. Функция для создания списка чисел, которые есть в словаре и кортежах
def find_numbers_in_dict_and_tuple(d, t):
    if not d or not t:
        return None
    result = []
    for value in d.values():
        if value in t:
            result.append(value)
    return result if result else None


# 945. Функция для создания словаря, где ключи — это элементы списка, а значения — их индексы
def create_index_dict(lst):
    if not lst:
        return None
    index_dict = {}
    for i, item in enumerate(lst):
        index_dict[item] = i
    return index_dict if index_dict else None


# 946. Функция для создания множества всех уникальных символов из строк в списке и словаре
def create_unique_char_set(lst, d):
    if not lst or not d:
        return None
    char_set = set()
    for s in lst:
        if isinstance(s, str):
            char_set.update(s)
    for value in d.values():
        if isinstance(value, str):
            char_set.update(value)
    return char_set if char_set else None


# 947. Функция для подсчёта уникальных элементов в списке и добавления их в словарь
def count_unique_elements(lst):
    if not lst:
        return None
    count_dict = {}
    for item in lst:
        count_dict[item] = count_dict.get(item, 0) + 1
    return count_dict if count_dict else None


# 948. Функция для нахождения чисел, которые являются квадратами чисел из множества
def find_squares_in_set(s):
    if not s:
        return None
    result = []
    for n in s:
        if (n ** 0.5).is_integer():
            result.append(n)
    return tuple(result) if result else None


# 949. Функция для нахождения строк с числовыми символами, которые встречаются в списке и словаре
def find_numeric_strings(lst, d):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if isinstance(item, str) and any(char.isdigit() for char in item):
            result.append(item)
    for value in d.values():
        if isinstance(value, str) and any(char.isdigit() for char in value):
            result.append(value)
    return tuple(result) if result else None


# 950. Функция для нахождения чисел в списке, которые равны числовым значениям в словаре
def find_equal_numbers(lst, d):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if item in d.values():
            result.append(item)
    return tuple(result) if result else None


# 951. Функция для нахождения всех чисел, которые могут быть составлены из цифр строки
def find_numbers_from_string(s):
    if not s:
        return None
    result = []
    for char in s:
        if char.isdigit():
            result.append(int(char))
    return tuple(result) if result else None


# 952. Функция для создания списка, где элементы — это чётные индексы словаря
def create_even_indexed_list(d):
    if not d:
        return None
    result = []
    for i, (key, value) in enumerate(d.items()):
        if i % 2 == 0:
            result.append((key, value))
    return result if result else None


# 953. Функция для нахождения чисел, которые встречаются в списке, но отсутствуют в множестве
def find_numbers_not_in_set(lst, s):
    if not lst or not s:
        return None
    result = []
    for item in lst:
        if item not in s:
            result.append(item)
    return tuple(result) if result else None


# 954. Функция для создания словаря, где ключи — это элементы списка, а значения — множества их делителей
def create_divisors_dict(lst):
    if not lst:
        return None
    divisors_dict = {}
    for item in lst:
        divisors = {i for i in range(1, item + 1) if item % i == 0}
        divisors_dict[item] = divisors
    return divisors_dict if divisors_dict else None


# 955. Функция для нахождения чисел, которые одновременно больше и меньше заданных значений
def find_numbers_between_bounds(lst, lower, upper):
    if not lst:
        return None
    result = []
    for n in lst:
        if lower < n < upper:
            result.append(n)
    return tuple(result) if result else None


# 956. Функция для нахождения всех значений из словаря, которые меньше заданного числа
def find_values_less_than(d, num):
    if not d:
        return None
    result = []
    for value in d.values():
        if value < num:
            result.append(value)
    return tuple(result) if result else None


# 957. Функция для создания словаря, где ключи — это элементы множества, а значения — их длины (если это строки)
def create_length_dict_from_set(s):
    if not s:
        return None
    length_dict = {}
    for item in s:
        if isinstance(item, str):
            length_dict[item] = len(item)
    return length_dict if length_dict else None


# 958. Функция для создания списка чисел, которые являются нечётными в списке и чётными в словаре
def find_odd_in_list_and_even_in_dict(lst, d):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if item % 2 != 0 and item in d:
            if d[item] % 2 == 0:
                result.append(item)
    return result if result else None


# 959. Функция для создания множества, которое объединяет все чётные числа из списка и множества
def create_even_number_set(lst, s):
    if not lst or not s:
        return None
    even_set = set()
    for item in lst:
        if item % 2 == 0:
            even_set.add(item)
    for item in s:
        if item % 2 == 0:
            even_set.add(item)
    return even_set if even_set else None


# 960. Функция для нахождения чисел из списка и словаря, которые больше среднего в словаре
def find_numbers_greater_than_avg_in_dict(lst, d):
    if not lst or not d:
        return None
    avg = sum(d.values()) / len(d)
    result = []
    for item in lst:
        if item > avg:
            result.append(item)
    return tuple(result) if result else None
