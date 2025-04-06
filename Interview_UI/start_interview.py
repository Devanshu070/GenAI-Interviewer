import streamlit as st
import pre_questions
import llm_evaluator
from Interview_UI.show_result import show_result

def show_interview(MAX_QUESTIONS=5):
    st.title(f"🧠 {st.session_state.job_role} Interview")

    if st.session_state.question_count >= MAX_QUESTIONS:
        show_result()
        return

    st.subheader(f"Question {st.session_state.question_count + 1}")
    st.write(st.session_state.question)

    # 👇 Reset text input using a flag
    if st.session_state.get("clear_input", False):
        st.session_state.user_input = ""
        st.session_state.clear_input = False

    # 👇 Use key="user_input", but don't set value manually
    user_answer = st.text_area("Your Answer", key="user_input")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Submit"):
            if user_answer.strip():
                score, feedback = llm_evaluator.get_feedback(
                    st.session_state.job_role, st.session_state.question, user_answer
                )

                st.session_state.chat_history.append({
                    "question": st.session_state.question,
                    "answer": user_answer,
                    "score": score,
                    "feedback": feedback
                })

                st.session_state.question_count += 1

                if st.session_state.question_count < MAX_QUESTIONS:
                    st.session_state.question = pre_questions.get_question(
                        st.session_state.job_role, st.session_state.chat_history, st.session_state.retriever
                    )

                # ✅ Set the flag to clear on next run
                st.session_state.clear_input = True
                st.rerun()
            else:
                st.warning("Please provide an answer before submitting.")

    with col2:
        if st.button("Go Back"):
            st.session_state.page = "home"
            st.session_state.clear_input = True
            st.rerun()
