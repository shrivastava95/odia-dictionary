## Structure
**Folder**
- [testgpt_compare_pdfs](testgpt_compare_pdfs) - stores outputs for comparision.
- [testgpt_images](testgpt_images) - Stores the images which will be converted to PDF files using [pdfmaker.py](pdfmaker.py).
- [testgpt_pdfs](testgpt_pdfs) - Stores the pdfs which will be converted to PDF files using [pdfmaker.py](pdfmaker.py).

**Files**

- [pdfmaker.py](pdfmaker.py) -This code uses Tesseract OCR to convert images to PDF files. It iterates over the images in the [testgpt_images](testgpt_images) and performs OCR on each image. The resulting text is saved as a PDF file in the [testgpt_pdfs](testgpt_compare_pdfs). The OCR configuration varies based on the image filename, specifically the id1 and id2 values.
- [reader.py](reader.py) -This code converts PDF files in the [parsed_pdfs] folder to plain text and saves them in the [parsed_texts] folder. It uses the PyPDF2 library to read the PDF files and extract the text content from the first page of each PDF. The extracted text is then saved as plain text files with the same name as the original PDF files but with the ".txt" extension.
- [sender.py](sender.py) -The purpose of this code is to use the OpenAI GPT-3.5 language model to parse raw OCR (Optical Character Recognition) output into a neat table. The code takes two OCR outputs and merges them to reduce errors. The OCR outputs contain English words, their corresponding parts of speech, and their Odia translations.



