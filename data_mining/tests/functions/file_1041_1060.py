# 1041. Функция для нахождения чисел, которые являются квадратными корнями элементов списка
def find_square_roots(lst):
    result = []
    for num in lst:
        if num >= 0:
            result.append(num ** 0.5)
    if not result:
        return None
    return result


# 1042. Функция для нахождения чисел, которые встречаются в одном списке, но не в другом
def find_unique_in_first_list(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    if not result:
        return None
    return result


# 1043. Функция для нахождения чисел, которые делятся на 10 или 12
def find_divisible_by_10_or_12(lst):
    result = []
    for num in lst:
        if num % 10 == 0 or num % 12 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 1044. Функция для нахождения чисел, которые делятся на 11, но не на 22
def find_divisible_by_11_not_22(lst):
    result = []
    for num in lst:
        if num % 11 == 0 and num % 22 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1045. Функция для нахождения чисел, которые являются факториалами элементов списка
def find_factorials(lst):
    result = []
    for num in lst:
        if num == 0:
            result.append(1)
        else:
            fact = 1
            for i in range(1, num + 1):
                fact *= i
            result.append(fact)
    if not result:
        return None
    return result


# 1046. Функция для нахождения чисел, которые являются разностью между максимальным и минимальным значением в списке
def find_diff_between_max_and_min(lst):
    result = []
    max_val = max(lst)
    min_val = min(lst)
    result.append(max_val - min_val)
    if not result:
        return None
    return result


# 1047. Функция для нахождения чисел, которые являются разностью квадратов элементов двух списков
def subtract_squares_of_lists_v2(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a**2 - b**2)
    if not result:
        return None
    return result


# 1048. Функция для нахождения чисел, которые являются произведением всех чисел из списка и заданной константы
def multiply_list_by_constant_v2(lst, constant):
    result = []
    for num in lst:
        result.append(num * constant)
    if not result:
        return None
    return result


# 1049. Функция для нахождения чисел, которые являются результатом деления всех элементов списка на заданную константу
def divide_list_by_constant(lst, constant):
    result = []
    if constant == 0:
        return None
    for num in lst:
        result.append(num / constant)
    if not result:
        return None
    return result


# 1050. Функция для нахождения чисел, которые делятся на 4 или 8, но не на 12
def find_divisible_by_4_or_8_not_12(lst):
    result = []
    for num in lst:
        if (num % 4 == 0 or num % 8 == 0) and num % 12 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1051. Функция для нахождения чисел, которые являются суммой элементов двух списков с проверкой условия
def add_lists_with_condition(lst1, lst2, condition):
    result = []
    for a, b in zip(lst1, lst2):
        if a + b > condition:
            result.append(a + b)
    if not result:
        return None
    return result


# 1052. Функция для нахождения чисел, которые являются разницей между максимальным и минимальным элементом в двух списках
def find_max_min_diff_in_lists(lst1, lst2):
    result = []
    max_val1 = max(lst1)
    min_val1 = min(lst1)
    max_val2 = max(lst2)
    min_val2 = min(lst2)
    result.append(max_val1 - min_val1)
    result.append(max_val2 - min_val2)
    if not result:
        return None
    return result


# 1053. Функция для нахождения чисел, которые делятся на 3 и на 7
def find_divisible_by_3_and_7(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 7 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 1054. Функция для нахождения чисел, которые делятся на 15, но не на 30
def find_divisible_by_15_not_30(lst):
    result = []
    for num in lst:
        if num % 15 == 0 and num % 30 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1055. Функция для нахождения чисел, которые равны разности между элементами двух списков
def subtract_lists_elements(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a - b)
    if not result:
        return None
    return result


# 1056. Функция для нахождения чисел, которые делятся на 2 и на 3, но не на 6
def find_divisible_by_2_and_3_not_6(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 == 0 and num % 6 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1057. Функция для нахождения чисел, которые являются квадратами элементов одного списка
def find_squares_of_elements(lst):
    result = []
    for num in lst:
        result.append(num**2)
    if not result:
        return None
    return result


# 1058. Функция для нахождения чисел, которые являются произведением элементов двух списков, но только тех, которые четные
def multiply_even_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if a % 2 == 0 and b % 2 == 0:
            result.append(a * b)
    if not result:
        return None
    return result


# 1059. Функция для нахождения чисел, которые делятся на 10, но не на 5
def find_divisible_by_10_not_5(lst):
    result = []
    for num in lst:
        if num % 10 == 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1060. Функция для нахождения чисел, которые равны произведению всех чисел другого списка
def find_product_of_elements_of_other_list(lst1, lst2):
    result = []
    product = 1
    for num in lst2:
        product *= num
    for num in lst1:
        if num == product:
            result.append(num)
    if not result:
        return None
    return result
