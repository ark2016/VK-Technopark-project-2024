# 101. Функция для проверки, является ли строка анаграммой другой строки
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        print("Strings are not of equal length.")
        return False
    char_count = {}
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s2:
        if char not in char_count or char_count[char] == 0:
            print(f"'{char}' is not in the first string or appears too many times.")
            return False
        char_count[char] -= 1
    return True


# 102. Функция для нахождения пересечения двух множеств
def intersection_of_sets(set1, set2):
    intersection = set1.intersection(set2)
    if not intersection:
        print("The sets have no common elements.")
    return intersection


# 103. Функция для удаления дубликатов из списка кортежей по первому элементу
def remove_duplicate_tuples(lst):
    seen = set()
    result = []
    for item in lst:
        if item[0] not in seen:
            seen.add(item[0])
            result.append(item)
    return result


# 104. Функция для подсчёта элементов в строках списка, возвращая словарь с длинами строк
def count_string_lengths(lst):
    length_dict = {}
    for s in lst:
        length_dict[s] = len(s)
    return length_dict


# 105. Функция для нахождения числа, которое встречается больше всех раз в словаре (ключи - элементы, значения - количество)
def most_frequent_in_dict(d):
    if not d:
        print("Dictionary is empty.")
        return None
    max_key = max(d, key=d.get)
    return max_key, d[max_key]


# 106. Функция для объединения двух словарей (если есть одинаковые ключи, их значения суммируются)
def merge_dicts(d1, d2):
    merged = d1.copy()
    for key, value in d2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged


# 107. Функция для подсчёта чётных и нечётных чисел в списке с использованием словаря
def count_even_odd(lst):
    count = {"even": 0, "odd": 0}
    for num in lst:
        if num % 2 == 0:
            count["even"] += 1
        else:
            count["odd"] += 1
    return count


# 108. Функция для нахождения минимального ключа в словаре с числовыми значениями
def min_key_in_dict(d):
    if not d:
        print("Dictionary is empty.")
        return None
    return min(d, key=d.get)


# 109. Функция для создания словаря из списка, где элементы списка становятся значениями, а их индексы — ключами
def list_to_dict(lst):
    result = {}
    for index, value in enumerate(lst):
        result[index] = value
    return result


# 110. Функция для проверки, является ли строка числом, и если да — вернуть её квадрат
def check_and_square(s):
    try:
        num = float(s)
        return num ** 2
    except ValueError:
        print(f"'{s}' is not a valid number.")
        return None


# 111. Функция для объединения двух кортежей, убирая повторяющиеся элементы
def merge_tuples(t1, t2):
    return tuple(sorted(set(t1 + t2)))


# 112. Функция для нахождения всех уникальных чисел в списке (с использованием множества)
def unique_numbers(lst):
    unique = set()
    for num in lst:
        unique.add(num)
    return sorted(list(unique))


# 113. Функция для создания словаря, где ключами будут уникальные элементы списка, а значениями — количество их повторений
def create_frequency_dict(lst):
    frequency_dict = {}
    for item in lst:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict


# 114. Функция для нахождения элементов, которые присутствуют в одном списке, но отсутствуют в другом
def difference_of_lists(lst1, lst2):
    result = []
    for item in lst1:
        if item not in lst2:
            result.append(item)
    for item in lst2:
        if item not in lst1:
            result.append(item)
    return result


# 115. Функция для нахождения всех элементов списка, которые встречаются в другой коллекции
def find_in_collection(lst, collection):
    result = []
    for item in lst:
        if item in collection:
            result.append(item)
    if not result:
        print("No elements found in the collection.")
    return result


# 116. Функция для нахождения суммы всех чисел в списке, которые встречаются более одного раза
def sum_of_duplicates(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    total = 0
    for key, value in count_dict.items():
        if value > 1:
            total += key
    if total == 0:
        print("No duplicates found.")
    return total


# 117. Функция для нахождения элементов, которые присутствуют в одном списке и не встречаются в другом
def unique_in_first(lst1, lst2):
    unique_elements = []
    for item in lst1:
        if item not in lst2:
            unique_elements.append(item)
    if not unique_elements:
        print("No unique elements found in the first list.")
    return unique_elements


# 118. Функция для нахождения минимального общего кратного двух чисел
def lcm_1(a, b):
    if a == 0 or b == 0:
        print("LCM is undefined for 0.")
        return None

    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return abs(a * b) // gcd(a, b)


# 119. Функция для получения всех элементов из словаря, чьи значения больше заданного порога
def filter_dict_by_value(d, threshold):
    result = {}
    for key, value in d.items():
        if value > threshold:
            result[key] = value
    if not result:
        print("No elements above the threshold.")
    return result


# 120. Функция для переворота словаря, меняя местами ключи и значения
def reverse_dict(d):
    reversed_dict = {}
    for key, value in d.items():
        if value in reversed_dict:
            print(f"Duplicate value {value} found, skipping.")
        else:
            reversed_dict[value] = key
    return reversed_dict
