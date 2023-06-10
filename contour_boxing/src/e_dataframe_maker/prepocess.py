import os
import html

source_dir = f'contour_boxing/GPT_outputs'
separator = '|'

for filepath in os.listdir(source_dir):
    filepath = os.path.join(source_dir, filepath)

    # edit each GPT output text file to remove the unnecessary text before the table begins.
    with open(filepath, 'r+b') as f:
        first = separator
        file_string = f.read().decode('utf8')
        first_index = file_string.index(first)
        print(filepath)
        print(file_string[:])
        f.seek(0)
        f.write(file_string[first_index:].encode())
        f.truncate()
        # break