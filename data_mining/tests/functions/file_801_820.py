# 801. Функция для вычисления суммы всех чисел, делящихся на 3 или на 5, используя список
def sum_divisible_by_3_or_5(arr):
    total = 0
    for val in arr:
        if val % 3 == 0 or val % 5 == 0:
            total += val
    return total if total > 0 else None


# 802. Функция для нахождения самого большого числа в словаре
def find_max_value_in_dict(d):
    if not d:
        return None
    max_val = None
    for key, val in d.items():
        if max_val is None or val > max_val:
            max_val = val
    return max_val


# 803. Функция для нахождения числа, которое встречается в массиве более одного раза
def find_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None


# 804. Функция для нахождения минимального числа, которое не делится на 4
def find_min_not_divisible_by_4(arr):
    min_val = None
    for val in arr:
        if val % 4 != 0:
            if min_val is None or val < min_val:
                min_val = val
    return min_val if min_val is not None else None


# 805. Функция для нахождения наименьшего числа, которое делится на 7 и на 11
def find_smallest_divisible_by_7_and_11(arr):
    min_val = None
    for val in arr:
        if val % 7 == 0 and val % 11 == 0:
            if min_val is None or val < min_val:
                min_val = val
    return min_val if min_val is not None else None


# 806. Функция для нахождения первого числа, которое делится на 3, но не на 5
def find_first_divisible_by_3_not_5(arr):
    for val in arr:
        if val % 3 == 0 and val % 5 != 0:
            return val
    return None


# 807. Функция для нахождения суммы всех элементов в словаре, значения которых больше 10
def sum_values_greater_than_10_in_dict(d):
    total = 0
    for key, val in d.items():
        if val > 10:
            total += val
    return total if total > 0 else None


# 808. Функция для нахождения строки, длина которой больше заданного числа
def find_string_longer_than(length, *strings):
    for s in strings:
        if len(s) > length:
            return s
    return None


# 809. Функция для проверки, является ли строка палиндромом
def is_palindrome_6(s):
    if not s:
        return None
    reversed_s = ''
    for i in range(len(s) - 1, -1, -1):
        reversed_s += s[i]
    if s == reversed_s:
        return True
    return False


# 810. Функция для подсчета количества гласных в строке
def count_vowels_in_string(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count if count > 0 else None


# 811. Функция для поиска первого вхождения подстроки в строку
def find_first_occurrence_of_substring(s, substring):
    for i in range(len(s) - len(substring) + 1):
        if s[i:i + len(substring)] == substring:
            return i
    return None


# 812. Функция для удаления всех пробелов в строке
def remove_spaces_from_string(s):
    result = ''
    for char in s:
        if char != ' ':
            result += char
    return result if result != s else None


# 813. Функция для получения всех уникальных символов в строке
def get_unique_characters(s):
    unique_chars = set()
    for char in s:
        unique_chars.add(char)
    return ''.join(sorted(unique_chars))


# 814. Функция для инвертирования строки
def reverse_string_5(s):
    reversed_str = ''
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str


# 815. Функция для подсчета количества слов в строке
def count_words_in_string_5(s):
    words = s.split()
    return len(words) if len(words) > 0 else None


# 816. Функция для получения строки с удаленными знаками препинания
def remove_punctuation_from_string(s):
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    result = ''
    for char in s:
        if char not in punctuation:
            result += char
    return result


# 817. Функция для проверки, состоит ли строка только из цифр
def is_string_only_digits(s):
    for char in s:
        if not char.isdigit():
            return False
    return True


# 818. Функция для получения индексов всех вхождений подстроки
def find_all_occurrences_of_substring(s, substring):
    indices = []
    for i in range(len(s) - len(substring) + 1):
        if s[i:i + len(substring)] == substring:
            indices.append(i)
    return indices if indices else None


# 819. Функция для получения строки, которая является повторением самой себя
def repeat_string(s, n):
    return s * n if n > 0 else None


# 820. Функция для получения первого слова в строке
def get_first_word(s):
    if not s:
        return None
    return s.split()[0]
