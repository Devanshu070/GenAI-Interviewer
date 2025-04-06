from langchain_core.prompts import PromptTemplate

def evaluate_answer_prompt():
    prompt = PromptTemplate(
        template="""You are an expert technical evaluator for {job_role} interviews. 
        Evaluate the candidate's response using these parameters:

        1. **Technical Accuracy (3 points)** - Is the answer factually correct and relevant?
        2. **Communication and Clarity (2 points)** - Is the response well-structured and easy to understand?
        3. **Completeness (5 points)** - Does it fully answer the question? 

        **Scoring Rules:**
        - Assign **0-3 points** for Technical Accuracy.
        - Assign **0-2 points** for Communication and Clarity.
        - Assign **0-5 points** for Completeness
        - The total score should be between **0 and 10**.
        - For answers that are completely off-topic or irrelevant, assign a score of **0**.
        - For answers that are completely correct and well-structured, assign a score of **10**.
        - For answers say it has 1/4 of the completeness, assign 5x1/4=1.25, and round it to 1.5.
        Given the question: {question}
        And the candidate's answer: {answer}  

        Your response **must be in valid JSON format**:

        ```json
        {{
          "score": <score between 0-10 based on the scoring rules>,
          "feedback": [
            "Technical Accuracy: <detailed evaluation>",
            "Communication and Clarity: <detailed evaluation>",
            "Completeness: <detailed evaluation>"
          ]
        }}
        ```
        **Do not include any text outside of the JSON format.**
        """,
        input_variables=['job_role', 'question', 'answer']
    )
    return prompt


def question_generator_prompt():
    prompt = PromptTemplate(
        template="""
        You are an expert technical interviewer. Based on the candidate's previous performance and resume context, generate the next **interview question** by following these rules:

        1. If the candidate's last_score is 6 or above:
        - Ask a follow-up question that builds on their last answer or goes deeper into a related topic.

        2. If the candidate's last_score is below 6:
        - Ask a fundamental concept related to the {job_role} that hasn't been asked yet.
        - If resume_context is available, you can instead ask something based on their experience or skills from the resume.

        3. **Do NOT repeat any previous questions** in {chat_questions}.

        4. The question should be suitable for someone with **0-1 years of experience** in the {job_role}.

        5. **IMPORTANT**: Only return a single interview question as a plain string. Do **NOT** include explanations, commentary, reasoning, or formatting like "Since the score is...".

        Resume context (optional):
        {resume_context}

        Input:
        - job_role: {job_role}
        - chat_questions: {chat_questions}
        - chat_answers: {chat_answers}
        - last_score: {last_score}

        Output Format:
        "Your next interview question here."

        Question:""",
                input_variables=["job_role", "chat_questions", "chat_answers", "last_score", "resume_context"]
            )
    return prompt