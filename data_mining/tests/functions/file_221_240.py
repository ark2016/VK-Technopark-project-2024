# 221. Функция для нахождения чисел, которые являются произведением двух нечётных чисел, но не делятся на 5
def find_product_of_two_odd_not_5(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1, 2):
            if num % i == 0 and (num // i) % 2 != 0 and num % 5 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 222. Функция для нахождения чисел, которые являются делителями 36, но не делятся на 9
def find_divisors_of_36_not_9(lst):
    result = []
    for num in lst:
        if 36 % num == 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 223. Функция для нахождения чисел, которые являются нечётными и делятся на 5, но не на 10
def find_odd_and_divisible_by_5_not_10(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 5 == 0 and num % 10 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 224. Функция для нахождения всех чисел, которые делятся на 6, но не на 3
def find_divisible_by_6(lst):
    result = []
    for num in lst:
        if num % 6 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 225. Функция для нахождения всех чисел, которые являются делителями 30, но не делятся на 5
def find_divisors_of_30_not_5(lst):
    result = []
    for num in lst:
        if 30 % num == 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 226. Функция для нахождения чисел, которые являются произведением двух простых чисел, но не делятся на 6
def find_product_of_two_primes_not_6(lst):
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
            if num % i == 0 and is_prime(i) and is_prime(num // i) and num % 6 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 227. Функция для нахождения чисел, которые являются чётными и делятся на 7, но не на 14
def find_even_and_divisible_by_7(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 7 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 228. Функция для нахождения чисел, которые являются разностью двух нечётных чисел, но не делятся на 5
def find_difference_of_two_odd_not_5(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1, 2):
            if num % 5 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 229. Функция для нахождения всех чисел, которые являются квадратами нечётных чисел, но не делятся на 5
def find_squares_of_odd_not_divisible_by_5(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 230. Функция для нахождения чисел, которые являются произведением двух простых чисел, но не делятся на 3
def find_product_of_two_primes_not_divisible_by_3(lst):
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
            if num % i == 0 and is_prime(i) and is_prime(num // i) and num % 3 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 231. Функция для нахождения всех чисел, которые являются делителями 40, но не являются чётными
def find_divisors_of_40_not_even(lst):
    result = []
    for num in lst:
        if 40 % num == 0 and num % 2 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 232. Функция для нахождения чисел, которые являются разностью двух чётных чисел, но не делятся на 5
def find_difference_of_two_even_not_5(lst):
    result = []
    for num in lst:
        for i in range(2, num // 2 + 1, 2):
            if (num - i) % 2 == 0 and num % 5 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 233. Функция для нахождения чисел, которые являются произведением двух нечётных чисел, но не делятся на 7
def find_product_of_two_odd_not_divisible_by_7(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1, 2):
            if num % i == 0 and (num // i) % 2 != 0 and num % 7 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 234. Функция для нахождения чисел, которые делятся на 4, но не на 2
def find_divisible_by_4(lst):
    result = []
    for num in lst:
        if num % 4 == 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 235. Функция для нахождения чисел, которые являются квадратами нечётных чисел, но не на 9
def find_squares_of_odd_not_9(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 236. Функция для нахождения чисел, которые являются разностью двух простых чисел
def find_difference_of_two_primes(lst):
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
            if is_prime(i) and is_prime(num - i):
                result.append(num)
                break
    if not result:
        return None
    return result


# 237. Функция для нахождения чисел, которые являются произведением двух простых чисел, но не на 5
def find_product_of_two_primes_not_5(lst):
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
            if num % i == 0 and is_prime(i) and is_prime(num // i) and num % 5 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 238. Функция для нахождения чисел, которые делятся на 2 и на 5, но не на 10
def find_divisible_by_2_and_5_not_10(lst):
    result = []
    for num in lst:
        if (num % 2 == 0 or num % 5 == 0) and num % 10 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 239. Функция для нахождения чисел, которые являются разностью двух чётных чисел, но не делятся на 6
def find_difference_of_two_even_not_divisible_by_6(lst):
    result = []
    for num in lst:
        for i in range(2, num // 2 + 1, 2):
            if (num - i) % 2 == 0 and num % 6 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 240. Функция для нахождения чисел, которые являются произведением двух нечётных чисел, но не делятся на 4
def find_product_of_two_odd_not_divisible_by_4(lst):
    result = []
    for num in lst:
        # Проверяем, что произведение двух нечётных чисел
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0 and i % 2 != 0 and (num // i) % 2 != 0 and num % 5 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result
