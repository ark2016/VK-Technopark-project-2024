# 681. Функция для поиска всех строк в списке, содержащих хотя бы одну цифру
def find_strings_with_digits(arr):
    return [s for s in arr if any(char.isdigit() for char in s)]


# 682. Функция для вычисления числа цифр в строке
def count_digits_in_string(s):
    return sum(1 for char in s if char.isdigit())


# 683. Функция для получения каждого второго элемента в строке
def get_every_second_char(s):
    return s[::2]


# 684. Функция для фильтрации строк, содержащих хотя бы одну заглавную букву
def filter_strings_with_uppercase(arr):
    return [s for s in arr if any(char.isupper() for char in s)]


# 685. Функция для подсчета повторений каждого символа в строке, кроме пробела
def count_non_space_characters(s):
    count = {}
    for char in s:
        if char != " ":
            count[char] = count.get(char, 0) + 1
    return count


# 686. Функция для поиска строки с максимальной длиной в списке
def find_longest_string(arr):
    if not arr:
        return None
    max_length = len(arr[0])
    longest_string = arr[0]
    for string in arr[1:]:
        if len(string) > max_length:
            max_length = len(string)
            longest_string = string
    return longest_string


# 687. Функция для нахождения индекса первого четного числа в списке
def find_first_even(arr):
    if not arr:
        return None
    for i, num in enumerate(arr):
        if num % 2 == 0:
            return i
    return None


# 688. Функция для вычисления суммы всех чисел в строке
def sum_numbers_in_string_v3(s):
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
    if total == 0:
        return None
    return total


# 689. Функция для преобразования строки в список чисел (каждое число отделено пробелом)
def string_to_number_list(s):
    if not s:
        return []
    num_list = s.split()
    try:
        return [int(num) for num in num_list]
    except ValueError:
        return None


# 690. Функция для поиска максимального и минимального элемента в списке
def find_max_min(arr):
    if not arr:
        return None, None
    max_val = arr[0]
    min_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val


# 691. Функция для замены всех пробелов на подчеркивания в строке
def replace_spaces_with_underscores_5(s):
    if not s:
        return None
    result = ""
    for char in s:
        if char == " ":
            result += "_"
        else:
            result += char
    return result


# 692. Функция для удаления дубликатов из списка, не изменяя порядок
def remove_duplicates_maintain_order(arr):
    if not arr:
        return []
    seen = set()
    result = []
    for el in arr:
        if el not in seen:
            result.append(el)
            seen.add(el)
    return result


# 693. Функция для поиска первого числа в списке, которое делится на заданное число
def find_first_multiple(arr, divisor):
    if not arr or divisor == 0:
        return None
    for num in arr:
        if num % divisor == 0:
            return num
    return None


# 694. Функция для проверки, является ли строка полиндромом, игнорируя пробелы и регистр
def is_palindrome_v2(s):
    if not s:
        return False
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


# 695. Функция для получения всех четных чисел из списка
def get_even_numbers(arr):
    if not arr:
        return []
    even_numbers = []
    for num in arr:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


# 696. Функция для проверки, является ли строка числом (целым или с плавающей точкой)
def is_number_v2(s):
    if not s:
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False


# 697. Функция для подсчета всех повторяющихся элементов в списке
def count_repeating_elements(arr):
    if not arr:
        return {}
    counts = {}
    for el in arr:
        counts[el] = counts.get(el, 0) + 1
    return {key: value for key, value in counts.items() if value > 1}


# 698. Функция для извлечения уникальных слов из строки
def extract_unique_words(s):
    if not s:
        return []
    words = s.split()
    unique_words = set(words)
    return list(unique_words)


# 699. Функция для нахождения наибольшего простого числа в списке
def find_largest_prime(arr):
    if not arr:
        return None

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [x for x in arr if is_prime(x)]
    if primes:
        return max(primes)
    return None


# 700. Функция для извлечения всех цифр из строки
def extract_digits(s):
    if not s:
        return []
    digits = [int(c) for c in s if c.isdigit()]
    return digits
