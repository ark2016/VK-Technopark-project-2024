import re

def fix_function_numbers(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    function_counter = 1
    prev_function_added = False  # Флаг, чтобы отслеживать, была ли добавлена пустая строка после предыдущей функции

    for line in lines:
        # Ищем строки с комментариями вида "# N. Функция..."
        match = re.match(r'# (\d+)\.', line)
        if match:
            # Заменяем старый номер на новый
            new_line = re.sub(r'# \d+\.', f'# {function_counter}.', line)
            function_counter += 1
            # Если это не первая функция, добавляем две пустые строки перед новой
            # if new_lines and not prev_function_added:
            #     new_lines.append('\n')  # Первая пустая строка
            new_lines.append(new_line)
            prev_function_added = True
        else:
            # Если строка не содержит номер функции, просто добавляем её как есть
            new_lines.append(line)
            # Если строка с функцией добавлена, сбрасываем флаг, т.к. последующие строки не должны иметь промежутки
            if prev_function_added:
                prev_function_added = False

    # Записываем изменённый текст обратно в файл
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Пример использования
file_path = 'functions.py'  # Укажи путь к твоему файлу
fix_function_numbers(file_path)
