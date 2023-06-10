import pandas as pd
import numpy as np
import os

dataframes = []
source_dir = f'GPT_outputs'
output_dir = f'parsed_dicts'
output_name = f'parsed_dict_very_unclean.csv'
separator = '|'

for df_link in os.listdir(source_dir):
    try:
            
        df_full_source = os.path.join(source_dir, df_link)
        print(df_link)
        df = pd.read_csv(df_full_source, 
                        sep=separator, 
                        on_bad_lines='skip') 
        if df.shape[1] != 5:   # Enforce every row has three columns
            continue
        df = df.iloc[:, 1:-1]  # remove blank unused columns
        df.columns = ['English Word', 'Part of Speech', 'Odia Translation']
        dataframes.append(df)
        print(df.shape)
    except Exception as e:
        print(e)


data = pd.concat(dataframes, axis=0).reset_index(drop=True)
print(data.shape)
print(data.head())

# Remove the | --- | --- | --- |  garbage rows   
rows_to_remove = data[(data[data.columns[0]].str.contains('-')) & (data[data.columns[1]].str.contains('-')) & (data[data.columns[2]].str.contains('-'))].index
data = data.drop(rows_to_remove)

# save the dataframe
full_output_location = os.path.join(output_dir, output_name)
data.to_csv(full_output_location, index=None)