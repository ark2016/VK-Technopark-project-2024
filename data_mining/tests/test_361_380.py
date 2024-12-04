import pytest
from functions.file_361_380 import *


# 361. Тесты для функции `find_not_divisible_by_2_or_3_in_both_sets`
def test_find_not_divisible_by_2_or_3_in_both_sets():
    assert find_not_divisible_by_2_or_3_in_both_sets({1, 2, 3, 5, 7}, {5, 7, 9, 11}) == [5, 7]
    assert find_not_divisible_by_2_or_3_in_both_sets({1, 3, 5, 7}, {2, 4, 6, 8}) is None
    assert find_not_divisible_by_2_or_3_in_both_sets(set(), set()) is None
    assert find_not_divisible_by_2_or_3_in_both_sets({10, 15, 25}, {10, 25, 35}) == [25]
    assert find_not_divisible_by_2_or_3_in_both_sets({5, 8, 11, 14}, {3, 6, 9, 12}) is None
    assert find_not_divisible_by_2_or_3_in_both_sets({1, 2, 4, 5, 10}, {5, 10, 11, 20}) == [5]
    assert find_not_divisible_by_2_or_3_in_both_sets({1, 2, 3}, {4, 5, 6}) is None
    assert find_not_divisible_by_2_or_3_in_both_sets({4, 5, 6}, {4, 5, 6}) == [5]
    assert find_not_divisible_by_2_or_3_in_both_sets({1, 9, 13}, {2, 9, 13}) == [13]


# 362. Тесты для функции `find_divisible_by_4_in_both_sets`
def test_find_divisible_by_4_in_both_sets():
    assert find_divisible_by_4_in_both_sets({4, 8, 12, 16}, {4, 8, 16, 20}) == [4, 8, 16]
    assert find_divisible_by_4_in_both_sets({1, 2, 3}, {5, 7, 11}) is None
    assert find_divisible_by_4_in_both_sets({32, 48, 64}, {32, 64, 96}) == [32, 64]
    assert find_divisible_by_4_in_both_sets({1, 4, 6, 8}, {2, 4, 8, 16}) == [4, 8]
    assert find_divisible_by_4_in_both_sets({16, 32, 48}, {24, 32, 48}) == [32, 48]
    assert find_divisible_by_4_in_both_sets({3, 6, 9}, {12, 15, 18}) is None
    assert find_divisible_by_4_in_both_sets({4, 5, 6}, {7, 8, 9}) is None
    assert find_divisible_by_4_in_both_sets({4, 8, 12}, {16, 20, 24}) is None
    assert find_divisible_by_4_in_both_sets({8, 12, 16}, {8, 16, 20}) == [8, 16]


# 363. Тесты для функции `find_in_set_not_other_v2`
def test_find_in_set_not_other_v2():
    assert find_in_set_not_other_v2({1, 2, 3}, {2, 3, 4}) == [1]
    assert find_in_set_not_other_v2({4, 5, 6}, {1, 2, 3}) == [4, 5, 6]
    assert find_in_set_not_other_v2(set(), {1, 2, 3}) is None
    assert find_in_set_not_other_v2({1, 2, 3}, {1, 2, 3}) is None
    assert find_in_set_not_other_v2({1, 3, 5}, {2, 4, 6}) == [1, 3, 5]
    assert find_in_set_not_other_v2({10, 20, 30}, {20, 40, 60}) == [10, 30]
    assert find_in_set_not_other_v2({7, 8, 9}, {7, 8, 9}) is None
    assert find_in_set_not_other_v2({5, 6, 7}, {7, 8, 9}) == [5, 6]
    assert find_in_set_not_other_v2({0, 1, 2}, {0, 2, 4}) == [1]


# 364. Тесты для функции `find_in_any_set`
def test_find_in_any_set():
    assert find_in_any_set({1, 2, 3}, {3, 4, 5}) == [1, 2, 3, 4, 5]
    assert find_in_any_set({1, 3, 5}, {2, 4, 6}) == [1, 2, 3, 4, 5, 6]
    assert find_in_any_set(set(), set()) == None
    assert find_in_any_set({1, 2, 3}, {4, 5, 6}) == [1, 2, 3, 4, 5, 6]
    assert find_in_any_set({7, 8, 9}, {10, 11, 12}) == [7, 8, 9, 10, 11, 12]
    assert find_in_any_set({1, 2}, {2, 3}) == [1, 2, 3]
    assert find_in_any_set({1, 3, 5}, {1, 3, 5}) == [1, 3, 5]
    assert find_in_any_set({1, 4, 7}, {2, 5, 8}) == [1, 2, 4, 5, 7, 8]
    assert find_in_any_set({1}, set()) == [1]


# 365. Тесты для функции `find_divisible_by_7_in_both_sets`
def test_find_divisible_by_7_in_both_sets():
    assert find_divisible_by_7_in_both_sets({7, 14, 21}, {14, 21, 28}) == [14, 21]
    assert find_divisible_by_7_in_both_sets({1, 2, 3}, {4, 5, 6}) is None
    assert find_divisible_by_7_in_both_sets({7, 14, 21, 28}, {7, 21, 35, 49}) == [7, 21]
    assert find_divisible_by_7_in_both_sets({7, 14, 28}, {14, 21, 35}) == [14]
    assert find_divisible_by_7_in_both_sets({14, 21, 28}, {14, 21, 28}) == [14, 21, 28]
    assert find_divisible_by_7_in_both_sets({7, 14}, {21, 28}) is None
    assert find_divisible_by_7_in_both_sets({2, 3, 5}, {7, 11, 13}) is None
    assert find_divisible_by_7_in_both_sets({14, 21, 35}, {14, 21, 35}) == [14, 21, 35]
    assert find_divisible_by_7_in_both_sets({1, 7, 14}, {7, 14, 21}) == [7, 14]


# 366. Тесты для функции `find_difference_in_sets`
def test_find_difference_in_sets():
    assert find_difference_in_sets({1, 2, 3}, {2, 3, 4}) == [1]
    assert find_difference_in_sets({4, 5, 6}, {1, 2, 3}) == [4, 5, 6]
    assert find_difference_in_sets(set(), {1, 2, 3}) is None
    assert find_difference_in_sets({1, 2, 3}, {1, 2, 3}) is None
    assert find_difference_in_sets({1, 3, 5}, {2, 4, 6}) == [1, 3, 5]
    assert find_difference_in_sets({10, 20, 30}, {20, 40, 60}) == [10, 30]
    assert find_difference_in_sets({7, 8, 9}, {7, 8, 9}) is None


# 367. Тесты для функции `find_not_divisible_by_2_in_both_sets`
def test_find_not_divisible_by_2_in_both_sets():
    assert find_not_divisible_by_2_in_both_sets({1, 2, 3, 5}, {3, 5, 7, 9}) == [3, 5]
    assert find_not_divisible_by_2_in_both_sets({2, 4, 6, 8}, {1, 3, 5, 7}) is None
    assert find_not_divisible_by_2_in_both_sets({1, 3, 5, 7}, {3, 5, 9, 11}) == [3, 5]
    assert find_not_divisible_by_2_in_both_sets({10, 15, 25}, {10, 25, 35}) == [25]
    assert find_not_divisible_by_2_in_both_sets(set(), {1, 3, 5}) is None
    assert find_not_divisible_by_2_in_both_sets({1, 3, 5}, {6, 8, 10}) is None
    assert find_not_divisible_by_2_in_both_sets({3, 5, 7}, {1, 3, 7}) == [3, 7]
    assert find_not_divisible_by_2_in_both_sets({5, 9, 13}, {5, 9, 17}) == [5, 9]
    assert find_not_divisible_by_2_in_both_sets({2, 4, 6}, {3, 5, 7}) is None


# 368. Тесты для функции `find_common_in_three_sets`
def test_find_common_in_three_sets():
    assert find_common_in_three_sets({1, 2, 3}, {2, 3, 4}, {3, 4, 5}) == [3]
    assert find_common_in_three_sets({1, 2, 3}, {3, 4, 5}, {5, 6, 7}) is None
    assert find_common_in_three_sets({10, 20, 30}, {20, 30, 40}, {30, 40, 50}) == [30]
    assert find_common_in_three_sets({5, 10, 15}, {15, 20, 25}, {15, 30, 45}) == [15]
    assert find_common_in_three_sets({1, 1, 1}, {2, 2, 2}, {3, 3, 3}) is None
    assert find_common_in_three_sets({4, 8, 12}, {8, 12, 16}, {12, 16, 20}) == [12]
    assert find_common_in_three_sets({1, 3, 5}, {1, 3, 5}, {1, 3, 5}) == [1, 3, 5]
    assert find_common_in_three_sets(set(), {1, 2, 3}, {1, 2, 3}) is None
    assert find_common_in_three_sets({2, 4, 6}, {4, 6, 8}, {6, 8, 10}) == [6]


# 369. Тесты для функции `find_difference_in_three_sets`
def test_find_difference_in_three_sets():
    assert find_difference_in_three_sets({1, 2, 3}, {2, 3, 4}, {3, 4, 5}) == [1]
    assert find_difference_in_three_sets({1, 2, 3}, {1, 2, 3}, {1, 2, 3}) is None
    assert find_difference_in_three_sets({5, 10, 15}, {10, 15, 20}, {15, 20, 25}) == [5]
    assert find_difference_in_three_sets({7, 14, 21}, {14, 21, 28}, {21, 28, 35}) == [7]
    assert find_difference_in_three_sets({2, 3, 4}, {4, 5, 6}, {6, 7, 8}) == [2, 3]
    assert find_difference_in_three_sets({10, 20, 30}, {20, 30, 40}, {30, 40, 50}) == [10]
    assert find_difference_in_three_sets({1, 3, 5}, {2, 4, 6}, {3, 6, 9}) == [1, 5]
    assert find_difference_in_three_sets({1, 2}, {2, 3}, {3, 4}) == [1]
    assert find_difference_in_three_sets(set(), {1, 2, 3}, {1, 2, 3}) is None


# 370. Тесты для функции `find_diff_in_sets_v2`
def test_find_diff_in_sets_v2():
    assert find_diff_in_sets_v2({1, 2, 3}, {2, 3, 4}) == [1]
    assert find_diff_in_sets_v2({4, 5, 6}, {1, 2, 3}) == [4, 5, 6]
    assert find_diff_in_sets_v2(set(), {1, 2, 3}) is None
    assert find_diff_in_sets_v2({1, 2, 3}, {1, 2, 3}) is None
    assert find_diff_in_sets_v2({1, 3, 5}, {2, 4, 6}) == [1, 3, 5]
    assert find_diff_in_sets_v2({10, 20, 30}, {20, 40, 60}) == [10, 30]
    assert find_diff_in_sets_v2({7, 8, 9}, {7, 8, 9}) is None
    assert find_diff_in_sets_v2({5, 6, 7}, {7, 8, 9}) == [5, 6]
    assert find_diff_in_sets_v2({0, 1, 2}, {0, 2, 4}) == [1]


# 371. Тесты для функции `find_not_divisible_by_5_in_both_sets`
def test_find_not_divisible_by_5_in_both_sets():
    assert find_not_divisible_by_5_in_both_sets({1, 2, 3, 10, 15}, {2, 3, 20, 25}) == [2, 3]
    assert find_not_divisible_by_5_in_both_sets({5, 10, 15}, {5, 10, 15}) is None
    assert find_not_divisible_by_5_in_both_sets({1, 2, 3}, {4, 5, 6}) is None
    assert find_not_divisible_by_5_in_both_sets({10, 20, 30}, {40, 50, 60}) is None
    assert find_not_divisible_by_5_in_both_sets({1, 3, 7, 11}, {7, 11, 13, 17}) == [7, 11]
    assert find_not_divisible_by_5_in_both_sets(set(), set()) is None
    assert find_not_divisible_by_5_in_both_sets({1, 2, 3}, {5, 10, 15}) == None
    assert find_not_divisible_by_5_in_both_sets({5, 6, 7}, {5, 6, 7}) == [6, 7]
    assert find_not_divisible_by_5_in_both_sets({4, 5, 6}, {4, 6, 7}) == [4, 6]


# 372. Тесты для функции `find_divisible_by_3_or_6_in_both_sets`
def test_find_divisible_by_3_or_6_in_both_sets():
    assert find_divisible_by_3_or_6_in_both_sets({3, 6, 9, 12}, {6, 9, 12, 18}) == [6, 9, 12]
    assert find_divisible_by_3_or_6_in_both_sets({1, 2, 3}, {4, 5, 6}) is None
    assert find_divisible_by_3_or_6_in_both_sets({2, 4, 6, 8}, {3, 5, 9, 12}) == None
    assert find_divisible_by_3_or_6_in_both_sets({2, 4, 5}, {1, 2, 5}) == None
    assert find_divisible_by_3_or_6_in_both_sets({6, 7, 8}, {9, 10, 11}) == None
    assert find_divisible_by_3_or_6_in_both_sets(set(), set()) is None
    assert find_divisible_by_3_or_6_in_both_sets({3, 6, 9}, {1, 2, 3}) == [3]
    assert find_divisible_by_3_or_6_in_both_sets({4, 5, 6}, {6, 7, 8}) == [6]
    assert find_divisible_by_3_or_6_in_both_sets({10, 20, 30}, {10, 30, 40}) == [30]


# 373. Тесты для функции `find_common_in_sets_divisible_by_3`
def test_find_common_in_sets_divisible_by_3():
    assert find_common_in_sets_divisible_by_3({3, 6, 9}, {3, 9, 12}) == [3, 9]
    assert find_common_in_sets_divisible_by_3({2, 4, 5}, {1, 2, 3}) is None
    assert find_common_in_sets_divisible_by_3({5, 6, 7}, {5, 6, 9}) == [6]
    assert find_common_in_sets_divisible_by_3({2, 4, 6}, {2, 4, 6}) == [6]
    assert find_common_in_sets_divisible_by_3({3, 6, 9}, {6, 9, 12}) == [6, 9]
    assert find_common_in_sets_divisible_by_3(set(), set()) is None
    assert find_common_in_sets_divisible_by_3({1, 2, 3}, {1, 2, 4}) == None
    assert find_common_in_sets_divisible_by_3({2, 5, 8}, {3, 5, 7}) is None
    assert find_common_in_sets_divisible_by_3({1, 2, 3}, {3, 6, 9}) == [3]


# 374. Тесты для функции `find_divisible_by_6_not_12_in_both_sets`
def test_find_divisible_by_6_not_12_in_both_sets():
    assert find_divisible_by_6_not_12_in_both_sets({6, 18, 24}, {6, 18, 30}) == [6, 18]
    assert find_divisible_by_6_not_12_in_both_sets({2, 4, 6}, {1, 2, 3}) == None
    assert find_divisible_by_6_not_12_in_both_sets({12, 18, 24}, {12, 18, 24}) == [18]
    assert find_divisible_by_6_not_12_in_both_sets({6, 12, 18}, {6, 18, 24}) == [6, 18]
    assert find_divisible_by_6_not_12_in_both_sets({1, 3, 5}, {6, 9, 12}) == None
    assert find_divisible_by_6_not_12_in_both_sets(set(), set()) is None
    assert find_divisible_by_6_not_12_in_both_sets({2, 4, 6}, {2, 4, 6}) == [6]
    assert find_divisible_by_6_not_12_in_both_sets({1, 2, 4}, {2, 4, 6}) is None
    assert find_divisible_by_6_not_12_in_both_sets({3, 6, 9}, {6, 9, 12}) == [6]


# 375. Тесты для функции `find_not_in_both_sets`
def test_find_not_in_both_sets():
    assert find_not_in_both_sets({1, 2, 3}, {3, 4, 5}) == [1, 2, 4, 5]
    assert find_not_in_both_sets({1, 2, 3}, {1, 2, 3}) is None
    assert find_not_in_both_sets({4, 5, 6}, {4, 6, 7}) == [5, 7]
    assert find_not_in_both_sets({2, 3, 4}, {1, 2, 3}) == [1, 4]
    assert find_not_in_both_sets({10, 20, 30}, {20, 30, 40}) == [10, 40]
    assert find_not_in_both_sets(set(), set()) is None
    assert find_not_in_both_sets({1, 2, 4}, {2, 3, 4}) == [1, 3]
    assert find_not_in_both_sets({2, 3, 5}, {3, 5, 7}) == [2, 7]
    assert find_not_in_both_sets({7, 8, 9}, {8, 9, 10}) == [7, 10]


# 376. Тесты для функции `find_difference_between_three_sets`
def test_find_difference_between_three_sets():
    assert find_difference_between_three_sets({1, 2, 3}, {2, 3, 4}, {3, 4, 5}) == [1]
    assert find_difference_between_three_sets({1, 2, 3}, {1, 2, 3}, {1, 2, 3}) is None
    assert find_difference_between_three_sets({5, 10, 15}, {10, 15, 20}, {15, 20, 25}) == [5]
    assert find_difference_between_three_sets({7, 14, 21}, {14, 21, 28}, {21, 28, 35}) == [7]
    assert find_difference_between_three_sets({2, 3, 4}, {4, 5, 6}, {6, 7, 8}) == [2, 3]
    assert find_difference_between_three_sets({10, 20, 30}, {20, 30, 40}, {30, 40, 50}) == [10]
    assert find_difference_between_three_sets({1, 3, 5}, {2, 4, 6}, {3, 6, 9}) == [1, 5]
    assert find_difference_between_three_sets({1, 2}, {2, 3}, {3, 4}) == [1]
    assert find_difference_between_three_sets(set(), {1, 2, 3}, {1, 2, 3}) is None


# 377. Тесты для функции `find_divisible_by_2_not_3_in_both_sets`
def test_find_divisible_by_2_not_3_in_both_sets():
    assert find_divisible_by_2_not_3_in_both_sets({2, 4, 6}, {2, 4, 8}) == [2, 4]
    assert find_divisible_by_2_not_3_in_both_sets({1, 3, 5}, {2, 4, 6}) == None
    assert find_divisible_by_2_not_3_in_both_sets({8, 10, 12}, {6, 8, 10}) == [8, 10]
    assert find_divisible_by_2_not_3_in_both_sets({4, 5, 6}, {1, 2, 4}) == [4]
    assert find_divisible_by_2_not_3_in_both_sets({1, 2, 3}, {4, 5, 6}) == None
    assert find_divisible_by_2_not_3_in_both_sets({2, 4, 6}, {3, 5, 7}) is None
    assert find_divisible_by_2_not_3_in_both_sets({2, 4, 6}, {4, 6, 8}) == [4]
    assert find_divisible_by_2_not_3_in_both_sets({1, 4, 5}, {2, 3, 4}) == [4]
    assert find_divisible_by_2_not_3_in_both_sets({8, 10, 12}, {14, 16, 18}) == None


# 378. Тесты для функции `find_common_not_divisible_by_4`
def test_find_common_not_divisible_by_4():
    assert find_common_not_divisible_by_4({1, 2, 3, 8, 12}, {2, 3, 12, 16}) == [2, 3]
    assert find_common_not_divisible_by_4({2, 4, 6}, {4, 6, 8}) == [6]
    assert find_common_not_divisible_by_4({1, 2, 3}, {4, 5, 6}) is None
    assert find_common_not_divisible_by_4({1, 3, 5}, {1, 3, 7}) == [1, 3]
    assert find_common_not_divisible_by_4({4, 8, 12}, {4, 12, 16}) is None
    assert find_common_not_divisible_by_4({3, 6, 9}, {6, 9, 12}) == [6, 9]
    assert find_common_not_divisible_by_4(set(), {1, 2, 3}) is None
    assert find_common_not_divisible_by_4({1, 2, 3}, {1, 2, 3}) == [1, 2, 3]
    assert find_common_not_divisible_by_4({5, 6, 7}, {6, 7, 8}) == [6, 7]


# 379. Тесты для функции `find_unique_in_sets`
def test_find_unique_in_sets():
    assert find_unique_in_sets({1, 2, 3}, {3, 4, 5}) == [1, 2, 4, 5]
    assert find_unique_in_sets({1, 2, 3}, {1, 2, 3}) is None
    assert find_unique_in_sets({4, 5, 6}, {4, 6, 7}) == [5, 7]
    assert find_unique_in_sets({2, 3, 4}, {1, 2, 3}) == [1, 4]
    assert find_unique_in_sets({10, 20, 30}, {20, 30, 40}) == [10, 40]
    assert find_unique_in_sets(set(), set()) is None
    assert find_unique_in_sets({1, 2, 4}, {2, 3, 4}) == [1, 3]
    assert find_unique_in_sets({2, 3, 5}, {3, 5, 7}) == [2, 7]
    assert find_unique_in_sets({7, 8, 9}, {8, 9, 10}) == [7, 10]


# 380. Тесты для функции `find_common_in_all_sets`
def test_find_common_in_all_sets():
    assert find_common_in_all_sets({1, 2, 3}, {2, 3, 4}, {3, 4, 5}) == [3]
    assert find_common_in_all_sets({1, 2, 3}, {3, 4, 5}, {5, 6, 7}) is None
    assert find_common_in_all_sets({10, 20, 30}, {20, 30, 40}, {30, 40, 50}) == [30]
    assert find_common_in_all_sets({5, 10, 15}, {15, 20, 25}, {15, 30, 45}) == [15]
    assert find_common_in_all_sets({1, 1, 1}, {2, 2, 2}, {3, 3, 3}) is None
    assert find_common_in_all_sets({4, 8, 12}, {8, 12, 16}, {12, 16, 20}) == [12]
    assert find_common_in_all_sets({1, 3, 5}, {1, 3, 5}, {1, 3, 5}) == [1, 3, 5]
    assert find_common_in_all_sets(set(), {1, 2, 3}, {1, 2, 3}) is None
    assert find_common_in_all_sets({2, 4, 6}, {4, 6, 8}, {6, 8, 10}) == [6]
