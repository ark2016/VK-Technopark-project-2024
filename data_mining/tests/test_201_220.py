import pytest
from functions.file_201_220 import *


# 201. Тесты для функции `find_powers_of_2_not_multiples_of_4`
def test_find_powers_of_2_not_multiples_of_4():
    assert find_powers_of_2_not_multiples_of_4([1, 2, 3, 4, 8, 16]) == [1, 2]
    assert find_powers_of_2_not_multiples_of_4([32, 64, 128]) == None
    assert find_powers_of_2_not_multiples_of_4([3, 5, 7]) == None
    assert find_powers_of_2_not_multiples_of_4([1024, 256]) == None
    assert find_powers_of_2_not_multiples_of_4([2, 4, 8, 16]) == [2]
    assert find_powers_of_2_not_multiples_of_4([1, 3, 9, 5]) == [1]
    assert find_powers_of_2_not_multiples_of_4([0]) == None


# 202. Тесты для функции `find_odd_not_square`
def test_find_odd_not_square():
    assert find_odd_not_square([1, 2, 3, 5, 7, 9, 10]) == [3, 5, 7]
    assert find_odd_not_square([9, 1, 3, 11]) == [3, 11]
    assert find_odd_not_square([4, 16, 25]) == None
    assert find_odd_not_square([1, 3, 5, 7, 11]) == [3, 5, 7, 11]
    assert find_odd_not_square([25, 49, 81]) == None
    assert find_odd_not_square([4, 16, 64]) == None


# 203. Тесты для функции `find_squares_of_even_not_divisible_by_8`
def test_find_squares_of_even_not_divisible_by_8():
    assert find_squares_of_even_not_divisible_by_8([4, 16, 64, 36, 49]) == [4, 36]
    assert find_squares_of_even_not_divisible_by_8([16, 64, 4, 81]) == [4]
    assert find_squares_of_even_not_divisible_by_8([1, 9, 25]) == None
    assert find_squares_of_even_not_divisible_by_8([100, 144]) == [100]
    assert find_squares_of_even_not_divisible_by_8([64, 256]) == None


# 204. Тесты для функции `find_divisors_of_6_not_2`
def test_find_divisors_of_6_not_2():
    assert find_divisors_of_6_not_2([1, 2, 3, 6]) == [1, 3, 6]
    assert find_divisors_of_6_not_2([6, 9, 12]) == [6]
    assert find_divisors_of_6_not_2([2, 3, 6]) == [3, 6]
    assert find_divisors_of_6_not_2([12, 3]) == [3]
    assert find_divisors_of_6_not_2([8, 10, 6]) == [6]
    assert find_divisors_of_6_not_2([18, 24, 30]) == None


# 205. Тесты для функции `find_divisors_of_48_not_16`
def test_find_divisors_of_48_not_16():
    assert find_divisors_of_48_not_16([1, 2, 3, 4, 6, 8]) == [1, 2, 3, 4, 6, 8]
    assert find_divisors_of_48_not_16([16, 8, 4, 24]) == [8, 4, 24]
    assert find_divisors_of_48_not_16([1, 2, 3, 6, 9]) == [1, 2, 3, 6]
    assert find_divisors_of_48_not_16([16, 48]) == None
    assert find_divisors_of_48_not_16([12, 16, 24]) == [12, 24]


# 206. Тесты для функции `find_divisors_of_20_not_even`
def test_find_divisors_of_20_not_even():
    assert find_divisors_of_20_not_even([1, 2, 5, 10]) == [1, 5]
    assert find_divisors_of_20_not_even([4, 6, 8]) == None
    assert find_divisors_of_20_not_even([5, 15, 30]) == [5]
    assert find_divisors_of_20_not_even([1, 2, 5]) == [1, 5]
    assert find_divisors_of_20_not_even([20, 10]) == None


# 207. Тесты для функции `find_divisible_by_2_not_4_or_8`
def test_find_divisible_by_2_not_4_or_8():
    assert find_divisible_by_2_not_4_or_8([2, 4, 8, 10]) == [2, 10]
    assert find_divisible_by_2_not_4_or_8([2, 6, 10, 14]) == [2, 6, 10, 14]
    assert find_divisible_by_2_not_4_or_8([1, 3, 5]) == None
    assert find_divisible_by_2_not_4_or_8([8, 16, 32]) == None
    assert find_divisible_by_2_not_4_or_8([100]) == None


# 208. Тесты для функции `find_squares_of_odd_not_7`
def test_find_squares_of_odd_not_7():
    assert find_squares_of_odd_not_7([1, 9, 25, 49, 81]) == [1, 9, 25, 81]
    assert find_squares_of_odd_not_7([49, 121, 169]) == [121, 169]
    assert find_squares_of_odd_not_7([64, 256]) == None
    assert find_squares_of_odd_not_7([49, 121, 169]) == [121, 169]
    assert find_squares_of_odd_not_7([81, 25]) == [81, 25]


# 209. Тесты для функции `find_divisible_by_5_not_divisible_by_10`
def test_find_divisible_by_5_not_divisible_by_10():
    assert find_divisible_by_5_not_divisible_by_10([5, 10, 15, 20]) == [5, 15]
    assert find_divisible_by_5_not_divisible_by_10([25, 30, 35]) == [25, 35]
    assert find_divisible_by_5_not_divisible_by_10([1, 3, 6]) == None
    assert find_divisible_by_5_not_divisible_by_10([50, 100]) == None
    assert find_divisible_by_5_not_divisible_by_10([5, 15]) == [5, 15]


# 210. Тесты для функции `find_product_of_two_odd_numbers_not_divisible_by_3`
def test_find_product_of_two_odd_numbers_not_divisible_by_3():
    assert find_product_of_two_odd_numbers_not_divisible_by_3([1, 9, 15, 35, 45]) == [35]
    assert find_product_of_two_odd_numbers_not_divisible_by_3([5, 7, 9, 11, 13]) == [5, 7, 11, 13]
    assert find_product_of_two_odd_numbers_not_divisible_by_3([9, 45, 63]) == None
    assert find_product_of_two_odd_numbers_not_divisible_by_3([21, 35]) == [35]
    assert find_product_of_two_odd_numbers_not_divisible_by_3([15, 33]) == None


# 211. Тесты для функции `find_even_not_divisible_by_3`
def test_find_even_not_divisible_by_3():
    assert find_even_not_divisible_by_3([2, 4, 6, 8, 10, 12]) == [2, 4, 8, 10]
    assert find_even_not_divisible_by_3([6, 12, 18]) == None
    assert find_even_not_divisible_by_3([2, 10, 4]) == [2, 10, 4]
    assert find_even_not_divisible_by_3([2, 4, 8]) == [2, 4, 8]
    assert find_even_not_divisible_by_3([18, 24]) == None


# 212. Тесты для функции `find_difference_of_two_even_numbers`
def test_find_difference_of_two_even_numbers():
    assert find_difference_of_two_even_numbers([4, 6, 8, 10, 12]) == [4, 6, 8, 10, 12]
    assert find_difference_of_two_even_numbers([2, 4, 6, 8]) == [4, 6, 8]
    assert find_difference_of_two_even_numbers([1, 3, 5]) == None
    assert find_difference_of_two_even_numbers([14, 18, 20]) == [14, 18, 20]
    assert find_difference_of_two_even_numbers([2, 6, 10]) == [6, 10]


# 213. Тесты для функции `find_divisors_of_18_not_9`
def test_find_divisors_of_18_not_9():
    assert find_divisors_of_18_not_9([1, 2, 3, 6]) == [1, 2, 3, 6]
    assert find_divisors_of_18_not_9([9, 12, 15]) == None
    assert find_divisors_of_18_not_9([18, 3, 6]) == [3, 6]
    assert find_divisors_of_18_not_9([1, 3, 9]) == [1, 3]
    assert find_divisors_of_18_not_9([6, 18]) == [6]


# 214. Тесты для функции `find_multiples_of_3_and_5_not_15` фиксит
def test_find_multiples_of_3_and_5_not_15():
    assert find_multiples_of_3_and_5_not_15([3, 5, 15, 30, 45]) == [3, 5, 15, 30, 45]
    assert find_multiples_of_3_and_5_not_15([4, 11, 7, 8]) == None
    assert find_multiples_of_3_and_5_not_15([6, 30, 60]) == [6, 30, 60]
    assert find_multiples_of_3_and_5_not_15([3, 15, 30]) == [3, 15, 30]
    assert find_multiples_of_3_and_5_not_15([45, 60]) == [45, 60]


# 215. Тесты для функции `find_product_of_two_primes_not_divisible_by_11`
def test_find_product_of_two_primes_not_divisible_by_11():
    assert find_product_of_two_primes_not_divisible_by_11([6, 15, 35, 55]) == [6, 15, 35]
    assert find_product_of_two_primes_not_divisible_by_11([2, 3, 5, 7]) == None
    assert find_product_of_two_primes_not_divisible_by_11([11, 22]) == None
    assert find_product_of_two_primes_not_divisible_by_11([6, 33]) == [6]
    assert find_product_of_two_primes_not_divisible_by_11([6, 15, 35]) == [6, 15, 35]
    assert find_product_of_two_primes_not_divisible_by_11([6, 625, 342]) == [6]


# 216. Тесты для функции `find_squares_of_even_not_divisible_by_4`
def test_find_squares_of_even_not_divisible_by_4():
    assert find_squares_of_even_not_divisible_by_4([4, 16, 36, 64, 100]) == None
    assert find_squares_of_even_not_divisible_by_4([64, 16, 4]) == None
    assert find_squares_of_even_not_divisible_by_4([25, 49, 121]) == [25, 49, 121]
    assert find_squares_of_even_not_divisible_by_4([144]) == None
    assert find_squares_of_even_not_divisible_by_4([2, 4, 6]) == [6]


# 217. Тесты для функции `find_multiples_of_5_and_6_not_10`
def test_find_multiples_of_5_and_6_not_10():
    assert find_multiples_of_5_and_6_not_10([30, 60, 90, 120]) == None
    assert find_multiples_of_5_and_6_not_10([10, 15, 25]) == [15, 25]
    assert find_multiples_of_5_and_6_not_10([30, 50, 75]) == [75]
    assert find_multiples_of_5_and_6_not_10([5, 6, 15]) == [5, 6, 15]
    assert find_multiples_of_5_and_6_not_10([90]) == None


# 218. Тесты для функции `find_difference_of_two_even_not_divisible_by_4`
def test_find_difference_of_two_even_not_divisible_by_4():
    assert find_difference_of_two_even_not_divisible_by_4([4, 8, 12, 16]) == None
    assert find_difference_of_two_even_not_divisible_by_4([10, 14, 18]) == [10, 14, 18]
    assert find_difference_of_two_even_not_divisible_by_4([2, 4, 6]) == [6]
    assert find_difference_of_two_even_not_divisible_by_4([24, 28, 32]) == None
    assert find_difference_of_two_even_not_divisible_by_4([10, 20]) == [10]


# 219. Тесты для функции `find_product_of_two_primes_not_7`
def test_find_product_of_two_primes_not_7():
    assert find_product_of_two_primes_not_7([6, 10, 14, 15]) == [6, 10, 15]
    assert find_product_of_two_primes_not_7([5, 13, 17]) == None
    assert find_product_of_two_primes_not_7([7, 11]) == None
    assert find_product_of_two_primes_not_7([6, 15, 21]) == [6, 15]
    assert find_product_of_two_primes_not_7([3, 5, 15]) == [15]
    assert find_product_of_two_primes_not_7([3, 270, 150]) == None


# 220. Тесты для функции `find_difference_of_two_odd`
def test_find_difference_of_two_odd():
    assert find_difference_of_two_odd([5, 7, 9, 11]) == [5, 7, 9, 11]
    assert find_difference_of_two_odd([1, 3, 5, 7]) == [3, 5, 7]
    assert find_difference_of_two_odd([3, 9, 15]) == [3, 9, 15]
    assert find_difference_of_two_odd([5, 15, 25]) == [5, 15, 25]
    assert find_difference_of_two_odd([1, 1, 1]) == None
    assert find_difference_of_two_odd([]) == None
