from functions.file_741_760 import *
import pytest


# 741. Тесты для функции `choose_largest_even_less_than`:
def test_choose_largest_even_less_than():
    assert choose_largest_even_less_than(10, 1, 2, 3, 4, 5, 6, 7, 8, 9) == 8
    assert choose_largest_even_less_than(5, 1, 3, 5) is None
    assert choose_largest_even_less_than(20, 10, 15, 20, 25) == 10


# 742. Тесты для функции `choose_second_smallest`:
def test_choose_second_smallest():
    assert choose_second_smallest(5, 3, 8, 6, 7, 2) == 3
    assert choose_second_smallest(4, 4, 4) is None
    assert choose_second_smallest(8, 1, 4, 5, 7) == 4


# 743. Тесты для функции `choose_string_start_and_end_same`:
def test_choose_string_start_and_end_same():
    assert choose_string_start_and_end_same("level", "racecar", "deified") == "level"
    assert choose_string_start_and_end_same("hello", "world") is None
    assert choose_string_start_and_end_same("anna", "noon") == "anna"


# 744. Тесты для функции `choose_first_divisible_by_5_and_7`:
def test_choose_first_divisible_by_5_and_7():
    assert choose_first_divisible_by_5_and_7([35, 70, 10, 14, 21]) == 35
    assert choose_first_divisible_by_5_and_7([2, 4, 7, 8, 10]) is None
    assert choose_first_divisible_by_5_and_7([105, 140, 28, 49]) == 105


# 745. Тесты для функции `choose_shortest_string_with_digit`:
def test_choose_shortest_string_with_digit():
    assert choose_shortest_string_with_digit("abc1", "a2b", "abcd3") == 'abc1'
    assert choose_shortest_string_with_digit("abc", "def") is None
    assert choose_shortest_string_with_digit("12345", "67890") == "12345"


# 746. Тесты для функции `choose_most_expensive_below_price`:
def test_choose_most_expensive_below_price():
    assert choose_most_expensive_below_price(120, *[{'name': 'item1', 'price': 50}, {'name': 'item2', 'price': 100}, {'name': 'item3', 'price': 150}]) == {'name': 'item2', 'price': 100}
    assert choose_most_expensive_below_price(40, *[{'name': 'item1', 'price': 50}, {'name': 'item2', 'price': 100}, {'name': 'item3', 'price': 150}]) is None
    assert choose_most_expensive_below_price(60, *[{'name': 'item1', 'price': 50}, {'name': 'item2', 'price': 100}, {'name': 'item3', 'price': 150}]) == {'name': 'item1', 'price': 50}


# 747. Тесты для функции `choose_first_square_number`:
def test_choose_first_square_number():
    assert choose_first_square_number([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
    assert choose_first_square_number([10, 15, 20, 25, 30]) == 25
    assert choose_first_square_number([2, 3, 5, 6, 7]) is None


# 748. Тесты для функции `choose_oldest_age`:
def test_choose_oldest_age():
    assert choose_oldest_age(20, 35, 50, 40) == 50
    assert choose_oldest_age(18, 12, 15) == 18
    assert choose_oldest_age(70, 85, 90, 95) == 95


# 749. Тесты для функции `choose_first_divisible_by_2_not_3`:
def test_choose_first_divisible_by_2_not_3():
    assert choose_first_divisible_by_2_not_3([4, 6, 8, 9, 12]) == 4
    assert choose_first_divisible_by_2_not_3([9, 15, 21, 33]) is None
    assert choose_first_divisible_by_2_not_3([10, 14, 20, 22]) == 10


# 750. Тесты для функции `choose_longest_all_digits_string`:
def test_choose_longest_all_digits_string():
    assert choose_longest_all_digits_string("123", "12345", "678") == "12345"
    assert choose_longest_all_digits_string("abc", "def") is None
    assert choose_longest_all_digits_string("12", "3456", "7890") == "3456"


# 751. Тесты для функции `choose_first_even_greater_than`:
def test_choose_first_even_greater_than():
    assert choose_first_even_greater_than(10, 11, 12, 13, 14) == 12
    assert choose_first_even_greater_than(15, 20, 22, 24, 26) == 20
    assert choose_first_even_greater_than(30, 25, 35) is None


# 752. Тесты для функции `choose_first_non_numeric_string`:
def test_choose_first_non_numeric_string():
    assert choose_first_non_numeric_string("123", "abc", "456", "789") == "abc"
    assert choose_first_non_numeric_string("001", "010") is None
    assert choose_first_non_numeric_string("apple", "banana", "cherry") == "apple"


# 753. Тесты для функции `choose_palindrome`:
def test_choose_palindrome():
    assert choose_palindrome("level", "world", "racecar") == "level"
    assert choose_palindrome("hello", "world") is None
    assert choose_palindrome("noon", "deified", "civic") == "noon"


# 754. Тесты для функции `choose_most_expensive_under_100`:
def test_choose_most_expensive_under_100():
    assert choose_most_expensive_under_100(*[{'name': 'item1', 'price': 60}, {'name': 'item2', 'price': 80}, {'name': 'item3', 'price': 100}]) == {'name': 'item3', 'price': 100}
    assert choose_most_expensive_under_100({'name': 'item4', 'price': 110}) is None
    assert choose_most_expensive_under_100({'name': 'item5', 'price': 90}) == {'name': 'item5', 'price': 90}


# 755. Тесты для функции `choose_first_even_greater_than_10`:
def test_choose_first_even_greater_than_10():
    assert choose_first_even_greater_than_10([9, 11, 13, 14, 16]) == 14
    assert choose_first_even_greater_than_10([5, 7, 8, 10]) is None
    assert choose_first_even_greater_than_10([12, 15, 18, 20]) == 12


# 756. Тесты для функции `choose_smallest_divisible_by_5`:
def test_choose_smallest_divisible_by_5():
    assert choose_smallest_divisible_by_5(10, 25, 30, 15) == 10
    assert choose_smallest_divisible_by_5(4, 8, 16, 32) is None
    assert choose_smallest_divisible_by_5(45, 50, 55) == 45


# 757. Тесты для функции `choose_first_long_word_starting_with_consonant`:
def test_choose_first_long_word_starting_with_consonant():
    assert choose_first_long_word_starting_with_consonant("banana", "strawberry", "apple", "grape") == 'banana'
    assert choose_first_long_word_starting_with_consonant("orange", "apricot", "kiwi") is None
    assert choose_first_long_word_starting_with_consonant("blackberry", "blueberry", "raspberry") == "blackberry"


# 758. Тесты для функции `choose_largest_less_than_20`:
def test_choose_largest_less_than_20():
    assert choose_largest_less_than_20(5, 10, 15, 18) == 18
    assert choose_largest_less_than_20(20, 21, 22) is None
    assert choose_largest_less_than_20(19, 1, 3, 6, 14) == 19


# 759. Тесты для функции `choose_string_starting_with_uppercase`:
def test_choose_string_starting_with_uppercase():
    assert choose_string_starting_with_uppercase("Apple", "banana", "Cherry", "date") == "Apple"
    assert choose_string_starting_with_uppercase("eggplant", "fig", "grape") is None
    assert choose_string_starting_with_uppercase("Honeydew", "Ice", "Juice") == "Honeydew"


# 760. Тесты для функции `choose_first_non_even_non_prime`:
def test_choose_first_non_even_non_prime():
    assert choose_first_non_even_non_prime([2, 4, 6, 9, 12, 15]) == 9
    assert choose_first_non_even_non_prime([2, 3, 5, 7, 11]) is None
    assert choose_first_non_even_non_prime([1, 22, 25, 28]) == 1
