# importing required modules
from PyPDF2 import PdfReader
import os
from tqdm import tqdm

  
# creating a pdf reader object

source_pdf_path = f'Hanuman_Chalisa_In_Odia.pdf'
target_folder = f'hanuman_chalisa/parsed_texts_copied'


reader = PdfReader(source_pdf_path)
for page_num, page in enumerate(reader.pages):
    text = page.extract_text()

    target_file_path = os.path.join(target_folder, f'page{page_num}.txt')
    with open(target_file_path, 'w+b') as f:
        f.write(bytes(text, encoding='utf-8'))
    # break