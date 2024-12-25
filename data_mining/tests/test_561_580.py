import pytest
from functions.file_561_580 import *


# 561. Тесты для функции `less_than_value`
def test_less_than_value():
    assert less_than_value([1, 2, 3, 4], 3) == [1, 2]
    assert less_than_value([5, 6, 7], 10) == [5, 6, 7]
    assert less_than_value([], 5) == None
    assert less_than_value([1, 2, "three"], 3) == [1, 2]
    assert less_than_value([1, 2], "three") == None
    assert less_than_value([1, 2, 3.5], 3.5) == [1, 2]


# 562. Тесты для функции `sum_of_squares_2`
def test_sum_of_squares_2():
    assert sum_of_squares_2([1, 2, 3]) == 14
    assert sum_of_squares_2([]) == None
    assert sum_of_squares_2([2, -2, 2.5]) == 14.25
    assert sum_of_squares_2(["one", 2, 3]) == 13
    assert sum_of_squares_2([0, -2, 5]) == 29
    assert sum_of_squares_2([3.5]) == 12.25


# 563. Тесты для функции `positive_max_min_difference`
def test_positive_max_min_difference():
    assert positive_max_min_difference([1, 2, 3]) == 2
    assert positive_max_min_difference([-1, -2, -3]) == None
    assert positive_max_min_difference([1, -1, 2, 3]) == 2
    assert positive_max_min_difference([0, 2, 5, 3]) == 3
    assert positive_max_min_difference([]) == None
    assert positive_max_min_difference(["one", 2, 3]) == 1


# 564. Тесты для функции `negative_max_min_difference`
def test_negative_max_min_difference():
    assert negative_max_min_difference([-1, -2, -3]) == 2
    assert negative_max_min_difference([1, 2, 3]) == None
    assert negative_max_min_difference([-1, 1, -2, -3]) == 2
    assert negative_max_min_difference([0, -2, -5, -3]) == 3
    assert negative_max_min_difference([]) == None
    assert negative_max_min_difference(["minus one", -2, -3]) == 1


# 565. Тесты для функции `sum_of_divisible_by_x`
def test_sum_of_divisible_by_x():
    assert sum_of_divisible_by_x([1, 2, 3, 4], 2) == 10
    assert sum_of_divisible_by_x([1, 3, 5, 7], 2) == 16
    assert sum_of_divisible_by_x([], 2) == None
    assert sum_of_divisible_by_x([1, 2, "three"], 2) == 3
    assert sum_of_divisible_by_x([1, 2, 3], "two") == None
    assert sum_of_divisible_by_x([4, 8, 12], 4) == 24


# 566. Тесты для функции `cubes`
def test_cubes():
    assert cubes([1, 8, 27]) == [1, 8, 27]
    assert cubes([]) == None
    assert cubes([1, 2, 3, 8]) == [1, 8]
    assert cubes(["one", 8, 27]) == [8, 27]
    assert cubes([8, 8]) == [8, 8]
    assert cubes([27.0]) == [27.0]


# 567. Тесты для функции `sum_of_two_squares_3`
def test_sum_of_two_squares_3():
    assert sum_of_two_squares_3([5, 4, 10, 13]) == [5, 5, 4, 4, 10, 10, 13, 13]
    assert sum_of_two_squares_3([]) == None
    assert sum_of_two_squares_3([8, 1, 2]) == [8, 1, 1, 2]
    assert sum_of_two_squares_3([1, 2, "three"]) == [1, 1, 2]
    assert sum_of_two_squares_3([5, 25]) == [5, 5, 25, 25, 25, 25]
    assert sum_of_two_squares_3([0, 3, 9]) == [0, 9, 9]


# 568. Тесты для функции `is_power_of_two`
def test_is_power_of_two():
    assert is_power_of_two(1) == True
    assert is_power_of_two(2) == True
    assert is_power_of_two(3) == False
    assert is_power_of_two(16) == True
    assert is_power_of_two(-2) == False
    assert is_power_of_two(4) == True


# 569. Тесты для функции `integers_in_float_list`
def test_integers_in_float_list():
    assert integers_in_float_list([1.0, 2.0, 3.5, 4]) == [1.0, 2.0, 4]
    assert integers_in_float_list([]) == None
    assert integers_in_float_list([1.1, 2.2, 3.3]) == []
    assert integers_in_float_list([1, 2, "three"]) == [1, 2]
    assert integers_in_float_list([0.0, 2.0, 5]) == [0.0, 2.0, 5]
    assert integers_in_float_list([4, 4.0]) == [4, 4.0]


# 570. Тесты для функции `sum_of_products_of_primes`
def test_sum_of_products_of_primes():
    assert sum_of_products_of_primes([6, 10, 15, 21]) == 52
    assert sum_of_products_of_primes([]) == None
    assert sum_of_products_of_primes([1, 2, 3]) == None
    assert sum_of_products_of_primes(["six", 10, 15]) == 25
    assert sum_of_products_of_primes([6, 10]) == 16
    assert sum_of_products_of_primes([25.0, 49]) == 74
    assert sum_of_products_of_primes([1025, 34, 234]) == 34


# 571. Тесты для функции `difference_of_two_squares`
def test_difference_of_two_squares():
    assert difference_of_two_squares([3, 4, 5, 7]) == [3, 4, 5, 7]
    assert difference_of_two_squares([]) == None
    assert difference_of_two_squares([1, 2, 4]) == [1, 4]
    assert difference_of_two_squares([4, 8, 12, 16, 25, 0]) == [4, 8, 12, 16, 25]
    assert difference_of_two_squares(["two", 4, 5]) == [4, 5]
    assert difference_of_two_squares([10]) == None


# 572. Тесты для функции `cubes_of_numbers`
def test_cubes_of_numbers():
    assert cubes_of_numbers([1, 8, 27]) == [1, 8, 27]
    assert cubes_of_numbers([]) == None
    assert cubes_of_numbers([1, 2, 3, 8]) == [1, 8]
    assert cubes_of_numbers(["one", 8, 27]) == [8, 27]
    assert cubes_of_numbers([5, 8]) == [8]
    assert cubes_of_numbers([27.0]) == [27.0]


# 573. Тесты для функции `average_of_squares`
def test_average_of_squares():
    assert average_of_squares([1, 2, 3]) == 4.666666666666667
    assert average_of_squares([]) == None
    assert average_of_squares([2, 2, 2.5]) == 4.75
    assert average_of_squares(["one", 2, 3]) == 4.333333333333333
    assert average_of_squares([0, -2, 5]) == 9.666666666666666
    assert average_of_squares([3.5]) == 12.25


# 574. Тесты для функции `factorial_2`
def test_factorial_2():
    assert factorial_2(5) == 120
    assert factorial_2(0) == 1
    assert factorial_2(2) == 2
    assert factorial_2(4) == 24


# 575. Тесты для функции `sum_to_n`
def test_sum_to_n():
    assert sum_to_n(5) == 15
    assert sum_to_n(0) == 0
    assert sum_to_n(1) == 1
    assert sum_to_n(-1) == 0
    assert sum_to_n(10) == 55
    assert sum_to_n(2) == 3


# 576. Тесты для функции `fibonacci_2`
def test_fibonacci_2():
    assert fibonacci_2(0) == 0
    assert fibonacci_2(1) == 1
    assert fibonacci_2(2) == 1
    assert fibonacci_2(3) == 2
    assert fibonacci_2(4) == 3
    assert fibonacci_2(5) == 5


# 577. Тесты для функции `power_2`
def test_power_2():
    assert power_2(2, 3) == 8
    assert power_2(5, 0) == 1
    assert power_2(2, -1) == 1
    assert power_2(3, 2) == 9
    assert power_2(4, 3) == 64
    assert power_2(-2, 3) == -8


# 578. Тесты для функции `recursive_sum`
def test_recursive_sum():
    assert recursive_sum([1, 2, 3]) == 6
    assert recursive_sum([]) == 0
    assert recursive_sum([2, -2, 2.5]) == 2.5
    assert recursive_sum([0, -2, 5]) == 3
    assert recursive_sum([3.5]) == 3.5


# 579. Тесты для функции `recursive_product`
def test_recursive_product():
    assert recursive_product([1, 2, 3]) == 6
    assert recursive_product([]) == 1
    assert recursive_product([2, -2, 2.5]) == -10
    assert recursive_product(["one", 2, 3]) == 'oneoneoneoneoneone'
    assert recursive_product([0, -2, 5]) == 0
    assert recursive_product([3.5]) == 3.5


# 580. Тесты для функции `recursive_max`
def test_recursive_max():
    assert recursive_max([1, 2, 3]) == 3
    assert recursive_max([3, 2, 1]) == 3
    assert recursive_max([-1, -2, -3]) == -1
    assert recursive_max([2, 0, 4, 3]) == 4
    assert recursive_max([5]) == 5
    assert recursive_max([3.5, 2.5, 1.5]) == 3.5
