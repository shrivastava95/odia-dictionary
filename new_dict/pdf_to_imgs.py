from pdf2image import convert_from_path
from tqdm import tqdm
import os

# Note: refer to the accompanying SETUP.md file for poppler setup
output_folder = 'new_dict/pages'
pages = convert_from_path('en-or.pdf', 
                          300, 
                          poppler_path=r'C:\ai_sem_7\poppler-0.68.0_x86\poppler-0.68.0\bin') 
for i, page in enumerate(tqdm(pages)):
    if i in range(10, 364): # save only the pages that contain translations
        page.save(os.path.join(output_folder, f'page{i}.png'), 
                'PNG')