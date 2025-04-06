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

# Load your Groq API key
GROQCLOUD_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize the Groq model (Llama 3.1)
model = ChatGroq(
    model="llama-3.1-8b-instant",  # You can replace with your specific model
    temperature=0.2,
    max_tokens=150,
    timeout=None,
    max_retries=2,
    api_key=GROQCLOUD_API_KEY
)

# Load the custom judge prompt
def load_judge_prompt():
    try:
        with open("judge_prompt.txt", "r") as file:
            judge_prompt = file.read()
        return judge_prompt
    except FileNotFoundError:
        print("Error: judge_prompt.txt not found.")
        return None

# Prepare the judge prompt
def prepare_judge_prompt(job_role, chat_questions, chat_answers):
    # Load the prompt template from the file
    judge_prompt = load_judge_prompt()

    if not judge_prompt:
        return None

    # Replace placeholders in the prompt template with actual data
    judge_prompt = judge_prompt.format(
        job_role=job_role,
        chat_questions="\n".join(chat_questions),
        chat_answers="\n".join(chat_answers)
    )

    return judge_prompt

# Function to evaluate the candidate's response using the Groq model
def evaluate_candidate(job_role, chat_questions, chat_answers):
    judge_prompt = prepare_judge_prompt(job_role, chat_questions, chat_answers)

    if not judge_prompt:
        return None

    # Use the Groq model to process the prompt
    parser = StrOutputParser()

    # Groq model chain: Prepare and process the prompt through the model and parser
    chain = judge_prompt | model | parser

    # Get the result from the chain
    result = chain.run()

    return result

# Example of how to use the evaluate_candidate function
if __name__ == "__main__":
    # Sample data (for testing)
    job_role = "AI Engineer"
    chat_questions = [
        "Tell me about yourself.",
        "What is overfitting?",
    ]
    chat_answers = [
        "I am an AI intern working with machine learning models...",
        "Overfitting occurs when a model learns too much from the training data...",
    ]

    # Evaluate the candidate's responses
    result = evaluate_candidate(job_role, chat_questions, chat_answers)
    
    if result:
        print("Evaluation Result:", result)
