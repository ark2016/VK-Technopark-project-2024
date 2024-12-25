import pytest
from functions.file_61_80 import *


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
