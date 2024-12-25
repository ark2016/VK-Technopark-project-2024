import pytest
from functions.file_501_520 import *


# 501. Тесты для функции `prime_numbers_up_to_x`
def test_prime_numbers_up_to_x():
    assert prime_numbers_up_to_x(10) == [2, 3, 5, 7]
    assert prime_numbers_up_to_x(2) == [2]
    assert prime_numbers_up_to_x(1) == None
    assert prime_numbers_up_to_x(0) == None
    assert prime_numbers_up_to_x(-5) == None
    assert prime_numbers_up_to_x(11) == [2, 3, 5, 7, 11]


# 502. Тесты для функции `factorial_of_number`
def test_factorial_of_number():
    assert factorial_of_number(5) == 120
    assert factorial_of_number(0) == 1
    assert factorial_of_number(-1) == None
    assert factorial_of_number(3) == 6
    assert factorial_of_number(1) == 1
    assert factorial_of_number(4) == 24


# 503. Тесты для функции `count_words_in_string`
def test_count_words_in_string():
    assert count_words_in_string("Hello world") == 2
    assert count_words_in_string("") == None
    assert count_words_in_string("A quick brown fox jumps over the lazy dog") == 9
    assert count_words_in_string(" ") == 0
    assert count_words_in_string("Testing, one, two, three.") == 4


# 504. Тесты для функции `find_all_indices_of_element`
def test_find_all_indices_of_element():
    assert find_all_indices_of_element([1, 2, 3, 2, 1], 2) == [1, 3]
    assert find_all_indices_of_element([1, 2, 3, 4, 5], 6) == None
    assert find_all_indices_of_element([], 1) == None
    assert find_all_indices_of_element([1, 1, 1, 1], 1) == [0, 1, 2, 3]
    assert find_all_indices_of_element(["a", "b", "a"], "a") == [0, 2]


# 505. Тесты для функции `square_numbers_from_list`
def test_square_numbers_from_list():
    assert square_numbers_from_list([1, 2, 3, 4, 5, 9]) == [1, 4, 9]
    assert square_numbers_from_list([]) == None
    assert square_numbers_from_list([10, 15, 20]) == None
    assert square_numbers_from_list([0, 1, 16, 25]) == [0, 1, 16, 25]
    assert square_numbers_from_list([1, 4, 9]) == [1, 4, 9]


# 506. Тесты для функции `greater_than_average`
def test_greater_than_average():
    assert greater_than_average([1, 2, 3, 4, 5]) == [4, 5]
    assert greater_than_average([10, 20, 30, 40, 50]) == [40, 50]
    assert greater_than_average([]) == None
    assert greater_than_average([5, 5, 5, 5]) == None
    assert greater_than_average([1, 2, 3, 3, 4]) == [3, 3, 4]


# 507. Тесты для функции `sort_strings_by_length`
def test_sort_strings_by_length():
    assert sort_strings_by_length(["a", "aaa", "aa"]) == ["a", "aa", "aaa"]
    assert sort_strings_by_length(["short", "longer", "longest"]) == ["short", "longer", "longest"]
    assert sort_strings_by_length([]) == None
    assert sort_strings_by_length(["same", "size"]) == ["same", "size"]
    assert sort_strings_by_length(["one", "three", "four"]) == ["one", "four", "three"]


# 508. Тесты для функции `sum_of_elements`
def test_sum_of_elements():
    assert sum_of_elements([1, 2, 3, 4, 5]) == 15
    assert sum_of_elements([]) == None
    assert sum_of_elements([10, 20, 30, 40]) == 100
    assert sum_of_elements([0, 0, 0, 0]) == 0
    assert sum_of_elements([-1, -2, -3, -4]) == -10


# 509. Тесты для функции `longest_string`
def test_longest_string():
    assert longest_string(["a", "aa", "aaa"]) == "aaa"
    assert longest_string(["short", "longer", "longest"]) == "longest"
    assert longest_string([]) == None
    assert longest_string(["same", "size"]) == "same"
    assert longest_string(["one", "three", "four"]) == "three"


# 510. Тесты для функции `difference_between_sets`
def test_difference_between_sets():
    assert difference_between_sets({1, 2, 3}, {2, 3, 4}) == {1}
    assert difference_between_sets(set(), {1, 2, 3}) == None
    assert difference_between_sets({1, 2, 3}, set()) == None
    assert difference_between_sets({1, 2, 3}, {1, 2, 3}) == set()
    assert difference_between_sets({1, 2}, {3, 4}) == {1, 2}


# 511. Тесты для функции `union_of_lists`
def test_union_of_lists():
    assert union_of_lists([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 4, 5]
    assert union_of_lists([], [1, 2, 3]) == [1, 2, 3]
    assert union_of_lists([1, 2, 3], []) == [1, 2, 3]
    assert union_of_lists([], []) == None
    assert union_of_lists([1, 1, 1], [2, 2, 2]) == [1, 2]


# 512. Тесты для функции `intersection_of_lists_3`
def test_intersection_of_lists_3():
    assert intersection_of_lists_3([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert intersection_of_lists_3([], [1, 2, 3]) == []
    assert intersection_of_lists_3([1, 2, 3], []) == []
    assert intersection_of_lists_3([], []) == None
    assert intersection_of_lists_3([1, 2, 2], [2, 2, 3]) == [2]


# 513. Тесты для функции `is_digit`
def test_is_digit():
    assert is_digit("123") == True
    assert is_digit("abc") == False
    assert is_digit("") == None
    assert is_digit("123abc") == False
    assert is_digit("0") == True


# 514. Тесты для функции `extract_letters_from_string`
def test_extract_letters_from_string():
    assert extract_letters_from_string("abc123") == "abc"
    assert extract_letters_from_string("") == None
    assert extract_letters_from_string("123") == ""
    assert extract_letters_from_string("a1b2c3") == "abc"
    assert extract_letters_from_string("!@#") == ""


# 515. Тесты для функции `find_all_strings_in_list`
def test_find_all_strings_in_list():
    assert find_all_strings_in_list([1, "a", 2, "b"]) == ["a", "b"]
    assert find_all_strings_in_list([]) == None
    assert find_all_strings_in_list([1, 2, 3]) == []
    assert find_all_strings_in_list(["a", "b", "c"]) == ["a", "b", "c"]
    assert find_all_strings_in_list([1, "one", 2, "two"]) == ["one", "two"]


# 516. Тесты для функции `all_unique`
def test_all_unique():
    assert all_unique([1, 2, 3]) == True
    assert all_unique([1, 1, 1]) == False
    assert all_unique([]) == None
    assert all_unique(["a", "b", "c"]) == True
    assert all_unique(["a", "b", "a"]) == False


# 517. Тесты для функции `join_elements_with_separator`
def test_join_elements_with_separator():
    assert join_elements_with_separator(["a", "b", "c"], "-") == "a-b-c"
    assert join_elements_with_separator([], "-") == None
    assert join_elements_with_separator(["one"], "-") == "one"
    assert join_elements_with_separator(["a", "b", "c"], "") == "abc"
    assert join_elements_with_separator(["1", "2", "3"], ", ") == "1, 2, 3"


# 518. Тесты для функции `difference_between_lists`
def test_difference_between_lists():
    assert difference_between_lists([1, 2, 3], [2, 3, 4]) == [1]
    assert difference_between_lists([], [1, 2, 3]) == []
    assert difference_between_lists([1, 2, 3], []) == [1, 2, 3]
    assert difference_between_lists([], []) == None
    assert difference_between_lists([1, 2, 3, 4], [3, 4]) == [1, 2]


# 519. Тесты для функции `count_non_overlapping_substring`
def test_count_non_overlapping_substring():
    assert count_non_overlapping_substring("ababab", "ab") == 3
    assert count_non_overlapping_substring("", "a") == None
    assert count_non_overlapping_substring("aaaa", "aa") == 2
    assert count_non_overlapping_substring("abc", "d") == 0
    assert count_non_overlapping_substring("abcdef", "abc") == 1


# 520. Тесты для функции `find_words_starting_with`
def test_find_words_starting_with():
    assert find_words_starting_with("apple banana apricot berry", "a") == ["apple", "apricot"]
    assert find_words_starting_with("", "a") == None
    assert find_words_starting_with("apple banana apricot berry", "b") == ["banana", "berry"]
    assert find_words_starting_with("apple banana apricot berry", "c") == None
    assert find_words_starting_with("cat cow car", "c") == ["cat", "cow", "car"]
