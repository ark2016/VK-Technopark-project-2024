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
