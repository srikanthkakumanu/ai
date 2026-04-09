from bs4 import BeautifulSoup
import requests

# Standard headers to fetch a website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def fetch_webpage_content(url):
    """
    Return the title and contents of the website at the given url;
    truncate to 2,000 characters as a sensible limit
    """

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string if soup.title else "No Title Found"
    if soup.body:
        for irrelevent in soup.body(
            [
                "script",
                "style",
                "img",
                "input",
                "button",
                "nav",
                "footer",
                "header",
                "aside",
                "meta",
                "link",
            ]
        ):
            irrelevent.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""
    return (title + "\n\n" + text)[:2_000]


def fetch_webpage_links(url):
    """
    Return a list of all the links on the webpage at the given url
    """

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    links = [link.get("href") for link in soup.find_all("a", href=True)]
    return [link for link in links if link]
