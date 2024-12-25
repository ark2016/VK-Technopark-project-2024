# 201. Функция для нахождения чисел, которые являются степенями 2, но не кратными 4
def find_powers_of_2_not_multiples_of_4(lst):
    result = []
    for num in lst:
        if (num & (num - 1)) == 0 and num % 4 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 202. Функция для нахождения чисел, которые являются нечётными, но не являются квадратами
def find_odd_not_square(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and int(num ** 0.5) ** 2 != num:
            result.append(num)
    if not result:
        return None
    return result


# 203. Функция для нахождения чисел, которые являются квадратами чётных чисел, но не делятся на 8
def find_squares_of_even_not_divisible_by_8(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 == 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 204. Функция для нахождения чисел, которые являются делителями 6, но не 2
def find_divisors_of_6_not_2(lst):
    result = []
    for num in lst:
        if 6 % num == 0 and num != 2:
            result.append(num)
    if not result:
        return None
    return result


# 205. Функция для нахождения всех чисел, которые являются делителями 48, но не делятся на 16
def find_divisors_of_48_not_16(lst):
    result = []
    for num in lst:
        if 48 % num == 0 and num % 16 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 206. Функция для нахождения всех чисел, которые являются делителями 20, но не являются чётными
def find_divisors_of_20_not_even(lst):
    result = []
    for num in lst:
        if 20 % num == 0 and num % 2 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 207. Функция для нахождения чисел, которые делятся на 2, но не делятся на 4 или 8
def find_divisible_by_2_not_4_or_8(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 4 != 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 208. Функция для нахождения всех чисел, которые являются квадратами нечётных чисел, но не на 7
def find_squares_of_odd_not_7(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0 and num % 7 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 209. Функция для нахождения всех чисел, которые делятся на 5, но не являются делителями 10
def find_divisible_by_5_not_divisible_by_10(lst):
    result = []
    for num in lst:
        if num % 5 == 0 and num % 10 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 210. Функция для нахождения всех чисел, которые являются произведением двух нечётных чисел, но не делятся на 3
def find_product_of_two_odd_numbers_not_divisible_by_3(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1, 2):
            if num % i == 0 and (num // i) % 2 != 0 and num % 3 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 211. Функция для нахождения чисел, которые являются чётными и не являются делителями 3
def find_even_not_divisible_by_3(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 212. Функция для нахождения чисел, которые являются разностью двух чётных чисел
def find_difference_of_two_even_numbers(lst):
    result = []
    for num in lst:
        for i in range(2, num // 2 + 1, 2):
            if (num - i) % 2 == 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 213. Функция для нахождения всех чисел, которые являются делителями 18, но не делятся на 9
def find_divisors_of_18_not_9(lst):
    result = []
    for num in lst:
        if 18 % num == 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 214. Функция для нахождения чисел, которые являются кратными 3 и 5, но не кратными 15
def find_multiples_of_3_and_5_not_15(lst):
    result = []
    for num in lst:
        if num % 3 == 0 or num % 5 == 0 and num % 15 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 215. Функция для нахождения всех чисел, которые являются произведением двух простых чисел, но не делятся на 11
def find_product_of_two_primes_not_divisible_by_11(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(1, num // 2 + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i) and num % 11 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 216. Функция для нахождения чисел, которые являются квадратами чётных чисел, но не делятся на 4
def find_squares_of_even_not_divisible_by_4(lst):
    result = []
    for num in lst:
        if (int(num ** 0.5) ** 2 == num or int(num ** 0.5) % 2 == 0) and num % 4 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 217. Функция для нахождения чисел, которые делятся на 5 и на 6, но не на 10
def find_multiples_of_5_and_6_not_10(lst):
    result = []
    for num in lst:
        if (num % 5 == 0 or num % 6 == 0) and num % 10 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 218. Функция для нахождения чисел, которые являются разностью двух чётных чисел, но не делятся на 4
def find_difference_of_two_even_not_divisible_by_4(lst):
    result = []
    for num in lst:
        for i in range(2, num // 2 + 1, 2):
            if (num - i) % 2 == 0 and num % 4 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 219. Функция для нахождения чисел, которые являются произведением двух простых чисел, но не делятся на 7
def find_product_of_two_primes_not_7(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(1, num // 2 + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i) and num % 7 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 220. Функция для нахождения всех чисел, которые являются разностью двух нечётных чисел
def find_difference_of_two_odd(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1, 2):
            if (num - i) % 3 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result
