import cv2
import pytesseract
from pytesseract import Output
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('page6.png')

# Perform OCR using Tesseract
lang = 'ori+eng'
custom_config = r'--oem 3 --psm 3'  # Configuration for Tesseract OCR (Page Segmentation Mode)
boxes = pytesseract.image_to_boxes(img, 
                                 lang=lang, 
                                 config=custom_config,
                                 output_type=Output.DATAFRAME)
print(boxes)
print(type(boxes))