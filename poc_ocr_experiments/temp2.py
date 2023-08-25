import cv2
import pytesseract
from pytesseract import Output
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('page6_section_testing_long.png')

# Perform OCR using Tesseract
lang = 'ori+eng'
custom_config = r'--oem 3 --psm 6'  # Configuration for Tesseract OCR (Page Segmentation Mode)
data = pytesseract.image_to_data(img, 
                                 lang=lang, 
                                 output_type=Output.DICT, 
                                 config=custom_config)
print(data['text'])
print(data['level'])
for level_num, text_item in zip(data['text'], data['level']):
    print(level_num, text_item)

# Function to draw bounding boxes
def draw_boxes(image, data, color, level):
    for i in range(len(data['level'])):
        if data['level'][i] == level:
            (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

# Draw bounding boxes of different levels
draw_boxes(img, data, (255, 0, 0), 1)
draw_boxes(img, data, (0, 255, 0), 2)
draw_boxes(img, data, (0, 0, 255), 3)
draw_boxes(img, data, (255, 255, 0), 4)
draw_boxes(img, data, (0, 255, 255), 5)

# Show the image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()