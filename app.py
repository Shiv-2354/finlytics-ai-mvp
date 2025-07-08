import streamlit as st
import pdfplumber

st.title("📊 Finlytics AI – PDF Financial Extractor (Safe Demo)")

uploaded_file = st.file_uploader("Upload a PDF report (max 5 pages)", type="pdf")

if uploaded_file is not None:
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            text = ''
            for i, page in enumerate(pdf.pages[:5]):
                text += page.extract_text() + "\\n"

        st.subheader("Extracted Text:")
        st.text_area("Text Preview", text[:3000], height=300)

        query = st.text_input("Ask a question (mock example):")

        if query:
            st.write("This is a demo. You asked:", query)

    except Exception as e:
        st.error("Failed to process PDF. Make sure it has selectable text.")
