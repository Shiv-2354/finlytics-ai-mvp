import streamlit as st
import pdfplumber
import io

st.write("App started") 
st.title("📊 Finlytics AI – PDF Financial Extractor (Safe Demo)")

uploaded_file = st.file_uploader("Upload a PDF report (max 5 pages)", type="pdf")

if uploaded_file is not None:
    st.write(f"Uploaded file: {uploaded_file.name}, size: {uploaded_file.size} bytes")
    try:
        with pdfplumber.open(io.BytesIO(uploaded_file.read())) as pdf:
            text = ''
            for i, page in enumerate(pdf.pages[:5]):
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        uploaded_file.seek(0)  # Reset file pointer after reading

        st.subheader("Extracted Text:")
        st.text_area("Text Preview", text[:3000], height=300)

        query = st.text_input("Ask a question (mock example):")

        if query:
            st.write("This is a demo. You asked:", query)

    except Exception as e:
        st.error(f"Failed to process PDF. Make sure it has selectable text. Error: {e}")
