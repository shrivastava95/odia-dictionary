#!/bin/bash

# python scripts/a-getting_page_images/pdf_to_imgs.py
python scripts/b-cropping_page_images/cropper.py
python scripts/c-images_to_pdfs_with_text/pdfmaker.py
python scripts/d-read_pdfs_with_text/reader.py
python scripts/e-gpt_api_sender/sender.py
python scripts/f-dataframe_maker/preprocess.py
python scripts/f-dataframe_maker/preprocess.py
python scripts/f-dataframe_maker/preprocess.py
rm GPT_outputs/page16_2.png.pdf.txt
python scripts/f-dataframe_maker/maker.py

python -c "print('we are done! check parsed_dicts for the unclean csv.')"