import pytest
from functions.file_461_480 import *


# 461. Тесты для функции process_queue_max_element
def test_process_queue_max_element():
    assert process_queue_max_element([1, 2, 3, 4, 5]) == 5
    assert process_queue_max_element([10, 9, 8, 7, 6]) == 10
    assert process_queue_max_element([-1, -2, -3, -4, -5]) == -1
    assert process_queue_max_element([]) == None
    assert process_queue_max_element([1, 1, 1, 1, 1]) == 1
    assert process_queue_max_element([4, 5, 6, 7, 4]) == 7


# 462. Тесты для функции process_queue_remove_divisible_by_4
def test_process_queue_remove_divisible_by_4():
    assert process_queue_remove_divisible_by_4([4, 8, 12, 16]) == None
    assert process_queue_remove_divisible_by_4([1, 2, 3, 5, 7]) == [1, 2, 3, 5, 7]
    assert process_queue_remove_divisible_by_4([4, 5, 6, 8, 9]) == [5, 6, 9]
    assert process_queue_remove_divisible_by_4([]) == None
    assert process_queue_remove_divisible_by_4([0, 4, 8, 4, 16]) == None
    assert process_queue_remove_divisible_by_4([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]


# 463. Тесты для функции process_queue_greater_than_x_and_divisible_by_2
def test_process_queue_greater_than_x_and_divisible_by_2():
    assert process_queue_greater_than_x_and_divisible_by_2([1, 2, 3, 4, 5], 2) == [4]
    assert process_queue_greater_than_x_and_divisible_by_2([10, 9, 8, 7, 6], 5) == [10, 8, 6]
    assert process_queue_greater_than_x_and_divisible_by_2([1, 2, 3, 4, 5], 6) == None
    assert process_queue_greater_than_x_and_divisible_by_2([], 1) == None
    assert process_queue_greater_than_x_and_divisible_by_2([1, 2, 3, 4, 5], 0) == [2, 4]
    assert process_queue_greater_than_x_and_divisible_by_2([1, 3, 5, 7, 9], 4) == None


# 464. Тесты для функции process_queue_greater_than_x_and_divisible_by_3
def test_process_queue_greater_than_x_and_divisible_by_3():
    assert process_queue_greater_than_x_and_divisible_by_3([1, 2, 3, 4, 5, 6], 2) == [3, 6]
    assert process_queue_greater_than_x_and_divisible_by_3([9, 8, 7, 6, 5], 5) == [9, 6]
    assert process_queue_greater_than_x_and_divisible_by_3([1, 2, 3, 4, 5], 3) == None
    assert process_queue_greater_than_x_and_divisible_by_3([], 1) == None
    assert process_queue_greater_than_x_and_divisible_by_3([1, 3, 6, 9], 0) == [3, 6, 9]
    assert process_queue_greater_than_x_and_divisible_by_3([2, 4, 8], 4) == None


# 465. Тесты для функции process_queue_less_than_x_not_divisible_by_5
def test_process_queue_less_than_x_not_divisible_by_5():
    assert process_queue_less_than_x_not_divisible_by_5([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4]
    assert process_queue_less_than_x_not_divisible_by_5([10, 9, 8, 7, 6], 8) == [7, 6]
    assert process_queue_less_than_x_not_divisible_by_5([15, 25, 35, 45], 50) == None
    assert process_queue_less_than_x_not_divisible_by_5([], 10) == None
    assert process_queue_less_than_x_not_divisible_by_5([0, 1, 2, 3], 4) == [1, 2, 3]
    assert process_queue_less_than_x_not_divisible_by_5([5, 10, 15], 20) == None


# 466. Тесты для функции process_queue_even_and_divisible_by_4
def test_process_queue_even_and_divisible_by_4():
    assert process_queue_even_and_divisible_by_4([4, 8, 12, 16, 20]) == [4, 8, 12, 16, 20]
    assert process_queue_even_and_divisible_by_4([1, 2, 3, 4, 5]) == [4]
    assert process_queue_even_and_divisible_by_4([5, 6, 7, 8, 9]) == [8]
    assert process_queue_even_and_divisible_by_4([1, 3, 5, 7]) == None
    assert process_queue_even_and_divisible_by_4([0, 4, 8, 12]) == [0, 4, 8, 12]
    assert process_queue_even_and_divisible_by_4([2, 6, 10, 14]) == None


# 467. Тесты для функции process_queue_not_divisible_by_3_and_5
def test_process_queue_not_divisible_by_3_and_5():
    assert process_queue_not_divisible_by_3_and_5([1, 2, 3, 4, 5]) == [1, 2, 4]
    assert process_queue_not_divisible_by_3_and_5([9, 8, 7, 6, 5]) == [8, 7]
    assert process_queue_not_divisible_by_3_and_5([15, 25, 35, 45]) == None
    assert process_queue_not_divisible_by_3_and_5([4, 8, 14, 22]) == [4, 8, 14, 22]
    assert process_queue_not_divisible_by_3_and_5([3, 5, 9, 15]) == None


# 468. Тесты для функции find_elements_greater_than_x
def test_find_elements_greater_than_x():
    assert find_elements_greater_than_x((1, 2, 3, 4, 5), 3) == (4, 5)
    assert find_elements_greater_than_x((10, 9, 8, 7, 6), 8) == (10, 9)
    assert find_elements_greater_than_x((-1, -2, -3, -4, -5), -3) == (-1, -2)
    assert find_elements_greater_than_x((), 1) == None
    assert find_elements_greater_than_x((1, 2, 3, 4, 5), 5) == None
    assert find_elements_greater_than_x((4, 5, 6, 7, 4), 6) == (7,)


# 469. Тесты для функции find_even_elements_in_tuple
def test_find_even_elements_in_tuple():
    assert find_even_elements_in_tuple((1, 2, 3, 4, 5)) == (2, 4)
    assert find_even_elements_in_tuple((10, 9, 8, 7, 6)) == (10, 8, 6)
    assert find_even_elements_in_tuple((-1, -2, -3, -4, -5)) == (-2, -4)
    assert find_even_elements_in_tuple((1, 3, 5)) == None
    assert find_even_elements_in_tuple((2, 4, 6, 8)) == (2, 4, 6, 8)
    assert find_even_elements_in_tuple(()) == None


# 470. Тесты для функции find_elements_less_than_average
def test_find_elements_less_than_average():
    assert find_elements_less_than_average((1, 2, 3, 4, 5)) == (1, 2)
    assert find_elements_less_than_average((10, 9, 8, 7, 6)) == (7, 6)
    assert find_elements_less_than_average((1, 1, 1, 1, 1)) == None
    assert find_elements_less_than_average((2, 4, 6, 8, 10)) == (2, 4)
    assert find_elements_less_than_average(()) == None
    assert find_elements_less_than_average((-1, -2, -3, -4, -5)) == (-4, -5)
    assert find_elements_less_than_average((5, 10, 15, 20, 25)) == (5, 10)


# 471. Тесты для функции find_elements_greater_than_x_divisible_by_5
def test_find_elements_greater_than_x_divisible_by_5():
    assert find_elements_greater_than_x_divisible_by_5((1, 5, 10, 15, 20), 10) == (15, 20)
    assert find_elements_greater_than_x_divisible_by_5((25, 30, 35, 40, 45), 20) == (25, 30, 35, 40, 45)
    assert find_elements_greater_than_x_divisible_by_5((5, 10, 15), 20) == None
    assert find_elements_greater_than_x_divisible_by_5((), 5) == None
    assert find_elements_greater_than_x_divisible_by_5((5, 10, 15, 20, 25), 0) == (5, 10, 15, 20, 25)
    assert find_elements_greater_than_x_divisible_by_5((1, 2, 3, 4), 3) == None


# 472. Тесты для функции find_unique_elements_in_tuple
def test_find_unique_elements_in_tuple():
    assert find_unique_elements_in_tuple((1, 2, 2, 3, 4, 4)) == (1, 3)
    assert find_unique_elements_in_tuple((5, 5, 5, 5, 5, 5)) == None
    assert find_unique_elements_in_tuple((1, 2, 3, 4, 5)) == (1, 2, 3, 4, 5)
    assert find_unique_elements_in_tuple(()) == None
    assert find_unique_elements_in_tuple((6, 7, 8, 9, 10, 10, 11)) == (6, 7, 8, 9, 11)
    assert find_unique_elements_in_tuple((2, 2, 2, 3, 3, 3, 4, 4)) == None


# 473. Тесты для функции find_divisible_by_3_and_4
def test_find_divisible_by_3_and_4():
    assert find_divisible_by_3_and_4((12, 24, 36, 48)) == (12, 24, 36, 48)
    assert find_divisible_by_3_and_4((6, 9, 12, 18, 24)) == (12, 24)
    assert find_divisible_by_3_and_4((3, 6, 9, 15)) == None
    assert find_divisible_by_3_and_4(()) == None
    assert find_divisible_by_3_and_4((3, 4, 5, 6, 7)) == None
    assert find_divisible_by_3_and_4((3, 12, 24, 36, 45)) == (12, 24, 36)


# 474. Тесты для функции find_odd_elements_in_tuple
def test_find_odd_elements_in_tuple():
    assert find_odd_elements_in_tuple((1, 2, 3, 4, 5)) == (1, 3, 5)
    assert find_odd_elements_in_tuple((10, 9, 8, 7, 6)) == (9, 7)
    assert find_odd_elements_in_tuple((-1, -2, -3, -4, -5)) == (-1, -3, -5)
    assert find_odd_elements_in_tuple((2, 4, 6)) == None
    assert find_odd_elements_in_tuple((1, 3, 5, 7)) == (1, 3, 5, 7)
    assert find_odd_elements_in_tuple(()) == None


# 475. Тесты для функции find_min_in_tuple
def test_find_min_in_tuple():
    assert find_min_in_tuple((1, 2, 3, 4, 5)) == 1
    assert find_min_in_tuple((10, 9, 8, 7, 6)) == 6
    assert find_min_in_tuple((-1, -2, -3, -4, -5)) == -5
    assert find_min_in_tuple(()) == None
    assert find_min_in_tuple((5, 5, 5, 5, 5)) == 5
    assert find_min_in_tuple((3, 4, 2, 1, 5)) == 1


# 476. Тесты для функции find_max_in_tuple
def test_find_max_in_tuple():
    assert find_max_in_tuple((1, 2, 3, 4, 5)) == 5
    assert find_max_in_tuple((10, 9, 8, 7, 6)) == 10
    assert find_max_in_tuple((-1, -2, -3, -4, -5)) == -1
    assert find_max_in_tuple(()) == None
    assert find_max_in_tuple((5, 5, 5, 5, 5)) == 5
    assert find_max_in_tuple((3, 4, 2, 1, 5)) == 5


# 477. Тесты для функции find_divisible_by_2_or_5
def test_find_divisible_by_2_or_5():
    assert find_divisible_by_2_or_5((1, 2, 3, 4, 5)) == (2, 4, 5)
    assert find_divisible_by_2_or_5((10, 9, 8, 7, 6)) == (10, 8, 6)
    assert find_divisible_by_2_or_5((1, 3, 7, 11, 13)) == None
    assert find_divisible_by_2_or_5(()) == None
    assert find_divisible_by_2_or_5((20, 25, 30, 35, 40)) == (20, 25, 30, 35, 40)
    assert find_divisible_by_2_or_5((1, 5, 10, 15, 20)) == (5, 10, 15, 20)


# 478. Тесты для функции find_divisible_by_6
def test_find_divisible_by_57():
    assert find_divisible_by_57((6, 12, 18, 24, 57)) == (57,)
    assert find_divisible_by_57((5, 10, 15, 20, 25)) == None
    assert find_divisible_by_57((1, 2, 3, 4, 5)) == None
    assert find_divisible_by_57(()) == None
    assert find_divisible_by_57((6, 114, 24)) == (114,)
    assert find_divisible_by_57((12, 228, 456, 60)) == (228, 456)


# 479. Тесты для функции find_square_numbers_in_tuple
def test_find_square_numbers_in_tuple():
    assert find_square_numbers_in_tuple((1, 2, 3, 4, 5)) == (1, 4)
    assert find_square_numbers_in_tuple((10, 9, 8, 7, 6)) == (9,)
    assert find_square_numbers_in_tuple((1, 2, 3, 4, 5)) == (1, 4)
    assert find_square_numbers_in_tuple((4, 9, 16, 25, 36)) == (4, 9, 16, 25, 36)
    assert find_square_numbers_in_tuple(()) == None
    assert find_square_numbers_in_tuple((1, 4, 9, 16, 25, 36, 49)) == (1, 4, 9, 16, 25, 36, 49)


# 480. Тесты для функции find_greater_than_x_not_divisible_by_3
def test_find_greater_than_x_not_divisible_by_3():
    assert find_greater_than_x_not_divisible_by_3((1, 2, 3, 4, 5), 2) == (4, 5)
    assert find_greater_than_x_not_divisible_by_3((10, 9, 8, 7, 6), 5) == (10, 8, 7)
    assert find_greater_than_x_not_divisible_by_3((1, 2, 3, 4, 5), 6) == None
    assert find_greater_than_x_not_divisible_by_3((), 1) == None
    assert find_greater_than_x_not_divisible_by_3((4, 5, 6, 7, 8, 9), 3) == (4, 5, 7, 8)
    assert find_greater_than_x_not_divisible_by_3((1, 1, 1, 1, 1), 1) == None
