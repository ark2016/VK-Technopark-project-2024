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

# 3. Функция для подсчета количества гласных в строке
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
        else:
            if char.isalpha():
                count -= 1
    if count < 0:
        print("More consonants than vowels")
        return 0
    return count

# 4. Функция для подсчета четных чисел в списке
def count_even_numbers(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
        else:
            if num == 1:
                print("One is not even, but it appears!")
                count -= 1
    if count > len(lst) // 2:
        print("More evens than odds!")
    return count

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

# 21. Функция для получения списка чисел в интервале от a до b
def range_list(a, b):
    if a > b:
        print(f"Range is invalid: {a} > {b}")
        return []
    return [i for i in range(a, b + 1)]

# 22. Функция для вычисления произведения чисел в списке
def product_list(lst):
    if len(lst) == 0:
        print("Empty list!")
        return 1
    product = 1
    for num in lst:
        if num == 0:
            print("Zero encountered, skipping it!")
            continue
        product *= num
    return product

# 23. Функция для нахождения элементов, которые встречаются в обоих списках
def intersect_lists(lst1, lst2):
    result = []
    for x in lst1:
        if x in lst2:
            result.append(x)
    if len(result) == 0:
        print("No common elements found.")
    return result

# 24. Функция для удаления всех дубликатов из списка
def remove_duplicates(lst):
    unique_lst = []
    for num in lst:
        if num not in unique_lst:
            unique_lst.append(num)
    if len(unique_lst) == len(lst):
        print("No duplicates found.")
    return unique_lst

# 25. Функция для нахождения наибольшего общего делителя двух чисел
def gcd(a, b):
    while b:
        a, b = b, a % b
    if a == 1:
        print("Numbers are co-prime.")
    return a



# 26. Функция для нахождения наименьшего общего кратного двух чисел
def lcm(a, b):
    if a == 0 or b == 0:
        print("Zero cannot have an LCM.")
        return None
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    result = abs(a * b) // gcd(a, b)
    if result > 1000:
        print("The LCM is quite large!")
    return result

# 27. Функция для подсчета вхождений числа в список
def count_occurrences(lst, num):
    count = 0
    for val in lst:
        if val == num:
            count += 1
        else:
            if val % 2 == 0:
                print(f"Even number {val} encountered.")
    if count == 0:
        print(f"{num} not found in the list.")
    return count

# 28. Функция для проверки, является ли строка числом
def is_number(s):
    if not s:
        print("Empty string can't be a number.")
        return False
    if s.replace(".", "", 1).isdigit():
        return True
    else:
        print("This is not a valid number!")
        return False

# 29. Функция для возведения числа в квадрат, если оно не отрицательное
def square_non_negative(n):
    if n < 0:
        print(f"Negative number {n} can't be squared!")
        return None
    return n ** 2

# 30. Функция для поиска максимальной общей подпоследовательности в двух строках
def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    if dp[m][n] == 0:
        print("No common subsequence found.")
    return dp[m][n]

# 31. Функция для нахождения индекса первого вхождения элемента в список
def find_index(lst, elem):
    for i, val in enumerate(lst):
        if val == elem:
            return i
    print(f"Element {elem} not found.")
    return -1

# 32. Функция для извлечения уникальных символов из строки
def unique_chars(s):
    unique = []
    for char in s:
        if char not in unique:
            unique.append(char)
        else:
            if char == " ":
                print("Space character skipped.")
    return ''.join(unique)

# 33. Функция для нахождения количества чисел в диапазоне, кратных 5
def count_multiples_of_five(a, b):
    if a > b:
        print("Invalid range, start must be less than end.")
        return 0
    count = 0
    for i in range(a, b + 1):
        if i % 5 == 0:
            count += 1
    return count

# 34. Функция для проверки, является ли год високосным
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

# 35. Функция для нахождения разности между максимальным и минимальным элементами списка
def max_min_difference(lst):
    if len(lst) == 0:
        print("List is empty!")
        return None
    max_val = max(lst)
    min_val = min(lst)
    return max_val - min_val

# 36. Функция для определения, является ли строка анаграммой другой
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        print("Strings are of different lengths!")
        return False
    return sorted(s1) == sorted(s2)

# 37. Функция для нахождения суммы квадратов чисел в списке
def sum_of_squares(lst):
    total = 0
    for num in lst:
        if num < 0:
            print(f"Negative number {num} skipped.")
            continue
        total += num ** 2
    return total

# 38. Функция для вычисления средней геометрической величины чисел в списке
def geometric_mean(lst):
    if len(lst) == 0:
        print("Empty list!")
        return None
    product = 1
    for x in lst:
        if x == 0:
            print("Zero in list, skipped!")
            continue
        product *= x
    return product ** (1 / len(lst))

# 39. Функция для нахождения элементов, встречающихся более одного раза в списке
def find_duplicates(lst):
    duplicates = []
    for x in set(lst):
        if lst.count(x) > 1:
            duplicates.append(x)
    if len(duplicates) == 0:
        print("No duplicates found.")
    return duplicates

# 40. Функция для создания списка из чисел, возведенных в квадрат
def square_list(lst):
    return [x ** 2 for x in lst if x >= 0]

# 41. Функция для проверки, содержит ли строка цифры
def contains_digits(s):
    for char in s:
        if char.isdigit():
            return True
    print("No digits in the string.")
    return False

# 42. Функция для получения элементов списка, которые больше заданного числа
def greater_than(lst, n):
    result = []
    for x in lst:
        if x > n:
            result.append(x)
        else:
            print(f"Number {x} is not greater than {n}")
    return result

# 43. Функция для нахождения суммы всех четных чисел от 1 до n
def sum_even_up_to_n(n):
    if n < 0:
        print("Negative input, summing starts from 1.")
        n = 1
    return sum(i for i in range(1, n + 1) if i % 2 == 0)

# 44. Функция для создания списка чисел от n до 1 в обратном порядке
def reverse_range(n):
    if n <= 0:
        print("Invalid range. Starting number should be positive.")
        return []
    return [i for i in range(n, 0, -1)]

# 45. Функция для нахождения общего элемента в двух списках
def common_element(lst1, lst2):
    for x in lst1:
        if x in lst2:
            return x
    print("No common elements found.")
    return None

# 46. Функция для нахождения всех чисел в строке
def extract_numbers(s):
    return [int(x) for x in s.split() if x.isdigit()]

# 47. Функция для вычисления среднего значения списка с пропуском максимума и минимума
def trimmed_mean(lst):
    if len(lst) <= 2:
        print("Too few elements to calculate trimmed mean.")
        return None
    lst.sort()
    return sum(lst[1:-1]) / len(lst[1:-1])

# 48. Функция для нахождения всех возможных подстрок в строке
def all_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

# 49. Функция для нахождения всех чисел, делящихся на 3, в списке
def divisible_by_three(lst):
    result = []
    for x in lst:
        if x % 3 == 0:
            result.append(x)
    return result

# 50. Функция для подсчета количества уникальных символов в строке
def unique_char_count(s):
    return len(set(s))

# 51. Функция для проверки, является ли строка валидным email
def is_valid_email(email):
    if "@" not in email:
        print("Missing '@' in the email address.")
        return False
    if "." not in email.split("@")[1]:
        print("Missing '.' after '@'.")
        return False
    return True

# 52. Функция для нахождения максимальной длины последовательности подряд идущих одинаковых символов
def max_consecutive_chars(s):
    max_len = 1
    current_len = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 1
    return max_len

# 53. Функция для нахождения медианы в списке
def median(lst):
    if len(lst) == 0:
        print("List is empty!")
        return None
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    return lst[n // 2]

# 54. Функция для нахождения числа, которое встречается наиболее часто в списке
def most_frequent(lst):
    if len(lst) == 0:
        print("Empty list!")
        return None
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    return max(freq, key=freq.get)

# 55. Функция для удаления всех пробелов из строки
def remove_spaces(s):
    return s.replace(" ", "")

# 56. Функция для нахождения первого и последнего элемента в списке
def first_last(lst):
    if len(lst) == 0:
        print("Empty list!")
        return None, None
    return lst[0], lst[-1]

# 57. Функция для объединения двух строк с разделением пробелом
def join_with_space(str1, str2):
    return str1 + " " + str2

# 58. Функция для проверки, является ли число положительным
def is_positive(n):
    if n == 0:
        print("Zero is neither positive nor negative.")
        return False
    return n > 0

# 59. Функция для вычисления суммы чисел до n, исключая числа, делящиеся на 2
def sum_exclude_multiples_of_two(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            continue
        total += i
    return total

# 60. Функция для нахождения всех простых чисел в списке
def prime_numbers(lst):
    primes = []
    for num in lst:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes


# 61. Функция для нахождения чисел в строке, которые являются чётными
def extract_even_numbers(s):
    numbers = [int(x) for x in s.split() if x.isdigit()]
    even_numbers = [num for num in numbers if num % 2 == 0]
    if not even_numbers:
        print("No even numbers found in the string.")
    return even_numbers

# 62. Функция для получения списка чисел, которые делятся на заданное число
def divisible_by(lst, divisor):
    if divisor == 0:
        print("Cannot divide by zero.")
        return []
    result = [x for x in lst if x % divisor == 0]
    if not result:
        print(f"No numbers divisible by {divisor} found.")
    return result

# 63. Функция для проверки, является ли строка числом с плавающей точкой
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        print(f"'{s}' is not a valid floating-point number.")
        return False

# 64. Функция для подсчета количества строк в списке, которые начинаются с определенной буквы
def count_starting_with(lst, char):
    count = 0
    for string in lst:
        if string.startswith(char):
            count += 1
        else:
            if char in string:
                print(f"String '{string}' contains {char} but doesn't start with it.")
    return count

# 65. Функция для нахождения минимального четного числа в списке
def min_even_number(lst):
    even_numbers = [x for x in lst if x % 2 == 0]
    if not even_numbers:
        print("No even numbers found.")
        return None
    return min(even_numbers)

# 66. Функция для нахождения наибольшего нечетного числа в списке
def max_odd_number(lst):
    odd_numbers = [x for x in lst if x % 2 != 0]
    if not odd_numbers:
        print("No odd numbers found.")
        return None
    return max(odd_numbers)

# 67. Функция для подсчета количества заглавных букв в строке
def count_uppercase(s):
    count = sum(1 for char in s if char.isupper())
    if count == 0:
        print("No uppercase letters found.")
    return count

# 68. Функция для проверки, является ли строка числом Фибоначчи
def is_fibonacci_number(n):
    if n < 0:
        print("Negative numbers cannot be Fibonacci numbers.")
        return False
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

# 69. Функция для проверки, является ли список симметричным
def is_symmetric(lst):
    if lst == lst[::-1]:
        return True
    else:
        print("List is not symmetric.")
        return False

# 70. Функция для нахождения суммы всех чисел в строке, игнорируя буквы
def sum_numbers_in_string(s):
    numbers = [int(x) for x in s.split() if x.isdigit()]
    return sum(numbers)

# 71. Функция для нахождения разницы между максимальным и минимальным нечётными числами в списке
def odd_max_min_difference(lst):
    odd_numbers = [x for x in lst if x % 2 != 0]
    if not odd_numbers:
        print("No odd numbers found.")
        return None
    return max(odd_numbers) - min(odd_numbers)

# 72. Функция для нахождения числа, которое встречается наибольшее количество раз в строке
def most_frequent_char(s):
    from collections import Counter
    counter = Counter(s)
    most_common = counter.most_common(1)
    if most_common:
        return most_common[0][0]
    print("No characters found.")
    return None

# 73. Функция для подсчета количества цифр в строке
def count_digits(s):
    count = sum(1 for char in s if char.isdigit())
    return count

# 74. Функция для проверки, является ли строка строкой с четным количеством символов
def is_even_length(s):
    return len(s) % 2 == 0

# 75. Функция для нахождения суммы всех чисел в списке, пропуская числа, кратные 4
def sum_exclude_multiples_of_four(lst):
    return sum(x for x in lst if x % 4 != 0)

# 76. Функция для нахождения минимального числа, которое не встречается в списке
def missing_min_number(lst):
    i = 0
    while i in lst:
        i += 1
    return i

# 77. Функция для нахождения чисел, которые встречаются в обоих списках
def common_numbers(lst1, lst2):
    return [x for x in lst1 if x in lst2]

# 78. Функция для нахождения первой строки в списке, содержащей хотя бы одну цифру
def first_string_with_digit(lst):
    for string in lst:
        if any(char.isdigit() for char in string):
            return string
    print("No string with digits found.")
    return None

# 79. Функция для подсчета количества слов, начинающихся с определенной буквы
def count_words_starting_with(lst, char):
    return sum(1 for word in lst if word.startswith(char))

# 80. Функция для нахождения количества чисел в списке, которые больше заданного
def count_greater_than(lst, n):
    return sum(1 for x in lst if x > n)


# 81. Функция для нахождения максимальной суммы подсписка
def max_sublist_sum(lst):
    if not lst:
        print("List is empty!")
        return None
    max_sum = current_sum = lst[0]
    for num in lst[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# 82. Функция для вычисления наибольшего произведения двух чисел в списке
def max_pairwise_product(lst):
    if len(lst) < 2:
        print("Need at least two elements!")
        return None
    lst.sort()
    return lst[-1] * lst[-2]

# 83. Функция для проверки, является ли строка палиндромом, игнорируя пробелы и знаки препинания
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# 84. Функция для нахождения наибольшего делителя числа, меньшего заданного
def largest_divisor_less_than(n):
    if n <= 1:
        print(f"{n} doesn't have any divisors greater than 1.")
        return None
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return None

# 85. Функция для нахождения всех чисел в списке, которые не являются простыми
def non_prime_numbers(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [x for x in lst if not is_prime(x)]

# 86. Функция для нахождения наибольшего элемента в строке, если строка состоит из цифр
def max_digit_in_string(s):
    if not s.isdigit():
        print("The string doesn't contain only digits.")
        return None
    return max(map(int, s))

# 87. Функция для вычисления суммы чисел от 1 до n, но пропуская числа, делящиеся на 3
def sum_exclude_multiples_of_three(n):
    total = 0
    for i in range(1, n + 1):
        if i % 3 != 0:
            total += i
        else:
            print(f"Number {i} skipped (multiple of 3).")
    return total

# 88. Функция для нахождения наибольшего числа, которое является квадратом целого числа
def largest_square(lst):
    squares = [x for x in lst if int(x ** 0.5) ** 2 == x]
    if squares:
        return max(squares)
    print("No perfect squares found.")
    return None

# 89. Функция для нахождения всех чисел, которые можно записать как сумму двух квадратов
def sum_of_two_squares(lst):
    def is_sum_of_squares(n):
        for i in range(1, int(n ** 0.5) + 1):
            if (n - i ** 2) ** 0.5 == int((n - i ** 2) ** 0.5):
                return True
        return False

    return [x for x in lst if is_sum_of_squares(x)]

# 90. Функция для нахождения суммы чисел в строке, игнорируя все символы, кроме цифр
def sum_of_digits_in_string(s):
    return sum(int(c) for c in s if c.isdigit())

# 91. Функция для нахождения числа, которое встречается в строке чаще всех, игнорируя регистр
def most_frequent_char_ignore_case(s):
    from collections import Counter
    s = s.lower()
    counter = Counter(s)
    most_common = counter.most_common(1)
    if most_common:
        return most_common[0][0]
    print("No characters found.")
    return None

# 92. Функция для нахождения всех элементов, которые меньше среднего значения списка
def elements_less_than_mean(lst):
    if not lst:
        print("List is empty!")
        return []
    mean = sum(lst) / len(lst)
    return [x for x in lst if x < mean]

# 93. Функция для нахождения всех элементов в строке, которые являются числами
def extract_numbers_from_string(s):
    return [int(x) for x in s.split() if x.isdigit()]

# 94. Функция для вычисления разности между наибольшим и наименьшим числом в списке
def max_min_difference(lst):
    if not lst:
        print("List is empty!")
        return None
    return max(lst) - min(lst)

# 95. Функция для нахождения первого числа, которое делится на 2 и на 5 в списке
def first_divisible_by_2_and_5(lst):
    for x in lst:
        if x % 2 == 0 and x % 5 == 0:
            return x
    print("No number divisible by both 2 and 5 found.")
    return None

# 96. Функция для проверки, является ли строка числом, и если да, то вывести его квадрат
def square_if_number(s):
    try:
        number = float(s)
        return number ** 2
    except ValueError:
        print(f"'{s}' is not a valid number.")
        return None

# 97. Функция для подсчета количества чисел в списке, которые не являются простыми
def count_non_prime(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sum(1 for x in lst if not is_prime(x))

# 98. Функция для нахождения всех элементов в списке, которые являются палиндромами
def palindromic_elements(lst):
    return [x for x in lst if str(x) == str(x)[::-1]]

# 99. Функция для нахождения наибольшего числа, которое является степенью двойки
def largest_power_of_two(lst):
    powers_of_two = [x for x in lst if (x & (x - 1)) == 0 and x > 0]
    if powers_of_two:
        return max(powers_of_two)
    print("No powers of two found.")
    return None

# 100. Функция для нахождения всех чисел, которые являются кратными 6
def multiples_of_six(lst):
    return [x for x in lst if x % 6 == 0]


# 101. Функция для нахождения уникальных элементов в списке, используя множество
def unique_elements(lst):
    unique = set()
    for item in lst:
        if item not in unique:
            unique.add(item)
        else:
            print(f"Duplicate found: {item}")
    return list(unique)

# 102. Функция для подсчёта количества вхождений каждого элемента в список с использованием словаря
def count_occurrences(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    if not count_dict:
        print("No elements found.")
    return count_dict

# 103. Функция для нахождения пересечения двух списков с использованием множеств
def intersection_of_lists(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    intersection = set1 & set2
    if not intersection:
        print("No common elements found.")
    return list(intersection)

# 104. Функция для нахождения всех чисел, которые делятся на любое число из второго списка
def divisible_by_any(lst, divisors):
    divisible = []
    for num in lst:
        for divisor in divisors:
            if num % divisor == 0:
                divisible.append(num)
                break
    if not divisible:
        print("No numbers divisible by any divisor found.")
    return divisible

# 105. Функция для проверки, является ли строка анаграммой другой строки
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        print("Strings are not of equal length.")
        return False
    char_count = {}
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s2:
        if char not in char_count or char_count[char] == 0:
            print(f"'{char}' is not in the first string or appears too many times.")
            return False
        char_count[char] -= 1
    return True

# 106. Функция для нахождения пересечения двух множеств
def intersection_of_sets(set1, set2):
    intersection = set1.intersection(set2)
    if not intersection:
        print("The sets have no common elements.")
    return intersection

# 107. Функция для удаления дубликатов из списка кортежей по первому элементу
def remove_duplicate_tuples(lst):
    seen = set()
    result = []
    for item in lst:
        if item[0] not in seen:
            seen.add(item[0])
            result.append(item)
        else:
            print(f"Duplicate tuple found: {item}")
    return result

# 108. Функция для подсчёта элементов в строках списка, возвращая словарь с длинами строк
def count_string_lengths(lst):
    length_dict = {}
    for s in lst:
        length_dict[s] = len(s)
    return length_dict

# 109. Функция для нахождения числа, которое встречается больше всех раз в словаре (ключи - элементы, значения - количество)
def most_frequent_in_dict(d):
    if not d:
        print("Dictionary is empty.")
        return None
    max_key = max(d, key=d.get)
    return max_key, d[max_key]

# 110. Функция для объединения двух словарей (если есть одинаковые ключи, их значения суммируются)
def merge_dicts(d1, d2):
    merged = d1.copy()
    for key, value in d2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

# 111. Функция для подсчёта чётных и нечётных чисел в списке с использованием словаря
def count_even_odd(lst):
    count = {"even": 0, "odd": 0}
    for num in lst:
        if num % 2 == 0:
            count["even"] += 1
        else:
            count["odd"] += 1
    return count

# 112. Функция для нахождения минимального ключа в словаре с числовыми значениями
def min_key_in_dict(d):
    if not d:
        print("Dictionary is empty.")
        return None
    return min(d, key=d.get)

# 113. Функция для создания словаря из списка, где элементы списка становятся значениями, а их индексы — ключами
def list_to_dict(lst):
    result = {}
    for index, value in enumerate(lst):
        result[index] = value
    return result

# 114. Функция для проверки, является ли строка числом, и если да — вернуть её квадрат
def check_and_square(s):
    try:
        num = float(s)
        return num ** 2
    except ValueError:
        print(f"'{s}' is not a valid number.")
        return None


# 115. Функция для нахождения всех чисел в строке, игнорируя символы
def extract_numbers_from_string(s):
    result = []
    current_num = ''
    for char in s:
        if char.isdigit():
            current_num += char
        else:
            if current_num:
                result.append(int(current_num))
                current_num = ''
    if current_num:
        result.append(int(current_num))
    return result

# 116. Функция для объединения двух кортежей, убирая повторяющиеся элементы
def merge_tuples(t1, t2):
    return tuple(set(t1 + t2))

# 117. Функция для нахождения всех уникальных чисел в списке (с использованием множества)
def unique_numbers(lst):
    unique = set()
    for num in lst:
        unique.add(num)
    return list(unique)

# 118. Функция для создания словаря, где ключами будут уникальные элементы списка, а значениями — количество их повторений
def create_frequency_dict(lst):
    frequency_dict = {}
    for item in lst:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

# 119. Функция для нахождения элементов, которые присутствуют в одном списке, но отсутствуют в другом
def difference_of_lists(lst1, lst2):
    result = []
    for item in lst1:
        if item not in lst2:
            result.append(item)
    for item in lst2:
        if item not in lst1:
            result.append(item)
    return result

# 120. Функция для нахождения всех элементов списка, которые встречаются в другой коллекции
def find_in_collection(lst, collection):
    result = []
    for item in lst:
        if item in collection:
            result.append(item)
    if not result:
        print("No elements found in the collection.")
    return result



# 121. Функция для нахождения суммы всех чисел в списке, которые встречаются более одного раза
def sum_of_duplicates(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    total = 0
    for key, value in count_dict.items():
        if value > 1:
            total += key
    if total == 0:
        print("No duplicates found.")
    return total

# 122. Функция для нахождения элементов, которые присутствуют в одном списке и не встречаются в другом
def unique_in_first(lst1, lst2):
    unique_elements = []
    for item in lst1:
        if item not in lst2:
            unique_elements.append(item)
    if not unique_elements:
        print("No unique elements found in the first list.")
    return unique_elements

# 123. Функция для нахождения минимального общего кратного двух чисел
def lcm(a, b):
    if a == 0 or b == 0:
        print("LCM is undefined for 0.")
        return None
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)

# 124. Функция для получения всех элементов из словаря, чьи значения больше заданного порога
def filter_dict_by_value(d, threshold):
    result = {}
    for key, value in d.items():
        if value > threshold:
            result[key] = value
    if not result:
        print("No elements above the threshold.")
    return result

# 125. Функция для переворота словаря, меняя местами ключи и значения
def reverse_dict(d):
    reversed_dict = {}
    for key, value in d.items():
        if value in reversed_dict:
            print(f"Duplicate value {value} found, skipping.")
        else:
            reversed_dict[value] = key
    return reversed_dict

# 126. Функция для нахождения всех чисел, которые являются кратными числам из другого списка
def multiples_from_list(lst1, lst2):
    multiples = []
    for num in lst1:
        for divisor in lst2:
            if num % divisor == 0:
                multiples.append(num)
                break
    if not multiples:
        print("No numbers are divisible by elements from the second list.")
    return multiples

# 127. Функция для подсчёта частоты вхождения каждого символа в строке, игнорируя регистр
def case_insensitive_char_frequency(s):
    freq = {}
    for char in s.lower():
        if char.isalpha():
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    if not freq:
        print("No alphabetical characters found.")
    return freq

# 128. Функция для нахождения суммы всех чисел в строке, игнорируя символы
def sum_numbers_in_string(s):
    total = 0
    current_num = ''
    for char in s:
        if char.isdigit():
            current_num += char
        elif current_num:
            total += int(current_num)
            current_num = ''
    if current_num:
        total += int(current_num)
    return total

# 129. Функция для подсчёта всех различных элементов в списке, с учётом их частоты
def count_unique_with_frequency(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

# 130. Функция для подсчёта, сколько раз каждый символ в строке встречается подряд
def count_consecutive_chars(s):
    if not s:
        print("Empty string provided.")
        return {}
    count = {}
    current_char = s[0]
    current_count = 1
    for char in s[1:]:
        if char == current_char:
            current_count += 1
        else:
            if current_char in count:
                count[current_char] += current_count
            else:
                count[current_char] = current_count
            current_char = char
            current_count = 1
    if current_char in count:
        count[current_char] += current_count
    else:
        count[current_char] = current_count
    return count

# 131. Функция для нахождения всех чисел в списке, которые делятся на наибольший общий делитель всех чисел в списке
def divisible_by_gcd(lst):
    from math import gcd
    from functools import reduce
    if len(lst) < 2:
        print("Need at least two numbers.")
        return []
    overall_gcd = reduce(gcd, lst)
    divisible = [num for num in lst if num % overall_gcd == 0]
    return divisible

# 132. Функция для нахождения всех элементов в множестве, которые присутствуют в словаре в качестве ключей
def find_keys_in_set(s, d):
    result = []
    for item in s:
        if item in d:
            result.append(item)
    if not result:
        print("No elements from the set found in the dictionary keys.")
    return result

# 133. Функция для нахождения всех чисел в списке, которые являются простыми
def find_prime_numbers(lst):
    primes = []
    for num in lst:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# 134. Функция для разделения строки на два списка: один с цифрами, второй с остальными символами
def split_digits_and_others(s):
    digits = []
    others = []
    for char in s:
        if char.isdigit():
            digits.append(char)
        else:
            others.append(char)
    return digits, others

# 135. Функция для получения кортежа с минимальным и максимальным элементами списка
def min_max_tuple(lst):
    if not lst:
        print("List is empty.")
        return None
    return (min(lst), max(lst))

# 136. Функция для поиска элементов, которые присутствуют в двух словарях, но имеют разные значения
def find_common_keys_with_different_values(d1, d2):
    common_keys = set(d1.keys()) & set(d2.keys())
    result = []
    for key in common_keys:
        if d1[key] != d2[key]:
            result.append(key)
    if not result:
        print("No keys with different values found.")
    return result

# 137. Функция для преобразования строки в список чисел, разделённых пробелами, если в строке присутствуют только числа
def string_to_numbers(s):
    try:
        return [int(x) for x in s.split()]
    except ValueError:
        print("String contains non-numeric values.")
        return []

# 138. Функция для нахождения чисел в строке, которые могут быть переведены в степень двойки
def find_powers_of_two_in_string(s):
    numbers = []
    for word in s.split():
        try:
            num = int(word)
            if (num & (num - 1)) == 0 and num > 0:  # Check if number is power of two
                numbers.append(num)
        except ValueError:
            continue
    return numbers

# 139. Функция для нахождения слов, которые являются палиндромами
def find_palindromes(lst):
    palindromes = []
    for word in lst:
        if word == word[::-1]:
            palindromes.append(word)
    return palindromes

# 140. Функция для объединения двух списков с проверкой на дубликаты
def merge_lists_no_duplicates(lst1, lst2):
    result = lst1.copy()
    for item in lst2:
        if item not in result:
            result.append(item)
        else:
            print(f"Duplicate item found: {item}")
    return result



# 141. Функция для нахождения всех чисел, которые делятся на 2, но не делятся на 3
def divisible_by_2_not_3(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 != 0:
            result.append(num)
    if not result:
        print("No numbers divisible by 2 but not by 3 found.")
    return result

# 142. Функция для нахождения всех чисел в строке, которые являются чётными
def find_even_numbers_in_string(s):
    result = []
    current_num = ''
    for char in s:
        if char.isdigit():
            current_num += char
        elif current_num:
            num = int(current_num)
            if num % 2 == 0:
                result.append(num)
            current_num = ''
    if current_num:
        num = int(current_num)
        if num % 2 == 0:
            result.append(num)
    return result

# 143. Функция для нахождения всех чисел, которые не являются простыми
def find_non_prime_numbers(lst):
    non_primes = []
    for num in lst:
        if num < 2:
            non_primes.append(num)
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    non_primes.append(num)
                    break
    return non_primes

# 144. Функция для нахождения всех уникальных символов в строке, игнорируя пробелы
def unique_chars_ignore_spaces(s):
    unique_chars = {}
    for char in s:
        if char != ' ':
            if char not in unique_chars:
                unique_chars[char] = 1
            else:
                unique_chars[char] += 1
    return list(unique_chars.keys())

# 145. Функция для подсчёта слов в строке, игнорируя знаки препинания
def count_words_ignore_punctuation(s):
    word_count = 0
    current_word = ''
    for char in s:
        if char.isalnum():
            current_word += char
        elif current_word:
            word_count += 1
            current_word = ''
    if current_word:
        word_count += 1
    return word_count

# 146. Функция для нахождения всех чисел, которые являются квадратами целых чисел
def find_squares(lst):
    squares = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num:
            squares.append(num)
    return squares

# 147. Функция для подсчёта количества повторений каждого слова в строке
def word_frequency_in_string(s):
    word_count = {}
    current_word = ''
    for char in s:
        if char.isalnum():
            current_word += char
        elif current_word:
            if current_word in word_count:
                word_count[current_word] += 1
            else:
                word_count[current_word] = 1
            current_word = ''
    if current_word:
        if current_word in word_count:
            word_count[current_word] += 1
        else:
            word_count[current_word] = 1
    return word_count

# 148. Функция для поиска чисел, которые могут быть записаны как сумма двух квадратов
def find_sum_of_two_squares(lst):
    def is_sum_of_two_squares(n):
        for i in range(1, int(n ** 0.5) + 1):
            if (n - i ** 2) ** 0.5 == int((n - i ** 2) ** 0.5):
                return True
        return False

    result = []
    for num in lst:
        if is_sum_of_two_squares(num):
            result.append(num)
    return result

# 149. Функция для получения всех элементов списка, которые не содержат в себе цифры
def find_non_numeric_elements(lst):
    result = []
    for item in lst:
        if not any(char.isdigit() for char in item):
            result.append(item)
    return result

# 150. Функция для нахождения всех чисел, которые являются нечётными и делятся на 5
def find_odd_and_divisible_by_5(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 5 == 0:
            result.append(num)
    if not result:
        print("No odd numbers divisible by 5 found.")
    return result

# 151. Функция для подсчёта всех элементов в словаре, значения которых больше определённого порога
def count_elements_above_threshold(d, threshold):
    count = 0
    for key, value in d.items():
        if value > threshold:
            count += 1
    return count

# 152. Функция для поиска чисел, которые являются степенями числа 3
def find_powers_of_three(lst):
    powers_of_three = []
    for num in lst:
        while num % 3 == 0 and num > 0:
            num //= 3
        if num == 1:
            powers_of_three.append(num)
    return powers_of_three

# 153. Функция для получения всех чисел в строке, которые больше среднего значения
def find_numbers_greater_than_mean(s):
    nums = [int(x) for x in s.split() if x.isdigit()]
    mean = sum(nums) / len(nums) if nums else 0
    result = []
    for num in nums:
        if num > mean:
            result.append(num)
    return result

# 154. Функция для нахождения всех чисел, которые являются нечётными и не являются простыми
def find_odd_and_not_prime(lst):
    non_prime_odd = []
    for num in lst:
        if num % 2 != 0 and not is_prime(num):
            non_prime_odd.append(num)
    return non_prime_odd

# 155. Функция для нахождения всех чисел в списке, которые являются делителями другого числа в этом же списке
def find_divisors_in_list(lst):
    divisors = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] % lst[j] == 0:
                divisors.append(lst[i])
                break
    return divisors

# 156. Функция для нахождения всех чисел, которые не являются кратными чисел из другого списка
def find_non_multiples(lst1, lst2):
    non_multiples = []
    for num in lst1:
        if all(num % divisor != 0 for divisor in lst2):
            non_multiples.append(num)
    return non_multiples

# 157. Функция для нахождения всех элементов списка, которые присутствуют в обоих списках
def find_common_elements(lst1, lst2):
    common_elements = []
    for item in lst1:
        if item in lst2:
            common_elements.append(item)
    if not common_elements:
        print("No common elements found.")
    return common_elements

# 158. Функция для нахождения всех чисел, которые могут быть записаны как произведение двух простых чисел
def find_product_of_two_primes(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num):
            if num % i == 0 and is_prime(i) and is_prime(num // i):
                result.append(num)
                break
    return result

# 159. Функция для нахождения числа, которое является квадратом какого-то целого числа, но не является четным
def find_odd_square(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and num % 2 != 0:
            result.append(num)
    return result

# 160. Функция для нахождения всех элементов, которые содержат хотя бы одну гласную
def find_elements_with_vowels(lst):
    vowels = 'aeiouAEIOU'
    result = []
    for item in lst:
        if any(char in vowels for char in item):
            result.append(item)
    return result



# 161. Функция для нахождения всех чисел в списке, которые не делятся на 2 и на 3
def find_not_divisible_by_2_and_3(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 3 != 0:
            result.append(num)
    if not result:
        print("No numbers found that are not divisible by 2 or 3.")
        return []
    return result

# 162. Функция для подсчёта всех уникальных букв в строке
def count_unique_chars_in_string(s):
    char_count = {}
    for char in s:
        if char.isalpha():
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    if not char_count:
        print("No alphabetical characters found.")
        return {}
    return char_count

# 163. Функция для поиска чисел, которые могут быть записаны как произведение двух чётных чисел
def find_product_of_two_even_numbers(lst):
    result = []
    for num in lst:
        for i in range(2, num // 2 + 1, 2):
            if num % i == 0 and (num // i) % 2 == 0:
                result.append(num)
                break
    if not result:
        print("No numbers found that are the product of two even numbers.")
        return []
    return result

# 164. Функция для поиска всех чисел, которые являются квадратами нечётных чисел
def find_squares_of_odd_numbers(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0:
            result.append(num)
    if not result:
        print("No odd square numbers found.")
    return result

# 165. Функция для нахождения чисел, которые делятся на 5, но не делятся на 10
def find_multiples_of_5_not_10(lst):
    result = []
    for num in lst:
        if num % 5 == 0 and num % 10 != 0:
            result.append(num)
    if not result:
        print("No multiples of 5 that are not divisible by 10.")
    return result

# 166. Функция для нахождения всех чисел, которые являются двузначными и не делятся на 2
def find_double_digits_not_divisible_by_2(lst):
    result = []
    for num in lst:
        if 10 <= num <= 99 and num % 2 != 0:
            result.append(num)
    if not result:
        print("No double-digit numbers found that are not divisible by 2.")
    return result

# 167. Функция для нахождения всех чисел, которые могут быть записаны как сумма двух простых чисел
def find_sum_of_two_primes(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if is_prime(i) and is_prime(num - i):
                result.append(num)
                break
    if not result:
        print("No numbers that are the sum of two primes.")
    return result

# 168. Функция для нахождения чисел, которые встречаются в обеих строках
def find_common_numbers_in_strings(s1, s2):
    nums1 = {int(x) for x in s1.split() if x.isdigit()}
    nums2 = {int(x) for x in s2.split() if x.isdigit()}
    common = nums1 & nums2
    if not common:
        print("No common numbers found between the two strings.")
        return set()
    return common

# 169. Функция для нахождения всех чисел, которые делятся на 7, но не на 11
def find_divisible_by_7_not_11(lst):
    result = []
    for num in lst:
        if num % 7 == 0 and num % 11 != 0:
            result.append(num)
    if not result:
        print("No numbers found divisible by 7 but not 11.")
    return result

# 170. Функция для подсчёта, сколько раз слово встречается в строке, игнорируя регистр
def count_word_in_string(s, word):
    s = s.lower()
    word = word.lower()
    count = s.split().count(word)
    if count == 0:
        print(f"The word '{word}' was not found.")
        return 0
    return count

# 171. Функция для нахождения чисел, которые могут быть записаны как разность двух квадратов
def find_difference_of_two_squares(lst):
    result = []
    for num in lst:
        for i in range(1, int(num ** 0.5) + 1):
            if (num + i ** 2) ** 0.5 == int((num + i ** 2) ** 0.5):
                result.append(num)
                break
    if not result:
        print("No numbers found that are the difference of two squares.")
    return result

# 172. Функция для нахождения чисел, которые являются простыми, но не являются кратными 3
def find_primes_not_multiples_of_3(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        if is_prime(num) and num % 3 != 0:
            result.append(num)
    if not result:
        print("No prime numbers found that are not divisible by 3.")
    return result

# 173. Функция для нахождения всех чисел, которые можно записать как произведение двух простых чисел
def find_product_of_two_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i):
                result.append(num)
                break
    if not result:
        print("No numbers found that are the product of two primes.")
    return result

# 174. Функция для нахождения чисел, которые являются чётными и делятся на 4
def find_even_numbers_divisible_by_4(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 4 == 0:
            result.append(num)
    if not result:
        print("No even numbers divisible by 4 found.")
    return result

# 175. Функция для нахождения всех чисел, которые не являются степенями двойки
def find_non_powers_of_two(lst):
    result = []
    for num in lst:
        if (num & (num - 1)) != 0:
            result.append(num)
    if not result:
        print("No numbers found that are not powers of two.")
    return result

# 176. Функция для подсчёта всех чисел в строке, которые больше среднего значения всех чисел в строке
def count_numbers_greater_than_average(s):
    nums = [int(x) for x in s.split() if x.isdigit()]
    if not nums:
        print("No numbers found in the string.")
        return 0
    average = sum(nums) / len(nums)
    count = sum(1 for num in nums if num > average)
    return count

# 177. Функция для нахождения всех чисел, которые могут быть записаны как сумма двух чисел, каждое из которых делится на 3
def find_sum_of_two_divisible_by_3(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1):
            if i % 3 == 0 and (num - i) % 3 == 0:
                result.append(num)
                break
    if not result:
        print("No numbers found that are the sum of two numbers divisible by 3.")
    return result

# 178. Функция для нахождения всех чисел, которые делятся на 4 или на 5, но не на 20
def find_multiples_of_4_or_5_not_20(lst):
    result = []
    for num in lst:
        if (num % 4 == 0 or num % 5 == 0) and num % 20 != 0:
            result.append(num)
    if not result:
        print("No numbers found that are divisible by 4 or 5, but not by 20.")
    return result

# 179. Функция для поиска всех чисел, которые являются точными делителями 100
def find_exact_divisors_of_100(lst):
    result = []
    for num in lst:
        if 100 % num == 0:
            result.append(num)
    if not result:
        print("No numbers found that are exact divisors of 100.")
    return result

# 180. Функция для поиска чисел, которые являются нечётными и не являются делителями 5
def find_odd_not_divisible_by_5(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 5 != 0:
            result.append(num)
    if not result:
        print("No odd numbers found that are not divisible by 5.")
    return result


# 181. Функция для нахождения всех чисел, которые являются кратными либо 2, либо 3, но не обоим
def find_multiples_of_2_or_3(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 != 0:
            result.append(num)
        elif num % 3 == 0 and num % 2 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are multiples of 2 or 3, but not both."
    return result


# 182. Функция для нахождения всех чисел, которые делятся на 3 и на 5, но не на 7
def find_multiples_of_3_and_5_not_7(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 5 == 0 and num % 7 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are divisible by 3 and 5 but not 7."
    return result


# 183. Функция для нахождения всех чисел, которые либо нечётные, либо делятся на 4
def find_odd_or_divisible_by_4(lst):
    result = []
    for num in lst:
        if num % 2 != 0 or num % 4 == 0:
            result.append(num)
    if not result:
        return "No odd numbers or numbers divisible by 4 found."
    return result


# 184. Функция для нахождения чисел, которые являются квадратами целых чисел, но не чётными
def find_even_squares(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and num % 2 == 0:
            result.append(num)
    if not result:
        return "No even square numbers found."
    return result


# 185. Функция для нахождения всех чисел, которые являются суммой двух простых чисел
def find_sum_of_two_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if is_prime(i) and is_prime(num - i):
                result.append(num)
                break
    if not result:
        return "No numbers found that are the sum of two primes."
    return result


# 186. Функция для нахождения всех чисел, которые являются нечётными и не являются квадратами целых чисел
def find_odd_not_square(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and int(num ** 0.5) ** 2 != num:
            result.append(num)
    if not result:
        return "No odd numbers found that are not perfect squares."
    return result


# 187. Функция для нахождения всех чисел, которые являются кратными 3 или 5, но не кратными обоим
def find_multiples_of_3_or_5_not_both(lst):
    result = []
    for num in lst:
        if (num % 3 == 0 or num % 5 == 0) and not (num % 3 == 0 and num % 5 == 0):
            result.append(num)
    if not result:
        return "No numbers found that are multiples of 3 or 5 but not both."
    return result


# 188. Функция для нахождения чисел, которые являются чётными и делятся на 7, но не на 14
def find_even_and_divisible_by_7_not_14(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 7 == 0 and num % 14 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are even and divisible by 7 but not 14."
    return result


# 189. Функция для подсчёта всех чисел в строке, которые больше среднего значения
def count_numbers_greater_than_mean(s):
    nums = [int(x) for x in s.split() if x.isdigit()]
    if not nums:
        return "No numbers found in the string."

    mean = sum(nums) / len(nums)
    count = len([num for num in nums if num > mean])
    if count == 0:
        return "No numbers greater than the mean."
    return count


# 190. Функция для нахождения всех чисел, которые являются степенями 2
def find_powers_of_2(lst):
    result = []
    for num in lst:
        if (num & (num - 1)) == 0:
            result.append(num)
    if not result:
        return "No powers of 2 found."
    return result


# 191. Функция для нахождения всех чисел, которые являются четными и кратными 8
def find_even_and_divisible_by_8(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 8 == 0:
            result.append(num)
    if not result:
        return "No even numbers divisible by 8 found."
    return result


# 192. Функция для нахождения всех чисел, которые являются произведением двух простых чисел
def find_product_of_two_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i):
                result.append(num)
                break
    if not result:
        return "No numbers found that are the product of two primes."
    return result


# 193. Функция для нахождения всех чисел, которые являются квадратами нечётных чисел
def find_squares_of_odd_numbers(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0:
            result.append(num)
    if not result:
        return "No squares of odd numbers found."
    return result


# 194. Функция для нахождения чисел, которые являются нечётными и делятся на 3
def find_odd_and_divisible_by_3(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 3 == 0:
            result.append(num)
    if not result:
        return "No odd numbers divisible by 3 found."
    return result


# 195. Функция для нахождения всех чисел, которые не являются чётными или кратными 7
def find_non_even_or_not_multiples_of_7(lst):
    result = []
    for num in lst:
        if num % 2 != 0 or num % 7 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are not even or not divisible by 7."
    return result


# 196. Функция для нахождения всех чисел, которые являются квадратами чётных чисел
def find_squares_of_even_numbers(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 == 0:
            result.append(num)
    if not result:
        return "No squares of even numbers found."
    return result


# 197. Функция для нахождения чисел, которые могут быть записаны как разность двух простых чисел
def find_difference_of_two_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if is_prime(i) and is_prime(num - i):
                result.append(num)
                break
    if not result:
        return "No numbers found that are the difference of two primes."
    return result


# 198. Функция для нахождения чисел, которые не делятся на 2, но делятся на 5
def find_not_divisible_by_2_but_divisible_by_5(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 5 == 0:
            result.append(num)
    if not result:
        return "No numbers found that are not divisible by 2 but divisible by 5."
    return result


# 199. Функция для нахождения всех чисел, которые являются кратными 3, 5 или 7
def find_multiples_of_3_5_or_7(lst):
    result = []
    for num in lst:
        if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
            result.append(num)
    if not result:
        return "No numbers found that are multiples of 3, 5, or 7."
    return result


# 200. Функция для нахождения всех чисел, которые являются чётными и делятся на 3, но не на 6
def find_even_and_divisible_by_3_not_6(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 == 0 and num % 6 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are even and divisible by 3 but not by 6."
    return result



# 201. Функция для нахождения всех чисел, которые являются произведением двух нечётных чисел
def find_product_of_two_odd_numbers(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1, 2):
            if num % i == 0 and (num // i) % 2 != 0:
                result.append(num)
                break
    if not result:
        return "No numbers found that are the product of two odd numbers."
    return result

# 202. Функция для нахождения всех чисел, которые являются чётными, но не являются делителями 4
def find_even_not_divisible_by_4(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 4 != 0:
            result.append(num)
    if not result:
        return "No even numbers found that are not divisible by 4."
    return result

# 203. Функция для нахождения чисел, которые являются кратными 3 или 5, но не кратными 15
def find_multiples_of_3_or_5_not_15(lst):
    result = []
    for num in lst:
        if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are multiples of 3 or 5 but not 15."
    return result

# 204. Функция для нахождения всех чисел, которые являются разностью двух квадратов
def find_difference_of_two_squares(lst):
    result = []
    for num in lst:
        for i in range(1, int(num ** 0.5) + 1):
            if (num + i ** 2) ** 0.5 == int((num + i ** 2) ** 0.5):
                result.append(num)
                break
    if not result:
        return "No numbers found that are the difference of two squares."
    return result

# 205. Функция для нахождения чисел, которые могут быть записаны как произведение двух простых чисел
def find_product_of_two_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i):
                result.append(num)
                break
    if not result:
        return "No numbers found that are the product of two primes."
    return result

# 206. Функция для нахождения чисел, которые являются квадратами нечётных чисел
def find_squares_of_odd_numbers(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0:
            result.append(num)
    if not result:
        return "No squares of odd numbers found."
    return result

# 207. Функция для нахождения всех чисел, которые могут быть записаны как сумма двух чисел, каждое из которых делится на 3
def find_sum_of_two_divisible_by_3(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1):
            if i % 3 == 0 and (num - i) % 3 == 0:
                result.append(num)
                break
    if not result:
        return "No numbers found that are the sum of two numbers divisible by 3."
    return result

# 208. Функция для нахождения всех чисел, которые не являются чётными, но являются делителями 9
def find_not_even_but_divisible_by_9(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 9 == 0:
            result.append(num)
    if not result:
        return "No numbers found that are not even but divisible by 9."
    return result

# 209. Функция для нахождения чисел, которые являются чётными и не делятся на 3
def find_even_not_divisible_by_3(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 != 0:
            result.append(num)
    if not result:
        return "No even numbers found that are not divisible by 3."
    return result

# 210. Функция для нахождения всех чисел, которые являются нечетными и делятся на 4
def find_odd_and_divisible_by_4(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 4 == 0:
            result.append(num)
    if not result:
        return "No odd numbers found that are divisible by 4."
    return result

# 211. Функция для нахождения всех чисел, которые делятся на 2 или на 3, но не на 6
def find_divisible_by_2_or_3_not_6(lst):
    result = []
    for num in lst:
        if (num % 2 == 0 or num % 3 == 0) and num % 6 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are divisible by 2 or 3 but not 6."
    return result

# 212. Функция для нахождения чисел, которые являются делителями 12, но не являются чётными
def find_divisors_of_12_not_even(lst):
    result = []
    for num in lst:
        if 12 % num == 0 and num % 2 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are divisors of 12 but not even."
    return result

# 213. Функция для нахождения чисел, которые могут быть записаны как разность двух простых чисел
def find_difference_of_two_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if is_prime(i) and is_prime(num - i):
                result.append(num)
                break
    if not result:
        return "No numbers found that are the difference of two primes."
    return result

# 214. Функция для нахождения всех чисел, которые являются делителями 6, но не 12
def find_divisors_of_6_not_12(lst):
    result = []
    for num in lst:
        if 6 % num == 0 and num != 12:
            result.append(num)
    if not result:
        return "No numbers found that are divisors of 6 but not 12."
    return result

# 215. Функция для нахождения всех чисел, которые являются квадратами чётных чисел
def find_squares_of_even_numbers(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 == 0:
            result.append(num)
    if not result:
        return "No squares of even numbers found."
    return result

# 216. Функция для нахождения чисел, которые не являются степенями 2, но являются чётными
def find_even_not_powers_of_2(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and (num & (num - 1)) != 0:
            result.append(num)
    if not result:
        return "No even numbers found that are not powers of 2."
    return result

# 217. Функция для нахождения всех чисел, которые не являются чётными и не являются делителями 9
def find_not_even_and_not_divisible_by_9(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are neither even nor divisible by 9."
    return result

# 218. Функция для нахождения всех чисел, которые могут быть записаны как произведение двух нечётных чисел
def find_product_of_two_odd_numbers(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1, 2):
            if num % i == 0 and (num // i) % 2 != 0:
                result.append(num)
                break
    if not result:
        return "No numbers found that are the product of two odd numbers."
    return result

# 219. Функция для нахождения чисел, которые делятся на 3 и 5, но не на 7
def find_multiples_of_3_and_5_not_7(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 5 == 0 and num % 7 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are divisible by 3 and 5 but not 7."
    return result


# 220. Функция для нахождения всех чисел, которые являются делителями 30, но не делятся на 5
def find_divisors_of_30_not_5(lst):
    result = []
    for num in lst:
        if 30 % num == 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 221. Функция для нахождения чисел, которые являются квадратами чётных чисел, но не делятся на 4
def find_squares_of_even_not_divisible_by_4(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 == 0 and num % 4 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 222. Функция для нахождения всех чисел, которые являются произведением двух нечётных чисел
def find_product_of_two_odd_numbers(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1, 2):
            if num % i == 0 and (num // i) % 2 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result

# 223. Функция для нахождения чисел, которые являются произведением двух простых чисел
def find_product_of_two_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i):
                result.append(num)
                break
    if not result:
        return None
    return result

# 224. Функция для нахождения всех чисел, которые являются нечётными и не являются степенями 2
def find_odd_not_power_of_2(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and (num & (num - 1)) != 0:
            result.append(num)
    if not result:
        return None
    return result

# 225. Функция для нахождения чисел, которые являются чётными и делятся на 4, но не на 8
def find_even_divisible_by_4_not_8(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 4 == 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 226. Функция для нахождения чисел, которые делятся на 6, но не делятся на 9
def find_divisible_by_6_not_9(lst):
    result = []
    for num in lst:
        if num % 6 == 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 227. Функция для нахождения всех чисел, которые являются делителями 24, но не делятся на 8
def find_divisors_of_24_not_8(lst):
    result = []
    for num in lst:
        if 24 % num == 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 228. Функция для нахождения чисел, которые являются чётными и делятся на 5, но не на 10
def find_even_and_divisible_by_5_not_10(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 5 == 0 and num % 10 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 229. Функция для нахождения чисел, которые являются квадратами нечётных чисел
def find_squares_of_odd_numbers(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 230. Функция для нахождения чисел, которые являются степенями 2, но не чётными
def find_powers_of_2_not_even(lst):
    result = []
    for num in lst:
        if (num & (num - 1)) == 0 and num % 2 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 231. Функция для нахождения чисел, которые не являются кратными 3, но делятся на 5
def find_not_multiples_of_3_but_divisible_by_5(lst):
    result = []
    for num in lst:
        if num % 3 != 0 and num % 5 == 0:
            result.append(num)
    if not result:
        return None
    return result

# 232. Функция для нахождения чисел, которые являются чётными и не делятся на 5
def find_even_not_divisible_by_5(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 233. Функция для нахождения чисел, которые являются делителями 15, но не делятся на 3
def find_divisors_of_15_not_3(lst):
    result = []
    for num in lst:
        if 15 % num == 0 and num % 3 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 234. Функция для нахождения чисел, которые являются суммой двух простых чисел
def find_sum_of_two_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if is_prime(i) and is_prime(num - i):
                result.append(num)
                break
    if not result:
        return None
    return result

# 235. Функция для нахождения чисел, которые являются степенями 2, но не кратными 4
def find_powers_of_2_not_multiples_of_4(lst):
    result = []
    for num in lst:
        if (num & (num - 1)) == 0 and num % 4 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 236. Функция для нахождения чисел, которые являются нечётными, но не являются квадратами
def find_odd_not_square(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and int(num ** 0.5) ** 2 != num:
            result.append(num)
    if not result:
        return None
    return result

# 237. Функция для нахождения чисел, которые являются квадратами чётных чисел, но не делятся на 8
def find_squares_of_even_not_divisible_by_8(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 == 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 238. Функция для нахождения чисел, которые являются делителями 6, но не 2
def find_divisors_of_6_not_2(lst):
    result = []
    for num in lst:
        if 6 % num == 0 and num != 2:
            result.append(num)
    if not result:
        return None
    return result


# 239. Функция для нахождения всех чисел, которые являются делителями 48, но не делятся на 16
def find_divisors_of_48_not_16(lst):
    result = []
    for num in lst:
        if 48 % num == 0 and num % 16 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 240. Функция для нахождения чисел, которые являются чётными и делятся на 3, но не на 6
def find_even_and_divisible_by_3_not_6(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 == 0 and num % 6 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 241. Функция для нахождения чисел, которые являются квадратами нечётных чисел, но не делятся на 9
def find_squares_of_odd_not_divisible_by_9(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 242. Функция для нахождения всех чисел, которые являются разностью двух простых чисел
def find_difference_of_two_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if is_prime(i) and is_prime(num - i):
                result.append(num)
                break
    if not result:
        return None
    return result

# 243. Функция для нахождения чисел, которые являются суммой двух чётных чисел
def find_sum_of_two_even_numbers(lst):
    result = []
    for num in lst:
        for i in range(2, num // 2 + 1, 2):
            if (num - i) % 2 == 0:
                result.append(num)
                break
    if not result:
        return None
    return result

# 244. Функция для нахождения всех чисел, которые являются делителями 20, но не являются чётными
def find_divisors_of_20_not_even(lst):
    result = []
    for num in lst:
        if 20 % num == 0 and num % 2 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 245. Функция для нахождения чисел, которые делятся на 2, но не делятся на 4 или 8
def find_divisible_by_2_not_4_or_8(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 4 != 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 246. Функция для нахождения всех чисел, которые являются квадратами нечётных чисел, но не на 7
def find_squares_of_odd_not_7(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0 and num % 7 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 247. Функция для нахождения всех чисел, которые делятся на 5, но не являются делителями 10
def find_divisible_by_5_not_divisible_by_10(lst):
    result = []
    for num in lst:
        if num % 5 == 0 and num % 10 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 248. Функция для нахождения всех чисел, которые являются произведением двух нечётных чисел, но не делятся на 3
def find_product_of_two_odd_numbers_not_divisible_by_3(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1, 2):
            if num % i == 0 and (num // i) % 2 != 0 and num % 3 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result

# 249. Функция для нахождения чисел, которые являются чётными и не являются делителями 3
def find_even_not_divisible_by_3(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 250. Функция для нахождения чисел, которые являются разностью двух чётных чисел
def find_difference_of_two_even_numbers(lst):
    result = []
    for num in lst:
        for i in range(2, num // 2 + 1, 2):
            if (num - i) % 2 == 0:
                result.append(num)
                break
    if not result:
        return None
    return result

# 251. Функция для нахождения чисел, которые являются суммой двух простых чисел
def find_sum_of_two_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if is_prime(i) and is_prime(num - i):
                result.append(num)
                break
    if not result:
        return None
    return result

# 252. Функция для нахождения чисел, которые делятся на 2 и на 3, но не на 6
def find_multiples_of_2_and_3_not_6(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 == 0 and num % 6 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 253. Функция для нахождения чисел, которые являются чётными и делятся на 4, но не на 8
def find_even_and_divisible_by_4_not_8(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 4 == 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 254. Функция для нахождения чисел, которые являются квадратами нечётных чисел, но не делятся на 5
def find_squares_of_odd_not_divisible_by_5(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 255. Функция для нахождения всех чисел, которые являются произведением двух простых чисел, но не делятся на 7
def find_product_of_two_primes_not_divisible_by_7(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i) and num % 7 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result

# 256. Функция для нахождения всех чисел, которые являются делителями 18, но не делятся на 9
def find_divisors_of_18_not_9(lst):
    result = []
    for num in lst:
        if 18 % num == 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 257. Функция для нахождения чисел, которые являются кратными 3 и 5, но не кратными 15
def find_multiples_of_3_and_5_not_15(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 5 == 0 and num % 15 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 258. Функция для нахождения всех чисел, которые являются произведением двух простых чисел, но не делятся на 11
def find_product_of_two_primes_not_divisible_by_11(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i) and num % 11 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result

# 259. Функция для нахождения чисел, которые являются квадратами чётных чисел, но не делятся на 4
def find_squares_of_even_not_divisible_by_4(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 == 0 and num % 4 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 260. Функция для нахождения чисел, которые являются делителями 36, но не делятся на 9
def find_divisors_of_36_not_9(lst):
    result = []
    for num in lst:
        if 36 % num == 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return None
    return result



# 261. Функция для нахождения чисел, которые делятся на 5 и на 6, но не на 10
def find_multiples_of_5_and_6_not_10(lst):
    result = []
    for num in lst:
        if num % 5 == 0 and num % 6 == 0 and num % 10 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 262. Функция для нахождения чисел, которые являются разностью двух чётных чисел, но не делятся на 4
def find_difference_of_two_even_not_divisible_by_4(lst):
    result = []
    for num in lst:
        for i in range(2, num // 2 + 1, 2):
            if (num - i) % 2 == 0 and num % 4 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result

# 263. Функция для нахождения всех чисел, которые делятся на 8, но не на 16
def find_divisible_by_8_not_16(lst):
    result = []
    for num in lst:
        if num % 8 == 0 and num % 16 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 264. Функция для нахождения чисел, которые являются произведением двух простых чисел, но не делятся на 7
def find_product_of_two_primes_not_7(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i) and num % 7 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result

# 265. Функция для нахождения всех чисел, которые являются разностью двух нечётных чисел
def find_difference_of_two_odd(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1, 2):
            if (num - i) % 2 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result

# 266. Функция для нахождения чисел, которые делятся на 7, но не делятся на 14
def find_divisible_by_7_not_14(lst):
    result = []
    for num in lst:
        if num % 7 == 0 and num % 14 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 267. Функция для нахождения чисел, которые являются нечётными и не являются квадратами чётных чисел
def find_odd_not_square_of_even(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and int(num ** 0.5) ** 2 != num:
            result.append(num)
    if not result:
        return None
    return result

# 268. Функция для нахождения чисел, которые являются суммой двух простых чисел, но не делятся на 4
def find_sum_of_two_primes_not_divisible_by_4(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if is_prime(i) and is_prime(num - i) and num % 4 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result

# 269. Функция для нахождения чисел, которые являются произведением двух нечётных чисел, но не делятся на 5
def find_product_of_two_odd_not_5(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1, 2):
            if num % i == 0 and (num // i) % 2 != 0 and num % 5 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result

# 270. Функция для нахождения чисел, которые являются делителями 36, но не делятся на 9
def find_divisors_of_36_not_9(lst):
    result = []
    for num in lst:
        if 36 % num == 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 271. Функция для нахождения чисел, которые являются нечётными и делятся на 5, но не на 10
def find_odd_and_divisible_by_5_not_10(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 5 == 0 and num % 10 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 272. Функция для нахождения всех чисел, которые делятся на 6, но не на 3
def find_divisible_by_6_not_3(lst):
    result = []
    for num in lst:
        if num % 6 == 0 and num % 3 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 273. Функция для нахождения чисел, которые являются квадратами чётных чисел, но не делятся на 4
def find_squares_of_even_not_divisible_by_4(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 == 0 and num % 4 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 274. Функция для нахождения чисел, которые являются разностью двух простых чисел
def find_difference_of_two_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if is_prime(i) and is_prime(num - i):
                result.append(num)
                break
    if not result:
        return None
    return result

# 275. Функция для нахождения всех чисел, которые являются делителями 30, но не делятся на 5
def find_divisors_of_30_not_5(lst):
    result = []
    for num in lst:
        if 30 % num == 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 276. Функция для нахождения чисел, которые являются произведением двух простых чисел, но не делятся на 6
def find_product_of_two_primes_not_6(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i) and num % 6 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result

# 277. Функция для нахождения чисел, которые являются чётными и делятся на 7, но не на 14
def find_even_and_divisible_by_7_not_14(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 7 == 0 and num % 14 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 278. Функция для нахождения чисел, которые являются квадратами нечётных чисел, но не делятся на 3
def find_squares_of_odd_not_divisible_by_3(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0 and num % 3 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 279. Функция для нахождения чисел, которые делятся на 10, но не на 5
def find_divisible_by_10_not_5(lst):
    result = []
    for num in lst:
        if num % 10 == 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 280. Функция для нахождения чисел, которые являются разностью двух нечётных чисел, но не делятся на 5
def find_difference_of_two_odd_not_5(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1, 2):
            if (num - i) % 2 != 0 and num % 5 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 281. Функция для нахождения чисел, которые являются чётными и делятся на 3, но не на 6
def find_even_and_divisible_by_3_not_6(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 == 0 and num % 6 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 282. Функция для нахождения всех чисел, которые являются квадратами нечётных чисел, но не делятся на 5
def find_squares_of_odd_not_divisible_by_5(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 283. Функция для нахождения чисел, которые являются произведением двух простых чисел, но не делятся на 3
def find_product_of_two_primes_not_divisible_by_3(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i) and num % 3 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result

# 284. Функция для нахождения чисел, которые делятся на 2, на 4, но не на 8
def find_divisible_by_2_and_4_not_8(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 4 == 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 285. Функция для нахождения всех чисел, которые являются делителями 40, но не являются чётными
def find_divisors_of_40_not_even(lst):
    result = []
    for num in lst:
        if 40 % num == 0 and num % 2 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 286. Функция для нахождения чисел, которые являются разностью двух чётных чисел, но не делятся на 5
def find_difference_of_two_even_not_5(lst):
    result = []
    for num in lst:
        for i in range(2, num // 2 + 1, 2):
            if (num - i) % 2 == 0 and num % 5 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result

# 287. Функция для нахождения чисел, которые являются произведением двух нечётных чисел, но не делятся на 7
def find_product_of_two_odd_not_divisible_by_7(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1, 2):
            if num % i == 0 and (num // i) % 2 != 0 and num % 7 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result

# 288. Функция для нахождения чисел, которые делятся на 4, но не на 2
def find_divisible_by_4_not_2(lst):
    result = []
    for num in lst:
        if num % 4 == 0 and num % 2 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 289. Функция для нахождения всех чисел, которые делятся на 9, но не на 3
def find_divisible_by_9_not_3(lst):
    result = []
    for num in lst:
        if num % 9 == 0 and num % 3 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 290. Функция для нахождения чисел, которые являются квадратами нечётных чисел, но не на 9
def find_squares_of_odd_not_9(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 291. Функция для нахождения чисел, которые являются разностью двух простых чисел
def find_difference_of_two_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if is_prime(i) and is_prime(num - i):
                result.append(num)
                break
    if not result:
        return None
    return result

# 292. Функция для нахождения чисел, которые являются произведением двух простых чисел, но не на 5
def find_product_of_two_primes_not_5(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        for i in range(2, num // 2 + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i) and num % 5 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result

# 293. Функция для нахождения чисел, которые делятся на 2 и на 5, но не на 10
def find_divisible_by_2_and_5_not_10(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 5 == 0 and num % 10 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 294. Функция для нахождения чисел, которые являются разностью двух чётных чисел, но не делятся на 6
def find_difference_of_two_even_not_divisible_by_6(lst):
    result = []
    for num in lst:
        for i in range(2, num // 2 + 1, 2):
            if (num - i) % 2 == 0 and num % 6 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result

# 295. Функция для нахождения чисел, которые являются произведением двух нечётных чисел, но не делятся на 4
def find_product_of_two_odd_not_divisible_by_4(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1, 2):
            if num % i == 0 and (num // i) % 2 != 0 and num % 4 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result

# 296. Функция для нахождения чисел, которые являются кратными 6, но не на 12
def find_multiples_of_6_not_12(lst):
    result = []
    for num in lst:
        if num % 6 == 0 and num % 12 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 297. Функция для нахождения чисел, которые являются чётными и не делятся на 5
def find_even_not_divisible_by_5(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 298. Функция для нахождения чисел, которые являются квадратами нечётных чисел, но не делятся на 3
def find_squares_of_odd_not_divisible_by_3(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0 and num % 3 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 299. Функция для нахождения всех чисел, которые являются делителями 50, но не являются простыми
def find_divisors_of_50_not_prime(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        if 50 % num == 0 and not is_prime(num):
            result.append(num)
    if not result:
        return None
    return result

# 300. Функция для нахождения чисел, которые делятся на 3 и на 4, но не на 6
def find_divisible_by_3_and_4_not_6(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 4 == 0 and num % 6 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 301. Функция для нахождения чисел, которые являются пересечением двух множеств
def find_intersection_of_sets(lst1, lst2):
    result = set(lst1) & set(lst2)
    if not result:
        return None
    return list(result)

# 302. Функция для нахождения чисел, которые присутствуют в одном из двух списков, но не в обоих
def find_symmetric_difference(lst1, lst2):
    result = set(lst1) ^ set(lst2)
    if not result:
        return None
    return list(result)

# 303. Функция для нахождения чисел, которые являются ключами в одном словаре и значениями в другом
def find_keys_in_dicts(dict1, dict2):
    result = [key for key in dict1 if dict1[key] in dict2]
    if not result:
        return None
    return result

# 304. Функция для нахождения чисел, которые присутствуют в списке, но не в кортеже
def find_in_list_not_in_tuple(lst, tpl):
    result = [x for x in lst if x not in tpl]
    if not result:
        return None
    return result

# 305. Функция для нахождения чисел, которые являются парами, где первое число больше второго
def find_pairs_with_first_greater(lst):
    result = [(a, b) for a in lst for b in lst if a > b]
    if not result:
        return None
    return result

# 306. Функция для нахождения чисел, которые являются кортежами, но не содержат отрицательных чисел
def find_tuples_without_negatives(lst):
    result = [tpl for tpl in lst if all(x >= 0 for x in tpl)]
    if not result:
        return None
    return result

# 307. Функция для нахождения чисел, которые присутствуют в словаре как ключи, но не имеют чётных значений
def find_keys_with_odd_values(dict_data):
    result = [key for key, value in dict_data.items() if value % 2 != 0]
    if not result:
        return None
    return result

# 308. Функция для нахождения чисел, которые являются произведением двух чисел, но не делятся на 2
def find_product_of_two_not_divisible_by_2(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            product = lst[i] * lst[j]
            if product % 2 != 0:
                result.append(product)
    if not result:
        return None
    return result

# 309. Функция для нахождения чисел, которые являются элементами множества, но не присутствуют в списке
def find_in_set_not_in_list(s, lst):
    result = list(s - set(lst))
    if not result:
        return None
    return result

# 310. Функция для нахождения чисел, которые присутствуют в словаре как ключи, но не делятся на 3
def find_keys_not_divisible_by_3(dict_data):
    result = [key for key in dict_data if key % 3 != 0]
    if not result:
        return None
    return result

# 311. Функция для нахождения чисел, которые встречаются в двух списках и их сумма делится на 4
def find_numbers_with_sum_divisible_by_4(lst1, lst2):
    result = []
    for num1 in lst1:
        for num2 in lst2:
            if (num1 + num2) % 4 == 0:
                result.append((num1, num2))
    if not result:
        return None
    return result

# 312. Функция для нахождения чисел, которые встречаются только в одном из двух списков
def find_unique_in_one_list(lst1, lst2):
    result = list(set(lst1) ^ set(lst2))
    if not result:
        return None
    return result

# 313. Функция для нахождения чисел, которые являются парами, где сумма элементов делится на 5
def find_pairs_with_sum_divisible_by_5(lst):
    result = [(a, b) for a in lst for b in lst if (a + b) % 5 == 0]
    if not result:
        return None
    return result

# 314. Функция для нахождения чисел, которые являются кортежами, но не содержат чётных чисел
def find_tuples_without_even_numbers(lst):
    result = [tpl for tpl in lst if all(x % 2 != 0 for x in tpl)]
    if not result:
        return None
    return result

# 315. Функция для нахождения чисел, которые являются целыми числами в строках
def find_integers_in_strings(lst):
    result = []
    for s in lst:
        try:
            num = int(s)
            result.append(num)
        except ValueError:
            continue
    if not result:
        return None
    return result

# 316. Функция для нахождения чисел, которые делятся на 7 и на 8, но не на 56
def find_divisible_by_7_and_8_not_56(lst):
    result = []
    for num in lst:
        if num % 7 == 0 and num % 8 == 0 and num % 56 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 317. Функция для нахождения чисел, которые являются нечётными и присутствуют в словаре как ключи
def find_odd_keys_in_dict(dict_data):
    result = [key for key in dict_data if key % 2 != 0]
    if not result:
        return None
    return result

# 318. Функция для нахождения чисел, которые являются чётными и присутствуют в кортеже, но не в списке
def find_even_in_tuple_not_in_list(tpl, lst):
    result = [x for x in tpl if x % 2 == 0 and x not in lst]
    if not result:
        return None
    return result

# 319. Функция для нахождения чисел, которые являются делителями 100, но не являются простыми
def find_divisors_of_100_not_prime(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = [num for num in lst if 100 % num == 0 and not is_prime(num)]
    if not result:
        return None
    return result

# 320. Функция для нахождения чисел, которые встречаются в списке, но не в множестве
def find_in_list_not_in_set(lst, s):
    result = [x for x in lst if x not in s]
    if not result:
        return None
    return result

# 321. Функция для нахождения чисел, которые являются результатами суммы элементов из двух списков
def find_sum_of_two_lists(lst1, lst2):
    result = [a + b for a in lst1 for b in lst2]
    if not result:
        return None
    return result

# 322. Функция для нахождения чисел, которые являются разностью элементов из двух списков
def find_difference_of_two_lists(lst1, lst2):
    result = [a - b for a in lst1 for b in lst2]
    if not result:
        return None
    return result

# 323. Функция для нахождения чисел, которые являются нечётными и присутствуют в кортеже, но не в списке
def find_odd_in_tuple_not_in_list(tpl, lst):
    result = [x for x in tpl if x % 2 != 0 and x not in lst]
    if not result:
        return None
    return result

# 324. Функция для нахождения чисел, которые делятся на 5 и на 6, но не на 12
def find_divisible_by_5_and_6_not_12(lst):
    result = []
    for num in lst:
        if num % 5 == 0 and num % 6 == 0 and num % 12 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 325. Функция для нахождения чисел, которые являются нечётными, но не являются делителями 5
def find_odd_not_divisible_by_5(lst):
    result = [num for num in lst if num % 2 != 0 and num % 5 != 0]
    if not result:
        return None
    return result

# 326. Функция для нахождения чисел, которые являются чётными и присутствуют в списке и кортеже
def find_even_in_list_and_tuple(lst, tpl):
    result = [x for x in lst if x % 2 == 0 and x in tpl]
    if not result:
        return None
    return result

# 327. Функция для нахождения чисел, которые являются результатом произведения двух чисел
def find_product_of_two_numbers(lst):
    result = [a * b for a in lst for b in lst]
    if not result:
        return None
    return result

# 328. Функция для нахождения чисел, которые являются элементами множества, но не встречаются в списке
def find_in_set_not_in_list(s, lst):
    result = [x for x in s if x not in lst]
    if not result:
        return None
    return result

# 329. Функция для нахождения чисел, которые являются результатами разности чисел в списках
def find_difference_between_lists(lst1, lst2):
    result = [a - b for a in lst1 for b in lst2]
    if not result:
        return None
    return result

# 330. Функция для нахождения чисел, которые присутствуют в одном из списков, но не в обоих
def find_unique_in_one_list_not_both(lst1, lst2):
    result = [x for x in lst1 if x not in lst2] + [x for x in lst2 if x not in lst1]
    if not result:
        return None
    return result


# 331. Функция для нахождения чисел, которые являются четными и делятся на 3
def find_even_and_divisible_by_3(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            if num % 3 == 0:
                result.append(num)
    if not result:
        return None
    return result

# 332. Функция для нахождения чисел, которые являются квадратами, но не делятся на 5
def find_squares_not_divisible_by_5(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num:
            if num % 5 != 0:
                result.append(num)
    if not result:
        return None
    return result

# 333. Функция для нахождения чисел, которые делятся на 7 и на 8, но не на 56
def find_divisible_by_7_and_8_not_56(lst):
    result = []
    for num in lst:
        if num % 7 == 0:
            if num % 8 == 0:
                if num % 56 != 0:
                    result.append(num)
    if not result:
        return None
    return result

# 334. Функция для нахождения чисел, которые делятся на 4, но не на 8
def find_divisible_by_4_not_8(lst):
    result = []
    for num in lst:
        if num % 4 == 0:
            if num % 8 != 0:
                result.append(num)
    if not result:
        return None
    return result

# 335. Функция для нахождения чисел, которые присутствуют в списке и кортежах
def find_in_list_and_tuple(lst, tpl):
    result = []
    for num in lst:
        if num in tpl:
            result.append(num)
    if not result:
        return None
    return result

# 336. Функция для нахождения чисел, которые делятся на 3, но не на 9
def find_divisible_by_3_not_9(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 337. Функция для нахождения чисел, которые являются разностью двух элементов списка
def find_difference_of_two_elements(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            result.append(abs(lst[i] - lst[j]))
    if not result:
        return None
    return result

# 338. Функция для нахождения чисел, которые являются суммой двух чисел, но не делятся на 4
def find_sum_of_two_not_divisible_by_4(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i] + lst[j]) % 4 != 0:
                result.append(lst[i] + lst[j])
    if not result:
        return None
    return result

# 339. Функция для нахождения чисел, которые присутствуют в одном из списков, но не в обоих
def find_unique_in_one_list(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    for num in lst2:
        if num not in lst1:
            result.append(num)
    if not result:
        return None
    return result

# 340. Функция для нахождения чисел, которые делятся на 5, но не на 10
def find_divisible_by_5_not_10(lst):
    result = []
    for num in lst:
        if num % 5 == 0 and num % 10 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 341. Функция для нахождения чисел, которые присутствуют в кортеже, но не в списке
def find_in_tuple_not_in_list(tpl, lst):
    result = []
    for num in tpl:
        if num not in lst:
            result.append(num)
    if not result:
        return None
    return result

# 342. Функция для нахождения чисел, которые присутствуют в обоих списках
def find_in_both_lists(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2:
            result.append(num)
    if not result:
        return None
    return result

# 343. Функция для нахождения чисел, которые являются четными и не делятся на 5
def find_even_not_divisible_by_5(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 344. Функция для нахождения чисел, которые не присутствуют в одном из списков
def find_not_in_list(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    if not result:
        return None
    return result

# 345. Функция для нахождения чисел, которые являются произведением двух чисел, но не делятся на 7
def find_product_not_divisible_by_7(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            product = lst[i] * lst[j]
            if product % 7 != 0:
                result.append(product)
    if not result:
        return None
    return result

# 346. Функция для нахождения чисел, которые делятся на 3, но не на 6
def find_divisible_by_3_not_6(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 6 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 347. Функция для нахождения чисел, которые являются произведением двух нечётных чисел
def find_product_of_two_odds(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] % 2 != 0 and lst[j] % 2 != 0:
                result.append(lst[i] * lst[j])
    if not result:
        return None
    return result

# 348. Функция для нахождения чисел, которые являются суммой двух нечётных чисел
def find_sum_of_two_odds(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] % 2 != 0 and lst[j] % 2 != 0:
                result.append(lst[i] + lst[j])
    if not result:
        return None
    return result

# 349. Функция для нахождения чисел, которые присутствуют в обоих словарях как ключи
def find_keys_in_both_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2:
            result.append(key)
    if not result:
        return None
    return result

# 350. Функция для нахождения чисел, которые являются четными и находятся в кортеже
def find_even_in_tuple(tpl):
    result = []
    for num in tpl:
        if num % 2 == 0:
            result.append(num)
    if not result:
        return None
    return result

# 351. Функция для нахождения чисел, которые являются результатом разности двух чисел
def find_difference_between_two_numbers(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            result.append(abs(lst[i] - lst[j]))
    if not result:
        return None
    return result

# 352. Функция для нахождения чисел, которые являются произведением двух чисел, но не на 5
def find_product_not_divisible_by_5(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            product = lst[i] * lst[j]
            if product % 5 != 0:
                result.append(product)
    if not result:
        return None
    return result

# 353. Функция для нахождения чисел, которые делятся на 9, но не на 3
def find_divisible_by_9_not_3(lst):
    result = []
    for num in lst:
        if num % 9 == 0 and num % 3 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 354. Функция для нахождения чисел, которые присутствуют в одном словаре, но не в другом
def find_keys_in_dict_not_in_other(dict1, dict2):
    result = []
    for key in dict1:
        if key not in dict2:
            result.append(key)
    if not result:
        return None
    return result

# 355. Функция для нахождения чисел, которые являются разностью элементов в кортеже
def find_difference_in_tuple(tpl):
    result = []
    for i in range(len(tpl)):
        for j in range(i + 1, len(tpl)):
            result.append(abs(tpl[i] - tpl[j]))
    if not result:
        return None
    return result

# 356. Функция для нахождения чисел, которые являются результатом суммы двух чисел из списка
def find_sum_of_two_from_list(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            result.append(lst[i] + lst[j])
    if not result:
        return None
    return result

# 357. Функция для нахождения чисел, которые являются результатом разности двух чисел из двух списков
def find_difference_between_lists(lst1, lst2):
    result = []
    for num1 in lst1:
        for num2 in lst2:
            result.append(abs(num1 - num2))
    if not result:
        return None
    return result

# 358. Функция для нахождения чисел, которые являются нечётными и присутствуют в одном из списков
def find_odd_in_one_list(lst1, lst2):
    result = []
    for num in lst1:
        if num % 2 != 0 and num not in lst2:
            result.append(num)
    for num in lst2:
        if num % 2 != 0 and num not in lst1:
            result.append(num)
    if not result:
        return None
    return result

# 359. Функция для нахождения чисел, которые являются результатом суммы двух чисел из одного списка
def find_sum_of_two_from_one_list(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            result.append(lst[i] + lst[j])
    if not result:
        return None
    return result

# 360. Функция для нахождения чисел, которые встречаются в обоих списках, но не в обоих списках сразу
def find_common_not_in_both_lists(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2:
            result.append(num)
    if not result:
        return None
    return result


# 361. Функция для нахождения чисел, которые являются результатом суммы элементов двух списков
def find_sum_of_elements_from_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a + b)
    if not result:
        return None
    return result

# 362. Функция для нахождения чисел, которые являются результатом произведения чисел из двух списков
def find_product_of_elements_from_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a * b)
    if not result:
        return None
    return result

# 363. Функция для нахождения чисел, которые являются результатом разности элементов из двух списков
def find_difference_of_elements_from_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a - b)
    if not result:
        return None
    return result

# 364. Функция для преобразования чисел из списка в их квадраты
def square_numbers(lst):
    result = list(map(lambda x: x ** 2, lst))
    if not result:
        return None
    return result

# 365. Функция для нахождения чисел, которые делятся на 3, но не на 5
def find_divisible_by_3_not_5(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 366. Функция для нахождения чисел, которые присутствуют только в одном из двух списков
def find_unique_in_one_list(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if a != b:
            result.append(a)
            result.append(b)
    if not result:
        return None
    return result

# 367. Функция для нахождения чисел, которые присутствуют в списке, но не в кортеже
def find_in_list_not_in_tuple(lst, tpl):
    result = []
    for num in lst:
        if num not in tpl:
            result.append(num)
    if not result:
        return None
    return result

# 368. Функция для нахождения чисел, которые являются кубами чисел в списке
def find_cubes(lst):
    result = list(map(lambda x: x ** 3, lst))
    if not result:
        return None
    return result

# 369. Функция для нахождения чисел, которые делятся на 2 и 3
def find_divisible_by_2_and_3(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 == 0:
            result.append(num)
    if not result:
        return None
    return result

# 370. Функция для нахождения чисел, которые не присутствуют в двух списках одновременно
def find_not_in_both_lists(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    for num in lst2:
        if num not in lst1:
            result.append(num)
    if not result:
        return None
    return result

# 371. Функция для нахождения чисел, которые являются результатом возведения в степень
def find_powers_of_numbers(lst, power):
    result = list(map(lambda x: x ** power, lst))
    if not result:
        return None
    return result

# 372. Функция для нахождения чисел, которые присутствуют только в одном из двух списков
def find_unique_elements_in_lists(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    for num in lst2:
        if num not in lst1:
            result.append(num)
    if not result:
        return None
    return result

# 373. Функция для нахождения чисел, которые являются суммой чисел из двух списков
def find_sum_from_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a + b)
    if not result:
        return None
    return result

# 374. Функция для нахождения чисел, которые являются результатом разности двух чисел в разных списках
def find_difference_between_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(abs(a - b))
    if not result:
        return None
    return result

# 375. Функция для нахождения чисел, которые присутствуют в обоих списках
def find_common_elements_in_lists(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2:
            result.append(num)
    if not result:
        return None
    return result

# 376. Функция для нахождения чисел, которые присутствуют в обоих множествам
def find_common_elements_in_sets(set1, set2):
    result = list(set1 & set2)
    if not result:
        return None
    return result

# 377. Функция для нахождения чисел, которые присутствуют в первом списке, но не во втором
def find_elements_in_first_not_in_second(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    if not result:
        return None
    return result

# 378. Функция для нахождения чисел, которые присутствуют в обоих словарях
def find_keys_in_both_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2:
            result.append(key)
    if not result:
        return None
    return result

# 379. Функция для нахождения чисел, которые являются результатом произведения чисел из двух списков
def find_product_of_elements_from_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a * b)
    if not result:
        return None
    return result

# 380. Функция для нахождения чисел, которые встречаются только в одном из двух списков
def find_unique_in_either_list(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    for num in lst2:
        if num not in lst1:
            result.append(num)
    if not result:
        return None
    return result

# 381. Функция для нахождения чисел, которые присутствуют в словаре, но не в списке
def find_keys_in_dict_not_in_list(d, lst):
    result = []
    for key in d:
        if key not in lst:
            result.append(key)
    if not result:
        return None
    return result

# 382. Функция для нахождения чисел, которые делятся на 2 или 5
def find_divisible_by_2_or_5(lst):
    result = []
    for num in lst:
        if num % 2 == 0 or num % 5 == 0:
            result.append(num)
    if not result:
        return None
    return result

# 383. Функция для нахождения чисел, которые делятся на 3 и 5
def find_divisible_by_3_and_5(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 5 == 0:
            result.append(num)
    if not result:
        return None
    return result

# 384. Функция для нахождения чисел, которые являются результатом возведения чисел из списка в степень
def find_powers_of_numbers_in_list(lst, power):
    result = []
    for num in lst:
        result.append(num ** power)
    if not result:
        return None
    return result

# 385. Функция для нахождения чисел, которые делятся на 7, но не на 14
def find_divisible_by_7_not_14(lst):
    result = []
    for num in lst:
        if num % 7 == 0 and num % 14 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 386. Функция для нахождения чисел, которые присутствуют в обоих множествах
def find_elements_in_both_sets(set1, set2):
    result = list(set1 & set2)
    if not result:
        return None
    return result

# 387. Функция для нахождения чисел, которые делятся на 6, но не на 12
def find_divisible_by_6_not_12(lst):
    result = []
    for num in lst:
        if num % 6 == 0 and num % 12 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 388. Функция для нахождения чисел, которые присутствуют в первом списке, но не в общем с вторым
def find_in_first_not_in_second(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    if not result:
        return None
    return result

# 389. Функция для нахождения чисел, которые делятся на 8, но не на 16
def find_divisible_by_8_not_16(lst):
    result = []
    for num in lst:
        if num % 8 == 0 and num % 16 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 390. Функция для нахождения чисел, которые являются разницей элементов из двух списков
def find_diff_between_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(abs(a - b))
    if not result:
        return None
    return result

# 391. Функция для нахождения чисел, которые делятся на 3 или 5
def find_divisible_by_3_or_5(lst):
    result = []
    for num in lst:
        if num % 3 == 0 or num % 5 == 0:
            result.append(num)
    if not result:
        return None
    return result

# 392. Функция для нахождения чисел, которые являются результатом сложения чисел в двух списках
def find_sum_of_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a + b)
    if not result:
        return None
    return result

# 393. Функция для нахождения чисел, которые встречаются в одном словаре, но не в другом
def find_keys_in_dict_not_in_other_dict(dict1, dict2):
    result = []
    for key in dict1:
        if key not in dict2:
            result.append(key)
    if not result:
        return None
    return result

# 394. Функция для нахождения чисел, которые присутствуют в кортеже, но не в списке
def find_in_tuple_not_in_list(tpl, lst):
    result = []
    for num in tpl:
        if num not in lst:
            result.append(num)
    if not result:
        return None
    return result

# 395. Функция для нахождения чисел, которые являются произведением двух чисел в списке
def find_product_of_two_numbers_in_list(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            result.append(lst[i] * lst[j])
    if not result:
        return None
    return result

# 396. Функция для нахождения чисел, которые делятся на 10, но не на 20
def find_divisible_by_10_not_20(lst):
    result = []
    for num in lst:
        if num % 10 == 0 and num % 20 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 397. Функция для нахождения чисел, которые являются суммой элементов из двух списков
def find_sum_from_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a + b)
    if not result:
        return None
    return result

# 398. Функция для нахождения чисел, которые присутствуют в обоих множествах
def find_common_elements_in_sets(set1, set2):
    result = list(set1 & set2)
    if not result:
        return None
    return result

# 399. Функция для нахождения чисел, которые являются произведением чисел в списке
def find_product_in_list(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            result.append(lst[i] * lst[j])
    if not result:
        return None
    return result

# 400. Функция для нахождения чисел, которые являются результатом возведения элементов из списка в степень
def find_powers_of_numbers(lst, power):
    result = []
    for num in lst:
        result.append(num ** power)
    if not result:
        return None
    return result


# 401. Функция для нахождения чисел, которые присутствуют в списке и не присутствуют в словаре
def find_in_list_not_in_dict(lst, d):
    result = []
    for num in lst:
        if num not in d:
            result.append(num)
    if not result:
        return None
    return result

# 402. Функция для объединения двух словарей
def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    if not result:
        return None
    return result

# 403. Функция для нахождения чисел, которые присутствуют в одном из двух наборов
def find_in_one_set_not_other(set1, set2):
    result = set1.symmetric_difference(set2)
    if not result:
        return None
    return list(result)

# 404. Функция для нахождения чисел, которые являются результатом деления элементов из двух списков
def find_division_from_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:  # избегаем деления на ноль
            result.append(a / b)
    if not result:
        return None
    return result

# 405. Функция для нахождения чисел, которые являются результатом квадратных корней чисел из списка
import math

def find_square_roots(lst):
    result = []
    for num in lst:
        if num >= 0:
            result.append(math.sqrt(num))
    if not result:
        return None
    return result

# 406. Функция для нахождения чисел, которые присутствуют в обоих списках, но в одном из них меньше
def find_common_less_in_one_list(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2 and lst1.count(num) < lst2.count(num):
            result.append(num)
    if not result:
        return None
    return result

# 407. Функция для нахождения чисел, которые находятся в одном списке, но не в другом
def find_in_first_not_in_second(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    if not result:
        return None
    return result

# 408. Функция для нахождения чисел, которые присутствуют в обоих списках, но имеют разные индексы
def find_common_elements_diff_index(lst1, lst2):
    result = []
    for i, num1 in enumerate(lst1):
        for j, num2 in enumerate(lst2):
            if num1 == num2 and i != j:
                result.append(num1)
    if not result:
        return None
    return result

# 409. Функция для нахождения чисел, которые являются результатом добавления элементов из двух словарей
def add_values_of_dicts(dict1, dict2):
    result = {}
    for key in dict1:
        if key in dict2:
            result[key] = dict1[key] + dict2[key]
    if not result:
        return None
    return result

# 410. Функция для нахождения чисел, которые находятся в двух множествах, но в одном из них больше
def find_more_in_one_set(set1, set2):
    result = []
    for num in set1:
        if num in set2 and set1.count(num) > set2.count(num):
            result.append(num)
    if not result:
        return None
    return result

# 411. Функция для нахождения чисел, которые являются результатом умножения чисел в списке на два
def multiply_numbers_by_two(lst):
    result = []
    for num in lst:
        result.append(num * 2)
    if not result:
        return None
    return result

# 412. Функция для нахождения чисел, которые содержатся только в одном из двух списков
def find_unique_in_one_list(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    for num in lst2:
        if num not in lst1:
            result.append(num)
    if not result:
        return None
    return result

# 413. Функция для нахождения чисел, которые являются результатом суммы значений по ключам в словарях
def sum_dict_values(dict1, dict2):
    result = {}
    for key in dict1:
        if key in dict2:
            result[key] = dict1[key] + dict2[key]
    if not result:
        return None
    return result

# 414. Функция для нахождения чисел, которые являются квадратами чисел из списка
def find_squares(lst):
    result = []
    for num in lst:
        result.append(num ** 2)
    if not result:
        return None
    return result

# 415. Функция для нахождения чисел, которые являются разницей элементов из двух множеств
def find_difference_of_sets(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result

# 416. Функция для нахождения чисел, которые являются результатом суммирования элементов из списка и множества
def find_sum_list_set(lst, s):
    result = []
    for num in lst:
        if num in s:
            result.append(num + 1)
    if not result:
        return None
    return result

# 417. Функция для нахождения чисел, которые присутствуют в одном из двух списков, но не в обоих
def find_in_either_list(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    for num in lst2:
        if num not in lst1:
            result.append(num)
    if not result:
        return None
    return result

# 418. Функция для нахождения чисел, которые встречаются в одном множестве, но не в другом
def find_in_set_not_in_other_set(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result

# 419. Функция для нахождения чисел, которые являются результатом деления элементов одного списка на элементы другого
def divide_elements_of_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:  # избегаем деления на ноль
            result.append(a / b)
    if not result:
        return None
    return result

# 420. Функция для нахождения чисел, которые содержатся в одном словаре, но не в другом
def find_keys_in_dict1_not_in_dict2(dict1, dict2):
    result = []
    for key in dict1:
        if key not in dict2:
            result.append(key)
    if not result:
        return None
    return result

# 421. Функция для нахождения чисел, которые находятся в двух множествах, но не в одном из них
def find_in_both_sets_not_in_one(set1, set2):
    result = list(set1 & set2 - (set1 | set2))
    if not result:
        return None
    return result

# 422. Функция для нахождения чисел, которые присутствуют в одном из двух списков, но не в обоих
def find_unique_in_both_lists(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    for num in lst2:
        if num not in lst1:
            result.append(num)
    if not result:
        return None
    return result

# 423. Функция для нахождения чисел, которые содержатся в кортеже, но не в списке
def find_in_tuple_not_in_list(tpl, lst):
    result = []
    for num in tpl:
        if num not in lst:
            result.append(num)
    if not result:
        return None
    return result

# 424. Функция для нахождения чисел, которые являются результатом вычитания элементов из списка и множества
def subtract_set_from_list(lst, s):
    result = []
    for num in lst:
        if num not in s:
            result.append(num)
    if not result:
        return None
    return result

# 425. Функция для нахождения чисел, которые являются результатом суммирования элементов из двух кортежей
def find_sum_of_tuples(tpl1, tpl2):
    result = []
    for a, b in zip(tpl1, tpl2):
        result.append(a + b)
    if not result:
        return None
    return result


# 426. Функция для нахождения чисел, которые встречаются в обоих множествах
def find_common_in_sets(set1, set2):
    result = list(set1 & set2)
    if not result:
        return None
    return result

# 427. Функция для нахождения чисел, которые находятся в одном из двух списков, но не в обоих
def find_in_either_list(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    for num in lst2:
        if num not in lst1:
            result.append(num)
    if not result:
        return None
    return result

# 428. Функция для нахождения чисел, которые встречаются только в одном из двух кортежей
def find_unique_in_tuple(tpl1, tpl2):
    result = []
    for num in tpl1:
        if num not in tpl2:
            result.append(num)
    for num in tpl2:
        if num not in tpl1:
            result.append(num)
    if not result:
        return None
    return result

# 429. Функция для нахождения чисел, которые делятся на 5, но не на 10
def find_divisible_by_5_not_10(lst):
    result = []
    for num in lst:
        if num % 5 == 0 and num % 10 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 430. Функция для нахождения чисел, которые присутствуют в одном из двух множеств
def find_in_one_set_not_other(set1, set2):
    result = list(set1 ^ set2)  # Симметрическая разница
    if not result:
        return None
    return result

# 431. Функция для нахождения чисел, которые делятся на 4, но не на 8
def find_divisible_by_4_not_8(lst):
    result = []
    for num in lst:
        if num % 4 == 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 432. Функция для нахождения чисел, которые присутствуют в одном словаре, но не в другом
def find_keys_in_dict1_not_in_dict2(dict1, dict2):
    result = []
    for key in dict1:
        if key not in dict2:
            result.append(key)
    if not result:
        return None
    return result

# 433. Функция для нахождения чисел, которые делятся на 6, но не на 12
def find_divisible_by_6_not_12(lst):
    result = []
    for num in lst:
        if num % 6 == 0 and num % 12 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 434. Функция для нахождения чисел, которые являются результатом возведения элементов списка в степень
def find_powers_of_list(lst, power):
    result = []
    for num in lst:
        result.append(num ** power)
    if not result:
        return None
    return result

# 435. Функция для нахождения чисел, которые встречаются в одном списке, но не в другом
def find_in_first_not_in_second(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    if not result:
        return None
    return result

# 436. Функция для нахождения чисел, которые являются результатом умножения чисел в одном списке на два
def multiply_by_two(lst):
    result = []
    for num in lst:
        result.append(num * 2)
    if not result:
        return None
    return result

# 437. Функция для нахождения чисел, которые являются результатом вычитания элементов одного списка из другого
def subtract_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a - b)
    if not result:
        return None
    return result

# 438. Функция для нахождения чисел, которые являются результатом деления чисел в одном списке на числа из другого
def divide_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:
            result.append(a / b)
    if not result:
        return None
    return result

# 439. Функция для нахождения чисел, которые присутствуют в обоих словарях
def find_common_in_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2:
            result.append(key)
    if not result:
        return None
    return result

# 440. Функция для нахождения чисел, которые присутствуют в одном из двух списков, но не в обоих
def find_in_either_but_not_both(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    for num in lst2:
        if num not in lst1:
            result.append(num)
    if not result:
        return None
    return result

# 441. Функция для нахождения чисел, которые присутствуют только в одном словаре
def find_unique_in_dict(dict1, dict2):
    result = []
    for key in dict1:
        if key not in dict2:
            result.append(key)
    for key in dict2:
        if key not in dict1:
            result.append(key)
    if not result:
        return None
    return result

# 442. Функция для нахождения чисел, которые являются результатом сложения всех чисел в списке
def sum_list(lst):
    return sum(lst) if lst else None

# 443. Функция для нахождения чисел, которые делятся на 3, но не на 9
def find_divisible_by_3_not_9(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 444. Функция для нахождения чисел, которые делятся на 5 или 7
def find_divisible_by_5_or_7(lst):
    result = []
    for num in lst:
        if num % 5 == 0 or num % 7 == 0:
            result.append(num)
    if not result:
        return None
    return result

# 445. Функция для нахождения чисел, которые являются разницей элементов из двух множеств
def find_difference_in_sets(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result

# 446. Функция для нахождения чисел, которые присутствуют в одном множестве, но не в другом
def find_in_set_not_other(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result

# 447. Функция для нахождения чисел, которые делятся на 6, но не на 12
def find_divisible_by_6_not_12(lst):
    result = []
    for num in lst:
        if num % 6 == 0 and num % 12 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 448. Функция для нахождения чисел, которые присутствуют в кортеже, но не в списке
def find_in_tuple_not_in_list(tpl, lst):
    result = []
    for num in tpl:
        if num not in lst:
            result.append(num)
    if not result:
        return None
    return result

# 449. Функция для нахождения чисел, которые содержатся в одном из двух наборов
def find_in_one_set_not_other(set1, set2):
    result = list(set1 ^ set2)
    if not result:
        return None
    return result

# 450. Функция для нахождения чисел, которые являются результатом вычитания элементов из двух кортежей
def subtract_tuples(tpl1, tpl2):
    result = []
    for a, b in zip(tpl1, tpl2):
        result.append(a - b)
    if not result:
        return None
    return result

# 451. Функция для нахождения чисел, которые являются произведением чисел из двух списков
def multiply_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a * b)
    if not result:
        return None
    return result

# 452. Функция для нахождения чисел, которые являются результатом деления чисел одного списка на числа другого
def divide_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:
            result.append(a / b)
    if not result:
        return None
    return result

# 453. Функция для нахождения чисел, которые делятся на 4, но не на 8
def find_divisible_by_4_not_8(lst):
    result = []
    for num in lst:
        if num % 4 == 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 454. Функция для нахождения чисел, которые являются квадратами чисел из списка
def find_squares(lst):
    result = []
    for num in lst:
        result.append(num ** 2)
    if not result:
        return None
    return result

# 455. Функция для нахождения чисел, которые присутствуют в одном из двух словарей
def find_in_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2:
            result.append(key)
    if not result:
        return None
    return result

# 456. Функция для нахождения чисел, которые встречаются только в одном из двух списков
def find_in_one_not_in_other(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    for num in lst2:
        if num not in lst1:
            result.append(num)
    if not result:
        return None
    return result

# 457. Функция для нахождения чисел, которые присутствуют в одном из двух множеств
def find_in_sets(set1, set2):
    result = list(set1 ^ set2)
    if not result:
        return None
    return result

# 458. Функция для нахождения чисел, которые присутствуют в одном из двух кортежей
def find_in_tuples(tpl1, tpl2):
    result = []
    for num in tpl1:
        if num not in tpl2:
            result.append(num)
    for num in tpl2:
        if num not in tpl1:
            result.append(num)
    if not result:
        return None
    return result

# 459. Функция для нахождения чисел, которые являются разницей элементов из двух списков
def subtract_lists(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    if not result:
        return None
    return result

# 460. Функция для нахождения чисел, которые делятся на 3 или 5
def find_divisible_by_3_or_5(lst):
    result = []
    for num in lst:
        if num % 3 == 0 or num % 5 == 0:
            result.append(num)
    if not result:
        return None
    return result

## Вот здесь разрыв

# 476. Функция для нахождения чисел, которые делятся на 4, но не на 6
def find_divisible_by_4_not_6(lst):
    result = []
    for num in lst:
        if num % 4 == 0 and num % 6 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 477. Функция для нахождения чисел, которые присутствуют в одном множестве, но не в другом
def find_in_set_not_other(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result

# 478. Функция для нахождения чисел, которые присутствуют в одном из двух множеств
def find_in_one_set_not_other(set1, set2):
    result = list(set1 ^ set2)  # Симметрическая разница
    if not result:
        return None
    return result

# 479. Функция для нахождения чисел, которые делятся на 5, но не на 10
def find_divisible_by_5_not_10(lst):
    result = []
    for num in lst:
        if num % 5 == 0 and num % 10 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 480. Функция для нахождения чисел, которые являются результатом возведения элементов списка в степень
def find_powers_of_list(lst, power):
    result = []
    for num in lst:
        result.append(num ** power)
    if not result:
        return None
    return result

# 481. Функция для нахождения чисел, которые делятся на 6, но не на 12
def find_divisible_by_6_not_12(lst):
    result = []
    for num in lst:
        if num % 6 == 0 and num % 12 != 0:
            result.append(num)
    if not result:
        return None
    return result

# 482. Функция для нахождения чисел, которые присутствуют в одном словаре, но не в другом
def find_keys_in_dict1_not_in_dict2(dict1, dict2):
    result = []
    for key in dict1:
        if key not in dict2:
            result.append(key)
    if not result:
        return None
    return result

# 483. Функция для нахождения чисел, которые присутствуют в одном из двух кортежей, но не в обоих
def find_unique_in_tuples(tpl1, tpl2):
    result = []
    for num in tpl1:
        if num not in tpl2:
            result.append(num)
    for num in tpl2:
        if num not in tpl1:
            result.append(num)
    if not result:
        return None
    return result

# 484. Функция для нахождения чисел, которые являются результатом сложения всех чисел в списке
def sum_list(lst):
    return sum(lst) if lst else None

# 485. Функция для нахождения чисел, которые присутствуют в одном из двух словарей, но не в обоих
def find_keys_in_one_dict_not_other(dict1, dict2):
    result = []
    for key in dict1:
        if key not in dict2:
            result.append(key)
    for key in dict2:
        if key not in dict1:
            result.append(key)
    if not result:
        return None
    return result

# 486. Функция для нахождения чисел, которые делятся на 4 или 5
def find_divisible_by_4_or_5(lst):
    result = []
    for num in lst:
        if num % 4 == 0 or num % 5 == 0:
            result.append(num)
    if not result:
        return None
    return result

# 487. Функция для нахождения чисел, которые встречаются в одном списке, но не в другом
def find_in_first_not_in_second(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    if not result:
        return None
    return result

# 488. Функция для нахождения чисел, которые являются квадратами чисел из списка
def find_squares(lst):
    result = []
    for num in lst:
        result.append(num ** 2)
    if not result:
        return None
    return result

# 489. Функция для нахождения чисел, которые встречаются в обоих множествам
def find_common_in_sets(set1, set2):
    result = list(set1 & set2)
    if not result:
        return None
    return result

# 490. Функция для нахождения чисел, которые присутствуют в одном из двух списков, но не в обоих
def find_in_either_but_not_both(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    for num in lst2:
        if num not in lst1:
            result.append(num)
    if not result:
        return None
    return result

# 491. Функция для нахождения чисел, которые являются разницей элементов из двух множеств
def find_difference_in_sets(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result

# 492. Функция для нахождения чисел, которые присутствуют в одном списке, но не в другом
def find_in_list_not_in_another(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    if not result:
        return None
    return result

# 493. Функция для нахождения чисел, которые присутствуют в одном словаре, но не в другом
def find_unique_keys_in_dict(dict1, dict2):
    result = []
    for key in dict1:
        if key not in dict2:
            result.append(key)
    if not result:
        return None
    return result

# 494. Функция для нахождения чисел, которые являются разницей элементов из двух списков
def subtract_lists(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    if not result:
        return None
    return result

# 495. Функция для нахождения чисел, которые являются произведением чисел из двух списков
def multiply_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a * b)
    if not result:
        return None
    return result

# 496. Функция для нахождения чисел, которые присутствуют в одном из двух кортежей
def find_in_tuples_not_in_other(tpl1, tpl2):
    result = []
    for num in tpl1:
        if num not in tpl2:
            result.append(num)
    for num in tpl2:
        if num not in tpl1:
            result.append(num)
    if not result:
        return None
    return result

# 497. Функция для нахождения чисел, которые встречаются только в одном из двух списков
def find_in_one_list_not_other(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    for num in lst2:
        if num not in lst1:
            result.append(num)
    if not result:
        return None
    return result

# 498. Функция для нахождения чисел, которые делятся на 3 или 5
def find_divisible_by_3_or_5(lst):
    result = []
    for num in lst:
        if num % 3 == 0 or num % 5 == 0:
            result.append(num)
    if not result:
        return None
    return result

# 499. Функция для нахождения чисел, которые являются результатом вычитания элементов одного списка из другого
def subtract_lists_v2(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a - b)
    if not result:
        return None
    return result

# 500. Функция для нахождения чисел, которые являются результатом деления чисел из одного списка на числа из другого
def divide_lists_v2(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:
            result.append(a / b)
    if not result:
        return None
    return result


# 501. Функция для нахождения чисел, которые присутствуют в одном множестве, но не в другом
def find_in_set_not_other(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result

# 502. Функция для нахождения чисел, которые присутствуют в обоих множествах
def find_common_in_sets(set1, set2):
    result = list(set1 & set2)
    if not result:
        return None
    return result

# 503. Функция для нахождения чисел, которые присутствуют в одном из двух множеств, но не в обоих
def find_in_one_set_not_other(set1, set2):
    result = list(set1 ^ set2)  # Симметрическая разница
    if not result:
        return None
    return result

# 504. Функция для нахождения чисел, которые делятся на 2 и присутствуют в двух множествах
def find_divisible_by_2_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 2 == 0})
    if not result:
        return None
    return result

# 505. Функция для нахождения чисел, которые не делятся на 3 и присутствуют в двух множествах
def find_not_divisible_by_3_in_both_sets(set1, set2):
    result = list((set1 & set2) - {num for num in range(1, 101) if num % 3 == 0})
    if not result:
        return None
    return result

# 506. Функция для нахождения элементов, присутствующих только в одном множестве
def find_unique_elements(set1, set2):
    result = list(set1 ^ set2)  # Симметрическая разница
    if not result:
        return None
    return result

# 507. Функция для нахождения чисел, которые присутствуют в одном множестве и не присутствуют в другом
def find_in_one_set_not_other_v2(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result

# 508. Функция для нахождения чисел, которые делятся на 2 или 5, и присутствуют в двух множествах
def find_divisible_by_2_or_5_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 2 == 0 or num % 5 == 0})
    if not result:
        return None
    return result

# 509. Функция для нахождения чисел, которые не делятся на 2 или 3, и присутствуют в двух множествах
def find_not_divisible_by_2_or_3_in_both_sets(set1, set2):
    result = list((set1 & set2) - {num for num in range(1, 101) if num % 2 == 0 or num % 3 == 0})
    if not result:
        return None
    return result

# 510. Функция для нахождения чисел, которые делятся на 4 и присутствуют в обоих множествах
def find_divisible_by_4_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 4 == 0})
    if not result:
        return None
    return result

# 511. Функция для нахождения чисел, которые присутствуют в одном множестве, но не в другом
def find_in_set_not_other_v2(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result

# 512. Функция для нахождения чисел, которые присутствуют в одном из двух множеств
def find_in_any_set(set1, set2):
    result = list(set1 | set2)  # Объединение
    if not result:
        return None
    return result

# 513. Функция для нахождения чисел, которые делятся на 7 и присутствуют в обоих множествах
def find_divisible_by_7_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 7 == 0})
    if not result:
        return None
    return result

# 514. Функция для нахождения чисел, которые присутствуют в одном множестве, но не в другом
def find_difference_in_sets(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result

# 515. Функция для нахождения чисел, которые не делятся на 2, но присутствуют в обоих множествах
def find_not_divisible_by_2_in_both_sets(set1, set2):
    result = list((set1 & set2) - {num for num in range(1, 101) if num % 2 == 0})
    if not result:
        return None
    return result

# 516. Функция для нахождения чисел, которые являются общими для трёх множеств
def find_common_in_three_sets(set1, set2, set3):
    result = list(set1 & set2 & set3)
    if not result:
        return None
    return result

# 517. Функция для нахождения чисел, которые являются разностью элементов из трёх множеств
def find_difference_in_three_sets(set1, set2, set3):
    result = list(set1 - set2 - set3)
    if not result:
        return None
    return result

# 518. Функция для нахождения чисел, которые присутствуют в одном множестве, но не в другом
def find_diff_in_sets_v2(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result

# 519. Функция для нахождения чисел, которые не делятся на 5 и присутствуют в обоих множествах
def find_not_divisible_by_5_in_both_sets(set1, set2):
    result = list((set1 & set2) - {num for num in range(1, 101) if num % 5 == 0})
    if not result:
        return None
    return result

# 520. Функция для нахождения чисел, которые делятся на 3 или 6 и присутствуют в обоих множествах
def find_divisible_by_3_or_6_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 3 == 0 or num % 6 == 0})
    if not result:
        return None
    return result

# 521. Функция для нахождения чисел, которые являются общими для двух множеств и делятся на 3
def find_common_in_sets_divisible_by_3(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 3 == 0})
    if not result:
        return None
    return result

# 522. Функция для нахождения чисел, которые делятся на 6, но не на 12 и присутствуют в двух множествах
def find_divisible_by_6_not_12_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 6 == 0 and num % 12 != 0})
    if not result:
        return None
    return result

# 523. Функция для нахождения чисел, которые не присутствуют в обоих множествах
def find_not_in_both_sets(set1, set2):
    result = list(set1 ^ set2)  # Симметрическая разница
    if not result:
        return None
    return result

# 524. Функция для нахождения чисел, которые являются разницей между тремя множествами
def find_difference_between_three_sets(set1, set2, set3):
    result = list(set1 - set2 - set3)
    if not result:
        return None
    return result

# 525. Функция для нахождения чисел, которые делятся на 2, но не на 3, и присутствуют в двух множествах
def find_divisible_by_2_not_3_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 2 == 0 and num % 3 != 0})
    if not result:
        return None
    return result

# 526. Функция для нахождения чисел, которые присутствуют в обоих множествах и не делятся на 4
def find_common_not_divisible_by_4(set1, set2):
    result = list((set1 & set2) - {num for num in range(1, 101) if num % 4 == 0})
    if not result:
        return None
    return result

# 527. Функция для нахождения чисел, которые присутствуют только в одном из двух множеств
def find_unique_in_sets(set1, set2):
    result = list(set1 ^ set2)  # Симметрическая разница
    if not result:
        return None
    return result

# 528. Функция для нахождения чисел, которые являются общими для всех трёх множеств
def find_common_in_all_sets(set1, set2, set3):
    result = list(set1 & set2 & set3)
    if not result:
        return None
    return result

# 529. Функция для нахождения чисел, которые присутствуют в двух множествах и не делятся на 3
def find_in_both_sets_not_divisible_by_3(set1, set2):
    result = list((set1 & set2) - {num for num in range(1, 101) if num % 3 == 0})
    if not result:
        return None
    return result

# 530. Функция для нахождения чисел, которые присутствуют только в одном из двух множеств
def find_unique_in_one_set(set1, set2):
    result = list(set1 ^ set2)  # Симметрическая разница
    if not result:
        return None
    return result



# 541. Функция для нахождения чисел, которые присутствуют в одном множестве, но не в другом
def find_in_set_not_other_v3(set1, set2):
    result = []
    for elem in set1:
        if elem not in set2:
            result.append(elem)
    if not result:
        return None
    return result

# 542. Функция для нахождения чисел, которые являются пересечением двух множеств и делятся на 3
def find_common_divisible_by_3(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 543. Функция для нахождения чисел, которые присутствуют в одном из двух множеств, но не в обоих
def find_in_one_set_not_other_v3(set1, set2):
    result = []
    for elem in set1 | set2:
        if (elem in set1) != (elem in set2):  # Проверка на симметричную разницу
            result.append(elem)
    if not result:
        return None
    return result

# 544. Функция для нахождения чисел, которые делятся на 2, но не на 4 и присутствуют в двух множествах
def find_divisible_by_2_not_4_in_both_sets(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 2 == 0 and elem % 4 != 0:
            result.append(elem)
    if not result:
        return None
    return result

# 545. Функция для нахождения чисел, которые присутствуют в двух множествах и не делятся на 5
def find_in_both_sets_not_divisible_by_5(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 5 != 0:
            result.append(elem)
    if not result:
        return None
    return result

# 546. Функция для нахождения чисел, которые присутствуют в обоих множествах и делятся на 3
def find_in_both_sets_divisible_by_3(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 547. Функция для нахождения чисел, которые присутствуют в одном из двух множеств, но не в обоих
def find_unique_in_sets_v2(set1, set2):
    result = []
    for elem in set1 ^ set2:  # Симметрическая разница
        result.append(elem)
    if not result:
        return None
    return result

# 548. Функция для нахождения чисел, которые присутствуют в первом множестве, но не во втором, и делятся на 7
def find_in_first_set_not_second_divisible_by_7(set1, set2):
    result = []
    for elem in set1 - set2:
        if elem % 7 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 549. Функция для нахождения чисел, которые делятся на 6, но не на 12 и присутствуют в двух множествах
def find_divisible_by_6_not_12_in_both_sets(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 6 == 0 and elem % 12 != 0:
            result.append(elem)
    if not result:
        return None
    return result

# 550. Функция для нахождения чисел, которые присутствуют в одном из двух множеств, но не в обоих, и делятся на 5
def find_in_one_set_not_other_divisible_by_5(set1, set2):
    result = []
    for elem in set1 ^ set2:  # Симметрическая разница
        if elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 551. Функция для нахождения чисел, которые являются общими для двух множеств и делятся на 4
def find_common_in_sets_divisible_by_4(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 4 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 552. Функция для нахождения чисел, которые присутствуют только в одном множестве
def find_unique_in_one_set_v2(set1, set2):
    result = []
    for elem in set1:
        if elem not in set2:
            result.append(elem)
    for elem in set2:
        if elem not in set1:
            result.append(elem)
    if not result:
        return None
    return result

# 553. Функция для нахождения чисел, которые делятся на 3 и присутствуют в обоих множествах
def find_divisible_by_3_in_both_sets(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 554. Функция для нахождения чисел, которые присутствуют только в одном из двух множеств, но не в другом
def find_difference_in_sets_v2(set1, set2):
    result = []
    for elem in set1 - set2:
        result.append(elem)
    for elem in set2 - set1:
        result.append(elem)
    if not result:
        return None
    return result

# 555. Функция для нахождения чисел, которые присутствуют в двух множествах и делятся на 4
def find_divisible_by_4_in_both_sets(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 4 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 556. Функция для нахождения чисел, которые присутствуют только в одном множестве и не делятся на 3
def find_unique_not_divisible_by_3(set1, set2):
    result = []
    for elem in set1 - set2:
        if elem % 3 != 0:
            result.append(elem)
    for elem in set2 - set1:
        if elem % 3 != 0:
            result.append(elem)
    if not result:
        return None
    return result

# 557. Функция для нахождения чисел, которые делятся на 5 и присутствуют в двух множествах
def find_divisible_by_5_in_both_sets(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 558. Функция для нахождения чисел, которые присутствуют в обоих множествах и не делятся на 2
def find_in_both_sets_not_divisible_by_2(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 2 != 0:
            result.append(elem)
    if not result:
        return None
    return result

# 559. Функция для нахождения чисел, которые являются разностью между двумя множествами
def find_difference_between_sets(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result

# 560. Функция для нахождения чисел, которые присутствуют в одном из двух множеств, но не в обоих
def find_unique_elements_in_sets(set1, set2):
    result = list(set1 ^ set2)  # Симметрическая разница
    if not result:
        return None
    return result

# 561. Функция для нахождения чисел, которые делятся на 2 и присутствуют в двух множествах
def find_divisible_by_2_in_both_sets(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 562. Функция для нахождения чисел, которые присутствуют в первом множестве, но не во втором
def find_in_first_set_not_second(set1, set2):
    result = []
    for elem in set1 - set2:
        result.append(elem)
    if not result:
        return None
    return result

# 563. Функция для нахождения чисел, которые делятся на 5 и присутствуют только в одном множестве
def find_divisible_by_5_in_one_set(set1, set2):
    result = []
    for elem in set1:
        if elem % 5 == 0 and elem not in set2:
            result.append(elem)
    if not result:
        return None
    return result


# 564. Функция для проверки, является ли стек пустым
def is_stack_empty(stack):
    if len(stack) == 0:
        return True
    return False

# 565. Функция для добавления элементов в стек, пока не будет достигнут определённый предел
def fill_stack_until_limit(stack, limit):
    while len(stack) < limit:
        stack.append(len(stack) + 1)
    return stack

# 566. Функция для пополнения стека числами от 1 до N
def fill_stack_up_to_n(stack, n):
    for i in range(1, n + 1):
        stack.append(i)
    return stack

# 567. Функция для извлечения всех элементов из стека и их возвращения в обратном порядке
def reverse_stack(stack):
    reversed_stack = []
    while stack:
        reversed_stack.append(stack.pop())
    return reversed_stack

# 568. Функция для проверки, является ли стек палиндромом
def is_stack_palindrome(stack):
    original = list(stack)  # Копия стека
    reversed_stack = reverse_stack(stack)
    if original == reversed_stack:
        return True
    return False

# 569. Функция для извлечения и возврата элементов из стека, пока не встретится число, большее чем X
def pop_until_greater_than_x(stack, x):
    popped_elements = []
    while stack:
        elem = stack.pop()
        if elem > x:
            popped_elements.append(elem)
            break
        popped_elements.append(elem)
    if not popped_elements:
        return None
    return popped_elements

# 570. Функция для извлечения и возврата всех элементов стека, меньших чем Y
def pop_elements_less_than_y(stack, y):
    result = []
    while stack:
        elem = stack.pop()
        if elem < y:
            result.append(elem)
    if not result:
        return None
    return result

# 571. Функция для удаления всех нечётных чисел из стека
def remove_odds_from_stack(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 572. Функция для извлечения элементов из стека до тех пор, пока сумма элементов не превысит X
def pop_until_sum_exceeds_x(stack, x):
    popped_elements = []
    current_sum = 0
    while stack and current_sum <= x:
        elem = stack.pop()
        popped_elements.append(elem)
        current_sum += elem
    if not popped_elements:
        return None
    return popped_elements

# 573. Функция для извлечения всех элементов из стека, которые делятся на 3
def pop_elements_divisible_by_3(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 574. Функция для поиска и извлечения наименьшего элемента из стека
def pop_min_element(stack):
    if not stack:
        return None
    min_elem = min(stack)
    stack.remove(min_elem)
    return min_elem

# 575. Функция для создания нового стека с удвоенными значениями исходного стека
def double_stack_values(stack):
    new_stack = []
    while stack:
        elem = stack.pop()
        new_stack.append(elem * 2)
    return new_stack

# 576. Функция для извлечения элементов, пока не встретится чётное число
def pop_until_even(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 2 == 0:
            result.append(elem)
            break
        result.append(elem)
    if not result:
        return None
    return result

# 577. Функция для извлечения всех чисел из стека, которые являются простыми
def pop_prime_numbers(stack):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    while stack:
        elem = stack.pop()
        if is_prime(elem):
            result.append(elem)
    if not result:
        return None
    return result

# 578. Функция для извлечения элементов из стека до тех пор, пока не встретится число, которое делится на 4
def pop_until_divisible_by_4(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 4 == 0:
            result.append(elem)
            break
        result.append(elem)
    if not result:
        return None
    return result

# 579. Функция для удаления из стека всех чисел, которые не делятся на 2
def remove_non_divisible_by_2(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 580. Функция для нахождения и удаления всех элементов стека, которые меньше X
def remove_less_than_x(stack, x):
    result = []
    while stack:
        elem = stack.pop()
        if elem >= x:
            result.append(elem)
    if not result:
        return None
    return result

# 581. Функция для нахождения максимального числа в стеке
def find_max_in_stack(stack):
    if not stack:
        return None
    max_elem = max(stack)
    return max_elem

# 582. Функция для нахождения и удаления всех чётных чисел из стека
def remove_even_from_stack(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 2 != 0:
            result.append(elem)
    if not result:
        return None
    return result

# 583. Функция для извлечения всех чисел из стека, которые больше чем X
def pop_elements_greater_than_x(stack, x):
    result = []
    while stack:
        elem = stack.pop()
        if elem > x:
            result.append(elem)
    if not result:
        return None
    return result

# 584. Функция для нахождения всех чётных чисел в стеке
def find_even_in_stack(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 585. Функция для удаления всех чисел, которые делятся на 5 из стека
def remove_divisible_by_5_from_stack(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 5 != 0:
            result.append(elem)
    if not result:
        return None
    return result

# 586. Функция для удаления максимального элемента из стека
def remove_max_from_stack(stack):
    if not stack:
        return None
    max_elem = max(stack)
    stack.remove(max_elem)
    return max_elem

# 587. Функция для нахождения и извлечения всех чисел, которые не делятся на 3
def pop_elements_not_divisible_by_3(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 3 != 0:
            result.append(elem)
    if not result:
        return None
    return result


# 588. Функция для извлечения элементов из стека, пока их сумма не станет больше X
def pop_until_sum_exceeds(stack, x):
    result = []
    total = 0
    while stack:
        elem = stack.pop()
        result.append(elem)
        total += elem
        if total > x:
            break
    if not result:
        return None
    return result

# 589. Функция для нахождения элементов, которые меньше, чем среднее значение стека
def pop_elements_less_than_average(stack):
    result = []
    if not stack:
        return None
    average = sum(stack) / len(stack)
    while stack:
        elem = stack.pop()
        if elem < average:
            result.append(elem)
    if not result:
        return None
    return result

# 590. Функция для нахождения элементов, которые не встречаются более одного раза в стеке
def pop_unique_elements(stack):
    result = []
    element_count = {}
    while stack:
        elem = stack.pop()
        element_count[elem] = element_count.get(elem, 0) + 1

    for elem in element_count:
        if element_count[elem] == 1:
            result.append(elem)
    if not result:
        return None
    return result

# 591. Функция для извлечения всех элементов стека, которые делятся на 5
def pop_elements_divisible_by_5(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 592. Функция для нахождения элементов, которые больше, чем X, и возвращения их в обратном порядке
def pop_elements_greater_than_x_reverse(stack, x):
    result = []
    while stack:
        elem = stack.pop()
        if elem > x:
            result.append(elem)
    if not result:
        return None
    return result[::-1]

# 593. Функция для удаления всех элементов, которые меньше, чем X, из стека
def remove_less_than_x(stack, x):
    result = []
    while stack:
        elem = stack.pop()
        if elem >= x:
            result.append(elem)
    if not result:
        return None
    return result

# 594. Функция для нахождения наименьшего элемента в стеке
def find_min_in_stack(stack):
    if not stack:
        return None
    min_elem = min(stack)
    return min_elem

# 595. Функция для извлечения элементов, пока не встретится число, которое делится на 6
def pop_until_divisible_by_6(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 6 == 0:
            result.append(elem)
            break
        result.append(elem)
    if not result:
        return None
    return result

# 596. Функция для нахождения всех чисел в стеке, которые являются чётными и делятся на 4
def find_even_divisible_by_4(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 2 == 0 and elem % 4 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 597. Функция для нахождения чисел в стеке, которые делятся на 3, но не на 6
def find_divisible_by_3_not_6(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 3 == 0 and elem % 6 != 0:
            result.append(elem)
    if not result:
        return None
    return result

# 598. Функция для извлечения всех нечётных чисел из стека
def pop_odd_elements(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 2 != 0:
            result.append(elem)
    if not result:
        return None
    return result

# 599. Функция для нахождения всех чисел, которые меньше X, и их удаления из стека
def remove_less_than_x_v2(stack, x):
    result = []
    while stack:
        elem = stack.pop()
        if elem < x:
            result.append(elem)
    if not result:
        return None
    return result

# 600. Функция для нахождения всех чисел в стеке, которые являются квадратами целых чисел
def find_square_numbers_in_stack(stack):
    result = []
    while stack:
        elem = stack.pop()
        if (elem ** 0.5).is_integer():
            result.append(elem)
    if not result:
        return None
    return result

# 601. Функция для нахождения наибольшего элемента в стеке
def find_max_in_stack(stack):
    if not stack:
        return None
    max_elem = max(stack)
    return max_elem

# 602. Функция для извлечения всех элементов стека, которые делятся на 7
def pop_elements_divisible_by_7(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 7 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 603. Функция для нахождения всех чисел, которые больше X и делятся на 2
def find_greater_than_x_divisible_by_2(stack, x):
    result = []
    while stack:
        elem = stack.pop()
        if elem > x and elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 604. Функция для извлечения и удаления всех элементов стека, которые не делятся на 4
def remove_not_divisible_by_4(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 4 != 0:
            result.append(elem)
    if not result:
        return None
    return result

# 605. Функция для извлечения всех чисел, которые делятся на 10, из стека
def pop_elements_divisible_by_10(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 10 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 606. Функция для нахождения всех элементов стека, которые делятся на 3 и на 5
def find_divisible_by_3_and_5(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 3 == 0 and elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 607. Функция для удаления всех элементов стека, которые больше X
def remove_greater_than_x(stack, x):
    result = []
    while stack:
        elem = stack.pop()
        if elem <= x:
            result.append(elem)
    if not result:
        return None
    return result

# 608. Функция для нахождения чисел, которые делятся на 2 или на 3
def find_divisible_by_2_or_3(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 2 == 0 or elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 609. Функция для извлечения и удаления всех чисел, которые больше, чем X и чётные
def pop_elements_greater_than_x_even(stack, x):
    result = []
    while stack:
        elem = stack.pop()
        if elem > x and elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return result



# 610. Функция для извлечения элементов из очереди, пока их сумма не станет больше X
def process_queue_until_sum_exceeds(queue, x):
    result = []
    total = 0
    while queue:
        elem = queue.pop(0)
        result.append(elem)
        total += elem
        if total > x:
            break
    if not result:
        return None
    return result

# 611. Функция для нахождения всех элементов в очереди, которые меньше среднего
def process_queue_less_than_average(queue):
    result = []
    if not queue:
        return None
    average = sum(queue) / len(queue)
    while queue:
        elem = queue.pop(0)
        if elem < average:
            result.append(elem)
    if not result:
        return None
    return result

# 612. Функция для нахождения уникальных элементов, встречающихся только один раз в очереди
def process_queue_unique_elements(queue):
    result = []
    element_count = {}
    while queue:
        elem = queue.pop(0)
        element_count[elem] = element_count.get(elem, 0) + 1

    for elem in element_count:
        if element_count[elem] == 1:
            result.append(elem)
    if not result:
        return None
    return result

# 613. Функция для извлечения всех чисел, которые делятся на 5 из очереди
def process_queue_divisible_by_5(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 614. Функция для извлечения всех чисел из очереди, которые больше X
def process_queue_greater_than_x(queue, x):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem > x:
            result.append(elem)
    if not result:
        return None
    return result

# 615. Функция для извлечения всех чисел из очереди, которые делятся на 2, но не на 4
def process_queue_divisible_by_2_not_4(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem % 2 == 0 and elem % 4 != 0:
            result.append(elem)
    if not result:
        return None
    return result

# 616. Функция для нахождения всех элементов, которые делятся на 7 из очереди
def process_queue_divisible_by_7(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem % 7 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 617. Функция для нахождения всех чисел в очереди, которые больше X и делятся на 2
def process_queue_greater_than_x_and_divisible_by_2(queue, x):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem > x and elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 618. Функция для извлечения и возвращения всех элементов из очереди, которые являются нечётными
def process_queue_odd_elements(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem % 2 != 0:
            result.append(elem)
    if not result:
        return None
    return result

# 619. Функция для извлечения и возвращения всех чисел, которые являются квадратами целых чисел
def process_queue_square_numbers(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if (elem ** 0.5).is_integer():
            result.append(elem)
    if not result:
        return None
    return result

# 620. Функция для извлечения всех чисел, которые делятся на 3 или на 5
def process_queue_divisible_by_3_or_5(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem % 3 == 0 or elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 621. Функция для извлечения всех чисел, которые делятся на 3, но не на 6
def process_queue_divisible_by_3_not_6(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem % 3 == 0 and elem % 6 != 0:
            result.append(elem)
    if not result:
        return None
    return result

# 622. Функция для удаления всех чисел из очереди, которые меньше, чем X
def process_queue_remove_less_than_x(queue, x):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem >= x:
            result.append(elem)
    if not result:
        return None
    return result

# 623. Функция для извлечения всех чисел, которые меньше X
def process_queue_less_than_x(queue, x):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem < x:
            result.append(elem)
    if not result:
        return None
    return result

# 624. Функция для нахождения и извлечения минимального элемента из очереди
def process_queue_min_element(queue):
    if not queue:
        return None
    min_elem = min(queue)
    queue.remove(min_elem)
    return min_elem

# 625. Функция для удаления всех элементов из очереди, которые больше X
def process_queue_remove_greater_than_x(queue, x):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem <= x:
            result.append(elem)
    if not result:
        return None
    return result

# 626. Функция для нахождения и извлечения максимального элемента из очереди
def process_queue_max_element(queue):
    if not queue:
        return None
    max_elem = max(queue)
    queue.remove(max_elem)
    return max_elem

# 627. Функция для удаления всех элементов из очереди, которые делятся на 4
def process_queue_remove_divisible_by_4(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem % 4 != 0:
            result.append(elem)
    if not result:
        return None
    return result

# 628. Функция для извлечения всех чисел, которые больше X, и делятся на 2
def process_queue_greater_than_x_and_divisible_by_2(queue, x):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem > x and elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 629. Функция для извлечения всех элементов из очереди, которые больше X и делятся на 3
def process_queue_greater_than_x_and_divisible_by_3(queue, x):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem > x and elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 630. Функция для извлечения всех элементов из очереди, которые меньше X и не делятся на 5
def process_queue_less_than_x_not_divisible_by_5(queue, x):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem < x and elem % 5 != 0:
            result.append(elem)
    if not result:
        return None
    return result

# 631. Функция для нахождения всех чисел в очереди, которые являются чётными и делятся на 4
def process_queue_even_and_divisible_by_4(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem % 2 == 0 and elem % 4 == 0:
            result.append(elem)
    if not result:
        return None
    return result

# 632. Функция для нахождения всех элементов, которые не делятся на 3 и на 5
def process_queue_not_divisible_by_3_and_5(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem % 3 != 0 and elem % 5 != 0:
            result.append(elem)
    if not result:
        return None
    return result


# 633. Функция для нахождения всех элементов в кортеже, которые больше X
def find_elements_greater_than_x(tpl, x):
    result = []
    for elem in tpl:
        if elem > x:
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 634. Функция для извлечения всех чётных чисел из кортежа
def find_even_elements_in_tuple(tpl):
    result = []
    for elem in tpl:
        if elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 635. Функция для нахождения всех элементов, которые меньше среднего значения кортежа
def find_elements_less_than_average(tpl):
    result = []
    if not tpl:
        return None
    average = sum(tpl) / len(tpl)
    for elem in tpl:
        if elem < average:
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 636. Функция для нахождения всех элементов, которые больше X и делятся на 5
def find_elements_greater_than_x_divisible_by_5(tpl, x):
    result = []
    for elem in tpl:
        if elem > x and elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 637. Функция для извлечения элементов, которые не встречаются более одного раза в кортеже
def find_unique_elements_in_tuple(tpl):
    result = []
    element_count = {}
    for elem in tpl:
        element_count[elem] = element_count.get(elem, 0) + 1
    for elem in element_count:
        if element_count[elem] == 1:
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 638. Функция для нахождения чисел, которые делятся на 3 и на 4
def find_divisible_by_3_and_4(tpl):
    result = []
    for elem in tpl:
        if elem % 3 == 0 and elem % 4 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 639. Функция для извлечения всех нечётных чисел из кортежа
def find_odd_elements_in_tuple(tpl):
    result = []
    for elem in tpl:
        if elem % 2 != 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 640. Функция для нахождения минимального числа в кортеже
def find_min_in_tuple(tpl):
    if not tpl:
        return None
    return min(tpl)

# 641. Функция для нахождения максимального числа в кортеже
def find_max_in_tuple(tpl):
    if not tpl:
        return None
    return max(tpl)

# 642. Функция для нахождения чисел, которые делятся на 2 или на 5
def find_divisible_by_2_or_5(tpl):
    result = []
    for elem in tpl:
        if elem % 2 == 0 or elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 643. Функция для извлечения всех чисел, которые делятся на 6
def find_divisible_by_6(tpl):
    result = []
    for elem in tpl:
        if elem % 6 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 644. Функция для нахождения чисел, которые являются квадратами целых чисел
def find_square_numbers_in_tuple(tpl):
    result = []
    for elem in tpl:
        if (elem ** 0.5).is_integer():
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 645. Функция для нахождения чисел, которые больше X, но не делятся на 3
def find_greater_than_x_not_divisible_by_3(tpl, x):
    result = []
    for elem in tpl:
        if elem > x and elem % 3 != 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 646. Функция для нахождения чисел, которые делятся на 4, но не на 8
def find_divisible_by_4_not_8(tpl):
    result = []
    for elem in tpl:
        if elem % 4 == 0 and elem % 8 != 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 647. Функция для нахождения всех чисел, которые больше X, и делятся на 3
def find_greater_than_x_divisible_by_3(tpl, x):
    result = []
    for elem in tpl:
        if elem > x and elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 648. Функция для нахождения чисел, которые не делятся на 4 и на 5
def find_not_divisible_by_4_and_5(tpl):
    result = []
    for elem in tpl:
        if elem % 4 != 0 and elem % 5 != 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 649. Функция для нахождения чисел, которые меньше X, но делятся на 3
def find_less_than_x_divisible_by_3(tpl, x):
    result = []
    for elem in tpl:
        if elem < x and elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 650. Функция для нахождения чисел, которые делятся на 2 и на 5
def find_divisible_by_2_and_5(tpl):
    result = []
    for elem in tpl:
        if elem % 2 == 0 and elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 651. Функция для нахождения чисел, которые не являются квадратами целых чисел
def find_not_square_numbers_in_tuple(tpl):
    result = []
    for elem in tpl:
        if not (elem ** 0.5).is_integer():
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 652. Функция для извлечения чисел, которые делятся на 9, но не на 3
def find_divisible_by_9_not_3(tpl):
    result = []
    for elem in tpl:
        if elem % 9 == 0 and elem % 3 != 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 653. Функция для нахождения чисел, которые делятся на 2 и на 7
def find_divisible_by_2_and_7(tpl):
    result = []
    for elem in tpl:
        if elem % 2 == 0 and elem % 7 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 654. Функция для нахождения чисел, которые меньше X и являются нечётными
def find_less_than_x_odd(tpl, x):
    result = []
    for elem in tpl:
        if elem < x and elem % 2 != 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)

# 655. Функция для нахождения всех чисел, которые больше X и являются чётными
def find_greater_than_x_even(tpl, x):
    result = []
    for elem in tpl:
        if elem > x and elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)



# 656. Функция для получения уникальных элементов из списка с помощью множества
def unique_elements_from_list(lst):
    if not lst:
        return None
    unique_elements = set(lst)
    return tuple(unique_elements)

# 657. Функция для нахождения пересечения двух списков
def intersection_of_lists(lst1, lst2):
    result = list(set(lst1) & set(lst2))
    if not result:
        return None
    return result

# 658. Функция для объединения двух словарей, если они не содержат одинаковых ключей
def merge_dicts_no_common_keys(d1, d2):
    if any(k in d2 for k in d1):
        return None
    merged_dict = {**d1, **d2}
    return merged_dict

# 659. Функция для переворота строки
def reverse_string(s):
    if not s:
        return None
    return s[::-1]

# 660. Функция для нахождения всех чисел, которые являются делителями числа X
def divisors_of_x(x):
    if x <= 0:
        return None
    divisors = []
    for i in range(1, x + 1):
        if x % i == 0:
            divisors.append(i)
    if not divisors:
        return None
    return divisors

# 661. Функция для подсчёта количества вхождений каждого элемента в список
def count_elements_in_list(lst):
    if not lst:
        return None
    count_dict = {}
    for elem in lst:
        count_dict[elem] = count_dict.get(elem, 0) + 1
    return count_dict

# 662. Функция для создания словаря из списка пар (ключ, значение)
def list_to_dict(lst):
    if not lst or len(lst) % 2 != 0:
        return None
    return dict(zip(lst[::2], lst[1::2]))

# 663. Функция для подсчёта чётных и нечётных чисел в списке
def count_even_and_odd(lst):
    if not lst:
        return None
    even_count = 0
    odd_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return {"even": even_count, "odd": odd_count}

# 664. Функция для извлечения всех гласных из строки
def extract_vowels_from_string(s):
    if not s:
        return None
    vowels = "aeiouAEIOU"
    result = [ch for ch in s if ch in vowels]
    if not result:
        return None
    return ''.join(result)

# 665. Функция для слияния двух отсортированных списков в один отсортированный
def merge_sorted_lists(lst1, lst2):
    if not lst1 and not lst2:
        return None
    return sorted(lst1 + lst2)

# 666. Функция для проверки, является ли строка палиндромом
def is_palindrome(s):
    if not s:
        return None
    return s == s[::-1]

# 667. Функция для нахождения наибольшего общего делителя двух чисел
def gcd_of_two_numbers(a, b):
    if a <= 0 or b <= 0:
        return None
    while b:
        a, b = b, a % b
    return a

# 668. Функция для нахождения всех простых чисел в диапазоне от 1 до X
def prime_numbers_up_to_x(x):
    if x < 2:
        return None
    primes = []
    for num in range(2, x + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    if not primes:
        return None
    return primes

# 669. Функция для вычисления факториала числа
def factorial_of_number(n):
    if n < 0:
        return None
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# 670. Функция для подсчёта всех слов в строке
def count_words_in_string(s):
    if not s:
        return None
    return len(s.split())

# 671. Функция для нахождения всех индексов вхождения элемента в список
def find_all_indices_of_element(lst, element):
    if not lst:
        return None
    indices = [i for i, x in enumerate(lst) if x == element]
    if not indices:
        return None
    return indices

# 672. Функция для нахождения всех чисел, которые являются квадратами из списка
def square_numbers_from_list(lst):
    if not lst:
        return None
    squares = [x for x in lst if (x ** 0.5).is_integer()]
    if not squares:
        return None
    return squares

# 673. Функция для извлечения всех чисел, которые больше среднего значения
def greater_than_average(lst):
    if not lst:
        return None
    average = sum(lst) / len(lst)
    result = [x for x in lst if x > average]
    if not result:
        return None
    return result

# 674. Функция для сортировки списка строк по длине
def sort_strings_by_length(lst):
    if not lst:
        return None
    return sorted(lst, key=len)

# 675. Функция для нахождения суммы всех чисел в списке
def sum_of_elements(lst):
    if not lst:
        return None
    return sum(lst)

# 676. Функция для нахождения максимальной строки по длине из списка строк
def longest_string(lst):
    if not lst:
        return None
    return max(lst, key=len)

# 677. Функция для нахождения разницы между двумя множествами
def difference_between_sets(set1, set2):
    if not set1 or not set2:
        return None
    return set1 - set2

# 678. Функция для нахождения всех элементов, которые присутствуют в одном из двух списков
def union_of_lists(lst1, lst2):
    if not lst1 and not lst2:
        return None
    return list(set(lst1) | set(lst2))

# 679. Функция для нахождения всех элементов, которые присутствуют в обоих списках
def intersection_of_lists(lst1, lst2):
    if not lst1 and not lst2:
        return None
    return list(set(lst1) & set(lst2))

# 680. Функция для проверки, является ли строка цифрой
def is_digit(s):
    if not s:
        return None
    return s.isdigit()

# 681. Функция для извлечения всех буквенных символов из строки
def extract_letters_from_string(s):
    if not s:
        return None
    result = ''.join([ch for ch in s if ch.isalpha()])
    return result

# 682. Функция для нахождения всех элементов, которые являются строками в списке
def find_all_strings_in_list(lst):
    if not lst:
        return None
    return [x for x in lst if isinstance(x, str)]

# 683. Функция для проверки, все ли элементы в списке уникальны
def all_unique(lst):
    if not lst:
        return None
    return len(lst) == len(set(lst))

# 684. Функция для объединения всех элементов строки в единую строку с разделителями
def join_elements_with_separator(lst, separator):
    if not lst:
        return None
    return separator.join(lst)

# 685. Функция для нахождения разницы между двумя списками (без повторений)
def difference_between_lists(lst1, lst2):
    if not lst1 and not lst2:
        return None
    return list(set(lst1) - set(lst2))



# 686. Функция для подсчёта всех вхождений подстроки в строку без пересечения
def count_non_overlapping_substring(s, substring):
    if not s or not substring:
        return None
    count = 0
    i = 0
    while i < len(s):
        i = s.find(substring, i)
        if i == -1:
            break
        count += 1
        i += len(substring)  # Сдвигаем на длину подстроки, чтобы избежать пересечения
    return count

# 687. Функция для нахождения всех индексов вхождения подстроки в строку
def find_all_occurrences(s, substring):
    if not s or not substring:
        return None
    indices = []
    i = 0
    while i < len(s):
        i = s.find(substring, i)
        if i == -1:
            break
        indices.append(i)
        i += 1
    return indices if indices else None

# 688. Функция для нахождения всех слов, которые начинаются с определенной буквы
def find_words_starting_with(s, letter):
    if not s or not letter:
        return None
    words = s.split()
    result = [word for word in words if word[0].lower() == letter.lower()]
    return result if result else None

# 689. Функция для проверки, является ли строка анаграммой другой строки
def are_anagrams(s1, s2):
    if not s1 or not s2:
        return None
    return sorted(s1) == sorted(s2)

# 690. Функция для извлечения всех чисел, расположенных в строке
def extract_numbers_from_string(s):
    if not s:
        return None
    numbers = []
    current_number = []
    for ch in s:
        if ch.isdigit():
            current_number.append(ch)
        elif current_number:
            numbers.append(''.join(current_number))
            current_number = []
    if current_number:
        numbers.append(''.join(current_number))
    return numbers if numbers else None

# 691. Функция для проверки, является ли строка палиндромом (с учётом пробелов)
def is_palindrome_with_spaces(s):
    if not s:
        return None
    clean_s = ''.join(s.split()).lower()
    return clean_s == clean_s[::-1]

# 692. Функция для подсчёта количества гласных и согласных в строке
def count_vowels_and_consonants(s):
    if not s:
        return None
    vowels = "aeiouAEIOU"
    consonants = 0
    vowels_count = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                vowels_count += 1
            else:
                consonants += 1
    if vowels_count == 0 and consonants == 0:
        return None
    return {"vowels": vowels_count, "consonants": consonants}

# 693. Функция для удаления всех пробелов в строке, а затем инвертирования
def remove_spaces_and_reverse(s):
    if not s:
        return None
    no_spaces = s.replace(" ", "")
    return no_spaces[::-1]

# 694. Функция для нахождения подстроки с максимальной длиной без повторяющихся символов
def longest_unique_substring(s):
    if not s:
        return None
    max_len = 0
    max_substring = ""
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
        if len(seen) > max_len:
            max_len = len(seen)
            max_substring = s[i:i + max_len]
    return max_substring if max_len > 0 else None

# 695. Функция для нахождения наибольшего общего префикса двух строк
def longest_common_prefix(s1, s2):
    if not s1 or not s2:
        return None
    prefix = []
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            prefix.append(s1[i])
        else:
            break
    return ''.join(prefix) if prefix else None

# 696. Функция для подсчёта повторяющихся слов в строке
def count_repeating_words(s):
    if not s:
        return None
    words = s.split()
    word_count = {}
    for word in words:
        word_count[word.lower()] = word_count.get(word.lower(), 0) + 1
    return {word: count for word, count in word_count.items() if count > 1}

# 697. Функция для нахождения самого длинного слова в строке
def longest_word_in_string(s):
    if not s:
        return None
    words = s.split()
    return max(words, key=len) if words else None

# 698. Функция для извлечения подстрок длиной N
def extract_substrings_of_length_n(s, n):
    if not s or n <= 0:
        return None
    return [s[i:i+n] for i in range(len(s) - n + 1)]

# 699. Функция для удаления всех слов, которые начинаются на определённую букву
def remove_words_starting_with(s, letter):
    if not s or not letter:
        return None
    words = s.split()
    filtered_words = [word for word in words if not word.lower().startswith(letter.lower())]
    return ' '.join(filtered_words) if filtered_words else None

# 700. Функция для замены всех пробелов на подчеркивания
def replace_spaces_with_underscores(s):
    if not s:
        return None
    return s.replace(" ", "_")

# 701. Функция для нахождения всех возможных перестановок строки
def string_permutations(s):
    if not s:
        return None
    from itertools import permutations
    return [''.join(p) for p in permutations(s)]

# 702. Функция для извлечения всех буквенных символов и их сортировки по алфавиту
def sort_letters_in_string(s):
    if not s:
        return None
    letters = [ch for ch in s if ch.isalpha()]
    letters.sort()
    return ''.join(letters)

# 703. Функция для нахождения самого часто встречающегося символа в строке
def most_frequent_char(s):
    if not s:
        return None
    from collections import Counter
    counts = Counter(s)
    most_common = counts.most_common(1)
    return most_common[0][0] if most_common else None

# 704. Функция для удаления всех чисел из строки
def remove_numbers_from_string(s):
    if not s:
        return None
    return ''.join([ch for ch in s if not ch.isdigit()])

# 705. Функция для нахождения всех вхождений строки с учётом регистра
def find_case_sensitive_occurrences(s, substring):
    if not s or not substring:
        return None
    indices = []
    i = 0
    while i < len(s):
        i = s.find(substring, i)
        if i == -1:
            break
        indices.append(i)
        i += 1
    return indices if indices else None

# 706. Функция для нахождения подстроки, которая встречается чаще всего
def most_frequent_substring(s, length):
    if not s or length <= 0:
        return None
    substrings = [s[i:i+length] for i in range(len(s) - length + 1)]
    from collections import Counter
    counts = Counter(substrings)
    most_common = counts.most_common(1)
    return most_common[0][0] if most_common else None

# 707. Функция для удаления всех гласных из строки
def remove_vowels_from_string(s):
    if not s:
        return None
    vowels = "aeiouAEIOU"
    return ''.join([ch for ch in s if ch not in vowels])

# 708. Функция для вычисления расстояния Левенштейна между двумя строками
def levenshtein_distance(s1, s2):
    if not s1 or not s2:
        return None
    len_s1, len_s2 = len(s1), len(s2)
    dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    for i in range(len_s1 + 1):
        for j in range(len_s2 + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[len_s1][len_s2]

# 709. Функция для нахождения всех возможных подстрок строки заданной длины
def fixed_length_substrings(s, length):
    if not s or length <= 0:
        return None
    return [s[i:i+length] for i in range(len(s) - length + 1)]

# 710. Функция для удаления всех дублирующихся символов в строке
def remove_duplicates_from_string(s):
    if not s:
        return None
    return ''.join(sorted(set(s), key=s.index))



# 711. Функция для нахождения суммы всех чисел в списке с плавающими точками
def sum_of_floats(lst):
    if not lst:
        return None
    total = 0.0
    for num in lst:
        if isinstance(num, (int, float)):
            total += num
        else:
            return None
    return total

# 712. Функция для нахождения среднего арифметического с плавающими точками
def average_of_floats(lst):
    if not lst:
        return None
    total = sum_of_floats(lst)
    if total is None:
        return None
    return total / len(lst)

# 713. Функция для нахождения наибольшего числа с плавающей точкой в списке
def max_float(lst):
    if not lst:
        return None
    max_val = float('-inf')
    for num in lst:
        if isinstance(num, (int, float)) and num > max_val:
            max_val = num
    return max_val if max_val != float('-inf') else None

# 714. Функция для нахождения наименьшего числа с плавающей точкой в списке
def min_float(lst):
    if not lst:
        return None
    min_val = float('inf')
    for num in lst:
        if isinstance(num, (int, float)) and num < min_val:
            min_val = num
    return min_val if min_val != float('inf') else None

# 715. Функция для проверки, является ли число с плавающей точкой положительным
def is_positive_float(x):
    if not isinstance(x, (int, float)):
        return None
    return x > 0

# 716. Функция для нахождения разницы между двумя числами с плавающей точкой
def difference_between_floats(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return None
    return abs(x - y)

# 717. Функция для нахождения произведения всех чисел в списке с плавающими точками
def product_of_floats(lst):
    if not lst:
        return None
    product = 1.0
    for num in lst:
        if isinstance(num, (int, float)):
            product *= num
        else:
            return None
    return product

# 718. Функция для деления двух чисел с плавающей точкой с учётом ошибок деления на ноль
def divide_floats(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return None
    if y == 0:
        return None
    return x / y

# 719. Функция для нахождения квадратного корня числа с плавающей точкой
def square_root(x):
    if not isinstance(x, (int, float)) or x < 0:
        return None
    return x ** 0.5

# 720. Функция для округления числа с плавающей точкой до ближайшего целого
def round_to_nearest_integer(x):
    if not isinstance(x, (int, float)):
        return None
    return round(x)

# 721. Функция для нахождения всех чисел, которые делятся на X с плавающей точкой
def divisible_by_x(lst, x):
    if not isinstance(x, (int, float)) or x == 0 or not lst:
        return None
    result = []
    for num in lst:
        if isinstance(num, (int, float)) and num % x == 0:
            result.append(num)
    return result if result else None

# 722. Функция для вычисления значения экспоненты для числа с плавающей точкой
def exponentiation_of_float(x, n):
    if not isinstance(x, (int, float)) or not isinstance(n, (int, float)):
        return None
    return x ** n

# 723. Функция для вычисления факториала числа с плавающей точкой (для целых чисел)
def factorial_of_float(x):
    if not isinstance(x, int) or x < 0:
        return None
    factorial = 1
    for i in range(1, x + 1):
        factorial *= i
    return factorial

# 724. Функция для вычисления логарифма числа с плавающей точкой по основанию X
def log_of_float(x, base):
    if not isinstance(x, (int, float)) or not isinstance(base, (int, float)) or x <= 0 or base <= 1:
        return None
    import math
    return math.log(x, base)

# 725. Функция для нахождения чисел, которые больше среднего арифметического
def greater_than_average(lst):
    if not lst:
        return None
    avg = average_of_floats(lst)
    if avg is None:
        return None
    result = [x for x in lst if isinstance(x, (int, float)) and x > avg]
    return result if result else None

# 726. Функция для нахождения медианы в списке чисел с плавающей точкой
def median_of_floats(lst):
    if not lst:
        return None
    lst = [x for x in lst if isinstance(x, (int, float))]
    lst.sort()
    n = len(lst)
    if n == 0:
        return None
    if n % 2 == 1:
        return lst[n // 2]
    else:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2

# 727. Функция для нахождения всех чисел, которые являются простыми с плавающей точкой
def prime_floats(lst):
    if not lst:
        return None
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    result = [x for x in lst if isinstance(x, (int, float)) and is_prime(x)]
    return result if result else None

# 728. Функция для нахождения всех чисел в диапазоне от X до Y с плавающей точкой
def numbers_in_range(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return None
    return [i for i in range(int(x), int(y) + 1)]

# 729. Функция для нахождения геометрической прогрессии
def geometric_progression(a, r, n):
    if not isinstance(a, (int, float)) or not isinstance(r, (int, float)) or not isinstance(n, int) or n <= 0:
        return None
    result = [a * (r ** i) for i in range(n)]
    return result if result else None

# 730. Функция для нахождения суммы всех чисел в геометрической прогрессии
def sum_of_geometric_progression(a, r, n):
    if not isinstance(a, (int, float)) or not isinstance(r, (int, float)) or not isinstance(n, int) or n <= 0:
        return None
    if r == 1:
        return a * n
    return a * (1 - r ** n) / (1 - r)

# 731. Функция для нахождения числа Пи с заданной точностью
def pi_to_precision(precision):
    if not isinstance(precision, int) or precision <= 0:
        return None
    import math
    return round(math.pi, precision)

# 732. Функция для нахождения квадрата числа с плавающей точкой
def square_of_float(x):
    if not isinstance(x, (int, float)):
        return None
    return x * x

# 733. Функция для вычисления суммы ряда с плавающими числами (арифметическая прогрессия)
def sum_of_arithmetic_progression(a, d, n):
    if not isinstance(a, (int, float)) or not isinstance(d, (int, float)) or not isinstance(n, int) or n <= 0:
        return None
    return n * (2 * a + (n - 1) * d) / 2

# 734. Функция для нахождения разности между наибольшим и наименьшим числом с плавающей точкой
def difference_between_max_and_min(lst):
    if not lst:
        return None
    max_num = max_float(lst)
    min_num = min_float(lst)
    if max_num is None or min_num is None:
        return None
    return max_num - min_num


# 737. Функция для нахождения всех чисел, которые не равны нулю в списке с плавающими точками
def non_zero_floats(lst):
    if not lst:
        return None
    return [x for x in lst if isinstance(x, (int, float)) and x != 0]

# 738. Функция для вычисления разности между средним значением и каждым числом в списке
def difference_from_average(lst):
    if not lst:
        return None
    avg = average_of_floats(lst)
    if avg is None:
        return None
    return [abs(x - avg) for x in lst if isinstance(x, (int, float))]

# 739. Функция для нахождения чисел, квадрат которых больше заданного значения
def squares_greater_than(lst, value):
    if not isinstance(value, (int, float)) or not lst:
        return None
    return [x for x in lst if isinstance(x, (int, float)) and x ** 2 > value]

# 740. Функция для нахождения всех чисел, которые меньше заданного значения
def less_than_value(lst, value):
    if not isinstance(value, (int, float)) or not lst:
        return None
    return [x for x in lst if isinstance(x, (int, float)) and x < value]

# 741. Функция для нахождения суммы квадратов чисел в списке
def sum_of_squares(lst):
    if not lst:
        return None
    return sum(x ** 2 for x in lst if isinstance(x, (int, float)))

# 742. Функция для нахождения разности между максимальным и минимальным числом, но только для положительных чисел
def positive_max_min_difference(lst):
    if not lst:
        return None
    positive_numbers = [x for x in lst if isinstance(x, (int, float)) and x > 0]
    if not positive_numbers:
        return None
    return max(positive_numbers) - min(positive_numbers)

# 743. Функция для нахождения разности между максимальным и минимальным числом, но только для отрицательных чисел
def negative_max_min_difference(lst):
    if not lst:
        return None
    negative_numbers = [x for x in lst if isinstance(x, (int, float)) and x < 0]
    if not negative_numbers:
        return None
    return max(negative_numbers) - min(negative_numbers)

# 744. Функция для нахождения среднего квадратичного отклонения списка с плавающими числами
def standard_deviation(lst):
    if not lst:
        return None
    avg = average_of_floats(lst)
    if avg is None:
        return None
    variance = sum((x - avg) ** 2 for x in lst if isinstance(x, (int, float))) / len(lst)
    return variance ** 0.5

# 745. Функция для нахождения суммы всех чисел, которые делятся на X без остатка
def sum_of_divisible_by_x(lst, x):
    if not isinstance(x, (int, float)) or x == 0 or not lst:
        return None
    return sum(x for x in lst if isinstance(x, (int, float)) and x % x == 0)

# 746. Функция для вычисления коэффициента корреляции между двумя списками с плавающими точками
def correlation_coefficient(lst1, lst2):
    if not lst1 or not lst2 or len(lst1) != len(lst2):
        return None
    n = len(lst1)
    avg1, avg2 = average_of_floats(lst1), average_of_floats(lst2)
    if avg1 is None or avg2 is None:
        return None
    numerator = sum((x - avg1) * (y - avg2) for x, y in zip(lst1, lst2))
    denominator = (sum((x - avg1) ** 2 for x in lst1) ** 0.5) * (sum((y - avg2) ** 2 for y in lst2) ** 0.5)
    if denominator == 0:
        return None
    return numerator / denominator

# 747. Функция для нахождения медианы всех чисел, которые больше среднего
def median_greater_than_average(lst):
    if not lst:
        return None
    avg = average_of_floats(lst)
    if avg is None:
        return None
    greater_than_avg = [x for x in lst if isinstance(x, (int, float)) and x > avg]
    if not greater_than_avg:
        return None
    greater_than_avg.sort()
    n = len(greater_than_avg)
    if n % 2 == 1:
        return greater_than_avg[n // 2]
    else:
        return (greater_than_avg[n // 2 - 1] + greater_than_avg[n // 2]) / 2

# 748. Функция для нахождения всех чисел, которые являются кубами
def cubes(lst):
    if not lst:
        return None
    return [x for x in lst if isinstance(x, (int, float)) and round(x ** (1/3), 6) ** 3 == x]

# 749. Функция для нахождения разности между квадратами максимального и минимального числа
def square_difference_max_min(lst):
    if not lst:
        return None
    max_val = max_float(lst)
    min_val = min_float(lst)
    if max_val is None or min_val is None:
        return None
    return max_val ** 2 - min_val ** 2

# 750. Функция для нахождения чисел, которые могут быть представлены как сумма двух квадратов
def sum_of_two_squares(lst):
    if not lst:
        return None
    result = []
    for x in lst:
        if isinstance(x, (int, float)):
            for i in range(int(x ** 0.5) + 1):
                for j in range(int(x ** 0.5) + 1):
                    if i ** 2 + j ** 2 == x:
                        result.append(x)
                        break
    return result if result else None

# 751. Функция для проверки, является ли число с плавающей точкой степенью двойки
def is_power_of_two(x):
    if not isinstance(x, (int, float)) or x <= 0:
        return False
    return (x & (x - 1)) == 0

# 752. Функция для нахождения суммы всех чисел, которые являются степенями двойки
def sum_of_powers_of_two(lst):
    if not lst:
        return None
    return sum(x for x in lst if isinstance(x, (int, float)) and is_power_of_two(x))

# 753. Функция для нахождения суммы всех чисел, которые являются целыми степенями 10
def sum_of_powers_of_ten(lst):
    if not lst:
        return None
    return sum(x for x in lst if isinstance(x, (int, float)) and round(x, 10) == 10 ** round(math.log10(x)))

# 754. Функция для нахождения всех чисел, которые являются целыми числами
def integers_in_float_list(lst):
    if not lst:
        return None
    return [x for x in lst if isinstance(x, (int, float)) and x.is_integer()]

# 755. Функция для вычисления среднего квадратичного отклонения для заданного диапазона
def standard_deviation_in_range(lst, lower, upper):
    if not lst:
        return None
    valid_nums = [x for x in lst if isinstance(x, (int, float)) and lower <= x <= upper]
    if not valid_nums:
        return None
    avg = average_of_floats(valid_nums)
    variance = sum((x - avg) ** 2 for x in valid_nums) / len(valid_nums)
    return variance ** 0.5

# 756. Функция для нахождения суммы всех чисел, которые можно выразить как произведение двух простых чисел
def sum_of_products_of_primes(lst):
    if not lst:
        return None
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    result = []
    for num in lst:
        if isinstance(num, (int, float)):
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0 and is_prime(i) and is_prime(num // i):
                    result.append(num)
                    break
    return sum(result) if result else None

# 757. Функция для нахождения всех чисел, которые равны разности двух квадратов
def difference_of_two_squares(lst):
    if not lst:
        return None
    result = []
    for num in lst:
        if isinstance(num, (int, float)):
            for i in range(1, int(num ** 0.5) + 1):
                for j in range(i + 1, int(num ** 0.5) + 1):
                    if j ** 2 - i ** 2 == num:
                        result.append(num)
                        break
    return result if result else None

# 758. Функция для нахождения всех чисел, которые являются степенями 3 (кубами)
def cubes_of_numbers(lst):
    if not lst:
        return None
    return [x for x in lst if isinstance(x, (int, float)) and round(x ** (1/3), 6) ** 3 == x]

# 759. Функция для нахождения среднего арифметического квадратов чисел
def average_of_squares(lst):
    if not lst:
        return None
    return sum(x ** 2 for x in lst if isinstance(x, (int, float))) / len(lst)


# 760. Функция для вычисления факториала числа (рекурсия)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 761. Функция для вычисления суммы чисел от 1 до N (рекурсия)
def sum_to_n(n):
    if n == 0:
        return 0
    return n + sum_to_n(n - 1)

# 762. Функция для нахождения N-го числа Фибоначчи (рекурсия)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# 763. Функция для вычисления степени числа (рекурсия)
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

# 764. Функция для нахождения суммы элементов списка (рекурсия)
def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])

# 765. Функция для нахождения произведения элементов списка (рекурсия)
def recursive_product(lst):
    if not lst:
        return 1
    return lst[0] * recursive_product(lst[1:])

# 766. Функция для нахождения максимального числа в списке (рекурсия)
def recursive_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        sub_max = recursive_max(lst[1:])
        return lst[0] if lst[0] > sub_max else sub_max

# 767. Функция для нахождения минимального числа в списке (рекурсия)
def recursive_min(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        sub_min = recursive_min(lst[1:])
        return lst[0] if lst[0] < sub_min else sub_min

# 768. Функция для инвертирования строки (рекурсия)
def reverse_string(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])

# 769. Функция для проверки, является ли строка палиндромом (рекурсия)
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# 770. Функция для нахождения НОД (наибольший общий делитель) двух чисел (рекурсия)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 771. Функция для нахождения НОК (наименьшее общее кратное) двух чисел (рекурсия)
def lcm(a, b):
    if b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

# 772. Функция для подсчета количества вхождений элемента в списке (рекурсия)
def count_occurrences(lst, x):
    if not lst:
        return 0
    return (1 if lst[0] == x else 0) + count_occurrences(lst[1:], x)

# 773. Функция для проверки, является ли число простым (рекурсия)
def is_prime(n, divisor=None):
    if n <= 1:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor - 1)

# 774. Функция для нахождения наибольшего элемента в дереве (рекурсия)
def find_max_in_tree(tree):
    if tree is None:
        return float('-inf')
    left_max = find_max_in_tree(tree.get('left'))
    right_max = find_max_in_tree(tree.get('right'))
    return max(tree.get('value', float('-inf')), left_max, right_max)

# 775. Функция для проверки, является ли число четным (рекурсия)
def is_even(n):
    if n == 0:
        return True
    if n == 1:
        return False
    return is_even(n - 2)

# 776. Функция для вычисления суммы чисел, меньших X в списке (рекурсия)
def sum_less_than_x(lst, x):
    if not lst:
        return 0
    return (lst[0] if lst[0] < x else 0) + sum_less_than_x(lst[1:], x)

# 777. Функция для вычисления факториала числа с использованием хвоста (рекурсия с аккумулятором)
def factorial_tail(n, acc=1):
    if n == 0 or n == 1:
        return acc
    return factorial_tail(n - 1, acc * n)

# 778. Функция для вычисления суммы чисел в диапазоне от 1 до N, но с шагом 2 (рекурсия)
def sum_with_step(n):
    if n <= 0:
        return 0
    return n + sum_with_step(n - 2)

# 779. Функция для нахождения всех чисел Фибоначчи до N (рекурсия)
def fibonacci_up_to_n(n, a=0, b=1):
    if a > n:
        return []
    return [a] + fibonacci_up_to_n(n, b, a + b)

# 780. Функция для нахождения чисел, которые делятся на X, используя рекурсию
def find_divisible(lst, x):
    if not lst:
        return []
    return ([lst[0]] if lst[0] % x == 0 else []) + find_divisible(lst[1:], x)

# 781. Функция для подсчета количества четных чисел в списке (рекурсия)
def count_even(lst):
    if not lst:
        return 0
    return (1 if lst[0] % 2 == 0 else 0) + count_even(lst[1:])

# 782. Функция для подсчета количества отрицательных чисел в списке (рекурсия)
def count_negatives(lst):
    if not lst:
        return 0
    return (1 if lst[0] < 0 else 0) + count_negatives(lst[1:])

# 783. Функция для нахождения всех чисел в списке, которые больше среднего значения (рекурсия)
def greater_than_average(lst, avg=None):
    if not lst:
        return []
    if avg is None:
        avg = sum(lst) / len(lst)
    return ([lst[0]] if lst[0] > avg else []) + greater_than_average(lst[1:], avg)

# 784. Функция для нахождения суммы чисел, которые больше X в списке (рекурсия)
def sum_greater_than_x(lst, x):
    if not lst:
        return 0
    return (lst[0] if lst[0] > x else 0) + sum_greater_than_x(lst[1:], x)

# 785. Функция для нахождения длины строки (рекурсия)
def string_length(s):
    if s == "":
        return 0
    return 1 + string_length(s[1:])

# 786. Функция для подсчета количества четных чисел в диапазоне от 1 до N (рекурсия)
def count_evens_in_range(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return 1 + count_evens_in_range(n - 1)
    return count_evens_in_range(n - 1)

# 787. Функция для вычисления суммы чисел, которые находятся в пределах заданного диапазона (рекурсия)
def sum_in_range(lst, low, high):
    if not lst:
        return 0
    return (lst[0] if low <= lst[0] <= high else 0) + sum_in_range(lst[1:], low, high)

# 788. Функция для нахождения произведения чисел, которые меньше X в списке (рекурсия)
def product_less_than_x(lst, x):
    if not lst:
        return 1
    return (lst[0] if lst[0] < x else 1) * product_less_than_x(lst[1:], x)

# 789. Функция для нахождения суммы всех чисел в строке, которые можно преобразовать в числа (рекурсия)
def sum_of_numbers_in_string(s):
    if s == "":
        return 0
    current_num = ""
    if s[0].isdigit():
        current_num += s[0]
    elif current_num:
        return int(current_num) + sum_of_numbers_in_string(s[1:])
    return sum_of_numbers_in_string(s[1:])

# 790. Функция для нахождения всех четных чисел в строке, которые можно преобразовать в числа (рекурсия)
def even_numbers_in_string(s):
    if s == "":
        return []
    current_num = ""
    if s[0].isdigit():
        current_num += s[0]
    elif current_num:
        num = int(current_num)
        if num % 2 == 0:
            return [num] + even_numbers_in_string(s[1:])
        return even_numbers_in_string(s[1:])
    return even_numbers_in_string(s[1:])



# 792. Функция для добавления элемента в кольцевой массив с ограничением размера
def append_to_ring(arr, element, max_size=10):
    if len(arr) >= max_size:
        arr.pop(0)  # Удаляем первый элемент, если массив переполнен
    arr.append(element)
    if len(arr) > max_size:
        arr = arr[1:]  # Оставляем только max_size элементов
    return arr



# 794. Функция для нахождения индекса элемента в кольцевом массиве с возможностью обрабатывать отсутствующие элементы
def find_in_ring(arr, element):
    if not arr:
        return None
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return None




# 797. Функция для добавления нескольких элементов в кольцевой массив
def append_multiple_to_ring(arr, elements, max_size=10):
    for element in elements:
        arr = append_to_ring(arr, element, max_size)
    return arr

# 798. Функция для нахождения всех индексов в кольцевом массиве, где встречается заданный элемент
def find_all_in_ring(arr, element):
    if not arr:
        return []
    indices = []
    n = len(arr)
    for i in range(n):
        if arr[i] == element:
            indices.append(i)
    return indices

# 799. Функция для циклического сдвига элементов в кольцевом массиве с шагом, который может быть отрицательным
def rotate_with_negativity(arr, steps):
    if not arr:
        return arr
    n = len(arr)
    steps = steps % n  # Оставляем шаг в пределах длины массива
    if steps == 0:
        return arr
    if steps < 0:
        rotated = arr[steps:] + arr[:steps]
    else:
        rotated = arr[-steps:] + arr[:-steps]
    return rotated

# 801. Функция для увеличения всех элементов кольцевого массива на заданное число
def increase_ring_elements(arr, value):
    if not arr:
        return arr
    return [x + value for x in arr]

# 802. Функция для уменьшения всех элементов кольцевого массива на заданное число
def decrease_ring_elements(arr, value):
    if not arr:
        return arr
    return [x - value for x in arr]

# 803. Функция для умножения всех элементов кольцевого массива на заданное число
def multiply_ring_elements(arr, value):
    if not arr:
        return arr
    return [x * value for x in arr]

# 804. Функция для нахождения суммы элементов в кольцевом массиве
def sum_ring(arr):
    if not arr:
        return 0
    return sum(arr)

# 805. Функция для нахождения среднего значения элементов кольцевого массива
def average_ring(arr):
    if not arr:
        return None
    return sum(arr) / len(arr)

# 806. Функция для нахождения максимального элемента кольцевого массива
def max_ring(arr):
    if not arr:
        return None
    return max(arr)

# 807. Функция для нахождения минимального элемента кольцевого массива
def min_ring(arr):
    if not arr:
        return None
    return min(arr)

# 808. Функция для проверки, содержится ли хотя бы одно положительное число в кольцевом массиве
def has_positive_ring(arr):
    if not arr:
        return False
    for x in arr:
        if x > 0:
            return True
    return False

# 809. Функция для проверки, содержится ли хотя бы одно отрицательное число в кольцевом массиве
def has_negative_ring(arr):
    if not arr:
        return False
    for x in arr:
        if x < 0:
            return True
    return False


# 811. Функция для инвертирования элементов в кольцевом массиве, если они находятся в четных индексах
def reverse_even_index_elements(arr):
    if not arr:
        return arr
    n = len(arr)
    result = arr[:]
    for i in range(0, n, 2):
        result[i] = arr[n - 1 - i]
    return result

# 812. Функция для нахождения четных чисел в кольцевом массиве
def find_even_ring(arr):
    if not arr:
        return []
    return [x for x in arr if x % 2 == 0]

# 813. Функция для нахождения нечетных чисел в кольцевом массиве
def find_odd_ring(arr):
    if not arr:
        return []
    return [x for x in arr if x % 2 != 0]

# 814. Функция для подсчета количества четных чисел в кольцевом массиве
def count_even_ring(arr):
    if not arr:
        return 0
    return sum(1 for x in arr if x % 2 == 0)

# 815. Функция для подсчета количества нечетных чисел в кольцевом массиве
def count_odd_ring(arr):
    if not arr:
        return 0
    return sum(1 for x in arr if x % 2 != 0)

# 816. Функция для добавления элемента в кольцевой массив только если он еще не существует
def append_unique_ring(arr, element):
    if element not in arr:
        arr.append(element)
    return arr

# 817. Функция для нахождения всех элементов кольцевого массива, которые делятся на X
def find_divisible_ring(arr, x):
    if not arr:
        return []
    return [el for el in arr if el % x == 0]

# 818. Функция для удаления всех элементов, которые меньше заданного числа
def remove_less_than_ring(arr, threshold):
    if not arr:
        return arr
    return [x for x in arr if x >= threshold]


# 820. Функция для очистки кольцевого массива от элементов, больших заданного числа
def remove_greater_than_ring(arr, threshold):
    if not arr:
        return arr
    return [x for x in arr if x <= threshold]


# 821. Функция для преобразования строки в список символов, с проверкой на пустоту
def string_to_list(s):
    if s == "":
        return []
    return list(s)

# 822. Функция для объединения двух списков без повторений
def merge_unique_lists(list1, list2):
    return list(set(list1 + list2))

# 823. Функция для создания множества из строк, игнорируя регистр
def set_from_strings_ignore_case(strings):
    return {s.lower() for s in strings}

# 824. Функция для подсчета количества вхождений каждого символа в строку
def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# 825. Функция для проверки, является ли строка палиндромом
def is_palindrome(s):
    cleaned = ''.join(e for e in s if e.isalnum()).lower()
    return cleaned == cleaned[::-1]

# 826. Функция для вычисления факториала числа с использованием рекурсии
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# 827. Функция для подсчета числа всех вхождений слова в тексте
def count_word_occurrences(text, word):
    words = text.split()
    count = 0
    for w in words:
        if w == word:
            count += 1
    return count

# 828. Функция для извлечения всех чисел из строки
def extract_numbers_from_string(s):
    numbers = []
    temp = ""
    for char in s:
        if char.isdigit():
            temp += char
        elif temp:
            numbers.append(int(temp))
            temp = ""
    if temp:
        numbers.append(int(temp))
    return numbers

# 829. Функция для фильтрации строк, которые содержат только цифры
def filter_numeric_strings(strings):
    return [s for s in strings if s.isdigit()]

# 830. Функция для поиска ближайшего к числу в списке
def closest_number(arr, num):
    if not arr:
        return None
    closest = arr[0]
    for x in arr:
        if abs(x - num) < abs(closest - num):
            closest = x
    return closest

# 831. Функция для сортировки списка словарей по заданному ключу
def sort_dicts_by_key(lst, key):
    return sorted(lst, key=lambda x: x.get(key, None))

# 832. Функция для поиска наибольшего общего делителя двух чисел
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 833. Функция для вычисления среднего арифметического элементов списка с защитой от деления на 0
def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

# 834. Функция для преобразования строки в формат "заглавными и маленькими буквами"
def alternate_case(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

# 835. Функция для подсчета, сколько раз встречается каждый элемент в списке
def count_elements(arr):
    counts = {}
    for el in arr:
        counts[el] = counts.get(el, 0) + 1
    return counts

# 836. Функция для преобразования списка в строку через разделитель
def list_to_string(lst, separator=","):
    return separator.join(map(str, lst))

# 837. Функция для извлечения уникальных элементов из списка с сохранением порядка
def unique_elements(arr):
    seen = set()
    result = []
    for el in arr:
        if el not in seen:
            result.append(el)
            seen.add(el)
    return result

# 838. Функция для поиска строки в тексте с учетом возможных пробелов
def find_word_in_text(text, word):
    index = text.find(word)
    if index != -1:
        return f"Word found at index {index}"
    return "Word not found"

# 839. Функция для определения, является ли строка числом (целым или с плавающей точкой)
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# 840. Функция для объединения двух словарей, при этом значения по одинаковым ключам складываются
def merge_dicts(dict1, dict2):
    result = dict1.copy()  # Начинаем с первого словаря
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

# 841. Функция для извлечения элементов с четными индексами из списка
def even_index_elements(arr):
    return [arr[i] for i in range(0, len(arr), 2)]

# 842. Функция для инвертирования словаря (меняем местами ключи и значения)
def invert_dict(d):
    return {v: k for k, v in d.items()}

# 843. Функция для слияния двух отсортированных списков в один отсортированный
def merge_sorted_lists(list1, list2):
    merged = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

# 844. Функция для замены каждого второго символа в строке на звездочку
def replace_second_char(s):
    return ''.join([c if i % 2 == 0 else '*' for i, c in enumerate(s)])

# 845. Функция для получения уникальных чисел из списка с их суммой
def unique_numbers_and_sum(lst):
    unique_numbers = set(lst)
    total = sum(unique_numbers)
    return unique_numbers, total

# 846. Функция для проверки, является ли строка правильным email
def is_valid_email(email):
    if "@" not in email or "." not in email:
        return False
    username, domain = email.split("@", 1)
    if not username or not domain:
        return False
    return True

# 847. Функция для подсчета всех слов в строке с учётом знаков препинания
def count_words_in_string(s):
    words = s.split()
    return len(words)

# 848. Функция для нахождения максимального числа в списке с проверкой на пустоту
def max_in_list(lst):
    if not lst:
        return None
    return max(lst)

# 849. Функция для преобразования строки в список чисел, разделенных запятой
def string_to_numbers(s):
    return [int(x) for x in s.split(",") if x.strip().isdigit()]

# 850. Функция для вычисления степени числа с обработкой возможных ошибок
def power(base, exponent):
    try:
        return base ** exponent
    except TypeError:
        return "Invalid input"

# 851. Функция для генерации списка всех чисел от 1 до N, которые делятся на X
def divisible_by_x(n, x):
    return [i for i in range(1, n+1) if i % x == 0]

# 852. Функция для вычисления длины строки, игнорируя пробелы
def length_without_spaces(s):
    return len(s.replace(" ", ""))

# 853. Функция для проверки, является ли строка числом в десятичной системе
def is_decimal(s):
    try:
        float(s)
        return '.' in s
    except ValueError:
        return False

# 854. Функция для изменения регистра в строках, включая те, которые начинаются с пробела
def change_case_and_strip(s):
    return s.strip().upper() if s.startswith(" ") else s.lower()


# 855. Функция для нахождения индекса первого отрицательного числа в списке
def find_first_negative(arr):
    if not arr:
        return None
    for i in range(len(arr)):
        if arr[i] < 0:
            return i
    return None

# 856. Функция для удаления всех повторяющихся элементов из списка, сохраняя порядок
def remove_duplicates(arr):
    if not arr:
        return arr
    seen = set()
    result = []
    for el in arr:
        if el not in seen:
            result.append(el)
            seen.add(el)
    return result

# 857. Функция для проверки, является ли строка числом с плавающей точкой
def is_float(s):
    try:
        float(s)
        return "." in s
    except ValueError:
        return False

# 858. Функция для извлечения всех слов из строки, содержащих цифры
def extract_words_with_numbers(s):
    if not s:
        return []
    words = s.split()
    result = []
    for word in words:
        if any(char.isdigit() for char in word):
            result.append(word)
    return result

# 859. Функция для нахождения наименьшего общего кратного двух чисел
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1

# 860. Функция для объединения двух списков с уникальными значениями
def merge_unique_lists(arr1, arr2):
    result = arr1.copy()
    for el in arr2:
        if el not in result:
            result.append(el)
    return result

# 861. Функция для возврата индекса элемента в списке, если он существует, или None
def find_index_of_element(arr, element):
    if not arr:
        return None
    for i, el in enumerate(arr):
        if el == element:
            return i
    return None

# 862. Функция для подсчета всех слов в строке с учетом разделителей
def count_words_in_string_with_delimiters(s, delimiters=" "):
    if not s:
        return 0
    for delimiter in delimiters:
        s = s.replace(delimiter, " ")
    return len(s.split())

# 863. Функция для поиска наибольшего и наименьшего элементов в списке
def find_max_min(arr):
    if not arr:
        return None, None
    max_val = min_val = arr[0]
    for el in arr:
        if el > max_val:
            max_val = el
        if el < min_val:
            min_val = el
    return max_val, min_val

# 864. Функция для нахождения всех чисел больше среднего в списке
def greater_than_average(arr):
    if not arr:
        return []
    avg = sum(arr) / len(arr)
    return [x for x in arr if x > avg]

# 865. Функция для объединения словаря и списка кортежей в новый словарь
def merge_dict_and_tuple(lst, d):
    if not lst:
        return d
    for key, value in lst:
        d[key] = value
    return d

# 866. Функция для вычисления суммы всех чисел в строке
def sum_numbers_in_string(s):
    if not s:
        return 0
    total = 0
    temp = ""
    for char in s:
        if char.isdigit():
            temp += char
        elif temp:
            total += int(temp)
            temp = ""
    if temp:
        total += int(temp)
    return total

# 867. Функция для нахождения числа, которое не встречается в двух списках
def find_missing_number(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    missing = set1 - set2
    if missing:
        return missing.pop()
    return None

# 868. Функция для слияния двух строк с их чередующимися символами
def alternate_merge(s1, s2):
    if not s1:
        return s2
    if not s2:
        return s1
    result = []
    for c1, c2 in zip(s1, s2):
        result.append(c1)
        result.append(c2)
    result.extend(s1[len(s2):])
    result.extend(s2[len(s1):])
    return ''.join(result)

# 869. Функция для проверки, все ли элементы в списке больше заданного числа
def are_all_greater_than(arr, number):
    if not arr:
        return False
    return all(x > number for x in arr)

# 870. Функция для поиска и замены первого вхождения подстроки в строке
def replace_first_occurrence(s, old, new):
    if old not in s:
        return s
    index = s.find(old)
    return s[:index] + new + s[index+len(old):]

# 871. Функция для возврата наибольшего общего делителя массива
def gcd_of_list(arr):
    if not arr:
        return None
    result = arr[0]
    for num in arr[1:]:
        result = gcd(result, num)
    return result

# 872. Функция для получения уникальных элементов из списка, исключая те, которые повторяются
def get_unique_elements(arr):
    if not arr:
        return []
    count = {}
    for el in arr:
        count[el] = count.get(el, 0) + 1
    return [key for key, value in count.items() if value == 1]

# 873. Функция для нахождения минимального четного числа в списке
def min_even_number(arr):
    if not arr:
        return None
    even_numbers = [x for x in arr if x % 2 == 0]
    if even_numbers:
        return min(even_numbers)
    return None

# 874. Функция для преобразования числа в строку с ведущими нулями
def number_to_string_with_leading_zeros(n, width):
    return str(n).zfill(width)



# 876. Функция для преобразования списка чисел в строку с разделением на запятую
def list_to_comma_separated_string(arr):
    if not arr:
        return ""
    return ", ".join(map(str, arr))

# 877. Функция для проверки, является ли строка правильным числом (целым или с плавающей точкой)
def is_valid_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# 878. Функция для подсчета гласных букв в строке
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# 879. Функция для вычисления произведения всех чисел в строке
def product_of_numbers_in_string(s):
    if not s:
        return 1
    total = 1
    temp = ""
    for char in s:
        if char.isdigit():
            temp += char
        elif temp:
            total *= int(temp)
            temp = ""
    if temp:
        total *= int(temp)
    return total

# 880. Функция для поиска всех строк в списке, содержащих хотя бы одну цифру
def find_strings_with_digits(arr):
    return [s for s in arr if any(char.isdigit() for char in s)]

# 881. Функция для вычисления числа цифр в строке
def count_digits_in_string(s):
    return sum(1 for char in s if char.isdigit())

# 882. Функция для получения каждого второго элемента в строке
def get_every_second_char(s):
    return s[::2]

# 883. Функция для фильтрации строк, содержащих хотя бы одну заглавную букву
def filter_strings_with_uppercase(arr):
    return [s for s in arr if any(char.isupper() for char in s)]

# 884. Функция для поиска всех чисел в строке и их суммирования
def sum_numbers_in_string_v2(s):
    numbers = extract_numbers_from_string(s)
    return sum(numbers)

# 885. Функция для подсчета повторений каждого символа в строке, кроме пробела
def count_non_space_characters(s):
    count = {}
    for char in s:
        if char != " ":
            count[char] = count.get(char, 0) + 1
    return count



# 886. Функция для поиска строки с максимальной длиной в списке
def find_longest_string(arr):
    if not arr:
        return None
    max_length = len(arr[0])
    longest_string = arr[0]
    for string in arr[1:]:
        if len(string) > max_length:
            max_length = len(string)
            longest_string = string
    return longest_string

# 887. Функция для нахождения индекса первого четного числа в списке
def find_first_even(arr):
    if not arr:
        return None
    for i, num in enumerate(arr):
        if num % 2 == 0:
            return i
    return None

# 888. Функция для вычисления суммы всех чисел в строке
def sum_numbers_in_string_v3(s):
    total = 0
    temp = ""
    for char in s:
        if char.isdigit():
            temp += char
        elif temp:
            total += int(temp)
            temp = ""
    if temp:
        total += int(temp)
    if total == 0:
        return None
    return total

# 889. Функция для преобразования строки в список чисел (каждое число отделено пробелом)
def string_to_number_list(s):
    if not s:
        return []
    num_list = s.split()
    try:
        return [int(num) for num in num_list]
    except ValueError:
        return None

# 890. Функция для поиска максимального и минимального элемента в списке
def find_max_min(arr):
    if not arr:
        return None, None
    max_val = arr[0]
    min_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val

# 891. Функция для замены всех пробелов на подчеркивания в строке
def replace_spaces_with_underscores(s):
    if not s:
        return None
    result = ""
    for char in s:
        if char == " ":
            result += "_"
        else:
            result += char
    return result

# 892. Функция для удаления дубликатов из списка, не изменяя порядок
def remove_duplicates_maintain_order(arr):
    if not arr:
        return []
    seen = set()
    result = []
    for el in arr:
        if el not in seen:
            result.append(el)
            seen.add(el)
    return result

# 893. Функция для поиска первого числа в списке, которое делится на заданное число
def find_first_multiple(arr, divisor):
    if not arr or divisor == 0:
        return None
    for num in arr:
        if num % divisor == 0:
            return num
    return None

# 894. Функция для проверки, является ли строка полиндромом, игнорируя пробелы и регистр
def is_palindrome_v2(s):
    if not s:
        return False
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# 895. Функция для получения всех четных чисел из списка
def get_even_numbers(arr):
    if not arr:
        return []
    even_numbers = []
    for num in arr:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# 896. Функция для проверки, является ли строка числом (целым или с плавающей точкой)
def is_number_v2(s):
    if not s:
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False

# 897. Функция для подсчета всех повторяющихся элементов в списке
def count_repeating_elements(arr):
    if not arr:
        return {}
    counts = {}
    for el in arr:
        counts[el] = counts.get(el, 0) + 1
    return {key: value for key, value in counts.items() if value > 1}

# 898. Функция для извлечения уникальных слов из строки
def extract_unique_words(s):
    if not s:
        return []
    words = s.split()
    unique_words = set(words)
    return list(unique_words)

# 899. Функция для нахождения наибольшего простого числа в списке
def find_largest_prime(arr):
    if not arr:
        return None
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [x for x in arr if is_prime(x)]
    if primes:
        return max(primes)
    return None

# 900. Функция для извлечения всех цифр из строки
def extract_digits(s):
    if not s:
        return []
    digits = [int(c) for c in s if c.isdigit()]
    return digits

# 901. Функция для поиска всех слов в строке, длина которых больше 3 символов
def find_long_words(s):
    if not s:
        return []
    words = s.split()
    long_words = [word for word in words if len(word) > 3]
    return long_words

# 902. Функция для получения всех чисел в строке, разделенных запятыми
def get_numbers_from_string(s):
    if not s:
        return []
    numbers = []
    temp = ""
    for char in s:
        if char.isdigit():
            temp += char
        elif temp:
            numbers.append(int(temp))
            temp = ""
    if temp:
        numbers.append(int(temp))
    return numbers

# 903. Функция для нахождения всех чисел в списке, которые больше заданного числа
def find_numbers_greater_than(arr, n):
    if not arr:
        return []
    greater_numbers = []
    for num in arr:
        if num > n:
            greater_numbers.append(num)
    return greater_numbers

# 904. Функция для объединения списка строк в одну строку с разделителями
def join_strings_with_separator(arr, separator):
    if not arr:
        return ""
    result = arr[0]
    for string in arr[1:]:
        result += separator + string
    return result

# 905. Функция для вычисления суммы всех четных чисел в списке
def sum_even_numbers(arr):
    if not arr:
        return 0
    total = 0
    for num in arr:
        if num % 2 == 0:
            total += num
    return total

# 906. Функция для нахождения первой строки, содержащей заданное слово
def find_string_with_word(arr, word):
    if not arr or not word:
        return None
    for s in arr:
        if word in s:
            return s
    return None

# 907. Функция для нахождения наименьшего нечетного числа в списке
def find_smallest_odd(arr):
    if not arr:
        return None
    odd_numbers = [x for x in arr if x % 2 != 0]
    if odd_numbers:
        return min(odd_numbers)
    return None


# 908. Функция для замены всех вхождений подстроки на другую подстроку
def replace_substring(s, old_sub, new_sub):
    if not s or not old_sub:
        return s
    count = 0
    result = ""
    i = 0
    while i < len(s):
        if s[i:i+len(old_sub)] == old_sub:
            result += new_sub
            i += len(old_sub)
            count += 1
        else:
            result += s[i]
            i += 1
    if count == 0:
        return None
    return result


# 909. Функция для нахождения первого элемента списка, который делится на 3 и на 5
def find_divisible_by_3_and_5(arr):
    if not arr:
        return None
    for num in arr:
        if num % 3 == 0 and num % 5 == 0:
            return num
    return None

# 910. Функция для вычисления среднего арифметического элементов списка
def calculate_average(arr):
    if not arr:
        return None
    total = sum(arr)
    count = len(arr)
    return total / count

# 911. Функция для объединения двух списков в один и удаления повторяющихся элементов
def combine_and_unique(arr1, arr2):
    if not arr1 and not arr2:
        return []
    combined = arr1 + arr2
    unique = []
    for el in combined:
        if el not in unique:
            unique.append(el)
    return unique

