import io

if uploaded_file is not None:
    try:
        with pdfplumber.open(io.BytesIO(uploaded_file.read())) as pdf:
            text = ''
            for i, page in enumerate(pdf.pages[:5]):
                text += page.extract_text() + "\n"

        # Reset the file pointer after reading for further uses
        uploaded_file.seek(0)

        st.subheader("Extracted Text:")
        st.text_area("Text Preview", text[:3000], height=300)

        query = st.text_input("Ask a question (mock example):")

        if query:
            st.write("This is a demo. You asked:", query)

    except Exception as e:
        st.error(f"Failed to process PDF. Make sure it has selectable text. Error: {e}")
