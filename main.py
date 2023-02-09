import pytesseract
from PIL import Image
from pathlib import Path
import pyperclip
import os

image_path = Path(os.environ.get("IMAGE_PATH"))
text_list = []
for img in image_path.iterdir():
    print(img)
    image = Image.open(img)
    pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(image)
    text_list.append(text)

required = " ".join(map(str, text_list))


def copy_text(some_text: str):
    pyperclip.copy(some_text)
    print("Text has been copied to clipboard.")


copy_text(required)

print(required)
