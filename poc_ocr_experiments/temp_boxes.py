import cv2
import pytesseract
from pytesseract import Output

# Path to your Tesseract OCR executable (Update this if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
lang = 'ori+eng'

def main(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Perform OCR using Tesseract and get the resulting data
    custom_config = r'--oem 3 --psm 3'  # Configuration for Tesseract OCR (Page Segmentation Mode)
    data = pytesseract.image_to_data(image, lang=lang, output_type=Output.DICT, config=custom_config)

    # Display the data returned by the image_to_data function
    print(data.keys())
    print(data)

if __name__ == "__main__":
    image_path = "page6_section_testing.png"  # Replace this with the path to your image
    main(image_path)