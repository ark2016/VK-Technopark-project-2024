# 481. Функция для нахождения всех чисел, которые больше X, и делятся на 3
def find_greater_than_x_divisible_by_3(tpl, x):
    result = []
    for elem in tpl:
        if elem > x and elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 482. Функция для нахождения чисел, которые не делятся на 4 и на 5
def find_not_divisible_by_4_and_5(tpl):
    result = []
    for elem in tpl:
        if elem % 4 != 0 and elem % 5 != 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 483. Функция для нахождения чисел, которые меньше X, но делятся на 3
def find_less_than_x_divisible_by_3(tpl, x):
    result = []
    for elem in tpl:
        if elem < x and elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 484. Функция для нахождения чисел, которые делятся на 2 и на 5
def find_divisible_by_2_and_5(tpl):
    result = []
    for elem in tpl:
        if elem % 2 == 0 and elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 485. Функция для нахождения чисел, которые не являются квадратами целых чисел
def find_not_square_numbers_in_tuple(tpl):
    result = []
    for elem in tpl:
        if not (elem ** 0.5).is_integer():
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 486. Функция для нахождения чисел, которые делятся на 2 и на 7
def find_divisible_by_2_and_7(tpl):
    result = []
    for elem in tpl:
        if elem % 2 == 0 and elem % 7 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 487. Функция для нахождения чисел, которые меньше X и являются нечётными
def find_less_than_x_odd(tpl, x):
    result = []
    for elem in tpl:
        if elem < x and elem % 2 != 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 488. Функция для нахождения всех чисел, которые больше X и являются чётными
def find_greater_than_x_even(tpl, x):
    result = []
    for elem in tpl:
        if elem > x and elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 489. Функция для получения уникальных элементов из списка с помощью множества
def unique_elements_from_list(lst):
    if not lst:
        return None
    unique_elements = set(lst)
    return tuple(unique_elements)


# 490. Функция для нахождения пересечения двух списков
def intersection_of_lists_2(lst1, lst2):
    result = list(set(lst1) & set(lst2))
    if not result:
        return None
    return result


# 491. Функция для объединения двух словарей, если они не содержат одинаковых ключей
def merge_dicts_no_common_keys(d1, d2):
    if any(k in d2 for k in d1):
        return None
    merged_dict = {**d1, **d2}
    return merged_dict


# 492. Функция для переворота строки
def reverse_string_3(s):
    if not s:
        return None
    return s[::-1]


# 493. Функция для нахождения всех чисел, которые являются делителями числа X
def divisors_of_x(x):
    if x <= 0:
        return None
    divisors = []
    for i in range(1, x + 1):
        if x % i == 0:
            divisors.append(i)
    if not divisors:
        return None
    return divisors


# 494. Функция для подсчёта количества вхождений каждого элемента в список
def count_elements_in_list(lst):
    if not lst:
        return None
    count_dict = {}
    for elem in lst:
        count_dict[elem] = count_dict.get(elem, 0) + 1
    return count_dict


# 495. Функция для создания словаря из списка пар (ключ, значение)
def list_to_dict_2(lst):
    if not lst or len(lst) % 2 != 0:
        return None
    return dict(zip(lst[::2], lst[1::2]))


# 496. Функция для подсчёта чётных и нечётных чисел в списке
def count_even_and_odd(lst):
    if not lst:
        return None
    even_count = 0
    odd_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return {"even": even_count, "odd": odd_count}


# 497. Функция для извлечения всех гласных из строки
def extract_vowels_from_string(s):
    if not s:
        return None
    vowels = "aeiouAEIOU"
    result = [ch for ch in s if ch in vowels]
    if not result:
        return None
    return ''.join(result)


# 498. Функция для слияния двух отсортированных списков в один отсортированный
def merge_sorted_lists(lst1, lst2):
    if not lst1 and not lst2:
        return None
    return sorted(lst1 + lst2)


# 499. Функция для проверки, является ли строка палиндромом
def is_palindrome_2(s):
    if not s:
        return None
    return s == s[::-1]


# 500. Функция для нахождения наибольшего общего делителя двух чисел
def gcd_of_two_numbers(a, b):
    if a <= 0 or b <= 0:
        return None
    while b:
        a, b = b, a % b
    return a
