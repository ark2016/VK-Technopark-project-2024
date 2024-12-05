import pytest
from functions.file_601_620 import *


# 601. Тесты для функции `product_less_than_x`:
def test_product_less_than_x():
    assert product_less_than_x([2, 3, 4], 3) == 2
    assert product_less_than_x([1, 2, 3, 4], 5) == 24
    assert product_less_than_x([], 5) == 1
    assert product_less_than_x([5, 6, 7], 5) == 1
    assert product_less_than_x([1, 2, 0, 4], 5) == 0
    assert product_less_than_x([2, 3, 4], 2) == 1
    assert product_less_than_x([4, 5, 6, 1], 4) == 1
    assert product_less_than_x([-1, -2, -3], 0) == -6
    assert product_less_than_x([4, 0, 3], 1) == 0


# 602. Тесты для функции `sum_of_numbers_in_string`:
def test_sum_of_numbers_in_string():
    assert sum_of_numbers_in_string("123abc") == 369
    assert sum_of_numbers_in_string("abc123") == 0
    assert sum_of_numbers_in_string("abc123def") == 369
    assert sum_of_numbers_in_string("123abc456") == 369
    assert sum_of_numbers_in_string("") == 0
    assert sum_of_numbers_in_string("abc") == 0
    assert sum_of_numbers_in_string("12a34b56") == 1246
    assert sum_of_numbers_in_string("0") == 0
    assert sum_of_numbers_in_string("1a1b1c") == 123


# 603. Тесты для функции `even_numbers_in_string`:
def test_even_numbers_in_string():
    assert even_numbers_in_string("1234") == []
    assert even_numbers_in_string("abc") == []
    assert even_numbers_in_string("2468") == []
    assert even_numbers_in_string("1357") == []
    assert even_numbers_in_string("1a2b3c4d") == [12, 1234]
    assert even_numbers_in_string("abcdefg") == []
    assert even_numbers_in_string("0") == []
    assert even_numbers_in_string("a1b2c3d4") == [12]
    assert even_numbers_in_string("123456") == []


# 604. Тесты для функции `append_to_ring`:
def test_append_to_ring():
    assert append_to_ring([1, 2, 3], 4) == [1, 2, 3, 4]
    assert append_to_ring([1, 2, 3, 4, 5], 6, 5) == [2, 3, 4, 5, 6]
    assert append_to_ring([], 1, 3) == [1]
    assert append_to_ring([1, 2, 3, 4], 5, 3) == [3, 4, 5]
    assert append_to_ring([1, 2], 3) == [1, 2, 3]
    assert append_to_ring([1, 2, 3], 4, 3) == [2, 3, 4]
    assert append_to_ring([1], 2, 1) == [2]
    assert append_to_ring([1, 2], 3, 1) == [3]
    assert append_to_ring([1, 2], 3, 2) == [2, 3]


# 605. Тесты для функции `find_in_ring`:
def test_find_in_ring():
    assert find_in_ring([1, 2, 3], 2) == 1
    assert find_in_ring([1, 2, 3], 4) is None
    assert find_in_ring([], 1) is None
    assert find_in_ring([1, 2, 3, 1], 1) == 0
    assert find_in_ring([1, 2, 3, 4, 5], 5) == 4
    assert find_in_ring([1, 2, 3, 4, 5], 6) is None
    assert find_in_ring([1, 1, 1, 1], 1) == 0
    assert find_in_ring([1, 2, 3], 1) == 0
    assert find_in_ring([1, 2, 3], 3) == 2


# 606. Тесты для функции `find_all_in_ring`:
def test_find_all_in_ring():
    assert find_all_in_ring([1, 2, 3, 1], 1) == [0, 3]
    assert find_all_in_ring([1, 2, 3], 4) == []
    assert find_all_in_ring([], 1) == []
    assert find_all_in_ring([1, 2, 3, 1, 2, 3], 2) == [1, 4]
    assert find_all_in_ring([1, 1, 1, 1], 1) == [0, 1, 2, 3]
    assert find_all_in_ring([1, 2, 3, 4, 5], 5) == [4]
    assert find_all_in_ring([1, 2, 3, 4, 5], 6) == []
    assert find_all_in_ring([1, 2, 3, 3], 3) == [2, 3]
    assert find_all_in_ring([1, 2, 3, 3], 1) == [0]


# 607. Тесты для функции `rotate_with_negativity`:
def test_rotate_with_negativity():
    assert rotate_with_negativity([1, 2, 3], 1) == [3, 1, 2]
    assert rotate_with_negativity([1, 2, 3], -1) == [3, 1, 2]
    assert rotate_with_negativity([], 1) == []
    assert rotate_with_negativity([1, 2, 3, 4], 2) == [3, 4, 1, 2]
    assert rotate_with_negativity([1, 2, 3], 3) == [1, 2, 3]
    assert rotate_with_negativity([1, 2, 3], 0) == [1, 2, 3]
    assert rotate_with_negativity([1, 2, 3], -3) == [1, 2, 3]
    assert rotate_with_negativity([1, 2, 3], -2) == [2, 3, 1]
    assert rotate_with_negativity([1, 2, 3, 4], -1) == [4, 1, 2, 3]


# 608. Тесты для функции `increase_ring_elements`:
def test_increase_ring_elements():
    assert increase_ring_elements([1, 2, 3], 1) == [2, 3, 4]
    assert increase_ring_elements([], 1) == []
    assert increase_ring_elements([0], 1) == [1]
    assert increase_ring_elements([1, 2, 3], -1) == [0, 1, 2]
    assert increase_ring_elements([1, 2, 3], 0) == [1, 2, 3]
    assert increase_ring_elements([1, 2, 3], 2) == [3, 4, 5]
    assert increase_ring_elements([1, -2, 3], 1) == [2, -1, 4]
    assert increase_ring_elements([-1, -2, -3], 1) == [0, -1, -2]
    assert increase_ring_elements([1, 1, 1], 1) == [2, 2, 2]


# 609. Тесты для функции `decrease_ring_elements`:
def test_decrease_ring_elements():
    assert decrease_ring_elements([1, 2, 3], 1) == [0, 1, 2]
    assert decrease_ring_elements([], 1) == []
    assert decrease_ring_elements([0], 1) == [-1]
    assert decrease_ring_elements([1, 2, 3], -1) == [2, 3, 4]
    assert decrease_ring_elements([1, 2, 3], 0) == [1, 2, 3]
    assert decrease_ring_elements([1, 2, 3], 2) == [-1, 0, 1]
    assert decrease_ring_elements([1, -2, 3], 1) == [0, -3, 2]
    assert decrease_ring_elements([-1, -2, -3], 1) == [-2, -3, -4]
    assert decrease_ring_elements([1, 1, 1], 1) == [0, 0, 0]


# 610. Тесты для функции `multiply_ring_elements`:
def test_multiply_ring_elements():
    assert multiply_ring_elements([1, 2, 3], 2) == [2, 4, 6]
    assert multiply_ring_elements([], 2) == []
    assert multiply_ring_elements([0], 2) == [0]
    assert multiply_ring_elements([1, 2, 3], 0) == [0, 0, 0]
    assert multiply_ring_elements([1, 2, 3], -1) == [-1, -2, -3]
    assert multiply_ring_elements([1, -2, 3], 2) == [2, -4, 6]
    assert multiply_ring_elements([-1, -2, -3], 2) == [-2, -4, -6]
    assert multiply_ring_elements([1, 1, 1], 2) == [2, 2, 2]
    assert multiply_ring_elements([1, 2, 3], 1) == [1, 2, 3]


# 611. Тесты для функции `sum_ring`:
def test_sum_ring():
    assert sum_ring([1, 2, 3]) == 6
    assert sum_ring([]) == 0
    assert sum_ring([0]) == 0
    assert sum_ring([-1, -2, -3]) == -6
    assert sum_ring([1, -1, 2, -2]) == 0
    assert sum_ring([5, 5, 5, 5]) == 20
    assert sum_ring([10]) == 10
    assert sum_ring([-1, -1, 1, 1]) == 0
    assert sum_ring([1, 2, 3, 4, 5]) == 15


# 612. Тесты для функции `average_ring`:
def test_average_ring():
    assert average_ring([1, 2, 3]) == 2
    assert average_ring([]) is None
    assert average_ring([0]) == 0
    assert average_ring([-1, -2, -3]) == -2
    assert average_ring([1, -1, 2, -2]) == 0
    assert average_ring([5, 5, 5, 5]) == 5
    assert average_ring([10]) == 10
    assert average_ring([-1, -1, 1, 1]) == 0
    assert average_ring([1, 2, 3, 4, 5]) == 3


# 613. Тесты для функции `max_ring`:
def test_max_ring():
    assert max_ring([1, 2, 3]) == 3
    assert max_ring([]) is None
    assert max_ring([0]) == 0
    assert max_ring([-1, -2, -3]) == -1
    assert max_ring([1, -1, 2, -2]) == 2
    assert max_ring([5, 5, 5, 5]) == 5
    assert max_ring([10]) == 10
    assert max_ring([-1, -1, 1, 1]) == 1
    assert max_ring([1, 2, 3, 4, 5]) == 5


# 614. Тесты для функции `min_ring`:
def test_min_ring():
    assert min_ring([1, 2, 3]) == 1
    assert min_ring([]) is None
    assert min_ring([0]) == 0
    assert min_ring([-1, -2, -3]) == -3
    assert min_ring([1, -1, 2, -2]) == -2
    assert min_ring([5, 5, 5, 5]) == 5
    assert min_ring([10]) == 10
    assert min_ring([-1, -1, 1, 1]) == -1
    assert min_ring([1, 2, 3, 4, 5]) == 1


# 615. Тесты для функции `has_positive_ring`:
def test_has_positive_ring():
    assert has_positive_ring([1, 2, 3]) is True
    assert has_positive_ring([]) is False
    assert has_positive_ring([0]) is False
    assert has_positive_ring([-1, -2, -3]) is False
    assert has_positive_ring([1, -1, 2, -2]) is True
    assert has_positive_ring([5, 5, 5, 5]) is True
    assert has_positive_ring([10]) is True
    assert has_positive_ring([-1, -1, -1, -1]) is False
    assert has_positive_ring([1, 2, 3, 4, 5]) is True


# 616. Тесты для функции `has_negative_ring`:
def test_has_negative_ring():
    assert has_negative_ring([1, 2, 3]) is False
    assert has_negative_ring([]) is False
    assert has_negative_ring([0]) is False
    assert has_negative_ring([-1, -2, -3]) is True
    assert has_negative_ring([1, -1, 2, -2]) is True
    assert has_negative_ring([5, 5, 5, 5]) is False
    assert has_negative_ring([10]) is False
    assert has_negative_ring([-1, -1, -1, -1]) is True
    assert has_negative_ring([1, 2, 3, 4, 5]) is False


# 617. Тесты для функции `reverse_even_index_elements`:
def test_reverse_even_index_elements():
    assert reverse_even_index_elements([1, 2, 3, 4]) == [4, 2, 2, 4]
    assert reverse_even_index_elements([]) == []
    assert reverse_even_index_elements([0]) == [0]
    assert reverse_even_index_elements([1, 2, 3, 4, 5]) == [5, 2, 3, 4, 1]
    assert reverse_even_index_elements([1, -1, 2, -2]) == [-2, -1, -1, -2]
    assert reverse_even_index_elements([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert reverse_even_index_elements([10]) == [10]
    assert reverse_even_index_elements([1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1]
    assert reverse_even_index_elements([1, 2, 3, 4, 5, 6]) == [6, 2, 4, 4, 2, 6]


# 618. Тесты для функции `find_even_ring`:
def test_find_even_ring():
    assert find_even_ring([1, 2, 3, 4]) == [2, 4]
    assert find_even_ring([]) == []
    assert find_even_ring([0]) == [0]
    assert find_even_ring([1, 3, 5]) == []
    assert find_even_ring([2, 4, 6]) == [2, 4, 6]
    assert find_even_ring([-2, -4, -6]) == [-2, -4, -6]
    assert find_even_ring([-1, -3, -5]) == []
    assert find_even_ring([1, 2, 3, 4, 5]) == [2, 4]
    assert find_even_ring([2, 2, 2, 2]) == [2, 2, 2, 2]


# 619. Тесты для функции `find_odd_ring`:
def test_find_odd_ring():
    assert find_odd_ring([1, 2, 3, 4]) == [1, 3]
    assert find_odd_ring([]) == []
    assert find_odd_ring([0]) == []
    assert find_odd_ring([1, 3, 5]) == [1, 3, 5]
    assert find_odd_ring([2, 4, 6]) == []
    assert find_odd_ring([-2, -4, -6]) == []
    assert find_odd_ring([-1, -3, -5]) == [-1, -3, -5]
    assert find_odd_ring([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert find_odd_ring([2, 2, 2, 2]) == []


# 620. Тесты для функции `count_even_ring`:
def test_count_even_ring():
    assert count_even_ring([1, 2, 3, 4]) == 2
    assert count_even_ring([]) == 0
    assert count_even_ring([0]) == 1
    assert count_even_ring([1, 3, 5]) == 0
    assert count_even_ring([2, 4, 6]) == 3
    assert count_even_ring([-2, -4, -6]) == 3
    assert count_even_ring([-1, -3, -5]) == 0
    assert count_even_ring([1, 2, 3, 4, 5]) == 2
    assert count_even_ring([2, 2, 2, 2]) == 4
