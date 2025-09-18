# Streamlit frontend for user interaction

import streamlit as st
import requests

st.title("SmartSDLC Dashboard")

uploaded_pdf = st.file_uploader("Upload Requirements PDF", type="pdf")
if uploaded_pdf:
    st.write("Extracting requirements...")
    files = {"pdf": uploaded_pdf.getvalue()}
    response = requests.post("http://localhost:8000/requirements/extract", files=files)
    st.json(response.json())

prompt = st.text_input("Enter natural language code prompt:")
if prompt and st.button("Generate Code"):
    response = requests.post("http://localhost:8000/codegen/generate", json={"prompt": prompt})
    st.code(response.json().get("code", "No code generated."))