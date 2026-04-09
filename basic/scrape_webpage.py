from pathlib import Path
from pyexpat.errors import messages
import sys
from IPython.display import Markdown, display

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils import web_scraper
from llm import LLMClient, LLMType


def summarize_website(url: str):
    system_prompt = """
        You are a helpfulassistant that analyzes the contents of a website,
        and provides a short summary, ignoring text that might be navigation related.
        Respond in markdown.
    """

    user_prompt = """
    Here are the contents of a website.
    Provide a short summary of this website in markdown.
    It it includes news or announcements, then summarize these too.
    """

    contents = web_scraper.fetch_webpage_content(url)
    messages = [  # List of dictionaries with "role" and "content" keys
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt + "\n\n" + contents},
    ]
    summary = LLMClient.get_answers(LLMType.GEMINI, messages)
    return summary


def display_summary(url: str):
    summary = summarize_website(url)
    print(Markdown(summary))


if __name__ == "__main__":
    url = "https://www.nature.com/news"
    print(summarize_website(url))
