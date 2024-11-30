# 901. Функция для нахождения всех чисел, которые меньше их суммы цифр
def find_numbers_less_than_digit_sum(lst):
    result = []
    for n in lst:
        if n < sum(int(digit) for digit in str(abs(n))):
            result.append(n)
    return tuple(result) if result else None


# 902. Функция для создания кортежа из чисел, которые равны сумме всех их делителей
def find_numbers_equal_to_sum_of_divisors(lst):
    result = []
    for n in lst:
        divisors = [i for i in range(1, n) if n % i == 0]
        if n == sum(divisors):
            result.append(n)
    return tuple(result) if result else None


# 903. Функция для создания кортежа чисел, которые кратны 9, но не кратны 3
def find_multiples_of_9_not_3(lst):
    result = []
    for n in lst:
        if n % 9 == 0 and n % 3 != 0:
            result.append(n)
    return tuple(result) if result else None


# 904. Функция для нахождения чисел, которые делятся на 11 и 13
def find_divisible_by_11_and_13(lst):
    result = []
    for n in lst:
        if n % 11 == 0 and n % 13 == 0:
            result.append(n)
    return tuple(result) if result else None


# 905. Функция для создания словаря, где ключами являются элементы списка, а значениями их квадраты
def create_square_dict(lst):
    if not lst:
        return None
    square_dict = {}
    for item in lst:
        square_dict[item] = item ** 2
    return square_dict if square_dict else None


# 906. Функция для нахождения минимального и максимального значений в словаре
def find_min_max_in_dict(d):
    if not d:
        return None
    min_key = min(d, key=d.get)
    max_key = max(d, key=d.get)
    return (min_key, d[min_key]), (max_key, d[max_key])


# 907. Функция для фильтрации словаря, оставляя только те ключи, которые являются строками
def filter_dict_with_strings(d):
    if not d:
        return None
    filtered_dict = {}
    for key, value in d.items():
        if isinstance(key, str):
            filtered_dict[key] = value
    return filtered_dict if filtered_dict else None


# 908. Функция для нахождения суммы значений всех числовых ключей в словаре
def sum_of_numeric_keys(d):
    if not d:
        return None
    total = 0
    for key, value in d.items():
        if isinstance(key, (int, float)):
            total += value
    return total if total else None


# 909. Функция для создания словаря, в котором ключи — это длины строк из списка, а значения — сами строки
def create_dict_from_string_lengths(lst):
    if not lst:
        return None
    length_dict = {}
    for s in lst:
        length_dict[len(s)] = s
    return length_dict if length_dict else None


# 910. Функция для удаления из словаря всех элементов с отрицательными значениями
def remove_negative_values(d):
    if not d:
        return None
    clean_dict = {}
    for key, value in d.items():
        if value >= 0:
            clean_dict[key] = value
    return clean_dict if clean_dict else None


# 911. Функция для создания словаря из двух списков: первый — ключи, второй — значения
def create_dict_from_lists(keys, values):
    if not keys or not values or len(keys) != len(values):
        return None
    result_dict = {}
    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]
    return result_dict if result_dict else None


# 912. Функция для подсчёта количества строк с одинаковыми длинами в списке
def count_strings_by_length(lst):
    if not lst:
        return None
    length_count = {}
    for s in lst:
        length_count[len(s)] = length_count.get(len(s), 0) + 1
    return length_count if length_count else None


# 913. Функция для нахождения минимального значения в словаре, в котором ключи — это числа
def find_min_value_in_dict(d):
    if not d:
        return None
    min_value = min(d.values())
    return min_value if min_value else None


# 914. Функция для создания словаря, где ключами являются индексы, а значениями элементы списка
def create_dict_from_list(lst):
    if not lst:
        return None
    index_dict = {}
    for i, value in enumerate(lst):
        index_dict[i] = value
    return index_dict if index_dict else None


# 915. Функция для нахождения всех чисел, которые встречаются более одного раза в словаре
def find_duplicates_in_dict(d):
    if not d:
        return None
    reverse_dict = {}
    for key, value in d.items():
        if value not in reverse_dict:
            reverse_dict[value] = [key]
        else:
            reverse_dict[value].append(key)
    duplicates = {value: keys for value, keys in reverse_dict.items() if len(keys) > 1}
    return duplicates if duplicates else None


# 916. Функция для подсчёта количества элементов в списке, которые равны значению по заданному ключу
def count_values_by_key(d, key):
    if not d or key not in d:
        return None
    count = 0
    for value in d.values():
        if value == d[key]:
            count += 1
    return count if count else None


# 917. Функция для поиска всех значений в словаре, которые больше заданного порога
def find_values_greater_than(d, threshold):
    if not d:
        return None
    result = []
    for key, value in d.items():
        if value > threshold:
            result.append((key, value))
    return result if result else None


# 918. Функция для создания словаря, в котором ключи — это числа, а значения — это их остатки от деления на 5
def create_remainders_dict(lst):
    if not lst:
        return None
    remainder_dict = {}
    for n in lst:
        remainder_dict[n] = n % 5
    return remainder_dict if remainder_dict else None


# 919. Функция для нахождения суммы всех числовых значений в словаре
def sum_of_dict_values(d):
    if not d:
        return None
    total = 0
    for value in d.values():
        total += value
    return total if total else None


# 920. Функция для создания словаря, где ключи — это строки, а значения — длины этих строк
def create_length_dict(lst):
    if not lst:
        return None
    length_dict = {}
    for s in lst:
        length_dict[s] = len(s)
    return length_dict if length_dict else None
