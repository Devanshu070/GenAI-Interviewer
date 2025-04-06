import streamlit as st
from Interview_UI.home import show_home
from Interview_UI.start_interview import show_interview
# from Interview_UI.show_result import show_result


st.set_page_config(page_title="AI Interview", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "home"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "question_count" not in st.session_state:
    st.session_state.question_count = 0

MAX_QUESTIONS = 5

# --- Router ---  Will be executed when the page is loaded rerun
if st.session_state.page == "home":
    show_home()
elif st.session_state.page == "interview":
    show_interview(MAX_QUESTIONS)
