import pytest
from functions.file_221_240 import *


# 221. Тесты для функции `find_product_of_two_odd_not_5`:
def test_find_product_of_two_odd_not_5():
    assert find_product_of_two_odd_not_5([15, 21, 35, 45]) == [21]
    assert find_product_of_two_odd_not_5([10, 5, 7, 9]) == [7, 9]
    assert find_product_of_two_odd_not_5([27, 49, 77, 99]) == [27, 49, 77, 99]
    assert find_product_of_two_odd_not_5([]) == None
    assert find_product_of_two_odd_not_5([9, 25, 49, 63]) == [9, 49, 63]
    assert find_product_of_two_odd_not_5([1, 1, 1, 1, 1, 1]) == None


# 222. Тесты для функции `find_divisors_of_36_not_9`:
def test_find_divisors_of_36_not_9():
    assert find_divisors_of_36_not_9([1, 2, 3, 4, 6, 9, 12, 18]) == [1, 2, 3, 4, 6, 12]
    assert find_divisors_of_36_not_9([5, 7, 10]) == None
    assert find_divisors_of_36_not_9([36, 6, 4]) == [6, 4]
    assert find_divisors_of_36_not_9([18, 3, 9]) == [3]
    assert find_divisors_of_36_not_9([8, 2, 6]) == [2, 6]
    assert find_divisors_of_36_not_9([1, 36, 12, 2]) == [1, 12, 2]


# 223. Тесты для функции `find_odd_and_divisible_by_5_not_10`:
def test_find_odd_and_divisible_by_5_not_10():
    assert find_odd_and_divisible_by_5_not_10([5, 15, 25, 35, 10]) == [5, 15, 25, 35]
    assert find_odd_and_divisible_by_5_not_10([5, 10, 20]) == [5]
    assert find_odd_and_divisible_by_5_not_10([35, 55, 75]) == [35, 55, 75]
    assert find_odd_and_divisible_by_5_not_10([10, 30, 50]) == None
    assert find_odd_and_divisible_by_5_not_10([25, 15, 5]) == [25, 15, 5]
    assert find_odd_and_divisible_by_5_not_10([35, 45, 100, 90]) == [35, 45]


# 224. Тесты для функции `find_divisible_by_6`:
def test_find_divisible_by_6():
    assert find_divisible_by_6([6, 12, 18, 24, 36]) == [6, 12, 18, 24, 36]
    assert find_divisible_by_6([3, 6, 9, 12]) == [6, 12]
    assert find_divisible_by_6([36, 42, 48]) == [36, 42, 48]
    assert find_divisible_by_6([54, 60, 72]) == [54, 60, 72]
    assert find_divisible_by_6([5, 10, 79]) == None
    assert find_divisible_by_6([9, 18, 72]) == [18, 72]


# 225. Тесты для функции `find_divisors_of_30_not_5`:
def test_find_divisors_of_30_not_5():
    assert find_divisors_of_30_not_5([1, 2, 3, 5, 6, 10, 15, 30]) == [1, 2, 3, 6]
    assert find_divisors_of_30_not_5([7, 11, 13]) == None
    assert find_divisors_of_30_not_5([30, 12, 6]) == [6]
    assert find_divisors_of_30_not_5([9, 12, 4]) == None
    assert find_divisors_of_30_not_5([15, 3]) == [3]
    assert find_divisors_of_30_not_5([10, 12, 18]) == None


# 226. Тесты для функции `find_product_of_two_primes_not_6`:
def test_find_product_of_two_primes_not_6():
    assert find_product_of_two_primes_not_6([6, 10, 15, 77]) == [10, 15, 77]
    assert find_product_of_two_primes_not_6([2, 3, 5, 7]) == None
    assert find_product_of_two_primes_not_6([21, 35, 77]) == [21, 35, 77]
    assert find_product_of_two_primes_not_6([199, 235, 569]) == [235]
    assert find_product_of_two_primes_not_6([11, 13, 17]) == None
    assert find_product_of_two_primes_not_6([8, 9, 14, 21]) == [9, 14, 21]


# 227. Тесты для функции `find_even_and_divisible_by_7_not_14`:
def test_find_even_and_divisible_by_7():
    assert find_even_and_divisible_by_7([14, 28, 70]) == [14, 28, 70]
    assert find_even_and_divisible_by_7([7, 35, 49]) == None
    assert find_even_and_divisible_by_7([21, 49, 21]) == None
    assert find_even_and_divisible_by_7([12, 24, 42]) == [42]
    assert find_even_and_divisible_by_7([]) == None
    assert find_even_and_divisible_by_7([2, 4, 12, 16]) == None


# 228. Тесты для функции `find_difference_of_two_odd_not_5`:
def test_find_difference_of_two_odd_not_5():
    assert find_difference_of_two_odd_not_5([9, 15, 25, 35]) == [9]
    assert find_difference_of_two_odd_not_5([3, 5, 7, 11]) == [3, 7, 11]
    assert find_difference_of_two_odd_not_5([10, 5, 7, 9]) == [7, 9]
    assert find_difference_of_two_odd_not_5([21, 35, 49]) == [21, 49]
    assert find_difference_of_two_odd_not_5([5, 25]) == None
    assert find_difference_of_two_odd_not_5([15, 25, 35]) == None


# 229. Тесты для функции `find_squares_of_odd_not_divisible_by_5`:
def test_find_squares_of_odd_not_divisible_by_5():
    assert find_squares_of_odd_not_divisible_by_5([1, 9, 25, 49, 81]) == [1, 9, 49, 81]
    assert find_squares_of_odd_not_divisible_by_5([4, 16, 64]) == None
    assert find_squares_of_odd_not_divisible_by_5([25, 49, 121]) == [49, 121]
    assert find_squares_of_odd_not_divisible_by_5([49, 81]) == [49, 81]
    assert find_squares_of_odd_not_divisible_by_5([100, 121, 169]) == [121, 169]
    assert find_squares_of_odd_not_divisible_by_5([64, 169, 81]) == [169, 81]


# 230. Тесты для функции `find_product_of_two_primes_not_divisible_by_3`:
def test_find_product_of_two_primes_not_divisible_by_3():
    assert find_product_of_two_primes_not_divisible_by_3([6, 10, 15, 77]) == [10, 77]
    assert find_product_of_two_primes_not_divisible_by_3([2, 3, 5, 7, 11]) == None
    assert find_product_of_two_primes_not_divisible_by_3([30, 42, 49, 35]) == [49, 35]
    assert find_product_of_two_primes_not_divisible_by_3([10, 14, 26, 77]) == [10, 14, 26, 77]
    assert find_product_of_two_primes_not_divisible_by_3([2, 5, 7, 11, 13]) == None
    assert find_product_of_two_primes_not_divisible_by_3([9, 15, 21]) == None
    assert find_product_of_two_primes_not_divisible_by_3([657, 1234, 6754]) == [1234]


# 231. Тесты для функции `find_divisors_of_40_not_even`:
def test_find_divisors_of_40_not_even():
    assert find_divisors_of_40_not_even([1, 2, 4, 5, 8, 10, 20, 40]) == [1, 5]
    assert find_divisors_of_40_not_even([1, 3, 5, 7, 9, 11]) == [1, 5]
    assert find_divisors_of_40_not_even([5, 3, 1]) == [5, 1]
    assert find_divisors_of_40_not_even([2, 4, 8]) == None
    assert find_divisors_of_40_not_even([5, 1, 20]) == [5, 1]
    assert find_divisors_of_40_not_even([15, 7, 9]) == None


# 232. Тесты для функции `find_difference_of_two_even_not_5`:
def test_find_difference_of_two_even_not_5():
    assert find_difference_of_two_even_not_5([6, 10, 14, 20, 4, 8]) == [6, 14, 4, 8]
    assert find_difference_of_two_even_not_5([2, 4, 6, 8]) == [4, 6, 8]
    assert find_difference_of_two_even_not_5([10, 12, 16, 18]) == [12, 16, 18]
    assert find_difference_of_two_even_not_5([30, 50, 60]) == None
    assert find_difference_of_two_even_not_5([40, 60, 80]) == None
    assert find_difference_of_two_even_not_5([5, 15, 25]) == None


# 233. Тесты для функции `find_product_of_two_odd_not_divisible_by_7`:
def test_find_product_of_two_odd_not_divisible_by_7():
    assert find_product_of_two_odd_not_divisible_by_7([9, 15, 21, 35]) == [9, 15]
    assert find_product_of_two_odd_not_divisible_by_7([7, 11, 13, 25]) == [11, 13, 25]
    assert find_product_of_two_odd_not_divisible_by_7([3, 5, 9, 15]) == [3, 5, 9, 15]
    assert find_product_of_two_odd_not_divisible_by_7([49, 77, 35]) == None
    assert find_product_of_two_odd_not_divisible_by_7([21, 25, 45, 49]) == [25, 45]
    assert find_product_of_two_odd_not_divisible_by_7([5, 15, 30, 45]) == [5, 15, 45]


# 234. Тесты для функции `find_divisible_by_4`:
def test_find_divisible_by_4():
    assert find_divisible_by_4([4, 8, 12, 16, 20, 24]) == [4, 12, 20]
    assert find_divisible_by_4([2, 4, 8, 10, 20]) == [4, 20]
    assert find_divisible_by_4([64, 8, 32]) == None
    assert find_divisible_by_4([6, 10, 14, 22]) == None
    assert find_divisible_by_4([5, 7, 9, 11, 13]) == None
    assert find_divisible_by_4([4, 12]) == [4, 12]


# 235. Тесты для функции `find_squares_of_odd_not_9`:
def test_find_squares_of_odd_not_9():
    assert find_squares_of_odd_not_9([1, 9, 25, 49, 81]) == [1, 25, 49]
    assert find_squares_of_odd_not_9([1, 9, 25]) == [1, 25]
    assert find_squares_of_odd_not_9([9, 81, 729]) == None
    assert find_squares_of_odd_not_9([1, 4, 16]) == [1]
    assert find_squares_of_odd_not_9([1, 25, 49, 81]) == [1, 25, 49]
    assert find_squares_of_odd_not_9([49, 121, 225]) == [49, 121]


# 236. Тесты для функции `find_difference_of_two_primes`:
def test_find_difference_of_two_primes():
    assert find_difference_of_two_primes([10, 15, 20, 23]) == [10, 15, 20]
    assert find_difference_of_two_primes([3, 5, 7, 9]) == [5, 7, 9]
    assert find_difference_of_two_primes([10, 5, 8, 13]) == [10, 5, 8, 13]
    assert find_difference_of_two_primes([2, 7, 11]) == [7]
    assert find_difference_of_two_primes([11, 1030, 1024, 13]) == [1030, 1024, 13]
    assert find_difference_of_two_primes([5, 10, 12]) == [5, 10, 12]
    assert find_difference_of_two_primes([2, 77, 11]) == None


# 237. Тесты для функции `find_product_of_two_primes_not_5`:
def test_find_product_of_two_primes_not_5():
    assert find_product_of_two_primes_not_5([6, 10, 15, 35]) == [6]
    assert find_product_of_two_primes_not_5([15, 25, 35, 77]) == [77]
    assert find_product_of_two_primes_not_5([2, 3, 7, 11]) == None
    assert find_product_of_two_primes_not_5([5, 7, 3]) == None
    assert find_product_of_two_primes_not_5([5, 7, 11, 9]) == [9]
    assert find_product_of_two_primes_not_5([9, 25, 49]) == [9, 49]
    assert find_product_of_two_primes_not_5([4, 6, 8, 9, 14, 21]) == [4, 6, 9, 14, 21]


# 238. Тесты для функции `find_divisible_by_2_and_5_not_10`:
def test_find_divisible_by_2_and_5_not_10():
    assert find_divisible_by_2_and_5_not_10([10, 20, 30, 40]) == None
    assert find_divisible_by_2_and_5_not_10([5, 15, 25]) == [5, 15, 25]
    assert find_divisible_by_2_and_5_not_10([10, 25]) == [25]
    assert find_divisible_by_2_and_5_not_10([5, 50, 75]) == [5, 75]
    assert find_divisible_by_2_and_5_not_10([10, 15, 30]) == [15]
    assert find_divisible_by_2_and_5_not_10([5, 20]) == [5]


# 239. Тесты для функции `find_difference_of_two_even_not_divisible_by_6`:
def test_find_difference_of_two_even_not_divisible_by_6():
    assert find_difference_of_two_even_not_divisible_by_6([6, 12, 20, 30, 40]) == [20, 40]
    assert find_difference_of_two_even_not_divisible_by_6([4, 8, 10]) == [4, 8, 10]
    assert find_difference_of_two_even_not_divisible_by_6([8, 14, 20, 40]) == [8, 14, 20, 40]
    assert find_difference_of_two_even_not_divisible_by_6([6, 8, 10]) == [8, 10]
    assert find_difference_of_two_even_not_divisible_by_6([2, 4, 8]) == [4, 8]
    assert find_difference_of_two_even_not_divisible_by_6([6, 30]) == None


# 240. Тесты для функции `find_product_of_two_odd_not_divisible_by_4`:
def test_find_product_of_two_odd_not_divisible_by_4():
    assert find_product_of_two_odd_not_divisible_by_4([9, 15, 35, 45]) == [9]
    assert find_product_of_two_odd_not_divisible_by_4([3, 7, 11, 13, 17]) == [3, 7, 11, 13, 17]
    assert find_product_of_two_odd_not_divisible_by_4([5, 32, 8]) == None
    assert find_product_of_two_odd_not_divisible_by_4([5, 64, 20]) == None
    assert find_product_of_two_odd_not_divisible_by_4([7, 9, 15]) == [7, 9]
    assert find_product_of_two_odd_not_divisible_by_4([9, 15, 25, 35]) == [9]


