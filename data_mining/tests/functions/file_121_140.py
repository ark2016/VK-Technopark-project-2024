# 121. Функция для нахождения всех чисел, которые являются кратными числам из другого списка
def multiples_from_list(lst1, lst2):
    multiples = []
    for num in lst1:
        for divisor in lst2:
            if num % divisor == 0:
                multiples.append(num)
                break
    if not multiples:
        print("No numbers are divisible by elements from the second list.")
    return multiples


# 122. Функция для подсчёта частоты вхождения каждого символа в строке, игнорируя регистр
def case_insensitive_char_frequency(s):
    freq = {}
    for char in s.lower():
        if char.isalpha():
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    if not freq:
        print("No alphabetical characters found.")
    return freq


# 123. Функция для подсчёта всех различных элементов в списке, с учётом их частоты
def count_unique_with_frequency(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency


# 124. Функция для подсчёта, сколько раз каждый символ в строке встречается подряд
def count_consecutive_chars(s):
    if not s:
        print("Empty string provided.")
        return {}
    count = {}
    current_char = s[0]
    current_count = 1
    for char in s[1:]:
        if char == current_char:
            current_count += 1
        else:
            if current_char in count:
                count[current_char] += current_count
            else:
                count[current_char] = current_count
            current_char = char
            current_count = 1
    if current_char in count:
        count[current_char] += current_count
    else:
        count[current_char] = current_count
    return count


# 125. Функция для нахождения всех элементов в множестве, которые присутствуют в словаре в качестве ключей
def find_keys_in_set(s, d):
    result = []
    for item in s:
        if item in d:
            result.append(item)
    if not result:
        print("No elements from the set found in the dictionary keys.")
    return sorted(result)


# 126. Функция для нахождения всех чисел в списке, которые являются простыми
def find_prime_numbers(lst):
    primes = []
    for num in lst:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


# 127. Функция для разделения строки на два списка: один с цифрами, второй с остальными символами
def split_digits_and_others(s):
    digits = []
    others = []
    for char in s:
        if char.isdigit():
            digits.append(char)
        else:
            others.append(char)
    return digits, others


# 128. Функция для получения кортежа с минимальным и максимальным элементами списка
def min_max_tuple(lst):
    if not lst:
        print("List is empty.")
        return None
    return min(lst), max(lst)


# 129. Функция для поиска элементов, которые присутствуют в двух словарях, но имеют разные значения
def find_common_keys_with_different_values(d1, d2):
    common_keys = set(d1.keys()) & set(d2.keys())
    result = []
    for key in common_keys:
        if d1[key] != d2[key]:
            result.append(key)
    if not result:
        print("No keys with different values found.")
    return result


# 130. Функция для преобразования строки в список чисел, разделённых пробелами, если в строке присутствуют только числа
def string_to_numbers(s):
    try:
        return [int(x) for x in s.split()]
    except ValueError:
        print("String contains non-numeric values.")
        return []


# 131. Функция для нахождения чисел в строке, которые могут быть переведены в степень двойки
def find_powers_of_two_in_string(s):
    numbers = []
    for word in s.split():
        try:
            num = int(word)
            if (num & (num - 1)) == 0 and num > 0:
                numbers.append(num)
        except ValueError:
            continue
    return numbers


# 132. Функция для нахождения слов, которые являются палиндромами
def find_palindromes(lst):
    palindromes = []
    for word in lst:
        if word == word[::-1]:
            palindromes.append(word)
    return palindromes


# 133. Функция для объединения двух списков с проверкой на дубликаты
def merge_lists_no_duplicates(lst1, lst2):
    result = lst1.copy()
    for item in lst2:
        if item not in result:
            result.append(item)
        else:
            print(f"Duplicate item found: {item}")
    return result


# 134. Функция для нахождения всех чисел, которые делятся на 2, но не делятся на 3
def divisible_by_2_not_3(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 != 0:
            result.append(num)
    if not result:
        print("No numbers divisible by 2 but not by 3 found.")
    return result


# 135. Функция для нахождения всех чисел в строке, которые являются чётными
def find_even_numbers_in_string(s):
    result = []
    current_num = ''
    for char in s:
        if char.isdigit():
            current_num += char
        elif current_num:
            num = int(current_num)
            if num % 2 == 0:
                result.append(num)
            current_num = ''
    if current_num:
        num = int(current_num)
        if num % 2 == 0:
            result.append(num)
    return result


# 136. Функция для нахождения всех чисел, которые не являются простыми
def find_non_prime_numbers(lst):
    non_primes = []
    for num in lst:
        if num < 2:
            non_primes.append(num)
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    non_primes.append(num)
                    break
    return non_primes


# 137. Функция для нахождения всех уникальных символов в строке, игнорируя пробелы
def unique_chars_ignore_spaces(s):
    unique_chars = {}
    for char in s:
        if char != ' ':
            if char not in unique_chars:
                unique_chars[char] = 1
            else:
                unique_chars[char] += 1
    return list(unique_chars.keys())


# 138. Функция для подсчёта слов в строке, игнорируя знаки препинания
def count_words_ignore_punctuation(s):
    word_count = 0
    current_word = ''
    for char in s:
        if char.isalnum():
            current_word += char
        elif current_word:
            word_count += 1
            current_word = ''
    if current_word:
        word_count += 1
    return word_count


# 139. Функция для нахождения всех чисел, которые являются квадратами целых чисел
def find_squares(lst):
    squares = []
    for num in lst:
        if int(num ** 0.5) ** 2 == num:
            squares.append(num)
    return squares


# 140. Функция для подсчёта количества повторений каждого слова в строке
def word_frequency_in_string(s):
    word_count = {}
    current_word = ''
    for char in s:
        if char.isalnum():
            current_word += char
        elif current_word:
            if current_word in word_count:
                word_count[current_word] += 1
            else:
                word_count[current_word] = 1
            current_word = ''
    if current_word:
        if current_word in word_count:
            word_count[current_word] += 1
        else:
            word_count[current_word] = 1
    return word_count
