from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from groq import Groq
import os
from dotenv import load_dotenv
import json
import custom_prompts
import re

# Load environment variables from .env
load_dotenv()

GROQCLOUD_API_KEY = os.getenv("GROQ_API_KEY")

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2,
    max_tokens=150,
    timeout=None,
    max_retries=2,
    api_key=GROQCLOUD_API_KEY
)

prompt = custom_prompts.question_generator_prompt()
parser = StrOutputParser()
chain = prompt | model | parser


# Function to get structured feedback
def generate_question(job_role, chat_questions, chat_answers, chat_scores):
    print(f"Job Role: {job_role}")
    print(f"Chat Questions: {chat_questions}")
    print(f"Chat Answers: {chat_answers}")
    print(f"Last Score: {chat_scores[-1]}")
    result = chain.invoke({'job_role': job_role, 'chat_questions': chat_questions, 'chat_answers': chat_answers, 'last_score': chat_scores[-1]})
    return result

def generate_question(job_role, chat_questions, chat_answers, chat_scores, retriever):
    print(f"[INFO] Generating questions for role: {job_role}")

    # Get resume context using RAG
    resume_context = ""
    try:
        relevant_docs = retriever.invoke(" ".join(chat_questions[-3:] + chat_answers[-3:]))  # Optional: last 3 answers as query
        resume_context = "\n".join([doc.page_content for doc in relevant_docs])
    except Exception as e:
        print(f"[ERROR] Retrieving context from resume failed: {e}")

    # Prepare inputs for the prompt
    inputs = {
        "job_role": job_role,
        "chat_questions": chat_questions,
        "chat_answers": chat_answers,
        "last_score": chat_scores[-1] if chat_scores else 5,
        "resume_context": resume_context
    }

    # Invoke LLM chain
    result = chain.invoke(inputs)
    return result

#  Testing Purposes
if __name__ == "__main__":
    from Interview_UI.pdf_vectorstore import create_vectorstore
    from Interview_UI.pdf_loader import load_pdf

    pdf_path = "sample_resume.pdf"
    with open(pdf_path, "rb") as f:
        docs = load_pdf(f)
        vectorstore = create_vectorstore(docs)
        retriever = vectorstore.as_retriever()

    question = generate_question(
        "AI Engineer",
        ["Tell me about yourself", "What is overfitting?"],
        ["I am an AI intern...", "Overfitting is..."],
        [7, 8],
        retriever
    )
    print("Generated Question:", question)
