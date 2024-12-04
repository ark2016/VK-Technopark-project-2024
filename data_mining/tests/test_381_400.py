import pytest
from functions.file_381_400 import *


# 381. Тесты для функции find_in_both_sets_not_divisible_by_3
def test_find_in_both_sets_not_divisible_by_3():
    assert find_in_both_sets_not_divisible_by_3({1, 2, 3, 6, 9}, {2, 3, 5, 6}) == [2]
    assert find_in_both_sets_not_divisible_by_3({1, 2, 4}, {3, 4, 5, 6}) == [4]
    assert find_in_both_sets_not_divisible_by_3({3, 6, 9}, {12, 15}) == None
    assert find_in_both_sets_not_divisible_by_3(set(), {1, 2, 4}) == None
    assert find_in_both_sets_not_divisible_by_3({1, 2, 3}, set()) == None
    assert find_in_both_sets_not_divisible_by_3({2, 4, 6}, {2, 8, 10}) == [2]
    assert find_in_both_sets_not_divisible_by_3({1, 7, 9, 10}, {3, 7, 10}) == [7, 10]
    assert find_in_both_sets_not_divisible_by_3({1, 5, 12}, {4, 5, 6, 12}) == [5]
    assert find_in_both_sets_not_divisible_by_3({8, 12, 15, 20}, {5, 8, 15, 25}) == [8]


# 382. Тесты для функции find_unique_in_one_set
def test_find_unique_in_one_set():
    assert find_unique_in_one_set({1, 2, 3}, {2, 3, 4}) == [1, 4]
    assert find_unique_in_one_set({1, 3}, {2, 4}) == [1, 2, 3, 4]
    assert find_unique_in_one_set({1, 2, 3}, {1, 2, 3}) == None
    assert find_unique_in_one_set(set(), {1, 2, 3}) == [1, 2, 3]
    assert find_unique_in_one_set({1, 2, 3}, set()) == [1, 2, 3]
    assert find_unique_in_one_set({1, 2, 3, 5}, {2, 3, 4, 5}) == [1, 4]
    assert find_unique_in_one_set({1, 6, 7}, {2, 3, 6}) == [1, 2, 3, 7]
    assert find_unique_in_one_set({9, 10}, {11, 12}) == [9, 10, 11, 12]
    assert find_unique_in_one_set({7, 8, 9}, {8, 10, 11}) == [7, 9, 10, 11]


# 383. Тесты для функции find_in_set_not_other_v3
def test_find_in_set_not_other_v3():
    assert find_in_set_not_other_v3({1, 2, 3}, {2, 3, 4}) == [1]
    assert find_in_set_not_other_v3({1, 3}, {2, 4}) == [1, 3]
    assert find_in_set_not_other_v3({1, 2, 3}, {1, 2, 3}) == None
    assert find_in_set_not_other_v3(set(), {1, 2, 3}) == None
    assert find_in_set_not_other_v3({1, 2, 3}, set()) == [1, 2, 3]
    assert find_in_set_not_other_v3({1, 2, 3, 5}, {2, 3, 4, 5}) == [1]
    assert find_in_set_not_other_v3({1, 6, 7}, {2, 3, 6}) == [1, 7]
    assert find_in_set_not_other_v3({9, 10}, {11, 12}) == [9, 10]
    assert find_in_set_not_other_v3({7, 8, 9}, {8, 10, 11}) == [7, 9]


# 384. Тесты для функции find_common_divisible_by_3
def test_find_common_divisible_by_3():
    assert find_common_divisible_by_3({1, 2, 3}, {2, 3, 4}) == [3]
    assert find_common_divisible_by_3({3, 6, 9}, {6, 12, 18}) == [6]
    assert find_common_divisible_by_3({3, 6, 9}, {3, 6, 9}) == [3, 6, 9]
    assert find_common_divisible_by_3({1, 2, 4}, {5, 7, 8}) == None
    assert find_common_divisible_by_3(set(), {3, 6, 9}) == None
    assert find_common_divisible_by_3({3, 6, 9}, set()) == None
    assert find_common_divisible_by_3({1, 3, 5, 9}, {9, 12, 15}) == [9]
    assert find_common_divisible_by_3({6, 12}, {3, 6, 9}) == [6]
    assert find_common_divisible_by_3({4, 8, 12}, {3, 9, 12}) == [12]


# 385. Тесты для функции find_in_one_set_not_other_v3
def test_find_in_one_set_not_other_v3_2():
    assert find_in_one_set_not_other_v3({1, 2, 3}, {2, 3, 4}) == [1, 4]
    assert find_in_one_set_not_other_v3({1, 3}, {2, 4}) == [1, 2, 3, 4]
    assert find_in_one_set_not_other_v3({1, 2, 3}, {1, 2, 3}) == None
    assert find_in_one_set_not_other_v3(set(), {1, 2, 3}) == [1, 2, 3]
    assert find_in_one_set_not_other_v3({1, 2, 3}, set()) == [1, 2, 3]
    assert find_in_one_set_not_other_v3({1, 2, 3, 5}, {2, 3, 4, 5}) == [1, 4]
    assert find_in_one_set_not_other_v3({1, 6, 7}, {2, 3, 6}) == [1, 2, 3, 7]
    assert find_in_one_set_not_other_v3({9, 10}, {11, 12}) == [9, 10, 11, 12]
    assert find_in_one_set_not_other_v3({7, 8, 9}, {8, 10, 11}) == [7, 9, 10, 11]


# 386. Тесты для функции find_divisible_by_2_not_4_in_both_sets
def test_find_divisible_by_2_not_4_in_both_sets():
    assert find_divisible_by_2_not_4_in_both_sets({1, 2, 4}, {2, 3, 4}) == [2]
    assert find_divisible_by_2_not_4_in_both_sets({2, 6, 10}, {4, 6, 10}) == [6, 10]
    assert find_divisible_by_2_not_4_in_both_sets({1, 3, 5}, {7, 9, 11}) == None
    assert find_divisible_by_2_not_4_in_both_sets({1, 2}, {2, 3}) == [2]
    assert find_divisible_by_2_not_4_in_both_sets(set(), {2, 4, 6}) == None
    assert find_divisible_by_2_not_4_in_both_sets({2, 4, 6}, set()) == None
    assert find_divisible_by_2_not_4_in_both_sets({2, 3, 8}, {2, 4, 8}) == [2]
    assert find_divisible_by_2_not_4_in_both_sets({1, 2, 6}, {2, 5, 6}) == [2, 6]
    assert find_divisible_by_2_not_4_in_both_sets({4, 8, 10}, {2, 4, 8}) == None


# 387. Тесты для функции find_in_both_sets_not_divisible_by_5
def test_find_in_both_sets_not_divisible_by_5():
    assert find_in_both_sets_not_divisible_by_5({1, 2, 5, 10}, {2, 3, 5}) == [2]
    assert find_in_both_sets_not_divisible_by_5({5, 15, 25}, {10, 20, 30}) == None
    assert find_in_both_sets_not_divisible_by_5({1, 2, 3, 4, 5}, {3, 5, 7, 9}) == [3]
    assert find_in_both_sets_not_divisible_by_5({5, 10, 15}, {2, 4, 6}) == None
    assert find_in_both_sets_not_divisible_by_5(set(), {1, 2, 3}) == None
    assert find_in_both_sets_not_divisible_by_5({1, 2, 4}, set()) == None
    assert find_in_both_sets_not_divisible_by_5({1, 2, 3, 7}, {2, 3, 7}) == [2, 3, 7]
    assert find_in_both_sets_not_divisible_by_5({1, 8, 12}, {4, 8, 12}) == [8, 12]
    assert find_in_both_sets_not_divisible_by_5({6, 7, 8}, {7, 8, 9}) == [7, 8]


# 388. Тесты для функции find_in_both_sets_divisible_by_3
def test_find_in_both_sets_divisible_by_3():
    assert find_in_both_sets_divisible_by_3({1, 2, 3}, {3, 4, 5}) == [3]
    assert find_in_both_sets_divisible_by_3({6, 9, 12}, {9, 12, 18}) == [9, 12]
    assert find_in_both_sets_divisible_by_3({3, 6, 9}, {3, 6, 9}) == [3, 6, 9]
    assert find_in_both_sets_divisible_by_3({1, 4, 5}, {7, 8, 10}) == None
    assert find_in_both_sets_divisible_by_3(set(), {1, 2, 3}) == None
    assert find_in_both_sets_divisible_by_3({1, 2, 3}, set()) == None
    assert find_in_both_sets_divisible_by_3({1, 3, 6, 9}, {3, 6, 9}) == [3, 6, 9]
    assert find_in_both_sets_divisible_by_3({4, 8, 12}, {6, 12, 18}) == [12]
    assert find_in_both_sets_divisible_by_3({2, 3, 5, 6}, {1, 2, 3, 6}) == [3, 6]


# 389. Тесты для функции find_unique_in_sets_v2
def test_find_unique_in_sets_v2():
    assert find_unique_in_sets_v2({1, 2, 3}, {3, 4, 5}) == [1, 2, 4, 5]
    assert find_unique_in_sets_v2({1, 3}, {2, 4}) == [1, 2, 3, 4]
    assert find_unique_in_sets_v2({1, 2, 3}, {1, 2, 3}) == None
    assert find_unique_in_sets_v2(set(), {1, 2, 3}) == [1, 2, 3]
    assert find_unique_in_sets_v2({1, 2, 3}, set()) == [1, 2, 3]
    assert find_unique_in_sets_v2({1, 2, 3, 5}, {2, 3, 4, 5}) == [1, 4]
    assert find_unique_in_sets_v2({1, 6, 7}, {2, 3, 6}) == [1, 2, 3, 7]
    assert find_unique_in_sets_v2({9, 10}, {11, 12}) == [9, 10, 11, 12]
    assert find_unique_in_sets_v2({7, 8, 9}, {8, 10, 11}) == [7, 9, 10, 11]


# 390. Тесты для функции find_in_first_set_not_second_divisible_by_7
def test_find_in_first_set_not_second_divisible_by_7():
    assert find_in_first_set_not_second_divisible_by_7({7, 14, 21}, {1, 2, 3}) == [7, 14, 21]
    assert find_in_first_set_not_second_divisible_by_7({7, 14}, {14, 28}) == [7]
    assert find_in_first_set_not_second_divisible_by_7({1, 2, 3}, {3, 7, 14}) == None
    assert find_in_first_set_not_second_divisible_by_7({7, 14, 28}, set()) == [7, 14, 28]
    assert find_in_first_set_not_second_divisible_by_7(set(), {1, 2, 3}) == None
    assert find_in_first_set_not_second_divisible_by_7({7, 49, 70}, {7, 14, 49}) == [70]
    assert find_in_first_set_not_second_divisible_by_7({1, 2, 7}, {3, 5, 9}) == [7]
    assert find_in_first_set_not_second_divisible_by_7({14, 21, 28}, {14, 28, 35}) == [21]
    assert find_in_first_set_not_second_divisible_by_7({7, 21, 35}, {35, 42, 49}) == [7, 21]


# 391. Тесты для функции find_divisible_by_6_not_12_in_both_sets_2
def test_find_divisible_by_6_not_12_in_both_sets_2():
    assert find_divisible_by_6_not_12_in_both_sets_2({6, 12, 18}, {6, 18, 30}) == [6, 18]
    assert find_divisible_by_6_not_12_in_both_sets_2({12, 24, 36}, {24, 36, 48}) == None
    assert find_divisible_by_6_not_12_in_both_sets_2({6, 12, 18}, {12, 24, 36}) == None
    assert find_divisible_by_6_not_12_in_both_sets_2(set(), {6, 18, 24}) == None
    assert find_divisible_by_6_not_12_in_both_sets_2({6, 18, 24}, set()) == None
    assert find_divisible_by_6_not_12_in_both_sets_2({6, 12, 18}, {6, 12, 18}) == [6, 18]
    assert find_divisible_by_6_not_12_in_both_sets_2({18, 24, 30}, {6, 18, 30}) == [18, 30]
    assert find_divisible_by_6_not_12_in_both_sets_2({6, 30, 48}, {12, 18, 30}) == [30]
    assert find_divisible_by_6_not_12_in_both_sets_2({1, 2, 3, 6}, {6, 9, 12, 18}) == [6]


# 392. Тесты для функции find_in_one_set_not_other_divisible_by_5
def test_find_in_one_set_not_other_divisible_by_5():
    assert find_in_one_set_not_other_divisible_by_5({5, 10, 15}, {10, 20, 30}) == [5, 15, 20, 30]
    assert find_in_one_set_not_other_divisible_by_5({1, 2, 5}, {5, 10, 15}) == [10, 15]
    assert find_in_one_set_not_other_divisible_by_5({5, 10}, {5, 10}) == None
    assert find_in_one_set_not_other_divisible_by_5(set(), {5, 10, 15}) == [5, 10, 15]
    assert find_in_one_set_not_other_divisible_by_5({5, 10, 15}, set()) == [5, 10, 15]
    assert find_in_one_set_not_other_divisible_by_5({1, 5, 9}, {2, 5, 10}) == [10]
    assert find_in_one_set_not_other_divisible_by_5({6, 7, 8}, {5, 10, 15}) == [5, 10, 15]
    assert find_in_one_set_not_other_divisible_by_5({5, 12, 20}, {20, 30, 40}) == [5, 30, 40]
    assert find_in_one_set_not_other_divisible_by_5({3, 6, 9}, {3, 6, 9}) == None


# 393. Тесты для функции find_common_in_sets_divisible_by_4
def test_find_common_in_sets_divisible_by_4():
    assert find_common_in_sets_divisible_by_4({4, 8, 12}, {8, 12, 16}) == [8, 12]
    assert find_common_in_sets_divisible_by_4({16, 32, 48}, {32, 48, 64}) == [32, 48]
    assert find_common_in_sets_divisible_by_4({4, 8, 12}, {4, 8, 12}) == [4, 8, 12]
    assert find_common_in_sets_divisible_by_4({2, 6, 10}, {3, 6, 9}) == None
    assert find_common_in_sets_divisible_by_4(set(), {4, 8, 12}) == None
    assert find_common_in_sets_divisible_by_4({4, 8, 12}, set()) == None
    assert find_common_in_sets_divisible_by_4({8, 12, 24}, {12, 24, 36}) == [12, 24]
    assert find_common_in_sets_divisible_by_4({16, 32, 64}, {8, 16, 32}) == [16, 32]
    assert find_common_in_sets_divisible_by_4({1, 2, 4}, {2, 4, 8}) == [4]


# 394. Тесты для функции find_divisible_by_3_in_both_sets
def test_find_divisible_by_3_in_both_sets():
    assert find_divisible_by_3_in_both_sets({3, 6, 9}, {6, 9, 12}) == [6, 9]
    assert find_divisible_by_3_in_both_sets({3, 9, 15}, {3, 9, 15}) == [3, 9, 15]
    assert find_divisible_by_3_in_both_sets({6, 12, 18}, {18, 24, 30}) == [18]
    assert find_divisible_by_3_in_both_sets({1, 2, 3}, {4, 5, 6}) == None
    assert find_divisible_by_3_in_both_sets(set(), {3, 6, 9}) == None
    assert find_divisible_by_3_in_both_sets({3, 6, 9}, set()) == None
    assert find_divisible_by_3_in_both_sets({3, 12, 15}, {12, 15, 18}) == [12, 15]
    assert find_divisible_by_3_in_both_sets({6, 9, 12}, {9, 12, 15}) == [9, 12]
    assert find_divisible_by_3_in_both_sets({6, 9, 18}, {6, 12, 18}) == [6, 18]


# 395. Тесты для функции find_difference_in_sets_v2
def test_find_difference_in_sets_v2():
    assert find_difference_in_sets_v2({1, 2, 3}, {2, 3, 4}) == [1, 4]
    assert find_difference_in_sets_v2({1, 3}, {2, 4}) == [1, 2, 3, 4]
    assert find_difference_in_sets_v2({1, 2, 3}, {1, 2, 3}) == None
    assert find_difference_in_sets_v2(set(), {1, 2, 3}) == [1, 2, 3]
    assert find_difference_in_sets_v2({1, 2, 3}, set()) == [1, 2, 3]
    assert find_difference_in_sets_v2({1, 2, 3, 5}, {2, 3, 4, 5}) == [1, 4]
    assert find_difference_in_sets_v2({1, 6, 7}, {2, 3, 6}) == [1, 2, 3, 7]
    assert find_difference_in_sets_v2({9, 10}, {11, 12}) == [9, 10, 11, 12]
    assert find_difference_in_sets_v2({7, 8, 9}, {8, 10, 11}) == [7, 9, 10, 11]


# 396. Тесты для функции find_divisible_by_4_in_both_sets_2
def test_find_divisible_by_4_in_both_sets_2():
    assert find_divisible_by_4_in_both_sets_2({4, 8, 12}, {8, 12, 16}) == [8, 12]
    assert find_divisible_by_4_in_both_sets_2({16, 32, 48}, {32, 48, 64}) == [32, 48]
    assert find_divisible_by_4_in_both_sets_2({4, 8, 12}, {4, 8, 12}) == [4, 8, 12]
    assert find_divisible_by_4_in_both_sets_2({2, 6, 10}, {3, 6, 9}) == None
    assert find_divisible_by_4_in_both_sets_2(set(), {4, 8, 12}) == None
    assert find_divisible_by_4_in_both_sets_2({4, 8, 12}, set()) == None
    assert find_divisible_by_4_in_both_sets_2({8, 12, 24}, {12, 24, 36}) == [12, 24]
    assert find_divisible_by_4_in_both_sets_2({16, 32, 64}, {8, 16, 32}) == [16, 32]
    assert find_divisible_by_4_in_both_sets_2({1, 2, 4}, {2, 4, 8}) == [4]


# 397. Тесты для функции find_unique_not_divisible_by_3
def test_find_unique_not_divisible_by_3():
    assert find_unique_not_divisible_by_3({1, 2, 3, 4}, {4, 5, 6, 7}) == [1, 2, 5, 7]
    assert find_unique_not_divisible_by_3({9, 18, 27}, {3, 6, 9}) == None
    assert find_unique_not_divisible_by_3({7, 10, 14}, {1, 7, 10}) == [1, 14]
    assert find_unique_not_divisible_by_3(set(), {3, 6, 9}) == None
    assert find_unique_not_divisible_by_3({3, 6, 9}, set()) == None
    assert find_unique_not_divisible_by_3({1, 4, 7}, {2, 5, 8}) == [1, 2, 4, 5, 7, 8]
    assert find_unique_not_divisible_by_3({10, 20, 30}, {30, 40, 50}) == [10, 20, 40, 50]
    assert find_unique_not_divisible_by_3({2, 3, 4}, {5, 6, 7}) == [2, 4, 5, 7]
    assert find_unique_not_divisible_by_3({15, 21, 27}, {3, 9, 21}) == None


# 398. Тесты для функции find_divisible_by_5_in_both_sets
def test_find_divisible_by_5_in_both_sets():
    assert find_divisible_by_5_in_both_sets({5, 10, 15}, {10, 15, 20}) == [10, 15]
    assert find_divisible_by_5_in_both_sets({25, 30, 35}, {35, 40, 45}) == [35]
    assert find_divisible_by_5_in_both_sets({50, 55}, {55, 60}) == [55]
    assert find_divisible_by_5_in_both_sets({1, 2, 3}, {4, 5, 6}) == None
    assert find_divisible_by_5_in_both_sets(set(), {5, 10, 15}) == None
    assert find_divisible_by_5_in_both_sets({5, 10, 15}, set()) == None
    assert find_divisible_by_5_in_both_sets({20, 25, 30}, {25, 35, 40}) == [25]
    assert find_divisible_by_5_in_both_sets({10, 20, 30}, {10, 40, 50}) == [10]
    assert find_divisible_by_5_in_both_sets({15, 45}, {5, 15, 25}) == [15]


# 399. Тесты для функции find_in_both_sets_not_divisible_by_2
def test_find_in_both_sets_not_divisible_by_2():
    assert find_in_both_sets_not_divisible_by_2({1, 3, 5}, {3, 5, 7}) == [3, 5]
    assert find_in_both_sets_not_divisible_by_2({11, 13, 15}, {13, 15, 17}) == [13, 15]
    assert find_in_both_sets_not_divisible_by_2({19, 21, 23}, {21, 23, 25}) == [21, 23]
    assert find_in_both_sets_not_divisible_by_2({2, 4, 6}, {8, 10, 12}) == None
    assert find_in_both_sets_not_divisible_by_2(set(), {1, 3, 5}) == None
    assert find_in_both_sets_not_divisible_by_2({1, 3, 5}, set()) == None
    assert find_in_both_sets_not_divisible_by_2({7, 9, 11}, {11, 13, 15}) == [11]
    assert find_in_both_sets_not_divisible_by_2({5, 7, 9}, {7, 9, 11}) == [7, 9]
    assert find_in_both_sets_not_divisible_by_2({3, 6, 9}, {3, 9, 12}) == [3, 9]


# 400. Тесты для функции find_difference_between_sets
def test_find_difference_between_sets():
    assert find_difference_between_sets({1, 2, 3}, {2, 3, 4}) == [1]
    assert find_difference_between_sets({5, 6, 7}, {6, 8, 9}) == [5, 7]
    assert find_difference_between_sets({1, 2, 3}, {1, 2, 3}) == None
    assert find_difference_between_sets(set(), {1, 2, 3}) == None
    assert find_difference_between_sets({1, 2, 3}, set()) == [1, 2, 3]
    assert find_difference_between_sets({7, 8, 9}, {8, 9, 10}) == [7]
    assert find_difference_between_sets({3, 6, 9}, {6, 9, 12}) == [3]
    assert find_difference_between_sets({15, 18, 21}, {18, 21, 24}) == [15]
    assert find_difference_between_sets({2, 4, 6}, {4, 6, 8}) == [2]
