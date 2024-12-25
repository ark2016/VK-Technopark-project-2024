from typing import Optional
from pydantic import BaseModel

# Модель запроса для get_chat_response
class GetChatResponseRequest(BaseModel):
    prompt: str
    context: Optional[str] = None
    model: Optional[str] = "open-mistral-7b"
