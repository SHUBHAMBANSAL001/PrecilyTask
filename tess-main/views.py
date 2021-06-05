import os
import sys
import pytesseract
import cv2
import requests
from urllib.parse import unquote
from flask import request

IMAGEPATH = "data"

def read_ocr():
    """
    """
    content = request.json
    image = content['image']
    lang = content['lang']
    config = content['config']
    response = requests.get(image)
    image_name = unquote(os.path.basename(image))
    image_path = os.path.join(IMAGEPATH, image_name)
    with open(image_path, 'wb') as file:
        file.write(response.content)
    img_arr = cv2.imread(image_path)
    text = pytesseract.image_to_string(img_arr, lang=lang, config=config)
    if os.path.isfile(image_path):
        os.unlink(image_path)
    return {"text":text}

def root():
    """
        Root Endpoint
        Returns: Link to the API documentation
    """
    return {"API Documentation":''}
