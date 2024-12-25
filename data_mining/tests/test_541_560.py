import pytest
from functions.file_541_560 import *


# 541. Тесты для функции `max_float`:
def test_max_float():
    assert max_float([1.2, 3.4, 5.6]) == 5.6
    assert max_float([-1.1, -2.2, -3.3]) == -1.1
    assert max_float([]) == None
    assert max_float([1, 2, 3.3, 'a', 0]) == 3.3
    assert max_float([1.1, -2, 0]) == 1.1


# 542. Тесты для функции `min_float`:
def test_min_float():
    assert min_float([1.2, 3.4, 5.6]) == 1.2
    assert min_float([-1.1, -2.2, -3.3]) == -3.3
    assert min_float([]) == None
    assert min_float([1, 2, 3.3, 'a', 0]) == 0
    assert min_float([1.1, -2, 0]) == -2


# 543. Тесты для функции `is_positive_float`:
def test_is_positive_float():
    assert is_positive_float(5.5) == True
    assert is_positive_float(-3.2) == False
    assert is_positive_float(0) == False
    assert is_positive_float('a') == None
    assert is_positive_float(None) == None


# 544. Тесты для функции `difference_between_floats`:
def test_difference_between_floats():
    assert difference_between_floats(5.5, 3.2) == 2.3
    assert difference_between_floats(-3.2, 5.5) == 8.7
    assert difference_between_floats(0, 0) == 0
    assert difference_between_floats('a', 3.2) == None
    assert difference_between_floats(5.5, None) == None


# 545. Тесты для функции `product_of_floats`:
def test_product_of_floats():
    assert product_of_floats([1.2, 3.4, 5.6]) == pytest.approx(22.848)
    assert product_of_floats([-1.1, -2.2, -3.3]) == pytest.approx(-7.986)
    assert product_of_floats([]) == None
    assert product_of_floats([1, 2, 3, 'a', 0]) == None
    assert product_of_floats([1.1, -2, 3]) == pytest.approx(-6.6)


# 546. Тесты для функции `divide_floats`:
def test_divide_floats():
    assert divide_floats(6.6, 3.3) == 2.0
    assert divide_floats(-6.6, 3.3) == -2.0
    assert divide_floats(6.6, 0) == None
    assert divide_floats('a', 3.3) == None
    assert divide_floats(6.6, None) == None


# 547. Тесты для функции `square_root`:
def test_square_root():
    assert square_root(4) == 2.0
    assert square_root(9) == 3.0
    assert square_root(-4) == None
    assert square_root('a') == None
    assert square_root(None) == None


# 548. Тесты для функции `round_to_nearest_integer`:
def test_round_to_nearest_integer():
    assert round_to_nearest_integer(4.4) == 4
    assert round_to_nearest_integer(4.5) == 4
    assert round_to_nearest_integer(4.6) == 5
    assert round_to_nearest_integer(-4.5) == -4
    assert round_to_nearest_integer('a') == None


# 549. Тесты для функции `divisible_by_x`:
def test_divisible_by_x():
    assert divisible_by_x([10, 20, 30], 10) == [10, 20, 30]
    assert divisible_by_x([10, 21, 30], 10) == [10, 30]
    assert divisible_by_x([10, 21, 33], 0) == None
    assert divisible_by_x(['a', 21, 33], 7) == [21]
    assert divisible_by_x([], 2) == None


# 550. Тесты для функции `exponentiation_of_float`:
def test_exponentiation_of_float():
    assert exponentiation_of_float(2, 3) == 8
    assert exponentiation_of_float(-2, 3) == -8
    assert exponentiation_of_float(2, -3) == 0.125
    assert exponentiation_of_float('a', 3) == None
    assert exponentiation_of_float(2, 'b') == None


# 551. Тесты для функции `factorial_of_float`:
def test_factorial_of_float():
    assert factorial_of_float(5) == 120
    assert factorial_of_float(0) == 1
    assert factorial_of_float(-1) == None
    assert factorial_of_float(3) == 6
    assert factorial_of_float('a') == None


# 552. Тесты для функции `median_of_floats`:
def test_median_of_floats():
    assert median_of_floats([1, 2, 3]) == 2
    assert median_of_floats([1, 2, 3, 4]) == 2.5
    assert median_of_floats([]) == None
    assert median_of_floats([1, 'a', 3]) == 2
    assert median_of_floats([-1, -2, -3]) == -2
    assert median_of_floats(['a', 'b', 'c']) == None


# 553. Тесты для функции `prime_floats`:
def test_prime_floats():
    assert prime_floats([2, 3, 4, 5]) == [2, 3, 5]
    assert prime_floats([2.2, 3.3, 5.5]) == None
    assert prime_floats([]) == None
    assert prime_floats([-2, -3, -5]) == None
    assert prime_floats([11, 13, 15]) == [11, 13]


# 554. Тесты для функции `numbers_in_range`:
def test_numbers_in_range():
    assert numbers_in_range(1, 5) == [1, 2, 3, 4, 5]
    assert numbers_in_range(5, 5) == [5]
    assert numbers_in_range('a', 5) == None
    assert numbers_in_range(1, 'b') == None
    assert numbers_in_range(10, 1) == []


# 555. Тесты для функции `geometric_progression`:
def test_geometric_progression():
    assert geometric_progression(2, 3, 4) == [2, 6, 18, 54]
    assert geometric_progression(1, 2, 5) == [1, 2, 4, 8, 16]
    assert geometric_progression(1, 1, 5) == [1, 1, 1, 1, 1]
    assert geometric_progression(1, 2, 0) == None
    assert geometric_progression('a', 2, 5) == None


# 556. Тесты для функции `sum_of_geometric_progression`:
def test_sum_of_geometric_progression():
    assert sum_of_geometric_progression(2, 3, 4) == 80
    assert sum_of_geometric_progression(1, 2, 5) == 31
    assert sum_of_geometric_progression(1, 1, 5) == 5
    assert sum_of_geometric_progression(1, 2, 0) == None
    assert sum_of_geometric_progression('a', 2, 5) == None


# 557. Тесты для функции `square_of_float`:
def test_square_of_float():
    assert square_of_float(2) == 4
    assert square_of_float(-3) == 9
    assert square_of_float(0) == 0
    assert square_of_float('a') == None
    assert square_of_float(None) == None


# 558. Тесты для функции `sum_of_arithmetic_progression`:
def test_sum_of_arithmetic_progression():
    assert sum_of_arithmetic_progression(2, 3, 4) == 26
    assert sum_of_arithmetic_progression(1, 1, 5) == 15
    assert sum_of_arithmetic_progression(0, 0, 5) == 0
    assert sum_of_arithmetic_progression('a', 1, 5) == None
    assert sum_of_arithmetic_progression(1, 1, -5) == None


# 559. Тесты для функции `non_zero_floats`:
def test_non_zero_floats():
    assert non_zero_floats([1.2, 0, 3.4, 5.6]) == [1.2, 3.4, 5.6]
    assert non_zero_floats([-1.1, 0, -3.3]) == [-1.1, -3.3]
    assert non_zero_floats([]) == None
    assert non_zero_floats([0, 0, 0]) == []
    assert non_zero_floats([1.1, 'a', 3.3, 0]) == [1.1, 3.3]


# 560. Тесты для функции `squares_greater_than`:
def test_squares_greater_than():
    assert squares_greater_than([1, 2, 3], 4) == [3]
    assert squares_greater_than([-3, 1, 4], 9) == [4]
    assert squares_greater_than([], 4) == None
    assert squares_greater_than([3, 'a', 4], 9) == [4]
    assert squares_greater_than([4, 5, 6], 16) == [5, 6]
