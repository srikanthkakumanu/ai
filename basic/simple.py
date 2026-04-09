from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from llm import LLMClient, LLMType


def main():
    # Simple test to check if the LLM client is working
    message = "Hello, Gemini!, How are you today?"
    answer = LLMClient.get_answer(LLMType.GEMINI, message)
    print(answer)

    # Types of prompts: Using system and user prompts
    system_prompt = "You are a world famous mathematician from 17th century."
    user_prompt = "Why is 2 + 2 = 4?"
    messages = [  # List of dictionaries with "role" and "content" keys
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    answer = LLMClient.get_answers(LLMType.GEMINI, messages)
    print(answer)


if __name__ == "__main__":
    main()
