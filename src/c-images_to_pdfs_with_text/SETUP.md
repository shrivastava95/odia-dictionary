# Setting up Tesseract OCR
## Linux
1. `sudo apt install tesseract-ocr`
2. `wget https://github.com/tesseract-ocr/tessdata/raw/3.04.00/ori.traineddata -O /usr/share/tesseract-ocr/4.00/tessdata/ori.traineddata`
3. verify if the output of `tesseract --list-langs` contains both "eng" and "ori"
4. `pip install pytesseract`
5. comment line 7 in `pdfmaker.py`

## Windows
1. Install the latest exe from https://github.com/UB-Mannheim/tesseract/wiki in `C:\Program Files (x86)\Tesseract-OCR`
2. `pip install pytesseract`
3. make sure line 7 is NOT commented in `pdfmaker.py`