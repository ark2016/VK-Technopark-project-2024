import pytest
from functions.file_581_600 import *


# 581. Тесты для функции `recursive_min`:
def test_recursive_min():
    assert recursive_min([5]) == 5
    assert recursive_min([3, 1, 4, 1, 5, 9]) == 1
    assert recursive_min([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert recursive_min([0, -1, -2, -3, -4]) == -4
    assert recursive_min([-3, -1, -4, -2, -5]) == -5
    assert recursive_min([1, 2, 3, 4, 5]) == 1
    assert recursive_min([100, 99, 98, 97]) == 97
    assert recursive_min([10, 20, 30, 40]) == 10
    assert recursive_min([42, 23, 34, 45, 56]) == 23


# 582. Тесты для функции `reverse_string_2`:
def test_reverse_string_2():
    assert reverse_string_2('') == ''
    assert reverse_string_2('hello') == 'olleh'
    assert reverse_string_2('python') == 'nohtyp'
    assert reverse_string_2('a') == 'a'
    assert reverse_string_2('racecar') == 'racecar'
    assert reverse_string_2('level') == 'level'
    assert reverse_string_2('12345') == '54321'
    assert reverse_string_2('abcdefg') == 'gfedcba'
    assert reverse_string_2('!@#$%^&*()') == ')(*&^%$#@!'


# 583. Тесты для функции `is_palindrome_4`:
def test_is_palindrome_4():
    assert is_palindrome_4('') == True
    assert is_palindrome_4('a') == True
    assert is_palindrome_4('racecar') == True
    assert is_palindrome_4('level') == True
    assert is_palindrome_4('hello') == False
    assert is_palindrome_4('world') == False
    assert is_palindrome_4('madam') == True
    assert is_palindrome_4('noon') == True
    assert is_palindrome_4('palindrome') == False


# 584. Тесты для функции `gsd_2`:
def test_gsd_2():
    assert gsd_2(54, 24) == 6
    assert gsd_2(48, 18) == 6
    assert gsd_2(101, 10) == 1
    assert gsd_2(0, 10) == 10
    assert gsd_2(10, 0) == 10
    assert gsd_2(10, 5) == 5
    assert gsd_2(7, 3) == 1
    assert gsd_2(50, 100) == 50
    assert gsd_2(37, 600) == 1


# 585. Тесты для функции `count_occurrences_3`:
def test_count_occurrences_3():
    assert count_occurrences_3([1, 2, 3, 4, 1, 2, 1], 1) == 3
    assert count_occurrences_3([1, 2, 3, 4, 5], 6) == 0
    assert count_occurrences_3([1, 1, 1, 1], 1) == 4
    assert count_occurrences_3([], 1) == 0
    assert count_occurrences_3([2, 3, 4, 5], 1) == 0
    assert count_occurrences_3([5, 5, 5, 5, 5], 5) == 5
    assert count_occurrences_3([0, 0, 0, 0], 0) == 4
    assert count_occurrences_3([-1, -1, -1], -1) == 3
    assert count_occurrences_3([1, 2, 3], 2) == 1


# 586. Тесты для функции `is_prime_4`:
def test_is_prime_4():
    assert is_prime_4(2) == True
    assert is_prime_4(3) == True
    assert is_prime_4(4) == False
    assert is_prime_4(17) == True
    assert is_prime_4(20) == False
    assert is_prime_4(1) == False
    assert is_prime_4(0) == False
    assert is_prime_4(-5) == False
    assert is_prime_4(23) == True


# 587. Тесты для функции `find_max_in_tree`:
def test_find_max_in_tree():
    tree1 = {'value': 5, 'left': {'value': 3}, 'right': {'value': 7}}
    tree2 = {'value': 10, 'left': None, 'right': {'value': 20}}
    tree3 = {'value': -1, 'left': {'value': -3}, 'right': {'value': -2}}
    assert find_max_in_tree(tree1) == 7
    assert find_max_in_tree(tree2) == 20
    assert find_max_in_tree(tree3) == -1
    assert find_max_in_tree({'value': 42}) == 42
    assert find_max_in_tree({'value': -100, 'left': None, 'right': None}) == -100
    assert find_max_in_tree(None) == float('-inf')
    assert find_max_in_tree({'value': 0, 'left': {'value': -5}, 'right': {'value': 5}}) == 5
    assert find_max_in_tree({'value': 6, 'left': {'value': 6}, 'right': {'value': 6}}) == 6
    assert find_max_in_tree({'value': -50, 'left': {'value': -60}, 'right': {'value': -70}}) == -50


# 588. Тесты для функции `is_even_2`:
def test_is_even_2():
    assert is_even_2(0) == True
    assert is_even_2(1) == False
    assert is_even_2(2) == True
    assert is_even_2(3) == False
    assert is_even_2(4) == True
    assert is_even_2(5) == False
    assert is_even_2(-2) == True
    assert is_even_2(-3) == False
    assert is_even_2(100) == True


# 589. Тесты для функции `sum_less_than_x`:
def test_sum_less_than_x():
    assert sum_less_than_x([1, 2, 3, 4, 5], 3) == 3
    assert sum_less_than_x([10, 20, 30, 40, 50], 25) == 30
    assert sum_less_than_x([5, 5, 5, 5, 5], 10) == 25
    assert sum_less_than_x([], 5) == 0
    assert sum_less_than_x([1, 2, 3, 4, 5], 0) == 0
    assert sum_less_than_x([-1, -2, -3, 4, 5], 0) == -6
    assert sum_less_than_x([100, 200, 300], 150) == 100
    assert sum_less_than_x([1, 1, 1, 1, 1], 2) == 5
    assert sum_less_than_x([6, 7, 8, 9, 10], 5) == 0


# 590. Тесты для функции `factorial_tail`:
def test_factorial_tail():
    assert factorial_tail(5) == 120
    assert factorial_tail(0) == 1
    assert factorial_tail(1) == 1
    assert factorial_tail(3) == 6
    assert factorial_tail(4) == 24
    assert factorial_tail(6) == 720
    assert factorial_tail(2) == 2
    assert factorial_tail(7) == 5040
    assert factorial_tail(8) == 40320


# 591. Тесты для функции `sum_with_step`:
def test_sum_with_step():
    assert sum_with_step(10) == 30
    assert sum_with_step(1) == 1
    assert sum_with_step(0) == 0
    assert sum_with_step(2) == 2
    assert sum_with_step(3) == 4
    assert sum_with_step(4) == 6
    assert sum_with_step(5) == 9
    assert sum_with_step(6) == 12
    assert sum_with_step(7) == 16


# 592. Тесты для функции `fibonacci_up_to_n`:
def test_fibonacci_up_to_n():
    assert fibonacci_up_to_n(0) == [0]
    assert fibonacci_up_to_n(1) == [0, 1, 1]
    assert fibonacci_up_to_n(2) == [0, 1, 1, 2]
    assert fibonacci_up_to_n(5) == [0, 1, 1, 2, 3, 5]
    assert fibonacci_up_to_n(10) == [0, 1, 1, 2, 3, 5, 8]
    assert fibonacci_up_to_n(15) == [0, 1, 1, 2, 3, 5, 8, 13]
    assert fibonacci_up_to_n(20) == [0, 1, 1, 2, 3, 5, 8, 13]
    assert fibonacci_up_to_n(25) == [0, 1, 1, 2, 3, 5, 8, 13, 21]
    assert fibonacci_up_to_n(30) == [0, 1, 1, 2, 3, 5, 8, 13, 21]


# 593. Тесты для функции `find_divisible`:
def test_find_divisible():
    assert find_divisible([1, 2, 3, 4, 5], 2) == [2, 4]
    assert find_divisible([10, 20, 30, 40, 50], 10) == [10, 20, 30, 40, 50]
    assert find_divisible([5, 7, 11], 2) == []
    assert find_divisible([], 5) == []
    assert find_divisible([1, 2, 3, 4, 5], 3) == [3]
    assert find_divisible([9, 12, 15, 18, 21], 3) == [9, 12, 15, 18, 21]
    assert find_divisible([100, 200, 300], 100) == [100, 200, 300]
    assert find_divisible([1, 1, 1, 1], 1) == [1, 1, 1, 1]
    assert find_divisible([6, 7, 8, 9, 10], 2) == [6, 8, 10]


# 594. Тесты для функции `count_even`:
def test_count_even():
    assert count_even([1, 2, 3, 4, 5]) == 2
    assert count_even([10, 20, 30, 40, 50]) == 5
    assert count_even([5, 7, 11]) == 0
    assert count_even([5]) == 0
    assert count_even([1, 3, 5, 7, 9]) == 0
    assert count_even([2, 4, 6, 8, 10]) == 5
    assert count_even([100, 200, 300]) == 3
    assert count_even([0, 0, 0, 0]) == 4
    assert count_even([-2, -4, -6]) == 3


# 595. Тесты для функции `count_negatives`:
def test_count_negatives():
    assert count_negatives([-1, -2, -3, 4, 5]) == 3
    assert count_negatives([-10, -20, -30, -40, -50]) == 5
    assert count_negatives([5, 7, 11]) == 0
    assert count_negatives([]) == 0
    assert count_negatives([1, 2, 3, 4, 5]) == 0
    assert count_negatives([-1, -2, -3, -4, -5]) == 5
    assert count_negatives([-100, -200, -300]) == 3
    assert count_negatives([0, 0, 0, 0]) == 0
    assert count_negatives([-2, -4, 6, 8, 10]) == 2


# 596. Тесты для функции `greater_than_average_3`:
def test_greater_than_average_3():
    assert greater_than_average_3([1, 2, 3, 4, 5]) == [4, 5]
    assert greater_than_average_3([10, 20, 30, 40, 50]) == [40, 50]
    assert greater_than_average_3([5, 7, 11, 13, 15]) == [11, 13, 15]
    assert greater_than_average_3([]) == []
    assert greater_than_average_3([1, 2, 3, 4]) == [3, 4]
    assert greater_than_average_3([10, 20, 30]) == [30]
    assert greater_than_average_3([0, 1, 2, 3]) == [2, 3]
    assert greater_than_average_3([-1, -2, -3, 0]) == [-1, 0]
    assert greater_than_average_3([6, 7, 8, 9, 10]) == [9, 10]


# 597. Тесты для функции `sum_greater_than_x`:
def test_sum_greater_than_x():
    assert sum_greater_than_x([1, 2, 3, 4, 5], 3) == 9
    assert sum_greater_than_x([10, 20, 30, 40, 50], 25) == 120
    assert sum_greater_than_x([5, 5, 5, 5, 5], 10) == 0
    assert sum_greater_than_x([], 5) == 0
    assert sum_greater_than_x([1, 2, 3, 4, 5], 5) == 0
    assert sum_greater_than_x([-1, -2, -3, 4, 5], 0) == 9
    assert sum_greater_than_x([100, 200, 300], 150) == 500
    assert sum_greater_than_x([1, 1, 1, 1, 1], 2) == 0
    assert sum_greater_than_x([6, 7, 8, 9, 10], 5) == 40


# 598. Тесты для функции `string_length`:
def test_string_length():
    assert string_length("") == 0
    assert string_length("hello") == 5
    assert string_length("a") == 1
    assert string_length("Python") == 6
    assert string_length("length") == 6
    assert string_length("test") == 4
    assert string_length("pytest") == 6
    assert string_length("recursion") == 9
    assert string_length("1234567890") == 10


# 599. Тесты для функции `count_evens_in_range`:
def test_count_evens_in_range():
    assert count_evens_in_range(0) == 0
    assert count_evens_in_range(1) == 0
    assert count_evens_in_range(2) == 1
    assert count_evens_in_range(3) == 1
    assert count_evens_in_range(4) == 2
    assert count_evens_in_range(5) == 2
    assert count_evens_in_range(6) == 3
    assert count_evens_in_range(10) == 5
    assert count_evens_in_range(15) == 7


# 600. Тесты для функции `sum_in_range`:
def test_sum_in_range():
    assert sum_in_range([1, 2, 3, 4, 5], 2, 4) == 9
    assert sum_in_range([10, 20, 30, 40, 50], 15, 35) == 50
    assert sum_in_range([5, 5, 5, 5, 5], 5, 5) == 25
    assert sum_in_range([], 5, 10) == 0
    assert sum_in_range([1, 2, 3, 4, 5], 0, 2) == 3
    assert sum_in_range([1, 2, 3, 4, 5], 4, 6) == 9
    assert sum_in_range([1, 2, 3, 4, 5], 10, 20) == 0
    assert sum_in_range([1, 5, 9, 13, 17], 5, 15) == 27
    assert sum_in_range([-1, -2, -3, 4, 5], -3, 3) == -6
