import pytest
from functions.file_41_60 import *


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
