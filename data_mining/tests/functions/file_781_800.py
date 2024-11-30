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
