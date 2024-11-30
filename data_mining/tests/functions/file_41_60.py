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
