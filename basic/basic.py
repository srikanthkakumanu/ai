from openai import OpenAI
from ConfigReader import get_uri
from LLMSelector import LLMType, LLMModel


def get_answer(llm_type: LLMType, prompt: str):

    LLAMA_URI = get_uri(llm_type)
    MODEL = LLMModel.get_model(llm_type)

    openai = OpenAI(base_url=LLAMA_URI, api_key="ollama")

    response = openai.chat.completions.create(
        model=MODEL, messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print(get_answer(LLMType.LLAMA, "What is the capital of France?"))
