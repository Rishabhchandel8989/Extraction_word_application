import pytesseract
import os
import shutil

# Set tesseract path if not in PATH
if not shutil.which("tesseract"):
    possible_paths = [
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    ]
    for path in possible_paths:
        if os.path.exists(path):
            pytesseract.pytesseract.tesseract_cmd = path
            break

def extract_text_bbox(image):
    return pytesseract.image_to_data(
        image,
        output_type=pytesseract.Output.DICT
    )
