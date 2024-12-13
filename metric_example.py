# Импортируем только эти две функции из модуля, всё остальные в нём - служебные
from metric_module.metric import coverage_percent, calculate_coverage_for_df

import pandas as pd

# В начале кода не должно быть переноса строки, код должен начинаться с def
code = '''def is_even(n):
    if n < 0:
        print("Negative number, can't be checked for evenness.")
        return False
    if n % 2 == 0:
        return True
    else:
        if n == 1:
            print("One is odd!")
        return False'''

# То же самое для тестирующей функции
test = '''def test_is_even():
    assert is_even(4) is True
    assert is_even(0) is True
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(1) is False
    assert is_even(7) is False
    assert is_even(-2) is False
    assert is_even(-3) is False
    assert is_even(-7) is False'''

code2 = '''def product_of_floats(lst):
    if not lst:
        return None
    product = 1.0
    for num in lst:
        if isinstance(num, (int, float)):
            product *= num
        else:
            return None
    return product
'''

test2 = '''def test_product_of_floats():
    assert product_of_floats([1.2, 3.4, 5.6]) == pytest.approx(22.848)
    assert product_of_floats([-1.1, -2.2, -3.3]) == pytest.approx(-7.986)
    assert product_of_floats([]) is None
    assert product_of_floats([1, 2, 3, 'a', 0]) is None
    assert product_of_floats([1.1, -2, 3]) == pytest.approx(-6.6)
'''

code3 = '''def remove_punctuation_from_string(s):
    punctuation = '!"#$%&()*+,-./:;<=>?@[]^_`{|}~'
    result = ''
    for char in s:
        if char not in punctuation:
            result += char
    return result
'''

test3 = '''def test_remove_punctuation_from_string():
    assert remove_punctuation_from_string("hello, world!") == "hello world"
    assert remove_punctuation_from_string("a.b.c!") == "abc"
    assert remove_punctuation_from_string("") == ""
    assert remove_punctuation_from_string("no_punctuation") == "nopunctuation"
'''

if __name__ == '__main__':  # Это здесь обязательно, если на Windows, так как используется мультипроцессинг

    # /Рассчитаем метрики для отдельных строк/ #

    # Процент покрытия, количество ошибок выполнения, список пропущенных строк
    percent1, errors1, missing1 = coverage_percent(code, test)
    percent2, errors2, missing2 = coverage_percent(code2, test2)
    percent3, errors3, missing3 = coverage_percent(code3, test3)

    print(f'Test 1. Процент покрытия: {percent1} %, Количество ошибок: {errors1}, Пропущенные строчки: {missing1}')
    print(f'Test 2. Процент покрытия: {percent2} %, Количество ошибок: {errors2}, Пропущенные строчки: {missing2}')
    print(f'Test 2. Процент покрытия: {percent3} %, Количество ошибок: {errors3}, Пропущенные строчки: {missing3}')

    # /Рассчитаем метрики для целого датафрейма/ #
    df = pd.read_csv("data/04_functions_tests_1200.csv")

    # Рассчитываем покрытие и ошибки для каждой строки в DataFrame
    # ВАЖНО! Функция никуда не записывает result_df, она только его возвращает

    # Итоговый df с метриками, среднее значение покрытия, среднее значение ошибок выполнения
    result_df, mean_cov, mean_err = calculate_coverage_for_df(df)
    result_df.to_csv("tests_metric.csv", index=False)

    # Выводим результат
    print(f'Mean cov: {mean_cov}.')
    print(f'Mean err: {mean_err}.')
