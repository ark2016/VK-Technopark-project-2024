# 961. Функция для нахождения строк, длина которых меньше заданного числа в списке и словаре
def find_short_strings_2(lst, d, length):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if isinstance(item, str) and len(item) < length:
            result.append(item)
    for value in d.values():
        if isinstance(value, str) and len(value) < length:
            result.append(value)
    return tuple(result) if result else None


# 962. Функция для нахождения максимального числа среди значений словаря и элементов списка
def find_max_in_dict_and_list(lst, d):
    if not lst or not d:
        return None
    max_list_value = max(lst)
    max_dict_value = max(d.values())
    return max(max_list_value, max_dict_value)


# 963. Функция для создания словаря, где ключи — это элементы множества, а значения — длина строки ключа
def create_length_dict_from_set_2(s):
    if not s:
        return None
    length_dict = {}
    for item in s:
        length_dict[item] = len(str(item))
    return length_dict if length_dict else None


# 964. Функция для подсчёта, сколько раз встречаются элементы в списке и словаре
def count_elements_in_list_and_dict(lst, d):
    if not lst or not d:
        return None
    count_dict = {}
    for item in lst + list(d.values()):
        count_dict[item] = count_dict.get(item, 0) + 1
    return count_dict if count_dict else None


# 965. Функция для нахождения общих значений между множеством и кортежем
def find_common_in_set_and_tuple(s, t):
    if not s or not t:
        return None
    result = s.intersection(t)
    return tuple(result) if result else None


# 966. Функция для нахождения чисел, которые содержат хотя бы одну цифру из другого числа
def find_numbers_with_digit(lst, num):
    if not lst:
        return None
    result = []
    str_num = str(num)
    for item in lst:
        if any(digit in str(item) for digit in str_num):
            result.append(item)
    return tuple(result) if result else None


# 967. Функция для создания множества всех нечётных чисел, которые присутствуют и в списке, и в словаре
def find_odd_numbers_in_both(lst, d):
    if not lst or not d:
        return None
    odd_set = set()
    for item in lst:
        if item % 2 != 0 and item in d:
            odd_set.add(item)
    return odd_set if odd_set else None


# 968. Функция для нахождения чисел из списка, которые не присутствуют в словаре
def find_numbers_not_in_dict(lst, d):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if item not in d:
            result.append(item)
    return tuple(result) if result else None


# 969. Функция для нахождения уникальных элементов в списке, кортежах и множествах
def find_unique_elements_9(lst, t, s):
    if not lst or not t or not s:
        return None
    unique_elements = set(lst).union(set(t)).union(s)
    return tuple(unique_elements) if unique_elements else None


# 970. Функция для нахождения всех чисел в списке, которые делятся на все числа в множестве
def find_numbers_divisible_by_all(lst, s):
    if not lst or not s:
        return None
    result = []
    for item in lst:
        if all(item % i == 0 for i in s):
            result.append(item)
    return tuple(result) if result else None


# 971. Функция для создания множества, которое объединяет все нечётные числа из списка и множества
def create_odd_number_set(lst, s):
    if not lst or not s:
        return None
    odd_set = set()
    for item in lst:
        if item % 2 != 0:
            odd_set.add(item)
    for item in s:
        if item % 2 != 0:
            odd_set.add(item)
    return odd_set if odd_set else None


# 972. Функция для нахождения всех чисел, которые находятся в обеих коллекциях (списке и словаре)
def find_numbers_in_list_and_dict(lst, d):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if item in d.values():
            result.append(item)
    return tuple(result) if result else None


# 973. Функция для подсчёта уникальных элементов в списке и словаре
def count_unique_elements_in_list_and_dict(lst, d):
    if not lst or not d:
        return None
    result = set(lst).union(set(d.values()))
    return len(result) if result else None


# 974. Функция для создания словаря, где ключи — это элементы множества, а значения — их квадраты
def create_square_dict_from_set(s):
    if not s:
        return None
    square_dict = {}
    for item in s:
        square_dict[item] = item ** 2
    return square_dict if square_dict else None


# 975. Функция для создания списка, в котором каждый элемент — это результат вычисления произведения всех чисел из словаря
def create_product_list_from_dict(d):
    if not d:
        return None
    product_list = []
    for key, value in d.items():
        product = 1
        for num in value:
            product *= num
        product_list.append(product)
    return product_list if product_list else None


# 976. Функция для нахождения всех строк из списка и множества, которые содержат хотя бы одну цифру
def find_strings_with_digit(lst, s):
    if not lst or not s:
        return None
    result = []
    for item in lst:
        if isinstance(item, str) and any(char.isdigit() for char in item):
            result.append(item)
    for item in s:
        if isinstance(item, str) and any(char.isdigit() for char in item):
            result.append(item)
    return tuple(result) if result else None


# 977. Функция для нахождения чисел, которые встречаются и в списке, и в кортеже, и в множестве
def find_common_numbers(lst, t, s):
    if not lst or not t or not s:
        return None
    common = set(lst).intersection(t, s)
    return tuple(common) if common else None


# 978. Функция для создания множества, состоящего из всех строк, длина которых меньше заданного числа
def create_set_of_short_strings(lst, max_len):
    if not lst:
        return None
    result = set()
    for item in lst:
        if isinstance(item, str) and len(item) < max_len:
            result.add(item)
    return result if result else None


# 979. Функция для нахождения строк, длина которых больше средней длины всех строк в списке
def find_long_strings_2(lst):
    if not lst:
        return None
    avg_length = sum(len(item) for item in lst) / len(lst)
    result = []
    for item in lst:
        if len(item) > avg_length:
            result.append(item)
    return tuple(result) if result else None


# 980. Функция для нахождения чисел, которые находятся в кортеже, но отсутствуют в словаре
def find_numbers_in_tuple_not_in_dict(t, d):
    if not t or not d:
        return None
    result = []
    for item in t:
        if item not in d:
            result.append(item)
    return tuple(result) if result else None
