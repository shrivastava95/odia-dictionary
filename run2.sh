#!/bin/bash

# python src/a-getting_page_images/pdf_to_imgs.py
python src/b-cropping_page_images/cropper.py
python src/c-images_to_pdfs_with_text/pdfmaker.py
python src/d-read_pdfs_with_text/reader.py
python src/e-gpt_api_sender/sender.py
python src/f-dataframe_maker/preprocess.py
python src/f-dataframe_maker/preprocess.py
python src/f-dataframe_maker/preprocess.py
rm GPT_outputs/page16_2.png.pdf.txt
python src/f-dataframe_maker/maker.py

python -c "print('we are done! check parsed_dicts for the unclean csv.')"