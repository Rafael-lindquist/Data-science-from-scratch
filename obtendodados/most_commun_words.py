# most_commun_words.py
import sys
from collections import Counter

# passe o número de palavras como primeiro argumento
try:
    num_words = int(sys.argv[1])
except:
    print("usage: most_commun+words.py num_words")
    sys.exit(1) # código de saída diferente de zero indica erro 

counter = Counter(word.lower()                   
                for line in sys.stdin
                for word in line.strip().split()
                if word)

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write('\n')

# type the_bible.txt | python most_commun_words.py 10