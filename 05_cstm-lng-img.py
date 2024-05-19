import cv2
import pytesseract
import numpy as np
import os

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
imgName = "xxx.xxx"
outputFile = "output.txt"
if os.path.exists(imgName) and os.path.isfile(imgName):
    try:
        img = cv2.imread(imgName)   
        if img is not None:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5,5), 0)
            bin_image = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31,2)
            kernel = np.ones((1,1), np.uint8)
            finalImg = cv2.dilate(bin_image,kernel, iterations=1)
            finalImg = cv2.erode(img, kernel, iterations=1)
            text = pytesseract.image_to_string(finalImg, lang='guj+eng')
            print(text)
            with open(outputFile, 'w', encoding="utf-8") as text_file:
                text_file.write(text)
            print(f"Extracted text has been saved to {outputFile}.")
        else:
            print(f"Failed to load the image {imgName}.")
    except Exception as e:
        print(f"An error occurred while processing the image: {e}")
else:
    print(f"The image file {imgName} does not exist or is not accessible.")