import sys
import os
import coverage
import pytest
import re
import threading
import io
from pathlib import Path

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

def exec_tests(code_string, test_string, code_filename, test_filename):
    code_path = Path(code_filename).resolve()
    test_path = Path(test_filename).resolve()

    # Сохраняем строки кода в файлы
    with open(code_path, 'w', encoding='utf-8') as f:
        f.write(code_string)
    with open(test_path, 'w', encoding='utf-8') as f:
        f.write(test_string)

    # Проверяем наличие файлов
    if not code_path.is_file():
        print(f"Файл с кодом '{code_filename}' не найден.")
        sys.exit(1)
    if not test_path.is_file():
        print(f"Файл с тестами '{test_filename}' не найден.")
        sys.exit(1)

    # Запускаем измерение покрытия
    cov = coverage.Coverage()
    cov.start()

    # Инициализируем плагин для сбора результатов тестов
    collector = TestResultCollector()

    # Выполняем тесты с помощью pytest, передавая плагин
    pytest_result = pytest.main([str(test_path)], plugins=[collector])

    # Останавливаем измерение покрытия
    cov.stop()
    cov.save()

    # Генерируем отчет по покрытию для файла с кодом
    total_percentage = cov.report(include=[str(code_path)], show_missing=True)

    # Получаем данные покрытия
    data = cov.get_data()
    analysis = cov.analysis(str(code_path))
    # analysis содержит: (filename, executed_lines, missing_lines, excluded_lines)
    _, executed_lines, missing_lines, _ = analysis

    os.remove(code_path)
    os.remove(test_path)
    os.remove('.coverage')

    # Возвращаем процент покрытия, количество неудачных тестов и пропущенные строки
    return total_percentage, collector.failed_tests, missing_lines


def coverage_percent(code_string, test_string, code_filename='code.py', test_filename='test_code.py'):
    test_string = split_test_function(test_string)
    test_string = add_import_to_code(test_string, os.path.splitext(code_filename)[0])

    # Список для хранения результата из потока
    result = []

    def run_tests_in_thread():
        # Перенаправление вывода в StringIO для подавления
        original_stdout = sys.stdout
        original_stderr = sys.stderr
        sys.stdout = io.StringIO()
        sys.stderr = io.StringIO()

        try:
            total_percentage, failed_tests, missing_lines = exec_tests(
                code_string, test_string, code_filename, test_filename
            )
            result.append((total_percentage, failed_tests, missing_lines))
        finally:
            # Восстанавливаем стандартные выводы
            sys.stdout = original_stdout
            sys.stderr = original_stderr

    # Создание и запуск потока
    test_thread = threading.Thread(target=run_tests_in_thread)
    test_thread.start()
    test_thread.join()

    if result:
        total_percentage, failed_tests, missing_lines = result[0]
        return total_percentage, failed_tests, missing_lines
    else:
        raise RuntimeError("Не удалось получить результат покрытия.")

# Пример использования
# if __name__ == "__main__":
#     # Пример кода и тестов
#     code_string = """
# def add(a, b):
#     return a + b
# """
#
#     test_string = """
# def test_add():
#     assert add(1, 2) == 3
#     assert add(-1, 1) == 0
#     assert add(0, 0) == 0
# """
#
#     coverage_result = coverage_percent(code_string, test_string)
#     print(f"Процент покрытия: {coverage_result}%")
