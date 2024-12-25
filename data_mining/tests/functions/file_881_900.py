# 881. Функция для создания кортежа, состоящего из строк, длина которых больше 3 символов
def find_long_strings(lst):
    result = []
    for s in lst:
        if len(s) > 3:
            result.append(s)
    return tuple(result) if result else None


# 882. Функция для создания кортежа из строк, содержащих хотя бы одну цифру
def find_strings_with_digits_2(lst):
    result = []
    for s in lst:
        if any(char.isdigit() for char in s):
            result.append(s)
    return tuple(result) if result else None


# 883. Функция для создания кортежа из всех чисел, которые являются квадратами целых чисел
def find_square_numbers(lst):
    result = []
    for n in lst:
        if (n ** 0.5).is_integer():
            result.append(n)
    return tuple(result) if result else None


# 884. Функция для создания кортежа из чисел, которые делятся на 5
def find_divisible_by_5(lst):
    result = []
    for n in lst:
        if n % 5 == 0:
            result.append(n)
    return tuple(result) if result else None


# 885. Функция для создания кортежа из строк, длина которых меньше или равна 5 символам
def find_short_strings(lst):
    result = []
    for s in lst:
        if len(s) <= 5:
            result.append(s)
    return tuple(result) if result else None


# 886. Функция для создания кортежа из чисел, которые больше заданного порога
def find_greater_than(lst, threshold):
    result = []
    for n in lst:
        if n > threshold:
            result.append(n)
    return tuple(result) if result else None


# 887. Функция для создания кортежа, содержащего индексы всех элементов, равных максимальному
def find_max_indexes(lst):
    if not lst:
        return None
    max_val = max(lst)
    indexes = [i for i, x in enumerate(lst) if x == max_val]
    return tuple(indexes) if indexes else None


# 888. Функция для нахождения кортежа чисел, которые являются четными и больше 10
def find_even_and_greater_than_ten(lst):
    result = []
    for n in lst:
        if n % 2 == 0 and n > 10:
            result.append(n)
    return tuple(result) if result else None


# 889. Функция для создания кортежа из всех строк, в которых есть хотя бы одна заглавная буква
def find_strings_with_uppercase(lst):
    result = []
    for s in lst:
        if any(char.isupper() for char in s):
            result.append(s)
    return tuple(result) if result else None


# 890. Функция для создания кортежа из чисел, которые делятся на 4 и не делятся на 2
def find_numbers_divisible_by_4_not_2(lst):
    result = []
    for n in lst:
        if n % 2 == 0 and n % 16 != 0:
            result.append(n)
    return tuple(result) if result else None


# 891. Функция для создания кортежа из всех строк, длина которых больше средней длины всех строк
def find_longer_than_average(lst):
    average_length = sum(len(s) for s in lst) / len(lst) if lst else 0
    result = []
    for s in lst:
        if len(s) > average_length:
            result.append(s)
    return tuple(result) if result else None


# 892. Функция для создания кортежа из чисел, которые равны сумме их цифр
def find_numbers_equal_to_digit_sum(lst):
    result = []
    for n in lst:
        if n == sum(int(digit) for digit in str(abs(n))):
            result.append(n)
    return tuple(result) if result else None


# 893. Функция для создания кортежа из чисел, которые являются делителями 100
def find_divisors_of_100(lst):
    result = []
    for n in lst:
        if 100 % n == 0:
            result.append(n)
    return tuple(result) if result else None


# 894. Функция для создания кортежа из чисел, которые являются кратными 3 и 5
def find_multiples_of_3_and_5(lst):
    result = []
    for n in lst:
        if n % 3 == 0 and n % 5 == 0:
            result.append(n)
    return tuple(result) if result else None


# 895. Функция для создания кортежа, содержащего все числа, кратные числу из списка
def find_multiples_of_list(lst, n):
    result = []
    for num in lst:
        if num % n == 0:
            result.append(num)
    return tuple(result) if result else None


# 896. Функция для нахождения всех чисел, которые являются результатом возведения чисел в квадрат
def find_squared_numbers(lst):
    result = []
    for n in lst:
        if (n ** 0.5).is_integer():
            result.append(n)
    return tuple(result) if result else None


# 897. Функция для создания кортежа, содержащего числа из списка, которые делятся на 6
def find_divisible_by_6_2(lst):
    result = []
    for n in lst:
        if n % 6 == 0:
            result.append(n)
    return tuple(result) if result else None


# 898. Функция для нахождения чисел, делящихся на 2 и 3
def find_divisible_by_2_and_3_2(lst):
    result = []
    for n in lst:
        if n % 2 == 0 and n % 3 == 0:
            result.append(n)
    return tuple(result) if result else None


# 899. Функция для создания кортежа с числами, которые кратны 2, 3 и 5
def find_multiples_of_2_3_5(lst):
    result = []
    for n in lst:
        if n % 2 == 0 and n % 3 == 0 and n % 5 == 0:
            result.append(n)
    return tuple(result) if result else None


# 900. Функция для создания кортежа из всех чисел, которые являются палиндромами
def find_palindromes_4(lst):
    result = []
    for n in lst:
        if str(n) == str(n)[::-1]:
            result.append(n)
    return tuple(result) if result else None
