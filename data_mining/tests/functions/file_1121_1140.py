# 1121. Функция для нахождения чисел, которые равны разности квадратов элементов первого списка и индексов элементов второго
def diff_of_squares_and_indexes(lst1, lst2):
    result = []
    for i, num in enumerate(lst2):
        if i < len(lst1):
            result.append((lst1[i] ** 2) - i)
    if not result:
        return None
    return result


# 1122. Функция для нахождения чисел, которые являются разностью всех чисел первого списка и произведений чисел второго списка
def diff_of_lists_and_products(lst1, lst2):
    result = []
    product_lst2 = 1
    for num in lst2:
        product_lst2 *= num
    for num in lst1:
        result.append(num - product_lst2)
    if not result:
        return None
    return result


# 1123. Функция для нахождения чисел, которые являются результатом возведения чисел одного списка в степень числа, которое является суммой элементов второго списка
def power_by_sum_of_other_list(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    if sum_lst2 < 0 or sum_lst2 > 10:  # Ограничиваем степень для предотвращения переполнения
        return None
    for num in lst1:
        result.append(num ** sum_lst2)
    if not result:
        return None
    return result


# 1124. Функция для нахождения чисел, которые являются разностью квадратов чисел из двух списков, но с добавлением их индексов
def diff_of_squares_with_index(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] ** 2 - lst2[i] ** 2) + i)
    if not result:
        return None
    return result


# 1125. Функция для нахождения чисел, которые равны произведению всех чисел в первом списке, делённого на элементы второго списка
def multiply_by_division_of_other_list(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2) and lst2[i] != 0:
            result.append(lst1[i] * (1 / lst2[i]))
    if not result:
        return None
    return result


# 1126. Функция для нахождения чисел, которые являются результатом возведения чисел из одного списка в степень их индексов в другом
def power_by_index_of_other_list(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append(lst1[i] ** lst2[i])
    if not result:
        return None
    return result


# 1127. Функция для нахождения чисел, которые делятся на 9, но не на 12
def find_divisible_by_9_not_12(lst):
    result = []
    for num in lst:
        if num % 9 == 0 and num % 12 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1128. Функция для нахождения чисел, которые равны разности между квадратом чисел первого списка и их индексов во втором списке
def diff_of_squares_and_indexes_from_other_list(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append(lst1[i] ** 2 - lst2[i])
    if not result:
        return None
    return result


# 1129. Функция для нахождения чисел, которые являются результатом деления чисел одного списка на индексы второго списка
def divide_by_index_of_other_list(lst1, lst2):
    result = []
    for i in range(len(lst2)):
        if i < len(lst1) and i != 0:
            result.append(lst1[i] / i)
    if not result:
        return None
    return result


# 1130. Функция для нахождения чисел, которые равны произведению чисел первого списка и индексов второго списка, но только если результат меньше 50
def multiply_by_index_if_less_than_50(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            product = lst1[i] * lst2[i]
            if product < 50:
                result.append(product)
    if not result:
        return None
    return result


# 1131. Функция для нахождения чисел, которые делятся на 6 и 9, но не на 12
def find_divisible_by_6_and_9_not_12(lst):
    result = []
    for num in lst:
        if num % 6 == 0 and num % 9 == 0 and num % 12 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1132. Функция для нахождения чисел, которые являются результатом разности квадратов чисел первого списка и суммы чисел второго
def diff_of_squares_and_sum_of_other_list(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for num in lst1:
        result.append(num ** 2 - sum_lst2)
    if not result:
        return None
    return result


# 1133. Функция для нахождения чисел, которые являются произведением чисел одного списка на элементы второго, делённого на их индексы
def multiply_by_divided_index(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2) and i != 0:
            result.append((lst1[i] * lst2[i]) / i)
    if not result:
        return None
    return result


# 1134. Функция для нахождения чисел, которые равны произведению всех чисел из первого списка и суммы чисел из второго
def multiply_by_sum_of_other_list_v2(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for num in lst1:
        result.append(num * sum_lst2)
    if not result:
        return None
    return result


# 1135. Функция для нахождения чисел, которые равны разности элементов одного списка от произведений элементов другого
def subtract_from_product_of_other_list_v2(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a - (a * b))
    if not result:
        return None
    return result


# 1136. Функция для нахождения чисел, которые равны разности между элементами одного списка и их произведением с индексами другого списка
def diff_and_multiply_by_index(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] - lst2[i]) * i)
    if not result:
        return None
    return result


# 1137. Функция для нахождения чисел, которые являются результатом деления всех чисел из одного списка на их индексы
def divide_by_index_of_list(lst):
    result = []
    for i in range(len(lst)):
        if i != 0:
            result.append(lst[i] / i)
    if not result:
        return None
    return result


# 1138. Функция для нахождения чисел, которые равны разности всех чисел из одного списка, умноженных на элементы второго списка
def diff_of_lists_and_multiplied_by_other_list(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] - lst2[i]) * lst2[i])
    if not result:
        return None
    return result


# 1139. Функция для нахождения чисел, которые являются разностью квадратов чисел одного списка и суммы чисел из другого
def diff_of_squares_and_sum_v2(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for num in lst1:
        result.append((num ** 2) - sum_lst2)
    if not result:
        return None
    return result


# 1140. Функция для нахождения чисел, которые являются разностью произведений элементов одного списка и их квадратов
def diff_of_product_and_square(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append((a * b) - (a ** 2))
    if not result:
        return None
    return result
