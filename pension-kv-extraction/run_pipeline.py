# from ocr.image_preprocess import preprocess_image
# from ocr.ocr_engine import extract_text_bbox

# # image = preprocess_image("data/raw_images/form1.jpg")
# image = preprocess_image("F:\NLP Project\pension-kv-extraction\data\data\raw_images\form1.jpg")
# ocr_data = extract_text_bbox(image)

# ...existing code...
from ocr.image_preprocess import preprocess_image
from ocr.ocr_engine import extract_text_bbox
import os

# ...existing code...
# image = preprocess_image("data/raw_images/form1.jpg")
image_path = r"F:\NLP Project\pension-kv-extraction\data\data\raw_images\form1.jpg"
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image not found: {image_path}")

image = preprocess_image(image_path)
import json

from utils.parser import parse_ocr_data

ocr_data = extract_text_bbox(image)
# print(ocr_data) # Reduced verbosity

# Parse data
extracted_data = parse_ocr_data(ocr_data)
print("Extracted Data:", json.dumps(extracted_data, indent=4))

# Save to JSON
output_path = r"output/predication result.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w') as f:
    json.dump(extracted_data, f, indent=4)
print(f"Results saved to {output_path}")
# ...existing code...