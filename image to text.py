#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Asad Raja\AppData\Local\Programs\Python\Python310\Lib\site-packages\pytesseract"


# Open the image file
image = Image.open('image_1.jpg')

# Perform OCR using PyTesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)



