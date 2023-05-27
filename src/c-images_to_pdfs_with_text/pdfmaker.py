from PIL import Image
import pytesseract
from tqdm import tqdm
from PyPDF2 import PdfReader
import os


pytesseract.pytesseract.tesseract_cmd = f"C:/Program Files/Tesseract-OCR/tesseract.exe"

psm_mode = 6
config = f'--psm {psm_mode}'
source_pdf_folder = 'pages_processed'
target_folder = 'parsed_pdfs'
lang='ori+eng'

for i, image_path in enumerate(tqdm(os.listdir(source_pdf_folder))):
    if int(image_path.split('.')[0].split('_')[0][4:]) in range(6, 88):
        source_image_path =f'{source_pdf_folder}/{image_path}' # source_pdf_folder/page6_0.png
        target_image_path =f'{target_folder}/{image_path}.pdf'

        with open(target_image_path, 'w+b') as f:
            f.write(pytesseract.image_to_pdf_or_hocr(source_image_path, 
                                                    lang=lang, 
                                                    extension='pdf', 
                                                    config=config))