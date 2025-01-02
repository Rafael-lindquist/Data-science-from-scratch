from bs4 import BeautifulSoup
import requests
import re

url = "https://www.house.gov/representatives"
text = requests.get(url).text
soup = BeautifulSoup(text, "html5lib")

all_urls = [a["href"] for a in soup('a') if a.has_attr('href')]

print(len(all_urls))

# Deve começar com http:// ou https://
# Deve terminar com .house.gov ou .house.gov/
regex = r"^https?://.*\.house\.gov/?$"

# teste simples
assert re.match(regex, "http://joel.house.gov")

good_urls = [url for url in all_urls if re.match(regex, url)]

good_urls = list(set(good_urls))
print(len(good_urls))

html = requests.get("https://murphy.house.gov/").text
soup = BeautifulSoup(html, 'html5lib')

# Usando um conjunto porque os links podem surgir várias vezes
links = {a["href"] for a in soup('a') if 'press releases' in a.text.lower()}
print(links)

from typing import Dict, Set

press_releases: Dict[str, Set[str]] = {}

for house_url in good_urls:
    html = requests.get(house_url).text
    soup = BeautifulSoup(html, "html5lib")
    pr_links = {a['href'] for a in soup('a') if 'press_releases' in a.text.lower()}

    print(f"{house_url}: {pr_links}")
    press_releases[house_url] = pr_links

def paragraph_mentions(text: str, keyword: str) -> bool:
    """Retorna True se em <p> no texto mencionar {keyword}"""
    soup = BeautifulSoup(text, "html5lib")
    paragraphs = [p.get_text() for p in soup('p')]

    return any(keyword.lower() in paragraph.lower() for paragraph in paragraphs)

text = "<body><h1>Facebook</h1><p>Twitter</p>"
assert paragraph_mentions(text, "TwiTter")
assert paragraph_mentions(text, "facebook")

for house_url, pr_links, in press_releases.items():
    for pr_link in pr_links:
        url = f"{house_url}/{pr_link}"
        text = requests.get(url).text

        if paragraph_mentions(text, 'data'):
            print(f"{house_url}")
            break