# 1101. Функция для нахождения чисел, которые являются суммой всех чисел в одном списке, делённых на числа из другого
def sum_divided_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:
            result.append(a / b)
    if not result:
        return None
    return result


# 1102. Функция для нахождения чисел, которые равны разности квадратов элементов одного списка и квадратов элементов другого
def diff_of_squares(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a**2 - b**2)
    if not result:
        return None
    return result


# 1103. Функция для нахождения чисел, которые делятся на 7, но не делятся на 14 и 21
def find_divisible_by_7_not_14_or_21(lst):
    result = []
    for num in lst:
        if num % 7 == 0 and num % 14 != 0 and num % 21 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1104. Функция для нахождения чисел, которые являются суммой чисел из одного списка и разности чисел другого списка
def sum_and_diff_of_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append((a + b) - (b - a))
    if not result:
        return None
    return result


# 1105. Функция для нахождения чисел, которые являются результатом умножения чисел из одного списка на чисел другого, но только если произведение больше 50
def multiply_lists_if_greater_than_50(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        product = a * b
        if product > 50:
            result.append(product)
    if not result:
        return None
    return result


# 1106. Функция для нахождения чисел, которые делятся на 8, но не делятся на 4
def find_divisible_by_8_not_4(lst):
    result = []
    for num in lst:
        if num % 8 == 0 and num % 4 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1107. Функция для нахождения чисел, которые равны разнице квадратов всех чисел из первого списка и всех чисел из второго
def diff_of_all_squares(lst1, lst2):
    result = []
    sum_sq_lst1 = sum([num ** 2 for num in lst1])
    sum_sq_lst2 = sum([num ** 2 for num in lst2])
    result.append(sum_sq_lst1 - sum_sq_lst2)
    if not result:
        return None
    return result


# 1108. Функция для нахождения чисел, которые присутствуют в обоих списках, но только если их сумма больше 20
def find_common_and_sum_gt_20(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2 and (num + num > 20):
            result.append(num)
    if not result:
        return None
    return result


# 1109. Функция для нахождения чисел, которые являются результатом деления чисел из одного списка на числа из другого, с учётом остатка
def divide_with_remainder(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:
            result.append(a % b)
    if not result:
        return None
    return result


# 1110. Функция для нахождения чисел, которые равны произведению чисел из первого списка и чисел второго, если результат больше 100
def multiply_if_greater_than_100(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        product = a * b
        if product > 100:
            result.append(product)
    if not result:
        return None
    return result


# 1111. Функция для нахождения чисел, которые являются разностью элементов из одного списка и индексов элементов другого списка
def subtract_by_index(lst1, lst2):
    result = []
    for i, num in enumerate(lst1):
        if i < len(lst2):
            result.append(num - lst2[i])
    if not result:
        return None
    return result


# 1112. Функция для нахождения чисел, которые являются результатом возведения элементов одного списка в степень их индекса
def power_by_index(lst):
    result = []
    for i, num in enumerate(lst):
        result.append(num ** (i + 1))
    if not result:
        return None
    return result


# 1113. Функция для нахождения чисел, которые являются результатом разности чисел одного списка и элементов другого, делённых на их индексы
def diff_divided_by_index(lst1, lst2):
    result = []
    for i, (a, b) in enumerate(zip(lst1, lst2)):
        if i != 0:
            result.append((a - b) / i)
    if not result:
        return None
    return result


# 1114. Функция для нахождения чисел, которые равны произведению всех элементов списка, делённых на количество элементов другого списка
def multiply_by_len_of_other_list(lst1, lst2):
    result = []
    len_lst2 = len(lst2)
    for num in lst1:
        result.append(num * len_lst2)
    if not result:
        return None
    return result


# 1115. Функция для нахождения чисел, которые являются суммой элементов двух списков и их произведений
def sum_and_multiply_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a + b + (a * b))
    if not result:
        return None
    return result


# 1116. Функция для нахождения чисел, которые равны сумме чисел одного списка и произведению элементов другого
def sum_and_product_of_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append((a + b) * (a * b))
    if not result:
        return None
    return result


# 1117. Функция для нахождения чисел, которые делятся на 4, но не на 8 и 16
def find_divisible_by_4_not_8_or_16(lst):
    result = []
    for num in lst:
        if num % 4 == 0 and num % 8 != 0 and num % 16 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1118. Функция для нахождения чисел, которые представляют собой разницу чисел одного списка и индексов чисел другого
def subtract_by_other_list_index(lst1, lst2):
    result = []
    for i, num in enumerate(lst2):
        if i < len(lst1):
            result.append(lst1[i] - num)
    if not result:
        return None
    return result


# 1119. Функция для нахождения чисел, которые являются результатом деления чисел одного списка на индексы элементов другого списка
def divide_by_index(lst1, lst2):
    result = []
    for i, num in enumerate(lst2):
        if i != 0:
            result.append(lst1[i] / i)
    if not result:
        return None
    return result


# 1120. Функция для нахождения чисел, которые являются разностью чисел одного списка, умноженных на индексы другого списка
def diff_multiplied_by_index(lst1, lst2):
    result = []
    for i, num in enumerate(lst2):
        if i < len(lst1):
            result.append((lst1[i] - num) * i)
    if not result:
        return None
    return result
