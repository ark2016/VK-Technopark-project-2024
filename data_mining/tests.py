import pytest
from functions import *


# 1. Тест функции, проверяющей чётное ли число
def test_is_even():
    assert is_even(4) is True
    assert is_even(0) is True
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(1) is False
    assert is_even(7) is False
    assert is_even(-2) is False
    assert is_even(-3) is False
    assert is_even(-7) is False


# 2. Тест функции, возвращающей факториал числа
def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(-1) is None
    assert factorial(-12) is None
    assert factorial(-5) is None
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(4) == 24


# 3. Тест функции, проверяющей, чего больше, гласных или согласных
def test_count_vowels():
    assert count_vowels("hello") is False
    assert count_vowels("aeioubcd") is True
    assert count_vowels("aeiou") is True
    assert count_vowels("bcd") is False
    assert count_vowels("xylophone") is False
    assert count_vowels("consonant") is False
    assert count_vowels("aaaabbbbcccc") is False


# 4. Тест функции, проверяющей чего больше, чётных или нечётных чисел в списке
def test_count_even_numbers():
    assert count_even_numbers([1, 2, 3, 4, 5]) is False
    assert count_even_numbers([2, 4, 6, 8]) is True
    assert count_even_numbers([1, 3, 5, 7]) is False
    assert count_even_numbers([0, 1, 2, 3, 4]) is True
    assert count_even_numbers([2, 3, 4, 1, 6]) is True
    assert count_even_numbers([2, 1, 2, 1, 2]) is True


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
    assert is_palindrome("radar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("level") is True
    assert is_palindrome("empty") is False
    assert is_palindrome("madam") is True
    assert is_palindrome(" ") is True
    assert is_palindrome("") is False


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
    assert find_max([]) is None


# 9. Тест функции для нахождения минимального числа в списке
def test_find_min():
    assert find_min([1, 2, 3, 4, 5]) == 1
    assert find_min([5, 4, 3, 2, 1]) == 1
    assert find_min([1, 2, 3, 4, 0]) == 0
    assert find_min([0, 0, 0, 0]) == 0
    assert find_min([-1, -2, -3, -4]) == -4
    assert find_min([5, 1, 5, 2, 5]) == 1
    assert find_min([5, 1, 10, 2, 5]) == 1
    assert find_min([]) is None


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
    assert power(0, 0) is None
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
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(17) is True
    assert is_prime(-3) is False


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
    assert lcm(0, 5) is None
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
    assert is_number("123") is True
    assert is_number("12.34") is True
    assert is_number("") is False
    assert is_number("abc") is False
    assert is_number("123abc") is False
    assert is_number("-123") is False


# 29. Тесты для функции `square_non_negative`:
def test_square_non_negative():
    assert square_non_negative(4) == 16
    assert square_non_negative(0) == 0
    assert square_non_negative(-4) is None
    assert square_non_negative(5) == 25
    assert square_non_negative(-10) is None
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
    assert is_leap_year(2020) is True
    assert is_leap_year(2024) is True
    assert is_leap_year(1900) is False
    assert is_leap_year(2000) is True
    assert is_leap_year(2023) is False
    assert is_leap_year(2004) is True


# 35. Тесты для функции `max_min_difference_1`:
def test_max_min_difference_1():
    assert max_min_difference_1([1, 2, 3, 4]) == 3
    assert max_min_difference_1([10, 5]) == 5
    assert max_min_difference_1([1, 1, 1, 1]) == 0
    assert max_min_difference_1([0, 2, 0]) == 2
    assert max_min_difference_1([100]) == 0
    assert max_min_difference_1([]) is None


# 36. Тесты для функции `is_anagram`:
def test_is_anagram():
    assert is_anagram("listen", "silent") is True
    assert is_anagram("hello", "world") is False
    assert is_anagram("evil", "vile") is True
    assert is_anagram("abc", "acb") is True
    assert is_anagram("abc", "abcd") is False
    assert is_anagram("123", "321") is True


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
    assert geometric_mean([]) is None
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
    assert contains_digits("123abc") is True
    assert contains_digits("abcdef") is False
    assert contains_digits("abc1") is True
    assert contains_digits("") is False
    assert contains_digits("123") is True
    assert contains_digits("no digits here!") is False


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
    assert common_element([1, 2, 3], [4, 5, 6]) is None
    assert common_element([], [1, 2, 3]) is None
    assert common_element([1, 2, 3], []) is None
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
    assert trimmed_mean([1, 2]) is None
    assert trimmed_mean([10]) is None
    assert trimmed_mean([]) is None
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
    assert is_valid_email("test@example.com") is True
    assert is_valid_email("test.example.com") is False
    assert is_valid_email("test@.com") is True
    assert is_valid_email("test@com") is False
    assert is_valid_email("test@e.com") is True
    assert is_valid_email("") is False


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
    assert median([]) is None
    assert median([1]) == 1
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 1, 1, 1, 1]) == 1


# 54. Тесты для функции `most_frequent`:
def test_most_frequent():
    assert most_frequent([1, 2, 2, 3, 3, 3]) == 3
    assert most_frequent([4, 4, 4, 4]) == 4
    assert most_frequent([1, 1, 2, 2, 3, 3]) == 1
    assert most_frequent([5]) == 5
    assert most_frequent([]) is None
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
    assert is_positive(5) is True
    assert is_positive(-1) is False
    assert is_positive(0) is False
    assert is_positive(100) is True
    assert is_positive(-50) is False
    assert is_positive(1) is True


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
    assert is_float("3.14") is True
    assert is_float("2.718") is True
    assert is_float("abc") is False
    assert is_float("123") is True
    assert is_float("0.0") is True
    assert is_float("-1.5") is True


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
    assert max_odd_number([2, 4, 6, 8]) is None
    assert max_odd_number([10, 15, 20, 25]) == 25
    assert max_odd_number([-1, -3, -5, -7, -9]) == -1
    assert max_odd_number([]) is None


# 66. Тесты для функции `count_uppercase`:
def test_count_uppercase():
    assert count_uppercase("Hello World!") == 2
    assert count_uppercase("HELLO") == 5
    assert count_uppercase("hello") == 0
    assert count_uppercase("HeLLo WoRLd!") == 6
    assert count_uppercase("123ABC") == 3


# 67. Тесты для функции `is_fibonacci_number`:
def test_is_fibonacci_number():
    assert is_fibonacci_number(0) is False
    assert is_fibonacci_number(1) is True
    assert is_fibonacci_number(2) is True
    assert is_fibonacci_number(3) is True
    assert is_fibonacci_number(4) is False
    assert is_fibonacci_number(5) is True
    assert is_fibonacci_number(-1) is False


# 68. Тесты для функции `is_symmetric`:
def test_is_symmetric():
    assert is_symmetric([1, 2, 3, 2, 1]) is True
    assert is_symmetric([1, 2, 2, 1]) is True
    assert is_symmetric([1, 2, 3, 4, 5]) is False
    assert is_symmetric([]) is True
    assert is_symmetric([1, 2, 3, 4, 3, 2, 1]) is True


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
    assert odd_max_min_difference([2, 4, 6, 8]) is None
    assert odd_max_min_difference([10, 15, 20, 25, 30]) == 10
    assert odd_max_min_difference([-1, -3, -5, -7, -9]) == 8
    assert odd_max_min_difference([]) is None


# 71. Тесты для функции `count_digits`:
def test_count_digits():
    assert count_digits("abc123") == 3
    assert count_digits("1234567890") == 10
    assert count_digits("no digits here") == 0
    assert count_digits("123abc456") == 6
    assert count_digits("") == 0


# 72. Тесты для функции `is_even_length`:
def test_is_even_length():
    assert is_even_length("abcd") is True
    assert is_even_length("abcde") is False
    assert is_even_length("") is True
    assert is_even_length("abcdefgh") is True
    assert is_even_length("abc") is False


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
    assert first_string_with_digit(["abc", "def", "ghi"]) is None
    assert first_string_with_digit(["abc1", "def", "ghi"]) == "abc1"
    assert first_string_with_digit([]) is None


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
    assert max_sublist_sum([]) is None


# 80. Тесты для функции `max_pairwise_product`:
def test_max_pairwise_product():
    assert max_pairwise_product([1, 2, 3, 4, 5]) == 20
    assert max_pairwise_product([5, 5, 5, 5]) == 25
    assert max_pairwise_product([1, 0, 0, 1]) == 1
    assert max_pairwise_product([-1, -2, -3, -4]) == 2
    assert max_pairwise_product([5]) is None


# 81. Тесты для функции `is_palindrome_1`:
def test_is_palindrome_1():
    assert is_palindrome_1("A man, a plan, a canal, Panama") is True
    assert is_palindrome_1("No lemon, no melon") is True
    assert is_palindrome_1("Hello, World!") is False
    assert is_palindrome_1("Madam") is True
    assert is_palindrome_1("") is True
    assert is_palindrome_1("12321") is True
    assert is_palindrome_1("12345") is False
    assert is_palindrome_1("Was it a car or a cat I saw?") is True
    assert is_palindrome_1("Not a palindrome") is False


# 82. Тесты для функции `largest_divisor_less_than`:
def test_largest_divisor_less_than():
    assert largest_divisor_less_than(10) == 5
    assert largest_divisor_less_than(15) == 5
    assert largest_divisor_less_than(1) is None
    assert largest_divisor_less_than(2) is None
    assert largest_divisor_less_than(3) is None
    assert largest_divisor_less_than(25) == 5
    assert largest_divisor_less_than(100) == 50
    assert largest_divisor_less_than(49) == 7
    assert largest_divisor_less_than(97) is None
    assert largest_divisor_less_than(11) is None


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
    assert max_digit_in_string("") is None
    assert max_digit_in_string("a1b2c3") is None
    assert max_digit_in_string("7654321") == 7
    assert max_digit_in_string("0000") == 0
    assert max_digit_in_string("2468") == 8


# 85. Тесты для функции `largest_square`:
def test_largest_square():
    assert largest_square([1, 4, 9, 16, 25]) == 25
    assert largest_square([3, 6, 8, 10]) is None
    assert largest_square([4, 16, 25, 36]) == 36
    assert largest_square([0, 1, 2, 3]) == 1
    assert largest_square([49, 64, 81]) == 81
    assert largest_square([10, 20, 30]) is None
    assert largest_square([5, 12, 13]) is None
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
    assert max_min_difference([]) is None
    assert max_min_difference([1]) == 0
    assert max_min_difference([100, 200, 300, 400]) == 300
    assert max_min_difference([7, 14, 21, 28]) == 21
    assert max_min_difference([9, 18, 27, 36]) == 27
    assert max_min_difference([3, 6, 9, 12]) == 9


# 91. Тесты для функции `first_divisible_by_2_and_5`:
def test_first_divisible_by_2_and_5():
    assert first_divisible_by_2_and_5([1, 3, 5, 10]) == 10
    assert first_divisible_by_2_and_5([20, 15, 25, 30]) == 20
    assert first_divisible_by_2_and_5([1, 2, 3, 4]) is None
    assert first_divisible_by_2_and_5([50, 60, 70]) == 50
    assert first_divisible_by_2_and_5([21, 35, 49]) is None
    assert first_divisible_by_2_and_5([100, 200, 300]) == 100
    assert first_divisible_by_2_and_5([]) is None
    assert first_divisible_by_2_and_5([6, 9, 12, 18]) is None
    assert first_divisible_by_2_and_5([25, 50, 75]) == 50


# 92. Тесты для функции `square_if_number`:
def test_square_if_number():
    assert square_if_number("4") == 16.0
    assert square_if_number("2.5") == 6.25
    assert square_if_number("-3") == 9.0
    assert square_if_number("abc") is None
    assert square_if_number("0") == 0.0
    assert square_if_number("10") == 100.0
    assert square_if_number("3.14") == 9.8596
    assert square_if_number("") is None
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
    assert largest_power_of_two([3, 5, 7]) is None
    assert largest_power_of_two([2, 4, 16, 32]) == 32
    assert largest_power_of_two([]) is None
    assert largest_power_of_two([10, 20, 40]) is None
    assert largest_power_of_two([6, 12, 18]) is None
    assert largest_power_of_two([256, 512, 1024]) == 1024
    assert largest_power_of_two([5, 10, 20, 40]) is None


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
    assert are_anagrams("listen", "silent") is True
    assert are_anagrams("hello", "world") is False
    assert are_anagrams("evil", "vile") is True
    assert are_anagrams("fluster", "restful") is True
    assert are_anagrams("test", "TEST") is False
    assert are_anagrams("a", "a") is True
    assert are_anagrams("abc", "abcd") is False
    assert are_anagrams("", "") is True
    assert are_anagrams("aabb", "abab") is True
    assert are_anagrams("aabb", "abac") is False


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
    assert most_frequent_in_dict(None) is None
    assert most_frequent_in_dict({"a": 1, "b": 2, "c": 2}) == ("b", 2)
    assert most_frequent_in_dict({"x": 10, "y": 15, "z": 10}) == ("y", 15)
    assert most_frequent_in_dict({"apple": 3, "banana": 2, "cherry": 5}) == ("cherry", 5)
    assert most_frequent_in_dict({"a": 1, "b": 2, "c": 2, "d": 3}) == ("d", 3)
    assert most_frequent_in_dict({"a": 0, "b": 0, "c": 0}) == ("a", 0)
    assert most_frequent_in_dict({"a": 4}) == ("a", 4)
    assert most_frequent_in_dict({}) is None
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
    assert min_key_in_dict({}) is None
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
    assert check_and_square("abc") is None
    assert check_and_square("0") == 0
    assert check_and_square("100") == 10000
    assert check_and_square("1.5") == 2.25
    assert check_and_square("-2") == 4
    assert check_and_square("1000") == 1000000
    assert check_and_square("") is None


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
    assert lcm_1(0, 5) is None
    assert lcm_1(6, 8) == 24
    assert lcm_1(9, 12) == 36
    assert lcm_1(3, 7) == 21
    assert lcm_1(10, 0) is None
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
    assert min_max_tuple([]) is None
    assert min_max_tuple([100, 200, 300]) == (100, 300)
    assert min_max_tuple([-100, 0, 100]) == (-100, 100)
    assert min_max_tuple([7, 7, 7]) == (7, 7)


# 129. Тесты для функции `find_common_keys_with_different_values`:
def test_find_common_keys_with_different_values():
    assert find_common_keys_with_different_values({'a': 1, 'b': 2}, {'a': 2, 'b': 2}) == ['a']
    assert find_common_keys_with_different_values({'x': 1, 'y': 2}, {'y': 3, 'z': 4}) == ['y']
    assert find_common_keys_with_different_values({'k': 10, 'l': 20}, {'m': 30, 'n': 40}) == []
    assert find_common_keys_with_different_values({}, {}) == []
    assert find_common_keys_with_different_values({'a': 1, 'b': 1}, {'a': 1, 'b': 2}) == ['b']
    assert find_common_keys_with_different_values({'key1': 100, 'key2': 200}, {'key1': 300, 'key2': 200}) == ['key1']
    assert find_common_keys_with_different_values({'k1': 1, 'k2': 2}, {'k2': 3, 'k3': 4}) == ['k2']
    assert find_common_keys_with_different_values({'a': 1}, {'a': 2}) == ['a']
    assert find_common_keys_with_different_values({'x': 5}, {'y': 5}) == []


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
    assert find_divisible_by_2([4, 16, 28]) == 'No numbers.'
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
    assert find_product_of_two_odd_numbers([10, 16, 20]) is None
    assert find_product_of_two_odd_numbers([21, 27, 45]) == [21, 27, 45]
    assert find_product_of_two_odd_numbers([14, 18, 22]) is None


# 193. Тесты для функции `find_product_of_two_primes`:
def test_find_product_of_two_primes():
    assert find_product_of_two_primes([6, 10, 14]) == [6, 10, 14]
    assert find_product_of_two_primes([8, 12, 18]) is None
    assert find_product_of_two_primes([15, 21, 35]) == [15, 21, 35]
    assert find_product_of_two_primes([20, 28, 30]) is None
    assert find_product_of_two_primes([]) is None


# 194. Тесты для функции `find_odd_not_power_of_2`:
def test_find_odd_not_power_of_2():
    assert find_odd_not_power_of_2([1, 3, 7]) == [3, 7]
    assert find_odd_not_power_of_2([2, 4, 8]) is None
    assert find_odd_not_power_of_2([9, 11, 13]) == [9, 11, 13]
    assert find_odd_not_power_of_2([16, 32, 64]) is None


# 195. Тесты для функции `find_divisible_by_6_not_9`:
def test_find_divisible_by_6_not_9():
    assert find_divisible_by_6_not_9([6, 12, 24]) == [6, 12, 24]
    assert find_divisible_by_6_not_9([9, 18, 27]) is None
    assert find_divisible_by_6_not_9([30, 36, 42]) == [30, 42]
    assert find_divisible_by_6_not_9([45, 54, 63]) is None


# 196. Тесты для функции `find_divisors_of_24_not_8`:
def test_find_divisors_of_24_not_8():
    assert find_divisors_of_24_not_8([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert find_divisors_of_24_not_8([8, 16, 24]) is None
    assert find_divisors_of_24_not_8([6, 12, 18]) == [6, 12]
    assert find_divisors_of_24_not_8([5, 10, 15]) is None


# 197. Тесты для функции `find_squares_of_odd_numbers`:
def test_find_squares_of_odd_numbers():
    assert find_squares_of_odd_numbers([9, 25, 49]) == [9, 25, 49]
    assert find_squares_of_odd_numbers([16, 36, 64]) is None
    assert find_squares_of_odd_numbers([81, 121, 169]) == [81, 121, 169]
    assert find_squares_of_odd_numbers([100, 144, 196]) is None


# 198. Тесты для функции `find_powers_of_2_not_even`:
def test_find_powers_of_2_not_even():
    assert find_powers_of_2_not_even([1, 3, 7]) == [1]
    assert find_powers_of_2_not_even([8, 16, 32]) is None
    assert find_powers_of_2_not_even([2, 4, 64]) is None
    assert find_powers_of_2_not_even([128, 256, 512]) is None


# 199. Тесты для функции `find_not_multiples_of_3_but_divisible_by_5`:
def test_find_not_multiples_of_3_but_divisible_by_5():
    assert find_not_multiples_of_3_but_divisible_by_5([5, 10, 20]) == [5, 10, 20]
    assert find_not_multiples_of_3_but_divisible_by_5([9, 15, 21]) is None
    assert find_not_multiples_of_3_but_divisible_by_5([25, 35, 50]) == [25, 35, 50]
    assert find_not_multiples_of_3_but_divisible_by_5([6, 12, 18]) is None


# 200. Тесты для функции `find_divisors_of_15_not_3`:
def test_find_divisors_of_15_not_3():
    assert find_divisors_of_15_not_3([1, 5, 15]) == [1, 5]
    assert find_divisors_of_15_not_3([3, 9, 12]) is None
    assert find_divisors_of_15_not_3([2, 4, 6]) is None
    assert find_divisors_of_15_not_3([7, 11, 13]) is None


# 201. Тесты для функции `find_powers_of_2_not_multiples_of_4`
def test_find_powers_of_2_not_multiples_of_4():
    assert find_powers_of_2_not_multiples_of_4([1, 2, 3, 4, 8, 16]) == [1, 2]
    assert find_powers_of_2_not_multiples_of_4([32, 64, 128]) is None
    assert find_powers_of_2_not_multiples_of_4([3, 5, 7]) is None
    assert find_powers_of_2_not_multiples_of_4([1024, 256]) is None
    assert find_powers_of_2_not_multiples_of_4([2, 4, 8, 16]) == [2]
    assert find_powers_of_2_not_multiples_of_4([1, 3, 9, 5]) == [1]
    assert find_powers_of_2_not_multiples_of_4([0]) is None


# 202. Тесты для функции `find_odd_not_square`
def test_find_odd_not_square():
    assert find_odd_not_square([1, 2, 3, 5, 7, 9, 10]) == [3, 5, 7]
    assert find_odd_not_square([9, 1, 3, 11]) == [3, 11]
    assert find_odd_not_square([4, 16, 25]) is None
    assert find_odd_not_square([1, 3, 5, 7, 11]) == [3, 5, 7, 11]
    assert find_odd_not_square([25, 49, 81]) is None
    assert find_odd_not_square([4, 16, 64]) is None


# 203. Тесты для функции `find_squares_of_even_not_divisible_by_8`
def test_find_squares_of_even_not_divisible_by_8():
    assert find_squares_of_even_not_divisible_by_8([4, 16, 64, 36, 49]) == [4, 36]
    assert find_squares_of_even_not_divisible_by_8([16, 64, 4, 81]) == [4]
    assert find_squares_of_even_not_divisible_by_8([1, 9, 25]) is None
    assert find_squares_of_even_not_divisible_by_8([100, 144]) == [100]
    assert find_squares_of_even_not_divisible_by_8([64, 256]) is None


# 204. Тесты для функции `find_divisors_of_6_not_2`
def test_find_divisors_of_6_not_2():
    assert find_divisors_of_6_not_2([1, 2, 3, 6]) == [1, 3, 6]
    assert find_divisors_of_6_not_2([6, 9, 12]) == [6]
    assert find_divisors_of_6_not_2([2, 3, 6]) == [3, 6]
    assert find_divisors_of_6_not_2([12, 3]) == [3]
    assert find_divisors_of_6_not_2([8, 10, 6]) == [6]
    assert find_divisors_of_6_not_2([18, 24, 30]) is None


# 205. Тесты для функции `find_divisors_of_48_not_16`
def test_find_divisors_of_48_not_16():
    assert find_divisors_of_48_not_16([1, 2, 3, 4, 6, 8]) == [1, 2, 3, 4, 6, 8]
    assert find_divisors_of_48_not_16([16, 8, 4, 24]) == [8, 4, 24]
    assert find_divisors_of_48_not_16([1, 2, 3, 6, 9]) == [1, 2, 3, 6]
    assert find_divisors_of_48_not_16([16, 48]) is None
    assert find_divisors_of_48_not_16([12, 16, 24]) == [12, 24]


# 206. Тесты для функции `find_divisors_of_20_not_even`
def test_find_divisors_of_20_not_even():
    assert find_divisors_of_20_not_even([1, 2, 5, 10]) == [1, 5]
    assert find_divisors_of_20_not_even([4, 6, 8]) is None
    assert find_divisors_of_20_not_even([5, 15, 30]) == [5]
    assert find_divisors_of_20_not_even([1, 2, 5]) == [1, 5]
    assert find_divisors_of_20_not_even([20, 10]) is None


# 207. Тесты для функции `find_divisible_by_2_not_4_or_8`
def test_find_divisible_by_2_not_4_or_8():
    assert find_divisible_by_2_not_4_or_8([2, 4, 8, 10]) == [2, 10]
    assert find_divisible_by_2_not_4_or_8([2, 6, 10, 14]) == [2, 6, 10, 14]
    assert find_divisible_by_2_not_4_or_8([1, 3, 5]) is None
    assert find_divisible_by_2_not_4_or_8([8, 16, 32]) is None
    assert find_divisible_by_2_not_4_or_8([100]) is None


# 208. Тесты для функции `find_squares_of_odd_not_7`
def test_find_squares_of_odd_not_7():
    assert find_squares_of_odd_not_7([1, 9, 25, 49, 81]) == [1, 9, 25, 81]
    assert find_squares_of_odd_not_7([49, 121, 169]) == [121, 169]
    assert find_squares_of_odd_not_7([64, 256]) is None
    assert find_squares_of_odd_not_7([49, 121, 169]) == [121, 169]
    assert find_squares_of_odd_not_7([81, 25]) == [81, 25]


# 209. Тесты для функции `find_divisible_by_5_not_divisible_by_10`
def test_find_divisible_by_5_not_divisible_by_10():
    assert find_divisible_by_5_not_divisible_by_10([5, 10, 15, 20]) == [5, 15]
    assert find_divisible_by_5_not_divisible_by_10([25, 30, 35]) == [25, 35]
    assert find_divisible_by_5_not_divisible_by_10([1, 3, 6]) is None
    assert find_divisible_by_5_not_divisible_by_10([50, 100]) is None
    assert find_divisible_by_5_not_divisible_by_10([5, 15]) == [5, 15]


# 210. Тесты для функции `find_product_of_two_odd_numbers_not_divisible_by_3`
def test_find_product_of_two_odd_numbers_not_divisible_by_3():
    assert find_product_of_two_odd_numbers_not_divisible_by_3([1, 9, 15, 35, 45]) == [35]
    assert find_product_of_two_odd_numbers_not_divisible_by_3([5, 7, 9, 11, 13]) == [5, 7, 11, 13]
    assert find_product_of_two_odd_numbers_not_divisible_by_3([9, 45, 63]) is None
    assert find_product_of_two_odd_numbers_not_divisible_by_3([21, 35]) == [35]
    assert find_product_of_two_odd_numbers_not_divisible_by_3([15, 33]) is None


# 211. Тесты для функции `find_even_not_divisible_by_3`
def test_find_even_not_divisible_by_3():
    assert find_even_not_divisible_by_3([2, 4, 6, 8, 10, 12]) == [2, 4, 8, 10]
    assert find_even_not_divisible_by_3([6, 12, 18]) is None
    assert find_even_not_divisible_by_3([2, 10, 4]) == [2, 10, 4]
    assert find_even_not_divisible_by_3([2, 4, 8]) == [2, 4, 8]
    assert find_even_not_divisible_by_3([18, 24]) is None


# 212. Тесты для функции `find_difference_of_two_even_numbers`
def test_find_difference_of_two_even_numbers():
    assert find_difference_of_two_even_numbers([4, 6, 8, 10, 12]) == [4, 6, 8, 10, 12]
    assert find_difference_of_two_even_numbers([2, 4, 6, 8]) == [4, 6, 8]
    assert find_difference_of_two_even_numbers([1, 3, 5]) is None
    assert find_difference_of_two_even_numbers([14, 18, 20]) == [14, 18, 20]
    assert find_difference_of_two_even_numbers([2, 6, 10]) == [6, 10]


# 213. Тесты для функции `find_divisors_of_18_not_9`
def test_find_divisors_of_18_not_9():
    assert find_divisors_of_18_not_9([1, 2, 3, 6]) == [1, 2, 3, 6]
    assert find_divisors_of_18_not_9([9, 12, 15]) is None
    assert find_divisors_of_18_not_9([18, 3, 6]) == [3, 6]
    assert find_divisors_of_18_not_9([1, 3, 9]) == [1, 3]
    assert find_divisors_of_18_not_9([6, 18]) == [6]


# 214. Тесты для функции `find_multiples_of_3_and_5_not_15` фиксит
def test_find_multiples_of_3_and_5_not_15():
    assert find_multiples_of_3_and_5_not_15([3, 5, 15, 30, 45]) == [3, 5, 15, 30, 45]
    assert find_multiples_of_3_and_5_not_15([4, 11, 7, 8]) is None
    assert find_multiples_of_3_and_5_not_15([6, 30, 60]) == [6, 30, 60]
    assert find_multiples_of_3_and_5_not_15([3, 15, 30]) == [3, 15, 30]
    assert find_multiples_of_3_and_5_not_15([45, 60]) == [45, 60]


# 215. Тесты для функции `find_product_of_two_primes_not_divisible_by_11`
def test_find_product_of_two_primes_not_divisible_by_11():
    assert find_product_of_two_primes_not_divisible_by_11([6, 15, 35, 55]) == [6, 15, 35]
    assert find_product_of_two_primes_not_divisible_by_11([2, 3, 5, 7]) is None
    assert find_product_of_two_primes_not_divisible_by_11([11, 22]) is None
    assert find_product_of_two_primes_not_divisible_by_11([6, 33]) == [6]
    assert find_product_of_two_primes_not_divisible_by_11([6, 15, 35]) == [6, 15, 35]
    assert find_product_of_two_primes_not_divisible_by_11([6, 625, 342]) == [6]


# 216. Тесты для функции `find_squares_of_even_not_divisible_by_4`
def test_find_squares_of_even_not_divisible_by_4():
    assert find_squares_of_even_not_divisible_by_4([4, 16, 36, 64, 100]) is None
    assert find_squares_of_even_not_divisible_by_4([64, 16, 4]) is None
    assert find_squares_of_even_not_divisible_by_4([25, 49, 121]) == [25, 49, 121]
    assert find_squares_of_even_not_divisible_by_4([144]) is None
    assert find_squares_of_even_not_divisible_by_4([2, 4, 6]) == [6]


# 217. Тесты для функции `find_multiples_of_5_and_6_not_10`
def test_find_multiples_of_5_and_6_not_10():
    assert find_multiples_of_5_and_6_not_10([30, 60, 90, 120]) is None
    assert find_multiples_of_5_and_6_not_10([10, 15, 25]) == [15, 25]
    assert find_multiples_of_5_and_6_not_10([30, 50, 75]) == [75]
    assert find_multiples_of_5_and_6_not_10([5, 6, 15]) == [5, 6, 15]
    assert find_multiples_of_5_and_6_not_10([90]) is None


# 218. Тесты для функции `find_difference_of_two_even_not_divisible_by_4`
def test_find_difference_of_two_even_not_divisible_by_4():
    assert find_difference_of_two_even_not_divisible_by_4([4, 8, 12, 16]) is None
    assert find_difference_of_two_even_not_divisible_by_4([10, 14, 18]) == [10, 14, 18]
    assert find_difference_of_two_even_not_divisible_by_4([2, 4, 6]) == [6]
    assert find_difference_of_two_even_not_divisible_by_4([24, 28, 32]) is None
    assert find_difference_of_two_even_not_divisible_by_4([10, 20]) == [10]


# 219. Тесты для функции `find_product_of_two_primes_not_7`
def test_find_product_of_two_primes_not_7():
    assert find_product_of_two_primes_not_7([6, 10, 14, 15]) == [6, 10, 15]
    assert find_product_of_two_primes_not_7([5, 13, 17]) is None
    assert find_product_of_two_primes_not_7([7, 11]) is None
    assert find_product_of_two_primes_not_7([6, 15, 21]) == [6, 15]
    assert find_product_of_two_primes_not_7([3, 5, 15]) == [15]
    assert find_product_of_two_primes_not_7([3, 270, 150]) is None


# 220. Тесты для функции `find_difference_of_two_odd`
def test_find_difference_of_two_odd():
    assert find_difference_of_two_odd([5, 7, 9, 11]) == [5, 7, 9, 11]
    assert find_difference_of_two_odd([1, 3, 5, 7]) == [3, 5, 7]
    assert find_difference_of_two_odd([3, 9, 15]) == [3, 9, 15]
    assert find_difference_of_two_odd([5, 15, 25]) == [5, 15, 25]
    assert find_difference_of_two_odd([1, 1, 1]) is None
    assert find_difference_of_two_odd([]) is None


# 221. Тесты для функции `find_product_of_two_odd_not_5`:
def test_find_product_of_two_odd_not_5():
    assert find_product_of_two_odd_not_5([15, 21, 35, 45]) == [21]
    assert find_product_of_two_odd_not_5([10, 5, 7, 9]) == [7, 9]
    assert find_product_of_two_odd_not_5([27, 49, 77, 99]) == [27, 49, 77, 99]
    assert find_product_of_two_odd_not_5([]) is None
    assert find_product_of_two_odd_not_5([9, 25, 49, 63]) == [9, 49, 63]
    assert find_product_of_two_odd_not_5([1, 1, 1, 1, 1, 1]) is None


# 222. Тесты для функции `find_divisors_of_36_not_9`:
def test_find_divisors_of_36_not_9():
    assert find_divisors_of_36_not_9([1, 2, 3, 4, 6, 9, 12, 18]) == [1, 2, 3, 4, 6, 12]
    assert find_divisors_of_36_not_9([5, 7, 10]) is None
    assert find_divisors_of_36_not_9([36, 6, 4]) == [6, 4]
    assert find_divisors_of_36_not_9([18, 3, 9]) == [3]
    assert find_divisors_of_36_not_9([8, 2, 6]) == [2, 6]
    assert find_divisors_of_36_not_9([1, 36, 12, 2]) == [1, 12, 2]


# 223. Тесты для функции `find_odd_and_divisible_by_5_not_10`:
def test_find_odd_and_divisible_by_5_not_10():
    assert find_odd_and_divisible_by_5_not_10([5, 15, 25, 35, 10]) == [5, 15, 25, 35]
    assert find_odd_and_divisible_by_5_not_10([5, 10, 20]) == [5]
    assert find_odd_and_divisible_by_5_not_10([35, 55, 75]) == [35, 55, 75]
    assert find_odd_and_divisible_by_5_not_10([10, 30, 50]) is None
    assert find_odd_and_divisible_by_5_not_10([25, 15, 5]) == [25, 15, 5]
    assert find_odd_and_divisible_by_5_not_10([35, 45, 100, 90]) == [35, 45]


# 224. Тесты для функции `find_divisible_by_6`:
def test_find_divisible_by_6():
    assert find_divisible_by_6([6, 12, 18, 24, 36]) == [6, 12, 18, 24, 36]
    assert find_divisible_by_6([3, 6, 9, 12]) == [6, 12]
    assert find_divisible_by_6([36, 42, 48]) == [36, 42, 48]
    assert find_divisible_by_6([54, 60, 72]) == [54, 60, 72]
    assert find_divisible_by_6([5, 10, 79]) is None
    assert find_divisible_by_6([9, 18, 72]) == [18, 72]


# 225. Тесты для функции `find_divisors_of_30_not_5`:
def test_find_divisors_of_30_not_5():
    assert find_divisors_of_30_not_5([1, 2, 3, 5, 6, 10, 15, 30]) == [1, 2, 3, 6]
    assert find_divisors_of_30_not_5([7, 11, 13]) is None
    assert find_divisors_of_30_not_5([30, 12, 6]) == [6]
    assert find_divisors_of_30_not_5([9, 12, 4]) is None
    assert find_divisors_of_30_not_5([15, 3]) == [3]
    assert find_divisors_of_30_not_5([10, 12, 18]) is None


# 226. Тесты для функции `find_product_of_two_primes_not_6`:
def test_find_product_of_two_primes_not_6():
    assert find_product_of_two_primes_not_6([6, 10, 15, 77]) == [10, 15, 77]
    assert find_product_of_two_primes_not_6([2, 3, 5, 7]) is None
    assert find_product_of_two_primes_not_6([21, 35, 77]) == [21, 35, 77]
    assert find_product_of_two_primes_not_6([199, 235, 569]) == [235]
    assert find_product_of_two_primes_not_6([11, 13, 17]) is None
    assert find_product_of_two_primes_not_6([8, 9, 14, 21]) == [9, 14, 21]


# 227. Тесты для функции `find_even_and_divisible_by_7_not_14`:
def test_find_even_and_divisible_by_7():
    assert find_even_and_divisible_by_7([14, 28, 70]) == [14, 28, 70]
    assert find_even_and_divisible_by_7([7, 35, 49]) is None
    assert find_even_and_divisible_by_7([21, 49, 21]) is None
    assert find_even_and_divisible_by_7([12, 24, 42]) == [42]
    assert find_even_and_divisible_by_7([]) is None
    assert find_even_and_divisible_by_7([2, 4, 12, 16]) is None


# 228. Тесты для функции `find_difference_of_two_odd_not_5`:
def test_find_difference_of_two_odd_not_5():
    assert find_difference_of_two_odd_not_5([9, 15, 25, 35]) == [9]
    assert find_difference_of_two_odd_not_5([3, 5, 7, 11]) == [3, 7, 11]
    assert find_difference_of_two_odd_not_5([10, 5, 7, 9]) == [7, 9]
    assert find_difference_of_two_odd_not_5([21, 35, 49]) == [21, 49]
    assert find_difference_of_two_odd_not_5([5, 25]) is None
    assert find_difference_of_two_odd_not_5([15, 25, 35]) is None


# 229. Тесты для функции `find_squares_of_odd_not_divisible_by_5`:
def test_find_squares_of_odd_not_divisible_by_5():
    assert find_squares_of_odd_not_divisible_by_5([1, 9, 25, 49, 81]) == [1, 9, 49, 81]
    assert find_squares_of_odd_not_divisible_by_5([4, 16, 64]) is None
    assert find_squares_of_odd_not_divisible_by_5([25, 49, 121]) == [49, 121]
    assert find_squares_of_odd_not_divisible_by_5([49, 81]) == [49, 81]
    assert find_squares_of_odd_not_divisible_by_5([100, 121, 169]) == [121, 169]
    assert find_squares_of_odd_not_divisible_by_5([64, 169, 81]) == [169, 81]


# 230. Тесты для функции `find_product_of_two_primes_not_divisible_by_3`:
def test_find_product_of_two_primes_not_divisible_by_3():
    assert find_product_of_two_primes_not_divisible_by_3([6, 10, 15, 77]) == [10, 77]
    assert find_product_of_two_primes_not_divisible_by_3([2, 3, 5, 7, 11]) is None
    assert find_product_of_two_primes_not_divisible_by_3([30, 42, 49, 35]) == [49, 35]
    assert find_product_of_two_primes_not_divisible_by_3([10, 14, 26, 77]) == [10, 14, 26, 77]
    assert find_product_of_two_primes_not_divisible_by_3([2, 5, 7, 11, 13]) is None
    assert find_product_of_two_primes_not_divisible_by_3([9, 15, 21]) is None
    assert find_product_of_two_primes_not_divisible_by_3([657, 1234, 6754]) == [1234]


# 231. Тесты для функции `find_divisors_of_40_not_even`:
def test_find_divisors_of_40_not_even():
    assert find_divisors_of_40_not_even([1, 2, 4, 5, 8, 10, 20, 40]) == [1, 5]
    assert find_divisors_of_40_not_even([1, 3, 5, 7, 9, 11]) == [1, 5]
    assert find_divisors_of_40_not_even([5, 3, 1]) == [5, 1]
    assert find_divisors_of_40_not_even([2, 4, 8]) is None
    assert find_divisors_of_40_not_even([5, 1, 20]) == [5, 1]
    assert find_divisors_of_40_not_even([15, 7, 9]) is None


# 232. Тесты для функции `find_difference_of_two_even_not_5`:
def test_find_difference_of_two_even_not_5():
    assert find_difference_of_two_even_not_5([6, 10, 14, 20, 4, 8]) == [6, 14, 4, 8]
    assert find_difference_of_two_even_not_5([2, 4, 6, 8]) == [4, 6, 8]
    assert find_difference_of_two_even_not_5([10, 12, 16, 18]) == [12, 16, 18]
    assert find_difference_of_two_even_not_5([30, 50, 60]) is None
    assert find_difference_of_two_even_not_5([40, 60, 80]) is None
    assert find_difference_of_two_even_not_5([5, 15, 25]) is None


# 233. Тесты для функции `find_product_of_two_odd_not_divisible_by_7`:
def test_find_product_of_two_odd_not_divisible_by_7():
    assert find_product_of_two_odd_not_divisible_by_7([9, 15, 21, 35]) == [9, 15]
    assert find_product_of_two_odd_not_divisible_by_7([7, 11, 13, 25]) == [11, 13, 25]
    assert find_product_of_two_odd_not_divisible_by_7([3, 5, 9, 15]) == [3, 5, 9, 15]
    assert find_product_of_two_odd_not_divisible_by_7([49, 77, 35]) is None
    assert find_product_of_two_odd_not_divisible_by_7([21, 25, 45, 49]) == [25, 45]
    assert find_product_of_two_odd_not_divisible_by_7([5, 15, 30, 45]) == [5, 15, 45]


# 234. Тесты для функции `find_divisible_by_4`:
def test_find_divisible_by_4():
    assert find_divisible_by_4([4, 8, 12, 16, 20, 24]) == [4, 12, 20]
    assert find_divisible_by_4([2, 4, 8, 10, 20]) == [4, 20]
    assert find_divisible_by_4([64, 8, 32]) is None
    assert find_divisible_by_4([6, 10, 14, 22]) is None
    assert find_divisible_by_4([5, 7, 9, 11, 13]) is None
    assert find_divisible_by_4([4, 12]) == [4, 12]


# 235. Тесты для функции `find_squares_of_odd_not_9`:
def test_find_squares_of_odd_not_9():
    assert find_squares_of_odd_not_9([1, 9, 25, 49, 81]) == [1, 25, 49]
    assert find_squares_of_odd_not_9([1, 9, 25]) == [1, 25]
    assert find_squares_of_odd_not_9([9, 81, 729]) is None
    assert find_squares_of_odd_not_9([1, 4, 16]) == [1]
    assert find_squares_of_odd_not_9([1, 25, 49, 81]) == [1, 25, 49]
    assert find_squares_of_odd_not_9([49, 121, 225]) == [49, 121]


# 236. Тесты для функции `find_difference_of_two_primes`:
def test_find_difference_of_two_primes():
    assert find_difference_of_two_primes([10, 15, 20, 23]) == [10, 15, 20]
    assert find_difference_of_two_primes([3, 5, 7, 9]) == [5, 7, 9]
    assert find_difference_of_two_primes([10, 5, 8, 13]) == [10, 5, 8, 13]
    assert find_difference_of_two_primes([2, 7, 11]) == [7]
    assert find_difference_of_two_primes([11, 1030, 1024, 13]) == [1030, 1024, 13]
    assert find_difference_of_two_primes([5, 10, 12]) == [5, 10, 12]
    assert find_difference_of_two_primes([2, 77, 11]) is None


# 237. Тесты для функции `find_product_of_two_primes_not_5`:
def test_find_product_of_two_primes_not_5():
    assert find_product_of_two_primes_not_5([6, 10, 15, 35]) == [6]
    assert find_product_of_two_primes_not_5([15, 25, 35, 77]) == [77]
    assert find_product_of_two_primes_not_5([2, 3, 7, 11]) is None
    assert find_product_of_two_primes_not_5([5, 7, 3]) is None
    assert find_product_of_two_primes_not_5([5, 7, 11, 9]) == [9]
    assert find_product_of_two_primes_not_5([9, 25, 49]) == [9, 49]
    assert find_product_of_two_primes_not_5([4, 6, 8, 9, 14, 21]) == [4, 6, 9, 14, 21]


# 238. Тесты для функции `find_divisible_by_2_and_5_not_10`:
def test_find_divisible_by_2_and_5_not_10():
    assert find_divisible_by_2_and_5_not_10([10, 20, 30, 40]) is None
    assert find_divisible_by_2_and_5_not_10([5, 15, 25]) == [5, 15, 25]
    assert find_divisible_by_2_and_5_not_10([10, 25]) == [25]
    assert find_divisible_by_2_and_5_not_10([5, 50, 75]) == [5, 75]
    assert find_divisible_by_2_and_5_not_10([10, 15, 30]) == [15]
    assert find_divisible_by_2_and_5_not_10([5, 20]) == [5]


# 239. Тесты для функции `find_difference_of_two_even_not_divisible_by_6`:
def test_find_difference_of_two_even_not_divisible_by_6():
    assert find_difference_of_two_even_not_divisible_by_6([6, 12, 20, 30, 40]) == [20, 40]
    assert find_difference_of_two_even_not_divisible_by_6([4, 8, 10]) == [4, 8, 10]
    assert find_difference_of_two_even_not_divisible_by_6([8, 14, 20, 40]) == [8, 14, 20, 40]
    assert find_difference_of_two_even_not_divisible_by_6([6, 8, 10]) == [8, 10]
    assert find_difference_of_two_even_not_divisible_by_6([2, 4, 8]) == [4, 8]
    assert find_difference_of_two_even_not_divisible_by_6([6, 30]) is None


# 240. Тесты для функции `find_product_of_two_odd_not_divisible_by_4`:
def test_find_product_of_two_odd_not_divisible_by_4():
    assert find_product_of_two_odd_not_divisible_by_4([9, 15, 35, 45]) == [9]
    assert find_product_of_two_odd_not_divisible_by_4([3, 7, 11, 13, 17]) == [3, 7, 11, 13, 17]
    assert find_product_of_two_odd_not_divisible_by_4([5, 32, 8]) is None
    assert find_product_of_two_odd_not_divisible_by_4([5, 64, 20]) is None
    assert find_product_of_two_odd_not_divisible_by_4([7, 9, 15]) == [7, 9]
    assert find_product_of_two_odd_not_divisible_by_4([9, 15, 25, 35]) == [9]


# 241. Тесты для функции `find_multiples_of_6_not_12`:
def test_find_multiples_of_6_not_12():
    assert find_multiples_of_6_not_12([6, 12, 18, 24, 30]) == [6, 18, 30]
    assert find_multiples_of_6_not_12([1, 2, 3, 4, 5]) is None
    assert find_multiples_of_6_not_12([12, 24, 36]) is None
    assert find_multiples_of_6_not_12([-6, -12, -18, -30]) == [-6, -18, -30]
    assert find_multiples_of_6_not_12([]) is None
    assert find_multiples_of_6_not_12([6, 36, 60]) == [6]
    assert find_multiples_of_6_not_12([60]) is None
    assert find_multiples_of_6_not_12([60, 70, 80]) is None
    assert find_multiples_of_6_not_12([13, 18, 22]) == [18]


# 242. Тесты для функции `find_even_not_divisible_by_5`:
def test_find_even_not_divisible_by_5():
    assert find_even_not_divisible_by_5([10, 20, 30, 40, 50]) is None
    assert find_even_not_divisible_by_5([1, 2, 3, 4, 5]) == [2, 4]
    assert find_even_not_divisible_by_5([6, 12, 18, 24, 30]) == [6, 12, 18, 24]
    assert find_even_not_divisible_by_5([-10, -20, -30, -40, -50]) is None
    assert find_even_not_divisible_by_5([-1, -2, -3, -4, -5]) == [-2, -4]
    assert find_even_not_divisible_by_5([15, 25, 35, 45]) is None
    assert find_even_not_divisible_by_5([0, 1, 2, 3, 4, 5]) == [2, 4]
    assert find_even_not_divisible_by_5([6, 7, 8, 9, 10]) == [6, 8]
    assert find_even_not_divisible_by_5([15, 20, 25, 30, 35]) is None


# 243. Тесты для функции `find_squares_of_odd_not_divisible_by_3`:
def test_find_squares_of_odd_not_divisible_by_3():
    assert find_squares_of_odd_not_divisible_by_3([1, 4, 9, 16, 25, 36, 49]) == [1, 25, 49]
    assert find_squares_of_odd_not_divisible_by_3([2, 3, 5, 7, 11]) is None
    assert find_squares_of_odd_not_divisible_by_3([1, 25, 49, 81]) == [1, 25, 49]
    assert find_squares_of_odd_not_divisible_by_3([1, 4, 9, 16, 25, 36, 49]) == [1, 25, 49]
    assert find_squares_of_odd_not_divisible_by_3([1, 3, 5, 7, 9, 11]) == [1]
    assert find_squares_of_odd_not_divisible_by_3([25, 49, 81, 100]) == [25, 49]
    assert find_squares_of_odd_not_divisible_by_3([36, 45, 54, 63, 72]) is None
    assert find_squares_of_odd_not_divisible_by_3([10, 20, 30, 40, 50]) is None
    assert find_squares_of_odd_not_divisible_by_3([100, 121, 144, 169]) == [121, 169]


# 244. Тесты для функции `find_divisors_of_50_not_prime`:
def test_find_divisors_of_50_not_prime():
    assert find_divisors_of_50_not_prime([1, 2, 5, 10, 25, 50]) == [1, 10, 25, 50]
    assert find_divisors_of_50_not_prime([2, 3, 5, 7, 11, 13]) is None
    assert find_divisors_of_50_not_prime([4, 6, 8, 10, 12]) == [10]
    assert find_divisors_of_50_not_prime([-1, -2, -5, -10, -25, -50]) == [-1, -2, -5, -10, -25, -50]
    assert find_divisors_of_50_not_prime([1, 2, 3, 4, 5]) == [1]
    assert find_divisors_of_50_not_prime([50, 100, 150, 200]) == [50]
    assert find_divisors_of_50_not_prime([7, 8, 9, 10, 11]) == [10]
    assert find_divisors_of_50_not_prime([13, 17, 19, 23]) is None
    assert find_divisors_of_50_not_prime([25, 30, 35, 40]) == [25]


# 245. Тесты для функции `find_divisible_by_3_and_4_not_7`:
def test_find_divisible_by_3_and_4_not_7():
    assert find_divisible_by_3_and_4_not_7([12, 24, 36, 48, 60]) == [12, 24, 36, 48, 60]
    assert find_divisible_by_3_and_4_not_7([1, 2, 3, 4, 5]) is None
    assert find_divisible_by_3_and_4_not_7([21, 28, 35, 42, 49]) is None
    assert find_divisible_by_3_and_4_not_7([-12, -24, -36, -48, -60]) == [-12, -24, -36, -48, -60]
    assert find_divisible_by_3_and_4_not_7([6, 18, 30, 42, 54]) is None
    assert find_divisible_by_3_and_4_not_7([84, 96, 108, 120]) == [96, 108, 120]
    assert find_divisible_by_3_and_4_not_7([36, 48, 54, 72]) == [36, 48, 72]
    assert find_divisible_by_3_and_4_not_7([27, 33, 39, 45]) is None
    assert find_divisible_by_3_and_4_not_7([12, 24, 36]) == [12, 24, 36]


# 246. Тесты для функции `find_intersection_of_sets`:
def test_find_intersection_of_sets():
    assert find_intersection_of_sets([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    assert find_intersection_of_sets([1, 2, 3], [4, 5, 6]) is None
    assert find_intersection_of_sets([7, 8, 9], [7, 8, 9]) == [7, 8, 9]
    assert find_intersection_of_sets([], [1, 2, 3]) is None
    assert find_intersection_of_sets([1, 2, 3], []) is None
    assert find_intersection_of_sets([0, 1, 2], [2, 3, 4]) == [2]
    assert find_intersection_of_sets([-1, -2, -3], [-3, -4, -5]) == [-3]
    assert find_intersection_of_sets([10, 11, 12], [12, 13, 14]) == [12]
    assert find_intersection_of_sets([15, 16, 17], [18, 19, 20]) is None


# 247. Тесты для функции `find_symmetric_difference`:
def test_find_symmetric_difference():
    assert find_symmetric_difference([1, 2, 3], [3, 4, 5]) == [1, 2, 4, 5]
    assert find_symmetric_difference([7, 8, 9], [7, 8, 9]) is None
    assert find_symmetric_difference([10, 20, 30], [30, 40, 50]) == [10, 20, 40, 50]
    assert find_symmetric_difference([], [1, 2, 3]) == [1, 2, 3]
    assert find_symmetric_difference([1, 2, 3], []) == [1, 2, 3]
    assert find_symmetric_difference([-1, -2, -3], [-3, -4, -5]) == [-5, -4, -2, -1]
    assert find_symmetric_difference([10, 11, 12], [12, 13, 14]) == [10, 11, 13, 14]
    assert find_symmetric_difference([15, 16, 17], [18, 19, 20]) == [15, 16, 17, 18, 19, 20]
    assert find_symmetric_difference([1, 3, 5, 7], [2, 4, 6, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]


# 248. Тесты для функции `find_keys_in_dicts`:
def test_find_keys_in_dicts():
    assert find_keys_in_dicts({1: 2, 3: 4, 5: 6}, {2: 'a', 4: 'b', 6: 'c'}) == [1, 3, 5]
    assert find_keys_in_dicts({1: 2, 3: 4, 5: 6}, {7: 'a', 8: 'b', 9: 'c'}) is None
    assert find_keys_in_dicts({}, {2: 'a', 4: 'b', 6: 'c'}) is None
    assert find_keys_in_dicts({1: 2, 3: 4, 5: 6}, {}) is None
    assert find_keys_in_dicts({1: 2, 3: 4, 5: 6}, {4: 'b'}) == [3]
    assert find_keys_in_dicts({1: 2, 3: 4, 5: 6}, {6: 'c'}) == [5]
    assert find_keys_in_dicts({1: 2, 3: 4}, {4: 'b', 2: 'a'}) == [1, 3]
    assert find_keys_in_dicts({7: 8, 9: 10}, {8: 'd', 10: 'e'}) == [7, 9]
    assert find_keys_in_dicts({11: 12, 13: 14}, {14: 'g', 12: 'f'}) == [11, 13]


# 249. Тесты для функции `find_in_list_not_in_tuple`:
def test_find_in_list_not_in_tuple():
    assert find_in_list_not_in_tuple([1, 2, 3, 4, 5], (4, 5, 6, 7)) == [1, 2, 3]
    assert find_in_list_not_in_tuple([1, 2, 3], (1, 2, 3)) is None
    assert find_in_list_not_in_tuple([4, 5, 6], (1, 2, 3)) == [4, 5, 6]
    assert find_in_list_not_in_tuple([], (1, 2, 3)) is None
    assert find_in_list_not_in_tuple([1, 2, 3], ()) == [1, 2, 3]
    assert find_in_list_not_in_tuple([1, 3, 5], (2, 4, 6)) == [1, 3, 5]
    assert find_in_list_not_in_tuple([-1, -2, -3], (-3, -4, -5)) == [-1, -2]
    assert find_in_list_not_in_tuple([10, 20, 30], (20, 30, 40)) == [10]
    assert find_in_list_not_in_tuple([15, 25, 35], (10, 20, 30)) == [15, 25, 35]


# 250. Тесты для функции `find_pairs_with_first_greater`:
def test_find_pairs_with_first_greater():
    assert find_pairs_with_first_greater([1, 2, 3]) == [(2, 1), (3, 1), (3, 2)]
    assert find_pairs_with_first_greater([3, 1, 2]) == [(3, 1), (3, 2), (2, 1)]
    assert find_pairs_with_first_greater([1, 1, 1]) is None
    assert find_pairs_with_first_greater([]) is None
    assert find_pairs_with_first_greater([5, 5, 5]) is None
    assert find_pairs_with_first_greater([4, 5, 6]) == [(5, 4), (6, 4), (6, 5)]
    assert find_pairs_with_first_greater([10, 20, 30]) == [(20, 10), (30, 10), (30, 20)]
    assert find_pairs_with_first_greater([-1, 0, 1]) == [(0, -1), (1, -1), (1, 0)]
    assert find_pairs_with_first_greater([10, 20, 30, 40]) == [(20, 10), (30, 10), (30, 20), (40, 10), (40, 20), (40, 30)]


# 251. Тесты для функции `find_tuples_without_negatives`:
def test_find_tuples_without_negatives():
    assert find_tuples_without_negatives([(1, 2), (-1, 2), (3, 4)]) == [(1, 2), (3, 4)]
    assert find_tuples_without_negatives([(1, 2, -3), (-4, 5, 6), (7, 8, 9)]) == [(7, 8, 9)]
    assert find_tuples_without_negatives([(0, 1, 2)]) == [(0, 1, 2)]
    assert find_tuples_without_negatives([(-1, -2, -3)]) is None
    assert find_tuples_without_negatives([]) is None
    assert find_tuples_without_negatives([(1, 1), (0, 0), (-1, -1)]) == [(1, 1), (0, 0)]
    assert find_tuples_without_negatives([(1,), (-1,)]) == [(1,)]
    assert find_tuples_without_negatives([(0, 0, 0)]) == [(0, 0, 0)]
    assert find_tuples_without_negatives([(-5, -4, -3)]) is None


# 252. Тесты для функции `find_keys_with_odd_values`:
def test_find_keys_with_odd_values():
    assert find_keys_with_odd_values({1: 2, 3: 4, 5: 6}) is None
    assert find_keys_with_odd_values({1: 1, 3: 3, 5: 5}) == [1, 3, 5]
    assert find_keys_with_odd_values({1: 2, 3: 3, 5: 6}) == [3]
    assert find_keys_with_odd_values({}) is None
    assert find_keys_with_odd_values({1: 2, 2: 4, 3: 6}) is None
    assert find_keys_with_odd_values({1: 3, 2: 5, 3: 7}) == [1, 2, 3]
    assert find_keys_with_odd_values({4: 5, 6: 7}) == [4, 6]
    assert find_keys_with_odd_values({8: 9, 10: 11}) == [8, 10]
    assert find_keys_with_odd_values({12: 13, 14: 15}) == [12, 14]


# 253. Тесты для функции `find_product_of_two_not_divisible_by_2`:
def test_find_product_of_two_not_divisible_by_2():
    assert find_product_of_two_not_divisible_by_2([1, 2, 3, 4, 5]) == [3, 5, 15]
    assert find_product_of_two_not_divisible_by_2([2, 4, 6]) is None
    assert find_product_of_two_not_divisible_by_2([1, 3, 5, 7]) == [3, 5, 7, 15, 21, 35]
    assert find_product_of_two_not_divisible_by_2([0, 1, 2, 3]) == [3]
    assert find_product_of_two_not_divisible_by_2([-1, -3, -5]) == [3, 5, 15]
    assert find_product_of_two_not_divisible_by_2([-2, -4, -6]) is None
    assert find_product_of_two_not_divisible_by_2([1, -1, 3, -3]) == [-1, 3, -3, -3, 3, -9]
    assert find_product_of_two_not_divisible_by_2([1]) is None
    assert find_product_of_two_not_divisible_by_2([2]) is None


# 254. Тесты для функции `find_in_set_not_in_list`:
def test_find_in_set_not_in_list():
    assert find_in_set_not_in_list({1, 2, 3}, [2, 3, 4]) == [1]
    assert find_in_set_not_in_list({1, 2, 3}, [1, 2, 3]) is None
    assert find_in_set_not_in_list({4, 5, 6}, [1, 2, 3]) == [4, 5, 6]
    assert find_in_set_not_in_list({0, 1, 2}, [2, 3, 4]) == [0, 1]
    assert find_in_set_not_in_list({-1, -2, -3}, [-3, -4, -5]) == [-2, -1]
    assert find_in_set_not_in_list({10, 20, 30}, [20, 30, 40]) == [10]
    assert find_in_set_not_in_list({15, 25, 35}, [10, 20, 30]) == [15, 25, 35]
    assert find_in_set_not_in_list({1, 2, 3}, []) == [1, 2, 3]
    assert find_in_set_not_in_list(set(), [1, 2, 3]) is None


# 255. Тесты для функции `find_keys_not_divisible_by_3`:
def test_find_keys_not_divisible_by_3():
    assert find_keys_not_divisible_by_3({1: 'a', 3: 'b', 6: 'c'}) == [1]
    assert find_keys_not_divisible_by_3({3: 'a', 6: 'b', 9: 'c'}) is None
    assert find_keys_not_divisible_by_3({1: 'a', 2: 'b', 4: 'c'}) == [1, 2, 4]
    assert find_keys_not_divisible_by_3({0: 'a', 3: 'b', 6: 'c'}) is None
    assert find_keys_not_divisible_by_3({7: 'a', 8: 'b', 10: 'c'}) == [7, 8, 10]
    assert find_keys_not_divisible_by_3({5: 'a', 7: 'b', 11: 'c'}) == [5, 7, 11]
    assert find_keys_not_divisible_by_3({12: 'a', 15: 'b', 18: 'c'}) is None
    assert find_keys_not_divisible_by_3({2: 'a', 4: 'b', 5: 'c'}) == [2, 4, 5]
    assert find_keys_not_divisible_by_3({11: 'a', 14: 'b', 17: 'c'}) == [11, 14, 17]


# 256. Тесты для функции `find_numbers_with_sum_divisible_by_4`:
def test_find_numbers_with_sum_divisible_by_4():
    assert find_numbers_with_sum_divisible_by_4([1, 2, 3], [4, 5, 6]) == [(2, 6), (3, 5)]
    assert find_numbers_with_sum_divisible_by_4([1, 2, 3], [7, 8, 9]) == [(1, 7), (3, 9)]
    assert find_numbers_with_sum_divisible_by_4([4, 5, 6], [1, 2, 3]) == [(5, 3), (6, 2)]
    assert find_numbers_with_sum_divisible_by_4([0, 1, 2], [2, 3, 4]) == [(0, 4), (1, 3), (2, 2)]
    assert find_numbers_with_sum_divisible_by_4([5, 6, 7], [3, 4, 5]) == [(5, 3), (7, 5)]
    assert find_numbers_with_sum_divisible_by_4([], []) is None
    assert find_numbers_with_sum_divisible_by_4([], [1, 2, 3]) is None
    assert find_numbers_with_sum_divisible_by_4([112, 3, 45], []) is None


# 257. Тесты для функции `find_unique_in_one_list`:
def test_find_unique_in_one_list():
    assert find_unique_in_one_list([1, 2, 3], [3, 4, 5]) == [1, 2, 4, 5]
    assert find_unique_in_one_list([7, 8, 9], [7, 8, 9]) is None
    assert find_unique_in_one_list([10, 20, 30], [30, 40, 50]) == [40, 10, 50, 20]
    assert find_unique_in_one_list([], [1, 2, 3]) == [1, 2, 3]
    assert find_unique_in_one_list([1, 2, 3], []) == [1, 2, 3]
    assert find_unique_in_one_list([-1, -2, -3], [-3, -4, -5]) == [-2, -5, -4, -1]
    assert find_unique_in_one_list([10, 11, 12], [12, 13, 14]) == [10, 11, 13, 14]
    assert find_unique_in_one_list([15, 16, 17], [18, 19, 20]) == [15, 16, 17, 18, 19, 20]


# 258. Тесты для функции `find_pairs_with_sum_divisible_by_5`:
def test_find_pairs_with_sum_divisible_by_5():
    assert find_pairs_with_sum_divisible_by_5([1, 2, 3]) == [(2, 3), (3, 2)]
    assert find_pairs_with_sum_divisible_by_5([3, 1, 4]) == [(1, 4), (4, 1)]
    assert find_pairs_with_sum_divisible_by_5([7, 2, 5, 0]) == [(5, 5), (5, 0), (0, 5), (0, 0)]
    assert find_pairs_with_sum_divisible_by_5([-2, -4]) is None
    assert find_pairs_with_sum_divisible_by_5([1, 21, 7]) is None
    assert find_pairs_with_sum_divisible_by_5([2, 7, 9]) is None


# 259. Тесты для функции `find_tuples_without_even_numbers`:
def test_find_tuples_without_even_numbers():
    assert find_tuples_without_even_numbers([(1, 3, 5), (2, 4, 6), (7, 9, 11)]) == [(1, 3, 5), (7, 9, 11)]
    assert find_tuples_without_even_numbers([(1, 2), (3, 4), (5, 6)]) is None
    assert find_tuples_without_even_numbers([(1, 3), (5, 7), (9, 11)]) == [(1, 3), (5, 7), (9, 11)]
    assert find_tuples_without_even_numbers([(0, 2, 4), (6, 8, 10)]) is None
    assert find_tuples_without_even_numbers([(1, 3, 5)]) == [(1, 3, 5)]
    assert find_tuples_without_even_numbers([(-1, -3), (-5, -7)]) == [(-1, -3), (-5, -7)]
    assert find_tuples_without_even_numbers([(-2, -4), (-6, -8)]) is None
    assert find_tuples_without_even_numbers([(5, -5), (7, -7)]) == [(5, -5), (7, -7)]
    assert find_tuples_without_even_numbers([(1,), (3,)]) == [(1,), (3,)]


# 260. Тесты для функции `find_integers_in_strings`:
def test_find_integers_in_strings():
    assert find_integers_in_strings(['1', '2', '3']) == [1, 2, 3]
    assert find_integers_in_strings(['a', 'b', 'c']) is None
    assert find_integers_in_strings(['1', 'b', '3']) == [1, 3]
    assert find_integers_in_strings(['123', '456', '789']) == [123, 456, 789]
    assert find_integers_in_strings(['1a', 'b2', '3c']) is None
    assert find_integers_in_strings(['']) is None
    assert find_integers_in_strings(['1', '0', '-3']) == [1, 0, -3]
    assert find_integers_in_strings(['0']) == [0]
    assert find_integers_in_strings(['-1', '-2', '-3']) == [-1, -2, -3]


# 261. Тесты для функции `find_divisible_by_7_and_8_not_56`:
def test_find_divisible_by_7_and_8_not_56():
    assert find_divisible_by_7_and_8_not_56([7, 8, 14, 16, 56, 112]) == [7, 8, 14, 16]
    assert find_divisible_by_7_and_8_not_56([1, 2, 3, 4, 5]) is None
    assert find_divisible_by_7_and_8_not_56([]) is None
    assert find_divisible_by_7_and_8_not_56([49, 64, 9, 21, 32]) == [49, 64, 21, 32]


# 262. Тесты для функции `find_odd_keys_in_dict`:
def test_find_odd_keys_in_dict():
    assert find_odd_keys_in_dict({1: 'a', 2: 'b', 3: 'c'}) == [1, 3]
    assert find_odd_keys_in_dict({4: 'd', 6: 'e'}) is None
    assert find_odd_keys_in_dict({}) is None
    assert find_odd_keys_in_dict({1: 'a', 5: 'b', 8: 'c'}) == [1, 5]


# 263. Тесты для функции `find_even_in_tuple_not_in_list`:
def test_find_even_in_tuple_not_in_list():
    assert find_even_in_tuple_not_in_list((2, 4, 6, 8), [3, 5, 7]) == [2, 4, 6, 8]
    assert find_even_in_tuple_not_in_list((2, 4, 6, 8), [2, 4, 6, 8]) is None
    assert find_even_in_tuple_not_in_list((), [1, 2, 3]) is None
    assert find_even_in_tuple_not_in_list((10, 12, 14), [1, 3, 7]) == [10, 12, 14]


# 264. Тесты для функции `find_divisors_of_100_not_prime`:
def test_find_divisors_of_100_not_prime():
    assert find_divisors_of_100_not_prime([1, 2, 4, 5, 10, 20, 25, 50]) == [1, 4, 10, 20, 25, 50]
    assert find_divisors_of_100_not_prime([2, 5, 7, 11]) is None
    assert find_divisors_of_100_not_prime([10, 20, 30]) == [10, 20]
    assert find_divisors_of_100_not_prime([100, 200]) == [100]


# 265. Тесты для функции `find_in_list_not_in_set`:
def test_find_in_list_not_in_set():
    assert find_in_list_not_in_set([1, 2, 3], {2}) == [1, 3]
    assert find_in_list_not_in_set([1, 2, 3], {1, 2, 3}) is None
    assert find_in_list_not_in_set([], {1, 2, 3}) is None
    assert find_in_list_not_in_set([4, 5, 6], {1, 2, 3}) == [4, 5, 6]


# 266. Тесты для функции `find_sum_of_two_lists`:
def test_find_sum_of_two_lists():
    assert find_sum_of_two_lists([1, 2], [3, 4]) == [4, 5, 5, 6]
    assert find_sum_of_two_lists([], [1, 2, 3]) is None
    assert find_sum_of_two_lists([1, 2], []) is None
    assert find_sum_of_two_lists([0, 0], [0, 0]) == [0, 0, 0, 0]


# 267. Тесты для функции `find_difference_of_two_lists`:
def test_find_difference_of_two_lists():
    assert find_difference_of_two_lists([5, 6], [2, 3]) == [3, 2, 4, 3]
    assert find_difference_of_two_lists([], [1, 2, 3]) is None
    assert find_difference_of_two_lists([1, 2], []) is None
    assert find_difference_of_two_lists([10, 20], [5, 15]) == [5, -5, 15, 5]


# 268. Тесты для функции `find_odd_in_tuple_not_in_list`:
def test_find_odd_in_tuple_not_in_list():
    assert find_odd_in_tuple_not_in_list((1, 3, 5, 7), [2, 4, 6]) == [1, 3, 5, 7]
    assert find_odd_in_tuple_not_in_list((1, 2, 3, 4), [1, 3]) is None
    assert find_odd_in_tuple_not_in_list((), [1, 2, 3]) is None
    assert find_odd_in_tuple_not_in_list((9, 11, 13), [2, 4, 6]) == [9, 11, 13]


# 269. Тесты для функции `find_divisible_by_5_and_6_not_12`:
def test_find_divisible_by_5_and_6_not_12():
    assert find_divisible_by_5_and_6_not_12([30, 60, 90]) == [30, 90]
    assert find_divisible_by_5_and_6_not_12([12, 24, 36]) is None
    assert find_divisible_by_5_and_6_not_12([]) is None
    assert find_divisible_by_5_and_6_not_12([15, 45, 75]) is None


# 270. Тесты для функции `find_odd_not_divisible_by_5_2`:
def test_find_odd_not_divisible_by_5_2():
    assert find_odd_not_divisible_by_5_2([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 7, 9]
    assert find_odd_not_divisible_by_5_2([10, 20, 30]) is None
    assert find_odd_not_divisible_by_5_2([15, 25, 35]) is None
    assert find_odd_not_divisible_by_5_2([2, 4, 6, 8, 12]) is None


# 271. Тесты для функции `find_even_in_list_and_tuple`:
def test_find_even_in_list_and_tuple():
    assert find_even_in_list_and_tuple([2, 4, 6], (4, 6, 8)) == [4, 6]
    assert find_even_in_list_and_tuple([1, 3, 5], (2, 4, 6)) is None
    assert find_even_in_list_and_tuple([], (2, 4, 6)) is None
    assert find_even_in_list_and_tuple([2, 4, 6], (1, 3, 5)) is None


# 272. Тесты для функции `find_product_of_two_numbers`:
def test_find_product_of_two_numbers():
    assert find_product_of_two_numbers([1, 2, 3]) == [1, 2, 3, 2, 4, 6, 3, 6, 9]
    assert find_product_of_two_numbers([0, 1, 2]) == [0, 0, 0, 0, 1, 2, 0, 2, 4]
    assert find_product_of_two_numbers([1]) == [1]
    assert find_product_of_two_numbers([]) is None


# 273. Тесты для функции `find_in_set_not_in_list_2`:
def test_find_in_set_not_in_list_2():
    assert find_in_set_not_in_list_2({1, 2, 3}, [2, 3, 4]) == [1]
    assert find_in_set_not_in_list_2({2, 3, 4}, [2, 3, 4]) is None
    assert find_in_set_not_in_list_2({1, 5, 7}, [2, 3, 4]) == [1, 5, 7]
    assert find_in_set_not_in_list_2(set(), [2, 3, 4]) is None


# 274. Тесты для функции `find_difference_between_lists`:
def test_find_difference_between_lists():
    assert find_difference_between_lists([5, 6], [2, 3]) == [3, 2, 4, 3]
    assert find_difference_between_lists([], [1, 2, 3]) is None
    assert find_difference_between_lists([1, 2], []) is None
    assert find_difference_between_lists([10, 20], [5, 15]) == [5, -5, 15, 5]


# 275. Тесты для функции `find_unique_in_one_list_not_both`:
def test_find_unique_in_one_list_not_both():
    assert find_unique_in_one_list_not_both([1, 2, 3], [3, 4, 5]) == [1, 2, 4, 5]
    assert find_unique_in_one_list_not_both([1, 2, 3], [1, 2, 3]) is None
    assert find_unique_in_one_list_not_both([], [3, 4, 5]) == [3, 4, 5]
    assert find_unique_in_one_list_not_both([1, 2, 3], []) == [1, 2, 3]


# 276. Тесты для функции `find_even_and_divisible_by_3`:
def test_find_even_and_divisible_by_3():
    assert find_even_and_divisible_by_3([6, 12, 18]) == [6, 12, 18]
    assert find_even_and_divisible_by_3([1, 2, 3]) is None
    assert find_even_and_divisible_by_3([]) is None
    assert find_even_and_divisible_by_3([5, 7, 10]) is None


# 277. Тесты для функции `find_squares_not_divisible_by_5`:
def test_find_squares_not_divisible_by_5():
    assert find_squares_not_divisible_by_5([1, 4, 9, 16, 25, 36]) == [1, 4, 9, 16, 36]
    assert find_squares_not_divisible_by_5([25, 50, 75]) is None
    assert find_squares_not_divisible_by_5([]) is None
    assert find_squares_not_divisible_by_5([100, 144, 169]) == [144, 169]


# 278. Тесты для функции `find_divisible_by_7_and_8_not_56_2`:
def test_find_divisible_by_7_and_8_not_56_2():
    assert find_divisible_by_7_and_8_not_56_2([7, 8, 14, 16, 56, 112]) == [56, 112]
    assert find_divisible_by_7_and_8_not_56_2([1, 2, 3, 4, 5]) is None
    assert find_divisible_by_7_and_8_not_56_2([]) is None
    assert find_divisible_by_7_and_8_not_56_2([56, 112, 21, 32]) == [56, 112]


# 279. Тесты для функции `find_in_list_and_tuple`:
def test_find_in_list_and_tuple():
    assert find_in_list_and_tuple([1, 2, 3], (3, 4, 5)) == [3]
    assert find_in_list_and_tuple([1, 2, 3], (1, 2, 3)) == [1, 2, 3]
    assert find_in_list_and_tuple([], (1, 2, 3)) is None
    assert find_in_list_and_tuple([1, 2, 3], ()) is None


# 280. Тесты для функции `find_sum_of_two_not_divisible_by_4`:
def test_find_sum_of_two_not_divisible_by_4():
    assert find_sum_of_two_not_divisible_by_4([1, 2, 3, 4]) == [3, 5, 5, 6, 7]
    assert find_sum_of_two_not_divisible_by_4([4, 8, 12]) is None
    assert find_sum_of_two_not_divisible_by_4([]) is None
    assert find_sum_of_two_not_divisible_by_4([3, 6, 9]) == [9, 15]


# 281. Тесты для функции `find_in_both_lists`:
def test_find_in_both_lists():
    assert find_in_both_lists([1, 2, 3], [3, 4, 5]) == [3]
    assert find_in_both_lists([1, 2, 3], [4, 5, 6]) is None
    assert find_in_both_lists([], [1, 2, 3]) is None
    assert find_in_both_lists([1, 2, 3], []) is None
    assert find_in_both_lists([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert find_in_both_lists([-1, -2, -3], [-3, -4, -5]) == [-3]
    assert find_in_both_lists([0, 2, 4], [4, 0, 6]) == [0, 4]
    assert find_in_both_lists([1.1, 2.2, 3.3], [3.3, 4.4, 5.5]) == [3.3]
    assert find_in_both_lists(["a", "b", "c"], ["c", "d", "e"]) == ["c"]


# 282. Тесты для функции `find_not_in_list`:
def test_find_not_in_list():
    assert find_not_in_list([1, 2, 3], [3, 4, 5]) == [1, 2]
    assert find_not_in_list([1, 2, 3], [1, 2, 3]) is None
    assert find_not_in_list([], [1, 2, 3]) is None
    assert find_not_in_list([1, 2, 3], []) == [1, 2, 3]
    assert find_not_in_list([-1, -2, -3], [-3, -4, -5]) == [-1, -2]
    assert find_not_in_list([0, 2, 4], [4, 0, 6]) == [2]
    assert find_not_in_list([1.1, 2.2, 3.3], [3.3, 4.4, 5.5]) == [1.1, 2.2]
    assert find_not_in_list(["a", "b", "c"], ["c", "d", "e"]) == ["a", "b"]


# 283. Тесты для функции `find_product_not_divisible_by_7`:
def test_find_product_not_divisible_by_7():
    assert find_product_not_divisible_by_7([7, 14, 21]) is None
    assert find_product_not_divisible_by_7([1, 7, 14]) is None
    assert find_product_not_divisible_by_7([]) is None
    assert find_product_not_divisible_by_7([2, 3]) == [6]
    assert find_product_not_divisible_by_7([3, 5]) == [15]
    assert find_product_not_divisible_by_7([1, 2, 3, 4]) == [2, 3, 4, 6, 8, 12]


# 284. Тесты для функции `find_product_of_two_odds`:
def test_find_product_of_two_odds():
    assert find_product_of_two_odds([1, 3, 5, 7]) == [3, 5, 7, 15, 21, 35]
    assert find_product_of_two_odds([2, 4, 6]) is None
    assert find_product_of_two_odds([1, 2, 3, 4]) == [3]
    assert find_product_of_two_odds([]) is None
    assert find_product_of_two_odds([9, 7]) == [63]
    assert find_product_of_two_odds([11, 15, 19]) == [165, 209, 285]


# 285. Тесты для функции `find_sum_of_two_odds`:
def test_find_sum_of_two_odds():
    assert find_sum_of_two_odds([1, 3, 5, 7]) == [4, 6, 8, 8, 10, 12]
    assert find_sum_of_two_odds([2, 4, 6]) is None
    assert find_sum_of_two_odds([1, 2, 3, 4]) == [4]
    assert find_sum_of_two_odds([]) is None
    assert find_sum_of_two_odds([9, 7]) == [16]
    assert find_sum_of_two_odds([11, 15, 19]) == [26, 30, 34]


# 286. Тесты для функции `find_even_in_tuple`:
def test_find_even_in_tuple():
    assert find_even_in_tuple((1, 2, 3, 4, 5)) == [2, 4]
    assert find_even_in_tuple((1, 3, 5)) is None
    assert find_even_in_tuple((2, 4, 6, 8)) == [2, 4, 6, 8]
    assert find_even_in_tuple(()) is None
    assert find_even_in_tuple((1, 3, 4)) == [4]
    assert find_even_in_tuple((2, 0, -2, -4)) == [2, 0, -2, -4]
    assert find_even_in_tuple((7, 8, 10)) == [8, 10]


# 287. Тесты для функции `find_product_not_divisible_by_5`:
def test_find_product_not_divisible_by_5():
    assert find_product_not_divisible_by_5([1, 2, 3, 4]) == [2, 3, 4, 6, 8, 12]
    assert find_product_not_divisible_by_5([5, 10, 15]) is None
    assert find_product_not_divisible_by_5([1, 5, 10]) is None
    assert find_product_not_divisible_by_5([]) is None
    assert find_product_not_divisible_by_5([2, 3]) == [6]
    assert find_product_not_divisible_by_5([3, 4, 7]) == [12, 21, 28]
    assert find_product_not_divisible_by_5([11, 3, 2]) == [33, 22, 6]


# 288. Тесты для функции `find_keys_in_dict_not_in_other`:
def test_find_keys_in_dict_not_in_other():
    assert find_keys_in_dict_not_in_other({"a": 1, "b": 2, "c": 3}, {"b": 4, "d": 5}) == ["a", "c"]
    assert find_keys_in_dict_not_in_other({"a": 1}, {"a": 2}) is None
    assert find_keys_in_dict_not_in_other({}, {"a": 2}) is None
    assert find_keys_in_dict_not_in_other({"a": 1, "b": 2}, {}) == ["a", "b"]
    assert find_keys_in_dict_not_in_other({"x": 9, "y": 8}, {"y": 7}) == ["x"]
    assert find_keys_in_dict_not_in_other({"k": 11}, {"m": 13}) == ["k"]


# 289. Тесты для функции `find_difference_in_tuple`:
def test_find_difference_in_tuple():
    assert find_difference_in_tuple((1, 2, 3)) == [1, 2, 1]
    assert find_difference_in_tuple((1, 1, 1)) == [0, 0, 0]
    assert find_difference_in_tuple((4, 6, 8)) == [2, 4, 2]
    assert find_difference_in_tuple(()) is None
    assert find_difference_in_tuple((3,)) is None
    assert find_difference_in_tuple((10, 5, 1)) == [5, 9, 4]


# 290. Тесты для функции `find_difference_between_lists_2`:
def test_find_difference_between_lists_2():
    assert find_difference_between_lists_2([1, 2, 3], [4, 5, 6]) == [3, 4, 5, 2, 3, 4, 1, 2, 3]
    assert find_difference_between_lists_2([1, 1, 1], [1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert find_difference_between_lists_2([10, 20], [1, 2]) == [9, 8, 19, 18]
    assert find_difference_between_lists_2([5], [3]) == [2]
    assert find_difference_between_lists_2([], [1, 2, 3]) is None
    assert find_difference_between_lists_2([1, 2, 3], []) is None
    assert find_difference_between_lists_2([], []) is None


# 291. Тесты для функции `find_odd_in_one_list`:
def test_find_odd_in_one_list():
    assert find_odd_in_one_list([1, 2, 3], [3, 4, 5]) == [1, 5]
    assert find_odd_in_one_list([1, 3, 5], [1, 3, 5]) is None
    assert find_odd_in_one_list([], [1, 3, 5]) == [1, 3, 5]
    assert find_odd_in_one_list([1, 2, 4], []) == [1]
    assert find_odd_in_one_list([-1, -2, -3], [-3, -4, -5]) == [-1, -5]
    assert find_odd_in_one_list([0, 2, 4], [4, 0, 6]) is None
    assert find_odd_in_one_list([1, 2, 3], [1, 4, 3]) is None
    assert find_odd_in_one_list([1.1, 2.2, 3.3], [3.3, 4.4, 5.5]) == [1.1, 2.2, 4.4, 5.5]


# 292. Тесты для функции `find_sum_of_two_from_one_list`:
def test_find_sum_of_two_from_one_list():
    assert find_sum_of_two_from_one_list([1, 2, 3, 4]) == [3, 4, 5, 5, 6, 7]
    assert find_sum_of_two_from_one_list([1, 1, 1]) == [2, 2, 2]
    assert find_sum_of_two_from_one_list([]) is None
    assert find_sum_of_two_from_one_list([0, 2, 4]) == [2, 4, 6]
    assert find_sum_of_two_from_one_list([-1, -2, -3]) == [-3, -4, -5]
    assert find_sum_of_two_from_one_list([1.1, 2.2, 3.3]) == [3.3000000000000003, 4.4, 5.5]
    assert find_sum_of_two_from_one_list([0, 0, 0]) == [0, 0, 0]


# 293. Тесты для функции `find_common_not_in_both_lists`:
def test_find_common_not_in_both_lists():
    assert find_common_not_in_both_lists([1, 2, 3], [3, 4, 5]) == [3]
    assert find_common_not_in_both_lists([1, 2, 3], [4, 5, 6]) is None
    assert find_common_not_in_both_lists([], [1, 2, 3]) is None
    assert find_common_not_in_both_lists([1, 2, 3], []) is None
    assert find_common_not_in_both_lists([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert find_common_not_in_both_lists([-1, -2, -3], [-3, -4, -5]) == [-3]
    assert find_common_not_in_both_lists([0, 2, 4], [4, 0, 6]) == [0, 4]
    assert find_common_not_in_both_lists([1.1, 2.2, 3.3], [3.3, 4.4, 5.5]) == [3.3]
    assert find_common_not_in_both_lists(["a", "b", "c"], ["c", "d", "e"]) == ["c"]


# 294. Тесты для функции `find_sum_of_elements_from_two_lists`:
def test_find_sum_of_elements_from_two_lists():
    assert find_sum_of_elements_from_two_lists([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert find_sum_of_elements_from_two_lists([1, 1, 1], [1, 1, 1]) == [2, 2, 2]
    assert find_sum_of_elements_from_two_lists([], [1, 2, 3]) is None
    assert find_sum_of_elements_from_two_lists([1, 2, 3], []) is None
    assert find_sum_of_elements_from_two_lists([1, 2, 3], [1, 2, 3]) == [2, 4, 6]
    assert find_sum_of_elements_from_two_lists([-1, -2, -3], [-3, -4, -5]) == [-4, -6, -8]
    assert find_sum_of_elements_from_two_lists([0, 2, 4], [4, 0, 6]) == [4, 2, 10]


# 295. Тесты для функции `find_difference_of_elements_from_two_lists`:
def test_find_difference_of_elements_from_two_lists():
    assert find_difference_of_elements_from_two_lists([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]
    assert find_difference_of_elements_from_two_lists([1, 1, 1], [1, 1, 1]) == [0, 0, 0]
    assert find_difference_of_elements_from_two_lists([], [1, 2, 3]) is None
    assert find_difference_of_elements_from_two_lists([1, 2, 3], []) is None
    assert find_difference_of_elements_from_two_lists([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    assert find_difference_of_elements_from_two_lists([-1, -2, -3], [-3, -4, -5]) == [2, 2, 2]
    assert find_difference_of_elements_from_two_lists([0, 2, 4], [4, 0, 6]) == [-4, 2, -2]


# 296. Тесты для функции `square_numbers`:
def test_square_numbers():
    assert square_numbers([1, 2, 3, 4]) == [1, 4, 9, 16]
    assert square_numbers([0, 1, -1, 2]) == [0, 1, 1, 4]
    assert square_numbers([5, 6, 7]) == [25, 36, 49]
    assert square_numbers([-5, -6, -7]) == [25, 36, 49]
    assert square_numbers([]) is None
    assert square_numbers([1]) == [1]
    assert square_numbers([2.2, 3.3]) == [4.840000000000001, 10.889999999999999]


# 297. Тесты для функции `find_divisible_by_3_not_5`:
def test_find_divisible_by_3_not_5():
    assert find_divisible_by_3_not_5([3, 6, 9, 12, 15]) == [3, 6, 9, 12]
    assert find_divisible_by_3_not_5([5, 10, 15]) is None
    assert find_divisible_by_3_not_5([1, 2, 4, 5]) is None
    assert find_divisible_by_3_not_5([]) is None
    assert find_divisible_by_3_not_5([3, 5, 7, 11]) == [3]
    assert find_divisible_by_3_not_5([6, 9, 18]) == [6, 9, 18]
    assert find_divisible_by_3_not_5([-3, -6, -9]) == [-3, -6, -9]
    assert find_divisible_by_3_not_5([21, 25, 30]) == [21]
    assert find_divisible_by_3_not_5([0, 3, 6, 15, 30]) == [3, 6]


# 298. Тесты для функции `find_unique_in_one_list_3`:
def test_find_unique_in_one_list_3():
    assert find_unique_in_one_list_3([1, 2, 3], [3, 2, 1]) == [1, 3, 3, 1]
    assert find_unique_in_one_list_3([1, 1, 1], [1, 1, 1]) is None
    assert find_unique_in_one_list_3([], [1, 2, 3]) is None
    assert find_unique_in_one_list_3([1, 2, 3], []) is None
    assert find_unique_in_one_list_3([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6]
    assert find_unique_in_one_list_3([-1, -2, -3], [-3, -2, -1]) == [-1, -3, -3, -1]
    assert find_unique_in_one_list_3([0, 2, 4], [4, 2, 0]) == [0, 4, 4, 0]


# 299. Тесты для функции `find_in_list_not_in_tuple_2`:
def test_find_in_list_not_in_tuple_2():
    assert find_in_list_not_in_tuple_2([1, 2, 3], (3, 4, 5)) == [1, 2]
    assert find_in_list_not_in_tuple_2([1, 2, 3], (1, 2, 3)) is None
    assert find_in_list_not_in_tuple_2([], (1, 2, 3)) is None
    assert find_in_list_not_in_tuple_2([1, 2, 3], ()) == [1, 2, 3]
    assert find_in_list_not_in_tuple_2([-1, -2, -3], (-3, -4, -5)) == [-1, -2]
    assert find_in_list_not_in_tuple_2([0, 2, 4], (4, 0, 6)) == [2]
    assert find_in_list_not_in_tuple_2([1.1, 2.2, 3.3], (3.3, 4.4, 5.5)) == [1.1, 2.2]
    assert find_in_list_not_in_tuple_2(["a", "b", "c"], ("c", "d", "e")) == ["a", "b"]
    assert find_in_list_not_in_tuple_2(["a", "b", "c"], ("a", "b", "c")) is None


# 300. Тесты для функции `find_cubes`:
def test_find_cubes():
    assert find_cubes([1, 2, 3]) == [1, 8, 27]
    assert find_cubes([-1, -2, -3]) == [-1, -8, -27]
    assert find_cubes([0, 2, 4]) == [0, 8, 64]
    assert find_cubes([]) is None
    assert find_cubes([1, 1, 1]) == [1, 1, 1]
    assert find_cubes([2]) == [8]
    assert find_cubes([3, 5, 7]) == [27, 125, 343]
    assert find_cubes([-4, -6, -8]) == [-64, -216, -512]
    assert find_cubes([1.1, 2.2]) == [1.3310000000000004, 10.648000000000003]


# 301. Тесты для функции `find_divisible_by_2_and_3`
def test_find_divisible_by_2_and_3():
    assert find_divisible_by_2_and_3([6, 12, 18]) == [6, 12, 18]
    assert find_divisible_by_2_and_3([7, 14, 21]) is None
    assert find_divisible_by_2_and_3([2, 4, 8]) is None
    assert find_divisible_by_2_and_3([3, 9, 15]) is None
    assert find_divisible_by_2_and_3([6]) == [6]
    assert find_divisible_by_2_and_3([1, 2, 3]) is None
    assert find_divisible_by_2_and_3([]) is None


# 302. Тесты для функции `find_powers_of_numbers`
def test_find_powers_of_numbers():
    assert find_powers_of_numbers([2, 3], 2) == [4, 9]
    assert find_powers_of_numbers([1, 2, 3], 3) == [1, 8, 27]
    assert find_powers_of_numbers([], 2) is None
    assert find_powers_of_numbers([0], 5) == [0]
    assert find_powers_of_numbers([2], 0) == [1]
    assert find_powers_of_numbers([-2, -3], 2) == [4, 9]
    assert find_powers_of_numbers([2], 1) == [2]


# 303. Тесты для функции `find_difference_between_two_lists`
def test_find_difference_between_two_lists():
    assert find_difference_between_two_lists([1, 3, 5], [1, 2, 3]) == [0, 1, 2]
    assert find_difference_between_two_lists([4, 6], [2, 3]) == [2, 3]
    assert find_difference_between_two_lists([], []) is None
    assert find_difference_between_two_lists([1], [0]) == [1]
    assert find_difference_between_two_lists([0], [1]) == [1]
    assert find_difference_between_two_lists([1], [-1]) == [2]
    assert find_difference_between_two_lists([2, 3, 4], [5, 3, 1]) == [3, 0, 3]


# 304. Тесты для функции `find_keys_in_both_dicts`
def test_find_keys_in_both_dicts():
    assert find_keys_in_both_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) == ["b"]
    assert find_keys_in_both_dicts({"a": 1, "b": 2}, {"d": 3, "e": 4}) is None
    assert find_keys_in_both_dicts({"a": 1}, {"a": 4}) == ["a"]
    assert find_keys_in_both_dicts({}, {"a": 4}) is None
    assert find_keys_in_both_dicts({"a": 1, "b": 2}, {}) is None
    assert find_keys_in_both_dicts({}, {}) is None
    assert find_keys_in_both_dicts({"a": 1, "b": 2, "c": 3}, {"c": 4, "d": 5, "a": 0}) == ["a", "c"]


# 305. Тесты для функции `find_product_of_elements_from_two_lists`
def test_find_product_of_elements_from_two_lists():
    assert find_product_of_elements_from_two_lists([1, 2], [3, 4]) == [3, 8]
    assert find_product_of_elements_from_two_lists([5, 6], [0, 7]) == [0, 42]
    assert find_product_of_elements_from_two_lists([1], [1]) == [1]
    assert find_product_of_elements_from_two_lists([0], [2]) == [0]
    assert find_product_of_elements_from_two_lists([2], [0]) == [0]
    assert find_product_of_elements_from_two_lists([], []) is None
    assert find_product_of_elements_from_two_lists([2, 3], [4, 1]) == [8, 3]


# 306. Тесты для функции `find_keys_in_dict_not_in_list`
def test_find_keys_in_dict_not_in_list():
    assert find_keys_in_dict_not_in_list({"a": 1, "b": 2}, ["a"]) == ["b"]
    assert find_keys_in_dict_not_in_list({"a": 1, "b": 2}, ["a", "b"]) is None
    assert find_keys_in_dict_not_in_list({}, ["a"]) is None
    assert find_keys_in_dict_not_in_list({"a": 1}, []) == ["a"]
    assert find_keys_in_dict_not_in_list({"a": 1, "b": 2}, []) == ["a", "b"]
    assert find_keys_in_dict_not_in_list({"a": 1, "b": 2}, ["c"]) == ["a", "b"]
    assert find_keys_in_dict_not_in_list({"a": 1}, ["a", "b"]) is None


# 307. Тесты для функции `find_powers_of_numbers_in_list`
def test_find_powers_of_numbers_in_list():
    assert find_powers_of_numbers_in_list([2, 3], 2) == [4, 9]
    assert find_powers_of_numbers_in_list([1, 2, 3], 3) == [1, 8, 27]
    assert find_powers_of_numbers_in_list([], 2) is None
    assert find_powers_of_numbers_in_list([0], 5) == [0]
    assert find_powers_of_numbers_in_list([2], 0) == [1]
    assert find_powers_of_numbers_in_list([-2, -3], 2) == [4, 9]
    assert find_powers_of_numbers_in_list([2], 1) == [2]


# 308. Тесты для функции `find_elements_in_both_sets`
def test_find_elements_in_both_sets():
    assert find_elements_in_both_sets({1, 2, 3}, {2, 3, 4}) == [2, 3]
    assert find_elements_in_both_sets({1, 2, 3}, {4, 5, 6}) is None
    assert find_elements_in_both_sets(set(), {1, 2, 3}) is None
    assert find_elements_in_both_sets({1}, {1}) == [1]
    assert find_elements_in_both_sets({1, 2, 3}, {1}) == [1]
    assert find_elements_in_both_sets(set(), set()) is None
    assert find_elements_in_both_sets({0, 1, 2}, {2, 0, 3}) == [0, 2]


# 309. Тесты для функции `find_diff_between_lists`
def test_find_diff_between_lists():
    assert find_diff_between_lists([1, 2, 3], [4, 5, 6]) == [3, 3, 3]
    assert find_diff_between_lists([7, 8, 9], [1, 2, 3]) == [6, 6, 6]
    assert find_diff_between_lists([0], [0]) == [0]
    assert find_diff_between_lists([], []) is None
    assert find_diff_between_lists([1], [0]) == [1]
    assert find_diff_between_lists([0], [1]) == [1]
    assert find_diff_between_lists([2, 3, 4], [5, 3, 1]) == [3, 0, 3]


# 310. Тесты для функции `find_sum_of_two_lists_2`
def test_find_sum_of_two_lists_2():
    assert find_sum_of_two_lists_2([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert find_sum_of_two_lists_2([7, 8, 9], [1, 2, 3]) == [8, 10, 12]
    assert find_sum_of_two_lists_2([0], [0]) == [0]
    assert find_sum_of_two_lists_2([], []) is None
    assert find_sum_of_two_lists_2([1], [0]) == [1]
    assert find_sum_of_two_lists_2([0], [1]) == [1]
    assert find_sum_of_two_lists_2([2, 3, 4], [5, 3, 1]) == [7, 6, 5]


# 311. Тесты для функции `find_in_tuple_not_in_list`
def test_find_in_tuple_not_in_list():
    assert find_in_tuple_not_in_list((1, 2, 3), [2, 3, 4]) == [1]
    assert find_in_tuple_not_in_list((5, 6), [6, 7]) == [5]
    assert find_in_tuple_not_in_list((), [1, 2]) is None
    assert find_in_tuple_not_in_list((1,), [1]) is None
    assert find_in_tuple_not_in_list((1,), []) == [1]
    assert find_in_tuple_not_in_list((1, 2, 3), (2, 4)) == [1, 3]
    assert find_in_tuple_not_in_list((1, 2), (1, 2, 3)) is None


# 312. Тесты для функции `find_divisible_by_10_not_20`
def test_find_divisible_by_10_not_20():
    assert find_divisible_by_10_not_20([10, 20, 30, 40]) == [10, 30]
    assert find_divisible_by_10_not_20([5, 10, 15, 25]) == [10]
    assert find_divisible_by_10_not_20([1, 2, 3, 4]) is None
    assert find_divisible_by_10_not_20([20, 40, 60]) is None
    assert find_divisible_by_10_not_20([10, 50, 70]) == [10, 50, 70]
    assert find_divisible_by_10_not_20([]) is None
    assert find_divisible_by_10_not_20([30, 50, 90]) == [30, 50, 90]


# 313. Тесты для функции `find_sum_from_two_lists`
def test_find_sum_from_two_lists():
    assert find_sum_from_two_lists([1, 2], [3, 4]) == [4, 6]
    assert find_sum_from_two_lists([5, 6], [1, 2]) == [6, 8]
    assert find_sum_from_two_lists([], []) is None
    assert find_sum_from_two_lists([1], [1]) == [2]
    assert find_sum_from_two_lists([0], [0]) == [0]
    assert find_sum_from_two_lists([2, 3], [4, 5]) == [6, 8]
    assert find_sum_from_two_lists([5, 5], [5, 5]) == [10, 10]


# 314. Тесты для функции `find_common_elements_in_sets`
def test_find_common_elements_in_sets():
    assert find_common_elements_in_sets({1, 2, 3}, {3, 4, 5}) == [3]
    assert find_common_elements_in_sets({6, 7}, {7, 8}) == [7]
    assert find_common_elements_in_sets(set(), {1, 2}) is None
    assert find_common_elements_in_sets({1}, {1}) == [1]
    assert find_common_elements_in_sets({1, 2, 3}, {4, 5, 6}) is None
    assert find_common_elements_in_sets(set(), set()) is None
    assert find_common_elements_in_sets({0, 1, 2}, {2, 3, 0}) == [0, 2]


# 315. Тесты для функции `find_product_in_list`
def test_find_product_in_list():
    assert find_product_in_list([1, 2, 3]) == [2, 3, 6]
    assert find_product_in_list([4, 5]) == [20]
    assert find_product_in_list([]) is None
    assert find_product_in_list([0, 1]) == [0]
    assert find_product_in_list([1]) is None
    assert find_product_in_list([1, 2]) == [2]
    assert find_product_in_list([2, 3, 4]) == [6, 8, 12]


# 316. Тесты для функции `find_in_list_not_in_dict`
def test_find_in_list_not_in_dict():
    assert find_in_list_not_in_dict([1, 2, 3], {3: "a", 4: "b"}) == [1, 2]
    assert find_in_list_not_in_dict([5, 6], {5: "x", 7: "y"}) == [6]
    assert find_in_list_not_in_dict([], {1: "a"}) is None
    assert find_in_list_not_in_dict([1], {1: "a"}) is None
    assert find_in_list_not_in_dict([1], {}) == [1]
    assert find_in_list_not_in_dict([1, 2, 3], {}) == [1, 2, 3]
    assert find_in_list_not_in_dict([1, 2], {3: "b", 4: "c"}) == [1, 2]


# 317. Тесты для функции `merge_dicts_2`
def test_merge_dicts_2():
    assert merge_dicts_2({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}
    assert merge_dicts_2({}, {"c": 3}) == {"c": 3}
    assert merge_dicts_2({"d": 4}, {}) == {"d": 4}
    assert merge_dicts_2({}, {}) is None
    assert merge_dicts_2({"a": 1}, {"a": 2}) == {"a": 2}
    assert merge_dicts_2({"a": 1, "b": 2}, {"c": 3}) == {"a": 1, "b": 2, "c": 3}
    assert merge_dicts_2({"x": 0}, {"y": -1}) == {"x": 0, "y": -1}


# 318. Тесты для функции `find_in_one_set_not_other`
def test_find_in_one_set_not_other():
    assert find_in_one_set_not_other({1, 2}, {2, 3}) == [1, 3]
    assert find_in_one_set_not_other({5, 6}, {6, 7}) == [5, 7]
    assert find_in_one_set_not_other(set(), {1, 2}) == [1, 2]
    assert find_in_one_set_not_other({1}, {1}) is None
    assert find_in_one_set_not_other({1}, set()) == [1]
    assert find_in_one_set_not_other(set(), set()) is None
    assert find_in_one_set_not_other({1, 2, 3}, {4, 5, 6}) == [1, 2, 3, 4, 5, 6]


# 319. Тесты для функции `find_division_from_two_lists`
def test_find_division_from_two_lists():
    assert find_division_from_two_lists([1, 2], [1, 2]) == [1, 1]
    assert find_division_from_two_lists([4, 6], [2, 3]) == [2, 2]
    assert find_division_from_two_lists([], []) is None
    assert find_division_from_two_lists([1], [1]) == [1]
    assert find_division_from_two_lists([5], [0]) is None
    assert find_division_from_two_lists([1, 2], [0, 1]) == [2]
    assert find_division_from_two_lists([0, 1], [1, 2]) == [0, 0.5]


# 320. Тесты для функции `find_common_less_in_one_list`
def test_find_common_less_in_one_list():
    assert find_common_less_in_one_list([1, 2, 3], [2, 3, 3]) == [3]
    assert find_common_less_in_one_list([4, 5, 6], [5, 6, 7]) is None
    assert find_common_less_in_one_list([], []) is None
    assert find_common_less_in_one_list([1], [1]) is None
    assert find_common_less_in_one_list([1, 2, 3], [1, 2, 2, 3]) == [2]


# 321. Тесты для функции `find_in_first_not_in_second`
def test_find_in_first_not_in_second():
    assert find_in_first_not_in_second([1, 2, 3], [2, 3, 4]) == [1]
    assert find_in_first_not_in_second([1, 2, 3], [1, 2, 3]) is None
    assert find_in_first_not_in_second([1, 2, 3, 4, 5], [4, 5]) == [1, 2, 3]
    assert find_in_first_not_in_second([], [1, 2, 3]) is None
    assert find_in_first_not_in_second([1, 2, 3], []) == [1, 2, 3]


# 322. Тесты для функции `find_common_elements_diff_index`
def test_find_common_elements_diff_index():
    assert find_common_elements_diff_index([1, 2, 3], [3, 2, 1]) == [1, 3]
    assert find_common_elements_diff_index([1, 2, 3], [1, 2, 3]) is None
    assert find_common_elements_diff_index([1, 2, 2, 3], [2, 3, 1, 2]) == [1, 2, 3]
    assert find_common_elements_diff_index([], [1, 2, 3]) is None
    assert find_common_elements_diff_index([1, 2, 3], []) is None


# 323. Тесты для функции `add_values_of_dicts`
def test_add_values_of_dicts():
    assert add_values_of_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == {'b': 5}
    assert add_values_of_dicts({'a': 1, 'b': 2}, {'c': 3, 'd': 4}) is None
    assert add_values_of_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 2, 'c': 3}) == {'b': 4, 'c': 6}
    assert add_values_of_dicts({}, {'a': 1, 'b': 2}) is None
    assert add_values_of_dicts({'a': 1, 'b': 2}, {}) is None


# 324. Тесты для функции `find_more_in_one_set`
def test_find_more_in_one_set():
    assert find_more_in_one_set({1, 2, 3}, {1, 2}) is None
    assert find_more_in_one_set({1, 2, 2, 3}, {1, 2}) is None
    assert find_more_in_one_set({1, 2, 2, 3, 3}, {2, 3}) == [3]
    assert find_more_in_one_set({1, 2}, {3, 1}) is None
    assert find_more_in_one_set({1, 21, 1, 2}, {21, 2}) == [21]


# 325. Тесты для функции `multiply_numbers_by_two`
def test_multiply_numbers_by_two():
    assert multiply_numbers_by_two([1, 2, 3]) == [2, 4, 6]
    assert multiply_numbers_by_two([0, -1, -2]) == [0, -2, -4]
    assert multiply_numbers_by_two([10, 100, 1000]) == [20, 200, 2000]
    assert multiply_numbers_by_two([]) is None
    assert multiply_numbers_by_two([1]) == [2]


# 326. Тесты для функции `sum_dict_values`
def test_sum_dict_values():
    assert sum_dict_values({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == {'b': 5}
    assert sum_dict_values({'a': 1, 'b': 2}, {'c': 3, 'd': 4}) is None
    assert sum_dict_values({'a': 1, 'b': 2, 'c': 3}, {'b': 2, 'c': 3}) == {'b': 4, 'c': 6}
    assert sum_dict_values({}, {'a': 1, 'b': 2}) is None
    assert sum_dict_values({'a': 1, 'b': 2}, {}) is None


# 327. Тесты для функции `find_squares_2`
def test_find_squares_2():
    assert find_squares_2([1, 2, 3]) == [1, 4, 9]
    assert find_squares_2([0, -1, -2]) == [0, 1, 4]
    assert find_squares_2([10, 100, 1000]) == [100, 10000, 1000000]
    assert find_squares_2([]) is None
    assert find_squares_2([1]) == [1]


# 328. Тесты для функции `find_difference_of_sets`
def test_find_difference_of_sets():
    assert find_difference_of_sets({1, 2, 3}, {2, 3, 4}) == [1]
    assert find_difference_of_sets({1, 2, 3}, {1, 2, 3}) is None
    assert find_difference_of_sets({1, 2, 3, 4}, {3, 4}) == [1, 2]
    assert find_difference_of_sets({1, 2}, {3, 4}) == [1, 2]
    assert find_difference_of_sets(set(), {1, 2, 3}) is None


# 329. Тесты для функции `find_sum_list_set`
def test_find_sum_list_set():
    assert find_sum_list_set([1, 2, 3], {2, 3, 4}) == [3, 4]
    assert find_sum_list_set([1, 2, 3], {1, 2, 3}) == [2, 3, 4]
    assert find_sum_list_set([1, 2, 3, 4], {4, 5}) == [5]
    assert find_sum_list_set([], {1, 2, 3}) is None
    assert find_sum_list_set([1, 2, 3], set()) is None


# 330. Тесты для функции `find_in_set_not_in_other_set`
def test_find_in_set_not_in_other_set():
    assert find_in_set_not_in_other_set({1, 2, 3}, {2, 3, 4}) == [1]
    assert find_in_set_not_in_other_set({1, 2, 3}, {1, 2, 3}) is None
    assert find_in_set_not_in_other_set({1, 2, 3, 4}, {3, 4}) == [1, 2]
    assert find_in_set_not_in_other_set({1, 2}, {3, 4}) == [1, 2]
    assert find_in_set_not_in_other_set(set(), {1, 2, 3}) is None


# 331. Тесты для функции `divide_elements_of_lists`
def test_divide_elements_of_lists():
    assert divide_elements_of_lists([4, 9, 16], [2, 3, 4]) == [2, 3, 4]
    assert divide_elements_of_lists([4, 9, 16], [2, 0, 4]) == [2, 4]
    assert divide_elements_of_lists([1, 2, 3], [0, 1, 1]) == [2, 3]
    assert divide_elements_of_lists([], [1, 2, 3]) is None
    assert divide_elements_of_lists([1, 2, 3], []) is None


# 332. Тесты для функции `find_in_both_sets_not_in_one`
def test_find_in_both_sets_not_in_one():
    assert find_in_both_sets_not_in_one({1, 2, 3}, {3, 4, 5}) == [1, 2, 4, 5]
    assert find_in_both_sets_not_in_one({1, 2}, {2, 3}) == [1, 3]
    assert find_in_both_sets_not_in_one({1, 2, 3}, {4, 5, 6}) == [1, 2, 3, 4, 5, 6]
    assert find_in_both_sets_not_in_one({1, 2, 3}, {1, 2, 3}) is None
    assert find_in_both_sets_not_in_one(set(), set()) is None


# 333. Тесты для функции `subtract_set_from_list`
def test_subtract_set_from_list():
    assert subtract_set_from_list([1, 2, 3], {2, 3, 4}) == [1]
    assert subtract_set_from_list([1, 2, 3], {1, 2, 3}) is None
    assert subtract_set_from_list([1, 2, 3, 4], {4, 5}) == [1, 2, 3]
    assert subtract_set_from_list([], {1, 2, 3}) is None
    assert subtract_set_from_list([1, 2, 3], set()) == [1, 2, 3]


# 334. Тесты для функции `find_sum_of_tuples`
def test_find_sum_of_tuples():
    assert find_sum_of_tuples((1, 2, 3), (4, 5, 6)) == [5, 7, 9]
    assert find_sum_of_tuples((1, 2), (1, 2, 3)) == [2, 4]
    assert find_sum_of_tuples((0, 0, 0), (0, 0, 0)) == [0, 0, 0]
    assert find_sum_of_tuples((), ()) is None
    assert find_sum_of_tuples((1, 2, 3), ()) is None


# 335. Тесты для функции `find_in_one_set_not_other_2`
def test_find_in_one_set_not_other_2():
    assert find_in_one_set_not_other_2({1, 2, 3}, {2, 3, 4}) == [1, 4]
    assert find_in_one_set_not_other_2({1, 2, 3}, {1, 2, 3}) is None
    assert find_in_one_set_not_other_2({1, 2, 3, 4}, {3, 4}) == [1, 2]
    assert find_in_one_set_not_other_2({1, 2}, {3, 4}) == [1, 2, 3, 4]
    assert find_in_one_set_not_other_2(set(), {1, 2, 3}) == [1, 2, 3]


# 336. Тесты для функции `find_divisible_by_4_not_8`
def test_find_divisible_by_4_not_8():
    assert find_divisible_by_4_not_8([4, 8, 16]) == [4]
    assert find_divisible_by_4_not_8([0, 8, 16]) is None
    assert find_divisible_by_4_not_8([4, 12, 20]) == [4, 12, 20]
    assert find_divisible_by_4_not_8([]) is None
    assert find_divisible_by_4_not_8([3, 5, 7]) is None


# 337. Тесты для функции `find_keys_in_dict1_not_in_dict2`
def test_find_keys_in_dict1_not_in_dict2():
    assert find_keys_in_dict1_not_in_dict2({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == ['a']
    assert find_keys_in_dict1_not_in_dict2({'a': 1, 'b': 2}, {'a': 1, 'b': 2}) is None
    assert find_keys_in_dict1_not_in_dict2({'a': 1, 'b': 2, 'c': 3}, {'b': 3}) == ['a', 'c']
    assert find_keys_in_dict1_not_in_dict2({}, {'a': 1}) is None
    assert find_keys_in_dict1_not_in_dict2({'a': 1}, {}) == ['a']


# 338. Тесты для функции `multiply_by_two`
def test_multiply_by_two():
    assert multiply_by_two([1, 2, 3]) == [2, 4, 6]
    assert multiply_by_two([0, -1, -2]) == [0, -2, -4]
    assert multiply_by_two([10, 100, 1000]) == [20, 200, 2000]
    assert multiply_by_two([]) is None
    assert multiply_by_two([1]) == [2]


# 339. Тесты для функции `subtract_lists`
def test_subtract_lists():
    assert subtract_lists([4, 9, 16], [2, 3, 4]) == [2, 6, 12]
    assert subtract_lists([4, 9, 16], [2, 0, 4]) == [2, 9, 12]
    assert subtract_lists([1, 2, 3], [0, 1, 1]) == [1, 1, 2]
    assert subtract_lists([], [1, 2, 3]) is None
    assert subtract_lists([1, 2, 3], []) is None


# 340. Тесты для функции `find_common_in_dicts`
def test_find_common_in_dicts():
    assert find_common_in_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == ['b']
    assert find_common_in_dicts({'a': 1, 'b': 2}, {'a': 1, 'b': 2}) == ['a', 'b']
    assert find_common_in_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 3}) == ['b']
    assert find_common_in_dicts({}, {'a': 1}) is None
    assert find_common_in_dicts({'a': 1}, {}) is None


# 341. Тесты для функции `sum_list_3`
def test_sum_list_3():
    assert sum_list_3([1, 2, 3]) == 6
    assert sum_list_3([]) is None
    assert sum_list_3([0]) == 0


# 342. Тесты для функции `find_divisible_by_3_not_9`
def test_find_divisible_by_3_not_9():
    assert find_divisible_by_3_not_9([3, 6, 9]) == [3, 6]
    assert find_divisible_by_3_not_9([9, 18, 27]) is None
    assert find_divisible_by_3_not_9([]) is None


# 343. Тесты для функции `find_divisible_by_5_or_7`
def test_find_divisible_by_5_or_7():
    assert find_divisible_by_5_or_7([5, 10, 7, 14, 21]) == [5, 10, 7, 14, 21]
    assert find_divisible_by_5_or_7([1, 2, 3]) is None
    assert find_divisible_by_5_or_7([]) is None


# 344. Тесты для функции `find_in_dicts`
def test_find_in_dicts():
    assert find_in_dicts({'a': 1, 'b': 2}, {'a': 3, 'c': 4}) == ['a']
    assert find_in_dicts({'a': 1}, {'b': 2}) is None
    assert find_in_dicts({}, {'a': 1}) is None


# 345. Тесты для функции `find_divisible_by_3_or_5`
def test_find_divisible_by_3_or_5():
    assert find_divisible_by_3_or_5([3, 5, 15, 30]) == [3, 5, 15, 30]
    assert find_divisible_by_3_or_5([1, 2, 4]) is None
    assert find_divisible_by_3_or_5([]) is None


# 346. Тесты для функции `find_divisible_by_4_not_6`
def test_find_divisible_by_4_not_6():
    assert find_divisible_by_4_not_6([4, 8, 12, 24]) == [4, 8]
    assert find_divisible_by_4_not_6([6, 12, 18]) is None
    assert find_divisible_by_4_not_6([]) is None


# 347. Тесты для функции `find_divisible_by_5_not_10`
def test_find_divisible_by_5_not_10():
    assert find_divisible_by_5_not_10([5, 15, 20]) == [5, 15]
    assert find_divisible_by_5_not_10([10, 20, 30]) is None
    assert find_divisible_by_5_not_10([]) is None


# 348. Тесты для функции `find_powers_of_list`
def test_find_powers_of_list():
    assert find_powers_of_list([2, 3, 4], 2) == [4, 9, 16]
    assert find_powers_of_list([1, 0, -1], 3) == [1, 0, -1]
    assert find_powers_of_list([], 2) is None


# 349. Тесты для функции `find_divisible_by_6_not_12`
def test_find_divisible_by_6_not_12():
    assert find_divisible_by_6_not_12([6, 18, 12, 24]) == [6, 18]
    assert find_divisible_by_6_not_12([12, 24, 36]) is None
    assert find_divisible_by_6_not_12([]) is None


# 350. Тесты для функции `find_divisible_by_4_or_5`
def test_find_divisible_by_4_or_5():
    assert find_divisible_by_4_or_5([4, 5, 8, 10]) == [4, 5, 8, 10]
    assert find_divisible_by_4_or_5([1, 2, 3]) is None
    assert find_divisible_by_4_or_5([]) is None


# 351. Тесты для функции `find_in_list_not_in_another`
def test_find_in_list_not_in_another():
    assert find_in_list_not_in_another([1, 2, 3], [2, 3, 4]) == [1]
    assert find_in_list_not_in_another([5, 6, 7], [5, 6, 7]) is None
    assert find_in_list_not_in_another([], [1, 2, 3]) is None


# 352. Тесты для функции `find_unique_keys_in_dict`
def test_find_unique_keys_in_dict():
    assert find_unique_keys_in_dict({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == ['a']
    assert find_unique_keys_in_dict({'a': 1}, {'a': 2}) is None
    assert find_unique_keys_in_dict({}, {'a': 1}) is None


# 353. Тесты для функции `multiply_lists`
def test_multiply_lists():
    assert multiply_lists([1, 2, 3], [4, 5, 6]) == [4, 10, 18]
    assert multiply_lists([1, 2], [3, 4, 5]) == [3, 8]
    assert multiply_lists([], [1, 2, 3]) is None


# 354. Тесты для функции `subtract_lists_v2`
def test_subtract_lists_v2():
    assert subtract_lists_v2([5, 6, 7], [1, 2, 3]) == [4, 4, 4]
    assert subtract_lists_v2([10, 20], [5, 5]) == [5, 15]
    assert subtract_lists_v2([], [1, 2]) is None


# 355. Тесты для функции `find_in_set_not_other`
def test_find_in_set_not_other():
    assert find_in_set_not_other({1, 2, 3}, {2, 3, 4}) == [1]
    assert find_in_set_not_other({5, 6, 7}, {5, 6, 7}) is None
    assert find_in_set_not_other(set(), {1, 2, 3}) is None


# 356. Тесты для функции `find_common_in_sets`
def test_find_common_in_sets():
    assert find_common_in_sets({1, 2, 3}, {2, 3, 4}) == [2, 3]
    assert find_common_in_sets({1, 2}, {3, 4}) is None
    assert find_common_in_sets(set(), {1, 2, 3}) is None


# 357. Тесты для функции `find_divisible_by_2_in_both_sets`
def test_find_divisible_by_2_in_both_sets():
    assert find_divisible_by_2_in_both_sets({2, 4, 6}, {4, 6, 8}) == [4, 6]
    assert find_divisible_by_2_in_both_sets({1, 3, 5}, {2, 4, 6}) is None
    assert find_divisible_by_2_in_both_sets(set(), {2, 4, 6}) is None


# 358. Тесты для функции `find_not_divisible_by_3_in_both_sets`
def test_find_not_divisible_by_3_in_both_sets():
    assert find_not_divisible_by_3_in_both_sets({1, 2, 4}, {2, 4, 5}) == [2, 4]
    assert find_not_divisible_by_3_in_both_sets({3, 6, 9}, {3, 6, 9}) is None
    assert find_not_divisible_by_3_in_both_sets(set(), {1, 2, 3}) is None


# 359. Тесты для функции `find_in_one_set_not_other_v2`
def test_find_in_one_set_not_other_v2():
    assert find_in_one_set_not_other_v2({1, 2, 3}, {2, 3, 4}) == [1]
    assert find_in_one_set_not_other_v2({5, 6, 7}, {5, 6, 7}) is None
    assert find_in_one_set_not_other_v2(set(), {1, 2, 3}) is None


# 360. Тесты для функции `find_divisible_by_2_or_5_in_both_sets`
def test_find_divisible_by_2_or_5_in_both_sets():
    assert find_divisible_by_2_or_5_in_both_sets({10, 15, 20}, {5, 10, 20}) == [10, 20]
    assert find_divisible_by_2_or_5_in_both_sets({1, 3, 7}, {2, 4, 8}) is None
    assert find_divisible_by_2_or_5_in_both_sets(set(), {1, 2, 3}) is None


# 361. Тесты для функции `find_not_divisible_by_2_or_3_in_both_sets`
def test_find_not_divisible_by_2_or_3_in_both_sets():
    assert find_not_divisible_by_2_or_3_in_both_sets({1, 2, 3, 5, 7}, {5, 7, 9, 11}) == [5, 7]
    assert find_not_divisible_by_2_or_3_in_both_sets({1, 3, 5, 7}, {2, 4, 6, 8}) is None
    assert find_not_divisible_by_2_or_3_in_both_sets(set(), set()) is None
    assert find_not_divisible_by_2_or_3_in_both_sets({10, 15, 25}, {10, 25, 35}) == [25]
    assert find_not_divisible_by_2_or_3_in_both_sets({5, 8, 11, 14}, {3, 6, 9, 12}) is None
    assert find_not_divisible_by_2_or_3_in_both_sets({1, 2, 4, 5, 10}, {5, 10, 11, 20}) == [5]
    assert find_not_divisible_by_2_or_3_in_both_sets({1, 2, 3}, {4, 5, 6}) is None
    assert find_not_divisible_by_2_or_3_in_both_sets({4, 5, 6}, {4, 5, 6}) == [5]
    assert find_not_divisible_by_2_or_3_in_both_sets({1, 9, 13}, {2, 9, 13}) == [13]


# 362. Тесты для функции `find_divisible_by_4_in_both_sets`
def test_find_divisible_by_4_in_both_sets():
    assert find_divisible_by_4_in_both_sets({4, 8, 12, 16}, {4, 8, 16, 20}) == [4, 8, 16]
    assert find_divisible_by_4_in_both_sets({1, 2, 3}, {5, 7, 11}) is None
    assert find_divisible_by_4_in_both_sets({32, 48, 64}, {32, 64, 96}) == [32, 64]
    assert find_divisible_by_4_in_both_sets({1, 4, 6, 8}, {2, 4, 8, 16}) == [4, 8]
    assert find_divisible_by_4_in_both_sets({16, 32, 48}, {24, 32, 48}) == [32, 48]
    assert find_divisible_by_4_in_both_sets({3, 6, 9}, {12, 15, 18}) is None
    assert find_divisible_by_4_in_both_sets({4, 5, 6}, {7, 8, 9}) is None
    assert find_divisible_by_4_in_both_sets({4, 8, 12}, {16, 20, 24}) is None
    assert find_divisible_by_4_in_both_sets({8, 12, 16}, {8, 16, 20}) == [8, 16]


# 363. Тесты для функции `find_in_set_not_other_v2`
def test_find_in_set_not_other_v2():
    assert find_in_set_not_other_v2({1, 2, 3}, {2, 3, 4}) == [1]
    assert find_in_set_not_other_v2({4, 5, 6}, {1, 2, 3}) == [4, 5, 6]
    assert find_in_set_not_other_v2(set(), {1, 2, 3}) is None
    assert find_in_set_not_other_v2({1, 2, 3}, {1, 2, 3}) is None
    assert find_in_set_not_other_v2({1, 3, 5}, {2, 4, 6}) == [1, 3, 5]
    assert find_in_set_not_other_v2({10, 20, 30}, {20, 40, 60}) == [10, 30]
    assert find_in_set_not_other_v2({7, 8, 9}, {7, 8, 9}) is None
    assert find_in_set_not_other_v2({5, 6, 7}, {7, 8, 9}) == [5, 6]
    assert find_in_set_not_other_v2({0, 1, 2}, {0, 2, 4}) == [1]


# 364. Тесты для функции `find_in_any_set`
def test_find_in_any_set():
    assert find_in_any_set({1, 2, 3}, {3, 4, 5}) == [1, 2, 3, 4, 5]
    assert find_in_any_set({1, 3, 5}, {2, 4, 6}) == [1, 2, 3, 4, 5, 6]
    assert find_in_any_set(set(), set()) is None
    assert find_in_any_set({1, 2, 3}, {4, 5, 6}) == [1, 2, 3, 4, 5, 6]
    assert find_in_any_set({7, 8, 9}, {10, 11, 12}) == [7, 8, 9, 10, 11, 12]
    assert find_in_any_set({1, 2}, {2, 3}) == [1, 2, 3]
    assert find_in_any_set({1, 3, 5}, {1, 3, 5}) == [1, 3, 5]
    assert find_in_any_set({1, 4, 7}, {2, 5, 8}) == [1, 2, 4, 5, 7, 8]
    assert find_in_any_set({1}, set()) == [1]


# 365. Тесты для функции `find_divisible_by_7_in_both_sets`
def test_find_divisible_by_7_in_both_sets():
    assert find_divisible_by_7_in_both_sets({7, 14, 21}, {14, 21, 28}) == [14, 21]
    assert find_divisible_by_7_in_both_sets({1, 2, 3}, {4, 5, 6}) is None
    assert find_divisible_by_7_in_both_sets({7, 14, 21, 28}, {7, 21, 35, 49}) == [7, 21]
    assert find_divisible_by_7_in_both_sets({7, 14, 28}, {14, 21, 35}) == [14]
    assert find_divisible_by_7_in_both_sets({14, 21, 28}, {14, 21, 28}) == [14, 21, 28]
    assert find_divisible_by_7_in_both_sets({7, 14}, {21, 28}) is None
    assert find_divisible_by_7_in_both_sets({2, 3, 5}, {7, 11, 13}) is None
    assert find_divisible_by_7_in_both_sets({14, 21, 35}, {14, 21, 35}) == [14, 21, 35]
    assert find_divisible_by_7_in_both_sets({1, 7, 14}, {7, 14, 21}) == [7, 14]


# 366. Тесты для функции `find_difference_in_sets`
def test_find_difference_in_sets():
    assert find_difference_in_sets({1, 2, 3}, {2, 3, 4}) == [1]
    assert find_difference_in_sets({4, 5, 6}, {1, 2, 3}) == [4, 5, 6]
    assert find_difference_in_sets(set(), {1, 2, 3}) is None
    assert find_difference_in_sets({1, 2, 3}, {1, 2, 3}) is None
    assert find_difference_in_sets({1, 3, 5}, {2, 4, 6}) == [1, 3, 5]
    assert find_difference_in_sets({10, 20, 30}, {20, 40, 60}) == [10, 30]
    assert find_difference_in_sets({7, 8, 9}, {7, 8, 9}) is None


# 367. Тесты для функции `find_not_divisible_by_2_in_both_sets`
def test_find_not_divisible_by_2_in_both_sets():
    assert find_not_divisible_by_2_in_both_sets({1, 2, 3, 5}, {3, 5, 7, 9}) == [3, 5]
    assert find_not_divisible_by_2_in_both_sets({2, 4, 6, 8}, {1, 3, 5, 7}) is None
    assert find_not_divisible_by_2_in_both_sets({1, 3, 5, 7}, {3, 5, 9, 11}) == [3, 5]
    assert find_not_divisible_by_2_in_both_sets({10, 15, 25}, {10, 25, 35}) == [25]
    assert find_not_divisible_by_2_in_both_sets(set(), {1, 3, 5}) is None
    assert find_not_divisible_by_2_in_both_sets({1, 3, 5}, {6, 8, 10}) is None
    assert find_not_divisible_by_2_in_both_sets({3, 5, 7}, {1, 3, 7}) == [3, 7]
    assert find_not_divisible_by_2_in_both_sets({5, 9, 13}, {5, 9, 17}) == [5, 9]
    assert find_not_divisible_by_2_in_both_sets({2, 4, 6}, {3, 5, 7}) is None


# 368. Тесты для функции `find_common_in_three_sets`
def test_find_common_in_three_sets():
    assert find_common_in_three_sets({1, 2, 3}, {2, 3, 4}, {3, 4, 5}) == [3]
    assert find_common_in_three_sets({1, 2, 3}, {3, 4, 5}, {5, 6, 7}) is None
    assert find_common_in_three_sets({10, 20, 30}, {20, 30, 40}, {30, 40, 50}) == [30]
    assert find_common_in_three_sets({5, 10, 15}, {15, 20, 25}, {15, 30, 45}) == [15]
    assert find_common_in_three_sets({1, 1, 1}, {2, 2, 2}, {3, 3, 3}) is None
    assert find_common_in_three_sets({4, 8, 12}, {8, 12, 16}, {12, 16, 20}) == [12]
    assert find_common_in_three_sets({1, 3, 5}, {1, 3, 5}, {1, 3, 5}) == [1, 3, 5]
    assert find_common_in_three_sets(set(), {1, 2, 3}, {1, 2, 3}) is None
    assert find_common_in_three_sets({2, 4, 6}, {4, 6, 8}, {6, 8, 10}) == [6]


# 369. Тесты для функции `find_difference_in_three_sets`
def test_find_difference_in_three_sets():
    assert find_difference_in_three_sets({1, 2, 3}, {2, 3, 4}, {3, 4, 5}) == [1]
    assert find_difference_in_three_sets({1, 2, 3}, {1, 2, 3}, {1, 2, 3}) is None
    assert find_difference_in_three_sets({5, 10, 15}, {10, 15, 20}, {15, 20, 25}) == [5]
    assert find_difference_in_three_sets({7, 14, 21}, {14, 21, 28}, {21, 28, 35}) == [7]
    assert find_difference_in_three_sets({2, 3, 4}, {4, 5, 6}, {6, 7, 8}) == [2, 3]
    assert find_difference_in_three_sets({10, 20, 30}, {20, 30, 40}, {30, 40, 50}) == [10]
    assert find_difference_in_three_sets({1, 3, 5}, {2, 4, 6}, {3, 6, 9}) == [1, 5]
    assert find_difference_in_three_sets({1, 2}, {2, 3}, {3, 4}) == [1]
    assert find_difference_in_three_sets(set(), {1, 2, 3}, {1, 2, 3}) is None


# 370. Тесты для функции `find_diff_in_sets_v2`
def test_find_diff_in_sets_v2():
    assert find_diff_in_sets_v2({1, 2, 3}, {2, 3, 4}) == [1]
    assert find_diff_in_sets_v2({4, 5, 6}, {1, 2, 3}) == [4, 5, 6]
    assert find_diff_in_sets_v2(set(), {1, 2, 3}) is None
    assert find_diff_in_sets_v2({1, 2, 3}, {1, 2, 3}) is None
    assert find_diff_in_sets_v2({1, 3, 5}, {2, 4, 6}) == [1, 3, 5]
    assert find_diff_in_sets_v2({10, 20, 30}, {20, 40, 60}) == [10, 30]
    assert find_diff_in_sets_v2({7, 8, 9}, {7, 8, 9}) is None
    assert find_diff_in_sets_v2({5, 6, 7}, {7, 8, 9}) == [5, 6]
    assert find_diff_in_sets_v2({0, 1, 2}, {0, 2, 4}) == [1]


# 371. Тесты для функции `find_not_divisible_by_5_in_both_sets`
def test_find_not_divisible_by_5_in_both_sets():
    assert find_not_divisible_by_5_in_both_sets({1, 2, 3, 10, 15}, {2, 3, 20, 25}) == [2, 3]
    assert find_not_divisible_by_5_in_both_sets({5, 10, 15}, {5, 10, 15}) is None
    assert find_not_divisible_by_5_in_both_sets({1, 2, 3}, {4, 5, 6}) is None
    assert find_not_divisible_by_5_in_both_sets({10, 20, 30}, {40, 50, 60}) is None
    assert find_not_divisible_by_5_in_both_sets({1, 3, 7, 11}, {7, 11, 13, 17}) == [7, 11]
    assert find_not_divisible_by_5_in_both_sets(set(), set()) is None
    assert find_not_divisible_by_5_in_both_sets({1, 2, 3}, {5, 10, 15}) is None
    assert find_not_divisible_by_5_in_both_sets({5, 6, 7}, {5, 6, 7}) == [6, 7]
    assert find_not_divisible_by_5_in_both_sets({4, 5, 6}, {4, 6, 7}) == [4, 6]


# 372. Тесты для функции `find_divisible_by_3_or_6_in_both_sets`
def test_find_divisible_by_3_or_6_in_both_sets():
    assert find_divisible_by_3_or_6_in_both_sets({3, 6, 9, 12}, {6, 9, 12, 18}) == [6, 9, 12]
    assert find_divisible_by_3_or_6_in_both_sets({1, 2, 3}, {4, 5, 6}) is None
    assert find_divisible_by_3_or_6_in_both_sets({2, 4, 6, 8}, {3, 5, 9, 12}) is None
    assert find_divisible_by_3_or_6_in_both_sets({2, 4, 5}, {1, 2, 5}) is None
    assert find_divisible_by_3_or_6_in_both_sets({6, 7, 8}, {9, 10, 11}) is None
    assert find_divisible_by_3_or_6_in_both_sets(set(), set()) is None
    assert find_divisible_by_3_or_6_in_both_sets({3, 6, 9}, {1, 2, 3}) == [3]
    assert find_divisible_by_3_or_6_in_both_sets({4, 5, 6}, {6, 7, 8}) == [6]
    assert find_divisible_by_3_or_6_in_both_sets({10, 20, 30}, {10, 30, 40}) == [30]


# 373. Тесты для функции `find_common_in_sets_divisible_by_3`
def test_find_common_in_sets_divisible_by_3():
    assert find_common_in_sets_divisible_by_3({3, 6, 9}, {3, 9, 12}) == [3, 9]
    assert find_common_in_sets_divisible_by_3({2, 4, 5}, {1, 2, 3}) is None
    assert find_common_in_sets_divisible_by_3({5, 6, 7}, {5, 6, 9}) == [6]
    assert find_common_in_sets_divisible_by_3({2, 4, 6}, {2, 4, 6}) == [6]
    assert find_common_in_sets_divisible_by_3({3, 6, 9}, {6, 9, 12}) == [6, 9]
    assert find_common_in_sets_divisible_by_3(set(), set()) is None
    assert find_common_in_sets_divisible_by_3({1, 2, 3}, {1, 2, 4}) is None
    assert find_common_in_sets_divisible_by_3({2, 5, 8}, {3, 5, 7}) is None
    assert find_common_in_sets_divisible_by_3({1, 2, 3}, {3, 6, 9}) == [3]


# 374. Тесты для функции `find_divisible_by_6_not_12_in_both_sets`
def test_find_divisible_by_6_not_12_in_both_sets():
    assert find_divisible_by_6_not_12_in_both_sets({6, 18, 24}, {6, 18, 30}) == [6, 18]
    assert find_divisible_by_6_not_12_in_both_sets({2, 4, 6}, {1, 2, 3}) is None
    assert find_divisible_by_6_not_12_in_both_sets({12, 18, 24}, {12, 18, 24}) == [18]
    assert find_divisible_by_6_not_12_in_both_sets({6, 12, 18}, {6, 18, 24}) == [6, 18]
    assert find_divisible_by_6_not_12_in_both_sets({1, 3, 5}, {6, 9, 12}) is None
    assert find_divisible_by_6_not_12_in_both_sets(set(), set()) is None
    assert find_divisible_by_6_not_12_in_both_sets({2, 4, 6}, {2, 4, 6}) == [6]
    assert find_divisible_by_6_not_12_in_both_sets({1, 2, 4}, {2, 4, 6}) is None
    assert find_divisible_by_6_not_12_in_both_sets({3, 6, 9}, {6, 9, 12}) == [6]


# 375. Тесты для функции `find_not_in_both_sets`
def test_find_not_in_both_sets():
    assert find_not_in_both_sets({1, 2, 3}, {3, 4, 5}) == [1, 2, 4, 5]
    assert find_not_in_both_sets({1, 2, 3}, {1, 2, 3}) is None
    assert find_not_in_both_sets({4, 5, 6}, {4, 6, 7}) == [5, 7]
    assert find_not_in_both_sets({2, 3, 4}, {1, 2, 3}) == [1, 4]
    assert find_not_in_both_sets({10, 20, 30}, {20, 30, 40}) == [10, 40]
    assert find_not_in_both_sets(set(), set()) is None
    assert find_not_in_both_sets({1, 2, 4}, {2, 3, 4}) == [1, 3]
    assert find_not_in_both_sets({2, 3, 5}, {3, 5, 7}) == [2, 7]
    assert find_not_in_both_sets({7, 8, 9}, {8, 9, 10}) == [7, 10]


# 376. Тесты для функции `find_difference_between_three_sets`
def test_find_difference_between_three_sets():
    assert find_difference_between_three_sets({1, 2, 3}, {2, 3, 4}, {3, 4, 5}) == [1]
    assert find_difference_between_three_sets({1, 2, 3}, {1, 2, 3}, {1, 2, 3}) is None
    assert find_difference_between_three_sets({5, 10, 15}, {10, 15, 20}, {15, 20, 25}) == [5]
    assert find_difference_between_three_sets({7, 14, 21}, {14, 21, 28}, {21, 28, 35}) == [7]
    assert find_difference_between_three_sets({2, 3, 4}, {4, 5, 6}, {6, 7, 8}) == [2, 3]
    assert find_difference_between_three_sets({10, 20, 30}, {20, 30, 40}, {30, 40, 50}) == [10]
    assert find_difference_between_three_sets({1, 3, 5}, {2, 4, 6}, {3, 6, 9}) == [1, 5]
    assert find_difference_between_three_sets({1, 2}, {2, 3}, {3, 4}) == [1]
    assert find_difference_between_three_sets(set(), {1, 2, 3}, {1, 2, 3}) is None


# 377. Тесты для функции `find_divisible_by_2_not_3_in_both_sets`
def test_find_divisible_by_2_not_3_in_both_sets():
    assert find_divisible_by_2_not_3_in_both_sets({2, 4, 6}, {2, 4, 8}) == [2, 4]
    assert find_divisible_by_2_not_3_in_both_sets({1, 3, 5}, {2, 4, 6}) is None
    assert find_divisible_by_2_not_3_in_both_sets({8, 10, 12}, {6, 8, 10}) == [8, 10]
    assert find_divisible_by_2_not_3_in_both_sets({4, 5, 6}, {1, 2, 4}) == [4]
    assert find_divisible_by_2_not_3_in_both_sets({1, 2, 3}, {4, 5, 6}) is None
    assert find_divisible_by_2_not_3_in_both_sets({2, 4, 6}, {3, 5, 7}) is None
    assert find_divisible_by_2_not_3_in_both_sets({2, 4, 6}, {4, 6, 8}) == [4]
    assert find_divisible_by_2_not_3_in_both_sets({1, 4, 5}, {2, 3, 4}) == [4]
    assert find_divisible_by_2_not_3_in_both_sets({8, 10, 12}, {14, 16, 18}) is None


# 378. Тесты для функции `find_common_not_divisible_by_4`
def test_find_common_not_divisible_by_4():
    assert find_common_not_divisible_by_4({1, 2, 3, 8, 12}, {2, 3, 12, 16}) == [2, 3]
    assert find_common_not_divisible_by_4({2, 4, 6}, {4, 6, 8}) == [6]
    assert find_common_not_divisible_by_4({1, 2, 3}, {4, 5, 6}) is None
    assert find_common_not_divisible_by_4({1, 3, 5}, {1, 3, 7}) == [1, 3]
    assert find_common_not_divisible_by_4({4, 8, 12}, {4, 12, 16}) is None
    assert find_common_not_divisible_by_4({3, 6, 9}, {6, 9, 12}) == [6, 9]
    assert find_common_not_divisible_by_4(set(), {1, 2, 3}) is None
    assert find_common_not_divisible_by_4({1, 2, 3}, {1, 2, 3}) == [1, 2, 3]
    assert find_common_not_divisible_by_4({5, 6, 7}, {6, 7, 8}) == [6, 7]


# 379. Тесты для функции `find_unique_in_sets`
def test_find_unique_in_sets():
    assert find_unique_in_sets({1, 2, 3}, {3, 4, 5}) == [1, 2, 4, 5]
    assert find_unique_in_sets({1, 2, 3}, {1, 2, 3}) is None
    assert find_unique_in_sets({4, 5, 6}, {4, 6, 7}) == [5, 7]
    assert find_unique_in_sets({2, 3, 4}, {1, 2, 3}) == [1, 4]
    assert find_unique_in_sets({10, 20, 30}, {20, 30, 40}) == [10, 40]
    assert find_unique_in_sets(set(), set()) is None
    assert find_unique_in_sets({1, 2, 4}, {2, 3, 4}) == [1, 3]
    assert find_unique_in_sets({2, 3, 5}, {3, 5, 7}) == [2, 7]
    assert find_unique_in_sets({7, 8, 9}, {8, 9, 10}) == [7, 10]


# 380. Тесты для функции `find_common_in_all_sets`
def test_find_common_in_all_sets():
    assert find_common_in_all_sets({1, 2, 3}, {2, 3, 4}, {3, 4, 5}) == [3]
    assert find_common_in_all_sets({1, 2, 3}, {3, 4, 5}, {5, 6, 7}) is None
    assert find_common_in_all_sets({10, 20, 30}, {20, 30, 40}, {30, 40, 50}) == [30]
    assert find_common_in_all_sets({5, 10, 15}, {15, 20, 25}, {15, 30, 45}) == [15]
    assert find_common_in_all_sets({1, 1, 1}, {2, 2, 2}, {3, 3, 3}) is None
    assert find_common_in_all_sets({4, 8, 12}, {8, 12, 16}, {12, 16, 20}) == [12]
    assert find_common_in_all_sets({1, 3, 5}, {1, 3, 5}, {1, 3, 5}) == [1, 3, 5]
    assert find_common_in_all_sets(set(), {1, 2, 3}, {1, 2, 3}) is None
    assert find_common_in_all_sets({2, 4, 6}, {4, 6, 8}, {6, 8, 10}) == [6]


# 381. Тесты для функции find_in_both_sets_not_divisible_by_3
def test_find_in_both_sets_not_divisible_by_3():
    assert find_in_both_sets_not_divisible_by_3({1, 2, 3, 6, 9}, {2, 3, 5, 6}) == [2]
    assert find_in_both_sets_not_divisible_by_3({1, 2, 4}, {3, 4, 5, 6}) == [4]
    assert find_in_both_sets_not_divisible_by_3({3, 6, 9}, {12, 15}) is None
    assert find_in_both_sets_not_divisible_by_3(set(), {1, 2, 4}) is None
    assert find_in_both_sets_not_divisible_by_3({1, 2, 3}, set()) is None
    assert find_in_both_sets_not_divisible_by_3({2, 4, 6}, {2, 8, 10}) == [2]
    assert find_in_both_sets_not_divisible_by_3({1, 7, 9, 10}, {3, 7, 10}) == [7, 10]
    assert find_in_both_sets_not_divisible_by_3({1, 5, 12}, {4, 5, 6, 12}) == [5]
    assert find_in_both_sets_not_divisible_by_3({8, 12, 15, 20}, {5, 8, 15, 25}) == [8]


# 382. Тесты для функции find_unique_in_one_set
def test_find_unique_in_one_set():
    assert find_unique_in_one_set({1, 2, 3}, {2, 3, 4}) == [1, 4]
    assert find_unique_in_one_set({1, 3}, {2, 4}) == [1, 2, 3, 4]
    assert find_unique_in_one_set({1, 2, 3}, {1, 2, 3}) is None
    assert find_unique_in_one_set(set(), {1, 2, 3}) == [1, 2, 3]
    assert find_unique_in_one_set({1, 2, 3}, set()) == [1, 2, 3]
    assert find_unique_in_one_set({1, 2, 3, 5}, {2, 3, 4, 5}) == [1, 4]
    assert find_unique_in_one_set({1, 6, 7}, {2, 3, 6}) == [1, 2, 3, 7]
    assert find_unique_in_one_set({9, 10}, {11, 12}) == [9, 10, 11, 12]
    assert find_unique_in_one_set({7, 8, 9}, {8, 10, 11}) == [7, 9, 10, 11]


# 383. Тесты для функции find_in_set_not_other_v3
def test_find_in_set_not_other_v3():
    assert find_in_set_not_other_v3({1, 2, 3}, {2, 3, 4}) == [1]
    assert find_in_set_not_other_v3({1, 3}, {2, 4}) == [1, 3]
    assert find_in_set_not_other_v3({1, 2, 3}, {1, 2, 3}) is None
    assert find_in_set_not_other_v3(set(), {1, 2, 3}) is None
    assert find_in_set_not_other_v3({1, 2, 3}, set()) == [1, 2, 3]
    assert find_in_set_not_other_v3({1, 2, 3, 5}, {2, 3, 4, 5}) == [1]
    assert find_in_set_not_other_v3({1, 6, 7}, {2, 3, 6}) == [1, 7]
    assert find_in_set_not_other_v3({9, 10}, {11, 12}) == [9, 10]
    assert find_in_set_not_other_v3({7, 8, 9}, {8, 10, 11}) == [7, 9]


# 384. Тесты для функции find_common_divisible_by_3
def test_find_common_divisible_by_3():
    assert find_common_divisible_by_3({1, 2, 3}, {2, 3, 4}) == [3]
    assert find_common_divisible_by_3({3, 6, 9}, {6, 12, 18}) == [6]
    assert find_common_divisible_by_3({3, 6, 9}, {3, 6, 9}) == [3, 6, 9]
    assert find_common_divisible_by_3({1, 2, 4}, {5, 7, 8}) is None
    assert find_common_divisible_by_3(set(), {3, 6, 9}) is None
    assert find_common_divisible_by_3({3, 6, 9}, set()) is None
    assert find_common_divisible_by_3({1, 3, 5, 9}, {9, 12, 15}) == [9]
    assert find_common_divisible_by_3({6, 12}, {3, 6, 9}) == [6]
    assert find_common_divisible_by_3({4, 8, 12}, {3, 9, 12}) == [12]


# 385. Тесты для функции find_in_one_set_not_other_v3
def test_find_in_one_set_not_other_v3():
    assert find_in_one_set_not_other_v3({1, 2, 3}, {2, 3, 4}) == [1, 4]
    assert find_in_one_set_not_other_v3({1, 3}, {2, 4}) == [1, 2, 3, 4]
    assert find_in_one_set_not_other_v3({1, 2, 3}, {1, 2, 3}) is None
    assert find_in_one_set_not_other_v3(set(), {1, 2, 3}) == [1, 2, 3]
    assert find_in_one_set_not_other_v3({1, 2, 3}, set()) == [1, 2, 3]
    assert find_in_one_set_not_other_v3({1, 2, 3, 5}, {2, 3, 4, 5}) == [1, 4]
    assert find_in_one_set_not_other_v3({1, 6, 7}, {2, 3, 6}) == [1, 2, 3, 7]
    assert find_in_one_set_not_other_v3({9, 10}, {11, 12}) == [9, 10, 11, 12]
    assert find_in_one_set_not_other_v3({7, 8, 9}, {8, 10, 11}) == [7, 9, 10, 11]


# 386. Тесты для функции find_divisible_by_2_not_4_in_both_sets
def test_find_divisible_by_2_not_4_in_both_sets():
    assert find_divisible_by_2_not_4_in_both_sets({1, 2, 4}, {2, 3, 4}) == [2]
    assert find_divisible_by_2_not_4_in_both_sets({2, 6, 10}, {4, 6, 10}) == [6, 10]
    assert find_divisible_by_2_not_4_in_both_sets({1, 3, 5}, {7, 9, 11}) is None
    assert find_divisible_by_2_not_4_in_both_sets({1, 2}, {2, 3}) == [2]
    assert find_divisible_by_2_not_4_in_both_sets(set(), {2, 4, 6}) is None
    assert find_divisible_by_2_not_4_in_both_sets({2, 4, 6}, set()) is None
    assert find_divisible_by_2_not_4_in_both_sets({2, 3, 8}, {2, 4, 8}) == [2]
    assert find_divisible_by_2_not_4_in_both_sets({1, 2, 6}, {2, 5, 6}) == [2, 6]
    assert find_divisible_by_2_not_4_in_both_sets({4, 8, 10}, {2, 4, 8}) is None


# 387. Тесты для функции find_in_both_sets_not_divisible_by_5
def test_find_in_both_sets_not_divisible_by_5():
    assert find_in_both_sets_not_divisible_by_5({1, 2, 5, 10}, {2, 3, 5}) == [2]
    assert find_in_both_sets_not_divisible_by_5({5, 15, 25}, {10, 20, 30}) is None
    assert find_in_both_sets_not_divisible_by_5({1, 2, 3, 4, 5}, {3, 5, 7, 9}) == [3]
    assert find_in_both_sets_not_divisible_by_5({5, 10, 15}, {2, 4, 6}) is None
    assert find_in_both_sets_not_divisible_by_5(set(), {1, 2, 3}) is None
    assert find_in_both_sets_not_divisible_by_5({1, 2, 4}, set()) is None
    assert find_in_both_sets_not_divisible_by_5({1, 2, 3, 7}, {2, 3, 7}) == [2, 3, 7]
    assert find_in_both_sets_not_divisible_by_5({1, 8, 12}, {4, 8, 12}) == [8, 12]
    assert find_in_both_sets_not_divisible_by_5({6, 7, 8}, {7, 8, 9}) == [7, 8]


# 388. Тесты для функции find_in_both_sets_divisible_by_3
def test_find_in_both_sets_divisible_by_3():
    assert find_in_both_sets_divisible_by_3({1, 2, 3}, {3, 4, 5}) == [3]
    assert find_in_both_sets_divisible_by_3({6, 9, 12}, {9, 12, 18}) == [9, 12]
    assert find_in_both_sets_divisible_by_3({3, 6, 9}, {3, 6, 9}) == [3, 6, 9]
    assert find_in_both_sets_divisible_by_3({1, 4, 5}, {7, 8, 10}) is None
    assert find_in_both_sets_divisible_by_3(set(), {1, 2, 3}) is None
    assert find_in_both_sets_divisible_by_3({1, 2, 3}, set()) is None
    assert find_in_both_sets_divisible_by_3({1, 3, 6, 9}, {3, 6, 9}) == [3, 6, 9]
    assert find_in_both_sets_divisible_by_3({4, 8, 12}, {6, 12, 18}) == [12]
    assert find_in_both_sets_divisible_by_3({2, 3, 5, 6}, {1, 2, 3, 6}) == [3, 6]


# 389. Тесты для функции find_unique_in_sets_v2
def test_find_unique_in_sets_v2():
    assert find_unique_in_sets_v2({1, 2, 3}, {3, 4, 5}) == [1, 2, 4, 5]
    assert find_unique_in_sets_v2({1, 3}, {2, 4}) == [1, 2, 3, 4]
    assert find_unique_in_sets_v2({1, 2, 3}, {1, 2, 3}) is None
    assert find_unique_in_sets_v2(set(), {1, 2, 3}) == [1, 2, 3]
    assert find_unique_in_sets_v2({1, 2, 3}, set()) == [1, 2, 3]
    assert find_unique_in_sets_v2({1, 2, 3, 5}, {2, 3, 4, 5}) == [1, 4]
    assert find_unique_in_sets_v2({1, 6, 7}, {2, 3, 6}) == [1, 2, 3, 7]
    assert find_unique_in_sets_v2({9, 10}, {11, 12}) == [9, 10, 11, 12]
    assert find_unique_in_sets_v2({7, 8, 9}, {8, 10, 11}) == [7, 9, 10, 11]


# 390. Тесты для функции find_in_first_set_not_second_divisible_by_7
def test_find_in_first_set_not_second_divisible_by_7():
    assert find_in_first_set_not_second_divisible_by_7({7, 14, 21}, {1, 2, 3}) == [7, 14, 21]
    assert find_in_first_set_not_second_divisible_by_7({7, 14}, {14, 28}) == [7]
    assert find_in_first_set_not_second_divisible_by_7({1, 2, 3}, {3, 7, 14}) is None
    assert find_in_first_set_not_second_divisible_by_7({7, 14, 28}, set()) == [7, 14, 28]
    assert find_in_first_set_not_second_divisible_by_7(set(), {1, 2, 3}) is None
    assert find_in_first_set_not_second_divisible_by_7({7, 49, 70}, {7, 14, 49}) == [70]
    assert find_in_first_set_not_second_divisible_by_7({1, 2, 7}, {3, 5, 9}) == [7]
    assert find_in_first_set_not_second_divisible_by_7({14, 21, 28}, {14, 28, 35}) == [21]
    assert find_in_first_set_not_second_divisible_by_7({7, 21, 35}, {35, 42, 49}) == [7, 21]


# 391. Тесты для функции find_divisible_by_6_not_12_in_both_sets_2
def test_find_divisible_by_6_not_12_in_both_sets_2():
    assert find_divisible_by_6_not_12_in_both_sets_2({6, 12, 18}, {6, 18, 30}) == [6, 18]
    assert find_divisible_by_6_not_12_in_both_sets_2({12, 24, 36}, {24, 36, 48}) is None
    assert find_divisible_by_6_not_12_in_both_sets_2({6, 12, 18}, {12, 24, 36}) is None
    assert find_divisible_by_6_not_12_in_both_sets_2(set(), {6, 18, 24}) is None
    assert find_divisible_by_6_not_12_in_both_sets_2({6, 18, 24}, set()) is None
    assert find_divisible_by_6_not_12_in_both_sets_2({6, 12, 18}, {6, 12, 18}) == [6, 18]
    assert find_divisible_by_6_not_12_in_both_sets_2({18, 24, 30}, {6, 18, 30}) == [18, 30]
    assert find_divisible_by_6_not_12_in_both_sets_2({6, 30, 48}, {12, 18, 30}) == [30]
    assert find_divisible_by_6_not_12_in_both_sets_2({1, 2, 3, 6}, {6, 9, 12, 18}) == [6]


# 392. Тесты для функции find_in_one_set_not_other_divisible_by_5
def test_find_in_one_set_not_other_divisible_by_5():
    assert find_in_one_set_not_other_divisible_by_5({5, 10, 15}, {10, 20, 30}) == [5, 15, 20, 30]
    assert find_in_one_set_not_other_divisible_by_5({1, 2, 5}, {5, 10, 15}) == [10, 15]
    assert find_in_one_set_not_other_divisible_by_5({5, 10}, {5, 10}) is None
    assert find_in_one_set_not_other_divisible_by_5(set(), {5, 10, 15}) == [5, 10, 15]
    assert find_in_one_set_not_other_divisible_by_5({5, 10, 15}, set()) == [5, 10, 15]
    assert find_in_one_set_not_other_divisible_by_5({1, 5, 9}, {2, 5, 10}) == [10]
    assert find_in_one_set_not_other_divisible_by_5({6, 7, 8}, {5, 10, 15}) == [5, 10, 15]
    assert find_in_one_set_not_other_divisible_by_5({5, 12, 20}, {20, 30, 40}) == [5, 30, 40]
    assert find_in_one_set_not_other_divisible_by_5({3, 6, 9}, {3, 6, 9}) is None


# 393. Тесты для функции find_common_in_sets_divisible_by_4
def test_find_common_in_sets_divisible_by_4():
    assert find_common_in_sets_divisible_by_4({4, 8, 12}, {8, 12, 16}) == [8, 12]
    assert find_common_in_sets_divisible_by_4({16, 32, 48}, {32, 48, 64}) == [32, 48]
    assert find_common_in_sets_divisible_by_4({4, 8, 12}, {4, 8, 12}) == [4, 8, 12]
    assert find_common_in_sets_divisible_by_4({2, 6, 10}, {3, 6, 9}) is None
    assert find_common_in_sets_divisible_by_4(set(), {4, 8, 12}) is None
    assert find_common_in_sets_divisible_by_4({4, 8, 12}, set()) is None
    assert find_common_in_sets_divisible_by_4({8, 12, 24}, {12, 24, 36}) == [12, 24]
    assert find_common_in_sets_divisible_by_4({16, 32, 64}, {8, 16, 32}) == [16, 32]
    assert find_common_in_sets_divisible_by_4({1, 2, 4}, {2, 4, 8}) == [4]


# 394. Тесты для функции find_divisible_by_3_in_both_sets
def test_find_divisible_by_3_in_both_sets():
    assert find_divisible_by_3_in_both_sets({3, 6, 9}, {6, 9, 12}) == [6, 9]
    assert find_divisible_by_3_in_both_sets({3, 9, 15}, {3, 9, 15}) == [3, 9, 15]
    assert find_divisible_by_3_in_both_sets({6, 12, 18}, {18, 24, 30}) == [18]
    assert find_divisible_by_3_in_both_sets({1, 2, 3}, {4, 5, 6}) is None
    assert find_divisible_by_3_in_both_sets(set(), {3, 6, 9}) is None
    assert find_divisible_by_3_in_both_sets({3, 6, 9}, set()) is None
    assert find_divisible_by_3_in_both_sets({3, 12, 15}, {12, 15, 18}) == [12, 15]
    assert find_divisible_by_3_in_both_sets({6, 9, 12}, {9, 12, 15}) == [9, 12]
    assert find_divisible_by_3_in_both_sets({6, 9, 18}, {6, 12, 18}) == [6, 18]


# 395. Тесты для функции find_difference_in_sets_v2
def test_find_difference_in_sets_v2():
    assert find_difference_in_sets_v2({1, 2, 3}, {2, 3, 4}) == [1, 4]
    assert find_difference_in_sets_v2({1, 3}, {2, 4}) == [1, 2, 3, 4]
    assert find_difference_in_sets_v2({1, 2, 3}, {1, 2, 3}) is None
    assert find_difference_in_sets_v2(set(), {1, 2, 3}) == [1, 2, 3]
    assert find_difference_in_sets_v2({1, 2, 3}, set()) == [1, 2, 3]
    assert find_difference_in_sets_v2({1, 2, 3, 5}, {2, 3, 4, 5}) == [1, 4]
    assert find_difference_in_sets_v2({1, 6, 7}, {2, 3, 6}) == [1, 2, 3, 7]
    assert find_difference_in_sets_v2({9, 10}, {11, 12}) == [9, 10, 11, 12]
    assert find_difference_in_sets_v2({7, 8, 9}, {8, 10, 11}) == [7, 9, 10, 11]


# 396. Тесты для функции find_divisible_by_4_in_both_sets_2
def test_find_divisible_by_4_in_both_sets_2():
    assert find_divisible_by_4_in_both_sets_2({4, 8, 12}, {8, 12, 16}) == [8, 12]
    assert find_divisible_by_4_in_both_sets_2({16, 32, 48}, {32, 48, 64}) == [32, 48]
    assert find_divisible_by_4_in_both_sets_2({4, 8, 12}, {4, 8, 12}) == [4, 8, 12]
    assert find_divisible_by_4_in_both_sets_2({2, 6, 10}, {3, 6, 9}) is None
    assert find_divisible_by_4_in_both_sets_2(set(), {4, 8, 12}) is None
    assert find_divisible_by_4_in_both_sets_2({4, 8, 12}, set()) is None
    assert find_divisible_by_4_in_both_sets_2({8, 12, 24}, {12, 24, 36}) == [12, 24]
    assert find_divisible_by_4_in_both_sets_2({16, 32, 64}, {8, 16, 32}) == [16, 32]
    assert find_divisible_by_4_in_both_sets_2({1, 2, 4}, {2, 4, 8}) == [4]


# 397. Тесты для функции find_unique_not_divisible_by_3
def test_find_unique_not_divisible_by_3():
    assert find_unique_not_divisible_by_3({1, 2, 3, 4}, {4, 5, 6, 7}) == [1, 2, 5, 7]
    assert find_unique_not_divisible_by_3({9, 18, 27}, {3, 6, 9}) is None
    assert find_unique_not_divisible_by_3({7, 10, 14}, {1, 7, 10}) == [1, 14]
    assert find_unique_not_divisible_by_3(set(), {3, 6, 9}) is None
    assert find_unique_not_divisible_by_3({3, 6, 9}, set()) is None
    assert find_unique_not_divisible_by_3({1, 4, 7}, {2, 5, 8}) == [1, 2, 4, 5, 7, 8]
    assert find_unique_not_divisible_by_3({10, 20, 30}, {30, 40, 50}) == [10, 20, 40, 50]
    assert find_unique_not_divisible_by_3({2, 3, 4}, {5, 6, 7}) == [2, 4, 5, 7]
    assert find_unique_not_divisible_by_3({15, 21, 27}, {3, 9, 21}) is None


# 398. Тесты для функции find_divisible_by_5_in_both_sets
def test_find_divisible_by_5_in_both_sets():
    assert find_divisible_by_5_in_both_sets({5, 10, 15}, {10, 15, 20}) == [10, 15]
    assert find_divisible_by_5_in_both_sets({25, 30, 35}, {35, 40, 45}) == [35]
    assert find_divisible_by_5_in_both_sets({50, 55}, {55, 60}) == [55]
    assert find_divisible_by_5_in_both_sets({1, 2, 3}, {4, 5, 6}) is None
    assert find_divisible_by_5_in_both_sets(set(), {5, 10, 15}) is None
    assert find_divisible_by_5_in_both_sets({5, 10, 15}, set()) is None
    assert find_divisible_by_5_in_both_sets({20, 25, 30}, {25, 35, 40}) == [25]
    assert find_divisible_by_5_in_both_sets({10, 20, 30}, {10, 40, 50}) == [10]
    assert find_divisible_by_5_in_both_sets({15, 45}, {5, 15, 25}) == [15]


# 399. Тесты для функции find_in_both_sets_not_divisible_by_2
def test_find_in_both_sets_not_divisible_by_2():
    assert find_in_both_sets_not_divisible_by_2({1, 3, 5}, {3, 5, 7}) == [3, 5]
    assert find_in_both_sets_not_divisible_by_2({11, 13, 15}, {13, 15, 17}) == [13, 15]
    assert find_in_both_sets_not_divisible_by_2({19, 21, 23}, {21, 23, 25}) == [21, 23]
    assert find_in_both_sets_not_divisible_by_2({2, 4, 6}, {8, 10, 12}) is None
    assert find_in_both_sets_not_divisible_by_2(set(), {1, 3, 5}) is None
    assert find_in_both_sets_not_divisible_by_2({1, 3, 5}, set()) is None
    assert find_in_both_sets_not_divisible_by_2({7, 9, 11}, {11, 13, 15}) == [11]
    assert find_in_both_sets_not_divisible_by_2({5, 7, 9}, {7, 9, 11}) == [7, 9]
    assert find_in_both_sets_not_divisible_by_2({3, 6, 9}, {3, 9, 12}) == [3, 9]


# 400. Тесты для функции find_difference_between_sets
def test_find_difference_between_sets():
    assert find_difference_between_sets({1, 2, 3}, {2, 3, 4}) == [1]
    assert find_difference_between_sets({5, 6, 7}, {6, 8, 9}) == [5, 7]
    assert find_difference_between_sets({1, 2, 3}, {1, 2, 3}) is None
    assert find_difference_between_sets(set(), {1, 2, 3}) is None
    assert find_difference_between_sets({1, 2, 3}, set()) == [1, 2, 3]
    assert find_difference_between_sets({7, 8, 9}, {8, 9, 10}) == [7]
    assert find_difference_between_sets({3, 6, 9}, {6, 9, 12}) == [3]
    assert find_difference_between_sets({15, 18, 21}, {18, 21, 24}) == [15]
    assert find_difference_between_sets({2, 4, 6}, {4, 6, 8}) == [2]


# 401. Тесты для функции find_unique_elements_in_sets
def test_find_unique_elements_in_sets():
    assert find_unique_elements_in_sets({1, 2, 3}, {3, 4, 5}) == [1, 2, 4, 5]
    assert find_unique_elements_in_sets({1, 2, 3}, {1, 2, 3}) is None
    assert find_unique_elements_in_sets({1}, {2}) == [1, 2]
    assert find_unique_elements_in_sets(set(), {1, 2, 3}) == [1, 2, 3]
    assert find_unique_elements_in_sets({1, 2, 3}, set()) == [1, 2, 3]
    assert find_unique_elements_in_sets(set(), set()) is None


# 402. Тесты для функции find_divisible_by_2_in_both_sets_2
def test_find_divisible_by_2_in_both_sets_2():
    assert find_divisible_by_2_in_both_sets_2({2, 4, 6}, {4, 6, 8}) == [4, 6]
    assert find_divisible_by_2_in_both_sets_2({1, 2, 3}, {4, 5, 6}) is None
    assert find_divisible_by_2_in_both_sets_2({1, 3, 5}, {7, 9, 11}) is None
    assert find_divisible_by_2_in_both_sets_2({2, 4, 6, 8}, {4, 8, 10}) == [4, 8]
    assert find_divisible_by_2_in_both_sets_2({2, 4, 6}, {1, 3, 5}) is None
    assert find_divisible_by_2_in_both_sets_2({2}, {2}) == [2]


# 403. Тесты для функции find_in_first_set_not_second
def test_find_in_first_set_not_second():
    assert find_in_first_set_not_second({1, 2, 3}, {3, 4, 5}) == [1, 2]
    assert find_in_first_set_not_second({1, 2, 3}, {1, 2, 3}) is None
    assert find_in_first_set_not_second({1}, {2}) == [1]
    assert find_in_first_set_not_second(set(), {1, 2, 3}) is None
    assert find_in_first_set_not_second({1, 2, 3}, set()) == [1, 2, 3]
    assert find_in_first_set_not_second({1, 2, 3}, {2}) == [1, 3]


# 404. Тесты для функции find_divisible_by_5_in_one_set
def test_find_divisible_by_5_in_one_set():
    assert find_divisible_by_5_in_one_set({5, 10, 15}, {10, 20, 30}) == [5, 15]
    assert find_divisible_by_5_in_one_set({5, 10, 15}, {5, 10, 15}) is None
    assert find_divisible_by_5_in_one_set({1, 2, 3}, {4, 5, 6}) is None
    assert find_divisible_by_5_in_one_set({10, 20, 30}, {5, 15, 25}) == [10, 20, 30]
    assert find_divisible_by_5_in_one_set({5, 10, 15}, {2, 4, 6}) == [5, 10, 15]
    assert find_divisible_by_5_in_one_set({1, 2, 3}, {3, 4, 5}) is None


# 405. Тесты для функции is_stack_empty
def test_is_stack_empty():
    assert is_stack_empty([]) is True
    assert is_stack_empty([1, 2, 3]) is False
    assert is_stack_empty([0]) is False
    assert is_stack_empty(['a', 'b']) is False
    assert is_stack_empty([None]) is False
    assert is_stack_empty([False]) is False


# 406. Тесты для функции fill_stack_until_limit
def test_fill_stack_until_limit():
    assert fill_stack_until_limit([], 3) == [1, 2, 3]
    assert fill_stack_until_limit([1, 2], 4) == [1, 2, 3, 4]
    assert fill_stack_until_limit([1], 1) == [1]
    assert fill_stack_until_limit([], 0) == []
    assert fill_stack_until_limit([1, 2, 3], 2) == [1, 2, 3]
    assert fill_stack_until_limit([], 5) == [1, 2, 3, 4, 5]


# 407. Тесты для функции fill_stack_up_to_n
def test_fill_stack_up_to_n():
    assert fill_stack_up_to_n([], 3) == [1, 2, 3]
    assert fill_stack_up_to_n([1, 2], 4) == [1, 2, 1, 2, 3, 4]
    assert fill_stack_up_to_n([1], 1) == [1, 1]
    assert fill_stack_up_to_n([], 0) == []
    assert fill_stack_up_to_n([1, 2, 3], 2) == [1, 2, 3, 1, 2]
    assert fill_stack_up_to_n([], 5) == [1, 2, 3, 4, 5]


# 408. Тесты для функции is_stack_palindrome
def test_is_stack_palindrome():
    assert is_stack_palindrome([1, 2, 1]) is True
    assert is_stack_palindrome([1, 2, 2, 1]) is True
    assert is_stack_palindrome([1, 2, 3]) is False
    assert is_stack_palindrome([1]) is True
    assert is_stack_palindrome([]) is True
    assert is_stack_palindrome([1, 2, 3, 2, 1]) is True


# 409. Тесты для функции pop_until_greater_than_x
def test_pop_until_greater_than_x():
    assert pop_until_greater_than_x([1, 2, 3, 4, 5], 3) == [5]
    assert pop_until_greater_than_x([5, 4, 3, 2, 1], 3) == [1, 2, 3, 4]
    assert pop_until_greater_than_x([1, 2, 3], 5) == [3, 2, 1]
    assert pop_until_greater_than_x([], 3) is None
    assert pop_until_greater_than_x([1, 2, 3], 0) == [3]
    assert pop_until_greater_than_x([5, 6, 7], 4) == [7]


# 410. Тесты для функции pop_elements_less_than_y
def test_pop_elements_less_than_y():
    assert pop_elements_less_than_y([1, 2, 3, 4, 5], 3) == [2, 1]
    assert pop_elements_less_than_y([5, 4, 3, 2, 1], 3) == [1, 2]
    assert pop_elements_less_than_y([1, 2, 3], 5) == [3, 2, 1]
    assert pop_elements_less_than_y([], 3) is None
    assert pop_elements_less_than_y([1, 2, 3], 0) is None
    assert pop_elements_less_than_y([5, 6, 7], 4) is None


# 411. Тесты для функции remove_odds_from_stack
def test_remove_odds_from_stack():
    assert remove_odds_from_stack([1, 2, 3, 4, 5]) == [4, 2]
    assert remove_odds_from_stack([1, 3, 5]) is None
    assert remove_odds_from_stack([2, 4, 6]) == [6, 4, 2]
    assert remove_odds_from_stack([]) is None
    assert remove_odds_from_stack([1, 2, 3]) == [2]
    assert remove_odds_from_stack([5, 4, 3, 2, 1]) == [2, 4]


# 412. Тесты для функции pop_until_sum_exceeds_x
def test_pop_until_sum_exceeds_x():
    assert pop_until_sum_exceeds_x([1, 2, 3, 4, 5], 10) == [5, 4, 3]
    assert pop_until_sum_exceeds_x([5, 4, 3, 2, 1], 7) == [1, 2, 3, 4]
    assert pop_until_sum_exceeds_x([], 3) is None
    assert pop_until_sum_exceeds_x([1, 2, 3], 1) == [3]
    assert pop_until_sum_exceeds_x([5, 6, 7], 4) == [7]
    assert pop_until_sum_exceeds_x([1, 2, 3], 5) == [3, 2, 1]


# 413. Тесты для функции pop_elements_divisible_by_3
def test_pop_elements_divisible_by_3():
    assert pop_elements_divisible_by_3([1, 2, 3, 4, 5, 6, 9]) == [9, 6, 3]
    assert pop_elements_divisible_by_3([1, 2, 4, 5]) is None
    assert pop_elements_divisible_by_3([3, 6, 9]) == [9, 6, 3]
    assert pop_elements_divisible_by_3([]) is None
    assert pop_elements_divisible_by_3([3]) == [3]
    assert pop_elements_divisible_by_3([1, 2, 3]) == [3]


# 414. Тесты для функции pop_min_element
def test_pop_min_element():
    assert pop_min_element([1, 2, 3, 4, 5]) == 1
    assert pop_min_element([5, 4, 3, 2, 1]) == 1
    assert pop_min_element([]) is None
    assert pop_min_element([1]) == 1
    assert pop_min_element([5, 3, 9, 7]) == 3
    assert pop_min_element([2, 2, 2, 2]) == 2


# 415. Тесты для функции double_stack_values
def test_double_stack_values():
    assert double_stack_values([1, 2, 3]) == [6, 4, 2]
    assert double_stack_values([0, 1, 2]) == [4, 2, 0]
    assert double_stack_values([]) == []
    assert double_stack_values([2, 4, 6]) == [12, 8, 4]
    assert double_stack_values([5, 5, 5]) == [10, 10, 10]
    assert double_stack_values([-1, -2, -3]) == [-6, -4, -2]


# 416. Тесты для функции pop_until_even
def test_pop_until_even():
    assert pop_until_even([1, 3, 5, 2, 7]) == [7, 2]
    assert pop_until_even([2, 4, 6, 1]) == [1, 6]
    assert pop_until_even([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert pop_until_even([]) is None
    assert pop_until_even([2, 4, 6, 8]) == [8]
    assert pop_until_even([3, 3, 3, 3]) == [3, 3, 3, 3]


# 417. Тесты для функции pop_prime_numbers
def test_pop_prime_numbers():
    assert pop_prime_numbers([1, 2, 3, 4, 5, 6, 7]) == [7, 5, 3, 2]
    assert pop_prime_numbers([1, 1, 1, 1]) is None
    assert pop_prime_numbers([2, 3, 5, 7]) == [7, 5, 3, 2]
    assert pop_prime_numbers([]) is None
    assert pop_prime_numbers([4, 6, 8, 9]) is None
    assert pop_prime_numbers([11, 13, 17]) == [17, 13, 11]


# 418. Тесты для функции pop_until_divisible_by_4
def test_pop_until_divisible_by_4():
    assert pop_until_divisible_by_4([1, 2, 3, 4, 5]) == [5, 4]
    assert pop_until_divisible_by_4([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert pop_until_divisible_by_4([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert pop_until_divisible_by_4([]) is None
    assert pop_until_divisible_by_4([2, 2, 2, 4]) == [4]
    assert pop_until_divisible_by_4([4]) == [4]


# 419. Тесты для функции remove_non_divisible_by_2
def test_remove_non_divisible_by_2():
    assert remove_non_divisible_by_2([1, 2, 3, 4, 5]) == [4, 2]
    assert remove_non_divisible_by_2([1, 3, 5]) is None
    assert remove_non_divisible_by_2([2, 4, 6]) == [6, 4, 2]
    assert remove_non_divisible_by_2([]) is None
    assert remove_non_divisible_by_2([1, 2, 3]) == [2]
    assert remove_non_divisible_by_2([5, 4, 3, 2, 1]) == [2, 4]


# 420. Тесты для функции remove_even_from_stack
def test_remove_even_from_stack():
    assert remove_even_from_stack([1, 2, 3, 4, 5]) == [5, 3, 1]
    assert remove_even_from_stack([2, 4, 6, 8]) is None
    assert remove_even_from_stack([1, 3, 5, 7]) == [7, 5, 3, 1]
    assert remove_even_from_stack([]) is None
    assert remove_even_from_stack([1]) == [1]
    assert remove_even_from_stack([4, 3, 2, 1]) == [1, 3]


# 421. Тесты для функции `pop_elements_greater_than_x`:
def test_pop_elements_greater_than_x():
    assert pop_elements_greater_than_x([1, 3, 5, 7, 9], 4) == [9, 7, 5]
    assert pop_elements_greater_than_x([2, 4, 6, 8], 10) is None
    assert pop_elements_greater_than_x([10, 20, 30], 15) == [30, 20]
    assert pop_elements_greater_than_x([], 5) is None
    assert pop_elements_greater_than_x([-5, -2, -1, 0], -3) == [0, -1, -2]
    assert pop_elements_greater_than_x([5, 5, 5, 5, 5], 5) is None
    assert pop_elements_greater_than_x([1, 2, 3, 4, 5], 0) == [5, 4, 3, 2, 1]
    assert pop_elements_greater_than_x([1, 2, 3, 4, 5], 5) is None
    assert pop_elements_greater_than_x([100], 10) == [100]


# 422. Тесты для функции `find_even_in_stack`:
def test_find_even_in_stack():
    assert find_even_in_stack([1, 2, 3, 4, 5, 6]) == [6, 4, 2]
    assert find_even_in_stack([1, 3, 5, 7]) is None
    assert find_even_in_stack([0, 2, 4, 6, 8]) == [8, 6, 4, 2, 0]
    assert find_even_in_stack([-2, -4, -6, -8]) == [-8, -6, -4, -2]
    assert find_even_in_stack([1]) is None
    assert find_even_in_stack([2]) == [2]
    assert find_even_in_stack([]) is None
    assert find_even_in_stack([1, 3, 5, 7, 10]) == [10]
    assert find_even_in_stack([2, 2, 2, 2]) == [2, 2, 2, 2]


# 423. Тесты для функции `remove_divisible_by_5_from_stack`:
def test_remove_divisible_by_5_from_stack():
    assert remove_divisible_by_5_from_stack([1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [1]
    assert remove_divisible_by_5_from_stack([5, 10, 15, 20, 25]) is None
    assert remove_divisible_by_5_from_stack([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert remove_divisible_by_5_from_stack([0, 5, 10]) is None
    assert remove_divisible_by_5_from_stack([1, 2, 3, 6, 7, 11]) == [11, 7, 6, 3, 2, 1]
    assert remove_divisible_by_5_from_stack([]) is None
    assert remove_divisible_by_5_from_stack([1, 2, 3, 4, 6]) == [6, 4, 3, 2, 1]
    assert remove_divisible_by_5_from_stack([25]) is None
    assert remove_divisible_by_5_from_stack([1, 10, 100]) == [1]


# 424. Тесты для функции `remove_max_from_stack`:
def test_remove_max_from_stack():
    assert remove_max_from_stack([1, 2, 3, 4, 5]) == 5
    assert remove_max_from_stack([5, 4, 3, 2, 1]) == 5
    assert remove_max_from_stack([1]) == 1
    assert remove_max_from_stack([-5, -10, -1, -3]) == -1
    assert remove_max_from_stack([100, 200, 300, 400]) == 400
    assert remove_max_from_stack([0]) == 0
    assert remove_max_from_stack([3, 3, 3, 3]) == 3
    assert remove_max_from_stack([10, 20, 30, 40, 50]) == 50
    assert remove_max_from_stack([]) is None


# 425. Тесты для функции `pop_elements_not_divisible_by_3`:
def test_pop_elements_not_divisible_by_3():
    assert pop_elements_not_divisible_by_3([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [8, 7, 5, 4, 2, 1]
    assert pop_elements_not_divisible_by_3([3, 6, 9]) is None
    assert pop_elements_not_divisible_by_3([1, 4, 7, 10]) == [10, 7, 4, 1]
    assert pop_elements_not_divisible_by_3([3, 3, 3, 3]) is None
    assert pop_elements_not_divisible_by_3([10, 11, 12, 13, 14, 15]) == [14, 13, 11, 10]
    assert pop_elements_not_divisible_by_3([3]) is None
    assert pop_elements_not_divisible_by_3([1]) == [1]
    assert pop_elements_not_divisible_by_3([]) is None
    assert pop_elements_not_divisible_by_3([9, 18, 27, 36, 45]) is None


# 426. Тесты для функции `pop_until_sum_exceeds`:
def test_pop_until_sum_exceeds():
    assert pop_until_sum_exceeds([1, 2, 3, 4, 5], 7) == [5, 4]
    assert pop_until_sum_exceeds([5, 5, 5, 5, 5], 15) == [5, 5, 5, 5]
    assert pop_until_sum_exceeds([10, 20, 30], 25) == [30]
    assert pop_until_sum_exceeds([], 5) is None
    assert pop_until_sum_exceeds([1, 1, 1, 1, 1], 0) == [1]
    assert pop_until_sum_exceeds([3, 6, 9], 15) == [9, 6, 3]
    assert pop_until_sum_exceeds([10, 10, 10], 5) == [10]
    assert pop_until_sum_exceeds([5], 10) == [5]
    assert pop_until_sum_exceeds([3, 3, 3], 7) == [3, 3, 3]


# 427. Тесты для функции `pop_elements_less_than_average`:
def test_pop_elements_less_than_average():
    assert pop_elements_less_than_average([1, 2, 3, 4, 5]) == [2, 1]
    assert pop_elements_less_than_average([5, 5, 5, 5]) is None
    assert pop_elements_less_than_average([1, 3, 5, 7]) == [3, 1]
    assert pop_elements_less_than_average([10, 20, 30, 40, 50]) == [20, 10]
    assert pop_elements_less_than_average([]) is None
    assert pop_elements_less_than_average([1]) is None
    assert pop_elements_less_than_average([2, 4, 6, 8]) == [4, 2]
    assert pop_elements_less_than_average([-10, -20, -30]) == [-30]
    assert pop_elements_less_than_average([1, 2, 3, 4, 5, 5, 5, 5]) == [3, 2, 1]


# 428. Тесты для функции `pop_unique_elements`:
def test_pop_unique_elements():
    assert pop_unique_elements([1, 1, 2, 2, 3]) == [3]
    assert pop_unique_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert pop_unique_elements([1, 1, 2, 2, 3, 3, 4, 4]) is None
    assert pop_unique_elements([5]) == [5]
    assert pop_unique_elements([]) is None
    assert pop_unique_elements([2, 2, 2, 2]) is None
    assert pop_unique_elements([3, 1, 4, 1, 5, 9]) == [9, 5, 4, 3]
    assert pop_unique_elements([1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8]) == [8, 6, 3, 1]
    assert pop_unique_elements([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]) == [6]


# 429. Тесты для функции `pop_elements_divisible_by_5`:
def test_pop_elements_divisible_by_5():
    assert pop_elements_divisible_by_5([5, 10, 15, 20, 25]) == [25, 20, 15, 10, 5]
    assert pop_elements_divisible_by_5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 5]
    assert pop_elements_divisible_by_5([1, 2, 3, 4, 6, 7, 8, 9]) is None
    assert pop_elements_divisible_by_5([0, 5, 10, 15]) == [15, 10, 5, 0]
    assert pop_elements_divisible_by_5([1, 2, 3, 4]) is None
    assert pop_elements_divisible_by_5([5]) == [5]
    assert pop_elements_divisible_by_5([25, 30, 35, 40, 45]) == [45, 40, 35, 30, 25]
    assert pop_elements_divisible_by_5([10, 20, 30, 40, 50]) == [50, 40, 30, 20, 10]
    assert pop_elements_divisible_by_5([12, 17, 22, 27]) is None


# 430. Тесты для функции `pop_elements_greater_than_x_reverse`:
def test_pop_elements_greater_than_x_reverse():
    assert pop_elements_greater_than_x_reverse([1, 2, 3, 4, 5], 3) == [4, 5]
    assert pop_elements_greater_than_x_reverse([10, 20, 30, 40, 50], 25) == [30, 40, 50]
    assert pop_elements_greater_than_x_reverse([5, 5, 5, 5], 5) is None
    assert pop_elements_greater_than_x_reverse([1, 2, 3, 4, 5, 6], 3) == [4, 5, 6]
    assert pop_elements_greater_than_x_reverse([1], 0) == [1]
    assert pop_elements_greater_than_x_reverse([2], 1) == [2]
    assert pop_elements_greater_than_x_reverse([7, 8, 9, 10], 8) == [9, 10]
    assert pop_elements_greater_than_x_reverse([11, 22, 33, 44], 15) == [22, 33, 44]
    assert pop_elements_greater_than_x_reverse([1, 2, 3, 4, 5, 6, 7, 8, 9], 20) is None


# 431. Тесты для функции `remove_less_than_x`:
def test_remove_less_than_x():
    assert remove_less_than_x([1, 3, 5, 7, 9], 4) == [9, 7, 5]
    assert remove_less_than_x([2, 4, 6, 8], 10) is None
    assert remove_less_than_x([10, 20, 30], 15) == [30, 20]
    assert remove_less_than_x([], 5) is None
    assert remove_less_than_x([-5, -2, -1, 0], -3) == [0, -1, -2]
    assert remove_less_than_x([5, 5, 5, 5, 5], 5) == [5, 5, 5, 5, 5]
    assert remove_less_than_x([1, 2, 3, 4, 5], 0) == [5, 4, 3, 2, 1]
    assert remove_less_than_x([1, 2, 3, 4, 5], 5) == [5]
    assert remove_less_than_x([100], 10) == [100]


# 432. Тесты для функции `find_min_in_stack`:
def test_find_min_in_stack():
    assert find_min_in_stack([1, 2, 3, 4, 5]) == 1
    assert find_min_in_stack([5, 4, 3, 2, 1]) == 1
    assert find_min_in_stack([1]) == 1
    assert find_min_in_stack([-5, -10, -1, -3]) == -10
    assert find_min_in_stack([100, 200, 300, 400]) == 100
    assert find_min_in_stack([0]) == 0
    assert find_min_in_stack([3, 3, 3, 3]) == 3
    assert find_min_in_stack([10, 20, 30, 40, 50]) == 10
    assert find_min_in_stack([]) is None


# 433. Тесты для функции `pop_until_divisible_by_6`:
def test_pop_until_divisible_by_6():
    assert pop_until_divisible_by_6([1, 2, 3, 4, 5, 6]) == [6]
    assert pop_until_divisible_by_6([1, 2, 3, 4, 5, 12]) == [12]
    assert pop_until_divisible_by_6([6, 7, 8, 9]) == [9, 8, 7, 6]
    assert pop_until_divisible_by_6([12, 14, 15, 18]) == [18]
    assert pop_until_divisible_by_6([7, 5, 11]) == [11, 5, 7]
    assert pop_until_divisible_by_6([]) is None
    assert pop_until_divisible_by_6([12, 24, 36, 48]) == [48]
    assert pop_until_divisible_by_6([1, 3, 5, 7]) == [7, 5, 3, 1]
    assert pop_until_divisible_by_6([2, 8, 10, 11]) == [11, 10, 8, 2]


# 434. Тесты для функции `find_even_divisible_by_4`:
def test_find_even_divisible_by_4():
    assert find_even_divisible_by_4([1, 2, 3, 4, 5, 6, 8, 12, 16]) == [16, 12, 8, 4]
    assert find_even_divisible_by_4([5, 7, 11, 13]) is None
    assert find_even_divisible_by_4([4, 8, 12]) == [12, 8, 4]
    assert find_even_divisible_by_4([0, 4, 8, 16, 32]) == [32, 16, 8, 4, 0]
    assert find_even_divisible_by_4([1, 3, 5, 7]) is None
    assert find_even_divisible_by_4([4]) == [4]
    assert find_even_divisible_by_4([]) is None
    assert find_even_divisible_by_4([4, 4, 4, 4]) == [4, 4, 4, 4]
    assert find_even_divisible_by_4([6, 10, 14, 18]) is None


# 435. Тесты для функции `pop_odd_elements`:
def test_pop_odd_elements():
    assert pop_odd_elements([1, 2, 3, 4, 5, 6]) == [5, 3, 1]
    assert pop_odd_elements([1, 3, 5, 7]) == [7, 5, 3, 1]
    assert pop_odd_elements([2, 4, 6, 8]) is None
    assert pop_odd_elements([0, 1, 2, 3]) == [3, 1]
    assert pop_odd_elements([]) is None
    assert pop_odd_elements([1]) == [1]
    assert pop_odd_elements([2]) is None
    assert pop_odd_elements([5, 5, 5]) == [5, 5, 5]
    assert pop_odd_elements([1, 2, 3, 4, 5]) == [5, 3, 1]


# 436. Тесты для функции `remove_less_than_x_v2`:
def test_remove_less_than_x_v2():
    assert remove_less_than_x_v2([1, 3, 5, 7, 9], 4) == [3, 1]
    assert remove_less_than_x_v2([2, 4, 6, 8], 10) == [8, 6, 4, 2]
    assert remove_less_than_x_v2([10, 20, 30], 15) == [10]
    assert remove_less_than_x_v2([], 5) is None
    assert remove_less_than_x_v2([-5, -2, -1, 0], -3) == [-5]
    assert remove_less_than_x_v2([5, 5, 5, 5, 5], 5) is None
    assert remove_less_than_x_v2([1, 2, 3, 4, 5], 0) is None
    assert remove_less_than_x_v2([1, 2, 3, 4, 5], 5) == [4, 3, 2, 1]
    assert remove_less_than_x_v2([100], 10) is None


# 437. Тесты для функции `find_square_numbers_in_stack`:
def test_find_square_numbers_in_stack():
    assert find_square_numbers_in_stack([1, 2, 3, 4, 9, 16]) == [16, 9, 4, 1]
    assert find_square_numbers_in_stack([1, 3, 5, 7]) == [1]
    assert find_square_numbers_in_stack([0, 4, 9, 16, 25]) == [25, 16, 9, 4, 0]
    assert find_square_numbers_in_stack([10, 20, 30, 40]) is None
    assert find_square_numbers_in_stack([1]) == [1]
    assert find_square_numbers_in_stack([2]) is None
    assert find_square_numbers_in_stack([4, 4, 4]) == [4, 4, 4]
    assert find_square_numbers_in_stack([9, 16, 25]) == [25, 16, 9]
    assert find_square_numbers_in_stack([2, 3, 5, 7]) is None


# 438. Тесты для функции `find_max_in_stack`:
def test_find_max_in_stack():
    assert find_max_in_stack([1, 2, 3, 4, 5]) == 5
    assert find_max_in_stack([5, 4, 3, 2, 1]) == 5
    assert find_max_in_stack([1]) == 1
    assert find_max_in_stack([-5, -10, -1, -3]) == -1
    assert find_max_in_stack([100, 200, 300, 400]) == 400
    assert find_max_in_stack([0]) == 0
    assert find_max_in_stack([3, 3, 3, 3]) == 3
    assert find_max_in_stack([10, 20, 30, 40, 50]) == 50
    assert find_max_in_stack([]) is None


# 439. Тесты для функции `pop_elements_divisible_by_7`:
def test_pop_elements_divisible_by_7():
    assert pop_elements_divisible_by_7([7, 14, 21, 28, 35]) == [35, 28, 21, 14, 7]
    assert pop_elements_divisible_by_7([1, 2, 3, 4, 5, 6, 7]) == [7]
    assert pop_elements_divisible_by_7([1, 2, 3, 4, 5, 6, 8, 9]) is None
    assert pop_elements_divisible_by_7([0, 7, 14, 21]) == [21, 14, 7, 0]
    assert pop_elements_divisible_by_7([1, 3, 5, 11]) is None
    assert pop_elements_divisible_by_7([7]) == [7]
    assert pop_elements_divisible_by_7([14, 28, 42, 56]) == [56, 42, 28, 14]
    assert pop_elements_divisible_by_7([21, 35, 49, 63, 77]) == [77, 63, 49, 35, 21]
    assert pop_elements_divisible_by_7([5, 10, 20, 25]) is None


# 440. Тесты для функции `find_greater_than_x_divisible_by_2`:
def test_find_greater_than_x_divisible_by_2():
    assert find_greater_than_x_divisible_by_2([1, 2, 3, 4, 5], 3) == [4]
    assert find_greater_than_x_divisible_by_2([10, 20, 30, 40, 50], 25) == [50, 40, 30]
    assert find_greater_than_x_divisible_by_2([5, 5, 5, 5], 5) is None
    assert find_greater_than_x_divisible_by_2([1, 2, 3, 4, 5, 6], 3) == [6, 4]
    assert find_greater_than_x_divisible_by_2([1], 0) is None
    assert find_greater_than_x_divisible_by_2([2], 1) == [2]
    assert find_greater_than_x_divisible_by_2([7, 8, 9, 10], 8) == [10]
    assert find_greater_than_x_divisible_by_2([11, 22, 33, 44], 15) == [44, 22]
    assert find_greater_than_x_divisible_by_2([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == [8, 6]


# 441. Тесты для функции `remove_not_divisible_by_4`:
def test_remove_not_divisible_by_4():
    assert remove_not_divisible_by_4([8, 15, 3, 4]) == [3, 15]
    assert remove_not_divisible_by_4([16, 2, 12]) == [2]
    assert remove_not_divisible_by_4([4, 8, 16, 32]) is None
    assert remove_not_divisible_by_4([]) is None
    assert remove_not_divisible_by_4([5, 7, 11]) == [11, 7, 5]
    assert remove_not_divisible_by_4([4, 15, 20, 8, 3, 12]) == [3, 15]
    assert remove_not_divisible_by_4([-4, -8, 0]) is None
    assert remove_not_divisible_by_4([9, 17, 21]) == [21, 17, 9]
    assert remove_not_divisible_by_4([-1, -2, -5, -6]) == [-6, -5, -2, -1]


# 442. Тесты для функции `pop_elements_divisible_by_10`:
def test_pop_elements_divisible_by_10():
    assert pop_elements_divisible_by_10([20, 5, 30, 7, 10]) == [10, 30, 20]
    assert pop_elements_divisible_by_10([4, 2, 12]) is None
    assert pop_elements_divisible_by_10([40, 50, 60]) == [60, 50, 40]
    assert pop_elements_divisible_by_10([]) is None
    assert pop_elements_divisible_by_10([10, 20, 30, 5, 1]) == [30, 20, 10]
    assert pop_elements_divisible_by_10([0, 100, 200]) == [200, 100, 0]
    assert pop_elements_divisible_by_10([5, 7, 15]) is None
    assert pop_elements_divisible_by_10([-10, -20, -5]) == [-20, -10]
    assert pop_elements_divisible_by_10([9, 19, 29]) is None


# 443. Тесты для функции `find_divisible_by_3_and_5`:
def test_find_divisible_by_3_and_5():
    assert find_divisible_by_3_and_5([30, 45, 60, 10, 15]) == [15, 60, 45, 30]
    assert find_divisible_by_3_and_5([3, 5, 9, 10]) is None
    assert find_divisible_by_3_and_5([75, 90, 105]) == [105, 90, 75]
    assert find_divisible_by_3_and_5([]) is None
    assert find_divisible_by_3_and_5([15, 30, 45, 5, 10]) == [45, 30, 15]
    assert find_divisible_by_3_and_5([0, 60, 120]) == [120, 60, 0]
    assert find_divisible_by_3_and_5([4, 2, 6]) is None
    assert find_divisible_by_3_and_5([-15, -30, -5]) == [-30, -15]
    assert find_divisible_by_3_and_5([9, 21, 27]) is None


# 444. Тесты для функции `remove_greater_than_x`:
def test_remove_greater_than_x():
    assert remove_greater_than_x([8, 12, 15, 4], 10) == [4, 8]
    assert remove_greater_than_x([16, 2, 5, 12], 7) == [5, 2]
    assert remove_greater_than_x([4, 8, 16, 3], 8) == [3, 8, 4]
    assert remove_greater_than_x([], 10) is None
    assert remove_greater_than_x([5, 7, 11], 15) == [11, 7, 5]
    assert remove_greater_than_x([4, 15, 20, 8], 10) == [8, 4]
    assert remove_greater_than_x([-4, -8, 0], -1) == [-8, -4]
    assert remove_greater_than_x([9, 17, 21], 10) == [9]
    assert remove_greater_than_x([-1, -2, -5, -6], -3) == [-6, -5]


# 445. Тесты для функции `pop_elements_greater_than_x_even`:
def test_pop_elements_greater_than_x_even():
    assert pop_elements_greater_than_x_even([8, 10, 12, 4], 9) == [12, 10]
    assert pop_elements_greater_than_x_even([16, 3, 5, 14], 12) == [14, 16]
    assert pop_elements_greater_than_x_even([4, 8, 16, 3], 6) == [16, 8]
    assert pop_elements_greater_than_x_even([], 5) is None
    assert pop_elements_greater_than_x_even([5, 7, 11], 10) is None
    assert pop_elements_greater_than_x_even([4, 15, 20, 8], 15) == [20]
    assert pop_elements_greater_than_x_even([-4, -8, 0], -3) == [0]
    assert pop_elements_greater_than_x_even([9, 17, 21], 15) is None
    assert pop_elements_greater_than_x_even([-1, -2, -5, -6], -4) == [-2]


# 446. Тесты для функции `process_queue_until_sum_exceeds`:
def test_process_queue_until_sum_exceeds():
    assert process_queue_until_sum_exceeds([3, 5, 2, 7], 8) == [3, 5, 2]
    assert process_queue_until_sum_exceeds([16, 3, 5, 12], 14) == [16]
    assert process_queue_until_sum_exceeds([4, 8, 1, 3], 7) == [4, 8]
    assert process_queue_until_sum_exceeds([], 5) is None
    assert process_queue_until_sum_exceeds([5, 7, 1], 10) == [5, 7]
    assert process_queue_until_sum_exceeds([4, 2, 5, 8], 6) == [4, 2, 5]
    assert process_queue_until_sum_exceeds([-4, -8, 10], -5) == [-4]
    assert process_queue_until_sum_exceeds([9, 1, 2], 10) == [9, 1, 2]
    assert process_queue_until_sum_exceeds([-1, -2, -3, -4], -1) == [-1, -2, -3, -4]


# 447. Тесты для функции `process_queue_less_than_average`:
def test_process_queue_less_than_average():
    assert process_queue_less_than_average([3, 5, 2, 7]) == [3, 2]
    assert process_queue_less_than_average([16, 3, 5, 12]) == [3, 5]
    assert process_queue_less_than_average([4, 8, 1, 3]) == [1, 3]
    assert process_queue_less_than_average([]) is None
    assert process_queue_less_than_average([77, 77, 77]) is None
    assert process_queue_less_than_average([4, 2, 5, 8]) == [4, 2]
    assert process_queue_less_than_average([-4, -8, 0]) == [-8]
    assert process_queue_less_than_average([9, 1, 2]) == [1, 2]
    assert process_queue_less_than_average([-1, -2, -3, -4]) == [-3, -4]


# 448. Тесты для функции `process_queue_unique_elements`:
def test_process_queue_unique_elements():
    assert process_queue_unique_elements([3, 5, 2, 7, 5, 3]) == [2, 7]
    assert process_queue_unique_elements([16, 3, 5, 12, 16]) == [3, 5, 12]
    assert process_queue_unique_elements([4, 8, 1, 4, 3, 8]) == [1, 3]
    assert process_queue_unique_elements([]) is None
    assert process_queue_unique_elements([5, 7, 1, 7, 5]) == [1]
    assert process_queue_unique_elements([4, 8, 4, 8, 1]) == [1]
    assert process_queue_unique_elements([10, 20, 30, 40, 20]) == [10, 30, 40]
    assert process_queue_unique_elements([5, 10, 5, 15, 20]) == [10, 15, 20]
    assert process_queue_unique_elements([9, 19, 9, 21, 21]) == [19]


# 449. Тесты для функции `process_queue_divisible_by_5`:
def test_process_queue_divisible_by_5():
    assert process_queue_divisible_by_5([3, 5, 10, 7, 25]) == [5, 10, 25]
    assert process_queue_divisible_by_5([1, 2, 3, 4]) is None
    assert process_queue_divisible_by_5([50, 5, 10, 20]) == [50, 5, 10, 20]
    assert process_queue_divisible_by_5([]) is None
    assert process_queue_divisible_by_5([5, 10, 15]) == [5, 10, 15]
    assert process_queue_divisible_by_5([0, 100, 200]) == [0, 100, 200]
    assert process_queue_divisible_by_5([1, 3, 7]) is None
    assert process_queue_divisible_by_5([-5, -10, -15]) == [-5, -10, -15]
    assert process_queue_divisible_by_5([25, 30, 35, 40]) == [25, 30, 35, 40]


# 450. Тесты для функции `process_queue_greater_than_x`:
def test_process_queue_greater_than_x():
    assert process_queue_greater_than_x([8, 12, 15, 4], 10) == [12, 15]
    assert process_queue_greater_than_x([16, 2, 5, 12], 7) == [16, 12]
    assert process_queue_greater_than_x([4, 8, 16, 3], 8) == [16]
    assert process_queue_greater_than_x([], 10) is None
    assert process_queue_greater_than_x([5, 7, 11], 5) == [7, 11]
    assert process_queue_greater_than_x([4, 15, 20, 8], 10) == [15, 20]
    assert process_queue_greater_than_x([-4, -8, 0], -1) == [0]
    assert process_queue_greater_than_x([9, 17, 21], 10) == [17, 21]
    assert process_queue_greater_than_x([-1, -2, -5, -6], -3) == [-1, -2]


# 451. Тесты для функции `process_queue_divisible_by_2_not_4`:
def test_process_queue_divisible_by_2_not_4():
    assert process_queue_divisible_by_2_not_4([2, 4, 6, 8, 10, 12]) == [2, 6, 10]
    assert process_queue_divisible_by_2_not_4([4, 8, 12, 16]) is None
    assert process_queue_divisible_by_2_not_4([2, 6, 10]) == [2, 6, 10]
    assert process_queue_divisible_by_2_not_4([]) is None
    assert process_queue_divisible_by_2_not_4([1, 3, 5, 7]) is None
    assert process_queue_divisible_by_2_not_4([14, 18, 20, 24]) == [14, 18]
    assert process_queue_divisible_by_2_not_4([-2, -4, -6, -8]) == [-2, -6]
    assert process_queue_divisible_by_2_not_4([9, 13, 17]) is None
    assert process_queue_divisible_by_2_not_4([3, 6, 9, 12]) == [6]


# 452. Тесты для функции `process_queue_divisible_by_7`:
def test_process_queue_divisible_by_7():
    assert process_queue_divisible_by_7([7, 14, 21, 5, 10]) == [7, 14, 21]
    assert process_queue_divisible_by_7([1, 2, 3, 4]) is None
    assert process_queue_divisible_by_7([28, 35, 42, 49]) == [28, 35, 42, 49]
    assert process_queue_divisible_by_7([]) is None
    assert process_queue_divisible_by_7([7, 14, 21]) == [7, 14, 21]
    assert process_queue_divisible_by_7([0, 70, 140]) == [0, 70, 140]
    assert process_queue_divisible_by_7([1, 3, 7]) == [7]
    assert process_queue_divisible_by_7([-7, -14, -21]) == [-7, -14, -21]
    assert process_queue_divisible_by_7([35, 70, 105]) == [35, 70, 105]


# 453. Тесты для функции `process_queue_odd_elements`:
def test_process_queue_odd_elements():
    assert process_queue_odd_elements([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert process_queue_odd_elements([2, 4, 6, 8]) is None
    assert process_queue_odd_elements([1, 3, 5, 7]) == [1, 3, 5, 7]
    assert process_queue_odd_elements([]) is None
    assert process_queue_odd_elements([1, 3, 5]) == [1, 3, 5]
    assert process_queue_odd_elements([2, 4, 6]) is None
    assert process_queue_odd_elements([7, 14, 21]) == [7, 21]
    assert process_queue_odd_elements([-1, -3, -5]) == [-1, -3, -5]
    assert process_queue_odd_elements([5, 10, 15, 20]) == [5, 15]


# 454. Тесты для функции `process_queue_square_numbers`:
def test_process_queue_square_numbers():
    assert process_queue_square_numbers([1, 2, 3, 4, 5, 9, 16]) == [1, 4, 9, 16]
    assert process_queue_square_numbers([2, 3, 5, 7]) is None
    assert process_queue_square_numbers([4, 9, 16, 25, 36]) == [4, 9, 16, 25, 36]
    assert process_queue_square_numbers([]) is None
    assert process_queue_square_numbers([1, 4, 9]) == [1, 4, 9]
    assert process_queue_square_numbers([2, 3, 6]) is None
    assert process_queue_square_numbers([7, 14, 21]) is None
    assert process_queue_square_numbers([1, 4, 9]) == [1, 4, 9]
    assert process_queue_square_numbers([25, 49, 81]) == [25, 49, 81]


# 455. Тесты для функции `process_queue_divisible_by_3_or_5`:
def test_process_queue_divisible_by_3_or_5():
    assert process_queue_divisible_by_3_or_5([1, 2, 3, 4, 5, 6, 7, 9]) == [3, 5, 6, 9]
    assert process_queue_divisible_by_3_or_5([1, 2, 4, 7, 8]) is None
    assert process_queue_divisible_by_3_or_5([15, 30, 45, 60]) == [15, 30, 45, 60]
    assert process_queue_divisible_by_3_or_5([]) is None
    assert process_queue_divisible_by_3_or_5([3, 6, 9]) == [3, 6, 9]
    assert process_queue_divisible_by_3_or_5([5, 10, 15]) == [5, 10, 15]
    assert process_queue_divisible_by_3_or_5([7, 14, 21]) == [21]
    assert process_queue_divisible_by_3_or_5([-3, -6, -9]) == [-3, -6, -9]
    assert process_queue_divisible_by_3_or_5([12, 18, 24]) == [12, 18, 24]


# 456. Тесты для функции `process_queue_divisible_by_3_not_6`:
def test_process_queue_divisible_by_3_not_6():
    assert process_queue_divisible_by_3_not_6([3, 6, 9, 12, 15]) == [3, 9, 15]
    assert process_queue_divisible_by_3_not_6([6, 12, 18]) is None
    assert process_queue_divisible_by_3_not_6([3, 9, 15, 21]) == [3, 9, 15, 21]
    assert process_queue_divisible_by_3_not_6([]) is None
    assert process_queue_divisible_by_3_not_6([3, 6, 9]) == [3, 9]
    assert process_queue_divisible_by_3_not_6([12, 15, 18]) == [15]
    assert process_queue_divisible_by_3_not_6([4, 8, 14]) is None
    assert process_queue_divisible_by_3_not_6([3, 27, 9]) == [3, 27, 9]
    assert process_queue_divisible_by_3_not_6([12, 24, 36]) is None


# 457. Тесты для функции `process_queue_remove_less_than_x`:
def test_process_queue_remove_less_than_x():
    assert process_queue_remove_less_than_x([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    assert process_queue_remove_less_than_x([1, 2, 3, 4, 5], 1) == [1, 2, 3, 4, 5]
    assert process_queue_remove_less_than_x([1, 2, 3, 4, 5], 6) is None
    assert process_queue_remove_less_than_x([], 3) is None
    assert process_queue_remove_less_than_x([1, 2, 3, 4, 5], 5) == [5]
    assert process_queue_remove_less_than_x([5, 10, 15], 10) == [10, 15]
    assert process_queue_remove_less_than_x([7, 14, 21], 15) == [21]
    assert process_queue_remove_less_than_x([-1, -3, 5], 0) == [5]
    assert process_queue_remove_less_than_x([3, 6, 9], 7) == [9]


# 458. Тесты для функции `process_queue_less_than_x`:
def test_process_queue_less_than_x():
    assert process_queue_less_than_x([1, 2, 3, 4, 5], 3) == [1, 2]
    assert process_queue_less_than_x([1, 2, 3, 4, 5], 1) is None
    assert process_queue_less_than_x([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5]
    assert process_queue_less_than_x([], 3) is None
    assert process_queue_less_than_x([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4]
    assert process_queue_less_than_x([5, 10, 15], 10) == [5]
    assert process_queue_less_than_x([7, 14, 21], 15) == [7, 14]
    assert process_queue_less_than_x([-1, -3, 5], 0) == [-1, -3]
    assert process_queue_less_than_x([3, 6, 9], 7) == [3, 6]


# 459. Тесты для функции `process_queue_min_element`:
def test_process_queue_min_element():
    assert process_queue_min_element([1, 2, 3, 4, 5]) == 1
    assert process_queue_min_element([5, 4, 3, 2, 1]) == 1
    assert process_queue_min_element([-1, -2, -3, -4, -5]) == -5
    assert process_queue_min_element([0]) == 0
    assert process_queue_min_element([]) is None
    assert process_queue_min_element([10, 20, 5, 30]) == 5
    assert process_queue_min_element([7, 14, 21, 2]) == 2
    assert process_queue_min_element([3, 3, 3]) == 3
    assert process_queue_min_element([-1, 1, -2, 2]) == -2


# 460. Тесты для функции `process_queue_remove_greater_than_x`:
def test_process_queue_remove_greater_than_x():
    assert process_queue_remove_greater_than_x([1, 2, 3, 4, 5], 3) == [1, 2, 3]
    assert process_queue_remove_greater_than_x([5, 10, 15], 10) == [5, 10]
    assert process_queue_remove_greater_than_x([7, 14, 21], 15) == [7, 14]
    assert process_queue_remove_greater_than_x([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
    assert process_queue_remove_greater_than_x([], 3) is None
    assert process_queue_remove_greater_than_x([-1, -3, 5], 0) == [-1, -3]
    assert process_queue_remove_greater_than_x([3, 6, 9], 7) == [3, 6]
    assert process_queue_remove_greater_than_x([10, 20, 30], 25) == [10, 20]
    assert process_queue_remove_greater_than_x([8, 12, 15, 4], 10) == [8, 4]


# 461. Тесты для функции process_queue_max_element
def test_process_queue_max_element():
    assert process_queue_max_element([1, 2, 3, 4, 5]) == 5
    assert process_queue_max_element([10, 9, 8, 7, 6]) == 10
    assert process_queue_max_element([-1, -2, -3, -4, -5]) == -1
    assert process_queue_max_element([]) is None
    assert process_queue_max_element([1, 1, 1, 1, 1]) == 1
    assert process_queue_max_element([4, 5, 6, 7, 4]) == 7


# 462. Тесты для функции process_queue_remove_divisible_by_4
def test_process_queue_remove_divisible_by_4():
    assert process_queue_remove_divisible_by_4([4, 8, 12, 16]) is None
    assert process_queue_remove_divisible_by_4([1, 2, 3, 5, 7]) == [1, 2, 3, 5, 7]
    assert process_queue_remove_divisible_by_4([4, 5, 6, 8, 9]) == [5, 6, 9]
    assert process_queue_remove_divisible_by_4([]) is None
    assert process_queue_remove_divisible_by_4([0, 4, 8, 4, 16]) is None
    assert process_queue_remove_divisible_by_4([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]


# 463. Тесты для функции process_queue_greater_than_x_and_divisible_by_2
def test_process_queue_greater_than_x_and_divisible_by_2():
    assert process_queue_greater_than_x_and_divisible_by_2([1, 2, 3, 4, 5], 2) == [4]
    assert process_queue_greater_than_x_and_divisible_by_2([10, 9, 8, 7, 6], 5) == [10, 8, 6]
    assert process_queue_greater_than_x_and_divisible_by_2([1, 2, 3, 4, 5], 6) is None
    assert process_queue_greater_than_x_and_divisible_by_2([], 1) is None
    assert process_queue_greater_than_x_and_divisible_by_2([1, 2, 3, 4, 5], 0) == [2, 4]
    assert process_queue_greater_than_x_and_divisible_by_2([1, 3, 5, 7, 9], 4) is None


# 464. Тесты для функции process_queue_greater_than_x_and_divisible_by_3
def test_process_queue_greater_than_x_and_divisible_by_3():
    assert process_queue_greater_than_x_and_divisible_by_3([1, 2, 3, 4, 5, 6], 2) == [3, 6]
    assert process_queue_greater_than_x_and_divisible_by_3([9, 8, 7, 6, 5], 5) == [9, 6]
    assert process_queue_greater_than_x_and_divisible_by_3([1, 2, 3, 4, 5], 3) is None
    assert process_queue_greater_than_x_and_divisible_by_3([], 1) is None
    assert process_queue_greater_than_x_and_divisible_by_3([1, 3, 6, 9], 0) == [3, 6, 9]
    assert process_queue_greater_than_x_and_divisible_by_3([2, 4, 8], 4) is None


# 465. Тесты для функции process_queue_less_than_x_not_divisible_by_5
def test_process_queue_less_than_x_not_divisible_by_5():
    assert process_queue_less_than_x_not_divisible_by_5([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4]
    assert process_queue_less_than_x_not_divisible_by_5([10, 9, 8, 7, 6], 8) == [7, 6]
    assert process_queue_less_than_x_not_divisible_by_5([15, 25, 35, 45], 50) is None
    assert process_queue_less_than_x_not_divisible_by_5([], 10) is None
    assert process_queue_less_than_x_not_divisible_by_5([0, 1, 2, 3], 4) == [1, 2, 3]
    assert process_queue_less_than_x_not_divisible_by_5([5, 10, 15], 20) is None


# 466. Тесты для функции process_queue_even_and_divisible_by_4
def test_process_queue_even_and_divisible_by_4():
    assert process_queue_even_and_divisible_by_4([4, 8, 12, 16, 20]) == [4, 8, 12, 16, 20]
    assert process_queue_even_and_divisible_by_4([1, 2, 3, 4, 5]) == [4]
    assert process_queue_even_and_divisible_by_4([5, 6, 7, 8, 9]) == [8]
    assert process_queue_even_and_divisible_by_4([1, 3, 5, 7]) is None
    assert process_queue_even_and_divisible_by_4([0, 4, 8, 12]) == [0, 4, 8, 12]
    assert process_queue_even_and_divisible_by_4([2, 6, 10, 14]) is None


# 467. Тесты для функции process_queue_not_divisible_by_3_and_5
def test_process_queue_not_divisible_by_3_and_5():
    assert process_queue_not_divisible_by_3_and_5([1, 2, 3, 4, 5]) == [1, 2, 4]
    assert process_queue_not_divisible_by_3_and_5([9, 8, 7, 6, 5]) == [8, 7]
    assert process_queue_not_divisible_by_3_and_5([15, 25, 35, 45]) is None
    assert process_queue_not_divisible_by_3_and_5([4, 8, 14, 22]) == [4, 8, 14, 22]
    assert process_queue_not_divisible_by_3_and_5([3, 5, 9, 15]) is None


# 468. Тесты для функции find_elements_greater_than_x
def test_find_elements_greater_than_x():
    assert find_elements_greater_than_x((1, 2, 3, 4, 5), 3) == (4, 5)
    assert find_elements_greater_than_x((10, 9, 8, 7, 6), 8) == (10, 9)
    assert find_elements_greater_than_x((-1, -2, -3, -4, -5), -3) == (-1, -2)
    assert find_elements_greater_than_x((), 1) is None
    assert find_elements_greater_than_x((1, 2, 3, 4, 5), 5) is None
    assert find_elements_greater_than_x((4, 5, 6, 7, 4), 6) == (7,)


# 469. Тесты для функции find_even_elements_in_tuple
def test_find_even_elements_in_tuple():
    assert find_even_elements_in_tuple((1, 2, 3, 4, 5)) == (2, 4)
    assert find_even_elements_in_tuple((10, 9, 8, 7, 6)) == (10, 8, 6)
    assert find_even_elements_in_tuple((-1, -2, -3, -4, -5)) == (-2, -4)
    assert find_even_elements_in_tuple((1, 3, 5)) is None
    assert find_even_elements_in_tuple((2, 4, 6, 8)) == (2, 4, 6, 8)
    assert find_even_elements_in_tuple(()) is None


# 470. Тесты для функции find_elements_less_than_average
def test_find_elements_less_than_average():
    assert find_elements_less_than_average((1, 2, 3, 4, 5)) == (1, 2)
    assert find_elements_less_than_average((10, 9, 8, 7, 6)) == (7, 6)
    assert find_elements_less_than_average((1, 1, 1, 1, 1)) is None
    assert find_elements_less_than_average((2, 4, 6, 8, 10)) == (2, 4)
    assert find_elements_less_than_average(()) is None
    assert find_elements_less_than_average((-1, -2, -3, -4, -5)) == (-4, -5)
    assert find_elements_less_than_average((5, 10, 15, 20, 25)) == (5, 10)


# 471. Тесты для функции find_elements_greater_than_x_divisible_by_5
def test_find_elements_greater_than_x_divisible_by_5():
    assert find_elements_greater_than_x_divisible_by_5((1, 5, 10, 15, 20), 10) == (15, 20)
    assert find_elements_greater_than_x_divisible_by_5((25, 30, 35, 40, 45), 20) == (25, 30, 35, 40, 45)
    assert find_elements_greater_than_x_divisible_by_5((5, 10, 15), 20) is None
    assert find_elements_greater_than_x_divisible_by_5((), 5) is None
    assert find_elements_greater_than_x_divisible_by_5((5, 10, 15, 20, 25), 0) == (5, 10, 15, 20, 25)
    assert find_elements_greater_than_x_divisible_by_5((1, 2, 3, 4), 3) is None


# 472. Тесты для функции find_unique_elements_in_tuple
def test_find_unique_elements_in_tuple():
    assert find_unique_elements_in_tuple((1, 2, 2, 3, 4, 4)) == (1, 3)
    assert find_unique_elements_in_tuple((5, 5, 5, 5, 5, 5)) is None
    assert find_unique_elements_in_tuple((1, 2, 3, 4, 5)) == (1, 2, 3, 4, 5)
    assert find_unique_elements_in_tuple(()) is None
    assert find_unique_elements_in_tuple((6, 7, 8, 9, 10, 10, 11)) == (6, 7, 8, 9, 11)
    assert find_unique_elements_in_tuple((2, 2, 2, 3, 3, 3, 4, 4)) is None


# 473. Тесты для функции find_divisible_by_3_and_4
def test_find_divisible_by_3_and_4():
    assert find_divisible_by_3_and_4((12, 24, 36, 48)) == (12, 24, 36, 48)
    assert find_divisible_by_3_and_4((6, 9, 12, 18, 24)) == (12, 24)
    assert find_divisible_by_3_and_4((3, 6, 9, 15)) is None
    assert find_divisible_by_3_and_4(()) is None
    assert find_divisible_by_3_and_4((3, 4, 5, 6, 7)) is None
    assert find_divisible_by_3_and_4((3, 12, 24, 36, 45)) == (12, 24, 36)


# 474. Тесты для функции find_odd_elements_in_tuple
def test_find_odd_elements_in_tuple():
    assert find_odd_elements_in_tuple((1, 2, 3, 4, 5)) == (1, 3, 5)
    assert find_odd_elements_in_tuple((10, 9, 8, 7, 6)) == (9, 7)
    assert find_odd_elements_in_tuple((-1, -2, -3, -4, -5)) == (-1, -3, -5)
    assert find_odd_elements_in_tuple((2, 4, 6)) is None
    assert find_odd_elements_in_tuple((1, 3, 5, 7)) == (1, 3, 5, 7)
    assert find_odd_elements_in_tuple(()) is None


# 475. Тесты для функции find_min_in_tuple
def test_find_min_in_tuple():
    assert find_min_in_tuple((1, 2, 3, 4, 5)) == 1
    assert find_min_in_tuple((10, 9, 8, 7, 6)) == 6
    assert find_min_in_tuple((-1, -2, -3, -4, -5)) == -5
    assert find_min_in_tuple(()) is None
    assert find_min_in_tuple((5, 5, 5, 5, 5)) == 5
    assert find_min_in_tuple((3, 4, 2, 1, 5)) == 1


# 476. Тесты для функции find_max_in_tuple
def test_find_max_in_tuple():
    assert find_max_in_tuple((1, 2, 3, 4, 5)) == 5
    assert find_max_in_tuple((10, 9, 8, 7, 6)) == 10
    assert find_max_in_tuple((-1, -2, -3, -4, -5)) == -1
    assert find_max_in_tuple(()) is None
    assert find_max_in_tuple((5, 5, 5, 5, 5)) == 5
    assert find_max_in_tuple((3, 4, 2, 1, 5)) == 5


# 477. Тесты для функции find_divisible_by_2_or_5
def test_find_divisible_by_2_or_5():
    assert find_divisible_by_2_or_5((1, 2, 3, 4, 5)) == (2, 4, 5)
    assert find_divisible_by_2_or_5((10, 9, 8, 7, 6)) == (10, 8, 6)
    assert find_divisible_by_2_or_5((1, 3, 7, 11, 13)) is None
    assert find_divisible_by_2_or_5(()) is None
    assert find_divisible_by_2_or_5((20, 25, 30, 35, 40)) == (20, 25, 30, 35, 40)
    assert find_divisible_by_2_or_5((1, 5, 10, 15, 20)) == (5, 10, 15, 20)


# 478. Тесты для функции find_divisible_by_6
def test_find_divisible_by_57():
    assert find_divisible_by_57((6, 12, 18, 24, 57)) == (57,)
    assert find_divisible_by_57((5, 10, 15, 20, 25)) is None
    assert find_divisible_by_57((1, 2, 3, 4, 5)) is None
    assert find_divisible_by_57(()) is None
    assert find_divisible_by_57((6, 114, 24)) == (114,)
    assert find_divisible_by_57((12, 228, 456, 60)) == (228, 456)


# 479. Тесты для функции find_square_numbers_in_tuple
def test_find_square_numbers_in_tuple():
    assert find_square_numbers_in_tuple((1, 2, 3, 4, 5)) == (1, 4)
    assert find_square_numbers_in_tuple((10, 9, 8, 7, 6)) == (9,)
    assert find_square_numbers_in_tuple((1, 2, 3, 4, 5)) == (1, 4)
    assert find_square_numbers_in_tuple((4, 9, 16, 25, 36)) == (4, 9, 16, 25, 36)
    assert find_square_numbers_in_tuple(()) is None
    assert find_square_numbers_in_tuple((1, 4, 9, 16, 25, 36, 49)) == (1, 4, 9, 16, 25, 36, 49)


# 480. Тесты для функции find_greater_than_x_not_divisible_by_3
def test_find_greater_than_x_not_divisible_by_3():
    assert find_greater_than_x_not_divisible_by_3((1, 2, 3, 4, 5), 2) == (4, 5)
    assert find_greater_than_x_not_divisible_by_3((10, 9, 8, 7, 6), 5) == (10, 8, 7)
    assert find_greater_than_x_not_divisible_by_3((1, 2, 3, 4, 5), 6) is None
    assert find_greater_than_x_not_divisible_by_3((), 1) is None
    assert find_greater_than_x_not_divisible_by_3((4, 5, 6, 7, 8, 9), 3) == (4, 5, 7, 8)
    assert find_greater_than_x_not_divisible_by_3((1, 1, 1, 1, 1), 1) is None


# 481. Тесты для функции `find_greater_than_x_divisible_by_3`:
def test_find_greater_than_x_divisible_by_3():
    assert find_greater_than_x_divisible_by_3((1, 2, 3, 6, 9, 12), 5) == (6, 9, 12)
    assert find_greater_than_x_divisible_by_3((1, 2, 3, 4, 5), 2) == (3,)
    assert find_greater_than_x_divisible_by_3((10, 11, 15, 18), 16) == (18,)
    assert find_greater_than_x_divisible_by_3((1, 2, 3, 6, 9, 12), 12) is None
    assert find_greater_than_x_divisible_by_3((1, 2, 3, 4, 5), 5) is None
    assert find_greater_than_x_divisible_by_3((0, 3, 6, 9, 12), 10) == (12,)
    assert find_greater_than_x_divisible_by_3((3,), 0) == (3,)
    assert find_greater_than_x_divisible_by_3((), 0) is None
    assert find_greater_than_x_divisible_by_3((3, 5, 7, 9), 8) == (9,)


# 482. Тесты для функции `find_not_divisible_by_4_and_5`:
def test_find_not_divisible_by_4_and_5():
    assert find_not_divisible_by_4_and_5((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) == (1, 2, 3, 6, 7, 9)
    assert find_not_divisible_by_4_and_5((4, 5, 8, 10, 12, 15, 16, 20)) is None
    assert find_not_divisible_by_4_and_5((4, 8, 12, 16, 20)) is None
    assert find_not_divisible_by_4_and_5((5, 10, 15, 25)) is None
    assert find_not_divisible_by_4_and_5((2, 3, 6, 7, 9)) == (2, 3, 6, 7, 9)
    assert find_not_divisible_by_4_and_5((1, 4, 5, 8, 10)) == (1,)
    assert find_not_divisible_by_4_and_5((),) is None
    assert find_not_divisible_by_4_and_5((20, 25, 30, 35, 40)) is None
    assert find_not_divisible_by_4_and_5((9, 14, 21, 33)) == (9, 14, 21, 33)


# 483. Тесты для функции `find_less_than_x_divisible_by_3`:
def test_find_less_than_x_divisible_by_3():
    assert find_less_than_x_divisible_by_3((1, 2, 3, 6, 9, 12), 10) == (3, 6, 9)
    assert find_less_than_x_divisible_by_3((1, 2, 3, 4, 5), 6) == (3,)
    assert find_less_than_x_divisible_by_3((10, 11, 15, 18), 20) == (15, 18)
    assert find_less_than_x_divisible_by_3((1, 2, 3, 6, 9, 12), 2) is None
    assert find_less_than_x_divisible_by_3((1, 2, 3, 4, 5), 1) is None
    assert find_less_than_x_divisible_by_3((0, 3, 6, 9, 12), 9) == (0, 3, 6)
    assert find_less_than_x_divisible_by_3((3,), 4) == (3,)
    assert find_less_than_x_divisible_by_3((), 3) is None
    assert find_less_than_x_divisible_by_3((3, 5, 7, 9), 10) == (3, 9)


# 484. Тесты для функции `find_divisible_by_2_and_5`:
def test_find_divisible_by_2_and_5():
    assert find_divisible_by_2_and_5((1, 2, 5, 10, 12, 15, 20)) == (10, 20)
    assert find_divisible_by_2_and_5((10, 20, 30, 40, 50)) == (10, 20, 30, 40, 50)
    assert find_divisible_by_2_and_5((5, 15, 25, 35)) is None
    assert find_divisible_by_2_and_5((2, 4, 6, 8)) is None
    assert find_divisible_by_2_and_5((0, 10, 20, 25)) == (0, 10, 20)
    assert find_divisible_by_2_and_5((5, 10, 15)) == (10,)
    assert find_divisible_by_2_and_5((),) is None
    assert find_divisible_by_2_and_5((30, 35, 40, 50)) == (30, 40, 50)
    assert find_divisible_by_2_and_5((25, 50, 75, 100)) == (50, 100)


# 485. Тесты для функции `find_not_square_numbers_in_tuple`:
def test_find_not_square_numbers_in_tuple():
    assert find_not_square_numbers_in_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) == (2, 3, 5, 6, 7, 8, 10)
    assert find_not_square_numbers_in_tuple((4, 9, 16, 25, 36)) is None
    assert find_not_square_numbers_in_tuple((2, 3, 5, 6, 7, 8, 10)) == (2, 3, 5, 6, 7, 8, 10)
    assert find_not_square_numbers_in_tuple((4, 8, 12, 16, 20)) == (8, 12, 20)
    assert find_not_square_numbers_in_tuple((4, 5, 6, 7, 9)) == (5, 6, 7)
    assert find_not_square_numbers_in_tuple((),) is None
    assert find_not_square_numbers_in_tuple((1, 3, 7, 11, 12)) == (3, 7, 11, 12)
    assert find_not_square_numbers_in_tuple((4, 16, 25, 36)) is None
    assert find_not_square_numbers_in_tuple((5, 10, 15, 20)) == (5, 10, 15, 20)


# 486. Тесты для функции `find_divisible_by_2_and_7`:
def test_find_divisible_by_2_and_7():
    assert find_divisible_by_2_and_7((1, 2, 7, 14, 21, 28, 35, 42)) == (14, 28, 42)
    assert find_divisible_by_2_and_7((14, 28, 42, 56, 70, 84)) == (14, 28, 42, 56, 70, 84)
    assert find_divisible_by_2_and_7((1, 3, 5, 7, 9, 11)) is None
    assert find_divisible_by_2_and_7((2, 4, 8, 16)) is None
    assert find_divisible_by_2_and_7((0, 7, 14, 28)) == (0, 14, 28)
    assert find_divisible_by_2_and_7((7, 14, 21)) == (14,)
    assert find_divisible_by_2_and_7((),) is None
    assert find_divisible_by_2_and_7((7, 14, 35, 42)) == (14, 42)
    assert find_divisible_by_2_and_7((28, 56, 84, 112)) == (28, 56, 84, 112)


# 487. Тесты для функции `find_less_than_x_odd`:
def test_find_less_than_x_odd():
    assert find_less_than_x_odd((1, 2, 3, 6, 9, 12), 10) == (1, 3, 9)
    assert find_less_than_x_odd((1, 2, 3, 4, 5), 6) == (1, 3, 5)
    assert find_less_than_x_odd((10, 11, 15, 18), 16) == (11, 15)
    assert find_less_than_x_odd((1, 2, 3, 6, 9, 12), 2) == (1,)
    assert find_less_than_x_odd((1, 2, 3, 4, 5), 1) is None
    assert find_less_than_x_odd((0, 3, 6, 9, 12), 9) == (3,)
    assert find_less_than_x_odd((3,), 4) == (3,)
    assert find_less_than_x_odd((), 3) is None
    assert find_less_than_x_odd((3, 5, 7, 9), 8) == (3, 5, 7)


# 488. Тесты для функции `find_greater_than_x_even`:
def test_find_greater_than_x_even():
    assert find_greater_than_x_even((1, 2, 3, 6, 9, 12), 5) == (6, 12)
    assert find_greater_than_x_even((1, 2, 3, 4, 5), 2) == (4,)
    assert find_greater_than_x_even((10, 11, 14, 18), 13) == (14, 18)
    assert find_greater_than_x_even((1, 2, 3, 6, 9, 12), 12) is None
    assert find_greater_than_x_even((1, 2, 3, 4, 5), 5) is None
    assert find_greater_than_x_even((0, 3, 6, 8, 12), 7) == (8, 12)
    assert find_greater_than_x_even((4,), 3) == (4,)
    assert find_greater_than_x_even((), 3) is None
    assert find_greater_than_x_even((3, 5, 7, 9), 8) is None


# 489. Тесты для функции `unique_elements_from_list`:
def test_unique_elements_from_list():
    assert unique_elements_from_list([1, 2, 2, 3, 4, 4, 5]) == (1, 2, 3, 4, 5)
    assert unique_elements_from_list([1, 1, 1, 1, 1]) == (1,)
    assert unique_elements_from_list([1, 2, 3, 4, 5]) == (1, 2, 3, 4, 5)
    assert unique_elements_from_list([]) is None
    assert unique_elements_from_list([1, 2, 3, 4, 4, 5, 5]) == (1, 2, 3, 4, 5)
    assert unique_elements_from_list([3, 3, 3, 2, 1, 1]) == (1, 2, 3)
    assert unique_elements_from_list([10, 9, 9, 10]) == (9, 10)
    assert unique_elements_from_list([5]) == (5,)
    assert unique_elements_from_list([4, 5, 6, 6, 7]) == (4, 5, 6, 7)


# 490. Тесты для функции `intersection_of_lists_2`:
def test_intersection_of_lists_2():
    assert intersection_of_lists_2([1, 2, 3], [3, 4, 5]) == [3]
    assert intersection_of_lists_2([1, 2, 2, 3], [3, 3, 4]) == [3]
    assert intersection_of_lists_2([1, 2, 3], [4, 5, 6]) is None
    assert intersection_of_lists_2([], [1, 2, 3]) is None
    assert intersection_of_lists_2([1, 2, 3], []) is None
    assert intersection_of_lists_2([1, 2, 3, 4], [2, 3, 4, 5]) == [2, 3, 4]
    assert intersection_of_lists_2([5, 6, 7], [7, 8, 9]) == [7]
    assert intersection_of_lists_2([1, 1, 2, 2], [2, 2, 3, 3]) == [2]
    assert intersection_of_lists_2([9, 8, 7], [7, 6, 5]) == [7]


# 491. Тесты для функции `merge_dicts_no_common_keys`:
def test_merge_dicts_no_common_keys():
    assert merge_dicts_no_common_keys({"a": 1, "b": 2}, {"c": 3, "d": 4}) == {"a": 1, "b": 2, "c": 3, "d": 4}
    assert merge_dicts_no_common_keys({"a": 1}, {"b": 2, "c": 3}) == {"a": 1, "b": 2, "c": 3}
    assert merge_dicts_no_common_keys({"a": 1, "b": 2}, {"b": 3, "d": 4}) is None
    assert merge_dicts_no_common_keys({}, {"a": 1, "b": 2}) == {"a": 1, "b": 2}
    assert merge_dicts_no_common_keys({"a": 1, "b": 2}, {}) == {"a": 1, "b": 2}
    assert merge_dicts_no_common_keys({}, {}) == {}
    assert merge_dicts_no_common_keys({"a": 1, "b": 2}, {"c": 2, "d": 3}) == {"a": 1, "b": 2, "c": 2, "d": 3}
    assert merge_dicts_no_common_keys({"a": 1}, {"a": 2}) is None
    assert merge_dicts_no_common_keys({"a": 1, "b": 2}, {"a": 2, "c": 3}) is None


# 492. Тесты для функции `reverse_string_3`:
def test_reverse_string_3():
    assert reverse_string_3("hello") == "olleh"
    assert reverse_string_3("world") == "dlrow"
    assert reverse_string_3("") is None
    assert reverse_string_3("a") == "a"
    assert reverse_string_3("ab") == "ba"
    assert reverse_string_3("abc") == "cba"
    assert reverse_string_3("racecar") == "racecar"
    assert reverse_string_3("Python") == "nohtyP"
    assert reverse_string_3("12345") == "54321"


# 493. Тесты для функции `divisors_of_x`:
def test_divisors_of_x():
    assert divisors_of_x(6) == [2, 3]
    assert divisors_of_x(12) == [2, 3, 4, 6]
    assert divisors_of_x(1) is None
    assert divisors_of_x(0) is None
    assert divisors_of_x(-5) is None
    assert divisors_of_x(17) is None
    assert divisors_of_x(100) == [2, 4, 5, 10, 20, 25, 50]
    assert divisors_of_x(25) == [5]
    assert divisors_of_x(2) is None


# 494. Тесты для функции `count_elements_in_list`:
def test_count_elements_in_list():
    assert count_elements_in_list([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
    assert count_elements_in_list([1, 1, 1, 1, 1]) == {1: 5}
    assert count_elements_in_list([]) is None
    assert count_elements_in_list([1, 2, 3, 4, 5]) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    assert count_elements_in_list([3, 3, 3]) == {3: 3}
    assert count_elements_in_list(["a", "b", "a", "c", "a", "b", "a"]) == {"a": 4, "b": 2, "c": 1}
    assert count_elements_in_list([None, None, None]) == {None: 3}
    assert count_elements_in_list([True, False, True, True]) == {True: 3, False: 1}
    assert count_elements_in_list([1, "1", 1, "1", 1]) == {1: 3, "1": 2}


# 495. Тесты для функции `list_to_dict_2`:
def test_list_to_dict_2():
    assert list_to_dict_2(["a", 1, "b", 2, "c", 3]) == {"a": 1, "b": 2, "c": 3}
    assert list_to_dict_2(["key1", "value1", "key2", "value2"]) == {"key1": "value1", "key2": "value2"}
    assert list_to_dict_2([]) is None
    assert list_to_dict_2(["a", 1, "b", 2, "c"]) is None
    assert list_to_dict_2(["a", 1]) == {"a": 1}
    assert list_to_dict_2(["one", 1, "two", 2, "three", 3]) == {"one": 1, "two": 2, "three": 3}
    assert list_to_dict_2([1, 2, 3, 4, 5, 6]) == {1: 2, 3: 4, 5: 6}
    assert list_to_dict_2(["apple", "red", "banana", "yellow"]) == {"apple": "red", "banana": "yellow"}
    assert list_to_dict_2(["name", "Alice", "age", 30]) == {"name": "Alice", "age": 30}


# 496. Тесты для функции `count_even_and_odd`:
def test_count_even_and_odd():
    assert count_even_and_odd([1, 2, 3, 4, 5, 6]) == {"even": 3, "odd": 3}
    assert count_even_and_odd([1, 3, 5, 7]) == {"even": 0, "odd": 4}
    assert count_even_and_odd([2, 4, 6, 8]) == {"even": 4, "odd": 0}
    assert count_even_and_odd([]) is None
    assert count_even_and_odd([1, 1, 1, 1]) == {"even": 0, "odd": 4}
    assert count_even_and_odd([2, 2, 2, 2]) == {"even": 4, "odd": 0}
    assert count_even_and_odd([1]) == {"even": 0, "odd": 1}
    assert count_even_and_odd([2]) == {"even": 1, "odd": 0}
    assert count_even_and_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == {"even": 5, "odd": 5}


# 497. Тесты для функции `extract_vowels_from_string`:
def test_extract_vowels_from_string():
    assert extract_vowels_from_string("hello") == "eo"
    assert extract_vowels_from_string("world") == "o"
    assert extract_vowels_from_string("") is None
    assert extract_vowels_from_string("a") == "a"
    assert extract_vowels_from_string("bcdfg") is None
    assert extract_vowels_from_string("AEIOU") == "AEIOU"
    assert extract_vowels_from_string("Python Programming") == 'ooai'
    assert extract_vowels_from_string("abcdefghijklmnopqrstuvwxyz") == "aeiou"
    assert extract_vowels_from_string("HELLO WORLD") == "EOO"


# 498. Тесты для функции `merge_sorted_lists`
def test_merge_sorted_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_lists([], []) is None
    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]
    assert merge_sorted_lists([], [4, 5, 6]) == [4, 5, 6]
    assert merge_sorted_lists([0], [0]) == [0, 0]
    assert merge_sorted_lists([10, 20], [5, 15, 25]) == [5, 10, 15, 20, 25]
    assert merge_sorted_lists([-1, -2], [-3, -4]) == [-4, -3, -2, -1]


# 499. Тесты для функции `is_palindrome_2`
def test_is_palindrome_2():
    assert is_palindrome_2('racecar') is True
    assert is_palindrome_2('') is None
    assert is_palindrome_2('madam') is True
    assert is_palindrome_2('python') is False
    assert is_palindrome_2('Aibohphobia') is False
    assert is_palindrome_2('step on no pets') is True
    assert is_palindrome_2('Was it a car or a cat I saw') is False
    assert is_palindrome_2('civic') is True


# 500. Тесты для функции `gcd_of_two_numbers`
def test_gcd_of_two_numbers():
    assert gcd_of_two_numbers(48, 18) == 6
    assert gcd_of_two_numbers(0, 10) is None
    assert gcd_of_two_numbers(15, 0) is None
    assert gcd_of_two_numbers(-5, 10) is None
    assert gcd_of_two_numbers(5, -10) is None
    assert gcd_of_two_numbers(36, 6) == 6
    assert gcd_of_two_numbers(101, 103) == 1
    assert gcd_of_two_numbers(56, 98) == 14
    assert gcd_of_two_numbers(14, 28) == 14


# 501. Тесты для функции `prime_numbers_up_to_x`
def test_prime_numbers_up_to_x():
    assert prime_numbers_up_to_x(10) == [2, 3, 5, 7]
    assert prime_numbers_up_to_x(2) == [2]
    assert prime_numbers_up_to_x(1) is None
    assert prime_numbers_up_to_x(0) is None
    assert prime_numbers_up_to_x(-5) is None
    assert prime_numbers_up_to_x(11) == [2, 3, 5, 7, 11]


# 502. Тесты для функции `factorial_of_number`
def test_factorial_of_number():
    assert factorial_of_number(5) == 120
    assert factorial_of_number(0) == 1
    assert factorial_of_number(-1) is None
    assert factorial_of_number(3) == 6
    assert factorial_of_number(1) == 1
    assert factorial_of_number(4) == 24


# 503. Тесты для функции `count_words_in_string`
def test_count_words_in_string():
    assert count_words_in_string("Hello world") == 2
    assert count_words_in_string("") is None
    assert count_words_in_string("A quick brown fox jumps over the lazy dog") == 9
    assert count_words_in_string(" ") == 0
    assert count_words_in_string("Testing, one, two, three.") == 4


# 504. Тесты для функции `find_all_indices_of_element`
def test_find_all_indices_of_element():
    assert find_all_indices_of_element([1, 2, 3, 2, 1], 2) == [1, 3]
    assert find_all_indices_of_element([1, 2, 3, 4, 5], 6) is None
    assert find_all_indices_of_element([], 1) is None
    assert find_all_indices_of_element([1, 1, 1, 1], 1) == [0, 1, 2, 3]
    assert find_all_indices_of_element(["a", "b", "a"], "a") == [0, 2]


# 505. Тесты для функции `square_numbers_from_list`
def test_square_numbers_from_list():
    assert square_numbers_from_list([1, 2, 3, 4, 5, 9]) == [1, 4, 9]
    assert square_numbers_from_list([]) is None
    assert square_numbers_from_list([10, 15, 20]) is None
    assert square_numbers_from_list([0, 1, 16, 25]) == [0, 1, 16, 25]
    assert square_numbers_from_list([1, 4, 9]) == [1, 4, 9]


# 506. Тесты для функции `greater_than_average`
def test_greater_than_average():
    assert greater_than_average([1, 2, 3, 4, 5]) == [4, 5]
    assert greater_than_average([10, 20, 30, 40, 50]) == [40, 50]
    assert greater_than_average([]) is None
    assert greater_than_average([5, 5, 5, 5]) is None
    assert greater_than_average([1, 2, 3, 3, 4]) == [3, 3, 4]


# 507. Тесты для функции `sort_strings_by_length`
def test_sort_strings_by_length():
    assert sort_strings_by_length(["a", "aaa", "aa"]) == ["a", "aa", "aaa"]
    assert sort_strings_by_length(["short", "longer", "longest"]) == ["short", "longer", "longest"]
    assert sort_strings_by_length([]) is None
    assert sort_strings_by_length(["same", "size"]) == ["same", "size"]
    assert sort_strings_by_length(["one", "three", "four"]) == ["one", "four", "three"]


# 508. Тесты для функции `sum_of_elements`
def test_sum_of_elements():
    assert sum_of_elements([1, 2, 3, 4, 5]) == 15
    assert sum_of_elements([]) is None
    assert sum_of_elements([10, 20, 30, 40]) == 100
    assert sum_of_elements([0, 0, 0, 0]) == 0
    assert sum_of_elements([-1, -2, -3, -4]) == -10


# 509. Тесты для функции `longest_string`
def test_longest_string():
    assert longest_string(["a", "aa", "aaa"]) == "aaa"
    assert longest_string(["short", "longer", "longest"]) == "longest"
    assert longest_string([]) is None
    assert longest_string(["same", "size"]) == "same"
    assert longest_string(["one", "three", "four"]) == "three"


# 510. Тесты для функции `difference_between_sets`
def test_difference_between_sets():
    assert difference_between_sets({1, 2, 3}, {2, 3, 4}) == {1}
    assert difference_between_sets(set(), {1, 2, 3}) is None
    assert difference_between_sets({1, 2, 3}, set()) is None
    assert difference_between_sets({1, 2, 3}, {1, 2, 3}) == set()
    assert difference_between_sets({1, 2}, {3, 4}) == {1, 2}


# 511. Тесты для функции `union_of_lists`
def test_union_of_lists():
    assert union_of_lists([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 4, 5]
    assert union_of_lists([], [1, 2, 3]) == [1, 2, 3]
    assert union_of_lists([1, 2, 3], []) == [1, 2, 3]
    assert union_of_lists([], []) is None
    assert union_of_lists([1, 1, 1], [2, 2, 2]) == [1, 2]


# 512. Тесты для функции `intersection_of_lists_3`
def test_intersection_of_lists_3():
    assert intersection_of_lists_3([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert intersection_of_lists_3([], [1, 2, 3]) == []
    assert intersection_of_lists_3([1, 2, 3], []) == []
    assert intersection_of_lists_3([], []) is None
    assert intersection_of_lists_3([1, 2, 2], [2, 2, 3]) == [2]


# 513. Тесты для функции `is_digit`
def test_is_digit():
    assert is_digit("123") is True
    assert is_digit("abc") is False
    assert is_digit("") is None
    assert is_digit("123abc") is False
    assert is_digit("0") is True


# 514. Тесты для функции `extract_letters_from_string`
def test_extract_letters_from_string():
    assert extract_letters_from_string("abc123") == "abc"
    assert extract_letters_from_string("") is None
    assert extract_letters_from_string("123") == ""
    assert extract_letters_from_string("a1b2c3") == "abc"
    assert extract_letters_from_string("!@#") == ""


# 515. Тесты для функции `find_all_strings_in_list`
def test_find_all_strings_in_list():
    assert find_all_strings_in_list([1, "a", 2, "b"]) == ["a", "b"]
    assert find_all_strings_in_list([]) is None
    assert find_all_strings_in_list([1, 2, 3]) == []
    assert find_all_strings_in_list(["a", "b", "c"]) == ["a", "b", "c"]
    assert find_all_strings_in_list([1, "one", 2, "two"]) == ["one", "two"]


# 516. Тесты для функции `all_unique`
def test_all_unique():
    assert all_unique([1, 2, 3]) is True
    assert all_unique([1, 1, 1]) is False
    assert all_unique([]) is None
    assert all_unique(["a", "b", "c"]) is True
    assert all_unique(["a", "b", "a"]) is False


# 517. Тесты для функции `join_elements_with_separator`
def test_join_elements_with_separator():
    assert join_elements_with_separator(["a", "b", "c"], "-") == "a-b-c"
    assert join_elements_with_separator([], "-") is None
    assert join_elements_with_separator(["one"], "-") == "one"
    assert join_elements_with_separator(["a", "b", "c"], "") == "abc"
    assert join_elements_with_separator(["1", "2", "3"], ", ") == "1, 2, 3"


# 518. Тесты для функции `difference_between_lists`
def test_difference_between_lists():
    assert difference_between_lists([1, 2, 3], [2, 3, 4]) == [1]
    assert difference_between_lists([], [1, 2, 3]) == []
    assert difference_between_lists([1, 2, 3], []) == [1, 2, 3]
    assert difference_between_lists([], []) is None
    assert difference_between_lists([1, 2, 3, 4], [3, 4]) == [1, 2]


# 519. Тесты для функции `count_non_overlapping_substring`
def test_count_non_overlapping_substring():
    assert count_non_overlapping_substring("ababab", "ab") == 3
    assert count_non_overlapping_substring("", "a") is None
    assert count_non_overlapping_substring("aaaa", "aa") == 2
    assert count_non_overlapping_substring("abc", "d") == 0
    assert count_non_overlapping_substring("abcdef", "abc") == 1


# 520. Тесты для функции `find_words_starting_with`
def test_find_words_starting_with():
    assert find_words_starting_with("apple banana apricot berry", "a") == ["apple", "apricot"]
    assert find_words_starting_with("", "a") is None
    assert find_words_starting_with("apple banana apricot berry", "b") == ["banana", "berry"]
    assert find_words_starting_with("apple banana apricot berry", "c") is None
    assert find_words_starting_with("cat cow car", "c") == ["cat", "cow", "car"]


# 521. Тесты для функции `are_anagrams_2`
def test_are_anagrams_2():
    assert are_anagrams_2("listen", "silent") is True
    assert are_anagrams_2("triangle", "integral") is True
    assert are_anagrams_2("apple", "pale") is False
    assert are_anagrams_2("", "") is None
    assert are_anagrams_2(None, "test") is None
    assert are_anagrams_2("test", None) is None


# 522. Тесты для функции `extract_numbers_from_string_2`
def test_extract_numbers_from_string_2():
    assert extract_numbers_from_string_2("abc123xyz456") == ["123", "456"]
    assert extract_numbers_from_string_2("no numbers here") is None
    assert extract_numbers_from_string_2("") is None
    assert extract_numbers_from_string_2(None) is None
    assert extract_numbers_from_string_2("123") == ["123"]
    assert extract_numbers_from_string_2("abc123") == ["123"]
    assert extract_numbers_from_string_2("123abc") == ["123"]


# 523. Тесты для функции `is_palindrome_with_spaces`
def test_is_palindrome_with_spaces():
    assert is_palindrome_with_spaces("A man a plan a canal Panama") is True
    assert is_palindrome_with_spaces("race car") is True
    assert is_palindrome_with_spaces("hello world") is False
    assert is_palindrome_with_spaces("") is None
    assert is_palindrome_with_spaces(None) is None
    assert is_palindrome_with_spaces("Was it a car or a cat I saw") is True


# 524. Тесты для функции `count_vowels_and_consonants`
def test_count_vowels_and_consonants():
    assert count_vowels_and_consonants("hello") == {"vowels": 2, "consonants": 3}
    assert count_vowels_and_consonants("a") == {"vowels": 1, "consonants": 0}
    assert count_vowels_and_consonants("bcdfg") == {"vowels": 0, "consonants": 5}
    assert count_vowels_and_consonants("12345") is None
    assert count_vowels_and_consonants("") is None
    assert count_vowels_and_consonants(None) is None


# 525. Тесты для функции `remove_spaces_and_reverse`
def test_remove_spaces_and_reverse():
    assert remove_spaces_and_reverse("hello world") == "dlrowolleh"
    assert remove_spaces_and_reverse(" ") == ""
    assert remove_spaces_and_reverse("a b c d e f") == "fedcba"
    assert remove_spaces_and_reverse("") is None
    assert remove_spaces_and_reverse(None) is None


# 526. Тесты для функции `longest_unique_substring`
def test_longest_unique_substring():
    assert longest_unique_substring("abcabcbb") == "abc"
    assert longest_unique_substring("bbbbb") == "b"
    assert longest_unique_substring("pwwkew") == "wke"
    assert longest_unique_substring("") is None
    assert longest_unique_substring(None) is None
    assert longest_unique_substring("abcdef") == "abcdef"


# 527. Тесты для функции `longest_common_prefix`
def test_longest_common_prefix():
    assert longest_common_prefix("flower", "flow") == "flow"
    assert longest_common_prefix("dog", "racecar") is None
    assert longest_common_prefix("", "") is None
    assert longest_common_prefix(None, "test") is None
    assert longest_common_prefix("test", None) is None
    assert longest_common_prefix("interspecies", "interstellar") == "inters"


# 528. Тесты для функции `count_repeating_words`
def test_count_repeating_words():
    assert count_repeating_words("hello Hello world world") == {"hello": 2, "world": 2}
    assert count_repeating_words("one two three") == {}
    assert count_repeating_words("") is None
    assert count_repeating_words(None) is None
    assert count_repeating_words("repeat repeat repeat") == {"repeat": 3}


# 529. Тесты для функции `longest_word_in_string`
def test_longest_word_in_string():
    assert longest_word_in_string("hello world") == "hello"
    assert longest_word_in_string("a abc ab") == "abc"
    assert longest_word_in_string("") is None
    assert longest_word_in_string(None) is None
    assert longest_word_in_string("single") == "single"


# 530. Тесты для функции `extract_substrings_of_length_n`
def test_extract_substrings_of_length_n():
    assert extract_substrings_of_length_n("abcdefg", 3) == ["abc", "bcd", "cde", "def", "efg"]
    assert extract_substrings_of_length_n("hello", 2) == ["he", "el", "ll", "lo"]
    assert extract_substrings_of_length_n("", 2) is None
    assert extract_substrings_of_length_n("a", 2) == []
    assert extract_substrings_of_length_n("test", 0) is None
    assert extract_substrings_of_length_n(None, 2) is None


# 531. Тесты для функции `remove_words_starting_with`
def test_remove_words_starting_with():
    assert remove_words_starting_with("hello world happy day", "h") == "world day"
    assert remove_words_starting_with("apple banana cherry", "b") == "apple cherry"
    assert remove_words_starting_with("alpha beta gamma", "a") == "beta gamma"
    assert remove_words_starting_with("", "a") is None
    assert remove_words_starting_with(None, "a") is None
    assert remove_words_starting_with("test string", "") is None
    assert remove_words_starting_with("test string", None) is None


# 532. Тесты для функции `replace_spaces_with_underscores`
def test_replace_spaces_with_underscores():
    assert replace_spaces_with_underscores("hello world") == "hello_world"
    assert replace_spaces_with_underscores(" a b c ") == "_a_b_c_"
    assert replace_spaces_with_underscores("") is None
    assert replace_spaces_with_underscores(None) is None
    assert replace_spaces_with_underscores("nospace") == "nospace"


# 533. Тесты для функции `sort_letters_in_string`
def test_sort_letters_in_string():
    assert sort_letters_in_string("dcba") == "abcd"
    assert sort_letters_in_string("hello") == "ehllo"
    assert sort_letters_in_string("h3el1lo2") == "ehllo"
    assert sort_letters_in_string("") is None
    assert sort_letters_in_string(None) is None


# 534. Тесты для функции `remove_numbers_from_string`
def test_remove_numbers_from_string():
    assert remove_numbers_from_string("a1b2c3") == "abc"
    assert remove_numbers_from_string("123") == ""
    assert remove_numbers_from_string("abc") == "abc"
    assert remove_numbers_from_string("") is None
    assert remove_numbers_from_string(None) is None


# 535. Тесты для функции `find_case_sensitive_occurrences`
def test_find_case_sensitive_occurrences():
    assert find_case_sensitive_occurrences("Test test TEST", "test") == [5]
    assert find_case_sensitive_occurrences("abcabcabc", "abc") == [0, 3, 6]
    assert find_case_sensitive_occurrences("Hello world", "o") == [4, 7]
    assert find_case_sensitive_occurrences("", "test") is None
    assert find_case_sensitive_occurrences(None, "test") is None
    assert find_case_sensitive_occurrences("Test", "") is None
    assert find_case_sensitive_occurrences("Test", None) is None


# 536. Тесты для функции `remove_vowels_from_string`
def test_remove_vowels_from_string():
    assert remove_vowels_from_string("hello") == "hll"
    assert remove_vowels_from_string("aeiou") == ""
    assert remove_vowels_from_string("bcdfg") == "bcdfg"
    assert remove_vowels_from_string("") is None
    assert remove_vowels_from_string(None) is None


# 537. Тесты для функции `levenshtein_distance`
def test_levenshtein_distance():
    assert levenshtein_distance("kitten", "sitting") == 3
    assert levenshtein_distance("flaw", "lawn") == 2
    assert levenshtein_distance("", "abc") is None
    assert levenshtein_distance("abc", "") is None
    assert levenshtein_distance(None, "abc") is None
    assert levenshtein_distance("abc", None) is None


# 538. Тесты для функции `fixed_length_substrings`
def test_fixed_length_substrings():
    assert fixed_length_substrings("abcdef", 2) == ["ab", "bc", "cd", "de", "ef"]
    assert fixed_length_substrings("abcdef", 3) == ["abc", "bcd", "cde", "def"]
    assert fixed_length_substrings("", 2) is None
    assert fixed_length_substrings("abc", 0) is None
    assert fixed_length_substrings(None, 2) is None


# 539. Тесты для функции `remove_duplicates_from_string`
def test_remove_duplicates_from_string():
    assert remove_duplicates_from_string("aabbcc") == "abc"
    assert remove_duplicates_from_string("abcabc") == "abc"
    assert remove_duplicates_from_string("abc") == "abc"
    assert remove_duplicates_from_string("") is None
    assert remove_duplicates_from_string(None) is None


# 540. Тесты для функции `average_of_floats`
def test_average_of_floats():
    assert average_of_floats([1.0, 2.0, 3.0]) == 2.0
    assert average_of_floats([1, 2, 3, 4]) == 2.5
    assert average_of_floats([1.0]) == 1.0
    assert average_of_floats([]) is None
    assert average_of_floats(None) is None
    assert average_of_floats([1.0, "a", 3.0]) is None
    assert average_of_floats(["a", "b", "c"]) is None


# 541. Тесты для функции `max_float`:
def test_max_float():
    assert max_float([1.2, 3.4, 5.6]) == 5.6
    assert max_float([-1.1, -2.2, -3.3]) == -1.1
    assert max_float([]) is None
    assert max_float([1, 2, 3.3, 'a', 0]) == 3.3
    assert max_float([1.1, -2, 0]) == 1.1


# 542. Тесты для функции `min_float`:
def test_min_float():
    assert min_float([1.2, 3.4, 5.6]) == 1.2
    assert min_float([-1.1, -2.2, -3.3]) == -3.3
    assert min_float([]) is None
    assert min_float([1, 2, 3.3, 'a', 0]) == 0
    assert min_float([1.1, -2, 0]) == -2


# 543. Тесты для функции `is_positive_float`:
def test_is_positive_float():
    assert is_positive_float(5.5) is True
    assert is_positive_float(-3.2) is False
    assert is_positive_float(0) is False
    assert is_positive_float('a') is None
    assert is_positive_float(None) is None


# 544. Тесты для функции `difference_between_floats`:
def test_difference_between_floats():
    assert difference_between_floats(5.5, 3.2) == 2.3
    assert difference_between_floats(-3.2, 5.5) == 8.7
    assert difference_between_floats(0, 0) == 0
    assert difference_between_floats('a', 3.2) is None
    assert difference_between_floats(5.5, None) is None


# 545. Тесты для функции `product_of_floats`:
def test_product_of_floats():
    assert product_of_floats([1.2, 3.4, 5.6]) == pytest.approx(22.848)
    assert product_of_floats([-1.1, -2.2, -3.3]) == pytest.approx(-7.986)
    assert product_of_floats([]) is None
    assert product_of_floats([1, 2, 3, 'a', 0]) is None
    assert product_of_floats([1.1, -2, 3]) == pytest.approx(-6.6)


# 546. Тесты для функции `divide_floats`:
def test_divide_floats():
    assert divide_floats(6.6, 3.3) == 2.0
    assert divide_floats(-6.6, 3.3) == -2.0
    assert divide_floats(6.6, 0) is None
    assert divide_floats('a', 3.3) is None
    assert divide_floats(6.6, None) is None


# 547. Тесты для функции `square_root`:
def test_square_root():
    assert square_root(4) == 2.0
    assert square_root(9) == 3.0
    assert square_root(-4) is None
    assert square_root('a') is None
    assert square_root(None) is None


# 548. Тесты для функции `round_to_nearest_integer`:
def test_round_to_nearest_integer():
    assert round_to_nearest_integer(4.4) == 4
    assert round_to_nearest_integer(4.5) == 4
    assert round_to_nearest_integer(4.6) == 5
    assert round_to_nearest_integer(-4.5) == -4
    assert round_to_nearest_integer('a') is None


# 549. Тесты для функции `divisible_by_x`:
def test_divisible_by_x():
    assert divisible_by_x([10, 20, 30], 10) == [10, 20, 30]
    assert divisible_by_x([10, 21, 30], 10) == [10, 30]
    assert divisible_by_x([10, 21, 33], 0) is None
    assert divisible_by_x(['a', 21, 33], 7) == [21]
    assert divisible_by_x([], 2) is None


# 550. Тесты для функции `exponentiation_of_float`:
def test_exponentiation_of_float():
    assert exponentiation_of_float(2, 3) == 8
    assert exponentiation_of_float(-2, 3) == -8
    assert exponentiation_of_float(2, -3) == 0.125
    assert exponentiation_of_float('a', 3) is None
    assert exponentiation_of_float(2, 'b') is None


# 551. Тесты для функции `factorial_of_float`:
def test_factorial_of_float():
    assert factorial_of_float(5) == 120
    assert factorial_of_float(0) == 1
    assert factorial_of_float(-1) is None
    assert factorial_of_float(3) == 6
    assert factorial_of_float('a') is None


# 552. Тесты для функции `median_of_floats`:
def test_median_of_floats():
    assert median_of_floats([1, 2, 3]) == 2
    assert median_of_floats([1, 2, 3, 4]) == 2.5
    assert median_of_floats([]) is None
    assert median_of_floats([1, 'a', 3]) == 2
    assert median_of_floats([-1, -2, -3]) == -2
    assert median_of_floats(['a', 'b', 'c']) is None


# 553. Тесты для функции `prime_floats`:
def test_prime_floats():
    assert prime_floats([2, 3, 4, 5]) == [2, 3, 5]
    assert prime_floats([2.2, 3.3, 5.5]) is None
    assert prime_floats([]) is None
    assert prime_floats([-2, -3, -5]) is None
    assert prime_floats([11, 13, 15]) == [11, 13]


# 554. Тесты для функции `numbers_in_range`:
def test_numbers_in_range():
    assert numbers_in_range(1, 5) == [1, 2, 3, 4, 5]
    assert numbers_in_range(5, 5) == [5]
    assert numbers_in_range('a', 5) is None
    assert numbers_in_range(1, 'b') is None
    assert numbers_in_range(10, 1) == []


# 555. Тесты для функции `geometric_progression`:
def test_geometric_progression():
    assert geometric_progression(2, 3, 4) == [2, 6, 18, 54]
    assert geometric_progression(1, 2, 5) == [1, 2, 4, 8, 16]
    assert geometric_progression(1, 1, 5) == [1, 1, 1, 1, 1]
    assert geometric_progression(1, 2, 0) is None
    assert geometric_progression('a', 2, 5) is None


# 556. Тесты для функции `sum_of_geometric_progression`:
def test_sum_of_geometric_progression():
    assert sum_of_geometric_progression(2, 3, 4) == 80
    assert sum_of_geometric_progression(1, 2, 5) == 31
    assert sum_of_geometric_progression(1, 1, 5) == 5
    assert sum_of_geometric_progression(1, 2, 0) is None
    assert sum_of_geometric_progression('a', 2, 5) is None


# 557. Тесты для функции `square_of_float`:
def test_square_of_float():
    assert square_of_float(2) == 4
    assert square_of_float(-3) == 9
    assert square_of_float(0) == 0
    assert square_of_float('a') is None
    assert square_of_float(None) is None


# 558. Тесты для функции `sum_of_arithmetic_progression`:
def test_sum_of_arithmetic_progression():
    assert sum_of_arithmetic_progression(2, 3, 4) == 26
    assert sum_of_arithmetic_progression(1, 1, 5) == 15
    assert sum_of_arithmetic_progression(0, 0, 5) == 0
    assert sum_of_arithmetic_progression('a', 1, 5) is None
    assert sum_of_arithmetic_progression(1, 1, -5) is None


# 559. Тесты для функции `non_zero_floats`:
def test_non_zero_floats():
    assert non_zero_floats([1.2, 0, 3.4, 5.6]) == [1.2, 3.4, 5.6]
    assert non_zero_floats([-1.1, 0, -3.3]) == [-1.1, -3.3]
    assert non_zero_floats([]) is None
    assert non_zero_floats([0, 0, 0]) == []
    assert non_zero_floats([1.1, 'a', 3.3, 0]) == [1.1, 3.3]


# 560. Тесты для функции `squares_greater_than`:
def test_squares_greater_than():
    assert squares_greater_than([1, 2, 3], 4) == [3]
    assert squares_greater_than([-3, 1, 4], 9) == [4]
    assert squares_greater_than([], 4) is None
    assert squares_greater_than([3, 'a', 4], 9) == [4]
    assert squares_greater_than([4, 5, 6], 16) == [5, 6]


# 561. Тесты для функции `less_than_value`
def test_less_than_value():
    assert less_than_value([1, 2, 3, 4], 3) == [1, 2]
    assert less_than_value([5, 6, 7], 10) == [5, 6, 7]
    assert less_than_value([], 5) is None
    assert less_than_value([1, 2, "three"], 3) == [1, 2]
    assert less_than_value([1, 2], "three") is None
    assert less_than_value([1, 2, 3.5], 3.5) == [1, 2]


# 562. Тесты для функции `sum_of_squares_2`
def test_sum_of_squares_2():
    assert sum_of_squares_2([1, 2, 3]) == 14
    assert sum_of_squares_2([]) is None
    assert sum_of_squares_2([2, -2, 2.5]) == 14.25
    assert sum_of_squares_2(["one", 2, 3]) == 13
    assert sum_of_squares_2([0, -2, 5]) == 29
    assert sum_of_squares_2([3.5]) == 12.25


# 563. Тесты для функции `positive_max_min_difference`
def test_positive_max_min_difference():
    assert positive_max_min_difference([1, 2, 3]) == 2
    assert positive_max_min_difference([-1, -2, -3]) is None
    assert positive_max_min_difference([1, -1, 2, 3]) == 2
    assert positive_max_min_difference([0, 2, 5, 3]) == 3
    assert positive_max_min_difference([]) is None
    assert positive_max_min_difference(["one", 2, 3]) == 1


# 564. Тесты для функции `negative_max_min_difference`
def test_negative_max_min_difference():
    assert negative_max_min_difference([-1, -2, -3]) == 2
    assert negative_max_min_difference([1, 2, 3]) is None
    assert negative_max_min_difference([-1, 1, -2, -3]) == 2
    assert negative_max_min_difference([0, -2, -5, -3]) == 3
    assert negative_max_min_difference([]) is None
    assert negative_max_min_difference(["minus one", -2, -3]) == 1


# 565. Тесты для функции `sum_of_divisible_by_x`
def test_sum_of_divisible_by_x():
    assert sum_of_divisible_by_x([1, 2, 3, 4], 2) == 10
    assert sum_of_divisible_by_x([1, 3, 5, 7], 2) == 16
    assert sum_of_divisible_by_x([], 2) is None
    assert sum_of_divisible_by_x([1, 2, "three"], 2) == 3
    assert sum_of_divisible_by_x([1, 2, 3], "two") is None
    assert sum_of_divisible_by_x([4, 8, 12], 4) == 24


# 566. Тесты для функции `cubes`
def test_cubes():
    assert cubes([1, 8, 27]) == [1, 8, 27]
    assert cubes([]) is None
    assert cubes([1, 2, 3, 8]) == [1, 8]
    assert cubes(["one", 8, 27]) == [8, 27]
    assert cubes([8, 8]) == [8, 8]
    assert cubes([27.0]) == [27.0]


# 567. Тесты для функции `sum_of_two_squares_3`
def test_sum_of_two_squares_3():
    assert sum_of_two_squares_3([5, 4, 10, 13]) == [5, 5, 4, 4, 10, 10, 13, 13]
    assert sum_of_two_squares_3([]) is None
    assert sum_of_two_squares_3([8, 1, 2]) == [8, 1, 1, 2]
    assert sum_of_two_squares_3([1, 2, "three"]) == [1, 1, 2]
    assert sum_of_two_squares_3([5, 25]) == [5, 5, 25, 25, 25, 25]
    assert sum_of_two_squares_3([0, 3, 9]) == [0, 9, 9]


# 568. Тесты для функции `is_power_of_two`
def test_is_power_of_two():
    assert is_power_of_two(1) is True
    assert is_power_of_two(2) is True
    assert is_power_of_two(3) is False
    assert is_power_of_two(16) is True
    assert is_power_of_two(-2) is False
    assert is_power_of_two(4) is True


# 569. Тесты для функции `integers_in_float_list`
def test_integers_in_float_list():
    assert integers_in_float_list([1.0, 2.0, 3.5, 4]) == [1.0, 2.0, 4]
    assert integers_in_float_list([]) is None
    assert integers_in_float_list([1.1, 2.2, 3.3]) == []
    assert integers_in_float_list([1, 2, "three"]) == [1, 2]
    assert integers_in_float_list([0.0, 2.0, 5]) == [0.0, 2.0, 5]
    assert integers_in_float_list([4, 4.0]) == [4, 4.0]


# 570. Тесты для функции `sum_of_products_of_primes`
def test_sum_of_products_of_primes():
    assert sum_of_products_of_primes([6, 10, 15, 21]) == 52
    assert sum_of_products_of_primes([]) is None
    assert sum_of_products_of_primes([1, 2, 3]) is None
    assert sum_of_products_of_primes(["six", 10, 15]) == 25
    assert sum_of_products_of_primes([6, 10]) == 16
    assert sum_of_products_of_primes([25.0, 49]) == 74
    assert sum_of_products_of_primes([1025, 34, 234]) == 34


# 571. Тесты для функции `difference_of_two_squares`
def test_difference_of_two_squares():
    assert difference_of_two_squares([3, 4, 5, 7]) == [3, 4, 5, 7]
    assert difference_of_two_squares([]) is None
    assert difference_of_two_squares([1, 2, 4]) == [1, 4]
    assert difference_of_two_squares([4, 8, 12, 16, 25, 0]) == [4, 8, 12, 16, 25]
    assert difference_of_two_squares(["two", 4, 5]) == [4, 5]
    assert difference_of_two_squares([10]) is None


# 572. Тесты для функции `cubes_of_numbers`
def test_cubes_of_numbers():
    assert cubes_of_numbers([1, 8, 27]) == [1, 8, 27]
    assert cubes_of_numbers([]) is None
    assert cubes_of_numbers([1, 2, 3, 8]) == [1, 8]
    assert cubes_of_numbers(["one", 8, 27]) == [8, 27]
    assert cubes_of_numbers([5, 8]) == [8]
    assert cubes_of_numbers([27.0]) == [27.0]


# 573. Тесты для функции `average_of_squares`
def test_average_of_squares():
    assert average_of_squares([1, 2, 3]) == 4.666666666666667
    assert average_of_squares([]) is None
    assert average_of_squares([2, 2, 2.5]) == 4.75
    assert average_of_squares(["one", 2, 3]) == 4.333333333333333
    assert average_of_squares([0, -2, 5]) == 9.666666666666666
    assert average_of_squares([3.5]) == 12.25


# 574. Тесты для функции `factorial_2`
def test_factorial_2():
    assert factorial_2(5) == 120
    assert factorial_2(0) == 1
    assert factorial_2(2) == 2
    assert factorial_2(4) == 24


# 575. Тесты для функции `sum_to_n`
def test_sum_to_n():
    assert sum_to_n(5) == 15
    assert sum_to_n(0) == 0
    assert sum_to_n(1) == 1
    assert sum_to_n(-1) == 0
    assert sum_to_n(10) == 55
    assert sum_to_n(2) == 3


# 576. Тесты для функции `fibonacci_2`
def test_fibonacci_2():
    assert fibonacci_2(0) == 0
    assert fibonacci_2(1) == 1
    assert fibonacci_2(2) == 1
    assert fibonacci_2(3) == 2
    assert fibonacci_2(4) == 3
    assert fibonacci_2(5) == 5


# 577. Тесты для функции `power_2`
def test_power_2():
    assert power_2(2, 3) == 8
    assert power_2(5, 0) == 1
    assert power_2(2, -1) == 1
    assert power_2(3, 2) == 9
    assert power_2(4, 3) == 64
    assert power_2(-2, 3) == -8


# 578. Тесты для функции `recursive_sum`
def test_recursive_sum():
    assert recursive_sum([1, 2, 3]) == 6
    assert recursive_sum([]) == 0
    assert recursive_sum([2, -2, 2.5]) == 2.5
    assert recursive_sum([0, -2, 5]) == 3
    assert recursive_sum([3.5]) == 3.5


# 579. Тесты для функции `recursive_product`
def test_recursive_product():
    assert recursive_product([1, 2, 3]) == 6
    assert recursive_product([]) == 1
    assert recursive_product([2, -2, 2.5]) == -10
    assert recursive_product(["one", 2, 3]) == 'oneoneoneoneoneone'
    assert recursive_product([0, -2, 5]) == 0
    assert recursive_product([3.5]) == 3.5


# 580. Тесты для функции `recursive_max`
def test_recursive_max():
    assert recursive_max([1, 2, 3]) == 3
    assert recursive_max([3, 2, 1]) == 3
    assert recursive_max([-1, -2, -3]) == -1
    assert recursive_max([2, 0, 4, 3]) == 4
    assert recursive_max([5]) == 5
    assert recursive_max([3.5, 2.5, 1.5]) == 3.5


# 581. Тесты для функции `recursive_min`:
def test_recursive_min():
    assert recursive_min([5]) == 5
    assert recursive_min([3, 1, 4, 1, 5, 9]) == 1
    assert recursive_min([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert recursive_min([0, -1, -2, -3, -4]) == -4
    assert recursive_min([-3, -1, -4, -2, -5]) == -5
    assert recursive_min([1, 2, 3, 4, 5]) == 1
    assert recursive_min([100, 99, 98, 97]) == 97
    assert recursive_min([10, 20, 30, 40]) == 10
    assert recursive_min([42, 23, 34, 45, 56]) == 23


# 582. Тесты для функции `reverse_string_2`:
def test_reverse_string_2():
    assert reverse_string_2('') == ''
    assert reverse_string_2('hello') == 'olleh'
    assert reverse_string_2('python') == 'nohtyp'
    assert reverse_string_2('a') == 'a'
    assert reverse_string_2('racecar') == 'racecar'
    assert reverse_string_2('level') == 'level'
    assert reverse_string_2('12345') == '54321'
    assert reverse_string_2('abcdefg') == 'gfedcba'
    assert reverse_string_2('!@#$%^&*()') == ')(*&^%$#@!'


# 583. Тесты для функции `is_palindrome_4`:
def test_is_palindrome_4():
    assert is_palindrome_4('') is True
    assert is_palindrome_4('a') is True
    assert is_palindrome_4('racecar') is True
    assert is_palindrome_4('level') is True
    assert is_palindrome_4('hello') is False
    assert is_palindrome_4('world') is False
    assert is_palindrome_4('madam') is True
    assert is_palindrome_4('noon') is True
    assert is_palindrome_4('palindrome') is False


# 584. Тесты для функции `gsd_2`:
def test_gsd_2():
    assert gsd_2(54, 24) == 6
    assert gsd_2(48, 18) == 6
    assert gsd_2(101, 10) == 1
    assert gsd_2(0, 10) == 10
    assert gsd_2(10, 0) == 10
    assert gsd_2(10, 5) == 5
    assert gsd_2(7, 3) == 1
    assert gsd_2(50, 100) == 50
    assert gsd_2(37, 600) == 1


# 585. Тесты для функции `count_occurrences_3`:
def test_count_occurrences_3():
    assert count_occurrences_3([1, 2, 3, 4, 1, 2, 1], 1) == 3
    assert count_occurrences_3([1, 2, 3, 4, 5], 6) == 0
    assert count_occurrences_3([1, 1, 1, 1], 1) == 4
    assert count_occurrences_3([], 1) == 0
    assert count_occurrences_3([2, 3, 4, 5], 1) == 0
    assert count_occurrences_3([5, 5, 5, 5, 5], 5) == 5
    assert count_occurrences_3([0, 0, 0, 0], 0) == 4
    assert count_occurrences_3([-1, -1, -1], -1) == 3
    assert count_occurrences_3([1, 2, 3], 2) == 1


# 586. Тесты для функции `is_prime_4`:
def test_is_prime_4():
    assert is_prime_4(2) is True
    assert is_prime_4(3) is True
    assert is_prime_4(4) is False
    assert is_prime_4(17) is True
    assert is_prime_4(20) is False
    assert is_prime_4(1) is False
    assert is_prime_4(0) is False
    assert is_prime_4(-5) is False
    assert is_prime_4(23) is True


# 587. Тесты для функции `find_max_in_tree`:
def test_find_max_in_tree():
    assert find_max_in_tree({'value': 5, 'left': {'value': 3}, 'right': {'value': 7}}) == 7
    assert find_max_in_tree({'value': 10, 'left': None, 'right': {'value': 20}}) == 20
    assert find_max_in_tree({'value': -1, 'left': {'value': -3}, 'right': {'value': -2}}) == -1
    assert find_max_in_tree({'value': 42}) == 42
    assert find_max_in_tree({'value': -100, 'left': None, 'right': None}) == -100
    assert find_max_in_tree(None) == float('-inf')
    assert find_max_in_tree({'value': 0, 'left': {'value': -5}, 'right': {'value': 5}}) == 5
    assert find_max_in_tree({'value': 6, 'left': {'value': 6}, 'right': {'value': 6}}) == 6
    assert find_max_in_tree({'value': -50, 'left': {'value': -60}, 'right': {'value': -70}}) == -50


# 588. Тесты для функции `is_even_2`:
def test_is_even_2():
    assert is_even_2(0) is True
    assert is_even_2(1) is False
    assert is_even_2(2) is True
    assert is_even_2(3) is False
    assert is_even_2(4) is True
    assert is_even_2(5) is False
    assert is_even_2(-2) is True
    assert is_even_2(-3) is False
    assert is_even_2(100) is True


# 589. Тесты для функции `sum_less_than_x`:
def test_sum_less_than_x():
    assert sum_less_than_x([1, 2, 3, 4, 5], 3) == 3
    assert sum_less_than_x([10, 20, 30, 40, 50], 25) == 30
    assert sum_less_than_x([5, 5, 5, 5, 5], 10) == 25
    assert sum_less_than_x([], 5) == 0
    assert sum_less_than_x([1, 2, 3, 4, 5], 0) == 0
    assert sum_less_than_x([-1, -2, -3, 4, 5], 0) == -6
    assert sum_less_than_x([100, 200, 300], 150) == 100
    assert sum_less_than_x([1, 1, 1, 1, 1], 2) == 5
    assert sum_less_than_x([6, 7, 8, 9, 10], 5) == 0


# 590. Тесты для функции `factorial_tail`:
def test_factorial_tail():
    assert factorial_tail(5) == 120
    assert factorial_tail(0) == 1
    assert factorial_tail(1) == 1
    assert factorial_tail(3) == 6
    assert factorial_tail(4) == 24
    assert factorial_tail(6) == 720
    assert factorial_tail(2) == 2
    assert factorial_tail(7) == 5040
    assert factorial_tail(8) == 40320


# 591. Тесты для функции `sum_with_step`:
def test_sum_with_step():
    assert sum_with_step(10) == 30
    assert sum_with_step(1) == 1
    assert sum_with_step(0) == 0
    assert sum_with_step(2) == 2
    assert sum_with_step(3) == 4
    assert sum_with_step(4) == 6
    assert sum_with_step(5) == 9
    assert sum_with_step(6) == 12
    assert sum_with_step(7) == 16


# 592. Тесты для функции `fibonacci_up_to_n`:
def test_fibonacci_up_to_n():
    assert fibonacci_up_to_n(0) == [0]
    assert fibonacci_up_to_n(1) == [0, 1, 1]
    assert fibonacci_up_to_n(2) == [0, 1, 1, 2]
    assert fibonacci_up_to_n(5) == [0, 1, 1, 2, 3, 5]
    assert fibonacci_up_to_n(10) == [0, 1, 1, 2, 3, 5, 8]
    assert fibonacci_up_to_n(15) == [0, 1, 1, 2, 3, 5, 8, 13]
    assert fibonacci_up_to_n(20) == [0, 1, 1, 2, 3, 5, 8, 13]
    assert fibonacci_up_to_n(25) == [0, 1, 1, 2, 3, 5, 8, 13, 21]
    assert fibonacci_up_to_n(30) == [0, 1, 1, 2, 3, 5, 8, 13, 21]


# 593. Тесты для функции `find_divisible`:
def test_find_divisible():
    assert find_divisible([1, 2, 3, 4, 5], 2) == [2, 4]
    assert find_divisible([10, 20, 30, 40, 50], 10) == [10, 20, 30, 40, 50]
    assert find_divisible([5, 7, 11], 2) == []
    assert find_divisible([], 5) == []
    assert find_divisible([1, 2, 3, 4, 5], 3) == [3]
    assert find_divisible([9, 12, 15, 18, 21], 3) == [9, 12, 15, 18, 21]
    assert find_divisible([100, 200, 300], 100) == [100, 200, 300]
    assert find_divisible([1, 1, 1, 1], 1) == [1, 1, 1, 1]
    assert find_divisible([6, 7, 8, 9, 10], 2) == [6, 8, 10]


# 594. Тесты для функции `count_even`:
def test_count_even():
    assert count_even([1, 2, 3, 4, 5]) == 2
    assert count_even([10, 20, 30, 40, 50]) == 5
    assert count_even([5, 7, 11]) == 0
    assert count_even([5]) == 0
    assert count_even([1, 3, 5, 7, 9]) == 0
    assert count_even([2, 4, 6, 8, 10]) == 5
    assert count_even([100, 200, 300]) == 3
    assert count_even([0, 0, 0, 0]) == 4
    assert count_even([-2, -4, -6]) == 3


# 595. Тесты для функции `count_negatives`:
def test_count_negatives():
    assert count_negatives([-1, -2, -3, 4, 5]) == 3
    assert count_negatives([-10, -20, -30, -40, -50]) == 5
    assert count_negatives([5, 7, 11]) == 0
    assert count_negatives([]) == 0
    assert count_negatives([1, 2, 3, 4, 5]) == 0
    assert count_negatives([-1, -2, -3, -4, -5]) == 5
    assert count_negatives([-100, -200, -300]) == 3
    assert count_negatives([0, 0, 0, 0]) == 0
    assert count_negatives([-2, -4, 6, 8, 10]) == 2


# 596. Тесты для функции `greater_than_average_3`:
def test_greater_than_average_3():
    assert greater_than_average_3([1, 2, 3, 4, 5]) == [4, 5]
    assert greater_than_average_3([10, 20, 30, 40, 50]) == [40, 50]
    assert greater_than_average_3([5, 7, 11, 13, 15]) == [11, 13, 15]
    assert greater_than_average_3([]) == []
    assert greater_than_average_3([1, 2, 3, 4]) == [3, 4]
    assert greater_than_average_3([10, 20, 30]) == [30]
    assert greater_than_average_3([0, 1, 2, 3]) == [2, 3]
    assert greater_than_average_3([-1, -2, -3, 0]) == [-1, 0]
    assert greater_than_average_3([6, 7, 8, 9, 10]) == [9, 10]


# 597. Тесты для функции `sum_greater_than_x`:
def test_sum_greater_than_x():
    assert sum_greater_than_x([1, 2, 3, 4, 5], 3) == 9
    assert sum_greater_than_x([10, 20, 30, 40, 50], 25) == 120
    assert sum_greater_than_x([5, 5, 5, 5, 5], 10) == 0
    assert sum_greater_than_x([], 5) == 0
    assert sum_greater_than_x([1, 2, 3, 4, 5], 5) == 0
    assert sum_greater_than_x([-1, -2, -3, 4, 5], 0) == 9
    assert sum_greater_than_x([100, 200, 300], 150) == 500
    assert sum_greater_than_x([1, 1, 1, 1, 1], 2) == 0
    assert sum_greater_than_x([6, 7, 8, 9, 10], 5) == 40


# 598. Тесты для функции `string_length`:
def test_string_length():
    assert string_length("") == 0
    assert string_length("hello") == 5
    assert string_length("a") == 1
    assert string_length("Python") == 6
    assert string_length("length") == 6
    assert string_length("test") == 4
    assert string_length("pytest") == 6
    assert string_length("recursion") == 9
    assert string_length("1234567890") == 10


# 599. Тесты для функции `count_evens_in_range`:
def test_count_evens_in_range():
    assert count_evens_in_range(0) == 0
    assert count_evens_in_range(1) == 0
    assert count_evens_in_range(2) == 1
    assert count_evens_in_range(3) == 1
    assert count_evens_in_range(4) == 2
    assert count_evens_in_range(5) == 2
    assert count_evens_in_range(6) == 3
    assert count_evens_in_range(10) == 5
    assert count_evens_in_range(15) == 7


# 600. Тесты для функции `sum_in_range`:
def test_sum_in_range():
    assert sum_in_range([1, 2, 3, 4, 5], 2, 4) == 9
    assert sum_in_range([10, 20, 30, 40, 50], 15, 35) == 50
    assert sum_in_range([5, 5, 5, 5, 5], 5, 5) == 25
    assert sum_in_range([], 5, 10) == 0
    assert sum_in_range([1, 2, 3, 4, 5], 0, 2) == 3
    assert sum_in_range([1, 2, 3, 4, 5], 4, 6) == 9
    assert sum_in_range([1, 2, 3, 4, 5], 10, 20) == 0
    assert sum_in_range([1, 5, 9, 13, 17], 5, 15) == 27
    assert sum_in_range([-1, -2, -3, 4, 5], -3, 3) == -6


# 601. Тесты для функции `product_less_than_x`:
def test_product_less_than_x():
    assert product_less_than_x([2, 3, 4], 3) == 2
    assert product_less_than_x([1, 2, 3, 4], 5) == 24
    assert product_less_than_x([], 5) == 1
    assert product_less_than_x([5, 6, 7], 5) == 1
    assert product_less_than_x([1, 2, 0, 4], 5) == 0
    assert product_less_than_x([2, 3, 4], 2) == 1
    assert product_less_than_x([4, 5, 6, 1], 4) == 1
    assert product_less_than_x([-1, -2, -3], 0) == -6
    assert product_less_than_x([4, 0, 3], 1) == 0


# 602. Тесты для функции `sum_of_numbers_in_string`:
def test_sum_of_numbers_in_string():
    assert sum_of_numbers_in_string("123abc") == 369
    assert sum_of_numbers_in_string("abc123") == 0
    assert sum_of_numbers_in_string("abc123def") == 369
    assert sum_of_numbers_in_string("123abc456") == 369
    assert sum_of_numbers_in_string("") == 0
    assert sum_of_numbers_in_string("abc") == 0
    assert sum_of_numbers_in_string("12a34b56") == 1246
    assert sum_of_numbers_in_string("0") == 0
    assert sum_of_numbers_in_string("1a1b1c") == 123


# 603. Тесты для функции `even_numbers_in_string`:
def test_even_numbers_in_string():
    assert even_numbers_in_string("1234") == []
    assert even_numbers_in_string("abc") == []
    assert even_numbers_in_string("2468") == []
    assert even_numbers_in_string("1357") == []
    assert even_numbers_in_string("1a2b3c4d") == [12, 1234]
    assert even_numbers_in_string("abcdefg") == []
    assert even_numbers_in_string("0") == []
    assert even_numbers_in_string("a1b2c3d4") == [12]
    assert even_numbers_in_string("123456") == []


# 604. Тесты для функции `append_to_ring`:
def test_append_to_ring():
    assert append_to_ring([1, 2, 3], 4) == [1, 2, 3, 4]
    assert append_to_ring([1, 2, 3, 4, 5], 6, 5) == [2, 3, 4, 5, 6]
    assert append_to_ring([], 1, 3) == [1]
    assert append_to_ring([1, 2, 3, 4], 5, 3) == [3, 4, 5]
    assert append_to_ring([1, 2], 3) == [1, 2, 3]
    assert append_to_ring([1, 2, 3], 4, 3) == [2, 3, 4]
    assert append_to_ring([1], 2, 1) == [2]
    assert append_to_ring([1, 2], 3, 1) == [3]
    assert append_to_ring([1, 2], 3, 2) == [2, 3]


# 605. Тесты для функции `find_in_ring`:
def test_find_in_ring():
    assert find_in_ring([1, 2, 3], 2) == 1
    assert find_in_ring([1, 2, 3], 4) is None
    assert find_in_ring([], 1) is None
    assert find_in_ring([1, 2, 3, 1], 1) == 0
    assert find_in_ring([1, 2, 3, 4, 5], 5) == 4
    assert find_in_ring([1, 2, 3, 4, 5], 6) is None
    assert find_in_ring([1, 1, 1, 1], 1) == 0
    assert find_in_ring([1, 2, 3], 1) == 0
    assert find_in_ring([1, 2, 3], 3) == 2


# 606. Тесты для функции `find_all_in_ring`:
def test_find_all_in_ring():
    assert find_all_in_ring([1, 2, 3, 1], 1) == [0, 3]
    assert find_all_in_ring([1, 2, 3], 4) == []
    assert find_all_in_ring([], 1) == []
    assert find_all_in_ring([1, 2, 3, 1, 2, 3], 2) == [1, 4]
    assert find_all_in_ring([1, 1, 1, 1], 1) == [0, 1, 2, 3]
    assert find_all_in_ring([1, 2, 3, 4, 5], 5) == [4]
    assert find_all_in_ring([1, 2, 3, 4, 5], 6) == []
    assert find_all_in_ring([1, 2, 3, 3], 3) == [2, 3]
    assert find_all_in_ring([1, 2, 3, 3], 1) == [0]


# 607. Тесты для функции `rotate_with_negativity`:
def test_rotate_with_negativity():
    assert rotate_with_negativity([1, 2, 3], 1) == [3, 1, 2]
    assert rotate_with_negativity([1, 2, 3], -1) == [3, 1, 2]
    assert rotate_with_negativity([], 1) == []
    assert rotate_with_negativity([1, 2, 3, 4], 2) == [3, 4, 1, 2]
    assert rotate_with_negativity([1, 2, 3], 3) == [1, 2, 3]
    assert rotate_with_negativity([1, 2, 3], 0) == [1, 2, 3]
    assert rotate_with_negativity([1, 2, 3], -3) == [1, 2, 3]
    assert rotate_with_negativity([1, 2, 3], -2) == [2, 3, 1]
    assert rotate_with_negativity([1, 2, 3, 4], -1) == [4, 1, 2, 3]


# 608. Тесты для функции `increase_ring_elements`:
def test_increase_ring_elements():
    assert increase_ring_elements([1, 2, 3], 1) == [2, 3, 4]
    assert increase_ring_elements([], 1) == []
    assert increase_ring_elements([0], 1) == [1]
    assert increase_ring_elements([1, 2, 3], -1) == [0, 1, 2]
    assert increase_ring_elements([1, 2, 3], 0) == [1, 2, 3]
    assert increase_ring_elements([1, 2, 3], 2) == [3, 4, 5]
    assert increase_ring_elements([1, -2, 3], 1) == [2, -1, 4]
    assert increase_ring_elements([-1, -2, -3], 1) == [0, -1, -2]
    assert increase_ring_elements([1, 1, 1], 1) == [2, 2, 2]


# 609. Тесты для функции `decrease_ring_elements`:
def test_decrease_ring_elements():
    assert decrease_ring_elements([1, 2, 3], 1) == [0, 1, 2]
    assert decrease_ring_elements([], 1) == []
    assert decrease_ring_elements([0], 1) == [-1]
    assert decrease_ring_elements([1, 2, 3], -1) == [2, 3, 4]
    assert decrease_ring_elements([1, 2, 3], 0) == [1, 2, 3]
    assert decrease_ring_elements([1, 2, 3], 2) == [-1, 0, 1]
    assert decrease_ring_elements([1, -2, 3], 1) == [0, -3, 2]
    assert decrease_ring_elements([-1, -2, -3], 1) == [-2, -3, -4]
    assert decrease_ring_elements([1, 1, 1], 1) == [0, 0, 0]


# 610. Тесты для функции `multiply_ring_elements`:
def test_multiply_ring_elements():
    assert multiply_ring_elements([1, 2, 3], 2) == [2, 4, 6]
    assert multiply_ring_elements([], 2) == []
    assert multiply_ring_elements([0], 2) == [0]
    assert multiply_ring_elements([1, 2, 3], 0) == [0, 0, 0]
    assert multiply_ring_elements([1, 2, 3], -1) == [-1, -2, -3]
    assert multiply_ring_elements([1, -2, 3], 2) == [2, -4, 6]
    assert multiply_ring_elements([-1, -2, -3], 2) == [-2, -4, -6]
    assert multiply_ring_elements([1, 1, 1], 2) == [2, 2, 2]
    assert multiply_ring_elements([1, 2, 3], 1) == [1, 2, 3]


# 611. Тесты для функции `sum_ring`:
def test_sum_ring():
    assert sum_ring([1, 2, 3]) == 6
    assert sum_ring([]) == 0
    assert sum_ring([0]) == 0
    assert sum_ring([-1, -2, -3]) == -6
    assert sum_ring([1, -1, 2, -2]) == 0
    assert sum_ring([5, 5, 5, 5]) == 20
    assert sum_ring([10]) == 10
    assert sum_ring([-1, -1, 1, 1]) == 0
    assert sum_ring([1, 2, 3, 4, 5]) == 15


# 612. Тесты для функции `average_ring`:
def test_average_ring():
    assert average_ring([1, 2, 3]) == 2
    assert average_ring([]) is None
    assert average_ring([0]) == 0
    assert average_ring([-1, -2, -3]) == -2
    assert average_ring([1, -1, 2, -2]) == 0
    assert average_ring([5, 5, 5, 5]) == 5
    assert average_ring([10]) == 10
    assert average_ring([-1, -1, 1, 1]) == 0
    assert average_ring([1, 2, 3, 4, 5]) == 3


# 613. Тесты для функции `max_ring`:
def test_max_ring():
    assert max_ring([1, 2, 3]) == 3
    assert max_ring([]) is None
    assert max_ring([0]) == 0
    assert max_ring([-1, -2, -3]) == -1
    assert max_ring([1, -1, 2, -2]) == 2
    assert max_ring([5, 5, 5, 5]) == 5
    assert max_ring([10]) == 10
    assert max_ring([-1, -1, 1, 1]) == 1
    assert max_ring([1, 2, 3, 4, 5]) == 5


# 614. Тесты для функции `min_ring`:
def test_min_ring():
    assert min_ring([1, 2, 3]) == 1
    assert min_ring([]) is None
    assert min_ring([0]) == 0
    assert min_ring([-1, -2, -3]) == -3
    assert min_ring([1, -1, 2, -2]) == -2
    assert min_ring([5, 5, 5, 5]) == 5
    assert min_ring([10]) == 10
    assert min_ring([-1, -1, 1, 1]) == -1
    assert min_ring([1, 2, 3, 4, 5]) == 1


# 615. Тесты для функции `has_positive_ring`:
def test_has_positive_ring():
    assert has_positive_ring([1, 2, 3]) is True
    assert has_positive_ring([]) is False
    assert has_positive_ring([0]) is False
    assert has_positive_ring([-1, -2, -3]) is False
    assert has_positive_ring([1, -1, 2, -2]) is True
    assert has_positive_ring([5, 5, 5, 5]) is True
    assert has_positive_ring([10]) is True
    assert has_positive_ring([-1, -1, -1, -1]) is False
    assert has_positive_ring([1, 2, 3, 4, 5]) is True


# 616. Тесты для функции `has_negative_ring`:
def test_has_negative_ring():
    assert has_negative_ring([1, 2, 3]) is False
    assert has_negative_ring([]) is False
    assert has_negative_ring([0]) is False
    assert has_negative_ring([-1, -2, -3]) is True
    assert has_negative_ring([1, -1, 2, -2]) is True
    assert has_negative_ring([5, 5, 5, 5]) is False
    assert has_negative_ring([10]) is False
    assert has_negative_ring([-1, -1, -1, -1]) is True
    assert has_negative_ring([1, 2, 3, 4, 5]) is False


# 617. Тесты для функции `reverse_even_index_elements`:
def test_reverse_even_index_elements():
    assert reverse_even_index_elements([1, 2, 3, 4]) == [4, 2, 2, 4]
    assert reverse_even_index_elements([]) == []
    assert reverse_even_index_elements([0]) == [0]
    assert reverse_even_index_elements([1, 2, 3, 4, 5]) == [5, 2, 3, 4, 1]
    assert reverse_even_index_elements([1, -1, 2, -2]) == [-2, -1, -1, -2]
    assert reverse_even_index_elements([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert reverse_even_index_elements([10]) == [10]
    assert reverse_even_index_elements([1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1]
    assert reverse_even_index_elements([1, 2, 3, 4, 5, 6]) == [6, 2, 4, 4, 2, 6]


# 618. Тесты для функции `find_even_ring`:
def test_find_even_ring():
    assert find_even_ring([1, 2, 3, 4]) == [2, 4]
    assert find_even_ring([]) == []
    assert find_even_ring([0]) == [0]
    assert find_even_ring([1, 3, 5]) == []
    assert find_even_ring([2, 4, 6]) == [2, 4, 6]
    assert find_even_ring([-2, -4, -6]) == [-2, -4, -6]
    assert find_even_ring([-1, -3, -5]) == []
    assert find_even_ring([1, 2, 3, 4, 5]) == [2, 4]
    assert find_even_ring([2, 2, 2, 2]) == [2, 2, 2, 2]


# 619. Тесты для функции `find_odd_ring`:
def test_find_odd_ring():
    assert find_odd_ring([1, 2, 3, 4]) == [1, 3]
    assert find_odd_ring([]) == []
    assert find_odd_ring([0]) == []
    assert find_odd_ring([1, 3, 5]) == [1, 3, 5]
    assert find_odd_ring([2, 4, 6]) == []
    assert find_odd_ring([-2, -4, -6]) == []
    assert find_odd_ring([-1, -3, -5]) == [-1, -3, -5]
    assert find_odd_ring([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert find_odd_ring([2, 2, 2, 2]) == []


# 620. Тесты для функции `count_even_ring`:
def test_count_even_ring():
    assert count_even_ring([1, 2, 3, 4]) == 2
    assert count_even_ring([]) == 0
    assert count_even_ring([0]) == 1
    assert count_even_ring([1, 3, 5]) == 0
    assert count_even_ring([2, 4, 6]) == 3
    assert count_even_ring([-2, -4, -6]) == 3
    assert count_even_ring([-1, -3, -5]) == 0
    assert count_even_ring([1, 2, 3, 4, 5]) == 2
    assert count_even_ring([2, 2, 2, 2]) == 4


# 621. Тесты для функции `count_odd_ring`:
def test_count_odd_ring():
    assert count_odd_ring([]) == 0
    assert count_odd_ring([1, 2, 3, 4, 5]) == 3
    assert count_odd_ring([2, 4, 6, 8]) == 0
    assert count_odd_ring([1, 3, 5, 7]) == 4
    assert count_odd_ring([0, 1, -1, -2]) == 2


# 622. Тесты для функции `append_unique_ring`:
def test_append_unique_ring():
    assert append_unique_ring([], 1) == [1]
    assert append_unique_ring([1, 2, 3], 2) == [1, 2, 3]
    assert append_unique_ring([1, 2, 3], 4) == [1, 2, 3, 4]
    assert append_unique_ring(['a', 'b'], 'a') == ['a', 'b']
    assert append_unique_ring(['a', 'b'], 'c') == ['a', 'b', 'c']


# 623. Тесты для функции `find_divisible_ring`:
def test_find_divisible_ring():
    assert find_divisible_ring([], 2) == []
    assert find_divisible_ring([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]
    assert find_divisible_ring([1, 3, 5], 2) == []
    assert find_divisible_ring([10, 20, 30], 10) == [10, 20, 30]
    assert find_divisible_ring([10, 25, 35], 5) == [10, 25, 35]


# 624. Тесты для функции `remove_less_than_ring`:
def test_remove_less_than_ring():
    assert remove_less_than_ring([], 10) == []
    assert remove_less_than_ring([1, 5, 10, 15], 10) == [10, 15]
    assert remove_less_than_ring([20, 25, 30], 20) == [20, 25, 30]
    assert remove_less_than_ring([1, 2, 3], 5) == []
    assert remove_less_than_ring([5, 5, 5], 5) == [5, 5, 5]


# 625. Тесты для функции `remove_greater_than_ring`:
def test_remove_greater_than_ring():
    assert remove_greater_than_ring([], 10) == []
    assert remove_greater_than_ring([1, 5, 10, 15], 10) == [1, 5, 10]
    assert remove_greater_than_ring([20, 25, 30], 20) == [20]
    assert remove_greater_than_ring([1, 2, 3], 5) == [1, 2, 3]
    assert remove_greater_than_ring([5, 5, 5], 5) == [5, 5, 5]


# 626. Тесты для функции `string_to_list`:
def test_string_to_list():
    assert string_to_list("") == []
    assert string_to_list("hello") == ['h', 'e', 'l', 'l', 'o']
    assert string_to_list("12345") == ['1', '2', '3', '4', '5']
    assert string_to_list(" ") == [' ']
    assert string_to_list("!@#") == ['!', '@', '#']


# 627. Тесты для функции `merge_unique_lists`:
def test_merge_unique_lists():
    assert merge_unique_lists([], []) == []
    assert merge_unique_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_unique_lists([1, 1, 2], [2, 3, 3]) == [1, 2, 3]
    assert merge_unique_lists(['a', 'b'], ['b', 'c']) == ['a', 'b', 'c']
    assert merge_unique_lists([1, 2, 3], []) == [1, 2, 3]


# 628. Тесты для функции `set_from_strings_ignore_case`:
def test_set_from_strings_ignore_case():
    assert set_from_strings_ignore_case([]) == []
    assert set_from_strings_ignore_case(["a", "A", "b", "B"]) == ['a', 'b']
    assert set_from_strings_ignore_case(["abc", "ABC"]) == ['abc']
    assert set_from_strings_ignore_case(["hello", "HELLO", "Hello"]) == ['hello']
    assert set_from_strings_ignore_case(["a"]) == ['a']


# 629. Тесты для функции `count_characters`:
def test_count_characters():
    assert count_characters("") == {}
    assert count_characters("aabbcc") == {'a': 2, 'b': 2, 'c': 2}
    assert count_characters("aabbc") == {'a': 2, 'b': 2, 'c': 1}
    assert count_characters("abc") == {'a': 1, 'b': 1, 'c': 1}
    assert count_characters("aaa") == {'a': 3}


# 630. Тесты для функции `is_palindrome_5`:
def test_is_palindrome_5():
    assert is_palindrome_5("racecar") is True
    assert is_palindrome_5("RaceCar") is True
    assert is_palindrome_5("hello") is False
    assert is_palindrome_5("A man, a plan, a canal, Panama") is True
    assert is_palindrome_5("") is True


# 631. Тесты для функции `factorial_4`:
def test_factorial_4():
    assert factorial_4(0) == 1
    assert factorial_4(1) == 1
    assert factorial_4(2) == 2
    assert factorial_4(3) == 6
    assert factorial_4(5) == 120
    assert factorial_4(10) == 3628800
    assert factorial_4(4) == 24


# 632. Тесты для функции `count_word_occurrences`:
def test_count_word_occurrences():
    assert count_word_occurrences("", "word") == 0
    assert count_word_occurrences("word", "word") == 1
    assert count_word_occurrences("word word", "word") == 2
    assert count_word_occurrences("word word notword", "word") == 2
    assert count_word_occurrences("notword", "word") == 0
    assert count_word_occurrences("a b c d", "a") == 1
    assert count_word_occurrences("a a a a", "a") == 4


# 633. Тесты для функции `filter_numeric_strings`:
def test_filter_numeric_strings():
    assert filter_numeric_strings([]) == []
    assert filter_numeric_strings(["123", "abc", "456", "78a"]) == ["123", "456"]
    assert filter_numeric_strings(["12", "12b", "c34", "56"]) == ["12", "56"]
    assert filter_numeric_strings(["one", "two", "three"]) == []
    assert filter_numeric_strings(["0", "1", "2"]) == ["0", "1", "2"]


# 634. Тесты для функции `closest_number`:
def test_closest_number():
    assert closest_number([], 10) is None
    assert closest_number([10, 20, 30], 25) == 20
    assert closest_number([1, 2, 3, 4, 5], 3) == 3
    assert closest_number([1, 2, 3, 4, 5], 6) == 5
    assert closest_number([-1, -2, -3, -4, -5], -3) == -3
    assert closest_number([7, 14, 21], 18) == 21


# 635. Тесты для функции `sort_dicts_by_key`:
def test_sort_dicts_by_key():
    assert sort_dicts_by_key([], 'key') == []
    assert sort_dicts_by_key([{'key': 2}, {'key': 1}], 'key') == [{'key': 1}, {'key': 2}]
    assert sort_dicts_by_key([{'key': 3}, {'key': 2}, {'key': 1}], 'key') == [{'key': 1}, {'key': 2}, {'key': 3}]
    assert sort_dicts_by_key([{'a': 3}, {'a': 2}, {'a': 1}], 'a') == [{'a': 1}, {'a': 2}, {'a': 3}]
    assert sort_dicts_by_key([{'b': 1}, {'a': 2}], 'a') == [{'b': 1}, {'a': 2}]


# 636. Тесты для функции `gcd_5`:
def test_gcd_5():
    assert gcd_5(10, 5) == 5
    assert gcd_5(20, 8) == 4
    assert gcd_5(100, 10) == 10
    assert gcd_5(42, 56) == 14
    assert gcd_5(9, 3) == 3
    assert gcd_5(17, 13) == 1


# 637. Тесты для функции `average_6`:
def test_average_6():
    assert average_6([]) is None
    assert average_6([1, 2, 3]) == 2
    assert average_6([10, 20, 30]) == 20
    assert average_6([5, 15, 25, 35]) == 20
    assert average_6([-1, -2, -3]) == -2
    assert average_6([0]) == 0


# 638. Тесты для функции `alternate_case`:
def test_alternate_case():
    assert alternate_case("") == ""
    assert alternate_case("hello") == "HeLlO"
    assert alternate_case("HELLO") == "HeLlO"
    assert alternate_case("12345") == "12345"
    assert alternate_case("hElLo WoRlD") == 'HeLlO WoRlD'
    assert alternate_case("abc") == "AbC"


# 639. Тесты для функции `count_elements`:
def test_count_elements():
    assert count_elements([]) == {}
    assert count_elements([1, 1, 2, 2, 2, 3]) == {1: 2, 2: 3, 3: 1}
    assert count_elements(['a', 'b', 'a', 'a', 'c']) == {'a': 3, 'b': 1, 'c': 1}
    assert count_elements([0, 1, 0, 1, 0, 1]) == {0: 3, 1: 3}
    assert count_elements(['apple', 'banana', 'apple']) == {'apple': 2, 'banana': 1}


# 640. Тесты для функции `list_to_string`:
def test_list_to_string():
    assert list_to_string([], ",") == ""
    assert list_to_string([1, 2, 3], ",") == "1,2,3"
    assert list_to_string(["a", "b", "c"], "-") == "a-b-c"
    assert list_to_string([1, 2, 3], " ") == "1 2 3"
    assert list_to_string(["apple", "banana"], " and ") == "apple and banana"


# 641. Тесты для функции `unique_elements_6`:
def test_unique_elements_6():
    assert unique_elements_6([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
    assert unique_elements_6([1, 1, 1, 1]) == [1]
    assert unique_elements_6([]) == []
    assert unique_elements_6([5, 5, 6, 6, 7]) == [5, 6, 7]
    assert unique_elements_6([10, 20, 10, 30, 20]) == [10, 20, 30]


# 642. Тесты для функции `find_word_in_text`:
def test_find_word_in_text():
    assert find_word_in_text("Hello world", "world") == "Word found at index 6"
    assert find_word_in_text("Hello world", "hi") == "Word not found"
    assert find_word_in_text("", "anything") == "Word not found"
    assert find_word_in_text("Testing the function", "function") == 'Word found at index 12'
    assert find_word_in_text("Multiple words here", "words") == "Word found at index 9"


# 643. Тесты для функции `is_number_5`:
def test_is_number_5():
    assert is_number_5("123") is True
    assert is_number_5("123.45") is True
    assert is_number_5("abc") is False
    assert is_number_5("") is False
    assert is_number_5("123abc") is False
    assert is_number_5("-123.45") is True
    assert is_number_5("0") is True
    assert is_number_5(".5") is True
    assert is_number_5("-.5") is True


# 644. Тесты для функции `merge_dicts_6`:
def test_merge_dicts_6():
    assert merge_dicts_6({1: 10, 2: 20}, {2: 30, 3: 40}) == {1: 10, 2: 50, 3: 40}
    assert merge_dicts_6({}, {2: 20}) == {2: 20}
    assert merge_dicts_6({1: 10}, {}) == {1: 10}
    assert merge_dicts_6({1: 10}, {1: 5}) == {1: 15}
    assert merge_dicts_6({1: 10, 4: 40}, {4: 10, 5: 50}) == {1: 10, 4: 50, 5: 50}


# 645. Тесты для функции `even_index_elements`:
def test_even_index_elements():
    assert even_index_elements([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert even_index_elements([0, 2, 4, 6, 8]) == [0, 4, 8]
    assert even_index_elements(["a", "b", "c", "d"]) == ["a", "c"]
    assert even_index_elements([]) == []
    assert even_index_elements([7]) == [7]


# 646. Тесты для функции `invert_dict`:
def test_invert_dict():
    assert invert_dict({1: "a", 2: "b", 3: "c"}) == {"a": 1, "b": 2, "c": 3}
    assert invert_dict({"x": 10, "y": 20}) == {10: "x", 20: "y"}
    assert invert_dict({}) == {}
    assert invert_dict({1: 1, 2: 2}) == {1: 1, 2: 2}
    assert invert_dict({"key": "value"}) == {"value": "key"}


# 647. Тесты для функции `merge_sorted_lists_5`:
def test_merge_sorted_lists_5():
    assert merge_sorted_lists_5([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_lists_5([], [2, 4, 6]) == [2, 4, 6]
    assert merge_sorted_lists_5([1, 3, 5], []) == [1, 3, 5]
    assert merge_sorted_lists_5([1], [2]) == [1, 2]
    assert merge_sorted_lists_5([1, 1, 1], [1, 1, 1]) == [1, 1, 1, 1, 1, 1]


# 648. Тесты для функции `replace_second_char`:
def test_replace_second_char():
    assert replace_second_char("abcdef") == "a*c*e*"
    assert replace_second_char("123456") == "1*3*5*"
    assert replace_second_char("a") == "a"
    assert replace_second_char("") == ""
    assert replace_second_char("!") == "!"
    assert replace_second_char("hello world") == "h*l*o*w*r*d"


# 649. Тесты для функции `unique_numbers_and_sum`:
def test_unique_numbers_and_sum():
    assert unique_numbers_and_sum([1, 2, 2, 3, 1, 4]) == ([1, 2, 3, 4], 10)
    assert unique_numbers_and_sum([1, 1, 1, 1]) == ([1], 1)
    assert unique_numbers_and_sum([]) == ([], 0)
    assert unique_numbers_and_sum([5, 5, 6, 6, 7]) == ([5, 6, 7], 18)
    assert unique_numbers_and_sum([10, 20, 10, 30, 20]) == ([10, 20, 30], 60)


# 650. Тесты для функции `is_valid_email_2`:
def test_is_valid_email_2():
    assert is_valid_email_2("example@example.com") is True
    assert is_valid_email_2("example.com") is False
    assert is_valid_email_2("example@com") is False
    assert is_valid_email_2("@example.com") is False
    assert is_valid_email_2("example@.com") is True


# 651. Тесты для функции `count_words_in_string_2`:
def test_count_words_in_string_2():
    assert count_words_in_string_2("Hello world!") == 2
    assert count_words_in_string_2("A quick brown fox.") == 4
    assert count_words_in_string_2("") == 0
    assert count_words_in_string_2("One two three") == 3
    assert count_words_in_string_2("  Leading and trailing spaces  ") == 4


# 652. Тесты для функции `max_in_list`:
def test_max_in_list():
    assert max_in_list([1, 2, 3, 4, 5]) == 5
    assert max_in_list([-1, -2, -3, -4, -5]) == -1
    assert max_in_list([]) is None
    assert max_in_list([0]) == 0
    assert max_in_list([5, 5, 5]) == 5


# 653. Тесты для функции `string_to_numbers_2`:
def test_string_to_numbers_2():
    assert string_to_numbers_2("1,2,3") == [1, 2, 3]
    assert string_to_numbers_2("4, 5, 6") == [4, 5, 6]
    assert string_to_numbers_2("7,,8,,9") == [7, 8, 9]
    assert string_to_numbers_2("10, 11, 12") == [10, 11, 12]
    assert string_to_numbers_2("") == []
    assert string_to_numbers_2("a,b,c") == []


# 654. Тесты для функции `power_5`:
def test_power_5():
    assert power_5(2, 3) == 8
    assert power_5(5, 0) == 1
    assert power_5(1, 100) == 1
    assert power_5("a", 2) == "Invalid input"
    assert power_5(3, "b") == "Invalid input"
    assert power_5(2, -3) == 0.125
    assert power_5(-2, 3) == -8
    assert power_5(0, 0) == 1
    assert power_5(0, 5) == 0


# 655. Тесты для функции `divisible_by_x_5`:
def test_divisible_by_x_5():
    assert divisible_by_x_5(10, 2) == [2, 4, 6, 8, 10]
    assert divisible_by_x_5(15, 3) == [3, 6, 9, 12, 15]
    assert divisible_by_x_5(5, 1) == [1, 2, 3, 4, 5]
    assert divisible_by_x_5(20, 5) == [5, 10, 15, 20]
    assert divisible_by_x_5(7, 7) == [7]


# 656. Тесты для функции `length_without_spaces`:
def test_length_without_spaces():
    assert length_without_spaces("hello world") == 10
    assert length_without_spaces(" a b c ") == 3
    assert length_without_spaces("") == 0
    assert length_without_spaces("leading spaces") == 13
    assert length_without_spaces("no_spaces") == 9


# 657. Тесты для функции `is_decimal`:
def test_is_decimal():
    assert is_decimal("123.45") is True
    assert is_decimal("123") is False
    assert is_decimal("abc") is False
    assert is_decimal("") is False
    assert is_decimal("123.") is True
    assert is_decimal(".45") is True


# 658. Тесты для функции `change_case_and_strip`:
def test_change_case_and_strip():
    assert change_case_and_strip(" hello") == "HELLO"
    assert change_case_and_strip("hello") == "hello"
    assert change_case_and_strip(" HELLO") == "HELLO"
    assert change_case_and_strip("Hello World") == "hello world"
    assert change_case_and_strip("HELLO WORLD") == "hello world"
    assert change_case_and_strip("") == ""


# 659. Тесты для функции `find_first_negative`:
def test_find_first_negative():
    assert find_first_negative([1, 2, 3, -4, 5]) == 3
    assert find_first_negative([1, -2, 3, -4, 5]) == 1
    assert find_first_negative([1, 2, 3, 4, 5]) is None
    assert find_first_negative([]) is None
    assert find_first_negative([-1, -2, -3]) == 0


# 660. Тесты для функции `remove_duplicates_5`:
def test_remove_duplicates_5():
    assert remove_duplicates_5([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
    assert remove_duplicates_5([1, 1, 1, 1]) == [1]
    assert remove_duplicates_5([]) == []
    assert remove_duplicates_5([5, 5, 6, 6, 7]) == [5, 6, 7]
    assert remove_duplicates_5([10, 20, 10, 30, 20]) == [10, 20, 30]


# 661. Тесты для функции `is_float_5`
def test_is_float_5():
    assert is_float_5("3.14") is True
    assert is_float_5("0.001") is True
    assert is_float_5("-3.14") is True
    assert is_float_5("3") is False
    assert is_float_5("abc") is False
    assert is_float_5("3.") is True


# 662. Тесты для функции `extract_words_with_numbers`
def test_extract_words_with_numbers():
    assert extract_words_with_numbers("abc123 def456") == ["abc123", "def456"]
    assert extract_words_with_numbers("123") == ["123"]
    assert extract_words_with_numbers("abc def") == []
    assert extract_words_with_numbers("") == []
    assert extract_words_with_numbers("a1b2 c3") == ["a1b2", "c3"]
    assert extract_words_with_numbers("word1 word2 word3") == ["word1", "word2", "word3"]


# 663. Тесты для функции `lcm_4`
def test_lcm_4():
    assert lcm_4(4, 5) == 20
    assert lcm_4(0, 5) == 0
    assert lcm_4(6, 8) == 24
    assert lcm_4(7, 3) == 21
    assert lcm_4(21, 6) == 42
    assert lcm_4(1, 1) == 1


# 664. Тесты для функции `merge_unique_lists_2`
def test_merge_unique_lists_2():
    assert merge_unique_lists_2([1, 2], [2, 3]) == [1, 2, 3]
    assert merge_unique_lists_2([], [1, 2]) == [1, 2]
    assert merge_unique_lists_2([1, 2], []) == [1, 2]
    assert merge_unique_lists_2([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert merge_unique_lists_2([], []) == []
    assert merge_unique_lists_2([1, 3, 5], [2, 4, 6]) == [1, 3, 5, 2, 4, 6]


# 665. Тесты для функции `find_index_of_element`
def test_find_index_of_element():
    assert find_index_of_element([1, 2, 3], 2) == 1
    assert find_index_of_element([1, 2, 3], 4) is None
    assert find_index_of_element([], 2) is None
    assert find_index_of_element([1, 2, 3, 2], 2) == 1
    assert find_index_of_element([1], 1) == 0
    assert find_index_of_element([2], 1) is None


# 666. Тесты для функции `count_words_in_string_with_delimiters`
def test_count_words_in_string_with_delimiters():
    assert count_words_in_string_with_delimiters("Hello world") == 2
    assert count_words_in_string_with_delimiters("word,word2", ",") == 2
    assert count_words_in_string_with_delimiters("") == 0
    assert count_words_in_string_with_delimiters("a, b; c", ",; ") == 3
    assert count_words_in_string_with_delimiters(" one  two   three ") == 3
    assert count_words_in_string_with_delimiters("singleword") == 1


# 667. Тесты для функции `greater_than_average_6`
def test_greater_than_average_6():
    assert greater_than_average_6([1, 2, 3, 4, 5]) == [4, 5]
    assert greater_than_average_6([5, 10, 15]) == [15]
    assert greater_than_average_6([2, 4, 6, 8]) == [6, 8]
    assert greater_than_average_6([1, 1, 1, 1]) == []
    assert greater_than_average_6([]) == []
    assert greater_than_average_6([3, 3, 3, 3, 4]) == [4]


# 668. Тесты для функции `merge_dict_and_tuple`
def test_merge_dict_and_tuple():
    assert merge_dict_and_tuple([("key1", "value1"), ("key2", "value2")], {"key3": "value3"}) == {"key3": "value3", "key1": "value1", "key2": "value2"}
    assert merge_dict_and_tuple([], {"key1": "value1"}) == {"key1": "value1"}
    assert merge_dict_and_tuple([("key1", "value1")], {}) == {"key1": "value1"}
    assert merge_dict_and_tuple([], {}) == {}
    assert merge_dict_and_tuple([("key1", "value1"), ("key2", "value2")], {"key1": "old_value"}) == {"key1": "value1", "key2": "value2"}
    assert merge_dict_and_tuple([("key1", "value1"), ("key2", "value2")], {"key3": "value3"}) == {"key3": "value3", "key1": "value1", "key2": "value2"}


# 669. Тесты для функции `sum_numbers_in_string_2`
def test_sum_numbers_in_string_2():
    assert sum_numbers_in_string_2("abc123def456") == 579
    assert sum_numbers_in_string_2("123") == 123
    assert sum_numbers_in_string_2("") == 0
    assert sum_numbers_in_string_2("abc") == 0
    assert sum_numbers_in_string_2("1a2b3c") == 6
    assert sum_numbers_in_string_2("10, 20, 30") == 60


# 670. Тесты для функции `find_missing_number`
def test_find_missing_number():
    assert find_missing_number([1, 2, 3], [2, 3]) == 1
    assert find_missing_number([1, 2, 3], [1, 2, 3]) is None
    assert find_missing_number([], [1, 2, 3]) is None
    assert find_missing_number([1, 2, 3], []) == 3
    assert find_missing_number([1, 1, 2, 2], [1, 2]) is None
    assert find_missing_number([4, 5, 6], [4, 6]) == 5


# 671. Тесты для функции `alternate_merge`
def test_alternate_merge():
    assert alternate_merge("abc", "def") == "adbecf"
    assert alternate_merge("", "def") == "def"
    assert alternate_merge("abc", "") == "abc"
    assert alternate_merge("a", "b") == "ab"
    assert alternate_merge("abc", "defgh") == "adbecfgh"
    assert alternate_merge("abcd", "ef") == 'aebfcd'


# 672. Тесты для функции `are_all_greater_than`
def test_are_all_greater_than():
    assert are_all_greater_than([5, 6, 7], 4) is True
    assert are_all_greater_than([3, 4, 5], 5) is False
    assert are_all_greater_than([], 1) is False
    assert are_all_greater_than([10, 20], 15) is False
    assert are_all_greater_than([1, 1, 1], 1) is False
    assert are_all_greater_than([2, 3, 4], 1) is True


# 673. Тесты для функции `replace_first_occurrence`
def test_replace_first_occurrence():
    assert replace_first_occurrence("hello world", "world", "there") == "hello there"
    assert replace_first_occurrence("hello hello", "hello", "hi") == "hi hello"
    assert replace_first_occurrence("abc", "d", "e") == "abc"
    assert replace_first_occurrence("", "a", "b") == ""
    assert replace_first_occurrence("a a a", "a", "b") == "b a a"
    assert replace_first_occurrence("test", "test", "best") == "best"


# 674. Тесты для функции `get_unique_elements`
def test_get_unique_elements():
    assert get_unique_elements([1, 2, 2, 3, 4, 4]) == [1, 3]
    assert get_unique_elements([]) == []
    assert get_unique_elements([1, 1, 1]) == []
    assert get_unique_elements([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert get_unique_elements([1, 1, 2, 3, 3, 4, 5, 5]) == [2, 4]
    assert get_unique_elements([2, 2, 2, 3, 3]) == []


# 675. Тесты для функции `min_even_number`
def test_min_even_number():
    assert min_even_number([1, 2, 3, 4]) == 2
    assert min_even_number([5, 7, 9]) is None
    assert min_even_number([]) is None
    assert min_even_number([2, 4, 6, 8]) == 2
    assert min_even_number([1, 3, 5, 7, 2]) == 2
    assert min_even_number([10, 20, 30]) == 10


# 676. Тесты для функции `number_to_string_with_leading_zeros`
def test_number_to_string_with_leading_zeros():
    assert number_to_string_with_leading_zeros(5, 3) == "005"
    assert number_to_string_with_leading_zeros(123, 5) == "00123"
    assert number_to_string_with_leading_zeros(0, 4) == "0000"
    assert number_to_string_with_leading_zeros(456, 2) == "456"
    assert number_to_string_with_leading_zeros(12, 4) == "0012"
    assert number_to_string_with_leading_zeros(789, 6) == "000789"


# 677. Тесты для функции `list_to_comma_separated_string`
def test_list_to_comma_separated_string():
    assert list_to_comma_separated_string([1, 2, 3]) == "1, 2, 3"
    assert list_to_comma_separated_string([]) == ""
    assert list_to_comma_separated_string([1]) == "1"
    assert list_to_comma_separated_string([1, 2, 3, 4, 5]) == "1, 2, 3, 4, 5"
    assert list_to_comma_separated_string([10, 20, 30]) == "10, 20, 30"
    assert list_to_comma_separated_string([100, 200]) == "100, 200"


# 678. Тесты для функции `is_valid_number`
def test_is_valid_number():
    assert is_valid_number("3.14") is True
    assert is_valid_number("123") is True
    assert is_valid_number("-0.001") is True
    assert is_valid_number("abc") is False
    assert is_valid_number("") is False
    assert is_valid_number("3.14.15") is False


# 679. Тесты для функции `count_vowels_2`
def test_count_vowels_2():
    assert count_vowels_2("hello") == 2
    assert count_vowels_2("world") == 1
    assert count_vowels_2("AEIOUaeiou") == 10
    assert count_vowels_2("bcdfg") == 0
    assert count_vowels_2("") == 0
    assert count_vowels_2("aEiOu") == 5


# 680. Тесты для функции `product_of_numbers_in_string`
def test_product_of_numbers_in_string():
    assert product_of_numbers_in_string("1234") == 1234
    assert product_of_numbers_in_string("56a78") == 4368
    assert product_of_numbers_in_string("1a2b3c4") == 24
    assert product_of_numbers_in_string("abc") == 1
    assert product_of_numbers_in_string("") == 1
    assert product_of_numbers_in_string("10, 20, 30") == 6000


# 681. Тесты для функции `find_strings_with_digits`:
def test_find_strings_with_digits():
    assert find_strings_with_digits(["abc", "a1c", "123", ""]) == ["a1c", "123"]
    assert find_strings_with_digits(["no_digits", "still_no", "3digits"]) == ["3digits"]
    assert find_strings_with_digits(["", "1"]) == ["1"]
    assert find_strings_with_digits(["all_numbers1", "2gether", ""]) == ["all_numbers1", "2gether"]
    assert find_strings_with_digits(["none_here", "and_here", ""]) == []
    assert find_strings_with_digits(["12three", "fou4r", ""]) == ["12three", "fou4r"]


# 682. Тесты для функции `count_digits_in_string`:
def test_count_digits_in_string():
    assert count_digits_in_string("abc123") == 3
    assert count_digits_in_string("") == 0
    assert count_digits_in_string("no_digits") == 0
    assert count_digits_in_string("5abc67") == 3
    assert count_digits_in_string("123456") == 6
    assert count_digits_in_string("only1digit") == 1


# 683. Тесты для функции `get_every_second_char`:
def test_get_every_second_char():
    assert get_every_second_char("abcdef") == "ace"
    assert get_every_second_char("a") == "a"
    assert get_every_second_char("") == ""
    assert get_every_second_char("123456") == "135"
    assert get_every_second_char("a1b2c3d4") == "abcd"
    assert get_every_second_char("even") == 'ee'


# 684. Тесты для функции `filter_strings_with_uppercase`:
def test_filter_strings_with_uppercase():
    assert filter_strings_with_uppercase(["abc", "ABC", "aBc"]) == ["ABC", "aBc"]
    assert filter_strings_with_uppercase(["no_upper", "STILL_NONE", ""]) == ["STILL_NONE"]
    assert filter_strings_with_uppercase(["lower", "Case", "UPPER"]) == ["Case", "UPPER"]
    assert filter_strings_with_uppercase(["", "noupper", ""]) == []
    assert filter_strings_with_uppercase(["Empty", "Spaces", "OnlyUpper"]) == ["Empty", "Spaces", "OnlyUpper"]
    assert filter_strings_with_uppercase(["upperCASE", "MiXeD", ""]) == ["upperCASE", "MiXeD"]


# 685. Тесты для функции `count_non_space_characters`:
def test_count_non_space_characters():
    assert count_non_space_characters("abc abc") == {"a": 2, "b": 2, "c": 2}
    assert count_non_space_characters("") == {}
    assert count_non_space_characters("no spaces") == {'n': 1, 'o': 1, 's': 2, 'p': 1, 'a': 1, 'c': 1, 'e': 1}
    assert count_non_space_characters("a b c") == {"a": 1, "b": 1, "c": 1}
    assert count_non_space_characters("repeated repeated") == {"r": 2, "e": 6, "p": 2, "a": 2, "t": 2, "d": 2}
    assert count_non_space_characters("spaces only") == {"s": 2, "p": 1, "a": 1, "c": 1, "e": 1, "o": 1, "n": 1, "l": 1, "y": 1}


# 686. Тесты для функции `find_longest_string`:
def test_find_longest_string():
    assert find_longest_string(["short", "longer", "longest"]) == "longest"
    assert find_longest_string(["one", "three"]) == "three"
    assert find_longest_string(["same", "size"]) == "same"
    assert find_longest_string([""]) == ""
    assert find_longest_string(["two", "letters", "word"]) == "letters"
    assert find_longest_string([]) is None


# 687. Тесты для функции `find_first_even`:
def test_find_first_even():
    assert find_first_even([1, 3, 5, 6]) == 3
    assert find_first_even([2, 4, 6, 8]) == 0
    assert find_first_even([1, 3, 5, 7]) is None
    assert find_first_even([1, 2, 3, 4, 5]) == 1
    assert find_first_even([]) is None
    assert find_first_even([1, 2, 4, 8, 16]) == 1


# 688. Тесты для функции `sum_numbers_in_string_v3`:
def test_sum_numbers_in_string_v3():
    assert sum_numbers_in_string_v3("abc123") == 123
    assert sum_numbers_in_string_v3("") is None
    assert sum_numbers_in_string_v3("123abc45") == 168
    assert sum_numbers_in_string_v3("no digits here") is None
    assert sum_numbers_in_string_v3("12 and 34") == 46
    assert sum_numbers_in_string_v3("100") == 100


# 689. Тесты для функции `string_to_number_list`:
def test_string_to_number_list():
    assert string_to_number_list("1 2 3") == [1, 2, 3]
    assert string_to_number_list("") == []
    assert string_to_number_list("one two three") is None
    assert string_to_number_list("1 2 3 four") is None
    assert string_to_number_list("10 20 30") == [10, 20, 30]
    assert string_to_number_list("10 20") == [10, 20]


# 690. Тесты для функции `find_max_min`:
def test_find_max_min():
    assert find_max_min([1, 2, 3, 4, 5]) == (5, 1)
    assert find_max_min([5, 1, 5, 5]) == (5, 1)
    assert find_max_min([3, -3, 5, 7]) == (7, -3)
    assert find_max_min([10]) == (10, 10)
    assert find_max_min([]) == (None, None)
    assert find_max_min([-5, -4, -3, -2, -1]) == (-1, -5)


# 691. Тесты для функции `replace_spaces_with_underscores_5`:
def test_replace_spaces_with_underscores_5():
    assert replace_spaces_with_underscores_5("a b c") == "a_b_c"
    assert replace_spaces_with_underscores_5("") is None
    assert replace_spaces_with_underscores_5("no spaces") == "no_spaces"
    assert replace_spaces_with_underscores_5("only one") == "only_one"
    assert replace_spaces_with_underscores_5("leading space ") == "leading_space_"
    assert replace_spaces_with_underscores_5(" trailing space") == "_trailing_space"


# 692. Тесты для функции `remove_duplicates_maintain_order`:
def test_remove_duplicates_maintain_order():
    assert remove_duplicates_maintain_order([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates_maintain_order([]) == []
    assert remove_duplicates_maintain_order([1, 1, 1, 1]) == [1]
    assert remove_duplicates_maintain_order(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]
    assert remove_duplicates_maintain_order([1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates_maintain_order([4, 4, 4, 4, 4, 4]) == [4]


# 693. Тесты для функции `find_first_multiple`:
def test_find_first_multiple():
    assert find_first_multiple([10, 20, 30], 10) == 10
    assert find_first_multiple([1, 3, 5], 2) is None
    assert find_first_multiple([], 2) is None
    assert find_first_multiple([5, 10, 15], 5) == 5
    assert find_first_multiple([2, 4, 6], 3) == 6
    assert find_first_multiple([4, 8, 12, 16], 4) == 4


# 694. Тесты для функции `is_palindrome_v2`:
def test_is_palindrome_v2():
    assert is_palindrome_v2("A man a plan a canal Panama") is True
    assert is_palindrome_v2("") is False
    assert is_palindrome_v2("racecar") is True
    assert is_palindrome_v2("hello") is False
    assert is_palindrome_v2("Never odd or even") is True
    assert is_palindrome_v2("not a palindrome") is False


# 695. Тесты для функции `get_even_numbers`:
def test_get_even_numbers():
    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert get_even_numbers([]) == []
    assert get_even_numbers([1, 3, 5]) == []
    assert get_even_numbers([0, 2, 4, 6, 8]) == [0, 2, 4, 6, 8]
    assert get_even_numbers([1, 2, 3, 4, 5]) == [2, 4]
    assert get_even_numbers([10, 11, 12, 13]) == [10, 12]


# 696. Тесты для функции `is_number_v2`:
def test_is_number_v2():
    assert is_number_v2("123") is True
    assert is_number_v2("abc") is False
    assert is_number_v2("") is False
    assert is_number_v2("123.45") is True
    assert is_number_v2("12e4") is True
    assert is_number_v2("one") is False


# 697. Тесты для функции `count_repeating_elements`:
def test_count_repeating_elements():
    assert count_repeating_elements([1, 2, 2, 3, 3, 3]) == {2: 2, 3: 3}
    assert count_repeating_elements([]) == {}
    assert count_repeating_elements([1, 1, 1, 1]) == {1: 4}
    assert count_repeating_elements(["a", "b", "a", "c", "b"]) == {"a": 2, "b": 2}
    assert count_repeating_elements([1, 2, 3]) == {}
    assert count_repeating_elements([4, 4, 4, 4, 4, 4]) == {4: 6}


# 698. Тесты для функции `extract_unique_words`:
def test_extract_unique_words():
    assert extract_unique_words("one two two three three three") == ['one', 'three', 'two']
    assert extract_unique_words("") == []
    assert extract_unique_words("word") == ["word"]
    assert extract_unique_words("a b c a b c") == ["a", "b", "c"]
    assert extract_unique_words("unique words in this string") == ['in', 'string', 'this', 'unique', 'words']
    assert extract_unique_words("repeat repeat") == ["repeat"]


# 699. Тесты для функции `find_largest_prime`:
def test_find_largest_prime():
    assert find_largest_prime([2, 3, 5, 7, 11, 13]) == 13
    assert find_largest_prime([]) is None
    assert find_largest_prime([4, 6, 8, 10]) is None
    assert find_largest_prime([11, 1024, 23, 19]) == 23
    assert find_largest_prime([10, 13, 17, 18, 19]) == 19
    assert find_largest_prime([1, 2, 3]) == 3


# 700. Тесты для функции `extract_digits`:
def test_extract_digits():
    assert extract_digits("a1b2c3") == [1, 2, 3]
    assert extract_digits("") == []
    assert extract_digits("no digits here") == []
    assert extract_digits("123abc456") == [1, 2, 3, 4, 5, 6]
    assert extract_digits("0") == [0]
    assert extract_digits("one1two2") == [1, 2]


# 701. Тесты для функции `find_long_words`
def test_find_long_words():
    assert find_long_words("Hello world from AI") == ["Hello", "world", "from"]
    assert find_long_words("AI is fun") == []
    assert find_long_words("") == []
    assert find_long_words("Test the function find long words") == ["Test", "function", "find", "long", "words"]
    assert find_long_words("Short and sweet") == ["Short", "sweet"]
    assert find_long_words("A sequence of longwordsisrequired") == ["sequence", "longwordsisrequired"]
    assert find_long_words("Edge case with wordsss") == ["Edge", "case", "with", "wordsss"]
    assert find_long_words("Another edge case with word") == ["Another", "edge", "case", "with", "word"]
    assert find_long_words("1234567890 more than 10") == ["1234567890", "more", "than"]


# 702. Тесты для функции `get_numbers_from_string`
def test_get_numbers_from_string():
    assert get_numbers_from_string("123,456,789") == [123, 456, 789]
    assert get_numbers_from_string("100,200,300") == [100, 200, 300]
    assert get_numbers_from_string("") == []
    assert get_numbers_from_string("0,1,2,3") == [0, 1, 2, 3]
    assert get_numbers_from_string("11,22,33") == [11, 22, 33]
    assert get_numbers_from_string("text without numbers") == []
    assert get_numbers_from_string("400number,500text,600number") == [400, 500, 600]
    assert get_numbers_from_string("999text999") == [999, 999]
    assert get_numbers_from_string("1.2.3") == [1, 2, 3]


# 703. Тесты для функции `find_numbers_greater_than`
def test_find_numbers_greater_than():
    assert find_numbers_greater_than([1, 2, 3, 4, 5], 3) == [4, 5]
    assert find_numbers_greater_than([], 3) == []
    assert find_numbers_greater_than([3, 3, 3], 3) == []
    assert find_numbers_greater_than([10, 20, 30, 40, 50], 25) == [30, 40, 50]
    assert find_numbers_greater_than([-1, -2, -3, -4], -3) == [-1, -2]
    assert find_numbers_greater_than([100, 101, 102], 100) == [101, 102]
    assert find_numbers_greater_than([2, 4, 6, 8], 1) == [2, 4, 6, 8]
    assert find_numbers_greater_than([5, 3, 1], 4) == [5]
    assert find_numbers_greater_than([5, 4, 3, 2, 1], 2) == [5, 4, 3]


# 704. Тесты для функции `join_strings_with_separator`
def test_join_strings_with_separator():
    assert join_strings_with_separator(["a", "b", "c"], ",") == "a,b,c"
    assert join_strings_with_separator([], ",") == ""
    assert join_strings_with_separator(["onlyone"], ",") == "onlyone"
    assert join_strings_with_separator(["this", "is", "a", "test"], " ") == "this is a test"
    assert join_strings_with_separator(["test", "function"], "-") == "test-function"
    assert join_strings_with_separator(["join", "with", "different", "separators"], "|") == "join|with|different|separators"
    assert join_strings_with_separator(["first", "second"], ".") == "first.second"
    assert join_strings_with_separator(["combine", "all", "words"], "") == "combineallwords"
    assert join_strings_with_separator(["1", "2", "3"], " ") == "1 2 3"


# 705. Тесты для функции `sum_even_numbers`
def test_sum_even_numbers():
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12
    assert sum_even_numbers([]) == 0
    assert sum_even_numbers([1, 3, 5, 7]) == 0
    assert sum_even_numbers([2, 4, 6, 8, 10]) == 30
    assert sum_even_numbers([-2, -4, -6]) == -12
    assert sum_even_numbers([0, 2, 4]) == 6
    assert sum_even_numbers([1, 2, 3, 4]) == 6
    assert sum_even_numbers([10, 20, 30, 40]) == 100
    assert sum_even_numbers([2, 2, 2, 2]) == 8


# 706. Тесты для функции `find_string_with_word`
def test_find_string_with_word():
    assert find_string_with_word(["hello world", "foo bar"], "hello") == "hello world"
    assert find_string_with_word(["one two", "three four"], "five") is None
    assert find_string_with_word([], "word") is None
    assert find_string_with_word(["find this string", "or this one"], "this") == "find this string"
    assert find_string_with_word(["no match here"], "hello") is None
    assert find_string_with_word(["searching", "for", "word"], "for") == "for"
    assert find_string_with_word(["multiple", "matches", "here"], "matches") == "matches"
    assert find_string_with_word(["first", "last"], "last") == "last"
    assert find_string_with_word(["edge case"], "edge") == "edge case"


# 707. Тесты для функции `find_smallest_odd`
def test_find_smallest_odd():
    assert find_smallest_odd([1, 3, 5, 7, 9]) == 1
    assert find_smallest_odd([2, 4, 6, 8, 10]) is None
    assert find_smallest_odd([]) is None
    assert find_smallest_odd([10, 15, 20, 25]) == 15
    assert find_smallest_odd([11, 13, 15, 17]) == 11
    assert find_smallest_odd([-1, -3, -5, 0]) == -5
    assert find_smallest_odd([100, 101, 102, 103]) == 101
    assert find_smallest_odd([5, 4, 3, 2, 1]) == 1
    assert find_smallest_odd([12, 14, 16, 19]) == 19


# 708. Тесты для функции `replace_substring`
def test_replace_substring():
    assert replace_substring("hello world", "world", "there") == "hello there"
    assert replace_substring("ababab", "ab", "cd") == "cdcdcd"
    assert replace_substring("", "a", "b") == ""
    assert replace_substring("nothing to replace", "xyz", "abc") is None
    assert replace_substring("12345", "123", "678") == "67845"
    assert replace_substring("replace me if you can", "can", "will") == "replace me if you will"
    assert replace_substring("edgecase", "edge", "case") == "casecase"
    assert replace_substring("simple test", "simple", "complex") == "complex test"
    assert replace_substring("aaaa", "aa", "bb") == "bbbb"


# 709. Тесты для функции `find_divisible_by_3_and_5`
def test_find_divisible_by_3_and_5_5():
    assert find_divisible_by_3_and_5_5([15, 30, 45, 60]) == 15
    assert find_divisible_by_3_and_5_5([1, 2, 3, 4, 5]) is None
    assert find_divisible_by_3_and_5_5([]) is None
    assert find_divisible_by_3_and_5_5([0, 3, 5, 15]) == 0
    assert find_divisible_by_3_and_5_5([9, 18, 27, 45]) == 45
    assert find_divisible_by_3_and_5_5([100, 101, 102, 103]) is None
    assert find_divisible_by_3_and_5_5([30, 60, 90, 120]) == 30
    assert find_divisible_by_3_and_5_5([-15, -30, -45]) == -15
    assert find_divisible_by_3_and_5_5([3, 6, 9, 12, 15]) == 15


# 710. Тесты для функции `calculate_average`
def test_calculate_average():
    assert calculate_average([1, 2, 3, 4, 5]) == 3
    assert calculate_average([]) is None
    assert calculate_average([10, 20, 30]) == 20
    assert calculate_average([-1, -2, -3]) == -2
    assert calculate_average([5, 10, 15, 20]) == 12.5
    assert calculate_average([100]) == 100
    assert calculate_average([0, 0, 0]) == 0
    assert calculate_average([0, 5, 10]) == 5
    assert calculate_average([-10, 10, -10, 10]) == 0


# 711. Тесты для функции `combine_and_unique`
def test_combine_and_unique():
    assert combine_and_unique([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 4, 5]
    assert combine_and_unique([], [1, 2, 3]) == [1, 2, 3]
    assert combine_and_unique([1, 2, 3], []) == [1, 2, 3]
    assert combine_and_unique([], []) == []
    assert combine_and_unique([1, 1, 1], [1, 1, 1]) == [1]
    assert combine_and_unique([1, 2, 2], [2, 3, 3]) == [1, 2, 3]
    assert combine_and_unique([-1, -2, -3], [-3, -4, -5]) == [-1, -2, -3, -4, -5]
    assert combine_and_unique([1, 2, 3, 4], [5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert combine_and_unique(["a", "b"], ["b", "c"]) == ["a", "b", "c"]


# 712. Тесты для функции `choose_largest`
def test_choose_largest():
    assert choose_largest(1, 2, 3) == 3
    assert choose_largest(3, 2, 1) == 3
    assert choose_largest(1, 3, 2) == 3
    assert choose_largest(3, 3, 2) == 3
    assert choose_largest(2, 3, 3) == 3
    assert choose_largest(3, 3, 3) == 3
    assert choose_largest(-1, -2, -3) == -1
    assert choose_largest(0, 0, 0) == 0
    assert choose_largest(100, 50, 25) == 100


# 713. Тесты для функции `choose_longest_string`
def test_choose_longest_string():
    assert choose_longest_string("one", "three", "five") == "three"
    assert choose_longest_string("a", "bc", "def") == "def"
    assert choose_longest_string("apple", "banana", "cherry") == "cherry"
    assert choose_longest_string("") == ""
    assert choose_longest_string("short", "longer", "longest") == "longest"
    assert choose_longest_string("a", "ab", "abc") == "abc"
    assert choose_longest_string("equal", "equal") == "equal"
    assert choose_longest_string("A", "BB", "CCC") == "CCC"
    assert choose_longest_string("one", "two", "three") == "three"


# 714. Тесты для функции `choose_most_frequent`
def test_choose_most_frequent():
    assert choose_most_frequent([1, 2, 2, 3, 3, 3]) == 3
    assert choose_most_frequent(["a", "b", "b", "c", "c", "c"]) == "c"
    assert choose_most_frequent([1, 1, 1, 2, 2, 3, 3, 3, 3]) == 3
    assert choose_most_frequent([]) is None
    assert choose_most_frequent([1, 1, 2, 2, 3, 3]) == 3
    assert choose_most_frequent(["equal", "equal", "equal", "equal"]) == "equal"
    assert choose_most_frequent(["x", "x", "y", "y", "z"]) == "y"
    assert choose_most_frequent([1, 2, 3, 4, 5, 1, 2, 3, 1]) == 1
    assert choose_most_frequent(["apple", "banana", "apple"]) == "apple"


# 715. Тесты для функции `choose_smallest`
def test_choose_smallest():
    assert choose_smallest(3, 2, 1) == 1
    assert choose_smallest(1, 2, 3) == 1
    assert choose_smallest(2, 2, 2) == 2
    assert choose_smallest(-1, -2, -3) == -3
    assert choose_smallest(0, -1, 1) == -1
    assert choose_smallest(100, 50, 25) == 25
    assert choose_smallest(1) == 1
    assert choose_smallest(-10, -20, -30) == -30
    assert choose_smallest(1, 1, 1, 1) == 1


# 716. Тесты для функции `choose_string_with_most_vowels`
def test_choose_string_with_most_vowels():
    assert choose_string_with_most_vowels("hello", "world", "ai") == "hello"
    assert choose_string_with_most_vowels("a", "e", "i", "o", "u") == "u"
    assert choose_string_with_most_vowels("rhythm", "glyph", "fly") == "rhythm"
    assert choose_string_with_most_vowels("vowel", "consonant") == "consonant"
    assert choose_string_with_most_vowels("aaa", "bbb", "ccc") == "aaa"
    assert choose_string_with_most_vowels("aeiou", "bcdfg", "xyz") == "aeiou"
    assert choose_string_with_most_vowels("a", "aaa", "aa") == "aaa"
    assert choose_string_with_most_vowels("equal", "longer", "longest") == "equal"
    assert choose_string_with_most_vowels("a", "ab", "abc") == "abc"


# 717. Тесты для функции `choose_smallest_even`
def test_choose_smallest_even():
    assert choose_smallest_even(1, 2, 3, 4) == 2
    assert choose_smallest_even(2, 2, 2, 2) == 2
    assert choose_smallest_even(1, 1, 1, 1) == "No even numbers"
    assert choose_smallest_even(0) == 0
    assert choose_smallest_even(-2, -4, -6) == -6
    assert choose_smallest_even(10, 20, 30) == 10
    assert choose_smallest_even(1, 3, 5, 7) == "No even numbers"
    assert choose_smallest_even(2) == 2
    assert choose_smallest_even(-10, -20, -30) == -30


# 718. Тесты для функции `choose_number_with_max_diff`
def test_choose_number_with_max_diff():
    assert choose_number_with_max_diff(1, 2, 3) == 1
    assert choose_number_with_max_diff(-1, -2, -3) == -1
    assert choose_number_with_max_diff(10, 20, 30) == 10
    assert choose_number_with_max_diff(1, 1, 1) is None
    assert choose_number_with_max_diff(5, 5, 5, 10) == 10
    assert choose_number_with_max_diff(0, 0, 0) is None
    assert choose_number_with_max_diff(-10, -20, -30) == -10
    assert choose_number_with_max_diff(3, 6, 9, 12) == 3
    assert choose_number_with_max_diff(-1, 0, 1) == -1


# 719. Тесты для функции `choose_string_starting_with_vowel`
def test_choose_string_starting_with_vowel():
    assert choose_string_starting_with_vowel("apple", "banana", "orange") == "apple"
    assert choose_string_starting_with_vowel("test", "test", "test") == "No string starts with a vowel"
    assert choose_string_starting_with_vowel("egg", "emphasis") == "egg"
    assert choose_string_starting_with_vowel("quick", "brown", "fox") == "No string starts with a vowel"
    assert choose_string_starting_with_vowel("upper", "lower") == "upper"
    assert choose_string_starting_with_vowel("a", "e", "i") == "a"
    assert choose_string_starting_with_vowel("AI", "rules") == "AI"
    assert choose_string_starting_with_vowel("buzz", "quiz") == "No string starts with a vowel"


# 720. Тесты для функции `choose_second_largest`
def test_choose_second_largest():
    assert choose_second_largest(1, 2, 3) == 2
    assert choose_second_largest(3, 2, 1) == 2
    assert choose_second_largest(1, 3, 2) == 2
    assert choose_second_largest(10, 20, 30) == 20
    assert choose_second_largest(30, 20, 10) == 20
    assert choose_second_largest(20, 10, 30) == 20
    assert choose_second_largest(1, 1, 1) == "Not enough distinct numbers"
    assert choose_second_largest(1, 2) == 1
    assert choose_second_largest(3, 3, 5, 5, 5) == 3


# 721. Тесты для функции `choose_smallest_even_from_list`
def test_choose_smallest_even_from_list():
    assert choose_smallest_even_from_list([1, 3, 5, 7]) == "No even numbers found"
    assert choose_smallest_even_from_list([2, 4, 6, 8]) == 2
    assert choose_smallest_even_from_list([1, 2, 3, 4, 5]) == 2
    assert choose_smallest_even_from_list([-2, 3, -4, 5, -6]) == -6
    assert choose_smallest_even_from_list([10, 15, 7, 3]) == 10
    assert choose_smallest_even_from_list([]) == "No even numbers found"


# 722. Тесты для функции `choose_longest_non_vowel_word`
def test_choose_longest_non_vowel_word():
    assert choose_longest_non_vowel_word("apple", "banana", "cherry") == "banana"
    assert choose_longest_non_vowel_word("Apple", "Orange", "Grape") == "Grape"
    assert choose_longest_non_vowel_word("egg", "ibex", "owl") == "No word found"
    assert choose_longest_non_vowel_word("cat", "dog", "fish") == "fish"
    assert choose_longest_non_vowel_word("bird", "fly", "ant") == "bird"
    assert choose_longest_non_vowel_word("enter", "exit", "island") == 'No word found'


# 723. Тесты для функции `choose_smallest_negative`
def test_choose_smallest_negative():
    assert choose_smallest_negative(1, 2, 3, 4) == "No negative numbers"
    assert choose_smallest_negative(-1, -2, -3, -4) == -1
    assert choose_smallest_negative(1, -2, 3, -4) == -2
    assert choose_smallest_negative(-10, -20, -30, -40) == -10
    assert choose_smallest_negative(-5, 0, -10) == -5
    assert choose_smallest_negative(5, 10, 15) == "No negative numbers"


# 724. Тесты для функции `choose_string_with_most_digits`
def test_choose_string_with_most_digits():
    assert choose_string_with_most_digits("abc123", "def45", "gh6789") == "gh6789"
    assert choose_string_with_most_digits("123", "456", "789") == "789"
    assert choose_string_with_most_digits("abc", "def", "ghi") == 'ghi'
    assert choose_string_with_most_digits("ab123cd", "ef45gh", "ij678kl") == "ij678kl"
    assert choose_string_with_most_digits("abc1", "def2", "ghi3") == "ghi3"
    assert choose_string_with_most_digits("123abc", "456def", "789ghi") == "789ghi"


# 725. Тесты для функции `choose_largest_in_range`
def test_choose_largest_in_range():
    assert choose_largest_in_range(1, 10, 5, 3, 8, 15) == 8
    assert choose_largest_in_range(0, 100, 50, 60, 70) == 70
    assert choose_largest_in_range(-10, 10, -5, 0, 5) == 5
    assert choose_largest_in_range(10, 20, 5, 25, 30) == "No numbers in the range (10, 20)"
    assert choose_largest_in_range(1, 5, 2, 3, 4) == 4
    assert choose_largest_in_range(100, 200, 150, 175, 190) == 190


# 726. Тесты для функции `choose_first_even_number`
def test_choose_first_even_number():
    assert choose_first_even_number([1, 3, 5, 7]) == "No even numbers"
    assert choose_first_even_number([2, 4, 6, 8]) == 2
    assert choose_first_even_number([1, 2, 3, 4]) == 2
    assert choose_first_even_number([5, 7, 8, 10]) == 8
    assert choose_first_even_number([10, 20, 30]) == 10
    assert choose_first_even_number([1, 3, 7]) == "No even numbers"


# 727. Тесты для функции `choose_shortest_no_space_string`
def test_choose_shortest_no_space_string():
    assert choose_shortest_no_space_string("hello", "world", "hi") == "hi"
    assert choose_shortest_no_space_string("a b c", "de bf", "g h") == 'No string without spaces'
    assert choose_shortest_no_space_string("one", "two", "three") == "one"
    assert choose_shortest_no_space_string("no spaces", "he re", "or here") == 'No string without spaces'
    assert choose_shortest_no_space_string("apple", "banana", "cherry") == "apple"
    assert choose_shortest_no_space_string("ab", "abc", "abcd") == "ab"


# 728. Тесты для функции `choose_youngest_age`
def test_choose_youngest_age():
    assert choose_youngest_age(25, 30, 20, 35) == 20
    assert choose_youngest_age(40, 50, 30, 20) == 20
    assert choose_youngest_age(15, 20, 25, 10) == 10
    assert choose_youngest_age(60, 55, 45, 35) == 35
    assert choose_youngest_age(5, 10, 15, 20) == 5
    assert choose_youngest_age(100, 90, 80, 70) == 70


# 729. Тесты для функции `choose_string_with_most_unique_chars`
def test_choose_string_with_most_unique_chars():
    assert choose_string_with_most_unique_chars("apple", "banana", "cherry") == 'cherry'
    assert choose_string_with_most_unique_chars("cat", "dog", "elephant") == "elephant"
    assert choose_string_with_most_unique_chars("abcd", "efgh", "ijkl") == "abcd"
    assert choose_string_with_most_unique_chars("unique", "characters", "test") == "characters"
    assert choose_string_with_most_unique_chars("simple", "complex", "word") == "complex"
    assert choose_string_with_most_unique_chars("first", "second", "third") == "second"


# 730. Тесты для функции `choose_first_even_divisible_by_three`
def test_choose_first_even_divisible_by_three():
    assert choose_first_even_divisible_by_three([1, 3, 5, 7]) == "No even number divisible by 3"
    assert choose_first_even_divisible_by_three([2, 4, 6, 8]) == 6
    assert choose_first_even_divisible_by_three([12, 18, 24]) == 12
    assert choose_first_even_divisible_by_three([7, 14, 21, 28]) == 'No even number divisible by 3'
    assert choose_first_even_divisible_by_three([3, 6, 9, 12]) == 6
    assert choose_first_even_divisible_by_three([2, 5, 8, 11]) == "No even number divisible by 3"


# 731. Тесты для функции `choose_largest_less_than`
def test_choose_largest_less_than():
    assert choose_largest_less_than(10, 1, 2, 3, 4) == 4
    assert choose_largest_less_than(-20, 1, 2, 3) == 'No numbers less than -20'
    assert choose_largest_less_than(0, -1, -2, -3) == -1
    assert choose_largest_less_than(1, 5, 6, 8) == 'No numbers less than 1'
    assert choose_largest_less_than(15, 10, 12, 14) == 14
    assert choose_largest_less_than(2, 1, 3, 5) == 1


# 732. Тесты для функции `choose_first_greater_than`
def test_choose_first_greater_than():
    assert choose_first_greater_than(10, 5, 15, 20) == 15
    assert choose_first_greater_than(0, 1, 2, 3) == 1
    assert choose_first_greater_than(-5, -1, 0, 5) == -1
    assert choose_first_greater_than(100, 150, 200, 250) == 150
    assert choose_first_greater_than(3, 2, 4, 5) == 4
    assert choose_first_greater_than(10, 5, 6, 7) == f"No numbers greater than 10"


# 733. Тесты для функции `choose_string_with_length_divisible_by_three`
def test_choose_string_with_length_divisible_by_three():
    assert choose_string_with_length_divisible_by_three("abcd", "defg", "hijklmn") == "No string with length divisible by 3"
    assert choose_string_with_length_divisible_by_three("abcdefgh", "ijklmnopqrs", "tuv") == "tuv"
    assert choose_string_with_length_divisible_by_three("123456", "789", "0123") == "123456"
    assert choose_string_with_length_divisible_by_three("aaaaaa", "bbbbbbb", "ccccccccc") == "aaaaaa"
    assert choose_string_with_length_divisible_by_three("hello", "world", "test") == "No string with length divisible by 3"
    assert choose_string_with_length_divisible_by_three("one", "two", "three") == 'one'


# 734. Тесты для функции `choose_most_expensive_item`
def test_choose_most_expensive_item():
    assert choose_most_expensive_item({"name": "item1", "price": 10}, {"name": "item2", "price": 20}, {"name": "item3", "price": 30}) == {"name": "item3", "price": 30}
    assert choose_most_expensive_item({"name": "item4", "price": 5}, {"name": "item5", "price": 15}, {"name": "item6", "price": 25}) == {"name": "item6", "price": 25}
    assert choose_most_expensive_item({"name": "item7", "price": 100}, {"name": "item8", "price": 200}, {"name": "item9", "price": 300}) == {"name": "item9", "price": 300}
    assert choose_most_expensive_item({"name": "item10", "price": 50}, {"name": "item11", "price": 75}, {"name": "item12", "price": 100}) == {"name": "item12", "price": 100}
    assert choose_most_expensive_item({"name": "item13", "price": 60}, {"name": "item14", "price": 80}, {"name": "item15", "price": 120}) == {"name": "item15", "price": 120}
    assert choose_most_expensive_item({"name": "item16", "price": 10}, {"name": "item17", "price": 5}) == {"name": "item16", "price": 10}


# 735. Тесты для функции `choose_string_shorter_than`
def test_choose_string_shorter_than():
    assert choose_string_shorter_than(5, "apple", "cat", "banana") == "cat"
    assert choose_string_shorter_than(4, "dog", "fish", "whale") == "dog"
    assert choose_string_shorter_than(7, "elephant", "snake", "shark") == "snake"
    assert choose_string_shorter_than(3, "sun", "moon", "star") is None
    assert choose_string_shorter_than(6, "planet", "comet", "asteroid") == "comet"
    assert choose_string_shorter_than(8, "galaxy", "universe", "cosmos") == "galaxy"


# 736. Тесты для функции `choose_first_not_divisible_by_2_and_3`
def test_choose_first_not_divisible_by_2_and_3():
    assert choose_first_not_divisible_by_2_and_3([1, 2, 3, 4, 5]) == 1
    assert choose_first_not_divisible_by_2_and_3([6, 9, 12, 15]) is None
    assert choose_first_not_divisible_by_2_and_3([7, 14, 21, 28]) == 7
    assert choose_first_not_divisible_by_2_and_3([8, 11, 13, 16]) == 11
    assert choose_first_not_divisible_by_2_and_3([10, 25, 30, 45]) == 25
    assert choose_first_not_divisible_by_2_and_3([17, 34, 51, 68]) == 17


# 737. Тесты для функции `choose_word_with_only_vowels`
def test_choose_word_with_only_vowels():
    assert choose_word_with_only_vowels("aeiou", "io", "u") == "aeiou"
    assert choose_word_with_only_vowels("aaaa", "eieio", "iiiii") == "aaaa"
    assert choose_word_with_only_vowels("oo", "u", "eeee") == "oo"
    assert choose_word_with_only_vowels("ui", "oe", "aa") == "ui"
    assert choose_word_with_only_vowels("o", "e", "i") == "o"
    assert choose_word_with_only_vowels("apple", "banana", "cherry") is None


# 738. Тесты для функции `choose_largest_less_than_or_equal_to`
def test_choose_largest_less_than_or_equal_to():
    assert choose_largest_less_than_or_equal_to(10, 1, 2, 3, 4) == 4
    assert choose_largest_less_than_or_equal_to(5, 1, 2, 3) == 3
    assert choose_largest_less_than_or_equal_to(0, -1, -2, -3) == -1
    assert choose_largest_less_than_or_equal_to(7, 5, 6, 8) == 6
    assert choose_largest_less_than_or_equal_to(15, 10, 12, 14) == 14
    assert choose_largest_less_than_or_equal_to(2, 1, 3, 5) == 1


# 739. Тесты для функции `choose_longest_digit_string`
def test_choose_longest_digit_string():
    assert choose_longest_digit_string("123", "45678", "90") == "45678"
    assert choose_longest_digit_string("112233", "44556677", "889900") == "44556677"
    assert choose_longest_digit_string("abc123", "def456", "ghi789") is None
    assert choose_longest_digit_string("111", "2222", "333") == "2222"
    assert choose_longest_digit_string("99999", "8888", "7777") == "99999"
    assert choose_longest_digit_string("1234567890", "0987654321", "1112131415") == "1234567890"


# 740. Тесты для функции `choose_shortest_string_without_vowels`
def test_choose_shortest_string_without_vowels():
    assert choose_shortest_string_without_vowels("bcdf", "ghjkl", "mnpqr") == "bcdf"
    assert choose_shortest_string_without_vowels("bcdfg", "hjklm", "npqr") == "npqr"
    assert choose_shortest_string_without_vowels("b", "c", "d") == "b"
    assert choose_shortest_string_without_vowels("xyz", "wxy", "uvw") == 'xyz'
    assert choose_shortest_string_without_vowels("apple", "banana", "cherry") is None
    assert choose_shortest_string_without_vowels("bcd", "ghj", "mn") == "mn"


# 741. Тесты для функции `choose_largest_even_less_than`:
def test_choose_largest_even_less_than():
    assert choose_largest_even_less_than(10, 1, 2, 3, 4, 5, 6, 7, 8, 9) == 8
    assert choose_largest_even_less_than(5, 1, 3, 5) is None
    assert choose_largest_even_less_than(20, 10, 15, 20, 25) == 10


# 742. Тесты для функции `choose_second_smallest`:
def test_choose_second_smallest():
    assert choose_second_smallest(5, 3, 8, 6, 7, 2) == 3
    assert choose_second_smallest(4, 4, 4) is None
    assert choose_second_smallest(8, 1, 4, 5, 7) == 4


# 743. Тесты для функции `choose_string_start_and_end_same`:
def test_choose_string_start_and_end_same():
    assert choose_string_start_and_end_same("level", "racecar", "deified") == "level"
    assert choose_string_start_and_end_same("hello", "world") is None
    assert choose_string_start_and_end_same("anna", "noon") == "anna"


# 744. Тесты для функции `choose_first_divisible_by_5_and_7`:
def test_choose_first_divisible_by_5_and_7():
    assert choose_first_divisible_by_5_and_7([35, 70, 10, 14, 21]) == 35
    assert choose_first_divisible_by_5_and_7([2, 4, 7, 8, 10]) is None
    assert choose_first_divisible_by_5_and_7([105, 140, 28, 49]) == 105


# 745. Тесты для функции `choose_shortest_string_with_digit`:
def test_choose_shortest_string_with_digit():
    assert choose_shortest_string_with_digit("abc1", "a2b", "abcd3") == 'abc1'
    assert choose_shortest_string_with_digit("abc", "def") is None
    assert choose_shortest_string_with_digit("12345", "67890") == "12345"


# 746. Тесты для функции `choose_most_expensive_below_price`:
def test_choose_most_expensive_below_price():
    assert choose_most_expensive_below_price(120, *[{'name': 'item1', 'price': 50}, {'name': 'item2', 'price': 100}, {'name': 'item3', 'price': 150}]) == {'name': 'item2', 'price': 100}
    assert choose_most_expensive_below_price(40, *[{'name': 'item1', 'price': 50}, {'name': 'item2', 'price': 100}, {'name': 'item3', 'price': 150}]) is None
    assert choose_most_expensive_below_price(60, *[{'name': 'item1', 'price': 50}, {'name': 'item2', 'price': 100}, {'name': 'item3', 'price': 150}]) == {'name': 'item1', 'price': 50}


# 747. Тесты для функции `choose_first_square_number`:
def test_choose_first_square_number():
    assert choose_first_square_number([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
    assert choose_first_square_number([10, 15, 20, 25, 30]) == 25
    assert choose_first_square_number([2, 3, 5, 6, 7]) is None


# 748. Тесты для функции `choose_oldest_age`:
def test_choose_oldest_age():
    assert choose_oldest_age(20, 35, 50, 40) == 50
    assert choose_oldest_age(18, 12, 15) == 18
    assert choose_oldest_age(70, 85, 90, 95) == 95


# 749. Тесты для функции `choose_first_divisible_by_2_not_3`:
def test_choose_first_divisible_by_2_not_3():
    assert choose_first_divisible_by_2_not_3([4, 6, 8, 9, 12]) == 4
    assert choose_first_divisible_by_2_not_3([9, 15, 21, 33]) is None
    assert choose_first_divisible_by_2_not_3([10, 14, 20, 22]) == 10


# 750. Тесты для функции `choose_longest_all_digits_string`:
def test_choose_longest_all_digits_string():
    assert choose_longest_all_digits_string("123", "12345", "678") == "12345"
    assert choose_longest_all_digits_string("abc", "def") is None
    assert choose_longest_all_digits_string("12", "3456", "7890") == "3456"


# 751. Тесты для функции `choose_first_even_greater_than`:
def test_choose_first_even_greater_than():
    assert choose_first_even_greater_than(10, 11, 12, 13, 14) == 12
    assert choose_first_even_greater_than(15, 20, 22, 24, 26) == 20
    assert choose_first_even_greater_than(30, 25, 35) is None


# 752. Тесты для функции `choose_first_non_numeric_string`:
def test_choose_first_non_numeric_string():
    assert choose_first_non_numeric_string("123", "abc", "456", "789") == "abc"
    assert choose_first_non_numeric_string("001", "010") is None
    assert choose_first_non_numeric_string("apple", "banana", "cherry") == "apple"


# 753. Тесты для функции `choose_palindrome`:
def test_choose_palindrome():
    assert choose_palindrome("level", "world", "racecar") == "level"
    assert choose_palindrome("hello", "world") is None
    assert choose_palindrome("noon", "deified", "civic") == "noon"


# 754. Тесты для функции `choose_most_expensive_under_100`:
def test_choose_most_expensive_under_100():
    assert choose_most_expensive_under_100(*[{'name': 'item1', 'price': 60}, {'name': 'item2', 'price': 80}, {'name': 'item3', 'price': 100}]) == {'name': 'item3', 'price': 100}
    assert choose_most_expensive_under_100({'name': 'item4', 'price': 110}) is None
    assert choose_most_expensive_under_100({'name': 'item5', 'price': 90}) == {'name': 'item5', 'price': 90}


# 755. Тесты для функции `choose_first_even_greater_than_10`:
def test_choose_first_even_greater_than_10():
    assert choose_first_even_greater_than_10([9, 11, 13, 14, 16]) == 14
    assert choose_first_even_greater_than_10([5, 7, 8, 10]) is None
    assert choose_first_even_greater_than_10([12, 15, 18, 20]) == 12


# 756. Тесты для функции `choose_smallest_divisible_by_5`:
def test_choose_smallest_divisible_by_5():
    assert choose_smallest_divisible_by_5(10, 25, 30, 15) == 10
    assert choose_smallest_divisible_by_5(4, 8, 16, 32) is None
    assert choose_smallest_divisible_by_5(45, 50, 55) == 45


# 757. Тесты для функции `choose_first_long_word_starting_with_consonant`:
def test_choose_first_long_word_starting_with_consonant():
    assert choose_first_long_word_starting_with_consonant("banana", "strawberry", "apple", "grape") == 'banana'
    assert choose_first_long_word_starting_with_consonant("orange", "apricot", "kiwi") is None
    assert choose_first_long_word_starting_with_consonant("blackberry", "blueberry", "raspberry") == "blackberry"


# 758. Тесты для функции `choose_largest_less_than_20`:
def test_choose_largest_less_than_20():
    assert choose_largest_less_than_20(5, 10, 15, 18) == 18
    assert choose_largest_less_than_20(20, 21, 22) is None
    assert choose_largest_less_than_20(19, 1, 3, 6, 14) == 19


# 759. Тесты для функции `choose_string_starting_with_uppercase`:
def test_choose_string_starting_with_uppercase():
    assert choose_string_starting_with_uppercase("Apple", "banana", "Cherry", "date") == "Apple"
    assert choose_string_starting_with_uppercase("eggplant", "fig", "grape") is None
    assert choose_string_starting_with_uppercase("Honeydew", "Ice", "Juice") == "Honeydew"


# 760. Тесты для функции `choose_first_non_even_non_prime`:
def test_choose_first_non_even_non_prime():
    assert choose_first_non_even_non_prime([2, 4, 6, 9, 12, 15]) == 9
    assert choose_first_non_even_non_prime([2, 3, 5, 7, 11]) is None
    assert choose_first_non_even_non_prime([1, 22, 25, 28]) == 1


# 761. Тесты для функции `choose_shortest_string_starting_with_digit`:
def test_choose_shortest_string_starting_with_digit():
    assert choose_shortest_string_starting_with_digit("abc", "1abc", "2a") == "1abc"
    assert choose_shortest_string_starting_with_digit("abc", "abc1", "2a") == "2a"
    assert choose_shortest_string_starting_with_digit("abc", "a1bc", "abc") is None
    assert choose_shortest_string_starting_with_digit("1abc", "2abc", "3abc") == "1abc"
    assert choose_shortest_string_starting_with_digit("123", "456", "789") == "123"
    assert choose_shortest_string_starting_with_digit("abc", "def", "ghi") is None


# 762. Тесты для функции `choose_anagram_of`:
def test_choose_anagram_of():
    assert choose_anagram_of("listen", "enlist", "google", "inlets") == "enlist"
    assert choose_anagram_of("listen", "google", "facebook", "silent") == "silent"
    assert choose_anagram_of("abc", "def", "ghi", "jkl") is None
    assert choose_anagram_of("cat", "tac", "act") == "tac"
    assert choose_anagram_of("cat", "dog", "god") is None
    assert choose_anagram_of("abc", "bca", "cab", "bac") == "bca"


# 763. Тесты для функции `choose_smallest_greater_than`:
def test_choose_smallest_greater_than():
    assert choose_smallest_greater_than(5, 1, 2, 6, 8, 7) == 6
    assert choose_smallest_greater_than(3, 4, 5, 1, 2, 6) == 4
    assert choose_smallest_greater_than(10, 11, 12, 13, 14) == 11
    assert choose_smallest_greater_than(0, -1, -2, 1, 2, 3) == 1
    assert choose_smallest_greater_than(50, 100, 200, 300) == 100
    assert choose_smallest_greater_than(100, 50, 60, 70, 80) is None


# 764. Тесты для функции `choose_first_even_length_word`:
def test_choose_first_even_length_word():
    assert choose_first_even_length_word("one", "two", "three", "four") == "four"
    assert choose_first_even_length_word("hello", "world", "Python") == 'Python'
    assert choose_first_even_length_word("apple", "banana", "cherry", "dates") == "banana"
    assert choose_first_even_length_word("apple", "b", "c", "dd") == "dd"
    assert choose_first_even_length_word("a", "bb", "ccc", "dddd") == "bb"
    assert choose_first_even_length_word("a", "b", "c", "d") is None


# 765. Тесты для функции `choose_longer_than_average`:
def test_choose_longer_than_average():
    assert choose_longer_than_average("a", "bb", "ccc", "dddd") == 'ccc'
    assert choose_longer_than_average("short", "longer", "longest") == 'longest'
    assert choose_longer_than_average("aa", "bbb", "cccc") == 'cccc'
    assert choose_longer_than_average("one", "one", "one", "one") is None
    assert choose_longer_than_average("one", "two", "three") == "three"
    assert choose_longer_than_average("a", "a", "a") is None


# 766. Тесты для функции `choose_string_with_only_letters`:
def test_choose_string_with_only_letters():
    assert choose_string_with_only_letters("abc123", "def456", "ghi789") is None
    assert choose_string_with_only_letters("abc", "def", "ghi") == "abc"
    assert choose_string_with_only_letters("123", "456", "789") is None
    assert choose_string_with_only_letters("abc", "def", "123") == "abc"
    assert choose_string_with_only_letters("abc123", "def", "ghi") == "def"
    assert choose_string_with_only_letters("abc", "123", "def456") == "abc"


# 767. Тесты для функции `choose_oldest_under_30`:
def test_choose_oldest_under_30():
    assert choose_oldest_under_30(25, 20, 18, 22) == 25
    assert choose_oldest_under_30(10, 15, 30, 35) == 15
    assert choose_oldest_under_30(30, 40, 50) is None
    assert choose_oldest_under_30(29, 28, 27, 26) == 29
    assert choose_oldest_under_30(25, 29, 21, 28) == 29
    assert choose_oldest_under_30(20, 19, 18, 25) == 25


# 768. Тесты для функции `choose_multiple_of_4_not_5`:
def test_choose_multiple_of_4_not_5():
    assert choose_multiple_of_4_not_5([4, 8, 12, 16, 20]) == 4
    assert choose_multiple_of_4_not_5([5, 10, 15, 20, 25]) is None
    assert choose_multiple_of_4_not_5([7, 14, 21, 28, 35]) == 28
    assert choose_multiple_of_4_not_5([8, 16, 24, 32, 40]) == 8
    assert choose_multiple_of_4_not_5([6, 12, 18, 24, 30]) == 12
    assert choose_multiple_of_4_not_5([3, 6, 9, 12, 15]) == 12


# 769. Тесты для функции `choose_string_length_divisible_by_3`:
def test_choose_string_length_divisible_by_3():
    assert choose_string_length_divisible_by_3("a", "bb", "ccc", "dddd", "eeeee") == "ccc"
    assert choose_string_length_divisible_by_3("abcdef", "ghijk", "lmnopqr") == "abcdef"
    assert choose_string_length_divisible_by_3("a", "b", "c") is None
    assert choose_string_length_divisible_by_3("123", "456", "789") == "123"
    assert choose_string_length_divisible_by_3("111", "222", "333") == "111"
    assert choose_string_length_divisible_by_3("a", "bbb", "cc", "ddd") == "bbb"


# 770. Тесты для функции `choose_smallest_even_greater_than_10`:
def test_choose_smallest_even_greater_than_10():
    assert choose_smallest_even_greater_than_10(12, 14, 16, 18, 20) == 12
    assert choose_smallest_even_greater_than_10(21, 22, 23, 24, 25) == 22
    assert choose_smallest_even_greater_than_10(10, 11, 12, 13, 14) == 12
    assert choose_smallest_even_greater_than_10(30, 32, 34, 36) == 30
    assert choose_smallest_even_greater_than_10(8, 9, 10, 11, 12) == 12
    assert choose_smallest_even_greater_than_10(50, 60, 70) == 50


# 771. Тесты для функции `choose_first_divisible_by_2_and_5`:
def test_choose_first_divisible_by_2_and_5():
    assert choose_first_divisible_by_2_and_5([10, 20, 30, 40, 50]) == 10
    assert choose_first_divisible_by_2_and_5([5, 10, 15, 20, 25]) == 10
    assert choose_first_divisible_by_2_and_5([1, 3, 5, 7, 9]) is None
    assert choose_first_divisible_by_2_and_5([2, 4, 6, 8, 10]) == 10
    assert choose_first_divisible_by_2_and_5([12, 14, 16, 18, 20]) == 20
    assert choose_first_divisible_by_2_and_5([15, 25, 35, 45, 50]) == 50


# 772. Тесты для функции `choose_longest_non_digit_starting_string`:
def test_choose_longest_non_digit_starting_string():
    assert choose_longest_non_digit_starting_string("abc1", "def2", "ghi3") == "abc1"
    assert choose_longest_non_digit_starting_string("1abc", "2def", "3ghi") is None
    assert choose_longest_non_digit_starting_string("abcd", "efgh", "ijkl") == "abcd"
    assert choose_longest_non_digit_starting_string("1abcd", "2efgh", "3ijkl") is None
    assert choose_longest_non_digit_starting_string("abcd", "1efgh", "ijkl") == "abcd"
    assert choose_longest_non_digit_starting_string("1abcd", "efgh", "ijkl") == "efgh"


# 773. Тесты для функции `choose_first_all_uppercase_word`:
def test_choose_first_all_uppercase_word():
    assert choose_first_all_uppercase_word("HELLO", "WORLD", "PYTHON") == "HELLO"
    assert choose_first_all_uppercase_word("hello", "WORLD", "python") == "WORLD"
    assert choose_first_all_uppercase_word("hello", "world", "python") is None
    assert choose_first_all_uppercase_word("HELLO", "WORLD", "PYTHON") == "HELLO"
    assert choose_first_all_uppercase_word("hello", "WORLD", "PYTHON") == "WORLD"
    assert choose_first_all_uppercase_word("hello", "world", "PYTHON") == "PYTHON"


# 774. Тесты для функции `choose_youngest_over_50`:
def test_choose_youngest_over_50():
    assert choose_youngest_over_50(55, 60, 65, 70) == 55
    assert choose_youngest_over_50(50, 55, 60, 65) == 55
    assert choose_youngest_over_50(40, 45, 50, 55) == 55
    assert choose_youngest_over_50(45, 50, 55, 60) == 55
    assert choose_youngest_over_50(35, 40, 45, 50) is None
    assert choose_youngest_over_50(25, 30, 35, 40) is None


# 775. Тесты для функции `choose_largest_multiple_of_3_not_2`:
def test_choose_largest_multiple_of_3_not_2():
    assert choose_largest_multiple_of_3_not_2([3, 6, 9, 12, 15]) == 15
    assert choose_largest_multiple_of_3_not_2([1, 2, 3, 4, 5]) == 3
    assert choose_largest_multiple_of_3_not_2([5, 10, 15, 20, 25]) == 15
    assert choose_largest_multiple_of_3_not_2([9, 18, 27, 36, 45]) == 45
    assert choose_largest_multiple_of_3_not_2([12, 24, 36, 48, 60]) is None
    assert choose_largest_multiple_of_3_not_2([11, 22, 33, 44, 55]) == 33


# 776. Тесты для функции `choose_string_with_uppercase_and_digit`:
def test_choose_string_with_uppercase_and_digit():
    assert choose_string_with_uppercase_and_digit("Abc1", "def2", "ghi3") == "Abc1"
    assert choose_string_with_uppercase_and_digit("1abc", "2def", "3ghi") is None
    assert choose_string_with_uppercase_and_digit("Abc", "def", "Ghi") is None
    assert choose_string_with_uppercase_and_digit("Abc1", "Def2", "Ghi3") == "Abc1"
    assert choose_string_with_uppercase_and_digit("1Abc", "2Def", "3Ghi") == "1Abc"
    assert choose_string_with_uppercase_and_digit("abc1", "def2", "ghi3") is None


# 777. Тесты для функции `choose_first_even_less_than_50`:
def test_choose_first_even_less_than_50():
    assert choose_first_even_less_than_50([10, 20, 30, 40, 50]) == 10
    assert choose_first_even_less_than_50([5, 10, 15, 20, 25]) == 10
    assert choose_first_even_less_than_50([1, 3, 5, 7, 9]) is None
    assert choose_first_even_less_than_50([2, 4, 6, 8, 10]) == 2
    assert choose_first_even_less_than_50([12, 14, 16, 18, 20]) == 12
    assert choose_first_even_less_than_50([15, 25, 35, 45, 50]) is None


# 778. Тесты для функции `choose_shortest_no_space_string_3`:
def test_choose_shortest_no_space_string_3():
    assert choose_shortest_no_space_string_3("hello", "world", "python") == "hello"
    assert choose_shortest_no_space_string_3("this is a test", "no spaces here", "short") == "short"
    assert choose_shortest_no_space_string_3("a", "ab", "abc") == "a"
    assert choose_shortest_no_space_string_3("abc", "abcd", "abcdef") == "abc"
    assert choose_shortest_no_space_string_3("hello world", "python programming", "short text") is None
    assert choose_shortest_no_space_string_3("no space", "shortest", "longest text") == "shortest"


# 779. Тесты для функции `choose_repeated_string`:
def test_choose_repeated_string():
    assert choose_repeated_string("abcabc", "defdef", "ghighi") == "abcabc"
    assert choose_repeated_string("hello", "world", "python") is None
    assert choose_repeated_string("aabbcc", "ddeeff", "gghhii") is None
    assert choose_repeated_string("abcabc", "abc", "def") == "abcabc"
    assert choose_repeated_string("xyzxyz", "xyz", "xyxxyx") == "xyzxyz"
    assert choose_repeated_string("repeatrepeat", "repe", "repeated") == "repeatrepeat"


# 780. Тесты для функции `choose_number_in_range_0_100`:
def test_choose_number_in_range_0_100():
    assert choose_number_in_range_0_100(0, 10, 20, 30, 40) == 10
    assert choose_number_in_range_0_100(50, 60, 70, 80, 90) == 50
    assert choose_number_in_range_0_100(100, 110, 120, 130, 140) == 100
    assert choose_number_in_range_0_100(-10, -20, -30) is None
    assert choose_number_in_range_0_100(-15, -25, -35, -45, -55) is None
    assert choose_number_in_range_0_100(1, 2, 3, 4, 5) == 1


# 781. Тесты для функции `choose_smallest_odd_number`:
def test_choose_smallest_odd_number():
    assert choose_smallest_odd_number(5, 3, 9) == 3
    assert choose_smallest_odd_number(2, 4, 6) is None
    assert choose_smallest_odd_number(7, 3, -1, -5) == -5
    assert choose_smallest_odd_number(1, 1, 1) == 1
    assert choose_smallest_odd_number() is None
    assert choose_smallest_odd_number(4, 9, 11) == 9


# 782. Тесты для функции `choose_first_greater_than_100_even`:
def test_choose_first_greater_than_100_even():
    assert choose_first_greater_than_100_even([101, 102, 103]) == 102
    assert choose_first_greater_than_100_even([100, 99, 98]) is None
    assert choose_first_greater_than_100_even([150, 101, 200]) == 150
    assert choose_first_greater_than_100_even([]) is None
    assert choose_first_greater_than_100_even([200, 150, 180]) == 200
    assert choose_first_greater_than_100_even([123, 245, 132]) == 132


# 783. Тесты для функции `choose_longest_digit_word`:
def test_choose_longest_digit_word():
    assert choose_longest_digit_word("123", "4567", "89") == "4567"
    assert choose_longest_digit_word("abc", "def", "ghi") is None
    assert choose_longest_digit_word("1", "22", "333", "4444", "55555") == "55555"
    assert choose_longest_digit_word() is None
    assert choose_longest_digit_word("789", "12", "234") == "789"
    assert choose_longest_digit_word("10", "20", "30", "40") == "10"


# 784. Тесты для функции `is_prime_using_set`:
def test_is_prime_using_set():
    assert is_prime_using_set(2) is True
    assert is_prime_using_set(3) is True
    assert is_prime_using_set(4) is False
    assert is_prime_using_set(-1) is False
    assert is_prime_using_set(11) is True
    assert is_prime_using_set(1) is False
    assert is_prime_using_set(0) is False
    assert is_prime_using_set(5) is True
    assert is_prime_using_set(9) is False


# 785. Тесты для функции `count_multiples_of`:
def test_count_multiples_of():
    assert count_multiples_of(3, [3, 6, 9, 12]) == 4
    assert count_multiples_of(5, [1, 2, 3, 4]) is None
    assert count_multiples_of(2, [4, 6, 8, 10]) == 4
    assert count_multiples_of(7, [14, 21, 28, 35]) == 4
    assert count_multiples_of(1, [1, 2, 3, 4, 5]) == 5
    assert count_multiples_of(10, [10, 20, 30, 40]) == 4


# 786. Тесты для функции `find_divisible_by_all_in_set`:
def test_find_divisible_by_all_in_set():
    assert find_divisible_by_all_in_set({1, 2, 3}, 6) == 6
    assert find_divisible_by_all_in_set({2, 3}, 5) is None
    assert find_divisible_by_all_in_set({5, 10, 15}, 30) == 30
    assert find_divisible_by_all_in_set({3, 9, 27}, 81) == 81
    assert find_divisible_by_all_in_set({2, 4, 8}, 16) == 16
    assert find_divisible_by_all_in_set({3, 6, 12}, 12) == 12


# 787. Тесты для функции `find_number_not_in_dict`:
def test_find_number_not_in_dict():
    assert find_number_not_in_dict({1: 'a', 2: 'b', 3: 'c'}, 4) == 4
    assert find_number_not_in_dict({1: 'a', 2: 'b', 3: 'c'}, 2) is None
    assert find_number_not_in_dict({}, 1) == 1
    assert find_number_not_in_dict({5: 'x', 6: 'y', 7: 'z'}, 8) == 8
    assert find_number_not_in_dict({9: 'a', 10: 'b'}, 10) is None
    assert find_number_not_in_dict({100: 'a', 200: 'b'}, 150) == 150


# 788. Тесты для функции `find_max_divisible`:
def test_find_max_divisible():
    assert find_max_divisible([12, 15, 20, 30], 5) == 30
    assert find_max_divisible([7, 14, 21, 28], 3) == 21
    assert find_max_divisible([8, 16, 24], 4) == 24
    assert find_max_divisible([1, 2, 3, 4], 5) is None
    assert find_max_divisible([9, 18, 27, 36], 9) == 36
    assert find_max_divisible([], 5) is None


# 789. Тесты для функции `find_not_divisible_by_2_3_5`:
def test_find_not_divisible_by_2_3_5():
    assert find_not_divisible_by_2_3_5([7, 11, 13, 17]) == [7, 11, 13, 17]
    assert find_not_divisible_by_2_3_5([6, 10, 15, 20]) is None
    assert find_not_divisible_by_2_3_5([1, 2, 3, 5, 7]) == [1, 7]
    assert find_not_divisible_by_2_3_5([9, 18, 27, 35]) is None
    assert find_not_divisible_by_2_3_5([8, 16, 24, 30]) is None
    assert find_not_divisible_by_2_3_5([19, 23, 29, 31]) == [19, 23, 29, 31]


# 790. Тесты для функции `sum_of_elements_greater_than`:
def test_sum_of_elements_greater_than():
    assert sum_of_elements_greater_than(10, {12, 15, 20}) == 47
    assert sum_of_elements_greater_than(25, {5, 10, 15, 20}) is None
    assert sum_of_elements_greater_than(0, {1, 2, 3, 4}) == 10
    assert sum_of_elements_greater_than(5, {10, 20, 30}) == 60
    assert sum_of_elements_greater_than(100, {50, 75, 125}) == 125
    assert sum_of_elements_greater_than(-5, {1, 2, 3, 4}) == 10


# 791. Тесты для функции `max_difference_in_dict`:
def test_max_difference_in_dict():
    assert max_difference_in_dict({1: 10, 2: 20, 3: 30}) == 20
    assert max_difference_in_dict({}) is None
    assert max_difference_in_dict({4: 50}) is None
    assert max_difference_in_dict({5: 5, 6: 10, 7: 15}) == 10
    assert max_difference_in_dict({10: 100, 20: 200}) == 100
    assert max_difference_in_dict({8: 8, 9: 18, 10: 28}) == 20


# 792. Тесты для функции `average_of_set`:
def test_average_of_set():
    assert average_of_set({1, 2, 3, 4}) == 2.5
    assert average_of_set({10, 20, 30}) == 20.0
    assert average_of_set(set()) is None
    assert average_of_set({5, 15, 25, 35}) == 20.0
    assert average_of_set({100}) == 100.0
    assert average_of_set({1, 3, 5, 7, 9}) == 5.0


# 793. Тесты для функции `find_greater_than_and_not_divisible_by_2`:
def test_find_greater_than_and_not_divisible_by_2():
    assert find_greater_than_and_not_divisible_by_2([1, 3, 5, 7, 9], 4) == [5, 7, 9]
    assert find_greater_than_and_not_divisible_by_2([2, 4, 6, 8], 3) is None
    assert find_greater_than_and_not_divisible_by_2([11, 13, 17, 19], 10) == [11, 13, 17, 19]
    assert find_greater_than_and_not_divisible_by_2([], 5) is None
    assert find_greater_than_and_not_divisible_by_2([5, 15, 25, 35], 10) == [15, 25, 35]
    assert find_greater_than_and_not_divisible_by_2([21, 23, 25, 27], 22) == [23, 25, 27]


# 794. Тесты для функции `find_min_divisible_by_all`:
def test_find_min_divisible_by_all():
    assert find_min_divisible_by_all([1, 2, 3]) is None
    assert find_min_divisible_by_all([5, 10, 15]) is None
    assert find_min_divisible_by_all([4, 8, 16]) == 16
    assert find_min_divisible_by_all([7, 14, 28]) == 28
    assert find_min_divisible_by_all([2, 3, 5]) is None
    assert find_min_divisible_by_all([3, 5, 7, 11]) is None


# 795. Тесты для функции `find_smallest_key_greater_than`:
def test_find_smallest_key_greater_than():
    assert find_smallest_key_greater_than({1: 10, 2: 20, 3: 30}, 15) == 2
    assert find_smallest_key_greater_than({4: 40, 5: 50}, 60) is None
    assert find_smallest_key_greater_than({6: 60, 7: 70, 8: 80}, 65) == 7
    assert find_smallest_key_greater_than({}, 10) is None
    assert find_smallest_key_greater_than({9: 90, 10: 100}, 95) == 10
    assert find_smallest_key_greater_than({11: 110, 12: 120}, 105) == 11


# 796. Тесты для функции `find_first_square_greater_than`:
def test_find_first_square_greater_than():
    assert find_first_square_greater_than([1, 4, 9, 16], 5) == 9
    assert find_first_square_greater_than([25, 36, 49], 30) == 36
    assert find_first_square_greater_than([2, 3, 5], 6) is None
    assert find_first_square_greater_than([81, 64, 49], 50) == 81
    assert find_first_square_greater_than([], 10) is None
    assert find_first_square_greater_than([100, 121, 144], 110) == 121


# 797. Тесты для функции `find_first_divisible_by_2_and_3`:
def test_find_first_divisible_by_2_and_3():
    assert find_first_divisible_by_2_and_3({6, 12, 18}) == 18
    assert find_first_divisible_by_2_and_3({1, 3, 5}) is None
    assert find_first_divisible_by_2_and_3({24, 30, 36}) == 24
    assert find_first_divisible_by_2_and_3(set()) is None
    assert find_first_divisible_by_2_and_3({7, 14, 21}) is None
    assert find_first_divisible_by_2_and_3({9, 15, 21, 27}) is None


# 798. Тесты для функции `find_common_in_lists`:
def test_find_common_in_lists():
    assert find_common_in_lists([1, 2, 3], [3, 4, 5]) == 3
    assert find_common_in_lists([6, 7, 8], [9, 10, 11]) is None
    assert find_common_in_lists([12, 13, 14], [14, 15, 16]) == 14
    assert find_common_in_lists([17, 18, 19], [20, 21, 22]) is None
    assert find_common_in_lists([23, 24, 25], [25, 26, 27]) == 25
    assert find_common_in_lists([], [28, 29, 30]) is None


# 799. Тесты для функции `find_smallest_even_greater_than`:
def test_find_smallest_even_greater_than():
    assert find_smallest_even_greater_than([2, 4, 6, 8], 5) == 6
    assert find_smallest_even_greater_than([10, 12, 14], 15) is None
    assert find_smallest_even_greater_than([16, 18, 20], 17) == 18
    assert find_smallest_even_greater_than([], 3) is None
    assert find_smallest_even_greater_than([22, 24, 26], 21) == 22
    assert find_smallest_even_greater_than([28, 30, 32], 29) == 30


# 800. Тесты для функции `find_element_greater_than_in_set`:
def test_find_element_greater_than_in_set():
    assert find_element_greater_than_in_set({1, 2, 3, 4}, 3) == 4
    assert find_element_greater_than_in_set({5, 6, 7, 8}, 10) is None
    assert find_element_greater_than_in_set({11, 12, 13, 14}, 12) == 13
    assert find_element_greater_than_in_set(set(), 0) is None
    assert find_element_greater_than_in_set({15, 16, 17, 18}, 16) == 17
    assert find_element_greater_than_in_set({19, 20, 21, 22}, 18) == 19
