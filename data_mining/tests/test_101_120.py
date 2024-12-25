import pytest
from functions.file_101_120 import *


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
