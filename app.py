
import streamlit as st
import pdfplumber

st.set_page_config(page_title="Finlytics AI", layout="wide")

st.title("📊 Finlytics AI – PDF Financial Extractor")

uploaded_file = st.file_uploader("Upload a financial PDF", type="pdf")

if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    st.subheader("Extracted Text:")
    st.text_area("Raw Text", text[:3000], height=300)

    query = st.text_input("Ask a financial question (demo):")

    if query:
        st.subheader("Answer (Mock):")
        if "eps" in query.lower():
            st.write("EPS in 2022 was ₹3.12 vs ₹2.78 in 2021.")
        elif "net profit" in query.lower():
            st.write("Net profit for 2022 was ₹15.2 Cr.")
        elif "revenue" in query.lower():
            st.write("Revenue rose to ₹134 Cr in 2022 from ₹120 Cr in 2021.")
        else:
            st.write("Sorry, this is a demo and cannot answer that.")
