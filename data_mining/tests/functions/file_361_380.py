# 361. Функция для нахождения чисел, которые не делятся на 2 или 3, и присутствуют в двух множествах
def find_not_divisible_by_2_or_3_in_both_sets(set1, set2):
    result = list((set1 & set2) - {num for num in range(1, 101) if num % 2 == 0 or num % 3 == 0})
    if not result:
        return None
    return result


# 362. Функция для нахождения чисел, которые делятся на 4 и присутствуют в обоих множествах
def find_divisible_by_4_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 4 == 0})
    if not result:
        return None
    return result


# 363. Функция для нахождения чисел, которые присутствуют в одном множестве, но не в другом
def find_in_set_not_other_v2(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result


# 364. Функция для нахождения чисел, которые присутствуют в одном из двух множеств
def find_in_any_set(set1, set2):
    result = list(set1 | set2)  # Объединение
    if not result:
        return None
    return result


# 365. Функция для нахождения чисел, которые делятся на 7 и присутствуют в обоих множествах
def find_divisible_by_7_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 7 == 0})
    if not result:
        return None
    return result


# 366. Функция для нахождения чисел, которые присутствуют в одном множестве, но не в другом
def find_difference_in_sets(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result


# 367. Функция для нахождения чисел, которые не делятся на 2, но присутствуют в обоих множествах
def find_not_divisible_by_2_in_both_sets(set1, set2):
    result = list((set1 & set2) - {num for num in range(1, 101) if num % 2 == 0})
    if not result:
        return None
    return result


# 368. Функция для нахождения чисел, которые являются общими для трёх множеств
def find_common_in_three_sets(set1, set2, set3):
    result = list(set1 & set2 & set3)
    if not result:
        return None
    return result


# 369. Функция для нахождения чисел, которые являются разностью элементов из трёх множеств
def find_difference_in_three_sets(set1, set2, set3):
    result = list(set1 - set2 - set3)
    if not result:
        return None
    return result


# 370. Функция для нахождения чисел, которые присутствуют в одном множестве, но не в другом
def find_diff_in_sets_v2(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result


# 371. Функция для нахождения чисел, которые не делятся на 5 и присутствуют в обоих множествах
def find_not_divisible_by_5_in_both_sets(set1, set2):
    result = list((set1 & set2) - {num for num in range(1, 101) if num % 5 == 0})
    if not result:
        return None
    return result


# 372. Функция для нахождения чисел, которые делятся на 3 или 6 и присутствуют в обоих множествах
def find_divisible_by_3_or_6_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 3 == 0 or num % 6 == 0})
    if not result:
        return None
    return result


# 373. Функция для нахождения чисел, которые являются общими для двух множеств и делятся на 3
def find_common_in_sets_divisible_by_3(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 3 == 0})
    if not result:
        return None
    return result


# 374. Функция для нахождения чисел, которые делятся на 6, но не на 12 и присутствуют в двух множествах
def find_divisible_by_6_not_12_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 6 == 0 and num % 12 != 0})
    if not result:
        return None
    return result


# 375. Функция для нахождения чисел, которые не присутствуют в обоих множествах
def find_not_in_both_sets(set1, set2):
    result = list(set1 ^ set2)  # Симметрическая разница
    if not result:
        return None
    return result


# 376. Функция для нахождения чисел, которые являются разницей между тремя множествами
def find_difference_between_three_sets(set1, set2, set3):
    result = list(set1 - set2 - set3)
    if not result:
        return None
    return result


# 377. Функция для нахождения чисел, которые делятся на 2, но не на 3, и присутствуют в двух множествах
def find_divisible_by_2_not_3_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 2 == 0 and num % 3 != 0})
    if not result:
        return None
    return result


# 378. Функция для нахождения чисел, которые присутствуют в обоих множествах и не делятся на 4
def find_common_not_divisible_by_4(set1, set2):
    result = list((set1 & set2) - {num for num in range(1, 101) if num % 4 == 0})
    if not result:
        return None
    return result


# 379. Функция для нахождения чисел, которые присутствуют только в одном из двух множеств
def find_unique_in_sets(set1, set2):
    result = list(set1 ^ set2)  # Симметрическая разница
    if not result:
        return None
    return result


# 380. Функция для нахождения чисел, которые являются общими для всех трёх множеств
def find_common_in_all_sets(set1, set2, set3):
    result = list(set1 & set2 & set3)
    if not result:
        return None
    return result
