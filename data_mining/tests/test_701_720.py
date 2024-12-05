from functions.file_701_720 import *
import pytest


# 701. Тесты для функции `find_long_words`
def test_find_long_words():
    assert find_long_words("Hello world from AI") == ["Hello", "world", "from"]
    assert find_long_words("AI is fun") == []
    assert find_long_words("") == []
    assert find_long_words("Test the function find long words") == ["Test", "function", "find", "long", "words"]
    assert find_long_words("Short and sweet") == ["Short", "sweet"]
    assert find_long_words("A sequence of longwordsisrequired") == ["sequence", "longwordsisrequired"]
    assert find_long_words("Edge case with wordsss") == ["Edge", "case", "with", "wordsss"]
    assert find_long_words("Another edge case with word") == ["Another", "edge", "case", "with", "word"]
    assert find_long_words("1234567890 more than 10") == ["1234567890", "more", "than"]


# 702. Тесты для функции `get_numbers_from_string`
def test_get_numbers_from_string():
    assert get_numbers_from_string("123,456,789") == [123, 456, 789]
    assert get_numbers_from_string("100,200,300") == [100, 200, 300]
    assert get_numbers_from_string("") == []
    assert get_numbers_from_string("0,1,2,3") == [0, 1, 2, 3]
    assert get_numbers_from_string("11,22,33") == [11, 22, 33]
    assert get_numbers_from_string("text without numbers") == []
    assert get_numbers_from_string("400number,500text,600number") == [400, 500, 600]
    assert get_numbers_from_string("999text999") == [999, 999]
    assert get_numbers_from_string("1.2.3") == [1, 2, 3]


# 703. Тесты для функции `find_numbers_greater_than`
def test_find_numbers_greater_than():
    assert find_numbers_greater_than([1, 2, 3, 4, 5], 3) == [4, 5]
    assert find_numbers_greater_than([], 3) == []
    assert find_numbers_greater_than([3, 3, 3], 3) == []
    assert find_numbers_greater_than([10, 20, 30, 40, 50], 25) == [30, 40, 50]
    assert find_numbers_greater_than([-1, -2, -3, -4], -3) == [-1, -2]
    assert find_numbers_greater_than([100, 101, 102], 100) == [101, 102]
    assert find_numbers_greater_than([2, 4, 6, 8], 1) == [2, 4, 6, 8]
    assert find_numbers_greater_than([5, 3, 1], 4) == [5]
    assert find_numbers_greater_than([5, 4, 3, 2, 1], 2) == [5, 4, 3]


# 704. Тесты для функции `join_strings_with_separator`
def test_join_strings_with_separator():
    assert join_strings_with_separator(["a", "b", "c"], ",") == "a,b,c"
    assert join_strings_with_separator([], ",") == ""
    assert join_strings_with_separator(["onlyone"], ",") == "onlyone"
    assert join_strings_with_separator(["this", "is", "a", "test"], " ") == "this is a test"
    assert join_strings_with_separator(["test", "function"], "-") == "test-function"
    assert join_strings_with_separator(["join", "with", "different", "separators"], "|") == "join|with|different|separators"
    assert join_strings_with_separator(["first", "second"], ".") == "first.second"
    assert join_strings_with_separator(["combine", "all", "words"], "") == "combineallwords"
    assert join_strings_with_separator(["1", "2", "3"], " ") == "1 2 3"


# 705. Тесты для функции `sum_even_numbers`
def test_sum_even_numbers():
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12
    assert sum_even_numbers([]) == 0
    assert sum_even_numbers([1, 3, 5, 7]) == 0
    assert sum_even_numbers([2, 4, 6, 8, 10]) == 30
    assert sum_even_numbers([-2, -4, -6]) == -12
    assert sum_even_numbers([0, 2, 4]) == 6
    assert sum_even_numbers([1, 2, 3, 4]) == 6
    assert sum_even_numbers([10, 20, 30, 40]) == 100
    assert sum_even_numbers([2, 2, 2, 2]) == 8


# 706. Тесты для функции `find_string_with_word`
def test_find_string_with_word():
    assert find_string_with_word(["hello world", "foo bar"], "hello") == "hello world"
    assert find_string_with_word(["one two", "three four"], "five") is None
    assert find_string_with_word([], "word") is None
    assert find_string_with_word(["find this string", "or this one"], "this") == "find this string"
    assert find_string_with_word(["no match here"], "hello") is None
    assert find_string_with_word(["searching", "for", "word"], "for") == "for"
    assert find_string_with_word(["multiple", "matches", "here"], "matches") == "matches"
    assert find_string_with_word(["first", "last"], "last") == "last"
    assert find_string_with_word(["edge case"], "edge") == "edge case"


# 707. Тесты для функции `find_smallest_odd`
def test_find_smallest_odd():
    assert find_smallest_odd([1, 3, 5, 7, 9]) == 1
    assert find_smallest_odd([2, 4, 6, 8, 10]) is None
    assert find_smallest_odd([]) is None
    assert find_smallest_odd([10, 15, 20, 25]) == 15
    assert find_smallest_odd([11, 13, 15, 17]) == 11
    assert find_smallest_odd([-1, -3, -5, 0]) == -5
    assert find_smallest_odd([100, 101, 102, 103]) == 101
    assert find_smallest_odd([5, 4, 3, 2, 1]) == 1
    assert find_smallest_odd([12, 14, 16, 19]) == 19


# 708. Тесты для функции `replace_substring`
def test_replace_substring():
    assert replace_substring("hello world", "world", "there") == "hello there"
    assert replace_substring("ababab", "ab", "cd") == "cdcdcd"
    assert replace_substring("", "a", "b") == ""
    assert replace_substring("nothing to replace", "xyz", "abc") is None
    assert replace_substring("12345", "123", "678") == "67845"
    assert replace_substring("replace me if you can", "can", "will") == "replace me if you will"
    assert replace_substring("edgecase", "edge", "case") == "casecase"
    assert replace_substring("simple test", "simple", "complex") == "complex test"
    assert replace_substring("aaaa", "aa", "bb") == "bbbb"


# 709. Тесты для функции `find_divisible_by_3_and_5`
def test_find_divisible_by_3_and_5():
    assert find_divisible_by_3_and_5_5([15, 30, 45, 60]) == 15
    assert find_divisible_by_3_and_5_5([1, 2, 3, 4, 5]) is None
    assert find_divisible_by_3_and_5_5([]) is None
    assert find_divisible_by_3_and_5_5([0, 3, 5, 15]) == 0
    assert find_divisible_by_3_and_5_5([9, 18, 27, 45]) == 45
    assert find_divisible_by_3_and_5_5([100, 101, 102, 103]) is None
    assert find_divisible_by_3_and_5_5([30, 60, 90, 120]) == 30
    assert find_divisible_by_3_and_5_5([-15, -30, -45]) == -15
    assert find_divisible_by_3_and_5_5([3, 6, 9, 12, 15]) == 15


# 710. Тесты для функции `calculate_average`
def test_calculate_average():
    assert calculate_average([1, 2, 3, 4, 5]) == 3
    assert calculate_average([]) is None
    assert calculate_average([10, 20, 30]) == 20
    assert calculate_average([-1, -2, -3]) == -2
    assert calculate_average([5, 10, 15, 20]) == 12.5
    assert calculate_average([100]) == 100
    assert calculate_average([0, 0, 0]) == 0
    assert calculate_average([0, 5, 10]) == 5
    assert calculate_average([-10, 10, -10, 10]) == 0


# 711. Тесты для функции `combine_and_unique`
def test_combine_and_unique():
    assert combine_and_unique([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 4, 5]
    assert combine_and_unique([], [1, 2, 3]) == [1, 2, 3]
    assert combine_and_unique([1, 2, 3], []) == [1, 2, 3]
    assert combine_and_unique([], []) == []
    assert combine_and_unique([1, 1, 1], [1, 1, 1]) == [1]
    assert combine_and_unique([1, 2, 2], [2, 3, 3]) == [1, 2, 3]
    assert combine_and_unique([-1, -2, -3], [-3, -4, -5]) == [-1, -2, -3, -4, -5]
    assert combine_and_unique([1, 2, 3, 4], [5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert combine_and_unique(["a", "b"], ["b", "c"]) == ["a", "b", "c"]


# 712. Тесты для функции `choose_largest`
def test_choose_largest():
    assert choose_largest(1, 2, 3) == 3
    assert choose_largest(3, 2, 1) == 3
    assert choose_largest(1, 3, 2) == 3
    assert choose_largest(3, 3, 2) == 3
    assert choose_largest(2, 3, 3) == 3
    assert choose_largest(3, 3, 3) == 3
    assert choose_largest(-1, -2, -3) == -1
    assert choose_largest(0, 0, 0) == 0
    assert choose_largest(100, 50, 25) == 100


# 713. Тесты для функции `choose_longest_string`
def test_choose_longest_string():
    assert choose_longest_string("one", "three", "five") == "three"
    assert choose_longest_string("a", "bc", "def") == "def"
    assert choose_longest_string("apple", "banana", "cherry") == "cherry"
    assert choose_longest_string("") == ""
    assert choose_longest_string("short", "longer", "longest") == "longest"
    assert choose_longest_string("a", "ab", "abc") == "abc"
    assert choose_longest_string("equal", "equal") == "equal"
    assert choose_longest_string("A", "BB", "CCC") == "CCC"
    assert choose_longest_string("one", "two", "three") == "three"


# 714. Тесты для функции `choose_most_frequent`
def test_choose_most_frequent():
    assert choose_most_frequent([1, 2, 2, 3, 3, 3]) == 3
    assert choose_most_frequent(["a", "b", "b", "c", "c", "c"]) == "c"
    assert choose_most_frequent([1, 1, 1, 2, 2, 3, 3, 3, 3]) == 3
    assert choose_most_frequent([]) is None
    assert choose_most_frequent([1, 1, 2, 2, 3, 3]) == 3
    assert choose_most_frequent(["equal", "equal", "equal", "equal"]) == "equal"
    assert choose_most_frequent(["x", "x", "y", "y", "z"]) == "y"
    assert choose_most_frequent([1, 2, 3, 4, 5, 1, 2, 3, 1]) == 1
    assert choose_most_frequent(["apple", "banana", "apple"]) == "apple"


# 715. Тесты для функции `choose_smallest`
def test_choose_smallest():
    assert choose_smallest(3, 2, 1) == 1
    assert choose_smallest(1, 2, 3) == 1
    assert choose_smallest(2, 2, 2) == 2
    assert choose_smallest(-1, -2, -3) == -3
    assert choose_smallest(0, -1, 1) == -1
    assert choose_smallest(100, 50, 25) == 25
    assert choose_smallest(1) == 1
    assert choose_smallest(-10, -20, -30) == -30
    assert choose_smallest(1, 1, 1, 1) == 1


# 716. Тесты для функции `choose_string_with_most_vowels`
def test_choose_string_with_most_vowels():
    assert choose_string_with_most_vowels("hello", "world", "ai") == "hello"
    assert choose_string_with_most_vowels("a", "e", "i", "o", "u") == "u"
    assert choose_string_with_most_vowels("rhythm", "glyph", "fly") == "rhythm"
    assert choose_string_with_most_vowels("vowel", "consonant") == "consonant"
    assert choose_string_with_most_vowels("aaa", "bbb", "ccc") == "aaa"
    assert choose_string_with_most_vowels("aeiou", "bcdfg", "xyz") == "aeiou"
    assert choose_string_with_most_vowels("a", "aaa", "aa") == "aaa"
    assert choose_string_with_most_vowels("equal", "longer", "longest") == "equal"
    assert choose_string_with_most_vowels("a", "ab", "abc") == "abc"


# 717. Тесты для функции `choose_smallest_even`
def test_choose_smallest_even():
    assert choose_smallest_even(1, 2, 3, 4) == 2
    assert choose_smallest_even(2, 2, 2, 2) == 2
    assert choose_smallest_even(1, 1, 1, 1) == "No even numbers"
    assert choose_smallest_even(0) == 0
    assert choose_smallest_even(-2, -4, -6) == -6
    assert choose_smallest_even(10, 20, 30) == 10
    assert choose_smallest_even(1, 3, 5, 7) == "No even numbers"
    assert choose_smallest_even(2) == 2
    assert choose_smallest_even(-10, -20, -30) == -30


# 718. Тесты для функции `choose_number_with_max_diff`
def test_choose_number_with_max_diff():
    assert choose_number_with_max_diff(1, 2, 3) == 1
    assert choose_number_with_max_diff(-1, -2, -3) == -1
    assert choose_number_with_max_diff(10, 20, 30) == 10
    assert choose_number_with_max_diff(1, 1, 1) is None
    assert choose_number_with_max_diff(5, 5, 5, 10) == 10
    assert choose_number_with_max_diff(0, 0, 0) is None
    assert choose_number_with_max_diff(-10, -20, -30) == -10
    assert choose_number_with_max_diff(3, 6, 9, 12) == 3
    assert choose_number_with_max_diff(-1, 0, 1) == -1


# 719. Тесты для функции `choose_string_starting_with_vowel`
def test_choose_string_starting_with_vowel():
    assert choose_string_starting_with_vowel("apple", "banana", "orange") == "apple"
    assert choose_string_starting_with_vowel("test", "test", "test") == "No string starts with a vowel"
    assert choose_string_starting_with_vowel("egg", "emphasis") == "egg"
    assert choose_string_starting_with_vowel("quick", "brown", "fox") == "No string starts with a vowel"
    assert choose_string_starting_with_vowel("upper", "lower") == "upper"
    assert choose_string_starting_with_vowel("a", "e", "i") == "a"
    assert choose_string_starting_with_vowel("AI", "rules") == "AI"
    assert choose_string_starting_with_vowel("buzz", "quiz") == "No string starts with a vowel"


# 720. Тесты для функции `choose_second_largest`
def test_choose_second_largest():
    assert choose_second_largest(1, 2, 3) == 2
    assert choose_second_largest(3, 2, 1) == 2
    assert choose_second_largest(1, 3, 2) == 2
    assert choose_second_largest(10, 20, 30) == 20
    assert choose_second_largest(30, 20, 10) == 20
    assert choose_second_largest(20, 10, 30) == 20
    assert choose_second_largest(1, 1, 1) == "Not enough distinct numbers"
    assert choose_second_largest(1, 2) == 1
    assert choose_second_largest(3, 3, 5, 5, 5) == 3
