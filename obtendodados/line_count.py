# Este script conta as linhas recebidas e grava a contagem 

import sys

count = 0
for line in sys.stdin:
    count += 1

# a impressão para sys.stdout
print(count)

# type SomeFile.txt | python egrep.py "[0-9]" | python line_count.py 
# isso conta quantas linhas possuem determinado termo no arquivo