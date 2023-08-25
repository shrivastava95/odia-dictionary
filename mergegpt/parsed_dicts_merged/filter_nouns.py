import numpy as np
import pandas as pd

df_path = 'mergegpt/parsed_dicts_merged/parsed_dict_merged_unclean.csv'
output_path = 'mergegpt/parsed_dicts_merged/nouns_merged_unclean.csv'
df = pd.read_csv(df_path).fillna('')
# print(df['Part of Speech'].str.lower().str.contains('noun'))
filtered_df = df[df['Part of Speech'].str.lower().str.contains('noun') & ~df['Odia Translation'].str.contains(r'[A-Za-z]')]
print(filtered_df.head(), filtered_df.shape)

rows = []

for row in filtered_df.to_numpy():
    eng = row[0] + row[1]
    print(eng)
    print([ord(ci) for ci in eng])
    if sum([ord(ci) in range(1816, 1943+1) for ci in eng]) == 0:
        rows.append(row)


filtered_df = pd.DataFrame(rows, columns=filtered_df.columns)
print(filtered_df.head(), filtered_df.shape)
filtered_df.to_csv(output_path, index=None)