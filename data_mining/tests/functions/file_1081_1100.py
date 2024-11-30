# 1081. Функция для нахождения чисел, которые делятся на 3, но не делятся на 6
def find_divisible_by_3_not_6(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 6 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1082. Функция для нахождения чисел, которые присутствуют в одном из двух списков, но не в обоих, с использованием множеств
def find_unique_elements_in_sets_3(lst1, lst2):
    result = list(set(lst1) ^ set(lst2))
    if not result:
        return None
    return result


# 1083. Функция для нахождения чисел, которые являются суммой всех чисел в списке, умноженных на их индексы
def sum_elements_times_index(lst):
    result = []
    for i, num in enumerate(lst):
        result.append(num * i)
    if not result:
        return None
    return result


# 1084. Функция для нахождения чисел, которые представляют собой разность элементов одного списка, умноженных на элементы другого списка
def diff_of_multiplied_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append((a * b) - a)
    if not result:
        return None
    return result


# 1085. Функция для нахождения чисел, которые встречаются в одном из двух списков, но не в обоих, и вычисление их суммы
def find_unique_in_both_lists_and_sum(lst1, lst2):
    result = []
    total_sum = 0
    for num in lst1:
        if num not in lst2:
            result.append(num)
            total_sum += num
    for num in lst2:
        if num not in lst1:
            result.append(num)
            total_sum += num
    if not result:
        return None
    return total_sum


# 1086. Функция для нахождения чисел, которые равны произведению всех элементов одного списка и разности элементов другого списка
def multiply_by_difference_of_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append((a * b) - (b - a))
    if not result:
        return None
    return result


# 1087. Функция для нахождения чисел, которые равны разности всех элементов одного списка и их квадратичных значений
def find_difference_of_elements_and_squares(lst):
    result = []
    for num in lst:
        result.append(num - num**2)
    if not result:
        return None
    return result


# 1088. Функция для нахождения чисел, которые присутствуют в обоих списках, но только если они делятся на 5
def find_common_and_divisible_by_5(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2 and num % 5 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 1089. Функция для нахождения чисел, которые меньше всех элементов из другого списка, но больше 10
def find_less_than_all_and_gt_10(lst1, lst2):
    result = []
    for num in lst1:
        if all(num < x for x in lst2) and num > 10:
            result.append(num)
    if not result:
        return None
    return result


# 1090. Функция для нахождения чисел, которые делятся на 2 и на 4, но не на 8
def find_divisible_by_2_and_4_not_8(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 4 == 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1091. Функция для нахождения чисел, которые равны разности между квадратом и кубом числа
def find_diff_between_square_and_cube(lst):
    result = []
    for num in lst:
        result.append(num**2 - num**3)
    if not result:
        return None
    return result


# 1092. Функция для нахождения чисел, которые являются результатом возведения каждого числа в степень его индекса в списке
def power_elements_by_index(lst):
    result = []
    for i, num in enumerate(lst):
        result.append(num ** i)
    if not result:
        return None
    return result


# 1093. Функция для нахождения чисел, которые равны разности квадратов двух элементов из двух списков
def subtract_squares_of_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a**2 - b**2)
    if not result:
        return None
    return result


# 1094. Функция для нахождения чисел, которые являются результатом разности всех элементов одного списка, деленных на элементы другого
def subtract_divided_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:
            result.append(a - (a / b))
    if not result:
        return None
    return result


# 1095. Функция для нахождения чисел, которые представляют собой сумму всех чисел из одного списка, умноженных на их индексы
def sum_elements_times_index_v2(lst):
    result = []
    for i, num in enumerate(lst):
        result.append(num * (i + 1))
    if not result:
        return None
    return result


# 1096. Функция для нахождения чисел, которые делятся на 6 и на 8
def find_divisible_by_6_and_8(lst):
    result = []
    for num in lst:
        if num % 6 == 0 and num % 8 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 1097. Функция для нахождения чисел, которые представляют собой разницу всех чисел в списке и их факториалов
def find_diff_and_factorials(lst):
    result = []
    for num in lst:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        result.append(num - fact)
    if not result:
        return None
    return result


# 1098. Функция для нахождения чисел, которые являются результатом умножения чисел одного списка на элементы другого, но только если результат меньше 100
def multiply_lists_if_less_than_100(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        product = a * b
        if product < 100:
            result.append(product)
    if not result:
        return None
    return result


# 1099. Функция для нахождения чисел, которые равны результату возведения элементов списка в степень их индекса
def find_powers_by_index(lst):
    result = []
    for i, num in enumerate(lst):
        result.append(num ** (i + 1))
    if not result:
        return None
    return result


# 1100. Функция для нахождения чисел, которые равны разности всех чисел из двух списков, умноженных на индексы
def subtract_lists_with_index(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] - lst2[i]) * i)
        else:
            result.append(lst1[i] * i)
    if not result:
        return None
    return result
