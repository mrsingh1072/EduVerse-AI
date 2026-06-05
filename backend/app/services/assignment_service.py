from app.services.ai_client import ask_ai

def evaluate_assignment(
    assignment: str
):

    prompt = f"""
You are EduVerse AI Assignment Evaluator.

Evaluate the student's assignment.

Assignment:

{assignment}

Provide:

1. Marks out of 10
2. Strengths
3. Weaknesses
4. Suggestions for Improvement

Give feedback in a professional and student-friendly format.
"""

    return ask_ai(prompt)