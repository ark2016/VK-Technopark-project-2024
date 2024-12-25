from fastapi import APIRouter, HTTPException
from ..utils.Mistral.mistral import get_chat_response, generate_tests,analyze_generated_tests
from ..schemas.questions import GetChatResponseRequest
from ..schemas.questions import GenerateTestsRequest, GenerateTestsResponse, AnalyzeTestsRequest, AnalyzeTestsResponse

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

@router.post("/generate_tests", response_model=GenerateTestsResponse)
def api_generate_tests(request: GenerateTestsRequest):
    """
    Generates unit tests for the given Python code.

    :param request: The request containing the Python function code.
    :return: Generated unit tests.
    """
    generated_tests = generate_tests(request.code)
    if "Error" in generated_tests:
        raise HTTPException(status_code=500, detail=generated_tests)
    return GenerateTestsResponse(generated_tests=generated_tests)

@router.post("/analyze_tests", response_model=AnalyzeTestsResponse)
def api_analyze_tests(request: AnalyzeTestsRequest):
    """
    Analyzes the quality of generated tests for the given Python code.

    :param request: The request containing the Python function code and optionally the tests.
    :return: Analysis of the tests.
    """
    analysis = analyze_generated_tests(
        code_snippet=request.code,
        model_name="4ervonec19/SimpleTestGenerator"
    )
    if "Error" in analysis:
        raise HTTPException(status_code=500, detail=analysis)
    return AnalyzeTestsResponse(analysis=analysis)
