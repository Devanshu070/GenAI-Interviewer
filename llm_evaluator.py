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
    max_tokens=300,
    timeout=None,
    max_retries=2,
    api_key=GROQCLOUD_API_KEY
)

prompt = custom_prompts.evaluate_answer_prompt()
if prompt is None:
    raise ValueError("Error: `evaluate_answer_prompt()` returned None!")

parser = StrOutputParser()
chain = prompt | model | parser


# Function to get structured feedback
def get_feedback(job_role: str, question: str, answer: str):
    result = chain.invoke({'job_role': job_role, 'question': question, 'answer': answer})

    # Try parsing as JSON first (if LLM responds in JSON format)
    try:
        response_json = json.loads(result)
        score = response_json.get("score", "N/A")
        feedback = response_json.get("feedback", "No feedback provided.")
    except json.JSONDecodeError:
        # If JSON parsing fails, fall back to regex
        match = re.search(r"Score:\s*(\d+)\s*Feedback:\s*(.*)", result, re.DOTALL)
        if match:
            score = int(match.group(1))
            feedback = match.group(2).strip()
        else:
            score = "N/A"
            feedback = "Could not parse feedback.."

    return score, feedback


# Example test
if __name__ == "__main__":
    test_score, test_feedback = get_feedback(
        'Software Engineer',
        'What are the basic principles of OOP?',
        'Basic properties are inheritance, encapsulation, polymorphism, and abstraction. Inheritance allows a class to acquire features from another class. Encapsulation hides unnecessary details. Polymorphism allows multiple forms. Abstraction hides implementation details while showing functionality.'
    )
    print(f"Score: {test_score}")
    print(test_feedback)
    test_score, test_feedback = get_feedback(
        'Software Engineer',
        'What are the basic principles of OOP?',
        'Basic properties are inheritance. Inheritance allows a class to acquire features from another class.'
    )
    print(f"Score: {test_score}")
    print(test_feedback)
    test_score, test_feedback = get_feedback(
        'Software Engineer',
        'What are the basic principles of OOP?',
        'TADA .'
    )
    print(f"Score: {test_score}")
    print(test_feedback)