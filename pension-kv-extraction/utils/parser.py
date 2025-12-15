import re

def parse_ocr_data(ocr_data):
    """
    Parses raw Tesseract data into structured key-value pairs.
    """
    n_boxes = len(ocr_data['text'])
    
    # Reconstruct lines
    lines = {}
    for i in range(n_boxes):
        if int(ocr_data['conf'][i]) > 0:  # specific confidence threshold could be added
            (x, y, w, h) = (ocr_data['left'][i], ocr_data['top'][i], ocr_data['width'][i], ocr_data['height'][i])
            text = ocr_data['text'][i].strip()
            
            if not text:
                continue
                
            # Use line_num and block_num to group
            block_num = ocr_data['block_num'][i]
            line_num = ocr_data['line_num'][i]
            key = (block_num, line_num)
            
            if key not in lines:
                lines[key] = []
            lines[key].append(text)
            
    # Join words to form full text lines
    full_lines = [" ".join(words) for words in lines.values()]
    
    extracted_data = {}
    
    # regex patterns for expected fields
    patterns = {
        "Name": r"Name\s*[:]\s*(.*)",
        "DOB": r"DOB\s*[:]\s*([\d-]+)",
        "Pension ID": r"Pension\s*ID\s*[:]\s*(\w+)",
        "Account No": r"Account\s*NO\s*[:]\s*(\d+)"
    }
    
    for line in full_lines:
        for key, pattern in patterns.items():
            match = re.search(pattern, line, re.IGNORECASE)
            if match:
                extracted_data[key] = match.group(1).strip()
                
    return extracted_data
