import pytest
from functions.file_281_300 import *


# 281. Тесты для функции `find_in_both_lists`:
def test_find_in_both_lists():
    assert find_in_both_lists([1, 2, 3], [3, 4, 5]) == [3]
    assert find_in_both_lists([1, 2, 3], [4, 5, 6]) == None
    assert find_in_both_lists([], [1, 2, 3]) == None
    assert find_in_both_lists([1, 2, 3], []) == None
    assert find_in_both_lists([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert find_in_both_lists([-1, -2, -3], [-3, -4, -5]) == [-3]
    assert find_in_both_lists([0, 2, 4], [4, 0, 6]) == [0, 4]
    assert find_in_both_lists([1.1, 2.2, 3.3], [3.3, 4.4, 5.5]) == [3.3]
    assert find_in_both_lists(["a", "b", "c"], ["c", "d", "e"]) == ["c"]

# 282. Тесты для функции `find_not_in_list`:
def test_find_not_in_list():
    assert find_not_in_list([1, 2, 3], [3, 4, 5]) == [1, 2]
    assert find_not_in_list([1, 2, 3], [1, 2, 3]) == None
    assert find_not_in_list([], [1, 2, 3]) == None
    assert find_not_in_list([1, 2, 3], []) == [1, 2, 3]
    assert find_not_in_list([-1, -2, -3], [-3, -4, -5]) == [-1, -2]
    assert find_not_in_list([0, 2, 4], [4, 0, 6]) == [2]
    assert find_not_in_list([1.1, 2.2, 3.3], [3.3, 4.4, 5.5]) == [1.1, 2.2]
    assert find_not_in_list(["a", "b", "c"], ["c", "d", "e"]) == ["a", "b"]

# 283. Тесты для функции `find_product_not_divisible_by_7`:
def test_find_product_not_divisible_by_7():
    assert find_product_not_divisible_by_7([7, 14, 21]) == None
    assert find_product_not_divisible_by_7([1, 7, 14]) == None
    assert find_product_not_divisible_by_7([]) == None
    assert find_product_not_divisible_by_7([2, 3]) == [6]
    assert find_product_not_divisible_by_7([3, 5]) == [15]
    assert find_product_not_divisible_by_7([1, 2, 3, 4]) == [2, 3, 4, 6, 8, 12]

# 284. Тесты для функции `find_product_of_two_odds`:
def test_find_product_of_two_odds():
    assert find_product_of_two_odds([1, 3, 5, 7]) == [3, 5, 7, 15, 21, 35]
    assert find_product_of_two_odds([2, 4, 6]) == None
    assert find_product_of_two_odds([1, 2, 3, 4]) == [3]
    assert find_product_of_two_odds([]) == None
    assert find_product_of_two_odds([9, 7]) == [63]
    assert find_product_of_two_odds([11, 15, 19]) == [165, 209, 285]

# 285. Тесты для функции `find_sum_of_two_odds`:
def test_find_sum_of_two_odds():
    assert find_sum_of_two_odds([1, 3, 5, 7]) == [4, 6, 8, 8, 10, 12]
    assert find_sum_of_two_odds([2, 4, 6]) == None
    assert find_sum_of_two_odds([1, 2, 3, 4]) == [4]
    assert find_sum_of_two_odds([]) == None
    assert find_sum_of_two_odds([9, 7]) == [16]
    assert find_sum_of_two_odds([11, 15, 19]) == [26, 30, 34]

# 286. Тесты для функции `find_even_in_tuple`:
def test_find_even_in_tuple():
    assert find_even_in_tuple((1, 2, 3, 4, 5)) == [2, 4]
    assert find_even_in_tuple((1, 3, 5)) == None
    assert find_even_in_tuple((2, 4, 6, 8)) == [2, 4, 6, 8]
    assert find_even_in_tuple(()) == None
    assert find_even_in_tuple((1, 3, 4)) == [4]
    assert find_even_in_tuple((2, 0, -2, -4)) == [2, 0, -2, -4]
    assert find_even_in_tuple((7, 8, 10)) == [8, 10]

# 287. Тесты для функции `find_product_not_divisible_by_5`:
def test_find_product_not_divisible_by_5():
    assert find_product_not_divisible_by_5([1, 2, 3, 4]) == [2, 3, 4, 6, 8, 12]
    assert find_product_not_divisible_by_5([5, 10, 15]) == None
    assert find_product_not_divisible_by_5([1, 5, 10]) == None
    assert find_product_not_divisible_by_5([]) == None
    assert find_product_not_divisible_by_5([2, 3]) == [6]
    assert find_product_not_divisible_by_5([3, 4, 7]) == [12, 21, 28]
    assert find_product_not_divisible_by_5([11, 3, 2]) == [33, 22, 6]

# 288. Тесты для функции `find_keys_in_dict_not_in_other`:
def test_find_keys_in_dict_not_in_other():
    assert find_keys_in_dict_not_in_other({"a": 1, "b": 2, "c": 3}, {"b": 4, "d": 5}) == ["a", "c"]
    assert find_keys_in_dict_not_in_other({"a": 1}, {"a": 2}) == None
    assert find_keys_in_dict_not_in_other({}, {"a": 2}) == None
    assert find_keys_in_dict_not_in_other({"a": 1, "b": 2}, {}) == ["a", "b"]
    assert find_keys_in_dict_not_in_other({"x": 9, "y": 8}, {"y": 7}) == ["x"]
    assert find_keys_in_dict_not_in_other({"k": 11}, {"m": 13}) == ["k"]

# 289. Тесты для функции `find_difference_in_tuple`:
def test_find_difference_in_tuple():
    assert find_difference_in_tuple((1, 2, 3)) == [1, 2, 1]
    assert find_difference_in_tuple((1, 1, 1)) == [0, 0, 0]
    assert find_difference_in_tuple((4, 6, 8)) == [2, 4, 2]
    assert find_difference_in_tuple(()) == None
    assert find_difference_in_tuple((3,)) == None
    assert find_difference_in_tuple((10, 5, 1)) == [5, 9, 4]


# 290. Тесты для функции `find_difference_between_lists_2`:
def test_find_difference_between_lists_2():
    assert find_difference_between_lists_2([1, 2, 3], [4, 5, 6]) == [3, 4, 5, 2, 3, 4, 1, 2, 3]
    assert find_difference_between_lists_2([1, 1, 1], [1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert find_difference_between_lists_2([10, 20], [1, 2]) == [9, 8, 19, 18]
    assert find_difference_between_lists_2([5], [3]) == [2]
    assert find_difference_between_lists_2([], [1, 2, 3]) == None
    assert find_difference_between_lists_2([1, 2, 3], []) == None
    assert find_difference_between_lists_2([], []) == None


# 291. Тесты для функции `find_odd_in_one_list`:
def test_find_odd_in_one_list():
    assert find_odd_in_one_list([1, 2, 3], [3, 4, 5]) == [1, 5]
    assert find_odd_in_one_list([1, 3, 5], [1, 3, 5]) == None
    assert find_odd_in_one_list([], [1, 3, 5]) == [1, 3, 5]
    assert find_odd_in_one_list([1, 2, 4], []) == [1]
    assert find_odd_in_one_list([-1, -2, -3], [-3, -4, -5]) == [-1, -5]
    assert find_odd_in_one_list([0, 2, 4], [4, 0, 6]) == None
    assert find_odd_in_one_list([1, 2, 3], [1, 4, 3]) == None
    assert find_odd_in_one_list([1.1, 2.2, 3.3], [3.3, 4.4, 5.5]) == [1.1, 2.2, 4.4, 5.5]

# 292. Тесты для функции `find_sum_of_two_from_one_list`:
def test_find_sum_of_two_from_one_list():
    assert find_sum_of_two_from_one_list([1, 2, 3, 4]) == [3, 4, 5, 5, 6, 7]
    assert find_sum_of_two_from_one_list([1, 1, 1]) == [2, 2, 2]
    assert find_sum_of_two_from_one_list([]) == None
    assert find_sum_of_two_from_one_list([0, 2, 4]) == [2, 4, 6]
    assert find_sum_of_two_from_one_list([-1, -2, -3]) == [-3, -4, -5]
    assert find_sum_of_two_from_one_list([1.1, 2.2, 3.3]) == [3.3000000000000003, 4.4, 5.5]
    assert find_sum_of_two_from_one_list([0, 0, 0]) == [0, 0, 0]

# 293. Тесты для функции `find_common_not_in_both_lists`:
def test_find_common_not_in_both_lists():
    assert find_common_not_in_both_lists([1, 2, 3], [3, 4, 5]) == [3]
    assert find_common_not_in_both_lists([1, 2, 3], [4, 5, 6]) == None
    assert find_common_not_in_both_lists([], [1, 2, 3]) == None
    assert find_common_not_in_both_lists([1, 2, 3], []) == None
    assert find_common_not_in_both_lists([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert find_common_not_in_both_lists([-1, -2, -3], [-3, -4, -5]) == [-3]
    assert find_common_not_in_both_lists([0, 2, 4], [4, 0, 6]) == [0, 4]
    assert find_common_not_in_both_lists([1.1, 2.2, 3.3], [3.3, 4.4, 5.5]) == [3.3]
    assert find_common_not_in_both_lists(["a", "b", "c"], ["c", "d", "e"]) == ["c"]

# 294. Тесты для функции `find_sum_of_elements_from_two_lists`:
def test_find_sum_of_elements_from_two_lists():
    assert find_sum_of_elements_from_two_lists([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert find_sum_of_elements_from_two_lists([1, 1, 1], [1, 1, 1]) == [2, 2, 2]
    assert find_sum_of_elements_from_two_lists([], [1, 2, 3]) == None
    assert find_sum_of_elements_from_two_lists([1, 2, 3], []) == None
    assert find_sum_of_elements_from_two_lists([1, 2, 3], [1, 2, 3]) == [2, 4, 6]
    assert find_sum_of_elements_from_two_lists([-1, -2, -3], [-3, -4, -5]) == [-4, -6, -8]
    assert find_sum_of_elements_from_two_lists([0, 2, 4], [4, 0, 6]) == [4, 2, 10]

# 295. Тесты для функции `find_difference_of_elements_from_two_lists`:
def test_find_difference_of_elements_from_two_lists():
    assert find_difference_of_elements_from_two_lists([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]
    assert find_difference_of_elements_from_two_lists([1, 1, 1], [1, 1, 1]) == [0, 0, 0]
    assert find_difference_of_elements_from_two_lists([], [1, 2, 3]) == None
    assert find_difference_of_elements_from_two_lists([1, 2, 3], []) == None
    assert find_difference_of_elements_from_two_lists([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    assert find_difference_of_elements_from_two_lists([-1, -2, -3], [-3, -4, -5]) == [2, 2, 2]
    assert find_difference_of_elements_from_two_lists([0, 2, 4], [4, 0, 6]) == [-4, 2, -2]

# 296. Тесты для функции `square_numbers`:
def test_square_numbers():
    assert square_numbers([1, 2, 3, 4]) == [1, 4, 9, 16]
    assert square_numbers([0, 1, -1, 2]) == [0, 1, 1, 4]
    assert square_numbers([5, 6, 7]) == [25, 36, 49]
    assert square_numbers([-5, -6, -7]) == [25, 36, 49]
    assert square_numbers([]) == None
    assert square_numbers([1]) == [1]
    assert square_numbers([2.2, 3.3]) == [4.840000000000001, 10.889999999999999]

# 297. Тесты для функции `find_divisible_by_3_not_5`:
def test_find_divisible_by_3_not_5():
    assert find_divisible_by_3_not_5([3, 6, 9, 12, 15]) == [3, 6, 9, 12]
    assert find_divisible_by_3_not_5([5, 10, 15]) == None
    assert find_divisible_by_3_not_5([1, 2, 4, 5]) == None
    assert find_divisible_by_3_not_5([]) == None
    assert find_divisible_by_3_not_5([3, 5, 7, 11]) == [3]
    assert find_divisible_by_3_not_5([6, 9, 18]) == [6, 9, 18]
    assert find_divisible_by_3_not_5([-3, -6, -9]) == [-3, -6, -9]
    assert find_divisible_by_3_not_5([21, 25, 30]) == [21]
    assert find_divisible_by_3_not_5([0, 3, 6, 15, 30]) == [3, 6]


# 298. Тесты для функции `find_unique_in_one_list_3`:
def test_find_unique_in_one_list_3():
    assert find_unique_in_one_list_3([1, 2, 3], [3, 2, 1]) == [1, 3, 3, 1]
    assert find_unique_in_one_list_3([1, 1, 1], [1, 1, 1]) == None
    assert find_unique_in_one_list_3([], [1, 2, 3]) == None
    assert find_unique_in_one_list_3([1, 2, 3], []) == None
    assert find_unique_in_one_list_3([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6]
    assert find_unique_in_one_list_3([-1, -2, -3], [-3, -2, -1]) == [-1, -3, -3, -1]
    assert find_unique_in_one_list_3([0, 2, 4], [4, 2, 0]) == [0, 4, 4, 0]


# 299. Тесты для функции `find_in_list_not_in_tuple_2`:
def test_find_in_list_not_in_tuple_2():
    assert find_in_list_not_in_tuple_2([1, 2, 3], (3, 4, 5)) == [1, 2]
    assert find_in_list_not_in_tuple_2([1, 2, 3], (1, 2, 3)) == None
    assert find_in_list_not_in_tuple_2([], (1, 2, 3)) == None
    assert find_in_list_not_in_tuple_2([1, 2, 3], ()) == [1, 2, 3]
    assert find_in_list_not_in_tuple_2([-1, -2, -3], (-3, -4, -5)) == [-1, -2]
    assert find_in_list_not_in_tuple_2([0, 2, 4], (4, 0, 6)) == [2]
    assert find_in_list_not_in_tuple_2([1.1, 2.2, 3.3], (3.3, 4.4, 5.5)) == [1.1, 2.2]
    assert find_in_list_not_in_tuple_2(["a", "b", "c"], ("c", "d", "e")) == ["a", "b"]
    assert find_in_list_not_in_tuple_2(["a", "b", "c"], ("a", "b", "c")) == None


# 300. Тесты для функции `find_cubes`:
def test_find_cubes():
    assert find_cubes([1, 2, 3]) == [1, 8, 27]
    assert find_cubes([-1, -2, -3]) == [-1, -8, -27]
    assert find_cubes([0, 2, 4]) == [0, 8, 64]
    assert find_cubes([]) == None
    assert find_cubes([1, 1, 1]) == [1, 1, 1]
    assert find_cubes([2]) == [8]
    assert find_cubes([3, 5, 7]) == [27, 125, 343]
    assert find_cubes([-4, -6, -8]) == [-64, -216, -512]
    assert find_cubes([1.1, 2.2]) == [1.3310000000000004, 10.648000000000003]
