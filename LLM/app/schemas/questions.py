from typing import Optional
from pydantic import BaseModel


# Модель запроса для get_chat_response
class GetChatResponseRequest(BaseModel):
    prompt: str
    context: Optional[str] = None
    model: Optional[str] = "ft:codestral-latest:58fde890:20241217:9862a68b"


class GenerateTestsRequest(BaseModel):
    code: str = ("def equals_zero(a):\n"
                 "    if a == 0:\n"
                 "        return True\n"
                 "    return False")


class GenerateTestsResponse(BaseModel):
    generated_tests: str = ("def test_equals_zero():\n"
                            "    assert equals_zero(0) is True\n"
                            "    assert equals_zero(1) is False\n"
                            "    assert equals_zero(-1) is False\n"
                            "    assert equals_zero(0) is True")


# Schema for analyzing generated tests
class AnalyzeTestsRequest(BaseModel):
    code: str = ("def equals_zero(a):\n"
                 "    if a == 0:\n"
                 "        return True\n"
                 "    return False")
    tests: Optional[str] = None  # Optional, as tests might be generated internally


class AnalyzeTestsResponse(BaseModel):
    analysis: str


class MetricsRequest(BaseModel):
    csv_path: str


class MetricsResponse(BaseModel):
    metric_frame: list[dict]
    mean_failed: float
    mean_coverage_percent: float
    output_file: str
