from functions.file_661_680 import *
import pytest


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
