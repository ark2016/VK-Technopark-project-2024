from functions.file_761_780 import *
import pytest


# 761. Тесты для функции `choose_shortest_string_starting_with_digit`:
def test_choose_shortest_string_starting_with_digit():
    assert choose_shortest_string_starting_with_digit("abc", "1abc", "2a") == "1abc"
    assert choose_shortest_string_starting_with_digit("abc", "abc1", "2a") == "2a"
    assert choose_shortest_string_starting_with_digit("abc", "a1bc", "abc") is None
    assert choose_shortest_string_starting_with_digit("1abc", "2abc", "3abc") == "1abc"
    assert choose_shortest_string_starting_with_digit("123", "456", "789") == "123"
    assert choose_shortest_string_starting_with_digit("abc", "def", "ghi") is None


# 762. Тесты для функции `choose_anagram_of`:
def test_choose_anagram_of():
    assert choose_anagram_of("listen", "enlist", "google", "inlets") == "enlist"
    assert choose_anagram_of("listen", "google", "facebook", "silent") == "silent"
    assert choose_anagram_of("abc", "def", "ghi", "jkl") is None
    assert choose_anagram_of("cat", "tac", "act") == "tac"
    assert choose_anagram_of("cat", "dog", "god") is None
    assert choose_anagram_of("abc", "bca", "cab", "bac") == "bca"


# 763. Тесты для функции `choose_smallest_greater_than`:
def test_choose_smallest_greater_than():
    assert choose_smallest_greater_than(5, 1, 2, 6, 8, 7) == 6
    assert choose_smallest_greater_than(3, 4, 5, 1, 2, 6) == 4
    assert choose_smallest_greater_than(10, 11, 12, 13, 14) == 11
    assert choose_smallest_greater_than(0, -1, -2, 1, 2, 3) == 1
    assert choose_smallest_greater_than(50, 100, 200, 300) == 100
    assert choose_smallest_greater_than(100, 50, 60, 70, 80) is None


# 764. Тесты для функции `choose_first_even_length_word`:
def test_choose_first_even_length_word():
    assert choose_first_even_length_word("one", "two", "three", "four") == "four"
    assert choose_first_even_length_word("hello", "world", "Python") == 'Python'
    assert choose_first_even_length_word("apple", "banana", "cherry", "dates") == "banana"
    assert choose_first_even_length_word("apple", "b", "c", "dd") == "dd"
    assert choose_first_even_length_word("a", "bb", "ccc", "dddd") == "bb"
    assert choose_first_even_length_word("a", "b", "c", "d") is None


# 765. Тесты для функции `choose_longer_than_average`:
def test_choose_longer_than_average():
    assert choose_longer_than_average("a", "bb", "ccc", "dddd") == 'ccc'
    assert choose_longer_than_average("short", "longer", "longest") == 'longest'
    assert choose_longer_than_average("aa", "bbb", "cccc") == 'cccc'
    assert choose_longer_than_average("one", "one", "one", "one") is None
    assert choose_longer_than_average("one", "two", "three") == "three"
    assert choose_longer_than_average("a", "a", "a") is None


# 766. Тесты для функции `choose_string_with_only_letters`:
def test_choose_string_with_only_letters():
    assert choose_string_with_only_letters("abc123", "def456", "ghi789") is None
    assert choose_string_with_only_letters("abc", "def", "ghi") == "abc"
    assert choose_string_with_only_letters("123", "456", "789") is None
    assert choose_string_with_only_letters("abc", "def", "123") == "abc"
    assert choose_string_with_only_letters("abc123", "def", "ghi") == "def"
    assert choose_string_with_only_letters("abc", "123", "def456") == "abc"


# 767. Тесты для функции `choose_oldest_under_30`:
def test_choose_oldest_under_30():
    assert choose_oldest_under_30(25, 20, 18, 22) == 25
    assert choose_oldest_under_30(10, 15, 30, 35) == 15
    assert choose_oldest_under_30(30, 40, 50) is None
    assert choose_oldest_under_30(29, 28, 27, 26) == 29
    assert choose_oldest_under_30(25, 29, 21, 28) == 29
    assert choose_oldest_under_30(20, 19, 18, 25) == 25


# 768. Тесты для функции `choose_multiple_of_4_not_5`:
def test_choose_multiple_of_4_not_5():
    assert choose_multiple_of_4_not_5([4, 8, 12, 16, 20]) == 4
    assert choose_multiple_of_4_not_5([5, 10, 15, 20, 25]) is None
    assert choose_multiple_of_4_not_5([7, 14, 21, 28, 35]) == 28
    assert choose_multiple_of_4_not_5([8, 16, 24, 32, 40]) == 8
    assert choose_multiple_of_4_not_5([6, 12, 18, 24, 30]) == 12
    assert choose_multiple_of_4_not_5([3, 6, 9, 12, 15]) == 12


# 769. Тесты для функции `choose_string_length_divisible_by_3`:
def test_choose_string_length_divisible_by_3():
    assert choose_string_length_divisible_by_3("a", "bb", "ccc", "dddd", "eeeee") == "ccc"
    assert choose_string_length_divisible_by_3("abcdef", "ghijk", "lmnopqr") == "abcdef"
    assert choose_string_length_divisible_by_3("a", "b", "c") is None
    assert choose_string_length_divisible_by_3("123", "456", "789") == "123"
    assert choose_string_length_divisible_by_3("111", "222", "333") == "111"
    assert choose_string_length_divisible_by_3("a", "bbb", "cc", "ddd") == "bbb"


# 770. Тесты для функции `choose_smallest_even_greater_than_10`:
def test_choose_smallest_even_greater_than_10():
    assert choose_smallest_even_greater_than_10(12, 14, 16, 18, 20) == 12
    assert choose_smallest_even_greater_than_10(21, 22, 23, 24, 25) == 22
    assert choose_smallest_even_greater_than_10(10, 11, 12, 13, 14) == 12
    assert choose_smallest_even_greater_than_10(30, 32, 34, 36) == 30
    assert choose_smallest_even_greater_than_10(8, 9, 10, 11, 12) == 12
    assert choose_smallest_even_greater_than_10(50, 60, 70) == 50


# 771. Тесты для функции `choose_first_divisible_by_2_and_5`:
def test_choose_first_divisible_by_2_and_5():
    assert choose_first_divisible_by_2_and_5([10, 20, 30, 40, 50]) == 10
    assert choose_first_divisible_by_2_and_5([5, 10, 15, 20, 25]) == 10
    assert choose_first_divisible_by_2_and_5([1, 3, 5, 7, 9]) is None
    assert choose_first_divisible_by_2_and_5([2, 4, 6, 8, 10]) == 10
    assert choose_first_divisible_by_2_and_5([12, 14, 16, 18, 20]) == 20
    assert choose_first_divisible_by_2_and_5([15, 25, 35, 45, 50]) == 50


# 772. Тесты для функции `choose_longest_non_digit_starting_string`:
def test_choose_longest_non_digit_starting_string():
    assert choose_longest_non_digit_starting_string("abc1", "def2", "ghi3") == "abc1"
    assert choose_longest_non_digit_starting_string("1abc", "2def", "3ghi") is None
    assert choose_longest_non_digit_starting_string("abcd", "efgh", "ijkl") == "abcd"
    assert choose_longest_non_digit_starting_string("1abcd", "2efgh", "3ijkl") is None
    assert choose_longest_non_digit_starting_string("abcd", "1efgh", "ijkl") == "abcd"
    assert choose_longest_non_digit_starting_string("1abcd", "efgh", "ijkl") == "efgh"


# 773. Тесты для функции `choose_first_all_uppercase_word`:
def test_choose_first_all_uppercase_word():
    assert choose_first_all_uppercase_word("HELLO", "WORLD", "PYTHON") == "HELLO"
    assert choose_first_all_uppercase_word("hello", "WORLD", "python") == "WORLD"
    assert choose_first_all_uppercase_word("hello", "world", "python") is None
    assert choose_first_all_uppercase_word("HELLO", "WORLD", "PYTHON") == "HELLO"
    assert choose_first_all_uppercase_word("hello", "WORLD", "PYTHON") == "WORLD"
    assert choose_first_all_uppercase_word("hello", "world", "PYTHON") == "PYTHON"


# 774. Тесты для функции `choose_youngest_over_50`:
def test_choose_youngest_over_50():
    assert choose_youngest_over_50(55, 60, 65, 70) == 55
    assert choose_youngest_over_50(50, 55, 60, 65) == 55
    assert choose_youngest_over_50(40, 45, 50, 55) == 55
    assert choose_youngest_over_50(45, 50, 55, 60) == 55
    assert choose_youngest_over_50(35, 40, 45, 50) is None
    assert choose_youngest_over_50(25, 30, 35, 40) is None


# 775. Тесты для функции `choose_largest_multiple_of_3_not_2`:
def test_choose_largest_multiple_of_3_not_2():
    assert choose_largest_multiple_of_3_not_2([3, 6, 9, 12, 15]) == 15
    assert choose_largest_multiple_of_3_not_2([1, 2, 3, 4, 5]) == 3
    assert choose_largest_multiple_of_3_not_2([5, 10, 15, 20, 25]) == 15
    assert choose_largest_multiple_of_3_not_2([9, 18, 27, 36, 45]) == 45
    assert choose_largest_multiple_of_3_not_2([12, 24, 36, 48, 60]) is None
    assert choose_largest_multiple_of_3_not_2([11, 22, 33, 44, 55]) == 33


# 776. Тесты для функции `choose_string_with_uppercase_and_digit`:
def test_choose_string_with_uppercase_and_digit():
    assert choose_string_with_uppercase_and_digit("Abc1", "def2", "ghi3") == "Abc1"
    assert choose_string_with_uppercase_and_digit("1abc", "2def", "3ghi") is None
    assert choose_string_with_uppercase_and_digit("Abc", "def", "Ghi") is None
    assert choose_string_with_uppercase_and_digit("Abc1", "Def2", "Ghi3") == "Abc1"
    assert choose_string_with_uppercase_and_digit("1Abc", "2Def", "3Ghi") == "1Abc"
    assert choose_string_with_uppercase_and_digit("abc1", "def2", "ghi3") is None


# 777. Тесты для функции `choose_first_even_less_than_50`:
def test_choose_first_even_less_than_50():
    assert choose_first_even_less_than_50([10, 20, 30, 40, 50]) == 10
    assert choose_first_even_less_than_50([5, 10, 15, 20, 25]) == 10
    assert choose_first_even_less_than_50([1, 3, 5, 7, 9]) is None
    assert choose_first_even_less_than_50([2, 4, 6, 8, 10]) == 2
    assert choose_first_even_less_than_50([12, 14, 16, 18, 20]) == 12
    assert choose_first_even_less_than_50([15, 25, 35, 45, 50]) is None


# 778. Тесты для функции `choose_shortest_no_space_string_3`:
def test_choose_shortest_no_space_string_3():
    assert choose_shortest_no_space_string_3("hello", "world", "python") == "hello"
    assert choose_shortest_no_space_string_3("this is a test", "no spaces here", "short") == "short"
    assert choose_shortest_no_space_string_3("a", "ab", "abc") == "a"
    assert choose_shortest_no_space_string_3("abc", "abcd", "abcdef") == "abc"
    assert choose_shortest_no_space_string_3("hello world", "python programming", "short text") is None
    assert choose_shortest_no_space_string_3("no space", "shortest", "longest text") == "shortest"


# 779. Тесты для функции `choose_repeated_string`:
def test_choose_repeated_string():
    assert choose_repeated_string("abcabc", "defdef", "ghighi") == "abcabc"
    assert choose_repeated_string("hello", "world", "python") is None
    assert choose_repeated_string("aabbcc", "ddeeff", "gghhii") is None
    assert choose_repeated_string("abcabc", "abc", "def") == "abcabc"
    assert choose_repeated_string("xyzxyz", "xyz", "xyxxyx") == "xyzxyz"
    assert choose_repeated_string("repeatrepeat", "repe", "repeated") == "repeatrepeat"


# 780. Тесты для функции `choose_number_in_range_0_100`:
def test_choose_number_in_range_0_100():
    assert choose_number_in_range_0_100(0, 10, 20, 30, 40) == 10
    assert choose_number_in_range_0_100(50, 60, 70, 80, 90) == 50
    assert choose_number_in_range_0_100(100, 110, 120, 130, 140) == 100
    assert choose_number_in_range_0_100(-10, -20, -30) is None
    assert choose_number_in_range_0_100(-15, -25, -35, -45, -55) is None
    assert choose_number_in_range_0_100(1, 2, 3, 4, 5) == 1
