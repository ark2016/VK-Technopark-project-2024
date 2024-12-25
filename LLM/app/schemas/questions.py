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
    generated_tests: str = ("def equals_zero(a):\n"
                            "    if a == 0:\n"
                            "        return True\n"
                            "    return False\n"
                            "\n"
                            "def find_divisible_by_2_and_5_not_10(lst):\n"
                            "    result = []\n"
                            "    for num in lst:\n"
                            "        if (num % 2 == 0 or num % 5 == 0) and num % 10!= 0:\n"
                            "            result.append(num)\n"
                            "    if not result:\n"
                            "        return None\n"
                            "    return result\n"
                            "\n"
                            "def find_divisible_by_2_and_5_not_10(lst):\n"
                            "    result = []\n"
                            "    for num in lst:\n"
                            "        if (num % 2 == 0 or num % 5 == 0) and num % 10!= 0:\n"
                            "            result.append(num)\n"
                            "    if not result:\n"
                            "        return None\n"
                            "    return result\n"
                            "\n"
                            "def find_divisible_by_2_and_5_not_10")

# Schema for analyzing generated tests
class AnalyzeTestsRequest(BaseModel):
    code: str = ("def equals_zero(a):\n"
                 "    if a == 0:\n"
                 "        return True\n"
                 "    return False")
    tests: Optional[str] = None  # Optional, as tests might be generated internally

class AnalyzeTestsResponse(BaseModel):
    analysis: str