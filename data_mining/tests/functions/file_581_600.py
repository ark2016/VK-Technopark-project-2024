# 581. Функция для нахождения минимального числа в списке (рекурсия)
def recursive_min(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        sub_min = recursive_min(lst[1:])
        return lst[0] if lst[0] < sub_min else sub_min


# 582. Функция для инвертирования строки (рекурсия)
def reverse_string_2(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string_2(s[:-1])


# 583. Функция для проверки, является ли строка палиндромом (рекурсия)
def is_palindrome_4(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_4(s[1:-1])


# 584. Функция для нахождения НОД (наибольший общий делитель) двух чисел (рекурсия)
def gsd_2(a, b):
    if b == 0:
        return a
    return gsd_2(b, a % b)


# 585. Функция для подсчета количества вхождений элемента в списке (рекурсия)
def count_occurrences_3(lst, x):
    if not lst:
        return 0
    return (1 if lst[0] == x else 0) + count_occurrences_3(lst[1:], x)


# 586. Функция для проверки, является ли число простым (рекурсия)
def is_prime_4(n, divisor=None):
    if n <= 1:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime_4(n, divisor - 1)


# 587. Функция для нахождения наибольшего элемента в дереве (рекурсия)
def find_max_in_tree(tree):
    if tree is None:
        return float('-inf')
    left_max = find_max_in_tree(tree.get('left'))
    right_max = find_max_in_tree(tree.get('right'))
    return max(tree.get('value', float('-inf')), left_max, right_max)


# 588. Функция для проверки, является ли число четным (рекурсия)
def is_even_2(n):
    if n == 0:
        return True
    if n == 1:
        return False
    return is_even_2(n - 2)


# 589. Функция для вычисления суммы чисел, меньших X в списке (рекурсия)
def sum_less_than_x(lst, x):
    if not lst:
        return 0
    return (lst[0] if lst[0] < x else 0) + sum_less_than_x(lst[1:], x)


# 590. Функция для вычисления факториала числа с использованием хвоста (рекурсия с аккумулятором)
def factorial_tail(n, acc=1):
    if n == 0 or n == 1:
        return acc
    return factorial_tail(n - 1, acc * n)


# 591. Функция для вычисления суммы чисел в диапазоне от 1 до N, но с шагом 2 (рекурсия)
def sum_with_step(n):
    if n <= 0:
        return 0
    return n + sum_with_step(n - 2)


# 592. Функция для нахождения всех чисел Фибоначчи до N (рекурсия)
def fibonacci_up_to_n(n, a=0, b=1):
    if a > n:
        return []
    return [a] + fibonacci_up_to_n(n, b, a + b)


# 593. Функция для нахождения чисел, которые делятся на X, используя рекурсию
def find_divisible(lst, x):
    if not lst:
        return []
    return ([lst[0]] if lst[0] % x == 0 else []) + find_divisible(lst[1:], x)


# 594. Функция для подсчета количества четных чисел в списке (рекурсия)
def count_even(lst):
    if not lst:
        return 0
    return (1 if lst[0] % 2 == 0 else 0) + count_even(lst[1:])


# 595. Функция для подсчета количества отрицательных чисел в списке (рекурсия)
def count_negatives(lst):
    if not lst:
        return 0
    return (1 if lst[0] < 0 else 0) + count_negatives(lst[1:])


# 596. Функция для нахождения всех чисел в списке, которые больше среднего значения (рекурсия)
def greater_than_average_3(lst, avg=None):
    if not lst:
        return []
    if avg is None:
        avg = sum(lst) / len(lst)
    return ([lst[0]] if lst[0] > avg else []) + greater_than_average_3(lst[1:], avg)


# 597. Функция для нахождения суммы чисел, которые больше X в списке (рекурсия)
def sum_greater_than_x(lst, x):
    if not lst:
        return 0
    return (lst[0] if lst[0] > x else 0) + sum_greater_than_x(lst[1:], x)


# 598. Функция для нахождения длины строки (рекурсия)
def string_length(s):
    if s == "":
        return 0
    return 1 + string_length(s[1:])


# 599. Функция для подсчета количества четных чисел в диапазоне от 1 до N (рекурсия)
def count_evens_in_range(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return 1 + count_evens_in_range(n - 1)
    return count_evens_in_range(n - 1)


# 600. Функция для вычисления суммы чисел, которые находятся в пределах заданного диапазона (рекурсия)
def sum_in_range(lst, low, high):
    if not lst:
        return 0
    return (lst[0] if low <= lst[0] <= high else 0) + sum_in_range(lst[1:], low, high)
