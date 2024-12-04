import pytest
from functions.file_401_420 import *


# 401. Тесты для функции find_unique_elements_in_sets
def test_find_unique_elements_in_sets():
    assert find_unique_elements_in_sets({1, 2, 3}, {3, 4, 5}) == [1, 2, 4, 5]
    assert find_unique_elements_in_sets({1, 2, 3}, {1, 2, 3}) == None
    assert find_unique_elements_in_sets({1}, {2}) == [1, 2]
    assert find_unique_elements_in_sets(set(), {1, 2, 3}) == [1, 2, 3]
    assert find_unique_elements_in_sets({1, 2, 3}, set()) == [1, 2, 3]
    assert find_unique_elements_in_sets(set(), set()) == None


# 402. Тесты для функции find_divisible_by_2_in_both_sets_2
def test_find_divisible_by_2_in_both_sets_2():
    assert find_divisible_by_2_in_both_sets_2({2, 4, 6}, {4, 6, 8}) == [4, 6]
    assert find_divisible_by_2_in_both_sets_2({1, 2, 3}, {4, 5, 6}) == None
    assert find_divisible_by_2_in_both_sets_2({1, 3, 5}, {7, 9, 11}) == None
    assert find_divisible_by_2_in_both_sets_2({2, 4, 6, 8}, {4, 8, 10}) == [4, 8]
    assert find_divisible_by_2_in_both_sets_2({2, 4, 6}, {1, 3, 5}) == None
    assert find_divisible_by_2_in_both_sets_2({2}, {2}) == [2]


# 403. Тесты для функции find_in_first_set_not_second
def test_find_in_first_set_not_second():
    assert find_in_first_set_not_second({1, 2, 3}, {3, 4, 5}) == [1, 2]
    assert find_in_first_set_not_second({1, 2, 3}, {1, 2, 3}) == None
    assert find_in_first_set_not_second({1}, {2}) == [1]
    assert find_in_first_set_not_second(set(), {1, 2, 3}) == None
    assert find_in_first_set_not_second({1, 2, 3}, set()) == [1, 2, 3]
    assert find_in_first_set_not_second({1, 2, 3}, {2}) == [1, 3]


# 404. Тесты для функции find_divisible_by_5_in_one_set
def test_find_divisible_by_5_in_one_set():
    assert find_divisible_by_5_in_one_set({5, 10, 15}, {10, 20, 30}) == [5, 15]
    assert find_divisible_by_5_in_one_set({5, 10, 15}, {5, 10, 15}) == None
    assert find_divisible_by_5_in_one_set({1, 2, 3}, {4, 5, 6}) == None
    assert find_divisible_by_5_in_one_set({10, 20, 30}, {5, 15, 25}) == [10, 20, 30]
    assert find_divisible_by_5_in_one_set({5, 10, 15}, {2, 4, 6}) == [5, 10, 15]
    assert find_divisible_by_5_in_one_set({1, 2, 3}, {3, 4, 5}) == None


# 405. Тесты для функции is_stack_empty
def test_is_stack_empty():
    assert is_stack_empty([]) == True
    assert is_stack_empty([1, 2, 3]) == False
    assert is_stack_empty([0]) == False
    assert is_stack_empty(['a', 'b']) == False
    assert is_stack_empty([None]) == False
    assert is_stack_empty([False]) == False


# 406. Тесты для функции fill_stack_until_limit
def test_fill_stack_until_limit():
    assert fill_stack_until_limit([], 3) == [1, 2, 3]
    assert fill_stack_until_limit([1, 2], 4) == [1, 2, 3, 4]
    assert fill_stack_until_limit([1], 1) == [1]
    assert fill_stack_until_limit([], 0) == []
    assert fill_stack_until_limit([1, 2, 3], 2) == [1, 2, 3]
    assert fill_stack_until_limit([], 5) == [1, 2, 3, 4, 5]


# 407. Тесты для функции fill_stack_up_to_n
def test_fill_stack_up_to_n():
    assert fill_stack_up_to_n([], 3) == [1, 2, 3]
    assert fill_stack_up_to_n([1, 2], 4) == [1, 2, 1, 2, 3, 4]
    assert fill_stack_up_to_n([1], 1) == [1, 1]
    assert fill_stack_up_to_n([], 0) == []
    assert fill_stack_up_to_n([1, 2, 3], 2) == [1, 2, 3, 1, 2]
    assert fill_stack_up_to_n([], 5) == [1, 2, 3, 4, 5]


# 408. Тесты для функции is_stack_palindrome
def test_is_stack_palindrome():
    assert is_stack_palindrome([1, 2, 1]) == True
    assert is_stack_palindrome([1, 2, 2, 1]) == True
    assert is_stack_palindrome([1, 2, 3]) == False
    assert is_stack_palindrome([1]) == True
    assert is_stack_palindrome([]) == True
    assert is_stack_palindrome([1, 2, 3, 2, 1]) == True


# 409. Тесты для функции pop_until_greater_than_x
def test_pop_until_greater_than_x():
    assert pop_until_greater_than_x([1, 2, 3, 4, 5], 3) == [5]
    assert pop_until_greater_than_x([5, 4, 3, 2, 1], 3) == [1, 2, 3, 4]
    assert pop_until_greater_than_x([1, 2, 3], 5) == [3, 2, 1]
    assert pop_until_greater_than_x([], 3) == None
    assert pop_until_greater_than_x([1, 2, 3], 0) == [3]
    assert pop_until_greater_than_x([5, 6, 7], 4) == [7]


# 410. Тесты для функции pop_elements_less_than_y
def test_pop_elements_less_than_y():
    assert pop_elements_less_than_y([1, 2, 3, 4, 5], 3) == [2, 1]
    assert pop_elements_less_than_y([5, 4, 3, 2, 1], 3) == [1, 2]
    assert pop_elements_less_than_y([1, 2, 3], 5) == [3, 2, 1]
    assert pop_elements_less_than_y([], 3) == None
    assert pop_elements_less_than_y([1, 2, 3], 0) == None
    assert pop_elements_less_than_y([5, 6, 7], 4) == None


# 411. Тесты для функции remove_odds_from_stack
def test_remove_odds_from_stack():
    assert remove_odds_from_stack([1, 2, 3, 4, 5]) == [4, 2]
    assert remove_odds_from_stack([1, 3, 5]) == None
    assert remove_odds_from_stack([2, 4, 6]) == [6, 4, 2]
    assert remove_odds_from_stack([]) == None
    assert remove_odds_from_stack([1, 2, 3]) == [2]
    assert remove_odds_from_stack([5, 4, 3, 2, 1]) == [2, 4]


# 412. Тесты для функции pop_until_sum_exceeds_x
def test_pop_until_sum_exceeds_x():
    assert pop_until_sum_exceeds_x([1, 2, 3, 4, 5], 10) == [5, 4, 3]
    assert pop_until_sum_exceeds_x([5, 4, 3, 2, 1], 7) == [1, 2, 3, 4]
    assert pop_until_sum_exceeds_x([], 3) == None
    assert pop_until_sum_exceeds_x([1, 2, 3], 1) == [3]
    assert pop_until_sum_exceeds_x([5, 6, 7], 4) == [7]
    assert pop_until_sum_exceeds_x([1, 2, 3], 5) == [3, 2, 1]


# 413. Тесты для функции pop_elements_divisible_by_3
def test_pop_elements_divisible_by_3():
    assert pop_elements_divisible_by_3([1, 2, 3, 4, 5, 6, 9]) == [9, 6, 3]
    assert pop_elements_divisible_by_3([1, 2, 4, 5]) == None
    assert pop_elements_divisible_by_3([3, 6, 9]) == [9, 6, 3]
    assert pop_elements_divisible_by_3([]) == None
    assert pop_elements_divisible_by_3([3]) == [3]
    assert pop_elements_divisible_by_3([1, 2, 3]) == [3]


# 414. Тесты для функции pop_min_element
def test_pop_min_element():
    assert pop_min_element([1, 2, 3, 4, 5]) == 1
    assert pop_min_element([5, 4, 3, 2, 1]) == 1
    assert pop_min_element([]) == None
    assert pop_min_element([1]) == 1
    assert pop_min_element([5, 3, 9, 7]) == 3
    assert pop_min_element([2, 2, 2, 2]) == 2


# 415. Тесты для функции double_stack_values
def test_double_stack_values():
    assert double_stack_values([1, 2, 3]) == [6, 4, 2]
    assert double_stack_values([0, 1, 2]) == [4, 2, 0]
    assert double_stack_values([]) == []
    assert double_stack_values([2, 4, 6]) == [12, 8, 4]
    assert double_stack_values([5, 5, 5]) == [10, 10, 10]
    assert double_stack_values([-1, -2, -3]) == [-6, -4, -2]


# 416. Тесты для функции pop_until_even
def test_pop_until_even():
    assert pop_until_even([1, 3, 5, 2, 7]) == [7, 2]
    assert pop_until_even([2, 4, 6, 1]) == [1, 6]
    assert pop_until_even([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert pop_until_even([]) == None
    assert pop_until_even([2, 4, 6, 8]) == [8]
    assert pop_until_even([3, 3, 3, 3]) == [3, 3, 3, 3]


# 417. Тесты для функции pop_prime_numbers
def test_pop_prime_numbers():
    assert pop_prime_numbers([1, 2, 3, 4, 5, 6, 7]) == [7, 5, 3, 2]
    assert pop_prime_numbers([1, 1, 1, 1]) == None
    assert pop_prime_numbers([2, 3, 5, 7]) == [7, 5, 3, 2]
    assert pop_prime_numbers([]) == None
    assert pop_prime_numbers([4, 6, 8, 9]) == None
    assert pop_prime_numbers([11, 13, 17]) == [17, 13, 11]


# 418. Тесты для функции pop_until_divisible_by_4
def test_pop_until_divisible_by_4():
    assert pop_until_divisible_by_4([1, 2, 3, 4, 5]) == [5, 4]
    assert pop_until_divisible_by_4([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert pop_until_divisible_by_4([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert pop_until_divisible_by_4([]) == None
    assert pop_until_divisible_by_4([2, 2, 2, 4]) == [4]
    assert pop_until_divisible_by_4([4]) == [4]


# 419. Тесты для функции remove_non_divisible_by_2
def test_remove_non_divisible_by_2():
    assert remove_non_divisible_by_2([1, 2, 3, 4, 5]) == [4, 2]
    assert remove_non_divisible_by_2([1, 3, 5]) == None
    assert remove_non_divisible_by_2([2, 4, 6]) == [6, 4, 2]
    assert remove_non_divisible_by_2([]) == None
    assert remove_non_divisible_by_2([1, 2, 3]) == [2]
    assert remove_non_divisible_by_2([5, 4, 3, 2, 1]) == [2, 4]


# 420. Тесты для функции remove_even_from_stack
def test_remove_even_from_stack():
    assert remove_even_from_stack([1, 2, 3, 4, 5]) == [5, 3, 1]
    assert remove_even_from_stack([2, 4, 6, 8]) == None
    assert remove_even_from_stack([1, 3, 5, 7]) == [7, 5, 3, 1]
    assert remove_even_from_stack([]) == None
    assert remove_even_from_stack([1]) == [1]
    assert remove_even_from_stack([4, 3, 2, 1]) == [1, 3]
