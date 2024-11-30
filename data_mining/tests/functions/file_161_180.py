# 161. Функция для нахождения чисел, которые являются простыми, но не являются кратными 3
def find_primes_not_multiples_of_3(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        if is_prime(num) and num % 3 != 0:
            result.append(num)
    if not result:
        print("No prime numbers found that are not divisible by 3.")
    return result


# 162. Функция для нахождения чисел, которые являются чётными и делятся на 4
def find_even_numbers_divisible_by_4(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 4 == 0:
            result.append(num)
    if not result:
        print("No even numbers divisible by 4 found.")
    return result


# 163. Функция для нахождения всех чисел, которые не являются степенями двойки
def find_non_powers_of_two(lst):
    result = []
    for num in lst:
        if (num & (num - 1)) != 0:
            result.append(num)
    if not result:
        print("No numbers found that are not powers of two.")
    return result


# 164. Функция для подсчёта всех чисел в строке, которые больше среднего значения всех чисел в строке
def count_numbers_greater_than_average(s):
    nums = [int(x) for x in s.split() if x.isdigit()]
    if not nums:
        print("No numbers found in the string.")
        return 0
    average = sum(nums) / len(nums)
    count = sum(1 for num in nums if num > average)
    return count


# 165. Функция для нахождения всех чисел, которые делятся на 4 или на 5, но не на 20
def find_multiples_of_4_or_5_not_20(lst):
    result = []
    for num in lst:
        if (num % 4 == 0 or num % 5 == 0) and num % 20 != 0:
            result.append(num)
    if not result:
        print("No numbers found that are divisible by 4 or 5, but not by 20.")
    return result


# 166. Функция для поиска всех чисел, которые являются точными делителями 100
def find_exact_divisors_of_100(lst):
    result = []
    for num in lst:
        if 100 % num == 0:
            result.append(num)
    if not result:
        print("No numbers found that are exact divisors of 100.")
    return result


# 167. Функция для поиска чисел, которые являются нечётными и не являются делителями 5
def find_odd_not_divisible_by_5(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 5 != 0:
            result.append(num)
    if not result:
        print("No odd numbers found that are not divisible by 5.")
    return result


# 168. Функция для нахождения всех чисел, которые являются кратными либо 2, либо 3, но не обоим
def find_multiples_of_2_or_3(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 != 0:
            result.append(num)
        elif num % 3 == 0 and num % 2 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are multiples of 2 or 3, but not both."
    return result


# 169. Функция для нахождения всех чисел, которые либо нечётные, либо делятся на 4
def find_odd_or_divisible_by_4(lst):
    result = []
    for num in lst:
        if num % 2 != 0 or num % 4 == 0:
            result.append(num)
    if not result:
        return "No odd numbers or numbers divisible by 4 found."
    return result


# 170. Функция для нахождения чисел, которые являются квадратами целых чисел, но не чётными
def find_even_squares(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and num % 2 == 0:
            result.append(num)
    if not result:
        return "No even square numbers found."
    return result


# 171. Функция для нахождения всех чисел, которые являются кратными 3 или 5, но не кратными обоим
def find_multiples_of_3_or_5_not_both(lst):
    result = []
    for num in lst:
        if (num % 3 == 0 or num % 5 == 0) and not (num % 3 == 0 and num % 5 == 0):
            result.append(num)
    if not result:
        return "No numbers found that are multiples of 3 or 5 but not both."
    return result


# 172. Функция для подсчёта всех чисел в строке, которые больше среднего значения
def count_numbers_greater_than_mean(s):
    nums = [int(x) for x in s.split() if x.isdigit()]
    if not nums:
        return "No numbers found in the string."

    mean = sum(nums) / len(nums)
    count = len([num for num in nums if num > mean])
    if count == 0:
        return "No numbers greater than the mean."
    return count


# 173. Функция для нахождения всех чисел, которые являются степенями 2
def find_powers_of_2(lst):
    result = []
    for num in lst:
        if (num & (num - 1)) == 0:
            result.append(num)
    if not result:
        return "No powers of 2 found."
    return result


# 174. Функция для нахождения всех чисел, которые являются четными и кратными 8
def find_even_and_divisible_by_8(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 8 == 0:
            result.append(num)
    if not result:
        return "No even numbers divisible by 8 found."
    return result


# 175. Функция для нахождения чисел, которые являются нечётными и делятся на 3
def find_odd_and_divisible_by_3(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 3 == 0:
            result.append(num)
    if not result:
        return "No odd numbers divisible by 3 found."
    return result


# 176. Функция для нахождения всех чисел, которые не являются чётными или кратными 7
def find_non_even_or_not_multiples_of_7(lst):
    result = []
    for num in lst:
        if num % 2 != 0 or num % 7 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are not even or not divisible by 7."
    return result

# 177. Функция для нахождения чисел, которые не делятся на 2, но делятся на 5
def find_not_divisible_by_2_but_divisible_by_5(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 5 == 0:
            result.append(num)
    if not result:
        return "No numbers found that are not divisible by 2 but divisible by 5."
    return result


# 178. Функция для нахождения всех чисел, которые являются кратными 3, 5 или 7
def find_multiples_of_3_5_or_7(lst):
    result = []
    for num in lst:
        if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
            result.append(num)
    if not result:
        return "No numbers found that are multiples of 3, 5, or 7."
    return result


# 179. Функция для нахождения всех чисел, которые являются чётными, но не являются делителями 4
def find_even_not_divisible_by_4(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 4 != 0:
            result.append(num)
    if not result:
        return "No even numbers found that are not divisible by 4."
    return result


# 180. Функция для нахождения чисел, которые являются кратными 3 или 5, но не кратными 15
def find_multiples_of_3_or_5_not_15(lst):
    result = []
    for num in lst:
        if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are multiples of 3 or 5 but not 15."
    return result
