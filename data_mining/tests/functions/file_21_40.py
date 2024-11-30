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
