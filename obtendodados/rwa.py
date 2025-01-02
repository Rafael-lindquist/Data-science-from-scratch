import re

filename = "readingfile.txt"

starts_with_r = 0
with open(filename) as f:
    for line in f:              # analisa cada linha do arquivo
        if re.match("r", line): # use um regex para determinar se começa com R
            starts_with_r +=1

print(starts_with_r)

def get_domain(email_address: str) -> str:
    """Divida em @ e retorne o último trecho"""
    return email_address.lower().split('@')[-1]

assert get_domain("rafaelblemail@gmail.com") == "gmail.com" 

from collections import Counter

with open("readingfile.txt", 'r') as f:
    domain_counts = Counter(get_domain(l.strip()) for l in f if "@" in l )

print(domain_counts)

import csv

with open("stockprices.txt") as f:
    tab_reader = csv.reader(f, delimiter=";")
    for row in tab_reader:
        date = row[0]
        symbol = row[1]
        price = row[2]
        print(date, symbol, price)
