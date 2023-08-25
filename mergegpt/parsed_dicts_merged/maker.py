import pandas as pd
import numpy as np
import os
import enchant

spellcheck = enchant.Dict('en_US')

separator = '|'
input_dir = f'mergegpt/parsed_dicts_merged/GPT_outputs'
output_path = f'mergegpt/parsed_dicts_merged/agri_nouns_merged_unclean.json'

df = pd.read_csv('mergegpt/parsed_dicts_merged/nouns_merged_unclean.csv')
df.columns = [col.strip() for col in df.columns]
for col in df.columns:
    df[col] = df[col].str.strip()

rows = {}

for csv in os.listdir(input_dir):
    csv_path = os.path.join(input_dir, csv)
    csv = pd.read_csv(csv_path, sep=separator).iloc[1:, :]
    if csv.shape[1] == 4:
        csv = csv.iloc[:, 1:3]
    csv.columns = [col.strip() for col in csv.columns]
    csv['Word Meaning in English'] = csv['Word Meaning in English'].str.strip()
    csv['Agri Related']            = csv['Agri Related'].str.strip().str.strip('/').str.strip('\\')
    csv['Agri Related']            = [int(item) for item in csv['Agri Related']]

    for row in df.to_numpy():
        for noun, is_agri in csv.to_numpy():
            if noun == row[0] and is_agri:
                # print(noun, is_agri)
                rows[noun] = [item.split(',')[0] for item in row]
rows = [value for key, value in rows.items()]

import json
import html
dic = {}
for eng, pos, ori in rows:
    dic[ori] = eng


outstring = json.dumps(dic, indent=4, ensure_ascii=False)

with open(output_path, 'w+b') as f:
    f.write(outstring.encode())