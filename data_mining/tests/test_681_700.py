from functions.file_681_700 import *
import pytest


# 681. Тесты для функции `find_strings_with_digits`:
def test_find_strings_with_digits():
    assert find_strings_with_digits(["abc", "a1c", "123", ""]) == ["a1c", "123"]
    assert find_strings_with_digits(["no_digits", "still_no", "3digits"]) == ["3digits"]
    assert find_strings_with_digits(["", "1"]) == ["1"]
    assert find_strings_with_digits(["all_numbers1", "2gether", ""]) == ["all_numbers1", "2gether"]
    assert find_strings_with_digits(["none_here", "and_here", ""]) == []
    assert find_strings_with_digits(["12three", "fou4r", ""]) == ["12three", "fou4r"]


# 682. Тесты для функции `count_digits_in_string`:
def test_count_digits_in_string():
    assert count_digits_in_string("abc123") == 3
    assert count_digits_in_string("") == 0
    assert count_digits_in_string("no_digits") == 0
    assert count_digits_in_string("5abc67") == 3
    assert count_digits_in_string("123456") == 6
    assert count_digits_in_string("only1digit") == 1


# 683. Тесты для функции `get_every_second_char`:
def test_get_every_second_char():
    assert get_every_second_char("abcdef") == "ace"
    assert get_every_second_char("a") == "a"
    assert get_every_second_char("") == ""
    assert get_every_second_char("123456") == "135"
    assert get_every_second_char("a1b2c3d4") == "abcd"
    assert get_every_second_char("even") == 'ee'


# 684. Тесты для функции `filter_strings_with_uppercase`:
def test_filter_strings_with_uppercase():
    assert filter_strings_with_uppercase(["abc", "ABC", "aBc"]) == ["ABC", "aBc"]
    assert filter_strings_with_uppercase(["no_upper", "STILL_NONE", ""]) == ["STILL_NONE"]
    assert filter_strings_with_uppercase(["lower", "Case", "UPPER"]) == ["Case", "UPPER"]
    assert filter_strings_with_uppercase(["", "noupper", ""]) == []
    assert filter_strings_with_uppercase(["Empty", "Spaces", "OnlyUpper"]) == ["Empty", "Spaces", "OnlyUpper"]
    assert filter_strings_with_uppercase(["upperCASE", "MiXeD", ""]) == ["upperCASE", "MiXeD"]


# 685. Тесты для функции `count_non_space_characters`:
def test_count_non_space_characters():
    assert count_non_space_characters("abc abc") == {"a": 2, "b": 2, "c": 2}
    assert count_non_space_characters("") == {}
    assert count_non_space_characters("no spaces") == {'n': 1, 'o': 1, 's': 2, 'p': 1, 'a': 1, 'c': 1, 'e': 1}
    assert count_non_space_characters("a b c") == {"a": 1, "b": 1, "c": 1}
    assert count_non_space_characters("repeated repeated") == {"r": 2, "e": 6, "p": 2, "a": 2, "t": 2, "d": 2}
    assert count_non_space_characters("spaces only") == {"s": 2, "p": 1, "a": 1, "c": 1, "e": 1, "o": 1, "n": 1, "l": 1, "y": 1}


# 686. Тесты для функции `find_longest_string`:
def test_find_longest_string():
    assert find_longest_string(["short", "longer", "longest"]) == "longest"
    assert find_longest_string(["one", "three"]) == "three"
    assert find_longest_string(["same", "size"]) == "same"
    assert find_longest_string([""]) == ""
    assert find_longest_string(["two", "letters", "word"]) == "letters"
    assert find_longest_string([]) is None


# 687. Тесты для функции `find_first_even`:
def test_find_first_even():
    assert find_first_even([1, 3, 5, 6]) == 3
    assert find_first_even([2, 4, 6, 8]) == 0
    assert find_first_even([1, 3, 5, 7]) is None
    assert find_first_even([1, 2, 3, 4, 5]) == 1
    assert find_first_even([]) is None
    assert find_first_even([1, 2, 4, 8, 16]) == 1


# 688. Тесты для функции `sum_numbers_in_string_v3`:
def test_sum_numbers_in_string_v3():
    assert sum_numbers_in_string_v3("abc123") == 123
    assert sum_numbers_in_string_v3("") is None
    assert sum_numbers_in_string_v3("123abc45") == 168
    assert sum_numbers_in_string_v3("no digits here") is None
    assert sum_numbers_in_string_v3("12 and 34") == 46
    assert sum_numbers_in_string_v3("100") == 100


# 689. Тесты для функции `string_to_number_list`:
def test_string_to_number_list():
    assert string_to_number_list("1 2 3") == [1, 2, 3]
    assert string_to_number_list("") == []
    assert string_to_number_list("one two three") is None
    assert string_to_number_list("1 2 3 four") is None
    assert string_to_number_list("10 20 30") == [10, 20, 30]
    assert string_to_number_list("10 20") == [10, 20]


# 690. Тесты для функции `find_max_min`:
def test_find_max_min():
    assert find_max_min([1, 2, 3, 4, 5]) == (5, 1)
    assert find_max_min([5, 1, 5, 5]) == (5, 1)
    assert find_max_min([3, -3, 5, 7]) == (7, -3)
    assert find_max_min([10]) == (10, 10)
    assert find_max_min([]) == (None, None)
    assert find_max_min([-5, -4, -3, -2, -1]) == (-1, -5)


# 691. Тесты для функции `replace_spaces_with_underscores_5`:
def test_replace_spaces_with_underscores_5():
    assert replace_spaces_with_underscores_5("a b c") == "a_b_c"
    assert replace_spaces_with_underscores_5("") is None
    assert replace_spaces_with_underscores_5("no spaces") == "no_spaces"
    assert replace_spaces_with_underscores_5("only one") == "only_one"
    assert replace_spaces_with_underscores_5("leading space ") == "leading_space_"
    assert replace_spaces_with_underscores_5(" trailing space") == "_trailing_space"


# 692. Тесты для функции `remove_duplicates_maintain_order`:
def test_remove_duplicates_maintain_order():
    assert remove_duplicates_maintain_order([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates_maintain_order([]) == []
    assert remove_duplicates_maintain_order([1, 1, 1, 1]) == [1]
    assert remove_duplicates_maintain_order(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]
    assert remove_duplicates_maintain_order([1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates_maintain_order([4, 4, 4, 4, 4, 4]) == [4]


# 693. Тесты для функции `find_first_multiple`:
def test_find_first_multiple():
    assert find_first_multiple([10, 20, 30], 10) == 10
    assert find_first_multiple([1, 3, 5], 2) is None
    assert find_first_multiple([], 2) is None
    assert find_first_multiple([5, 10, 15], 5) == 5
    assert find_first_multiple([2, 4, 6], 3) == 6
    assert find_first_multiple([4, 8, 12, 16], 4) == 4


# 694. Тесты для функции `is_palindrome_v2`:
def test_is_palindrome_v2():
    assert is_palindrome_v2("A man a plan a canal Panama") is True
    assert is_palindrome_v2("") is False
    assert is_palindrome_v2("racecar") is True
    assert is_palindrome_v2("hello") is False
    assert is_palindrome_v2("Never odd or even") is True
    assert is_palindrome_v2("not a palindrome") is False


# 695. Тесты для функции `get_even_numbers`:
def test_get_even_numbers():
    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert get_even_numbers([]) == []
    assert get_even_numbers([1, 3, 5]) == []
    assert get_even_numbers([0, 2, 4, 6, 8]) == [0, 2, 4, 6, 8]
    assert get_even_numbers([1, 2, 3, 4, 5]) == [2, 4]
    assert get_even_numbers([10, 11, 12, 13]) == [10, 12]


# 696. Тесты для функции `is_number_v2`:
def test_is_number_v2():
    assert is_number_v2("123") is True
    assert is_number_v2("abc") is False
    assert is_number_v2("") is False
    assert is_number_v2("123.45") is True
    assert is_number_v2("12e4") is True
    assert is_number_v2("one") is False


# 697. Тесты для функции `count_repeating_elements`:
def test_count_repeating_elements():
    assert count_repeating_elements([1, 2, 2, 3, 3, 3]) == {2: 2, 3: 3}
    assert count_repeating_elements([]) == {}
    assert count_repeating_elements([1, 1, 1, 1]) == {1: 4}
    assert count_repeating_elements(["a", "b", "a", "c", "b"]) == {"a": 2, "b": 2}
    assert count_repeating_elements([1, 2, 3]) == {}
    assert count_repeating_elements([4, 4, 4, 4, 4, 4]) == {4: 6}


# 698. Тесты для функции `extract_unique_words`:
def test_extract_unique_words():
    assert extract_unique_words("one two two three three three") == ['one', 'three', 'two']
    assert extract_unique_words("") == []
    assert extract_unique_words("word") == ["word"]
    assert extract_unique_words("a b c a b c") == ["a", "b", "c"]
    assert extract_unique_words("unique words in this string") == ['in', 'string', 'this', 'unique', 'words']
    assert extract_unique_words("repeat repeat") == ["repeat"]


# 699. Тесты для функции `find_largest_prime`:
def test_find_largest_prime():
    assert find_largest_prime([2, 3, 5, 7, 11, 13]) == 13
    assert find_largest_prime([]) is None
    assert find_largest_prime([4, 6, 8, 10]) is None
    assert find_largest_prime([11, 1024, 23, 19]) == 23
    assert find_largest_prime([10, 13, 17, 18, 19]) == 19
    assert find_largest_prime([1, 2, 3]) == 3


# 700. Тесты для функции `extract_digits`:
def test_extract_digits():
    assert extract_digits("a1b2c3") == [1, 2, 3]
    assert extract_digits("") == []
    assert extract_digits("no digits here") == []
    assert extract_digits("123abc456") == [1, 2, 3, 4, 5, 6]
    assert extract_digits("0") == [0]
    assert extract_digits("one1two2") == [1, 2]
