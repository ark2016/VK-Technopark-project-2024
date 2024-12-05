from functions.file_781_800 import *
import pytest


# 781. Тесты для функции `choose_smallest_odd_number`:
def test_choose_smallest_odd_number():
    assert choose_smallest_odd_number(5, 3, 9) == 3
    assert choose_smallest_odd_number(2, 4, 6) is None
    assert choose_smallest_odd_number(7, 3, -1, -5) == -5
    assert choose_smallest_odd_number(1, 1, 1) == 1
    assert choose_smallest_odd_number() is None
    assert choose_smallest_odd_number(4, 9, 11) == 9


# 782. Тесты для функции `choose_first_greater_than_100_even`:
def test_choose_first_greater_than_100_even():
    assert choose_first_greater_than_100_even([101, 102, 103]) == 102
    assert choose_first_greater_than_100_even([100, 99, 98]) is None
    assert choose_first_greater_than_100_even([150, 101, 200]) == 150
    assert choose_first_greater_than_100_even([]) is None
    assert choose_first_greater_than_100_even([200, 150, 180]) == 200
    assert choose_first_greater_than_100_even([123, 245, 132]) == 132


# 783. Тесты для функции `choose_longest_digit_word`:
def test_choose_longest_digit_word():
    assert choose_longest_digit_word("123", "4567", "89") == "4567"
    assert choose_longest_digit_word("abc", "def", "ghi") is None
    assert choose_longest_digit_word("1", "22", "333", "4444", "55555") == "55555"
    assert choose_longest_digit_word() is None
    assert choose_longest_digit_word("789", "12", "234") == "789"
    assert choose_longest_digit_word("10", "20", "30", "40") == "10"


# 784. Тесты для функции `is_prime_using_set`:
def test_is_prime_using_set():
    assert is_prime_using_set(2) is True
    assert is_prime_using_set(3) is True
    assert is_prime_using_set(4) is False
    assert is_prime_using_set(-1) is False
    assert is_prime_using_set(11) is True
    assert is_prime_using_set(1) is False
    assert is_prime_using_set(0) is False
    assert is_prime_using_set(5) is True
    assert is_prime_using_set(9) is False


# 785. Тесты для функции `count_multiples_of`:
def test_count_multiples_of():
    assert count_multiples_of(3, [3, 6, 9, 12]) == 4
    assert count_multiples_of(5, [1, 2, 3, 4]) is None
    assert count_multiples_of(2, [4, 6, 8, 10]) == 4
    assert count_multiples_of(7, [14, 21, 28, 35]) == 4
    assert count_multiples_of(1, [1, 2, 3, 4, 5]) == 5
    assert count_multiples_of(10, [10, 20, 30, 40]) == 4


# 786. Тесты для функции `find_divisible_by_all_in_set`:
def test_find_divisible_by_all_in_set():
    assert find_divisible_by_all_in_set({1, 2, 3}, 6) == 6
    assert find_divisible_by_all_in_set({2, 3}, 5) is None
    assert find_divisible_by_all_in_set({5, 10, 15}, 30) == 30
    assert find_divisible_by_all_in_set({3, 9, 27}, 81) == 81
    assert find_divisible_by_all_in_set({2, 4, 8}, 16) == 16
    assert find_divisible_by_all_in_set({3, 6, 12}, 12) == 12


# 787. Тесты для функции `find_number_not_in_dict`:
def test_find_number_not_in_dict():
    assert find_number_not_in_dict({1: 'a', 2: 'b', 3: 'c'}, 4) == 4
    assert find_number_not_in_dict({1: 'a', 2: 'b', 3: 'c'}, 2) is None
    assert find_number_not_in_dict({}, 1) == 1
    assert find_number_not_in_dict({5: 'x', 6: 'y', 7: 'z'}, 8) == 8
    assert find_number_not_in_dict({9: 'a', 10: 'b'}, 10) is None
    assert find_number_not_in_dict({100: 'a', 200: 'b'}, 150) == 150


# 788. Тесты для функции `find_max_divisible`:
def test_find_max_divisible():
    assert find_max_divisible([12, 15, 20, 30], 5) == 30
    assert find_max_divisible([7, 14, 21, 28], 3) == 21
    assert find_max_divisible([8, 16, 24], 4) == 24
    assert find_max_divisible([1, 2, 3, 4], 5) is None
    assert find_max_divisible([9, 18, 27, 36], 9) == 36
    assert find_max_divisible([], 5) is None


# 789. Тесты для функции `find_not_divisible_by_2_3_5`:
def test_find_not_divisible_by_2_3_5():
    assert find_not_divisible_by_2_3_5([7, 11, 13, 17]) == [7, 11, 13, 17]
    assert find_not_divisible_by_2_3_5([6, 10, 15, 20]) is None
    assert find_not_divisible_by_2_3_5([1, 2, 3, 5, 7]) == [1, 7]
    assert find_not_divisible_by_2_3_5([9, 18, 27, 35]) is None
    assert find_not_divisible_by_2_3_5([8, 16, 24, 30]) is None
    assert find_not_divisible_by_2_3_5([19, 23, 29, 31]) == [19, 23, 29, 31]


# 790. Тесты для функции `sum_of_elements_greater_than`:
def test_sum_of_elements_greater_than():
    assert sum_of_elements_greater_than(10, {12, 15, 20}) == 47
    assert sum_of_elements_greater_than(25, {5, 10, 15, 20}) is None
    assert sum_of_elements_greater_than(0, {1, 2, 3, 4}) == 10
    assert sum_of_elements_greater_than(5, {10, 20, 30}) == 60
    assert sum_of_elements_greater_than(100, {50, 75, 125}) == 125
    assert sum_of_elements_greater_than(-5, {1, 2, 3, 4}) == 10


# 791. Тесты для функции `max_difference_in_dict`:
def test_max_difference_in_dict():
    assert max_difference_in_dict({1: 10, 2: 20, 3: 30}) == 20
    assert max_difference_in_dict({}) is None
    assert max_difference_in_dict({4: 50}) is None
    assert max_difference_in_dict({5: 5, 6: 10, 7: 15}) == 10
    assert max_difference_in_dict({10: 100, 20: 200}) == 100
    assert max_difference_in_dict({8: 8, 9: 18, 10: 28}) == 20


# 792. Тесты для функции `average_of_set`:
def test_average_of_set():
    assert average_of_set({1, 2, 3, 4}) == 2.5
    assert average_of_set({10, 20, 30}) == 20.0
    assert average_of_set(set()) is None
    assert average_of_set({5, 15, 25, 35}) == 20.0
    assert average_of_set({100}) == 100.0
    assert average_of_set({1, 3, 5, 7, 9}) == 5.0


# 793. Тесты для функции `find_greater_than_and_not_divisible_by_2`:
def test_find_greater_than_and_not_divisible_by_2():
    assert find_greater_than_and_not_divisible_by_2([1, 3, 5, 7, 9], 4) == [5, 7, 9]
    assert find_greater_than_and_not_divisible_by_2([2, 4, 6, 8], 3) is None
    assert find_greater_than_and_not_divisible_by_2([11, 13, 17, 19], 10) == [11, 13, 17, 19]
    assert find_greater_than_and_not_divisible_by_2([], 5) is None
    assert find_greater_than_and_not_divisible_by_2([5, 15, 25, 35], 10) == [15, 25, 35]
    assert find_greater_than_and_not_divisible_by_2([21, 23, 25, 27], 22) == [23, 25, 27]


# 794. Тесты для функции `find_min_divisible_by_all`:
def test_find_min_divisible_by_all():
    assert find_min_divisible_by_all([1, 2, 3]) is None
    assert find_min_divisible_by_all([5, 10, 15]) is None
    assert find_min_divisible_by_all([4, 8, 16]) == 16
    assert find_min_divisible_by_all([7, 14, 28]) == 28
    assert find_min_divisible_by_all([2, 3, 5]) is None
    assert find_min_divisible_by_all([3, 5, 7, 11]) is None


# 795. Тесты для функции `find_smallest_key_greater_than`:
def test_find_smallest_key_greater_than():
    assert find_smallest_key_greater_than({1: 10, 2: 20, 3: 30}, 15) == 2
    assert find_smallest_key_greater_than({4: 40, 5: 50}, 60) is None
    assert find_smallest_key_greater_than({6: 60, 7: 70, 8: 80}, 65) == 7
    assert find_smallest_key_greater_than({}, 10) is None
    assert find_smallest_key_greater_than({9: 90, 10: 100}, 95) == 10
    assert find_smallest_key_greater_than({11: 110, 12: 120}, 105) == 11


# 796. Тесты для функции `find_first_square_greater_than`:
def test_find_first_square_greater_than():
    assert find_first_square_greater_than([1, 4, 9, 16], 5) == 9
    assert find_first_square_greater_than([25, 36, 49], 30) == 36
    assert find_first_square_greater_than([2, 3, 5], 6) is None
    assert find_first_square_greater_than([81, 64, 49], 50) == 81
    assert find_first_square_greater_than([], 10) is None
    assert find_first_square_greater_than([100, 121, 144], 110) == 121


# 797. Тесты для функции `find_first_divisible_by_2_and_3`:
def test_find_first_divisible_by_2_and_3():
    assert find_first_divisible_by_2_and_3({6, 12, 18}) == 18
    assert find_first_divisible_by_2_and_3({1, 3, 5}) is None
    assert find_first_divisible_by_2_and_3({24, 30, 36}) == 24
    assert find_first_divisible_by_2_and_3(set()) is None
    assert find_first_divisible_by_2_and_3({7, 14, 21}) is None
    assert find_first_divisible_by_2_and_3({9, 15, 21, 27}) is None


# 798. Тесты для функции `find_common_in_lists`:
def test_find_common_in_lists():
    assert find_common_in_lists([1, 2, 3], [3, 4, 5]) == 3
    assert find_common_in_lists([6, 7, 8], [9, 10, 11]) is None
    assert find_common_in_lists([12, 13, 14], [14, 15, 16]) == 14
    assert find_common_in_lists([17, 18, 19], [20, 21, 22]) is None
    assert find_common_in_lists([23, 24, 25], [25, 26, 27]) == 25
    assert find_common_in_lists([], [28, 29, 30]) is None


# 799. Тесты для функции `find_smallest_even_greater_than`:
def test_find_smallest_even_greater_than():
    assert find_smallest_even_greater_than([2, 4, 6, 8], 5) == 6
    assert find_smallest_even_greater_than([10, 12, 14], 15) is None
    assert find_smallest_even_greater_than([16, 18, 20], 17) == 18
    assert find_smallest_even_greater_than([], 3) is None
    assert find_smallest_even_greater_than([22, 24, 26], 21) == 22
    assert find_smallest_even_greater_than([28, 30, 32], 29) == 30


# 800. Тесты для функции `find_element_greater_than_in_set`:
def test_find_element_greater_than_in_set():
    assert find_element_greater_than_in_set({1, 2, 3, 4}, 3) == 4
    assert find_element_greater_than_in_set({5, 6, 7, 8}, 10) is None
    assert find_element_greater_than_in_set({11, 12, 13, 14}, 12) == 13
    assert find_element_greater_than_in_set(set(), 0) is None
    assert find_element_greater_than_in_set({15, 16, 17, 18}, 16) == 17
    assert find_element_greater_than_in_set({19, 20, 21, 22}, 18) == 19
