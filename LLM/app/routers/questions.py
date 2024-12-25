from fastapi import APIRouter, HTTPException
from ..utils.Mistral.mistral import get_chat_response
from ..schemas.questions import GetChatResponseRequest

router = APIRouter(
    tags=["Questions"]
)

# Маршрут для healthcheck
@router.get("/ping")
def api_ping():
    return {"status": "OK"}

# Маршрут для get_chat_response
@router.post("/get_chat_response")
def api_get_chat_response(request: GetChatResponseRequest):
    response = get_chat_response(
        prompt=request.prompt,
        context=request.context,
        model=request.model
    )
    if "Ошибка" in response:
        raise HTTPException(status_code=500, detail=response)
    return {"response": response}
