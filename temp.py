import os
counter = {}

for filepath in os.listdir('GPT_outputs'):
    filepath = filepath.split('.')[0]
    
    triple = int(filepath.split('_')[1])
    base = int(filepath[4:].split('_')[0])
    if base not in counter:
        counter[base] = 0
    counter[base] += 1

for base in counter.keys():
    print(base, counter[base])
