# 501. Функция для нахождения всех простых чисел в диапазоне от 1 до X
def prime_numbers_up_to_x(x):
    if x < 2:
        return None
    primes = []
    for num in range(2, x + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


# 502. Функция для вычисления факториала числа
def factorial_of_number(n):
    if n < 0:
        return None
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


# 503. Функция для подсчёта всех слов в строке
def count_words_in_string(s):
    if not s:
        return None
    return len(s.split())


# 504. Функция для нахождения всех индексов вхождения элемента в список
def find_all_indices_of_element(lst, element):
    if not lst:
        return None
    indices = [i for i, x in enumerate(lst) if x == element]
    if not indices:
        return None
    return indices


# 505. Функция для нахождения всех чисел, которые являются квадратами из списка
def square_numbers_from_list(lst):
    if not lst:
        return None
    squares = [x for x in lst if (x ** 0.5).is_integer()]
    if not squares:
        return None
    return squares


# 506. Функция для извлечения всех чисел, которые больше среднего значения
def greater_than_average(lst):
    if not lst:
        return None
    average = sum(lst) / len(lst)
    result = [x for x in lst if x > average]
    if not result:
        return None
    return result


# 507. Функция для сортировки списка строк по длине
def sort_strings_by_length(lst):
    if not lst:
        return None
    return sorted(lst, key=len)


# 508. Функция для нахождения суммы всех чисел в списке
def sum_of_elements(lst):
    if not lst:
        return None
    return sum(lst)


# 509. Функция для нахождения максимальной строки по длине из списка строк
def longest_string(lst):
    if not lst:
        return None
    return max(lst, key=len)


# 510. Функция для нахождения разницы между двумя множествами
def difference_between_sets(set1, set2):
    if not set1 or not set2:
        return None
    return set1 - set2


# 511. Функция для нахождения всех элементов, которые присутствуют в одном из двух списков
def union_of_lists(lst1, lst2):
    if not lst1 and not lst2:
        return None
    return sorted(list(set(lst1) | set(lst2)))


# 512. Функция для нахождения всех элементов, которые присутствуют в обоих списках
def intersection_of_lists_3(lst1, lst2):
    if not lst1 and not lst2:
        return None
    return sorted(list(set(lst1) & set(lst2)))


# 513. Функция для проверки, является ли строка цифрой
def is_digit(s):
    if not s:
        return None
    return s.isdigit()


# 514. Функция для извлечения всех буквенных символов из строки
def extract_letters_from_string(s):
    if not s:
        return None
    result = ''.join([ch for ch in s if ch.isalpha()])
    return result


# 515. Функция для нахождения всех элементов, которые являются строками в списке
def find_all_strings_in_list(lst):
    if not lst:
        return None
    return [x for x in lst if isinstance(x, str)]


# 516. Функция для проверки, все ли элементы в списке уникальны
def all_unique(lst):
    if not lst:
        return None
    return len(lst) == len(set(lst))


# 517. Функция для объединения всех элементов строки в единую строку с разделителями
def join_elements_with_separator(lst, separator):
    if not lst:
        return None
    return separator.join(lst)


# 518. Функция для нахождения разницы между двумя списками (без повторений)
def difference_between_lists(lst1, lst2):
    if not lst1 and not lst2:
        return None
    return sorted(list(set(lst1) - set(lst2)))


# 519. Функция для подсчёта всех вхождений подстроки в строку без пересечения
def count_non_overlapping_substring(s, substring):
    if not s or not substring:
        return None
    count = 0
    i = 0
    while i < len(s):
        i = s.find(substring, i)
        if i == -1:
            break
        count += 1
        i += len(substring)
    return count


# 520. Функция для нахождения всех слов, которые начинаются с определенной буквы
def find_words_starting_with(s, letter):
    if not s or not letter:
        return None
    words = s.split()
    result = [word for word in words if word[0].lower() == letter.lower()]
    return result if result else None
