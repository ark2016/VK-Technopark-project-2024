import ast
import contextlib
import multiprocessing
import os
import tempfile
import coverage
import pytest
import re

from tqdm import tqdm


# Плагин для сбора результатов тестов
class TestResultCollector:
    def __init__(self):
        self.failed_tests = 0
        self.passed_tests = 0

    def pytest_runtest_logreport(self, report):
        if report.when == 'call':
            if report.failed:
                self.failed_tests += 1
            elif report.passed:
                self.passed_tests += 1


# Функция для добавления импорта в начало кода
def add_import_to_code(code: str, module_name: str) -> str:
    return f"from {module_name} import *\n\n" + code


def add_import_module_to_code(code: str, module_name: str) -> str:
    return f"import {module_name}\n\n" + code


# Функция для разделения тестов на отдельные функции
# Обновлённая функция для разделения тестов на отдельные функции, игнорируя комментарии и поддерживая различные операторы
def split_test_function(code: str) -> str:
    """
    Разделяет тестовую функцию на отдельные функции, каждая из которых содержит одно assert выражение.
    Игнорирует закомментированные assert выражения и поддерживает различные операторы сравнения.
    """
    # Регулярное выражение для поиска assert выражений, не закомментированных
    # Оно захватывает:
    # - Любые пробельные символы в начале строки
    # - Ключевое слово assert
    # - Левое выражение (non-greedy)
    # - Оператор сравнения (==, !=, is, is not)
    # - Правое выражение
    test_case_pattern = r'^\s*assert\s+(.*?)\s+(==|!=|is\s+not|is)\s+(.*)$'
    function_name_pattern = r'def\s+(test_\w+)\s*\('

    # Находим название функции
    function_match = re.search(function_name_pattern, code, re.MULTILINE)
    if not function_match:
        raise ValueError("Не удалось найти название тестовой функции.")

    function_name = function_match.group(1)

    # Находим все assert выражения, игнорируя закомментированные
    test_cases = re.findall(test_case_pattern, code, re.MULTILINE)

    # Генерируем новый код
    new_code = ""
    for i, (expression, operator, expected) in enumerate(test_cases, 1):
        # Убираем лишние пробелы в операторах
        operator = operator.strip()
        new_function_name = f"{function_name}_{i}"
        new_code += f"def {new_function_name}():\n"
        new_code += f"    assert {expression} {operator} {expected}\n\n"

    # print(new_code)

    return new_code


# Функция для выполнения тестов в отдельном процессе
def run_coverage_process(code_string, test_string, queue):
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            code_filename = os.path.join(temp_dir, 'user_code.py')  # Изменено имя файла
            test_filename = os.path.join(temp_dir, 'test_user_code.py')  # Соответствующее имя тестового файла

            # Запись кода и тестов во временные файлы
            with open(code_filename, 'w', encoding='utf-8') as f:
                f.write(code_string)

            # Разделение тестов и добавление импорта
            test_string = split_test_function(test_string)
            test_string = add_import_to_code(test_string, 'user_code')  # Обновлён модуль
            test_string = add_import_module_to_code(test_string, 'pytest')

            # print(test_string)

            with open(test_filename, 'w', encoding='utf-8') as f:
                f.write(test_string)

            # Перенаправление вывода в devnull для подавления
            with open(os.devnull, 'w') as devnull:
                with contextlib.redirect_stdout(devnull), contextlib.redirect_stderr(devnull):
                    # Переход в временную директорию
                    original_cwd = os.getcwd()
                    os.chdir(temp_dir)

                    try:
                        # Инициализация coverage
                        cov = coverage.Coverage()
                        cov.erase()
                        cov.start()

                        # Инициализация плагина для сбора результатов тестов
                        collector = TestResultCollector()

                        # Запуск pytest с очисткой кеша
                        pytest_args = [test_filename, '--cache-clear']
                        pytest_result = pytest.main(pytest_args, plugins=[collector])

                        # Остановка coverage
                        cov.stop()
                        cov.save()

                        # Получение процента покрытия
                        total_percentage = cov.report(include=[code_filename], show_missing=True)

                        # Анализ покрытия
                        _, executed_lines, missing_lines, _ = cov.analysis(code_filename)

                        # Отправка результатов через очередь
                        queue.put((total_percentage, collector.failed_tests, missing_lines))
                    finally:
                        # Возвращение в исходную директорию
                        os.chdir(original_cwd)
    except Exception as e:
        # Отправка исключений через очередь
        queue.put(e)


# Обновленная функция coverage_percent, использующая multiprocessing
def coverage_percent(code_string, test_string):
    # Создание очереди для передачи результатов
    queue = multiprocessing.Queue()

    # Создание и запуск процесса
    process = multiprocessing.Process(target=run_coverage_process, args=(code_string, test_string, queue))
    process.start()
    process.join()

    # Проверка завершения процесса
    if process.exitcode != 0:
        raise RuntimeError(f"Процесс завершился с ошибкой. Код выхода: {process.exitcode}")

    try:
        result = queue.get_nowait()
    except:
        raise RuntimeError("Не удалось получить результат из процесса.")

    if isinstance(result, Exception):
        raise result

    return result  # (total_percentage, failed_tests, missing_lines)


# Функция для проверки синтаксиса Python кода
def is_valid_python_code(code):
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False


# Функция для вычисления покрытия и ошибок для каждой строки датафрейма
def calculate_coverage_for_df(df):
    # Создаем новый DataFrame с такими же колонками, как у исходного, и добавляем новые столбцы
    result_df = df.copy()

    # Список для хранения результатов
    coverage_percentages = []
    failed_tests_counts = []
    missing_lines_counts = []

    # Проходим по каждой строке в датафрейме
    for index, row in tqdm(df.iterrows(), total=df.shape[0]):
        code_string = row['Function']
        test_string = row['Test']

        # Проверка синтаксиса
        if not is_valid_python_code(code_string):
            print(f"Синтаксическая ошибка в Function {index}")
        if not is_valid_python_code(test_string):
            print(f"Синтаксическая ошибка в Test {index}")

        try:
            # Получаем данные покрытия и ошибок для каждого кода и теста
            total_percentage, failed_tests, missing_lines = coverage_percent(code_string, test_string)
        except Exception as e:
            # В случае ошибки при выполнении тестов записываем значения по умолчанию
            print(f"Ошибка при обработке строки {index}: {e}")
            total_percentage, failed_tests, missing_lines = 0.0, -1, []

        # Добавляем результат в соответствующие списки
        coverage_percentages.append(total_percentage)
        failed_tests_counts.append(failed_tests)
        missing_lines_counts.append(missing_lines)

    # Добавляем новые столбцы в DataFrame
    result_df['coverage_percent'] = coverage_percentages
    result_df['Errors'] = failed_tests_counts

    return result_df
