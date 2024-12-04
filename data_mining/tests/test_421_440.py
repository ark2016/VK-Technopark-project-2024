import pytest
from functions.file_421_440 import *


# 421. Тесты для функции `pop_elements_greater_than_x`:
def test_pop_elements_greater_than_x():
    assert pop_elements_greater_than_x([1, 3, 5, 7, 9], 4) == [9, 7, 5]
    assert pop_elements_greater_than_x([2, 4, 6, 8], 10) == None
    assert pop_elements_greater_than_x([10, 20, 30], 15) == [30, 20]
    assert pop_elements_greater_than_x([], 5) == None
    assert pop_elements_greater_than_x([-5, -2, -1, 0], -3) == [0, -1, -2]
    assert pop_elements_greater_than_x([5, 5, 5, 5, 5], 5) == None
    assert pop_elements_greater_than_x([1, 2, 3, 4, 5], 0) == [5, 4, 3, 2, 1]
    assert pop_elements_greater_than_x([1, 2, 3, 4, 5], 5) == None
    assert pop_elements_greater_than_x([100], 10) == [100]


# 422. Тесты для функции `find_even_in_stack`:
def test_find_even_in_stack():
    assert find_even_in_stack([1, 2, 3, 4, 5, 6]) == [6, 4, 2]
    assert find_even_in_stack([1, 3, 5, 7]) == None
    assert find_even_in_stack([0, 2, 4, 6, 8]) == [8, 6, 4, 2, 0]
    assert find_even_in_stack([-2, -4, -6, -8]) == [-8, -6, -4, -2]
    assert find_even_in_stack([1]) == None
    assert find_even_in_stack([2]) == [2]
    assert find_even_in_stack([]) == None
    assert find_even_in_stack([1, 3, 5, 7, 10]) == [10]
    assert find_even_in_stack([2, 2, 2, 2]) == [2, 2, 2, 2]


# 423. Тесты для функции `remove_divisible_by_5_from_stack`:
def test_remove_divisible_by_5_from_stack():
    assert remove_divisible_by_5_from_stack([1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [1]
    assert remove_divisible_by_5_from_stack([5, 10, 15, 20, 25]) == None
    assert remove_divisible_by_5_from_stack([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert remove_divisible_by_5_from_stack([0, 5, 10]) == None
    assert remove_divisible_by_5_from_stack([1, 2, 3, 6, 7, 11]) == [11, 7, 6, 3, 2, 1]
    assert remove_divisible_by_5_from_stack([]) == None
    assert remove_divisible_by_5_from_stack([1, 2, 3, 4, 6]) == [6, 4, 3, 2, 1]
    assert remove_divisible_by_5_from_stack([25]) == None
    assert remove_divisible_by_5_from_stack([1, 10, 100]) == [1]


# 424. Тесты для функции `remove_max_from_stack`:
def test_remove_max_from_stack():
    assert remove_max_from_stack([1, 2, 3, 4, 5]) == 5
    assert remove_max_from_stack([5, 4, 3, 2, 1]) == 5
    assert remove_max_from_stack([1]) == 1
    assert remove_max_from_stack([-5, -10, -1, -3]) == -1
    assert remove_max_from_stack([100, 200, 300, 400]) == 400
    assert remove_max_from_stack([0]) == 0
    assert remove_max_from_stack([3, 3, 3, 3]) == 3
    assert remove_max_from_stack([10, 20, 30, 40, 50]) == 50
    assert remove_max_from_stack([]) == None


# 425. Тесты для функции `pop_elements_not_divisible_by_3`:
def test_pop_elements_not_divisible_by_3():
    assert pop_elements_not_divisible_by_3([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [8, 7, 5, 4, 2, 1]
    assert pop_elements_not_divisible_by_3([3, 6, 9]) == None
    assert pop_elements_not_divisible_by_3([1, 4, 7, 10]) == [10, 7, 4, 1]
    assert pop_elements_not_divisible_by_3([3, 3, 3, 3]) == None
    assert pop_elements_not_divisible_by_3([10, 11, 12, 13, 14, 15]) == [14, 13, 11, 10]
    assert pop_elements_not_divisible_by_3([3]) == None
    assert pop_elements_not_divisible_by_3([1]) == [1]
    assert pop_elements_not_divisible_by_3([]) == None
    assert pop_elements_not_divisible_by_3([9, 18, 27, 36, 45]) == None


# 426. Тесты для функции `pop_until_sum_exceeds`:
def test_pop_until_sum_exceeds():
    assert pop_until_sum_exceeds([1, 2, 3, 4, 5], 7) == [5, 4]
    assert pop_until_sum_exceeds([5, 5, 5, 5, 5], 15) == [5, 5, 5, 5]
    assert pop_until_sum_exceeds([10, 20, 30], 25) == [30]
    assert pop_until_sum_exceeds([], 5) == None
    assert pop_until_sum_exceeds([1, 1, 1, 1, 1], 0) == [1]
    assert pop_until_sum_exceeds([3, 6, 9], 15) == [9, 6, 3]
    assert pop_until_sum_exceeds([10, 10, 10], 5) == [10]
    assert pop_until_sum_exceeds([5], 10) == [5]
    assert pop_until_sum_exceeds([3, 3, 3], 7) == [3, 3, 3]


# 427. Тесты для функции `pop_elements_less_than_average`:
def test_pop_elements_less_than_average():
    assert pop_elements_less_than_average([1, 2, 3, 4, 5]) == [2, 1]
    assert pop_elements_less_than_average([5, 5, 5, 5]) == None
    assert pop_elements_less_than_average([1, 3, 5, 7]) == [3, 1]
    assert pop_elements_less_than_average([10, 20, 30, 40, 50]) == [20, 10]
    assert pop_elements_less_than_average([]) == None
    assert pop_elements_less_than_average([1]) == None
    assert pop_elements_less_than_average([2, 4, 6, 8]) == [4, 2]
    assert pop_elements_less_than_average([-10, -20, -30]) == [-30]
    assert pop_elements_less_than_average([1, 2, 3, 4, 5, 5, 5, 5]) == [3, 2, 1]


# 428. Тесты для функции `pop_unique_elements`:
def test_pop_unique_elements():
    assert pop_unique_elements([1, 1, 2, 2, 3]) == [3]
    assert pop_unique_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert pop_unique_elements([1, 1, 2, 2, 3, 3, 4, 4]) == None
    assert pop_unique_elements([5]) == [5]
    assert pop_unique_elements([]) == None
    assert pop_unique_elements([2, 2, 2, 2]) == None
    assert pop_unique_elements([3, 1, 4, 1, 5, 9]) == [9, 5, 4, 3]
    assert pop_unique_elements([1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8]) == [8, 6, 3, 1]
    assert pop_unique_elements([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]) == [6]


# 429. Тесты для функции `pop_elements_divisible_by_5`:
def test_pop_elements_divisible_by_5():
    assert pop_elements_divisible_by_5([5, 10, 15, 20, 25]) == [25, 20, 15, 10, 5]
    assert pop_elements_divisible_by_5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 5]
    assert pop_elements_divisible_by_5([1, 2, 3, 4, 6, 7, 8, 9]) == None
    assert pop_elements_divisible_by_5([0, 5, 10, 15]) == [15, 10, 5, 0]
    assert pop_elements_divisible_by_5([1, 2, 3, 4]) == None
    assert pop_elements_divisible_by_5([5]) == [5]
    assert pop_elements_divisible_by_5([25, 30, 35, 40, 45]) == [45, 40, 35, 30, 25]
    assert pop_elements_divisible_by_5([10, 20, 30, 40, 50]) == [50, 40, 30, 20, 10]
    assert pop_elements_divisible_by_5([12, 17, 22, 27]) == None


# 430. Тесты для функции `pop_elements_greater_than_x_reverse`:
def test_pop_elements_greater_than_x_reverse():
    assert pop_elements_greater_than_x_reverse([1, 2, 3, 4, 5], 3) == [4, 5]
    assert pop_elements_greater_than_x_reverse([10, 20, 30, 40, 50], 25) == [30, 40, 50]
    assert pop_elements_greater_than_x_reverse([5, 5, 5, 5], 5) == None
    assert pop_elements_greater_than_x_reverse([1, 2, 3, 4, 5, 6], 3) == [4, 5, 6]
    assert pop_elements_greater_than_x_reverse([1], 0) == [1]
    assert pop_elements_greater_than_x_reverse([2], 1) == [2]
    assert pop_elements_greater_than_x_reverse([7, 8, 9, 10], 8) == [9, 10]
    assert pop_elements_greater_than_x_reverse([11, 22, 33, 44], 15) == [22, 33, 44]
    assert pop_elements_greater_than_x_reverse([1, 2, 3, 4, 5, 6, 7, 8, 9], 20) == None


# 431. Тесты для функции `remove_less_than_x`:
def test_remove_less_than_x():
    assert remove_less_than_x([1, 3, 5, 7, 9], 4) == [9, 7, 5]
    assert remove_less_than_x([2, 4, 6, 8], 10) == None
    assert remove_less_than_x([10, 20, 30], 15) == [30, 20]
    assert remove_less_than_x([], 5) == None
    assert remove_less_than_x([-5, -2, -1, 0], -3) == [0, -1, -2]
    assert remove_less_than_x([5, 5, 5, 5, 5], 5) == [5, 5, 5, 5, 5]
    assert remove_less_than_x([1, 2, 3, 4, 5], 0) == [5, 4, 3, 2, 1]
    assert remove_less_than_x([1, 2, 3, 4, 5], 5) == [5]
    assert remove_less_than_x([100], 10) == [100]


# 432. Тесты для функции `find_min_in_stack`:
def test_find_min_in_stack():
    assert find_min_in_stack([1, 2, 3, 4, 5]) == 1
    assert find_min_in_stack([5, 4, 3, 2, 1]) == 1
    assert find_min_in_stack([1]) == 1
    assert find_min_in_stack([-5, -10, -1, -3]) == -10
    assert find_min_in_stack([100, 200, 300, 400]) == 100
    assert find_min_in_stack([0]) == 0
    assert find_min_in_stack([3, 3, 3, 3]) == 3
    assert find_min_in_stack([10, 20, 30, 40, 50]) == 10
    assert find_min_in_stack([]) == None


# 433. Тесты для функции `pop_until_divisible_by_6`:
def test_pop_until_divisible_by_6():
    assert pop_until_divisible_by_6([1, 2, 3, 4, 5, 6]) == [6]
    assert pop_until_divisible_by_6([1, 2, 3, 4, 5, 12]) == [12]
    assert pop_until_divisible_by_6([6, 7, 8, 9]) == [9, 8, 7, 6]
    assert pop_until_divisible_by_6([12, 14, 15, 18]) == [18]
    assert pop_until_divisible_by_6([7, 5, 11]) == [11, 5, 7]
    assert pop_until_divisible_by_6([]) == None
    assert pop_until_divisible_by_6([12, 24, 36, 48]) == [48]
    assert pop_until_divisible_by_6([1, 3, 5, 7]) == [7, 5, 3, 1]
    assert pop_until_divisible_by_6([2, 8, 10, 11]) == [11, 10, 8, 2]


# 434. Тесты для функции `find_even_divisible_by_4`:
def test_find_even_divisible_by_4():
    assert find_even_divisible_by_4([1, 2, 3, 4, 5, 6, 8, 12, 16]) == [16, 12, 8, 4]
    assert find_even_divisible_by_4([5, 7, 11, 13]) == None
    assert find_even_divisible_by_4([4, 8, 12]) == [12, 8, 4]
    assert find_even_divisible_by_4([0, 4, 8, 16, 32]) == [32, 16, 8, 4, 0]
    assert find_even_divisible_by_4([1, 3, 5, 7]) == None
    assert find_even_divisible_by_4([4]) == [4]
    assert find_even_divisible_by_4([]) == None
    assert find_even_divisible_by_4([4, 4, 4, 4]) == [4, 4, 4, 4]
    assert find_even_divisible_by_4([6, 10, 14, 18]) == None


# 435. Тесты для функции `pop_odd_elements`:
def test_pop_odd_elements():
    assert pop_odd_elements([1, 2, 3, 4, 5, 6]) == [5, 3, 1]
    assert pop_odd_elements([1, 3, 5, 7]) == [7, 5, 3, 1]
    assert pop_odd_elements([2, 4, 6, 8]) == None
    assert pop_odd_elements([0, 1, 2, 3]) == [3, 1]
    assert pop_odd_elements([]) == None
    assert pop_odd_elements([1]) == [1]
    assert pop_odd_elements([2]) == None
    assert pop_odd_elements([5, 5, 5]) == [5, 5, 5]
    assert pop_odd_elements([1, 2, 3, 4, 5]) == [5, 3, 1]


# 436. Тесты для функции `remove_less_than_x_v2`:
def test_remove_less_than_x_v2():
    assert remove_less_than_x_v2([1, 3, 5, 7, 9], 4) == [3, 1]
    assert remove_less_than_x_v2([2, 4, 6, 8], 10) == [8, 6, 4, 2]
    assert remove_less_than_x_v2([10, 20, 30], 15) == [10]
    assert remove_less_than_x_v2([], 5) == None
    assert remove_less_than_x_v2([-5, -2, -1, 0], -3) == [-5]
    assert remove_less_than_x_v2([5, 5, 5, 5, 5], 5) == None
    assert remove_less_than_x_v2([1, 2, 3, 4, 5], 0) == None
    assert remove_less_than_x_v2([1, 2, 3, 4, 5], 5) == [4, 3, 2, 1]
    assert remove_less_than_x_v2([100], 10) == None


# 437. Тесты для функции `find_square_numbers_in_stack`:
def test_find_square_numbers_in_stack():
    assert find_square_numbers_in_stack([1, 2, 3, 4, 9, 16]) == [16, 9, 4, 1]
    assert find_square_numbers_in_stack([1, 3, 5, 7]) == [1]
    assert find_square_numbers_in_stack([0, 4, 9, 16, 25]) == [25, 16, 9, 4, 0]
    assert find_square_numbers_in_stack([10, 20, 30, 40]) == None
    assert find_square_numbers_in_stack([1]) == [1]
    assert find_square_numbers_in_stack([2]) == None
    assert find_square_numbers_in_stack([4, 4, 4]) == [4, 4, 4]
    assert find_square_numbers_in_stack([9, 16, 25]) == [25, 16, 9]
    assert find_square_numbers_in_stack([2, 3, 5, 7]) == None


# 438. Тесты для функции `find_max_in_stack`:
def test_find_max_in_stack():
    assert find_max_in_stack([1, 2, 3, 4, 5]) == 5
    assert find_max_in_stack([5, 4, 3, 2, 1]) == 5
    assert find_max_in_stack([1]) == 1
    assert find_max_in_stack([-5, -10, -1, -3]) == -1
    assert find_max_in_stack([100, 200, 300, 400]) == 400
    assert find_max_in_stack([0]) == 0
    assert find_max_in_stack([3, 3, 3, 3]) == 3
    assert find_max_in_stack([10, 20, 30, 40, 50]) == 50
    assert find_max_in_stack([]) == None


# 439. Тесты для функции `pop_elements_divisible_by_7`:
def test_pop_elements_divisible_by_7():
    assert pop_elements_divisible_by_7([7, 14, 21, 28, 35]) == [35, 28, 21, 14, 7]
    assert pop_elements_divisible_by_7([1, 2, 3, 4, 5, 6, 7]) == [7]
    assert pop_elements_divisible_by_7([1, 2, 3, 4, 5, 6, 8, 9]) == None
    assert pop_elements_divisible_by_7([0, 7, 14, 21]) == [21, 14, 7, 0]
    assert pop_elements_divisible_by_7([1, 3, 5, 11]) == None
    assert pop_elements_divisible_by_7([7]) == [7]
    assert pop_elements_divisible_by_7([14, 28, 42, 56]) == [56, 42, 28, 14]
    assert pop_elements_divisible_by_7([21, 35, 49, 63, 77]) == [77, 63, 49, 35, 21]
    assert pop_elements_divisible_by_7([5, 10, 20, 25]) == None


# 440. Тесты для функции `find_greater_than_x_divisible_by_2`:
def test_find_greater_than_x_divisible_by_2():
    assert find_greater_than_x_divisible_by_2([1, 2, 3, 4, 5], 3) == [4]
    assert find_greater_than_x_divisible_by_2([10, 20, 30, 40, 50], 25) == [50, 40, 30]
    assert find_greater_than_x_divisible_by_2([5, 5, 5, 5], 5) == None
    assert find_greater_than_x_divisible_by_2([1, 2, 3, 4, 5, 6], 3) == [6, 4]
    assert find_greater_than_x_divisible_by_2([1], 0) == None
    assert find_greater_than_x_divisible_by_2([2], 1) == [2]
    assert find_greater_than_x_divisible_by_2([7, 8, 9, 10], 8) == [10]
    assert find_greater_than_x_divisible_by_2([11, 22, 33, 44], 15) == [44, 22]
    assert find_greater_than_x_divisible_by_2([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == [8, 6]
