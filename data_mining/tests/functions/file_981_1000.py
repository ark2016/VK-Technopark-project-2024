# 981. Функция для нахождения элементов, которые встречаются в списке, но не в множестве и словаре
def find_in_list_not_in_set_and_dict(lst, s, d):
    if not lst or not s or not d:
        return None
    result = []
    for item in lst:
        if item not in s and item not in d.values():
            result.append(item)
    return tuple(result) if result else None


# 982. Функция для нахождения максимальных элементов из списка и словаря
def find_max_values(lst, d):
    if not lst or not d:
        return None
    max_lst = max(filter(lambda x: isinstance(x, (int, float)), lst), default=None)
    max_dict = max(filter(lambda x: isinstance(x, (int, float)), d.values()), default=None)
    if max_lst is None or max_dict is None:
        return None
    return max(max_lst, max_dict)


# 983. Функция для нахождения всех элементов из множества, которые не присутствуют в словаре
def find_in_set_not_in_dict(s, d):
    if not s or not d:
        return None
    result = []
    for item in s:
        if item not in d:
            result.append(item)
    return tuple(sorted(result)) if result else None


# 984. Функция для создания словаря, где ключи — это строки из множества, а значения — длина строки
def create_string_length_dict(s):
    if not s:
        return None
    string_length_dict = {}
    for item in s:
        if isinstance(item, str):
            string_length_dict[item] = len(item)
    return string_length_dict if string_length_dict else None


# 985. Функция для создания множества, которое содержит уникальные элементы из списка и множества
def create_unique_set_from_list_and_set(lst, s):
    if not lst or not s:
        return None
    unique_set = set()
    for item in lst:
        unique_set.add(item)
    for item in s:
        unique_set.add(item)
    return sorted(unique_set) if unique_set else None


# 986. Функция для нахождения всех чисел из списка и словаря, которые являются чётными
def find_even_numbers_in_list_and_dict(lst, d):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if item % 2 == 0:
            result.append(item)
    for value in d.values():
        if value % 2 == 0:
            result.append(value)
    return tuple(result) if result else None


# 987. Функция для создания словаря, где ключи — это строки, а значения — длины строк, встречающихся и в списке, и в множестве
def create_length_dict_from_strings_in_both(lst, s):
    if not lst or not s:
        return None
    length_dict = {}
    for item in lst:
        if isinstance(item, str) and item in s:
            length_dict[item] = len(item)
    return length_dict if length_dict else None


# 988. Функция для нахождения строк в списке, которые содержат хотя бы один символ, присутствующий в другом списке
def find_strings_with_common_characters(lst1, lst2):
    if not lst1 or not lst2:
        return None
    result = []
    for item in lst1:
        if isinstance(item, str):
            for char in item:
                if any(char in s for s in lst2 if isinstance(s, str)):
                    result.append(item)
                    break
    return tuple(result) if result else None


# 989. Функция для нахождения чисел в словаре, значения которых больше, чем в списке
def find_values_greater_than_in_list(d, lst):
    if not d or not lst:
        return None
    result = []
    for value in d.values():
        for item in lst:
            if value > item:
                result.append(value)
                break
    return tuple(result) if result else None


# 990. Функция для нахождения всех чисел, которые присутствуют и в списке, и в множестве
def find_numbers_in_both_list_and_set(lst, s):
    if not lst or not s:
        return None
    result = []
    for item in lst:
        if item in s:
            result.append(item)
    return tuple(result) if result else None


# 991. Функция для нахождения элементов из списка, которые не встречаются в других структурах данных
def find_elements_not_in_other_structures(lst, s, d, t):
    if not lst or not s or not d or not t:
        return None
    result = []
    for item in lst:
        if item not in s and item not in d.values() and item not in t:
            result.append(item)
    return tuple(result) if result else None


# 992. Функция для нахождения чисел, которые меньше минимального значения в списке и больше максимального в словаре
def find_numbers_between_min_in_list_and_max_in_dict(lst, d):
    if not lst or not d:
        return None
    min_lst = min(lst)
    max_dict = max(d.values())
    result = []
    for item in lst:
        if min_lst < item < max_dict:
            result.append(item)
    return tuple(result) if result else None


# 993. Функция для создания множества из всех строк, длина которых больше заданного значения
def create_set_of_long_strings(lst, min_length):
    if not lst:
        return None
    long_strings = set()
    for item in lst:
        if isinstance(item, str) and len(item) > min_length:
            long_strings.add(item)
    return sorted(long_strings) if long_strings else None


# 994. Функция для нахождения всех чисел в словаре, которые меньше средней величины всех значений в словаре
def find_numbers_less_than_avg_in_dict(d):
    if not d:
        return None
    avg = sum(d.values()) / len(d)
    result = []
    for value in d.values():
        if value < avg:
            result.append(value)
    return tuple(result) if result else None


# 995. Функция для подсчёта количества строк, длина которых больше средней длины всех строк в списке
def count_strings_longer_than_avg(lst):
    if not lst:
        return None
    avg_length = sum(len(item) for item in lst if isinstance(item, str)) / len(lst)
    count = 0
    for item in lst:
        if isinstance(item, str) and len(item) > avg_length:
            count += 1
    return count if count > 0 else None


# 996. Функция для нахождения элементов, которые одновременно присутствуют в множестве и кортеже
def find_common_in_set_and_tuple_2(s, t):
    if not s or not t:
        return None
    result = []
    for item in s:
        if item in t:
            result.append(item)
    return tuple(result) if result else None


# 997. Функция для создания словаря, где ключи — это строки, а значения — их длина, если строка есть в списке
def create_length_dict_from_strings_in_list(lst):
    if not lst:
        return None
    length_dict = {}
    for item in lst:
        if isinstance(item, str):
            length_dict[item] = len(item)
    return length_dict if length_dict else None


# 998. Функция для нахождения чисел, которые больше максимума в списке и меньше минимума в словаре
def find_numbers_between_max_in_list_and_min_in_dict(lst, d):
    if not lst or not d:
        return None
    max_lst = max(lst)
    min_dict = min(d.values())
    result = []
    for item in lst:
        if min_dict < item < max_lst:
            result.append(item)
    return tuple(result) if result else None


# 999. Функция для нахождения строк, содержащих хотя бы одну букву из множества
def find_strings_with_letter_from_set(lst, s):
    if not lst or not s:
        return None
    result = []
    for item in lst:
        if isinstance(item, str) and any(char in s for char in item):
            result.append(item)
    return tuple(result) if result else None


# 1000. Функция для нахождения чисел, которые присутствуют в списке, но не в словаре
def find_numbers_in_list_not_in_dict(lst, d):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if item not in d:
            result.append(item)
    return tuple(result) if result else None
