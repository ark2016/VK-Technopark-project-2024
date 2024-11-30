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
