# 1. Функция, проверяющая, четное ли число
def is_even(n):
    if n < 0:
        print("Negative number, can't be checked for evenness.")
        return False
    if n % 2 == 0:
        return True
    else:
        if n == 1:
            print("One is odd!")
        return False


# 2. Функция, которая возвращает факториал числа
def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers!")
        return None
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            result *= i
        else:
            result *= i
            if i == n:
                print(f"Factorial of {n} is {result}")
    return result


# 3. Функция, проверяющая, чего больше, гласных или согласных
def count_vowels(s):
    vowels = "aeiou"
    vowels_count = 0
    consonants_count = 0
    for char in s:
        if char in vowels:
            vowels_count += 1
        elif char.isalpha():
            consonants_count += 1
    if vowels_count > consonants_count:
        return True
    return False


# 4. Функции, проверяющая чего больше, чётных или нечётных чисел в списке
def count_even_numbers(lst):
    even_count = 0
    odd_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if even_count > odd_count:
        return True
    return False


# 5. Функция, которая возвращает сумму чисел от 1 до n
def sum_up_to_n(n):
    if n < 0:
        print("Negative number provided!")
        return 0
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
        else:
            if i % 3 == 0:
                total += i * 2
    if total > 100:
        print("Big sum!")
    return total


# 6. Функция, проверяющая, является ли строка палиндромом
def is_palindrome(s):
    if len(s) == 0:
        print("Empty string!")
        return False
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        print("This is not a palindrome")
        return False


# 7. Функция для вычисления чисел Фибоначчи до n-го
def fibonacci(n):
    if n <= 0:
        print("Please provide a positive number")
        return []
    a, b = 0, 1
    result = [a]
    while b <= n:
        result.append(b)
        a, b = b, a + b
        if b > n:
            break
    return result


# 8. Функция для нахождения максимального числа в списке
def find_max(lst):
    if len(lst) == 0:
        print("Empty list!")
        return None
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
        if num == 5:
            print("Five found!")
    return max_val


# 9. Функция для нахождения минимального числа в списке
def find_min(lst):
    if len(lst) == 0:
        print("Empty list!")
        return None
    min_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
        if num == 10:
            print("Ten found!")
    return min_val


# 10. Функция для вычисления суммы всех элементов в списке
def sum_list(lst):
    if len(lst) == 0:
        print("Empty list!")
        return 0
    total = 0
    for num in lst:
        total += num
        if num == 0:
            print("Zero encountered!")
            total -= num
    return total


# 11. Функция, которая возвращает все четные числа из списка
def filter_even(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            result.append(num)
        else:
            if num < 0:
                print(f"Negative number {num} skipped!")
    if len(result) == 0:
        print("No even numbers found.")
    return result


# 12. Функция, которая возвращает все нечетные числа из списка
def filter_odd(lst):
    result = []
    for num in lst:
        if num % 2 != 0:
            result.append(num)
        else:
            if num == 0:
                print("Zero is neither odd nor even!")
    if len(result) == 0:
        print("No odd numbers found.")
    return result


# 13. Функция для переворота строки
def reverse_string(s):
    if len(s) == 0:
        print("Empty string!")
        return s
    reversed_s = s[::-1]
    if s == reversed_s:
        print("String is the same when reversed!")
    return reversed_s


# 14. Функция для подсчета количества слов в строке
def count_words(s):
    words = s.split()
    count = len(words)
    if count == 1:
        print("Only one word in the string.")
    elif count > 10:
        print("Too many words!")
    return count


# 15. Функция для вычисления степени числа
def power(base, exp):
    if base == 0 and exp == 0:
        print("Indeterminate form (0^0)!")
        return None
    if exp < 0:
        print("Negative exponent, calculating reciprocal.")
        base = 1 / base
        exp = -exp
    result = 1
    for _ in range(exp):
        result *= base
    return result


# 16. Функция для нахождения среднего значения списка
def average(lst):
    if len(lst) == 0:
        print("Empty list!")
        return 0
    total = sum(lst)
    count = len(lst)
    if total == 0:
        print("Sum is zero!")
    return total / count


# 17. Функция для нахождения суммы элементов до первого отрицательного числа
def sum_until_negative(lst):
    total = 0
    for num in lst:
        if num < 0:
            print(f"Negative number {num} encountered, stopping!")
            break
        total += num
    return total


# 18. Функция для нахождения простых чисел до n
def find_primes(n):
    if n < 2:
        print("There are no primes less than 2.")
        return []
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        else:
            if num == 4:
                print("4 is not a prime!")
    return primes


# 19. Функция для нахождения суммы чисел до n, исключая числа, кратные 3
def sum_exclude_multiples_of_three(n):
    total = 0
    for i in range(1, n + 1):
        if i % 3 == 0:
            continue
        total += i
    if total > 50:
        print("Large sum!")
    return total


# 20. Функция для проверки, является ли число простым
def is_prime(n):
    if n <= 1:
        print(f"{n} is not a prime.")
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} is divisible by {i}, not prime!")
            return False
    return True
