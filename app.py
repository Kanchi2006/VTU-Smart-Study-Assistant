import streamlit as st

from src.pdf_loader import upload_pdf
from src.file_manager import save_uploaded_file
from src.text_extractor import extract_text_from_pdf


st.set_page_config(
    page_title="VTU Smart Study Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 VTU Smart Study Assistant")


module = st.sidebar.selectbox(
    "Select Module",
    [
        "Notes Assistant",
        "PYQ Trend Analyzer"
    ]
)


if module == "Notes Assistant":

    st.header("📚 Notes Assistant")

    uploaded_files = upload_pdf()

    if uploaded_files:

        for file in uploaded_files:

            path = save_uploaded_file(
                file,
                "Notes"
            )

            st.success(
                f"{file.name} uploaded successfully"
            )

            text = extract_text_from_pdf(path)

            st.text_area(
                f"Preview - {file.name}",
                text[:1500],
                height=250
            )


elif module == "PYQ Trend Analyzer":

    st.header("📄 PYQ Trend Analyzer")

    uploaded_files = upload_pdf()

    if uploaded_files:

        for file in uploaded_files:

            path = save_uploaded_file(
                file,
                "PYQ"
            )

            st.success(
                f"{file.name} uploaded successfully"
            )

            text = extract_text_from_pdf(path)
            st.write(f"Characters extracted: {len(text)}")
            st.text_area(
                f"Preview - {file.name}",
                text[:1500],
                height=250
            )