from pathlib import Path
import sys

from openai import OpenAI

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from llm.LLMModel import LLMModel
from llm.LLMType import LLMType


def get_answer(llm_type: LLMType, prompt: str):

    llm_model = LLMModel.get_model(llm_type)

    openai = OpenAI(base_url=llm_model.uri, api_key=llm_model.api_key)

    response = openai.chat.completions.create(
        model=llm_model.model, messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print(get_answer(LLMType.GEMINI, "What is the capital of France?"))
