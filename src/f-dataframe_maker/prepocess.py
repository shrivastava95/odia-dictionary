import os
import html

for filepath in os.listdir('GPT_outputs'):
    filepath = 'GPT_outputs/' + filepath
    with open(filepath, 'r+b') as f:
        first = '|'
        file_string = f.read().decode('utf8')
        first_index = file_string.index(first)
        print(filepath)
        print(file_string[:])
        f.seek(0)
        f.write(file_string[first_index:].encode())
        f.truncate()
        # break

        