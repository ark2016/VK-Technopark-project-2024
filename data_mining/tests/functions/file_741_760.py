# 741. Функция для выбора наибольшего четного числа, которое меньше заданного
def choose_largest_even_less_than(value, *nums):
    largest = None
    for num in nums:
        if num % 2 == 0 and num < value:
            if largest is None or num > largest:
                largest = num
    return largest if largest is not None else None


# 742. Функция для выбора второго самого маленького числа
def choose_second_smallest(*nums):
    unique_nums = list(set(nums))
    unique_nums.sort()
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]


# 743. Функция для выбора строки, которая начинается и заканчивается на одну и ту же букву
def choose_string_start_and_end_same(*strings):
    for s in strings:
        if s[0] == s[-1]:
            return s
    return None


# 744. Функция для выбора первого числа, которое делится на 5 и 7
def choose_first_divisible_by_5_and_7(arr):
    for num in arr:
        if num % 5 == 0 and num % 7 == 0:
            return num
    return None


# 745. Функция для выбора самой короткой строки, содержащей хотя бы одну цифру
def choose_shortest_string_with_digit(*strings):
    for s in strings:
        if any(char.isdigit() for char in s):
            return s
    return None


# 746. Функция для выбора самой дорогой покупки, не превышающей заданную цену
def choose_most_expensive_below_price(limit, *items):
    max_price = None
    most_expensive = None
    for item in items:
        if item['price'] <= limit:
            if max_price is None or item['price'] > max_price:
                most_expensive = item
                max_price = item['price']
    return most_expensive if most_expensive else None


# 747. Функция для выбора первого числа, которое является квадратом числа
def choose_first_square_number(arr):
    for num in arr:
        if int(num ** 0.5) ** 2 == num:
            return num
    return None


# 748. Функция для выбора самого старшего возраста среди людей
def choose_oldest_age(*ages):
    oldest = None
    for age in ages:
        if oldest is None or age > oldest:
            oldest = age
    return oldest if oldest is not None else None


# 749. Функция для выбора первого числа, которое делится на 2, но не на 3
def choose_first_divisible_by_2_not_3(arr):
    for num in arr:
        if num % 2 == 0 and num % 3 != 0:
            return num
    return None


# 750. Функция для выбора самой длинной строки, в которой все символы – цифры
def choose_longest_all_digits_string(*strings):
    longest = None
    for s in strings:
        if s.isdigit():
            if longest is None or len(s) > len(longest):
                longest = s
    return longest if longest is not None else None


# 751. Функция для выбора первого четного числа, которое больше заданного
def choose_first_even_greater_than(value, *nums):
    for num in nums:
        if num % 2 == 0 and num > value:
            return num
    return None


# 752. Функция для выбора первой строки, которая не является числом
def choose_first_non_numeric_string(*strings):
    for s in strings:
        if not s.isdigit():
            return s
    return None


# 753. Функция для выбора строки, которая является палиндромом
def choose_palindrome(*strings):
    for s in strings:
        if s == s[::-1]:
            return s
    return None


# 754. Функция для выбора самой дорогой покупки, которая не дороже 100
def choose_most_expensive_under_100(*items):
    max_price = None
    most_expensive = None
    for item in items:
        if item['price'] <= 100:
            if max_price is None or item['price'] > max_price:
                most_expensive = item
                max_price = item['price']
    return most_expensive if most_expensive else None


# 755. Функция для выбора самого первого четного числа, которое больше 10
def choose_first_even_greater_than_10(arr):
    for num in arr:
        if num % 2 == 0 and num > 10:
            return num
    return None


# 756. Функция для выбора самого маленького числа, которое делится на 5
def choose_smallest_divisible_by_5(*nums):
    smallest = None
    for num in nums:
        if num % 5 == 0:
            if smallest is None or num < smallest:
                smallest = num
    return smallest if smallest is not None else None


# 757. Функция для выбора первого слова с длиной больше 5, которое начинается с согласной
def choose_first_long_word_starting_with_consonant(*words):
    vowels = 'aeiouAEIOU'
    for word in words:
        if len(word) > 5 and word[0] not in vowels:
            return word
    return None


# 758. Функция для выбора самого большого числа, которое меньше чем 20
def choose_largest_less_than_20(*nums):
    largest = None
    for num in nums:
        if num < 20:
            if largest is None or num > largest:
                largest = num
    return largest if largest is not None else None


# 759. Функция для выбора строки, которая начинается с заглавной буквы
def choose_string_starting_with_uppercase(*strings):
    for s in strings:
        if s[0].isupper():
            return s
    return None


# 760. Функция для выбора первого числа, которое не является ни четным, ни простым
def choose_first_non_even_non_prime(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for num in arr:
        if num % 2 != 0 and not is_prime(num):
            return num
    return None
