# 821. Функция для получения всех чисел из строки
def extract_numbers_from_string_4(s):
    numbers = []
    temp = ''
    for char in s:
        if char.isdigit():
            temp += char
        elif temp:
            numbers.append(int(temp))
            temp = ''
    if temp:
        numbers.append(int(temp))
    return numbers if numbers else None


# 822. Функция для проверки, является ли строка буквой
def is_string_single_letter(s):
    return len(s) == 1 and s.isalpha()


# 823. Функция для получения строки с заглавными буквами
def get_uppercase_letters(s):
    uppercase = ''
    for char in s:
        if char.isupper():
            uppercase += char
    return uppercase if uppercase else None


# 824. Функция для удаления всех символов, которые встречаются в строке более одного раза
def remove_duplicates_from_string_2(s):
    result = ''
    seen = set()
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result


# 825. Функция для нахождения всех подстрок заданной длины
def find_substrings_of_length(s, length):
    substrings = []
    for i in range(len(s) - length + 1):
        substrings.append(s[i:i + length])
    return substrings if substrings else None


# 826. Функция для нахождения самой длинной буквы в строке
def find_longest_alphabetic_char(s):
    longest = ''
    for char in s:
        if char.isalpha() and len(char) > len(longest):
            longest = char
    return longest if longest else None


# 827. Функция для поиска самой частой буквы в строке
def find_most_frequent_char(s):
    frequency = {}
    for char in s:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    most_frequent = max(frequency, key=frequency.get, default=None)
    return most_frequent


# 828. Функция для разделения строки на части по символу
def split_string_by_char(s, char):
    parts = []
    temp = ''
    for c in s:
        if c == char:
            if temp:
                parts.append(temp)
                temp = ''
        else:
            temp += c
    if temp:
        parts.append(temp)
    return parts if parts else None


# 829. Функция для замены всех цифр на символ `*`
def replace_digits_with_asterisks(s):
    result = ''
    for char in s:
        if char.isdigit():
            result += '*'
        else:
            result += char
    return result


# 830. Функция для нахождения всех подстрок, начинающихся на заглавную букву
def find_substrings_starting_with_uppercase(s):
    substrings = []
    temp = ''
    for char in s:
        if char.isupper() and temp:
            substrings.append(temp)
            temp = ''
        temp += char
    if temp:
        substrings.append(temp)
    return substrings if substrings else None


# 831. Функция для преобразования строки в список символов
def string_to_list_of_chars(s):
    return list(s) if s else None


# 832. Функция для поиска самого длинного слова в строке
def find_longest_word(s):
    words = s.split()
    if not words:
        return None
    return max(words, key=len)


# 833. Функция для нахождения строки, которая является комбинацией двух других
def is_combination_of_two(s, s1, s2):
    return s == s1 + s2


# 834. Функция для проверки, является ли строка числовой
def is_numeric_string(s):
    return s.isdigit() if s else False


# 835. Функция для подсчета всех слов в строке, начинающихся с гласной
def count_words_starting_with_vowel(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for word in s.split():
        if word[0] in vowels:
            count += 1
    return count if count > 0 else None


# 836. Функция для нахождения всех слов длиной больше 3 символов
def find_words_longer_than_3(s):
    words = s.split()
    result = [word for word in words if len(word) > 3]
    return result if result else None


# 837. Функция для удаления всех гласных в строке
def remove_vowels_from_string_2(s):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in s:
        if char not in vowels:
            result += char
    return result if result != s else None


# 838. Функция для замены всех пробелов на подчеркивания
def replace_spaces_with_underscores_6(s):
    return s.replace(' ', '_') if s else None


# 839. Функция для нахождения всех цифр в строке
def find_digits_in_string(s):
    digits = ''
    for char in s:
        if char.isdigit():
            digits += char
    return digits if digits else None


# 840. Функция для подсчета всех букв в строке
def count_letters_in_string(s):
    count = 0
    for char in s:
        if char.isalpha():
            count += 1
    return count if count > 0 else None
