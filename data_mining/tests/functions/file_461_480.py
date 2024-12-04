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
