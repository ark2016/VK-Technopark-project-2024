# 1021. Функция для нахождения чисел, которые больше минимального в одном списке и меньше максимального в другом списке
def find_floats_between_min_in_first_list_and_max_in_second_list(lst1, lst2):
    if not lst1 or not lst2:
        return None
    min_lst1 = min(lst1)
    max_lst2 = max(lst2)
    result = []
    for item in lst1:
        if isinstance(item, float) and min_lst1 < item < max_lst2:
            result.append(item)
    return tuple(result) if result else None


# 1022. Функция для нахождения чисел, которые меньше среднего значения всех чисел в словаре
def find_floats_less_than_avg_in_dict(lst, d):
    if not lst or not d:
        return None
    avg_dict = sum(d.values()) / len(d)
    result = []
    for item in lst:
        if isinstance(item, float) and item < avg_dict:
            result.append(item)
    return tuple(result) if result else None


# 1023. Функция для нахождения чисел, которые больше заданного значения, присутствующего в словаре
def find_floats_greater_than_value_in_dict(lst, d, value):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if isinstance(item, float) and any(val > value for val in d.values()):
            result.append(item)
    return tuple(result) if result else None


# 1024. Функция для нахождения чисел, которые больше максимального значения в одном списке и меньше максимального в другом
def find_floats_between_max_in_first_list_and_max_in_second_list(lst1, lst2):
    if not lst1 or not lst2:
        return None
    max_lst1 = max(lst1)
    max_lst2 = max(lst2)
    result = []
    for item in lst1:
        if isinstance(item, float) and max_lst1 < item < max_lst2:
            result.append(item)
    return tuple(result) if result else None


# 1025. Функция для нахождения чисел, которые являются суммой элементов из двух списков
def add_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a + b)
    if not result:
        return None
    return result


# 1026. Функция для нахождения чисел, которые являются результатом возведения элементов одного списка в квадрат
def square_list_2(lst):
    result = []
    for num in lst:
        result.append(num ** 2)
    if not result:
        return None
    return result


# 1027. Функция для нахождения чисел, которые делятся на 7, но не на 14
def find_divisible_by_7_not_14(lst):
    result = []
    for num in lst:
        if num % 7 == 0 and num % 14 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1028. Функция для нахождения чисел, которые встречаются в обоих списках
def find_common_in_lists_2(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2:
            result.append(num)
    if not result:
        return None
    return result


# 1029. Функция для нахождения чисел, которые являются произведением всех элементов списка
def multiply_list_elements(lst):
    result = 1
    for num in lst:
        result *= num
    if result == 1:
        return None
    return result


# 1030. Функция для нахождения чисел, которые являются разницей квадратов элементов из двух списков
def subtract_squares_of_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a**2 - b**2)
    if not result:
        return None
    return result


# 1031. Функция для нахождения чисел, которые делятся на 8, но не на 16
def find_divisible_by_8_not_16(lst):
    result = []
    for num in lst:
        if num % 8 == 0 and num % 16 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1032. Функция для нахождения чисел, которые представляют собой делители других чисел в списке
def find_divisors_in_list_2(lst):
    result = []
    for num in lst:
        for other in lst:
            if other != num and other % num == 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 1033. Функция для нахождения чисел, которые меньше всех элементов другого списка
def find_less_than_all_other(lst1, lst2):
    result = []
    for num in lst1:
        if all(num < x for x in lst2):
            result.append(num)
    if not result:
        return None
    return result


# 1034. Функция для нахождения чисел, которые делятся на 2 или 3
def find_divisible_by_2_or_3(lst):
    result = []
    for num in lst:
        if num % 2 == 0 or num % 3 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 1035. Функция для нахождения чисел, которые являются суммой элементов из одного списка и чисел из другого
def add_lists_elements_with_offset(lst1, lst2, offset):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a + b + offset)
    if not result:
        return None
    return result


# 1036. Функция для нахождения чисел, которые являются результатом умножения всех элементов списка на константу
def multiply_list_by_constant(lst, constant):
    result = []
    for num in lst:
        result.append(num * constant)
    if not result:
        return None
    return result


# 1037. Функция для нахождения чисел, которые не делятся на 3 и на 5
def find_not_divisible_by_3_and_5(lst):
    result = []
    for num in lst:
        if num % 3 != 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1038. Функция для нахождения чисел, которые представляют собой сумму элементов из двух списков с условием
def add_lists_conditionally(lst1, lst2, condition):
    result = []
    for a, b in zip(lst1, lst2):
        if a + b > condition:
            result.append(a + b)
    if not result:
        return None
    return result


# 1039. Функция для нахождения чисел, которые являются четными и больше 10
def find_even_and_greater_than_10(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num > 10:
            result.append(num)
    if not result:
        return None
    return result


# 1040. Функция для нахождения чисел, которые равны разности двух других элементов в списке
def find_difference_elements_in_list(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] - lst[j] == 0:
                result.append(lst[i])
    if not result:
        return None
    return result
