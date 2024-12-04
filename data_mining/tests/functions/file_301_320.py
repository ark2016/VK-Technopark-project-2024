# 301. Функция для нахождения чисел, которые делятся на 2 и 3
def find_divisible_by_2_and_3(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 302. Функция для нахождения чисел, которые являются результатом возведения в степень
def find_powers_of_numbers(lst, power):
    result = list(map(lambda x: x ** power, lst))
    if not result:
        return None
    return result


# 303. Функция для нахождения чисел, которые являются результатом разности двух чисел в разных списках
def find_difference_between_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(abs(a - b))
    if not result:
        return None
    return result


# 304. Функция для нахождения чисел, которые присутствуют в обоих словарях
def find_keys_in_both_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2:
            result.append(key)
    if not result:
        return None
    return result


# 305. Функция для нахождения чисел, которые являются результатом произведения чисел из двух списков
def find_product_of_elements_from_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a * b)
    if not result:
        return None
    return result


# 306. Функция для нахождения чисел, которые присутствуют в словаре, но не в списке
def find_keys_in_dict_not_in_list(d, lst):
    result = []
    for key in d:
        if key not in lst:
            result.append(key)
    if not result:
        return None
    return result


# 307. Функция для нахождения чисел, которые являются результатом возведения чисел из списка в степень
def find_powers_of_numbers_in_list(lst, power):
    result = []
    for num in lst:
        result.append(num ** power)
    if not result:
        return None
    return result


# 308. Функция для нахождения чисел, которые присутствуют в обоих множествах
def find_elements_in_both_sets(set1, set2):
    result = list(set1 & set2)
    if not result:
        return None
    return result


# 309. Функция для нахождения чисел, которые являются разницей элементов из двух списков
def find_diff_between_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(abs(a - b))
    if not result:
        return None
    return result


# 310. Функция для нахождения чисел, которые являются результатом сложения чисел в двух списках
def find_sum_of_two_lists_2(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a + b)
    if not result:
        return None
    return result


# 311. Функция для нахождения чисел, которые присутствуют в кортеже, но не в списке
def find_in_tuple_not_in_list(tpl, lst):
    result = []
    for num in tpl:
        if num not in lst:
            result.append(num)
    if not result:
        return None
    return result


# 312. Функция для нахождения чисел, которые делятся на 10, но не на 20
def find_divisible_by_10_not_20(lst):
    result = []
    for num in lst:
        if num % 10 == 0 and num % 20 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 313. Функция для нахождения чисел, которые являются суммой элементов из двух списков
def find_sum_from_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a + b)
    if not result:
        return None
    return result


# 314. Функция для нахождения чисел, которые присутствуют в обоих множествах
def find_common_elements_in_sets(set1, set2):
    result = list(set1 & set2)
    if not result:
        return None
    return result


# 315. Функция для нахождения чисел, которые являются произведением чисел в списке
def find_product_in_list(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            result.append(lst[i] * lst[j])
    if not result:
        return None
    return result


# 316. Функция для нахождения чисел, которые присутствуют в списке и не присутствуют в словаре
def find_in_list_not_in_dict(lst, d):
    result = []
    for num in lst:
        if num not in d:
            result.append(num)
    if not result:
        return None
    return result


# 317. Функция для объединения двух словарей
def merge_dicts_2(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    if not result:
        return None
    return result


# 318. Функция для нахождения чисел, которые присутствуют в одном из двух наборов
def find_in_one_set_not_other(set1, set2):
    result = set1.symmetric_difference(set2)
    if not result:
        return None
    return list(result)


# 319. Функция для нахождения чисел, которые являются результатом деления элементов из двух списков
def find_division_from_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:
            result.append(a / b)
    if not result:
        return None
    return result


# 320. Функция для нахождения чисел, которые присутствуют в обоих списках, но в одном из них меньше
def find_common_less_in_one_list(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2 and lst1.count(num) < lst2.count(num):
            result.append(num)
    if not result:
        return None
    return result
