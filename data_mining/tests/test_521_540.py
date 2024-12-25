import pytest
from functions.file_521_540 import *


# 521. Тесты для функции `are_anagrams_2`
def test_are_anagrams_2():
    assert are_anagrams_2("listen", "silent") == True
    assert are_anagrams_2("triangle", "integral") == True
    assert are_anagrams_2("apple", "pale") == False
    assert are_anagrams_2("", "") == None
    assert are_anagrams_2(None, "test") == None
    assert are_anagrams_2("test", None) == None


# 522. Тесты для функции `extract_numbers_from_string_2`
def test_extract_numbers_from_string_2():
    assert extract_numbers_from_string_2("abc123xyz456") == ["123", "456"]
    assert extract_numbers_from_string_2("no numbers here") == None
    assert extract_numbers_from_string_2("") == None
    assert extract_numbers_from_string_2(None) == None
    assert extract_numbers_from_string_2("123") == ["123"]
    assert extract_numbers_from_string_2("abc123") == ["123"]
    assert extract_numbers_from_string_2("123abc") == ["123"]


# 523. Тесты для функции `is_palindrome_with_spaces`
def test_is_palindrome_with_spaces():
    assert is_palindrome_with_spaces("A man a plan a canal Panama") == True
    assert is_palindrome_with_spaces("race car") == True
    assert is_palindrome_with_spaces("hello world") == False
    assert is_palindrome_with_spaces("") == None
    assert is_palindrome_with_spaces(None) == None
    assert is_palindrome_with_spaces("Was it a car or a cat I saw") == True


# 524. Тесты для функции `count_vowels_and_consonants`
def test_count_vowels_and_consonants():
    assert count_vowels_and_consonants("hello") == {"vowels": 2, "consonants": 3}
    assert count_vowels_and_consonants("a") == {"vowels": 1, "consonants": 0}
    assert count_vowels_and_consonants("bcdfg") == {"vowels": 0, "consonants": 5}
    assert count_vowels_and_consonants("12345") == None
    assert count_vowels_and_consonants("") == None
    assert count_vowels_and_consonants(None) == None


# 525. Тесты для функции `remove_spaces_and_reverse`
def test_remove_spaces_and_reverse():
    assert remove_spaces_and_reverse("hello world") == "dlrowolleh"
    assert remove_spaces_and_reverse(" ") == ""
    assert remove_spaces_and_reverse("a b c d e f") == "fedcba"
    assert remove_spaces_and_reverse("") == None
    assert remove_spaces_and_reverse(None) == None


# 526. Тесты для функции `longest_unique_substring`
def test_longest_unique_substring():
    assert longest_unique_substring("abcabcbb") == "abc"
    assert longest_unique_substring("bbbbb") == "b"
    assert longest_unique_substring("pwwkew") == "wke"
    assert longest_unique_substring("") == None
    assert longest_unique_substring(None) == None
    assert longest_unique_substring("abcdef") == "abcdef"


# 527. Тесты для функции `longest_common_prefix`
def test_longest_common_prefix():
    assert longest_common_prefix("flower", "flow") == "flow"
    assert longest_common_prefix("dog", "racecar") == None
    assert longest_common_prefix("", "") == None
    assert longest_common_prefix(None, "test") == None
    assert longest_common_prefix("test", None) == None
    assert longest_common_prefix("interspecies", "interstellar") == "inters"


# 528. Тесты для функции `count_repeating_words`
def test_count_repeating_words():
    assert count_repeating_words("hello Hello world world") == {"hello": 2, "world": 2}
    assert count_repeating_words("one two three") == {}
    assert count_repeating_words("") == None
    assert count_repeating_words(None) == None
    assert count_repeating_words("repeat repeat repeat") == {"repeat": 3}


# 529. Тесты для функции `longest_word_in_string`
def test_longest_word_in_string():
    assert longest_word_in_string("hello world") == "hello"
    assert longest_word_in_string("a abc ab") == "abc"
    assert longest_word_in_string("") == None
    assert longest_word_in_string(None) == None
    assert longest_word_in_string("single") == "single"


# 530. Тесты для функции `extract_substrings_of_length_n`
def test_extract_substrings_of_length_n():
    assert extract_substrings_of_length_n("abcdefg", 3) == ["abc", "bcd", "cde", "def", "efg"]
    assert extract_substrings_of_length_n("hello", 2) == ["he", "el", "ll", "lo"]
    assert extract_substrings_of_length_n("", 2) == None
    assert extract_substrings_of_length_n("a", 2) == []
    assert extract_substrings_of_length_n("test", 0) == None
    assert extract_substrings_of_length_n(None, 2) == None


# 531. Тесты для функции `remove_words_starting_with`
def test_remove_words_starting_with():
    assert remove_words_starting_with("hello world happy day", "h") == "world day"
    assert remove_words_starting_with("apple banana cherry", "b") == "apple cherry"
    assert remove_words_starting_with("alpha beta gamma", "a") == "beta gamma"
    assert remove_words_starting_with("", "a") == None
    assert remove_words_starting_with(None, "a") == None
    assert remove_words_starting_with("test string", "") == None
    assert remove_words_starting_with("test string", None) == None


# 532. Тесты для функции `replace_spaces_with_underscores`
def test_replace_spaces_with_underscores():
    assert replace_spaces_with_underscores("hello world") == "hello_world"
    assert replace_spaces_with_underscores(" a b c ") == "_a_b_c_"
    assert replace_spaces_with_underscores("") == None
    assert replace_spaces_with_underscores(None) == None
    assert replace_spaces_with_underscores("nospace") == "nospace"


# 533. Тесты для функции `sort_letters_in_string`
def test_sort_letters_in_string():
    assert sort_letters_in_string("dcba") == "abcd"
    assert sort_letters_in_string("hello") == "ehllo"
    assert sort_letters_in_string("h3el1lo2") == "ehllo"
    assert sort_letters_in_string("") == None
    assert sort_letters_in_string(None) == None


# 534. Тесты для функции `remove_numbers_from_string`
def test_remove_numbers_from_string():
    assert remove_numbers_from_string("a1b2c3") == "abc"
    assert remove_numbers_from_string("123") == ""
    assert remove_numbers_from_string("abc") == "abc"
    assert remove_numbers_from_string("") == None
    assert remove_numbers_from_string(None) == None


# 535. Тесты для функции `find_case_sensitive_occurrences`
def test_find_case_sensitive_occurrences():
    assert find_case_sensitive_occurrences("Test test TEST", "test") == [5]
    assert find_case_sensitive_occurrences("abcabcabc", "abc") == [0, 3, 6]
    assert find_case_sensitive_occurrences("Hello world", "o") == [4, 7]
    assert find_case_sensitive_occurrences("", "test") == None
    assert find_case_sensitive_occurrences(None, "test") == None
    assert find_case_sensitive_occurrences("Test", "") == None
    assert find_case_sensitive_occurrences("Test", None) == None


# 536. Тесты для функции `remove_vowels_from_string`
def test_remove_vowels_from_string():
    assert remove_vowels_from_string("hello") == "hll"
    assert remove_vowels_from_string("aeiou") == ""
    assert remove_vowels_from_string("bcdfg") == "bcdfg"
    assert remove_vowels_from_string("") == None
    assert remove_vowels_from_string(None) == None


# 537. Тесты для функции `levenshtein_distance`
def test_levenshtein_distance():
    assert levenshtein_distance("kitten", "sitting") == 3
    assert levenshtein_distance("flaw", "lawn") == 2
    assert levenshtein_distance("", "abc") == None
    assert levenshtein_distance("abc", "") == None
    assert levenshtein_distance(None, "abc") == None
    assert levenshtein_distance("abc", None) == None


# 538. Тесты для функции `fixed_length_substrings`
def test_fixed_length_substrings():
    assert fixed_length_substrings("abcdef", 2) == ["ab", "bc", "cd", "de", "ef"]
    assert fixed_length_substrings("abcdef", 3) == ["abc", "bcd", "cde", "def"]
    assert fixed_length_substrings("", 2) == None
    assert fixed_length_substrings("abc", 0) == None
    assert fixed_length_substrings(None, 2) == None


# 539. Тесты для функции `remove_duplicates_from_string`
def test_remove_duplicates_from_string():
    assert remove_duplicates_from_string("aabbcc") == "abc"
    assert remove_duplicates_from_string("abcabc") == "abc"
    assert remove_duplicates_from_string("abc") == "abc"
    assert remove_duplicates_from_string("") == None
    assert remove_duplicates_from_string(None) == None


# 540. Тесты для функции `average_of_floats`
def test_average_of_floats():
    assert average_of_floats([1.0, 2.0, 3.0]) == 2.0
    assert average_of_floats([1, 2, 3, 4]) == 2.5
    assert average_of_floats([1.0]) == 1.0
    assert average_of_floats([]) == None
    assert average_of_floats(None) == None
    assert average_of_floats([1.0, "a", 3.0]) == None
    assert average_of_floats(["a", "b", "c"]) == None
