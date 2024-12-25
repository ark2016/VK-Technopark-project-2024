import json


def view_jsonl(file_path, num_lines=5):
    """
    Построчный просмотр JSONL файла.

    :param file_path: Путь к JSONL файлу.
    :param num_lines: Количество строк для отображения.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file):
                if i >= num_lines:
                    break
                data = json.loads(line.strip())
                print(f"### Строка {i + 1} ###")
                print(json.dumps(data, indent=4, ensure_ascii=False))
                print("\n")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")


# Путь к файлу
file_path = "tests_python.jsonl"

# Вызываем функцию просмотра
view_jsonl(file_path, num_lines=5)
