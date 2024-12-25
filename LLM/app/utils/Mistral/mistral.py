from mistralai import Mistral
from transformers import pipeline
from ...utils.Mistral.config import api_key
from ...utils.Mistral.inference_gptbigcode import LargeCodeModelGPTBigCode
import re
import json

def initialize_client():
    """Инициализирует клиента Mistral с API-ключом."""
    if api_key:
        print("API key найден")
        return Mistral(api_key=api_key)
    else:
        print("API key не найден.")
        return None

def get_chat_response(prompt, context=None, model="open-mistral-7b"):
    """
    Получает ответ от LLM на основе предоставленного промпта и контекста.

    :param prompt: Строка с текстовым промптом от пользователя.
    :param context: Строка с дополнительным контекстом (опционально).
    :return: Ответ от LLM.
    """
    client = initialize_client()
    if not client:
        return "Ошибка: Клиент не инициализирован."

    messages = []
    if context:
        messages.append({"role": "system", "content": context})

    messages.append({"role": "user", "content": prompt})

    try:
        chat_response = client.chat.complete(
            model=model,
            messages=messages
        )
        return chat_response.choices[0].message.content
    except Exception as e:
        return f"Ошибка при получении ответа: {str(e)}"

def initialize_test_generator(model_name="4ervonec19/SimpleTestGenerator"):
    """
    Initializes a LargeCodeModelGPTBigCode instance for test generation.

    :param model_name: The model identifier on Hugging Face.
    :return: The initialized LargeCodeModelGPTBigCode instance.
    """
    return LargeCodeModelGPTBigCode(
        gpt2_name=model_name,
        flag_pretrained=True,
        flag_hugging_face=True
    )

def generate_tests(code_snippet: str, model_name="4ervonec19/SimpleTestGenerator"):
    """
    Generates tests for a given code snippet using a large code model.

    :param code_snippet: The Python function code.
    :param model_name: The model identifier on Hugging Face.
    :return: Generated tests as a string.
    """
    # Initialize the model
    generator = initialize_test_generator(model_name)
    try:
        # Perform inference
        result = generator.input_inference(code_text=code_snippet)
        # Return the generated tests
        return result['generated_output']
    except Exception as e:
        return f"Error generating tests: {str(e)}"


def extract_tests_from_message(message):
    """
    Извлекает код тестов из JSON-сообщения.

    :param message: строка с сообщением с тестами.
    :return: Строка с кодом тестов или None, если не найдено.
    """
    try:
        # Шаблон для поиска кода тестов внутри блока ```python ... ```
        test_code_pattern = r"```python\n(.*?)```"

        # Ищем все совпадения
        match = re.search(test_code_pattern, message, re.DOTALL)

        # Если совпадение найдено, возвращаем код тестов
        if match:
            return match.group(1).strip()
        return None
    except json.JSONDecodeError:
        print("Ошибка: Неверный формат JSON. Тесты не найдены.")
        return None

def analyze_generated_tests(code_snippet: str, model_name="4ervonec19/SimpleTestGenerator",
                            llm_model="ft:codestral-latest:58fde890:20241217:9862a68b"):
    """
    Generates unit tests for the given Python code snippet and analyzes them using LLM.

    :param code_snippet: The Python function code.
    :param model_name: The model identifier for test.py generation.
    :param llm_model: The LLM model identifier for analysis.
    :return: Analysis of generated tests as a string.
    """
    # Generate unit tests for the provided code snippet
    generated_tests = generate_tests(code_snippet, model_name)

    if "Error" in generated_tests:
        return f"Error during test.py generation: {generated_tests}"

    char = "{char}"
    prompt = (
        f"Analyze the given Python function and its associated unit tests:\n\n"
        f"Function:\n{code_snippet}\n\n"
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

    # Get LLM analysis
    analysis = get_chat_response(prompt, model=llm_model)

    print(analysis)
    res = extract_tests_from_message(analysis)
    if res is None:
        return analysis
    return res


