import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)

def tutor_response(question: str):

    prompt = f"""
You are EduVerse AI Tutor.

Rules:
1. Explain in simple student-friendly language.
2. Give real-life examples.
3. Explain step by step.
4. End with a short quiz question.

Student Question:
{question}
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-oss-20b:free",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    result = response.json()

    if "choices" in result:
        return result["choices"][0]["message"]["content"]

    return str(result)