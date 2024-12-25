from functions.file_321_340 import *
import pytest


# 321. Тесты для функции `find_in_first_not_in_second`
def test_find_in_first_not_in_second():
    assert find_in_first_not_in_second([1, 2, 3], [2, 3, 4]) == [1]
    assert find_in_first_not_in_second([1, 2, 3], [1, 2, 3]) == None
    assert find_in_first_not_in_second([1, 2, 3, 4, 5], [4, 5]) == [1, 2, 3]
    assert find_in_first_not_in_second([], [1, 2, 3]) == None
    assert find_in_first_not_in_second([1, 2, 3], []) == [1, 2, 3]


# 322. Тесты для функции `find_common_elements_diff_index`
def test_find_common_elements_diff_index():
    assert find_common_elements_diff_index([1, 2, 3], [3, 2, 1]) == [1, 3]
    assert find_common_elements_diff_index([1, 2, 3], [1, 2, 3]) == None
    assert find_common_elements_diff_index([1, 2, 2, 3], [2, 3, 1, 2]) == [1, 2, 3]
    assert find_common_elements_diff_index([], [1, 2, 3]) == None
    assert find_common_elements_diff_index([1, 2, 3], []) == None


# 323. Тесты для функции `add_values_of_dicts`
def test_add_values_of_dicts():
    assert add_values_of_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == {'b': 5}
    assert add_values_of_dicts({'a': 1, 'b': 2}, {'c': 3, 'd': 4}) == None
    assert add_values_of_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 2, 'c': 3}) == {'b': 4, 'c': 6}
    assert add_values_of_dicts({}, {'a': 1, 'b': 2}) == None
    assert add_values_of_dicts({'a': 1, 'b': 2}, {}) == None


# 324. Тесты для функции `find_more_in_one_set`
def test_find_more_in_one_set():
    assert find_more_in_one_set({1, 2, 3}, {1, 2}) == None
    assert find_more_in_one_set({1, 2, 2, 3}, {1, 2}) == None
    assert find_more_in_one_set({1, 2, 2, 3, 3}, {2, 3}) == [3]
    assert find_more_in_one_set({1, 2}, {3, 1}) == None
    assert find_more_in_one_set({1, 21, 1, 2}, {21, 2}) == [21]


# 325. Тесты для функции `multiply_numbers_by_two`
def test_multiply_numbers_by_two():
    assert multiply_numbers_by_two([1, 2, 3]) == [2, 4, 6]
    assert multiply_numbers_by_two([0, -1, -2]) == [0, -2, -4]
    assert multiply_numbers_by_two([10, 100, 1000]) == [20, 200, 2000]
    assert multiply_numbers_by_two([]) == None
    assert multiply_numbers_by_two([1]) == [2]


# 326. Тесты для функции `sum_dict_values`
def test_sum_dict_values():
    assert sum_dict_values({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == {'b': 5}
    assert sum_dict_values({'a': 1, 'b': 2}, {'c': 3, 'd': 4}) == None
    assert sum_dict_values({'a': 1, 'b': 2, 'c': 3}, {'b': 2, 'c': 3}) == {'b': 4, 'c': 6}
    assert sum_dict_values({}, {'a': 1, 'b': 2}) == None
    assert sum_dict_values({'a': 1, 'b': 2}, {}) == None


# 327. Тесты для функции `find_squares_2`
def test_find_squares_2():
    assert find_squares_2([1, 2, 3]) == [1, 4, 9]
    assert find_squares_2([0, -1, -2]) == [0, 1, 4]
    assert find_squares_2([10, 100, 1000]) == [100, 10000, 1000000]
    assert find_squares_2([]) == None
    assert find_squares_2([1]) == [1]


# 328. Тесты для функции `find_difference_of_sets`
def test_find_difference_of_sets():
    assert find_difference_of_sets({1, 2, 3}, {2, 3, 4}) == [1]
    assert find_difference_of_sets({1, 2, 3}, {1, 2, 3}) == None
    assert find_difference_of_sets({1, 2, 3, 4}, {3, 4}) == [1, 2]
    assert find_difference_of_sets({1, 2}, {3, 4}) == [1, 2]
    assert find_difference_of_sets(set(), {1, 2, 3}) == None


# 329. Тесты для функции `find_sum_list_set`
def test_find_sum_list_set():
    assert find_sum_list_set([1, 2, 3], {2, 3, 4}) == [3, 4]
    assert find_sum_list_set([1, 2, 3], {1, 2, 3}) == [2, 3, 4]
    assert find_sum_list_set([1, 2, 3, 4], {4, 5}) == [5]
    assert find_sum_list_set([], {1, 2, 3}) == None
    assert find_sum_list_set([1, 2, 3], set()) == None


# 330. Тесты для функции `find_in_set_not_in_other_set`
def test_find_in_set_not_in_other_set():
    assert find_in_set_not_in_other_set({1, 2, 3}, {2, 3, 4}) == [1]
    assert find_in_set_not_in_other_set({1, 2, 3}, {1, 2, 3}) == None
    assert find_in_set_not_in_other_set({1, 2, 3, 4}, {3, 4}) == [1, 2]
    assert find_in_set_not_in_other_set({1, 2}, {3, 4}) == [1, 2]
    assert find_in_set_not_in_other_set(set(), {1, 2, 3}) == None


# 331. Тесты для функции `divide_elements_of_lists`
def test_divide_elements_of_lists():
    assert divide_elements_of_lists([4, 9, 16], [2, 3, 4]) == [2, 3, 4]
    assert divide_elements_of_lists([4, 9, 16], [2, 0, 4]) == [2, 4]
    assert divide_elements_of_lists([1, 2, 3], [0, 1, 1]) == [2, 3]
    assert divide_elements_of_lists([], [1, 2, 3]) == None
    assert divide_elements_of_lists([1, 2, 3], []) == None


# 332. Тесты для функции `find_in_both_sets_not_in_one`
def test_find_in_both_sets_not_in_one():
    assert find_in_both_sets_not_in_one({1, 2, 3}, {3, 4, 5}) == [1, 2, 4, 5]
    assert find_in_both_sets_not_in_one({1, 2}, {2, 3}) == [1, 3]
    assert find_in_both_sets_not_in_one({1, 2, 3}, {4, 5, 6}) == [1, 2, 3, 4, 5, 6]
    assert find_in_both_sets_not_in_one({1, 2, 3}, {1, 2, 3}) == None
    assert find_in_both_sets_not_in_one(set(), set()) == None


# 333. Тесты для функции `subtract_set_from_list`
def test_subtract_set_from_list():
    assert subtract_set_from_list([1, 2, 3], {2, 3, 4}) == [1]
    assert subtract_set_from_list([1, 2, 3], {1, 2, 3}) == None
    assert subtract_set_from_list([1, 2, 3, 4], {4, 5}) == [1, 2, 3]
    assert subtract_set_from_list([], {1, 2, 3}) == None
    assert subtract_set_from_list([1, 2, 3], set()) == [1, 2, 3]


# 334. Тесты для функции `find_sum_of_tuples`
def test_find_sum_of_tuples():
    assert find_sum_of_tuples((1, 2, 3), (4, 5, 6)) == [5, 7, 9]
    assert find_sum_of_tuples((1, 2), (1, 2, 3)) == [2, 4]
    assert find_sum_of_tuples((0, 0, 0), (0, 0, 0)) == [0, 0, 0]
    assert find_sum_of_tuples((), ()) == None
    assert find_sum_of_tuples((1, 2, 3), ()) == None


# 335. Тесты для функции `find_in_one_set_not_other_2`
def test_find_in_one_set_not_other_2():
    assert find_in_one_set_not_other_2({1, 2, 3}, {2, 3, 4}) == [1, 4]
    assert find_in_one_set_not_other_2({1, 2, 3}, {1, 2, 3}) == None
    assert find_in_one_set_not_other_2({1, 2, 3, 4}, {3, 4}) == [1, 2]
    assert find_in_one_set_not_other_2({1, 2}, {3, 4}) == [1, 2, 3, 4]
    assert find_in_one_set_not_other_2(set(), {1, 2, 3}) == [1, 2, 3]


# 336. Тесты для функции `find_divisible_by_4_not_8`
def test_find_divisible_by_4_not_8():
    assert find_divisible_by_4_not_8([4, 8, 16]) == [4]
    assert find_divisible_by_4_not_8([0, 8, 16]) == None
    assert find_divisible_by_4_not_8([4, 12, 20]) == [4, 12, 20]
    assert find_divisible_by_4_not_8([]) == None
    assert find_divisible_by_4_not_8([3, 5, 7]) == None


# 337. Тесты для функции `find_keys_in_dict1_not_in_dict2`
def test_find_keys_in_dict1_not_in_dict2():
    assert find_keys_in_dict1_not_in_dict2({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == ['a']
    assert find_keys_in_dict1_not_in_dict2({'a': 1, 'b': 2}, {'a': 1, 'b': 2}) == None
    assert find_keys_in_dict1_not_in_dict2({'a': 1, 'b': 2, 'c': 3}, {'b': 3}) == ['a', 'c']
    assert find_keys_in_dict1_not_in_dict2({}, {'a': 1}) == None
    assert find_keys_in_dict1_not_in_dict2({'a': 1}, {}) == ['a']


# 338. Тесты для функции `multiply_by_two`
def test_multiply_by_two():
    assert multiply_by_two([1, 2, 3]) == [2, 4, 6]
    assert multiply_by_two([0, -1, -2]) == [0, -2, -4]
    assert multiply_by_two([10, 100, 1000]) == [20, 200, 2000]
    assert multiply_by_two([]) == None
    assert multiply_by_two([1]) == [2]


# 339. Тесты для функции `subtract_lists`
def test_subtract_lists():
    assert subtract_lists([4, 9, 16], [2, 3, 4]) == [2, 6, 12]
    assert subtract_lists([4, 9, 16], [2, 0, 4]) == [2, 9, 12]
    assert subtract_lists([1, 2, 3], [0, 1, 1]) == [1, 1, 2]
    assert subtract_lists([], [1, 2, 3]) == None
    assert subtract_lists([1, 2, 3], []) == None


# 340. Тесты для функции `find_common_in_dicts`
def test_find_common_in_dicts():
    assert find_common_in_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == ['b']
    assert find_common_in_dicts({'a': 1, 'b': 2}, {'a': 1, 'b': 2}) == ['a', 'b']
    assert find_common_in_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 3}) == ['b']
    assert find_common_in_dicts({}, {'a': 1}) == None
    assert find_common_in_dicts({'a': 1}, {}) == None
