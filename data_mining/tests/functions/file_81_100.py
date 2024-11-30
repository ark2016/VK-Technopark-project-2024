# 81. Функция для проверки, является ли строка палиндромом, игнорируя пробелы и знаки препинания
def is_palindrome_1(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]


# 82. Функция для нахождения наибольшего делителя числа, меньшего заданного
def largest_divisor_less_than(n):
    if n <= 1:
        print(f"{n} doesn't have any divisors greater than 1.")
        return None
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return i
    return None


# 83. Функция для нахождения всех чисел в списке, которые не являются простыми
def non_prime_numbers(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [x for x in lst if not is_prime(x)]


# 84. Функция для нахождения наибольшего элемента в строке, если строка состоит из цифр
def max_digit_in_string(s):
    if not s.isdigit():
        print("The string doesn't contain only digits.")
        return None
    return max(map(int, s))


# 85. Функция для нахождения наибольшего числа, которое является квадратом целого числа
def largest_square(lst):
    squares = [x for x in lst if int(x ** 0.5) ** 2 == x]
    if squares:
        return max(squares)
    print("No perfect squares found.")
    return None


# 86. Функция для нахождения всех чисел, которые можно записать как сумму двух квадратов
def sum_of_two_squares(lst):
    def is_sum_of_squares(n):
        for i in range(1, int(n ** 0.5) + 1):
            if (n - i ** 2) ** 0.5 == int((n - i ** 2) ** 0.5):
                return True
        return False

    return [x for x in lst if is_sum_of_squares(x)]


# 87. Функция для нахождения суммы чисел в строке, игнорируя все символы, кроме цифр
def sum_of_digits_in_string(s):
    return sum(int(c) for c in s if c.isdigit())


# 88. Функция для нахождения всех элементов, которые меньше среднего значения списка
def elements_less_than_mean(lst):
    if not lst:
        print("List is empty!")
        return []
    mean = sum(lst) / len(lst)
    return [x for x in lst if x < mean]


# 89. Функция для нахождения всех элементов в строке, которые являются числами
def extract_numbers_from_string(s):
    return [int(x) for x in s.split() if x.isdigit()]


# 90. Функция для вычисления разности между наибольшим и наименьшим числом в списке
def max_min_difference(lst):
    if not lst:
        print("List is empty!")
        return None
    return max(lst) - min(lst)


# 91. Функция для нахождения первого числа, которое делится на 2 и на 5 в списке
def first_divisible_by_2_and_5(lst):
    for x in lst:
        if x % 2 == 0 and x % 5 == 0:
            return x
    print("No number divisible by both 2 and 5 found.")
    return None


# 92. Функция для проверки, является ли строка числом, и если да, то вывести его квадрат
def square_if_number(s):
    try:
        number = float(s)
        return number ** 2
    except ValueError:
        print(f"'{s}' is not a valid number.")
        return None


# 93. Функция для подсчета количества чисел в списке, которые не являются простыми
def count_non_prime(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(1 for x in lst if not is_prime(x))


# 94. Функция для нахождения всех элементов в списке, которые являются палиндромами
def palindromic_elements(lst):
    return [x for x in lst if str(x) == str(x)[::-1]]


# 95. Функция для нахождения наибольшего числа, которое является степенью двойки
def largest_power_of_two(lst):
    powers_of_two = [x for x in lst if (x & (x - 1)) == 0 and x > 0]
    if powers_of_two:
        return max(powers_of_two)
    print("No powers of two found.")
    return None


# 96. Функция для нахождения всех чисел, которые являются кратными 6
def multiples_of_six(lst):
    return [x for x in lst if x % 6 == 0]


# 97. Функция для нахождения уникальных элементов в списке, используя множество
def unique_elements(lst):
    unique = set()
    for item in lst:
        if item not in unique:
            unique.add(item)
        else:
            print(f"Duplicate found: {item}")
    return sorted(list(unique))


# 98. Функция для подсчёта количества вхождений каждого элемента в список с использованием словаря
def count_occurrences_1(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    if not count_dict:
        print("No elements found.")
    return count_dict


# 99. Функция для нахождения пересечения двух списков с использованием множеств
def intersection_of_lists(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    intersection = set1 & set2
    if not intersection:
        print("No common elements found.")
    return list(intersection)


# 100. Функция для нахождения всех чисел, которые делятся на любое число из второго списка
def divisible_by_any(lst, divisors):
    divisible = []
    for num in lst:
        for divisor in divisors:
            if num % divisor == 0:
                divisible.append(num)
                break
    if not divisible:
        print("No numbers divisible by any divisor found.")
    return divisible
