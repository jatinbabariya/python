import cv2
import pytesseract
import requests
from PIL import Image
from io import BytesIO
import os


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_url = "https://placehold.co/600x400.jpg"

response = requests.get(image_url)

if response.status_code == 200:
    image = Image.open(BytesIO(response.content))
    file_path = "img.jpg"

    if os.path.exists(file_path):
        os.remove(file_path)

    image.save(file_path)
    
    # Correctly read the image file using cv2.imread()
    imageRead = cv2.imread(file_path)
    
    # Pass the OpenCV image object directly to pytesseract
    text = pytesseract.image_to_string(imageRead)

    print(text)
else:
    print("Something went wrong")
