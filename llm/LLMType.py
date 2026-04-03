from enum import Enum


class LLMType(str, Enum):
    """Enumeration for the different supported Large Language Models."""

    ANTHROPIC = "ANTHROPIC"
    DEEPSEEK = "DEEPSEEK"
    GEMINI = "GEMINI"
    GROK = "GROK"
    GROQ = "GROQ"
    OPENROUTER = "OPENROUTER"
    LLAMA = "LLAMA"
    OPENAI = "OPENAI"
