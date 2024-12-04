# 241. Функция для нахождения чисел, которые являются кратными 6, но не на 12
def find_multiples_of_6_not_12(lst):
    result = []
    for num in lst:
        if num % 6 == 0 and num % 12 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 242. Функция для нахождения чисел, которые являются чётными и не делятся на 5
def find_even_not_divisible_by_5(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 243. Функция для нахождения чисел, которые являются квадратами нечётных чисел, но не делятся на 3
def find_squares_of_odd_not_divisible_by_3(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0 and num % 3 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 244. Функция для нахождения всех чисел, которые являются делителями 50, но не являются простыми
def find_divisors_of_50_not_prime(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        if 50 % num == 0 and not is_prime(num):
            result.append(num)
    if not result:
        return None
    return result


# 245. Функция для нахождения чисел, которые делятся на 3 и на 4, но не на 6
def find_divisible_by_3_and_4_not_7(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 4 == 0 and num % 7 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 246. Функция для нахождения чисел, которые являются пересечением двух множеств
def find_intersection_of_sets(lst1, lst2):
    result = set(lst1) & set(lst2)
    if not result:
        return None
    return sorted(list(result))


# 247. Функция для нахождения чисел, которые присутствуют в одном из двух списков, но не в обоих
def find_symmetric_difference(lst1, lst2):
    result = set(lst1) ^ set(lst2)
    if not result:
        return None
    return sorted(list(result))


# 248. Функция для нахождения чисел, которые являются ключами в одном словаре и значениями в другом
def find_keys_in_dicts(dict1, dict2):
    result = [key for key in dict1 if dict1[key] in dict2]
    if not result:
        return None
    return result


# 249. Функция для нахождения чисел, которые присутствуют в списке, но не в кортеже
def find_in_list_not_in_tuple(lst, tpl):
    result = [x for x in lst if x not in tpl]
    if not result:
        return None
    return result


# 250. Функция для нахождения чисел, которые являются парами, где первое число больше второго
def find_pairs_with_first_greater(lst):
    result = [(a, b) for a in lst for b in lst if a > b]
    if not result:
        return None
    return result


# 251. Функция для нахождения чисел, которые являются кортежами, но не содержат отрицательных чисел
def find_tuples_without_negatives(lst):
    result = [tpl for tpl in lst if all(x >= 0 for x in tpl)]
    if not result:
        return None
    return result


# 252. Функция для нахождения чисел, которые присутствуют в словаре как ключи, но не имеют чётных значений
def find_keys_with_odd_values(dict_data):
    result = [key for key, value in dict_data.items() if value % 2 != 0]
    if not result:
        return None
    return result


# 253. Функция для нахождения чисел, которые являются произведением двух чисел, но не делятся на 2
def find_product_of_two_not_divisible_by_2(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            product = lst[i] * lst[j]
            if product % 2 != 0:
                result.append(product)
    if not result:
        return None
    return result


# 254. Функция для нахождения чисел, которые являются элементами множества, но не присутствуют в списке
def find_in_set_not_in_list(s, lst):
    result = sorted(list(s - set(lst)))
    if not result:
        return None
    return result


# 255. Функция для нахождения чисел, которые присутствуют в словаре как ключи, но не делятся на 3
def find_keys_not_divisible_by_3(dict_data):
    result = [key for key in dict_data if key % 3 != 0]
    if not result:
        return None
    return result


# 256. Функция для нахождения чисел, которые встречаются в двух списках и их сумма делится на 4
def find_numbers_with_sum_divisible_by_4(lst1, lst2):
    result = []
    for num1 in lst1:
        for num2 in lst2:
            if (num1 + num2) % 4 == 0:
                result.append((num1, num2))
    if not result:
        return None
    return result


# 257. Функция для нахождения чисел, которые встречаются только в одном из двух списков
def find_unique_in_one_list(lst1, lst2):
    result = list(set(lst1) ^ set(lst2))
    if not result:
        return None
    return result


# 258. Функция для нахождения чисел, которые являются парами, где сумма элементов делится на 5
def find_pairs_with_sum_divisible_by_5(lst):
    result = [(a, b) for a in lst for b in lst if (a + b) % 5 == 0]
    if not result:
        return None
    return result


# 259. Функция для нахождения чисел, которые являются кортежами, но не содержат чётных чисел
def find_tuples_without_even_numbers(lst):
    result = [tpl for tpl in lst if all(x % 2 != 0 for x in tpl)]
    if not result:
        return None
    return result


# 260. Функция для нахождения чисел, которые являются целыми числами в строках
def find_integers_in_strings(lst):
    result = []
    for s in lst:
        try:
            num = int(s)
            result.append(num)
        except ValueError:
            continue
    if not result:
        return None
    return result
