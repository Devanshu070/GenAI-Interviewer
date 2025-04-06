import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
import os

def load_pdf(uploaded_file):
    if uploaded_file is not None:
        with open("temp_uploaded_file.pdf", "wb") as f:
            f.write(uploaded_file.read())

        loader = PyPDFLoader("temp_uploaded_file.pdf")
        docs = loader.load()

        st.success(f"✅ Loaded {len(docs)} page(s) from uploaded PDF.")
        st.session_state.pdf_docs = docs

        return docs
    return None