# importing required modules
from PyPDF2 import PdfReader
import os
from tqdm import tqdm

  
# creating a pdf reader object

source_folder = f'new_dict/parsed_pdfs'
target_folder = f'new_dict/parsed_texts_ocr'

for pdf_path in tqdm(os.listdir(f'{source_folder}')):
    source_pdf_path = f'{source_folder}/{pdf_path}'
    target_text_path = f'{target_folder}/{pdf_path}.txt'

    reader = PdfReader(source_pdf_path)
    page = reader.pages[0]
    text = page.extract_text()
    
    with open(f'{target_text_path}', 'w+b') as f:
        f.write(bytes(text, encoding='utf-8'))