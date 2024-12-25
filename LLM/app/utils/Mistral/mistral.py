from mistralai import Mistral
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
