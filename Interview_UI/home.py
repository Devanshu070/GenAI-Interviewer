import streamlit as st
import pre_questions
from Interview_UI.pdf_loader import load_pdf
from Interview_UI.pdf_vectorstore import create_vectorstore

# --- Home Page ---
def show_home():
    st.title("🎯 AI-Powered Interview")
    st.write("Select a role and start the interview.")
    role = st.selectbox("Choose a Job Role", ["AI Engineer", "Software Engineer", "Data Scientist", "Prompt Engineer"])

    st.markdown("---")

    uploaded_file = st.file_uploader("Upload your Resume", type="pdf")
    if uploaded_file is not None:
        docs = load_pdf(uploaded_file)
        if docs:
            st.session_state.pdf_docs = docs
            vectorstore = create_vectorstore(docs)
            st.session_state.retriever = vectorstore.as_retriever()

    st.markdown("---")

    if st.button("Start Interview"):
        st.session_state.page = "interview"
        st.session_state.job_role = role
        st.session_state.chat_history = []
        st.session_state.question_count = 0
        st.session_state.question = pre_questions.get_question(role, [], st.session_state.retriever)
        st.rerun()