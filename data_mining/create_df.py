import pandas as pd


def parse_functions(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    functions = []
    function_names = []

    n = len(lines)
    i = 0
    while i < n:
        line = lines[i]
        stripped_line = line.lstrip()
        if stripped_line.startswith('#'):
            # Пропускаем комментарии (перед функциями и между ними)
            i += 1
            continue
        elif stripped_line.startswith('def '):
            # Начало функции
            function_code = ''
            function_name = stripped_line.split('def ')[1].split('(')[0].strip()
            base_indentation = len(line) - len(stripped_line)
            function_code += line
            i += 1
            empty_line_count = 0
            while i < n:
                next_line = lines[i]
                next_line_stripped = next_line.lstrip()
                next_line_indentation = len(next_line) - len(next_line_stripped)
                if next_line.strip() == '':
                    # Пустая строка, включаем только одну подряд
                    if empty_line_count == 0:
                        function_code += next_line
                    empty_line_count += 1
                    i += 1
                    continue
                elif next_line_indentation > base_indentation:
                    # Строка внутри функции
                    function_code += next_line
                    empty_line_count = 0
                    i += 1
                else:
                    # Строка с отступом меньше или равным базовому
                    # Проверяем, не является ли это комментарием
                    if next_line_stripped.startswith('#'):
                        # Комментарий вне функции, пропускаем
                        i += 1
                        continue
                    else:
                        # Начало следующей функции или код вне функции
                        break
            # Удаляем лишние пустые строки в конце функции и добавляем одну
            function_code = function_code.rstrip('\n') + '\n\n'
            functions.append(function_code)
            function_names.append(function_name)
        else:
            i += 1
    return dict(zip(function_names, functions))


# Парсим functions.py
functions_dict = parse_functions('functions.py')

# Парсим tests.py
tests_dict = parse_functions('tests.py')

# Сопоставляем тесты с функциями
data = []

for test_name, test_code in tests_dict.items():
    if test_name.startswith('test_'):
        function_name = test_name[len('test_'):]
        if function_name in functions_dict:
            function_code = functions_dict[function_name]
            data.append({'Function': function_code.strip(), 'Test': test_code.strip()})

# Создаем DataFrame
df = pd.DataFrame(data)

# Выводим DataFrame
print(df)

# Сохраняем DataFrame в файл, если необходимо
df.to_csv('functions_tests.csv', index=False)

# Выводим DataFrame
print(df)
