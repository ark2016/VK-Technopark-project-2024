# 1181. Функция для нахождения чисел, которые равны произведению чисел одного списка на индексы второго, делённых на их квадраты
def multiply_by_index_divided_by_square(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2) and i != 0:
            result.append((lst1[i] * lst2[i]) / (i ** 2))
    if not result:
        return None
    return result


# 1182. Функция для нахождения чисел, которые равны разности всех чисел первого списка и произведений всех чисел из второго, умноженных на индексы
def diff_and_product_multiplied_by_index(lst1, lst2):
    result = []
    product_lst2 = 1
    for num in lst2:
        product_lst2 *= num
    for i, num in enumerate(lst1):
        result.append(num - (product_lst2 * i))
    if not result:
        return None
    return result


# 1183. Функция для нахождения чисел, которые равны произведению всех элементов одного списка и разности всех чисел другого
def multiply_by_diff_of_all_lists(lst1, lst2):
    if not lst1 or not lst2:
        return None
    result = []
    total_diff = sum(lst1) - sum(lst2)
    for num in lst1:
        result.append(num * total_diff)
    return result


# 1184. Функция для нахождения чисел, которые являются результатом возведения элементов первого списка в степень их индексов в другом списке
def power_by_index_v2(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append(lst1[i] ** lst2[i])
    if not result:
        return None
    return result


# 1185. Функция для нахождения чисел, которые делятся на 2 и на 5, но не на 12, и вычисление их произведения
def find_divisible_by_2_and_5_not_12_and_multiply(lst):
    result = []
    product = 1
    for num in lst:
        if num % 2 == 0 and num % 5 == 0 and num % 12 != 0:
            result.append(num)
            product *= num
    if not result:
        return None
    return product


# 1186. Функция для нахождения чисел, которые равны разности всех чисел из одного списка и произведений элементов другого, с учётом их индексов
def diff_and_product_with_index(lst1, lst2):
    if not lst1 or not lst2:
        return None
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append(lst1[i] - (lst2[i] * i))
    return result


# 1187. Функция для нахождения чисел, которые являются разностью всех чисел первого списка и разности всех чисел второго списка, умноженных на их индексы
def diff_of_all_and_index_product(lst1, lst2):
    if not lst1 or not lst2:
        return None
    result = []
    total_diff_lst2 = sum(lst2) - sum(lst1)
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append(lst1[i] - (total_diff_lst2 * i))
    return result


# 1188. Функция для нахождения чисел, которые равны произведению всех чисел из одного списка и разности всех чисел второго списка
def multiply_and_diff_of_lists_v2(lst1, lst2):
    if not lst1 or not lst2:
        return None
    result = []
    total_diff = sum(lst1) - sum(lst2)
    for num in lst1:
        result.append(num * total_diff)
    return result


# 1189. Функция для нахождения чисел, которые являются результатом разности произведений элементов первого списка и их индексов
def diff_of_product_and_index_v3(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] * lst2[i]) - (i ** 2))
    if not result:
        return None
    return result


# 1190. Функция для нахождения значений, которые равны разности значений одинаковых ключей из двух словарей
def diff_of_values_in_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2:
            result.append(dict1[key] - dict2[key])
    if not result:
        return None
    return result


# 1191. Функция для нахождения ключей, которые присутствуют в обоих словарях, но только если их значения больше 10
def find_common_keys_with_values_gt_10(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2 and dict1[key] > 10 and dict2[key] > 10:
            result.append(key)
    if not result:
        return None
    return result


# 1192. Функция для нахождения значений, которые равны произведению значений одного словаря и их индексов в другом
def multiply_values_by_index_in_other_dict(dict1, dict2):
    result = []
    for i, key in enumerate(dict1):
        if key in dict2:
            result.append(dict1[key] * dict2.get(key, 0) * i)
    if not result:
        return None
    return result


# 1193. Функция для нахождения ключей, у которых значения из первого словаря больше значений из второго
def find_keys_with_value_greater_in_first_dict(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2 and dict1[key] > dict2[key]:
            result.append(key)
    if not result:
        return None
    return result


# 1194. Функция для нахождения ключей, значения которых в обоих словарях совпадают
def find_keys_with_equal_values_in_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2 and dict1[key] == dict2[key]:
            result.append(key)
    if not result:
        return None
    return result


# 1195. Функция для нахождения значений, которые равны разности значений одного словаря и значения того же ключа в другом словаре
def find_value_diff_between_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2:
            result.append(dict1[key] - dict2[key])
    if not result:
        return None
    return result


# 1196. Функция для нахождения значений, которые являются результатом умножения значений одинаковых ключей из двух словарей
def multiply_values_in_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2:
            result.append(dict1[key] * dict2[key])
    if not result:
        return None
    return result


# 1197. Функция для нахождения ключей, которые присутствуют в обоих словарях, но значения которых делятся на 3
def find_keys_with_values_divisible_by_3(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2 and dict1[key] % 3 == 0 and dict2[key] % 3 == 0:
            result.append(key)
    if not result:
        return None
    return result


# 1198. Функция для нахождения ключей, у которых значения из первого словаря меньше значений из второго, но больше 5
def find_keys_with_value_range_in_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2 and dict2[key] > dict1[key] > 5:
            result.append(key)
    if not result:
        return None
    return result


# 1199. Функция для сортировки массива по убыванию с использованием пузырьковой сортировки
def bubble_sort_descending(arr):
    result = arr[:]
    n = len(result)
    for i in range(n):
        for j in range(0, n-i-1):
            if result[j] < result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
    if not result:
        return None
    return result


# 1200. Функция для сортировки массива по возрастанию с использованием сортировки вставками
def insertion_sort_ascending(arr):
    result = arr[:]
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and key < result[j]:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    if not result:
        return None
    return result
