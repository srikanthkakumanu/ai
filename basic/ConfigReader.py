from jproperties import Properties
from typing import Optional

from LLMSelector import LLMType, get_llm_config

configs = Properties()

try:
    with open("../configs/URI.properties", "rb") as uri_prop:
        configs.load(uri_prop)

except FileNotFoundError:
    print("URI.properties file not found.")
except Exception as e:
    print(f"An error occurred while reading the properties file: {e}")


def get_uri(llm: LLMType) -> Optional[str]:
    """Gets the base URI for a given LLM type from the properties file."""
    try:
        key = get_llm_config(llm).uri_key
    except ValueError:
        return None

    if key in configs:
        value, _ = configs[key]
        return value

    return None
