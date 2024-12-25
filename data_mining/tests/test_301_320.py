import pytest
from functions.file_301_320 import *


# 301. Тесты для функции `find_divisible_by_2_and_3`
def test_find_divisible_by_2_and_3():
    assert find_divisible_by_2_and_3([6, 12, 18]) == [6, 12, 18]
    assert find_divisible_by_2_and_3([7, 14, 21]) == None
    assert find_divisible_by_2_and_3([2, 4, 8]) == None
    assert find_divisible_by_2_and_3([3, 9, 15]) == None
    assert find_divisible_by_2_and_3([6]) == [6]
    assert find_divisible_by_2_and_3([1, 2, 3]) == None
    assert find_divisible_by_2_and_3([]) == None


# 302. Тесты для функции `find_powers_of_numbers`
def test_find_powers_of_numbers():
    assert find_powers_of_numbers([2, 3], 2) == [4, 9]
    assert find_powers_of_numbers([1, 2, 3], 3) == [1, 8, 27]
    assert find_powers_of_numbers([], 2) == None
    assert find_powers_of_numbers([0], 5) == [0]
    assert find_powers_of_numbers([2], 0) == [1]
    assert find_powers_of_numbers([-2, -3], 2) == [4, 9]
    assert find_powers_of_numbers([2], 1) == [2]


# 303. Тесты для функции `find_difference_between_two_lists`
def test_find_difference_between_two_lists():
    assert find_difference_between_two_lists([1, 3, 5], [1, 2, 3]) == [0, 1, 2]
    assert find_difference_between_two_lists([4, 6], [2, 3]) == [2, 3]
    assert find_difference_between_two_lists([], []) == None
    assert find_difference_between_two_lists([1], [0]) == [1]
    assert find_difference_between_two_lists([0], [1]) == [1]
    assert find_difference_between_two_lists([1], [-1]) == [2]
    assert find_difference_between_two_lists([2, 3, 4], [5, 3, 1]) == [3, 0, 3]


# 304. Тесты для функции `find_keys_in_both_dicts`
def test_find_keys_in_both_dicts():
    assert find_keys_in_both_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) == ["b"]
    assert find_keys_in_both_dicts({"a": 1, "b": 2}, {"d": 3, "e": 4}) == None
    assert find_keys_in_both_dicts({"a": 1}, {"a": 4}) == ["a"]
    assert find_keys_in_both_dicts({}, {"a": 4}) == None
    assert find_keys_in_both_dicts({"a": 1, "b": 2}, {}) == None
    assert find_keys_in_both_dicts({}, {}) == None
    assert find_keys_in_both_dicts({"a": 1, "b": 2, "c": 3}, {"c": 4, "d": 5, "a": 0}) == ["a", "c"]


# 305. Тесты для функции `find_product_of_elements_from_two_lists`
def test_find_product_of_elements_from_two_lists():
    assert find_product_of_elements_from_two_lists([1, 2], [3, 4]) == [3, 8]
    assert find_product_of_elements_from_two_lists([5, 6], [0, 7]) == [0, 42]
    assert find_product_of_elements_from_two_lists([1], [1]) == [1]
    assert find_product_of_elements_from_two_lists([0], [2]) == [0]
    assert find_product_of_elements_from_two_lists([2], [0]) == [0]
    assert find_product_of_elements_from_two_lists([], []) == None
    assert find_product_of_elements_from_two_lists([2, 3], [4, 1]) == [8, 3]


# 306. Тесты для функции `find_keys_in_dict_not_in_list`
def test_find_keys_in_dict_not_in_list():
    assert find_keys_in_dict_not_in_list({"a": 1, "b": 2}, ["a"]) == ["b"]
    assert find_keys_in_dict_not_in_list({"a": 1, "b": 2}, ["a", "b"]) == None
    assert find_keys_in_dict_not_in_list({}, ["a"]) == None
    assert find_keys_in_dict_not_in_list({"a": 1}, []) == ["a"]
    assert find_keys_in_dict_not_in_list({"a": 1, "b": 2}, []) == ["a", "b"]
    assert find_keys_in_dict_not_in_list({"a": 1, "b": 2}, ["c"]) == ["a", "b"]
    assert find_keys_in_dict_not_in_list({"a": 1}, ["a", "b"]) == None


# 307. Тесты для функции `find_powers_of_numbers_in_list`
def test_find_powers_of_numbers_in_list():
    assert find_powers_of_numbers_in_list([2, 3], 2) == [4, 9]
    assert find_powers_of_numbers_in_list([1, 2, 3], 3) == [1, 8, 27]
    assert find_powers_of_numbers_in_list([], 2) == None
    assert find_powers_of_numbers_in_list([0], 5) == [0]
    assert find_powers_of_numbers_in_list([2], 0) == [1]
    assert find_powers_of_numbers_in_list([-2, -3], 2) == [4, 9]
    assert find_powers_of_numbers_in_list([2], 1) == [2]


# 308. Тесты для функции `find_elements_in_both_sets`
def test_find_elements_in_both_sets():
    assert find_elements_in_both_sets({1, 2, 3}, {2, 3, 4}) == [2, 3]
    assert find_elements_in_both_sets({1, 2, 3}, {4, 5, 6}) == None
    assert find_elements_in_both_sets(set(), {1, 2, 3}) == None
    assert find_elements_in_both_sets({1}, {1}) == [1]
    assert find_elements_in_both_sets({1, 2, 3}, {1}) == [1]
    assert find_elements_in_both_sets(set(), set()) == None
    assert find_elements_in_both_sets({0, 1, 2}, {2, 0, 3}) == [0, 2]


# 309. Тесты для функции `find_diff_between_lists`
def test_find_diff_between_lists():
    assert find_diff_between_lists([1, 2, 3], [4, 5, 6]) == [3, 3, 3]
    assert find_diff_between_lists([7, 8, 9], [1, 2, 3]) == [6, 6, 6]
    assert find_diff_between_lists([0], [0]) == [0]
    assert find_diff_between_lists([], []) == None
    assert find_diff_between_lists([1], [0]) == [1]
    assert find_diff_between_lists([0], [1]) == [1]
    assert find_diff_between_lists([2, 3, 4], [5, 3, 1]) == [3, 0, 3]


# 310. Тесты для функции `find_sum_of_two_lists_2`
def test_find_sum_of_two_lists_2():
    assert find_sum_of_two_lists_2([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert find_sum_of_two_lists_2([7, 8, 9], [1, 2, 3]) == [8, 10, 12]
    assert find_sum_of_two_lists_2([0], [0]) == [0]
    assert find_sum_of_two_lists_2([], []) == None
    assert find_sum_of_two_lists_2([1], [0]) == [1]
    assert find_sum_of_two_lists_2([0], [1]) == [1]
    assert find_sum_of_two_lists_2([2, 3, 4], [5, 3, 1]) == [7, 6, 5]


# 311. Тесты для функции `find_in_tuple_not_in_list`
def test_find_in_tuple_not_in_list():
    assert find_in_tuple_not_in_list((1, 2, 3), [2, 3, 4]) == [1]
    assert find_in_tuple_not_in_list((5, 6), [6, 7]) == [5]
    assert find_in_tuple_not_in_list((), [1, 2]) == None
    assert find_in_tuple_not_in_list((1,), [1]) == None
    assert find_in_tuple_not_in_list((1,), []) == [1]
    assert find_in_tuple_not_in_list((1, 2, 3), (2, 4)) == [1, 3]
    assert find_in_tuple_not_in_list((1, 2), (1, 2, 3)) == None


# 312. Тесты для функции `find_divisible_by_10_not_20`
def test_find_divisible_by_10_not_20():
    assert find_divisible_by_10_not_20([10, 20, 30, 40]) == [10, 30]
    assert find_divisible_by_10_not_20([5, 10, 15, 25]) == [10]
    assert find_divisible_by_10_not_20([1, 2, 3, 4]) == None
    assert find_divisible_by_10_not_20([20, 40, 60]) == None
    assert find_divisible_by_10_not_20([10, 50, 70]) == [10, 50, 70]
    assert find_divisible_by_10_not_20([]) == None
    assert find_divisible_by_10_not_20([30, 50, 90]) == [30, 50, 90]


# 313. Тесты для функции `find_sum_from_two_lists`
def test_find_sum_from_two_lists():
    assert find_sum_from_two_lists([1, 2], [3, 4]) == [4, 6]
    assert find_sum_from_two_lists([5, 6], [1, 2]) == [6, 8]
    assert find_sum_from_two_lists([], []) == None
    assert find_sum_from_two_lists([1], [1]) == [2]
    assert find_sum_from_two_lists([0], [0]) == [0]
    assert find_sum_from_two_lists([2, 3], [4, 5]) == [6, 8]
    assert find_sum_from_two_lists([5, 5], [5, 5]) == [10, 10]


# 314. Тесты для функции `find_common_elements_in_sets`
def test_find_common_elements_in_sets():
    assert find_common_elements_in_sets({1, 2, 3}, {3, 4, 5}) == [3]
    assert find_common_elements_in_sets({6, 7}, {7, 8}) == [7]
    assert find_common_elements_in_sets(set(), {1, 2}) == None
    assert find_common_elements_in_sets({1}, {1}) == [1]
    assert find_common_elements_in_sets({1, 2, 3}, {4, 5, 6}) == None
    assert find_common_elements_in_sets(set(), set()) == None
    assert find_common_elements_in_sets({0, 1, 2}, {2, 3, 0}) == [0, 2]


# 315. Тесты для функции `find_product_in_list`
def test_find_product_in_list():
    assert find_product_in_list([1, 2, 3]) == [2, 3, 6]
    assert find_product_in_list([4, 5]) == [20]
    assert find_product_in_list([]) == None
    assert find_product_in_list([0, 1]) == [0]
    assert find_product_in_list([1]) == None
    assert find_product_in_list([1, 2]) == [2]
    assert find_product_in_list([2, 3, 4]) == [6, 8, 12]


# 316. Тесты для функции `find_in_list_not_in_dict`
def test_find_in_list_not_in_dict():
    assert find_in_list_not_in_dict([1, 2, 3], {3: "a", 4: "b"}) == [1, 2]
    assert find_in_list_not_in_dict([5, 6], {5: "x", 7: "y"}) == [6]
    assert find_in_list_not_in_dict([], {1: "a"}) == None
    assert find_in_list_not_in_dict([1], {1: "a"}) == None
    assert find_in_list_not_in_dict([1], {}) == [1]
    assert find_in_list_not_in_dict([1, 2, 3], {}) == [1, 2, 3]
    assert find_in_list_not_in_dict([1, 2], {3: "b", 4: "c"}) == [1, 2]


# 317. Тесты для функции `merge_dicts_2`
def test_merge_dicts_2():
    assert merge_dicts_2({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}
    assert merge_dicts_2({}, {"c": 3}) == {"c": 3}
    assert merge_dicts_2({"d": 4}, {}) == {"d": 4}
    assert merge_dicts_2({}, {}) == None
    assert merge_dicts_2({"a": 1}, {"a": 2}) == {"a": 2}
    assert merge_dicts_2({"a": 1, "b": 2}, {"c": 3}) == {"a": 1, "b": 2, "c": 3}
    assert merge_dicts_2({"x": 0}, {"y": -1}) == {"x": 0, "y": -1}


# 318. Тесты для функции `find_in_one_set_not_other`
def test_find_in_one_set_not_other():
    assert find_in_one_set_not_other({1, 2}, {2, 3}) == [1, 3]
    assert find_in_one_set_not_other({5, 6}, {6, 7}) == [5, 7]
    assert find_in_one_set_not_other(set(), {1, 2}) == [1, 2]
    assert find_in_one_set_not_other({1}, {1}) == None
    assert find_in_one_set_not_other({1}, set()) == [1]
    assert find_in_one_set_not_other(set(), set()) == None
    assert find_in_one_set_not_other({1, 2, 3}, {4, 5, 6}) == [1, 2, 3, 4, 5, 6]


# 319. Тесты для функции `find_division_from_two_lists`
def test_find_division_from_two_lists():
    assert find_division_from_two_lists([1, 2], [1, 2]) == [1, 1]
    assert find_division_from_two_lists([4, 6], [2, 3]) == [2, 2]
    assert find_division_from_two_lists([], []) == None
    assert find_division_from_two_lists([1], [1]) == [1]
    assert find_division_from_two_lists([5], [0]) == None
    assert find_division_from_two_lists([1, 2], [0, 1]) == [2]
    assert find_division_from_two_lists([0, 1], [1, 2]) == [0, 0.5]


# 320. Тесты для функции `find_common_less_in_one_list`
def test_find_common_less_in_one_list():
    assert find_common_less_in_one_list([1, 2, 3], [2, 3, 3]) == [3]
    assert find_common_less_in_one_list([4, 5, 6], [5, 6, 7]) == None
    assert find_common_less_in_one_list([], []) == None
    assert find_common_less_in_one_list([1], [1]) == None
    assert find_common_less_in_one_list([1, 2, 3], [1, 2, 2, 3]) == [2]

