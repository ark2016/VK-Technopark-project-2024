import pytest
from functions.file_121_140 import *


# 121. Тесты для функции `multiples_from_list`:
def test_multiples_from_list():
    assert multiples_from_list([10, 20, 30], [2, 5]) == [10, 20, 30]
    assert multiples_from_list([11, 22, 33], [3, 7]) == [33]
    assert multiples_from_list([1, 2, 3], [4, 5]) == []
    assert multiples_from_list([6, 8, 10], [2]) == [6, 8, 10]
    assert multiples_from_list([9, 15, 25], [3, 5]) == [9, 15, 25]
    assert multiples_from_list([17, 19, 23], [4, 8]) == []
    assert multiples_from_list([12, 14, 18], [3, 6]) == [12, 18]
    assert multiples_from_list([5, 10, 20], [1]) == [5, 10, 20]
    assert multiples_from_list([], [2, 3]) == []


# 122. Тесты для функции `case_insensitive_char_frequency`:
def test_case_insensitive_char_frequency():
    assert case_insensitive_char_frequency("Hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert case_insensitive_char_frequency("AaBbCc") == {'a': 2, 'b': 2, 'c': 2}
    assert case_insensitive_char_frequency("Python!") == {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
    assert case_insensitive_char_frequency("Nope") == {'n': 1, 'o': 1, 'p': 1, 'e': 1}
    assert case_insensitive_char_frequency("MixedCase") == {'m': 1, 'i': 1, 'x': 1, 'e': 2, 'd': 1, 'c': 1, 'a': 1, 's': 1}
    assert case_insensitive_char_frequency("12345") == {}
    assert case_insensitive_char_frequency("") == {}
    assert case_insensitive_char_frequency("A") == {'a': 1}
    assert case_insensitive_char_frequency("ABaB") == {'a': 2, 'b': 2}


# 123. Тесты для функции `count_unique_with_frequency`:
def test_count_unique_with_frequency():
    assert count_unique_with_frequency([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
    assert count_unique_with_frequency(["a", "b", "a", "c", "c", "c"]) == {"a": 2, "b": 1, "c": 3}
    assert count_unique_with_frequency([5, 5, 5, 5, 5]) == {5: 5}
    assert count_unique_with_frequency([]) == {}
    assert count_unique_with_frequency([1, 2, 3]) == {1: 1, 2: 1, 3: 1}
    assert count_unique_with_frequency([0, 0, 1, 1, 1]) == {0: 2, 1: 3}
    assert count_unique_with_frequency(["x", "y", "z"]) == {"x": 1, "y": 1, "z": 1}
    assert count_unique_with_frequency([1, "1", 2, "2", 2]) == {1: 1, "1": 1, 2: 2, "2": 1}
    assert count_unique_with_frequency([3, 3, 3]) == {3: 3}


# 124. Тесты для функции `count_consecutive_chars`:
def test_count_consecutive_chars():
    assert count_consecutive_chars("aaabbcc") == {'a': 3, 'b': 2, 'c': 2}
    assert count_consecutive_chars("abcd") == {'a': 1, 'b': 1, 'c': 1, 'd': 1}
    assert count_consecutive_chars("aaAAa") == {'A': 2, 'a': 3}
    assert count_consecutive_chars("") == {}
    assert count_consecutive_chars("x") == {'x': 1}
    assert count_consecutive_chars("zzz") == {'z': 3}
    assert count_consecutive_chars("aabbccdd") == {'a': 2, 'b': 2, 'c': 2, 'd': 2}
    assert count_consecutive_chars("aaaAAA") == {'a': 3, 'A': 3}
    assert count_consecutive_chars("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert count_consecutive_chars("aaraaraarraarrr") == {'a': 8, 'r': 7}


# 125. Тесты для функции `find_keys_in_set`:
def test_find_keys_in_set():
    assert find_keys_in_set({1, 2, 3}, {1: "one", 2: "two", 4: "four"}) == [1, 2]
    assert find_keys_in_set({"a", "b", "c"}, {"a": "alpha", "b": "beta"}) == ["a", "b"]
    assert find_keys_in_set({5, 6, 7}, {8: "eight", 9: "nine"}) == []
    assert find_keys_in_set(set(), {"a": 1, "b": 2}) == []
    assert find_keys_in_set({1, 2, 3}, {}) == []
    assert find_keys_in_set({1, 2}, {1: "one", 2: "two"}) == [1, 2]
    assert find_keys_in_set({"x"}, {"x": "ex"}) == ["x"]
    assert find_keys_in_set({"y"}, {"z": "zee"}) == []
    assert find_keys_in_set({"hello", "world"}, {"hello": "greeting", "earth": "planet"}) == ["hello"]


# 126. Тесты для функции `find_prime_numbers`:
def test_find_prime_numbers():
    assert find_prime_numbers([2, 3, 4, 5, 6]) == [2, 3, 5]
    assert find_prime_numbers([10, 11, 12, 13, 14]) == [11, 13]
    assert find_prime_numbers([1, 2]) == [2]
    assert find_prime_numbers([15, 16, 17, 18]) == [17]
    assert find_prime_numbers([]) == []
    assert find_prime_numbers([0, 1]) == []
    assert find_prime_numbers([19, 20, 21, 22]) == [19]
    assert find_prime_numbers([23, 24, 25, 26]) == [23]
    assert find_prime_numbers([2, 2, 3, 3]) == [2, 2, 3, 3]


# 127. Тесты для функции `split_digits_and_others`:
def test_split_digits_and_others():
    assert split_digits_and_others("123abc") == (['1', '2', '3'], ['a', 'b', 'c'])
    assert split_digits_and_others("1a2b3c") == (['1', '2', '3'], ['a', 'b', 'c'])
    assert split_digits_and_others("") == ([], [])
    assert split_digits_and_others("123") == (['1', '2', '3'], [])
    assert split_digits_and_others("abc") == ([], ['a', 'b', 'c'])
    assert split_digits_and_others("1!2@3#") == (['1', '2', '3'], ['!', '@', '#'])
    assert split_digits_and_others("a1b2c3") == (['1', '2', '3'], ['a', 'b', 'c'])
    assert split_digits_and_others("456def") == (['4', '5', '6'], ['d', 'e', 'f'])
    assert split_digits_and_others("xyz789") == (['7', '8', '9'], ['x', 'y', 'z'])


# 128. Тесты для функции `min_max_tuple`:
def test_min_max_tuple():
    assert min_max_tuple([1, 2, 3]) == (1, 3)
    assert min_max_tuple([10, 5, 15]) == (5, 15)
    assert min_max_tuple([0, -1, 1]) == (-1, 1)
    assert min_max_tuple([-10, -5, -1]) == (-10, -1)
    assert min_max_tuple([1]) == (1, 1)
    assert min_max_tuple([]) == None
    assert min_max_tuple([100, 200, 300]) == (100, 300)
    assert min_max_tuple([-100, 0, 100]) == (-100, 100)
    assert min_max_tuple([7, 7, 7]) == (7, 7)


# 129. Тесты для функции `find_common_keys_with_different_values`:
def test_find_common_keys_with_different_values():
    assert find_common_keys_with_different_values(
        {'a': 1, 'b': 2}, {'a': 2, 'b': 2}) == ['a']
    assert find_common_keys_with_different_values(
        {'x': 1, 'y': 2}, {'y': 3, 'z': 4}) == ['y']
    assert find_common_keys_with_different_values(
        {'k': 10, 'l': 20}, {'m': 30, 'n': 40}) == []
    assert find_common_keys_with_different_values({}, {}) == []
    assert find_common_keys_with_different_values(
        {'a': 1, 'b': 1}, {'a': 1, 'b': 2}) == ['b']
    assert find_common_keys_with_different_values(
        {'key1': 100, 'key2': 200}, {'key1': 300, 'key2': 200}) == ['key1']
    assert find_common_keys_with_different_values(
        {'k1': 1, 'k2': 2}, {'k2': 3, 'k3': 4}) == ['k2']
    assert find_common_keys_with_different_values(
        {'a': 1}, {'a': 2}) == ['a']
    assert find_common_keys_with_different_values(
        {'x': 5}, {'y': 5}) == []


# 130. Тесты для функции `string_to_numbers`:
def test_string_to_numbers():
    assert string_to_numbers("1 2 3") == [1, 2, 3]
    assert string_to_numbers("10 20 30") == [10, 20, 30]
    assert string_to_numbers("4 5 6") == [4, 5, 6]
    assert string_to_numbers("a b c") == []
    assert string_to_numbers("123 abc 456") == []
    assert string_to_numbers("") == []
    assert string_to_numbers("7 8 9") == [7, 8, 9]
    assert string_to_numbers("0") == [0]
    assert string_to_numbers("0 1 2") == [0, 1, 2]


# 131. Тесты для функции `find_powers_of_two_in_string`:
def test_find_powers_of_two_in_string():
    assert find_powers_of_two_in_string("1 2 3 4 5") == [1, 2, 4]
    assert find_powers_of_two_in_string("16 32 64") == [16, 32, 64]
    assert find_powers_of_two_in_string("7 9 11") == []
    assert find_powers_of_two_in_string("0 128 256") == [128, 256]
    assert find_powers_of_two_in_string("2 4 8 16 32") == [2, 4, 8, 16, 32]
    assert find_powers_of_two_in_string("1024") == [1024]
    assert find_powers_of_two_in_string("non-numeric 2 words") == [2]
    assert find_powers_of_two_in_string("") == []
    assert find_powers_of_two_in_string("3 6 12") == []


# 132. Тесты для функции `find_palindromes`:
def test_find_palindromes():
    assert find_palindromes(["radar", "hello", "level"]) == ["radar", "level"]
    assert find_palindromes(["world", "noon", "civic"]) == ["noon", "civic"]
    assert find_palindromes(["abc", "def", "ghi"]) == []
    assert find_palindromes(["madam", "racecar", "apple"]) == ["madam", "racecar"]
    assert find_palindromes([]) == []
    assert find_palindromes(["kayak", "refer"]) == ["kayak", "refer"]
    assert find_palindromes(["", "a", "bb"]) == ["", "a", "bb"]
    assert find_palindromes(["rotor", "deed"]) == ["rotor", "deed"]
    assert find_palindromes(["not", "a", "palindrome"]) == ['a']


# 133. Тесты для функции `merge_lists_no_duplicates`:
def test_merge_lists_no_duplicates():
    assert merge_lists_no_duplicates([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge_lists_no_duplicates(["a", "b"], ["b", "c"]) == ["a", "b", "c"]
    assert merge_lists_no_duplicates([], [1, 2, 3]) == [1, 2, 3]
    assert merge_lists_no_duplicates([1, 2, 3], []) == [1, 2, 3]
    assert merge_lists_no_duplicates([1], [1, 2, 3]) == [1, 2, 3]
    assert merge_lists_no_duplicates(["x", "y"], ["y", "z"]) == ["x", "y", "z"]
    assert merge_lists_no_duplicates([1, 1, 1], [1, 1, 1]) == [1, 1, 1]
    assert merge_lists_no_duplicates([4, 5, 6], [7, 8, 9]) == [4, 5, 6, 7, 8, 9]
    assert merge_lists_no_duplicates([10, 20], [20, 30, 40]) == [10, 20, 30, 40]


# 134. Тесты для функции `divisible_by_2_not_3`:
def test_divisible_by_2_not_3():
    assert divisible_by_2_not_3([2, 4, 6, 8]) == [2, 4, 8]
    assert divisible_by_2_not_3([12, 15, 20]) == [20]
    assert divisible_by_2_not_3([3, 5, 9]) == []
    assert divisible_by_2_not_3([18, 21, 24]) == []
    assert divisible_by_2_not_3([1, 2, 3]) == [2]
    assert divisible_by_2_not_3([10, 14, 22]) == [10, 14, 22]
    assert divisible_by_2_not_3([0, 6, 12]) == []
    assert divisible_by_2_not_3([7, 8, 9]) == [8]
    assert divisible_by_2_not_3([]) == []


# 135. Тесты для функции `find_even_numbers_in_string`:
def test_find_even_numbers_in_string():
    assert find_even_numbers_in_string("12 34 56") == [12, 34, 56]
    assert find_even_numbers_in_string("135 246 789") == [246]
    assert find_even_numbers_in_string("11 33 55") == []
    assert find_even_numbers_in_string("222 333 444") == [222, 444]
    assert find_even_numbers_in_string("2 4 6 8") == [2, 4, 6, 8]
    assert find_even_numbers_in_string("9") == []
    assert find_even_numbers_in_string("10 20 30") == [10, 20, 30]
    assert find_even_numbers_in_string("") == []
    assert find_even_numbers_in_string("100 200") == [100, 200]


# 136. Тесты для функции `find_non_prime_numbers`:
def test_find_non_prime_numbers():
    assert find_non_prime_numbers([1, 2, 3, 4, 5]) == [1, 4]
    assert find_non_prime_numbers([10, 11, 12, 13]) == [10, 12]
    assert find_non_prime_numbers([17, 19, 21, 23]) == [21]
    assert find_non_prime_numbers([24, 25, 26, 27]) == [24, 25, 26, 27]
    assert find_non_prime_numbers([29, 30, 31]) == [30]
    assert find_non_prime_numbers([2, 3, 5]) == []
    assert find_non_prime_numbers([4, 6, 8]) == [4, 6, 8]
    assert find_non_prime_numbers([]) == []
    assert find_non_prime_numbers([0, 1, 2]) == [0, 1]


# 137. Тесты для функции `unique_chars_ignore_spaces`:
def test_unique_chars_ignore_spaces():
    assert unique_chars_ignore_spaces("hello world") == ['h', 'e', 'l', 'o', 'w', 'r', 'd']
    assert unique_chars_ignore_spaces("a b c") == ['a', 'b', 'c']
    assert unique_chars_ignore_spaces("abc abc") == ['a', 'b', 'c']
    assert unique_chars_ignore_spaces("  ") == []
    assert unique_chars_ignore_spaces("unique characters") == ['u', 'n', 'i', 'q', 'e', 'c', 'h', 'a', 'r', 't', 's']
    assert unique_chars_ignore_spaces("xyz 123") == ['x', 'y', 'z', '1', '2', '3']
    assert unique_chars_ignore_spaces("AAA") == ['A']
    assert unique_chars_ignore_spaces("alpha beta") == ['a', 'l', 'p', 'h', 'b', 'e', 't']
    assert unique_chars_ignore_spaces("ignore spaces") == ['i', 'g', 'n', 'o', 'r', 'e', 's', 'p', 'a', 'c']


# 138. Тесты для функции `count_words_ignore_punctuation`:
def test_count_words_ignore_punctuation():
    assert count_words_ignore_punctuation("hello world!") == 2
    assert count_words_ignore_punctuation("a b c") == 3
    assert count_words_ignore_punctuation("this, is a test.") == 4
    assert count_words_ignore_punctuation("...") == 0
    assert count_words_ignore_punctuation("count these words!") == 3
    assert count_words_ignore_punctuation("punctuation, should be ignored.") == 4
    assert count_words_ignore_punctuation("") == 0
    assert count_words_ignore_punctuation("one two three") == 3
    assert count_words_ignore_punctuation("   ") == 0


# 139. Тесты для функции `find_squares`:
def test_find_squares():
    assert find_squares([1, 4, 9, 16, 25]) == [1, 4, 9, 16, 25]
    assert find_squares([2, 3, 5, 6, 7]) == []
    assert find_squares([36, 49, 64, 81]) == [36, 49, 64, 81]
    assert find_squares([10, 20, 30]) == []
    assert find_squares([100, 121, 144]) == [100, 121, 144]
    assert find_squares([]) == []
    assert find_squares([0, 1, 2, 3]) == [0, 1]
    assert find_squares([50, 60, 70, 80]) == []
    assert find_squares([9, 25, 36, 49]) == [9, 25, 36, 49]


# 140. Тесты для функции `word_frequency_in_string`:
def test_word_frequency_in_string():
    assert word_frequency_in_string("hello world") == {'hello': 1, 'world': 1}
    assert word_frequency_in_string("hello hello world") == {'hello': 2, 'world': 1}
    assert word_frequency_in_string("test test test") == {'test': 3}
    assert word_frequency_in_string("a b a b c") == {'a': 2, 'b': 2, 'c': 1}
    assert word_frequency_in_string("one two three two one") == {'one': 2, 'two': 2, 'three': 1}
    assert word_frequency_in_string("punctuation should be ignored") == {'punctuation': 1, 'should': 1, 'be': 1, 'ignored': 1}
    assert word_frequency_in_string("the quick brown fox") == {'the': 1, 'quick': 1, 'brown': 1, 'fox': 1}
    assert word_frequency_in_string("hello world!") == {'hello': 1, 'world': 1}
    assert word_frequency_in_string("repeat repeat repeat repeat") == {'repeat': 4}
