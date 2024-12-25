import pytest
from functions.file_621_640 import *


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
