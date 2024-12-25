import pytest
from functions.file_481_500 import *


# 481. Тесты для функции `find_greater_than_x_divisible_by_3`:
def test_find_greater_than_x_divisible_by_3():
    assert find_greater_than_x_divisible_by_3((1, 2, 3, 6, 9, 12), 5) == (6, 9, 12)
    assert find_greater_than_x_divisible_by_3((1, 2, 3, 4, 5), 2) == (3,)
    assert find_greater_than_x_divisible_by_3((10, 11, 15, 18), 16) == (18,)
    assert find_greater_than_x_divisible_by_3((1, 2, 3, 6, 9, 12), 12) == None
    assert find_greater_than_x_divisible_by_3((1, 2, 3, 4, 5), 5) == None
    assert find_greater_than_x_divisible_by_3((0, 3, 6, 9, 12), 10) == (12,)
    assert find_greater_than_x_divisible_by_3((3,), 0) == (3,)
    assert find_greater_than_x_divisible_by_3((), 0) == None
    assert find_greater_than_x_divisible_by_3((3, 5, 7, 9), 8) == (9,)


# 482. Тесты для функции `find_not_divisible_by_4_and_5`:
def test_find_not_divisible_by_4_and_5():
    assert find_not_divisible_by_4_and_5((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) == (1, 2, 3, 6, 7, 9)
    assert find_not_divisible_by_4_and_5((4, 5, 8, 10, 12, 15, 16, 20)) == None
    assert find_not_divisible_by_4_and_5((4, 8, 12, 16, 20)) == None
    assert find_not_divisible_by_4_and_5((5, 10, 15, 25)) == None
    assert find_not_divisible_by_4_and_5((2, 3, 6, 7, 9)) == (2, 3, 6, 7, 9)
    assert find_not_divisible_by_4_and_5((1, 4, 5, 8, 10)) == (1,)
    assert find_not_divisible_by_4_and_5((),) == None
    assert find_not_divisible_by_4_and_5((20, 25, 30, 35, 40)) == None
    assert find_not_divisible_by_4_and_5((9, 14, 21, 33)) == (9, 14, 21, 33)


# 483. Тесты для функции `find_less_than_x_divisible_by_3`:
def test_find_less_than_x_divisible_by_3():
    assert find_less_than_x_divisible_by_3((1, 2, 3, 6, 9, 12), 10) == (3, 6, 9)
    assert find_less_than_x_divisible_by_3((1, 2, 3, 4, 5), 6) == (3,)
    assert find_less_than_x_divisible_by_3((10, 11, 15, 18), 20) == (15, 18)
    assert find_less_than_x_divisible_by_3((1, 2, 3, 6, 9, 12), 2) == None
    assert find_less_than_x_divisible_by_3((1, 2, 3, 4, 5), 1) == None
    assert find_less_than_x_divisible_by_3((0, 3, 6, 9, 12), 9) == (0, 3, 6)
    assert find_less_than_x_divisible_by_3((3,), 4) == (3,)
    assert find_less_than_x_divisible_by_3((), 3) == None
    assert find_less_than_x_divisible_by_3((3, 5, 7, 9), 10) == (3, 9)


# 484. Тесты для функции `find_divisible_by_2_and_5`:
def test_find_divisible_by_2_and_5():
    assert find_divisible_by_2_and_5((1, 2, 5, 10, 12, 15, 20)) == (10, 20)
    assert find_divisible_by_2_and_5((10, 20, 30, 40, 50)) == (10, 20, 30, 40, 50)
    assert find_divisible_by_2_and_5((5, 15, 25, 35)) == None
    assert find_divisible_by_2_and_5((2, 4, 6, 8)) == None
    assert find_divisible_by_2_and_5((0, 10, 20, 25)) == (0, 10, 20)
    assert find_divisible_by_2_and_5((5, 10, 15)) == (10,)
    assert find_divisible_by_2_and_5((),) == None
    assert find_divisible_by_2_and_5((30, 35, 40, 50)) == (30, 40, 50)
    assert find_divisible_by_2_and_5((25, 50, 75, 100)) == (50, 100)


# 485. Тесты для функции `find_not_square_numbers_in_tuple`:
def test_find_not_square_numbers_in_tuple():
    assert find_not_square_numbers_in_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) == (2, 3, 5, 6, 7, 8, 10)
    assert find_not_square_numbers_in_tuple((4, 9, 16, 25, 36)) == None
    assert find_not_square_numbers_in_tuple((2, 3, 5, 6, 7, 8, 10)) == (2, 3, 5, 6, 7, 8, 10)
    assert find_not_square_numbers_in_tuple((4, 8, 12, 16, 20)) == (8, 12, 20)
    assert find_not_square_numbers_in_tuple((4, 5, 6, 7, 9)) == (5, 6, 7)
    assert find_not_square_numbers_in_tuple((),) == None
    assert find_not_square_numbers_in_tuple((1, 3, 7, 11, 12)) == (3, 7, 11, 12)
    assert find_not_square_numbers_in_tuple((4, 16, 25, 36)) == None
    assert find_not_square_numbers_in_tuple((5, 10, 15, 20)) == (5, 10, 15, 20)


# 486. Тесты для функции `find_divisible_by_2_and_7`:
def test_find_divisible_by_2_and_7():
    assert find_divisible_by_2_and_7((1, 2, 7, 14, 21, 28, 35, 42)) == (14, 28, 42)
    assert find_divisible_by_2_and_7((14, 28, 42, 56, 70, 84)) == (14, 28, 42, 56, 70, 84)
    assert find_divisible_by_2_and_7((1, 3, 5, 7, 9, 11)) == None
    assert find_divisible_by_2_and_7((2, 4, 8, 16)) == None
    assert find_divisible_by_2_and_7((0, 7, 14, 28)) == (0, 14, 28)
    assert find_divisible_by_2_and_7((7, 14, 21)) == (14,)
    assert find_divisible_by_2_and_7((),) == None
    assert find_divisible_by_2_and_7((7, 14, 35, 42)) == (14, 42)
    assert find_divisible_by_2_and_7((28, 56, 84, 112)) == (28, 56, 84, 112)


# 487. Тесты для функции `find_less_than_x_odd`:
def test_find_less_than_x_odd():
    assert find_less_than_x_odd((1, 2, 3, 6, 9, 12), 10) == (1, 3, 9)
    assert find_less_than_x_odd((1, 2, 3, 4, 5), 6) == (1, 3, 5)
    assert find_less_than_x_odd((10, 11, 15, 18), 16) == (11, 15)
    assert find_less_than_x_odd((1, 2, 3, 6, 9, 12), 2) == (1,)
    assert find_less_than_x_odd((1, 2, 3, 4, 5), 1) == None
    assert find_less_than_x_odd((0, 3, 6, 9, 12), 9) == (3,)
    assert find_less_than_x_odd((3,), 4) == (3,)
    assert find_less_than_x_odd((), 3) == None
    assert find_less_than_x_odd((3, 5, 7, 9), 8) == (3, 5, 7)


# 488. Тесты для функции `find_greater_than_x_even`:
def test_find_greater_than_x_even():
    assert find_greater_than_x_even((1, 2, 3, 6, 9, 12), 5) == (6, 12)
    assert find_greater_than_x_even((1, 2, 3, 4, 5), 2) == (4,)
    assert find_greater_than_x_even((10, 11, 14, 18), 13) == (14, 18)
    assert find_greater_than_x_even((1, 2, 3, 6, 9, 12), 12) == None
    assert find_greater_than_x_even((1, 2, 3, 4, 5), 5) == None
    assert find_greater_than_x_even((0, 3, 6, 8, 12), 7) == (8, 12)
    assert find_greater_than_x_even((4,), 3) == (4,)
    assert find_greater_than_x_even((), 3) == None
    assert find_greater_than_x_even((3, 5, 7, 9), 8) == None


# 489. Тесты для функции `unique_elements_from_list`:
def test_unique_elements_from_list():
    assert unique_elements_from_list([1, 2, 2, 3, 4, 4, 5]) == (1, 2, 3, 4, 5)
    assert unique_elements_from_list([1, 1, 1, 1, 1]) == (1,)
    assert unique_elements_from_list([1, 2, 3, 4, 5]) == (1, 2, 3, 4, 5)
    assert unique_elements_from_list([]) == None
    assert unique_elements_from_list([1, 2, 3, 4, 4, 5, 5]) == (1, 2, 3, 4, 5)
    assert unique_elements_from_list([3, 3, 3, 2, 1, 1]) == (1, 2, 3)
    assert unique_elements_from_list([10, 9, 9, 10]) == (9, 10)
    assert unique_elements_from_list([5]) == (5,)
    assert unique_elements_from_list([4, 5, 6, 6, 7]) == (4, 5, 6, 7)


# 490. Тесты для функции `intersection_of_lists_2`:
def test_intersection_of_lists_2():
    assert intersection_of_lists_2([1, 2, 3], [3, 4, 5]) == [3]
    assert intersection_of_lists_2([1, 2, 2, 3], [3, 3, 4]) == [3]
    assert intersection_of_lists_2([1, 2, 3], [4, 5, 6]) == None
    assert intersection_of_lists_2([], [1, 2, 3]) == None
    assert intersection_of_lists_2([1, 2, 3], []) == None
    assert intersection_of_lists_2([1, 2, 3, 4], [2, 3, 4, 5]) == [2, 3, 4]
    assert intersection_of_lists_2([5, 6, 7], [7, 8, 9]) == [7]
    assert intersection_of_lists_2([1, 1, 2, 2], [2, 2, 3, 3]) == [2]
    assert intersection_of_lists_2([9, 8, 7], [7, 6, 5]) == [7]


# 491. Тесты для функции `merge_dicts_no_common_keys`:
def test_merge_dicts_no_common_keys():
    assert merge_dicts_no_common_keys({"a": 1, "b": 2}, {"c": 3, "d": 4}) == {"a": 1, "b": 2, "c": 3, "d": 4}
    assert merge_dicts_no_common_keys({"a": 1}, {"b": 2, "c": 3}) == {"a": 1, "b": 2, "c": 3}
    assert merge_dicts_no_common_keys({"a": 1, "b": 2}, {"b": 3, "d": 4}) == None
    assert merge_dicts_no_common_keys({}, {"a": 1, "b": 2}) == {"a": 1, "b": 2}
    assert merge_dicts_no_common_keys({"a": 1, "b": 2}, {}) == {"a": 1, "b": 2}
    assert merge_dicts_no_common_keys({}, {}) == {}
    assert merge_dicts_no_common_keys({"a": 1, "b": 2}, {"c": 2, "d": 3}) == {"a": 1, "b": 2, "c": 2, "d": 3}
    assert merge_dicts_no_common_keys({"a": 1}, {"a": 2}) == None
    assert merge_dicts_no_common_keys({"a": 1, "b": 2}, {"a": 2, "c": 3}) == None


# 492. Тесты для функции `reverse_string_3`:
def test_reverse_string_3():
    assert reverse_string_3("hello") == "olleh"
    assert reverse_string_3("world") == "dlrow"
    assert reverse_string_3("") == None
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
    assert divisors_of_x(1) == None
    assert divisors_of_x(0) == None
    assert divisors_of_x(-5) == None
    assert divisors_of_x(17) == None
    assert divisors_of_x(100) == [2, 4, 5, 10, 20, 25, 50]
    assert divisors_of_x(25) == [5]
    assert divisors_of_x(2) == None


# 494. Тесты для функции `count_elements_in_list`:
def test_count_elements_in_list():
    assert count_elements_in_list([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
    assert count_elements_in_list([1, 1, 1, 1, 1]) == {1: 5}
    assert count_elements_in_list([]) == None
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
    assert list_to_dict_2([]) == None
    assert list_to_dict_2(["a", 1, "b", 2, "c"]) == None
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
    assert count_even_and_odd([]) == None
    assert count_even_and_odd([1, 1, 1, 1]) == {"even": 0, "odd": 4}
    assert count_even_and_odd([2, 2, 2, 2]) == {"even": 4, "odd": 0}
    assert count_even_and_odd([1]) == {"even": 0, "odd": 1}
    assert count_even_and_odd([2]) == {"even": 1, "odd": 0}
    assert count_even_and_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == {"even": 5, "odd": 5}


# 497. Тесты для функции `extract_vowels_from_string`:
def test_extract_vowels_from_string():
    assert extract_vowels_from_string("hello") == "eo"
    assert extract_vowels_from_string("world") == "o"
    assert extract_vowels_from_string("") == None
    assert extract_vowels_from_string("a") == "a"
    assert extract_vowels_from_string("bcdfg") == None
    assert extract_vowels_from_string("AEIOU") == "AEIOU"
    assert extract_vowels_from_string("Python Programming") == 'ooai'
    assert extract_vowels_from_string("abcdefghijklmnopqrstuvwxyz") == "aeiou"
    assert extract_vowels_from_string("HELLO WORLD") == "EOO"


# 498. Тесты для функции `merge_sorted_lists`
def test_merge_sorted_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_lists([], []) == None
    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]
    assert merge_sorted_lists([], [4, 5, 6]) == [4, 5, 6]
    assert merge_sorted_lists([0], [0]) == [0, 0]
    assert merge_sorted_lists([10, 20], [5, 15, 25]) == [5, 10, 15, 20, 25]
    assert merge_sorted_lists([-1, -2], [-3, -4]) == [-4, -3, -2, -1]


# 499. Тесты для функции `is_palindrome_2`
def test_is_palindrome_2():
    assert is_palindrome_2('racecar') == True
    assert is_palindrome_2('') == None
    assert is_palindrome_2('madam') == True
    assert is_palindrome_2('python') == False
    assert is_palindrome_2('Aibohphobia') == False
    assert is_palindrome_2('step on no pets') == True
    assert is_palindrome_2('Was it a car or a cat I saw') == False
    assert is_palindrome_2('civic') == True


# 500. Тесты для функции `gcd_of_two_numbers`
def test_gcd_of_two_numbers():
    assert gcd_of_two_numbers(48, 18) == 6
    assert gcd_of_two_numbers(0, 10) == None
    assert gcd_of_two_numbers(15, 0) == None
    assert gcd_of_two_numbers(-5, 10) == None
    assert gcd_of_two_numbers(5, -10) == None
    assert gcd_of_two_numbers(36, 6) == 6
    assert gcd_of_two_numbers(101, 103) == 1
    assert gcd_of_two_numbers(56, 98) == 14
    assert gcd_of_two_numbers(14, 28) == 14


