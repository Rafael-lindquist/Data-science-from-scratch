from bs4 import BeautifulSoup
import requests

url = ("https://raw.githubusercontent.com/joelgrus/data/master/getting-data.html")
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')
print(soup)

# Obter o conteúdo de texto de uma tag
first_paragraph = soup.find("p") # ou apenas soup.p
first_paragraph_text = soup.p.text
first_paragraph_words = soup.p.text.split()

# Extrair atributos de uma tag
first_paragraph_id = soup.p['id'] # Gera KeyError se não houver 'id'
first_paragraph_id2 = soup.p.get('id') # Retorna None se não houver 'id'

# Obter múltiplas tags ao mesmo tempo
all_paragraphs = soup.find_all('p') # Ou apenas soup('p')
paragraphs_with_ids = [p for p in soup('p') if p.get('id')]

# Tags com uma class específica
important_paragraphs = soup('p', {'class': 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p for p in soup('p') if 'important' in p.get('class', [])]

