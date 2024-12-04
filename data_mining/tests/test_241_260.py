import pytest
from functions.file_241_260 import *


# 241. Тесты для функции `find_multiples_of_6_not_12`:
def test_find_multiples_of_6_not_12():
    assert find_multiples_of_6_not_12([6, 12, 18, 24, 30]) == [6, 18, 30]
    assert find_multiples_of_6_not_12([1, 2, 3, 4, 5]) == None
    assert find_multiples_of_6_not_12([12, 24, 36]) == None
    assert find_multiples_of_6_not_12([-6, -12, -18, -30]) == [-6, -18, -30]
    assert find_multiples_of_6_not_12([]) == None
    assert find_multiples_of_6_not_12([6, 36, 60]) == [6]
    assert find_multiples_of_6_not_12([60]) == None
    assert find_multiples_of_6_not_12([60, 70, 80]) == None
    assert find_multiples_of_6_not_12([13, 18, 22]) == [18]

# 242. Тесты для функции `find_even_not_divisible_by_5`:
def test_find_even_not_divisible_by_5():
    assert find_even_not_divisible_by_5([10, 20, 30, 40, 50]) == None
    assert find_even_not_divisible_by_5([1, 2, 3, 4, 5]) == [2, 4]
    assert find_even_not_divisible_by_5([6, 12, 18, 24, 30]) == [6, 12, 18, 24]
    assert find_even_not_divisible_by_5([-10, -20, -30, -40, -50]) == None
    assert find_even_not_divisible_by_5([-1, -2, -3, -4, -5]) == [-2, -4]
    assert find_even_not_divisible_by_5([15, 25, 35, 45]) == None
    assert find_even_not_divisible_by_5([0, 1, 2, 3, 4, 5]) == [2, 4]
    assert find_even_not_divisible_by_5([6, 7, 8, 9, 10]) == [6, 8]
    assert find_even_not_divisible_by_5([15, 20, 25, 30, 35]) == None

# 243. Тесты для функции `find_squares_of_odd_not_divisible_by_3`:
def test_find_squares_of_odd_not_divisible_by_3():
    assert find_squares_of_odd_not_divisible_by_3([1, 4, 9, 16, 25, 36, 49]) == [1, 25, 49]
    assert find_squares_of_odd_not_divisible_by_3([2, 3, 5, 7, 11]) == None
    assert find_squares_of_odd_not_divisible_by_3([1, 25, 49, 81]) == [1, 25, 49]
    assert find_squares_of_odd_not_divisible_by_3([1, 4, 9, 16, 25, 36, 49]) == [1, 25, 49]
    assert find_squares_of_odd_not_divisible_by_3([1, 3, 5, 7, 9, 11]) == [1]
    assert find_squares_of_odd_not_divisible_by_3([25, 49, 81, 100]) == [25, 49]
    assert find_squares_of_odd_not_divisible_by_3([36, 45, 54, 63, 72]) == None
    assert find_squares_of_odd_not_divisible_by_3([10, 20, 30, 40, 50]) == None
    assert find_squares_of_odd_not_divisible_by_3([100, 121, 144, 169]) == [121, 169]

# 244. Тесты для функции `find_divisors_of_50_not_prime`:
def test_find_divisors_of_50_not_prime():
    assert find_divisors_of_50_not_prime([1, 2, 5, 10, 25, 50]) == [1, 10, 25, 50]
    assert find_divisors_of_50_not_prime([2, 3, 5, 7, 11, 13]) == None
    assert find_divisors_of_50_not_prime([4, 6, 8, 10, 12]) == [10]
    assert find_divisors_of_50_not_prime([-1, -2, -5, -10, -25, -50]) == [-1, -2, -5, -10, -25, -50]
    assert find_divisors_of_50_not_prime([1, 2, 3, 4, 5]) == [1]
    assert find_divisors_of_50_not_prime([50, 100, 150, 200]) == [50]
    assert find_divisors_of_50_not_prime([7, 8, 9, 10, 11]) == [10]
    assert find_divisors_of_50_not_prime([13, 17, 19, 23]) == None
    assert find_divisors_of_50_not_prime([25, 30, 35, 40]) == [25]

# 245. Тесты для функции `find_divisible_by_3_and_4_not_7`:
def test_find_divisible_by_3_and_4_not_7():
    assert find_divisible_by_3_and_4_not_7([12, 24, 36, 48, 60]) == [12, 24, 36, 48, 60]
    assert find_divisible_by_3_and_4_not_7([1, 2, 3, 4, 5]) == None
    assert find_divisible_by_3_and_4_not_7([21, 28, 35, 42, 49]) == None
    assert find_divisible_by_3_and_4_not_7([-12, -24, -36, -48, -60]) == [-12, -24, -36, -48, -60]
    assert find_divisible_by_3_and_4_not_7([6, 18, 30, 42, 54]) == None
    assert find_divisible_by_3_and_4_not_7([84, 96, 108, 120]) == [96, 108, 120]
    assert find_divisible_by_3_and_4_not_7([36, 48, 54, 72]) == [36, 48, 72]
    assert find_divisible_by_3_and_4_not_7([27, 33, 39, 45]) == None
    assert find_divisible_by_3_and_4_not_7([12, 24, 36]) == [12, 24, 36]

# 246. Тесты для функции `find_intersection_of_sets`:
def test_find_intersection_of_sets():
    assert find_intersection_of_sets([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    assert find_intersection_of_sets([1, 2, 3], [4, 5, 6]) == None
    assert find_intersection_of_sets([7, 8, 9], [7, 8, 9]) == [7, 8, 9]
    assert find_intersection_of_sets([], [1, 2, 3]) == None
    assert find_intersection_of_sets([1, 2, 3], []) == None
    assert find_intersection_of_sets([0, 1, 2], [2, 3, 4]) == [2]
    assert find_intersection_of_sets([-1, -2, -3], [-3, -4, -5]) == [-3]
    assert find_intersection_of_sets([10, 11, 12], [12, 13, 14]) == [12]
    assert find_intersection_of_sets([15, 16, 17], [18, 19, 20]) == None


# 247. Тесты для функции `find_symmetric_difference`:
def test_find_symmetric_difference():
    assert find_symmetric_difference([1, 2, 3], [3, 4, 5]) == [1, 2, 4, 5]
    assert find_symmetric_difference([7, 8, 9], [7, 8, 9]) == None
    assert find_symmetric_difference([10, 20, 30], [30, 40, 50]) == [10, 20, 40, 50]
    assert find_symmetric_difference([], [1, 2, 3]) == [1, 2, 3]
    assert find_symmetric_difference([1, 2, 3], []) == [1, 2, 3]
    assert find_symmetric_difference([-1, -2, -3], [-3, -4, -5]) == [-5, -4, -2, -1]
    assert find_symmetric_difference([10, 11, 12], [12, 13, 14]) == [10, 11, 13, 14]
    assert find_symmetric_difference([15, 16, 17], [18, 19, 20]) == [15, 16, 17, 18, 19, 20]
    assert find_symmetric_difference([1, 3, 5, 7], [2, 4, 6, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]

# 248. Тесты для функции `find_keys_in_dicts`:
def test_find_keys_in_dicts():
    assert find_keys_in_dicts({1: 2, 3: 4, 5: 6}, {2: 'a', 4: 'b', 6: 'c'}) == [1, 3, 5]
    assert find_keys_in_dicts({1: 2, 3: 4, 5: 6}, {7: 'a', 8: 'b', 9: 'c'}) == None
    assert find_keys_in_dicts({}, {2: 'a', 4: 'b', 6: 'c'}) == None
    assert find_keys_in_dicts({1: 2, 3: 4, 5: 6}, {}) == None
    assert find_keys_in_dicts({1: 2, 3: 4, 5: 6}, {4: 'b'}) == [3]
    assert find_keys_in_dicts({1: 2, 3: 4, 5: 6}, {6: 'c'}) == [5]
    assert find_keys_in_dicts({1: 2, 3: 4}, {4: 'b', 2: 'a'}) == [1, 3]
    assert find_keys_in_dicts({7: 8, 9: 10}, {8: 'd', 10: 'e'}) == [7, 9]
    assert find_keys_in_dicts({11: 12, 13: 14}, {14: 'g', 12: 'f'}) == [11, 13]

# 249. Тесты для функции `find_in_list_not_in_tuple`:
def test_find_in_list_not_in_tuple():
    assert find_in_list_not_in_tuple([1, 2, 3, 4, 5], (4, 5, 6, 7)) == [1, 2, 3]
    assert find_in_list_not_in_tuple([1, 2, 3], (1, 2, 3)) == None
    assert find_in_list_not_in_tuple([4, 5, 6], (1, 2, 3)) == [4, 5, 6]
    assert find_in_list_not_in_tuple([], (1, 2, 3)) == None
    assert find_in_list_not_in_tuple([1, 2, 3], ()) == [1, 2, 3]
    assert find_in_list_not_in_tuple([1, 3, 5], (2, 4, 6)) == [1, 3, 5]
    assert find_in_list_not_in_tuple([-1, -2, -3], (-3, -4, -5)) == [-1, -2]
    assert find_in_list_not_in_tuple([10, 20, 30], (20, 30, 40)) == [10]
    assert find_in_list_not_in_tuple([15, 25, 35], (10, 20, 30)) == [15, 25, 35]

# 250. Тесты для функции `find_pairs_with_first_greater`:
def test_find_pairs_with_first_greater():
    assert find_pairs_with_first_greater([1, 2, 3]) == [(2, 1), (3, 1), (3, 2)]
    assert find_pairs_with_first_greater([3, 1, 2]) == [(3, 1), (3, 2), (2, 1)]
    assert find_pairs_with_first_greater([1, 1, 1]) == None
    assert find_pairs_with_first_greater([]) == None
    assert find_pairs_with_first_greater([5, 5, 5]) == None
    assert find_pairs_with_first_greater([4, 5, 6]) == [(5, 4), (6, 4), (6, 5)]
    assert find_pairs_with_first_greater([10, 20, 30]) == [(20, 10), (30, 10), (30, 20)]
    assert find_pairs_with_first_greater([-1, 0, 1]) == [(0, -1), (1, -1), (1, 0)]
    assert find_pairs_with_first_greater([10, 20, 30, 40]) == [(20, 10), (30, 10), (30, 20), (40, 10), (40, 20), (40, 30)]


# 251. Тесты для функции `find_tuples_without_negatives`:
def test_find_tuples_without_negatives():
    assert find_tuples_without_negatives([(1, 2), (-1, 2), (3, 4)]) == [(1, 2), (3, 4)]
    assert find_tuples_without_negatives([(1, 2, -3), (-4, 5, 6), (7, 8, 9)]) == [(7, 8, 9)]
    assert find_tuples_without_negatives([(0, 1, 2)]) == [(0, 1, 2)]
    assert find_tuples_without_negatives([(-1, -2, -3)]) == None
    assert find_tuples_without_negatives([]) == None
    assert find_tuples_without_negatives([(1, 1), (0, 0), (-1, -1)]) == [(1, 1), (0, 0)]
    assert find_tuples_without_negatives([(1,), (-1,)]) == [(1,)]
    assert find_tuples_without_negatives([(0, 0, 0)]) == [(0, 0, 0)]
    assert find_tuples_without_negatives([(-5, -4, -3)]) == None

# 252. Тесты для функции `find_keys_with_odd_values`:
def test_find_keys_with_odd_values():
    assert find_keys_with_odd_values({1: 2, 3: 4, 5: 6}) == None
    assert find_keys_with_odd_values({1: 1, 3: 3, 5: 5}) == [1, 3, 5]
    assert find_keys_with_odd_values({1: 2, 3: 3, 5: 6}) == [3]
    assert find_keys_with_odd_values({}) == None
    assert find_keys_with_odd_values({1: 2, 2: 4, 3: 6}) == None
    assert find_keys_with_odd_values({1: 3, 2: 5, 3: 7}) == [1, 2, 3]
    assert find_keys_with_odd_values({4: 5, 6: 7}) == [4, 6]
    assert find_keys_with_odd_values({8: 9, 10: 11}) == [8, 10]
    assert find_keys_with_odd_values({12: 13, 14: 15}) == [12, 14]

# 253. Тесты для функции `find_product_of_two_not_divisible_by_2`:
def test_find_product_of_two_not_divisible_by_2():
    assert find_product_of_two_not_divisible_by_2([1, 2, 3, 4, 5]) == [3, 5, 15]
    assert find_product_of_two_not_divisible_by_2([2, 4, 6]) == None
    assert find_product_of_two_not_divisible_by_2([1, 3, 5, 7]) == [3, 5, 7, 15, 21, 35]
    assert find_product_of_two_not_divisible_by_2([0, 1, 2, 3]) == [3]
    assert find_product_of_two_not_divisible_by_2([-1, -3, -5]) == [3, 5, 15]
    assert find_product_of_two_not_divisible_by_2([-2, -4, -6]) == None
    assert find_product_of_two_not_divisible_by_2([1, -1, 3, -3]) == [-1, 3, -3, -3, 3, -9]
    assert find_product_of_two_not_divisible_by_2([1]) == None
    assert find_product_of_two_not_divisible_by_2([2]) == None

# 254. Тесты для функции `find_in_set_not_in_list`:
def test_find_in_set_not_in_list():
    assert find_in_set_not_in_list({1, 2, 3}, [2, 3, 4]) == [1]
    assert find_in_set_not_in_list({1, 2, 3}, [1, 2, 3]) == None
    assert find_in_set_not_in_list({4, 5, 6}, [1, 2, 3]) == [4, 5, 6]
    assert find_in_set_not_in_list({0, 1, 2}, [2, 3, 4]) == [0, 1]
    assert find_in_set_not_in_list({-1, -2, -3}, [-3, -4, -5]) == [-2, -1]
    assert find_in_set_not_in_list({10, 20, 30}, [20, 30, 40]) == [10]
    assert find_in_set_not_in_list({15, 25, 35}, [10, 20, 30]) == [15, 25, 35]
    assert find_in_set_not_in_list({1, 2, 3}, []) == [1, 2, 3]
    assert find_in_set_not_in_list(set(), [1, 2, 3]) == None

# 255. Тесты для функции `find_keys_not_divisible_by_3`:
def test_find_keys_not_divisible_by_3():
    assert find_keys_not_divisible_by_3({1: 'a', 3: 'b', 6: 'c'}) == [1]
    assert find_keys_not_divisible_by_3({3: 'a', 6: 'b', 9: 'c'}) == None
    assert find_keys_not_divisible_by_3({1: 'a', 2: 'b', 4: 'c'}) == [1, 2, 4]
    assert find_keys_not_divisible_by_3({0: 'a', 3: 'b', 6: 'c'}) == None
    assert find_keys_not_divisible_by_3({7: 'a', 8: 'b', 10: 'c'}) == [7, 8, 10]
    assert find_keys_not_divisible_by_3({5: 'a', 7: 'b', 11: 'c'}) == [5, 7, 11]
    assert find_keys_not_divisible_by_3({12: 'a', 15: 'b', 18: 'c'}) == None
    assert find_keys_not_divisible_by_3({2: 'a', 4: 'b', 5: 'c'}) == [2, 4, 5]
    assert find_keys_not_divisible_by_3({11: 'a', 14: 'b', 17: 'c'}) == [11, 14, 17]

# 256. Тесты для функции `find_numbers_with_sum_divisible_by_4`:
def test_find_numbers_with_sum_divisible_by_4():
    assert find_numbers_with_sum_divisible_by_4([1, 2, 3], [4, 5, 6]) == [(2, 6), (3, 5)]
    assert find_numbers_with_sum_divisible_by_4([1, 2, 3], [7, 8, 9]) == [(1, 7), (3, 9)]
    assert find_numbers_with_sum_divisible_by_4([4, 5, 6], [1, 2, 3]) == [(5, 3), (6, 2)]
    assert find_numbers_with_sum_divisible_by_4([0, 1, 2], [2, 3, 4]) == [(0, 4), (1, 3), (2, 2)]
    assert find_numbers_with_sum_divisible_by_4([5, 6, 7], [3, 4, 5]) == [(5, 3), (7, 5)]
    assert find_numbers_with_sum_divisible_by_4([], []) == None
    assert find_numbers_with_sum_divisible_by_4([], [1, 2, 3]) == None
    assert find_numbers_with_sum_divisible_by_4([112, 3, 45], []) == None


# 257. Тесты для функции `find_unique_in_one_list`:
def test_find_unique_in_one_list():
    assert find_unique_in_one_list([1, 2, 3], [3, 4, 5]) == [1, 2, 4, 5]
    assert find_unique_in_one_list([7, 8, 9], [7, 8, 9]) == None
    assert find_unique_in_one_list([10, 20, 30], [30, 40, 50]) == [40, 10, 50, 20]
    assert find_unique_in_one_list([], [1, 2, 3]) == [1, 2, 3]
    assert find_unique_in_one_list([1, 2, 3], []) == [1, 2, 3]
    assert find_unique_in_one_list([-1, -2, -3], [-3, -4, -5]) == [-2, -5, -4, -1]
    assert find_unique_in_one_list([10, 11, 12], [12, 13, 14]) == [10, 11, 13, 14]
    assert find_unique_in_one_list([15, 16, 17], [18, 19, 20]) == [15, 16, 17, 18, 19, 20]

# 258. Тесты для функции `find_pairs_with_sum_divisible_by_5`:
def test_find_pairs_with_sum_divisible_by_5():
    assert find_pairs_with_sum_divisible_by_5([1, 2, 3]) == [(2, 3), (3, 2)]
    assert find_pairs_with_sum_divisible_by_5([3, 1, 4]) == [(1, 4), (4, 1)]
    assert find_pairs_with_sum_divisible_by_5([7, 2, 5, 0]) == [(5, 5), (5, 0), (0, 5), (0, 0)]
    assert find_pairs_with_sum_divisible_by_5([-2, -4]) == None
    assert find_pairs_with_sum_divisible_by_5([1, 21, 7]) == None
    assert find_pairs_with_sum_divisible_by_5([2, 7, 9]) == None

# 259. Тесты для функции `find_tuples_without_even_numbers`:
def test_find_tuples_without_even_numbers():
    assert find_tuples_without_even_numbers([(1, 3, 5), (2, 4, 6), (7, 9, 11)]) == [(1, 3, 5), (7, 9, 11)]
    assert find_tuples_without_even_numbers([(1, 2), (3, 4), (5, 6)]) == None
    assert find_tuples_without_even_numbers([(1, 3), (5, 7), (9, 11)]) == [(1, 3), (5, 7), (9, 11)]
    assert find_tuples_without_even_numbers([(0, 2, 4), (6, 8, 10)]) == None
    assert find_tuples_without_even_numbers([(1, 3, 5)]) == [(1, 3, 5)]
    assert find_tuples_without_even_numbers([(-1, -3), (-5, -7)]) == [(-1, -3), (-5, -7)]
    assert find_tuples_without_even_numbers([(-2, -4), (-6, -8)]) == None
    assert find_tuples_without_even_numbers([(5, -5), (7, -7)]) == [(5, -5), (7, -7)]
    assert find_tuples_without_even_numbers([(1,), (3,)]) == [(1,), (3,)]

# 260. Тесты для функции `find_integers_in_strings`:
def test_find_integers_in_strings():
    assert find_integers_in_strings(['1', '2', '3']) == [1, 2, 3]
    assert find_integers_in_strings(['a', 'b', 'c']) == None
    assert find_integers_in_strings(['1', 'b', '3']) == [1, 3]
    assert find_integers_in_strings(['123', '456', '789']) == [123, 456, 789]
    assert find_integers_in_strings(['1a', 'b2', '3c']) == None
    assert find_integers_in_strings(['']) == None
    assert find_integers_in_strings(['1', '0', '-3']) == [1, 0, -3]
    assert find_integers_in_strings(['0']) == [0]
    assert find_integers_in_strings(['-1', '-2', '-3']) == [-1, -2, -3]
