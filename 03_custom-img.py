import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

imgName = "xxx.jpg"

if os.path.exists(imgName) and os.path.isfile(imgName):
    try:
        img = cv2.imread(imgName)   
        if img is not None:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray)
            print(text)
        else:
            print(f"Failed to load the image {imgName}.")
    except Exception as e:
        print(f"An error occurred while processing the image: {e}")
else:
    print(f"The image file {imgName} does not exist or is not accessible.")
