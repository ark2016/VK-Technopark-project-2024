import pytest
from functions.file_341_360 import *


# 341. Тесты для функции `sum_list_3`
def test_sum_list_3():
    assert sum_list_3([1, 2, 3]) == 6
    assert sum_list_3([]) == None
    assert sum_list_3([0]) == 0


# 342. Тесты для функции `find_divisible_by_3_not_9`
def test_find_divisible_by_3_not_9():
    assert find_divisible_by_3_not_9([3, 6, 9]) == [3, 6]
    assert find_divisible_by_3_not_9([9, 18, 27]) == None
    assert find_divisible_by_3_not_9([]) == None


# 343. Тесты для функции `find_divisible_by_5_or_7`
def test_find_divisible_by_5_or_7():
    assert find_divisible_by_5_or_7([5, 10, 7, 14, 21]) == [5, 10, 7, 14, 21]
    assert find_divisible_by_5_or_7([1, 2, 3]) == None
    assert find_divisible_by_5_or_7([]) == None


# 344. Тесты для функции `find_in_dicts`
def test_find_in_dicts():
    assert find_in_dicts({'a': 1, 'b': 2}, {'a': 3, 'c': 4}) == ['a']
    assert find_in_dicts({'a': 1}, {'b': 2}) == None
    assert find_in_dicts({}, {'a': 1}) == None


# 345. Тесты для функции `find_divisible_by_3_or_5`
def test_find_divisible_by_3_or_5():
    assert find_divisible_by_3_or_5([3, 5, 15, 30]) == [3, 5, 15, 30]
    assert find_divisible_by_3_or_5([1, 2, 4]) == None
    assert find_divisible_by_3_or_5([]) == None


# 346. Тесты для функции `find_divisible_by_4_not_6`
def test_find_divisible_by_4_not_6():
    assert find_divisible_by_4_not_6([4, 8, 12, 24]) == [4, 8]
    assert find_divisible_by_4_not_6([6, 12, 18]) == None
    assert find_divisible_by_4_not_6([]) == None


# 347. Тесты для функции `find_divisible_by_5_not_10`
def test_find_divisible_by_5_not_10():
    assert find_divisible_by_5_not_10([5, 15, 20]) == [5, 15]
    assert find_divisible_by_5_not_10([10, 20, 30]) == None
    assert find_divisible_by_5_not_10([]) == None


# 348. Тесты для функции `find_powers_of_list`
def test_find_powers_of_list():
    assert find_powers_of_list([2, 3, 4], 2) == [4, 9, 16]
    assert find_powers_of_list([1, 0, -1], 3) == [1, 0, -1]
    assert find_powers_of_list([], 2) == None


# 349. Тесты для функции `find_divisible_by_6_not_12`
def test_find_divisible_by_6_not_12():
    assert find_divisible_by_6_not_12([6, 18, 12, 24]) == [6, 18]
    assert find_divisible_by_6_not_12([12, 24, 36]) == None
    assert find_divisible_by_6_not_12([]) == None


# 350. Тесты для функции `find_divisible_by_4_or_5`
def test_find_divisible_by_4_or_5():
    assert find_divisible_by_4_or_5([4, 5, 8, 10]) == [4, 5, 8, 10]
    assert find_divisible_by_4_or_5([1, 2, 3]) == None
    assert find_divisible_by_4_or_5([]) == None


# 351. Тесты для функции `find_in_list_not_in_another`
def test_find_in_list_not_in_another():
    assert find_in_list_not_in_another([1, 2, 3], [2, 3, 4]) == [1]
    assert find_in_list_not_in_another([5, 6, 7], [5, 6, 7]) == None
    assert find_in_list_not_in_another([], [1, 2, 3]) == None


# 352. Тесты для функции `find_unique_keys_in_dict`
def test_find_unique_keys_in_dict():
    assert find_unique_keys_in_dict({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == ['a']
    assert find_unique_keys_in_dict({'a': 1}, {'a': 2}) == None
    assert find_unique_keys_in_dict({}, {'a': 1}) == None


# 353. Тесты для функции `multiply_lists`
def test_multiply_lists():
    assert multiply_lists([1, 2, 3], [4, 5, 6]) == [4, 10, 18]
    assert multiply_lists([1, 2], [3, 4, 5]) == [3, 8]
    assert multiply_lists([], [1, 2, 3]) == None


# 354. Тесты для функции `subtract_lists_v2`
def test_subtract_lists_v2():
    assert subtract_lists_v2([5, 6, 7], [1, 2, 3]) == [4, 4, 4]
    assert subtract_lists_v2([10, 20], [5, 5]) == [5, 15]
    assert subtract_lists_v2([], [1, 2]) == None


# 355. Тесты для функции `find_in_set_not_other`
def test_find_in_set_not_other():
    assert find_in_set_not_other({1, 2, 3}, {2, 3, 4}) == [1]
    assert find_in_set_not_other({5, 6, 7}, {5, 6, 7}) == None
    assert find_in_set_not_other(set(), {1, 2, 3}) == None


# 356. Тесты для функции `find_common_in_sets`
def test_find_common_in_sets():
    assert find_common_in_sets({1, 2, 3}, {2, 3, 4}) == [2, 3]
    assert find_common_in_sets({1, 2}, {3, 4}) == None
    assert find_common_in_sets(set(), {1, 2, 3}) == None


# 357. Тесты для функции `find_divisible_by_2_in_both_sets`
def test_find_divisible_by_2_in_both_sets():
    assert find_divisible_by_2_in_both_sets({2, 4, 6}, {4, 6, 8}) == [4, 6]
    assert find_divisible_by_2_in_both_sets({1, 3, 5}, {2, 4, 6}) == None
    assert find_divisible_by_2_in_both_sets(set(), {2, 4, 6}) == None


# 358. Тесты для функции `find_not_divisible_by_3_in_both_sets`
def test_find_not_divisible_by_3_in_both_sets():
    assert find_not_divisible_by_3_in_both_sets({1, 2, 4}, {2, 4, 5}) == [2, 4]
    assert find_not_divisible_by_3_in_both_sets({3, 6, 9}, {3, 6, 9}) == None
    assert find_not_divisible_by_3_in_both_sets(set(), {1, 2, 3}) == None


# 359. Тесты для функции `find_in_one_set_not_other_v2`
def test_find_in_one_set_not_other_v2():
    assert find_in_one_set_not_other_v2({1, 2, 3}, {2, 3, 4}) == [1]
    assert find_in_one_set_not_other_v2({5, 6, 7}, {5, 6, 7}) == None
    assert find_in_one_set_not_other_v2(set(), {1, 2, 3}) == None


# 360. Тесты для функции `find_divisible_by_2_or_5_in_both_sets`
def test_find_divisible_by_2_or_5_in_both_sets():
    assert find_divisible_by_2_or_5_in_both_sets({10, 15, 20}, {5, 10, 20}) == [10, 20]
    assert find_divisible_by_2_or_5_in_both_sets({1, 3, 7}, {2, 4, 8}) == None
    assert find_divisible_by_2_or_5_in_both_sets(set(), {1, 2, 3}) == None
