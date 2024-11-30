# 921. Функция для нахождения чисел в словаре, которые являются простыми
def find_prime_numbers_2(d):
    if not d:
        return None
    prime_numbers = {}
    for key, value in d.items():
        if value > 1 and all(value % i != 0 for i in range(2, int(value ** 0.5) + 1)):
            prime_numbers[key] = value
    return prime_numbers if prime_numbers else None


# 922. Функция для фильтрации словаря, оставляя только те элементы, у которых значения — чётные числа
def filter_even_values(d):
    if not d:
        return None
    filtered_dict = {}
    for key, value in d.items():
        if isinstance(value, int) and value % 2 == 0:
            filtered_dict[key] = value
    return filtered_dict if filtered_dict else None


# 923. Функция для создания словаря, где ключами являются элементы списка, а значениями — их удвоенные значения
def create_double_value_dict(lst):
    if not lst:
        return None
    double_dict = {}
    for item in lst:
        double_dict[item] = item * 2
    return double_dict if double_dict else None


# 924. Функция для создания словаря с числовыми значениями, где значения кратны 7
def create_sevens_dict(lst):
    if not lst:
        return None
    sevens_dict = {}
    for item in lst:
        if item % 7 == 0:
            sevens_dict[item] = item
    return sevens_dict if sevens_dict else None


# 925. Функция для нахождения всех значений в словаре, которые равны их ключам
def find_equal_key_value_pairs(d):
    if not d:
        return None
    result = []
    for key, value in d.items():
        if key == value:
            result.append((key, value))
    return result if result else None


# 926. Функция для поиска максимального значения среди всех значений словаря
def find_max_value_in_dict_4(d):
    if not d:
        return None
    max_value = max(d.values())
    return max_value if max_value else None


# 927. Функция для создания словаря, где ключами являются элементы списка, а значениями их кубы
def create_cube_dict(lst):
    if not lst:
        return None
    cube_dict = {}
    for item in lst:
        cube_dict[item] = item ** 3
    return cube_dict if cube_dict else None


# 928. Функция для поиска строк, которые содержат больше определённого количества символов
def find_long_strings_3(d, length):
    if not d:
        return None
    result = []
    for key, value in d.items():
        if isinstance(value, str) and len(value) > length:
            result.append((key, value))
    return result if result else None


# 929. Функция для нахождения всех значений, которые являются нечётными числами
def find_odd_values(d):
    if not d:
        return None
    result = []
    for key, value in d.items():
        if isinstance(value, int) and value % 2 != 0:
            result.append((key, value))
    return result if result else None


# 930. Функция для нахождения всех чисел, которые больше среднего значения всех значений в словаре
def find_values_greater_than_average(d):
    if not d:
        return None
    avg_value = sum(d.values()) / len(d)
    result = []
    for key, value in d.items():
        if value > avg_value:
            result.append((key, value))
    return result if result else None


# 931. Функция для создания словаря, где ключи — это индексы строк из списка, а значения — это сами строки
def create_string_dict(lst):
    if not lst:
        return None
    string_dict = {}
    for i, s in enumerate(lst):
        string_dict[i] = s
    return string_dict if string_dict else None


# 932. Функция для нахождения чисел, которые больше заданного порога в словаре
def find_values_greater_than_threshold(d, threshold):
    if not d:
        return None
    result = []
    for key, value in d.items():
        if value > threshold:
            result.append((key, value))
    return result if result else None


# 933. Функция для подсчёта количества уникальных значений в словаре
def count_unique_values(d):
    if not d:
        return None
    unique_values = set(d.values())
    return len(unique_values) if unique_values else None


# 934. Функция для фильтрации словаря, оставляя только те элементы, у которых ключи являются строками
def filter_dict_with_string_keys(d):
    if not d:
        return None
    filtered_dict = {}
    for key, value in d.items():
        if isinstance(key, str):
            filtered_dict[key] = value
    return filtered_dict if filtered_dict else None


# 935. Функция для нахождения наибольшего числа в списке значений словаря
def find_max_in_values(d):
    if not d:
        return None
    max_value = max(d.values())
    return max_value if max_value else None


# 936. Функция для удаления из словаря всех элементов, где значение является пустой строкой
def remove_empty_values(d):
    if not d:
        return None
    clean_dict = {}
    for key, value in d.items():
        if value != "":
            clean_dict[key] = value
    return clean_dict if clean_dict else None


# 937. Функция для нахождения чисел, которые содержатся и в списке, и в множестве, и выводятся как кортежи
def find_common_elements_5(lst, s):
    if not lst or not s:
        return None
    common = set(lst).intersection(s)
    if not common:
        return None
    result = [(item, lst.index(item)) for item in common]
    return tuple(result) if result else None


# 938. Функция для вычисления суммы всех элементов кортежа, которые делятся на 3
def sum_of_multiples_of_3(t):
    if not t:
        return None
    total = 0
    for n in t:
        if n % 3 == 0:
            total += n
    return total if total else None


# 939. Функция для нахождения чисел, которые встречаются как в списке, так и в словаре
def find_elements_in_list_and_dict(lst, d):
    if not lst or not d:
        return None
    common_elements = []
    for item in lst:
        if item in d:
            common_elements.append(item)
    return tuple(common_elements) if common_elements else None


# 940. Функция для создания множества уникальных значений из списка, кортежа и словаря
def create_unique_set_from_multiple_sources(lst, t, d):
    if not lst or not t or not d:
        return None
    combined_set = set(lst).union(t).union(d.values())
    return combined_set if combined_set else None
