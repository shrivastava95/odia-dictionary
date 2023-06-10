# Pipeline
1. Run `python new_dict/reader_copied.py`: copies the text from the original pdf itself
2. Run `python new_dict/pdf_to_imgs.py`: converts original pdf pages to .png images
3. Run `python new_dict/cropper.py`: (NEEDS EDITING) crops relevant regions from .png images
2. Run `python new_dict/pdfmaker.py`: Tesseract OCR converts preprocessed page images to PDFs with copyable text
4. Run `python new_dict/reader_ocr.py`: copies text from the PDFs, dumps to .txt files
5. Run `python new_dict/sender_merger.py`: merges raw text copied from PDF files
6. Run `python new_dict/`:

# Other files
1. `uniques.json`
2. `uniques.py`
3. `test_prompt.py`

# Files not yet added
1. `new_dict/sender_merger.py`: Sends the GPT queries to merge `new_dict/parsed_texts/ocr` and `new_dict/parsed_texts/copied` into clean tables in `new_dict/GPT_outputs_merged.py`.
