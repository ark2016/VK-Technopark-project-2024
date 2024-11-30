import pytest
from functions.file_181_200 import *


# 181. Тесты для функции `find_difference_of_two_squares`:
def test_find_difference_of_two_squares():
    assert find_difference_of_two_squares([1, 7, 8]) == [8]
    assert find_difference_of_two_squares([14, 15, 17]) == [15]
    assert find_difference_of_two_squares([2, 3, 5]) == [3, 5]
    assert find_difference_of_two_squares([16, 24, 35]) == [16, 24, 35]
    assert find_difference_of_two_squares([16, 24, 35]) == [16, 24, 35]
    assert find_difference_of_two_squares([]) == "No numbers found that are the difference of two squares."


# 182. Тесты для функции `find_sum_of_two_divisible_by_3`:
def test_find_sum_of_two_divisible_by_3():
    assert find_sum_of_two_divisible_by_3([6, 15, 21]) == [6, 15, 21]
    assert find_sum_of_two_divisible_by_3([5, 7, 11]) == "No numbers found that are the sum of two numbers divisible by 3."
    assert find_sum_of_two_divisible_by_3([9, 18, 30]) == [9, 18, 30]
    assert find_sum_of_two_divisible_by_3([1, 2, 4]) == "No numbers found that are the sum of two numbers divisible by 3."


# 183. Тесты для функции `find_not_even_but_divisible_by_9`:
def test_find_not_even_but_divisible_by_9():
    assert find_not_even_but_divisible_by_9([9, 27, 45]) == [9, 27, 45]
    assert find_not_even_but_divisible_by_9([2, 4, 6]) == "No numbers found that are not even but divisible by 9."
    assert find_not_even_but_divisible_by_9([15, 33, 81]) == [81]
    assert find_not_even_but_divisible_by_9([12, 18, 24]) == "No numbers found that are not even but divisible by 9."


# 184. Тесты для функции `find_odd_and_divisible_by_4`:
def test_find_divisible_by_2():
    assert find_divisible_by_2([4, 16, 28]) ==  'No numbers.'
    assert find_divisible_by_2([1, 3, 5]) == 'No numbers.'
    assert find_divisible_by_2([20, 22, 32]) == [22]
    assert find_divisible_by_2([6, 7, 10]) == [6, 10]


# 185. Тесты для функции `find_divisible_by_2_or_3_not_6`:
def test_find_divisible_by_2_or_3_not_6():
    assert find_divisible_by_2_or_3_not_6([2, 5, 8]) == [2, 8]
    assert find_divisible_by_2_or_3_not_6([4, 10, 14]) == [4, 10, 14]
    assert find_divisible_by_2_or_3_not_6([6, 12, 24]) == "No numbers found that are divisible by 2 or 3 but not 6."
    assert find_divisible_by_2_or_3_not_6([1, 7, 11]) == "No numbers found that are divisible by 2 or 3 but not 6."


# 186. Тесты для функции `find_divisors_of_12_not_even`:
def test_find_divisors_of_12_not_even():
    assert find_divisors_of_12_not_even([1, 3, 6]) == [1, 3]
    assert find_divisors_of_12_not_even([2, 4, 8]) == "No numbers found that are divisors of 12 but not even."
    assert find_divisors_of_12_not_even([5, 7, 9]) == "No numbers found that are divisors of 12 but not even."
    assert find_divisors_of_12_not_even([12, 18, 24]) == "No numbers found that are divisors of 12 but not even."


# 187. Тесты для функции `find_divisors_of_6_not_12`:
def test_find_divisors_of_6_not_12():
    assert find_divisors_of_6_not_12([1, 3, 6]) == [1, 3, 6]
    assert find_divisors_of_6_not_12([2, 4, 8]) == [2]
    assert find_divisors_of_6_not_12([5, 9, 11]) == "No numbers found that are divisors of 6 but not 12."
    assert find_divisors_of_6_not_12([12, 18, 24]) == "No numbers found that are divisors of 6 but not 12."


# 188. Тесты для функции `find_squares_of_even_numbers`:
def test_find_squares_of_even_numbers():
    assert find_squares_of_even_numbers([4, 16, 36]) == [4, 16, 36]
    assert find_squares_of_even_numbers([9, 25, 49]) == "No squares of even numbers found."
    assert find_squares_of_even_numbers([8, 18, 32]) == "No squares of even numbers found."
    assert find_squares_of_even_numbers([64, 100, 144]) == [64, 100, 144]


# 189. Тесты для функции `find_even_not_powers_of_2`:
def test_find_even_not_powers_of_2():
    assert find_even_not_powers_of_2([2, 3, 6, 9]) == [6]
    assert find_even_not_powers_of_2([4, 8, 16, 32]) == "No even numbers found that are not powers of 2."
    assert find_even_not_powers_of_2([18, 20, 22, 24]) == [18, 20, 22, 24]
    assert find_even_not_powers_of_2([1, 2, 4, 8]) == "No even numbers found that are not powers of 2."


# 190. Тесты для функции `find_not_even_and_not_divisible_by_9`:
def test_find_not_even_and_not_divisible_by_9():
    assert find_not_even_and_not_divisible_by_9([1, 3, 7, 11]) == [1, 3, 7, 11]
    assert find_not_even_and_not_divisible_by_9([2, 4, 8, 16]) == "No numbers found that are neither even nor divisible by 9."
    assert find_not_even_and_not_divisible_by_9([5, 15, 25, 35]) == [5, 15, 25, 35]
    assert find_not_even_and_not_divisible_by_9([18, 27, 36, 45]) == "No numbers found that are neither even nor divisible by 9."


# 191. Тесты для функции `find_multiples_of_3_and_5_not_7`:
def test_find_multiples_of_3_and_5_not_7():
    assert find_multiples_of_3_and_5_not_7([15, 30, 45]) == [15, 30, 45]
    assert find_multiples_of_3_and_5_not_7([21, 42, 63]) == "No numbers found that are divisible by 3 and 5 but not 7."
    assert find_multiples_of_3_and_5_not_7([35, 50, 55]) == "No numbers found that are divisible by 3 and 5 but not 7."
    assert find_multiples_of_3_and_5_not_7([75, 90, 105]) == [75, 90]


# 192. Тесты для функции `find_product_of_two_odd_numbers`:
def test_find_product_of_two_odd_numbers():
    assert find_product_of_two_odd_numbers([9, 15, 25]) == [9, 15, 25]
    assert find_product_of_two_odd_numbers([10, 16, 20]) == None
    assert find_product_of_two_odd_numbers([21, 27, 45]) == [21, 27, 45]
    assert find_product_of_two_odd_numbers([14, 18, 22]) == None


# 193. Тесты для функции `find_product_of_two_primes`:
def test_find_product_of_two_primes():
    assert find_product_of_two_primes([6, 10, 14]) == [6, 10, 14]
    assert find_product_of_two_primes([8, 12, 18]) == None
    assert find_product_of_two_primes([15, 21, 35]) == [15, 21, 35]
    assert find_product_of_two_primes([20, 28, 30]) == None
    assert find_product_of_two_primes([]) == None


# 194. Тесты для функции `find_odd_not_power_of_2`:
def test_find_odd_not_power_of_2():
    assert find_odd_not_power_of_2([1, 3, 7]) == [3, 7]
    assert find_odd_not_power_of_2([2, 4, 8]) == None
    assert find_odd_not_power_of_2([9, 11, 13]) == [9, 11, 13]
    assert find_odd_not_power_of_2([16, 32, 64]) == None


# 195. Тесты для функции `find_divisible_by_6_not_9`:
def test_find_divisible_by_6_not_9():
    assert find_divisible_by_6_not_9([6, 12, 24]) == [6, 12, 24]
    assert find_divisible_by_6_not_9([9, 18, 27]) == None
    assert find_divisible_by_6_not_9([30, 36, 42]) == [30, 42]
    assert find_divisible_by_6_not_9([45, 54, 63]) == None


# 196. Тесты для функции `find_divisors_of_24_not_8`:
def test_find_divisors_of_24_not_8():
    assert find_divisors_of_24_not_8([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert find_divisors_of_24_not_8([8, 16, 24]) == None
    assert find_divisors_of_24_not_8([6, 12, 18]) == [6, 12]
    assert find_divisors_of_24_not_8([5, 10, 15]) == None


# 197. Тесты для функции `find_squares_of_odd_numbers`:
def test_find_squares_of_odd_numbers():
    assert find_squares_of_odd_numbers([9, 25, 49]) == [9, 25, 49]
    assert find_squares_of_odd_numbers([16, 36, 64]) == None
    assert find_squares_of_odd_numbers([81, 121, 169]) == [81, 121, 169]
    assert find_squares_of_odd_numbers([100, 144, 196]) == None


# 198. Тесты для функции `find_powers_of_2_not_even`:
def test_find_powers_of_2_not_even():
    assert find_powers_of_2_not_even([1, 3, 7]) == [1]
    assert find_powers_of_2_not_even([8, 16, 32]) == None
    assert find_powers_of_2_not_even([2, 4, 64]) == None
    assert find_powers_of_2_not_even([128, 256, 512]) == None


# 199. Тесты для функции `find_not_multiples_of_3_but_divisible_by_5`:
def test_find_not_multiples_of_3_but_divisible_by_5():
    assert find_not_multiples_of_3_but_divisible_by_5([5, 10, 20]) == [5, 10, 20]
    assert find_not_multiples_of_3_but_divisible_by_5([9, 15, 21]) == None
    assert find_not_multiples_of_3_but_divisible_by_5([25, 35, 50]) == [25, 35, 50]
    assert find_not_multiples_of_3_but_divisible_by_5([6, 12, 18]) == None


# 200. Тесты для функции `find_divisors_of_15_not_3`:
def test_find_divisors_of_15_not_3():
    assert find_divisors_of_15_not_3([1, 5, 15]) == [1, 5]
    assert find_divisors_of_15_not_3([3, 9, 12]) == None
    assert find_divisors_of_15_not_3([2, 4, 6]) == None
    assert find_divisors_of_15_not_3([7, 11, 13]) == None
