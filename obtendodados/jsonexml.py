import json

livro = {
    "title": "Data Science Book",
    "author": "Joel Grus",
    "publicationyear": 2019,
    "topics": ["data", 'science', 'data science']
}


# with open('livro.json', 'w') as file:
#     json.dump(livro, file, indent=4)

with open('livro.json', "r") as file:
    dados = json.load(file)

print(dados)