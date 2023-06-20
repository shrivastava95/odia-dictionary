import os
import numpy as np
import pandas as pd
import json
from tqdm import tqdm
import html

source_folder = f'new_dict/parsed_texts_copied'
target_path = f'new_dict/uniques.json'
uniques = []

for source_file in tqdm(os.listdir(source_folder)):
    source_file_path = os.path.join(source_folder, source_file)

    with open(source_file_path, 'r+b') as f:
        text = html.unescape(f.read().decode('utf-8'))
        text = list(text)
        uniques = np.unique(
            np.append(
                uniques, 
                np.unique(text)
            )
        )

uniques = list(uniques)
print(uniques)
with open(target_path, 'w') as f:
    json.dump(uniques, f, indent=4)
