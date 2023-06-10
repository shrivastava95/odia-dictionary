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

# Setting up pyenchant
## Windows
According to the documentation [here](https://pyenchant.github.io/pyenchant/install.html), Windows installation must be done from the wheel file.
1. `wget https://files.pythonhosted.org/packages/49/96/2087455de16b08e86fa7ce70b53ddac5fcc040c899d9ebad507a0efec52d/pyenchant-3.2.2-py3-none-win_amd64.whl`
2. `pip install pyenchant-3.2.2-py3-none-win_amd64.whl`
3. You can remove the wheel file after installing - `rm pyenchant-3.2.2-py3-none-win_amd64.whl`
4. In case this doesnt work, refer to [Enchant Documenation](https://pyenchant.github.io/pyenchant/install.html)

## Linux
Refer to [Enchant Documentation](https://pyenchant.github.io/pyenchant/install.html)