import easyocr
import os
import requests
from PIL import Image
from io import BytesIO

image_url = "https://placehold.co/600x400.jpg"
reader = easyocr.Reader(['en'])
response = requests.get(image_url)

if response.status_code == 200:
    file_path = "img.jpg"
    image = Image.open(BytesIO(response.content))
    if os.path.exists(file_path):
        os.remove(file_path)

    image.save(file_path)
    

    result = reader.readtext(file_path)

    for detection in result:
        text = detection[1]
        print(text)

    # result = reader.readtext(file_path, detail = 0)
    # print(result)
else:
    print("Something went wrong")