from openai import OpenAI

from .LLMModel import LLMModel
from .LLMType import LLMType


def get_answer(llm_type: LLMType, prompt: str):

    llm_model = LLMModel.get_model(llm_type)

    openai = OpenAI(base_url=llm_model.uri, api_key=llm_model.api_key)

    response = openai.chat.completions.create(
        model=llm_model.model, messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def get_answers(llm_type: LLMType, prompts: list[str]):

    llm_model = LLMModel.get_model(llm_type)

    openai = OpenAI(base_url=llm_model.uri, api_key=llm_model.api_key)

    response = openai.chat.completions.create(model=llm_model.model, messages=prompts)

    return response.choices[0].message.content
