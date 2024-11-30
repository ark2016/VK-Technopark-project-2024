from functions.file_21_40 import *
import pytest


# 21. Тесты для функции `range_list`:
def test_range_list():
    assert range_list(1, 5) == [1, 2, 3, 4, 5]
    assert range_list(5, 5) == [5]
    assert range_list(0, 3) == [0, 1, 2, 3]
    assert range_list(3, 1) == []
    assert range_list(10, 7) == []
    assert range_list(-5, 0) == [-5, -4, -3, -2, -1, 0]


# 22. Тесты для функции `product_list`:
def test_product_list():
    assert product_list([1, 2, 3]) == 6
    assert product_list([1, 0, 3]) == 3
    assert product_list([0, 0, 0]) == 1
    assert product_list([]) == 1
    assert product_list([5, 7]) == 35
    assert product_list([1, -2, 3]) == -6


# 23. Тесты для функции `intersect_lists`:
def test_intersect_lists():
    assert intersect_lists([1, 2, 3], [3, 4, 5]) == [3]
    assert intersect_lists([1, 2], [3, 4]) == []
    assert intersect_lists([5, 6], [6, 7]) == [6]
    assert intersect_lists([], [1, 2, 3]) == []
    assert intersect_lists([1, 2, 3], []) == []
    assert intersect_lists([10, 20], [20, 30]) == [20]


# 24. Тесты для функции `remove_duplicates`:
def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 1]) == [1, 2, 3]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([10, 20, 20, 30]) == [10, 20, 30]
    assert remove_duplicates([1, 1, 1, 2, 2, 2]) == [1, 2]
    assert remove_duplicates([1, 2, 2, 1]) == [1, 2]


# 25. Тесты для функции `gcd`:
def test_gcd():
    assert gcd(12, 15) == 3
    assert gcd(100, 25) == 25
    assert gcd(7, 13) == 1
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(14, 49) == 7


# 26. Тесты для функции `lcm`:
def test_lcm():
    assert lcm(4, 5) == 20
    assert lcm(3, 7) == 21
    assert lcm(0, 5) == None
    assert lcm(10, 15) == 30
    assert lcm(25, 40) == 200
    assert lcm(8, 12) == 24
    assert lcm(1000, 1001) == 1001000


# 27. Тесты для функции `count_occurrences`:
def test_count_occurrences():
    assert count_occurrences([1, 2, 3, 1], 1) == 2
    assert count_occurrences([2, 4, 6], 2) == 1
    assert count_occurrences([1, 1, 1, 1], 2) == 0
    assert count_occurrences([10, 20, 10], 10) == 2
    assert count_occurrences([1, 3, 1, 2], 5) == 0
    assert count_occurrences([0, 2, 0, 4], 0) == 2


# 28. Тесты для функции `is_number`:
def test_is_number():
    assert is_number("123") == True
    assert is_number("12.34") == True
    assert is_number("") == False
    assert is_number("abc") == False
    assert is_number("123abc") == False
    assert is_number("-123") == False


# 29. Тесты для функции `square_non_negative`:
def test_square_non_negative():
    assert square_non_negative(4) == 16
    assert square_non_negative(0) == 0
    assert square_non_negative(-4) == None
    assert square_non_negative(5) == 25
    assert square_non_negative(-10) == None
    assert square_non_negative(10) == 100


# 30. Тесты для функции `longest_common_subsequence`:
def test_longest_common_subsequence():
    assert longest_common_subsequence("abc", "ac") == 2
    assert longest_common_subsequence("abcdef", "abdf") == 4
    assert longest_common_subsequence("abc", "xyz") == 0
    assert longest_common_subsequence("abc", "") == 0
    assert longest_common_subsequence("12345", "54321") == 1
    assert longest_common_subsequence("", "") == 0


# 31. Тесты для функции `find_index`:
def test_find_index():
    assert find_index([1, 2, 3], 2) == 1
    assert find_index([10, 20, 30], 40) == -1
    assert find_index([1, 2, 3, 4], 1) == 0
    assert find_index([], 1) == -1
    assert find_index([10, 20], 20) == 1
    assert find_index([1, 1, 1], 1) == 0


# 32. Тесты для функции `unique_chars`:
def test_unique_chars():
    assert unique_chars("aabcc") == "abc"
    assert unique_chars("abcd") == "abcd"
    assert unique_chars("aabbcc") == "abc"
    assert unique_chars("aabb  cc") == "ab c"
    assert unique_chars("abcdabcd") == "abcd"
    assert unique_chars("") == ""


# 33. Тесты для функции `count_multiples_of_five`:
def test_count_multiples_of_five():
    assert count_multiples_of_five(1, 10) == 2
    assert count_multiples_of_five(10, 1) == 0
    assert count_multiples_of_five(0, 5) == 2
    assert count_multiples_of_five(5, 5) == 1
    assert count_multiples_of_five(10, 20) == 3
    assert count_multiples_of_five(12, 18) == 1
    assert count_multiples_of_five(1, 4) == 0


# 34. Тесты для функции `is_leap_year`:
def test_is_leap_year():
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True
    assert is_leap_year(1900) == False
    assert is_leap_year(2000) == True
    assert is_leap_year(2023) == False
    assert is_leap_year(2004) == True


# 35. Тесты для функции `max_min_difference_1`:
def test_max_min_difference_1():
    assert max_min_difference_1([1, 2, 3, 4]) == 3
    assert max_min_difference_1([10, 5]) == 5
    assert max_min_difference_1([1, 1, 1, 1]) == 0
    assert max_min_difference_1([0, 2, 0]) == 2
    assert max_min_difference_1([100]) == 0
    assert max_min_difference_1([]) == None


# 36. Тесты для функции `is_anagram`:
def test_is_anagram():
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "world") == False
    assert is_anagram("evil", "vile") == True
    assert is_anagram("abc", "acb") == True
    assert is_anagram("abc", "abcd") == False
    assert is_anagram("123", "321") == True


# 37. Тесты для функции `sum_of_squares`:
def test_sum_of_squares():
    assert sum_of_squares([1, 2, 3]) == 14
    assert sum_of_squares([0, 4, 5]) == 41
    assert sum_of_squares([-1, -2, -3]) == 0
    assert sum_of_squares([1, 2, 3, 4]) == 30
    assert sum_of_squares([]) == 0
    assert sum_of_squares([1, 0, 1]) == 2


# 38. Тесты для функции `geometric_mean`:
def test_geometric_mean():
    assert geometric_mean([1, 2, 3]) == 1.8171205928321397
    assert geometric_mean([5, 5, 5]) == 5.0
    assert geometric_mean([1, 1, 1]) == 1.0
    assert geometric_mean([0, 1, 2]) == 1.2599210498948732
    assert geometric_mean([]) == None
    assert geometric_mean([3, 2, 4]) == 2.8844991406148166


# 39. Тесты для функции `find_duplicates`:
def test_find_duplicates():
    assert find_duplicates([1, 2, 3, 2]) == [2]
    assert find_duplicates([1, 1, 1]) == [1]
    assert find_duplicates([4, 5, 6]) == []
    assert find_duplicates([10, 20, 20, 30]) == [20]
    assert find_duplicates([2, 3, 2, 3]) == [2, 3]
    assert find_duplicates([1, 1, 2, 3, 3]) == [1, 3]


# 40. Тесты для функции `square_list`:
def test_square_list():
    assert square_list([1, 2, 3]) == [1, 4, 9]
    assert square_list([0, -1, -2]) == [0]
    assert square_list([5, 6]) == [25, 36]
    assert square_list([-1, -3, 2]) == [4]
    assert square_list([]) == []
    assert square_list([4, 0, -5]) == [16, 0]
