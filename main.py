import pytesseract
from PIL import Image
from pathlib import Path
import pyperclip
import shutil
from datetime import datetime
import os
import time


def read_image_text() -> str:
    image_path = Path(os.environ.get("IMAGE_PATH"))
    text_list = []
    for img in image_path.iterdir():
        print(img)
        image = Image.open(img)
        pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        text = pytesseract.image_to_string(image)
        text_list.append(text)
    required = " ".join(map(str, text_list))
    return required


def save_to_file(content: str):
    file_name = "result.txt"
    image_path = Path(os.environ.get("IMAGE_PATH"))/file_name
    txt_file = image_path
    txt_file.parent.mkdir(parents=True, exist_ok=True)
    with txt_file.open('w') as f:
        f.write(content)


def copy_text(some_text: str):
    pyperclip.copy(some_text)
    print("Text has been copied to clipboard.")


def move_files(src, dest):
    try:
        shutil.move(src, dest)
    except Exception as e:
        print("An error occurred: ", e)


result = read_image_text()
save_to_file(result)
copy_text(result)

src_dir = Path(os.environ.get("IMAGE_PATH"))
dest_dir = Path(os.environ.get("DEST_PATH"))
current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
dest_folder = dest_dir / current_date
dest_folder.mkdir(parents=True, exist_ok=True)

files = src_dir.iterdir()
time.sleep(1)
for file in files:
    src_file = file
    dest_file = dest_folder / file.name
    move_files(src_file, dest_file)
