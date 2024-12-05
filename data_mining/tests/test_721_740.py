from functions.file_721_740 import *
import pytest


# 721. Тесты для функции `choose_smallest_even_from_list`
def test_choose_smallest_even_from_list():
    assert choose_smallest_even_from_list([1, 3, 5, 7]) == "No even numbers found"
    assert choose_smallest_even_from_list([2, 4, 6, 8]) == 2
    assert choose_smallest_even_from_list([1, 2, 3, 4, 5]) == 2
    assert choose_smallest_even_from_list([-2, 3, -4, 5, -6]) == -6
    assert choose_smallest_even_from_list([10, 15, 7, 3]) == 10
    assert choose_smallest_even_from_list([]) == "No even numbers found"


# 722. Тесты для функции `choose_longest_non_vowel_word`
def test_choose_longest_non_vowel_word():
    assert choose_longest_non_vowel_word("apple", "banana", "cherry") == "banana"
    assert choose_longest_non_vowel_word("Apple", "Orange", "Grape") == "Grape"
    assert choose_longest_non_vowel_word("egg", "ibex", "owl") == "No word found"
    assert choose_longest_non_vowel_word("cat", "dog", "fish") == "fish"
    assert choose_longest_non_vowel_word("bird", "fly", "ant") == "bird"
    assert choose_longest_non_vowel_word("enter", "exit", "island") == 'No word found'


# 723. Тесты для функции `choose_smallest_negative`
def test_choose_smallest_negative():
    assert choose_smallest_negative(1, 2, 3, 4) == "No negative numbers"
    assert choose_smallest_negative(-1, -2, -3, -4) == -1
    assert choose_smallest_negative(1, -2, 3, -4) == -2
    assert choose_smallest_negative(-10, -20, -30, -40) == -10
    assert choose_smallest_negative(-5, 0, -10) == -5
    assert choose_smallest_negative(5, 10, 15) == "No negative numbers"


# 724. Тесты для функции `choose_string_with_most_digits`
def test_choose_string_with_most_digits():
    assert choose_string_with_most_digits("abc123", "def45", "gh6789") == "gh6789"
    assert choose_string_with_most_digits("123", "456", "789") == "789"
    assert choose_string_with_most_digits("abc", "def", "ghi") == 'ghi'
    assert choose_string_with_most_digits("ab123cd", "ef45gh", "ij678kl") == "ij678kl"
    assert choose_string_with_most_digits("abc1", "def2", "ghi3") == "ghi3"
    assert choose_string_with_most_digits("123abc", "456def", "789ghi") == "789ghi"


# 725. Тесты для функции `choose_largest_in_range`
def test_choose_largest_in_range():
    assert choose_largest_in_range(1, 10, 5, 3, 8, 15) == 8
    assert choose_largest_in_range(0, 100, 50, 60, 70) == 70
    assert choose_largest_in_range(-10, 10, -5, 0, 5) == 5
    assert choose_largest_in_range(10, 20, 5, 25, 30) == "No numbers in the range (10, 20)"
    assert choose_largest_in_range(1, 5, 2, 3, 4) == 4
    assert choose_largest_in_range(100, 200, 150, 175, 190) == 190


# 726. Тесты для функции `choose_first_even_number`
def test_choose_first_even_number():
    assert choose_first_even_number([1, 3, 5, 7]) == "No even numbers"
    assert choose_first_even_number([2, 4, 6, 8]) == 2
    assert choose_first_even_number([1, 2, 3, 4]) == 2
    assert choose_first_even_number([5, 7, 8, 10]) == 8
    assert choose_first_even_number([10, 20, 30]) == 10
    assert choose_first_even_number([1, 3, 7]) == "No even numbers"


# 727. Тесты для функции `choose_shortest_no_space_string`
def test_choose_shortest_no_space_string():
    assert choose_shortest_no_space_string("hello", "world", "hi") == "hi"
    assert choose_shortest_no_space_string("a b c", "de bf", "g h") == 'No string without spaces'
    assert choose_shortest_no_space_string("one", "two", "three") == "one"
    assert choose_shortest_no_space_string("no spaces", "he re", "or here") == 'No string without spaces'
    assert choose_shortest_no_space_string("apple", "banana", "cherry") == "apple"
    assert choose_shortest_no_space_string("ab", "abc", "abcd") == "ab"


# 728. Тесты для функции `choose_youngest_age`
def test_choose_youngest_age():
    assert choose_youngest_age(25, 30, 20, 35) == 20
    assert choose_youngest_age(40, 50, 30, 20) == 20
    assert choose_youngest_age(15, 20, 25, 10) == 10
    assert choose_youngest_age(60, 55, 45, 35) == 35
    assert choose_youngest_age(5, 10, 15, 20) == 5
    assert choose_youngest_age(100, 90, 80, 70) == 70


# 729. Тесты для функции `choose_string_with_most_unique_chars`
def test_choose_string_with_most_unique_chars():
    assert choose_string_with_most_unique_chars("apple", "banana", "cherry") == 'cherry'
    assert choose_string_with_most_unique_chars("cat", "dog", "elephant") == "elephant"
    assert choose_string_with_most_unique_chars("abcd", "efgh", "ijkl") == "abcd"
    assert choose_string_with_most_unique_chars("unique", "characters", "test") == "characters"
    assert choose_string_with_most_unique_chars("simple", "complex", "word") == "complex"
    assert choose_string_with_most_unique_chars("first", "second", "third") == "second"


# 730. Тесты для функции `choose_first_even_divisible_by_three`
def test_choose_first_even_divisible_by_three():
    assert choose_first_even_divisible_by_three([1, 3, 5, 7]) == "No even number divisible by 3"
    assert choose_first_even_divisible_by_three([2, 4, 6, 8]) == 6
    assert choose_first_even_divisible_by_three([12, 18, 24]) == 12
    assert choose_first_even_divisible_by_three([7, 14, 21, 28]) == 'No even number divisible by 3'
    assert choose_first_even_divisible_by_three([3, 6, 9, 12]) == 6
    assert choose_first_even_divisible_by_three([2, 5, 8, 11]) == "No even number divisible by 3"


# 731. Тесты для функции `choose_largest_less_than`
def test_choose_largest_less_than():
    assert choose_largest_less_than(10, 1, 2, 3, 4) == 4
    assert choose_largest_less_than(-20, 1, 2, 3) == 'No numbers less than -20'
    assert choose_largest_less_than(0, -1, -2, -3) == -1
    assert choose_largest_less_than(1, 5, 6, 8) == 'No numbers less than 1'
    assert choose_largest_less_than(15, 10, 12, 14) == 14
    assert choose_largest_less_than(2, 1, 3, 5) == 1


# 732. Тесты для функции `choose_first_greater_than`
def test_choose_first_greater_than():
    assert choose_first_greater_than(10, 5, 15, 20) == 15
    assert choose_first_greater_than(0, 1, 2, 3) == 1
    assert choose_first_greater_than(-5, -1, 0, 5) == -1
    assert choose_first_greater_than(100, 150, 200, 250) == 150
    assert choose_first_greater_than(3, 2, 4, 5) == 4
    assert choose_first_greater_than(10, 5, 6, 7) == f"No numbers greater than 10"


# 733. Тесты для функции `choose_string_with_length_divisible_by_three`
def test_choose_string_with_length_divisible_by_three():
    assert choose_string_with_length_divisible_by_three("abcd", "defg", "hijklmn") == "No string with length divisible by 3"
    assert choose_string_with_length_divisible_by_three("abcdefgh", "ijklmnopqrs", "tuv") == "tuv"
    assert choose_string_with_length_divisible_by_three("123456", "789", "0123") == "123456"
    assert choose_string_with_length_divisible_by_three("aaaaaa", "bbbbbbb", "ccccccccc") == "aaaaaa"
    assert choose_string_with_length_divisible_by_three("hello", "world", "test") == "No string with length divisible by 3"
    assert choose_string_with_length_divisible_by_three("one", "two", "three") == 'one'


# 734. Тесты для функции `choose_most_expensive_item`
def test_choose_most_expensive_item():
    assert choose_most_expensive_item({"name": "item1", "price": 10}, {"name": "item2", "price": 20}, {"name": "item3", "price": 30}) == {"name": "item3", "price": 30}
    assert choose_most_expensive_item({"name": "item4", "price": 5}, {"name": "item5", "price": 15}, {"name": "item6", "price": 25}) == {"name": "item6", "price": 25}
    assert choose_most_expensive_item({"name": "item7", "price": 100}, {"name": "item8", "price": 200}, {"name": "item9", "price": 300}) == {"name": "item9", "price": 300}
    assert choose_most_expensive_item({"name": "item10", "price": 50}, {"name": "item11", "price": 75}, {"name": "item12", "price": 100}) == {"name": "item12", "price": 100}
    assert choose_most_expensive_item({"name": "item13", "price": 60}, {"name": "item14", "price": 80}, {"name": "item15", "price": 120}) == {"name": "item15", "price": 120}
    assert choose_most_expensive_item({"name": "item16", "price": 10}, {"name": "item17", "price": 5}) == {"name": "item16", "price": 10}


# 735. Тесты для функции `choose_string_shorter_than`
def test_choose_string_shorter_than():
    assert choose_string_shorter_than(5, "apple", "cat", "banana") == "cat"
    assert choose_string_shorter_than(4, "dog", "fish", "whale") == "dog"
    assert choose_string_shorter_than(7, "elephant", "snake", "shark") == "snake"
    assert choose_string_shorter_than(3, "sun", "moon", "star") is None
    assert choose_string_shorter_than(6, "planet", "comet", "asteroid") == "comet"
    assert choose_string_shorter_than(8, "galaxy", "universe", "cosmos") == "galaxy"


# 736. Тесты для функции `choose_first_not_divisible_by_2_and_3`
def test_choose_first_not_divisible_by_2_and_3():
    assert choose_first_not_divisible_by_2_and_3([1, 2, 3, 4, 5]) == 1
    assert choose_first_not_divisible_by_2_and_3([6, 9, 12, 15]) is None
    assert choose_first_not_divisible_by_2_and_3([7, 14, 21, 28]) == 7
    assert choose_first_not_divisible_by_2_and_3([8, 11, 13, 16]) == 11
    assert choose_first_not_divisible_by_2_and_3([10, 25, 30, 45]) == 25
    assert choose_first_not_divisible_by_2_and_3([17, 34, 51, 68]) == 17


# 737. Тесты для функции `choose_word_with_only_vowels`
def test_choose_word_with_only_vowels():
    assert choose_word_with_only_vowels("aeiou", "io", "u") == "aeiou"
    assert choose_word_with_only_vowels("aaaa", "eieio", "iiiii") == "aaaa"
    assert choose_word_with_only_vowels("oo", "u", "eeee") == "oo"
    assert choose_word_with_only_vowels("ui", "oe", "aa") == "ui"
    assert choose_word_with_only_vowels("o", "e", "i") == "o"
    assert choose_word_with_only_vowels("apple", "banana", "cherry") is None


# 738. Тесты для функции `choose_largest_less_than_or_equal_to`
def test_choose_largest_less_than_or_equal_to():
    assert choose_largest_less_than_or_equal_to(10, 1, 2, 3, 4) == 4
    assert choose_largest_less_than_or_equal_to(5, 1, 2, 3) == 3
    assert choose_largest_less_than_or_equal_to(0, -1, -2, -3) == -1
    assert choose_largest_less_than_or_equal_to(7, 5, 6, 8) == 6
    assert choose_largest_less_than_or_equal_to(15, 10, 12, 14) == 14
    assert choose_largest_less_than_or_equal_to(2, 1, 3, 5) == 1


# 739. Тесты для функции `choose_longest_digit_string`
def test_choose_longest_digit_string():
    assert choose_longest_digit_string("123", "45678", "90") == "45678"
    assert choose_longest_digit_string("112233", "44556677", "889900") == "44556677"
    assert choose_longest_digit_string("abc123", "def456", "ghi789") is None
    assert choose_longest_digit_string("111", "2222", "333") == "2222"
    assert choose_longest_digit_string("99999", "8888", "7777") == "99999"
    assert choose_longest_digit_string("1234567890", "0987654321", "1112131415") == "1234567890"


# 740. Тесты для функции `choose_shortest_string_without_vowels`
def test_choose_shortest_string_without_vowels():
    assert choose_shortest_string_without_vowels("bcdf", "ghjkl", "mnpqr") == "bcdf"
    assert choose_shortest_string_without_vowels("bcdfg", "hjklm", "npqr") == "npqr"
    assert choose_shortest_string_without_vowels("b", "c", "d") == "b"
    assert choose_shortest_string_without_vowels("xyz", "wxy", "uvw") == 'xyz'
    assert choose_shortest_string_without_vowels("apple", "banana", "cherry") is None
    assert choose_shortest_string_without_vowels("bcd", "ghj", "mn") == "mn"
