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
