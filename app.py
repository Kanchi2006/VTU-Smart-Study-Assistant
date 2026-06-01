import streamlit as st

st.set_page_config(
    page_title="VTU Smart Study Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 VTU Smart Study Assistant")

st.markdown("""
Welcome to VTU Smart Study Assistant.

Features:
- Upload VTU Notes
- Ask Questions
- Generate 5-Mark Answers
- Generate 10-Mark Answers
- Generate Quiz Questions
- Generate Revision Notes
""")

st.success("Project setup completed successfully!")