# 1061. Функция для нахождения чисел, которые являются делителями числа
def find_divisors_4(lst, num):
    result = []
    for i in lst:
        if num % i == 0:
            result.append(i)
    if not result:
        return None
    return result


# 1062. Функция для нахождения чисел, которые больше всех чисел в другом списке
def find_greater_than_all_in_other_list(lst1, lst2):
    result = []
    for num in lst1:
        if all(num > x for x in lst2):
            result.append(num)
    if not result:
        return None
    return result


# 1063. Функция для нахождения чисел, которые являются результатом умножения всех чисел в списке на 2
def multiply_list_by_2(lst):
    result = []
    for num in lst:
        result.append(num * 2)
    if not result:
        return None
    return result


# 1064. Функция для нахождения чисел, которые являются результатом возведения чисел в степень, заданную как аргумент
def find_powers_of_elements(lst, power):
    result = []
    for num in lst:
        result.append(num ** power)
    if not result:
        return None
    return result


# 1065. Функция для нахождения чисел, которые больше или равны всем элементам другого списка
def find_greater_or_equal_to_all(lst1, lst2):
    result = []
    for num in lst1:
        if all(num >= x for x in lst2):
            result.append(num)
    if not result:
        return None
    return result


# 1066. Функция для нахождения чисел, которые являются разностью элементов из двух списков, с учетом определенного условия
def subtract_lists_with_condition(lst1, lst2, condition):
    result = []
    for a, b in zip(lst1, lst2):
        if a - b > condition:
            result.append(a - b)
    if not result:
        return None
    return result


# 1067. Функция для нахождения чисел, которые являются произведением элементов одного списка на элементы другого списка
def multiply_lists_elements(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a * b)
    if not result:
        return None
    return result


# 1068. Функция для нахождения чисел, которые являются делителями чисел из списка
def find_divisors_of_list_elements(lst):
    result = []
    for num in lst:
        for i in range(1, num + 1):
            if num % i == 0:
                result.append(i)
    if not result:
        return None
    return result


# 1069. Функция для нахождения чисел, которые больше или равны минимальному элементу в другом списке
def find_greater_than_or_equal_min(lst1, lst2):
    result = []
    min_val = min(lst2)
    for num in lst1:
        if num >= min_val:
            result.append(num)
    if not result:
        return None
    return result


# 1070. Функция для нахождения чисел, которые равны разнице двух элементов в одном списке
def find_difference_of_elements(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            result.append(lst[i] - lst[j])
    if not result:
        return None
    return result


# 1071. Функция для нахождения чисел, которые являются квадратными корнями элементов другого списка
def find_square_roots_of_list(lst):
    result = []
    for num in lst:
        result.append(num**0.5)
    if not result:
        return None
    return result

# 1072. Функция для нахождения чисел, которые являются разностью всех элементов двух списков по порядку
def subtract_lists_elementwise(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append(lst1[i] - lst2[i])
        else:
            result.append(lst1[i])
    if not result:
        return None
    return result


# 1073. Функция для нахождения чисел, которые встречаются в двух списках, но не одновременно в одном из них
def find_exclusive_in_both(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    for num in lst2:
        if num not in lst1:
            result.append(num)
    if not result:
        return None
    return result


# 1074. Функция для нахождения чисел, которые являются результатом суммы чисел двух списков, если сумма больше 10
def sum_lists_if_greater_than_10(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        summ = a + b
        if summ > 10:
            result.append(summ)
    if not result:
        return None
    return result


# 1075. Функция для нахождения чисел, которые являются результатом возведения элементов одного списка в степень элементов другого
def power_of_elements(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a ** b)
    if not result:
        return None
    return result


# 1076. Функция для нахождения чисел, которые являются результатом деления элементов одного списка на элементы другого, при этом исключая делители, равные нулю
def divide_lists_with_exclusion_of_zero(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:
            result.append(a / b)
    if not result:
        return None
    return result


# 1077. Функция для нахождения чисел, которые встречаются в двух списках и являются четными
def find_even_common(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2 and num % 2 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 1078. Функция для нахождения чисел, которые меньше суммы элементов второго списка
def find_less_than_sum_of_other_list(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for num in lst1:
        if num < sum_lst2:
            result.append(num)
    if not result:
        return None
    return result


# 1079. Функция для нахождения чисел, которые являются разностью элементов одного списка от их квадратов
def subtract_from_squares(lst):
    result = []
    for num in lst:
        result.append(num**2 - num)
    if not result:
        return None
    return result


# 1080. Функция для нахождения чисел, которые являются результатом умножения чисел одного списка на числа другого, но только если результат больше 20
def multiply_lists_if_greater_than_20(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        product = a * b
        if product > 20:
            result.append(product)
    if not result:
        return None
    return result
