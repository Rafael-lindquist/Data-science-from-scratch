import usacongresso
import requests

for house_url, pr_links in usacongresso.press_releases.items():
    for pr_link in pr_links:
        url = f"{house_url}/{pr_links}"
        text = requests.get(url).text

        if usacongresso.paragraph_mentions(text, 'data'):
            print(f"{house_url}")
            break # fim da atividade em house_url

        
