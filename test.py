import pandas as pd
from mistralai import Mistral

# Замените на ваш путь к файлу конфигурации
from LLM.app.utils.Mistral.config import api_key
from LLM.app.utils.Mistral.mistral import get_chat_response

def initialize_client():
    """Инициализирует клиента Mistral с API-ключом."""
    if api_key:
        print("API key найден")
        return Mistral(api_key=api_key)
    else:
        print("API key не найден.")
        return None

def analyze_tests_from_csv(csv_path, llm_model="ft:codestral-latest:58fde890:20241217:9862a68b"):
    """
    Читает сгенерированные тесты из CSV-файла и обрабатывает их с помощью Mistral.

    :param csv_path: Путь к CSV-файлу с тестами и кодом.
    :param llm_model: Модель LLM для анализа.
    :return: Результаты анализа.
    """
    # Загрузка данных из CSV
    try:
        data = pd.read_csv(csv_path)
    except FileNotFoundError:
        raise ValueError(f"Файл {csv_path} не найден.")

    if 'Function' not in data.columns or 'GeneratedTests' not in data.columns:
        raise ValueError("CSV файл должен содержать колонки 'Function' и 'GeneratedTests'.")

    # Инициализация клиента
    client = initialize_client()
    if not client:
        raise RuntimeError("Mistral клиент не инициализирован.")

    results = []

    for index, row in data.iterrows():
        function_code = row['Function']
        generated_tests = row['GeneratedTests']

        char = "{char}"
        prompt = (
            f"Analyze the given Python function and its associated unit tests:\n\n"
            f"Function:\n{function_code}\n\n"
            f"Provided Unit Tests:\n{generated_tests}\n\n"
            f"Based on these tests, generate a comprehensive suite of additional unit tests to achieve 100% code coverage. "
            f"Ensure the newly generated tests adhere to the format and structure of the provided tests. "
            f"Highlight missing edge cases and suggest improvements to the existing tests. "
            f"Return only the complete Python code for the generated unit tests in a well-formatted and executable manner, "
            f"without any additional explanations or commentary.\n\n"
            f"Examples:\n"
            f"Input Function:\n"
            f"def are_anagrams(s1, s2):\n"
            f"    if len(s1) != len(s2):\n"
            f"        print(\"Strings are not of equal length.\")\n"
            f"        return False\n"
            f"    char_count = {{}}\n"
            f"    for char in s1:\n"
            f"        char_count[char] = char_count.get(char, 0) + 1\n"
            f"    for char in s2:\n"
            f"        if char not in char_count or char_count[char] == 0:\n"
            f"            print(f\"' {char}' is not in the first string or appears too many times.\")\n"
            f"            return False\n"
            f"        char_count[char] -= 1\n"
            f"    return True\n\n"
            f"Output Tests:\n"
            f"def test_are_anagrams():\n"
            f"    assert are_anagrams(\"listen\", \"silent\") == True\n"
            f"    assert are_anagrams(\"hello\", \"world\") == False\n"
            f"    assert are_anagrams(\"evil\", \"vile\") == True\n"
            f"    assert are_anagrams(\"fluster\", \"restful\") == True\n"
            f"    assert are_anagrams(\"test.py\", \"TEST\") == False  # Case-sensitive check\n"
            f"    assert are_anagrams(\"a\", \"a\") == True\n"
            f"    assert are_anagrams(\"abc\", \"abcd\") == False\n"
            f"    assert are_anagrams(\"\", \"\") == True\n"
            f"    assert are_anagrams(\"aabb\", \"abab\") == True\n"
            f"    assert are_anagrams(\"aabb\", \"abac\") == False\n"
        )

        try:
            analysis = get_chat_response(prompt, model=llm_model)
            results.append({
                'Function': function_code,
                'GeneratedTests': generated_tests,
                'Analysis': analysis
            })
        except Exception as e:
            print(f"Ошибка при анализе строки {index}: {e}")
            results.append({
                'Function': function_code,
                'GeneratedTests': generated_tests,
                'Analysis': f"Ошибка: {e}"
            })

    # Преобразование результатов в DataFrame
    results_df = pd.DataFrame(results)
    results_csv_path = "analyzed_tests.csv"

    # Сохранение результатов в CSV
    results_df.to_csv(results_csv_path, index=False)
    print(f"Результаты анализа сохранены в {results_csv_path}")

    return results_csv_path

# Пример вызова
if __name__ == "__main__":
    csv_file_path = "generated_tests.csv"  # Укажите путь к вашему CSV файлу
    analyze_tests_from_csv(csv_file_path)
