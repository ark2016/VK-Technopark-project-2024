# 761. Функция для выбора самой короткой строки, которая начинается с цифры
def choose_shortest_string_starting_with_digit(*strings):
    for s in strings:
        if s[0].isdigit():
            return s
    return None


# 762. Функция для выбора строки, которая является анаграммой другой строки
def choose_anagram_of(string, *strings):
    sorted_string = sorted(string)
    for s in strings:
        if sorted(s) == sorted_string:
            return s
    return None


# 763. Функция для выбора наименьшего числа, которое больше заданного
def choose_smallest_greater_than(value, *nums):
    smallest = None
    for num in nums:
        if num > value:
            if smallest is None or num < smallest:
                smallest = num
    return smallest if smallest is not None else None


# 764. Функция для выбора первого слова, которое имеет четное количество букв
def choose_first_even_length_word(*words):
    for word in words:
        if len(word) % 2 == 0:
            return word
    return None


# 765. Функция для выбора строки, длина которой больше средней длины всех строк
def choose_longer_than_average(*strings):
    avg_length = sum(len(s) for s in strings) / len(strings) if strings else 0
    for s in strings:
        if len(s) > avg_length:
            return s
    return None


# 766. Функция для выбора строки, которая содержит только буквы
def choose_string_with_only_letters(*strings):
    for s in strings:
        if s.isalpha():
            return s
    return None


# 767. Функция для выбора самого старого возраста, который меньше 30
def choose_oldest_under_30(*ages):
    oldest = None
    for age in ages:
        if age < 30:
            if oldest is None or age > oldest:
                oldest = age
    return oldest if oldest is not None else None


# 768. Функция для выбора числа, которое является кратным 4, но не кратным 5
def choose_multiple_of_4_not_5(arr):
    for num in arr:
        if num % 4 == 0 and num % 5 != 0:
            return num
    return None


# 769. Функция для выбора строки, длина которой кратна 3
def choose_string_length_divisible_by_3(*strings):
    for s in strings:
        if len(s) % 3 == 0:
            return s
    return None


# 770. Функция для выбора наименьшего числа, которое является четным и больше 10
def choose_smallest_even_greater_than_10(*nums):
    smallest = None
    for num in nums:
        if num % 2 == 0 and num > 10:
            if smallest is None or num < smallest:
                smallest = num
    return smallest if smallest is not None else None


# 771. Функция для выбора первого числа, которое делится на 2 и 5
def choose_first_divisible_by_2_and_5(arr):
    for num in arr:
        if num % 2 == 0 and num % 5 == 0:
            return num
    return None


# 772. Функция для выбора самой длинной строки, которая не начинается с цифры
def choose_longest_non_digit_starting_string(*strings):
    for s in strings:
        if not s[0].isdigit():
            return s
    return None


# 773. Функция для выбора первого слова, которое состоит только из заглавных букв
def choose_first_all_uppercase_word(*words):
    for word in words:
        if word.isupper():
            return word
    return None


# 774. Функция для выбора самого младшего возраста среди людей старше 50 лет
def choose_youngest_over_50(*ages):
    youngest = None
    for age in ages:
        if age > 50:
            if youngest is None or age < youngest:
                youngest = age
    return youngest if youngest is not None else None


# 775. Функция для выбора наибольшего числа, которое делится на 3, но не на 2
def choose_largest_multiple_of_3_not_2(arr):
    largest = None
    for num in arr:
        if num % 3 == 0 and num % 2 != 0:
            if largest is None or num > largest:
                largest = num
    return largest if largest is not None else None


# 776. Функция для выбора строки, содержащей хотя бы одну заглавную букву и цифру
def choose_string_with_uppercase_and_digit(*strings):
    for s in strings:
        if any(char.isdigit() for char in s) and any(char.isupper() for char in s):
            return s
    return None


# 777. Функция для выбора первого четного числа, которое меньше 50
def choose_first_even_less_than_50(arr):
    for num in arr:
        if num % 2 == 0 and num < 50:
            return num
    return None


# 778. Функция для выбора самой короткой строки, которая не содержит пробела
def choose_shortest_no_space_string_3(*strings):
    for s in strings:
        if " " not in s:
            return s
    return None


# 779. Функция для выбора строки, которая является повторением другого слова
def choose_repeated_string(*strings):
    for s in strings:
        if s == s * 2:
            return s
    return None


# 780. Функция для выбора числа, которое больше 0, но не больше 100
def choose_number_in_range_0_100(*nums):
    for num in nums:
        if 0 < num <= 100:
            return num
    return None
