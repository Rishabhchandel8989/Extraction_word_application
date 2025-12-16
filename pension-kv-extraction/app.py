import streamlit as st
import json
import os
from PIL import Image
import tempfile
from run_pipeline import process_form

st.set_page_config(page_title="Pension Form OCR", layout="wide")

st.title("Pension Form OCR Extraction")
st.markdown("Upload a form image to extract structured data.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save uploaded file to temp
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") 
    tfile.write(uploaded_file.read())
    temp_path = tfile.name
    tfile.close()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Original Image")
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)
        
    with col2:
        st.header("Extracted Data")
        with st.spinner("Processing..."):
            try:
                # Run pipeline
                extract_data = process_form(temp_path)
                
                # Clean up temp file
                os.unlink(temp_path)
                
                st.json(extract_data)
                
                # Option to download JSON
                json_str = json.dumps(extract_data, indent=4)
                st.download_button(
                    label="Download JSON",
                    data=json_str,
                    file_name="extraction_result.json",
                    mime="application/json"
                )
            except Exception as e:
                st.error(f"Error processing image: {e}")
