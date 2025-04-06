import random
import question_generator

# Sample job roles and questions
def get_question(job_role, chat_history, retriever):
    
    if not chat_history:
        question = "Hi, can you tell me about yourself?"
    else:

        # Extract separate lists of questions and scores
        chat_questions = [chat["question"] for chat in chat_history]
        chat_answers = [chat["answer"] for chat in chat_history]
        chat_scores = [int(chat["score"]) for chat in chat_history]

        return question_generator.generate_question(job_role, chat_questions, chat_answers, chat_scores, retriever)
    return question
