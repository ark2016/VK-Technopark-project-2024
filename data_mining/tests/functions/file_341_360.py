# 341. Функция для нахождения чисел, которые являются результатом сложения всех чисел в списке
def sum_list_3(lst):
    return sum(lst) if lst else None


# 342. Функция для нахождения чисел, которые делятся на 3, но не на 9
def find_divisible_by_3_not_9(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 343. Функция для нахождения чисел, которые делятся на 5 или 7
def find_divisible_by_5_or_7(lst):
    result = []
    for num in lst:
        if num % 5 == 0 or num % 7 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 344. Функция для нахождения чисел, которые присутствуют в одном из двух словарей
def find_in_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2:
            result.append(key)
    if not result:
        return None
    return result


# 345. Функция для нахождения чисел, которые делятся на 3 или 5
def find_divisible_by_3_or_5(lst):
    result = []
    for num in lst:
        if num % 3 == 0 or num % 5 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 346. Функция для нахождения чисел, которые делятся на 4, но не на 6
def find_divisible_by_4_not_6(lst):
    result = []
    for num in lst:
        if num % 4 == 0 and num % 6 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 347. Функция для нахождения чисел, которые делятся на 5, но не на 10
def find_divisible_by_5_not_10(lst):
    result = []
    for num in lst:
        if num % 5 == 0 and num % 10 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 348. Функция для нахождения чисел, которые являются результатом возведения элементов списка в степень
def find_powers_of_list(lst, power):
    result = []
    for num in lst:
        result.append(num ** power)
    if not result:
        return None
    return result


# 349. Функция для нахождения чисел, которые делятся на 6, но не на 12
def find_divisible_by_6_not_12(lst):
    result = []
    for num in lst:
        if num % 6 == 0 and num % 12 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 350. Функция для нахождения чисел, которые делятся на 4 или 5
def find_divisible_by_4_or_5(lst):
    result = []
    for num in lst:
        if num % 4 == 0 or num % 5 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 351. Функция для нахождения чисел, которые присутствуют в одном списке, но не в другом
def find_in_list_not_in_another(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    if not result:
        return None
    return result


# 352. Функция для нахождения чисел, которые присутствуют в одном словаре, но не в другом
def find_unique_keys_in_dict(dict1, dict2):
    result = []
    for key in dict1:
        if key not in dict2:
            result.append(key)
    if not result:
        return None
    return result


# 353. Функция для нахождения чисел, которые являются произведением чисел из двух списков
def multiply_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a * b)
    if not result:
        return None
    return result


# 354. Функция для нахождения чисел, которые являются результатом вычитания элементов одного списка из другого
def subtract_lists_v2(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a - b)
    if not result:
        return None
    return result


# 355. Функция для нахождения чисел, которые присутствуют в одном множестве, но не в другом
def find_in_set_not_other(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result


# 356. Функция для нахождения чисел, которые присутствуют в обоих множествах
def find_common_in_sets(set1, set2):
    result = list(set1 & set2)
    if not result:
        return None
    return result


# 357. Функция для нахождения чисел, которые делятся на 2 и присутствуют в двух множествах
def find_divisible_by_2_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 2 == 0})
    if not result:
        return None
    return result


# 358. Функция для нахождения чисел, которые не делятся на 3 и присутствуют в двух множествах
def find_not_divisible_by_3_in_both_sets(set1, set2):
    result = list((set1 & set2) - {num for num in range(1, 101) if num % 3 == 0})
    if not result:
        return None
    return result


# 359. Функция для нахождения чисел, которые присутствуют в одном множестве и не присутствуют в другом
def find_in_one_set_not_other_v2(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result


# 360. Функция для нахождения чисел, которые делятся на 2 или 5, и присутствуют в двух множествах
def find_divisible_by_2_or_5_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 2 == 0 or num % 5 == 0})
    if not result:
        return None
    return result
