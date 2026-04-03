from __future__ import annotations

from dataclasses import dataclass

from basic.ConfigReader import ConfigReader
from llm.EnvLoader import EnvLoader
from llm.LLMType import LLMType


@dataclass
class LLMModel:
    llm_type: LLMType
    model: str
    uri_key: str
    env_key: str
    uri: str | None = None
    api_key: str | None = None

    @staticmethod
    def get_model(llm_type: LLMType) -> LLMModel:
        """Returns the LLM model for a given LLM type."""

        EnvLoader.load_env()
        ConfigReader.load_configs()

        match llm_type:
            case LLMType.LLAMA:
                llm = LLMModel(
                    llm_type=llm_type,
                    model="llama3.2",
                    uri_key="OLLAMA_BASE_URL",
                    env_key="LLAMA_API_KEY",
                )
            case LLMType.ANTHROPIC:
                llm = LLMModel(
                    llm_type=llm_type,
                    model="claude-2",
                    uri_key="ANTHROPIC_BASE_URL",
                    env_key="ANTHROPIC_API_KEY",
                )
            case LLMType.DEEPSEEK:
                llm = LLMModel(
                    llm_type=llm_type,
                    model="deepseek-1",
                    uri_key="DEEPSEEK_BASE_URL",
                    env_key="DEEPSEEK_API_KEY",
                )
            case LLMType.GEMINI:
                llm = LLMModel(
                    llm_type=llm_type,
                    model="gemini-3-flash-preview",
                    uri_key="GEMINI_BASE_URL",
                    env_key="GOOGLE_API_KEY",
                )
            case LLMType.GROK:
                llm = LLMModel(
                    llm_type=llm_type,
                    model="grok-1",
                    uri_key="GROK_BASE_URL",
                    env_key="GROK_API_KEY",
                )
            case LLMType.GROQ:
                llm = LLMModel(
                    llm_type=llm_type,
                    model="groq-1",
                    uri_key="GROQ_BASE_URL",
                    env_key="GROQ_API_KEY",
                )
            case LLMType.OPENROUTER:
                llm = LLMModel(
                    llm_type=llm_type,
                    model="openai/gpt-4.1-nano",
                    uri_key="OPENROUTER_BASE_URL",
                    env_key="OPENROUTER_API_KEY",
                )
            case LLMType.OPENAI:
                llm = LLMModel(
                    llm_type=llm_type,
                    model="gpt-4.1-nano",
                    uri_key="OPENAI_BASE_URL",
                    env_key="OPENAI_API_KEY",
                )
            case _:
                raise ValueError(f"Unsupported LLM type: {llm_type}")

        llm.uri = ConfigReader.get_uri(llm.uri_key)
        llm.api_key = EnvLoader.get_value(llm.env_key)
        return llm

    @classmethod
    def get_llm_models(cls) -> list[LLMModel]:
        """Return all LLM models with uri and api_key loaded."""
        EnvLoader.load_env()
        ConfigReader.load_configs()
        return [cls.get_model(llm_type) for llm_type in LLMType]
