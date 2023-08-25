import openai
from dotenv import load_dotenv
import os
from math import ceil, floor
import time
import html
import pandas as pd
import numpy as np
from tqdm import tqdm

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY_GAUTAM")

openai.api_key = OPENAI_API_KEY

input_csv = 'mergegpt/parsed_dicts_merged/nouns_merged_unclean.csv'
output_dir = 'mergegpt/parsed_dicts_merged/GPT_outputs'
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

inputs_list = [[]]
for noun in pd.read_csv(input_csv).iloc[:, 0].tolist():
    if sum([len(noun) for noun in inputs_list[-1]]) > 1000:
        inputs_list.append([])
    inputs_list[-1].append(noun.strip())
outputs_list = []

for i, input_text in enumerate(tqdm(inputs_list)):
    messages = [
        {
            "role": "system", 
            "content": "You help me decide whether english definitions of words of my odia dictionary are agriculture related or not."
        },
        {
            "role": "user", 
            "content": """The table should have two columns:
    1. Word Meaning in English
    2. Agri Related

    I will give you a column of the word meaning in english. 
    Some entries hold erroneous values due to the fact that they were obtained using OCR. 
    Your job is to add the second column 'Agri Related' to determine whether each row is related to agriculture or not.
    Here is the column. Format it into the table. Additionally, ignore any rows that do not contain english words. 
    For example, here are the first two rows of an example output table:

    bathroom | 0
    toddy tree | 1
    """
        },
        {
            "role": "assistant",
            "content": "Sure! Please provide me with the column."
        },
        {
            "role": "user",
            "content": f"""{input_text}"""
        },
    ]
    # counts number of tokens in the message sequence. should be less than 4096
    num_tokens = sum([len(dictionary['content']) for dictionary in messages])
    # print(num_tokens)
    # sleep(2)
    # break
    # continue
    start = time.time()
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        temperature = 0.0,
        max_tokens = 2000,
        messages = messages
    )
    total = floor(time.time() - start)
    if total < 20:
        time.sleep(21 - total)

    gpt_text = html.unescape(completion.choices[0].message['content'])
    
    with open(os.path.join(output_dir, 'output' + str(i) + '.txt'), 'w+b') as f:
        f.write(gpt_text.encode())
