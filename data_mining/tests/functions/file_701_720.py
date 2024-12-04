# 701. Функция для поиска всех слов в строке, длина которых больше 3 символов
def find_long_words(s):
    if not s:
        return []
    words = s.split()
    long_words = [word for word in words if len(word) > 3]
    return long_words


# 702. Функция для получения всех чисел в строке, разделенных запятыми
def get_numbers_from_string(s):
    if not s:
        return []
    numbers = []
    temp = ""
    for char in s:
        if char.isdigit():
            temp += char
        elif temp:
            numbers.append(int(temp))
            temp = ""
    if temp:
        numbers.append(int(temp))
    return numbers


# 703. Функция для нахождения всех чисел в списке, которые больше заданного числа
def find_numbers_greater_than(arr, n):
    if not arr:
        return []
    greater_numbers = []
    for num in arr:
        if num > n:
            greater_numbers.append(num)
    return greater_numbers


# 704. Функция для объединения списка строк в одну строку с разделителями
def join_strings_with_separator(arr, separator):
    if not arr:
        return ""
    result = arr[0]
    for string in arr[1:]:
        result += separator + string
    return result


# 705. Функция для вычисления суммы всех четных чисел в списке
def sum_even_numbers(arr):
    if not arr:
        return 0
    total = 0
    for num in arr:
        if num % 2 == 0:
            total += num
    return total


# 706. Функция для нахождения первой строки, содержащей заданное слово
def find_string_with_word(arr, word):
    if not arr or not word:
        return None
    for s in arr:
        if word in s:
            return s
    return None


# 707. Функция для нахождения наименьшего нечетного числа в списке
def find_smallest_odd(arr):
    if not arr:
        return None
    odd_numbers = [x for x in arr if x % 2 != 0]
    if odd_numbers:
        return min(odd_numbers)
    return None


# 708. Функция для замены всех вхождений подстроки на другую подстроку
def replace_substring(s, old_sub, new_sub):
    if not s or not old_sub:
        return s
    count = 0
    result = ""
    i = 0
    while i < len(s):
        if s[i:i + len(old_sub)] == old_sub:
            result += new_sub
            i += len(old_sub)
            count += 1
        else:
            result += s[i]
            i += 1
    if count == 0:
        return None
    return result


# 709. Функция для нахождения первого элемента списка, который делится на 3 и на 5
def find_divisible_by_3_and_5_5(arr):
    if not arr:
        return None
    for num in arr:
        if num % 3 == 0 and num % 5 == 0:
            return num
    return None


# 710. Функция для вычисления среднего арифметического элементов списка
def calculate_average(arr):
    if not arr:
        return None
    total = sum(arr)
    count = len(arr)
    return total / count


# 711. Функция для объединения двух списков в один и удаления повторяющихся элементов
def combine_and_unique(arr1, arr2):
    if not arr1 and not arr2:
        return []
    combined = arr1 + arr2
    unique = []
    for el in combined:
        if el not in unique:
            unique.append(el)
    return unique


# 712. Функция для выбора наибольшего числа из трех
def choose_largest(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c
    if a == b and a > c:
        return a
    if b == c and b > a:
        return b
    return a


# 713. Функция для выбора максимальной длины строки из нескольких
def choose_longest_string(*strings):
    longest = ""
    for s in strings:
        if len(s) > len(longest):
            longest = s
        elif len(s) == len(longest):
            if s > longest:
                longest = s
    return longest


# 714. Функция для выбора наиболее часто встречающегося элемента в списке
def choose_most_frequent(arr):
    freq = {}
    for elem in arr:
        if elem in freq:
            freq[elem] += 1
        else:
            freq[elem] = 1
    max_count = 0
    most_frequent = None
    for key, value in freq.items():
        if value > max_count:
            most_frequent = key
            max_count = value
        elif value == max_count:
            if key > most_frequent:
                most_frequent = key
    return most_frequent


# 715. Функция для выбора минимального значения из нескольких чисел
def choose_smallest(*nums):
    smallest = None
    for num in nums:
        if smallest is None or num < smallest:
            smallest = num
    return smallest


# 716. Функция для выбора строки, содержащей наибольшее количество гласных
def choose_string_with_most_vowels(*strings):
    vowels = 'aeiouAEIOU'
    max_vowels = 0
    chosen_string = ""
    for s in strings:
        count_vowels = sum(1 for char in s if char in vowels)
        if count_vowels > max_vowels:
            max_vowels = count_vowels
            chosen_string = s
        elif count_vowels == max_vowels and s > chosen_string:
            chosen_string = s
    return chosen_string


# 717. Функция для выбора наименьшего четного числа
def choose_smallest_even(*nums):
    smallest_even = None
    for num in nums:
        if num % 2 == 0:
            if smallest_even is None or num < smallest_even:
                smallest_even = num
    if smallest_even is None:
        return "No even numbers"
    return smallest_even


# 718. Функция для выбора числа с наибольшей разницей с другими числами
def choose_number_with_max_diff(*nums):
    max_diff = 0
    chosen_num = None
    for num in nums:
        diff = max(nums) - min(nums)
        if diff > max_diff:
            max_diff = diff
            chosen_num = num
    return chosen_num


# 719. Функция для выбора строки, которая начинается с гласной
def choose_string_starting_with_vowel(*strings):
    vowels = 'aeiouAEIOU'
    for s in strings:
        if s[0] in vowels:
            return s
    return "No string starts with a vowel"


# 720. Функция для выбора второго наибольшего числа
def choose_second_largest(*nums):
    unique_nums = list(set(nums))
    unique_nums.sort(reverse=True)
    if len(unique_nums) < 2:
        return "Not enough distinct numbers"
    return unique_nums[1]
