import requests
from bs4 import BeautifulSoup


def fetch_wikipedia_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all('p')
    text = ' '.join([para.text for para in paragraphs])
    return text
