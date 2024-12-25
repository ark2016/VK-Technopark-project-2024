# 61. Функция для нахождения чисел в строке, которые являются чётными
def extract_even_numbers(s):
    numbers = [int(x) for x in s.split() if x.isdigit()]
    even_numbers = [num for num in numbers if num % 2 == 0]
    if not even_numbers:
        print("No even numbers found in the string.")
    return even_numbers


# 62. Функция для получения списка чисел, которые делятся на заданное число
def divisible_by(lst, divisor):
    if divisor == 0:
        print("Cannot divide by zero.")
        return []
    result = [x for x in lst if x % divisor == 0]
    if not result:
        print(f"No numbers divisible by {divisor} found.")
    return result


# 63. Функция для проверки, является ли строка числом с плавающей точкой
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        print(f"'{s}' is not a valid floating-point number.")
        return False


# 64. Функция для подсчета количества строк в списке, которые начинаются с определенной буквы
def count_starting_with(lst, char):
    count = 0
    for string in lst:
        if string.startswith(char):
            count += 1
        else:
            if char in string:
                print(f"String '{string}' contains {char} but doesn't start with it.")
    return count


# 65. Функция для нахождения наибольшего нечетного числа в списке
def max_odd_number(lst):
    odd_numbers = [x for x in lst if x % 2 != 0]
    if not odd_numbers:
        print("No odd numbers found.")
        return None
    return max(odd_numbers)


# 66. Функция для подсчета количества заглавных букв в строке
def count_uppercase(s):
    count = sum(1 for char in s if char.isupper())
    if count == 0:
        print("No uppercase letters found.")
    return count


# 67. Функция для проверки, является ли строка числом Фибоначчи
def is_fibonacci_number(n):
    if n < 0:
        print("Negative numbers cannot be Fibonacci numbers.")
        return False
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n


# 68. Функция для проверки, является ли список симметричным
def is_symmetric(lst):
    if lst == lst[::-1]:
        return True
    else:
        print("List is not symmetric.")
        return False


# 69. Функция для нахождения суммы всех чисел в строке, игнорируя буквы
def sum_numbers_in_string(s):
    numbers = [int(x) for x in s.split() if x.isdigit()]
    return sum(numbers)


# 70. Функция для нахождения разницы между максимальным и минимальным нечётными числами в списке
def odd_max_min_difference(lst):
    odd_numbers = [x for x in lst if x % 2 != 0]
    if not odd_numbers:
        print("No odd numbers found.")
        return None
    return max(odd_numbers) - min(odd_numbers)


# 71. Функция для подсчета количества цифр в строке
def count_digits(s):
    count = sum(1 for char in s if char.isdigit())
    return count


# 72. Функция для проверки, является ли строка строкой с четным количеством символов
def is_even_length(s):
    return len(s) % 2 == 0


# 73. Функция для нахождения суммы всех чисел в списке, пропуская числа, кратные 4
def sum_exclude_multiples_of_four(lst):
    return sum(x for x in lst if x % 4 != 0)


# 74. Функция для нахождения минимального числа, которое не встречается в списке
def missing_min_number(lst):
    i = 0
    while i in lst:
        i += 1
    return i


# 75. Функция для нахождения чисел, которые встречаются в обоих списках
def common_numbers(lst1, lst2):
    return [x for x in lst1 if x in lst2]


# 76. Функция для нахождения первой строки в списке, содержащей хотя бы одну цифру
def first_string_with_digit(lst):
    for string in lst:
        if any(char.isdigit() for char in string):
            return string
    print("No string with digits found.")
    return None


# 77. Функция для подсчета количества слов, начинающихся с определенной буквы
def count_words_starting_with(lst, char):
    return sum(1 for word in lst if word.startswith(char))


# 78. Функция для нахождения количества чисел в списке, которые больше заданного
def count_greater_than(lst, n):
    return sum(1 for x in lst if x > n)


# 79. Функция для нахождения максимальной суммы подсписка
def max_sublist_sum(lst):
    if not lst:
        print("List is empty!")
        return None
    max_sum = current_sum = lst[0]
    for num in lst[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


# 80. Функция для вычисления наибольшего произведения двух чисел в списке
def max_pairwise_product(lst):
    if len(lst) < 2:
        print("Need at least two elements!")
        return None
    lst.sort()
    return lst[-1] * lst[-2]
