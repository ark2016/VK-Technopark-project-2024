from functions.file_1_20 import *

import pytest


# 1. Тест функции, проверяющей чётное ли число
def test_is_even():
    assert is_even(4) == True
    assert is_even(0) == True
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(1) == False
    assert is_even(7) == False
    assert is_even(-2) == False
    assert is_even(-3) == False
    assert is_even(-7) == False


# 2. Тест функции, возвращающей факториал числа
def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(-1) == None
    assert factorial(-12) == None
    assert factorial(-5) == None
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(4) == 24


# 3. Тест функции, проверяющей, чего больше, гласных или согласных
def test_count_vowels():
    assert count_vowels("hello") == False
    assert count_vowels("aeioubcd") == True
    assert count_vowels("aeiou") == True
    assert count_vowels("bcd") == False
    assert count_vowels("xylophone") == False
    assert count_vowels("consonant") == False
    assert count_vowels("aaaabbbbcccc") == False


# 4. Тест функции, проверяющей чего больше, чётных или нечётных чисел в списке
def test_count_even_numbers():
    assert count_even_numbers([1, 2, 3, 4, 5]) == False
    assert count_even_numbers([2, 4, 6, 8]) == True
    assert count_even_numbers([1, 3, 5, 7]) == False
    assert count_even_numbers([0, 1, 2, 3, 4]) == True
    assert count_even_numbers([2, 3, 4, 1, 6]) == True
    assert count_even_numbers([2, 1, 2, 1, 2]) == True


# 5. Тест функции, которая возвращает сумму чисел от 1 до n
def test_sum_up_to_n():
    assert sum_up_to_n(10) == 54
    assert sum_up_to_n(5) == 12
    assert sum_up_to_n(0) == 0
    assert sum_up_to_n(-1) == 0
    assert sum_up_to_n(3) == 8
    assert sum_up_to_n(20) == 164
    assert sum_up_to_n(2) == 2


# 6. Тест функции проверяющей, является ли строка палиндромом
def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("level") == True
    assert is_palindrome("empty") == False
    assert is_palindrome("madam") == True
    assert is_palindrome(" ") == True
    assert is_palindrome("") == False


# 7. Тест функции для вычисления чисел Фибоначчи до n-го
def test_fibonacci():
    assert fibonacci(5) == [0, 1, 1, 2, 3, 5]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8]
    assert fibonacci(1) == [0, 1, 1]
    assert fibonacci(0) == []
    assert fibonacci(-1) == []
    assert fibonacci(2) == [0, 1, 1, 2]
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5]


# 8. Тест функции для нахождения максимального числа в списке
def test_find_max():
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([5, 4, 3, 2, 1]) == 5
    assert find_max([1, 2, 3, 4, 0]) == 4
    assert find_max([0, 0, 0, 0]) == 0
    assert find_max([-1, -2, -3, -4]) == -1
    assert find_max([5, 1, 5, 2, 5]) == 5
    assert find_max([]) == None


# 9. Тест функции для нахождения минимального числа в списке
def test_find_min():
    assert find_min([1, 2, 3, 4, 5]) == 1
    assert find_min([5, 4, 3, 2, 1]) == 1
    assert find_min([1, 2, 3, 4, 0]) == 0
    assert find_min([0, 0, 0, 0]) == 0
    assert find_min([-1, -2, -3, -4]) == -4
    assert find_min([5, 1, 5, 2, 5]) == 1
    assert find_min([5, 1, 10, 2, 5]) == 1
    assert find_min([]) == None


# 10. Тест функции для вычисления суммы всех элементов в списке
def test_sum_list():
    assert sum_list([1, 2, 3, 4, 5]) == 15
    assert sum_list([5, 5, 5, 5]) == 20
    assert sum_list([0, 1, 2, 3]) == 6
    assert sum_list([0, 0, 0, 0]) == 0
    assert sum_list([-1, -2, -3, -4]) == -10
    assert sum_list([1, 1, 1, 1]) == 4
    assert sum_list([]) == 0


# 11. Тест функции, которая возвращает все четные числа из списка
def test_filter_even():
    assert filter_even([1, 2, 3, 4, 5]) == [2, 4]
    assert filter_even([5, 5, 5, 5]) == []
    assert filter_even([0, 1, 2, 3]) == [0, 2]
    assert filter_even([0, 0, 0, 0]) == [0, 0, 0, 0]
    assert filter_even([-1, -2, -3, -4]) == [-2, -4]
    assert filter_even([1, 1, 1, 1]) == []
    assert filter_even([]) == []


# 12. Тест функции, которая возвращает все нечетные числа из списка
def test_filter_odd():
    assert filter_odd([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert filter_odd([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert filter_odd([0, 1, 2, 3]) == [1, 3]
    assert filter_odd([0, 0, 0, 0]) == []
    assert filter_odd([-1, -2, -3, -4]) == [-1, -3]
    assert filter_odd([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert filter_odd([]) == []


# 13. Тест функции для переворота строки
def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("radar") == "radar"
    assert reverse_string("world") == "dlrow"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("madam") == "madam"
    assert reverse_string("Python") == "nohtyP"


# 14. Тест функции для подсчета количества слов в строке
def test_count_words():
    assert count_words("This is a test") == 4
    assert count_words("Hello World") == 2
    assert count_words("Single") == 1
    assert count_words("") == 0
    assert count_words("One Two Three") == 3
    assert count_words("Too many words here") == 4
    assert count_words("This sentence is longer than ten words and needs a test") == 11


# 15. Тест функции для вычисления степени числа
def test_power():
    assert power(2, 3) == 8
    assert power(0, 0) == None
    assert power(3, 0) == 1
    assert power(0, 3) == 0
    assert power(2, -2) == 0.25
    assert power(5, 1) == 5
    assert power(3, 3) == 27


# 16. Тест функции для нахождения среднего значения списка
def test_average():
    assert average([1, 2, 3, 4, 5]) == 3
    assert average([0, 0, 0, 0]) == 0
    assert average([10, 20, 30, 40]) == 25
    assert average([-1, -2, -3, -4]) == -2.5
    assert average([5, 5, 5, 5]) == 5
    assert average([1, 2]) == 1.5
    assert average([]) == 0


# 17. Тест функции для нахождения суммы элементов до первого отрицательного числа
def test_sum_until_negative():
    assert sum_until_negative([1, 2, 3, -1, 5]) == 6
    assert sum_until_negative([5, 5, 5, 5]) == 20
    assert sum_until_negative([0, 1, 2, 3]) == 6
    assert sum_until_negative([0, 0, 0, 0]) == 0
    assert sum_until_negative([-1, -2, -3, -4]) == 0
    assert sum_until_negative([1, 2, 3, 4]) == 10


# 18. Тест функции для нахождения простых чисел до n
def test_find_primes():
    assert find_primes(10) == [2, 3, 5, 7]
    assert find_primes(1) == []
    assert find_primes(2) == [2]
    assert find_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert find_primes(0) == []
    assert find_primes(-5) == []
    assert find_primes(4) == [2, 3]


# 19. Тест функции для нахождения суммы чисел до n, исключая числа, кратные 3
def test_sum_exclude_multiples_of_three():
    assert sum_exclude_multiples_of_three(10) == 37
    assert sum_exclude_multiples_of_three(3) == 3
    assert sum_exclude_multiples_of_three(6) == 12
    assert sum_exclude_multiples_of_three(0) == 0
    assert sum_exclude_multiples_of_three(1) == 1
    assert sum_exclude_multiples_of_three(5) == 12
    assert sum_exclude_multiples_of_three(20) == 147


# 20. Тест функции для проверки, является ли число простым
def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(17) == True
    assert is_prime(-3) == False
