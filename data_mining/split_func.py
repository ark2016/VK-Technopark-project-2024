import re
import os


def extract_functions_to_files(file_path, output_dir, functions_per_file=10, include_comments=True):
    # Создаём директорию для вывода, если её нет
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    function_counter = 1  # Это счётчик всех функций
    function_code = []  # Здесь будем собирать код функции
    in_function = False  # Флаг, что мы находимся внутри функции
    stack = []  # Стек для отслеживания вложенности
    functions_in_file = 0  # Счётчик функций в текущем файле

    for line in lines:
        # Ищем строки с комментариями вида "# N."
        match = re.match(r'# \d+\.', line)
        if match:
            # Если уже накопилось нужное количество функций, записываем их в файл
            if functions_in_file == functions_per_file:
                # Убираем все пустые строки в конце перед записью
                while function_code and function_code[-1] == '\n':
                    function_code.pop()

                # Формируем имя файла по диапазону
                if functions_in_file == 1:
                    # Если только одна функция в файле, имя файла будет просто числом
                    file_range_start = function_counter - 1
                    function_filename = os.path.join(output_dir, f"file_{file_range_start}.py")
                else:
                    file_range_start = (function_counter - functions_in_file)
                    file_range_end = function_counter - 1
                    function_filename = os.path.join(output_dir, f"file_{file_range_start}_{file_range_end}.py")

                with open(function_filename, 'w', encoding='utf-8') as func_file:
                    func_file.writelines(function_code)

                # Сбросим для следующего файла
                function_code = []
                functions_in_file = 0  # Сбросить счётчик функций в файле

            # Начинаем новую функцию
            if include_comments:
                function_code.append(line)  # Добавляем комментарий перед функцией
            functions_in_file += 1
            function_counter += 1
            stack = [line]  # Сброс стека для новой функции
            in_function = True

        elif in_function:
            # Добавляем строки внутри функции
            function_code.append(line)

            # Учитываем скобки для определения начала и конца блока
            if '{' in line:
                stack.append('{')
            if '}' in line:
                stack.pop()

            # Когда стек пуст, это означает, что мы завершили функцию
            if not stack:
                in_function = False

        # Если комментарии не включаем, пропускаем их
        elif not include_comments and match:
            continue

    # Записываем оставшиеся функции в последний файл
    if function_code:
        # Убираем все пустые строки в конце перед записью
        while function_code and function_code[-1] == '\n':
            function_code.pop()

        # Формируем имя для последнего файла
        if functions_in_file == 1:
            # Если только одна функция в файле, имя файла будет просто числом
            file_range_start = function_counter - 1
            function_filename = os.path.join(output_dir, f"file_{file_range_start}.py")
        else:
            file_range_start = (function_counter - functions_in_file)
            file_range_end = function_counter - 1
            function_filename = os.path.join(output_dir, f"file_{file_range_start}_{file_range_end}.py")

        with open(function_filename, 'w', encoding='utf-8') as func_file:
            func_file.writelines(function_code)


# # Раскомментировать для функций
# file_path = 'functions.py'  # Укажи путь к исходному файлу
# output_dir = 'tests/functions'  # Укажи директорию для сохранения файлов
#
# functions_per_file = 20  # Укажи количество функций на файл
# include_comments = True  # Укажи, нужно ли включать комментарии перед функциями


# Раскомментировать для тестов
file_path = 'tests.py'  # Укажи путь к исходному файлу
output_dir = 'tests/tests'  # Укажи директорию для сохранения файлов

functions_per_file = 20  # Укажи количество функций на файл
include_comments = True  # Укажи, нужно ли включать комментарии перед функциями

extract_functions_to_files(file_path, output_dir, functions_per_file, include_comments)
