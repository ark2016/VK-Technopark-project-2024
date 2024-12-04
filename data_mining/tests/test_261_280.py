import pytest
from functions.file_261_280 import *


# 261. Тесты для функции `find_divisible_by_7_and_8_not_56`:
def test_find_divisible_by_7_and_8_not_56():
    assert find_divisible_by_7_and_8_not_56([7, 8, 14, 16, 56, 112]) == [7, 8, 14, 16]
    assert find_divisible_by_7_and_8_not_56([1, 2, 3, 4, 5]) == None
    assert find_divisible_by_7_and_8_not_56([]) == None
    assert find_divisible_by_7_and_8_not_56([49, 64, 9, 21, 32]) == [49, 64, 21, 32]


# 262. Тесты для функции `find_odd_keys_in_dict`:
def test_find_odd_keys_in_dict():
    assert find_odd_keys_in_dict({1: 'a', 2: 'b', 3: 'c'}) == [1, 3]
    assert find_odd_keys_in_dict({4: 'd', 6: 'e'}) == None
    assert find_odd_keys_in_dict({}) == None
    assert find_odd_keys_in_dict({1: 'a', 5: 'b', 8: 'c'}) == [1, 5]


# 263. Тесты для функции `find_even_in_tuple_not_in_list`:
def test_find_even_in_tuple_not_in_list():
    assert find_even_in_tuple_not_in_list((2, 4, 6, 8), [3, 5, 7]) == [2, 4, 6, 8]
    assert find_even_in_tuple_not_in_list((2, 4, 6, 8), [2, 4, 6, 8]) == None
    assert find_even_in_tuple_not_in_list((), [1, 2, 3]) == None
    assert find_even_in_tuple_not_in_list((10, 12, 14), [1, 3, 7]) == [10, 12, 14]


# 264. Тесты для функции `find_divisors_of_100_not_prime`:
def test_find_divisors_of_100_not_prime():
    assert find_divisors_of_100_not_prime([1, 2, 4, 5, 10, 20, 25, 50]) == [1, 4, 10, 20, 25, 50]
    assert find_divisors_of_100_not_prime([2, 5, 7, 11]) == None
    assert find_divisors_of_100_not_prime([10, 20, 30]) == [10, 20]
    assert find_divisors_of_100_not_prime([100, 200]) == [100]


# 265. Тесты для функции `find_in_list_not_in_set`:
def test_find_in_list_not_in_set():
    assert find_in_list_not_in_set([1, 2, 3], {2}) == [1, 3]
    assert find_in_list_not_in_set([1, 2, 3], {1, 2, 3}) == None
    assert find_in_list_not_in_set([], {1, 2, 3}) == None
    assert find_in_list_not_in_set([4, 5, 6], {1, 2, 3}) == [4, 5, 6]


# 266. Тесты для функции `find_sum_of_two_lists`:
def test_find_sum_of_two_lists():
    assert find_sum_of_two_lists([1, 2], [3, 4]) == [4, 5, 5, 6]
    assert find_sum_of_two_lists([], [1, 2, 3]) == None
    assert find_sum_of_two_lists([1, 2], []) == None
    assert find_sum_of_two_lists([0, 0], [0, 0]) == [0, 0, 0, 0]


# 267. Тесты для функции `find_difference_of_two_lists`:
def test_find_difference_of_two_lists():
    assert find_difference_of_two_lists([5, 6], [2, 3]) == [3, 2, 4, 3]
    assert find_difference_of_two_lists([], [1, 2, 3]) == None
    assert find_difference_of_two_lists([1, 2], []) == None
    assert find_difference_of_two_lists([10, 20], [5, 15]) == [5, -5, 15, 5]


# 268. Тесты для функции `find_odd_in_tuple_not_in_list`:
def test_find_odd_in_tuple_not_in_list():
    assert find_odd_in_tuple_not_in_list((1, 3, 5, 7), [2, 4, 6]) == [1, 3, 5, 7]
    assert find_odd_in_tuple_not_in_list((1, 2, 3, 4), [1, 3]) == None
    assert find_odd_in_tuple_not_in_list((), [1, 2, 3]) == None
    assert find_odd_in_tuple_not_in_list((9, 11, 13), [2, 4, 6]) == [9, 11, 13]


# 269. Тесты для функции `find_divisible_by_5_and_6_not_12`:
def test_find_divisible_by_5_and_6_not_12():
    assert find_divisible_by_5_and_6_not_12([30, 60, 90]) == [30, 90]
    assert find_divisible_by_5_and_6_not_12([12, 24, 36]) == None
    assert find_divisible_by_5_and_6_not_12([]) == None
    assert find_divisible_by_5_and_6_not_12([15, 45, 75]) == None


# 270. Тесты для функции `find_odd_not_divisible_by_5_2`:
def test_find_odd_not_divisible_by_5_2():
    assert find_odd_not_divisible_by_5_2([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 7, 9]
    assert find_odd_not_divisible_by_5_2([10, 20, 30]) == None
    assert find_odd_not_divisible_by_5_2([15, 25, 35]) == None
    assert find_odd_not_divisible_by_5_2([2, 4, 6, 8, 12]) == None


# 271. Тесты для функции `find_even_in_list_and_tuple`:
def test_find_even_in_list_and_tuple():
    assert find_even_in_list_and_tuple([2, 4, 6], (4, 6, 8)) == [4, 6]
    assert find_even_in_list_and_tuple([1, 3, 5], (2, 4, 6)) == None
    assert find_even_in_list_and_tuple([], (2, 4, 6)) == None
    assert find_even_in_list_and_tuple([2, 4, 6], (1, 3, 5)) == None


# 272. Тесты для функции `find_product_of_two_numbers`:
def test_find_product_of_two_numbers():
    assert find_product_of_two_numbers([1, 2, 3]) == [1, 2, 3, 2, 4, 6, 3, 6, 9]
    assert find_product_of_two_numbers([0, 1, 2]) == [0, 0, 0, 0, 1, 2, 0, 2, 4]
    assert find_product_of_two_numbers([1]) == [1]
    assert find_product_of_two_numbers([]) == None


# 273. Тесты для функции `find_in_set_not_in_list_2`:
def test_find_in_set_not_in_list_2():
    assert find_in_set_not_in_list_2({1, 2, 3}, [2, 3, 4]) == [1]
    assert find_in_set_not_in_list_2({2, 3, 4}, [2, 3, 4]) == None
    assert find_in_set_not_in_list_2({1, 5, 7}, [2, 3, 4]) == [1, 5, 7]
    assert find_in_set_not_in_list_2(set(), [2, 3, 4]) == None


# 274. Тесты для функции `find_difference_between_lists`:
def test_find_difference_between_lists():
    assert find_difference_between_lists([5, 6], [2, 3]) == [3, 2, 4, 3]
    assert find_difference_between_lists([], [1, 2, 3]) == None
    assert find_difference_between_lists([1, 2], []) == None
    assert find_difference_between_lists([10, 20], [5, 15]) == [5, -5, 15, 5]


# 275. Тесты для функции `find_unique_in_one_list_not_both`:
def test_find_unique_in_one_list_not_both():
    assert find_unique_in_one_list_not_both([1, 2, 3], [3, 4, 5]) == [1, 2, 4, 5]
    assert find_unique_in_one_list_not_both([1, 2, 3], [1, 2, 3]) == None
    assert find_unique_in_one_list_not_both([], [3, 4, 5]) == [3, 4, 5]
    assert find_unique_in_one_list_not_both([1, 2, 3], []) == [1, 2, 3]


# 276. Тесты для функции `find_even_and_divisible_by_3`:
def test_find_even_and_divisible_by_3():
    assert find_even_and_divisible_by_3([6, 12, 18]) == [6, 12, 18]
    assert find_even_and_divisible_by_3([1, 2, 3]) == None
    assert find_even_and_divisible_by_3([]) == None
    assert find_even_and_divisible_by_3([5, 7, 10]) == None


# 277. Тесты для функции `find_squares_not_divisible_by_5`:
def test_find_squares_not_divisible_by_5():
    assert find_squares_not_divisible_by_5([1, 4, 9, 16, 25, 36]) == [1, 4, 9, 16, 36]
    assert find_squares_not_divisible_by_5([25, 50, 75]) == None
    assert find_squares_not_divisible_by_5([]) == None
    assert find_squares_not_divisible_by_5([100, 144, 169]) == [144, 169]


# 278. Тесты для функции `find_divisible_by_7_and_8_not_56_2`:
def test_find_divisible_by_7_and_8_not_56_2():
    assert find_divisible_by_7_and_8_not_56_2([7, 8, 14, 16, 56, 112]) == [56, 112]
    assert find_divisible_by_7_and_8_not_56_2([1, 2, 3, 4, 5]) == None
    assert find_divisible_by_7_and_8_not_56_2([]) == None
    assert find_divisible_by_7_and_8_not_56_2([56, 112, 21, 32]) == [56, 112]


# 279. Тесты для функции `find_in_list_and_tuple`:
def test_find_in_list_and_tuple():
    assert find_in_list_and_tuple([1, 2, 3], (3, 4, 5)) == [3]
    assert find_in_list_and_tuple([1, 2, 3], (1, 2, 3)) == [1, 2, 3]
    assert find_in_list_and_tuple([], (1, 2, 3)) == None
    assert find_in_list_and_tuple([1, 2, 3], ()) == None


# 280. Тесты для функции `find_sum_of_two_not_divisible_by_4`:
def test_find_sum_of_two_not_divisible_by_4():
    assert find_sum_of_two_not_divisible_by_4([1, 2, 3, 4]) == [3, 5, 5, 6, 7]
    assert find_sum_of_two_not_divisible_by_4([4, 8, 12]) == None
    assert find_sum_of_two_not_divisible_by_4([]) == None
    assert find_sum_of_two_not_divisible_by_4([3, 6, 9]) == [9, 15]
