import pytest
from functions.file_161_180 import *


# 161. Тесты для функции `find_primes_not_multiples_of_3`
def test_find_primes_not_multiples_of_3():
    assert find_primes_not_multiples_of_3([2, 3, 5, 6, 7, 9, 11, 12]) == [2, 5, 7, 11]
    assert find_primes_not_multiples_of_3([3, 6, 9, 12, 15]) == []
    assert find_primes_not_multiples_of_3([1, 2, 4, 5, 8, 10, 14]) == [2, 5]
    assert find_primes_not_multiples_of_3([7, 11, 13, 17, 19, 23]) == [7, 11, 13, 17, 19, 23]
    assert find_primes_not_multiples_of_3([]) == []
    assert find_primes_not_multiples_of_3([29, 31, 37, 41]) == [29, 31, 37, 41]
    assert find_primes_not_multiples_of_3([9, 27, 30]) == []
    assert find_primes_not_multiples_of_3([2, 3, 5, 9, 15, 21]) == [2, 5]
    assert find_primes_not_multiples_of_3([4, 6, 8, 10, 12, 14]) == []


# 162. Тесты для функции `find_even_numbers_divisible_by_4`
def test_find_even_numbers_divisible_by_4():
    assert find_even_numbers_divisible_by_4([4, 8, 12, 16, 20, 24]) == [4, 8, 12, 16, 20, 24]
    assert find_even_numbers_divisible_by_4([1, 2, 3, 5, 7, 11]) == []
    assert find_even_numbers_divisible_by_4([4, 5, 6, 7, 8, 9, 10, 11]) == [4, 8]
    assert find_even_numbers_divisible_by_4([32, 48, 64, 80, 96, 112]) == [32, 48, 64, 80, 96, 112]
    assert find_even_numbers_divisible_by_4([]) == []
    assert find_even_numbers_divisible_by_4([12, 14, 18, 20]) == [12, 20]
    assert find_even_numbers_divisible_by_4([3, 5, 7, 9, 11]) == []
    assert find_even_numbers_divisible_by_4([0, 4, 8, 16, 32]) == [0, 4, 8, 16, 32]
    assert find_even_numbers_divisible_by_4([2, 6, 10, 14]) == []


# 163. Тесты для функции `find_non_powers_of_two`
def test_find_non_powers_of_two():
    assert find_non_powers_of_two([1, 2, 3, 4, 5, 6, 7, 8]) == [3, 5, 6, 7]
    assert find_non_powers_of_two([8, 16, 32, 64, 128]) == []
    assert find_non_powers_of_two([3, 5, 6, 7, 10, 12]) == [3, 5, 6, 7, 10, 12]
    assert find_non_powers_of_two([1, 2, 4, 8, 16]) == []
    assert find_non_powers_of_two([]) == []
    assert find_non_powers_of_two([1024, 2048, 4096]) == []
    assert find_non_powers_of_two([1, 2, 4, 6, 8, 12, 18]) == [6, 12, 18]
    assert find_non_powers_of_two([10, 20, 30, 40]) == [10, 20, 30, 40]
    assert find_non_powers_of_two([7, 14, 21, 28]) == [7, 14, 21, 28]


# 164. Тесты для функции `count_numbers_greater_than_average`
def test_count_numbers_greater_than_average():
    assert count_numbers_greater_than_average("1 2 3 4 5 6 7 8 9") == 4
    assert count_numbers_greater_than_average("10 20 30 40 50") == 2
    assert count_numbers_greater_than_average("5 5 5 5") == 0
    assert count_numbers_greater_than_average("100") == 0
    assert count_numbers_greater_than_average("") == 0
    assert count_numbers_greater_than_average("10 15 20 25 30") == 2
    assert count_numbers_greater_than_average("7 14 21 28") == 2
    assert count_numbers_greater_than_average("3 6 9 12 15 18") == 3
    assert count_numbers_greater_than_average("0 1 2 3 4 5 6 7 8 9 10") == 5


# 165. Тесты для функции `find_multiples_of_4_or_5_not_20`
def test_find_multiples_of_4_or_5_not_20():
    assert find_multiples_of_4_or_5_not_20([4, 5, 8, 10, 12, 15, 16, 25, 40]) == [4, 5, 8, 10, 12, 15, 16, 25]
    assert find_multiples_of_4_or_5_not_20([20, 40, 60, 80, 100]) == []
    assert find_multiples_of_4_or_5_not_20([3, 6, 9, 11, 13, 17, 19]) == []
    assert find_multiples_of_4_or_5_not_20([25, 30, 35, 50]) == [25, 30, 35, 50]
    assert find_multiples_of_4_or_5_not_20([]) == []
    assert find_multiples_of_4_or_5_not_20([4, 8, 12, 16, 24]) == [4, 8, 12, 16, 24]
    assert find_multiples_of_4_or_5_not_20([5, 10, 15, 25]) == [5, 10, 15, 25]
    assert find_multiples_of_4_or_5_not_20([1, 2, 3, 7, 11]) == []
    assert find_multiples_of_4_or_5_not_20([9, 27, 33, 45]) == [45]


# 166. Тесты для функции `find_exact_divisors_of_100`
def test_find_exact_divisors_of_100():
    assert find_exact_divisors_of_100([1, 2, 4, 5, 10, 20, 25, 50, 100]) == [1, 2, 4, 5, 10, 20, 25, 50, 100]
    assert find_exact_divisors_of_100([3, 6, 9, 12, 15, 18, 21]) == []
    assert find_exact_divisors_of_100([4, 8, 16, 32, 64]) == [4]
    assert find_exact_divisors_of_100([50, 100]) == [50, 100]
    assert find_exact_divisors_of_100([]) == []
    assert find_exact_divisors_of_100([10, 20, 30, 40]) == [10, 20]
    assert find_exact_divisors_of_100([1, 25, 100]) == [1, 25, 100]
    assert find_exact_divisors_of_100([5, 15, 20]) == [5, 20]
    assert find_exact_divisors_of_100([7, 14, 21, 35, 70]) == []


# 167. Тесты для функции `find_odd_not_divisible_by_5`
def test_find_odd_not_divisible_by_5():
    assert find_odd_not_divisible_by_5([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [1, 3, 7, 9, 11, 13, 17, 19]
    assert find_odd_not_divisible_by_5([5, 10, 15, 20, 25]) == []
    assert find_odd_not_divisible_by_5([2, 4, 6, 8, 10, 12]) == []
    assert find_odd_not_divisible_by_5([1, 2, 3, 4, 5]) == [1, 3]
    assert find_odd_not_divisible_by_5([]) == []
    assert find_odd_not_divisible_by_5([11, 12, 13, 14, 15, 16]) == [11, 13]
    assert find_odd_not_divisible_by_5([1, 21, 31, 41]) == [1, 21, 31, 41]
    assert find_odd_not_divisible_by_5([25, 30, 35, 40, 45, 50]) == []
    assert find_odd_not_divisible_by_5([33, 37, 39, 43, 47]) == [33, 37, 39, 43, 47]


# 168. Тесты для функции `find_multiples_of_2_or_3`
def test_find_multiples_of_2_or_3():
    assert find_multiples_of_2_or_3([2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [2, 3, 4, 8, 9, 10]
    assert find_multiples_of_2_or_3([3, 6, 9, 12, 15, 18, 21]) == [3, 9, 15, 21]
    assert find_multiples_of_2_or_3([2, 4, 6, 8, 10, 12]) == [2, 4, 8, 10]
    assert find_multiples_of_2_or_3([1, 3, 5, 7, 9, 11]) == [3, 9]
    assert find_multiples_of_2_or_3([]) == 'No numbers found that are multiples of 2 or 3, but not both.'
    assert find_multiples_of_2_or_3([6, 12, 18, 24]) == 'No numbers found that are multiples of 2 or 3, but not both.'
    assert find_multiples_of_2_or_3([3, 6, 7, 9, 14]) == [3, 9, 14]
    assert find_multiples_of_2_or_3([2, 3, 5, 7]) == [2, 3]
    assert find_multiples_of_2_or_3([5, 10, 15, 20, 25, 30]) == [10, 15, 20]


# 169. Тесты для функции `find_odd_or_divisible_by_4`
def test_find_odd_or_divisible_by_4():
    assert find_odd_or_divisible_by_4([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 4, 5, 7, 8, 9]
    assert find_odd_or_divisible_by_4([2, 4, 6, 8, 10]) == [4, 8]
    assert find_odd_or_divisible_by_4([1, 3, 5, 7, 9, 11, 13, 15]) == [1, 3, 5, 7, 9, 11, 13, 15]
    assert find_odd_or_divisible_by_4([4, 8, 12, 16, 20]) == [4, 8, 12, 16, 20]
    assert find_odd_or_divisible_by_4([]) == 'No odd numbers or numbers divisible by 4 found.'
    assert find_odd_or_divisible_by_4([3, 5, 6, 7]) == [3, 5, 7]
    assert find_odd_or_divisible_by_4([10, 12, 14, 16]) == [12, 16]
    assert find_odd_or_divisible_by_4([2, 3, 4, 5]) == [3, 4, 5]
    assert find_odd_or_divisible_by_4([9, 10, 12, 15]) == [9, 12, 15]


# 170. Тесты для функции `find_even_squares`
def test_find_even_squares():
    assert find_even_squares([4, 16, 25, 36, 49, 64, 81, 100]) == [4, 16, 36, 64, 100]
    assert find_even_squares([1, 3, 5, 7, 9]) == 'No even square numbers found.'
    assert find_even_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [4]
    assert find_even_squares([9, 25, 49, 81, 121]) == 'No even square numbers found.'
    assert find_even_squares([]) == 'No even square numbers found.'
    assert find_even_squares([0, 4, 8, 12]) == [0, 4]
    assert find_even_squares([2, 6, 8, 10, 14, 18]) == 'No even square numbers found.'
    assert find_even_squares([4, 5, 6, 7, 8, 9]) == [4]
    assert find_even_squares([4, 16, 36, 64]) == [4, 16, 36, 64]


# 171. Тесты для функции `find_multiples_of_3_or_5_not_both`
def test_find_multiples_of_3_or_5_not_both():
    assert find_multiples_of_3_or_5_not_both([3, 5, 6, 10, 15, 18, 20]) == [3, 5, 6, 10, 18, 20]
    assert find_multiples_of_3_or_5_not_both([15, 30, 45, 60]) == 'No numbers found that are multiples of 3 or 5 but not both.'
    assert find_multiples_of_3_or_5_not_both([1, 2, 4, 7]) == 'No numbers found that are multiples of 3 or 5 but not both.'
    assert find_multiples_of_3_or_5_not_both([3, 6, 9, 12, 18]) == [3, 6, 9, 12, 18]
    assert find_multiples_of_3_or_5_not_both([]) == 'No numbers found that are multiples of 3 or 5 but not both.'
    assert find_multiples_of_3_or_5_not_both([5, 10, 20, 25]) == [5, 10, 20, 25]
    assert find_multiples_of_3_or_5_not_both([7, 11, 13]) == 'No numbers found that are multiples of 3 or 5 but not both.'
    assert find_multiples_of_3_or_5_not_both([2, 4, 8, 16]) == 'No numbers found that are multiples of 3 or 5 but not both.'
    assert find_multiples_of_3_or_5_not_both([15, 25, 35, 45]) == [25, 35]


# 172. Тесты для функции `count_numbers_greater_than_mean`
def test_count_numbers_greater_than_mean():
    assert count_numbers_greater_than_mean("1 2 3 4 5") == 2
    assert count_numbers_greater_than_mean("10 20 30 40") == 2
    assert count_numbers_greater_than_mean("5 5 5 5 5") == "No numbers greater than the mean."
    assert count_numbers_greater_than_mean("100") == "No numbers greater than the mean."
    assert count_numbers_greater_than_mean("") == "No numbers found in the string."
    assert count_numbers_greater_than_mean("10 20 30") == 1
    assert count_numbers_greater_than_mean("1 1 1 1 1 2 2 2 2 2") == 5
    assert count_numbers_greater_than_mean("50 100 150 200") == 2
    assert count_numbers_greater_than_mean("6 7 8 9 10") == 2


# 173. Тесты для функции `find_powers_of_2`
def test_find_powers_of_2():
    assert find_powers_of_2([1, 2, 3, 4, 5, 8, 16, 32, 64]) == [1, 2, 4, 8, 16, 32, 64]
    assert find_powers_of_2([7, 14, 21, 28]) == 'No powers of 2 found.'
    assert find_powers_of_2([2, 3, 6, 7, 9, 12]) == [2]
    assert find_powers_of_2([]) == 'No powers of 2 found.'
    assert find_powers_of_2([1024, 2048, 4096]) == [1024, 2048, 4096]
    assert find_powers_of_2([1, 4, 8, 16, 32]) == [1, 4, 8, 16, 32]
    assert find_powers_of_2([1, 2, 3, 4, 6, 7]) == [1, 2, 4]
    assert find_powers_of_2([5, 10, 20, 40]) == 'No powers of 2 found.'
    assert find_powers_of_2([64, 128, 256, 512]) == [64, 128, 256, 512]


# 174. Тесты для функции `find_even_and_divisible_by_8`
def test_find_even_and_divisible_by_8():
    assert find_even_and_divisible_by_8([8, 16, 24, 32, 40, 48, 56, 64]) == [8, 16, 24, 32, 40, 48, 56, 64]
    assert find_even_and_divisible_by_8([7, 14, 21, 28]) == 'No even numbers divisible by 8 found.'
    assert find_even_and_divisible_by_8([2, 4, 6, 10, 12, 14]) == 'No even numbers divisible by 8 found.'
    assert find_even_and_divisible_by_8([8, 16, 32, 40]) == [8, 16, 32, 40]
    assert find_even_and_divisible_by_8([]) == 'No even numbers divisible by 8 found.'
    assert find_even_and_divisible_by_8([80, 96, 112]) == [80, 96, 112]
    assert find_even_and_divisible_by_8([1, 3, 5, 7]) == 'No even numbers divisible by 8 found.'
    assert find_even_and_divisible_by_8([0, 8, 16, 24]) == [0, 8, 16, 24]
    assert find_even_and_divisible_by_8([9, 18, 27, 36]) == 'No even numbers divisible by 8 found.'


# 175. Тесты для функции `find_odd_and_divisible_by_3`
def test_find_odd_and_divisible_by_3():
    assert find_odd_and_divisible_by_3([3, 6, 9, 12, 15, 18, 21, 24]) == [3, 9, 15, 21]
    assert find_odd_and_divisible_by_3([2, 4, 6, 8, 10, 12]) == 'No odd numbers divisible by 3 found.'
    assert find_odd_and_divisible_by_3([5, 10, 15, 20, 25, 30]) == [15]
    assert find_odd_and_divisible_by_3([1, 2, 3, 4, 5]) == [3]
    assert find_odd_and_divisible_by_3([]) == 'No odd numbers divisible by 3 found.'
    assert find_odd_and_divisible_by_3([9, 18, 27, 36]) == [9, 27]
    assert find_odd_and_divisible_by_3([3, 5, 7, 11, 13, 15]) == [3, 15]
    assert find_odd_and_divisible_by_3([21, 33, 45, 57]) == [21, 33, 45, 57]
    assert find_odd_and_divisible_by_3([8, 16, 32, 64]) == 'No odd numbers divisible by 3 found.'


# 176. Тесты для функции `find_non_even_or_not_multiples_of_7`
def test_find_non_even_or_not_multiples_of_7():
    assert find_non_even_or_not_multiples_of_7([2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3, 4, 5, 6, 7, 8, 9]
    assert find_non_even_or_not_multiples_of_7([7, 14, 21, 28]) == [7, 21]
    assert find_non_even_or_not_multiples_of_7([1, 2, 4, 8, 16, 32]) == [1, 2, 4, 8, 16, 32]
    assert find_non_even_or_not_multiples_of_7([2, 3, 5, 7]) == [2, 3, 5, 7]
    assert find_non_even_or_not_multiples_of_7([0, 7, 14, 21]) == [7, 21]
    assert find_non_even_or_not_multiples_of_7([9, 18, 27, 36]) == [9, 18, 27, 36]
    assert find_non_even_or_not_multiples_of_7([3, 7, 10, 13]) == [3, 7, 10, 13]
    assert find_non_even_or_not_multiples_of_7([2, 6, 14, 28]) == [2, 6]
    assert find_non_even_or_not_multiples_of_7([5, 10, 20, 25]) == [5, 10, 20, 25]
    assert find_non_even_or_not_multiples_of_7([28, 14]) == "No numbers found that are not even or not divisible by 7."


# 177. Тесты для функции `find_not_divisible_by_2_but_divisible_by_5`
def test_find_not_divisible_by_2_but_divisible_by_5():
    assert find_not_divisible_by_2_but_divisible_by_5([5, 10, 15, 20, 25, 30]) == [5, 15, 25]
    assert find_not_divisible_by_2_but_divisible_by_5([2, 4, 6, 8, 10]) == 'No numbers found that are not divisible by 2 but divisible by 5.'
    assert find_not_divisible_by_2_but_divisible_by_5([1, 2, 3, 4, 5]) == [5]
    assert find_not_divisible_by_2_but_divisible_by_5([11, 13, 15, 17]) == [15]
    assert find_not_divisible_by_2_but_divisible_by_5([]) == 'No numbers found that are not divisible by 2 but divisible by 5.'
    assert find_not_divisible_by_2_but_divisible_by_5([21, 25, 29]) == [25]
    assert find_not_divisible_by_2_but_divisible_by_5([30, 35, 40, 45]) == [35, 45]
    assert find_not_divisible_by_2_but_divisible_by_5([7, 14, 21, 28]) == 'No numbers found that are not divisible by 2 but divisible by 5.'
    assert find_not_divisible_by_2_but_divisible_by_5([50, 75, 95]) == [75, 95]


# 178. Тесты для функции `find_multiples_of_3_5_or_7`
def test_find_multiples_of_3_5_or_7():
    assert find_multiples_of_3_5_or_7([3, 5, 7, 9, 10, 14, 15, 21, 25, 30]) == [3, 5, 7, 9, 10, 14, 15, 21, 25, 30]
    assert find_multiples_of_3_5_or_7([1, 2, 4, 8, 11]) == 'No numbers found that are multiples of 3, 5, or 7.'
    assert find_multiples_of_3_5_or_7([3, 6, 12, 18]) == [3, 6, 12, 18]
    assert find_multiples_of_3_5_or_7([5, 10, 20, 25]) == [5, 10, 20, 25]
    assert find_multiples_of_3_5_or_7([7, 14, 28, 35]) == [7, 14, 28, 35]
    assert find_multiples_of_3_5_or_7([]) == 'No numbers found that are multiples of 3, 5, or 7.'
    assert find_multiples_of_3_5_or_7([9, 15, 21, 27, 33]) == [9, 15, 21, 27, 33]
    assert find_multiples_of_3_5_or_7([35, 45, 55, 65]) == [35, 45, 55, 65]
    assert find_multiples_of_3_5_or_7([50, 75, 100]) == [50, 75, 100]


# 179. Тесты для функции `find_even_not_divisible_by_4`
def test_find_even_not_divisible_by_4():
    assert find_even_not_divisible_by_4([2, 3, 4, 6, 8, 10, 12, 14, 16]) == [2, 6, 10, 14]
    assert find_even_not_divisible_by_4([4, 8, 12, 16, 20]) == 'No even numbers found that are not divisible by 4.'
    assert find_even_not_divisible_by_4([1, 3, 5, 7, 9]) == 'No even numbers found that are not divisible by 4.'
    assert find_even_not_divisible_by_4([10, 20, 30, 40]) == [10, 30]
    assert find_even_not_divisible_by_4([]) == 'No even numbers found that are not divisible by 4.'
    assert find_even_not_divisible_by_4([6, 18, 26]) == [6, 18, 26]
    assert find_even_not_divisible_by_4([14, 28, 44, 52]) == [14]
    assert find_even_not_divisible_by_4([32, 36, 48, 60]) == 'No even numbers found that are not divisible by 4.'
    assert find_even_not_divisible_by_4([22, 26, 38]) == [22, 26, 38]


# 180. Тесты для функции `find_multiples_of_3_or_5_not_15`
def test_find_multiples_of_3_or_5_not_15():
    assert find_multiples_of_3_or_5_not_15([3, 5, 9, 10, 12, 18, 20, 30, 33]) == [3, 5, 9, 10, 12, 18, 20, 33]
    assert find_multiples_of_3_or_5_not_15([15, 30, 45, 60]) == 'No numbers found that are multiples of 3 or 5 but not 15.'
    assert find_multiples_of_3_or_5_not_15([1, 2, 4, 7, 11]) == 'No numbers found that are multiples of 3 or 5 but not 15.'
    assert find_multiples_of_3_or_5_not_15([5, 10, 20, 25]) == [5, 10, 20, 25]
    assert find_multiples_of_3_or_5_not_15([3, 6, 9, 12]) == [3, 6, 9, 12]
    assert find_multiples_of_3_or_5_not_15([]) == 'No numbers found that are multiples of 3 or 5 but not 15.'
    assert find_multiples_of_3_or_5_not_15([27, 33, 39]) == [27, 33, 39]
    assert find_multiples_of_3_or_5_not_15([5, 25, 35]) == [5, 25, 35]
    assert find_multiples_of_3_or_5_not_15([9, 21, 27, 39]) == [9, 21, 27, 39]
