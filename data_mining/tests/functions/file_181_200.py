# 181. Функция для нахождения всех чисел, которые являются разностью двух квадратов
def find_difference_of_two_squares(lst):
    result = []
    for num in lst:
        for i in range(1, int(num ** 0.5) + 1):
            if (num + i ** 2) ** 0.5 == int((num + i ** 2) ** 0.5):
                result.append(num)
                break
    if not result:
        return "No numbers found that are the difference of two squares."
    return result


# 182. Функция для нахождения всех чисел, которые могут быть записаны как сумма двух чисел, каждое из которых делится на 3
def find_sum_of_two_divisible_by_3(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1):
            if i % 3 == 0 and (num - i) % 3 == 0:
                result.append(num)
                break
    if not result:
        return "No numbers found that are the sum of two numbers divisible by 3."
    return result


# 183. Функция для нахождения всех чисел, которые не являются чётными, но являются делителями 9
def find_not_even_but_divisible_by_9(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 9 == 0:
            result.append(num)
    if not result:
        return "No numbers found that are not even but divisible by 9."
    return result


# 184. Функция для нахождения всех чисел, которые являются четными но не делятся на 4
def find_divisible_by_2(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 4 != 0:
            result.append(num)
    if not result:
        return "No numbers."
    return result


# 185. Функция для нахождения всех чисел, которые делятся на 2 или на 3, но не на 6
def find_divisible_by_2_or_3_not_6(lst):
    result = []
    for num in lst:
        if (num % 2 == 0 or num % 3 == 0) and num % 6 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are divisible by 2 or 3 but not 6."
    return result


# 186. Функция для нахождения чисел, которые являются делителями 12, но не являются чётными
def find_divisors_of_12_not_even(lst):
    result = []
    for num in lst:
        if 12 % num == 0 and num % 2 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are divisors of 12 but not even."
    return result


# 187. Функция для нахождения всех чисел, которые являются делителями 6, но не 12
def find_divisors_of_6_not_12(lst):
    result = []
    for num in lst:
        if 6 % num == 0 and num != 12:
            result.append(num)
    if not result:
        return "No numbers found that are divisors of 6 but not 12."
    return result


# 188. Функция для нахождения всех чисел, которые являются квадратами чётных чисел
def find_squares_of_even_numbers(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 == 0:
            result.append(num)
    if not result:
        return "No squares of even numbers found."
    return result


# 189. Функция для нахождения чисел, которые не являются степенями 2, но являются чётными
def find_even_not_powers_of_2(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and (num & (num - 1)) != 0:
            result.append(num)
    if not result:
        return "No even numbers found that are not powers of 2."
    return result


# 190. Функция для нахождения всех чисел, которые не являются чётными и не являются делителями 9
def find_not_even_and_not_divisible_by_9(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are neither even nor divisible by 9."
    return result


# 191. Функция для нахождения чисел, которые делятся на 3 и 5, но не на 7
def find_multiples_of_3_and_5_not_7(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 5 == 0 and num % 7 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are divisible by 3 and 5 but not 7."
    return result


# 192. Функция для нахождения всех чисел, которые являются произведением двух нечётных чисел
def find_product_of_two_odd_numbers(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1, 2):
            if num % i == 0 and (num // i) % 2 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 193. Функция для нахождения чисел, которые являются произведением двух простых чисел
def find_product_of_two_primes(lst):
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
            if num % i == 0 and is_prime(i) and is_prime(num // i):
                result.append(num)
                break
    if not result:
        return None
    return result


# 194. Функция для нахождения всех чисел, которые являются нечётными и не являются степенями 2
def find_odd_not_power_of_2(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and (num & (num - 1)) != 0:
            result.append(num)
    if not result:
        return None
    return result


# 195. Функция для нахождения чисел, которые делятся на 6, но не делятся на 9
def find_divisible_by_6_not_9(lst):
    result = []
    for num in lst:
        if num % 6 == 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 196. Функция для нахождения всех чисел, которые являются делителями 24, но не делятся на 8
def find_divisors_of_24_not_8(lst):
    result = []
    for num in lst:
        if 24 % num == 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 197. Функция для нахождения чисел, которые являются квадратами нечётных чисел
def find_squares_of_odd_numbers(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 198. Функция для нахождения чисел, которые являются степенями 2, но не чётными
def find_powers_of_2_not_even(lst):
    result = []
    for num in lst:
        if (num & (num - 1)) == 0 and num % 2 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 199. Функция для нахождения чисел, которые не являются кратными 3, но делятся на 5
def find_not_multiples_of_3_but_divisible_by_5(lst):
    result = []
    for num in lst:
        if num % 3 != 0 and num % 5 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 200. Функция для нахождения чисел, которые являются делителями 15, но не делятся на 3
def find_divisors_of_15_not_3(lst):
    result = []
    for num in lst:
        if 15 % num == 0 and num % 3 != 0:
            result.append(num)
    if not result:
        return None
    return result
