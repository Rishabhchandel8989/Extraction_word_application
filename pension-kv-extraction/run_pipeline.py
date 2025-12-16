
from ocr.image_preprocess import preprocess_image
from ocr.ocr_engine import extract_text_bbox
import os
import json
from utils.parser import parse_ocr_data

def process_form(image_path):
    """
    Runs the OCR pipeline on the given image path.
    Returns the extracted data and the path where it was saved (if relevant).
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    image = preprocess_image(image_path)
    ocr_data = extract_text_bbox(image)
    extracted_data = parse_ocr_data(ocr_data)
    
    return extracted_data

if __name__ == "__main__":
    # Default behavior for terminal execution
    image_path = r"F:\NLP Project\pension-kv-extraction\data\data\raw_images\form12.jpg"
    
    try:
        extracted_data = process_form(image_path)
        print("Extracted Data:", json.dumps(extracted_data, indent=4))

        output_path = r"output/predication result.json"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(extracted_data, f, indent=4)
        print(f"Results saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")
