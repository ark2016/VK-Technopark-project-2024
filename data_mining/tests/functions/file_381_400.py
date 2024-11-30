# 381. Функция для нахождения чисел, которые присутствуют в двух множествах и не делятся на 3
def find_in_both_sets_not_divisible_by_3(set1, set2):
    result = list((set1 & set2) - {num for num in range(1, 101) if num % 3 == 0})
    if not result:
        return None
    return result


# 382. Функция для нахождения чисел, которые присутствуют только в одном из двух множеств
def find_unique_in_one_set(set1, set2):
    result = list(set1 ^ set2)  # Симметрическая разница
    if not result:
        return None
    return result


# 383. Функция для нахождения чисел, которые присутствуют в одном множестве, но не в другом
def find_in_set_not_other_v3(set1, set2):
    result = []
    for elem in set1:
        if elem not in set2:
            result.append(elem)
    if not result:
        return None
    return result


# 384. Функция для нахождения чисел, которые являются пересечением двух множеств и делятся на 3
def find_common_divisible_by_3(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 385. Функция для нахождения чисел, которые присутствуют в одном из двух множеств, но не в обоих
def find_in_one_set_not_other_v3(set1, set2):
    result = []
    for elem in set1 | set2:
        if (elem in set1) != (elem in set2):  # Проверка на симметричную разницу
            result.append(elem)
    if not result:
        return None
    return result


# 386. Функция для нахождения чисел, которые делятся на 2, но не на 4 и присутствуют в двух множествах
def find_divisible_by_2_not_4_in_both_sets(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 2 == 0 and elem % 4 != 0:
            result.append(elem)
    if not result:
        return None
    return result


# 387. Функция для нахождения чисел, которые присутствуют в двух множествах и не делятся на 5
def find_in_both_sets_not_divisible_by_5(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 5 != 0:
            result.append(elem)
    if not result:
        return None
    return result


# 388. Функция для нахождения чисел, которые присутствуют в обоих множествах и делятся на 3
def find_in_both_sets_divisible_by_3(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 389. Функция для нахождения чисел, которые присутствуют в одном из двух множеств, но не в обоих
def find_unique_in_sets_v2(set1, set2):
    result = []
    for elem in set1 ^ set2:  # Симметрическая разница
        result.append(elem)
    if not result:
        return None
    return result


# 390. Функция для нахождения чисел, которые присутствуют в первом множестве, но не во втором, и делятся на 7
def find_in_first_set_not_second_divisible_by_7(set1, set2):
    result = []
    for elem in set1 - set2:
        if elem % 7 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 391. Функция для нахождения чисел, которые делятся на 6, но не на 12 и присутствуют в двух множествах
def find_divisible_by_6_not_12_in_both_sets_2(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 6 == 0 and elem % 12 != 0:
            result.append(elem)
    if not result:
        return None
    return result


# 392. Функция для нахождения чисел, которые присутствуют в одном из двух множеств, но не в обоих, и делятся на 5
def find_in_one_set_not_other_divisible_by_5(set1, set2):
    result = []
    for elem in set1 ^ set2:  # Симметрическая разница
        if elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 393. Функция для нахождения чисел, которые являются общими для двух множеств и делятся на 4
def find_common_in_sets_divisible_by_4(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 4 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 394. Функция для нахождения чисел, которые делятся на 3 и присутствуют в обоих множествах
def find_divisible_by_3_in_both_sets(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 395. Функция для нахождения чисел, которые присутствуют только в одном из двух множеств, но не в другом
def find_difference_in_sets_v2(set1, set2):
    result = []
    for elem in set1 - set2:
        result.append(elem)
    for elem in set2 - set1:
        result.append(elem)
    if not result:
        return None
    return result


# 396. Функция для нахождения чисел, которые присутствуют в двух множествах и делятся на 4
def find_divisible_by_4_in_both_sets_2(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 4 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 397. Функция для нахождения чисел, которые присутствуют только в одном множестве и не делятся на 3
def find_unique_not_divisible_by_3(set1, set2):
    result = []
    for elem in set1 - set2:
        if elem % 3 != 0:
            result.append(elem)
    for elem in set2 - set1:
        if elem % 3 != 0:
            result.append(elem)
    if not result:
        return None
    return result


# 398. Функция для нахождения чисел, которые делятся на 5 и присутствуют в двух множествах
def find_divisible_by_5_in_both_sets(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 399. Функция для нахождения чисел, которые присутствуют в обоих множествах и не делятся на 2
def find_in_both_sets_not_divisible_by_2(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 2 != 0:
            result.append(elem)
    if not result:
        return None
    return result


# 400. Функция для нахождения чисел, которые являются разностью между двумя множествами
def find_difference_between_sets(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result
