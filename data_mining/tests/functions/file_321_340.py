# 321. Функция для нахождения чисел, которые находятся в одном списке, но не в другом
def find_in_first_not_in_second(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    if not result:
        return None
    return result


# 322. Функция для нахождения чисел, которые присутствуют в обоих списках, но имеют разные индексы
def find_common_elements_diff_index(lst1, lst2):
    result = []
    for i, num1 in enumerate(lst1):
        for j, num2 in enumerate(lst2):
            if num1 == num2 and i != j:
                result.append(num1)
    if not result:
        return None
    return sorted(set(result))


# 323. Функция для нахождения чисел, которые являются результатом добавления элементов из двух словарей
def add_values_of_dicts(dict1, dict2):
    result = {}
    for key in dict1:
        if key in dict2:
            result[key] = dict1[key] + dict2[key]
    if not result:
        return None
    return result


# 324. Функция для нахождения чисел, которые находятся в двух множествах, но в одном из них больше
def find_more_in_one_set(set1, set2):
    result = []
    list1, list2 = list(set1), list(set2)
    for num in set1:
        if num in set2 and num % 3 == 0:
            result.append(num)
    if not result:
        return None
    return sorted(result)


# 325. Функция для нахождения чисел, которые являются результатом умножения чисел в списке на два
def multiply_numbers_by_two(lst):
    result = []
    for num in lst:
        result.append(num * 2)
    if not result:
        return None
    return result


# 326. Функция для нахождения чисел, которые являются результатом суммы значений по ключам в словарях
def sum_dict_values(dict1, dict2):
    result = {}
    for key in dict1:
        if key in dict2:
            result[key] = dict1[key] + dict2[key]
    if not result:
        return None
    return result


# 327. Функция для нахождения чисел, которые являются квадратами чисел из списка
def find_squares_2(lst):
    result = []
    for num in lst:
        result.append(num ** 2)
    if not result:
        return None
    return result


# 328. Функция для нахождения чисел, которые являются разницей элементов из двух множеств
def find_difference_of_sets(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return sorted(result)


# 329. Функция для нахождения чисел, которые являются результатом суммирования элементов из списка и множества
def find_sum_list_set(lst, s):
    result = []
    for num in lst:
        if num in s:
            result.append(num + 1)
    if not result:
        return None
    return result


# 330. Функция для нахождения чисел, которые встречаются в одном множестве, но не в другом
def find_in_set_not_in_other_set(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result


# 331. Функция для нахождения чисел, которые являются результатом деления элементов одного списка на элементы другого
def divide_elements_of_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:  # избегаем деления на ноль
            result.append(a / b)
    if not result:
        return None
    return result


# 332. Функция для нахождения чисел, которые находятся в двух множествах, но не в одном из них
def find_in_both_sets_not_in_one(set1, set2):
    result = list(set1 & set2 ^ (set1 | set2))
    if not result:
        return None
    return sorted(result)


# 333. Функция для нахождения чисел, которые являются результатом вычитания элементов из списка и множества
def subtract_set_from_list(lst, s):
    result = []
    for num in lst:
        if num not in s:
            result.append(num)
    if not result:
        return None
    return result


# 334. Функция для нахождения чисел, которые являются результатом суммирования элементов из двух кортежей
def find_sum_of_tuples(tpl1, tpl2):
    result = []
    for a, b in zip(tpl1, tpl2):
        result.append(a + b)
    if not result:
        return None
    return result


# 335. Функция для нахождения чисел, которые присутствуют в одном из двух множеств
def find_in_one_set_not_other_2(set1, set2):
    result = list(set1 ^ set2)  # Симметрическая разница
    if not result:
        return None
    return result


# 336. Функция для нахождения чисел, которые делятся на 4, но не на 8
def find_divisible_by_4_not_8(lst):
    result = []
    for num in lst:
        if num % 4 == 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 337. Функция для нахождения чисел, которые присутствуют в одном словаре, но не в другом
def find_keys_in_dict1_not_in_dict2(dict1, dict2):
    result = []
    for key in dict1:
        if key not in dict2:
            result.append(key)
    if not result:
        return None
    return result


# 338. Функция для нахождения чисел, которые являются результатом умножения чисел в одном списке на два
def multiply_by_two(lst):
    result = []
    for num in lst:
        result.append(num * 2)
    if not result:
        return None
    return result


# 339. Функция для нахождения чисел, которые являются результатом вычитания элементов одного списка из другого
def subtract_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a - b)
    if not result:
        return None
    return result


# 340. Функция для нахождения чисел, которые присутствуют в обоих словарях
def find_common_in_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2:
            result.append(key)
    if not result:
        return None
    return result
