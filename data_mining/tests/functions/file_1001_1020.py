# 1001. Функция для нахождения всех чисел в списке, которые встречаются и в множестве, и в словаре
def find_numbers_in_both_set_and_dict(lst, s, d):
    if not lst or not s or not d:
        return None
    result = []
    for item in lst:
        if item in s and item in d.values():
            result.append(item)
    return tuple(result) if result else None


# 1002. Функция для создания списка всех чисел, которые больше минимального в словаре и меньше максимального в множестве
def create_list_between_min_in_dict_and_max_in_set(d, s):
    if not d or not s:
        return None
    min_dict = min(d.values())
    max_set = max(s)
    result = []
    for value in sorted(d.values()):
        if min_dict < value < max_set:
            result.append(value)
    return result if result else None


# 1003. Функция для нахождения чисел, которые присутствуют в кортеже, но отсутствуют в множестве и словаре
def find_in_tuple_not_in_set_and_dict(t, s, d):
    if not t or not s or not d:
        return None
    result = []
    for item in t:
        if item not in s and item not in d:
            result.append(item)
    return tuple(result) if result else None


# 1004. Функция для нахождения всех чисел, которые больше заданного в списке, но меньше в словаре
def find_floats_between_list_and_dict(lst, d):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if isinstance(item, float):
            if min(lst) < item < max(d.values()):
                result.append(item)
    return tuple(result) if result else None


# 1005. Функция для нахождения всех чисел в списке, которые больше максимума в словаре
def find_floats_greater_than_max_in_dict(lst, d):
    if not lst or not d:
        return None
    max_dict = max(d.values())
    result = []
    for item in lst:
        if isinstance(item, float) and item > max_dict:
            result.append(item)
    return tuple(result) if result else None


# 1006. Функция для подсчёта количества чисел, которые меньше заданного значения в списке и словаре
def count_floats_less_than_value_in_list_and_dict(lst, d, value):
    if not lst or not d:
        return None
    count = 0
    for item in lst:
        if isinstance(item, float) and item < value:
            count += 1
    for val in d.values():
        if isinstance(val, float) and val < value:
            count += 1
    return count if count > 0 else None


# 1007. Функция для нахождения чисел в списке, которые меньше максимального значения в другом списке
def find_floats_less_than_max_in_other_list(lst1, lst2):
    if not lst1 or not lst2:
        return None
    max_lst2 = max(lst2)
    result = []
    for item in lst1:
        if isinstance(item, float) and item < max_lst2:
            result.append(item)
    return tuple(result) if result else None


# 1008. Функция для нахождения чисел, которые меньше всех значений в словаре и больше всех значений в списке
def find_floats_between_max_in_list_and_min_in_dict(lst, d):
    if not lst or not d:
        return None
    min_dict = min(d.values())
    max_lst = max(lst)
    result = []
    for item in lst:
        if isinstance(item, float) and min_dict < item < max_lst:
            result.append(item)
    return tuple(result) if result else None


# 1009. Функция для нахождения чисел в списке, которые равны или меньше значений в множестве
def find_floats_less_than_or_equal_to_set_values(lst, s):
    if not lst or not s:
        return None
    result = []
    for item in lst:
        if isinstance(item, float) and any(item <= elem for elem in s):
            result.append(item)
    return tuple(sorted(result)) if result else None


# 1010. Функция для нахождения всех чисел в словаре, которые меньше заданного значения
def find_floats_less_than_value_in_dict(d, value):
    if not d:
        return None
    result = []
    for item in d.values():
        if isinstance(item, float) and item < value:
            result.append(item)
    return tuple(result) if result else None


# 1011. Функция для нахождения чисел, которые одновременно больше максимума в одном списке и меньше минимума в другом списке
def find_floats_between_max_in_first_list_and_min_in_second_list(lst1, lst2):
    if not lst1 or not lst2:
        return None
    max_lst2 = max(lst2)
    min_lst2 = min(lst2)
    result = []
    for item in lst1:
        if isinstance(item, float) and min_lst2 < item < max_lst2:
            result.append(item)
    return tuple(result) if result else None


# 1012. Функция для нахождения чисел, которые меньше или равны максимальному значению в списке
def find_floats_less_than_or_equal_to_max_in_list(lst):
    if not lst:
        return None
    max_lst = max(lst)
    result = []
    for item in lst:
        if isinstance(item, float) and item <= max_lst:
            result.append(item)
    return tuple(result) if result else None


# 1013. Функция для нахождения чисел, которые больше минимального значения в списке, но меньше максимального в словаре
def find_floats_between_min_in_list_and_max_in_dict(lst, d):
    if not lst or not d:
        return None
    min_lst = min(lst)
    max_dict = max(d.values())
    result = []
    for item in lst:
        if isinstance(item, float) and min_lst < item < max_dict:
            result.append(item)
    return tuple(result) if result else None


# 1014. Функция для создания множества, содержащего все числа, которые больше минимального в словаре и меньше максимального в списке
def create_set_between_min_in_dict_and_max_in_list(d, lst):
    if not d or not lst:
        return None
    min_dict = min(d.values())
    max_lst = max(lst)
    result = set()
    for value in sorted(d.values()):
        if isinstance(value, float) and min_dict < value < max_lst:
            result.add(value)
    return result if result else None


# 1015. Функция для нахождения всех чисел в списке, которые делятся на заданное число
def find_floats_divisible_by_value_in_list(lst, value):
    if not lst:
        return None
    result = []
    for item in lst:
        if isinstance(item, float) and item % value == 0:
            result.append(item)
    return tuple(result) if result else None


# 1016. Функция для нахождения чисел, которые меньше заданного значения в списке и больше в словаре
def find_floats_between_value_in_list_and_value_in_dict(lst, d, value):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if isinstance(item, float) and item < value and any(val > value for val in d.values()):
            result.append(item)
    return tuple(result) if result else None


# 1017. Функция для подсчёта чисел в списке, которые больше средней величины всех чисел в словаре
def count_floats_greater_than_avg_in_dict(lst, d):
    if not lst or not d:
        return None
    avg_dict = sum(d.values()) / len(d)
    count = 0
    for item in lst:
        if isinstance(item, float) and item > avg_dict:
            count += 1
    return count if count > 0 else None


# 1018. Функция для нахождения всех чисел в списке, которые делятся на два заданных числа
def find_floats_divisible_by_two_values(lst, value1, value2):
    if not lst:
        return None
    result = []
    for item in lst:
        if isinstance(item, float) and item % value1 == 0 and item % value2 == 0:
            result.append(item)
    return tuple(result) if result else None


# 1019. Функция для создания множества чисел, которые больше заданного в списке
def create_set_of_floats_greater_than_value_in_list(lst, value):
    if not lst:
        return None
    result = set()
    for item in lst:
        if isinstance(item, float) and item > value:
            result.add(item)
    return sorted(result) if result else None


# 1020. Функция для нахождения чисел в списке, которые меньше среднего значения в другом списке
def find_floats_less_than_avg_in_other_list(lst1, lst2):
    if not lst1 or not lst2:
        return None
    avg_lst2 = sum(lst2) / len(lst2)
    result = []
    for item in lst1:
        if isinstance(item, float) and item < avg_lst2:
            result.append(item)
    return tuple(result) if result else None
