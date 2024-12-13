# 1161. Функция для нахождения чисел, которые являются результатом возведения элементов списка в степень их индекса из другого списка, но с учётом остатка от деления на 5
def power_and_modulo(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result_value = lst1[i] ** lst2[i]
            result.append(result_value % 5)
    if not result:
        return None
    return result


# 1162. Функция для нахождения чисел, которые делятся на 6, но не на 9, и вычисление их произведения
def find_divisible_by_6_not_9_and_multiply(lst):
    result = []
    product = 1
    for num in lst:
        if num % 6 == 0 and num % 9 != 0:
            result.append(num)
            product *= num
    if not result:
        return None
    return product


# 1163. Функция для нахождения чисел, которые равны разности элементов одного списка и разности всех элементов другого списка
def diff_of_lists_and_total_diff(lst1, lst2):
    result = []
    diff_lst2 = sum(lst2) - sum(lst1)
    for num in lst1:
        result.append(num - diff_lst2)
    if not result:
        return None
    return result


# 1164. Функция для нахождения чисел, которые являются результатом умножения чисел одного списка на индексы второго, с учётом разности от их суммы
def multiply_by_index_and_diff(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for i, num in enumerate(lst1):
        if i < len(lst2):
            result.append((num * i) - sum_lst2)
    if not result:
        return None
    return result


# 1165. Функция для нахождения чисел, которые равны разности всех чисел из одного списка и индексов другого списка, умноженных на их квадраты
def diff_and_index_squared(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] - lst2[i]) * (i ** 2))
    if not result:
        return None
    return result


# 1166. Функция для нахождения чисел, которые равны разности между произведениями элементов из двух списков и их индексами
def diff_of_product_and_index(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] * lst2[i]) - i)
    if not result:
        return None
    return result


# 1167. Функция для нахождения чисел, которые равны разности элементов одного списка и их произведений с элементами другого списка
def diff_and_product_of_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a - (a * b))
    if not result:
        return None
    return result


# 1168. Функция для нахождения чисел, которые являются результатом произведения чисел первого списка на индексы второго списка, делённые на их сумму
def multiply_by_index_divided_by_sum(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for i in range(len(lst1)):
        if i < len(lst2) and sum_lst2 != 0:
            result.append((lst1[i] * lst2[i]) / sum_lst2)
    if not result:
        return None
    return result


# 1169. Функция для нахождения чисел, которые равны разности квадратов элементов одного списка и их индексов в другом списке
def diff_of_squares_and_indexes_v2(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] ** 2) - lst2[i])
    if not result:
        return None
    return result


# 1170. Функция для нахождения чисел, которые делятся на 7 и на 11, но не на 154
def find_divisible_by_7_and_11_not_154(lst):
    result = []
    for num in lst:
        if num % 7 == 0 and num % 11 == 0 and num % 154 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1171. Функция для нахождения чисел, которые равны разности всех чисел из одного списка и всех чисел из другого списка
def diff_of_all_lists_v2(lst1, lst2):
    result = []
    sum_lst1 = sum(lst1)
    sum_lst2 = sum(lst2)
    for num in lst1:
        result.append(num - (sum_lst1 - sum_lst2))
    if not result:
        return None
    return result


# 1172. Функция для нахождения чисел, которые равны произведению чисел одного списка и индексов другого, умноженных на их квадрат
def multiply_by_index_and_square(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] * lst2[i]) * (i ** 2))
    if not result:
        return None
    return result


# 1173. Функция для нахождения чисел, которые делятся на 5, но не на 10 и 15, и вычисление их произведения
def find_divisible_by_5_not_10_and_15_and_multiply(lst):
    result = []
    product = 1
    for num in lst:
        if num % 5 == 0 and num % 10 != 0 and num % 15 != 0:
            result.append(num)
            product *= num
    if not result:
        return None
    return product


# 1174. Функция для нахождения чисел, которые равны произведению всех чисел первого списка и суммы чисел второго, делённой на количество элементов второго списка
def multiply_by_sum_and_len_other_list(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    len_lst2 = len(lst2)
    for num in lst1:
        result.append(num * (sum_lst2 / len_lst2))
    if not result:
        return None
    return result


# 1175. Функция для нахождения чисел, которые являются результатом умножения чисел первого списка на индексы второго списка, но только если произведение больше 20
def multiply_by_index_if_greater_than_20(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            product = lst1[i] * lst2[i]
            if product > 20:
                result.append(product)
    if not result:
        return None
    return result


# 1176. Функция для нахождения чисел, которые равны произведению чисел одного списка и их квадратов, делённых на элементы другого
def multiply_by_square_divided(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] ** 2) * lst2[i])
    if not result:
        return None
    return result


# 1177. Функция для нахождения чисел, которые являются разностью всех чисел первого списка и суммы всех чисел второго, умноженной на их индексы
def diff_from_sum_multiplied_by_index(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for i, num in enumerate(lst1):
        result.append(num - (sum_lst2 * i))
    if not result:
        return None
    return result


# 1178. Функция для нахождения чисел, которые являются результатом деления элементов одного списка на индексы элементов другого списка, если индекс меньше 5
def divide_by_index_if_less_than_5(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2) and i < 5:
            result.append(lst1[i] / lst2[i])
    if not result:
        return None
    return result


# 1179. Функция для нахождения чисел, которые равны произведению чисел первого списка на разность всех чисел второго
def multiply_by_diff_of_other_list(lst1, lst2):
    result = []
    diff_lst2 = sum(lst2) - sum(lst1)
    for num in lst1:
        result.append(num * diff_lst2)
    if not result:
        return None
    return result


# 1180. Функция для нахождения чисел, которые делятся на 4, но не на 8, и вычисление их произведения
def find_divisible_by_4_not_8_and_multiply(lst):
    result = []
    product = 1
    for num in lst:
        if num % 4 == 0 and num % 8 != 0:
            result.append(num)
            product *= num
    if not result:
        return None
    return product
