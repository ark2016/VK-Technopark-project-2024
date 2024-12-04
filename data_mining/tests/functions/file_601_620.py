# 601. Функция для нахождения произведения чисел, которые меньше X в списке (рекурсия)
def product_less_than_x(lst, x):
    if not lst:
        return 1
    return (lst[0] if lst[0] < x else 1) * product_less_than_x(lst[1:], x)


# 602. Функция для нахождения суммы всех чисел в строке, которые можно преобразовать в числа (рекурсия)
def sum_of_numbers_in_string(s):
    if s == "":
        return 0
    current_num = ""
    if s[0].isdigit():
        current_num += s[0]
    elif current_num:
        return int(current_num) + sum_of_numbers_in_string(s[1:])
    return sum_of_numbers_in_string(s[1:])


# 603. Функция для нахождения всех четных чисел в строке, которые можно преобразовать в числа (рекурсия)
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
    steps = steps % n
    if steps == 0:
        return arr
    if steps < 0:
        rotated = arr[steps:] + arr[:steps]
    else:
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
