> - [Common Library](#common-library)
> - [01_opencv.py](#Required-Libraries-for-OpenCV)
> - [02_easyocr.py](#Required-Libraries-for-easyocr)
> - [03_custom-img.py](#custom-image)
> - [04_cstm-adv-img.py](#custom-image-advance)
> - [05_cstm-lng-img.py](#custom-language-image)

## Common Library

- Image Download Library

  ### Pillow

  ```bash
  pip install requests pillow
  ```

## Required Libraries for OpenCV

- Image reader libraries

  ### Tesseract and OpenCV

  ```bash
  pip install pytesseract
  pip install opencv-python
  ```

  You'll require the following software

  - [Tesseract - Windows](https://github.com/UB-Mannheim/tesseract/wiki)
  - [Other Platforms](https://tesseract-ocr.github.io/tessdoc/Installation.html)

- Finally run the code

  ```bash
  python 01_opencv.py
  ```

## Required Libraries for easyOcr

- easyOCR

  ```bash
  pip install torch torchvision torchaudio
  pip install easyocr
  ```

- Finally run the code

  ```bash
  python 02_easyocr.py
  ```

## Custom Image

- Put the image in root directory of this project
- Replace the name and extension of image with "xxx.xxx"
- Finally run the code

  ```bash
  python 03_custom-img.py
  ```

## Custom Image Advance

- Put the image in root directory of this project
- Replace the name and extension of image with "xxx.xxx"
- Finally run the code

  ```bash
  python 04_cstm-adv-img.py
  ```

## Custom Language Image

- Put the image in root directory of this project
- Replace the name and extension of image with "xxx.xxx"
- Finally run the code
- [Download Language Pack](https://github.com/tesseract-ocr/tessdata/tree/main)
- On Linux :
  - Move these files to /usr/share/tesseract-ocr/4.00/tessdata/ (you may need sudo privileges).
- On MacOS:
  - Move these files to /usr/local/share/tessdata/
- on Windows:
  - Move these files to C:\Program Files\Tesseract-OCR\tessdata
- Replace the name of language or add language with lang='guj+eng'
- Check installed language using this code
  ```bash
    tesseract --list-langs
  ```
- Finally run the code
  ```bash
    python 05_cstm-lng-img.py
  ```
