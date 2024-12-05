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
def max_min_difference_1(lst):
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


# 65. Функция для нахождения наибольшего нечетного числа в списке
def max_odd_number(lst):
    odd_numbers = [x for x in lst if x % 2 != 0]
    if not odd_numbers:
        print("No odd numbers found.")
        return None
    return max(odd_numbers)


# 66. Функция для подсчета количества заглавных букв в строке
def count_uppercase(s):
    count = sum(1 for char in s if char.isupper())
    if count == 0:
        print("No uppercase letters found.")
    return count


# 67. Функция для проверки, является ли строка числом Фибоначчи
def is_fibonacci_number(n):
    if n < 0:
        print("Negative numbers cannot be Fibonacci numbers.")
        return False
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n


# 68. Функция для проверки, является ли список симметричным
def is_symmetric(lst):
    if lst == lst[::-1]:
        return True
    else:
        print("List is not symmetric.")
        return False


# 69. Функция для нахождения суммы всех чисел в строке, игнорируя буквы
def sum_numbers_in_string(s):
    numbers = [int(x) for x in s.split() if x.isdigit()]
    return sum(numbers)


# 70. Функция для нахождения разницы между максимальным и минимальным нечётными числами в списке
def odd_max_min_difference(lst):
    odd_numbers = [x for x in lst if x % 2 != 0]
    if not odd_numbers:
        print("No odd numbers found.")
        return None
    return max(odd_numbers) - min(odd_numbers)


# 71. Функция для подсчета количества цифр в строке
def count_digits(s):
    count = sum(1 for char in s if char.isdigit())
    return count


# 72. Функция для проверки, является ли строка строкой с четным количеством символов
def is_even_length(s):
    return len(s) % 2 == 0


# 73. Функция для нахождения суммы всех чисел в списке, пропуская числа, кратные 4
def sum_exclude_multiples_of_four(lst):
    return sum(x for x in lst if x % 4 != 0)


# 74. Функция для нахождения минимального числа, которое не встречается в списке
def missing_min_number(lst):
    i = 0
    while i in lst:
        i += 1
    return i


# 75. Функция для нахождения чисел, которые встречаются в обоих списках
def common_numbers(lst1, lst2):
    return [x for x in lst1 if x in lst2]


# 76. Функция для нахождения первой строки в списке, содержащей хотя бы одну цифру
def first_string_with_digit(lst):
    for string in lst:
        if any(char.isdigit() for char in string):
            return string
    print("No string with digits found.")
    return None


# 77. Функция для подсчета количества слов, начинающихся с определенной буквы
def count_words_starting_with(lst, char):
    return sum(1 for word in lst if word.startswith(char))


# 78. Функция для нахождения количества чисел в списке, которые больше заданного
def count_greater_than(lst, n):
    return sum(1 for x in lst if x > n)


# 79. Функция для нахождения максимальной суммы подсписка
def max_sublist_sum(lst):
    if not lst:
        print("List is empty!")
        return None
    max_sum = current_sum = lst[0]
    for num in lst[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


# 80. Функция для вычисления наибольшего произведения двух чисел в списке
def max_pairwise_product(lst):
    if len(lst) < 2:
        print("Need at least two elements!")
        return None
    lst.sort()
    return lst[-1] * lst[-2]


# 81. Функция для проверки, является ли строка палиндромом, игнорируя пробелы и знаки препинания
def is_palindrome_1(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]


# 82. Функция для нахождения наибольшего делителя числа, меньшего заданного
def largest_divisor_less_than(n):
    if n <= 1:
        print(f"{n} doesn't have any divisors greater than 1.")
        return None
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return i
    return None


# 83. Функция для нахождения всех чисел в списке, которые не являются простыми
def non_prime_numbers(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [x for x in lst if not is_prime(x)]


# 84. Функция для нахождения наибольшего элемента в строке, если строка состоит из цифр
def max_digit_in_string(s):
    if not s.isdigit():
        print("The string doesn't contain only digits.")
        return None
    return max(map(int, s))


# 85. Функция для нахождения наибольшего числа, которое является квадратом целого числа
def largest_square(lst):
    squares = [x for x in lst if int(x ** 0.5) ** 2 == x]
    if squares:
        return max(squares)
    print("No perfect squares found.")
    return None


# 86. Функция для нахождения всех чисел, которые можно записать как сумму двух квадратов
def sum_of_two_squares(lst):
    def is_sum_of_squares(n):
        for i in range(1, int(n ** 0.5) + 1):
            if (n - i ** 2) ** 0.5 == int((n - i ** 2) ** 0.5):
                return True
        return False

    return [x for x in lst if is_sum_of_squares(x)]


# 87. Функция для нахождения суммы чисел в строке, игнорируя все символы, кроме цифр
def sum_of_digits_in_string(s):
    return sum(int(c) for c in s if c.isdigit())


# 88. Функция для нахождения всех элементов, которые меньше среднего значения списка
def elements_less_than_mean(lst):
    if not lst:
        print("List is empty!")
        return []
    mean = sum(lst) / len(lst)
    return [x for x in lst if x < mean]


# 89. Функция для нахождения всех элементов в строке, которые являются числами
def extract_numbers_from_string(s):
    return [int(x) for x in s.split() if x.isdigit()]


# 90. Функция для вычисления разности между наибольшим и наименьшим числом в списке
def max_min_difference(lst):
    if not lst:
        print("List is empty!")
        return None
    return max(lst) - min(lst)


# 91. Функция для нахождения первого числа, которое делится на 2 и на 5 в списке
def first_divisible_by_2_and_5(lst):
    for x in lst:
        if x % 2 == 0 and x % 5 == 0:
            return x
    print("No number divisible by both 2 and 5 found.")
    return None


# 92. Функция для проверки, является ли строка числом, и если да, то вывести его квадрат
def square_if_number(s):
    try:
        number = float(s)
        return number ** 2
    except ValueError:
        print(f"'{s}' is not a valid number.")
        return None


# 93. Функция для подсчета количества чисел в списке, которые не являются простыми
def count_non_prime(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(1 for x in lst if not is_prime(x))


# 94. Функция для нахождения всех элементов в списке, которые являются палиндромами
def palindromic_elements(lst):
    return [x for x in lst if str(x) == str(x)[::-1]]


# 95. Функция для нахождения наибольшего числа, которое является степенью двойки
def largest_power_of_two(lst):
    powers_of_two = [x for x in lst if (x & (x - 1)) == 0 and x > 0]
    if powers_of_two:
        return max(powers_of_two)
    print("No powers of two found.")
    return None


# 96. Функция для нахождения всех чисел, которые являются кратными 6
def multiples_of_six(lst):
    return [x for x in lst if x % 6 == 0]


# 97. Функция для нахождения уникальных элементов в списке, используя множество
def unique_elements(lst):
    unique = set()
    for item in lst:
        if item not in unique:
            unique.add(item)
        else:
            print(f"Duplicate found: {item}")
    return sorted(list(unique))


# 98. Функция для подсчёта количества вхождений каждого элемента в список с использованием словаря
def count_occurrences_1(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    if not count_dict:
        print("No elements found.")
    return count_dict


# 99. Функция для нахождения пересечения двух списков с использованием множеств
def intersection_of_lists(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    intersection = set1 & set2
    if not intersection:
        print("No common elements found.")
    return list(intersection)


# 100. Функция для нахождения всех чисел, которые делятся на любое число из второго списка
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


# 101. Функция для проверки, является ли строка анаграммой другой строки
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


# 102. Функция для нахождения пересечения двух множеств
def intersection_of_sets(set1, set2):
    intersection = set1.intersection(set2)
    if not intersection:
        print("The sets have no common elements.")
    return intersection


# 103. Функция для удаления дубликатов из списка кортежей по первому элементу
def remove_duplicate_tuples(lst):
    seen = set()
    result = []
    for item in lst:
        if item[0] not in seen:
            seen.add(item[0])
            result.append(item)
    return result


# 104. Функция для подсчёта элементов в строках списка, возвращая словарь с длинами строк
def count_string_lengths(lst):
    length_dict = {}
    for s in lst:
        length_dict[s] = len(s)
    return length_dict


# 105. Функция для нахождения числа, которое встречается больше всех раз в словаре (ключи - элементы, значения - количество)
def most_frequent_in_dict(d):
    if not d:
        print("Dictionary is empty.")
        return None
    max_key = max(d, key=d.get)
    return max_key, d[max_key]


# 106. Функция для объединения двух словарей (если есть одинаковые ключи, их значения суммируются)
def merge_dicts(d1, d2):
    merged = d1.copy()
    for key, value in d2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged


# 107. Функция для подсчёта чётных и нечётных чисел в списке с использованием словаря
def count_even_odd(lst):
    count = {"even": 0, "odd": 0}
    for num in lst:
        if num % 2 == 0:
            count["even"] += 1
        else:
            count["odd"] += 1
    return count


# 108. Функция для нахождения минимального ключа в словаре с числовыми значениями
def min_key_in_dict(d):
    if not d:
        print("Dictionary is empty.")
        return None
    return min(d, key=d.get)


# 109. Функция для создания словаря из списка, где элементы списка становятся значениями, а их индексы — ключами
def list_to_dict(lst):
    result = {}
    for index, value in enumerate(lst):
        result[index] = value
    return result


# 110. Функция для проверки, является ли строка числом, и если да — вернуть её квадрат
def check_and_square(s):
    try:
        num = float(s)
        return num ** 2
    except ValueError:
        print(f"'{s}' is not a valid number.")
        return None


# 111. Функция для объединения двух кортежей, убирая повторяющиеся элементы
def merge_tuples(t1, t2):
    return tuple(sorted(set(t1 + t2)))


# 112. Функция для нахождения всех уникальных чисел в списке (с использованием множества)
def unique_numbers(lst):
    unique = set()
    for num in lst:
        unique.add(num)
    return sorted(list(unique))


# 113. Функция для создания словаря, где ключами будут уникальные элементы списка, а значениями — количество их повторений
def create_frequency_dict(lst):
    frequency_dict = {}
    for item in lst:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict


# 114. Функция для нахождения элементов, которые присутствуют в одном списке, но отсутствуют в другом
def difference_of_lists(lst1, lst2):
    result = []
    for item in lst1:
        if item not in lst2:
            result.append(item)
    for item in lst2:
        if item not in lst1:
            result.append(item)
    return result


# 115. Функция для нахождения всех элементов списка, которые встречаются в другой коллекции
def find_in_collection(lst, collection):
    result = []
    for item in lst:
        if item in collection:
            result.append(item)
    if not result:
        print("No elements found in the collection.")
    return result


# 116. Функция для нахождения суммы всех чисел в списке, которые встречаются более одного раза
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


# 117. Функция для нахождения элементов, которые присутствуют в одном списке и не встречаются в другом
def unique_in_first(lst1, lst2):
    unique_elements = []
    for item in lst1:
        if item not in lst2:
            unique_elements.append(item)
    if not unique_elements:
        print("No unique elements found in the first list.")
    return unique_elements


# 118. Функция для нахождения минимального общего кратного двух чисел
def lcm_1(a, b):
    if a == 0 or b == 0:
        print("LCM is undefined for 0.")
        return None

    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return abs(a * b) // gcd(a, b)


# 119. Функция для получения всех элементов из словаря, чьи значения больше заданного порога
def filter_dict_by_value(d, threshold):
    result = {}
    for key, value in d.items():
        if value > threshold:
            result[key] = value
    if not result:
        print("No elements above the threshold.")
    return result


# 120. Функция для переворота словаря, меняя местами ключи и значения
def reverse_dict(d):
    reversed_dict = {}
    for key, value in d.items():
        if value in reversed_dict:
            print(f"Duplicate value {value} found, skipping.")
        else:
            reversed_dict[value] = key
    return reversed_dict


# 121. Функция для нахождения всех чисел, которые являются кратными числам из другого списка
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


# 122. Функция для подсчёта частоты вхождения каждого символа в строке, игнорируя регистр
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


# 123. Функция для подсчёта всех различных элементов в списке, с учётом их частоты
def count_unique_with_frequency(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency


# 124. Функция для подсчёта, сколько раз каждый символ в строке встречается подряд
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


# 125. Функция для нахождения всех элементов в множестве, которые присутствуют в словаре в качестве ключей
def find_keys_in_set(s, d):
    result = []
    for item in s:
        if item in d:
            result.append(item)
    if not result:
        print("No elements from the set found in the dictionary keys.")
    return sorted(result)


# 126. Функция для нахождения всех чисел в списке, которые являются простыми
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


# 127. Функция для разделения строки на два списка: один с цифрами, второй с остальными символами
def split_digits_and_others(s):
    digits = []
    others = []
    for char in s:
        if char.isdigit():
            digits.append(char)
        else:
            others.append(char)
    return digits, others


# 128. Функция для получения кортежа с минимальным и максимальным элементами списка
def min_max_tuple(lst):
    if not lst:
        print("List is empty.")
        return None
    return min(lst), max(lst)


# 129. Функция для поиска элементов, которые присутствуют в двух словарях, но имеют разные значения
def find_common_keys_with_different_values(d1, d2):
    common_keys = set(d1.keys()) & set(d2.keys())
    result = []
    for key in common_keys:
        if d1[key] != d2[key]:
            result.append(key)
    if not result:
        print("No keys with different values found.")
    return result


# 130. Функция для преобразования строки в список чисел, разделённых пробелами, если в строке присутствуют только числа
def string_to_numbers(s):
    try:
        return [int(x) for x in s.split()]
    except ValueError:
        print("String contains non-numeric values.")
        return []


# 131. Функция для нахождения чисел в строке, которые могут быть переведены в степень двойки
def find_powers_of_two_in_string(s):
    numbers = []
    for word in s.split():
        try:
            num = int(word)
            if (num & (num - 1)) == 0 and num > 0:
                numbers.append(num)
        except ValueError:
            continue
    return numbers


# 132. Функция для нахождения слов, которые являются палиндромами
def find_palindromes(lst):
    palindromes = []
    for word in lst:
        if word == word[::-1]:
            palindromes.append(word)
    return palindromes


# 133. Функция для объединения двух списков с проверкой на дубликаты
def merge_lists_no_duplicates(lst1, lst2):
    result = lst1.copy()
    for item in lst2:
        if item not in result:
            result.append(item)
        else:
            print(f"Duplicate item found: {item}")
    return result


# 134. Функция для нахождения всех чисел, которые делятся на 2, но не делятся на 3
def divisible_by_2_not_3(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 != 0:
            result.append(num)
    if not result:
        print("No numbers divisible by 2 but not by 3 found.")
    return result


# 135. Функция для нахождения всех чисел в строке, которые являются чётными
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


# 136. Функция для нахождения всех чисел, которые не являются простыми
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


# 137. Функция для нахождения всех уникальных символов в строке, игнорируя пробелы
def unique_chars_ignore_spaces(s):
    unique_chars = {}
    for char in s:
        if char != ' ':
            if char not in unique_chars:
                unique_chars[char] = 1
            else:
                unique_chars[char] += 1
    return list(unique_chars.keys())


# 138. Функция для подсчёта слов в строке, игнорируя знаки препинания
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


# 139. Функция для нахождения всех чисел, которые являются квадратами целых чисел
def find_squares(lst):
    squares = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num:
            squares.append(num)
    return squares


# 140. Функция для подсчёта количества повторений каждого слова в строке
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


# 141. Функция для поиска чисел, которые могут быть записаны как сумма двух квадратов
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


# 142. Функция для получения всех элементов списка, которые не содержат в себе цифры
def find_non_numeric_elements(lst):
    result = []
    for item in lst:
        if not any(char.isdigit() for char in item):
            result.append(item)
    return result


# 143. Функция для нахождения всех чисел, которые являются нечётными и делятся на 5
def find_odd_and_divisible_by_5(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 5 == 0:
            result.append(num)
    if not result:
        print("No odd numbers divisible by 5 found.")
    return result


# 144. Функция для подсчёта всех элементов в словаре, значения которых больше определённого порога
def count_elements_above_threshold(d, threshold):
    count = 0
    for key, value in d.items():
        if value > threshold:
            count += 1
    return count


# 145. Функция для поиска чисел, которые являются степенями числа 3
def find_powers_of_three(lst):
    powers_of_three = []
    for num in lst:
        while num % 3 == 0 and num > 0:
            num //= 3
        if num == 1:
            powers_of_three.append(num)
    return powers_of_three


# 146. Функция для получения всех чисел в строке, которые больше среднего значения
def find_numbers_greater_than_mean(s):
    nums = [int(x) for x in s.split() if x.isdigit()]
    mean = sum(nums) / len(nums) if nums else 0
    result = []
    for num in nums:
        if num > mean:
            result.append(num)
    return result


# 147. Функция для нахождения всех чисел, которые являются нечётными и не являются простыми
def find_odd_and_not_prime(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    non_prime_odd = []
    for num in lst:
        if num % 2 != 0 and not is_prime(num):
            non_prime_odd.append(num)
    return non_prime_odd


# 148. Функция для нахождения всех чисел в списке, которые являются делителями другого числа в этом же списке
def find_divisors_in_list(lst):
    divisors = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] % lst[j] == 0:
                divisors.append(lst[i])
                break
    return divisors


# 149. Функция для нахождения всех чисел, которые не являются кратными чисел из другого списка
def find_non_multiples(lst1, lst2):
    non_multiples = []
    for num in lst1:
        if all(num % divisor != 0 for divisor in lst2):
            non_multiples.append(num)
    return non_multiples


# 150. Функция для нахождения всех элементов списка, которые присутствуют в обоих списках
def find_common_elements(lst1, lst2):
    common_elements = []
    for item in lst1:
        if item in lst2:
            common_elements.append(item)
    if not common_elements:
        print("No common elements found.")
    return common_elements

# 151. Функция для нахождения числа, которое является квадратом какого-то целого числа, но не является четным
def find_odd_square(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and num % 2 != 0:
            result.append(num)
    return result


# 152. Функция для нахождения всех элементов, которые содержат хотя бы одну гласную
def find_elements_with_vowels(lst):
    vowels = 'aeiouAEIOU'
    result = []
    for item in lst:
        if any(char in vowels for char in item):
            result.append(item)
    return result


# 153. Функция для нахождения всех чисел в списке, которые не делятся на 2 и на 3
def find_not_divisible_by_2_and_3(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 3 != 0:
            result.append(num)
    if not result:
        print("No numbers found that are not divisible by 2 or 3.")
        return []
    return result


# 154. Функция для подсчёта всех уникальных букв в строке
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


# 155. Функция для поиска чисел, которые могут быть записаны как произведение двух чётных чисел
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


# 156. Функция для нахождения чисел, которые делятся на 5, но не делятся на 10
def find_multiples_of_5_not_10(lst):
    result = []
    for num in lst:
        if num % 5 == 0 and num % 10 != 0:
            result.append(num)
    if not result:
        print("No multiples of 5 that are not divisible by 10.")
    return result


# 157. Функция для нахождения всех чисел, которые являются двузначными и не делятся на 2
def find_double_digits_not_divisible_by_2(lst):
    result = []
    for num in lst:
        if 10 <= num <= 99 and num % 2 != 0:
            result.append(num)
    if not result:
        print("No double-digit numbers found that are not divisible by 2.")
    return result


# 158. Функция для нахождения чисел, которые встречаются в обеих строках
def find_common_numbers_in_strings(s1, s2):
    nums1 = {int(x) for x in s1.split() if x.isdigit()}
    nums2 = {int(x) for x in s2.split() if x.isdigit()}
    common = nums1 & nums2
    if not common:
        print("No common numbers found between the two strings.")
        return set()
    return common


# 159. Функция для нахождения всех чисел, которые делятся на 7, но не на 11
def find_divisible_by_7_not_11(lst):
    result = []
    for num in lst:
        if num % 7 == 0 and num % 11 != 0:
            result.append(num)
    if not result:
        print("No numbers found divisible by 7 but not 11.")
    return result


# 160. Функция для подсчёта, сколько раз слово встречается в строке, игнорируя регистр
def count_word_in_string(s, word):
    s = s.lower()
    word = word.lower()
    count = s.split().count(word)
    if count == 0:
        print(f"The word '{word}' was not found.")
        return 0
    return count


# 161. Функция для нахождения чисел, которые являются простыми, но не являются кратными 3
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


# 162. Функция для нахождения чисел, которые являются чётными и делятся на 4
def find_even_numbers_divisible_by_4(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 4 == 0:
            result.append(num)
    if not result:
        print("No even numbers divisible by 4 found.")
    return result


# 163. Функция для нахождения всех чисел, которые не являются степенями двойки
def find_non_powers_of_two(lst):
    result = []
    for num in lst:
        if (num & (num - 1)) != 0:
            result.append(num)
    if not result:
        print("No numbers found that are not powers of two.")
    return result


# 164. Функция для подсчёта всех чисел в строке, которые больше среднего значения всех чисел в строке
def count_numbers_greater_than_average(s):
    nums = [int(x) for x in s.split() if x.isdigit()]
    if not nums:
        print("No numbers found in the string.")
        return 0
    average = sum(nums) / len(nums)
    count = sum(1 for num in nums if num > average)
    return count


# 165. Функция для нахождения всех чисел, которые делятся на 4 или на 5, но не на 20
def find_multiples_of_4_or_5_not_20(lst):
    result = []
    for num in lst:
        if (num % 4 == 0 or num % 5 == 0) and num % 20 != 0:
            result.append(num)
    if not result:
        print("No numbers found that are divisible by 4 or 5, but not by 20.")
    return result


# 166. Функция для поиска всех чисел, которые являются точными делителями 100
def find_exact_divisors_of_100(lst):
    result = []
    for num in lst:
        if 100 % num == 0:
            result.append(num)
    if not result:
        print("No numbers found that are exact divisors of 100.")
    return result


# 167. Функция для поиска чисел, которые являются нечётными и не являются делителями 5
def find_odd_not_divisible_by_5(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 5 != 0:
            result.append(num)
    if not result:
        print("No odd numbers found that are not divisible by 5.")
    return result


# 168. Функция для нахождения всех чисел, которые являются кратными либо 2, либо 3, но не обоим
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


# 169. Функция для нахождения всех чисел, которые либо нечётные, либо делятся на 4
def find_odd_or_divisible_by_4(lst):
    result = []
    for num in lst:
        if num % 2 != 0 or num % 4 == 0:
            result.append(num)
    if not result:
        return "No odd numbers or numbers divisible by 4 found."
    return result


# 170. Функция для нахождения чисел, которые являются квадратами целых чисел, но не чётными
def find_even_squares(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and num % 2 == 0:
            result.append(num)
    if not result:
        return "No even square numbers found."
    return result


# 171. Функция для нахождения всех чисел, которые являются кратными 3 или 5, но не кратными обоим
def find_multiples_of_3_or_5_not_both(lst):
    result = []
    for num in lst:
        if (num % 3 == 0 or num % 5 == 0) and not (num % 3 == 0 and num % 5 == 0):
            result.append(num)
    if not result:
        return "No numbers found that are multiples of 3 or 5 but not both."
    return result


# 172. Функция для подсчёта всех чисел в строке, которые больше среднего значения
def count_numbers_greater_than_mean(s):
    nums = [int(x) for x in s.split() if x.isdigit()]
    if not nums:
        return "No numbers found in the string."

    mean = sum(nums) / len(nums)
    count = len([num for num in nums if num > mean])
    if count == 0:
        return "No numbers greater than the mean."
    return count


# 173. Функция для нахождения всех чисел, которые являются степенями 2
def find_powers_of_2(lst):
    result = []
    for num in lst:
        if (num & (num - 1)) == 0:
            result.append(num)
    if not result:
        return "No powers of 2 found."
    return result


# 174. Функция для нахождения всех чисел, которые являются четными и кратными 8
def find_even_and_divisible_by_8(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 8 == 0:
            result.append(num)
    if not result:
        return "No even numbers divisible by 8 found."
    return result


# 175. Функция для нахождения чисел, которые являются нечётными и делятся на 3
def find_odd_and_divisible_by_3(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 3 == 0:
            result.append(num)
    if not result:
        return "No odd numbers divisible by 3 found."
    return result


# 176. Функция для нахождения всех чисел, которые не являются чётными или кратными 7
def find_non_even_or_not_multiples_of_7(lst):
    result = []
    for num in lst:
        if num % 2 != 0 or num % 7 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are not even or not divisible by 7."
    return result

# 177. Функция для нахождения чисел, которые не делятся на 2, но делятся на 5
def find_not_divisible_by_2_but_divisible_by_5(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 5 == 0:
            result.append(num)
    if not result:
        return "No numbers found that are not divisible by 2 but divisible by 5."
    return result


# 178. Функция для нахождения всех чисел, которые являются кратными 3, 5 или 7
def find_multiples_of_3_5_or_7(lst):
    result = []
    for num in lst:
        if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
            result.append(num)
    if not result:
        return "No numbers found that are multiples of 3, 5, or 7."
    return result


# 179. Функция для нахождения всех чисел, которые являются чётными, но не являются делителями 4
def find_even_not_divisible_by_4(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 4 != 0:
            result.append(num)
    if not result:
        return "No even numbers found that are not divisible by 4."
    return result


# 180. Функция для нахождения чисел, которые являются кратными 3 или 5, но не кратными 15
def find_multiples_of_3_or_5_not_15(lst):
    result = []
    for num in lst:
        if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are multiples of 3 or 5 but not 15."
    return result


# 181. Функция для нахождения всех чисел, которые являются разностью двух квадратов
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


# 182. Функция для нахождения всех чисел, которые могут быть записаны как сумма двух чисел, каждое из которых делится на 3
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


# 183. Функция для нахождения всех чисел, которые не являются чётными, но являются делителями 9
def find_not_even_but_divisible_by_9(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 9 == 0:
            result.append(num)
    if not result:
        return "No numbers found that are not even but divisible by 9."
    return result


# 184. Функция для нахождения всех чисел, которые являются нечетными и делятся на 4
def find_divisible_by_2(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 4 != 0:
            result.append(num)
    if not result:
        return "No numbers."
    return result


# 185. Функция для нахождения всех чисел, которые делятся на 2 или на 3, но не на 6
def find_divisible_by_2_or_3_not_6(lst):
    result = []
    for num in lst:
        if (num % 2 == 0 or num % 3 == 0) and num % 6 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are divisible by 2 or 3 but not 6."
    return result


# 186. Функция для нахождения чисел, которые являются делителями 12, но не являются чётными
def find_divisors_of_12_not_even(lst):
    result = []
    for num in lst:
        if 12 % num == 0 and num % 2 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are divisors of 12 but not even."
    return result


# 187. Функция для нахождения всех чисел, которые являются делителями 6, но не 12
def find_divisors_of_6_not_12(lst):
    result = []
    for num in lst:
        if 6 % num == 0 and num != 12:
            result.append(num)
    if not result:
        return "No numbers found that are divisors of 6 but not 12."
    return result


# 188. Функция для нахождения всех чисел, которые являются квадратами чётных чисел
def find_squares_of_even_numbers(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 == 0:
            result.append(num)
    if not result:
        return "No squares of even numbers found."
    return result


# 189. Функция для нахождения чисел, которые не являются степенями 2, но являются чётными
def find_even_not_powers_of_2(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and (num & (num - 1)) != 0:
            result.append(num)
    if not result:
        return "No even numbers found that are not powers of 2."
    return result


# 190. Функция для нахождения всех чисел, которые не являются чётными и не являются делителями 9
def find_not_even_and_not_divisible_by_9(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are neither even nor divisible by 9."
    return result


# 191. Функция для нахождения чисел, которые делятся на 3 и 5, но не на 7
def find_multiples_of_3_and_5_not_7(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 5 == 0 and num % 7 != 0:
            result.append(num)
    if not result:
        return "No numbers found that are divisible by 3 and 5 but not 7."
    return result


# 192. Функция для нахождения всех чисел, которые являются произведением двух нечётных чисел
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


# 193. Функция для нахождения чисел, которые являются произведением двух простых чисел
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
        for i in range(1, num // 2 + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i):
                result.append(num)
                break
    if not result:
        return None
    return result


# 194. Функция для нахождения всех чисел, которые являются нечётными и не являются степенями 2
def find_odd_not_power_of_2(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and (num & (num - 1)) != 0:
            result.append(num)
    if not result:
        return None
    return result


# 195. Функция для нахождения чисел, которые делятся на 6, но не делятся на 9
def find_divisible_by_6_not_9(lst):
    result = []
    for num in lst:
        if num % 6 == 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 196. Функция для нахождения всех чисел, которые являются делителями 24, но не делятся на 8
def find_divisors_of_24_not_8(lst):
    result = []
    for num in lst:
        if 24 % num == 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 197. Функция для нахождения чисел, которые являются квадратами нечётных чисел
def find_squares_of_odd_numbers(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 198. Функция для нахождения чисел, которые являются степенями 2, но не чётными
def find_powers_of_2_not_even(lst):
    result = []
    for num in lst:
        if (num & (num - 1)) == 0 and num % 2 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 199. Функция для нахождения чисел, которые не являются кратными 3, но делятся на 5
def find_not_multiples_of_3_but_divisible_by_5(lst):
    result = []
    for num in lst:
        if num % 3 != 0 and num % 5 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 200. Функция для нахождения чисел, которые являются делителями 15, но не делятся на 3
def find_divisors_of_15_not_3(lst):
    result = []
    for num in lst:
        if 15 % num == 0 and num % 3 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 201. Функция для нахождения чисел, которые являются степенями 2, но не кратными 4
def find_powers_of_2_not_multiples_of_4(lst):
    result = []
    for num in lst:
        if (num & (num - 1)) == 0 and num % 4 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 202. Функция для нахождения чисел, которые являются нечётными, но не являются квадратами
def find_odd_not_square(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and int(num ** 0.5) ** 2 != num:
            result.append(num)
    if not result:
        return None
    return result


# 203. Функция для нахождения чисел, которые являются квадратами чётных чисел, но не делятся на 8
def find_squares_of_even_not_divisible_by_8(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 == 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 204. Функция для нахождения чисел, которые являются делителями 6, но не 2
def find_divisors_of_6_not_2(lst):
    result = []
    for num in lst:
        if 6 % num == 0 and num != 2:
            result.append(num)
    if not result:
        return None
    return result


# 205. Функция для нахождения всех чисел, которые являются делителями 48, но не делятся на 16
def find_divisors_of_48_not_16(lst):
    result = []
    for num in lst:
        if 48 % num == 0 and num % 16 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 206. Функция для нахождения всех чисел, которые являются делителями 20, но не являются чётными
def find_divisors_of_20_not_even(lst):
    result = []
    for num in lst:
        if 20 % num == 0 and num % 2 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 207. Функция для нахождения чисел, которые делятся на 2, но не делятся на 4 или 8
def find_divisible_by_2_not_4_or_8(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 4 != 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 208. Функция для нахождения всех чисел, которые являются квадратами нечётных чисел, но не на 7
def find_squares_of_odd_not_7(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0 and num % 7 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 209. Функция для нахождения всех чисел, которые делятся на 5, но не являются делителями 10
def find_divisible_by_5_not_divisible_by_10(lst):
    result = []
    for num in lst:
        if num % 5 == 0 and num % 10 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 210. Функция для нахождения всех чисел, которые являются произведением двух нечётных чисел, но не делятся на 3
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


# 211. Функция для нахождения чисел, которые являются чётными и не являются делителями 3
def find_even_not_divisible_by_3(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 212. Функция для нахождения чисел, которые являются разностью двух чётных чисел
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


# 213. Функция для нахождения всех чисел, которые являются делителями 18, но не делятся на 9
def find_divisors_of_18_not_9(lst):
    result = []
    for num in lst:
        if 18 % num == 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 214. Функция для нахождения чисел, которые являются кратными 3 и 5, но не кратными 15
def find_multiples_of_3_and_5_not_15(lst):
    result = []
    for num in lst:
        if num % 3 == 0 or num % 5 == 0 and num % 15 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 215. Функция для нахождения всех чисел, которые являются произведением двух простых чисел, но не делятся на 11
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
        for i in range(1, num // 2 + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i) and num % 11 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 216. Функция для нахождения чисел, которые являются квадратами чётных чисел, но не делятся на 4
def find_squares_of_even_not_divisible_by_4(lst):
    result = []
    for num in lst:
        if (int(num ** 0.5) ** 2 == num or int(num ** 0.5) % 2 == 0) and num % 4 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 217. Функция для нахождения чисел, которые делятся на 5 и на 6, но не на 10
def find_multiples_of_5_and_6_not_10(lst):
    result = []
    for num in lst:
        if (num % 5 == 0 or num % 6 == 0) and num % 10 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 218. Функция для нахождения чисел, которые являются разностью двух чётных чисел, но не делятся на 4
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


# 219. Функция для нахождения чисел, которые являются произведением двух простых чисел, но не делятся на 7
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
        for i in range(1, num // 2 + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i) and num % 7 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 220. Функция для нахождения всех чисел, которые являются разностью двух нечётных чисел
def find_difference_of_two_odd(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1, 2):
            if (num - i) % 3 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 221. Функция для нахождения чисел, которые являются произведением двух нечётных чисел, но не делятся на 5
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


# 222. Функция для нахождения чисел, которые являются делителями 36, но не делятся на 9
def find_divisors_of_36_not_9(lst):
    result = []
    for num in lst:
        if 36 % num == 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 223. Функция для нахождения чисел, которые являются нечётными и делятся на 5, но не на 10
def find_odd_and_divisible_by_5_not_10(lst):
    result = []
    for num in lst:
        if num % 2 != 0 and num % 5 == 0 and num % 10 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 224. Функция для нахождения всех чисел, которые делятся на 6, но не на 3
def find_divisible_by_6(lst):
    result = []
    for num in lst:
        if num % 6 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 225. Функция для нахождения всех чисел, которые являются делителями 30, но не делятся на 5
def find_divisors_of_30_not_5(lst):
    result = []
    for num in lst:
        if 30 % num == 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 226. Функция для нахождения чисел, которые являются произведением двух простых чисел, но не делятся на 6
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
        for i in range(1, num // 2 + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i) and num % 6 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 227. Функция для нахождения чисел, которые являются чётными и делятся на 7, но не на 14
def find_even_and_divisible_by_7(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 7 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 228. Функция для нахождения чисел, которые являются разностью двух нечётных чисел, но не делятся на 5
def find_difference_of_two_odd_not_5(lst):
    result = []
    for num in lst:
        for i in range(1, num // 2 + 1, 2):
            if num % 5 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 229. Функция для нахождения всех чисел, которые являются квадратами нечётных чисел, но не делятся на 5
def find_squares_of_odd_not_divisible_by_5(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 230. Функция для нахождения чисел, которые являются произведением двух простых чисел, но не делятся на 3
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
        for i in range(1, num // 2 + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i) and num % 3 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 231. Функция для нахождения всех чисел, которые являются делителями 40, но не являются чётными
def find_divisors_of_40_not_even(lst):
    result = []
    for num in lst:
        if 40 % num == 0 and num % 2 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 232. Функция для нахождения чисел, которые являются разностью двух чётных чисел, но не делятся на 5
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


# 233. Функция для нахождения чисел, которые являются произведением двух нечётных чисел, но не делятся на 7
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


# 234. Функция для нахождения чисел, которые делятся на 4, но не на 2
def find_divisible_by_4(lst):
    result = []
    for num in lst:
        if num % 4 == 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 235. Функция для нахождения чисел, которые являются квадратами нечётных чисел, но не на 9
def find_squares_of_odd_not_9(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 236. Функция для нахождения чисел, которые являются разностью двух простых чисел
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
        for i in range(1, num // 2 + 1):
            if is_prime(i) and is_prime(num - i):
                result.append(num)
                break
    if not result:
        return None
    return result


# 237. Функция для нахождения чисел, которые являются произведением двух простых чисел, но не на 5
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
        for i in range(1, num // 2 + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i) and num % 5 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 238. Функция для нахождения чисел, которые делятся на 2 и на 5, но не на 10
def find_divisible_by_2_and_5_not_10(lst):
    result = []
    for num in lst:
        if (num % 2 == 0 or num % 5 == 0) and num % 10 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 239. Функция для нахождения чисел, которые являются разностью двух чётных чисел, но не делятся на 6
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


# 240. Функция для нахождения чисел, которые являются произведением двух нечётных чисел, но не делятся на 4
def find_product_of_two_odd_not_divisible_by_4(lst):
    result = []
    for num in lst:
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0 and i % 2 != 0 and (num // i) % 2 != 0 and num % 5 != 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 241. Функция для нахождения чисел, которые являются кратными 6, но не на 12
def find_multiples_of_6_not_12(lst):
    result = []
    for num in lst:
        if num % 6 == 0 and num % 12 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 242. Функция для нахождения чисел, которые являются чётными и не делятся на 5
def find_even_not_divisible_by_5(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 243. Функция для нахождения чисел, которые являются квадратами нечётных чисел, но не делятся на 3
def find_squares_of_odd_not_divisible_by_3(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num and int(num ** 0.5) % 2 != 0 and num % 3 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 244. Функция для нахождения всех чисел, которые являются делителями 50, но не являются простыми
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


# 245. Функция для нахождения чисел, которые делятся на 3 и на 4, но не на 7
def find_divisible_by_3_and_4_not_7(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 4 == 0 and num % 7 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 246. Функция для нахождения чисел, которые являются пересечением двух множеств
def find_intersection_of_sets(lst1, lst2):
    result = set(lst1) & set(lst2)
    if not result:
        return None
    return sorted(list(result))


# 247. Функция для нахождения чисел, которые присутствуют в одном из двух списков, но не в обоих
def find_symmetric_difference(lst1, lst2):
    result = set(lst1) ^ set(lst2)
    if not result:
        return None
    return sorted(list(result))


# 248. Функция для нахождения чисел, которые являются ключами в одном словаре и значениями в другом
def find_keys_in_dicts(dict1, dict2):
    result = [key for key in dict1 if dict1[key] in dict2]
    if not result:
        return None
    return result


# 249. Функция для нахождения чисел, которые присутствуют в списке, но не в кортеже
def find_in_list_not_in_tuple(lst, tpl):
    result = [x for x in lst if x not in tpl]
    if not result:
        return None
    return result


# 250. Функция для нахождения чисел, которые являются парами, где первое число больше второго
def find_pairs_with_first_greater(lst):
    result = [(a, b) for a in lst for b in lst if a > b]
    if not result:
        return None
    return result


# 251. Функция для нахождения чисел, которые являются кортежами, но не содержат отрицательных чисел
def find_tuples_without_negatives(lst):
    result = [tpl for tpl in lst if all(x >= 0 for x in tpl)]
    if not result:
        return None
    return result


# 252. Функция для нахождения чисел, которые присутствуют в словаре как ключи, но не имеют чётных значений
def find_keys_with_odd_values(dict_data):
    result = [key for key, value in dict_data.items() if value % 2 != 0]
    if not result:
        return None
    return result


# 253. Функция для нахождения чисел, которые являются произведением двух чисел, но не делятся на 2
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


# 254. Функция для нахождения чисел, которые являются элементами множества, но не присутствуют в списке
def find_in_set_not_in_list(s, lst):
    result = sorted(list(s - set(lst)))
    if not result:
        return None
    return result


# 255. Функция для нахождения чисел, которые присутствуют в словаре как ключи, но не делятся на 3
def find_keys_not_divisible_by_3(dict_data):
    result = [key for key in dict_data if key % 3 != 0]
    if not result:
        return None
    return result


# 256. Функция для нахождения чисел, которые встречаются в двух списках и их сумма делится на 4
def find_numbers_with_sum_divisible_by_4(lst1, lst2):
    result = []
    for num1 in lst1:
        for num2 in lst2:
            if (num1 + num2) % 4 == 0:
                result.append((num1, num2))
    if not result:
        return None
    return result


# 257. Функция для нахождения чисел, которые встречаются только в одном из двух списков
def find_unique_in_one_list(lst1, lst2):
    result = list(set(lst1) ^ set(lst2))
    if not result:
        return None
    return result


# 258. Функция для нахождения чисел, которые являются парами, где сумма элементов делится на 5
def find_pairs_with_sum_divisible_by_5(lst):
    result = [(a, b) for a in lst for b in lst if (a + b) % 5 == 0]
    if not result:
        return None
    return result


# 259. Функция для нахождения чисел, которые являются кортежами, но не содержат чётных чисел
def find_tuples_without_even_numbers(lst):
    result = [tpl for tpl in lst if all(x % 2 != 0 for x in tpl)]
    if not result:
        return None
    return result


# 260. Функция для нахождения чисел, которые являются целыми числами в строках
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


# 261. Функция для нахождения чисел, которые делятся на 7 и на 8, но не на 56
def find_divisible_by_7_and_8_not_56(lst):
    result = []
    for num in lst:
        if (num % 7 == 0 or num % 8 == 0) and num % 56 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 262. Функция для нахождения чисел, которые являются нечётными и присутствуют в словаре как ключи
def find_odd_keys_in_dict(dict_data):
    result = [key for key in dict_data if key % 2 != 0]
    if not result:
        return None
    return result


# 263. Функция для нахождения чисел, которые являются чётными и присутствуют в кортеже, но не в списке
def find_even_in_tuple_not_in_list(tpl, lst):
    result = [x for x in tpl if x % 2 == 0 and x not in lst]
    if not result:
        return None
    return result


# 264. Функция для нахождения чисел, которые являются делителями 100, но не являются простыми
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


# 265. Функция для нахождения чисел, которые встречаются в списке, но не в множестве
def find_in_list_not_in_set(lst, s):
    result = [x for x in lst if x not in s]
    if not result:
        return None
    return result


# 266. Функция для нахождения чисел, которые являются результатами суммы элементов из двух списков
def find_sum_of_two_lists(lst1, lst2):
    result = [a + b for a in lst1 for b in lst2]
    if not result:
        return None
    return result


# 267. Функция для нахождения чисел, которые являются разностью элементов из двух списков
def find_difference_of_two_lists(lst1, lst2):
    result = [a - b for a in lst1 for b in lst2]
    if not result:
        return None
    return result


# 268. Функция для нахождения чисел, которые являются нечётными и присутствуют в кортеже, но не в списке
def find_odd_in_tuple_not_in_list(tpl, lst):
    result = [x for x in tpl if x % 2 != 0 and x not in lst]
    if not result:
        return None
    return result


# 269. Функция для нахождения чисел, которые делятся на 5 и на 6, но не на 12
def find_divisible_by_5_and_6_not_12(lst):
    result = []
    for num in lst:
        if num % 5 == 0 and num % 6 == 0 and num % 12 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 270. Функция для нахождения чисел, которые являются нечётными, но не являются делителями 5
def find_odd_not_divisible_by_5_2(lst):
    result = [num for num in lst if num % 2 != 0 and num % 5 != 0]
    if not result:
        return None
    return result


# 271. Функция для нахождения чисел, которые являются чётными и присутствуют в списке и кортеже
def find_even_in_list_and_tuple(lst, tpl):
    result = [x for x in lst if x % 2 == 0 and x in tpl]
    if not result:
        return None
    return result


# 272. Функция для нахождения чисел, которые являются результатом произведения двух чисел
def find_product_of_two_numbers(lst):
    result = [a * b for a in lst for b in lst]
    if not result:
        return None
    return result


# 273. Функция для нахождения чисел, которые являются элементами множества, но не встречаются в списке
def find_in_set_not_in_list_2(s, lst):
    result = [x for x in s if x not in lst]
    if not result:
        return None
    return result


# 274. Функция для нахождения чисел, которые являются результатами разности чисел в списках
def find_difference_between_lists(lst1, lst2):
    result = [a - b for a in lst1 for b in lst2]
    if not result:
        return None
    return result


# 275. Функция для нахождения чисел, которые присутствуют в одном из списков, но не в обоих
def find_unique_in_one_list_not_both(lst1, lst2):
    result = [x for x in lst1 if x not in lst2] + [x for x in lst2 if x not in lst1]
    if not result:
        return None
    return result


# 276. Функция для нахождения чисел, которые являются четными и делятся на 3
def find_even_and_divisible_by_3(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            if num % 3 == 0:
                result.append(num)
    if not result:
        return None
    return result


# 277. Функция для нахождения чисел, которые являются квадратами, но не делятся на 5
def find_squares_not_divisible_by_5(lst):
    result = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num:
            if num % 5 != 0:
                result.append(num)
    if not result:
        return None
    return result


# 278. Функция для нахождения чисел, которые делятся на 7 и на 8, но не на 56
def find_divisible_by_7_and_8_not_56_2(lst):
    result = []
    for num in lst:
        if num % 7 == 0:
            if num % 8 == 0:
                if num % 56 == 0:
                    result.append(num)
    if not result:
        return None
    return result


# 279. Функция для нахождения чисел, которые присутствуют в списке и кортежах
def find_in_list_and_tuple(lst, tpl):
    result = []
    for num in lst:
        if num in tpl:
            result.append(num)
    if not result:
        return None
    return result


# 280. Функция для нахождения чисел, которые являются суммой двух чисел, но не делятся на 4
def find_sum_of_two_not_divisible_by_4(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i] + lst[j]) % 4 != 0:
                result.append(lst[i] + lst[j])
    if not result:
        return None
    return result


# 281. Функция для нахождения чисел, которые присутствуют в обоих списках
def find_in_both_lists(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2:
            result.append(num)
    if not result:
        return None
    return result


# 282. Функция для нахождения чисел, которые не присутствуют в одном из списков
def find_not_in_list(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    if not result:
        return None
    return result


# 283. Функция для нахождения чисел, которые являются произведением двух чисел, но не делятся на 7
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


# 284. Функция для нахождения чисел, которые являются произведением двух нечётных чисел
def find_product_of_two_odds(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] % 2 != 0 and lst[j] % 2 != 0:
                result.append(lst[i] * lst[j])
    if not result:
        return None
    return result


# 285. Функция для нахождения чисел, которые являются суммой двух нечётных чисел
def find_sum_of_two_odds(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] % 2 != 0 and lst[j] % 2 != 0:
                result.append(lst[i] + lst[j])
    if not result:
        return None
    return result


# 286. Функция для нахождения чисел, которые являются четными и находятся в кортеже
def find_even_in_tuple(tpl):
    result = []
    for num in tpl:
        if num % 2 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 287. Функция для нахождения чисел, которые являются произведением двух чисел, но не на 5
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


# 288. Функция для нахождения чисел, которые присутствуют в одном словаре, но не в другом
def find_keys_in_dict_not_in_other(dict1, dict2):
    result = []
    for key in dict1:
        if key not in dict2:
            result.append(key)
    if not result:
        return None
    return result


# 289. Функция для нахождения чисел, которые являются разностью элементов в кортеже
def find_difference_in_tuple(tpl):
    result = []
    for i in range(len(tpl)):
        for j in range(i + 1, len(tpl)):
            result.append(abs(tpl[i] - tpl[j]))
    if not result:
        return None
    return result


# 290. Функция для нахождения чисел, которые являются результатом разности двух чисел из двух списков
def find_difference_between_lists_2(lst1, lst2):
    result = []
    for num1 in lst1:
        for num2 in lst2:
            result.append(abs(num1 - num2))
    if not result:
        return None
    return result


# 291. Функция для нахождения чисел, которые являются нечётными и присутствуют в одном из списков
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


# 292. Функция для нахождения чисел, которые являются результатом суммы двух чисел из одного списка
def find_sum_of_two_from_one_list(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            result.append(lst[i] + lst[j])
    if not result:
        return None
    return result


# 293. Функция для нахождения чисел, которые встречаются в обоих списках, но не в обоих списках сразу
def find_common_not_in_both_lists(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2:
            if num not in result:
                result.append(num)
    if not result:
        return None
    return result


# 294. Функция для нахождения чисел, которые являются результатом суммы элементов двух списков
def find_sum_of_elements_from_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a + b)
    if not result:
        return None
    return result


# 295. Функция для нахождения чисел, которые являются результатом разности элементов из двух списков
def find_difference_of_elements_from_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a - b)
    if not result:
        return None
    return result


# 296. Функция для преобразования чисел из списка в их квадраты
def square_numbers(lst):
    result = list(map(lambda x: x ** 2, lst))
    if not result:
        return None
    return result


# 297. Функция для нахождения чисел, которые делятся на 3, но не на 5
def find_divisible_by_3_not_5(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 298. Функция для нахождения чисел, которые присутствуют только в одном из двух списков
def find_unique_in_one_list_3(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if a != b:
            result.append(a)
            result.append(b)
    if not result:
        return None
    return result


# 299. Функция для нахождения чисел, которые присутствуют в списке, но не в кортеже
def find_in_list_not_in_tuple_2(lst, tpl):
    result = []
    for num in lst:
        if num not in tpl:
            result.append(num)
    if not result:
        return None
    return result


# 300. Функция для нахождения чисел, которые являются кубами чисел в списке
def find_cubes(lst):
    result = list(map(lambda x: x ** 3, lst))
    if not result:
        return None
    return result


# 301. Функция для нахождения чисел, которые делятся на 2 и 3
def find_divisible_by_2_and_3(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 302. Функция для нахождения чисел, которые являются результатом возведения в степень
def find_powers_of_numbers(lst, power):
    result = list(map(lambda x: x ** power, lst))
    if not result:
        return None
    return result


# 303. Функция для нахождения чисел, которые являются результатом разности двух чисел в разных списках
def find_difference_between_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(abs(a - b))
    if not result:
        return None
    return result


# 304. Функция для нахождения чисел, которые присутствуют в обоих словарях
def find_keys_in_both_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2:
            result.append(key)
    if not result:
        return None
    return result


# 305. Функция для нахождения чисел, которые являются результатом произведения чисел из двух списков
def find_product_of_elements_from_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a * b)
    if not result:
        return None
    return result


# 306. Функция для нахождения чисел, которые присутствуют в словаре, но не в списке
def find_keys_in_dict_not_in_list(d, lst):
    result = []
    for key in d:
        if key not in lst:
            result.append(key)
    if not result:
        return None
    return result


# 307. Функция для нахождения чисел, которые являются результатом возведения чисел из списка в степень
def find_powers_of_numbers_in_list(lst, power):
    result = []
    for num in lst:
        result.append(num ** power)
    if not result:
        return None
    return result


# 308. Функция для нахождения чисел, которые присутствуют в обоих множествах
def find_elements_in_both_sets(set1, set2):
    result = list(set1 & set2)
    if not result:
        return None
    return result


# 309. Функция для нахождения чисел, которые являются разницей элементов из двух списков
def find_diff_between_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(abs(a - b))
    if not result:
        return None
    return result


# 310. Функция для нахождения чисел, которые являются результатом сложения чисел в двух списках
def find_sum_of_two_lists_2(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a + b)
    if not result:
        return None
    return result


# 311. Функция для нахождения чисел, которые присутствуют в кортеже, но не в списке
def find_in_tuple_not_in_list(tpl, lst):
    result = []
    for num in tpl:
        if num not in lst:
            result.append(num)
    if not result:
        return None
    return result


# 312. Функция для нахождения чисел, которые делятся на 10, но не на 20
def find_divisible_by_10_not_20(lst):
    result = []
    for num in lst:
        if num % 10 == 0 and num % 20 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 313. Функция для нахождения чисел, которые являются суммой элементов из двух списков
def find_sum_from_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a + b)
    if not result:
        return None
    return result


# 314. Функция для нахождения чисел, которые присутствуют в обоих множествах
def find_common_elements_in_sets(set1, set2):
    result = list(set1 & set2)
    if not result:
        return None
    return result


# 315. Функция для нахождения чисел, которые являются произведением чисел в списке
def find_product_in_list(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            result.append(lst[i] * lst[j])
    if not result:
        return None
    return result


# 316. Функция для нахождения чисел, которые присутствуют в списке и не присутствуют в словаре
def find_in_list_not_in_dict(lst, d):
    result = []
    for num in lst:
        if num not in d:
            result.append(num)
    if not result:
        return None
    return result


# 317. Функция для объединения двух словарей
def merge_dicts_2(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    if not result:
        return None
    return result


# 318. Функция для нахождения чисел, которые присутствуют в одном из двух наборов
def find_in_one_set_not_other(set1, set2):
    result = set1.symmetric_difference(set2)
    if not result:
        return None
    return list(result)


# 319. Функция для нахождения чисел, которые являются результатом деления элементов из двух списков
def find_division_from_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:
            result.append(a / b)
    if not result:
        return None
    return result


# 320. Функция для нахождения чисел, которые присутствуют в обоих списках, но в одном из них меньше
def find_common_less_in_one_list(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2 and lst1.count(num) < lst2.count(num):
            result.append(num)
    if not result:
        return None
    return result


# 321. Функция для нахождения чисел, которые находятся в одном списке, но не в другом
def find_in_first_not_in_second(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    if not result:
        return None
    return result


# 322. Функция для нахождения чисел, которые присутствуют в обоих списках, но имеют разные индексы
def find_common_elements_diff_index(lst1, lst2):
    result = []
    for i, num1 in enumerate(lst1):
        for j, num2 in enumerate(lst2):
            if num1 == num2 and i != j:
                result.append(num1)
    if not result:
        return None
    return sorted(set(result))


# 323. Функция для нахождения чисел, которые являются результатом добавления элементов из двух словарей
def add_values_of_dicts(dict1, dict2):
    result = {}
    for key in dict1:
        if key in dict2:
            result[key] = dict1[key] + dict2[key]
    if not result:
        return None
    return result


# 324. Функция для нахождения чисел, которые находятся в двух множествах, но в одном из них больше
def find_more_in_one_set(set1, set2):
    result = []
    for num in set1:
        if num in set2 and num % 3 == 0:
            result.append(num)
    if not result:
        return None
    return sorted(result)


# 325. Функция для нахождения чисел, которые являются результатом умножения чисел в списке на два
def multiply_numbers_by_two(lst):
    result = []
    for num in lst:
        result.append(num * 2)
    if not result:
        return None
    return result


# 326. Функция для нахождения чисел, которые являются результатом суммы значений по ключам в словарях
def sum_dict_values(dict1, dict2):
    result = {}
    for key in dict1:
        if key in dict2:
            result[key] = dict1[key] + dict2[key]
    if not result:
        return None
    return result


# 327. Функция для нахождения чисел, которые являются квадратами чисел из списка
def find_squares_2(lst):
    result = []
    for num in lst:
        result.append(num ** 2)
    if not result:
        return None
    return result


# 328. Функция для нахождения чисел, которые являются разницей элементов из двух множеств
def find_difference_of_sets(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return sorted(result)


# 329. Функция для нахождения чисел, которые являются результатом суммирования элементов из списка и множества
def find_sum_list_set(lst, s):
    result = []
    for num in lst:
        if num in s:
            result.append(num + 1)
    if not result:
        return None
    return result


# 330. Функция для нахождения чисел, которые встречаются в одном множестве, но не в другом
def find_in_set_not_in_other_set(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return result


# 331. Функция для нахождения чисел, которые являются результатом деления элементов одного списка на элементы другого
def divide_elements_of_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:
            result.append(a / b)
    if not result:
        return None
    return result


# 332. Функция для нахождения чисел, которые находятся в двух множествах, но не в одном из них
def find_in_both_sets_not_in_one(set1, set2):
    result = list(set1 & set2 ^ (set1 | set2))
    if not result:
        return None
    return sorted(result)


# 333. Функция для нахождения чисел, которые являются результатом вычитания элементов из списка и множества
def subtract_set_from_list(lst, s):
    result = []
    for num in lst:
        if num not in s:
            result.append(num)
    if not result:
        return None
    return result


# 334. Функция для нахождения чисел, которые являются результатом суммирования элементов из двух кортежей
def find_sum_of_tuples(tpl1, tpl2):
    result = []
    for a, b in zip(tpl1, tpl2):
        result.append(a + b)
    if not result:
        return None
    return result


# 335. Функция для нахождения чисел, которые присутствуют в одном из двух множеств
def find_in_one_set_not_other_2(set1, set2):
    result = list(set1 ^ set2)
    if not result:
        return None
    return result


# 336. Функция для нахождения чисел, которые делятся на 4, но не на 8
def find_divisible_by_4_not_8(lst):
    result = []
    for num in lst:
        if num % 4 == 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 337. Функция для нахождения чисел, которые присутствуют в одном словаре, но не в другом
def find_keys_in_dict1_not_in_dict2(dict1, dict2):
    result = []
    for key in dict1:
        if key not in dict2:
            result.append(key)
    if not result:
        return None
    return result


# 338. Функция для нахождения чисел, которые являются результатом умножения чисел в одном списке на два
def multiply_by_two(lst):
    result = []
    for num in lst:
        result.append(num * 2)
    if not result:
        return None
    return result


# 339. Функция для нахождения чисел, которые являются результатом вычитания элементов одного списка из другого
def subtract_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a - b)
    if not result:
        return None
    return result


# 340. Функция для нахождения чисел, которые присутствуют в обоих словарях
def find_common_in_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2:
            result.append(key)
    if not result:
        return None
    return result


# 341. Функция для нахождения чисел, которые являются результатом сложения всех чисел в списке
def sum_list_3(lst):
    return sum(lst) if lst else None


# 342. Функция для нахождения чисел, которые делятся на 3, но не на 9
def find_divisible_by_3_not_9(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 9 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 343. Функция для нахождения чисел, которые делятся на 5 или 7
def find_divisible_by_5_or_7(lst):
    result = []
    for num in lst:
        if num % 5 == 0 or num % 7 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 344. Функция для нахождения чисел, которые присутствуют в одном из двух словарей
def find_in_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2:
            result.append(key)
    if not result:
        return None
    return result


# 345. Функция для нахождения чисел, которые делятся на 3 или 5
def find_divisible_by_3_or_5(lst):
    result = []
    for num in lst:
        if num % 3 == 0 or num % 5 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 346. Функция для нахождения чисел, которые делятся на 4, но не на 6
def find_divisible_by_4_not_6(lst):
    result = []
    for num in lst:
        if num % 4 == 0 and num % 6 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 347. Функция для нахождения чисел, которые делятся на 5, но не на 10
def find_divisible_by_5_not_10(lst):
    result = []
    for num in lst:
        if num % 5 == 0 and num % 10 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 348. Функция для нахождения чисел, которые являются результатом возведения элементов списка в степень
def find_powers_of_list(lst, power):
    result = []
    for num in lst:
        result.append(num ** power)
    if not result:
        return None
    return result


# 349. Функция для нахождения чисел, которые делятся на 6, но не на 12
def find_divisible_by_6_not_12(lst):
    result = []
    for num in lst:
        if num % 6 == 0 and num % 12 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 350. Функция для нахождения чисел, которые делятся на 4 или 5
def find_divisible_by_4_or_5(lst):
    result = []
    for num in lst:
        if num % 4 == 0 or num % 5 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 351. Функция для нахождения чисел, которые присутствуют в одном списке, но не в другом
def find_in_list_not_in_another(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    if not result:
        return None
    return result


# 352. Функция для нахождения чисел, которые присутствуют в одном словаре, но не в другом
def find_unique_keys_in_dict(dict1, dict2):
    result = []
    for key in dict1:
        if key not in dict2:
            result.append(key)
    if not result:
        return None
    return result


# 353. Функция для нахождения чисел, которые являются произведением чисел из двух списков
def multiply_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a * b)
    if not result:
        return None
    return result


# 354. Функция для нахождения чисел, которые являются результатом вычитания элементов одного списка из другого
def subtract_lists_v2(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a - b)
    if not result:
        return None
    return result


# 355. Функция для нахождения чисел, которые присутствуют в одном множестве, но не в другом
def find_in_set_not_other(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return sorted(result)


# 356. Функция для нахождения чисел, которые присутствуют в обоих множествах
def find_common_in_sets(set1, set2):
    result = list(set1 & set2)
    if not result:
        return None
    return sorted(result)


# 357. Функция для нахождения чисел, которые делятся на 2 и присутствуют в двух множествах
def find_divisible_by_2_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 2 == 0})
    if not result:
        return None
    return sorted(result)


# 358. Функция для нахождения чисел, которые не делятся на 3 и присутствуют в двух множествах
def find_not_divisible_by_3_in_both_sets(set1, set2):
    result = list((set1 & set2) - {num for num in range(1, 101) if num % 3 == 0})
    if not result:
        return None
    return sorted(result)


# 359. Функция для нахождения чисел, которые присутствуют в одном множестве и не присутствуют в другом
def find_in_one_set_not_other_v2(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return sorted(result)


# 360. Функция для нахождения чисел, которые делятся на 2 или 5, и присутствуют в двух множествах
def find_divisible_by_2_or_5_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 2 == 0 or num % 5 == 0})
    if not result:
        return None
    return sorted(result)


# 361. Функция для нахождения чисел, которые не делятся на 2 или 3, и присутствуют в двух множествах
def find_not_divisible_by_2_or_3_in_both_sets(set1, set2):
    result = list((set1 & set2) - {num for num in range(1, 101) if num % 2 == 0 or num % 3 == 0})
    if not result:
        return None
    return sorted(result)


# 362. Функция для нахождения чисел, которые делятся на 4 и присутствуют в обоих множествах
def find_divisible_by_4_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 4 == 0})
    if not result:
        return None
    return sorted(result)


# 363. Функция для нахождения чисел, которые присутствуют в одном множестве, но не в другом
def find_in_set_not_other_v2(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return sorted(result)


# 364. Функция для нахождения чисел, которые присутствуют в одном из двух множеств
def find_in_any_set(set1, set2):
    result = list(set1 | set2)
    if not result:
        return None
    return sorted(result)


# 365. Функция для нахождения чисел, которые делятся на 7 и присутствуют в обоих множествах
def find_divisible_by_7_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 7 == 0})
    if not result:
        return None
    return sorted(result)


# 366. Функция для нахождения чисел, которые присутствуют в одном множестве, но не в другом
def find_difference_in_sets(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return sorted(result)


# 367. Функция для нахождения чисел, которые не делятся на 2, но присутствуют в обоих множествах
def find_not_divisible_by_2_in_both_sets(set1, set2):
    result = list((set1 & set2) - {num for num in range(1, 101) if num % 2 == 0})
    if not result:
        return None
    return sorted(result)


# 368. Функция для нахождения чисел, которые являются общими для трёх множеств
def find_common_in_three_sets(set1, set2, set3):
    result = list(set1 & set2 & set3)
    if not result:
        return None
    return sorted(result)


# 369. Функция для нахождения чисел, которые являются разностью элементов из трёх множеств
def find_difference_in_three_sets(set1, set2, set3):
    result = list(set1 - set2 - set3)
    if not result:
        return None
    return sorted(result)


# 370. Функция для нахождения чисел, которые присутствуют в одном множестве, но не в другом
def find_diff_in_sets_v2(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return sorted(result)


# 371. Функция для нахождения чисел, которые не делятся на 5 и присутствуют в обоих множествах
def find_not_divisible_by_5_in_both_sets(set1, set2):
    result = list((set1 & set2) - {num for num in range(1, 101) if num % 5 == 0})
    if not result:
        return None
    return sorted(result)


# 372. Функция для нахождения чисел, которые делятся на 3 или 6 и присутствуют в обоих множествах
def find_divisible_by_3_or_6_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 3 == 0 or num % 6 == 0})
    if not result:
        return None
    return sorted(result)


# 373. Функция для нахождения чисел, которые являются общими для двух множеств и делятся на 3
def find_common_in_sets_divisible_by_3(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 3 == 0})
    if not result:
        return None
    return sorted(result)


# 374. Функция для нахождения чисел, которые делятся на 6, но не на 12 и присутствуют в двух множествах
def find_divisible_by_6_not_12_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 6 == 0 and num % 12 != 0})
    if not result:
        return None
    return sorted(result)


# 375. Функция для нахождения чисел, которые не присутствуют в обоих множествах
def find_not_in_both_sets(set1, set2):
    result = list(set1 ^ set2)
    if not result:
        return None
    return sorted(result)


# 376. Функция для нахождения чисел, которые являются разницей между тремя множествами
def find_difference_between_three_sets(set1, set2, set3):
    result = list(set1 - set2 - set3)
    if not result:
        return None
    return sorted(result)


# 377. Функция для нахождения чисел, которые делятся на 2, но не на 3, и присутствуют в двух множествах
def find_divisible_by_2_not_3_in_both_sets(set1, set2):
    result = list((set1 & set2) & {num for num in range(1, 101) if num % 2 == 0 and num % 3 != 0})
    if not result:
        return None
    return sorted(result)


# 378. Функция для нахождения чисел, которые присутствуют в обоих множествах и не делятся на 4
def find_common_not_divisible_by_4(set1, set2):
    result = list((set1 & set2) - {num for num in range(1, 101) if num % 4 == 0})
    if not result:
        return None
    return sorted(result)


# 379. Функция для нахождения чисел, которые присутствуют только в одном из двух множеств
def find_unique_in_sets(set1, set2):
    result = list(set1 ^ set2)
    if not result:
        return None
    return sorted(result)


# 380. Функция для нахождения чисел, которые являются общими для всех трёх множеств
def find_common_in_all_sets(set1, set2, set3):
    result = list(set1 & set2 & set3)
    if not result:
        return None
    return sorted(result)


# 381. Функция для нахождения чисел, которые присутствуют в двух множествах и не делятся на 3
def find_in_both_sets_not_divisible_by_3(set1, set2):
    result = list((set1 & set2) - {num for num in range(1, 101) if num % 3 == 0})
    if not result:
        return None
    return sorted(result)


# 382. Функция для нахождения чисел, которые присутствуют только в одном из двух множеств
def find_unique_in_one_set(set1, set2):
    result = list(set1 ^ set2)
    if not result:
        return None
    return sorted(result)


# 383. Функция для нахождения чисел, которые присутствуют в одном множестве, но не в другом
def find_in_set_not_other_v3(set1, set2):
    result = []
    for elem in set1:
        if elem not in set2:
            result.append(elem)
    if not result:
        return None
    return sorted(result)


# 384. Функция для нахождения чисел, которые являются пересечением двух множеств и делятся на 3
def find_common_divisible_by_3(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return sorted(result)


# 385. Функция для нахождения чисел, которые присутствуют в одном из двух множеств, но не в обоих
def find_in_one_set_not_other_v3(set1, set2):
    result = []
    for elem in set1 | set2:
        if (elem in set1) != (elem in set2):
            result.append(elem)
    if not result:
        return None
    return sorted(result)


# 386. Функция для нахождения чисел, которые делятся на 2, но не на 4 и присутствуют в двух множествах
def find_divisible_by_2_not_4_in_both_sets(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 2 == 0 and elem % 4 != 0:
            result.append(elem)
    if not result:
        return None
    return sorted(result)


# 387. Функция для нахождения чисел, которые присутствуют в двух множествах и не делятся на 5
def find_in_both_sets_not_divisible_by_5(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 5 != 0:
            result.append(elem)
    if not result:
        return None
    return sorted(result)


# 388. Функция для нахождения чисел, которые присутствуют в обоих множествах и делятся на 3
def find_in_both_sets_divisible_by_3(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return sorted(result)


# 389. Функция для нахождения чисел, которые присутствуют в одном из двух множеств, но не в обоих
def find_unique_in_sets_v2(set1, set2):
    result = []
    for elem in set1 ^ set2:
        result.append(elem)
    if not result:
        return None
    return sorted(result)


# 390. Функция для нахождения чисел, которые присутствуют в первом множестве, но не во втором, и делятся на 7
def find_in_first_set_not_second_divisible_by_7(set1, set2):
    result = []
    for elem in set1 - set2:
        if elem % 7 == 0:
            result.append(elem)
    if not result:
        return None
    return sorted(result)


# 391. Функция для нахождения чисел, которые делятся на 6, но не на 12 и присутствуют в двух множествах
def find_divisible_by_6_not_12_in_both_sets_2(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 6 == 0 and elem % 12 != 0:
            result.append(elem)
    if not result:
        return None
    return sorted(result)


# 392. Функция для нахождения чисел, которые присутствуют в одном из двух множеств, но не в обоих, и делятся на 5
def find_in_one_set_not_other_divisible_by_5(set1, set2):
    result = []
    for elem in set1 ^ set2:
        if elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return sorted(result)


# 393. Функция для нахождения чисел, которые являются общими для двух множеств и делятся на 4
def find_common_in_sets_divisible_by_4(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 4 == 0:
            result.append(elem)
    if not result:
        return None
    return sorted(result)


# 394. Функция для нахождения чисел, которые делятся на 3 и присутствуют в обоих множествах
def find_divisible_by_3_in_both_sets(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return sorted(result)


# 395. Функция для нахождения чисел, которые присутствуют только в одном из двух множеств, но не в другом
def find_difference_in_sets_v2(set1, set2):
    result = []
    for elem in set1 - set2:
        result.append(elem)
    for elem in set2 - set1:
        result.append(elem)
    if not result:
        return None
    return sorted(result)


# 396. Функция для нахождения чисел, которые присутствуют в двух множествах и делятся на 4
def find_divisible_by_4_in_both_sets_2(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 4 == 0:
            result.append(elem)
    if not result:
        return None
    return sorted(result)


# 397. Функция для нахождения чисел, которые присутствуют только в одном множестве и не делятся на 3
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
    return sorted(result)


# 398. Функция для нахождения чисел, которые делятся на 5 и присутствуют в двух множествах
def find_divisible_by_5_in_both_sets(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return sorted(result)


# 399. Функция для нахождения чисел, которые присутствуют в обоих множествах и не делятся на 2
def find_in_both_sets_not_divisible_by_2(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 2 != 0:
            result.append(elem)
    if not result:
        return None
    return sorted(result)


# 400. Функция для нахождения чисел, которые являются разностью между двумя множествами
def find_difference_between_sets(set1, set2):
    result = list(set1 - set2)
    if not result:
        return None
    return sorted(result)


# 401. Функция для нахождения чисел, которые присутствуют в одном из двух множеств, но не в обоих
def find_unique_elements_in_sets(set1, set2):
    result = list(set1 ^ set2)
    if not result:
        return None
    return sorted(result)


# 402. Функция для нахождения чисел, которые делятся на 2 и присутствуют в двух множествах
def find_divisible_by_2_in_both_sets_2(set1, set2):
    result = []
    for elem in set1 & set2:
        if elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return sorted(result)


# 403. Функция для нахождения чисел, которые присутствуют в первом множестве, но не во втором
def find_in_first_set_not_second(set1, set2):
    result = []
    for elem in set1 - set2:
        result.append(elem)
    if not result:
        return None
    return sorted(result)


# 404. Функция для нахождения чисел, которые делятся на 5 и присутствуют только в одном множестве
def find_divisible_by_5_in_one_set(set1, set2):
    result = []
    for elem in set1:
        if elem % 5 == 0 and elem not in set2:
            result.append(elem)
    if not result:
        return None
    return sorted(result)


# 405. Функция для проверки, является ли стек пустым
def is_stack_empty(stack):
    if len(stack) == 0:
        return True
    return False


# 406. Функция для добавления элементов в стек, пока не будет достигнут определённый предел
def fill_stack_until_limit(stack, limit):
    while len(stack) < limit:
        stack.append(len(stack) + 1)
    return stack


# 407. Функция для пополнения стека числами от 1 до N
def fill_stack_up_to_n(stack, n):
    for i in range(1, n + 1):
        stack.append(i)
    return stack


# 408. Функция для проверки, является ли стек палиндромом
def is_stack_palindrome(stack):
    def reverse_stack(stack):
        reversed_stack = []
        while stack:
            reversed_stack.append(stack.pop())
        return reversed_stack
    original = list(stack)
    reversed_stack = reverse_stack(stack)
    if original == reversed_stack:
        return True
    return False


# 409. Функция для извлечения и возврата элементов из стека, пока не встретится число, большее чем X
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


# 410. Функция для извлечения и возврата всех элементов стека, меньших чем Y
def pop_elements_less_than_y(stack, y):
    result = []
    while stack:
        elem = stack.pop()
        if elem < y:
            result.append(elem)
    if not result:
        return None
    return result


# 411. Функция для удаления всех нечётных чисел из стека
def remove_odds_from_stack(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 412. Функция для извлечения элементов из стека до тех пор, пока сумма элементов не превысит X
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


# 413. Функция для извлечения всех элементов из стека, которые делятся на 3
def pop_elements_divisible_by_3(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 414. Функция для поиска и извлечения наименьшего элемента из стека
def pop_min_element(stack):
    if not stack:
        return None
    min_elem = min(stack)
    stack.remove(min_elem)
    return min_elem


# 415. Функция для создания нового стека с удвоенными значениями исходного стека
def double_stack_values(stack):
    new_stack = []
    while stack:
        elem = stack.pop()
        new_stack.append(elem * 2)
    return new_stack


# 416. Функция для извлечения элементов, пока не встретится чётное число
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


# 417. Функция для извлечения всех чисел из стека, которые являются простыми
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


# 418. Функция для извлечения элементов из стека до тех пор, пока не встретится число, которое делится на 4
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


# 419. Функция для удаления из стека всех чисел, которые не делятся на 2
def remove_non_divisible_by_2(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 420. Функция для нахождения и удаления всех чётных чисел из стека
def remove_even_from_stack(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 2 != 0:
            result.append(elem)
    if not result:
        return None
    return result


# 421. Функция для извлечения всех чисел из стека, которые больше чем X
def pop_elements_greater_than_x(stack, x):
    result = []
    while stack:
        elem = stack.pop()
        if elem > x:
            result.append(elem)
    if not result:
        return None
    return result


# 422. Функция для нахождения всех чётных чисел в стеке
def find_even_in_stack(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 423. Функция для удаления всех чисел, которые делятся на 5 из стека
def remove_divisible_by_5_from_stack(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 5 != 0:
            result.append(elem)
    if not result:
        return None
    return result


# 424. Функция для удаления максимального элемента из стека
def remove_max_from_stack(stack):
    if not stack:
        return None
    max_elem = max(stack)
    stack.remove(max_elem)
    return max_elem


# 425. Функция для нахождения и извлечения всех чисел, которые не делятся на 3
def pop_elements_not_divisible_by_3(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 3 != 0:
            result.append(elem)
    if not result:
        return None
    return result


# 426. Функция для извлечения элементов из стека, пока их сумма не станет больше X
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


# 427. Функция для нахождения элементов, которые меньше, чем среднее значение стека
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


# 428. Функция для нахождения элементов, которые не встречаются более одного раза в стеке
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


# 429. Функция для извлечения всех элементов стека, которые делятся на 5
def pop_elements_divisible_by_5(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 430. Функция для нахождения элементов, которые больше, чем X, и возвращения их в обратном порядке
def pop_elements_greater_than_x_reverse(stack, x):
    result = []
    while stack:
        elem = stack.pop()
        if elem > x:
            result.append(elem)
    if not result:
        return None
    return result[::-1]


# 431. Функция для удаления всех элементов, которые меньше, чем X, из стека
def remove_less_than_x(stack, x):
    result = []
    while stack:
        elem = stack.pop()
        if elem >= x:
            result.append(elem)
    if not result:
        return None
    return result


# 432. Функция для нахождения наименьшего элемента в стеке
def find_min_in_stack(stack):
    if not stack:
        return None
    min_elem = min(stack)
    return min_elem


# 433. Функция для извлечения элементов, пока не встретится число, которое делится на 6
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


# 434. Функция для нахождения всех чисел в стеке, которые являются чётными и делятся на 4
def find_even_divisible_by_4(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 2 == 0 and elem % 4 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 435. Функция для извлечения всех нечётных чисел из стека
def pop_odd_elements(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 2 != 0:
            result.append(elem)
    if not result:
        return None
    return result


# 436. Функция для нахождения всех чисел, которые меньше X, и их удаления из стека
def remove_less_than_x_v2(stack, x):
    result = []
    while stack:
        elem = stack.pop()
        if elem < x:
            result.append(elem)
    if not result:
        return None
    return result


# 437. Функция для нахождения всех чисел в стеке, которые являются квадратами целых чисел
def find_square_numbers_in_stack(stack):
    result = []
    while stack:
        elem = stack.pop()
        if (elem ** 0.5).is_integer():
            result.append(elem)
    if not result:
        return None
    return result


# 438. Функция для нахождения наибольшего элемента в стеке
def find_max_in_stack(stack):
    if not stack:
        return None
    max_elem = max(stack)
    return max_elem


# 439. Функция для извлечения всех элементов стека, которые делятся на 7
def pop_elements_divisible_by_7(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 7 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 440. Функция для нахождения всех чисел, которые больше X и делятся на 2
def find_greater_than_x_divisible_by_2(stack, x):
    result = []
    while stack:
        elem = stack.pop()
        if elem > x and elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 441. Функция для извлечения и удаления всех элементов стека, которые не делятся на 4
def remove_not_divisible_by_4(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 4 != 0:
            result.append(elem)
    if not result:
        return None
    return result


# 442. Функция для извлечения всех чисел, которые делятся на 10, из стека
def pop_elements_divisible_by_10(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 10 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 443. Функция для нахождения всех элементов стека, которые делятся на 3 и на 5
def find_divisible_by_3_and_5(stack):
    result = []
    while stack:
        elem = stack.pop()
        if elem % 3 == 0 and elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 444. Функция для удаления всех элементов стека, которые больше X
def remove_greater_than_x(stack, x):
    result = []
    while stack:
        elem = stack.pop()
        if elem <= x:
            result.append(elem)
    if not result:
        return None
    return result


# 445. Функция для извлечения и удаления всех чисел, которые больше, чем X и чётные
def pop_elements_greater_than_x_even(stack, x):
    result = []
    while stack:
        elem = stack.pop()
        if elem > x and elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 446. Функция для извлечения элементов из очереди, пока их сумма не станет больше X
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


# 447. Функция для нахождения всех элементов в очереди, которые меньше среднего
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


# 448. Функция для нахождения уникальных элементов, встречающихся только один раз в очереди
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


# 449. Функция для извлечения всех чисел, которые делятся на 5 из очереди
def process_queue_divisible_by_5(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 450. Функция для извлечения всех чисел из очереди, которые больше X
def process_queue_greater_than_x(queue, x):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem > x:
            result.append(elem)
    if not result:
        return None
    return result


# 451. Функция для извлечения всех чисел из очереди, которые делятся на 2, но не на 4
def process_queue_divisible_by_2_not_4(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem % 2 == 0 and elem % 4 != 0:
            result.append(elem)
    if not result:
        return None
    return result


# 452. Функция для нахождения всех элементов, которые делятся на 7 из очереди
def process_queue_divisible_by_7(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem % 7 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 453. Функция для извлечения и возвращения всех элементов из очереди, которые являются нечётными
def process_queue_odd_elements(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem % 2 != 0:
            result.append(elem)
    if not result:
        return None
    return result


# 454. Функция для извлечения и возвращения всех чисел, которые являются квадратами целых чисел
def process_queue_square_numbers(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if (elem ** 0.5).is_integer():
            result.append(elem)
    if not result:
        return None
    return result


# 455. Функция для извлечения всех чисел, которые делятся на 3 или на 5
def process_queue_divisible_by_3_or_5(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem % 3 == 0 or elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 456. Функция для извлечения всех чисел, которые делятся на 3, но не на 6
def process_queue_divisible_by_3_not_6(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem % 3 == 0 and elem % 6 != 0:
            result.append(elem)
    if not result:
        return None
    return result


# 457. Функция для удаления всех чисел из очереди, которые меньше, чем X
def process_queue_remove_less_than_x(queue, x):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem >= x:
            result.append(elem)
    if not result:
        return None
    return result


# 458. Функция для извлечения всех чисел, которые меньше X
def process_queue_less_than_x(queue, x):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem < x:
            result.append(elem)
    if not result:
        return None
    return result


# 459. Функция для нахождения и извлечения минимального элемента из очереди
def process_queue_min_element(queue):
    if not queue:
        return None
    min_elem = min(queue)
    queue.remove(min_elem)
    return min_elem


# 460. Функция для удаления всех элементов из очереди, которые больше X
def process_queue_remove_greater_than_x(queue, x):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem <= x:
            result.append(elem)
    if not result:
        return None
    return result


# 461. Функция для нахождения и извлечения максимального элемента из очереди
def process_queue_max_element(queue):
    if not queue:
        return None
    max_elem = max(queue)
    queue.remove(max_elem)
    return max_elem


# 462. Функция для удаления всех элементов из очереди, которые делятся на 4
def process_queue_remove_divisible_by_4(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem % 4 != 0:
            result.append(elem)
    if not result:
        return None
    return result


# 463. Функция для извлечения всех чисел, которые больше X, и делятся на 2
def process_queue_greater_than_x_and_divisible_by_2(queue, x):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem > x and elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 464. Функция для извлечения всех элементов из очереди, которые больше X и делятся на 3
def process_queue_greater_than_x_and_divisible_by_3(queue, x):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem > x and elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 465. Функция для извлечения всех элементов из очереди, которые меньше X и не делятся на 5
def process_queue_less_than_x_not_divisible_by_5(queue, x):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem < x and elem % 5 != 0:
            result.append(elem)
    if not result:
        return None
    return result


# 466. Функция для нахождения всех чисел в очереди, которые являются чётными и делятся на 4
def process_queue_even_and_divisible_by_4(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem % 2 == 0 and elem % 4 == 0:
            result.append(elem)
    if not result:
        return None
    return result


# 467. Функция для нахождения всех элементов, которые не делятся на 3 и на 5
def process_queue_not_divisible_by_3_and_5(queue):
    result = []
    while queue:
        elem = queue.pop(0)
        if elem % 3 != 0 and elem % 5 != 0:
            result.append(elem)
    if not result:
        return None
    return result


# 468. Функция для нахождения всех элементов в кортеже, которые больше X
def find_elements_greater_than_x(tpl, x):
    result = []
    for elem in tpl:
        if elem > x:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 469. Функция для извлечения всех чётных чисел из кортежа
def find_even_elements_in_tuple(tpl):
    result = []
    for elem in tpl:
        if elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 470. Функция для нахождения всех элементов, которые меньше среднего значения кортежа
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


# 471. Функция для нахождения всех элементов, которые больше X и делятся на 5
def find_elements_greater_than_x_divisible_by_5(tpl, x):
    result = []
    for elem in tpl:
        if elem > x and elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 472. Функция для извлечения элементов, которые не встречаются более одного раза в кортеже
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


# 473. Функция для нахождения чисел, которые делятся на 3 и на 4
def find_divisible_by_3_and_4(tpl):
    result = []
    for elem in tpl:
        if elem % 3 == 0 and elem % 4 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 474. Функция для извлечения всех нечётных чисел из кортежа
def find_odd_elements_in_tuple(tpl):
    result = []
    for elem in tpl:
        if elem % 2 != 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 475. Функция для нахождения минимального числа в кортеже
def find_min_in_tuple(tpl):
    if not tpl:
        return None
    return min(tpl)


# 476. Функция для нахождения максимального числа в кортеже
def find_max_in_tuple(tpl):
    if not tpl:
        return None
    return max(tpl)


# 477. Функция для нахождения чисел, которые делятся на 2 или на 5
def find_divisible_by_2_or_5(tpl):
    result = []
    for elem in tpl:
        if elem % 2 == 0 or elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 478. Функция для извлечения всех чисел, которые делятся на 6
def find_divisible_by_57(tpl):
    result = []
    for elem in tpl:
        if elem % 57 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 479. Функция для нахождения чисел, которые являются квадратами целых чисел
def find_square_numbers_in_tuple(tpl):
    result = []
    for elem in tpl:
        if (elem ** 0.5).is_integer():
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 480. Функция для нахождения чисел, которые больше X, но не делятся на 3
def find_greater_than_x_not_divisible_by_3(tpl, x):
    result = []
    for elem in tpl:
        if elem > x and elem % 3 != 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 481. Функция для нахождения всех чисел, которые больше X, и делятся на 3
def find_greater_than_x_divisible_by_3(tpl, x):
    result = []
    for elem in tpl:
        if elem > x and elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 482. Функция для нахождения чисел, которые не делятся на 4 и на 5
def find_not_divisible_by_4_and_5(tpl):
    result = []
    for elem in tpl:
        if elem % 4 != 0 and elem % 5 != 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 483. Функция для нахождения чисел, которые меньше X, но делятся на 3
def find_less_than_x_divisible_by_3(tpl, x):
    result = []
    for elem in tpl:
        if elem < x and elem % 3 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 484. Функция для нахождения чисел, которые делятся на 2 и на 5
def find_divisible_by_2_and_5(tpl):
    result = []
    for elem in tpl:
        if elem % 2 == 0 and elem % 5 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 485. Функция для нахождения чисел, которые не являются квадратами целых чисел
def find_not_square_numbers_in_tuple(tpl):
    result = []
    for elem in tpl:
        if not (elem ** 0.5).is_integer():
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 486. Функция для нахождения чисел, которые делятся на 2 и на 7
def find_divisible_by_2_and_7(tpl):
    result = []
    for elem in tpl:
        if elem % 2 == 0 and elem % 7 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 487. Функция для нахождения чисел, которые меньше X и являются нечётными
def find_less_than_x_odd(tpl, x):
    result = []
    for elem in tpl:
        if elem < x and elem % 2 != 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 488. Функция для нахождения всех чисел, которые больше X и являются чётными
def find_greater_than_x_even(tpl, x):
    result = []
    for elem in tpl:
        if elem > x and elem % 2 == 0:
            result.append(elem)
    if not result:
        return None
    return tuple(result)


# 489. Функция для получения уникальных элементов из списка с помощью множества
def unique_elements_from_list(lst):
    if not lst:
        return None
    unique_elements = set(lst)
    return tuple(unique_elements)


# 490. Функция для нахождения пересечения двух списков
def intersection_of_lists_2(lst1, lst2):
    result = list(set(lst1) & set(lst2))
    if not result:
        return None
    return result


# 491. Функция для объединения двух словарей, если они не содержат одинаковых ключей
def merge_dicts_no_common_keys(d1, d2):
    if any(k in d2 for k in d1):
        return None
    merged_dict = {**d1, **d2}
    return merged_dict


# 492. Функция для переворота строки
def reverse_string_3(s):
    if not s:
        return None
    return s[::-1]


# 493. Функция для нахождения всех чисел, которые являются делителями числа X
def divisors_of_x(x):
    if x <= 0:
        return None
    divisors = []
    for i in range(2, x):
        if x % i == 0:
            divisors.append(i)
    if not divisors:
        return None
    return divisors


# 494. Функция для подсчёта количества вхождений каждого элемента в список
def count_elements_in_list(lst):
    if not lst:
        return None
    count_dict = {}
    for elem in lst:
        count_dict[elem] = count_dict.get(elem, 0) + 1
    return count_dict


# 495. Функция для создания словаря из списка пар (ключ, значение)
def list_to_dict_2(lst):
    if not lst or len(lst) % 2 != 0:
        return None
    return dict(zip(lst[::2], lst[1::2]))


# 496. Функция для подсчёта чётных и нечётных чисел в списке
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


# 497. Функция для извлечения всех гласных из строки
def extract_vowels_from_string(s):
    if not s:
        return None
    vowels = "aeiouAEIOU"
    result = [ch for ch in s if ch in vowels]
    if not result:
        return None
    return ''.join(result)


# 498. Функция для слияния двух отсортированных списков в один отсортированный
def merge_sorted_lists(lst1, lst2):
    if not lst1 and not lst2:
        return None
    return sorted(lst1 + lst2)


# 499. Функция для проверки, является ли строка палиндромом
def is_palindrome_2(s):
    if not s:
        return None
    return s == s[::-1]


# 500. Функция для нахождения наибольшего общего делителя двух чисел
def gcd_of_two_numbers(a, b):
    if a <= 0 or b <= 0:
        return None
    while b:
        a, b = b, a % b
    return a


# 501. Функция для нахождения всех простых чисел в диапазоне от 1 до X
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
    return primes


# 502. Функция для вычисления факториала числа
def factorial_of_number(n):
    if n < 0:
        return None
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


# 503. Функция для подсчёта всех слов в строке
def count_words_in_string(s):
    if not s:
        return None
    return len(s.split())


# 504. Функция для нахождения всех индексов вхождения элемента в список
def find_all_indices_of_element(lst, element):
    if not lst:
        return None
    indices = [i for i, x in enumerate(lst) if x == element]
    if not indices:
        return None
    return indices


# 505. Функция для нахождения всех чисел, которые являются квадратами из списка
def square_numbers_from_list(lst):
    if not lst:
        return None
    squares = [x for x in lst if (x ** 0.5).is_integer()]
    if not squares:
        return None
    return squares


# 506. Функция для извлечения всех чисел, которые больше среднего значения
def greater_than_average(lst):
    if not lst:
        return None
    average = sum(lst) / len(lst)
    result = [x for x in lst if x > average]
    if not result:
        return None
    return result


# 507. Функция для сортировки списка строк по длине
def sort_strings_by_length(lst):
    if not lst:
        return None
    return sorted(lst, key=len)


# 508. Функция для нахождения суммы всех чисел в списке
def sum_of_elements(lst):
    if not lst:
        return None
    return sum(lst)


# 509. Функция для нахождения максимальной строки по длине из списка строк
def longest_string(lst):
    if not lst:
        return None
    return max(lst, key=len)


# 510. Функция для нахождения разницы между двумя множествами
def difference_between_sets(set1, set2):
    if not set1 or not set2:
        return None
    return set1 - set2


# 511. Функция для нахождения всех элементов, которые присутствуют в одном из двух списков
def union_of_lists(lst1, lst2):
    if not lst1 and not lst2:
        return None
    return sorted(list(set(lst1) | set(lst2)))


# 512. Функция для нахождения всех элементов, которые присутствуют в обоих списках
def intersection_of_lists_3(lst1, lst2):
    if not lst1 and not lst2:
        return None
    return sorted(list(set(lst1) & set(lst2)))


# 513. Функция для проверки, является ли строка цифрой
def is_digit(s):
    if not s:
        return None
    return s.isdigit()


# 514. Функция для извлечения всех буквенных символов из строки
def extract_letters_from_string(s):
    if not s:
        return None
    result = ''.join([ch for ch in s if ch.isalpha()])
    return result


# 515. Функция для нахождения всех элементов, которые являются строками в списке
def find_all_strings_in_list(lst):
    if not lst:
        return None
    return [x for x in lst if isinstance(x, str)]


# 516. Функция для проверки, все ли элементы в списке уникальны
def all_unique(lst):
    if not lst:
        return None
    return len(lst) == len(set(lst))


# 517. Функция для объединения всех элементов строки в единую строку с разделителями
def join_elements_with_separator(lst, separator):
    if not lst:
        return None
    return separator.join(lst)


# 518. Функция для нахождения разницы между двумя списками (без повторений)
def difference_between_lists(lst1, lst2):
    if not lst1 and not lst2:
        return None
    return sorted(list(set(lst1) - set(lst2)))


# 519. Функция для подсчёта всех вхождений подстроки в строку без пересечения
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
        i += len(substring)
    return count


# 520. Функция для нахождения всех слов, которые начинаются с определенной буквы
def find_words_starting_with(s, letter):
    if not s or not letter:
        return None
    words = s.split()
    result = [word for word in words if word[0].lower() == letter.lower()]
    return result if result else None


# 521. Функция для проверки, является ли строка анаграммой другой строки
def are_anagrams_2(s1, s2):
    if not s1 or not s2:
        return None
    return sorted(s1) == sorted(s2)


# 522. Функция для извлечения всех чисел, расположенных в строке
def extract_numbers_from_string_2(s):
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


# 523. Функция для проверки, является ли строка палиндромом (с учётом пробелов)
def is_palindrome_with_spaces(s):
    if not s:
        return None
    clean_s = ''.join(s.split()).lower()
    return clean_s == clean_s[::-1]


# 524. Функция для подсчёта количества гласных и согласных в строке
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


# 525. Функция для удаления всех пробелов в строке, а затем инвертирования
def remove_spaces_and_reverse(s):
    if not s:
        return None
    no_spaces = s.replace(" ", "")
    return no_spaces[::-1]


# 526. Функция для нахождения подстроки с максимальной длиной без повторяющихся символов
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


# 527. Функция для нахождения наибольшего общего префикса двух строк
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


# 528. Функция для подсчёта повторяющихся слов в строке
def count_repeating_words(s):
    if not s:
        return None
    words = s.split()
    word_count = {}
    for word in words:
        word_count[word.lower()] = word_count.get(word.lower(), 0) + 1
    return {word: count for word, count in word_count.items() if count > 1}


# 529. Функция для нахождения самого длинного слова в строке
def longest_word_in_string(s):
    if not s:
        return None
    words = s.split()
    return max(words, key=len) if words else None


# 530. Функция для извлечения подстрок длиной N
def extract_substrings_of_length_n(s, n):
    if not s or n <= 0:
        return None
    return [s[i:i + n] for i in range(len(s) - n + 1)]


# 531. Функция для удаления всех слов, которые начинаются на определённую букву
def remove_words_starting_with(s, letter):
    if not s or not letter:
        return None
    words = s.split()
    filtered_words = [word for word in words if not word.lower().startswith(letter.lower())]
    return ' '.join(filtered_words) if filtered_words else None


# 532. Функция для замены всех пробелов на подчеркивания
def replace_spaces_with_underscores(s):
    if not s:
        return None
    return s.replace(" ", "_")


# 533. Функция для извлечения всех буквенных символов и их сортировки по алфавиту
def sort_letters_in_string(s):
    if not s:
        return None
    letters = [ch for ch in s if ch.isalpha()]
    letters.sort()
    return ''.join(letters)


# 534. Функция для удаления всех чисел из строки
def remove_numbers_from_string(s):
    if not s:
        return None
    return ''.join([ch for ch in s if not ch.isdigit()])


# 535. Функция для нахождения всех вхождений строки с учётом регистра
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


# 536. Функция для удаления всех гласных из строки
def remove_vowels_from_string(s):
    if not s:
        return None
    vowels = "aeiouAEIOU"
    return ''.join([ch for ch in s if ch not in vowels])


# 537. Функция для вычисления расстояния Левенштейна между двумя строками
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
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[len_s1][len_s2]


# 538. Функция для нахождения всех возможных подстрок строки заданной длины
def fixed_length_substrings(s, length):
    if not s or length <= 0:
        return None
    return [s[i:i + length] for i in range(len(s) - length + 1)]


# 539. Функция для удаления всех дублирующихся символов в строке
def remove_duplicates_from_string(s):
    if not s:
        return None
    return ''.join(sorted(set(s), key=s.index))


# 540. Функция для нахождения среднего арифметического с плавающими точками
def average_of_floats(lst):
    def sum_of_floats(lst):
        total = 0.0
        for num in lst:
            if isinstance(num, (int, float)):
                total += num
            else:
                return None
        return total
    if not lst:
        return None
    total = sum_of_floats(lst)
    if total is None:
        return None
    return total / len(lst)


# 541. Функция для нахождения наибольшего числа с плавающей точкой в списке
def max_float(lst):
    if not lst:
        return None
    max_val = float('-inf')
    for num in lst:
        if isinstance(num, (int, float)) and num > max_val:
            max_val = num
    return max_val if max_val != float('-inf') else None


# 542. Функция для нахождения наименьшего числа с плавающей точкой в списке
def min_float(lst):
    if not lst:
        return None
    min_val = float('inf')
    for num in lst:
        if isinstance(num, (int, float)) and num < min_val:
            min_val = num
    return min_val if min_val != float('inf') else None


# 543. Функция для проверки, является ли число с плавающей точкой положительным
def is_positive_float(x):
    if not isinstance(x, (int, float)):
        return None
    return x > 0


# 544. Функция для нахождения разницы между двумя числами с плавающей точкой
def difference_between_floats(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return None
    return abs(x - y)


# 545. Функция для нахождения произведения всех чисел в списке с плавающими точками
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


# 546. Функция для деления двух чисел с плавающей точкой с учётом ошибок деления на ноль
def divide_floats(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return None
    if y == 0:
        return None
    return x / y


# 547. Функция для нахождения квадратного корня числа с плавающей точкой
def square_root(x):
    if not isinstance(x, (int, float)) or x < 0:
        return None
    return x ** 0.5


# 548. Функция для округления числа с плавающей точкой до ближайшего целого
def round_to_nearest_integer(x):
    if not isinstance(x, (int, float)):
        return None
    return round(x)


# 549. Функция для нахождения всех чисел, которые делятся на X с плавающей точкой
def divisible_by_x(lst, x):
    if not isinstance(x, (int, float)) or x == 0 or not lst:
        return None
    result = []
    for num in lst:
        if isinstance(num, (int, float)) and num % x == 0:
            result.append(num)
    return result if result else None


# 550. Функция для вычисления значения экспоненты для числа с плавающей точкой
def exponentiation_of_float(x, n):
    if not isinstance(x, (int, float)) or not isinstance(n, (int, float)):
        return None
    return x ** n


# 551. Функция для вычисления факториала числа с плавающей точкой (для целых чисел)
def factorial_of_float(x):
    if not isinstance(x, int) or x < 0:
        return None
    factorial = 1
    for i in range(1, x + 1):
        factorial *= i
    return factorial


# 552. Функция для нахождения медианы в списке чисел с плавающей точкой
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


# 553. Функция для нахождения всех чисел, которые являются простыми с плавающей точкой
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

    result = [x for x in lst if isinstance(x, int) and is_prime(x)]
    return result if result else None


# 554. Функция для нахождения всех чисел в диапазоне от X до Y с плавающей точкой
def numbers_in_range(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return None
    return [i for i in range(int(x), int(y) + 1)]


# 555. Функция для нахождения геометрической прогрессии
def geometric_progression(a, r, n):
    if not isinstance(a, (int, float)) or not isinstance(r, (int, float)) or not isinstance(n, int) or n <= 0:
        return None
    result = [a * (r ** i) for i in range(n)]
    return result if result else None


# 556. Функция для нахождения суммы всех чисел в геометрической прогрессии
def sum_of_geometric_progression(a, r, n):
    if not isinstance(a, (int, float)) or not isinstance(r, (int, float)) or not isinstance(n, int) or n <= 0:
        return None
    if r == 1:
        return a * n
    return a * (1 - r ** n) / (1 - r)


# 557. Функция для нахождения квадрата числа с плавающей точкой
def square_of_float(x):
    if not isinstance(x, (int, float)):
        return None
    return x * x


# 558. Функция для вычисления суммы ряда с плавающими числами (арифметическая прогрессия)
def sum_of_arithmetic_progression(a, d, n):
    if not isinstance(a, (int, float)) or not isinstance(d, (int, float)) or not isinstance(n, int) or n <= 0:
        return None
    return n * (2 * a + (n - 1) * d) / 2


# 559. Функция для нахождения всех чисел, которые не равны нулю в списке с плавающими точками
def non_zero_floats(lst):
    if not lst:
        return None
    return [x for x in lst if isinstance(x, (int, float)) and x != 0]


# 560. Функция для нахождения чисел, квадрат которых больше заданного значения
def squares_greater_than(lst, value):
    if not isinstance(value, (int, float)) or not lst:
        return None
    return [x for x in lst if isinstance(x, (int, float)) and x ** 2 > value]


# 561. Функция для нахождения всех чисел, которые меньше заданного значения
def less_than_value(lst, value):
    if not isinstance(value, (int, float)) or not lst:
        return None
    return [x for x in lst if isinstance(x, (int, float)) and x < value]


# 562. Функция для нахождения суммы квадратов чисел в списке
def sum_of_squares_2(lst):
    if not lst:
        return None
    return sum(x ** 2 for x in lst if isinstance(x, (int, float)))


# 563. Функция для нахождения разности между максимальным и минимальным числом, но только для положительных чисел
def positive_max_min_difference(lst):
    if not lst:
        return None
    positive_numbers = [x for x in lst if isinstance(x, (int, float)) and x > 0]
    if not positive_numbers:
        return None
    return max(positive_numbers) - min(positive_numbers)


# 564. Функция для нахождения разности между максимальным и минимальным числом, но только для отрицательных чисел
def negative_max_min_difference(lst):
    if not lst:
        return None
    negative_numbers = [x for x in lst if isinstance(x, (int, float)) and x < 0]
    if not negative_numbers:
        return None
    return max(negative_numbers) - min(negative_numbers)


# 565. Функция для нахождения суммы всех чисел, которые делятся на X без остатка
def sum_of_divisible_by_x(lst, x):
    if not isinstance(x, (int, float)) or x == 0 or not lst:
        return None
    return sum(x for x in lst if isinstance(x, (int, float)) and x % x == 0)


# 566. Функция для нахождения всех чисел, которые являются кубами
def cubes(lst):
    if not lst:
        return None
    return [x for x in lst if isinstance(x, (int, float)) and round(x ** (1 / 3), 6) ** 3 == x]


# 567. Функция для нахождения чисел, которые могут быть представлены как сумма двух квадратов
def sum_of_two_squares_3(lst):
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


# 568. Функция для проверки, является ли число с плавающей точкой степенью двойки
def is_power_of_two(x):
    if not isinstance(x, (int, float)) or x <= 0:
        return False
    return (x & (x - 1)) == 0


# 569. Функция для нахождения всех чисел, которые являются целыми числами
def integers_in_float_list(lst):
    if not lst:
        return None
    return [x for x in lst if isinstance(x, (int, float)) and x.is_integer()]


# 570. Функция для нахождения суммы всех чисел, которые можно выразить как произведение двух простых чисел
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
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0 and is_prime(i) and is_prime(num // i):
                    result.append(num)
                    break
    return sum(result) if result else None


# 571. Функция для нахождения всех чисел, которые равны разности двух квадратов
def difference_of_two_squares(lst):
    if not lst:
        return None
    result = []
    for num in lst:
        if isinstance(num, int) and num > 0:
            for a in range(1, int(num ** 0.5) + 1):
                if num % a == 0:
                    b = num // a
                    if (a + b) % 2 == 0 and (b - a) % 2 == 0:
                        result.append(num)
                        break
    return result if result else None


# 572. Функция для нахождения всех чисел, которые являются степенями 3 (кубами)
def cubes_of_numbers(lst):
    if not lst:
        return None
    return [x for x in lst if isinstance(x, (int, float)) and round(x ** (1 / 3), 6) ** 3 == x]


# 573. Функция для нахождения среднего арифметического квадратов чисел
def average_of_squares(lst):
    if not lst:
        return None
    return sum(x ** 2 for x in lst if isinstance(x, (int, float))) / len(lst)


# 574. Функция для вычисления факториала числа (рекурсия)
def factorial_2(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_2(n - 1)


# 575. Функция для вычисления суммы чисел от 1 до N (рекурсия)
def sum_to_n(n):
    if n <= 0:
        return 0
    return n + sum_to_n(n - 1)


# 576. Функция для нахождения N-го числа Фибоначчи (рекурсия)
def fibonacci_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_2(n - 1) + fibonacci_2(n - 2)


# 577. Функция для вычисления степени числа (рекурсия)
def power_2(base, exp):
    if exp <= 0:
        return 1
    return base * power_2(base, exp - 1)


# 578. Функция для нахождения суммы элементов списка (рекурсия)
def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])


# 579. Функция для нахождения произведения элементов списка (рекурсия)
def recursive_product(lst):
    if not lst:
        return 1
    return lst[0] * recursive_product(lst[1:])


# 580. Функция для нахождения максимального числа в списке (рекурсия)
def recursive_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        sub_max = recursive_max(lst[1:])
        return lst[0] if lst[0] > sub_max else sub_max


# 581. Функция для нахождения минимального числа в списке (рекурсия)
def recursive_min(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        sub_min = recursive_min(lst[1:])
        return lst[0] if lst[0] < sub_min else sub_min


# 582. Функция для инвертирования строки (рекурсия)
def reverse_string_2(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string_2(s[:-1])


# 583. Функция для проверки, является ли строка палиндромом (рекурсия)
def is_palindrome_4(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_4(s[1:-1])


# 584. Функция для нахождения НОД (наибольший общий делитель) двух чисел (рекурсия)
def gsd_2(a, b):
    if b == 0:
        return a
    return gsd_2(b, a % b)


# 585. Функция для подсчета количества вхождений элемента в списке (рекурсия)
def count_occurrences_3(lst, x):
    if not lst:
        return 0
    return (1 if lst[0] == x else 0) + count_occurrences_3(lst[1:], x)


# 586. Функция для проверки, является ли число простым (рекурсия)
def is_prime_4(n, divisor=None):
    if n <= 1:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime_4(n, divisor - 1)


# 587. Функция для нахождения наибольшего элемента в дереве (рекурсия)
def find_max_in_tree(tree):
    if tree is None:
        return float('-inf')
    left_max = find_max_in_tree(tree.get('left'))
    right_max = find_max_in_tree(tree.get('right'))
    return max(tree.get('value', float('-inf')), left_max, right_max)


# 588. Функция для проверки, является ли число четным (рекурсия)
def is_even_2(n):
    if n < 0:
        n = abs(n)
    if n == 0:
        return True
    if n == 1:
        return False
    return is_even_2(n - 2)


# 589. Функция для вычисления суммы чисел, меньших X в списке (рекурсия)
def sum_less_than_x(lst, x):
    if not lst:
        return 0
    return (lst[0] if lst[0] < x else 0) + sum_less_than_x(lst[1:], x)


# 590. Функция для вычисления факториала числа с использованием хвоста (рекурсия с аккумулятором)
def factorial_tail(n, acc=1):
    if n == 0 or n == 1:
        return acc
    return factorial_tail(n - 1, acc * n)


# 591. Функция для вычисления суммы чисел в диапазоне от 1 до N, но с шагом 2 (рекурсия)
def sum_with_step(n):
    if n <= 0:
        return 0
    return n + sum_with_step(n - 2)


# 592. Функция для нахождения всех чисел Фибоначчи до N (рекурсия)
def fibonacci_up_to_n(n, a=0, b=1):
    if a > n:
        return []
    return [a] + fibonacci_up_to_n(n, b, a + b)


# 593. Функция для нахождения чисел, которые делятся на X, используя рекурсию
def find_divisible(lst, x):
    if not lst:
        return []
    return ([lst[0]] if lst[0] % x == 0 else []) + find_divisible(lst[1:], x)


# 594. Функция для подсчета количества четных чисел в списке (рекурсия)
def count_even(lst):
    if not lst:
        return 0
    return (1 if lst[0] % 2 == 0 else 0) + count_even(lst[1:])


# 595. Функция для подсчета количества отрицательных чисел в списке (рекурсия)
def count_negatives(lst):
    if not lst:
        return 0
    return (1 if lst[0] < 0 else 0) + count_negatives(lst[1:])


# 596. Функция для нахождения всех чисел в списке, которые больше среднего значения (рекурсия)
def greater_than_average_3(lst, avg=None):
    if not lst:
        return []
    if avg is None:
        avg = sum(lst) / len(lst)
    return ([lst[0]] if lst[0] > avg else []) + greater_than_average_3(lst[1:], avg)


# 597. Функция для нахождения суммы чисел, которые больше X в списке (рекурсия)
def sum_greater_than_x(lst, x):
    if not lst:
        return 0
    return (lst[0] if lst[0] > x else 0) + sum_greater_than_x(lst[1:], x)


# 598. Функция для нахождения длины строки (рекурсия)
def string_length(s):
    if s == "":
        return 0
    return 1 + string_length(s[1:])


# 599. Функция для подсчета количества четных чисел в диапазоне от 1 до N (рекурсия)
def count_evens_in_range(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return 1 + count_evens_in_range(n - 1)
    return count_evens_in_range(n - 1)


# 600. Функция для вычисления суммы чисел, которые находятся в пределах заданного диапазона (рекурсия)
def sum_in_range(lst, low, high):
    if not lst:
        return 0
    return (lst[0] if low <= lst[0] <= high else 0) + sum_in_range(lst[1:], low, high)


# 601. Функция для нахождения произведения чисел, которые меньше X в списке (рекурсия)
def product_less_than_x(lst, x):
    if not lst:
        return 1
    return (lst[0] if lst[0] < x else 1) * product_less_than_x(lst[1:], x)


# 602. Функция для нахождения суммы всех чисел в строке, которые можно преобразовать в числа (рекурсия)
def sum_of_numbers_in_string(s, current_num=None):
    if s == "":
        return 0
    if current_num is None:
        current_num = ""
    if s[0].isdigit():
        current_num += s[0]
    elif current_num:
        return int(current_num) + sum_of_numbers_in_string(s[1:], current_num)
    return sum_of_numbers_in_string(s[1:], current_num)


# 603. Функция для нахождения всех четных чисел в строке, которые можно преобразовать в числа (рекурсия)
def even_numbers_in_string(s, current_num=None):
    if s == "":
        return []
    if current_num is None:
        current_num = ""
    if s[0].isdigit():
        current_num += s[0]
    elif current_num:
        num = int(current_num)
        if num % 2 == 0:
            return [num] + even_numbers_in_string(s[1:], current_num)
        return even_numbers_in_string(s[1:], current_num)
    return even_numbers_in_string(s[1:], current_num)


# 604. Функция для добавления элемента в кольцевой массив с ограничением размера
def append_to_ring(arr, element, max_size=10):
    if len(arr) >= max_size:
        arr.pop(0)
    arr.append(element)
    if len(arr) > max_size:
        arr = arr[1:]
    return arr


# 605. Функция для нахождения индекса элемента в кольцевом массиве с возможностью обрабатывать отсутствующие элементы
def find_in_ring(arr, element):
    if not arr:
        return None
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return None


# 606. Функция для нахождения всех индексов в кольцевом массиве, где встречается заданный элемент
def find_all_in_ring(arr, element):
    if not arr:
        return []
    indices = []
    n = len(arr)
    for i in range(n):
        if arr[i] == element:
            indices.append(i)
    return indices


# 607. Функция для циклического сдвига элементов в кольцевом массиве с шагом, который может быть отрицательным
def rotate_with_negativity(arr, steps):
    if not arr:
        return arr
    n = len(arr)
    if steps == 0:
        return arr
    if steps < 0:
        steps = steps % n
        rotated = arr[steps:] + arr[:steps]
    else:
        steps = steps % n
        rotated = arr[-steps:] + arr[:-steps]
    return rotated


# 608. Функция для увеличения всех элементов кольцевого массива на заданное число
def increase_ring_elements(arr, value):
    if not arr:
        return arr
    return [x + value for x in arr]


# 609. Функция для уменьшения всех элементов кольцевого массива на заданное число
def decrease_ring_elements(arr, value):
    if not arr:
        return arr
    return [x - value for x in arr]


# 610. Функция для умножения всех элементов кольцевого массива на заданное число
def multiply_ring_elements(arr, value):
    if not arr:
        return arr
    return [x * value for x in arr]


# 611. Функция для нахождения суммы элементов в кольцевом массиве
def sum_ring(arr):
    if not arr:
        return 0
    return sum(arr)


# 612. Функция для нахождения среднего значения элементов кольцевого массива
def average_ring(arr):
    if not arr:
        return None
    return sum(arr) / len(arr)


# 613. Функция для нахождения максимального элемента кольцевого массива
def max_ring(arr):
    if not arr:
        return None
    return max(arr)


# 614. Функция для нахождения минимального элемента кольцевого массива
def min_ring(arr):
    if not arr:
        return None
    return min(arr)


# 615. Функция для проверки, содержится ли хотя бы одно положительное число в кольцевом массиве
def has_positive_ring(arr):
    if not arr:
        return False
    for x in arr:
        if x > 0:
            return True
    return False


# 616. Функция для проверки, содержится ли хотя бы одно отрицательное число в кольцевом массиве
def has_negative_ring(arr):
    if not arr:
        return False
    for x in arr:
        if x < 0:
            return True
    return False


# 617. Функция для инвертирования элементов в кольцевом массиве, если они находятся в четных индексах
def reverse_even_index_elements(arr):
    if not arr:
        return arr
    n = len(arr)
    result = arr[:]
    for i in range(0, n, 2):
        result[i] = arr[n - 1 - i]
    return result


# 618. Функция для нахождения четных чисел в кольцевом массиве
def find_even_ring(arr):
    if not arr:
        return []
    return [x for x in arr if x % 2 == 0]


# 619. Функция для нахождения нечетных чисел в кольцевом массиве
def find_odd_ring(arr):
    if not arr:
        return []
    return [x for x in arr if x % 2 != 0]


# 620. Функция для подсчета количества четных чисел в кольцевом массиве
def count_even_ring(arr):
    if not arr:
        return 0
    return sum(1 for x in arr if x % 2 == 0)


# 621. Функция для подсчета количества нечетных чисел в кольцевом массиве
def count_odd_ring(arr):
    if not arr:
        return 0
    return sum(1 for x in arr if x % 2 != 0)


# 622. Функция для добавления элемента в кольцевой массив только если он еще не существует
def append_unique_ring(arr, element):
    if element not in arr:
        arr.append(element)
    return arr


# 623. Функция для нахождения всех элементов кольцевого массива, которые делятся на X
def find_divisible_ring(arr, x):
    if not arr:
        return []
    return [el for el in arr if el % x == 0]


# 624. Функция для удаления всех элементов, которые меньше заданного числа
def remove_less_than_ring(arr, threshold):
    if not arr:
        return arr
    return [x for x in arr if x >= threshold]


# 625. Функция для очистки кольцевого массива от элементов, больших заданного числа
def remove_greater_than_ring(arr, threshold):
    if not arr:
        return arr
    return [x for x in arr if x <= threshold]


# 626. Функция для преобразования строки в список символов, с проверкой на пустоту
def string_to_list(s):
    if s == "":
        return []
    return list(s)


# 627. Функция для объединения двух списков без повторений
def merge_unique_lists(list1, list2):
    return sorted(list(set(list1 + list2)))


# 628. Функция для создания множества из строк, игнорируя регистр
def set_from_strings_ignore_case(strings):
    return sorted({s.lower() for s in strings})


# 629. Функция для подсчета количества вхождений каждого символа в строку
def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


# 630. Функция для проверки, является ли строка палиндромом
def is_palindrome_5(s):
    cleaned = ''.join(e for e in s if e.isalnum()).lower()
    return cleaned == cleaned[::-1]


# 631. Функция для вычисления факториала числа с использованием рекурсии
def factorial_4(n):
    if n == 0:
        return 1
    return n * factorial_4(n - 1)


# 632. Функция для подсчета числа всех вхождений слова в тексте
def count_word_occurrences(text, word):
    words = text.split()
    count = 0
    for w in words:
        if w == word:
            count += 1
    return count


# 633. Функция для фильтрации строк, которые содержат только цифры
def filter_numeric_strings(strings):
    return [s for s in strings if s.isdigit()]


# 634. Функция для поиска ближайшего к числу в списке
def closest_number(arr, num):
    if not arr:
        return None
    closest = arr[0]
    for x in arr:
        if abs(x - num) < abs(closest - num):
            closest = x
    return closest


# 635. Функция для сортировки списка словарей по заданному ключу
def sort_dicts_by_key(lst, key):
    return sorted(lst, key=lambda x: x.get(key, 0))


# 636. Функция для поиска наибольшего общего делителя двух чисел
def gcd_5(a, b):
    while b:
        a, b = b, a % b
    return a


# 637. Функция для вычисления среднего арифметического элементов списка с защитой от деления на 0
def average_6(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


# 638. Функция для преобразования строки в формат "заглавными и маленькими буквами"
def alternate_case(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])


# 639. Функция для подсчета, сколько раз встречается каждый элемент в списке
def count_elements(arr):
    counts = {}
    for el in arr:
        counts[el] = counts.get(el, 0) + 1
    return counts


# 640. Функция для преобразования списка в строку через разделитель
def list_to_string(lst, separator=","):
    return separator.join(map(str, lst))


# 641. Функция для извлечения уникальных элементов из списка с сохранением порядка
def unique_elements_6(arr):
    seen = set()
    result = []
    for el in arr:
        if el not in seen:
            result.append(el)
            seen.add(el)
    return result


# 642. Функция для поиска строки в тексте с учетом возможных пробелов
def find_word_in_text(text, word):
    index = text.find(word)
    if index != -1:
        return f"Word found at index {index}"
    return "Word not found"


# 643. Функция для определения, является ли строка числом (целым или с плавающей точкой)
def is_number_5(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# 644. Функция для объединения двух словарей, при этом значения по одинаковым ключам складываются
def merge_dicts_6(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result


# 645. Функция для извлечения элементов с четными индексами из списка
def even_index_elements(arr):
    return [arr[i] for i in range(0, len(arr), 2)]


# 646. Функция для инвертирования словаря (меняем местами ключи и значения)
def invert_dict(d):
    return {v: k for k, v in d.items()}


# 647. Функция для слияния двух отсортированных списков в один отсортированный
def merge_sorted_lists_5(list1, list2):
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


# 648. Функция для замены каждого второго символа в строке на звездочку
def replace_second_char(s):
    return ''.join([c if i % 2 == 0 else '*' for i, c in enumerate(s)])


# 649. Функция для получения уникальных чисел из списка с их суммой
def unique_numbers_and_sum(lst):
    seen = set()
    unique_numbers = []
    for num in lst:
        if num not in seen:
            unique_numbers.append(num)
            seen.add(num)
    total = sum(unique_numbers)
    return unique_numbers, total


# 650. Функция для проверки, является ли строка правильным email
def is_valid_email_2(email):
    if "@" not in email or "." not in email:
        return False
    username, domain = email.split("@", 1)
    if not username or not domain:
        return False
    return True


# 651. Функция для подсчета всех слов в строке с учётом знаков препинания
def count_words_in_string_2(s):
    words = s.split()
    return len(words)


# 652. Функция для нахождения максимального числа в списке с проверкой на пустоту
def max_in_list(lst):
    if not lst:
        return None
    return max(lst)


# 653. Функция для преобразования строки в список чисел, разделенных запятой
def string_to_numbers_2(s):
    return [int(x) for x in s.split(",") if x.strip().isdigit()]


# 654. Функция для вычисления степени числа с обработкой возможных ошибок
def power_5(base, exponent):
    try:
        return base ** exponent
    except TypeError:
        return "Invalid input"


# 655. Функция для генерации списка всех чисел от 1 до N, которые делятся на X
def divisible_by_x_5(n, x):
    return [i for i in range(1, n + 1) if i % x == 0]


# 656. Функция для вычисления длины строки, игнорируя пробелы
def length_without_spaces(s):
    return len(s.replace(" ", ""))


# 657. Функция для проверки, является ли строка числом в десятичной системе
def is_decimal(s):
    try:
        float(s)
        return '.' in s
    except ValueError:
        return False


# 658. Функция для изменения регистра в строках, включая те, которые начинаются с пробела
def change_case_and_strip(s):
    return s.strip().upper() if s.startswith(" ") else s.lower()


# 659. Функция для нахождения индекса первого отрицательного числа в списке
def find_first_negative(arr):
    if not arr:
        return None
    for i in range(len(arr)):
        if arr[i] < 0:
            return i
    return None


# 660. Функция для удаления всех повторяющихся элементов из списка, сохраняя порядок
def remove_duplicates_5(arr):
    if not arr:
        return arr
    seen = set()
    result = []
    for el in arr:
        if el not in seen:
            result.append(el)
            seen.add(el)
    return result


# 661. Функция для проверки, является ли строка числом с плавающей точкой
def is_float_5(s):
    try:
        float(s)
        return "." in s
    except ValueError:
        return False


# 662. Функция для извлечения всех слов из строки, содержащих цифры
def extract_words_with_numbers(s):
    if not s:
        return []
    words = s.split()
    result = []
    for word in words:
        if any(char.isdigit() for char in word):
            result.append(word)
    return result


# 663. Функция для нахождения наименьшего общего кратного двух чисел
def lcm_4(a, b):
    if a == 0 or b == 0:
        return 0
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1


# 664. Функция для объединения двух списков с уникальными значениями
def merge_unique_lists_2(arr1, arr2):
    result = arr1.copy()
    for el in arr2:
        if el not in result:
            result.append(el)
    return result


# 665. Функция для возврата индекса элемента в списке, если он существует, или None
def find_index_of_element(arr, element):
    if not arr:
        return None
    for i, el in enumerate(arr):
        if el == element:
            return i
    return None


# 666. Функция для подсчета всех слов в строке с учетом разделителей
def count_words_in_string_with_delimiters(s, delimiters=" "):
    if not s:
        return 0
    for delimiter in delimiters:
        s = s.replace(delimiter, " ")
    return len(s.split())


# 667. Функция для нахождения всех чисел больше среднего в списке
def greater_than_average_6(arr):
    if not arr:
        return []
    avg = sum(arr) / len(arr)
    return [x for x in arr if x > avg]


# 668. Функция для объединения словаря и списка кортежей в новый словарь
def merge_dict_and_tuple(lst, d):
    if not lst:
        return d
    for key, value in lst:
        d[key] = value
    return d


# 669. Функция для вычисления суммы всех чисел в строке
def sum_numbers_in_string_2(s):
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


# 670. Функция для нахождения числа, которое не встречается в двух списках
def find_missing_number(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    missing = set1 - set2
    if missing:
        return sorted(missing, reverse=True)[0]
    return None


# 671. Функция для слияния двух строк с их чередующимися символами
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


# 672. Функция для проверки, все ли элементы в списке больше заданного числа
def are_all_greater_than(arr, number):
    if not arr:
        return False
    return all(x > number for x in arr)


# 673. Функция для поиска и замены первого вхождения подстроки в строке
def replace_first_occurrence(s, old, new):
    if old not in s:
        return s
    index = s.find(old)
    return s[:index] + new + s[index + len(old):]


# 674. Функция для получения уникальных элементов из списка, исключая те, которые повторяются
def get_unique_elements(arr):
    if not arr:
        return []
    count = {}
    for el in arr:
        count[el] = count.get(el, 0) + 1
    return [key for key, value in count.items() if value == 1]


# 675. Функция для нахождения минимального четного числа в списке
def min_even_number(arr):
    if not arr:
        return None
    even_numbers = [x for x in arr if x % 2 == 0]
    if even_numbers:
        return min(even_numbers)
    return None


# 676. Функция для преобразования числа в строку с ведущими нулями
def number_to_string_with_leading_zeros(n, width):
    return str(n).zfill(width)


# 677. Функция для преобразования списка чисел в строку с разделением на запятую
def list_to_comma_separated_string(arr):
    if not arr:
        return ""
    return ", ".join(map(str, arr))


# 678. Функция для проверки, является ли строка правильным числом (целым или с плавающей точкой)
def is_valid_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# 679. Функция для подсчета гласных букв в строке
def count_vowels_2(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


# 680. Функция для вычисления произведения всех чисел в строке
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


# 681. Функция для поиска всех строк в списке, содержащих хотя бы одну цифру
def find_strings_with_digits(arr):
    return [s for s in arr if any(char.isdigit() for char in s)]


# 682. Функция для вычисления числа цифр в строке
def count_digits_in_string(s):
    return sum(1 for char in s if char.isdigit())


# 683. Функция для получения каждого второго элемента в строке
def get_every_second_char(s):
    return s[::2]


# 684. Функция для фильтрации строк, содержащих хотя бы одну заглавную букву
def filter_strings_with_uppercase(arr):
    return [s for s in arr if any(char.isupper() for char in s)]


# 685. Функция для подсчета повторений каждого символа в строке, кроме пробела
def count_non_space_characters(s):
    count = {}
    for char in s:
        if char != " ":
            count[char] = count.get(char, 0) + 1
    return count


# 686. Функция для поиска строки с максимальной длиной в списке
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


# 687. Функция для нахождения индекса первого четного числа в списке
def find_first_even(arr):
    if not arr:
        return None
    for i, num in enumerate(arr):
        if num % 2 == 0:
            return i
    return None


# 688. Функция для вычисления суммы всех чисел в строке
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


# 689. Функция для преобразования строки в список чисел (каждое число отделено пробелом)
def string_to_number_list(s):
    if not s:
        return []
    num_list = s.split()
    try:
        return [int(num) for num in num_list]
    except ValueError:
        return None


# 690. Функция для поиска максимального и минимального элемента в списке
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


# 691. Функция для замены всех пробелов на подчеркивания в строке
def replace_spaces_with_underscores_5(s):
    if not s:
        return None
    result = ""
    for char in s:
        if char == " ":
            result += "_"
        else:
            result += char
    return result


# 692. Функция для удаления дубликатов из списка, не изменяя порядок
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


# 693. Функция для поиска первого числа в списке, которое делится на заданное число
def find_first_multiple(arr, divisor):
    if not arr or divisor == 0:
        return None
    for num in arr:
        if num % divisor == 0:
            return num
    return None


# 694. Функция для проверки, является ли строка полиндромом, игнорируя пробелы и регистр
def is_palindrome_v2(s):
    if not s:
        return False
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


# 695. Функция для получения всех четных чисел из списка
def get_even_numbers(arr):
    if not arr:
        return []
    even_numbers = []
    for num in arr:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


# 696. Функция для проверки, является ли строка числом (целым или с плавающей точкой)
def is_number_v2(s):
    if not s:
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False


# 697. Функция для подсчета всех повторяющихся элементов в списке
def count_repeating_elements(arr):
    if not arr:
        return {}
    counts = {}
    for el in arr:
        counts[el] = counts.get(el, 0) + 1
    return {key: value for key, value in counts.items() if value > 1}


# 698. Функция для извлечения уникальных слов из строки
def extract_unique_words(s):
    if not s:
        return []
    words = s.split()
    unique_words = set(words)
    return sorted(list(unique_words))


# 699. Функция для нахождения наибольшего простого числа в списке
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


# 700. Функция для извлечения всех цифр из строки
def extract_digits(s):
    if not s:
        return []
    digits = [int(c) for c in s if c.isdigit()]
    return digits


# 701. Функция для поиска всех слов в строке, длина которых больше 3 символов
def find_long_words(s):
    if not s:
        return []
    words = s.split()
    long_words = [word for word in words if len(word) > 3]
    return long_words


# 702. Функция для получения всех чисел в строке, разделенных запятыми
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


# 703. Функция для нахождения всех чисел в списке, которые больше заданного числа
def find_numbers_greater_than(arr, n):
    if not arr:
        return []
    greater_numbers = []
    for num in arr:
        if num > n:
            greater_numbers.append(num)
    return greater_numbers


# 704. Функция для объединения списка строк в одну строку с разделителями
def join_strings_with_separator(arr, separator):
    if not arr:
        return ""
    result = arr[0]
    for string in arr[1:]:
        result += separator + string
    return result


# 705. Функция для вычисления суммы всех четных чисел в списке
def sum_even_numbers(arr):
    if not arr:
        return 0
    total = 0
    for num in arr:
        if num % 2 == 0:
            total += num
    return total


# 706. Функция для нахождения первой строки, содержащей заданное слово
def find_string_with_word(arr, word):
    if not arr or not word:
        return None
    for s in arr:
        if word in s:
            return s
    return None


# 707. Функция для нахождения наименьшего нечетного числа в списке
def find_smallest_odd(arr):
    if not arr:
        return None
    odd_numbers = [x for x in arr if x % 2 != 0]
    if odd_numbers:
        return min(odd_numbers)
    return None


# 708. Функция для замены всех вхождений подстроки на другую подстроку
def replace_substring(s, old_sub, new_sub):
    if not s or not old_sub:
        return s
    count = 0
    result = ""
    i = 0
    while i < len(s):
        if s[i:i + len(old_sub)] == old_sub:
            result += new_sub
            i += len(old_sub)
            count += 1
        else:
            result += s[i]
            i += 1
    if count == 0:
        return None
    return result


# 709. Функция для нахождения первого элемента списка, который делится на 3 и на 5
def find_divisible_by_3_and_5_5(arr):
    if not arr:
        return None
    for num in arr:
        if num % 3 == 0 and num % 5 == 0:
            return num
    return None


# 710. Функция для вычисления среднего арифметического элементов списка
def calculate_average(arr):
    if not arr:
        return None
    total = sum(arr)
    count = len(arr)
    return total / count


# 711. Функция для объединения двух списков в один и удаления повторяющихся элементов
def combine_and_unique(arr1, arr2):
    if not arr1 and not arr2:
        return []
    combined = arr1 + arr2
    unique = []
    for el in combined:
        if el not in unique:
            unique.append(el)
    return unique


# 712. Функция для выбора наибольшего числа из трех
def choose_largest(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c
    if a == b and a > c:
        return a
    if b == c and b > a:
        return b
    return a


# 713. Функция для выбора максимальной длины строки из нескольких
def choose_longest_string(*strings):
    longest = ""
    for s in strings:
        if len(s) > len(longest):
            longest = s
        elif len(s) == len(longest):
            if s > longest:
                longest = s
    return longest


# 714. Функция для выбора наиболее часто встречающегося элемента в списке
def choose_most_frequent(arr):
    freq = {}
    for elem in arr:
        if elem in freq:
            freq[elem] += 1
        else:
            freq[elem] = 1
    max_count = 0
    most_frequent = None
    for key, value in freq.items():
        if value > max_count:
            most_frequent = key
            max_count = value
        elif value == max_count:
            if key > most_frequent:
                most_frequent = key
    return most_frequent


# 715. Функция для выбора минимального значения из нескольких чисел
def choose_smallest(*nums):
    smallest = None
    for num in nums:
        if smallest is None or num < smallest:
            smallest = num
    return smallest


# 716. Функция для выбора строки, содержащей наибольшее количество гласных
def choose_string_with_most_vowels(*strings):
    vowels = 'aeiouAEIOU'
    max_vowels = 0
    chosen_string = ""
    for s in strings:
        count_vowels = sum(1 for char in s if char in vowels)
        if count_vowels > max_vowels:
            max_vowels = count_vowels
            chosen_string = s
        elif count_vowels == max_vowels and s > chosen_string:
            chosen_string = s
    return chosen_string


# 717. Функция для выбора наименьшего четного числа
def choose_smallest_even(*nums):
    smallest_even = None
    for num in nums:
        if num % 2 == 0:
            if smallest_even is None or num < smallest_even:
                smallest_even = num
    if smallest_even is None:
        return "No even numbers"
    return smallest_even


# 718. Функция для выбора числа с наибольшей разницей с другими числами
def choose_number_with_max_diff(*nums):
    max_diff = 0
    chosen_num = None
    for num in nums:
        diff = sum(abs(num - x) for x in nums)
        if diff > max_diff:
            max_diff = diff
            chosen_num = num
    return chosen_num


# 719. Функция для выбора строки, которая начинается с гласной
def choose_string_starting_with_vowel(*strings):
    vowels = 'aeiouAEIOU'
    for s in strings:
        if s[0] in vowels:
            return s
    return "No string starts with a vowel"


# 720. Функция для выбора второго наибольшего числа
def choose_second_largest(*nums):
    unique_nums = list(set(nums))
    unique_nums.sort(reverse=True)
    if len(unique_nums) < 2:
        return "Not enough distinct numbers"
    return unique_nums[1]


# 721. Функция для выбора минимального элемента из списка, если он четный
def choose_smallest_even_from_list(arr):
    smallest_even = None
    for num in arr:
        if num % 2 == 0:
            if smallest_even is None or num < smallest_even:
                smallest_even = num
    if smallest_even is None:
        return "No even numbers found"
    return smallest_even


# 722. Функция для выбора самого длинного слова, не начинающегося на гласную
def choose_longest_non_vowel_word(*words):
    vowels = 'aeiouAEIOU'
    longest = ""
    for word in words:
        if word[0] not in vowels:
            if len(word) > len(longest):
                longest = word
    if not longest:
        return "No word found"
    return longest


# 723. Функция для выбора наименьшего отрицательного числа
def choose_smallest_negative(*nums):
    smallest_negative = None
    for num in nums:
        if num < 0:
            if smallest_negative is None or num > smallest_negative:
                smallest_negative = num
    if smallest_negative is None:
        return "No negative numbers"
    return smallest_negative


# 724. Функция для выбора строки, которая содержит наибольшее количество цифр
def choose_string_with_most_digits(*strings):
    max_digits = 0
    chosen_string = ""
    for s in strings:
        count_digits = sum(1 for char in s if char.isdigit())
        if count_digits > max_digits:
            max_digits = count_digits
            chosen_string = s
        elif count_digits == max_digits and s > chosen_string:
            chosen_string = s
    return chosen_string


# 725. Функция для выбора наибольшего числа в пределах диапазона
def choose_largest_in_range(low, high, *nums):
    largest_in_range = None
    for num in nums:
        if low <= num <= high:
            if largest_in_range is None or num > largest_in_range:
                largest_in_range = num
    if largest_in_range is None:
        return f"No numbers in the range ({low}, {high})"
    return largest_in_range


# 726. Функция для выбора первого четного числа в списке
def choose_first_even_number(arr):
    for num in arr:
        if num % 2 == 0:
            return num
    return "No even numbers"


# 727. Функция для выбора самой короткой строки, не содержащей пробелы
def choose_shortest_no_space_string(*strings):
    shortest = None
    for s in strings:
        if ' ' not in s:
            if shortest is None or len(s) < len(shortest):
                shortest = s
    if shortest is None:
        return "No string without spaces"
    return shortest


# 728. Функция для выбора самого младшего возраста в группе
def choose_youngest_age(*ages):
    youngest = None
    for age in ages:
        if youngest is None or age < youngest:
            youngest = age
    return youngest


# 729. Функция для выбора строки с наибольшим количеством уникальных символов
def choose_string_with_most_unique_chars(*strings):
    max_unique = 0
    chosen_string = ""
    for s in strings:
        unique_chars = len(set(s))
        if unique_chars > max_unique:
            max_unique = unique_chars
            chosen_string = s
    return chosen_string


# 730. Функция для выбора первого четного числа, которое делится на 3
def choose_first_even_divisible_by_three(arr):
    for num in arr:
        if num % 2 == 0 and num % 3 == 0:
            return num
    return "No even number divisible by 3"


# 731. Функция для выбора максимального числа, которое меньше заданного
def choose_largest_less_than(value, *nums):
    largest = None
    for num in nums:
        if num < value:
            if largest is None or num > largest:
                largest = num
    if largest is None:
        return f"No numbers less than {value}"
    return largest


# 732. Функция для выбора первого числа, которое больше заданного
def choose_first_greater_than(value, *nums):
    for num in nums:
        if num > value:
            return num
    return f"No numbers greater than {value}"


# 733. Функция для выбора строки, длина которой делится на 3
def choose_string_with_length_divisible_by_three(*strings):
    for s in strings:
        if len(s) % 3 == 0:
            return s
    return "No string with length divisible by 3"


# 734. Функция для выбора самого дорогого товара в списке
def choose_most_expensive_item(*items):
    max_price = 0
    most_expensive = None
    for item in items:
        price = item['price']
        if price > max_price:
            max_price = price
            most_expensive = item
    return most_expensive if most_expensive else "No items found"


# 735. Функция для выбора строки, длина которой меньше заданного числа
def choose_string_shorter_than(length, *strings):
    for s in strings:
        if len(s) < length:
            return s
    return None


# 736. Функция для выбора первого числа, которое не делится на 2 и 3
def choose_first_not_divisible_by_2_and_3(arr):
    for num in arr:
        if num % 2 != 0 and num % 3 != 0:
            return num
    return None


# 737. Функция для выбора первого слова, в котором все буквы – гласные
def choose_word_with_only_vowels(*words):
    vowels = 'aeiouAEIOU'
    for word in words:
        if all(char in vowels for char in word):
            return word
    return None


# 738. Функция для выбора самого большого числа в списке, которое не превышает заданное значение
def choose_largest_less_than_or_equal_to(value, *nums):
    largest = None
    for num in nums:
        if num <= value:
            if largest is None or num > largest:
                largest = num
    return largest if largest is not None else None


# 739. Функция для выбора самой длинной строки, состоящей только из цифр
def choose_longest_digit_string(*strings):
    longest = None
    for s in strings:
        if s.isdigit():
            if longest is None or len(s) > len(longest):
                longest = s
    return longest if longest is not None else None


# 740. Функция для выбора самой короткой строки, в которой нет гласных
def choose_shortest_string_without_vowels(*strings):
    vowels = 'aeiouAEIOU'
    shortest = None
    for s in strings:
        if all(char not in vowels for char in s):
            if shortest is None or len(s) < len(shortest):
                shortest = s
    return shortest if shortest is not None else None


# 741. Функция для выбора наибольшего четного числа, которое меньше заданного
def choose_largest_even_less_than(value, *nums):
    largest = None
    for num in nums:
        if num % 2 == 0 and num < value:
            if largest is None or num > largest:
                largest = num
    return largest if largest is not None else None


# 742. Функция для выбора второго самого маленького числа
def choose_second_smallest(*nums):
    unique_nums = list(set(nums))
    unique_nums.sort()
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]


# 743. Функция для выбора строки, которая начинается и заканчивается на одну и ту же букву
def choose_string_start_and_end_same(*strings):
    for s in strings:
        if s[0] == s[-1]:
            return s
    return None


# 744. Функция для выбора первого числа, которое делится на 5 и 7
def choose_first_divisible_by_5_and_7(arr):
    for num in arr:
        if num % 5 == 0 and num % 7 == 0:
            return num
    return None


# 745. Функция для выбора самой короткой строки, содержащей хотя бы одну цифру
def choose_shortest_string_with_digit(*strings):
    for s in strings:
        if any(char.isdigit() for char in s):
            return s
    return None


# 746. Функция для выбора самой дорогой покупки, не превышающей заданную цену
def choose_most_expensive_below_price(limit, *items):
    max_price = None
    most_expensive = None
    for item in items:
        if item['price'] <= limit:
            if max_price is None or item['price'] > max_price:
                most_expensive = item
                max_price = item['price']
    return most_expensive if most_expensive else None


# 747. Функция для выбора первого числа, которое является квадратом числа
def choose_first_square_number(arr):
    for num in arr:
        if int(num ** 0.5) ** 2 == num:
            return num
    return None


# 748. Функция для выбора самого старшего возраста среди людей
def choose_oldest_age(*ages):
    oldest = None
    for age in ages:
        if oldest is None or age > oldest:
            oldest = age
    return oldest if oldest is not None else None


# 749. Функция для выбора первого числа, которое делится на 2, но не на 3
def choose_first_divisible_by_2_not_3(arr):
    for num in arr:
        if num % 2 == 0 and num % 3 != 0:
            return num
    return None


# 750. Функция для выбора самой длинной строки, в которой все символы – цифры
def choose_longest_all_digits_string(*strings):
    longest = None
    for s in strings:
        if s.isdigit():
            if longest is None or len(s) > len(longest):
                longest = s
    return longest if longest is not None else None


# 751. Функция для выбора первого четного числа, которое больше заданного
def choose_first_even_greater_than(value, *nums):
    for num in nums:
        if num % 2 == 0 and num > value:
            return num
    return None


# 752. Функция для выбора первой строки, которая не является числом
def choose_first_non_numeric_string(*strings):
    for s in strings:
        if not s.isdigit():
            return s
    return None


# 753. Функция для выбора строки, которая является палиндромом
def choose_palindrome(*strings):
    for s in strings:
        if s == s[::-1]:
            return s
    return None


# 754. Функция для выбора самой дорогой покупки, которая не дороже 100
def choose_most_expensive_under_100(*items):
    max_price = None
    most_expensive = None
    for item in items:
        if item['price'] <= 100:
            if max_price is None or item['price'] > max_price:
                most_expensive = item
                max_price = item['price']
    return most_expensive if most_expensive else None


# 755. Функция для выбора самого первого четного числа, которое больше 10
def choose_first_even_greater_than_10(arr):
    for num in arr:
        if num % 2 == 0 and num > 10:
            return num
    return None


# 756. Функция для выбора самого маленького числа, которое делится на 5
def choose_smallest_divisible_by_5(*nums):
    smallest = None
    for num in nums:
        if num % 5 == 0:
            if smallest is None or num < smallest:
                smallest = num
    return smallest if smallest is not None else None


# 757. Функция для выбора первого слова с длиной больше 5, которое начинается с согласной
def choose_first_long_word_starting_with_consonant(*words):
    vowels = 'aeiouAEIOU'
    for word in words:
        if len(word) > 5 and word[0] not in vowels:
            return word
    return None


# 758. Функция для выбора самого большого числа, которое меньше чем 20
def choose_largest_less_than_20(*nums):
    largest = None
    for num in nums:
        if num < 20:
            if largest is None or num > largest:
                largest = num
    return largest if largest is not None else None


# 759. Функция для выбора строки, которая начинается с заглавной буквы
def choose_string_starting_with_uppercase(*strings):
    for s in strings:
        if s[0].isupper():
            return s
    return None


# 760. Функция для выбора первого числа, которое не является ни четным, ни простым
def choose_first_non_even_non_prime(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for num in arr:
        if num % 2 != 0 and not is_prime(num):
            return num
    return None


# 761. Функция для выбора самой короткой строки, которая начинается с цифры
def choose_shortest_string_starting_with_digit(*strings):
    for s in strings:
        if s[0].isdigit():
            return s
    return None


# 762. Функция для выбора строки, которая является анаграммой другой строки
def choose_anagram_of(string, *strings):
    sorted_string = sorted(string)
    for s in strings:
        if sorted(s) == sorted_string:
            return s
    return None


# 763. Функция для выбора наименьшего числа, которое больше заданного
def choose_smallest_greater_than(value, *nums):
    smallest = None
    for num in nums:
        if num > value:
            if smallest is None or num < smallest:
                smallest = num
    return smallest if smallest is not None else None


# 764. Функция для выбора первого слова, которое имеет четное количество букв
def choose_first_even_length_word(*words):
    for word in words:
        if len(word) % 2 == 0:
            return word
    return None


# 765. Функция для выбора строки, длина которой больше средней длины всех строк
def choose_longer_than_average(*strings):
    avg_length = sum(len(s) for s in strings) / len(strings) if strings else 0
    for s in strings:
        if len(s) > avg_length:
            return s
    return None


# 766. Функция для выбора строки, которая содержит только буквы
def choose_string_with_only_letters(*strings):
    for s in strings:
        if s.isalpha():
            return s
    return None


# 767. Функция для выбора самого старого возраста, который меньше 30
def choose_oldest_under_30(*ages):
    oldest = None
    for age in ages:
        if age < 30:
            if oldest is None or age > oldest:
                oldest = age
    return oldest if oldest is not None else None


# 768. Функция для выбора числа, которое является кратным 4, но не кратным 5
def choose_multiple_of_4_not_5(arr):
    for num in arr:
        if num % 4 == 0 and num % 5 != 0:
            return num
    return None


# 769. Функция для выбора строки, длина которой кратна 3
def choose_string_length_divisible_by_3(*strings):
    for s in strings:
        if len(s) % 3 == 0:
            return s
    return None


# 770. Функция для выбора наименьшего числа, которое является четным и больше 10
def choose_smallest_even_greater_than_10(*nums):
    smallest = None
    for num in nums:
        if num % 2 == 0 and num > 10:
            if smallest is None or num < smallest:
                smallest = num
    return smallest if smallest is not None else None


# 771. Функция для выбора первого числа, которое делится на 2 и 5
def choose_first_divisible_by_2_and_5(arr):
    for num in arr:
        if num % 2 == 0 and num % 5 == 0:
            return num
    return None


# 772. Функция для выбора самой длинной строки, которая не начинается с цифры
def choose_longest_non_digit_starting_string(*strings):
    for s in strings:
        if not s[0].isdigit():
            return s
    return None


# 773. Функция для выбора первого слова, которое состоит только из заглавных букв
def choose_first_all_uppercase_word(*words):
    for word in words:
        if word.isupper():
            return word
    return None


# 774. Функция для выбора самого младшего возраста среди людей старше 50 лет
def choose_youngest_over_50(*ages):
    youngest = None
    for age in ages:
        if age > 50:
            if youngest is None or age < youngest:
                youngest = age
    return youngest if youngest is not None else None


# 775. Функция для выбора наибольшего числа, которое делится на 3, но не на 2
def choose_largest_multiple_of_3_not_2(arr):
    largest = None
    for num in arr:
        if num % 3 == 0 and num % 2 != 0:
            if largest is None or num > largest:
                largest = num
    return largest if largest is not None else None


# 776. Функция для выбора строки, содержащей хотя бы одну заглавную букву и цифру
def choose_string_with_uppercase_and_digit(*strings):
    for s in strings:
        if any(char.isdigit() for char in s) and any(char.isupper() for char in s):
            return s
    return None


# 777. Функция для выбора первого четного числа, которое меньше 50
def choose_first_even_less_than_50(arr):
    for num in arr:
        if num % 2 == 0 and num < 50:
            return num
    return None


# 778. Функция для выбора самой короткой строки, которая не содержит пробела
def choose_shortest_no_space_string_3(*strings):
    for s in strings:
        if " " not in s:
            return s
    return None


# 779. Функция для выбора строки, которая является повторением другого слова
def choose_repeated_string(*strings):
    for s in strings:
        if len(s) % 2 == 0:
            half = len(s) // 2
            if s[:half] == s[half:]:
                return s
    return None


# 780. Функция для выбора числа, которое больше 0, но не больше 100
def choose_number_in_range_0_100(*nums):
    for num in nums:
        if 0 < num <= 100:
            return num
    return None


# 781. Функция для выбора самого младшего числа, которое является нечётным
def choose_smallest_odd_number(*nums):
    smallest_odd = None
    for num in nums:
        if num % 2 != 0:
            if smallest_odd is None or num < smallest_odd:
                smallest_odd = num
    return smallest_odd if smallest_odd is not None else None


# 782. Функция для выбора первого элемента списка, который больше 100 и четный
def choose_first_greater_than_100_even(arr):
    for num in arr:
        if num > 100 and num % 2 == 0:
            return num
    return None


# 783. Функция для выбора самого длинного слова, содержащее только цифры
def choose_longest_digit_word(*words):
    longest = None
    for word in words:
        if word.isdigit():
            if longest is None or len(word) > len(longest):
                longest = word
    return longest if longest is not None else None


# 784. Функция для проверки, является ли число простым, используя множество
def is_prime_using_set(n):
    if n < 2:
        return False
    factors = set()
    for i in range(1, n + 1):
        if n % i == 0:
            factors.add(i)
    return len(factors) == 2


# 785. Функция для подсчета чисел, которые кратны заданному числу в списке
def count_multiples_of(num, arr):
    count = 0
    for val in arr:
        if val % num == 0:
            count += 1
    return count if count > 0 else None


# 786. Функция для нахождения числа, которое делится на все элементы множества
def find_divisible_by_all_in_set(num_set, num):
    for divisor in num_set:
        if num % divisor != 0:
            return None
    return num


# 787. Функция для поиска первого числа, которое не встречается в словаре
def find_number_not_in_dict(d, num):
    for key in d:
        if key == num:
            return None
    return num


# 788. Функция для нахождения максимального числа в списке, которое делится на заданное
def find_max_divisible(arr, divisor):
    max_val = None
    for num in arr:
        if num % divisor == 0:
            if max_val is None or num > max_val:
                max_val = num
    return max_val if max_val is not None else None


# 789. Функция для получения всех чисел, которые не делятся на 2, 3 и 5, используя список
def find_not_divisible_by_2_3_5(arr):
    result = []
    for num in arr:
        if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
            result.append(num)
    return result if result else None


# 790. Функция для нахождения суммы всех элементов множества, больших заданного числа
def sum_of_elements_greater_than(n, num_set):
    total = 0
    for num in num_set:
        if num > n:
            total += num
    return total if total > 0 else None


# 791. Функция для нахождения максимальной разницы между числами в словаре
def max_difference_in_dict(d):
    if len(d) < 2:
        return None
    values = list(d.values())
    max_val = max(values)
    min_val = min(values)
    return max_val - min_val


# 792. Функция для вычисления среднего значения всех элементов множества
def average_of_set(num_set):
    if not num_set:
        return None
    total = 0
    for num in num_set:
        total += num
    return total / len(num_set)


# 793. Функция для нахождения всех чисел, которые больше заданного числа и не делятся на 2
def find_greater_than_and_not_divisible_by_2(arr, num):
    result = []
    for value in arr:
        if value > num and value % 2 != 0:
            result.append(value)
    return result if result else None


# 794. Функция для нахождения минимального числа, которое делится на все элементы списка
def find_min_divisible_by_all(arr):
    min_val = None
    for num in arr:
        if all(num % val == 0 for val in arr):
            if min_val is None or num < min_val:
                min_val = num
    return min_val if min_val is not None else None


# 795. Функция для нахождения самого маленького ключа в словаре, где значения больше заданного
def find_smallest_key_greater_than(d, value):
    smallest_key = None
    for key, val in d.items():
        if val > value:
            if smallest_key is None or key < smallest_key:
                smallest_key = key
    return smallest_key if smallest_key is not None else None


# 796. Функция для нахождения первого числа, которое больше заданного и является квадратом
def find_first_square_greater_than(arr, num):
    for val in arr:
        if num < val == int(val ** 0.5) ** 2:
            return val
    return None


# 797. Функция для нахождения первого числа, которое делится на 2 и на 3, используя множества
def find_first_divisible_by_2_and_3(num_set):
    for num in num_set:
        if num % 2 == 0 and num % 3 == 0:
            return num
    return None


# 798. Функция для нахождения числа, которое встречается в обоих списках
def find_common_in_lists(arr1, arr2):
    for val in arr1:
        if val in arr2:
            return val
    return None


# 799. Функция для нахождения наименьшего числа, которое является четным и больше заданного
def find_smallest_even_greater_than(arr, num):
    smallest = None
    for val in arr:
        if val > num and val % 2 == 0:
            if smallest is None or val < smallest:
                smallest = val
    return smallest if smallest is not None else None


# 800. Функция для нахождения элемента множества, который больше заданного
def find_element_greater_than_in_set(num_set, value):
    for num in num_set:
        if num > value:
            return num
    return None


# 801. Функция для вычисления суммы всех чисел, делящихся на 3 или на 5, используя список
def sum_divisible_by_3_or_5(arr):
    total = 0
    for val in arr:
        if val % 3 == 0 or val % 5 == 0:
            total += val
    return total if total > 0 else None


# 802. Функция для нахождения самого большого числа в словаре
def find_max_value_in_dict(d):
    if not d:
        return None
    max_val = None
    for key, val in d.items():
        if max_val is None or val > max_val:
            max_val = val
    return max_val


# 803. Функция для нахождения числа, которое встречается в массиве более одного раза
def find_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None


# 804. Функция для нахождения минимального числа, которое не делится на 4
def find_min_not_divisible_by_4(arr):
    min_val = None
    for val in arr:
        if val % 4 != 0:
            if min_val is None or val < min_val:
                min_val = val
    return min_val if min_val is not None else None


# 805. Функция для нахождения наименьшего числа, которое делится на 7 и на 11
def find_smallest_divisible_by_7_and_11(arr):
    min_val = None
    for val in arr:
        if val % 7 == 0 and val % 11 == 0:
            if min_val is None or val < min_val:
                min_val = val
    return min_val if min_val is not None else None


# 806. Функция для нахождения первого числа, которое делится на 3, но не на 5
def find_first_divisible_by_3_not_5(arr):
    for val in arr:
        if val % 3 == 0 and val % 5 != 0:
            return val
    return None


# 807. Функция для нахождения суммы всех элементов в словаре, значения которых больше 10
def sum_values_greater_than_10_in_dict(d):
    total = 0
    for key, val in d.items():
        if val > 10:
            total += val
    return total if total > 0 else None


# 808. Функция для нахождения строки, длина которой больше заданного числа
def find_string_longer_than(length, *strings):
    for s in strings:
        if len(s) > length:
            return s
    return None


# 809. Функция для проверки, является ли строка палиндромом
def is_palindrome_6(s):
    if not s:
        return None
    reversed_s = ''
    for i in range(len(s) - 1, -1, -1):
        reversed_s += s[i]
    if s == reversed_s:
        return True
    return False


# 810. Функция для подсчета количества гласных в строке
def count_vowels_in_string(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count if count > 0 else None


# 811. Функция для поиска первого вхождения подстроки в строку
def find_first_occurrence_of_substring(s, substring):
    for i in range(len(s) - len(substring) + 1):
        if s[i:i + len(substring)] == substring:
            return i
    return None


# 812. Функция для удаления всех пробелов в строке
def remove_spaces_from_string(s):
    result = ''
    for char in s:
        if char != ' ':
            result += char
    return result if result != s else None


# 813. Функция для получения всех уникальных символов в строке
def get_unique_characters(s):
    unique_chars = set()
    for char in s:
        unique_chars.add(char)
    return ''.join(unique_chars)


# 814. Функция для инвертирования строки
def reverse_string_5(s):
    reversed_str = ''
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str


# 815. Функция для подсчета количества слов в строке
def count_words_in_string_5(s):
    words = s.split()
    return len(words) if len(words) > 0 else None


# 816. Функция для получения строки с удаленными знаками препинания
def remove_punctuation_from_string(s):
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    result = ''
    for char in s:
        if char not in punctuation:
            result += char
    return result


# 817. Функция для проверки, состоит ли строка только из цифр
def is_string_only_digits(s):
    for char in s:
        if not char.isdigit():
            return False
    return True


# 818. Функция для получения индексов всех вхождений подстроки
def find_all_occurrences_of_substring(s, substring):
    indices = []
    for i in range(len(s) - len(substring) + 1):
        if s[i:i + len(substring)] == substring:
            indices.append(i)
    return indices if indices else None


# 819. Функция для получения строки, которая является повторением самой себя
def repeat_string(s, n):
    return s * n if n > 0 else None


# 820. Функция для получения первого слова в строке
def get_first_word(s):
    if not s:
        return None
    return s.split()[0]


# 821. Функция для получения всех чисел из строки
def extract_numbers_from_string_4(s):
    numbers = []
    temp = ''
    for char in s:
        if char.isdigit():
            temp += char
        elif temp:
            numbers.append(int(temp))
            temp = ''
    if temp:
        numbers.append(int(temp))
    return numbers if numbers else None


# 822. Функция для проверки, является ли строка буквой
def is_string_single_letter(s):
    return len(s) == 1 and s.isalpha()


# 823. Функция для получения строки с заглавными буквами
def get_uppercase_letters(s):
    uppercase = ''
    for char in s:
        if char.isupper():
            uppercase += char
    return uppercase if uppercase else None


# 824. Функция для удаления всех символов, которые встречаются в строке более одного раза
def remove_duplicates_from_string_2(s):
    result = ''
    seen = set()
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result


# 825. Функция для нахождения всех подстрок заданной длины
def find_substrings_of_length(s, length):
    substrings = []
    for i in range(len(s) - length + 1):
        substrings.append(s[i:i + length])
    return substrings if substrings else None


# 826. Функция для нахождения самой длинной буквы в строке
def find_longest_alphabetic_char(s):
    longest = ''
    for char in s:
        if char.isalpha() and len(char) > len(longest):
            longest = char
    return longest if longest else None


# 827. Функция для поиска самой частой буквы в строке
def find_most_frequent_char(s):
    frequency = {}
    for char in s:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    most_frequent = max(frequency, key=frequency.get, default=None)
    return most_frequent


# 828. Функция для разделения строки на части по символу
def split_string_by_char(s, char):
    parts = []
    temp = ''
    for c in s:
        if c == char:
            if temp:
                parts.append(temp)
                temp = ''
        else:
            temp += c
    if temp:
        parts.append(temp)
    return parts if parts else None


# 829. Функция для замены всех цифр на символ `*`
def replace_digits_with_asterisks(s):
    result = ''
    for char in s:
        if char.isdigit():
            result += '*'
        else:
            result += char
    return result


# 830. Функция для нахождения всех подстрок, начинающихся на заглавную букву
def find_substrings_starting_with_uppercase(s):
    substrings = []
    temp = ''
    for char in s:
        if char.isupper() and temp:
            substrings.append(temp)
            temp = ''
        temp += char
    if temp:
        substrings.append(temp)
    return substrings if substrings else None


# 831. Функция для преобразования строки в список символов
def string_to_list_of_chars(s):
    return list(s) if s else None


# 832. Функция для поиска самого длинного слова в строке
def find_longest_word(s):
    words = s.split()
    if not words:
        return None
    return max(words, key=len)


# 833. Функция для нахождения строки, которая является комбинацией двух других
def is_combination_of_two(s, s1, s2):
    return s == s1 + s2


# 834. Функция для проверки, является ли строка числовой
def is_numeric_string(s):
    return s.isdigit() if s else False


# 835. Функция для подсчета всех слов в строке, начинающихся с гласной
def count_words_starting_with_vowel(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for word in s.split():
        if word[0] in vowels:
            count += 1
    return count if count > 0 else None


# 836. Функция для нахождения всех слов длиной больше 3 символов
def find_words_longer_than_3(s):
    words = s.split()
    result = [word for word in words if len(word) > 3]
    return result if result else None


# 837. Функция для удаления всех гласных в строке
def remove_vowels_from_string_2(s):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in s:
        if char not in vowels:
            result += char
    return result if result != s else None


# 838. Функция для замены всех пробелов на подчеркивания
def replace_spaces_with_underscores_6(s):
    return s.replace(' ', '_') if s else None


# 839. Функция для нахождения всех цифр в строке
def find_digits_in_string(s):
    digits = ''
    for char in s:
        if char.isdigit():
            digits += char
    return digits if digits else None


# 840. Функция для подсчета всех букв в строке
def count_letters_in_string(s):
    count = 0
    for char in s:
        if char.isalpha():
            count += 1
    return count if count > 0 else None


# 841. Функция для нахождения первой заглавной буквы в строке
def find_first_uppercase_letter(s):
    for char in s:
        if char.isupper():
            return char
    return None


# 842. Функция для преобразования строки в обратный порядок
def reverse_string_in_place(s):
    result = ''
    for char in reversed(s):
        result += char
    return result


# 843. Функция для замены всех заглавных букв на строчные
def convert_upper_to_lower(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char.lower()
        else:
            result += char
    return result


# 844. Функция для нахождения всех букв, которые встречаются более одного раза
def find_repeated_chars(s):
    count = {}
    repeated = ''
    for char in s:
        if char.isalpha():
            count[char] = count.get(char, 0) + 1
    for char, cnt in count.items():
        if cnt > 1:
            repeated += char
    return repeated if repeated else None


# 845. Функция для нахождения всех символов, которые не являются буквами
def find_non_alphabetic_chars(s):
    result = ''
    for char in s:
        if not char.isalpha():
            result += char
    return result if result else None


# 846. Функция для конкатенации списка строк
def concatenate_strings_from_list(lst):
    result = ''
    for s in lst:
        result += s
    return result


# 847. Функция для поиска строки с минимальной длиной
def find_min_length_string(lst):
    if not lst:
        return None
    min_string = lst[0]
    for s in lst:
        if len(s) < len(min_string):
            min_string = s
    return min_string


# 848. Функция для замены всех символов на их позицию в алфавите
def replace_with_alphabet_position(s):
    result = ''
    for char in s:
        if char.isalpha():
            result += str(ord(char.lower()) - 96)
        else:
            result += char
    return result


# 849. Функция для нахождения всех делителей числа
def find_divisors(n):
    if n == 0:
        return None
    divisors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors if divisors else None


# 850. Функция для проверки, является ли число простым
def is_prime_66(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 851. Функция для нахождения суммы цифр числа
def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


# 852. Функция для умножения числа на его собственные цифры
def multiply_by_digits(n):
    n = abs(n)
    result = 1
    while n > 0:
        digit = n % 10
        if digit != 0:
            result *= digit
        n //= 10
    return result if result != 1 else None


# 853. Функция для нахождения максимальной цифры в числе
def max_digit_in_number(n):
    n = abs(n)
    max_digit = -1
    while n > 0:
        digit = n % 10
        if digit > max_digit:
            max_digit = digit
        n //= 10
    return max_digit if max_digit != -1 else None


def count_even_numbers_5(lst):
    def is_odd(n):
        if n % 2 != 0:
            return True
        return False
    count = 0
    for n in lst:
        if not is_odd(n):
            count += 1
    return count if count > 0 else None


# 854. Функция для нахождения наибольшего числа, которое делится на 3 в списке
def find_largest_divisible_by_3(lst):
    largest = None
    for n in lst:
        if n % 3 == 0 and (largest is None or n > largest):
            largest = n
    return largest


# 855. Функция для нахождения наименьшего числа, которое делится на 5 в списке
def find_smallest_divisible_by_5(lst):
    smallest = None
    for n in lst:
        if n % 5 == 0 and (smallest is None or n < smallest):
            smallest = n
    return smallest


# 856. Функция для нахождения произведения всех чисел в списке
def multiply_all_numbers(lst):
    if not lst:
        return None
    result = 1
    for n in lst:
        result *= n
    return result


# 857. Функция для нахождения количества чисел, которые больше заданного порога
def count_numbers_greater_than(lst, threshold):
    count = 0
    for n in lst:
        if n > threshold:
            count += 1
    return count if count > 0 else None


# 858. Функция для нахождения чисел, которые не делятся на 2, 3 или 5
def find_numbers_not_divisible_by_2_3_5(lst):
    result = []
    for n in lst:
        if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
            result.append(n)
    return result if result else None


# 859. Функция для подсчета количества чисел, которые делятся на 7
def count_divisible_by_7(lst):
    count = 0
    for n in lst:
        if n % 7 == 0:
            count += 1
    return count if count > 0 else None


# 860. Функция для нахождения максимального числа, которое является квадратом целого числа
def find_largest_square_number(lst):
    largest = None
    for n in lst:
        if (n ** 0.5).is_integer() and (largest is None or n > largest):
            largest = n
    return largest


# 861. Функция для нахождения наименьшего числа, которое является кубом целого числа
def find_smallest_cube_number(lst):
    smallest = None
    for n in lst:
        if (n ** (1 / 3)).is_integer() and (smallest is None or n < smallest):
            smallest = n
    return smallest


# 862. Функция для нахождения числа, которое является и квадратом, и кубом одновременно
def find_square_and_cube(lst):
    result = []
    for n in lst:
        if (n ** 0.5).is_integer() and (n ** (1 / 3)).is_integer():
            result.append(n)
    return result if result else None


# 863. Функция для нахождения наибольшего числа, которое является степенью двойки
def find_largest_power_of_two(lst):
    largest = None
    for n in lst:
        if (n & (n - 1)) == 0 and (largest is None or n > largest):
            largest = n
    return largest


# 864. Функция для нахождения наименьшего числа, которое является степенью двойки
def find_smallest_power_of_two(lst):
    smallest = None
    for n in lst:
        if (n & (n - 1)) == 0 and (smallest is None or n < smallest):
            smallest = n
    return smallest


# 865. Функция для нахождения всех чисел, которые являются степенями двойки
def find_all_powers_of_two(lst):
    powers_of_two = []
    for n in lst:
        if (n & (n - 1)) == 0:
            powers_of_two.append(n)
    return powers_of_two if powers_of_two else None


# 866. Функция для нахождения всех чисел, которые являются отрицательными
def find_all_negative_numbers(lst):
    negative_numbers = []
    for n in lst:
        if n < 0:
            negative_numbers.append(n)
    return negative_numbers if negative_numbers else None


# 867. Функция для нахождения всех чисел, которые являются положительными
def find_all_positive_numbers(lst):
    positive_numbers = []
    for n in lst:
        if n > 0:
            positive_numbers.append(n)
    return positive_numbers if positive_numbers else None


# 868. Функция для нахождения всех чисел, которые являются нулями
def find_all_zeros(lst):
    zeros = []
    for n in lst:
        if n == 0:
            zeros.append(n)
    return zeros if zeros else None


# 869. Функция для нахождения суммы чисел, которые больше заданного порога
def sum_numbers_greater_than(lst, threshold):
    total = 0
    for n in lst:
        if n > threshold:
            total += n
    return total if total > 0 else None


# 870. Функция для нахождения максимального значения среди всех чисел, делящихся на 4
def find_max_divisible_by_4(lst):
    max_divisible_by_4 = None
    for n in lst:
        if n % 4 == 0:
            if max_divisible_by_4 is None or n > max_divisible_by_4:
                max_divisible_by_4 = n
    return max_divisible_by_4


# 871. Функция для нахождения минимального значения среди всех чисел, делящихся на 6
def find_min_divisible_by_6(lst):
    min_divisible_by_6 = None
    for n in lst:
        if n % 6 == 0:
            if min_divisible_by_6 is None or n < min_divisible_by_6:
                min_divisible_by_6 = n
    return min_divisible_by_6


# 872. Функция для нахождения числа, которое делится и на 7, и на 11
def find_divisible_by_7_and_11(lst):
    result = []
    for n in lst:
        if n % 7 == 0 and n % 11 == 0:
            result.append(n)
    return result if result else None


# 873. Функция для нахождения наибольшего числа, которое делится на 9
def find_largest_divisible_by_9(lst):
    largest = None
    for n in lst:
        if n % 9 == 0 and (largest is None or n > largest):
            largest = n
    return largest


# 874. Функция для нахождения наименьшего числа, которое делится на 12
def find_smallest_divisible_by_12(lst):
    smallest = None
    for n in lst:
        if n % 12 == 0 and (smallest is None or n < smallest):
            smallest = n
    return smallest


# 875. Функция для нахождения чисел, которые делятся на 15 и на 20
def find_divisible_by_15_and_20(lst):
    result = []
    for n in lst:
        if n % 15 == 0 and n % 20 == 0:
            result.append(n)
    return result if result else None


# 876. Функция для создания кортежа из чисел, переданных в список
def create_tuple_from_list(lst):
    if not lst:
        return None
    result = tuple(lst)
    return result


# 877. Функция для нахождения кортежа с минимальным и максимальным элементом из списка
def find_min_max_from_list(lst):
    if not lst:
        return None
    min_val = min(lst)
    max_val = max(lst)
    return min_val, max_val


# 878. Функция для создания кортежа, состоящего из уникальных элементов списка
def create_tuple_of_unique_elements(lst):
    unique_elements = set(lst)
    return tuple(unique_elements) if unique_elements else None


# 879. Функция для нахождения кортежа из чисел, которые делятся на 3 из переданного списка
def find_divisible_by_3(lst):
    result = []
    for n in lst:
        if n % 3 == 0:
            result.append(n)
    return tuple(result) if result else None


# 880. Функция для нахождения кортежа из всех четных чисел в списке
def find_even_numbers(lst):
    result = []
    for n in lst:
        if n % 2 == 0:
            result.append(n)
    return tuple(result) if result else None


# 881. Функция для создания кортежа, состоящего из строк, длина которых больше 3 символов
def find_long_strings(lst):
    result = []
    for s in lst:
        if len(s) > 3:
            result.append(s)
    return tuple(result) if result else None


# 882. Функция для создания кортежа из строк, содержащих хотя бы одну цифру
def find_strings_with_digits_2(lst):
    result = []
    for s in lst:
        if any(char.isdigit() for char in s):
            result.append(s)
    return tuple(result) if result else None


# 883. Функция для создания кортежа из всех чисел, которые являются квадратами целых чисел
def find_square_numbers(lst):
    result = []
    for n in lst:
        if (n ** 0.5).is_integer():
            result.append(n)
    return tuple(result) if result else None


# 884. Функция для создания кортежа из чисел, которые делятся на 5
def find_divisible_by_5(lst):
    result = []
    for n in lst:
        if n % 5 == 0:
            result.append(n)
    return tuple(result) if result else None


# 885. Функция для создания кортежа из строк, длина которых меньше или равна 5 символам
def find_short_strings(lst):
    result = []
    for s in lst:
        if len(s) <= 5:
            result.append(s)
    return tuple(result) if result else None


# 886. Функция для создания кортежа из чисел, которые больше заданного порога
def find_greater_than(lst, threshold):
    result = []
    for n in lst:
        if n > threshold:
            result.append(n)
    return tuple(result) if result else None


# 887. Функция для создания кортежа, содержащего индексы всех элементов, равных максимальному
def find_max_indexes(lst):
    if not lst:
        return None
    max_val = max(lst)
    indexes = [i for i, x in enumerate(lst) if x == max_val]
    return tuple(indexes) if indexes else None


# 888. Функция для нахождения кортежа чисел, которые являются четными и больше 10
def find_even_and_greater_than_ten(lst):
    result = []
    for n in lst:
        if n % 2 == 0 and n > 10:
            result.append(n)
    return tuple(result) if result else None


# 889. Функция для создания кортежа из всех строк, в которых есть хотя бы одна заглавная буква
def find_strings_with_uppercase(lst):
    result = []
    for s in lst:
        if any(char.isupper() for char in s):
            result.append(s)
    return tuple(result) if result else None


# 890. Функция для создания кортежа из чисел, которые делятся на 4 и не делятся на 2
def find_numbers_divisible_by_4_not_2(lst):
    result = []
    for n in lst:
        if n % 4 == 0 and n % 2 != 0:
            result.append(n)
    return tuple(result) if result else None


# 891. Функция для создания кортежа из всех строк, длина которых больше средней длины всех строк
def find_longer_than_average(lst):
    average_length = sum(len(s) for s in lst) / len(lst) if lst else 0
    result = []
    for s in lst:
        if len(s) > average_length:
            result.append(s)
    return tuple(result) if result else None


# 892. Функция для создания кортежа из чисел, которые равны сумме их цифр
def find_numbers_equal_to_digit_sum(lst):
    result = []
    for n in lst:
        if n == sum(int(digit) for digit in str(abs(n))):
            result.append(n)
    return tuple(result) if result else None


# 893. Функция для создания кортежа из чисел, которые являются делителями 100
def find_divisors_of_100(lst):
    result = []
    for n in lst:
        if 100 % n == 0:
            result.append(n)
    return tuple(result) if result else None


# 894. Функция для создания кортежа из чисел, которые являются кратными 3 и 5
def find_multiples_of_3_and_5(lst):
    result = []
    for n in lst:
        if n % 3 == 0 and n % 5 == 0:
            result.append(n)
    return tuple(result) if result else None


# 895. Функция для создания кортежа, содержащего все числа, кратные числу из списка
def find_multiples_of_list(lst, n):
    result = []
    for num in lst:
        if num % n == 0:
            result.append(num)
    return tuple(result) if result else None


# 896. Функция для нахождения всех чисел, которые являются результатом возведения чисел в квадрат
def find_squared_numbers(lst):
    result = []
    for n in lst:
        if (n ** 0.5).is_integer():
            result.append(n)
    return tuple(result) if result else None


# 897. Функция для создания кортежа, содержащего числа из списка, которые делятся на 6
def find_divisible_by_6_2(lst):
    result = []
    for n in lst:
        if n % 6 == 0:
            result.append(n)
    return tuple(result) if result else None


# 898. Функция для нахождения чисел, делящихся на 2 и 3
def find_divisible_by_2_and_3_2(lst):
    result = []
    for n in lst:
        if n % 2 == 0 and n % 3 == 0:
            result.append(n)
    return tuple(result) if result else None


# 899. Функция для создания кортежа с числами, которые кратны 2, 3 и 5
def find_multiples_of_2_3_5(lst):
    result = []
    for n in lst:
        if n % 2 == 0 and n % 3 == 0 and n % 5 == 0:
            result.append(n)
    return tuple(result) if result else None


# 900. Функция для создания кортежа из всех чисел, которые являются палиндромами
def find_palindromes_4(lst):
    result = []
    for n in lst:
        if str(n) == str(n)[::-1]:
            result.append(n)
    return tuple(result) if result else None


# 901. Функция для нахождения всех чисел, которые меньше их суммы цифр
def find_numbers_less_than_digit_sum(lst):
    result = []
    for n in lst:
        if n < sum(int(digit) for digit in str(abs(n))):
            result.append(n)
    return tuple(result) if result else None


# 902. Функция для создания кортежа из чисел, которые равны сумме всех их делителей
def find_numbers_equal_to_sum_of_divisors(lst):
    result = []
    for n in lst:
        divisors = [i for i in range(1, n) if n % i == 0]
        if n == sum(divisors):
            result.append(n)
    return tuple(result) if result else None


# 903. Функция для создания кортежа чисел, которые кратны 9, но не кратны 3
def find_multiples_of_9_not_3(lst):
    result = []
    for n in lst:
        if n % 9 == 0 and n % 3 != 0:
            result.append(n)
    return tuple(result) if result else None


# 904. Функция для нахождения чисел, которые делятся на 11 и 13
def find_divisible_by_11_and_13(lst):
    result = []
    for n in lst:
        if n % 11 == 0 and n % 13 == 0:
            result.append(n)
    return tuple(result) if result else None


# 905. Функция для создания словаря, где ключами являются элементы списка, а значениями их квадраты
def create_square_dict(lst):
    if not lst:
        return None
    square_dict = {}
    for item in lst:
        square_dict[item] = item ** 2
    return square_dict if square_dict else None


# 906. Функция для нахождения минимального и максимального значений в словаре
def find_min_max_in_dict(d):
    if not d:
        return None
    min_key = min(d, key=d.get)
    max_key = max(d, key=d.get)
    return (min_key, d[min_key]), (max_key, d[max_key])


# 907. Функция для фильтрации словаря, оставляя только те ключи, которые являются строками
def filter_dict_with_strings(d):
    if not d:
        return None
    filtered_dict = {}
    for key, value in d.items():
        if isinstance(key, str):
            filtered_dict[key] = value
    return filtered_dict if filtered_dict else None


# 908. Функция для нахождения суммы значений всех числовых ключей в словаре
def sum_of_numeric_keys(d):
    if not d:
        return None
    total = 0
    for key, value in d.items():
        if isinstance(key, (int, float)):
            total += value
    return total if total else None


# 909. Функция для создания словаря, в котором ключи — это длины строк из списка, а значения — сами строки
def create_dict_from_string_lengths(lst):
    if not lst:
        return None
    length_dict = {}
    for s in lst:
        length_dict[len(s)] = s
    return length_dict if length_dict else None


# 910. Функция для удаления из словаря всех элементов с отрицательными значениями
def remove_negative_values(d):
    if not d:
        return None
    clean_dict = {}
    for key, value in d.items():
        if value >= 0:
            clean_dict[key] = value
    return clean_dict if clean_dict else None


# 911. Функция для создания словаря из двух списков: первый — ключи, второй — значения
def create_dict_from_lists(keys, values):
    if not keys or not values or len(keys) != len(values):
        return None
    result_dict = {}
    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]
    return result_dict if result_dict else None


# 912. Функция для подсчёта количества строк с одинаковыми длинами в списке
def count_strings_by_length(lst):
    if not lst:
        return None
    length_count = {}
    for s in lst:
        length_count[len(s)] = length_count.get(len(s), 0) + 1
    return length_count if length_count else None


# 913. Функция для нахождения минимального значения в словаре, в котором ключи — это числа
def find_min_value_in_dict(d):
    if not d:
        return None
    min_value = min(d.values())
    return min_value if min_value else None


# 914. Функция для создания словаря, где ключами являются индексы, а значениями элементы списка
def create_dict_from_list(lst):
    if not lst:
        return None
    index_dict = {}
    for i, value in enumerate(lst):
        index_dict[i] = value
    return index_dict if index_dict else None


# 915. Функция для нахождения всех чисел, которые встречаются более одного раза в словаре
def find_duplicates_in_dict(d):
    if not d:
        return None
    reverse_dict = {}
    for key, value in d.items():
        if value not in reverse_dict:
            reverse_dict[value] = [key]
        else:
            reverse_dict[value].append(key)
    duplicates = {value: keys for value, keys in reverse_dict.items() if len(keys) > 1}
    return duplicates if duplicates else None


# 916. Функция для подсчёта количества элементов в списке, которые равны значению по заданному ключу
def count_values_by_key(d, key):
    if not d or key not in d:
        return None
    count = 0
    for value in d.values():
        if value == d[key]:
            count += 1
    return count if count else None


# 917. Функция для поиска всех значений в словаре, которые больше заданного порога
def find_values_greater_than(d, threshold):
    if not d:
        return None
    result = []
    for key, value in d.items():
        if value > threshold:
            result.append((key, value))
    return result if result else None


# 918. Функция для создания словаря, в котором ключи — это числа, а значения — это их остатки от деления на 5
def create_remainders_dict(lst):
    if not lst:
        return None
    remainder_dict = {}
    for n in lst:
        remainder_dict[n] = n % 5
    return remainder_dict if remainder_dict else None


# 919. Функция для нахождения суммы всех числовых значений в словаре
def sum_of_dict_values(d):
    if not d:
        return None
    total = 0
    for value in d.values():
        total += value
    return total if total else None


# 920. Функция для создания словаря, где ключи — это строки, а значения — длины этих строк
def create_length_dict(lst):
    if not lst:
        return None
    length_dict = {}
    for s in lst:
        length_dict[s] = len(s)
    return length_dict if length_dict else None


# 921. Функция для нахождения чисел в словаре, которые являются простыми
def find_prime_numbers_2(d):
    if not d:
        return None
    prime_numbers = {}
    for key, value in d.items():
        if value > 1 and all(value % i != 0 for i in range(2, int(value ** 0.5) + 1)):
            prime_numbers[key] = value
    return prime_numbers if prime_numbers else None


# 922. Функция для фильтрации словаря, оставляя только те элементы, у которых значения — чётные числа
def filter_even_values(d):
    if not d:
        return None
    filtered_dict = {}
    for key, value in d.items():
        if isinstance(value, int) and value % 2 == 0:
            filtered_dict[key] = value
    return filtered_dict if filtered_dict else None


# 923. Функция для создания словаря, где ключами являются элементы списка, а значениями — их удвоенные значения
def create_double_value_dict(lst):
    if not lst:
        return None
    double_dict = {}
    for item in lst:
        double_dict[item] = item * 2
    return double_dict if double_dict else None


# 924. Функция для создания словаря с числовыми значениями, где значения кратны 7
def create_sevens_dict(lst):
    if not lst:
        return None
    sevens_dict = {}
    for item in lst:
        if item % 7 == 0:
            sevens_dict[item] = item
    return sevens_dict if sevens_dict else None


# 925. Функция для нахождения всех значений в словаре, которые равны их ключам
def find_equal_key_value_pairs(d):
    if not d:
        return None
    result = []
    for key, value in d.items():
        if key == value:
            result.append((key, value))
    return result if result else None


# 926. Функция для поиска максимального значения среди всех значений словаря
def find_max_value_in_dict_4(d):
    if not d:
        return None
    max_value = max(d.values())
    return max_value if max_value else None


# 927. Функция для создания словаря, где ключами являются элементы списка, а значениями их кубы
def create_cube_dict(lst):
    if not lst:
        return None
    cube_dict = {}
    for item in lst:
        cube_dict[item] = item ** 3
    return cube_dict if cube_dict else None


# 928. Функция для поиска строк, которые содержат больше определённого количества символов
def find_long_strings_3(d, length):
    if not d:
        return None
    result = []
    for key, value in d.items():
        if isinstance(value, str) and len(value) > length:
            result.append((key, value))
    return result if result else None


# 929. Функция для нахождения всех значений, которые являются нечётными числами
def find_odd_values(d):
    if not d:
        return None
    result = []
    for key, value in d.items():
        if isinstance(value, int) and value % 2 != 0:
            result.append((key, value))
    return result if result else None


# 930. Функция для нахождения всех чисел, которые больше среднего значения всех значений в словаре
def find_values_greater_than_average(d):
    if not d:
        return None
    avg_value = sum(d.values()) / len(d)
    result = []
    for key, value in d.items():
        if value > avg_value:
            result.append((key, value))
    return result if result else None


# 931. Функция для создания словаря, где ключи — это индексы строк из списка, а значения — это сами строки
def create_string_dict(lst):
    if not lst:
        return None
    string_dict = {}
    for i, s in enumerate(lst):
        string_dict[i] = s
    return string_dict if string_dict else None


# 932. Функция для нахождения чисел, которые больше заданного порога в словаре
def find_values_greater_than_threshold(d, threshold):
    if not d:
        return None
    result = []
    for key, value in d.items():
        if value > threshold:
            result.append((key, value))
    return result if result else None


# 933. Функция для подсчёта количества уникальных значений в словаре
def count_unique_values(d):
    if not d:
        return None
    unique_values = set(d.values())
    return len(unique_values) if unique_values else None


# 934. Функция для фильтрации словаря, оставляя только те элементы, у которых ключи являются строками
def filter_dict_with_string_keys(d):
    if not d:
        return None
    filtered_dict = {}
    for key, value in d.items():
        if isinstance(key, str):
            filtered_dict[key] = value
    return filtered_dict if filtered_dict else None


# 935. Функция для нахождения наибольшего числа в списке значений словаря
def find_max_in_values(d):
    if not d:
        return None
    max_value = max(d.values())
    return max_value if max_value else None


# 936. Функция для удаления из словаря всех элементов, где значение является пустой строкой
def remove_empty_values(d):
    if not d:
        return None
    clean_dict = {}
    for key, value in d.items():
        if value != "":
            clean_dict[key] = value
    return clean_dict if clean_dict else None


# 937. Функция для нахождения чисел, которые содержатся и в списке, и в множестве, и выводятся как кортежи
def find_common_elements_5(lst, s):
    if not lst or not s:
        return None
    common = set(lst).intersection(s)
    if not common:
        return None
    result = [(item, lst.index(item)) for item in common]
    return tuple(result) if result else None


# 938. Функция для вычисления суммы всех элементов кортежа, которые делятся на 3
def sum_of_multiples_of_3(t):
    if not t:
        return None
    total = 0
    for n in t:
        if n % 3 == 0:
            total += n
    return total if total else None


# 939. Функция для нахождения чисел, которые встречаются как в списке, так и в словаре
def find_elements_in_list_and_dict(lst, d):
    if not lst or not d:
        return None
    common_elements = []
    for item in lst:
        if item in d:
            common_elements.append(item)
    return tuple(common_elements) if common_elements else None


# 940. Функция для создания множества уникальных значений из списка, кортежа и словаря
def create_unique_set_from_multiple_sources(lst, t, d):
    if not lst or not t or not d:
        return None
    combined_set = set(lst).union(t).union(d.values())
    return combined_set if combined_set else None


# 941. Функция для нахождения строк, длина которых больше заданного числа, из списка и словаря
def find_long_strings_6(lst, d, length):
    if not lst or not d:
        return None
    long_strings = []
    for item in lst:
        if isinstance(item, str) and len(item) > length:
            long_strings.append(item)
    for value in d.values():
        if isinstance(value, str) and len(value) > length:
            long_strings.append(value)
    return tuple(long_strings) if long_strings else None


# 942. Функция для нахождения чисел, которые больше всех чисел в словаре, и добавление их в множество
def find_numbers_greater_than_dict_values(lst, d):
    if not lst or not d:
        return None
    greater_numbers = set()
    max_value = max(d.values())
    for n in lst:
        if n > max_value:
            greater_numbers.add(n)
    return greater_numbers if greater_numbers else None


# 943. Функция для подсчёта, сколько раз встречаются числа в списке, и создание словаря с этим количеством
def count_numbers_in_list(lst):
    if not lst:
        return None
    count_dict = {}
    for n in lst:
        count_dict[n] = count_dict.get(n, 0) + 1
    return count_dict if count_dict else None


# 944. Функция для создания списка чисел, которые есть в словаре и кортежах
def find_numbers_in_dict_and_tuple(d, t):
    if not d or not t:
        return None
    result = []
    for value in d.values():
        if value in t:
            result.append(value)
    return result if result else None


# 945. Функция для создания словаря, где ключи — это элементы списка, а значения — их индексы
def create_index_dict(lst):
    if not lst:
        return None
    index_dict = {}
    for i, item in enumerate(lst):
        index_dict[item] = i
    return index_dict if index_dict else None


# 946. Функция для создания множества всех уникальных символов из строк в списке и словаре
def create_unique_char_set(lst, d):
    if not lst or not d:
        return None
    char_set = set()
    for s in lst:
        if isinstance(s, str):
            char_set.update(s)
    for value in d.values():
        if isinstance(value, str):
            char_set.update(value)
    return char_set if char_set else None


# 947. Функция для подсчёта уникальных элементов в списке и добавления их в словарь
def count_unique_elements(lst):
    if not lst:
        return None
    count_dict = {}
    for item in lst:
        count_dict[item] = count_dict.get(item, 0) + 1
    return count_dict if count_dict else None


# 948. Функция для нахождения чисел, которые являются квадратами чисел из множества
def find_squares_in_set(s):
    if not s:
        return None
    result = []
    for n in s:
        if (n ** 0.5).is_integer():
            result.append(n)
    return tuple(result) if result else None


# 949. Функция для нахождения строк с числовыми символами, которые встречаются в списке и словаре
def find_numeric_strings(lst, d):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if isinstance(item, str) and any(char.isdigit() for char in item):
            result.append(item)
    for value in d.values():
        if isinstance(value, str) and any(char.isdigit() for char in value):
            result.append(value)
    return tuple(result) if result else None


# 950. Функция для нахождения чисел в списке, которые равны числовым значениям в словаре
def find_equal_numbers(lst, d):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if item in d.values():
            result.append(item)
    return tuple(result) if result else None


# 951. Функция для нахождения всех чисел, которые могут быть составлены из цифр строки
def find_numbers_from_string(s):
    if not s:
        return None
    result = []
    for char in s:
        if char.isdigit():
            result.append(int(char))
    return tuple(result) if result else None


# 952. Функция для создания списка, где элементы — это чётные индексы словаря
def create_even_indexed_list(d):
    if not d:
        return None
    result = []
    for i, (key, value) in enumerate(d.items()):
        if i % 2 == 0:
            result.append((key, value))
    return result if result else None


# 953. Функция для нахождения чисел, которые встречаются в списке, но отсутствуют в множестве
def find_numbers_not_in_set(lst, s):
    if not lst or not s:
        return None
    result = []
    for item in lst:
        if item not in s:
            result.append(item)
    return tuple(result) if result else None


# 954. Функция для создания словаря, где ключи — это элементы списка, а значения — множества их делителей
def create_divisors_dict(lst):
    if not lst:
        return None
    divisors_dict = {}
    for item in lst:
        divisors = {i for i in range(1, item + 1) if item % i == 0}
        divisors_dict[item] = divisors
    return divisors_dict if divisors_dict else None


# 955. Функция для нахождения чисел, которые одновременно больше и меньше заданных значений
def find_numbers_between_bounds(lst, lower, upper):
    if not lst:
        return None
    result = []
    for n in lst:
        if lower < n < upper:
            result.append(n)
    return tuple(result) if result else None


# 956. Функция для нахождения всех значений из словаря, которые меньше заданного числа
def find_values_less_than(d, num):
    if not d:
        return None
    result = []
    for value in d.values():
        if value < num:
            result.append(value)
    return tuple(result) if result else None


# 957. Функция для создания словаря, где ключи — это элементы множества, а значения — их длины (если это строки)
def create_length_dict_from_set(s):
    if not s:
        return None
    length_dict = {}
    for item in s:
        if isinstance(item, str):
            length_dict[item] = len(item)
    return length_dict if length_dict else None


# 958. Функция для создания списка чисел, которые являются нечётными в списке и чётными в словаре
def find_odd_in_list_and_even_in_dict(lst, d):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if item % 2 != 0 and item in d:
            if d[item] % 2 == 0:
                result.append(item)
    return result if result else None


# 959. Функция для создания множества, которое объединяет все чётные числа из списка и множества
def create_even_number_set(lst, s):
    if not lst or not s:
        return None
    even_set = set()
    for item in lst:
        if item % 2 == 0:
            even_set.add(item)
    for item in s:
        if item % 2 == 0:
            even_set.add(item)
    return even_set if even_set else None


# 960. Функция для нахождения чисел из списка и словаря, которые больше среднего в словаре
def find_numbers_greater_than_avg_in_dict(lst, d):
    if not lst or not d:
        return None
    avg = sum(d.values()) / len(d)
    result = []
    for item in lst:
        if item > avg:
            result.append(item)
    return tuple(result) if result else None


# 961. Функция для нахождения строк, длина которых меньше заданного числа в списке и словаре
def find_short_strings_2(lst, d, length):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if isinstance(item, str) and len(item) < length:
            result.append(item)
    for value in d.values():
        if isinstance(value, str) and len(value) < length:
            result.append(value)
    return tuple(result) if result else None


# 962. Функция для нахождения максимального числа среди значений словаря и элементов списка
def find_max_in_dict_and_list(lst, d):
    if not lst or not d:
        return None
    max_list_value = max(lst)
    max_dict_value = max(d.values())
    return max(max_list_value, max_dict_value)


# 963. Функция для создания словаря, где ключи — это элементы множества, а значения — длина строки ключа
def create_length_dict_from_set_2(s):
    if not s:
        return None
    length_dict = {}
    for item in s:
        length_dict[item] = len(str(item))
    return length_dict if length_dict else None


# 964. Функция для подсчёта, сколько раз встречаются элементы в списке и словаре
def count_elements_in_list_and_dict(lst, d):
    if not lst or not d:
        return None
    count_dict = {}
    for item in lst + list(d.values()):
        count_dict[item] = count_dict.get(item, 0) + 1
    return count_dict if count_dict else None


# 965. Функция для нахождения общих значений между множеством и кортежем
def find_common_in_set_and_tuple(s, t):
    if not s or not t:
        return None
    result = s.intersection(t)
    return tuple(result) if result else None


# 966. Функция для нахождения чисел, которые содержат хотя бы одну цифру из другого числа
def find_numbers_with_digit(lst, num):
    if not lst:
        return None
    result = []
    str_num = str(num)
    for item in lst:
        if any(digit in str(item) for digit in str_num):
            result.append(item)
    return tuple(result) if result else None


# 967. Функция для создания множества всех нечётных чисел, которые присутствуют и в списке, и в словаре
def find_odd_numbers_in_both(lst, d):
    if not lst or not d:
        return None
    odd_set = set()
    for item in lst:
        if item % 2 != 0 and item in d:
            odd_set.add(item)
    return odd_set if odd_set else None


# 968. Функция для нахождения чисел из списка, которые не присутствуют в словаре
def find_numbers_not_in_dict(lst, d):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if item not in d:
            result.append(item)
    return tuple(result) if result else None


# 969. Функция для нахождения уникальных элементов в списке, кортежах и множествах
def find_unique_elements_9(lst, t, s):
    if not lst or not t or not s:
        return None
    unique_elements = set(lst).union(set(t)).union(s)
    return tuple(unique_elements) if unique_elements else None


# 970. Функция для нахождения всех чисел в списке, которые делятся на все числа в множестве
def find_numbers_divisible_by_all(lst, s):
    if not lst or not s:
        return None
    result = []
    for item in lst:
        if all(item % i == 0 for i in s):
            result.append(item)
    return tuple(result) if result else None


# 971. Функция для создания множества, которое объединяет все нечётные числа из списка и множества
def create_odd_number_set(lst, s):
    if not lst or not s:
        return None
    odd_set = set()
    for item in lst:
        if item % 2 != 0:
            odd_set.add(item)
    for item in s:
        if item % 2 != 0:
            odd_set.add(item)
    return odd_set if odd_set else None


# 972. Функция для нахождения всех чисел, которые находятся в обеих коллекциях (списке и словаре)
def find_numbers_in_list_and_dict(lst, d):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if item in d.values():
            result.append(item)
    return tuple(result) if result else None


# 973. Функция для подсчёта уникальных элементов в списке и словаре
def count_unique_elements_in_list_and_dict(lst, d):
    if not lst or not d:
        return None
    result = set(lst).union(set(d.values()))
    return len(result) if result else None


# 974. Функция для создания словаря, где ключи — это элементы множества, а значения — их квадраты
def create_square_dict_from_set(s):
    if not s:
        return None
    square_dict = {}
    for item in s:
        square_dict[item] = item ** 2
    return square_dict if square_dict else None


# 975. Функция для создания списка, в котором каждый элемент — это результат вычисления произведения всех чисел из словаря
def create_product_list_from_dict(d):
    if not d:
        return None
    product_list = []
    for key, value in d.items():
        product = 1
        for num in value:
            product *= num
        product_list.append(product)
    return product_list if product_list else None


# 976. Функция для нахождения всех строк из списка и множества, которые содержат хотя бы одну цифру
def find_strings_with_digit(lst, s):
    if not lst or not s:
        return None
    result = []
    for item in lst:
        if isinstance(item, str) and any(char.isdigit() for char in item):
            result.append(item)
    for item in s:
        if isinstance(item, str) and any(char.isdigit() for char in item):
            result.append(item)
    return tuple(result) if result else None


# 977. Функция для нахождения чисел, которые встречаются и в списке, и в кортеже, и в множестве
def find_common_numbers(lst, t, s):
    if not lst or not t or not s:
        return None
    common = set(lst).intersection(t, s)
    return tuple(common) if common else None


# 978. Функция для создания множества, состоящего из всех строк, длина которых меньше заданного числа
def create_set_of_short_strings(lst, max_len):
    if not lst:
        return None
    result = set()
    for item in lst:
        if isinstance(item, str) and len(item) < max_len:
            result.add(item)
    return result if result else None


# 979. Функция для нахождения строк, длина которых больше средней длины всех строк в списке
def find_long_strings_2(lst):
    if not lst:
        return None
    avg_length = sum(len(item) for item in lst) / len(lst)
    result = []
    for item in lst:
        if len(item) > avg_length:
            result.append(item)
    return tuple(result) if result else None


# 980. Функция для нахождения чисел, которые находятся в кортеже, но отсутствуют в словаре
def find_numbers_in_tuple_not_in_dict(t, d):
    if not t or not d:
        return None
    result = []
    for item in t:
        if item not in d:
            result.append(item)
    return tuple(result) if result else None


# 981. Функция для нахождения элементов, которые встречаются в списке, но не в множестве и словаре
def find_in_list_not_in_set_and_dict(lst, s, d):
    if not lst or not s or not d:
        return None
    result = []
    for item in lst:
        if item not in s and item not in d.values():
            result.append(item)
    return tuple(result) if result else None


# 982. Функция для нахождения максимальных элементов из списка и словаря
def find_max_values(lst, d):
    if not lst or not d:
        return None
    max_lst = max(lst)
    max_dict = max(d.values())
    return max(max_lst, max_dict)


# 983. Функция для нахождения всех элементов из множества, которые не присутствуют в словаре
def find_in_set_not_in_dict(s, d):
    if not s or not d:
        return None
    result = []
    for item in s:
        if item not in d:
            result.append(item)
    return tuple(result) if result else None


# 984. Функция для создания словаря, где ключи — это строки из множества, а значения — длина строки
def create_string_length_dict(s):
    if not s:
        return None
    string_length_dict = {}
    for item in s:
        if isinstance(item, str):
            string_length_dict[item] = len(item)
    return string_length_dict if string_length_dict else None


# 985. Функция для создания множества, которое содержит уникальные элементы из списка и множества
def create_unique_set_from_list_and_set(lst, s):
    if not lst or not s:
        return None
    unique_set = set()
    for item in lst:
        unique_set.add(item)
    for item in s:
        unique_set.add(item)
    return unique_set if unique_set else None


# 986. Функция для нахождения всех чисел из списка и словаря, которые являются чётными
def find_even_numbers_in_list_and_dict(lst, d):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if item % 2 == 0:
            result.append(item)
    for value in d.values():
        if value % 2 == 0:
            result.append(value)
    return tuple(result) if result else None


# 987. Функция для создания словаря, где ключи — это строки, а значения — длины строк, встречающихся и в списке, и в множестве
def create_length_dict_from_strings_in_both(lst, s):
    if not lst or not s:
        return None
    length_dict = {}
    for item in lst:
        if isinstance(item, str) and item in s:
            length_dict[item] = len(item)
    return length_dict if length_dict else None


# 988. Функция для нахождения строк в списке, которые содержат хотя бы один символ, присутствующий в другом списке
def find_strings_with_common_characters(lst1, lst2):
    if not lst1 or not lst2:
        return None
    result = []
    for item in lst1:
        if isinstance(item, str):
            for char in item:
                if any(char in s for s in lst2 if isinstance(s, str)):
                    result.append(item)
                    break
    return tuple(result) if result else None


# 989. Функция для нахождения чисел в словаре, значения которых больше, чем в списке
def find_values_greater_than_in_list(d, lst):
    if not d or not lst:
        return None
    result = []
    for value in d.values():
        for item in lst:
            if value > item:
                result.append(value)
                break
    return tuple(result) if result else None


# 990. Функция для нахождения всех чисел, которые присутствуют и в списке, и в множестве
def find_numbers_in_both_list_and_set(lst, s):
    if not lst or not s:
        return None
    result = []
    for item in lst:
        if item in s:
            result.append(item)
    return tuple(result) if result else None


# 991. Функция для нахождения элементов из списка, которые не встречаются в других структурах данных
def find_elements_not_in_other_structures(lst, s, d, t):
    if not lst or not s or not d or not t:
        return None
    result = []
    for item in lst:
        if item not in s and item not in d.values() and item not in t:
            result.append(item)
    return tuple(result) if result else None


# 992. Функция для нахождения чисел, которые меньше минимального значения в списке и больше максимального в словаре
def find_numbers_between_min_in_list_and_max_in_dict(lst, d):
    if not lst or not d:
        return None
    min_lst = min(lst)
    max_dict = max(d.values())
    result = []
    for item in lst:
        if min_lst < item < max_dict:
            result.append(item)
    return tuple(result) if result else None


# 993. Функция для создания множества из всех строк, длина которых больше заданного значения
def create_set_of_long_strings(lst, min_length):
    if not lst:
        return None
    long_strings = set()
    for item in lst:
        if isinstance(item, str) and len(item) > min_length:
            long_strings.add(item)
    return long_strings if long_strings else None


# 994. Функция для нахождения всех чисел в словаре, которые меньше средней величины всех значений в словаре
def find_numbers_less_than_avg_in_dict(d):
    if not d:
        return None
    avg = sum(d.values()) / len(d)
    result = []
    for value in d.values():
        if value < avg:
            result.append(value)
    return tuple(result) if result else None


# 995. Функция для подсчёта количества строк, длина которых больше средней длины всех строк в списке
def count_strings_longer_than_avg(lst):
    if not lst:
        return None
    avg_length = sum(len(item) for item in lst if isinstance(item, str)) / len(lst)
    count = 0
    for item in lst:
        if isinstance(item, str) and len(item) > avg_length:
            count += 1
    return count if count > 0 else None


# 996. Функция для нахождения элементов, которые одновременно присутствуют в множестве и кортеже
def find_common_in_set_and_tuple_2(s, t):
    if not s or not t:
        return None
    result = []
    for item in s:
        if item in t:
            result.append(item)
    return tuple(result) if result else None


# 997. Функция для создания словаря, где ключи — это строки, а значения — их длина, если строка есть в списке
def create_length_dict_from_strings_in_list(lst):
    if not lst:
        return None
    length_dict = {}
    for item in lst:
        if isinstance(item, str):
            length_dict[item] = len(item)
    return length_dict if length_dict else None


# 998. Функция для нахождения чисел, которые больше максимума в списке и меньше минимума в словаре
def find_numbers_between_max_in_list_and_min_in_dict(lst, d):
    if not lst or not d:
        return None
    max_lst = max(lst)
    min_dict = min(d.values())
    result = []
    for item in lst:
        if min_dict < item < max_lst:
            result.append(item)
    return tuple(result) if result else None


# 999. Функция для нахождения строк, содержащих хотя бы одну букву из множества
def find_strings_with_letter_from_set(lst, s):
    if not lst or not s:
        return None
    result = []
    for item in lst:
        if isinstance(item, str) and any(char in s for char in item):
            result.append(item)
    return tuple(result) if result else None


# 1000. Функция для нахождения чисел, которые присутствуют в списке, но не в словаре
def find_numbers_in_list_not_in_dict(lst, d):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if item not in d:
            result.append(item)
    return tuple(result) if result else None


# 1001. Функция для нахождения всех чисел в списке, которые встречаются и в множестве, и в словаре
def find_numbers_in_both_set_and_dict(lst, s, d):
    if not lst or not s or not d:
        return None
    result = []
    for item in lst:
        if item in s and item in d.values():
            result.append(item)
    return tuple(result) if result else None


# 1002. Функция для создания списка всех чисел, которые больше минимального в словаре и меньше максимального в множестве
def create_list_between_min_in_dict_and_max_in_set(d, s):
    if not d or not s:
        return None
    min_dict = min(d.values())
    max_set = max(s)
    result = []
    for value in d.values():
        if min_dict < value < max_set:
            result.append(value)
    return result if result else None


# 1003. Функция для нахождения чисел, которые присутствуют в кортеже, но отсутствуют в множестве и словаре
def find_in_tuple_not_in_set_and_dict(t, s, d):
    if not t or not s or not d:
        return None
    result = []
    for item in t:
        if item not in s and item not in d:
            result.append(item)
    return tuple(result) if result else None


# 1004. Функция для нахождения всех чисел, которые больше заданного в списке, но меньше в словаре
def find_floats_between_list_and_dict(lst, d):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if isinstance(item, float):
            if min(lst) < item < max(d.values()):
                result.append(item)
    return tuple(result) if result else None


# 1005. Функция для нахождения всех чисел в списке, которые больше максимума в словаре
def find_floats_greater_than_max_in_dict(lst, d):
    if not lst or not d:
        return None
    max_dict = max(d.values())
    result = []
    for item in lst:
        if isinstance(item, float) and item > max_dict:
            result.append(item)
    return tuple(result) if result else None


# 1006. Функция для подсчёта количества чисел, которые меньше заданного значения в списке и словаре
def count_floats_less_than_value_in_list_and_dict(lst, d, value):
    if not lst or not d:
        return None
    count = 0
    for item in lst:
        if isinstance(item, float) and item < value:
            count += 1
    for val in d.values():
        if isinstance(val, float) and val < value:
            count += 1
    return count if count > 0 else None


# 1007. Функция для нахождения чисел в списке, которые меньше максимального значения в другом списке
def find_floats_less_than_max_in_other_list(lst1, lst2):
    if not lst1 or not lst2:
        return None
    max_lst2 = max(lst2)
    result = []
    for item in lst1:
        if isinstance(item, float) and item < max_lst2:
            result.append(item)
    return tuple(result) if result else None


# 1008. Функция для нахождения чисел, которые меньше всех значений в словаре и больше всех значений в списке
def find_floats_between_max_in_list_and_min_in_dict(lst, d):
    if not lst or not d:
        return None
    min_dict = min(d.values())
    max_lst = max(lst)
    result = []
    for item in lst:
        if isinstance(item, float) and min_dict < item < max_lst:
            result.append(item)
    return tuple(result) if result else None


# 1009. Функция для нахождения чисел в списке, которые равны или меньше значений в множестве
def find_floats_less_than_or_equal_to_set_values(lst, s):
    if not lst or not s:
        return None
    result = []
    for item in lst:
        if isinstance(item, float) and any(item <= elem for elem in s):
            result.append(item)
    return tuple(result) if result else None


# 1010. Функция для нахождения всех чисел в словаре, которые меньше заданного значения
def find_floats_less_than_value_in_dict(d, value):
    if not d:
        return None
    result = []
    for item in d.values():
        if isinstance(item, float) and item < value:
            result.append(item)
    return tuple(result) if result else None


# 1011. Функция для нахождения чисел, которые одновременно больше максимума в одном списке и меньше минимума в другом списке
def find_floats_between_max_in_first_list_and_min_in_second_list(lst1, lst2):
    if not lst1 or not lst2:
        return None
    max_lst1 = max(lst1)
    min_lst2 = min(lst2)
    result = []
    for item in lst1:
        if isinstance(item, float) and max_lst1 < item < min_lst2:
            result.append(item)
    return tuple(result) if result else None


# 1012. Функция для нахождения чисел, которые меньше или равны максимальному значению в списке
def find_floats_less_than_or_equal_to_max_in_list(lst):
    if not lst:
        return None
    max_lst = max(lst)
    result = []
    for item in lst:
        if isinstance(item, float) and item <= max_lst:
            result.append(item)
    return tuple(result) if result else None


# 1013. Функция для нахождения чисел, которые больше минимального значения в списке, но меньше максимального в словаре
def find_floats_between_min_in_list_and_max_in_dict(lst, d):
    if not lst or not d:
        return None
    min_lst = min(lst)
    max_dict = max(d.values())
    result = []
    for item in lst:
        if isinstance(item, float) and min_lst < item < max_dict:
            result.append(item)
    return tuple(result) if result else None


# 1014. Функция для создания множества, содержащего все числа, которые больше минимального в словаре и меньше максимального в списке
def create_set_between_min_in_dict_and_max_in_list(d, lst):
    if not d or not lst:
        return None
    min_dict = min(d.values())
    max_lst = max(lst)
    result = set()
    for value in d.values():
        if isinstance(value, float) and min_dict < value < max_lst:
            result.add(value)
    return result if result else None


# 1015. Функция для нахождения всех чисел в списке, которые делятся на заданное число
def find_floats_divisible_by_value_in_list(lst, value):
    if not lst:
        return None
    result = []
    for item in lst:
        if isinstance(item, float) and item % value == 0:
            result.append(item)
    return tuple(result) if result else None


# 1016. Функция для нахождения чисел, которые меньше заданного значения в списке и больше в словаре
def find_floats_between_value_in_list_and_value_in_dict(lst, d, value):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if isinstance(item, float) and item < value and any(val > value for val in d.values()):
            result.append(item)
    return tuple(result) if result else None


# 1017. Функция для подсчёта чисел в списке, которые больше средней величины всех чисел в словаре
def count_floats_greater_than_avg_in_dict(lst, d):
    if not lst or not d:
        return None
    avg_dict = sum(d.values()) / len(d)
    count = 0
    for item in lst:
        if isinstance(item, float) and item > avg_dict:
            count += 1
    return count if count > 0 else None


# 1018. Функция для нахождения всех чисел в списке, которые делятся на два заданных числа
def find_floats_divisible_by_two_values(lst, value1, value2):
    if not lst:
        return None
    result = []
    for item in lst:
        if isinstance(item, float) and item % value1 == 0 and item % value2 == 0:
            result.append(item)
    return tuple(result) if result else None


# 1019. Функция для создания множества чисел, которые больше заданного в списке
def create_set_of_floats_greater_than_value_in_list(lst, value):
    if not lst:
        return None
    result = set()
    for item in lst:
        if isinstance(item, float) and item > value:
            result.add(item)
    return result if result else None


# 1020. Функция для нахождения чисел в списке, которые меньше среднего значения в другом списке
def find_floats_less_than_avg_in_other_list(lst1, lst2):
    if not lst1 or not lst2:
        return None
    avg_lst2 = sum(lst2) / len(lst2)
    result = []
    for item in lst1:
        if isinstance(item, float) and item < avg_lst2:
            result.append(item)
    return tuple(result) if result else None


# 1021. Функция для нахождения чисел, которые больше минимального в одном списке и меньше максимального в другом списке
def find_floats_between_min_in_first_list_and_max_in_second_list(lst1, lst2):
    if not lst1 or not lst2:
        return None
    min_lst1 = min(lst1)
    max_lst2 = max(lst2)
    result = []
    for item in lst1:
        if isinstance(item, float) and min_lst1 < item < max_lst2:
            result.append(item)
    return tuple(result) if result else None


# 1022. Функция для нахождения чисел, которые меньше среднего значения всех чисел в словаре
def find_floats_less_than_avg_in_dict(lst, d):
    if not lst or not d:
        return None
    avg_dict = sum(d.values()) / len(d)
    result = []
    for item in lst:
        if isinstance(item, float) and item < avg_dict:
            result.append(item)
    return tuple(result) if result else None


# 1023. Функция для нахождения чисел, которые больше заданного значения, присутствующего в словаре
def find_floats_greater_than_value_in_dict(lst, d, value):
    if not lst or not d:
        return None
    result = []
    for item in lst:
        if isinstance(item, float) and any(val > value for val in d.values()):
            result.append(item)
    return tuple(result) if result else None


# 1024. Функция для нахождения чисел, которые больше максимального значения в одном списке и меньше максимального в другом
def find_floats_between_max_in_first_list_and_max_in_second_list(lst1, lst2):
    if not lst1 or not lst2:
        return None
    max_lst1 = max(lst1)
    max_lst2 = max(lst2)
    result = []
    for item in lst1:
        if isinstance(item, float) and max_lst1 < item < max_lst2:
            result.append(item)
    return tuple(result) if result else None


# 1025. Функция для нахождения чисел, которые являются суммой элементов из двух списков
def add_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a + b)
    if not result:
        return None
    return result


# 1026. Функция для нахождения чисел, которые являются результатом возведения элементов одного списка в квадрат
def square_list_2(lst):
    result = []
    for num in lst:
        result.append(num ** 2)
    if not result:
        return None
    return result


# 1027. Функция для нахождения чисел, которые делятся на 7, но не на 14
def find_divisible_by_7_not_14(lst):
    result = []
    for num in lst:
        if num % 7 == 0 and num % 14 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1028. Функция для нахождения чисел, которые встречаются в обоих списках
def find_common_in_lists_2(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2:
            result.append(num)
    if not result:
        return None
    return result


# 1029. Функция для нахождения чисел, которые являются произведением всех элементов списка
def multiply_list_elements(lst):
    result = 1
    for num in lst:
        result *= num
    if result == 1:
        return None
    return result


# 1030. Функция для нахождения чисел, которые являются разницей квадратов элементов из двух списков
def subtract_squares_of_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a**2 - b**2)
    if not result:
        return None
    return result


# 1031. Функция для нахождения чисел, которые делятся на 8, но не на 16
def find_divisible_by_8_not_16(lst):
    result = []
    for num in lst:
        if num % 8 == 0 and num % 16 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1032. Функция для нахождения чисел, которые представляют собой делители других чисел в списке
def find_divisors_in_list_2(lst):
    result = []
    for num in lst:
        for other in lst:
            if other != num and other % num == 0:
                result.append(num)
                break
    if not result:
        return None
    return result


# 1033. Функция для нахождения чисел, которые меньше всех элементов другого списка
def find_less_than_all_other(lst1, lst2):
    result = []
    for num in lst1:
        if all(num < x for x in lst2):
            result.append(num)
    if not result:
        return None
    return result


# 1034. Функция для нахождения чисел, которые делятся на 2 или 3
def find_divisible_by_2_or_3(lst):
    result = []
    for num in lst:
        if num % 2 == 0 or num % 3 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 1035. Функция для нахождения чисел, которые являются суммой элементов из одного списка и чисел из другого
def add_lists_elements_with_offset(lst1, lst2, offset):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a + b + offset)
    if not result:
        return None
    return result


# 1036. Функция для нахождения чисел, которые являются результатом умножения всех элементов списка на константу
def multiply_list_by_constant(lst, constant):
    result = []
    for num in lst:
        result.append(num * constant)
    if not result:
        return None
    return result


# 1037. Функция для нахождения чисел, которые не делятся на 3 и на 5
def find_not_divisible_by_3_and_5(lst):
    result = []
    for num in lst:
        if num % 3 != 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1038. Функция для нахождения чисел, которые представляют собой сумму элементов из двух списков с условием
def add_lists_conditionally(lst1, lst2, condition):
    result = []
    for a, b in zip(lst1, lst2):
        if a + b > condition:
            result.append(a + b)
    if not result:
        return None
    return result


# 1039. Функция для нахождения чисел, которые являются четными и больше 10
def find_even_and_greater_than_10(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num > 10:
            result.append(num)
    if not result:
        return None
    return result


# 1040. Функция для нахождения чисел, которые равны разности двух других элементов в списке
def find_difference_elements_in_list(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] - lst[j] == 0:
                result.append(lst[i])
    if not result:
        return None
    return result


# 1041. Функция для нахождения чисел, которые являются квадратными корнями элементов списка
def find_square_roots(lst):
    result = []
    for num in lst:
        if num >= 0:
            result.append(num ** 0.5)
    if not result:
        return None
    return result


# 1042. Функция для нахождения чисел, которые встречаются в одном списке, но не в другом
def find_unique_in_first_list(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    if not result:
        return None
    return result


# 1043. Функция для нахождения чисел, которые делятся на 10 или 12
def find_divisible_by_10_or_12(lst):
    result = []
    for num in lst:
        if num % 10 == 0 or num % 12 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 1044. Функция для нахождения чисел, которые делятся на 11, но не на 22
def find_divisible_by_11_not_22(lst):
    result = []
    for num in lst:
        if num % 11 == 0 and num % 22 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1045. Функция для нахождения чисел, которые являются факториалами элементов списка
def find_factorials(lst):
    result = []
    for num in lst:
        if num == 0:
            result.append(1)
        else:
            fact = 1
            for i in range(1, num + 1):
                fact *= i
            result.append(fact)
    if not result:
        return None
    return result


# 1046. Функция для нахождения чисел, которые являются разностью между максимальным и минимальным значением в списке
def find_diff_between_max_and_min(lst):
    result = []
    max_val = max(lst)
    min_val = min(lst)
    result.append(max_val - min_val)
    if not result:
        return None
    return result


# 1047. Функция для нахождения чисел, которые являются разностью квадратов элементов двух списков
def subtract_squares_of_lists_v2(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a**2 - b**2)
    if not result:
        return None
    return result


# 1048. Функция для нахождения чисел, которые являются произведением всех чисел из списка и заданной константы
def multiply_list_by_constant_v2(lst, constant):
    result = []
    for num in lst:
        result.append(num * constant)
    if not result:
        return None
    return result


# 1049. Функция для нахождения чисел, которые являются результатом деления всех элементов списка на заданную константу
def divide_list_by_constant(lst, constant):
    result = []
    if constant == 0:
        return None
    for num in lst:
        result.append(num / constant)
    if not result:
        return None
    return result


# 1050. Функция для нахождения чисел, которые делятся на 4 или 8, но не на 12
def find_divisible_by_4_or_8_not_12(lst):
    result = []
    for num in lst:
        if (num % 4 == 0 or num % 8 == 0) and num % 12 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1051. Функция для нахождения чисел, которые являются суммой элементов двух списков с проверкой условия
def add_lists_with_condition(lst1, lst2, condition):
    result = []
    for a, b in zip(lst1, lst2):
        if a + b > condition:
            result.append(a + b)
    if not result:
        return None
    return result


# 1052. Функция для нахождения чисел, которые являются разницей между максимальным и минимальным элементом в двух списках
def find_max_min_diff_in_lists(lst1, lst2):
    result = []
    max_val1 = max(lst1)
    min_val1 = min(lst1)
    max_val2 = max(lst2)
    min_val2 = min(lst2)
    result.append(max_val1 - min_val1)
    result.append(max_val2 - min_val2)
    if not result:
        return None
    return result


# 1053. Функция для нахождения чисел, которые делятся на 3 и на 7
def find_divisible_by_3_and_7(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 7 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 1054. Функция для нахождения чисел, которые делятся на 15, но не на 30
def find_divisible_by_15_not_30(lst):
    result = []
    for num in lst:
        if num % 15 == 0 and num % 30 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1055. Функция для нахождения чисел, которые равны разности между элементами двух списков
def subtract_lists_elements(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a - b)
    if not result:
        return None
    return result


# 1056. Функция для нахождения чисел, которые делятся на 2 и на 3, но не на 6
def find_divisible_by_2_and_3_not_6(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 == 0 and num % 6 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1057. Функция для нахождения чисел, которые являются квадратами элементов одного списка
def find_squares_of_elements(lst):
    result = []
    for num in lst:
        result.append(num**2)
    if not result:
        return None
    return result


# 1058. Функция для нахождения чисел, которые являются произведением элементов двух списков, но только тех, которые четные
def multiply_even_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if a % 2 == 0 and b % 2 == 0:
            result.append(a * b)
    if not result:
        return None
    return result


# 1059. Функция для нахождения чисел, которые делятся на 10, но не на 5
def find_divisible_by_10_not_5(lst):
    result = []
    for num in lst:
        if num % 10 == 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1060. Функция для нахождения чисел, которые равны произведению всех чисел другого списка
def find_product_of_elements_of_other_list(lst1, lst2):
    result = []
    product = 1
    for num in lst2:
        product *= num
    for num in lst1:
        if num == product:
            result.append(num)
    if not result:
        return None
    return result


# 1061. Функция для нахождения чисел, которые являются делителями числа
def find_divisors_4(lst, num):
    result = []
    for i in lst:
        if num % i == 0:
            result.append(i)
    if not result:
        return None
    return result


# 1062. Функция для нахождения чисел, которые больше всех чисел в другом списке
def find_greater_than_all_in_other_list(lst1, lst2):
    result = []
    for num in lst1:
        if all(num > x for x in lst2):
            result.append(num)
    if not result:
        return None
    return result


# 1063. Функция для нахождения чисел, которые являются результатом умножения всех чисел в списке на 2
def multiply_list_by_2(lst):
    result = []
    for num in lst:
        result.append(num * 2)
    if not result:
        return None
    return result


# 1064. Функция для нахождения чисел, которые являются результатом возведения чисел в степень, заданную как аргумент
def find_powers_of_elements(lst, power):
    result = []
    for num in lst:
        result.append(num ** power)
    if not result:
        return None
    return result


# 1065. Функция для нахождения чисел, которые больше или равны всем элементам другого списка
def find_greater_or_equal_to_all(lst1, lst2):
    result = []
    for num in lst1:
        if all(num >= x for x in lst2):
            result.append(num)
    if not result:
        return None
    return result


# 1066. Функция для нахождения чисел, которые являются разностью элементов из двух списков, с учетом определенного условия
def subtract_lists_with_condition(lst1, lst2, condition):
    result = []
    for a, b in zip(lst1, lst2):
        if a - b > condition:
            result.append(a - b)
    if not result:
        return None
    return result


# 1067. Функция для нахождения чисел, которые являются произведением элементов одного списка на элементы другого списка
def multiply_lists_elements(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a * b)
    if not result:
        return None
    return result


# 1068. Функция для нахождения чисел, которые являются делителями чисел из списка
def find_divisors_of_list_elements(lst):
    result = []
    for num in lst:
        for i in range(1, num + 1):
            if num % i == 0:
                result.append(i)
    if not result:
        return None
    return result


# 1069. Функция для нахождения чисел, которые больше или равны минимальному элементу в другом списке
def find_greater_than_or_equal_min(lst1, lst2):
    result = []
    min_val = min(lst2)
    for num in lst1:
        if num >= min_val:
            result.append(num)
    if not result:
        return None
    return result


# 1070. Функция для нахождения чисел, которые равны разнице двух элементов в одном списке
def find_difference_of_elements(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            result.append(lst[i] - lst[j])
    if not result:
        return None
    return result


# 1071. Функция для нахождения чисел, которые являются квадратными корнями элементов другого списка
def find_square_roots_of_list(lst):
    result = []
    for num in lst:
        result.append(num**0.5)
    if not result:
        return None
    return result

# 1072. Функция для нахождения чисел, которые являются разностью всех элементов двух списков по порядку
def subtract_lists_elementwise(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append(lst1[i] - lst2[i])
        else:
            result.append(lst1[i])
    if not result:
        return None
    return result


# 1073. Функция для нахождения чисел, которые встречаются в двух списках, но не одновременно в одном из них
def find_exclusive_in_both(lst1, lst2):
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


# 1074. Функция для нахождения чисел, которые являются результатом суммы чисел двух списков, если сумма больше 10
def sum_lists_if_greater_than_10(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        summ = a + b
        if summ > 10:
            result.append(summ)
    if not result:
        return None
    return result


# 1075. Функция для нахождения чисел, которые являются результатом возведения элементов одного списка в степень элементов другого
def power_of_elements(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a ** b)
    if not result:
        return None
    return result


# 1076. Функция для нахождения чисел, которые являются результатом деления элементов одного списка на элементы другого, при этом исключая делители, равные нулю
def divide_lists_with_exclusion_of_zero(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:
            result.append(a / b)
    if not result:
        return None
    return result


# 1077. Функция для нахождения чисел, которые встречаются в двух списках и являются четными
def find_even_common(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2 and num % 2 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 1078. Функция для нахождения чисел, которые меньше суммы элементов второго списка
def find_less_than_sum_of_other_list(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for num in lst1:
        if num < sum_lst2:
            result.append(num)
    if not result:
        return None
    return result


# 1079. Функция для нахождения чисел, которые являются разностью элементов одного списка от их квадратов
def subtract_from_squares(lst):
    result = []
    for num in lst:
        result.append(num**2 - num)
    if not result:
        return None
    return result


# 1080. Функция для нахождения чисел, которые являются результатом умножения чисел одного списка на числа другого, но только если результат больше 20
def multiply_lists_if_greater_than_20(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        product = a * b
        if product > 20:
            result.append(product)
    if not result:
        return None
    return result


# 1081. Функция для нахождения чисел, которые делятся на 3, но не делятся на 6
def find_divisible_by_3_not_6(lst):
    result = []
    for num in lst:
        if num % 3 == 0 and num % 6 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1082. Функция для нахождения чисел, которые присутствуют в одном из двух списков, но не в обоих, с использованием множеств
def find_unique_elements_in_sets_3(lst1, lst2):
    result = list(set(lst1) ^ set(lst2))
    if not result:
        return None
    return result


# 1083. Функция для нахождения чисел, которые являются суммой всех чисел в списке, умноженных на их индексы
def sum_elements_times_index(lst):
    result = []
    for i, num in enumerate(lst):
        result.append(num * i)
    if not result:
        return None
    return result


# 1084. Функция для нахождения чисел, которые представляют собой разность элементов одного списка, умноженных на элементы другого списка
def diff_of_multiplied_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append((a * b) - a)
    if not result:
        return None
    return result


# 1085. Функция для нахождения чисел, которые встречаются в одном из двух списков, но не в обоих, и вычисление их суммы
def find_unique_in_both_lists_and_sum(lst1, lst2):
    result = []
    total_sum = 0
    for num in lst1:
        if num not in lst2:
            result.append(num)
            total_sum += num
    for num in lst2:
        if num not in lst1:
            result.append(num)
            total_sum += num
    if not result:
        return None
    return total_sum


# 1086. Функция для нахождения чисел, которые равны произведению всех элементов одного списка и разности элементов другого списка
def multiply_by_difference_of_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append((a * b) - (b - a))
    if not result:
        return None
    return result


# 1087. Функция для нахождения чисел, которые равны разности всех элементов одного списка и их квадратичных значений
def find_difference_of_elements_and_squares(lst):
    result = []
    for num in lst:
        result.append(num - num**2)
    if not result:
        return None
    return result


# 1088. Функция для нахождения чисел, которые присутствуют в обоих списках, но только если они делятся на 5
def find_common_and_divisible_by_5(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2 and num % 5 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 1089. Функция для нахождения чисел, которые меньше всех элементов из другого списка, но больше 10
def find_less_than_all_and_gt_10(lst1, lst2):
    result = []
    for num in lst1:
        if all(num < x for x in lst2) and num > 10:
            result.append(num)
    if not result:
        return None
    return result


# 1090. Функция для нахождения чисел, которые делятся на 2 и на 4, но не на 8
def find_divisible_by_2_and_4_not_8(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 4 == 0 and num % 8 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1091. Функция для нахождения чисел, которые равны разности между квадратом и кубом числа
def find_diff_between_square_and_cube(lst):
    result = []
    for num in lst:
        result.append(num**2 - num**3)
    if not result:
        return None
    return result


# 1092. Функция для нахождения чисел, которые являются результатом возведения каждого числа в степень его индекса в списке
def power_elements_by_index(lst):
    result = []
    for i, num in enumerate(lst):
        result.append(num ** i)
    if not result:
        return None
    return result


# 1093. Функция для нахождения чисел, которые равны разности квадратов двух элементов из двух списков
def subtract_squares_of_two_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a**2 - b**2)
    if not result:
        return None
    return result


# 1094. Функция для нахождения чисел, которые являются результатом разности всех элементов одного списка, деленных на элементы другого
def subtract_divided_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:
            result.append(a - (a / b))
    if not result:
        return None
    return result


# 1095. Функция для нахождения чисел, которые представляют собой сумму всех чисел из одного списка, умноженных на их индексы
def sum_elements_times_index_v2(lst):
    result = []
    for i, num in enumerate(lst):
        result.append(num * (i + 1))
    if not result:
        return None
    return result


# 1096. Функция для нахождения чисел, которые делятся на 6 и на 8
def find_divisible_by_6_and_8(lst):
    result = []
    for num in lst:
        if num % 6 == 0 and num % 8 == 0:
            result.append(num)
    if not result:
        return None
    return result


# 1097. Функция для нахождения чисел, которые представляют собой разницу всех чисел в списке и их факториалов
def find_diff_and_factorials(lst):
    result = []
    for num in lst:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        result.append(num - fact)
    if not result:
        return None
    return result


# 1098. Функция для нахождения чисел, которые являются результатом умножения чисел одного списка на элементы другого, но только если результат меньше 100
def multiply_lists_if_less_than_100(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        product = a * b
        if product < 100:
            result.append(product)
    if not result:
        return None
    return result


# 1099. Функция для нахождения чисел, которые равны результату возведения элементов списка в степень их индекса
def find_powers_by_index(lst):
    result = []
    for i, num in enumerate(lst):
        result.append(num ** (i + 1))
    if not result:
        return None
    return result


# 1100. Функция для нахождения чисел, которые равны разности всех чисел из двух списков, умноженных на индексы
def subtract_lists_with_index(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] - lst2[i]) * i)
        else:
            result.append(lst1[i] * i)
    if not result:
        return None
    return result


# 1101. Функция для нахождения чисел, которые являются суммой всех чисел в одном списке, делённых на числа из другого
def sum_divided_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:
            result.append(a / b)
    if not result:
        return None
    return result


# 1102. Функция для нахождения чисел, которые равны разности квадратов элементов одного списка и квадратов элементов другого
def diff_of_squares(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a**2 - b**2)
    if not result:
        return None
    return result


# 1103. Функция для нахождения чисел, которые делятся на 7, но не делятся на 14 и 21
def find_divisible_by_7_not_14_or_21(lst):
    result = []
    for num in lst:
        if num % 7 == 0 and num % 14 != 0 and num % 21 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1104. Функция для нахождения чисел, которые являются суммой чисел из одного списка и разности чисел другого списка
def sum_and_diff_of_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append((a + b) - (b - a))
    if not result:
        return None
    return result


# 1105. Функция для нахождения чисел, которые являются результатом умножения чисел из одного списка на чисел другого, но только если произведение больше 50
def multiply_lists_if_greater_than_50(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        product = a * b
        if product > 50:
            result.append(product)
    if not result:
        return None
    return result


# 1106. Функция для нахождения чисел, которые делятся на 8, но не делятся на 4
def find_divisible_by_8_not_4(lst):
    result = []
    for num in lst:
        if num % 8 == 0 and num % 4 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1107. Функция для нахождения чисел, которые равны разнице квадратов всех чисел из первого списка и всех чисел из второго
def diff_of_all_squares(lst1, lst2):
    result = []
    sum_sq_lst1 = sum([num ** 2 for num in lst1])
    sum_sq_lst2 = sum([num ** 2 for num in lst2])
    result.append(sum_sq_lst1 - sum_sq_lst2)
    if not result:
        return None
    return result


# 1108. Функция для нахождения чисел, которые присутствуют в обоих списках, но только если их сумма больше 20
def find_common_and_sum_gt_20(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2 and (num + num > 20):
            result.append(num)
    if not result:
        return None
    return result


# 1109. Функция для нахождения чисел, которые являются результатом деления чисел из одного списка на числа из другого, с учётом остатка
def divide_with_remainder(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:
            result.append(a % b)
    if not result:
        return None
    return result


# 1110. Функция для нахождения чисел, которые равны произведению чисел из первого списка и чисел второго, если результат больше 100
def multiply_if_greater_than_100(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        product = a * b
        if product > 100:
            result.append(product)
    if not result:
        return None
    return result


# 1111. Функция для нахождения чисел, которые являются разностью элементов из одного списка и индексов элементов другого списка
def subtract_by_index(lst1, lst2):
    result = []
    for i, num in enumerate(lst1):
        if i < len(lst2):
            result.append(num - lst2[i])
    if not result:
        return None
    return result


# 1112. Функция для нахождения чисел, которые являются результатом возведения элементов одного списка в степень их индекса
def power_by_index(lst):
    result = []
    for i, num in enumerate(lst):
        result.append(num ** (i + 1))
    if not result:
        return None
    return result


# 1113. Функция для нахождения чисел, которые являются результатом разности чисел одного списка и элементов другого, делённых на их индексы
def diff_divided_by_index(lst1, lst2):
    result = []
    for i, (a, b) in enumerate(zip(lst1, lst2)):
        if i != 0:
            result.append((a - b) / i)
    if not result:
        return None
    return result


# 1114. Функция для нахождения чисел, которые равны произведению всех элементов списка, делённых на количество элементов другого списка
def multiply_by_len_of_other_list(lst1, lst2):
    result = []
    len_lst2 = len(lst2)
    for num in lst1:
        result.append(num * len_lst2)
    if not result:
        return None
    return result


# 1115. Функция для нахождения чисел, которые являются суммой элементов двух списков и их произведений
def sum_and_multiply_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a + b + (a * b))
    if not result:
        return None
    return result


# 1116. Функция для нахождения чисел, которые равны сумме чисел одного списка и произведению элементов другого
def sum_and_product_of_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append((a + b) * (a * b))
    if not result:
        return None
    return result


# 1117. Функция для нахождения чисел, которые делятся на 4, но не на 8 и 16
def find_divisible_by_4_not_8_or_16(lst):
    result = []
    for num in lst:
        if num % 4 == 0 and num % 8 != 0 and num % 16 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1118. Функция для нахождения чисел, которые представляют собой разницу чисел одного списка и индексов чисел другого
def subtract_by_other_list_index(lst1, lst2):
    result = []
    for i, num in enumerate(lst2):
        if i < len(lst1):
            result.append(lst1[i] - num)
    if not result:
        return None
    return result


# 1119. Функция для нахождения чисел, которые являются результатом деления чисел одного списка на индексы элементов другого списка
def divide_by_index(lst1, lst2):
    result = []
    for i, num in enumerate(lst2):
        if i != 0:
            result.append(lst1[i] / i)
    if not result:
        return None
    return result


# 1120. Функция для нахождения чисел, которые являются разностью чисел одного списка, умноженных на индексы другого списка
def diff_multiplied_by_index(lst1, lst2):
    result = []
    for i, num in enumerate(lst2):
        if i < len(lst1):
            result.append((lst1[i] - num) * i)
    if not result:
        return None
    return result


# 1121. Функция для нахождения чисел, которые равны разности квадратов элементов первого списка и индексов элементов второго
def diff_of_squares_and_indexes(lst1, lst2):
    result = []
    for i, num in enumerate(lst2):
        if i < len(lst1):
            result.append((lst1[i] ** 2) - i)
    if not result:
        return None
    return result


# 1122. Функция для нахождения чисел, которые являются разностью всех чисел первого списка и произведений чисел второго списка
def diff_of_lists_and_products(lst1, lst2):
    result = []
    product_lst2 = 1
    for num in lst2:
        product_lst2 *= num
    for num in lst1:
        result.append(num - product_lst2)
    if not result:
        return None
    return result


# 1123. Функция для нахождения чисел, которые являются результатом возведения чисел одного списка в степень числа, которое является суммой элементов второго списка
def power_by_sum_of_other_list(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for num in lst1:
        result.append(num ** sum_lst2)
    if not result:
        return None
    return result


# 1124. Функция для нахождения чисел, которые являются разностью квадратов чисел из двух списков, но с добавлением их индексов
def diff_of_squares_with_index(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] ** 2 - lst2[i] ** 2) + i)
    if not result:
        return None
    return result


# 1125. Функция для нахождения чисел, которые равны произведению всех чисел в первом списке, делённого на элементы второго списка
def multiply_by_division_of_other_list(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2) and lst2[i] != 0:
            result.append(lst1[i] * (1 / lst2[i]))
    if not result:
        return None
    return result


# 1126. Функция для нахождения чисел, которые являются результатом возведения чисел из одного списка в степень их индексов в другом
def power_by_index_of_other_list(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append(lst1[i] ** lst2[i])
    if not result:
        return None
    return result


# 1127. Функция для нахождения чисел, которые делятся на 9, но не на 3
def find_divisible_by_9_not_3(lst):
    result = []
    for num in lst:
        if num % 9 == 0 and num % 3 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1128. Функция для нахождения чисел, которые равны разности между квадратом чисел первого списка и их индексов во втором списке
def diff_of_squares_and_indexes_from_other_list(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append(lst1[i] ** 2 - lst2[i])
    if not result:
        return None
    return result


# 1129. Функция для нахождения чисел, которые являются результатом деления чисел одного списка на индексы второго списка
def divide_by_index_of_other_list(lst1, lst2):
    result = []
    for i in range(len(lst2)):
        if i != 0:
            result.append(lst1[i] / i)
    if not result:
        return None
    return result


# 1130. Функция для нахождения чисел, которые равны произведению чисел первого списка и индексов второго списка, но только если результат меньше 50
def multiply_by_index_if_less_than_50(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            product = lst1[i] * lst2[i]
            if product < 50:
                result.append(product)
    if not result:
        return None
    return result


# 1131. Функция для нахождения чисел, которые делятся на 6 и 9, но не на 12
def find_divisible_by_6_and_9_not_12(lst):
    result = []
    for num in lst:
        if num % 6 == 0 and num % 9 == 0 and num % 12 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1132. Функция для нахождения чисел, которые являются результатом разности квадратов чисел первого списка и суммы чисел второго
def diff_of_squares_and_sum_of_other_list(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for num in lst1:
        result.append(num ** 2 - sum_lst2)
    if not result:
        return None
    return result


# 1133. Функция для нахождения чисел, которые являются произведением чисел одного списка на элементы второго, делённого на их индексы
def multiply_by_divided_index(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2) and i != 0:
            result.append((lst1[i] * lst2[i]) / i)
    if not result:
        return None
    return result


# 1134. Функция для нахождения чисел, которые равны произведению всех чисел из первого списка и суммы чисел из второго
def multiply_by_sum_of_other_list_v2(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for num in lst1:
        result.append(num * sum_lst2)
    if not result:
        return None
    return result


# 1135. Функция для нахождения чисел, которые равны разности элементов одного списка от произведений элементов другого
def subtract_from_product_of_other_list_v2(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a - (a * b))
    if not result:
        return None
    return result


# 1136. Функция для нахождения чисел, которые равны разности между элементами одного списка и их произведением с индексами другого списка
def diff_and_multiply_by_index(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] - lst2[i]) * i)
    if not result:
        return None
    return result


# 1137. Функция для нахождения чисел, которые являются результатом деления всех чисел из одного списка на их индексы
def divide_by_index_of_list(lst):
    result = []
    for i in range(len(lst)):
        if i != 0:
            result.append(lst[i] / i)
    if not result:
        return None
    return result


# 1138. Функция для нахождения чисел, которые равны разности всех чисел из одного списка, умноженных на элементы второго списка
def diff_of_lists_and_multiplied_by_other_list(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] - lst2[i]) * lst2[i])
    if not result:
        return None
    return result


# 1139. Функция для нахождения чисел, которые являются разностью квадратов чисел одного списка и суммы чисел из другого
def diff_of_squares_and_sum_v2(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for num in lst1:
        result.append((num ** 2) - sum_lst2)
    if not result:
        return None
    return result


# 1140. Функция для нахождения чисел, которые являются разностью произведений элементов одного списка и их квадратов
def diff_of_product_and_square(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append((a * b) - (a ** 2))
    if not result:
        return None
    return result


# 1141. Функция для нахождения чисел, которые делятся на 4 и на 7, но не на 14
def find_divisible_by_4_and_7_not_14(lst):
    result = []
    for num in lst:
        if num % 4 == 0 and num % 7 == 0 and num % 14 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1142. Функция для нахождения чисел, которые являются результатом суммы всех элементов первого списка и разности элементов второго
def sum_and_diff_of_lists_v2(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a + b - a)
    if not result:
        return None
    return result


# 1143. Функция для нахождения чисел, которые являются произведением всех чисел из одного списка, умноженных на сумму чисел из другого
def multiply_all_and_sum_other_list(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for num in lst1:
        result.append(num * sum_lst2)
    if not result:
        return None
    return result


# 1144. Функция для нахождения чисел, которые являются результатом разности чисел одного списка и суммы элементов другого
def diff_of_lists_and_sum_other_list(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for num in lst1:
        result.append(num - sum_lst2)
    if not result:
        return None
    return result


# 1145. Функция для нахождения чисел, которые равны разности квадратов чисел одного списка и их деления на элементы второго
def diff_of_squares_and_division_by_other_list(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2) and lst2[i] != 0:
            result.append((lst1[i] ** 2) / lst2[i])
    if not result:
        return None
    return result


# 1146. Функция для нахождения чисел, которые являются результатом произведения всех элементов списка и разности элементов другого
def multiply_by_diff_of_lists(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append(lst1[i] * (lst1[i] - lst2[i]))
    if not result:
        return None
    return result


# 1147. Функция для нахождения чисел, которые делятся на 5, но не на 10 и 15
def find_divisible_by_5_not_10_and_15(lst):
    result = []
    for num in lst:
        if num % 5 == 0 and num % 10 != 0 and num % 15 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1148. Функция для нахождения чисел, которые равны разности всех чисел в первом списке и разности всех чисел во втором
def diff_of_all_lists(lst1, lst2):
    result = []
    diff_lst2 = sum(lst2) - sum(lst1)
    for num in lst1:
        result.append(num - diff_lst2)
    if not result:
        return None
    return result


# 1149. Функция для нахождения чисел, которые являются результатом разности произведений элементов двух списков
def diff_of_products(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append((a * b) - (a * b))
    if not result:
        return None
    return result


# 1150. Функция для нахождения чисел, которые являются суммой элементов первого списка и разностью элементов второго, но только если разность положительна
def sum_and_positive_diff(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        diff = a - b
        if diff > 0:
            result.append(a + diff)
    if not result:
        return None
    return result


# 1151. Функция для нахождения чисел, которые являются результатом умножения чисел первого списка на индексы второго списка, с учётом остатка от деления на 3
def multiply_by_index_with_remainder(lst1, lst2):
    result = []
    for i, num in enumerate(lst1):
        if i < len(lst2):
            product = num * lst2[i]
            result.append(product % 3)
    if not result:
        return None
    return result


# 1152. Функция для нахождения чисел, которые равны разности квадрата элементов первого списка и разности квадратов элементов второго
def diff_of_squares_of_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append((a ** 2) - (b ** 2))
    if not result:
        return None
    return result


# 1153. Функция для нахождения чисел, которые являются произведением чисел из одного списка, делённых на элементы другого, но только если результат больше 10
def multiply_and_divide_by_condition(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        if b != 0:
            result_value = (a * b) / b
            if result_value > 10:
                result.append(result_value)
    if not result:
        return None
    return result


# 1154. Функция для нахождения чисел, которые являются разностью всех чисел одного списка и произведений всех чисел из другого
def diff_from_product_of_other_list(lst1, lst2):
    result = []
    product_lst2 = 1
    for num in lst2:
        product_lst2 *= num
    for num in lst1:
        result.append(num - product_lst2)
    if not result:
        return None
    return result


# 1155. Функция для нахождения чисел, которые являются результатом возведения чисел первого списка в степень их индексов в другом списке, с условием, что степень больше 1
def power_by_index_with_condition(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2) and lst2[i] > 1:
            result.append(lst1[i] ** lst2[i])
    if not result:
        return None
    return result


# 1156. Функция для нахождения чисел, которые равны разности всех чисел одного списка и суммы всех элементов другого списка, умноженных на их индексы
def diff_and_sum_multiplied_by_indexes(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for i, num in enumerate(lst1):
        result.append(num - (sum_lst2 * i))
    if not result:
        return None
    return result


# 1157. Функция для нахождения чисел, которые являются результатом деления каждого числа первого списка на индекс соответствующего числа из второго списка, если индекс больше 2
def divide_by_index_if_greater_than_2(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if len(lst2) > i > 2:
            result.append(lst1[i] / lst2[i])
    if not result:
        return None
    return result


# 1158. Функция для нахождения чисел, которые делятся на 8, но не на 16, и вычисление их суммы
def find_divisible_by_8_not_16_and_sum(lst):
    result = []
    total_sum = 0
    for num in lst:
        if num % 8 == 0 and num % 16 != 0:
            result.append(num)
            total_sum += num
    if not result:
        return None
    return total_sum


# 1159. Функция для нахождения чисел, которые являются результатом возведения элементов одного списка в степень их индексов из другого, с условием, что результат меньше 100
def power_with_index_condition(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result_value = lst1[i] ** lst2[i]
            if result_value < 100:
                result.append(result_value)
    if not result:
        return None
    return result


# 1160. Функция для нахождения чисел, которые равны разности произведений всех чисел в одном списке и их квадратов
def diff_of_product_and_squares(lst1, lst2):
    result = []
    product_lst1 = 1
    for num in lst1:
        product_lst1 *= num
    for num in lst2:
        result.append(product_lst1 - (num ** 2))
    if not result:
        return None
    return result


# 1161. Функция для нахождения чисел, которые являются результатом возведения элементов списка в степень их индекса из другого списка, но с учётом остатка от деления на 5
def power_and_modulo(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result_value = lst1[i] ** lst2[i]
            result.append(result_value % 5)
    if not result:
        return None
    return result


# 1162. Функция для нахождения чисел, которые делятся на 6, но не на 9, и вычисление их произведения
def find_divisible_by_6_not_9_and_multiply(lst):
    result = []
    product = 1
    for num in lst:
        if num % 6 == 0 and num % 9 != 0:
            result.append(num)
            product *= num
    if not result:
        return None
    return product


# 1163. Функция для нахождения чисел, которые равны разности элементов одного списка и разности всех элементов другого списка
def diff_of_lists_and_total_diff(lst1, lst2):
    result = []
    diff_lst2 = sum(lst2) - sum(lst1)
    for num in lst1:
        result.append(num - diff_lst2)
    if not result:
        return None
    return result


# 1164. Функция для нахождения чисел, которые являются результатом умножения чисел одного списка на индексы второго, с учётом разности от их суммы
def multiply_by_index_and_diff(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for i, num in enumerate(lst1):
        if i < len(lst2):
            result.append((num * i) - sum_lst2)
    if not result:
        return None
    return result


# 1165. Функция для нахождения чисел, которые равны разности всех чисел из одного списка и индексов другого списка, умноженных на их квадраты
def diff_and_index_squared(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] - lst2[i]) * (i ** 2))
    if not result:
        return None
    return result


# 1166. Функция для нахождения чисел, которые равны разности между произведениями элементов из двух списков и их индексами
def diff_of_product_and_index(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] * lst2[i]) - i)
    if not result:
        return None
    return result


# 1167. Функция для нахождения чисел, которые равны разности элементов одного списка и их произведений с элементами другого списка
def diff_and_product_of_lists(lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a - (a * b))
    if not result:
        return None
    return result


# 1168. Функция для нахождения чисел, которые являются результатом произведения чисел первого списка на индексы второго списка, делённые на их сумму
def multiply_by_index_divided_by_sum(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for i in range(len(lst1)):
        if i < len(lst2) and sum_lst2 != 0:
            result.append((lst1[i] * lst2[i]) / sum_lst2)
    if not result:
        return None
    return result


# 1169. Функция для нахождения чисел, которые равны разности квадратов элементов одного списка и их индексов в другом списке
def diff_of_squares_and_indexes_v2(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] ** 2) - lst2[i])
    if not result:
        return None
    return result


# 1170. Функция для нахождения чисел, которые делятся на 7 и на 11, но не на 77
def find_divisible_by_7_and_11_not_77(lst):
    result = []
    for num in lst:
        if num % 7 == 0 and num % 11 == 0 and num % 77 != 0:
            result.append(num)
    if not result:
        return None
    return result


# 1171. Функция для нахождения чисел, которые равны разности всех чисел из одного списка и всех чисел из другого списка
def diff_of_all_lists_v2(lst1, lst2):
    result = []
    sum_lst1 = sum(lst1)
    sum_lst2 = sum(lst2)
    for num in lst1:
        result.append(num - (sum_lst1 - sum_lst2))
    if not result:
        return None
    return result


# 1172. Функция для нахождения чисел, которые равны произведению чисел одного списка и индексов другого, умноженных на их квадрат
def multiply_by_index_and_square(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] * lst2[i]) * (i ** 2))
    if not result:
        return None
    return result


# 1173. Функция для нахождения чисел, которые делятся на 5, но не на 10 и 15, и вычисление их произведения
def find_divisible_by_5_not_10_and_15_and_multiply(lst):
    result = []
    product = 1
    for num in lst:
        if num % 5 == 0 and num % 10 != 0 and num % 15 != 0:
            result.append(num)
            product *= num
    if not result:
        return None
    return product


# 1174. Функция для нахождения чисел, которые равны произведению всех чисел первого списка и суммы чисел второго, делённой на количество элементов второго списка
def multiply_by_sum_and_len_other_list(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    len_lst2 = len(lst2)
    for num in lst1:
        result.append(num * (sum_lst2 / len_lst2))
    if not result:
        return None
    return result


# 1175. Функция для нахождения чисел, которые являются результатом умножения чисел первого списка на индексы второго списка, но только если произведение больше 20
def multiply_by_index_if_greater_than_20(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            product = lst1[i] * lst2[i]
            if product > 20:
                result.append(product)
    if not result:
        return None
    return result


# 1176. Функция для нахождения чисел, которые равны произведению чисел одного списка и их квадратов, делённых на элементы другого
def multiply_by_square_divided(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] ** 2) * lst2[i])
    if not result:
        return None
    return result


# 1177. Функция для нахождения чисел, которые являются разностью всех чисел первого списка и суммы всех чисел второго, умноженной на их индексы
def diff_from_sum_multiplied_by_index(lst1, lst2):
    result = []
    sum_lst2 = sum(lst2)
    for i, num in enumerate(lst1):
        result.append(num - (sum_lst2 * i))
    if not result:
        return None
    return result


# 1178. Функция для нахождения чисел, которые являются результатом деления элементов одного списка на индексы элементов другого списка, если индекс меньше 5
def divide_by_index_if_less_than_5(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2) and i < 5:
            result.append(lst1[i] / lst2[i])
    if not result:
        return None
    return result


# 1179. Функция для нахождения чисел, которые равны произведению чисел первого списка на разность всех чисел второго
def multiply_by_diff_of_other_list(lst1, lst2):
    result = []
    diff_lst2 = sum(lst2) - sum(lst1)
    for num in lst1:
        result.append(num * diff_lst2)
    if not result:
        return None
    return result


# 1180. Функция для нахождения чисел, которые делятся на 4, но не на 8, и вычисление их произведения
def find_divisible_by_4_not_8_and_multiply(lst):
    result = []
    product = 1
    for num in lst:
        if num % 4 == 0 and num % 8 != 0:
            result.append(num)
            product *= num
    if not result:
        return None
    return product


# 1181. Функция для нахождения чисел, которые равны произведению чисел одного списка на индексы второго, делённых на их квадраты
def multiply_by_index_divided_by_square(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2) and i != 0:
            result.append((lst1[i] * lst2[i]) / (i ** 2))
    if not result:
        return None
    return result


# 1182. Функция для нахождения чисел, которые равны разности всех чисел первого списка и произведений всех чисел из второго, умноженных на индексы
def diff_and_product_multiplied_by_index(lst1, lst2):
    result = []
    product_lst2 = 1
    for num in lst2:
        product_lst2 *= num
    for i, num in enumerate(lst1):
        result.append(num - (product_lst2 * i))
    if not result:
        return None
    return result


# 1183. Функция для нахождения чисел, которые равны произведению всех элементов одного списка и разности всех чисел другого
def multiply_by_diff_of_all_lists(lst1, lst2):
    result = []
    total_diff = sum(lst1) - sum(lst2)
    for num in lst1:
        result.append(num * total_diff)
    if not result:
        return None
    return result


# 1184. Функция для нахождения чисел, которые являются результатом возведения элементов первого списка в степень их индексов в другом списке
def power_by_index_v2(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append(lst1[i] ** lst2[i])
    if not result:
        return None
    return result


# 1185. Функция для нахождения чисел, которые делятся на 2 и на 5, но не на 10, и вычисление их произведения
def find_divisible_by_2_and_5_not_10_and_multiply(lst):
    result = []
    product = 1
    for num in lst:
        if num % 2 == 0 and num % 5 == 0 and num % 10 != 0:
            result.append(num)
            product *= num
    if not result:
        return None
    return product


# 1186. Функция для нахождения чисел, которые равны разности всех чисел из одного списка и произведений элементов другого, с учётом их индексов
def diff_and_product_with_index(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append(lst1[i] - (lst2[i] * i))
    if not result:
        return None
    return result


# 1187. Функция для нахождения чисел, которые являются разностью всех чисел первого списка и разности всех чисел второго списка, умноженных на их индексы
def diff_of_all_and_index_product(lst1, lst2):
    result = []
    total_diff_lst2 = sum(lst2) - sum(lst1)
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append(lst1[i] - (total_diff_lst2 * i))
    if not result:
        return None
    return result


# 1188. Функция для нахождения чисел, которые равны произведению всех чисел из одного списка и разности всех чисел второго списка
def multiply_and_diff_of_lists_v2(lst1, lst2):
    result = []
    total_diff = sum(lst1) - sum(lst2)
    for num in lst1:
        result.append(num * total_diff)
    if not result:
        return None
    return result


# 1189. Функция для нахождения чисел, которые являются результатом разности произведений элементов первого списка и их индексов
def diff_of_product_and_index_v3(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if i < len(lst2):
            result.append((lst1[i] * lst2[i]) - (i ** 2))
    if not result:
        return None
    return result


# 1190. Функция для нахождения значений, которые равны разности значений одинаковых ключей из двух словарей
def diff_of_values_in_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2:
            result.append(dict1[key] - dict2[key])
    if not result:
        return None
    return result


# 1191. Функция для нахождения ключей, которые присутствуют в обоих словарях, но только если их значения больше 10
def find_common_keys_with_values_gt_10(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2 and dict1[key] > 10 and dict2[key] > 10:
            result.append(key)
    if not result:
        return None
    return result


# 1192. Функция для нахождения значений, которые равны произведению значений одного словаря и их индексов в другом
def multiply_values_by_index_in_other_dict(dict1, dict2):
    result = []
    for i, key in enumerate(dict1):
        if key in dict2:
            result.append(dict1[key] * dict2.get(key, 0) * i)
    if not result:
        return None
    return result


# 1193. Функция для нахождения ключей, у которых значения из первого словаря больше значений из второго
def find_keys_with_value_greater_in_first_dict(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2 and dict1[key] > dict2[key]:
            result.append(key)
    if not result:
        return None
    return result


# 1194. Функция для нахождения ключей, значения которых в обоих словарях совпадают
def find_keys_with_equal_values_in_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2 and dict1[key] == dict2[key]:
            result.append(key)
    if not result:
        return None
    return result


# 1195. Функция для нахождения значений, которые равны разности значений одного словаря и значения того же ключа в другом словаре
def find_value_diff_between_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2:
            result.append(dict1[key] - dict2[key])
    if not result:
        return None
    return result


# 1196. Функция для нахождения значений, которые являются результатом умножения значений одинаковых ключей из двух словарей
def multiply_values_in_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2:
            result.append(dict1[key] * dict2[key])
    if not result:
        return None
    return result


# 1197. Функция для нахождения ключей, которые присутствуют в обоих словарях, но значения которых делятся на 3
def find_keys_with_values_divisible_by_3(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2 and dict1[key] % 3 == 0 and dict2[key] % 3 == 0:
            result.append(key)
    if not result:
        return None
    return result


# 1198. Функция для нахождения ключей, у которых значения из первого словаря меньше значений из второго, но больше 5
def find_keys_with_value_range_in_dicts(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2 and dict2[key] > dict1[key] > 5:
            result.append(key)
    if not result:
        return None
    return result


# 1199. Функция для сортировки массива по убыванию с использованием пузырьковой сортировки
def bubble_sort_descending(arr):
    result = arr[:]
    n = len(result)
    for i in range(n):
        for j in range(0, n-i-1):
            if result[j] < result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
    if not result:
        return None
    return result


# 1200. Функция для сортировки массива по возрастанию с использованием сортировки вставками
def insertion_sort_ascending(arr):
    result = arr[:]
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and key < result[j]:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    if not result:
        return None
    return result
