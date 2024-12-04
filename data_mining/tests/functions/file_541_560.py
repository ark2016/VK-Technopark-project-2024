# 541. Функция для нахождения наибольшего числа с плавающей точкой в списке
def max_float(lst):
    if not lst:
        return None
    max_val = float('-inf')
    for num in lst:
        if isinstance(num, (int, float)) and num > max_val:
            max_val = num
    return max_val if max_val != float('-inf') else None


# 542. Функция для нахождения наименьшего числа с плавающей точкой в списке
def min_float(lst):
    if not lst:
        return None
    min_val = float('inf')
    for num in lst:
        if isinstance(num, (int, float)) and num < min_val:
            min_val = num
    return min_val if min_val != float('inf') else None


# 543. Функция для проверки, является ли число с плавающей точкой положительным
def is_positive_float(x):
    if not isinstance(x, (int, float)):
        return None
    return x > 0


# 544. Функция для нахождения разницы между двумя числами с плавающей точкой
def difference_between_floats(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return None
    return abs(x - y)


# 545. Функция для нахождения произведения всех чисел в списке с плавающими точками
def product_of_floats(lst):
    if not lst:
        return None
    product = 1.0
    for num in lst:
        if isinstance(num, (int, float)):
            product *= num
        else:
            return None
    return product


# 546. Функция для деления двух чисел с плавающей точкой с учётом ошибок деления на ноль
def divide_floats(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return None
    if y == 0:
        return None
    return x / y


# 547. Функция для нахождения квадратного корня числа с плавающей точкой
def square_root(x):
    if not isinstance(x, (int, float)) or x < 0:
        return None
    return x ** 0.5


# 548. Функция для округления числа с плавающей точкой до ближайшего целого
def round_to_nearest_integer(x):
    if not isinstance(x, (int, float)):
        return None
    return round(x)


# 549. Функция для нахождения всех чисел, которые делятся на X с плавающей точкой
def divisible_by_x(lst, x):
    if not isinstance(x, (int, float)) or x == 0 or not lst:
        return None
    result = []
    for num in lst:
        if isinstance(num, (int, float)) and num % x == 0:
            result.append(num)
    return result if result else None


# 550. Функция для вычисления значения экспоненты для числа с плавающей точкой
def exponentiation_of_float(x, n):
    if not isinstance(x, (int, float)) or not isinstance(n, (int, float)):
        return None
    return x ** n


# 551. Функция для вычисления факториала числа с плавающей точкой (для целых чисел)
def factorial_of_float(x):
    if not isinstance(x, int) or x < 0:
        return None
    factorial = 1
    for i in range(1, x + 1):
        factorial *= i
    return factorial


# 552. Функция для нахождения медианы в списке чисел с плавающей точкой
def median_of_floats(lst):
    if not lst:
        return None
    lst = [x for x in lst if isinstance(x, (int, float))]
    lst.sort()
    n = len(lst)
    if n == 0:
        return None
    if n % 2 == 1:
        return lst[n // 2]
    else:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2


# 553. Функция для нахождения всех чисел, которые являются простыми с плавающей точкой
def prime_floats(lst):
    if not lst:
        return None

    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    result = [x for x in lst if isinstance(x, int) and is_prime(x)]
    return result if result else None


# 554. Функция для нахождения всех чисел в диапазоне от X до Y с плавающей точкой
def numbers_in_range(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return None
    return [i for i in range(int(x), int(y) + 1)]


# 555. Функция для нахождения геометрической прогрессии
def geometric_progression(a, r, n):
    if not isinstance(a, (int, float)) or not isinstance(r, (int, float)) or not isinstance(n, int) or n <= 0:
        return None
    result = [a * (r ** i) for i in range(n)]
    return result if result else None


# 556. Функция для нахождения суммы всех чисел в геометрической прогрессии
def sum_of_geometric_progression(a, r, n):
    if not isinstance(a, (int, float)) or not isinstance(r, (int, float)) or not isinstance(n, int) or n <= 0:
        return None
    if r == 1:
        return a * n
    return a * (1 - r ** n) / (1 - r)


# 557. Функция для нахождения квадрата числа с плавающей точкой
def square_of_float(x):
    if not isinstance(x, (int, float)):
        return None
    return x * x


# 558. Функция для вычисления суммы ряда с плавающими числами (арифметическая прогрессия)
def sum_of_arithmetic_progression(a, d, n):
    if not isinstance(a, (int, float)) or not isinstance(d, (int, float)) or not isinstance(n, int) or n <= 0:
        return None
    return n * (2 * a + (n - 1) * d) / 2


# 559. Функция для нахождения всех чисел, которые не равны нулю в списке с плавающими точками
def non_zero_floats(lst):
    if not lst:
        return None
    return [x for x in lst if isinstance(x, (int, float)) and x != 0]


# 560. Функция для нахождения чисел, квадрат которых больше заданного значения
def squares_greater_than(lst, value):
    if not isinstance(value, (int, float)) or not lst:
        return None
    return [x for x in lst if isinstance(x, (int, float)) and x ** 2 > value]
