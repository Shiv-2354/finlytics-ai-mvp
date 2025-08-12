import streamlit as st
import pdfplumber
import pandas as pd

# -----------------------------
# App Title
# -----------------------------
st.set_page_config(page_title="Finlytics AI MVP", page_icon="📊")
st.title("📊 Finlytics AI – Financial Statement Extractor & Demo Database")

# -----------------------------
# PDF Upload Section
# -----------------------------
uploaded_file = st.file_uploader("📤 Upload a financial PDF report", type=["pdf"])

if uploaded_file is not None:
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            extracted_text = ""
            for page in pdf.pages[:5]:  # Limit to first 5 pages
                text = page.extract_text()
                if text:
                    extracted_text += text + "\n"

        if extracted_text.strip():
            st.subheader("📄 Extracted Text Preview:")
            st.text_area("First 3000 characters of extracted text:", extracted_text[:3000], height=300)

            # Example Q&A Section
            st.subheader("🤖 Ask a financial question (Demo Mode)")
            question = st.text_input("Type your question:")
            if question:
                st.success(f"Mock answer: Based on extracted text, your query '{question}' would be processed here.")

        else:
            st.error("No text could be extracted from the PDF.")

    except Exception as e:
        st.error(f"Error reading PDF: {e}")

# -----------------------------
# Demo CSV Database Section
# -----------------------------
st.subheader("📂 Demo Financial Database")
try:
    df = pd.read_csv("database.csv")  # Make sure your CSV file name matches
    st.dataframe(df)

    # Basic insights
    st.write("### 📊 Summary Statistics")
    st.write(df.describe())

    # Filter by State
    state_filter = st.selectbox("Filter by State:", options=["All"] + df['state_l'].unique().tolist())
    if state_filter != "All":
        st.dataframe(df[df['state_l'] == state_filter])

    # Top revenue companies
    top_n = st.slider("Show Top N Companies by Revenue", 1, len(df), 5)
    top_revenue = df.sort_values(by="revenue", ascending=False).head(top_n)
    st.write(f"### 💰 Top {top_n} Companies by Revenue")
    st.dataframe(top_revenue)

except FileNotFoundError:
    st.warning("No database.csv file found in repo.")
