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
