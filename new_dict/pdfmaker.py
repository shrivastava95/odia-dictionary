import pytesseract
from tqdm import tqdm
import os


# remove this line on linux.
pytesseract.pytesseract.tesseract_cmd = f"C:/Program Files/Tesseract-OCR/tesseract.exe"

# different psm mode can change the behaviour of parsing.
# refer to documentation for further details.
psm_mode = 3
config = f'--psm {psm_mode}'
source_pdf_folder = 'new_dict/pages_processed'
target_folder = 'new_dict/parsed_pdfs'
lang='ori+eng'

for i, image_path in enumerate(tqdm(os.listdir(source_pdf_folder))):
    if int(image_path.split('.')[0].split('_')[0][4:]) in range(10, 364):      # only parsing pages 6 - 87, inclusive
        source_image_path = os.path.join(source_pdf_folder, image_path)       # for example: source_pdf_folder/page6_0.png
        target_image_path = os.path.join(target_folder, f'{image_path}.pdf')  # for example: target_folder/page6_0.png.pdf

        with open(target_image_path, 'w+b') as f:
            f.write(pytesseract.image_to_pdf_or_hocr(source_image_path, 
                                                    lang=lang, 
                                                    extension='pdf', 
                                                    config=config))