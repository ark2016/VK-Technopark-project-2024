# 841. Функция для нахождения первой заглавной буквы в строке
def find_first_uppercase_letter(s):
    for char in s:
        if char.isupper():
            return char
    return None


# 842. Функция для преобразования строки в обратный порядок
def reverse_string_in_place(s):
    result = ''
    for char in reversed(s):
        result += char
    return result


# 843. Функция для замены всех заглавных букв на строчные
def convert_upper_to_lower(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char.lower()
        else:
            result += char
    return result


# 844. Функция для нахождения всех букв, которые встречаются более одного раза
def find_repeated_chars(s):
    count = {}
    repeated = ''
    for char in s:
        if char.isalpha():
            count[char] = count.get(char, 0) + 1
    for char, cnt in count.items():
        if cnt > 1:
            repeated += char
    return repeated if repeated else None


# 845. Функция для нахождения всех символов, которые не являются буквами
def find_non_alphabetic_chars(s):
    result = ''
    for char in s:
        if not char.isalpha():
            result += char
    return result if result else None


# 846. Функция для конкатенации списка строк
def concatenate_strings_from_list(lst):
    result = ''
    for s in lst:
        result += s
    return result


# 847. Функция для поиска строки с минимальной длиной
def find_min_length_string(lst):
    if not lst:
        return None
    min_string = lst[0]
    for s in lst:
        if len(s) < len(min_string):
            min_string = s
    return min_string


# 848. Функция для замены всех символов на их позицию в алфавите
def replace_with_alphabet_position(s):
    result = ''
    for char in s:
        if char.isalpha():
            result += str(ord(char.lower()) - 96)
        else:
            result += char
    return result


# 849. Функция для нахождения всех делителей числа
def find_divisors(n):
    if n == 0:
        return None
    divisors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors if divisors else None


# 850. Функция для проверки, является ли число простым
def is_prime_66(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 851. Функция для нахождения суммы цифр числа
def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


# 852. Функция для умножения числа на его собственные цифры
def multiply_by_digits(n):
    n = abs(n)
    result = 1
    while n > 0:
        digit = n % 10
        if digit != 0:
            result *= digit
        n //= 10
    return result if result != 1 else None


# 853. Функция для нахождения максимальной цифры в числе
def max_digit_in_number(n):
    n = abs(n)
    max_digit = -1
    while n > 0:
        digit = n % 10
        if digit > max_digit:
            max_digit = digit
        n //= 10
    return max_digit if max_digit != -1 else None


def count_even_numbers_5(lst):
    def is_odd(n):
        if n % 2 != 0:
            return True
        return False
    count = 0
    for n in lst:
        if not is_odd(n):
            count += 1
    return count if count > 0 else None


# 854. Функция для нахождения наибольшего числа, которое делится на 3 в списке
def find_largest_divisible_by_3(lst):
    largest = None
    for n in lst:
        if n % 3 == 0 and (largest is None or n > largest):
            largest = n
    return largest


# 855. Функция для нахождения наименьшего числа, которое делится на 5 в списке
def find_smallest_divisible_by_5(lst):
    smallest = None
    for n in lst:
        if n % 5 == 0 and (smallest is None or n < smallest):
            smallest = n
    return smallest


# 856. Функция для нахождения произведения всех чисел в списке
def multiply_all_numbers(lst):
    if not lst:
        return None
    result = 1
    for n in lst:
        result *= n
    return result


# 857. Функция для нахождения количества чисел, которые больше заданного порога
def count_numbers_greater_than(lst, threshold):
    count = 0
    for n in lst:
        if n > threshold:
            count += 1
    return count if count > 0 else None


# 858. Функция для нахождения чисел, которые не делятся на 2, 3 или 5
def find_numbers_not_divisible_by_2_3_5(lst):
    result = []
    for n in lst:
        if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
            result.append(n)
    return result if result else None


# 859. Функция для подсчета количества чисел, которые делятся на 7
def count_divisible_by_7(lst):
    count = 0
    for n in lst:
        if n % 7 == 0:
            count += 1
    return count if count > 0 else None


# 860. Функция для нахождения максимального числа, которое является квадратом целого числа
def find_largest_square_number(lst):
    largest = None
    for n in lst:
        if (n ** 0.5).is_integer() and (largest is None or n > largest):
            largest = n
    return largest
