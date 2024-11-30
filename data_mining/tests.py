import pytest
from functions import *


# 1. Тест функции, проверяющей чётное ли число
def test_is_even():
    assert is_even(4) == True
    assert is_even(0) == True
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(1) == False
    assert is_even(7) == False
    assert is_even(-2) == False
    assert is_even(-3) == False
    assert is_even(-7) == False


# 2. Тест функции, возвращающей факториал числа
def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(-1) == None
    assert factorial(-12) == None
    assert factorial(-5) == None
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(4) == 24


# 3. Тест функции, проверяющей, чего больше, гласных или согласных
def test_count_vowels():
    assert count_vowels("hello") == False
    assert count_vowels("aeioubcd") == True
    assert count_vowels("aeiou") == True
    assert count_vowels("bcd") == False
    assert count_vowels("xylophone") == False
    assert count_vowels("consonant") == False
    assert count_vowels("aaaabbbbcccc") == False


# 4. Тест функции, проверяющей чего больше, чётных или нечётных чисел в списке
def test_count_even_numbers():
    assert count_even_numbers([1, 2, 3, 4, 5]) == False
    assert count_even_numbers([2, 4, 6, 8]) == True
    assert count_even_numbers([1, 3, 5, 7]) == False
    assert count_even_numbers([0, 1, 2, 3, 4]) == True
    assert count_even_numbers([2, 3, 4, 1, 6]) == True
    assert count_even_numbers([2, 1, 2, 1, 2]) == True


# 5. Тест функции, которая возвращает сумму чисел от 1 до n
def test_sum_up_to_n():
    assert sum_up_to_n(10) == 54
    assert sum_up_to_n(5) == 12
    assert sum_up_to_n(0) == 0
    assert sum_up_to_n(-1) == 0
    assert sum_up_to_n(3) == 8
    assert sum_up_to_n(20) == 164
    assert sum_up_to_n(2) == 2


# 6. Тест функции проверяющей, является ли строка палиндромом
def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("level") == True
    assert is_palindrome("empty") == False
    assert is_palindrome("madam") == True
    assert is_palindrome(" ") == True
    assert is_palindrome("") == False


# 7. Тест функции для вычисления чисел Фибоначчи до n-го
def test_fibonacci():
    assert fibonacci(5) == [0, 1, 1, 2, 3, 5]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8]
    assert fibonacci(1) == [0, 1, 1]
    assert fibonacci(0) == []
    assert fibonacci(-1) == []
    assert fibonacci(2) == [0, 1, 1, 2]
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5]


# 8. Тест функции для нахождения максимального числа в списке
def test_find_max():
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([5, 4, 3, 2, 1]) == 5
    assert find_max([1, 2, 3, 4, 0]) == 4
    assert find_max([0, 0, 0, 0]) == 0
    assert find_max([-1, -2, -3, -4]) == -1
    assert find_max([5, 1, 5, 2, 5]) == 5
    assert find_max([]) == None


# 9. Тест функции для нахождения минимального числа в списке
def test_find_min():
    assert find_min([1, 2, 3, 4, 5]) == 1
    assert find_min([5, 4, 3, 2, 1]) == 1
    assert find_min([1, 2, 3, 4, 0]) == 0
    assert find_min([0, 0, 0, 0]) == 0
    assert find_min([-1, -2, -3, -4]) == -4
    assert find_min([5, 1, 5, 2, 5]) == 1
    assert find_min([5, 1, 10, 2, 5]) == 1
    assert find_min([]) == None


# 10. Тест функции для вычисления суммы всех элементов в списке
def test_sum_list():
    assert sum_list([1, 2, 3, 4, 5]) == 15
    assert sum_list([5, 5, 5, 5]) == 20
    assert sum_list([0, 1, 2, 3]) == 6
    assert sum_list([0, 0, 0, 0]) == 0
    assert sum_list([-1, -2, -3, -4]) == -10
    assert sum_list([1, 1, 1, 1]) == 4
    assert sum_list([]) == 0


# 11. Тест функции, которая возвращает все четные числа из списка
def test_filter_even():
    assert filter_even([1, 2, 3, 4, 5]) == [2, 4]
    assert filter_even([5, 5, 5, 5]) == []
    assert filter_even([0, 1, 2, 3]) == [0, 2]
    assert filter_even([0, 0, 0, 0]) == [0, 0, 0, 0]
    assert filter_even([-1, -2, -3, -4]) == [-2, -4]
    assert filter_even([1, 1, 1, 1]) == []
    assert filter_even([]) == []


# 12. Тест функции, которая возвращает все нечетные числа из списка
def test_filter_odd():
    assert filter_odd([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert filter_odd([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert filter_odd([0, 1, 2, 3]) == [1, 3]
    assert filter_odd([0, 0, 0, 0]) == []
    assert filter_odd([-1, -2, -3, -4]) == [-1, -3]
    assert filter_odd([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert filter_odd([]) == []


# 13. Тест функции для переворота строки
def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("radar") == "radar"
    assert reverse_string("world") == "dlrow"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("madam") == "madam"
    assert reverse_string("Python") == "nohtyP"


# 14. Тест функции для подсчета количества слов в строке
def test_count_words():
    assert count_words("This is a test") == 4
    assert count_words("Hello World") == 2
    assert count_words("Single") == 1
    assert count_words("") == 0
    assert count_words("One Two Three") == 3
    assert count_words("Too many words here") == 4
    assert count_words("This sentence is longer than ten words and needs a test") == 11


# 15. Тест функции для вычисления степени числа
def test_power():
    assert power(2, 3) == 8
    assert power(0, 0) == None
    assert power(3, 0) == 1
    assert power(0, 3) == 0
    assert power(2, -2) == 0.25
    assert power(5, 1) == 5
    assert power(3, 3) == 27


# 16. Тест функции для нахождения среднего значения списка
def test_average():
    assert average([1, 2, 3, 4, 5]) == 3
    assert average([0, 0, 0, 0]) == 0
    assert average([10, 20, 30, 40]) == 25
    assert average([-1, -2, -3, -4]) == -2.5
    assert average([5, 5, 5, 5]) == 5
    assert average([1, 2]) == 1.5
    assert average([]) == 0


# 17. Тест функции для нахождения суммы элементов до первого отрицательного числа
def test_sum_until_negative():
    assert sum_until_negative([1, 2, 3, -1, 5]) == 6
    assert sum_until_negative([5, 5, 5, 5]) == 20
    assert sum_until_negative([0, 1, 2, 3]) == 6
    assert sum_until_negative([0, 0, 0, 0]) == 0
    assert sum_until_negative([-1, -2, -3, -4]) == 0
    assert sum_until_negative([1, 2, 3, 4]) == 10


# 18. Тест функции для нахождения простых чисел до n
def test_find_primes():
    assert find_primes(10) == [2, 3, 5, 7]
    assert find_primes(1) == []
    assert find_primes(2) == [2]
    assert find_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert find_primes(0) == []
    assert find_primes(-5) == []
    assert find_primes(4) == [2, 3]


# 19. Тест функции для нахождения суммы чисел до n, исключая числа, кратные 3
def test_sum_exclude_multiples_of_three():
    assert sum_exclude_multiples_of_three(10) == 37
    assert sum_exclude_multiples_of_three(3) == 3
    assert sum_exclude_multiples_of_three(6) == 12
    assert sum_exclude_multiples_of_three(0) == 0
    assert sum_exclude_multiples_of_three(1) == 1
    assert sum_exclude_multiples_of_three(5) == 12
    assert sum_exclude_multiples_of_three(20) == 147


# 20. Тест функции для проверки, является ли число простым
def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(17) == True
    assert is_prime(-3) == False


# 21. Тесты для функции `range_list`:
def test_range_list():
    assert range_list(1, 5) == [1, 2, 3, 4, 5]
    assert range_list(5, 5) == [5]
    assert range_list(0, 3) == [0, 1, 2, 3]
    assert range_list(3, 1) == []
    assert range_list(10, 7) == []
    assert range_list(-5, 0) == [-5, -4, -3, -2, -1, 0]


# 22. Тесты для функции `product_list`:
def test_product_list():
    assert product_list([1, 2, 3]) == 6
    assert product_list([1, 0, 3]) == 3
    assert product_list([0, 0, 0]) == 1
    assert product_list([]) == 1
    assert product_list([5, 7]) == 35
    assert product_list([1, -2, 3]) == -6


# 23. Тесты для функции `intersect_lists`:
def test_intersect_lists():
    assert intersect_lists([1, 2, 3], [3, 4, 5]) == [3]
    assert intersect_lists([1, 2], [3, 4]) == []
    assert intersect_lists([5, 6], [6, 7]) == [6]
    assert intersect_lists([], [1, 2, 3]) == []
    assert intersect_lists([1, 2, 3], []) == []
    assert intersect_lists([10, 20], [20, 30]) == [20]


# 24. Тесты для функции `remove_duplicates`:
def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 1]) == [1, 2, 3]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([10, 20, 20, 30]) == [10, 20, 30]
    assert remove_duplicates([1, 1, 1, 2, 2, 2]) == [1, 2]
    assert remove_duplicates([1, 2, 2, 1]) == [1, 2]


# 25. Тесты для функции `gcd`:
def test_gcd():
    assert gcd(12, 15) == 3
    assert gcd(100, 25) == 25
    assert gcd(7, 13) == 1
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(14, 49) == 7


# 26. Тесты для функции `lcm`:
def test_lcm():
    assert lcm(4, 5) == 20
    assert lcm(3, 7) == 21
    assert lcm(0, 5) == None
    assert lcm(10, 15) == 30
    assert lcm(25, 40) == 200
    assert lcm(8, 12) == 24
    assert lcm(1000, 1001) == 1001000


# 27. Тесты для функции `count_occurrences`:
def test_count_occurrences():
    assert count_occurrences([1, 2, 3, 1], 1) == 2
    assert count_occurrences([2, 4, 6], 2) == 1
    assert count_occurrences([1, 1, 1, 1], 2) == 0
    assert count_occurrences([10, 20, 10], 10) == 2
    assert count_occurrences([1, 3, 1, 2], 5) == 0
    assert count_occurrences([0, 2, 0, 4], 0) == 2


# 28. Тесты для функции `is_number`:
def test_is_number():
    assert is_number("123") == True
    assert is_number("12.34") == True
    assert is_number("") == False
    assert is_number("abc") == False
    assert is_number("123abc") == False
    assert is_number("-123") == False


# 29. Тесты для функции `square_non_negative`:
def test_square_non_negative():
    assert square_non_negative(4) == 16
    assert square_non_negative(0) == 0
    assert square_non_negative(-4) == None
    assert square_non_negative(5) == 25
    assert square_non_negative(-10) == None
    assert square_non_negative(10) == 100


# 30. Тесты для функции `longest_common_subsequence`:
def test_longest_common_subsequence():
    assert longest_common_subsequence("abc", "ac") == 2
    assert longest_common_subsequence("abcdef", "abdf") == 4
    assert longest_common_subsequence("abc", "xyz") == 0
    assert longest_common_subsequence("abc", "") == 0
    assert longest_common_subsequence("12345", "54321") == 1
    assert longest_common_subsequence("", "") == 0


# 31. Тесты для функции `find_index`:
def test_find_index():
    assert find_index([1, 2, 3], 2) == 1
    assert find_index([10, 20, 30], 40) == -1
    assert find_index([1, 2, 3, 4], 1) == 0
    assert find_index([], 1) == -1
    assert find_index([10, 20], 20) == 1
    assert find_index([1, 1, 1], 1) == 0


# 32. Тесты для функции `unique_chars`:
def test_unique_chars():
    assert unique_chars("aabcc") == "abc"
    assert unique_chars("abcd") == "abcd"
    assert unique_chars("aabbcc") == "abc"
    assert unique_chars("aabb  cc") == "ab c"
    assert unique_chars("abcdabcd") == "abcd"
    assert unique_chars("") == ""


# 33. Тесты для функции `count_multiples_of_five`:
def test_count_multiples_of_five():
    assert count_multiples_of_five(1, 10) == 2
    assert count_multiples_of_five(10, 1) == 0
    assert count_multiples_of_five(0, 5) == 2
    assert count_multiples_of_five(5, 5) == 1
    assert count_multiples_of_five(10, 20) == 3
    assert count_multiples_of_five(12, 18) == 1
    assert count_multiples_of_five(1, 4) == 0


# 34. Тесты для функции `is_leap_year`:
def test_is_leap_year():
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True
    assert is_leap_year(1900) == False
    assert is_leap_year(2000) == True
    assert is_leap_year(2023) == False
    assert is_leap_year(2004) == True


# 35. Тесты для функции `max_min_difference_1`:
def test_max_min_difference_1():
    assert max_min_difference_1([1, 2, 3, 4]) == 3
    assert max_min_difference_1([10, 5]) == 5
    assert max_min_difference_1([1, 1, 1, 1]) == 0
    assert max_min_difference_1([0, 2, 0]) == 2
    assert max_min_difference_1([100]) == 0
    assert max_min_difference_1([]) == None


# 36. Тесты для функции `is_anagram`:
def test_is_anagram():
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "world") == False
    assert is_anagram("evil", "vile") == True
    assert is_anagram("abc", "acb") == True
    assert is_anagram("abc", "abcd") == False
    assert is_anagram("123", "321") == True


# 37. Тесты для функции `sum_of_squares`:
def test_sum_of_squares():
    assert sum_of_squares([1, 2, 3]) == 14
    assert sum_of_squares([0, 4, 5]) == 41
    assert sum_of_squares([-1, -2, -3]) == 0
    assert sum_of_squares([1, 2, 3, 4]) == 30
    assert sum_of_squares([]) == 0
    assert sum_of_squares([1, 0, 1]) == 2


# 38. Тесты для функции `geometric_mean`:
def test_geometric_mean():
    assert geometric_mean([1, 2, 3]) == 1.8171205928321397
    assert geometric_mean([5, 5, 5]) == 5.0
    assert geometric_mean([1, 1, 1]) == 1.0
    assert geometric_mean([0, 1, 2]) == 1.2599210498948732
    assert geometric_mean([]) == None
    assert geometric_mean([3, 2, 4]) == 2.8844991406148166


# 39. Тесты для функции `find_duplicates`:
def test_find_duplicates():
    assert find_duplicates([1, 2, 3, 2]) == [2]
    assert find_duplicates([1, 1, 1]) == [1]
    assert find_duplicates([4, 5, 6]) == []
    assert find_duplicates([10, 20, 20, 30]) == [20]
    assert find_duplicates([2, 3, 2, 3]) == [2, 3]
    assert find_duplicates([1, 1, 2, 3, 3]) == [1, 3]


# 40. Тесты для функции `square_list`:
def test_square_list():
    assert square_list([1, 2, 3]) == [1, 4, 9]
    assert square_list([0, -1, -2]) == [0]
    assert square_list([5, 6]) == [25, 36]
    assert square_list([-1, -3, 2]) == [4]
    assert square_list([]) == []
    assert square_list([4, 0, -5]) == [16, 0]


# 41. Тесты для функции `contains_digits`:
def test_contains_digits():
    assert contains_digits("123abc") == True
    assert contains_digits("abcdef") == False
    assert contains_digits("abc1") == True
    assert contains_digits("") == False
    assert contains_digits("123") == True
    assert contains_digits("no digits here!") == False


# 42. Тесты для функции `greater_than`:
def test_greater_than():
    assert greater_than([1, 2, 3, 4], 2) == [3, 4]
    assert greater_than([5, 6, 7], 7) == []
    assert greater_than([10, 20, 30], 25) == [30]
    assert greater_than([-1, 0, 1], 0) == [1]
    assert greater_than([], 0) == []
    assert greater_than([2, 2, 2], 2) == []


# 43. Тесты для функции `sum_even_up_to_n`:
def test_sum_even_up_to_n():
    assert sum_even_up_to_n(10) == 30
    assert sum_even_up_to_n(1) == 0
    assert sum_even_up_to_n(0) == 0
    assert sum_even_up_to_n(-5) == 0
    assert sum_even_up_to_n(7) == 12
    assert sum_even_up_to_n(2) == 2


# 44. Тесты для функции `reverse_range`:
def test_reverse_range():
    assert reverse_range(5) == [5, 4, 3, 2, 1]
    assert reverse_range(1) == [1]
    assert reverse_range(0) == []
    assert reverse_range(-1) == []
    assert reverse_range(10) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert reverse_range(2) == [2, 1]


# 45. Тесты для функции `common_element`:
def test_common_element():
    assert common_element([1, 2, 3], [3, 4, 5]) == 3
    assert common_element([10, 20, 30], [5, 15, 20]) == 20
    assert common_element([1, 2, 3], [4, 5, 6]) == None
    assert common_element([], [1, 2, 3]) == None
    assert common_element([1, 2, 3], []) == None
    assert common_element([1, 2, 3], [1, 2, 3]) == 1


# 46. Тесты для функции `extract_numbers`:
def test_extract_numbers():
    assert extract_numbers("1 2 3 abc 4 5 6") == [1, 2, 3, 4, 5, 6]
    assert extract_numbers("no numbers here") == []
    assert extract_numbers("123") == [123]
    assert extract_numbers("") == []
    assert extract_numbers("56 78") == [56, 78]
    assert extract_numbers("1 2 three") == [1, 2]


# 47. Тесты для функции `trimmed_mean`:
def test_trimmed_mean():
    assert trimmed_mean([1, 2, 3, 4, 5]) == 3
    assert trimmed_mean([10, 10, 10, 10, 10, 10]) == 10
    assert trimmed_mean([1, 2]) == None
    assert trimmed_mean([10]) == None
    assert trimmed_mean([]) == None
    assert trimmed_mean([1, 3, 3, 6, 7, 8, 9]) == 5.4


# 48. Тесты для функции `all_substrings`:
def test_all_substrings():
    assert all_substrings("abc") == ["a", "ab", "abc", "b", "bc", "c"]
    assert all_substrings("ab") == ["a", "ab", "b"]
    assert all_substrings("a") == ["a"]
    assert all_substrings("") == []
    assert all_substrings("xyz") == ["x", "xy", "xyz", "y", "yz", "z"]
    assert all_substrings("abca") == ["a", "ab", "abc", "abca", "b", "bc", "bca", "c", "ca", "a"]


# 49. Тесты для функции `divisible_by_three`:
def test_divisible_by_three():
    assert divisible_by_three([3, 6, 9, 12]) == [3, 6, 9, 12]
    assert divisible_by_three([1, 2, 4, 5]) == []
    assert divisible_by_three([0, 3, 6]) == [0, 3, 6]
    assert divisible_by_three([-3, -6, -9]) == [-3, -6, -9]
    assert divisible_by_three([4, 5, 6, 7, 8, 9]) == [6, 9]
    assert divisible_by_three([]) == []


# 50. Тесты для функции `unique_char_count`:
def test_unique_char_count():
    assert unique_char_count("abcdef") == 6
    assert unique_char_count("aabbcc") == 3
    assert unique_char_count("abcABC") == 6
    assert unique_char_count("") == 0
    assert unique_char_count("a") == 1
    assert unique_char_count("aaaa") == 1


# 51. Тесты для функции `is_valid_email`:
def test_is_valid_email():
    assert is_valid_email("test@example.com") == True
    assert is_valid_email("test.example.com") == False
    assert is_valid_email("test@.com") == True
    assert is_valid_email("test@com") == False
    assert is_valid_email("test@e.com") == True
    assert is_valid_email("") == False


# 52. Тесты для функции `max_consecutive_chars`:
def test_max_consecutive_chars():
    assert max_consecutive_chars("aaabbccc") == 3
    assert max_consecutive_chars("abcd") == 1
    assert max_consecutive_chars("aabbaa") == 2
    assert max_consecutive_chars("") == 1
    assert max_consecutive_chars("a") == 1
    assert max_consecutive_chars("aaabbbaaacccddd") == 3


# 53. Тесты для функции `median`:
def test_median():
    assert median([3, 1, 2]) == 2
    assert median([4, 1, 3, 2]) == 2.5
    assert median([]) == None
    assert median([1]) == 1
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 1, 1, 1, 1]) == 1


# 54. Тесты для функции `most_frequent`:
def test_most_frequent():
    assert most_frequent([1, 2, 2, 3, 3, 3]) == 3
    assert most_frequent([4, 4, 4, 4]) == 4
    assert most_frequent([1, 1, 2, 2, 3, 3]) == 1  # first encountered
    assert most_frequent([5]) == 5
    assert most_frequent([]) == None
    assert most_frequent([1, 2, 3, 4, 5]) == 1


# 55. Тесты для функции `remove_spaces`:
def test_remove_spaces():
    assert remove_spaces("hello world") == "helloworld"
    assert remove_spaces(" ") == ""
    assert remove_spaces("") == ""
    assert remove_spaces("a b c") == "abc"
    assert remove_spaces("no_spaces") == "no_spaces"
    assert remove_spaces("  leading and trailing spaces  ") == "leadingandtrailingspaces"


# 56. Тесты для функции `first_last`:
def test_first_last():
    assert first_last([1, 2, 3, 4]) == (1, 4)
    assert first_last([5]) == (5, 5)
    assert first_last([]) == (None, None)
    assert first_last([10, 20, 30, 40]) == (10, 40)
    assert first_last([0]) == (0, 0)
    assert first_last([1, 1, 1, 1]) == (1, 1)


# 57. Тесты для функции `join_with_space`:
def test_join_with_space():
    assert join_with_space("hello", "world") == "hello world"
    assert join_with_space("a", "b") == "a b"
    assert join_with_space("", "empty") == " empty"
    assert join_with_space("empty", "") == "empty "
    assert join_with_space("", "") == " "
    assert join_with_space("one", "two") == "one two"


# 58. Тесты для функции `is_positive`:
def test_is_positive():
    assert is_positive(5) == True
    assert is_positive(-1) == False
    assert is_positive(0) == False
    assert is_positive(100) == True
    assert is_positive(-50) == False
    assert is_positive(1) == True


# 59. Тесты для функции `sum_exclude_multiples_of_two`:
def test_sum_exclude_multiples_of_two():
    assert sum_exclude_multiples_of_two(10) == 25
    assert sum_exclude_multiples_of_two(1) == 1
    assert sum_exclude_multiples_of_two(0) == 0
    assert sum_exclude_multiples_of_two(-5) == 0
    assert sum_exclude_multiples_of_two(5) == 9
    assert sum_exclude_multiples_of_two(7) == 16


# 60. Тесты для функции `prime_numbers`:
def test_prime_numbers():
    assert prime_numbers([2, 3, 4, 5, 6]) == [2, 3, 5]
    assert prime_numbers([10, 11, 12, 13, 14]) == [11, 13]
    assert prime_numbers([0, 1, 2, 3]) == [2, 3]
    assert prime_numbers([-1, -2, 2, 3]) == [2, 3]
    assert prime_numbers([4, 6, 8, 9]) == []
    assert prime_numbers([29, 31, 37, 41]) == [29, 31, 37, 41]


# 61. Тесты для функции `extract_even_numbers`:
def test_extract_even_numbers():
    assert extract_even_numbers("1 2 3 4 5") == [2, 4]
    assert extract_even_numbers("10 15 20 25") == [10, 20]
    assert extract_even_numbers("7 9 11 13") == []
    assert extract_even_numbers("0 6 8 10") == [0, 6, 8, 10]
    assert extract_even_numbers("1 3 5 7 9") == []


# 62. Тесты для функции `divisible_by`:
def test_divisible_by():
    assert divisible_by([1, 2, 3, 4, 5], 2) == [2, 4]
    assert divisible_by([6, 7, 8, 9], 3) == [6, 9]
    assert divisible_by([10, 20, 30], 5) == [10, 20, 30]
    assert divisible_by([1, 2, 3], 1) == [1, 2, 3]
    assert divisible_by([1, 2, 3], 0) == []
    assert divisible_by([5, 10, 15], 7) == []


# 63. Тесты для функции `is_float`:
def test_is_float():
    assert is_float("3.14") == True
    assert is_float("2.718") == True
    assert is_float("abc") == False
    assert is_float("123") == True
    assert is_float("0.0") == True
    assert is_float("-1.5") == True


# 64. Тесты для функции `count_starting_with`:
def test_count_starting_with():
    assert count_starting_with(["apple", "apricot", "banana"], 'a') == 2
    assert count_starting_with(["pear", "plum", "peach"], 'p') == 3
    assert count_starting_with(["apple", "banana", "cherry"], 'x') == 0
    assert count_starting_with(["apple", "banana", "ananas"], 'a') == 2
    assert count_starting_with(["apple", "banana", "cherry"], 'b') == 1


# 65. Тесты для функции `max_odd_number`:
def test_max_odd_number():
    assert max_odd_number([1, 3, 5, 7, 9]) == 9
    assert max_odd_number([2, 4, 6, 8]) == None
    assert max_odd_number([10, 15, 20, 25]) == 25
    assert max_odd_number([-1, -3, -5, -7, -9]) == -1
    assert max_odd_number([]) == None


# 66. Тесты для функции `count_uppercase`:
def test_count_uppercase():
    assert count_uppercase("Hello World!") == 2
    assert count_uppercase("HELLO") == 5
    assert count_uppercase("hello") == 0
    assert count_uppercase("HeLLo WoRLd!") == 6
    assert count_uppercase("123ABC") == 3


# 67. Тесты для функции `is_fibonacci_number`:
def test_is_fibonacci_number():
    assert is_fibonacci_number(0) == False
    assert is_fibonacci_number(1) == True
    assert is_fibonacci_number(2) == True
    assert is_fibonacci_number(3) == True
    assert is_fibonacci_number(4) == False
    assert is_fibonacci_number(5) == True
    assert is_fibonacci_number(-1) == False


# 68. Тесты для функции `is_symmetric`:
def test_is_symmetric():
    assert is_symmetric([1, 2, 3, 2, 1]) == True
    assert is_symmetric([1, 2, 2, 1]) == True
    assert is_symmetric([1, 2, 3, 4, 5]) == False
    assert is_symmetric([]) == True
    assert is_symmetric([1, 2, 3, 4, 3, 2, 1]) == True


# 69. Тесты для функции `sum_numbers_in_string`:
def test_sum_numbers_in_string():
    assert sum_numbers_in_string("1 2 3 4 5") == 15
    assert sum_numbers_in_string("10 20 30") == 60
    assert sum_numbers_in_string("abc 123 def") == 123
    assert sum_numbers_in_string("100") == 100
    assert sum_numbers_in_string("1 a 2 b 3 c") == 6


# 70. Тесты для функции `odd_max_min_difference`:
def test_odd_max_min_difference():
    assert odd_max_min_difference([1, 3, 5, 7, 9]) == 8
    assert odd_max_min_difference([2, 4, 6, 8]) == None
    assert odd_max_min_difference([10, 15, 20, 25, 30]) == 10
    assert odd_max_min_difference([-1, -3, -5, -7, -9]) == 8
    assert odd_max_min_difference([]) == None


# 71. Тесты для функции `count_digits`:
def test_count_digits():
    assert count_digits("abc123") == 3
    assert count_digits("1234567890") == 10
    assert count_digits("no digits here") == 0
    assert count_digits("123abc456") == 6
    assert count_digits("") == 0


# 72. Тесты для функции `is_even_length`:
def test_is_even_length():
    assert is_even_length("abcd") == True
    assert is_even_length("abcde") == False
    assert is_even_length("") == True
    assert is_even_length("abcdefgh") == True
    assert is_even_length("abc") == False


# 73. Тесты для функции `sum_exclude_multiples_of_four`:
def test_sum_exclude_multiples_of_four():
    assert sum_exclude_multiples_of_four([1, 2, 3, 4, 5, 6, 7, 8]) == 24
    assert sum_exclude_multiples_of_four([4, 8, 12]) == 0
    assert sum_exclude_multiples_of_four([1, 2, 3]) == 6
    assert sum_exclude_multiples_of_four([]) == 0
    assert sum_exclude_multiples_of_four([5, 10, 15]) == 30


# 74. Тесты для функции `missing_min_number`:
def test_missing_min_number():
    assert missing_min_number([0, 1, 2, 4, 5]) == 3
    assert missing_min_number([1, 2, 3]) == 0
    assert missing_min_number([0, 1, 2, 3]) == 4
    assert missing_min_number([]) == 0
    assert missing_min_number([5, 6, 7, 8]) == 0


# 75. Тесты для функции `common_numbers`:
def test_common_numbers():
    assert common_numbers([1, 2, 3], [3, 4, 5]) == [3]
    assert common_numbers([6, 7, 8], [8, 9, 10]) == [8]
    assert common_numbers([1, 2, 3], [4, 5, 6]) == []
    assert common_numbers([], [1, 2, 3]) == []
    assert common_numbers([1, 2, 3], [1, 2, 3]) == [1, 2, 3]


# 76. Тесты для функции `first_string_with_digit`:
def test_first_string_with_digit():
    assert first_string_with_digit(["abc", "def2", "ghi"]) == "def2"
    assert first_string_with_digit(["123", "abc", "456"]) == "123"
    assert first_string_with_digit(["abc", "def", "ghi"]) == None
    assert first_string_with_digit(["abc1", "def", "ghi"]) == "abc1"
    assert first_string_with_digit([]) == None


# 77. Тесты для функции `count_words_starting_with`:
def test_count_words_starting_with():
    assert count_words_starting_with(["apple", "apricot", "banana"], 'a') == 2
    assert count_words_starting_with(["pear", "plum", "peach"], 'p') == 3
    assert count_words_starting_with(["apple", "banana", "cherry"], 'x') == 0
    assert count_words_starting_with(["apple", "banana", "ananas"], 'a') == 2
    assert count_words_starting_with(["apple", "banana", "cherry"], 'b') == 1


# 78. Тесты для функции `count_greater_than`:
def test_count_greater_than():
    assert count_greater_than([1, 2, 3, 4, 5], 3) == 2
    assert count_greater_than([10, 20, 30, 40], 25) == 2
    assert count_greater_than([1, 2, 3], 4) == 0
    assert count_greater_than([], 5) == 0
    assert count_greater_than([5, 6, 7, 8], 5) == 3


# 79. Тесты для функции `max_sublist_sum`:
def test_max_sublist_sum():
    assert max_sublist_sum([1, -2, 3, 4, -1, 2, 1, -5, 4]) == 9
    assert max_sublist_sum([1, 2, 3, 4, 5]) == 15
    assert max_sublist_sum([-1, -2, -3, -4]) == -1
    assert max_sublist_sum([3, -2, 5, -1]) == 6
    assert max_sublist_sum([]) == None


# 80. Тесты для функции `max_pairwise_product`:
def test_max_pairwise_product():
    assert max_pairwise_product([1, 2, 3, 4, 5]) == 20
    assert max_pairwise_product([5, 5, 5, 5]) == 25
    assert max_pairwise_product([1, 0, 0, 1]) == 1
    assert max_pairwise_product([-1, -2, -3, -4]) == 2
    assert max_pairwise_product([5]) == None


# 81. Тесты для функции `is_palindrome_1`:
def test_is_palindrome_1():
    assert is_palindrome_1("A man, a plan, a canal, Panama") == True
    assert is_palindrome_1("No lemon, no melon") == True
    assert is_palindrome_1("Hello, World!") == False
    assert is_palindrome_1("Madam") == True
    assert is_palindrome_1("") == True
    assert is_palindrome_1("12321") == True
    assert is_palindrome_1("12345") == False
    assert is_palindrome_1("Was it a car or a cat I saw?") == True
    assert is_palindrome_1("Not a palindrome") == False


# 82. Тесты для функции `largest_divisor_less_than`:
def test_largest_divisor_less_than():
    assert largest_divisor_less_than(10) == 5
    assert largest_divisor_less_than(15) == 5
    assert largest_divisor_less_than(1) == None
    assert largest_divisor_less_than(2) == None
    assert largest_divisor_less_than(3) == None
    assert largest_divisor_less_than(25) == 5
    assert largest_divisor_less_than(100) == 50
    assert largest_divisor_less_than(49) == 7
    assert largest_divisor_less_than(97) == None
    assert largest_divisor_less_than(11) == None


# 83. Тесты для функции `non_prime_numbers`:
def test_non_prime_numbers():
    assert non_prime_numbers([2, 3, 4, 5, 6]) == [4, 6]
    assert non_prime_numbers([11, 13, 17, 19, 23]) == []
    assert non_prime_numbers([8, 12, 15]) == [8, 12, 15]
    assert non_prime_numbers([1, 2, 3, 5, 7]) == [1]
    assert non_prime_numbers([4, 6, 8, 9, 10]) == [4, 6, 8, 9, 10]
    assert non_prime_numbers([25, 26, 27]) == [25, 26, 27]
    assert non_prime_numbers([16, 18, 20]) == [16, 18, 20]
    assert non_prime_numbers([22, 24, 28]) == [22, 24, 28]
    assert non_prime_numbers([31, 33, 35]) == [33, 35]


# 84. Тесты для функции `max_digit_in_string`:
def test_max_digit_in_string():
    assert max_digit_in_string("1234567890") == 9
    assert max_digit_in_string("5555") == 5
    assert max_digit_in_string("1029384756") == 9
    assert max_digit_in_string("9081726354") == 9
    assert max_digit_in_string("") == None
    assert max_digit_in_string("a1b2c3") == None
    assert max_digit_in_string("7654321") == 7
    assert max_digit_in_string("0000") == 0
    assert max_digit_in_string("2468") == 8


# 85. Тесты для функции `largest_square`:
def test_largest_square():
    assert largest_square([1, 4, 9, 16, 25]) == 25
    assert largest_square([3, 6, 8, 10]) == None
    assert largest_square([4, 16, 25, 36]) == 36
    assert largest_square([0, 1, 2, 3]) == 1
    assert largest_square([49, 64, 81]) == 81
    assert largest_square([10, 20, 30]) == None
    assert largest_square([5, 12, 13]) == None
    assert largest_square([100, 121, 144]) == 144
    assert largest_square([9, 25, 49]) == 49


# 86. Тесты для функции `sum_of_two_squares`:
def test_sum_of_two_squares():
    assert sum_of_two_squares([5, 10, 13, 18]) == [5, 10, 13, 18]
    assert sum_of_two_squares([2, 3, 7, 8]) == [2, 8]
    assert sum_of_two_squares([1, 4, 9, 16]) == [1, 4, 9, 16]
    assert sum_of_two_squares([6, 11, 15, 20]) == [20]
    assert sum_of_two_squares([17, 29, 37]) == [17, 29, 37]
    assert sum_of_two_squares([49, 64, 81]) == [49, 64, 81]
    assert sum_of_two_squares([3, 5, 7, 12]) == [5]
    assert sum_of_two_squares([50, 73, 90]) == [50, 73, 90]
    assert sum_of_two_squares([25, 41, 60]) == [25, 41]


# 87. Тесты для функции `sum_of_digits_in_string`:
def test_sum_of_digits_in_string():
    assert sum_of_digits_in_string("123abc456") == 21
    assert sum_of_digits_in_string("789xyz") == 24
    assert sum_of_digits_in_string("0") == 0
    assert sum_of_digits_in_string("abc") == 0
    assert sum_of_digits_in_string("555") == 15
    assert sum_of_digits_in_string("12a34b56c") == 21
    assert sum_of_digits_in_string("111") == 3
    assert sum_of_digits_in_string("909") == 18
    assert sum_of_digits_in_string("246") == 12


# 88. Тесты для функции `elements_less_than_mean`:
def test_elements_less_than_mean():
    assert elements_less_than_mean([1, 2, 3, 4, 5]) == [1, 2]
    assert elements_less_than_mean([10, 20, 30, 40, 50]) == [10, 20]
    assert elements_less_than_mean([5, 6, 7, 8, 9]) == [5, 6]
    assert elements_less_than_mean([]) == []
    assert elements_less_than_mean([3, 3, 3, 3, 3]) == []
    assert elements_less_than_mean([2, 3, 5, 7, 11]) == [2, 3, 5]
    assert elements_less_than_mean([12, 14, 16, 18]) == [12, 14]
    assert elements_less_than_mean([8, 10, 12]) == [8]
    assert elements_less_than_mean([1, 4, 9, 16]) == [1, 4]


# 89. Тесты для функции `extract_numbers_from_string`:
def test_extract_numbers_from_string():
    assert extract_numbers_from_string("1 2 3 a b c 4 5 6") == [1, 2, 3, 4, 5, 6]
    assert extract_numbers_from_string("7 8 9 x y z") == [7, 8, 9]
    assert extract_numbers_from_string("No numbers here") == []
    assert extract_numbers_from_string("10 20 30 40") == [10, 20, 30, 40]
    assert extract_numbers_from_string("123abc456") == []
    assert extract_numbers_from_string("0 1 2 3") == [0, 1, 2, 3]
    assert extract_numbers_from_string("Only numbers 0 100") == [0, 100]
    assert extract_numbers_from_string("255 512 1024") == [255, 512, 1024]
    assert extract_numbers_from_string("5 15 25") == [5, 15, 25]


# 90. Тесты для функции `max_min_difference`:
def test_max_min_difference():
    assert max_min_difference([1, 2, 3, 4, 5]) == 4
    assert max_min_difference([10, 20, 30, 40, 50]) == 40
    assert max_min_difference([5, 10, 15, 20]) == 15
    assert max_min_difference([]) == None
    assert max_min_difference([1]) == 0
    assert max_min_difference([100, 200, 300, 400]) == 300
    assert max_min_difference([7, 14, 21, 28]) == 21
    assert max_min_difference([9, 18, 27, 36]) == 27
    assert max_min_difference([3, 6, 9, 12]) == 9


# 91. Тесты для функции `first_divisible_by_2_and_5`:
def test_first_divisible_by_2_and_5():
    assert first_divisible_by_2_and_5([1, 3, 5, 10]) == 10
    assert first_divisible_by_2_and_5([20, 15, 25, 30]) == 20
    assert first_divisible_by_2_and_5([1, 2, 3, 4]) == None
    assert first_divisible_by_2_and_5([50, 60, 70]) == 50
    assert first_divisible_by_2_and_5([21, 35, 49]) == None
    assert first_divisible_by_2_and_5([100, 200, 300]) == 100
    assert first_divisible_by_2_and_5([]) == None
    assert first_divisible_by_2_and_5([6, 9, 12, 18]) == None
    assert first_divisible_by_2_and_5([25, 50, 75]) == 50


# 92. Тесты для функции `square_if_number`:
def test_square_if_number():
    assert square_if_number("4") == 16.0
    assert square_if_number("2.5") == 6.25
    assert square_if_number("-3") == 9.0
    assert square_if_number("abc") == None
    assert square_if_number("0") == 0.0
    assert square_if_number("10") == 100.0
    assert square_if_number("3.14") == 9.8596
    assert square_if_number("") == None
    assert square_if_number("1.5e2") == 22500.0


# 93. Тесты для функции `count_non_prime`:
def test_count_non_prime():
    assert count_non_prime([2, 3, 4, 5, 6]) == 2
    assert count_non_prime([10, 12, 14]) == 3
    assert count_non_prime([11, 13, 17]) == 0
    assert count_non_prime([1, 2, 3, 4]) == 2
    assert count_non_prime([9, 15, 21]) == 3
    assert count_non_prime([4, 6, 8, 10]) == 4
    assert count_non_prime([5, 7, 11, 13]) == 0
    assert count_non_prime([0, 1, 2, 3, 4]) == 3
    assert count_non_prime([25, 36, 49]) == 3


# 94. Тесты для функции `palindromic_elements`:
def test_palindromic_elements():
    assert palindromic_elements(["121", "abc", "mam", "pop"]) == ["121", "mam", "pop"]
    assert palindromic_elements(["12321", "hello", "wow"]) == ["12321", "wow"]
    assert palindromic_elements([121, 1331, 12321]) == [121, 1331, 12321]
    assert palindromic_elements([123, 456, 789]) == []
    assert palindromic_elements([1441, 1221, 101]) == [1441, 1221, 101]
    assert palindromic_elements([]) == []
    assert palindromic_elements([55, 66, 77]) == [55, 66, 77]
    assert palindromic_elements(["aba", "cdc", "dad"]) == ["aba", "cdc", "dad"]
    assert palindromic_elements(["a", "b", "c", "d"]) == ["a", "b", "c", "d"]


# 95. Тесты для функции `largest_power_of_two`:
def test_largest_power_of_two():
    assert largest_power_of_two([1, 2, 4, 8, 16]) == 16
    assert largest_power_of_two([32, 64, 128]) == 128
    assert largest_power_of_two([3, 5, 7]) == None
    assert largest_power_of_two([2, 4, 16, 32]) == 32
    assert largest_power_of_two([]) == None
    assert largest_power_of_two([10, 20, 40]) == None
    assert largest_power_of_two([6, 12, 18]) == None
    assert largest_power_of_two([256, 512, 1024]) == 1024
    assert largest_power_of_two([5, 10, 20, 40]) == None


# 96. Тесты для функции `multiples_of_six`:
def test_multiples_of_six():
    assert multiples_of_six([6, 12, 18, 24]) == [6, 12, 18, 24]
    assert multiples_of_six([5, 10, 15, 20]) == []
    assert multiples_of_six([36, 42, 48]) == [36, 42, 48]
    assert multiples_of_six([7, 14, 21]) == []
    assert multiples_of_six([6, 6, 6]) == [6, 6, 6]
    assert multiples_of_six([]) == []
    assert multiples_of_six([30, 60, 90]) == [30, 60, 90]
    assert multiples_of_six([11, 22, 33]) == []
    assert multiples_of_six([18, 24, 36]) == [18, 24, 36]


# 97. Тесты для функции `unique_elements`:
def test_unique_elements():
    assert unique_elements([1, 2, 3, 1, 2]) == [1, 2, 3]
    assert unique_elements([4, 5, 6, 4, 5]) == [4, 5, 6]
    assert unique_elements([7, 8, 9]) == [7, 8, 9]
    assert unique_elements([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert unique_elements([10, 10, 10]) == [10]
    assert unique_elements([]) == []
    assert unique_elements([11, 22, 33, 22, 11]) == [11, 22, 33]
    assert unique_elements([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]
    assert unique_elements([5, 10, 15, 10, 5]) == [5, 10, 15]


# 98. Тесты для функции `count_occurrences_1`:
def test_count_occurrences_1():
    assert count_occurrences_1([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
    assert count_occurrences_1([4, 5, 6, 5, 4]) == {4: 2, 5: 2, 6: 1}
    assert count_occurrences_1([7, 8, 9]) == {7: 1, 8: 1, 9: 1}
    assert count_occurrences_1([1, 1, 1, 1]) == {1: 4}
    assert count_occurrences_1([]) == {}
    assert count_occurrences_1([2, 4, 4, 6, 6, 6]) == {2: 1, 4: 2, 6: 3}
    assert count_occurrences_1([10, 20, 30, 20, 10, 30, 30]) == {10: 2, 20: 2, 30: 3}
    assert count_occurrences_1([2, 3, 4, 5, 2, 4, 5]) == {2: 2, 3: 1, 4: 2, 5: 2}
    assert count_occurrences_1([100, 100, 100, 200, 200]) == {100: 3, 200: 2}


# 99. Тесты для функции `intersection_of_lists`:
def test_intersection_of_lists():
    assert intersection_of_lists([1, 2, 3], [3, 4, 5]) == [3]
    assert intersection_of_lists([10, 20, 30], [20, 30, 40]) == [20, 30]
    assert intersection_of_lists([5, 6, 7], [8, 9, 10]) == []
    assert intersection_of_lists([1, 2, 3, 4], [4, 5, 6, 7]) == [4]
    assert intersection_of_lists([1, 1, 2, 2], [2, 2, 3, 3]) == [2]
    assert intersection_of_lists([100, 200, 300], [400, 500, 600]) == []
    assert intersection_of_lists([0, 1, 2], [2, 3, 4]) == [2]
    assert intersection_of_lists([10, 11, 12], [13, 14, 15]) == []
    assert intersection_of_lists([], [1, 2, 3]) == []
    assert intersection_of_lists([1, 2, 3], []) == []


# 100. Тесты для функции `divisible_by_any`:
def test_divisible_by_any():
    assert divisible_by_any([10, 20, 30, 40], [2, 5]) == [10, 20, 30, 40]
    assert divisible_by_any([9, 18, 27, 36], [3]) == [9, 18, 27, 36]
    assert divisible_by_any([7, 14, 21], [2, 7]) == [7, 14, 21]
    assert divisible_by_any([11, 13, 17], [5, 10]) == []
    assert divisible_by_any([100, 200, 300], [2, 10]) == [100, 200, 300]
    assert divisible_by_any([8, 12, 16], [4]) == [8, 12, 16]
    assert divisible_by_any([15, 25, 35], [5]) == [15, 25, 35]
    assert divisible_by_any([1, 3, 5, 7], [2, 4]) == []
    assert divisible_by_any([100, 150, 200], [5]) == [100, 150, 200]
    assert divisible_by_any([], [2, 3]) == []


# 101. Тесты для функции `are_anagrams`:
def test_are_anagrams():
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("evil", "vile") == True
    assert are_anagrams("fluster", "restful") == True
    assert are_anagrams("test", "TEST") == False  # Case-sensitive check
    assert are_anagrams("a", "a") == True
    assert are_anagrams("abc", "abcd") == False
    assert are_anagrams("", "") == True
    assert are_anagrams("aabb", "abab") == True
    assert are_anagrams("aabb", "abac") == False


# 102. Тесты для функции `intersection_of_sets`:
def test_intersection_of_sets():
    assert intersection_of_sets({1, 2, 3}, {3, 4, 5}) == {3}
    assert intersection_of_sets({1, 2, 3}, {4, 5, 6}) == set()
    assert intersection_of_sets({"a", "b"}, {"b", "c"}) == {"b"}
    assert intersection_of_sets({"a", "b", "c"}, {"a", "b", "c"}) == {"a", "b", "c"}
    assert intersection_of_sets({"x", "y"}, {"y", "z"}) == {"y"}
    assert intersection_of_sets({1}, {1}) == {1}
    assert intersection_of_sets(set(), {1, 2, 3}) == set()
    assert intersection_of_sets({1, 2, 3}, set()) == set()
    assert intersection_of_sets({"apple"}, {"banana"}) == set()
    assert intersection_of_sets({"dog"}, {"dog", "cat"}) == {"dog"}


# 103. Тесты для функции `remove_duplicate_tuples`:
def test_remove_duplicate_tuples():
    assert remove_duplicate_tuples([(1, "a"), (2, "b"), (1, "c")]) == [(1, "a"), (2, "b")]
    assert remove_duplicate_tuples([(1, "a"), (1, "b"), (1, "c")]) == [(1, "a")]
    assert remove_duplicate_tuples([(1, "x"), (2, "y"), (2, "z")]) == [(1, "x"), (2, "y")]
    assert remove_duplicate_tuples([(3, "a"), (4, "b"), (5, "c")]) == [(3, "a"), (4, "b"), (5, "c")]
    assert remove_duplicate_tuples([("a", 1), ("b", 2), ("a", 3)]) == [("a", 1), ("b", 2)]
    assert remove_duplicate_tuples([("a", 1), ("a", 2), ("a", 3), ("b", 4)]) == [("a", 1), ("b", 4)]
    assert remove_duplicate_tuples([]) == []
    assert remove_duplicate_tuples([("x", 1), ("y", 2)]) == [("x", 1), ("y", 2)]
    assert remove_duplicate_tuples([("a", 5), ("a", 6), ("b", 5)]) == [("a", 5), ("b", 5)]


# 104. Тесты для функции `count_string_lengths`:
def test_count_string_lengths():
    assert count_string_lengths(["apple", "banana", "cherry"]) == {"apple": 5, "banana": 6, "cherry": 6}
    assert count_string_lengths(["hello", "world"]) == {"hello": 5, "world": 5}
    assert count_string_lengths(["a", "ab", "abc", "abcd"]) == {"a": 1, "ab": 2, "abc": 3, "abcd": 4}
    assert count_string_lengths(["", "non-empty", ""]) == {"": 0, "non-empty": 9}
    assert count_string_lengths([]) == {}
    assert count_string_lengths(["short", "longer", "longest"]) == {"short": 5, "longer": 6, "longest": 7}
    assert count_string_lengths(["test", "testing", "tests"]) == {"test": 4, "testing": 7, "tests": 5}
    assert count_string_lengths(["x", "xx", "xxx", "xxxx"]) == {"x": 1, "xx": 2, "xxx": 3, "xxxx": 4}
    assert count_string_lengths(["single", "word", "example"]) == {"single": 6, "word": 4, "example": 7}
    assert count_string_lengths(["one", "two", "three", "four"]) == {"one": 3, "two": 3, "three": 5, "four": 4}


# 105. Тесты для функции `most_frequent_in_dict`:
def test_most_frequent_in_dict():
    assert most_frequent_in_dict(None) == None
    assert most_frequent_in_dict({"a": 1, "b": 2, "c": 2}) == ("b", 2)
    assert most_frequent_in_dict({"x": 10, "y": 15, "z": 10}) == ("y", 15)
    assert most_frequent_in_dict({"apple": 3, "banana": 2, "cherry": 5}) == ("cherry", 5)
    assert most_frequent_in_dict({"a": 1, "b": 2, "c": 2, "d": 3}) == ("d", 3)
    assert most_frequent_in_dict({"a": 0, "b": 0, "c": 0}) == ("a", 0)
    assert most_frequent_in_dict({"a": 4}) == ("a", 4)
    assert most_frequent_in_dict({}) == None
    assert most_frequent_in_dict({"x": 5, "y": 5, "z": 5}) == ("x", 5)
    assert most_frequent_in_dict({"p": 10, "q": 12}) == ("q", 12)
    assert most_frequent_in_dict({"cat": 2, "dog": 3, "rabbit": 1}) == ("dog", 3)


# 106. Тесты для функции `merge_dicts`:
def test_merge_dicts():
    assert merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 5, "c": 4}
    assert merge_dicts({"x": 5, "y": 6}, {"y": 7, "z": 8}) == {"x": 5, "y": 13, "z": 8}
    assert merge_dicts({"a": 2}, {"a": 3}) == {"a": 5}
    assert merge_dicts({"apple": 2, "banana": 3}, {"apple": 4, "cherry": 5}) == {"apple": 6, "banana": 3, "cherry": 5}
    assert merge_dicts({"a": 1, "b": 2}, {}) == {"a": 1, "b": 2}
    assert merge_dicts({}, {"a": 1, "b": 2}) == {"a": 1, "b": 2}
    assert merge_dicts({"x": 1}, {"x": 1}) == {"x": 2}
    assert merge_dicts({"key1": 10}, {"key2": 20}) == {"key1": 10, "key2": 20}
    assert merge_dicts({}, {}) == {}
    assert merge_dicts({"a": 1}, {"b": 2, "a": 3}) == {"a": 4, "b": 2}


# 107. Тесты для функции `count_even_odd`:
def test_count_even_odd():
    assert count_even_odd([1, 2, 3, 4, 5]) == {"even": 2, "odd": 3}
    assert count_even_odd([2, 4, 6]) == {"even": 3, "odd": 0}
    assert count_even_odd([1, 3, 5]) == {"even": 0, "odd": 3}
    assert count_even_odd([0, -2, -4, 1, 3]) == {"even": 3, "odd": 2}
    assert count_even_odd([]) == {"even": 0, "odd": 0}
    assert count_even_odd([2, 3, 5, 7]) == {"even": 1, "odd": 3}
    assert count_even_odd([0, 2, 4, 6]) == {"even": 4, "odd": 0}
    assert count_even_odd([10, 11, 12, 13, 14]) == {"even": 3, "odd": 2}
    assert count_even_odd([1, 2, 3, 5, 6]) == {"even": 2, "odd": 3}
    assert count_even_odd([1, 1, 1, 1]) == {"even": 0, "odd": 4}


# 108. Тесты для функции `min_key_in_dict`:
def test_min_key_in_dict():
    assert min_key_in_dict({"a": 1, "b": 2, "c": 3}) == "a"
    assert min_key_in_dict({"apple": 10, "banana": 5, "cherry": 15}) == "banana"
    assert min_key_in_dict({"x": 1, "y": 0, "z": 2}) == "y"
    assert min_key_in_dict({"a": 100, "b": 50, "c": 150}) == "b"
    assert min_key_in_dict({}) == None
    assert min_key_in_dict({"cat": 5, "dog": 3, "rabbit": 8}) == "dog"
    assert min_key_in_dict({"p": 0, "q": 1}) == "p"
    assert min_key_in_dict({"a": -1, "b": 2}) == "a"
    assert min_key_in_dict({"a": -1, "b": -2}) == "b"
    assert min_key_in_dict({"x": 4, "y": 1, "z": 4}) == "y"


# 109. Тесты для функции `list_to_dict`:
def test_list_to_dict():
    assert list_to_dict([1, 2, 3]) == {0: 1, 1: 2, 2: 3}
    assert list_to_dict(["a", "b", "c"]) == {0: "a", 1: "b", 2: "c"}
    assert list_to_dict([True, False, True]) == {0: True, 1: False, 2: True}
    assert list_to_dict([3.14, 2.71]) == {0: 3.14, 1: 2.71}
    assert list_to_dict([]) == {}
    assert list_to_dict(["apple", "banana", "cherry"]) == {0: "apple", 1: "banana", 2: "cherry"}
    assert list_to_dict([10, 20, 30, 40]) == {0: 10, 1: 20, 2: 30, 3: 40}
    assert list_to_dict([1]) == {0: 1}
    assert list_to_dict([0, 0, 0]) == {0: 0, 1: 0, 2: 0}
    assert list_to_dict(["one", "two", "three"]) == {0: "one", 1: "two", 2: "three"}


# 110. Тесты для функции `check_and_square`:
def test_check_and_square():
    assert check_and_square("4") == 16
    assert check_and_square("-3") == 9
    assert check_and_square("2.5") == 6.25
    assert check_and_square("abc") == None
    assert check_and_square("0") == 0
    assert check_and_square("100") == 10000
    assert check_and_square("1.5") == 2.25
    assert check_and_square("-2") == 4
    assert check_and_square("1000") == 1000000
    assert check_and_square("") == None


# 111. Тесты для функции `merge_tuples`:
def test_merge_tuples():
    assert merge_tuples((1, 2), (2, 3)) == (1, 2, 3)
    assert merge_tuples(("a", "b"), ("b", "c")) == ("a", "b", "c")
    assert merge_tuples((1, 2, 3), (4, 5)) == (1, 2, 3, 4, 5)
    assert merge_tuples((1, 1), (1, 2)) == (1, 2)
    assert merge_tuples(("x", "y"), ("z", "y")) == ("x", "y", "z")
    assert merge_tuples((1, 1, 2), (2, 3)) == (1, 2, 3)
    assert merge_tuples((5, 5), (5, 6)) == (5, 6)
    assert merge_tuples((), ()) == ()
    assert merge_tuples(("a", "b"), ("a", "c", "d")) == ("a", "b", "c", "d")
    assert merge_tuples(("apple", "banana"), ("orange", "banana")) == ("apple", "banana", "orange")


# 112. Тесты для функции `unique_numbers`:
def test_unique_numbers():
    assert unique_numbers([1, 2, 2, 3, 4, 4]) == [1, 2, 3, 4]
    assert unique_numbers([10, 10, 10]) == [10]
    assert unique_numbers([5, 7, 8, 5, 8]) == [5, 7, 8]
    assert unique_numbers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert unique_numbers([0, 0, 1]) == [0, 1]
    assert unique_numbers([100, 200, 100, 300]) == [100, 200, 300]
    assert unique_numbers([1, 3, 2, 4, 3]) == [1, 2, 3, 4]
    assert unique_numbers([5, 6, 7, 8]) == [5, 6, 7, 8]
    assert unique_numbers([]) == []
    assert unique_numbers([1, 1, 1, 1]) == [1]


# 113. Тесты для функции `create_frequency_dict`:
def test_create_frequency_dict():
    assert create_frequency_dict([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
    assert create_frequency_dict(["apple", "banana", "apple"]) == {"apple": 2, "banana": 1}
    assert create_frequency_dict([1, 1, 2, 2, 3]) == {1: 2, 2: 2, 3: 1}
    assert create_frequency_dict([]) == {}
    assert create_frequency_dict(["a", "a", "b", "c", "b"]) == {"a": 2, "b": 2, "c": 1}
    assert create_frequency_dict([5, 5, 5]) == {5: 3}
    assert create_frequency_dict([1, 2, 3, 4, 5]) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    assert create_frequency_dict([1, 1, 1, 1]) == {1: 4}
    assert create_frequency_dict([9, 8, 7, 6]) == {9: 1, 8: 1, 7: 1, 6: 1}
    assert create_frequency_dict([1, 1, 1]) == {1: 3}


# 114. Тесты для функции `difference_of_lists`:
def test_difference_of_lists():
    assert difference_of_lists([1, 2, 3], [3, 4, 5]) == [1, 2, 4, 5]
    assert difference_of_lists([1, 2], [2, 3]) == [1, 3]
    assert difference_of_lists([1, 2, 3], [1, 2, 3]) == []
    assert difference_of_lists([], [1, 2]) == [1, 2]
    assert difference_of_lists([5, 6, 7], [7, 8, 9]) == [5, 6, 8, 9]
    assert difference_of_lists([1], [1]) == []
    assert difference_of_lists([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert difference_of_lists([1, 3, 5], [2, 4, 6]) == [1, 3, 5, 2, 4, 6]
    assert difference_of_lists([1, 2, 3], []) == [1, 2, 3]
    assert difference_of_lists([], []) == []


# 115. Тесты для функции `find_in_collection`:
def test_find_in_collection():
    assert find_in_collection([1, 2, 3], {3, 4, 5}) == [3]
    assert find_in_collection([1, 2, 3], {4, 5, 6}) == []
    assert find_in_collection(["a", "b", "c"], {"b", "c", "d"}) == ["b", "c"]
    assert find_in_collection([1, 2], {1, 2, 3}) == [1, 2]
    assert find_in_collection([5, 6, 7], {7, 8}) == [7]
    assert find_in_collection([], {1, 2, 3}) == []
    assert find_in_collection([1, 2], set()) == []
    assert find_in_collection([1, 2, 3], {3, 4, 5}) == [3]
    assert find_in_collection(["apple", "banana"], {"banana", "orange"}) == ["banana"]
    assert find_in_collection([10, 20], {5, 10, 15}) == [10]


# 116. Тесты для функции `sum_of_duplicates`:
def test_sum_of_duplicates():
    assert sum_of_duplicates([1, 2, 2, 3, 4, 4]) == 6
    assert sum_of_duplicates([5, 5, 5, 5]) == 5
    assert sum_of_duplicates([1, 1, 1]) == 1
    assert sum_of_duplicates([10, 20, 30]) == 0
    assert sum_of_duplicates([1, 2, 3, 4, 5]) == 0
    assert sum_of_duplicates([1, 2, 2, 3, 3, 3, 4]) == 5
    assert sum_of_duplicates([7, 8, 9, 9, 9]) == 9
    assert sum_of_duplicates([10, 10, 10]) == 10
    assert sum_of_duplicates([1, 2, 2, 3, 3]) == 5
    assert sum_of_duplicates([1, 1, 1, 1, 1]) == 1


# 117. Тесты для функции `unique_in_first`:
def test_unique_in_first():
    assert unique_in_first([1, 2, 3], [3, 4, 5]) == [1, 2]
    assert unique_in_first([1, 2, 3], [4, 5, 6]) == [1, 2, 3]
    assert unique_in_first([5, 6, 7], [7, 8, 9]) == [5, 6]
    assert unique_in_first([1, 2], [1, 2]) == []
    assert unique_in_first([1, 2, 3], []) == [1, 2, 3]
    assert unique_in_first([], [1, 2, 3]) == []
    assert unique_in_first([10, 20, 30], [20, 40, 60]) == [10, 30]
    assert unique_in_first([1, 1, 2], [1, 3]) == [2]
    assert unique_in_first([100, 200], [100, 300]) == [200]
    assert unique_in_first([1, 2, 3], [3]) == [1, 2]


# 118. Тесты для функции `lcm_1`:
def test_lcm_1():
    assert lcm_1(4, 5) == 20
    assert lcm_1(0, 5) == None
    assert lcm_1(6, 8) == 24
    assert lcm_1(9, 12) == 36
    assert lcm_1(3, 7) == 21
    assert lcm_1(10, 0) == None
    assert lcm_1(13, 17) == 221
    assert lcm_1(15, 25) == 75
    assert lcm_1(1, 1) == 1
    assert lcm_1(10, 20) == 20


# 119. Тесты для функции `filter_dict_by_value`:
def test_filter_dict_by_value():
    assert filter_dict_by_value({"apple": 100, "banana": 50}, 1000) == {}
    assert filter_dict_by_value({"a": 5, "b": 10, "c": 2}, 4) == {"a": 5, "b": 10}
    assert filter_dict_by_value({"apple": 5, "banana": 3}, 4) == {"apple": 5}
    assert filter_dict_by_value({"x": 1, "y": 2, "z": 3}, 2) == {"z": 3}
    assert filter_dict_by_value({"a": 1, "b": 2}, 2) == {}
    assert filter_dict_by_value({}, 2) == {}
    assert filter_dict_by_value({"apple": 10, "banana": 20}, 15) == {"banana": 20}
    assert filter_dict_by_value({"a": 1, "b": 1, "c": 1}, 1) == {}
    assert filter_dict_by_value({"cat": 5, "dog": 3}, 4) == {"cat": 5}
    assert filter_dict_by_value({"cat": 1, "dog": 0}, 0) == {"cat": 1}
    assert filter_dict_by_value({"apple": 100, "banana": 50}, 60) == {"apple": 100}


# 120. Тесты для функции `reverse_dict`:
def test_reverse_dict():
    assert reverse_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert reverse_dict({"x": 10, "y": 20}) == {10: "x", 20: "y"}
    assert reverse_dict({"apple": 100, "banana": 200}) == {100: "apple", 200: "banana"}
    assert reverse_dict({"cat": 5, "dog": 3}) == {5: "cat", 3: "dog"}
    assert reverse_dict({"one": 1, "two": 2}) == {1: "one", 2: "two"}
    assert reverse_dict({"x": 1, "y": 1}) == {1: "x"}
    assert reverse_dict({"key1": "value1", "key2": "value2"}) == {"value1": "key1", "value2": "key2"}
    assert reverse_dict({}) == {}
    assert reverse_dict({"p": 0, "q": 0}) == {0: "p"}
    assert reverse_dict({"a": 10, "b": 10}) == {10: "a"}


# 121. Тесты для функции `multiples_from_list`:
def test_multiples_from_list():
    assert multiples_from_list([10, 20, 30], [2, 5]) == [10, 20, 30]
    assert multiples_from_list([11, 22, 33], [3, 7]) == [33]
    assert multiples_from_list([1, 2, 3], [4, 5]) == []
    assert multiples_from_list([6, 8, 10], [2]) == [6, 8, 10]
    assert multiples_from_list([9, 15, 25], [3, 5]) == [9, 15, 25]
    assert multiples_from_list([17, 19, 23], [4, 8]) == []
    assert multiples_from_list([12, 14, 18], [3, 6]) == [12, 18]
    assert multiples_from_list([5, 10, 20], [1]) == [5, 10, 20]
    assert multiples_from_list([], [2, 3]) == []


# 122. Тесты для функции `case_insensitive_char_frequency`:
def test_case_insensitive_char_frequency():
    assert case_insensitive_char_frequency("Hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert case_insensitive_char_frequency("AaBbCc") == {'a': 2, 'b': 2, 'c': 2}
    assert case_insensitive_char_frequency("Python!") == {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
    assert case_insensitive_char_frequency("Nope") == {'n': 1, 'o': 1, 'p': 1, 'e': 1}
    assert case_insensitive_char_frequency("MixedCase") == {'m': 1, 'i': 1, 'x': 1, 'e': 2, 'd': 1, 'c': 1, 'a': 1, 's': 1}
    assert case_insensitive_char_frequency("12345") == {}
    assert case_insensitive_char_frequency("") == {}
    assert case_insensitive_char_frequency("A") == {'a': 1}
    assert case_insensitive_char_frequency("ABaB") == {'a': 2, 'b': 2}


# 123. Тесты для функции `count_unique_with_frequency`:
def test_count_unique_with_frequency():
    assert count_unique_with_frequency([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
    assert count_unique_with_frequency(["a", "b", "a", "c", "c", "c"]) == {"a": 2, "b": 1, "c": 3}
    assert count_unique_with_frequency([5, 5, 5, 5, 5]) == {5: 5}
    assert count_unique_with_frequency([]) == {}
    assert count_unique_with_frequency([1, 2, 3]) == {1: 1, 2: 1, 3: 1}
    assert count_unique_with_frequency([0, 0, 1, 1, 1]) == {0: 2, 1: 3}
    assert count_unique_with_frequency(["x", "y", "z"]) == {"x": 1, "y": 1, "z": 1}
    assert count_unique_with_frequency([1, "1", 2, "2", 2]) == {1: 1, "1": 1, 2: 2, "2": 1}
    assert count_unique_with_frequency([3, 3, 3]) == {3: 3}


# 124. Тесты для функции `count_consecutive_chars`:
def test_count_consecutive_chars():
    assert count_consecutive_chars("aaabbcc") == {'a': 3, 'b': 2, 'c': 2}
    assert count_consecutive_chars("abcd") == {'a': 1, 'b': 1, 'c': 1, 'd': 1}
    assert count_consecutive_chars("aaAAa") == {'A': 2, 'a': 3}
    assert count_consecutive_chars("") == {}
    assert count_consecutive_chars("x") == {'x': 1}
    assert count_consecutive_chars("zzz") == {'z': 3}
    assert count_consecutive_chars("aabbccdd") == {'a': 2, 'b': 2, 'c': 2, 'd': 2}
    assert count_consecutive_chars("aaaAAA") == {'a': 3, 'A': 3}
    assert count_consecutive_chars("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert count_consecutive_chars("aaraaraarraarrr") == {'a': 8, 'r': 7}


# 125. Тесты для функции `find_keys_in_set`:
def test_find_keys_in_set():
    assert find_keys_in_set({1, 2, 3}, {1: "one", 2: "two", 4: "four"}) == [1, 2]
    assert find_keys_in_set({"a", "b", "c"}, {"a": "alpha", "b": "beta"}) == ["a", "b"]
    assert find_keys_in_set({5, 6, 7}, {8: "eight", 9: "nine"}) == []
    assert find_keys_in_set(set(), {"a": 1, "b": 2}) == []
    assert find_keys_in_set({1, 2, 3}, {}) == []
    assert find_keys_in_set({1, 2}, {1: "one", 2: "two"}) == [1, 2]
    assert find_keys_in_set({"x"}, {"x": "ex"}) == ["x"]
    assert find_keys_in_set({"y"}, {"z": "zee"}) == []
    assert find_keys_in_set({"hello", "world"}, {"hello": "greeting", "earth": "planet"}) == ["hello"]


# 126. Тесты для функции `find_prime_numbers`:
def test_find_prime_numbers():
    assert find_prime_numbers([2, 3, 4, 5, 6]) == [2, 3, 5]
    assert find_prime_numbers([10, 11, 12, 13, 14]) == [11, 13]
    assert find_prime_numbers([1, 2]) == [2]
    assert find_prime_numbers([15, 16, 17, 18]) == [17]
    assert find_prime_numbers([]) == []
    assert find_prime_numbers([0, 1]) == []
    assert find_prime_numbers([19, 20, 21, 22]) == [19]
    assert find_prime_numbers([23, 24, 25, 26]) == [23]
    assert find_prime_numbers([2, 2, 3, 3]) == [2, 2, 3, 3]


# 127. Тесты для функции `split_digits_and_others`:
def test_split_digits_and_others():
    assert split_digits_and_others("123abc") == (['1', '2', '3'], ['a', 'b', 'c'])
    assert split_digits_and_others("1a2b3c") == (['1', '2', '3'], ['a', 'b', 'c'])
    assert split_digits_and_others("") == ([], [])
    assert split_digits_and_others("123") == (['1', '2', '3'], [])
    assert split_digits_and_others("abc") == ([], ['a', 'b', 'c'])
    assert split_digits_and_others("1!2@3#") == (['1', '2', '3'], ['!', '@', '#'])
    assert split_digits_and_others("a1b2c3") == (['1', '2', '3'], ['a', 'b', 'c'])
    assert split_digits_and_others("456def") == (['4', '5', '6'], ['d', 'e', 'f'])
    assert split_digits_and_others("xyz789") == (['7', '8', '9'], ['x', 'y', 'z'])


# 128. Тесты для функции `min_max_tuple`:
def test_min_max_tuple():
    assert min_max_tuple([1, 2, 3]) == (1, 3)
    assert min_max_tuple([10, 5, 15]) == (5, 15)
    assert min_max_tuple([0, -1, 1]) == (-1, 1)
    assert min_max_tuple([-10, -5, -1]) == (-10, -1)
    assert min_max_tuple([1]) == (1, 1)
    assert min_max_tuple([]) == None
    assert min_max_tuple([100, 200, 300]) == (100, 300)
    assert min_max_tuple([-100, 0, 100]) == (-100, 100)
    assert min_max_tuple([7, 7, 7]) == (7, 7)


# 129. Тесты для функции `find_common_keys_with_different_values`:
def test_find_common_keys_with_different_values():
    assert find_common_keys_with_different_values(
        {'a': 1, 'b': 2}, {'a': 2, 'b': 2}) == ['a']
    assert find_common_keys_with_different_values(
        {'x': 1, 'y': 2}, {'y': 3, 'z': 4}) == ['y']
    assert find_common_keys_with_different_values(
        {'k': 10, 'l': 20}, {'m': 30, 'n': 40}) == []
    assert find_common_keys_with_different_values({}, {}) == []
    assert find_common_keys_with_different_values(
        {'a': 1, 'b': 1}, {'a': 1, 'b': 2}) == ['b']
    assert find_common_keys_with_different_values(
        {'key1': 100, 'key2': 200}, {'key1': 300, 'key2': 200}) == ['key1']
    assert find_common_keys_with_different_values(
        {'k1': 1, 'k2': 2}, {'k2': 3, 'k3': 4}) == ['k2']
    assert find_common_keys_with_different_values(
        {'a': 1}, {'a': 2}) == ['a']
    assert find_common_keys_with_different_values(
        {'x': 5}, {'y': 5}) == []


# 130. Тесты для функции `string_to_numbers`:
def test_string_to_numbers():
    assert string_to_numbers("1 2 3") == [1, 2, 3]
    assert string_to_numbers("10 20 30") == [10, 20, 30]
    assert string_to_numbers("4 5 6") == [4, 5, 6]
    assert string_to_numbers("a b c") == []
    assert string_to_numbers("123 abc 456") == []
    assert string_to_numbers("") == []
    assert string_to_numbers("7 8 9") == [7, 8, 9]
    assert string_to_numbers("0") == [0]
    assert string_to_numbers("0 1 2") == [0, 1, 2]


# 131. Тесты для функции `find_powers_of_two_in_string`:
def test_find_powers_of_two_in_string():
    assert find_powers_of_two_in_string("1 2 3 4 5") == [1, 2, 4]
    assert find_powers_of_two_in_string("16 32 64") == [16, 32, 64]
    assert find_powers_of_two_in_string("7 9 11") == []
    assert find_powers_of_two_in_string("0 128 256") == [128, 256]
    assert find_powers_of_two_in_string("2 4 8 16 32") == [2, 4, 8, 16, 32]
    assert find_powers_of_two_in_string("1024") == [1024]
    assert find_powers_of_two_in_string("non-numeric 2 words") == [2]
    assert find_powers_of_two_in_string("") == []
    assert find_powers_of_two_in_string("3 6 12") == []


# 132. Тесты для функции `find_palindromes`:
def test_find_palindromes():
    assert find_palindromes(["radar", "hello", "level"]) == ["radar", "level"]
    assert find_palindromes(["world", "noon", "civic"]) == ["noon", "civic"]
    assert find_palindromes(["abc", "def", "ghi"]) == []
    assert find_palindromes(["madam", "racecar", "apple"]) == ["madam", "racecar"]
    assert find_palindromes([]) == []
    assert find_palindromes(["kayak", "refer"]) == ["kayak", "refer"]
    assert find_palindromes(["", "a", "bb"]) == ["", "a", "bb"]
    assert find_palindromes(["rotor", "deed"]) == ["rotor", "deed"]
    assert find_palindromes(["not", "a", "palindrome"]) == ['a']


# 133. Тесты для функции `merge_lists_no_duplicates`:
def test_merge_lists_no_duplicates():
    assert merge_lists_no_duplicates([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge_lists_no_duplicates(["a", "b"], ["b", "c"]) == ["a", "b", "c"]
    assert merge_lists_no_duplicates([], [1, 2, 3]) == [1, 2, 3]
    assert merge_lists_no_duplicates([1, 2, 3], []) == [1, 2, 3]
    assert merge_lists_no_duplicates([1], [1, 2, 3]) == [1, 2, 3]
    assert merge_lists_no_duplicates(["x", "y"], ["y", "z"]) == ["x", "y", "z"]
    assert merge_lists_no_duplicates([1, 1, 1], [1, 1, 1]) == [1, 1, 1]
    assert merge_lists_no_duplicates([4, 5, 6], [7, 8, 9]) == [4, 5, 6, 7, 8, 9]
    assert merge_lists_no_duplicates([10, 20], [20, 30, 40]) == [10, 20, 30, 40]


# 134. Тесты для функции `divisible_by_2_not_3`:
def test_divisible_by_2_not_3():
    assert divisible_by_2_not_3([2, 4, 6, 8]) == [2, 4, 8]
    assert divisible_by_2_not_3([12, 15, 20]) == [20]
    assert divisible_by_2_not_3([3, 5, 9]) == []
    assert divisible_by_2_not_3([18, 21, 24]) == []
    assert divisible_by_2_not_3([1, 2, 3]) == [2]
    assert divisible_by_2_not_3([10, 14, 22]) == [10, 14, 22]
    assert divisible_by_2_not_3([0, 6, 12]) == []
    assert divisible_by_2_not_3([7, 8, 9]) == [8]
    assert divisible_by_2_not_3([]) == []


# 135. Тесты для функции `find_even_numbers_in_string`:
def test_find_even_numbers_in_string():
    assert find_even_numbers_in_string("12 34 56") == [12, 34, 56]
    assert find_even_numbers_in_string("135 246 789") == [246]
    assert find_even_numbers_in_string("11 33 55") == []
    assert find_even_numbers_in_string("222 333 444") == [222, 444]
    assert find_even_numbers_in_string("2 4 6 8") == [2, 4, 6, 8]
    assert find_even_numbers_in_string("9") == []
    assert find_even_numbers_in_string("10 20 30") == [10, 20, 30]
    assert find_even_numbers_in_string("") == []
    assert find_even_numbers_in_string("100 200") == [100, 200]


# 136. Тесты для функции `find_non_prime_numbers`:
def test_find_non_prime_numbers():
    assert find_non_prime_numbers([1, 2, 3, 4, 5]) == [1, 4]
    assert find_non_prime_numbers([10, 11, 12, 13]) == [10, 12]
    assert find_non_prime_numbers([17, 19, 21, 23]) == [21]
    assert find_non_prime_numbers([24, 25, 26, 27]) == [24, 25, 26, 27]
    assert find_non_prime_numbers([29, 30, 31]) == [30]
    assert find_non_prime_numbers([2, 3, 5]) == []
    assert find_non_prime_numbers([4, 6, 8]) == [4, 6, 8]
    assert find_non_prime_numbers([]) == []
    assert find_non_prime_numbers([0, 1, 2]) == [0, 1]


# 137. Тесты для функции `unique_chars_ignore_spaces`:
def test_unique_chars_ignore_spaces():
    assert unique_chars_ignore_spaces("hello world") == ['h', 'e', 'l', 'o', 'w', 'r', 'd']
    assert unique_chars_ignore_spaces("a b c") == ['a', 'b', 'c']
    assert unique_chars_ignore_spaces("abc abc") == ['a', 'b', 'c']
    assert unique_chars_ignore_spaces("  ") == []
    assert unique_chars_ignore_spaces("unique characters") == ['u', 'n', 'i', 'q', 'e', 'c', 'h', 'a', 'r', 't', 's']
    assert unique_chars_ignore_spaces("xyz 123") == ['x', 'y', 'z', '1', '2', '3']
    assert unique_chars_ignore_spaces("AAA") == ['A']
    assert unique_chars_ignore_spaces("alpha beta") == ['a', 'l', 'p', 'h', 'b', 'e', 't']
    assert unique_chars_ignore_spaces("ignore spaces") == ['i', 'g', 'n', 'o', 'r', 'e', 's', 'p', 'a', 'c']


# 138. Тесты для функции `count_words_ignore_punctuation`:
def test_count_words_ignore_punctuation():
    assert count_words_ignore_punctuation("hello world!") == 2
    assert count_words_ignore_punctuation("a b c") == 3
    assert count_words_ignore_punctuation("this, is a test.") == 4
    assert count_words_ignore_punctuation("...") == 0
    assert count_words_ignore_punctuation("count these words!") == 3
    assert count_words_ignore_punctuation("punctuation, should be ignored.") == 4
    assert count_words_ignore_punctuation("") == 0
    assert count_words_ignore_punctuation("one two three") == 3
    assert count_words_ignore_punctuation("   ") == 0


# 139. Тесты для функции `find_squares`:
def test_find_squares():
    assert find_squares([1, 4, 9, 16, 25]) == [1, 4, 9, 16, 25]
    assert find_squares([2, 3, 5, 6, 7]) == []
    assert find_squares([36, 49, 64, 81]) == [36, 49, 64, 81]
    assert find_squares([10, 20, 30]) == []
    assert find_squares([100, 121, 144]) == [100, 121, 144]
    assert find_squares([]) == []
    assert find_squares([0, 1, 2, 3]) == [0, 1]
    assert find_squares([50, 60, 70, 80]) == []
    assert find_squares([9, 25, 36, 49]) == [9, 25, 36, 49]


# 140. Тесты для функции `word_frequency_in_string`:
def test_word_frequency_in_string():
    assert word_frequency_in_string("hello world") == {'hello': 1, 'world': 1}
    assert word_frequency_in_string("hello hello world") == {'hello': 2, 'world': 1}
    assert word_frequency_in_string("test test test") == {'test': 3}
    assert word_frequency_in_string("a b a b c") == {'a': 2, 'b': 2, 'c': 1}
    assert word_frequency_in_string("one two three two one") == {'one': 2, 'two': 2, 'three': 1}
    assert word_frequency_in_string("punctuation should be ignored") == {'punctuation': 1, 'should': 1, 'be': 1, 'ignored': 1}
    assert word_frequency_in_string("the quick brown fox") == {'the': 1, 'quick': 1, 'brown': 1, 'fox': 1}
    assert word_frequency_in_string("hello world!") == {'hello': 1, 'world': 1}
    assert word_frequency_in_string("repeat repeat repeat repeat") == {'repeat': 4}


# 141. Тесты для функции `find_sum_of_two_squares`:
def test_find_sum_of_two_squares():
    assert find_sum_of_two_squares([1, 2, 3, 4, 5, 10, 25]) == [1, 2, 4, 5, 10, 25]
    assert find_sum_of_two_squares([0, 1, 2, 9, 16, 20, 25]) == [1, 2, 9, 16, 20, 25]
    assert find_sum_of_two_squares([3, 5, 7, 8, 10, 15, 50]) == [5, 8, 10, 50]


# 142. Тесты для функции `find_non_numeric_elements`:
def test_find_non_numeric_elements():
    assert find_non_numeric_elements(["hello", "123", "world", "456"]) == ["hello", "world"]
    assert find_non_numeric_elements(["abc", "def", "456", "789"]) == ["abc", "def"]
    assert find_non_numeric_elements(["123", "456", "789"]) == []


# 143. Тесты для функции `find_odd_and_divisible_by_5`:
def test_find_odd_and_divisible_by_5():
    assert find_odd_and_divisible_by_5([5, 10, 15, 20, 25, 30]) == [5, 15, 25]
    assert find_odd_and_divisible_by_5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [5]
    assert find_odd_and_divisible_by_5([2, 4, 6, 8, 10]) == []


# 144. Тесты для функции `count_elements_above_threshold`:
def test_count_elements_above_threshold():
    assert count_elements_above_threshold({"a": 5, "b": 10, "c": 15}, 7) == 2
    assert count_elements_above_threshold({"a": 1, "b": 2, "c": 3}, 2) == 1
    assert count_elements_above_threshold({"a": 20, "b": 25, "c": 30}, 15) == 3


# 145. Тесты для функции `find_powers_of_three`:
def test_find_powers_of_three():
    assert find_powers_of_three([1, 3, 9, 27, 81, 243]) == [1, 1, 1, 1, 1, 1]
    assert find_powers_of_three([1, 2, 4, 8, 16]) == [1]
    assert find_powers_of_three([1, 3, 9, 27, 81, 243]) == [1, 1, 1, 1, 1, 1]


# 146. Тесты для функции `find_numbers_greater_than_mean`:
def test_find_numbers_greater_than_mean():
    assert find_numbers_greater_than_mean("1 2 3 4 5 6 7 8 9") == [6, 7, 8, 9]
    assert find_numbers_greater_than_mean("10 20 30 40 50") == [40, 50]
    assert find_numbers_greater_than_mean("5 5 5 5 5") == []


# 147. Тесты для функции `find_odd_and_not_prime`:
def test_find_odd_and_not_prime():
    assert find_odd_and_not_prime([1, 3, 5, 7, 9, 11, 13, 15]) == [1, 9, 15]
    assert find_odd_and_not_prime([2, 4, 6, 8, 10]) == []
    assert find_odd_and_not_prime([21, 33, 35, 39]) == [21, 33, 35, 39]


# 148. Тесты для функции `find_divisors_in_list`:
def test_find_divisors_in_list():
    assert find_divisors_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert find_divisors_in_list([10, 20, 30, 40]) == [20, 30, 40]
    assert find_divisors_in_list([1, 3, 5, 7]) == [3, 5, 7]


# 149. Тесты для функции `find_non_multiples`:
def test_find_non_multiples():
    assert find_non_multiples([1, 2, 3, 4, 5, 6], [2, 3]) == [1, 5]
    assert find_non_multiples([10, 15, 20, 25], [5]) == []
    assert find_non_multiples([8, 16, 24], [4]) == []


# 150. Тесты для функции `find_common_elements`:
def test_find_common_elements():
    assert find_common_elements([1, 2, 3], [3, 4, 5]) == [3]
    assert find_common_elements(["a", "b", "c"], ["c", "d", "e"]) == ["c"]
    assert find_common_elements([1, 2, 3], [4, 5, 6]) == []


# 151. Тесты для функции `find_odd_square`:
def test_find_odd_square():
    assert find_odd_square([1, 2, 3, 4, 5, 9, 16, 25]) == [1, 9, 25]
    assert find_odd_square([2, 4, 6, 8, 10, 12, 14, 18]) == []
    assert find_odd_square([1, 5, 13, 15, 21, 22, 27, 28]) == [1]


# 152. Тесты для функции `find_elements_with_vowels`:
def test_find_elements_with_vowels():
    assert find_elements_with_vowels(["hello", "world", "sky", "tryst"]) == ["hello", "world"]
    assert find_elements_with_vowels(["rhythm", "gym", "sky"]) == []
    assert find_elements_with_vowels(["apple", "banana", "grape"]) == ["apple", "banana", "grape"]


# 153. Тесты для функции `find_not_divisible_by_2_and_3`:
def test_find_not_divisible_by_2_and_3():
    assert find_not_divisible_by_2_and_3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 5, 7]
    assert find_not_divisible_by_2_and_3([2, 4, 6, 8, 10]) == []
    assert find_not_divisible_by_2_and_3([11, 13, 17, 19, 23, 25, 29]) == [11, 13, 17, 19, 23, 25, 29]


# 154. Тесты для функции `count_unique_chars_in_string`:
def test_count_unique_chars_in_string():
    assert count_unique_chars_in_string("hello world") == {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
    assert count_unique_chars_in_string("abcdefg") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1}
    assert count_unique_chars_in_string("1234 5678") == {}


# 155. Тесты для функции `find_product_of_two_even_numbers`:
def test_find_product_of_two_even_numbers():
    assert find_product_of_two_even_numbers([4, 8, 12, 16, 20]) == [4, 8, 12, 16, 20]
    assert find_product_of_two_even_numbers([1, 3, 5, 7, 9]) == []
    assert find_product_of_two_even_numbers([6, 10, 14, 18, 22]) == []


# 156. Тесты для функции `find_multiples_of_5_not_10`:
def test_find_multiples_of_5_not_10():
    assert find_multiples_of_5_not_10([5, 10, 15, 20, 25, 30]) == [5, 15, 25]
    assert find_multiples_of_5_not_10([2, 4, 6, 8, 10]) == []
    assert find_multiples_of_5_not_10([1, 3, 7, 9, 11]) == []


# 157. Тесты для функции `find_double_digits_not_divisible_by_2`:
def test_find_double_digits_not_divisible_by_2():
    assert find_double_digits_not_divisible_by_2([10, 12, 14, 16, 18]) == []
    assert find_double_digits_not_divisible_by_2([11, 13, 15, 17, 19]) == [11, 13, 15, 17, 19]
    assert find_double_digits_not_divisible_by_2([21, 23, 25, 27, 29]) == [21, 23, 25, 27, 29]


# 158. Тесты для функции `find_common_numbers_in_strings`:
def test_find_common_numbers_in_strings():
    assert find_common_numbers_in_strings("1 2 3 4 5", "3 4 5 6 7") == {3, 4, 5}
    assert find_common_numbers_in_strings("1 2 3 4 5", "6 7 8 9 10") == set()
    assert find_common_numbers_in_strings("10 20 30 40 50", "15 25 35 45 55") == set()


# 159. Тесты для функции `find_divisible_by_7_not_11`:
def test_find_divisible_by_7_not_11():
    assert find_divisible_by_7_not_11([7, 14, 21, 28, 35, 42]) == [7, 14, 21, 28, 35, 42]
    assert find_divisible_by_7_not_11([11, 22, 33, 44, 55, 66]) == []
    assert find_divisible_by_7_not_11([49, 63, 77, 84]) == [49, 63, 84]


# 160. Тесты для функции `count_word_in_string`:
def test_count_word_in_string():
    assert count_word_in_string("Hello world, hello universe", "hello") == 2
    assert count_word_in_string("Python is great. I love Python.", "Python") == 1
    assert count_word_in_string("This is a test string.", "python") == 0


# 161. Тесты для функции `find_primes_not_multiples_of_3`
def test_find_primes_not_multiples_of_3():
    assert find_primes_not_multiples_of_3([2, 3, 5, 6, 7, 9, 11, 12]) == [2, 5, 7, 11]
    assert find_primes_not_multiples_of_3([3, 6, 9, 12, 15]) == []
    assert find_primes_not_multiples_of_3([1, 2, 4, 5, 8, 10, 14]) == [2, 5]
    assert find_primes_not_multiples_of_3([7, 11, 13, 17, 19, 23]) == [7, 11, 13, 17, 19, 23]
    assert find_primes_not_multiples_of_3([]) == []
    assert find_primes_not_multiples_of_3([29, 31, 37, 41]) == [29, 31, 37, 41]
    assert find_primes_not_multiples_of_3([9, 27, 30]) == []
    assert find_primes_not_multiples_of_3([2, 3, 5, 9, 15, 21]) == [2, 5]
    assert find_primes_not_multiples_of_3([4, 6, 8, 10, 12, 14]) == []


# 162. Тесты для функции `find_even_numbers_divisible_by_4`
def test_find_even_numbers_divisible_by_4():
    assert find_even_numbers_divisible_by_4([4, 8, 12, 16, 20, 24]) == [4, 8, 12, 16, 20, 24]
    assert find_even_numbers_divisible_by_4([1, 2, 3, 5, 7, 11]) == []
    assert find_even_numbers_divisible_by_4([4, 5, 6, 7, 8, 9, 10, 11]) == [4, 8]
    assert find_even_numbers_divisible_by_4([32, 48, 64, 80, 96, 112]) == [32, 48, 64, 80, 96, 112]
    assert find_even_numbers_divisible_by_4([]) == []
    assert find_even_numbers_divisible_by_4([12, 14, 18, 20]) == [12, 20]
    assert find_even_numbers_divisible_by_4([3, 5, 7, 9, 11]) == []
    assert find_even_numbers_divisible_by_4([0, 4, 8, 16, 32]) == [0, 4, 8, 16, 32]
    assert find_even_numbers_divisible_by_4([2, 6, 10, 14]) == []


# 163. Тесты для функции `find_non_powers_of_two`
def test_find_non_powers_of_two():
    assert find_non_powers_of_two([1, 2, 3, 4, 5, 6, 7, 8]) == [3, 5, 6, 7]
    assert find_non_powers_of_two([8, 16, 32, 64, 128]) == []
    assert find_non_powers_of_two([3, 5, 6, 7, 10, 12]) == [3, 5, 6, 7, 10, 12]
    assert find_non_powers_of_two([1, 2, 4, 8, 16]) == []
    assert find_non_powers_of_two([]) == []
    assert find_non_powers_of_two([1024, 2048, 4096]) == []
    assert find_non_powers_of_two([1, 2, 4, 6, 8, 12, 18]) == [6, 12, 18]
    assert find_non_powers_of_two([10, 20, 30, 40]) == [10, 20, 30, 40]
    assert find_non_powers_of_two([7, 14, 21, 28]) == [7, 14, 21, 28]


# 164. Тесты для функции `count_numbers_greater_than_average`
def test_count_numbers_greater_than_average():
    assert count_numbers_greater_than_average("1 2 3 4 5 6 7 8 9") == 4
    assert count_numbers_greater_than_average("10 20 30 40 50") == 2
    assert count_numbers_greater_than_average("5 5 5 5") == 0
    assert count_numbers_greater_than_average("100") == 0
    assert count_numbers_greater_than_average("") == 0
    assert count_numbers_greater_than_average("10 15 20 25 30") == 2
    assert count_numbers_greater_than_average("7 14 21 28") == 2
    assert count_numbers_greater_than_average("3 6 9 12 15 18") == 3
    assert count_numbers_greater_than_average("0 1 2 3 4 5 6 7 8 9 10") == 5


# 165. Тесты для функции `find_multiples_of_4_or_5_not_20`
def test_find_multiples_of_4_or_5_not_20():
    assert find_multiples_of_4_or_5_not_20([4, 5, 8, 10, 12, 15, 16, 25, 40]) == [4, 5, 8, 10, 12, 15, 16, 25]
    assert find_multiples_of_4_or_5_not_20([20, 40, 60, 80, 100]) == []
    assert find_multiples_of_4_or_5_not_20([3, 6, 9, 11, 13, 17, 19]) == []
    assert find_multiples_of_4_or_5_not_20([25, 30, 35, 50]) == [25, 30, 35, 50]
    assert find_multiples_of_4_or_5_not_20([]) == []
    assert find_multiples_of_4_or_5_not_20([4, 8, 12, 16, 24]) == [4, 8, 12, 16, 24]
    assert find_multiples_of_4_or_5_not_20([5, 10, 15, 25]) == [5, 10, 15, 25]
    assert find_multiples_of_4_or_5_not_20([1, 2, 3, 7, 11]) == []
    assert find_multiples_of_4_or_5_not_20([9, 27, 33, 45]) == [45]


# 166. Тесты для функции `find_exact_divisors_of_100`
def test_find_exact_divisors_of_100():
    assert find_exact_divisors_of_100([1, 2, 4, 5, 10, 20, 25, 50, 100]) == [1, 2, 4, 5, 10, 20, 25, 50, 100]
    assert find_exact_divisors_of_100([3, 6, 9, 12, 15, 18, 21]) == []
    assert find_exact_divisors_of_100([4, 8, 16, 32, 64]) == [4]
    assert find_exact_divisors_of_100([50, 100]) == [50, 100]
    assert find_exact_divisors_of_100([]) == []
    assert find_exact_divisors_of_100([10, 20, 30, 40]) == [10, 20]
    assert find_exact_divisors_of_100([1, 25, 100]) == [1, 25, 100]
    assert find_exact_divisors_of_100([5, 15, 20]) == [5, 20]
    assert find_exact_divisors_of_100([7, 14, 21, 35, 70]) == []


# 167. Тесты для функции `find_odd_not_divisible_by_5`
def test_find_odd_not_divisible_by_5():
    assert find_odd_not_divisible_by_5([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [1, 3, 7, 9, 11, 13, 17, 19]
    assert find_odd_not_divisible_by_5([5, 10, 15, 20, 25]) == []
    assert find_odd_not_divisible_by_5([2, 4, 6, 8, 10, 12]) == []
    assert find_odd_not_divisible_by_5([1, 2, 3, 4, 5]) == [1, 3]
    assert find_odd_not_divisible_by_5([]) == []
    assert find_odd_not_divisible_by_5([11, 12, 13, 14, 15, 16]) == [11, 13]
    assert find_odd_not_divisible_by_5([1, 21, 31, 41]) == [1, 21, 31, 41]
    assert find_odd_not_divisible_by_5([25, 30, 35, 40, 45, 50]) == []
    assert find_odd_not_divisible_by_5([33, 37, 39, 43, 47]) == [33, 37, 39, 43, 47]


# 168. Тесты для функции `find_multiples_of_2_or_3`
def test_find_multiples_of_2_or_3():
    assert find_multiples_of_2_or_3([2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [2, 3, 4, 8, 9, 10]
    assert find_multiples_of_2_or_3([3, 6, 9, 12, 15, 18, 21]) == [3, 9, 15, 21]
    assert find_multiples_of_2_or_3([2, 4, 6, 8, 10, 12]) == [2, 4, 8, 10]
    assert find_multiples_of_2_or_3([1, 3, 5, 7, 9, 11]) == [3, 9]
    assert find_multiples_of_2_or_3([]) == 'No numbers found that are multiples of 2 or 3, but not both.'
    assert find_multiples_of_2_or_3([6, 12, 18, 24]) == 'No numbers found that are multiples of 2 or 3, but not both.'
    assert find_multiples_of_2_or_3([3, 6, 7, 9, 14]) == [3, 9, 14]
    assert find_multiples_of_2_or_3([2, 3, 5, 7]) == [2, 3]
    assert find_multiples_of_2_or_3([5, 10, 15, 20, 25, 30]) == [10, 15, 20]


# 169. Тесты для функции `find_odd_or_divisible_by_4`
def test_find_odd_or_divisible_by_4():
    assert find_odd_or_divisible_by_4([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 4, 5, 7, 8, 9]
    assert find_odd_or_divisible_by_4([2, 4, 6, 8, 10]) == [4, 8]
    assert find_odd_or_divisible_by_4([1, 3, 5, 7, 9, 11, 13, 15]) == [1, 3, 5, 7, 9, 11, 13, 15]
    assert find_odd_or_divisible_by_4([4, 8, 12, 16, 20]) == [4, 8, 12, 16, 20]
    assert find_odd_or_divisible_by_4([]) == 'No odd numbers or numbers divisible by 4 found.'
    assert find_odd_or_divisible_by_4([3, 5, 6, 7]) == [3, 5, 7]
    assert find_odd_or_divisible_by_4([10, 12, 14, 16]) == [12, 16]
    assert find_odd_or_divisible_by_4([2, 3, 4, 5]) == [3, 4, 5]
    assert find_odd_or_divisible_by_4([9, 10, 12, 15]) == [9, 12, 15]


# 170. Тесты для функции `find_even_squares`
def test_find_even_squares():
    assert find_even_squares([4, 16, 25, 36, 49, 64, 81, 100]) == [4, 16, 36, 64, 100]
    assert find_even_squares([1, 3, 5, 7, 9]) == 'No even square numbers found.'
    assert find_even_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [4]
    assert find_even_squares([9, 25, 49, 81, 121]) == 'No even square numbers found.'
    assert find_even_squares([]) == 'No even square numbers found.'
    assert find_even_squares([0, 4, 8, 12]) == [0, 4]
    assert find_even_squares([2, 6, 8, 10, 14, 18]) == 'No even square numbers found.'
    assert find_even_squares([4, 5, 6, 7, 8, 9]) == [4]
    assert find_even_squares([4, 16, 36, 64]) == [4, 16, 36, 64]


# 171. Тесты для функции `find_multiples_of_3_or_5_not_both`
def test_find_multiples_of_3_or_5_not_both():
    assert find_multiples_of_3_or_5_not_both([3, 5, 6, 10, 15, 18, 20]) == [3, 5, 6, 10, 18, 20]
    assert find_multiples_of_3_or_5_not_both([15, 30, 45, 60]) == 'No numbers found that are multiples of 3 or 5 but not both.'
    assert find_multiples_of_3_or_5_not_both([1, 2, 4, 7]) == 'No numbers found that are multiples of 3 or 5 but not both.'
    assert find_multiples_of_3_or_5_not_both([3, 6, 9, 12, 18]) == [3, 6, 9, 12, 18]
    assert find_multiples_of_3_or_5_not_both([]) == 'No numbers found that are multiples of 3 or 5 but not both.'
    assert find_multiples_of_3_or_5_not_both([5, 10, 20, 25]) == [5, 10, 20, 25]
    assert find_multiples_of_3_or_5_not_both([7, 11, 13]) == 'No numbers found that are multiples of 3 or 5 but not both.'
    assert find_multiples_of_3_or_5_not_both([2, 4, 8, 16]) == 'No numbers found that are multiples of 3 or 5 but not both.'
    assert find_multiples_of_3_or_5_not_both([15, 25, 35, 45]) == [25, 35]


# 172. Тесты для функции `count_numbers_greater_than_mean`
def test_count_numbers_greater_than_mean():
    assert count_numbers_greater_than_mean("1 2 3 4 5") == 2
    assert count_numbers_greater_than_mean("10 20 30 40") == 2
    assert count_numbers_greater_than_mean("5 5 5 5 5") == "No numbers greater than the mean."
    assert count_numbers_greater_than_mean("100") == "No numbers greater than the mean."
    assert count_numbers_greater_than_mean("") == "No numbers found in the string."
    assert count_numbers_greater_than_mean("10 20 30") == 1
    assert count_numbers_greater_than_mean("1 1 1 1 1 2 2 2 2 2") == 5
    assert count_numbers_greater_than_mean("50 100 150 200") == 2
    assert count_numbers_greater_than_mean("6 7 8 9 10") == 2


# 173. Тесты для функции `find_powers_of_2`
def test_find_powers_of_2():
    assert find_powers_of_2([1, 2, 3, 4, 5, 8, 16, 32, 64]) == [1, 2, 4, 8, 16, 32, 64]
    assert find_powers_of_2([7, 14, 21, 28]) == 'No powers of 2 found.'
    assert find_powers_of_2([2, 3, 6, 7, 9, 12]) == [2]
    assert find_powers_of_2([]) == 'No powers of 2 found.'
    assert find_powers_of_2([1024, 2048, 4096]) == [1024, 2048, 4096]
    assert find_powers_of_2([1, 4, 8, 16, 32]) == [1, 4, 8, 16, 32]
    assert find_powers_of_2([1, 2, 3, 4, 6, 7]) == [1, 2, 4]
    assert find_powers_of_2([5, 10, 20, 40]) == 'No powers of 2 found.'
    assert find_powers_of_2([64, 128, 256, 512]) == [64, 128, 256, 512]


# 174. Тесты для функции `find_even_and_divisible_by_8`
def test_find_even_and_divisible_by_8():
    assert find_even_and_divisible_by_8([8, 16, 24, 32, 40, 48, 56, 64]) == [8, 16, 24, 32, 40, 48, 56, 64]
    assert find_even_and_divisible_by_8([7, 14, 21, 28]) == 'No even numbers divisible by 8 found.'
    assert find_even_and_divisible_by_8([2, 4, 6, 10, 12, 14]) == 'No even numbers divisible by 8 found.'
    assert find_even_and_divisible_by_8([8, 16, 32, 40]) == [8, 16, 32, 40]
    assert find_even_and_divisible_by_8([]) == 'No even numbers divisible by 8 found.'
    assert find_even_and_divisible_by_8([80, 96, 112]) == [80, 96, 112]
    assert find_even_and_divisible_by_8([1, 3, 5, 7]) == 'No even numbers divisible by 8 found.'
    assert find_even_and_divisible_by_8([0, 8, 16, 24]) == [0, 8, 16, 24]
    assert find_even_and_divisible_by_8([9, 18, 27, 36]) == 'No even numbers divisible by 8 found.'


# 175. Тесты для функции `find_odd_and_divisible_by_3`
def test_find_odd_and_divisible_by_3():
    assert find_odd_and_divisible_by_3([3, 6, 9, 12, 15, 18, 21, 24]) == [3, 9, 15, 21]
    assert find_odd_and_divisible_by_3([2, 4, 6, 8, 10, 12]) == 'No odd numbers divisible by 3 found.'
    assert find_odd_and_divisible_by_3([5, 10, 15, 20, 25, 30]) == [15]
    assert find_odd_and_divisible_by_3([1, 2, 3, 4, 5]) == [3]
    assert find_odd_and_divisible_by_3([]) == 'No odd numbers divisible by 3 found.'
    assert find_odd_and_divisible_by_3([9, 18, 27, 36]) == [9, 27]
    assert find_odd_and_divisible_by_3([3, 5, 7, 11, 13, 15]) == [3, 15]
    assert find_odd_and_divisible_by_3([21, 33, 45, 57]) == [21, 33, 45, 57]
    assert find_odd_and_divisible_by_3([8, 16, 32, 64]) == 'No odd numbers divisible by 3 found.'


# 176. Тесты для функции `find_non_even_or_not_multiples_of_7`
def test_find_non_even_or_not_multiples_of_7():
    assert find_non_even_or_not_multiples_of_7([2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3, 4, 5, 6, 7, 8, 9]
    assert find_non_even_or_not_multiples_of_7([7, 14, 21, 28]) == [7, 21]
    assert find_non_even_or_not_multiples_of_7([1, 2, 4, 8, 16, 32]) == [1, 2, 4, 8, 16, 32]
    assert find_non_even_or_not_multiples_of_7([2, 3, 5, 7]) == [2, 3, 5, 7]
    assert find_non_even_or_not_multiples_of_7([0, 7, 14, 21]) == [7, 21]
    assert find_non_even_or_not_multiples_of_7([9, 18, 27, 36]) == [9, 18, 27, 36]
    assert find_non_even_or_not_multiples_of_7([3, 7, 10, 13]) == [3, 7, 10, 13]
    assert find_non_even_or_not_multiples_of_7([2, 6, 14, 28]) == [2, 6]
    assert find_non_even_or_not_multiples_of_7([5, 10, 20, 25]) == [5, 10, 20, 25]
    assert find_non_even_or_not_multiples_of_7([28, 14]) == "No numbers found that are not even or not divisible by 7."


# 177. Тесты для функции `find_not_divisible_by_2_but_divisible_by_5`
def test_find_not_divisible_by_2_but_divisible_by_5():
    assert find_not_divisible_by_2_but_divisible_by_5([5, 10, 15, 20, 25, 30]) == [5, 15, 25]
    assert find_not_divisible_by_2_but_divisible_by_5([2, 4, 6, 8, 10]) == 'No numbers found that are not divisible by 2 but divisible by 5.'
    assert find_not_divisible_by_2_but_divisible_by_5([1, 2, 3, 4, 5]) == [5]
    assert find_not_divisible_by_2_but_divisible_by_5([11, 13, 15, 17]) == [15]
    assert find_not_divisible_by_2_but_divisible_by_5([]) == 'No numbers found that are not divisible by 2 but divisible by 5.'
    assert find_not_divisible_by_2_but_divisible_by_5([21, 25, 29]) == [25]
    assert find_not_divisible_by_2_but_divisible_by_5([30, 35, 40, 45]) == [35, 45]
    assert find_not_divisible_by_2_but_divisible_by_5([7, 14, 21, 28]) == 'No numbers found that are not divisible by 2 but divisible by 5.'
    assert find_not_divisible_by_2_but_divisible_by_5([50, 75, 95]) == [75, 95]


# 178. Тесты для функции `find_multiples_of_3_5_or_7`
def test_find_multiples_of_3_5_or_7():
    assert find_multiples_of_3_5_or_7([3, 5, 7, 9, 10, 14, 15, 21, 25, 30]) == [3, 5, 7, 9, 10, 14, 15, 21, 25, 30]
    assert find_multiples_of_3_5_or_7([1, 2, 4, 8, 11]) == 'No numbers found that are multiples of 3, 5, or 7.'
    assert find_multiples_of_3_5_or_7([3, 6, 12, 18]) == [3, 6, 12, 18]
    assert find_multiples_of_3_5_or_7([5, 10, 20, 25]) == [5, 10, 20, 25]
    assert find_multiples_of_3_5_or_7([7, 14, 28, 35]) == [7, 14, 28, 35]
    assert find_multiples_of_3_5_or_7([]) == 'No numbers found that are multiples of 3, 5, or 7.'
    assert find_multiples_of_3_5_or_7([9, 15, 21, 27, 33]) == [9, 15, 21, 27, 33]
    assert find_multiples_of_3_5_or_7([35, 45, 55, 65]) == [35, 45, 55, 65]
    assert find_multiples_of_3_5_or_7([50, 75, 100]) == [50, 75, 100]


# 179. Тесты для функции `find_even_not_divisible_by_4`
def test_find_even_not_divisible_by_4():
    assert find_even_not_divisible_by_4([2, 3, 4, 6, 8, 10, 12, 14, 16]) == [2, 6, 10, 14]
    assert find_even_not_divisible_by_4([4, 8, 12, 16, 20]) == 'No even numbers found that are not divisible by 4.'
    assert find_even_not_divisible_by_4([1, 3, 5, 7, 9]) == 'No even numbers found that are not divisible by 4.'
    assert find_even_not_divisible_by_4([10, 20, 30, 40]) == [10, 30]
    assert find_even_not_divisible_by_4([]) == 'No even numbers found that are not divisible by 4.'
    assert find_even_not_divisible_by_4([6, 18, 26]) == [6, 18, 26]
    assert find_even_not_divisible_by_4([14, 28, 44, 52]) == [14]
    assert find_even_not_divisible_by_4([32, 36, 48, 60]) == 'No even numbers found that are not divisible by 4.'
    assert find_even_not_divisible_by_4([22, 26, 38]) == [22, 26, 38]


# 180. Тесты для функции `find_multiples_of_3_or_5_not_15`
def test_find_multiples_of_3_or_5_not_15():
    assert find_multiples_of_3_or_5_not_15([3, 5, 9, 10, 12, 18, 20, 30, 33]) == [3, 5, 9, 10, 12, 18, 20, 33]
    assert find_multiples_of_3_or_5_not_15([15, 30, 45, 60]) == 'No numbers found that are multiples of 3 or 5 but not 15.'
    assert find_multiples_of_3_or_5_not_15([1, 2, 4, 7, 11]) == 'No numbers found that are multiples of 3 or 5 but not 15.'
    assert find_multiples_of_3_or_5_not_15([5, 10, 20, 25]) == [5, 10, 20, 25]
    assert find_multiples_of_3_or_5_not_15([3, 6, 9, 12]) == [3, 6, 9, 12]
    assert find_multiples_of_3_or_5_not_15([]) == 'No numbers found that are multiples of 3 or 5 but not 15.'
    assert find_multiples_of_3_or_5_not_15([27, 33, 39]) == [27, 33, 39]
    assert find_multiples_of_3_or_5_not_15([5, 25, 35]) == [5, 25, 35]
    assert find_multiples_of_3_or_5_not_15([9, 21, 27, 39]) == [9, 21, 27, 39]


# 181. Тесты для функции `find_difference_of_two_squares`:
def test_find_difference_of_two_squares():
    assert find_difference_of_two_squares([1, 7, 8]) == [8]
    assert find_difference_of_two_squares([14, 15, 17]) == [15]
    assert find_difference_of_two_squares([2, 3, 5]) == [3, 5]
    assert find_difference_of_two_squares([16, 24, 35]) == [16, 24, 35]
    assert find_difference_of_two_squares([16, 24, 35]) == [16, 24, 35]
    assert find_difference_of_two_squares([]) == "No numbers found that are the difference of two squares."


# 182. Тесты для функции `find_sum_of_two_divisible_by_3`:
def test_find_sum_of_two_divisible_by_3():
    assert find_sum_of_two_divisible_by_3([6, 15, 21]) == [6, 15, 21]
    assert find_sum_of_two_divisible_by_3([5, 7, 11]) == "No numbers found that are the sum of two numbers divisible by 3."
    assert find_sum_of_two_divisible_by_3([9, 18, 30]) == [9, 18, 30]
    assert find_sum_of_two_divisible_by_3([1, 2, 4]) == "No numbers found that are the sum of two numbers divisible by 3."


# 183. Тесты для функции `find_not_even_but_divisible_by_9`:
def test_find_not_even_but_divisible_by_9():
    assert find_not_even_but_divisible_by_9([9, 27, 45]) == [9, 27, 45]
    assert find_not_even_but_divisible_by_9([2, 4, 6]) == "No numbers found that are not even but divisible by 9."
    assert find_not_even_but_divisible_by_9([15, 33, 81]) == [81]
    assert find_not_even_but_divisible_by_9([12, 18, 24]) == "No numbers found that are not even but divisible by 9."


# 184. Тесты для функции `find_odd_and_divisible_by_4`:
def test_find_divisible_by_2():
    assert find_divisible_by_2([4, 16, 28]) ==  'No numbers.'
    assert find_divisible_by_2([1, 3, 5]) == 'No numbers.'
    assert find_divisible_by_2([20, 22, 32]) == [22]
    assert find_divisible_by_2([6, 7, 10]) == [6, 10]


# 185. Тесты для функции `find_divisible_by_2_or_3_not_6`:
def test_find_divisible_by_2_or_3_not_6():
    assert find_divisible_by_2_or_3_not_6([2, 5, 8]) == [2, 8]
    assert find_divisible_by_2_or_3_not_6([4, 10, 14]) == [4, 10, 14]
    assert find_divisible_by_2_or_3_not_6([6, 12, 24]) == "No numbers found that are divisible by 2 or 3 but not 6."
    assert find_divisible_by_2_or_3_not_6([1, 7, 11]) == "No numbers found that are divisible by 2 or 3 but not 6."


# 186. Тесты для функции `find_divisors_of_12_not_even`:
def test_find_divisors_of_12_not_even():
    assert find_divisors_of_12_not_even([1, 3, 6]) == [1, 3]
    assert find_divisors_of_12_not_even([2, 4, 8]) == "No numbers found that are divisors of 12 but not even."
    assert find_divisors_of_12_not_even([5, 7, 9]) == "No numbers found that are divisors of 12 but not even."
    assert find_divisors_of_12_not_even([12, 18, 24]) == "No numbers found that are divisors of 12 but not even."


# 187. Тесты для функции `find_divisors_of_6_not_12`:
def test_find_divisors_of_6_not_12():
    assert find_divisors_of_6_not_12([1, 3, 6]) == [1, 3, 6]
    assert find_divisors_of_6_not_12([2, 4, 8]) == [2]
    assert find_divisors_of_6_not_12([5, 9, 11]) == "No numbers found that are divisors of 6 but not 12."
    assert find_divisors_of_6_not_12([12, 18, 24]) == "No numbers found that are divisors of 6 but not 12."


# 188. Тесты для функции `find_squares_of_even_numbers`:
def test_find_squares_of_even_numbers():
    assert find_squares_of_even_numbers([4, 16, 36]) == [4, 16, 36]
    assert find_squares_of_even_numbers([9, 25, 49]) == "No squares of even numbers found."
    assert find_squares_of_even_numbers([8, 18, 32]) == "No squares of even numbers found."
    assert find_squares_of_even_numbers([64, 100, 144]) == [64, 100, 144]


# 189. Тесты для функции `find_even_not_powers_of_2`:
def test_find_even_not_powers_of_2():
    assert find_even_not_powers_of_2([2, 3, 6, 9]) == [6]
    assert find_even_not_powers_of_2([4, 8, 16, 32]) == "No even numbers found that are not powers of 2."
    assert find_even_not_powers_of_2([18, 20, 22, 24]) == [18, 20, 22, 24]
    assert find_even_not_powers_of_2([1, 2, 4, 8]) == "No even numbers found that are not powers of 2."


# 190. Тесты для функции `find_not_even_and_not_divisible_by_9`:
def test_find_not_even_and_not_divisible_by_9():
    assert find_not_even_and_not_divisible_by_9([1, 3, 7, 11]) == [1, 3, 7, 11]
    assert find_not_even_and_not_divisible_by_9([2, 4, 8, 16]) == "No numbers found that are neither even nor divisible by 9."
    assert find_not_even_and_not_divisible_by_9([5, 15, 25, 35]) == [5, 15, 25, 35]
    assert find_not_even_and_not_divisible_by_9([18, 27, 36, 45]) == "No numbers found that are neither even nor divisible by 9."


# 191. Тесты для функции `find_multiples_of_3_and_5_not_7`:
def test_find_multiples_of_3_and_5_not_7():
    assert find_multiples_of_3_and_5_not_7([15, 30, 45]) == [15, 30, 45]
    assert find_multiples_of_3_and_5_not_7([21, 42, 63]) == "No numbers found that are divisible by 3 and 5 but not 7."
    assert find_multiples_of_3_and_5_not_7([35, 50, 55]) == "No numbers found that are divisible by 3 and 5 but not 7."
    assert find_multiples_of_3_and_5_not_7([75, 90, 105]) == [75, 90]


# 192. Тесты для функции `find_product_of_two_odd_numbers`:
def test_find_product_of_two_odd_numbers():
    assert find_product_of_two_odd_numbers([9, 15, 25]) == [9, 15, 25]
    assert find_product_of_two_odd_numbers([10, 16, 20]) == None
    assert find_product_of_two_odd_numbers([21, 27, 45]) == [21, 27, 45]
    assert find_product_of_two_odd_numbers([14, 18, 22]) == None


# 193. Тесты для функции `find_product_of_two_primes`:
def test_find_product_of_two_primes():
    assert find_product_of_two_primes([6, 10, 14]) == [6, 10, 14]
    assert find_product_of_two_primes([8, 12, 18]) == None
    assert find_product_of_two_primes([15, 21, 35]) == [15, 21, 35]
    assert find_product_of_two_primes([20, 28, 30]) == None
    assert find_product_of_two_primes([]) == None


# 194. Тесты для функции `find_odd_not_power_of_2`:
def test_find_odd_not_power_of_2():
    assert find_odd_not_power_of_2([1, 3, 7]) == [3, 7]
    assert find_odd_not_power_of_2([2, 4, 8]) == None
    assert find_odd_not_power_of_2([9, 11, 13]) == [9, 11, 13]
    assert find_odd_not_power_of_2([16, 32, 64]) == None


# 195. Тесты для функции `find_divisible_by_6_not_9`:
def test_find_divisible_by_6_not_9():
    assert find_divisible_by_6_not_9([6, 12, 24]) == [6, 12, 24]
    assert find_divisible_by_6_not_9([9, 18, 27]) == None
    assert find_divisible_by_6_not_9([30, 36, 42]) == [30, 42]
    assert find_divisible_by_6_not_9([45, 54, 63]) == None


# 196. Тесты для функции `find_divisors_of_24_not_8`:
def test_find_divisors_of_24_not_8():
    assert find_divisors_of_24_not_8([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert find_divisors_of_24_not_8([8, 16, 24]) == None
    assert find_divisors_of_24_not_8([6, 12, 18]) == [6, 12]
    assert find_divisors_of_24_not_8([5, 10, 15]) == None


# 197. Тесты для функции `find_squares_of_odd_numbers`:
def test_find_squares_of_odd_numbers():
    assert find_squares_of_odd_numbers([9, 25, 49]) == [9, 25, 49]
    assert find_squares_of_odd_numbers([16, 36, 64]) == None
    assert find_squares_of_odd_numbers([81, 121, 169]) == [81, 121, 169]
    assert find_squares_of_odd_numbers([100, 144, 196]) == None


# 198. Тесты для функции `find_powers_of_2_not_even`:
def test_find_powers_of_2_not_even():
    assert find_powers_of_2_not_even([1, 3, 7]) == [1]
    assert find_powers_of_2_not_even([8, 16, 32]) == None
    assert find_powers_of_2_not_even([2, 4, 64]) == None
    assert find_powers_of_2_not_even([128, 256, 512]) == None


# 199. Тесты для функции `find_not_multiples_of_3_but_divisible_by_5`:
def test_find_not_multiples_of_3_but_divisible_by_5():
    assert find_not_multiples_of_3_but_divisible_by_5([5, 10, 20]) == [5, 10, 20]
    assert find_not_multiples_of_3_but_divisible_by_5([9, 15, 21]) == None
    assert find_not_multiples_of_3_but_divisible_by_5([25, 35, 50]) == [25, 35, 50]
    assert find_not_multiples_of_3_but_divisible_by_5([6, 12, 18]) == None


# 200. Тесты для функции `find_divisors_of_15_not_3`:
def test_find_divisors_of_15_not_3():
    assert find_divisors_of_15_not_3([1, 5, 15]) == [1, 5]
    assert find_divisors_of_15_not_3([3, 9, 12]) == None
    assert find_divisors_of_15_not_3([2, 4, 6]) == None
    assert find_divisors_of_15_not_3([7, 11, 13]) == None
