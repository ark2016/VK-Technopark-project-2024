from mistralai import Mistral
from transformers import pipeline
from ...utils.Mistral.config import api_key

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
    Initializes a text-generation pipeline for test generation.

    :param model_name: The model identifier on Hugging Face.
    :return: The initialized pipeline.
    """
    return pipeline("text-generation", model=model_name)

def generate_tests(code_snippet: str, model_name="4ervonec19/SimpleTestGenerator"):
    """
    Generates tests for a given code snippet.

    :param code_snippet: The Python function code.
    :param model_name: The model identifier on Hugging Face.
    :return: Generated tests as a string.
    """
    generator = initialize_test_generator(model_name)
    try:
        generated = generator(code_snippet, max_length=200, num_return_sequences=1)
        return generated[0]["generated_text"]
    except Exception as e:
        return f"Error generating tests: {str(e)}"

def analyze_generated_tests(code_snippet: str, model_name="4ervonec19/SimpleTestGenerator",
                            llm_model="ft:codestral-latest:58fde890:20241217:9862a68b"):
    """
    Generates unit tests for the given Python code snippet and analyzes them using LLM.

    :param code_snippet: The Python function code.
    :param model_name: The model identifier for test generation.
    :param llm_model: The LLM model identifier for analysis.
    :return: Analysis of generated tests as a string.
    """
    # Generate unit tests for the provided code snippet
    generated_tests = generate_tests(code_snippet, model_name)

    if "Error" in generated_tests:
        return f"Error during test generation: {generated_tests}"

    prompt = (
        f"Analyze the given Python function and the associated unit tests:\n\n"
        f"Function:\n{code_snippet}\n\n"
        f"Provided Unit Tests:\n{generated_tests}\n\n"
        f"Based on these tests, generate a comprehensive suite of additional unit tests to achieve 100% code coverage. "
        f"Ensure the newly generated tests adhere to the format and structure of the provided tests, "
        f"highlight any missing edge cases, and suggest improvements for the existing tests where necessary. "
        f"Your output should be well-organized, formatted, and executable."
    )

    # Get LLM analysis
    analysis = get_chat_response(prompt, model=llm_model)

    if "Ошибка" in analysis:
        return f"Error during LLM analysis: {analysis}"

    return analysis


