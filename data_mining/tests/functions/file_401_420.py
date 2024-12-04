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
