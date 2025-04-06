import streamlit as st
import pre_questions
import llm_evaluator

# --- Result Page ---
def show_result(MAX_QUESTIONS=5):
    st.success("✅ Interview Completed")

    total_score = sum(item["score"] for item in st.session_state.chat_history)
    avg_score = total_score / MAX_QUESTIONS

    for idx, item in enumerate(st.session_state.chat_history, 1):
        st.write(f"**Q{idx}:** {item['question']}")
        st.write(f"**Your Answer:** {item['answer']}")
        st.write(f"**Score:** {item['score']}/10")
        st.write("**Feedback:**")
        for fb in item["feedback"]:
            st.markdown(f"- {fb}")
        st.markdown("---")

    st.write(f"### Total Score: {total_score} / {MAX_QUESTIONS * 10}")
    st.write(f"### Average Score: {avg_score:.2f} / 10")

    if st.button("🔁 Start Again"):
        for key in ["page", "chat_history", "question", "question_count"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()