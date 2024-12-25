# 521. Функция для проверки, является ли строка анаграммой другой строки
def are_anagrams_2(s1, s2):
    if not s1 or not s2:
        return None
    return sorted(s1) == sorted(s2)


# 522. Функция для извлечения всех чисел, расположенных в строке
def extract_numbers_from_string_2(s):
    if not s:
        return None
    numbers = []
    current_number = []
    for ch in s:
        if ch.isdigit():
            current_number.append(ch)
        elif current_number:
            numbers.append(''.join(current_number))
            current_number = []
    if current_number:
        numbers.append(''.join(current_number))
    return numbers if numbers else None


# 523. Функция для проверки, является ли строка палиндромом (с учётом пробелов)
def is_palindrome_with_spaces(s):
    if not s:
        return None
    clean_s = ''.join(s.split()).lower()
    return clean_s == clean_s[::-1]


# 524. Функция для подсчёта количества гласных и согласных в строке
def count_vowels_and_consonants(s):
    if not s:
        return None
    vowels = "aeiouAEIOU"
    consonants = 0
    vowels_count = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                vowels_count += 1
            else:
                consonants += 1
    if vowels_count == 0 and consonants == 0:
        return None
    return {"vowels": vowels_count, "consonants": consonants}


# 525. Функция для удаления всех пробелов в строке, а затем инвертирования
def remove_spaces_and_reverse(s):
    if not s:
        return None
    no_spaces = s.replace(" ", "")
    return no_spaces[::-1]


# 526. Функция для нахождения подстроки с максимальной длиной без повторяющихся символов
def longest_unique_substring(s):
    if not s:
        return None
    max_len = 0
    max_substring = ""
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
        if len(seen) > max_len:
            max_len = len(seen)
            max_substring = s[i:i + max_len]
    return max_substring if max_len > 0 else None


# 527. Функция для нахождения наибольшего общего префикса двух строк
def longest_common_prefix(s1, s2):
    if not s1 or not s2:
        return None
    prefix = []
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            prefix.append(s1[i])
        else:
            break
    return ''.join(prefix) if prefix else None


# 528. Функция для подсчёта повторяющихся слов в строке
def count_repeating_words(s):
    if not s:
        return None
    words = s.split()
    word_count = {}
    for word in words:
        word_count[word.lower()] = word_count.get(word.lower(), 0) + 1
    return {word: count for word, count in word_count.items() if count > 1}


# 529. Функция для нахождения самого длинного слова в строке
def longest_word_in_string(s):
    if not s:
        return None
    words = s.split()
    return max(words, key=len) if words else None


# 530. Функция для извлечения подстрок длиной N
def extract_substrings_of_length_n(s, n):
    if not s or n <= 0:
        return None
    return [s[i:i + n] for i in range(len(s) - n + 1)]


# 531. Функция для удаления всех слов, которые начинаются на определённую букву
def remove_words_starting_with(s, letter):
    if not s or not letter:
        return None
    words = s.split()
    filtered_words = [word for word in words if not word.lower().startswith(letter.lower())]
    return ' '.join(filtered_words) if filtered_words else None


# 532. Функция для замены всех пробелов на подчеркивания
def replace_spaces_with_underscores(s):
    if not s:
        return None
    return s.replace(" ", "_")


# 533. Функция для извлечения всех буквенных символов и их сортировки по алфавиту
def sort_letters_in_string(s):
    if not s:
        return None
    letters = [ch for ch in s if ch.isalpha()]
    letters.sort()
    return ''.join(letters)


# 534. Функция для удаления всех чисел из строки
def remove_numbers_from_string(s):
    if not s:
        return None
    return ''.join([ch for ch in s if not ch.isdigit()])


# 535. Функция для нахождения всех вхождений строки с учётом регистра
def find_case_sensitive_occurrences(s, substring):
    if not s or not substring:
        return None
    indices = []
    i = 0
    while i < len(s):
        i = s.find(substring, i)
        if i == -1:
            break
        indices.append(i)
        i += 1
    return indices if indices else None


# 536. Функция для удаления всех гласных из строки
def remove_vowels_from_string(s):
    if not s:
        return None
    vowels = "aeiouAEIOU"
    return ''.join([ch for ch in s if ch not in vowels])


# 537. Функция для вычисления расстояния Левенштейна между двумя строками
def levenshtein_distance(s1, s2):
    if not s1 or not s2:
        return None
    len_s1, len_s2 = len(s1), len(s2)
    dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    for i in range(len_s1 + 1):
        for j in range(len_s2 + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[len_s1][len_s2]


# 538. Функция для нахождения всех возможных подстрок строки заданной длины
def fixed_length_substrings(s, length):
    if not s or length <= 0:
        return None
    return [s[i:i + length] for i in range(len(s) - length + 1)]


# 539. Функция для удаления всех дублирующихся символов в строке
def remove_duplicates_from_string(s):
    if not s:
        return None
    return ''.join(sorted(set(s), key=s.index))


# 540. Функция для нахождения среднего арифметического с плавающими точками
def average_of_floats(lst):
    def sum_of_floats(lst):
        total = 0.0
        for num in lst:
            if isinstance(num, (int, float)):
                total += num
            else:
                return None
        return total
    if not lst:
        return None
    total = sum_of_floats(lst)
    if total is None:
        return None
    return total / len(lst)
