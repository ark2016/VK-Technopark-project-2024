import pytest
from functions.file_641_660 import *


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
