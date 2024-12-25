import pytest
from functions.file_81_100 import *


# 81. Тесты для функции `is_palindrome_1`:
def test_is_palindrome_1():
    assert is_palindrome_1("A man, a plan, a canal, Panama") == True
    assert is_palindrome_1("No lemon, no melon") == True
    assert is_palindrome_1("Hello, World!") == False
    assert is_palindrome_1("Madam") == True
    assert is_palindrome_1("") == True
    assert is_palindrome_1("12321") == True
    assert is_palindrome_1("12345") == False
    assert is_palindrome_1("Was it a car or a cat I saw?") == True
    assert is_palindrome_1("Not a palindrome") == False


# 82. Тесты для функции `largest_divisor_less_than`:
def test_largest_divisor_less_than():
    assert largest_divisor_less_than(10) == 5
    assert largest_divisor_less_than(15) == 5
    assert largest_divisor_less_than(1) == None
    assert largest_divisor_less_than(2) == None
    assert largest_divisor_less_than(3) == None
    assert largest_divisor_less_than(25) == 5
    assert largest_divisor_less_than(100) == 50
    assert largest_divisor_less_than(49) == 7
    assert largest_divisor_less_than(97) == None
    assert largest_divisor_less_than(11) == None


# 83. Тесты для функции `non_prime_numbers`:
def test_non_prime_numbers():
    assert non_prime_numbers([2, 3, 4, 5, 6]) == [4, 6]
    assert non_prime_numbers([11, 13, 17, 19, 23]) == []
    assert non_prime_numbers([8, 12, 15]) == [8, 12, 15]
    assert non_prime_numbers([1, 2, 3, 5, 7]) == [1]
    assert non_prime_numbers([4, 6, 8, 9, 10]) == [4, 6, 8, 9, 10]
    assert non_prime_numbers([25, 26, 27]) == [25, 26, 27]
    assert non_prime_numbers([16, 18, 20]) == [16, 18, 20]
    assert non_prime_numbers([22, 24, 28]) == [22, 24, 28]
    assert non_prime_numbers([31, 33, 35]) == [33, 35]


# 84. Тесты для функции `max_digit_in_string`:
def test_max_digit_in_string():
    assert max_digit_in_string("1234567890") == 9
    assert max_digit_in_string("5555") == 5
    assert max_digit_in_string("1029384756") == 9
    assert max_digit_in_string("9081726354") == 9
    assert max_digit_in_string("") == None
    assert max_digit_in_string("a1b2c3") == None
    assert max_digit_in_string("7654321") == 7
    assert max_digit_in_string("0000") == 0
    assert max_digit_in_string("2468") == 8


# 85. Тесты для функции `largest_square`:
def test_largest_square():
    assert largest_square([1, 4, 9, 16, 25]) == 25
    assert largest_square([3, 6, 8, 10]) == None
    assert largest_square([4, 16, 25, 36]) == 36
    assert largest_square([0, 1, 2, 3]) == 1
    assert largest_square([49, 64, 81]) == 81
    assert largest_square([10, 20, 30]) == None
    assert largest_square([5, 12, 13]) == None
    assert largest_square([100, 121, 144]) == 144
    assert largest_square([9, 25, 49]) == 49


# 86. Тесты для функции `sum_of_two_squares`:
def test_sum_of_two_squares():
    assert sum_of_two_squares([5, 10, 13, 18]) == [5, 10, 13, 18]
    assert sum_of_two_squares([2, 3, 7, 8]) == [2, 8]
    assert sum_of_two_squares([1, 4, 9, 16]) == [1, 4, 9, 16]
    assert sum_of_two_squares([6, 11, 15, 20]) == [20]
    assert sum_of_two_squares([17, 29, 37]) == [17, 29, 37]
    assert sum_of_two_squares([49, 64, 81]) == [49, 64, 81]
    assert sum_of_two_squares([3, 5, 7, 12]) == [5]
    assert sum_of_two_squares([50, 73, 90]) == [50, 73, 90]
    assert sum_of_two_squares([25, 41, 60]) == [25, 41]


# 87. Тесты для функции `sum_of_digits_in_string`:
def test_sum_of_digits_in_string():
    assert sum_of_digits_in_string("123abc456") == 21
    assert sum_of_digits_in_string("789xyz") == 24
    assert sum_of_digits_in_string("0") == 0
    assert sum_of_digits_in_string("abc") == 0
    assert sum_of_digits_in_string("555") == 15
    assert sum_of_digits_in_string("12a34b56c") == 21
    assert sum_of_digits_in_string("111") == 3
    assert sum_of_digits_in_string("909") == 18
    assert sum_of_digits_in_string("246") == 12


# 88. Тесты для функции `elements_less_than_mean`:
def test_elements_less_than_mean():
    assert elements_less_than_mean([1, 2, 3, 4, 5]) == [1, 2]
    assert elements_less_than_mean([10, 20, 30, 40, 50]) == [10, 20]
    assert elements_less_than_mean([5, 6, 7, 8, 9]) == [5, 6]
    assert elements_less_than_mean([]) == []
    assert elements_less_than_mean([3, 3, 3, 3, 3]) == []
    assert elements_less_than_mean([2, 3, 5, 7, 11]) == [2, 3, 5]
    assert elements_less_than_mean([12, 14, 16, 18]) == [12, 14]
    assert elements_less_than_mean([8, 10, 12]) == [8]
    assert elements_less_than_mean([1, 4, 9, 16]) == [1, 4]


# 89. Тесты для функции `extract_numbers_from_string`:
def test_extract_numbers_from_string():
    assert extract_numbers_from_string("1 2 3 a b c 4 5 6") == [1, 2, 3, 4, 5, 6]
    assert extract_numbers_from_string("7 8 9 x y z") == [7, 8, 9]
    assert extract_numbers_from_string("No numbers here") == []
    assert extract_numbers_from_string("10 20 30 40") == [10, 20, 30, 40]
    assert extract_numbers_from_string("123abc456") == []
    assert extract_numbers_from_string("0 1 2 3") == [0, 1, 2, 3]
    assert extract_numbers_from_string("Only numbers 0 100") == [0, 100]
    assert extract_numbers_from_string("255 512 1024") == [255, 512, 1024]
    assert extract_numbers_from_string("5 15 25") == [5, 15, 25]


# 90. Тесты для функции `max_min_difference`:
def test_max_min_difference():
    assert max_min_difference([1, 2, 3, 4, 5]) == 4
    assert max_min_difference([10, 20, 30, 40, 50]) == 40
    assert max_min_difference([5, 10, 15, 20]) == 15
    assert max_min_difference([]) == None
    assert max_min_difference([1]) == 0
    assert max_min_difference([100, 200, 300, 400]) == 300
    assert max_min_difference([7, 14, 21, 28]) == 21
    assert max_min_difference([9, 18, 27, 36]) == 27
    assert max_min_difference([3, 6, 9, 12]) == 9


# 91. Тесты для функции `first_divisible_by_2_and_5`:
def test_first_divisible_by_2_and_5():
    assert first_divisible_by_2_and_5([1, 3, 5, 10]) == 10
    assert first_divisible_by_2_and_5([20, 15, 25, 30]) == 20
    assert first_divisible_by_2_and_5([1, 2, 3, 4]) == None
    assert first_divisible_by_2_and_5([50, 60, 70]) == 50
    assert first_divisible_by_2_and_5([21, 35, 49]) == None
    assert first_divisible_by_2_and_5([100, 200, 300]) == 100
    assert first_divisible_by_2_and_5([]) == None
    assert first_divisible_by_2_and_5([6, 9, 12, 18]) == None
    assert first_divisible_by_2_and_5([25, 50, 75]) == 50


# 92. Тесты для функции `square_if_number`:
def test_square_if_number():
    assert square_if_number("4") == 16.0
    assert square_if_number("2.5") == 6.25
    assert square_if_number("-3") == 9.0
    assert square_if_number("abc") == None
    assert square_if_number("0") == 0.0
    assert square_if_number("10") == 100.0
    assert square_if_number("3.14") == 9.8596
    assert square_if_number("") == None
    assert square_if_number("1.5e2") == 22500.0


# 93. Тесты для функции `count_non_prime`:
def test_count_non_prime():
    assert count_non_prime([2, 3, 4, 5, 6]) == 2
    assert count_non_prime([10, 12, 14]) == 3
    assert count_non_prime([11, 13, 17]) == 0
    assert count_non_prime([1, 2, 3, 4]) == 2
    assert count_non_prime([9, 15, 21]) == 3
    assert count_non_prime([4, 6, 8, 10]) == 4
    assert count_non_prime([5, 7, 11, 13]) == 0
    assert count_non_prime([0, 1, 2, 3, 4]) == 3
    assert count_non_prime([25, 36, 49]) == 3


# 94. Тесты для функции `palindromic_elements`:
def test_palindromic_elements():
    assert palindromic_elements(["121", "abc", "mam", "pop"]) == ["121", "mam", "pop"]
    assert palindromic_elements(["12321", "hello", "wow"]) == ["12321", "wow"]
    assert palindromic_elements([121, 1331, 12321]) == [121, 1331, 12321]
    assert palindromic_elements([123, 456, 789]) == []
    assert palindromic_elements([1441, 1221, 101]) == [1441, 1221, 101]
    assert palindromic_elements([]) == []
    assert palindromic_elements([55, 66, 77]) == [55, 66, 77]
    assert palindromic_elements(["aba", "cdc", "dad"]) == ["aba", "cdc", "dad"]
    assert palindromic_elements(["a", "b", "c", "d"]) == ["a", "b", "c", "d"]


# 95. Тесты для функции `largest_power_of_two`:
def test_largest_power_of_two():
    assert largest_power_of_two([1, 2, 4, 8, 16]) == 16
    assert largest_power_of_two([32, 64, 128]) == 128
    assert largest_power_of_two([3, 5, 7]) == None
    assert largest_power_of_two([2, 4, 16, 32]) == 32
    assert largest_power_of_two([]) == None
    assert largest_power_of_two([10, 20, 40]) == None
    assert largest_power_of_two([6, 12, 18]) == None
    assert largest_power_of_two([256, 512, 1024]) == 1024
    assert largest_power_of_two([5, 10, 20, 40]) == None


# 96. Тесты для функции `multiples_of_six`:
def test_multiples_of_six():
    assert multiples_of_six([6, 12, 18, 24]) == [6, 12, 18, 24]
    assert multiples_of_six([5, 10, 15, 20]) == []
    assert multiples_of_six([36, 42, 48]) == [36, 42, 48]
    assert multiples_of_six([7, 14, 21]) == []
    assert multiples_of_six([6, 6, 6]) == [6, 6, 6]
    assert multiples_of_six([]) == []
    assert multiples_of_six([30, 60, 90]) == [30, 60, 90]
    assert multiples_of_six([11, 22, 33]) == []
    assert multiples_of_six([18, 24, 36]) == [18, 24, 36]


# 97. Тесты для функции `unique_elements`:
def test_unique_elements():
    assert unique_elements([1, 2, 3, 1, 2]) == [1, 2, 3]
    assert unique_elements([4, 5, 6, 4, 5]) == [4, 5, 6]
    assert unique_elements([7, 8, 9]) == [7, 8, 9]
    assert unique_elements([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert unique_elements([10, 10, 10]) == [10]
    assert unique_elements([]) == []
    assert unique_elements([11, 22, 33, 22, 11]) == [11, 22, 33]
    assert unique_elements([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]
    assert unique_elements([5, 10, 15, 10, 5]) == [5, 10, 15]


# 98. Тесты для функции `count_occurrences_1`:
def test_count_occurrences_1():
    assert count_occurrences_1([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
    assert count_occurrences_1([4, 5, 6, 5, 4]) == {4: 2, 5: 2, 6: 1}
    assert count_occurrences_1([7, 8, 9]) == {7: 1, 8: 1, 9: 1}
    assert count_occurrences_1([1, 1, 1, 1]) == {1: 4}
    assert count_occurrences_1([]) == {}
    assert count_occurrences_1([2, 4, 4, 6, 6, 6]) == {2: 1, 4: 2, 6: 3}
    assert count_occurrences_1([10, 20, 30, 20, 10, 30, 30]) == {10: 2, 20: 2, 30: 3}
    assert count_occurrences_1([2, 3, 4, 5, 2, 4, 5]) == {2: 2, 3: 1, 4: 2, 5: 2}
    assert count_occurrences_1([100, 100, 100, 200, 200]) == {100: 3, 200: 2}


# 99. Тесты для функции `intersection_of_lists`:
def test_intersection_of_lists():
    assert intersection_of_lists([1, 2, 3], [3, 4, 5]) == [3]
    assert intersection_of_lists([10, 20, 30], [20, 30, 40]) == [20, 30]
    assert intersection_of_lists([5, 6, 7], [8, 9, 10]) == []
    assert intersection_of_lists([1, 2, 3, 4], [4, 5, 6, 7]) == [4]
    assert intersection_of_lists([1, 1, 2, 2], [2, 2, 3, 3]) == [2]
    assert intersection_of_lists([100, 200, 300], [400, 500, 600]) == []
    assert intersection_of_lists([0, 1, 2], [2, 3, 4]) == [2]
    assert intersection_of_lists([10, 11, 12], [13, 14, 15]) == []
    assert intersection_of_lists([], [1, 2, 3]) == []
    assert intersection_of_lists([1, 2, 3], []) == []


# 100. Тесты для функции `divisible_by_any`:
def test_divisible_by_any():
    assert divisible_by_any([10, 20, 30, 40], [2, 5]) == [10, 20, 30, 40]
    assert divisible_by_any([9, 18, 27, 36], [3]) == [9, 18, 27, 36]
    assert divisible_by_any([7, 14, 21], [2, 7]) == [7, 14, 21]
    assert divisible_by_any([11, 13, 17], [5, 10]) == []
    assert divisible_by_any([100, 200, 300], [2, 10]) == [100, 200, 300]
    assert divisible_by_any([8, 12, 16], [4]) == [8, 12, 16]
    assert divisible_by_any([15, 25, 35], [5]) == [15, 25, 35]
    assert divisible_by_any([1, 3, 5, 7], [2, 4]) == []
    assert divisible_by_any([100, 150, 200], [5]) == [100, 150, 200]
    assert divisible_by_any([], [2, 3]) == []
