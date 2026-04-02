from enum import Enum
from dataclasses import dataclass


class LLMType(str, Enum):
    """Enumeration for the different supported Large Language Models."""

    ANTHROPIC = "ANTHROPIC"
    DEEPSEEK = "DEEPSEEK"
    GEMINI = "GEMINI"
    GROK = "GROK"
    GROQ = "GROQ"
    OPENROUTER = "OPENROUTER"
    LLAMA = "LLAMA"


@dataclass(frozen=True)
class LLMConfig:
    """Represents the configuration for a large language model."""

    model: str
    uri_key: str


def get_llm_config(llm_type: LLMType) -> LLMConfig:
    """Returns the configuration for a given LLM type."""
    match llm_type:
        case LLMType.LLAMA:
            return LLMConfig(model="llama3.2", uri_key="OLLAMA_BASE_URL")
        case LLMType.ANTHROPIC:
            return LLMConfig(model="claude-2", uri_key="ANTHROPIC_BASE_URL")
        case LLMType.DEEPSEEK:
            return LLMConfig(model="deepseek-1", uri_key="DEEPSEEK_BASE_URL")
        case LLMType.GEMINI:
            return LLMConfig(model="gemini-1.5-pro", uri_key="GEMINI_BASE_URL")
        case LLMType.GROK:
            return LLMConfig(model="grok-1", uri_key="GROK_BASE_URL")
        case LLMType.GROQ:
            return LLMConfig(model="groq-1", uri_key="GROQ_BASE_URL")
        case LLMType.OPENROUTER:
            return LLMConfig(model="openai/gpt-4.1-nano", uri_key="OPENROUTER_BASE_URL")
        case _:
            raise ValueError(f"Unsupported LLM type: {llm_type}")


class LLMModel:
    @staticmethod
    def get_model(llm_type: LLMType) -> str:
        """Gets the model name for the given LLM type."""
        return get_llm_config(llm_type).model
