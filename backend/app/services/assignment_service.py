from app.services.ai_client import ask_ai

def evaluate_assignment(
    assignment: str
):

    prompt = f"""
You are an experienced college professor.

Evaluate the following student assignment:

{assignment}

Provide:

1. Marks out of 10
2. Strengths
3. Weaknesses
4. Suggestions
5. Final Remark

Do not ask for more information.
Assume this is the complete submission.
"""

    return ask_ai(prompt)