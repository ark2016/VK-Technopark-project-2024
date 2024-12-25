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



