import pytest
from functions.file_141_160 import *


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
