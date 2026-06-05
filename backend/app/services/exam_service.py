from app.services.ai_client import ask_ai

def generate_exam(
    subject: str,
    difficulty: str,
    questions: int
):

    prompt = f"""
You are EduVerse AI Exam Generator.

Generate an exam paper.

Subject:
{subject}

Difficulty:
{difficulty}

Total Questions:
{questions}

Format:

Part A:
MCQ Questions

Part B:
Short Answer Questions

Part C:
Long Answer Questions

Provide answer key at the end.

Make the paper professional and suitable for college students.
"""

    return ask_ai(prompt)