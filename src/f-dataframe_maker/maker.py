import pandas as pd
import numpy as np
import os

dataframes = []
source_dir = f'GPT_outputs'

for df_link in os.listdir(source_dir):
    df_full_source = f'{source_dir}/{df_link}'
    print(df_link)
    df = pd.read_csv(f'{df_full_source}', sep='|', on_bad_lines='skip')
    if df.shape[1] != 3:
        continue
    df = df.iloc[:, 1:-1]
    df.columns = ['English Word', 'Part of Speech', 'Odia Translation']

    dataframes.append(df)
    print(df.shape)
    

data = pd.concat(dataframes, axis=0).reset_index(drop=True)
print(data.shape)
print(data.head())
rows_to_remove = data[(data[data.columns[0]].str.contains('-')) & (data[data.columns[1]].str.contains('-')) & (data[data.columns[2]].str.contains('-'))].index
data = data.drop(rows_to_remove)

data.to_csv('parsed_dicts/parsed_dict_very_unclean.csv', index=None)