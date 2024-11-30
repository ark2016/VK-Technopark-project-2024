# 261. Функция для нахождения чисел, которые делятся на 7 и на 8, но не на 56
def find_divisible_by_7_and_8_not_56(lst):
    result = []
    for num in lst:
        if num % 7 == 0 and num % 8 == 0 and num % 56 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 262. Функция для нахождения чисел, которые являются нечётными и присутствуют в словаре как ключи
def find_odd_keys_in_dict(dict_data):
    result = [key for key in dict_data if key % 2 != 0]
    if not result:
        return None
    return result


# 263. Функция для нахождения чисел, которые являются чётными и присутствуют в кортеже, но не в списке
def find_even_in_tuple_not_in_list(tpl, lst):
    result = [x for x in tpl if x % 2 == 0 and x not in lst]
    if not result:
        return None
    return result


# 264. Функция для нахождения чисел, которые являются делителями 100, но не являются простыми
def find_divisors_of_100_not_prime(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = [num for num in lst if 100 % num == 0 and not is_prime(num)]
    if not result:
        return None
    return result


# 265. Функция для нахождения чисел, которые встречаются в списке, но не в множестве
def find_in_list_not_in_set(lst, s):
    result = [x for x in lst if x not in s]
    if not result:
        return None
    return result


# 266. Функция для нахождения чисел, которые являются результатами суммы элементов из двух списков
def find_sum_of_two_lists(lst1, lst2):
    result = [a + b for a in lst1 for b in lst2]
    if not result:
        return None
    return result


# 267. Функция для нахождения чисел, которые являются разностью элементов из двух списков
def find_difference_of_two_lists(lst1, lst2):
    result = [a - b for a in lst1 for b in lst2]
    if not result:
        return None
    return result


# 268. Функция для нахождения чисел, которые являются нечётными и присутствуют в кортеже, но не в списке
def find_odd_in_tuple_not_in_list(tpl, lst):
    result = [x for x in tpl if x % 2 != 0 and x not in lst]
    if not result:
        return None
    return result


# 269. Функция для нахождения чисел, которые делятся на 5 и на 6, но не на 12
def find_divisible_by_5_and_6_not_12(lst):
    result = []
    for num in lst:
        if num % 5 == 0 and num % 6 == 0 and num % 12 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 270. Функция для нахождения чисел, которые являются нечётными, но не являются делителями 5
def find_odd_not_divisible_by_5_2(lst):
    result = [num for num in lst if num % 2 != 0 and num % 5 != 0]
    if not result:
        return None
    return result


# 271. Функция для нахождения чисел, которые являются чётными и присутствуют в списке и кортеже
def find_even_in_list_and_tuple(lst, tpl):
    result = [x for x in lst if x % 2 == 0 and x in tpl]
    if not result:
        return None
    return result


# 272. Функция для нахождения чисел, которые являются результатом произведения двух чисел
def find_product_of_two_numbers(lst):
    result = [a * b for a in lst for b in lst]
    if not result:
        return None
    return result


# 273. Функция для нахождения чисел, которые являются элементами множества, но не встречаются в списке
def find_in_set_not_in_list_2(s, lst):
    result = [x for x in s if x not in lst]
    if not result:
        return None
    return result


# 274. Функция для нахождения чисел, которые являются результатами разности чисел в списках
def find_difference_between_lists(lst1, lst2):
    result = [a - b for a in lst1 for b in lst2]
    if not result:
        return None
    return result


# 275. Функция для нахождения чисел, которые присутствуют в одном из списков, но не в обоих
def find_unique_in_one_list_not_both(lst1, lst2):
    result = [x for x in lst1 if x not in lst2] + [x for x in lst2 if x not in lst1]
    if not result:
        return None
    return result


# 276. Функция для нахождения чисел, которые являются четными и делятся на 3
def find_even_and_divisible_by_3(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            if num % 3 == 0:
                result.append(num)
    if not result:
        return None
    return result


# 277. Функция для нахождения чисел, которые являются квадратами, но не делятся на 5
def find_squares_not_divisible_by_5(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num:
            if num % 5 != 0:
                result.append(num)
    if not result:
        return None
    return result


# 278. Функция для нахождения чисел, которые делятся на 7 и на 8, но не на 56
def find_divisible_by_7_and_8_not_56_2(lst):
    result = []
    for num in lst:
        if num % 7 == 0:
            if num % 8 == 0:
                if num % 56 != 0:
                    result.append(num)
    if not result:
        return None
    return result


# 279. Функция для нахождения чисел, которые присутствуют в списке и кортежах
def find_in_list_and_tuple(lst, tpl):
    result = []
    for num in lst:
        if num in tpl:
            result.append(num)
    if not result:
        return None
    return result


# 280. Функция для нахождения чисел, которые являются суммой двух чисел, но не делятся на 4
def find_sum_of_two_not_divisible_by_4(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i] + lst[j]) % 4 != 0:
                result.append(lst[i] + lst[j])
    if not result:
        return None
    return result
