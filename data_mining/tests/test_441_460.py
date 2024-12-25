import pytest
from functions.file_441_460 import *


# 441. Тесты для функции `remove_not_divisible_by_4`:
def test_remove_not_divisible_by_4():
    assert remove_not_divisible_by_4([8, 15, 3, 4]) == [3, 15]
    assert remove_not_divisible_by_4([16, 2, 12]) == [2]
    assert remove_not_divisible_by_4([4, 8, 16, 32]) == None
    assert remove_not_divisible_by_4([]) == None
    assert remove_not_divisible_by_4([5, 7, 11]) == [11, 7, 5]
    assert remove_not_divisible_by_4([4, 15, 20, 8, 3, 12]) == [3, 15]
    assert remove_not_divisible_by_4([-4, -8, 0]) == None
    assert remove_not_divisible_by_4([9, 17, 21]) == [21, 17, 9]
    assert remove_not_divisible_by_4([-1, -2, -5, -6]) == [-6, -5, -2, -1]


# 442. Тесты для функции `pop_elements_divisible_by_10`:
def test_pop_elements_divisible_by_10():
    assert pop_elements_divisible_by_10([20, 5, 30, 7, 10]) == [10, 30, 20]
    assert pop_elements_divisible_by_10([4, 2, 12]) == None
    assert pop_elements_divisible_by_10([40, 50, 60]) == [60, 50, 40]
    assert pop_elements_divisible_by_10([]) == None
    assert pop_elements_divisible_by_10([10, 20, 30, 5, 1]) == [30, 20, 10]
    assert pop_elements_divisible_by_10([0, 100, 200]) == [200, 100, 0]
    assert pop_elements_divisible_by_10([5, 7, 15]) == None
    assert pop_elements_divisible_by_10([-10, -20, -5]) == [-20, -10]
    assert pop_elements_divisible_by_10([9, 19, 29]) == None


# 443. Тесты для функции `find_divisible_by_3_and_5`:
def test_find_divisible_by_3_and_5():
    assert find_divisible_by_3_and_5([30, 45, 60, 10, 15]) == [15, 60, 45, 30]
    assert find_divisible_by_3_and_5([3, 5, 9, 10]) == None
    assert find_divisible_by_3_and_5([75, 90, 105]) == [105, 90, 75]
    assert find_divisible_by_3_and_5([]) == None
    assert find_divisible_by_3_and_5([15, 30, 45, 5, 10]) == [45, 30, 15]
    assert find_divisible_by_3_and_5([0, 60, 120]) == [120, 60, 0]
    assert find_divisible_by_3_and_5([4, 2, 6]) == None
    assert find_divisible_by_3_and_5([-15, -30, -5]) == [-30, -15]
    assert find_divisible_by_3_and_5([9, 21, 27]) == None


# 444. Тесты для функции `remove_greater_than_x`:
def test_remove_greater_than_x():
    assert remove_greater_than_x([8, 12, 15, 4], 10) == [4, 8]
    assert remove_greater_than_x([16, 2, 5, 12], 7) == [5, 2]
    assert remove_greater_than_x([4, 8, 16, 3], 8) == [3, 8, 4]
    assert remove_greater_than_x([], 10) == None
    assert remove_greater_than_x([5, 7, 11], 15) == [11, 7, 5]
    assert remove_greater_than_x([4, 15, 20, 8], 10) == [8, 4]
    assert remove_greater_than_x([-4, -8, 0], -1) == [-8, -4]
    assert remove_greater_than_x([9, 17, 21], 10) == [9]
    assert remove_greater_than_x([-1, -2, -5, -6], -3) == [-6, -5]


# 445. Тесты для функции `pop_elements_greater_than_x_even`:
def test_pop_elements_greater_than_x_even():
    assert pop_elements_greater_than_x_even([8, 10, 12, 4], 9) == [12, 10]
    assert pop_elements_greater_than_x_even([16, 3, 5, 14], 12) == [14, 16]
    assert pop_elements_greater_than_x_even([4, 8, 16, 3], 6) == [16, 8]
    assert pop_elements_greater_than_x_even([], 5) == None
    assert pop_elements_greater_than_x_even([5, 7, 11], 10) == None
    assert pop_elements_greater_than_x_even([4, 15, 20, 8], 15) == [20]
    assert pop_elements_greater_than_x_even([-4, -8, 0], -3) == [0]
    assert pop_elements_greater_than_x_even([9, 17, 21], 15) == None
    assert pop_elements_greater_than_x_even([-1, -2, -5, -6], -4) == [-2]


# 446. Тесты для функции `process_queue_until_sum_exceeds`:
def test_process_queue_until_sum_exceeds():
    assert process_queue_until_sum_exceeds([3, 5, 2, 7], 8) == [3, 5, 2]
    assert process_queue_until_sum_exceeds([16, 3, 5, 12], 14) == [16]
    assert process_queue_until_sum_exceeds([4, 8, 1, 3], 7) == [4, 8]
    assert process_queue_until_sum_exceeds([], 5) == None
    assert process_queue_until_sum_exceeds([5, 7, 1], 10) == [5, 7]
    assert process_queue_until_sum_exceeds([4, 2, 5, 8], 6) == [4, 2, 5]
    assert process_queue_until_sum_exceeds([-4, -8, 10], -5) == [-4]
    assert process_queue_until_sum_exceeds([9, 1, 2], 10) == [9, 1, 2]
    assert process_queue_until_sum_exceeds([-1, -2, -3, -4], -1) == [-1, -2, -3, -4]


# 447. Тесты для функции `process_queue_less_than_average`:
def test_process_queue_less_than_average():
    assert process_queue_less_than_average([3, 5, 2, 7]) == [3, 2]
    assert process_queue_less_than_average([16, 3, 5, 12]) == [3, 5]
    assert process_queue_less_than_average([4, 8, 1, 3]) == [1, 3]
    assert process_queue_less_than_average([]) == None
    assert process_queue_less_than_average([77, 77, 77]) == None
    assert process_queue_less_than_average([4, 2, 5, 8]) == [4, 2]
    assert process_queue_less_than_average([-4, -8, 0]) == [-8]
    assert process_queue_less_than_average([9, 1, 2]) == [1, 2]
    assert process_queue_less_than_average([-1, -2, -3, -4]) == [-3, -4]


# 448. Тесты для функции `process_queue_unique_elements`:
def test_process_queue_unique_elements():
    assert process_queue_unique_elements([3, 5, 2, 7, 5, 3]) == [2, 7]
    assert process_queue_unique_elements([16, 3, 5, 12, 16]) == [3, 5, 12]
    assert process_queue_unique_elements([4, 8, 1, 4, 3, 8]) == [1, 3]
    assert process_queue_unique_elements([]) == None
    assert process_queue_unique_elements([5, 7, 1, 7, 5]) == [1]
    assert process_queue_unique_elements([4, 8, 4, 8, 1]) == [1]
    assert process_queue_unique_elements([10, 20, 30, 40, 20]) == [10, 30, 40]
    assert process_queue_unique_elements([5, 10, 5, 15, 20]) == [10, 15, 20]
    assert process_queue_unique_elements([9, 19, 9, 21, 21]) == [19]


# 449. Тесты для функции `process_queue_divisible_by_5`:
def test_process_queue_divisible_by_5():
    assert process_queue_divisible_by_5([3, 5, 10, 7, 25]) == [5, 10, 25]
    assert process_queue_divisible_by_5([1, 2, 3, 4]) == None
    assert process_queue_divisible_by_5([50, 5, 10, 20]) == [50, 5, 10, 20]
    assert process_queue_divisible_by_5([]) == None
    assert process_queue_divisible_by_5([5, 10, 15]) == [5, 10, 15]
    assert process_queue_divisible_by_5([0, 100, 200]) == [0, 100, 200]
    assert process_queue_divisible_by_5([1, 3, 7]) == None
    assert process_queue_divisible_by_5([-5, -10, -15]) == [-5, -10, -15]
    assert process_queue_divisible_by_5([25, 30, 35, 40]) == [25, 30, 35, 40]


# 450. Тесты для функции `process_queue_greater_than_x`:
def test_process_queue_greater_than_x():
    assert process_queue_greater_than_x([8, 12, 15, 4], 10) == [12, 15]
    assert process_queue_greater_than_x([16, 2, 5, 12], 7) == [16, 12]
    assert process_queue_greater_than_x([4, 8, 16, 3], 8) == [16]
    assert process_queue_greater_than_x([], 10) == None
    assert process_queue_greater_than_x([5, 7, 11], 5) == [7, 11]
    assert process_queue_greater_than_x([4, 15, 20, 8], 10) == [15, 20]
    assert process_queue_greater_than_x([-4, -8, 0], -1) == [0]
    assert process_queue_greater_than_x([9, 17, 21], 10) == [17, 21]
    assert process_queue_greater_than_x([-1, -2, -5, -6], -3) == [-1, -2]


# 451. Тесты для функции `process_queue_divisible_by_2_not_4`:
def test_process_queue_divisible_by_2_not_4():
    assert process_queue_divisible_by_2_not_4([2, 4, 6, 8, 10, 12]) == [2, 6, 10]
    assert process_queue_divisible_by_2_not_4([4, 8, 12, 16]) == None
    assert process_queue_divisible_by_2_not_4([2, 6, 10]) == [2, 6, 10]
    assert process_queue_divisible_by_2_not_4([]) == None
    assert process_queue_divisible_by_2_not_4([1, 3, 5, 7]) == None
    assert process_queue_divisible_by_2_not_4([14, 18, 20, 24]) == [14, 18]
    assert process_queue_divisible_by_2_not_4([-2, -4, -6, -8]) == [-2, -6]
    assert process_queue_divisible_by_2_not_4([9, 13, 17]) == None
    assert process_queue_divisible_by_2_not_4([3, 6, 9, 12]) == [6]


# 452. Тесты для функции `process_queue_divisible_by_7`:
def test_process_queue_divisible_by_7():
    assert process_queue_divisible_by_7([7, 14, 21, 5, 10]) == [7, 14, 21]
    assert process_queue_divisible_by_7([1, 2, 3, 4]) == None
    assert process_queue_divisible_by_7([28, 35, 42, 49]) == [28, 35, 42, 49]
    assert process_queue_divisible_by_7([]) == None
    assert process_queue_divisible_by_7([7, 14, 21]) == [7, 14, 21]
    assert process_queue_divisible_by_7([0, 70, 140]) == [0, 70, 140]
    assert process_queue_divisible_by_7([1, 3, 7]) == [7]
    assert process_queue_divisible_by_7([-7, -14, -21]) == [-7, -14, -21]
    assert process_queue_divisible_by_7([35, 70, 105]) == [35, 70, 105]


# 453. Тесты для функции `process_queue_odd_elements`:
def test_process_queue_odd_elements():
    assert process_queue_odd_elements([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert process_queue_odd_elements([2, 4, 6, 8]) == None
    assert process_queue_odd_elements([1, 3, 5, 7]) == [1, 3, 5, 7]
    assert process_queue_odd_elements([]) == None
    assert process_queue_odd_elements([1, 3, 5]) == [1, 3, 5]
    assert process_queue_odd_elements([2, 4, 6]) == None
    assert process_queue_odd_elements([7, 14, 21]) == [7, 21]
    assert process_queue_odd_elements([-1, -3, -5]) == [-1, -3, -5]
    assert process_queue_odd_elements([5, 10, 15, 20]) == [5, 15]


# 454. Тесты для функции `process_queue_square_numbers`:
def test_process_queue_square_numbers():
    assert process_queue_square_numbers([1, 2, 3, 4, 5, 9, 16]) == [1, 4, 9, 16]
    assert process_queue_square_numbers([2, 3, 5, 7]) == None
    assert process_queue_square_numbers([4, 9, 16, 25, 36]) == [4, 9, 16, 25, 36]
    assert process_queue_square_numbers([]) == None
    assert process_queue_square_numbers([1, 4, 9]) == [1, 4, 9]
    assert process_queue_square_numbers([2, 3, 6]) == None
    assert process_queue_square_numbers([7, 14, 21]) == None
    assert process_queue_square_numbers([1, 4, 9]) == [1, 4, 9]
    assert process_queue_square_numbers([25, 49, 81]) == [25, 49, 81]


# 455. Тесты для функции `process_queue_divisible_by_3_or_5`:
def test_process_queue_divisible_by_3_or_5():
    assert process_queue_divisible_by_3_or_5([1, 2, 3, 4, 5, 6, 7, 9]) == [3, 5, 6, 9]
    assert process_queue_divisible_by_3_or_5([1, 2, 4, 7, 8]) == None
    assert process_queue_divisible_by_3_or_5([15, 30, 45, 60]) == [15, 30, 45, 60]
    assert process_queue_divisible_by_3_or_5([]) == None
    assert process_queue_divisible_by_3_or_5([3, 6, 9]) == [3, 6, 9]
    assert process_queue_divisible_by_3_or_5([5, 10, 15]) == [5, 10, 15]
    assert process_queue_divisible_by_3_or_5([7, 14, 21]) == [21]
    assert process_queue_divisible_by_3_or_5([-3, -6, -9]) == [-3, -6, -9]
    assert process_queue_divisible_by_3_or_5([12, 18, 24]) == [12, 18, 24]


# 456. Тесты для функции `process_queue_divisible_by_3_not_6`:
def test_process_queue_divisible_by_3_not_6():
    assert process_queue_divisible_by_3_not_6([3, 6, 9, 12, 15]) == [3, 9, 15]
    assert process_queue_divisible_by_3_not_6([6, 12, 18]) == None
    assert process_queue_divisible_by_3_not_6([3, 9, 15, 21]) == [3, 9, 15, 21]
    assert process_queue_divisible_by_3_not_6([]) == None
    assert process_queue_divisible_by_3_not_6([3, 6, 9]) == [3, 9]
    assert process_queue_divisible_by_3_not_6([12, 15, 18]) == [15]
    assert process_queue_divisible_by_3_not_6([4, 8, 14]) == None
    assert process_queue_divisible_by_3_not_6([3, 27, 9]) == [3, 27, 9]
    assert process_queue_divisible_by_3_not_6([12, 24, 36]) == None


# 457. Тесты для функции `process_queue_remove_less_than_x`:
def test_process_queue_remove_less_than_x():
    assert process_queue_remove_less_than_x([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    assert process_queue_remove_less_than_x([1, 2, 3, 4, 5], 1) == [1, 2, 3, 4, 5]
    assert process_queue_remove_less_than_x([1, 2, 3, 4, 5], 6) == None
    assert process_queue_remove_less_than_x([], 3) == None
    assert process_queue_remove_less_than_x([1, 2, 3, 4, 5], 5) == [5]
    assert process_queue_remove_less_than_x([5, 10, 15], 10) == [10, 15]
    assert process_queue_remove_less_than_x([7, 14, 21], 15) == [21]
    assert process_queue_remove_less_than_x([-1, -3, 5], 0) == [5]
    assert process_queue_remove_less_than_x([3, 6, 9], 7) == [9]


# 458. Тесты для функции `process_queue_less_than_x`:
def test_process_queue_less_than_x():
    assert process_queue_less_than_x([1, 2, 3, 4, 5], 3) == [1, 2]
    assert process_queue_less_than_x([1, 2, 3, 4, 5], 1) == None
    assert process_queue_less_than_x([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5]
    assert process_queue_less_than_x([], 3) == None
    assert process_queue_less_than_x([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4]
    assert process_queue_less_than_x([5, 10, 15], 10) == [5]
    assert process_queue_less_than_x([7, 14, 21], 15) == [7, 14]
    assert process_queue_less_than_x([-1, -3, 5], 0) == [-1, -3]
    assert process_queue_less_than_x([3, 6, 9], 7) == [3, 6]


# 459. Тесты для функции `process_queue_min_element`:
def test_process_queue_min_element():
    assert process_queue_min_element([1, 2, 3, 4, 5]) == 1
    assert process_queue_min_element([5, 4, 3, 2, 1]) == 1
    assert process_queue_min_element([-1, -2, -3, -4, -5]) == -5
    assert process_queue_min_element([0]) == 0
    assert process_queue_min_element([]) == None
    assert process_queue_min_element([10, 20, 5, 30]) == 5
    assert process_queue_min_element([7, 14, 21, 2]) == 2
    assert process_queue_min_element([3, 3, 3]) == 3
    assert process_queue_min_element([-1, 1, -2, 2]) == -2


# 460. Тесты для функции `process_queue_remove_greater_than_x`:
def test_process_queue_remove_greater_than_x():
    assert process_queue_remove_greater_than_x([1, 2, 3, 4, 5], 3) == [1, 2, 3]
    assert process_queue_remove_greater_than_x([5, 10, 15], 10) == [5, 10]
    assert process_queue_remove_greater_than_x([7, 14, 21], 15) == [7, 14]
    assert process_queue_remove_greater_than_x([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
    assert process_queue_remove_greater_than_x([], 3) == None
    assert process_queue_remove_greater_than_x([-1, -3, 5], 0) == [-1, -3]
    assert process_queue_remove_greater_than_x([3, 6, 9], 7) == [3, 6]
    assert process_queue_remove_greater_than_x([10, 20, 30], 25) == [10, 20]
    assert process_queue_remove_greater_than_x([8, 12, 15, 4], 10) == [8, 4]
