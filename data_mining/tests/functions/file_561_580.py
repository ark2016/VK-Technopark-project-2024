# 561. Функция для нахождения всех чисел, которые меньше заданного значения
def less_than_value(lst, value):
    if not isinstance(value, (int, float)) or not lst:
        return None
    return [x for x in lst if isinstance(x, (int, float)) and x < value]


# 562. Функция для нахождения суммы квадратов чисел в списке
def sum_of_squares_2(lst):
    if not lst:
        return None
    return sum(x ** 2 for x in lst if isinstance(x, (int, float)))


# 563. Функция для нахождения разности между максимальным и минимальным числом, но только для положительных чисел
def positive_max_min_difference(lst):
    if not lst:
        return None
    positive_numbers = [x for x in lst if isinstance(x, (int, float)) and x > 0]
    if not positive_numbers:
        return None
    return max(positive_numbers) - min(positive_numbers)


# 564. Функция для нахождения разности между максимальным и минимальным числом, но только для отрицательных чисел
def negative_max_min_difference(lst):
    if not lst:
        return None
    negative_numbers = [x for x in lst if isinstance(x, (int, float)) and x < 0]
    if not negative_numbers:
        return None
    return max(negative_numbers) - min(negative_numbers)


# 565. Функция для нахождения суммы всех чисел, которые делятся на X без остатка
def sum_of_divisible_by_x(lst, x):
    if not isinstance(x, (int, float)) or x == 0 or not lst:
        return None
    return sum(x for x in lst if isinstance(x, (int, float)) and x % x == 0)


# 566. Функция для нахождения всех чисел, которые являются кубами
def cubes(lst):
    if not lst:
        return None
    return [x for x in lst if isinstance(x, (int, float)) and round(x ** (1 / 3), 6) ** 3 == x]


# 567. Функция для нахождения чисел, которые могут быть представлены как сумма двух квадратов
def sum_of_two_squares_3(lst):
    if not lst:
        return None
    result = []
    for x in lst:
        if isinstance(x, (int, float)):
            for i in range(int(x ** 0.5) + 1):
                for j in range(int(x ** 0.5) + 1):
                    if i ** 2 + j ** 2 == x:
                        result.append(x)
                        break
    return result if result else None


# 568. Функция для проверки, является ли число с плавающей точкой степенью двойки
def is_power_of_two(x):
    if not isinstance(x, (int, float)) or x <= 0:
        return False
    return (x & (x - 1)) == 0


# 569. Функция для нахождения всех чисел, которые являются целыми числами
def integers_in_float_list(lst):
    if not lst:
        return None
    return [x for x in lst if isinstance(x, (int, float)) and x.is_integer()]


# 570. Функция для нахождения суммы всех чисел, которые можно выразить как произведение двух простых чисел
def sum_of_products_of_primes(lst):
    if not lst:
        return None

    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    result = []
    for num in lst:
        if isinstance(num, (int, float)):
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0 and is_prime(i) and is_prime(num // i):
                    result.append(num)
                    break
    return sum(result) if result else None


# 571. Функция для нахождения всех чисел, которые равны разности двух квадратов
def difference_of_two_squares(lst):
    if not lst:
        return None
    result = []
    for num in lst:
        if isinstance(num, int) and num > 0:
            for a in range(1, int(num ** 0.5) + 1):
                if num % a == 0:
                    b = num // a
                    if (a + b) % 2 == 0 and (b - a) % 2 == 0:
                        result.append(num)
                        break
    return result if result else None


# 572. Функция для нахождения всех чисел, которые являются степенями 3 (кубами)
def cubes_of_numbers(lst):
    if not lst:
        return None
    return [x for x in lst if isinstance(x, (int, float)) and round(x ** (1 / 3), 6) ** 3 == x]


# 573. Функция для нахождения среднего арифметического квадратов чисел
def average_of_squares(lst):
    if not lst:
        return None
    return sum(x ** 2 for x in lst if isinstance(x, (int, float))) / len(lst)


# 574. Функция для вычисления факториала числа (рекурсия)
def factorial_2(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_2(n - 1)


# 575. Функция для вычисления суммы чисел от 1 до N (рекурсия)
def sum_to_n(n):
    if n <= 0:
        return 0
    return n + sum_to_n(n - 1)


# 576. Функция для нахождения N-го числа Фибоначчи (рекурсия)
def fibonacci_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_2(n - 1) + fibonacci_2(n - 2)


# 577. Функция для вычисления степени числа (рекурсия)
def power_2(base, exp):
    if exp <= 0:
        return 1
    return base * power_2(base, exp - 1)


# 578. Функция для нахождения суммы элементов списка (рекурсия)
def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])


# 579. Функция для нахождения произведения элементов списка (рекурсия)
def recursive_product(lst):
    if not lst:
        return 1
    return lst[0] * recursive_product(lst[1:])


# 580. Функция для нахождения максимального числа в списке (рекурсия)
def recursive_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        sub_max = recursive_max(lst[1:])
        return lst[0] if lst[0] > sub_max else sub_max
