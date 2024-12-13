# 1141. Функция для нахождения чисел, которые делятся на 4 и на 7, но не на 18
def find_divisible_by_4_and_7_not_18(lst):
    result = []
    for num in lst:
        if num % 4 == 0 and num % 7 == 0 and num % 18 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1142. Функция для нахождения чисел, которые являются результатом суммы всех элементов первого списка и разности элементов второго
def sum_and_diff_of_lists_v2(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a + b - 2*a)
    if not result:
        return None
    return result


# 1143. Функция для нахождения чисел, которые являются произведением всех чисел из одного списка, умноженных на сумму чисел из другого
def multiply_all_and_sum_other_list(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for num in lst1:
        result.append(num * sum_lst2)
    if not result:
        return None
    return result


# 1144. Функция для нахождения чисел, которые являются результатом разности чисел одного списка и суммы элементов другого
def diff_of_lists_and_sum_other_list(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for num in lst1:
        result.append(num - sum_lst2)
    if not result:
        return None
    return result


# 1145. Функция для нахождения чисел, которые равны разности квадратов чисел одного списка и их деления на элементы второго
def diff_of_squares_and_division_by_other_list(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2) and lst2[i] != 0:
            result.append((lst1[i] ** 2) / lst2[i])
    if not result:
        return None
    return result


# 1146. Функция для нахождения чисел, которые являются результатом произведения всех элементов списка и разности элементов другого
def multiply_by_diff_of_lists(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append(lst1[i] * (lst1[i] - lst2[i]))
    if not result:
        return None
    return result


# 1147. Функция для нахождения чисел, которые делятся на 5, но не на 10 и 15
def find_divisible_by_5_not_10_and_15(lst):
    result = []
    for num in lst:
        if num % 5 == 0 and num % 10 != 0 and num % 15 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1148. Функция для нахождения чисел, которые равны разности всех чисел в первом списке и разности всех чисел во втором
def diff_of_all_lists(lst1, lst2):
    result = []
    diff_lst2 = sum(lst2) - sum(lst1)
    for num in lst1:
        result.append(num - diff_lst2)
    if not result:
        return None
    return result


# 1149. Функция для нахождения чисел, которые являются результатом разности произведений элементов двух списков
def diff_of_products(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append((a * b) - (a * 2 * b))
    if not result:
        return None
    return result


# 1150. Функция для нахождения чисел, которые являются суммой элементов первого списка и разностью элементов второго, но только если разность положительна
def sum_and_positive_diff(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        diff = a - b
        if diff > 0:
            result.append(a + diff)
    if not result:
        return None
    return result


# 1151. Функция для нахождения чисел, которые являются результатом умножения чисел первого списка на индексы второго списка, с учётом остатка от деления на 3
def multiply_by_index_with_remainder(lst1, lst2):
    result = []
    for i, num in enumerate(lst1):
        if i < len(lst2):
            product = num * lst2[i]
            result.append(product % 3)
    if not result:
        return None
    return result


# 1152. Функция для нахождения чисел, которые равны разности квадрата элементов первого списка и разности квадратов элементов второго
def diff_of_squares_of_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append((a ** 2) - (b ** 2))
    if not result:
        return None
    return result


# 1153. Функция для нахождения чисел, которые являются произведением чисел из одного списка, делённых на элементы другого, но только если результат больше 10
def multiply_and_divide_by_condition(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:
            result_value = (a * b) / b
            if result_value > 10:
                result.append(result_value)
    if not result:
        return None
    return result


# 1154. Функция для нахождения чисел, которые являются разностью всех чисел одного списка и произведений всех чисел из другого
def diff_from_product_of_other_list(lst1, lst2):
    result = []
    product_lst2 = 1
    for num in lst2:
        product_lst2 *= num
    for num in lst1:
        result.append(num - product_lst2)
    if not result:
        return None
    return result


# 1155. Функция для нахождения чисел, которые являются результатом возведения чисел первого списка в степень их индексов в другом списке, с условием, что степень больше 1
def power_by_index_with_condition(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2) and lst2[i] > 1:
            result.append(lst1[i] ** lst2[i])
    if not result:
        return None
    return result


# 1156. Функция для нахождения чисел, которые равны разности всех чисел одного списка и суммы всех элементов другого списка, умноженных на их индексы
def diff_and_sum_multiplied_by_indexes(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for i, num in enumerate(lst1):
        result.append(num - (sum_lst2 * i))
    if not result:
        return None
    return result


# 1157. Функция для нахождения чисел, которые являются результатом деления каждого числа первого списка на индекс соответствующего числа из второго списка, если индекс больше 2
def divide_by_index_if_greater_than_2(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if len(lst2) > i > 2:
            result.append(lst1[i] / lst2[i])
    if not result:
        return None
    return result


# 1158. Функция для нахождения чисел, которые делятся на 8, но не на 16, и вычисление их суммы
def find_divisible_by_8_not_16_and_sum(lst):
    result = []
    total_sum = 0
    for num in lst:
        if num % 8 == 0 and num % 16 != 0:
            result.append(num)
            total_sum += num
    if not result:
        return None
    return total_sum


# 1159. Функция для нахождения чисел, которые являются результатом возведения элементов одного списка в степень их индексов из другого, с условием, что результат меньше 100
def power_with_index_condition(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result_value = lst1[i] ** lst2[i]
            if result_value < 100:
                result.append(result_value)
    if not result:
        return None
    return result


# 1160. Функция для нахождения чисел, которые равны разности произведений всех чисел в одном списке и их квадратов
def diff_of_product_and_squares(lst1, lst2):
    result = []
    product_lst1 = 1
    for num in lst1:
        product_lst1 *= num
    for num in lst2:
        result.append(product_lst1 - (num ** 2))
    if not result:
        return None
    return result
