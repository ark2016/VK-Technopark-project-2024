# 661. Функция для проверки, является ли строка числом с плавающей точкой
def is_float_5(s):
    try:
        float(s)
        return "." in s
    except ValueError:
        return False


# 662. Функция для извлечения всех слов из строки, содержащих цифры
def extract_words_with_numbers(s):
    if not s:
        return []
    words = s.split()
    result = []
    for word in words:
        if any(char.isdigit() for char in word):
            result.append(word)
    return result


# 663. Функция для нахождения наименьшего общего кратного двух чисел
def lcm_4(a, b):
    if a == 0 or b == 0:
        return 0
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1


# 664. Функция для объединения двух списков с уникальными значениями
def merge_unique_lists_2(arr1, arr2):
    result = arr1.copy()
    for el in arr2:
        if el not in result:
            result.append(el)
    return result


# 665. Функция для возврата индекса элемента в списке, если он существует, или None
def find_index_of_element(arr, element):
    if not arr:
        return None
    for i, el in enumerate(arr):
        if el == element:
            return i
    return None


# 666. Функция для подсчета всех слов в строке с учетом разделителей
def count_words_in_string_with_delimiters(s, delimiters=" "):
    if not s:
        return 0
    for delimiter in delimiters:
        s = s.replace(delimiter, " ")
    return len(s.split())


# 667. Функция для нахождения всех чисел больше среднего в списке
def greater_than_average_6(arr):
    if not arr:
        return []
    avg = sum(arr) / len(arr)
    return [x for x in arr if x > avg]


# 668. Функция для объединения словаря и списка кортежей в новый словарь
def merge_dict_and_tuple(lst, d):
    if not lst:
        return d
    for key, value in lst:
        d[key] = value
    return d


# 669. Функция для вычисления суммы всех чисел в строке
def sum_numbers_in_string_2(s):
    if not s:
        return 0
    total = 0
    temp = ""
    for char in s:
        if char.isdigit():
            temp += char
        elif temp:
            total += int(temp)
            temp = ""
    if temp:
        total += int(temp)
    return total


# 670. Функция для нахождения числа, которое не встречается в двух списках
def find_missing_number(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    missing = set1 - set2
    if missing:
        return sorted(missing, reverse=True)[0]
    return None


# 671. Функция для слияния двух строк с их чередующимися символами
def alternate_merge(s1, s2):
    if not s1:
        return s2
    if not s2:
        return s1
    result = []
    for c1, c2 in zip(s1, s2):
        result.append(c1)
        result.append(c2)
    result.extend(s1[len(s2):])
    result.extend(s2[len(s1):])
    return ''.join(result)


# 672. Функция для проверки, все ли элементы в списке больше заданного числа
def are_all_greater_than(arr, number):
    if not arr:
        return False
    return all(x > number for x in arr)


# 673. Функция для поиска и замены первого вхождения подстроки в строке
def replace_first_occurrence(s, old, new):
    if old not in s:
        return s
    index = s.find(old)
    return s[:index] + new + s[index + len(old):]


# 674. Функция для получения уникальных элементов из списка, исключая те, которые повторяются
def get_unique_elements(arr):
    if not arr:
        return []
    count = {}
    for el in arr:
        count[el] = count.get(el, 0) + 1
    return [key for key, value in count.items() if value == 1]


# 675. Функция для нахождения минимального четного числа в списке
def min_even_number(arr):
    if not arr:
        return None
    even_numbers = [x for x in arr if x % 2 == 0]
    if even_numbers:
        return min(even_numbers)
    return None


# 676. Функция для преобразования числа в строку с ведущими нулями
def number_to_string_with_leading_zeros(n, width):
    return str(n).zfill(width)


# 677. Функция для преобразования списка чисел в строку с разделением на запятую
def list_to_comma_separated_string(arr):
    if not arr:
        return ""
    return ", ".join(map(str, arr))


# 678. Функция для проверки, является ли строка правильным числом (целым или с плавающей точкой)
def is_valid_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# 679. Функция для подсчета гласных букв в строке
def count_vowels_2(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


# 680. Функция для вычисления произведения всех чисел в строке
def product_of_numbers_in_string(s):
    if not s:
        return 1
    total = 1
    temp = ""
    for char in s:
        if char.isdigit():
            temp += char
        elif temp:
            total *= int(temp)
            temp = ""
    if temp:
        total *= int(temp)
    return total
