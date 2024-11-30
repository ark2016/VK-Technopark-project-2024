# 281. Функция для нахождения чисел, которые присутствуют в обоих списках
def find_in_both_lists(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2:
            result.append(num)
    if not result:
        return None
    return result


# 282. Функция для нахождения чисел, которые не присутствуют в одном из списков
def find_not_in_list(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    if not result:
        return None
    return result


# 283. Функция для нахождения чисел, которые являются произведением двух чисел, но не делятся на 7
def find_product_not_divisible_by_7(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            product = lst[i] * lst[j]
            if product % 7 != 0:
                result.append(product)
    if not result:
        return None
    return result


# 284. Функция для нахождения чисел, которые являются произведением двух нечётных чисел
def find_product_of_two_odds(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] % 2 != 0 and lst[j] % 2 != 0:
                result.append(lst[i] * lst[j])
    if not result:
        return None
    return result


# 285. Функция для нахождения чисел, которые являются суммой двух нечётных чисел
def find_sum_of_two_odds(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] % 2 != 0 and lst[j] % 2 != 0:
                result.append(lst[i] + lst[j])
    if not result:
        return None
    return result


# 286. Функция для нахождения чисел, которые являются четными и находятся в кортеже
def find_even_in_tuple(tpl):
    result = []
    for num in tpl:
        if num % 2 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 287. Функция для нахождения чисел, которые являются произведением двух чисел, но не на 5
def find_product_not_divisible_by_5(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            product = lst[i] * lst[j]
            if product % 5 != 0:
                result.append(product)
    if not result:
        return None
    return result


# 288. Функция для нахождения чисел, которые присутствуют в одном словаре, но не в другом
def find_keys_in_dict_not_in_other(dict1, dict2):
    result = []
    for key in dict1:
        if key not in dict2:
            result.append(key)
    if not result:
        return None
    return result


# 289. Функция для нахождения чисел, которые являются разностью элементов в кортеже
def find_difference_in_tuple(tpl):
    result = []
    for i in range(len(tpl)):
        for j in range(i + 1, len(tpl)):
            result.append(abs(tpl[i] - tpl[j]))
    if not result:
        return None
    return result


# 290. Функция для нахождения чисел, которые являются результатом разности двух чисел из двух списков
def find_difference_between_lists_2(lst1, lst2):
    result = []
    for num1 in lst1:
        for num2 in lst2:
            result.append(abs(num1 - num2))
    if not result:
        return None
    return result


# 291. Функция для нахождения чисел, которые являются нечётными и присутствуют в одном из списков
def find_odd_in_one_list(lst1, lst2):
    result = []
    for num in lst1:
        if num % 2 != 0 and num not in lst2:
            result.append(num)
    for num in lst2:
        if num % 2 != 0 and num not in lst1:
            result.append(num)
    if not result:
        return None
    return result


# 292. Функция для нахождения чисел, которые являются результатом суммы двух чисел из одного списка
def find_sum_of_two_from_one_list(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            result.append(lst[i] + lst[j])
    if not result:
        return None
    return result


# 293. Функция для нахождения чисел, которые встречаются в обоих списках, но не в обоих списках сразу
def find_common_not_in_both_lists(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2:
            result.append(num)
    if not result:
        return None
    return result


# 294. Функция для нахождения чисел, которые являются результатом суммы элементов двух списков
def find_sum_of_elements_from_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a + b)
    if not result:
        return None
    return result


# 295. Функция для нахождения чисел, которые являются результатом разности элементов из двух списков
def find_difference_of_elements_from_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a - b)
    if not result:
        return None
    return result


# 296. Функция для преобразования чисел из списка в их квадраты
def square_numbers(lst):
    result = list(map(lambda x: x ** 2, lst))
    if not result:
        return None
    return result


# 297. Функция для нахождения чисел, которые делятся на 3, но не на 5
def find_divisible_by_3_not_5(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 298. Функция для нахождения чисел, которые присутствуют только в одном из двух списков
def find_unique_in_one_list_3(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if a != b:
            result.append(a)
            result.append(b)
    if not result:
        return None
    return result


# 299. Функция для нахождения чисел, которые присутствуют в списке, но не в кортеже
def find_in_list_not_in_tuple_2(lst, tpl):
    result = []
    for num in lst:
        if num not in tpl:
            result.append(num)
    if not result:
        return None
    return result


# 300. Функция для нахождения чисел, которые являются кубами чисел в списке
def find_cubes(lst):
    result = list(map(lambda x: x ** 3, lst))
    if not result:
        return None
    return result
