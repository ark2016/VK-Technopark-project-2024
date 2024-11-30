# 721. Функция для выбора минимального элемента из списка, если он четный
def choose_smallest_even_from_list(arr):
    smallest_even = None
    for num in arr:
        if num % 2 == 0:
            if smallest_even is None or num < smallest_even:
                smallest_even = num
    if smallest_even is None:
        return "No even numbers found"
    return smallest_even


# 722. Функция для выбора самого длинного слова, не начинающегося на гласную
def choose_longest_non_vowel_word(*words):
    vowels = 'aeiouAEIOU'
    longest = ""
    for word in words:
        if word[0] not in vowels:
            if len(word) > len(longest):
                longest = word
    if not longest:
        return "No word found"
    return longest


# 723. Функция для выбора наименьшего отрицательного числа
def choose_smallest_negative(*nums):
    smallest_negative = None
    for num in nums:
        if num < 0:
            if smallest_negative is None or num > smallest_negative:
                smallest_negative = num
    if smallest_negative is None:
        return "No negative numbers"
    return smallest_negative


# 724. Функция для выбора строки, которая содержит наибольшее количество цифр
def choose_string_with_most_digits(*strings):
    max_digits = 0
    chosen_string = ""
    for s in strings:
        count_digits = sum(1 for char in s if char.isdigit())
        if count_digits > max_digits:
            max_digits = count_digits
            chosen_string = s
        elif count_digits == max_digits and s > chosen_string:
            chosen_string = s
    return chosen_string


# 725. Функция для выбора наибольшего числа в пределах диапазона
def choose_largest_in_range(low, high, *nums):
    largest_in_range = None
    for num in nums:
        if low <= num <= high:
            if largest_in_range is None or num > largest_in_range:
                largest_in_range = num
    if largest_in_range is None:
        return f"No numbers in the range ({low}, {high})"
    return largest_in_range


# 726. Функция для выбора первого четного числа в списке
def choose_first_even_number(arr):
    for num in arr:
        if num % 2 == 0:
            return num
    return "No even numbers"


# 727. Функция для выбора самой короткой строки, не содержащей пробелы
def choose_shortest_no_space_string(*strings):
    shortest = None
    for s in strings:
        if ' ' not in s:
            if shortest is None or len(s) < len(shortest):
                shortest = s
    if shortest is None:
        return "No string without spaces"
    return shortest


# 728. Функция для выбора самого младшего возраста в группе
def choose_youngest_age(*ages):
    youngest = None
    for age in ages:
        if youngest is None or age < youngest:
            youngest = age
    return youngest


# 729. Функция для выбора строки с наибольшим количеством уникальных символов
def choose_string_with_most_unique_chars(*strings):
    max_unique = 0
    chosen_string = ""
    for s in strings:
        unique_chars = len(set(s))
        if unique_chars > max_unique:
            max_unique = unique_chars
            chosen_string = s
    return chosen_string


# 730. Функция для выбора первого четного числа, которое делится на 3
def choose_first_even_divisible_by_three(arr):
    for num in arr:
        if num % 2 == 0 and num % 3 == 0:
            return num
    return "No even number divisible by 3"


# 731. Функция для выбора максимального числа, которое меньше заданного
def choose_largest_less_than(value, *nums):
    largest = None
    for num in nums:
        if num < value:
            if largest is None or num > largest:
                largest = num
    if largest is None:
        return f"No numbers less than {value}"
    return largest


# 732. Функция для выбора первого числа, которое больше заданного
def choose_first_greater_than(value, *nums):
    for num in nums:
        if num > value:
            return num
    return f"No numbers greater than {value}"


# 733. Функция для выбора строки, длина которой делится на 3
def choose_string_with_length_divisible_by_three(*strings):
    for s in strings:
        if len(s) % 3 == 0:
            return s
    return "No string with length divisible by 3"


# 734. Функция для выбора самого дорогого товара в списке
def choose_most_expensive_item(*items):
    max_price = 0
    most_expensive = None
    for item in items:
        price = item['price']
        if price > max_price:
            max_price = price
            most_expensive = item
    return most_expensive if most_expensive else "No items found"


# 735. Функция для выбора строки, длина которой меньше заданного числа
def choose_string_shorter_than(length, *strings):
    for s in strings:
        if len(s) < length:
            return s
    return None


# 736. Функция для выбора первого числа, которое не делится на 2 и 3
def choose_first_not_divisible_by_2_and_3(arr):
    for num in arr:
        if num % 2 != 0 and num % 3 != 0:
            return num
    return None


# 737. Функция для выбора первого слова, в котором все буквы – гласные
def choose_word_with_only_vowels(*words):
    vowels = 'aeiouAEIOU'
    for word in words:
        if all(char in vowels for char in word):
            return word
    return None


# 738. Функция для выбора самого большого числа в списке, которое не превышает заданное значение
def choose_largest_less_than_or_equal_to(value, *nums):
    largest = None
    for num in nums:
        if num <= value:
            if largest is None or num > largest:
                largest = num
    return largest if largest is not None else None


# 739. Функция для выбора самой длинной строки, состоящей только из цифр
def choose_longest_digit_string(*strings):
    longest = None
    for s in strings:
        if s.isdigit():
            if longest is None or len(s) > len(longest):
                longest = s
    return longest if longest is not None else None


# 740. Функция для выбора самой короткой строки, в которой нет гласных
def choose_shortest_string_without_vowels(*strings):
    vowels = 'aeiouAEIOU'
    shortest = None
    for s in strings:
        if all(char not in vowels for char in s):
            if shortest is None or len(s) < len(shortest):
                shortest = s
    return shortest if shortest is not None else None
