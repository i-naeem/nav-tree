from bs4 import PageElement
from bs4 import BeautifulSoup
import requests

# Constants

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"


# Utils
def get_nav(url: str) -> PageElement:
    """
    Send the request to given url and parse the navbar element of it.

    Args:
        url (str): Website URL

    Returns:
        PageElement: Navbar Element
    """

    response = requests.get(url, headers={"User-Agent": USER_AGENT})
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.find('nav')
